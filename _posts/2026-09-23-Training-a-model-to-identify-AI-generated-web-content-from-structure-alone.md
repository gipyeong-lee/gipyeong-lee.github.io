---
layout: post
title: "AI가 쓴 글, '단어'가 아니라 '구조'로 알아볼 수 있을까?"
description: "AI로 생성된 웹 콘텐츠를 단어 수준이 아닌, 글의 전체적인 정보 구성과 흐름이라는 구조적 특징으로 탐지하는 새로운 연구 기법을 소개합니다."
summary: "단어를 바꿔도 AI 특유의 글쓰기 '구조'는 숨길 수 없다는 연구 결과가 나왔습니다. 최근 연구된 'SlopShape' 기법은 정보의 배치와 논리 전개 방식만으로 AI 콘텐츠를 98%의 정확도로 찾아냅니다."
tags: [AI, 콘텐츠탐지, SlopShape, 기술연구, AI윤리]
image: 2026-09-23-Training-a-model-to-identify-AI-generated-web-content-from-structure-alone.jpg
image_alt: "다양한 데이터 블록들이 복잡한 논리 구조를 이루고 있는 웹페이지를 AI가 분석하는 모습을 형상화한 이미지."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "단어의 나열은 쉽게 수정될 수 있지만, AI가 학습한 글쓰기 체질인 '구조적 패턴'은 더욱 깊숙한 본질을 찌릅니다. 이번 연구는 AI 콘텐츠 식별의 새로운 국면을 예고합니다."
quiz:
  - question: "기존의 단어 기반 AI 탐지 방식이 가진 가장 큰 약점은 무엇인가요?"
    choices: ["느린 처리 속도", "내용의 문맥 파악 불가", "문장을 조금만 바꿔도 탐지 성능이 급격히 떨어짐"]
    answer: 2
    explanation: "기존 탐지기는 특정 단어나 패턴에 의존하기 때문에 글의 표현을 살짝 바꾸면 탐지하기 어려워지는 취약점이 있습니다."
  - question: "'SlopShape' 연구에서 AI 콘텐츠를 탐지하는 핵심 기준은 무엇인가요?"
    choices: ["문장의 단어 선택", "글의 구조와 정보 배열 방식", "사용된 이미지의 개수"]
    answer: 1
    explanation: "SlopShape는 단어의 선택이 아닌, 정보가 제시되는 순서나 논리적인 전개 방식 같은 구조적 특징을 분석합니다."
  - question: "'SlopShape'가 상업용 블로그 포스트를 탐지했을 때 달성한 정확도(macro-F1)는?"
    choices: ["85.0%", "92.5%", "98.0%"]
    answer: 2
    explanation: "연구 결과에 따르면 SlopShape는 새로운 데이터셋에서도 98.0%라는 높은 정확도로 AI 콘텐츠를 식별해냈습니다."
lang: ko
ref: 2026-09-23-Training-a-model-to-identify-AI-generated-web-content-from-structure-alone
audio: 2026-09-23-Training-a-model-to-identify-AI-generated-web-content-from-structure-alone.mp3
permalink: /2026/09/23/Training-a-model-to-identify-AI-generated-web-content-from-structure-alone/
---

상상해보세요. 여러분이 아침마다 읽는 즐겨찾는 뉴스레터나 블로그 글들이 있습니다. 평소와 다름없이 읽고 있었는데, 알고 보니 이 글의 절반 이상이 사람이 아닌 AI에 의해 작성되었다면 어떤 기분이 들까요? 

지금까지 우리는 AI가 쓴 글을 찾아내기 위해 주로 '단어'에 집중해 왔습니다. 하지만 AI를 만드는 개발자들이 똑똑해지면서, AI에게 "사람처럼 글을 써라"라고 지시하거나 단어를 조금만 비틀어 써도 기존의 탐지 기술들은 금세 무용지물이 되곤 했습니다. 이제 우리는 글의 겉모습이 아니라, 그 안의 '뼈대'를 볼 수 있는 새로운 시대에 접어들었습니다.

## 이게 왜 중요한가요?

