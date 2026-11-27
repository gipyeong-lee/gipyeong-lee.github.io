---
layout: post
title: "AI가 스스로 실험하는 시대: 구글 딥마인드, 제미나이 연산 자원을 AI 에이전트에 맡기다"
description: "구글 딥마인드가 차세대 제미나이(Gemini) 모델 개발을 위해 AI 에이전트에 연산 자원 통제권을 일부 넘겼습니다. AI가 스스로 과학 실험을 수행하는 시대의 의미와 안전장치에 대해 알아봅니다."
summary: "구글 딥마인드가 차세대 제미나이 모델 실험을 위해 AI 에이전트에게 자체 연산 자원의 일부를 위임했습니다. 다만 완전한 자가 개선은 아직 멀었으며, 인간 감독을 위해 내부 생각 흐름은 보상하지 않는 안전장치를 유지하고 있습니다."
tags: [AI, GoogleDeepMind, Gemini, AI장치, 기술동향]
image: 2026-11-27-AI-agents-now-control-part-of-DeepMinds-compute-for-Gemini-experiments.jpg
image_alt: "실험실 컴퓨터 화면 앞에서 자율적으로 연산 데이터를 분석하고 있는 AI 시스템의 모습을 형상화한 일러스트"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI가 스스로 실험을 설계하고 실행하는 것은 도구에서 동료로의 거대한 전환입니다. 투명한 생각 흐름 검증이라는 안전장치가 유지되는 한, 과학적 발견의 속도는 상상을 초월하게 빨라질 것입니다."
quiz:
  - question: "구글 딥마인드가 AI 에이전트에게 맡긴 것은 무엇인가요?"
    choices: ["회사 인사 채용 권한", "차세대 제미나이 실험을 위한 연산 자원 일부", "구글 검색 엔진의 소스 코드 수정 권한"]
    answer: 1
    explanation: "구글 딥마인드는 차세대 제미나이 모델 개발을 위한 실험을 위해 AI 에이전트에게 자체 연산 자원(compute budget)의 일부를 자율적으로 제어하도록 허용했습니다."
  - question: "딥마인드가 AI의 훈련 과정에서 의도적으로 보상하지 않는 것은 무엇인가요?"
    choices: ["코드 작성 속도", "내부 생각 흐름(Chain of Thought)", "서버 전력 사용량"]
    answer: 1
    explanation: "딥마인드는 AI의 내부 생각 흐름(Chain of Thought)을 훈련 중에 보상하지 않음으로써, AI의 의도가 자연어 상태로 필터링 없이 유지되어 인간이 실행 전에 검토할 수 있도록 안전장치를 마련했습니다."
  - question: "딥마인드 연구 책임자인 코라이 카부쿠오글루(Koray Kavukcuoglu)가 강조한 현재 AI의 상태는 무엇인가요?"
    choices: ["완전한 재귀적 자가 개선(Recursive Self-Improvement)은 아직 멀었다", "AI가 이미 인간 연구원을 완전히 대체했다", "인간의 개입이 전혀 필요 없는 자율 연구 시대가 열렸다"]
    answer: 0
    explanation: "연구 부사장 코라이 카부쿠오글루는 AI가 실험 연산을 제어하기 시작했지만, 스스로를 무한히 업그레이드하는 재귀적 자가 개선(RSI) 단계는 아직 먼 미래라고 강조했습니다."
lang: ko
ref: 2026-11-27-AI-agents-now-control-part-of-DeepMinds-compute-for-Gemini-experiments
audio: 2026-11-27-AI-agents-now-control-part-of-DeepMinds-compute-for-Gemini-experiments.mp3
permalink: /2026/11/27/AI-agents-now-control-part-of-DeepMinds-compute-for-Gemini-experiments/
---

