# AHNYOUNGCHAN.KR V2 — 구현 및 검증 보고서

작성일: 2026-09-06

최종 검토용 배포: https://6a9d6c87fe5c8a9d21956308--ahn-youngchan-homepage.netlify.app/

운영 발행: 사용자 승인 후 2026-09-06 https://ahnyoungchan.kr 에 공개했습니다. Production deploy ID: `6a9d6d1cd0aeb9a6808eb45e`. 아래 구현 보고서의 미발행 표기는 최초 검토본 기준이며, 현재 운영 배포는 완료되었습니다. GitHub commit/push는 수행하지 않았습니다.

## 결과와 공개 상태

기존 HTML·Netlify 구조를 유지하며, 개인 브랜드 중심의 메인 10개 섹션과 총 20개 정적 페이지를 구현했습니다. 별도 SPA 또는 프레임워크를 추가하지 않았습니다. 검토용 Netlify 배포를 생성했으며 운영 도메인의 production 배포와 GitHub main은 변경하지 않았습니다.

## 변경한 기존 파일

- `index.html`: 메인 10개 섹션, 6개 메뉴, 자문 중심 CTA, 인물 사진, 서비스 3개, 사례 6개, Insights·Brief·People First·문의 재배치.
- `netlify.toml`: 운영에서 확인한 카드뉴스 3개 주소의 외부 이동을 명시적 301로 보존.

## 새 파일

- 공통 표시: `assets/legacy.css`, `assets/v2.css`, `assets/v2.js`.
- 원본 보존 및 콘텐츠 데이터: `content/legacy.json`, `content/cases.json`, `content/articles.json`.
- 상세 페이지: 아래 URL 각각의 `index.html`.
- 검색: `sitemap.xml`, `robots.txt`.
- 재생성·검증·배포 패키징: `scripts/build.py`, `scripts/check.py`, `scripts/qa.cjs`, `scripts/package.py`.
- 기록: `V2_AUDIT.md`, `V2_DELIVERY.md`.

삭제한 파일: 없음. 작업 시작 전에 수정되어 있던 홈페이지는 별도 로컬 스냅샷과 `content/legacy.json`으로 보존했습니다. 기존 `seminar/`와 `safety-disclosure-seminar-20260720/` 파일, PDF, 원본 WebP, `thank-you.html`은 수정하지 않았습니다. 이 두 세미나 디렉터리는 작업 시작 때부터 Git 미추적 상태였습니다.

## 새 URL

- `/about`
- `/advisory`
- `/ax-transformation`
- `/executive-education`
- `/cases`
- `/cases/k-bpi`
- `/cases/hyundai-crm`
- `/cases/b2b-marketing`
- `/cases/smart-tourism`
- `/cases/safety-management`
- `/cases/ai-transformation`
- `/insights`
- `/insights/safety-part-3`
- `/insights/safety-part-4`
- `/insights/safety-part-5`
- `/professors-question`
- `/ax-management-brief`
- `/people-first`
- `/contact`

Netlify는 디렉터리 URL을 trailing slash 형태로 정규화합니다.

## Redirect와 기존 주소

- `/safety-cardnews-part5-20260731/*` → `https://safety-cardnews-part5-20260731.netlify.app/:splat` (301)
- `/safety-cardnews-part4-20260721/*` → `https://safety-cardnews-part4-20260721.netlify.app/:splat` (301)
- `/safety-cardnews-part3-20260709/*` → `https://safety-cardnews-part3-20260709.netlify.app/:splat` (301)
- 메인 `#support` → `/people-first#support`, `#expertise` → `/ax-transformation#expertise`, `#cardnews-series` → `/insights#cardnews-series`. Fragment는 서버에 전송되지 않아 JS로 이동합니다.
- `#subscribe`, `#services`, `#proof`, `#career`, `#probono`, `#contact`, `#top`는 메인에 유지됩니다.
- 기존 세미나·PDF·카드뉴스 PNG 다운로드 주소를 보존했습니다.

## 유지한 기능

- Netlify `subscribe`, `contact` 폼 이름, POST `/thank-you`, `form-name`, `subject`, `bot-field` honeypot.
- 구독 `name/org/email/phone/plan`, 문의 `name/org/email/type/message` 필드 이름.
- 구독 플랜 가격, 서비스 기준가, Pro Bono 프로그램, 후원 계좌·복사, 공식 및 개인 이메일, YouTube 링크.
- 기존 경력·학력·연구·보고서·기업명과 전문분야 콘텐츠. 운영본에서 로컬보다 추가된 카드뉴스 공지도 함께 보존.

## 변경한 기능과 UX

- 문의 유형을 요청한 6개 카테고리로 표시하고 소속을 필수로 지정했습니다. 기존 자문·컨설팅·특강·사회공헌의 저장 값은 최대한 유지하고 연구/공공·언론 유형만 새 값을 사용합니다.
- 구독 폼·가격은 브리프 상세, 후원 정보는 People First 상세, 개인 이메일은 About으로 이동했습니다.
- 홈 서비스는 3개, 대표 사례는 6개입니다. 구독은 Insights 이후에 배치했습니다.
- 개인정보·프로젝트 성과를 새로 추정하지 않았습니다. 원본에 없는 사례의 세부 서술은 자료 확인 상태로 남겼습니다.

## SEO

20개 페이지에 고유 제목·설명·canonical·Open Graph를 설정했습니다. Person·WebSite·BreadcrumbList, 서비스 3개의 Service, 기존 카드뉴스를 소개하는 내부 글 3개의 Article JSON-LD를 추가했습니다. Article에는 작성자 안영찬, 원본 공지의 발행일, V2 편집일, 설명·이미지·canonical을 포함했습니다. 안전 카드뉴스 원문은 기존 사이트로 연결됩니다.

