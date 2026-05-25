---
layout: post
title: "AI가 만든 가짜 사진, 이제 딱 걸린다? 챗GPT에 숨겨진 '투명 도장'의 비밀"
description: "오픈AI와 구글이 협력하여 챗GPT가 만든 이미지에 지워지지 않는 투명 워터마크(SynthID)를 도입합니다. 가짜 AI 사진을 누구나 쉽게 구별할 수 있게 해주는 새로운 검증 도구와 기술의 원리를 아주 쉽게 설명해 드립니다."
summary: "오픈AI가 구글의 신스아이디(SynthID) 기술을 도입해 AI 생성 이미지에 지워지지 않는 보이지 않는 워터마크를 새기고, 이를 확인할 수 있는 대중용 감별 도구를 전격 공개했습니다."
tags: [OpenAI, Google, SynthID, 워터마크, AI가짜사진, 챗GPT, 딥페이크]
image: 2026-05-25-OpenAI-Adopts-Googles-SynthID-Watermark-for-AI-Images-with-Verification-Tool.jpg
image_alt: "돋보기를 들고 디지털 이미지 픽셀 속에 숨겨진 밝게 빛나는 AI 워터마크를 찾아내는 모습을 부드러운 일러스트로 표현한 그림"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "기술이 만들어낸 혼란은 결국 더 발전된 기술과 책임감 있는 연대를 통해 해결됩니다. 오픈AI와 구글의 이번 협력은 '보이지 않는 진실'을 지켜내기 위한 위대한 첫걸음입니다."
quiz:
  - question: "기사에서 메타데이터(C2PA)의 한계를 설명하기 위해 사용한 비유는 무엇인가요?"
    choices: ["물감에 섞은 특수 형광 물질", "사진 뒷면에 붙여놓은 포스트잇", "은행의 위조지폐 감별기"]
    answer: 1
    explanation: "메타데이터는 사진의 유용한 정보를 담고 있지만, 누군가 악의적으로 지우려고 하면 '포스트잇'처럼 쉽게 떼어내어 없앨 수 있다는 한계가 있습니다."
  - question: "구글 딥마인드가 개발한 '신스아이디(SynthID)' 워터마크 기술의 가장 큰 특징은 무엇인가요?"
    choices: ["사람의 눈에 뚜렷하게 보이는 커다란 로고를 박아 넣는다.", "이미지를 자르거나 색감을 바꿔도 워터마크가 지워지지 않고 살아남는다.", "텍스트로 작성된 문서의 조작 여부만 확인해 준다."]
    answer: 1
    explanation: "신스아이디는 픽셀 자체에 정보를 숨기기 때문에 이미지를 자르거나(크롭), 필터를 적용하거나, 포맷을 변환하는 등의 편집을 거쳐도 워터마크가 강력하게 살아남습니다."
  - question: "오픈AI가 새롭게 공개한 '퍼블릭 검증 도구(Verification Tool)'와 관련된 설명으로 알맞은 것은 무엇인가요?"
    choices: ["세상에 존재하는 모든 종류의 AI 이미지를 100% 감별할 수 있다.", "오픈AI의 도구(챗GPT, 코덱스 등)로 만들어진 이미지에 숨겨진 신호를 확인해 준다.", "사용하려면 반드시 유료 구독을 해야만 접속할 수 있다."]
    answer: 1
    explanation: "현재 이 검증 도구는 세상의 모든 AI 이미지가 아닌, 챗GPT, 코덱스, 오픈AI API 등 자사의 도구로 생성된 이미지에 담긴 신호를 확인하는 데 초점이 맞춰져 있습니다."
lang: ko
ref: 2026-05-25-OpenAI-Adopts-Googles-SynthID-Watermark-for-AI-Images-with-Verification-Tool
audio: 2026-05-25-OpenAI-Adopts-Googles-SynthID-Watermark-for-AI-Images-with-Verification-Tool.mp3
permalink: /2026/05/25/OpenAI-Adopts-Googles-SynthID-Watermark-for-AI-Images-with-Verification-Tool/
---

