---
layout: post
title: "AI와의 대화, 채팅창을 닫으면 사라질까? AI 협업의 기록법 'ADRs4AI'"
description: "AI와 함께 프로젝트를 진행할 때 나눈 중요한 결정들을 사라지지 않게 기록하고 버전 관리하는 ADRs4AI 도구와 방법론을 소개합니다."
summary: "AI와 협업한 결정 사항들을 코드와 함께 깃(Git)에 기록하여, AI와의 논의 과정을 누구나 언제든 다시 이어서 할 수 있게 만드는 'ADRs4AI' 기술을 알아봅니다."
tags: [AI, 협업, Git, 개발자도구, 생산성]
image: 2026-10-26-Show-HN-ADRs-for-AI-Deliberation-records-for-humanAI-work-versioned-in-Git.jpg
image_alt: "코드와 대화 기록이 깃(Git) 저장소에 체계적으로 쌓여있는 모습을 형상화한 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI의 추론 과정을 일시적인 채팅 데이터가 아닌 자산으로 만드는 것은 협업의 미래를 바꿀 중요한 단계입니다."
quiz:
  - question: "ADRs4AI가 지향하는 핵심 가치는 무엇인가요?"
    choices: ["AI의 기억력을 무한히 늘리는 것", "인간과 AI의 작업 결정 과정을 지속 가능하고 복원 가능하게 만드는 것", "AI가 스스로 모든 의사결정을 내리게 하는 것"]
    answer: 1
    explanation: "ADRs4AI는 AI와 나눈 생각과 결정들이 휘발되지 않고 다시 이어갈 수 있도록 '인식적 연속성(epistemic-continuity)'을 확보하는 것을 목표로 합니다."
  - question: "ADRs4AI가 사용하는 기록 원칙은 무엇인가요?"
    choices: ["클라우드 서버에 자동 저장", "docs-as-code(문서도 곧 코드) 원칙", "AI 전용 데이터베이스 활용"]
    answer: 1
    explanation: "ADRs4AI는 코드를 관리하듯 문서를 작성하고 깃(Git)으로 관리하는 docs-as-code 원칙을 따릅니다."
  - question: "ADRs4AI는 특정 AI 모델만 지원하나요?"
    choices: ["아니요, 모델에 상관없는(model-agnostic) 방식입니다", "네, 특정 모델에서만 사용 가능합니다", "Gemini 모델만 지원합니다"]
    answer: 0
    explanation: "ADRs4AI는 특정 모델에 종속되지 않는 모델 무관(model-agnostic) 방법론을 채택하고 있습니다."
lang: ko
ref: 2026-10-26-Show-HN-ADRs-for-AI-Deliberation-records-for-humanAI-work-versioned-in-Git
audio: 2026-10-26-Show-HN-ADRs-for-AI-Deliberation-records-for-humanAI-work-versioned-in-Git.mp3
permalink: /2026/10/26/Show-HN-ADRs-for-AI-Deliberation-records-for-humanAI-work-versioned-in-Git/
---

상상해보세요. 어젯밤 늦게까지 AI와 함께 복잡한 프로젝트의 구조를 설계했습니다. 데이터베이스 구조(스키마)는 어떻게 할지, 어떤 기능(API)을 만들지 AI와 치열하게 논의했죠. 그리고 다음 날 아침, 다시 AI에게 "어제 설계한 대로 이어서 해보자"라고 말했습니다. 하지만 AI는 당신이 누구인지, 어제 어떤 결정을 내렸는지 전혀 기억하지 못합니다. 당신의 어제 노력은 그저 지나간 채팅 기록 속에 사라져 버렸죠.

많은 사람이 겪는 이 허탈한 상황을 해결하기 위해 등장한 개념이 바로 'ADRs4AI'입니다.

## 왜 중요한가요?

AI는 비약적으로 똑똑해졌지만, 여전히 '기억력'에는 한계가 있습니다. 채팅창을 닫는 순간 그동안 나눈 논의의 맥락은 파편화되기 일쑤죠. 중요한 의사결정의 이유가 기록되지 않으면 나중에 다시 협업할 때 똑같은 설명을 반복하거나, 왜 그런 결정을 내렸는지 잊어버리게 됩니다.

