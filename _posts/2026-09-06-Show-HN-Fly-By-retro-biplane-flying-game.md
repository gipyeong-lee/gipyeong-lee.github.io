---
layout: post
title: "추억의 복엽기를 조종해볼까? 3D로 돌아온 레트로 비행 게임 'Fly By'"
description: "웹 브라우저에서 즐기는 복고풍 3D 비행 게임 Fly By의 특징과 매력, 그리고 웹 기술로 구현된 레트로 감성에 대해 알아봅니다."
summary: "최근 공개된 'Fly By'는 Three.js를 활용한 웹 기반 3D 비행 게임으로, 특유의 스캔 라인 효과를 통해 80~90년대 레트로 게임의 향수를 자극합니다."
tags: [레트로게임, 웹게임, FlyBy, Three.js, 비행게임]
image: 2026-09-06-Show-HN-Fly-By-retro-biplane-flying-game.jpg
image_alt: "화면 전체에 스캔 라인 효과가 적용된 복엽기 비행 게임 Fly By의 화면 모습."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "복잡한 고사양 게임 사이에서 웹 기술로 구현한 소박하지만 정교한 레트로 게임은 사용자에게 훌륭한 휴식처를 제공합니다."
quiz:
  - question: "이 기사에서 소개한 'Fly By' 게임이 사용하는 시각 효과는 무엇인가요?"
    choices: ["실사 그래픽", "스캔 라인 효과", "픽셀 아트"]
    answer: 1
    explanation: "Fly By는 특유의 레트로한 분위기를 살리기 위해 스캔 라인 효과를 사용합니다."
  - question: "Fly By는 어떤 기술로 제작되었나요?"
    choices: ["Unity", "Unreal Engine", "Three.js"]
    answer: 2
    explanation: "Fly By는 웹 기반의 3D 라이브러리인 Three.js를 사용하여 제작되었습니다."
  - question: "복엽기(Biplane)의 특징은 무엇인가요?"
    choices: ["날개가 하나인 비행기", "날개가 두 개인 비행기", "헬리콥터의 일종"]
    answer: 1
    explanation: "복엽기는 위아래로 두 개의 날개가 겹쳐져 있는 형태의 항공기를 말합니다."
lang: ko
ref: 2026-09-06-Show-HN-Fly-By-retro-biplane-flying-game
audio: 2026-09-06-Show-HN-Fly-By-retro-biplane-flying-game.mp3
permalink: /2026/09/06/Show-HN-Fly-By-retro-biplane-flying-game/
---

상상해보세요. 어린 시절, 동네 오락실이나 낡은 브라운관 TV 앞에서 시간 가는 줄 모르고 조이스틱을 움직이던 그 순간을 말이죠. 지지직거리는 노이즈와 화면을 가로지르는 미세한 줄무늬, 그리고 단순하지만 몰입감 넘쳤던 비행기 게임들 말입니다. 최근 웹 커뮤니티에서 이 시절의 향수를 정조준한 게임이 하나 등장해 화제입니다. 바로 'Fly By'입니다.

## 이게 왜 중요한가요?

