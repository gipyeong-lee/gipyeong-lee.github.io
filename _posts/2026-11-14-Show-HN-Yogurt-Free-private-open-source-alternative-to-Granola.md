---
layout: post
title: "회의 때마다 들어오는 감시자 봇, 이제 그만! 사생활을 지키는 오픈소스 회의 노트 앱 '요거트(Yogurt)'"
description: "줌, 구글 밋, 팀즈 회의에 몰래 들어오는 봇 없이 내 컴퓨터에서 안전하게 작동하는 무료 오픈소스 회의 노트 앱 요거트(Yogurt)를 소개합니다."
summary: "회의 때마다 낯선 봇이 참석해 눈치를 보게 만들던 기존 AI 회의록 서비스의 대안으로, 내 컴퓨터 안에서 안전하게 음성을 텍스트로 바꾸고 요약해주는 오픈소스 데스크톱 앱 '요거트(Yogurt)'가 주목받고 있습니다."
tags: [Yogurt, Granola, AI회의록, 오픈소스, 개인정보보호, 온디바이스AI]
image: 2026-11-14-Show-HN-Yogurt-Free-private-open-source-alternative-to-Granola.jpg
image_alt: "컴퓨터 화면 앞에 놓인 요거트(Yogurt) 앱 인터페이스와 회의 노트가 로컬에서 안전하게 처리되는 모습을 형상화한 일러스트"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "클라우드 서비스가 주도하던 회의 노트 시장에 프라이버시와 오픈소스 철학을 무기로 등장한 요거트는, 개발자와 프라이버시 민감 사용자 모두에게 반가운 전환점이 될 것입니다."
quiz:
  - question: "요거트(Yogurt)가 기존의 많은 회의 녹음 툴과 다른 가장 큰 특징은 무엇인가요?"
    choices: ["회의에 AI 봇이 직접 참여하지 않고 로컬에서 백그라운드 녹음한다", "유료 구독을 해야만 녹취록을 내보낼 수 있다", "인터넷 연결이 없으면 아예 실행되지 않는다"]
    answer: 0
    explanation: "요거트는 줌, 구글 밋, 팀즈 등의 회의에 봇으로 입장하지 않고, 내 컴퓨터 백그라운드에서 직접 소리를 녹음하여 프라이버시를 지킵니다."
  - question: "요거트 앱에서 생성된 회의 녹음과 요약본은 어디에 저장되나요?"
    choices: ["개발사의 클라우드 서버", "사용자의 컴퓨터 내부", "오픈소스 퍼블릭 데이터베이스"]
    answer: 1
    explanation: "요거트는 모든 회의 녹음, 텍스트 변환(트랜스크립트), 요약본이 컴퓨터 외부로 유출되지 않고 오직 로컬 장치에만 머무르도록 설계되었습니다."
  - question: "요거트는 어떤 라이선스로 배포되는 오픈소스 프로젝트인가요?"
    choices: ["GPL v3", "MIT 라이선스", "상용 독점 라이선스"]
    answer: 1
    explanation: "요거트는 에릭(Eric)이 개발한 MIT 라이선스 기반의 자유롭고 개방된 오픈소스 데스크톱 애플리케이션입니다."
lang: ko
ref: 2026-11-14-Show-HN-Yogurt-Free-private-open-source-alternative-to-Granola
audio: 2026-11-14-Show-HN-Yogurt-Free-private-open-source-alternative-to-Granola.mp3
permalink: /2026/11/14/Show-HN-Yogurt-Free-private-open-source-alternative-to-Granola/
---

상상해보세요. 중요한 사내 회의나 고객사 미팅이 시작되는데, 회의 화면 구석에 낯선 이름의 'AI 봇(Bot)'이 떡하니 자리 잡습니다. 회의 참여자들은 왠지 모를 긴장감을 느끼고, "이 대화가 어디 클라우드 서버에 고스란히 저장되어 나중에 광고 타겟팅이나 모델 학습에 쓰이지 않을까?" 하는 찜찜한 불안감을 지울 수 없습니다. 

우리가 일상적으로 사용하는 많은 AI 회의 보조 도구들은 편리함을 주는 대신, 우리의 소중한 대화 내용을 외부 클라우드로 전송하고 때로는 유료 구독을 강요합니다. 특히 최근 인기를 끌었던 그라놀라(Granola) 같은 서비스들도 훌륭하지만, 전체 내보내기 기능을 유료 플랜으로 제한하거나 데이터를 암호화하여 관리하는 등의 제약이 존재합니다 [Source 13]. 비유하자면, 다이어리를 쓰는데 매번 모르는 사람이 옆에서 내용을 훔쳐보고 검열하는 듯한 답답함과 비슷합니다.

