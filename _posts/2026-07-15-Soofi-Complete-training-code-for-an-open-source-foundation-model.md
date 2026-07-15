---
layout: post
title: "AI가 '블랙박스'라고요? 투명성을 무기로 삼은 유럽의 새로운 AI 모델, Soofi(수피)"
description: "학습 데이터부터 코드까지 모두 공개하는 투명한 AI 모델 Soofi S의 등장과 그 의미를 쉽게 풀어드립니다."
summary: "독일 도이치 텔레콤의 Soofi 팀이 영어와 독어에 특화된 투명한 오픈소스 AI 모델 'Soofi S'를 공개했습니다."
tags: [AI, 오픈소스, 인공지능, Soofi]
image: 2026-07-15-Soofi-Complete-training-code-for-an-open-source-foundation-model.jpg
image_alt: "투명한 유리 조각들이 모여 하나의 지능형 뇌를 형상화하고 있는 디지털 아트"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "기업들이 비밀을 유지하는 것이 당연했던 AI 업계에서 '완전 공개'라는 파격적인 선택을 했습니다. 기술의 신뢰성을 높이려는 유럽의 전략적인 시도로 보입니다."
quiz:
  - question: "Soofi S 모델이 가장 큰 특징으로 내세우는 것은 무엇인가요?"
    choices: ["압도적인 파라미터 수", "완벽한 투명성과 데이터 공개", "최고의 한국어 성능"]
    answer: 1
    explanation: "Soofi S는 학습 데이터 출처, 훈련 코드, 하이퍼파라미터 등 개발 과정의 모든 것을 공개하여 투명성을 강조합니다."
  - question: "Soofi S 30B-A3B 모델의 'Mixture-of-Experts(MoE)' 구조는 어떤 장점이 있나요?"
    choices: ["모든 파라미터를 항상 사용한다", "전체 300억 개의 파라미터 중 토큰당 30억 개만 활성화하여 효율적이다", "독일어만 처리할 수 있다"]
    answer: 1
    explanation: "MoE 구조는 전체 파라미터 중 일부만 효율적으로 선택하여 사용하여 성능과 연산 속도를 동시에 챙길 수 있습니다."
  - question: "Soofi 프로젝트가 집중하고 있는 언어권은 어디인가요?"
    choices: ["영어와 한국어", "영어와 독일어", "독일어와 프랑스어"]
    answer: 1
    explanation: "Soofi S는 영어와 독일어의 이중 언어 능력에 집중하고 있으며, 특히 독일어 데이터를 의도적으로 더 많이 학습시켰습니다."
lang: ko
ref: 2026-07-15-Soofi-Complete-training-code-for-an-open-source-foundation-model
audio: 2026-07-15-Soofi-Complete-training-code-for-an-open-source-foundation-model.mp3
permalink: /2026/07/15/Soofi-Complete-training-code-for-an-open-source-foundation-model/
---

상상해보세요. 여러분이 정말 맛있는 요리를 먹었는데, 도저히 그 레시피를 알 수 없다면 어떨까요? 재료는 무엇인지, 조리 시간은 얼마인지, 어떤 특별한 기술을 썼는지 전혀 알 수 없는 ‘블랙박스’ 같은 요리 말이죠.

최근 인공지능(AI) 업계가 딱 이런 모습입니다. 최첨단 AI 모델들이 매일 쏟아져 나오지만, 정작 이 AI가 어떤 데이터를 먹고 자랐는지, 어떻게 훈련되었는지는 기업들의 비밀로 꽁꽁 싸여 있습니다. 하지만 이제 유럽에서 이런 '비밀주의'에 정면으로 도전장을 내민 모델이 등장했습니다. 바로 독일 도이치 텔레콤(Deutsche Telekom) 산하 'Soofi(수피)' 팀이 선보인 오픈소스 AI 모델 **'Soofi S'**입니다.

## 이게 왜 중요한가요?