인터넷은 정보의 바다입니다. 하지만 최근 생성형 AI가 대량으로 콘텐츠를 쏟아내면서, 무엇이 진짜 사람의 고민이 담긴 글인지, 무엇이 AI가 생성한 기계적인 결과물인지 구분하기가 매우 어려워졌습니다. [출처: 책임감 있는 탐지 및 완화 프레임워크](https://link.springer.com/article/10.1007/s44196-025-01025-w) 

기존의 탐지 방식은 마치 '특정 단어만 잡아내는 낚싯대'와 같았습니다. AI가 쓰는 단어 패턴이 조금만 바뀌어도 탐지기가 작동하지 않는 '취약성(brittleness)'을 보였죠. [출처: SlopShape 연구 논문](https://arxiv.org/abs/2609.15369) 하지만 글의 '구조'를 분석하는 방식이 도입된다면 상황은 달라집니다. 이는 우리가 온라인 정보를 소비할 때 콘텐츠의 진위 여부를 판단하는 신뢰의 기준을 바꿀 수 있는 중요한 전환점입니다.

## 쉽게 이해하기: '단어'라는 포장지에서 '구조'라는 본질로

AI가 쓴 글과 사람이 쓴 글을 구분하는 비결, 이렇게 비유하면 이해하기 쉽습니다. 

쉽게 말해서 '레고(LEGO)'를 생각해 보세요. 사람이 만든 레고 성과 기계가 자동으로 조립한 레고 성이 겉보기엔 비슷해 보여도, 레고 블록을 쌓아 올린 순서나 고정하는 방식은 서로 다를 수 있습니다. 우리가 기존에 사용하던 단어 탐지기가 "어떤 모양의 블록을 썼나"를 확인했다면, 이제는 "성벽을 쌓고 탑을 올린 전체적인 공정 순서(구조)"를 확인하는 것입니다. 

비유하면, 글을 사진 필터에 비유할 수도 있습니다. 단어 수준의 탐지기가 사진의 색감을 보정하는 필터를 감지하려 했다면, 구조적 탐지기는 사진 속 피사체가 놓인 위치, 조명의 각도, 카메라의 구도 같은 사진의 '본질적인 구도'를 파악하는 것입니다. 

최근 연구된 'SlopShape(슬롭셰이프)' 기법은 바로 이 본질적인 '글의 뼈대'를 분석합니다. [출처: SlopShape 연구 논문](https://arxiv.org/abs/2609.15369) 정보가 어떤 순서로 제시되는지, 어떤 논리적 단계를 거쳐 결론에 도달하는지, 근거를 어떻게 배치하는지 등을 학습하는 것이죠. 

## 현재 상황: '구조'를 보는 탐지기의 등장

실제로 2026년에 발표된 연구들에 따르면, 이러한 구조 분석 방식은 매우 강력한 성능을 보여줍니다. 

- **스토리 분석의 변화**: '스토리 스코프(StoryScope)' 연구(Russell et al., 2026)에서는 단어를 전혀 보지 않고도 AI가 작성한 이야기와 사람이 작성한 이야기를 구분해내는 데 성공했습니다. [출처: YCombinator 토론](https://news.ycombinator.com/item?id=49800566)
- **높은 정확도**: 'SlopShape' 연구에서는 상업용 블로그 포스트를 대상으로 테스트한 결과, 구조적인 특징만으로 AI 콘텐츠를 98.0%라는 경이로운 정확도로 찾아냈습니다. [출처: SlopShape 연구 논문](https://arxiv.org/html/2609.15369) 특히 이 모델은 학습 과정에서 본 적 없는 새로운 기업의 데이터에서도 일관된 성능을 보였습니다. 

이는 기술적으로 AI가 아무리 유창한 단어를 선택해 문장을 다듬어도, 모델 자체가 학습한 '글쓰기 관습'이나 '정보 전달의 논리 구조'까지 완전히 버리기는 어렵다는 것을 시사합니다. [출처: SlopShape 연구 논문](https://arxiv.org/abs/2609.15369)

## AI의 생각

단어의 나열은 쉽게 수정될 수 있지만, AI가 학습한 글쓰기 체질인 '구조적 패턴'은 더욱 깊숙한 본질을 찌릅니다. 이번 연구는 AI 콘텐츠 식별의 새로운 국면을 예고합니다.

## 앞으로 어떻게 될까?

앞으로는 '말장난'만으로는 탐지기를 피하기 힘든 세상이 올 것입니다. AI 개발자들은 더 자연스러운 구조를 만들기 위해 노력할 것이고, 탐지 기술은 더 깊은 차원의 논리 흐름을 읽어내는 방향으로 발전하겠죠. 독자인 우리는 AI와 사람이 만들어낸 콘텐츠가 뒤섞인 디지털 환경에서, 글의 형식을 넘어 그 안에 담긴 '의도'와 '논리적 뼈대'를 더 주의 깊게 살펴야 하는 시대가 올 것입니다.

## 참고자료

1. [YCombinator: Training a model to identify AI-generated web content from structure alone](https://news.ycombinator.com/item?id=49800566)
2. [ArXiv: SlopShape: Identifying AI-Generated Commercial Web Content](https://arxiv.org/html/2609.15369)
3. [ArXiv: SlopShape: Identifying AI-Generated Commercial Web Content](https://arxiv.org/abs/2609.15369)
4. [Springer: Responsible Detection and Mitigation of AI-Generated Text](https://link.springer.com/article/10.1007/s44196-025-01025-w)