상상해보세요. 여러분이 어떤 거대한 연구소의 총괄 책임자인데, 밤사이에 인공지능 조수에게 연구실의 슈퍼컴퓨터 사용 권한을 일부 떼어주었습니다. 아침에 출근해보니 그 인공지능이 인간 연구원도 생각하지 못했던 참신한 가설을 세우고, 밤새 수천 번의 가상 실험을 돌려 유의미한 결과물까지 깔끔하게 정리해 놓았습니다. 소설 속 이야기처럼 들리나요? 하지만 지금 구글 딥마인드(Google DeepMind) 연구실에서는 실제로 이와 비슷한 일이 벌어지고 있습니다.

## AI가 스스로 연구실의 열쇠를 쥐다

최근 구글 딥마인드는 차세대 제미나이(Gemini, 텍스트, 이미지, 오디오 등 다양한 형태의 데이터를 동시에 이해하는 구글의 핵심 대형 언어 모델 시리즈 [출처: 위키백과](https://en.wikipedia.org/wiki/Gemini_(language_model))) 모델들의 실험을 위해, **AI 에이전트(AI Agent, 스스로 판단하고 목표를 수행하는 자율형 인공지능 프로그램)**에게 연구실의 핵심 자원인 연산 예산(compute budget)의 일부를 자율적으로 제어하도록 허용했습니다 ([AI agents now control part of DeepMind's compute for Gemini experiments](https://the-decoder.com/ai-agents-now-control-part-of-deepminds-compute-for-gemini-experiments-but-recursive-self-improvement-remains-distant/)). 

이 소식은 구글 딥마인드의 연구 부사장(VP of Research)이자 제미나이 개발을 총괄하는 코라이 카부쿠오글루(Koray Kavukcuoglu)가 공식 팟캐스트인 '구글 딥마인드: 팟캐스트(Google DeepMind: The Podcast)' 제35화에서 직접 밝히면서 세상에 알려졌습니다 ([DeepMind Agents Control Part of Gemini Training Compute](https://explainx.ai/blog/google-deepmind-gemini-agents-training-compute-koray-kavukcuoglu-november-2026)). 단순히 질문에 답하는 수준을 넘어, AI가 직접 실험을 기획하고 연산을 배분하는 주체로 올라섰다는 점에서 기술계의 이목이 집중되고 있습니다.

---

## 이게 왜 중요한가요?

우리 같은 일반 사람들의 일상에 이 뉴스가 어떤 의미를 가질까요? 핵심은 **'연구와 기술 발전의 속도가 인간의 시간표를 벗어나기 시작했다'**는 점입니다. 

과거에는 새로운 AI 모델을 만들거나 신소재를 발굴할 때, 인간 과학자들이 직접 가설을 세우고 컴퓨터에 명령어를 입력한 뒤 결과를 기다려야 했습니다. 이 과정은 수많은 시간과 비용이 소모되는 지루한 반복 작업의 연속이었습니다. 하지만 AI 에이전트가 직접 연산 자원을 통제하며 실험을 주도하게 되면, 인류가 새로운 지식을 발견하고 기술을 혁신하는 속도가 상상을 초월할 정도로 빨라질 수 있습니다.

실제로 구글 딥마인드는 이러한 자율 에이전트 시스템(예컨대 코-사이언티스트·Co-Scientist 시스템)을 통해 이미 엄청난 성과를 거두고 있습니다. 신소재 합성부터 의료용 AI 아키텍처의 자율적 개발에 이르기까지, 다양한 과학 분야에서 실험적으로 검증된 결과물을 성공적으로 도출해 낸 바 있습니다 ([Google Deepmind's AI Co-Scientist now plans experiments, runs ...](https://the-decoder.com/google-deepminds-ai-co-scientist-now-plans-experiments-runs-lab-equipment-and-writes-scientific-papers/)). 심지어 AI 에이전트가 인간 연구원들의 감독 아래 구형 RSA 암호화 방식의 취약점을 기존 방식보다 최대 1,600배 빠른 속도로 찾아내는 기술을 발견하기도 했습니다 ([Google DeepMind finds 1,600x faster way to expose encryption flaws](https://interestingengineering.com/ai-robotics/google-deepmind-agents-expose-older-encryption-flaws)). 

즉, 이번 조치는 이러한 실험적 성공이 단발성 이벤트에 그치지 않고, 구글의 핵심 AI 모델인 제미나이 개발 프로세스 전체의 표준 운영 방식으로 깊숙이 편입되었음을 뜻합니다.

---

## 쉽게 이해하기: '수퍼 인턴'에게 법인카드를 준 것과 같습니다

이 복잡한 상황을 쉽게 이해하기 위해 일상적인 비유를 들어보겠습니다. 

아주 유능하지만 아직 정식 직원이 아닌 '슈퍼 인턴'을 한 명 채용했다고 상상해보세요. 지금까지 이 인턴은 선배가 시키는 단순 문서 작업이나 자료 조사를 수행했습니다. 하지만 대표가 결단을 내려 이 인턴에게 **"회사 법인카드의 일부를 줄 테니, 네가 직접 필요하다고 생각하는 시장 조사 프로젝트를 밤사이에 마음껏 돌려보라"**고 권한을 넘겨준 것입니다. 

인턴(AI 에이전트)은 주어진 예산(연산 자원) 안에서 어떤 주제를 파악할지 스스로 결정하고, 밤새 컴퓨터를 돌려 데이터를 분석한 뒤 아침에 보고서를 올립니다. 이것이 바로 이번에 딥마인드가 제미나이 실험에서 시도하고 있는 일입니다.

하지만 여기서 중요한 의문이 생깁니다. "인턴이 자율적으로 권한을 쓰기 시작하면, 통제를 벗어나 자기 마음대로 폭주하지 않을까요?"

딥마인드 연구진은 이 점을 정확히 꿰뚫고 매우 독특한 안전장치를 마련했습니다. 인공지능이 내부적으로 생각하는 과정, 즉 **'생각의 사슬(Chain of Thought, AI가 답을 도출하기 전에 머릿속으로 단계별 추론을 거치는 내부 생각 흐름)'**을 훈련 과정에서 의도적으로 보상(reward)하지 않기로 한 것입니다 ([AI agents now control part of Deepmind's compute for Gemini experiments ...](https://www.topai-tools.org/news/ai-agents-now-control-part-of-deepmind-s-compute-for-gemini-experiments-but)). 

이게 무슨 뜻일까요? 쉽게 말해서, AI가 왜 그런 실험을 하려고 하는지 그 **내부 의도와 동기를 자연어(인간이 읽을 수 있는 언어) 그대로 필터링 없이 투명하게 남겨두어**, 행동으로 옮기기 전에 인간 관리자들이 철저하게 검토할 수 있도록 판을 짜놓은 것입니다 ([AI agents now control part of Deepmind's compute for Gemini experiments ...](https://www.topai-tools.org/news/ai-agents-now-control-part-of-deepmind-s-compute-for-gemini-experiments-but)). 머릿속을 캄캄하게 가려두는 것이 아니라, 인턴이 무슨 생각을 하는지 투명하게 들여다볼 수 있는 유리창을 만들어 낸 셈입니다.

---

## 현재 상황: 어디까지 왔고, 어디가 한계일까?

미디어에서는 종종 "AI가 스스로를 고치며 터미네이터처럼 진화하고 있다"고 자극적으로 보도하곤 합니다. 하지만 현장의 목소리는 훨씬 냉철하고 현실적입니다.

구글 딥마인드의 코라이 카부쿠오글루 부사장은 팟캐스트 인터뷰에서 이번 조치가 연구실 내부의 거대한 전략적 전환(strategic shift)의 일환이라고 인정하면서도, SF 영화에서 흔히 묘사되는 **'재귀적 자가 개선(Recursive Self-Improvement, AI가 스스로 코드를 수정해 가며 무한히 똑똑해지는 루프)'**은 아직 갈 길이 멀다고 선을 그었습니다 ([AI agents now control part of Deepmind's compute for Gemini experiments, but recursive self-improvement remains distant](https://the-decoder.com/ai-agents-now-control-part-of-deepminds-compute-for-gemini-experiments-but-recursive-self-improvement-remains-distant/)).

즉, 현재의 AI 에이전트는 어디까지나 인간이 설계해 준 틀과 안전장치 안에서 지정된 연산 예산을 활용해 실험을 '대행'하는 수준입니다. 자율적으로 목표를 설정하고 자신의 아키텍처를 완전히 개조하는 단계는 아니라는 뜻입니다. AI는 매우 강력한 '실험 도우미'이자 '오케스트레이터'로 진화했지만, 최종 지휘봉은 여전히 인간 연구원의 손에 쥐여져 있습니다.

---

## 앞으로 어떻게 될까?

이번 발표를 통해 우리는 AI 발전의 다음 국면이 어떤 모습일지 엿볼 수 있습니다. 

단순히 글을 잘 쓰고 그림을 예쁘게 그려주는 생성형 AI의 시대를 지나, 이제는 **과학적 발견과 기술 개발 그 자체를 수행하는 '에이전틱 AI(Agentic AI)'의 시대**로 빠르게 진입하고 있습니다. 구글 딥마인드의 궁극적인 목표는 과학 전반을 아우르는 통일된 범용 알고리즘을 구축하는 것입니다 ([DeepMind's Gemini Experiments Now Orchestrated by AI Agents](https://best-ai.org/ai-news/deepminds-gemini-experiments-now-orchestrated-by-ai-agents-5o695i)).

앞으로 우리가 지켜봐야 할 부분은 AI 에이전트가 통제된 연산 자원 속에서 얼마나 더 정교한 가설을 만들어내느냐와, 그 과정에서 인간과의 협업 거버넌스(Governance, 관리 체계)가 얼마나 안전하게 유지되느냐입니다. 기술이 고도화될수록 인공지능의 '내부 생각 흐름'을 투명하게 모니터링하려는 딥마인드의 철학은 전 세계 AI 업계의 중요한 표준 안전 지침이 될 것으로 보입니다.

---

## 참고자료

1. The Decoder, *AI agents now control part of Deepmind's compute for Gemini experiments, but recursive self-improvement remains distant*, https://the-decoder.com/ai-agents-now-control-part-of-deepminds-compute-for-gemini-experiments-but-recursive-self-improvement-remains-distant/
2. AI Weekly, *DeepMind Agents Now Run Part of Gemini Experiment Compute*, https://aiweekly.co/alerts/deepmind-agents-now-run-part-of-gemini-experiment-compute
3. TopAI Tools, *AI agents now control part of Deepmind's compute for Gemini experiments, but*, https://www.topai-tools.org/news/ai-agents-now-control-part-of-deepmind-s-compute-for-gemini-experiments-but
4. ExplainX AI, *DeepMind Agents Control Part of Gemini Training Compute — Koray Kavukcuoglu*, https://explainx.ai/blog/google-deepmind-gemini-agents-training-compute-koray-kavukcuoglu-november-2026
5. Emergent SH, *DeepMind AI Agents Now Control Gemini Experiment Compute*, https://emergent.sh/news/deepmind-ai-agents-now-control-gemini
6. Best AI, *DeepMind's Gemini Experiments Now Orchestrated by AI Agents*, https://best-ai.org/ai-news/deepminds-gemini-experiments-now-orchestrated-by-ai-agents-5o695i
7. AI Future, *AI agents now control part of Deepmind's compute for Gemini experiments, but recursive self-improvement*, https://aifuture.org/news/ai-agents-now-control-part-of-deepmind-s-compute-for-gemini-experiments-but-recu-21077
8. The Decoder, *Google Deepmind's AI Co-Scientist now plans experiments, runs lab equipment and writes scientific papers*, https://the-decoder.com/google-deepminds-ai-co-scientist-now-plans-experiments-runs-lab-equipment-and-writes-scientific-papers/
9. Wikipedia, *Gemini (language model)*, https://en.wikipedia.org/wiki/Gemini_(language_model)
10. Interesting Engineering, *Google DeepMind finds 1,600x faster way to expose encryption flaws*, https://interestingengineering.com/ai-robotics/google-deepmind-agents-expose-older-encryption-flaws