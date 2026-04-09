# YouTube 자동 업로드 OAuth 설정 가이드

Phase E 비디오 파이프라인이 블로그 → 비디오 → YouTube 업로드를 수행하려면
YouTube Data API v3 에 대한 OAuth 2.0 Desktop 자격 증명이 필요합니다. 1회
설정이며, 이후 `~/.config/aiblog/youtube_token.json` 에 저장된 refresh
token 을 통해 daemon 이 자동 갱신·사용합니다.

## 사전 요건

- YouTube 채널이 연결된 본인 Google 계정
- Google Cloud Console 접근 권한 (개인 계정으로 충분)

## Step 1 — GCP 프로젝트 생성

1. <https://console.cloud.google.com> 접속 → 상단 프로젝트 선택기 → **NEW PROJECT**
2. Name: `aiblog-youtube` (아무거나)
3. **CREATE**

## Step 2 — YouTube Data API v3 활성화

1. 왼쪽 상단 햄버거 → **APIs & Services → Library**
2. 검색: `YouTube Data API v3`
3. 카드 진입 → **ENABLE**

## Step 3 — OAuth 동의 화면 구성

1. **APIs & Services → OAuth consent screen**
2. **User Type: External** 선택 → Create
3. App name: `aiblog local uploader`
4. User support email: 본인 Google 계정
5. Developer contact: 본인 Google 계정
6. **SAVE AND CONTINUE**
7. **Scopes** → `Add or remove scopes` → 필터 `youtube.upload` → 체크 →
   `https://www.googleapis.com/auth/youtube.upload` 추가 → Update →
   **SAVE AND CONTINUE**
8. **Test users** → **+ Add users** → 본인 Google 계정 이메일 입력 → Add →
   **SAVE AND CONTINUE**
9. **Back to Dashboard**

**주의:** Publishing status 는 `Testing` 으로 두어도 본인 계정이라면
토큰 만료 없이 무기한 사용할 수 있습니다. `In production` 으로 전환
하려면 Google 의 검증 절차를 거쳐야 하므로, 본인만 사용하는 경우
Testing 모드를 유지하세요.

## Step 4 — OAuth 2.0 Desktop 클라이언트 생성

1. **APIs & Services → Credentials**
2. **+ CREATE CREDENTIALS → OAuth client ID**
3. Application type: **Desktop app**
4. Name: `aiblog desktop`
5. **CREATE** → 확인 창 나오면 **DOWNLOAD JSON**
6. 다운로드된 파일 (`client_secret_*.json`) 의 경로를 기억

## Step 5 — 자격 증명 파일 배치

```bash
mkdir -p ~/.config/aiblog
mv ~/Downloads/client_secret_*.json ~/.config/aiblog/client_secrets.json
ls -la ~/.config/aiblog/
```

(파일 이름이 정확히 `client_secrets.json` 이어야 합니다. `config.py`
에서 이 이름을 찾습니다.)

## Step 6 — 첫 OAuth 플로우 실행

Admin UI `/videos` 에서 수동 업로드를 시도하거나, daemon 이 자동 트리거
하여 업로드를 시도하는 순간, `YouTubeUploaderAgent` 가 브라우저 창을
띄우고 본인 Google 계정에 로그인하도록 안내합니다.

1. "This app isn't verified" 경고 → **Advanced** → **Go to aiblog local
   uploader (unsafe)** (본인 앱이므로 안전합니다)
2. Google 계정 선택 → Continue
3. `youtube.upload` 권한 요청 → **Continue**
4. 브라우저에 "The authentication flow has completed" 표시
5. 터미널에서는 자동으로 `~/.config/aiblog/youtube_token.json` 이 생성되며
   이후 업로드는 무인 동작합니다.

## 문제 해결

### 할당량 초과 (`quotaExceeded`)

- YouTube Data API v3 의 기본 일일 할당량은 10,000 units 입니다.
- 업로드 1 건 ≈ 1,600 units → 일 최대 약 6 건 업로드 가능합니다.
- `settings.youtube_upload_daily_cap` (기본 5) 로 하드 리밋이 걸려 있어
  이를 초과하면 자동 업로드가 대기열에서 멈춥니다.
- 필요 시 GCP 콘솔의 Quotas 페이지에서 할당량 증가 요청이 가능합니다.

### 토큰 만료

- refresh token 은 Testing 모드에서 7 일 후 만료될 수 있습니다.
- 만료되면 daemon 로그에 `invalid_grant` 가 남고, 다음 실행 시 다시 Step 6
  의 브라우저 플로우가 열립니다. 이때 한 번 재승인 해주세요.

### `client_secret not found`

- `~/.config/aiblog/client_secrets.json` 경로와 파일명을 정확히 확인하세요.
- 파일 권한은 600 이 권장됩니다: `chmod 600 ~/.config/aiblog/client_secrets.json`
