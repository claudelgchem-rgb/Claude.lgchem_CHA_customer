#!/usr/bin/env python3
"""
send.py — outreach-agent Send Orchestrator (CLAUDE.md 4번 Agent 4 / 7번 계약)

계약(interface):
  --dry-run (기본)  실제 발송 없이 "누구에게/제목/미리보기"만 출력
  --confirm         실제 발송
  발송마다 logs/sent_log.csv에 timestamp,company,email,subject,status,message_id 기록
  throttle          발송 간 지연(config throttle_seconds.min~max)
  retry             실패 시 지수 백오프로 최대 2회 재시도, 최종 실패는 status=failed

안전장치:
  - approved/ 폴더의 초안만 대상
  - unsubscribe.csv 제외
  - daily_cap 초과 시 자동 중단
  - 같은 email+purpose 이미 발송 이력이 있으면 경고(skipped_duplicate)
  - --confirm 없으면 절대 실제 발송하지 않음

비밀정보는 config가 아니라 환경변수에서 읽는다.
"""
from __future__ import annotations

import argparse
import csv
import os
import random
import smtplib
import sys
import time
from datetime import datetime, timezone
from email.mime.text import MIMEText
from email.utils import formataddr, make_msgid
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML이 필요합니다: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "config.yaml"
APPROVED_DIR = ROOT / "approved"
DATA_DIR = ROOT / "data"
LOG_PATH = ROOT / "logs" / "sent_log.csv"
LOG_FIELDS = ["timestamp", "company", "email", "subject", "status", "message_id"]


# ---------- 유틸 ----------

