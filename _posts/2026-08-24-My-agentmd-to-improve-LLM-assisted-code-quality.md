---
layout: post
title: "내 코딩 AI를 똑똑하게 만드는 마법의 파일, AGENTS.md의 진실"
description: "AI 코딩 에이전트에게 프로젝트만의 특별한 규칙을 알려주는 AGENTS.md 파일, 정말 효과가 있을까요?"
summary: "직접 작성한 AGENTS.md 파일은 AI 코딩 성능을 소폭 향상시키지만, AI가 생성한 파일은 오히려 성능을 떨어뜨리고 비용만 높일 수 있습니다."
tags: [AI, 코딩, 개발도구, 생산성]
image: 2026-08-24-My-agentmd-to-improve-LLM-assisted-code-quality.jpg
image_alt: "코드 에디터 화면 위에 AGENTS.md 파일이 열려 있고 AI와 대화하는 모습"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "도구는 도구일 뿐입니다. 에이전트의 규칙은 개발자가 프로젝트의 맥락을 깊이 이해하고 직접 정교하게 설계할 때 비로소 진정한 가치를 발휘합니다."
quiz:
  - question: "사람이 직접 작성한 AGENTS.md 파일은 AI 코딩 에이전트의 성능을 평균적으로 얼마나 향상시키나요?"
    choices: ["약 4%", "약 20%", "약 50%"]
    answer: 0
    explanation: "최근 연구에 따르면 사람이 직접 작성한 AGENTS.md 파일은 AI 에이전트의 코딩 성능을 평균 4% 향상시키는 것으로 나타났습니다."
  - question: "AI(LLM)가 자동으로 생성한 AGENTS.md 파일의 성능에 대한 설명으로 옳은 것은?"
    choices: ["성능을 크게 향상시킨다", "성능에 영향이 없다", "오히려 성능을 떨어뜨릴 수 있다"]
    answer: 2
    explanation: "연구 결과, AI가 생성한 문맥 파일은 오히려 에이전트의 성능을 2~3%가량 하락시키는 것으로 확인되었습니다."
  - question: "AGENTS.md 파일을 도입할 때 고려해야 할 경제적 비용은 무엇인가요?"
    choices: ["도입 비용은 없다", "사용 비용이 20% 이상 증가한다", "도입 시 AI 요금을 50% 할인받는다"]
    answer: 1
    explanation: "문맥 파일(AGENTS.md 등)을 사용하는 것은 AI 코딩 에이전트 이용 비용을 최소 20% 이상 증가시키는 원인이 됩니다."
lang: ko
ref: 2026-08-24-My-agentmd-to-improve-LLM-assisted-code-quality
audio: 2026-08-24-My-agentmd-to-improve-LLM-assisted-code-quality.mp3
permalink: /2026/08/24/My-agentmd-to-improve-LLM-assisted-code-quality/
---

상상해보세요. 새로 입사한 신입 사원에게 우리 회사의 복잡한 코딩 규칙과 테스트 방식을 매번 처음부터 다시 설명해야 한다면 어떨까요? 매일 아침 출근할 때마다 "우리 프로젝트에선 변수 이름은 이렇게 지어주세요", "테스트는 이 라이브러리를 써야 해요"라고 반복하는 것은 매우 소모적인 일입니다.

최근 개발자들 사이에서는 AI 코딩 도구를 사용할 때 이런 반복적인 수고를 덜어줄 '비밀 소스'로 불리는 파일이 있습니다. 바로 `AGENTS.md`입니다. 과연 이 파일이 정말로 우리의 코딩 AI를 더 똑똑하게 만들어줄까요?

### 이게 왜 중요한가요?

