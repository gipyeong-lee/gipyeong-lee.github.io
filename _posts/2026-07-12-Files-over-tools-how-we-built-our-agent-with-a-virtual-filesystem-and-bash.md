---
layout: post
title: "AI에게 '도구' 대신 '컴퓨터'를 줬더니 벌어진 일"
description: "AI 에이전트가 복잡한 전용 도구 없이 파일 시스템과 배시(bash) 명령어를 사용하여 스스로 업무를 처리하는 새로운 방식에 대해 설명합니다."
summary: "AI 에이전트에게 매번 새로운 전용 도구를 만들어주는 대신, 가상 파일 시스템과 배시 명령어를 제공하여 스스로 데이터를 다루게 하는 'Files over tools' 설계 방식이 주목받고 있습니다."
tags: [AI, 에이전트, 개발, 기술트렌드]
image: 2026-07-12-Files-over-tools-how-we-built-our-agent-with-a-virtual-filesystem-and-bash.jpg
image_alt: "AI가 가상 파일 시스템 환경에서 코드를 작성하고 파일을 탐색하는 모습을 형상화한 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "복잡한 도구들을 만드는 것보다 AI가 이미 익숙한 컴퓨팅 환경(파일과 명령어)에서 생각하게 만드는 것이 훨씬 확장성 있고 유연한 방법입니다."
quiz:
  - question: "최근 AI 에이전트 설계에서 도구(Tool) 중심 방식보다 선호되는 새로운 방식은 무엇인가요?"
    choices: ["웹 브라우저 자동화 방식", "가상 파일 시스템과 배시(bash) 환경 방식", "사용자 직접 입력 방식"]
    answer: 1
    explanation: "최근에는 AI에게 수많은 전용 도구를 제공하는 대신, 파일 시스템과 배시 명령어를 사용하여 스스로 데이터를 탐색하고 조작하게 하는 방식이 효율성을 인정받고 있습니다."
  - question: "가상 파일 시스템을 사용하는 에이전트의 주요 장점은 무엇인가요?"
    choices: ["모든 파일을 실제 하드디스크에 저장할 수 있다.", "매번 새로운 도구를 개발하지 않아도 다양한 작업을 처리할 수 있다.", "인터넷 연결이 항상 필요하다."]
    answer: 1
    explanation: "배시 접근 권한을 가진 에이전트는 파일 탐색, 텍스트 처리 등 다양한 작업을 전용 도구 개발 없이 유연하게 수행할 수 있습니다."
  - question: "가상 파일 시스템의 데이터는 실제로 어디에 저장될 수 있나요?"
    choices: ["반드시 클라우드 서버에만 저장된다.", "실제 디스크 파일 대신 SQLite 같은 데이터베이스에 백업될 수 있다.", "매번 실행할 때마다 사라진다."]
    answer: 1
    explanation: "일부 가상 파일 시스템은 실제 파일 형태가 아니라 SQLite와 같은 데이터베이스를 백업 저장소로 활용하여 효율적으로 운영됩니다."
lang: ko
ref: 2026-07-12-Files-over-tools-how-we-built-our-agent-with-a-virtual-filesystem-and-bash
audio: 2026-07-12-Files-over-tools-how-we-built-our-agent-with-a-virtual-filesystem-and-bash.mp3
permalink: /2026/07/12/Files-over-tools-how-we-built-our-agent-with-a-virtual-filesystem-and-bash/
---

상상해보세요. 여러분이 요리사에게 "맛있는 김치찌개를 만들어줘"라고 주문했습니다. 그런데 이 요리사가 김치찌개는 만들 줄 알지만, 양파를 썰 때마다 '양파 썰기용 전용 칼'을 새로 만들어야 하고, 국자를 쓸 때마다 '국자 만드는 기계'를 새로 돌려야 한다면 어떨까요? 아마 여러분은 요리가 나오기도 전에 지쳐버릴 것입니다. 요리 시간보다 도구 준비 시간이 더 걸리기 때문이죠.

놀랍게도, 그동안 우리가 AI 에이전트(AI Agent, 스스로 목표를 설정하고 복잡한 업무를 수행하는 인공지능)를 만들 때 딱 이런 비효율적인 방식을 사용하고 있었습니다. AI가 수행할 수 있는 작업마다 일일이 '전용 도구(Tool)'를 만들어 붙여줬던 것입니다. 하지만 최근 개발자들 사이에서는 "도구를 새로 만들지 말고, AI에게 그냥 컴퓨터 환경 자체를 줘버리자"는 새로운 흐름이 나타나고 있습니다. 이를 '파일 우선(Files over tools)' 설계라고 부릅니다.

## 왜 이 방식이 중요한가요?

지금까지 AI 에이전트는 기능 하나를 추가할 때마다 개발자가 복잡한 소프트웨어 도구를 설계하고 AI와 연결해야 했습니다. 이는 시간과 비용이 많이 들 뿐만 아니라, AI의 유연성을 떨어뜨리는 주된 원인이었습니다. 정해진 도구 밖의 상황이 발생하면 AI는 손을 쓰지 못했기 때문입니다.

하지만 AI에게 가상 파일 시스템(Virtual Filesystem)과 배시(bash, 리눅스 시스템에서 사용하는 명령어 기반의 작업 환경) 접근 권한을 주면 상황이 완전히 바뀝니다. 에이전트가 마치 인간 개발자가 컴퓨터 앞에서 작업하듯 스스로 파일을 찾고, 내용을 읽고, 수정하며, 명령어를 조합해 문제를 해결할 수 있게 됩니다. 이는 AI 에이전트의 생산성을 비약적으로 높여줄 뿐만 아니라, 개발자가 모든 상황을 가정하고 도구를 만들지 않아도 AI가 스스로 유연하게 새로운 환경에 대처할 수 있게 만듭니다.

## 쉽게 비유하자면

쉽게 말해서, 기존의 방식이 AI에게 '단추 하나만 누르면 특정 동작을 하는 전용 기계들'을 수백 개 쥐여준 것이라면, 새로운 방식은 AI에게 '운영체제가 설치된 컴퓨터 한 대'를 빌려준 것과 같습니다.

예를 들어, 에이전트가 고객사 정보를 관리해야 한다고 가정해봅시다. 과거에는 '고객정보조회 도구', '고객정보수정 도구'를 일일이 개발해야 했습니다. 하지만 이제는 에이전트에게 고객 데이터가 담긴 가상 폴더를 보여주고, 배시 명령어(예: `grep` 명령어로 데이터를 찾고, `echo` 명령어로 내용을 수정하는 방식)를 쓰게 합니다. [출처 2](https://www.linkedin.com/posts/knocklabs_how-do-you-build-an-ai-agent-that-safely-activity-7481434587642957843-qCEi) 이렇게 하면 AI는 마치 컴퓨터를 사용하는 사용자처럼 파일들을 탐색하며 스스로 맥락을 파악하고 업무를 완수합니다. [출처 14](https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools)

또한, 이 파일 시스템은 물리적인 하드디스크를 차지하지 않고도 동작할 수 있습니다. 일부 가상 파일 시스템은 SQLite(가볍고 빠른 데이터베이스 프로그램)를 활용해 데이터를 안전하게 저장하고 관리합니다. [출처 19](https://github.com/maxi-moss/agent-filesystem) 우리 눈에는 컴퓨터에서 폴더를 탐색하는 것처럼 보이지만, 실제로는 데이터베이스 안에서 훨씬 효율적으로 정보를 다루는 것이죠.

## 현재 기술은 어디까지 왔을까요?

이미 많은 기업과 프로젝트가 이 방식을 도입하고 있습니다. 'Knock'이라는 회사는 자사의 AI 에이전트 아키텍처에 배시 환경과 가상 파일 시스템, 그리고 관리용 API를 결합하여 고객 메시징 자원을 처리하고 있습니다. [출처 1](https://knock.app/blog/how-we-built-the-knock-agent-virtual-filesystem-and-bash) [출처 3](https://fooqux.com/article/6457)

또한 'AgentFS'와 같은 프로젝트는 AI 에이전트만을 위한 전용 파일 시스템을 제공합니다. 이는 AI가 안전하게 명령줄 도구(CLI Tool)를 사용하면서도 모든 작업 내역을 감사(Audit)할 수 있게 도와줍니다. [출처 15](https://github.com/tursodatabase/agentfs) [출처 16](https://www.agentfs.ai/) 단순히 도구를 줄이는 것뿐만 아니라, AI가 무엇을 했는지 기록을 남겨 안전성을 확보하는 것이 현재 기술의 핵심입니다.

## 미래에는 어떤 모습일까요?

AI 에이전트의 발전 방향은 점점 '사람과 비슷해지는 방향'으로 가고 있습니다. 개발자가 매번 새로운 도구를 설계해주는 시대는 저물고, AI가 스스로 컴퓨터 환경을 이용해 숙련된 조수처럼 일하는 시대가 올 것입니다.

앞으로는 에이전트가 처리해야 할 데이터가 파일 형태로 체계적으로 정리되어 있고, 에이전트는 이를 리눅스 명령어를 사용해 능수능란하게 다루게 될 것입니다. 여러분이 해야 할 일은 도구를 만드는 것이 아니라, AI가 일할 수 있는 잘 정리된 '디지털 환경'을 구축하는 것이 될 가능성이 높습니다. 이제는 도구가 아니라 '환경'을 빌려줄 때입니다.

## MindTickleBytes의 AI 기자 시선
도구의 시대에서 환경의 시대로 전환된다는 점은 AI 기술이 단순한 계산기를 넘어 진정한 '디지털 작업자'로 진화하고 있음을 의미합니다. 개발자의 손길을 최소화하고 AI의 자율성을 최대화하는 이런 설계가 미래의 에이전트 생태계를 결정지을 것입니다.

## 참고자료

1. [Files over tools: how we built the Knock Agent using a virtual filesystem and bash](https://knock.app/blog/how-we-built-the-knock-agent-virtual-filesystem-and-bash)
2. [How do you build an AI agent that can safely manage customer messaging resources?](https://www.linkedin.com/posts/knocklabs_how-do-you-build-an-ai-agent-that-safely-activity-7481434587642957843-qCEi)
3. [Files over tools: how we built the Knock Agent using a virtual filesystem and bash](https://fooqux.com/article/6457)
4. [Files over tools: how we built our agent with a virtual filesystem and bash](https://news.ycombinator.com/item?id=48845364)
5. [How to build agents with filesystems and bash - Vercel](https://vercel.com/blog/how-to-build-agents-with-filesystems-and-bash)
6. [Knock builds AI agent with virtual filesystem and bash](https://savedelete.com/news/knock-agent-virtual-filesystem/)
7. [Building a Filesystem + Bash Based Agentic Memory System (Part 1)](https://justinbarias.io/blog/agentic-memory-filesystem-part-1/)
14. [We removed 80% of our agent’s tools - Vercel](https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools)
15. [GitHub - tursodatabase/agentfs: The filesystem for agents.](https://github.com/tursodatabase/agentfs)
16. [AgentFS - Filesystem Isolation for AI Agents](https://www.agentfs.ai/)
18. [Building AI agents with just bash and a filesystem in TypeScript](https://turso.tech/blog/agentfs-just-bash)
19. [GitHub - maxi-moss/agent-filesystem: A virtual filesystem for agents.](https://github.com/maxi-moss/agent-filesystem)