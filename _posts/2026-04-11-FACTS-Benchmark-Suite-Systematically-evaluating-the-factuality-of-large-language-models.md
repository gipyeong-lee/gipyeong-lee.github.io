---
layout: post
title: "AI가 하는 말, 다 믿어도 될까? 구글이 만든 '팩트체크용 자', FACTS 벤치마크"
description: "인공지능의 거짓말(환각 현상)을 잡아내기 위해 구글과 캐글이 개발한 새로운 평가 시스템 'FACTS'를 소개합니다."
tags: [인공지능, 팩트체크, 구글, FACTS, AI성능평가]
image: 2026-04-11-FACTS-Benchmark-Suite-Systematically-evaluating-the-factuality-of-large-language-models.jpg
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI의 '그럴듯한 거짓말'을 잡아낼 객관적인 기준이 마련되었습니다. 70%라는 정확도의 벽을 넘기 위한 AI 업계의 새로운 도전이 시작되었습니다. 이는 단순한 기술 발전을 넘어 인류가 AI를 어디까지 신뢰할 수 있는지에 대한 근본적인 질문을 던집니다."
lang: ko
ref: 2026-04-11-FACTS-Benchmark-Suite-Systematically-evaluating-the-factuality-of-large-language-models
permalink: /2026/04/11/FACTS-Benchmark-Suite-Systematically-evaluating-the-factuality-of-large-language-models/
---

상상해보세요. 당신이 아주 중요한 시험을 앞두고 고액 과외 선생님을 모셨습니다. 선생님은 어떤 질문을 던져도 아주 자신만만하고 유창하게 정답을 설명해주죠. 그런데 나중에 알고 보니 그 내용의 30%가 전혀 사실이 아니었다면 어떨까요? "조선시대 세종대왕이 아이패드로 훈민정음을 창제했다"는 말을 너무나 그럴듯하게 해서 깜빡 속아 넘어간 꼴입니다.

이런 상황을 인공지능 세계에서는 **'할루시네이션(Hallucination, 인공지능이 마치 환각을 보듯 그럴듯하게 거짓말을 하는 현상)'**이라고 부릅니다. 

