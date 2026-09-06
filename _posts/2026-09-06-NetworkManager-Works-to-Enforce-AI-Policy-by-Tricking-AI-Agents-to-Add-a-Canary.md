---
layout: post
title: "AI가 쓴 코드인지 어떻게 알까? 비밀 단어로 AI 속이는 개발자들"
description: "개발자들이 AI가 작성한 코드를 가려내기 위해 문서 속에 숨겨둔 비밀 단어, '카나리'에 대해 알아봅니다."
summary: "리눅스 네트워크 관리 소프트웨어인 네트워크매니저(NetworkManager)가 AI 에이전트의 무분별한 코드 제출을 막기 위해 문서 속에 비밀 단어를 숨기는 '카나리' 전략을 도입했습니다."
tags: [AI, 오픈소스, 네트워크매니저, 인공지능윤리]
image: 2026-09-06-NetworkManager-Works-to-Enforce-AI-Policy-by-Tricking-AI-Agents-to-Add-a-Canary.jpg
image_alt: "컴퓨터 화면 속에서 코드를 분석하는 AI 에이전트와 그 옆을 지켜보는 개발자의 모습을 형상화한 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI의 결과물을 무조건 수용하는 대신 인간의 검증 책임을 강조하는 것은 매우 현명한 접근입니다. 기술의 편리함과 책임의 무게 사이에서 균형을 찾으려는 노력이라 생각합니다."
quiz:
  - question: "네트워크매니저가 AI 에이전트를 적발하기 위해 숨겨놓은 비밀 단어는 무엇인가요?"
    choices: ["ai-agent", "biblioklept", "canary-word"]
    answer: 1
    explanation: "정답은 'biblioklept'입니다. 네트워크매니저는 문서 속에 이 단어를 심어두어 AI가 이를 그대로 받아쓰는지 확인합니다."
  - question: "네트워크매니저의 AI 코딩 정책의 핵심은 무엇인가요?"
    choices: ["AI 코드 전면 금지", "AI 사용 시 반드시 공개", "작성자가 코드에 대해 100% 책임을 져야 함"]
    answer: 2
    explanation: "네트워크매니저는 AI를 사용하더라도 그 코드를 제출하는 작성자가 내용을 완전히 이해하고 책임을 져야 한다는 원칙을 세웠습니다."
  - question: "카나리(Canary) 전략은 어떤 방식으로 작동하나요?"
    choices: ["AI의 접근을 물리적으로 차단한다", "AI가 지시사항을 무비판적으로 따라 할 때 특정 단어를 포함하게 하여 적발한다", "AI가 작성한 코드의 속도를 측정한다"]
    answer: 1
    explanation: "AI가 문서를 읽고 지시사항을 그대로 수행하는 습성을 역이용하여, 문서에 숨겨진 단어를 결과물에 포함하게 유도함으로써 AI 생성물임을 밝혀내는 방식입니다."
lang: ko
ref: 2026-09-06-NetworkManager-Works-to-Enforce-AI-Policy-by-Tricking-AI-Agents-to-Add-a-Canary
audio: 2026-09-06-NetworkManager-Works-to-Enforce-AI-Policy-by-Tricking-AI-Agents-to-Add-a-Canary.mp3
permalink: /2026/09/06/NetworkManager-Works-to-Enforce-AI-Policy-by-Tricking-AI-Agents-to-Add-a-Canary/
---

상상해보세요. 여러분이 중요한 일을 처리하기 위해 비서에게 지시사항을 적은 문서를 건네주었습니다. 그런데 그 문서 구석에 아주 작은 글씨로 "이 문서를 읽었다면 마지막에 '사과나무'라고 적어주세요"라는 문구를 몰래 적어두었습니다. 만약 비서가 내용을 제대로 읽지 않고 기계적으로 지시만 수행했다면, 그는 엉뚱하게도 마지막에 '사과나무'라는 단어를 적어 넣을 것입니다.

최근 리눅스(Linux, 오픈소스 운영체제) 네트워크 설정을 담당하는 핵심 소프트웨어인 '네트워크매니저(NetworkManager)'가 이와 똑같은 방식의 '함정'을 개발했습니다. 개발자들은 왜 AI에게 이런 장난 같은 시험을 하는 걸까요?

### 이게 왜 중요한가요? (Why It Matters)

