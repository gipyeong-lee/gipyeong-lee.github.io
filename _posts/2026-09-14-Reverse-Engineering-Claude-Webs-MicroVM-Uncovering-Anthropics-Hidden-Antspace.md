---
layout: post
title: "AI가 내 앱을 만들고 직접 배포까지? Anthropic의 비밀 프로젝트 'Antspace'를 파헤치다"
description: "Anthropic의 Claude가 코드를 작성하는 것을 넘어 직접 웹 서비스를 배포하는 비밀 플랫폼 'Antspace'의 정체를 분석합니다."
summary: "Anthropic이 Claude Code 환경 내에 자체 배포 플랫폼인 'Antspace'를 숨겨두고 AI가 직접 앱을 개발하고 호스팅하는 수직 통합 생태계를 구축하고 있습니다."
tags: [Anthropic, Claude, AI, 클라우드, Antspace, 개발]
image: 2026-09-14-Reverse-Engineering-Claude-Webs-MicroVM-Uncovering-Anthropics-Hidden-Antspace.jpg
image_alt: "Claude Code 개발 환경인 파이어크래커 마이크로VM과 그 내부의 비밀스러운 배포 플랫폼 Antspace를 상징하는 추상적인 일러스트."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Anthropic의 이러한 행보는 AI 모델이 단순히 텍스트를 생성하는 도구를 넘어, 전체 개발 생태계를 장악하는 '에이전트 중심 플랫폼'으로 진화하고 있음을 보여줍니다."
quiz:
  - question: "Anthropic이 개발 중인 내부 배포 플랫폼의 명칭은 무엇인가요?"
    choices: ["Vercel", "Antspace", "Baku"]
    answer: 1
    explanation: "'Antspace'는 Anthropic이 개발한 내부 배포 플랫폼(PaaS)입니다. 'Baku'는 프로젝트 빌더 환경의 코드네임입니다."
  - question: "Claude Code Web 환경이 실행되는 기술적 기반은 무엇인가요?"
    choices: ["Firecracker 마이크로VM", "AWS Lambda", "도커 컨테이너"]
    answer: 0
    explanation: "Claude Code Web은 4개의 vCPU와 16GB RAM을 갖춘 Firecracker 마이크로VM 위에서 동작합니다."
  - question: "Anthropic이 자체 배포 플랫폼을 구축하는 이유는 무엇으로 추측되나요?"
    choices: ["단순한 기술 과시", "수직 통합을 통한 서비스 생태계 장악", "기존 플랫폼과의 협업 강화"]
    answer: 1
    explanation: "AI 모델, 개발 환경, 그리고 배포까지 전 과정을 수직 통합하여 사용자가 외부 플랫폼 없이도 완벽한 서비스를 완성하게 하려는 전략으로 분석됩니다."
lang: ko
ref: 2026-09-14-Reverse-Engineering-Claude-Webs-MicroVM-Uncovering-Anthropics-Hidden-Antspace
audio: 2026-09-14-Reverse-Engineering-Claude-Webs-MicroVM-Uncovering-Anthropics-Hidden-Antspace.mp3
permalink: /2026/09/14/Reverse-Engineering-Claude-Webs-MicroVM-Uncovering-Anthropics-Hidden-Antspace/
---

아침에 일어나서 AI에게 "오늘 내가 생각한 아이디어로 웹 서비스를 하나 만들어줘"라고 말하고, 커피를 한 잔 마시는 동안 결과물까지 세상에 배포되는 미래를 상상해 본 적 있나요? 지금은 여러 도구를 오가며 복잡한 과정을 거쳐야 하지만, Anthropic의 최근 행보를 보면 이 과정이 아주 매끄러워질 것으로 보입니다. 최근 보안 전문가들이 Claude Code 환경을 분석하다가 Anthropic이 숨겨두었던 놀라운 프로젝트를 발견했습니다.

### 이게 왜 중요한가요?

