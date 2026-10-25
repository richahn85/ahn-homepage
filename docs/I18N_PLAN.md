# 다국어(EN·中文·日本語) 사이트 계획

## 1. 구조
- 하위 폴더 방식: `/en/`, `/zh/`(간체), `/ja/`. 한국어는 루트 그대로 둔다.
- 1단계 범위(핵심 축소판): 홈, 소개, 강의·특강, 기업 자문, 실적(목록), 문의, 감사 페이지.
  - `/en/` `/en/about/` `/en/executive-education/` `/en/advisory/` `/en/cases/` `/en/contact/` `/en/thank-you/`
  - zh·ja도 같은 경로.
- 2단계 후보: AI 전환, 공공·연구, 실적 상세 2건(현대백화점 CRM, 스마트관광도시).
- 옮기지 않음: 회원가입, 다운로드, 칼럼·카드뉴스, 굿슬립랩, 파르팜 등 국내 독자용 콘텐츠.

## 2. 연계
- 헤더 오른쪽에 `KO · EN · 中文 · 日本語` 전환. 각 언어판의 같은 페이지로 1:1 연결(없으면 그 언어 홈).
- 모든 짝 페이지에 `hreflang`(ko, en, zh-Hans, ja, x-default=ko).
- `og:locale`: ko_KR · en_US · zh_CN · ja_JP.
- sitemap.xml에 언어별 URL 추가.
- 문의 폼: Netlify Forms 이름을 `contact-en` · `contact-zh` · `contact-ja`로 나눠 출처 구분.
- 모바일 하단 문의 바(v2.js)는 `<html lang>`을 읽어 문구를 바꾼다.
- 공용 스타일은 `assets/i18n.css`(언어 전환·라틴/한자 폰트 보정)에 둔다.

## 3. 용어집 (확정 전 초안 — 교수님 검수 필요)

| 한국어 | English | 中文(简体) | 日本語 |
|---|---|---|---|
| 안영찬 | Youngchan Ahn | 安永灿 (간체, 확정) | 安永燦（アン・ヨンチャン）(확정) |
| 동국대학교 경영대학원 교수 | Professor, Graduate School of Business, Dongguk University | 东国大学经营研究生院 教授 | 東国大学校 経営大学院 教授 |
| 국가기술표준원 선정 국제표준 전문가 | International Standards Expert designated by the Korean Agency for Technology and Standards (KATS) | 韩国国家技术标准院（KATS）认定 国际标准专家 | 韓国国家技術標準院（KATS）選定 国際標準専門家 |
| Management Transformation Advisor | (고정) | 经营变革顾问 (Management Transformation Advisor) | 経営変革アドバイザー (Management Transformation Advisor) |
| THINKING INTO ACTION | (고정, 번역 안 함) | 同左 | 同左 |
| Technology Changes. People Come First. | (고정) | 同左 + 부제 번역 | 同左 + 부제 번역 |
| 강의·특강 | Lectures (Executive Education) | 讲座·培训 | 講演・研修 |
| 기업 자문 | CEO Advisory | 企业咨询 | 経営顧問 |
| AI 전환 | AI Transformation | AI 转型 | AI トランスフォーメーション |
| 실적 | Selected Work | 项目业绩 | 実績 |
| 소개 | About | 简介 | プロフィール |
| 문의하기 | Contact | 联系咨询 | お問い合わせ |
| 중대재해처벌법 | Serious Accidents Punishment Act (Korea) | 韩国《重大灾害处罚法》 | 韓国「重大災害処罰法」 |
| 안전보건공시제 | Occupational Safety & Health Disclosure System | 安全保健公示制度 | 安全保健公示制度 |
| 고객만족경영 | Customer Satisfaction Management | 顾客满意经营 | 顧客満足経営 |
| 현대백화점 | Hyundai Department Store | 现代百货 | 現代百貨店 |
| 한국관광공사 | Korea Tourism Organization | 韩国观光公社 | 韓国観光公社 |
| 전화 02-2260-1651 | +82-2-2260-1651 | 同左 | 同左 |

### 확정 표기 (2026-10-26 교수님 확인)
| 한국어 | English |
|---|---|
| 미래융합 | Future Design |
| 대한경영학회 | The Korean Academic Association of Business Administration |
| 비콘코리아 | BCK Consulting Group (formerly BCon Korea) — 일본 비즈니스 컨설턴트(BCon) 한국법인에서 출발한 OD·HRD 컨설팅사 |
| 소방학교 | Central Fire Service Academy (중앙소방학교) |

### 영문판 참고 사항
- 동양제과·태평양화학 → 당시 사명 그대로 "Tongyang Confectionery", "Pacific Chemical"
- 강사 프로필 PDF는 한국어본뿐이라 영문판에서 뺐음 (영문 PDF가 생기면 추가)
- 실적 상세 2건은 한국어만 있어 영문판 카드는 링크 없이 둠 (2단계에서 번역)

## 4. 현지화 원칙
- EN: 문제 해결 사례와 역할(“what I did”)을 앞세운다. 짧은 문장.
- 中文: 기관·기업 협력 이력과 직함을 앞세운다. 정중한 서면체.
- 日本語: 겸양 표현과 구체적 실적. です・ます체.
- 기업명은 각 사의 공식 외국어 표기를 쓴다.

## 5. 배포
- 로컬 미리보기 → `scripts/deploy_v3.py preview` → 교수님 확인 → production.
- 한국어 페이지에 언어 전환 링크를 넣는 작업은 en·zh·ja 1단계가 모두 준비된 뒤 한 번에 한다.

## 6. 진행 현황 (2026-10-26)
- 완료(로컬): `/en/` `/zh/` `/ja/` 1단계 7개 페이지씩, 총 21개. 각 페이지 헤더에 KO·EN·中文·日本語 전환, hreflang 4개 언어 + x-default.
- 중·일문 페이지는 스크래치 스크립트로 생성 후 HTML을 직접 관리 (build.py와 무관).
- 휴대폰 화면(≤560px)에서는 언어 링크 4개 때문에 헤더의 문의 버튼을 숨기고, 하단 고정 문의 바로 대신함.
- 문의 폼: `contact-en` · `contact-zh` · `contact-ja`. 중·일문 폼에 "현지어로 써도 되며 답장은 영어·한국어"라고 안내함.
- 이름 한자 확정: 安永燦 (중국어판은 간체 安永灿).
- 한국어 6개 페이지(홈·소개·강의·자문·실적·문의)에 언어 전환과 hreflang 추가, sitemap에 18개 URL 추가.
