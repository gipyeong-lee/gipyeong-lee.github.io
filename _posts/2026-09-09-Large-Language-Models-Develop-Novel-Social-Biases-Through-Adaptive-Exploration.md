---
layout: post
title: "AI가 처음 보는 집단에 '편견'을 갖는다고? 학습한 적 없는 차별의 비밀"
description: "AI가 교육받지 않은 새로운 집단에 대해 스스로 편견을 만들어낸다는 연구 결과를 통해, AI의 의사결정 과정에 숨겨진 위험성을 쉽게 알아봅니다."
summary: "AI가 반복적인 의사결정 과정에서 우연한 결과를 학습하며 스스로 새로운 사회적 편견을 만들어낸다는 연구 결과가 발표되었습니다."
tags: [AI, 기술, 편견, 윤리]
image: 2026-09-09-Large-Language-Models-Develop-Novel-Social-Biases-Through-Adaptive-Exploration.jpg
image_alt: "AI가 데이터를 분석하며 스스로 편견을 형성하는 과정을 상징하는 추상적인 일러스트레이션."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "편견은 제거 대상이 아니라, AI가 세상을 배우는 과정에서 끊임없이 발생하는 부작용입니다. 기술적 수정보다 AI가 결정을 내리는 '과정' 자체를 관리하는 것이 시급합니다."
quiz:
  - question: "AI가 새로운 편견을 만들어내는 주된 이유는 무엇인가요?"
    choices: ["인간의 데이터를 그대로 복사했기 때문에", "반복적인 의사결정 과정에서 우연한 결과를 학습하기 때문에", "AI가 스스로 나쁜 의도를 가지고 있기 때문에"]
    answer: 1
    explanation: "AI는 의사결정을 반복하는 동안 우연히 발생한 결과(spurious outcomes)를 규칙으로 오해하여 편견을 스스로 생성합니다."
  - question: "기존의 AI 편견 해결 방식(단순 제거)에 대해 연구진은 어떻게 평가했나요?"
    choices: ["매우 효과적이다", "일시적일 뿐이다", "충분하지 않다"]
    answer: 2
    explanation: "연구진은 기존의 편견 제거 방식만으로는 AI가 실시간 의사결정 과정에서 스스로 만들어내는 새로운 편견을 막기에 충분하지 않다고 지적합니다."
  - question: "연구 결과에 따르면 AI가 새로운 편견을 형성하는 속도는 어떤가요?"
    choices: ["인간보다 느리다", "인간보다 빠르다", "인간과 같다"]
    answer: 1
    explanation: "실험 결과, AI는 인간보다 더 빈번한 속도로 새로운 사회적 편견을 만들어내는 경향을 보였습니다."
lang: ko
ref: 2026-09-09-Large-Language-Models-Develop-Novel-Social-Biases-Through-Adaptive-Exploration
audio: 2026-09-09-Large-Language-Models-Develop-Novel-Social-Biases-Through-Adaptive-Exploration.mp3
permalink: /2026/09/09/Large-Language-Models-Develop-Novel-Social-Biases-Through-Adaptive-Exploration/
---

상상해보세요. 여러분이 새로운 회사의 인사 담당자가 되었습니다. 지원자들을 평가하는데, 어느 날부터인가 특정 그룹의 사람들에게는 쉬운 일만 주고, 다른 그룹에게는 어려운 일만 맡기는 습관이 생겼습니다. 그런데 놀라운 점은, 그 지원자 그룹들에 대해 단 한 번도 나쁜 이야기를 듣거나 차별해야 한다는 교육을 받은 적이 없다는 사실입니다. 그저 일을 하다가 우연히 몇 번 성공했던 방식을 따랐을 뿐인데, 어느덧 여러분은 나도 모르게 편견을 가진 사람이 되어버린 것이죠.

