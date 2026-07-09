---
layout: post
title: "내가 말하는 대로 그림을 그린다고? AI와 실시간으로 협업하는 '에이전트 드로우(Agent Draw)'"
description: "AI에게 말만 하면 무한 캔버스 위에서 실시간으로 그림을 그려주는 에이전트 드로우 도구와 그 원리를 알아봅니다."
summary: "에이전트 드로우는 AI 에이전트가 사용자의 음성 명령을 이해하고 무한 캔버스 위에서 실시간으로 직접 그림을 그리고 도형을 배치하게 해주는 인터랙티브 도구입니다."
tags: [AI, 에이전트, tldraw, 창의성, 도구]
image: 2026-07-09-Show-HN-Agent-Draw-An-agent-draws-while-you-talk-built-on-TLDraw.jpg
image_alt: "무한 캔버스 위에 AI가 실시간으로 그림을 그리고 있는 에이전트 드로우의 인터페이스 화면."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "단순한 이미지 생성을 넘어, AI가 캔버스라는 공간 속에서 사용자와 물리적으로 상호작용하는 첫걸음입니다."
quiz:
  - question: "에이전트 드로우가 기반으로 사용하는 기술은 무엇인가요?"
    choices: ["피그마(Figma)", "TLDraw SDK", "어도비 포토샵"]
    answer: 1
    explanation: "에이전트 드로우는 리액트(React) 기반의 무한 캔버스 SDK인 tldraw를 기반으로 구축되었습니다."
  - question: "사용자가 에이전트에게 명령을 전달하는 방식은 무엇인가요?"
    choices: ["전용 키보드 입력", "오른쪽 채팅 패널을 통한 음성 및 텍스트 대화", "이미지 파일 업로드"]
    answer: 1
    explanation: "화면 오른쪽의 채팅 패널을 통해 사용자가 음성이나 텍스트로 에이전트와 대화하고 컨텍스트를 추가할 수 있습니다."
  - question: "에이전트 드로우는 여러 개의 요청을 어떻게 처리하나요?"
    choices: ["무작위 순서로 처리", "FIFO(선입선출) 큐를 사용한 상태 머신 처리", "모든 요청을 동시에 병렬 처리"]
    answer: 1
    explanation: "여러 요청이 들어올 경우 FIFO(First-In, First-Out) 큐와 상태 머신을 사용해 한 번에 하나의 세션을 순차적으로 처리합니다."
lang: ko
ref: 2026-07-09-Show-HN-Agent-Draw-An-agent-draws-while-you-talk-built-on-TLDraw
audio: 2026-07-09-Show-HN-Agent-Draw-An-agent-draws-while-you-talk-built-on-TLDraw.mp3
permalink: /2026/07/09/Show-HN-Agent-Draw-An-agent-draws-while-you-talk-built-on-TLDraw/
---

상상해보세요. 빈 종이를 앞에 두고 "이곳에 맛있는 피자를 그려줘"라고 말했더니, 눈앞에서 AI가 선을 긋고 치즈와 페퍼로니를 슥슥 그려내기 시작합니다. 마치 마법 같은 이 상황이 이제는 일상이 될 준비를 하고 있습니다. 최근 발표된 '에이전트 드로우(Agent Draw)'는 우리가 AI와 협업하는 방식을 완전히 뒤바꿔놓고 있습니다.

### 왜 이 도구가 주목받을까요?

