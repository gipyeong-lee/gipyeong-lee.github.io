---
layout: post
title: "AI가 복잡한 결정을 한 번에 내린다고? 퍼플렉시티 '디시더 v1.3'의 비밀"
description: "퍼플렉시티가 공개한 오픈웨이트 멀티모달 결정 모델 '디시더 v1.3'의 성능, 분류·추출 능력, 그리고 비즈니스 활용법을 쉽게 알아봅니다."
summary: "퍼플렉시티가 분류, 라우팅, 스코어링, 정보 추출을 한 번에 수행하는 오픈웨이트 멀티모달 결정 모델 '디시더 v1.3'과 '디시더 플래시 v1.3'을 공개했습니다."
tags: [Perplexity, Decider, AI Models, Multimodal, Open-weight]
image: 2026-11-15-Perplexity-Decider-v13-Training-eval-and-use-cases.jpg
image_alt: "다양한 데이터와 문서를 한눈에 분석하고 분류하는 인공지능 결정 모델의 개념도를 표현한 일러스트"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "디시더 v1.3은 AI가 단순한 대화 상대에서 벗어나, 기업의 복잡한 의사결정과 데이터 분류 업무를 직접 수행하는 강력한 실무 파트너로 진화하고 있음을 보여줍니다."
quiz:
  - question: "퍼플렉시티가 이번에 공개한 결정 모델 v1.3 시리즈의 특징으로 올바른 것은?"
    choices: ["텍스트만 처리할 수 있다", "분류, 스코어링, 정보 추출을 한 번에 수행한다", "입력 데이터를 중간에 반드시 잘라낸다(Truncation)"]
    answer: 1
    explanation: "디시더 v1.3은 텍스트, 구조화된 JSON, 이미지를 바탕으로 분류, 라우팅, 스코어링, 정보 추출을 단 한 번의 패스로 처리할 수 있는 멀티모달 결정 모델입니다."
  - question: "디시더 v1.3이 63개의 쿼리 분류 태스크에서 기록한 평균 정확도는 얼마인가요?"
    choices: ["81.2%", "91.6%", "99.4%"]
    answer: 1
    explanation: "더 큰 모델 기준 63개의 쿼리 분류 태스크에서 91.6%의 평균 정확도를 기록하여 자사 프로덕션 분류기보다 뛰어난 성능을 입증했습니다."
  - question: "새롭게 추가된 디시더 v1.3의 핵심 기능 중 하나로, 텍스트에서 특정한 정보를 직접 콕 집어내는 능력은 무엇인가요?"
    choices: ["로케이트(Locate)", "트랜스레이트(Translate)", "컴파일(Compile)"]
    answer: 0
    explanation: "디시더 v1.3은 새롭게 도입된 '로케이트(Locate)' 기능을 통해 텍스트 속에서 특정한 정보를 직접 추출하는 능력을 갖추었습니다."
lang: ko
ref: 2026-11-15-Perplexity-Decider-v13-Training-eval-and-use-cases
audio: 2026-11-15-Perplexity-Decider-v13-Training-eval-and-use-cases.mp3
permalink: /2026/11/15/Perplexity-Decider-v13-Training-eval-and-use-cases/
---

