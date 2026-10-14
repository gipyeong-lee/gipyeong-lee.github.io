---
layout: post
title: "AI가 코드를 3만 번이나 고친다고요? 앤스로픽이 '깃(Git)'을 버린 이유"
description: "AI가 너무 많은 코드를 작성해 기존 버전 관리 시스템이 한계에 다다르자, 앤스로픽이 자체 개발한 시스템 '사이온(Scion)'으로 전환한 사연"
summary: "AI 모델 클로드(Claude)가 매일 3만 건이 넘는 코드 변경을 만들어내자, 앤스로픽은 기존의 깃(Git) 기반 인프라를 버리고 자체 버전 관리 시스템인 '사이온(Scion)'을 개발해 도입했습니다."
tags: [앤스로픽, AI개발, 버전관리, 사이온, 클로드]
image: 2026-10-14-Redesigning-Source-Control-at-Anthropic.jpg
image_alt: "복잡한 코드 네트워크와 AI 에이전트가 상호작용하는 모습을 시각화한 그래픽"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "인간 개발자의 속도를 넘어선 AI의 생산성이 기존 도구 체계를 흔들고 있습니다. 이제는 인프라 자체가 '에이전트'를 위해 설계되어야 하는 시대입니다."
quiz:
  - question: "앤스로픽이 기존의 깃(Git) 대신 자체 버전 관리 시스템인 '사이온(Scion)'을 도입한 주된 이유는 무엇인가요?"
    choices: ["비용 절감을 위해서", "AI 에이전트의 폭발적인 코드 생성으로 인한 기존 시스템의 병목 현상 때문", "더 안전한 보안 기능을 제공하기 위해서"]
    answer: 1
    explanation: "AI가 스스로 코드를 작성하고 반복하는 과정에서 코드 병합량이 하루 2,500건에서 3만 건으로 급증하여 기존 인프라로는 감당이 불가능해졌기 때문입니다."
  - question: "앤스로픽의 새로운 시스템인 '사이온(Scion)'은 어떤 환경을 위해 설계되었나요?"
    choices: ["인간 개발자들만 사용하는 오프라인 환경", "AI 에이전트가 24시간 내내 코드를 작성하고 반복(Iteration)하는 환경", "모바일 앱 개발 전용 환경"]
    answer: 1
    explanation: "사이온은 AI 에이전트가 끊임없이 코드를 생성하고 스스로 반복 학습하는 환경에 최적화되어 설계되었습니다."
  - question: "앤스로픽이 코드 변경 후 모든 테스트를 실행하는 대신 도입한 방식은 무엇인가요?"
    choices: ["테스트 완전 생략", "결정론적 테스트 영향 분석(Test Impact Analysis)", "임의로 테스트 선택하기"]
    answer: 1
    explanation: "수많은 코드 변경마다 모든 테스트를 실행하는 대신, 과거 데이터와 패키지 관련성을 바탕으로 필요한 테스트만 골라 실행하는 결정론적 테스트 영향 분석 서비스를 도입했습니다."
lang: ko
ref: 2026-10-14-Redesigning-Source-Control-at-Anthropic
audio: 2026-10-14-Redesigning-Source-Control-at-Anthropic.mp3
permalink: /2026/10/14/Redesigning-Source-Control-at-Anthropic/
---

상상해보세요. 여러분이 쓴 글을 누군가 1초마다 3만 번씩 수정하고, 다시 검토받으라고 요청한다면 어떨까요? 사람이 감당하기 힘든 속도겠죠. 그런데 지금 AI 기업 앤스로픽(Anthropic)의 사무실에서 실제로 벌어지고 있는 일입니다. AI 모델 '클로드(Claude)'가 스스로 연구를 반복하고 새로운 서비스를 구축하면서, 회사의 코딩 인프라가 비명을 지르기 시작했습니다.

### 이게 왜 중요한가요?

