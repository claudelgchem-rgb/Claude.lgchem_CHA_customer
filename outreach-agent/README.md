# outreach-agent — 고객 아웃리치 이메일 Agentic Harness

LG화학 사업전략/시장분석 관점의 B2B 고객 아웃리치 이메일 파이프라인.
**고객 리스트 → 개인화 초안 → QA/컴플라이언스 검수 → 사람 승인 → 발송 → 로깅.**

동작 규칙·에이전트 워크플로우·컴플라이언스 기준은 [`CLAUDE.md`](./CLAUDE.md)가 정본이다.
이 README는 빠른 사용법만 정리한다.

## 핵심 안전 원칙
- **기본은 초안까지만.** 실제 발송은 `approved/` 이동 + `mode: send` + `--confirm` 3중 조건이 모두 충족될 때만.
- `send.py`는 항상 **dry-run이 기본**이다. `--confirm` 없이는 절대 발송하지 않는다.
- 승인은 사람이 한다. 에이전트는 `drafts/` → `approved/`로 초안을 **임의로 옮기지 않는다**.
- 비밀정보(비밀번호/토큰)는 `config.yaml`이 아니라 **환경변수**로 주입.

## 디렉터리
```
config.yaml     발송자/모드/한도/백엔드 설정
data/           customers.csv(입력), unsubscribe.csv(제외)
templates/      세그먼트/목적별 골격 템플릿
drafts/         생성 초안 + .review.md (검수 대기)
approved/       사람이 승인해 옮긴 초안 (발송 대상)
logs/           sent_log.csv (append-only 발송 이력, gitignore)
scripts/send.py 발송 스크립트 (dry-run/confirm/logging/throttle/retry)
```

## 셋업
```bash
pip install pyyaml            # send.py 의존성
# config.yaml 편집: sender / backend / daily_cap / mode
export OUTREACH_SMTP_PASSWORD='...'   # backend=smtp일 때 비밀번호
```

## 사용 흐름
1. `data/customers.csv` 준비 (스펙: CLAUDE.md 2번).
2. 에이전트로 초안 생성 → `drafts/{company}_{date}.md` + `.review.md`.
3. 사람이 초안·리뷰 검토, 수정 후 `approved/`로 이동.
4. **dry-run**으로 대상·건수 확인:
   ```bash
   python3 scripts/send.py            # dry-run (기본)
   ```
5. 본인 주소로 테스트 발송 1건 → 문제없으면 실전:
   ```bash
   python3 scripts/send.py --confirm  # 실제 발송
   ```

## send.py 계약
- `--dry-run`(기본): 수신자/제목/미리보기만 출력, 발송 안 함.
- `--confirm`: 실제 발송.
- `unsubscribe.csv` 제외, 동일 email+purpose 중복 방지, `daily_cap` 강제.
- 발송마다 `logs/sent_log.csv`에 `timestamp,company,email,subject,status,message_id` 기록.
- throttle(발송 간 지연) + 실패 시 지수 백오프 2회 재시도.
- 백엔드: 현재 `smtp` 구현. `graph`/`gmail`은 `config.yaml`에 자리만 있음 —
  사내 IT/보안의 OAuth 앱 승인 확보 후 `BACKENDS`에 핸들러 추가.

## 초안 파일 포맷
YAML front-matter(필수: `email`, `subject`) + 본문. 예시는 `drafts/`의 샘플 참조.