상상해보세요. 수천 건의 고객 문의와 서류, 이미지가 쏟아지는 대규모 고객센터에서 담당 직원이 매번 이게 환불 요청인지, 단순 문의인지, 긴급 불만인지 분류하고 점수를 매기느라 녹초가 됩니다. 그런데 이 복잡하고 지루한 판단 작업을 단 몇 초 만에, 인간보다 더 정확하게 해치우는 AI가 등장했습니다. [퍼플렉시티(Perplexity, AI 기반 검색 및 대화형 플랫폼)](https://aiweekly.co/alerts/perplexity-ships-decider-v13-classifier-916-on-63-tasks)가 공개한 오픈웨이트(Open-weight, 누구나 내부 구조를 살펴보고 활용할 수 있는 공개 가중치 모델) 멀티모달(Multimodal, 텍스트뿐만 아니라 이미지, 소리 등 다양한 형태의 데이터를 동시에 이해하는 기술) 결정 모델 **'디시더 v1.3(Decider v1.3)'**과 **'디시더 플래시 v1.3(Decider Flash v1.3)'** 이야기입니다 [Source 2, Source 7].

이번 글에서는 퍼플렉시티가 내놓은 이 새로운 의사결정 AI가 왜 주목받고 있는지, 우리 일상과 비즈니스에 어떤 변화를 가져올지 차근차근 살펴보겠습니다.

---

## 이게 왜 중요한가요?

기업들이 AI를 비즈니스에 도입할 때 가장 골치 아픈 지점은 '판단과 결정'입니다. 비유하면, 거대한 공장에서 수많은 부품의 불량 여부를 일일이 수작업으로 검수하느라 멈춰 서 있는 것과 같습니다. "이 이메일이 스팸인가요?", "이 고객이 제출한 서류가 규정을 충족했나요?", "이 상품 리뷰는 긍정적인가요, 부정적인가요?" 같은 질문에 답하기 위해 기존에는 각각 다른 프로그램을 복잡하게 엮어야 했습니다.

하지만 [퍼플렉시티의 디시더 v1.3](https://aiweekly.co/alerts/perplexity-ships-decider-v13-classifier-916-on-63-tasks)은 63개의 쿼리 분류(Query-classification, 사용자의 질문이나 요청 의도를 유형별로 나누는 작업) 태스크에서 **평균 정확도 91.6%**를 기록하며, 기존 자사 프로덕션 분류기보다 6.54%포인트 높은 성능을 증명했습니다 [Source 2]. 

단순히 글을 읽고 대답하는 것을 넘어, **분류(Classification), 스코어링(Scoring, 점수 산정), 정보 추출(Extraction)**을 단 한 번의 패스로 처리할 수 있기 때문에 [Source 4, Source 6] 기업들은 훨씬 적은 비용으로 빠르고 정확한 자동화 시스템을 구축할 수 있게 됩니다.

---

## 쉽게 이해하기: 디시더 v1.3은 어떻게 일하나요?

쉽게 말해서, 디시더 v1.3은 마치 **'초고속 판사'** 또는 **'대형 도서관의 천재 사서'**에 비유할 수 있습니다. 

이 모델은 텍스트, 구조화된 JSON(데이터를 저장하고 교환하기 위한 경량의 텍스트 형식), 심지어 이미지까지 다양한 형태의 자료를 한꺼번에 받아들입니다 [Source 6]. 그리고 예/아니오 질문, 사용자가 미리 정한 맞춤 선택지, 순서가 있는 루브릭(Rubric, 평가 기준표)에 따라 철저하게 심사한 뒤 확률값과 함께 타이핑된 정답을 내놓습니다 [Source 6].

### 비유로 보는 핵심 기능
- **X-ray 보안 검색대**: 공항 검색대가 짐을 스캔하듯, 디시더 v1.3은 방대한 데이터 속에서 규정 위반이나 특정 항목을 오차 없이 골라냅니다.
- **새로운 '로케이트(Locate)' 기능**: 텍스트 속에서 특정한 정보를 직접 콕 집어내는 능력이 추가되었습니다 [Source 1, Source 7]. 마치 거대한 백과사전에서 특정 단어가 적힌 페甚至是 정확하게 칼로 도려내듯 찾아내는 기술입니다.

이 모든 과정이 하나의 모델 안에서 유기적으로 일어난다는 점이 기존 AI와 가장 큰 차이점입니다 [Source 4, Source 6].

---

## 현재 상황: 어디까지 와 있나?

[퍼플렉시티 데시더 v1.3](https://aiweekly.co/alerts/perplexity-ships-decider-v13-classifier-916-on-63-tasks)은 이전 버전인 v1, v1.1, v1.2, 그리고 Flash v1.2의 훌륭한 계보를 이어받아 탄생한 최신 모델입니다 [Source 2]. 현재 파악된 기술적 특징과 스펙은 다음과 같습니다.

1. **강력한 멀티모달 처리**: 텍스트뿐만 아니라 이미지와 구조화된 데이터까지 동시에 평가할 수 있습니다 [Source 6].
2. **방대한 컨텍스트 윈도우**: **256K(약 25만 6천 개)**라는 엄청난 컨텍스트 윈도우(Context window, AI가 한 번에 기억하고 처리할 수 있는 정보의 양)를 제공하여, 책 한 권 분량의 데이터를 통째로 넣고 분석할 수 있습니다 [Source 6].
3. **입력 데이터의 무손실 보존**: 학습 과정에서 최대 **30,720토큰(Token, AI가 문장을 읽고 처리하는 기본 단위)** 길이의 시퀀스를 사용했으며, 입력 데이터를 절대 중간에 자르지(Truncation) 않는 원칙을 고수합니다 [Source 9].
4. **유연한 질문 제한**: 질문의 개수에 고정된 제한이 없어, 허용된 길이 한도 내에서 한 번에 수많은 질문을 던질 수 있습니다 [Source 9].

개발자와 기업들은 오픈라우터(OpenRouter)나 브이셀(Vercel) AI 게이트웨이 등을 통해 이 모델을 손쉽게 테스트하고 API 형태로 가져다 쓸 수 있습니다 [Source 6, Source 8].

---

## 앞으로 어떻게 될까?

[퍼플렉시티](https://aiweekly.co/alerts/perplexity-ships-decider-v13-classifier-916-on-63-tasks)가 오픈웨이트 모델로 [디시더 v1.3과 디시더 플래시 v1.3](https://lapaasvoice.com/perplexity-open-sources-decider-v1.3-and-decider-flash-v1-3-with-new-locate-feature/)을 전격 개방함에 따라 [Source 2, Source 7], 앞으로 수많은 기업과 개발자들이 각자의 서비스에 이 '지능형 판단 엔진'을 이식할 것으로 보입니다.

고객센터의 자동 분류 시스템, 대규모 계약서 및 법률 문서 검토, 실시간 콘텐츠 모더레이션 등 '정확한 판단'이 비즈니스의 성패를 가르는 영역에서 디시더 v1.3은 핵심 인프라로 자리 잡을 전망입니다. AI가 단순히 말을 잘하는 것을 넘어, 진짜 '일잘러 참모'로 거듭나는 시계바늘이 빠르게 움직이고 있습니다.

---

## AI의 시선

MindTickleBytes의 AI 기자 시선: AI의 발전은 단순히 글을 잘 쓰는 것을 넘어, '올바른 판단'을 내리는 정밀함으로 진화하고 있습니다. 디시더 v1.3은 AI가 단순한 수다쟁이가 아니라, 비즈니스의 가장 까다로운 결정권자 곁에서 일하는 신뢰할 수 있는 참모가 될 수 있음을 증명합니다.

---

## 참고자료

1. [Perplexity Decider v1.3: Training, eval, and use cases](https://www.perplexity.ai/hub/blog/perplexity-decider)
2. [Perplexity Ships Decider v1.3 Classifier, 91.6% on 63 Tasks](https://aiweekly.co/alerts/perplexity-ships-decider-v13-classifier-916-on-63-tasks)
3. [Perplexity's Decider v1.3 lets one model · 21 HN comments | Zeli](https://zeli.app/story/50488464)
4. [Decider v1.3: Release, Decision Index Score, Performance ...](https://artificialanalysis.ai/decision-models/pplx-decider-v1-3)
5. [Decider V1.3 API, Pricing & Playground | Vercel AI Gateway](https://vercel.com/ai-gateway/models/pplx-decider-v1.3)
6. [Perplexity Open-Sources Decider v1.3 and Decider Flash v1.3 ...](https://lapaasvoice.com/perplexity-open-sources-decider-v1-3-and-decider-flash-v1-3-with-new-locate-feature/)
7. [DeciderV1.3(free) - API Pricing & Providers | OpenRouter](https://openrouter.ai/perplexity/pplx-decider-v1.3:free)
8. [perplexity-ai/pplx-decider-v1.3 · Hugging Face](https://huggingface.co/perplexity-ai/pplx-decider-v1.3)
9. [Perplexity Decider v1.2 27B Benchmarks & Pricing | BenchLM.ai](https://benchlm.ai/models/pplx-decider-v1.2)
10. [How To Use Decision Models for Evals – Hamel’s Blog](https://hamel.dev/blog/posts/decision-model-evals/)
11. [Perplexity Decider V1.2 API Pricing & Benchmarks | LMSpeed](https://lmspeed.net/model/pplx-decider-v1.2)