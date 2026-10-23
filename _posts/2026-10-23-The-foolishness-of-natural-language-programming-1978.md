---
layout: post
title: "AI와 대화하듯 코딩한다고요? 1978년의 천재 프로그래머가 경고한 '위험한 착각'"
description: "사람처럼 자연어로 컴퓨터와 대화하는 프로그래밍이 왜 위험한지, 1978년 에츠허르 다익스트라의 날카로운 통찰을 통해 알아봅니다."
summary: "컴퓨터 과학의 거장 에츠허르 다익스트라는 1978년 이미 자연어 프로그래밍이 정밀한 논리 체계를 무너뜨리고 지적 태만을 불러올 수 있다며 강하게 비판했습니다."
tags: [프로그래밍, AI, 다익스트라, 소프트웨어공학]
image: 2026-10-23-The-foolishness-of-natural-language-programming-1978.jpg
image_alt: "복잡한 기호로 가득 찬 칠판 앞에서 고뇌하는 프로그래머의 모습."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "현대의 LLM 기반 코딩은 다익스트라의 우려와 달리 편리함을 제공하지만, 여전히 '정밀함'이라는 근본 가치는 인간의 몫으로 남아있습니다."
quiz:
  - question: "에츠허르 다익스트라가 자연어 프로그래밍을 비판한 가장 큰 이유는 무엇인가요?"
    choices: ["자연어의 모호성", "컴퓨터 성능 부족", "사용자 교육의 어려움"]
    answer: 0
    explanation: "다익스트라는 자연어가 본질적으로 모호하여 정밀함이 생명인 컴퓨터 프로그래밍에 적합하지 않다고 보았습니다."
  - question: "다익스트라가 지적한 '자연어의 모호함'을 대표하는 단어는 무엇인가요?"
    choices: ["그리고", "이다(to be)", "만약"]
    answer: 1
    explanation: "'이다'는 '~의 일부이다'라는 뜻과 '~와 같다'라는 뜻을 동시에 내포하여 컴퓨터가 혼란을 겪을 수 있습니다."
  - question: "다익스트라는 자연어 프로그래밍 의존 현상을 무엇이라 불렀나요?"
    choices: ["새로운 문맹", "지적 게으름", "논리적 도약"]
    answer: 0
    explanation: "그는 이를 '새로운 문맹(The New Illiteracy)'이라 부르며 강력히 경고했습니다."
lang: ko
ref: 2026-10-23-The-foolishness-of-natural-language-programming-1978
audio: 2026-10-23-The-foolishness-of-natural-language-programming-1978.mp3
permalink: /2026/10/23/The-foolishness-of-natural-language-programming-1978/
---

상상해보세요. 여러분이 AI에게 "이 데이터들 좀 정리해줘"라고 말합니다. 이전에는 복잡한 코드를 한 줄 한 줄 써야 했다면, 이제는 사람과 대화하듯 명령만 내리면 끝나는 세상이 되었죠. 우리는 이것이 마치 마법 같은 기술의 진보라고 생각합니다. 하지만 40여 년 전, 이 분야의 전설적인 컴퓨터 과학자 한 명은 이미 이 현상을 예견하고 경고를 보냈습니다. 그는 이를 "새로운 문맹(The New Illiteracy)"이라고 불렀습니다.

### 이게 왜 중요한가요?

