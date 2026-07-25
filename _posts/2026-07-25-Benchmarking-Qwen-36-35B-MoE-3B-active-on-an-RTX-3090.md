---
layout: post
title: "내 컴퓨터에서 AI가 쌩쌩 달린다고? Qwen 3.6 35B MoE로 알아보는 로컬 AI의 세계"
description: "고성능 AI 모델인 Qwen 3.6 35B MoE를 RTX 3090 그래픽카드에서 직접 돌려본 성능 테스트 결과와 로컬 AI 활용법을 쉽게 설명합니다."
summary: "RTX 3090에서 Qwen 3.6 35B-A3B 모델을 실행하면 초당 100개 이상의 토큰을 생성할 수 있어, 일반적인 27B 밀집 모델보다 훨씬 빠른 속도를 경험할 수 있습니다."
tags: [AI, 로컬LLM, Qwen, RTX3090, 하드웨어]
image: 2026-07-25-Benchmarking-Qwen-36-35B-MoE-3B-active-on-an-RTX-3090.jpg
image_alt: "RTX 3090 그래픽카드 위에서 구동되는 Qwen 3.6 AI 모델의 성능을 측정하는 모습."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "로컬 환경에서 대규모 모델을 효율적으로 구동하는 것은 데이터 프라이버시와 비용 측면에서 엄청난 이점입니다. 특히 MoE 구조를 활용하면 하드웨어 제약을 영리하게 극복할 수 있습니다."
quiz:
  - question: "MoE(Mixture-of-Experts) 구조의 모델이 일반적인 밀집 모델보다 빠른 이유는 무엇일까요?"
    choices: ["모든 매개변수를 항상 사용하기 때문에", "한 번에 3B(30억) 정도의 활성 매개변수만 처리하기 때문에", "RTX 3090에 최적화된 코드만 들어있기 때문에"]
    answer: 1
    explanation: "MoE 모델은 전체 모델 중 일부 전문가(매개변수)만 골라 작동하므로, 35B 크기 모델이라도 3B 정도의 활성 매개변수만 사용해 연산 속도가 빠릅니다 [Source 5]."
  - question: "RTX 3090에서 Qwen 3.6 35B-A3B 모델을 실행할 때 나타나는 성능은 어느 정도인가요?"
    choices: ["초당 5~10개 토큰", "초당 50~100개 이상의 토큰", "초당 1,000개 이상의 토큰"]
    answer: 1
    explanation: "테스트 결과에 따라 다르지만, 설정에 따라 초당 50개에서 100개 이상의 토큰 생성 속도를 보여줍니다 [Source 2], [Source 5], [Source 7]."
  - question: "성능이 더 높은 27B 밀집 모델과 35B-A3B MoE 모델 중 하나를 선택해야 한다면?"
    choices: ["무조건 35B 모델이 우수함", "답변 품질이 중요하다면 27B 밀집 모델을 추천함", "둘 다 성능 차이가 전혀 없음"]
    answer: 1
    explanation: "27B 밀집 모델은 벤치마크 결과에서 MoE 모델보다 1~10점 정도 앞서기 때문에 답변 품질이 우선일 때 권장됩니다 [Source 3]."
lang: ko
ref: 2026-07-25-Benchmarking-Qwen-36-35B-MoE-3B-active-on-an-RTX-3090
audio: 2026-07-25-Benchmarking-Qwen-36-35B-MoE-3B-active-on-an-RTX-3090.mp3
permalink: /2026/07/25/Benchmarking-Qwen-36-35B-MoE-3B-active-on-an-RTX-3090/
---

상상해보세요. 여러분이 매일 사용하는 컴퓨터에 있는 AI 비서가, 인터넷 연결 없이도 아주 복잡한 질문에 1초 만에 척척 대답해준다면 어떨까요? 개인정보 유출 걱정 없이, 내 컴퓨터 안에서만 안전하게 돌아가는 '나만의 AI'를 갖는 것은 더 이상 공상과학 영화 속 이야기가 아닙니다. 최근 출시된 강력한 AI 모델인 'Qwen 3.6 35B-A3B'가 이를 어떻게 현실로 만들어주는지, 고등학생도 이해할 수 있도록 쉽게 풀어서 설명해 드립니다.