신규 Professor’s Question은 제공된 질문만 게시하고, 작성되지 않은 해설이나 발행일을 창작하지 않았습니다. 칼럼·연구 원문이 없는 부분에는 자료 정리 상태와 실제 관련 경로를 표시했습니다. 향후 실질적인 본문·발행일이 준비되면 같은 콘텐츠 모델로 확장할 수 있습니다.

원본 HTML에 analytics 태그는 발견되지 않았습니다. 호스팅 측 analytics·폼 알림 설정은 변경하지 않았습니다.

## 모바일·접근성

320/390/1440px에서 메뉴·그리드·한글 줄바꿈·가격표를 점검했습니다. 모든 신규 페이지는 h1 하나, 주요 이미지 alt, visible label, focus 스타일, skip link를 갖습니다. 메뉴에는 aria-expanded/aria-controls 및 Escape 닫기가 있고 JavaScript가 꺼져도 메뉴를 노출합니다. 폼은 native required/email 검증을 유지합니다. 후원 계좌 복사는 실패 시 수동 복사 안내를 제공합니다. reduced-motion을 존중합니다.

## Build / Test

- `python scripts/build.py`: 20페이지 생성 성공.
- `python scripts/check.py`: 20개 경로·내부 링크·fragment, 기존 외부 링크 6개, Netlify 필드 계약, 메인 섹션 10개, 메인 가격/후원계좌 비노출 검사 통과.
- `node scripts/qa.cjs`: Chrome/Playwright로 20개 페이지 × 3개 viewport, 총 60개 조합 검사 통과. 가로 넘침, 누락 alt, 로드 실패 이미지, visible label 누락, JS 오류 없음. 메뉴 열림/Escape 닫기, 빈 필수 폼 검증 통과.
- 홈페이지 desktop/mobile 및 브리프·People First 상세를 스크린샷으로 시각 검토했습니다.
- 미리보기의 홈/About/문의/브리프/안전 콘텐츠/기존 카드뉴스 redirect/접수 완료 경로 HTTP 200 확인.
- 실제 상담·구독 신청은 전송하지 않았습니다. Netlify 수신·이메일 알림과 신규 유형 처리의 end-to-end 확인은 운영 승인 후 별도 검증이 필요합니다.
- 추가 확인: 후원 계좌 복사의 성공/권한 거절 처리, 구독 폼의 빈 필수 입력 거절 및 유효 입력 허용, `git diff --check` 통과.
- agent-browser CLI가 설치되어 있지 않아 사용 가능한 Playwright와 설치된 Chrome으로 동등한 브라우저 검증을 수행했습니다.

## 성능 확인의 범위

클라이언트 라우터·추가 런타임 의존성 없음. 공통 JS 약 1.2KB, CSS 약 26KB, 기존 메인 인물 WebP 약 92KB. Hero 이미지는 높은 우선순위로 로드하고 하단 이미지는 lazy loading을 사용합니다. 테스트 환경의 로컬 390px 단일 측정은 LCP 약 444ms, CLS 약 0.0034였습니다. 이는 실제 모바일 네트워크·CrUX 수치나 Lighthouse 인증 결과가 아닙니다. 실제 방문자 Core Web Vitals는 공개 후 측정해야 합니다.

## 사실 확인과 TODO

1. ‘국내 최초 7건+’와 실제 목록 8개 불일치. `content/cases.json`에 원본 값·목록 수·검증 대기 상태·Evidence URL 배열을 보존했습니다. 8건+로 임의 교정하지 않았습니다.
2. 30년+, 200개사+, 30편+ 및 ‘최초’ 개별 근거, 경력의 현재성은 외부 증빙 검증이 필요합니다.
3. Case BACKGROUND/PROBLEM/APPROACH/RESULT/LESSON, 정확한 기간·역할·결과와 Evidence 문서·URL 제공이 필요합니다. EXECUTION은 기존 공개 문구 또는 사용자 제공 내용을 사용했습니다.
4. 공개된 최근 AX Brief 호수/PDF를 확인하지 못해 ‘최근 호’로 위장하지 않고 구성 미리보기를 제공합니다.
5. Professor’s Question 해설·Column·연구 원문은 후속 편집 대상입니다. 존재하지 않는 본문·성과·후기·언론 보도는 생성하지 않았습니다.
6. 기존 서비스 가격·1영업일 회신·구독 및 후원 운영 약속은 원본 그대로 보존했으므로 최신 운영 정책 확인이 필요합니다.
7. 운영 공개 전 검토용 미리보기 최종 확인. production 배포 및 Git commit/push는 수행하지 않았습니다.

## 10초 이해 검토

정보 구조 검토의 답은 **YES**입니다. 첫 화면에 안영찬·교수/컨설턴트 정체성, 30년의 경영혁신 경험, AI를 경영성과로 연결하는 가치, CEO·기업 자문 CTA를 함께 배치했습니다. 이는 실제 CEO 사용자 테스트 결과는 아니며 설계·화면 검토 판단입니다.

## 재생성과 편집

공통 마크업은 `scripts/build.py`, 스타일은 `assets/v2.css`, 기존 콘텐츠는 `content/legacy.json`에서 관리합니다. `content/cases.json`과 `content/articles.json`은 현재 빌더가 생성하는 편집용 데이터 산출물이므로 개별 수정 시 빌더에도 반영해야 합니다. 빌드 후 `check.py`, `qa.cjs`를 실행하고 `package.py`로 공개 파일만 패키징합니다.