이러한 답답함을 근본적으로 해소하기 위해 등장한 신선한 오픈소스 프로젝트가 있습니다. 바로 **요거트(Yogurt)**입니다. 해커뉴스(Hacker News) 쇼 HN(Show HN)을 통해 세상에 알려진 요거트는, 줌(Zoom), 구글 밋(Google Meet), 팀즈(Teams) 등의 화상 회의에 봇을 들여보내지 않고 오직 내 컴퓨터 안에서 안전하게 작동하는 무료 오픈소스 회의 노트 앱입니다 [Source 1, Source 8].

---

## 이게 왜 중요한가요?

현대 직장인들과 프리랜서, 원격 근무자들에게 회의는 하루의 상당 부분을 차지합니다. 회의 내용을 기록하고 요약해주는 AI 도구는 이제 필수품이 되었지만, 그 이면에는 늘 '프라이버시 침해'라는 꼬리표가 따라붙었습니다. 내가 나눈 민감한 사업상 아이디어, 개인적인 대화, 혹은 사내 기밀 정보가 타사의 클라우드 서버에 저장된다는 것은 언제 터질지 모르는 보안 사고의 시한폭탄과도 같습니다.

요거트는 이 문제를 근본부터 해결합니다. **"내 회의록은 내 컴퓨터에만 존재해야 한다"**는 철학을 바탕으로, 회의 녹음 파일과 텍스트 변환본, AI 요약 내용이 단 한 번도 외부 서버로 유출되지 않도록 설계되었습니다 [Source 1]. 개발자인 에릭(Eric)은 작고 강력해진 온디바이스(On-device, 기기 자체 탑재) AI 모델들을 활용하면, 굳이 비싼 유료 클라우드 서비스를 거치지 않고도 하드웨어 성능을 극대화하여 훌륭한 회의 노트를 만들 수 있다는 점에 주목했습니다 [Source 1].

또한, 완전한 오픈소스(MIT 라이선스)로 공개되어 있어 투명하게 코드를 검증할 수 있으며, 구독료 걱정 없이 누구나 자유롭게 다운로드하여 사용할 수 있습니다 [Source 1, Source 8]. 이는 비용에 민감한 개인 사용자나 보안이 철저해야 하는 기업 환경 모두에게 거대한 매력 포인트로 작용합니다. 더 이상 비싼 월 구독료를 내며 기능을 제한당할 필요가 없어진 것입니다.

---

## 쉽게 이해하기: 요거트는 어떻게 작동할까요?

쉽게 말해서, 요거트는 **‘내 컴퓨터 안에서 조용히 작동하는 개인 비서’**와 같습니다. 

기존의 회의 녹음 봇들이 회의실 문을 벌컥 열고 들어와 "안녕하세요, 기록을 시작합니다"라고 소리치며 참여자들을 긴장시키는 외부 참관인이라면, 요거트는 마치 회의실 한켠에 조용히 앉아 내 수첩에만 속삭이듯 기록을 남기는 정교한 녹음기와 같습니다. 

요거트의 작동 방식을 단계별로 살펴보면 다음과 같습니다.

1. **봇 없는 백그라운드 녹음**: 줌이나 구글 밋, 팀즈 미팅을 시작할 때 요거트는 회의방에 봇 계정으로 입장하지 않습니다 [Source 1, Source 2]. 대신 사용자의 컴퓨터 오디오 시스템을 백그라운드에서 감지하여 조용히 녹음을 진행합니다. 다른 사람들은 내가 회의록 앱을 돌리고 있는지조차 알 수 없습니다.
2. **실시간 텍스트 변환 및 요약**: 회의가 진행되는 동안 화면에는 실시간으로 대화 내용이 텍스트(Transcript)로 변환되어 표시됩니다 [Source 2]. 회의가 끝나면 온디바이스 AI 모델이 즉시 핵심 내용을 요약하고, 회의에서 결정된 실행 계획(Action Items)과 참석자별 할 일, 개인 메모를 깔끔하게 정리해 줍니다 [Source 2, Source 8].
3. **로컬 데이터 보관**: 생성된 모든 데이터는 외부 클라우드로 전송되지 않고 사용자의 하드디스크에 안전하게 저장됩니다 [Source 1]. 
4. **로컬 MCP 서버 연동**: 만약 더 거대한 성능을 가진 프론티어 AI 모델(예: 앤트로픽의 Claude, OpenAI 등)에게 회의 노트를 분석시키고 싶다면, 요거트가 제공하는 로컬 MCP(Model Context Protocol) 서버를 통해 사용자가 직접 선택하여 연결할 수 있습니다 [Source 1]. 중간 다리 역할을 하는 유료 클라우드 서비스에 의존할 필요가 전혀 없습니다 [Source 1].

이것은 마치 사진을 찍을 때 클라우드에 무조건 업로드하는 대신 스마트폰 기본 갤러리에 저장하고, 필요할 때만 내가 원하는 곳에 공유하는 것과 같습니다. 기술의 주도권이 서비스 제공자가 아닌 사용자에게 온전히 돌아오는 셈입니다.

---

