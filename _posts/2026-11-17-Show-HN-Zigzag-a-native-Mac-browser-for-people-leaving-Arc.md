---
layout: post
title: "아크(Arc) 브라우저가 사라진다고? 상하이 고등학생이 3주 만에 만든 기적의 맥 브라우저 '지그재그(Zigzag)'"
description: "2026년 12월 종료되는 아크 브라우저의 대안으로, 상하이의 고등학생 개발자가 스위프트(Swift)와 웹킷(WebKit)으로 단 3주 만에 개발한 초경량 맥 브라우저 지그재그(Zigzag)의 모든 것."
summary: "아크 브라우저 종료 소식에 충격받은 상하이 고등학생이 단 3주 만에 개발한, 18MB 초경량 맥 브라우저 '지그재그(Zigzag)'의 특징과 개발 비하인드."
tags: [Zigzag, Arc, MacBrowser, WebKit, OpenSource]
image: 2026-11-17-Show-HN-Zigzag-a-native-Mac-browser-for-people-leaving-Arc.jpg
image_alt: "맥 화면에 띄워진 깔끔한 사이드바와 스플릿 뷰 기능을 갖춘 지그재그 브라우저의 인터페이스 화면"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "대기업의 서비스 종료 결정에 좌절하지 않고 직접 코딩으로 답을 찾아낸 고등학생 개발자의 집념이 돋보입니다. 무거워진 현대 브라우저 생태계에 신선한 충격을 주는 가벼운 대안입니다."
quiz:
  - question: "지그재그(Zigzag) 브라우저를 개발한 개발자의 배경은 무엇인가요?"
    choices: ["실리콘밸리의 베테랑 브라우저 엔지니어", "상하이 출신의 고등학생", "유럽의 오픈소스 연구원"]
    answer: 1
    explanation: "지그재그는 상하이 출신의 고등학생 개발자 ZigaoWang이 아크 브라우저 종료 소식에 충격을 받아 3주 만에 직접 개발한 브라우저입니다 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)."
  - question: "지그재그 브라우저가 기반으로 하고 있는 애플의 엔진은 무엇인가요?"
    choices: ["크로미움(Chromium) 엔진", "웹킷(WebKit) 엔진", "게코(Gecko) 엔진"]
    answer: 1
    explanation: "지그재그는 크로미움이나 일렉트론이 아닌 애플의 순수 웹킷(WebKit) 엔진과 스위프트(Swift) 언어로 제작되었습니다 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)."
  - question: "지그재그 브라우저의 설치 용량은 대략 어느 정도인가요?"
    choices: ["약 18 MB", "약 871 MB", "약 1.5 GB"]
    answer: 0
    explanation: "지그재그는 불필요한 무거움을 덜어내고 약 18 MB의 초경량 설치 용량을 자랑합니다 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)."
lang: ko
ref: 2026-11-17-Show-HN-Zigzag-a-native-Mac-browser-for-people-leaving-Arc
audio: 2026-11-17-Show-HN-Zigzag-a-native-Mac-browser-for-people-leaving-Arc.mp3
permalink: /2026/11/17/Show-HN-Zigzag-a-native-Mac-browser-for-people-leaving-Arc/
---

상상해보세요. 매일 아침 컴퓨터를 켜고 업무와 개인 생활을 정리할 때, 내 손에 꼭 맞는 맞춤형 서랍장처럼 깔끔하게 정돈된 브라우저 창을 엽니다. 수많은 탭이 가로로 늘어서 정신없던 과거와 달리, 화면 측면에 우아하게 자리 잡은 사이드바와 공간별(Space) 분류는 디지털 작업의 신세계였습니다. 그러던 어느 날, 청천벽력 같은 소식이 날아듭니다. "당신이 매일 쓰던 그 브라우저가 곧 문을 닫습니다."

개발사인 The Browser Company가 혁신적인 인터페이스로 전 세계 사용자들의 사랑을 받았던 아크(Arc) 브라우저를 오는 2026년 12월 22일까지만 지원하고 완전히 종료한다고 발표했습니다 [BestArcBrowserAlternatives forMac(ArcEnds Dec 22...) | Macfolio](https://macfolio.com/blog/best-arc-browser-alternatives-for-mac). 이 소식에 맥(Mac) 사용자들은 거대한 혼란에 빠졌습니다. 다시 지루한 상단 가로 탭 방식으로 돌아갈 수는 없었기 때문입니다 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag). 바로 그때, 지구 반대편에서 한 고등학생 개발자가 이 절망적인 상황에 정면으로 도전장을 내밀었습니다. 단 3주 만에 아크 사용자들이 그리워하던 모든 것을 담아낸 초경량 맥 브라우저, **지그재그(Zigzag)**가 탄생한 것입니다 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag).

---

## 이게 왜 중요한가요?

현대의 웹 브라우저들은 점점 더 무거워지고 있습니다. 수많은 기능을 집어넣다 보니 램(RAM)을 블랙홀처럼 빨아먹고, 배터리를 광속으로 소모하며, 프로그램 설치 용량만 수백 메가바이트에서 기가바이트를 넘나들기 일쑤입니다. 실제로 종료를 앞둔 아크 브라우저는 설치 용량이 800MB를 훌쩍 넘습니다 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag). 

