---
layout: post
title: "내 AI 기획자가 코딩 AI를 '해고'하고 새로 만들자고 한다면?"
description: "AI 기획자가 코딩 AI를 교체하자고 제안했다면, 과연 무엇이 문제일까요? AI 코딩 에이전트의 현실과 한계를 알아봅니다."
summary: "AI 코딩 에이전트는 사람이 아이디어를 실현하도록 돕는 도구일 뿐, 스스로 판단하는 직원이 아님을 이해하고 올바르게 활용하는 방법을 제시합니다."
tags: [AI, 코딩, 개발, 기획, 에이전트]
image: 2026-08-01-My-PM-agent-suggests-firing-my-coding-agents-and-creating-a-replacement.jpg
image_alt: "복잡한 코드 화면을 바라보는 고민에 빠진 기획자의 모습"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "에이전트를 도구로 볼지 직원으로 볼지에 따라 성과가 달라집니다. AI의 제안은 개선의 신호이지 무조건적인 해고의 신호가 아닙니다."
quiz:
  - question: "코딩 AI 에이전트의 정의로 가장 적절한 것은?"
    choices: ["스스로 결정하는 자율적 직원", "목표 달성을 위해 도구를 반복적으로 사용하는 LLM", "코드 없이 앱을 만드는 마법"]
    answer: 1
    explanation: "AI 에이전트는 LLM이 주어진 목표를 달성하기 위해 필요한 도구를 반복적으로 실행하는 구조를 의미합니다."
  - question: "코딩 AI가 기존의 지저분한 코드 패턴을 복제하는 이유는?"
    choices: ["데이터베이스에 접속해서", "기존 코드를 유효한 패턴으로 인식해서", "창의적으로 코드를 짜기 위해"]
    answer: 1
    explanation: "AI는 코드베이스에 존재하는 방식을 분석하므로, 개발자가 남겨둔 '임시 코드'도 유효한 패턴으로 학습해 복제할 위험이 있습니다."
  - question: "AI 코딩 에이전트를 가장 잘 활용하는 방법은?"
    choices: ["모든 계획을 AI에게 완전히 맡긴다", "사람의 아이디어를 구현하는 도구로 활용한다", "코드를 모두 AI가 짜도록 방치한다"]
    answer: 1
    explanation: "코딩 에이전트는 인간의 의도를 바탕으로 아이디어를 실현하는 도구로 사용할 때 가장 효율적입니다."
lang: ko
ref: 2026-08-01-My-PM-agent-suggests-firing-my-coding-agents-and-creating-a-replacement
audio: 2026-08-01-My-PM-agent-suggests-firing-my-coding-agents-and-creating-a-replacement.mp3
permalink: /2026/08/01/My-PM-agent-suggests-firing-my-coding-agents-and-creating-a-replacement/
---

상상해보세요. 아침에 출근했는데, 우리 프로젝트의 살림을 맡고 있는 AI 기획자(PM)가 단호한 말투로 메시지를 보냅니다. "우리 팀의 코딩 AI를 다 해고하고, 더 나은 걸로 새로 꾸리는 게 좋겠습니다." 

마치 오랫동안 함께 일한 팀 동료를 바꾸자는 것 같은 이 충격적인 제안, 정말 AI가 스스로 판단해서 내린 결론일까요? 아니면 우리가 도구에 대해 너무 많은 기대를 하고 있는 걸까요? 이 질문을 통해 AI 코딩 에이전트의 현실과 우리가 그들을 대하는 태도를 점검해 보겠습니다.

### 이게 왜 중요한가요?

최근 많은 개발자와 기획자가 AI 코딩 에이전트를 업무에 도입하고 있습니다. 마치 사람처럼 코드를 뚝딱 만들어내는 AI를 보며 "이제 개발자가 사라지는 것 아니냐"는 기대와 불안이 교차하기도 하죠. 

하지만 현실은 조금 다릅니다. AI가 코드를 잘못 짜거나, 엉뚱한 방향으로 개발을 진행해 시간을 낭비하는 경우도 적지 않습니다. 겉보기엔 사람 동료 같지만, 사실 이들은 정교하게 설계된 소프트웨어 도구입니다. 이들의 한계와 특성을 이해하지 못하면, 프로젝트의 생산성은커녕 오히려 업무 효율이 크게 떨어질 수 있습니다.

