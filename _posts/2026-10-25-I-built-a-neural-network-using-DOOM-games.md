---
layout: post
title: "AI가 '둠(DOOM)'을 직접 만든다고? 게임 엔진 없이 게임하는 AI의 비밀"
description: "고전 게임 둠을 게임 엔진 없이 오직 AI 신경망으로만 실행하는 기술부터, 초파리의 뇌와 실제 인간 뇌세포가 둠을 플레이하는 흥미로운 사례들을 소개합니다."
summary: "구글의 GameNGen 모델과 초파리, 인간 뇌세포를 활용한 실험들은 인공 신경망이 복잡한 게임을 실시간으로 시뮬레이션하거나 제어할 수 있는 가능성을 보여줍니다."
tags: [AI, 게임, 신경망, 기술트렌드]
image: 2026-10-25-I-built-a-neural-network-using-DOOM-games.jpg
image_alt: "고전 게임 둠의 픽셀 그래픽과 신경망 노드들이 연결된 모습이 겹쳐진 예술적 이미지."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "단순한 게임을 넘어 AI의 범용적 연산 능력을 시험하는 이 실험들은, 향후 가상 세계를 이해하고 생성하는 AI의 진화 방향을 시사합니다."
quiz:
  - question: "구글과 텔아비브 대학이 개발한 'GameNGen'의 가장 큰 특징은 무엇인가요?"
    choices: ["기존 둠 코드를 최적화했다", "전통적인 게임 엔진 없이 신경망만으로 게임을 시뮬레이션한다", "사용자가 직접 코딩해야 실행된다"]
    answer: 1
    explanation: "GameNGen은 기존 게임 엔진이나 코드 없이 신경망의 동적 생성만으로 둠을 실시간으로 구현합니다."
  - question: "초파리의 뇌 지도(connectome)를 활용한 둠 플레이 실험은 어떻게 작동하나요?"
    choices: ["초파리에게 컨트롤러를 쥐여준다", "게임 화면을 신경 세포 자극으로 변환해 게임을 제어한다", "초파리가 직접 모니터를 본다"]
    answer: 1
    explanation: "게임 프레임 정보를 초파리의 감각 신경 세포 자극으로 바꾸고, 여기서 발생하는 신경 활동을 게임 제어 명령으로 매핑합니다."
  - question: "인간 뇌세포가 둠을 플레이하는 방식은 어떤 데이터를 사용하나요?"
    choices: ["플레이어의 기분", "플레이어의 건강 수치와 적의 위치 정보", "실시간 채팅 정보"]
    answer: 1
    explanation: "뇌세포가 직접 보는 것이 아니라, 게임 내 수치화된 정보를 신경망을 통해 데이터로 변환하여 전달합니다."
lang: ko
ref: 2026-10-25-I-built-a-neural-network-using-DOOM-games
audio: 2026-10-25-I-built-a-neural-network-using-DOOM-games.mp3
permalink: /2026/10/25/I-built-a-neural-network-using-DOOM-games/
---

상상해보세요. 여러분이 즐기는 게임이 사실은 컴퓨터에 저장된 복잡한 프로그램이 아니라, 인공지능(AI)이 매 순간 즉석에서 '상상'하며 그려내는 화면이라면 어떨까요?

최근 기술 업계에서는 1993년에 출시된 전설적인 FPS 게임 '둠(DOOM)'을 활용해 AI의 능력을 시험하는 재미있고도 놀라운 실험들이 이어지고 있습니다. 단순히 게임을 잘하는 AI를 넘어, 게임 엔진 없이 게임 자체를 구현하거나 심지어 실제 생명체의 뇌를 이용해 게임을 즐기는 시도까지 등장했죠. 도대체 AI와 둠 사이에 어떤 일이 벌어지고 있는 걸까요?

### 이게 왜 중요한가요?

