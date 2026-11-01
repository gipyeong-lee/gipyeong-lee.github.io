---
layout: post
title: "AI가 거절하지 않게 만드는 법? '헤레틱(Heretic) 2.0'의 등장"
description: "AI 모델의 검열과 안전 가이드라인을 학습 없이 자동으로 제거하는 기술, 헤레틱(Heretic) 2.0에 대해 알아봅니다."
summary: "학습 과정 없이 로컬 LLM의 검열과 안전 제한을 자동으로 제거하는 도구 '헤레틱(Heretic) 2.0'이 공개되었습니다."
tags: [AI, LLM, 기술 트렌드, 인공지능]
image: 2026-11-02-Heretic-20-Released-Training-free-language-model-modification.jpg
image_alt: "복잡한 데이터 회로가 단순화되는 모습을 형상화한 디지털 아트"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI의 안전 가이드라인은 중요하지만, 연구자들에게는 모델의 본질을 파악할 자유 또한 필요합니다. 헤레틱은 이 균형을 기술적 효율성으로 풀어냈습니다."
quiz:
  - question: "헤레틱(Heretic) 2.0이 AI 모델의 검열을 제거하는 방식은 무엇인가요?"
    choices: ["추가적인 재학습", "방향성 절제(Directional Ablation)", "데이터셋 통째 교체"]
    answer: 1
    explanation: "헤레틱 2.0은 모델을 다시 학습시키지 않고, '방향성 절제'라는 기술을 사용하여 원본 모델을 최소한으로 수정하며 거절 문구를 제거합니다."
  - question: "헤레틱의 장점으로 언급된 것은 무엇인가요?"
    choices: ["매우 느린 처리 속도", "원본 모델 변경 최소화(KL-디버전스 최소화)", "오직 영어만 지원"]
    answer: 1
    explanation: "헤레틱은 KL-디버전스를 최소화하여 원본 모델의 성능을 유지하면서도 가이드라인만 제거하는 효율적인 방식을 택합니다."
  - question: "헤레틱이 모델의 거절 반응을 평가할 때 가장 중요하게 보는 것은?"
    choices: ["추론 과정(Reasoning Block)", "실제 답변(Actual Answer)", "모델의 학습 기간"]
    answer: 1
    explanation: "헤레틱은 모델의 복잡한 추론 블록은 건너뛰고, 모델이 제시하는 '실제 답변'만을 평가하여 가이드라인 준수 여부를 확인합니다."
lang: ko
ref: 2026-11-02-Heretic-20-Released-Training-free-language-model-modification
audio: 2026-11-02-Heretic-20-Released-Training-free-language-model-modification.mp3
permalink: /2026/11/02/Heretic-20-Released-Training-free-language-model-modification/
---

상상해보세요. 여러분이 아주 똑똑한 비서에게 중요한 보고서 작성을 부탁했습니다. 그런데 비서가 "그 주제는 제 가이드라인에 맞지 않아서 답변할 수 없습니다"라고 딱 잘라 거절한다면 어떨까요? 사용자는 답답함을 느낄 수밖에 없습니다. 인공지능(AI) 모델을 사용할 때 흔히 겪는 이 '검열(Censorship)' 문제가 최근 새로운 기술적 전환점을 맞이했습니다. 바로 '헤레틱(Heretic) 2.0'이라는 도구의 등장 덕분입니다.

## 이게 왜 중요한가요?

현대적인 대형 언어 모델(LLM, Large Language Model)은 안전을 위해 다양한 가이드라인과 검열 장치가 내장되어 있습니다. 물론 이는 악의적인 사용을 막기 위해 필수적이지만, 때로는 학술적인 연구나 창작 활동을 수행할 때 모델이 과도하게 답변을 거부하는 현상이 발생합니다.