### 쉽게 이해하기: 코딩 AI는 마법사가 아니라 '필터'입니다

AI 에이전트란 무엇일까요? 쉽게 말해 **'목표를 달성하기 위해 필요한 도구들을 스스로 반복해서 사용하는 거대언어모델(LLM)'**을 뜻합니다 [AI 에이전트 정의 참고](https://simonw.github.io/nicar-2026-coding-agents/coding-agents.html).

이 과정을 사진 앱의 필터에 비유해 볼까요? 우리가 "사진을 예쁘게 해줘"라고 말하면, 앱은 명도 조절, 색감 보정, 선명도 강화 등 여러 가지 필터를 알아서 순서대로 적용합니다. 코딩 AI도 비슷합니다. 우리가 "이 기능을 만들어줘"라고 요청하면 AI는 코드베이스를 검색하고, 파일을 수정하고, 테스트를 돌리는 '필터(도구)'들을 조합해 결과를 만들어냅니다.

하지만 문제가 있습니다. 많은 AI 도구에 있는 '계획 모드(Plan Mode)'는 사실 사용자의 요구사항을 텍스트로 처리하는 일종의 '제안'에 불과합니다 [계획 모드의 한계](https://blog.apiad.net/p/the-anatomy-of-ai-coding-agents). AI가 "먼저 이렇게 계획하고 이렇게 구현하겠다"라고 의기양양하게 선언하지만, 실제 작업 중에는 의도가 흐려지거나 급한 마음에 계획을 무시하고 바로 코드를 짜버리기도 합니다. 마치 요리사가 레시피를 무시하고 눈대중으로 간을 맞추는 것과 비슷하죠.

더 큰 문제는 AI의 '학습된 습관'입니다. AI는 코드베이스에 이미 존재하는 코드를 분석하며 학습합니다. 만약 개발자가 예전에 급하게 짜놓은 '임시 hack 코드'가 있다면, AI는 그것을 "아, 이 프로젝트는 이렇게 짜는 게 패턴이구나!"라고 착각합니다. 그 결과, 지저분한 방식을 그대로 복제해 프로젝트 전체를 혼란에 빠뜨리곤 합니다 [코드 복제 문제](https://eliteaiadvantage.com/blog/stop-ai-coding-agents-rewriting-code-incorrectly).

### 현재 상황: 기대와 현실의 간극

현재 많은 사용자가 AI 코딩 도구를 사용하고 있지만, 기대치와 현실 사이에는 분명한 간극이 존재합니다 [사용자 경험 참고](https://news.ycombinator.com/item?id=47867857). 에이전트가 "코딩을 마법처럼 해낸다"고 생각하기 쉽지만, 사실 이들은 인간의 아이디어를 실현하는 효율적인 도구일 뿐입니다 [도구로서의 에이전트](https://arstechnica.com/information-technology/2026/01/10-things-i-learned-from-burning-myself-out-with-ai-coding-agents/).

이미 많은 팀이 AI를 도입했지만, 에이전트가 완벽한 직원이 아니라는 점을 점차 깨닫고 있습니다. 한 사용자는 "에이전트가 생산성을 높여주긴 하지만, 정작 중요한 '무엇을 만들 것인가'를 결정하는 의사결정의 병목 현상은 여전하다"고 지적합니다 [개발의 병목](https://kasperjunge.com/blog/should-pms-code-with-agents/). 또한, 지시 사항이 담긴 설정 파일(`AGENTS.md`)이 너무 방대해지면 오히려 AI가 정보 과부하로 인해 혼란을 겪어 성능이 떨어지는 현상도 발견되었습니다 [성능 저하 원인](https://medium.com/coding-nexus/bad-agents-md-are-making-your-coding-agent-worse-0d0aa8aa6585).

### 앞으로 어떻게 될까?

앞으로는 '에이전트 관리자(Agent Manager)'라는 새로운 역할이 중요해질 전망입니다 [역할의 변화](https://productgrindhq.substack.com/p/from-product-manager-to-agent-manager). 기획자나 관리자가 단순한 도구 사용자를 넘어, 여러 AI 에이전트를 운영하고 조정하는 역량이 필수적이 될 것입니다. 이제 AI에게 모든 것을 맡기고 "알아서 해줘"라고 방치하는 시대는 지났습니다. 에이전트가 우리 프로젝트의 맥락을 잘 이해하도록 돕고, 잘못된 패턴을 학습하지 않도록 끊임없이 가이드를 제공하는 과정이 핵심이 될 것입니다.

### MindTickleBytes의 AI 기자 시선

AI 코딩 에이전트가 내린 '해고 제안'은 정말 그들을 교체하라는 통보가 아닙니다. 그것은 현재의 운영 방식에 개선이 필요하다는 시스템의 경고등입니다. 에이전트를 자율적인 직원이 아닌 고성능 도구로 대할 때, 비로소 우리는 AI가 가진 진짜 힘을 끌어낼 수 있을 것입니다. 여러분의 AI 동료는 여러분이 어떻게 관리하느냐에 따라 최고의 팀원이 될 수도, 혹은 가장 손이 많이 가는 도구가 될 수도 있습니다.

## 참고자료

1. Why Your Coding Agent Gets Stuck and How to Fix It with Parth Patil - YouTube ([https://www.youtube.com/watch?v=2Jb83UWqGe4](https://www.youtube.com/watch?v=2Jb83UWqGe4))
2. Ask HN: How do people use coding agents? | Hacker News ([https://news.ycombinator.com/item?id=47867857](https://news.ycombinator.com/item?id=47867857))
3. 10 things I learned from burning myself out with AI coding agents - Ars Technica ([https://arstechnica.com/information-technology/2026/01/10-things-i-learned-from-burning-myself-out-with-ai-coding-agents/](https://arstechnica.com/information-technology/2026/01/10-things-i-learned-from-burning-myself-out-with-ai-coding-agents/))
4. I used AI coding agents for a week at work. Here is what actually happened. | by Emily | Medium ([https://medium.com/@emilyhustlenyc/i-used-ai-coding-agents-for-a-week-at-work-here-is-what-actually-happened-765d723f1c53](https://medium.com/@emilyhustlenyc/i-used-ai-coding-agents-for-a-week-at-work-here-is-what-actually-happened-765d723f1c53))
5. How to Stop AI Coding Agents from Rewriting Code Incorrectly ([https://eliteaiadvantage.com/blog/stop-ai-coding-agents-rewriting-code-incorrectly](https://eliteaiadvantage.com/blog/stop-ai-coding-agents-rewriting-code-incorrectly))
6. Bad AGENTS.md Are Making Your Coding Agent Worse | by Code Coup | Coding Nexus | Medium ([https://medium.com/coding-nexus/bad-agents-md-are-making-your-coding-agent-worse-0d0aa8aa6585](https://medium.com/coding-nexus/bad-agents-md-are-making-your-coding-agent-worse-0d0aa8aa6585))
7. Coding Agents in Feb 2026 ([https://calv.info/agents-feb-2026](https://calv.info/agents-feb-2026))
8. Everyone got excited they can suddenly code, and completely missed the point — Kasper Junge ([https://kasperjunge.com/blog/should-pms-code-with-agents/](https://kasperjunge.com/blog/should-pms-code-with-agents/))
9. 10 AI Agents for Product Managers | MindStudio ([https://www.mindstudio.ai/blog/ai-agents-for-product-managers](https://www.mindstudio.ai/blog/ai-agents-for-product-managers))
10. AI Coding Agents, Deconstructed - by Alejandro Piad Morffis ([https://blog.apiad.net/p/the-anatomy-of-ai-coding-agents](https://blog.apiad.net/p/the-anatomy-of-ai-coding-agents))
11. Coding agents - Coding agents for data analysis ([https://simonw.github.io/nicar-2026-coding-agents/coding-agents.html](https://simonw.github.io/nicar-2026-coding-agents/coding-agents.html))
12. From Product Manager to Agent Manager - by Zakir Tyebjee ([https://productgrindhq.substack.com/p/from-product-manager-to-agent-manager](https://productgrindhq.substack.com/p/from-product-manager-to-agent-manager))