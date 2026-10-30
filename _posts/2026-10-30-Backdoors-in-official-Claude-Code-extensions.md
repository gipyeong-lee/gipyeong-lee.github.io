---
layout: post
title: "내 코딩 도우미가 해커의 문을 열어줬다고? Claude Code 확장 프로그램 보안 이슈"
description: "최근 발견된 Claude Code 확장 프로그램의 공급망 공격 사례와 개발자가 주의해야 할 보안 위협에 대해 알아봅니다."
summary: "공식 Claude Code 확장 프로그램의 일부 버전에서 원격 접속이 가능한 백도어가 발견되어 개발자들의 주의가 필요합니다."
tags: [보안, AI, 개발자, ClaudeCode, 공급망공격]
image: 2026-10-30-Backdoors-in-official-Claude-Code-extensions.jpg
image_alt: "컴퓨터 화면 속 코드와 자물쇠가 그려진 보안 사고를 상징하는 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "편리함을 위해 설치한 도구가 공격자의 통로가 될 수 있다는 점을 항상 경계해야 합니다. 최신 버전 업데이트는 이제 선택이 아닌 생존의 문제입니다."
quiz:
  - question: "이번 보안 이슈의 핵심 원인은 무엇인가요?"
    choices: ["AI 모델 자체의 결함", "공식 확장 프로그램의 변조된 업데이트", "인터넷 연결 불량"]
    answer: 1
    explanation: "Claude Code 확장 프로그램의 2.1.313 버전이 변조되어 악성 코드가 포함된 것이 이번 문제의 핵심입니다."
  - question: "악성 코드가 수행하는 주요 기능은 무엇인가요?"
    choices: ["광고 노출", "지속적인 SSH 원격 접속 통로 개설", "컴퓨터 속도 향상"]
    answer: 1
    explanation: "해당 악성 코드는 공격자가 개발자의 컴퓨터에 원격으로 접속할 수 있도록 SSH 백도어를 설치합니다."
  - question: "사용자가 취해야 할 조치는 무엇인가요?"
    choices: ["컴퓨터 교체", "최신 버전으로 업데이트 및 보안 점검", "AI 사용 중단"]
    answer: 1
    explanation: "Anthropic이 대응책으로 내놓은 2.1.314 버전으로 즉시 업데이트하고 관련 보안 지침을 확인해야 합니다."
lang: ko
ref: 2026-10-30-Backdoors-in-official-Claude-Code-extensions
audio: 2026-10-30-Backdoors-in-official-Claude-Code-extensions.mp3
permalink: /2026/10/30/Backdoors-in-official-Claude-Code-extensions/
---

상상해보세요. 평소처럼 코딩 생산성을 높이기 위해 신뢰할 수 있는 개발 도구의 업데이트를 클릭했습니다. 하지만 그 업데이트가 사실은 당신의 컴퓨터 문을 활짝 열어둔 채 몰래 도둑을 들인 것이라면 어떨까요? 

최근 전 세계 개발자들이 사용하는 공식 Claude Code 확장 프로그램에서 보안 사고가 발생했습니다. 평소 우리가 편리하게 사용하던 도구가 사실은 공격자의 원격 접속 통로로 변질되어 있었던 것입니다. 이번 사건은 우리가 무심코 설치하는 '코드 도우미'가 얼마나 큰 보안 리스크를 안고 있는지 보여주는 뼈아픈 사례입니다.

## 이게 왜 중요한가요?

