#!/usr/bin/env python3
"""
CIRV 3분류 리포트 — ADC / Collagen / 무관
사용자 기준: mTG는 '자체 개발(효소 자체 생산/개발)'이 아니면 연관으로 보지 않음.
검증 결과 48개사 중 mTG 효소 자체 개발사는 0곳 → mTG 버킷 제거, ADC/Collagen/무관 3분류로 재정리.
데이터: reports/data/*.json (커밋된 감사 데이터셋) 우선.
산출: reports/CIRV_buckets_3way_2026-07-06.md
"""
from __future__ import annotations
import json, os
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUN_DATE = "2026-07-06"
LEVEL_RANK = {"하": 1, "중": 2, "상": 3}
THR = 2  # match_threshold=중
SCORED_ITEMS = ["ADC", "Collagen"]   # mTG는 자체개발 0곳으로 분류기준에서 제외


def src(name):
    for base in ("reports/data", "out"):
        p = os.path.join(ROOT, base, name)
        if os.path.exists(p):
            return p
    raise FileNotFoundError(name)


relrecs = json.load(open(src("relevance_records.json"), encoding="utf-8"))
rel = defaultdict(dict)
name = {}
for r in relrecs:
    rel[r["_code"]][r["item"]] = r
    name.setdefault(r["_code"], r["company"])
codes = sorted(rel.keys(), key=lambda k: name[k].lower())


def related(rec):
    return bool(rec) and rec.get("relevance_type") != "무관" \
        and LEVEL_RANK.get(rec.get("relevance_level"), 0) >= THR


def cell(rec):
    if not rec:
        return "—"
    t, l = rec.get("relevance_type"), rec.get("relevance_level")
    if t == "무관":
        return "무관"
    return ("●" if related(rec) else "○") + f"{l}/{t}"


def eids(rec):
    return ", ".join((rec.get("supporting_evidence_ids") or [])[:3]) if rec else ""


adc = [c for c in codes if related(rel[c].get("ADC"))]
col = [c for c in codes if related(rel[c].get("Collagen"))]
none3 = [c for c in codes if not related(rel[c].get("ADC")) and not related(rel[c].get("Collagen"))]
both = [c for c in codes if related(rel[c].get("ADC")) and related(rel[c].get("Collagen"))]

out, w = [], lambda s="": out.append(s)
w("# CIRV 3분류 리포트 — ADC · Collagen · 무관\n")
w(f"**조사일**: {RUN_DATE} · 기준: match_threshold=중\n")

w("## 분류 기준\n")
w("- **mTG 버킷 제거**: 사용자 기준상 mTG는 *효소를 자체 개발/생산*하는 경우에만 연관으로 인정한다. "
  "48개사 검증 결과 mTG 효소를 자체 개발·생산하는 기업은 **0곳**이다. mTG 접점이 잡힌 5개사(GELITA·TissenBioFarm·"
  "Rousselot·Nitta·Aleph Farms)는 모두 (a)자사 젤라틴/콜라겐이 mTG 가교의 *기질*이거나, (b)자사 특허에서 mTG를 *가져다 쓰는* "
  "응용일 뿐, 효소 자체의 개발 주체가 아님이 각 rationale에 명문화됨. → mTG를 분류 기준에서 제외.")
w("- 남은 두 기준(**ADC**·**Collagen**)으로 분류하고, 둘 다 아니면 **무관**으로 둔다. ADC·Collagen 양쪽 연관 기업은 양쪽에 표기(배타 아님), '무관'은 배타적.")
w("- ●=연관(≥중) · ○=약한 인접('하') · 무관=근거상 무관. 모든 판정은 evidence_id로 추적 가능.\n")

w("## 1. 요약\n")
w("| 분류 | 기업 수 |")
w("|------|:---:|")
w(f"| **ADC 관계사** | {len(adc)} |")
w(f"| **Collagen 관계사** | {len(col)} |")
w(f"| **무관 (ADC·Collagen 모두 아님)** | {len(none3)} |")
w(f"\n- ADC∩Collagen 중복: {len(both)}개({', '.join(name[c] for c in both)}).")
w(f"- 배타적 집계: ADC 전용 {len(adc)-len(both)} · Collagen 전용 {len(col)-len(both)} · 양쪽 {len(both)} · 무관 {len(none3)} "
  f"= 총 {(len(adc)-len(both))+(len(col)-len(both))+len(both)+len(none3)}개.\n")

