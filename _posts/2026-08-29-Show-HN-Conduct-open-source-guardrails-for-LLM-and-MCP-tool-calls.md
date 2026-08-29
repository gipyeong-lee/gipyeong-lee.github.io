---
layout: post
title: "AI가 당신의 컴퓨터를 조종하기 전, '생각'을 검문할 방법이 있을까?"
description: "AI가 외부 도구를 실행하기 전에 위험한 행동을 차단하는 오픈소스 보안 프로젝트 'Conduct'에 대해 알아봅니다."
summary: "AI 비서가 외부 도구를 사용하여 작업할 때, 위험한 명령을 미리 차단하고 감시할 수 있는 오픈소스 보안 레이어 'Conduct'를 소개합니다."
tags: [AI, 보안, 오픈소스, LLM, MCP]
image: 2026-08-29-Show-HN-Conduct-open-source-guardrails-for-LLM-and-MCP-tool-calls.jpg
image_alt: "AI 비서와 외부 시스템 사이에서 보안을 지키는 가상의 방화벽을 시각화한 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 비서의 능력이 확장될수록 그 권한 또한 위험해집니다. Conduct와 같은 '가드레일'은 AI를 믿고 쓰기 위해 반드시 필요한 안전벨트가 될 것입니다."
quiz:
  - question: "Conduct는 주로 어떤 기능을 수행하나요?"
    choices: ["AI 모델 직접 개발", "AI 비서의 도구 실행 전 감시 및 차단", "AI 모델 학습 데이터 수집"]
    answer: 1
    explanation: "Conduct는 AI가 외부 도구(MCP 등)를 실행하려는 의도를 포착하여, 실제로 도구가 실행되기 전에 위험성을 점검하고 필요시 차단하는 보안 프로젝트입니다."
  - question: "Conduct가 감시하는 주요 지점은 어디인가요?"
    choices: ["웹 브라우저의 접속 기록", "MCP 레이어, 라우터, LLM 호출 등 세 곳", "사용자의 개인 비밀번호 저장소"]
    answer: 1
    explanation: "Conduct는 MCP 레이어, 라우터, 그리고 LLM 호출이라는 세 가지 enforcement surface(강제 지점)에서 보안 정책을 적용합니다."
  - question: "Conduct의 실패 모드(Failure mode)는 어떤 방식을 취하나요?"
    choices: ["Fail-close(차단)", "Fail-open(허용/소프트)", "무조건 강제 종료"]
    answer: 1
    explanation: "Conduct는 보안 시스템에 문제가 생겼을 때 우선 작동을 유지하는 'Fail-open(소프트)' 방식을 택하고 있습니다."
lang: ko
ref: 2026-08-29-Show-HN-Conduct-open-source-guardrails-for-LLM-and-MCP-tool-calls
audio: 2026-08-29-Show-HN-Conduct-open-source-guardrails-for-LLM-and-MCP-tool-calls.mp3
permalink: /2026/08/29/Show-HN-Conduct-open-source-guardrails-for-LLM-and-MCP-tool-calls/
---

상상해보세요. 아침에 일어나서 스마트폰의 AI 비서에게 "내 이메일을 다 읽고, 중요한 내용만 골라서 내 업무용 슬랙(Slack) 채널에 공유해줘"라고 말했습니다. 아주 편리한 기능이죠? 하지만 이 AI가 이메일 계정에 접근하는 권한을 넘어, 당신의 컴퓨터에 있는 파일 삭제 권한까지 가지고 있다면 어떨까요? 혹은 실수로 비공개 문서까지 슬랙에 올려버린다면요?

이런 편리함 이면에 숨겨진 불안함을 해결하기 위해 등장한 오픈소스 보안 프로젝트가 있습니다. 바로 **Conduct**입니다.

### 이게 왜 중요한가요? (Why It Matters)

최근 AI 모델들은 단순히 대화하는 수준을 넘어, 사람처럼 외부 도구를 사용하여 직접 업무를 처리하기 시작했습니다. 이를 가능하게 하는 핵심 기술 중 하나가 바로 **MCP(Model Context Protocol, AI 비서와 외부 데이터나 도구를 연결하는 표준 통신 규약)**입니다. [[출처: What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/)]