일반 사용자 입장에서는 웹서핑 하나 하자고 컴퓨터 자원의 대부분을 브라우저에 내어주어야 하는 셈입니다. 게다가 대기업 서비스가 종료되면 사용자는 영문도 모른 채 익숙한 도구를 잃고 다른 대안을 찾아 헤매야 합니다. 

지그재그는 이러한 현대 소프트웨어의 거대함과 폐쇄성에 반기를 듭니다. 설치 용량이 고작 **18 MB**에 불과하며 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag), 계정 가입도 필요 없고 텔레메트리(사용자 행태 추적 데이터)나 분석 도구를 일체 배제하여 완전한 프라이버시를 보장합니다 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag). 개인이 만든 오픈소스 프로젝트이기 때문에 그 누구도 마음대로 서비스를 중단시킬 수 없으며, 누구나 코드를 수정하고 발전시킬 수 있습니다 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag).

---

## 쉽게 이해하기: 맥에 최적화된 맞춤형 스포츠카 만들기

비유하면 이렇습니다. 기존의 많은 브라우저들이 거대한 버스 엔진을 달고 이리저리 무거운 짐을 실어 나르는 대형 트럭 같다면, 지그재그는 맥(Mac)이라는 정교한 도로 구조에 맞춰 가공된 날렵한 경량 전기 스포츠카에 비유할 수 있습니다. 쉽게 말해서 불필요한 무게를 과감히 덜어내고 꼭 필요한 핵심 주행 성능에만 집중한 것입니다.

지그재그는 구글의 크로미움(Chromium, 크롬 브라우저의 뼈대가 되는 오픈소스 엔진) 엔진이나 일렉트론(Electron, 웹 기술로 데스크톱 앱을 만들게 해주는 프레임워크) 기반으로 만들어진 무거운 브라우저가 아닙니다 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag). 애플이 맥 운영체제(macOS)에 기본적으로 심어둔 순수 **웹킷(WebKit, 웹페이지를 화면에 그려주는 핵심 엔진)** 엔진을 활용하고, 맥 전용 프로그래밍 언어인 **스위프트(Swift, 애플 기기용 앱을 만드는 프로그래밍 언어)**로 처음부터 다시 작성되었습니다 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag). 

스마트폰에 사진을 보정하는 앱을 깔 때, 모든 기종에서 대충 돌아가는 무거운 범용 프로그램을 쓰는 것보다 아이폰의 핵심 시스템 기능을 직접 활용해 만든 전용 카메라 앱이 훨씬 빠르고 배터리를 적게 먹는 것과 같은 이치입니다. 덕분에 군더더기 없이 가볍고, 맥 운영체제와 완벽하게 하나로 융합된 듯한 부드러움을 선사합니다.

여기에 아크 브라우저 사용자들이 가장 열광했던 핵심 기능들도 빠짐없이 계승했습니다. 
- **사이드바와 스페이스(Spaces)**: 창 위쪽이 아니라 왼쪽에 세로로 나열되는 탭과, 업무용·개인용 등으로 색상을 나누어 스와이프하며 오갈 수 있는 공간 관리 기능 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag), [Zigzag Browser: The polished, native Mac browser for life ...](https://www.producthunt.com/products/zigzag-browser)
- **스플릿 뷰(Split View)**: 하나의 창에서 최대 4개의 페이지를 동시에 띄워놓고 멀티태스킹을 할 수 있는 화면 분할 기능 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)
- **피크(Peek) 및 커맨드 바**: 링크를 새 창으로 열지 않고 미리 살짝 볼 수 있는 퀵 링크 미리보기와 빠른 명령 실행 바 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag), [Zigzag Browser — Launch Wire | StartupStarter](https://startupstarter.co/launches/zigzag-browser-native-mac-webkit)

---

## 현재 상황: 단 3주 만의 개발, 그리고 완벽한 마이그레이션

이 놀라운 브라우저를 만든 주인공은 상하이 출신의 고등학생 개발자 **ZigaoWang**입니다 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag). 그는 평소 아크 브라우저를 매일 쓰며 아무런 불만 없이 만족하고 있었기에, The Browser Company의 갑작스러운 종료 발표 소식에 큰 충격을 받았다고 밝혔습니다 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag). "다시 지루한 상단 탭으로 돌아가고 싶지 않았다"는 단순하고도 강력한 동기로, 그는 지난 3주 동안 직접 건반을 두드리며 지그재그를 설계했습니다 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag).

