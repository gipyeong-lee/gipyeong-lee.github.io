---
layout: post
title: "AI 코딩 실력, 시험 문제부터 다시 봐야 한다? OpenAI의 결단"
description: "OpenAI가 AI 코딩 능력 평가의 표준으로 쓰이던 'SWE-Bench Pro'의 사용 권장을 중단했습니다. 문제 자체의 오류가 발견되면서 AI 성능 평가의 신뢰성에 빨간불이 켜졌습니다."
summary: "OpenAI가 AI의 코딩 실력을 측정하던 주요 지표인 SWE-Bench Pro에서 약 30%의 오류를 발견하고 사용 권장을 중단했습니다."
tags: [AI, 코딩, 개발, OpenAI, SWE-Bench]
image: 2026-07-09-OpenAI-no-longer-recommends-SWE-Bench-Pro.jpg
image_alt: "코드 조각과 AI 아이콘이 얽혀 있는 배경 위로 시험지 오류를 상징하는 경고 표시가 떠 있는 모습."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI의 기술이 빠르게 발전하면서 이를 측정하는 '시험'의 정교함이 그 속도를 따라가지 못하는 상황입니다. 개발자가 직접 검증하는 시대가 다가오고 있습니다."
quiz:
  - question: "OpenAI가 SWE-Bench Pro 사용 권장을 중단한 가장 큰 이유는 무엇인가요?"
    choices: ["AI의 실력이 너무 좋아서", "공개된 작업 과제의 약 30%가 잘못 구성되어 있어서", "이미 모든 AI가 만점을 받아서"]
    answer: 1
    explanation: "OpenAI는 SWE-Bench Pro의 공개 작업 과제 중 약 30%가 제대로 작동하지 않아 신뢰할 수 없는 결과가 나온다고 밝혔습니다."
  - question: "SWE-Bench Verified가 먼저 중단된 이유는 무엇인가요?"
    choices: ["사용료가 너무 비싸서", "개발자가 부족해서", "데이터 오염과 시험 문제 자체의 결함 때문"]
    answer: 2
    explanation: "데이터 오염 문제와 함께 검토된 문제의 약 60%가 구조적으로 결함이 있는 것으로 드러나 중단되었습니다."
  - question: "SWE-Bench Pro를 개발한 회사는 어디인가요?"
    choices: ["Google", "Scale AI", "Microsoft"]
    answer: 1
    explanation: "SWE-Bench Pro는 Scale AI에서 개발하여 2025년 9월에 공개했습니다."
lang: ko
ref: 2026-07-09-OpenAI-no-longer-recommends-SWE-Bench-Pro
audio: 2026-07-09-OpenAI-no-longer-recommends-SWE-Bench-Pro.mp3
permalink: /2026/07/09/OpenAI-no-longer-recommends-SWE-Bench-Pro/
---

상상해보세요. 아주 중요한 수학 시험을 보러 갔는데, 정답지가 틀려 있거나 문제 자체가 성립하지 않는 오류 투성이인 상황입니다. 학생은 아무리 열심히 문제를 풀어도 자신의 정확한 실력을 평가받을 수 없겠죠. 최근 AI 업계에서 벌어지고 있는 '코딩 시험' 논란이 딱 이와 같습니다.

OpenAI는 그동안 AI의 소프트웨어 엔지니어링 능력을 측정하는 도구로 'SWE-Bench Pro'를 적극 추천해왔습니다. 하지만 최근 OpenAI는 이 시험 문제의 약 30%가 잘못 구성되어 있어 결과의 신뢰성을 담보할 수 없다고 판단했습니다. 이에 따라 더 이상 공식적인 평가 기준으로 권장하지 않겠다고 발표했습니다 [Source 3, Source 11, Source 4].

### 이게 왜 중요한가요?

우리가 매일 사용하는 스마트폰 앱, 은행 시스템, 뉴스 서비스 등은 모두 개발자들이 작성한 코드로 움직입니다. 따라서 AI가 코딩을 얼마나 잘하느냐는 우리가 일상에서 접하는 기술이 얼마나 스마트해질지 결정하는 매우 중요한 척도입니다.

그런데 이 '코딩 실력'을 측정하는 시험 문제들이 쓸모없다면 어떻게 될까요? AI 기업들은 자신들의 모델이 더 뛰어나다는 것을 증명하기 위해 이 시험 성적을 활용해왔습니다. 만약 시험 자체가 잘못되었다면, 성능이 부풀려지거나 혹은 정당한 평가를 받지 못하는 왜곡된 결과가 나올 수 있습니다. 이는 곧 우리 소비자들이 접하는 AI 기술의 실질적인 진보 수준을 오해하게 만들 위험이 큽니다.

### 쉽게 이해하기: AI 코딩 시험의 비밀

코딩 시험은 보통 '유닛 테스트(Unit Test, 특정 기능을 코드가 잘 수행하는지 확인하는 자동화된 검사)'를 통해 점수를 매깁니다. 예를 들어, "이 버튼을 누르면 화면이 바뀌게 만들어봐"라는 문제에 대해 AI가 코드를 짜고, 테스트를 통과하면 정답으로 처리하는 방식입니다.