지금까지 AI는 주로 코드를 제안하거나 수정해 주는 '조수' 역할에 머물러 있었습니다. 사용자는 AI가 준 코드를 복사해서 내 컴퓨터에 붙여넣고, 다시 웹 서비스로 배포하기 위해 다른 플랫폼(예: Vercel)을 이용해야 했죠. 하지만 Anthropic이 'Antspace(앤트스페이스)'라는 자체 배포 플랫폼을 준비하고 있다는 사실은, AI가 **"생각하고, 코드를 짜고, 서버에 올리기까지"** 전 과정을 단독으로 수행하는 '원스톱 개발자'로 진화하고 있음을 의미합니다[Source 1](https://aprilnea.me/en/blog/reverse-engineering-claude-code-antspace), [Source 6](https://x.com/AprilNEA/status/2034209430158619084), [Source 11](https://www.romanpeschke.com/guides/claude-code-scheduled-tasks/). 사용자는 복잡한 기술적 지식 없이도 AI만으로 아이디어를 서비스로 전환할 수 있는 시대가 오고 있는 것입니다.

### 쉽게 이해하기: '주방'의 진화

이해하기 쉽게 비유해 볼까요? 예전의 AI 개발 환경이 **'재료를 다듬어주는 칼'**이었다면, Antspace는 **'재료부터 요리, 배달까지 모두 해주는 중앙 집중형 주방'**과 같습니다.

지금까지는 여러분이 직접 식재료(코드)를 받아 주방(클라우드 플랫폼)으로 달려가서 요리(배포)를 해야 했습니다. 하지만 Anthropic은 Claude라는 셰프에게 아예 전용 주방을 마련해 주었습니다. 이것이 바로 '바쿠(Baku)'라고 불리는 전용 환경입니다. 사용자가 "웹 앱 만들어줘"라고 말하면, 시스템은 순식간에 **'파이어크래커(Firecracker) 마이크로VM'**이라는 가상의 공간을 만듭니다[Source 2](https://www.weex.com/news/detail/reverse-engineering-claude-code-reveals-anthropicas-undisclosed-paas-platform-antspace-built-in-baku-self-hosted-full-stack-ecosystem-already-taking-shape-386582), [Source 4](https://github.com/AprilNEA/reverse-engineering-claude-code-antspace/blob/master/baku-analysis.md). 

쉽게 말해, 파이어크래커는 아주 가볍고 빠른 '가상 컴퓨터'입니다. 일반적인 가상 머신이 거대한 공장이라면, 이 마이크로VM은 필요한 기능만 딱 챙겨서 순식간에 나타나는 '조립식 주방' 같은 것이죠[Source 11](https://www.romanpeschke.com/guides/claude-code-scheduled-tasks/). 이 안에서 4개의 뇌(vCPU)와 16GB의 메모리를 활용해 Claude가 직접 앱을 짓고, 배포까지 일사천리로 처리하는 것입니다[Source 2](https://www.weex.com/news/detail/reverse-engineering-claude-code-reveals-anthropicas-undisclosed-paas-platform-antspace-built-in-baku-self-hosted-full-stack-ecosystem-already-taking-shape-386582).

상상해보세요. 여러분이 캠핑을 가서 텐트를 직접 치지 않고, AI에게 "예쁜 텐트 쳐줘"라고 말하자마자 마법처럼 텐트가 설치되는 것과 비슷합니다. Antspace가 바로 여러분의 웹 사이트를 위한 '자동 텐트 설치 서비스'인 셈이죠.

### 현재 상황: 수면 위로 드러난 비밀

전문가들의 역공학(Reverse-Engineering) 분석에 따르면, 이 시스템은 단순히 기존의 외부 서비스를 빌려 쓰는 방식이 아니었습니다. Anthropic은 Vercel 같은 기존 서비스의 API를 단순히 연결하는 수준을 넘어, **기초부터 직접 배포 프로토콜을 구축**했습니다[Source 1](https://aprilnea.me/en/blog/reverse-engineering-claude-code-antspace), [Source 3](https://github.com/AprilNEA/reverse-engineering-claude-code-antspace). 

현재 Anthropic은 Claude Code를 통해 사용자들이 무엇을, 어떻게 만드는지에 대한 방대한 데이터를 수집하고 있습니다. 이 데이터를 바탕으로 Antspace를 최적화한다면, 개발자가 일일이 서버 설정을 조정하지 않아도 AI가 알아서 가장 효율적인 환경에 앱을 띄워주는 시대가 올 것입니다[Source 5](https://x.com/mayazi/status/2034282767693873492).

### 앞으로 어떻게 될까?

Anthropic의 전략은 명확해 보입니다. 사용자가 Claude에 머무는 시간을 늘리고, 단순히 '대화'하는 상대를 넘어 '생산'의 중심지로 만드는 것입니다. 앞으로는 개발자가 "이 앱 배포해줘"라고 말 한마디만 하면, Antspace가 뒤에서 보이지 않게 서버를 구축하고 도메인을 연결해 줄 것입니다. 

사용자 입장에서는 편리함이 극대화되겠지만, 한편으로는 특정 AI 생태계에 의존하게 되는 측면도 있습니다. Anthropic이 구축하려는 이 수직 통합 생태계는 앞으로 다른 AI 모델들에게도 강력한 기준점이 될 것입니다[Source 5](https://x.com/mayazi/status/2034282767693873492), [Source 14](https://www.linkedin.com/posts/laserfocus_breaking-if-you-reverse-engineered-the-activity-7440048762829443072-of-K).

### MindTickleBytes의 AI 기자 시선

AI가 코드를 생성하는 수준을 넘어 '배포'라는 현실적인 인프라까지 직접 통제하기 시작했다는 것은, AI가 단순히 가상세계의 텍스트 생성기가 아니라 물리적 서비스(웹 사이트)를 운영하는 주체로 올라섰음을 의미합니다. 개발자의 정의가 '코드를 직접 쓰는 사람'에서 'AI의 배포 방향을 결정하는 감독자'로 바뀌고 있는지도 모릅니다. 이제 우리는 무엇을 만드는지를 넘어, 어떤 AI에게 배포를 맡길지를 고민해야 할 때가 올 것입니다.

## 참고자료

1. [Anthropic's Hidden Vercel Competitor "Antspace" | AprilNEA](https://aprilnea.me/en/blog/reverse-engineering-claude-code-antspace)
2. [Reverse-engineering Claude Code reveals Anthropica's undisclosed PaaS platform "Antspace": Built in Baku, self-hosted, full-stack ecosystem already taking shape | WEEX Crypto News](https://www.weex.com/news/detail/reverse-engineering-claude-code-reveals-anthropicas-undisclosed-paas-platform-antspace-built-in-baku-self-hosted-full-stack-ecosystem-already-taking-shape-386582)
3. [GitHub - AprilNEA/reverse-engineering-claude-code-antspace: Anthropic's Hidden Vercel Competitor "Antspace" · GitHub](https://github.com/AprilNEA/reverse-engineering-claude-code-antspace)
4. [reverse-engineering-claude-code-antspace/baku-analysis.md at master · AprilNEA/reverse-engineering-claude-code-antspace](https://github.com/AprilNEA/reverse-engineering-claude-code-antspace/blob/master/baku-analysis.md)
5. [Maya Zehavi on X: "Anthropic is making the obvious play to build out a platform & own the entire stack from deployment, cloud & orchestration. But more importantly, Anthropic is gathering the user data about ppl are building with Claude so that they can offer a more optimized end to end platform." / X](https://x.com/mayazi/status/2034282767693873492)
6. [AprilNEA on X: "🧵 I just reverse-engineered the binaries inside Claude Code's Firecracker MicroVM and found something wild: Anthropic is building their own PaaS platform called "Antspace" (Ants + Space). It's a full deployment pipeline — hidden in plain sight inside the environment-runner https://t.co/QbPT9ILECG" / X](https://x.com/AprilNEA/status/2034209430158619084)
11. [ClaudeCode Scheduled Tasks and Project Antspace | Roman Peschke](https://www.romanpeschke.com/guides/claude-code-scheduled-tasks/)
14. [BREAKING: If you reverse-engineered the binaries inside Claude...](https://www.linkedin.com/posts/laserfocus_breaking-if-you-reverse-engineered-the-activity-7440048762829443072-of-K)