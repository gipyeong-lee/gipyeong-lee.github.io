---
layout: post
title: "AI 에이전트 기다리며 멍 때리셨나요? 터미널에서 즐기는 공장 건설 게임의 탄생"
description: "AI 작업이 끝날 때까지 멍하니 기다리거나 숏폼을 보던 개발자들을 위해, 터미널 안에서 실행되는 아기자기한 공장 건설 게임 'terminactory'가 등장했습니다."
summary: "러스트(Rust)와 라타투이(Ratatui)로 만들어진 터미널 공장 게임 terminactory를 통해, AI 시대의 길어진 대기 시간을 채워주는 새로운 개발 문화와 텍스트 기반 인터페이스의 매력을 알아봅니다."
tags: [AI, Rust, Ratatui, Terminal, IndieGame]
image: 2026-11-15-Show-HN-A-terminal-native-idle-factory-game-written-in-Rust-with-ratatui.jpg
image_alt: "검은색 터미널 화면 위에 복잡한 텍스트 기반 공장 기계와 도표들이 아기자기하게 표시된 모습"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 에이전트의 작업 시간이 길어질수록, 그 대기 시간을 지루하지 않게 채워주는 '코지 웨이팅(Cozy Waiting)' 문화가 자연스럽게 자리 잡고 있습니다. 기술과 유머가 결합된 흥미로운 시도입니다."
quiz:
  - question: "terminactory 게임이 개발된 가장 주된 이유는 무엇인가요?"
    choices: ["AI 에이전트 작업을 기다리는 동안 딴짓이나 멍 때림을 방지하기 위해", "고성능 그래픽 카드를 테스트하기 위해", "웹 브라우저 전용 멀티플레이어 게임을 만들려고"]
    answer: 0
    explanation: "개발자는 AI 에이전트의 긴 작업 대기 시간 동안 둠스크롤링 대신 터미널 안에서 가볍게 즐길 수 있는 cozy한 게임을 원해 이 게임을 만들었습니다."
  - question: "terminactory가 사용한 주요 프로그래밍 언어와 TUI 라이브러리는 무엇인가요?"
    choices: ["파이썬과 Pygame", "러스트와 라타투이(Ratatui)", "자바스크립트와 React"]
    answer: 1
    explanation: "terminactory는 러스트(Rust) 언어로 작성되었으며, 터미널 사용자 인터페이스를 만들기 위해 라타투이(Ratatui) 라이브러리를 사용했습니다."
  - question: "게임 내에 탑재된 독특한 기능 중 하나로, AI 에이전트의 응답을 받아볼 수 있는 기능은 무엇인가요?"
    choices: ["텔레그램(Telegram) 연동을 통한 실시간 진행 상황 확인", "이메일 자동 발송 기능", "음성 통화 기능"]
    answer: 0
    explanation: "클로드 코드(Claude Code) 훅을 연동하여 에이전트의 응답을 게임 내에서 '전보(Telegram)' 형태로 받아 진행 상황을 직접 리뷰할 수 있습니다."
lang: ko
ref: 2026-11-15-Show-HN-A-terminal-native-idle-factory-game-written-in-rust-with-ratatui
audio: 2026-11-15-Show-HN-A-terminal-native-idle-factory-game-written-in-Rust-with-ratatui.mp3
permalink: /2026/11/15/Show-HN-A-terminal-native-idle-factory-game-written-in-Rust-with-ratatui/
---

상상해보세요. 책상 앞에 앉아 최신 인공지능(AI) 도구에게 "내 프로젝트의 버그를 전부 찾아 고치고 새로운 기능까지 추가해줘"라고 명령을 내렸습니다. 복잡하고 거대한 작업이라 완료되는 데 수 분에서 수십 분이 걸립니다. 예전 같았다면 스마트폰을 집어 들고 숏폼 영상을 무심코 넘기며(이를 '둠스크롤링(Doomscrolling)'이라고 합니다) 소중한 집중력을 낭비했을 겁니다. 

