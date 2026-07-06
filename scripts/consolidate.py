#!/usr/bin/env python3
"""
CIRV 통합기 (오케스트레이터 ①)
==============================
기업별 shard(out/evidence, out/verification, out/relevance)를 병합하고,
연관성 레코드를 정규화(유형-등급 일관성)하며, 검증 등급을 조인하고,
아이템 × 기업 매칭 테이블을 계산한다.

산출:
  out/evidence_cards.json        (전 카드 병합)
  out/verification_records.json  (전 검증 병합)
  out/relevance_records.json     (정규화 + 검증등급 조인)
  out/match_table.json           (아이템 × 기업 매칭, 요약 통계)
"""
from __future__ import annotations
import json, glob, os
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "out")
LEVEL_RANK = {"하": 1, "중": 2, "상": 3}
MATCH_THRESHOLD = "중"  # options.match_threshold


def load_all(subdir):
    data = {}
    for f in sorted(glob.glob(os.path.join(OUT, subdir, "*.json"))):
        code = os.path.basename(f)[:-5]
        data[code] = json.load(open(f, encoding="utf-8"))
    return data


def main():
    evidence = load_all("evidence")
    verification = load_all("verification")
    relevance = load_all("relevance")

    # company codes -> names (from first evidence card)
    code_name = {c: (cards[0]["company"] if cards else c) for c, cards in evidence.items()}

    # flat merges
    all_ev = [card for c in evidence for card in evidence[c]]
    all_ver = [r for c in verification for r in verification[c]]
    json.dump(all_ev, open(os.path.join(OUT, "evidence_cards.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    json.dump(all_ver, open(os.path.join(OUT, "verification_records.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)

    # evidence_id -> verified_confidence / verdict
    ver_by_id = {r["evidence_id"]: r for r in all_ver}

    # normalize relevance + join verification
    norm_rel = []
    for code, recs in relevance.items():
        for r in recs:
            rec = dict(r)
            # 1) type-level consistency: 무관 => 하
            if rec.get("relevance_type") == "무관":
                rec["relevance_level"] = "하"
            # 2) verified grade = best confidence among supporting evidence (accepted only)
            best = None
            rejected = []
            for eid in rec.get("supporting_evidence_ids", []):
                v = ver_by_id.get(eid)
                if not v:
                    continue
                if v.get("verdict") == "reject_reinvestigate":
                    rejected.append(eid)
                conf = v.get("verified_confidence")
                if conf and (best is None or LEVEL_RANK[conf] > LEVEL_RANK[best]):
                    best = conf
            rec["verified_grade"] = best            # 종합 검증등급(최고 신뢰 근거)
            rec["rejected_evidence"] = rejected
            rec["_code"] = code
            norm_rel.append(rec)
    json.dump(norm_rel, open(os.path.join(OUT, "relevance_records.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)

    # match table: (item -> [companies at/above threshold])
    thr = LEVEL_RANK[MATCH_THRESHOLD]
    by_item = defaultdict(list)
    for rec in norm_rel:
        by_item[rec["item"]].append(rec)

    match = {}
    for item, recs in by_item.items():
        rows = []
        for rec in recs:
            lvl = rec.get("relevance_level")
            is_match = (rec.get("relevance_type") != "무관"
                        and LEVEL_RANK.get(lvl, 0) >= thr)
            rows.append({
                "code": rec["_code"],
                "company": code_name.get(rec["_code"], rec.get("company")),
                "relevance_type": rec.get("relevance_type"),
                "relevance_level": lvl,
                "relevance_score": rec.get("relevance_score"),
                "verified_grade": rec.get("verified_grade"),
                "match": is_match,
                "n_evidence": len(rec.get("supporting_evidence_ids", [])),
                "rejected_evidence": rec.get("rejected_evidence", []),
            })
        rows.sort(key=lambda x: (-(LEVEL_RANK.get(x["relevance_level"], 0)),
                                 -(x["relevance_score"] or 0)))
        match[item] = rows

    summary = {
        "companies": len(evidence),
        "items": list(by_item.keys()),
        "evidence_cards": len(all_ev),
        "verified": dict(Counter(r.get("verified_confidence") for r in all_ver)),
        "matches_per_item": {it: sum(1 for r in rows if r["match"]) for it, rows in match.items()},
    }
    json.dump({"summary": summary, "match": match},
              open(os.path.join(OUT, "match_table.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)

    # console report
    print("=== 통합 요약 ===")
    print(f"기업 {summary['companies']} · 증거카드 {summary['evidence_cards']} · 검증분포 {summary['verified']}")
    for it, rows in match.items():
        matched = [r for r in rows if r["match"]]
        print(f"\n[{it}] 연관(≥{MATCH_THRESHOLD}) {len(matched)}개사:")
        for r in matched:
            flag = " ⚠reject" if r["rejected_evidence"] else ""
            print(f"  {r['relevance_level']}/{r['relevance_type']:<10} "
                  f"검증{r['verified_grade']} {r['company']}{flag}")


if __name__ == "__main__":
    main()
