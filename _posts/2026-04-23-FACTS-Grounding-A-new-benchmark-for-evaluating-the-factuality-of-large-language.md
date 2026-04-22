---
layout: post
title: "AI의 '그럴듯한 거짓말'을 잡는 엄격한 시험지, 구글의 FACTS가 나타났다!"
description: "구글 딥마인드가 공개한 새로운 AI 팩트 체크 벤치마크 FACTS Grounding을 소개합니다. AI의 할루시네이션 문제를 해결하기 위한 3만 2천 토큰의 방대한 문서 기반 검증 도구를 알아보세요."
summary: "구글 딥마인드가 AI가 주어진 문서 내에서 얼마나 정확하고 상세하게 답변하는지 측정하는 'FACTS Grounding' 벤치마크를 공개하며 AI 신뢰성의 새로운 기준을 제시했습니다."
tags: [AI, 구글딥마인드, FACTS, 팩트체크, 인공지능, 할루시네이션]
image: 2026-04-23-FACTS-Grounding-A-new-benchmark-for-evaluating-the-factuality-of-large-language.jpg
image_alt: "돋보기를 든 로봇이 방대한 문서 더미 속에서 정확한 사실을 골라내어 체크 표시를 하는 일러스트"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI가 단순히 똑똑한 것을 넘어 '믿을 수 있는' 존재가 되기 위한 중요한 관문이 열렸습니다. 70%라는 성능의 벽을 확인한 것은 기술적 한계를 인정하고 정교한 개선을 시작하겠다는 강력한 의지의 표현입니다."
quiz:
  - question: "FACTS Grounding 벤치마크에서 AI가 읽어야 하는 문서의 최대 길이는 얼마인가요?"
    choices: ["1,000 토큰", "12,000 토큰", "32,000 토큰"]
    answer: 2
    explanation: "FACTS Grounding은 최대 32,000 토큰 분량의 긴 문서를 기반으로 AI의 사실 관계 파악 능력을 테스트합니다."
  - question: "현재까지 이 벤치마크에서 최상위권 모델들이 보여준 정확도는 어느 수준인가요?"
    choices: ["약 50%", "약 74%", "약 99%"]
    answer: 1
    explanation: "최상위권 모델들도 현재 약 74% 수준의 정확도에 머물고 있어, 여전히 개선의 여지가 많은 것으로 나타났습니다."
  - question: "FACTS 벤치마크의 공정한 평가를 위해 도입된 시스템은 무엇인가요?"
    choices: ["1인 심사 시스템", "3인 판사(Judge) 시스템", "무작위 선출 시스템"]
    answer: 1
    explanation: "FACTS 프레임워크는 평가의 정확성과 공정성을 높이기 위해 3인의 판사 모델이 평가하는 시스템을 사용합니다."
lang: ko
ref: 2026-04-23-FACTS-Grounding-A-new-benchmark-for-evaluating-the-factuality-of-large-language
audio: 2026-04-23-FACTS-Grounding-A-new-benchmark-for-evaluating-the-factuality-of-large-language.mp3
permalink: /2026/04/23/FACTS-Grounding-A-new-benchmark-for-evaluating-the-factuality-of-large-language/
---

상상해보세요. 여러분이 아주 중요한 비즈니스 보고서 50페이지를 AI에게 건네주며 "이 안에서 가장 중요한 숫자 3개만 정확하게 뽑아줘"라고 부탁했습니다. AI는 1초 만에 아주 자신감 넘치는 말투로 답변을 내놓습니다. 그런데 나중에 직접 확인해보니 그 숫자 중 하나가 보고서 어디에도 없는, AI가 멋대로 지어낸 숫자라면 어떨까요? 등줄기가 서늘해지는 경험이겠죠.

이런 현상을 우리는 **할루시네이션(Hallucination, 인공지능이 사실이 아닌 정보를 마치 사실인 것처럼 자신 있게 말하는 현상)**이라고 부릅니다. 쉽게 말해 '그럴듯한 헛소리'를 하는 것이죠. AI가 아무리 똑똑해져도 이 고질적인 문제는 늘 꼬리표처럼 따라다녔습니다. 하지만 이제 AI가 얼마나 정직하게 답변하는지, 아니면 아는 척을 하는지 엄격하게 점수를 매기는 '현미경'이 등장했습니다. 바로 구글 딥마인드(Google DeepMind)가 공개한 **'FACTS Grounding'**입니다.

