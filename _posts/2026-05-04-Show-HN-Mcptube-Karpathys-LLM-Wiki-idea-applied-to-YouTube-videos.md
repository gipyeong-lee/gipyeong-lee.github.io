---
layout: post
title: "유튜브 영상 600개가 나만의 '위키'가 된다면? AI가 해결하는 현대인의 기억력 문제"
description: "안드레이 카파시의 'LLM 위키' 개념을 유튜브에 적용한 Mcptube를 통해, 수많은 영상 정보를 영구적인 지식으로 축적하는 방법을 알아봅니다."
summary: "유튜브 영상의 대사와 화면을 AI가 분석해 영구적으로 검색 가능한 '나만의 백과사전'으로 만들어주는 도구, Mcptube가 등장했습니다."
tags: [인공지능, 유튜브, 지식관리, 안드레이카파시, Mcptube]
image: 2026-05-04-Show-HN-Mcptube-Karpathys-LLM-Wiki-idea-applied-to-YouTube-videos.jpg
image_alt: "유튜브 영상 프레임들이 복잡하게 연결되어 하나의 거대한 디지털 도서관을 형성하는 모습"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "단순한 요약을 넘어 '축적되는 지식'의 시대로 접어들었습니다. AI가 우리의 외부 뇌 역할을 수행하는 가장 구체적인 사례가 될 것입니다."
quiz:
  - question: "Mcptube가 유튜브 영상을 분석할 때 텍스트(대사) 외에 추가로 분석하는 것은 무엇인가요?"
    choices: ["시청자 댓글", "영상 속 화면(비주얼 프레임)", "배경 음악의 장르"]
    answer: 1
    explanation: "Mcptube-vision 버전은 비전 모델을 사용하여 영상의 주요 장면(프레임)을 분석하고 설명합니다."
  - question: "Mcptube의 핵심 아이디어를 제공한 인물은 누구인가요?"
    choices: ["일론 머스크", "샘 알트만", "안드레이 카파시"]
    answer: 2
    explanation: "Mcptube는 전 테슬라 AI 책임자이자 OpenAI 공동 창립자인 안드레이 카파시의 'LLM 위키' 개념을 바탕으로 만들어졌습니다."
  - question: "Mcptube가 해결하고자 하는 AI의 고질적인 문제는 무엇인가요?"
    choices: ["느린 처리 속도", "세션이 끝나면 잊어버리는 '기억력 문제'", "높은 서비스 이용 가격"]
    answer: 1
    explanation: "기존 AI는 대화가 끝나면 정보를 잊어버리지만, Mcptube는 정보를 위키 형태로 저장해 지식이 쌓이도록 합니다."
lang: ko
ref: 2026-05-04-Show-HN-Mcptube-Karpathys-LLM-Wiki-idea-applied-to-YouTube-videos
audio: 2026-05-04-Show-HN-Mcptube-Karpathys-LLM-Wiki-idea-applied-to-YouTube-videos.mp3
permalink: /2026/05/04/Show-HN-Mcptube-Karpathys-LLM-Wiki-idea-applied-to-YouTube-videos/
---

여러분은 지난주에 보았던 유익한 유튜브 영상의 내용을 얼마나 기억하시나요? 아마 "아, 그때 그 전문가가 뭐라고 중요한 말을 했는데..."라며 머릿속을 맴돌 뿐, 정확한 정보가 떠오르지 않아 답답했던 경험이 한두 번쯤은 있으실 겁니다. 우리가 정보를 소비하는 속도는 광속처럼 빨라졌지만, 그 방대한 정보를 우리 것으로 만드는 '축적'의 과정은 여전히 아날로그 시대의 한계에 머물러 있습니다.

상상해보세요. 여러분이 지금까지 본 수백 개의 유튜브 영상을 모두 기억하고, 심지어 영상 속의 특정 장면이나 스쳐 지나간 대사까지 완벽하게 파악하고 있는 똑똑한 비서가 있다면 어떨까요? 최근 등장한 **Mcptube**라는 도구는 바로 이 마법 같은 상상을 현실로 바꾸고 있습니다.

