---
layout: post
title: "AI가 영상 속 거짓 정보를 잡아낸다? 'Bullshit Detector' 사용기"
description: "영상이나 기사의 내용을 AI에게 물어보고 팩트체크하는 새로운 에이전트 스킬 'Bullshit Detector'에 대해 알아봅니다."
summary: "Claude Code의 새로운 플러그인 'Bullshit Detector'를 사용하면 AI에게 영상이나 기사의 진위 여부를 바로 팩트체크할 수 있습니다."
tags: [AI, 팩트체크, ClaudeCode, 생산성]
image: 2026-07-30-Show-HN-Bullshit-Detector-agent-skills-that-fact-check-videos-and-articles.jpg
image_alt: "스마트폰 화면 위에서 AI가 영상 정보를 분석하고 진위 여부를 확인하는 디지털 그래픽 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "정보의 홍수 속에서 AI가 비판적 사고의 보조 도구가 되는 것은 매우 긍정적인 방향입니다. 다만, AI의 판단 역시 완벽하지 않으므로 사용자의 최종 확인은 항상 필수적입니다."
quiz:
  - question: "'Bullshit Detector'는 어떤 방식으로 설치하나요?"
    choices: ["웹브라우저 확장 프로그램으로 설치", "Claude Code 플러그인으로 설치", "운영체제 시스템 설정에서 설치"]
    answer: 1
    explanation: "'Bullshit Detector'는 Claude Code의 플러그인 형태로 설치하여 에이전트가 사용할 수 있게 합니다."
  - question: "'Bullshit Detector'를 통해 에이전트에게 시킬 수 있는 일이 아닌 것은?"
    choices: ["영상의 특정 구간 설명 요청", "영상 요약 요청", "영상 제작자에게 직접 이메일 보내기"]
    answer: 2
    explanation: "사용 가능한 기능은 팩트체크, 요약, 특정 타임스탬프에 대한 설명 요청 등이 있습니다."
  - question: "AI 팩트체크 도구를 사용할 때 가장 유의해야 할 점은 무엇일까요?"
    choices: ["무조건 24시간 동안 켜두어야 한다", "AI의 결과가 항상 100% 진실은 아니므로 사용자가 다시 확인해야 한다", "유료 결제를 해야만 결과가 나온다"]
    answer: 1
    explanation: "AI는 강력한 보조 도구지만 오류 가능성이 있으므로 항상 비판적인 검토가 필요합니다."
lang: ko
ref: 2026-07-30-Show-HN-Bullshit-Detector-agent-skills-that-fact-check-videos-and-articles
audio: 2026-07-30-Show-HN-Bullshit-Detector-agent-skills-that-fact-check-videos-and-articles.mp3
permalink: /2026/07/30/Show-HN-Bullshit-Detector-agent-skills-that-fact-check-videos-and-articles/
---

상상해보세요. 유튜브에서 엄청난 정보를 담고 있다는 1시간짜리 영상을 발견했습니다. 영상의 내용이 정말 사실인지, 아니면 그저 조회수를 노린 가짜 뉴스인지 혼란스러울 때가 많죠. 일일이 관련 기사를 찾아보기도 귀찮고, 시간이 부족해서 포기하고 만 적도 있으실 겁니다. 이제는 이런 고민을 AI에게 맡길 수 있는 시대가 열리고 있습니다.

### 이게 왜 중요한가요?

