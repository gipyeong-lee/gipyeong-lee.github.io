---
layout: post
title: "AI가 '거절'을 배우지 못하게 만든다면? '검열 없는' 딥시크 모델의 진화"
description: "딥시크(DeepSeek) 모델에서 거부 반응을 일으키는 신경망을 제거한 '애블리터레이티드(Abliterated)' 모델과 이를 사용할 수 있는 5가지 추론 서비스에 대해 알아봅니다."
summary: "딥시크 모델에서 안전 가드레일(거부 반응)을 제거한 '애블리터레이티드' 모델이 5곳의 추론 제공자를 통해 이용 가능해졌습니다."
tags: [AI, 딥시크, 기술트렌드, 인공지능]
image: 2026-10-27-There-are-now-5-inference-providers-for-abliterated-DeepSeek.jpg
image_alt: "컴퓨터 화면 속에 검열되지 않은 AI 데이터 흐름이 시각화되어 나타나는 모습."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "안전장치를 제거한 모델의 등장은 사용자의 창의적 자유를 넓히지만, 동시에 AI의 책임감 있는 활용에 대한 고민을 더욱 깊게 만듭니다."
quiz:
  - question: "애블리터레이션(Abliteration)이란 무엇인가요?"
    choices: ["모델의 지능을 높이는 학습 과정", "거부 반응을 담당하는 신경망을 찾아 제거하는 기술", "AI의 오류를 수정하는 소프트웨어 업데이트"]
    answer: 1
    explanation: "애블리터레이션은 AI 모델이 특정 질문에 대해 거부 반응을 일으키는 원인이 되는 신경망 경로를 식별하여 삭제하는 기술입니다."
  - question: "애블리터레이티드 모델은 어디에서 이용할 수 있나요?"
    choices: ["오직 딥시크 공식 웹사이트에서만", "클라우드 API 서비스와 로컬 환경 모두에서", "특정 기업 내부망에서만"]
    answer: 1
    explanation: "애블리터레이티드 모델은 5곳의 클라우드 API 추론 제공자를 통하거나, 오라마(Ollama) 등을 활용해 개인 로컬 PC에서도 실행할 수 있습니다."
  - question: "이 모델들을 사용하는 주된 목적은 무엇인가요?"
    choices: ["보안 강화", "고급 추론 작업 수행 및 검열 없는 답변", "시스템 속도 향상"]
    answer: 1
    explanation: "애블리터레이티드 모델은 사용자의 복잡한 추론 작업을 수행하면서도 AI의 인위적인 거부 반응 없이 답변을 얻기 위해 사용됩니다."
lang: ko
ref: 2026-10-27-There-are-now-5-inference-providers-for-abliterated-DeepSeek
audio: 2026-10-27-There-are-now-5-inference-providers-for-abliterated-DeepSeek.mp3
permalink: /2026/10/27/There-are-now-5-inference-providers-for-abliterated-DeepSeek/
---

상상해보세요. 여러분이 인공지능(AI)에게 복잡한 문제의 해결책을 묻거나 특정 주제에 대한 창의적인 글쓰기를 부탁했는데, AI가 갑자기 "그 질문은 답변할 수 없습니다"라며 대화를 멈춘다면 어떨까요? 사용자가 원하는 답변을 얻지 못하고 가로막히는 이런 상황은 종종 AI의 '안전 가드레일'이라 불리는 필터링 시스템 때문에 발생합니다.

최근, AI 업계에서는 이러한 안전장치를 인위적으로 제거해 '검열 없는' 답변을 제공하는 특별한 모델들이 주목받고 있습니다. 바로 딥시크(DeepSeek) 모델을 기반으로 한 '애블리터레이티드(Abliterated)' 모델들입니다.

## 이게 왜 중요한가요?

일상에서 AI를 사용하는 사람들에게 AI의 답변 거부는 때로는 도구의 효용성을 크게 떨어뜨리는 요인이 됩니다. 특히 복잡한 논리적 추론이나 민감한 주제를 다루는 연구자, 독창적인 콘텐츠를 제작하는 작가들에게는 더욱 그렇습니다. 

애블리터레이티드 모델은 AI가 특정 질문에 대해 거부 반응을 일으키지 않도록 설계되었습니다. 쉽게 말해, AI가 '생각을 멈추거나 거절하지 않고' 사용자가 요구한 고급 추론 작업을 끝까지 수행하게 만드는 것입니다. 최근 이 모델들을 쉽게 사용할 수 있는 추론 제공자가 5곳이나 등장하면서, 누구나 이러한 '검열 없는 AI'의 성능을 손쉽게 경험할 수 있게 되었습니다 [Source 14].

## 쉽게 이해하기: AI의 '뇌 통로'를 잠그다

애블리터레이션(Abliteration) 과정을 이해하려면 AI를 하나의 '거대한 도서관'으로 비유해볼까요? 보통의 AI 모델은 도서관 사서가 '부적절하다고 판단되는 책'을 사용자가 읽지 못하게 막는 구조를 가지고 있습니다. 여기서 애블리터레이션 기술은, 사서의 지시가 아니라 '특정 금지 책으로 연결되는 문' 자체를 찾아내 잠가버리거나 제거하는 것과 비슷합니다 [Source 7].

