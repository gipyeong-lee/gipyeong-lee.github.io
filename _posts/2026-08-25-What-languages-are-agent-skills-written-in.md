---
layout: post
title: "AI에게 '스킬'을 가르치는 법, 꼭 영어로만 코딩해야 할까요?"
description: "AI 에이전트의 능력을 확장하는 '에이전트 스킬'을 작성할 때 사용하는 프로그래밍 언어와 언어 선택의 자유에 대해 알아봅니다."
summary: "AI 에이전트 스킬은 파이썬, 자바스크립트 등 다양한 언어로 작성 가능하며, 다국어 모델 덕분에 모국어로도 정교한 지시가 가능합니다."
tags: [AI, 에이전트스킬, 프로그래밍, 파이썬]
image: 2026-08-25-What-languages-are-agent-skills-written-in.jpg
image_alt: "다양한 코딩 언어 아이콘들이 AI 에이전트의 구조를 형성하는 추상적인 일러스트레이션"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 모델이 언어의 장벽을 허물면서, 이제 프로그래밍은 '영어 지식'이 아닌 '논리적 표현력'의 영역으로 진화하고 있습니다."
quiz:
  - question: "AI 에이전트 스킬 작성 시 가장 중요하게 고려해야 할 점은 무엇인가요?"
    choices: ["반드시 영어로만 작성해야 한다", "사용하는 에이전트 구현체에서 지원하는 언어를 확인해야 한다", "파이썬만 사용해야 한다"]
    answer: 1
    explanation: "지원되는 언어는 사용하는 에이전트 구현체에 따라 다르기 때문에, 사전에 확인이 필요합니다."
  - question: "에이전트 스킬을 꼭 영어로 작성하지 않아도 되는 기술적 이유는 무엇인가요?"
    choices: ["컴파일러가 자동 번역해주기 때문에", "런타임 환경인 AI 모델이 다국어를 이해하기 때문에", "영어가 필요 없도록 코드가 간소화되었기 때문에"]
    answer: 1
    explanation: "에이전트 스킬의 런타임이 다국어 모델이기 때문에, 개발자는 자신의 모국어로 더 정교하게 절차를 기술할 수 있습니다."
  - question: "일반적으로 에이전트 스킬 작성에 널리 사용되는 언어들은 무엇인가요?"
    choices: ["파이썬, Bash, 자바스크립트", "HTML, CSS, SQL", "C, Rust, Go"]
    answer: 0
    explanation: "Python, Bash, JavaScript 등이 에이전트 스킬 작성에 공통적으로 많이 사용되는 옵션입니다."
lang: ko
ref: 2026-08-25-What-languages-are-agent-skills-written-in
audio: 2026-08-25-What-languages-are-agent-skills-written-in.mp3
permalink: /2026/08/25/What-languages-are-agent-skills-written-in/
---

상상해보세요. 여러분이 AI에게 "내 일정 관리 도와줘"라고 말했는데, AI가 단순히 답변만 하는 게 아니라 직접 캘린더 앱을 열어 일정을 등록하고, 회의 링크를 생성해 메신저로 공유까지 한다면 어떨까요? 여기서 AI가 특정 작업을 수행하는 능력을 우리는 '에이전트 스킬(Agent Skills)'이라고 부릅니다. 

그런데 문득 이런 궁금증이 생기지 않나요? "AI에게 이런 기술을 가르치려면, 반드시 영어로 된 복잡한 프로그래밍 언어를 배워야 할까?" 코딩에 익숙하지 않은 분들에게는 이 질문이 AI를 활용하는 데 있어 가장 큰 문턱처럼 느껴질지도 모릅니다. 오늘은 이 문턱 뒤에 숨겨진 흥미로운 사실들을 함께 살펴보겠습니다.

### 이게 왜 중요한가요?

과거에 컴퓨터와 대화하려면 C언어나 파이썬(Python) 같은 프로그래밍 언어를 완벽하게 숙달해야 했습니다. 하지만 AI 에이전트 시대에는 이야기가 조금 다릅니다. 에이전트 스킬은 AI가 인간의 조수처럼 복잡한 업무를 자동화하게 만들어 줍니다. 

이 기술을 어떻게 작성하느냐에 따라 누군가는 전 세계를 무대로 일하는 생산성을 얻을 수도 있고, 누군가는 여전히 언어와 기술의 장벽에 부딪힐 수도 있습니다. 더 많은 사람이 AI에게 필요한 스킬을 가르칠 수 있다는 것은 곧, 우리 일상에 AI가 얼마나 더 깊숙이, 그리고 편리하게 녹아들 수 있는지를 결정하는 핵심적인 열쇠가 됩니다.

### 쉽게 이해하기: 요리 레시피와 같은 원리

에이전트 스킬을 작성하는 것은 마치 '요리 레시피'를 적는 것과 비슷합니다. 요리사(AI 에이전트)에게 맛있는 스파게티를 만드는 법(스킬)을 알려주려면, 요리사가 알아들을 수 있는 언어(프로그래밍 언어)로 순서를 명확하게 적어야 하죠.