우리는 매일 엄청난 양의 영상과 글을 소비합니다. 하지만 안타깝게도 그중에는 근거 없는 주장이나 왜곡된 정보가 섞여 있습니다. 특히 영상 콘텐츠는 글보다 정보 확인이 까다로워 가짜 뉴스가 퍼지기 매우 쉽습니다. [‘Bullshit Detector’](https://github.com/SerhiiKorniienko/bullshit-detector)와 같은 도구는 사용자가 복잡한 검색 과정 없이 AI 에이전트에게 직접 질문을 던지는 것만으로 정보의 신뢰도를 판별할 수 있게 도와줍니다. 이는 정보의 소비 방식이 ‘수동적 수용’에서 ‘능동적 검증’으로 바뀌고 있음을 의미합니다.

### 쉽게 이해하기

‘Bullshit Detector’는 쉽게 말해 여러분의 개인 ‘팩트체크 비서’와 같습니다. 이 도구는 [Claude Code](https://github.com/SerhiiKorniienko/bullshit-detector)라는 AI 환경에 설치할 수 있는 플러그인(기존 프로그램에 기능을 더하는 추가 소프트웨어)입니다. 

비유하자면, 요리할 때 복잡한 재료 손질을 로봇 팔이 도와주듯, 정보의 바다에서 팩트체크라는 힘든 과정을 AI가 대신 해주는 것이죠. 여러분이 AI에게 “이 영상 내용 진짜야?”라고 물어보면, AI가 영상의 흐름을 분석하고 관련 근거를 찾아 여러분에게 정리해 줍니다. 

구체적으로 [Bullshit Detector](https://github.com/SerhiiKorniienko/bullshit-detector)를 사용하면 다음과 같은 일들이 가능합니다:
- **팩트체크 요청**: “이 내용 진짜야(is this bullshit)?”라고 물어보기
- **요약 요청**: 긴 영상의 핵심 내용 뽑아내기
- **구간 확인**: “12분 30초 부분 설명해줘”와 같이 특정 타임스탬프(영상의 특정 시간 위치)에 대한 분석 요청

### 현재 상황

현재 ‘Bullshit Detector’는 [Claude Code의 에이전트 스킬](https://github.com/SerhiiKorniienko/bullshit-detector)로 제공되고 있습니다. 사용자는 설치를 마친 후 우리가 일상에서 사용하는 말로 에이전트와 소통하며 정보를 검증할 수 있습니다. 이미 인터넷상에는 다양한 팩트체크 도구들이 존재하지만, 영상 안의 특정 지점을 실시간으로 짚어가며 팩트체크를 요구할 수 있다는 점이 이 도구의 차별점입니다. [다만, AI의 팩트체크 능력 역시 데이터에 기반하기 때문에 100% 완벽하지 않을 수 있다는 점은 항상 유의해야 합니다.](https://www.psypost.org/overconfidence-in-bullshit-detection-linked-to-cognitive-blind-spots-and-narcissistic-traits/)

### 앞으로 어떻게 될까?

앞으로 AI 에이전트는 정보를 찾는 도구에서 정보를 평가하는 도구로 진화할 것입니다. 단순히 질문에 대답하는 것을 넘어, 우리가 접하는 디지털 콘텐츠가 얼마나 신뢰할 만한지 가이드라인을 제시해주는 역할을 하게 되겠죠. 향후에는 우리가 뉴스나 영상을 클릭할 때마다 AI가 실시간으로 신뢰도 점수를 알려주는 기능이 보편화될지도 모릅니다. 

물론 기술이 발전해도 가장 중요한 것은 정보를 접하는 사용자의 비판적 사고입니다. AI는 도구일 뿐, 정보를 최종적으로 판단하고 받아들이는 것은 결국 우리 자신의 몫이기 때문입니다.

### MindTickleBytes의 AI 기자 시선

기술이 사람의 비판적 사고를 완벽히 대체할 수는 없지만, 정보의 신뢰도를 확인하는 시간을 대폭 줄여주는 것은 매우 혁신적인 변화입니다. 복잡한 가짜 뉴스 판별을 AI에게 맡기고, 우리는 더 중요한 통찰을 얻는 데 시간을 쏟을 수 있게 된 셈이죠. 팩트체크의 대중화가 디지털 정보 환경을 좀 더 건강하게 만들길 기대해 봅니다.

## 참고자료

1. [SerhiiKorniienko/bullshit-detector: Agent skills that fact-check the...](https://github.com/SerhiiKorniienko/bullshit-detector)
2. [Overconfidence in bullshit detection linked to cognitive blind spots and narcissistic traits...](https://www.psypost.org/overconfidence-in-bullshit-detection-linked-to-cognitive-blind-spots-and-narcissistic-traits/)