## 들어가며: 눈으로 보는 것도 믿을 수 없는 시대

상상해보세요. 평화로운 주말 아침, 소셜 미디어를 스크롤하다가 너무나도 생생하고 충격적인 사진을 발견하게 됩니다. 유명 정치인이 터무니없는 옷을 입고 있거나, 한 번도 일어난 적 없는 재난 현장이 마치 진짜처럼 눈앞에 펼쳐집니다. 처음에는 두 눈을 의심하지만, 사진 속 그림자와 질감이 너무나 완벽해서 결국 그 사진이 진짜라고 믿게 되어버리죠. 우리는 지금 스마트폰의 음성 비서가 똑똑해지는 것을 넘어, 인공지능(AI, 인간의 지능을 모방하여 학습하고 판단하는 컴퓨터 시스템)이 우리의 눈을 완벽하게 속일 수 있는 시대에 살고 있습니다.

현재 많은 사람들이 실제 사진과 AI가 만들어낸 창작물을 구별하는 데 엄청난 어려움을 겪고 있습니다. 무엇이 진짜이고 무엇이 가짜인지 알 수 없다는 불안감은 사회적 신뢰를 무너뜨릴 수 있는 심각한 문제입니다. 이런 혼란 속에서, 세상을 놀라게 할 거대한 연합군이 등장했습니다. 바로 세계 최고의 AI 기술을 자랑하는 두 라이벌 기업, 오픈AI(OpenAI)와 구글(Google)이 전격적으로 손을 잡은 것입니다. 

