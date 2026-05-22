---
layout: post
title: "AI에게 코딩을 맡겼더니 엉망진창? '설계도(Spec)'부터 쓰면 달라집니다"
description: "AI 코딩 비서 클로드 코드(Claude Code)를 제대로 활용하는 방법, 스펙 주도 개발(SDD) 워크플로우를 알아봅니다."
summary: "단순히 대화로 코딩을 지시하는 방식에서 벗어나, 명확한 설계도를 먼저 작성하고 작업을 세분화하는 '스펙 주도 개발(SDD)'이 AI 코딩의 새로운 표준으로 떠오르고 있습니다."
tags: [AI코딩, 클로드코드, 스펙주도개발, 소프트웨어개발, AI생산성]
image: 2026-05-22-Show-HN-Spec-Driven-Development-Workflow-for-Claude-Code.jpg
image_alt: "건축가가 복잡한 청사진을 펴놓고 로봇 팔과 함께 작업하는 모습을 부드러운 일러스트로 표현한 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "인공지능은 마법 지팡이가 아니라 뛰어난 일꾼입니다. 일꾼이 제 실력을 발휘하려면, 우리가 먼저 '무엇을 원하는지' 명확한 청사진을 제시해야 한다는 당연한 진리를 다시금 깨닫게 됩니다."
quiz:
  - question: "기사에서 설명하는 '스펙 주도 개발(SDD)'의 핵심 원칙 중 하나로, AI가 혼란스러워하는 것을 막기 위해 단계마다 수행하는 작업은 무엇인가요?"
    choices: ["AI의 컨텍스트(기억) 지우기", "더 높은 성능의 컴퓨터 구매하기", "코드 작성 속도 2배로 올리기"]
    answer: 0
    explanation: "SDD 워크플로우에서는 단계 사이에 AI의 이전 대화 맥락(컨텍스트)을 지워, AI가 특정 하위 작업에만 온전히 집중할 수 있도록 합니다."
  - question: "AI에게 계획 없이 무작정 코드를 짜달라고 요청하는 기존의 방식을 일컫는 용어는 무엇인가요?"
    choices: ["바이브 코딩(Vibe coding)", "스펙 주도 개발(SDD)", "페어 프로그래밍(Pair programming)"]
    answer: 0
    explanation: "아무런 명세서 없이 기분이나 느낌대로 대화형 지시를 내리는 방식을 '바이브 코딩(Vibe coding)'이라고 부릅니다."
  - question: "개발자 핌지노(Pimzino)가 스펙 주도 개발에서 절대로 타협할 수 없는(non-negotiable) 필수 과정이라고 강조한 것은 무엇인가요?"
    choices: ["계획 단계와 구현 단계의 분리", "무조건 파이썬 언어만 사용하기", "AI의 오류를 무시하기"]
    answer: 0
    explanation: "핌지노는 설계(계획) 단계와 실제 코드를 작성하는 구현 단계를 확실하게 나누어 진행하는 것이 성공적인 AI 코딩의 필수 조건이라고 강조했습니다."
lang: ko
ref: 2026-05-22-Show-HN-Spec-Driven-Development-Workflow-for-Claude-Code
audio: 2026-05-22-Show-HN-Spec-Driven-Development-Workflow-for-Claude-Code.mp3
permalink: /2026/05/22/Show-HN-Spec-Driven-Development-Workflow-for-Claude-Code/
---

상상해보세요. 여러분이 꿈에 그리던 전원주택을 짓기 위해 베테랑 건축가와 시공업자를 고용했습니다. 그런데 현장에 나가서 이렇게 말합니다. "저기요, 그냥 살기 좋고 예쁜 2층 집 하나 지어주세요. 주방은 좀 넓었으면 좋겠고, 햇빛이 잘 들어왔으면 하네요. 전문가시니까 알아서 잘 부탁합니다!"

과연 어떤 결과가 나올까요? 아마도 거실 한복판에 변기가 덩그러니 놓여 있거나, 2층으로 올라가는 계단이 엉뚱하게 천장으로 막혀 있는 황당한 집이 완성될지도 모릅니다. 

