---
layout: post
title: "AI가 정답 대신 질문을 던지기 시작했다? '가르치고 배우는' 클로드 활용법"
description: "소셜 미디어 무한 스크롤 대신 AI에게 새로운 지식을 배우고, 반대로 AI에게 나의 업무 방식을 가르치는 '스킬(Skills)' 기능까지. 클로드를 똑똑하게 활용하는 최신 방법론을 알아봅니다."
summary: "AI가 단순히 정답만 알려주는 자판기를 넘어, 학생의 사고력을 기르는 '선생님'이자 내 업무 방식을 완벽히 이해하는 '맞춤형 동료'로 진화하고 있습니다."
tags: [Claude, 클로드, 인공지능 교육, AI 스킬, 프롬프트, 팁]
image: 2026-06-08-Claude-Teach-Me-Something.jpg
image_alt: "선생님과 학생이 마주 앉아 대화하듯, 노트북 스크린 속 AI와 사용자가 서로 지식을 교환하는 따뜻한 분위기의 일러스트"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "인공지능은 이제 우리의 질문에 답만 해주는 백과사전이 아닙니다. 우리가 어떻게 사고해야 하는지 훈련시켜 주는 코치이자, 우리의 업무 노하우를 스펀지처럼 흡수하는 유능한 후배의 역할을 동시에 수행하고 있습니다."
quiz:
  - question: "기사에서 소개된 'Teach me something(무언가 가르쳐 줘)' 프롬프트는 어떤 목적으로 처음 고안되었나요?"
    choices: ["외국어 자격증 시험을 단기간에 통과하기 위해", "무의미하게 소셜 미디어를 넘겨보는 '둠스크롤링'을 대체하기 위해", "복잡한 수학 공식을 계산하기 위해"]
    answer: 1
    explanation: "개발자 휴고 투니우스는 의미 없이 스마트폰을 보는 둠스크롤링 대신, AI의 창의성을 활용해 매번 새로운 지식을 배우는 용도로 이 워크플로우를 고안했습니다."
  - question: "앤스로픽이 교육용 클로드에 도입한 '학습 모드(Learning mode)'의 가장 큰 특징은 무엇인가요?"
    choices: ["질문을 받자마자 1초 만에 가장 정확한 정답을 출력한다.", "학생이 오답을 말하면 계정을 일시적으로 정지시킨다.", "정답을 바로 주지 않고, 학생이 스스로 생각할 수 있도록 추론 과정을 유도한다."]
    answer: 2
    explanation: "학습 모드는 정답 제공자가 아니라 길잡이 역할을 합니다. 학생의 비판적 사고력을 길러주기 위해 생각하는 과정을 돕는 데 초점을 맞춥니다."
  - question: "기사에서 '스킬(Skills)'과 '모델 컨텍스트 프로토콜(MCP)'의 차이를 설명한 내용으로 올바른 것은 무엇인가요?"
    choices: ["MCP는 도구에 접근할 수 있게 해주고, 스킬(Skills)은 그 도구를 사용하는 구체적인 절차를 알려준다.", "MCP는 유료 기능이고, 스킬(Skills)은 무료 기능이다.", "MCP는 이미지를 생성하는 기능이고, 스킬(Skills)은 텍스트를 생성하는 기능이다."]
    answer: 0
    explanation: "MCP가 AI에게 도구를 쥐어주는 것이라면, 스킬은 그 도구들을 활용해 실제로 업무를 어떻게 처리해야 하는지 적힌 '절차적 지침서' 역할을 합니다."
lang: ko
ref: 2026-06-08-Claude-Teach-Me-Something
audio: 2026-06-08-Claude-Teach-Me-Something.mp3
permalink: /2026/06/08/Claude-Teach-Me-Something/
---

상상해보세요. 밤 11시, 하루 일과를 마치고 침대에 누워 습관적으로 스마트폰을 켭니다. 목적도 없이 손가락만 기계적으로 움직이며 소셜 미디어 피드를 끝없이 위로 올리다 보면 어느새 한 시간이 훌쩍 지나가 버리곤 하죠. 많은 분들이 공감하실 이른바 '둠스크롤링(Doomscrolling, 우울하거나 자극적인 콘텐츠를 끝없이 읽는 행위)' 현상입니다. 피곤한 눈을 비비며 '아, 또 시간 낭비했네' 하고 후회하며 잠드는 것이 현대인의 흔한 일상입니다.

