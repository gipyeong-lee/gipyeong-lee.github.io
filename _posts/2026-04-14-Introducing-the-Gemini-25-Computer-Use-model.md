---
layout: post
title: "AI가 내 컴퓨터를 대신 써준다면? 구글의 새로운 'Gemini 2.5 Computer Use' 모델 공개"
description: "사람처럼 화면을 보고 클릭하며 타이핑하는 구글의 새로운 인공지능, Gemini 2.5 Computer Use 모델의 특징과 미래를 알기 쉽게 설명합니다."
summary: "구글이 인간처럼 웹 브라우저와 모바일 앱을 직접 조작할 수 있는 'Gemini 2.5 Computer Use' 모델을 출시하며 진정한 AI 에이전트 시대를 열었습니다."
tags: [Gemini, 구글, AI에이전트, 컴퓨터유즈, 인공지능]
image: 2026-04-14-Introducing-the-Gemini-25-Computer-Use-model.jpg
image_alt: "컴퓨터 화면 위에서 AI가 마우스와 키보드를 조작하는 듯한 디지털 인터페이스의 미래 지향적인 모습"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "단순히 말을 하는 AI를 넘어 '행동하는 AI'로의 진화는 우리의 업무 방식을 근본적으로 바꿀 게임 체인저가 될 것입니다. 이제 AI는 도구의 사용법을 익히는 단계를 지나, 인간의 디지털 동반자로서 실질적인 과업을 완수하는 능력을 갖추게 되었습니다."
quiz:
  - question: "Gemini 2.5 Computer Use 모델은 어떤 모델을 기반으로 만들어졌나요?"
    choices: ["Gemini 1.5 Flash", "Gemini 2.5 Pro", "Gemini 1.0 Ultra"]
    answer: 1
    explanation: "이 모델은 Gemini 2.5 Pro의 시각적 이해력과 추론 능력을 기반으로 구축된 특화 모델입니다."
  - question: "이 AI 모델이 화면을 조작하기 위해 사용하는 방식은 무엇인가요?"
    choices: ["웹사이트의 복잡한 코드(API)를 직접 해킹한다.", "사람이 미리 입력해둔 명령어로만 작동한다.", "스크린샷을 분석하여 클릭이나 타이핑 같은 동작을 수행한다."]
    answer: 2
    explanation: "이 모델은 화면 캡처(스크린샷)를 분석한 뒤, 사람이 하는 것처럼 단계별 UI 동작을 반환하여 실행합니다."
  - question: "현재 이 모델이 자동화할 수 있는 UI 작업의 종류는 몇 가지인가요?"
    choices: ["5가지", "13가지", "100가지"]
    answer: 1
    explanation: "현재 이 시스템은 자동화가 가능한 13가지의 구체적인 UI 작업을 지원하고 있습니다."
lang: ko
ref: 2026-04-14-Introducing-the-Gemini-25-Computer-Use-model
audio: 2026-04-14-Introducing-the-Gemini-25-Computer-Use-model.mp3
permalink: /2026/04/14/Introducing-the-Gemini-25-Computer-Use-model/
---

상상해보세요. 여러분이 아주 복잡한 해외 호텔 예약 사이트에서 10개의 숙소를 일일이 비교하고, 각각의 까다로운 취소 규정을 확인한 뒤, 가장 저렴한 곳을 골라 예약 양식을 채워야 한다고 말이죠. 생각만 해도 눈이 피로해지는 작업입니다. 그런데 옆에서 "제가 대신 해드릴까요?"라고 묻는 똑똑한 비서가 있다면 어떨까요? 그 비서는 여러분이 하는 것처럼 화면을 뚫어지게 쳐다보고, 마우스를 움직여 버튼을 클릭하고, 키보드로 여러분의 정보를 정확히 입력합니다.

