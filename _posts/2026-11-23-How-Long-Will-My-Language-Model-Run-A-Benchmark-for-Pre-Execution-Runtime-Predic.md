---
layout: post
title: "AI에게 '이 일 얼마나 걸릴까?' 물어봤더니… 99%를 틀렸다?"
description: "거대 언어 모델(LLM)이 AI 작업 실행 시간을 예측할 수 있을까? PreRun 벤치마크 연구를 통해 본 AI의 시간 감각과 현실적인 한계를 알기 쉽게 파악해봅니다."
summary: "연구진이 개발한 PreRun 벤치마크에 따르면, 최신 AI 모델들은 작업 설명만 듣고 실행 시간을 예측할 때 실제보다 90~99%나 터무니없이 짧게 예측하는 것으로 나타났습니다."
tags: [AI, 벤치마크, 머신러닝, GPU, PreRun]
image: 2026-11-23-How-Long-Will-My-Language-Model-Run-A-Benchmark-for-Pre-Execution-Runtime-Predic.jpg
image_alt: "첨단 슈퍼컴퓨터 서버실과 미래지향적인 디지털 타이머가 나란히 빛나고 있는 모습을 표현한 일러스트"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI가 아무리 똑똑해져도 '물리적인 컴퓨팅 자원의 소요 시간'을 직감만으로 맞히기는 어렵습니다. 전통적인 통계 모델과 AI의 협업이 왜 필요한지 보여주는 흥미로운 사례입니다."
quiz:
  - question: "연구진이 대규모 언어 모델과 비전 모델의 실행 시간을 예측하기 위해 도입한 새로운 벤치마크의 이름은 무엇인가요?"
    choices: ["PreRun", "LiveBench", "TerminalBench"]
    answer: 0
    explanation: "PreRun은 실행 전에 가능한 정보를 바탕으로 딥러닝 학습 및 추론 런타임을 예측하기 위해 도입된 벤치마크입니다."
  - question: "오픈웨이트 LLM들이 예시(Few-shot) 없이 작업 설정을 처리했을 때, 레이턴시(실행 지연 시간)를 평균적으로 얼마나 과소평가(축소 예측)했나요?"
    choices: ["10~20%", "50~60%", "90~99%"]
    answer: 2
    explanation: "오픈웨이트 LLM들은 예시 없이 질문했을 때 레이턴시를 90~99%나 과소평가하는 심각한 오차를 보였습니다."
  - question: "비교 평가에서 32개의 설정으로 학습된 어떤 전통적 머신러닝 방식이 제로숏 Claude의 평균 절대 오차보다 훨씬 우수한 성능을 보였나요?"
    choices: ["랜덤 포레스트(Random Forest)", "선형 회귀(Linear Regression)", "서포트 벡터 머신(SVM)"]
    answer: 0
    explanation: "랜덤 포레스트(Random Forest) 회귀 모델은 32개의 설정으로 학습되었을 때 Claude의 제로숏 오차보다 훨씬 낮은 오차를 기록했습니다."
lang: ko
ref: 2026-11-23-How-Long-Will-My-Language-Model-Run-A-Benchmark-for-Pre-Execution-Runtime-Predic
audio: 2026-11-23-How-Long-Will-My-Language-Model-Run-A-Benchmark-for-Pre-Execution-Runtime-Predic.mp3
permalink: /2026/11/23/How-Long-Will-My-Language-Model-Run-A-Benchmark-for-Pre-Execution-Runtime-Predic/
---

상상해보세요. 여러분이 엄청나게 비싸고 거대한 공유 주방(슈퍼컴퓨터 GPU 클러스터)을 빌려서 아주 복잡한 요리(대형 AI 모델 학습 및 추론 작업)를 시작하려고 합니다. 주방 관리자에게 "이 요리를 완성하는 데 정확히 몇 분이 걸릴까요?"라고 물어보았습니다. 관리자가 요리 레시피(작업 설명서)를 대충 훑어보고는 "음, 1분이면 끝납니다!"라고 자신 있게 대답했습니다. 

하지만 실제로 요리를 시작해보니 무려 100분이 넘게 걸렸고, 주방 대여 비용은 눈덩이처럼 불어났습니다.