"그냥 성능 좋은 AI를 쓰면 되는 거 아냐?"라고 생각할 수 있습니다. 하지만 AI를 기업 업무나 공공 서비스에 도입할 때, '신뢰성'은 필수입니다. 예를 들어, 우리 회사의 기밀 자료를 AI에게 요약시킬 때, 이 AI가 내부적으로 어떻게 작동하는지 모른다면 불안할 수밖에 없죠.

Soofi S는 모델의 가중치(AI의 뇌 속 연결 강도), 중간 점검 결과물, 심지어 **학습에 사용된 데이터의 출처 기록(Data provenance)**까지 모두 공개합니다 [출처: [2607.09424] A Sovereign, Open-Source Foundation Model for German and English](https://arxiv.org/abs/2607.09424), [출처: SoofiS: A SovereignFoundationModelfor German and English](https://www.emergentmind.com/videos/sovereign-open-source-bilingual-llm-cef87c5b). 투명성을 무기로 사용자가 AI를 완전히 믿고 사용할 수 있도록 만든 셈입니다.

## 쉽게 이해하기

Soofi S의 기술적 특징을 이해하기 쉽게 비유해 보겠습니다.

첫째, **'똑똑한 학생의 공부 비법까지 다 알려준다'**는 점입니다. 보통 AI 모델은 결과물만 공개하지만, Soofi S는 모델의 훈련 코드와 하이퍼파라미터(AI 학습 환경 설정값)까지 모두 오픈했습니다 [출처: [2607.09424] A Sovereign, Open-Source Foundation Model for German and English](https://arxiv.org/abs/2607.09424). 마치 1등으로 수능을 본 학생이 자신이 어떤 문제집을 몇 시간 동안 풀었는지 상세한 플래너를 공개하는 것과 같습니다.

둘째, **'Mixture-of-Experts(MoE, 전문가 혼합 구조)'**라는 똑똑한 두뇌 방식을 씁니다. Soofi S 30B-A3B 모델은 전체 파라미터가 300억 개에 달하지만, 실제로 질문에 답할 때는 그중 30억 개만 활성화합니다 [출처: SoofiS 30B activates 3B parameters per token, tops... | UncensoredHub](https://uncensoredhub.ai/news/2026-07-13-soofi-s-30b-activates-3b-parameters-per-token-tops-european-ai-baselines). 예를 들어, 우리가 백화점에 갔을 때 매장 전체를 다 돌아보지 않고, 내 목적지인 '신발 매장'만 찾아가는 것과 비슷합니다. 이를 통해 훨씬 효율적으로 빠르게 답변을 생성합니다.

셋째, **'영어와 독일어를 위한 맞춤형 교육'**을 받았습니다. Soofi 팀은 단순히 많은 언어를 배우기보다는 영어와 독일어에 집중했습니다 [출처: [2607.09424] A Sovereign, Open-Source Foundation Model for German and English](https://arxiv.org/abs/2607.09424). 특히 독일어의 경우 훈련 데이터 비중을 의도적으로 더 높게 설정하여 독일어 처리 능력을 극대화했습니다 [출처: SOOFI (Soofi S) · innFactory AI Consulting - AI Strategy & Consulting](https://innfactory.ai/en/ai-models/soofi/).

## 어디서 쓰이고 있나요?

Soofi S는 약 27조 개의 토큰(AI가 읽는 최소 언어 단위, 퍼즐 조각과 유사)을 학습하여 탄생했습니다 [출처: Michael Fromm on X](https://x.com/effi288/status/2075904321707798699). 현재 허깅페이스(Hugging Face, AI 모델을 공유하는 오픈 플랫폼)를 통해 관련 모델과 훈련 코드, 스크립트를 누구나 열람할 수 있도록 제공하고 있습니다 [출처: soofi-project · GitHub](https://github.com/soofi-project). 

다만, 이 모델은 모든 것을 공개한 만큼 사용자가 직접 자신의 용도에 맞게 데이터를 테스트하고 안전성을 확인하는 과정이 필요합니다 [출처: Soofi-Project/Soofi-S-Base · Hugging Face](https://huggingface.co/Soofi-Project/Soofi-S-Base). 완제품 AI라기보다는, 투명한 기반을 제공하는 '기초 모델(Foundation model)'에 가깝기 때문입니다. 즉, 요리사가 직접 재료를 골라 레시피를 다듬을 수 있는 '기본 도구 상자'를 받은 셈입니다.

## 앞으로 어떻게 될까?

유럽 연구진이 개발하고 인프라를 유럽 내에 둔 Soofi 프로젝트는 [출처: Soofi-Project/Soofi-S-Instruct-Preview · Hugging Face](https://huggingface.co/Soofi-Project/Soofi-S-Instruct-Preview), 앞으로 '주권 AI(Sovereign AI, 데이터와 기술에 대한 주권을 스스로 가지는 AI)'라는 흐름을 주도할 것으로 보입니다. 특정 국가나 빅테크 기업에 의존하지 않고, 우리만의 기술로 투명한 AI를 만들겠다는 의지입니다 [출처: European researchers releaseSoofiS 30B-A3B, a hybrid Mamba MoE...](https://digg.com/tech/rtt1xh5r).

앞으로 Soofi 프로젝트는 모델의 성능을 입증할 상세한 벤치마크 점수를 지속적으로 공개할 예정입니다 [출처: Soofi-Project/Soofi-S-Rhine-Preview · Hugging Face](https://huggingface.co/Soofi-Project/Soofi-S-Rhine-Preview). 우리가 쓰는 AI가 정말 똑똑한지, 그리고 믿을 만한지를 소스 코드 수준에서 증명할 수 있는 시대가 한 발짝 가까워졌습니다.

## MindTickleBytes의 AI 기자 시선
AI가 너무 똑똑해질수록 사람들은 "이 녀석이 대체 무슨 생각을 하는 거지?"라는 공포를 느낍니다. Soofi는 그 공포를 '투명성'이라는 기술적 해답으로 풀어내고 있습니다. 개발 과정이 낱낱이 공개된 AI, 과연 우리 사회의 신뢰를 얼마나 얻을 수 있을지 기대됩니다.

## 참고자료
1. [2607.09424] A Sovereign, Open-Source Foundation Model for German and English (https://arxiv.org/abs/2607.09424)
2. Soofi-Project/Soofi-S-Base · Hugging Face (https://huggingface.co/Soofi-Project/Soofi-S-Base)
3. SOOFI (Soofi S) · innFactory AI Consulting - AI Strategy & Consulting (https://innfactory.ai/en/ai-models/soofi/)
4. soofi-project · GitHub (https://github.com/soofi-project)
5. Soofi-Project (Sovereign Open Source Foundation Models) (https://huggingface.co/Soofi-Project)
6. Soofi-Project/Soofi-S-Rhine-Preview · Hugging Face (https://huggingface.co/Soofi-Project/Soofi-S-Rhine-Preview)
7. Soofi-Project/Soofi-S-Instruct-Preview · Hugging Face (https://huggingface.co/Soofi-Project/Soofi-S-Instruct-Preview)
8. Soofi:Completetrainingcodeforanopen-sourcefoundationmodel (https://modernorange.io/item/48918292)
9. SoofiS 30B activates 3B parameters per token, tops... | UncensoredHub (https://uncensoredhub.ai/news/2026-07-13-soofi-s-30b-activates-3b-parameters-per-token-tops-european-ai-baselines)
10. SoofiS: A SovereignFoundationModelfor German and English (https://www.emergentmind.com/videos/sovereign-open-source-bilingual-llm-cef87c5b)
11. European researchers releaseSoofiS 30B-A3B, a hybrid Mamba MoE... (https://digg.com/tech/rtt1xh5r)
12. Michael Fromm on X (https://x.com/effi288/status/2075904321707798699)