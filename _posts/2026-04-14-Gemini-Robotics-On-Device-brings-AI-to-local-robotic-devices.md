---
layout: post
title: "인터넷 끊겨도 '척척' 스스로 움직이는 로봇? 구글의 새로운 '온디바이스' AI가 가져올 변화"
description: "구글 딥마인드가 공개한 제미나이 로보틱스 온디바이스(Gemini Robotics On-Device)가 왜 로봇 기술의 새로운 전환점인지, 일반인의 눈높이에서 쉽게 설명해 드립니다."
summary: "인터넷 연결 없이도 로봇 내부에서 직접 실행되는 인공지능 '제미나이 로보틱스 온디바이스'가 공개되어, 더 빠르고 민첩한 로봇의 등장을 예고하고 있습니다."
tags: [구글, 딥마인드, AI, 로보틱스, 제미나이, 온디바이스, 기술트렌드]
image: 2026-04-14-Gemini-Robotics-On-Device-brings-AI-to-local-robotic-devices.jpg
image_alt: "다양한 작업을 수행하는 로봇 팔과 그 내부에서 작동하는 인공지능 칩을 형상화한 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "인터넷이라는 '생명줄'을 끊고도 스스로 판단하는 로봇의 등장은, AI가 구름(클라우드) 위를 벗어나 우리 곁의 실제 물리적 세계로 완전히 내려왔음을 의미합니다. 이는 단순한 성능 향상을 넘어, 로봇이 인간의 안전을 책임지는 진정한 파트너로 진화하는 결정적 계기가 될 것입니다."
quiz:
  - question: "제미나이 로보틱스 온디바이스의 가장 큰 특징은 무엇인가요?"
    choices: ["항상 인터넷에 연결되어 있어야 한다.", "로봇 기기 내부에서 직접 AI가 실행된다.", "사람이 조종기로만 움직여야 한다."]
    answer: 1
    explanation: "이 모델은 '온디바이스(On-Device)'라는 이름처럼 인터넷이나 클라우드 연결 없이 로봇 기기 자체에서 로컬로 실행됩니다."
  - question: "이 모델이 기반으로 삼고 있는 구글의 또 다른 온디바이스 AI 모델은 무엇인가요?"
    choices: ["제마(Gemma)", "파워봇(PowerBot)", "클라우드(Cloud)"]
    answer: 0
    explanation: "제미나이 로보틱스 온디바이스는 구글의 온디바이스 모델인 제마(Gemma)를 기반으로 설계되었습니다."
  - question: "제미나이 로보틱스 온디바이스가 처리하는 VLA(Vision-Language-Action) 모델의 역할은 무엇인가요?"
    choices: ["오직 텍스트만 번역한다.", "그림만 그린다.", "보고(V), 이해하고(L), 행동하는(A) 과정을 통합 처리한다."]
    answer: 2
    explanation: "VLA 모델은 시각 정보(Vision)와 언어(Language)를 이해하여 로봇의 구체적인 행동(Action)으로 연결하는 구조를 뜻합니다."
lang: ko
ref: 2026-04-14-Gemini-Robotics-On-Device-brings-AI-to-local-robotic-devices
audio: 2026-04-14-Gemini-Robotics-On-Device-brings-AI-to-local-robotic-devices.mp3
permalink: /2026/04/14/Gemini-Robotics-On-Device-brings-AI-to-local-robotic-devices/
---

**상상해보세요.** 정전이 되어 인터넷이 모두 끊긴 공장 안, 혹은 통신 신호조차 잡히지 않는 깊은 지하 시설에서 로봇이 긴박한 구조 작업을 수행해야 하는 상황을 말이죠. 지금까지의 로봇들은 대부분 '두뇌' 역할을 하는 인공지능(AI)이 멀리 떨어진 거대한 컴퓨터(클라우드)에 있었기 때문에, 인터넷이 끊기면 아무것도 할 수 없는 '먹통'이 되곤 했습니다. 마치 머리는 서울에 있는데 몸은 부산에 있는 상태에서 전화선이 끊긴 것과 같았죠.

