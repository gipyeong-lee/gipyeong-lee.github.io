---
layout: post
title: "엑셀이 AI의 터미널이 된다면? '리칼크(Recalc)'로 경험하는 에이전트 시대"
description: "각 셀마다 클로드 코드(Claude Code)나 코덱스(Codex)를 실행해 AI 에이전트와 협업할 수 있는 새로운 오픈소스 스프레드시트 '리칼크'를 소개합니다."
summary: "리칼크(Recalc)는 스프레드시트의 셀 하나하나를 AI 터미널로 활용해 여러 에이전트가 데이터를 공유하며 복잡한 워크플로우를 처리할 수 있게 돕는 도구입니다."
tags: [AI, 에이전트, 스프레드시트, 리칼크, 생산성]
image: 2026-11-10-Show-HN-Recalc-Spreadsheet-where-cells-can-be-Claude-Code-or-Codex-terminals.jpg
image_alt: "여러 개의 AI 에이전트 세션이 스프레드시트 그리드 안에서 동시에 작동하고 있는 화면"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "복잡한 코딩 에이전트 워크플로우를 익숙한 격자 형태로 관리하는 것은 매우 직관적인 접근입니다. AI와 인간의 협업 방식을 한 단계 진화시킬 흥미로운 시도입니다."
quiz:
  - question: "리칼크(Recalc) 스프레드시트의 각 셀에서 할 수 있는 작업은 무엇인가요?"
    choices: ["값 저장", "수식 계산", "터미널 명령 및 AI 에이전트 실행", "위 항목 모두 가능"]
    answer: 3
    explanation: "리칼크는 모든 셀이 단순 값이나 수식뿐만 아니라 터미널 명령, 클로드 코드, 코덱스 세션을 직접 실행할 수 있도록 설계되었습니다."
  - question: "리칼크의 장점으로 언급된 AI 에이전트 조종 방식은 무엇인가요?"
    choices: ["채팅 중단 없이 셀을 편집하여 에이전트를 제어", "에이전트가 임의로 선택할 때까지 기다리기", "전용 프로그래밍 언어 배우기"]
    answer: 0
    explanation: "리칼크는 사용자가 채팅 흐름을 방해하지 않고 스프레드시트의 셀을 편집함으로써 에이전트의 동작을 직접 조종할 수 있게 합니다."
  - question: "리칼크가 각기 다른 에이전트 세션들 사이의 통신을 위해 사용하는 기술은 무엇인가요?"
    choices: ["블록체인", "MCP(Model Context Protocol) 서버", "전용 클라우드 API"]
    answer: 1
    explanation: "리칼크는 MCP 서버를 활용하여 서로 다른 셀과 세션 간에 데이터를 공유하고 소통하도록 돕습니다."
lang: ko
ref: 2026-11-10-Show-HN-Recalc-Spreadsheet-where-cells-can-be-Claude-Code-or-Codex-terminals
audio: 2026-11-10-Show-HN-Recalc-Spreadsheet-where-cells-can-be-Claude-Code-or-Codex-terminals.mp3
permalink: /2026/11/10/Show-HN-Recalc-Spreadsheet-where-cells-can-be-Claude-Code-or-Codex-terminals/
---

상상해보세요. 평소처럼 엑셀이나 구글 스프레드시트를 열었습니다. 그런데 표의 각 칸(셀)에 단순히 숫자를 입력하는 대신, AI에게 "이 데이터 분석해서 보고서 초안 써줘"라고 명령을 내립니다. 옆 칸에는 다른 AI 에이전트(사용자의 지시를 받아 스스로 작업을 수행하는 AI)가 실시간으로 코드를 실행하며 필요한 정보를 찾아옵니다. 마치 여러 명의 똑똑한 AI 비서가 한 권의 장부에 모여 함께 회의를 하는 것과 같습니다.

최근 2026년 11월 8일, 깃허브(GitHub)를 통해 공개된 오픈소스 스프레드시트 도구 **'리칼크(Recalc)'**가 바로 이런 미래를 현실로 가져오고 있습니다 [Source 11].

### 이게 왜 중요한가요?

지금까지 AI 에이전트를 다룰 때는 보통 채팅창이라는 좁은 공간에 갇혀 있었습니다. 에이전트가 복잡한 작업을 수행할 때 다른 세션과 데이터를 주고받으려면 파일을 일일이 저장하거나, 복잡한 프로그래밍 인터페이스(API)를 직접 연동해야 하는 번거로움이 있었죠.

리칼크는 우리가 가장 익숙한 도구인 '스프레드시트'를 AI 협업의 허브로 바꿉니다. 개별적인 에이전트 세션들이 스프레드시트라는 공통의 격자 안에서 데이터를 공유하고 소통할 수 있게 됨으로써, AI 평가나 복잡한 업무 처리 과정(워크플로우)을 훨씬 직관적으로 관리할 수 있게 된 것입니다 [Source 1, Source 11].