## 이게 왜 중요한가요?

우리가 AI를 일상에서 정말 믿고 쓰려면, 단순히 문장을 유려하게 쓰는 것을 넘어 **'근거'**가 확실해야 합니다. 특히 전문적인 의학 논문을 요약하거나 기업의 대외비 문서를 분석할 때 AI가 단 한 문장이라도 거짓말을 한다면, 이는 단순한 실수를 넘어 치명적인 사고로 이어질 수 있습니다. 

구글 딥마인드가 이 벤치마크(Benchmark, 성능 측정 기준)를 만든 이유는 아주 명확합니다. AI 모델이 사용자에게 단순히 기분 좋은 답변을 주는 수준을 넘어, **주어진 입력 데이터에 대해 사실적으로 정확하고 충분히 상세한 답변**을 생성하도록 보장하기 위해서입니다 [FACTS Grounding: A new benchmark for evaluating the factuality of large language models — Google DeepMind](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/).

비유하자면, AI가 인터넷의 수만 가지 정보를 대충 훑어 대답하는 '박학다식한 척하는 검색왕'이 되는 대신, 선생님이 준 교과서 한 권만 철저히 파고들어 정답을 찾는 '우직한 우등생'이 되도록 훈련시키는 과정인 셈입니다. 이를 통해 실제 비즈니스 현장에서 AI에 대한 신뢰도를 높이고, 더 전문적인 영역까지 활용할 수 있는 토대를 마련하려는 의도입니다 [FACTS Grounding: A new benchmark for evaluating the factuality of large language models](https://bestofai.com/article/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models).

## 쉽게 이해하기: FACTS는 어떤 시험인가요?

FACTS Grounding을 한마디로 정의하자면 **'초대형 오픈북 테스트'**라고 할 수 있습니다. 하지만 문제는 이 '오픈북'이 우리가 생각하는 것보다 훨씬 더 두껍고 까다롭다는 점입니다.

### 1. 엄청난 분량의 시험지: "한 권의 책을 통째로?"
학생(AI)에게 주어지는 시험지의 길이는 무려 **32,000 토큰(Token, AI가 글자를 처리하는 최소 단위)**에 달합니다 [The FACTS Grounding Leaderboard: Benchmarking LLMs' Ability to Ground ...](https://arxiv.org/abs/2501.03200). 

여기서 32,000 토큰이 어느 정도인지 감이 안 오실 텐데요, 쉽게 말해 대략 수십 페이지 분량의 두툼한 보고서 한 권이나 중편 소설 한 권과 맞먹는 엄청난 양입니다. AI는 이 긴 글을 처음부터 끝까지 놓치지 않고 읽어낸 뒤, 사용자의 복잡한 질문에 대해 아주 상세하고 구체적인 답변을 내놓아야 합니다 [FACTS Grounding Leaderboard - llm-stats.com](https://llm-stats.com/benchmarks/facts-grounding). 이 테스트는 총 **1,719개의 예시**로 구성되어 있어, AI가 우연히 한두 번 찍어서 맞히는 요행을 부릴 수도 없게 아주 정밀하게 설계되었습니다 [FACTS Grounding Leaderboard - llm-stats.com](https://llm-stats.com/benchmarks/facts-grounding).

### 2. 깐깐한 세 명의 판사: "공정성이 생명"
시험을 봤으면 채점을 해야겠죠? FACTS는 채점의 공정성을 확보하기 위해 **'3인 판사(Judge) 시스템'**을 도입했습니다 [DeepMind FACTS Framework 2026: LLM Factual Accuracy Guide](https://galileo.ai/blog/deepmind-facts-framework-llm-factual-accuracy). 

혼자서 채점하다가 주관적인 판단이 섞이거나 실수할 수 있으니, 고도로 훈련된 세 명의 인공지능 판사가 나섭니다. 이들은 각 모델의 답변이 주어진 문서에 정말로 근거(Grounding)하고 있는지, 아니면 교묘하게 다른 곳에서 주워들은 지식을 섞어 마치 문서에 있는 것처럼 연기하고 있는지 꼼꼼하게 따집니다.

### 3. '팩트'에 발을 붙였는가: Grounding의 의미
여기서 가장 핵심적인 키워드는 **'그라운딩(Grounding)'**입니다. 이는 AI가 답변을 할 때 허공을 떠도는 근거 없는 지식이 아니라, 마치 땅(Ground)을 단단히 딛고 서 있듯 **주어진 근거 문서에 발을 꼭 붙이고 있는가**를 의미합니다 [The FACTS Grounding Leaderboard: Benchmarking LLMs' Ability to Ground ...](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_grounding_paper.pdf). 문서에 없는 내용을 단 한 마디라도 섞는 순간, 그 답변은 '근거 없음(Ungrounded)'으로 간주되어 엄격한 감점 대상이 됩니다 [FACTS Grounding Benchmark Overview - api.emergentmind.com](https://api.emergentmind.com/topics/facts-grounding-benchmark).

## 현재 상황: '70%의 벽'에 부딪힌 AI의 민낯

이 엄격한 시험 결과, 현재 AI 기술이 가진 한계가 고스란히 드러났습니다. 연구자들에 따르면, 현재 전 세계에서 가장 똑똑하다고 칭송받는 최상위권 모델들조차 이 테스트에서 **약 74%의 정확도**를 기록하는 데 그쳤습니다 [DeepMind FACTS Framework 2026: LLM Factual Accuracy Guide](https://galileo.ai/blog/deepmind-facts-framework-llm-factual-accuracy).

이를 두고 전문가들은 **'70%의 사실성 천장(70% factuality ceiling)'**이라는 표현을 씁니다 [The 70% factuality ceiling: why Google's new 'FACTS' benchmark is a ...](https://venturebeat.com/ai/the-70-factuality-ceiling-why-googles-new-facts-benchmark-is-a-wake-up-call). 아무리 수억 달러를 들여 만든 최신 모델이라도, 방대한 정보 속에서 100% 완벽하게 사실만을 골라내 답변하는 데는 여전히 한계가 있다는 뜻입니다. 이는 인공지능 업계에 던져진 일종의 '경고장'인 동시에, AI가 '신뢰할 수 있는 도구'로 인정받기 위해 넘어야 할 명확한 숙제가 되었습니다 [The 70% factuality ceiling: why Google's new 'FACTS' benchmark is a ...](https://venturebeat.com/ai/the-70-factuality-ceiling-why-googles-new-facts-benchmark-is-a-wake-up-call).

또한, 이번 벤치마크는 데이터 과학의 메카라 불리는 플랫폼 **캐글(Kaggle)**과 협력하여 개발되어 그 전문성을 더했습니다 [FACTS Benchmark Suite Introduced to Evaluate Factual Accuracy of Large Language Models - InfoQ](https://www.infoq.com/news/2026/01/facts-benchmark-suite/). 전 세계의 내로라하는 데이터 전문가들이 머리를 맞대고 AI가 어떤 부분에서 실수를 저지르는지 정확히 짚어낼 수 있는 정교한 감시 체계를 만든 것입니다 [FACTS Benchmark Suite Elevates LLM Factuality Scrutiny](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny).

## 앞으로 어떻게 될까?

구글 딥마인드는 여기서 만족하지 않고, 지난 2025년 12월 성능이 대폭 향상된 판사 모델을 탑재한 **'FACTS Grounding v2'**를 전격 출시했습니다 [FACTS Benchmark Suite: a new way to systematically evaluate LLMs factuality — Google DeepMind](https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models/). 더 까다로워진 판사들이 AI를 감시하게 된 것이죠 [The FACTS Leaderboard: A Comprehensive Benchmark for Large Language Model Factuality](https://arxiv.org/html/2512.10791v1).

앞으로 우리는 온라인 **리더보드(Leaderboard, 순위표)**를 통해 어떤 AI가 가장 정직하고 똑똑한지 실시간으로 확인할 수 있게 됩니다 [The FACTS Grounding Leaderboard: Benchmarking LLMs' Ability to Ground ...](https://huggingface.co/papers/2501.03200). 이는 마치 가전제품의 '에너지 효율 등급'처럼, 우리가 AI 서비스를 선택할 때 '정확도 등급'을 직접 확인하고 믿고 쓰는 시대를 열어줄 것입니다.

복잡하고 방대한 정보를 다룰 때 발생할 수 있는 AI의 실수를 0에 가깝게 줄여나가는 이 치열한 과정은, 인공지능이 단순한 장난감을 넘어 우리 삶의 진정한 파트너로 거듭나기 위한 가장 필수적인 발걸음이 될 것입니다 [FACTS Grounding: A New Benchmark for Evaluating the Factuality of Large Language Models | ASU+GSV Summit Schedule](https://www.asugsvsummit.com/schedule/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models).

## AI의 시선
**MindTickleBytes의 AI 기자 시선**

AI가 단순히 화려한 문장을 지어내어 '창의성'으로 칭송받던 낭만적인 시대는 저물고 있습니다. 이제는 얼마나 정확하고 정직한지를 입증해야 하는 '검증의 시대'가 도래했습니다. 74%라는 성적표는 결코 부끄러운 결과가 아닙니다. 오히려 우리가 정복해야 할 정상을 발견했다는 희망의 신호에 가깝습니다. '모르는 것을 모른다'고 말하고, '있는 사실만을 말하는' 인격적인 AI를 향한 여정이 드디어 본격적인 궤도에 올랐습니다.

## 참고자료
1. [FACTS Grounding: A new benchmark for evaluating the factuality of large language models — Google DeepMind](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/)
2. [FACTS Benchmark Suite: a new way to systematically evaluate LLMs factuality — Google DeepMind](https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models/)
3. [FACTS Grounding: A New Benchmark for Evaluating the Factuality of Large Language Models | ASU+GSV Summit Schedule](https://www.asugsvsummit.com/schedule/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models)
4. [r/LocalLLaMA on Reddit: FACTS Grounding: A new benchmark for evaluating the factuality of large language models](https://www.reddit.com/r/LocalLLaMA/comments/1hgyp2d/facts_grounding_a_new_benchmark_for_evaluating/)
5. [The FACTS Leaderboard: A Comprehensive Benchmark for Large Language Model Factuality](https://arxiv.org/html/2512.10791v1)
6. [FACTS Grounding: A new benchmark for evaluating the factuality of large language models](https://bestofai.com/article/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models)
7. [FACTS Benchmark Suite Introduced to Evaluate Factual Accuracy of Large Language Models - InfoQ](https://www.infoq.com/news/2026/01/facts-benchmark-suite/)
8. [The FACTS Grounding Leaderboard: Benchmarking LLMs' Ability to Ground ...](https://arxiv.org/abs/2501.03200)
9. [PDFThe FACTS Grounding Leaderboard: BenchmarkingLLMs'AbilitytoGround ...](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_grounding_paper.pdf)
10. [FACTS Grounding Leaderboard - llm-stats.com](https://llm-stats.com/benchmarks/facts-grounding)
11. [The FACTS Grounding Leaderboard: Benchmarking LLMs' Ability to Ground ...](https://huggingface.co/papers/2501.03200)
12. [DeepMind FACTS Framework 2026: LLM Factual Accuracy Guide](https://galileo.ai/blog/deepmind-facts-framework-llm-factual-accuracy)
13. [FACTS Grounding Benchmark Overview - api.emergentmind.com](https://api.emergentmind.com/topics/facts-grounding-benchmark)
14. [The 70% factuality ceiling: why Google's new 'FACTS' benchmark is a ...](https://venturebeat.com/ai/the-70-factuality-ceiling-why-googles-new-facts-benchmark-is-a-wake-up-call)
15. [FACTS Benchmark Suite Elevates LLM Factuality Scrutiny](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny)