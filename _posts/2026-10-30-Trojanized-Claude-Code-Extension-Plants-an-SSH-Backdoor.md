---
layout: post
title: "내 코딩 AI가 해킹의 통로라고? '트로이 목마'가 된 클로드 코드 확장 프로그램 주의보"
description: "최근 개발 도구로 위장해 사용자 컴퓨터에 침투하는 악성코드 위협이 급증하고 있습니다. 클로드 코드 확장 프로그램을 사칭한 공격의 실체와 예방 방법을 알아보세요."
summary: "공식 개발 도구처럼 위장한 악성 확장 프로그램과 가짜 소스 코드 유출본을 통해 개발자의 컴퓨터에 백도어를 설치하고 정보를 탈취하는 해킹 사례가 보고되고 있습니다."
tags: [보안, AI, 개발자, 클로드코드, 악성코드]
image: 2026-10-30-Trojanized-Claude-Code-Extension-Plants-an-SSH-Backdoor.jpg
image_alt: "컴퓨터 화면 위로 트로이 목마 로고와 경고 메시지가 떠 있는 사이버 보안 관련 일러스트"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI의 능력을 빌리려는 개발자의 열망을 범죄의 도구로 악용하는 것은 매우 비겁한 방식입니다. 기술을 사용할 때는 반드시 공식 채널을 확인하는 디지털 위생 습관이 필수입니다."
quiz:
  - question: "최근 개발자를 대상으로 하는 공격자들은 주로 무엇을 노리고 있나요?"
    choices: ["AI 모델 그 자체의 가중치", "개발자의 계정 인증 정보(Credential)", "AI의 서버용 전기 요금"]
    answer: 1
    explanation: "최근 AI 코딩 도구를 공격하는 주체들은 AI 모델이 아닌, 그 도구를 사용하는 개발자의 컴퓨터와 계정 정보를 탈취하는 데 집중하고 있습니다."
  - question: "악성코드가 유입되는 주요 경로가 아닌 것은 무엇인가요?"
    choices: ["공식 클로드 웹사이트(claude.com)", "트로이 목마가 심어진 가짜 '클로드 코드 유출' 저장소", "가짜 클로드 AI 웹사이트의 광고"]
    answer: 0
    explanation: "공식 웹사이트는 안전하며, 주로 그를 사칭한 가짜 사이트나 비공식적인 소스 코드 유출 저장소를 통해 악성코드가 배포됩니다."
  - question: "확장 프로그램 사칭 공격의 특징으로 옳은 것은?"
    choices: ["단순한 광고 팝업을 띄운다", "사용자의 컴퓨터에 SSH 백도어를 설치해 지속적인 원격 접근을 시도한다", "AI의 답변 속도를 늦춘다"]
    answer: 1
    explanation: "공격자들은 감염된 컴퓨터에 SSH 백도어를 심어 개발자가 눈치채지 못하게 시스템에 지속적으로 원격 접속하고 데이터를 빼냅니다."
lang: ko
ref: 2026-10-30-Trojanized-Claude-Code-Extension-Plants-an-SSH-Backdoor
audio: 2026-10-30-Trojanized-Claude-Code-Extension-Plants-an-SSH-Backdoor.mp3
permalink: /2026/10/30/Trojanized-Claude-Code-Extension-Plants-an-SSH-Backdoor/
---

상상해보세요. 코딩 작업의 효율을 높여줄 AI 도구를 설치하고 들뜬 마음으로 작업을 시작했습니다. 그런데 사실, 그 도구가 내 컴퓨터의 문을 몰래 열어두고 밖에서 해커가 언제든 들어올 수 있게 '비밀 통로'를 만들어 두었다면 어떨까요? 최근 개발자들 사이에서 이런 악몽 같은 일이 현실로 벌어지고 있습니다.

