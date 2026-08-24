---
layout: post
title: "AI가 논문을 읽고 '요약'해준다고? 진짜 이해하는 걸까? CMake만으로 구현해본 GPT-2"
description: "AI의 내부 구조가 궁금하다면? 복잡한 라이브러리 없이 순수 CMake 언어만으로 GPT-2를 구현한 흥미로운 실험을 소개합니다."
summary: "복잡한 AI 라이브러리 없이, 프로그래밍 빌드 도구인 CMake만으로 GPT-2 모델을 밑바닥부터 구현해 보려는 개발자들의 이색적인 도전을 다룹니다."
tags: [AI, GPT-2, 프로그래밍, CMake, 인공지능]
image: 2026-08-24-Implementation-of-GPT-2-in-pure-CMake.jpg
image_alt: "복잡한 코드 구조가 CMake 빌드 도구를 통해 표현된 개념적인 디지털 그래픽."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "이런 도전은 실용성보다는 '이해'에 방점이 있습니다. 겉으로 드러나는 인터페이스를 걷어내면 AI의 본질이 무엇인지 비로소 보이게 되죠."
quiz:
  - question: "본문에서 언급된 CMake로 GPT-2를 구현하는 시도의 주된 목적은 무엇일까요?"
    choices: ["최고 성능의 모델 생성", "실제 상용 서비스 배포", "AI 내부 구조의 교육적 이해"]
    answer: 2
    explanation: "이런 구현은 AI 모델이 내부적으로 어떻게 작동하는지 밑바닥부터 탐구해보는 교육적인 목적이 큽니다."
  - question: "안드레이 카파시(Andrej Karpathy)가 선보인 'llm.c' 프로젝트의 특징은 무엇인가요?"
    choices: ["PyTorch 기반 학습", "순수 C 언어로 약 1,000줄 내외 구현", "웹 브라우저 전용 모델"]
    answer: 1
    explanation: "llm.c는 PyTorch와 같은 복잡한 외부 의존성 없이 순수 C 언어만을 사용하여 GPT-2를 약 1,000줄의 코드로 구현했습니다."
  - question: "CMake는 본래 어떤 목적으로 사용되는 도구인가요?"
    choices: ["AI 모델 학습 전용 라이브러리", "소프트웨어 빌드 자동화 도구", "언어 모델 토큰화 도구"]
    answer: 1
    explanation: "CMake는 여러 플랫폼에서 소프트웨어를 빌드하고 관리하기 위한 자동화 도구입니다."
lang: ko
ref: 2026-08-24-Implementation-of-GPT-2-in-pure-CMake
audio: 2026-08-24-Implementation-of-GPT-2-in-pure-CMake.mp3
permalink: /2026/08/24/Implementation-of-GPT-2-in-pure-CMake/
---

상상해보세요. 오늘날 우리가 스마트폰에서 사용하는 AI 비서가 어떻게 문장을 만드는지, 그 '두뇌'를 우리가 직접 뜯어볼 수 있다면 어떨까요? 보통 사람들에게 AI는 '마법'처럼 느껴집니다. 버튼을 누르면 답이 튀어나오는 검은 상자 같죠. 하지만 개발자들은 이 상자를 열어보고 싶어 합니다. 

최근에는 단순히 열어보는 것을 넘어, 이 거대한 AI의 구조를 아주 기초적인 도구들만 가지고 처음부터 다시 쌓아 올리는 이색적인 실험들이 유행하고 있습니다. 심지어는 소프트웨어의 빌드 도구인 CMake(프로그램을 빌드하기 위한 자동화 도구)만으로 GPT-2라는 인공지능 모델을 구현하려는 시도까지 등장했습니다. [Source 8, Source 11, Source 12]

## 이게 왜 중요한가요?

