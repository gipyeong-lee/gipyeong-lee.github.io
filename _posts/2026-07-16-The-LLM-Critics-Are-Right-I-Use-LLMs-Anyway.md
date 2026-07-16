---
layout: post
title: "AI가 거짓말을 한다고? 그래도 우리가 LLM을 계속 쓰는 이유"
description: "AI의 환각 현상과 비판적 의견들 속에서도 왜 많은 사람들이 여전히 거대언어모델(LLM)을 활용하는지, 그 실질적인 가치와 미래를 알아봅니다."
summary: "AI에 대한 비판적 시각에도 불구하고, 기술의 진화와 보완책 덕분에 LLM은 여전히 강력한 도구로서 우리 일상과 업무의 생산성을 높이고 있습니다."
tags: [AI, LLM, 기술 트렌드, 생성형AI]
image: 2026-07-16-The-LLM-Critics-Are-Right-I-Use-LLMs-Anyway.jpg
image_alt: "복잡한 코드와 대화창이 겹쳐진 화면 위로 긍정적 검토와 비판적 검토가 오가는 모습을 상징적으로 나타낸 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "비판은 기술 성장의 거름입니다. LLM의 한계를 인지하고 이를 보완하는 '비평 모델'의 등장은 우리가 AI와 더 건강하게 공존할 수 있음을 보여줍니다."
quiz:
  - question: "LLM이 잘못된 정보를 자신 있게 답변하는 '환각 현상'이 발생하는 주요 원인 중 하나는 무엇인가요?"
    choices: ["인터넷의 편향된 데이터를 학습하기 때문", "컴퓨터 성능이 너무 낮기 때문", "단순히 전기를 많이 쓰기 때문"]
    answer: 0
    explanation: "LLM은 인터넷상의 방대한 데이터를 학습하는데, 여기에는 모순, 잘못된 정보, 의견이 포함되어 있으며 현재의 벤치마크 방식이 정확성보다 자신 있는 답변을 보상하기 때문입니다."
  - question: "최근 AI 개발 분야에서 코드의 버그를 찾기 위해 활용되는 '비평 모델(Critic Models)'이란 무엇인가요?"
    choices: ["인간의 감정을 읽는 모델", "다른 AI가 생성한 결과물을 평가하고 피드백을 주는 LLM", "AI의 전력 사용량을 계산하는 프로그램"]
    answer: 1
    explanation: "비평 모델은 인간의 피드백을 강화학습(RLHF)으로 학습하여, 다른 AI가 만든 코드나 결과물의 오류를 자연어 피드백으로 지적해 주는 역할을 합니다."
  - question: "일부 오픈소스 프로젝트가 LLM으로 생성된 기여(PR)를 거부하는 주된 이유는 무엇인가요?"
    choices: ["기여자가 너무 많아서", "오픈소스 정신과 맞지 않는 저작권 문제", "AI 생성물에 대한 신뢰성 및 시간 투입 확인의 어려움"]
    answer: 2
    explanation: "사람이 정성스럽게 작성한 코드인지, AI가 자동으로 찍어낸 코드인지 구분하기 어려워지면서 커뮤니티의 신뢰가 깨질 것을 우려하고 있습니다."
lang: ko
ref: 2026-07-16-The-LLM-Critics-Are-Right-I-Use-LLMs-Anyway
audio: 2026-07-16-The-LLM-Critics-Are-Right-I-Use-LLMs-Anyway.mp3
permalink: /2026/07/16/The-LLM-Critics-Are-Right-I-Use-LLMs-Anyway/
---

상상해보세요. 오늘 아침, 당신은 업무를 시작하며 AI에게 어제 정리해둔 수십 페이지의 계약서 초안을 넘겼습니다. 그리고 "주요 리스크 항목을 뽑아줘"라고 말했죠. AI는 순식간에 답을 내놓습니다. 그런데 문득 이런 생각이 듭니다. '이 내용, 정말 믿어도 되는 걸까? 혹시 AI가 자기 마음대로 없는 내용을 지어낸 건 아닐까?'