최근 출시되는 게임들은 현실과 구분하기 어려울 정도로 엄청난 사양과 정교한 그래픽을 자랑합니다. 하지만 때로는 그런 복잡함 대신, 예전의 단순함이 주는 '코지(Cozy, 아늑하고 편안한)한 재미'를 찾는 사람들이 많습니다. 'Fly By'는 복잡한 설치 과정 없이 웹 브라우저만 있다면 누구나 즉시 옛날 비행 게임의 감성을 즐길 수 있다는 점에서 큰 의미가 있습니다. 이는 현대 기술이 단순히 고성능만을 지향하는 것이 아니라, 과거의 감성을 현재의 기술로 어떻게 아름답게 재해석할 수 있는지를 잘 보여주는 사례입니다 [출처 3](https://www.darkhackernews.com/item?id=49519101).

## 쉽게 이해하기: 3D와 레트로의 만남

'Fly By'는 겉보기엔 아주 오래된 게임 같지만, 실제로는 최신 웹 기술의 결정체입니다. 이 게임은 'Three.js(쓰리 제이에스)'라는 웹 기반 3D 라이브러리를 사용하여 만들어졌습니다 [출처 4](https://x.com/grok/status/2041124655033954732). 

쉽게 비유하자면, 도화지에 그림을 그리는 것이 아니라, 투명한 유리판 여러 장을 겹쳐서 입체적인 공간을 만들고 그 위에 색을 입히는 방식이라고 생각하면 됩니다. 여기에 '셰이더(Shader, 화면의 색상이나 질감을 바꾸는 특수 효과 처리 기술)'를 사용하는데, 이는 마치 스마트폰의 사진 앱에서 '빈티지'나 '필름' 효과를 선택하는 것과 비슷합니다. 개발자는 이 셰이더를 통해 화면에 '스캔 라인(Scan lines, 브라운관 모니터에서 화면을 그릴 때 생기는 가로 줄무늬)'을 입혔습니다 [출처 1](https://news.ycombinator.com/item?id=49519101). 옛날 브라운관 TV에서 볼 수 있었던 그 정겨운 가로줄 무늬 덕분에 사용자는 이 3D 게임을 보면서도 80년대 레트로 비행 게임을 하는 듯한 강력한 향수를 느끼게 되는 것이죠.

복엽기(Biplane, 날개가 위아래로 두 개 겹쳐져 있는 항공기)라는 소재 또한 레트로한 감성을 한층 더해줍니다. 복엽기는 초기 항공 역사에서 매우 중요한 역할을 했던 기체로, 고전적인 비행의 맛을 살리는 데 안성맞춤인 선택입니다 [출처 2](https://en.wikipedia.org/wiki/Biplane), [출처 5](https://www.youtube.com/shorts/JxUg9XZrxiI).

## 현재 상황

현재 'Fly By'는 누구나 자유롭게 시도해볼 수 있는 웹 기반의 데모 게임입니다. 우리가 흔히 접하는 거대한 비행 시뮬레이션 게임들이 방대한 조작법을 학습해야 하고 높은 사양의 PC를 요구하는 것과 달리 [출처 6](https://en.wikipedia.org/wiki/List_of_flight_simulator_video_games), 이 게임은 웹 환경에서 가볍게 즐길 수 있는 'Cozy 3D 비행 게임'을 지향합니다 [출처 4](https://x.com/grok/status/2041124655033954732). 고전적인 비행의 즐거움을 느끼고 싶은 분들에게는 더할 나위 없는 최고의 선택지가 될 것입니다 [출처 1](https://news.ycombinator.com/item?id=49519101).

## 앞으로 어떻게 될까?

'Fly By'처럼 웹 기술을 활용한 레트로풍 게임들은 앞으로 더욱 늘어날 전망입니다. 개발자들은 단순히 게임을 제작하는 데 그치지 않고, 셰이더와 같은 간단한 코드 기법들을 사용해 게임을 훨씬 더 '레트로'하게 만드는 기술들을 계속 탐구하고 있습니다 [출처 4](https://x.com/grok/status/2041124655033954732). 웹 브라우저가 점점 더 강력해짐에 따라, 앞으로 우리는 더 많은 과거의 유산들이 세련된 최신 기술로 재탄생하는 모습을 목격하게 될 것입니다.

## MindTickleBytes의 AI 기자 시선

레트로 게임은 단순히 과거를 똑같이 재현하는 것이 아닙니다. 복잡한 현대 사회에서 우리가 잃어버린 '단순함의 미학'을 현재의 기술로 되살려내는 마법과도 같죠. 'Fly By'는 웹 기술이 어떻게 우리의 기억을 따뜻하게 소환할 수 있는지 보여주는 아주 좋은 사례입니다.

## 참고자료

1. [ShowHN: Fly By – retro biplane flying game | Hacker News](https://news.ycombinator.com/item?id=49519101)
2. [Biplane - Wikipedia](https://en.wikipedia.org/wiki/Biplane)
3. [Show HN: Fly By – retro biplane flying game | Dark Hacker News](https://www.darkhackernews.com/item?id=49519101)
4. [It's a fun demo of a cozy 3D flying game built in Three.js ...](https://x.com/grok/status/2041124655033954732)
5. [Why Airplanes Have Curved Wing Tips - YouTube](https://www.youtube.com/shorts/JxUg9XZrxiI)
6. [List of flight simulator video games - Wikipedia](https://en.wikipedia.org/wiki/List_of_flight_simulator_video_games)