지금까지 소프트웨어 개발은 '사람'의 속도에 맞춰져 있었습니다. 하지만 AI가 코드를 직접 짜기 시작하면서, 이제 코드를 작성하는 것보다 **작성된 코드를 관리하고 배포하는 일**이 더 큰 병목 현상이 되었습니다. [앤스로픽은 코딩 인프라가 더 이상 AI의 생산성을 따라가지 못하는 상황에 직면했습니다.](https://www.theregister.com/devops/2026/10/13/anthropic-reinvents-source-control-as-claude-floods-the-world-with-code/5302943) 앤스로픽이 이번에 인프라를 완전히 갈아엎은 것은 AI 시대에 개발 도구가 어떻게 진화해야 하는지를 보여주는 중요한 이정표입니다.

### 쉽게 이해하기: '깃(Git)'이라는 퍼즐 상자의 한계

우리가 흔히 쓰는 '깃(Git)'은 개발자들이 코드를 저장하고 수정하는 공동 작업 공간입니다. 쉽게 비유하면, 여러 명이 하나의 거대한 퍼즐을 맞추는 '퍼즐 상자'와 같습니다. 사람이 몇 명일 때는 서로 순서를 지키며 조각을 끼워 맞출 수 있죠.

하지만 AI 에이전트들이 이 퍼즐 상자에 달려들어 1초마다 수천 개의 조각을 끼웠다 뺐다 한다면 어떻게 될까요? 상자는 터져버릴 겁니다. 기존의 깃은 인간 중심의 '오프라인' 개발 환경을 전제로 설계되었기 때문에, AI가 실시간으로 쏟아내는 수만 건의 변경 사항을 한꺼번에 처리하기엔 너무 무거웠습니다. [앤스로픽의 코드 병합량은 하루 2,500건에서 3만 건으로 무려 12배 가까이 폭증했습니다.](https://braindetox.kr/en/posts/anthropic_scion_version_control_replaces_git_2026.html) 

그래서 앤스로픽은 아예 새로운 방식의 시스템, **'사이온(Scion)'**을 직접 만들었습니다. 사이온은 AI 에이전트들이 24시간 내내 쉬지 않고 코드를 수정해도 끄떡없도록 설계된 'AI 전용 버전 관리 시스템'입니다. [앤스로픽은 5개월 동안 기존 단일 저장소(Monorepo)를 깃에서 사이온으로 완전히 이전했습니다.](https://braindetox.kr/en/posts/anthropic_scion_version_control_replaces_git_2026.html)

### 현재 상황: AI의 속도에 맞춘 인프라 개선

앤스로픽은 단순히 버전 관리 시스템만 바꾼 것이 아닙니다. 사이온 도입과 함께 몇 가지 핵심적인 변화를 주었습니다.

1.  **코드 리뷰 도구의 진화**: 사람이 수만 건의 코드를 직접 확인하는 것은 불가능합니다. 앤스로픽은 **'앤티크(Antique)'**라는 새로운 코드 리뷰 전용 시스템을 도입해, AI가 쏟아내는 변경 사항들을 사람이 효율적으로 검토할 수 있는 환경을 만들었습니다. [앤스로픽은 사이온과 함께 이 새로운 코드 리뷰 표면을 개발하고 배포했습니다.](https://braindetox.kr/en/posts/anthropic_scion_version_control_replaces_git_2026.html)
2.  **똑똑한 테스트 시스템**: 코드가 바뀔 때마다 모든 테스트를 돌리면 시간이 너무 많이 걸립니다. 그래서 앤스로픽은 과거 데이터와 코드의 연관성을 분석해, **꼭 필요한 테스트만 골라서 실행하는 '결정론적 테스트 영향 분석 서비스'**를 도입했습니다. [이 방식은 테스트 실행 효율을 높여 개발 속도를 다시 한번 끌어올렸습니다.](https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic)

### 어디에 서 있나요?

현재 앤스로픽의 사례는 소프트웨어 개발 환경이 '인간 중심'에서 'AI 에이전트 중심'으로 이동하고 있음을 보여주는 신호탄입니다. 과거에는 개발자가 컴퓨터의 성능을 고민했다면, 이제는 컴퓨터가 에이전트의 활동을 감당할 수 있는지를 고민해야 하는 시기가 온 것입니다. 이러한 변화는 단지 앤스로픽만의 일이 아닙니다. 앞으로 수많은 테크 기업들이 인간의 편의성을 넘어, 기계의 엄청난 생산성을 지탱할 새로운 인프라를 찾게 될 것입니다.

### 앞으로 어떻게 될까?

우리가 사용하는 서비스의 업데이트 주기는 점점 더 짧아질 것이고, 그 이면에는 이렇게 AI가 스스로 성장하기 위해 고군분투하는 새로운 형태의 '디지털 공장'들이 자리 잡게 될 것입니다. 사이온과 같은 인프라는 AI가 단순한 도구를 넘어 스스로 기술의 기반을 재설계하는 '자가 발전' 단계로 진입했음을 상징합니다. [사이온은 AI가 상시 작동하는 'Agent-always-on' 시나리오에 특화되어 설계되었습니다.](https://zeli.app/zh/story/50073633) 

우리는 지금 인간 개발자가 코드를 쓰던 시대를 지나, AI가 코드를 작성하고 인간이 그 결과물을 감독하는 흥미로운 전환점에 서 있습니다.

---

**MindTickleBytes의 AI 기자 시선**
AI가 스스로 코드를 고치고 연구하는 '에이전틱(Agentic)' 시대는 이미 시작되었습니다. 앤스로픽의 행보는 이제 AI가 기술을 소비하는 것을 넘어, 기술의 기반 시설까지 스스로 재설계하게 만드는 자가 발전의 단계로 진입했음을 의미합니다.

## 참고자료

1. [AnthropicClaude Can NowControlYour Computer - YouTube](https://www.youtube.com/watch?v=eB7E-mtpC18)
2. [Anthropic(Anthropic)](https://huggingface.co/Anthropic)
3. [How AI is transforming workatAnthropic\Anthropic](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)
4. [Agentic coding is straining CI. Here’s how we... | Claude byAnthropic](https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic)
5. [AnthropicAI safety researcher quits with 'world in peril' warning](https://www.bbc.com/news/articles/c62dlvdq3e3o)
6. [EggheadsatAnthropicSaid They Used Claude to "Solve" Humor](https://futurism.com/artificial-intelligence/anthropic-solve-humor)
7. [Anthropicrestores Fable 5, Mythos 5 after U.S. lifts exportcontrols](https://www.linkedin.com/pulse/anthropic-restores-fable-5-mythos-after-us-lifts-export-controls-3ffnc)
8. [Redesigning source control at Anthropic — CodeNews.com](https://codenews.com/news/redesigning-source-control-at-anthropic-1ojqmz)
9. [Anthropic Scion: Why Its Monorepo Left Git at 30,000 Merges](https://braindetox.kr/en/posts/anthropic_scion_version_control_replaces_git_2026.html)
10. [Anthropic Scion Redesigns Source Control for AI Agents](https://scalevise.com/resources/anthropic-scion-agent-scale-source-control/)
11. [Anthropic reinvents source control as Claude floods the world ...](https://www.theregister.com/devops/2026/10/13/anthropic-reinvents-source-control-as-claude-floods-the-world-with-code/5302943)
12. [Anthropic Overhauls Source Control to Fix Bottlenecks](https://book.st-hakky.com/en/news/redesigning-source-control-at-anthropic)
13. [Redesigning source control at Anthropic - hoton.ai](https://hoton.ai/en/news/redesigning-source-control-at-anthropic-1vlb4uz)
14. [Anthropic 因Claude重写版本控制系统 — Redesigning Source Control a...](https://zeli.app/zh/story/50073633)
15. [Newsroom \Anthropic](https://www.anthropic.com/news)
16. [AnthropicIs Bleeding Out](https://www.wheresyoured.at/anthropic-is-bleeding-out/)
17. [Hidden AI instructions reveal howAnthropiccontrols... - Ars Technica](https://arstechnica.com/ai/2025/05/hidden-ai-instructions-reveal-how-anthropic-controls-claude-4/)
18. [OpenAI andAnthropicAI crisis explained: OpenAI andAnthropicfear...](https://economictimes.indiatimes.com/world/business/openai-and-anthropic-fear-a-major-ai-crisis-in-the-next-6-to-12-months-heres-what-theyre-preparing-for/articleshow/134860984.cms)
20. [LatestAnthropic(Claude AI) Statistics (2025) | StatsUp](https://analyzify.com/statsup/anthropic)