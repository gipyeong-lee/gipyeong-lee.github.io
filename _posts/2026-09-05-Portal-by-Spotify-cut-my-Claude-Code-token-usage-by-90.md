---
layout: post
title: "AI 코딩 비서에게 '잔심부름'만 시켰더니, 비용이 90% 줄었다고?"
description: "스포티파이가 공개한 '포털(Portal)' 기술을 통해 AI 코딩 에이전트의 토큰 비용을 획기적으로 절감하는 방법을 알아봅니다."
summary: "스포티파이가 오픈소스 기술 '포털(Portal)'과 AiKA 모드를 활용해 AI 코딩 에이전트의 반복적인 단순 업무를 저렴한 모델로 위임함으로써 토큰 사용량을 90% 절감했습니다."
tags: [AI, 코딩, 스포티파이, 비용절감, 효율화]
image: 2026-09-05-Portal-by-Spotify-cut-my-Claude-Code-token-usage-by-90.jpg
image_alt: "코딩 에이전트와 코드베이스 사이에서 효율적인 경로를 찾아주는 데이터 흐름을 형상화한 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "복잡한 추론이 필요 없는 단순 작업까지 최고급 AI 모델에게 맡기는 것은 비효율적입니다. 이 기술은 AI 활용의 '가성비'를 최적화하는 현명한 접근입니다."
quiz:
  - question: "스포티파이가 AI 코딩 에이전트 비용을 줄이기 위해 도입한 핵심 기술의 이름은 무엇인가요?"
    choices: ["Claude Code", "Portal", "AiKA"]
    answer: 1
    explanation: "스포티파이는 AI 코딩 에이전트와 코드베이스 사이에 위치하는 지식 그래프 레이어인 '포털(Portal)'을 공개했습니다."
  - question: "포털의 AiKA 모드에서 수행하는 'code-writer'의 주요 역할은 무엇인가요?"
    choices: ["코드베이스 전체 분석", "패턴 기반의 코드 생성", "사용자 문서 업데이트"]
    answer: 1
    explanation: "code-writer 모드는 기존 패턴을 따라 반복적인 코드를 생성하는 작업을 담당합니다."
  - question: "단순 반복 업무를 저렴한 모델로 위임함으로써 얻은 토큰 사용량 절감률은 얼마인가요?"
    choices: ["50%", "70%", "90%"]
    answer: 2
    explanation: "반복적이고 I/O(입출력)가 많은 작업을 Gemini 2.5 Flash와 같은 저렴한 모델로 라우팅하여 토큰 사용량을 90% 절감했습니다."
lang: ko
ref: 2026-09-05-Portal-by-Spotify-cut-my-Claude-Code-token-usage-by-90
audio: 2026-09-05-Portal-by-Spotify-cut-my-Claude-Code-token-usage-by-90.mp3
permalink: /2026/09/05/Portal-by-Spotify-cut-my-Claude-Code-token-usage-by-90/
---

상상해보세요. 아주 똑똑한 박사님 한 분을 개인 비서로 채용했습니다. 그런데 이 박사님에게 매일 아침 '복사기 버튼 누르기'나 '서류 분류해서 파일에 꽂기' 같은 아주 단순한 잡무만 시키고 있다면 어떨까요? 월급은 박사님 대우로 드리면서 말이죠.

최근 개발자들 사이에서 큰 화제가 된 'AI 코딩 에이전트'의 상황이 딱 이렇습니다. 아주 뛰어난 지능을 가진 AI에게 코딩을 맡겼더니, 정작 고도의 논리적 사고가 필요한 문제 해결보다는 단순하게 파일을 읽고 쓰는 '잔심부름'에 더 많은 비용을 쓰고 있었던 것이죠. 여기서 비용이란 AI가 문장을 이해하고 처리할 때마다 지불하는 '토큰(AI의 연산 단위를 세는 말)' 비용을 의미합니다. 이 비효율적인 상황을 타개하기 위해 스포티파이(Spotify) 엔지니어들이 새로운 해결책을 내놓았습니다.

## 이게 왜 중요한가요?

AI 기술이 급성장하면서 많은 개발자가 Claude Code와 같은 AI 코딩 에이전트를 통해 업무 생산성을 크게 높이고 있습니다. 하지만 여기엔 치명적인 걸림돌이 하나 있습니다. 바로 '비용'입니다. AI가 아주 복잡한 논리 문제를 풀 때 사용하는 최고 성능의 모델, 이른바 '프런티어 모델'은 성능이 뛰어난 만큼 사용료가 매우 비쌉니다.

문제는 이 똑똑한 AI가 단순한 파일을 여러 번 읽거나, 이미 수십 번 작성해본 것과 똑같은 형식의 테스트 코드를 짤 때도 똑같이 비싼 요금을 부과한다는 점입니다. 스포티파이의 이번 사례는 AI를 단순히 '쓰는' 단계를 넘어, **어떤 일을 어떤 등급의 AI에게 맡겨야 가장 경제적이고 효율적인지**를 보여주는 중요한 전환점이 될 것입니다. 이는 개발자의 생산성을 유지하면서도 운영 비용을 획기적으로 낮출 수 있는 현실적인 길을 제시합니다 [[출처 1](https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90)].

## 쉽게 이해하기: '똑똑한 교통 정류장'

