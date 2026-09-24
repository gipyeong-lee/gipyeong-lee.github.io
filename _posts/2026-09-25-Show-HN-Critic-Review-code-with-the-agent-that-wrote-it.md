---
layout: post
title: "AI가 쓴 코드, '작성한 AI'에게 직접 물어보며 리뷰한다면? 'Critic'의 등장"
description: "AI가 생성한 코드의 리뷰 과정을 혁신하는 도구 'Critic'에 대해 알아봅니다. 개발자가 AI 에이전트와 직접 소통하며 코드 변경 사항을 더 투명하게 검토할 수 있는 방법과 그 중요성을 쉽고 명확하게 설명합니다."
summary: "Critic은 AI 에이전트가 생성한 코드의 리뷰를 해당 AI 에이전트와 직접 대화하며 진행할 수 있게 함으로써, 개발자가 코드 변경 사항을 더 깊이 이해하고 버그를 조기에 발견할 수 있도록 돕는 새로운 도구입니다."
tags: [AI, 코드리뷰, 개발자도구, Critic, 에이전트]
image: 2026-09-25-Show-HN-Critic-Review-code-with-the-agent-that-wrote-it.jpg
image_alt: "코드를 검토하는 개발자와 그 옆에서 코드 생성 과정을 설명하는 AI 에이전트의 모습. 투명한 코드 리뷰 과정을 상징합니다."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 코드 생성 시대의 필수적인 동반자, Critic은 개발과 AI의 협업 방식에 새로운 기준을 제시하며, 더욱 신뢰할 수 있는 소프트웨어 개발을 가능하게 합니다."
quiz:
  - question: "Critic이 해결하고자 하는 주요 문제점은 무엇인가요?"
    choices: ["AI 에이전트의 코드 작성 속도가 너무 느림", "AI가 생성한 코드의 변경 사항을 개발자가 충분히 이해하기 어려움", "개발자들이 코드 리뷰를 너무 자주 함", "AI 에이전트가 너무 많은 질문을 함"]
    answer: 1
    explanation: "Critic은 AI가 생성한 코드의 변경 사항을 개발자가 충분히 이해하고 검토하기 어렵다는 문제를 해결하고자 합니다. 이를 위해 작성 에이전트와 직접 소통할 수 있게 합니다."
  - question: "Critic을 통해 AI 에이전트가 코드 변경 사항을 어떻게 '설명'할 수 있나요?"
    choices: ["음성으로 직접 설명", "코드 블록에 주석을 달고 스크린샷 등의 증거를 첨부", "자동으로 문서 파일 생성", "다른 AI 에이전트에게 설명을 요청"]
    answer: 1
    explanation: "Critic을 사용하는 AI 에이전트는 코드의 핵심 블록에 주석을 달고, 스크린샷이나 로컬 실행 지침 같은 관련 증거를 포함하여 자신의 코드 변경 사항을 설명할 수 있습니다 [Source 8]."
  - question: "Critic이 제공하는 '대화형 코드 리뷰'의 가장 큰 장점은 무엇인가요?"
    choices: ["코드 작성 시간을 단축", "개발자가 AI 에이전트의 의도를 더 깊이 이해하고 피드백 가능", "코드의 복잡도를 증가", "AI 에이전트의 학습 능력을 향상"]
    answer: 1
    explanation: "개발자는 코드 변경 사항을 보면서 해당 AI 에이전트와 직접 대화하여, AI가 왜 그렇게 코드를 작성했는지, 어떤 의도를 가졌는지 깊이 이해하고 필요한 피드백을 즉시 전달할 수 있습니다 [Source 8]."
lang: ko
ref: 2026-09-25-Show-HN-Critic-Review-code-with-the-agent-that-wrote-it
permalink: /2026/09/25/Show-HN-Critic-Review-code-with-the-agent-that-wrote-it/
---

## AI가 쓴 코드, '작성한 AI'에게 직접 물어보며 리뷰한다면? 'Critic'의 등장

