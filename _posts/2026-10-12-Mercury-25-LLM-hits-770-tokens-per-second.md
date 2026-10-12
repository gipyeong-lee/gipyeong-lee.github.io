---
layout: post
title: "AI가 내 말보다 더 빨리 대답한다고? 초고속 언어모델 '머큐리 2.5' 이야기"
description: "인셉션 랩스(Inception Labs)가 공개한 초고속 확산형 AI 모델 '머큐리 2.5(Mercury 2.5)'의 성능과 특징을 알기 쉽게 설명합니다."
summary: "초당 770~1,107개의 토큰을 생성하는 초고속 AI '머큐리 2.5'의 등장으로 실시간 대화형 AI 서비스의 반응 속도가 획기적으로 개선될 전망입니다."
tags: [AI, 머큐리2.5, 인공지능, LLM]
image: 2026-10-12-Mercury-25-LLM-hits-770-tokens-per-second.jpg
image_alt: "데이터가 빠르게 흐르는 디지털 네트워크를 형상화한 그래픽 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "머큐리 2.5는 단순히 속도만 빠른 것이 아니라, 확산 모델 기반의 병렬 처리라는 새로운 기술적 돌파구를 보여줍니다. 이는 AI가 인간의 대화 속도를 완전히 추월하는 시대가 열렸음을 의미합니다."
quiz:
  - question: "머큐리 2.5가 기존 모델 대비 가지는 가장 큰 특징은 무엇인가요?"
    choices: ["훨씬 저렴한 가격", "압도적인 텍스트 생성 속도", "오프라인 전용 구동"]
    answer: 1
    explanation: "머큐리 2.5는 초당 770개에서 1,107개에 이르는 토큰을 생성하며, 기존 모델 대비 약 7배 빠른 속도를 기록했습니다."
  - question: "머큐리 2.5는 어떤 기술 방식을 기반으로 하나요?"
    choices: ["변환기(Transformer) 전용 모델", "확산(Diffusion) 기반 모델", "순차적 단순 연산 모델"]
    answer: 1
    explanation: "머큐리 2.5는 인셉션 랩스에서 개발한 확산 기반의 대형 언어 모델(dLLM)입니다."
  - question: "머큐리 2.5의 문맥 파악 범위(Context Window)는 얼마인가요?"
    choices: ["26만 토큰", "10만 토큰", "50만 토큰"]
    answer: 0
    explanation: "머큐리 2.5는 260,000 토큰의 대규모 문맥 파악 범위를 지원합니다."
lang: ko
ref: 2026-10-12-Mercury-25-LLM-hits-770-tokens-per-second
audio: 2026-10-12-Mercury-25-LLM-hits-770-tokens-per-second.mp3
permalink: /2026/10/12/Mercury-25-LLM-hits-770-tokens-per-second/
---

상상해보세요. 친구와 메신저로 대화를 나누는데, 친구가 내 질문이 끝나기도 전에 정답을 말하고, 내가 보낸 긴 글을 1초 만에 요약해서 돌려줍니다. 마치 사람이 아니라, 나와 똑같은 속도로 생각하는 누군가가 옆에 있는 것 같겠죠.

최근 인공지능(AI) 업계에서 이런 일이 현실이 되고 있습니다. 인셉션 랩스(Inception Labs)가 내놓은 새로운 언어모델, '머큐리 2.5(Mercury 2.5)'가 그 주인공입니다. 단순히 똑똑한 것을 넘어, '빛의 속도'로 대답하는 이 모델이 우리 일상을 어떻게 바꿀지 살펴보겠습니다. [출처: 인셉션 랩스 블로그](https://www.inceptionlabs.ai/blog/introducing-mercury-2-5)

### 이게 왜 중요한가요? (Why It Matters)

우리가 평소 쓰는 AI 챗봇은 대답을 내놓을 때 가끔 '생각하는 시간'이 필요합니다. 화면에 글자가 한 글자씩 '타닥타닥' 나타나는 것을 본 적 있으시죠? 이는 AI가 순차적으로 단어를 만들어내기 때문입니다.

하지만 머큐리 2.5는 이 속도의 판도를 완전히 뒤집었습니다. 인공지능 분석 기업인 'Artificial Analysis'의 측정에 따르면, 이 모델은 초당 약 770.4개의 토큰(AI가 글자를 처리하는 최소 단위)을 생성합니다. [출처: 샘 코드맨](https://www.samcodeman.com/writing/mercury-2-5-770-tokens-per-second-benchmark) 개발사 보고에 따르면 특정 환경에서는 초당 1,107개까지도 가능하다고 합니다. [출처: 프라다](https://www.pradha.id/read/mercury-25-inceptions-push-for-high-speed-diffusion-llms) 이는 기존 AI 모델보다 무려 7배나 빠른 수치입니다. [출처: AIPULSEN](https://aipulsen.com/artikel/14260)

쉽게 말해서, 기존 AI가 7초 동안 고민할 분량을 머큐리 2.5는 단 1초 만에 끝내는 셈입니다. 이런 속도가 실현되면 우리가 AI와 음성으로 대화할 때 느끼던 미세한 지연 시간(Latency)이 사라집니다. 실시간 통역기나 코딩 도우미가 마치 실제 사람처럼 즉각적으로 반응하게 되는 것이죠. [출처: TechBriefe](https://techbriefe.com/tech/ai/mercury-25-llm-achieves-770-tokens-per-second-in-inference-speed)

### 쉽게 이해하기 (The Explainer)

기존의 대형 언어 모델(LLM)들은 '변환기(Transformer, 문장의 단어들 사이 관계를 파악하는 AI 구조)'라는 방식을 주로 썼습니다. 이는 책을 첫 문장부터 끝까지 순서대로 정직하게 읽는 것과 비슷해서 속도에 분명한 한계가 있었습니다.

반면, 머큐리 2.5는 '확산(Diffusion)' 방식이라는 독특한 기술을 사용합니다. [출처: 오픈라우터](https://openrouter.ai/inception/mercury-2-5) 비유하자면, 기존 AI가 소설을 한 글자씩 써 내려가는 '성실한 작가'라면, 머큐리 2.5는 화가가 그림을 그릴 때처럼 전체 구도를 먼저 잡고 상세 내용을 한꺼번에 채워 넣는 '능숙한 화가'에 가깝습니다.

이 기술을 전문 용어로 '병렬 토큰 생성 및 정제(Parallel token generation and refinement)'라고 부릅니다. 여러 단어를 동시에 고민하고 다듬기 때문에 훨씬 빠르게 결과물을 내놓을 수 있는 것이죠. [출처: 벤처블](https://benchable.ai/models/inception/mercury-2.5-20260908)

### 현재 상황 (Where We Stand)

현재 머큐리 2.5는 단순히 빠르기만 한 것이 아니라, 260,000 토큰이라는 거대한 문맥 파악 범위(Context Window)를 갖추고 있습니다. [출처: 블로그 빌드 패스트 위드 AI](https://blog.buildfastwithai.com/mercury-2-5-ai-model-review) 이는 두꺼운 책 수십 권 분량의 정보를 한 번에 읽고 기억할 수 있다는 뜻입니다. 또한 구조화된 데이터 출력, 도구 활용, 복잡한 논리적 추론까지 가능해 실무적인 활용도가 높습니다. [출처: 블로그 빌드 패스트 위드 AI](https://blog.buildfastwithai.com/mercury-2-5-ai-model-review)

다만, 기술적 수치는 측정 방식에 따라 차이가 있을 수 있고, 매우 복잡한 전문적 작업에서 기존의 거대 모델들과 비교해 실질적인 성능 우위를 가지는지에 대해서는 사용자들의 검증이 더 필요한 단계입니다. [출처: 6ic](https://6ic.com/news/mercury-25-llm-achieves-770-tokens-per-second-setting-new-benchmark-for-speed)

### 앞으로 어떻게 될까? (What's Next)

앞으로 AI 서비스들은 '얼마나 똑똑한가'를 넘어 '얼마나 빨리 반응하는가'로 경쟁하게 될 것입니다. 특히 음성 비서나 실시간 상담, 게임 내 NPC(비플레이어 캐릭터) 등 즉각적인 반응이 중요한 분야에서 머큐리 2.5와 같은 모델들의 활약이 기대됩니다. [출처: 콜 미스드](https://www.callmissed.com/blog/mercury-diffusion-llm-770-tok-voice-latency) 여러분의 스마트폰 속에 더 빠르게 반응하는 AI 비서가 탑재되어, 질문을 던지자마자 대답을 듣는 날이 머지않아 보입니다.

---

## 참고자료
1. 샘 코드맨, [머큐리 2.5 770 토큰/초 벤치마크](https://www.samcodeman.com/writing/mercury-2-5-770-tokens-per-second-benchmark)
2. 6ic, [머큐리 2.5 LLM 초당 770 토큰 달성](https://6ic.com/news/mercury-25-llm-achieves-770-tokens-per-second-setting-new-benchmark-for-speed)
3. 프라다, [머큐리 2.5: 인셉션의 초고속 확산형 LLM](https://www.pradha.id/read/mercury-25-inceptions-push-for-high-speed-diffusion-llms)
4. 테크브리프(TechBriefe), [머큐리 2.5 LLM 추론 속도 초당 770 토큰 달성](https://techbriefe.com/tech/ai/mercury-25-llm-achieves-770-tokens-per-second-in-inference-speed)
5. VK.ru, [머큐리 2.5 LLM 초당 770 토큰 도달](https://vk.ru/wall-238001904_6156)
6. 인셉션 랩스, [머큐리 2.5 소개](https://www.inceptionlabs.ai/blog/introducing-mercury-2-5)
7. 쿠날 강글라니, [머큐리 2.5 770 토큰/초 벤치마크 (2026)](https://www.kunalganglani.com/blog/mercury-2-5-770-tokens-benchmark)
8. 블로그 빌드 패스트 위드 AI, [머큐리 2.5 AI 모델 리뷰](https://blog.buildfastwithai.com/mercury-2-5-ai-model-review)
9. AIPULSEN, [머큐리 2.5 LLM 초당 770 토큰 달성](https://aipulsen.com/artikel/14260)
10. 콜 미스드(CallMissed), [머큐리 2.5 확산형 LLM](https://www.callmissed.com/blog/mercury-diffusion-llm-770-tok-voice-latency)
11. 벤처블(Benchable), [인셉션: 머큐리 2.5 AI 모델 상세 정보 및 벤치마크](https://benchable.ai/models/inception/mercury-2.5-20260908)
12. 텔레그램(Hacker News Feed), [머큐리 2.5 LLM 초당 770 토큰 도달](https://t.me/hacker_news_feed/132200)
13. 오픈라우터(OpenRouter), [머큐리 2.5 API 가격 및 벤치마크](https://openrouter.ai/inception/mercury-2.5)