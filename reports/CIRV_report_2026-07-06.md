# CIRV 최종 리포트 — 기업–아이템 연관성 인텔리전스

**조사일**: 2026-07-06 · **하니스**: CIRV (Company Intelligence · Relevance · Verification)

**아이템**: mTG (microbial transglutaminase) · ADC (Antibody-Drug Conjugate) · Collagen (콜라겐/젤라틴)  
**옵션**: recency_window 12개월 · min_sources_per_claim 2 · match_threshold 중

> 본 리포트의 모든 사실은 증거 카드(`evidence_id`)로 추적 가능하며, 각 사실에는 검증관(④)의 상/중/하 등급이 부여되어 있다. 감사 데이터셋(커밋됨): `reports/data/evidence_cards.json`(증거) · `reports/data/verification_records.json`(검증) · `reports/data/relevance_records.json`(연관성) · `reports/data/match_table.json`(매칭). 대화형 검토: `streamlit run ui/evidence_dashboard.py`.

## 1. 요약

- **조사 기업**: 48개 · **관심 아이템**: 3개 · **총 증거 카드**: 617개
- **검증 신뢰도 분포**: 상 184 · 중 402 · 하 31 (전건 accept, 재조사 반려 3건은 재조사 루프 후 해소)
- **아이템별 연관(≥중) 기업 수**: Collagen **44** · mTG **5** · ADC **2**

### 아이템별 매칭 한눈표

| 아이템 | 연관(≥중) 기업 수 | 상세 |
|--------|:---:|------|
| **Collagen** | 44/48 | 콜라겐·젤라틴이 본업(직접사업/직접연구)인 기업 다수 + 바이오프린팅·배양육 '인접·응용' |
| **mTG** | 5/48 | 대부분 자사 소재가 mTG 가교의 *기질*이거나 자사 특허에 mTG 명시. 효소 제조사는 아님 |
| **ADC** | 2/48 | 항체-약물 접합체는 이 기업군과 대체로 무관. 제약 계열만 연관 |

## 2. 아이템별 연관 기업 테이블 (match_threshold=중 이상)

### mTG — 연관 5개사

| 기업 | 연관유형 | 연관도 | 근거 검증등급 | 핵심 근거(evidence_id) |
|------|----------|:---:|:---:|------|
| GELITA AG | 인접·응용 | 중 | 🟢상 | EV-GEL-009, EV-GEL-010, EV-GEL-011 |
| 티센바이오팜 (TissenBioFarm Co., Ltd.) | 인접·응용 | 중 | 🟢상 | EV-TBF-006, EV-TBF-007 |
| Rousselot (Darling Ingredients Inc. 브랜드) | 인접·응용 | 중 | 🟠중 | EV-ROU-008, EV-ROU-005 |
| Aleph Farms Ltd | 인접·응용 | 중 | 🟢상 | EV-ALE-005, EV-ALE-002, EV-ALE-006 |
| Nitta Gelatin Inc. | 인접·응용 | 중 | 🟢상 | EV-NIT-005, EV-NIT-012, EV-NIT-013 |

### ADC — 연관 2개사

| 기업 | 연관유형 | 연관도 | 근거 검증등급 | 핵심 근거(evidence_id) |
|------|----------|:---:|:---:|------|
| Johnson & Johnson MedTech (Ethicon) | 직접연구 | 상 | 🟠중 | EV-JNJ-008, EV-JNJ-009 |
| 대웅제약 (Daewoong Pharmaceutical Co., Ltd.) | 인접·응용 | 중 | 🟢상 | EV-DWG-011, EV-DWG-006, EV-DWG-007 |

### Collagen — 연관 44개사

| 기업 | 연관유형 | 연관도 | 근거 검증등급 | 핵심 근거(evidence_id) |
|------|----------|:---:|:---:|------|
| CollPlant Biotechnologies Ltd. | 직접사업 | 상 | 🟢상 | EV-CLP-001, EV-CLP-002, EV-CLP-003 |
| 셀론텍 (Cellontech, 구 세원셀론텍) | 직접사업 | 상 | 🟢상 | EV-CLT-001, EV-CLT-002, EV-CLT-003 |
| Rousselot (Darling Ingredients Inc. 브랜드) | 직접사업 | 상 | 🟢상 | EV-ROU-001, EV-ROU-002, EV-ROU-003 |
| Advanced BioMatrix, Inc. | 직접사업 | 상 | 🟢상 | EV-ABM-001, EV-ABM-002, EV-ABM-003 |
| Geistlich Pharma AG | 직접사업 | 상 | 🟢상 | EV-GEI-001, EV-GEI-002, EV-GEI-003 |
| GELITA AG | 직접사업 | 상 | 🟢상 | EV-GEL-001, EV-GEL-002, EV-GEL-003 |
| Integra LifeSciences Holdings Corporation | 직접사업 | 상 | 🟢상 | EV-INT-001, EV-INT-002, EV-INT-003 |
| Regenity Biosciences (구 Collagen Matrix, Inc.) | 직접사업 | 상 | 🟠중 | EV-RGN-001, EV-RGN-002, EV-RGN-003 |
| 한스바이오메드 (Hans Biomed Corp.) | 직접사업 | 상 | 🟢상 | EV-HAN-002, EV-HAN-003, EV-HAN-006 |
| Nitta Gelatin Inc. | 직접사업 | 상 | 🟢상 | EV-NIT-001, EV-NIT-002, EV-NIT-003 |
| 주식회사 제네웰 (Genewel Co., Ltd.) | 직접사업 | 상 | 🟢상 | EV-GNW-002, EV-GNW-003, EV-GNW-005 |
| 엘앤씨바이오 (L&C Bio Co., Ltd., 290650) | 직접사업 | 상 | 🟢상 | EV-LNC-001, EV-LNC-003, EV-LNC-004 |
| Aroa Biosurgery Limited | 직접사업 | 상 | 🟢상 | EV-ARO-001, EV-ARO-003, EV-ARO-004 |
| Baxter International Inc. — Advanced Surgery | 직접사업 | 상 | 🟢상 | EV-BAX-002, EV-BAX-003, EV-BAX-006 |
| BIO INX | 직접사업 | 상 | 🟢상 | EV-BIX-002, EV-BIX-003, EV-BIX-004 |
| CELLINK (BICO Group AB) | 직접사업 | 상 | 🟢상 | EV-CEL-002, EV-CEL-003, EV-CEL-004 |
| Evonik Industries AG — Health Care | 직접사업 | 상 | 🟢상 | EV-EVO-002, EV-EVO-004, EV-EVO-006 |
| 주식회사 제노스 (Genoss Co., Ltd.) | 직접사업 | 상 | 🟢상 | EV-GNS-002, EV-GNS-003, EV-GNS-005 |
| Organogenesis Holdings Inc. | 직접사업 | 상 | 🟢상 | EV-ORG-003, EV-ORG-004, EV-ORG-008 |
| Smith+Nephew plc — Advanced Wound Management | 직접사업 | 상 | 🟢상 | EV-SNP-002, EV-SNP-003, EV-SNP-004 |
| Gelatex Technologies OÜ | 직접사업 | 상 | 🟢상 | EV-GLX-001, EV-GLX-002, EV-GLX-003 |
| Johnson & Johnson MedTech (Ethicon) | 직접사업 | 상 | 🟢상 | EV-JNJ-003, EV-JNJ-004, EV-JNJ-005 |
| 티앤알바이오팹 (T&R Biofab Co., Ltd.) | 직접사업 | 상 | 🟢상 | EV-TNR-003, EV-TNR-004, EV-TNR-006 |
| Vericel Corporation | 직접사업 | 상 | 🟢상 | EV-VER-002, EV-VER-003, EV-VER-005 |
| 3D Systems Corporation (Healthcare) | 직접연구 | 상 | 🟢상 | EV-3DS-003, EV-3DS-008, EV-3DS-009 |
| 주식회사 시지바이오 (CGBio) | 직접사업 | 상 | 🟠중 | EV-CGB-002, EV-CGB-003, EV-CGB-001 |
| Keenova Therapeutics plc (구 Mallinckrodt) | 직접사업 | 상 | 🟢상 | EV-KEE-003, EV-KEE-004, EV-KEE-005 |
| MiMedx Group, Inc. | 직접사업 | 상 | 🟢상 | EV-MMX-001, EV-MMX-004, EV-MMX-005 |
| Corza Medical | 직접사업 | 상 | 🟢상 | EV-COR-002, EV-COR-004, EV-COR-005 |
| Aleph Farms Ltd | 직접연구 | 상 | 🟢상 | EV-ALE-004, EV-ALE-007, EV-ALE-002 |
| Becton, Dickinson and Company (BD) | 직접사업 | 상 | 🟢상 | EV-BD-003, EV-BD-004, EV-BD-005 |
| 티센바이오팜 (TissenBioFarm Co., Ltd.) | 인접·응용 | 중 | 🟢상 | EV-TBF-006, EV-TBF-002, EV-TBF-001 |
| 로킷헬스케어 (ROKIT Healthcare, Inc.) | 인접·응용 | 중 | 🟠중 | EV-ROK-002, EV-ROK-004, EV-ROK-005 |
| Advanced Solutions Life Sciences, LLC | 인접·응용 | 중 | 🟢상 | EV-ASL-001, EV-ASL-004, EV-ASL-005 |
| 주식회사 제테마 (Jetema Co., Ltd.) | 인접·응용 | 중 | 🟠중 | EV-JET-003, EV-JET-004, EV-JET-005 |
| 다나그린 (DaNAgreen Co., Ltd.) | 인접·응용 | 중 | 🟠중 | EV-DNG-001, EV-DNG-002, EV-DNG-006 |
| Artivion, Inc. (구 CryoLife) | 인접·응용 | 중 | 🟢상 | EV-ART-005, EV-ART-006, EV-ART-002 |
| 휴메딕스 (Humedix Co., Ltd.) | 인접·응용 | 중 | 🟠중 | EV-HUM-003, EV-HUM-004, EV-HUM-013 |
| Nexture Bio, Inc. (formerly Matrix Meats / Matrix Food Technologies) | 인접·응용 | 중 | 🟢상 | EV-NXT-005, EV-NXT-007, EV-NXT-013 |
| RegenHU (REGENHU AG) | 인접·응용 | 중 | 🟠중 | EV-RGH-003, EV-RGH-004, EV-RGH-005 |
| 테고사이언스 (Tego Science, Inc.) | 인접·응용 | 중 | 🟢상 | EV-TEG-004, EV-TEG-003, EV-TEG-005 |
| Medtronic plc | 인접·응용 | 중 | 🟢상 | EV-MDT-004, EV-MDT-002, EV-MDT-003 |
| 스페이스에프 (Space F Corp.) | 인접·응용 | 중 | 🟠중 | EV-SPF-003, EV-SPF-007, EV-SPF-011 |
| 씨위드 (SeaWith, Inc.) | 인접·응용 | 중 | 🟢상 | EV-SEA-004, EV-SEA-006, EV-SEA-007 |

## 3. 기업별 상세 (5영역 조사 사실 + 검증등급 + 아이템 판정)

각 사실 뒤 대괄호는 검증등급(상/중/하). 아이템 판정은 연관성 분석관(③) 산출.

### 3D Systems Corporation (Healthcare)