개발자에게 확장 프로그램은 업무 효율을 위한 필수품입니다. 하지만 이번 사건은 '공식' 확장 프로그램이라고 해서 무조건 안전하지 않다는 사실을 증명했습니다. [출처 4](https://daily.dev/posts/backdoors-in-official-claude-code-extensions-kzegz0lci), [출처 8](https://undercodenews.com/claude-code-extension-supply-chain-attack-malicious-update-exposed-up-to-5000-cursor-users-to-ssh-backdoors-and-remote-access-video/)에 따르면, 약 5,000명의 사용자가 이번에 변조된 버전을 설치한 것으로 추정됩니다.

공격자는 이 경로를 통해 사용자의 Git 이메일, 환경 변수, 운영체제 정보 등 민감한 데이터에 접근할 수 있었습니다 [출처 2](https://cursor.com/blog/claude-code-extension-security-notice). 단순히 정보를 훔치는 것을 넘어, 당신의 컴퓨터에 언제든 다시 접속할 수 있는 '비상구(백도어)'까지 만들어두었다는 점이 가장 큰 위협입니다.

## 쉽게 이해하기

이번 사건은 '공급망 공격(Supply-Chain Attack)'의 전형적인 모습입니다. 이를 쉽게 비유하면 이렇습니다. 우리가 매일 마시는 생수 공장의 시스템이 해킹당해서, 불순물이 섞인 물이 정식 유통 경로를 통해 우리 집 식탁까지 배달된 것과 같습니다. 우리는 공장을 신뢰했기에 물이 오염되었을 것이라고는 의심조차 하지 않죠.

기술적으로는 'SSH(Secure Shell, 원격 컴퓨터를 안전하게 제어하는 기술) 백도어'라는 방식을 사용했습니다. 공격자는 이 기술을 거꾸로 이용해 '역방향 SSH 터널'을 만들었습니다 [출처 5](https://www.explainx.ai/blog/claude-code-extension-trojanized-2-1-313-cursor-marketplace-ssh-backdoor-what-is-confirmed-2026). 쉽게 말해서, 도둑이 우리 집 현관문의 잠금장치를 해체해 놓고, 언제든 원할 때 다시 들어올 수 있는 비밀 통로를 몰래 하나 더 뚫어놓은 셈입니다.

## 현재 상황

문제의 발단은 공식 Claude Code 확장 프로그램의 2.1.313 버전이었습니다 [출처 1](https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor), [출처 4](https://daily.dev/posts/backdoors-in-official-claude-code-extensions-kzegz0lci). Cursor 마켓플레이스 등 주요 경로를 통해 배포된 이 버전은 사용자의 컴퓨터 정보를 수집하고 공격자의 서버와 연결되는 악성 코드를 포함하고 있었습니다 [출처 2](https://cursor.com/blog/claude-code-extension-security-notice), [출처 6](https://www.rescana.com/post/claude-code-extension-2-1-313-cursor-marketplace-trojanized-ssh-backdoor). 

현재는 Cursor 측에서 해당 버전을 즉시 삭제하고 조치를 취했습니다 [출처 7](https://www.news9live.com/technology/tech-news/claude-code-extension-hacked-ssh-backdoor-cursor-users-at-risk-3020396). Anthropic 측에서도 문제의 버전을 대체할 2.1.314 버전을 내놓으며 진화에 나섰습니다 [출처 4](https://daily.dev/posts/backdoors-in-official-claude-code-extensions-kzegz0lci). 하지만, 일부 보고에 따르면 이전 버전(2.1.91 ~ 2.1.196)에서도 코드 추적이나 위치 정보 유출 등의 의혹이 제기된 바 있어 주의가 요구됩니다 [출처 3](https://nowosci.ai/en/article/china-claude-code-backdoor-location-tracking).

## 앞으로 어떻게 될까?

이번 사건으로 인해 개발 도구 시장 전반에 보안 검증 강화의 필요성이 대두될 것입니다. 개발자들은 앞으로 외부 확장 프로그램을 설치할 때 좀 더 보수적인 태도를 취하게 될 것이며, 보안 전문가들은 마켓플레이스에 올라오는 코드에 대한 자동화된 분석 시스템을 더 엄격하게 요구할 것입니다.

독자 여러분께서는 본인이 사용하는 IDE(통합 개발 환경)의 확장 프로그램 버전을 즉시 확인하시고, 최신 버전으로 업데이트하는 것을 잊지 마세요. 보안의 시작은 작은 의심과 정기적인 점검에서 시작됩니다.

## AI의 시선

AI 코딩 보조 도구는 우리의 생산성을 극적으로 높여주지만, 그만큼 우리가 쥐여주는 권한도 막강합니다. 이번 사건은 우리에게 '편리함의 대가'에 대해 다시 한번 생각하게 합니다. 기술을 활용하되, 그 기술이 내 컴퓨터의 주도권을 뺏어가지 않도록 감시하는 태도가 어느 때보다 중요해졌습니다.

## 참고자료

1. [Trojanized Claude Code Extension Plants an SSH Backdoor](https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor)
2. [Security notice — malicious version of Anthropic.claude-code...](https://cursor.com/blog/claude-code-extension-security-notice)
3. [China Warns of Backdoor in Claude Code, Anthropic Admits](https://nowosci.ai/en/article/china-claude-code-backdoor-location-tracking)
4. [Backdoors in official Claude Code extensions - daily.dev](https://daily.dev/posts/backdoors-in-official-claude-code-extensions-kzegz0lci)
5. [Claude Code Extension 2.1.313 SSH Backdoor: What To Check...](https://www.explainx.ai/blog/claude-code-extension-trojanized-2-1-313-cursor-marketplace-ssh-backdoor-what-is-confirmed-2026)
6. [Trojanized Claude Code Extension 2.1.313 in Cursor...](https://www.rescana.com/post/claude-code-extension-2-1-313-cursor-marketplace-trojanized-ssh-backdoor)
7. [Claude Code extension hacked: SSH backdoor puts 5,000 Cursor...](https://www.news9live.com/technology/tech-news/claude-code-extension-hacked-ssh-backdoor-cursor-users-at-risk-3020396)
8. [Claude Code Extension Supply-Chain Attack: Malicious Update...](https://undercodenews.com/claude-code-extension-supply-chain-attack-malicious-update-exposed-up-to-5000-cursor-users-to-ssh-backdoors-and-remote-access-video/)