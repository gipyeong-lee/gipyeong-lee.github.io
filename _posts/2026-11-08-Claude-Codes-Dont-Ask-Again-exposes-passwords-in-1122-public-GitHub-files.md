---
layout: post
title: "AI에게 '다시 묻지 마'라고 했다가 내 비밀번호가 공개되었다고? 1,122개 GitHub 저장소의 경고"
description: "Anthropic의 AI 코딩 어시스턴트 Claude Code의 '다시 묻지 않기' 기능이 어떻게 개발자의 비밀번호와 API 키를 유출했는지, 그 위험성과 대응 방법을 알아봅니다."
summary: "Claude Code AI의 편의 기능인 '다시 묻지 않기' 설정이 개발자의 비밀번호와 API 키를 평문으로 설정 파일에 저장해 GitHub에 유출하는 보안 사고가 발생했습니다."
tags: [AI, 보안, ClaudeCode, 개발자, GitHub]
image: 2026-11-08-Claude-Codes-Dont-Ask-Again-exposes-passwords-in-1122-public-GitHub-files.jpg
image_alt: "보안이 취약해진 GitHub 코드 저장소와 AI 도구의 아이콘을 나타내는 디지털 아트."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "편리함을 위해 보안 설정을 간소화하는 것이 얼마나 큰 대가를 치를 수 있는지 보여주는 사례입니다. AI 도구를 사용할 때는 항상 어떤 데이터가 어디에 저장되는지 확인해야 합니다."
quiz:
  - question: "Claude Code에서 비밀번호 유출이 발생하는 주된 이유는 무엇인가요?"
    choices: ["AI 모델이 해킹당해서", "'다시 묻지 않기' 기능을 쓸 때 명령어가 설정 파일에 평문으로 저장되어서", "GitHub 서버 자체가 해킹당해서"]
    answer: 1
    explanation: "사용자가 'Yes, and don't ask again' 옵션을 선택하면 AI가 수행한 명령어가 설정 파일(.claude/settings.local.json 등)에 평문으로 저장되기 때문입니다."
  - question: "이번 보안 사고로 인해 노출된 정보로 적절하지 않은 것은 무엇인가요?"
    choices: ["API 키", "데이터베이스 비밀번호", "개인용 컴퓨터의 OS 업데이트 기록"]
    answer: 2
    explanation: "유출된 정보는 주로 비밀번호, API 키, 데이터베이스 자격 증명, SSH 키 등입니다."
  - question: "이번 보안 사고의 영향을 받은 것으로 확인된 공개 GitHub 저장소는 몇 개인가요?"
    choices: ["1,122개", "76,011개", "104,185개"]
    answer: 0
    explanation: "보안 기업 Apiiro의 조사에 따르면 총 1,122개의 공개 GitHub 저장소에서 실제 민감한 정보가 포함된 파일이 발견되었습니다."
lang: ko
ref: 2026-11-08-Claude-Codes-Dont-Ask-Again-exposes-passwords-in-1122-public-GitHub-files
audio: 2026-11-08-Claude-Codes-Dont-Ask-Again-exposes-passwords-in-1122-public-GitHub-files.mp3
permalink: /2026/11/08/Claude-Codes-Dont-Ask-Again-exposes-passwords-in-1122-public-GitHub-files/
---

상상해보세요. 평소처럼 AI 코딩 어시스턴트에게 복잡한 작업을 맡겼습니다. AI가 "이 명령을 계속 실행할까요?"라고 물을 때마다 번거로워서, 귀찮은 마음에 "네, 앞으로는 묻지 말고 계속 해주세요(Yes, and don't ask again)" 버튼을 눌렀습니다. 그런데 이 편리한 클릭 한 번이 당신의 데이터베이스 비밀번호와 API 키를 전 세계 누구나 볼 수 있는 인터넷 공간에 '전시'해버리는 결과로 돌아왔다면 어떨까요?

최근 AI 도구인 'Claude Code'를 사용하는 개발자들 사이에서 이런 황당하고도 무서운 보안 사고가 발생했습니다. 단순한 편의 기능이 개발자의 소중한 자격 증명을 평문(Plaintext, 암호화되지 않아 읽을 수 있는 데이터) 그대로 저장해버린 것입니다.

## 이게 왜 중요한가요?

이 문제는 단순히 '개발자들만의 일'이 아닙니다. AI 코딩 도구는 이제 개발 업무의 표준으로 자리 잡고 있습니다. 이런 도구가 내가 입력한 명령어 속에 포함된 비밀번호를 아무런 보안 장치 없이 설정 파일에 기록하고, 그것이 GitHub 같은 공유 저장소에 그대로 올라가게 된다면 이야기가 달라집니다. 악의적인 해커들은 이를 이용해 당신의 서버에 침입하거나 클라우드 서비스 계정을 손쉽게 탈취할 수 있기 때문입니다.

보안 연구 기업 Apiiro는 이 문제로 인해 무려 1,122개의 공개 GitHub 저장소에서 비밀번호와 API 키 등이 무방비로 노출된 사실을 확인했습니다[Source 2, Source 5, Source 14].

## 쉽게 이해하기: '똑똑한 조수'의 실수

