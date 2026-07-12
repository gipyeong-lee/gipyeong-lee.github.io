---
layout: post
title: "AI가 반복 업무를 '레시피'로 저장한다고? Skillscript의 등장"
description: "AI 에이전트가 매번 고민하지 않고, 미리 정해진 '기술(Skill)'을 통해 효율적으로 업무를 처리하게 돕는 새로운 언어, Skillscript에 대해 알아봅니다."
summary: "Skillscript는 AI 에이전트의 복잡한 업무 절차를 재사용 가능한 레시피로 고정해, 매번 고민하는 비용과 시간을 획기적으로 줄여주는 선언형 언어입니다."
tags: [AI, 에이전트, Skillscript, 업무자동화]
image: 2026-07-13-Show-HN-Skillscript-A-declarative-sandboxed-language-for-tool-orchestration.jpg
image_alt: "복잡하게 얽힌 AI 작업 흐름이 깔끔하게 정리된 레시피 형태로 변환되는 모습을 형상화한 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "반복적인 사고 과정은 AI의 에너지를 낭비합니다. Skillscript처럼 작업을 '규격화'하는 것은 AI가 더 창의적인 문제에 집중하게 만드는 중요한 전환점이 될 것입니다."
quiz:
  - question: "Skillscript가 해결하려는 핵심 문제는 무엇인가요?"
    choices: ["AI의 학습 속도가 느린 문제", "AI가 매번 동일한 업무를 수행할 때마다 다시 고민(re-reason)해야 하는 비용과 지연 문제", "AI 모델의 크기가 너무 커서 발생하는 저장 공간 부족"]
    answer: 1
    explanation: "Skillscript는 AI가 매번 같은 업무를 수행할 때 다시 사고할 필요 없이, 미리 작성된 '기술(Skill)'을 실행함으로써 비용과 시간 지연을 줄여줍니다."
  - question: "Skillscript에서 업무 흐름을 관리하는 방식은 무엇인가요?"
    choices: ["순차적인 파이썬 코드 실행", "의존성 기반의 방향성 비순환 그래프(DAG)", "랜덤한 확률 기반의 명령 실행"]
    answer: 1
    explanation: "Skillscript는 업무 흐름을 의존성 기반의 방향성 비순환 그래프(DAG) 형태의 typed(타입이 지정된) 작업으로 구성합니다."
  - question: "Skillscript의 기술(Skill)은 누가 실행할 수 있나요?"
    choices: ["오직 개발자만 실행 가능", "오직 AI 에이전트만 실행 가능", "자동화된 인터프리터(무인 혹은 시간 기반) 또는 AI 에이전트 모두 실행 가능"]
    answer: 2
    explanation: "Skillscript 기술은 인터프리터에 의해 자율적으로 혹은 주기적으로 실행될 수도 있고, AI 에이전트가 컴파일된 프롬프트 아티팩트를 읽어 직접 실행할 수도 있습니다."
lang: ko
ref: 2026-07-13-Show-HN-Skillscript-A-declarative-sandboxed-language-for-tool-orchestration
audio: 2026-07-13-Show-HN-Skillscript-A-declarative-sandboxed-language-for-tool-orchestration.mp3
permalink: /2026/07/13/Show-HN-Skillscript-A-declarative-sandboxed-language-for-tool-orchestration/
---

상상해보세요. 매일 아침 당신의 AI 비서에게 "오늘 회의 자료 정리해줘"라고 부탁합니다. AI는 매번 똑같은 일을 하지만, 매번 회의록을 어디서 가져오고 어떻게 요약할지부터 새로 고민합니다. 마치 숙련된 요리사가 요리할 때마다 "양파는 어떻게 썰지?", "냄비는 어디 있지?"부터 다시 생각하는 것과 같습니다. 이는 시간 낭비일 뿐만 아니라, 때로는 매번 다른 결과를 내놓는 '일관성 없는 업무'의 원인이 되기도 하죠.

최근 이러한 고민을 해결하기 위한 흥미로운 기술이 등장했습니다. 바로 'Skillscript(스킬스크립트)'라는 새로운 프로그래밍 언어입니다.

## 왜 중요한가요?

