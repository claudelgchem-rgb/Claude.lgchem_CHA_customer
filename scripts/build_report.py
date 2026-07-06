#!/usr/bin/env python3
"""
CIRV 리포트 작성관 (⑤) — 결정론적 생성기
검증된 감사 데이터(out/*.json)에서 최종 리포트를 생성한다. 모든 사실은 evidence_id로 추적 가능.
산출: reports/CIRV_report_2026-07-06.md
"""
from __future__ import annotations
import json, os
from collections import defaultdict, Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "out")
RUN_DATE = "2026-07-06"
LEVEL_RANK = {"하": 1, "중": 2, "상": 3}
CATS = ["사업분야", "연구분야", "뉴스·동향", "IP·특허", "파트너십·M&A"]

evidence = json.load(open(f"{OUT}/evidence_cards.json", encoding="utf-8"))
verrecs = json.load(open(f"{OUT}/verification_records.json", encoding="utf-8"))
relrecs = json.load(open(f"{OUT}/relevance_records.json", encoding="utf-8"))
match = json.load(open(f"{OUT}/match_table.json", encoding="utf-8"))

def code_of(eid):
    return eid.split("-")[1]  # EV-<CODE>-nnn

ver = {r["evidence_id"]: r for r in verrecs}
ev_by_code = defaultdict(list)
code_name = {}
for c in evidence:
    code = code_of(c["evidence_id"])
    ev_by_code[code].append(c)
    code_name.setdefault(code, c["company"])
rel_by_code = defaultdict(dict)
for r in relrecs:
    rel_by_code[r["_code"]][r["item"]] = r

codes = sorted(ev_by_code.keys(), key=lambda k: code_name[k].lower())
ITEMS = ["mTG", "ADC", "Collagen"]
GRADE_EMOJI = {"상": "🟢상", "중": "🟠중", "하": "🔴하", None: "—"}


def esc(s):
    return (s or "").replace("|", "\\|").replace("\n", " ").strip()


def grade(eid):
    v = ver.get(eid, {})
    return v.get("verified_confidence")


out = []
w = out.append

# ── 헤더 ──
w(f"# CIRV 최종 리포트 — 기업–아이템 연관성 인텔리전스\n")
w(f"**조사일**: {RUN_DATE} · **하니스**: CIRV (Company Intelligence · Relevance · Verification)\n")
w("**아이템**: mTG (microbial transglutaminase) · ADC (Antibody-Drug Conjugate) · Collagen (콜라겐/젤라틴)  ")
w("**옵션**: recency_window 12개월 · min_sources_per_claim 2 · match_threshold 중\n")
w("> 본 리포트의 모든 사실은 증거 카드(`evidence_id`)로 추적 가능하며, 각 사실에는 검증관(④)의 상/중/하 등급이 부여되어 있다. "
  "감사 데이터셋(커밋됨): `reports/data/evidence_cards.json`(증거) · `reports/data/verification_records.json`(검증) · "
  "`reports/data/relevance_records.json`(연관성) · `reports/data/match_table.json`(매칭). "
  "대화형 검토: `streamlit run ui/evidence_dashboard.py`.\n")

# ── 1. 요약 ──
w("## 1. 요약\n")
vdist = Counter(r.get("verified_confidence") for r in verrecs)
w(f"- **조사 기업**: {len(codes)}개 · **관심 아이템**: {len(ITEMS)}개 · **총 증거 카드**: {len(evidence)}개")
w(f"- **검증 신뢰도 분포**: 상 {vdist.get('상',0)} · 중 {vdist.get('중',0)} · 하 {vdist.get('하',0)} "
  f"(전건 accept, 재조사 반려 3건은 재조사 루프 후 해소)")
mpi = match["summary"]["matches_per_item"]
w(f"- **아이템별 연관(≥중) 기업 수**: Collagen **{mpi['Collagen']}** · mTG **{mpi['mTG']}** · ADC **{mpi['ADC']}**\n")

w("### 아이템별 매칭 한눈표\n")
w("| 아이템 | 연관(≥중) 기업 수 | 상세 |")
w("|--------|:---:|------|")
w(f"| **Collagen** | {mpi['Collagen']}/48 | 콜라겐·젤라틴이 본업(직접사업/직접연구)인 기업 다수 + 바이오프린팅·배양육 '인접·응용' |")
w(f"| **mTG** | {mpi['mTG']}/48 | 대부분 자사 소재가 mTG 가교의 *기질*이거나 자사 특허에 mTG 명시. 효소 제조사는 아님 |")
w(f"| **ADC** | {mpi['ADC']}/48 | 항체-약물 접합체는 이 기업군과 대체로 무관. 제약 계열만 연관 |\n")