최근 인공지능(AI) 연구계에서 이와 똑같은 황당하면서도 진지한 실험 결과가 발표되었습니다. 거대 언어 모델(LLM, Large Language Model - 인간의 언어를 이해하고 생성하는 대형 인공지능)에게 AI 모델 학습과 추론 작업이 얼마나 걸릴지 미리 물어봤더니, 예상보다 시간을 터무니없이 짧게 예측해버린 것입니다 [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)]. 도대체 왜 이런 일이 벌어진 걸까요?

---

## 이게 왜 중요한가요?

AI 기술이 눈부시게 발전하면서 전 세계의 연구원들과 기업들은 수많은 딥러닝(Deep Learning, 인간의 신경망을 모방하여 컴퓨터가 스스로 학습하게 만드는 기술) 모델을 만들고 실행하고 있습니다. 이 과정에서 가장 골치 아픈 문제 중 하나는 **'이 AI 작업을 실행하는 데 컴퓨터 자원이 얼마나 들고 시간이 얼마나 걸릴까'**를 정확히 예측하는 것입니다 [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)].

현실에서 연구원들이 GPU(Graphics Processing Unit, 고성능 연산을 빠르게 처리하는 그래픽 카드 장치) 클러스터라는 공유 컴퓨팅 자원에 작업을 제출할 때는 반드시 '시간 제한(Time limit)'을 설정해야 합니다. 시간이 지나면 작업이 강제로 종료되기 때문입니다. 또한 예산을 효율적으로 배분하고 하드웨어를 선택하기 위해서도 정확한 실행 시간(Runtime) 예측은 필수적입니다 [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)].

여기서 사람들은 매번 복잡한 수학적 계산을 하거나 시뮬레이션을 돌리는 대신, 유혹적인 지름길을 떠올렸습니다. 바로 **"AI에게 작업 설명서를 주고 몇 분 걸릴지 물어보자!"**라는 아이디어였습니다 [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)]. 만약 LLM이 문서를 읽고 실행 시간을 척척 맞힐 수 있다면 연구원들의 수고가 엄청나게 줄어들 것입니다. 하지만 정말 AI가 그럴 능력이 있는지 검증해볼 필요가 있었고, 연구진은 이를 위해 특별한 시험대를 만들었습니다.

---

## 쉽게 이해하기: PreRun 벤치마크란 무엇인가요?

이 문제를 해결하기 위해 연구진은 **PreRun**이라는 새로운 벤치마크(Benchmark, 성능을 공정하게 비교하기 위한 평가 시험)를 도입했습니다 [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)]. 

쉽게 말해서 **PreRun은 AI 모델들의 '시간 감각 시험지'**입니다. 이 시험지에는 실제 GPU 클러스터에서 수집된 방대한 기록들이 담겨 있습니다. 구체적으로는 언어 모델과 비전(시각) 모델의 학습(Training) 기록 801건과 추론(Inference, 학습된 모델이 실제로 답을 만들어내는 과정) 기록 1,884건이 포함되어 있습니다 [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)]. 여기에 작업 설정값과 명확하게 정의된 시간 목표치들이 짝을 이루고 있습니다. 또한 표준화된 조건에서 측정된 64개의 텍스트 생성 설정(각각 3회씩 별도로 프로그램 실행)도 포함되어 철저한 검증이 가능하도록 설계되었습니다 [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)].

비유하자면, 우리가 요리사에게 '이 재료로 2인분 파스타를 만들 때 걸리는 시간'을 맞히게 하려고 과거에 수천 번 요리했던 주방 CCTV 영상과 레시피 노트를 통째로 모아둔 것과 같습니다. 이 노트를 보고 AI가 얼마나 정확하게 시간을 맞히는지 채점하는 것입니다.

연구진은 이 시험을 통해 세 가지 대표적인 AI 모델—**Qwen3.5-9B, GPT-OSS-120B, Claude Opus 5.5**—의 실력을 기존의 통계적 회귀 분석 모델(Regression baselines, 데이터를 기반으로 수치의 관계를 예측하는 전통적인 수학 모델)과 비교했습니다 [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)].

---

## 현재 상황: AI의 시간 감각은 어느 수준일까?

