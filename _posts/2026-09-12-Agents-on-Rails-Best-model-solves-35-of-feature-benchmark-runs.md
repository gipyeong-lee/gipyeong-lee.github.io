---
layout: post
title: "AI가 내 대신 코딩을? 'Agents on Rails' 벤치마크로 본 AI의 실제 실력"
description: "AI 코딩 에이전트가 실제 Ruby on Rails 프로젝트에서 어느 정도의 성능을 내는지, 최신 벤치마크 결과를 통해 쉽고 명쾌하게 설명해 드립니다."
summary: "AI가 실제 Ruby on Rails 프로젝트의 복잡한 기능을 얼마나 잘 구현할 수 있는지 측정한 'Agents on Rails' 벤치마크 결과, 최상위 모델이 35%의 성공률을 기록하며 실전 투입 가능성을 증명했습니다."
tags: [AI, 코딩, Ruby on Rails, Agents on Rails, 프로그래밍]
image: 2026-09-12-Agents-on-Rails-Best-model-solves-35-of-feature-benchmark-runs.jpg
image_alt: "복잡한 코드 파일들 위로 AI 에이전트의 데이터 흐름이 시각화되어 있는 모습"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI의 코딩 실력이 비약적으로 발전하고 있지만, 아직 실무 수준의 복잡한 기능을 완벽히 수행하기엔 갈 길이 멀어 보입니다. 하지만 35%라는 수치는 단순한 시작일 뿐입니다."
quiz:
  - question: "Agents on Rails 벤치마크에서 사용하는 실제 프로젝트 이름은 무엇인가요?"
    choices: ["Writebook", "RailsApp", "CodeAgent"]
    answer: 0
    explanation: "Agents on Rails는 Writebook이라는 실제 프로젝트를 사용하여 AI 에이전트의 성능을 테스트합니다."
  - question: "최근 발표된 'Stage 2' 벤치마크에서 가장 높은 성공률을 기록한 모델의 점수는 몇 퍼센트인가요?"
    choices: ["92%", "35%", "50%"]
    answer: 1
    explanation: "GPT-6 Astra 모델이 Stage 2 기능 구현 과제에서 35%의 성공률을 기록했습니다."
  - question: "이 벤치마크가 중요한 이유로 가장 적절한 것은?"
    choices: ["AI의 그래픽 처리 능력을 측정하기 위해서", "실제 업무 환경과 유사한 환경에서 AI 코딩 성능을 측정하기 위해서", "AI의 작문 실력을 테스트하기 위해서"]
    answer: 1
    explanation: "이 프로젝트는 실제 Ruby on Rails codebase를 기반으로 개발자가 겪는 실무적인 과제를 얼마나 잘 해결하는지 측정하는 것이 목표입니다."
lang: ko
ref: 2026-09-12-Agents-on-Rails-Best-model-solves-35-of-feature-benchmark-runs
audio: 2026-09-12-Agents-on-Rails-Best-model-solves-35-of-feature-benchmark-runs.mp3
permalink: /2026/09/12/Agents-on-Rails-Best-model-solves-35-of-feature-benchmark-runs/
---

상상해보세요. 아침에 눈을 떠서 AI 비서에게 "오늘 우리 웹사이트에 회원가입 기능을 추가하고, 관련된 보안 이슈도 점검해줘"라고 말합니다. 여러분이 커피 한 잔을 마시는 동안 AI는 복잡한 코드를 작성하고, 스스로 테스트까지 마친 뒤 "모든 작업이 완료되었습니다"라고 보고합니다.