# ── 2. 아이템별 연관 기업 테이블 ──
w("## 2. 아이템별 연관 기업 테이블 (match_threshold=중 이상)\n")
for item in ITEMS:
    rows = [r for r in match["match"][item] if r["match"]]
    w(f"### {item} — 연관 {len(rows)}개사\n")
    if not rows:
        w("_해당 없음._\n"); continue
    w("| 기업 | 연관유형 | 연관도 | 근거 검증등급 | 핵심 근거(evidence_id) |")
    w("|------|----------|:---:|:---:|------|")
    for r in rows:
        rec = rel_by_code[r["code"]][item]
        eids = ", ".join(rec.get("supporting_evidence_ids", [])[:3])
        w(f"| {esc(r['company'])} | {r['relevance_type']} | {r['relevance_level']} "
          f"| {GRADE_EMOJI.get(r['verified_grade'])} | {eids} |")
    w("")

# ── 3. 기업별 상세 dossier ──
w("## 3. 기업별 상세 (5영역 조사 사실 + 검증등급 + 아이템 판정)\n")
w("각 사실 뒤 대괄호는 검증등급(상/중/하). 아이템 판정은 연관성 분석관(③) 산출.\n")
for comp_code in codes:
    cards = ev_by_code[comp_code]
    comp = code_name[comp_code]
    w(f"### {esc(comp)}\n")
    # 아이템 판정 라인
    verd = []
    for item in ITEMS:
        rec = rel_by_code[comp_code].get(item)
        if rec:
            verd.append(f"**{item}**: {rec['relevance_type']}/{rec['relevance_level']}")
    w("연관 판정 — " + " · ".join(verd) + "\n")
    # 5영역별 카드
    by_cat = defaultdict(list)
    for c in cards:
        by_cat[c.get("category", "기타")].append(c)
    w("| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |")
    w("|---|---|---|---|:---:|---|")
    order = {cat: i for i, cat in enumerate(CATS)}
    for c in sorted(cards, key=lambda x: order.get(x.get("category"), 99)):
        g = grade(c["evidence_id"])
        url = c.get("source_url", "")
        link = f"[{esc(c.get('source_name',''))}]({url})" if url else esc(c.get("source_name", ""))
        w(f"| {c['evidence_id']} | {esc(c.get('category'))} | {esc(c.get('claim'))} "
          f"| {esc(c.get('source_type'))} | {GRADE_EMOJI.get(g)} | {link} |")
    w("")

# ── 4. 데이터 갭 & 미확인 ──
w("## 4. 데이터 갭 & 미확인 항목 (정직한 갭 — 시도 내역 포함)\n")
w("검증관이 '원문접근불가/추론과다/상충' 이슈를 표기했거나 조사관이 honest_gap으로 명문화한 항목의 요약. "
  "각 기업의 아이템 핵심 연관은 별도 상/중 근거로 독립 성립함(§방법론 참조).\n")
gap_terms = ("gap", "갭", "미확인", "미확보", "403", "추론", "미상", "불가")
w("| 기업 | 갭/이슈 카드 | 요지 |")
w("|------|:---:|------|")
for comp_code in codes:
    cards = ev_by_code[comp_code]
    gaps = []
    for c in cards:
        v = ver.get(c["evidence_id"], {})
        issues = [i for i in v.get("issues", []) if i != "없음"]
        note = (c.get("notes") or "")
        if issues or any(t in note for t in gap_terms):
            gaps.append(c)
    if not gaps:
        continue
    # 대표 갭 1~2개 요지
    reps = []
    for c in gaps[:2]:
        v = ver.get(c["evidence_id"], {})
        iss = "/".join(i for i in v.get("issues", []) if i != "없음") or "honest_gap"
        reps.append(f"{c['evidence_id']}({iss})")
    w(f"| {esc(code_name[comp_code])} | {len(gaps)}건 | {esc('; '.join(reps))} |")
w("")
w("> 대표적 공통 갭: (1) 다수 공식 홈페이지·DART·특허 DB가 봇 차단(HTTP 403)으로 원문 직접 페치 불가 → "
  "검색 스니펫·2차 언론·Google Patents로 교차확인 대체. (2) 일부 국내 비상장사/스타트업의 정확한 특허 등록번호·매출 세부는 "
  "KIPRIS 인터랙티브 제한으로 미확보(특허 '존재'는 언론·발표로 확인). (3) mTG/ADC '무관' 판정은 검색 부재에 기반한 negative finding으로, "
  "각 시도 검색어를 카드 notes에 명문화함.\n")