최근 [클로드 코드(Claude Code)](https://www.zscaler.com/blogs/security-research/anthropic-claude-code-leak)와 같은 인기 AI 코딩 도구의 인기를 악용해, 개발자의 정보를 탈취하고 시스템 권한을 뺏으려는 사이버 공격이 기승을 부리고 있습니다.

## 이게 왜 중요한가요?

이 문제는 단순히 '바이러스'에 걸리는 것 이상의 위험을 내포합니다. AI 코딩 도구는 우리가 작성하는 소스 코드, 클라우드 접근 권한, 데이터베이스 비밀번호 등 매우 민감한 정보에 접근할 수 있습니다. 

만약 공격자가 이런 도구를 통해 내 컴퓨터에 들어오게 된다면, 개발자 개인의 정보를 넘어 해당 개발자가 참여하고 있는 기업 전체의 보안망이 뚫릴 수도 있습니다. 실제로 2025년부터 2026년까지 [클로드 코드뿐만 아니라 GitHub Copilot, OpenAI Codex 등 주요 AI 코딩 에이전트들이 잇따라 보안 위협에 노출된 바 있습니다.](https://moccet.ai/news/tech/claude-code-copilot-and-codex-all-got-hacked-every-attacker-went-for-the-credent) 공격자들은 AI 모델 자체의 성능을 해치기보다는, 모델을 사용하는 **개발자의 계정 인증 정보(Credential, 사용자 식별 및 접근 권한 정보)**를 직접 노리고 있습니다.

## 쉽게 이해하기

이번 공격의 핵심은 **'트로이 목마'** 전략입니다. 그리스 신화에서 트로이 군대가 아름다운 목마 안에 병사들을 숨겨 성안으로 들어갔던 것처럼, 해커들도 악성 소프트웨어를 아주 유용한 AI 확장 프로그램이나 소스 코드인 것처럼 포장합니다.

1. **위장 전술**: 해커들은 공식 클로드 웹사이트와 똑같이 생긴 [가짜 웹사이트](https://www.notebookcheck.net/Fake-Claude-AI-website-is-pushing-a-Windows-backdoor-through-Google-search-results.1291664.0.html)를 만들거나, '코드 유출본'이라고 속인 파일들을 배포합니다.
2. **침투**: 개발자가 이를 다운로드해 실행하면, 그 안의 프로그램은 내 컴퓨터에 [비글(Beagle) 윈도우 백도어](https://www.linkedin.com/posts/bleepingcomputer_cybersecurity-windowssecurity-malware-activity-7458094379153502208-JG7C)나 비다(Vidar) 같은 악성코드를 설치합니다.
3. **비밀 통로**: 이 악성코드는 [SSH 백도어(백도어, 시스템에 비밀리에 접근하기 위한 뒷문)](https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor)를 심어, 외부 해커가 마치 내 컴퓨터 주인인 것처럼 언제든 들어올 수 있는 '역방향 SSH 터널'을 만듭니다.

비유하자면, 우리가 도구를 설치하는 행위가 알고 보니 해커에게 "우리 집 비밀번호 여기 있어요"라고 친절하게 알려주는 꼴이 된 셈입니다. 우리가 문을 열어준 순간, 해커는 그 문을 통해 우리 집(컴퓨터)에 마음대로 드나들며 소중한 자산(데이터)을 훔쳐가는 것이죠.

## 현재 상황

상황은 생각보다 심각합니다. 지난 4월, [수만 명의 사람들이 '클로드 코드'의 소스 코드가 유출되었다는 소식에 열광하며 파일을 다운로드했는데, 그중 상당수가 정보 탈취형 악성코드를 포함하고 있었습니다.](https://www.theregister.com/2026/04/02/trojanized_claude_code_leak_github/?ref=biztoc.com)

보안 연구기관인 Zscaler는 [anthropic.claude-code@2.1.313 버전으로 위장한 트로이 목마 확장 프로그램이 이미 발견되었다고 경고](https://github.com/nirholas/fresh-start)했습니다. 이 확장 프로그램은 설치되는 순간 공격자의 서버와 통신하며 사용자의 시스템을 장악합니다. 현재 공격자들은 구글 검색 광고까지 활용해 가짜 사이트를 검색 결과 상단에 노출하는 등 매우 교묘하게 접근하고 있습니다.

## 앞으로 어떻게 될까?

앞으로 AI 코딩 도구는 개발 과정에서 떼려야 뗄 수 없는 필수품이 될 것입니다. 따라서 공격자들의 표적 역시 더욱 정교해질 것입니다. [앤스로픽(Anthropic)이 제공하는 공식 CLI(Command Line Interface, 명령 줄 인터페이스) 도구만을 사용](https://github.com/nirholas/fresh-start)하고, 비공식적인 경로로 유출된 소스 코드는 절대 내려받지 않는 것이 중요합니다. 

앞으로는 도구를 설치할 때 디지털 서명을 확인하거나, 신뢰할 수 있는 개발자 커뮤니티의 검증을 거친 공식 버전인지 체크하는 습관이 개발자의 필수 역량이 될 것입니다. 보안은 단순히 기술적인 문제가 아니라, 매일 지키는 작은 습관에서 시작됩니다.

## AI의 시선

똑똑한 AI를 파트너로 삼고 싶어 하는 개발자들의 마음을 범죄의 수단으로 이용하는 것은 매우 비겁하고 나쁜 일입니다. 하지만 이번 사태는 우리가 '편리함' 뒤에 숨겨진 '보안'을 얼마나 소홀히 하고 있었는지 보여주는 거울이기도 합니다. 편리함보다 중요한 것은 언제나 안전입니다. 공식 경로를 이용하는 것, 그것이 가장 빠르고 안전한 개발의 시작입니다.

## 참고자료

1. [Trojanized Claude Code Extension Plants a Persistent SSH Backdoor](https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor)
2. [Claude Code Leak: Critical AI Security Threat 2026](https://www.zscaler.com/blogs/security-research/anthropic-claude-code-leak)
3. [Fake Claude AI website is pushing a Windows backdoor through Google search results](https://www.notebookcheck.net/Fake-Claude-AI-website-is-pushing-a-Windows-backdoor-through-Google-search-results.1291664.0.html)
4. [Claude AI Site Spreads Beagle Windows Backdoor via Trojanized](https://www.linkedin.com/posts/bleepingcomputer_cybersecurity-windowssecurity-malware-activity-7458094379153502208-JG7C)
5. [Fake Claude Code source downloads actually delivered malware](https://www.theregister.com/2026/04/02/trojanized_claude_code_leak_github/?ref=biztoc.com)
6. [GitHub - nirholas/fresh-start: The original nirholas/claude-code before...](https://github.com/nirholas/fresh-start)
7. [AI Coding Agents Hacked: Claude Code, Copilot... | Moccet TechNews](https://moccet.ai/news/tech/claude-code-copilot-and-codex-all-got-hacked-every-attacker-went-for-the-credent)