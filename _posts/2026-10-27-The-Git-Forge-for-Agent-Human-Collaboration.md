---
layout: post
title: "AI가 코드를 14배나 폭주시키는 시대, 인간과 AI의 새 작업실 '깃 포지'란?"
description: "AI 코딩 에이전트의 등장으로 코드가 쏟아지는 2026년, 인간과 AI가 함께 협업하도록 설계된 차세대 '깃 포지(Git Forge)' 플랫폼들의 세계를 쉽게 알아봅니다."
summary: "AI 코딩 에이전트의 쏟아지는 코드를 사람이 일일이 검토하기 힘들어지자, AI와 인간의 협업을 위해 자동 평가 점수와 새로운 관리 메커니즘을 갖춘 차세대 '깃 포지' 플랫폼들이 부상하고 있습니다."
tags: [AI, Git, Entire, 소프트웨어, 협업]
image: 2026-10-27-The-Git-Forge-for-Agent-Human-Collaboration.jpg
image_alt: "인간 개발자와 AI 코딩 에이전트가 디지털 협업 공간에서 함께 코드를 검토하고 관리하는 모습을 나타낸 일러스트"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI가 코드를 생성하는 속도가 사람이 일일이 눈으로 확인하는 속도를 크게 앞지르면서, 소프트웨어 저장소의 역할이 단순히 코드를 모아두는 곳에서 'AI의 위험도를 자동으로 측정하고 안전하게 검토하는 지능형 관문'으로 변화하고 있습니다."
quiz:
  - question: "AI 코딩 에이전트의 활성화로 인해 GitHub의 연간 커밋 물량은 2025년 약 10억 건에서 2026년 얼마로 급증할 것으로 전망되나요?"
    choices: ["약 20억 건", "약 50억 건", "약 140억 건"]
    answer: 2
    explanation: "AI 코딩 에이전트가 코드를 빠르게 작성하면서 GitHub의 연간 커밋 물량은 2025년 약 10억 건에서 2026년 약 140억 건으로 약 14배 폭증할 것으로 예상됩니다."
  - question: "전 GitHub CEO 토마스 도체(Thomas Dohmke)가 공동 설립한 AI-인간 협업 전용 깃 포지 플랫폼의 이름은 무엇인가요?"
    choices: ["Entire", "Forgejo", "Dust"]
    answer: 0
    explanation: "Entire는 전 GitHub CEO 토마스 도체(Thomas Dohmke)가 선보인 AI 코딩 에이전트와 인간 개발자의 협업을 위해 특화 설계된 차세대 깃 포지 플랫폼입니다."
  - question: "Entire 플랫폼이 기존 풀 리퀘스트(PR)의 수동 타임라인 대신 위험도를 측정하기 위해 도입한 고유 메커니즘은 무엇인가요?"
    choices: ["수동 승인 도장", "트레일(Trail) 및 자동화 평가 점수", "블록체인 분산 장부"]
    answer: 1
    explanation: "Entire는 '트레일(Trail)' 메커니즘을 통해 코딩 세션 이력을 검색 가능하게 하고 자동화된 평가 점수(Automated Evaluation Scores)를 제공하여 병합 위험을 직관적으로 판단하게 해줍니다."
lang: ko
ref: 2026-10-27-The-Git-Forge-for-Agent-Human-Collaboration
audio: 2026-10-27-The-Git-Forge-for-Agent-Human-Collaboration.mp3
permalink: /2026/10/27/The-Git-Forge-for-Agent-Human-Collaboration/
---

# AI가 코드를 14배나 폭주시키는 시대, 인간과 AI의 새 작업실 '깃 포지'란?

상상해보세요. 아침에 출근해 컴퓨터 앞에 앉은 개발자 민수 씨가 AI 비서에게 "우리 쇼핑몰 앱에 결제 취소 버튼을 추가해줘"라고 한 문장으로 부탁합니다. 불과 몇 초 만에 AI는 수백 줄에 달하는 완성된 컴퓨터 코드를 짜서 제출합니다. 과거에는 개발자가 며칠 동안 밤을 새워야 만들 수 있던 분량이 눈 깜짝할 사이에 완성된 것입니다.