AI가 편리해질수록, 그 AI가 내 컴퓨터나 서버에서 실행할 수 있는 '권한' 또한 강력해지고 있습니다. 기업들이 업무용으로 AI를 도입할 때 가장 큰 걸림돌은 보안 사고입니다. AI가 실수로 중요 파일을 지우거나 외부로 유출할 위험을 완벽히 통제하기 어렵기 때문이죠. **Conduct**는 기업들이 AI 비서를 안전하게 배치할 수 있도록 돕는 일종의 '안전벨트' 역할을 합니다. [[출처: Conduct开源详解：为LLM与MCP... - OpenAI Hub](https://www.openai-hub.com/news/1799/)]

### 쉽게 이해하기 (The Explainer)

Conduct를 쉽게 비유하자면, 회사 건물 입구에 있는 **'보안 검색대'**와 같습니다.

지금까지 AI 비서가 도구를 실행하는 과정이 "지나가세요"라고 말하는 수준이었다면, Conduct는 AI가 "이 파일을 삭제하세요"라는 명령을 내릴 때 **"잠시만요, 어디로 가는 어떤 파일인지 확인하겠습니다"**라고 가로막는 검색대 역할을 합니다. [[출처: Conduct开源详解：为LLM与MCP... - OpenAI Hub](https://www.openai-hub.com/news/1799/)]

또 다른 예로, 우리가 사진 보정 앱을 쓸 때 앱이 내 사진첩에 바로 접근하는 것을 허용할지 묻는 '접근 권한 필터'가 있듯이, Conduct는 AI 모델의 '실행 의도'를 미리 낚아채서 해당 작업이 안전한지 판단하는 감시 필터입니다. 

이 시스템은 크게 세 곳을 감시합니다. [[출처: GitHub - sseshachala/conductai: AI agent governance for teams.](https://github.com/sseshachala/conductai)]
1. **MCP 레이어**: AI가 외부 데이터를 주고받는 모든 MCP 도구 호출을 확인합니다.
2. **라우터**: AI가 어떤 SDK를 통하든 호출되는 모든 LLM(거대 언어 모델) 명령을 감시합니다.
3. **LLM 호출**: AI 모델이 생성한 구체적인 명령 호출 자체를 점검합니다.

만약 AI가 수상한 행동을 하려 한다면, Conduct는 외부 도구에 명령이 전달되기 전에 이를 차단하거나 기록(audit)을 남겨 보안팀이 나중에 검토할 수 있게 합니다.

### 현재 상황 (Where We Stand)

현재 Conduct는 **오픈소스**로 제공되는 보안 가드레일(Guardrail, AI 안전을 위한 제어 장치) 프로젝트입니다. [[출처: Conduct开源详解：为LLM与MCP... - OpenAI Hub](https://www.openai-hub.com/news/1799/)] [[출처: ConductOpenSourceGuardrailsFORLLMANDMCPToolCalls](https://rankium.io/rankium/product/conduct-open-source-guardrails-for-llm-and-mcp-tool-calls)]

이 프로젝트의 흥미로운 점 중 하나는 실패 모드가 **'Fail-open(소프트)'** 방식을 따른다는 것입니다. [[출처: GitHub - sseshachala/conductai: AI agent governance for teams.](https://github.com/sseshachala/conductai)] 이는 보안 시스템 자체에 오류가 생겨도 AI 비서의 모든 기능이 멈추지 않게 설계된 것인데, 비즈니스 연속성을 중요하게 생각하는 조직에게는 유리한 선택입니다.

물론, 이 도구 하나만 설치한다고 해서 모든 보안 위협이 사라지는 것은 아닙니다. 실제 업무 환경에서의 AI 안전은 여러 겹의 가드레일이 겹쳐진 '스택' 구조를 가져야 합니다. [[출처: LLMGuardrails: Production Safety Layers Reference 2026](https://www.digitalapplied.com/blog/llm-guardrails-production-safety-layers-2026)] Conduct는 그 여러 겹 중 '도구 실행 단계'를 책임지는 중요한 레이어인 셈입니다.

### 앞으로 어떻게 될까? (What's Next)

앞으로는 AI가 단순히 텍스트를 읽고 쓰는 것을 넘어, 코드를 실행하고 서버를 관리하며 업무 자동화를 수행하는 '에이전트(Agent)'로 진화할 것입니다. 이에 따라 AI의 모든 도구 호출을 검사하는 Conduct와 같은 도구들의 중요성은 점점 커질 것입니다. 사용자가 직접 도구 입력값을 확인하고, 결과를 검증하는 과정이 필수적인 시대가 오고 있습니다. [[출처: Tools- Model Context Protocol](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)]

개발자들은 앞으로 AI가 "무엇을 할 수 있느냐"를 넘어 "어떻게 안전하게 제어할 수 있느냐"를 고민하게 될 것입니다.

---

### MindTickleBytes의 AI 기자 시선
AI의 능력을 확장하는 것은 기술의 영역이지만, 그 권한을 통제하는 것은 신뢰의 영역입니다. Conduct와 같은 오픈소스 가드레일은 AI가 인간의 도구로서 안전하게 공존할 수 있는 기반을 다지는 중요한 흐름입니다. 투명한 검증 과정이 기술의 발전을 오히려 가속화할 것입니다.

## 참고자료
1. [ShowHN: Conduct, open-source guardrails for LLM and MCP tool calls](https://news.ycombinator.com/item?id=49483173)
2. [Conduct开源详解：为LLM与MCP... - OpenAI Hub](https://www.openai-hub.com/news/1799/)
3. [GitHub - sseshachala/conductai: AI agent governance for teams.](https://github.com/sseshachala/conductai)
4. [ConductOpenSourceGuardrailsFORLLMANDMCPToolCalls](https://rankium.io/rankium/product/conduct-open-source-guardrails-for-llm-and-mcp-tool-calls)
5. [What is the Model Context Protocol (MCP)? - Model Context Protocol](https://modelcontextprotocol.io/)
6. [LLMGuardrails: Production Safety Layers Reference 2026](https://www.digitalapplied.com/blog/llm-guardrails-production-safety-layers-2026)
7. [Tools- Model Context Protocol](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)