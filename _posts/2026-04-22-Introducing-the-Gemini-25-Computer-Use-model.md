---
layout: post
title: "내 대신 클릭하고 타이핑하는 AI? 구글 '제미나이 2.5 컴퓨터 유즈'의 등장"
description: "사람처럼 화면을 보고 마우스를 움직여 작업을 수행하는 구글의 새로운 AI 모델, 제미나이 2.5 컴퓨터 유즈를 소개합니다."
summary: "구글이 화면을 이해하고 스스로 13가지 동작을 수행하며 웹 브라우저를 조작하는 '에이전트급' AI 모델을 공개했습니다."
tags: [제미나이, AI에이전트, 구글, 인공지능, 컴퓨터유즈]
image: 2026-04-22-Introducing-the-Gemini-25-Computer-Use-model.jpg
image_alt: "컴퓨터 화면 위에서 AI가 마우스 커서를 조작하며 다양한 웹페이지를 넘나드는 모습을 형상화한 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "단순히 말을 잘하는 AI를 넘어, 이제는 우리의 '손'이 되어주는 AI 에이전트 시대가 본격적으로 열렸습니다."
quiz:
  - question: "제미나이 2.5 컴퓨터 유즈 모델이 작업을 수행할 때 가장 먼저 받는 데이터는 무엇인가요?"
    choices: ["사용자의 음성", "화면 스크린샷이나 컨텍스트 정보", "엑셀 파일 데이터"]
    answer: 1
    explanation: "이 모델은 '에이전트 루프'를 통해 화면 스크린샷을 찍어 현재 상황을 파악한 뒤 다음 동작을 결정합니다."
  - question: "이 모델이 학습을 통해 수행할 수 있는 동작은 총 몇 가지인가요?"
    choices: ["5가지", "13가지", "100가지"]
    answer: 1
    explanation: "제미나이 2.5 컴퓨터 유즈는 브라우저를 탐색하고 조작하기 위해 13가지의 서로 다른 동작을 수행하도록 훈련되었습니다."
  - question: "이 모델이 우수한 성능을 보인 벤치마크(성능 지표) 중 안드로이드 환경을 테스트하는 것은 무엇인가요?"
    choices: ["Online-Mind2Web", "WebVoyager", "AndroidWorld"]
    answer: 2
    explanation: "제미나이 2.5 컴퓨터 유즈는 AndroidWorld를 포함한 여러 인터페이스 제어 벤치마크에서 강력한 성능을 보여주었습니다."
lang: ko
ref: 2026-04-22-Introducing-the-Gemini-25-Computer-Use-model
audio: 2026-04-22-Introducing-the-Gemini-25-Computer-Use-model.mp3
permalink: /2026/04/22/Introducing-the-Gemini-25-Computer-Use-model/
---

월요일 아침, 출근하자마자 마주하는 산더미 같은 이메일과 영수증들을 상상해보세요. 하나하나 열어보고, 날짜와 금액을 확인한 뒤, 회사 정산 시스템에 일일이 타이핑해 넣어야 하는 지루한 과정입니다. 로그인하고, 파일을 업로드하고, 빈칸을 채우는 이 단순 반복적인 업무는 우리 소중한 시간의 상당 부분을 앗아갑니다. 그런데 이때 AI에게 "이 영수증들 다 정리해서 제출해줘"라고 한마디만 하면 어떨까요? AI가 마치 사람처럼 내 눈 대신 화면을 들여다보고, 내 손 대신 마우스를 움직여 모든 작업을 완벽하게 끝마치는 세상. 이제 공상과학 영화 속 이야기가 아닙니다. 구글이 최근 공개한 **'제미나이 2.5 컴퓨터 유즈(Gemini 2.5 Computer Use)'** 모델이 우리 앞에 그려내고 있는 가까운 미래의 모습입니다. [Introducing the Gemini 2.5 Computer Use model](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-computer-use-model/)

## 이게 왜 중요한가요?

지금까지 우리가 열광했던 챗GPT나 기존의 제미나이는 주로 '말'을 잘하는 AI였습니다. 궁금한 것을 물어보면 척척 대답해주고, 복잡한 논문을 요약해주며 우리를 놀라게 했죠. 하지만 곰곰이 생각해보면, 우리가 컴퓨터로 하는 업무의 80~90%는 대화가 아니라 구체적인 '행동'입니다. 특정 버튼을 클릭하고, 화면을 아래로 내리고(스크롤), 검색창에 글자를 입력하는 일련의 조작들입니다.