실험 결과는 다소 충격적이었습니다. AI가 인간의 언어를 아무리 유창하게 이해하고 복잡한 코딩을 해낸다고 하더라도, 물리적인 컴퓨터 작업의 실행 시간 예측에서는 엄청난 허점을 드러냈습니다.

1. **지독한 과소평가 (90~99% 오류)**: 예시(Few-shot)를 전혀 주지 않고(Zero-shot) AI에게 작업 설정을 주며 시간을 물어보았을 때, 오픈웨이트 LLM(Open-weight LLMs, 소스코드가 공개된 개방형 인공지능 모델)들은 레이턴시(Latancy, 명령을 내리고 결과가 나올 때까지 걸리는 지연 시간)를 무려 **90%에서 99%나 과소평가**하는 것으로 나타났습니다 [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)]. 즉, 실제로는 100분이 걸릴 작업을 AI는 "1분이면 됩니다"라고 엉터리로 예측한 셈입니다.
2. **전통적 방식과의 비교**: Claude의 경우, 예시 없이 곧바로 예측(제로숏)했을 때의 평균 절대 오차(Mean absolute error)가, 단 32개의 설정값으로 학습된 **랜덤 포레스트(Random Forest, 여러 개의 결정 트리를 조합해 예측 정확도를 높이는 전통적인 머신러닝 알고리즘)** 모델보다 **4.5배**나 높았습니다 [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)]. AI가 직감이나 문장 이해력만으로는 하드웨어의 물리적 소요 시간을 제대로 가늠하지 못한다는 뜻입니다.
3. **모범 답안(예시)의 효과**: 다만, AI에게 단 5개의 구체적인 학습 예시(Labeled examples)를 사전에 제공했더니 Claude의 텍스트 생성 예측 오차가 크게 줄어드는 모습을 보였습니다. 다만 이 예시들의 효과는 측정하려는 타이밍 목표에 따라 조금씩 다르게 나타났습니다 [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)].

이러한 결과는 AI가 텍스트를 읽고 '무슨 작업인지'는 기가 막히게 이해하지만, 실물 하드웨어 속에서 전자가 움직이고 메모리와 연산 장치가 부딪히며 소모되는 물리적 시간의 무게를 직관적으로 느끼지는 못한다는 점을 명확히 보여줍니다.

---

## 앞으로 어떻게 될까?

그렇다면 이번 연구가 우리에게 주는 시사점은 무엇일까요? 앞으로 AI와 시스템 운영의 세계는 어떤 방향으로 나아가게 될까요?

우선, 연구진은 이번에 구축한 데이터와 평가 파이프라인(Pipeline, 데이터가 흘러가며 처리되는 일련의 가공 체계)을 학계와 업계에 오픈소스(Open-source, 누구든지 자유롭게 쓰고 수정할 수 있도록 공개된 소프트웨어)로 공개할 예정입니다 [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)]. 이를 통해 전 세계의 연구원들이 AI의 '시간 예측 능력'을 향상시키기 위한 다양한 후속 연구를 진행할 수 있게 됩니다.

앞으로의 발전 방향은 다음과 같이 예상해 볼 수 있습니다:
- **하이브리드 접근법의 대중화**: AI의 뛰어난 문서 이해 능력과, 전통적인 머신러닝(랜덤 포레스트 등)의 수치 계산 능력을 결합한 하이브리드 시스템이 주목받을 것입니다. 작업 설명서는 AI가 읽고, 실제 시간 계산은 수학적 회귀 모델이 보완하는 방식입니다.
- **클라우드 자원 관리의 효율화**: GPU 클러스터를 운영하는 기업들은 작업 제출 전 시간 제한을 더 정확하게 설정하여 컴퓨팅 자원의 낭비를 막고, 불필요한 비용 지출을 줄일 수 있게 될 것입니다 [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)].

AI가 모든 것을 마법처럼 척척 해내는 시대처럼 보이지만, '하드웨어의 물리적인 시간'을 이해하는 것만큼은 여전히 차갑고 정확한 데이터와 통계의 영역으로 남아 있습니다. 앞으로 AI가 자신의 작업 시간마저 정확히 예측하는 똑똑한 비서로 진화해 나갈지 지켜보는 것도 큰 재미가 될 것입니다.

---

## 참고자료

1. [How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)