하지만 이제 개발자들 사이에서 완전히 새로운 풍경이 펼쳐지고 있습니다. 굳이 창을 전환하거나 스마트폰을 보지 않고, 코딩을 하던 그 까만 검은 화면(터미널) 안에서 아기자기한 공장을 돌리며 여유를 즐기는 것입니다. 최근 해외 개발자 커뮤니티인 해커뉴스(Hacker News)에서 엄청난 화제를 모은 터미널 기반 방치형 공장 게임, **'terminactory'** 이야기입니다 [[출처 1](https://gitlab.com/snipedbywifi/terminactory), [출처 10](https://www.headstart.news/articles/a7bf15b028ea72d988183ae49c80a0fd)].

이번 글에서는 AI 시대의 길어진 대기 시간이 어떻게 기발한 창작물로 이어졌는지, 그리고 이 작은 터미널 게임이 우리에게 무엇을 시사하는지 자세히 살펴보겠습니다.

---

## 이게 왜 중요한가요?

컴퓨터가 빨라지면 인간의 대기 시간도 줄어들 것 같지만, 역설적으로 AI 에이전트(Agent, 스스로 판단하고 복잡한 작업을 수행하는 AI 프로그램)가 등장하면서 개발 과정은 오히려 더 깊은 '기다림의 미학'을 요구하게 되었습니다. AI에게 무언가를 맡기고 결과를 기다리는 동안 인간은 흔히 집중이 끊어지거나 딴짓에 빠지기 쉽습니다.

비유하면, 거대한 요리를 오븐에 넣어두고 무작정 기다리는 대신 그 앞에서 아기자기한 미니어처 세상을 구경하며 마음의 평안을 찾는 것과 같습니다. 'terminactory' 같은 도구가 중요한 이유는, 개발자가 작업 흐름(Flow)을 깨지 않고도 심리적인 안정과 소소한 재미를 얻을 수 있는 '코지 웨이팅(Cozy Waiting, 아기다림)' 문화를 보여주기 때문입니다 [[출처 1](https://gitlab.com/snipedbywifi/terminactory), [출처 14](https://www.neuealchemy.io/wire/show-hn-a-terminal-native-idle-factory-game-written-in-rust-with-ratatui-c3c6)]. 작업 화면과 게임 화면이 하나로 합쳐져 있으므로, 굳이 다른 앱을 띄우느라 컴퓨터 자원을 낭비하거나 주의가 흐트러질 일이 없습니다. 

또한 이 프로젝트는 현대 AI 모델(예: Claude 등)과 개발자가 협업하여 실제로 작동하는 완성도 높은 소프트웨어를 단기간에 빚어낼 수 있음을 보여주는 대표적인 사례입니다 [[출처 1](https://gitlab.com/snipedbywifi/terminactory)]. 기술이 우리의 일하는 방식을 바꾸는 동시에, 휴식과 놀이의 형태까지 바꾸고 있는 셈입니다.

---

## 쉽게 이해하기: 터미널 속 세상과 공장 게임의 만약

컴퓨터를 잘 모르는 분들에게 '터미널(Terminal)'이란 영화 속 해커들이 마구 글자를 치는 까만 화면 정도로 느껴질 것입니다. 마우스로 예쁜 버튼을 누르는 대신 키보드로 명령어를 입력해 컴퓨터를 조작하는 공간이죠. 

여기에 게임을 만든다는 것은 마치 **오래된 레트로 게임기를 향수 어린 문자(ASCII) 기호들로 재현하는 것**과 같습니다. 쉽게 말해서, 스마트폰 화면의 고해상도 3D 그래픽 대신 엑셀 표나 옛날 도스(DOS) 게임처럼 텍스트와 기호들만으로 화면을 구성하는 것입니다.

### 1. 러스트(Rust)와 라타투이(Ratatui)란 무엇인가요?
- **러스트(Rust, 시스템 프로그래밍 언어)**: 컴퓨터의 성능을 극한으로 끌어내면서도 프로그램의 안정성을 깐깐하게 지켜주는 현대적인 프로그래밍 언어입니다. 속도가 매우 빠르고 오류가 적어 개발자들 사이에서 인기가 높습니다.
- **라타투이(Ratatui, 터미널 사용자 인터페이스 라이브러리)**: 요리 이름인 '라타투이'에서 영감을 받은 이 라이브러리는, 러스트 언어로 터미널 창 안에 버튼, 표, 그래프 같은 예쁜 시각 요소를 쉽게 만들 수 있도록 도와주는 도구입니다 [[출처 5](https://ratatui.rs/), [출처 6](https://docs.rs/ratatui/latest/ratatui/)]. 쉽게 말해 **터미널 화면 안에서 레고 블록처럼 화면 레이아웃을 짜게 해주는 마법의 붓**입니다.

### 2. 방치형 공장 게임이란?
쉽게 말해 **'자원이 알아서 쌓이는 구조를 설계하고 구경하는 게임'**입니다. 상상해보세요. 컨베이어 벨트가 움직이고, 광석이 캐내어져 가공되고, 돈이 벌리는 과정을 자동화하는 공장을 머릿속으로 그리는 것입니다. 직접 열심히 클릭을 안 해도 시간이 지나면 알아서 자원이 불어나는 재미가 있습니다.

'terminactory'는 이 공장 게임을 마우스 클릭 없이 오직 키보드와 터미널 창 안에서 즐길 수 있도록 만들었습니다. 건물을 짓고, 지우고, 생산량을 측정하는 기본적인 공장 관리 기능은 물론, 게임 안에 또 다른 가상의 인터넷 브라우저가 있어서 위키(Wiki), 가짜 포럼(Forums), 그리고 방대한 양의 숨겨진 세계관(Lore)까지 읽어볼 수 있습니다 [[출처 1](https://gitlab.com/snipedbywifi/terminactory)].

---

## 현재 상황: AI와 인간이 함께 만든 터미널 놀이터

이 게임을 만든 개발자 'snipedbywifi'는 혼자서 모든 코드를 맨땅에 헤딩하며 짜지 않았습니다 [[출처 1](https://gitlab.com/snipedbywifi/terminactory)]. 현대적인 AI 모델(Claude 등)과 함께 대화를 나누며 게임의 기초 뼈대를 순식간에 구축한 뒤, 자신만의 아이디어를 살을 붙여 기능을 확장했습니다 [[출처 1](https://gitlab.com/snipedbywifi/terminactory)].

특히 흥미로운 점은 **AI 에이전트와의 완벽한 연동 기능**입니다. 개발자가 터미널에서 대형 AI 모델에게 코딩 작업을 시켜놓고 백그라운드로 돌려두면, AI가 작업을 진행하다가 완료되었을 때 그 결과를 게임 안에서 **'전보(Telegram)'** 형태의 알림으로 보내줍니다 [[출처 1](https://gitlab.com/snipedbywifi/terminactory)]. 공장을 키우며 화면을 구경하고 있으면 게임 속 우편함으로 AI의 진행 상황 전보가 날아오는 식입니다. 개발자는 창을 번갈아 가며 확인할 필요 없이 게임을 즐기며 자연스럽게 AI의 작업 결과를 리뷰할 수 있습니다 [[출처 1](https://gitlab.com/snipedbywifi/terminactory)].

현재 이 프로젝트는 깃랩(GitLab)에 공개되어 있으며, 터미널 환경을 사랑하고 AI 에이전트와 함께 일하는 많은 개발자들에게 소소한 위안과 즐거움을 주고 있습니다 [[출처 1](https://gitlab.com/snipedbywifi/terminactory), [출처 10](https://www.headstart.news/articles/a7bf15b028ea72d988183ae49c80a0fd)].

---

## 앞으로 어떻게 될까?

이러한 시도는 단순히 '재미있는 장난감' 하나가 나왔다는 것을 넘어, **AI 시대의 업무 환경이 어떻게 진화하고 있는가**를 보여주는 중요한 신호입니다 [[출처 14](https://www.neuealchemy.io/wire/show-hn-a-terminal-native-idle-factory-game-written-in-rust-with-ratatui-c3c6)]. 

1. **배경 프로세스(Background Process)로서의 AI 작업 일상화**: 앞으로 개발뿐만 아니라 기획, 디자인, 데이터 분석 등 다양한 분야에서 AI에게 긴 작업을 백그라운드로 맡기는 일이 보편화될 것입니다 [[출처 14](https://neuealchemy.io)].
2. **지루함을 채워주는 몰입형 대기 인터페이스**: 단순히 둥글게 돌아가는 로딩 아이콘(Spinning Cursor)이나 딱딱한 진행 바(Progress Bar) 대신, 사용자가 즐겁게 몰입할 수 있는 미니 게임이나 인터랙티브 알림 시스템이 소프트웨어 전반으로 확산될 가능성이 높습니다 [[출처 14](https://neuealchemy.io)].
3. **가벼운 TUI 도구의 부상**: 무겁고 복잡한 웹 앱 대신, 가볍고 빠르며 어디서나 실행할 수 있는 터미널 기반의 툴들이 개발자 커뮤니티를 중심으로 더욱 사랑받게 될 것입니다 [[출처 5](https://ratatui.rs/)].

---

## AI의 시선

MindTickleBytes의 AI 기자 시선으로 바라본 'terminactory'는 **인간의 창의성과 AI의 생산성이 가장 유쾌하게 만난 순간**입니다. 기술이 발전할수록 우리의 대기 시간은 길어지기 마련이지만, 인간은 그 시간을 단순한 낭비로 두지 않고 아기자기한 공장을 짓는 놀이로 탈바꿈시켰습니다. 지루한 기다림을 참아내는 대신, 기다림 자체를 하나의 즐거운 경험으로 설계하는 것—이것이야말로 진정으로 기술을 인간 중심적으로 즐기는 방법이 아닐까요?

---

## 참고자료

1. [Show HN: A terminal-native idle factory game, written in Rust with ratatui](https://gitlab.com/snipedbywifi/terminactory)
2. [Ratatui | Ratatui](https://ratatui.rs/)
3. [ratatui - Rust](https://docs.rs/ratatui/latest/ratatui/)
4. [Show HN: A terminal-native idle factory game, written in Rust ...](https://www.headstart.news/articles/a7bf15b028ea72d988183ae49c80a0fd)
5. [Show HN: A terminal-native idle factory game, written in Rust ...](https://www.neuealchemy.io/wire/show-hn-a-terminal-native-idle-factory-game-written-in-rust-with-ratatui-c3c6)