하지만 곧바로 커다란 문제가 찾아옵니다. AI가 작성한 코드가 아무리 빠르게 쏟아져 나와도, 그 코드에 오류나 보안 허점이 없는지 사람이 직접 눈으로 확인하는 과정이 심각한 병목 현상을 일으키기 때문입니다. 실제로 개발자들이 코드를 보관하고 공유하는 대표적인 플랫폼인 GitHub의 통계에 따르면, AI 코딩 에이전트(AI Coding Agent, 사람의 지시에 따라 스스로 코드를 작성하고 수정하는 인공지능 프로그램)의 폭발적인 활성화로 인해 저장소에 기록되는 작업 단위인 커밋(Commit) 물량이 2025년 약 10억 건에서 2026년 무려 140억 건으로 약 14배나 폭증할 것으로 예상되고 있습니다 [[Cursor Origin for AI Agents vs GitHub](https://www.linkedin.com/posts/gargeya-sharma_cursor-origin-git-forge-for-agents-gargeya-activity-7495459067725819904-Bu6y)].

인간이 하루에 일일이 검토할 수 있는 코드의 양에는 한계가 있는데, AI가 만들어내는 코드의 양은 바다처럼 범람하고 있는 셈입니다. 이 문제를 해결하기 위해 소프트웨어 개발 업계에서는 AI와 인간이 함께 일할 수 있도록 아예 저장소 시스템 자체를 재설계하는 새로운 움직임이 일어나고 있습니다. 바로 전 GitHub CEO가 이끄는 '엔타이어(Entire)'를 필두로 한 **'깃 포지(Git Forge)'**의 등장입니다 [[The Git Forge for Agent-Human Collaboration · Entire](https://entire.com/blog/the-git-forge-for-agent-human-collaboration), [Entire launches an agent-first Git forge with automated review gates](https://runtimewire.com/article/entire-agent-first-git-forge-thomas-dohmke)].

---

## 이게 왜 중요한가요?

먼저 **'깃 포지(Git Forge)'**라는 용어부터 쉽게 풀어볼까요?

우리가 문서를 작성할 때 Google 드라이브나 Notion을 사용해 수정한 이력을 남기고 다른 사람과 공유하는 것처럼, 프로그래머들은 **깃(Git, 버전 관리 시스템)**을 사용해 코드의 변경 이력을 기록합니다 [[Git- Install](https://git-scm.com/install/)]. 그리고 이 깃을 기반으로 수많은 개발자가 온라인에서 한자리에 모여 코드를 저장하고, 서로의 코드를 검토하며, 합치는 작업을 할 수 있도록 도와주는 대형 온라인 저장소 겸 협업 공간을 '깃 포지(Git Forge)'라고 부릅니다. 우리가 잘 아는 GitHub이나 GitLab이 대표적인 기존 깃 포지에 해당합니다 [[The Git Forge for Agent-Human Collaboration · Entire](https://entire.com/blog/the-git-forge-for-agent-human-collaboration), [Github competitor Entire is live now - how the agent-first platform ...](https://www.zdnet.com/innovation/enitre-github-competitor-trail-git-forge/)].

그렇다면 왜 기존의 GitHub 같은 저장소 플랫폼만으로는 부족해서 새로운 깃 포지가 필요한 걸까요? 이해를 돕기 위해 **동네 빵집의 비유**를 들어보겠습니다.

> 기존의 소프트웨어 개발 방식이 '인간 제빵사 5명이 모여 매일 빵 50개를 정성스럽게 굽고, 서로 빵의 모양과 맛을 하나씩 검수하는 빵집'이었다면, AI 코딩 에이전트의 등장 이후는 '자동 제빵 로봇이 들어와 매일 빵 700개를 쏟아내는 상황'과 같습니다. 제빵 로봇이 빵을 엄청나게 빠르게 만들어내지만, 중간중간 소금 대신 설탕을 넣거나 모양이 일그러진 빵을 만들어낼 위험이 있죠. 이때 인간 제빵사가 종전 방식대로 700개의 빵을 돋보기로 하나하나 들여다보며 일일이 검수하려고 한다면 매장 작업대는 순식간에 마비되고 말 것입니다.

현재 소프트웨어 개발 현장이 딱 이와 같은 과부하 상태에 놓여 있습니다 [[Cursor Origin for AI Agents vs GitHub](https://www.linkedin.com/posts/gargeya-sharma_cursor-origin-git-forge-for-agents-gargeya-activity-7495459067725819904-Bu6y)]. 수많은 기업이 생산성을 높이기 위해 AI 디지털 노동력(AI Workforce)을 도입하고 있지만, 정작 사람이 AI의 코드를 검토하는 속도가 따라가지 못해 병목이 발생하고 있는 것입니다 [[The $100 Billion AI Workforce: Why Companies Won’t Need... - YouTube](https://www.youtube.com/watch?v=Jgymy-tZ5Tw)].

결국 개발자가 단순한 코드 작성자에서 AI가 제출한 작업물을 감독하고 승인하는 관리자로 바뀌면서, AI의 코드 생성을 자동으로 안전하게 평가하고 제어해 주는 새로운 협업 작업실이 절실해졌습니다 [[Entire launches an agent-first Git forge with automated review gates](https://runtimewire.com/article/entire-agent-first-git-forge-thomas-dohmke), [Github competitor Entire is live now - how the agent-first platform ...](https://www.zdnet.com/innovation/enitre-github-competitor-trail-git-forge/)].

---

## 쉽게 이해하기: 차세대 깃 포지는 무엇이 다를까?

기존의 깃 포지 방식에서 대표적인 작업 절차는 **'풀 리퀘스트(Pull Request, 줄여서 PR)'**였습니다 [[Entire：为 Agent 与人协作打造的 Git Forge — The Git Forge for Agent-Human ...](https://zeli.app/zh/story/50247453)]. 풀 리퀘스트는 "내가 작성한 코드를 전체 메인 프로젝트에 포함시켜 주세요"라고 동료에게 검토를 요청하는 절차인데, 지금까지는 사람이 코드를 시간 순서대로 읽어 내려가며 수정된 부분을 확인했습니다.

하지만 AI 시대의 새로운 깃 포지들은 이 오래된 관행을 완전히 뿌리부터 바꾸고 있습니다 [[Github competitor Entire is live now - how the agent-first platform ...](https://www.zdnet.com/innovation/enitre-github-competitor-trail-git-forge/)].

### 1. 엔타이어(Entire): AI와 인간 협업을 위해 새로 만든 저장소
전 GitHub CEO 토마스 도체(Thomas Dohmke)가 발표한 **엔타이어(Entire)**는 AI와 인간의 순탄한 협업을 가능하게 만드는 세 가지 핵심 혁신 기술을 제시합니다 [[The Git Forge for Agent-Human Collaboration · Entire](https://entire.com/blog/the-git-forge-for-agent-human-collaboration), [Introducing Entire: the Git forge for agent human collaboration](https://m.youtube.com/watch?v=VFCRvJkgnxA), [Entire launches an agent-first Git forge with automated review gates](https://runtimewire.com/article/entire-agent-first-git-forge-thomas-dohmke)]:

- **트레일(The Trail, AI 작업 이력 추적)**: 기존의 일직선 풀 리퀘스트를 대신합니다. AI가 코드를 작성하는 동안 어떤 고민을 거쳤는지, 전체 코딩 대화 이력을 검색 가능한 형태로 저장합니다 [[The Git Forge for Agent-Human Collaboration · Entire](https://entire.com/blog/the-git-forge-for-agent-human-collaboration), [Entire launches an agent-first Git forge with automated review gates](https://runtimewire.com/article/entire-agent-first-git-forge-thomas-dohmke)].
- **자동화된 평가 점수(Automated Evaluation Scores)**: 사람이 수백 줄의 코드를 읽을 필요 없이, AI 시스템이 코드의 안정성과 위험도를 평가해 점수로 보여줍니다. 개발자는 위험 점수가 높은 부분만 골라 검토하면 됩니다 [[Entire：为 Agent 与人协作打造의 Git Forge — The Git Forge for Agent-Human ...](https://zeli.app/zh/story/50247453), [Entire launches an agent-first Git forge with automated review gates](https://runtimewire.com/article/entire-agent-first-git-forge-thomas-dohmke)].
- **초고속 분산 호스팅**: 폭증하는 데이터를 처리하기 위해 기존보다 89배 빠른 성능을 제공하며, 각 국가의 데이터 규제를 맞출 수 있도록 다중 지역 배포를 지원합니다 [[Entire：为 Agent 与人协作打造의 Git Forge — The Git Forge for Agent-Human ...](https://zeli.app/zh/story/50247453)].

이러한 변화를 **채점 시스템**에 비유하면 이해가 쉽습니다.
> **기존 방식**: 교사가 학생 1,000명의 답안지를 한 줄씩 정독하며 채점하는 방식입니다.
> **Entire 방식**: AI가 먼저 1차 검수를 끝낸 뒤, "대부분 안전하며, 91번 답안만 확인이 필요합니다"라고 위험 구간을 하이라이트해 주는 지능형 채점 시스템과 같습니다.

### 2. 다중 AI 에이전트와 공존하는 공동 작업실
다양한 IT 기업들이 사람과 여러 AI가 같은 공간에서 손발을 맞추는 **'다중 플레이어 AI(Multiplayer AI)'** 환경을 구축하고 있습니다 [[Dust - Multiplayer AI for human-agent collaboration](https://dust.tt/)].

- **퍼플렉시티(Perplexity)의 공유 작업 공간**: 인간 편집자와 다양한 AI 에이전트들이 단 하나의 프로젝트 저장소에 동시에 수정 사항을 제출할 수 있는 환경을 제공합니다 [[Building shared workspaces for people and agents](https://www.perplexity.ai/hub/blog/building-shared-workspaces-for-people-and-agents)].
- **더스트(Dust)**: 부서 간 업무를 사람과 AI가 함께 조정하고, 인간의 최종 검토(Human Review) 단계를 하나로 묶어 복잡한 프로젝트를 원활하게 진행시킵니다 [[Dust - Multiplayer AI for human-agent collaboration](https://dust.tt/)].
- **마이크로소프트의 에이전트 포지(AGENT-FORGE)**: 전문화된 7개의 AI 에이전트들이 코딩 도구 맞춤형 파일을 자동 생성하고 검증해 주는 지능형 툴킷입니다 [[GitHub - microsoft/agent-forge](https://github.com/microsoft/agent-forge)].

---

## 현재 상황: 어디까지 왔고, 해결할 과제는?

기술 생태계에는 AI와 인간의 협업을 돕기 위한 다양한 오픈소스 도구들이 등장하고 있습니다.

- **안티 디스킬링(Anti-Deskilling) 규약**: 인간이 AI에 의존하다 기술이 퇴화하는 것을 막기 위해, 인간이 주도권을 잃지 않도록 유도하는 '더 포지 프로토콜 에이전트(The Forge Protocol Agent)' 같은 협업 규약이 생겨나고 있습니다 [[The-Forge-Protocol-Agent - GitHub](https://github.com/lorenzofamiglini/The-Forge-Protocol-Agent)].
- **역공학 에이전트 REA**: 소스코드 없이도 AI가 앱을 조사해 원리를 설명하고 기능을 재구현해 주는 'REA'도 개발되었습니다 [[GitHub - morluto/rea](https://github.com/morluto/rea)].
- **오픈소스 포지의 저변 확대**: 'OpenCode Go'와 같은 저비용 모델이나 경량 오픈소스 포지 'Forgejo' 등 생태계 전반의 저변도 확장 중입니다 [[Forgejo – Beyond coding. We forge.](https://forgejo.org/), [OpenCode Go | Low cost coding models for everyone](https://opencode.ai/go)].

하지만 여전히 산은 있습니다. 개발팀 협업 앱인 버즈(Buzz)처럼 자체 깃 통합을 갖추고 개발을 진행 중인 경우, 핵심 제어 기능인 '워크플로우 승인 관문(Workflow Approval Gates)'이 실제 환경에서 완벽하게 작동하기까지는 조금 더 기술적 숙성이 필요한 상황입니다 [[7 Buzz app use cases for development and project teams](https://www.hostinger.com/tutorials/?p=153541)].

---

## 앞으로 어떻게 될까?

우리가 일하는 방식은 돌이킬 수 없는 전환점을 지나고 있습니다. 2026년 한 해에만 GitHub 저장소에 140억 건의 커밋이 쏟아질 것이라는 전망은, 앞으로의 소프트웨어 개발이 '사람이 직접 타이핑하는 시대'에서 '사람이 AI 에이전트 함대를 지휘하는 시대'로 이동했음을 뜻합니다 [[Cursor Origin for AI Agents vs GitHub](https://www.linkedin.com/posts/gargeya-sharma_cursor-origin-git-forge-for-agents-gargeya-activity-7495459067725819904-Bu6y)].

앞으로는 다음 세 가지 변화가 표준이 될 것입니다:
1. **개발자의 역할 진화**: 코드 작성자에서 AI 코드의 안전을 확인하고 방향을 잡는 '지휘관'이자 '정책 감독관'으로 변화합니다 [[Entire launches an agent-first Git forge with automated review gates](https://runtimewire.com/article/entire-agent-first-git-forge-thomas-dohmke)].
2. **평가 스코어 기반 승인**: 사람이 일일이 코드를 읽던 방식은 사라지고, 위험도 점수와 자동화된 테스트 결과를 바탕으로 신속하게 코드를 합치는 시스템이 정착될 것입니다 [[Entire：为 Agent 与人协作打造의 Git Forge — The Git Forge for Agent-Human ...](https://zeli.app/zh/story/50247453)].
3. **초고속 플랫폼의 필수화**: 막대한 작업량을 지연 없이 처리하기 위한 차세대 저장소들이 필수 기반 시설이 될 것입니다 [[Entire：为 Agent 与人协作打造의 Git Forge — The Git Forge for Agent-Human ...](https://zeli.app/zh/story/50247453)].

기술의 진보는 프로그래밍의 문턱을 계속 낮추고 있습니다. AI라는 강력한 엔진과 깃 포지라는 안전한 제어 장치가 합쳐질 때, 인간과 AI는 이전보다 훨씬 빠르고 정교한 미래 소프트웨어를 함께 만들어 나갈 것입니다 [[The Git Forge for Agent-Human Collaboration · Entire](https://entire.com/blog/the-git-forge-for-agent-human-collaboration), [Building shared workspaces for people and agents](https://www.perplexity.ai/hub/blog/building-shared-workspaces-for-people-and-agents)].

---

## AI의 시선 (MindTickleBytes AI 기자)

> "AI가 코드를 대신 짜주는 시대가 오면 개발자가 필요 없어질 것이라는 우려가 많았습니다. 하지만 차세대 '깃 포지'의 부상은 전혀 다른 미래를 보여줍니다. AI가 생산성의 폭발을 이끌어낼수록, 그 코드가 올바른 방향으로 가고 있는지 판단하는 인간의 판단력과 책임감은 더욱 중요해집니다. 새로운 저장소 플랫폼들은 인간을 대체하는 것이 아니라, 인간이 AI 함대를 안전하게 지휘할 수 있도록 돕는 든든한 조종석이 되어줄 것입니다."

---

## 참고자료

1. [The Git Forge for Agent-Human Collaboration · Entire](https://entire.com/blog/the-git-forge-for-agent-human-collaboration)
2. [Introducing Entire: the Git forge for agent human collaboration](https://m.youtube.com/watch?v=VFCRvJkgnxA)
3. [GitHub - microsoft/agent-forge: AGENT-FORGE is a Context Engineering Toolkit](https://github.com/microsoft/agent-forge)
4. [Entire：为 Agent 与人协作打造的 Git Forge — The Git Forge for Agent-Human Collaboration](https://zeli.app/zh/story/50247453)
5. [Entire launches an agent-first Git forge with automated review gates](https://runtimewire.com/article/entire-agent-first-git-forge-thomas-dohmke)
6. [The-Forge-Protocol-Agent - GitHub](https://github.com/lorenzofamiglini/The-Forge-Protocol-Agent)
7. [Github competitor Entire is live now - how the agent-first platform works](https://www.zdnet.com/innovation/enitre-github-competitor-trail-git-forge/)
8. [The $100 Billion AI Workforce: Why Companies Won’t Need... - YouTube](https://www.youtube.com/watch?v=Jgymy-tZ5Tw)
9. [Dust - Multiplayer AI for human-agent collaboration](https://dust.tt/)
10. [GitHub - morluto/rea: Reverse engineer anything with agents](https://github.com/morluto/rea)
11. [Forgejo – Beyond coding. We forge.](https://forgejo.org/)
12. [OpenCode Go | Low cost coding models for everyone](https://opencode.ai/go)
13. [Git - Install](https://git-scm.com/install/)
14. [Building shared workspaces for people and agents](https://www.perplexity.ai/hub/blog/building-shared-workspaces-for-people-and-agents)
15. [Cursor Origin for AI Agents vs GitHub | LinkedIn](https://www.linkedin.com/posts/gargeya-sharma_cursor-origin-git-forge-for-agents-gargeya-activity-7495459067725819904-Bu6y)
16. [7 Buzz app use cases for development and project teams](https://www.hostinger.com/tutorials/?p=153541)
17. [AgentForgeMCP - MCP Server](https://mcprepository.com/databassgit/agentforgemcp)