지금까지 우리가 AI에게 그림을 그려달라고 하면, 보통은 명령어를 입력하고 잠시 기다린 뒤 완성된 결과물을 '받아보기만' 했습니다. 즉, AI는 일방적으로 결과물을 던져주는 존재에 가까웠죠. 하지만 에이전트 드로우는 완전히 다릅니다. 캔버스 위에서 사용자와 끊임없이 소통하며 실시간으로 그림을 함께 그려 나가는 '협업'의 과정을 보여주기 때문입니다 [출처 2](https://www.youtube.com/watch?v=iIH2hJAxxm8).

이는 창의적인 작업이 더 이상 혼자만의 과정이 아님을 의미합니다. 마치 회의실 화이트보드 앞에서 동료와 아이디어를 주고받으며 그림을 완성하듯, AI와 사람이 같은 공간에서 의견을 나누며 작업할 수 있게 된 것입니다. 이제 AI는 단순히 결과물을 만들어내는 '도구'를 넘어, 캔버스 위에 함께 올라선 능동적인 '동료'로 거듭나고 있습니다 [출처 13](https://gitnation.com/contents/agents-on-the-canvas-with-tldraw).

### 어떻게 작동하는 걸까요?

에이전트 드로우가 작동하는 원리는 생각보다 정교합니다. 쉽게 비유하자면, 우리가 직접 그리지 않아도 내 손의 연장선이 되어 대신 그림을 그려주는 '똑똑한 AI 로봇 팔'이 캔버스 위에 있다고 생각하면 이해가 빠릅니다.

1. **무한한 도화지 (tldraw SDK)**: 기초가 되는 캔버스 환경입니다. 리액트(React) 기반의 무한 캔버스 SDK인 'tldraw'를 사용해, AI가 자유롭게 도형을 배치하고 그림을 그릴 수 있는 공간을 마련했습니다 [출처 1, 출처 15](https://tldraw.dev/blog/tldraw-mcp-app).
2. **에이전트 스타터 키트 (기본 교육 과정)**: AI에게는 그림을 그리고 도형을 다루는 법을 가르치는 일종의 '기본기'입니다. 이 키트를 통해 AI는 단순한 이미지를 넘어 사각형, 다이아몬드, 화살표 같은 기본 도형들을 읽고 배치하며 캔버스 요소를 세밀하게 조작할 수 있게 됩니다 [출처 6, 출처 12](https://github.com/tldraw/tldraw/blob/main/apps/docs/content/starter-kits/agent.mdx).
3. **교통정리 시스템 (상태 머신)**: 사용자가 여러 요청을 동시에 쏟아내도 시스템이 엉키지 않게 해줍니다. '먼저 들어온 요청을 먼저 처리하는' FIFO(First-In, First-Out) 큐와 상태 머신을 통해, AI가 한 번에 하나의 작업 세션을 집중해서 순차적으로 해결하도록 관리합니다 [출처 8](https://techstackups.com/articles/tldraw-agent-draw/).

이런 과정을 통해 AI는 사용자가 지정한 캔버스 영역 안에서 음성 명령의 의미를 파악하고, 실시간으로 도형을 그려 넣으며 사용자의 의도를 즉각 반영합니다 [출처 2, 출처 3](https://www.youtube.com/watch?v=livloOnVpC8).

### 현재 어디까지 왔을까요?

현재 에이전트 드로우는 개발자들을 위한 공식 '에이전트 스타터 키트'를 토대로 구축되었습니다 [출처 2, 출처 5](https://memedata.com/post/130752). 사용자는 화면 오른쪽 채팅 패널을 통해 에이전트와 대화를 나눕니다. 이곳에서 필요한 배경 설명을 덧붙이거나, 에이전트가 그동안 수행한 작업 기록을 확인하며 소통할 수 있죠 [출처 6, 출처 11](https://zenn.dev/slowhand/articles/bb203aba83e385?locale=en).

AI는 기본적인 도형 조합이나 구성을 아주 능숙하게 수행합니다. 단순히 그림만 그리는 게 아니라, 할 일 목록을 작성하거나 수정을 요청하면 즉시 반영하여 업데이트하는 등 복합적인 업무 보조도 가능합니다 [출처 12](https://github.com/tldraw/tldraw/blob/main/apps/docs/content/starter-kits/agent.mdx). 물론 아직은 복잡한 예술적 창작보다는 체계적인 다이어그램 생성이나 실시간 시각적 보조 도구로서의 역할에 훨씬 더 최적화되어 있습니다 [출처 9, 출처 11](https://zenn.dev/slowhand/articles/bb203aba83e385?locale=en).

### 미래의 우리는 어떻게 일하게 될까요?

에이전트 드로우의 등장은 우리가 머지않은 미래에 AI와 어떻게 일하게 될지를 보여주는 작은 예고편입니다. 앞으로 AI 에이전트는 캔버스 위에서 더 깊이 있는 추론을 수행하고, 사용자의 미세한 의도까지 파악하여 스스로 도면을 수정하거나 아이디어를 제시하는 수준까지 발전할 것입니다.

우리는 곧 AI가 단순히 멈춰 있는 이미지를 만드는 것을 넘어, 캔버스라는 물리적 공간에서 우리와 함께 고민하고 그리는 '진정한 시각적 동료'를 곁에 두게 될 것입니다. 이제 화면 속 캔버스는 단순한 그림판이 아니라, 인간과 AI가 실시간으로 생각을 맞추는 협업의 새로운 장이 될 것입니다.

---

### MindTickleBytes의 AI 기자 시선
지금껏 그림을 그려주는 AI는 많았지만, 캔버스라는 '공간'을 이해하고 사용자와 상호작용하며 결과물을 빌드업하는 AI는 드물었습니다. AI가 우리의 생각과 함께 호흡하며 무언가를 완성해 나가는 과정 자체가 창의적인 경험의 본질을 바꾸고 있습니다.

## 참고자료

1. [Show HN: Agent Draw: An agent draws while you talk, built on TLDraw](https://news.ycombinator.com/item?id=48805475)
2. [Agent Draw — Speak, and an AI Agent Draws It Live on Canvas](https://www.youtube.com/watch?v=iIH2hJAxxm8)
3. [Agent Draw: drag a box, speak, an AI agent draws inside it](https://www.youtube.com/watch?v=livloOnVpC8)
4. [Agent Draw: An agent draws while you talk, built on TLDraw](https://vuink.com/post/grpufgnpxhcf-d-dpbz/articles/tldraw-agent-draw)
5. [Show HN：Agent Draw，基于 TLDraw 构建，在你说话时自动绘图。](https://memedata.com/post/130752)
6. [GitHub - tldraw/agent-template: Enable AI agents to interpret ...](https://github.com/tldraw/agent-template)
7. [Better HN - bhn.vercel.app](https://bhn.vercel.app/show)
8. [Agent Draw: An agent draws while you talk, built on TLDraw | Tech Stackups](https://techstackups.com/articles/tldraw-agent-draw/)
9. [Agent starter kit • tldraw Docs](https://tldraw.dev/starter-kits/agent)
10. [Starter kits • tldraw Docs](https://tldraw.dev/starter-kits)
11. [tldraw × AI Agent: Exploring the Mechanics with the Agent Starter Kit](https://zenn.dev/slowhand/articles/bb203aba83e385?locale=en)
12. [tldraw/apps/docs/content/starter-kits/agent.mdx at main · tldraw/tldraw](https://github.com/tldraw/tldraw/blob/main/apps/docs/content/starter-kits/agent.mdx)
13. [Agents on the Canvas With tldraw by Max Drake](https://gitnation.com/contents/agents-on-the-canvas-with-tldraw)
14. [Build a Real-Time tldraw Whiteboard with Velt Comments inside ChatGPT🤯🔥 - DEV Community](https://dev.to/astrodevil/build-a-real-time-tldraw-whiteboard-with-velt-comments-inside-chatgpt-1dhe)
15. [tldraw MCP App: Letting your agents draw](https://tldraw.dev/blog/tldraw-mcp-app)
16. [Show | Hacker News - nhn.yuu.is](https://nhn.yuu.is/show)