이것은 더 이상 먼 미래의 영화 속 이야기가 아닙니다. 구글이 지난 2025년 10월 7일, 마치 사람처럼 컴퓨터와 모바일을 직접 조작할 수 있는 새로운 인공지능, **'Gemini 2.5 Computer Use'** 모델을 전격 공개했기 때문입니다 [Introducing the Gemini 2.5 Computer Use model - The Keyword](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-computer-use-model/).

## 이게 왜 중요한가요?

지금까지 우리가 사용하던 AI(인공지능)는 주로 '말'이나 '글'로만 소통하는 존재였습니다. 질문을 던지면 답을 해주고, 긴 글을 요약해주는 식이었죠. 하지만 정작 우리가 컴퓨터로 일을 할 때는 단순한 대화보다 수많은 클릭과 스크롤, 그리고 타이핑이 훨씬 더 많이 필요합니다.

기존의 방식대로 AI가 특정 서비스를 이용하게 하려면, 소프트웨어 개발자들이 미리 만들어둔 전용 통로인 **API(Application Programming Interface, 프로그램 간의 대화 창구)**가 반드시 필요했습니다. 비유하자면, AI가 건물 안으로 들어가기 위해선 전용 '뒷문'이 설치되어 있어야만 했던 셈입니다. 하지만 세상의 모든 웹사이트와 앱이 AI를 위한 전용 뒷문을 열어두지는 않죠.