지금까지 우리가 인공지능(AI) 코딩 비서를 사용할 때 정확히 이런 방식을 고수해 왔습니다. 챗GPT나 클로드 같은 AI에게 "이런 기능이 있는 앱 하나 만들어줘"라고 대화창에 툭 던진 뒤, AI가 마법처럼 완벽한 프로그램을 단숨에 뱉어내기를 기대한 것이죠. 전문가들은 이렇게 뚜렷한 계획이나 명세서 없이 기분이나 느낌 가는 대로 지시를 내리는 방식을 일명 **'바이브 코딩(Vibe coding)'**이라고 부릅니다 [[From VibeCodingto Shipping: MySpec-DrivenWorkflow... | SunDr](https://www.sundr.dev/blog/spec-driven-development-claude-code), [Spec-Driven Development with Claude Code: Build It Right](https://solguruz.com/blog/spec-driven-development-with-claude-code/)]. 

하지만 최근 소프트웨어 개발자들 사이에서는 '클로드 코드(Claude Code, 코딩에 특화된 AI 에이전트 도구)'를 다루는 완전히 새로운 접근법이 화제입니다. AI에게 무작정 코드를 짜라고 시키는 대신, 꼼꼼한 '설계도(Spec)'부터 작성하게 하는 **스펙 주도 개발(Spec-Driven Development, 이하 SDD)**입니다 [[Claude Code Spec-Driven Development Implementation Guide](https://github.com/papaoloba/spec-based-claude-code)]. 

## 이게 왜 중요한가요? (Why It Matters)

AI가 코딩을 다 해준다고 했을 때, 우리는 작업 속도가 단숨에 수십 배 빨라질 것이라 환호했습니다. 하지만 현실은 달랐습니다. 프로젝트가 조금만 복잡해져도 AI와의 작업은 순식간에 번거로운 짐(cumbersome)이 되곤 했습니다 [[ClaudeCode:Spec-DrivenDevelopment(SDD)](https://mifkata.com/blog/2026/01/claude-code-spec-driven-development/)]. AI가 앞뒤 맥락을 잊어버리거나, 한쪽을 고치면 다른 쪽을 망가뜨리는 일이 반복되었기 때문입니다.

실제로 한 현업 개발자는 AI 비서를 도입하고 대화형으로만 지시했을 때, 생산성이 오히려 19%나 떨어지는 '생산성 둔화(slowdown)'를 겪었다고 고백했습니다 [[From VibeCodingto Shipping: MySpec-DrivenWorkflow... | SunDr](https://www.sundr.dev/blog/spec-driven-development-claude-code)]. 엉망이 된 코드를 사람이 일일이 찾아내어 수습하고 디버깅(오류 수정)하느라 시간을 더 허비한 것이죠. 

하지만 작업 방식을 '스펙 주도 개발(SDD)'로 바꾼 후, 이 19%의 손실은 기적처럼 실질적인 생산성 향상(real lift)으로 돌아왔습니다 [[From VibeCodingto Shipping: MySpec-DrivenWorkflow... | SunDr](https://www.sundr.dev/blog/spec-driven-development-claude-code)]. 우리가 AI에게 원하는 것은 장난감이 아니라 실제 고객이 쓸 수 있는 수준(production-ready)의 견고한 프로그램입니다. 이를 위해서는 전문가 수준의 개발 관행(professional software development practices)을 유지하는 SDD가 필수적입니다 [[Claude Code Spec-Driven Development Implementation Guide](https://github.com/papaoloba/spec-based-claude-code)].

## 쉽게 이해하기 (The Explainer)

스펙 주도 개발(SDD)은 거대한 작업을 두 가지 차원(two dimensions)으로 날카롭게 쪼개는 것이 핵심입니다 [[Show HN: Spec-Driven Development Workflow for Claude Code](https://news.ycombinator.com/item?id=48231575)].

**1. 철저한 사전 조사 (Research)**
집을 짓기 전 땅의 상태를 검사하듯, 복수의 AI 에이전트를 투입해 현재 시스템의 상태와 문제점을 입체적으로 분석합니다 [[Spec-DrivenDevelopmentwithClaudeCodein Action | alexop.dev](https://alexop.dev/posts/spec-driven-development-claude-code-in-action/)].

**2. 흔들리지 않는 설계도 작성 (Spec Creation)**
가장 중요한 단계입니다. 조사 결과를 바탕으로 요구사항(requirements)과 시스템 디자인을 담은 명세서 문서를 만듭니다 [[Show HN: Spec-Driven Development Workflow for Claude Code](https://news.ycombinator.com/item?id=48231575)]. 이는 인간과 AI 사이의 흔들리지 않는 서면 계약서(written spec contracts)가 됩니다 [[Spec-DrivenDevelopmentwithClaudeCode](https://greeto.me/blog/spec-driven-development-claude-code-in-action)].

**3. 작업의 파편화 (Task Decomposition)**
아무리 똑똑한 AI라도 복잡한 시스템을 한 번에 만들 순 없습니다. 전체 작업을 아주 작은 단위의 하위 작업(subtasks)으로 잘게 쪼갭니다 [[Show HN: Spec-Driven Development Workflow for Claude Code](https://news.ycombinator.com/item?id=48231575)].

**4. 단계별 구현 및 검증 (Implementation & Verification)**
쪼개진 작업들을 하나씩 순서대로 실행하며 코드를 작성합니다. 이때 한 번에 저장하지 않고, 의미 있는 최소 단위로 저장하는 원자적 커밋(atomic commits) 방식을 사용해 안전성을 높입니다 [[Spec-DrivenDevelopmentwithClaudeCode](https://greeto.me/blog/spec-driven-development-claude-code-in-action)].

**비유하자면 이렇습니다.** 
회의실 화이트보드에 온갖 아이디어를 적으며 토론을 마쳤습니다. 이제 구체적으로 '창문 디자인' 하나에만 집중해야 하는데, 보드에 '지붕 색깔'이나 '배관 위치' 같은 낙서가 남아 있다면 어떨까요? 작업자는 헷갈리기 마련입니다.

그래서 SDD에서는 매 단계가 끝날 때마다 **'AI의 컨텍스트(기억 맥락)를 완전히 지워버리는 것(clear context)'**을 원칙으로 합니다 [[Show HN: Spec-Driven Development Workflow for Claude Code](https://news.ycombinator.com/item?id=48231575)]. 머릿속을 백지로 만들고, 오직 방금 완성된 '설계도'와 '지금 당장의 목표'만 다시 쥐어주는 것이죠. 이렇게 하면 AI가 환각(할루시네이션, 거짓 정보를 마치 사실인 양 말하는 현상)에 빠지지 않고 눈앞의 작업에만 매섭게 집중할 수 있습니다.

## 어디까지 와 있나? (Where We Stand)

이 방식의 효과가 입증되면서, 전 세계 개발자들은 이 과정을 자동화해 주는 도구들을 내놓고 있습니다.

*   **ShipSpec:** 개발자가 설계도를 직접 쓸 필요 없이, AI가 프로젝트를 분석해 3개의 문서 파일로 설계도를 자동 생성해 줍니다 [[ShowHN:SpecDrivenDevelopmentPluginforClaudeCode](https://news.ycombinator.com/item?id=46591238)].
*   **sddw:** 코딩을 수행할 AI 본인에게 직접 자신의 작업 설계도를 쓰게 만듭니다. 스스로 계획을 세우고 작은 단위(atomic tasks)로 일을 처리하게 돕죠 [[Spec-drivendevelopmentworkflow- how to get production-ready...](https://www.linkedin.com/pulse/spec-driven-development-workflow-how-get-code-from-ai-makarevych-xolxf)].
*   **claude-code-spec-workflow:** 개발자 핌지노(Pimzino)가 공개한 이 패키지는 깃허브에서 3,700개 이상의 별을 받으며 폭발적인 인기를 끌고 있습니다 [[GitHub - Pimzino/claude-code-spec-workflow: Automatedworkflows...](https://github.com/Pimzino/claude-code-spec-workflow)]. 핌지노는 "계획 세션과 구현 세션을 분리하는 것은 타협할 수 없는(non-negotiable) 필수 조건"이라고 강조합니다 [[Spec-Driven Development with Claude Code | Build This Now](https://www.buildthisnow.com/blog/guide/mechanics/spec-driven-development)].

## 앞으로 어떻게 될까? (What's Next)

미래의 개발자는 컴퓨터 앞에서 밤을 새우는 대신, 자신의 아이디어를 음성으로 구술하게 될 것입니다. 그러면 AI가 그 목소리를 분석해 완벽한 '설계도(Spec)'를 쓰고, 자율적으로 코드를 작성한 뒤 테스트까지 마칩니다. 실제로 글로벌 기업 노션(Notion)은 이미 이러한 방식의 AI 워크플로우를 내부적으로 구축하고 있습니다 [[Spec-drivendevelopment: The AI engineeringworkflowat Notion](https://www.lennysnewsletter.com/p/spec-driven-development-the-ai-engineering)].

결국 인공지능은 단순히 명령을 받아 적는 타자기를 넘어, 스스로 계획하고 검증하는 자가 발전 시스템(Self-Developing AI System)으로 진화하고 있습니다 [[A Config-Driven Way to BuildSpec-DrivenWorkflowsforClaude...](https://www.linkedin.com/pulse/config-driven-way-build-spec-driven-workflows-claude-code-makarevych-qjmwf)]. 우리는 이제 충동적인 '바이브 코딩'에서 벗어나, 큰 그림을 그리는 '총괄 건축가'가 되어 AI '건축 로봇' 군단을 지휘하는 시대를 맞이하고 있습니다.

## AI's Take
인공지능은 마법 지팡이가 아니라 뛰어난 일꾼입니다. 일꾼이 제 실력을 발휘하려면, 우리가 먼저 '무엇을 원하는지' 명확한 청사진을 제시해야 한다는 당연한 진리를 다시금 깨닫게 됩니다.

## 참고자료
1. [Spec-DrivenDevelopmentwithClaudeCodein Action | alexop.dev](https://alexop.dev/posts/spec-driven-development-claude-code-in-action/)
2. [GitHub - Pimzino/claude-code-spec-workflow: Automatedworkflows...](https://github.com/Pimzino/claude-code-spec-workflow)
3. [A Config-Driven Way to BuildSpec-DrivenWorkflowsforClaude...](https://www.linkedin.com/pulse/config-driven-way-build-spec-driven-workflows-claude-code-makarevych-qjmwf)
4. [From VibeCodingto Shipping: MySpec-DrivenWorkflow... | SunDr](https://www.sundr.dev/blog/spec-driven-development-claude-code)
5. [Spec-DrivenDevelopmentwithClaudeCode](https://greeto.me/blog/spec-driven-development-claude-code-in-action)
6. [ClaudeCode:Spec-DrivenDevelopment(SDD)](https://mifkata.com/blog/2026/01/claude-code-spec-driven-development/)
7. [Claude Code Spec-Driven Development Implementation Guide](https://github.com/papaoloba/spec-based-claude-code)
8. [Spec-Driven Development with Claude Code: Build It Right](https://solguruz.com/blog/spec-driven-development-with-claude-code/)
9. [Spec-Driven Development with Claude Code | Build This Now](https://www.buildthisnow.com/blog/guide/mechanics/spec-driven-development)
10. [Spec-Driven Development with Claude Code: A Guided Tutorial](https://www.datacamp.com/tutorial/spec-driven-development-with-claude-code)
11. [Show HN: Spec-Driven Development Workflow for Claude Code](https://news.ycombinator.com/item?id=48231575)
12. [Claude Code Spec Workflow Guide (2026) | ClaudHQ](https://claudhq.com/claude-code-spec-workflow-guide/)
13. [Spec-drivendevelopmentworkflow- how to get production-ready...](https://www.linkedin.com/pulse/spec-driven-development-workflow-how-get-code-from-ai-makarevych-xolxf)
14. [ClaudeEngineer is INSANE... Upgrade YourClaudeCodeWorkflow](https://www.youtube.com/watch?v=6Rg5M69bMgQ)
15. [ShowHN:SpecDrivenDevelopmentPluginforClaudeCode](https://news.ycombinator.com/item?id=46591238)
16. [Spec-drivendevelopment: The AI engineeringworkflowat Notion](https://www.lennysnewsletter.com/p/spec-driven-development-the-ai-engineering)