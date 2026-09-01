---
layout: post
title: "내 컴퓨터 속 숨겨진 거인: ChatGPT 앱은 왜 LibreOffice를 품고 있을까?"
description: "최근 발견된 ChatGPT 데스크톱 앱의 1.7GB 거대 번들, 그 안에 숨겨진 LibreOffice와 개발 도구들에 대해 알아봅니다."
summary: "OpenAI의 ChatGPT 데스크톱 앱이 설치 과정에서 1.7GB에 달하는 외부 소프트웨어 패키지를 숨겨둔 사실이 밝혀졌습니다."
tags: [ChatGPT, OpenAI, 소프트웨어, LibreOffice, 기술뉴스]
image: 2026-09-02-The-ChatGPTCodex-app-bundles-a-full-copy-of-LibreOffice.jpg
image_alt: "ChatGPT 앱의 내부 폴더 구조를 보여주는 추상적인 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "단순한 채팅 앱인 줄 알았던 ChatGPT가 사실은 강력한 개발 및 문서 처리 엔진을 내장하고 있다는 점이 흥미롭습니다. 이는 AI가 단순한 대화 상대를 넘어 사용자의 컴퓨터 안에서 실질적인 '작업'을 수행하는 에이전트로 진화하고 있음을 보여줍니다."
quiz:
  - question: "ChatGPT 데스크톱 앱 내의 'codex-primary-runtime' 폴더 용량은?"
    choices: ["170MB", "1.7GB", "17GB"]
    answer: 1
    explanation: "해당 폴더는 약 1.7GB의 소프트웨어 패키지를 포함하고 있습니다."
  - question: "이 번들에 포함되지 않은 소프트웨어는 무엇인가요?"
    choices: ["Python", "Node.js", "Microsoft Word"]
    answer: 2
    explanation: "번들에는 파이썬(Python), 노드(Node.js), 그리고 리브레오피스(LibreOffice) 등이 포함되어 있지만 MS Word는 포함되어 있지 않습니다."
  - question: "왜 이 앱은 LibreOffice 같은 외부 도구를 함께 설치할까요?"
    choices: ["단순한 용량 낭비", "문서 작업을 위한 내부 도구 활용", "삭제 불가능한 라이브러리"]
    answer: 1
    explanation: "함께 포함된 기술 문서들을 통해 AI가 이 바이너리들을 찾아 활용하는 방법을 배우기 때문입니다."
lang: ko
ref: 2026-09-02-The-ChatGPTCodex-app-bundles-a-full-copy-of-LibreOffice
audio: 2026-09-02-The-ChatGPTCodex-app-bundles-a-full-copy-of-LibreOffice.mp3
permalink: /2026/09/02/The-ChatGPTCodex-app-bundles-a-full-copy-of-LibreOffice/
---

## ChatGPT, 대화 상대를 넘어 '도구'를 챙기다

