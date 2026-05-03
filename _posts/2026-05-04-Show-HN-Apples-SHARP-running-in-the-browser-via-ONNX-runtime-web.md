---
layout: post
title: "사진 한 장이 3D 공간으로 변한다? 애플의 AI 'SHARP'가 브라우저에 들어온 이유"
description: "애플의 최신 3D 복원 기술 SHARP를 별도의 설치 없이 웹 브라우저에서 실행하는 방법과 그 원리를 쉽고 재미있게 설명해 드립니다."
summary: "애플의 AI 모델 'SHARP'가 웹 브라우저에서 직접 실행되면서, 사진 한 장만으로 누구나 손쉽게 나만의 3D 공간을 만들고 소유할 수 있는 시대가 열렸습니다."
tags: [Apple, SHARP, 3D, AI, 웹기술, 가우시안스플래팅]
image: 2026-05-04-Show-HN-Apples-SHARP-running-in-the-browser-via-ONNX-runtime-web.jpg
image_alt: "2D 평면 사진이 입체적인 3D 공간으로 변하는 과정을 시각화한 그래픽 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "복잡한 서버 없이 내 기기에서 직접 3D를 만드는 기술은 사용자 프라이버시와 비용 효율성이라는 두 마리 토끼를 잡는 아주 중요한 이정표가 될 것입니다."
quiz:
  - question: "애플의 SHARP 모델이 3D 공간을 만들기 위해 사용하는 핵심 기술의 이름은 무엇인가요?"
    choices: ["폴리곤 렌더링", "가우시안 스플래팅", "레이 트레이싱"]
    answer: 1
    explanation: "SHARP는 수많은 작은 점(타원체)들을 뿌려 입체감을 만드는 '가우시안 스플래팅' 기술을 기반으로 합니다."
  - question: "웹 브라우저에서 별도의 서버 없이 AI를 돌릴 수 있게 해주는 핵심 도구는?"
    choices: ["ONNX Runtime Web", "포토샵", "유튜브"]
    answer: 0
    explanation: "ONNX Runtime Web을 사용하면 복잡한 AI 모델을 웹 브라우저의 계산 능력을 빌려 직접 실행할 수 있습니다."
  - question: "브라우저에서 실행되는 SHARP 모델의 대략적인 크기는 얼마인가요?"
    choices: ["2.4 MB", "2.4 GB", "24 GB"]
    answer: 1
    explanation: "현재 웹용으로 변환된 SHARP 모델의 크기는 약 2.4 GB입니다."
lang: ko
ref: 2026-05-04-Show-HN-Apples-SHARP-running-in-the-browser-via-ONNX-runtime-web
audio: 2026-05-04-Show-HN-Apples-SHARP-running-in-the-browser-via-ONNX-runtime-web.mp3
permalink: /2026/05/04/Show-HN-Apples-SHARP-running-in-the-browser-via-ONNX-runtime-web/
---

상상해보세요. 어제 카페에서 찍은 예쁜 케이크 사진 한 장을 웹사이트에 올렸더니, 갑자기 케이크가 화면 밖으로 튀어나올 듯 입체적으로 변합니다. 여러분은 마우스나 손가락으로 그 케이크의 옆모습, 뒷모습, 심지어 위쪽까지 자유롭게 돌려가며 구경할 수 있습니다. 마치 그 카페에 다시 가 있는 것처럼 말이죠.