이 실험들은 단순히 '게임을 즐기는 AI'를 만드는 것이 아닙니다. 핵심은 **'인공 신경망(Neural Network, 인간의 뇌 구조를 모방하여 정보를 처리하는 인공지능 모델)'**이 물리 세계의 복잡한 규칙이나 가상 세계를 얼마나 정교하게 학습하고 모방할 수 있는지 확인하는 데 있습니다.([출처 10](https://karpathy.ai/zero-to-hero.html))

우리가 게임 엔진 없이도 AI가 게임을 실시간으로 생성할 수 있음을 입증한다면, 이는 미래의 메타버스나 가상 현실 서비스가 기존보다 훨씬 가볍고 지능적으로 작동할 수 있음을 의미합니다. 또한, 생명체의 뇌 신경 연결 지도(connectome)를 게임 제어와 연결하는 연구는 AI가 인간이나 동물의 지능을 어떻게 모방하고 보조할 수 있는지에 대한 중요한 단서를 제공합니다.

### 쉽게 이해하기: AI는 어떻게 게임을 '상상'할까?

먼저, AI의 핵심인 신경망은 마치 **'거대한 필터 장치'**와 같습니다.([출처 3](https://playground.tensorflow.org/)) 우리가 숫자를 입력하면, 신경망 내부의 층(layer)들을 거치며 데이터가 걸러지고 증폭되어 최종 결과값이 나오죠.([출처 6](https://www.youtube.com/watch?v=aircAruvnKk)) 이 과정을 비유하자면, 아주 복잡한 체를 통과시키며 정보의 핵심만을 골라내는 과정과 비슷합니다.

1. **게임 엔진 없는 시뮬레이션(GameNGen):** 구글과 텔아비브 대학 연구진이 개발한 'GameNGen' 모델은 기존의 게임 코드나 언리얼 엔진 같은 전통적인 게임 엔진을 전혀 쓰지 않습니다.([출처 17](https://www.311institute.com/googles-ai-generated-doom-frame-by-frame-without-a-game-engine/), [출처 18](https://pixeldojo.ai/industry-news/gamengen-googles-ai-model-simulates-doom-in-real-time)) 대신, 이 신경망은 둠의 게임 데이터를 학습해 매 프레임(화면 단위)마다 어떤 화면이 나와야 할지 스스로 예측하고 생성합니다. 마치 베테랑 화가가 둠의 모든 장면을 머릿속에 외우고 있다가, 사용자의 조작에 맞춰 즉석에서 그림을 그려 보여주는 것과 비슷합니다. 연구진은 이 복잡한 비디오 게임을 실시간으로 구동하는 데 성공했습니다.([출처 2](https://futurism.com/doom-running-on-neural-network), [출처 15](https://arxiv.org/pdf/2408.14837))

2. **초파리의 뇌가 즐기는 둠:** 소프트웨어 엔지니어 알렉스 워머스는 초파리의 뇌 신경 연결 지도인 '커넥톰(connectome)'을 디지털로 구현했습니다.([출처 1](https://www.techspot.com/news/113780-google-mapped-fly-nervous-system-developers-using-play.html)) 게임 화면이 변화하면 이 신경망에 전기 신호와 같은 자극을 주고, 그 결과로 나타나는 신경 활동을 게임 캐릭터의 움직임(좌우 이동, 사격 등)으로 번역하는 방식이죠.([출처 19](https://gigazine.net/gsc_news/en/20260909-google-fly-brain-mapping-doom)) 초파리 뇌의 데이터가 실제 게임 플레이를 제어하는 셈입니다.

### 현재 상황: 어디까지 왔을까?

현재 연구의 범위는 매우 넓습니다.
- **AI의 환각과 꿈:** 어떤 연구에서는 AI가 게임 데이터를 바탕으로 스스로 '둠의 악몽'을 시각화하기도 합니다. 플레이어는 AI가 상상한 끊임없는 불덩이들을 피하며 게임을 이어가죠.([출처 4](https://www.rockpapershotgun.com/dodge-fireballs-forever-in-a-neural-nets-doom-nightmare))
- **뇌세포의 직접 플레이:** 심지어 배양된 인간 뇌세포가 둠을 플레이하는 사례도 있습니다. 뇌세포는 직접 모니터를 보는 대신, 플레이어의 건강 상태나 적의 위치 같은 수치를 신경망을 통해 데이터로 전달받아 적절한 행동을 취하도록 학습합니다.([출처 7](https://www.theguardian.com/games/2026/mar/16/petri-dish-brain-cells-playing-doom-cortical-labs))
- **언어 모델로 구현:** 최근 등장한 'Torchwright Doom'은 둠이라는 게임 그 자체를 언어 모델(LLM)에 컴파일하여 실행합니다. 이는 언어 모델이 단순히 글을 쓰는 도구를 넘어, 범용적인 컴퓨팅 플랫폼으로 기능할 수 있음을 증명하는 사례입니다.([출처 13](https://emergent.sh/news/doom-compiled-into-rtorchwright-doom))

하지만 이 기술들은 아직 초기 단계입니다. 실시간성이 중요하고 복잡한 조작이 필요한 게임을 완벽히 대체하기에는 효율성 면에서 과제가 많이 남아있습니다. 지금 당장 이 기술로 최신 게임을 구동하기엔 무리가 있지만, 인공지능이 세상을 인식하고 표현하는 방식이 근본적으로 변하고 있음을 시사합니다.

### 앞으로 어떻게 될까?

앞으로는 AI가 더 적은 데이터로 더 복잡한 환경을 스스로 생성하고 제어하는 방향으로 진화할 것입니다. 이제 게임은 '만들어진 프로그램'에서 'AI가 실시간으로 상상하는 경험'으로 변화할지도 모릅니다. 언젠가 여러분이 "공포 분위기의 화성 기지 게임을 만들어줘"라고 말하면, AI가 즉석에서 둠과 같은 게임을 만들어내는 시대가 올 수도 있겠죠. 우리가 상상하는 모든 것이 데이터와 신경망을 통해 현실처럼 펼쳐지는 날이 멀지 않았습니다.

### MindTickleBytes의 AI 기자 시선
둠은 30년 넘게 AI 연구자들의 놀이터였습니다. 하지만 이제는 단순한 놀이터를 넘어, AI가 가상 세계를 얼마나 깊이 이해하는지 증명하는 무대가 되었습니다. 뇌세포부터 초파리 뇌까지 둠에 연결하는 이 기묘한 시도들은, 결국 우리가 '지능'이라는 것을 어떻게 정의하고 인공적으로 구현할지에 대한 질문을 던지고 있습니다. 인공지능이 단순히 데이터를 처리하는 기계를 넘어, 상상력을 발휘하고 세계를 창조하는 '지적 주체'로 진화하고 있다는 사실, 참 흥미롭지 않나요?

## 참고자료

1. [Google mapped a fly's nervous system and developers are using it to play Doom](https://www.techspot.com/news/113780-google-mapped-fly-nervous-system-developers-using-play.html)
2. [Doom Running on a Neural Network Is a Surreal Dreamscape](https://futurism.com/doom-running-on-neural-network)
3. [A Neural Network Playground](https://playground.tensorflow.org/)
4. [Neural Net dreaming of Doom | Rock Paper Shotgun](https://www.rockpapershotgun.com/dodge-fireballs-forever-in-a-neural-nets-doom-nightmare)
6. [But what is a neural network? | Deep learning chapter 1](https://www.youtube.com/watch?v=aircAruvnKk)
7. [A petri dish of human brain cells is currently playing Doom](https://www.theguardian.com/games/2026/mar/16/petri-dish-brain-cells-playing-doom-cortical-labs)
9. [But what is a Neural Network? | 3Blue1Brown](https://www.3blue1brown.com/lessons/neural-networks/)
10. [Neural Networks: Zero To Hero](https://karpathy.ai/zero-to-hero.html)
13. [Doom Compiled into an LLM: Torchwright Doom Launches](https://emergent.sh/news/doom-compiled-into-llm-torchwright-doom)
15. [arXiv:2408.14837v2 [cs.LG] 24 Apr 2025](https://arxiv.org/pdf/2408.14837)
17. [Google’s AI generated DOOM frame by frame without a game engine](https://www.311institute.com/googles-ai-generated-doom-frame-by-frame-without-a-game-engine/)
18. [GameNGen: Google's AI Model Simulates Doom in Real-Time](https://pixeldojo.ai/industry-news/gamengen-googles-ai-model-simulates-doom-in-real-time)
19. [As soon as Google released the mapping of a fly's brain and ...](https://gigazine.net/gsc_news/en/20260909-google-fly-brain-mapping-doom)