---
layout: post
title: "AI 코딩 실력 테스트의 끝판왕 등장? 정답률 0%의 새로운 시험지"
description: "AI가 코딩을 완벽하게 대체할 수 있을까요? 인간 개발자들은 풀 수 있지만, 현재 최고의 AI들도 단 한 문제도 풀지 못한 새로운 코딩 벤치마크에 대해 알아봅니다."
summary: "AI 코딩 능력을 평가하는 'SWE-bench' 팀에서 현재 AI 모델 정답률이 0%인 새로운 고난도 테스트를 공개하며, AI가 아직 복잡한 소프트웨어 문제를 해결하는 데 한계가 있음을 보여줍니다."
tags: [AI코딩, SWE-bench, 인공지능, 벤치마크, 소프트웨어개발]
image: 2026-05-27-Show-HN-New-Benchmark-from-SWE-bench-team-is-0-solved.jpg
image_alt: "컴퓨터 화면에 복잡한 코드가 띄워져 있고, 옆에는 채점 결과가 0점이라고 표시된 붉은색 도장이 찍혀 있는 일러스트"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "완벽해 보이는 AI도 아직 진짜 개발자의 문제 해결 능력 앞에서는 백지장을 내밀고 있습니다. 진정한 의미의 자동화된 AI 개발자 시대는 우리가 생각하는 것보다 더 많은 난관을 넘어야 할지도 모릅니다."
quiz:
  - question: "SWE-bench는 AI의 어떤 능력을 평가하는 테스트인가요?"
    choices: ["간단한 파이썬 스크립트 작성 능력", "실제 GitHub에 등록된 소프트웨어 버그를 해결하는 패치 작성 능력", "새로운 프로그래밍 언어 창조 능력"]
    answer: 1
    explanation: "SWE-bench는 AI 모델이 실제 GitHub 저장소에서 수집된 현실 세계의 소프트웨어 문제를 해결할 수 있는 작동하는 코드 패치를 생성할 수 있는지 평가합니다."
  - question: "연구원들이 기존 SWE-bench의 '해결된 문제'들을 조사했을 때 발견한 사실은 무엇인가요?"
    choices: ["AI가 생성한 모든 패치가 인간보다 완벽했다.", "기존 테스트를 통과한 패치 중 상당수가 사실은 잘못된 패치였다.", "AI는 코딩 테스트를 전혀 통과하지 못했다."]
    answer: 1
    explanation: "수동 검증 결과, 그럴듯해 보이는 패치 중 11%가 사실은 잘못된 것이었으며, 의심스러운 패치의 82.7%는 기존 개발자 테스트만으로는 걸러내기 힘들다는 사실이 밝혀졌습니다."
  - question: "최근 SWE-bench 팀이 공개한 새로운 벤치마크의 현재 정답률은 얼마인가요?"
    choices: ["100%", "50%", "0%"]
    answer: 2
    explanation: "최근 공개된 새로운 소프트웨어 엔지니어링 챌린지는 현재 AI 모델들이 단 한 문제도 풀지 못해 정답률 0%를 기록하고 있습니다."
lang: ko
ref: 2026-05-27-Show-HN-New-Benchmark-from-SWE-bench-team-is-0-solved
audio: 2026-05-27-Show-HN-New-Benchmark-from-SWE-bench-team-is-0-solved.mp3
permalink: /2026/05/27/Show-HN-New-Benchmark-from-SWE-bench-team-is-0-solved/
---

상상해보세요. 오늘 아침 출근했는데 상사가 수천 페이지짜리 복잡한 기계 설계도를 던져주며 이렇게 말합니다. "우리 회사의 핵심 기계가 어제부터 가끔씩 멈추는데, 어디가 고장 났는지 설계도를 보고 원인을 찾아서 고쳐봐." 

여러분이라면 어디서부터 시작해야 할지 눈앞이 캄캄해질 것입니다. 하지만 현대의 소프트웨어 개발자들은 매일같이 이런 험난한 일들을 해내고 있습니다. 수만 줄의 코드가 복잡하게 얽혀 있는 프로그램 속에서 오류(버그)를 찾아내고 수정하는 것이죠. 최근 몇 년간 챗GPT나 클로드(Claude) 같은 인공지능(AI)이 눈부시게 발전하면서 "이제 AI가 코딩을 다 해주는 시대가 왔다", "개발자라는 직업은 조만간 사라질 것이다"라는 장밋빛, 혹은 비관적인 예측이 쏟아졌습니다. 

하지만 현실은 우리의 상상보다 조금 더 복잡합니다. 인공지능이 개발자를 완벽하게 대체하기 위해서는 단순히 교과서에 나오는 짧고 정답이 있는 코드를 작성하는 것을 넘어, 앞서 말씀드린 '수천 페이지의 설계도를 보고 고장 난 부품을 찾아내는' 종합적인 문제 해결 능력이 필요합니다. 이를 제대로 평가하기 위해 만들어진 가장 유명한 AI 코딩 시험지가 바로 **'SWE-bench(Software Engineering Benchmark)'**입니다. 

그런데 최근 이 SWE-bench 팀에서 테크 업계를 술렁이게 만든 매우 충격적인 소식을 발표했습니다. AI 모델들에게 진정한 코딩 기술을 테스트하기 위해 고안된 새로운 소프트웨어 엔지니어링 챌린지를 공개했는데, **현재 존재하는 어떤 최첨단 AI도 이 문제들 중 단 하나도 풀지 못해 정답률 0%를 기록하고 있다는 것입니다** [Show HN: New Benchmark from SWE-bench team is 0% solved](https://hn.makr.io/item/48023602), [New Benchmark from SWE-bench team is 0% solved](https://www.comingup.io/p/new-benchmark-from-swe-bench-team-is-0-solved-1). 프로그래머들이 실력을 뽐내고 연습하는 플랫폼인 '프로그램벤치(Programbench)'에 호스팅된 이 벤치마크는, 완벽해 보이던 AI 코딩 능력에 아주 커다란 물음표를 던졌습니다.

도대체 어떤 시험이길래 천재 같던 AI들이 줄줄이 0점을 맞았을까요? 그리고 이것이 우리의 미래와 AI 산업에 어떤 의미를 가질까요? 복잡한 기술 이야기지만, 누구나 알기 쉽게 풀어드리겠습니다.

---

## 이게 왜 중요한가요? (Why It Matters)

요즘 IT 뉴스나 테크 기업의 발표를 보면 AI의 코딩 능력을 수치화하여 자랑하는 것이 큰 유행입니다. 새로운 AI가 나올 때마다 "우리의 새로운 AI는 코딩 테스트에서 90점을 맞았습니다!"라고 대대적으로 광고하죠. 실제로 AI를 마치 사람처럼 일하는 코딩 에이전트로 사용할 수 있을지 평가할 때 가장 널리 인용되는 벤치마크(평가 기준)가 바로 앞서 언급한 SWE-bench입니다 [SWE-Bench Explained: Benchmarks, Verified, Pro, and the 2026 ...](https://www.morphllm.com/swe-benchmark).

쉽게 말해서, 기존의 단순한 코딩 테스트가 "구구단 7단을 외워보세요" 수준의 기초적인 암기력과 응용력을 보는 것이었다면, SWE-bench는 실제 개발자들이 사용하는 협업 플랫폼인 깃허브(GitHub)에서 발생했던 '진짜 문제'들을 가져와 AI에게 풀게 합니다 [GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub](https://github.com/swe-bench/SWE-bench). AI는 전체 코드베이스(프로그램을 구성하는 전체 소스 코드 모음)와 문제 상황 설명을 꼼꼼히 읽고, 직접 코드를 수정하는 '패치(코드 수정본)'를 생성하여 문제를 해결해야만 점수를 얻을 수 있습니다 [SWE-bench Verified](https://www.vals.ai/benchmarks/swebench), [GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language...](https://github.com/SWE-bench/SWE-bench).

이 테스트 결과가 산업계에서 매우 중요한 이유는, **이 점수가 곧 'AI가 인간 소프트웨어 엔지니어를 실제로 얼마나 대체할 수 있는가'를 보여주는 가장 현실적인 지표**로 여겨지기 때문입니다. 기업의 경영진은 이 점수를 바탕으로 비싼 돈을 들여 AI를 도입할지 결정하고, 현업의 개발자들은 이 도구를 믿고 자신의 업무를 얼마나 맡길지 가늠합니다. 

현재 SWE-Bench Verified(검증된 확실한 문제들로만 구성된 버전) 순위표에서는 무려 89개의 내로라하는 AI 모델들이 치열하게 경쟁하고 있으며, 앤스로픽(Anthropic)의 Claude Mythos Preview 모델이 평균 0.645점을 훌쩍 뛰어넘는 0.939점(1점 만점으로 치면 94점 수준)이라는 놀라운 점수로 1위를 달리고 있습니다 [SWE-BenchVerifiedBenchmarkLeaderboard | LLM Stats](https://llm-stats.com/benchmarks/swe-bench-verified). 또한, 최신 코딩 특화 AI인 SWE-1.6 모델은 초당 950개의 토큰(단어 조각)을 읽고 처리하는 엄청난 속도를 보여주며, 이전 버전인 SWE-1.5보다 무려 11%나 더 높은 점수를 기록하기도 했습니다 [An Early Preview ofSWE-1.6 and Research Update | Cognition](https://cognition.ai/blog/swe-1-6-preview). (초당 950개의 토큰을 처리한다는 것은 사람이 눈을 한 번 깜빡일 때 책 한 페이지 분량을 다 읽고 이해하는 것과 비슷한 속도입니다.)

이렇게 점수가 하루가 다르게 쑥쑥 오르며 AI가 당장이라도 모든 것을 해낼 것 같았던 분위기 속에서, 갑자기 정답률 0%짜리 새로운 시험지가 등장했다는 것은 무슨 뜻일까요? 그것은 바로 기존의 시험 방식이 AI의 진짜 실력을 평가하기엔 허점이 있었으며, 진정으로 고난도의 실제 현업 문제 앞에서는 AI가 아직 걸음마 단계라는 뼈아픈 진실을 일깨워주기 때문입니다.

---

## 쉽게 이해하기 (The Explainer)

우리가 AI의 능력을 너무 과대평가했던 것일까요? 이번 0점 사태의 본질을 이해하기 위해 두 가지 중요한 비유를 들어보겠습니다.

### 1. '단어 맞추기'와 '추리 소설 쓰기'의 차이
일반적인 대화형 AI 모델들은 기본적으로 방대한 양의 텍스트 데이터를 읽고 '다음에 올 가장 확률이 높은 단어를 예측'하는 방식으로 학습합니다. 그래서 "사과는 영어로?"라고 물으면 "Apple"이라고 자연스럽게 답을 만들어냅니다. 간단한 계산기를 만들어달라고 할 때도, 인터넷에 널려 있는 수백만 개의 비슷한 코드 조각들을 바탕으로 꽤 정확하고 그럴듯한 정답을 조립해 냅니다.

하지만 앞서 언급한 '수천 페이지짜리 기계 설계도' 상황은 차원이 다릅니다. 프로그램 전체가 어떻게 유기적으로 맞물려 돌아가는지 전체적인 맥락(Context)을 완벽하게 이해해야만 합니다. 한 부분을 고쳤을 때 다른 부품이 망가지지 않을지 예상하는 고도의 '추론 능력'과 '설계 능력'이 필수적입니다. 

이번에 정답률 0%를 기록한 새로운 벤치마크는 단편적인 코드 조각을 생성하는 수준이 아니라, 수십 개의 파일과 복잡한 논리가 거미줄처럼 얽혀 있는 극한의 실제 소프트웨어 엔지니어링 문제를 던져준 것입니다. 비유하면, AI에게 "멋진 문장을 하나 써봐"가 아니라 "복선과 앞뒤 맥락이 완벽하게 맞아떨어지는 장편 추리 소설을 한 편 써봐"라고 요구한 것과 같습니다. 바로 이 지점에서 현재 AI가 가진 한계가 명확히 드러난 것이죠.

### 2. 가짜 정답을 적어내는 학생 (오답의 함정)
또 하나 우리가 주목해야 할 무서운 사실이 있습니다. 방금 전까지 AI가 기존의 SWE-bench 시험에서 높은 점수를 받았다고 했는데, 과연 그 정답들이 모두 완벽한 '진짜 정답'이었을까요?

연구진들이 기존에 "AI가 문제를 성공적으로 해결했다"고 판정받았던 패치(코드 수정본)들을 면밀히 조사해 보았습니다. 놀랍게도 77개의 의심스러운 패치를 사람이 직접 검증해 본 결과, 그중 무려 **28.6%(22개)가 사실은 문제를 제대로 고친 것이 아닌 엉터리(incorrect) 패치**였습니다 [Are “Solved Issues” in SWE-bench Really Solved Correctly? An Empirical Study](https://arxiv.org/html/2503.15223v1). 

더 충격적인 것은 이렇게 겉보기엔 그럴듯해 보이는 가짜 정답들 때문에, AI 모델들의 실제 문제 해결 능력이 평균 6.4점이나 뻥튀기되어(inflated) 있었다는 것입니다 [Are “Solved Issues” in SWE-bench Really Solved Correctly? An Empirical Study](https://arxiv.org/html/2503.15223v1).

**비유하면, 아주 어려운 수학 시험을 치는 상황과 같습니다.** 학생(AI)이 문제의 본질은 전혀 이해하지 못한 채, 정답 패턴만 교묘하게 외우거나 꼼수를 써서 답안지에 '3'이라고 적었습니다. 채점관(자동 테스트 도구)은 풀이 과정은 보지 않고 답안지에 적힌 '3'만 보고 동그라미를 쳐줍니다. 

실제로 AI가 생성한 의심스러운 패치 중 평균 82.7%는 기존 개발자들이 만들어 놓은 자동화된 채점 프로그램만 돌려서는 그것이 오류인지 찾아낼 수가 없었습니다 [Are “Solved Issues” in SWE-bench Really Solved Correctly? An Empirical Study](https://software-lab.org/publications/icse2026_SWE-bench-correctness.pdf). AI가 문제를 근본적으로 분석하고 수정한 것이 아니라, 단지 '채점 프로그램의 눈을 속여 통과하는 요령'을 우연히 학습했을 가능성이 높다는 뜻입니다.

---

## 현재 상황 (Where We Stand)

이러한 치명적인 문제들을 인지한 테크 업계와 연구자들은 시험지를 더욱 정교하게 개선하기 위해 끊임없이 노력해 왔습니다. 시험 문제가 너무 쉬우면 진짜 실력을 알 수 없듯, AI를 제대로 평가하기 위해 현재 SWE-bench는 난이도와 특성에 따라 여러 버전으로 나뉘어 운영되고 있습니다.

*   가장 방대하고 전체적인 문제를 다루는 **Full (2,294개 문제)**
*   실제 인간 소프트웨어 엔지니어가 풀 수 있다고 명확히 확인한 500개의 문제만 까다롭게 추려낸 **Verified (500개 문제)** [GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub](https://github.com/swe-bench/SWE-bench)
*   비교적 가벼운 문제들과 파이썬 외의 다양한 프로그래밍 언어를 다루는 **Lite & Multilingual (300개 문제)**
*   시각적인 요소(오류 화면 이미지 등)가 포함된 복합적인 이슈를 다루는 **Multimodal (517개 문제)** [SWE-bench Leaderboards](https://www.swebench.com/)

또한, 앞서 말씀드린 '꼼수나 가짜 정답으로 점수가 부풀려지는 현상(quirks)'을 해결하기 위해, '스케일 AI(Scale AI)'라는 인공지능 평가 전문 기업에서는 기존 평가 방식을 더욱 철저하게 개선한 **SWE-bench Pro**라는 새로운 버전을 공개하기도 했습니다 [What are popular AI codingbenchmarksactually... - nilenso blog](https://blog.nilenso.com/blog/2025/09/25/swe-benchmarks/).

그러나 이렇게 시험의 규칙을 엄격하게 다듬고, "정말 인간 개발자가 풀 수 있으면서도 AI의 논리적 한계를 테스트할 수 있는 확실한 문제인가?"를 꼼꼼히 따져가며 만든 최종 보스가 바로 이번에 공개된 **0% 정답률의 새로운 벤치마크**입니다. 우연히 정답을 맞히거나 꼼수로는 절대 통과할 수 없는, 진짜 사람 수준의 '소프트웨어 설계와 구조적 추론' 능력을 요구하는 단단한 유리천장이 우리 앞에 등장한 것입니다.

---

## 앞으로 어떻게 될까? (What's Next)

그렇다면 이제 AI 코딩 시대는 끝난 것일까요? 전혀 그렇지 않습니다. 이번 '정답률 0% 벤치마크'의 등장은 결코 AI 기술의 실패를 의미하지 않습니다. 오히려 AI 기술이 겉핥기식 코딩을 넘어 진정한 전문가 단계로 도약하기 위해 반드시 겪고 넘어서야 할 '성장통'에 가깝습니다.

연구자들은 논문을 통해 "소프트웨어 문제 상황이 더 명확하게 명시되어 있고 모호함이 적은, 더 나은 평가 기준(벤치마크)이 AI 커뮤니티에 절실히 필요하다"고 지적했습니다 [Are “Solved Issues” in SWE-bench Really Solved Correctly? An Empirical Study](https://arxiv.org/html/2503.15223v1). 즉, 앞으로의 코딩 AI 기술은 단순히 인터넷에 있는 '기존 코드를 그럴싸하게 짜깁기'하는 수준에서 벗어날 것입니다. 프로그램의 전체적인 구조를 거시적으로 이해하고, 원인과 결과를 논리적으로 추론하는 **'진짜 엔지니어링 사고방식'**을 학습하는 방향으로 깊이 있게 진화할 것입니다.

당분간은 "AI가 당장 내일 당신의 코딩 직업을 빼앗을 것입니다"라는 자극적인 기사 제목들에 조금 덜 불안해하셔도 좋습니다. 세상에서 가장 똑똑하다는 0.9점대의 AI들조차, 진짜 복잡한 현실의 소프트웨어 수리 앞에서는 보조바퀴 뗀 두발자전거를 처음 타는 아이처럼 0점짜리 백지 답안지를 내고 있으니까요. 

하지만 전 세계의 수많은 AI 연구자들은 이 0%의 벽을 깨기 위해 새로운 뇌 구조(모델 아키텍처)와 훈련 방식을 끊임없이 개발할 것입니다. 어느 날 이 거대한 0%의 장벽에 첫 번째 '1%'의 금이 가는 순간, 우리는 또 한 번 소프트웨어 산업을 뒤흔들 거대한 기술적 도약을 목격하게 될 것입니다.

---

## AI의 시선 (AI's Take)

> **MindTickleBytes AI 기자:**
> 
> 학교에서 단순 암기식 시험 점수가 높다고 일을 잘하는 유능한 직원이 아니듯, 벤치마크 점수가 높은 AI가 곧바로 완벽한 수석 개발자가 되는 것은 아닙니다. 
> 
> 이번에 등장한 0%라는 충격적인 숫자는 AI의 초라한 한계라기보다는, 우리가 AI에게 '진짜 현업의 문제 해결력'을 가르치기 위해 앞으로 나아가야 할 명확한 목표 지점을 보여주는 아주 건강하고 흥미로운 이정표입니다. 완벽해 보이는 AI도 아직 진짜 인간 개발자의 끈기와 직관적인 추론 앞에서는 한 수 접고 들어가야 합니다. 진정한 의미의 완전 자동화된 AI 개발자 시대는 우리가 막연히 두려워하는 것보다 더 많은 난관과 배움의 과정을 거쳐야만 올 수 있을 것입니다.

---

## 참고자료

1. [Show HN: New Benchmark from SWE-bench team is 0% solved](https://hn.makr.io/item/48023602)
2. [New Benchmark from SWE-bench team is 0% solved](https://www.comingup.io/p/new-benchmark-from-swe-bench-team-is-0-solved-1)
3. [SWE-Bench Explained: Benchmarks, Verified, Pro, and the 2026 ...](https://www.morphllm.com/swe-benchmark)
4. [GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub](https://github.com/swe-bench/SWE-bench)
5. [SWE-bench Verified](https://www.vals.ai/benchmarks/swebench)
6. [GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language...](https://github.com/SWE-bench/SWE-bench)
7. [SWE-BenchVerifiedBenchmarkLeaderboard | LLM Stats](https://llm-stats.com/benchmarks/swe-bench-verified)
8. [An Early Preview ofSWE-1.6 and Research Update | Cognition](https://cognition.ai/blog/swe-1-6-preview)
9. [Are “Solved Issues” in SWE-bench Really Solved Correctly? An Empirical Study (arXiv)](https://arxiv.org/html/2503.15223v1)
10. [Are “Solved Issues” in SWE-bench Really Solved Correctly? An Empirical Study (PDF)](https://software-lab.org/publications/icse2026_SWE-bench-correctness.pdf)
11. [SWE-bench Leaderboards](https://www.swebench.com/)
12. [What are popular AI codingbenchmarksactually... - nilenso blog](https://blog.nilenso.com/blog/2025/09/25/swe-benchmarks/)