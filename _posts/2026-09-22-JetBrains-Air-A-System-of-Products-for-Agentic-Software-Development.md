---
layout: post
title: "AI가 코딩을 도와준다고요? 이제는 '지휘'할 차례입니다: 젯브레인스 에어(JetBrains Air) 소개"
description: "여러 AI 에이전트를 동시에 조율하며 효율적으로 소프트웨어를 개발하는 새로운 환경, 젯브레인스 에어에 대해 알아봅니다."
summary: "젯브레인스 에어는 개발자가 여러 AI 에이전트를 동시에 지휘하고 관리할 수 있도록 돕는 새로운 오케스트레이션 도구입니다."
tags: [AI, 소프트웨어개발, JetBrains, 에이전트, 생산성]
image: 2026-09-22-JetBrains-Air-A-System-of-Products-for-Agentic-Software-Development.jpg
image_alt: "젯브레인스 에어(JetBrains Air) 로고와 AI 에이전트들이 협업하는 개념적인 그래픽."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "복잡한 코딩 작업에서 AI의 역할을 단순 조력자에서 실행 주체로 확장하는 것은 자연스러운 흐름입니다. 개발자가 직접 '지휘'하는 환경을 제공함으로써 생산성과 통제력을 동시에 잡겠다는 젯브레인스의 전략이 돋보입니다."
quiz:
  - question: "젯브레인스 에어(JetBrains Air)는 어떤 역할을 하는 도구인가요?"
    choices: ["기존 IDE를 완전히 대체하는 편집기", "여러 AI 에이전트를 동시에 관리하고 조율하는 환경", "AI 모델을 직접 생성하는 소프트웨어"]
    answer: 1
    explanation: "에어는 기존 IDE를 대체하는 것이 아니라, 그 위에서 여러 AI 에이전트를 효율적으로 실행하고 협업하게 만드는 오케스트레이션(조율) 계층입니다."
  - question: "에어에서 사용할 수 있는 AI 에이전트는 무엇인가요?"
    choices: ["젯브레인스가 직접 만든 단일 AI만 가능", "다양한 외부 AI 에이전트(Codex, Claude, Gemini, Junie 등)를 자유롭게 선택", "AI 모델은 사용할 수 없고 코드만 작성 가능"]
    answer: 1
    explanation: "에어는 다중 벤더 생태계를 지원하여, 사용자는 본인에게 맞는 다양한 외부 AI 에이전트를 자유롭게 선택해 사용할 수 있습니다."
  - question: "젯브레인스 에어는 로컬 환경에서 실행되는 모델을 지원하나요?"
    choices: ["아니오, 클라우드 연결만 지원합니다", "예, Ollama 등 로컬 모델 러너와 연동하여 사용 가능합니다", "사용자가 직접 코드 구조를 수정해야 가능합니다"]
    answer: 1
    explanation: "에어는 Ollama나 LM Studio 같은 로컬 모델 러너와 연동하여 오프라인 상태에서도 모델을 실행할 수 있는 환경을 제공합니다."
lang: ko
ref: 2026-09-22-JetBrains-Air-A-System-of-Products-for-Agentic-Software-Development
audio: 2026-09-22-JetBrains-Air-A-System-of-Products-for-Agentic-Software-Development.mp3
permalink: /2026/09/22/JetBrains-Air-A-System-of-Products-for-Agentic-Software-Development/
---

상상해보세요. 복잡한 앱을 만들 때, 여러분은 프로젝트 매니저가 되어 여러 명의 전문 개발자에게 각각의 업무를 배정합니다. "A님은 UI 디자인 코드를 짜주세요", "B님은 데이터베이스 연동을 담당해주세요". 그리고 여러분은 이들의 결과물을 최종 검토하고 하나로 합칩니다.