# ── 5. 방법론 & 한계 ──
w("## 5. 방법론 & 한계\n")
w("- **아키텍처**: 오케스트레이터(①)가 48개 기업을 조사관(②, 필수)에 분배 → 증거 카드 617개 생성. "
  "검증관(④, 필수)이 카드만 근거로 상/중/하 판정 → 반려 3건 재조사 루프 → 연관성 분석관(③) 판정 → 리포트(⑤) 종합.")
w("- **출처 위계**: 1차(공식 홈페이지·IR/공시·등록특허·논문·규제기관) > 2차(주요 언론·시장리포트) > 3차(비채택/‘하’).")
w("- **검증 루브릭(§7)**: 상=1차+원문+발췌+최신성/24개월(가능시 2+교차) · 중=신뢰 2차·단일이나 검증가능·24–48개월/부분교차 · "
  "하=미상/접근불가/상충/추론과다/48개월초과.")
w(f"- **연관도 임계**: match_threshold=중. '무관' 유형은 등급을 '하'로 정규화하여 매칭에서 제외.")
w("- **최신성 창**: 12개월(뉴스·동향). 구조적 사실(사업·특허)은 시점 무관.")
w("- **재조사 루프**: reject_reinvestigate 3건(EV-STK-006/JET-015/TBF-014) → 재조사 1회로 전건 해소(STK 콜라겐 근거 약함 확정·하향, JET/TBF 무관 확정·상향).")
w("- **핵심 한계**: (1) 웹 접근 차단(403)으로 상당수 1차 원문을 2차/스니펫으로 대체 검증 — 등급에 반영(‘중’ 다수). "
  "(2) 특허 등록번호 다수 미확보. (3) mTG/ADC 무관은 검색 부재 기반이라 원리상 완전 부정 증명은 아님. "
  "(4) 그룹 계열사 파이프라인(예: J&J Innovative Medicine, 대웅-한올바이오파마)은 배정 사업부와 구분해 기록함.\n")

# 핵심 인사이트 (매칭 데이터 기반)
w("### 핵심 인사이트\n")
w("1. **Collagen은 이 기업군의 공통 분모** — 44/48이 연관(대부분 직접사업). 콜라겐·젤라틴 원료사(GELITA·Rousselot·Nitta·Evonik·CollPlant), "
  "의료기기 ADM·창상·조직재생(Integra·Geistlich·Aroa·MiMedx·한스바이오메드·엘앤씨바이오·시지바이오·셀론텍 등), 바이오프린팅·배양육 스캐폴드로 삼분된다.")
w("2. **mTG 연관은 '효소 제조'가 아니라 '가교 기질/응용'** — GELITA는 젤라틴-트랜스글루타미나제 의료접착제 특허를 직접 보유(자사 응용), "
  "TissenBioFarm은 자사 배양육 특허에 mTG를 명시. Rousselot·Nitta·Aleph는 자사 젤라틴/콜라겐이 mTG 가교의 기질로 쓰이는 접점.")
w("3. **ADC(항체-약물 접합체)는 대체로 무관** — 예상대로 콜라겐/배양육 기업군과 직접 접점이 거의 없다. 유의미한 연관은 제약 계열뿐: "
  "J&J(Ambrx 인수로 자체 ADC 파이프라인, 단 MedTech가 아닌 Innovative Medicine 부문), 대웅제약(자회사 한올바이오파마의 Crystal Bioscience 항체 플랫폼 경유, 초기 단계).")
w("4. **mTG↔ADC 교차 접점(부위특이 접합)은 이 48개 기업 중 실사업으로 구현한 곳 없음** — 개념적 연결고리는 존재하나, "
  "본 조사 대상 기업 어느 곳도 mTG를 ADC 접합에 상용 공급/응용하지 않는 것으로 확인.\n")

w("---")
w(f"*생성: CIRV 하니스 · {RUN_DATE} · 감사 데이터셋 48개 기업 / 617 증거 카드 / 617 검증 레코드 / 144 연관성 레코드.*")

os.makedirs(f"{ROOT}/reports", exist_ok=True)
path = f"{ROOT}/reports/CIRV_report_{RUN_DATE}.md"
body = "\n".join(out) + "\n"
open(path, "w", encoding="utf-8").write(body)
print("wrote", path, f"({len(body)} chars)")