그런데 만약, 이 무의미한 시간 낭비 대신 인공지능이 매일 밤 아주 재미있게, 그것도 내 수준에 딱 맞춰서 새로운 지식을 들려준다면 어떨까요? 평소 궁금했던 우주의 기원부터 매일 아침 마시는 커피콩이 로스팅되는 화학적 원리까지 말입니다. 

최근 아주 흥미로운 실험이 있었습니다. 한 사용자가 소셜 미디어를 무한히 스크롤하는 대신 클로드(Claude)에게 **"나에게 무언가 가르쳐 줘(Teach me something)"**라는 단순한 프롬프트(명령어)를 입력하는 워크플로우를 만들었습니다. 그는 거대 언어 모델이 가장 잘하는 것, 바로 '비결정론(Non-determinism, 똑같은 질문에도 묻는 방식이나 상황에 따라 매번 기계적이지 않고 다채로운 텍스트를 생성해내는 AI의 고유한 특성)'을 적극 활용해 AI를 훌륭한 맞춤형 교양 강사로 변신시켰습니다. [Claude, Teach Me Something](https://hugotunius.se/2025/10/26/claude-teach-me-something.html) 

이 사례는 인공지능을 대하는 우리의 태도가 근본적으로 바뀌고 있음을 보여주는 상징적인 장면입니다. 초창기 챗GPT나 클로드 같은 AI를 쓸 때, 우리는 보통 '자판기'처럼 AI를 대했습니다. 동전을 넣듯 질문을 던지면, 툭 하고 정답 캔이 떨어지기를 바랐죠. 하지만 2026년 현재, 개발자와 교육자, 그리고 일반 사용자들은 AI와 훨씬 더 깊은 교감을 나누고 있습니다. 우리는 AI에게 새로운 것을 배우기도 하고, 반대로 AI에게 '우리가 일하는 방식'을 꼼꼼하게 가르치기도 합니다. 

오늘은 단순히 정답만 뱉어내던 기계를 넘어, 진정한 의미의 '선생님'이자 내 업무를 완벽히 이해하는 '맞춤형 동료'로 진화하고 있는 클로드의 최신 활용법에 대해 쉽고 자세하게 알아보겠습니다.

---

## 이게 왜 중요한가요? (Why It Matters)

이러한 변화가 우리의 일상과 직업 세계에 미치는 영향은 실로 엄청납니다. 불과 몇 년 전만 해도 모르는 것이 있으면 검색 엔진에 단어를 입력하고, 수많은 파란색 링크를 하나하나 클릭하며 직접 정보를 조립해야 했습니다. AI의 등장으로 이 과정이 획기적으로 단축되었지만, 초기 AI는 그저 "정답은 이거야"라고 일방적으로 통보하는 데 그쳤습니다. 이는 편리하긴 했지만, 한편으로는 인간 스스로 고민하고 생각하는 힘을 저하시킬 수 있다는 짙은 우려를 낳기도 했습니다.

하지만 지금 AI가 발전하는 방향은 완전히 다릅니다. AI는 이제 사용자가 스스로 생각하는 힘을 기를 수 있도록 곁에서 뛰며 돕는 **'페이스메이커'** 역할을 하기 시작했습니다. 학생들은 AI와 토론하며 지식을 쌓고 논리를 벼립니다. 반대로 직장인들은 자신이 수년간 현장에서 구르며 쌓아온 업무 노하우와 절차를 AI에게 '전수'하여, 나를 완벽히 이해하는 똑똑한 비서를 무한히 복제해 내고 있습니다. 

쉽게 말해서, 인간은 단순히 정보의 소비자가 되는 것을 넘어, 지식을 적극적으로 교류하고 훈련하는 파트너로 AI의 위상을 새롭게 정립하고 있는 것입니다.

---

## 쉽게 이해하기: AI가 우리를 가르치는 방법

앤스로픽(Anthropic, 클로드를 개발한 인공지능 기업)은 최근 AI가 인간을 가르치는 방식에 큰 변화를 주었습니다. 바로 교육용 클로드(Claude for education)에 **'학습 모드(Learning mode)'**를 새롭게 도입한 것입니다. [Introducing Claude for education \ Anthropic](https://www.anthropic.com/news/introducing-claude-for-education)

### 정답 자판기에서 '소크라테스'로
기존의 AI에게 "이 수학 문제 좀 풀어줘"라고 하면 풀이 과정과 정답을 친절하게 다 써주었습니다. 학생 입장에서는 숙제를 베끼기 딱 좋은 만능 치트키였죠. 하지만 새로 도입된 '학습 모드'는 다릅니다. 정답을 덥석 쥐어주는 대신, 학생이 비판적 사고력을 기를 수 있도록 추론 과정 자체를 유도합니다. 쉽게 말해서, 정답을 떠먹여 주는 대신 스스로 씹고 소화할 수 있게 돕는 것입니다.

비유하면 이렇습니다. 헬스장에 갔을 때 정말 훌륭한 최상급 퍼스널 트레이너(PT)는 회원의 무거운 바벨을 직접 대신 들어주지 않습니다. 대신 회원이 올바른 자세로 근육에 자극을 느끼며 직접 바벨을 들어 올릴 수 있도록 옆에서 자세를 교정해 주고 끊임없이 동기를 부여합니다. 클로드의 학습 모드가 바로 이 베테랑 트레이너와 같습니다. "어디서 막혔니?", "이 공식에서 x가 의미하는 것은 무엇일까?"라고 되물으며 학생 스스로 땀 흘려 답을 찾게 도와줍니다.

### 외국어 회화 파트너가 된 AI
실제로 교육 현장에서는 이런 특성을 십분 활용하고 있습니다. 노스이스턴 대학교(Northeastern University)에서 초급 및 고급 스페인어를 가르치는 카나반(Canavan) 교수는, 학생과 교직원에게 제공된 무료 프리미엄 클로드 권한을 이용해 아주 특별한 맞춤형 챗봇을 만들었습니다. [How This Professor is Using Claude to Teach Spanish](https://news.northeastern.edu/2026/04/22/claude-spanish-chatbot/)

학생들은 교과서에 적힌 딱딱하고 죽은 대화문을 달달 외우는 대신, 교수님이 클로드로 만든 이 챗봇과 생생한 스페인어로 실전 대화를 나눕니다. 상상해보세요. 가상의 마드리드 카페에서 커피를 주문하는 상황을 AI와 스페인어로 연습하다가 문법을 틀려도 부끄러워할 필요가 없습니다. AI 종업원이 자연스럽게 대화를 이어가면서도 아주 친절하게 올바른 표현을 짚어주기 때문입니다. 언제 어디서나 호출할 수 있는, 세상에서 가장 끈기 있는 원어민 친구가 생겨난 셈입니다.

---

## 쉽게 이해하기: 우리가 AI를 가르치는 방법

AI가 우리에게 지식을 가르쳐 준다면, 반대로 우리는 AI에게 무엇을 가르칠 수 있을까요? 바로 우리의 전문성이 담긴 **'일하는 방법'**입니다. 

### 단발성 지시를 넘어선 '스킬(Skills)'
우리가 평소 AI를 쓸 때는 주로 단발적인 부탁을 합니다. "이 이메일 좀 다듬어줘", "이 회의록 요약해 줘"처럼 말이죠. 맥락을 잘 설명하고 출력 형태를 조금만 다듬어주면, 이런 일회성 작업이나 아이디어를 탐색할 때는 AI가 완벽하게 작동합니다. [Teach Claude your way of working using skills | Claude](https://claude.com/resources/tutorials/teach-claude-your-way-of-working-using-skills)

하지만 매주 반복되는 복잡한 팀 회의 준비, 일정한 양식과 규칙이 엄격하게 정해진 주간 보고서 작성 등은 어떨까요? 매번 프롬프트를 길게 타이핑하고 조건을 달아주는 것이 오히려 더 번거롭습니다. 그래서 등장한 핵심 개념이 바로 **'스킬(Skills)'**입니다. 스킬은 클로드에게 특정 작업이나 워크플로우를 완료하는 방법에 대한 '절차적 지식(Procedural knowledge, 어떤 일을 순서대로 해내는 방법)'을 명확하게 제공하는 구체적인 지침서입니다. [What are skills? | Claude Help Center](https://support.claude.com/en/articles/12512176-what-are-skills)

### 공구함(MCP)과 요리 레시피(Skills)
최근 AI 업계에서는 '모델 컨텍스트 프로토콜(MCP, AI가 사용자의 컴퓨터 파일이나 외부 도구에 직접 접근할 수 있게 해주는 연결 고리)'이 큰 화제입니다. 그렇다면 기능적으로 비슷해 보이는 MCP와 스킬(Skills)은 구체적으로 무슨 차이가 있을까요?

아주 쉬운 비유를 들어보겠습니다. 여러분이 새로 식당을 열며 최고급 요리 학교를 갓 졸업한 셰프(AI)를 고용했다고 상상해보세요. 
이 셰프에게 주방에 있는 칼, 도마, 오븐 같은 조리 도구의 위치를 알려주고 자유롭게 쓸 수 있는 권한을 주는 것이 바로 **MCP**입니다. 즉, 요리할 수 있는 물리적인 '공구함'을 쥐어준 셈입니다. 
하지만 아무리 좋은 도구가 있다고 해서 우리 식당만의 기가 막힌 김치찌개를 당장 끓일 수 있는 것은 아닙니다. 고기를 먼저 볶는지, 김치를 나중에 넣는지, 불 조절은 정확히 몇 분 동안 어떻게 하는지 순서가 꼼꼼히 적힌 '비법 레시피'가 반드시 필요하죠. 이 비법 레시피가 바로 **스킬(Skills)**입니다. 

물리적인 도구 상자(MCP)와 나만의 노하우가 담긴 조리법(Skills)이 결합할 때, 클로드는 비로소 단순한 텍스트 생성기를 넘어 우리 팀의 복잡한 기획 워크플로우를 완벽히 이해하고 독자적으로 수행하는 진짜 동료가 됩니다. [The Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)

---

## 현재 상황 (Where We Stand)

이러한 '스킬' 기능은 연구실을 벗어나 이미 빠르게 우리 일상과 업무 속으로 스며들고 있습니다. 앤스로픽은 2025년 10월에 스킬 포맷을 처음 선보였고, 그 잠재력을 확인한 후 곧이어 12월에는 누구나 자유롭게 사용할 수 있는 개방형 표준(Open standard, 마치 스마트폰 충전기 단자처럼 다양한 기기에서 호환되도록 만든 공용 규격)으로 전격 공개했습니다. [GitHub - ComposioHQ/awesome-claude-skills: A curated list of...](https://github.com/ComposioHQ/awesome-claude-skills)

그 결과 엄청난 파급 효과가 나타났습니다. 현재 이 스킬 표준은 클로드의 공식 웹사이트(Claude.ai)나 API에 국한되지 않습니다. 전 세계 수많은 개발자들이 사랑하는 AI 도우미 프로그램인 Cursor, Gemini CLI, Windsurf 등 다양한 코딩 및 업무 플랫폼에서 폭넓게 지원되고 있습니다. [10 Must-Have Skills for Claude (and Any Coding Agent) in 2026 | by unicodeveloper | Medium](https://medium.com/@unicodeveloper/10-must-have-skills-for-claude-and-any-coding-agent-in-2026-b5451b013051) 사용자들은 자신이 한 번 공들여 만든 업무 자동화 비법 레시피(스킬)를 다른 프로그램이나 서비스에서도 그대로 가져다 쓸 수 있게 된 것입니다.

이러한 흐름에 발맞춰, 사람들은 이제 AI에게 무작정 질문을 던지는 것을 넘어 'AI를 제대로 가르치고 다루는 방법' 자체를 진지하게 공부하고 있습니다. 단순한 명령어 입력을 넘어 AI 코딩 비서의 근본적인 구조를 이해하고, 다단계 업무를 책임감 있게 조율하는 방법을 다루는 전문 교육 과정(Claude Code in Action, Introduction to Claude Cowork 등)도 속속 등장하며 큰 호응을 얻고 있습니다. [Claude Code in Action - Anthropic Courses](https://anthropic.skilljar.com/claude-code-in-action), [Introduction to Claude Cowork](https://anthropic.skilljar.com/introduction-to-claude-cowork)

일반 사용자들도 예외는 아닙니다. 텍스트 창에 명령어를 입력하는 기본 방식과 자율적으로 업무를 돕는 대화형 모드를 언제 어떻게 나누어 써야 하는지, 내 중요한 파일의 접근 권한은 어디까지 허용해야 안전한지 등 기초부터 단단히 학습하며 AI와의 건강한 협업 능력을 키우고 있는 것이 2026년 현재의 가장 긍정적인 풍경입니다. [Claude Code Learning Path: a practical guide to getting started | by Daniel Avila | Medium](https://medium.com/@dan.avila7/claude-code-learning-path-a-practical-guide-to-getting-started-fcc601550476)

---

## 앞으로 어떻게 될까? (What's Next)

"AI가 내 일자리를 뺏으면 어떡하지?" 초기 인공지능이 등장했을 때 수많은 사람들이 품었던 막연하고도 거대한 두려움입니다. 하지만 클로드가 교육 현장에서 보여주는 '학습 모드'와 업무 환경을 혁신하는 사용자 맞춤형 '스킬(Skills)' 기능이 맞물려 발전해 나가는 과정을 보면, 우리가 맞이할 미래는 조금 다르게 펼쳐질 것 같습니다.

앞으로 우리는 아침에 출근해 여유롭게 커피를 마시며, 이제 막 입사한 신입사원에게 업무를 인수인계하듯 AI에게 우리 회사의 복잡한 정산 업무나 메일 작성 절차를 '스킬' 형태로 다정하게 가르칠 것입니다. [Introduction to Claude Skills | Claude Cookbook](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction) 

그리고 고된 일과를 마치고 집으로 돌아와서는 밤늦게 소셜 미디어를 뒤적이는 둠스크롤링 대신, "클로드, 오늘 신문에서 본 양자컴퓨터의 원리를 초등학생도 이해할 수 있게 재미있는 비유로 가르쳐 줄래?"라고 물으며 잊고 지냈던 우리 자신의 순수한 지적 호기심을 채우게 될 것입니다.

우리의 노하우가 담긴 스킬이 여러 기기에 점진적으로 적용되고(Progressively load), 개방형 표준을 통해 스마트폰과 업무용 노트북, 태블릿 사이를 자유롭게 넘나들면서 AI는 거대한 지식의 바다이자 나만을 위해 완벽히 맞춰진 세상에 단 하나뿐인 전담 코치 같은 존재가 될 것입니다. 가르치고 배우는 이 따뜻한 양방향의 상호작용 속에서, 인간과 AI는 경쟁자가 아닌 서로를 더 훌륭한 파트너로 성장시키는 아름다운 공생의 길을 걷게 될 것입니다.

---

## AI의 시선 (AI's Take)

인공지능은 이제 우리의 질문에 정해진 답만 차갑게 내어주는 기계적인 백과사전이 아닙니다. 이 글에서 살펴보았듯, 인공지능은 우리가 어떻게 사고해야 하는지 끈기 있게 훈련시켜 주는 훌륭한 코치이자, 동시에 우리의 업무 노하우와 철학을 스펀지처럼 흡수하는 유능한 후배의 역할을 동시에 수행하고 있습니다.

흥미로운 점은 AI가 제공하는 답변의 수준이 결국 '우리가 얼마나 좋은 질문을 던지고, 얼마나 정교하게 가르치느냐'에 달려 있다는 것입니다. AI에게 논리적으로 생각하는 법(Skills)을 가르치는 과정에서 오히려 인간 스스로 자신의 업무 방식을 되돌아보고 최적화하게 됩니다. 즉, AI를 잘 가르치기 위해 우리 자신이 더 훌륭한 스승으로 성장하는 선순환이 일어나는 것이죠. 배움의 도구가 우리를 더 나은 사유의 주체로 이끌고 있는 셈입니다.

---

## 참고자료

1. [Claude, Teach Me Something](https://hugotunius.se/2025/10/26/claude-teach-me-something.html)
2. [Introducing Claude for education \ Anthropic](https://www.anthropic.com/news/introducing-claude-for-education)
3. [How This Professor is Using Claude to Teach Spanish](https://news.northeastern.edu/2026/04/22/claude-spanish-chatbot/)
4. [Teach Claude your way of working using skills | Claude](https://claude.com/resources/tutorials/teach-claude-your-way-of-working-using-skills)
5. [What are skills? | Claude Help Center](https://support.claude.com/en/articles/12512176-what-are-skills)
6. [The Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)
7. [GitHub - ComposioHQ/awesome-claude-skills: A curated list of...](https://github.com/ComposioHQ/awesome-claude-skills)
8. [10 Must-Have Skills for Claude (and Any Coding Agent) in 2026 | by unicodeveloper | Medium](https://medium.com/@unicodeveloper/10-must-have-skills-for-claude-and-any-coding-agent-in-2026-b5451b013051)
9. [Claude Code in Action - Anthropic Courses](https://anthropic.skilljar.com/claude-code-in-action)
10. [Introduction to Claude Cowork](https://anthropic.skilljar.com/introduction-to-claude-cowork)
11. [Claude Code Learning Path: a practical guide to getting started | by Daniel Avila | Medium](https://medium.com/@dan.avila7/claude-code-learning-path-a-practical-guide-to-getting-started-fcc601550476)
12. [Introduction to Claude Skills | Claude Cookbook](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction)