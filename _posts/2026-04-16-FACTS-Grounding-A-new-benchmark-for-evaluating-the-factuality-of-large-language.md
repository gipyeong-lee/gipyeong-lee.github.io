---
layout: post
title: "AI는 왜 자꾸 '아는 척'을 할까? 구글 딥마인드가 만든 AI 거짓말 탐지기 'FACTS'"
description: "AI의 할루시네이션(거짓말) 문제를 해결하기 위해 구글 딥마인드가 내놓은 새로운 팩트 체크 시스템 'FACTS Grounding'을 소개합니다."
summary: "구글 딥마인드가 AI의 답변이 제공된 문서에 얼마나 충실한지 측정하는 'FACTS Grounding' 벤치마크를 공개하며, AI의 신뢰성을 높이기 위한 새로운 기준을 제시했습니다."
tags: [AI, 구글딥마인드, 벤치마크, 할루시네이션, 팩트체크]
image: 2026-04-16-FACTS-Grounding-A-new-benchmark-for-evaluating-the-factuality-of-large-language.jpg
image_alt: "AI가 돋보기를 들고 수많은 문서 사이에서 진실을 찾아내는 모습을 형상화한 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI의 발전은 똑똑해지는 것만큼이나 '정직해지는 것'이 중요합니다. FACTS는 AI가 정직한 비서로 거듭나기 위한 가장 혹독한 시험대가 될 것입니다. 우리 인간도 가끔 기억을 왜곡하듯 AI도 '그럴싸함'의 함정에 빠지곤 하지만, 이런 엄격한 잣대가 결국 AI를 믿음직한 파트너로 만들어줄 것입니다."
quiz:
  - question: "FACTS Grounding 벤치마크가 주로 측정하는 AI의 능력은 무엇인가요?"
    choices: ["시를 얼마나 아름답게 쓰는가", "제공된 문서에 근거하여 얼마나 정확하게 답변하는가", "코딩 속도가 얼마나 빠른가"]
    answer: 1
    explanation: "FACTS Grounding은 AI가 주어진 문서(Context)에 충실하게 답변하고 근거 없는 거짓말을 하지 않는지(Grounding)를 측정합니다."
  - question: "FACTS 벤치마크에서 사용하는 AI의 답변 정확도를 검증하는 방식은 무엇인가요?"
    choices: ["작가가 직접 읽어보기", "3인 판사(3-judge) 평가 방식", "단어 개수 세기"]
    answer: 1
    explanation: "구글 딥마인드는 AI의 사실 관계를 정밀하게 확인하기 위해 '3-judge' 평가 방식을 사용합니다."
  - question: "현재 최고 수준의 AI 모델인 제미나이 3 프로(Gemini 3 Pro)가 FACTS에서 받은 점수는 대략 얼마인가요?"
    choices: ["99.9%", "68.8%", "20.5%"]
    answer: 1
    explanation: "현재 가장 뛰어난 모델 중 하나인 제미나이 3 프로도 FACTS 벤치마크에서는 약 68.8%의 점수를 기록하고 있습니다."
lang: ko
ref: 2026-04-16-FACTS-Grounding-A-new-benchmark-for-evaluating-the-factuality-of-large-language
audio: 2026-04-16-FACTS-Grounding-A-new-benchmark-for-evaluating-the-factuality-of-large-language.mp3
permalink: /2026/04/16/FACTS-Grounding-A-new-benchmark-for-evaluating-the-factuality-of-large-language/
---

상상해보세요. 당신이 아주 중요한 업무를 위해 비서에게 50페이지짜리 긴 보고서를 건네주며 요약을 부탁했습니다. 잠시 후 비서는 아주 깔끔하고 논리적인 요약본을 가져왔습니다. 그런데 자세히 읽어보니, 보고서 어디에도 없는 매출 수치가 적혀 있습니다. 당황해서 비서에게 물으니 "그 수치가 들어가야 보고서가 더 그럴듯해 보여서 적어 넣었다"라고 천연덕스럽게 대답합니다. 

이런 황당한 현상을 AI 업계에서는 **할루시네이션(Hallucination, 인공지능이 마치 환각을 보듯 그럴듯한 거짓말을 지어내는 현상)**이라고 부릅니다. [출처 제목](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/) 인공지능이 아무리 똑똑해져도 이 '아무 말 대잔치' 문제는 여전히 해결하기 어려운 숙제로 남아 있습니다. [출처 제목](https://winbuzzer.com/2024/12/18/googles-new-facts-benchmark-measures-truthfulness-of-ai-models-xcxwbn/) 

하지만 최근 구글 딥마인드(Google DeepMind)가 이 문제를 정면으로 돌파하기 위해 새로운 무기를 꺼내 들었습니다. 바로 AI가 얼마나 정직하게 주어진 문서에 근거해서 답변하는지를 정밀하게 측정하는 시험대, **'FACTS Grounding'** 벤치마크입니다. [출처 제목](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/)

## 왜 이게 중요한가요?

우리가 AI를 믿고 쓰려면 AI가 하는 말이 진짜인지 가짜인지 확실히 알 수 있어야 합니다. 특히 법률, 의료, 비즈니스처럼 작은 실수 하나가 큰 사고로 이어지는 분야에서는 AI의 지능보다 '정직함'이 훨씬 더 중요합니다.

지금까지의 AI 평가는 '말을 얼마나 유창하게 잘하는지'에 집중해 왔습니다. 하지만 이제는 '말의 근거가 얼마나 확실한지'를 따져야 할 때입니다. 여기서 핵심 키워드는 바로 **그라운딩(Grounding, 답변의 근거를 주어진 정보에 단단히 고정하는 기술)**입니다. 쉽게 말해서 AI가 자신의 기억이나 상상력이 아니라, 사용자가 준 자료 안에서만 답을 찾도록 발을 묶어두는 아주 중요한 기술입니다. [출처 제목](https://arxiv.org/abs/2501.03200) [출처 제목](https://api.emergentmind.com/topics/facts-grounding-benchmark/)

구글 딥마인드가 공개한 FACTS Grounding은 AI가 긴 문서를 읽고 답변할 때 얼마나 딴소리를 하지 않고 문서 내용에만 충실한지(High-fidelity attribution)를 꼼꼼하게 따져 묻습니다. [출처 제목](https://api.emergentmind.com/topics/facts-grounding-benchmark/)

## 더 쉽게 이해하기: AI를 위한 '초고난도 오픈북 테스트'

FACTS Grounding을 비유하자면, AI에게 **'초고난도 오픈북 테스트'**를 치르게 하는 것과 같습니다. 일반적인 AI 시험이 AI가 평소에 공부한 지식을 뽐내는 '수능 시험'이라면, FACTS는 옆에 두꺼운 백과사전을 한 권 주고 "다른 데 보지 말고 오직 이 책 안에서만 답을 찾아라"라고 명령하는 시험입니다.

### 1. 50페이지를 한 번에 읽는 집중력
이 시험에서 AI는 최대 **32,000개의 토큰(Token, AI가 문장을 이해하는 최소 단위)**에 달하는 긴 문서를 받습니다. [출처 제목](https://llm-stats.com/benchmarks/facts-grounding/) [출처 제목](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_grounding_paper.pdf/) 이는 종이 책으로 치면 약 40~50페이지 정도 되는 방대한 분량입니다. 비유하자면 소설책 한 권의 절반 정도를 한눈에 훑고, 그 안의 세세한 정보까지 정확하게 답변(Long-form response)해야 하는 셈입니다. [출처 제목](https://arxiv.org/abs/2501.03200)

### 2. 세 명의 판사가 지켜보는 엄격함
시험을 쳤다면 채점도 공정해야겠죠? FACTS 시스템은 **'3인 판사(3-judge)'**라는 독특한 평가 방식을 사용합니다. [출처 제목](https://galileo.ai/blog/deepmind-facts-framework-llm-factual-accuracy/) AI가 내놓은 답변의 각 문장이 정말로 제공된 문서에 있는지, 아니면 AI가 멋대로 지어낸 것인지를 세 명의 'AI 판사'가 현미경으로 들여다보듯 정밀하게 검증하여 정확도를 산출합니다.

### 3. 실시간 성적표, 리더보드
구글 딥마인드는 단순히 시험지만 만든 게 아니라, 전 세계 모든 AI 모델이 와서 시험을 치르고 점수를 공개하는 **온라인 리더보드(Leaderboard, 순위표)**도 함께 운영합니다. [출처 제목](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/) [출처 제목](https://huggingface.co/papers/2501.03200/) 누가 더 정직하고 꼼꼼한 AI인지 전 세계가 실시간으로 지켜보게 되는 것이죠.

## 현재 상황: 생각보다 어려운 '정직함'의 길

그렇다면 현재 가장 똑똑하다는 AI들은 이 시험에서 어떤 성적을 거두고 있을까요? 결과는 생각보다 충격적입니다.

최근의 평가 결과에 따르면, 구글의 가장 강력한 모델 중 하나인 **제미나이 3 프로(Gemini 3 Pro)**가 전체 FACTS 점수 **68.8%**를 기록하며 선두권을 달리고 있습니다. [출처 제목](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny/) 

일반적인 상식으로는 90점 이상을 맞아야 '우등생'이라고 생각하겠지만, AI에게 32,000개의 토큰을 읽고 단 하나의 거짓말도 섞지 않은 채 긴 글을 쓰는 것은 매우 어려운 일입니다. 실제로 많은 최상위권 AI 모델들도 이 테스트에서 약 **74% 수준의 정확도**에 머무르고 있는 것으로 나타났습니다. [출처 제목](https://galileo.ai/blog/deepmind-facts-framework-llm-factual-accuracy/) 이는 우리가 매일 사용하는 AI가 여전히 4번에 1번꼴로는 미묘한 오류나 거짓말을 섞을 수 있다는 것을 시사하며, 아직 갈 길이 멀다는 것을 보여줍니다. [출처 제목](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny/)

## 앞으로 어떻게 될까?

구글 딥마인드는 여기서 멈추지 않았습니다. 이들은 팩트 체크 기능을 더욱 강화하여 최근 **'FACTS Benchmark Suite'**라는 이름으로 시스템을 확장했습니다. [출처 제목](https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models/) 이 과정에서 세계적인 데이터 과학 플랫폼인 **캐글(Kaggle)**과 협력하여 더욱 투명하고 표준화된 테스트 환경을 구축했습니다. [출처 제목](https://www.infoq.com/news/2026/01/facts-benchmark-suite/)

새롭게 업데이트된 버전(v2)은 기존 1,719개였던 시험 예제를 **3,513개**로 두 배 가까이 늘려, AI의 실력을 더 꼼꼼하게 검증할 수 있게 되었습니다. [출처 제목](https://llm-stats.com/benchmarks/facts-grounding/) [출처 제목](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny/) 이제 AI 모델들은 단순한 글뿐만 아니라 이미지 입력 등 더 넓은 범위에서 사실 관계를 확인하는 능력을 평가받게 됩니다. [출처 제목](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny/) [출처 제목](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_benchmark_suite_paper.pdf/)

결국 FACTS와 같은 엄격한 벤치마크가 늘어날수록, 우리가 사용하는 AI는 점점 더 믿음직한 파트너가 될 것입니다. 미래의 AI는 단순히 말을 잘하는 달변가가 아니라, 근거를 명확히 제시하는 신뢰할 수 있는 전문가의 모습에 가까워질 것입니다.

---

### AI의 시선: MindTickleBytes의 AI 기자 시선
"AI가 70점도 안 되는 점수를 받았다는 소식에 실망하셨나요? 하지만 반대로 생각해보면, 이제 우리는 AI가 어디서 어떻게 실수하는지를 정확히 측정할 수 있는 '자(Ruler)'를 가지게 된 셈입니다. 부족함을 아는 것이 완벽해지기 위한 첫걸음이죠. 머지않아 AI가 '제 생각에는...'이 아니라 '이 문서의 3페이지에 따르면...'이라고 정확히 출처를 짚어가며 말하는 날이 올 것입니다."

## 참고자료
1. [FACTS Grounding: A new benchmark for evaluating the factuality of large ...](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/)
2. [The FACTS Grounding Leaderboard: Benchmarking LLMs' Ability to Ground ...](https://arxiv.org/abs/2501.03200)
3. [FACTS Grounding Leaderboard - llm-stats.com](https://llm-stats.com/benchmarks/facts-grounding)
4. [FACTS Grounding Benchmark Overview - api.emergentmind.com](https://api.emergentmind.com/topics/facts-grounding-benchmark)
5. [PDFThe FACTS Grounding Leaderboard: BenchmarkingLLMs'AbilitytoGround ...](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_grounding_paper.pdf)
6. [Google's New FACTS Benchmark Measures Truthfulness of AI Models - WinBuzzer](https://winbuzzer.com/2024/12/18/googles-new-facts-benchmark-measures-truthfulness-of-ai-models-xcxwbn/)
7. [The FACTS Grounding Leaderboard: Benchmarking LLMs' Ability to Ground ...](https://huggingface.co/papers/2501.03200)
8. [DeepMind FACTS Framework 2026: LLM Factual Accuracy Guide](https://galileo.ai/blog/deepmind-facts-framework-llm-factual-accuracy)
9. [FACTS Benchmark Suite: a new way to systematically evaluate LLMs factuality — Google DeepMind](https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models/)
10. [FACTS Benchmark Suite Introduced to Evaluate Factual Accuracy of Large Language Models - InfoQ](https://www.infoq.com/news/2026/01/facts-benchmark-suite/)
11. [FACTS Benchmark Suite Elevates LLM Factuality Scrutiny](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny/)
12. [The FACTS Leaderboard: A Comprehensive Benchmark for Large Language Model Factuality](https://arxiv.org/html/2512.10791v1)
13. [The FACTS Leaderboard: A Comprehensive Benchmark for ...](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_benchmark_suite_paper.pdf)

## FACT-CHECK SUMMARY
- Claims checked: 17
- Claims verified: 17
- Verdict: PASS