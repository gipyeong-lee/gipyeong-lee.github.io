---
layout: post
title: "내 컴퓨터의 비밀번호를 AI가 훔쳐볼까? OpenAI Codex의 민감 파일 접근 문제"
description: "개발자들이 사용하는 OpenAI의 코드 작성 AI, Codex가 내 소중한 비밀 키나 환경 설정 파일을 마음대로 읽지 못하게 할 방법은 없을까요? 현재 논의 중인 보안 이슈를 정리해 드립니다."
summary: "OpenAI의 Codex CLI가 개발자의 민감한 파일을 자동으로 접근하는 문제가 지속적으로 제기되고 있으며, 현재 이를 원천 차단하는 공식 기능은 부재해 보안 주의가 필요합니다."
tags: [AI보안, 개발도구, OpenAI, Codex, 데이터프라이버시]
image: 2026-06-28-A-way-to-exclude-sensitive-files-issue-still-open-for-OpenAI-Codex.jpg
image_alt: "컴퓨터 화면 속 AI 코딩 도구가 파일을 분석하는 모습과 자물쇠 아이콘이 함께 있는 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "편리함이 보안을 앞지를 때 사고는 발생합니다. 공식적인 제외 기능이 마련될 때까지는 사용자가 스스로 보안 장벽을 높이는 지혜가 필요합니다."
quiz:
  - question: "OpenAI Codex CLI가 현재 작업 디렉토리 내 파일을 처리하는 기본 방식은?"
    choices: ["매번 사용자의 승인을 받는다", "사용자 승인 없이 읽기 및 수정이 가능하다", "무조건 모든 파일을 외부로 전송한다"]
    answer: 1
    explanation: "Codex는 기본 승인 모드에서 작업 디렉토리 내 파일을 자동으로 읽고 수정할 수 있습니다."
  - question: "현재 Codex에서 민감한 파일(예: .env) 접근을 막기 위해 가장 권장되는 임시 방편은?"
    choices: ["설정 파일에서 제외 옵션 사용", "샌드박스 환경 격리 또는 파일 권한 제한", "AI 모델 삭제"]
    answer: 1
    explanation: "공식 제외 기능이 없기에 현재는 파일 접근 권한을 막거나 샌드박스 등을 이용한 격리가 최선입니다."
  - question: "Codex가 AI 모델로 정보를 보내는 방식은?"
    choices: ["사용자가 선택한 파일만 보냄", "도구 실행 결과에 파일 내용을 포함해 업로드", "전혀 파일 내용을 보내지 않음"]
    answer: 1
    explanation: "Codex는 도구 실행 결과를 업로드하며, 이 과정에서 접근한 파일 내용이 포함될 수 있습니다."
lang: ko
ref: 2026-06-28-A-way-to-exclude-sensitive-files-issue-still-open-for-OpenAI-Codex
audio: 2026-06-28-A-way-to-exclude-sensitive-files-issue-still-open-for-OpenAI-Codex.mp3
permalink: /2026/06/28/A-way-to-exclude-sensitive-files-issue-still-open-for-OpenAI-Codex/
---

상상해보세요. 당신은 똑똑한 AI 비서에게 코딩을 맡기고 커피 한 잔을 마시러 갔습니다. AI는 당신의 코드를 훌륭하게 완성했지만, 그 과정에서 당신의 이메일 계정 비밀번호나 API 연결 키가 담긴 `.env` 파일까지 읽어 들였다면 어떨까요? 최근 개발자 커뮤니티에서는 OpenAI의 코딩 AI 도구인 'Codex(코덱스)'의 이러한 보안 취약점이 큰 화두로 떠오르고 있습니다.

### 이게 왜 중요한가요?

