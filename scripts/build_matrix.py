#!/usr/bin/env python3
"""
CIRV 관계 매트릭스 (4-버킷)
mTG / ADC / Collagen 관계사 + '3가지 모두 무관' 을 재분류해 리포트를 만든다.
데이터 소스: reports/data/*.json (커밋된 감사 데이터셋) 우선, 없으면 out/.
산출: reports/CIRV_relation_matrix_2026-07-06.md
"""
from __future__ import annotations
import json, os
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUN_DATE = "2026-07-06"
ITEMS = ["mTG", "ADC", "Collagen"]
LEVEL_RANK = {"하": 1, "중": 2, "상": 3}
THR = 2  # match_threshold=중


def src(name):
    for base in ("reports/data", "out"):
        p = os.path.join(ROOT, base, name)
        if os.path.exists(p):
            return p
    raise FileNotFoundError(name)


relrecs = json.load(open(src("relevance_records.json"), encoding="utf-8"))

# code -> {item -> rec}, code -> name
rel = defaultdict(dict)
name = {}
for r in relrecs:
    code = r["_code"]
    rel[code][r["item"]] = r
    name.setdefault(code, r["company"])

codes = sorted(rel.keys(), key=lambda k: name[k].lower())


def related(rec):
    if not rec or rec.get("relevance_type") == "무관":
        return False
    return LEVEL_RANK.get(rec.get("relevance_level"), 0) >= THR


def cell(rec):
    if not rec:
        return "—"
    t, l = rec.get("relevance_type"), rec.get("relevance_level")
    if t == "무관":
        return "무관"
    mark = "●" if related(rec) else "○"        # ● ≥중 관계 / ○ 약한 인접(하)
    return f"{mark}{l}/{t}"


# 버킷
buckets = {it: [] for it in ITEMS}
none_bucket = []
multi = []
for c in codes:
    hits = [it for it in ITEMS if related(rel[c].get(it))]
    for it in hits:
        buckets[it].append(c)
    if not hits:
        none_bucket.append(c)
    if len(hits) >= 2:
        multi.append((c, hits))

out = []
w = out.append
w("# CIRV 관계 매트릭스 — mTG · ADC · Collagen · (3가지 모두 무관)\n")
w(f"**조사일**: {RUN_DATE} · 기준: match_threshold=중(●=연관 ≥중, ○=약한 인접 '하', 무관=근거상 무관)\n")
w("> 원 리포트(`reports/CIRV_report_{}.md`)의 검증된 연관성 레코드를 재분류한 것. 모든 판정은 evidence_id로 추적 가능.\n".format(RUN_DATE))

# 1) 버킷 요약
w("## 1. 버킷 요약\n")
w("| 버킷 | 기업 수 |")
w("|------|:---:|")
for it in ITEMS:
    w(f"| **{it} 관계사** | {len(buckets[it])} |")
w(f"| **3가지 모두 무관** | {len(none_bucket)} |")
w(f"| (참고) 2개 이상 아이템 동시 연관 | {len(multi)} |")
w(f"\n총 기업 {len(codes)}개. 한 기업이 여러 버킷에 중복 집계될 수 있음(예: Collagen+mTG). '3가지 모두 무관'은 배타적.\n")

# 2) 전체 매트릭스
w("## 2. 전체 기업 × 아이템 매트릭스 (48개사)\n")
w("| 기업 | mTG | ADC | Collagen | 관계 버킷 |")
w("|------|-----|-----|----------|-----------|")
for c in codes:
    tags = [it for it in ITEMS if related(rel[c].get(it))]
    bucket = ", ".join(tags) if tags else "**3가지 모두 무관**"
    row = [name[c].replace("|", "/")]
    for it in ITEMS:
        row.append(cell(rel[c].get(it)))
    row.append(bucket)
    w("| " + " | ".join(row) + " |")
w("")

# 3) 버킷별 명단
def eids(rec):
    return ", ".join((rec.get("supporting_evidence_ids") or [])[:3]) if rec else ""

for it in ITEMS:
    w(f"## 3.{ITEMS.index(it)+1} {it} 관계사 — {len(buckets[it])}개\n")
    w("| 기업 | 연관유형 | 연관도 | 핵심 근거 |")
    w("|------|----------|:---:|------|")
    rows = sorted(buckets[it],
                  key=lambda c: -LEVEL_RANK.get(rel[c][it]["relevance_level"], 0))
    for c in rows:
        r = rel[c][it]
        w(f"| {name[c].replace('|','/')} | {r['relevance_type']} | {r['relevance_level']} | {eids(r)} |")
    w("")

# 4) 모두 무관
w(f"## 4. 3가지(mTG·ADC·Collagen) 모두 무관 — {len(none_bucket)}개\n")
w("아래 기업은 세 아이템 어느 것도 match_threshold(중) 이상 연관이 없다(약한 '하' 인접 또는 무관). "
  "판정 근거를 아이템별로 명시한다.\n")
if none_bucket:
    w("| 기업 | mTG | ADC | Collagen | 왜 무관인가 |")
    w("|------|-----|-----|----------|-------------|")
    for c in none_bucket:
        cells = [cell(rel[c].get(it)) for it in ITEMS]
        # rationale from Collagen record notes usually most informative
        why = (rel[c].get("Collagen") or {}).get("rationale", "")
        why = why.replace("|", "/")[:160]
        w(f"| {name[c].replace('|','/')} | {cells[0]} | {cells[1]} | {cells[2]} | {why} |")
    w("")
else:
    w("_해당 없음._\n")

# 5) 2개 이상 동시 연관 (참고)
w("## 5. (참고) 2개 이상 아이템 동시 연관\n")
if multi:
    w("| 기업 | 동시 연관 아이템 |")
    w("|------|------------------|")
    for c, hits in multi:
        w(f"| {name[c].replace('|','/')} | {' + '.join(hits)} |")
    w("")
else:
    w("_해당 없음._\n")

w("---")
w(f"*생성: CIRV 하니스 · {RUN_DATE} · 재분류 소스 = 검증된 연관성 레코드 144건.*")

path = os.path.join(ROOT, "reports", f"CIRV_relation_matrix_{RUN_DATE}.md")
open(path, "w", encoding="utf-8").write("\n".join(out) + "\n")
print("wrote", path)
print("buckets:", {it: len(buckets[it]) for it in ITEMS}, "| 모두무관:", len(none_bucket),
      "| 다중연관:", len(multi))
print("모두무관 기업:", [name[c] for c in none_bucket])