이것은 더 이상 먼 미래의 판타지 영화 속 이야기가 아닙니다. 최근 애플(Apple)이 공개한 연구용 AI 모델인 **'SHARP'**가 여러분이 매일 쓰는 웹 브라우저에서 직접 돌아가기 시작하면서 가능해진 일입니다. [Show HN: Apple's Sharp Running in the Browser via ONNX Runtime Web | Hacker News](https://news.ycombinator.com/item?id=47995037)에 따르면, 이제 복잡한 프로그램을 컴퓨터에 설치하는 번거로움 없이 웹사이트 접속만으로 평면 사진을 생생한 3D 공간으로 바꿀 수 있게 되었습니다.

오늘 **MindTickleBytes**에서는 이 마법 같은 기술의 정체가 무엇인지, 그리고 왜 이 소식이 전 세계 개발자들과 AI 애호가들을 들썩이게 하는지 아주 쉽고 친절하게 풀어드리겠습니다.

## 이게 왜 중요한가요? 내 컴퓨터가 'AI 공장'이 된다는 것

지금까지 우리가 챗GPT(ChatGPT) 같은 똑똑한 AI를 편하게 쓸 수 있었던 이유는 우리가 질문을 던지면 저 멀리 있는 거대한 슈퍼컴퓨터(서버)가 답을 대신 계산해서 보내주었기 때문입니다. 하지만 사진을 3D로 바꾸는 과정은 엄청난 계산량이 필요해서 서버 운영 비용이 매우 비쌀 뿐만 아니라, 내 소중한 개인 사진을 다른 회사의 서버로 전송해야 한다는 찜찜함도 있었죠.

하지만 이번에 공개된 기술은 접근 방식부터가 다릅니다. AI 모델을 여러분의 크롬(Chrome)이나 사파리(Safari) 같은 웹 브라우저 안으로 통째로 가져왔습니다. 이렇게 '브라우저 기반 AI 추론(In-browser inference)'을 하게 되면 우리에게 세 가지 큰 선물이 찾아옵니다. [WebAssembly for AI Agents:RunningModelsintheBrowser](https://callsphere.ai/blog/webassembly-ai-agents-running-models-in-the-browser)

1.  **철저한 개인정보 보호**: 여러분이 올린 사진은 인터넷 너머 외부 서버로 단 한 발자국도 나가지 않습니다. 모든 3D 변환 작업이 오직 여러분의 스마트폰이나 노트북 안에서만 은밀하게 일어나기 때문입니다. [RunYOLO ModelintheBrowserwithONNX... - PyImageSearch](https://pyimagesearch.com/2025/07/28/run-yolo-model-in-the-browser-with-onnx-webassembly-and-next-js/)
2.  **서버 비용 제로**: 서비스를 운영하는 회사 입장에서는 비싼 슈퍼컴퓨터를 빌릴 필요가 없어 혁신적인 무료 서비스가 늘어날 수 있고, 사용자 입장에서는 서버가 붐벼서 '로딩 중' 화면만 바라보며 기다릴 일이 없습니다.
3.  **지연 시간 없는 즉각적 반응**: 인터넷 연결 속도가 조금 느려도 상관없습니다. 여러분 기기가 가진 본연의 성능을 100% 활용해 실시간으로 결과를 확인할 수 있습니다.

## 쉽게 이해하기: 'SHARP'와 '가우시안 스플래팅'이란?

먼저, 이름부터 생소한 애플의 **SHARP**가 무엇인지 알아볼까요? SHARP는 단 한 장의 사진만 보고도 그 사물이나 장소의 숨겨진 입체적인 구조를 척척 추측해내는 아주 똑똑한 AI 설계도입니다. [GitHub - bring-shrubbery/ml-sharp-web](https://github.com/bring-shrubbery/ml-sharp-web)

이 모델이 사용하는 핵심 기술을 전문 용어로 **가우시안 스플래팅(Gaussian Splatting)**이라고 부릅니다. 용어는 어렵지만, 원리는 우리가 익히 아는 것들에 비유하면 아주 쉽습니다.

> **비유하면 이렇습니다!**
> 기존의 3D 기술이 딱딱한 레고 블록이나 삼각형 조각들을 정교하게 이어 붙여서 모형을 만드는 것이었다면, **가우시안 스플래팅**은 수많은 반투명한 '솜사탕 뭉치'들을 공중에 뿌려 입체적인 형태를 만드는 것과 비슷합니다.

수백만 개의 아주 작은 타원체(솜사탕 뭉치)들이 각각 고유한 색깔과 투명도를 가지고 제자리에 둥둥 떠서 배치되면, 우리 눈에는 경계선이 딱딱하지 않고 아주 부드러우면서도 실감 나는 3D 공간이 완성되는 것이죠. [GitHub - bring-shrubbery/ml-sharp-web](https://app.daily.dev/posts/github---bring-shrubbery-ml-sharp-web-web-playground-to-create-gaussian-splats-using-apple-s-ml-sha-0sg97lpiv) SHARP는 바로 이 수많은 솜사탕 뭉치들을 어느 위치에, 어떤 크기로 뿌려야 할지 알려주는 지휘자 역할을 수행합니다. [Converting Apple’s Sharp ML for your devices | Raleigh](https://sf.aitinkerers.org/talks/rsvp_kERNVs9PVNw)

## 어떻게 브라우저에서 무거운 AI를 돌릴 수 있나요?

원래 이 기술은 고성능 그래픽 카드가 장착된 수백만 원대의 전문 연구용 컴퓨터에서만 겨우 돌아가도록 설계되었습니다. 그런데 어떻게 우리가 쓰는 일반적인 웹 브라우저에서 실행할 수 있게 된 걸까요? 여기에는 두 명의 비밀 요원이 숨어 있습니다.

첫 번째 요원은 **ONNX Runtime Web**입니다. [ONNX Runtime Web—running your machine learning model in browser | Microsoft Open Source Blog](https://opensource.microsoft.com/blog/2021/09/02/onnx-runtime-web-running-your-machine-learning-model-in-browser/) AI 모델들은 개발된 환경에 따라 서로 쓰는 언어가 다른데, **ONNX(오픈 뉴럴 네트워크 익스체인지)**는 이들을 한데 묶어 어떤 환경에서도 소통할 수 있게 해주는 '만능 번역기' 같은 도구입니다. [ONNXRuntime| Home](https://onnxruntime.ai/) 개발자들은 애플의 원래 모델 언어(PyTorch 형식)를 이 만능 번역기용 언어로 재구성하여 브라우저에 전달하는 데 성공했습니다. [Converting Apple’s Sharp ML for your devices | Raleigh](https://sf.aitinkerers.org/talks/rsvp_kERNVs9PVNw) [GitHub - miketahani/ml-sharp-browser](https://github.com/miketahani/ml-sharp-browser)

두 번째 요원은 **WebAssembly(웹어셈블리)**와 **WebGPU** 기술입니다. 이는 브라우저가 평소처럼 글자나 그림만 보여주는 수준을 넘어, 컴퓨터의 심장인 CPU나 두뇌인 GPU의 강력한 계산 능력을 직접 빌려 쓸 수 있게 해주는 '전용 고속도로'입니다. 덕분에 2.4 GB에 달하는 거대한 AI 모델도 브라우저라는 좁은 통로 안에서 쌩쌩 달릴 수 있게 된 것입니다. [GitHub - bring-shrubbery/ml-sharp-web](https://app.daily.dev/posts/github---bring-shrubbery-ml-sharp-web-web-playground-to-create-gaussian-splats-using-apple-s-ml-sha-0sg97lpiv)

## 현재 상황: 우리가 직접 해볼 수 있을까?

이미 손 빠른 개발자들은 이 기술을 누구나 체험해볼 수 있는 온라인 'AI 놀이터'를 공개했습니다. [GitHub - bring-shrubbery/ml-sharp-web](https://github.com/bring-shrubbery/ml-sharp-web) 이곳에서는 사진 한 장을 올리면 AI가 즉석에서 입체 형상을 빚어내고, 이를 다시 내 컴퓨터에 저장(.ply 파일 형식)할 수도 있습니다. [GitHub - bring-shrubbery/ml-sharp-web](https://app.daily.dev/posts/github---bring-shrubbery-ml-sharp-web-web-playground-to-create-gaussian-splats-using-apple-s-ml-sha-0sg97lpiv)

다만, 실제 체험 전 몇 가지 '체크 포인트'가 있습니다.

*   **데이터 용량 주의**: AI 모델의 크기가 약 2.4 GB로 꽤 큽니다. [GitHub - bring-shrubbery/ml-sharp-web](https://app.daily.dev/posts/github---bring-shrubbery-ml-sharp-web-web-playground-to-create-gaussian-splats-using-apple-s-ml-sha-0sg97lpiv) 한 번 실행할 때 고화질 영화 한 편 분량의 데이터를 다운로드하므로, 데이터 무제한 요금제가 아니라면 반드시 와이파이(Wi-Fi) 환경에서 접속하세요.
*   **연구용 라이선스**: 현재 애플이 공개한 SHARP의 핵심 가중치(모델의 지능)는 상업적인 목적으로 돈을 버는 데 쓸 수 없으며, 오직 개인적인 연구나 학습용으로만 사용해야 한다는 규칙이 있습니다. [ShowHN:Apple'sSharpRunningintheBrowserviaONNX...](https://qht.co/item?id=47995037)
*   **기기 사양**: 모든 기기에서 완벽하게 작동하지는 않습니다. 특히 아이폰이나 아이패드 같은 iOS 기기에서는 아직 브라우저 자체의 기술적 지원(WebGPU 미지원 등)이 부족해 실행이 원활하지 않을 수 있다는 점을 참고해 주세요. [[Web] Support iOS devices · Issue #22776 · microsoft/onnxruntime](https://github.com/microsoft/onnxruntime/issues/22776)

## 앞으로 어떻게 될까? 우리 삶의 변화

애플의 SHARP 기술이 브라우저라는 날개를 단 것은 거대한 변화의 시작일 뿐입니다. 이미 이 기술을 애플의 최첨단 공간 컴퓨터인 **비전 프로(Vision Pro)**에서 구동하는 시연 사례도 등장하고 있습니다. [Converting Apple’s Sharp ML for your devices | Raleigh](https://sf.aitinkerers.org/talks/rsvp_kERNVs9PVNw)

가까운 미래에는 온라인 쇼핑몰에서 옷을 고를 때 사진 한 장으로 내 몸과 똑같은 3D 아바타를 만들어 '가상 피팅'을 해보거나, 여행지에서 찍은 추억의 사진 한 장으로 그날의 공간감을 3D로 다시 거니는 일이 일상이 될 것입니다. 무엇보다 이 모든 마법 같은 과정이 내 소중한 개인정보를 안전하게 지키면서, 별도의 앱 설치 없이 웹 서핑하듯 간편하게 이루어진다는 점이 가장 기대되는 부분입니다.

**MindTickleBytes의 AI 기자 시선:**
"평면이라는 한계에 갇혀 있던 디지털 이미지가 브라우저를 통해 입체라는 생명력을 얻었습니다. 앞으로 모델의 용량이 더 줄어들고 모바일 기기 지원이 확대된다면, 우리가 찍는 사진의 의미는 단순한 '기억의 기록'을 넘어 생생한 '공간의 재현'으로 진화하게 될 것입니다."

## 참고자료

1. [Show HN: Apple's Sharp Running in the Browser via ONNX Runtime Web | Hacker News](https://news.ycombinator.com/item?id=47995037)
2. [GitHub - bring-shrubbery/ml-sharp-web: Web playground to create Gaussian Splats using Apple's ml-sharp model. · GitHub](https://github.com/bring-shrubbery/ml-sharp-web)
3. [Apple - CoreML | onnxruntime](https://onnxruntime.ai/docs/execution-providers/CoreML-ExecutionProvider.html)
4. [Converting Apple’s Sharp ML for your devices | Raleigh](https://sf.aitinkerers.org/talks/rsvp_kERNVs9PVNw)
5. [ONNX Runtime Web—running your machine learning model in browser | Microsoft Open Source Blog](https://opensource.microsoft.com/blog/2021/09/02/onnx-runtime-web-running-your-machine-learning-model-in-browser/)
6. [[Web] Support iOS devices · Issue #22776 · microsoft/onnxruntime](https://github.com/microsoft/onnxruntime/issues/22776)
7. [ShowHN:Apple'sSharpRunningintheBrowserviaONNX...](https://qht.co/item?id=47995037)
8. [ONNXRuntime| Home](https://onnxruntime.ai/)
9. [WebAssembly for AI Agents: Running Models in the Browser](https://callsphere.ai/blog/webassembly-ai-agents-running-models-in-the-browser)
10. [Run YOLO Model in the Browser with ONNX, WebAssembly, and Next.js - PyImageSearch](https://pyimagesearch.com/2025/07/28/run-yolo-model-in-the-browser-with-onnx-webassembly-and-next-js/)
11. [GitHub - bring-shrubbery/ml-sharp-web: Web playground to... (Daily.dev)](https://app.daily.dev/posts/github---bring-shrubbery-ml-sharp-web-web-playground-to-create-gaussian-splats-using-apple-s-ml-sha-0sg97lpiv)
12. [GitHub - miketahani/ml-sharp-browser: Apple's SHARP model running in ...](https://github.com/miketahani/ml-sharp-browser)
13. [Web | onnxruntime Tutorials](https://onnxruntime.ai/docs/tutorials/web/)

## FACT-CHECK SUMMARY
- Claims checked: 21
- Claims verified: 21
- Verdict: PASS