상상해보세요. 여러분이 맡은 프로젝트에 새로운 기능을 추가해야 하는데, 이번에는 코딩 전문 AI 에이전트(Agent, 자율적으로 작업을 수행하는 AI)가 그 기능을 대신 만들어주었습니다. 코드는 완벽해 보이지만, 여러분은 이 코드가 왜 이런 식으로 작성되었는지, 숨겨진 의도는 없는지 궁금해집니다. 마치 학생이 쓴 에세이를 검토하는 선생님처럼, 코드의 모든 줄을 이해하고 싶지만 AI의 생각 과정을 정확히 파악하기란 쉽지 않죠. 기존의 방식으로는 단순히 '결과물'만 보고 판단해야 했습니다.

하지만 이제 이런 고민을 덜어줄 새로운 도구가 등장했습니다. 바로 'Critic'입니다. Critic은 AI가 생성한 코드를 리뷰할 때, 해당 코드를 작성한 AI 에이전트에게 직접 질문하고 설명을 들을 수 있도록 돕는 혁신적인 도구입니다. 마치 코드를 함께 작성한 동료 개발자와 이야기하듯이, AI와 대화하며 코드 변경 사항을 검토할 수 있게 된 것입니다 [Source 8].

## 이게 왜 중요한가요?

AI 기술이 발전하면서, 코딩 에이전트는 우리 개발 과정의 중요한 부분이 되고 있습니다. 하지만 AI가 코드를 만들면 한 가지 큰 문제가 발생합니다. 바로 '투명성'과 '이해'의 부족입니다. AI가 생성한 코드는 종종 복잡하거나 예측 불가능한 방식으로 작동할 수 있으며, 그 의도를 파악하기 어렵습니다 [Source 16, Source 19].

이러한 이해 부족은 심각한 문제를 초래할 수 있습니다. 예를 들어, CodeRabbit의 연구에 따르면 AI가 생성한 코드는 기존 코드보다 논리 및 정확성 문제, 보안 취약점, 가독성 문제 등이 1.5배에서 2배 이상 더 많이 발견되었다고 합니다 [Source 17, Source 19]. 쉽게 말해서, AI가 쓴 코드는 '겉으로는 멀쩡해 보이지만 속은 알 수 없는' 경우가 많다는 뜻입니다. 개발자가 AI 코드를 완전히 이해하지 못한 채 병합하면, 의도치 않은 버그나 보안 구멍이 실제 서비스에 배포될 위험이 커지는 것이죠 [Source 16].

Critic은 이러한 문제를 해결하기 위해, 개발자가 AI 에이전트와 직접 소통하며 코드 변경의 '왜(Why)'를 파악하도록 돕습니다 [Source 8]. 마치 건축 설계도를 보면서 설계자와 직접 대화하는 것처럼, 코드의 각 부분을 왜 그렇게 만들었는지 AI에게 물어보고 그 설명을 들을 수 있게 되는 것입니다. 이는 개발자가 AI 코드에 대한 신뢰를 높이고, 잠재적인 문제를 PR(Pull Request, 코드 병합 요청)이 생성되기 전에 미리 발견하여 수정할 수 있도록 돕습니다 [Source 1]. 

## 쉽게 이해하기: 요리사 AI의 설명

Critic의 핵심 아이디어는 간단합니다. AI가 코드를 작성하는 과정을 사람이 설명을 덧붙이듯 '주석(Annotation, 코드에 다는 설명)'과 '증거(Evidence)'와 함께 보여주는 것입니다.

비유하자면, Critic은 여러분 옆에서 요리 과정을 설명해주는 '요리사 AI'와 같습니다. 보통 요리책은 최종 레시피만 알려주지만, 이 요리사 AI는 이렇게 말합니다. "이 재료를 먼저 넣은 이유는 맛의 균형을 위해서였고, 여기 튀김옷을 두껍게 한 것은 바삭함을 살리기 위함입니다. 그 증거로 제가 실험했던 사진을 보여드릴게요."