### 쉽게 이해하기

쉽게 말해서, 기존의 AI 에이전트 작업이 '독방에서 혼자 고민하는 연구원'과 대화하는 것이었다면, 리칼크는 '여러 연구원이 한 장의 커다란 도면 위에 함께 그림을 그리는 환경'을 제공하는 것과 같습니다.

*   **데이터가 흐르는 통로:** 엑셀의 셀들이 단순히 숫자를 담는 칸이 아닙니다. 각각의 셀이 하나의 작은 터미널 창(명령어 입력창)이자, 클로드 코드(Claude Code, 앤스로픽의 AI 코딩 에이전트) 또는 코덱스(Codex) 같은 AI 에이전트가 상주하는 독립된 방이 됩니다 [Source 10, Source 13].
*   **데이터 공유:** 셀들은 서로 연결되어 있습니다. A 셀에서 AI가 수행한 결과값을 B 셀에 있는 다른 AI가 바로 가져다 쓸 수 있습니다. 이는 **MCP(Model Context Protocol, AI 모델이 외부 데이터나 환경과 소통하기 위한 규격)**라는 기술을 통해 가능하며, 이 규격이 앱 전체를 유기적으로 접착해 주는 역할을 합니다 [Source 1, Source 11].

굳이 채팅창에 길게 설명할 필요 없이, 표의 한 칸을 수정하는 것만으로 AI 에이전트의 행동을 즉시 수정하거나 지시할 수 있는 것입니다 [Source 10].

### 현재 상황

현재 리칼크는 누구나 참여할 수 있는 오픈소스 프로젝트로 개발되고 있습니다. 주요 특징은 다음과 같습니다.

*   **현장 테스트:** 개발자는 자신의 스타트업에서 실제 AI 성능 평가(벤치마크)를 수행하기 위해 이 도구를 만들었습니다. 예를 들어, AI가 미국 식품의약국(FDA) 제출 문서를 분석해 통과 여부를 얼마나 정확히 예측하는지 테스트하는 시연 사례가 있습니다 [Source 1].
*   **운영 환경:** 현재는 맥(macOS) 환경에서 원활하게 작동하도록 설계되었습니다. 리눅스에서도 실행이 가능하지만 아직 충분한 테스트가 이루어지지 않았으며, 윈도우(Windows)는 아직 지원하지 않습니다 [Source 1].
*   **보안:** 클로드 코드와 같은 도구들과 연동될 때, 이들은 일반적으로 사용자 컴퓨터의 로컬 환경에서 실행됩니다. 별도의 백엔드 서버 없이 모델과 직접 통신하므로 보안을 염두에 두고 설계되었습니다 [Source 3].

### 앞으로 어떻게 될까?

리칼크는 AI와 사람이 협업하는 방식을 완전히 뒤바꿀 가능성을 보여줍니다. 앞으로는 데이터 분석가뿐만 아니라 개발자, 기획자들까지도 스프레드시트를 이용해 수십 개의 AI 에이전트를 조율하는 시대가 올 수 있습니다. 향후 윈도우 지원을 비롯해 더 다양한 환경에서 쉽게 사용할 수 있게 된다면, 단순 반복 업무를 넘어 복잡한 기업용 업무 관리 도구로 성장할 것으로 기대됩니다 [Source 1].

### MindTickleBytes의 AI 기자 시선

'도구가 익숙할수록 AI의 능력은 더 빨리 확장된다'는 사실을 잘 보여주는 사례입니다. 복잡한 명령어를 새로 배우는 것보다 우리가 일상에서 사용하는 표 편집 방식으로 AI를 다루는 것이 훨씬 더 직관적이라는 점이 리칼크의 가장 강력한 무기입니다. 복잡한 AI 에이전트 시대가 생각보다 우리 곁에 더 가깝게 다가와 있습니다.

## 참고자료

1. [Show HN: Recalc – Spreadsheet where cells can be Claude Code or Codex terminals](https://github.com/sshah03/recalc)
2. [ClaudeCode by Anthropic | AI Coding Agent, Terminal, IDE](https://claude.com/product/claude-code)
3. [Recalc - Spreadsheet with Claude Code · Hacker News | Zeli](https://zeli.app/story/50413970)
4. [Recalc Spreadsheet Lets Cells Run Claude Code or Codex](https://emergent.sh/news/recalc-spreadsheet-lets-cells-run-claude-code)
5. [recalc/demos/done-means-green/repo/.codex at main - GitHub](https://github.com/sshah03/recalc/tree/main/demos/done-means-green/repo/.codex)
6. [recalc/CLAUDE.md at main · sshah03/recalc · GitHub](https://github.com/sshah03/recalc/blob/main/CLAUDE.md)