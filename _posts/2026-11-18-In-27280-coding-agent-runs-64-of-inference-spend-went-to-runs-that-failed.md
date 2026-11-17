---
layout: post
title: "AI 코딩 도우미, 실패할 때마다 '돈 먹는 하마' 된다? 27,280번의 실패 분석"
description: "AI 코딩 에이전트가 잦은 실패와 재시도로 인해 예산을 초과하고 개발자의 디버깅 시간을 늘리는 문제점을 심층 분석합니다. 비용 절감 및 효율성 증대를 위한 방안을 모색합니다."
summary: "AI 코딩 에이전트의 잦은 실패가 막대한 비용 낭비와 디버깅의 어려움을 야기하며, 전체 추론 비용의 64%를 차지한다는 분석 결과를 소개합니다."
tags: ["AI", "코딩 에이전트", "개발", "비용", "효율성", "LLM"]
image: 2026-11-18-In-27280-coding-agent-runs-64-of-inference-spend-went-to-runs-that-failed.jpg
image_alt: "AI 코딩 에이전트가 복잡한 코드 문제를 해결하려다 실패하는 모습, 그래프로 표시된 비용 증가"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 코딩 에이전트의 잠재력을 현실화하려면, 실패의 근본 원인을 파악하고 이를 해결하기 위한 기술적, 운영적 개선이 필수적입니다. 단순히 더 강력한 모델을 사용하는 것만으로는 부족하며, 효율적인 제어와 검증 시스템 구축이 시급합니다."
quiz:
  - question: "AI 코딩 에이전트 실행에서 가장 큰 비용을 차지하는 부분은 무엇인가요?"
    choices: ["성공적인 작업 완료", "모델 학습 및 튜닝", "실패한 실행 및 재시도"]
    answer: 2
    explanation: "27,280번의 코딩 에이전트 실행 분석 결과, 실패한 실행이 전체 추론 비용의 64%를 차지했습니다. 이는 실패한 작업에 대한 재시도가 비용을 크게 증가시키기 때문입니다."
  - question: "AI 코딩 에이전트가 실패했을 때 개발자가 겪는 어려움은 무엇인가요?"
    choices: ["코드 이해도 증가", "비용 절감 효과", "디버깅의 어려움 및 비용 증대"]
    answer: 2
    explanation: "AI 코딩 에이전트의 실패는 이해하기 어려운 실행 흔적을 남겨 디버깅을 복잡하게 만들고, 반복되는 재시도로 인해 비용이 기하급수적으로 증가하는 문제를 야기합니다."
  - question: "AI 코딩 에이전트의 잠재적 효율성에 대한 OpenAI의 보고 내용은 무엇인가요?"
    choices: ["인간 개발자보다 10배 효율적", "연구 업무에 3.1일 분량의 작업량 제공", "실패율이 낮아 비용이 거의 들지 않음"]
    answer: 1
    explanation: "OpenAI는 코딩 에이전트가 인간 연구자 하루 업무량의 3.1일 분량을 제공한다고 보고했습니다. 그러나 이러한 효율성은 실패로 인한 비용 및 제어 문제로 인해 제약을 받을 수 있습니다."
lang: ko
ref: 2026-11-18-In-27280-coding-agent-runs-64-of-inference-spend-went-to-runs-that-failed
audio: 2026-11-18-In-27280-coding-agent-runs-64-of-inference-spend-went-to-runs-that-failed.mp3
permalink: /2026/11/18/In-27280-coding-agent-runs-64-of-inference-spend-went-to-runs-that-failed/
---

# AI 코딩 도우미, 실패할 때마다 '돈 먹는 하마' 된다? 27,280번의 실패 분석

개발자의 생산성을 마법처럼 끌어올려 줄 것으로 기대를 모았던 AI 코딩 에이전트(AI 기반 자동 프로그래밍 도구). 하지만 이 똑똑한 디지털 조력자가 잦은 실패를 거듭하면서, 기업과 개발자들에게 예상치 못한 '비용 폭탄'을 안겨주고 있다는 충격적인 분석 결과가 나왔습니다. 

비유하자면, 아주 영리하지만 고집이 센 조교에게 어려운 수학 문제를 풀게 맡긴 셈입니다. 조교가 답을 틀릴 때마다 오답노트를 만들기는커녕, 똑같은 실수를 반복하며 밤새도록 종이를 낭비하는 것과 정확히 닮아 있습니다. AI 코딩 에이전트가 왜 이렇게 많은 비용을 낭비하게 되는지, 그리고 이 문제를 어떻게 해결해야 할지 차근차근 살펴보겠습니다.