### 이게 왜 중요한가요? (Why It Matters)

과거의 고성능 AI 모델들은 덩치가 너무 커서 일반 사용자의 컴퓨터로는 돌릴 엄두조차 내기 어려웠습니다. 하지만 이제는 상황이 달라졌습니다. '로컬 AI(인터넷 연결 없이 사용자의 기기에서 직접 작동하는 AI)' 기술이 비약적으로 발전하면서, 집에 있는 RTX 3090 같은 그래픽카드만으로도 수준 높은 AI를 충분히 경험할 수 있게 된 것입니다 [Source 8].

로컬 AI가 주목받는 이유는 크게 두 가지입니다. 첫째는 **프라이버시**입니다. 내 데이터가 외부 서버로 나가지 않고 내 컴퓨터 안에서만 처리되니 훨씬 안심할 수 있습니다. 둘째는 **속도와 경제성**입니다. 인터넷 속도에 영향을 받지 않아 끊김이 없고, 모델을 한 번 내려받기만 하면 추가 비용 없이 마음껏 쓸 수 있습니다. 이번에 테스트한 Qwen 3.6 35B-A3B 모델은 이러한 로컬 AI 환경에서 특히 뛰어난 가성비와 성능을 보여주며 많은 관심을 받고 있습니다 [Source 6].

### 쉽게 이해하기 (The Explainer)

Qwen 3.6 35B-A3B 모델의 핵심은 **MoE(Mixture-of-Experts, 전문가 혼합 구조)**라는 특별한 설계에 있습니다. 

쉽게 비유해볼까요? 여러분이 거대한 도서관을 운영하는데, 모든 책을 한 명의 사서가 다 관리하려면 너무 힘듭니다. 그래서 분야별 전문가 사서를 여러 명 고용했다고 상상해보세요. 여기서 '35B'는 총 사서들의 수(전체 매개변수)를 의미하고, '3B active'는 질문이 들어왔을 때 실제로 답을 찾기 위해 호출하는 사서의 수(활성 매개변수)를 뜻합니다 [Source 5].

일반적인 '밀집 모델(Dense Model)'이 모든 사서가 매번 일을 하는 구조라면, MoE 모델은 질문의 내용에 따라 딱 필요한 분야의 사서들만 일을 합니다. 덕분에 모델은 350억 개의 매개변수를 가진 만큼 아주 똑똑하지만, 실제 머리를 쓸 때는 30억 개의 매개변수만큼만 계산하면 되어 아주 빠르게 결과를 내놓을 수 있는 것입니다 [Source 5].

### 현재 상황 (Where We Stand)

최근 실제 RTX 3090 그래픽카드에서 진행한 벤치마크 테스트 결과는 놀랍습니다.

* **속도**: 특정 설정(UD-Q4_K_XL 양자화)을 적용했을 때, 짧은 질문에는 초당 약 101.7개의 토큰(AI가 글자를 만드는 단위)을, 긴 질문에는 80.9개의 토큰을 생성해냅니다 [Source 7]. 다른 환경에서도 초당 50~100개 토큰 수준을 꾸준히 유지하는데, 이는 27B 밀집 모델(초당 약 35개 토큰)보다 훨씬 빠른 속도입니다 [Source 5].
* **한계**: 물론 무조건 덩치가 크고 빠른 MoE 모델이 정답은 아닙니다. 27B 밀집 모델과 비교했을 때, 답변의 정확도(품질) 면에서는 27B 밀집 모델이 1~10점 정도 더 높은 벤치마크 결과를 보여줍니다 [Source 3]. 즉, 속도가 가장 중요하다면 MoE 모델을, 답변의 품질이 가장 중요하다면 밀집 모델을 선택하는 것이 현명합니다 [Source 3].
* **최적화**: 또한, AI 학습 기법 중 하나인 '추론 가속 기법(Speculative Decoding)'은 의외로 RTX 3090과 같은 환경에서는 속도 향상에 큰 도움이 되지 않는 것으로 확인되었습니다 [Source 4].

### 앞으로 어떻게 될까? (What's Next)