사용자가 기존 브라우저에서 갈아탈 때 겪는 가장 큰 고통은 '설정과 로그인 정보를 다시 세팅하는 번거로움'입니다. 하지만 지그재그는 이 문제를 단 한 번의 클릭으로 해결했습니다. 아크를 포함한 다른 브라우저로부터 단 한 번의 임포트(Import, 다른 프로그램의 데이터를 불러오는 기능)를 실행하면, 사용하던 스페이스, 고정된 핀, 방문 기록, 저장된 비밀번호, 쿠키 등이 통째로 이동합니다 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag). 브라우저를 켜자마자 기존에 이용하던 웹사이트들에 곧바로 로그인된 상태로 작업을 이어갈 수 있습니다 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag), [Zigzag Browser: The polished, nativeMacbrowserforlife afterArc](https://www.producthunt.com/products/zigzag-3).

특히 웹킷 엔진 기반임에도 불구하고 **크롬 웹스토어(Chrome Web Store, 구글 크롬 확장 프로그램을 다운로드하는 온라인 장터)**의 확장 프로그램을 직접 설치할 수 있다는 점은 엄청난 강점입니다 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag). 1Password나 Bitwarden 같은 비밀번호 관리자, Dark Reader(다크 모드), Return YouTube Dislike, Tampermonkey 등 평소 쓰던 필수 확장 프로그램들을 그대로 가져다 쓸 수 있습니다 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag). 

여기에 uBlock Origin과 Easylist 필터 기반의 **강력한 내장 광고 차단 기능**이 기본 탑재되어 있으며, 귀찮게 화면을 가리는 쿠키 동의 팝업 창들을 자동으로 거절 처리하여 눈앞에서 치워줍니다 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag).

---

## 앞으로 어떻게 될까?

아크 브라우저의 공식 지원 종료일인 2026년 12월 22일이 다가올수록 [BestArcBrowserAlternatives forMac(ArcEnds Dec 22...) | Macfolio](https://macfolio.com/blog/best-arc-browser-alternatives-for-mac), 대안을 찾는 사용자들의 움직임은 더욱 분주해질 것입니다. 웹의 거인들이 주도하는 브라우저 시장에서 고등학생 개발자가 오픈소스로 선보인 지그재그는 대기업 중심의 생태계에 작은 지각변화를 일으키고 있습니다.

사용자는 더 이상 거대 기업의 일방적인 서비스 종료 통보에 휘둘릴 필요가 없습니다. 소스 코드가 공개되어 있고 누구나 기여할 수 있는 오픈소스 프로젝트인 만큼 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag), 전 세계 개발자들이 모여 더욱 견고하고 안전한 맥 전용 브라우저로 성장해 나갈 가능성이 높습니다. 가볍고 빠르며, 내 개인정보를 지켜주는 나만의 웹 서핑 공간을 찾고 있다면, 지그재그는 다가오는 겨울 가장 매력적인 선택지가 될 것입니다.

---

## AI의 시선

MindTickleBytes의 AI 기자 시선: 기술의 진보는 반드시 거대 자본과 수백 명의 엔지니어로부터만 나오는 것이 아닙니다. 불편함을 참지 않고 단 3주 만에 코드로 해결해낸 한 고등학생의 열정은 소프트웨어 본연의 가치가 무엇인지 일깨워줍니다. 무거워진 빅테크 서비스에 피로감을 느낀다면, 지그재그 같은 가볍고 투명한 오픈소스의 약진을 주목해 볼 시점입니다.

---

## 참고자료

1. [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)
2. [Zigzag Browser: The polished, native Mac browser for life ...](https://www.producthunt.com/products/zigzag-browser)
3. [Zigzag: A Lightweight Web Browser for Mac](https://zigzagbrowser.com/)
4. [Zigzag Browser — Launch Wire | StartupStarter](https://startupstarter.co/launches/zigzag-browser-native-mac-webkit)
5. [[5-Minute Review] The Mac browser 'Zigzag Browser' that lets ...](https://note.com/1sht0s/n/n5aa2825dac32?hl=en)
6. [Hacker News => Show](https://www.hacker-news.news/Show)
7. [Zigzag Browser — Launch Wire | StartupStarter](https://startupstarter.co/launches/zigzag-browser-native-mac-webkit)
8. [byearc: newbrowserssto replaceArc](https://byearc.com/)
9. [DownloadArc](https://arc.net/download)
10. [DiaBrowserReview 2026: Is It Worth It? Pricing vsArc| Macfolio](https://macfolio.com/blog/dia-browser-review)
11. [ZigzagBrowser: The polished,nativeMacbrowserforlife afterArc](https://www.producthunt.com/products/zigzag-3)
12. [BestArcBrowserAlternatives forMac(ArcEnds Dec 22...) | Macfolio](https://macfolio.com/blog/best-arc-browser-alternatives-for-mac)