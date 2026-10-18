# Authority Edit — 2026-09-06

최종 미리보기: https://6a9d789705b0a4efddc59191--ahn-youngchan-homepage.netlify.app/

운영 발행 완료: 사용자의 명시적 승인 후 2026-09-06 https://ahnyoungchan.kr 에 게시했습니다. Production deploy ID: `6a9d79abdd6590536df79f13`. 아래 공개 상태 문단은 최초 승인 대기 당시의 기록이며 현재는 발행 완료 상태입니다.

## 구현 결과

- 기존 Deep Navy·Blue·Ivory, 폰트, 사진, 메뉴와 레이아웃 언어 유지.
- 메인 10 → 7개 섹션: Hero / Authority / What I Do / Selected Work / Signature Thinking / About & Philosophy / Contact.
- Hero 본문과 부제 유지. 이름·Advisor·교수·국제표준 전문가를 한 번씩 배치. 미래융합 직함은 About에 유지. CTA는 자문·협력 문의와 대표 프로젝트.
- 미검증 숫자 200개사+, 30편+, 국내 최초 공개 제외. 기관 기반 credential과 실제 경력서에 등장하는 기관 10개로 대체.
- 독립 Evolution·Brief 섹션 제외. About & Philosophy 안의 짧은 timeline, Insights 안의 작은 Brief 링크로 재배치.
- CEO Advisory는 When to Call / Discussion Areas / How We Work / Selected Experience / Contact로 집중. 반복 프로그램·서비스 가격표 제거.
- 교육 가격 제거, 대상·과제·산출물 중심으로 편집. 원래 가격은 content/legacy.json에 보존.
- AX-01~06 대신 Management Capabilities 4개 축 적용.
- 교수의 질문 1개와 100~180자 관점, 상세 해설을 편집. 제공된 브랜드 철학을 바탕으로 이번 작업에서 새로 작성한 문장으로, 기존 발행 원고나 과거 발언 인용으로 취급하지 않음.
- 비어 있는 Column·Research 안내·Brief 미리보기 제외. 실제 카드뉴스·구독 기능 유지.
- 후원 계좌·복사 버튼·모금 문구 제거. Pro Bono 활동 유지.
- 공통 Footer는 About / Insights / Contact와 공식 이메일. 과거 세미나 HTML 두 페이지에서도 개인 Gmail 표시 제거.

## 사례와 근거

공개 2건: 현대백화점 CRM, 한국관광공사 스마트관광도시 구축 매뉴얼.

원본 `C:/Users/USER/Documents/2026 DUICA/2026 안영찬교수 경력서.pdf`를 직접 읽고 확인했습니다. 현대백화점: 2·7·9쪽의 CRM PM, 고객만족도 조사 수주, 후속 2년 수행. 한국관광공사: 2·8쪽의 가이드라인/매뉴얼 제작 컨설팅. 자기 작성 경력서에 기록된 내용에 대한 확인이며, 발주기관의 독립적인 증명 확인을 의미하지 않습니다. 이 출처를 공개 사례 하단에 명시했습니다. ‘국내 최초’, 프로젝트 날짜, 매출·ROI·고객 후기 등은 추가하지 않았습니다. 오늘의 경영에 대한 의미는 해석 문단으로 구분했습니다. 개인정보가 포함된 CV 전체 파일은 배포하지 않았습니다.

공개 목록에서 제외한 4건: K-BPI, B2B Marketing, Safety Management, AI Transformation. 원본 HTML은 `content/drafts/`에 보존하고 배포에서 제외했습니다. 기존 URL에는 공개 사례 안내를 제공하며 `noindex,follow`를 지정했습니다. 내부 navigation과 sitemap에는 포함하지 않았습니다. 과거 사례 데이터는 content/cases.json에도 남아 있습니다.

## 변경 파일

- 재생성: index.html, 기존 상세 19개 index.html, sitemap.xml, robots.txt.
- 수정: scripts/build.py, scripts/check.py, assets/v2.css, assets/v2.js, seminar/20260720/index.html, seminar/20260720/summary-download.html.
- 추가: scripts/authority.py, content/authority.json, content/drafts/ 아래 HTML 4개, 본 보고서.
- 기존 실제 콘텐츠 파일 삭제 없음. 폼 name/method/action/필드명, 구독 plan 값, 카드뉴스 외부 주소, 세미나·다운로드 파일 유지.

## 검증

- build: sitemap 포함 16개 공개 페이지 + 기존 URL 대응 noindex 4개.
- static checks: 7개 섹션, 공개 사례 2개, 요약 100~180자, 초안 링크 제외/noindex, 폼 계약, 내부 주소, 주요 다운로드/외부 주소 유지, 준비중 문구·후원계좌·개인메일·가격 금지 범위 검사 통과.
- browser: 20개 경로 × 1440/390/320px = 60개 조합 검사 통과. 가로 넘침, h1 누락/중복, 이미지 실패, alt·label 누락, JS 오류 없음. 메뉴/Escape/required 검증 통과.
- 홈페이지 desktop/mobile, Advisory, 사례, essay 시각 검토 완료. 마지막 변경은 확인된 문장의 축약과 기존 세미나 이메일 제거였으며 static/link 검사 재실행 통과.
- 실제 문의·구독 접수는 전송하지 않았습니다.

## 최종 다섯 질문

화면·문구에 대한 편집 검토 기준으로 모두 YES: 첫 화면의 정체성 / 교수·Senior Advisor 포지션 / 전문가 중심 / 개발상태 문구 없음 / 30년 Management Transformation과 AI 시대 경영 판단의 일관성. 실제 방문자 테스트를 뜻하지 않습니다.

## 공개 상태

운영 배포 시도는 자동 승인 검토가 거절했습니다. 최신 사용자 메시지에 이번 Authority Edit의 production 공개에 대한 명시적 승인이 필요하다는 이유였습니다. 운영 배포는 수행되지 않았습니다. 검토용 미리보기만 생성하며, 사용자 승인 후 해당 최종 파일로 공개 가능합니다. 이전 V2 운영 배포는 그대로 유지됩니다.
