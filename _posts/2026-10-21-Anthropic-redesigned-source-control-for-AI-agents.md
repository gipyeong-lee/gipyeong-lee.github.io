---
layout: post
title: "AI와 함께 일하는 새로운 방식? Anthropic이 소스 제어 시스템을 완전히 뒤집었습니다"
description: "Anthropic이 여러 AI 에이전트와 동시에 협업할 수 있도록 설계된 새로운 소스 제어 방식 'Scion'과 개선된 Claude Code 데스크탑 앱을 공개했습니다."
summary: "Anthropic이 기존 깃(git) 방식의 한계를 넘어, 여러 AI 에이전트가 병렬로 코딩하고 테스트할 수 있도록 설계된 차세대 소스 제어 시스템과 인터페이스를 선보였습니다."
tags: [AI, 개발, Anthropic, Claude, 코딩에이전트]
image: 2026-10-21-Anthropic-redesigned-source-control-for-AI-agents.jpg
image_alt: "여러 AI 에이전트가 동시에 코드를 분석하고 병렬로 작업을 수행하는 현대적인 개발 환경을 나타내는 인터페이스 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "과거의 개발 도구가 인간 중심의 순차적 작업에 맞춰져 있었다면, 이제는 도구 자체가 '에이전트'라는 새로운 동료를 받아들일 준비를 마쳤습니다. 개발자의 역할이 코드를 직접 짜는 것에서 AI 에이전트의 오케스트레이터(지휘자)로 진화하고 있음을 보여주는 중요한 변화입니다."
quiz:
  - question: "Anthropic이 공개한 차세대 소스 제어 시스템의 이름은 무엇인가요?"
    choices: ["Git Plus", "Scion", "Claude Control"]
    answer: 1
    explanation: "Anthropic은 기존 git의 한계를 넘어서기 위해 'Scion'이라는 새로운 접근 방식을 개발했습니다."
  - question: "새로운 Claude Code 데스크탑 앱이 개발자의 컨텍스트 스위칭을 줄이기 위해 도입한 기능이 아닌 것은?"
    choices: ["세션 사이드바", "드래그 앤 드롭 레이아웃", "클라우드 자동 삭제"]
    answer: 2
    explanation: "Claude Code는 세션 사이드바, 드래그 앤 드롭 레이아웃, 내장 터미널 등을 통해 여러 에이전트를 동시에 관리할 수 있도록 개선되었습니다."
  - question: "에이전트 중심 코딩(agentic coding) 환경에서 개발자의 역할은 주로 무엇인가요?"
    choices: ["직접 코드 한 줄씩 작성하기", "여러 에이전트 세션을 관리하는 오케스트레이터", "하드웨어 서버 구축"]
    answer: 1
    explanation: "많은 에이전트가 병렬로 작업을 수행함에 따라 개발자는 이들을 지휘하고 관리하는 오케스트레이터(orchestrator) 역할을 하게 됩니다."
lang: ko
ref: 2026-10-21-Anthropic-redesigned-source-control-for-AI-agents
audio: 2026-10-21-Anthropic-redesigned-source-control-for-AI-agents.mp3
permalink: /2026/10/21/Anthropic-redesigned-source-control-for-AI-agents/
---

상상해보세요. 아침에 일어나 컴퓨터를 켰더니 3명의 AI 개발자가 이미 당신의 소프트웨어 프로젝트를 돕고 있습니다. 한 명은 새로운 기능을 구현하고, 다른 한 명은 버그를 수정하며, 마지막 한 명은 새로 짠 코드가 제대로 작동하는지 실시간으로 테스트하고 있습니다. 

과거에는 개발자가 이 모든 과정을 순차적으로 직접 수행하거나, 여러 조각의 작업 결과를 하나로 합치느라 진땀을 흘려야 했습니다. 하지만 이제 개발 방식이 완전히 달라지고 있습니다. Anthropic이 '에이전트 시대'에 걸맞은 새로운 소스 제어(Source Control) 시스템과 도구를 선보였기 때문입니다.

## 이게 왜 중요한가요?