최근 생성형 AI, 특히 거대언어모델(LLM, Large Language Models)을 둘러싼 여론은 극명하게 갈립니다. 누군가는 AI가 우리 삶을 완전히 바꿔놓을 것이라며 환호하고, 또 누군가는 환각 현상(Hallucination, AI가 사실이 아닌 정보를 사실인 것처럼 꾸며내는 현상)과 환경적 영향, 신뢰성 문제를 지적하며 강력하게 비판합니다. 심지어 지그(Zig)나 젠투(Gentoo) 같은 오픈소스 소프트웨어 프로젝트들은 AI가 생성한 코드 기여를 거부하기도 합니다. [출처: The LLM Critics Are Right. I Use LLMs Anyway. | Jeremy Theocharis](https://www.theocharis.dev/blog/llm-critics-are-right-i-use-llms-anyway/)

하지만 비판이 거세짐에도 불구하고, 전 세계 수많은 사용자들은 여전히 매달 비용을 지불하면서까지 LLM을 사용하고 있습니다. [출처: 2025: The Year in LLMs | Hacker News](https://news.ycombinator.com/item?id=46449643) 도대체 왜 비판과 사용이 공존하는 것일까요?

## 이게 왜 중요한가요?

단순히 AI가 '신기해서' 사용하는 시대는 지났습니다. 이제는 AI가 업무의 효율성을 결정짓는 필수 도구로 자리 잡고 있습니다. 개발자들에게 LLM은 복잡한 함수 구조를 설계할 때 훌륭한 파트너가 되어줍니다. [출처: Here’s how I use LLMs to help me write code](https://simonwillison.net/2025/Mar/11/using-llms-for-code/) 하지만 신뢰 문제가 해결되지 않으면, 중요한 결정이 필요한 비즈니스 현장에서 AI를 안심하고 사용할 수 없습니다.

비판가들의 목소리는 AI를 더 안전하게 만드는 '가드레일' 역할을 합니다. 그들이 지적하는 환각 현상은 사실 LLM이 학습한 인터넷 데이터 자체가 모순과 편견으로 가득 차 있고, 모델들이 정확성보다는 '사용자가 좋아할 만한 자신 있는 답변'을 하도록 훈련받았기 때문에 발생하는 부산물입니다. [출처: It's 2026. Why Are LLMs Still Hallucinating? - Duke University Libraries](https://blogs.library.duke.edu/blog/2026/01/05/its-2026-why-are-llms-still-hallucinating/) 우리가 이 문제를 직시할수록 기술은 더 정교해집니다.

## 쉽게 이해하기: 초능력 도서관 사서

LLM을 쉽게 비유하자면, 세상의 모든 책과 인터넷 글을 읽은 '초능력 도서관 사서'라고 할 수 있습니다. 이 사서는 수많은 패턴을 학습하여 우리가 질문할 때 가장 그럴듯한 답변을 빠르게 찾아주죠. [출처: Part 1: How to Apply LLMs and AI to Contracts](https://www.knowable.com/blog/part-1-how-to-apply-llms-and-ai-to-contracts-what-are-llms-anyway/)

하지만 때로는 그 방대한 지식 속에서 엉뚱한 내용을 섞어버리기도 합니다. 마치 사서가 너무 많은 책을 읽은 나머지, 허구의 소설 속 내용을 실제 역사적 사실로 착각해 설명하는 것과 비슷합니다. 그래서 최근에는 이 사서의 답변을 옆에서 감시하는 '비평가'를 두는 방식이 도입되고 있습니다.

'비평 모델(Critic Models)'은 다른 AI가 쓴 코드를 꼼꼼히 읽고, 논리적 오류가 있는지, 보안상 위험하지는 않은지 마치 동료 개발자처럼 피드백을 주는 LLM입니다. [출처: LLM Critics Help Catch LLM Bugs | Athina AI](https://blog.athina.ai/llm-critics-help-catch-llm-bugs) 실제로 비평 모델인 'CriticGPT'는 사람이 직접 코드의 버그를 찾는 것보다 더 뛰어난 성능을 보이기도 했습니다. [출처: LLM Critics: A New Weapon in the Fight Against AI Bugs](https://medium.com/@ayoubkirouane3/llm-critics-a-new-weapon-in-the-fight-against-ai-bugs-f258a6b7cf91)

## 현재 우리는 어디에 서 있나요?

오늘날의 LLM들은 문맥을 파악해 다음 단어를 예측하는 '디코더 스타일 트랜스포머' 구조를 기반으로 작동하지만, 내부적으로는 훨씬 똑똑해졌습니다. 전문가 집단을 연상시키는 '전문가 혼합(MoE, Mixture-of-Experts) 구조'를 사용하여, 질문의 성격에 따라 가장 적합한 작은 모델들을 활성화하는 방식으로 효율을 높이고 있습니다. [출처: The State Of LLMs 2025: Progress, Progress, and Predictions](https://magazine.sebastianraschka.com/p/state-of-llms-2025)

그러나 분명한 한계도 존재합니다. MIT 연구에 따르면, 모델이 학습 과정에서 잘못된 상관관계를 형성하여 겉보기엔 완벽하지만 논리적으로는 실패하는 '합성적 오류'가 발생하기도 합니다. [출처: Researchers discover a shortcoming that makes LLMs less reliable](https://news.mit.edu/2025/shortcoming-makes-llms-less-reliable-1126) 이는 우리가 AI의 답변을 맹신해서는 안 되며, 여전히 '검증하는 사용자'가 반드시 필요하다는 사실을 증명합니다.

## AI의 미래: 협업하는 비서

앞으로 차세대 LLM은 지금보다 훨씬 더 저렴하고 효율적으로 변할 것입니다. [출처: LLMs+: 10 Things That Matter in AI Right Now](https://www.technologyreview.com/2026/04/21/1135645/llm-large-language-models-ai/) 단순히 더 많은 데이터를 쏟아붓는 것이 아니라, 우리가 고민하는 오류를 찾아내고 스스로 수정하는 능력이 강화될 것입니다.

우리는 AI를 '모든 것을 아는 완벽한 정답지'로 생각하는 단계에서 벗어나, '협업하는 창의적인 비서'로 바라보는 태도가 필요합니다. 비판은 기술을 멈추게 하는 것이 아니라, 기술이 올바른 방향으로 나아가게 하는 등불입니다. LLM의 한계를 인지하고, 그 위에서 비판적으로 도구를 활용할 때 비로소 우리는 AI 시대의 진짜 주인이 될 수 있을 것입니다.

## AI의 한마디

비판은 기술 성장의 거름입니다. LLM의 한계를 인지하고 이를 보완하는 '비평 모델'의 등장은 우리가 AI와 더 건강하게 공존할 수 있음을 보여줍니다.

## 참고자료

1. [How I use LLMs - YouTube](https://www.youtube.com/watch?v=EWvNQjAaOHw)
2. [As an Experienced LLM User, I Actually Don’t Use Generative LLMs...](https://minimaxir.com/2025/05/llm-use/)
3. [LLM Critics Help Catch LLM Bugs | Athina AI](https://blog.athina.ai/llm-critics-help-catch-llm-bugs)
4. [Using ChatGPT is not bad for the environment](https://blog.andymasley.com/p/individual-ai-use-is-not-bad-for)
5. [Bad (but common) LLM criticisms - Ritza Articles](https://ritza.co/articles/gareth/bad-llm-criticisms/)
6. [Part 1: How to Apply LLMs and AI to Contracts: What are LLMs anyway? - Knowable](https://www.knowable.com/blog/part-1-how-to-apply-llms-and-ai-to-contracts-what-are-llms-anyway/)
7. [Here’s how I use LLMs to help me write code](https://simonwillison.net/2025/Mar/11/using-llms-for-code/)
8. [LLMs+: 10 Things That Matter in AI Right Now | MIT Technology Review](https://www.technologyreview.com/2026/04/21/1135645/llm-large-language-models-ai/)
9. [It's 2026. Why Are LLMs Still Hallucinating? - Duke University Libraries](https://blogs.library.duke.edu/blog/2026/01/05/its-2026-why-are-llms-still-hallucinating/)
10. [Assessing the Strengths and Weaknesses of Large Language Models](https://link.springer.com/article/10.1007/s10849-023-09409-x)
11. [LLM Critics: A New Weapon in the Fight Against AI Bugs](https://medium.com/@ayoubkirouane3/llm-critics-a-new-weapon-in-the-fight-against-ai-bugs-f258a6b7cf91)
12. [LLM News, Updates and Articles](https://llm-explorer.com/static/llm-news/)
13. [The State Of LLMs 2025: Progress, Progress, and Predictions](https://magazine.sebastianraschka.com/p/state-of-llms-2025)
14. [The LLM Critics Are Right. I Use LLMs Anyway. | Jeremy Theocharis](https://www.theocharis.dev/blog/llm-critics-are-right-i-use-llms-anyway/)
15. [Researchers discover a shortcoming that makes LLMs less reliable | MIT News](https://news.mit.edu/2025/shortcoming-makes-llms-less-reliable-1126)
16. [2025 LLM Year in Review – karpathy](https://karpathy.bearblog.dev/year-in-review-2025/)
17. [2025: The Year in LLMs | Hacker News](https://news.ycombinator.com/item?id=46449643)