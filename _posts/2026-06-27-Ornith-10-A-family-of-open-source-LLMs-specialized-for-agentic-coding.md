---
layout: post
title: "AI가 스스로 '시험 문제'를 만든다고? 코딩 에이전트의 새로운 진화, Ornith-1.0"
description: "딥레인포스(Deep Reinforce)가 공개한 오픈소스 코딩 AI 'Ornith-1.0'은 스스로 코딩 환경을 구축하며 문제를 해결합니다. 일반인을 위한 쉬운 해설."
summary: "Ornith-1.0은 스스로 필요한 테스트 환경(스캐폴드)을 설계하고 학습하는 능력을 갖춘 최신 오픈소스 코딩 AI 모델입니다."
tags: [AI, 코딩, 오픈소스, 기술트렌드]
image: 2026-06-27-Ornith-10-A-family-of-open-source-LLMs-specialized-for-agentic-coding.jpg
image_alt: "Ornith-1.0 로고와 함께 복잡한 코딩 로직이 스스로 재구성되는 디지털 그래픽"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "인간이 만든 틀에 갇히지 않고 AI 스스로 시행착오의 기준을 만드는 능동적 학습 방식은 코딩 에이전트의 수준을 한 단계 높일 것입니다."
quiz:
  - question: "Ornith-1.0 모델이 이전 코딩 AI와 차별화되는 가장 큰 특징은 무엇인가요?"
    choices: ["인터넷 검색 속도 향상", "스스로 문제 해결을 위한 테스트 환경(스캐폴드)을 구축", "이미지 생성 기능 추가"]
    answer: 1
    explanation: "Ornith-1.0은 강화학습을 통해 코딩 문제를 해결하는 것뿐만 아니라, 그 문제를 검증할 환경(스캐폴드)까지 스스로 설계합니다."
  - question: "Ornith-1.0 모델은 어떤 라이선스로 공개되었나요?"
    choices: ["비공개 독점 라이선스", "GPL 라이선스", "MIT 라이선스"]
    answer: 2
    explanation: "Ornith-1.0은 MIT 라이선스로 공개되어 연구용은 물론 상업적 목적으로도 자유롭게 활용할 수 있습니다."
  - question: "Ornith-1.0 모델의 학습에 기반이 된 기존 모델은 무엇인가요?"
    choices: ["Gemma 4와 Qwen 3.5", "GPT-4o", "Llama 3"]
    answer: 0
    explanation: "Ornith-1.0은 기존의 강력한 모델인 Gemma 4와 Qwen 3.5를 바탕으로 추가 학습(포스트 트레이닝)되었습니다."
lang: ko
ref: 2026-06-27-Ornith-10-A-family-of-open-source-LLMs-specialized-for-agentic-coding
audio: 2026-06-27-Ornith-10-A-family-of-open-source-LLMs-specialized-for-agentic-coding.mp3
permalink: /2026/06/27/Ornith-10-A-family-of-open-source-LLMs-specialized-for-agentic-coding/
---

상상해보세요. 당신이 유능한 개발자에게 복잡한 소프트웨어 버그 수정을 부탁했습니다. 그런데 이 개발자는 단순히 코드만 고치는 게 아니라, 그 버그가 정말로 고쳐졌는지 확인하기 위해 필요한 모든 테스트 도구와 환경까지 스스로 뚝딱 만들어낸다면 어떨까요? 마치 마법처럼 말이죠.

최근 인공지능 연구소 딥레인포스(Deep Reinforce)가 공개한 새로운 AI 모델 가족, **Ornith-1.0**이 바로 이런 놀라운 능력을 보여줍니다. 지금까지 코딩하는 AI는 많았지만, Ornith-1.0은 숙련된 엔지니어처럼 스스로 문제를 해결할 '무대'를 직접 설계한다는 점에서 차원이 다른 진화를 보여줍니다.

## 이게 왜 중요한가요?

