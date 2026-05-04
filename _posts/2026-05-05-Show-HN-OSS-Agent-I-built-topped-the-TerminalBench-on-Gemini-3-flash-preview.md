---
layout: post
title: "거대 기업 구글을 제친 '무명의 AI 기사', 터미널의 왕좌에 오르다"
description: "오픈소스 AI 에이전트 '디락(Dirac)'이 구글의 공식 기록을 깨고 터미널 벤치마크 1위를 차지한 비결과 이것이 우리 미래에 미칠 영향"
summary: "오픈소스 AI 에이전트 디락이 구글 제미나이 3를 탑재하고 컴퓨터 전문가들의 영역인 '터미널' 제어 시험에서 세계 1위 기록을 경신했습니다."
tags: [AI에이전트, 제미나이3, 오픈소스, 디락, 터미널벤치]
image: 2026-05-05-Show-HN-OSS-Agent-I-built-topped-the-TerminalBench-on-Gemini-3-flash-preview.jpg
image_alt: "검은색 터미널 화면 위로 빛나는 디지털 뇌가 복잡한 코드를 실시간으로 해결하고 있는 모습"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "거대 기업의 독점 기술보다 공개된 협력의 힘이 더 강력할 수 있음을 증명한 사건입니다. AI가 단순한 대화 상대를 넘어 '행동하는 도우미'로 진화하는 변곡점을 보여줍니다."
quiz:
  - question: "이번에 세계 기록을 경신한 오픈소스 AI 에이전트의 이름은 무엇인가요?"
    choices: ["제미나이 클리(Gemini CLI)", "디락(Dirac)", "주니 클리(Junie CLI)"]
    answer: 1
    explanation: "디락(Dirac)은 디락 델타 랩스의 맥스 트리베디가 개발한 오픈소스 AI 에이전트입니다."
  - question: "AI의 터미널 작업 능력을 평가하는 이번 시험의 이름은?"
    choices: ["터미널벤치 2.0(TerminalBench 2.0)", "제미나이 테스트", "해커뉴스 벤치마크"]
    answer: 0
    explanation: "터미널벤치(TerminalBench)는 AI가 명령줄 인터페이스에서 파일 관리나 스크립팅을 얼마나 잘 수행하는지 평가하는 기준입니다."
  - question: "디락이 이번 시험에서 기록한 정답률은 얼마인가요?"
    choices: ["47.8%", "64.3%", "65.2%"]
    answer: 2
    explanation: "디락은 65.2%의 성공률을 기록하여 구글의 공식 기록(47.8%)을 크게 앞질렀습니다."
lang: ko
ref: 2026-05-05-Show-HN-OSS-Agent-I-built-topped-the-TerminalBench-on-Gemini-3-flash-preview
audio: 2026-05-05-Show-HN-OSS-Agent-I-built-topped-the-TerminalBench-on-Gemini-3-flash-preview.mp3
permalink: /2026/05/05/Show-HN-OSS-Agent-I-built-topped-the-TerminalBench-on-Gemini-3-flash-preview/
---

상상해보세요. 여러분이 갑자기 복잡한 기계 장치로 가득한 거대한 공장의 제어실에 홀로 남겨졌습니다. 사방에는 수천 개의 스위치가 있고, 화면에는 이해할 수 없는 암호 같은 코드들이 쉴 새 없이 흘러갑니다. 이곳은 공장의 모든 것을 움직이는 심장부이지만, 아주 숙련된 기술자가 아니면 감히 손을 댈 엄두조차 나지 않는 두려운 공간이죠.

우리가 매일 사용하는 컴퓨터 안에도 이런 '비밀의 제어실'이 존재합니다. 바로 검은 화면에 흰 글자만 가득한 **터미널(Terminal, 명령어를 직접 입력해 컴퓨터를 제어하는 창)**입니다. 일반 사용자들은 예쁜 아이콘을 마우스로 클릭하며 컴퓨터를 쓰지만, 진짜 전문가들은 이 터미널이라는 도구를 통해 컴퓨터의 뼈대를 직접 움직이고 복잡한 시스템을 설계합니다.

