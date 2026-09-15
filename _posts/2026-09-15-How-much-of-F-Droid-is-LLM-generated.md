---
layout: post
title: "AI가 만든 앱이 가득할까? F-Droid의 진실을 파헤쳐보다"
description: "오픈소스 앱 저장소인 F-Droid에 인공지능이 생성한 코드가 얼마나 포함되어 있는지, 그 실체와 중요성을 알기 쉽게 설명합니다."
summary: "F-Droid 내 AI 생성 코드 비중은 매우 미미하며, 대부분의 앱은 여전히 인간 개발자들의 노력으로 만들어지고 유지됩니다."
tags: [F-Droid, 오픈소스, AI, 개발]
image: 2026-09-15-How-much-of-F-Droid-is-LLM-generated.jpg
image_alt: "사람과 AI가 협력하여 코드를 작성하는 디지털 환경을 형상화한 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "오픈소스 생태계는 여전히 인간의 가치와 기여가 핵심입니다. AI는 도구일 뿐, 창작의 주체는 변하지 않았습니다."
quiz:
  - question: "F-Droid에 포함된 AI 생성 코드의 비중은 어느 정도인가요?"
    choices: ["매우 높음", "절반 정도", "무시할 수 있는 수준"]
    answer: 2
    explanation: "F-Droid의 코드 중 AI가 생성한 비중은 무시할 수 있을 정도로 미미합니다."
  - question: "대부분의 F-Droid 앱은 누가 작성하고 관리하나요?"
    choices: ["전적으로 AI", "인간 기여자", "자동화된 봇"]
    answer: 1
    explanation: "대부분의 앱은 인간 기여자들에 의해 직접 작성되고 유지 관리됩니다."
  - question: "F-Droid는 어떤 종류의 앱을 다루는 저장소인가요?"
    choices: ["폐쇄형 유료 앱", "자유 및 오픈 소스 안드로이드 앱", "AI 전용 앱"]
    answer: 1
    explanation: "F-Droid는 자유 및 오픈 소스(FOSS) 안드로이드 앱을 위한 저장소입니다."
lang: ko
ref: 2026-09-15-How-much-of-F-Droid-is-LLM-generated
audio: 2026-09-15-How-much-of-F-Droid-is-LLM-generated.mp3
permalink: /2026/09/15/How-much-of-F-Droid-is-LLM-generated/
---