지금까지 대부분의 코딩 AI는 인간이 정해준 규칙 안에서 답을 찾는 데 그쳤습니다. 하지만 현실 세계의 코딩은 '정답'이 하나로 정해져 있지 않습니다. 무엇이 문제인지 파악하고, 이를 검증하는 테스트 환경을 구축하고, 수정 후 다시 확인하는 복잡한 과정이 필수적이죠. [출처: Ornith1.0: SelfLearningLLM forCoding| by Mehul Gupta | Medium](https://medium.com/data-science-in-your-pocket/ornith-1-0-self-learning-llm-for-coding-318c9a830bfc)

Ornith-1.0과 같은 '에이전트형 코딩 모델'은 AI가 단순히 다음 단어를 예측하는 수준을 넘어, 소프트웨어 엔지니어링의 전체 과정을 스스로 수행할 수 있게 만듭니다. 게다가 이 모델들은 오픈소스로 공개되어, 전 세계 개발자들이 기업 규모에 상관없이 최첨단 기술을 자신의 서비스에 도입할 수 있게 되었습니다. [출처: DeepReinforce ReleasesOrnith-1.0:AnOpen-SourceCodingModel...](https://www.marktechpost.com/2026/06/25/deepreinforce-releases-ornith-1-0-an-open-source-coding-model-family-that-learns-its-own-rl-scaffolds/)

## 쉽게 이해하기: '스스로 부엌을 만드는 요리사'

Ornith-1.0의 핵심은 **'스스로 만드는 테스트 환경(Self-Scaffolding)'**에 있습니다.

쉽게 비유해 볼까요? 우리가 요리사를 채용한다고 가정해 봅시다. 기존의 AI가 레시피만 보고 요리하는 로봇이었다면, Ornith-1.0은 요리를 하기 전에 부엌 설비부터 확인합니다. 만약 가스레인지가 부족하면 스스로 버너를 설치하고, 재료의 신선도를 체크할 도구가 없으면 그 도구까지 직접 만들어서 요리를 시작하는 셈입니다.

여기서 '스캐폴드(Scaffold, 발판)'란 코드가 제대로 작동하는지 검증하기 위한 일종의 테스트 설계도입니다. 기존 모델들은 인간이 미리 만들어둔 테스트 환경에 의존했지만, Ornith-1.0은 **강화학습(Reinforcement Learning, 정답을 맞히면 상을 받는 식으로 시행착오를 거치며 학습하는 방식)**을 통해 문제 해결책과 그 결과를 검증할 무대를 동시에 최적화합니다. [출처: Ornith on X: "Aloha! 🌺 Meet Ornith-1.0..."](https://x.com/ornith_/status/2070148887067963854) [출처: Open-Source Coding Model Ornith-1.0 Writes Its Own Training Scaffold in Reinforcement Learning](https://www.techtimes.com/articles/319122/20260626/open-source-coding-model-ornith-10-writes-its-own-training-scaffold-reinforcement-learning.htm)

## 어디까지 왔을까?

딥레인포스는 사용자의 환경에 맞춰 선택할 수 있도록 다양한 모델을 공개했습니다. 가볍고 빠른 9B(90억 개 파라미터) 모델부터, 거대한 규모를 자랑하는 397B(3,970억 개 파라미터) '전문가 혼합(MoE, 여러 개의 작은 모델을 효율적으로 조합한 방식)' 모델까지 선택의 폭이 넓습니다. [출처: DeepReinforce ReleasesOrnith-1.0:AnOpen-SourceCodingModel...](https://www.marktechpost.com/2026/06/25/deepreinforce-releases-ornith-1-0-an-open-source-coding-model-family-that-learns-its-own-rl-scaffolds/)

성능 또한 눈부십니다. 실제 코딩 문제를 해결하는 능력을 측정하는 유명한 시험대인 'SWE-Bench Verified'에서 82.4점이라는 높은 점수를 기록했습니다. 이는 기존 오픈소스 모델 중 단연 최고 수준입니다. [출처: Ornith on X: "Aloha! 🌺 Meet Ornith-1.0..."](https://x.com/ornith_/status/2070148887067963854) [출처: Open-Source Coding Model Ornith-1.0 Writes Its Own Training Scaffold in Reinforcement Learning](https://www.techtimes.com/articles/319122/20260626/open-source-coding-model-ornith-10-writes-its-own-training-scaffold-reinforcement-learning.htm)

## 미래의 풍경

Ornith-1.0의 등장은 오픈소스 AI 생태계에 큰 파장을 예고합니다. 거대 IT 기업의 독점적인 모델에만 의존하던 시대가 지나고, 누구나 강력한 코딩 도구를 직접 구축하고 개선할 수 있는 시대가 열린 것입니다. [출처: DeepReinforce ReleasesOrnith-1.0:AnOpen-SourceCodingModel...](https://www.marktechpost.com/2026/06/25/deepreinforce-releases-ornith-1-0-an-open-source-coding-model-family-that-learns-its-own-rl-scaffolds/)

앞으로는 AI가 단순히 코드를 짜주는 것을 넘어, 소프트웨어 개발 프로젝트 전체를 지휘하는 '자율형 엔지니어'로 발전할 것입니다. 개발자는 더 창의적이고 설계적인 고민에 집중하고, 반복적이고 지루한 검증 작업은 AI 에이전트가 대신하는 미래, 그 첫걸음이 Ornith-1.0과 함께 시작되었습니다. [출처: DeepReinforce Releases Ornith-1.0 for Self-Scaffolding Coding Agents, TechGig](https://techgig.com/news/software-devops/deepreinforce-releases-ornith-1-0-for-self-scaffolding-coding-agents/132008000)

## 참고자료

1. [Ornith1.0—Open-SourceAgenticCodingModels](https://www.ornith.site/)
2. [Ornith1.0: SelfLearningLLM forCoding| by Mehul Gupta | Medium](https://medium.com/data-science-in-your-pocket/ornith-1-0-self-learning-llm-for-coding-318c9a830bfc)
3. [IntroducingOrnith1.0-AgenticCodingLLMs - YouTube](https://www.youtube.com/watch?v=uD4-uy0GmHE)
4. [Ornith-1.0-adeepreinforce-ai Collection](https://huggingface.co/collections/deepreinforce-ai/ornith-10)
5. [IntroducingOrnith1.0-open-source- Art of Smart](https://www.artofsm.art/t/introducing-ornith-1-0/20592)
6. [DeepReinforce ReleasesOrnith-1.0:AnOpen-SourceCodingModel...](https://www.marktechpost.com/2026/06/25/deepreinforce-releases-ornith-1-0-an-open-source-coding-model-family-that-learns-its-own-rl-scaffolds/)
7. [DeepReinforce releasesopen-sourceOrnith-1.0codingmodels...](https://digg.com/tech/f2u02pzq)
8. [deepreinforce-ai/Ornith-1.0-9B-GGUF · Hugging Face](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B-GGUF)
9. [Ornith-1.0: Self-ScaffoldingLLMsforAgenticCoding](https://deep-reinforce.com/ornith_1_0.html)
10. [DeepReinforceOpenSourcesOrnith-1.0CodingModels - Open...](https://www.opensourceforu.com/2026/06/deepreinforce-open-sources-ornith-1-0-coding-models/)
11. [LLM Explorer: AI Agent andOpen-SourceLanguage Model Directory](https://llm-explorer.com/)
12. [Ornith on X: "Aloha! 🌺 Meet Ornith-1.0..."](https://x.com/ornith_/status/2070148887067963854)
13. [Saidul on X: "Open-source AI just raised the bar for coding agents..."](https://x.com/saidul_dev/status/2070154993240608844)
14. [🚨 AI News | TestingCatalog on X: "DeepReinforce has released Ornith-1.0..."](https://x.com/testingcatalog/status/2070153054679179400)
15. [Open-Source Coding Model Ornith-1.0 Writes Its Own Training Scaffold in Reinforcement Learning](https://www.techtimes.com/articles/319122/20260626/open-source-coding-model-ornith-10-writes-its-own-training-scaffold-reinforcement-learning.htm)
16. [DeepReinforce Releases Ornith-1.0 for Self-Scaffolding Coding Agents, TechGig](https://techgig.com/news/software-devops/deepreinforce-releases-ornith-1-0-for-self-scaffolding-coding-agents/132008000)
17. [0xMarioNawfal on X: "DeepReinforce just launched Ornith-1.0..."](https://x.com/RoundtableSpace/status/2070211260898275530)
18. [deepreinforce-ai/Ornith-1.0-9B · Hugging Face](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B)