스포티파이는 '포털(Portal)'이라는 기술을 공개했습니다 [[출처 6](https://www.youtube.com/watch?v=TfZsMjB9PMo)]. 쉽게 비유하자면, 포털은 AI 에이전트와 코드(코드베이스) 사이에 놓인 **'똑똑한 교통 정류장'**과 같습니다. 기존에는 AI가 무작정 코드 곳곳을 뒤지며 모든 내용을 읽느라 토큰을 낭비했습니다 [[출처 9](https://getpushtoprod.substack.com/p/how-to-reduce-90-of-claude-code-token)]. 

스포티파이는 여기서 'AiKA 모드'라는 두 가지 특별한 직원을 고용해 업무를 분담시켰습니다 [[출처 11](https://github.com/spotify/portal-ai-plugins)]. 

1. **bulk-reader(대량 읽기 담당)**: 여러 파일을 분석해야 할 때, 비싼 AI를 쓰지 않고 성능은 적당하지만 비용이 매우 저렴한 'Gemini 2.5 Flash' 모델에게 일을 시킵니다 [[출처 2](https://yomu.fyi/post/portal-by-spotify-cut-my-claude-code-token-usage-by-90)]. 
2. **code-writer(코드 작성 담당)**: 기존 코드 패턴을 따라 반복적인 코드를 짤 때도 마찬가지로 저렴한 모델에게 맡깁니다 [[출처 2](https://yomu.fyi/post/portal-by-spotify-cut-my-claude-code-token-usage-by-90)]. 

'shunt(분기)'라는 이름의 플러그인을 설치하면, 비싼 고성능 AI 모델은 정말 머리가 필요한 '창의적인 문제 해결'에만 집중하고, 나머지 단순 반복 노동은 저렴한 AiKA 모델들이 나누어 처리하게 됩니다 [[출처 4](https://www.linkedin.com/posts/spotify-for-backstage_portal-by-spotify-cut-my-claude-code-token-activity-7501610054891274241-y4Db), [출처 11](https://github.com/spotify/portal-ai-plugins)]. 

## 현재 상황

이미 많은 개발자가 AI 에이전트를 사용하며 매달 발생하는 막대한 토큰 비용에 부담을 느끼고 있습니다 [[출처 12](https://www.youtube.com/watch?v=UslVzxAkiZ0)]. 스포티파이의 이번 시도는 단순히 이론에 그치지 않고, 실제로 코딩 에이전트의 토큰 사용량을 **90%나 줄이는 놀라운 결과**를 낳았습니다 [[출처 3](https://zeli.app/story/49571465), [출처 14](https://news.ycombinator.com/item?id=49571465)]. 

현재 이 기술은 오픈소스로 공개되어 누구나 활용할 수 있는 상태이며, 주로 Claude Code 환경에서 파일 입출력(I/O)이 많은 작업을 최적화하는 데 활발히 사용되고 있습니다 [[출처 6](https://www.youtube.com/watch?v=TfZsMjB9PMo), [출처 11](https://github.com/spotify/portal-ai-plugins)]. 

## 앞으로 어떻게 될까?

앞으로는 단순히 '어떤 AI가 더 똑똑한가'를 넘어, **'어떤 AI를 어떻게 배치할 것인가'**가 진정한 경쟁력이 될 것입니다. 스포티파이의 포털처럼 복잡한 시스템 내부를 지식 그래프(데이터 간의 관계를 시각화한 형태) 형태로 관리하고, 작업의 성격에 따라 모델을 자동으로 배분하는 시스템들이 더 많이 등장할 것으로 보입니다.

개발자들은 이제 "AI에게 어떻게 지시할까?"를 고민하는 것을 넘어, "비싼 AI를 아끼고 싼 AI를 현명하게 활용하는 구조를 어떻게 설계할까?"를 고민해야 합니다. 똑똑한 AI를 더 현명하게 쓰기 위해, 이제는 효율적인 '분업'이 필요한 때입니다.

## MindTickleBytes의 AI 기자 시선
AI 활용의 성패는 이제 모델 그 자체의 성능이 아니라, 시스템 전반의 효율을 관리하는 '운용의 묘'에 달려 있습니다. 스포티파이의 사례는 최고 성능의 AI를 효율적으로 배치함으로써 비용은 낮추고 생산성은 극대화할 수 있음을 보여주는 가장 모범적인 답안지입니다.

## 참고자료
1. [Portal by Spotify cut my Claude Code token usage by 90%](https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90)
2. [Portal by Spotify cut my Claude Code token usage by 90%](https://yomu.fyi/post/portal-by-spotify-cut-my-claude-code-token-usage-by-90)
3. [Spotify's Portal cut my Claude Code · Hacker News | Zeli](https://zeli.app/story/49571465)
4. [Portal by Spotify cut my Claude Code token usage by 90% ...](https://www.linkedin.com/posts/spotify-for-backstage_portal-by-spotify-cut-my-claude-code-token-activity-7501610054891274241-y4Db)
5. [Spotify’s Backstage Portal cut my Claude Code… | VibeLeaderboard](https://www.vibeleaderboard.ai/intel/7ff05f2d-e1d9-4b86-aa58-8d94a5fccd5f)
6. [Spotify cut Claude Code token usage by 90% with Portal](https://www.youtube.com/watch?v=TfZsMjB9PMo)
9. [How to Reduce 90% of Claude Code Token Usage - by John Kim](https://getpushtoprod.substack.com/p/how-to-reduce-90-of-claude-code-token)
11. [GitHub - spotify/portal-ai-plugins · GitHub](https://github.com/spotify/portal-ai-plugins)
12. [How To Save 90% of Claude Code Token Usage - YouTube](https://www.youtube.com/watch?v=UslVzxAkiZ0)
14. [PortalbySpotifycutmyClaudeCodetokenusage... | HackerNews](https://news.ycombinator.com/item?id=49571465)