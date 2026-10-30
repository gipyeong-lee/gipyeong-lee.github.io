---
layout: post
title: "AI가 코드를 짜기 전에 '계획서'부터 쓴다고? — AI와 안전하게 협업하는 법"
description: "AI 에이전트가 함부로 코드를 수정하지 못하게 막는 '플랜 모드'와 코드 검증의 중요성을 알아봅니다."
summary: "AI 에이전트가 코드를 수정하기 전 반드시 인간의 승인을 받게 하는 '플랜 모드'를 통해, AI와의 협업에서 발생할 수 있는 오류를 예방하는 검증 시스템을 소개합니다."
tags: [AI, 에이전트, 코딩, 플랜모드, AI안전]
image: 2026-10-30-Until-You-approve-the-plan-a-separate-agent-checks-the-code-against-it.jpg
image_alt: "인간이 태블릿 화면의 AI 계획서를 검토하고 승인 버튼을 누르는 모습"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI의 능력을 믿되 검증은 철저히 해야 합니다. 플랜 모드는 AI와 인간이 서로의 의도를 완벽히 이해하고 신뢰할 수 있게 만드는 다리입니다."
quiz:
  - question: "AI의 '플랜 모드(Plan Mode)'가 하는 핵심 역할은 무엇인가요?"
    choices: ["AI가 자동으로 배포까지 완료하게 함", "AI가 코드를 수정하기 전 인간의 승인을 받도록 함", "AI의 연산 속도를 2배로 높임"]
    answer: 1
    explanation: "플랜 모드는 AI 에이전트가 코드를 수정하거나 파일을 생성하기 전 반드시 계획서를 작성하고 인간의 승인을 거치게 하는 안전장치입니다."
  - question: "에이전트 중심의 개발 환경에서 코드 품질을 높이기 위해 사용하는 방법은?"
    choices: ["인간이 직접 모든 코드를 작성함", "별도의 리뷰어 에이전트와 CI 도구를 활용함", "AI의 승인 없이 배포를 진행함"]
    answer: 1
    explanation: "최신 AI 개발 워크플로우에서는 CI(지속적 통합) 도구와 더불어 별도의 리뷰어 에이전트가 코드와 계획서를 대조 평가하여 품질을 보장합니다."
  - question: "보안이 중요한 환경에서 AI가 수정안을 적용하는 기준은?"
    choices: ["고객이 승인한 범위 안에서만 테스트 후 적용", "AI가 스스로 판단하여 즉시 적용", "일단 적용하고 나중에 확인"]
    answer: 0
    explanation: "보안이 중요한 플랫폼에서는 고객이 승인한 범위 내에서 테스트를 거친 후, 명시적인 승인이 있어야만 수정사항이 적용됩니다."
lang: ko
ref: 2026-10-30-Until-You-approve-the-plan-a-separate-agent-checks-the-code-against-it
audio: 2026-10-30-Until-You-approve-the-plan-a-separate-agent-checks-the-code-against-it.mp3
permalink: /2026/10/30/Until-You-approve-the-plan-a-separate-agent-checks-the-code-against-it/
---

상상해보세요. 여러분이 인테리어 공사를 맡겼는데, 목수가 말도 없이 벽을 다 허물고 나서야 "이제 어떻게 고칠까요?"라고 묻는다면 어떨까요? 무척 당황스럽고 화가 날 것입니다. 우리가 사용하는 AI 코딩 도구들도 마찬가지입니다. AI에게 "이 기능을 만들어줘"라고 부탁했는데, AI가 앞뒤 재지 않고 코드를 엉망으로 고쳐놓는다면 큰일이겠죠.

최근 AI 기술이 발전하면서, AI가 직접 코드를 작성하고 수정하는 '에이전트(Agent, 스스로 판단하여 특정 업무를 수행하는 AI)' 시대가 열렸습니다. 그런데 이 에이전트가 실수 없이 우리 의도대로 움직이게 하려면 어떻게 해야 할까요? 오늘은 AI가 코드를 고치기 전에 반드시 '계획서'부터 쓰게 만드는, 이른바 '플랜 모드(Plan Mode)'라는 안전장치에 대해 이야기해보려 합니다.

## 이게 왜 중요한가요?

일상에서 AI를 사용하는 사람들에게 이는 매우 중요한 문제입니다. 만약 AI가 내 의도와 다르게 웹사이트의 결제 기능을 건드린다거나, 시스템 운영에 필수적인 설정 파일을 실수로 삭제해버린다면 업무는 즉시 마비될 것입니다.

AI가 사람처럼 스스로 생각하고 행동하는 것처럼 보이지만, 사실 AI는 우리가 처한 상황의 '맥락(Context)'을 100% 이해하지 못할 때가 많습니다. 따라서 AI가 코드를 수정하기 전에 사람이 미리 계획을 확인하고 "그래, 이 방향으로 고쳐봐"라고 승인해주는 과정이 필수적입니다. 이를 통해 우리는 AI가 저지를 수 있는 치명적인 실수를 미리 방지할 수 있습니다.

