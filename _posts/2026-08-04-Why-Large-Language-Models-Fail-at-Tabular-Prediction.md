---
layout: post
title: "AI가 엑셀 데이터 분석은 왜 못할까? 똑똑한 모델의 의외의 약점"
description: "거대 언어 모델(LLM)이 왜 표 형태의 데이터(Tabular Data) 분석에서 기존 방식보다 뒤처지는지 그 이유와 한계를 알기 쉽게 설명합니다."
summary: "거대 언어 모델은 텍스트 분석에는 탁월하지만, 표 데이터를 다룰 때는 데이터의 순차적 구조에 대한 잘못된 편향과 복잡한 수치 해석의 한계로 인해 기존 데이터 분석 방법보다 성능이 떨어집니다."
tags: [AI, 데이터분석, LLM, 테크상식]
image: 2026-08-04-Why-Large-Language-Models-Fail-at-Tabular-Prediction.jpg
image_alt: "복잡하게 얽힌 표 데이터를 돋보기로 들여다보는 AI의 모습을 형상화한 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "언어 모델에게 모든 것을 맡기는 것은 위험합니다. 분야에 맞는 적절한 도구를 선택하는 지혜가 필요합니다."
quiz:
  - question: "거대 언어 모델(LLM)이 표 데이터를 분석할 때 겪는 주요 문제점은 무엇인가요?"
    choices: ["모든 수치를 완벽하게 이해하지만 속도가 느리다", "표 데이터를 순차적인 텍스트로 바꾸면서 데이터의 본질적인 구조를 오해한다", "표 데이터를 읽지 못해 이미지로 변환해야만 한다"]
    answer: 1
    explanation: "LLM은 표를 텍스트로 직렬화하면서 언어 모델 특유의 '순차적 구조'라는 편향을 가지게 되어 표 데이터의 특징을 제대로 파악하지 못합니다."
  - question: "LLM이 표 데이터를 위해 자동으로 생성한 기능(feature)들이 낮은 성능을 보이는 이유는 무엇인가요?"
    choices: ["덧셈과 같은 단순한 연산에만 치우치고, 그룹화나 집계 같은 복잡한 연산을 잘 활용하지 못하기 때문이다", "너무 복잡한 연산만 수행해서 일반적인 데이터에는 맞지 않기 때문이다", "데이터 보안 규정 때문에 복잡한 연산을 수행할 수 없기 때문이다"]
    answer: 0
    explanation: "최신 연구들에 따르면 LLM은 덧셈 같은 단순 연산에 편향되어 있으며, 데이터 분석에 필수적인 집계나 그룹화 기능을 제대로 활용하지 못하는 것으로 나타났습니다."
  - question: "LLM 기반 데이터 분석 모델의 성능이 급격히 떨어지는 상황은 언제인가요?"
    choices: ["데이터의 양이 너무 적을 때", "데이터에 사람 이름이 포함되어 있을 때", "열(column)의 식별자(이름)가 제거되거나 의미 없는 문자로 바뀌었을 때"]
    answer: 2
    explanation: "LLM은 인간이 읽을 수 있는 메타데이터(열 이름 등)에 크게 의존하기 때문에, 이것이 사라지면 성능이 매우 크게 하락합니다."
lang: ko
ref: 2026-08-04-Why-Large-Language-Models-Fail-at-Tabular-Prediction
audio: 2026-08-04-Why-Large-Language-Models-Fail-at-Tabular-Prediction.mp3
permalink: /2026/08/04/Why-Large-Language-Models-Fail-at-Tabular-Prediction/
---

상상해보세요. 여러분이 회사에서 수만 줄의 매출 데이터가 담긴 엑셀 파일을 들고 있다고 말이죠. 매달 제품별로 누가, 언제, 얼마나 팔았는지 정리된 이 '표'를 분석해달라고, 요즘 세상에서 가장 똑똑하다는 AI에게 물어봅니다. 그런데 AI가 "음, 이 데이터는 그냥 평범한 이야기처럼 읽히네요"라며 엉뚱한 소리를 합니다. 숫자 계산을 정확히 해야 할 AI가 왜 이런 실수를 하는 걸까요?