def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        sys.exit(f"config.yaml 없음: {CONFIG_PATH}")
    with CONFIG_PATH.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def parse_draft(path: Path) -> dict | None:
    """YAML front-matter + 본문 파싱. email/subject 없으면 None(=skipped)."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        print(f"  ! {path.name}: front-matter 없음 → skipped")
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        print(f"  ! {path.name}: front-matter 형식 오류 → skipped")
        return None
    try:
        meta = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as e:
        print(f"  ! {path.name}: front-matter YAML 오류 ({e}) → skipped")
        return None
    body = parts[2].lstrip("\n")
    meta["_body"] = body
    meta["_file"] = path.name
    if not meta.get("email") or not meta.get("subject"):
        print(f"  ! {path.name}: email/subject 누락 → skipped")
        return None
    return meta


def load_unsubscribe() -> set[str]:
    path = DATA_DIR / "unsubscribe.csv"
    out: set[str] = set()
    if not path.exists():
        return out
    with path.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            email = (row.get("email") or "").strip().lower()
            if email:
                out.add(email)
    return out


def load_sent_history() -> list[dict]:
    if not LOG_PATH.exists():
        return []
    with LOG_PATH.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def count_sent_today(history: list[dict]) -> int:
    today = datetime.now().astimezone().date().isoformat()
    return sum(
        1 for r in history
        if r.get("status") == "sent" and (r.get("timestamp") or "").startswith(today)
    )


def already_sent(history: list[dict], email: str, purpose: str) -> bool:
    email = (email or "").lower()
    for r in history:
        if (
            r.get("status") == "sent"
            and (r.get("email") or "").lower() == email
            and (r.get("_purpose") or r.get("purpose") or "") == (purpose or "")
        ):
            return True
    return False


def append_log(row: dict) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    new_file = not LOG_PATH.exists()
    with LOG_PATH.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=LOG_FIELDS)
        if new_file:
            w.writeheader()
        w.writerow({k: row.get(k, "") for k in LOG_FIELDS})


def build_body(meta: dict, config: dict) -> str:
    """본문 하단에 언어별 서명 자동 삽입(발신자 신원 컴플라이언스)."""
    body = meta.get("_body", "").rstrip()
    lang = (meta.get("language") or "ko").lower()
    sig = config.get("sender", {}).get(
        "signature_en" if lang == "en" else "signature_ko", ""
    )
    if sig and sig.strip() not in body:
        body = f"{body}\n\n--\n{sig.strip()}\n"
    return body


# ---------- 발송 백엔드 ----------

def send_smtp(meta: dict, body: str, config: dict) -> str:
    sender = config["sender"]
    smtp_cfg = config["smtp"]
    password = os.environ.get(smtp_cfg.get("password_env", ""), "")
    if not password:
        raise RuntimeError(
            f"SMTP 비밀번호 환경변수 미설정: {smtp_cfg.get('password_env')}"
        )
    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = meta["subject"]
    msg["From"] = formataddr((sender.get("name", ""), sender["email"]))
    msg["To"] = meta["email"]
    msg_id = make_msgid()
    msg["Message-ID"] = msg_id

    host, port = smtp_cfg["host"], int(smtp_cfg.get("port", 587))
    with smtplib.SMTP(host, port, timeout=30) as server:
        if smtp_cfg.get("use_tls", True):
            server.starttls()
        server.login(smtp_cfg["username"], password)
        server.send_message(msg)
    return msg_id


BACKENDS = {"smtp": send_smtp}


def send_with_retry(meta: dict, body: str, config: dict) -> tuple[str, str]:
    """지수 백오프로 최대 2회 재시도. (status, message_id) 반환."""
    backend = config.get("backend", "smtp")
    fn = BACKENDS.get(backend)
    if fn is None:
        return ("failed", f"backend '{backend}' 미구현(현재 smtp만 지원)")
    delay = 2
    last_err = ""
    for attempt in range(3):  # 최초 1회 + 재시도 2회
        try:
            msg_id = fn(meta, body, config)
            return ("sent", msg_id)
        except Exception as e:  # noqa: BLE001 — 로깅 후 재시도
            last_err = str(e)
            if attempt < 2:
                print(f"    재시도 {attempt + 1}/2 ({last_err}) — {delay}s 대기")
                time.sleep(delay)
                delay *= 2
    return ("failed", last_err)


# ---------- 메인 ----------

def main() -> int:
    ap = argparse.ArgumentParser(description="outreach-agent 발송 스크립트")
    ap.add_argument("--confirm", action="store_true",
                    help="실제 발송. 없으면 dry-run(기본).")
    ap.add_argument("--dry-run", action="store_true",
                    help="실제 발송 없이 요약만(기본 동작).")
    args = ap.parse_args()

    # 기본은 dry-run. --confirm이 있어야만 실제 발송.
    do_send = args.confirm and not args.dry_run

    config = load_config()
    daily_cap = int(config.get("daily_cap", 20))
    throttle = config.get("throttle_seconds", {}) or {}
    t_min, t_max = float(throttle.get("min", 2)), float(throttle.get("max", 5))

    if not APPROVED_DIR.exists():
        print(f"approved/ 폴더 없음: {APPROVED_DIR}")
        return 1
    drafts = sorted(APPROVED_DIR.glob("*.md"))
    if not drafts:
        print("approved/ 에 발송할 초안이 없습니다. (사람이 검토 후 옮겨야 함)")
        return 0

    unsub = load_unsubscribe()
    history = load_sent_history()
    sent_today = count_sent_today(history)
    remaining_cap = max(0, daily_cap - sent_today)

    print("=" * 60)
    print(f"모드: {'*** 실제 발송(--confirm) ***' if do_send else 'DRY-RUN (실제 발송 안 함)'}")
    print(f"백엔드: {config.get('backend')}   |   오늘 발송: {sent_today}/{daily_cap} "
          f"(잔여 {remaining_cap})")
    print(f"approved/ 초안: {len(drafts)}건")
    print("=" * 60)

    stats = {"sent": 0, "failed": 0, "skipped": 0}

    for path in drafts:
        meta = parse_draft(path)
        if meta is None:
            stats["skipped"] += 1
            continue

        email = meta["email"].strip()
        company = meta.get("company", "?")
        subject = meta["subject"]
        purpose = meta.get("purpose", "")

        # 제외 리스트
        if email.lower() in unsub:
            print(f"  ⊘ {company} <{email}>: unsubscribe 목록 → skipped")
            stats["skipped"] += 1
            continue

        # 중복 발송 경고
        if already_sent(history, email, purpose):
            print(f"  ⚠ {company} <{email}>: 동일 purpose '{purpose}' 발송 이력 있음 → skipped_duplicate")
            stats["skipped"] += 1
            continue

        # 일일 한도
        if do_send and stats["sent"] >= remaining_cap:
            print(f"  ■ daily_cap({daily_cap}) 도달 → 이후 중단")
            stats["skipped"] += 1
            continue

        body = build_body(meta, config)
        preview = body.strip().replace("\n", " ")[:80]

        print(f"\n  ▶ {company} <{email}>")
        print(f"    제목: {subject}")
        print(f"    미리보기: {preview}...")

        if not do_send:
            stats["skipped"] += 1  # dry-run은 전부 미발송 취급
            continue

        status, msg_id = send_with_retry(meta, body, config)
        append_log({
            "timestamp": now_iso(),
            "company": company,
            "email": email,
            "subject": subject,
            "status": status,
            "message_id": msg_id,
        })
        if status == "sent":
            print(f"    ✅ 발송 완료 ({msg_id})")
            stats["sent"] += 1
            history.append({"email": email, "purpose": purpose, "status": "sent",
                            "timestamp": now_iso()})
        else:
            print(f"    ❌ 발송 실패 ({msg_id})")
            stats["failed"] += 1

        # throttle
        if do_send:
            time.sleep(random.uniform(t_min, t_max))

    print("\n" + "=" * 60)
    print(f"요약 — 발송: {stats['sent']}  실패: {stats['failed']}  스킵: {stats['skipped']}")
    if not do_send:
        print("이건 DRY-RUN이었습니다. 실제 발송하려면 --confirm 을 주세요.")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