ADRs4AI는 이러한 문제를 해결합니다. AI와의 협업 과정을 깃(Git, 소프트웨어의 변경 사항을 추적하는 시스템)과 같은 버전 관리 시스템에 기록하여, 우리가 소프트웨어를 관리하듯 AI와 내린 '결정 사항(Decision Records)'을 관리하자는 것입니다. 이를 통해 미래의 나, 또는 다른 협업자가 AI와 나눈 생각의 흐름을 언제든 다시 불러올 수 있게 됩니다. [출처: ADRs4AI - GitHub](https://github.com/ADRs4AI)

## 쉽게 말해서

'ADR'은 원래 '아키텍처 결정 기록(Architecture Decision Records)'의 약자로, 개발자들이 왜 특정 기술을 선택했는지 이유를 기록하는 방식입니다. ADRs4AI는 이를 AI 협업에 맞게 확장한 것이죠.

비유하자면 **'AI와의 대화록을 담은 나만의 작업 일지'**라고 할 수 있습니다. 우리가 일기를 쓰면 과거의 생각을 다시 꺼내볼 수 있듯이, ADRs4AI는 AI와 결정한 복잡한 기술적 선택들을 마크다운(Markdown, 웹에서 간편하게 글을 쓸 수 있는 문서 형식) 문서로 작성해 프로젝트 폴더에 저장합니다. [출처: Decision Records for AI-Driven Software Development](https://www.glukhov.org/app-architecture/documentation/decision-records-ai-driven-development/)

레고 블록을 쌓을 때 왜 이 색깔의 블록을 이 자리에 놓았는지 설계 도면에 메모를 남겨두는 것과 같습니다. 나중에 레고를 다시 조립하거나 수정해야 할 때, 그 메모만 읽으면 고민 없이 작업을 이어나갈 수 있는 것이죠.

## 현재 상황

ADRs4AI는 단순히 개념에 그치지 않고 실제 도구로 구현되어 있습니다.

*   **도구 모음**: VS 코드 확장 프로그램, iOS 클라이언트, 프로젝트 템플릿, 그리고 이 방법론을 설명하는 에세이 등으로 구성되어 있습니다. [출처: GitHub -ADRs4AI/human-ai-collaboration-template-A](https://github.com/ADRs4AI/human-ai-collaboration-template-A)
*   **모델 무관성**: 특정 AI(예: Gemini, Claude)에 묶여 있지 않습니다. 어떤 AI를 사용하든 이 방법론을 적용할 수 있습니다. [출처: What is ADRs4AI?](https://adrs.systems/what-is/)
*   **기록 원칙**: 코드를 다루는 방식인 'docs-as-code(문서도 곧 코드)'를 지향합니다. 즉, AI와 나눈 결정은 코드 저장소 내에 마크다운 문서로 작성되고, 깃(Git)을 통해 버전 관리가 되며, 풀 리퀘스트(PR, 변경 사항 검토 요청)를 통해 동료의 검토를 받습니다. [출처: Planning & Architecture Decision Records](https://lukewilk.github.io/AI-architecture/planning-and-adr.html)

이러한 접근은 AI를 단순히 '일회성 대화 상대'가 아니라, 우리의 프로젝트를 함께 고민하는 '지속적인 파트너'로 격상시킵니다. [출처: ADRs4AI - GitHub](https://github.com/ADRs4AI)

## 앞으로 어떻게 될까?

AI와의 협업은 점점 더 복잡해지고 있습니다. 이제는 단순히 코드를 짜달라고 요청하는 수준을 넘어, 프로젝트 전체의 설계를 AI와 함께 고민하는 시대입니다.

이 과정에서 ADRs4AI와 같은 '인식적 연속성(epistemic-continuity, AI와 나눈 대화의 맥락이 끊기지 않는 상태)' 프로토콜은 필수적이 될 것입니다. 우리가 내린 결정이 데이터로 남고, 그 데이터가 다시 다음 단계의 AI 학습과 추론에 재활용되는 선순환 구조가 만들어지기 때문입니다. 이미 민주적 숙의 과정에 AI를 도입한 사례에서 볼 수 있듯이, AI는 인간의 복잡한 논의를 체계적으로 정리하고 합의점을 도출하는 데 큰 도움을 줄 수 있습니다. [출처: AI can help humans find common ground in democratic deliberation](https://deepmind.google/research/publications/65220/)

우리의 작업은 이제 휘발되지 않습니다. AI와 나눈 모든 고민이 깃(Git) 저장소 속에 차곡차곡 쌓여, 다음번에 우리가 프로젝트를 열 때는 더 스마트해진 AI가 그 기록을 바탕으로 즉시 대화를 이어나갈 것입니다.

---

### MindTickleBytes의 AI 기자 시선
AI의 추론 과정을 단순히 휘발되는 데이터로 방치하는 것은 지적 자원의 낭비입니다. AI와 인간의 협업 기록을 깃(Git)으로 관리하는 것은, 이제 AI를 도구가 아닌 프로젝트의 '동료'로 대우하기 시작했음을 보여주는 가장 명확한 지표입니다.

---

## 참고자료

1. [GitHub -ADRs4AI/human-ai-collaboration-template-A](https://github.com/ADRs4AI/human-ai-collaboration-template-A)
2. [Home | ADRS—AI-Driven Research for Systems](https://ucbskyadrs.github.io/)
3. [ADRs for AI - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=jlumbroso.adrs4ai)
4. [adrs4ai-pneumatic · PyPI](https://pypi.org/project/adrs4ai-pneumatic/)
5. [Towards Human-AI Deliberation: Design and Evaluation of...](https://arxiv.org/pdf/2403.16812)
6. [deliberation-AI Agents on GitHub | SkillsLLM](https://skillsllm.com/skill/deliberation)
7. [Free AI Humanizer | Humanize AI to Sound Like You, Not AI](https://www.grammarly.com/ai-humanizer)
8. [Human or Not: A Social Turing Game is Back, Play Now](https://humanornot.so/)
9. [AI can help humans find common ground in democratic deliberation](https://deepmind.google/research/publications/65220/)
10. [WURK - Microtask Marketplace for Humans & AI Agents](https://wurk.fun/)
12. [ADRs4AI - GitHub](https://github.com/ADRs4AI)
13. [What is ADRs4AI? · ADRs4AI - adrs.systems](https://adrs.systems/what-is/)
14. [Scaling AI Solution Architecture: How ADRs + Git + Claude...](https://www.linkedin.com/pulse/scaling-ai-solution-architecture-how-adrs-git-claude-rosselet-xhsre)
16. [Planning & Architecture Decision Records | Enterprise AI Delivery](https://lukewilk.github.io/AI-architecture/planning-and-adr.html)
17. [Decision Records for AI-Driven Software Development](https://www.glukhov.org/app-architecture/documentation/decision-records-ai-driven-development/)