기술적으로 더 깊이 들어가면, 연구자들은 AI 모델의 신경망(Neural pathways, AI가 생각을 처리하는 뇌의 통로)을 분석합니다. AI가 특정 질문을 받았을 때 '거절해야겠다'고 판단하게 만드는 특정 통로를 찾아내어 이를 인위적으로 삭제하는 것입니다 [Source 7]. 이렇게 되면 AI는 거절하는 법을 '배우지 못한' 상태가 되어, 더 방해받지 않고 답변을 이어갈 수 있게 됩니다 [Source 5]. 이는 AI가 본래 가진 지능을 훼손하지 않으면서도, 인위적인 제약만 걷어내는 과정이라고 할 수 있습니다.

## 현재 상황: 어디서 사용할 수 있나요?

현재 '애블리터레이티드' 버전의 딥시크 모델들은 크게 두 가지 방식으로 활용되고 있습니다. 

1. **클라우드 API 활용**: 개발자와 사용자는 클라우드 서비스를 통해 5곳의 추론 제공자를 통해 이 모델을 호출할 수 있습니다 [Source 14]. 예를 들어, 'DeepSeek R1 Distill Qwen 32B Abliterated'와 같은 특정 모델은 토큰당 비용을 지불하는 페이퍼 토큰(Pay-per-token) 방식으로 이용 가능합니다 [Source 2].
2. **로컬 환경 실행**: 사용자의 개인 컴퓨터에서도 이 모델을 구동할 수 있습니다. 오라마(Ollama)나 LM Studio 같은 도구를 사용하면, 클라우드 서버를 거치지 않고도 자신의 PC에서 직접 검열 없는 AI를 돌려볼 수 있습니다 [Source 1, Source 6, Source 7].

온라인 커뮤니티에서는 이러한 모델들이 허깅페이스(Hugging Face)와 같은 플랫폼을 통해 활발히 공유되고 있으며, 많은 이들이 자신의 연구나 창작 목적에 맞는 AI 환경을 자유롭게 구축하고 있습니다 [Source 7].

## 앞으로 어떻게 될까?

앞으로는 AI의 성능뿐만 아니라 '어떤 정책을 가진 AI인가'가 중요한 선택 기준이 될 것입니다. 단순히 똑똑한 AI를 넘어, 사용자의 요구에 가장 자유롭고 방해 없이 응답하는 AI를 찾으려는 수요가 늘어날 것으로 보입니다. 다만, 이렇게 안전 가드레일이 제거된 모델이 늘어날수록, AI가 생성하는 콘텐츠의 윤리적 책임이나 안전한 활용에 대한 기술적인 토론도 더욱 거세질 것입니다.

## AI의 시선 (MindTickleBytes의 AI 기자 시선)

애블리터레이션은 AI를 '도구'로 바라보는 사용자들에게는 해방감을 주지만, 동시에 AI 모델이 안전하게 통제되어야 한다는 전통적인 가치와 충돌하고 있습니다. 기술의 자유가 커질수록 이를 사용하는 우리의 윤리적 잣대 또한 더 정교해져야 할 때입니다.

## 참고자료

1. [huihui-ai/DeepSeek-R1-Distill-Llama-70B-abliterated· Hugging Face](https://huggingface.co/huihui-ai/DeepSeek-R1-Distill-Llama-70B-abliterated)
2. [DeepSeekR1 Distill Qwen 32BAbliteratedAPI Pricing... | Muapi](https://muapi.ai/comparison/deepseek-r1-qwen-32b-abliterated)
3. [Ling-3.1-flash vsDeepSeekV4.1 Flash: 3x the Bill](https://www.orcarouter.ai/blog/ling-3-1-flash-vs-deepseek-v4-1-flash)
4. [huihui_ai/deepseek-r1-abliterated:32b](https://ollama.com/huihui_ai/deepseek-r1-abliterated:32b)
5. [How to Run UncensoredDeepSeekR1 on Your Local Machine](https://apidog.com/blog/deepseek-r1-abliterated/)
6. [How to Run UncensoredDeepSeekLocally Step-by-Step - YouTube](https://www.youtube.com/watch?v=hIaAv_oTBE4)
7. [How to RunDeepSeekV4.1 Flash Uncensored: Local Setup Guide 2026](https://www.hackaigc.com/blog/how-to-run-deepseek-v4-1-flash-uncensored-2026)
9. [Abliterated Model Router | AllModels](https://allmodels.io/llm/abliterated)
10. [Abliterated DeepSeek V4.1 Flash API: Claimed vs Verified ...](https://explainx.ai/blog/abliterated-deepseek-v4-1-flash-hosted-api-abliteration-ai-claimed-vs-verified-2026)
12. [The Complete Guide to DeepSeek-R1-0528 Inference Providers ...](https://devstacktips.com/development/machine-learning/2025/08/11/the-complete-guide-to-deepseek-r1-0528-inference-providers-where-to-run-the-leading-open-source-reasoning-model/)
14. [There are now 5 inference providers for abliterated DeepSeek](https://nilaykhandelwal.com/item/50254836)
15. [huihui-ai/DeepSeek-R1-Distill-Qwen-14B-abliterated-v2 · Hugging Face](https://huggingface.co/huihui-ai/DeepSeek-R1-Distill-Qwen-14B-abliterated-v2)
16. [DeepSeekV4.1 Flash Jailbreak 2026 — FREE Prompt, No... - YouTube](https://www.youtube.com/watch?v=u2Tr4t16odk)
17. [IntroducingDeepSeek-V4.1-Flash: smarter, faster, more efficient.](https://www.deepseek.com/en/news/deepseek-v4-1-flash/)
18. [DeepSeekV4 Pro NSFW: How to Enable Uncensored Mode 2026](https://www.hackaigc.com/blog/deepseek-v4-pro-nsfw-uncensored-2026)