최근 거대 언어 모델(Large Language Models, LLM, 방대한 양의 텍스트를 학습해 인간처럼 대화하는 AI)은 우리가 쓰는 문장을 요약하고 어려운 논문을 분석하거나, 복잡한 프로그래밍 코드를 짜는 데 놀라운 능력을 보여줍니다. 하지만 정작 엑셀이나 데이터베이스 같은 '표 형태의 데이터(Tabular Data)'를 분석하는 데에는 10년 전부터 쓰던 전통적인 통계 방식보다 오히려 뒤처지는 모습을 보입니다 [출처 10](https://arxiv.org/html/2403.01570v3), [출처 11](https://openreview.net/forum?id=r8tMECbxOl).

### 이게 왜 중요한가요?

현대 비즈니스와 연구 현장에서 대부분의 핵심 데이터는 표 형태로 존재합니다. 재무 보고서, 고객 구매 내역, 임상 시험 결과 등 중요한 결정은 모두 이 숫자들의 표를 통해 이루어집니다. 만약 가장 진보된 AI가 이 핵심 데이터를 제대로 이해하지 못한다면, 기업들은 여전히 구식 분석 도구에 의존해야 하며 최신 AI의 혜택을 온전히 누리지 못하게 됩니다. 우리가 AI에게 기대하는 '똑똑한 비서'의 모습이 되려면, 이 숫자 데이터 분석이라는 벽을 반드시 넘어야 합니다.

### 쉽게 말해서: AI는 표를 '문장'으로 읽습니다

AI가 왜 표 데이터를 잘 못 다루는지 비유를 들어 설명해 드릴게요.

'트랜스포머(Transformer, 문장 속 단어 간의 관계를 파악해 의미를 추출하는 AI의 핵심 구조)'라는 기술은 원래 '언어'를 위해 태어났습니다. 쉽게 말해, AI는 텍스트를 읽을 때 왼쪽에서 오른쪽으로 흐르는 '이야기의 흐름'을 찾도록 훈련되었습니다. 

그런데 표 데이터를 만나면 AI는 마치 외국어로 된 소설책을 읽듯이 표를 강제로 텍스트로 바꾸어서(직렬화) 읽기 시작합니다. [출처 9](https://arxiv.org/html/2602.04031v2) "1행 1열은 매출, 1행 2열은 제품..." 이런 식으로 말이죠. 

여기서 문제가 발생합니다. 표는 '이야기'가 아닙니다. 표는 행과 열이 독립적으로, 혹은 아주 복잡하게 연결된 2차원 공간입니다. AI는 본능적으로 순서가 있는 문장을 읽으려 하지만, 표는 순서와 상관없는 다차원적인 정보의 덩어리입니다. 마치 **지도를 보고 길을 찾아야 하는데, 지도 위 지명들을 순서대로 나열한 글만 보고 위치를 파악하려는 것**과 비슷합니다. [출처 9](https://arxiv.org/html/2602.04031v2)

또한, AI는 데이터를 분석할 때 덧셈 같은 기초적인 산술 연산에는 익숙하지만, 실제 데이터 분석에서 중요한 '그룹별 합계(grouping and aggregations)' 같은 복잡한 논리를 스스로 만들어내는 데에는 서툽니다 [출처 3](https://arxiv.org/html/2410.17787v1), [출처 8](https://arxiv.org/html/2410.17787v2). 사람이 엑셀에서 피벗 테이블을 만드는 수준의 논리적 분석을 AI는 아직 '학습'하지 못한 것이죠.

### 어디서 우리는 서 있는가: AI는 '눈치'로 분석합니다

현재 많은 AI 모델은 데이터 자체가 무엇인지 깊이 이해하기보다는, 표에 적힌 열의 이름(식별자)에 크게 의존합니다. [출처 12](https://arxiv.org/html/2605.06290v1) 예를 들어, 'Sales_Amount'라는 열 이름을 보면 AI는 "아, 이건 매출액이구나"라고 눈치를 챕니다. 그런데 만약 이 이름을 'col_01'처럼 의미 없는 문자로 바꾸면 AI의 성능은 급격히 떨어집니다. [출처 12](https://arxiv.org/html/2605.06290v1) 즉, 실제 데이터의 값을 깊게 해석하는 게 아니라, 사람이 붙여둔 이름표(메타데이터)를 보고 짐작하고 있는 수준인 셈입니다. [출처 6](https://arxiv.org/abs/2402.17944)

이러한 한계 때문에 현장에서는 여전히 결정 트리(Decision Tree) 기반의 전통적인 머신러닝 방식이 훨씬 더 빠르고 정확하게 표 데이터를 분석하고 있습니다. [출처 11](https://openreview.net/forum?id=r8tMECbxOl)

### 앞으로의 방향: 진정한 데이터 분석가로

앞으로는 언어 모델이 텍스트만 잘하는 것이 아니라, 표의 구조 그 자체를 이해할 수 있도록 하는 '데이터 언어 모델'에 대한 연구가 활발해질 것입니다. [출처 6](https://arxiv.org/abs/2402.17944) 우리가 표 데이터를 보며 "여기서 가장 많이 팔린 제품이 뭐야?"라고 물었을 때, AI가 이름표를 보고 눈치를 채는 것이 아니라, 표의 구조를 정확히 인지하고 수학적으로 집계하여 답변하는 날이 올 것입니다. 

하지만 지금 당장은 AI에게 중요한 경영 수치 분석을 100% 맡기기보다는, 텍스트 요약이나 코드 생성과 같은 분야에서 보조적인 도구로 활용하는 현명함이 필요합니다.

### MindTickleBytes의 AI 기자 시선
언어 모델은 세상의 지식을 텍스트로 배워왔기에 숫자로 가득 찬 표를 '낯선 언어'로 받아들이고 있습니다. 하지만 AI가 수학적 논리를 언어적 통찰과 결합하는 법을 배우는 순간, 우리 업무 효율은 지금과는 차원이 다른 속도로 빨라질 것입니다. 그때까지는 AI를 우리의 '천재적인 비서'로만 부려주세요.

## 참고자료

1. [Source 3] Large Language Models Engineer Too Many Simple Features for Tabular Data (https://arxiv.org/html/2410.17787v1)
2. [Source 6] Large Language Models(LLMs) on Tabular Data: Prediction, Generation, and Understanding -- A Survey (https://arxiv.org/abs/2402.17944)
3. [Source 8] Large Language Models Engineer Too Many Simple Features for Tabular Data (https://arxiv.org/html/2410.17787v2)
4. [Source 9] The Illusion of Generalization in Tabular Language Models (https://arxiv.org/html/2602.04031v2)
5. [Source 10] Small Models are LLM Knowledge Triggers for Medical Tabular Prediction (https://arxiv.org/html/2403.01570v3)
6. [Source 11] Language Models Are Good Tabular Learners (https://openreview.net/forum?id=r8tMECbxOl)
7. [Source 12] Data Language Models: A New Foundation Model Class for Tabular Data (https://arxiv.org/html/2605.06290v1)