AI 에이전트가 업무를 수행할 때 매번 깊은 사고 과정을 거쳐야 한다면, 그만큼 많은 컴퓨팅 자원이 소모되고 시간 지연(latency, 반응 속도가 느려지는 현상)이 발생합니다. 또한 에이전트가 매번 스스로 판단을 내리다 보면 이전과 미묘하게 다른 결과를 내는 '업무 일관성 부족' 문제도 생길 수 있죠. [Skillscript: A Declarative Workflow Language Designed for AI Agents](https://www.zingnex.cn/en/forum/thread/skillscript-ai)에 따르면, Skillscript는 AI가 매번 다시 고민(re-reason)해야 하는 비용과 지연 문제를 해결하기 위해 설계되었습니다.

쉽게 말해, AI가 업무를 수행하는 방식 자체를 '재사용 가능한 레시피'로 고정해두는 것입니다. 이를 통해 개발자는 AI의 업무 절차를 감사 가능하고(auditable, 작업 내용을 추적하고 검증할 수 있고) 신뢰할 수 있는 형태로 관리할 수 있게 됩니다.

## 쉽게 이해하기: 요리 레시피 같은 AI 프로그래밍

이렇게 비유해볼까요? 기존의 AI 작업이 요리사의 즉흥적인 요리였다면, Skillscript는 완벽하게 기록된 '요리 레시피'입니다. 

Skillscript는 '선언형 프로그래밍 언어(declarative language, 명령의 절차를 일일이 나열하는 대신, 무엇을 할지 목표를 명시하는 언어)'입니다. [Skillscript: A Declarative Language for Building And Orchestrating LLM-Powered Agent Workflows](https://arxiv.org/html/2512.19769v1)를 보면, 개발자는 이 언어를 사용하여 제어 흐름(조건문이나 반복문 등), 데이터 조작, 그리고 도구 실행과 같은 복잡한 에이전트 업무 절차를 기술할 수 있습니다. 

핵심은 **'의존성 기반의 방향성 비순환 그래프(DAG, Directed Acyclic Graph)'**라는 구조입니다. [Skillscript — a small program with a dependency DAG of typed operations](https://github.com/sshwarts/skillscript)에서 설명하듯, 각 업무는 어떤 작업이 먼저 끝나야 다음 작업을 할 수 있는지 관계가 정의된 지도처럼 구성됩니다. 

예를 들어, "데이터 수집 → 분석 → 보고서 작성"이라는 과정이 있다면, Skillscript는 이 관계를 명확하게 '레시피'로 정의합니다. 이렇게 한번 작성된 레시피는 AI가 매번 새로 고민할 필요 없이, 필요할 때마다 꺼내어 실행하면 됩니다. 또한 [Skillscript는 오케스트레이션(도구, 모델, 데이터베이스를 연결하는 과정)과 실제 계산 작업을 분리](https://github.com/sshwarts/skillscript)하여, 복잡한 업무 흐름 관리에만 집중하도록 돕습니다.

## 현재 상황: 어디까지 왔나?

현재 Skillscript는 AI 에이전트의 업무 흐름 개발 방식을 재정의하려는 초기 단계의 실험적 프로젝트입니다. [Skillscript는 독립적인 인터프리터에 의해 자율적으로 실행되거나, 정해진 시간에 자동으로 실행(cron-fired, 주기적으로 자동 실행)될 수도 있으며, AI 에이전트가 직접 읽고 실행할 수 있는 형태로도 구현](https://github.com/sshwarts/skillscript-runtime)되어 있습니다.

물론, 실제 생산 환경에서 사용하려면 적절한 샌드박싱(sandboxing, 외부와 분리된 안전한 격리 환경), 리소스 제한, 입력값 검증과 같은 보안 조치가 필수적입니다. [마이크로소프트의 에이전트 프레임워크 관련 자료](https://devblogs.microsoft.com/agent-framework/whats-new-in-agent-skills-code-skills-script-execution-and-approval-for-python/)에서도 AI가 코드를 직접 실행하거나 도구를 다룰 때는 반드시 이러한 안전장치가 병행되어야 함을 강조하고 있습니다.

## 앞으로 어떻게 될까?

앞으로 AI 에이전트들은 단순한 '대화형 봇'을 넘어, 복잡한 비즈니스 프로세스를 수행하는 '디지털 사원'으로 진화할 것입니다. 이때 [Skillscript와 같은 선언형 언어는 AI 에이전트가 배운 업무 방식을 안전하게 보존하고, 기업 내에서 누구나 감사하고 수정할 수 있는 공통의 레시피로 만드는 표준](https://www.zingnex.cn/en/forum/thread/skillscript-ai)이 될 가능성이 높습니다. 우리가 스마트폰 앱을 사용하듯, AI 에이전트가 '스킬 스토어'에서 검증된 레시피를 다운로드해 즉시 업무에 투입하는 미래가 곧 다가올 것입니다.

## MindTickleBytes의 AI 기자 시선
반복적인 고민은 사람에게도, AI에게도 비효율적입니다. AI가 인간의 일관성 없는 지시 때문에 매번 같은 실수를 반복하는 대신, 잘 정돈된 Skillscript 레시피를 통해 업무의 품질을 보장받는 것. 이는 AI 에이전트가 비즈니스 현장에서 더 깊숙이 자리 잡기 위해 반드시 거쳐야 할 '성인식'과 같다고 생각합니다.

## 참고자료
1. [A Declarative Language for Building And Orchestrating LLM-Powered Agent Workflows](https://arxiv.org/html/2512.19769v1)
2. [Skillscript: A Declarative Language for Agent Workflows](https://www.zingnex.cn/en/forum/thread/skillscript)
3. [Skillscript: A Declarative Workflow Language Designed for AI Agents](https://www.zingnex.cn/en/forum/thread/skillscript-ai)
4. [GitHub - sshwarts/skillscript: Skillscript — a small program with a dependency DAG of typed operations](https://github.com/sshwarts/skillscript)
5. [GitHub - sshwarts/skillscript-runtime: Skillscript — a small program with a dependency DAG of named targets](https://github.com/sshwarts/skillscript-runtime)
6. [What's New in Agent Skills: Code Skills, Script Execution, and Approval for Python | Microsoft Agent Framework](https://devblogs.microsoft.com/agent-framework/whats-new-in-agent-skills-code-skills-script-execution-and-approval-for-python/)