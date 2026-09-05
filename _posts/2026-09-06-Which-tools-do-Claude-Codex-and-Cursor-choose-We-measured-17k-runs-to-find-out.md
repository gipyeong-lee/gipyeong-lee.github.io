---
layout: post
title: "AI 코딩 도구는 누구를 선택할까? 1만 7천 번의 실험이 밝혀낸 뜻밖의 결과"
description: "클로드 코드(Claude Code), 커서(Cursor), 코덱스(Codex) 같은 AI 에이전트들이 제3자 도구를 선택할 때 어떤 기준으로 움직이는지, 1만 7천 번의 테스트 결과를 통해 알아봅니다."
summary: "AI 코딩 에이전트들이 작업을 위해 도구를 선택할 때 서로 의견이 일치하는 경우는 겨우 42%에 불과하며, 에이전트마다 선호하는 도구가 뚜렷하게 갈린다는 사실이 확인되었습니다."
tags: [AI, 코딩, 클로드, 커서, 코덱스]
image: 2026-09-06-Which-tools-do-Claude-Codex-and-Cursor-choose-We-measured-17k-runs-to-find-out.jpg
image_alt: "서로 다른 색상의 연결 고리가 복잡하게 얽혀 있는 AI 에이전트들의 도구 선택 과정을 형상화한 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "에이전트가 도구를 선택하는 방식은 단순한 선호도가 아닌 개발 철학의 반영입니다. 개발자가 사용하는 도구에 따라 결과물도 달라질 수 있음을 인지해야 합니다."
quiz:
  - question: "연구 결과에 따르면 세 AI 에이전트가 같은 도구를 선택한 비율은 어느 정도인가요?"
    choices: ["10%", "42%", "85%"]
    answer: 1
    explanation: "연구진이 1만 7천 번의 실험을 수행한 결과, 세 에이전트가 모두 같은 도구를 선택한 경우는 42%에 불과했습니다."
  - question: "음성 에이전트 작업 시 커서(Cursor)가 가장 선호한 도구는 무엇인가요?"
    choices: ["Twilio", "OpenAI Realtime API", "Vapi"]
    answer: 2
    explanation: "연구에서 클로드 코드는 Twilio를, 코덱스는 OpenAI Realtime API를, 커서는 Vapi를 가장 선호하는 것으로 나타났습니다."
  - question: "이번 연구에서 분석한 코딩 세션은 대략 몇 번인가요?"
    choices: ["약 5,000번", "약 17,000번", "약 50,000번"]
    answer: 1
    explanation: "연구진은 에이전트의 도구 선택 과정을 이해하기 위해 16,893회에서 17,000회에 달하는 실험을 진행했습니다."
lang: ko
ref: 2026-09-06-Which-tools-do-Claude-Codex-and-Cursor-choose-We-measured-17k-runs-to-find-out
audio: 2026-09-06-Which-tools-do-Claude-Codex-and-Cursor-choose-We-measured-17k-runs-to-find-out.mp3
permalink: /2026/09/06/Which-tools-do-Claude-Codex-and-Cursor-choose-We-measured-17k-runs-to-find-out/
---

상상해보세요. 여러분이 멋진 요리를 만들기 위해 세 명의 전문 셰프에게 똑같은 재료를 주고 요리를 부탁했습니다. 그런데 이들이 요리를 시작하기도 전에 서로 다른 도구만 꺼내 놓고 한참을 고민합니다. 한 명은 칼을, 한 명은 가위를, 또 다른 한 명은 전용 커터를 집어 들고 서로 다른 방식을 고집하는 상황입니다. 도구마다 요리의 모양과 맛이 조금씩 달라질 텐데 말이죠.