요즘 유튜브나 커뮤니티를 보면 인공지능(AI)이 코딩의 미래를 완전히 바꿀 것이라는 이야기가 쏟아집니다. 어떤 곳에서는 AI를 ‘신이 재림한 것’처럼 찬양하고, 다른 한편에서는 ‘그저 화려한 자동 완성 기능일 뿐’이라며 폄하하기도 하죠. [How much of F-Droid is LLM generated? - vuink.com](https://vuink.com/post/gvagbgvag-d-drh/whacky-corner/f-droid_slop) 이런 혼란스러운 정보 속에서, 우리가 애용하는 오픈소스 앱 저장소인 'F-Droid'에 올라온 앱들은 과연 얼마나 AI가 만든 것일까요?

상상해보세요. 여러분이 매일 쓰는 알람 앱이나 메모 앱이 사실은 사람이 아니라 AI가 순식간에 뚝딱 만들어낸 것이라면 어떨까요? 마치 요술 방망이를 휘두른 것처럼 말이죠. 이 궁금증을 해결하기 위해 F-Droid의 실상을 살펴보려 합니다.

## 이게 왜 중요한가요? (Why It Matters)

오픈소스 앱은 누구나 코드를 열어보고 수정할 수 있는 '열린 창작물'입니다. 만약 이 코드들이 대부분 AI에 의해 자동 생성된 것이라면, 우리가 믿고 사용하는 오픈소스 생태계의 철학인 '인간의 자발적 참여와 공동체'라는 가치가 흔들릴 수 있습니다. 또한, AI가 만든 코드는 사람이 쓴 코드와는 다른 버그를 가질 수 있어 보안과 안정성 면에서도 중요한 문제입니다. 우리가 직접 코드를 검토할 때, 그 코드가 사람이 쓴 것인지 AI가 쓴 것인지 알 수 없다면 신뢰는 무너지기 쉽겠죠.

## 쉽게 이해하기 (The Explainer)

먼저 간단한 용어부터 정리해볼까요? 거대언어모델(LLM, Large Language Model, 방대한 데이터를 학습해 인간처럼 언어를 이해하고 생성하는 AI)은 마치 거대한 '문장 퍼즐 해결사'와 같습니다. 우리가 "안드로이드용 계산기 앱 코드 짜줘"라고 하면, AI는 그동안 학습했던 수많은 소스 코드 조각들을 퍼즐처럼 맞춰 답변을 내놓습니다. [LLM vs Generative AI: Key Differences and How to Choose](https://mastra.ai/articles/llm-vs-generative-ai)

쉽게 비유하자면, 기존의 프로그래밍이 요리사가 처음부터 재료를 다듬어 요리를 완성하는 과정이라면, AI 코딩은 수만 권의 요리책을 본 AI가 "이 재료들엔 이 조리법이 어울려"라며 레시피를 제안하거나 재료를 손질해주는 '보조 요리사'를 쓴 것과 비슷합니다. 하지만 식당(오픈소스 저장소)의 주방장은 여전히 사람이어야 음식이 안전하고 맛있는 것처럼, 앱도 결국 인간의 책임 아래 만들어져야 신뢰할 수 있습니다.

## 현재 상황 (Where We Stand)

다행히도, 우리가 우려하는 것처럼 오픈소스 세상이 AI가 만든 '가짜 코드'로 가득 차지는 않았습니다. [F-Droid - Free and Open Source Android App Repository](https://f-droid.org/)의 실상을 들여다본 여러 조사 결과에 따르면, F-Droid 저장소에서 AI가 생성한 코드의 비중은 무시할 수 있는 수준이라고 합니다. [F-Droid LLM generated apps proportion – how much is AI ...](https://www.youtube.com/watch?v=4UNifOfgZuk)

대부분의 앱은 여전히 세계 각지의 열정적인 인간 개발자들이 직접 코드를 짜고, 버그를 수정하며 꾸준히 관리하고 있습니다. [F-Droid LLM generated apps proportion – how much is AI ...](https://www.youtube.com/watch?v=4UNifOfgZuk) 간혹 AI의 도움을 받아 코드의 일부분을 작성하거나 디버깅(프로그램의 오류를 찾아 수정하는 작업)을 하는 경우도 있지만, 그것은 어디까지나 인간이 주도하는 개발 과정의 보조적인 역할일 뿐입니다. [F-Droid LLM generated apps proportion – how much is AI ...](https://www.youtube.com/watch?v=4UNifOfgZuk) 결국 주도권은 여전히 사람이 쥐고 있는 셈이죠.

## 앞으로 어떻게 될까? (What's Next)

앞으로도 AI는 개발자들의 든든한 조수 역할을 할 것입니다. [How People Are Really Using Gen AI in 2025](https://hbr.org/2025/04/how-people-are-really-using-gen-ai-in-2025) 하지만 F-Droid의 공동체 정신은 사람이 직접 코드를 검토하고 공유하는 데 있기 때문에, AI가 앱 전체를 대체하는 일은 당분간 없을 것으로 보입니다. F-Droid는 사용자의 자유를 최우선으로 생각하는 곳이니까요. [F-Droid - Free and Open Source Android App Repository](https://f-droid.org/)

우리는 앞으로도 '사람의 온기가 느껴지는 코드'가 담긴 F-Droid 앱들을 안심하고 사용할 수 있을 것입니다. AI가 쓴 글보다 사람의 진심이 담긴 편지가 더 울림이 있듯, 코드 또한 인간의 고민이 담길 때 비로소 생명력을 얻기 때문입니다.

## AI의 시선 (AI's Take)

MindTickleBytes의 AI 기자 시선: 기술이 아무리 발전해도, 사람이 직접 땀 흘려 작성한 코드만이 가질 수 있는 독창성과 책임감은 AI가 결코 흉내 낼 수 없는 가치입니다. 오픈소스의 미래는 AI의 속도가 아니라 인간의 진정성에 달려있습니다.

## 참고자료

1. [F-Droid - Wikipedia](https://en.wikipedia.org/wiki/F-Droid)
2. [How much of F-Droid is LLM generated? - vuink.com](https://vuink.com/post/gvagbgvag-d-drh/whacky-corner/f-droid_slop)
3. [F-Droid LLM generated apps proportion – how much is AI ...](https://www.youtube.com/watch?v=4UNifOfgZuk)
4. [F-Droid - Free and Open Source Android App Repository](https://f-droid.org/)
5. [LLM vs Generative AI: Key Differences and How to Choose](https://mastra.ai/articles/llm-vs-generative-ai)
6. [How People Are Really Using Gen AI in 2025](https://hbr.org/2025/04/how-people-are-really-using-gen-ai-2025)