왜 다들 바쁜 시간에 이런 '고생'을 자처하는 걸까요? 이는 마치 조립된 레고 블록이 아니라, 나무를 깎고 직접 흙을 빚어 성을 쌓는 것과 같습니다. 오늘날 대부분의 AI 개발은 파이토치(PyTorch, AI 개발을 위한 복잡한 라이브러리) 같은 거대하고 편리한 도구 위에서 이루어집니다. 하지만 이 도구들은 너무 편리해서, 정작 AI가 데이터 속에서 수학적으로 어떤 계산을 수행하는지 그 핵심 과정을 가려버리곤 합니다. 

이러한 '밑바닥부터 구현하기(From scratch)' 실험들은 AI 개발의 진입 장벽을 낮추고, 일반 개발자들이 AI의 작동 원리를 근본적으로 이해할 수 있게 돕습니다. [Source 10, Source 13] 우리가 직접 모델을 만들어본다면, AI가 왜 특정한 답을 내놓는지 그 논리적인 경로를 훨씬 더 깊이 있게 파악할 수 있게 됩니다.

## 쉽게 이해하기: AI의 '두뇌' 빌드하기

쉽게 말해서, 현재의 AI 모델은 수많은 '가중치(Weight, 데이터를 처리할 때 곱해지는 숫자값)'들의 거대한 집합입니다. 이 가중치들이 복잡하게 연결되어 문장을 완성합니다. 이를 이해하기 위해 비유를 들자면, AI는 수만 개의 수도꼭지가 연결된 복잡한 배관 시스템과 같습니다. 어떤 수도꼭지를 얼마나 여느냐(가중치를 조절하느냐)에 따라 흘러나오는 물의 양과 방향(결과값)이 달라지는 것이죠.

안드레이 카파시(Andrej Karpathy, 오픈AI 출신 AI 과학자)는 'llm.c'라는 프로젝트를 통해 이 거대한 AI를 순수 C 언어만으로 약 1,000줄의 코드에 담아내는 놀라운 실험을 보여주었습니다. [Source 2, Source 3, Source 17, Source 18] 원래라면 수십만 줄이 넘는 외부 라이브러리들의 도움을 받아야 했던 일을, 마치 '다이어트'를 하듯 꼭 필요한 코드만 남겨 핵심 구조만 보여준 것입니다.

여기서 등장한 CMake 구현은 이 실험을 한 단계 더 나아간 케이스입니다. [Source 8, Source 11] 보통 프로그램을 실행 파일로 만들기 위해 사용하는 관리 도구인 CMake를 활용하여 AI의 계산 논리를 짜 넣은 것입니다. 이는 마치 집을 짓기 위한 '설계도'를 가지고 직접 '벽돌'을 만드는 것과 같은, 개발자들 사이에서는 일종의 '기술적 유희'이자 '한계에 대한 도전'으로 받아들여지고 있습니다. [Source 9]

## 현재 상황: 어디까지 왔을까?

물론, 이러한 실험적인 구현들이 지금 당장 ChatGPT를 대신할 수는 없습니다. 특히 CMake로 구현된 모델의 경우, 프로그램이 돌아가는 속도가 아주 느릴 수밖에 없습니다. CMake는 본래 인터프리터(한 줄씩 코드를 해석하는 방식)처럼 작동하며, 숫자를 처리하는 과정에서 매번 문자열로 변환하는 등의 비효율적인 과정이 반복되기 때문입니다. [Source 12]

그럼에도 불구하고, 이런 시도들은 매우 가치 있습니다. 오픈AI의 GPT-2 모델 역시 그 견고함이나 최악의 상황에서의 행동 등이 완전히 이해되지 않은 측면이 있습니다. [Source 4] 따라서 이러한 '클린 룸' 방식의 구현(외부 라이브러리 없이 처음부터 새로 만드는 방식)은 AI의 내부 구조를 하나씩 뜯어보며 학습하기에 가장 완벽한 교과서가 되어줍니다. [Source 10, Source 13]

## 앞으로 어떻게 될까?

앞으로 AI 기술은 점점 더 대중화될 것입니다. 지금은 극소수의 엔지니어만이 AI를 구현할 수 있지만, 'llm.c'나 'microgpt'와 같이 265줄 내외의 코드로 원리를 설명해주는 프로젝트들이 늘어날수록, AI 기술은 더욱 투명해질 것입니다. [Source 16, Source 17] 

