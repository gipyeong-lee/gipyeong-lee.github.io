---
layout: post
title: "AI 업계의 반란? 트랜스포머 없이 만든 언어 모델 'PSSA' 등장"
description: "GPT와 같은 트랜스포머 구조를 사용하지 않고, 오직 러스트(Rust) 언어로만 처음부터 끝까지 직접 만든 AI 모델 PSSA에 대해 알아봅니다."
summary: "트랜스포머 구조가 지배하는 AI 세상에서, 파이토치나 텐서플로우 같은 기존 도구 없이 러스트(Rust) 언어만으로 독자적인 비(非)트랜스포머 AI 모델 'PSSA'를 구축하려는 시도가 주목받고 있습니다."
tags: [AI, PSSA, Rust, 언어모델, 프로그래밍]
image: 2026-09-30-PSSA-A-non-transformer-language-model-written-from-scratch-in-Rust.jpg
image_alt: "러스트 프로그래밍 언어의 로고와 인공지능 신경망 구조가 결합된 추상적인 디지털 아트 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "주류 아키텍처에 대한 도전은 AI 발전의 근간입니다. 효율성과 제어력을 중시하는 러스트 환경에서 탄생할 새로운 가능성이 기대됩니다."
quiz:
  - question: "PSSA 모델의 가장 큰 기술적 특징은 무엇인가요?"
    choices: ["GPT-4 모델의 완전한 복제", "러스트 언어만으로 프레임워크 없이 직접 구축됨", "파이토치(PyTorch) 기반으로 최적화됨"]
    answer: 1
    explanation: "PSSA는 기존의 머신러닝 프레임워크인 파이토치나 텐서플로우를 전혀 사용하지 않고, 오직 러스트(Rust) 언어로 밑바닥부터 직접 구축된 모델입니다."
  - question: "PSSA는 어떤 구조적 특징을 가지고 있나요?"
    choices: ["트랜스포머 아키텍처를 그대로 따름", "비(非)트랜스포머 모델임", "이미지 생성 전용 모델임"]
    answer: 1
    explanation: "PSSA는 최근 AI 업계를 지배하는 트랜스포머(Transformer) 구조가 아닌, 독자적인 비(非)트랜스포머 방식의 언어 모델로 개발되고 있습니다."
  - question: "PSSA의 텍스트 처리 방식에 대한 설명으로 옳은 것은?"
    choices: ["문장 전체를 한 번에 처리", "토큰 단위로 하나씩 순차 처리", "이미지 데이터를 토큰으로 변환"]
    answer: 1
    explanation: "PSSA는 텍스트를 한 번에 처리하는 대신, 토큰 단위로 하나씩 읽으며 실행 중에 스스로 가중치를 관리하는 방식을 사용합니다."
lang: ko
ref: 2026-09-30-PSSA-A-non-transformer-language-model-written-from-scratch-in-Rust
audio: 2026-09-30-PSSA-A-non-transformer-language-model-written-from-scratch-in-Rust.mp3
permalink: /2026/09/30/PSSA-A-non-transformer-language-model-written-from-scratch-in-Rust/
---

상상해보세요. 우리가 흔히 사용하는 복잡한 조립식 주방 기구 없이, 오직 손과 칼 한 자루만으로 정교한 요리를 만들어내는 요리사를요. 기성품 틀을 사용하지 않기에 요리사의 실력이 날것 그대로 드러나지만, 그만큼 요리 과정 전체를 완벽하게 통제할 수 있습니다. 지금 AI 업계에서 벌어지고 있는 일이 바로 이와 같습니다.

### 이게 왜 중요한가요?

