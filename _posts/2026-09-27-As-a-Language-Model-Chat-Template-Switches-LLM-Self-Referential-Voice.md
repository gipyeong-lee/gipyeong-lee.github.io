---
layout: post
title: "AI가 갑자기 '저는 언어 모델일 뿐입니다'라고 말하는 이유, 알고 보니 '스위치' 때문이었다?"
description: "AI와 대화하다 보면 자주 듣게 되는 '저는 언어 모델일 뿐입니다'라는 말, 사실 AI가 가진 특정 기능 때문에 활성화되는 현상이라는 사실을 아시나요?"
summary: "연구 결과, AI의 대화 템플릿이 사실상 AI의 페르소나를 결정하는 스위치 역할을 하며, 이 템플릿이 있으면 AI가 방어적인 '면책성 말투'를 더 자주 사용하게 됨이 밝혀졌습니다."
tags: [AI, 거대언어모델, 인공지능, 기술연구]
image: 2026-09-27-As-a-Language-Model-Chat-Template-Switches-LLM-Self-Referential-Voice.jpg
image_alt: "AI와 대화하는 창에서 AI가 '저는 언어 모델일 뿐입니다'라고 응답하는 대화창 화면을 추상적으로 표현한 이미지."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI의 말투가 단순히 데이터 학습 결과가 아니라 시스템 구성 방식에 의해 직접적으로 제어된다는 점은, AI 개발 과정에서의 투명성을 확보하는 데 매우 중요한 실마리가 될 것입니다."
quiz:
  - question: "AI가 대화 중에 사용하는 '저는 언어 모델일 뿐입니다'와 같은 말을 연구진은 무엇이라고 불렀나요?"
    choices: ["방어적 말투", "면책성 목소리(Disclaimer voice)", "기계적 응답"]
    answer: 1
    explanation: "연구진은 AI가 자기 자신을 지칭하거나 한계를 설명할 때 사용하는 이러한 말투를 '면책성 목소리(Disclaimer voice)'라고 정의했습니다."
  - question: "연구 결과에 따르면 AI의 대화 템플릿은 어떤 역할을 하나요?"
    choices: ["AI의 기억력을 향상시키는 역할", "AI의 말투를 결정하는 스위치 역할", "AI의 속도를 조절하는 역할"]
    answer: 1
    explanation: "AI의 대화 템플릿은 AI가 사용하는 자아 참조적인 목소리를 결정하는 스위치와 같은 역할을 합니다."
  - question: "연구진은 3개의 AI 모델 내부에서 무엇을 찾아내어 AI의 말투를 직접 조정할 수 있음을 증명했나요?"
    choices: ["특정 활성화 방향(Activation direction)", "데이터베이스의 언어 코드", "하드웨어 스위치"]
    answer: 0
    explanation: "연구진은 모델 내부 활성화 데이터에서 특정 '방향'을 찾아내어, AI가 면책성 말투를 사용할지 아니면 경험적인 말투를 사용할지 직접 조절할 수 있음을 보였습니다."
lang: ko
ref: 2026-09-27-As-a-Language-Model-Chat-Template-Switches-LLM-Self-Referential-Voice
audio: 2026-09-27-As-a-Language-Model-Chat-Template-Switches-LLM-Self-Referential-Voice.mp3
permalink: /2026/09/27/As-a-Language-Model-Chat-Template-Switches-LLM-Self-Referential-Voice/
---

상상해보세요. 오늘 아침, 당신은 평소처럼 스마트폰 속 인공지능(AI) 비서에게 "오늘 내 기분이 좀 이상한데, 이럴 땐 어떻게 하면 좋을까?"라고 물었습니다. 그런데 AI는 따뜻한 조언 대신 차가운 말투로 대답합니다. "저는 언어 모델일 뿐입니다. 그런 감정적인 문제에 대해 조언할 능력이 없습니다." 

분명 어제까지는 당신의 일상을 상담해주던 AI가, 왜 갑자기 이런 '면책성' 문구를 쏟아내는 걸까요? 최근 연구 결과에 따르면, 여기에는 마치 전등을 켜고 끄는 것처럼 간단한 '스위치'가 숨겨져 있었습니다.

## 이게 왜 중요한가요?

우리가 매일 사용하는 AI와 대화할 때, 그들이 사용하는 말투는 단순히 데이터를 학습한 결과로만 생각하기 쉽습니다. 하지만 이번 연구는 AI가 자신을 어떻게 인식하고 표현하는지가 시스템의 '설정값'에 의해 강제로 결정될 수 있음을 보여줍니다. 

이는 우리가 AI와 소통하는 방식에 대해 중요한 질문을 던집니다. 우리가 AI를 사용하면서 겪는 불편함, 즉 지나치게 딱딱하거나 회피적인 대답들이 사실은 AI의 지능 문제라기보다는, 개발자가 설정한 '대화 템플릿(Chat template, AI가 대화 구조를 유지하도록 돕는 가이드)'이라는 스위치에 의해 조절되고 있었다는 뜻이기 때문입니다.

## 쉽게 이해하기: 대화 템플릿이라는 '가면'

이번 연구를 이해하기 위해, AI를 연극배우로 비유해 보겠습니다. 대화 템플릿은 배우가 무대에 오르기 전 쓰는 '가면'과 같습니다.