w("## 2. 전체 기업 × 분류 매트릭스 (48개사)\n")
w("| 기업 | ADC | Collagen | (참고)mTG | 분류 |")
w("|------|-----|----------|----------|------|")
for c in codes:
    tags = []
    if related(rel[c].get("ADC")): tags.append("ADC")
    if related(rel[c].get("Collagen")): tags.append("Collagen")
    label = ", ".join(tags) if tags else "**무관**"
    w(f"| {name[c].replace('|','/')} | {cell(rel[c].get('ADC'))} | {cell(rel[c].get('Collagen'))} "
      f"| {cell(rel[c].get('mTG'))} | {label} |")
w("")

def bucket_table(title, lst, item):
    w(f"## {title} — {len(lst)}개\n")
    if not lst:
        w("_해당 없음._\n"); return
    w("| 기업 | 연관유형 | 연관도 | 근거 검증등급 | 핵심 근거(evidence_id) |")
    w("|------|----------|:---:|:---:|------|")
    for c in sorted(lst, key=lambda c: -LEVEL_RANK.get(rel[c][item]["relevance_level"], 0)):
        r = rel[c][item]
        vg = r.get("verified_grade") or "—"
        extra = " ⟨Collagen도 해당⟩" if item == "ADC" and related(rel[c].get("Collagen")) else ""
        w(f"| {name[c].replace('|','/')}{extra} | {r['relevance_type']} | {r['relevance_level']} | {vg} | {eids(r)} |")
    w("")

bucket_table("3. ADC 관계사", adc, "ADC")
bucket_table("4. Collagen 관계사", col, "Collagen")

w(f"## 5. 무관 (ADC·Collagen 모두 아님) — {len(none3)}개\n")
w("세 아이템(mTG 자체개발 기준 포함) 어느 것도 연관(≥중)이 없는 기업. 모두 배양육(cultivated meat) 기업으로, "
  "동물성 콜라겐/젤라틴을 회피·대체하는 전략이라 Collagen이 '하'에 그친다.\n")
w("| 기업 | ADC | Collagen | (참고)mTG | 무관 근거 |")
w("|------|-----|----------|----------|-----------|")
for c in none3:
    why = (rel[c].get("Collagen") or {}).get("rationale", "").replace("|", "/")[:150]
    w(f"| {name[c].replace('|','/')} | {cell(rel[c].get('ADC'))} | {cell(rel[c].get('Collagen'))} "
      f"| {cell(rel[c].get('mTG'))} | {why} |")
w("")

w("## 6. (참고) mTG 접점은 있으나 자체 개발이 아니어서 mTG 기준 제외된 기업\n")
w("아래 5개사는 mTG 가교 기질/응용 접점이 있으나 효소 자체 개발이 아니라 mTG 관계사로 분류하지 않음. "
  "다만 전부 Collagen 관계사에는 해당한다.\n")
w("| 기업 | mTG 접점 | 자체개발? | 실제 분류 |")
w("|------|----------|:---:|-----------|")
mtg5 = [c for c in codes if related(rel[c].get("mTG"))]
for c in mtg5:
    coltag = "Collagen" if related(rel[c].get("Collagen")) else "—"
    w(f"| {name[c].replace('|','/')} | {rel[c]['mTG']['relevance_level']}/{rel[c]['mTG']['relevance_type']} "
      f"| ✗ (기질/응용) | {coltag} |")
w("")

w("---")
w(f"*생성: CIRV 하니스 · {RUN_DATE} · mTG 자체개발 기준 적용(자체개발 0곳) → ADC/Collagen/무관 3분류.*")

path = os.path.join(ROOT, "reports", f"CIRV_buckets_3way_{RUN_DATE}.md")
open(path, "w", encoding="utf-8").write("\n".join(out) + "\n")
print("wrote", path)
print(f"ADC {len(adc)} · Collagen {len(col)} · 무관 {len(none3)} · (ADC∩Col {len(both)})")
print("ADC:", [name[c] for c in adc])
print("무관:", [name[c] for c in none3])