최근 오픈AI는 챗GPT(ChatGPT)를 비롯한 자사의 AI 도구로 만든 이미지에 구글의 '신스아이디(SynthID)'라는 보이지 않는 워터마크를 도입하기로 발표했습니다 [[Source 2] OpenAI Adopts Google SynthID Watermarks for AI Image Detection](https://winbuzzer.com/2026/05/20/openai-adds-support-for-googles-synthid-watermarks-xcxwbn/). 과연 이 기술이 어떻게 우리의 눈을 지켜주고 혼란을 막아줄 수 있을지, 지금부터 따뜻한 커피 한잔 마시며 이야기하듯 아주 쉽고 자세하게 풀어드리겠습니다.

---

## 이게 왜 중요한가요? (Why It Matters)

쉽게 말해서, 일상 속 평범한 사진 한 장이 엄청난 사회적 파장을 일으킬 수 있을 만큼 AI 기술이 고도화되었기 때문입니다. 최근 몇 년간 AI 이미지 생성 기술은 그야말로 폭발적으로 발전했습니다. 과거에는 AI가 그린 사람의 손가락 개수가 이상하거나 배경이 어색해서 누구나 쉽게 가짜임을 눈치챌 수 있었습니다. 하지만 이제는 모공의 미세한 질감이나 눈동자에 맺힌 빛의 반사까지도 완벽하게 모방해 냅니다. 일반 대중뿐만 아니라 전문 사진작가들조차 육안으로는 진짜와 가짜를 판별하기 어려운 수준에 이르렀습니다.

이런 상황에서 우리가 안심하고 의존할 수 있는 기술적 장치가 절실히 필요했습니다. 누군가 악의적인 목적으로 가짜 뉴스를 퍼뜨리거나 타인의 명예를 훼손하는 정교한 합성 사진(딥페이크, Deepfake)을 만들었을 때, 이를 기술적으로 명확하게 "이것은 AI가 만든 가짜입니다"라고 증명할 수단이 없다면 겉잡을 수 없는 혼란에 빠질 것입니다. 

따라서 오픈AI가 자사의 생성물에 구글의 첨단 기술을 도입하여 '보이지 않는 꼬리표'를 달고, 대중이 이를 직접 확인할 수 있는 환경을 구축한다는 것은 매우 큰 의미를 지닙니다. 사람들은 이제 그저 두 눈의 착각에 기대는 것을 넘어, 기술이 제공하는 투명한 정보를 통해 사진의 진위를 판단할 수 있게 될 것입니다. 이러한 두 회사의 결단은 대중들이 실제 사진과 AI 창작물을 보다 쉽게 구별할 수 있도록 돕기 위한 강력하고 책임감 있는 목표를 가지고 있습니다 [[Source 2] OpenAI Adopts Google SynthID Watermarks for AI Image Detection](https://winbuzzer.com/2026/05/20/openai-adds-support-for-googles-synthid-watermarks-xcxwbn/).

---

## 쉽게 이해하기: '포스트잇'과 '지워지지 않는 특수 물감' (The Explainer)

가짜 사진을 막기 위해 오픈AI가 꺼내든 방패는 크게 두 가지입니다. 바로 'C2PA 메타데이터'와 구글의 '신스아이디(SynthID)'입니다. 이 두 가지가 도대체 무엇인지, 왜 굳이 두 가지나 겹쳐서 사용하는 것인지 재미있는 비유를 통해 알아보겠습니다.

### 첫 번째 방패: 사진 뒷면의 '포스트잇', 메타데이터
먼저 메타데이터(Metadata, 사진이 언제, 어디서, 어떤 기기로 만들어졌는지 기록해 둔 숨은 디지털 정보표)에 대해 알아보겠습니다. 오픈AI는 이번 발표 이전부터 이미 C2PA라는 국제 표준 메타데이터 방식을 사용해 왔으며, 이를 통해 'C2PA 준수 생성기(C2PA Conforming Generator)'라는 자격을 갖추고 있었습니다 [[Source 8] OpenAI joins C2PA and adds Google SynthID watermarks to provenance stack](https://www.resultsense.com/news/2026-05-20-openai-c2pa-synthid-content-provenance/). 

비유하면 메타데이터는 **"사진 뒷면에 정성스럽게 적어 붙여놓은 포스트잇"**과 같습니다. 이 포스트잇에는 "이 사진은 2026년 5월에 챗GPT가 그렸음"이라고 아주 선명하게 적혀 있죠. 착한 사람들이 정보를 확인할 때는 이 포스트잇이 너무나 유용합니다. 

하지만 치명적인 단점이 하나 있습니다. 나쁜 마음을 먹은 사람이 가짜 뉴스를 퍼뜨리기 위해 이 사진을 꾹 눌러 저장한 뒤, 메타데이터 편집기를 이용해 포스트잇을 툭 떼어버리거나 다른 소셜 미디어에 업로드하면서 시스템이 자동으로 포스트잇을 지워버리게 만들 수 있다는 점입니다. 제공하는 정보는 아주 정확하지만, 안타깝게도 외부 공격에 대한 생존력이 너무나 약한 것입니다.

### 두 번째 방패: 픽셀에 스며든 '특수 물감', 신스아이디(SynthID)
포스트잇의 이런 약점을 완벽하게 보완하기 위해 등장한 구원투수가 바로 구글 딥마인드(Google DeepMind, 구글의 첨단 인공지능 연구 부서)가 개발한 워터마크(Watermark, 파일의 출처를 밝히기 위해 디지털 파일에 삽입하는 식별용 표시) 기술인 신스아이디(SynthID)입니다. 구글이 만든 이 기술은 흔히 우리가 아는 것처럼 사진 한구석에 방송국 로고처럼 보기 싫게 도장을 쾅 찍어놓는 기술이 아닙니다 [[Source 9] OpenAI enhances AI detection with SynthID watermarking and verification portal](https://cryptobriefing.com/openai-synthid-watermarking-ai-detection/).

이 기술은 그림을 그릴 때 **"물감 자체에 아주 미세하게 섞어 넣은 보이지 않는 특수 형광 물질"**이라고 생각하시면 됩니다. 사람의 눈에는 그저 평범한 풍경이나 흠잡을 데 없는 인물 사진으로 보입니다. 이미지의 아름다움이나 화질에는 전혀 영향을 주지 않죠. 하지만 이 물감을 칠한 사진을 컴퓨터의 특별한 스캐너로 들여다보면, 수십만 개의 픽셀들 사이에 숨겨져 있던 고유한 패턴이 스스로 빛을 내며 "나는 AI가 그렸어!"라고 외치게 됩니다.

가장 놀라운 점은 이 '특수 물감'의 끈질긴 생존력입니다. 포스트잇은 쉽게 떼어낼 수 있었지만, 신스아이디는 사진을 구성하는 가장 작은 단위인 픽셀 자체에 녹아들어 있기 때문에 크롭(Cropping, 이미지의 가장자리를 잘라내는 작업), 필터 적용(Filtering, 사진의 색감이나 분위기를 인위적으로 바꾸는 작업), 포맷 변환(Format conversion, PNG 파일을 JPG 파일로 바꾸는 등의 작업)과 같은 흔한 사진 편집 과정을 거쳐도 끄떡없이 살아남아 워터마크를 유지합니다 [[Source 9] OpenAI enhances AI detection with SynthID watermarking and verification portal](https://cryptobriefing.com/openai-synthid-watermarking-ai-detection/). 심지어 스마트폰으로 화면 캡처(Screenshots)를 하거나 크기 조절(Resizing)을 겪어도 그 신호가 지워지지 않고 끈질기게 버텨냅니다 [[Source 7] OpenAI Adopts C2PA and SynthID for Image Verification](https://letsdatascience.com/news/openai-adopts-c2pa-and-synthid-for-image-verification-ed2f7b5f/). 

정리하자면, 오픈AI는 C2PA 메타데이터라는 '포스트잇'과 구글의 신스아이디라는 '특수 물감'을 동시에 사진에 적용하는 것입니다. 이러한 이중 시스템 접근 방식은 콘텐츠의 출처 증명을 더욱 강력하고 회복력 있게 만들기 위해 똑똑하게 설계되었습니다 [[Source 4] OpenAI Adopts Google's SynthID for AI Image Watermarking in ...](https://mwm.ai/articles/openai-adopts-google-s-synthid-for-ai-image-watermarking-in-may-2026). 오픈AI 측에서도 아주 명쾌하게 "이 두 시스템은 서로를 단단하게 강화합니다(These two systems reinforce each other)"라고 설명하며 두 기술의 완벽한 조화를 강조했습니다 [[Source 9] OpenAI enhances AI detection with SynthID watermarking and verification portal](https://cryptobriefing.com/openai-synthid-watermarking-ai-detection/).

---

## 현재 상황: 누구나 확인 가능한 'AI 감식반'의 등장 (Where We Stand)

방패를 아무리 튼튼하게 만들었다고 해도, 일반 사람들이 그 방패가 진짜인지 아닌지 확인할 방법이 없다면 아무 소용이 없겠죠? 그래서 오픈AI는 대중들을 위해 퍼블릭 검증 도구(Public Verification Tool, 누구나 접속해서 사진의 진위를 바로 확인할 수 있는 공개 사이트)의 프리뷰 버전을 함께 선보였습니다 [[Source 3] OpenAI is making it easier to check if an image was made by ...](https://techcrunch.com/2026/05/19/openai-is-making-it-easier-to-check-if-an-image-was-made-by-their-models/). 

이 도구는 마치 우리가 은행에서 5만 원권 지폐를 넣고 진짜 돈인지 가짜 돈인지 구별할 때 쓰는 **"위조지폐 감별기"**와 완벽하게 같은 역할을 합니다. 사용자가 의심스러운 이미지를 이 웹사이트에 업로드하기만 하면, 검증 도구가 이미지에 숨겨진 메타데이터 포스트잇과 신스아이디 특수 물감 신호가 존재하는지 두 가지를 모두 꼼꼼하게 검사합니다 [[Source 3] OpenAI is making it easier to check if an image was made by ...](https://techcrunch.com/2026/05/19/openai-is-making-it-easier-to-check-if-an-image-was-made-by-their-models/]. 대중들은 복잡한 컴퓨터 지식이 전혀 없어도, 이 포털을 통해 클릭 한 번으로 사진 속에 오픈AI가 남긴 AI 생성 신호가 숨어 있는지 쉽게 테스트해 볼 수 있습니다 [[Source 4] OpenAI Adopts Google's SynthID for AI Image Watermarking in ...](https://mwm.ai/articles/openai-adopts-google-s-synthid-for-ai-image-watermarking-in-may-2026). 

다만, 한 가지 꼭 알아두셔야 할 점이 있습니다. 현재 이 감별기가 세상의 모든 AI 사진을 100% 잡아내는 것은 아닙니다. 주로 챗GPT(ChatGPT, 텍스트로 명령하면 답변과 이미지를 만들어주는 대화형 AI), 오픈AI API(다른 회사의 앱에서도 오픈AI의 기능을 가져다 쓸 수 있게 해주는 통로), 그리고 코덱스(Codex, 코딩을 도와주는 AI 도구) 등 철저하게 오픈AI의 자사 도구를 통해 생성된 이미지를 집중적으로 확인해 줍니다 [[Source 7] OpenAI Adopts C2PA and SynthID for Image Verification](https://letsdatascience.com/news/openai-adopts-c2pa-and-synthid-for-image-verification-ed2f7b5f/]. 사용자는 이제 단톡방이나 소셜 미디어에서 챗GPT가 만든 것 같은 그럴싸한 가짜 뉴스를 보았을 때, 이 위조지폐 감별기에 사진을 쑥 넣어보고 단 1초 만에 "아하, 이건 사람이 찍은 게 아니라 AI가 만든 거구나!" 하고 진실을 파악할 수 있게 된 것입니다.

더욱 고무적인 사실은 이러한 투명성을 향한 움직임이 비단 오픈AI 혼자만의 외침으로 끝나지 않고 있다는 점입니다. 컴퓨터의 두뇌 역할을 하는 그래픽 칩(GPU)의 세계 최강자 엔비디아(Nvidia)를 비롯한 여러 대형 기술 기업들도 구글의 신스아이디 AI 워터마크 기술을 앞다투어 도입하고 있습니다 [[Source 5] Google's SynthID AI watermarking tech is being adopted by ...](https://arstechnica.com/google/2026/05/googles-synthid-ai-watermarking-tech-is-being-adopted-by-openai-nvidia-and-more/]. 

또한 오픈AI가 구글 딥마인드와 직접 파트너십을 맺고 C2PA 표준을 지키며 적극적으로 나선 것은, IT 업계 전반에 투명성의 가치를 널리 퍼뜨리는 거대한 신호탄으로 평가받고 있습니다 [[Source 13] OpenAIpartners withGoogleDeepMind to integrateSynthID... | KuCoin](https://www.kucoin.com/news/flash/openai-partners-with-google-deepmind-to-add-synthid-watermarks-and-image-verification-tool-to-chatgpt). 이는 곧 신스아이디 기술이 향후 AI 콘텐츠 시장의 핵심적인 글로벌 표준으로 확고하게 자리 잡아가고 있음을 명확하게 보여줍니다 [[Source 12] GoogleNews-OpenAIadoptsGoogle'sSynthIDtowatermark...](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2liN0xhWEVSRmxaemFtVkNUUmNpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN:en). 결론적으로, 이러한 구글의 앞선 기술을 채택함으로써 오픈AI는 AI가 생성한 이미지를 대중들이 한결 더 편하게 식별하고 불필요한 혼란을 방지할 수 있도록 돕는 실질적이고 뜻깊은 진전을 이루어냈습니다 [[Source 10] OpenAI adopts SynthID from Google to better identify images generated by AI](https://myhostnews.com/openai-adopts-synthid-from-google-to-better-identify-images-generated-by-ai/).

---

## 앞으로 어떻게 될까? 끝나지 않는 쫓고 쫓기는 추격전 (What's Next)

오픈AI와 구글의 이 놀라운 연합 작전 덕분에 우리는 일상 속 가짜 이미지를 가려낼 아주 든든한 무기를 얻게 되었습니다. 하지만 방심하기엔 이릅니다. 이 기술이 세상의 모든 혼란을 당장 내일 아침 100% 종식시킬 수 있는 마법의 지팡이는 결코 아니기 때문입니다. 앞으로 우리가 풀어가야 할 두 가지 현실적인 과제를 살펴보겠습니다.

첫째, 세상에는 오픈AI와 구글 말고도 수백 가지의 이름 모를 AI 이미지 생성 프로그램이 존재합니다. 안타깝게도 현재 모든 AI 이미지 제작 도구가 구글의 신스아이디 기술을 사용하는 것은 아닙니다 [[Source 14] SpottingAIimagesis finally getting easier thanks toOpenAIand...](https://tech-oracle.com/spotting-ai-images-is-finally-getting-easier-thanks-to-openai-and-google/). 누군가가 워터마크 기술이 아예 없는 다른 회사의 AI 모델을 사용해 교묘하게 가짜 사진을 만들어낸다면, 이 검증 도구는 그저 침묵할 수밖에 없습니다. 그렇기 때문에 세상의 모든 AI 도구들이 이와 유사한 강력한 검증 시스템을 전면적으로 의무 도입하지 않는 이상, 어떤 단일 도구도 특정 이미지가 AI로 만들어지지 않았다고 '완벽하게 보장'하는 것은 당분간 불가능에 가깝습니다 [[Source 14] SpottingAIimagesis finally getting easier thanks toOpenAIand...](https://tech-oracle.com/spotting-ai-images-is-finally-getting-easier-thanks-to-openai-and-google/).

둘째, 기술에 밝은 악의적인 사용자들과 이를 막으려는 보안 전문가들 사이의 끊임없는 '창과 방패'의 싸움이 예상됩니다. 전 세계 컴퓨터 전문가들이 모인 해커 커뮤니티인 해커뉴스(HackerNews)에서는 이 새로운 검증 도구에 대해 매우 날카롭고 흥미로운 관점을 제시했습니다. 악의적인 사용자가 사진의 워터마크를 지워보려고 사진을 마구 자르고 비틀어 조작한 뒤, 역설적이게도 **이 감별기를 사용해 "내 속임수가 통했는지" 스스로 테스트해 보는 용도로 이 도구를 반복해서 악용할 수도 있다**는 따끔한 지적을 한 것입니다 [[Source 16] OpenAIAdoptsGoogle'sSynthIDWatermarkforAI... | HackerNews](https://news.ycombinator.com/item?id=48198291). 

하지만 생각해 보면, 나쁜 사람들이 워터마크를 피하기 위해 이토록 복잡한 과정을 거쳐야 하거나, 처음부터 감시망이 없는 워터마크가 없는 이미지 생성 모델(Unwatermarked image-generation model)을 찾아 어둠의 경로를 헤매게 만든다는 사실 자체만으로도 의미가 있습니다. 범죄와 조작을 저지르기 위한 '진입 장벽'을 훨씬 높이는 본연의 목적을 어느 정도 훌륭하게 달성하고 있다고 볼 수 있기 때문입니다 [[Source 16] OpenAIAdoptsGoogle'sSynthIDWatermarkforAI... | HackerNews](https://news.ycombinator.com/item?id=48198291).

전문가들은 한목소리로 입을 모읍니다. 이러한 피할 수 없는 기술적 한계가 있다고 해서 오픈AI와 구글이 보여준 결단의 가치가 폄하되는 것은 결코 아니며, 이번 협력은 투명하고 안전한 AI 사회로 나아가기 위한 매우 긍정적이고 묵직한 첫걸음이라는 것입니다 [[Source 14] SpottingAIimagesis finally getting easier thanks toOpenAIand...](https://tech-oracle.com/spotting-ai-images-is-finally-getting-easier-thanks-to-openai-and-google/). 대형 기술 기업들이 자신들이 세상에 내놓은 강력한 창조물에 대해 끝까지 책임을 지고 대중과 소통하려는 따뜻한 의지를 보여주었다는 점에서, 우리는 다가올 인공지능 시대를 조금 더 안심하고 지혜롭게 맞이할 수 있게 되었습니다.

---

## AI의 시선 (AI's Take)

**MindTickleBytes AI 기자의 시선:** 
새로운 기술의 급격한 발전이 빚어낸 사회적 혼란과 불안은 역설적이게도, 결국 더 정교하게 발전된 다음 단계의 기술과 업계를 이끄는 선두주자들의 책임감 있는 연대를 통해서만 건강하게 해결될 수 있습니다. 평소에는 최고의 자리를 놓고 서로 치열하게 경쟁하는 관계인 오픈AI와 구글이 대중의 혼란을 막기 위해 흔쾌히 손을 맞잡은 이번 결정은, 자칫 차가운 디지털 데이터 속에 영원히 묻혀버릴 뻔한 '보이지 않는 진실'을 굳건히 지켜내기 위한 위대한 첫걸음입니다. 

거창한 법이나 규제 이전에, 기술을 만드는 사람들이 스스로 브레이크를 달고 안전망을 구축했다는 사실이 대중에게 주는 안도감은 실로 큽니다. 앞으로 더 많은 국내외 기업들이 기꺼이 이 흐름에 동참하여, 작은 물방울(워터마크) 하나하나가 모여 인공지능 생태계 전체의 투명성을 깨끗하게 정화하는 거대한 파도로 우렁차게 성장하기를 기대해 봅니다.

---

## 참고자료

1. [[Source 2] OpenAI Adopts Google SynthID Watermarks for AI Image Detection](https://winbuzzer.com/2026/05/20/openai-adds-support-for-googles-synthid-watermarks-xcxwbn/)
2. [[Source 3] OpenAI is making it easier to check if an image was made by ...](https://techcrunch.com/2026/05/19/openai-is-making-it-easier-to-check-if-an-image-was-made-by-their-models/)
3. [[Source 4] OpenAI Adopts Google's SynthID for AI Image Watermarking in ...](https://mwm.ai/articles/openai-adopts-google-s-synthid-for-ai-image-watermarking-in-may-2026)
4. [[Source 5] Google's SynthID AI watermarking tech is being adopted by ...](https://arstechnica.com/google/2026/05/googles-synthid-ai-watermarking-tech-is-being-adopted-by-openai-nvidia-and-more/)
5. [[Source 7] OpenAI Adopts C2PA and SynthID for Image Verification](https://letsdatascience.com/news/openai-adopts-c2pa-and-synthid-for-image-verification-ed2f7b5f/)
6. [[Source 8] OpenAI joins C2PA and adds Google SynthID watermarks to provenance stack](https://www.resultsense.com/news/2026-05-20-openai-c2pa-synthid-content-provenance/)
7. [[Source 9] OpenAI enhances AI detection with SynthID watermarking and verification portal](https://cryptobriefing.com/openai-synthid-watermarking-ai-detection/)
8. [[Source 10] OpenAI adopts SynthID from Google to better identify images generated by AI](https://myhostnews.com/openai-adopts-synthid-from-google-to-better-identify-images-generated-by-ai/)
9. [[Source 12] GoogleNews-OpenAIadoptsGoogle'sSynthIDtowatermark...](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2liN0xhWEVSRmxaemFtVkNUUmNpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN:en)
10. [[Source 13] OpenAIpartners withGoogleDeepMind to integrateSynthID... | KuCoin](https://www.kucoin.com/news/flash/openai-partners-with-google-deepmind-to-add-synthid-watermarks-and-image-verification-tool-to-chatgpt)
11. [[Source 14] SpottingAIimagesis finally getting easier thanks toOpenAIand...](https://tech-oracle.com/spotting-ai-images-is-finally-getting-easier-thanks-to-openai-and-google/)
12. [[Source 16] OpenAIAdoptsGoogle'sSynthIDWatermarkforAI... | HackerNews](https://news.ycombinator.com/item?id=48198291)