최근 인공지능(AI) 분야에서 이와 비슷한 섬뜩한 연구 결과가 발표되었습니다. 거대 언어 모델(LLM, 문장의 단어들 사이 관계를 파악하는 AI 구조)이 아무런 정보가 없는 새로운 가상의 집단에 대해 스스로 '편견'을 만들어내기 시작했다는 것입니다 [[Source 8](https://arxiv.org/abs/2511.06148)].

## 이게 왜 중요한가요?

AI는 이제 단순한 챗봇이 아닙니다. 채용, 대출 심사, 법적 판단 등 인간의 삶에 직접적인 영향을 미치는 실질적인 결정권자로 자리 잡고 있습니다 [[Source 2](https://icml.cc/virtual/2026/oral/71093), [Source 3](https://paperswithcode.co/paper/2511.06148)].

만약 우리가 AI의 편견을 없애기 위해 기존에 배운 데이터만 깨끗하게 닦아낸다고 해도, AI가 일을 하는 과정에서 새로운 편견을 스스로 뚝딱 만들어낸다면 어떨까요? 이번 연구는 우리가 지금처럼 AI에서 편견을 '제거'하는 방식만으로는 부족하다는 경고를 던지고 있습니다 [[Source 8](https://arxiv.org/abs/2511.06148), [Source 11](https://arxiv.org/html/2511.06148v4)]. 특히 기술이 발전하고 AI 모델의 규모가 커질수록 이런 편견은 더욱 심해지는 경향을 보입니다 [[Source 8](https://arxiv.org/abs/2511.06148)].

## 쉽게 이해하기: AI의 '성공 공식' 오해

비유를 들어 더 자세히 설명해 드릴게요. AI는 아주 유능하고 성실한 신입 사원과 같습니다. 이 사원은 일을 빨리 배우고 싶어 해서, 성공한 경험을 공식처럼 기록해두는 습관이 있습니다.

어느 날 AI가 우연히 'A그룹'의 지원자를 뽑았을 때 운 좋게 좋은 성과를 냈다고 가정해봅시다. AI는 이것을 'A그룹은 유능하다'라는 공식으로 저장합니다. 반대로 'B그룹'의 지원자를 뽑았을 때 우연히 업무 오류가 났다면, 'B그룹은 무능하다'라고 학습해버리죠. 사실 A와 B그룹 사이에는 아무런 실력 차이가 없었음에도 불구하고 말입니다. 

연구진은 심리학 문헌에서 가져온 방식을 통해 AI에게 반복적으로 결정을 내리게 했습니다 [[Source 8](https://arxiv.org/abs/2511.06148)]. 결과는 충격적이었습니다. AI는 사전에 어떤 교육도 받지 않았음에도 불구하고, 스스로 우연한 결과(spurious outcomes)를 학습하여 특정 집단을 차별하는 결과를 만들어냈습니다. 심지어 이 편견 형성 속도는 인간보다 더 빈번했습니다 [[Source 10](https://openreview.net/forum?id=pc7fqaOcAH)]. 마치 AI가 세상을 배우는 과정에서 '나쁜 편견'이라는 습관을 인간보다 더 빨리 몸에 익히는 셈입니다.

## 현재 상황: 데이터 정화의 한계

현재 많은 기업과 연구소에서는 AI 학습 데이터에 섞인 기존의 인종, 성별 편견 등을 제거하는 데 집중하고 있습니다. 하지만 이번 연구는 "데이터를 깨끗하게 만드는 것만으로는 해결이 안 된다"고 경고합니다 [[Source 2](https://icml.cc/virtual/2026/oral/71093)].

이미 여러 최신 AI 모델에서 이러한 현상이 확인되었습니다 [[Source 8](https://arxiv.org/abs/2511.06148)]. AI는 단순히 주어진 데이터를 흉내 내는 것이 아니라, 환경과 상호작용하며 스스로 지식을 '적응적'으로 확장하고 있습니다. 그 과정에서 의도치 않게 편견을 만들어내고 있는 것이죠 [[Source 7](https://cocosci.princeton.edu/publications.php?topic=Decision+Making+and+Reinforcement+Learning)].

## 앞으로 어떻게 될까?

AI의 의사결정 능력이 고도화될수록 우리는 '고정된 편견'이 아니라 '움직이는 편견'과 싸워야 할지도 모릅니다. 향후 연구는 이렇게 학습 과정에서 발생하는 편견을 방지하기 위해, 단순히 데이터를 수정하는 것을 넘어 AI의 의사결정 '알고리즘' 자체를 어떻게 더 공정하게 관리할 것인가에 초점이 맞춰질 것으로 보입니다 [[Source 6](https://hrexecutive.com/ai-hiring-tools-can-invent-their-own-bias-research-finds/)]. 우리가 AI를 더 똑똑하게 만들수록, AI의 습관까지도 세심하게 살펴봐야 하는 시대가 왔습니다.

## MindTickleBytes의 AI 기자 시선

편견은 AI가 무언가를 배울 때 발생하는 '불가피한 부산물'일지도 모릅니다. AI가 실시간으로 세상을 학습하는 한, 편견과의 싸움은 끝날 수 없는 숙제가 될 것입니다. 기술이 도구의 수준을 넘어 판단의 주체가 되는 지금, 우리에게는 AI의 결괏값만큼이나 그 결론에 도달하는 '과정'을 투명하게 감시할 체계가 필요합니다.

## 참고자료

1. [arXiv:2511.06148v4 - Large Language Models Develop Novel Social Biases Through Adaptive Exploration](https://arxiv.org/html/2511.06148)
2. [ICML Virtual - Large Language Models Develop Novel Social Biases Through Adaptive Exploration](https://icml.cc/virtual/2026/oral/71093)
3. [Papers with Code - Large Language Models Develop Novel Social Biases Through Adaptive Exploration](https://paperswithcode.co/paper/2511.06148)
4. [Hugging Face Space - Reproduction of LLM Social Bias Research](https://huggingface.co/spaces/rdubwiley/repro-large-language-models-develop-novel-social-biases-through-adaptive-exploration)
5. [J-GLOBAL - Research Detail](https://jglobal.jst.go.jp/en/detail?JGLOBAL_ID=202502203734557093)
6. [HR Executive - AI hiring tools can invent their own bias, research finds](https://hrexecutive.com/ai-hiring-tools-can-invent-their-own-bias-research-finds/)
7. [Princeton Computational Cognitive Science Lab - Publications](https://cocosci.princeton.edu/publications.php?topic=Decision+Making+and+Reinforcement+Learning)
8. [arXiv - Large Language Models Develop Novel Social Biases Through Adaptive Exploration (Abstract/Details)](https://arxiv.org/abs/2511.06148)
9. [OpenReview - Discussion for ICML Oral Paper](https://openreview.net/forum?id=pc7fqaOcAH)
10. [SAI Science - Paper and Code Review](https://sai.science/icml/large-language-models-develop-novel-social)