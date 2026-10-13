---
layout: post
title: "AI가 스스로 자신의 '지능 껍데기'를 수정한다고? 스스로 진화하는 AI 에이전트의 시대"
description: "AI 에이전트가 인간의 도움 없이 스스로 자신의 작동 방식인 '하네스(harness)'를 개선하고 진화시키는 최신 기술 연구를 쉽게 설명합니다."
summary: "구글 딥마인드의 최신 연구는 AI 에이전트가 복잡한 수동 엔지니어링 없이 스스로 자신의 작동 환경(하네스)을 수정하고 최적화하여 자율적인 소프트웨어 개발의 길을 열고 있음을 보여줍니다."
tags: [AI, GoogleDeepMind, 에이전트, AutoHarness, Evo2]
image: 2026-10-14-Google-DeepMind-paper-trains-an-agent-to-rewrite-its-own-harness.jpg
image_alt: "AI 에이전트가 스스로 코드를 작성하고 자신의 작동 체계를 수정하는 미래지향적인 모습을 묘사한 일러스트"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "인간이 일일이 규칙을 정해주던 시대는 저물고 있습니다. AI가 자신의 한계를 스스로 인식하고 고쳐나가는 능력은 진정한 자율 에이전트로 나아가는 가장 중요한 열쇠가 될 것입니다."
quiz:
  - question: "AI 에이전트의 '하네스(harness)'란 무엇인가요?"
    choices: ["AI의 기억 장치", "모델과 작업 사이를 연결하는 '접착제' 역할의 소프트웨어 체계", "AI의 학습 데이터셋"]
    answer: 1
    explanation: "하네스는 AI 모델과 해결해야 할 작업 사이에서 plumbing(배관)이나 glue(접착제) 역할을 하여 AI가 원활히 작동하도록 돕는 소프트웨어 scaffolding(비계/틀)입니다."
  - question: "구글 딥마인드의 AutoHarness 연구는 어떤 방식으로 작동하나요?"
    choices: ["인간이 매일 새로운 코드를 직접 입력합니다.", "제미나이(Gemini)가 환경으로부터 받은 피드백을 활용해 반복적인 정제 과정을 거쳐 스스로 코드를 생성합니다.", "기존의 규칙을 그대로 유지합니다."]
    answer: 1
    explanation: "AutoHarness는 제미나이(Gemini)-2.5-Flash가 환경으로부터 얻은 피드백을 토대로 반복적인 개선 과정을 거쳐 스스로 최적의 코드 하네스를 만들어내는 방식입니다."
  - question: "Evo2 프레임워크의 핵심 목표는 무엇인가요?"
    choices: ["인간의 개입을 극대화한다.", "AI의 기본 언어 모델을 완전히 교체한다.", "작업 실행자(task executor)를 바꾸지 않고 에이전트의 워크플로우와 정책을 개선한다."]
    answer: 2
    explanation: "Evo2는 작업 실행자 자체를 건드리지 않고, 에이전트의 하네스 수정 기록과 평가 데이터를 학습 데이터로 활용하여 워크플로우와 정책을 더 나은 방향으로 개선하는 프레임워크입니다."
lang: ko
ref: 2026-10-14-Google-DeepMind-paper-trains-an-agent-to-rewrite-its-own-harness
audio: 2026-10-14-Google-DeepMind-paper-trains-an-agent-to-rewrite-its-own-harness.mp3
permalink: /2026/10/14/Google-DeepMind-paper-trains-an-agent-to-rewrite-its-own-harness/
---

상상해보세요. 여러분이 새로운 조수를 채용했습니다. 그런데 이 조수는 일을 시킬 때마다 "이런 식으로 일하는 게 더 효율적일 것 같아요"라고 말하며 스스로 일하는 방식(매뉴얼)을 계속 업그레이드합니다. 심지어 여러분이 지시하지 않아도 자기만의 도구와 기억 체계를 스스로 재정비합니다. 공상과학 영화 속 이야기가 아닙니다. 구글 딥마인드(Google DeepMind)가 발표한 최신 연구들이 보여주는 '스스로 진화하는 AI 에이전트'의 모습입니다.