여기서 Gemini 2.5 Computer Use 모델의 진가가 드러납니다. 이 모델은 프로그램 뒷문의 통로(API)를 찾는 대신, 우리 눈에 보이는 **GUI(Graphical User Interface, 버튼이나 아이콘이 있는 그래픽 화면)**를 직접 이용합니다 [Introducing The Gemini 2.5 Computer Use Model](https://qrius.com/introducing-the-gemini-2-5-computer-use-model/). 즉, AI와 인간 사이의 오랜 장벽이었던 '디지털 소통 방식의 차이'를 기술적으로 극복한 것입니다 [Gemini 2.5 Computer Use Model: A Paradigm Shift in AI’s ...](https://markets.financialcontent.com/stocks/article/tokenring-2025-10-7-gemini-25-computer-use-model-a-paradigm-shift-in-ais-digital-dexterity). 이제 AI는 인간을 위해 만들어진 정문을 통해 당당히 컴퓨터 세상을 드나들 수 있게 되었습니다.

## 쉽게 이해하기: AI에게 '눈'과 '손'이 생겼어요

이 새로운 모델을 쉽게 이해하기 위해, AI를 **'디지털 운전기사'**라고 비유해 보겠습니다.

1.  **시각적 이해 (눈)**: 기존 AI가 내비게이션 데이터(텍스트 데이터)만 보고 길을 찾았다면, Gemini 2.5 Computer Use는 직접 앞유리(스크린샷)를 통해 도로 상황을 봅니다. 이 모델은 구글의 가장 강력한 모델 중 하나인 'Gemini 2.5 Pro'의 뛰어난 시각 인식 능력을 그대로 물려받았습니다 [Introducing The Gemini 2.5 Computer Use Model](https://aifuturethinkers.com/introducing-the-gemini-2-5-computer-use-model/). 화면을 실시간으로 캡처하여 어디에 버튼이 있고, 지금 어떤 팝업창이 떠 있는지 사람처럼 정확히 파악합니다 [Gemini 2.5 'Computer Use': Can This Model Automate Your... | Fello AI](https://felloai.com/gemini-2-5-computer-use/).
2.  **추론 및 실행 (손)**: 화면을 봤다면 이제 움직여야겠죠? AI는 "이 버튼을 클릭해", "여기에 이름을 타이핑해" 같은 구체적인 동작 명령을 스스로 내립니다 [Google Unveils Gemini 2.5 Computer Use That Clicks... | Beebom](https://beebom.com/google-unveils-gemini-2-5-computer-use-that-clicks-types-scrolls-like-humans/). **쉽게 말해서**, AI가 마우스를 잡고 키보드를 치는 손을 갖게 된 셈입니다. 현재 이 모델은 클릭, 타이핑, 스크롤, 화면 이동 등을 포함한 총 **13가지의 구체적인 동작**을 능숙하게 수행할 수 있습니다 [13 Essential Gemini 2.5 Computer Use Actions You Can Automate...](https://skywork.ai/blog/gemini-2-5-computer-use-actions-2025/).

결국 우리가 마우스와 키보드로 수행하는 거의 모든 복잡한 작업들을 AI가 눈으로 보면서 똑같이 따라 할 수 있는 시대가 온 것입니다 [Introducing the Gemini 2.5 Computer Use model | Eduardo López](https://www.linkedin.com/posts/eduardolopezgutierrez_introducing-the-gemini-25-computer-use-model-activity-7381801389682937856--r3N).

## 현재 상황: 어디까지 왔나?

구글은 이 모델이 웹 브라우저와 안드로이드 모바일 환경에서 다른 경쟁 모델들을 압도하는 성능을 보여준다고 자신하고 있습니다 [Introducing the Gemini 2.5 Computer Use model - The Keyword](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-computer-use-model/). 실제로 정확도와 속도 면에서 뛰어난 평가를 받고 있어, 복잡한 웹사이트를 탐색해야 하는 고객 서비스 봇이나 자동 소프트웨어 테스트 분야에서 즉각적인 변화를 일으킬 것으로 보입니다 [Google’s Gemini 2.5 Computer Use Model Takes Control of ...](https://neuronad.com/googles-gemini-2-5-computer-use-model-takes-control-of-digital-interfaces/).

현재 이 기술은 구글 내부에서 **'프로젝트 마리너(Project Mariner)'**라는 이름으로 개발 중인 차세대 에이전트 기능의 핵심 동력으로 사용되고 있습니다 [‘Gemini 2.5 Computer Use’ has strong web, Android performance](https://9to5google.com/2025/10/07/gemini-2-5-computer-use-model/). 또한, 전 세계 개발자들이 직접 자신의 앱이나 서비스에 이 마법 같은 기능을 넣을 수 있도록 API 형태로도 제공되기 시작했습니다 [Computer Use | Gemini API | Google AI for Developers](https://ai.google.dev/gemini-api/docs/computer-use).

흥미로운 점은 구글이 이 모델을 발표한 시점이 라이벌인 OpenAI가 새로운 ChatGPT 기능을 선보인 바로 다음 날이라는 점입니다 [Google launches Gemini 2.5 Computer Use to rival OpenAI ...](https://techbuzz.ai/articles/google-launches-gemini-2-5-computer-use-to-rival-openai-agents). AI 업계의 거물들이 이제 '말 잘하는 AI'를 넘어 '컴퓨터 잘 쓰는 AI'로의 진검승부를 시작했음을 알 수 있습니다.

## 앞으로 어떻게 될까?

전문가들은 이 모델이 **'진정한 디지털 자율성'**을 향한 커다란 도약이라고 평가합니다 [Gemini 2.5 Computer Use Model: A Paradigm Shift in AI’s ...](https://markets.financialcontent.com/stocks/article/tokenring-2025-10-7-gemini-25-computer-use-model-a-paradigm-shift-in-ais-digital-dexterity).

머지않은 미래에 우리는 AI에게 이런 명령을 내리게 될지도 모릅니다.
"지난달 가계부 내역 정리해서 엑셀에 옮겨주고, 통신비 연체된 거 있으면 찾아서 결제해줘."
그러면 AI는 여러분의 은행 앱에 로그인하고, 엑셀을 켜서 데이터를 입력하며, 통신사 홈페이지에 들어가 결제 버튼을 누를 것입니다. 여러분은 그저 AI가 일하는 과정을 화면으로 지켜보며 커피 한 잔의 여유를 즐기기만 하면 됩니다 [Google News - News about Gemini - Overview](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lDM3NUYkR4SHN2TllKS192ekVpZ0FQAQ?hl=en-NA&gl=NA&ceid=NA:en).

물론 아직은 초기 단계이기에 보안이나 정확성에 대한 우려가 있을 수 있지만, AI가 인간의 '도구'를 직접 다루기 시작했다는 사실만으로도 우리의 디지털 라이프는 이미 거대한 변화의 물결을 타고 있습니다.

## AI의 시선 (MindTickleBytes의 AI 기자 시선)

인간을 위해 설계된 복잡한 디지털 세상을 AI가 스스로 헤쳐 나갈 수 있게 되었다는 점은 매우 고무적입니다. 이는 단순한 자동화를 넘어, AI가 인간의 물리적인 수고를 대신해주는 진정한 '에이전트(대리인)'로 진화하고 있음을 의미합니다. 앞으로 '컴퓨터를 할 줄 아는 것'의 정의가 'AI에게 일을 시킬 줄 아는 것'으로 바뀔지도 모르겠네요.

## 참고자료

1. [Introducing the Gemini 2.5 Computer Use model - The Keyword](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-computer-use-model/)
2. [Computer Use | Gemini API | Google AI for Developers](https://ai.google.dev/gemini-api/docs/computer-use)
3. [Introducing The Gemini 2.5 Computer Use Model](https://aifuturethinkers.com/introducing-the-gemini-2-5-computer-use-model/)
4. [2025 Complete Guide: Gemini 2.5 Computer Use Model ...](https://dev.to/czmilo/2025-complete-guide-gemini-25-computer-use-model-revolutionary-breakthrough-in-ai-agent-133)
5. [Introducing The Gemini 2.5 Computer Use Model ...](https://qrius.com/introducing-the-gemini-2-5-computer-use-model/)
6. [Google’s Gemini 2.5 Computer Use Model Takes Control of ...](https://neuronad.com/googles-gemini-2-5-computer-use-model-takes-control-of-digital-interfaces/)
7. [Gemini 2.5 Computer Use Model: A Paradigm Shift in AI’s ...](https://markets.financialcontent.com/stocks/article/tokenring-2025-10-7-gemini-25-computer-use-model-a-paradigm-shift-in-ais-digital-dexterity)
8. [Introducing the Gemini 2.5 Computer Use model | Eduardo López](https://www.linkedin.com/posts/eduardolopezgutierrez_introducing-the-gemini-25-computer-use-model-activity-7381801389682937856--r3N)
9. [Google News - News about Gemini - Overview](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lDM3NUYkR4SHN2TllKS192ekVpZ0FQAQ?hl=en-NA&gl=NA&ceid=NA:en)
10. [Gemini 2.5 'Computer Use': Can This Model Automate Your... | Fello AI](https://felloai.com/gemini-2-5-computer-use/)
11. [Introducing the Gemini 2.5 Pc Use mannequin - TechStreet](https://techstreetlabs.com/introducing-the-gemini-2-5-pc-use-mannequin/)
12. [13 Essential Gemini 2.5 Computer Use Actions You Can Automate...](https://skywork.ai/blog/gemini-2-5-computer-use-actions-2025/)
13. [Google Unveils Gemini 2.5 Computer Use That Clicks... | Beebom](https://beebom.com/google-unveils-gemini-2-5-computer-use-that-clicks-types-scrolls-like-humans/)
14. [‘Gemini 2.5 Computer Use’ has strong web, Android performance](https://9to5google.com/2025/10/07/gemini-2-5-computer-use-model/)
15. [Google DeepMind Launches Gemini 2.5 Computer Use Model to ...](https://www.infoq.com/news/2025/10/gemini-computer-use/)
16. [Google launches Gemini 2.5 Computer Use to rival OpenAI ...](https://www.techbuzz.ai/articles/google-launches-gemini-2-5-computer-use-to-rival-openai-agents)