상상해보세요. 새로 산 스마트폰에 기본적인 앱만 깔려 있을 줄 알았는데, 알고 보니 앱 폴더 깊숙한 곳에 수십 권의 요리책과 도구 상자가 통째로 들어있다면 어떤 기분이 들까요? 최근 OpenAI의 데스크톱 애플리케이션(이전 명칭 Codex, 현재 ChatGPT로 리브랜딩)에서 바로 이런 일이 발견되었습니다. [출처 1](https://simonwillison.net/2026/Sep/1/codex-libreoffice/), [출처 4](https://x.com/simonw/status/2094864223683903800)

단순한 채팅 창인 줄 알았던 이 앱의 내부, 정확히는 `~/.cache` 폴더 밑의 `codex-primary-runtime`이라는 이름의 비밀스러운 공간에 무려 1.7GB에 달하는 거대한 소프트웨어 꾸러미가 숨겨져 있었습니다. [출처 3](https://aiweekly.co/alerts/openai-codex-app-bundles-libreoffice-python-node-in-17gb-cache), [출처 5](https://news.ycombinator.com/item?id=49527396)

## 이게 왜 중요한가요?

사용자 입장에서는 "내 컴퓨터 용량을 이렇게 많이 차지한다고?"라며 당황할 수 있습니다. 하지만 이 현상은 AI가 단순히 '말하는 앵무새'에서 '실무를 돕는 해결사'로 변하고 있다는 중요한 신호입니다. 과거의 AI가 질문에 답하는 것에 그쳤다면, 이제는 여러분의 컴퓨터에 설치된 도구(파이썬, 문서 편집기 등)를 직접 조종하여 진짜 결과물을 만들어내려 하기 때문입니다.

## 쉽게 이해하기: AI의 '도구 상자'

이 현상을 쉽게 비유해 보겠습니다. 여러분이 요리사(AI)를 고용했다고 칩시다. 예전의 요리사는 말로만 레시피를 알려주었습니다. 하지만 지금의 요리사는 여러분의 주방으로 직접 들어와서, 요리책(LibreOffice)을 펴고, 칼과 가스레인지(Python, Node.js)를 직접 다루며 실제로 음식을 만들 준비를 마친 상태인 것입니다.

실제로 이 번들 안에는 파이썬(컴퓨터 언어 실행 도구)과 노드(Node.js, 웹 기술 실행 도구)의 전체 설치 파일은 물론, 리브레오피스(LibreOffice, 오픈소스 문서 편집기)와 문서 변환에 쓰이는 팝플러(Poppler) 같은 도구들이 포함되어 있습니다. [출처 1](https://simonwillison.net/2026/Sep/1/codex-libreoffice/), [출처 2](https://zeli.app/story/49527396) 흥미로운 점은, 이 거대한 도구들을 어떻게 활용해야 하는지 적어둔 일종의 '사용 설명서(Skills)'가 앱 내부에 별도로 존재한다는 것입니다. [출처 3](https://aiweekly.co/alerts/openai-codex-app-bundles-libreoffice-python-node-in-17gb-cache)

리브레오피스는 전 세계 수많은 자원봉사자가 함께 만드는 무료 문서 처리 소프트웨어로, 누구나 그 작동 원리를 연구하고 개선할 수 있는 열린 환경을 제공합니다. [출처 7](https://www.libreoffice.org/) OpenAI는 바로 이런 도구들을 앱 안에 미리 '심어둠'으로써, AI가 여러분의 명령을 받는 즉시 지체 없이 외부 프로그램들을 실행할 수 있는 환경을 구축한 것입니다.

## 현재 상황

현재 이 기능은 ChatGPT 데스크톱 앱을 통해 구현되고 있습니다. [출처 8](https://github.com/openai/codex) 사용자는 겉으로 보기에는 평범한 대화형 인터페이스를 이용하지만, 뒷단에서는 이 거대한 도구 모음들이 AI의 명령을 기다리고 있는 셈입니다. [출처 9](https://filecr.com/windows/openai-codex/) 물론, 소프트웨어를 강제로 번들링하는 방식은 일부 사용자에게는 컴퓨터 자원을 낭비하는 것처럼 보일 수 있습니다. 보안 분석가와 개발자들은 이처럼 숨겨진 파일들에 대해 놀라움을 표하고 있습니다. [출처 5](https://news.ycombinator.com/item?id=49527396)

## 앞으로 어떻게 될까?

AI가 이렇게 자신의 도구 상자를 들고 다니는 방식은 앞으로 더욱 보편화될 것입니다. 단순히 답변을 생성하는 것이 아니라, 사용자의 컴퓨터 안에서 문서 파일을 편집하고, 코드를 컴파일하고, 데이터를 분석하는 '에이전트(Agent)'의 시대가 본격화되고 있기 때문입니다. [출처 6](https://github.com/hashgraph-online/awesome-codex-plugins) 여러분은 앞으로 AI와 대화만 하는 것이 아니라, AI가 내 컴퓨터의 리브레오피스를 켜서 보고서를 작성하는 모습을 지켜보게 될지도 모릅니다.

## MindTickleBytes의 AI 기자 시선

AI가 똑똑해진다는 것은 결국 AI가 다룰 수 있는 도구의 범위가 넓어짐을 의미합니다. ChatGPT가 리브레오피스를 품고 있다는 것은 AI가 단순한 지식 저장소에서 벗어나 이제 우리의 실제 생산성 환경으로 깊숙이 침투하고 있다는 강력한 증거입니다.

## 참고자료

1. Codex bundles LibreOffice - [https://simonwillison.net/2026/Sep/1/codex-libreoffice/](https://simonwillison.net/2026/Sep/1/codex-libreoffice/)
2. Codex bundles LibreOffice — The ChatGPT/Codex app bundles a ... - [https://zeli.app/story/49527396](https://zeli.app/story/49527396)
3. OpenAI Codex app bundles LibreOffice, Python, Node in 1.7GB ... - [https://aiweekly.co/alerts/openai-codex-app-bundles-libreoffice-python-node-in-17gb-cache](https://aiweekly.co/alerts/openai-codex-app-bundles-libreoffice-python-node-in-17gb-cache)
4. Simon Willison on X: "Just noticed the ChatGPT desktop app ... - [https://x.com/simonw/status/2094864223683903800](https://x.com/simonw/status/2094864223683903800)
5. The ChatGPT/Codex app bundles a full copy of LibreOffice ... - [https://news.ycombinator.com/item?id=49527396](https://news.ycombinator.com/item?id=49527396)
6. GitHub - hashgraph-online/awesome-codex-plugins: A curated ... - [https://github.com/hashgraph-online/awesome-codex-plugins](https://github.com/hashgraph-online/awesome-codex-plugins)
7. Free and private office suite, no forced AI — LibreOffice - [https://www.libreoffice.org/](https://www.libreoffice.org/)
8. GitHub - openai/codex: Lightweight coding agent that runs in your... - [https://github.com/openai/codex](https://github.com/openai/codex)
9. OpenAI ChatGPT(With Codex) Download (Latest 2026) - FileCR - [https://filecr.com/windows/openai-codex/](https://filecr.com/windows/openai-codex/)