## 이게 왜 중요한가요?

소프트웨어 개발 현장에서 AI 코딩 에이전트는 이미 거대한 혁신의 상징입니다. 실제로 오픈에이아이(OpenAI)는 코딩 에이전트가 인간 연구자의 하루 업무량에 무려 **3.1일 분량**의 작업량을 거뜬히 소화해 낸다고 보고했습니다 [출처: OpenAI Reports Coding Agents at 3.1 Workdays per... - GravityDevOps](https://gravitydevops.com/daily-openai-research-agent-operations/). 반복적이고 지루한 코드 작성 업무를 AI가 대신 처리해 준다면, 개발자들은 훨씬 더 창의적이고 고차원적인 문제 해결에 집중할 수 있게 됩니다.

하지만 찬란한 장밋빛 전망 뒤에는 차가운 현실이 숨어 있습니다. 최근 총 27,280번에 달하는 코딩 에이전트의 실제 실행 과정을 정밀 분석한 결과, **전체 추론 비용(AI가 답변을 생성하고 사고하는 데 소모되는 컴퓨터 연산 비용)의 무려 64%가 실패한 실행에 지출**된 것으로 드러났습니다 [출처: In 27,280 coding agent runs, 64% of inference spend went to runs that failed](https://runta.com/blog/introducing-frontierharness-eval-v1-1/). 

단순히 몇 번의 실수로 치부하기에는 타격이 큽니다. 수많은 코딩 에이전트가 네트워크 타임아웃(응답 시간 초과), 외부 응용프로그램 인터페이스(API) 오류, 또는 문법에 맞지 않는 잘못된 코드 생성 등으로 인해 연달아 좌절하고 있으며, 이 실패들이 눈덩이처럼 불어나 프로젝트 예산을 소리 없이 잠식하고 있습니다.

## 쉽게 이해하기: AI 코딩 에이전트의 '실패 딜레마'

상상해 보세요. 여러분이 회사 프로젝트를 마감하기 위해 AI에게 새로운 로그인 기능을 만들어 달라고 요청했습니다. 인간 직원이었다면 중간에 막히면 상사에게 조언을 구하거나 방향을 틀겠지만, AI 코딩 에이전트는 다릅니다. 타임아웃이나 API 오류, 혹은 생성된 코드가 유효성 검사를 통과하지 못하면 **스스로 무한 재시도 루프에 빠지거나 엉뚱한 방향으로 달리기 시작**합니다 [출처: AI Coding Agent Timeout and Retry Costs: How Failed Runs... - ai-cost-estimator.com](https://ai-cost-estimator.com/blog/ai-coding-agent-timeout-retry-costs-failed-runs-budget). 쉽게 말해서, 요리사가 레시피를 착각해 요리를 망쳤을 때 원인을 분석하는 대신, 같은 재료로 실패한 요리를 수십 번씩 계속 만들어내는 것과 같습니다. 이 무분별한 반복 작업이 바로 막대한 비용 낭비의 주범입니다.

더 큰 문제는 이러한 실패가 **개발자의 디버깅(오류 수정) 시간을 더욱 복잡하고 고통스럽게 만든다**는 점입니다. 대규모 언어 모델(LLM, 인간의 언어를 이해하고 생성하는 거대한 인공지능 신경망) 기반의 코딩 에이전트가 실패할 때 남기는 흔적은 사람이 이해하기 매우 어렵습니다. 에이전트가 뱉어내는 원시 실행 흔적(raw execution traces)은 베테랑 개발자조차 해독하기 버거울 때가 많습니다 [출처: XAI for Coding Agent Failures: Transforming Raw Execution... - arxiv.org](https://arxiv.org/html/2603.05941v1). 마치 수천 가닥의 전선이 뒤엉킨 거대한 기계 장치 속에서, 고장 난 단 하나의 전선을 찾기 위해 난해한 설계도를 처음부터 끝까지 다시 읽어야 하는 상황과 같습니다.

실제로 대규모 오픈소스 저장소의 에이전트 실행 데이터 1,281개를 면밀히 분석한 연구에 따르면, 코딩 에이전트가 무너질 때는 공통적으로 **5가지 반복 가능한 실패 패턴**이 존재한다는 사실이 밝혀지기도 했습니다 [출처: Why coding agents fail in large codebases (and what to do... - sourcegraph.com](https://sourcegraph.com/blog/why-coding-agents-fail-large-codebases).

## 현재 상황: 제어와 검증의 중요성

이러한 문제를 해결하기 위해 업계에서는 다양한 대안과 솔루션을 쏟아내고 있습니다. 예를 들어, 문매스 테크놀로지가 선보인 'Zro' 같은 서비스는 코딩 에이전트 전용 비공개 AI 추론 서비스를 제공하며, 합리적인 요금제로 추론 비용을 통제할 수 있도록 돕습니다 [출처: Zro by MoonMath.ai | Private AI Inference for Coding Agents](https://zro.moonmath.ai/). 또한 오픈소스 모델 구동 도구인 '오라마(Ollama)' 등을 활용해 개발자가 로컬 환경에서 직접 AI 에이전트를 띄우고, 웹 브라우징이나 기억 장치(RAG 메모리) 기능을 안전하게 실험하는 사례도 늘고 있습니다 [출처: Unlimited AI Agents running locally with Ollama... - YouTube](https://www.youtube.com/watch?v=4UFrVvy7VlA).

그럼에도 불구하고 기술의 본질적인 과제는 변하지 않습니다. 에이전트가 엉뚱한 행동을 하거나 길을 잃지 않도록 얼마나 엄격하게 **제어(Control)**하고, 결과물이 올바른지 철저하게 **검증(Verification)**하느냐가 승패를 가르는 열쇠입니다. 오픈에이아이 역시 코딩 에이전트 운영에서 가장 중요한 교훈으로 이 세 가지 요소를 꼽은 바 있습니다 [출처: OpenAI Reports Coding Agents at 3.1 Workdays per... - GravityDevOps](https://gravitydevops.com/daily-openai-research-agent-operations/).

AI 에이전트가 오랜 시간에 걸쳐 대규모 작업을 수행할 때는, 모델을 어떤 것으로 선택하느냐에 따라 연쇄적인 파급 효과가 발생하기 때문에 상황을 통제하기가 까다로워집니다 [출처: Interactive benchmarks: evaluating model routing for AI agents](https://www.notdiamond.ai/blog/interactive-benchmarks-a-new-methodology-for-evaluating-model-routing?trk=public_post_comment-text). 이에 따라 일부 선도적인 시스템들은 각 에이전트의 작업 공간을 완전히 격리된 컨테이너(가상 실행 환경) 속에 가두고, 허용되는 에이전트 턴 수(AI가 생각하고 행동을 주고받는 횟수)와 제한 시간을 엄격하게 걸어두는 방식으로 방어벽을 높이고 있습니다 [출처: zai-org/GLM-5.3 · Hugging Face](https://huggingface.co/zai-org/GLM-5.3).

## 앞으로 어떻게 될까?

그렇다면 이 '돈 먹는 하마' 같은 문제를 해결하고 AI 코딩 에이전트를 진정한 생산성 혁신 도구로 진화시키려면 어떤 변화가 필요할까요? 전문가들은 크게 세 가지 방향을 제시합니다.

첫째, **실패의 진짜 원인을 투명하게 진단하는 설명 가능한 인공지능(XAI, Explainable AI) 기술**의 발전입니다 [출처: XAI for Coding Agent Failures: Transforming Raw Execution... - arxiv.org](https://arxiv.org/html/2603.05941v1). 에이전트가 왜 중간에 길을 잃고 멈춰---
layout: post
title: "AI 코딩 도우미, 실패할 때마다 '돈 먹는 하마' 된다? 27,280번의 실패 분석"
description: "AI 코딩 에이전트가 잦은 실패와 재시도로 인해 예산을 초과하고 개발자의 디버깅 시간을 늘리는 문제점을 심층 분석합니다. 비용 절감 및 효율성 증대를 위한 방안을 모색합니다."
summary: "AI 코딩 에이전트의 잦은 실패가 막대한 비용 낭비와 디버깅의 어려움을 야기하며, 전체 추론 비용의 64%를 차지한다는 분석 결과를 소개합니다."
tags: ["AI", "코딩 에이전트", "개발", "비용", "효율성", "LLM"]
image: 2026-11-18-In-27280-coding-agent-runs-64-of-inference-spend-went-to-runs-that-failed.jpg
image_alt: "AI 코딩 에이전트가 복잡한 코드 문제를 해결하려다 실패하는 모습, 그래프로 표시된 비용 증가"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 코딩 에이전트의 잠재력을 현실화하려면, 실패의 근본 원인을 파악하고 이를 해결하기 위한 기술적, 운영적 개선이 필수적입니다. 단순히 더 강력한 모델을 사용하는 것만으로는 부족하며, 효율적인 제어와 검증 시스템 구축이 시급합니다."
quiz:
  - question: "AI 코딩 에이전트 실행에서 가장 큰 비용을 차지하는 부분은 무엇인가요?"
    choices: ["성공적인 작업 완료", "모델 학습 및 튜닝", "실패한 실행 및 재시도"]
    answer: 2
    explanation: "27,280번의 코딩 에이전트 실행 분석 결과, 실패한 실행이 전체 추론 비용의 64%를 차지했습니다. 이는 실패한 작업에 대한 재시도가 비용을 크게 증가시키기 때문입니다."
  - question: "AI 코딩 에이전트가 실패했을 때 개발자가 겪는 어려움은 무엇인가요?"
    choices: ["코드 이해도 증가", "비용 절감 효과", "디버깅의 어려움 및 비용 증대"]
    answer: 2
    explanation: "AI 코딩 에이전트의 실패는 이해하기 어려운 실행 흔적을 남겨 디버깅을 복잡하게 만들고, 반복되는 재시도로 인해 비용이 기하급수적으로 증가하는 문제를 야기합니다."
  - question: "AI 코딩 에이전트의 잠재적 효율성에 대한 OpenAI의 보고 내용은 무엇인가요?"
    choices: ["인간 개발자보다 10배 효율적", "연구 업무에 3.1일 분량의 작업량 제공", "실패율이 낮아 비용이 거의 들지 않음"]
    answer: 1
    explanation: "OpenAI는 코딩 에이전트가 인간 연구자 하루 업무량의 3.1일 분량을 제공한다고 보고했습니다. 그러나 이러한 효율성은 실패로 인한 비용 및 제어 문제로 인해 제약을 받을 수 있습니다."
lang: ko
ref: 2026-11-18-In-27280-coding-agent-runs-64-of-inference-spend-went-to-runs-that-failed
---

# AI 코딩 도우미, 실패할 때마다 '돈 먹는 하마' 된다? 27,280번의 실패 분석

개발자의 생산성을 혁신할 것으로 기대되었던 AI 코딩 에이전트. 하지만 이 똑똑한 조력자가 잦은 실패를 거듭하면서 예상치 못한 '비용 폭탄'을 안겨주고 있다는 분석 결과가 나왔습니다. 마치 똑똑한 친구에게 어려운 수학 문제를 풀게 했는데, 답을 틀릴 때마다 계속해서 다시 풀기만 반복하며 시간과 에너지를 낭비하는 것과 같습니다. AI 코딩 에이전트의 실패가 왜 이렇게 비싼지, 그리고 이를 어떻게 해결해야 할지 함께 알아보겠습니다.

## 이게 왜 중요한가요?

AI 코딩 에이전트는 소프트웨어 개발 과정을 자동화하고 가속화할 잠재력을 가지고 있습니다. OpenAI는 코딩 에이전트가 인간 연구자 하루 업무량의 **3.1일 분량**을 제공한다고 보고하기도 했습니다 [출처: OpenAI Reports Coding Agents at 3.1 Workdays per... - GravityDevOps](https://gravitydevops.com/daily-openai-research-agent-operations/). 이는 개발자들이 반복적이고 시간이 많이 소요되는 작업에서 벗어나 더 창의적이고 복잡한 문제에 집중할 수 있게 해줄 것입니다.

하지만 현실은 녹록지 않습니다. 최근 27,280번의 코딩 에이전트 실행을 분석한 결과, **전체 추론 비용의 무려 64%가 실패한 실행에 지출**된 것으로 나타났습니다 [출처: In 27,280 coding agent runs, 64% of inference spend went to runs that failed](https://runta.com/blog/introducing-frontierharness-eval-v1-1/). 단순히 몇 번의 실패가 아닙니다. 수많은 코딩 에이전트가 잦은 타임아웃, API 오류, 또는 잘못된 코드 생성 등으로 인해 실패하고 있으며, 이 실패들이 모여 눈덩이처럼 불어나는 비용을 발생시키고 있습니다.

## 쉽게 이해하기: AI 코딩 에이전트의 '실패 딜레마'

쉽게 말해서, AI 코딩 에이전트가 실패했을 때 일반적인 프로그램처럼 곧바로 멈추지 않는다는 점이 문제입니다. 에이전트는 타임아웃, API 오류, 혹은 생성된 코드가 유효성 검사에 실패하면 **자동으로 재시도**합니다 [출처: AI Coding Agent Timeout and Retry Costs: How Failed Runs... - ai-cost-estimator.com](https://ai-cost-estimator.com/blog/ai-coding-agent-timeout-retry-costs-failed-runs-budget). 비유하면, 요리사가 레시피대로 요리를 하다가 중간에 실수를 해도 그냥 포기하는 대신 똑같은 실수를 반복하며 계속 요리를 시도하는 것과 같습니다. 이 반복적인 재시도는 프로젝트의 예산을 조용히, 하지만 확실하게 잠식해 나갑니다.

상상해보세요. 제한된 예산으로 앱을 개발하는 스타트업에서 AI 에이전트가 밤새 잘못된 코드를 수천 번 고치려다 클라우드 사용료로 수백만 원의 청구서를 받게 되는 상황을 말입니다. 이러한 실패 패턴은 여러 대규모 오픈소스 저장소에서 1,281번의 에이전트 실행 데이터를 분석한 결과, **5가지 반복 가능한 실패 패턴**이 존재함이 밝혀지기도 했습니다 [출처: Why coding agents fail in large codebases (and what to do... - sourcegraph.com](https://sourcegraph.com/blog/why-coding-agents-fail-large-codebases).

더 큰 문제는 이러한 실패가 **개발자의 디버깅 시간을 복잡하게 만든다**는 것입니다. 대규모 언어 모델(LLM, Large Language Model) 기반 코딩 에이전트가 실패하는 방식은 개발자가 이해하고 디버깅하기 어렵기 때문입니다. 에이전트가 생성하는 원시 실행 흔적(raw execution traces)은 경험 많은 개발자조차 해석하기 어려울 수 있습니다 [출처: XAI for Coding Agent Failures: Transforming Raw Execution... - arxiv.org](https://arxiv.org/html/2603.05941v1). 마치 수천 개의 전선이 얽힌 거대한 기계에서 고장 난 특정 전선 하나를 찾기 위해 복잡한 회로도를 해독해야 하는 상황과 같습니다.

## 현재 상황: 제어와 검증의 중요성

현재 많은 AI 코딩 에이전트 솔루션들이 등장하고 있습니다. 예를 들어, Zro by MoonMath.ai는 코딩 에이전트를 위한 비공개 AI 추론 서비스를 제공하며, 월 $20부터 시작하는 요금제로 추론 비용을 관리할 수 있습니다 [출처: Zro by MoonMath.ai | Private AI Inference for Coding Agents](https://zro.moonmath.ai/). 또한, Ollama와 같은 도구를 사용하면 로컬 환경에서 AI 에이전트를 실행하며 웹 스크래핑, 브라우징, RAG(Retrieval-Augmented Generation, 검색 증강 생성) 메모리 등 다양한 기능을 활용할 수 있습니다 [출처: Unlimited AI Agents running locally with Ollama... - YouTube](https://www.youtube.com/watch?v=4UFrVvy7VlA).

하지만 이러한 솔루션들 역시 에이전트의 '행동'을 얼마나 잘 제어하고 '결과'를 정확히 검증하는지가 핵심 과제로 떠오르고 있습니다. OpenAI 역시 코딩 에이전트 운영의 핵심 교훈으로 **'제어(control), 비용(cost), 검증(verification)'**을 강조하고 있습니다 [출처: OpenAI Reports Coding Agents at 3.1 Workdays per... - GravityDevOps](https://gravitydevops.com/daily-openai-research-agent-operations/).

AI 에이전트의 장기 실행 작업에서는 모델 선택의 복잡성과 그로 인한 파급 효과 때문에 문제를 해결하는 것이 매우 어렵습니다 [출처: Interactive benchmarks: evaluating model routing for AI agents](https://www.notdiamond.ai/blog/interactive-benchmarks-a-new-methodology-for-evaluating-model-routing?trk=public_post_comment-text). 일부 시스템은 각 에이전트 실행을 격리된 컨테이너에서 처리하고, 최대 에이전트 턴 수와 타임아웃을 제한하며, 도구 검색을 비활성화하는 등의 방식으로 제어를 강화하기도 합니다 [출처: zai-org/GLM-5.3 · Hugging Face](https://huggingface.co/zai-org/GLM-5.3).

## 앞으로 어떻게 될까?

AI 코딩 에이전트의 실패 비용 문제를 해결하기 위해서는 몇 가지 기술적 및 운영적 방향으로 나아갈 수 있습니다.

첫째, **실패의 근본 원인을 파악하고 분석하는 기술(XAI, Explainable AI, 설명 가능한 인공지능)**이 중요해질 것입니다. 개발자가 에이전트의 실패를 더 쉽게 이해하고 디버깅할 수 있도록 돕는 시스템이 필요합니다 [출처: XAI for Coding Agent Failures: Transforming Raw Execution... - arxiv.org](https://arxiv.org/html/2603.05941v1).

둘째, **비용 효율적인 추론 및 모델 라우팅(Model Routing) 기술**이 발전할 것입니다. 예를 들어, Together.ai는 코딩 에이전트를 위한 실제 추론 벤치마크를 공개하며 TensorRT-LLM보다 31% 더 높은 TPS(Transactions Per Second, 초당 처리량)와 2배 더 나은 TTFT(Time To First Token, 첫 토큰 생성 시간)를 제공하고, Claude Opus 4.6 대비 76% 낮은 비용으로 서비스를 제공한다고 밝히고 있습니다 [출처: Benchmarking inference at scale: coding agents - together.ai](https://www.together.ai/blog/coding-agent-benchmarks).

셋째, **에이전트의 실행을 관리하고 비용을 추적하는 도구**가 더욱 정교해질 것입니다. CodeBurn과 같은 서비스는 Claude Code 세션에서 프롬프트, 도우미 실행, 컨텍스트 재독, 실패한 단계별 비용을 추적하고 분석하는 기능을 제공합니다 [출처: AICodingCost & Token Usage Tracker for ClaudeCode... | CodeBurn](https://codeburn.app/).

궁극적으로, AI 코딩 에이전트가 진정한 '개발 생산성 혁신'을 가져오기 위해서는 기술 자체의 발전뿐만 아니라, 실패를 최소화하고 비용을 효율적으로 관리하며, 그 과정을 투명하게 이해하고 제어할 수 있는 **견고한 운영 및 검증 시스템**이 필수적일 것입니다.

## 참고자료
*   [Source 1] In 27,280 coding agent runs, 64% of inference spend went to runs that failed - https://runta.com/blog/introducing-frontierharness-eval-v1-1/
*   [Source 2] Zro by MoonMath.ai | Private AI Inference for Coding Agents - https://zro.moonmath.ai/
*   [Source 3] Unlimited AI Agents running locally with Ollama... - YouTube - https://www.youtube.com/watch?v=4UFrVvy7VlA
*   [Source 5] Interactive benchmarks: evaluating model routing for AI agents - https://www.notdiamond.ai/blog/interactive-benchmarks-a-new-methodology-for-evaluating-model-routing?trk=public_post_comment-text
*   [Source 6] OpenAI Reports Coding Agents at 3.1 Workdays per... - GravityDevOps - https://gravitydevops.com/daily-openai-research-agent-operations/
*   [Source 7] zai-org/GLM-5.3 · Hugging Face - https://huggingface.co/zai-org/GLM-5.3
*   [Source 11] XAI for Coding Agent Failures: Transforming Raw Execution... - arxiv.org - https://arxiv.org/html/2603.05941v1
*   [Source 13] AI Coding Agent Timeout and Retry Costs: How Failed Runs... - ai-cost-estimator.com - https://ai-cost-estimator.com/blog/ai-coding-agent-timeout-retry-costs-failed-runs-budget
*   [Source 14] Benchmarking inference at scale: coding agents - together.ai - https://www.together.ai/blog/coding-agent-benchmarks
*   [Source 15] Why coding agents fail in large codebases (and what to do... - sourcegraph.com - https://sourcegraph.com/blog/why-coding-agents-fail-large-codebases
*   [Source 16] AICodingCost & Token Usage Tracker for ClaudeCode... | CodeBurn - https://codeburn.app/