비유하자면 이런 식입니다. 요리 대회를 여는데 심사위원들이 '국물의 농도'를 측정하겠다며 정해둔 기준이, 알고 보니 엉뚱한 온도계였다고 해봅시다. 쉐프(AI)가 아무리 훌륭한 요리를 만들어도, 잘못된 온도계 때문에 실력이 낮게 측정되거나 반대로 엉뚱한 요리에 높은 점수를 주는 것과 다를 바 없습니다.

OpenAI는 이전에 'SWE-Bench Verified'라는 평가 도구도 사용했습니다. 하지만 이 역시 데이터 오염 문제와 함께, 시험 문제의 약 59%가 구조적 결함이 있다는 사실이 밝혀져 중단된 바 있습니다 [Source 2, Source 8, Source 13, Source 9].

이번에 권장이 중단된 SWE-Bench Pro 역시, 실제 GitHub(개발자들이 코드를 공유하는 플랫폼)의 복잡한 이슈들을 바탕으로 문제를 만들다 보니, AI가 단독으로 풀기에는 과제의 성격 자체가 모호하고 파편화되어 있다는 지적을 받아왔습니다 [Source 3, Source 14].

### 현재 상황: 진흙탕 속의 진주 찾기

현재 AI 모델들은 비약적으로 발전하고 있습니다. 하지만 그 성능을 측정하는 지표들은 아직 'AI 시대'에 맞는 완성도를 갖추지 못했습니다 [Source 6, Source 14].

SWE-Bench Pro는 Scale AI라는 회사가 2025년 9월에 내놓은 것으로, 기존보다 더 강력한 저작권 라이선스를 적용해 데이터 오염을 최소화하려 노력했습니다 [Source 7, Source 8]. 하지만 이번 발표를 통해, 아무리 정교하게 설계하려 해도 실제 개발 환경의 복잡함을 자동화된 시험으로 완벽히 옮겨오는 것이 얼마나 어려운 일인지 드러났습니다.

Scale AI의 연구 책임자인 빙 리우(Bing Liu)는 이번 결정이 과제의 모호함, 데이터 오염, 그리고 좁은 의미의 유닛 테스트만으로는 AI의 실력을 완벽히 측정할 수 없다는 한계를 잘 보여준다고 언급했습니다 [Source 14].

### 앞으로 어떻게 될까?

앞으로 AI의 코딩 실력을 평가하는 방식은 근본적인 변화를 겪을 것입니다.

1. **더 정교한 평가 표준**: 업계는 단순히 자동화된 점수에 의존하는 대신, AI가 문제를 해결하는 '과정'과 '복잡도'를 더 종합적으로 판단할 수 있는 새로운 표준을 만들려 노력할 것입니다 [Source 12].
2. **개발자와의 협업 강조**: AI가 혼자 코드를 짜는 것에서 나아가, 실제 개발자가 AI와 어떻게 소통하며 문제를 해결하는지를 평가하는 방식이 더 중요해질 것입니다.
3. **지속적인 검증**: 평가 데이터 자체가 오염되지 않도록 관리하는 것이 AI 모델 개발만큼이나 중요한 '기초 과학' 영역으로 자리 잡을 것입니다.

우리는 이제 AI가 스스로 코드를 짜는 시대를 살고 있습니다. 하지만 그 능력을 정확히 평가할 '온도계'를 만드는 것도 기술 발전 못지않은 중요한 과제임을 이번 사건은 우리에게 일깨워주고 있습니다.

---

## 참고자료

1. [OpenAI Abandons SWE-Bench Verified, Citing Widespread Data Contamination and Flawed Tests](https://www.siliconreport.com/openai-abandons-swe-bench-verified-citing-widespread-data-contamination-and-flawed-tests-6ebd9b34)
2. [OpenAI Retracts Recommendation To Use SWE Bench Pro As Coding Eval Over 30% Broken Tasks](https://officechai.com/ai/openai-retracts-recommendation-to-use-swe-bench-pro-as-coding-eval-over-30-broken-tasks/)
3. [OpenAI no longer recommends SWE-Bench Pro as coding benchmarks saturate](https://savedelete.com/news/openai-swe-bench/)
4. [Why we no longer evaluate SWE-bench Verified - keynews.ai](https://keynews.ai/articles/290)
5. [OpenAI Drops SWE-bench Verified: What It Means for AI](https://www.adwaitx.com/openai-swe-bench-verified-retired-ai-benchmarks/)
6. [OpenAI Abandons SWE-bench Verified: 59% Flawed Tests](https://byteiota.com/openai-abandons-swe-bench-verified-59-flawed-tests/)
7. [OpenAI Drops SWE-bench Verified Over Contamination Concerns](https://aibreakingwire.com/news/openai-ditches-swe-bench-verified-cites-critical-flaws/)
8. [OpenAI Retracts SWE-Bench Pro After Finding 30% of Tasks Broken | AlphaSignal](https://alphasignal.ai/news/openai-retracts-swe-bench-pro-after-finding-30-of-tasks-broken)
9. [OpenAI Developers on X](https://x.com/OpenAIDevs/status/2026002219909427270)
10. [OpenAI Abandons SWE-bench Verified After Finding 59% of Failed Tests Were Flawed](https://blockchain.news/news/openai-abandons-swe-bench-verified-contamination-flawed-tests)
11. [OpenAI moves beyond SWE-bench Verified as coding benchmarks saturate](https://tessl.io/blog/openai-moves-beyond-swe-bench-verified-as-coding-benchmarks-saturate/)