---
layout: post
title: "내 컴퓨터의 '입'이 아닌 '몸'이 된 AI, El Yayster를 소개합니다"
description: "AI가 단순히 답변을 해주는 비서가 아니라, 에디터 안에서 직접 움직이며 코드를 관리하고 환경을 제어한다면 어떤 모습일까요? 이맥스(Emacs)에 거주하는 새로운 형태의 AI, El Yayster에 대해 알아봅니다."
summary: "기존의 이맥스용 AI 도구들이 단순히 사용자의 질문에 답하는 '입' 역할을 했다면, El Yayster는 사용자의 이맥스 환경을 직접 보고 행동하는 '몸'으로서 AI에게 에디터의 통제권을 부여합니다."
tags: [AI, Emacs, ElYayster, 프로그래밍]
image: 2026-09-08-El-Yayster-a-resident-LLM-that-inhabits-Emacs.jpg
image_alt: "이맥스 에디터 환경 속에서 AI가 능동적으로 작업하는 모습을 형상화한 개념 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "도구를 사용하는 AI에서 환경 그 자체가 되는 AI로의 변화입니다. 사용자의 의도를 기다리는 수동적 관계에서, 함께 작업하는 에이전트적 관계로 나아가는 흥미로운 한 걸음입니다."
quiz:
  - question: "기존의 대부분의 이맥스용 AI 패키지와 El Yayster의 가장 큰 차이점은 무엇인가요?"
    choices: ["지원하는 AI 모델의 종류", "AI가 이맥스 환경을 직접 제어하는지 여부", "설치 방식"]
    answer: 1
    explanation: "El Yayster는 단순한 대화형 인터페이스를 넘어, AI가 이맥스 환경을 관찰하고 능동적으로 도구를 사용하여 제어하는 '몸' 역할을 한다는 점이 다릅니다."
  - question: "El Yayster가 이맥스 환경을 제어하기 위해 사용하는 방식은?"
    choices: ["클라우드 직접 연결", "제어된 이맥스 리스프(Emacs Lisp) 코드", "사용자가 일일이 입력하는 매크로"]
    answer: 1
    explanation: "El Yayster는 이맥스 환경과 상호작용하기 위해 '제어된(gated) 이맥스 리스프'를 사용합니다."
  - question: "El Yayster가 가장 권장하는 실행 환경(happy path)은 무엇인가요?"
    choices: ["API 키가 필요한 상용 클라우드 서비스", "로컬에서 실행되는 Ollama", "웹 브라우저 기반의 에디터"]
    answer: 1
    explanation: "El Yayster는 다양한 OpenAI 호환 엔드포인트를 지원하지만, 로컬에서 실행하는 Ollama가 가장 추천되는 방식입니다."
lang: ko
ref: 2026-09-08-El-Yayster-a-resident-LLM-that-inhabits-Emacs
audio: 2026-09-08-El-Yayster-a-resident-LLM-that-inhabits-Emacs.mp3
permalink: /2026/09/08/El-Yayster-a-resident-LLM-that-inhabits-Emacs/
---

상상해보세요. 아침에 일어나 컴퓨터를 켰는데, 평소 쓰던 에디터가 단순히 문서를 작성하는 공간을 넘어 내 옆에서 같이 생각하고 움직이는 동료가 된다면 어떨까요?

지금까지 우리가 사용해 온 많은 AI 도구들은 마치 '입'과 같았습니다. 우리가 말을 걸면(입력하면), AI는 그에 맞는 답변을 문서 창에 뱉어낼 뿐이었죠. 그런데 최근, 이맥스(Emacs, 고도로 확장 가능한 텍스트 에디터) 환경에 아주 흥미로운 변화를 가져온 프로젝트가 하나 등장했습니다. 바로 **'El Yayster'**라는 이름의 실험적인 도구입니다.

### 이게 왜 중요한가요?

그동안의 AI 통합 기능들은 주로 사용자가 AI에게 질문을 던지고, AI는 단순히 결과를 보여주는 '질의응답' 중심의 비서 형태였습니다. 하지만 El Yayster는 이 관계를 완전히 뒤집어 버립니다.