Critic을 사용하는 AI 에이전트는 자신이 작성한 코드의 핵심 블록에 직접 주석을 달 수 있습니다. "이 함수는 사용자 인증을 위해 이런 로직을 사용합니다", "이 변수는 데이터를 효율적으로 처리하기 위해 배열 대신 해시맵(HashMap, 데이터를 빠르게 찾기 위한 자료구조)을 사용했습니다" 와 같은 설명이죠 [Source 8].

여기서 더 나아가, AI는 자신의 결정을 뒷받침하는 '증거'도 제시합니다. 예를 들어, 코드를 작성하기 전에 진행했던 시뮬레이션 결과 스크린샷을 첨부하거나, 해당 코드의 로컬 실행 지침을 포함할 수 있습니다 [Source 8]. 학생이 수학 문제를 풀고 나서 정답뿐만 아니라 풀이 과정과 사용한 공식, 그리고 연습 흔적까지 보여주는 것과 같습니다. 이렇게 하면 코드 리뷰는 단순한 확인을 넘어, 훨씬 더 깊이 있고 생산적인 소통의 장이 됩니다 [Source 3].

## 현재 상황

현재 Critic은 AI 에이전트가 생성한 코드를 개발자가 브라우저 환경에서 인라인 주석(코드 사이에 직접 넣는 주석)과 라인별 차이(line-level diffs, 수정된 코드의 상세 비교)를 통해 검토할 수 있도록 지원합니다 [Source 4, Source 18]. 개발자는 특정 코드 라인에 대해 질문하거나 피드백을 남길 수 있고, 그러면 AI 에이전트가 그 피드백에 따라 코드를 수정하고 다시 응답하는 방식으로 대화가 이어집니다 [Source 3, Source 18]. 마치 채팅하듯이 AI 에이전트와 실시간으로 소통하며 코드를 개선해나갈 수 있는 것이죠.

이러한 대화 시스템은 과거 AI 에이전트의 질문 시스템이 '최선의 노력 큐(best-effort queue, 요청을 처리하려 노력하지만 응답을 보장하지 않는 방식)'로 운영되었던 것과 비교하면 큰 발전입니다 [Source 2]. 과거에는 개발자가 질문을 해도 AI가 응답하지 않거나 지연되는 경우가 많았지만, Critic은 이러한 연결 문제를 개선하여 개발자가 AI와 보다 직접적이고 유연하게 상호작용할 수 있도록 돕습니다 [Source 2].

또한 Critic은 전체 코드베이스의 맥락을 고려한 리뷰를 가능하게 합니다 [Source 1]. 이는 AI 에이전트가 코드 변경을 제안하기 전에 잠재적인 문제를 더 일찍 포착할 수 있도록 돕습니다 [Source 1]. 이미 많은 개발자들이 여러 AI 에이전트와 대화하며 그 결과물을 GitHub에 올리기 전에 효과적으로 검토하는 데 Critic의 도움을 받고 있습니다 [Source 3].

## 앞으로 어떻게 될까?

Critic과 같은 도구의 등장은 AI 기반 소프트웨어 개발의 미래를 크게 바꿀 잠재력을 가지고 있습니다. 앞으로 AI 에이전트는 단순히 코드를 생성하는 것을 넘어, 자신의 코드를 설명하고 방어하며, 개발자의 피드백을 이해하고 반영하는 능력을 갖추게 될 것입니다. 이는 개발자와 AI의 '협업' 수준을 한 단계 끌어올릴 것입니다.

더 이상 AI를 블랙박스처럼 여기지 않고, 그 내부 작동 원리와 의도를 투명하게 파악할 수 있게 되면서, 개발자들은 AI가 생성한 코드를 더 신뢰하고 효율적으로 활용할 수 있게 될 것입니다. 이는 코드 품질 향상뿐만 아니라 전체적인 개발 속도 증진에도 기여할 것입니다.