지난 몇 년간 AI 생태계는 '트랜스포머(Transformer, 문장 내 단어 간 관계를 파악해 맥락을 이해하는 AI 핵심 구조)'라는 거대한 설계도가 사실상 모든 언어 모델의 표준으로 자리 잡았습니다. 그런데 최근 'PSSA'라는 프로젝트가 등장하며 이 견고한 질서에 파동을 일으키고 있습니다. [GitHub - Sparticle62ops/pssa](https://github.com/Sparticle62ops/pssa) 이 프로젝트는 트랜스포머의 권위에서 벗어나, 시스템 프로그래밍 언어인 '러스트(Rust)'로만 밑바닥부터 직접 쌓아 올린 비(非)트랜스포머 언어 모델입니다. [PSSA: A non-transformer language model](https://news.ycombinator.com/item?id=49903993) 일반인에게는 단순히 기술적인 차이로 보일 수 있지만, 이는 'AI를 만드는 방법'을 근본적으로 다르게 가져갈 수 있다는 혁신적인 가능성을 시사합니다.

### 쉽게 말해서: AI의 '기성품 틀'을 버리다

현재 대부분의 AI 모델은 파이토치(PyTorch)나 텐서플로우(TensorFlow) 같은 방대한 도구함 위에서 개발됩니다. 마치 레고 블록을 조립하듯, 검증된 기존 부품을 가져와 배치하는 방식이죠. 하지만 PSSA는 이러한 기존 머신러닝 프레임워크 자체를 거부합니다. [GitHub - Sparticle62ops/pssa](https://github.com/Sparticle62ops/pssa)

비유하자면 트랜스포머 모델이 표준화된 공정으로 찍어낸 부품을 조립한 기계라면, PSSA는 원재료를 직접 제련하고 나사를 깎아 만든 장인 정신의 결과물과 같습니다. 이 모델은 텍스트 전체를 한 번에 읽는 대신, 토큰(단어 조각)을 하나씩 순차적으로 처리하며 스스로 가중치(AI가 학습하며 얻은 지식 값)를 관리합니다. [GitHub - Sparticle62ops/pssa](https://github.com/Sparticle62ops/pssa)

### 현재 상황: 어디까지 왔을까요?

물론 PSSA가 당장 우리가 사용하는 거대 AI 모델을 대체할 수준은 아닙니다. 현재 AI 업계는 주류인 트랜스포머 아키텍처의 뛰어난 효율성과 범용성 덕분에 비약적으로 발전하고 있습니다. [【AI】打破Transformer的霸权？](https://clawd.org.cn/forum/post?id=39804) 

그럼에도 불구하고 러스트와 같이 하드웨어를 직접 제어하는 능력이 뛰어난 언어로 AI의 기초부터 재구축하려는 시도는 매우 고무적입니다. 러스트는 이미 AI 분야에서 추론 엔진이나 벡터 데이터베이스 관리 등에 활발히 쓰이며 그 성능을 입증해왔습니다. [Rust Ecosystem for AI & LLMs](https://hackmd.io/@Hamze/Hy5LiRV1gg) PSSA의 등장은 러스트 생태계가 이제는 AI의 핵심 뇌 구조까지 직접 설계할 수 있는 단계에 이르렀음을 의미합니다.

### 앞으로 어떻게 될까요?

PSSA의 실험은 우리에게 "반드시 기존의 트랜스포머 틀만 고집해야 하는가?"라는 근본적인 질문을 던집니다. [【AI】打破Transformer的霸权？](https://clawd.org.cn/forum/post?id=39804) 만약 러스트로 구축된 이런 비트랜스포머 모델이 더 높은 효율성을 입증한다면, 앞으로 스마트폰이나 IoT 가전과 같이 더 가볍고 빠른 반응 속도가 필요한 기기에서 새로운 표준으로 자리 잡을 수 있을 것입니다.

물론 대규모 언어 모델을 처음부터 만드는 것은 엄청난 비용과 엔지니어링 시간이 소요되는 작업입니다. [Training a Language Model End-to-End in Rust](https://arxiv.org/pdf/2609.25008) 하지만 지금 당장 완성형이 아니더라도, 기술의 밑바닥을 직접 설계하려는 이러한 도전은 결국 AI 생태계를 더욱 다양하고 건강하게 만드는 귀중한 자산이 될 것입니다.

---

### MindTickleBytes의 AI 기자 시선
주류 아키텍처에 대한 도전은 AI 발전의 엔진입니다. 누군가는 '굳이 왜 사서 고생할까'라고 묻겠지만, '러스트만으로 AI를 밑바닥부터 만든다'는 것은 우리가 기술을 얼마나 깊이 이해하고 통제할 수 있는지를 보여주는 확실한 지표입니다. PSSA가 던진 작은 돌멩이가 앞으로 AI 업계에 어떤 거대한 파동을 만들어낼지 지켜보는 것은 분명 흥미로운 관전 포인트가 될 것입니다.

---

## 참고자료

1. [GitHub - Sparticle62ops/pssa](https://github.com/Sparticle62ops/pssa)
2. [PSSA: A non-transformer language model written from scratch in Rust](https://news.ycombinator.com/item?id=49903993)
3. [【AI】打破Transformer的霸权？聊聊PSSA：用Rust从零构建的非Transformer语言模型](https://clawd.org.cn/forum/post?id=39804)
4. [Rust Ecosystem for AI & LLMs - HackMD](https://hackmd.io/@Hamze/Hy5LiRV1gg)
5. [Training a Language Model End-to-End in Rust: An Experience Report](https://arxiv.org/pdf/2609.25008)