가장 먼저 알아두어야 할 점은 **'정해진 하나의 언어는 없다'**는 것입니다. 현재 AI 에이전트를 구현하는 방식에 따라 파이썬, 배시(Bash, 리눅스 시스템 제어 언어), 자바스크립트(JavaScript, 웹 개발용 언어) 등 다양한 언어가 스킬 작성에 사용되고 있습니다 [Source 4]. 파이썬과 같이 범용적인(Versatile, 다양한 용도로 쓰이는) 언어부터, 특정 목적에 특화된 언어까지 그 범위가 매우 넓습니다 [Source 7].

하지만 여기서 아주 흥미로운 반전이 있습니다. 에이전트 스킬을 실행하는 '뇌' 역할을 하는 것이 바로 다국어를 이해하는 AI 모델이기 때문입니다. 그래서 기술적으로는 영어가 반드시 필요하지 않습니다 [Source 1]. 

쉽게 말해, 레시피를 작성하는 개발자가 영어가 아닌 모국어를 사용해도 된다는 뜻입니다. 중국 선전이나 브라질 상파울루에 있는 개발자들은 자신의 모국어로 절차를 훨씬 더 정교하고 명확하게 기술할 수 있으며, AI 에이전트는 이를 충분히 이해하고 따라올 수 있습니다 [Source 1]. 마치 한국인 셰프가 한국어로 적힌 레시피를 보고 요리하는 것처럼, AI도 더 익숙한 언어로 적힌 지시를 더 정확하게 수행할 수 있는 시대가 온 것입니다.

### 현재 상황: 이미 시작된 공유의 시대

지금 당장은 파이썬 기반의 스킬 정의와 실행, 승인 절차를 지원하는 프레임워크들이 활발히 개발되고 있습니다 [Source 6]. 이미 많은 개발자들이 GitHub 같은 플랫폼을 통해 자신만의 유용한 스킬을 공개하고 공유하고 있으며, 이를 통해 다른 이들의 AI 에이전트 능력을 쉽게 확장할 수 있는 환경이 조성되어 있습니다 [Source 8], [Source 10]. 

물론 고려해야 할 점도 있습니다. 코드를 작성하는 비용은 점점 낮아지고 있지만, AI가 생성하는 코드의 양이 방대해지면서 오히려 그 코드가 실제로 무엇을 하는지, 오류는 없는지 확인하는 리뷰 과정이 더 중요해지고 있습니다 [Source 2]. AI에게 일을 시키기 위해 코드를 짤 때도, 단순히 '돌아가는 코드'를 넘어 '명확하고 이해하기 쉬운 코드'를 작성하는 기술이 필요한 시점입니다.

### 앞으로 어떻게 될까?

앞으로는 '어떤 프로그래밍 언어를 쓰는가'라는 도구보다, '무엇을, 어떤 순서로 시킬 것인가'라는 논리적 사고력이 더 중요해질 것입니다. [Source 9]에서 볼 수 있듯이 스킬은 이제 복사해서 설치하기만 하면 되는 재사용 가능한 '능력 단위'로 자리 잡고 있습니다. 

여러분이 기억해야 할 핵심은 이것입니다. AI 에이전트에게 일을 시키기 위해 굳이 영어 공부에 매달릴 필요가 없습니다. 본인이 가장 잘하는 언어로 논리적인 절차를 구성할 수 있다면, AI는 그 언어의 장벽을 넘어 여러분의 비즈니스나 일상을 돕는 강력한 파트너가 될 것입니다. 앞으로는 공개된 스킬 마켓플레이스에서 내 입맛에 맞는 스킬을 골라 내 에이전트에게 장착하는 '스킬 쇼핑'의 시대가 더욱 본격화될 전망입니다 [Source 8].

---

**MindTickleBytes의 AI 기자 시선**
AI가 언어의 장벽을 허물면서 이제 프로그래밍은 더 이상 소수 전문가의 전유물이 아닌, '자신의 의도를 논리적으로 전달하는 대화의 기술'이 되고 있습니다. 이제는 무엇을 코딩할지 고민하기보다, 무엇을 해결할지를 고민하는 것이 진정한 실력이 될 것입니다.

## 참고자료

1. What language are agent skills written in? · Plicara Labs: https://plicara.ai/research/agent-skill-languages/
2. A Language For Agents | Armin Ronacher's Thoughts and Writings: https://lucumr.pocoo.org/2026/2/9/a-language-for-agents/
4. Agent Skills — Intuitively and Exhaustively Explained: https://iaee.substack.com/p/agent-skills-intuitively-and-exhaustively
6. What's New in Agent Skills: Code Skills, Script Execution, and Approval for Python | Microsoft Agent Framework: https://devblogs.microsoft.com/agent-framework/whats-new-in-agent-skills-code-skills-script-execution-and-approval-for-python/
7. Understanding AI Agent Programming Languages - SmythOS: https://smythos.com/developers/agent-development/ai-agent-programming-languages/
8. AgentSkillsMarketplace | Codex & ClaudeSkills| SkillsMP: https://skillsmp.com/
9. Discover and installskillsfor AIagents.: https://www.skills.sh/
10. GitHub - addyosmani/agent-skills: Production-grade engineeringskills...: https://github.com/addyosmani/agent-skills