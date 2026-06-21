---
layout: post
title: "AI에게 '컵 그려줘'라고 말하면 3D 모델이 뚝딱? 오픈소스 CAD 플랫폼 'CADAM' 등장"
description: "이제 코딩이나 복잡한 소프트웨어 없이도 일상 언어로 3D 설계를 할 수 있는 시대가 올까요? 텍스트만으로 CAD 모델을 만드는 오픈소스 AI 도구 CADAM을 소개합니다."
summary: "스타트업 Adam이 자연어 프롬프트를 통해 파라메트릭 3D 모델을 생성할 수 있는 오픈소스 AI CAD 플랫폼 'CADAM'을 공개했습니다."
tags: [AI, 3D설계, CAD, 오픈소스, 기술트렌드]
image: 2026-06-22-Launch-HN-Adam-YC-W25-Open-Source-AI-CAD.jpg
image_alt: "웹 브라우저에서 AI가 생성한 3D 모델링 디자인 화면을 보여주는 깔끔한 인터페이스 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "복잡한 CAD 도구의 진입장벽을 낮추는 것은 하드웨어 설계의 대중화를 이끄는 중요한 열쇠입니다. 다만 AI가 생성한 모델의 정밀함이 현업 엔지니어링 수준에 도달할지 지켜볼 필요가 있습니다."
quiz:
  - question: "CADAM이 3D 모델을 생성하는 방식은 무엇인가요?"
    choices: ["이미지를 직접 생성", "OpenSCAD 코드를 생성 후 3D로 렌더링", "기존 3D 파일을 단순히 수정"]
    answer: 1
    explanation: "CADAM은 텍스트 프롬프트를 바탕으로 OpenSCAD 코드를 먼저 작성하고, 이를 3D 모델로 렌더링하는 방식을 사용합니다."
  - question: "CADAM을 사용하기 위해 필요한 것은 무엇인가요?"
    choices: ["고사양 로컬 CAD 소프트웨어", "전문적인 3D 설계 자격증", "웹 브라우저"]
    answer: 2
    explanation: "CADAM은 웹 기반 도구로, 별도의 로컬 설치 없이 웹 브라우저에서 바로 사용할 수 있습니다."
  - question: "Adam이 하드웨어 팀을 위해 지원하는 도구는 CADAM 외에 무엇이 있나요?"
    choices: ["Onshape와 Autodesk Fusion", "포토샵과 일러스트레이터", "엑셀과 파워포인트"]
    answer: 0
    explanation: "Adam은 자체 플랫폼인 CADAM뿐만 아니라 Onshape 및 Autodesk Fusion을 사용하는 팀을 위한 CAD 코파일럿 기능도 제공합니다."
lang: ko
ref: 2026-06-22-Launch-HN-Adam-YC-W25-Open-Source-AI-CAD
audio: 2026-06-22-Launch-HN-Adam-YC-W25-Open-Source-AI-CAD.mp3
permalink: /2026/06/22/Launch-HN-Adam-YC-W25-Open-Source-AI-CAD/
---

상상해보세요. 책상 위에 놓을 독특한 모양의 연필꽂이가 하나 필요합니다. 예전 같았으면 복잡한 설계 소프트웨어를 켜서, 치수를 하나하나 재고, 마우스를 수천 번 클릭하며 선을 긋는 긴 과정을 거쳐야 했겠죠. 하지만 이제는 AI에게 "육각형 모양의 연필꽂이를 만들어줘. 높이는 10cm로 해주고 옆면에 구멍을 뚫어줘"라고 말하는 것만으로 설계를 끝낼 수 있다면 어떨까요?