소프트웨어 개발은 지금까지 '인간 중심의 순차적 작업'이라는 가정하에 발전해 왔습니다. 하지만 AI 에이전트(특정 목적을 스스로 수행하는 AI 프로그램)가 코딩에 참여하면서 상황이 변했습니다. Anthropic의 연구에 따르면, 에이전트 중심 코딩(agentic coding)이 보편화되면서 기존 소프트웨어 개발 방식의 근본적인 전제들이 빠르게 진화하고 있습니다[Source 1](https://www.anthropic.com/research/redesigning-source-control). 

이러한 변화는 단순히 코딩 속도를 높이는 문제를 넘어섭니다. 여러 개의 AI 에이전트가 동시에 각기 다른 작업을 수행하면서, 기존의 소스 제어 시스템(개발자의 코드 변경 이력을 관리하는 시스템)은 병목 현상을 겪게 되었습니다. Anthropic이 새롭게 제시한 환경은 개발자가 여러 에이전트의 작업을 실시간으로 지휘하는 '오케스트레이터(지휘자)' 역할을 하도록 유도하며, 이 과정에서 발생하는 잦은 맥락 전환(context-switching, 작업 중 다른 작업으로 옮겨갈 때 발생하는 집중력 저하 현상)을 획기적으로 줄여줍니다[Source 2](https://www.eigent.ai/blog/claude-code-desktop-redesign)[Source 5](https://completeaitraining.com/news/anthropic-redesigns-claude-code-desktop-app-to-better/).

## 쉽게 이해하기: 깃(git)에서 Scion으로

전통적인 소스 제어 시스템인 '깃(git)'은 사실 인간 한 명이 파일을 수정하고 저장하는 과정을 관리하는 데 최적화되어 있습니다. 마치 한 권의 책을 여러 사람이 돌아가며 쓰는 것과 비슷하죠. 하지만 여러 AI 에이전트가 동시에 서로 다른 부분을 수정한다면 어떻게 될까요? 

Anthropic은 'Scion'이라는 새로운 시스템을 개발했습니다[Source 1](https://www.anthropic.com/research/redesigning-source-control). 

쉽게 비유하자면, 기존의 깃이 한 명의 작가를 위한 '원고지'였다면, Scion은 수십 명의 작가가 각자 자기 방에서 동시에 글을 쓰고, 지휘자가 그 방들을 드나들며 실시간으로 내용을 조합하는 '현대적인 협업 플랫폼'과 같습니다. 이 시스템은 기존의 소스 제어 원칙을 에이전트의 규모에 맞춰 완전히 새롭게 설계한 것입니다[Source 1](https://www.anthropic.com/research/redesigning-source-control).

## 현재 상황: Claude Code의 진화

Anthropic은 이 철학을 담아 자사의 코딩 에이전트 도구인 'Claude Code' 데스크탑 앱을 완전히 재설계했습니다[Source 2](https://www.eigent.ai/blog/claude-code-desktop-redesign). 

이제 Claude Code는 단순한 명령줄 도구가 아닙니다. 다음과 같은 기능들이 탑재되어 개발자의 작업 공간을 바꿉니다[Source 5](https://completeaitraining.com/news/anthropic-redesigns-claude-code-desktop-app-to-better/):

*   **세션 사이드바:** 실행 중인 여러 AI 에이전트의 상태를 한눈에 볼 수 있습니다.
*   **드래그 앤 드롭 레이아웃:** 원하는 작업창을 자유롭게 배치하여 에이전트의 작업 흐름을 관리할 수 있습니다.
*   **내장 터미널:** 별도의 창을 옮겨 다닐 필요 없이 코드 수정, 테스트 실행, 변경 사항 커밋(저장)을 한곳에서 처리합니다[Source 5](https://completeaitraining.com/news/anthropic-redesigns-claude-code-desktop-app-to-better/)[Source 7](https://www.linkedin.com/posts/abhijeet-pachpute_anthropic-redesigned-claude-code-for-desktop-activity-7450256887431843840-lelR).

이러한 업데이트를 통해 AI 에이전트는 코드베이스를 직접 읽고, 수정하고, 테스트하며, 안전하게 변경 사항을 반영하는 업무를 병렬 세션으로 처리하게 됩니다[Source 7](https://www.linkedin.com/posts/abhijeet-pachpute_anthropic-redesigned-claude-code-for-desktop-activity-7450256887431843840-lelR).

## 앞으로 어떻게 될까?

Anthropic의 이번 변화는 단지 도구의 외형을 바꾼 것이 아닙니다. 개발자가 AI를 어떻게 다루어야 하는지에 대한 새로운 표준을 제시한 것입니다. 앞으로는 더 많은 AI 서비스가 서로 다른 에이전트와 연결되는 '표준 프로토콜(MCP, Model Context Protocol, 서로 다른 AI 도구가 정보를 주고받기 위해 사용하는 공통 언어)'을 채택하게 될 것입니다[Source 14](https://www.zdnet.com/article/google-joins-openai-in-adopting-anthropics-protocol-for-connecting-ai-agents-why-it-matters/). 

우리가 지켜봐야 할 미래는 AI가 더 똑똑해지는 것뿐만 아니라, **"AI들이 얼마나 서로 충돌 없이 협력하고, 인간 지휘자가 얼마나 효율적으로 그들을 통제할 수 있는가"**에 달려 있습니다. 소스 제어 시스템이 AI 시대를 받아들인 것처럼, 앞으로는 우리 주변의 모든 개발 환경이 '에이전트가 기본값'인 시대로 변모할 것입니다.

## 참고자료

1. Redesigning source control at Anthropic (https://www.anthropic.com/research/redesigning-source-control)
2. Claude Code Desktop Redesign: Parallel Agents (2026) (https://www.eigent.ai/blog/claude-code-desktop-redesign)
3. Projects redesigned: from folder to conversation | Claude by Anthropic (https://claude.com/blog/projects-redesigned)
4. Anthropic Turns Claude Code Projects Into a Parallel AI... - KingyAI (https://kingy.ai/news/anthropic-claude-code-projects-ai-agents/)
5. Anthropic redesigns Claude Code desktop app to better handle... (https://completeaitraining.com/news/anthropic-redesigns-claude-code-desktop-app-to-better/)
6. Anthropic redesigns Claude Projects as multi-agent coordinator (https://www.brocker.org/anthropic-redesigns-claude-projects-multi-agent-coordinator-claude-code)
7. Anthropic redesigned Claude Code for desktop. tl;dr This is a serious... (https://www.linkedin.com/posts/abhijeet-pachpute_anthropic-redesigned-claude-code-for-desktop-activity-7450256887431843840-lelR)
14. Google joins OpenAI in adopting Anthropic's protocol for connecting AI agents - ZDNET (https://www.zdnet.com/article/google-joins-openai-in-adopting-anthropics-protocol-for-connecting-ai-agents-why-it-matters/)