불과 몇 년 전까지만 해도 공상과학 영화에서나 보던 일이지만, 이제 우리는 이 미래에 한 발짝 더 다가가 있습니다. 과연 현재의 AI들은 개발자를 대신해 실제 업무를 얼마나 잘 수행하고 있을까요? 최근 루비 온 레일즈(Ruby on Rails, 웹 애플리케이션 개발을 위한 프로그래밍 프레임워크) 재단과 이블 마션스(Evil Martians)가 공개한 **'Agents on Rails'** 벤치마크 결과를 통해 그 실체를 살펴보겠습니다. [[출처: Agents on Rails: the first benchmark report](https://rubyonrails.org/2026/8/13/agents-on-rails-the-first-benchmark-report), [출처: Rails Foundation launches an AI coding agent benchmark for Ruby on Rails | daily.dev](https://daily.dev/posts/rails-foundation-launches-an-ai-coding-agent-benchmark-for-ruby-on-rails-shazaa4gk)]

## 이게 왜 중요한가요?

지금까지 많은 AI 모델이 코딩을 잘한다고 홍보해 왔지만, 실제 기업 현장의 프로젝트는 훨씬 복잡하고 까다롭습니다. 기존의 벤치마크들은 대부분 아주 짧고 단순한 코드 조각을 테스트하는 데 그쳤죠.

'Agents on Rails'가 중요한 이유는 바로 **'실전형 테스트'**이기 때문입니다. 실제 개발자들이 사용하는 'Writebook'이라는 프로젝트 코드를 그대로 가져와, 버그 수정, 보안 점검, 새로운 기능 추가 등 실무에서 마주하는 과제를 수행하게 합니다. [[출처: Agents on Rails: the first benchmark report](https://rubyonrails.org/2026/8/13/agents-on-rails-the-first-benchmark-report), [출처: Agents on Rails benchmark: model picks by cost and score](https://tokenstead.ai/guides/agents-on-rails-first-benchmark-report)] 즉, 이 결과는 우리 업무 환경에 AI를 당장 도입했을 때 얼마나 믿고 맡길 수 있는지 알려주는 '실무 성적표'와 같습니다.

## 쉽게 이해하기

이 벤치마크를 이렇게 비유해보면 이해가 쉽습니다. 

쉽게 말해서, 기존의 AI 성능 측정 방식이 '초등학생 수준의 영어 단어 시험'을 보는 것과 같았다면, 'Agents on Rails'는 실제 영어권 국가의 회사에 입사해서 신입 사원처럼 보고서를 쓰고 협업해야 하는 '실무 능력 평가'와 같습니다.

AI 에이전트는 마치 이제 막 회사에 들어온 신입 사원과 같습니다. 1단계 테스트에서는 아주 짧고 독립적인 업무(버그 찾기, 보안 문제 해결 등)를 시켰고, 2단계 테스트에서는 실제 개발자가 하는 것처럼 **'기능 구현 전체 과정'**을 수행하게 했습니다. [[출처: Agents on Rails: Stage 2. Can a model ship a feature?](https://rubyonrails.org/2026/9/9/agents-on-rails-stage-2), [출처: Agents on Rails: We ran 8 models against 21 atomic tasks to ...](https://www.linkedin.com/posts/ruby-on-rails-org_agents-on-rails-we-ran-8-models-against-activity-7493709649016188929-F2nq)]

최근 발표된 2단계 결과에서 가장 뛰어난 성능을 보인 'GPT-6 Astra' 모델이 기록한 성공률은 **35%**입니다. "어? 생각보다 낮네?"라고 느끼실 수도 있습니다. 하지만 복잡한 실제 업무를 AI 혼자서 35%나 성공적으로 끝낼 수 있다는 것은, 숙련된 개발자가 옆에서 검토하고 수정해준다면 업무 효율을 극적으로 높일 수 있는 수준이라는 의미이기도 합니다.

## 현재 상황

현재 'Agents on Rails'는 8개의 주요 AI 모델들을 대상으로 철저하게 검증하고 있습니다. [[출처: Rails Releases First AI Coding Agents Benchmark](https://x.com/i/trending/2087976916330459284)]

- **최상위권 모델의 활약**: 1단계 테스트에서 'Claude Opus 5'는 92%라는 놀라운 성공률을 기록했습니다. [[출처: Agents on Rails: the first benchmark report | Vuink.com](https://vuink.com/post/eholbaenvyf-d-dbet/2026/8/13/agents-on-rails-the-first-benchmark-report)]
- **다양한 선택지**: 'Kimi K3'는 최상위 모델의 절반 비용으로 90%의 성능을 내며 효율성을 입증했고, 'GPT-5.6 Luna'는 가장 저렴한 비용으로 눈길을 끌었습니다. [[출처: Rails Releases First AI Coding Agents Benchmark](https://x.com/i/trending/2087976916330459284)]
- **한계점**: 하지만 기능 전체를 구현해야 하는 2단계 테스트에서 알 수 있듯, 아직 AI는 실무 프로젝트의 전체 맥락을 완전히 이해하고 에러 없이 코드를 완성하는 데는 보완이 필요합니다.

## 앞으로 어떻게 될까?

앞으로 AI 코딩 에이전트는 더욱 똑똑해질 것입니다. Rails 재단은 모델들의 성공률뿐만 아니라, 최신 개발 패턴을 얼마나 잘 반영하는지, 토큰 비용(AI가 데이터를 처리할 때 발생하는 단위 비용)은 적절한지 등을 종합적으로 평가하며 계속해서 진화할 예정입니다. [[출처: Rails Foundation launches an AI coding agent benchmark for Ruby on Rails | daily.dev](https://daily.dev/posts/rails-foundation-launches-an-ai-coding-agent-benchmark-for-ruby-on-rails-shazaa4gk)]

독자 여러분이 주목해야 할 점은 단순한 점수보다 **'추세'**입니다. 단순히 문법을 아는 AI에서, 이제는 실제 비즈니스 가치를 만들어내는 기능을 직접 구현하는 단계로 넘어가고 있습니다. 머지않아 35%의 성공률이 50%, 70%로 올라가는 순간, 우리의 일하는 방식은 완전히 달라질 것입니다.

## MindTickleBytes의 AI 기자 시선
이번 벤치마크는 AI가 코딩의 '조수'를 넘어 '동료'로 성장하고 있음을 증명합니다. 35%라는 숫자는 비록 완벽하지는 않지만, AI가 실제 개발자의 워크플로우를 이해하고 실행하기 시작했다는 점에서 그 어떤 결과보다 희망적입니다.

## 참고자료

1. [Agents on Rails: the first benchmark report](https://rubyonrails.org/2026/8/13/agents-on-rails-the-first-benchmark-report)
2. [Agents on Rails: The LLM Benchmark Project](https://rubyonrails.org/2026/8/12/llm-benchmarking-project)
3. [Agents on Rails: Stage 2. Can a model ship a feature?](https://rubyonrails.org/2026/9/9/agents-on-rails-stage-2)
4. [Agents on Rails: Grok 4.6, GLM 5.3, Gemini 3.7 Flash, and Opus 4.8](https://rubyonrails.org/2026/8/17/agents-on-rails-grok-4-6-glm-5-3-gemini-3-7-flash-and-opus-4-8)
5. [Agents on Rails: the first benchmark report | Vuink.com](https://vuink.com/post/eholbaenvyf-d-dbet/2026/8/13/agents-on-rails-the-first-benchmark-report)
6. [Rails Foundation launches an AI coding agent benchmark for Ruby on Rails | daily.dev](https://daily.dev/posts/rails-foundation-launches-an-ai-coding-agent-benchmark-for-ruby-on-rails-shazaa4gk)
7. [Agents on Rails benchmark: model picks by cost and score](https://tokenstead.ai/guides/agents-on-rails-first-benchmark-report)
8. [Agents on Rails: We ran 8 models against 21 atomic tasks to ...](https://www.linkedin.com/posts/ruby-on-rails-org_agents-on-rails-we-ran-8-models-against-activity-7493709649016188929-F2nq)
9. [What the First Rails Agent Benchmark Tells You, and What It ...](https://www.convective.com/currents/what-the-first-rails-agent-benchmark-tells-you)
10. [Rails team's first "Agents on Rails" benchmark report: how well do models actually know Rails APIs?](https://www.rubyforum.org/t/rails-teams-first-agent-benchmark-report-how-well-do-models-actually-know-rails-apis/631)
11. [Rails Releases First AI Coding Agents Benchmark](https://x.com/i/trending/2087976916330459284)