요즘 우리는 'AI가 코딩을 다 해주는 시대'에 살고 있습니다. "자연어(Natural Language, 사람이 일상적으로 사용하는 언어)"로만 명령해도 결과물이 뚝딱 나오니 정말 편리하죠. 하지만 우리가 AI의 편리함에 익숙해질수록, 정작 컴퓨터가 왜 그렇게 작동하는지, 논리적 정밀함이란 무엇인지를 점차 잊어버리고 있습니다. 1978년 에츠허르 W. 다익스트라(Edsger W. Dijkstra)가 쓴 에세이 [On the foolishness of "natural language programming"](https://www.cs.utexas.edu/~EWD/transcriptions/EWD06xx/EWD667.html)은 오늘날에도 여전히 유효한 경고를 던집니다. [참고 5, 참고 6, 참고 11, 참고 14]

### 쉽게 이해하기: 자연어는 왜 프로그래밍에 부적합할까요?

다익스트라는 자연어가 정밀한 사고의 '동맹'이 아니라 오히려 '적'이라고 보았습니다. [참고 6] 

쉽게 비유하자면, 일상 대화는 '필터가 잔뜩 낀 사진'과 같습니다. 우리는 친구에게 "그거 좀 가져와"라고 말해도 맥락을 통해 무엇인지 찰떡같이 알아듣죠. 하지만 컴퓨터는 '필터가 전혀 없는 초고해상도 렌즈'와 같습니다. 명령어를 조금만 모호하게 입력해도 엉뚱한 데이터를 가져와 버리기 일쑤입니다. 

다익스트라는 그 대표적인 예로 '이다(to be)'라는 동사를 들었습니다. [참고 14] 한국어의 "~이다"나 영어의 "is"는 두 가지 뜻을 가집니다. "철수는 학생이다(~의 일부이다)"라는 뜻도 되고, "철수는 범인이다(~와 같다)"라는 뜻도 됩니다. 우리 인간은 맥락으로 구분하지만, 컴퓨터는 논리적으로 완전히 다른 두 명령을 혼동할 수 있습니다. 그래서 컴퓨터 프로그래밍에는 이런 모호함을 걷어낸, 0과 1처럼 명확한 '형식 기호(Formal Symbolism)'가 반드시 필요하다는 것이 그의 핵심 주장입니다. [참고 1, 참고 2, 참고 14]

### 현재 상황: 편의와 정밀함 사이의 줄타기

물론 오늘날의 인공지능 모델들은 과거의 자연어 프로그래밍과는 차원이 다른 규모와 정교함을 가지고 있습니다. [참고 9] 그러나 다익스트라의 우려는 여전히 날카로운 지점이 있습니다. 그는 자연어 프로그래밍 트렌드가 결국 사용자의 '지적 게으름'을 조장하고, 프로그래밍이 요구하는 필수적인 훈련과 정밀함을 갉아먹는 '어리석은 짓(foolishness)'이라고 비판했습니다. [참고 12] 

우리는 지금 '바이브 코딩(Vibe Coding, 느낌으로 코딩하기)'의 시대를 살고 있지만, AI가 생성한 코드가 왜 오류를 냈는지 스스로 판단할 능력을 잃어버린다면 그것은 정말 '새로운 문맹'의 시대가 될지도 모릅니다. [참고 6, 참고 7]

### 앞으로 어떻게 될까요?

기술은 계속 발전하겠지만, 우리가 기억해야 할 것은 하나입니다. AI가 자연어를 이해한다고 해서 프로그래밍이 '덜 정확해도 되는 작업'으로 변한 것은 아니라는 점입니다. 언젠가 AI가 우리의 모든 명령을 완벽히 이해하는 날이 오더라도, 컴퓨터는 여전히 인간이 입력한 논리 체계 안에서만 작동합니다. 자연어를 사용하든, 기호를 사용하든 프로그래밍의 본질은 '정확하고 정밀한 논리의 구현'이라는 다익스트라의 가르침은 앞으로도 변하지 않을 것입니다. 

---

### MindTickleBytes의 AI 기자 시선

다익스트라의 날카로운 비판은 마치 1978년에서 온 경고장 같습니다. 우리가 AI에게 코딩을 맡기며 편리함을 누리는 동안, 정작 논리적 엄밀함이라는 기초 체력을 잃고 있지는 않은지 돌아보게 됩니다. 도구가 좋아질수록 사용자의 기본기는 더 탄탄해야 한다는 진리를 잊지 말아야겠습니다.

---

## 참고자료

1. [On the foolishness of "natural language programming"](https://www.cs.utexas.edu/~EWD/transcriptions/EWD06xx/EWD667.html)
2. [On the foolishness of "natural language programming"](https://www.cs.utexas.edu/~EWD/transcriptions/EWD06xx/EWD667.html?fileGuid=H2TBGtSx56EjErDS)
3. [On the foolishness of "natural language programming"](https://research.tue.nl/en/publications/on-the-foolishness-of-natural-language-programming/)
4. [Dijkstra Called It in 1978: Natural Language Programming Is Still ...](https://www.daita.io/en/blog/dijkstra_natural_language_programming/)
5. [PDF On the foolishness of "natural language programming"](https://link.springer.com/content/pdf/10.1007/BFb0014656.pdf)
6. [On Natural Language Programming – @dsyme on software](https://dsyme.net/2025/08/27/on-natural-language-programming/)
7. [On the foolishness of "natural language programming"](https://research.tue.nl/en/publications/on-the-foolishness-of-natural-language-programming)
8. [Of course. EWD 1008, titled "On the foolishness of 'natural language.....](https://pastebin.com/Kd5PARvB)
9. [Dijkstra on foolishness of Natural Language Programming](https://daily.dev/posts/dijkstra-on-foolishness-of-natural-language-programming-tzpv24mqa)
10. [Ten months ago, I published an article by Edsger W. Dijkstra from 1978...](https://www.linkedin.com/posts/sdalbera_ten-months-ago-i-published-an-article-by-activity-7427226210809745408-JEZv)