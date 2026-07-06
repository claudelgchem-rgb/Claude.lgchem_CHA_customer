# CIRV 하니스 — 기업–아이템 연관성 인텔리전스

**CIRV** = **C**ompany **I**ntelligence · **R**elevance · **V**erification

사용자가 제공한 **기업 리스트**와 **관심 아이템(기술·물질·플랫폼) 리스트**를 입력받아,
각 기업의 사업·연구·뉴스/동향을 **근거 기반**으로 조사하고, 아이템과의 **연관성**을 판정한 뒤,
모든 사실의 신뢰도를 **상/중/하**로 검증하여 "어떤 기업이 어떤 아이템과 연관되는가"를
**감사(audit) 가능한 형태**로 산출하는 다중 에이전트 하니스입니다.

이 저장소는 해당 하니스를 **Claude Code 서브에이전트**로 배포한 구현체입니다(스펙 §10).

---

## 0. PRIME DIRECTIVE

> **"일을 절대 미루지 않고, 가능한 최선을 다해 업무 수행에 집중한다."**

모든 에이전트는 미루기(deferral)를 금지하며, 가용 도구(웹 검색·원문 페치·공식 홈페이지·IR/공시·특허 DB·논문·규제기관)를
소진한 뒤에만 판단합니다. 확인 불가는 "무엇을 어떻게 시도해 왜 실패했는지"를 남긴 **정직한 갭**으로만 기록합니다.
각 에이전트 정의 파일 상단에 이 규칙이 복제되어 드리프트를 방지합니다.

---

## 구성

```
.claude/agents/
  orchestrator.md        ① 오케스트레이터  — 작업 분해·분배, 재조사 루프, PRIME DIRECTIVE 집행
  research_agent.md      ② 조사관 (필수)   — 기업별 5영역 조사, 증거 카드 명문화
  relevance_agent.md     ③ 연관성 분석관   — 증거 ↔ 아이템 대조, 연관유형·연관도 판정
  verification_agent.md  ④ 검증관 (필수)   — 증거 카드만으로 상/중/하 판정, 반려
  report_agent.md        ⑤ 리포트 작성관   — 최종 종합 리포트 생성
schemas/
  evidence_card.schema.json         증거 카드 스키마 (§5.1)
  relevance_record.schema.json      연관성 레코드 스키마 (§5.2)
  verification_record.schema.json   검증 레코드 스키마 (§5.3)
ui/
  evidence_dashboard.py  §8 증거 UI (Streamlit) — 필터·색상 코딩(상=녹/중=주황/하=적)
examples/
  input_template.yaml               호출 입력 템플릿 (§1.2)
  sample_evidence_cards.json        스키마·UI 렌더 확인용 SAMPLE (실데이터 아님)
out/                     런타임 산출물 (gitignore) — 조사·검증·연관·리포트 결과
```

## 아키텍처

```
사용자 입력(기업+아이템)
        │
   ① 오케스트레이터 ──분배──▶ ② 조사관 ──증거 카드──▶ 증거 UI
        ▲                                    │        │
        │                                    ▼        ▼
   (재조사 루프) ◀──반려── ④ 검증관 ◀───┘   ③ 연관성 분석관
        │                    │                        │
        └───────────────▶ ⑤ 리포트 작성관 ◀───────────┘ ──▶ 최종 리포트 + 감사 데이터셋
```

- **필수 에이전트**: ② 조사관, ④ 검증관.
- **추가 에이전트**(완결 보장): ① 오케스트레이터, ③ 연관성 분석관, ⑤ 리포트 작성관.

## 사용법

### 1) 입력 준비
`examples/input_template.yaml`를 복사해 기업/아이템/옵션을 채웁니다.

### 2) 하니스 실행
Claude Code에서 오케스트레이터를 호출합니다:

```
> cirv-orchestrator 서브에이전트로 아래 입력을 조사해줘
  companies: [ ... ]
  items: [ ... ]
  options: { recency_window_months: 12, min_sources_per_claim: 2, match_threshold: "중" }
```

오케스트레이터가 조사관→검증관→(재조사 루프)→연관성 분석관→리포트 작성관을 순서대로 지휘하고,
결과를 `out/`에 씁니다.

### 3) 산출물 확인
- `out/report.md` — 최종 종합 리포트 (§5.4)
- `out/evidence_cards.json` / `out/verification_records.json` / `out/relevance_records.json` — 감사 데이터셋

### 4) 증거 UI 실행
```bash
pip install -r requirements.txt
streamlit run ui/evidence_dashboard.py
```
기업/카테고리/검증등급/아이템 필터와 색상 코딩으로 근거를 검토합니다.
(데이터가 없으면 `cp examples/sample_evidence_cards.json out/evidence_cards.json`로 렌더만 미리 확인 가능)

## 데이터 흐름 & 산출물

| 산출물 | 생성 주체 | 경로 | 스키마 |
|--------|-----------|------|--------|
| 증거 카드 | ② 조사관 | `out/evidence_cards.json` | `schemas/evidence_card.schema.json` |
| 검증 레코드 | ④ 검증관 | `out/verification_records.json` | `schemas/verification_record.schema.json` |
| 연관성 레코드 | ③ 연관성 분석관 | `out/relevance_records.json` | `schemas/relevance_record.schema.json` |
| 최종 리포트 | ⑤ 리포트 작성관 | `out/report.md` | — (§5.4 구조) |

## 신뢰도 루브릭 (검증관, §7)

| 등급 | 기준 요약 |
|------|-----------|
| **상** | 1차 공식 출처 + 원문 접근 + 근거 발췌 + 최신성/24개월 이내, 가능시 2+ 교차확인 |
| **중** | 신뢰 높은 2차 출처, 단일이나 검증·접근 가능, 24–48개월 또는 부분 교차확인 |
| **하** | 블로그·미상·링크 소실, 출처 상충, 추론 과다, 48개월 초과 동향/발췌 없는 주장 |

> 연관 판정을 좌우하는 '하중 큰 사실'이 **하**이거나 근거·출처 누락이면 `reject_reinvestigate`로 반려 → 재조사 루프(최대 3회).

## 원칙 (모든 에이전트 공통, §3)

1. PRIME DIRECTIVE 최우선.
2. 근거 없는 주장 금지 — 모든 진술은 `evidence_id`로 추적 가능.
3. 출처 위계 준수(1차 > 2차 > 3차; 3차 채택 시 '하').
4. 저작권 안전 발췌(핵심만 짧게, URL 병기, 나머지는 요약).
5. 산출 언어는 한국어(원문 인용·기업명·특허번호·논문 제목은 원어 유지).
6. 날짜·시점 명시(발행일 + 조사 일시).
7. 추론은 반드시 '추론' 표기.
8. 정직성 — 지어내지 않고, 확인 불가는 시도 내역 포함 갭으로 명문화.