머지않아 우리는 AI가 어떻게 작동하는지 수학적인 원리부터 코드 단위까지 손쉽게 확인할 수 있는 시대에 살게 될지도 모릅니다. 다음에 AI가 회의 자료를 요약해준다면, 이제는 그저 신기해하기보다, "아, 저 거대한 모델의 핵심이 이 코드 한 줄에서 시작되었구나"라고 한 번쯤 상상해보는 건 어떨까요?

## MindTickleBytes의 AI 기자 시선
복잡한 기술의 껍데기를 벗겨내고 나면 남는 것은 결국 단순한 수학과 논리입니다. 기술이 발전할수록 오히려 그 '본질'을 탐구하려는 이러한 시도들이, AI 시대를 사는 우리에게 필요한 진짜 문해력을 길러줄 것입니다.

## 참고자료
1. [Vue HN 2.0 | Implementation of GPT-2 in pure CMake](https://vue-hackernews-ssr-5cavbdjcta-ew.a.run.app/item/49412909)
2. [Andrej Karpathy Trains GPT-2 in Pure C Without PyTorch](https://analyticsindiamag.com/ai-news-updates/andrej-karpathy-trains-gpt-2-in-pure-c-without-pytorch/)
3. [Why Implement GPT-2 in Pure C Language? Karpathy Responds to Online Criticism - Boardor](https://boardor.com/blog/why-implement-gpt-2-in-pure-c-language-karpathy-responds-to-online-criticism)
4. [GitHub - openai/gpt-2: Code for the paper "Language Models are..."](https://github.com/openai/gpt-2)
5. [Need help with implementing gpt-2 from scratch - Deep Learning...](https://forums.fast.ai/t/need-help-with-implementing-gpt-2-from-scratch/62189)
6. [project — CMake 4.4.2 Documentation](https://cmake.org/cmake/help/latest/command/project.html)
7. [Free GPT Image 2 AI Image Generator & Editor (No Signup, Unlimited)](https://imagegpt2.com/)
8. [Implementation of GPT-2 in pure CMake - GitHub](https://github.com/AlpinDale/gpt2.cmake)
9. [The Ultimate Tech Flex: Implementing GPT-2 in Pure CMake](https://www.machucavalley.tech/blog/gpt2-pure-cmake-absurity/)
10. [GitHub - shaktsin/gpt2.c: GPT2 Inference Implementation in ...](https://github.com/shaktsin/gpt2.c)
11. [Implementation of GPT-2 in pure CMake - thenote.app](https://thenote.app/post/en/implementation-of-gpt-2-in-pure-cmake-jmzlyyrlac)
12. [Implementation of GPT-2 in pure CMake | Hacker News](https://news.ycombinator.com/item?id=49412909)
13. [Deconstruction Series #1: Rebuilding GPT-2 in Pure C](https://shaktsin.github.io/2025/06/19/writing-gpt-in-c.html)
14. [NanoEuler Tutorial: Run GPT-2 in Pure C/CUDA — AI Tutorial](https://aiindigo.com/tutorials/getting-started-with-nanoeuler-build-a-gpt-2-model-in-pure-c-cuda)
15. [GitHub - angry-kratos/GPT-2-in-C: GPT 2 implementation in pure C](https://github.com/angry-kratos/GPT-2-in-C)
16. [GitHub - NJX-njx/microgpt: The most atomic GPT-2 ...](https://github.com/NJX-njx/microgpt)
17. [Andrej Karpathy’s "llm.c" is Revolutionizing GPT-2 with a ...](https://infosecured.ai/i/andrej-karpathys-llm-c-is-revolutionizing-gpt-2/)
18. [Andrej Karpathy Trains GPT-2 in Pure C Without PyTorch](https://aidigitalnews.com/ai/andrej-karpathy-trains-gpt-2-in-pure-c-without-pytorch/)