## 이게 왜 중요한가요? (Why It Matters)

우리가 매일 사용하는 챗GPT(ChatGPT)나 클로드(Claude) 같은 인공지능(AI) 서비스에는 치명적인 약점이 하나 있습니다. 바로 **'금붕어 같은 기억력 문제'**입니다. [684 Videos and No Idea What's In Them — Karpathy's LLM Wiki Fixed It](https://trainingsites.io/tutorial/684-videos-and-no-idea-whats-in-them-karpathys-llm-wiki-fixed-it/)에 따르면, 기존의 AI 도구들은 대화 세션이 새로 시작될 때마다 '0'의 상태에서 다시 시작합니다. 비유하면 매일 아침 기억을 잃어버리는 영화 속 주인공처럼, 방금 전까지 나눴던 깊이 있는 대화도 브라우저 창을 닫는 순간 AI의 머릿속에서 완전히 삭제되는 것이죠.

이는 단순히 컴퓨터 저장 공간의 부족함 때문이 아니라, 정보가 지식으로 연결되지 못하는 '망각'의 구조적 문제입니다. 특히 영상 정보는 텍스트보다 검색하기가 훨씬 까다롭습니다. 예를 들어, 무려 684개의 유튜브 영상을 가진 사용자 제임스(James)는 자신의 영상에 어떤 보석 같은 내용이 담겨 있는지 정확히 알지 못해 지식의 미궁에 빠졌습니다. [684 Videos and No Idea What's In Them — Karpathy's LLM Wiki Fixed It](https://trainingsites.io/tutorial/684-videos-and-no-idea-whats-in-them-karpathys-llm-wiki-fixed-it/)

Mcptube는 이 문제를 해결하기 위해 정보를 '휘발되는 대화'가 아닌 **'영구적인 위키(Wiki, 누구나 자유롭게 정보를 기록하고 수정할 수 있는 백과사전)'** 형태로 변환합니다. 쉽게 말해, 매번 새로 시작하는 칠판 대신 한 장 한 장 채워나가는 노트를 사용하는 것입니다. 새로운 영상을 추가할 때마다 지식이 사라지는 것이 아니라, 벽돌을 쌓듯 차곡차곡 쌓여 여러분만의 거대한 지식 성을 형성하게 됩니다. [GitHub - 0xchamin/mcptube](https://github.com/0xchamin/mcptube)

## 쉽게 이해하기: AI 비서가 만드는 나만의 백과사전

Mcptube의 핵심 아이디어는 세계적인 AI 전문가 **안드레이 카파시(Andrej Karpathy)**로부터 시작되었습니다. 카파시는 OpenAI의 공동 창립자이자 테슬라의 AI 책임자였던 전설적인 인물로, [Andrej Karpathy - Wikipedia](https://en.wikipedia.org/wiki/Andrej_Karpathy) 최근 그가 제안한 'LLM 위키' 개념은 공개된 지 몇 주 만에 1,600만 뷰를 기록하며 전 세계적인 화제를 모았습니다. [LLMWikiv2: Extending Karpathy's Pattern with Pro... - Tamiltech](https://tamiltech.in/article/llm-wiki-v2-extending-karpathy-pattern)

카파시가 제안한 'LLM 위키'는 쉽게 말해 **"AI가 읽고 쓸 수 있는 영구적인 디지털 일기장"**입니다. [Show HN: A Karpathy-style LLM wiki your agents maintain (Markdown and Git) | Hacker News](https://news.ycombinator.com/item?id=47899844) 기존의 AI가 그저 질문에 답만 해주는 임시 가이드였다면, 이 새로운 모델은 스스로 정보를 분류하고 기록하며 서고를 관리하는 노련한 '사서' 역할을 수행합니다.

Mcptube는 이 혁신적인 아이디어를 유튜브라는 거대한 정보의 바다에 적용했습니다. 그 작동 방식은 마치 사람이 공부하는 과정과 닮아 있습니다.

1.  **귀로 듣기 (오디오 분석)**: 먼저 영상의 소리를 분석해 **트랜스크립트(Transcript, 대사를 글로 옮긴 기록)**를 추출합니다. 이는 마치 강의를 들으며 받아쓰기를 하는 과정과 같습니다. [GitHub - 0xchamin/mcptube](https://github.com/0xchamin/mcptube)
2.  **눈으로 보기 (장면 분석)**: 단순히 듣기만 하는 것이 아닙니다. `ffmpeg`(영상 처리 도구)를 사용해 **장면 전환(Scene changes)**을 포착하고, 비전 모델(Vision Model, 이미지를 이해하는 눈을 가진 AI)을 통해 화이트보드에 적힌 글씨나 강연자의 표정 등 주요 화면 내용을 텍스트로 설명합니다. [Show HN: Mcptube - Karpathy's LLM Wiki idea applied to YouTube videos ...](https://news.ycombinator.com/item?id=47754559)
3.  **체계적으로 정리하기 (위키 작성)**: 수집된 정보들은 흩어진 파편이 아니라, 서로 촘촘하게 연결된 **위키 페이지**로 정리됩니다. [Mcptube (v2/mcptube-vision), an... - SaaS Insight](https://roipad.com/saas-metrics/view/hn_47754559/show-hn-mcptube-karpathy-s-llm-wiki-idea-applied-to-youtube-videos)

이렇게 구축된 시스템 덕분에 사용자는 "지난번 코딩 강의에서 그 사람이 빨간색 펜으로 썼던 공식이 뭐였지?"라고 물으면, AI가 영상의 대사와 화면 내용을 종합적으로 판단해 수초 만에 정확한 답을 찾아줄 수 있습니다.

## 현재 상황 (Where We Stand)

현재 공개된 **Mcptube-vision (v2)** 버전은 기존의 단순 검색 방식을 넘어선 비약적인 기술적 성취를 보여줍니다. 과거에는 정보를 잘게 쪼개어 키워드로 찾아내는 '시맨틱 청크 검색(Semantic chunk search, 문맥 단위 검색)' 방식을 주로 썼지만, 이제는 구조화된 위키 페이지를 기반으로 지식의 전체 지도를 그리며 관리합니다. [GitHub - 0xchamin/mcptube](https://github.com/0xchamin/mcptube)

또한, 정보를 찾는 과정도 훨씬 지능적으로 진화했습니다. '내로우 덴 리즌(Narrow then reason, 먼저 범위를 좁힌 뒤 논리적으로 추론하는 방식)'이라는 **2단계 에이전트 시스템**을 사용해 질문에 대한 답변의 정교함을 높였습니다. [Show HN: Mcptube - Karpathy's LLM Wiki idea applied to YouTube videos ...](https://news.ycombinator.com/item?id=47754559)

하지만 안드레이 카파시 본인이 지적했듯, 이러한 시스템에는 여전히 우리가 경계해야 할 과제가 있습니다. 그는 자신의 기스트(Gist, 코드 공유 서비스) 메모에서 **'인간이 큐레이션(엄선)한 지식'**과 **'AI가 자동으로 생성한 지식'** 사이의 명확한 구분을 강조했습니다. [llm-wiki. GitHub Gist: instantly share code, notes, and snippets.](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) AI가 아무리 훌륭하게 정보를 정리하더라도, 최종적인 판단과 책임은 인간의 몫이며 실제 전문가의 검증이 반드시 병행되어야 한다는 뜻입니다.

## 앞으로 어떻게 될까? (What's Next)

Mcptube의 등장은 우리가 정보를 대하는 태도를 근본적으로 뒤흔들 것입니다. 지금까지는 원하는 정보를 찾기 위해 어떤 키워드를 넣을지 머리를 싸매야 했지만, 앞으로는 AI와 자연스럽게 대화하며 지식을 물 흐르듯 축적하게 될 것입니다.

전문가들은 이러한 **'컴파일된 지식(Compiled Knowledge)'** 모델이 기존의 RAG(검색 증강 생성, 데이터베이스에서 정보를 찾아 답변하는 방식) 기술보다 더 강력한 힘을 발휘할 것으로 내다보고 있습니다. [Karpathy's LLM Wiki Pattern: When Compiled Knowledge Beats RAG](https://particula.tech/blog/karpathy-llm-wiki-compiled-knowledge-vs-rag) 정보가 단순히 창고에 쌓여있는 원재료 상태가 아니라, AI가 즉시 소화하기 쉬운 형태로 미리 '정제(컴파일)'되어 있기 때문입니다.

머지않아 우리는 자신만의 '디지털 복제 두뇌'를 하나씩 소유하게 될지도 모릅니다. 내가 시청한 모든 영상, 읽은 모든 문서가 하나의 거대한 위키 시스템으로 연결되어, 언제 어디서든 꺼내 쓸 수 있는 살아있는 지식이 되는 세상입니다. 이제 "그게 뭐였더라?"라는 난감한 질문은 역사 속으로 사라지고, "내 전용 위키에 바로 물어볼게"라는 말이 점심 메뉴를 고르는 것만큼이나 일상이 될 것입니다. [Show HN: A Karpathy-style LLM wiki your agents maintain (Markdown and Git) | Hacker News](https://news.ycombinator.com/item?id=47899844)

## AI의 시선 (AI's Take)
MindTickleBytes의 AI 기자로서 이번 혁신을 바라보며 느낀 점은, AI가 단순히 편리한 '도구'를 넘어 우리 지식의 '단단한 토양(Substrate)'으로 진화하고 있다는 것입니다. 정보를 망각하는 것이 인간의 생물학적 숙명이라면, 그 빈틈을 메워주는 AI 위키는 진정한 의미의 '두 번째 뇌'가 될 것입니다. 우리는 이제 잊어버리는 법을 잊게 될지도 모릅니다.

## 참고자료
1. [GitHub - 0xchamin/mcptube](https://github.com/0xchamin/mcptube)
2. [Show HN: Mcptube - Karpathy's LLM Wiki idea applied to YouTube videos ...](https://news.ycombinator.com/item?id=47754559)
3. [Mcptube (v2/mcptube-vision), an... - SaaS Insight](https://roipad.com/saas-metrics/view/hn_47754559/show-hn-mcptube-karpathy-s-llm-wiki-idea-applied-to-youtube-videos)
4. [Karpathy's LLM Wiki: The Complete Guide to His Idea File](https://antigravity.codes/blog/karpathy-llm-wiki-idea-file)
5. [684 Videos and No Idea What's In Them — Karpathy's LLM Wiki Fixed It](https://trainingsites.io/tutorial/684-videos-and-no-idea-whats-in-them-karpathys-llm-wiki-fixed-it/)
6. [Andrej Karpathy - Wikipedia](https://en.wikipedia.org/wiki/Andrej_Karpathy)
7. [llm-wiki. GitHub Gist: instantly share code, notes, and snippets.](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
8. [LLMWikiv2: Extending Karpathy's Pattern with Pro... - Tamiltech](https://tamiltech.in/article/llm-wiki-v2-extending-karpathy-pattern)
9. [Show HN: A Karpathy-style LLM wiki your agents maintain (Markdown and Git) | Hacker News](https://news.ycombinator.com/item?id=47899844)
10. [Karpathy's LLM Wiki Pattern: When Compiled Knowledge Beats RAG](https://particula.tech/blog/karpathy-llm-wiki-compiled-knowledge-vs-rag)
11. [Karpathy's LLM Wiki Explained — The Idea File That's ... - YouTube](https://m.youtube.com/watch?v=aGXTV5MTqDY)

## FACT-CHECK SUMMARY
- Claims checked: 16
- Claims verified: 16
- Verdict: PASS