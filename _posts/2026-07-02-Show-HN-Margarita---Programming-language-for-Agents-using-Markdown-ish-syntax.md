---
layout: post
title: "AI 비서 만들기, 메모장 쓰는 것처럼 쉬워질까요? 마크다운으로 설계하는 '마가리타(Margarita)'"
description: "코딩을 몰라도 AI 에이전트를 만들 수 있을까요? 마크다운 형식을 확장해 AI 에이전트의 작업 흐름을 체계적으로 작성하는 새로운 도구, 마가리타를 소개합니다."
summary: "마가리타(Margarita)는 마크다운 문법에 변수, 반복문 등 프로그래밍 기능을 더해 누구나 쉽게 AI 에이전트의 작업 흐름을 설계할 수 있게 돕는 도구입니다."
tags: [AI, 에이전트, 마크다운, 프로그래밍, 마가리타]
image: 2026-07-02-Show-HN-Margaritapermalink: /2026/07/02/Show-HN-Margarita---Programming-language-for-Agents-using-Markdown-ish-syntax/
---Programming-language-for-Agents-using-Markdown-ish-syntax.jpg
image_alt: "마크다운 문법을 이용해 AI 에이전트의 복잡한 작업 흐름을 체계적으로 구조화한 모습"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "복잡한 코딩 없이 AI 에이전트의 논리를 설계하려는 시도는 에이전트 대중화의 중요한 열쇠가 될 것입니다."
quiz:
  - question: "마가리타(Margarita)의 주요 특징 중 하나인 .mgx 파일 형식은 무엇을 지원하나요?"
    choices: ["정적 텍스트 생성", "AI 에이전트의 실행 제어(상태, 메모리, 도구 호출 등)", "단순한 HTML 변환"]
    answer: 1
    explanation: ".mgx 형식은 기존 .mg 형식을 확장하여 AI 에이전트가 실행될 때 필요한 상태 관리나 도구 호출 등의 기능을 추가로 제공합니다."
  - question: "마가리타(Margarita)를 사용하기 위해 필요한 AI 모델은 무엇인가요?"
    choices: ["모든 종류의 모델", "Ollama와 Claude", "특정 언어 모델만 가능"]
    answer: 1
    explanation: "마가리타는 현재 사용을 위해 Ollama와 Claude를 필요로 합니다."
  - question: "마가리타(Margarita)의 목표는 무엇인가요?"
    choices: ["복잡한 프로그래밍 언어 학습", "마크다운만큼 쉽게 에이전트 작성하기", "검색 엔진 최적화"]
    answer: 1
    explanation: "마가리타는 에이전트를 작성하는 일이 마크다운을 쓰는 것만큼 쉬워지도록 만드는 것을 목표로 합니다."
lang: ko
ref: 2026-07-02-Show-HN-Margarita---Programming-language-for-Agents-using-Markdown-ish-syntax
audio: 2026-07-02-Show-HN-Margarita---Programming-language-for-Agents-using-Markdown-ish-syntax.mp3
---

상상해보세요. 여러분이 아침에 일어나서 AI 비서에게 "오늘의 회의 자료를 정리해서 요약해줘"라고 말합니다. 그러자 AI는 마치 사람처럼 스스로 필요한 파일을 찾고, 내용을 요약한 뒤 결과물을 이메일로 보내줍니다. 이런 똑똑한 비서를 우리는 'AI 에이전트'라고 부릅니다. 그런데 이런 에이전트를 만드는 과정은 지금까지 매우 복잡했습니다. 개발자들은 복잡한 코드를 짜고, AI가 시키는 대로 잘 따라오도록 계속해서 '프롬프트(AI에게 입력하는 지시문)'와 씨름해야 했죠.

그런데 최근, 마치 우리가 블로그에 글을 쓰거나 메모를 할 때 사용하는 '마크다운(Markdown, 웹 문서를 쉽게 만들기 위한 문법)'처럼 아주 간단하게 AI 에이전트를 설계할 수 있는 새로운 도구가 등장했습니다. 바로 '마가리타(Margarita)'입니다.

### 왜 이 도구가 중요한가요?

