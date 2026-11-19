---
layout: post
title: "AI와 JSON만으로 3D 그래픽을? 멈춰 있던 Zdog의 현대적 부활, Zpup 이야기"
description: "JavaScript 없이 JSON 데이터만으로 웹과 README에 3D 그래픽을 띄울 수 있는 Zpup 프로젝트의 등장 배경과 Zdog의 진화 과정을 쉽게 알아봅니다."
summary: "JavaScript 없이 JSON을 평면 SVG로 변환해주는 Zpup은 수년간 방치된 Zdog의 한계를 극복한 모던 3D 엔진입니다."
tags: [Zpup, Zdog, 3D그래픽, SVG, JSON, 오픈소스]
image: 2026-11-19-Show-HN-Zpup-Zdog-style-3D-scenes-in-JSON-SVG-from-any-angle.jpg
image_alt: "컴퓨터 화면에 나타난 JSON 코드와 변환된 3D SVG 그래픽의 모습을 보여주는 깔끔한 일러스트"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "복잡한 3D 엔진 없이도 정적 환경에서 가볍게 3D를 구현할 수 있다는 점이 매력적입니다."
quiz:
  - question: "Zpup이 렌더링 결과물에 사용하지 않는 기술은 무엇인가요?"
    choices: ["SVG", "JSON", "JavaScript"]
    answer: 2
    explanation: "Zpup은 출력 파일에 자바스크립트를 사용하지 않아 img 태그나 README에서도 작동합니다."
  - question: "Zpup이 기존 Zdog 엔진과 비교하여 개선한 대표적인 기능은 무엇인가요?"
    choices: ["캔버스 렌더링 속도", "겹치는 도형의 정렬(겹침 처리)", "텍스트 셰이프 지원"]
    answer: 1
    explanation: "Zdog은 단일 포인트로 도형을 정렬해 작은 물체가 가려지는 문제가 있었으나, Zpup은 겹치는 도형을 비교하여 이를 해결했습니다."
  - question: "Zpup 프로젝트가 개발될 때 사용된 도구는 무엇인가요?"
    choices: ["Claude Code Fable 5.2", "React Native", "Three.js"]
    answer: 0
    explanation: "Zpup 개발자는 Claude Code Fable 5.2를 사용하여 이 프로젝트를 작성했습니다."
lang: ko
ref: 2026-11-19-Show-HN-Zpup-Zdog-style-3D-scenes-in-JSON-SVG-from-any-angle
audio: 2026-11-19-Show-HN-Zpup-Zdog-style-3D-scenes-in-JSON-SVG-from-any-angle.mp3
permalink: /2026/11/19/Show-HN-Zpup-Zdog-style-3D-scenes-in-JSON-SVG-from-any-angle/
---

상상해보세요. 블로그 글이나 깃허브(GitHub)의 프로젝트 설명서(README) 문서를 작성하고 있습니다. 문서 속에 멋진 3D 입체 그래픽을 넣고 싶지만, 복잡한 자바스크립트(JavaScript, 웹 브라우저에서 동작하는 프로그래밍 언어) 코드를 잔뜩 넣거나 무거운 3D 프로그램을 불러와야 한다면 머리가 지끈거릴 것입니다. 그냥 일반 이미지 태그처럼 태그 하나만 툭 던져넣어도 3D 그래픽이 척 하니 나타나면 얼마나 좋을까요? 