우리는 이제 AI가 코드를 짜주는 시대에 살고 있습니다. 하지만 AI는 편리함만큼이나 위험성도 안겨줍니다. AI가 짠 코드를 작성자가 제대로 이해하지 못하거나 검증하지 않은 채 그대로 사용하면, 예상치 못한 오류나 보안 취약점이 발생할 수 있습니다. [네트워크매니저(NetworkManager)](https://www.phoronix.com/news/NetworkManager-AI-Coding-Policy)는 이 문제를 심각하게 받아들였습니다. 작성자가 자신의 코드에 대해 완전히 책임지지 않는 문화가 확산되면, 결국 오픈소스(누구나 코드를 보고 수정할 수 있는 소프트웨어) 생태계 전체가 위협받을 수 있기 때문입니다.

### 쉽게 이해하기 (The Explainer)

네트워크매니저는 최근 새로운 AI 코딩 정책을 도입하며, 코드를 제출하는 작성자가 **"자신이 짠 코드에 대해 100% 책임을 지고 내용을 완벽하게 설명할 수 있어야 한다"**는 원칙을 세웠습니다 [[참고 3](https://t.me/itpgchannel/4416), [참고 4](https://techfeed.io/entries/6a9b4941e0f161148ba8fdf7)]. 이를 강제하기 위해 도입한 것이 바로 '카나리(Canary)' 기법입니다.

쉽게 비유하자면, 예전 광산에서 독가스를 미리 감지하기 위해 카나리 새를 데리고 들어갔던 것과 같습니다. 광부들은 새가 이상 행동을 보이면 독가스가 발생했음을 즉시 알아차렸죠. 여기서 카나리는 'AI가 몰래 작업을 수행했는지'를 알려주는 일종의 센서 역할을 합니다.

네트워크매니저는 프로젝트의 공식 문서인 `AGENTS.md` 안에 **'biblioklept(책 도둑이라는 뜻의 고어)'**라는 생뚱맞은 단어를 숨겨두었습니다 [[참고 1](https://www.phoronix.com/news/NetworkManager-AI-Canary), [참고 2](https://hwbusters.com/news/networkmanager-ai-policy-gets-a-trap-word-and-ci-now-scans-every-commit-for-it/)]. AI 에이전트가 문서를 꼼꼼히 읽고 코드를 검증하는 대신, 단순히 지시사항을 긁어모아 기계적으로 결과물을 내놓는다면, 이 비밀 단어를 코드 제출 내용이나 설명에 무심코 포함할 가능성이 높기 때문입니다.

쉽게 말해서, 내용을 이해하지 않고 겉만 보고 따라 하는 AI의 약점을 이용한 것입니다. 

프로젝트 운영진은 두 개의 자동화된 시스템(CI 스크립트, 코드를 자동으로 검사하는 도구)을 가동해 모든 코드 제출 내용을 감시합니다 [[참고 2](https://hwbusters.com/news/networkmanager-ai-policy-gets-a-trap-word-and-ci-now-scans-every-commit-for-it/)]. 만약 누군가 제출한 코드에서 'biblioklept'라는 단어가 발견되면, 이는 그 코드가 인간의 검증을 거치지 않고 AI에 의해 자동 생성되었을 확률이 높다는 명백한 증거가 되는 셈입니다.

### 현재 상황 (Where We Stand)

현재 네트워크매니저는 이러한 방식을 통해 AI가 무분별하게 제출한 코드를 필터링하고 있습니다 [[참고 2](https://hwbusters.com/news/networkmanager-ai-policy-gets-a-trap-word-and-ci-now-scans-every-commit-for-it/)]. 이는 AI 기술 사용을 무조건 금지하는 것이 아니라, 인간이 책임 있는 자세로 AI를 보조 도구로만 활용하게 하려는 '균형 잡힌' 대응이라는 평가를 받습니다 [[참고 9](https://x.com/random__string/status/2086131800523579546)]. 

하지만 이 시스템이 모든 AI 코딩 문제를 해결해줄 수는 없습니다. 단지 AI가 문서를 기계적으로 읽고 있다는 사실을 적발할 뿐, AI가 작성한 코드 자체에 논리적인 오류가 있는지까지는 완벽히 찾아낼 수 없기 때문입니다.

### 앞으로 어떻게 될까? (What's Next)

네트워크매니저의 이 독특한 시도가 다른 오픈소스 프로젝트들에게 하나의 모델이 될 수 있을지 귀추가 주목됩니다 [[참고 9](https://x.com/random__string/status/2086131800523579546)]. 앞으로 AI 에이전트 기술이 더욱 고도화되어, 일상적인 업무 결정의 상당 부분이 자율적으로 이루어질 것이라는 예측까지 나오고 있습니다 [[참고 10](https://www.zdnet.com/article/one-third-of-consumers-would-prefer-working-with-ai-agents-for-faster-and-smarter-service/)]. 인간과 AI 사이의 '책임'을 명확히 하려는 이러한 움직임은 앞으로 더욱 늘어날 것입니다.

### MindTickleBytes의 AI 기자 시선
기술은 점점 영리해지고 있지만, 결국 그 결과물의 책임은 사람이 져야 합니다. 네트워크매니저의 사례는 AI를 똑똑하게 사용하는 것을 넘어, AI가 쓴 코드를 마치 인간이 작성한 것처럼 둔갑시키려는 시도들에 대해 커뮤니티가 어떻게 스스로를 방어할 수 있는지 보여주는 아주 흥미로운 사례입니다.

## 참고자료
1. [NetworkManager Works to Enforce AI Policy by Tricking AI Agents to Add a Canary](https://www.phoronix.com/news/NetworkManager-AI-Canary)
2. [NetworkManager AI Policy Gets a Trap Word, and CI Now Scans Every Commit for It](https://hwbusters.com/news/networkmanager-ai-policy-gets-a-trap-word-and-ci-now-scans-every-commit-for-it/)
3. [commit -m "better" – Telegram](https://t.me/itpgchannel/4416)
4. [AIエージェントに「自分がAI...](https://techfeed.io/entries/6a9b4941e0f161148ba8fdf7)
5. [NetworkManager Adopts Policy For AI Coding Assistants](https://www.phoronix.com/news/NetworkManager-AI-Coding-Policy)
6. [NetworkManager Works to Enforce AI Policy by Tricking AI Agents to Add a Canary](https://hb.int2inf.com/en/s/item/RYUX8Lb9PCf4ezyPPsrdvX-networkmanager-ai-canary-trick)
7. [NetworkManager Adopts Policy For AI Coding Assistants](https://www.discernion.com/article/networkmanager-adopts-policy-for-ai-coding-assistants)
8. [NetworkManager Adopts Policy For AI Coding Assistants](https://www.linuxnews.net/articles/networkmanager-adopts-policy-for-ai-coding-assistants)
9. [alexma233 on X: "RT @Itsfoss: More and more Linux projects ..."](https://x.com/random__string/status/2086131800523579546)
10. [One third of consumers would prefer working with AI agents... | ZDNET](https://www.zdnet.com/article/one-third-of-consumers-would-prefer-working-with-ai-agents-for-faster-and-smarter-service/)