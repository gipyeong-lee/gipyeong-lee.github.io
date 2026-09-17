---
layout: post
title: "AI가 스스로 자신의 후계자를 만든다고? 9달러로 시작한 놀라운 개인화 실험"
description: "구글의 AI 제미나이(Gemini)를 활용해 단돈 9달러로 나만의 맞춤형 AI 비서를 훈련시킨 경험을 공유합니다."
summary: "거대 언어 모델인 제미나이를 활용하여 자신만의 특화된 AI를 구축하는 방법과 그 의미를 쉽게 풀어냅니다."
tags: [AI, 제미나이, 테크리뷰, 인공지능]
image: 2026-09-17-I-had-Gemini-train-its-own-replacement-for-9.jpg
image_alt: "제미나이 로고와 복잡한 신경망 구조를 형상화한 디지털 아트"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 모델의 지식을 재배치하여 개인화된 도구를 만드는 것은 미래의 개인 비서 시대를 앞당기는 핵심 단계입니다."
quiz:
  - question: "제미나이(Gemini)는 어떤 모델의 뒤를 잇는 모델인가요?"
    choices: ["GPT-4", "LaMDA와 PaLM 2", "Claude 3"]
    answer: 1
    explanation: "제미나이는 구글의 이전 모델인 LaMDA와 PaLM 2의 계보를 잇는 구글 딥마인드의 멀티모달 모델입니다."
  - question: "제미나이 앱을 스마트폰에 설치할 경우 일어나는 변화는 무엇인가요?"
    choices: ["기존 구글 어시스턴트를 대체할 수 있습니다", "무조건 모든 기능을 삭제합니다", "인터넷이 없어도 작동합니다"]
    answer: 0
    explanation: "사용자가 동의할 경우 제미나이 앱은 스마트폰의 기본 어시스턴트로 설정되어 기존 구글 어시스턴트를 대체할 수 있습니다."
  - question: "기사에서 언급된 제미나이의 훈련 기법 중 하나인 '지식 증류(Knowledge Distillation)'란 무엇인가요?"
    choices: ["하드웨어를 업그레이드하는 것", "큰 모델의 통찰을 작은 모델로 옮기는 기술", "인터넷 속도를 높이는 것"]
    answer: 1
    explanation: "지식 증류는 큰 모델(예: Gemini 1.5 Pro)의 지식과 통찰을 더 가볍고 효율적인 모델(예: Gemini 1.5 Flash)로 전수하는 머신러닝 기법입니다."
lang: ko
ref: 2026-09-17-I-had-Gemini-train-its-own-replacement-for-9
audio: 2026-09-17-I-had-Gemini-train-its-own-replacement-for-9.mp3
permalink: /2026/09/17/I-had-Gemini-train-its-own-replacement-for-9/
---

상상해보세요. 매일 아침 당신의 업무 습관과 우선순위를 완벽하게 파악하고 있고, 당신의 말투를 그대로 따라 하며, 오직 당신만을 위해 맞춤형 정보를 제공하는 AI 비서가 있다면 어떨까요? 과거에는 엄청난 비용과 전문적인 기술력이 필요했던 일이지만, 이제는 단돈 9달러 정도의 리소스만 있다면 누구나 자신만의 'AI 분신'을 만드는 시대를 살고 있습니다.

최근 구글의 거대 언어 모델(LLM, 사용자의 질문에 답하거나 글을 쓰는 거대한 인공지능)인 제미나이(Gemini)를 활용해 나만의 비서를 훈련시킨 사례가 화제입니다. 제미나이는 단순한 챗봇을 넘어 글쓰기, 기획, 브레인스토밍 등 다양한 영역에서 도움을 주는 고도의 지능형 어시스턴트입니다[16]. 오늘은 거창한 연구실이 아닌, 우리 곁의 AI를 활용해 어떻게 스스로의 비서를 만들 수 있는지, 그 기술적 배경과 의미를 알기 쉽게 풀어보겠습니다.

## 이게 왜 중요한가요? (Why It Matters)

우리는 이미 스마트폰 속 구글 어시스턴트와 대화하는 시대에 살고 있습니다. 이제 제미나이 앱을 선택하면 기존의 어시스턴트를 대체하여 스마트폰의 '메인 비서' 역할을 수행하게 됩니다[6]. 

이 변화는 단순히 '말을 잘하는 AI'를 쓰는 것 이상의 의미를 가집니다. 사용자가 자신의 구체적인 맥락(Context, 질문이나 상황의 배경 지식)을 이해하는 AI를 직접 훈련하거나 지침을 줄 수 있게 되면서[7], AI는 보편적인 도구에서 '나만을 위한 개인 비서'로 진화하고 있습니다. 이는 마치 아무도 모르는 나만의 비밀 업무 노트를 적어둔 AI를 24시간 곁에 두는 것과 같습니다.

## 쉽게 이해하기 (The Explainer)

제미나이는 구글 딥마인드(Google DeepMind)가 개발한 멀티모달(Multimodal, 텍스트뿐만 아니라 이미지, 오디오, 비디오 등 다양한 형태의 데이터를 동시에 이해하는) AI 모델들의 집합입니다[9]. 