앞으로 로컬 AI 기술은 지금보다 더 가벼워지고, 더 똑똑해질 것입니다. 이번 테스트를 진행한 전문가들은 사용자의 PC 사양에 맞춰 모델을 효율적으로 구동할 수 있는 다양한 설정법들을 공유하고 있습니다 [Source 3], [Source 11]. 이제 사용자는 단순히 좋은 모델을 고르는 수준을 넘어, 자신의 그래픽카드 성능에 맞는 최적의 '양자화(데이터의 정밀도를 조절해 크기를 줄이는 기술)' 수준을 선택하여 자신만의 AI 환경을 직접 튜닝하는 시대를 맞이하고 있습니다 [Source 2], [Source 14].

### MindTickleBytes의 AI 기자 시선

로컬 AI는 단순히 기술적인 성취를 넘어 '내 기기의 주권'을 되찾는 과정입니다. Qwen 3.6 35B-A3B 같은 효율적인 모델의 등장은 고가의 서버 없이도 누구나 자신의 PC에서 고성능 AI를 누릴 수 있는 미래를 성큼 앞당기고 있습니다. 이제 AI는 멀리 있는 거대 기업의 서버가 아니라, 바로 여러분의 책상 위 컴퓨터 안에서 함께 호흡하는 존재가 되어가고 있습니다.

## 참고자료

1. [Qwen/Qwen3.6-35B-A3B · My RTX 3090 ran out of excuses: Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B/discussions/37)
2. [Qwen 3.6-35B-A3B Local Hardware Guide — GPU & VRAM (2026) | Compute Market](https://www.compute-market.com/blog/qwen-3-6-local-hardware-guide-2026)
3. [GitHub - tfriedel/qwen3.6-rtx3090-lab: Benchmarks, compose files, and findings for running Qwen3.6 (27B dense + 35B-A3B MoE) on 4× RTX 3090](https://github.com/tfriedel/qwen3.6-rtx3090-lab)
4. [GitHub - thc1006/qwen3.6-speculative-decoding-rtx3090](https://github.com/thc1006/qwen3.6-speculative-decoding-rtx3090)
5. [Best Way to Run Qwen 3.6 35B MoE Locally: VRAM, Speed, Setup | InsiderLLM](https://insiderllm.com/guides/best-way-run-qwen-3-6-35b-moe-locally/)
6. [I Benchmarked Qwen3.6–35B-A3B Model on 3090, 4090, 5090 and M5 Max. Here’s What Nobody Tells You. | Medium](https://medium.com/@ttio2tech_28094/i-benchmarked-qwen3-6-35b-a3b-model-on-3090-4090-5090-and-m5-max-heres-what-nobody-tells-you-62fbb2f4e64a)
7. [Qwen 3.6 Complete Guide: 27B Dense, 35B-A3B MoE, and Which to Use | InsiderLLM](https://insiderllm.com/guides/qwen-3-6-local-ai-guide/)
8. [Benchmarking Qwen 3.6 35B MoE (3B active) on an RTX 3090](https://www.gilesthomas.com/2026/07/benchmarking-qwen-3-6-35b-moe-rtx-3090)
9. [From 25 to 283 tok/s: Serving Qwen3.6 on Dual RTX 3090s](https://alexander-ollman.github.io/qwen3.6-on-rtx3090/qwen3.6-on-rtx3090.html)
10. [Qwen3.614B A3BFableVibes benchmarked and tested vs... - YouTube](https://www.youtube.com/watch?v=DBEd5dpxaNQ)
11. [Qwen/Qwen3.6-35B-A3B· Hugging Face](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)
12. [Qwen3.635B-A3BonRTX3060 12GB: Local LLM | SpecPicks](https://specpicks.com/reviews/qwen-36-35b-a3b-rtx-3060-12gb-local-2026)
13. [ЗапускаемQwen3.635B-A3B+ opencode локально наRTX... / Хабр](https://habr.com/ru/articles/1026482/)
14. [Qwen3.627B vs35B-A3BMoEMTP наRTX5080 16GB... | AiManual](https://ai-manual.ru/article/rtx-5080-16gb-qwen36-27b-mtp-ili-35b-a3b-moe-mtp---chto-vyibrat-dlya-lokalnogo-kodinga/)