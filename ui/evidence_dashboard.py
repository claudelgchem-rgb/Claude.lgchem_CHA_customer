"""
CIRV 증거 UI 대시보드 (§8)
==========================
조사관(②)이 명문화한 증거 카드와 검증관(④)의 검증 등급을 하나의 화면으로 표출한다.
"화면에 표출되지 않은 근거는 존재하지 않는 것으로 간주"한다는 원칙(§8)을 구현하는 렌더러.

실행:
    pip install streamlit pandas
    streamlit run ui/evidence_dashboard.py

읽는 파일:
    out/evidence_cards.json         # 증거 카드 배열 (schemas/evidence_card.schema.json)
    out/verification_records.json   # 검증 레코드 배열 (schemas/verification_record.schema.json)
    out/relevance_records.json      # (선택) 연관성 레코드 배열 — 아이템 필터에 사용
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent.parent
# 런타임 작업영역(out/)을 우선 사용하되, 없으면 커밋된 감사 데이터셋(reports/data/)로 폴백
OUT = ROOT / "out"
DATA_FALLBACK = ROOT / "reports" / "data"

CONF_COLOR = {"상": "#1a7f37", "중": "#bf8700", "하": "#cf222e"}  # 녹색 / 주황 / 적색
CONF_BG = {"상": "#e6f4ea", "중": "#fff4e0", "하": "#fce8e8"}


def _load(name: str) -> list[dict]:
    path = OUT / name
    if not path.exists():
        path = DATA_FALLBACK / name   # 커밋된 감사 데이터셋 폴백
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        st.error(f"{name} 파싱 실패: {exc}")
        return []
    return data if isinstance(data, list) else data.get("items", [])


def _confidence_of(row: dict) -> str:
    """검증 등급이 있으면 그것을, 없으면 조사관 자기추정을 사용."""
    return row.get("verified_confidence") or row.get("self_confidence") or "하"


def _relevance_map(relevance: list[dict]) -> dict[tuple[str, str], list[str]]:
    """evidence_id -> 연관 아이템 목록 (relevance 레코드에서 역인덱스)."""
    idx: dict[str, set[str]] = {}
    for rec in relevance:
        item = rec.get("item", "")
        for ev in rec.get("supporting_evidence_ids", []):
            idx.setdefault(ev, set()).add(item)
    return {k: sorted(v) for k, v in idx.items()}


def main() -> None:
    st.set_page_config(page_title="CIRV 증거 UI", layout="wide")
    st.title("CIRV 증거 UI — 기업–아이템 연관성 인텔리전스")
    st.caption("조사관(②)의 증거 카드 × 검증관(④)의 상/중/하 등급 · 근거는 화면에 표출된 것만 인정한다(§8)")

    cards = _load("evidence_cards.json")
    verifs = {v["evidence_id"]: v for v in _load("verification_records.json") if "evidence_id" in v}
    relevance = _load("relevance_records.json")
    ev_to_items = _relevance_map(relevance)

    if not cards:
        st.warning(
            "`out/evidence_cards.json`이 비어 있거나 없습니다. "
            "오케스트레이터(cirv-orchestrator)를 실행해 증거 카드를 먼저 생성하세요."
        )
        st.stop()

    # 증거 카드 + 검증 결과 조인
    rows = []
    for c in cards:
        v = verifs.get(c.get("evidence_id"), {})
        merged = {**c, **v}
        merged["_confidence"] = _confidence_of(merged)
        merged["_items"] = ", ".join(ev_to_items.get(c.get("evidence_id"), [])) or "—"
        rows.append(merged)
    df = pd.DataFrame(rows)

    # ---- 사이드바 필터 ----
    st.sidebar.header("필터")
    companies = sorted(df["company"].dropna().unique())
    cats = sorted(df["category"].dropna().unique())
    confs = ["상", "중", "하"]
    all_items = sorted({i for lst in ev_to_items.values() for i in lst})

    f_company = st.sidebar.multiselect("기업", companies, default=companies)
    f_cat = st.sidebar.multiselect("카테고리", cats, default=cats)
    f_conf = st.sidebar.multiselect("검증등급", confs, default=confs)
    f_item = st.sidebar.multiselect("연관 아이템", all_items, default=all_items) if all_items else []

    mask = (
        df["company"].isin(f_company)
        & df["category"].isin(f_cat)
        & df["_confidence"].isin(f_conf)
    )
    if all_items:
        mask &= df["evidence_id"].apply(lambda e: bool(set(ev_to_items.get(e, [])) & set(f_item)) or not ev_to_items.get(e))
    view = df[mask]

    # ---- 요약 지표 ----
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("증거 카드", len(view))
    c2.metric("상(高)", int((view["_confidence"] == "상").sum()))
    c3.metric("중", int((view["_confidence"] == "중").sum()))
    c4.metric("하(低)", int((view["_confidence"] == "하").sum()))

    # ---- 증거 카드 렌더 ----
    st.subheader("증거 카드")
    for _, r in view.iterrows():
        conf = r["_confidence"]
        with st.container():
            st.markdown(
                f"<div style='border-left:6px solid {CONF_COLOR[conf]};"
                f"background:{CONF_BG[conf]};padding:10px 14px;border-radius:6px;margin-bottom:8px'>"
                f"<b>{r.get('evidence_id','')}</b> · {r.get('company','')} · "
                f"<i>{r.get('category','')}</i> "
                f"<span style='float:right;color:{CONF_COLOR[conf]};font-weight:700'>검증등급 {conf}</span><br>"
                f"{r.get('claim','')}<br>"
                f"<small>출처: {r.get('source_name','')} ({r.get('source_type','')}) · "
                f"발행일 {r.get('source_date','')} · "
                f"<a href='{r.get('source_url','')}' target='_blank'>원문</a> · "
                f"연관 아이템: {r.get('_items','—')}</small>"
                f"</div>",
                unsafe_allow_html=True,
            )
            with st.expander("근거 발췌 · 검증 상세"):
                st.write("**발췌:**", r.get("excerpt", "—"))
                st.write("**자기신뢰도:**", r.get("self_confidence", "—"),
                         " · **검증등급:**", r.get("verified_confidence", "(미검증)"))
                st.write("**출처위계:**", r.get("source_tier", "—"),
                         " · **교차확인 수:**", r.get("corroboration_count", "—"),
                         " · **최신성:**", r.get("recency_ok", "—"))
                st.write("**검증 근거:**", r.get("verification_reason", "—"))
                if r.get("issues"):
                    st.write("**이슈:**", ", ".join(r.get("issues", [])))
                if r.get("notes"):
                    st.write("**비고:**", r.get("notes"))

    # ---- 원자료 테이블 ----
    with st.expander("전체 데이터 테이블 (§8-A 컬럼)"):
        cols = ["evidence_id", "company", "category", "claim", "source_type",
                "source_url", "source_date", "verified_confidence", "_items"]
        st.dataframe(view[[c for c in cols if c in view.columns]], use_container_width=True)


if __name__ == "__main__":
    main()