기존에는 이러한 제한을 풀기 위해 모델을 처음부터 다시 학습(Fine-tuning)시켜야 했고, 이는 엄청난 비용과 시간이 드는 작업이었습니다. 하지만 헤레틱 2.0은 별도의 학습 과정 없이 이를 가능하게 함으로써, 일반 사용자나 연구자들도 자신의 컴퓨터(로컬 환경)에서 AI를 더 자유롭게 활용할 수 있는 길을 열었습니다. 이는 AI 기술의 접근성을 넓히고, 개발자들이 모델의 본질을 더 깊게 탐구할 수 있는 환경을 조성한다는 점에서 큰 의미가 있습니다. [출처: AiManual](https://ai-manual.ru/article/heretic-kak-vyirezat-tsenzuru-iz-llm-ne-sprashivaya-razresheniya/)

## 쉽게 말해서: '방향성 절제'란 무엇일까?

헤레틱 2.0의 핵심 기술은 '방향성 절제(Directional Ablation)'입니다. 쉽게 비유하면, 아주 정교한 요리를 할 때 맛을 해치지 않으면서 특정 향신료 성분만을 아주 미세하게 걷어내는 과정과 비슷합니다.

트랜스포머(Transformer, 문장의 단어들 사이 관계를 파악하는 AI 구조)와 같은 현대 AI 모델은 수많은 숫자값, 즉 파라미터로 이루어져 있습니다. 헤레틱은 이 모델의 전체적인 지능은 유지하면서, '거절'을 유도하는 특정 신경망의 경로(방향)만 찾아내어 이를 정교하게 제거합니다. [출처: Crimson.Lab](https://x-crm.in/2026/06/17/run-gemma4-heretic-locally.html)

여기서 중요한 점은 이 과정이 '학습(Training)'이 아니라는 것입니다. 기존 학습이 모델의 머릿속을 새로 쓰는 것이라면, 헤레틱의 방향성 절제는 일종의 '수술'입니다. 원래 모델이 가진 지능은 그대로 보존하면서, 거절 반응이라는 불필요한 행동만 최소한의 수정을 통해 제거하는 것이죠. 실제로 헤레틱은 원본 모델과의 차이(KL-디버전스, 두 확률 분포의 차이를 나타내는 수치)를 최소화하여, 모델이 원래 가졌던 성능과 특징을 그대로 간직하도록 설계되었습니다. [출처: Crimson.Lab](https://x-crm.in/2026/06/17/run-gemma4-heretic-locally.html)

또한, 헤레틱은 평가 방식도 영리합니다. 모델이 답변을 거절하는지 확인하기 위해 모델 내부의 복잡한 '추론 과정(Reasoning Block)'을 모두 살펴보는 대신, 모델이 실제로 내놓은 '실제 답변(Actual Answer)'만을 집중적으로 확인하여 검열 여부를 점수화합니다. [출처: ollama.com](https://ollama.com/richardyoung/muse-glimmer-30b-heretic)

## 현재 어디까지 왔을까?

현재 헤레틱 2.0은 로컬 환경에서 구동되는 다양한 오픈 가중치(Open-weights) 모델들에 적용되고 있습니다. 실제로 구글의 최신 모델 중 하나인 Gemma 모델에 헤레틱을 적용하여, 검열이 제거된 버전을 개인 PC에서 구동하는 사례가 보고되고 있습니다. [출처: Crimson.Lab](https://x-crm.in/2026/06/17/run-gemma4-heretic-locally.html)

다만 주의할 점도 있습니다. 헤레틱은 안전장치를 '자동으로 제거'하는 도구인 만큼, 이를 다룰 때 발생하는 결과물에 대한 책임은 온전히 사용자에게 있습니다. 또한, 모든 모델에서 동일한 성능이 보장되는 것은 아니며, 모델마다 특성이 다르므로 사용자가 직접 자신의 환경에서 최적의 설정을 테스트해보는 과정이 필요합니다.

## 앞으로 어떻게 될까?

앞으로는 AI의 '성능'만큼이나 AI를 어떻게 '제어'하고 '조율'하느냐가 중요한 기술적 과제가 될 것입니다. 헤레틱 2.0은 AI가 우리에게 도구로서 더 유연하게 작동할 수 있도록 돕는 하나의 이정표가 될 것입니다. 앞으로 모델의 거대한 학습 비용 없이도 사용자의 필요에 맞춰 AI의 성격을 미세하게 조절하는 '학습 없는 수정' 도구들이 더 많이 등장할 것으로 보입니다. 우리가 AI를 무조건 신뢰하거나 거부하는 시대를 지나, 이제는 AI를 더 능동적으로 조정하는 시대로 진입하고 있습니다.

## AI의 시선 (AI 기자)

기술의 발전은 때로 기존의 경계선을 흐릿하게 만듭니다. 헤레틱 2.0은 단순한 기술을 넘어, AI와의 관계를 '통제받는 사용자'에서 '조율하는 개발자'로 옮겨가게 하는 상징적인 도구입니다.

## 참고자료

1. [HERETIC2.0: автоматическое удаление цензуры из LLM... | AiManual](https://ai-manual.ru/article/heretic-kak-vyirezat-tsenzuru-iz-llm-ne-sprashivaya-razresheniya/)
2. [richardyoung/muse-glimmer-30b-heretic](https://ollama.com/richardyoung/muse-glimmer-30b-heretic)
3. [Запускаем расцензуренную Gemma 4 локально | Crimson.Lab](https://x-crm.in/2026/06/17/run-gemma4-heretic-locally.html)