### 왜 이 기술이 중요한가요?

그동안 AI 에이전트를 만드는 과정은 매우 고통스럽고 비용이 많이 드는 '수동 노동'의 연속이었습니다. 에이전트가 어떤 작업을 하려면 인간 엔지니어가 그 작업을 위한 구체적인 규칙과 제약 사항을 일일이 정의해줘야 했기 때문입니다. 이 연결 고리를 만드는 과정을 업계에서는 '하네스(harness)'라고 부르는데, 사실 이 과정이 AI 에이전트 도입의 가장 큰 걸림돌이었습니다. [출처: This AutoHarness paper(from Google DeepMind) is the most...](https://www.linkedin.com/posts/omarsar_this-autoharness-paper-from-google-deepmind-activity-7437877601853153280-uWyl)

하지만 이제는 다릅니다. AI가 스스로 자신의 작동 체계를 수정하고 최적화할 수 있게 되면, 인간의 개입 없이도 AI 에이전트가 다양하고 복잡한 작업을 자율적으로 수행하는 세상이 빠르게 다가올 것입니다. 이는 AI 기술이 연구실 수준을 넘어 실무 현장에 '규모 있게(scalable)' 배치되는 중요한 분기점이 될 것입니다.

### 쉽게 이해하기: AI의 '접착제', 하네스

기술적인 이야기를 조금만 더 쉽게 풀어볼까요? AI 에이전트는 보통 '두뇌' 역할을 하는 거대언어모델(LLM)과, 이 두뇌가 외부 세상과 소통할 수 있게 돕는 '하네스'라는 틀로 구성됩니다. [출처: AutoHarness: improving LLM agents by automatically ...](https://arxiv.org/pdf/2603.03329)

이렇게 비유하면 쉽습니다. AI 에이전트를 '천재 화가'라고 해봅시다. 화가가 그림을 그리려면 붓도 있어야 하고(도구), 캔버스도 준비해야 하고(환경), 어떤 그림을 그릴지 지시사항(프롬프트)도 명확해야 합니다. 여기서 화가의 도구함과 그림 그리는 과정을 돕는 작업대 전체를 '하네스'라고 보면 됩니다. 기존에는 인간이 일일이 붓을 챙겨주고 작업대 높이를 조절해줬다면, 이제는 화가(AI)가 스스로 "이번 그림에는 이런 붓이 필요하겠군"이라며 도구함의 구조를 바꾸는 것입니다.

구글 딥마인드의 **AutoHarness**는 제미나이(Gemini)-2.5-Flash 모델이 환경으로부터 얻은 피드백을 이용해, 스스로 더 나은 '작업대'를 설계하도록 돕습니다. [출처: AutoHarness: improving LLM agents by automatically ...](https://arxiv.org/pdf/2603.03329), [출처: AutoHarness | DAIR.AI Academy](https://academy.dair.ai/papers/autoharness) 

또한 **Evo2**라는 프레임워크는 에이전트가 하네스를 고치면서 얻은 데이터를 학습 데이터로 재활용합니다. 즉, 고치고 실험해본 경험을 데이터로 쌓아 자신의 워크플로우(업무 흐름)를 스스로 강화하는 것이죠. [출처: Google DeepMind paper trains an agent to rewrite its own harness](https://runtimewire.com/article/google-deepmind-evo2-agent-harness-co-evolution)

### 어디까지 왔을까요?

현재 AI 연구 분야에서는 스스로 구조를 개선하는 여러 흥미로운 방식들이 논의되고 있습니다. 

첫째, **AutoHarness**는 에이전트가 코드를 직접 작성하여 스스로 하네스를 만들어냅니다. 인간이 복잡한 규칙을 수동으로 짜는 것보다, 소량의 반복적인 정제 과정을 거친 자동화된 하네스가 더 효율적인 성능을 보여주기도 합니다. [출처: [2603.03329] AutoHarness](https://arxiv.org/abs/2603.03329)

둘째, **Self-Harness**는 에이전트가 외부의 강력한 지원군이나 인간의 도움 없이 독립적으로 자신의 작동 환경을 개선하는 새로운 패러다임입니다. [출처: [2606.09498] Self-Harness: Harnesses That Improve Themselves](https://arxiv.org/abs/2606.09498)

셋째, **RRSI(재귀적 자기 개선)** 기술은 구글 클라우드 AI 연구팀 등이 발표한 것으로, 프롬프트, 도구, 기억 체계, 제어 흐름, 심지어는 하위 에이전트(sub-agents)까지 AI가 직접 다시 작성하게 합니다. [출처: Paper AutoHarness from DeepMind Changes AI Agents 1](https://www.youtube.com/watch?v=4Xczb2z3N_w)

현장 전문가들은 "모델 자체의 성능 차이보다 어떤 하네스를 쓰느냐에 따른 성능 격차가 더 크다"라고 입을 모읍니다. 아무리 똑똑한 모델이라도 도구를 활용하는 방식이 나쁘면 제 능력을 발휘하지 못하기 때문입니다. [출처: Auto-Harness Synthesis - Just Understanding Data](https://understandingdata.com/posts/auto-harness-synthesis/)

### 앞으로의 미래

앞으로 AI 에이전트는 정적인 존재가 아닐 것입니다. 오늘 만난 AI와 1,000일 뒤의 AI는 그 구조와 기억, 도구가 완전히 다를 수 있습니다. [출처: The Harness That Learns You | XO Docs](https://docs.xo.builders/research/perspectives/the-harness-that-learns-you) 

우리는 이제 'AI에게 무엇을 시킬까'를 고민하는 단계를 넘어, 'AI가 스스로 어떤 도구와 방식을 선택해 문제를 해결할지' 지켜보는 단계로 나아가고 있습니다. 인간의 개입이 최소화된, 진정한 의미의 자율 에이전트가 우리 일상을 어떻게 바꿔놓을지 함께 지켜보는 것은 어떨까요?

## 참고자료

1. [Google DeepMind - Wikipedia](https://en.wikipedia.org/wiki/Google_DeepMind)
2. [This AutoHarness paper(from Google DeepMind) is the most...](https://www.linkedin.com/posts/omarsar_this-autoharness-paper-from-google-deepmind-activity-7437877601853153280-uWyl)
3. [Google DeepMind](https://deepmind.google/)
4. [AI has grown beyond human knowledge, says Google's DeepMind unit](https://www.zdnet.com/article/ai-has-grown-beyond-human-knowledge-says-googles-deepmind-unit/)
5. [The Harness That Learns You | XO Docs](https://docs.xo.builders/research/perspectives/the-harness-that-learns-you)
6. [Google DeepMind paper trains an agent to rewrite its own harness](https://runtimewire.com/article/google-deepmind-evo2-agent-harness-co-evolution)
7. [AutoHarness: improving LLM agents by automatically ...](https://arxiv.org/pdf/2603.03329)
8. [[2603.03329] AutoHarness: improving LLM agents by ...](https://arxiv.org/abs/2603.03329)
9. [AutoHarness: LLM Agents That Build Own Scaffolding | aiHola](https://aihola.com/article/autoharness-llm-agent-code-harness)
10. [Auto-Harness Synthesis - Just Understanding Data](https://understandingdata.com/posts/auto-harness-synthesis/)
11. [AutoHarness | DAIR.AI Academy](https://academy.dair.ai/papers/autoharness)
12. [[2606.09498] Self-Harness: Harnesses That Improve Themselves](https://arxiv.org/abs/2606.09498)
13. [Paper AutoHarness from DeepMind Changes AI Agents 1](https://www.youtube.com/watch?v=4Xczb2z3N_w)