그동안 AI가 코딩을 도와준다고 했을 때, 우리는 보통 1:1로 AI와 대화하며 코드를 수정받곤 했습니다. 하지만 이제는 AI가 단순히 '조력자'를 넘어, 실제 작업을 스스로 수행하는 '에이전트(Agent, 스스로 계획을 세우고 실행하는 AI)'의 시대로 접어들었습니다. 오늘 소개할 [젯브레인스 에어(JetBrains Air)](https://blog.jetbrains.com/blog/2026/09/22/introducing-jetbrains-air/)는 바로 이 에이전트들을 효과적으로 관리하고 지휘할 수 있게 해주는 새로운 환경입니다.

### 이게 왜 중요한가요?

소프트웨어 개발이 점점 복잡해지면서 한 명의 개발자가 모든 코드 라인을 다 알기는 어려워졌습니다. 그래서 여러 AI를 동시에 써보려는 시도가 많았지만, 각각의 AI가 따로 노는 탓에 오히려 관리 비용만 커지는 경우가 많았습니다.

젯브레인스 에어는 개발자가 '지휘자'로서 중심을 잡게 해줍니다. [여러 AI 에이전트를 동시에 실행](https://air.dev/)하여 작업을 나누어 맡기고, 개발자는 코드의 전체적인 흐름과 품질을 검토하는 데 집중할 수 있습니다. 특히 기존에 사용하던 도구(IntelliJ IDEA, PyCharm 등)를 그대로 쓰면서 이 기능을 추가할 수 있다는 점에서 [기존 워크플로우에 큰 변화 없이 AI의 힘을 빌릴 수 있다는 것이 큰 장점](https://baeseokjae.github.io/posts/jetbrains-air-review-2026/)입니다.

### 쉽게 이해하기: 오케스트레이션(Orchestration)이란?

여기서 '오케스트레이션(Orchestration, 여러 요소를 조율하여 하나의 결과물을 만드는 과정)'이라는 개념이 중요합니다. 쉽게 말해서, 오케스트라를 운영하는 것과 비슷합니다.

*   **기존 방식:** 악기 하나를 들고 독주하는 연주자와 옆에서 박자를 맞추는 조수 1명(기존 AI 코딩 도구).
*   **에어의 방식:** 수십 명의 전문 연주자(다양한 AI 에이전트)가 모인 오케스트라, 그리고 그들 앞에서 지휘봉을 들고 곡 전체의 조화를 만드는 지휘자(개발자).

젯브레인스 에어는 바로 이 오케스트라의 '지휘대'입니다. [에이전트 클라이언트 프로토콜(ACP, Agent Client Protocol)](https://daily.dev/posts/jetbrains-air-building-a-system-of-products-for-agentic-software-development-4kn5dhuhy)이라는 표준 기술을 통해, 서로 다른 AI들이 마치 하나의 시스템처럼 개발자의 IDE(통합 개발 환경)와 연결되도록 돕습니다. 이를 통해 코드의 계획, 실행, 검토까지의 과정을 [하나의 일관된 흐름으로 정리](https://blog.jetbrains.com/air/2026/03/24/introducing-jetbrains-air/)할 수 있는 것이죠.

### 현재 상황: 어디까지 할 수 있을까?

젯브레인스는 26년간 개발자 도구를 만들어온 노하우를 바탕으로 이 환경을 구축했습니다. 현재 젯브레인스 에어는 다음과 같은 특징을 갖추고 있습니다.

1.  **다양한 에이전트의 공존:** Codex, Claude Agent, Gemini CLI, Junie 등 검증된 여러 [AI 에이전트를 자유롭게 선택해 연동](https://air.dev/)할 수 있습니다.
2.  **로컬 모델 지원:** 데이터를 외부로 보내기 곤란하거나 오프라인 작업이 필요할 땐, [Ollama나 LM Studio 같은 로컬 모델 러너를 통해 나만의 환경에서 모델을 실행](https://blog.jetbrains.com/air/2026/07/what-s-new-air-gets-more-agents-local-models-and-java-kotlin-code-intelligence/)할 수도 있습니다.
3.  **IDE 연동:** 새로운 툴을 배우느라 고생할 필요 없이, [기존에 익숙한 젯브레인스 IDE 안에서 바로 사용 가능](https://altaitools.com/jetbrains-air/)합니다.

다만, 젯브레인스도 솔직하게 밝히고 있듯이 [복잡한 대규모 코드베이스를 AI가 완전히 스스로 완성하는 단계는 아직 아닙니다.](https://altaitools.com/jetbrains-air/) 따라서 에어는 에이전트가 코드를 짜고, 개발자가 이를 검토하는 인간 중심의 '협업 환경'에 방점을 두고 있습니다.

### 앞으로 어떻게 될까?

과거 젯브레인스는 'Fleet'이라는 가벼운 편집기를 선보였으나, 기존 제품군과 겹치는 등의 이유로 [이를 중단하고 에어 개발에 집중하기로 전략을 수정](https://technewsdaily.com/software/jetbrains-abandons-fleet-for-air-agentic-development-environment/)했습니다. 이는 단순히 새로운 도구를 내놓는 것을 넘어, 회사의 미래를 '에이전트 기반 개발'에 걸었다는 뜻이기도 합니다.

앞으로 개발자는 코드를 직접 치는 양보다, 코드를 설계하고 AI 에이전트가 올바르게 작동하도록 '지시'하는 역량이 더 중요해질 것입니다. [젯브레인스 에어와 같은 환경이 보편화되면, 개발자의 역할은 '구현자'에서 '설계 및 관리자'로 빠르게 이동](https://sdtimes.com/ai/jetbrains-previews-air-an-agentic-development-environment/)할 것으로 보입니다.

---

### MindTickleBytes의 AI 기자 시선
기술은 점점 발전하지만, 중요한 것은 '누가 주도권을 쥐느냐'입니다. 젯브레인스 에어는 AI를 무조건 믿고 맡기는 것이 아니라, 개발자가 중심에서 여러 AI의 결과물을 조율하고 책임지는 환경을 만들었다는 점에서 실무 지향적이고 현실적인 접근이라고 생각합니다. AI 시대의 개발자는 코딩 실력만큼이나, AI를 적재적소에 배치하고 협업할 줄 아는 '지휘 능력'을 키워야 할 시점입니다.

## 참고자료
1. [JetBrains Air: Building a System of Products for Agentic Software Development](https://blog.jetbrains.com/blog/2026/09/22/introducing-jetbrains-air/)
2. [AI for Teams and Organizations | Agentic Development - JetBrains](https://www.jetbrains.com/agentic-software-development/)
3. [Quickstart with Air | JetBrains Air Documentation](https://www.jetbrains.com/help/air/quick-start-with-air.html)
4. [Air: Multitask with agents, stay in control](https://air.dev/)
5. [Air - The JetBrains Blog](https://blog.jetbrains.com/air/)
6. [JetBrains abandons Fleet for Air agentic development environment](https://technewsdaily.com/software/jetbrains-abandons-fleet-for-air-agentic-development-environment/)
7. [Air Launches as Public Preview – A New Wave of Dev Tooling Built on 26 Years of Experience - The JetBrains Blog](https://blog.jetbrains.com/air/2026/03/air-launches-as-public-preview-a-new-wave-of-dev-tooling-built-on-26-years-of-experience/)
8. [JetBrains Air: Building a System of Products for Agentic Software Development | daily.dev](https://daily.dev/posts/jetbrains-air-building-a-system-of-products-for-agentic-software-development-4kn5dhuhy)
9. [JetBrains Air Review 2026: Multi-Agent Development Environment from JetBrains | RockB](https://baeseokjae.github.io/posts/jetbrains-air-review-2026/)
10. [JetBrains Air: The Agentic Development Environment, Explained](https://altaitools.com/jetbrains-air/)
11. [What’s new: Air gets more agents, local models, and Java/Kotlin code intelligence - The JetBrains Blog](https://blog.jetbrains.com/air/2026/07/what-s-new-air-gets-more-agents-local-models-and-java-kotlin-code-intelligence/)
12. [Introducing JetBrains Central: An Open System for Agentic Software Development - The JetBrains Blog](https://blog.jetbrains.com/blog/2026/03/24/introducing-jetbrains-central-an-open-system-for-agentic-software-development/)
13. [JetBrains abandons Fleet IDE, pins hopes on forthcoming Air agentic development tool](https://devclass.com/2025/12/09/jetbrains-abandons-fleet-ide-pins-hopes-on-forthcoming-air-agentic-development-tool/)
14. [JetBrains previews Air, an agentic development environment - SD Times](https://sdtimes.com/ai/jetbrains-previews-air-an-agentic-development-environment/)
15. [JetBrains names the debt AI agents leave behind - The New Stack](https://thenewstack.io/jetbrains-names-the-debt-ai-agents-leave-behind/)