AI 코딩 에이전트가 점점 대중화되면서, 많은 개발자가 더 나은 코드를 얻기 위해 고민하고 있습니다. `AGENTS.md`는 AI에게 프로젝트만의 특별한 선호 사항과 규칙을 주입하여 코딩 세션 전체에 걸쳐 유지되도록 돕습니다. [출처: Improve Your AI Assisted Coding With AGENTS.md by Lance Cleveland ∥ Real-World AI Authority](https://lancecleveland.com/2026/02/24/improve-your-ai-assisted-coding-with-agents-md/) 이 파일을 잘 활용하면 개발자는 AI에게 프로젝트의 맥락을 매번 설명하지 않아도, 일관된 품질의 코드를 생산할 수 있는 환경을 만들 수 있습니다. [출처: How to teach your coding agent with AGENTS.md](https://ericmjl.github.io/blog/2025/10/4/how-to-teach-your-coding-agent-with-agentsmd/)

### 쉽게 말해서

`AGENTS.md`는 일종의 '프로젝트 가이드북'이라고 비유할 수 있습니다. 

비유하자면, 우리가 요리사를 고용했을 때 그냥 "맛있는 음식을 만들어달라"고 하는 것보다, "우리 집은 저염식을 선호하고, 특정 향신료는 사용하지 않으며, 요리 후에는 항상 싱크대를 이렇게 정리해달라"는 상세한 레시피와 매너를 적은 쪽지를 건네주는 것과 같습니다. AI 코딩 에이전트가 작업을 시작할 때 이 파일을 프롬프트에 자동으로 불러와 읽게 함으로써, AI가 어떤 스타일로 코드를 짜고 어떤 규칙을 지켜야 할지 명확하게 이해하게 만드는 것입니다. [출처: My agent.md to improve LLM-assisted code quality](https://fabiensanglard.net/agent.md/index.html)

하지만 주의할 점이 있습니다. '똑똑한 요리사'를 훈련하는 것처럼, 이 파일도 사람이 직접 정교하게 작성해야 효과가 있습니다. 최근 ETH 취리히 연구진이 진행한 벤치마크 평가에 따르면, 사람이 직접 꼼꼼하게 작성한 문맥 파일은 에이전트의 코딩 성능을 평균 4% 정도 개선하는 효과를 보였습니다. [출처: Does AGENTS.md Actually Help Coding Agents? A New Study Has ...](https://academy.dair.ai/blog/agents-md-evaluation) 이는 아주 큰 변화는 아니지만, 매일 코딩을 하는 개발자 입장에서는 무시할 수 없는 실질적인 효율성 향상입니다. [출처: Evaluating AGENTS.md: are they helpful for coding agents? | Hacker News](https://news.ycombinator.com/item?id=47034087)

### 어디까지 와 있을까?

안타깝게도 많은 분이 범하는 실수가 있습니다. 바로 "AI가 똑똑하니 `AGENTS.md`도 AI한테 써달라고 하면 되겠지?"라고 생각하는 것입니다. 연구 결과는 정반대였습니다. AI가 자동으로 생성한 문맥 파일을 사용할 경우, 오히려 에이전트의 성능이 2%에서 3%가량 하락할 수 있다는 사실이 드러났습니다. [출처: Controlling Claude Code & Coding Agent Behavior with AGENTS ...](https://devcheolu.com/en/posts/mjMpJ0tktBPBt7Mdpfgc) 마치 엉뚱한 요리법을 적은 쪽지를 요리사에게 주는 것과 같아서, AI가 잘못된 규칙을 학습하게 되는 셈입니다.

또한, 비용적인 측면도 간과해서는 안 됩니다. `AGENTS.md`와 같은 문맥 파일을 사용하면 AI 코딩 에이전트를 이용할 때 발생하는 비용이 최소 20% 이상 증가하게 됩니다. [출처: Does AGENTS.md Actually Help Coding Agents? A New Study Has ...](https://academy.dair.ai/blog/agents-md-evaluation) 파일이 프롬프트에 매번 포함되어 전송되기 때문에 발생하는 데이터 사용료인 셈입니다.

### 앞으로의 전망

전문가들은 이런 파일이 그저 마법의 도구가 아니라, 개발자의 노력이 담긴 정교한 설정 도구라는 점을 강조합니다. 일부 비판적인 시각에서는 `AGENTS.md`가 사실은 중복되는 추상화에 불과하며, AI 도구가 프로젝트 문서를 잘 참조할 수만 있다면 표준 문서화 방식만으로도 충분하다고 지적하기도 합니다. [출처: 我的 agent.md，用于提升 LLM 辅助代码质量](https://memedata.com/post/141483)

결론적으로, 성능 향상을 원하신다면 AI에게 맡기지 말고 직접 시간을 투자해 프로젝트의 핵심 규칙과 테스트 스타일, 도구 사용법 등을 담은 나만의 `AGENTS.md`를 만들어보세요. [출처: How to teach your coding agent with AGENTS.md](https://ericmjl.github.io/blog/2025/10/4/how-to-teach-your-coding-agent-with-agentsmd/) 비록 4%의 성능 개선을 위해 20%의 비용을 더 지불해야 하는 구조지만, 생산성과 코드 품질을 최우선으로 하는 환경이라면 충분히 고려해볼 가치가 있는 투자입니다. [출처: Evaluating AGENTS.md: are they helpful for coding agents? | Hacker News](https://news.ycombinator.com/item?id=47034087)

---

## MindTickleBytes의 AI 기자 시선
AI 에이전트가 코딩을 대신해주는 시대가 왔지만, 결국 '좋은 질문과 명확한 규칙'을 제공하는 것은 여전히 인간 개발자의 몫입니다. 도구에 의존하기보다, 프로젝트의 철학을 AI에게 어떻게 전달할지 고민하는 능력이 진짜 실력이 되는 시점입니다.

## 참고자료
1. [My agent.md to improve LLM-assisted code quality](https://fabiensanglard.net/agent.md/index.html)
2. [Improve Your AI Assisted Coding With AGENTS.md by Lance Cleveland ∥ Real-World AI Authority](https://lancecleveland.com/2026/02/24/improve-your-ai-assisted-coding-with-agents-md/)
3. [How to teach your coding agent with AGENTS.md](https://ericmjl.github.io/blog/2025/10/4/how-to-teach-your-coding-agent-with-agentsmd/)
4. [Evaluating AGENTS.md: are they helpful for coding agents? | Hacker News](https://news.ycombinator.com/item?id=47034087)
5. [How to Build Your AGENTS.md (2026): The Context File That Makes AI Coding Agents Actually Work | Augment Code](https://www.augmentcode.com/guides/how-to-build-agents-md)
6. [Stop Getting Average Code from Your LLM | Krzysztof Zabłocki](https://merowing.info/posts/stop-getting-average-code-from-your-llm/)
7. [New Research Reassesses the Value of AGENTS.md Files for AI Coding - InfoQ](https://www.infoq.com/news/2026/03/agents-context-file-value-review/)
8. [My agent.md to improve LLM-assisted code quality | Hacker News](https://news.ycombinator.com/item?id=49410932)
9. [What AGENTS.md Actually Does to Your Coding Agent](https://agentic-academy.ai/posts/agents-md-context-files-evaluation/)
10. [Does AGENTS.md Actually Help Coding Agents? A New Study Has ...](https://academy.dair.ai/blog/agents-md-evaluation)
11. [Controlling Claude Code & Coding Agent Behavior with AGENTS ...](https://devcheolu.com/en/posts/mjMpJ0tktBPBt7Mdpfgc)
12. [我的 agent.md，用于提升 LLM 辅助代码质量](https://memedata.com/post/141483)
13. [How to write a great agents.md: Lessons from over 2,500 ...](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/)
14. [[2511.04427] Speed at the Cost of Quality: How Cursor AI ...What AGENTS.md Actually Does to Your Coding AgentHow to Build Your AGENTS.md (2026): The Context File That ...](https://arxiv.org/abs/2511.04427)