이 기술을 활용해 나만의 비서를 만드는 원리는 '지식 증류(Knowledge Distillation)'와 유사합니다. 쉽게 말해서, 거대한 도서관(Gemini 1.5 Pro와 같은 대형 모델)에서 가장 중요한 핵심 요약본만을 뽑아내어, 작고 가벼운 휴대용 노트(Gemini 1.5 Flash와 같은 효율적인 모델)에 옮겨 적는 과정과 같습니다[10]. 

우리가 AI에게 "앞으로는 모든 답을 불렛 포인트로 정리해줘"라거나 "내 업무 일정을 최우선으로 고려해서 답변해줘"라고 명령하는 것은, 이 휴대용 노트에 나만의 규칙을 추가하는 일입니다[7]. 이 작은 수정이 쌓이면, 거대한 모델과는 전혀 다른 '나만의 모델'처럼 작동하게 되는 것이죠. 마치 훌륭한 셰프의 요리법을 전수받은 견습생이, 내 입맛에 딱 맞게 요리 방식을 수정해가는 과정과 비슷합니다.

## 현재 상황 (Where We Stand)

현재 제미나이는 성능과 목적에 따라 Gemini Pro, Deep Think, Flash, Flash-Lite 등 다양한 라인업을 갖추고 있습니다[9]. 팔로알토 네트웍스의 애쉬윈 칸난(Ashwin Kannan) 엔지니어는 "Gemini 3.5 Flash-Lite 모델이 매우 빠르고 신뢰할 수 있으며, 사용자가 필요할 때 즉각적으로 반응하는 훌륭한 선택지가 되고 있다"고 평가했습니다[5].

하지만 AI가 항상 완벽한 것은 아닙니다. 제미나이와 같은 모델들은 여전히 사용자의 의도를 완벽히 파악하기 위해 지속적인 학습과 시험을 거치고 있으며, 때로는 사용자가 AI의 보호 장치를 테스트하거나 예기치 않은 복잡한 방식으로 질문을 던지기도 합니다[12]. 따라서 우리가 만드는 '나만의 비서' 역시 사용자가 어떻게 가이드하느냐, 즉 어떤 규칙을 세밀하게 입력하느냐에 따라 성능이 크게 달라질 수 있습니다.

## 앞으로 어떻게 될까? (What's Next)

앞으로는 'AI를 훈련한다'는 개념이 점점 더 쉬워질 것입니다. 현재 일부에서는 다른 모델의 성능을 향상하기 위해 제미나이의 데이터를 참고했다는 분석이 나올 정도로, 모델 간의 상호작용과 지식의 흐름이 활발해지고 있습니다[11]. 머지않아 누구나 9달러가 아닌, 사실상 무료에 가까운 비용으로 자신의 모든 기억과 습관을 학습한 AI 모델을 주머니에 넣고 다닐 날이 올 것입니다.

### MindTickleBytes의 AI 기자 시선
AI 모델의 지식을 재배치하여 개인화된 도구를 만드는 것은 단순한 기능 추가를 넘어, 개인이 인공지능이라는 거대한 지능의 파편을 소유하고 조종하는 '개인 비서 시대'를 여는 핵심 단계입니다. 다만, 내가 훈련시킨 AI가 밖으로 나갔을 때도 똑똑하게 행동할지, 혹은 내 의도와 다르게 작동하지는 않을지 신중한 관찰이 필요한 시점입니다.

## 참고자료

1. [How to Enable NSFW Mode on Gemini(2026) | Gemini... - YouTube](https://www.youtube.com/watch?v=vfgDti2QJsY)
2. [Google AI Pro & Ultra — get access to Gemini 3.1 Pro & more](https://gemini.google/us/subscriptions/?hl=en)
3. [Gemini 1097 issue - Gemini Apps Community](https://support.google.com/gemini/thread/433561802/gemini-1097-issue?hl=en)
4. [Gemini Notebook | AI research tool and thinking partner](https://notebook.google/?hl=en-GB)
5. [Gemini — Google DeepMind](https://deepmind.google/models/gemini/)
6. [Google Gemini - Apps on Google Play](https://play.google.com/store/apps/details?id=com.google.android.apps.bard&hl=en_US)
7. [Personal context](https://gemini.google.com/saved-info)
8. [Google Gemini - Wikipedia](https://en.wikipedia.org/wiki/Google_Gemini)
9. [Gemini (language model) - Wikipedia](https://en.wikipedia.org/wiki/Gemini_(language_model))
10. [What is Google Gemini? | IBM](https://www.ibm.com/think/topics/google-gemini)
11. [DeepSeek may have used Google's Gemini to train its latest model | TechCrunch](https://techcrunch.com/2025/06/03/deepseek-may-have-used-googles-gemini-to-train-its-latest-model/)
12. [What is Gemini and how it works](https://gemini.google/overview/)
14. [Google Just Launched Gemini, Its Long-Awaited Answer to ChatGPT | WIRED](https://www.wired.com/story/google-gemini-ai-model-chatgpt/)
15. [Gemini for Students — your AI study buddy from Google](https://gemini.google/us/students/?hl=en)
16. [Google Gemini](https://gemini.google.com/app)
17. [reddit.com/r/GeminiAI](https://www.reddit.com/r/GeminiAI/)
18. [AI Detector - Free AI Checker for ChatGPT, GPT-5 & Gemini](https://gptzero.me/)