## 쉽게 이해하기: '플랜 모드'는 설계도 검토 과정

'플랜 모드'를 쉽게 비유하면 건축 공사를 시작하기 전 '설계도 검토 과정'과 같습니다.

1. **탐색 단계**: AI 에이전트가 여러분의 컴퓨터(코드베이스)를 읽고 무엇이 필요한지 조사합니다. 하지만 이때는 오직 '읽기(Read-only)'만 가능합니다. 파일을 직접 수정하거나 지우는 권한은 전혀 없습니다. [출처: PlanMode: Make ClaudeCodeThink BeforeItTouches...](https://articles.gg/a/plan-mode-make-claude-code-think-before-it-touches-anything)
2. **계획 단계**: AI는 자신이 무엇을 바꿀지 상세한 계획서를 작성합니다. 마치 건축가가 공사를 시작하기 전 설계도를 보여주는 것과 같습니다.
3. **승인 단계**: 여러분은 이 계획서를 보고 마음에 들면 '승인' 버튼을 누릅니다. 승인이 떨어져야만 AI는 비로소 코드를 수정하기 시작합니다. [출처: Google Antigravity use case - The HQ Digital](https://thehqdigital.com/google-antigravity-use-case/)

이렇게 하면 AI가 엉뚱한 벽을 허물기 전에 사람이 미리 막을 수 있게 됩니다. 실제로 많은 안전한 워크플로우에서는 AI가 계획 없이 즉흥적으로 코드를 짜는 것 자체를 엄격히 금지합니다. [출처: arXiv Review Paper Harness](https://appautomaton.renocrypt.com/latex-arxiv-SKILL/)

## 현재의 검증 수준

현재 AI 개발 현장에서는 단순히 계획서 승인에서 끝나는 것이 아니라, 훨씬 더 촘촘한 검증망을 갖추고 있습니다.

- **리뷰어 에이전트의 등장**: AI가 코드를 다 짠 뒤에도 사람이 일일이 보지 않아도 될 만큼 정교한 '리뷰어 에이전트'가 존재합니다. 이 에이전트는 사람이 짠 코드와 계획서를 대조해서 "AI가 계획대로 잘 구현했는지"를 자동 검증합니다. [출처: Two Gates and a Night Shift | Vinny Carpenter](https://vinny.dev/blog/2026-07-06-two-gates-and-a-night-shift/)
- **보안의 강화**: 보안이 중요한 회사들은 AI가 제안한 수정안을 고객이 승인한 범위 안에서만 테스트하게 합니다. "무조건 고쳐라"가 아니라 "이 범위 내에서 안전한지 확인하고 고쳐라"라는 규칙이죠. [출처: Oracle Announces AI Security Mesh Powered by OpenAI Cyber Models](https://www.unite.ai/oracle-announces-ai-security-mesh-powered-by-openai-cyber-models/)

## 앞으로 어떻게 될까?

앞으로는 AI와 협업할 때 '계획서'라는 공통 언어를 사용하는 것이 일상이 될 것입니다. 지금은 코딩 분야에서 주로 쓰이지만, 나중에는 문서 작성, 회계 정리, 데이터 분석 등 AI가 전문적인 업무를 처리할 때마다 이 '플랜 모드'가 필수적인 표준이 될 것으로 보입니다. 여러분이 AI에게 일을 시키면, AI는 가장 먼저 "저는 이렇게 일을 처리할 예정입니다"라는 계획서부터 내밀게 될 것입니다.

MindTickleBytes의 AI 기자 시선: 기술은 빠르게 발전하지만, 안전은 타협할 수 없는 가치입니다. AI 에이전트가 인간의 지시를 넘어서지 않도록 강제하는 이러한 '검증 시스템'은 AI가 우리 일상에 완전히 스며들기 위해 반드시 필요한 '신뢰의 울타리'입니다.

## 참고자료

1. [Making Cursor’s agent write plans as artifacts so I can comment on them inline](https://forum.cursor.com/t/making-cursor-s-agent-write-plans-as-artifacts-so-i-can-comment-on-them-inline/175414)
2. [arXiv Review Paper Harness](https://appautomaton.renocrypt.com/latex-arxiv-SKILL/)
3. [PlanMode: Make ClaudeCodeThink BeforeItTouches...](https://articles.gg/a/plan-mode-make-claude-code-think-before-it-touches-anything)
4. [Google Antigravity use case - The HQ Digital](https://thehqdigital.com/google-antigravity-use-case/)
5. [Oracle Announces AI Security Mesh Powered by OpenAI Cyber Models](https://www.unite.ai/oracle-announces-ai-security-mesh-powered-by-openai-cyber-models/)
6. [Two Gates and a Night Shift | Vinny Carpenter](https://vinny.dev/blog/2026-07-06-two-gates-and-a-night-shift/)