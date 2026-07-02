# 안영찬 홈페이지 배포본

GitHub 저장소와 Netlify 자동 배포에 바로 연결할 수 있는 정적 홈페이지입니다.

## 파일 구성

- `index.html`: 메인 홈페이지
- `thank-you.html`: 구독 신청 또는 문의 제출 후 이동하는 접수 완료 페이지
- `assets/`: 홈페이지 이미지 파일
- `netlify.toml`: Netlify 정적 배포 설정

## GitHub + Netlify 배포 절차

1. GitHub에서 새 저장소를 만듭니다. 예: `ahn-homepage`
2. 이 폴더의 모든 파일을 저장소 루트에 업로드합니다.
3. Netlify에서 `Add new site` - `Import an existing project`를 선택합니다.
4. GitHub 저장소를 연결합니다.
5. Build command는 비워두고, Publish directory는 `.`로 둡니다.
6. 배포 후 Netlify의 Forms 메뉴에서 `subscribe`, `contact` 폼이 감지되었는지 확인합니다.
7. 제출 알림을 받으려면 Netlify의 Notifications에서 이메일 알림을 추가합니다.

## 수정 및 자동 배포 절차

1. `index.html` 또는 필요한 파일을 수정합니다.
2. Git에 커밋합니다.
3. `main` 브랜치에 push합니다.
4. Netlify가 GitHub 저장소 변경을 감지해 자동으로 production 배포합니다.
5. 배포 후 `https://ahnyoungchan.kr`에서 반영 상태를 확인합니다.

## 폼

`index.html`에는 Netlify Forms가 감지할 수 있도록 두 개의 폼이 설정되어 있습니다.

- `subscribe`: 리포트 구독 신청
- `contact`: 특강, 자문, 컨설팅 문의

두 폼 모두 스팸 방지용 honeypot 필드와 접수 완료 페이지(`/thank-you`) 이동이 포함되어 있습니다.