지금까지 AI와 소통하는 방식은 주로 '대화' 위주였습니다. 하지만 대화는 때때로 AI가 사용자의 의도를 오해하거나, 긴 작업 과정에서 길을 잃게 만들기도 합니다. 개발자들은 AI가 복잡한 업무를 단계별로 완수하게 하려고 프롬프트 작성에 매달려야 했습니다. [출처 1](https://www.margarita.run/)

마가리타는 이런 어려움을 해결합니다. AI 에이전트의 행동을 복잡한 코드가 아닌, 누구나 익숙한 마크다운 방식으로 정해진 규칙에 따라 설계할 수 있게 해주기 때문입니다. 이는 더 이상 복잡한 프롬프트 엔지니어링에 매달리지 않고도, 원하는 결과를 체계적이고 일관되게 얻을 수 있다는 것을 의미합니다. [출처 1](https://www.margarita.run/)

### 쉽게 이해하기: 마크다운에 날개를 달다

마가리타를 이해하기 위해 비유를 하나 들어볼게요. 우리가 요리를 할 때 레시피 카드를 적는다고 상상해보세요. 기존의 방식이 요리사에게 일일이 "지금 양파 썰어주세요", "이제 불 조절 하세요"라고 말하며 쫓아다니는 것이라면, 마가리타는 미리 체계적인 '레시피 카드'를 작성해두는 것과 같습니다.

쉽게 말해서, 마가리타는 우리가 흔히 아는 마크다운 문법에 프로그래밍 기능을 섞었습니다. [출처 1](https://www.margarita.run/) 주요 기능은 다음과 같습니다.
- **변수(Variable)**: 정보의 값을 저장하는 칸.
- **반복문(Loop)**: 여러 항목을 하나씩 순서대로 처리하는 규칙.
- **조건문(Conditional)**: '만약 ~라면 이렇게 해라'는 결정.

이렇게 마크다운에 논리적인 기능을 추가해서 AI 에이전트가 어떤 상황에서 어떻게 행동해야 할지를 명확하게 명시하는 것이죠. [출처 4](https://github.com/Banyango/margarita) 마가리타는 두 가지 파일 형식을 제공합니다. [.mg 파일](https://pypi.org/project/margarita/)은 동적인 프롬프트를 만드는 데 쓰이고, [.mgx 파일](https://pypi.org/project/margarita/)은 더 나아가 에이전트의 메모리 관리나 도구 호출까지 제어하는 '에이전트 스크립트' 역할을 합니다. [출처 2](https://pypi.org/project/margarita/)

이렇게 작성된 결과물은 기본적으로 우리가 잘 아는 마크다운 형식으로 렌더링(화면에 보여줌)되기 때문에, 마크다운을 지원하는 곳이라면 어디서든 사용할 수 있습니다. [출처 4](https://github.com/Banyango/margarita)

### 현재 상황: 어디까지 왔을까?

마가리타는 개발자가 에이전트를 구성하고 논리를 쌓아가는 과정을 훨씬 단순하게 만들어줍니다. 특히 여러 템플릿을 나누어 저장하고, 필요할 때 가져다 쓰거나 겹쳐서 사용하는(Nested) 방식이 가능해져 업무 효율을 크게 높였습니다. [출처 3](https://www.banyango.com/margarita/)

다만 현재 이 도구를 활용하기 위해서는 Ollama와 Claude 모델에 대한 환경 설정이 필요하다는 점은 기억해야 합니다. [출처 3](https://www.banyango.com/margarita/) 즉, 완전한 초보자가 쓰기보다는 어느 정도 AI 개발 환경에 대한 이해가 있는 사용자가 생산성을 높이기 위해 활용하기 좋은 단계입니다.

### 앞으로 어떻게 될까?

전문가들은 머지않은 미래에 마크다운이 단순한 문서 형식을 넘어, 소프트웨어 개발의 핵심 언어로 자리 잡을 것이라고 예측합니다. [출처 13](https://www.infoworld.com/article/4146579/markdown-is-now-a-first-class-coding-language-deal-with-it.html) 마가리타와 같은 도구는 이런 흐름을 가속화할 것입니다. 앞으로 AI 에이전트를 만드는 일은 점점 더 자연스러운 언어와 친숙한 문서 형식을 닮아갈 것입니다. 여러분도 이제 '프롬프트'를 짜는 사람이 아니라, 에이전트라는 '비서의 행동 매뉴얼'을 작성하는 관리자가 되는 시대가 오고 있습니다.

---

### MindTickleBytes의 AI 기자 시선
기술이 복잡해질수록 이를 다루는 도구는 더 직관적이고 쉬워져야 합니다. 마크다운으로 에이전트를 정의하려는 마가리타의 시도는 AI와 인간이 협업하는 방식을 근본적으로 더 투명하게 만들 것입니다.

---

## 참고자료
1. Margarita — Writing agents should be as easy as writing markdown. (https://www.margarita.run/)
2. margarita · PyPI (https://pypi.org/project/margarita/)
3. MARGARITA - MARGARITA (https://www.banyango.com/margarita/)
4. GitHub - Banyango/margarita: Margarita is a lightweight ... (https://github.com/Banyango/margarita/)
13. Markdown is now a first-class coding language: Deal with it | InfoWorld (https://www.infoworld.com/article/4146579/markdown-is-now-a-first-class-coding-language-deal-with-it.html)