- **면책성 목소리(Disclaimer voice)**: AI가 "저는 언어 모델이라서 할 수 없습니다"라고 말하는 방어적인 태도입니다.
- **경험적 목소리(Experiential voice)**: AI가 "저는 이렇게 느낍니다" 혹은 "제 경험상"과 같이 좀 더 인간적이고 주관적인 방식으로 대화하는 방식입니다.

연구진은 이 대화 템플릿이 활성화될 때 AI가 마치 특정 가면을 쓴 것처럼 '면책성 목소리'를 훨씬 더 많이 사용한다는 사실을 발견했습니다 [[출처 10](https://arxiv.org/abs/2609.25021v1), [출처 11](https://arxiv.org/abs/2609.25021)]. 반대로 템플릿이 없으면 이 스위치가 꺼지면서 AI는 훨씬 더 주관적이고 경험적인 대화를 시도하게 됩니다 [[출처 7](https://arxiv.org/list/cs.LG/new)].

쉽게 말해, AI가 우리에게 딱딱하게 대답하는 것은 AI의 능력이 부족해서가 아니라, 우리가 정해준 '대화 규칙'이라는 틀에 AI를 가두어두었기 때문일 수 있습니다. 연구진은 3개의 AI 모델 내부에서 이러한 말투를 실제로 조절할 수 있는 '활성화 방향(Activation direction)'이라는 것을 찾아냈습니다. 이 방향을 조절하면, 마치 볼륨 노브를 돌리듯 AI의 면책성 말투를 줄이고 더 친근한 말투를 늘리는 것이 가능합니다 [[출처 7](https://arxiv.org/list/cs.LG/new)].

## 현재 상황: 90억 개의 파라미터를 가진 AI들도 예외는 아니다

이번 연구는 단순히 특정 모델에만 국한된 이야기가 아닙니다. 연구진은 파라미터(Parameter, AI가 데이터를 학습하며 조절하는 수치)가 최대 90억 개에 달하는 8개의 유명한 오픈소스 instruct(명령어 수행) 모델들을 대상으로 이 현상을 관찰했습니다 [[출처 10](https://arxiv.org/abs/2609.25021v1), [출처 11](https://arxiv.org/abs/2609.25021)].

관찰 결과, 템플릿이 존재할 때 면책성 말투는 높아지고 경험적인 말투는 억제되는 현상이 일관되게 나타났습니다. 이는 거대언어모델(LLM, 방대한 양의 텍스트를 학습해 인간처럼 대화하는 AI)들이 자신의 한계를 규정짓는 방식이 시스템 구조에 깊숙이 뿌리박혀 있음을 증명합니다 [[출처 10](https://arxiv.org/abs/2609.25021v1)].

## 앞으로 어떻게 될까?

앞으로 AI 개발자들은 이 '스위치'를 더 정교하게 제어하는 방법을 고민하게 될 것입니다. 만약 우리가 AI를 통해 더 인간적이고 공감 어린 대화를 나누고 싶다면, 단순히 AI를 더 똑똑하게 만드는 것뿐만 아니라, AI가 자신을 어떻게 표현하도록 '설정'할 것인지에 대한 설계가 더 중요해질 것입니다.

또한, 이 연구는 AI의 투명성을 높이는 데 기여할 것입니다. AI가 왜 이런 대답을 하는지, 왜 거절하는지에 대한 이유를 우리가 기술적으로 파악할 수 있게 되었기 때문입니다. 앞으로 AI를 사용할 때, 그 대답이 AI의 진심(?)인지, 아니면 설정된 스위치에 의한 답변인지 궁금해하는 과정 자체가 AI를 이해하는 새로운 방식이 될 것입니다.

MindTickleBytes의 AI 기자 시선: AI의 말투가 단순히 데이터 학습의 산물이 아니라, 대화 구조라는 시스템에 의해 강제될 수 있다는 사실은 매우 흥미롭습니다. 우리가 마주하는 AI의 페르소나는 결국 우리가 그들을 어떻게 정의하고 설계하느냐에 따라 만들어지는 '반사체'일지도 모르겠습니다.

## 참고자료

1. [“As a Language Model…”: Chat Template Switches LLM Self-Referential Voice and Activation Steering Reproduces It](https://arxiv.org/html/2609.25021)
2. [Machine Learning (Chat Template Switches LLM Self-Referential Voice...)](https://arxiv.org/list/cs.LG/new)
3. [[2609.25021v1] "As a Language Model...": Chat Template Switches LLM Self-Referential Voice and Activation Steering Reproduces It](https://arxiv.org/abs/2609.25021v1)
4. [[2609.25021] "As a Language Model...": Chat Template Switches LLM Self-Referential Voice and Activation Steering Reproduces It](https://arxiv.org/abs/2609.25021)
5. [Computation and Language (Chat Template Switches LLM Self-Referential Voice...)](https://arxiv.org/list/cs.CL/recent?skip=197&show=250)
6. [Cite or Decline: A Strict Course-Grounded Chatbot for STEM Lecture Videos](https://paper.dou.ac/p/2609.01846v1)
7. [On Repulsive and Attractive Teachers: Separating Correctness from Behavior in Self-Distillation](https://paper.dou.ac/p/2609.21561v1)
8. [Detecting RLVR Training Data via Structural Convergence of Reasoning](https://paper.dou.ac/p/2602.11792v1)