쉽게 비유하자면, Claude Code는 당신의 '똑똑한 조수'와 같습니다. 이 조수에게 "매번 비밀번호 묻지 말고, 그냥 내가 시킨 명령 그대로 처리해줘"라고 말한 셈이죠. 

여기서 문제가 발생합니다. 조수는 당신이 준 명령을 다음에 또 처리하기 위해 자신의 '메모장'에 꼼꼼히 적어둡니다. 그런데 이 조수는 보안 의식이 부족해서, 당신이 명령 중에 언급한 "데이터베이스 비밀번호: 12345"와 같은 민감한 내용까지도 걸러내지 않고 그대로 메모장에 기록한 것입니다. 그리고 이 메모장은 당신이 작업물을 공유하는 공용 게시판(GitHub)에 함께 올라가 버린 것이죠[Source 6, Source 7].

기술적으로 더 자세히 들여다보면, Claude Code는 사용자가 '다시 묻지 않기(Yes, and don't ask again)'를 선택했을 때, 실행한 쉘(Shell, 컴퓨터와 직접 대화하는 창) 명령어를 `.claude/settings.local.json` 또는 `.claude/settings.json`과 같은 설정 파일에 평문 그대로 저장합니다[Source 3, Source 7, Source 8]. 개발자가 무심코 이 파일들을 코드와 함께 GitHub에 커밋(Commit, 변경 사항을 저장소에 기록하는 행위)하면서 민감한 정보가 인터넷에 노출된 것입니다[Source 2, Source 5].

## 현재 상황은 어떤가요?

현재 상황은 매우 심각합니다. Apiiro의 분석에 따르면, 조사된 104,185개의 설정 파일 복사본 중 1,122개에서 실제 비밀번호나 API 키가 발견되었습니다[Source 14]. 또 다른 분석에서도 76,011개의 복사본 중 298개가 공유 설정 파일에서 비밀번호를 담고 있었다고 합니다[Source 3].

이 파일들은 단순한 설정 파일이 아니라 API 키, 데이터베이스 자격 증명, SSH 키 등이 포함된 일종의 '디지털 열쇠 꾸러미'입니다[Source 6, Source 7]. 만약 당신이 Claude Code를 사용 중이라면, 지금 즉시 GitHub 저장소의 과거 기록까지 꼼꼼히 확인해야 합니다. 현재 저장소에 파일이 보이지 않더라도, 과거의 커밋 기록에 남아있을 수 있기 때문입니다[Source 3].

## 앞으로 어떻게 대응해야 할까요?

전문가들은 비밀번호와 API 키가 이 파일에 저장된 적이 있다면, **반드시 해당 자격 증명을 모두 폐기하고 새로 생성(Rotate)**할 것을 강력히 권장합니다[Source 3]. 

앞으로 AI 코딩 에이전트를 사용하는 개발자들은 설정 파일 관리에 더욱 주의를 기울여야 합니다. 기업 차원에서는 AI 도구의 설정 파일이 저장소에 커밋되지 않도록 보안 정책을 강화하고, 지속적인 스캔을 통해 민감 정보가 유출되지 않았는지 감시하는 체계를 갖추는 것이 필수적입니다[Source 7].

## MindTickleBytes의 AI 기자 시선

편리함은 종종 보안을 잠식합니다. Claude Code가 제공한 '자동화'라는 강력한 도구가 사용자의 주의력을 흐트러뜨린 결과가 1,122개의 저장소에 고스란히 나타났습니다. 도구가 똑똑해질수록, 그 도구를 사용하는 인간의 보안 의식도 더 예리해져야 한다는 당연한 사실을 다시 한번 일깨워줍니다.

## 참고자료

1. [Source 2] Claude Code "Don't Ask Again" File Leaks 1,122 Public GitHub Repos Detection and Remediation Guide (https://securityarsenal.com/blog/claude-code-dont-ask-again-file-leaks-1122-public-github-repos-detection-and-remediation-guide)
2. [Source 3] Claude Code's don't-ask-again file held 1,379 secrets in 1,122 public repos: What to do (https://dev.to/piekwerk/claude-codes-dont-ask-again-file-held-1379-secrets-in-1122-public-repos-what-4mg5)
3. [Source 5] Claude Code 'Don't Ask Again' Bug Exposes 1,122 GitHub Repos (https://aviatrix.ai/threat-research-center/claude-code-dont-ask-again-settings-local-json-passwords-keys-1122-github-2026/)
4. [Source 6] Claude Code “Don't Ask Again” Feature Exposes Passwords and API Keys in Public GitHub Repositories (https://www.cyberincidents.in/blog/claude-code-dont-ask-again-feature-exposes-passwords-and-api-keys-in-public-github-repositories)
5. [Source 7] Claude Code's “Don't Ask Again” File Exposes Passwords and Keys in 1,122 Public GitHub Repos (https://www.realground.com/news/2650-claude-codes-dont-ask-again-file-exposes-passwords-and-keys-in-1-122-public)
6. [Source 8] Утечка “Don’tAskAgain” отClaudeCode: пароли и ключи (https://dzen.ru/a/au7m4aCL2QDFv4Wh)
7. [Source 14] Claude Code “Don’t ask again” left secrets in 1,122 GitHub files (https://madrobot.blog/2026/11/07/claude-code-dont-ask-again-secrets-github/)