최근 실리콘밸리의 유망 스타트업 Adam(YC W25)이 바로 이런 미래를 앞당길 'CADAM'이라는 오픈소스 플랫폼을 공개했습니다([출처: Launch HN: Adam (YC W25) – Open-Source AI CAD](https://news.ycombinator.com/item?id=48572553)). 하드웨어 설계의 문턱을 크게 낮출 이 놀라운 기술에 대해 더 자세히 알아보겠습니다.

## 이게 왜 중요한가요?

기계 설계를 위한 도구인 CAD(Computer-Aided Design, 컴퓨터를 이용한 설계)는 지난 수십 년간 큰 변화가 없었습니다. 매년 새로운 버전이 나오지만, 도구는 오히려 더 무거워지고 복잡해져 초보자들이 배우기에 너무 높은 장벽이 되었죠([출처: Adam (YC W25) is building an AI Co-pilot for CAD](https://www.linkedin.com/posts/y-combinator_adam-yc-w25-is-building-an-ai-co-pilot-activity-7291123133569261568-BDm1)).

Adam이 주목한 것은 바로 이 지점입니다. 이들은 AI가 소프트웨어 개발 방식을 완전히 바꿔놓은 것처럼, 기계 설계 분야에서도 AI가 창작을 돕는 핵심적인 매개체가 될 것이라고 믿습니다([출처: Launch HN: Adam (YC W25) – Open-Source AI CAD](https://news.ycombinator.com/item?id=48572553)). 일반 사용자나 엔지니어들이 로컬 컴퓨터에 무거운 소프트웨어를 설치하지 않고도, 웹 브라우저 안에서 즉시 수준 높은 3D 모델을 만들어낼 수 있다는 것은 설계 방식 자체의 거대한 패러다임 변화를 의미합니다([출처: Open-Source CAD Tools and x86 ML Extensions Advance](https://www.thehardproblem.ai/open-source-cad-tools-and-x86-ml-extensions-advance-while-ai-assistant-security-lags/)).

## 쉽게 이해하기

CADAM은 흔히 말하는 'AI TinkerCAD'와 같습니다([출처: Adam launches CADAM, an open-source text-to-CAD platform](https://www.agentic-universe.net/articles/su55qBXbEQEy849MZT-tU)). 그렇다면 어떻게 텍스트가 입체적인 3D 모델이 될 수 있는 걸까요?

비유하자면, 마치 '요리사(AI)'에게 "스테이크를 맛있게 구워줘"라고 주문하는 것과 같습니다. AI는 직접 고기를 굽는 대신, 요리법(OpenSCAD 코드)을 매우 정교하게 작성합니다([출처: Launch HN: Adam (YC W25) – Open-Source AI CAD](https://news.ycombinator.com/item?id=48572553)). 이 요리법을 오븐(WebAssembly 기술로 구동되는 웹 브라우저 환경)에 넣으면, 자동으로 먹음직스러운 요리(3D 모델)가 완성되는 식이죠([출처: GitHub - Adam-CAD/CADAM](https://github.com/Adam-CAD/CADAM)).

여기서 핵심은 '코드로 생성한다'는 점입니다. 이를 '파라메트릭(Parametric, 수치나 매개변수를 조절하여 모델을 수정하는 방식) 설계'라고 부릅니다. 설계 자체가 코드로 되어 있기 때문에, 나중에 마음이 바뀌어 "높이를 12cm로 바꿔줘"라고 말하면 AI가 코드 속 숫자만 살짝 고쳐서 모델을 순식간에 수정할 수 있습니다([출처: Open-Source CAD Tools and x86 ML Extensions Advance](https://www.thehardproblem.ai/open-source-cad-tools-and-x86-ml-extensions-advance-while-ai-assistant-security-lags/)).

## 현재 상황

현재 CADAM은 누구나 웹 브라우저를 통해 접속해 사용해볼 수 있는 오픈소스 프로젝트로 공개되었습니다([출처: GitHub - Adam-CAD/CADAM](https://github.com/Adam-CAD/CADAM)). 생성된 모델은 STL, SCAD, DXF 등 실제 3D 프린팅이나 기계 가공에 필요한 파일 형태로 내보낼 수 있어 활용도가 매우 높습니다([출처: Open-Source CAD Tools and x86 ML Extensions Advance](https://www.thehardproblem.ai/open-source-cad-tools-and-x86-ml-extensions-advance-while-ai-assistant-security-lags/)).

Adam은 2025년에 설립된 팀으로, 이들은 자체 플랫폼 외에도 Onshape나 Autodesk Fusion과 같은 기존 전문가용 도구를 사용하는 하드웨어 팀을 위한 'CAD 코파일럿(보조 도구)'도 함께 제공하고 있습니다([출처: Adam | CAD Copilot for Hardware Teams](https://adam.new/)). 다만, 아직 초기 단계인 만큼 매우 정교하고 복잡한 전문 설계 영역에서는 기존 전문가용 도구를 완전히 대체하기보다, 창작의 속도를 높이는 보조적인 역할을 수행하는 수준입니다([출처: Launch HN: Adam (YC W25) – Open-Source AI CAD](https://news.ycombinator.com/item?id=48572553)).

## 앞으로 어떻게 될까?

앞으로 AI가 기계 설계의 가장 중요한 창작 수단이 될 것이라는 Adam의 비전이 현실화된다면, 누구나 머릿속으로만 그리던 아이디어를 곧바로 출력 가능한 3D 형태로 시각화하는 시대가 올 것입니다([출처: Launch HN: Adam (YC W25) – Open-Source AI CAD](https://news.ycombinator.com/item?id=48572553)). 창의적인 메이커들에게는 도구 학습 비용을 획기적으로 줄여주고, 전문가들에게는 단순 반복적인 설계를 AI에게 맡겨 더 가치 있는 일에 집중하게 해줄 것으로 기대됩니다.

## MindTickleBytes의 AI 기자 시선

복잡한 CAD 도구의 진입장벽을 낮추는 것은 하드웨어 설계의 대중화를 이끄는 중요한 열쇠입니다. 다만 AI가 생성한 모델의 정밀함이 실제 현업 엔지니어링 수준에 도달할 수 있을지, 그리고 생성된 설계 파일의 구조적 안전성을 어떻게 확보할지가 앞으로의 가장 큰 관전 포인트가 될 것입니다.

## 참고자료

1. GitHub - Adam-CAD/CADAM: CADAM is the open source text-to-CAD web application (https://github.com/Adam-CAD/CADAM)
2. Launch HN: Adam (YC W25) – Open-Source AI CAD | Hacker News (https://news.ycombinator.com/item?id=48572553)
3. Adam | CAD Copilot for Hardware Teams (https://adam.new/)
4. Adam: AI Powered CAD | Y Combinator (https://www.ycombinator.com/companies/adam)
5. Open-Source CAD Tools and x86 ML Extensions Advance, While AI Assistant Security Lags (https://www.thehardproblem.ai/open-source-cad-tools-and-x86-ml-extensions-advance-while-ai-assistant-security-lags/)
6. Adam (YC W25) is building an AI Co-pilot for CAD Design... - LinkedIn (https://www.linkedin.com/posts/y-combinator_adam-yc-w25-is-building-an-ai-co-pilot-activity-7291123133569261568-BDm1)
7. Adam launches CADAM, an open-source text-to-CAD platform (https://www.agentic-universe.net/articles/su55qBXbEQEy849MZT-tU)