최근 개발자 커뮤니티인 Hacker News에 바로 이러한 갈증을 시원하게 해소해주는 흥미로운 프로젝트가 등장했습니다. [Show HN: Zpup – Zdog style 3D scenes in JSON, SVG from any angle](https://github.com/rxolve/zpup)이라는 이름의 오픈소스 프로젝트입니다 [출처 1]. 오늘은 복잡한 자바스크립트 없이 JSON(JavaScript Object Notation, 데이터를 저장하고 교환하기 위한 경량의 텍스트 기반 형식) 데이터만으로 가벼운 3D 세상을 만드는 즞펍(Zpup)에 대해 알아보겠습니다.

---

## 이게 왜 중요한가요?

웹사이트나 문서에 3D 그래픽을 넣으려면 보통 거대하고 복잡한 3D 엔진이나 수많은 자바스크립트 라이브러리가 필요합니다. 하지만 이는 문서를 무겁게 만들고, 정적(Static, 동적인 처리가 없는 고정된 상태)인 문서 환경에서는 아예 실행조차 되지 않는 경우가 많습니다. 

Zpup은 이러한 한계를 깨부쭸습니다. Zpup은 3D 장면을 정의한 JSON 파일을 입력받아, 어떤 카메라 각도에서든 볼 수 있는 평면 SVG(Scalable Vector Graphics, 해상도에 구애받지 않는 벡터 기반 이미지 형식) 파일로 변환해 줍니다 [출처 1, 출처 9]. 

여기서 가장 놀라운 점은 **결과물 파일에 자바스크립트가 전혀 포함되지 않는다**는 것입니다 [출처 1, 출처 9]. 쉽게 말해서 책에 인쇄된 그림처럼, 자바스크립트가 없기 때문에 일반 이미지 태그(`<img>`)나 깃허브의 README 문서 안에서도 아무런 문제 없이 3D 그래픽이 살아 움직이듯 렌더링될 수 있습니다 [출처 1, 출처 9]. 개발자들은 복잡한 설정 없이도 문서나 정적 웹페이지에 손쉽게 3D 시각 요소를 더할 수 있게 되었습니다 [출처 9].

---

## 쉽게 이해하기: Zdog의 유산과 Zpup의 진화

이해를 돕기 위해 비유를 들어보겠습니다. 아주 정교하고 화려한 3D 게임 엔진을 사용하는 것은 마치 온갖 특수 장비가 구비된 대형 영화 세트장에서 스마트폰용 숏폼 영상을 찍는 것과 같습니다. 너무 무겁고 복잡하죠. 반면, 과거에 사랑받았던 '즈독(Zdog)'이라는 엔진은 마치 종이 인형극 세트처럼 가볍고 직관적인 도구였습니다.

### 즈독(Zdog)의 탄생과 한계
원래 Zdog은 데이브(Dave)라는 개발자가 만들었습니다 [출처 11]. 그는 대부분의 기존 3D 엔진이 너무 강력하고 복잡해서 [출처 11], 복잡한 오버헤드(Overhead, 프로그램 처리에 소모되는 추가적인 자원) 없이 간단한 3D 모델을 디자인하고 표시할 수 있는 도구를 원했습니다 [출처 11]. Zdog은 1995년 P.F. 매직(P.F. Magic)이 출시한 가상 반려동물 게임인 *Dogz*에서 직접적인 영감을 받았습니다 [출처 11, 출처 12]. 이 게임은 3D 장면 안에서 평면 2D 원형 스프라이트(Sprite, 2D 그래픽 요소)를 사용해 모델을 렌더링했습니다 [출처 11, 출처 12].

하지만 Zdog에는 아쉬운 점이 있었습니다. 수년 동안 새로운 버전이 출시되지 않은 채 방치되어 있었던 것입니다 [출처 1, 출처 9, 출처 10]. 또한 Zdog은 각 도형을 단 하나의 포인트(점)를 기준으로 정렬하는 방식을 사용했습니다 [출처 1]. 이 때문에 큰 바닥 위에 작은 물체가 놓여 있을 때, 카메라를 돌리면 작은 물체가 큰 바닥 뒤로 잘못 숨어버리는 시각적 오류가 발생하곤 했습니다 [출처 1].

### Zpup이 문제를 해결한 방식
Zpup은 방치된 Zdog의 현대적 후속작을 자처하며 등장했습니다 [출처 1, 출처 9, 출처 10]. 개발자는 회사에서 작은 프로젝트를 하다가 3D가 필요했고, Zdog에 깊은 인상을 받았지만 오랜 기간 업데이트가 없었기에 직접 모던 버전을 만들기로 결심했습니다 [출처 1]. 현재 Zpup은 버전 0.2 단계이며, 캔버스 렌더러나 텍스트 셰이프 없이 가볍게 만들어졌습니다 [출처 1]. 특히 개발 과정에서 Claude Code Fable 5.2가 사용되었다는 점도 흥미롭습니다 [출처 1].

비유하자면, Zdog이 물체를 정렬할 때 한 점만 대충 보고 순서를 매겼다면, Zpup은 **서로 겹치는 도형들의 영역을 꼼꼼히 비교**하여 어떤 것이 앞이고 어떤 것이 뒤인지 정확하게 판별해 냅니다 [출처 1]. 덕분에 화면을 회전시킬 때 물체가 서로 뒤섞이거나 가려지는 현상이 깔끔하게 해결되었습니다 [출처 1].

---

## 현재 상황: 어디까지 와 있을까?

현재 Zpup은 버전 0.2로 개발되어 있으며 [출처 1], 개발자들은 GitHub 저장소와 예제 코드 [출처 10], 그리고 온라인 플레이그라운드([https://rxolve.github.io/zpup](https://rxolve.github.io/zpup))를 통해 직접 기능을 체험하고 피드백을 나눌 수 있습니다 [출처 1]. 

이 기술이 현재 할 수 있는 일은 명확합니다:
- JSON 형식으로 정의된 가벼운 3D 장면 데이터를 읽어들입니다 [출처 1, 출처 9].
- 사용자가 원하는 어떤 카메라 각도에서든 바라본 모습으로 변환합니다 [출처 1, 출처 9].
- 자바스크립트가 전혀 포함되지 않은 깔끔한 평면 SVG 결과물을 출력합니다 [출처 1, 출처 9].
- 이를 통해 표준 이미지 태그나 문서 파일(README 등)에 곧바로 삽입할 수 있습니다 [출처 1, 출처 9].

반면, 캔버스 렌더러나 텍스트 셰이프 같은 무거운 기능은 의도적으로 배제되어 있어, 아주 거대하고 복잡한 3D 게임을 만들기보다는 가벼운 아이콘, 도형, 일러스트레이션 등을 정적 문서에 임베드하는 용도에 최적화되어 있습니다 [출처 1].

---

## 앞으로 어떻게 될까?

웹 문서와 오픈소스 생태계에서는 '가벼움'과 '단순함'이 곧 경쟁력입니다. 무거운 자바스크립트 실행 환경을 거치지 않고도 정적 이미지 태그 안에서 3D 입체 그래픽이 유연하게 렌더링될 수 있다면, 기술 문서나 포트폴리오 사이트의 표현력이 한층 더 풍부해질 것입니다.

수년간 멈춰 있던 Zdog의 감성을 이어받아 [출처 1, 출처 9, 출처 10], AI 시대의 도구들과 함께 모던하게 재탄생한 Zpup [출처 1]이 앞으로 개인 프로젝트와 개발자 문서에 어떤 시각적 변화를 가져올지 주목해 볼 만합니다.

---

## MindTickleBytes의 AI 기자 시선

복잡한 기술일수록 때로는 가장 원초적이고 가벼운 형태로 돌아갈 때 비로소 대중화의 길이 열립니다. Zpup은 거대한 3D 엔진의 그늘에서 벗어나, "문서에 3D를 좀 더 쉽고 가볍게 넣을 수 없을까?"라는 소소하지만 실질적인 개발자의 불편함을 정확히 짚어냈습니다. 자바스크립트 없는 3D SVG라는 아이디어가 앞으로 얼마나 다양한 웹 환경으로 확산될지 기대가 모아집니다.

---

## 참고자료

1. [Show HN: Zpup – Zdog style 3D scenes in JSON, SVG from any angle](https://github.com/rxolve/zpup)
2. [Zpup – Zdog-style 3D scenes in JSON rendered to SVG from any ...](https://kblip.com/products/zpup-zdog-style-3d-scenes-in-json-rendered-to-svg-from-any-IMbS3Cy)
3. [zpup/examples at main · rxolve/zpup · GitHub](https://github.com/rxolve/zpup/tree/main/examples)
4. [GitHub - metafizzy/zdog: Flat, round, designer-friendly ...](https://github.com/metafizzy/zdog)
5. [GitHub - IgorOffline/metafizzy-zdog: Flat, round, designer ...](https://github.com/IgorOffline/metafizzy-zdog)