## 현재 상황: 어디까지 와 있고 어떤 기능이 있나요?

요거트는 윈도우(Windows), 맥(Mac), 리눅스(Linux)를 모두 지원하는 크로스플랫폼 데스크톱 앱으로 개발되었습니다 [Source 1, Source 5]. 개발 초기 단계부터 UI의 상호작용과 애니메이션, 하드웨어 성능 최적화에 공을 들여 매끄럽고 빠른 사용자 경험을 제공합니다 [Source 1].

최근 공개된 v0.3.6 버전에서는 자동 업데이트 및 버전 확인 설정 기능이 추가되었고, 맥OS 환경에서 설치 후 디스크 이미지(DMG)를 스스로 마운트 해제(Eject)하는 섬세한 편의 기능까지 더해졌습니다 [Source 11]. 계정을 생성하거나 별도의 복잡한 연동 과정을 거치지 않아도 캘린더와 연동되어 내 미팅 스케줄을 곧바로 불러올 수 있는 완성도를 보여줍니다 [Source 1].

오픈소스 커뮤니티와 테크 블로거들 사이에서는 그라놀라의 훌륭한 오픈소스 대안(Open-Source Granola Alternative)으로 입소문이 나며, 프라이버시를 중시하는 실무자와 개발자들 사이에서 빠르게 확산되고 있습니다 [Source 1, Source 9]. 특히 유료 구독 모델이 대세인 SaaS 시장에서 무료이면서도 강력한 로컬 중심 기능을 제공한다는 점이 큰 차별점으로 작용하고 있습니다 [Source 1, Source 9].

---

## 앞으로 어떻게 될까?

앞으로 AI 회의록 시장은 '클라우드 중심의 중앙집중형 서비스'와 '내 기기 중심의 프라이버시형 온디바이스 서비스'로 양분될 가능성이 높습니다. 소형 오픈소스 AI 모델들의 성능이 비약적으로 발전함에 따라, 굳이 거대 서버를 거치지 않고도 개인 노트북이나 PC에서 충분히 고품질의 요약과 질의응답(Chat with your meetings)이 가능해졌기 때문입니다 [Source 1].

사용자들은 앞으로 회의록을 저장할 때 "이 회의 내용이 어디로 전송되는가?"를 가장 먼저 따지게 될 것입니다. 요거트와 같은 프로젝트들은 개발자가 자유롭게 기능을 확장하고, 사용자가 자신의 데이터를 완전히 통제할 수 있는 표준을 제시하고 있습니다. 

회의가 끝난 뒤 찜찜한 마음으로 봇을 퇴장시키던 풍경 대신, 내 컴퓨터 안에서 안전하고 빠르게 회의를 갈무리하는 모습이 앞으로의 표준이 될지도 모릅니다.

---

## AI의 시선: 왜 주목해야 하는가?

클라우드 서비스가 주도하던 회의 노트 시장에 프라이버시와 오픈소스 철학을 무기로 등장한 요거트는, 개발자와 프라이버시 민감 사용자 모두에게 반가운 전환점이 될 것입니다. 중앙 집중식 SaaS 생태계에 피로감을 느낀 사용자들에게 온디바이스 로컬 AI와 오픈소스의 조합이 얼마나 강력한 대안이 될 수 있는지 보여주는 모범적인 사례입니다.

---

## 참고자료

1. [Show HN: Yogurt – Free, private, open-source alternative to Granola](https://github.com/FrigadeHQ/yogurt) [Source 1]
2. [Yogurt: Free, private, open-source alternative to Granola](https://www.producthunt.com/products/yogurt) [Source 2]
3. [5 Best Open Source Granola Alternatives in 2026](https://openalternative.co/alternatives/granola) [Source 4]
4. [Best 10 Granola Alternatives & Competitors [2026] | Jamie](https://www.meetjamie.ai/blog/granola-alternatives) [Source 5]
5. [Free open-source alternatives to Granola | Maigentools](https://www.maigentools.com/alternatives/granola) [Source 6]
6. [Show HN: Yogurt – Free, private, open-source alternative...](https://daily.dev/posts/show-hn-yogurt-free-private-open-source-alternative-to-granola-w8zhburxd) [Source 8]
7. [Yogurt Growth Play: Free + Open Source Beats a Paid Leader ...](https://www.figuringoutwithai.com/growth/yogurt-free-open-source-granola-alternative-growth-play-2026) [Source 9]
8. [Yogurt AI: Granola의 무료 오픈소스 대안, 개인정보를 보호하는 AI 회의...](https://dev-hub.dev/news/8348) [Source 10]
9. [Yogurt AI: Free, Private, Open-Source Meeting Notes | AI/TLDR](https://ai-tldr.dev/tools/yogurt/) [Source 11]
10. [9 Best Granola AI Alternatives in 2026 (Compared & Reviewed)](https://www.getvoibe.com/resources/granola-alternatives/) [Source 13]