연관 판정 — **mTG**: 무관/하 · **ADC**: 무관/하 · **Collagen**: 직접연구/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-3DS-001 | 사업분야 | 3D Systems는 적층제조(3D프린팅) 기업으로 Healthcare 부문(치과·MedTech·재생의학)이 주요 성장 축이며 2026 1분기 매출 약 9,550만 달러를 기록했다. | IR·공시 | 🟠중 | [3D Systems Q1 2026 Earnings (GlobeNewswire/Nasdaq 요약)](https://www.sec.gov/Archives/edgar/data/0000910638/000162828026033666/a3dq12026earningsrelease.htm) |
| EV-3DS-002 | 사업분야 | 3D Systems 헬스케어는 10년 이상 15만+ 환자맞춤 수술계획, 200만+ 임플란트·기구 제조, 100+ FDA/CE 인증 의료기기를 ISO13485 인증 시설에서 생산한다. | 주요언론 | 🟠중 | [Med-Tech Insights](https://med-techinsights.com/2025/06/26/3d-systems-advances-bioprinting-tech-for-first-of-its-kind-nerve-repair/) |
| EV-3DS-003 | 연구분야 | 3D Systems 재생의학은 콜라겐 등 단백질을 스캐폴드 원료로 하는 바이오프린팅과 고해상도 혈관화 하이드로겔 스캐폴드를 세포로 관류하는 'Print to Perfusion' 공정을 개발했다. | 공식홈페이지 | 🟢상 | [3D Systems 보도자료 / 3D Printing Industry](https://www.3dsystems.com/press-releases/3d-systems-announces-breakthrough-bioprinting-technology-and-expansion-0) |
| EV-3DS-004 | 연구분야 | 3D Systems는 2022년 자회사 Systemic Bio를 설립해 하이드로겔·인간세포 기반 혈관화 장기모델(h-VIOS, human vascularized integrated organ systems) organ-on-a-chip 플랫폼을 신약개발용으로 개발했다. | IR·공시 | 🟢상 | [3D Systems / GlobeNewswire, VoxelMatters](https://www.globenewswire.com/news-release/2022/09/08/2512940/0/en/3D-Systems-Announces-Formation-of-New-Biotech-Company-Systemic-Bio-to-Accelerate-Drug-Discovery-and-Development.html) |
| EV-3DS-011 | 연구분야 | 3D Systems가 미생물 트랜스글루타미나제(mTG)를 콜라겐/젤라틴 가교나 스캐폴드 제조에 사용한다는 직접 근거는 확인되지 않았으며, 자사 대표 공정은 광중합(photopolymer) 기반 Print to Perfusion이다. | 논문 | 🔴하 | [학술 문헌(TG-콜라겐 가교) / 3D Systems 보도자료 대조](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11408190/) |
| EV-3DS-012 | 연구분야 | 3D Systems는 항체-약물 접합체(ADC) 파이프라인이나 부위특이적 접합·링커 기술을 보유·공급한다는 근거가 없다(사업은 3D프린팅·재생의학·조직스캐폴드에 국한). | 기타 | 🔴하 | [웹검색 대조(3D Systems + ADC/oncology)](https://www.3dsystems.com/bioprinting) |
| EV-3DS-005 | 뉴스·동향 | 3D Systems는 2025년 7월 시장 역풍·단기수익성 재편을 이유로 자회사 Systemic Bio 운영을 종료했고 창업자 Taci Pereira가 사임했다. | 주요언론 | 🟠중 | [3D Printing Industry / 3DPrint.com / 3D ADEPT](https://3dprintingindustry.com/news/3d-systems-shuts-down-systemic-bio-amid-strategic-shift-taci-pereira-steps-down-242517/) |
| EV-3DS-006 | 뉴스·동향 | 2025년 6월 FDA는 3D Systems·TISSIUM이 공동개발한 무봉합·무외상 말초신경 복구용 3D프린팅 생분해성 기기 COAPTIUM CONNECT with TISSIUM Light에 De Novo 승인을 부여했다. | 주요언론 | 🟠중 | [TISSIUM 보도자료 / 3D Printing Industry](https://3dprintingindustry.com/news/3d-systems-and-tissium-receive-fda-approval-for-first-of-its-kind-peripheral-nerve-repair-device-241261/) |
| EV-3DS-007 | IP·특허 | 3D Systems의 콜라겐 바이오프린팅 관련 특정 등록특허 번호를 공개 DB에서 확정하지 못했다(관련 콜라겐 잉크 특허 US12173048은 Shu-Tung and Alice Li Foundation에 귀속, 3D Systems 아님). | 특허 | 🔴하 | [USPTO / Justia 특허검색](https://patents.justia.com/patent/20240261475) |
| EV-3DS-008 | 파트너십·M&A | 3D Systems는 재조합 인간 콜라겐(rhCollagen) 바이오잉크 개발사 CollPlant와 2020년 공동개발협약을 맺고 2021년 유방재건용 3D 바이오프린팅 연조직 매트릭스 공동개발 계약으로 확대했다. | 공식홈페이지 | 🟢상 | [3D Systems / PRNewswire / GlobeNewswire](https://www.3dsystems.com/press-releases/3d-systems-and-collplant-enter-co-development-agreement-deliver-bioprinted-solutions) |
| EV-3DS-009 | 파트너십·M&A | 3D Systems는 2017년부터 United Therapeutics와 협업해 rhCollagen 기반 3D프린팅 폐·장기 스캐폴드를 개발했으며, United Therapeutics는 CollPlant 콜라겐 바이오잉크를 신장 프린팅용으로 300만 달러에 독점 라이선스했다. | IR·공시 | 🟢상 | [United Therapeutics IR / 3D Printing Industry](https://ir.unither.com/press-releases/2017/04-26-2017-151606851) |
| EV-3DS-010 | 파트너십·M&A | 3D Systems는 프랑스 MedTech TISSIUM과 협업해 자사 재생의학 바이오프린팅 기술과 TISSIUM의 생체모방 프로그래머블 폴리머를 결합한 말초신경 복구 기기를 공동개발했다. | 주요언론 | 🟠중 | [Med-Tech Insights / 3D Printing Industry](https://med-techinsights.com/2025/06/26/3d-systems-advances-bioprinting-tech-for-first-of-its-kind-nerve-repair/) |

### Advanced BioMatrix, Inc.

연관 판정 — **mTG**: 인접·응용/하 · **ADC**: 무관/하 · **Collagen**: 직접사업/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-ABM-001 | 사업분야 | Advanced BioMatrix는 콜라겐 등 고순도 천연 세포외기질(ECM) 단백질을 추출·제조해 세포배양·3D 바이오프린팅·조직공학·신약개발용 시약으로 공급하는 기업이다. | 주요언론 | 🟠중 | [San Diego Business Journal / 회사 소개](https://www.sdbj.com/technology/advanced-biomatrix-acquired-15-million/) |
| EV-ABM-002 | 사업분야 | 주력 제품군은 PureCol, TeloCol, VitroCol 등 Type I 콜라겐 용액으로 2D/3D 세포배양용 매트릭스로 판매된다. | 공식홈페이지 | 🟠중 | [공식 홈페이지 (Collagen / PureCol 제품 페이지)](https://advancedbiomatrix.com/collagen/) |
| EV-ABM-003 | 사업분야 | Lifeink 시리즈(Lifeink 200/220/240)는 압출식 3D 바이오프린팅용 순수 Type I 콜라겐 바이오잉크로, 세계 최초의 순수 콜라겐 바이오잉크로 홍보된다. | 공식홈페이지 | 🟢상 | [공식 홈페이지 (Bioprinting)](https://advancedbiomatrix.com/bioprinting/) |
| EV-ABM-004 | 연구분야 | 핵심 기술 플랫폼은 광가교형 콜라겐/젤라틴(PhotoCol 메타크릴레이트 콜라겐, PhotoGel/GelMA)으로, 라이신 잔기 아민을 메타크릴화해 광가교로 강성을 조절하는 하이드로겔이다. | 공식홈페이지 | 🟢상 | [공식 홈페이지 (PhotoCol 제품) / Sigma-Aldrich](https://advancedbiomatrix.com/photocol-only.html) |
| EV-ABM-005 | 연구분야 | 가교(crosslinking) 시약으로 광개시제(LAP, Irgacure 2959, Ruthenium, Xcite)와 PEGDA·Extralink(티올반응성)를 판매하며, 가교 방식은 효소가 아닌 광화학·화학 가교 중심이다. | 공식홈페이지 | 🟢상 | [공식 홈페이지 (Reagents / Photoinitiators)](https://advancedbiomatrix.com/reagents/) |
| EV-ABM-006 | 연구분야 | 회사의 콜라겐 필름 교육 콘텐츠는 콜라겐 가교법으로 글루타르알데하이드(전형적)와 함께 genipin, EDC/NHS, transglutaminase, glyoxal, riboflavin 등을 '연구되는 방법'으로 언급한다. | 공식홈페이지 | 🟠중 | [공식 홈페이지 (Collagen Films)](https://advancedbiomatrix.com/collagen-films.html) |
| EV-ABM-009 | 뉴스·동향 | 최근 동향으로 2024년 5월 Nanoscribe-Advanced BioMatrix 협업 발표가 있었으며 고해상도 바이오프린팅용 광가교 바이오레진 포트폴리오 확장이 진행됐다. | 주요언론 | 🟠중 | [News-Medical](https://www.news-medical.net/news/20240516/Nanoscribe-partners-with-Advanced-BioMatrix-to-offer-4-new-bioresins-for-Quantum-X-bio.aspx) |
| EV-ABM-010 | IP·특허 | Advanced BioMatrix Inc이 출원인인 콜라겐 바이오잉크 특허 WO2018071639A1('3-D printing inks made from natural extracellular matrix molecules', 우선일 2016-10-12)이 US11850324B2로 등록됐다. | 특허 | 🟢상 | [Google Patents](https://patents.google.com/patent/WO2018071639A1/en) |
| EV-ABM-011 | IP·특허 | ADC(항체-약물 접합체) 또는 mTG 효소 관련 특허·제품·파이프라인은 Advanced BioMatrix에서 확인되지 않는다. | 기타 | 🟠중 | [복합 검색 (Google Patents / 공식 홈페이지)](https://patents.google.com/patent/WO2018071639A1/en) |
| EV-ABM-007 | 파트너십·M&A | Advanced BioMatrix는 2021년 8월 스웨덴 바이오컨버전스 그룹 BICO(구 CELLINK)에 약 1,500만 달러에 인수되어 BICO 계열사가 되었다. | 주요언론 | 🟠중 | [BICO 보도자료 / San Diego Business Journal](https://bico.com/bico-in-the-press/advanced-biomatrix-acquired-by-bico-for-15m/) |
| EV-ABM-008 | 파트너십·M&A | 2024년 5월 Advanced BioMatrix는 Nanoscribe(BICO 계열)와 협업해 2광자중합(2PP) Quantum X bio 바이오프린터용 4종 바이오레진(PhotoChitosan, PhotoDextran, PhotoHA-Stiff, PhotoGel)을 공급했다. | 주요언론 | 🟠중 | [News-Medical / Nanoscribe](https://www.news-medical.net/news/20240516/Nanoscribe-partners-with-Advanced-BioMatrix-to-offer-4-new-bioresins-for-Quantum-X-bio.aspx) |

### Advanced Solutions Life Sciences, LLC

연관 판정 — **mTG**: 인접·응용/하 · **ADC**: 무관/하 · **Collagen**: 인접·응용/중

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-ASL-001 | 사업분야 | Advanced Solutions의 주력 사업은 특허·cGMP 인증 6축 로봇 3D 바이오프린팅 플랫폼 'BioAssemblyBot(BAB)'으로 조직·장기 구조물을 제작하는 것이다. | 공식홈페이지 | 🟢상 | [Advanced Solutions 공식 홈페이지](https://www.advancedsolutions.com/3d-bioprinting) |
| EV-ASL-002 | 사업분야 | 제품군은 BioAssemblyBot 200/400/500 바이오프린터, TSIM(Tissue Structure Information Modeling) 3D 설계 소프트웨어, BioApps 및 프린팅 소모품(supplies)으로 구성된다. | 공식홈페이지 | 🟢상 | [Advanced Solutions 공식 홈페이지 / 언론](https://www.advancedsolutions.com/bioassemblybot-200) |
| EV-ASL-003 | 사업분야 | Angiomics는 지방유래 인간 미세혈관 단편(haMV)을 냉동보존한 조직 혈관화 제품으로, BioAssemblyBot 플랫폼과 결합해 혈관화 조직 모델링에 사용된다. | 공식홈페이지 | 🟢상 | [Advanced Solutions 공식 홈페이지(Microvessels)](https://www.advancedsolutions.com/microvessels) |
| EV-ASL-004 | 연구분야 | BioAssemblyBot 플랫폼은 조직공학·재생의학용으로 콜라겐/젤라틴 기반 바이오잉크(예: Type I 콜라겐, LifeSupport 젤라틴 지지욕 FRESH 프린팅)를 사용해 3D 조직 구조를 프린팅한다. | 논문 | 🟠중 | [MDPI Biomimetics / bioRxiv 논문 및 Advanced BioMatrix](https://pmc.ncbi.nlm.nih.gov/articles/PMC12028034/) |
| EV-ASL-005 | 연구분야 | ASL는 VA와 함께 비합성·혈관화·3D 바이오프린팅 가능한 이식용 뼈 'BioBone'(혈관화 골조직) 개발을 수행 중이다. | 규제기관 | 🟢상 | [VA Puget Sound (미 보훈부) 보도자료](https://www.va.gov/puget-sound-health-care/news-releases/va-puget-sound-health-care-systems-va-ventures-partners-with-advance-solutions-life-science-to-bring-3d-printed/) |
| EV-ASL-011 | 연구분야 | 미생물 트랜스글루타미나제(mTG)는 젤라틴·콜라겐 바이오잉크의 효소 가교제로 바이오프린팅 분야에서 널리 쓰이나, ASL의 제품·특허·논문에서 mTG를 직접 취급한다는 근거는 발견되지 않았다. | 논문 | 🟠중 | [PMC 문헌(일반 바이오프린팅 mTG 가교)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5554441/) |
| EV-ASL-012 | 연구분야 | ADC(항체-약물 접합체) 관련 파이프라인·링커/접합기술·mTG 공급 등 종양학 모달리티와의 접점은 ASL에서 전혀 확인되지 않았다. | 기타 | 🟠중 | [조사관 종합(검색 무발견)](https://www.advancedsolutions.com/) |
| EV-ASL-010 | 뉴스·동향 | ASL는 2025년 NH Tech Alliance 'Product of the Year'를 3D 바이오프린팅 BioAssembly 플랫폼(AI 기반 소프트웨어·BAB500)으로 수상했다. | 주요언론 | 🟠중 | [NH Tech Alliance / 언론 보도](https://www.advancedsolutions.com/) |
| EV-ASL-006 | IP·특허 | ASL는 '3D 프린팅된 생물학·공학 소재 경화용 모듈형 광원(Modular light source for curing of 3D printed biological and engineered materials)' 특허 US11,623,400을 보유한다. | 특허 | 🟢상 | [USPTO / Justia Patents](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11623400) |
| EV-ASL-007 | IP·특허 | ASL 특허 포트폴리오는 바이오프린터 로봇 엔드이펙터(교체형 '핸드')·센싱·모듈형 스테이지 등 하드웨어 중심이다(예: US20210205995 Robot End-Effector Sensing and Identification). | 특허 | 🟠중 | [Justia Patents (assignee: Advanced Solutions Life Sciences, LLC)](https://patents.justia.com/assignee/advanced-solutions-life-sciences-llc) |
| EV-ASL-008 | 파트너십·M&A | 2023년 1월 ASL와 Molecular Devices(Danaher 계열)가 협업, BAB400 for Drug Discovery를 ImageXpress 이미징과 통합해 오가노이드 신약탐색 자동화 기술로 상용화한다고 발표했다. | 주요언론 | 🟠중 | [PRWeb / Bio-IT World 보도자료](https://www.bio-itworld.com/pressreleases/2023/01/06/molecular-devices-and-advanced-solutions-life-sciences-collaborate-to-develop-3d-biology-automation-technologies-for-drug-discovery) |
| EV-ASL-009 | 파트너십·M&A | ASL는 미 보훈부 VA Puget Sound(VA Ventures/x_labs)와 파트너십을 맺어 point-of-care 3D 바이오프린팅 골조직(BioBone) 시설을 구축했다. | 규제기관 | 🟢상 | [VA Puget Sound (미 보훈부)](https://www.va.gov/puget-sound-health-care/stories/va-puget-sound-unveils-nation-leading-3d-bioprinting-facility-to-transform-veteran-care/) |

### Aleph Farms Ltd

연관 판정 — **mTG**: 인접·응용/중 · **ADC**: 무관/하 · **Collagen**: 직접연구/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-ALE-001 | 사업분야 | Aleph Farms는 세포를 배양해 통살(whole-cut) 배양 소고기 스테이크를 만드는 이스라엘 배양육 기업이며, 소비자 브랜드는 'Aleph Cuts'(주력 제품 Petit Steak)이다. | 공식홈페이지 | 🟢상 | [Aleph Farms 공식 홈페이지 / Wikipedia](https://aleph-farms.com/) |
| EV-ALE-002 | 사업분야 | 배양 스테이크는 대두·밀 식물성 단백 매트릭스(스캐폴드)에 세포를 시딩하여 세포 부착·증식·분화를 유도하고, 이 스캐폴드가 동물의 세포외기질(ECM)을 대체해 고기의 조직·식감을 형성한다. | 공식홈페이지 | 🟢상 | [Aleph Farms 'Our Recipe' / Green Matters](https://aleph-farms.com/our-recipe/) |
| EV-ALE-003 | 연구분야 | 핵심 기술 플랫폼은 Technion의 Shulamit Levenberg 교수 연구실 원천기술로, 대두 단백 다공성 스캐폴드에 소 세포를 부착·증식시켜 3~4주 만에 근조직을 형성하는 방법이며 Nature Food에 발표되었다. | 논문 | 🟢상 | [American Technion Society / Lab Manager](https://ats.org/our-impact/tissue-breakthrough-for-ethical-steak/) |
| EV-ALE-004 | 연구분야 | Aleph Farms는 '전체 소를 대체' 전략의 일환으로 배양(세포 기반) 콜라겐 플랫폼을 개발했다. 살아있는 소의 세포에서 도축 없이 자연 동일 콜라겐(세포외기질 포함)을 생산하며, deep-tech 인큐베이터 Aleph Frontiers의 첫 산물로 2024년 상용화를 목표했다. | 주요언론 | 🟠중 | [Aleph Farms 보도자료 (Businesswire) / vegconomist](https://www.businesswire.com/news/home/20220316005177/en/Aleph-Farms-Reveals-Its-Strategy-to-Replace-the-Whole-Cow-as-an-Alternative-to-Intensive-Cattle-Farming) |
| EV-ALE-005 | 연구분야 | Aleph Farms는 2019년 3D Bioprinting Solutions와 협업해 ISS(국제우주정거장) 무중력에서 소 근조직을 3D 바이오프린팅했으며, 적층된 섬유 구조를 유지하기 위해 가교 효소인 트랜스글루타미나제(transglutaminase)를 사용했다. | 주요언론 | 🟠중 | [Food Navigator / Food Bioengineering(Wiley) 리뷰](https://www.foodnavigator.com/Article/2019/10/08/Aleph-Farms-prints-lab-meat-in-space/) |
| EV-ALE-008 | 뉴스·동향 | Aleph Farms는 2023년 12월 이스라엘 보건부의 'no questions' 레터를 받아 세계 최초로 배양 소고기(Aleph Cuts)에 대한 규제 승인을 확보했다. | 주요언론 | 🟠중 | [TechCrunch / Food Navigator / Aleph Farms](https://techcrunch.com/2024/01/17/aleph-farms-cultivated-beef-process-regulatory-approval-israel/) |
| EV-ALE-009 | 뉴스·동향 | 2023년 이후 배양육 업황 악화·현금 부족으로 Aleph Farms는 반복적 감원(피크 약 140명→수십 명)과 '자산경량(asset-light)' 외주 전략으로 전환했고, 스위스 The Cultured Hub 생산기지 및 태국 규제 신청(2026년 중반 승인 기대)을 추진 중이다. | 주요언론 | 🟠중 | [Green Queen / Calcalist(Ctech) / AgFunderNews](https://www.greenqueen.com.hk/aleph-farms-explains-latest-layoffs-as-global-alignment-of-asset-light-strategy/) |
| EV-ALE-006 | IP·특허 | Aleph Farms 특허 US20200140810A1 'Cultured meat compositions'(출원 2018-07-15, 공개 2020-05-07)는 다공성 텍스처 단백 스캐폴드(대두 단백 등)에 근원세포 등 다세포 조직이 부착된 식용 조성물을 청구하며, 세포 부착 강화용 응고제로 thrombin/fibrin을 언급한다. | 특허 | 🟢상 | [Google Patents US20200140810A1](https://patents.google.com/patent/US20200140810A1/en) |
| EV-ALE-007 | IP·특허 | Aleph Farms 특허 포트폴리오는 배양육 조성물, 다능성 세포응집체, 대규모 배양 생산법, 조직·장기 프린팅법과 함께 'cell-free animal collagen(무세포 동물 콜라겐)'을 대상으로 하는 패밀리를 포함한다. | 업계리포트 | 🟠중 | [ABA Landslide 'Meat the Future: Patent Landscape of Cultivated Meat' / Rothwell Figg](https://www.americanbar.org/groups/intellectual_property_law/resources/landslide/2024-spring/meat-future-patent-landscape-cultivated-meat/) |
| EV-ALE-010 | 파트너십·M&A | Aleph Farms는 2021년 L Catterton Growth Fund와 DisruptAD가 주도한 1억500만 달러 규모 시리즈 B를 완료했으며, 참여사에 Thai Union·BRF·CJ CheilJedang·Cargill·Strauss Group 등 글로벌 식품·육류 기업이 포함되고 각국 MoU를 체결했다. | 주요언론 | 🟠중 | [PR Newswire / Meat+Poultry](https://www.prnewswire.com/news-releases/aleph-farms-completes-105-million-series-b-funding-round-301326759.html) |
| EV-ALE-011 | 파트너십·M&A | Aleph Farms는 Migros Industrie·Givaudan·Bühler Group의 합작사 The Cultured Hub(스위스 켐프탈)와 MoU를 맺어 유럽 첫 상업 생산기지를 구축 중이며, 2026년 중 기술이전·설비 완료를 목표한다. | 주요언론 | 🟠중 | [Green Queen / Food Business MEA](https://www.foodbusinessmea.com/aleph-farms-to-set-up-cultivated-meat-production-in-switzerland/) |
| EV-ALE-012 | 파트너십·M&A | Aleph Farms는 저비용 통살(whole-cut) 배양 스테이크 상용화를 위해 약 2,900만 달러의 추가 자금을 유치했다(생산 확대·효율 개선 목적). | 주요언론 | 🟠중 | [AgFunderNews / Cultivated X](https://agfundernews.com/exclusive-aleph-farms-raises-30m-unveils-lower-cost-version-of-whole-cut-technology) |

### Aroa Biosurgery Limited

연관 판정 — **mTG**: 무관/하 · **ADC**: 무관/하 · **Collagen**: 직접사업/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-ARO-001 | 사업분야 | Aroa Biosurgery는 양(ovine) 전위(forestomach) 유래 탈세포 ECM(AROA ECM/OFM)을 기반으로 창상치유·성형재건·탈장수복용 의료기기를 개발·판매하는 연조직 재생 기업이다. | 공식홈페이지 | 🟢상 | [Aroa Biosurgery 공식 홈페이지 (AROA ECM)](https://aroa.com/aroa-ecm/) |
| EV-ARO-002 | 사업분야 | 제품 포트폴리오는 창상치유(Endoform Natural/Antimicrobial, Symphony), 성형·재건외과(Myriad Matrix/Forme/Morcells, OviTex PRS), 탈장수복(OviTex, Myriad Ultra)으로 구성된다. | 기타 | 🔴하 | [Wikipedia — Aroa Biosurgery](https://en.wikipedia.org/wiki/Aroa_Biosurgery) |
| EV-ARO-003 | 연구분야 | AROA ECM(OFM)은 콜라겐을 핵심 구조단백질로 하는 탈세포 ECM으로, 24종 이상의 콜라겐(주로 type I·III)을 포함한 150여 개 ECM 단백질(매트리솜)을 보유한다. | 논문 | 🟢상 | [Journal of Biomaterials Applications — Further structural characterization of OFM (PMC8721687)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8721687/) |
| EV-ARO-004 | 연구분야 | OFM은 합성재료 첨가나 콜라겐 가교(crosslinking) 없이 천연(non-crosslinked) dECM 구조·생물학을 보존하는 제조공정으로 만들어진다. | 논문 | 🟢상 | [In-vivo evaluation of a reinforced ovine biologic (PMC7701079)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7701079/) |
| EV-ARO-005 | 연구분야 | Endoform/AROA ECM 플랫폼이 줄기세포(중간엽 기질세포)를 유인하며 데코린 유래 주화성 인자를 보유함을 전임상 연구로 제시했다. | 논문 | 🟢상 | [Business Wire / PLOS One (decorin chemotactic factor)](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0235784) |
| EV-ARO-011 | 연구분야 | Aroa의 사업·연구·특허 전반에서 항체-약물 접합체(ADC) 파이프라인, 링커·페이로드 접합기술, mTG 기반 부위특이적 접합 관련 활동은 확인되지 않았다. | 공식홈페이지 | 🟠중 | [복수 출처 종합(공식 홈페이지·Wikipedia·FY26 IR·특허)](https://aroa.com/about-aroa/) |
| EV-ARO-008 | 뉴스·동향 | FY26(2026-03-31 종료) 매출 NZ$104M(23% 성장), Myriad 계열 NZ$49.5M(54% 성장), 정상화 EBITDA NZ$13M으로 2년 연속 흑자를 기록했다. | 주요언론 | 🟠중 | [Kalkine / Listcorp (ASX:ARX FY26 Appendix 4E)](https://www.listcorp.com/asx/arx/aroa-biosurgery-limited/news/fy26-appendix-4e-and-full-year-results-3357029.html) |
| EV-ARO-009 | 뉴스·동향 | 만성창상용 Symphony(콜라겐/ECM 기반)의 무작위대조시험(RCT)이 진행 중이며 데이터 발표가 예정되어 중기 성장동력으로 육성 중이다. | 주요언론 | 🟠중 | [Quartr / Kalkine (ARX H1 FY26 요약)](https://kalkine.com.au/news/healthcare/aroa-biosurgery-asxarx-beats-fy26-guidance-as-myriad-drives-54-growth-surge) |
| EV-ARO-006 | IP·특허 | 핵심 원천특허 US8415159B2 'Tissue scaffolds derived from forestomach extracellular matrix'(2008 우선권, WO2010014021A1)가 Aroa(구 Mesynthes)에 귀속된다. | 특허 | 🟢상 | [Google Patents — US8415159B2](https://patents.google.com/patent/US8415159B2/und) |
| EV-ARO-007 | IP·특허 | Aroa는 콜라겐/ECM 기반 이식재 조성 관련 특허 패밀리를 보유하며, USPTO 공개 특허 US11628237(Collagen compositions and uses for biomaterial implants)가 확인된다. | 특허 | 🟠중 | [USPTO — US11628237 (Collagen compositions for biomaterial implants)](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11628237) |
| EV-ARO-010 | 파트너십·M&A | TELA Bio와 독점 제조·장기공급·라이선스 계약(2012 체결, 2015 개정)을 맺어 OviTex 강화형 바이오스캐폴드(탈장·복벽·유방재건)를 공동개발·공급한다. | IR·공시 | 🟢상 | [PR Newswire / TELA Bio SEC 10-K](https://www.prnewswire.com/news-releases/tela-bio-begins-commercialization-for-large-size-ovitex-reinforced-bioscaffolds-for-hernia-repair-and-abdominal-wall-reconstruction-after-aroa-biosurgery-receives-510k-clearance-300776055.html) |

### Artivion, Inc. (구 CryoLife)

연관 판정 — **mTG**: 무관/하 · **ADC**: 무관/하 · **Collagen**: 인접·응용/중

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-ART-001 | 사업분야 | Artivion은 심혈관·대동맥 수술에 집중하며 대동맥 스텐트그래프트, 수술용 실런트(BioGlue), On-X 기계판막, 이식용 인체조직 보존의 4개 제품군을 보유한다. | IR·공시 | 🟢상 | [StockTitan (Artivion 10-K 요약)](https://www.stocktitan.net/sec-filings/AORT/10-k-artivion-inc-files-annual-report-e6a155be36c9.html) |
| EV-ART-002 | 사업분야 | Artivion은 두 보고 세그먼트(Medical Devices, Preservation Services)를 운영하며 Preservation Services는 심장·혈관 이식용 인체조직 보존 서비스로 구성된다. | IR·공시 | 🟢상 | [Artivion 10-K / DCFmodeling 요약](https://investors.artivion.com/static-files/3f538d06-c0ed-4be0-9122-8d323831b880) |
| EV-ART-003 | 사업분야 | Artivion의 2024 총매출은 3억8,850만 달러로 전년 대비 GAAP 10% 성장했고, On-X·스텐트그래프트·BioGlue가 성장을 견인했다. | IR·공시 | 🟢상 | [Artivion FY2024 실적 보도자료 (Morningstar/PRNewswire)](https://investors.artivion.com/news-releases/news-release-details/artivion-reports-fourth-quarter-and-full-year-2024-financial) |
| EV-ART-004 | 사업분야 | BioGlue 수술접착제는 45% 소 혈청 알부민(BSA)과 10% 글루타르알데히드 2액형으로, 글루타르알데히드가 조직·알부민 단백질을 가교(crosslink)하여 접착한다. | 논문 | 🟢상 | [PMC 리뷰 / BioGlue IFU (CryoLife)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11059011/) |
| EV-ART-005 | 사업분야 | PhotoFix는 소 심막(bovine pericardium) 기반 이식 패치로, 염료 매개 광산화(photo-oxidation)로 내부 콜라겐 구조를 가교·안정화한다. | 공식홈페이지 | 🟠중 | [Artivion 제품 페이지(검색 스니펫)](https://artivion.com/product/photofix-decellularized-bovine-pericardium/) |
| EV-ART-006 | 연구분야 | PhotoFix 소 심막 패치는 소아 심혈관 수복에 2008~2011년 364명 환자에 490개 사용되어 우수한 성능을 보였으며, 광산화 가교는 글루타르알데히드 독성 부산물을 제거하는 대안 기술이다. | 논문 | 🟠중 | [Medical Product Outsourcing / 임상 문헌](https://www.mpo-mag.com/breaking-news/cryolife-buys-bovine-pericardium-patch-from-genesee-biomedical/) |
| EV-ART-007 | 연구분야 | On-X 기계판막은 그라파이트 기재에 실리콘프리 열분해탄소(pyrolytic carbon)를 코팅한 이엽식 밸브로, Artivion은 타사에 열분해탄소 코팅 OEM 서비스도 제공한다. | 업계리포트 | 🟠중 | [DCFmodeling / Artivion 제품 정보(검색 요약)](https://dcfmodeling.com/products/aort-business-model-canvas) |
| EV-ART-012 | 연구분야 | Artivion의 Preservation Services는 CryoVein·CryoArtery 등 동결보존 인체 혈관/심장 동종조직과 CryoPatch SG 폐동맥 패치를 제공하며, 이들은 콜라겐이 주성분인 자연 인체조직이다. | 공식홈페이지 | 🟠중 | [Artivion 제품 페이지(CryoPatch SG) / 10-K](https://artivion.com/product/cryopatch-sg/) |
| EV-ART-008 | 뉴스·동향 | 2025년 1월 STS 연례회의에서 AMDS PERSEVERE 임상의 1년 데이터(93명)가 발표되어 급성 DeBakey I형 박리 수복에서 지속적 이점을 보였다. | 주요언론 | 🟠중 | [Artivion 보도자료 (PRNewswire)](https://www.prnewswire.com/news-releases/artivion-announces-presentation-of-late-breaking-data-from-amds-persevere-trial-at-the-61st-society-of-thoracic-surgery-annual-meeting-302360153.html) |
| EV-ART-009 | IP·특허 | 심혈관 조직 가교 분야에서 트랜스글루타미나제(TGase)로 콜라겐을 가교하는 특허(US20080305517A1)가 존재하나 이는 Artivion/CryoLife 출원이 아니며, Artivion 자사 조직 가교는 글루타르알데히드·광산화 방식이다. | 특허 | 🟠중 | [Google Patents US20080305517A1](https://patents.google.com/patent/US20080305517A1/en) |
| EV-ART-010 | 파트너십·M&A | Artivion은 PerClot(다당류 지혈 시스템) 자산을 2021년 Baxter에 최대 6,080만 달러에 매각했고, 2023년 FDA PMA 승인 후 PMA를 Baxter에 이전했다. | 주요언론 | 🟠중 | [PRNewswire / Baxter 보도자료](https://www.prnewswire.com/news-releases/artivion-announces-fda-pma-approval-of-perclot-and-transfer-of-pma-to-baxter-301831804.html) |
| EV-ART-011 | 파트너십·M&A | Artivion은 2020년 Ascyrus Medical(AMDS)을 최대 2억 달러에, 2019년 JOTEC(독일 스텐트그래프트)를 약 2.5억 달러에 인수했고, Endospan(NEXUS)과 전략적 파트너십·인수 옵션을 보유한다. | IR·공시 | 🟢상 | [MatrixBCG / StockTitan (Artivion 8-K·10-K)](https://www.stocktitan.net/sec-filings/AORT/8-k-artivion-inc-reports-material-event-7862604323de.html) |

### Baxter International Inc. — Advanced Surgery

연관 판정 — **mTG**: 인접·응용/하 · **ADC**: 무관/하 · **Collagen**: 직접사업/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-BAX-001 | 사업분야 | Advanced Surgery는 Baxter의 Medical Products & Therapies 세그먼트 내 사업부로, 지혈제·실런트·유착방지 제품을 판매하며 2025년 매출 약 11억 달러(전년비 약 5% 성장)를 기록했다. | 주요언론 | 🟠중 | [FinancialContent (predictstreet 분석) / Baxter 실적](https://markets.financialcontent.com/wral/article/predictstreet-2025-12-26-baxter-international-bax-in-2025-a-deep-dive-into-the-transformation-of-a-medtech-giant) |
| EV-BAX-002 | 사업분야 | FLOSEAL 지혈 매트릭스는 소(bovine) 유래 콜라겐을 젤라틴화한 뒤 glutaraldehyde로 가교한 젤라틴 과립과 트롬빈을 결합한 제품이다. | 규제기관 | 🟢상 | [European Medicines Agency (EMA) — FloSeal 심사 문서](https://www.ema.europa.eu/en/documents/other/consultation-ancillary-medicinal-substance-incorporated-medical-device-floseal-haemostatic-matrix-floseal-vh-s-d_en.pdf) |
| EV-BAX-003 | 사업분야 | HEMOPATCH Sealing Hemostat는 소 진피 유래 콜라겐 패드를 NHS-PEG로 코팅한 흡수성 지혈·실링 제품이다. | 주요언론 | 🟠중 | [PR Newswire / Baxter 보도자료](https://www.prnewswire.com/news-releases/baxter-launches-hemopatch-sealing-hemostat-a-room-temperature-collagen-pad-approved-for-hemostasis-and-sealing-suitable-for-open-surgery-and-minimally-invasive-surgical-procedures-mis-302458074.html) |
| EV-BAX-004 | 사업분야 | TISSEEL 및 ARTISS는 인간 혈장 유래 fibrinogen과 thrombin으로 구성된 2성분 fibrin 실런트로, 콜라겐/젤라틴 기반이 아니다. | 규제기관 | 🟢상 | [DailyMed (NLM) / Drugs.com 처방정보](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=b3f69e25-1b87-4507-81fa-582ea084673d) |
| EV-BAX-005 | 사업분야 | COSEAL 및 PREVELEAK은 polyethylene glycol(PEG) 기반 합성 실런트로, Baxter 지혈·실링 포트폴리오의 비(非)콜라겐 축을 구성한다. | 특허 | 🟠중 | [Google Patents (Lifebond US9636433B2, 경쟁제품 언급)](https://patents.google.com/patent/US9636433B2/en) |
| EV-BAX-007 | 연구분야 | Baxter의 젤라틴 기반 지혈제(Floseal)는 glutaraldehyde 가교 화학을 사용하며, 이는 경쟁 기술인 미생물 트랜스글루타미나제(mTG) 가교와는 다른 접근이다. | 논문 | 🟢상 | [PMC — Gelatin-based hemostatic agents 리뷰 / EMA 문서](https://pmc.ncbi.nlm.nih.gov/articles/PMC9767835/) |
| EV-BAX-014 | 연구분야 | Baxter International(및 Advanced Surgery)에서 종양학 항체-약물 접합체(ADC) 파이프라인·링커/접합 기술·mTG 기반 ADC 접합 활동은 확인되지 않았다. | 기타 | 🟠중 | [웹 검색(다중) — 'Baxter International oncology ADC pipeline' 등](https://www.baxter.com/) |
| EV-BAX-006 | 뉴스·동향 | Baxter는 2025년 4~5월 실온 보관(유효기간 3년)이 가능한 신형 HEMOPATCH 콜라겐 지혈·실링 패드를 출시했다. | 주요언론 | 🟠중 | [Business Wire / Baxter 보도자료](https://www.businesswire.com/news/home/20250409022593/en/Baxter-Launches-New-Room-Temperature-Hemopatch-Sealing-Hemostat-for-Rapid-and-Convenient-Application-During-Surgery) |
| EV-BAX-013 | 뉴스·동향 | Baxter는 2025년 초 신장케어(Kidney Care, 신설 Vantive) 사업을 Carlyle에 38억 달러에 매각하고 채무 감축·핵심 사업(Advanced Surgery 포함) 집중으로 전환했다. | 공식홈페이지 | 🟢상 | [Baxter 보도자료 / FinancialContent](https://www.baxter.com/baxter-newsroom/baxter-announces-definitive-agreement-divest-its-vantive-kidney-care-segment) |
| EV-BAX-008 | IP·특허 | 젤라틴-트랜스글루타미나제(mTG) 지혈 드레싱·실런트 특허군(US9636433B2, US9017664B2, US8722039B2 등)은 Lifebond Ltd(현 양수인 Bard Shannon/BD) 소유이며 Baxter 소유가 아니다. | 특허 | 🟢상 | [Google Patents — US9636433B2](https://patents.google.com/patent/US9636433B2/en) |
| EV-BAX-009 | IP·특허 | Baxter International은 지혈 조성물 및 도포 장치 관련 다수 특허(예: US11246958 Haemostatic compositions, US11583610 spray-dried thrombin)를 보유하나, mTG(트랜스글루타미나제) 기반 청구항은 확인되지 않았다. | 특허 | 🟠중 | [USPTO / Google Patents / Justia (Baxter International 양수 특허)](https://patents.justia.com/assignee/baxter-international-inc) |
| EV-BAX-010 | 파트너십·M&A | Baxter는 2021년 CryoLife로부터 PerClot 다당류(polysaccharide) 지혈 시스템을 최대 6,080만 달러에 인수해 Advanced Surgery 포트폴리오를 확장했다. | 주요언론 | 🟠중 | [Business Wire / Baxter 보도자료](https://www.businesswire.com/news/home/20210729005059/en/Baxter-Announces-Acquisition-of-PerClot-Polysaccharide-Hemostatic-System-to-Expand-Advanced-Surgery-Portfolio) |
| EV-BAX-011 | 파트너십·M&A | Baxter는 2018년 Mallinckrodt로부터 RECOTHROM(재조합 트롬빈)과 PREVELEAK 실런트를 인수해 지혈·실런트 라인을 보강했다. | 공식홈페이지 | 🟢상 | [Baxter 보도자료](https://www.baxter.com/baxter-newsroom/baxter-completes-acquistion-recothrom-and-preveleak-broaden-surgical-hemostat-and) |
| EV-BAX-012 | 파트너십·M&A | Baxter는 2019~2020년 Sanofi로부터 Seprafilm 유착방지막(adhesion barrier)을 인수해 Advanced Surgery 포트폴리오를 확장했다. | 주요언론 | 🟠중 | [MassDevice / Baxter 보도자료](https://www.massdevice.com/baxter-completes-seprafilm-acquisition/) |

### Becton, Dickinson and Company (BD)

연관 판정 — **mTG**: 무관/하 · **ADC**: 공급망·파트너/하 · **Collagen**: 직접사업/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-BD-001 | 사업분야 | BD는 의료기기·진단 대기업으로 FY2025 매출 약 218억 달러이며, Medical이 최대 부문(약 114억 달러)이다. | IR·공시 | 🟢상 | [BD Investor Relations / Bullfincher](https://investors.bd.com/news-events/press-releases/detail/915/bd-reports-fourth-quarter-and-full-year-fiscal-2025-financial-results) |
| EV-BD-002 | 사업분야 | BD는 2025년 조직개편으로 5개 글로벌 부문 체계를 도입했고, 이 중 BioPharma Systems가 바이오의약품 약물전달 부문이다. | IR·공시 | 🟢상 | [US SEC (BD Form 10-Q FY2025)](https://www.sec.gov/Archives/edgar/data/0000010795/000001079526000005/bdx-20251231.htm) |
| EV-BD-003 | 사업분야 | BD(구 C.R. Bard/Davol)는 XenMatrix™ Surgical Graft라는 돼지 진피 유래 콜라겐 매트릭스 생체이식재를 탈장 등 연조직 보강용으로 판매한다. | 공식홈페이지 | 🟠중 | [BD 공식 제품 페이지 / Synergy Surgical](https://www.bd.com/en-us/products-and-solutions/products/product-families/xenmatrix-surgical-graft) |
| EV-BD-005 | 사업분야 | BD는 AlloMax™(인체 진피 유래 무세포 콜라겐 스캐폴드)를 재건수술용 연조직 보강재로 보유한다. | 주요언론 | 🟠중 | [MedTech Dive / TorHoerman Law(제품 설명)](https://www.medtechdive.com/news/fda-links-certain-breast-reconstruction-devices-to-risk-of-complications/597706/) |
| EV-BD-006 | 사업분야 | BD BioPharma Systems는 Neopak™ 유리 프리필드 시린지 등 바이오의약품(항체, GLP-1 등) 피하주사 전달 디바이스를 공급한다. | 주요언론 | 🟠중 | [PR Newswire (BD 보도자료) / BD](https://www.prnewswire.com/news-releases/bd-expands-capacity-for-advanced-prefillable-syringes-and-enhances-injection-experience-for-the-next-generation-of-biologics-302250865.html) |
| EV-BD-004 | 연구분야 | XenMatrix 그래프트는 특허받은 AquaPure™ 공정으로 세포를 제거해 강도를 유지한 개방형 콜라겐 스캐폴드를 형성, 조기 세포 침윤·재혈관화를 유도한다. | 규제기관 | 🟢상 | [ClinicalTrials.gov 프로토콜(NCT02691962) / BD](https://cdn.clinicaltrials.gov/large-docs/62/NCT02691962/Prot_000.pdf) |
| EV-BD-010 | 연구분야 | BD와 microbial transglutaminase(mTG)를 직접 연결하는 사업·연구·특허 근거는 확인되지 않았다(mTG 무관 판정 근거). | 기타 | 🟠중 | [복합 검색(BD + transglutaminase)](https://www.sciencedirect.com/topics/immunology-and-microbiology/transglutaminase) |
| EV-BD-007 | 뉴스·동향 | BD는 2026년 1월 바이오의약품 공급망 강화를 위해 미국 내 1.1억 달러 투자를 발표했다. | 공식홈페이지 | 🟢상 | [BD News (보도자료)](https://news.bd.com/2026-01-13-BD-Announces-110-Million-to-Support-U-S-Pharmaceutical-Supply-Chain-for-Biologic-Drugs) |
| EV-BD-009 | IP·특허 | BD/Bard의 콜라겐 그래프트 탈세포화 공정 'AquaPure'는 특허받은 기술로 명시되나, 공개 검색에서 구체 특허번호는 확보하지 못했다. | 규제기관 | 🟠중 | [BD 제품 자료 / ClinicalTrials 프로토콜](https://cdn.clinicaltrials.gov/large-docs/62/NCT02691962/Prot_000.pdf) |
| EV-BD-008 | 파트너십·M&A | BD는 2026년 2월 Biosciences & Diagnostic Solutions 사업을 분사해 Waters와 합병(Reverse Morris Trust, 약 175억 달러)했고 현금 40억 달러를 수령했다. | IR·공시 | 🟢상 | [Yahoo Finance / US SEC (BD 8-K)](https://finance.yahoo.com/news/bd-merges-biosciences-diagnostics-business-183400275.html) |

### BIO INX

연관 판정 — **mTG**: 인접·응용/하 · **ADC**: 무관/하 · **Collagen**: 직접사업/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-BIX-001 | 사업분야 | BIO INX는 벨기에 Ghent(Zwijnaarde) 소재로 Ghent University와 VUB에서 스핀오프한 3D 바이오프린팅용 바이오잉크·재료 상용화 기업이다. | 주요언론 | 🟠중 | [bionity / 3printr / VUB](https://www.bionity.com/en/companies/1043516/bio-inx.html) |
| EV-BIX-002 | 사업분야 | 핵심 제품 GEL-MA INX는 콜라겐 유래 젤라틴(type B) 기반 광가교(photo-crosslinkable) 잉크로, RGD 모티프를 가진 ECM 모사 바이오잉크다. | 공식홈페이지 | 🟠중 | [BIO INX 제품설명(검색 캐시) / ScienceDirect](https://bioinx.com/products/gel-ma-inx) |
| EV-BIX-003 | 사업분야 | BIO INX는 압출·DLP·2광자중합(2PP)·볼류메트릭 등 다양한 프린팅 기술용 잉크 포트폴리오(HYDROBIO INX, READYGEL INX, BIORES INX 등)를 보유하며 고해상도 레이저 기반 바이오프린팅 재료의 시장 선도기업으로 소개된다. | 주요언론 | 🟠중 | [UpNano / VoxelMatters / bionity](https://www.upnano.com/bio-inx-resins/) |
| EV-BIX-004 | 연구분야 | 창업 기술의 학술적 기반으로 CEO Jasper Van Hoorick과 Sandra Van Vlierberghe 등은 재조합 콜라겐(RCPhC1) 광가교 바이오잉크의 고해상도 3D 바이오프린팅 연구를 발표했다. | 논문 | 🟢상 | [Biomacromolecules (ACS) / PubMed](https://pubmed.ncbi.nlm.nih.gov/32841006/) |
| EV-BIX-005 | 연구분야 | 창업진의 핵심 플랫폼 기술은 티올-젤라틴-노르보르넨(thiol-gelatin-norbornene) 광가교 바이오잉크로 레이저 기반 고해상도(2PP) 프린팅을 가능케 한다. | 논문 | 🟢상 | [Biofabrication / Ghent Univ biblio / PubMed](https://pubmed.ncbi.nlm.nih.gov/31347290/) |
| EV-BIX-013 | 연구분야 | BIO INX의 핵심 기질인 젤라틴/GelMA는 학계에서 미생물 트랜스글루타미나제(mTG)로 가교되는 대표 기질이나, mTG-GelMA 제어가교 대표 논문은 NTU 싱가포르(Zhou 등)의 성과로 BIO INX/Ghent 그룹 소속이 아니다. | 논문 | 🟢상 | [Biofabrication (IOPscience) / ResearchGate](https://iopscience.iop.org/article/10.1088/1758-5090/ab063f) |
| EV-BIX-006 | 뉴스·동향 | 2024년 12월경 BIO INX는 젤라틴 기반 DLP 바이오프린팅 레진 BIORES INX를 출시했다. | 주요언론 | 🟠중 | [VoxelMatters / 3Dnatives / BIO INX](https://www.voxelmatters.com/biores-inx-a-new-gelatin-based-dlp-bioprinting-resin/) |
| EV-BIX-007 | 뉴스·동향 | 2025년 5월 BIO INX와 Readily3D는 볼류메트릭 바이오프린팅용 최초 폴리에스터 기반 레진 READYPCL INX를 출시했다. | 주요언론 | 🟠중 | [3printr / VoxelMatters / BIO INX](https://www.3printr.com/polyester-resin-for-volumetric-bioprinting-bio-inx-and-readily3d-introduce-readypcl-inx-3981198/) |
| EV-BIX-008 | 뉴스·동향 | BIO INX는 2광자중합(2PP)으로 매크로스케일 3D 프린팅을 가능케 하는 하이드로겔 레진 HYDROTECH INX N200을 세계 최초로 출시했다고 발표했다. | 공식홈페이지 | 🟠중 | [BIO INX 뉴스(검색 결과)](https://bioinx.com/news/bio-inx-launches-hydrotech-inx-n200-worlds-first-hydrogel-resin-enabling-macroscale-3d) |
| EV-BIX-012 | IP·특허 | BIO INX는 창업자 Van Hoorick과 CSO Aysu Arslan이 박사과정 중 개발·특허화한 3D 바이오프린팅 재료 기술을 기반으로 설립되었다. | 주요언론 | 🟠중 | [3Dnatives / 3printr / BioVox](https://www.3dnatives.com/en/3dstart-up-bio-inx-innovative-bio-inks-for-3d-printing-021120235/) |
| EV-BIX-009 | 파트너십·M&A | BIO INX는 고해상도 볼류메트릭 프린터사 Readily3D와 전략적 협업을 맺고 GelMA 기반 READYGEL INX 등 볼류메트릭 프린팅용 잉크를 공동 개발·상용화한다. | 주요언론 | 🟠중 | [VoxelMatters / TCT Magazine / flanders.bio](https://www.voxelmatters.com/bio-inx-and-readily3d-collaborate-on-bioinks-for-volumetric-bioprinting/) |
| EV-BIX-010 | 파트너십·M&A | BIO INX는 AstroCardia 컨소시엄(SCK CEN, Space Applications Services, QbD Group, Antleron)에서 심장 노화 연구용 heart-on-chip의 미세혈관 구조를 바이오프린팅하며, 2026년 ISS 발사 예정, VLAIO로부터 175만 유로를 확보했다. | 주요언론 | 🟠중 | [3DPrint.com / TCT Magazine / AstroCardia](https://3dprint.com/303076/bioprinted-hearts-in-space-belgiums-quest-to-unlock-the-secrets-of-cardiac-aging/) |
| EV-BIX-011 | 파트너십·M&A | BIO INX는 2022년 첫 자금 라운드로 총 70만 유로(사적 투자 50만 유로 + 국제 그랜트 20만 유로)를 조달했고, 2025년 12월 HealthTech Investor Summit 참가 등 추가 상용화 자금 조달을 진행 중이다. | 업계리포트 | 🟠중 | [BIO INX 뉴스 / Tracxn](https://tracxn.com/d/companies/bio-inx/__f67Jk_o9371LKpuZxmsF0ITGvKK8QSUhOUGbJBUB1cY) |

### CELLINK (BICO Group AB)

연관 판정 — **mTG**: 인접·응용/하 · **ADC**: 무관/하 · **Collagen**: 직접사업/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-CEL-001 | 사업분야 | CELLINK은 3D 바이오프린터와 바이오잉크를 공급하는 글로벌 바이오프린팅 선도기업으로, 스웨덴 상장사 BICO Group의 자회사다. | 공식홈페이지 | 🟢상 | [CELLINK 공식 홈페이지](https://www.cellink.com/) |
| EV-CEL-002 | 사업분야 | CELLINK/Advanced BioMatrix는 Lifeink 시리즈(200/220/240/260) 등 순수 type I 콜라겐 바이오잉크를 상용 판매하며, Lifeink 200·240은 세계 최초 압출식 순수 콜라겐 바이오잉크로 소개된다. | 공식홈페이지 | 🟢상 | [Advanced BioMatrix / CELLINK 제품 페이지](https://advancedbiomatrix.com/lifeink200.html) |
| EV-CEL-003 | 사업분야 | CELLINK은 메타크릴화 젤라틴(GelMA) 기반 바이오잉크(GelMA A/C, GelMA Bioink, PhotoGel 등)와 콜라겐·젤라틴 원료·동결건조 바이오소재를 폭넓게 판매한다. | 공식홈페이지 | 🟢상 | [CELLINK GelMA 제품 페이지](https://www.cellink.com/product/gelma-a/) |
| EV-CEL-013 | 사업분야 | CELLINK이 상용 공급하는 가교제는 알지네이트용 이온성 CaCl2 및 광가교(LAP/UV)이며, 트랜스글루타미나제(mTG) 단독 가교제 제품은 확인되지 않는다. | 공식홈페이지 | 🟠중 | [CELLINK Crosslinking Agent 제품 페이지](https://www.cellink.com/product/crosslinking-agent/) |
| EV-CEL-004 | 연구분야 | CELLINK의 핵심 기술 플랫폼은 콜라겐·젤라틴·GelMA·알지네이트·셀룰로오스 나노섬유 기반 바이오잉크와 조직공학·재생의학용 3D 세포배양 매트릭스다. | 공식홈페이지 | 🟢상 | [CELLINK Bioinks/Tissue Engineering 페이지](https://www.cellink.com/tissue-engineering/) |
| EV-CEL-005 | 연구분야 | CELLINK 바이오프린터·바이오잉크는 약물 스크리닝, 3D 종양·간·신장 조직 모델, organ-on-chip 등 신약개발 응용 연구에 활용된다. | 공식홈페이지 | 🟠중 | [CELLINK Drug Discovery Applications](https://www.cellink.com/bioprinting-applications/streamlining-drug-discovery-with-3d-biomimetic-models/) |
| EV-CEL-012 | 연구분야 | 미생물 트랜스글루타미나제(mTG)는 GelMA·젤라틴 바이오잉크를 효소 가교하여 3D 프린팅 유변물성을 제어하는 기법으로 학계에 확립되어 있다(분야 일반). | 논문 | 🟠중 | [Biofabrication (IOPscience)](https://iopscience.iop.org/article/10.1088/1758-5090/ab063f) |
| EV-CEL-014 | 연구분야 | CELLINK/BICO의 사업·연구 어디에서도 항체-약물 접합체(ADC) 파이프라인, ADC 링커·접합 기술, ADC용 mTG 공급 접점은 확인되지 않는다. | 기타 | 🟠중 | [웹 검색(다중) honest_gap](https://www.cellink.com/news/) |
| EV-CEL-006 | 뉴스·동향 | BICO는 2025년 MatTek·Visikol을 Sartorius에 8천만 달러에 매각하고 사업부를 재편, CELLINK과 Advanced BioMatrix를 Q2 2025부터 'Life Science Solutions' 사업부로 이전했다. | 주요언론 | 🟠중 | [3DPrint.com / Nordic Life Science](https://3dprint.com/317289/bicos-3rd-exit-under-ceo-maria-forss-mattek-and-visikol-to-be-sold-for-80m/) |
| EV-CEL-007 | 뉴스·동향 | BICO Group은 2025년 연간 매출을 24억 SEK 이상으로 안정화했다고 보고하며 바이오프린팅 분야에서 선도적 지위를 유지한다. | IR·공시 | 🟢상 | [BICO Year-end Report 2025 (mfn.se)](https://storage.mfn.se/40e2ffc0-e873-4e7b-9f80-5f32fe52754c/bico-q4-2025-eng.pdf) |
| EV-CEL-008 | IP·특허 | CELLINK은 셀룰로오스 나노섬유 바이오잉크 특허(US10675379B2, 공개 US20170368225A1)를 보유하며, 명세서에 콜라겐·탈세포화 매트릭스 기반 바이오잉크 지지재 응용이 기재된다. | 특허 | 🟢상 | [Google Patents / USPTO](https://patents.google.com/patent/US10675379B2/en) |
| EV-CEL-009 | IP·특허 | CELLINK/BICO는 온도조절 프린트베드로 젤화를 제어하는 특허(US11,046,001)를 보유하며 콜라겐·젤라틴 기반 바이오잉크 응용을 대상으로 한다. | 주요언론 | 🟠중 | [3D Printing Industry / CELLINK IP 보도](https://3dprintingindustry.com/news/bico-granted-two-new-patents-for-3d-bioprinting-with-temperature-sensitive-bioinks-198086/) |
| EV-CEL-010 | IP·특허 | GelMA C(메타크릴화 젤라틴+나노섬유셀룰로오스)는 UPM-Kymmene와 CELLINK Bioprinting이 공동 특허한 조성이다. | 공식홈페이지 | 🟠중 | [CELLINK GelMA C 제품 페이지](https://www.cellink.com/product/gelma-c/) |
| EV-CEL-011 | 파트너십·M&A | CELLINK은 Carcinotech과 파트너십을 맺어 BIO CELLX 시스템 기반 3D 바이오프린팅 종양 모델 프로토콜을 공동 개발·상용화한다. | 공식홈페이지 | 🟠중 | [CELLINK 보도자료](https://www.cellink.com/carcinotech-and-cellink-enter-a-partnership/) |

### CollPlant Biotechnologies Ltd.

연관 판정 — **mTG**: 인접·응용/하 · **ADC**: 무관/하 · **Collagen**: 직접사업/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-CLP-001 | 사업분야 | CollPlant는 비동물유래 rhCollagen 기반 재생·미용의학 기업으로 조직재생 및 메디컬 에스테틱 제품을 개발한다. | 공식홈페이지 | 🟢상 | [CollPlant IR (Company Information)](https://ir.collplant.com/company-information) |
| EV-CLP-002 | 사업분야 | 주력 제품군은 rhCollagen 기반 진피 필러, 3D 바이오프린팅 유방재건 스캐폴드, 바이오잉크(Collink.3D), 건병증 치료제 Vergenix STR이다. | 공식홈페이지 | 🟢상 | [CollPlant 공식 홈페이지 rhCollagen](https://collplant.com/rhcollagen/) |
| EV-CLP-003 | 연구분야 | 인간 프로콜라겐 합성 관련 5개 인간유전자를 담배식물에 도입해 Type I 재조합 인간 콜라겐(rhCollagen)을 대량생산하는 독자 식물기반 플랫폼을 보유한다. | 공식홈페이지 | 🟢상 | [CollPlant Technology - rhCollagen](https://collplant.com/technology/technology-rhcollagen/) |
| EV-CLP-004 | 연구분야 | Collink.3D는 메타크릴아마이드 변형 rhCollagen으로 광경화(photocuring) 방식으로 하이드로겔을 형성하는 바이오잉크이며, 압출·잉크젯·광조형 등 주요 바이오프린팅 기술과 호환된다. | 공식홈페이지 | 🟢상 | [CollPlant Bioinks](https://collplant.com/bioinks/) |
| EV-CLP-005 | 연구분야 | rhCollagen 바이오잉크 기반 재생형 3D 바이오프린팅 유방보형물 스캐폴드를 개발했으며, 2023년 1월 대동물 시험에서 3개월 후 결합조직·신생혈관 형성 등 조직재생을 확인했다. | 주요언론 | 🟠중 | [3D Printing Industry](https://3dprintingindustry.com/news/collplant-develops-first-prototypes-for-regenerative-3d-bioprinted-breast-implants-159645/) |
| EV-CLP-006 | 뉴스·동향 | 2026년 2월 CollPlant는 DLP(디지털광학처리) 바이오프린팅용 즉시출력 rhCollagen 키트 BioFlex를 출시했다. | 주요언론 | 🟠중 | [StockTitan (CLGN)](https://www.stocktitan.net/news/CLGN/coll-plant-elevates-rh-collagen-3d-bioprinting-portfolio-with-launch-skr8xq55q5xx.html) |
| EV-CLP-007 | 뉴스·동향 | 2025년 9개월 매출 약 $2.3M(AbbVie $2.0M 마일스톤 견인), 2025년 9월30일 기준 현금 약 $8.5M을 보고했다. | 주요언론 | 🟠중 | [StockTitan (CLGN) / CollPlant IR](https://www.stocktitan.net/news/CLGN/) |
| EV-CLP-008 | 뉴스·동향 | Mayo Clinic 연구진이 CollPlant의 rhCollagen 바이오잉크로 최초의 완전 인간화 3D 바이오프린팅 피부 모델을 개발했다. | 공식홈페이지 | 🟠중 | [CollPlant IR Press Release](https://ir.collplant.com/news-events/press-releases/detail/186/first-in-kind-fully-humanized-3d-bioprinted-human-skin) |
| EV-CLP-009 | IP·특허 | 미국특허 US 11,801,329는 변형 rhCollagen과 히알루론산 등을 포함하는 중합성 필러 용액을 조직에 주입 후 외부 광으로 in-situ 중합하는 광경화 진피필러 방법을 청구한다. | 특허 | 🟢상 | [CollPlant IR / BioSpace](https://ir.collplant.com/news-events/press-releases/detail/152/collplant-biotechnologies-announces-patent-granted-in-u-s-for-photocurable-dermal-filler) |
| EV-CLP-010 | IP·특허 | 유럽특허청이 CollPlant의 연질조직 필러 및 재생형 유방보형물 후보에 사용되는 콜라겐 기반 제형 특허출원을 허여했다. | 특허 | 🟠중 | [CollPlant IR Press Release](https://ir.collplant.com/news-events/press-releases/detail/177/collplant-biotechnologies-announces-european-patent) |
| EV-CLP-014 | IP·특허 | 'Transglutaminase Crosslinked Collagen Biomaterial'(US20080305517A1) 특허는 Aston University 소유이며 CollPlant와 무관하다 — CollPlant의 콜라겐 가교 방식은 mTG가 아닌 메타크릴레이트 광가교로 확인된다. | 특허 | 🟢상 | [Google Patents US20080305517A1](https://patents.google.com/patent/US20080305517A1/en) |
| EV-CLP-011 | 파트너십·M&A | 2021년 CollPlant는 AbbVie 계열 Allergan Aesthetics와 rhCollagen 진피·연질조직 필러의 독점 글로벌 개발·상업화 계약을 체결했고, 임상단계 진입으로 $10M 마일스톤을 수령했다. | IR·공시 | 🟢상 | [CollPlant / PRNewswire](https://www.prnewswire.com/il/news-releases/collplant-announces-development-and-global-commercialization-agreement-with-allergan-aesthetics-an-abbvie-company-for-rhcollagen-in-dermal-and-soft-tissue-filler-products-301223772.html) |
| EV-CLP-012 | 파트너십·M&A | CollPlant는 3D Systems와 유방재건용 3D 바이오프린팅 연질조직 매트릭스 공동개발 계약을 체결했다. | 주요언론 | 🟠중 | [3D Systems Press Release](https://www.3dsystems.com/press-releases/3d-systems-and-collplant-enter-co-development-agreement-deliver-bioprinted-solutions) |
| EV-CLP-013 | 파트너십·M&A | CollPlant는 STEMCELL Technologies와의 계약을 연구용을 넘어 임상개발 및 상업규모 제조까지 rhCollagen 사용을 확대하도록 확장했다. | 공식홈페이지 | 🟠중 | [CollPlant IR (Company Information)](https://ir.collplant.com/company-information) |

### Corza Medical

연관 판정 — **mTG**: 무관/하 · **ADC**: 무관/하 · **Collagen**: 직접사업/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-COR-001 | 사업분야 | Corza Medical은 봉합사(Quill/Sharpoint/Look), 안과기구(Katena/Blink), 지혈·실런트(TachoSil) 등 수술 기술 플랫폼을 제공하는 글로벌 의료기기 기업이다. | 공식홈페이지 | 🟢상 | [Corza Medical 공식 홈페이지 / 보도자료](https://corza.com/gtcr-and-corza-announce-acquisition-of-katena/) |
| EV-COR-002 | 사업분야 | 핵심 지혈 제품 TachoSil은 말(equine) 콜라겐 스펀지에 인간 피브리노겐과 트롬빈을 코팅한 국소 피브린 실런트 패치다. | 규제기관 | 🟢상 | [Corza 제품페이지 / TachoSil FDA 처방정보(medlibrary·rxdruglabels)](https://medlibrary.org/lib/rx/meds/tachosil/) |
| EV-COR-003 | 연구분야 | 2025년 8월 영국 Taunton에 Biomedical Textiles Innovation Lab을 개소해 OEM 파트너용 흡수성·비흡수성 섬유 의료소재의 프로토타이핑·시험을 지원한다. | 주요언론 | 🟠중 | [GlobeNewswire / BioSpace 보도자료](https://www.globenewswire.com/news-release/2025/08/13/3132321/0/en/Corza-Medical-Launches-Biomedical-Textiles-Innovation-Lab-to-Accelerate-OEM-Product-Development.html) |
| EV-COR-009 | 연구분야 | Corza Medical의 사업·R&D 어디에서도 미생물 트랜스글루타미나제(mTG)나 항체-약물 접합체(ADC) 관련 기술·파이프라인·공급 활동은 확인되지 않았다. | 기타 | 🟠중 | [웹 검색(Corza + transglutaminase/ADC) 결과](https://corza.com/products/hemostasis-and-sealing/) |
| EV-COR-006 | 뉴스·동향 | 2025년 11월 Corza는 corzaeye.com을 통한 안과 고객 포털을 출시하며 디지털 고객서비스를 확장했다. | 공식홈페이지 | 🟠중 | [Corza Medical 공식 홈페이지](https://corza.com/) |
| EV-COR-008 | IP·특허 | Quill 미늘봉합사 계열과 관련된 미늘봉합(barbed suture) 특허들이 존재하나(예: US 8,100,941 등), Corza/Surgical Specialties로의 현재 양수인 귀속은 공개검색으로 명확히 확인되지 않았다. | 특허 | 🔴하 | [USPTO / Google Patents (barbed suture)](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8100941) |
| EV-COR-004 | 파트너십·M&A | Corza Medical은 2021년 1월 GTCR와 Gregory Lucier가 Surgical Specialties와 Takeda의 TachoSil 카브아웃을 합병해 설립됐다. | 주요언론 | 🟠중 | [PR Newswire / GTCR 보도자료](https://www.prnewswire.com/news-releases/gtcr-and-gregory-t-lucier-announce-merger-of-surgical-specialties-and-tachosil-to-create-corza-medical-301218913.html) |
| EV-COR-005 | 파트너십·M&A | 2024년 7월 Corza는 Takeda로부터 TachoSil 제조 운영 자체를 인수 완료했다. | 주요언론 | 🟠중 | [GlobeNewswire](https://www.globenewswire.com/news-release/2024/07/01/2906630/0/en/Corza-Medical-Completes-Acquisition-of-TachoSil-Manufacturing-Operations.html) |
| EV-COR-007 | 파트너십·M&A | Corza(및 전신)는 콜라겐 소재 기업 NeuColl 및 Surgical Specialties, BG Sulzle, CohesionTech 등을 인수해 왔다. | 기타 | 🔴하 | [ZoomInfo 기업 프로필](https://www.zoominfo.com/c/corza-medical/534404100) |

### Evonik Industries AG — Health Care

연관 판정 — **mTG**: 무관/하 · **ADC**: 공급망·파트너/하 · **Collagen**: 직접사업/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-EVO-001 | 사업분야 | Evonik Health Care는 제약·바이오파마·의료기기 고객을 위한 CDMO 사업으로, 기능성 부형제(EUDRAGIT, RESOMER), 첨단 경구·주사제 약물전달, API/HPAPI, 세포배양 원료를 공급한다. | 공식홈페이지 | 🟢상 | [Evonik 공식 홈페이지 — Health Care 사업라인](https://www.evonik.com/en/company/businesslines/hc.html) |
| EV-EVO-002 | 사업분야 | Evonik은 의료기기용 바이오소재 사업에서 RESOMER 생분해성 폴리머, VECOLLAN 재조합 콜라겐, Biocellic 바이오셀룰로오스를 조직공학·이식재·창상치유용으로 제공한다. | 공식홈페이지 | 🟢상 | [Evonik 공식 홈페이지 — Biomaterials for medical devices](https://www.evonik.com/en/markets/market_1345345.html) |
| EV-EVO-003 | 사업분야 | Evonik은 종양학 등에 쓰이는 고활성 원료의약품(HPAPI)·세포독성 API의 봉쇄형 CDMO 제조를 제공하여, ADC 페이로드 공급망의 잠재적 접점을 가진다. | 공식홈페이지 | 🟠중 | [Evonik 공식 홈페이지 — CDMO for HPAPI](https://www.evonik.com/en/applications/application_1993559.html) |
| EV-EVO-004 | 연구분야 | VECOLLAN은 동물유래 없이 발효로 생산하는 재조합 콜라겐-유사 단백질 플랫폼으로, 삼중나선 구조·인간콜라겐 유사성을 갖고 스펀지·하이드로겔·마이크로입자·섬유·메시 형태로 정형외과·미용·스포츠의학·창상치유·바이오프린팅에 응용된다. | 공식홈페이지 | 🟢상 | [Evonik 공식 홈페이지 — VECOLLAN recombinant collagen](https://healthcare.evonik.com/en/medical-devices/recombinant-collagen) |
| EV-EVO-005 | 연구분야 | Evonik의 약물전달 R&D는 지질나노입자(LNP)·mRNA/핵산전달, 고분자 마이크로/나노입자, 미셀, 이식형 서방출 제형 등 6종 이상 기술 플랫폼을 포함한다. | 공식홈페이지 | 🟢상 | [Evonik Healthcare — Drug delivery systems CDMO](https://healthcare.evonik.com/en/drugdelivery/parenteral-drug-delivery/cdmo-services/drug-delivery-systems) |
| EV-EVO-006 | 뉴스·동향 | 2025년 9월 Evonik은 재조합 콜라겐 VECOLLAN을 임상시험용 등급으로 출시했고, 2026년 파트너에게 검증된(validated) 물질을 제공할 예정이라고 발표했다. | 주요언론 | 🟠중 | [Evonik 보도자료 (2025-09)](https://www.prnewswire.com/news-releases/evonik-achieves-major-biotech-breakthrough-with-a-new-animal-free-and-fermentation-based-collagen-platform-301025007.html) |
| EV-EVO-007 | 뉴스·동향 | Evonik은 북미 서방출 주사제 CDMO에 약 3,500만 유로(별도 보도 4,100만 달러) 및 슬로바키아 바이오파마 발효 생산에 8,000만 유로를 투자하며 CDMO 역량을 확장 중이다. | 주요언론 | 🟠중 | [Fierce Pharma / European Biotechnology / Contract Pharma](https://www.fiercepharma.com/manufacturing/evonik-puts-down-41m-to-expand-north-american-cdmo-capabilities-for-injectables) |
| EV-EVO-008 | 뉴스·동향 | Evonik은 Hanau 소재 제약원료 생산자산을 위탁제조사 ProChem Group에 매각(2026-06-19 종결 예정)하고 keto acid 생산을 2025년말 중단하는 등 핵심 약물전달·정밀바이오솔루션으로 자산 재편 중이다. | 주요언론 | 🟠중 | [ChemAnalyst / AlchemPro](https://www.chemanalyst.com/NewsAndDeals/NewsDetails/evonik-sells-hanau-pharma-assets-to-prochem-to-advance-healthcare-42882) |
| EV-EVO-009 | IP·특허 | Evonik Operations GmbH의 특허 WO2024002806A1는 세포 봉입·바이오잉크·조직공학 스캐폴드용 '광가교 재조합 박테리아 콜라겐-유사 단백질(CLP)'로, 메타크릴레이트 등 광가교(효소/트랜스글루타미나제 아님) 방식을 사용한다. | 특허 | 🟢상 | [Google Patents — WO2024002806A1](https://patents.google.com/patent/WO2024002806A1/en) |
| EV-EVO-010 | 파트너십·M&A | Evonik은 미국 정부와 파트너십으로 mRNA 기반 치료제용 지질(lipid) 생산시설 구축에 약 2억 2천만 달러를 투자한다. | 공식홈페이지 | 🟢상 | [Evonik Healthcare 보도자료](https://healthcare.evonik.com/en/evonik-invests-220-million-usd-in-partnership-with-the-us-government-to-build-new-lipid-production-174199.html) |
| EV-EVO-011 | 파트너십·M&A | Evonik은 일본 제약 무역상사 Higuchi Inc.와 요코하마에 공동 실험실(joint laboratory)을 개설하는 등 지역 파트너십을 확대하고 있다. | 주요언론 | 🟠중 | [DCAT Value Chain Insights — Supplier News](https://www.dcatvci.org/top-industry-news/supplier-news-siegfried-evonik-aurobindo-more/) |

### Geistlich Pharma AG

연관 판정 — **mTG**: 인접·응용/하 · **ADC**: 무관/하 · **Collagen**: 직접사업/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-GEI-001 | 사업분야 | Geistlich은 재생치의학 분야 글로벌 시장 리더로, 소뼈 유래 골대체재 Bio-Oss와 콜라겐 차폐막 Bio-Gide가 주력 제품이며 각각 2천만/2백만 환자 이상에 사용되었다. | 공식홈페이지 | 🟢상 | [Geistlich 공식 제품 사이트](https://geistlich.us/bio-oss/) |
| EV-GEI-002 | 사업분야 | Geistlich Bio-Oss Collagen은 Bio-Oss 과립 90%와 돼지 유래 콜라겐 10%로 구성된 골재생용 복합재로, 발치 후 치조제 보존에 사용된다. | 공식홈페이지 | 🟢상 | [Geistlich 공식 홈페이지](https://www.geistlich.com/dental/bone-substitutes/bio-oss-collagen) |
| EV-GEI-003 | 사업분야 | Geistlich Mucograft와 Fibro-Gide는 구강 연조직 재생용 콜라겐 매트릭스이며, Fibro-Gide는 Type I/III 콜라겐으로 만든 부피안정형(volume-stable) 매트릭스로 결합조직 이식 대체재로 포지셔닝된다. | 공식홈페이지 | 🟢상 | [Geistlich 공식 홈페이지 (Fibro-Gide)](https://www.geistlich.com/dental/products/matrices/fibro-gide) |
| EV-GEI-004 | 사업분야 | Geistlich은 1851년 창립된 100% 가족소유 스위스 기업(Wolhusen 소재)으로, 약 500~1000명을 고용하고 15개 자회사·60개 유통사를 통해 전 세계적으로 재생 바이오소재를 공급한다. | 공식홈페이지 | 🟠중 | [Geistlich 회사 소개 / ZoomInfo](https://www.geistlich.com/about-us/geistlich-pharma/our-company) |
| EV-GEI-005 | 연구분야 | Fibro-Gide는 부피안정성을 위해 독자적 'smart-linked'(스마트 화학 가교) 방식을 적용하며, 이는 효소가 아닌 화학적 콜라겐 가교 기술이다. | 주요언론 | 🟠중 | [Dental Tribune / Geistlich](https://us.dental-tribune.com/prod/geistlich-fibro-gide/) |
| EV-GEI-012 | 연구분야 | Geistlich은 항체-약물 접합체(ADC) 파이프라인이나 mTG 기반 부위특이 접합 기술과의 접점이 확인되지 않으며, 사업·R&D는 콜라겐/골 재생 바이오소재에 한정된다. | 기타 | 🟠중 | [웹 검색(ADC/oncology 대조)](https://www.geistlich.com/about-us/geistlich-pharma/our-company) |
| EV-GEI-010 | 뉴스·동향 | FDA가 Geistlich이 Wolhusen에서 제조하는 입자형 콜라겐(particulate collagen)에 510(k) 승인을 부여했고, 미국 창상치료 파트너 StimLabs가 DermaForm 브랜드로 2026년 2분기 출시할 예정이다. | 주요언론 | 🟠중 | [StimLabs 보도자료 / Geistlich 뉴스](https://www.prnewswire.com/news-releases/stimlabs-announces-fda-510k-clearance-for-dermaform-a-collagen-scaffold-particulate-wound-care-device-302685466.html) |
| EV-GEI-011 | 뉴스·동향 | Geistlich 콜라겐 매트릭스 Mucograft가 유럽에서 피부이식(skin graft)의 대안으로 승인되는 등 콜라겐 소재의 치과 외 창상·연조직 재생 적용이 확대되고 있다. | 공식홈페이지 | 🔴하 | [Geistlich 뉴스](https://www.geistlich.com/about-us/news) |
| EV-GEI-006 | IP·특허 | Geistlich 특허 WO2017093502A1(흡수성 가교 형태안정 막)은 콜라겐 가교에 EDC/NHS 화학 가교 또는 DHT 물리 가교를 사용하며, 트랜스글루타미나제(mTG) 등 효소 가교는 기재하지 않는다. | 특허 | 🟢상 | [Google Patents WO2017093502A1](https://patents.google.com/patent/WO2017093502A1/en) |
| EV-GEI-007 | IP·특허 | Geistlich은 콜라겐 골/막 관련 다수 특허를 보유하며, 예로 US10960107B2(콜라겐 매트릭스·골대체재 과립 블렌드, 2020년 Geistlich 등록)와 Bio-Gide 관련 US5837278이 있다. | 특허 | 🟠중 | [Google Patents / Justia](https://patents.google.com/patent/US10960107B2/en) |
| EV-GEI-008 | 파트너십·M&A | Geistlich은 3D 프린팅 환자맞춤 골재생 솔루션 ReOss Ltd.에 전략적 투자를 단행하고 주력 제품 Yxoss CBR의 독점 글로벌 판매·유통권을 확보했다. | 공식홈페이지 | 🟠중 | [Geistlich 뉴스](https://www.geistlich.com/about-us/news/news-detail/geistlich-makes-strategic-investment-in-its-partner-reossr-ltd) |
| EV-GEI-009 | 파트너십·M&A | Geistlich은 브라질 재생치의학 바이오소재 기업 Bionnovation Biomedical(2024년 인수)과 이탈리아 의료기술기업 Meta Technologies S.r.l.을 인수해 신흥시장·기술 포트폴리오를 확장했다. | 공식홈페이지 | 🟠중 | [Geistlich 뉴스 / Lucerne Business](https://www.geistlich.com/about-us/news/news-detail/geistlich-acquires-bionnovation-biomedical-in-brazil) |

### Gelatex Technologies OÜ

연관 판정 — **mTG**: 인접·응용/하 · **ADC**: 무관/하 · **Collagen**: 직접사업/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-GLX-001 | 사업분야 | Gelatex는 2016년 에스토니아 탈린에서 설립된 소재 기술 스타트업으로, 독자 halospinning 기술로 배양육·조직공학·창상치료·화장품용 나노섬유 소재를 제조한다. | 주요언론 | 🟠중 | [Invest in Estonia / Gelatex 공식 홈페이지](https://investinestonia.com/cutting-edge-nanofibers-that-compete-at-scale-from-estonian-cleantech-gelatex/) |
| EV-GLX-002 | 사업분야 | 주력 제품 Gelacell™은 세포외기질(ECM)을 모사한 비직조 다공성 나노섬유 스캐폴드로, 3D 세포배양·조직공학·약물 스크리닝·독성시험용으로 판매된다. | 공식홈페이지 | 🟢상 | [Gelatex / Ilex Life Sciences 제품 페이지](https://ilexlife.com/pages/gelacell-3d-nanofibrous-scaffolds) |
| EV-GLX-003 | 사업분야 | Gelatex는 식품등급 100% 동물유래-무함유 나노섬유 스캐폴드·마이크로캐리어를 배양육 대량생산용으로 공급하며, 스캐폴드 단가를 kg당 1,000유로 미만으로 낮췄다. | 공식홈페이지 | 🟢상 | [Gelatex 공식 홈페이지(cultured meat) / FoodNavigator](https://www.gelatex.com/cultured-meat) |
| EV-GLX-004 | 연구분야 | 핵심 기술 플랫폼은 HaloSpin™(halospinning)으로, 비정전기장 노즐 기반 용액방사 방식이며 전기방사 대비 14배 이상 빠른 나노섬유 대량생산이 가능하다. | 공식홈페이지 | 🟢상 | [Gelatex 공식 홈페이지(technology)](https://www.gelatex.com/technology) |
| EV-GLX-005 | 연구분야 | Gelacell 스캐폴드 소재군에는 젤라틴(gelatin)과 키토산 등 천연고분자 및 PLLA·PLGA·PCL 합성고분자가 포함되며, 젤라틴 스캐폴드가 별도 제품 라인으로 판매된다. | 주요언론 | 🟠중 | [Ilex Life Sciences 제품군](https://ilexlife.com/products/gelacell-gelatin-scaffold-inserts-for-24-well-plate-3d-cell-culture) |
| EV-GLX-006 | 연구분야 | Gelatex는 에스토니아 EAS로부터 76만유로 지원의 '배양육용 나노섬유 마이크로캐리어'(2022.07~2024.12) 및 Eurostars-2 지원 '실험실 배양 가죽 SMART'(2025~2027) R&D 과제를 수행한다. | 업계리포트 | 🟠중 | [Tracxn / Invest in Estonia (과제 정보)](https://tracxn.com/d/companies/gelatex-technologies/__2XddhFE0FpyTfFcFdw23AJt2P44kCcXGslJV3DW8rUE) |
| EV-GLX-011 | 연구분야 | 미생물 트랜스글루타미나제(mTG)는 젤라틴 스캐폴드를 수불용성·열안정성으로 만드는 대표적 식품안전 효소 가교제로, Gelatex의 식용 젤라틴 배양육 스캐폴드에 응용 가능한 접점이 존재한다. | 논문 | 🟠중 | [Yung et al. J Biomed Mater Res A (mTG-gelatin scaffold) 등 문헌](https://pubmed.ncbi.nlm.nih.gov/17584898/) |
| EV-GLX-012 | 연구분야 | Gelatex 및 관련 배양육 스캐폴드 분야에서 효소 가교(트랜스글루타미나제 포함)가 식용 스캐폴드의 기계적 안정성 향상을 위해 탐색되고 있다. | 논문 | 🟠중 | [Gels/MDPI 하이브리드 젤 스캐폴드 리뷰](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12385360/) |
| EV-GLX-013 | 연구분야 | Gelatex와 항체-약물 접합체(ADC)·바이오컨쥬게이션·종양학 모달리티 사이의 사업·연구·공급 연결은 확인되지 않았다(honest_gap). | 기타 | 🟠중 | [웹 검색(복수 검색어) 결과 종합](https://www.gelatex.com/) |
| EV-GLX-009 | 뉴스·동향 | Gelatex는 2021년 Change Ventures·Crosslight 주도 120만유로 시드를 유치했고, 2022년 배양육 사업 확장을 위해 1,500만유로 규모 Series A 라운드를 개시했다. | 주요언론 | 🟠중 | [EU-Startups / AIN.Capital](https://en.ain.ua/2022/09/28/gelatex-opens-15m-series-a/) |
| EV-GLX-007 | IP·특허 | 등록특허 US 11,697,892 B2 '고분자 섬유 제조 장치·방법'은 Gelatex Technologies OÜ 소유이며, 젤라틴(gelatin)과 콜라겐(collagen)을 용액방사 가능한 바이오기반 고분자로 명시한다. | 특허 | 🟢상 | [Google Patents US11697892B2](https://patents.google.com/patent/US11697892B2/en) |
| EV-GLX-008 | 파트너십·M&A | 2023년 10월 Gelatex는 Ilex Life Sciences를 Gelacell™ 3D 나노섬유 스캐폴드의 미국·캐나다 독점 유통사로 지정했다. | 주요언론 | 🟠중 | [Ilex Life Sciences 뉴스](https://ilexlife.com/blogs/news/gelatex-technologies-gelacell-scaffolds-distributor) |
| EV-GLX-010 | 파트너십·M&A | Gelatex는 세계 10대 배양육 생산기업 중 8곳과 파일럿 프로젝트를 진행했으며, Techstars 액셀러레이터의 지원을 받았다. | 주요언론 | 🟠중 | [FoodNavigator / vegconomist](https://www.foodnavigator.com/Article/2021/12/01/Gelatex-Cost-efficient-scaffolding-tech-developed-for-cultivated-meat-at-scale/) |

### GELITA AG

연관 판정 — **mTG**: 인접·응용/중 · **ADC**: 무관/하 · **Collagen**: 직접사업/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-GEL-001 | 사업분야 | GELITA는 식품·헬스&뉴트리션·제약·기술응용용 젤라틴과 콜라겐 펩타이드를 제조하는 글로벌 기업(1875년 설립, 독일 Eberbach 본사, 20개 이상 생산거점)이다. | 공식홈페이지 | 🟢상 | [GELITA 공식 홈페이지 (About)](https://www.gelita.com/en/about-gelita) |
| EV-GEL-002 | 사업분야 | 제약·의료용 젤라틴 브랜드 MEDELLAPRO는 지혈제, 창상치료, 혈장증량제, 색전술, 약물전달, 조직공학(3D 바이오프린팅) 등 바이오메디컬 용도로 공급된다. | 공식홈페이지 | 🟢상 | [GELITA MEDELLAPRO 제품 페이지](https://www.gelita.com/en/products-brands/gelatin/medellapro) |
| EV-GEL-003 | 사업분야 | 바이오액티브 콜라겐 펩타이드(VERISOL 등)를 피부·관절·뼈 건강 및 스포츠 뉴트리션용으로 공급하는 것이 헬스&뉴트리션 핵심 사업이다. | 공식홈페이지 | 🟢상 | [GELITA Collagen Peptides 페이지](https://www.gelita.com/en/products-brands/collagen-peptides) |
| EV-GEL-004 | 연구분야 | Bioscience 부문에서 백신 안정화(VACCIPRO), 3D 프린팅, 의료기기, 배양육(artificial meat) 스캐폴드 등 젤라틴·콜라겐 기반 R&D를 추진한다. | 공식홈페이지 | 🟢상 | [GELITA 공식 홈페이지 (Bioscience/Medical Devices)](https://www.gelita.com/en/markets-we-serve/bioscience/medical-devices) |
| EV-GEL-005 | 연구분야 | 차세대 바이오프린팅·주사제용으로 내독소 10 EU/g 미만의 MEDELLAPRO Ultra Low Endotoxin 젤라틴 그레이드를 개발했다. | 공식홈페이지 | 🟢상 | [GELITA 기술 블로그 (Ultra Low Endotoxin Bioprinting)](https://www.gelita.com/en/knowledge/blog/medellapror-ultra-low-endotoxin-gelatin-engineered-next-generation-bioprinting) |
| EV-GEL-006 | 뉴스·동향 | 2025~2026년 관절·뼈·대사 지원 바이오액티브 콜라겐 펩타이드로 파이프라인을 확장하고, EASYSEAL(제약 젤라틴)·PeptENDURE(콜라겐 펩타이드) 신제품을 출시한다. | 주요언론 | 🟠중 | [Nutraceutical Business Review](https://nutraceuticalbusinessreview.com/gelita-to-launch-two-innovative-ingredient-solutions-at) |
| EV-GEL-007 | 뉴스·동향 | COMPAMED 2025에서 MEDELLAPRO(제약 젤라틴)와 VACCIPRO를 수술용 실란트·지혈제·스캐폴드·약물전달용 부형제로 선보였다. | 주요언론 | 🟠중 | [Manufacturing Chemist](https://manufacturingchemist.com/gelita-showcase-next-gen-collagen-excipients-compamed) |
| EV-GEL-008 | 뉴스·동향 | BIO International 2026(샌디에이고)에서 MEDELLAPRO Ultra Low Endotoxin 젤라틴 그레이드를 내독소 통제 부형제 포트폴리오와 함께 발표했다. | 주요언론 | 🟠중 | [Pharma Excipients](https://www.pharmaexcipients.com/news/low-endotoxin-gelatin/) |
| EV-GEL-009 | IP·특허 | GELITA AG는 TETEC와 공동으로 젤라틴을 트랜스글루타미나제로 가교해 지혈·창상·조직고정용 의료접착제를 만드는 특허(US9295751B2, 우선일 2006-07-10)를 보유한다. | 특허 | 🟢상 | [Google Patents US9295751B2](https://patents.google.com/patent/US9295751B2/en) |
| EV-GEL-010 | IP·특허 | 젤라틴-트랜스글루타미나제 지혈 드레싱/실란트 및 가교 의료접착제 관련 특허 패밀리(WO2008076407, EP2037972B1, JP5581056B2)가 존재한다. | 특허 | 🟢상 | [Google Patents (WO2008076407 / EP2037972B1)](https://patents.google.com/patent/EP2037972B1/en) |
| EV-GEL-011 | 파트너십·M&A | GELITA AG는 조직공학 기업 TETEC Tissue Engineering Technologies AG와 젤라틴-트랜스글루타미나제 의료접착제 특허를 공동 출원·공동보유하며 협업했다. | 특허 | 🟠중 | [Google Patents US9295751B2 (co-assignee)](https://patents.google.com/patent/US9295751B2/en) |
| EV-GEL-012 | 파트너십·M&A | 2025년 12월 경쟁사 Darling Ingredients와 Tessenderlo가 젤라틴·콜라겐 사업 통합을 합의했으나, GELITA는 이 거래의 직접 당사자가 아니다. | 업계리포트 | 🟠중 | [MarketsandMarkets / 업계 뉴스](https://www.marketsandmarkets.com/ResearchInsight/gelatin-market.asp) |

### Integra LifeSciences Holdings Corporation

연관 판정 — **mTG**: 무관/하 · **ADC**: 무관/하 · **Collagen**: 직접사업/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-INT-001 | 사업분야 | Integra의 창업 기반 제품군은 콜라겐 기반 매트릭스로, 피부재생(Integra Dermal Regeneration Template), 경막(DuraGen), 말초신경(NeuraGen), 치주(BioMend) 등 조직재생 의료기기를 포함한다. | IR·공시 | 🟢상 | [Integra LifeSciences 10-K (SEC EDGAR)](https://www.sec.gov/Archives/edgar/data/0000917520/000091752003000005/form10k032003.txt) |
| EV-INT-002 | 사업분야 | Integra는 2025년 매출 약 16.4억 달러이며, Codman Specialty Surgical(신경외과·ENT, 약 70%)과 Tissue Technologies(조직재생·재건, 약 30%) 두 사업부로 구성된다. | 주요언론 | 🟠중 | [StockTitan (Integra 2025 10-K 요약)](https://www.stocktitan.net/sec-filings/IART/10-k-integra-lifesciences-holdings-corp-files-annual-report-0596929e7873.html) |
| EV-INT-003 | 연구분야 | Type I(1형) 콜라겐이 DuraGen, NeuraGen, Integra Dermal Regeneration Template 등 Integra 재생 기술의 핵심 원료이며, 누적 1,200만 명 이상 환자에게 이식되었다. | 공식홈페이지 | 🟢상 | [Integra LifeSciences EMEA 공식 홈페이지](https://integralife.eu/products/neuro/duraplasty/suturable-duragen-4/) |
| EV-INT-004 | 연구분야 | Integra Dermal Regeneration Template의 진피 대체층은 가교된 소(bovine) 힘줄 콜라겐과 글리코사미노글리칸(chondroitin-6-sulfate) 다공성 매트릭스로 구성된다. | 특허 | 🟢상 | [Google Patents (Integra 특허 US6969523B1 발췌 기반)](https://patents.google.com/patent/US6969523B1/en) |
| EV-INT-012 | 연구분야 | 학술 문헌상 미생물 트랜스글루타미나제(mTG)는 1형 콜라겐 가교와 ADC 부위특이적 접합 모두에 쓰이나, Integra의 콜라겐 제품은 mTG가 아닌 글루타르알데히드 화학 가교를 사용하며 Integra와 mTG/ADC를 직접 연결하는 근거는 발견되지 않았다. | 논문 | 🟢상 | [ScienceDirect / ACS Bioconjugate Chem (mTG 문헌) + Integra 특허 대조](https://www.sciencedirect.com/science/article/abs/pii/S0022354923003258) |
| EV-INT-007 | 뉴스·동향 | Integra는 태아 소진피 콜라겐 소재 SurgiMend와 흡수성 모노필라멘트 메시 DuraSorb에 대해 유방재건 적응증 PMA 승인을 2026년 목표로 추진 중이며, DuraSorb IDE 임상 등록을 완료했다. | IR·공시 | 🟠중 | [Integra LifeSciences 투자자 보도자료 (Nasdaq 게재)](https://www.nasdaq.com/press-release/integra-lifesciences-announces-complete-enrollment-in-durasorbr-monofilament-mesh-u.s) |
| EV-INT-008 | 뉴스·동향 | Integra는 2024~2025년 품질시스템 문제로 FDA 경고서한(2024-12) 및 다수 리콜(MediHoney 창상·화상 제품, Duraform 등 콜라겐 기반 제품 포함)을 겪었다. | 규제기관 | 🟢상 | [FDA / MedTech Dive](https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/warning-letters/integra-lifesciences-corporation-698850-12192024) |
| EV-INT-009 | 뉴스·동향 | Integra는 소 1형 콜라겐과 Dermal Regeneration Template를 결합한 NeuraGen 3D Nerve Guide Matrix를 출시하며 말초신경 재생 콜라겐 솔루션을 확장했다. | IR·공시 | 🟠중 | [Integra LifeSciences 투자자 보도자료](https://investor.integralife.com/news-releases/news-release-details/integra-lifesciences-launches-neuragenr-3d-nerve-guide-matrix) |
| EV-INT-005 | IP·특허 | Integra LifeSciences Corp가 소유한 특허 US6969523B1은 전자빔 멸균에 안정한 가교 콜라겐/글리코사미노글리칸 매트릭스를 다루며, 가교 방식으로 글루타르알데히드 등 화학적 가교를 사용한다. | 특허 | 🟢상 | [Google Patents US6969523B1](https://patents.google.com/patent/US6969523B1/en) |
| EV-INT-006 | IP·특허 | Integra의 콜라겐 매트릭스 제조 공정은 0.05M 아세트산 중 약 0.5% 글루타르알데히드 용액에서의 화학적 가교 및 잔류 글루타르알데히드 제거 세척 단계를 포함한다. | 특허 | 🟢상 | [Google Patents (Integra 콜라겐 매트릭스 특허군)](https://patents.google.com/patent/US6969523B1/en) |
| EV-INT-010 | 파트너십·M&A | Integra는 2024년 4월 J&J MedTech(Ethicon)로부터 ENT 기업 Acclarent를 약 2.75억 달러(+마일스톤 500만 달러)에 인수해 Codman Specialty Surgical 사업부에 편입했다. | IR·공시 | 🟢상 | [Integra LifeSciences 보도자료 (GlobeNewswire)](https://www.globenewswire.com/news-release/2024/04/01/2855464/1063/en/Integra-LifeSciences-Completes-the-Acquisition-of-Acclarent-Inc.html) |
| EV-INT-011 | 파트너십·M&A | Integra는 흡수성 모노필라멘트 메시 DuraSorb를 보유한 Surgical Innovation Associates(SIA)를 인수해 유방재건·연조직 보강 콜라겐/합성 매트릭스 포트폴리오를 강화했다. | IR·공시 | 🟢상 | [Integra LifeSciences 보도자료 (SEC EDGAR)](https://www.sec.gov/Archives/edgar/data/917520/000091752022000058/siapressreleasefinal.htm) |

### Johnson & Johnson MedTech (Ethicon)

연관 판정 — **mTG**: 무관/하 · **ADC**: 직접연구/상 · **Collagen**: 직접사업/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-JNJ-001 | 사업분야 | J&J MedTech은 2025년 약 337.9억 달러 매출로 Surgery(외과)·Orthopaedics·Cardiovascular·Vision 4개 프랜차이즈를 운영하며, Ethicon은 Surgery 부문의 외과 브랜드이다. | IR·공시 | 🟢상 | [Statista / J&J 10-K (StockTitan 요약)](https://www.stocktitan.net/sec-filings/JNJ/10-k-johnson-johnson-files-annual-report-20fbdd90419d.html) |
| EV-JNJ-002 | 사업분야 | Ethicon의 대표 지혈제 SURGICEL은 산화재생셀룰로스(ORC) 기반 흡수성 지혈제로 식물 유래이며 콜라겐/젤라틴이 아니다. | 공식홈페이지 | 🟢상 | [J&J MedTech 공식 제품 페이지](https://www.jnjmedtech.com/en-US/products/surgery/biosurgery/surgicel-original-absorbable-hemostat/) |
| EV-JNJ-003 | 사업분야 | Ethicon SURGIFOAM은 가교(cross-linked) 돼지 유래 흡수성 젤라틴 스펀지로, 젤라틴(콜라겐 유도체) 기반 지혈제이다. | 공식홈페이지 | 🟢상 | [J&J MedTech Biosurgery 포트폴리오 자료 (검색 요약)](https://www.jnjmedtech.com/system/files/pdf/Ethicon-Biosurgery-Comprehensive-Portfolio-Brochure-150460-200819.pdf) |
| EV-JNJ-004 | 사업분야 | Ethicon SURGIFLO는 돼지 유래 흡수성 젤라틴에 트롬빈을 혼합해 사용하는 유동형 지혈 매트릭스이다. | 공식홈페이지 | 🟢상 | [J&J MedTech 공식 제품 페이지](https://www.jnjmedtech.com/en-US/products/surgery/biosurgery/surgiflo-hemostatic-matrix-kit/) |
| EV-JNJ-005 | 사업분야 | Ethicon INSTAT MCH는 미세섬유상 콜라겐 지혈제(microfibrillar collagen hemostat)로, 콜라겐 소재 의료기기이다. | 주요언론 | 🟠중 | [Medline 제품 카탈로그 (Ethicon INSTAT MCH)](https://www.medline.com/product/INSTAT-MCH-Microfibrillar-Collagen-Hemostat-by-Ethicon/Z05-PF42184) |
| EV-JNJ-006 | 사업분야 | Ethicon EVARREST는 산화재생셀룰로스 패치에 인간 피브리노겐·트롬빈을 코팅한 피브린 실런트 패치이다. | 공식홈페이지 | 🟢상 | [J&J MedTech 공식 제품 페이지](https://www.jnjmedtech.com/en-US/products/surgery/biosurgery/evarrest-fibrin-sealant-patch/) |
| EV-JNJ-009 | 연구분야 | J&J의 ADC 후보 ARX517(JNJ-95298177, PSMA 표적 전립선암)은 비천연 아미노산 기반 옥심(oxime) 부위특이 접합을 사용하며 2025년 mCRPC 초기 임상에서 유효성을 보였다. | 주요언론 | 🟠중 | [OncLive (APEX-01 임상 보도)](https://www.onclive.com/view/arx517-demonstrates-early-efficacy-with-favorable-safety-in-heavily-pretreated-mcrpc) |
| EV-JNJ-012 | 연구분야 | J&J MedTech/Ethicon이 자사 제품·연구에서 미생물 트랜스글루타미나제(mTG)를 가교제 또는 ADC 접합에 사용한다는 증거는 확인되지 않았다. | 기타 | 🟠중 | [복수 검색(Google Patents, J&J MedTech, 언론)](https://patents.google.com/patent/WO2008076407A2/en) |
| EV-JNJ-007 | 뉴스·동향 | Ethicon은 2023년 11월 합성 폴리머 기반 신규 지혈 패치 ETHIZIA를 출시 발표했으며, 콜라겐/피브린이 아닌 합성 소재이다. | 주요언론 | 🟠중 | [PR Newswire / J&J 보도자료](https://www.prnewswire.com/news-releases/ethicon-introduces-ethizia-hemostatic-sealing-patch-clinically-proven-to-stop-disruptive-bleeding-301989164.html) |
| EV-JNJ-011 | 뉴스·동향 | J&J는 2025년 10월 Orthopaedics 사업 분사 계획을 발표했고, 분사 후 MedTech은 Surgery와 Vision을 핵심 성장영역으로 유지한다. | IR·공시 | 🟠중 | [J&J 10-K (StockTitan 요약)](https://www.stocktitan.net/sec-filings/JNJ/10-k-johnson-johnson-files-annual-report-20fbdd90419d.html) |
| EV-JNJ-010 | IP·특허 | 젤라틴-트랜스글루타미나제(mTG) 지혈 드레싱·실런트 특허군(US8722039, US9655988, WO2008076407)은 J&J가 아니라 경쟁사 Lifebond Ltd(현 Bard Shannon/BD)에 귀속된다. | 특허 | 🟢상 | [Google Patents (US8722039B2, US9655988B2)](https://patents.google.com/patent/US9655988B2/en) |
| EV-JNJ-008 | 파트너십·M&A | J&J는 2024년 3월 임상단계 ADC 기업 Ambrx를 약 20억 달러 전액현금으로 인수 완료해 차세대 ADC 파이프라인을 확보했다. | 주요언론 | 🟠중 | [J&J 공식 보도자료 / Pharmaceutical Technology](https://www.pharmaceutical-technology.com/news/johnson-johnson-ambrx/) |

### Keenova Therapeutics plc (구 Mallinckrodt)

연관 판정 — **mTG**: 무관/하 · **ADC**: 무관/하 · **Collagen**: 직접사업/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-KEE-001 | 사업분야 | Keenova Therapeutics는 Mallinckrodt가 Par Health(제네릭·주사제) 사업을 2025-11-10 분사한 뒤 리브랜드한 회사로, 희귀·미충족 질환용 브랜드 치료제 개발·제조·상업화에 집중한다(2024 프로포마 매출 약 17억 달러, 임직원 1,600명 이상, CEO Siggi Olafsson). | 주요언론 | 🟠중 | [Pharma Manufacturing / PRNewswire (Keenova 출범 보도)](https://www.pharmamanufacturing.com/industry-news/news/55329356/mallinckrodt-completes-spinoff-rebrands-as-keenova-therapeutics) |
| EV-KEE-002 | 사업분야 | Keenova의 제품 포트폴리오는 Acthar Gel(코르티코트로핀), XIAFLEX(콜라게나제 주사제), INOmax, StrataGraft, Terlivaz, Amitiza 등으로 구성되며 2026년 순매출 가이던스는 19.4억~20.0억 달러다. | 주요언론 | 🟠중 | [MarketScreener (Keenova 2026 실적 가이던스)](https://www.marketscreener.com/news/keenova-therapeutics-plc-provides-earnings-guidance-for-the-year-2026-ce7e51ded189f324) |
| EV-KEE-003 | 사업분야 | StrataGraft은 성인 심재성 2도 화상(온열화상) 치료용으로 2021-06-15 FDA 승인된 생체공학 동종 세포화 스캐폴드로, 뮤린(비소 유래) 제I형 콜라겐 진피 매트릭스에 배양 각질세포·진피섬유아세포를 결합한 이중층 인공피부다. | 규제기관 | 🟢상 | [Mallinckrodt/Keenova 공식 보도자료 (StrataGraft FDA 승인)](https://mallinckrodt.gcs-web.com/news-releases/news-release-details/mallinckrodt-announces-us-fda-approval-stratagraftr-allogeneic) |
| EV-KEE-004 | 연구분야 | StrataGraft 제조는 NIKS 인간 각질세포와 정상 인간 진피섬유아세포(NHDF)를 정제된 제I형 콜라겐과 결합해 세포화 진피 등가물(DE)을 만든 뒤 각질세포를 상층에 배양하는 3단계 조직배양 공정으로, 콜라겐 하이드로겔 매트릭스가 핵심 소재다. | 논문 | 🟢상 | [ScienceDirect (Burns 저널, StrataGraft ECM 논문)](https://www.sciencedirect.com/science/article/pii/S0305417923001171) |
| EV-KEE-005 | 연구분야 | 포트폴리오 제품 XIAFLEX(collagenase clostridium histolyticum)는 Clostridium histolyticum 발효로 정제한 두 콜라게나제(AUX-I, AUX-II)로 제I·III형 콜라겐을 분해해 뒤퓌트랑 구축·페이로니병을 치료하는 콜라겐 표적 생물의약품이다. | 규제기관 | 🟢상 | [XIAFLEX HCP 기전 페이지 / Wikipedia](https://peyronies-disease.xiaflex.com/hcp/xiaflex/mechanism-of-action/) |
| EV-KEE-006 | 연구분야 | StrataGraft은 21st Century Cures Act 하 초기 RMAT(재생의료 첨단치료) 지정 및 희귀의약품 지정을 받았고, 개발사 Stratatech는 BARDA로부터 약 8,600만 달러를 지원받아 개발했다. | 규제기관 | 🟠중 | [NIH SEED (Stratatech 스토리) / Keenova IR](https://seed.nih.gov/portfolio/stories/Stratatech) |
| EV-KEE-012 | 연구분야 | Keenova/Stratatech가 mTG(미생물 트랜스글루타미나제)를 콜라겐 가교나 ADC 접합에 사용하거나, 자체 항체-약물 접합체(ADC) 오ncology 파이프라인을 보유한다는 근거는 확인되지 않았다. | 기타 | 🟠중 | [honest_gap (복수 검색)](https://www.marketscreener.com/quote/stock/KEENOVA-THERAPEUTICS-PLC-152503479/) |
| EV-KEE-007 | 뉴스·동향 | 2025-11-10 Mallinckrodt는 Par Health 분사를 완료하고 Keenova Therapeutics로 출범했으며, 내년(2026) 뉴욕증권거래소 상장을 목표로 한다. | 주요언론 | 🟠중 | [pharmaphorum (Keenova 리브랜드 보도)](https://pharmaphorum.com/news/irelands-mallinckrodt-closes-spinout-rebrands-keenova) |
| EV-KEE-008 | 뉴스·동향 | FDA는 StrataGraft에 대해 이종이식(xenotransplantation) 관련 요건을 완화하는 라벨 업데이트를 승인해, 환자의 조직·세포 기증 제한을 해제했다. | 규제기관 | 🟠중 | [Dermatology Times / Keenova IR](https://ir.mallinckrodt.com/news-releases/news-release-details/mallinckrodt-receives-us-food-and-drug-administration-label) |
| EV-KEE-009 | 뉴스·동향 | Keenova는 류마티스·안과·신장·호흡기·신경·비뇨기·정형외과 등 치료영역에서 파이프라인 확장과 다각화된 브랜드 포트폴리오 성장을 전략 방향으로 제시했다. | IR·공시 | 🟢상 | [Keenova/Mallinckrodt IR 보도자료](https://ir.mallinckrodt.com/news-releases/news-release-details/mallinckrodt-completes-spin-par-health-introduces-keenova) |
| EV-KEE-010 | IP·특허 | Stratatech 계열 특허는 콜라겐 기반 오가노타입 인공피부 등가물의 냉장보관·동결보존에 관한 것으로, US 10,743,533(2020-08-18 등록), US 10,091,983, US 11,297,829, AU2019232795B2 등이 확인된다. | 특허 | 🟠중 | [Justia Patents / Google Patents](https://patents.justia.com/patent/10743533) |
| EV-KEE-011 | 파트너십·M&A | Keenova는 Mallinckrodt와 Endo, Inc.의 2025년 7월 합병으로 결합된 브랜드 사업으로 형성됐으며, 이후 Par Health 제네릭 사업을 분사(2025-11)해 완성됐다. | 주요언론 | 🟠중 | [FiercePharma (Mallinckrodt-Endo 합병/리브랜드)](https://www.fiercepharma.com/pharma/merger-books-mallinckrodt-and-endo-rebrand-keenova-spin-generics-business-par-health) |

### Medtronic plc

연관 판정 — **mTG**: 무관/하 · **ADC**: 무관/하 · **Collagen**: 인접·응용/중

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-MDT-001 | 사업분야 | Medtronic의 Medical Surgical 포트폴리오는 Surgical & Endoscopy 부문과 Acute Care & Monitoring 부문으로 구성되며 FY2025 매출은 약 84억 달러다. | IR·공시 | 🟠중 | [market.us / Medtronic FY2025 실적 (PR Newswire)](https://www.prnewswire.com/news-releases/medtronic-reports-third-quarter-fiscal-2025-financial-results-302378617.html) |
| EV-MDT-002 | 사업분야 | Medtronic의 주력 지혈 패치 Veriset은 산화셀룰로오스(ORC) + 트리라이신 + 반응성 PEG의 합성 소재로, 인체·동물 유래 성분을 포함하지 않는다. | 공식홈페이지 | 🟢상 | [Medtronic (South Africa/UK) 공식 제품 페이지](https://www.medtronic.com/covidien/en-za/products/hemostasis/veriset-hemostatic-patch.html) |
| EV-MDT-004 | 사업분야 | Medtronic은 척추/정형 사업의 INFUSE Bone Graft에서 흡수성 콜라겐 스펀지(ACS)를 rhBMP-2 담체(스캐폴드)로 사용하는 콜라겐 함유 의료기기를 시판한다. | 공식홈페이지 | 🟢상 | [Medtronic 공식 INFUSE 제품 페이지 / PMC 리뷰](https://global.medtronic.com/xg-en/healthcare-professionals/products/spinal-orthopaedic/bone-grafting/infuse-bone-graft.html) |
| EV-MDT-003 | 연구분야 | Medtronic 지혈/실런트 포트폴리오(Veriset, DuraSeal, TissuePatch)는 모두 합성 화학(PEG 하이드로겔·산화셀룰로오스·합성 폴리머 필름) 기반이며 콜라겐·젤라틴·효소 가교를 쓰지 않는다. | 논문 | 🟢상 | [tandfonline 임상리뷰 / Medtronic 제품 자료](https://www.tandfonline.com/doi/full/10.1080/17434440.2018.1464909) |
| EV-MDT-009 | 연구분야 | Medtronic은 의료기기 기업으로 항체-약물 접합체(ADC)나 종양학 치료제 파이프라인, mTG 기반 부위특이적 접합 사업을 보유하지 않는다. | 기타 | 🟠중 | [웹 검색 종합 (ADC 파이프라인 리뷰 대조)](https://link.springer.com/article/10.1186/s13045-025-01704-3) |
| EV-MDT-010 | 연구분야 | 젤라틴-mTG 지혈 실런트는 학계/BD·Lifebond가 주도하는 영역이며, Medtronic 제품은 오히려 비동물·비효소 합성 접근을 표방해 mTG 기술과 접점이 없다. | 논문 | 🟠중 | [PubMed (gelatin-mTG hemostat 논문) / Medtronic 제품 자료](https://pubmed.ncbi.nlm.nih.gov/28321657/) |
| EV-MDT-007 | 뉴스·동향 | Medtronic은 FY2026(2025.4월 종료 회계연도) 실적에서 10년 만의 최고 연간 매출 성장을 기록했고, 성장 동력으로 심혈관과 Surgical 사업을 지목했다. | 주요언론 | 🟠중 | [Medtronic 보도자료 (PR Newswire) / MedTech Intelligence](https://www.prnewswire.com/news-releases/medtronic-reports-fourth-quarter-and-full-year-fiscal-2026-results-delivers-highest-annual-revenue-growth-in-10-years-302789415.html) |
| EV-MDT-005 | IP·특허 | Medtronic 계열의 지혈 관련 특허는 산화셀룰로오스 용액 등 합성 소재 기반(US 11,872,244; US 10,413,566)으로, 콜라겐·젤라틴·트랜스글루타미나제 소재가 아니다. | 특허 | 🟠중 | [USPTO / Google Patents](https://patents.google.com/patent/US11872244) |
| EV-MDT-006 | IP·특허 | 젤라틴-트랜스글루타미나제(mTG) 지혈 드레싱/실런트 특허 패밀리(US 8,722,039; 9,017,664; 9,636,433; 9,655,988)의 소유자는 Lifebond Ltd / Bard Shannon Ltd(BD)이며 Medtronic이 아니다. | 특허 | 🟢상 | [Google Patents (US8722039B2)](https://patents.google.com/patent/US8722039B2/en) |
| EV-MDT-008 | 파트너십·M&A | 2025~2026년 지혈/바이오서저리 M&A는 경쟁사 중심(Merit Medical의 Biolife 인수, Baxter의 상온 Hemopatch 출시)이며 Medtronic의 콜라겐·mTG 관련 인수는 확인되지 않았다. | 업계리포트 | 🟠중 | [Mordor Intelligence / datahorizzon 시장리포트](https://www.mordorintelligence.com/industry-reports/hemostasis-and-tissue-sealing-agents-market) |

### MiMedx Group, Inc.

연관 판정 — **mTG**: 무관/하 · **ADC**: 무관/하 · **Collagen**: 직접사업/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-MMX-001 | 사업분야 | MiMedx는 인간 태반·양막(placental/amniotic) 유래 조직 동종이식(allograft)을 개발·판매하는 재생의학 기업으로, EpiFix·AmnioFix(dHACM), AmnioFill·CollaFix(Placental Collagen family), EpiCord/AmnioCord(제대), OrthoFlo(양수) 등의 제품군을 보유한다. | 업계리포트 | 🟠중 | [MarketsandMarkets / MiMedx 공식 자료 인용](https://www.marketsandmarkets.com/ResearchInsight/amniotic-products-market.asp) |
| EV-MMX-002 | 사업분야 | MiMedx는 사업을 Wound(창상)와 Surgical(수술) 두 부문으로 운영하며, 2025년 연매출 사상 최대 4억1,900만 달러(전년 3억4,900만 달러 대비 +20%)를 기록했다. | IR·공시 | 🟢상 | [MiMedx SEC Form 8-K (Q4/FY2025 실적) / StockTitan](https://www.sec.gov/Archives/edgar/data/0001376339/000137633926000012/mdxg-q42025pressreleasev.htm) |
| EV-MMX-003 | 사업분야 | MiMedx는 독자 PURION 공정으로 태반조직을 무균 처리(aseptic processing)와 최종 멸균(terminal sterilization)하여 allograft를 제조하며, 누적 180만 개 이상의 태반조직 기반 이식재를 공급했다. | 업계리포트 | 🟠중 | [MarketsandMarkets / MiMedx 공식 자료 인용](https://www.marketsandmarkets.com/ResearchInsight/amniotic-products-market.asp) |
| EV-MMX-004 | 연구분야 | MiMedx의 CollaFix 플랫폼은 정제된 가용성 콜라겐(purified soluble collagen)을 습식방사(wet spinning)해 사람 머리카락 굵기의 서브밀리미터 콜라겐 섬유를 만들고 이를 가교(crosslink)해 인간 힘줄에 필적하는 강도·강성을 갖는 생체모방 근골격 수복재를 만든다. | 주요언론 | 🟠중 | [PR Newswire (MiMedx CollaFix publication 발표)](https://www.prnewswire.com/news-releases/mimedx-announces-publication-on-collafix-the-companys-next-technology-platform-to-be-commercialized-300082891.html) |
| EV-MMX-005 | 연구분야 | MiMedx의 dHACM(탈수 인간 양막/융모막) allograft는 콜라겐 I·III·IV·V·VI형과 히알루론산·프로테오글리칸·피브로넥틴·라미닌 등으로 구성된 콜라겐 풍부 세포외기질(ECM)이며, 226종 이상의 성장인자·생리활성 단백질을 함유한다. | 논문 | 🟢상 | [Identification of ECM Components in Micronized dHACM (PMC5286550) / MiMedx](https://pmc.ncbi.nlm.nih.gov/articles/PMC5286550/) |
| EV-MMX-007 | 연구분야 | CollaFix 콜라겐 섬유의 가교에는 미생물 트랜스글루타미나제(mTG)가 아니라 천연 폴리페놀 가교제 NDGA(nordihydroguaiaretic acid)가 사용된다. | 논문 | 🟢상 | [AIMS Bioengineering (NDGA crosslinked collagen fiber) / CollaFix 기술 설명](http://www.aimspress.com/article/10.3934/bioeng.2017.2.300) |
| EV-MMX-012 | 연구분야 | MiMedx는 종양학 항체-약물 접합체(ADC) 파이프라인, 링커·페이로드 접합 기술, 또는 ADC용 mTG 효소 공급 사업이 전혀 확인되지 않는 태반조직 재생의학 전문기업이다. | 기타 | 🔴하 | [웹검색 종합(honest_gap)](https://www.mimedx.com/) |
| EV-MMX-009 | 뉴스·동향 | MiMedx는 2026년 상반기 신제품을 연이어 출시했다: CHORIOFIX(2026-03-23, 최두꺼운 동결건조 융모막 allograft), AMNIOFIX Thyroid Shields(갑상선 수술용 dHACM), G4Derm Plus(2026-05-08, 자기조립 펩타이드 기반 무세포 유동성 ECM, 510(k) 승인). | 주요언론 | 🟠중 | [MiMedx 보도자료 / StockTitan·GlobeNewswire 종합](https://www.stocktitan.net/news/MDXG/) |
| EV-MMX-010 | 뉴스·동향 | 2026년 신규 메디케어 상환규정이 Wound(창상/skin substitute) 부문을 강타해 Q1 2026 매출이 5,900만 달러로 전년 동기 8,800만 달러 대비 33% 감소(창상 -60%)했고, MiMedx는 2026년 연매출 가이던스를 당초 3.4~3.6억에서 2.6~2.9억 달러로 하향했다. | IR·공시 | 🟢상 | [MiMedx SEC Form 8-K (Q1 2026) / StockTitan](https://www.stocktitan.net/sec-filings/MDXG/8-k-mimedx-group-inc-reports-material-event-7e6f3709a922.html) |
| EV-MMX-006 | IP·특허 | MiMedx는 콜라겐 섬유의 선형 배열 및 가교로 최적 강성·강도의 기계적 구조물을 만드는 CollaFix 특허군(2015년 한 해에만 8건 등록)과 33건 이상의 양막·태반 특허 및 다수 출원을 보유한다. | 주요언론 | 🟠중 | [PR Newswire (MiMedx 특허 등록 발표)](https://www.prnewswire.com/news-releases/mimedx-awarded-12-new-us-patents-ytd-2015-with-four-awarded-for-its-amniotic-membrane-allografts-and-eight-awarded-for-its-collafix-technology-300182314.html) |
| EV-MMX-008 | 파트너십·M&A | CollaFix 콜라겐 섬유 원천기술은 Shriners Hospitals for Children 및 University of South Florida Research Foundation으로부터 전 세계 독점 라이선스로 도입되었으며, 발명자 Dr. Thomas Koob가 MiMedx 최고과학책임자(CSO)로 합류했다. | IR·공시 | 🟢상 | [Technology License Agreement (Shriners–MiMedx), Justia Contracts](https://contracts.justia.com/companies/mimedx-group-inc-888/contract/1110917/) |
| EV-MMX-011 | 파트너십·M&A | MiMedx는 2025년 12월 19일 RegenKit-Wound Gel의 미국 독점 유통계약을 체결하고, 2026년 G4Derm Plus의 미국 독점 유통권을 확보하는 등 유통 파트너십으로 창상 포트폴리오를 확장 중이다. | 주요언론 | 🟠중 | [MiMedx 보도자료 / StockTitan·GlobeNewswire 종합](https://www.stocktitan.net/news/MDXG/) |

### Mission Barns, Inc.

연관 판정 — **mTG**: 무관/하 · **ADC**: 무관/하 · **Collagen**: 인접·응용/하

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-MIS-001 | 사업분야 | Mission Barns의 주력 제품은 배양 돼지 지방(cultivated pork fat)을 식물성 단백질과 결합한 이탈리안 스타일 배양 미트볼과 애플우드 훈제 배양 베이컨이다. | 주요언론 | 🟠중 | [Quality Assurance & Food Safety / Cultivated X](https://www.qualityassurancemag.com/news/mission-barns-announces-cell-cultivated-pork-fat-launch-following-fda-clearance/) |
| EV-MIS-002 | 사업분야 | Mission Barns는 2018년 前 Eat Just 과학자 Eitan Fischer가 설립한 미국(SF/Berkeley) 배양 지방 스타트업으로, 첫 제품은 배양 돼지 지방 'Mission Fat'이다. | 주요언론 | 🟠중 | [vegconomist / AgFunderNews](https://agfundernews.com/mission-barns-unveils-novel-scalable-adherent-bioreactor-for-cultivated-meat-fat) |
| EV-MIS-003 | 연구분야 | Mission Barns의 핵심 플랫폼은 non-GMO 부착성(adherent) 세포를 동물성 성분 없는 배지에서 배양하는 것으로, 조직 형성·통합을 위해 식용 스캐폴드(edible scaffold)에 세포를 부착시킨다. | 주요언론 | 🟠중 | [vegconomist](https://vegconomist.com/cultivated-cell-cultured-biotechnology/mission-barns-revamps-pharma-bioreactors-cultivated-meat-production/) |
| EV-MIS-006 | 뉴스·동향 | Mission Barns는 2025년 FDA로부터 'No Questions' 레터를 받아 세계 최초로 배양 돼지 지방에 대한 규제 승인을 획득했다. | 주요언론 | 🟠중 | [AgFunderNews / Quality Assurance & Food Safety](https://agfundernews.com/breaking-mission-barns-secures-fda-approval-for-cultivated-fat-gears-up-for-us-launch) |
| EV-MIS-007 | 뉴스·동향 | Mission Barns는 SF 파일럿 시설에 대한 USDA 검사 승인(grant of inspection)과 라벨 승인을 받아 2025년 3분기 출시를 계획했다. | 주요언론 | 🟠중 | [Cultivated X / AgFunderNews](https://agfundernews.com/mission-barns-secures-usda-green-light-for-cultivated-fat-plans-q3-launches) |
| EV-MIS-010 | 뉴스·동향 | Mission Barns는 특허 바이오리액터 기술을 성분 제조사에 라이선스/플러그인 형태로 제공하는 사업 확장을 계획하고 있다. | 주요언론 | 🟠중 | [Green Queen / FoodNavigator-USA](https://www.greenqueen.com.hk/mission-barns-cultivated-pork-fat-lab-grown-meat-novel-bioreactors/) |
| EV-MIS-004 | IP·특허 | Mission Barns는 배양육·배양지방 저비용 대량생산을 위한 회전식 성장/스페이서 디스크 기반 스케일러블 바이오리액터 특허(US20230100306A1, HK40087052A)를 보유한다. | 특허 | 🟢상 | [Google Patents](https://patents.google.com/patent/US20230100306A1/en) |
| EV-MIS-005 | IP·특허 | Mission Barns 바이오리액터 특허(US20230100306A1)는 세포 부착 향상 코팅 옵션으로 fibronectin, gelatin(젤라틴), collagen(콜라겐)을 명시하나, transglutaminase/mTG 가교는 언급하지 않는다. | 특허 | 🟠중 | [Google Patents](https://patents.google.com/patent/US20230100306A1/en) |
| EV-MIS-008 | 파트너십·M&A | Mission Barns는 SF 베이 지역 이탈리안 레스토랑 그룹 Fiorella 및 Sprouts Farmers Market과 제휴해 배양육 제품을 출시하며, Sprouts는 배양육을 판매하는 첫 미국 식료품점이 되었다. | 주요언론 | 🟠중 | [Green Queen / Cultivated X](https://www.greenqueen.com.hk/mission-barns-lab-grown-pork-fat-fda-approved-cultivated-meat-sprouts-fiorella/) |
| EV-MIS-009 | 파트너십·M&A | Mission Barns는 2021년 4월 $24M Series A를 포함해 2025년 3월 기준 누적 $60M 이상을 조달했으며, 10X Capital·Analog Ventures·BlackPine 등 32개 투자자가 참여했다. | 주요언론 | 🟠중 | [Food Dive / PitchBook](https://www.fooddive.com/news/cultivated-fat-startup-mission-barns-raises-24m-to-scale-up/598037/) |

### Mosa Meat B.V.

연관 판정 — **mTG**: 인접·응용/하 · **ADC**: 무관/하 · **Collagen**: 인접·응용/하

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-MOS-001 | 사업분야 | Mosa Meat는 2016년 네덜란드 마스트리흐트에서 설립된 배양육 기업으로, Limousin 소의 근육·지방 세포를 배양해 배양 소고기(햄버거)를 만든다. | 기타 | 🔴하 | [Wikipedia (Mosa Meat)](https://en.wikipedia.org/wiki/Mosa_Meat) |
| EV-MOS-002 | 사업분야 | 첫 상업 제품은 식물성 원료와 혼합하는 '배양 소고기 지방(cultivated beef fat)'으로, 햄버거·미트볼·볼로네제 등 하이브리드 육제품을 겨냥하며 초기에는 외식·레스토랑 채널을 우선한다. | 주요언론 | 🟠중 | [FoodNavigator](https://www.foodnavigator.com/Article/2025/01/22/mosa-meat-submits-application-to-eu/) |
| EV-MOS-003 | 연구분야 | 2022년 우태아혈청(FBS) 없이, 유전자 변형 없이 근육 세포를 분화시키는 방법을 피어리뷰 논문으로 발표하는 등 무혈청 배지·분화 기술을 핵심 R&D로 삼는다. | 주요언론 | 🟠중 | [AgFunderNews](https://agfundernews.com/mosa-meat-opens-facility-sees-a-clear-path-towards-price-parity) |
| EV-MOS-004 | 연구분야 | 구조화 방식으로 제품에 남는 영구 스캐폴드 대신, 세포를 담은 '용해성 알지네이트 하이드로겔'로 세포를 배치·자기조직화시켜 근육·지방을 분화·구조화한다. | 업계리포트 | 🟠중 | [GFI / Cultured meat scaffolding + Mosa 접근법](https://gfi.org/science/the-science-of-cultivated-meat/deep-dive-cultivated-meat-scaffolding/) |
| EV-MOS-005 | 연구분야 | 알지네이트 하이드로겔에 RGD 등 세포접착 펩타이드(콜라겐·피브로넥틴 모방)를 접합해 세포 부착·분화를 유도하며, 동물유래 콜라겐 사용은 배양육 원칙과 상충하므로 의도적으로 회피한다. | 특허 | 🟢상 | [Google Patents WO2021158105A1](https://patents.google.com/patent/WO2021158105A1/en) |
| EV-MOS-009 | 뉴스·동향 | 2025년 1월 Mosa Meat는 EU 역사상 첫 배양 소고기 제품(배양 지방)에 대한 노벨푸드 시장허가를 신청했으며 EFSA/EC 심사는 약 18개월 소요 예상이다. | 주요언론 | 🟠중 | [FoodNavigator](https://www.foodnavigator.com/Article/2025/01/22/mosa-meat-submits-application-to-eu/) |
| EV-MOS-010 | 뉴스·동향 | 2025년 12월 Mosa Meat는 Invest-NL·LIOF·PHW Group·Jitse Groen 등 기존 투자자로부터 약 €15M($17.6M)를 유치해 2028년까지 자금여력을 확보했고, 최초 버거 대비 99.999% 원가절감을 달성했다고 밝혔다. | 주요언론 | 🟠중 | [Green Queen](https://www.greenqueen.com.hk/mosa-meat-lab-grown-meat-cultivated-beef-costs-funding/) |
| EV-MOS-011 | 뉴스·동향 | Mosa Meat는 싱가포르·EU·스위스·영국에 규제 허가를 신청했으며 영국을 첫 승인 시장으로 기대하고, 싱가포르에서는 Aleph Farms에 이어 두 번째로 배양 소고기 출시를 준비한다. | 주요언론 | 🟠중 | [Green Queen](https://www.greenqueen.com.hk/mosa-meat-funding-cultivated-beef-lab-grown-meat-singapore/) |
| EV-MOS-006 | IP·특허 | 특허 WO2021158105A1 'Hydrogels for cultured meat production'은 저분자 알지네이트+RGD 펩타이드를 칼슘 이온 가교 및 카보디이미드(EDC) 화학으로 가교하며, 콜라겐 회피·mTG 미사용을 확인한다. | 특허 | 🟢상 | [Google Patents](https://patents.google.com/patent/WO2021158105A1/en) |
| EV-MOS-007 | IP·특허 | 미국 출원 US20240148034 'Constructs comprising fibrin or other blood products for meat cultivation'은 피브린 등 혈액유래 단백질 기반 배양육 구조체를 다룬다. | 특허 | 🟠중 | [Justia Patents](https://patents.justia.com/patent/20240148034) |
| EV-MOS-008 | IP·특허 | Mosa Meat는 US20230203420A1(하이드로겔 내 세포 가압으로 비대 유도), WO2023224484A1(지방 배양용 하이드로겔 섬유 형성) 등 하이드로겔·바이오리액터 특허 포트폴리오를 보유한다. | 특허 | 🟠중 | [Google Patents / Justia (Mosa Meat 지정)](https://patents.justia.com/assignee/mosa-meat-b-v) |
| EV-MOS-012 | 파트너십·M&A | Mosa Meat는 설립 이후 Blue Horizon, Bell Food Group, Nutreco, Mitsubishi Corporation, M Ventures, Leonardo DiCaprio 등으로부터 누적 약 1억 달러 이상을 유치했다. | 주요언론 | 🟠중 | [AgFunderNews / Wikipedia](https://agfundernews.com/mosa-meat-opens-facility-sees-a-clear-path-towards-price-parity) |

### Nexture Bio, Inc. (formerly Matrix Meats / Matrix Food Technologies)

연관 판정 — **mTG**: 무관/하 · **ADC**: 무관/하 · **Collagen**: 인접·응용/중

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-NXT-001 | 사업분야 | Nexture Bio는 배양육(cellular agriculture)용 동물성분 무함유(animal-component-free) 식물 기반 마이크로캐리어·스캐폴드·세포부착인자를 개발·공급한다. | 업계리포트 | 🟠중 | [GFI Alternative Protein Ecosystem / Cultivated X](https://ecosystem.gfi.org/company/nexture-bio/) |
| EV-NXT-002 | 사업분야 | 주력 제품은 ProSphere 마이크로캐리어(완두/대두 다당류, 125-425µm)와 다공성 다당류 기반 Sponge Scaffold 등 식물성 3D 세포배양 소재다. | 주요언론 | 🟠중 | [Cellbase / Ilex Life Sciences 제품 페이지 (Nexture Bio 유통)](https://cellbase.com/products/nexture-bio-sponge-scaffold) |
| EV-NXT-003 | 사업분야 | 오하이오주 Xenia에 R&D 연구소, 캘리포니아주 Vacaville에 파일럿 규모 GMP 생산시설을 운영(개보수 중)한다. | 주요언론 | 🟠중 | [Protein Production Technology International](https://www.proteinproductiontechnology.com/post/nexture-bio-acquires-matrix-food-technologies-to-expand-animal-component-free-solutions) |
| EV-NXT-004 | 사업분야 | 배양육 외에 세포치료(cell therapy)용 마이크로캐리어·스캐폴드도 응용 분야로 제시하며 바이오메디컬 시장을 겨냥한다. | 공식홈페이지 | 🟠중 | [Nexture Bio 공식 홈페이지 (Cell Therapy 응용 페이지)](https://nexturebio.com/applications/cell-therapy/) |
| EV-NXT-005 | 연구분야 | 핵심 기술 플랫폼은 전기방사(electrospinning)/electrospraying로 살아있는 조직의 세포외기질(ECM)을 모사하는 나노섬유 스캐폴드이며, 소재 옵션에 콜라겐·젤라틴·식물단백질 등이 포함된다. | 주요언론 | 🟠중 | [FoodIngredientsFirst / FoodNavigator-USA (Matrix Meats)](https://www.foodingredientsfirst.com/news/matrix-meats-nanofiber-scaffold-system-boosts-cell-growth-and-texture-in-cultured-meat-production.html) |
| EV-NXT-006 | 연구분야 | 전기방사 나노섬유 기술은 재생의학용 전기방사 스캐폴드 전문기업 Nanofiber Solutions에서 약 15년간 축적된 것을 배양육에 이전한 것이다(공동창업자 Dr. Jed Johnson). | 주요언론 | 🟠중 | [LabGrownMeat.com / FoodNavigator-USA](https://labgrownmeat.com/matrix-meats/) |
| EV-NXT-013 | 연구분야 | 현재 Nexture Bio의 제품 전략은 '동물성분 무함유(ACF)'로, 동물 유래 콜라겐·젤라틴 등을 식물 다당류(완두·대두)로 대체하는 방향이다. | 업계리포트 | 🟠중 | [GFI / 공식 홈페이지 검색 스니펫](https://ecosystem.gfi.org/company/nexture-bio/) |
| EV-NXT-014 | 연구분야 | Nexture Bio/Matrix Meats가 미생물 트랜스글루타미나제(mTG)를 스캐폴드 가교에 사용한다는 직접 증거는 확인되지 않았다. | 기타 | 🟠중 | [복수 검색(공식·언론·특허) 종합](https://www.freepatentsonline.com/y2020/0245658.html) |
| EV-NXT-015 | 연구분야 | Nexture Bio는 항체-약물 접합체(ADC) 파이프라인·링커·접합기술 또는 ADC용 mTG 공급과 무관하다(관련 증거 없음). | 기타 | 🟠중 | [웹 검색 종합 (ADC 결과는 별개 회사 NextCure)](https://www.biospace.com/antibody-drug-conjugate-adc) |
| EV-NXT-009 | 뉴스·동향 | 2025년 1월(약 2025-01-19) Nexture Bio가 식물 기반 식용 나노섬유 스캐폴드·마이크로비드 제조사 Matrix Food Technologies(구 Matrix Meats)를 인수했다. | 주요언론 | 🟠중 | [EIN Presswire / New Tech Foods / Cultivated X](https://www.newtechfoods.com/news/nexture-bio-expands-portfolio-with-acquisition-of-matrix-ft) |
| EV-NXT-010 | 뉴스·동향 | 2025년 중 다수의 신규 마이크로캐리어 제품 출시를 계획하며 whole-cut(통살) 배양육용 스캐폴드 개발을 목표로 미국 시장에 진입했다. | 주요언론 | 🟠중 | [vegconomist / Cultivated X](https://vegconomist.com/cultivated-cell-cultured-biotechnology/cultivated-meat/nexture-bio-us-scaffoldings-whole-cut-cultivated-meat/) |
| EV-NXT-007 | IP·특허 | 미국 특허출원 US2020/0245658 'Electrospun Polymer Fibers for Cultured Meat Production'(출원인 Nanofiber Solutions LLC, 출원 2020-02-03)은 전기방사 소재로 collagen·gelatin을 명시한다. | 특허 | 🟢상 | [FreePatentsOnline](https://www.freepatentsonline.com/y2020/0245658.html) |
| EV-NXT-008 | IP·특허 | Matrix Meats 스캐폴드 기술은 약 50건의 등록·출원 특허로 뒷받침되며, 이 특허·영업비밀·데이터가 2025년 Nexture Bio에 통합되었다. | 주요언론 | 🟠중 | [LabGrownMeat.com / Protein Production Technology International](https://www.proteinproductiontechnology.com/post/nexture-bio-acquires-matrix-food-technologies-to-expand-animal-component-free-solutions) |
| EV-NXT-011 | 파트너십·M&A | Nexture Bio는 2023년 12월 Generation Food Rural Partners(GFRP) 펀드에 의해 설립된 포트폴리오사이며 Big Idea Ventures가 투자자로 참여, 약 $1M을 조달했다. | 업계리포트 | 🟠중 | [Crunchbase / New Tech Foods (Big Idea Ventures)](https://www.crunchbase.com/organization/nexture-bio-inc) |
| EV-NXT-012 | 파트너십·M&A | 전신 Matrix Meats는 Nanofiber Solutions와 Ikove Startup Nursery의 합작으로 설립, 2020년 12월 Unovis Asset Management 주도 시드 라운드(CPT Capital·Siddhi Capital·Clear Current Capital·Ikove 참여)를 마감했고 7개국 14개 배양육 생산기업과 개발 협력 관계를 맺었다. | 주요언론 | 🟠중 | [PR Newswire / FinSMEs](https://www.prnewswire.com/news-releases/matrix-meats-completes-seed-stage-round-301196900.html) |

### Nitta Gelatin Inc.

연관 판정 — **mTG**: 인접·응용/중 · **ADC**: 무관/하 · **Collagen**: 직접사업/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-NIT-001 | 사업분야 | Nitta Gelatin은 1918년 창업, 100년 이상 젤라틴·콜라겐 펩타이드를 식품·건강식품·제약 시장에 공급하며 6개국 11개 그룹사를 운영한다. | 공식홈페이지 | 🟢상 | [Nitta Gelatin NA 공식 홈페이지 (검색 스니펫)](https://nitta-gelatin.com/) |
| EV-NIT-002 | 사업분야 | 주력 제품은 소·돼지·어류 유래 젤라틴과 콜라겐 펩타이드로 식품·영양·제약·화장품·기술 용도로 공급된다. | 주요언론 | 🟠중 | [IngredientsNetwork / nutraingredients (Nitta Gelatin 프로필)](https://www.ingredientsnetwork.com/nitta-gelatin-inc-comp314845.html) |
| EV-NIT-003 | 사업분야 | 건강기능성 브랜드 Wellnex 콜라겐 펩타이드(피부·뼈·관절·근육·혈관·인지 기능)와 표준 대비 최대 30배 PO/OG 함량의 Wellnex Replenwell을 제공한다. | 공식홈페이지 | 🟢상 | [Nitta Gelatin 공식 홈페이지 (Wellnex/Collagen Peptides)](https://nitta-gelatin.com/products/collagen-peptides/) |
| EV-NIT-004 | 사업분야 | 생의료 사업으로 저엔도톡신 젤라틴·콜라겐 브랜드 beMatrix를 세포시트 이송·세포이식·bone void filler 등에 공급한다. | 공식홈페이지 | 🟢상 | [beMatrix Biomedical / Nitta Gelatin 공식](https://bematrixbiomedical.com/) |
| EV-NIT-005 | 연구분야 | 세포배양용 아텔로콜라겐 Cellmatrix(돼지 힘줄·피부 유래, Type I)를 30년 이상 3D 배양·재생의학·조직공학·암생물학용으로 개발·공급한다. | 공식홈페이지 | 🟢상 | [Nitta Gelatin Cellmatrix (Biomedical) / FUJIFILM Wako](https://www.nitta-gelatin.co.jp/en/business_activities/market/biomedical/cellmatrix/cellmatrix.html) |
| EV-NIT-006 | 연구분야 | beMatrix Collagen AT가 Takahashi 연구팀의 세계 최초 iPS 세포 유래 망막색소상피(RPE) 세포시트 이식 임상연구(가령성 황반변성) 배양 재료로 사용됐다. | 공식홈페이지 | 🟢상 | [beMatrix Biomedical 공식 / PLOS ONE·PMC](https://bematrixbiomedical.com/products/) |
| EV-NIT-012 | 연구분야 | Nitta Gelatin의 젤라틴(오사카)이 미생물 트랜스글루타미나제(mTG) 가교 연구의 기질로 실제 사용되어, 조직공학 스캐폴드·GelMA 3D 프린팅·근육 배양 하이드로겔에 응용된다. | 논문 | 🟢상 | [ScienceDirect / IOPscience (mTG-gelatin 가교 논문들)](https://iopscience.iop.org/article/10.1088/1758-5090/ab063f) |
| EV-NIT-013 | 연구분야 | 젤라틴·콜라겐 기반 스캐폴드는 배양육(cell-cultured meat) 세포 접착·구조 재료로 활발히 연구되며, mTG 가교로 기계적 안정성을 부여하는 접점이 존재한다. | 논문 | 🟠중 | [PubMed / PMC (Functionalized Gelatin-Based Materials for Cell-Cultured Meat)](https://pubmed.ncbi.nlm.nih.gov/41029968/) |
| EV-NIT-009 | 뉴스·동향 | 합작사 Nitta Gelatin India(NGIL, KSIDC와 JV)가 2024년 콜라겐 펩타이드 생산능력을 600→1150 MT/년으로 늘리는 증설(투자 약 Rs 460M)을 착공, 2025년 7월 가동 예정이다. | 주요언론 | 🟠중 | [Nitta Gelatin India / Global Flow Control / Chemical Weekly](https://gelatin.in/The-Ground-Breaking-ceremony-of-Nitta-Gelatin-India) |
| EV-NIT-007 | IP·특허 | Nitta Gelatin은 콜라겐 펩타이드 유래 이펩타이드(Hyp-Gly 등)와 골다공증·골관절염 억제 응용에 대한 미국특허 US8227424B2를 보유한다. | 특허 | 🟢상 | [Google Patents US8227424B2](https://patents.google.com/patent/US8227424B2/en) |
| EV-NIT-008 | IP·특허 | 관련 계열 특허 US8410062B2(Collagen peptide, dipeptide and malady inhibitor)도 Nitta Gelatin 명의로 등록되어 콜라겐 펩타이드 기능성 IP 포트폴리오를 형성한다. | 특허 | 🟠중 | [Google Patents US8410062B2](https://patents.google.com/patent/US8410062B2/en) |
| EV-NIT-014 | IP·특허 | Nitta Gelatin은 mTG를 이용한 ADC(항체-약물 접합) 자체 특허·파이프라인이 확인되지 않으며, ADC 모달리티와 직접 관련이 없다. | 기타 | 🟠중 | [웹검색 종합(Nitta Gelatin + ADC/site-specific conjugation)](https://pubmed.ncbi.nlm.nih.gov/31161507/) |
| EV-NIT-010 | 파트너십·M&A | Nitta Gelatin은 2019년 12월 콜라겐 케이싱 사업부(미국 NJ 압출·캐나다 온타리오 가공 및 콜라겐 젤·바이오메디컬 포함) Nitta Casings를 Viscofan에 약 US$13.5M에 매각했다. | 주요언론 | 🟠중 | [Nitta Casings / FoodNavigator](https://www.foodnavigator.com/Article/2020/01/03/Viscofan-to-acquire-Japanese-firm-Nitta-Casings/) |
| EV-NIT-011 | 파트너십·M&A | 인도 사업은 Nitta Gelatin Japan과 Kerala State Industrial Development Corp(KSIDC)의 합작(NGIL)으로 운영되며 케랄라주 Kakkanad에 젤라틴·콜라겐 펩타이드 생산·본사 확장을 추진한다. | 공식홈페이지 | 🟢상 | [Nitta Gelatin India (gelatin.in)](https://gelatin.in/The-Ground-Breaking-ceremony-of-Nitta-Gelatin-India) |

### Organogenesis Holdings Inc.

연관 판정 — **mTG**: 인접·응용/하 · **ADC**: 무관/하 · **Collagen**: 직접사업/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-ORG-001 | 사업분야 | Organogenesis는 재생의학 기업으로 첨단 창상치유(Advanced Wound Care)와 수술·스포츠의학(Surgical & Sports Medicine) 2개 사업부문을 운영한다. | 공식홈페이지 | 🟢상 | [Organogenesis 공식 홈페이지 / Yahoo Finance 기업개요](https://www.organogenesis.com/advanced-wound-care/) |
| EV-ORG-002 | 사업분야 | FY2025 순제품매출은 5.63억 달러로 전년(4.82억 달러) 대비 8,100만 달러 증가한 기록적 매출을 기록했다. | IR·공시 | 🟠중 | [SEC Form 8-K (FY2025) / Organogenesis IR 보도자료](https://www.sec.gov/Archives/edgar/data/0001661181/000095017025105032/orgo-ex99_1.htm) |
| EV-ORG-003 | 사업분야 | Apligraf는 이중층 생체공학 피부대체재로, 진피층이 소(bovine) I형 콜라겐 격자(collagen lattice)에 인간 섬유아세포를 배양한 구조다. | 특허 | 🟢상 | [US20090232878A1 (Artificial Skin Substitute) / WoundSource](https://patents.google.com/patent/US20090232878A1/en) |
| EV-ORG-004 | 사업분야 | PuraPly AM은 정제된 가교(cross-linked) 돼지유래 콜라겐 매트릭스에 항균제 PHMB를 결합한 FDA 승인 제품으로, 콜라겐 기반 창상 매트릭스가 핵심 소재다. | 주요언론 | 🟠중 | [Practical Dermatology / BioSpace (PuraPly AM RCT)](https://practicaldermatology.com/news/organogenesis-launches-puraply-wound-management-products) |
| EV-ORG-005 | 연구분야 | 핵심 R&D 파이프라인 ReNu는 무릎 골관절염 통증 관리용 동결보존 양막현탁 동종이식(amniotic suspension allograft)으로 세포·성장인자·세포외기질(ECM) 성분을 함유하며 2021년 FDA RMAT 지정을 받았다. | IR·공시 | 🟢상 | [Organogenesis IR 보도자료 / StockTitan](https://investors.organogenesis.com/news-releases/news-release-details/organogenesis-announces-initiation-biologics-license-application) |
| EV-ORG-011 | 연구분야 | Organogenesis는 종양학 항체-약물 접합체(ADC) 파이프라인이나 링커·페이로드·접합 기술을 보유하지 않으며, 사업은 재생의학(창상·수술/스포츠의학)에 국한된다. | 공식홈페이지 | 🟠중 | [Organogenesis 사업개요 / ADC 파이프라인 검색 결과](https://www.organogenesis.com/advanced-wound-care/) |
| EV-ORG-006 | 뉴스·동향 | 2025년 12월 FDA Type-B 미팅 후 ReNu BLA 롤링 제출을 개시했고, 2026년 4월 28일 임상·CMC 모듈로 제출을 완료했다. | 주요언론 | 🟠중 | [StockTitan / Investing.com](https://www.stocktitan.net/news/ORGO/) |
| EV-ORG-007 | 뉴스·동향 | 2025년 4분기 첨단창상치유(AWC) 순제품매출은 2.172억 달러로 전년 동기 대비 83% 증가하며 기록적 매출을 달성했다. | IR·공시 | 🟠중 | [SEC Form 8-K (FY2025) / Organogenesis IR](https://investors.organogenesis.com/news-releases/news-release-details/organogenesis-holdings-inc-reports-fourth-quarter-2025-financial) |
| EV-ORG-008 | IP·특허 | Organogenesis Inc.는 다수의 콜라겐 관련 특허를 보유한다: 전기처리 콜라겐(US8586345B2), 인공피부(US20090232878A1), PHMB 함유 정제 콜라겐 창상매트릭스(CWM) 등. | 특허 | 🟢상 | [Google Patents / Justia (Patents Assigned to Organogenesis Inc.)](https://patents.justia.com/assignee/organogenesis-inc) |
| EV-ORG-009 | IP·특허 | 트랜스글루타미나제(mTG) 가교 콜라겐은 공지 기술이나, 검색된 관련 특허(US20080305517A1 등)는 Organogenesis 소유가 아니며 Organogenesis가 mTG 효소를 자사 콜라겐 가교에 사용한다는 증거는 확인되지 않았다. | 특허 | 🟠중 | [Google Patents (검색) / Organogenesis 특허 대조](https://patents.google.com/patent/US20080305517A1/en) |
| EV-ORG-010 | 파트너십·M&A | Organogenesis는 2017년 NuTech Medical, 2020년 CPN Biosciences를 인수했고 2018년 Avista Healthcare와 합병해 상장했다. | 공식홈페이지 | 🟢상 | [Organogenesis Careers(연혁) / PR Newswire](https://careers.organogenesis.com/our-history) |

### RegenHU (REGENHU AG)

연관 판정 — **mTG**: 무관/하 · **ADC**: 무관/하 · **Collagen**: 인접·응용/중

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-RGH-001 | 사업분야 | RegenHU는 스위스 Villaz-St-Pierre 소재 바이오프린팅 전문기업으로 3D 바이오프린터·바이오잉크·소프트웨어를 개발·판매한다. | 공식홈페이지 | 🟢상 | [RegenHU 공식 홈페이지](https://www.regenhu.com/) |
| EV-RGH-002 | 사업분야 | 주력 제품은 3D 바이오프린터 라인(3DDiscovery, R-GEN 100/200, BioFactory)과 SHAPER 소프트웨어이며 타깃 시장은 조직공학·재생의학·약물발굴·경구제형이다. | 공식홈페이지 | 🟢상 | [RegenHU R-GEN 100 제품 페이지](https://www.regenhu.com/3dbioprinting-solutions/r-gen-100-3dbioprinter/) |
| EV-RGH-003 | 사업분야 | RegenHU는 화학적으로 정의된 자체 바이오소재 BioInk(하이드로겔)와 OsteoInk(인산칼슘 페이스트)를 3D 조직 프린팅용으로 공급한다. | 업계리포트 | 🟠중 | [Tracxn 기업 프로필](https://tracxn.com/d/companies/regenhu/__lpOJrCL5ELRwXRZ9EzxeWkToFFvDqgExglCHB5YfndE) |
| EV-RGH-004 | 연구분야 | RegenHU 바이오프린터는 콜라겐·젤라틴 기반 바이오잉크 프린팅을 가능하게 하는 인에이블링 플랫폼으로, 피부 패치·심장 패치·HAP/콜라겐 골 스캐폴드 등에 광범위하게 사용된다. | 주요언론 | 🟠중 | [3DPrint.com — regenHU therapeutical bioprinting](https://3dprint.com/246275/european-bioprinter-regenhu-is-paving-the-way-in-therapeutical-bioprinting/) |
| EV-RGH-005 | 연구분야 | 3DDiscovery는 열가소성·하이드로겔·세포를 프린팅하고 광가교(photocrosslinking)·고저온 프린트헤드를 지원하는 모듈형 조직공학 플랫폼이다. | 업계리포트 | 🟠중 | [Aniwaa — RegenHU 3DDiscovery review](https://www.aniwaa.com/product/3d-printers/regenhu-3ddiscovery/) |
| EV-RGH-012 | 연구분야 | RegenHU와 무관하게, mTG(미생물 트랜스글루타미나제)를 이용한 항체-약물 접합(ADC) 연구는 유사 상호의 별개 기업 Regeneron 등에서 수행된 것으로, RegenHU의 mTG/ADC 접점은 확인되지 않는다. | 논문 | 🟢상 | [ScienceDirect(Regeneron ADC mTG 연구)](https://www.sciencedirect.com/science/article/abs/pii/S0022354923003258) |
| EV-RGH-006 | 뉴스·동향 | RegenHU는 R-GEN 시리즈(R-GEN 100/200)와 SHAPER 소프트웨어를 신규 출시하며 사업 전반을 개편했다. | 공식홈페이지 | 🟠중 | [RegenHU 공식 뉴스](https://www.regenhu.com/community/news/regenhu-launches-r-gen-series-and-shaper/) |
| EV-RGH-007 | 뉴스·동향 | RegenHU는 미국 미네소타(Medical Alley)에 첫 미국 사무소를 개설했다. | 공식홈페이지 | 🟠중 | [RegenHU 공식 뉴스(office-opening 태그)](https://www.regenhu.com/tag/office-opening/) |
| EV-RGH-008 | IP·특허 | REGENHU AG는 조직대체물 프린팅 시스템용 카트리지 등 바이오프린팅 하드웨어·디스펜싱 특허를 보유한다(예: US10391203). | 특허 | 🟠중 | [Justia Patents — Assigned to REGENHU AG](https://patents.justia.com/assignee/regenhu-ag) |
| EV-RGH-009 | IP·특허 | RegenHU 3D Discovery 바이오프린터는 셀룰로오스 나노섬유·알지네이트 바이오잉크 등 제3자 바이오잉크 특허의 실시 장비로 반복 인용된다. | 특허 | 🟠중 | [Google Patents US10675379B2](https://patents.google.com/patent/US10675379B2/en) |
| EV-RGH-010 | 파트너십·M&A | RegenHU는 EU FLAMIN-GO 컨소시엄에 참여해 류마티스 관절염 synovia-on-chip용 맞춤형 바이오프린터·소프트웨어와 기술지원을 제공한다. | 주요언론 | 🟠중 | [RegenHU 공식 뉴스 / News-Medical](https://www.news-medical.net/news/20210204/REGENHU-announces-its-participation-in-the-FLAMIN-GO-project-aimed-at-developing-personalized-treatments-against-rheumatoid-arthritis.aspx) |
| EV-RGH-011 | 파트너십·M&A | RegenHU는 Nivalis Group(스위스 CPA Group SA 계열)에 인수되어 소속되어 있으며 AO Research Institute(ARI)와 그룹 관계를 표기한다. | 업계리포트 | 🟠중 | [PitchBook / RegenHU 그룹 페이지](https://www.regenhu.com/group/ao-research-institute-ari/) |

### Regenity Biosciences (구 Collagen Matrix, Inc.)

연관 판정 — **mTG**: 인접·응용/하 · **ADC**: 무관/하 · **Collagen**: 직접사업/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-RGN-001 | 사업분야 | Regenity는 콜라겐·합성폴리머·바이오세라믹·미네랄 플랫폼 기반의 생분해성(bioresorbable) 재생 의료기기를 개발·제조하며 CDM(위탁개발·제조) 서비스를 제공하고, 71개 이상 제품라인을 보유한다. | 주요언론 | 🟠중 | [PR Newswire (Regenity 리브랜딩 보도자료)](https://www.prnewswire.com/news-releases/collagen-matrix-inc-unveils-new-brand-and-name-as-regenity-biosciences-301782756.html) |
| EV-RGN-002 | 사업분야 | 회사는 1997년 Collagen Matrix, Inc.로 설립되어 콜라겐 기반 의료기기로 출발했고, Polyganics 인수 후 2023년 3월 28일 Regenity Biosciences로 사명·브랜드를 변경했다. | 주요언론 | 🟠중 | [ODT (Orthopedic Design & Technology)](https://www.odtmag.com/breaking-news/collagen-matrix-rebrands-to-regenity-biosciences/) |
| EV-RGN-003 | 사업분야 | Collagen Matrix(현 Regenity)는 콜라겐 기반 조직·골 재생 제품을 정형·스포츠의학·치과·신경외과 시장의 OEM·private label 고객에게 위탁·주문 방식으로 공급해 왔다. | 기타 | 🟠중 | [MTEC (Medical Technology Enterprise Consortium) 기업 프로필](https://mtec-sc.org/life-sciences/collagen-matrix-inc) |
| EV-RGN-004 | 연구분야 | Regenity의 Matrixflex는 돼지 유래 가교(crosslinked) 콜라겐 치과용 막으로, 중국 174명 6개월 다기관 RCT에서 Geistlich 비가교 Bio-Gide 막과 비교 평가되어 NMPA 승인을 받았다. | 주요언론 | 🟠중 | [PR Newswire (Matrixflex NMPA 승인 보도자료)](https://www.prnewswire.com/news-releases/regenity-biosciences-receives-regulatory-approval-for-collagen-dental-membrane-in-china-after-first-of-its-kind-breakthrough-clinical-study-302237209.html) |
| EV-RGN-005 | 연구분야 | RejuvaKnee는 소(bovine) 유래 콜라겐 기반 반월판(meniscus) 재생 임플란트로 2024년 10월 8일 FDA 510(k) 승인을 받았고 2025년 R&D 100 Award를 수상했다. | 주요언론 | 🟠중 | [PR Newswire (RejuvaKnee 510k 보도자료)](https://www.prnewswire.com/news-releases/regenity-biosciences-receives-510k-clearance-for-rejuvaknee-a-groundbreaking-regenerative-meniscus-implant-device-to-redefine-the-standard-of-care-302269177.html) |
| EV-RGN-006 | 연구분야 | DuraMatrix Repair는 고순도 I형·III형 소 콜라겐으로 구성된 흡수성 경막(dura) 재생 막으로 2025년 11월 회사의 63번째 FDA 510(k) 승인을 획득했다. | 주요언론 | 🟠중 | [PR Newswire (63번째 510k 보도자료)](https://www.prnewswire.com/news-releases/regenity-biosciences-marks-63rd-fda-510k-clearance-with-expansion-of-neurosurgical-portfolio-302625154.html) |
| EV-RGN-013 | 연구분야 | Regenity가 항체-약물 접합체(ADC)·면역접합체·bioconjugation·종양학 페이로드/링커에 관여한다는 근거는 확인되지 않았다. | 기타 | 🟠중 | [웹검색 (Regenity + ADC/bioconjugation) 결과](https://regenity.com/) |
| EV-RGN-014 | 연구분야 | Regenity의 가교 콜라겐 제품(Matrixflex 등)에서 미생물 트랜스글루타미나제(mTG) 효소 가교를 사용한다는 근거는 확인되지 않았으며, 확인된 가교 방식은 화학 가교제/환원당 계열로 나타난다. | 기타 | 🟠중 | [웹검색 (Regenity/Collagen Matrix + transglutaminase / crosslinking method)](https://www.prnewswire.com/news-releases/regenity-biosciences-receives-regulatory-approval-for-collagen-dental-membrane-in-china-after-first-of-its-kind-breakthrough-clinical-study-302237209.html) |
| EV-RGN-012 | 뉴스·동향 | 회사는 중등도~고삼출 창상 관리 및 미세출혈 제어용 섬유상(fibrillar) 마이크로피브릴 콜라겐 창상 드레싱의 510(k)를 획득하며 첨단 창상치료 시장으로 제품군을 확장했다. | 공식홈페이지 | 🔴하 | [Regenity 공식 블로그 (fibrillar collagen wound dressing)](https://regenity.com/blog/collagen-matrix-inc-announces-510k-clearance-for-fibrillar-collagen-wound-dressing-expanding-offerings-for-advanced-wound-market/) |
| EV-RGN-007 | IP·특허 | Collagen Matrix, Inc. 명의로 가교(cross-linked) 생체고분자 섬유로 형성된 self-curling·re-rollable 콜라겐 막 특허 등이 등록되어 있으며, 회사는 100건 이상의 특허를 보유한다고 밝힌다. | 특허 | 🟠중 | [Justia Patents (Collagen Matrix Inc 양수인 검색)](https://patents.justia.com/assignee/collagen-matrix-inc) |
| EV-RGN-008 | IP·특허 | 콜라겐 가교 분야에서는 리보스 등 환원당(sugar) 가교가 글루타르알데히드 대안으로 알려져 있으며(US6682760B2 등), Collagen Matrix 계열 초기 특허(US5567806)도 화학 가교제 기반 서서히-흡수되는 봉합가능 콜라겐 막을 다룬다. | 특허 | 🟠중 | [Google Patents US6682760B2 / Justia US5567806](https://patents.google.com/patent/US6682760B2/en) |
| EV-RGN-009 | 파트너십·M&A | 2026년 2월 Cinven이 기존 투자자 Linden Capital Partners와 함께 Regenity에 전략적 투자를 단행해 파트너십을 구성했다(금액 비공개). | 주요언론 | 🟠중 | [Linden Capital Partners / Cinven 공식 보도](https://www.linden.com/news/2026/02/regenity-biosciences-receives-strategic-investment-from-cinven-adding-new-partner-alongside-linden-capital-partners/) |
| EV-RGN-010 | 파트너십·M&A | 2022년 Collagen Matrix는 네덜란드 합성 생분해성 폴리머 기기 기업 Polyganics를 인수하여 신경재생·경막 봉합 등 합성폴리머 플랫폼을 확보했고, 이것이 Regenity 리브랜딩의 계기가 되었다. | 주요언론 | 🟠중 | [PR Newswire (Collagen Matrix Acquires Polyganics)](https://www.prnewswire.com/news-releases/collagen-matrix-acquires-polyganics-301640830.html) |
| EV-RGN-011 | 파트너십·M&A | 2019년 8월 시카고 기반 헬스케어 사모펀드 Linden Capital Partners가 Collagen Matrix, Inc.를 인수했다. | 주요언론 | 🟠중 | [Linden Capital Partners 공식 뉴스](https://www.linden.com/news/2019/08/linden-acquires-collagen-matrix/) |

### Rousselot (Darling Ingredients Inc. 브랜드)

연관 판정 — **mTG**: 인접·응용/중 · **ADC**: 무관/하 · **Collagen**: 직접사업/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-ROU-001 | 사업분야 | Rousselot은 Darling Ingredients의 콜라겐·젤라틴 브랜드로, 소·돼지·어류 유래 수백 종의 젤라틴/콜라겐 제품을 4개 대륙 17개 생산시설에서 공급하는 세계적 공급사다. | 공식홈페이지 | 🟢상 | [Darling Ingredients 공식 (Rousselot)](https://www.darlingii.com/rousselot) |
| EV-ROU-002 | 사업분야 | Darling Ingredients는 세계 콜라겐(젤라틴+가수분해 콜라겐)의 약 30%를 생산하는 최대급 생산사이며, Rousselot이 그 헬스 브랜드다. | 주요언론 | 🟠중 | [PR Newswire / Nutrition Insight (Darling-Tessenderlo)](https://www.nutritioninsight.com/news/rousselot-pb-leiner-darling-ingredients-tessenderlo.html) |
| EV-ROU-003 | 사업분야 | Rousselot은 Health & Nutrition, Biomedical, Functional Ingredients 3개 사업 부문으로 구성되며, Peptan은 세계 선도 콜라겐 펩타이드 브랜드다. | 공식홈페이지 | 🟢상 | [Darling Ingredients 공식 (Peptan / 제품)](https://www.darlingii.com/rousselot/brands/peptan) |
| EV-ROU-004 | 연구분야 | Rousselot Biomedical은 세계 최초로 GMP 조건에서 생산된 gelatin methacryloyl(X-Pure GelMA)을 개발했으며, 3D 바이오프린팅·조직공학·재생의학용 초순수 젤라틴/콜라겐 소재군을 보유한다. | 주요언론 | 🟠중 | [PR Newswire (Rousselot Biomedical GMP GelMA)](https://www.prnewswire.com/news-releases/rousselot-biomedical-darling-ingredients-brand-announces-the-worlds-first-gelma-produced-under-gmp-301525367.html) |
| EV-ROU-005 | 연구분야 | Rousselot Biomedical은 페놀(desaminotyrosine) 기능화 젤라틴 X-Pure GelDAT를 출시했으며, 효소 반응 또는 광유도로 가교 가능해 조직 접착·창상 드레싱 응용을 겨냥한다. | 주요언론 | 🟠중 | [BioSpace (X-Pure GelDAT 출시)](https://www.biospace.com/rousselot-biomedical-launches-x-pure-geldat-first-ever-purified-and-phenol-functionalized-gelatin) |
| EV-ROU-006 | 연구분야 | Rousselot은 GLP-1/GIP 분비 자극과 식후 혈당 조절을 타깃하는 특정 콜라겐 펩타이드 조성물 Nextida GC를 임상·전임상 근거와 함께 개발했다. | 주요언론 | 🟠중 | [Nutrition Insight (Nextida GC 대사건강)](https://www.nutritioninsight.com/news/nextida-gc-collagen-peptides-metabolic-health.html) |
| EV-ROU-012 | 연구분야 | Rousselot 공식 자료는 젤라틴과 콜라겐을 조직공학·3D 바이오프린팅용 천연 바이오소재로 규정하며 GelMA 등 개질 젤라틴 포트폴리오를 제시한다. | 공식홈페이지 | 🟢상 | [Rousselot Biomedical 공식 (Collagens)](https://www.rousselot.com/biomedical/products/biomedical-gelatins/collagens) |
| EV-ROU-007 | 뉴스·동향 | Rousselot은 2025년 Vitafoods Europe, SupplySide Global, Food Ingredients Europe 등에서 Nextida GC 콜라겐 펩타이드를 대사·혈당 건강 솔루션으로 집중 전시했다. | 주요언론 | 🟠중 | [Nutrition Insight (FiE 2025)](https://www.nutritioninsight.com/news/fie-2025-rousselot-collagen-glp-1-nextidagc.html) |
| EV-ROU-008 | 뉴스·동향 | 복수의 연구가 Rousselot X-Pure 젤라틴/GelMA를 미생물 트랜스글루타미나제(mTG)로 가교하여 3D 프린팅용 레올로지 특성 조절·기계강도 향상(최대 7배)을 시연했다. | 논문 | 🟠중 | [IOPscience Biofabrication (mTG-induced GelMA crosslinking)](https://iopscience.iop.org/article/10.1088/1758-5090/ab063f) |
| EV-ROU-009 | IP·특허 | Rousselot(Darling) 계열의 특허 WO2021233981A1은 저(低)엔도톡신 gelatin-(meth)acryloyl(리포다당 <100 EU/g, 최저 <1 EU/g)을 청구하며, 이는 X-Pure GelMA의 2단계 정제기술과 연계된다. | 특허 | 🟠중 | [Google Patents WO2021233981A1](https://patents.google.com/patent/WO2021233981A1/en) |
| EV-ROU-010 | 파트너십·M&A | Rousselot Biomedical은 xolo(볼류메트릭 3D프린팅)와 2024년 코브랜딩 협약으로 X-Pure GelMA를 xolo 바이오잉크에 통합했고, Gelomics·BIO INX와도 X-Pure GelMA 기반 협업을 맺었다. | 주요언론 | 🟠중 | [Sciad / VoxelMatters (Rousselot-xolo 협약)](https://businessofbiofabrication.com/2024/09/28/xolo-partners-with-rousselot-to-enhance-volumetric-bioprinting-with-x-pure-gelma/) |
| EV-ROU-011 | 파트너십·M&A | Darling Ingredients는 브라질 젤라틴·콜라겐 생산사 Gelnex를 인수했고, Tessenderlo Group과 초기 연매출 약 15억 달러·연 20만 톤 규모의 콜라겐/젤라틴 합작(85:15, 2026년 종결 예정)을 추진 중이다. | 주요언론 | 🟠중 | [FoodBev / PR Newswire (Gelnex, Tessenderlo JV)](https://www.foodbev.com/news/darling-ingredients-and-tessenderlo-group-to-launch-joint-venture-in-collagen-sector) |

### Smith+Nephew plc — Advanced Wound Management

연관 판정 — **mTG**: 무관/하 · **ADC**: 무관/하 · **Collagen**: 직접사업/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-SNP-001 | 사업분야 | Smith+Nephew의 Advanced Wound Management(AWM) 사업부는 급성·만성 창상(하지·당뇨·압박 궤양, 화상, 수술후 창상)용 첨단 창상관리 제품 포트폴리오를 공급한다. | 공식홈페이지 | 🟢상 | [Smith+Nephew 공식 홈페이지 (Wound Care)](https://www.smith-nephew.com/en/health-care-professionals/products/wound-care) |
| EV-SNP-002 | 사업분야 | S+N의 SANTYL은 콜라게나제(collagenase) 연고로, 만성 피부궤양·심한 화상의 효소적 변연절제(debridement)에 쓰이는 미국 FDA 승인 처방 바이오로직 제품이다. | 공식홈페이지 | 🟢상 | [Smith+Nephew 공식 홈페이지 (SANTYL)](https://www.smith-nephew.com/en-us/patients/products/advanced-wound-management/santyl) |
| EV-SNP-003 | 사업분야 | S+N의 BIOSTEP는 콜라겐 매트릭스 드레싱으로, 과잉 MMP(단백분해효소)를 표적·불활성화해 만성 창상 폐쇄를 촉진하며, 은(Ag) 함유 항균 버전(BIOSTEP Ag)도 있다. | 업계리포트 | 🟠중 | [WoundSource — BIOSTEP Collagen Matrix](https://www.woundsource.com/product/biostep-ag-collagen-matrix-dressing-silver) |
| EV-SNP-004 | 사업분야 | S+N의 OASIS Matrix 제품군은 돼지 소장점막하조직(SIS) 유래 세포외기질(ECM) 창상 매트릭스로, 콜라겐·엘라스틴·GAG·성장인자를 함유해 창상 재상피화·재혈관화 스캐폴드로 기능한다. | 공식홈페이지 | 🟢상 | [Smith+Nephew 공식 홈페이지 (OASIS Matrix) / PMC SIS review](https://www.smith-nephew.com/en-us/health-care-professionals/products/advanced-wound-management/oasis-us-only) |
| EV-SNP-013 | 사업분야 | Smith+Nephew는 Watford(영국)에 본사를 둔 영국 다국적 의료기기 기업으로, Advanced Wound Management를 3대 사업부(정형외과·스포츠의학/ENT·창상관리) 중 하나로 운영한다. | 공식홈페이지 | 🟢상 | [Smith+Nephew 공식 홈페이지 (Business Units) / Wikipedia](https://www.smith-nephew.com/en/who-we-are/our-business-units) |
| EV-SNP-005 | 연구분야 | S+N의 REGENETEN 생유도성(bioinductive) 임플란트는 흡수성 정제 소(bovine) 콜라겐 임플란트로, 자연 창상치유 과정을 이용해 새 힘줄유사 조직 성장을 유도하며 약 6개월 내 흡수된다. | 논문 | 🟢상 | [PMC / Smith+Nephew 뉴스 (REGENETEN)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8366148/) |
| EV-SNP-006 | 연구분야 | S+N은 100년 이상 위치한 Hull 부지를 대체할 신규 AWM R&D·제조 시설을 Hull 인근 Melton West에 1억 달러 이상 투자로 건설, 창상관리 R&D 역량을 강화한다. | 공식홈페이지 | 🟢상 | [Smith+Nephew 보도자료 / PR Newswire](https://www.smith-nephew.com/en/news/2022/06/09/20220609-sn-announces-new-uk-rd-and-manufacturing-facility-for-awm-with-$100m-investment-near-hull) |
| EV-SNP-012 | 연구분야 | S+N의 mTG(미생물 트랜스글루타미나제) 사용 또는 ADC(항체-약물 접합체) 파이프라인·접합기술·mTG 공급 접점은 조사에서 전혀 확인되지 않았다. | 기타 | 🟠중 | [웹검색 종합 (honest_gap)](https://pubmed.ncbi.nlm.nih.gov/37586591/) |
| EV-SNP-009 | 뉴스·동향 | S+N FY2025 실적(2026-03-02 발표)에서 Advanced Wound Bioactives는 언더라잉 매출 -0.5% 감소했으나, SANTYL 강세와 피부대체재 성장으로 향후 성장을 전망한다. | IR·공시 | 🟢상 | [Smith+Nephew Q4·FY2025 Results](https://www.smith-nephew.com/en/news/2026/03/02/smith-nephew-fourth-quarter-and-full-year-2025-results) |
| EV-SNP-010 | 뉴스·동향 | 2025년 9월 S+N은 REGENETEN 생유도성 콜라겐 임플란트의 주요 임상근거·환자접근성 업데이트를 발표했고, 전층 회전근개 재파열률을 68% 감소시킨다는 연구가 확인됐다. | 주요언론 | 🟠중 | [Ortho Spine News / Smith+Nephew 뉴스](https://orthospinenews.com/2025/09/11/smithnephew-unveils-major-clinical-evidence-and-patient-access-updates-for-its-regeneten-bioinductive-implant/) |
| EV-SNP-011 | 뉴스·동향 | 2025년 12월 S+N은 'RISE' 전략(Reach·Innovation·Scale·Execute)을 발표하고, 제조망 최적화의 일환으로 Hull 제조를 축소·이관하며 Melton에 신규 창상 시설을 구축 중이다. | IR·공시 | 🟠중 | [Smith+Nephew FY2025 Results / 전략 발표](https://www.smith-nephew.com/en/who-we-are/investors/annual-report-2025) |
| EV-SNP-007 | IP·특허 | 콜라겐+산화재생셀룰로스(ORC) 복합 창상드레싱 기술 특허 패밀리(EP1795210B1, US7833790B2, EP1325754A1)가 존재하며, 인간 재조합 콜라겐(FibroGen 유래, 효모 발현)을 ORC와 결합한다. | 특허 | 🔴하 | [Google Patents (EP1795210B1 / US7833790B2)](https://patents.google.com/patent/EP1795210B1/en) |
| EV-SNP-008 | 파트너십·M&A | S+N은 2019년 4월 재생의학 기업 Osiris Therapeutics를 주당 $19, 총 지분가치 약 6.6억 달러에 인수해 피부대체재(skin substitute)·재생의학 포트폴리오를 창상 사업에 통합했다. | IR·공시 | 🟢상 | [Smith+Nephew 보도자료 / PR Newswire](https://www.smith-nephew.com/en/news/2019/04/17/20190417-sn-completes-acquisition-of-osiris-therapeutics-inc) |

### Steakholder Foods Ltd. (구 MeaTech 3D Ltd.)

연관 판정 — **mTG**: 인접·응용/하 · **ADC**: 무관/하 · **Collagen**: 인접·응용/하

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-STK-001 | 사업분야 | 이스라엘 Rehovot 소재 딥테크 식품기업으로 배양육·대체육 3D 바이오프린팅을 핵심으로 하며 나스닥(STKH, 구 MITC)에 상장돼 있다. | 공식홈페이지 | 🟢상 | [Steakholder Foods 공식 홈페이지 / 다수 언론 종합](https://steakholderfoods.com/3d-printed-meat/) |
| EV-STK-002 | 사업분야 | 사업모델은 3D 바이오프린터와 바이오잉크(및 SH 프리믹스 블렌드)를 식품기업에 공급하는 B2B 구조다. | 주요언론 | 🟠중 | [PR Newswire (Steakholder 3D Bio-printing Business Model)](https://www.prnewswire.com/news-releases/steakholder-foods-unveils-3d-bio-printing-business-model-301834537.html) |
| EV-STK-003 | 사업분야 | 프리미엄 식물성 통살(whole-cut) 브랜드 'Perfecta'를 2026년 하반기 미국 북동부에 단계적 출시할 계획이며 스테이크·치킨브레스트·연어 등 아날로그를 포함한다. | 주요언론 | 🟠중 | [GlobeNewswire / vegconomist](https://www.globenewswire.com/news-release/2026/05/20/3298421/0/en/steakholder-foods-to-launch-perfecta-premium-plant-based-meat-in-the-u-s-market.html) |
| EV-STK-004 | 연구분야 | 배양육 공정은 동물 줄기세포를 근육·지방 세포로 분화시켜 이를 '바이오잉크'로 3D 프린팅한 뒤 인큐베이터에서 조직을 성숙시키는 방식이다. | 주요언론 | 🟠중 | [Inhabitat / 다수 언론 종합](https://inhabitat.com/check-out-the-new-3d-bio-printed-meat-from-steakholder-foods/) |
| EV-STK-005 | 연구분야 | 조리된 생선의 결(flaky) 텍스처는 '가교된(crosslinked) 생선 조직'의 여러 층을 느슨하게 결합해 구현하며, 맞춤형 바이오잉크와 3D프린팅을 결합한다. | 주요언론 | 🟠중 | [SeafoodSource / PR Newswire](https://www.seafoodsource.com/news/plant-based/steakholder-foods-achieves-flaky-texture-in-cell-cultured-fish) |
| EV-STK-006 | 연구분야 | Steakholder는 자사 바이오잉크를 '식물성 원료 + 배양세포의 블렌드'로 공식 설명하며 구체 배합은 비공개 독점이고, 공식 자료·특허 어디에도 콜라겐/젤라틴을 자사 바이오잉크·스캐폴드 원료로 명시한 근거는 확인되지 않는다(콜라겐 접점 약함). | 공식홈페이지 | 🔴하 | [Steakholder Foods 공식 홈페이지(3D Printed Meat) / 자사 특허 종합](https://www.steakholderfoods.com/blog/3d-printed-meat) |
| EV-STK-012 | 뉴스·동향 | 지난 1년간 Bondor Foods가 SH-Fish 프리믹스, Wyler Farm이 SH-Beef 프리믹스 구매주문을 내며 초기 매출 발생을 시작했다. | 주요언론 | 🟠중 | [vegconomist (Perfecta 관련 보도)](https://vegconomist.com/products-launches/steakholder-foods-plans-us-consumer-launch-whole-cut-plant-based-line/) |
| EV-STK-013 | 뉴스·동향 | 2025년 7월 약 250만 달러 공모, 9월 워런트 행사로 약 150만 달러를 조달했으며 여전히 적자 상태(총자산 약 990만 달러)다. | IR·공시 | 🟠중 | [SEC 6-K / Investing.com / Simply Wall St 종합](https://www.sec.gov/Archives/edgar/data/0001828098/000121390025094374/ea025946201ex99-1_steak.htm) |
| EV-STK-007 | IP·특허 | HD144 생선 프린터의 DLS(Drop Location in Space) 드롭온디맨드 인쇄 시스템 국제특허출원(PCT/US24/34252)에 대해 국제조사기관이 21개 청구항 전부 신규성·진보성·산업상 이용가능성을 인정하는 긍정적 견해서를 냈다. | 주요언론 | 🟠중 | [GlobeNewswire / StockTitan](https://www.globenewswire.com/news-release/2025/07/28/3122428/0/en/Steakholder-Foods-Receives-Positive-International-Search-Report-for-Patent-Covering-HD144-Fish-Printer-s-DLS-Based-Drop-on-Demand-Printing-System.html) |
| EV-STK-008 | IP·특허 | 조리 생선 텍스처(가교 조직 다층 구조) 구현에 관한 미국 임시특허출원을 2022년 11월에 제출했다. | 주요언론 | 🟠중 | [PR Newswire](https://www.prnewswire.com/news-releases/steakholder-foods-announces-the-filing-of-provisional-patent-application-to-mimic-the-texture-of-cooked-fish-301679945.html) |
| EV-STK-009 | IP·특허 | 고처리량 식용 3D 구조물 바이오프린팅을 위한 프린트헤드 관련 특허 허여(allowance)를 2023년 7월 통지받았다. | 주요언론 | 🟠중 | [PR Newswire / Asia Food Journal](https://www.prnewswire.com/news-releases/steakholder-foods-receives-patent-allowance-for-revolutionary-print-heads-for-bioprinting-of-edible-3d-structures-at-high-throughput-301888066.html) |
| EV-STK-010 | 파트너십·M&A | 싱가포르 UMAMI Bioworks와 싱가포르-이스라엘 산업R&D(SIIRD) 기금 지원 2년 공동연구로 3D프린팅 배양 생선 필렛의 확장생산 타당성을 확보하고 2024년 11월 상업화 단계로 진입, NAMIC/A*STAR와 연계했다. | 주요언론 | 🟠중 | [GlobeNewswire / Food Engineering](https://www.globenewswire.com/news-release/2024/11/25/2986692/0/en/UMAMI-Bioworks-and-Steakholder-Foods-Join-Forces-to-Scale-3D-Printed-Fish-Fillets-for-Global-Commercialization.html) |
| EV-STK-011 | 파트너십·M&A | 2020년 12월 벨기에 배양 조류지방(cultivated avian fat) 기업 Peace of Meat를 약 1,500만 유로에 인수했으나 2023년 핵심 3D프린팅에 집중하기 위해 운영을 중단·구조조정했다. | 주요언론 | 🟠중 | [vegconomist / MeaTech3D](https://vegconomist.com/company-news/steakholder-foods-closes-peace-of-meat/) |

### Vericel Corporation

연관 판정 — **mTG**: 무관/하 · **ADC**: 무관/하 · **Collagen**: 직접사업/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-VER-001 | 사업분야 | Vericel은 미국에서 세 개 제품(MACI 연골재생, Epicel 배양표피, NexoBrid 화상 가피제거)을 판매하는 세포치료·첨단재생의료 기업이다. | IR·공시 | 🟢상 | [Vericel 2Q2025 실적 보도자료 / SEC 8-K](https://www.sec.gov/Archives/edgar/data/0000887359/000162828025036854/ex991earningsreleaseq22025.htm) |
| EV-VER-002 | 사업분야 | MACI는 자가 배양 연골세포를 흡수성 Type I/III 돼지 콜라겐 멤브레인(collagen membrane)에 시딩한 세포화 스캐폴드 제품으로, 무릎 연골결손 치료에 2016년 FDA 승인을 받았다. | 규제기관 | 🟢상 | [FDA — MACI (autologous cultured chondrocytes on porcine collagen membrane)](https://www.fda.gov/vaccines-blood-biologics/cellular-gene-therapy-products/maci-autologous-cultured-chondrocytes-porcine-collagen-membrane) |
| EV-VER-003 | 사업분야 | MACI가 Vericel 매출의 최대 비중을 차지하며, 2024년 연매출 1억9,730만 달러(+20%), 2025년 2분기 총매출의 약 85%를 기록했다. | IR·공시 | 🟢상 | [Vericel FY2024/2Q2025 실적 보도자료 (SEC 8-K)](https://www.sec.gov/Archives/edgar/data/0000887359/000162828025008444/ex991earningsreleaseq42024.htm) |
| EV-VER-004 | 사업분야 | Vericel의 화상케어 부문은 중증 화상용 영구 피부대체재 Epicel(배양표피 자가이식)과 단백분해효소 기반 가피제거제 NexoBrid로 구성된다. | IR·공시 | 🟢상 | [Vericel 3Q2025 실적 보도자료 (SEC 8-K)](https://www.sec.gov/Archives/edgar/data/0000887359/000162828025049880/ex991earningsreleaseq32025.htm) |
| EV-VER-005 | 연구분야 | MACI Arthro(관절경적 전달용 MACI)가 2024년 8월 FDA 승인을 받아 소절개 관절경 전달이 가능해졌다. | 주요언론 | 🟠중 | [PharmExec — FDA Approves Arthroscopic Delivery of MACI](https://www.pharmexec.com/view/fda-approves-arthroscopic-delivery-vericel-maci-knee-cartilage-defects) |
| EV-VER-006 | 연구분야 | Vericel은 2025년 2분기 발목(talus) 적응증 MACI에 대한 IND 승인을 받고, 4분기에 309명 대상 무작위 대조 MASCOT 임상시험을 개시했다. | IR·공시 | 🟢상 | [Vericel Form 10-K (2026-02-26 제출)](https://investors.vcel.com/static-files/8557f822-a730-415f-bfc9-2e7c24fc2e62) |
| EV-VER-010 | 뉴스·동향 | NexoBrid는 2024년 소아(deep partial/full-thickness 화상) 적응증에 대해 글로벌 3상 CIDS 결과를 근거로 FDA 승인을 받았다. | 주요언론 | 🟠중 | [World Pharmaceuticals — NexoBrid pediatric FDA approval](https://www.worldpharmaceuticals.net/news/vericels-nexobrid-gets-fda-approval-for-children-with-severe-thermal-burns/) |
| EV-VER-007 | IP·특허 | MACI에 쓰이는 ACI-Maix Type I/III 콜라겐 멤브레인은 독일 Matricel GmbH가 제조·공급하며, 멤브레인 소재 기술의 IP는 Matricel 측이 보유한다. | 기타 | 🟠중 | [Matricel GmbH 뉴스 / MedLife e.V.](https://medlife-ev.de/en/matricel-gmbh-unterzeichnet-langfristigen-liefervertrag-mit-vericel-corporation/) |
| EV-VER-011 | IP·특허 | Vericel의 mTG(미생물 트랜스글루타미나제) 또는 ADC(항체-약물 접합체) 관련 파이프라인·특허·공급 접점은 확인되지 않았다. | 기타 | 🟠중 | [웹/USPTO 검색 결과 (honest_gap)](https://www.vcel.com/advanced-therapies/) |
| EV-VER-008 | 파트너십·M&A | Vericel은 2023년 7월 1일 Matricel과 ACI-Maix 콜라겐 멤브레인 장기 독점공급계약을 갱신했으며, 계약은 2030년 12월 31일까지 유효하고 2033년까지 3년 연장 옵션이 있다. | IR·공시 | 🟢상 | [Vericel 2Q2023 실적 보도자료 (GlobeNewswire)](https://www.globenewswire.com/news-release/2023/08/02/2716760/0/en/Vericel-Reports-Second-Quarter-2023-Financial-Results-and-Raises-Full-Year-2023-Financial-Guidance.html) |
| EV-VER-009 | 파트너십·M&A | Vericel은 2019년 5월 MediWound와 NexoBrid 북미 독점 라이선스 계약을 체결(선급금 1,750만 달러+마일스톤 최대 1억5천만 달러)했다. | IR·공시 | 🟢상 | [Vericel 보도자료 — Exclusive License Agreement with MediWound](https://investors.vcel.com/news-releases/news-release-details/vericel-enters-exclusive-license-agreement-mediwound-north) |

### 다나그린 (DaNAgreen Co., Ltd.)

연관 판정 — **mTG**: 인접·응용/하 · **ADC**: 무관/하 · **Collagen**: 인접·응용/중

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-DNG-001 | 사업분야 | 다나그린의 주력 제품은 단백질로 만든 세포외기질(ECM) 유사 다공성 3D 세포지지체 브랜드 'Protinet'이다. | 주요언론 | 🟠중 | [KoreaTechDesk / Green Queen (검색 스니펫 교차)](https://koreatechdesk.com/danagreen-3d-scaffold-to-enable-cultured-meat-mass-production) |
| EV-DNG-002 | 사업분야 | Protinet은 출발물질에 따라 Protinet-S(혈청/자가 인간혈청 기반, 임상용), Protinet-P(대두 식물성 단백질, 식용·배양육용), Protinet-TP(해조류 단백질, 반투명)로 구분된다. | 공식홈페이지 | 🟠중 | [다나그린 소개(넥스트유니콘/코스모진텍 배포 자료, 검색 스니펫)](https://www.nextunicorn.kr/company/2567df96b1e279e6) |
| EV-DNG-003 | 사업분야 | 핵심기술은 혈청 등에 존재하는 단백질을 고농도로 농축·구조변형(reformed protein)한 뒤 특허받은 교차결합(crosslinking) 기술로 다공성 지지체를 제조하는 것이다. | 주요언론 | 🟠중 | [넥스트유니콘 기업정보 / 한국경제 인터뷰(검색 스니펫)](https://www.nextunicorn.kr/company/2567df96b1e279e6) |
| EV-DNG-004 | 사업분야 | 다나그린은 2017년 서울에서 김기우 대표와 주승연 CTO(부부)가 설립했으며, 지지체는 3차원 세포배양·조직공학·약물스크리닝·배양육에 응용된다. | 주요언론 | 🟠중 | [한국경제(2019) / Green Queen(검색 스니펫 교차)](https://www.hankyung.com/article/2019080797601) |
| EV-DNG-005 | 연구분야 | 다나그린은 심장·간 유사체(미니장기)를 개발해 동물실험을 대체하는 세포독성시험·신약개발 플랫폼을 목표로 하며, 세포독성시험 시장을 1차 타깃으로 한다. | 주요언론 | 🟠중 | [한국경제 '김기우 대표 유사장기 세포배양체 독성시험'(검색 스니펫)](https://www.hankyung.com/article/2019080797601) |
| EV-DNG-006 | 연구분야 | 다나그린은 소·닭·돼지에서 추출한 근육세포와 주변세포를 식물성 단백질 3D 식용 스캐폴드 안에서 배양·분화시키는 하이브리드 방식 배양육을 개발한다. | 주요언론 | 🟠중 | [전자신문 '3차원 지지체 원천기술 활용 배양육 개발'(검색 스니펫)](https://www.etnews.com/20200522000119) |
| EV-DNG-007 | 뉴스·동향 | 다나그린은 어류 배양육을 개발 중이며 규제가 명확한 싱가포르를 교두보로 2026년 싱가포르 식품청(SFA) 최종 승인 및 글로벌 상용화를 목표로 한다. | 주요언론 | 🟠중 | [서울신문](https://www.seoul.co.kr/news/economy/2025/09/19/20250919500016) |
| EV-DNG-008 | 뉴스·동향 | 서울 가산디지털단지 파일럿플랜트 '다나그린혁신센터'는 2024년 HACCP·ISO 22000 인증을 취득했고, 배치당 생산량을 2kg에서 2026년 20kg으로 확대하고 단가를 kg당 1만7천원으로 낮출 계획이다. | 주요언론 | 🟠중 | [서울신문](https://www.seoul.co.kr/news/economy/2025/09/19/20250919500016) |
| EV-DNG-010 | IP·특허 | 다나그린의 세포지지체는 특허받은 단백질 교차결합 기술에 기반하며, 관련 국내 공개특허(공개번호 10-2021-0014705)가 확인된다. | 특허 | 🔴하 | [KIPRIS/Google Patents 특허공보 PDF(KR20210014705A)](https://patentimages.storage.googleapis.com/1b/b9/fe/7b8da22f7b2914/KR20210014705A.pdf) |
| EV-DNG-011 | IP·특허 | 단백질 스캐폴드 분야에서 미생물 트랜스글루타미나제(mTG)로 콜라겐·젤라틴을 가교하는 기술이 확립돼 있으나(예: KR20210062589A, 출원인 Bio-Change Ltd), 이는 다나그린 소유 특허가 아니며 다나그린의 mTG 사용은 공개 확인되지 않는다. | 특허 | 🟠중 | [Google Patents KR20210062589A(Bio-Change Ltd) / mTG-가교 문헌](https://patents.google.com/patent/KR20210062589A/ko) |
| EV-DNG-009 | 파트너십·M&A | 다나그린은 2021년 12월 약 80억원 규모 시리즈A를 유치했고(누적 약 100억원), 롯데벤처스·JW에셋·타임와이즈·패스파인더H·하이투자파트너스 등이 참여했다. | 주요언론 | 🟠중 | [플래텀 / 벤처스퀘어(검색 요약 교차)](https://platum.kr/archives/178349) |
| EV-DNG-012 | 파트너십·M&A | 다나그린은 2024년 경상북도 세포배양산업 육성 업무협약(영남대·포스텍·한국식품연구원 등 28개 산·학·연·관)과 '바이오 미래식품 산업 협의회'(33개사)에 참여했다. | 주요언론 | 🟠중 | [경상북도 보도자료 / 식품음료신문(검색 요약)](https://www.thinkfood.co.kr/news/articleView.html?idxno=100783) |

### 대웅제약 (Daewoong Pharmaceutical Co., Ltd.)

연관 판정 — **mTG**: 무관/하 · **ADC**: 인접·응용/중 · **Collagen**: 인접·응용/하

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-DWG-001 | 사업분야 | 대웅제약의 핵심 성장 품목은 보툴리눔 톡신 '나보타'로, 2024년 매출 약 1864억원(전년비 27% 성장)이며 수출 비중이 약 84%에 달한다. | 주요언론 | 🟠중 | [메디파나뉴스 / 아주경제](https://www.ajunews.com/view/20260523170758956) |
| EV-DWG-002 | 사업분야 | 대웅제약은 2024년 개별기준 매출 약 1조2654억원, 영업이익 약 1638억원(전년비 23% 증가)으로 창사 이래 최대 실적을 기록했다. | IR·공시 | 🟢상 | [메디게이트뉴스 / KRX 사업보고서](https://kind.krx.co.kr/common/disclsviewer.do?method=search&acptno=20260318002184) |
| EV-DWG-003 | 사업분야 | 대웅제약은 나보타(톡신)·펙수클루(P-CAB 위식도역류질환)·엔블로(SGLT-2 당뇨) 3대 신약을 2030년까지 각 1조원으로 키우는 '1품 1조' 비전을 제시한 종합제약사다. | 주요언론 | 🟠중 | [메디컬투데이 / 청년일보](https://mdtoday.co.kr/news/view/1065592463728177) |
| EV-DWG-004 | 사업분야 | 대웅제약은 유전자재조합 상피세포성장인자(EGF) 기반 창상치료제 '이지에프 외용액/새살연고'를 보유하며, 이 제품은 섬유아세포의 콜라겐 합성을 촉진해 상처를 치유한다. | 공식홈페이지 | 🟢상 | [대웅홀딩스 제품페이지 / 메디컬헤럴드](https://www.daewoongholdings.com/daewoongkr/popup/product_goods_view_popup.web?srno=377&sCate=2) |
| EV-DWG-005 | 연구분야 | 대웅제약은 AI 신약개발 플랫폼 'DAISY', NK세포치료제, 줄기세포·유전자·엑소좀 등 첨단재생의료와 세포치료제 CDMO(용인바이오센터, 첨단바이오의약품 제조업 허가)를 R&D 축으로 삼는다. | 주요언론 | 🟠중 | [스트레이트뉴스 / 데일리팜](https://www.straightnews.co.kr/news/articleView.html?idxno=274303) |
| EV-DWG-006 | 연구분야 | 그룹 내 R&D 분담상 대웅제약은 합성신약(자가면역·섬유증·당뇨·뇌신경) 중심이고, 자회사 한올바이오파마가 바이오 기반 자가면역·항암(항체) 연구를 담당한다. | 주요언론 | 🟠중 | [the bell](https://www.thebell.co.kr/free/content/ArticleView.asp?key=202406271755015640101720) |
| EV-DWG-007 | 연구분야 | 대웅제약 자회사 한올바이오파마는 항-FcRn 항체 batoclimab(HL161)·HL161ANS(IMVT-1402) 등 자가면역 항체 파이프라인을 임상 3/2상으로 개발하는 항체 개발 역량을 보유한다. | 공식홈페이지 | 🟢상 | [HanAll Biopharma / PR Newswire](https://www.prnewswire.com/news-releases/hanall-biopharma-daewoong-pharmaceutical-and-nurron-pharmaceuticals-initiate-first-in-human-phase-1-clinical-study-of-hl192-301954586.html) |
| EV-DWG-008 | 뉴스·동향 | 대웅제약은 2026년 5월 미국 턴바이오테크놀로지스의 mRNA 기반 후성유전체 역노화 플랫폼 'ERA'의 IP·자산 일체를 경매로 인수해 노화질환 치료제 개발에 착수했다. | 주요언론 | 🟠중 | [머니투데이 더바이오 / 서울경제](https://www.mt.co.kr/thebio/2026/05/21/2026052109451650373) |
| EV-DWG-009 | 뉴스·동향 | 나보타는 2025년에만 브라질(약 1800억원 갱신)·태국(약 738억원)·콜롬비아·쿠웨이트 등 10여개국에서 파트너십·수출 계약을 체결하며 글로벌 확장을 지속했다. | 주요언론 | 🟠중 | [파이낸셜뉴스](https://www.fnnews.com/news/202511201352383414) |
| EV-DWG-010 | IP·특허 | 대웅제약은 1992년부터 EGF를 연구해 2001년 세계 최초로 유전자재조합 EGF 의약품을 식약처 승인받았고, EGF는 세계 최초 WHO 국제일반명(INN)을 획득했다. | 주요언론 | 🟠중 | [메디컬헤럴드 / 대웅홀딩스](http://www.mediherald.com/news/articleView.html?idxno=46230) |
| EV-DWG-014 | IP·특허 | 콜라겐/젤라틴을 트랜스글루타미나제로 가교하는 조직수복 스캐폴드 특허(KR20210062589A)는 이스라엘 Bio-Change Ltd 출원으로, 대웅제약과 무관함을 확인했다(오귀속 방지). | 특허 | 🟢상 | [Google Patents](https://patents.google.com/patent/KR20210062589A/ko) |
| EV-DWG-011 | 파트너십·M&A | 대웅제약 자회사 한올바이오파마는 2024년 6월 미국 Crystal Bioscience와 총 2090만달러 규모 항체 디스커버리 플랫폼 도입·서비스 계약을 체결하고, 차세대 ADC(항체-약물접합체) 항암제 시장 진출을 위해 항체디스커버리팀을 신설했다. | 주요언론 | 🟠중 | [the bell / 더바이오](https://www.thebell.co.kr/free/content/ArticleView.asp?key=202406271755015640101720) |
| EV-DWG-012 | 파트너십·M&A | 나보타는 미국에서 파트너사 Evolus를 통해 'Jeuveau(주보)'로 판매되며, 대웅제약은 전환사채 보통주 전환·추가 2550만달러 투입 등으로 Evolus와 파트너십을 강화했다. | 주요언론 | 🟠중 | [메디게이트뉴스](https://www.medigatenews.com/news/3187517498) |
| EV-DWG-013 | 파트너십·M&A | 대웅제약은 2015년 약 1046억원으로 한올바이오파마 지분 약 30%를 확보해 최대주주가 된 지배관계로, 한올의 항체·역노화·항암 R&D가 대웅 그룹 전략에 편입돼 있다. | 주요언론 | 🟠중 | [바이오스펙테이터](http://www.biospectator.com/view/news_view.php?varAtcId=2957) |

### 로킷헬스케어 (ROKIT Healthcare, Inc.)

연관 판정 — **mTG**: 무관/하 · **ADC**: 무관/하 · **Collagen**: 인접·응용/중

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-ROK-001 | 사업분야 | 로킷헬스케어는 2012년 설립(대표 유석환)된 AI 기반 4D 바이오프린팅·장기재생 플랫폼 기업으로 2025년 5월 12일 코스닥(376900)에 상장했다. | 주요언론 | 🟠중 | [아시아타임 (IPO 기사) / 위키백과](https://www.asiatime.co.kr/article/20250421500174) |
| EV-ROK-002 | 사업분야 | 주력 제품은 Dr. INVIVO 4D 바이오프린터로, 환자 자가 지방에서 추출한 세포외기질(ECM) 바이오잉크로 당뇨족부궤양 맞춤형 진피 패치를 제작하는 재생 치료 플랫폼이다. | 주요언론 | 🟠중 | [3DPrint.com (Rokit diabetic foot ulcer)](https://3dprint.com/269464/bioprinted-skin-patches-for-diabetic-foot-ulcers-commercialized-by-rokit-healthcare/) |
| EV-ROK-003 | 사업분야 | Dr. INVIVO 기반 당뇨족부궤양 치료 키트가 美 FDA 의료기기로 등록되었고, EMA로부터 궤양·욕창·흉터·화상 치료용 non-ATMP 승인을 받았다. | 주요언론 | 🟠중 | [3DPrint.com (FDA medical device) / Nexus Scientific](https://3dprint.com/281717/rokit-healthcares-bioprinting-based-diabetic-foot-treatment-kit-registered-as-a-u-s-fda-medical-device/) |
| EV-ROK-004 | 연구분야 | AI 기반 3D 바이오프린팅 연골 재생 플랫폼은 4년 추적 임상에서 진성 초자연골(hyaline cartilage) 재생을 확인했으며, 해당 재생 산물은 콜라겐 등 조직재생 핵심 성분이 풍부하다. | 주요언론 | 🟠중 | [Seoul Economic Daily (cartilage 4-year data) / ORP Cartilage](https://en.sedaily.com/news/2026/06/01/rokit-healthcare-unveils-4-year-cartilage-regeneration-data) |
| EV-ROK-005 | 연구분야 | 핵심 바이오잉크는 환자 자가 지방 유래 탈세포 세포외기질(MA-ECM)로, 콜라겐을 비롯한 수백종 단백질·성장인자를 함유한 콜라겐 리치 매트릭스이며 피부 재생 바이오잉크로 응용된다. | 주요언론 | 🟠중 | [Seoulz / KoreaBiomed (skin regeneration)](https://www.koreabiomed.com/news/articleView.html?idxno=29290) |
| EV-ROK-006 | 연구분야 | 장기재생 플랫폼(ORP) 파이프라인은 피부·연골에서 모발·망막·신장·심장 패치 재생 등으로 확장 중이며, 4D 바이오프린팅과 자가세포·인체유래 바이오잉크를 공통 기반으로 한다. | 주요언론 | 🟠중 | [3DPrint.com (ROKIT Healthcare Zone) / MD투데이(신장 특허)](https://www.mdtoday.co.kr/news/view/1065588703292570) |
| EV-ROK-013 | 연구분야 | 로킷 자체 파이프라인·특허·언론에서 미생물 트랜스글루타미나제(mTG) 효소 가교나 항체-약물 접합체(ADC) 항암 모달리티와의 접점은 확인되지 않았다(가교는 물리적 냉각·자가 ECM 방식). | 기타 | 🔴하 | [복합 검색(Google/언론) — Rokit + transglutaminase / ADC](https://patents.google.com/patent/US20080305517A1/en) |
| EV-ROK-007 | 뉴스·동향 | 2025년 국내에서 AI 당뇨발 재생 혁신의료기술 규제 승인을 받아 11개 주요 병원에서 임상을 진행, 2026 상반기 임상 완료·하반기 병원 전면 도입을 계획한다. | 주요언론 | 🟠중 | [히트뉴스 (11개 병원 AI 당뇨발 임상)](https://www.hitnews.co.kr/news/articleView.html?idxno=72047) |
| EV-ROK-008 | 뉴스·동향 | 2025년 10월 당뇨족부궤양 재생치료 플랫폼이 美 주요 상급병원 공보험 청구 대상으로 인정받아 미국 공보험 체계 내 공식 시술로 첫 진입했다. | 주요언론 | 🟠중 | [딜사이트 (로킷헬스케어 톺아보기)](https://dealsite.co.kr/articles/153002) |
| EV-ROK-009 | 뉴스·동향 | 2026년 5월 자가지방 미세화 후 물리적 냉각(동결·고형화) 공정으로 조직재생 패치를 제조하는 'Method of Manufacturing a Tissue Regeneration Patch' 美 특허 등록이 결정됐다. | 주요언론 | 🟠중 | [더바이오 (물리적 냉각 공정 美 특허)](https://www.thebionews.net/news/articleView.html?idxno=24794) |
| EV-ROK-010 | IP·특허 | 신장 재생 기술 관련 美 특허를 획득했고, 복합 장기 3D 바이오프린터 기술도 美 특허 등록이 결정되는 등 장기재생 IP를 다국적으로 확보 중이다. | 주요언론 | 🟠중 | [MD투데이 / 더바이오 (복합장기 바이오프린터 특허)](https://www.thebionews.net/news/articleView.html?idxno=16807) |
| EV-ROK-011 | IP·특허 | 2025년 11월 '바이오 소재 동결·고형화 방식 기반 바이오프린터' 원천 특허를 중국에 등록해 중국 시장 진입 기술 기반을 확보했다. | 주요언론 | 🟠중 | [딜사이트 / 인베스팅닷컴](https://dealsite.co.kr/articles/153002) |
| EV-ROK-012 | 파트너십·M&A | IPO 이전 Series A~프리IPO에서 RCPS·CPS·CB 등으로 약 500억원을 조달했고, 코스닥 상장 2개월 뒤 300억원 규모 CB를 발행했으며, 자회사 ROKIT America는 NMN 항노화 보충제·재생플랫폼으로 나스닥 IPO를 신청했다. | 주요언론 | 🟠중 | [딜사이트 / TradingView (ROKIT America NASDAQ)](https://www.tradingview.com/news/tradingview:ed4448d6660a3:0-rokit-america-anti-aging-supplements-and-ai-driven-regenerative-platform-files-for-nasdaq-ipo/) |

### 셀론텍 (Cellontech, 구 세원셀론텍)

연관 판정 — **mTG**: 무관/하 · **ADC**: 무관/하 · **Collagen**: 직접사업/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-CLT-001 | 사업분야 | 셀론텍은 독자 개발한 바이오콜라겐(아텔로콜라겐) 소재를 핵심으로 하는 콜라겐 기반 재생의료 전문기업이다. | 공식홈페이지 | 🟠중 | [셀론텍 공식 홈페이지 (회사개요)](http://cellontech.com/aboutus/outline.php) |
| EV-CLT-002 | 사업분야 | 셀론텍은 2001년 국내 최초 세포치료제인 자가연골세포치료제 '콘드론(Chondron)'을 개발·상용화했다(세계 2번째). | 공식홈페이지 | 🟢상 | [셀론텍 공식 홈페이지 / 연혁](https://www.cellontech.com/aboutus/history.php) |
| EV-CLT-003 | 사업분야 | 제품 포트폴리오는 세포치료제 2종(콘드론, RMS Ossron), 제대혈보관(베이비셀), 바이오콜라겐 원료 기반 리젠그라프트 10종 등 총 12개 재생의료 제품으로 구성된다. | 공식홈페이지 | 🟢상 | [셀론텍 공식 홈페이지 / R&D 연구분야](https://www.cellontech.com/rnd/part.php) |
| EV-CLT-004 | 사업분야 | '카티졸(CartiZol)'은 항원성을 제거한 아텔로콜라겐을 관절강내 주입해 관절기능을 개선하는 국내 최초 콜라겐 관절강주사(흡수성 콜라겐 재료)이다. | 주요언론 | 🟠중 | [헬스경향/hnews (세원셀론텍 카티졸·리젠씰 시판허가)](https://www.hnews.kr/news/view.php?no=14664) |
| EV-CLT-005 | 사업분야 | '리젠씰'은 바이오콜라겐을 이식해 손상된 힘줄·인대 등 연부조직을 보충하는 콜라겐사용 조직보충재이다. | 주요언론 | 🟠중 | [헬스경향/hnews](https://www.hnews.kr/news/view.php?no=14664) |
| EV-CLT-006 | 사업분야 | 셀론텍은 바이오콜라겐 기반 안면 성형필러 '테라필(TheraFill)'과 '루시젠(LUCIZEN)'을 개발, 국내 최초 콜라겐 필러 국산화·상용화에 성공했다. | 주요언론 | 🟠중 | [팜뉴스 (셀론텍 콜라겐 필러 2종 태국 진출)](https://www.pharmnews.com/news/articleView.html?idxno=246029) |
| EV-CLT-007 | 연구분야 | 셀론텍은 '세포'와 '생체재료(바이오콜라겐)' 기반 재생의료시스템(RMS)을 핵심 플랫폼으로 골관절염·연골·뼈·연부조직·피부 재생 및 미용, 혈액·면역질환 분야를 연구한다. | 공식홈페이지 | 🟢상 | [셀론텍 공식 홈페이지 / R&D 연구분야](https://www.cellontech.com/rnd/part.php) |
| EV-CLT-008 | 연구분야 | 셀론텍의 바이오콜라겐은 미국 FDA 원료의약품집(DMF)에 등재된 의료용 콜라겐 원료로, 텔로펩타이드를 제거해 면역원성을 낮춘 아텔로콜라겐 제조 원천기술에 기반한다. | 주요언론 | 🟠중 | [이투데이 (이브이첨단소재 셀론텍 인수)](https://www.etoday.co.kr/news/view/2424127) |
| EV-CLT-015 | 연구분야 | 셀론텍의 콜라겐 응용은 창상피복재, 피부·뼈·각막 등 인체조직 이식재, 세포배양 지지체(스캐폴드), 화장품(마스크팩) 등 재생의료 전반으로 확장된다. | 주요언론 | 🟠중 | [메디파나뉴스 (세원셀론텍 바이오콜라겐 유럽 특허)](http://m.medipana.com/index_sub.asp?NewsNum=258780) |
| EV-CLT-016 | 연구분야 | 셀론텍은 자가 조직·콜라겐 기반 재생의료에 집중하며, 항체-약물 접합체(ADC) 파이프라인이나 mTG(미생물 트랜스글루타미나제) 효소 가교 기술을 사업·연구영역으로 표방한 근거는 확인되지 않는다. | 기타 | 🔴하 | [복합 검색(셀론텍 관련 국문·영문 웹검색)](http://cellontech.com/rnd/tech.php) |
| EV-CLT-009 | 뉴스·동향 | 셀론텍은 2024년 중국 사환제약과 약 550억원 규모 최소주문수량(MOQ) 공급계약을 체결하는 등 최근 1년간 3개국 6개사와 총 약 1200억원 규모 공급계약을 확보했다. | 주요언론 | 🟠중 | [바이오타임즈](https://www.biotimes.co.kr/news/articleView.html?idxno=16396) |
| EV-CLT-010 | 뉴스·동향 | 셀론텍은 콜라겐 수요 대응을 위해 연면적 약 1만6670㎡ 신공장을 건설해 생산능력을 기존 대비 5배 이상 확장(2026년 가동 목표)하고 있으며 매출이 급성장 중이다. | 주요언론 | 🟠중 | [파이낸셜포스트 / 팜뉴스](https://www.financialpost.co.kr/news/articleView.html?idxno=224171) |
| EV-CLT-011 | IP·특허 | 세원셀론텍은 고농도 의료용 바이오콜라겐 제조·제품화 원천기술로 유럽 특허를 등록했고, 미국·중국 등 글로벌 특허권을 선점했다. | 주요언론 | 🟠중 | [아시아경제 / 메디파나뉴스](https://www.asiae.co.kr/article/2020062213522623078) |
| EV-CLT-012 | IP·특허 | 세원셀론텍은 바이오콜라겐 생체접합재로 캐나다 특허를, 재생의료 수출용 RM Kit(연골·뼈세포 배양키트, 제대혈줄기세포 보관키트)로 일본·인도네시아 특허를 등록했다. | 주요언론 | 🟠중 | [데일리메디 / 메디컬타임즈](https://www.dailymedi.com/detail.php?number=856020&thread=22r05) |
| EV-CLT-013 | 파트너십·M&A | 2024년 11월 이브이첨단소재가 SC엔지니어링(에쓰씨엔지니어링) 제12회차 전환사채 250억원을 인수해 자회사 셀론텍을 편입, 재생의료로 사업을 확장했다. | 주요언론 | 🟠중 | [이투데이 / 머니투데이 더벨](https://www.etoday.co.kr/news/view/2424127) |
| EV-CLT-014 | 파트너십·M&A | 셀론텍은 LG화학·동국제약·코오롱제약과 카티졸 공동 마케팅을, 태국 SDX Biotech·코오롱제약과 콜라겐 필러(테라필·루시젠) 태국·베트남 공급계약을 체결했다. | 주요언론 | 🟠중 | [메디파나뉴스 / 이투데이 / 인사이드비나](https://www.medipana.com/medician/view.php?news_idx=327638) |

### 스페이스에프 (Space F Corp.)

연관 판정 — **mTG**: 인접·응용/하 · **ADC**: 무관/하 · **Collagen**: 인접·응용/중

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-SPF-001 | 사업분야 | 스페이스에프는 2020년 4월 설립된 경기 화성(동탄) 소재 세포배양육(배양육) 스타트업으로, 소·돼지·닭 배양육 상용화를 목표로 한다. | 주요언론 | 🟠중 | [글로벌이코노믹](https://www.g-enews.com/article/ICT/2022/01/2022012015534743961aef83fcde_1) |
| EV-SPF-002 | 사업분야 | 주력 제품은 배양돈육·배양우육·배양계육 시제품(소시지/브라트부르스트, 햄버거 패티·미트볼, 너겟·텐더 형태)이며 대표는 김병훈이다. | 주요언론 | 🟠중 | [아시아경제 [스타트人]](https://www.asiae.co.kr/article/2022063010171120855) |
| EV-SPF-003 | 연구분야 | 핵심 기술은 축종별 특화 근육줄기세포 분리·배양, 무혈청 배양액, 가식성 지지체(edible scaffold) 기반 3차원 분화, 대량 배양기 등 4개 축으로 구성된다. | 주요언론 | 🟠중 | [글로벌이코노믹](https://www.g-enews.com/article/ICT/2022/01/2022012015534743961aef83fcde_1) |
| EV-SPF-004 | 연구분야 | 서울대·세종대 연구진과 공동 R&D를 수행하며, 근육줄기세포 분리·배양 관련 특허 및 무혈청 배양액 원천기술을 확보했다고 밝힌다. | 주요언론 | 🟠중 | [벤처스퀘어](https://www.venturesquare.net/836318) |
| EV-SPF-011 | 연구분야 | 배양육 분야 일반에서 콜라겐 기반 식용 지지체를 트랜스글루타미나제(TG)로 가교하는 기법이 학계에 보고되나, 이는 업계 공통 기법이며 스페이스에프의 채택 여부는 확인되지 않는다. | 논문 | 🟠중 | [Korean J Food Sci Anim Resour — Scaffold Biomaterials in the Development of Cultured Meat: A Review](https://pmc.ncbi.nlm.nih.gov/articles/PMC12246907/) |
| EV-SPF-005 | 뉴스·동향 | 산업통상자원부 알키미스트 프로젝트 '아티피셜 에코푸드(배양육)' 분야 본연구에 선정돼 5년간 약 200억원 규모 국책과제를 수행한다. | 주요언론 | 🟠중 | [머니투데이](https://news.mt.co.kr/mtview.php?no=2022050310443761379) |
| EV-SPF-009 | 뉴스·동향 | 김병훈 대표는 파일럿 라인을 약 40% 구축 단계라 밝혔으며 국내 배양육 규제(식약처 세포배양식품 원료 임시기준 등) 정비가 상용화 변수로 남아 있다. | 주요언론 | 🟠중 | [머니투데이 / MFDS](https://www.mt.co.kr/living/2024/03/09/2024030717032931792) |
| EV-SPF-010 | IP·특허 | 스페이스에프를 출원인으로 하는 특허(가식성 지지체 소재·무혈청 배지)를 Google Patents 등에서 특정 번호로 확인하지 못했다(honest_gap). | 특허 | 🔴하 | [Google Patents (검색)](https://patents.google.com/?assignee=Space+F) |
| EV-SPF-006 | 파트너십·M&A | 종합식품기업 대상(Daesang)과 업무협약을 맺고 단가 절감형 가식성 배양액·배양 공정을 공동개발하며 2025년 대량생산·제품출시를 목표로 한다. | 주요언론 | 🟠중 | [식품저널](https://www.foodnews.co.kr/news/articleView.html?idxno=93535) |
| EV-SPF-007 | 파트너십·M&A | 롯데정밀화학과 배양육 생산에 필요한 고기능성 소재를 공동개발 중이다. | 주요언론 | 🟠중 | [바이오타임즈](https://www.biotimes.co.kr/news/articleView.html?idxno=7245) |
| EV-SPF-008 | 파트너십·M&A | 2021년 8월 약 70억원 규모 시리즈A를 유치했으며 투자자에 데일리파트너스, 대상, 롯데벤처스, 타임와이즈인베스트먼트(CJ) 등이 참여했다. | 주요언론 | 🟠중 | [한국경제](https://www.hankyung.com/economy/article/2021082586741) |

### 씨위드 (SeaWith, Inc.)

연관 판정 — **mTG**: 무관/하 · **ADC**: 무관/하 · **Collagen**: 인접·응용/중

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-SEA-001 | 사업분야 | 씨위드는 2019년 DGIST(대구경북과학기술원) 출신이 창업한 대구 소재 배양육 스타트업으로, 자체 브랜드 '웰던(Welldone)'으로 소고기 배양육(미트볼·스테이크 타입)을 개발한다. | 주요언론 | 🟠중 | [에너지경제신문 (K-스타트업의 도약 96)](https://m.ekn.kr/view.php?key=20240804021548018) |
| EV-SEA-002 | 사업분야 | 씨위드의 핵심 사업모델은 해조류 기반 지지체(스캐폴드)와 미세조류 기반 무혈청 배양액을 다른 배양육 기업에 B2B로 공급해 생산단가를 낮추는 것이다. | 주요언론 | 🟠중 | [The Spoon](https://thespoon.tech/south-korea-seawith-uses-algae-for-serum-and-scaffolding-in-cultured-meat/) |
| EV-SEA-003 | 사업분야 | 씨위드는 배양육 외에 저(低)요오드 해조류 가공식품 라인('요드/Yo.od')도 함께 운영한다. | 기타 | 🔴하 | [bizno.net 기업정보 / 전자신문](https://bizno.net/article/2368801246) |
| EV-SEA-004 | 연구분야 | 씨위드의 핵심 기술은 갈조류(미역, Undaria pinnatifida) 유래 알지네이트-셀룰로오스 하이드로겔 지지체 'ACe-gel(Ace-Gel)'로, 소 근육줄기세포(bMuSC)의 3차원 배양·분화 환경을 제공하는 동물유래물질-무함유(animal-free) 스캐폴드다. | 논문 | 🟢상 | [DGIST Scholar / Food Hydrocolloids (Lee et al.)](https://dgist.elsevierpure.com/en/publications/animal-free-scaffold-from-brown-algae-provides-a-three-dimensiona) |
| EV-SEA-005 | 연구분야 | 씨위드는 미세조류를 이용한 무혈청(FBS-free) 세포배양액을 개발해 소태아혈청 사용을 80% 이상 대체하고 배양액 가격을 최대 95% 절감했다고 밝혔다. | 주요언론 | 🟠중 | [에너지경제신문 / The Spoon](https://m.ekn.kr/view.php?key=20240804021548018) |
| EV-SEA-006 | 연구분야 | 씨위드/DGIST 연구진은 ACe-gel 갈조류 스캐폴드가 상용 알지네이트 스캐폴드 대비 세포 부착·증식(72시간 5.5배)에서 우수함을 보인 논문을 Food Hydrocolloids(2024)에 발표했다. | 논문 | 🟠중 | [Food Hydrocolloids (ScienceDirect, S0268005X24002182)](https://www.sciencedirect.com/science/article/pii/S0268005X24002182) |
| EV-SEA-007 | 연구분야 | 씨위드의 스캐폴드는 갈조류 유래 알지네이트-셀룰로오스로 만들어진 명시적 'animal-free' 지지체로, 동물유래 콜라겐/젤라틴 기반 스캐폴드를 대체하는 소재로 개발됐다. | 논문 | 🟠중 | [Food Hydrocolloids 논문 제목 / vegconomist](https://dgist.elsevierpure.com/en/publications/animal-free-scaffold-from-brown-algae-provides-a-three-dimensiona) |
| EV-SEA-008 | 뉴스·동향 | 씨위드는 경북 의성 세포배양식품 규제자유특구에 배양 시설을 짓고, 동물 독성시험·식약처(MFDS) 허가 절차를 거쳐 2027년경 미트볼 형태로 상용화를 추진 중이다. | 주요언론 | 🟠중 | [에너지경제신문 (K-스타트업의 도약 96)](https://m.ekn.kr/view.php?key=20240804021548018) |
| EV-SEA-009 | 뉴스·동향 | 씨위드는 2023년 Plug and Play 실리콘밸리 서밋 참가 등 미국 대기업·투자자와 배양육 투자·협업 논의를 진행했다. | 주요언론 | 🟠중 | [와우테일 (Wowtale)](https://wowtale.net/2023/12/15/68265/) |
| EV-SEA-010 | 뉴스·동향 | 2025년 12월 씨위드는 영국 3D Bio-Tissues와 배양액 첨가제 City-Mix 공급계약(약 £300,000)을 체결해 배양액 사용량 약 30% 절감을 통한 원가 절감을 추진한다. | 주요언론 | 🟠중 | [3D Bio-Tissues / GreenQueen / Investegate](https://www.3dbiotissues.com/post/3d-bio-tissues-partners-with-seawith-to-reduce-cultivated-meat-production-costs) |
| EV-SEA-011 | IP·특허 | 씨위드는 해조류 기반 스캐폴드, 미세조류 기반 세포배양액, 세포배양 리액터 관련 특허 약 5건과 해조류 요오드 저감 관련 특허 2건을 출원·등록했다고 밝힌다. | 기타 | 🔴하 | [HG Initiative / 회사 인터뷰 자료](https://www.hginitiative.com/content_library/2377) |
| EV-SEA-012 | 파트너십·M&A | 씨위드는 배양육 상업생산 규제승인을 받은 싱가포르 Esco Aster와 협력해, 자사 미세조류 기반 저가 스캐폴드·배양액을 활용한 싱가포르 상용화(2024말~2025)를 추진했다. | 주요언론 | 🟠중 | [vegconomist / FoodNavigator-Asia](https://vegconomist.com/cultivated-cell-cultured-biotechnology/seawith-esco-aster-leverage-microalgae-to-accelerate-cultivated-meat-production/) |
| EV-SEA-013 | 파트너십·M&A | 씨위드는 2023년 9월 아이슬란드 ORF Genetics와 식물성(식물 유래) 성장인자 공급 협력을 맺어 한우 배양육의 무혈청 배양 소재를 안정적으로 확보했다. | 주요언론 | 🟠중 | [vegconomist / 전자신문](https://www.etnews.com/20230921000297) |
| EV-SEA-014 | 파트너십·M&A | 씨위드는 BSF Enterprise 자회사 3D Bio-Tissues와 배양액 첨가제 City-Mix(고분자 크라우더) 상업 공급계약을 체결, 웰던 배양우육 개발에 적용한다. | IR·공시 | 🟢상 | [Investegate (BSF Enterprise RNS) / Proteinproductiontechnology](https://www.investegate.co.uk/announcement/rns/bsf-enterprise--bsfa/3d-bio-tissues-signs-supply-agreement-with-seawith/9298698) |
| EV-SEA-015 | 파트너십·M&A | 씨위드는 시리즈A로 약 55억원(2020~2021)에 이어 추가 라운드를 포함 누적 약 75억원(약 US$6.4M)을 유치했으며, 투자자에는 대성PE, DAYLI Partners, HG Initiative, Mint Venture Partners 등이 있다. | 업계리포트 | 🟠중 | [THE VC / Dealroom / 헬로디디](https://thevc.kr/seawith) |

### 엘앤씨바이오 (L&C Bio Co., Ltd., 290650)

연관 판정 — **mTG**: 인접·응용/하 · **ADC**: 무관/하 · **Collagen**: 직접사업/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-LNC-001 | 사업분야 | 엘앤씨바이오의 주력 제품은 기증 인체피부에서 AlloClean 공정으로 제조한 무세포진피(ADM) '메가덤(MegaDerm)'으로, 콜라겐·엘라스틴 등 진피 세포외기질(ECM) 구조를 그대로 보존한 조직재생 이식재다. | 공식홈페이지 | 🟢상 | [L&C Bio 공식 홈페이지 (MegaDerm/MegaDerm Plus 제품)](https://lncbio.co.kr/bbs/board.php?locale=en_US&bo_table=products2_en&wr_id=5) |
| EV-LNC-002 | 사업분야 | 엘앤씨바이오는 2025년 연결기준 매출 855억 원, 영업이익 42억 원(영업이익률 약 5%)으로 흑자전환하며 본업 수익성을 회복했다. | 주요언론 | 🟠중 | [한국경제](https://www.hankyung.com/article/202602270713P) |
| EV-LNC-003 | 사업분야 | ECM 기반 스킨부스터/필러 '엘라비에 리투오(Re2O)'는 인체 무세포동종진피(hADM)에서 유래해 콜라겐·엘라스틴·히알루론산을 직접 보충하는 제품으로, 회사의 핵심 성장 동력이자 수출 확대 축이다. | 주요언론 | 🟠중 | [딜사이트 / 한국경제](https://dealsite.co.kr/articles/149901) |
| EV-LNC-004 | 사업분야 | 제품 포트폴리오는 무세포진피(MegaDerm), 관절연골 치료재(MegaCarti), 미세화 진피 주입재(MegaFill/Esthen), 척추용 골대체재(Bone Spacer·MegaDBM) 등 인체조직 기반 재생 이식재로 구성된다. | 주요언론 | 🟠중 | [더바이오 / L&C Bio 보도자료](https://www.thebionews.net/news/articleView.html?idxno=15160) |
| EV-LNC-005 | 사업분야 | 제약 자회사 엘앤씨메디케어는 정형외과·신경외과 전문의약품(ETC) 유통·판매를 담당하며 100여 개 의약품 허가권과 안성 GMP 제조시설을 보유하나, 취급 품목은 제네릭·전문의약품이고 항체-약물 접합체(ADC) 등 항암 신약 파이프라인은 확인되지 않는다. | 주요언론 | 🟠중 | [서울경제 / 더바이오](https://www.sedaily.com/NewsView/2GSVDJI72N) |
| EV-LNC-006 | 연구분야 | 엘앤씨바이오는 인체 늑연골을 탈세포화해 가교 히알루론산(HA)-카복시메틸셀룰로스(CMC)와 혼합한 탈세포 동종연골 페이스트(DACP)를 개발, 미세골절술 병용 시 토끼 무릎 연골 재생이 향상됨을 보고했다. | 논문 | 🟢상 | [Frontiers in Cell and Developmental Biology (PMC7829663)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7829663/) |
| EV-LNC-007 | 연구분야 | 회사는 인체 유래 무세포진피기질(ADM)을 활용한 신규 생체적합성 열감응성(thermosensitive) 유착방지제 등 ADM/콜라겐 매트릭스의 응용 R&D를 수행하고 있다. | 논문 | 🟠중 | [PMC (조직공학 스캐폴드 연구 문헌)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10898337/) |
| EV-LNC-008 | 연구분야 | 무릎 연골결손 환자 대상 관절연골 치료재 '메가카티(MegaCarti)'의 연골재생 유효성·안전성 평가 임상시험이 진행됐다. | 업계리포트 | 🟠중 | [Synapse (PatSnap) 파이프라인 / 임상 요약](https://synapse.patsnap.com/organization/83cef9d75f3dde71ba4ddcf91a0def8d) |
| EV-LNC-017 | 연구분야 | 엘앤씨바이오의 가교(crosslinking) 기술은 히알루론산-CMC 다당류 가교, E-beam 방사선, 초저온 분쇄 등 물리·화학적 방식에 기반하며, 미생물 트랜스글루타미나제(mTG) 효소 가교의 채택·연구 근거는 다중 검색(국문·영문, transglutaminase/TGase 조합)에서 확인되지 않았다. | 기타 | 🔴하 | [종합 조사 (Google Patents/논문/언론 교차)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7829663/) |
| EV-LNC-012 | 뉴스·동향 | 2026년 회사는 눈가·목주름·흉터 개선용 부위특화 신제품 '리투오 파인(fine)'을 출시하고 리투오 중심 플랫폼 전략을 본격 가동, 리투오 CAPA를 2026년 말 월 8만 개까지 확대할 계획이다. | 주요언론 | 🟠중 | [한국경제](https://www.hankyung.com/article/202605068692P) |
| EV-LNC-013 | 뉴스·동향 | ECM 스킨부스터 '리투오'가 품귀 현상을 빚으며 주가가 상한가를 기록하는 등 시장 수요가 급증했다. | 주요언론 | 🟠중 | [바이오타임즈](https://www.biotimes.co.kr/news/articleView.html?idxno=23874) |
| EV-LNC-009 | IP·특허 | 엘앤씨바이오는 2021년 11월 출원해 2025년 등록한 '초미세 무세포진피 제조 기술' 특허를 보유하며, 초저온 분쇄로 콜라겐 손상 없이 미세바늘 주입이 가능한 크기로 ADM을 제조한다(메가필 하이젝트·에스텐 인젝션 제법 포함). | 주요언론 | 🟠중 | [한국경제 / 더바이오](https://www.hankyung.com/article/202504165056P) |
| EV-LNC-010 | IP·특허 | 엘앤씨바이오는 지방조직 유래 세포외기질(ECM) 관련 특허를 출원하는 등 ECM/콜라겐 소재 IP 포트폴리오를 확장하고 있다. | 주요언론 | 🟠중 | [헬스케어N (헬스조선) / 청년의사(보사)](http://www.bosa.co.kr/news/articleView.html?idxno=2162192) |
| EV-LNC-011 | IP·특허 | 엘앤씨바이오는 2014년 무세포진피기질을 입자화한 뒤 히알루론산을 가교 결합시킨 조성물 특허를 출원하는 등, 가교는 히알루론산·다당류 방식을 채택해 왔다. | 주요언론 | 🟠중 | [한국경제 (특허 관련 보도)](https://www.hankyung.com/article/202504165056P) |
| EV-LNC-014 | 파트너십·M&A | 중국 법인은 메가덤플러스의 NMPA 수입허가를 기반으로 2025년 12월 상하이 제이야라이프와 전략적 제휴를 맺고 23개 판매대리점 계약을 체결하며 현지 유통망을 구축, 2026년 1월 공식 판매를 개시했다. | 주요언론 | 🟠중 | [더벨 (thebell) / 한국경제](https://m.thebell.co.kr/m/newsview.asp?svccode=&newskey=202512100616123920105760) |
| EV-LNC-015 | 파트너십·M&A | 엘앤씨바이오는 2021년 중국 합자법인 L&C China(L&C Bioscience Technology)를 설립하고 2022년 쿤산 7,000평 공장을 준공, 2023년 12월 이를 완전자회사로 전환했다. | 공식홈페이지 | 🟠중 | [L&C Bio 회사소개 / 더벨](http://www.lncbio.co.kr/page/sub_01_01.php) |
| EV-LNC-016 | 파트너십·M&A | 회사는 리투오 상업화 골든타임 확보를 위해 재무적투자자(FI) 유치를 포함한 중국 진출 밸류업 전략을 추진하고 있다. | 주요언론 | 🟠중 | [더벨 (thebell) 밸류업 전략](https://m.thebell.co.kr/m/newsview.asp?svccode=00&newskey=202601290551362260103123) |

### 주식회사 시지바이오 (CGBio)

연관 판정 — **mTG**: 무관/하 · **ADC**: 무관/하 · **Collagen**: 직접사업/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-CGB-001 | 사업분야 | 시지바이오는 골이식재·창상피복재·조직재생 치료재료와 미용·성형(필러) 제품을 개발·제조·판매하는 재생의료 기업이다. | 주요언론 | 🟠중 | [chemknock 기업정보 / 메디포뉴스](https://chemknock.co.kr/chem/cgbio) |
| EV-CGB-002 | 사업분야 | 시지바이오는 콜라겐 유래 흡수성 차폐막(멤브레인) '시지가이드(CG-Gide)'를 제조하며 뉴질랜드산 bovine 콜라겐을 원료로 사용한다. | 주요언론 | 🟠중 | [치의신보 / 데일리덴탈](https://www.dailydental.co.kr/news/article.html?no=112942) |
| EV-CGB-003 | 사업분야 | 시지바이오는 마이크로 콜라겐 섬유(MCF) 공법을 적용한 동종진피 피부이식재 '시지덤(CGDERM)' 계열(원스텝·매트릭스·리알로퍼티)을 유방재건·화상·외상용으로 공급한다. | 주요언론 | 🟠중 | [메디칼타임즈](https://m.medicaltimes.com/News/NewsView.html?ID=1142109) |
| EV-CGB-004 | 사업분야 | 시지바이오는 히알루론산(HA) 필러(지젤리뉴·에일린)와 칼슘(CaHA) 필러 '페이스템' 등 더마 필러 풀라인업을 보유하고 수출한다. | 공식홈페이지 | 🟢상 | [CGBio 공식 홈페이지 / 메디포뉴스](https://www.cgbio.co.kr/22898) |
| EV-CGB-005 | 사업분야 | 시지바이오는 2023년 매출 1,567억 원·영업이익 204억 원의 역대 최대 실적을 기록했으며 골대체재·필러·피부이식재가 성장을 견인했다. | 주요언론 | 🟠중 | [메디칼타임즈 / 메디컬투데이(mdtoday)](https://www.medicaltimes.com/Mobile/News/NewsView.html?ID=1158874) |
| EV-CGB-006 | 연구분야 | 핵심 R&D 플랫폼은 rhBMP-2 골형성 단백질과 자사 서방형 캐리어 기술 'SLOREL', 하이드록시아파타이트/β-TCP 및 poloxamer 407 하이드로겔을 결합한 골대체재 '노보시스'다. | 주요언론 | 🟠중 | [PR Newswire / 더바이오뉴스](https://www.prnewswire.com/news-releases/cgbio-receives-fda-ide-approval-for-novosis-putty-advancing-toward-us-market-entry-302435469.html) |
| EV-CGB-007 | 연구분야 | 노보시스 관련 연구에서 HA/β-TCP 마이크로스피어/하이드로겔 복합체를 콜라겐 스펀지 기반 BMP-2 전달체의 대안으로 제시하며 골재생 효능을 검증했다. | 논문 | 🟠중 | [Scientific Reports (Nature) / PMC](https://www.nature.com/articles/s41598-021-96484-4) |
| EV-CGB-013 | 연구분야 | 시지바이오에서 항체-약물 접합체(ADC) 파이프라인·링커/접합 기술·mTG를 이용한 부위특이적 접합 관련 사업이나 연구는 확인되지 않는다. | 기타 | 🔴하 | [종합 검색(국문·영문)](https://www.cgbio.co.kr/en/product/product_all) |
| EV-CGB-008 | 뉴스·동향 | 노보시스 퍼티가 2025년 4월 미국 FDA IDE(확증임상) 승인을 받아 국산 바이오융복합 의료기기 최초로 미국 척추유합 임상에 진입했다. | 주요언론 | 🟠중 | [PR Newswire / 코리아헤럴드](https://www.koreaherald.com/article/10470138) |
| EV-CGB-010 | IP·특허 | 시지바이오는 rhBMP-2 방출을 정밀 제어하는 독자 서방형 제형 기술 'SLOREL'과 콜라겐 멤브레인 제조 기술을 보유하며, 콜라겐 흡수성 차폐막을 상용화했다. | 주요언론 | 🟠중 | [더바이오뉴스 / 라오션타임스(PR Newswire 인용)](https://www.thebionews.net/news/articleView.html?idxno=24894) |
| EV-CGB-009 | 파트너십·M&A | 자회사 시지메드텍이 2025년 7월 치과부품 제조사 '덴탈오션'을 인수해 디지털 덴티스트리(임플란트+골이식재 노보시스 덴트+콜라겐 멤브레인 시지가이드) 풀라인업을 구축했다. | 주요언론 | 🟠중 | [메디포뉴스 / 데일리팜](https://www.medifonews.com/news/article.html?no=205422) |
| EV-CGB-011 | 파트너십·M&A | 시지바이오는 대웅제약 관계사로, 노보시스 핵심 원료 rhBMP-2를 대웅제약이 대량 생산·공급하는 전략적 파트너십을 유지한다. | 주요언론 | 🟠중 | [AmericanHHM / 더바이오뉴스](https://www.americanhhm.com/technotrends/fda-approves-cgbios-breakthrough-device-novosis-putty) |
| EV-CGB-012 | 파트너십·M&A | 시지바이오는 골대체재 '노보시스'의 미국·캐나다·호주 글로벌 임상 및 독점 사업화 계약을 체결하며 북미 진출을 추진했다. | 주요언론 | 🟠중 | [더바이오뉴스](https://www.thebionews.net/news/articleView.html?idxno=24894) |

### 주식회사 제네웰 (Genewel Co., Ltd.)

연관 판정 — **mTG**: 무관/하 · **ADC**: 무관/하 · **Collagen**: 직접사업/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-GNW-001 | 사업분야 | 제네웰은 동성그룹 헬스케어 핵심 계열사로 2000년 설립되어 습윤드레싱 '메디폼(Medifoam)'과 유착방지제 '가딕스(Guardix)'로 국내 시장 점유율 1위를 확보한 바이오소재 의료기기 기업이다. | 공식홈페이지 | 🟠중 | [동성 그룹사 소개(제네웰) / 증권플러스·잡코리아 기업정보](https://idongsung.com/affiliate05/?lang=en) |
| EV-GNW-002 | 사업분야 | 제네웰의 창상피복재 '메가덤 울트라(Megaderm Ultra)'는 아텔로콜라겐(atelocollagen)과 히알루론산나트륨을 주성분으로 하는 상용 콜라겐 기반 의료기기다. | 공식홈페이지 | 🟠중 | [제네웰 제품 페이지(메가덤울트라) / healmize 회사소개](http://www.genewel.com/product/megaderm-ultra-%EB%A9%94%EA%B0%80%EB%8D%A4%EC%9A%B8%ED%8A%B8%EB%9D%BC/) |
| EV-GNW-003 | 사업분야 | 제네웰의 사업·연구 영역은 창상피복재, 유착방지제, 조직수복재(조직보강재), 만성창상 치료재, 기능성 약물함유 의료기기이며 코스메틱·에스테틱으로 확장 중이다. | 공식홈페이지 | 🟠중 | [동성 그룹사 소개(제네웰) / 팜이데일리 CEO 인터뷰](https://idongsung.com/affiliate05/?lang=en) |
| EV-GNW-005 | 연구분야 | 제네웰의 R&D는 콜라겐을 핵심 소재로 창상피복재·지혈제·유착방지·조직수복재를 개발하며, 콜라겐의 혈소판 응집(지혈)·습윤 특성을 응용한다. | 특허 | 🟢상 | [제네웰 특허 WO2016010330A1 / 동성 그룹사 소개](https://patents.google.com/patent/WO2016010330A1/ko) |
| EV-GNW-006 | 연구분야 | 제네웰은 성균관대 약학대학과 기능성 창상피복재 공동연구 협약을 체결했다. | 주요언론 | 🟠중 | [동성화인텍 뉴스](https://dsfinetec.co.kr/news/) |
| EV-GNW-007 | 연구분야 | 제네웰은 경희대학교와 공동으로 습식방사(wet spinning) 기반 ADM(무세포진피·acellular dermal matrix) 콜라겐 섬유 제조법을 개발했다. | 특허 | 🟢상 | [Google Patents US12583909B2](https://patents.google.com/patent/US12583909B2/en) |
| EV-GNW-004 | 뉴스·동향 | 제네웰은 2024년 1월 바르는 의료기기 'MD크림'을 출시하며 더마코스메틱 시장으로 사업을 확장했다. | 주요언론 | 🔴하 | [디지틀조선일보](https://digitalchosun.dizzo.com/site/data/html_dir/2024/01/23/2024012380119.html) |
| EV-GNW-012 | 뉴스·동향 | 한상덕 제네웰 대표는 강원 원주에 400억원 이상을 투입한 신공장을 2026년 6월 완공하고 FDA·EMA 기준 설비를 도입해 사업다각화로 2030년 수출 목표를 제시했다. | 주요언론 | 🔴하 | [팜이데일리 / 네이트뉴스](https://pharm.edaily.co.kr/news/read?newsId=02351766642132512) |
| EV-GNW-013 | 뉴스·동향 | 제네웰은 통증감소 약물전달키트 '웰패스(WELPASS)'·유착방지제 가딕스의 유럽·호주 진출과 메디폼의 이커머스 입점을 확대하며 글로벌 파트너십 네트워크를 넓히고 있다. | 주요언론 | 🔴하 | [팜이데일리](https://pharm.edaily.co.kr/news/read?newsId=02351766642132512) |
| EV-GNW-008 | IP·특허 | 제네웰·경희대 공동 특허 US12583909B2(2026-03-24 등록)는 ADM 콜라겐을 습식방사해 섬유를 만드는 방법으로, BDDE·디에폭시 등 화학 가교를 사용하며 트랜스글루타미나제(mTG)는 사용하지 않는다. | 특허 | 🟢상 | [Google Patents US12583909B2](https://patents.google.com/patent/US12583909B2/en) |
| EV-GNW-009 | IP·특허 | 제네웰 특허 WO2016010330A1은 콜라겐(20-99wt%)·히알루론산 유도체·CMC 기반 고분자 폼으로 이중 지혈·유착방지 효과를 제공하며, 열가교·PVA/PVP 등 화학 가교를 쓰고 트랜스글루타미나제는 사용하지 않는다. | 특허 | 🟢상 | [Google Patents WO2016010330A1](https://patents.google.com/patent/WO2016010330A1/ko) |
| EV-GNW-010 | IP·특허 | 제네웰은 조직유착 방지용 온도감응성(thermosensitive) 조성물 특허 EP2366409B1(2014-12-10 등록)을 보유한다. | 특허 | 🟢상 | [Google Patents(assignee=Genewel 검색)](https://patents.google.com/patent/EP2366409B1/en) |
| EV-GNW-011 | IP·특허 | 제네웰은 항균 드레싱 소재 특허 US10987447B2(2021-04-27 등록)를 보유하는 등 창상피복재 IP 패밀리를 축적하고 있다. | 특허 | 🟢상 | [Google Patents(assignee=Genewel 검색)](https://patents.google.com/patent/US10987447B2/en) |
| EV-GNW-014 | 파트너십·M&A | 제네웰은 동성그룹 헬스케어 계열사로, 2002년 편입된 바이오레인(Biorane)과 2005년 편입된 바이오폴(Biopol)을 계보로 두며 현재 동성코퍼레이션 지배구조 하의 바이오사업 핵심사다. | 공식홈페이지 | 🟠중 | [동성 그룹사 소개 / 기업정보 검색](https://idongsung.com/affiliate05/?lang=en) |
| EV-GNW-015 | 파트너십·M&A | 제네웰은 성균관대 약대(창상피복재 공동연구)·경희대(ADM 콜라겐 섬유 공동특허) 등 학계와 R&D 협력을 맺고, 해외 진출을 위해 지역별 로컬 전문기업과 파트너십을 확대하고 있다. | 특허 | 🟠중 | [동성화인텍 뉴스 / US12583909B2 / 팜이데일리](https://patents.google.com/patent/US12583909B2/en) |

### 주식회사 제노스 (Genoss Co., Ltd.)

연관 판정 — **mTG**: 무관/하 · **ADC**: 무관/하 · **Collagen**: 직접사업/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-GNS-001 | 사업분야 | 제노스는 수원 영통 소재 인체삽입형 의료기기 전문기업으로 심혈관 스텐트·카테터, 합성골이식재, 콜라겐 차폐막, 더말필러(모나리자)·HAC 원료, 코스메틱을 개발·제조하며 79개국에 수출한다. | 공식홈페이지 | 🟢상 | [제노스 공식 홈페이지·사람인 기업정보(검색 종합)](https://genoss.com/) |
| EV-GNS-002 | 사업분야 | 제노스의 'GENOSS Collagen Membrane'은 소 힘줄 유래 제1형 콜라겐으로 제조된 흡수성 치과용 차폐막(GBR)으로, 2차 수술이 불필요한 생분해성 제품이다. | 규제기관 | 🟢상 | [US FDA 510(k) K102307 / 검색 종합](https://www.accessdata.fda.gov/cdrh_docs/pdf10/K102307.pdf) |
| EV-GNS-003 | 사업분야 | 제노스는 2023년 콜라겐을 혼합한 이종골이식재 'OSTEON Xeno Collagen'의 국내 허가를 완료했으며, 시트형 콜라겐 이식재 'Collagen Graft' 시리즈도 보유한다. | 주요언론 | 🟠중 | [세계일보·인크루트 기업정보(검색 종합)](https://www.segyebiz.com/lifeView/20250110505740) |
| EV-GNS-004 | 연구분야 | 제노스는 매년 매출액의 약 20%를 R&D에 투자하며 국내 의료기기 제조사 중 최다 품목허가를 보유했고, 콜라겐·골재생·스텐트·필러 소재 기술을 자체 개발한다. | 공식홈페이지 | 🟠중 | [제노스 공식 홈페이지·사람인(검색 종합)](https://genoss.com/) |
| EV-GNS-012 | 연구분야 | 제노스의 콜라겐/하이드로겔 가교는 화학·물리적(이중가교, EDC·방사선 계열) 방식으로 확인되며, 미생물 트랜스글루타미나제(mTG) 효소 사용이나 항체-약물 접합체(ADC) 관련 사업·연구는 전혀 확인되지 않는다. | 기타 | 🔴하 | [복합 검색(제노스 특허 + 'Genoss transglutaminase ADC')](https://patents.google.com/?assignee=%EC%A3%BC%EC%8B%9D%ED%9A%8C%EC%82%AC+%EC%A0%9C%EB%85%B8%EC%8A%A4) |
| EV-GNS-008 | 뉴스·동향 | 제노스는 2025년 7월 고밀도 콜라겐 이식재 'Collagen Graft x2D'를 출시했으며, 기존 시트형 x1D 대비 조직 밀도·물리적 안정성을 높여 연조직 정밀 수복을 강화했다. | 주요언론 | 🟠중 | [디지틀조선일보](https://digitalchosun.dizzo.com/site/data/html_dir/2025/07/10/2025071080217.html) |
| EV-GNS-010 | 뉴스·동향 | 제노스는 2025년 1월 러시아에서 합성골이식재 'OSTEON 3' 등 신규 6개 품목 허가와 기존 5종 갱신을 완료하며 콜라겐 함유 합성골 등 글로벌 시장을 확대했다. | 주요언론 | 🔴하 | [세계일보(세계비즈)](https://www.segyebiz.com/lifeView/20250110505740) |
| EV-GNS-011 | 뉴스·동향 | 제노스는 2025년 AMWC Monaco·코스모프로프 홍콩에 참가해 모나리자(MONALISA) 필러(론칭 11주년)·스킨부스터·PDRN 함유 브라이트 화장품 라인을 선보였다. | 주요언론 | 🟠중 | [네이트뉴스(제노스 보도)](https://news.nate.com/view/20251117n25774) |
| EV-GNS-005 | IP·특허 | 제노스(주식회사 제노스)는 골조직 유도재생용 차폐막(KR20130038598A) 특허를 보유해 콜라겐 계열 GBR 멤브레인 기술을 자체 확보했다. | 특허 | 🟢상 | [Google Patents (assignee=주식회사 제노스)](https://patents.google.com/patent/KR20130038598A/ko) |
| EV-GNS-006 | IP·특허 | 제노스는 '이중가교된 생분해성 고분자 하이드로겔-인산칼슘 복합체'(KR20160122657A)와 하이드로겔 복합체(KR102071029B1) 등 가교(crosslinking) 기반 소재 특허를 다수 보유한다. | 특허 | 🟢상 | [Google Patents (assignee=주식회사 제노스)](https://patents.google.com/patent/KR102071029B1/ko) |
| EV-GNS-007 | IP·특허 | 제노스는 부식저항성·재협착 억제 마그네슘 스텐트(KR101806373B1), 다공성 세라믹/고분자 이중층 골연골 스캐폴드(KR20180112698A) 등 심혈관·골재생 특허를 보유한다. | 특허 | 🟢상 | [Google Patents (assignee=주식회사 제노스)](https://patents.google.com/patent/KR101806373B1/ko) |
| EV-GNS-009 | 파트너십·M&A | 제노스는 필러 단일품목으로 약 110억원 규모의 ODM 수출 계약을 체결했다. | 주요언론 | 🔴하 | [헬스경향](https://www.k-health.com/news/articleView.html?idxno=67030) |

### 주식회사 제테마 (Jetema Co., Ltd.)

연관 판정 — **mTG**: 무관/하 · **ADC**: 무관/하 · **Collagen**: 인접·응용/중

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-JET-001 | 사업분야 | 제테마의 매출은 HA 필러 약 60.7%, 보툴리눔 톡신 약 26.7%, 조직봉합·안면고정 리프팅실 등 약 12.6%로 구성된다. | 업계리포트 | 🟠중 | [THE VC 기업정보 (제테마)](https://thevc.kr/jetema) |
| EV-JET-002 | 사업분야 | 제테마는 HA 필러(에피티크 e.p.t.q)와 보툴리눔 톡신을 주력으로 하는 미용·성형 의료기기·의약품 B2B 기업이며 2025년 매출은 약 736억 원이다. | 주요언론 | 🟠중 | [컨슈머타임스](https://www.cstimes.com/news/articleView.html?idxno=699289) |
| EV-JET-003 | 사업분야 | 제테마는 PLLA를 주성분으로 자가 콜라겐 생성을 촉진하는 스킨부스터 '에꼴라S(Ecollas)'를 출시했다. | 주요언론 | 🟠중 | [제테마 뉴스(에꼴라S 출시) / 대한레이저피부모발학회 참가 보도](https://www.etnews.com/20241217000171) |
| EV-JET-004 | 사업분야 | 제테마는 인체조직 유래 무세포 동종진피(hADM) 기반 ECM 스킨부스터 '아디떼(ADITE)'로 재생의학 포트폴리오를 확대하며, 콜라겐·엘라스틴·히알루론산 등 ECM 성분을 직접 보충한다. | 주요언론 | 🟠중 | [뉴스핌](https://www.newspim.com/news/view/20260518000854) |
| EV-JET-005 | 사업분야 | 아디떼(ADITE)는 메드파크의 특허기반 MPT 기술로 완성된 hADM 스킨부스터로, 콜라겐 기반 무세포동종진피 성분을 미세입자(약 70㎛)로 피부에 공급한다. | 주요언론 | 🟠중 | [메디팜헬스뉴스 / 네이트뉴스(메드파크 아디떼)](https://news.nate.com/view/20251216n29169) |
| EV-JET-006 | 사업분야 | 제테마는 폴리뉴클레오타이드(PN) 성분 스킨부스터 '프라쥬에(Frajue)'를 국내 250명 임상 후 식약처 허가로 출시했다. | 주요언론 | 🟠중 | [메디컬투데이](https://mdtoday.co.kr/news/view/1065597354096485) |
| EV-JET-007 | 연구분야 | 제테마는 유럽 국립기관에서 도입한 균주로 고순도 A형 보툴리눔 톡신(제테마더톡신) 자체 생산기술을 개발했고, 차세대 E형 톡신 파이프라인을 개발 중이다. | 주요언론 | 🟠중 | [팜이데일리](https://pharm.edaily.co.kr/news/read?newsId=02050006642139400) |
| EV-JET-008 | 연구분야 | 제테마더톡신주 100U는 2024년 12월 국내 품목허가를 받아 2025년 3월 국내 출시되었고, 100U/200U는 앞서 수출용 허가를 받았다. | 주요언론 | 🟠중 | [팜이데일리](https://pharm.edaily.co.kr/News/Read?mediaCodeNo=257&newsId=01443206638852184) |
| EV-JET-015 | 연구분야 | 제테마의 사업·파이프라인·특허는 HA 필러·보툴리눔 톡신·리프팅실·스킨부스터에 한정되며, ADC(항체-약물 접합체) 프로그램과 mTG(미생물 트랜스글루타미나제) 효소가교 접점은 모두 부재하다(무관 확정). | 주요언론 | 🟢상 | [팜이데일리(제테마 사업/파이프라인) / Google Patents(assignee 제테마) 종합](https://pharm.edaily.co.kr/News/Read?newsId=01764646638761000&mediaCodeNo=257) |
| EV-JET-009 | 뉴스·동향 | 제테마의 보툴리눔 톡신 JTM201이 중국 임상 3상 결과보고서(CSR)를 승인받아 보톡스 대비 비열등성을 입증하며 중국 진출 기대가 커졌다. | 주요언론 | 🟠중 | [파이낸셜뉴스 / 한국경제](https://www.fnnews.com/news/202605291458570749) |
| EV-JET-010 | 뉴스·동향 | 제테마는 2025년 5월 칠레에서 HA 필러 '에피티크'와 콜라겐자극 제품 '에꼴라'를 론칭하며 중남미 시장 공략에 나섰다. | 주요언론 | 🟠중 | [한국경제](https://www.hankyung.com/article/202605211927i) |
| EV-JET-011 | 뉴스·동향 | 제테마는 2026년 5월 ECM 기반 hADM 스킨부스터 아디떼를 출시하며 흉터개선·조직재생 등 재생의학 영역으로 적용을 확대한다고 밝혔다. | 주요언론 | 🟠중 | [한국경제 / 메디팜헬스뉴스](https://www.medipharmhealth.co.kr/news/article.html?no=116378) |
| EV-JET-012 | IP·특허 | 제테마는 가교 히알루론산 필러 조성물·가교율 측정, 생분해성 고분자 나노입자 필러, 보툴리눔 톡신 액상제형 등 특허를 출원·보유하고 있다. | 특허 | 🟠중 | [Google Patents (assignee 제테마)](https://patents.google.com/?assignee=%EC%A0%9C%ED%85%8C%EB%A7%88) |
| EV-JET-013 | 파트너십·M&A | 제테마는 2022년 중국 화동(Huadong)과 보툴리눔 톡신 중국 라이선스아웃(약 6,000억 원 규모) 계약을, 이후 HA필러 에피티크 유통·판촉(약 439억 원) 계약을 체결했다. | 주요언론 | 🟠중 | [Businesskorea / 벤처스퀘어](https://www.businesskorea.co.kr/news/articleView.html?idxno=235575) |
| EV-JET-014 | 파트너십·M&A | 제테마는 태국 파트너사와 5년 약 400억 원 규모 톡신 수출계약을 체결하고 인도네시아 할랄 인증, 중국 에피티크 품목허가 등 글로벌 확장을 진행했다. | 주요언론 | 🟠중 | [파이낸셜투데이 / 바이오타임즈](https://www.ftoday.co.kr/news/articleView.html?idxno=337194) |

### 테고사이언스 (Tego Science, Inc.)

연관 판정 — **mTG**: 무관/하 · **ADC**: 무관/하 · **Collagen**: 인접·응용/중

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-TEG-001 | 사업분야 | 테고사이언스는 케라틴세포·섬유아세포 배양기술 기반 세포치료제(홀로덤·칼로덤·로스미르)를 개발·판매하는 KOSDAQ 상장 재생의료 기업이다. | 공식홈페이지 | 🟠중 | [테고사이언스 공식 홈페이지 (회사소개)](http://www.tegoscience.com/kor/company/introPage.do) |
| EV-TEG-002 | 사업분야 | 칼로덤은 신생아 포피 유래 케라틴세포로 대량생산되는 국내 최초 동종유래 배양피부 세포치료제로, 화상·당뇨성족부궤양 치료에 쓰이며 전체 매출의 약 80%를 차지한다. | 공식홈페이지 | 🟢상 | [테고사이언스 제품페이지 / 청년의사](http://www.tegoscience.com/kor/product/view.do?prdSeq=12) |
| EV-TEG-003 | 사업분야 | 로스미르는 환자 자기유래 진피 섬유아세포로 구성된 눈밑 주름개선 세포치료제로, 국내 유일·세계 최초 주름개선 세포치료제로 품목허가되었다. | 공식홈페이지 | 🟢상 | [테고사이언스 제품페이지 / 바이오스펙테이터](http://www.tegoscience.com/kor/product/view.do?prdSeq=13) |
| EV-TEG-004 | 사업분야 | 로스미르에 함유된 진피 섬유아세포는 생착 후 콜라겐 등 세포외기질(ECM) 단백질을 합성해 진피구조를 복원함으로써 주름을 개선한다. | 주요언론 | 🟠중 | [바이오스펙테이터 / 테고사이언스](http://biospectator.com/view/news_view.php?varAtcId=4681) |
| EV-TEG-005 | 사업분야 | 테고사이언스는 케라틴세포·섬유아세포·멜라닌세포와 생체재료를 조합한 3D 배양기술로 진피·표피 전층을 재현한 인공배양피부모델 '네오덤(Neoderm)'을 동물실험 대체용으로 생산·공급한다. | 공식홈페이지 | 🟢상 | [테고사이언스 / BRIC Bio마켓](http://www.tegoscience.com/kor/business/neodermPage.do) |
| EV-TEG-006 | 사업분야 | 테고사이언스는 자회사(큐티젠 래버러토리스)를 통해 케라틴 피부줄기세포배양액(KCM)·케모타이드(Chemotide) 등 세포유래 성장인자 기반 화장품 원료를 개발·공급하며, CDMO 사업도 병행한다. | 주요언론 | 🟠중 | [코스인코리아닷컴 (화장품원료 기업탐방)](https://cosinkorea.com/mobile/article.html?no=43718) |
| EV-TEG-007 | 연구분야 | 핵심 R&D 파이프라인 TPX-114는 자기유래 섬유아세포 기반 회전근개 전층파열 치료제로, 초기시험에서 부작용 없이 힘줄(건) 재생 촉진이 관찰되었다. | 주요언론 | 🟠중 | [청년의사 / 약업신문](https://www.docdocdoc.co.kr/news/articleView.html?idxno=2016482) |
| EV-TEG-008 | 연구분야 | TPX-115는 동종 진피 섬유아세포 기반 회전근개 부분파열 치료제로, 손상된 힘줄·인대 재생을 목표로 미국 임상 2상을 진행 중이다. | 주요언론 | 🟠중 | [이데일리 팜 / 파마뉴스](https://pharm.edaily.co.kr/news/read?newsId=03801526642070520) |
| EV-TEG-014 | 연구분야 | 테고사이언스의 제품·파이프라인 검색에서 mTG(미생물 트랜스글루타미나제) 효소의 생산·사용·공급이나 자체 ADC(항체-약물 접합체) 파이프라인·접합기술은 확인되지 않았다. | 기타 | 🔴하 | [웹검색 종합 (국문·영문)](https://pubs.acs.org/doi/10.1021/bc400574z) |
| EV-TEG-009 | 뉴스·동향 | 테고사이언스는 미국 FDA로부터 TPX-115 임상 2상(IND)을 승인받고, 2025년 11월 26일 미국 다기관 무작위·이중눈가림·위약대조 2상의 첫 환자 등록을 시작했다. | 주요언론 | 🟠중 | [이데일리 / 청년의사](https://www.edaily.co.kr/News/Read?newsId=02246806642370312&mediaCodeNo=257) |
| EV-TEG-010 | 뉴스·동향 | 테고사이언스의 2024년 매출은 약 59.4억원(전년 대비 -12%), 영업손실 약 -33억원이며, 2025년에도 분기 매출이 감소세를 보였다. | IR·공시 | 🟠중 | [증권/IR 자료 및 언론 종합 (FnGuide, IB토마토)](https://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?gicode=A191420) |
| EV-TEG-011 | IP·특허 | 테고사이언스는 '진피층 및 표피층을 포함하는 삼차원 배양 피부모델 제조방법'(네오덤 관련) 발명으로 미국 특허를 등록했다. | 주요언론 | 🟠중 | [청년의사](http://www.docdocdoc.co.kr/news/articleView.html?idxno=1066254) |
| EV-TEG-012 | IP·특허 | 테고사이언스는 화장품 원료 케모타이드(Chemotide, 피부재생 케모카인 BLC·TECK·MIP-3a)를 국내외 특허로 등록했다. | 주요언론 | 🟠중 | [코스인코리아닷컴](https://cosinkorea.com/mobile/article.html?no=43718) |
| EV-TEG-013 | 파트너십·M&A | 테고사이언스는 TPX-115의 미국 2상 종료 후 글로벌 개발·판권 기술수출을 최우선 전략으로 삼고 있으며, 국내 개발권은 자체 보유할 계획이다. | 주요언론 | 🟠중 | [이데일리 팜](https://pharm.edaily.co.kr/News/Read?newsId=01886006642039688) |

### 티센바이오팜 (TissenBioFarm Co., Ltd.)

연관 판정 — **mTG**: 인접·응용/중 · **ADC**: 무관/하 · **Collagen**: 인접·응용/중

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-TBF-001 | 사업분야 | 티센바이오팜은 POSTECH 기반 배양육(cultured meat) 스타트업으로, 3D 바이오프린팅과 조직공학으로 마블링·고깃결을 재현한 덩어리육(whole-cut)을 개발한다. | 주요언론 | 🟠중 | [vegconomist / KoreaTechDesk](https://vegconomist.com/investments-finance/investments-acquisitions/tissenbio-farms-cultivated-meat-marbling/) |
| EV-TBF-002 | 사업분야 | 배양육·식물성 대체육 대량생산에 적용 가능한 100g당 약 400원의 식용 바이오잉크 3종을 자체 개발했다. | 공식홈페이지 | 🟠중 | [티센바이오팜 공식 홈페이지 (스타트업 101 소개)](https://tissenbiofarm.co.kr/27/?bmode=view&idx=17078532) |
| EV-TBF-003 | 연구분야 | 배양육을 '세포의 집합'이 아닌 '조직'으로 정의하고 조직공학 기술로 실제 고기와 동일 수준의 세포 수를 세계 최초로 구현했다고 발표했다. | 주요언론 | 🟠중 | [바이오타임즈 / MD투데이](https://www.biotimes.co.kr/news/articleView.html?idxno=26154) |
| EV-TBF-004 | 연구분야 | 미세 섬유 압출 기반 초고속 바이오패브리케이션 시스템(시간당 수백 kg 섬유 생산)과 습식 컨베이어벨트 이송 시스템을 구축했다. | 주요언론 | 🟠중 | [유스연합 / 한국법률경제신문 (중기부 데모데이 보도)](https://www.youthassembly.kr/news/846552) |
| EV-TBF-005 | 연구분야 | 소태아혈청(FBS)을 사용하지 않는 배양 기술을 확보하고 고가 배양 소재를 식품등급의 저렴한 소재로 100% 대체해 생산비를 낮췄다고 밝혔다. | 주요언론 | 🟠중 | [매일신문 (대구경북 혁신기업 인터뷰)](https://www.imaeil.com/page/view/2025100800300317278) |
| EV-TBF-014 | 연구분야 | 티센바이오팜의 사업·연구·자사 특허(배양육 바이오잉크 WO2023063468A1 등)는 모두 배양육/식품테크에 한정되며, ADC(항체-약물 접합체)·링커/접합기술·ADC용 mTG 공급 등 종양학 모달리티 접점은 부재하다(무관 확정). | 특허 | 🟢상 | [Google Patents(WO2023063468A1 본문 확인) / 다중 웹검색 종합](https://patents.google.com/patent/WO2023063468A1/en) |
| EV-TBF-009 | 뉴스·동향 | 티센바이오팜은 2023년 세계 최초로 10kg 규모 덩어리형 배양육 시제품을 공개했고 2024년 AgTech Breakthrough Award 'Cultured Meat Product of the Year'를 수상했다. | 주요언론 | 🟠중 | [vegconomist / The Cell Base](https://vegconomist.com/cultivated-cell-cultured-biotechnology/cultivated-meat/tissenbiofarm-10-kg-cultivated-meat-south-korea-hub/) |
| EV-TBF-010 | 뉴스·동향 | 2025~2026년 배양육 세포배양·조직공학 기술을 화장품으로 확장, 세포배양 유래 원료 T-NUTREX PLUS와 닥랩 협업 리프팅 마스크를 롯데홈쇼핑에서 완판했다. | 주요언론 | 🟠중 | [스타트업엔 / 코스인코리아 / 머니투데이](https://www.startupn.kr/news/articleView.html?idxno=57485) |
| EV-TBF-006 | IP·특허 | 티센바이오팜 명의 특허 WO2023063468A1(인공육 제조방법)은 젤라틴·콜라겐 등을 식용 가능한 기초 원료로, 트랜스글루타미나제를 가교제로 명시한다. | 특허 | 🟢상 | [Google Patents (WO2023063468A1)](https://patents.google.com/patent/WO2023063468A1/en) |
| EV-TBF-007 | IP·특허 | 티센바이오팜 특허 KR102590675B1은 2~40,000개 다중 토출구를 갖는 압출 노즐과 가교제가 담긴 수용 챔버로 식용 섬유·세포 구조체를 초고속 생산하는 시스템이다. | 특허 | 🟢상 | [Google Patents (KR102590675B1)](https://patents.google.com/patent/KR102590675B1/ko) |
| EV-TBF-008 | IP·특허 | 티센바이오팜은 WO2023/063468 외 KR102747533·KR102747536·KR102590675 등 3D 바이오프린팅·다중노즐 배양육 제조 특허 패밀리를 보유한다. | 업계리포트 | 🟠중 | [Reddie & Grose IP 분석 (검색 스니펫)](https://www.reddie.co.uk/2025/03/05/sustainable-foods-for-the-future-3-meat-the-innovators-part-ii/) |
| EV-TBF-011 | 파트너십·M&A | 2022년 9월 22억원(약 $1.6M) 프리시리즈A를 인비저닝파트너스 리드(퓨처플레이·스톤브릿지벤처스·미래과학기술지주 참여)로 유치했다. | 주요언론 | 🟠중 | [머니투데이 / platum / greenqueen](https://platum.kr/archives/192655) |
| EV-TBF-012 | 파트너십·M&A | 2026년 1월 글로벌 임팩트 투자사 Beyond Impact로부터 투자를 유치하고 중소벤처기업부 '글로벌 팁스'에 선정되었다. | 주요언론 | 🟠중 | [와우테일 / 스포트피플타임스](https://wowtale.net/2026/01/14/253257/) |
| EV-TBF-013 | 파트너십·M&A | 2024년 중소벤처기업부 '아기유니콘' 기업에 선정되는 등 정부 지원 트랙에 진입했다. | 주요언론 | 🟠중 | [머니투데이](https://news.mt.co.kr/mtview.php?no=2024062717442519064) |

### 티앤알바이오팹 (T&R Biofab Co., Ltd.)

연관 판정 — **mTG**: 무관/하 · **ADC**: 무관/하 · **Collagen**: 직접사업/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-TNR-001 | 사업분야 | 티앤알바이오팹은 3D 바이오프린팅 기반 재생의료 기업으로 생분해성 인공지지체, 바이오잉크, 3D 오가노이드, 세포치료제, ECM 기반 바이오써지컬 솔루션을 개발·상용화한다. | 주요언론 | 🟠중 | [위키백과 / 팜이데일리(티앤알바이오팹 대해부)](https://ko.wikipedia.org/wiki/%ED%8B%B0%EC%95%A4%EC%95%8C%EB%B0%94%EC%9D%B4%EC%98%A4%ED%8C%B9) |
| EV-TNR-002 | 사업분야 | 3D프린팅 기반 의료기기 13개 품목과 ECM 기반 바이오써지컬 12개 품목이 식약처 승인을 받았고 누적 10만명 이상에게 적용되었다. | 공식홈페이지 | 🟠중 | [티앤알바이오팹 공식 보도자료 / 바이오스펙테이터](http://tnrbiofab.com/eng/product/) |
| EV-TNR-003 | 사업분야 | 주력 바이오잉크 제품 'deCelluid'는 돼지 조직 유래 탈세포화 세포외기질(dECM)로, 콜라겐·GAG·엘라스틴을 함유한 조직특이적 바이오잉크 8종 이상으로 구성된다. | 논문 | 🟢상 | [Materials(MDPI) 논문 PMC8467964 / 바이오스펙테이터](https://pmc.ncbi.nlm.nih.gov/articles/PMC8467964/) |
| EV-TNR-004 | 연구분야 | 피부 유래 dECM 바이오잉크로 인공피부를 3D 프린팅하며, 단일 콜라겐 대비 콜라겐 섬유 형성·세포미세환경 인식이 개선되어 기계적 강도가 향상됨을 연구로 입증했다. | 논문 | 🟢상 | [바이오타임즈 / Materials(MDPI) PMC8467964](https://www.mdpi.com/1996-1944/14/18/5177) |
| EV-TNR-005 | 연구분야 | 심장·간·피부 등 인공장기와 세포블록 조립형 조직 제작, 3D 프린팅 세포치료제(심근 조직 재생) 등 재생의료 파이프라인을 보유한다. | 주요언론 | 🟠중 | [바이오타임즈 / 바이오스펙테이터](https://www.biotimes.co.kr/news/articleView.html?idxno=26751) |
| EV-TNR-006 | 연구분야 | 젤라틴 메타크릴레이트(GelMA) 광가교 및 생체적합 가교제로 바이오잉크·지지체의 조직 강도를 확보하나, 미생물 트랜스글루타미나제(mTG) 효소 가교의 명시적 사용은 확인되지 않는다. | 주요언론 | 🟠중 | [잡코리아 기업정보 / 히트뉴스 등](https://m.jobkorea.co.kr/company/45174258) |
| EV-TNR-007 | 뉴스·동향 | 3D 바이오프린팅 인공피부의 치료 효능을 입증한 논문이 2021년 국제학술지 Materials(MDPI)에 게재되었다. | 논문 | 🟠중 | [Materials(MDPI) / 코스인코리아](https://www.mdpi.com/1996-1944/14/18/5177) |
| EV-TNR-008 | 뉴스·동향 | 코스맥스비티아이와 차세대 전층 인공피부 공동 연구개발 계약을 체결하는 등 화장품·피부 모델 분야로 사업을 확장하고 있다. | 주요언론 | 🟠중 | [바이오타임즈](https://www.biotimes.co.kr/news/articleView.html?idxno=8217) |
| EV-TNR-009 | 뉴스·동향 | CJ제일제당과 대체육 공동개발 협약을 맺고 3D 프린팅 세포지지체 기술로 배양육 시장 진출을 준비 중이다. | 주요언론 | 🟠중 | [팜이데일리(티앤알바이오팹 대해부 ②)](https://pharm.edaily.co.kr/news/read?newsId=01676086638758704) |
| EV-TNR-010 | IP·특허 | dECM 바이오잉크로 인체 피부 탄력까지 모사한 3D 바이오프린팅 인공피부 제조·탄성측정 기술로 2022년 2월 국내 특허를 취득했다. | 주요언론 | 🟠중 | [머니투데이 / 바이오타임즈](https://news.mt.co.kr/mtview.php?no=2022021509370831980) |
| EV-TNR-011 | IP·특허 | 살아있는 세포를 균일 분포시켜 인공장기를 대량 생산하는 '바이오잉크 공급 시스템' 기술로 한국·일본·중국·유럽에 이어 미국 특허 등록을 완료했다. | 주요언론 | 🟠중 | [히트뉴스](https://www.hitnews.co.kr/news/articleView.html?idxno=69551) |
| EV-TNR-012 | IP·특허 | 유방 재건술용 3D 프린팅 하이브리드 인공지지체 기술의 국내 특허를 등록 완료했다. | 주요언론 | 🟠중 | [히트뉴스 / 바이오타임즈](https://www.biotimes.co.kr/news/articleView.html?idxno=19338) |
| EV-TNR-013 | 파트너십·M&A | 독일 머크(Merck KGaA)와 dECM 바이오잉크 deCelluid의 OEM 공급계약을 체결해 시그마알드리치(Sigma-Aldrich) 유통망으로 글로벌 판매한다. | 주요언론 | 🟠중 | [바이오스펙테이터](http://www.biospectator.com/view/news_view.php?varAtcId=6061) |
| EV-TNR-014 | 파트너십·M&A | 존슨앤존슨(J&J) 자회사 에티콘(Ethicon) 및 J&J Innovation과 창상치료·조직재건용 3D 바이오프린팅 연조직 스캐폴드 공동개발 계약을 체결했다. | 주요언론 | 🟠중 | [Korea Biomedical Review / PlasticsToday](https://www.koreabiomed.com/news/articleView.html?idxno=14371) |
| EV-TNR-015 | 파트너십·M&A | 로레알(L'Oréal)과 협업해 3D 바이오프린팅 인공피부의 효능 개선을 입증한 논문을 발표한 것으로 보도되었다. | 주요언론 | 🔴하 | [THE K BEAUTY SCIENCE](https://www.thekbs.co.kr/news/articleView.html?idxno=3515) |
| EV-TNR-016 | 파트너십·M&A | 쥬디스인터내셔널과 국소 하이드로겔 창상피복재 공급계약을 체결하는 등 창상·조직재생 의료기기 유통 파트너십을 확대하고 있다. | 주요언론 | 🟠중 | [바이오타임즈](https://www.biotimes.co.kr/news/articleView.html?idxno=8243) |

### 한스바이오메드 (Hans Biomed Corp.)

연관 판정 — **mTG**: 무관/하 · **ADC**: 무관/하 · **Collagen**: 직접사업/상

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-HAN-001 | 사업분야 | 한스바이오메드는 인체조직 이식재(피부·뼈 ADM), 리프팅 실 등 의료기기, 실리콘 보형물, 화장품을 제조·판매하는 코스닥 상장(042520) 바이오기업이다. | 공식홈페이지 | 🟢상 | [한스바이오메드 공식 홈페이지 / 위키백과](https://www.hansbiomed.com/) |
| EV-HAN-002 | 사업분야 | SureDerm은 인체(동종) 진피 유래 무세포진피기질(ADM)로, 콜라겐 기반 연조직 재건용 이식재이며 회사의 대표 제품군이다. | 공식홈페이지 | 🟢상 | [한스바이오메드 제품 페이지 / ScienceDirect ADM overview](http://www.hansbiomed.com/product/product_view?idx=81&type=tissue&ptype=productKRTissue) |
| EV-HAN-003 | 사업분야 | 동종진피 콜라겐 필러 '벨라젠 플러스(BellaGen Plus)'는 100% 동종진피 유래 주사형 ADM으로 콜라겐 함량 76% 이상의 휴먼 콜라겐 필러다. | 공식홈페이지 | 🟢상 | [한스바이오메드 보도자료](https://hansbiomed.com/m/pr/view?btype=boardsKRMedia&idx=1210&stype=media) |
| EV-HAN-004 | 사업분야 | 제25기(2022.10~2023.9) 연결 매출 780억원 중 인체조직 이식재(뼈·피부) 47.7%, 의료기기(리프팅 실·모발이식기) 43.4%로 이식재와 의료기기가 양대 축이다. | IR·공시 | 🟠중 | [네이버 증권 리포트(한스바이오메드) / DART 사업보고서 요약](https://ssl.pstatic.net/imgstock/upload/research/company/1706224171509.pdf) |
| EV-HAN-005 | 사업분야 | 전체 매출은 제25기 780억원→제26기 811억원→제27기(2024.10~2025.9) 898억원으로 증가했고, 회사는 2026년 매출 1000억원 돌파를 전망한다. | 주요언론 | 🟠중 | [네이트/뉴스(한스바이오메드 대해부)](https://news.nate.com/view/20251222n04086) |
| EV-HAN-006 | 연구분야 | 회사는 ECM(세포외기질) 플랫폼 기반 R&D를 추진하며, 2024년 출시 스킨부스터 '셀르디엠(CellREDM)'은 무세포동종진피(hADM)를 원료로 콜라겐·엘라스틴·GAGs를 ECM 구조에 통합했다. | 주요언론 | 🟠중 | [바이오타임즈 / press9](https://www.biotimes.co.kr/news/articleView.html?idxno=24779) |
| EV-HAN-007 | 연구분야 | 한스바이오메드는 세계 최초 다공성 스펀지 구조 ADM 'SUREDERM Repair'를 개발, 블록형 무세포진피 분말 기반 피부이식 기술로 재건 치료재료 시장을 공략한다. | 주요언론 | 🟠중 | [스포츠경향 / 네이트](https://sports.khan.co.kr/article/202606101031003/) |
| EV-HAN-008 | 연구분야 | 유방재건용 인체 무세포진피 'BellaCell HD'는 AlloDerm RTU·DermACELL 등과 비교한 in vitro 특성 분석이 피어리뷰 논문으로 발표된 콜라겐 기반 이식재다. | 논문 | 🟢상 | [PMC (In Vitro Characterization of BellaCell HD)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7356368/) |
| EV-HAN-016 | 연구분야 | 한스바이오메드의 ADM·콜라겐 필러는 인체/돼지 진피를 탈세포화한 천연 콜라겐 기질이며, mTG(미생물 트랜스글루타미나제) 효소 가교 사용은 확인되지 않는다. | 기타 | 🔴하 | [복합 검색(홈페이지·Google Patents·학술)](https://www.hansbiomed.com/) |
| EV-HAN-017 | 연구분야 | 한스바이오메드에는 항체-약물 접합체(ADC) 파이프라인이나 링커·페이로드 접합 기술, ADC용 mTG 공급이 존재하지 않는다. | 기타 | 🔴하 | [복합 검색](https://www.hansbiomed.com/) |
| EV-HAN-009 | 뉴스·동향 | 한스바이오메드는 3D 몰딩실에 MESH 타입 구조를 적용한 안면 리프팅 실 신제품 'MINT MESH'를 출시했다. | 주요언론 | 🟠중 | [한스바이오메드 보도자료(언론 인용)](https://www.hansbiomed.com/) |
| EV-HAN-010 | 뉴스·동향 | 2026년 6월 인터뷰에서 한스바이오메드는 K-의료 수요 확대에도 인허가 규제를 애로로 지목했고, 중국 NMPA로부터 동종골 이식재 '익스퓨즈(ExFuse)' 수입 허가를 완료해 중국 진출을 본격화했다. | 주요언론 | 🟠중 | [뉴스핌 / 네이트](https://www.newspim.com/news/view/20260628000103) |
| EV-HAN-011 | 뉴스·동향 | 증권가는 2026년 한스바이오메드의 실적 턴어라운드를 전망하며(상상인증권 목표가 5만원), 셀르디엠의 국내 300억·일본 80억 등 총 380억원 매출과 50%대 영업이익률을 추정했다. | 업계리포트 | 🟠중 | [네이트/상상인증권 리포트 브리핑](https://news.nate.com/view/20260202n17884) |
| EV-HAN-012 | IP·특허 | SUREDERM Repair의 블록형 무세포진피 분말 기반 피부이식 기술은 특허 출원 중이며 스펀지형 ADM 분야 기술 경쟁력 확보의 기반이다. | 주요언론 | 🟠중 | [스포츠경향 / 네이트](https://news.nate.com/view/20260610n11864) |
| EV-HAN-013 | 파트너십·M&A | 오스템임플란트는 2020년 12월 벨라젤 판매중지 위기 때 200억원 규모 4회차 사모 CB를 인수(백기사)하고 전환으로 지분 11.63%를 확보해 2대주주에 올랐다. | 주요언론 | 🟠중 | [딜사이트 / 이데일리](https://dealsite.co.kr/articles/157881) |
| EV-HAN-014 | 파트너십·M&A | 오스템임플란트는 2024~2025년 주가 상승 후 한스바이오메드 보유 지분을 순차 매각해 전량 정리(약 200억원 시세차익)했으나, 양사 치과용 골이식재 공급 등 협력관계는 유지될 전망이다. | 주요언론 | 🟠중 | [딜사이트 / 스마트투데이](https://dealsite.co.kr/articles/157881) |
| EV-HAN-015 | 파트너십·M&A | 2024년 12월 한스바이오메드의 186억원 규모 제3자배정 유상증자에 최규옥 오스템 회장 가족회사 네오영이 참여해 지분 5.55%(특수관계 포함 9.26%)를 확보했다. | 주요언론 | 🟠중 | [비즈워치(거버넌스워치)](https://news.bizwatch.co.kr/article/governance/2025/12/05/0001) |

### 휴메딕스 (Humedix Co., Ltd.)

연관 판정 — **mTG**: 무관/하 · **ADC**: 무관/하 · **Collagen**: 인접·응용/중

| evidence_id | 카테고리 | 사실 | 출처유형 | 검증 | 출처 |
|---|---|---|---|:---:|---|
| EV-HUM-001 | 사업분야 | 휴메딕스는 히알루론산(HA)과 PDRN 원료의 생산·응용 기술을 기반으로 에스테틱·전문의약품 사업을 하는 휴온스그룹 계열 헬스케어 기업이다. | 공식홈페이지 | 🟢상 | [휴메딕스 공식 홈페이지 / 한국경제](https://humedix.com/web/home.php?go=Amenu_01) |
| EV-HUM-002 | 사업분야 | 주력 포트폴리오는 HA 필러(엘라비에/엘라비에 프리미어), 보툴리눔 톡신 '리즈톡스', 에스테틱 의료기기 '더마사인', 기능성 화장품 '더마 엘라비에'로 구성된 토탈 에스테틱 솔루션이다. | 공식홈페이지 | 🟢상 | [휴메딕스 영문 공식 홈페이지](https://humedix.com/eng/home.php?go=Amenu_03) |
| EV-HUM-003 | 사업분야 | 휴메딕스는 무세포동종진피(hADM) 성분으로 콜라겐 및 세포외기질(ECM)을 보충하는 스킨부스터 '엘라비에 리투오(Elravie Re2O)'를 국내 판매·마케팅한다. | 주요언론 | 🟠중 | [한국경제 / 더바이오뉴스](https://www.hankyung.com/article/202411187508P) |
| EV-HUM-004 | 사업분야 | 휴메딕스는 체내 콜라겐 생성을 자극하는 PLA(폴리락틱애시드) 필러 '에스테필'의 국내 공식 판권을 확보했다. | 주요언론 | 🟠중 | [메디컬투데이](https://www.mdtoday.co.kr/news/view/1065576597787298) |
| EV-HUM-005 | 연구분야 | 휴메딕스는 고분자·바이오·합성·제제 연구조직을 두고, 독자 'HiVE(High Viscoelasticity)' 공법으로 가교효율은 높이고 가교제(BDDE) 잔류량은 낮춘 HA 필러를 개발한다. | 공식홈페이지 | 🟠중 | [휴메딕스 홈페이지 / 약사공론(3Q 실적 기사)](https://www.kpanews.co.kr/article/show.asp?category=D&idx=265148) |
| EV-HUM-006 | 연구분야 | 개발 중인 차세대 HA 필러(HMM1-026)가 정부 '다부처 전주기 의료기기 연구개발 지원사업'에 선정되었다. | 공식홈페이지 | 🟠중 | [휴메딕스 보도자료](https://humedix.com/m/home.php?go=Emenu_05&num=2780) |
| EV-HUM-007 | 연구분야 | 전문의약품으로 HA 단회투여 골관절염 주사 '하이히알원스'와 PDRN 주사제 '리바이탈렉스' 등을 개발·보유한다. | 공식홈페이지 | 🟠중 | [휴메딕스 영문 홈페이지](https://humedix.com/eng/home.php?go=Amenu_03) |
| EV-HUM-016 | 연구분야 | 휴메딕스의 제품/특허에서 mTG(미생물 트랜스글루타미나제) 등 효소 가교나 재조합 콜라겐 자체 생산 기술은 확인되지 않았다. | 기타 | 🔴하 | [다중 검색 종합(honest_gap)](https://patents.google.com/patent/KR20160077750A/ko) |
| EV-HUM-008 | 뉴스·동향 | 휴메딕스의 2025년 3분기 매출액은 409억원, 영업이익 90억원으로 전년동기 대비 약 10% 성장했다. | 주요언론 | 🟠중 | [약사공론 / 청년일보](https://www.kpanews.co.kr/article/show.asp?category=D&idx=265148) |
| EV-HUM-009 | 뉴스·동향 | 휴메딕스는 2026년 HA 필러 '리포리아 HARA-L'의 중국 NMPA 품목허가를 획득하는 등 해외(중국·러시아·시리아·브라질) 시장 진출을 확대하고 있다. | 주요언론 | 🟠중 | [한국경제](https://www.hankyung.com/article/202606195816i) |
| EV-HUM-010 | 뉴스·동향 | 폴리뉴클레오티드나트륨(PN)과 HA를 결합한 복합 필러 '밸피엔'의 국내 확증임상을 완료하고 식약처 품목허가를 신청했다. | 주요언론 | 🟠중 | [휴메딕스 보도자료 / 약사공론](https://www.kpanews.co.kr/news/articleView.html?idxno=536862) |
| EV-HUM-011 | IP·특허 | 휴메딕스는 PN·HA 복합 필러 '밸피엔'의 조성물·제조방법에 대해 2026년 6월 러시아 특허청으로부터 특허 등록 결정을 받았다. | 주요언론 | 🟠중 | [뉴시스 / 아시아경제 / 약사공론](https://www.newsis.com/view/NISX20260617_0003672164) |
| EV-HUM-012 | IP·특허 | 휴메딕스는 2022년 'DNA 분획물을 포함하는 필러 제조방법 및 이로부터 제조된 필러' 국내 특허를 등록하고 PCT 국제출원을 통해 미국 포함 12개국에 출원을 진행 중이다. | 주요언론 | 🟠중 | [약사공론](https://www.kpanews.co.kr/news/articleView.html?idxno=536862) |
| EV-HUM-013 | 파트너십·M&A | 휴메딕스는 인체조직 재생 전문기업 엘앤씨바이오와 hADM 성분 스킨부스터 '엘라비에 리투오' 공급 계약을 체결해 콜라겐·ECM 기반 제품을 상용화했다. | 주요언론 | 🟠중 | [엘앤씨바이오 공지 / 한국경제](http://lncbio.co.kr/bbs/board.php?bo_table=notice&wr_id=196) |
| EV-HUM-014 | 파트너십·M&A | 휴메딕스는 엘앤씨바이오·광동제약 등과 전략적 협업을 맺고, 도움㈜의 '아르케'에 대한 국내 독점 판매 계약 등 유통 파트너십을 확대하고 있다. | 주요언론 | 🟠중 | [팜이데일리 / 휴메딕스 보도자료](https://pharm.edaily.co.kr/News/Read?newsId=01554726645313456) |
| EV-HUM-015 | 파트너십·M&A | 휴메딕스와 같은 휴온스그룹 계열사인 휴온스랩이 재조합 히알루로니다제 SC 플랫폼 '하이디퓨즈'로 항체 및 ADC(항체약물접합체)를 피하주사 제형으로 전환하는 전임상 결과를 확보했으나, 이는 휴메딕스 자체 사업이 아니다. | 주요언론 | 🟠중 | [팜이데일리 / 바이오스펙테이터](https://pharm.edaily.co.kr/news/read?newsId=03043846645380368) |

## 4. 데이터 갭 & 미확인 항목 (정직한 갭 — 시도 내역 포함)

검증관이 '원문접근불가/추론과다/상충' 이슈를 표기했거나 조사관이 honest_gap으로 명문화한 항목의 요약. 각 기업의 아이템 핵심 연관은 별도 상/중 근거로 독립 성립함(§방법론 참조).

| 기업 | 갭/이슈 카드 | 요지 |
|------|:---:|------|
| 3D Systems Corporation (Healthcare) | 4건 | EV-3DS-001(원문접근불가); EV-3DS-007(honest_gap) |
| Advanced BioMatrix, Inc. | 3건 | EV-ABM-002(원문접근불가); EV-ABM-009(honest_gap) |
| Advanced Solutions Life Sciences, LLC | 4건 | EV-ASL-004(원문접근불가/추론과다); EV-ASL-010(honest_gap) |
| Aleph Farms Ltd | 1건 | EV-ALE-007(honest_gap) |
| Aroa Biosurgery Limited | 2건 | EV-ARO-007(honest_gap); EV-ARO-011(추론과다) |
| Artivion, Inc. (구 CryoLife) | 2건 | EV-ART-005(원문접근불가); EV-ART-009(honest_gap) |
| Baxter International Inc. — Advanced Surgery | 2건 | EV-BAX-009(honest_gap); EV-BAX-014(honest_gap) |
| Becton, Dickinson and Company (BD) | 3건 | EV-BD-003(원문접근불가); EV-BD-009(honest_gap) |
| BIO INX | 4건 | EV-BIX-001(원문접근불가); EV-BIX-002(원문접근불가) |
| CELLINK (BICO Group AB) | 3건 | EV-CEL-012(추론과다); EV-CEL-013(honest_gap) |
| Corza Medical | 2건 | EV-COR-008(추론과다); EV-COR-009(honest_gap) |
| Evonik Industries AG — Health Care | 2건 | EV-EVO-003(추론과다); EV-EVO-006(원문접근불가) |
| Geistlich Pharma AG | 4건 | EV-GEI-009(honest_gap); EV-GEI-010(honest_gap) |
| Gelatex Technologies OÜ | 4건 | EV-GLX-009(honest_gap); EV-GLX-011(추론과다) |
| GELITA AG | 2건 | EV-GEL-011(추론과다); EV-GEL-012(honest_gap) |
| Integra LifeSciences Holdings Corporation | 3건 | EV-INT-007(honest_gap); EV-INT-009(honest_gap) |
| Johnson & Johnson MedTech (Ethicon) | 1건 | EV-JNJ-012(honest_gap) |
| Keenova Therapeutics plc (구 Mallinckrodt) | 2건 | EV-KEE-008(honest_gap); EV-KEE-012(honest_gap) |
| Medtronic plc | 2건 | EV-MDT-008(honest_gap); EV-MDT-009(honest_gap) |
| MiMedx Group, Inc. | 2건 | EV-MMX-006(honest_gap); EV-MMX-012(추론과다) |
| Mission Barns, Inc. | 2건 | EV-MIS-005(honest_gap); EV-MIS-009(상충) |
| Mosa Meat B.V. | 4건 | EV-MOS-001(honest_gap); EV-MOS-007(원문접근불가) |
| Nexture Bio, Inc. (formerly Matrix Meats / Matrix Food Technologies) | 6건 | EV-NXT-004(원문접근불가); EV-NXT-008(honest_gap) |
| Nitta Gelatin Inc. | 2건 | EV-NIT-013(추론과다); EV-NIT-014(honest_gap) |
| Organogenesis Holdings Inc. | 4건 | EV-ORG-002(원문접근불가); EV-ORG-007(원문접근불가) |
| RegenHU (REGENHU AG) | 3건 | EV-RGH-007(원문접근불가); EV-RGH-008(원문접근불가) |
| Regenity Biosciences (구 Collagen Matrix, Inc.) | 4건 | EV-RGN-007(원문접근불가); EV-RGN-012(원문접근불가) |
| Rousselot (Darling Ingredients Inc. 브랜드) | 1건 | EV-ROU-009(추론과다) |
| Smith+Nephew plc — Advanced Wound Management | 2건 | EV-SNP-007(상충); EV-SNP-012(honest_gap) |
| Steakholder Foods Ltd. (구 MeaTech 3D Ltd.) | 2건 | EV-STK-006(발췌누락); EV-STK-008(honest_gap) |
| Vericel Corporation | 2건 | EV-VER-007(honest_gap); EV-VER-011(honest_gap) |
| 다나그린 (DaNAgreen Co., Ltd.) | 9건 | EV-DNG-001(honest_gap); EV-DNG-002(원문접근불가) |
| 대웅제약 (Daewoong Pharmaceutical Co., Ltd.) | 4건 | EV-DWG-005(원문접근불가); EV-DWG-010(honest_gap) |
| 로킷헬스케어 (ROKIT Healthcare, Inc.) | 4건 | EV-ROK-003(honest_gap); EV-ROK-005(honest_gap) |
| 셀론텍 (Cellontech, 구 세원셀론텍) | 3건 | EV-CLT-001(원문접근불가); EV-CLT-011(honest_gap) |
| 스페이스에프 (Space F Corp.) | 5건 | EV-SPF-003(honest_gap); EV-SPF-006(honest_gap) |
| 씨위드 (SeaWith, Inc.) | 4건 | EV-SEA-006(원문접근불가); EV-SEA-007(추론과다) |
| 엘앤씨바이오 (L&C Bio Co., Ltd., 290650) | 3건 | EV-LNC-007(추론과다); EV-LNC-010(honest_gap) |
| 주식회사 시지바이오 (CGBio) | 2건 | EV-CGB-010(honest_gap); EV-CGB-013(추론과다) |
| 주식회사 제네웰 (Genewel Co., Ltd.) | 7건 | EV-GNW-001(honest_gap); EV-GNW-002(원문접근불가) |
| 주식회사 제노스 (Genoss Co., Ltd.) | 5건 | EV-GNS-002(honest_gap); EV-GNS-008(원문접근불가) |
| 테고사이언스 (Tego Science, Inc.) | 6건 | EV-TEG-001(원문접근불가); EV-TEG-010(honest_gap) |
| 티센바이오팜 (TissenBioFarm Co., Ltd.) | 5건 | EV-TBF-002(원문접근불가); EV-TBF-003(원문접근불가) |
| 티앤알바이오팹 (T&R Biofab Co., Ltd.) | 6건 | EV-TNR-002(원문접근불가); EV-TNR-006(추론과다) |
| 한스바이오메드 (Hans Biomed Corp.) | 3건 | EV-HAN-012(honest_gap); EV-HAN-016(추론과다) |
| 휴메딕스 (Humedix Co., Ltd.) | 2건 | EV-HUM-012(honest_gap); EV-HUM-016(추론과다) |

> 대표적 공통 갭: (1) 다수 공식 홈페이지·DART·특허 DB가 봇 차단(HTTP 403)으로 원문 직접 페치 불가 → 검색 스니펫·2차 언론·Google Patents로 교차확인 대체. (2) 일부 국내 비상장사/스타트업의 정확한 특허 등록번호·매출 세부는 KIPRIS 인터랙티브 제한으로 미확보(특허 '존재'는 언론·발표로 확인). (3) mTG/ADC '무관' 판정은 검색 부재에 기반한 negative finding으로, 각 시도 검색어를 카드 notes에 명문화함.

## 5. 방법론 & 한계

- **아키텍처**: 오케스트레이터(①)가 48개 기업을 조사관(②, 필수)에 분배 → 증거 카드 617개 생성. 검증관(④, 필수)이 카드만 근거로 상/중/하 판정 → 반려 3건 재조사 루프 → 연관성 분석관(③) 판정 → 리포트(⑤) 종합.
- **출처 위계**: 1차(공식 홈페이지·IR/공시·등록특허·논문·규제기관) > 2차(주요 언론·시장리포트) > 3차(비채택/‘하’).
- **검증 루브릭(§7)**: 상=1차+원문+발췌+최신성/24개월(가능시 2+교차) · 중=신뢰 2차·단일이나 검증가능·24–48개월/부분교차 · 하=미상/접근불가/상충/추론과다/48개월초과.
- **연관도 임계**: match_threshold=중. '무관' 유형은 등급을 '하'로 정규화하여 매칭에서 제외.
- **최신성 창**: 12개월(뉴스·동향). 구조적 사실(사업·특허)은 시점 무관.
- **재조사 루프**: reject_reinvestigate 3건(EV-STK-006/JET-015/TBF-014) → 재조사 1회로 전건 해소(STK 콜라겐 근거 약함 확정·하향, JET/TBF 무관 확정·상향).
- **핵심 한계**: (1) 웹 접근 차단(403)으로 상당수 1차 원문을 2차/스니펫으로 대체 검증 — 등급에 반영(‘중’ 다수). (2) 특허 등록번호 다수 미확보. (3) mTG/ADC 무관은 검색 부재 기반이라 원리상 완전 부정 증명은 아님. (4) 그룹 계열사 파이프라인(예: J&J Innovative Medicine, 대웅-한올바이오파마)은 배정 사업부와 구분해 기록함.

### 핵심 인사이트

1. **Collagen은 이 기업군의 공통 분모** — 44/48이 연관(대부분 직접사업). 콜라겐·젤라틴 원료사(GELITA·Rousselot·Nitta·Evonik·CollPlant), 의료기기 ADM·창상·조직재생(Integra·Geistlich·Aroa·MiMedx·한스바이오메드·엘앤씨바이오·시지바이오·셀론텍 등), 바이오프린팅·배양육 스캐폴드로 삼분된다.
2. **mTG 연관은 '효소 제조'가 아니라 '가교 기질/응용'** — GELITA는 젤라틴-트랜스글루타미나제 의료접착제 특허를 직접 보유(자사 응용), TissenBioFarm은 자사 배양육 특허에 mTG를 명시. Rousselot·Nitta·Aleph는 자사 젤라틴/콜라겐이 mTG 가교의 기질로 쓰이는 접점.
3. **ADC(항체-약물 접합체)는 대체로 무관** — 예상대로 콜라겐/배양육 기업군과 직접 접점이 거의 없다. 유의미한 연관은 제약 계열뿐: J&J(Ambrx 인수로 자체 ADC 파이프라인, 단 MedTech가 아닌 Innovative Medicine 부문), 대웅제약(자회사 한올바이오파마의 Crystal Bioscience 항체 플랫폼 경유, 초기 단계).
4. **mTG↔ADC 교차 접점(부위특이 접합)은 이 48개 기업 중 실사업으로 구현한 곳 없음** — 개념적 연결고리는 존재하나, 본 조사 대상 기업 어느 곳도 mTG를 ADC 접합에 상용 공급/응용하지 않는 것으로 확인.

---
*생성: CIRV 하니스 · 2026-07-06 · 감사 데이터셋 48개 기업 / 617 증거 카드 / 617 검증 레코드 / 144 연관성 레코드.*