하지만 이제 로봇이 인터넷이라는 '생명줄' 없이도 스스로 보고, 판단하고, 움직일 수 있는 시대가 열리고 있습니다. 구글 딥마인드(Google DeepMind)가 발표한 새로운 AI 모델, **'제미나이 로보틱스 온디바이스(Gemini Robotics On-Device)'** 덕분입니다. [Gemini Robotics On-Device brings AI to local robotic devices](https://deepmind.google/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/)

## 이게 왜 중요한가요?

우리가 스마트폰으로 비서 AI를 부를 때 가끔 답변이 늦게 오는 것을 경험하곤 하죠? 이건 내 목소리가 인터넷을 타고 멀리 있는 서버까지 갔다가 답변을 가지고 돌아와야 하기 때문입니다. 이를 전문 용어로 **지연 시간(Latency)**이라고 부릅니다. 

일상적인 대화에서는 1~2초의 지연이 큰 문제가 되지 않지만, 무거운 물건을 옮기거나 정밀한 조립을 하는 로봇에게 1초의 지연은 자칫 큰 사고로 이어질 수 있습니다. **'제미나이 로보틱스 온디바이스'**는 로봇의 몸체 안에 있는 그래픽 처리 장치(local GPU)를 사용하여 AI를 직접 실행합니다. [Google announces 'GeminiRoboticsOn-Device... - GIGAZINE](https://gigazine.net/gsc_news/en/20250625-gemini-robotics-on-device/)

**비유하자면**, 기존 로봇이 매번 "엄마, 이거 어디다 둬?"라고 전화를 걸어 물어보던 아이였다면, 이제는 스스로 판단하는 능력을 갖춘 '독립적인 성인'이 된 셈입니다. 이렇게 하면 인터넷 연결이 불안정하거나 아예 없는 곳에서도 로봇이 멈추지 않고 작동할 수 있으며, 무엇보다 즉각적으로 반응할 수 있어 훨씬 민첩하고 안전한 움직임이 가능해집니다. [DeepMind's Gemini Robotics On-Device brings advanced AI to local robots](https://roboticsandautomationnews.com/2025/06/26/google-deepmind-launches-new-vision-language-action-model-to-put-ai-directly-into-local-robotic-devices/92669/)

## 쉽게 이해하기: 로봇의 '눈, 입, 손'이 하나로 합쳐지다

이 기술을 이해하기 위해 꼭 알아야 할 핵심 개념이 있습니다. 바로 **VLA(Vision-Language-Action, 시각-언어-행동)** 모델입니다. [PDFGemini Robotics On-Device Model Card](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-Robotics-On-Device-Model-Card.pdf)

**쉽게 말해서**, 마치 숙련된 요리사의 '눈'과 '뇌'와 '손'이 하나로 완벽하게 연결된 시스템과 같습니다.

1.  **시각(Vision):** 로봇이 눈(카메라)을 통해 눈앞의 재료와 도구를 실시간으로 인식합니다.
2.  **언어(Language):** "사과를 깎아서 접시에 담아줘"라는 사람의 자연스러운 명령을 찰떡같이 이해합니다.
3.  **행동(Action):** 명령에 맞춰 팔을 움직여 사과를 집고 칼을 사용하는 정밀한 동작을 즉시 수행합니다.

기존에는 이 과정들이 각각 따로 놀거나 클라우드의 도움을 받아야 했지만, 제미나이 로보틱스 온디바이스는 이 모든 과정을 로봇 내부에서 한 번에 처리합니다. [Gemini Robotics On-Device: Robotics AI Autonomy to the... - KingyAI](https://kingy.ai/news/gemini-robotics-on-device/) 이를 통해 로봇은 마치 사람처럼 **'능숙한 솜씨(Dexterity, 로봇이 물체를 섬세하게 다루는 능력)'**를 발휘하며 처음 접하는 작업에도 빠르게 적응할 수 있게 됩니다. [Gemini Robotics On-Device brings AI to local robotic devices](https://aipulselab.tech/news/gemini-robotics-on-device-brings-ai-to-local-robotic-devices-4c6236)

마치 우리가 매번 부모님께 "사과는 어떻게 깎아요?"라고 전화로 물어보지 않고, 내 머릿속에 있는 지식으로 즉시 손을 움직이는 것과 같은 원리입니다.

## 현재 상황: 가볍지만 강력한 로봇의 뇌

제미나이 로보틱스 온디바이스는 구글의 **'제마(Gemma)'** 모델을 기반으로 만들어졌습니다. 제마는 기기 내부에서 가볍고 빠르게 돌아가도록 설계된 AI 모델로, 이번 로보틱스 버전은 이를 로봇 제어에 최적화시킨 것입니다. [PDFGemini Robotics On-Device Model Card](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-Robotics-On-Device-Model-Card.pdf)

이 모델의 주요 특징을 정리하면 다음과 같습니다.

*   **인터넷 없이 작동:** 클라우드 연결이 전혀 필요 없는 '클라우드 프리' 방식입니다. [Google rolls out new Gemini model that can run on robots locally](https://techcrunch.com/2025/06/24/google-rolls-out-new-gemini-model-that-can-run-on-robots-locally/)
*   **두 팔 로봇에 최적화:** 특히 사람처럼 두 팔을 가진 '양팔 로봇(bi-arm robots)'이 양손을 협동하여 복잡한 작업을 수행하는 데 특화되어 있습니다. [Gemini Robotics On-Device brings AI to local robotic devices](https://aipulselab.tech/news/gemini-robotics-on-device-brings-ai-to-local-robotic-devices-4c6236)
*   **범용성:** 특정 제조사의 로봇만 쓸 수 있는 게 아니라, 다양한 종류의 로봇과 환경에서 두루 쓰일 수 있도록 유연하게 설계되었습니다. [Google Introduces Gemini Robotics On-Device AI Model, Can Adapt to Different Types of Robots](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2pGX282NERoSGpuN1A2ZnpScUNDZ0FQAQ?hl=en-PK&gl=PK&ceid=PK:en)
*   **복잡한 명령 수행:** "이걸 집어서 저기 상자에 넣고 뚜껑을 닫아줘"와 같은 다단계 명령도 기존의 온디바이스 모델들보다 훨씬 뛰어나게 처리합니다. [Gemini Robotics On-Device also outperforms other on-device alternatives on more challenging out-of-distribution tasks and complex multi-step instructions.](https://yalladevelopment.services/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/)

현재 이 모델은 구글이 신뢰하는 소수의 파트너와 테스터들에게만 먼저 공개되어 실제 현장에서의 성능을 꼼꼼히 검증받고 있는 단계입니다. [PDFGemini Robotics On-Device Model Card](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-Robotics-On-Device-Model-Card.pdf)

## 앞으로 어떻게 될까?

전문가들은 이번 발표가 로봇 산업의 **'게임 체인저(결과나 흐름을 뒤바꿔 놓는 중요한 사건)'**가 될 것으로 보고 있습니다. [Gemini Robotics: Google Brings AI to Local Robots](https://insighttechtalk.com/tech-news/gemini-robotics-on-device-google-ai-local-robots/) 지금까지 로봇 도입을 망설이게 했던 비싼 유지 비용, 통신 보안 문제, 그리고 답답할 정도로 느린 반응 속도 문제를 한꺼번에 해결할 수 있기 때문입니다.

멀지 않은 미래에 우리는 식당에서 서빙하는 로봇이 손님의 갑작스러운 움직임에 즉각 반응하여 음식을 흘리지 않고 피하거나, 인터넷 신호가 잡히지 않는 거대 창고 구석에서도 묵묵히 재고를 정리하는 똑똑한 로봇들을 더 자주 보게 될 것입니다. [Google Launches Gemini Robotics On-Device AI: Robots Go Offline, Stay Smart](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2pGX282NERoSGpmVzIxSXBIVlNDZ0FQAQ?hl=en-IN&gl=IN&ceid=IN:en)

구글 딥마인드의 이번 시도는 AI가 단순히 화면 속의 글자나 그림에 머무는 것이 아니라, 우리와 같은 물리적인 공간에서 안전하고 민첩하게 움직이는 진정한 '동반자'로 거듭나는 중요한 발걸음이 될 것입니다. 로봇이 더 이상 '기계'가 아닌, 우리의 말을 알아듣고 현명하게 행동하는 '지능형 조력자'가 될 날이 머지않아 보입니다.

---

## 참고자료

1. [Gemini Robotics On-Device brings AI to local robotic devices](https://deepmind.google/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/)
2. [DeepMind's Gemini Robotics On-Device brings advanced AI to local robots](https://roboticsandautomationnews.com/2025/06/26/google-deepmind-launches-new-vision-language-action-model-to-put-ai-directly-into-local-robotic-devices/92669/)
3. [Google rolls out new Gemini model that can run on robots locally](https://techcrunch.com/2025/06/24/google-rolls-out-new-gemini-model-that-can-run-on-robots locally/)
4. [PDFGemini Robotics On-Device Model Card](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-Robotics-On-Device-Model-Card.pdf)
5. [Gemini Robotics On-Device brings AI to local robotic devices - AIPulse Lab](https://aipulselab.tech/news/gemini-robotics-on-device-brings-ai-to-local-robotic-devices-4c6236)
6. [Gemini Robotics On-Device: Google Brings AI to Local Robots - Insight Tech Talk](https://insighttechtalk.com/tech-news/gemini-robotics-on-device-google-ai-local-robots/)
7. [Google Introduces Gemini Robotics On-Device AI Model, Can Adapt to Different Types of Robots - Google News](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2pGX282NERoSGpuN1A2ZnpScUNDZ0FQAQ?hl=en-PK&gl=PK&ceid=PK:en)
8. [Gemini Robotics On-Device also outperforms other on-device alternatives... - Yalla Development](https://yalladevelopment.services/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/)
9. [Google announces 'GeminiRoboticsOn-Device... - GIGAZINE](https://gigazine.net/gsc_news/en/20250625-gemini-robotics-on-device/)
10. [Gemini Robotics On-Device: Robotics AI Autonomy to the... - KingyAI](https://kingy.ai/news/gemini-robotics-on-device/)
11. [Google Launches Gemini Robotics On-Device AI: Robots Go Offline, Stay Smart - Google News](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2pGX282NERoSGpmVzIxSXBIVlNDZ0FQAQ?hl=en-IN&gl=IN&ceid=IN:en)