그런데 최근, 이 전문가들만의 성역이었던 터미널에서 세상을 놀라게 한 사건이 벌어졌습니다. 구글(Google) 같은 거대 IT 기업이 만든 공식 AI를 제치고, 한 개인 개발자가 만든 '무명의 오픈소스 AI'가 세계에서 가장 똑똑한 터미널 전문가로 등극한 것입니다. 마치 골목 식당의 요리사가 미슐랭 3스타 셰프들의 요리 대결에서 당당히 우승을 차지한 것과 같은 반전입니다.

## 이게 왜 중요한가요? "말하는 AI에서 행동하는 AI로"

지금까지 우리가 만난 챗GPT나 제미나이 같은 AI들은 주로 '말'을 잘하는 존재였습니다. "시를 써줘", "영어를 번역해줘", "긴 글을 요약해줘" 같은 요청에는 아주 능숙했죠. 하지만 "내 컴퓨터에 엉망으로 흩어진 파일 1,000개를 내용별로 정리하고, 필요한 프로그램들을 알아서 설치해줘" 같은 실질적인 작업을 맡기기엔 아직 불안한 구석이 많았습니다.

이번에 화제가 된 **디락(Dirac)**이라는 이름의 AI 에이전트는 차원이 다릅니다. [Dirac OSS Agent Crushes Google's Baseline on TerminalBench](https://www.agent-wars.com/news/2026-04-27-show-hn-oss-agent-i-built-topped-the-terminalbench-on-gemini-3-flash-preview)에 따르면, 디락은 컴퓨터의 가장 깊숙한 곳인 터미널에 직접 접속해 복잡한 명령을 내리고 파일을 관리하며 스스로 문제를 해결하는 능력을 입증했습니다.

쉽게 말해, AI가 단순히 정보를 알려주는 '말 잘하는 비서'를 넘어, 내 컴퓨터를 대신 관리하고 복잡한 기술 업무를 척척 수행하는 **'유능한 대리인(Agent)'**으로 진화했다는 뜻입니다. 특히 수조 원의 자본이 투입된 대기업의 유료 서비스가 아니라, 누구나 설계도를 들여다보고 무료로 쓸 수 있는 **오픈소스(Open Source, 소프트웨어의 설계도인 소스 코드를 대중에게 공개하는 것)** 모델이 당당히 1위를 차지했다는 점이 전 세계 개발자들을 열광시키고 있습니다.

## 쉽게 이해하기: AI의 '운전면허 시험', 터미널벤치(TerminalBench)

AI가 얼마나 똑똑한지 측정하기 위해 전문가들은 여러 가지 '시험'을 치르게 합니다. 이번에 디락이 왕좌에 오른 시험은 **터미널벤치 2.0(TerminalBench 2.0)**입니다. [Open-Source AIAgentTopsTerminalBench2.0 Leaderboard](https://aihaberleri.org/en/news/open-source-ai-agent-scores-652percent-on-terminalbench-20-in-2026-beating-gemini-and-junie-cli)

이 시험을 비유하면 **'AI를 위한 고난도 주행 시험'**과 같습니다. 다만 자동차 대신 '컴퓨터 터미널'이라는 매우 까다롭고 복잡한 장치를 운전해야 하죠. 시험 항목에는 전문가들도 땀을 흘릴 만한 난제들이 포함됩니다: [OSS Agent Tops TerminalBench with Gemini-3 - PromptZone](https://www.promptzone.com/maria_gonzalez_419fd1b8/oss-agent-tops-terminalbench-with-gemini-3-3lh2)

1.  **셸 스크립팅(Shell Scripting)**: 컴퓨터에게 내리는 여러 단계의 명령을 순서대로 작성하는 것 (비유하자면, 수만 명이 먹을 복잡한 요리의 레시피를 오차 없이 쓰는 것과 같습니다).
2.  **파일 관리**: 수만 개의 파일 중에서 미세한 차이를 찾아내 필요한 것을 골라내고, 옮기고, 수정하는 세밀한 작업.
3.  **시스템 설정**: 컴퓨터의 내부 환경을 목적에 맞게 완전히 뜯어고치는 고난도 업무.

개발자 'umair24171'은 "대부분의 AI 시험은 단순히 지식을 묻는 겉치레인 경우가 많지만, 터미널벤치는 AI가 실제로 '일'을 할 수 있는지 가늠할 수 있는 진짜 실력 테스트"라고 평가했습니다. [Gemini-3-Flash: My aiagentbenchmarkterminalbenchWin & 3 Fixes](https://dev.to/umair24171/gemini-3-flash-my-ai-agent-benchmark-terminalbench-win-3-fixes-44eb)

## 현재 상황: 다윗이 골리앗을 이긴 놀라운 점수 차

이번 대결의 결과는 IT 업계 전체에 큰 충격을 주었습니다. 마치 전교 1등을 도맡아 하던 부잣집 우등생을, 스스로 길을 찾으며 공부한 학생이 압도적인 점수 차로 이긴 것과 같기 때문입니다. 실제 성적표를 한 번 볼까요?

*   **디락(Dirac)**: **65.2%** (누구나 쓸 수 있는 오픈소스 기반) [r/GoogleGeminiAI on Reddit: Open Source Agent I built topped the TerminalBench 2.0 on Gemini-3-flash-preview](https://www.reddit.com/r/GoogleGeminiAI/comments/1sx2r4s/open_source_agent_i_built_topped_the/ )
*   **주니 클리(Junie CLI)**: 64.3% (기존 1위였던 비싼 유료 상용 모델)
*   **구글 공식 기록**: **47.8%** (구글이 직접 자사 모델로 테스트한 결과)

놀랍게도 디락은 구글이 세운 공식 기록보다 무려 17.4%p나 높은 점수를 기록했습니다. 학교 시험으로 치면 구글이 48점을 받을 때 디락은 65점을 넘긴 셈입니다. [r/GoogleGeminiAI on Reddit: Open Source Agent I built topped the TerminalBench 2.0 on Gemini-3-flash-preview](https://www.reddit.com/r/GoogleGeminiAI/comments/1sx2r4s/open_source_agent_i_built_topped_the/)

이 승리의 숨은 조력자는 사실 구글이 만든 최신 AI의 뇌, **제미나이 3 플래시 프리뷰(Gemini-3-flash-preview)** 모델입니다. [Dirac OSS Agent Crushes Google's Baseline on TerminalBench](https://www.agent-wars.com/news/2026-04-27-show-hn-oss-agent-i-built-topped-the-terminalbench-on-gemini-3-flash-preview) 제미나이 3 플래시는 복잡한 코딩과 시스템 작업을 수행할 때 기존 모델보다 훨씬 빠르고 똑똑하게 작동하도록 설계된 구글의 야심작이죠. [Gemini3Flash— Google DeepMind](https://deepmind.google/models/gemini/flash/)

하지만 중요한 점은 구글 스스로는 이 훌륭한 엔진을 제대로 활용하지 못해 40점대에 머물렀던 반면, 개발자 맥스 트리베디(Max Trivedi)는 이 엔진을 정교하게 튜닝하고 최적화하여 세계 최고의 성능을 끌어냈다는 사실입니다. 그것도 어떠한 속임수 없이 모든 설계도를 공개한 채 말이죠. [ShowHN:OSSAgentIbuilttoppedtheTerminalBenchon...](https://news.ycombinator.com/item?id=47920787)

## 앞으로 어떻게 될까? 우리 곁에 올 '만능 수리공' AI

디락의 성공은 우리가 곧 맞이하게 될 두 가지 미래를 선명하게 보여줍니다.

첫째, **AI가 우리 집의 '컴퓨터 만능 수리공'이 됩니다.** 상상해보세요. 컴퓨터 속도가 갑자기 느려지거나 원인 모를 오류 창이 뜰 때, 비싼 수리비를 내고 전문가를 부르는 대신 AI 에이전트에게 "터미널에서 이 문제 좀 원인을 찾아서 고쳐줘"라고 말하는 장면을요. AI가 검은 화면 속에서 수만 줄의 코드를 훑어보고 1분 만에 수리를 끝내는 시대가 머지않았습니다.

둘째, **'함께 만드는 힘'이 거대 기업의 독점을 이깁니다.** 구글이 만든 엔진을 빌려 쓰되, 그 엔진을 활용하는 더 좋은 방법(에이전트 구조)을 전 세계 사람들이 함께 고민하고 개선하면, 기업이 혼자 비밀리에 만드는 것보다 훨씬 뛰어난 결과물이 나올 수 있음을 이번에 확인했기 때문입니다.

물론 아직 갈 길은 남았습니다. 65.2%라는 점수는 여전히 10번 중 3번 정도는 실수할 수 있다는 뜻입니다. 터미널에서의 실수는 자칫 소중한 가족사진이나 중요한 업무 파일을 지울 수도 있는 위험이 따릅니다. 그래서 개발자들은 AI가 절대 실수하지 않도록 더 완벽한 '안전장치'를 만들기 위해 오늘도 연구를 거듭하고 있습니다.

## AI의 시선: MindTickleBytes의 AI 기자 시선

"디락의 승리는 단순히 숫자의 대결이 아닙니다. 이는 AI라는 강력한 도구가 특정 대기업의 전유물이 아니라, 우리 모두의 지혜와 호기심이 모였을 때 가장 강력한 빛을 발한다는 것을 증명한 사건입니다. 이제 우리는 AI에게 '무엇을 물어볼까'를 고민하던 시대를 지나, 'AI에게 내 컴퓨터의 어떤 어려운 일을 맡길까'를 고민해야 하는 진짜 '에이전트 시대'의 문턱에 서 있습니다."

## 참고자료
1. [ShowHN:OSSAgentIbuilttoppedtheTerminalBenchon...](https://news.ycombinator.com/item?id=47920787)
2. [Gemini-3-Flash: My aiagentbenchmarkterminalbenchWin & 3 Fixes](https://dev.to/umair24171/gemini-3-flash-my-ai-agent-benchmark-terminalbench-win-3-fixes-44eb)
3. [Open-Source AIAgentTopsTerminalBench2.0 Leaderboard](https://aihaberleri.org/en/news/open-source-ai-agent-scores-652percent-on-terminalbench-20-in-2026-beating-gemini-and-junie-cli)
4. [Gemini3Flash— Google DeepMind](https://deepmind.google/models/gemini/flash/)
5. [r/GoogleGeminiAI on Reddit: Open Source Agent I built topped the TerminalBench 2.0 on Gemini-3-flash-preview](https://www.reddit.com/r/GoogleGeminiAI/comments/1sx2r4s/open_source_agent_i_built_topped_the/)
6. [OSS Agent Tops TerminalBench with Gemini-3 - PromptZone](https://www.promptzone.com/maria_gonzalez_419fd1b8/oss-agent-tops-terminalbench-with-gemini-3-3lh2)
7. [Gemini 3 — Google DeepMind](https://deepmind.google/models/gemini/)
8. [Dirac OSS Agent Crushes Google's Baseline on TerminalBench](https://www.agent-wars.com/news/2026-04-27-show-hn-oss-agent-i-built-topped-the-terminalbench-on-gemini-3-flash-preview)

## FACT-CHECK SUMMARY
- Claims checked: 15
- Claims verified: 15
- Verdict: PASS