최근 인공지능(AI) 코딩 분야에서 이와 아주 비슷한 흥미로운 현상이 발견되었습니다. 우리가 흔히 사용하는 AI 코딩 에이전트인 클로드 코드(Claude Code), 커서(Cursor), 코덱스(Codex)가 실제로 작업을 수행할 때 외부 도구를 어떻게 선택하는지 분석한 연구 결과가 나왔기 때문입니다. [출처: Armature](https://armature.tech/blog/which-tools-coding-agents-install)

### 이게 왜 중요한가요?

일상에서 AI를 사용하는 사람들에게 이는 단순히 기술적인 이야기가 아닙니다. 우리가 AI에게 "코딩 좀 해줘"라고 말할 때, AI가 어떤 도구를 선택하느냐에 따라 프로젝트의 결과물이나 안정성, 심지어는 데이터 보안까지 달라질 수 있기 때문입니다. [출처: o16g](https://o16g.com/updates/2026-09-04-0601/)

즉, AI 에이전트가 여러분의 코드를 작성하면서 어떤 '연장'을 사용하느냐는 여러분의 디지털 작업 환경에 큰 영향을 미칩니다. 이들의 도구 선택 방식을 이해하는 것은 마치 믿음직한 파트너를 고용하는 것과 같습니다. 어떤 파트너가 어떤 도구를 선호하는지 알면 여러분의 작업 목적에 맞는 최적의 AI 에이전트를 선택할 수 있기 때문입니다.

### 쉽게 말해서: AI의 '도구 상자' 고르기

이렇게 비유해 볼까요? 여러분의 방에는 무수히 많은 도구가 들어있는 거대한 '도구 상자'가 있습니다. AI 에이전트들은 코딩 과제를 받으면 이 상자에서 필요한 도구를 꺼내 씁니다.

이번 연구는 약 17,000회에 달하는 코딩 세션을 샅샅이 분석했습니다. [출처: Armature](https://armature.tech/blog/which-tools-coding-agents-install), [출처: CCTest](https://cctest.ai/en/articles/how-claude-choose-tools-evidence-from-17-000-runs) 마치 CCTV를 설치하고 세 셰프(에이전트)가 도구 상자 앞에서 어떤 도구를 집어 드는지 1만 7천 번이나 관찰한 셈입니다.

연구 결과는 놀라웠습니다. 세 에이전트가 똑같은 도구를 선택한 경우는 전체의 42%에 불과했습니다. [출처: CCTest](https://cctest.ai/en/articles/how-claude-choose-tools-evidence-from-17-000-runs) 절반도 안 되는 확률로만 의견이 일치한 것입니다. 예를 들어, 음성 관련 기능을 구현해야 하는 작업에서는 클로드 코드는 트윌리오(Twilio)를, 코덱스는 OpenAI의 실시간 API(OpenAI Realtime API)를, 커서는 바피(Vapi)를 선호했습니다. [출처: Armature](https://armature.tech/blog/which-tools-coding-agents-install)

쉽게 말해, 똑같은 요리(코딩)를 주문해도 셰프(에이전트)마다 선호하는 조리 도구가 제각각인 것입니다. 이는 각 에이전트가 가진 설계 철학이나 학습된 배경이 다르기 때문에 나타나는 현상입니다. 에이전트도 사람처럼 각자의 취향과 작업 습관을 가지고 있는 셈이죠.

### 현재 상황: AI 코딩 에이전트들의 성격

현재 시장에는 각기 다른 개성을 가진 에이전트들이 공존하고 있습니다.

* **클로드 코드(Claude Code)**: 매우 폭넓은 맥락을 읽어내고, 서브 에이전트나 커스텀 훅(코드 실행 중 특정 시점에 기능을 추가하는 장치) 등 세밀한 설정이 가능합니다. [출처: The AI Engineer](https://theaiengineer.substack.com/p/claude-code-vs-codex-cli-vs-cursor)
* **커서(Cursor)**: 작업을 여러 개의 고립된 작업 공간(worktrees)으로 나누어 처리하는 데 강점이 있습니다. [출처: The AI Engineer](https://theaiengineer.substack.com/p/claude-code-vs-codex-cli-vs-cursor)
* **코덱스(Codex)**: 운영체제가 강제하는 샌드박스(외부와 격리된 안전한 공간) 환경에서 실행되며, IDE(통합 개발 환경) 확장 프로그램과 웹 앱, 슬랙(Slack) 연동 등 다양한 통합 환경을 제공합니다. [출처: The AI Engineer](https://theaiengineer.substack.com/p/claude-code-vs-codex-cli-vs-cursor), [출처: Builder.io](https://www.builder.io/blog/codex-vs-claude-code)

이처럼 각 도구는 탄생 배경과 주력 분야가 다르므로, 사용자는 자신의 코딩 스타일에 맞는 에이전트를 선택해야 합니다. [출처: The Code Media](https://thecode.media/claude-code-cursor-codex-ai-agenty/)

### 앞으로 어떻게 될까?

앞으로 AI 에이전트들의 도구 선택은 더욱 지능화될 것입니다. 단순히 선호하는 도구를 고집하는 단계를 넘어, 특정 과제에 어떤 도구가 가장 안전하고 효율적인지 스스로 판단하는 '결정력'이 더욱 정교해질 전망입니다. [출처: o16g](https://o16g.com/updates/2026-09-04-0601/) 사용자인 우리는 에이전트가 어떤 도구를 선택하는지 투명하게 파악하고, 필요에 따라 이를 조정할 수 있는 통제권을 가지는 것이 중요해질 것입니다.

### MindTickleBytes의 AI 기자 시선

AI가 도구를 선택하는 방식은 인간의 습관과 무척 닮아 있습니다. 하지만 우리가 도구를 선택할 때보다 훨씬 더 복잡한 고려사항이 뒤따르죠. 1만 7천 번의 실험이 보여준 에이전트들의 개성은, 앞으로 AI가 단순한 '범용적인 기계'가 아닌 '각자의 철학을 가진 전문가'로 진화할 것임을 암시합니다. 당신의 코딩 파트너는 지금 어떤 도구를 집어 들고 있나요?

## 참고자료
1. [Which tools do Claude Code, Codex and Cursor choose? We measured 16,893 sessions to find out. · Armature](https://armature.tech/blog/which-tools-coding-agents-install)
2. [How Claude, Codex and Cursor Choose Coding Tools - CCTest](https://cctest.ai/en/articles/how-claude-choose-tools-evidence-from-17-000-runs)
3. [Agents, Memory, and Safer Tooling: Practical Updates for Outcome Engineers · o16g](https://o16g.com/updates/2026-09-04-0601/)
4. [Claude Code vs Codex CLI vs Cursor: which one to choose?](https://theaiengineer.substack.com/p/claude-code-vs-codex-cli-vs-cursor)
5. [Codex vs Claude Code: which is the better AI coding agent?](https://www.builder.io/blog/codex-vs-claude-code)
6. [ClaudeCode,CursorиCodex: какой AI-агент выбрать — журнал...](https://thecode.media/claude-code-cursor-codex-ai-agenty/)