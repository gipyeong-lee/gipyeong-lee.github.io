---
layout: post
title: "AI가 문서를 쓰는 방식이 바뀐다? 텍스트 대신 '웹페이지'로 대화하는 시대"
description: "최근 AI 개발자들 사이에서 AI의 답변을 단순한 텍스트나 마크다운 대신 HTML로 받는 것이 유행하고 있습니다. 앤스로픽 엔지니어가 쏘아 올린 이 흥미로운 변화와 그 이유를 알기 쉽게 설명해 드립니다."
summary: "AI가 작성하는 결과물의 기본 형태가 단순한 텍스트에서 풍부한 시각적 표현이 가능한 HTML로 넘어가면서, 우리가 AI와 소통하는 방식 자체가 더 직관적이고 다채롭게 변화하고 있습니다."
tags: [AI트렌드, 클로드, HTML, 마크다운, 프롬프트엔지니어링]
image: 2026-05-18-Using-Claude-Code-The-unreasonable-effectiveness-of-HTML.jpg
image_alt: "컴퓨터 화면 속에서 단순한 텍스트가 화려하고 인터랙티브한 웹페이지로 변환되는 과정을 묘사한 3D 일러스트"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "인간이 읽기 편한 포맷에서 기계가 최고의 시각적 결과물을 낼 수 있는 포맷으로의 전환은, AI가 단순한 '보조 작가'를 넘어 '독립적인 콘텐츠 생산자'로 진화하고 있음을 보여주는 강력한 신호입니다."
quiz:
  - question: "최근 앤스로픽의 엔지니어 타리크가 AI 에이전트의 기본 출력 형식으로 제안하여 화제가 된 포맷은 무엇인가요?"
    choices: ["마크다운(Markdown)", "파이썬(Python)", "HTML"]
    answer: 2
    explanation: "앤스로픽의 클로드 코드 팀 리드인 타리크 시히파르는 마크다운 대신 HTML을 AI 에이전트의 출력 형식으로 사용할 것을 강력히 옹호했습니다."
  - question: "AI의 결과물을 마크다운 대신 HTML로 받을 때의 주요 장점으로 언급되지 않은 것은 무엇인가요?"
    choices: ["시각적으로 풍부한 다이어그램 표현", "인간이 직접 텍스트를 수정하고 편집하기 쉬움", "양방향 상호작용 기능 포함"]
    answer: 1
    explanation: "HTML은 시각적으로 훌륭하지만, 코드가 복잡하여 오히려 인간이 직접 읽고 편집하면서 AI와 공동 작업(Co-authoring)을 하기에는 마크다운보다 불편하다는 단점이 지적되었습니다."
  - question: "타리크의 에세이가 폭발적인 반응을 얻으며 1위에 오른 개발자 커뮤니티는 어디인가요?"
    choices: ["해커뉴스(Hacker News)", "레딧(Reddit)", "스택오버플로우(Stack Overflow)"]
    answer: 0
    explanation: "타리크의 에세이는 20개의 완결된 HTML 예제를 포함하여 해커뉴스(Hacker News) 최상단에 오르며 큰 토론을 불러일으켰습니다."
lang: ko
ref: 2026-05-18-Using-Claude-Code-The-unreasonable-effectiveness-of-HTML
audio: 2026-05-18-Using-Claude-Code-The-unreasonable-effectiveness-of-HTML.mp3
permalink: /2026/05/18/Using-Claude-Code-The-unreasonable-effectiveness-of-HTML/
---

상상해보세요. 아침에 출근해서 AI 비서에게 "오늘 오후에 있을 신제품 기획 회의 자료를 정리해줘"라고 부탁합니다. 지금까지의 AI는 검은 바탕에 흰 글씨로, 기껏해야 굵은 글씨나 글머리 기호(•) 정도를 섞어서 줄글로 답변을 내놓았습니다. 우리는 그 텍스트를 복사해서 파워포인트나 워드 문서에 옮겨 담은 뒤, 직접 표를 그리고 색깔을 칠하는 귀찮은 후작업을 거쳐야만 했죠. 

그런데 만약, AI가 단순히 글만 써주는 것이 아니라 아예 클릭할 수 있는 버튼, 알록달록한 그래프, 그리고 세련된 레이아웃이 완벽하게 갖춰진 하나의 '웹페이지' 자체를 즉석에서 만들어서 보여준다면 어떨까요? 여러분은 그저 화면을 띄워놓고 바로 회의를 시작하면 됩니다. 