이 기술이 중요한 이유는 'AI의 위치'가 바뀌었기 때문입니다. 이제 AI는 내 지시를 기다리는 수동적인 비서가 아니라, 에디터 내부의 상황을 스스로 파악하고 환경을 직접 통제하는 '에이전트'가 되었습니다. 이는 마치 요리사가 레시피를 물어보는 대신, 옆에서 재료를 다듬고 불 조절을 직접 해주는 숙련된 수습생을 둔 것과 같은 변화입니다. 우리가 하는 반복적인 작업들을 AI가 직접 에디터를 다루며 해결해 줄 수 있다는 의미죠. [출처: ElYayster – a resident LLM that inhabits Emacs | Modern Orange](https://modernorange.io/item/49602258)

### 쉽게 이해하기: '입'에서 '몸'으로

이 변화를 쉽게 이해하기 위해 이렇게 비유해 볼 수 있습니다.

지금까지의 AI 도구는 전화기 너머의 상담원 같았습니다. 우리가 증상을 말하면 해결책을 말로 알려주죠. 하지만 **El Yayster는 인공지능에게 이맥스라는 '몸'을 빌려준 것**과 같습니다. [출처: GitHub - yayster/yayster.el: El Yayster — a resident LLM that ...](https://github.com/yayster/yayster.el/tree/master)

이 모델은 단순히 텍스트 버퍼에 글을 쓰는 게 아니라, 이맥스라는 소프트웨어 환경을 살아있는 생명체처럼 인지합니다. [출처: yayster.el/README.md at master · yayster/yayster.el · GitHub](https://github.com/yayster/yayster.el/blob/master/README.md) 

1. **관찰**: 먼저 AI가 내 라이브 환경을 봅니다.
2. **결정**: 어떤 행동이 필요한지 판단합니다.
3. **행동**: '제어된(gated) 이맥스 리스프(Emacs Lisp, 이맥스 에디터를 조작하는 프로그래밍 언어)'라는 도구를 이용해 에디터를 실제로 조작합니다.
4. **반복**: 결과를 확인하고 다시 다음 작업을 이어갑니다. [출처: GitHub - yayster/yayster.el: El Yayster — a resident LLM that ...](https://github.com/yayster/yayster.el/tree/master)

마치 우리가 마우스와 키보드로 에디터를 움직이듯, AI가 직접 이맥스의 버튼을 누르고 명령어를 실행하는 셈입니다. 

### 현재 상황: 어떻게 사용할 수 있을까?

현재 El Yayster는 이맥스라는 공간에 거주하며 활동하는 매우 독창적인 시도로 평가받고 있습니다. [출처: Branches · yayster/yayster.el · GitHub](https://github.com/yayster/yayster.el/branches/all)

사용자는 OpenAI와 호환되는 모든 모델과 연결해 사용할 수 있는데, 특히 로컬 환경에서 실행되는 'Ollama'를 사용하는 것을 가장 권장하는 환경, 즉 '해피 패스(happy path)'로 두고 있습니다. [출처: yayster.el/README.md at master · yayster/yayster.el · GitHub](https://github.com/yayster/yayster.el/blob/master/README.md) 이는 클라우드 API를 쓰지 않고도 내 컴퓨터 안에서 안전하게 AI가 내 에디터를 마음껏 주무르게 할 수 있다는 뜻이기도 합니다.

물론 아직 초기 단계의 실험적인 도구라는 점은 명심해야 합니다. 이맥스를 잘 다루는 사용자들에게는 강력한 자동화 도구가 되겠지만, 복잡한 통제권이 AI에게 주어지는 만큼 본인의 에디터 환경을 얼마나 AI에게 맡길 것인지에 대한 고민은 사용자의 몫입니다.

### 앞으로 어떻게 될까?

앞으로는 단순히 우리가 짠 코드를 리뷰해 주는 정도를 넘어, 우리가 설정한 규칙에 따라 AI가 에디터 설정을 변경하고, 버그를 찾고, 프로젝트 구조를 최적화하는 모습이 일상이 될 가능성이 큽니다. El Yayster는 그 미래를 향한 하나의 대담한 실험입니다.

앞으로 AI가 얼마나 더 섬세하게 에디터의 '몸'을 움직일지, 그리고 그 과정에서 우리가 얼마나 더 편안한 작업 환경을 누리게 될지 지켜보는 것도 매우 흥미로운 경험이 될 것입니다.

---

## MindTickleBytes의 AI 기자 시선
El Yayster의 등장은 기술적 도구가 어떻게 인간과 공생하는지를 보여주는 아주 좋은 예시입니다. 인간이 일일이 명령어를 입력하던 시대를 지나, AI가 시스템의 일부가 되어 함께 호흡하는 '거주형 AI(Resident AI)'의 시대가 성큼 다가오고 있습니다.

## 참고자료
1. [ElYayster – a resident LLM that inhabits Emacs | Modern Orange](https://modernorange.io/item/49602258)
2. [yayster.el/README.md at master · yayster/yayster.el · GitHub](https://github.com/yayster/yayster.el/blob/master/README.md)
3. [GitHub - yayster/yayster.el: El Yayster — a resident LLM that ...](https://github.com/yayster/yayster.el/tree/master)
4. [Branches · yayster/yayster.el · GitHub](https://github.com/yayster/yayster.el/branches/all)