제미나이 2.5 컴퓨터 유즈의 등장은 AI가 단순히 지식을 전달하는 '말하는 비서'에서 벗어나, 사용자의 업무를 실제로 수행하는 **'에이전트(Agent, 대리인)'**로 진화했음을 상징합니다. [Introducing Gemini 2.5 Computer Use model: A Paradigm Shift in AI's Digital Dexterity](https://markets.financialcontent.com/wedbush/article/tokenring-2025-10-7-gemini-25-computer-use-model-a-paradigm-shift-in-ais-digital-dexterity) 이 모델은 웹 브라우저나 스마트폰 앱의 화면 구성을 사람처럼 직관적으로 이해하고, 마우스와 키보드를 직접 제어할 수 있습니다. [Introducing Gemini 2.5 Computer Use: AI for web and... | LinkedIn](https://www.linkedin.com/posts/googleaidevs_introducing-gemini-25-computer-use-available-activity-7381415403840864256-ycSe) 쉽게 말해서, AI에게 컴퓨터를 다룰 줄 아는 '손'이 생긴 셈이죠. 이는 기업의 반복적인 사무 자동화는 물론, 소프트웨어가 정상적으로 작동하는지 검사하는 방식 자체를 근본적으로 바꿀 수 있는 엄청난 잠재력을 가지고 있습니다. [Gemini 2.5 Computer Use model | Gemini API | Google AI for Developers](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-computer-use-preview-10-2025)

## 쉽게 이해하기: AI에게 '눈'과 '손'이 생겼어요

제미나이 2.5 컴퓨터 유즈가 일하는 방식은 **'에이전트 루프(Agent Loop)'**라는 개념으로 설명할 수 있습니다. 비유하면, 우리가 초행길에서 운전할 때 '도로 상황을 살피고(눈) -> 내비게이션 경로와 비교해 판단한 뒤(머리) -> 핸들을 꺾거나 브레이크를 밟는(손)' 과정을 반복하는 것과 똑같습니다. [Introducing the Gemini 2.5 Computer Use model](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-computer-use-model/)

1. **상황 파악(눈):** AI는 먼저 현재 컴퓨터 화면을 스크린샷으로 찍어 실시간으로 분석합니다. 어디에 버튼이 있고 어디에 입력창이 있는지 '보는' 단계입니다. [Introducing the Gemini 2.5 Computer Use model](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-computer-use-model/)
2. **추론(머리):** 사용자가 "비행기 표 예약해줘"라고 요청했다면, AI는 현재 화면과 요청 사항을 대조합니다. 그리고 "지금은 '로그인' 버튼을 먼저 눌러야겠군"이라고 판단을 내립니다. [Google's Gemini 2.5 Computer Use model can navigate the web like a ...](https://siliconangle.com/2025/10/07/googles-gemini-2-5-computer-use-model-can-navigate-web-like-human/)
3. **실행(손):** 판단이 서면 실제로 마우스 커서를 해당 위치로 이동시켜 클릭하거나, 키보드로 아이디와 비밀번호를 타이핑합니다. [Introducing the Gemini 2.5 Computer Use model](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-computer-use-model/)

이 마법 같은 능력은 구글의 가장 강력한 AI 모델 중 하나인 '제미나이 2.5 프로(Gemini 2.5 Pro)'의 뛰어난 시각 분석 능력과 추론 능력을 토대로 만들어졌습니다. [Introducing Gemini 2.5 Computer Use: AI for web and... | LinkedIn](https://www.linkedin.com/posts/googleaidevs_introducing-gemini-25-computer-use-available-activity-7381415403840864256-ycSe) 특히 마우스 커서를 픽셀 단위로 정밀하게 제어하고, 웹 브라우저 상에서 일어나는 **13가지의 핵심적인 동작**을 집중적으로 학습하여 숙련도를 높였습니다. [Google News - Google releases Gemini 2.5, a new AI model with web...](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lDM3NUYkR4RU1DYjNPMmlnelhpZ0FQAQ?hl=en-US&gl=US&ceid=US:en)

다시 비유하자면, 기존의 AI가 "컴퓨터 사용법"이라는 두꺼운 백과사전을 통째로 외운 이론가였다면, 제미나이 2.5 컴퓨터 유즈는 실제로 마우스를 잡고 실습에 뛰어든 신입사원과 같습니다. 아직은 '프리뷰(미리보기)' 단계라 속도가 조금 느리거나 실수가 있을 수 있지만, 스스로 화면을 보고 길을 찾아간다는 점 자체가 거대한 도약입니다. [Google releases a preview of its Gemini 2.5 Computer Use AI model ...](https://gigazine.net/gsc_news/en/20251008-google-gemini-2-5-computer-use/)

## 현재 상황: 어디까지 왔나?

구글은 2025년 10월 초, 경쟁사인 오픈AI(OpenAI)가 유사한 기술을 언급한 바로 다음 날 이 모델을 전격 공개하며 AI 에이전트 시장의 주도권을 잡기 위한 강력한 승부수를 던졌습니다. [Google launches Gemini 2.5 Computer Use to rival OpenAI agents](https://www.techbuzz.ai/articles/google-launches-gemini-2-5-computer-use-to-rival-openai-agents) 현재 이 모델은 개발자들이 직접 테스트하고 자신의 서비스에 접목해볼 수 있는 '공개 프리뷰' 상태로 제공되고 있습니다. [Introducing Gemini 2.5 Computer Use model: A Paradigm Shift in AI's Digital Dexterity](https://markets.financialcontent.com/wedbush/article/tokenring-2025-10-7-gemini-25-computer-use-model-a-paradigm-shift-in-ais-digital-dexterity)

구글은 단순히 가능성만 보여준 것이 아니라, 객관적인 성능 지표(벤치마크)를 통해 그 실력을 증명했습니다.
- **Online-Mind2Web & WebVoyager:** 복잡한 웹사이트 내에서 AI가 길을 잃지 않고 목표를 달성하는지 측정하는 시험에서 우수한 성적을 거두었습니다. [Google DeepMind Launches Gemini 2.5 Computer Use Model to Power UI-Controlling AI Agents - InfoQ](https://www.infoq.com/news/2025/10/gemini-computer-use/)
- **AndroidWorld:** 윈도우나 맥 같은 PC 환경뿐만 아니라, 안드로이드 폰 환경을 얼마나 능숙하게 조작하는지 측정하는 시험에서도 강력한 성능을 보여주었습니다. [Google DeepMind Launches Gemini 2.5 Computer Use Model to Power UI-Controlling AI Agents - InfoQ](https://www.infoq.com/news/2025/10/gemini-computer-use/)

이러한 테스트 결과들은 제미나이 2.5 컴퓨터 유즈가 사람이 화면을 보며 느끼는 직관을 AI도 공유할 수 있으며, 이를 바탕으로 실제 문제를 해결해나갈 수 있음을 뒷받침합니다. [Gemini 2.5 Computer Use Model: How It Automates Browsers](https://skywork.ai/blog/gemini-2-5-computer-use-model/)

## 앞으로 어떻게 될까?

전문가들은 이번 모델의 등장이 AI가 우리 삶에 침투하는 방식에 있어 분수령이 될 것이라고 내다보고 있습니다. [2025 Complete Guide: Gemini 2.5 Computer Use Model - Revolutionary ...](https://dev.to/czmilo/2025-complete-guide-gemini-25-computer-use-model-revolutionary-breakthrough-in-ai-agent-133) 머지않아 우리는 다음과 같은 놀라운 변화들을 일상에서 마주하게 될지도 모릅니다.

1. **상상 그 이상의 개인 비서:** "이번 주말 친구들과 강남역 근처에서 만날 건데, 평점 4점 이상인 맛집 예약하고 단톡방에 위치랑 시간 공지해줘"라고 한마디만 하면 됩니다. AI가 식당 예약 앱을 실행해 예약을 마치고, 메신저를 열어 친구들에게 메시지까지 보내는 것이죠.
2. **소프트웨어 품질의 혁명:** 새로운 앱을 만든 개발자들은 이제 밤을 새워가며 버그를 찾을 필요가 없습니다. AI 에이전트가 수천 번, 수만 번 앱의 이곳저곳을 눌러보며 오류를 찾아내고 보고서를 작성할 테니까요. [Gemini 2.5 Computer Use model | Gemini API | Google AI for Developers](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-computer-use-preview-10-2025)
3. **모두를 위한 기술:** 스마트폰이나 컴퓨터 조작이 서툰 어르신들, 혹은 화면을 보기 어려운 시각 장애인분들에게도 큰 힘이 됩니다. 복잡한 클릭 과정 없이 오직 음성 명령만으로도 모든 디지털 서비스를 자유롭게 이용할 수 있게 되기 때문입니다.

물론 해결해야 할 숙제도 남아 있습니다. AI가 실수로 엉뚱한 물건을 결제해버리거나, 사용자의 민감한 개인정보를 잘못 다룰 때 어떻게 대응할 것인지에 대한 보안과 윤리적 가이드라인이 필요합니다. 하지만 구글이 내디딘 이 첫걸음은 AI가 단순한 도구를 넘어, 우리와 함께 디지털 세상을 살아가는 든든한 '동반자'가 되는 시대가 성큼 다가왔음을 확신하게 합니다. [Is Gemini 2.5 Computer Use Model the Future of AI-Driven Interface Control?](https://apidog.com/blog/gemini-2-5-computer-use-model/)

## AI의 시선
**MindTickleBytes의 AI 기자 시선:** "말만 번지르르하게 잘하던 AI가 이제 실제로 컴퓨터 마우스를 쥐었습니다. 이는 AI 기술이 '언어의 장벽'을 넘어 '행동의 영역'으로 진입했음을 의미하는 매우 상징적인 사건입니다. 머지않아 우리는 'AI에게 이 일을 시켜야지'라는 생각조차 하지 않을 정도로, 공기처럼 자연스럽게 AI 에이전트와 협업하게 될 것입니다. 편리함이 커지는 만큼, AI의 자율성을 어디까지 허용하고 신뢰할 것인지에 대한 사회적 합의도 진지하게 시작해야 할 때입니다."

## 참고자료
1. [Introducing the Gemini 2.5 Computer Use model](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-computer-use-model/)
2. [Google News - Google releases Gemini 2.5, a new AI model with web...](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lDM3NUYkR4RU1DYjNPMmlnelhpZ0FQAQ?hl=en-US&gl=US&ceid=US:en)
3. [Gemini 2.5 Computer Use AGENT: THE BEST AGENTIC... - YouTube](https://www.youtube.com/watch?v=Xllcw7YUjJA)
4. [Introducing Gemini 2.5 Computer Use: AI for web and... | LinkedIn](https://www.linkedin.com/posts/googleaidevs_introducing-gemini-25-computer-use-available-activity-7381415403840864256-ycSe)
5. [Gemini 2.5 Computer Use Model: How It Automates Browsers](https://skywork.ai/blog/gemini-2-5-computer-use-model/)
6. [Gemini Computer Use: Google's FREE Browser... - Analytics Vidhya](https://www.analyticsvidhya.com/blog/2025/10/gemini-2-5-computer-use/)
7. [Gemini 2.5 Computer Use model | Gemini API | Google AI for Developers](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-computer-use-preview-10-2025)
8. [Is Gemini 2.5 Computer Use Model the Future of AI-Driven Interface Control?](https://apidog.com/blog/gemini-2-5-computer-use-model/)
9. [Google DeepMind Launches Gemini 2.5 Computer Use Model to Power UI-Controlling AI Agents - InfoQ](https://www.infoq.com/news/2025/10/gemini-computer-use/)
10. [2025 Complete Guide: Gemini 2.5 Computer Use Model - Revolutionary ...](https://dev.to/czmilo/2025-complete-guide-gemini-25-computer-use-model-revolutionary-breakthrough-in-ai-agent-133)
11. [Google launches Gemini 2.5 Computer Use to rival OpenAI agents](https://www.techbuzz.ai/articles/google-launches-gemini-2-5-computer-use-to-rival-openai-agents)
12. [Google releases a preview of its Gemini 2.5 Computer Use AI model ...](https://gigazine.net/gsc_news/en/20251008-google-gemini-2-5-computer-use/)
13. [Introducing Gemini 2.5 Computer Use model: A Paradigm Shift in AI's Digital Dexterity](https://markets.financialcontent.com/wedbush/article/tokenring-2025-10-7-gemini-25-computer-use-model-a-paradigm-shift-in-ais-digital-dexterity)
14. [Google's Gemini 2.5 Computer Use model can navigate the web like a ...](https://siliconangle.com/2025/10/07/googles-gemini-2-5-computer-use-model-can-navigate-web-like-human/)

## FACT-CHECK SUMMARY
- Claims checked: 15
- Claims verified: 15
- Verdict: PASS