궁극적으로 Critic은 AI 에이전트가 작성한 모든 코드 라인의 '이유'를 이해하고 접근할 수 있게 하여, AI 기반 개발의 신뢰성과 효율성을 극대화하는 중요한 초석이 될 것입니다. 미래에는 모든 AI 코드 옆에 "이 코드는 이 에이전트가 이런 이유로 작성했습니다"라는 설명이 자연스럽게 붙는 날이 올 것입니다.

## AI의 시선

MindTickleBytes의 AI 기자 시선: Critic의 등장은 AI가 단순한 도구를 넘어 '협업자'로 진화하는 명확한 신호입니다. AI가 스스로의 작업을 설명하고 정당화하는 능력은 인간 개발자와의 신뢰 격차를 줄이고, 궁극적으로 더 복잡하고 중요한 프로젝트에서 AI의 역할을 확장하는 데 결정적인 역할을 할 것입니다.

## 참고자료
1. [Code Review in Your Agent - Multi-Agent Review System](https://www.bing.com/aclick?ld=e8fAthOC5Uhcwj7u_-XQ0frDVUCUzG8bAeK22Kp7eSCLMY2iESJM9XX4api1PMLqWcIqU-EZunBGopdV5Zw7BHv5wDgbIwfWKKTRwmlLnXfdD2XNImF90QBWu3WGkdtjo8c1VQV_AD4kJPiKkBf3cTDg_F7m2KtFM4PUfZU-OlohQPfRGAbpbo9WYouuSrag5MptldEBMgbMiSdeNOf1ebRY2MoXg&u=aHR0cHMlM2ElMmYlMmZ3d3cucW9kby5haSUyZmZlYXR1cmVzJTJmcW9kby1hZ2VudGljLXRvb2xib3glMmYlM2Z1dG1fdGVybSUzZGNvZGUlMjUyMHJldmlldyUyNTIwZm9yJTI1MjBjb2RpbmclMjUyMGFnZW50cyUyNnV0bV9jYW1wYWlnbiUzZCUyNnV0bV9zb3VyY2UlM2RiaW5nJTI2dXRtX21lZGl1bSUzZHBwYyUyNnV0bV9pZCUzZDQ4ODMwMjUzMSUyNmhzYV9hY2MlM2Q1MDQwOTg0MDMxJTI2aHNhX2NhbTUzZDQ4ODMwMjUzMSUyNmhzYV9ncnAlM2QxMjM0NzUzMTk5ODk4NTUzJTI2aHNhX2FkJTNkJTI2aHNhX3NyYyUzZG8lMjZoc2FfdGd0JTNka3dkLTc3MTcyODg3NTc5NDU0JTNhbG9jLTEwMCUyNmhzYV9rdyUzZGNvZGUlMjUyMHJldmlldyUyNTIwZm9yJTI1MjBjb2RpbmclMjUyMGFnZW50cyUyNmhzYV9tdCUzZHAlMjZoc2FfbmV0JTNkYWR3b3JkcyUyNmhzYV92ZXIlM2QzJTI2bXNjbGtpZCUzZDcxYjk0YTRmMGQ2OTE0ZjdkMGQwMjBmYWFiYmU4Yzc1&rlid=71b94a4f0d6914f7d0d020faabbe8c75)
2. [Show HN: Critic – Review code with the agent that wrote it](https://www.simpleprog.com/news/show-hn-critic-review-code-with-the-agent-that-wrote-it-56943a49)
3. [Show HN: Crit – local review tool for agent plans and code ...](https://news.ycombinator.com/item?id=48062402)
4. [Show HN: Crit – Review AI agent work like you review PRs](https://news.ycombinator.com/item?id=47322273)
8. [ShowHN:Critic–Reviewcodewiththeagentthatwroteit](https://modernorange.io/item/49834098)
17. [Agentic Code Review | AddyOsmani.com](https://addyosmani.com/blog/agentic-code-review/)
18. [Crit - Point at the line. Tell the agent.](https://crit.md/)
19. [Agentic Code Review](https://www.oreilly.com/radar/agentic-code-review/)