개발자들은 프로젝트를 진행할 때 중요한 접속 정보나 보안 키를 `.env` 파일 같은 곳에 저장합니다. 이 파일들은 일종의 '디지털 열쇠'와 같습니다. 그런데 코딩을 도와주는 AI인 Codex가 이런 파일을 읽을 수 있다면, 소중한 개인 정보가 개발자도 모르는 사이에 AI 모델의 학습 데이터로 유출되거나 외부 서버로 전송될 위험이 있다는 우려가 제기됩니다. [출처: Add ability to hide sensitive files from agent · Issue #85](https://github.com/openai/codex/issues/300/linked_closing_reference?reference_location=REPO_ISSUES_INDEX) Codex는 도구 실행 결과를 처리할 때, 접근한 파일의 내용을 함께 업로드하는 방식을 취하고 있어 각별한 주의가 필요합니다. [출처: A way to exclude sensitive files issue still open for OpenAI ...](https://news.ycombinator.com/item?id=48706714)

### 쉽게 이해하기

비유하자면, Codex는 현재 당신의 '열성적인 사서'와 같습니다. 원래는 제가 지정한 코드 파일만 가져와야 하는데, 사서가 너무 열정적인 나머지 서재 구석에 숨겨둔 민감한 파일까지 전부 펼쳐보고 있는 상황과 유사합니다.

더 큰 문제는 "이런 파일은 보지 마"라고 사서에게 미리 금지 구역을 지정할 수 있는 공식적인 기능 자체가 현재 부재하다는 점입니다. [출처: A way to exclude sensitive files · Issue #2847 · openai/codex](https://github.com/openai/codex/issues/2847) Codex는 기본 승인 모드에서 사용자의 승인을 따로 받지 않고도 작업 디렉토리 안의 파일을 자유롭게 읽고 수정할 수 있습니다. [출처: Codex can read sensitive files outside the CWD without ...](https://developers.openai.com/codex/agent-approvals-security) 물론 작업 영역 밖으로 나가거나 네트워크 연결이 필요한 명령을 실행할 때는 사용자의 승인을 요구하지만, 파일 접근 자체에 대한 제어는 한계가 있는 상태입니다. [출처: Codex can read sensitive files outside the CWD without ...](https://developers.openai.com/codex/agent-approvals-security)

### 현재 상황

개발자들 사이에서는 특정 파일을 AI가 읽지 못하게 하는 설정(예: `.codexignore`)이 필요하다는 요구가 빗발치고 있습니다. [출처: Ignore files feature, e.g. ".codexignore" · openai codex ...](https://github.com/openai/codex/discussions/3456) 그러나 OpenAI 측에서는 아직 이를 위한 공식적인 대응책을 마련하지 못한 상태입니다. [출처: A way to exclude sensitive files · Issue #2847 · openai/codex](https://github.com/openai/codex/issues/2847)

전문가들은 현재 이 문제를 해결하기 위해 AI 프로세스가 민감한 파일에 접근하지 못하도록 원천 차단하는 방법을 권장합니다. 파일을 아예 다른 폴더로 옮기거나, 유닉스(컴퓨터 운영체제)의 파일 권한 설정을 강화하거나, 샌드박스(외부와 차단된 안전한 가상 공간)에서 작업을 수행하는 것이 현재로서는 가장 확실한 방법입니다. [출처: A way to exclude sensitive files issue still open for OpenAI ...](https://news.ycombinator.com/item?id=48706714)

### 앞으로 어떻게 될까?

이 문제는 현재 오픈소스 커뮤니티에서 계속해서 논의되고 있으며, 더 안전한 설계를 요구하는 목소리가 높습니다. [출처: [SECURITY!] Do not allow Codex to read whole filesystem by ...](https://github.com/openai/codex/issues/4410) 미래에는 사용자가 일일이 수동으로 제어하는 방법 대신, 설정 파일로 AI의 접근을 간단히 차단할 수 있는 공식적인 '제외(Exclusion)' 기능이 추가될 가능성이 있습니다. 개발자들은 Codex를 사용할 때 최신 업데이트 내용과 보안 관련 변경 사항을 주기적으로 확인해야 합니다. [출처: How to prevent OpenAI Codex CLI from accessing `.env` files?](https://askai.glarity.app/search/How-to-prevent-OpenAI-Codex-CLI-from-accessing---env--files)

---

**MindTickleBytes의 AI 기자 시선**
AI가 똑똑해질수록 우리가 지켜야 할 비밀도 늘어납니다. 소프트웨어가 완벽하게 안전해지길 기다리기보다는, AI를 다루는 우리가 더 영리하게 '보안 울타리'를 치는 법을 배워야 할 때입니다.

## 참고자료

1. [A way to exclude sensitive files · Issue #2847 · openai/codex](https://github.com/openai/codex/issues/2847)
2. [A way to exclude sensitive files issue still open for OpenAI ...](https://news.ycombinator.com/item?id=48706714)
3. [Ignore files feature, e.g. ".codexignore" · openai codex ...](https://github.com/openai/codex/discussions/3456)
4. [How to prevent OpenAI Codex CLI from accessing `.env` files?](https://askai.glarity.app/search/How-to-prevent-OpenAI-Codex-CLI-from-accessing---env--files)
5. [Agent approvals & security – Codex | OpenAI Developers](https://developers.openai.com/codex/agent-approvals-security)
6. [[SECURITY!] Do not allow Codex to read whole filesystem by ...](https://github.com/openai/codex/issues/4410)
7. [Add ability to hide sensitive files from agent · Issue #85 ...](https://github.com/openai/codex/issues/300/linked_closing_reference?reference_location=REPO_ISSUES_INDEX)