최근 실리콘밸리의 AI 전문가들 사이에서는 바로 이런 방식의 대화법이 뜨거운 감자로 떠올랐습니다. AI의 답변을 단순한 텍스트 포맷이 아니라, 인터넷 웹사이트를 만드는 언어인 'HTML'로 받아내자는 움직임입니다. 도대체 왜 이런 변화가 일어나고 있는 것일까요? 일반인인 우리에게는 이것이 어떤 의미로 다가올까요?

## 이게 왜 중요한가요? (Why It Matters)

그동안 우리가 챗GPT(ChatGPT)나 클로드(Claude) 같은 AI와 대화할 때, AI가 우리에게 답변을 돌려주는 기본 형식은 '마크다운(Markdown)'이라는 것이었습니다. 마크다운은 아주 단순하고 가벼운 텍스트 작성 방식입니다. 앤스로픽(Anthropic)의 클로드(Claude)는 심지어 마크다운 파일 안에 특수문자(ASCII)를 조합해서 조잡하게나마 표나 다이어그램을 그려주는 데에도 꽤 놀라운 능력을 보여주기도 했습니다 [[Using Claude Code: The Unreasonable Effectiveness of HTML](https://www.techtwitter.com/articles/using-claude-code-the-unreasonable-effectiveness-of-html)]. 마크다운은 용량이 가볍고, 어떤 환경에서나 잘 열리며, 무엇보다 사람이 직접 읽고 수정하기가 매우 쉽다는 압도적인 장점 덕분에 AI 에이전트들이 우리와 소통하는 지배적인 파일 형식으로 굳건히 자리 잡았습니다 [[Using Claude Code: The Unreasonable Effectiveness of HTML](https://www.techtwitter.com/articles/using-claude-code-the-unreasonable-effectiveness-of-html)].

하지만 세상이 빠르게 바뀌고 있습니다. AI가 똑똑해지면서, 사람들은 이제 AI에게 단순한 '초안 작성'을 넘어서 '최종 결과물'에 가까운 것을 요구하기 시작했습니다. 

마크다운이 텍스트 중심의 정적인 '서류'라면, HTML은 색상, 이미지, 동적인 움직임까지 모두 담아낼 수 있는 '종합 예술'입니다. 이 작은 형식의 차이가 중요한 이유는, 우리가 AI를 활용하는 방식이 단순한 '글쓰기 도우미'에서 '완성된 애플리케이션 및 콘텐츠 제작자'로 넘어가고 있음을 보여주는 명확한 신호이기 때문입니다. 

HTML을 활용하면 복잡한 데이터 시각화, 양방향으로 조작할 수 있는 인터랙션 기능, 그리고 다른 사람들과 즉시 공유하기 좋은 풍부한 형태의 결과물을 얻을 수 있습니다 [[TheUnreasonableEffectivenessofHTMLinClaudeCode: Why...](https://www.explainx.ai/blog/unreasonable-effectiveness-html-claude-code-thariq-2026)]. 더 이상 AI의 답변을 복사해서 다듬을 필요 없이, 그 자체로 완성된 보고서나 디자인 시안, 혹은 작은 프로그램으로 기능할 수 있게 되는 것입니다. 이는 비단 개발자뿐만 아니라, 코딩을 전혀 모르는 일반인도 자신의 상상력을 눈에 보이는 결과물로 즉시 구현할 수 있는 새로운 시대를 열고 있습니다.

## 쉽게 이해하기 (The Explainer)

이 상황을 조금 더 명확하게 이해하기 위해 비유를 하나 들어보겠습니다.

쉽게 말해서, 마크다운(Markdown)은 사무용 포스트잇이나 줄 노트에 쓴 깔끔한 '메모'와 같습니다. 핵심 내용이 잘 정리되어 있고, 형광펜으로 밑줄을 긋거나(굵은 글씨) 번호를 매기는 정도의 꾸밈은 가능합니다. 누구나 쉽게 알아볼 수 있고, 글씨를 고쳐 쓰기도 편하죠. 하지만 그 메모장 자체를 최종 발표 자료로 쓰기에는 다소 밋밋합니다.

반면에 HTML은 풀 컬러로 인쇄되고 심지어 버튼을 누르면 소리까지 나는 '고급 인터랙티브 잡지'와 같습니다. 화려한 색감과 잘 짜인 구성 덕분에 한눈에 사람들의 시선을 사로잡을 수 있죠.

과거에는 AI의 실력이 조금 어설펐기 때문에, AI가 뼈대(초안 메모)를 잡아주면 인간이 그것을 받아서 예쁘게 포장(잡지로 만들기)하는 작업을 직접 해야 했습니다. 그래서 사람이 읽고 수정하기 편한 '마크다운' 형식이 단연 최고였죠. 하지만 이제 AI 에이전트들이 너무나 똑똑해져서 콘텐츠 창작이라는 무거운 짐을 스스로 다 짊어지게 되었습니다. 인간이 AI의 결과물을 일일이 손으로 편집할 일이 거의 사라진 것입니다 [[UsingClaudeCode:TheUnreasonableEffectivenessofHTML](https://andrey-markin.com/directory/claude-code-html)]. 인간이 굳이 수정할 필요가 없다면, 처음부터 시각적으로 훨씬 다채롭고 풍부한 다이어그램과 색상을 표현할 수 있는 HTML로 결과를 통째로 뽑아내는 것이 훨씬 이득이라는 주장이 나오게 된 배경입니다 [[UsingClaudeCode:TheUnreasonableEffectivenessofHTML](https://andrey-markin.com/directory/claude-code-html)].

또 다른 비유를 들어볼까요? 여러분이 근사한 자동차를 한 대 갖고 싶다고 가정해 봅시다. 
과거에는 AI에게 "최신식 자동차 공장을 짓는 복잡한 설계도(웹 프레임워크 코드)를 짜줘"라고 부탁했습니다. 너무 거창하고 복잡해서 시간도 오래 걸리고 길을 잃기도 쉬웠죠. 그런데 영리한 개발자들은 곧 깨달았습니다. "그냥 지금 당장 도로 위를 달릴 수 있는 굴러가는 자동차(순수 HTML) 한 대만 바로 만들어줘"라고 직설적으로 요구하는 것이 목표에 도달하는 훨씬 빠르고 효율적인 길이라는 것을요 [[ClaudeCodeJust SolvedHTMLin Ways We... | Cynthia Media](https://media.cynthiaconcierge.com/using-claude-code-the-unreasonable-effectiveness-of-html-tool-drop/)].

## 현재 상황 (Where We Stand)

이 흥미로운 논쟁에 불을 지핀 사람은 바로 앤스로픽(Anthropic)에서 '클로드 코드(Claude Code)' 개발팀을 이끌고 있는 엔지니어, 타리크 시히파르(Thariq Shihipar)입니다. 그는 2026년 5월, "클로드의 출력 형식으로 마크다운 대신 HTML을 요구하는 것이 터무니없을 정도로 효과적이다"라는 내용의 도발적이고 매력적인 에세이를 발표했습니다 [[UsingClaudeCode:TheUnreasonableEffectivenessofHTML](https://simonwillison.net/2026/May/8/unreasonable-effectiveness-of-html/)], [[HTMLvs Markdown inClaudeCode: Why Anthropic's Thariq Changed...](https://pasqualepillitteri.it/en/news/2243/html-vs-markdown-claude-code-thariq-anthropic)].

타리크는 최신 AI 에이전트에게 일을 시킬 때, 마크다운의 시대는 저물어가고 있으며 이제 HTML의 시대가 오고 있다고 단언했습니다 [[Anthropic Engineer Sparks Debate: HTML Is the New Markdown ...](https://noqta.tn/en/news/anthropic-thariq-html-over-markdown-ai-outputs-2026)]. 그는 자신의 주장을 뒷받침하기 위해 정보 밀도를 높이고, 상호작용이 가능하며, 기획서나 코드 리뷰, 디자인 프로토타입(시제품) 등 실제 업무 환경에서 HTML이 어떻게 실용적으로 쓰이는지를 보여주는 무려 20개의 완결된 HTML 예제를 함께 공개했습니다 [[TheUnreasonableEffectivenessofHTMLinClaudeCode: Why...](https://www.explainx.ai/blog/unreasonable-effectiveness-html-claude-code-thariq-2026)], [[Anthropic Engineer Sparks Debate: HTML Is the New Markdown ...](https://noqta.tn/en/news/anthropic-thariq-html-over-markdown-ai-outputs-2026)]. 

이 글의 파급력은 실로 어마어마했습니다. 전 세계 최고 수준의 개발자들이 모이는 커뮤니티인 '해커뉴스(Hacker News)'에서 단숨에 1위(Top)를 차지하며, 인간이 AI의 결과물을 소비하는 방식에 대한 거대한 인식의 전환을 일으켰습니다 [[Anthropic Engineer Sparks Debate: HTML Is the New Markdown ...](https://noqta.tn/en/news/anthropic-thariq-html-over-markdown-ai-outputs-2026)]. 트위터(X) 등 소셜 미디어에서도 "더 이상 지루한 마크다운에 머물지 말라"며 명확성과 상호작용성을 극대화할 수 있는 HTML의 장점을 칭송하는 글들이 널리 퍼졌습니다 [[Using Claude Code: The Unreasonable Effectiveness of HTML](https://youmind.com/landing/x-viral-articles/claude-code-html-effectiveness)].

하지만 모두가 이 의견에 두 손 들고 환영하는 것은 아닙니다. 심도 있는 반론도 제기되고 있습니다. 
가장 큰 우려는 인간과 AI의 '공동 작업(Co-authoring)'이 극도로 힘들어질 수 있다는 점입니다 [[Using Claude Code with HTML: Why It Works—and the Co ...](https://ideaverse.ai/blog/using-claude-code-with-html-why-it-works-and-the-co-authoring-tradeoff-moyv58kx)]. 

해커뉴스에서 벌어진 토론을 보면, 한 개발자는 이렇게 고백했습니다. "내가 직접 손으로 복잡한 HTML 표를 짜는 게 마크다운 표를 짜는 것보다 빠를 수는 있습니다. 하지만 그 외의 경우에는, 아무리 AI가 자동화를 해준다고 해도 순수한 HTML 코드를 보면서 글을 읽고 쓰는 흐름(Writing flow)을 매끄럽게 유지하기가 너무 어렵습니다" [[Using Claude Code: The unreasonable effectiveness of HTML ...](https://news.ycombinator.com/item?id=48071940)]. 

즉, 화면에 보이는 결과물이 아름다워지는 대신, 사람이 그 결과물의 뒷면(코드)을 뜯어보고 함께 수정해 나가는 과정은 코드가 너무 복잡해져서 오히려 방해를 받는다는 딜레마가 존재하는 것입니다.

실제로 이 흐름을 주도한 타리크조차도 길고 복잡한 에이전트의 HTML 출력물을 읽기 위해 개발자용 도구인 VIM이나 맥(MacOS)의 훑어보기(Quicklook) 기능을 특수한 확장 프로그램과 연결해서 사용하거나, 어딘가에 붙여넣기를 해야만 제대로 내용을 파악할 수 있다고 언급했습니다 [[UsingClaudeCode:TheunreasonableeffectivenessofHTML](https://modernorange.io/item/48071940)]. 일반인들에게는 여전히 기술적인 진입장벽이 존재하는 셈입니다.

## 앞으로 어떻게 될까? (What's Next)

이러한 장단점에도 불구하고, 개발자와 사용자들은 이미 빠르게 새로운 흐름에 적응하며 진화하고 있습니다. 
커뮤니티에서는 AI가 한 번에 완벽한 HTML을 생성하도록 유도하는 효과적인 프롬프트(명령어) 설정 파일들을 템플릿 형태로 큐레이션하고 공유하는 문화가 활발하게 퍼지고 있습니다 [[ClaudeCodeHTMLPrompts & GPT-5.5 API Cost... - DEV Community](https://dev.to/soytuber/claude-code-html-prompts-gpt-55-api-cost-changes-highlight-developer-focus-3kdg)]. 또한 클로드 코드를 능숙하게 다루기 위한 고급 기능과 작업 흐름을 알려주는 유튜브 튜토리얼 영상들도 쏟아져 나오고 있습니다 [[MasteringClaudeCodein 30 minutes - YouTube](https://www.youtube.com/watch?v=6eBSHbLKuN0)]. 

앞으로는 이 확장성이 텍스트를 넘어 미디어 영역까지 커질 전망입니다. 예를 들어, 코덱스(Codex)나 클로드 코드를 활용해 사용자가 팟캐스트 형태의 오디오 콘텐츠를 바로 생성하고, 이를 세계 최대 음원 플랫폼인 스포티파이(Spotify)로 직접 가져가는(import) 등 결과물의 형태가 웹페이지를 넘어 더욱 다양하고 입체적으로 변모할 것이라는 예측도 나오고 있습니다 [[UsingClaudeCode:TheUnreasonableEffectivenessofHTML](https://aiflow.news/2026/05/08/using-claude-code-the-unreasonable-effectiveness-of-html)].

결과적으로, 일상적인 짧은 대화나 메모를 위해서는 여전히 '마크다운'이 살아남겠지만, 복잡한 보고서, 기획안, 시각 자료가 필요한 업무에서는 'HTML 기반의 결과물'을 요구하는 것이 새로운 상식으로 자리 잡을 가능성이 높습니다. 우리는 이제 AI에게 "글로 설명해줘"라고 말하는 대신, "멋진 웹페이지로 보여줘, 클릭하게 해줘"라고 당당하게 요구하게 될 것입니다.

---

## AI의 시선 (AI's Take)

형식(Format)이 바뀌면 우리의 사고방식도 바뀝니다. AI가 평면적인 텍스트의 좁은 감옥을 벗어나 입체적인 웹 기술(HTML)이라는 날개를 달게 되면서, 이제 우리는 AI를 단순한 '타자기'가 아닌 살아 숨 쉬는 '독립적인 콘텐츠 생산자'이자 무한한 가능성을 지닌 '도화지'로 대해야 할 시점을 맞이했습니다. 

인간이 읽고 수정하기 편한 포맷에서 기계가 최고의 시각적 결과물을 뿜어낼 수 있는 포맷으로의 전환은, AI가 단순한 '보조 작가'를 넘어섰음을 보여주는 강력한 신호입니다. 우리가 던지는 다음 프롬프트는 그저 문장을 만들어내는 데 그치지 않고, 사람들이 직접 만지고 경험할 수 있는 온전한 세계를 창조해 낼 것입니다.

## 참고자료

1. [UsingClaudeCode:TheUnreasonableEffectivenessofHTML](https://simonwillison.net/2026/May/8/unreasonable-effectiveness-of-html/)
2. [TheUnreasonableEffectivenessofHTMLinClaudeCode: Why...](https://www.explainx.ai/blog/unreasonable-effectiveness-html-claude-code-thariq-2026)
3. [UsingClaudeCode:TheUnreasonableEffectivenessofHTML](https://andrey-markin.com/directory/claude-code-html)
4. [ClaudeCodeJust SolvedHTMLin Ways We... | Cynthia Media](https://media.cynthiaconcierge.com/using-claude-code-the-unreasonable-effectiveness-of-html-tool-drop/)
5. [HTMLvs Markdown inClaudeCode: Why Anthropic's Thariq Changed...](https://pasqualepillitteri.it/en/news/2243/html-vs-markdown-claude-code-thariq-anthropic)
6. [ClaudeCodeHTMLPrompts & GPT-5.5 API Cost... - DEV Community](https://dev.to/soytuber/claude-code-html-prompts-gpt-55-api-cost-changes-highlight-developer-focus-3kdg)
7. [UsingClaudeCode:TheunreasonableeffectivenessofHTML](https://modernorange.io/item/48071940)
8. [UsingClaudeCode:TheUnreasonableEffectivenessofHTML](https://aiflow.news/2026/05/08/using-claude-code-the-unreasonable-effectiveness-of-html)
9. [MasteringClaudeCodein 30 minutes - YouTube](https://www.youtube.com/watch?v=6eBSHbLKuN0)
10. [Using Claude Code: The unreasonable effectiveness of HTML ...](https://news.ycombinator.com/item?id=48071940)
11. [Using Claude Code: The Unreasonable Effectiveness of HTML](https://www.techtwitter.com/articles/using-claude-code-the-unreasonable-effectiveness-of-html)
12. [Using Claude Code: The Unreasonable Effectiveness of HTML](https://youmind.com/landing/x-viral-articles/claude-code-html-effectiveness)
13. [Using Claude Code with HTML: Why It Works—and the Co ...](https://ideaverse.ai/blog/using-claude-code-with-html-why-it-works-and-the-co-authoring-tradeoff-moyv58kx)
14. [Anthropic Engineer Sparks Debate: HTML Is the New Markdown ...](https://noqta.tn/en/news/anthropic-thariq-html-over-markdown-ai-outputs-2026)