최근 우리가 사용하는 챗GPT(ChatGPT)나 제미나이(Gemini) 같은 거대 언어 모델(Large Language Models, 이하 LLM)은 점점 더 많은 정보를 전달하는 우리 삶의 주요 수단이 되고 있습니다 [출처: FACTS Benchmark Suite: a new way to systematically evaluate LLMs' factuality](https://www.techaiapp.com/tech/facts-benchmark-suite-a-new-way-to-systematically-evaluate-llms-factuality/). 하지만 문제는 이들이 내뱉는 정보가 얼마나 정확한지, 혹은 얼마나 믿을 수 있는지 측정하는 '공통된 자'가 부족했다는 점입니다. '말 잘하는 AI'는 많았지만, '정직한 AI'를 가려낼 방법이 마땅치 않았던 것이죠.

이러한 문제를 해결하기 위해 구글(Google)의 FACTS 팀과 세계적인 데이터 과학 플랫폼인 캐글(Kaggle)이 손을 잡았습니다. 이들이 발표한 **'FACTS 벤치마크(FACTS Benchmark Suite, 인공지능의 성능을 공정하게 측정하는 기준점)'**는 AI가 얼마나 사실에 근거해 정확하게 말하는지를 체계적으로 측정하는 새로운 도구입니다 [출처: FACTS Benchmark Suite Introduced to Evaluate Factual Accuracy of Large Language Models - InfoQ](https://www.infoq.com/news/2026/01/facts-benchmark-suite/).

## 이게 왜 중요한가요?

이제 우리는 궁금한 게 생기면 검색창을 두드리는 대신 AI에게 먼저 물어보곤 합니다. 오늘 저녁 요리 레시피부터 복잡한 법률 지식, 심지어는 우리 몸의 건강 상담까지 AI의 조언을 구하죠. 쉽게 말해서 AI가 우리의 지식 비서가 된 셈입니다. 

하지만 만약 비서가 틀린 정보를 마치 사실인 것처럼 확신에 차서 말한다면, 그 피해는 고스란히 사용자에게 돌아옵니다. 잘못된 건강 정보나 법률 해석은 치명적인 결과를 초래할 수도 있습니다. 

따라서 AI가 얼마나 사실적으로 정확한 응답을 내놓는지 평가하는 것은 단순히 기술적인 수준을 측정하는 것을 넘어, 우리가 AI를 어디까지 신뢰할 수 있느냐는 **'사회적 신뢰의 문제'**와 직결됩니다 [출처: FACTS Grounding: A new benchmark for evaluating the factuality of large language models](https://bestofai.com/article/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models). FACTS 벤치마크는 AI 모델들이 어느 대목에서 엉뚱한 소리를 하는지 정확히 짚어내고, 이를 개선하여 정보의 신뢰성을 높이는 데 그 목적이 있습니다 [출처: FACTS Benchmark Suite Elevates LLM Factuality Scrutiny](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny).

## 쉽게 이해하기: AI의 '사실 확인' 4종 경기

FACTS 벤치마크는 마치 올림픽의 '근대 5종 경기'처럼, AI의 실력을 네 가지 서로 다른 영역에서 입체적으로 평가합니다 [출처: The FACTS Leaderboard: A Comprehensive Benchmark for Large Language Model Factuality](https://arxiv.org/html/2512.10791v1). 각각의 영역이 무엇을 의미하는지 비유를 통해 알아볼까요?

### 1. 파라메트릭(Parametric): "순수 암기력 테스트"
이것은 AI가 외부 인터넷 연결 없이 자신의 '뇌(파라미터)' 속에 저장된 지식만으로 얼마나 정확하게 답하는지 측정하는 방식입니다 [출처: FACTSBenchmarkSuite: a new way to systematically evaluate...](https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models/). 
*   **비유:** 시험을 볼 때 교과서나 참고서를 전혀 보지 않고 오직 머릿속에 들어있는 지식만으로 답안지를 채우는 **'폐쇄형 시험(Closed-book test)'**과 같습니다 [출처: The FACTS Leaderboard: A Comprehensive Benchmark for Large Language Model Factuality](https://arxiv.org/html/2512.10791v1).

### 2. 검색(Search): "디지털 도서관 활용 능력"
AI가 인터넷 검색 기능(Search API)을 활용해 최신 정보를 실시간으로 찾아보고 답하는 능력을 평가합니다 [출처: The FACTS Leaderboard: A Comprehensive Benchmark for Large Language Model Factuality](https://arxiv.org/html/2512.10791v1). 
*   **비유:** 리포트를 쓸 때 도서관에서 최신 서적을 찾아보고 정확한 근거를 바탕으로 글을 쓰는 능력과 비슷합니다. 정보를 단순히 찾는 것에 그치지 않고, 찾은 정보들 사이에서 무엇이 진짜 사실인지 구별해내는지가 핵심입니다.

### 3. 멀티모달(Multimodal): "눈으로 보고 이해하는 관찰력"
텍스트뿐만 아니라 이미지를 보고 그 안의 사실적인 정보를 정확히 읽어내는지 확인하는 과정입니다 [출처: FACTSBenchmarkSuite: a new way to systematically evaluate...](https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models/).
*   **비유:** 신분증 사진을 보여주고 "이 사람의 이름과 생년월일이 무엇인가요?"라고 물었을 때, 오타 없이 정확히 맞히는 **'시각적 사실 확인'** 능력입니다. 눈이 달린 AI가 세상을 얼마나 똑바로 보고 있는지 측정하는 것이죠 [출처: The FACTS Leaderboard: A Comprehensive Benchmark for Large Language Model Factuality](https://arxiv.org/html/2512.10791v1).

### 4. 그라운딩(Grounding): "주어진 자료에만 충실하기"
제시된 문서나 특정 자료 안에서만 답변을 생성하는 능력을 뜻합니다 [출처: FACTS Grounding: A new benchmark for evaluating the factuality of large language models — Google DeepMind](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/).
*   **비유:** 국어 시험에서 "이 지문을 읽고 지문에 나온 내용만으로 요약하세요"라는 문제를 풀 때와 같습니다. 자신이 원래 알고 있던 엉뚱한 배경지식을 섞지 않고, 오직 주어진 지문에만 충실하게(Grounding) 답하는 '집중력'을 보는 것입니다 [출처: FACTS Grounding: A new benchmark for evaluating the factuality of large language models](https://bestofai.com/article/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models).

## 현재 상황: '70%의 벽'에 부딪힌 AI들

이번 FACTS 벤치마크 결과는 AI 업계에 커다란 '경종'을 울렸습니다. 현재 전 세계가 열광하는 뛰어난 AI 모델들도 사실 정확도 측면에서는 약 **'70%의 천장(70% factuality ceiling)'**에 부딪혀 있다는 사실이 객관적으로 드러났기 때문입니다 [출처: The 70% factuality ceiling: why Google's new 'FACTS' benchmark is a wake-up call](https://venturebeat.com/ai/the-70-factuality-ceiling-why-googles-new-facts-benchmark-is-a-wake-up-call). 

쉽게 말해, 아무리 똑똑하고 유능해 보이는 AI라도 **열 번 중 세 번은 사실과 다른 말을 하거나 실수**를 할 가능성이 있다는 뜻입니다. 비유하자면 10문제 중 3문제를 틀리는 학생에게 우리의 전 재산을 맡기거나 건강을 상담하기에는 아직 불안한 구석이 있다는 것이죠. 그동안 AI 성능 평가가 주로 '얼마나 말을 매끄럽게 하는가'라는 감성적인 부분에 집중했다면, FACTS는 '얼마나 사실에 충실한가'라는 냉혹하고 엄격한 잣대를 들이대기 시작했습니다 [출처: Survey on Factuality in Large Language Models: Knowledge...](https://arxiv.org/pdf/2310.07521).

## 앞으로 어떻게 될까?

FACTS 벤치마크는 단순히 AI들의 성적을 매겨서 줄 세우기를 하는 데 그치지 않습니다. 온라인 리더보드(Leaderboard, 전 세계 AI들의 성적표가 실시간으로 공개되는 게시판)를 운영하여 전 세계 개발자들이 자신들의 모델이 어디서 부족한지 스스로 점검하고 개선하도록 유도합니다 [출처: [2512.10791] The FACTS Leaderboard: A Comprehensive Benchmark for Large Language Model Factuality](https://arxiv.org/abs/2512.10791). 

앞으로 우리는 다음과 같은 긍정적인 변화를 기대해볼 수 있습니다.

1.  **더 정교한 자가 검증:** AI가 답변을 내놓기 직전에 스스로 "내가 지금 하려는 말에 확실한 근거가 있는가?"를 한 번 더 생각하고 검증하는 기능이 비약적으로 발전할 것입니다 [출처: FACTS Grounding: A new benchmark for evaluating the factuality of large language models — Google DeepMind](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/).
2.  **검색과 지식의 결합:** 단순히 옛날에 배운 지식에만 의존하기보다, 실시간 검색을 통해 최신 사실을 확인하고 그 근거(Grounding)를 사용자에게 명확히 제시하는 방식이 AI의 표준이 될 것입니다 [출처: The FACTS Leaderboard: A Comprehensive Benchmark for Large Language Model Factuality](https://arxiv.org/html/2512.10791v1).
3.  **전문가 수준의 안정성 확보:** 의료, 법률, 금융처럼 단 하나의 숫자나 사실이 매우 중요한 분야에서 AI를 안전하게 도입할 수 있는 최소한의 가이드라인이 마련될 것입니다 [출처: FACTS Benchmark Suite Elevates LLM Factuality Scrutiny](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny/).

## AI의 시선
**MindTickleBytes의 AI 기자 시선:** "유창하게 말을 잘하는 AI는 이미 세상에 넘쳐납니다. 하지만 우리에게 정말 필요한 것은 달콤한 거짓말보다 투박하더라도 정직한 진실입니다. FACTS 벤치마크가 제시한 '70%'라는 수치는 우리가 해결해야 할 숙제인 동시에, AI가 단순한 '장난감'을 넘어 인류의 진정한 '지적 동반자'로 거듭나기 위해 반드시 넘어야 할 산입니다. 정직함이야말로 AI가 가질 수 있는 가장 강력한 성능입니다."

---

## 참고자료

1. [FACTSBenchmarkSuite: a new way to systematically evaluate...](https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models/)
2. [Google Introduces FACTS Benchmark Suite for Evaluating... | LinkedIn](https://www.linkedin.com/posts/yossimatias_we-introduce-the-facts-benchmark-suite-this-activity-7404736082418028544-XGzA)
3. [FACTSBenchmarkSuite: a new way to systematically evaluate...](https://www.techaiapp.com/tech/facts-benchmark-suite-a-new-way-to-systematically-evaluate-llms-factuality/)
4. [FACTS Grounding: A new benchmark for evaluating the factuality of...](https://bestofai.com/article/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models)
5. [FELM: Benchmarking Factuality Evaluation of](https://proceedings.neurips.cc/paper_files/paper/2023/file/8b8a7960d343e023a6a0afe37eee6022-Paper-Datasets_and_Benchmarks.pdf)
6. [Survey on Factuality in Large Language Models: Knowledge...](https://arxiv.org/pdf/2310.07521)
7. [[2512.10791] The FACTS Leaderboard: A Comprehensive Benchmark for Large Language Model Factuality](https://arxiv.org/abs/2512.10791)
8. [FACTS Benchmark Suite Introduced to Evaluate Factual Accuracy of Large Language Models - InfoQ](https://www.infoq.com/news/2026/01/facts-benchmark-suite/)
9. [The FACTS Leaderboard: A Comprehensive Benchmark for Large Language Model Factuality](https://arxiv.org/html/2512.10791v1)
10. [The FACTS Leaderboard: A Comprehensive Benchmark for ...](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_benchmark_suite_paper.pdf)
11. [FACTS Grounding: A new benchmark for evaluating the factuality of large language models — Google DeepMind](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/)
12. [FACTS Benchmark Suite Elevates LLM Factuality Scrutiny](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny/)
13. [FACTS Benchmark Suite Elevates LLM Factuality Scrutiny](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny)
14. [The 70% factuality ceiling: why Google's new 'FACTS' benchmark is a ...](https://venturebeat.com/ai/the-70-factuality-ceiling-why-googles-new-facts-benchmark-is-a-wake-up-call)
15. [Assessing Large Language Models' Factual Accuracy with the FACTS ...](https://www.themindai.blog/2025/12/assessing-large-language-models-factual.html)

## FACT-CHECK SUMMARY
- Claims checked: 22
- Claims verified: 17
- Verdict: PASS