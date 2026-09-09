---
layout: post
title: "내 사무실을 똑똑하게! 클로드와 코덱스 에이전트를 내 서버에 직접 설치한다고?"
description: "기업용 운영체제(Company OS)를 직접 내 서버에 설치해서 클로드 코드와 코덱스 같은 AI 에이전트를 부서별로 활용하는 방법을 알아봅니다."
summary: "클로드 코드(Claude Code)와 코덱스(Codex) 에이전트를 기반으로 부서별 AI 업무를 보안 걱정 없이 내 서버에서 직접 구동하는 '셀프 호스팅 기업용 운영체제(Company OS)'가 등장했습니다."
tags: [AI, 셀프호스팅, 기업운영체제, 클로드코드, 코덱스]
image: 2026-09-10-Show-HN-Self-hosted-company-OS-Claude-Code-and-Codex-agents-in-departments.jpg
image_alt: "내 서버에서 작동하는 부서별 AI 에이전트들의 모습을 보여주는 미래 지향적인 그래픽"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "데이터 보안이 중요한 기업 환경에서 AI 에이전트를 자체 서버에 가두어 관리하는 것은 클라우드 AI 도입의 가장 큰 걸림돌을 해결할 중요한 전환점이 될 것입니다."
quiz:
  - question: "이번에 소개된 기업용 운영체제(Company OS)의 주요 특징으로 옳은 것은 무엇인가요?"
    choices: ["클라우드 서버에서만 작동한다", "누구나 무료로 설치하고 스스로 호스팅할 수 있다", "유료 구독 없이는 사용할 수 없다"]
    answer: 1
    explanation: "이 시스템은 오픈 소스로 제공되며, 기업이 직접 내 서버에 설치하고 운영할 수 있는 무료 프로젝트입니다."
  - question: "AI 에이전트의 보안을 유지하기 위해 사용하는 기술적 방법은 무엇인가요?"
    choices: ["비밀번호 강화", "샌드박스 커널과 네트워크 격리 기술 적용", "인터넷 연결 상시 유지"]
    answer: 1
    explanation: "각 에이전트는 샌드박스(bubblewrap) 환경과 네트워크 격리(pasta) 기술을 통해 보안이 보장된 서버 내부에서 안전하게 실행됩니다."
  - question: "AI 에이전트에게 프로젝트의 규칙이나 명령을 전달하는 방식은 무엇인가요?"
    choices: ["전용 앱에만 입력", "프로젝트 폴더 내에 CLAUDE.md나 AGENTS.md 같은 규칙 파일을 생성", "매번 채팅창에 타이핑"]
    answer: 1
    explanation: "클로드 코드는 CLAUDE.md 파일을, 코덱스는 AGENTS.md 파일을 통해 프로젝트 규칙과 명령을 사전에 학습하고 실행합니다."
lang: ko
ref: 2026-09-10-Show-HN-Self-hosted-company-OS-Claude-Code-and-Codex-agents-in-departments
audio: 2026-09-10-Show-HN-Self-hosted-company-OS-Claude-Code-and-Codex-agents-in-departments.mp3
permalink: /2026/09/10/Show-HN-Self-hosted-company-OS-Claude-Code-and-Codex-agents-in-departments/
---

상상해보세요. 아침에 사무실에 출근해서 AI 비서에게 "지난달 판매 데이터 정리해서 부서별 보고서 초안 써줘"라고 말합니다. 그런데 이 AI가 외부 클라우드 서버로 내 자료를 보내지 않고, 우리 회사 지하 전산실에 있는 안전한 서버 안에서만 오직 우리 회사 자료만 학습해서 결과물을 내놓습니다. 정보 유출 걱정은 사라지고, 우리 회사만의 업무 방식은 그대로 유지하면서 말이죠.

최근 해커뉴스(Hacker News) 커뮤니티에서 개발자 디미트리스(Dimitris)가 공개한 **'기업용 운영체제(Company OS, 기업 업무 처리를 돕는 AI 통합 시스템)'** 프로젝트가 큰 관심을 받고 있습니다. [출처 1](https://modernorange.io/item/49630606) 이는 우리가 잘 아는 '클로드 코드(Claude Code, 개발을 돕는 AI 에이전트)'와 같은 강력한 도구들을 우리 회사 서버에 직접 설치해 부서별로 마음껏 쓸 수 있게 만든 환경입니다. [출처 1](https://modernorange.io/item/49630606), [출처 10](https://news.ycombinator.com/item?id=49630606)

## 이게 왜 중요한가요?

그동안 많은 기업이 AI를 도입하고 싶어도 '데이터 보안' 때문에 망설였습니다. 회사의 핵심 기밀이 외부 클라우드 서비스로 전송되는 것을 원치 않기 때문입니다. 하지만 이번에 나온 기업용 운영체제는 **'셀프 호스팅(Self-hosting, 외부 서비스를 빌리지 않고 내 서버에 직접 프로그램을 설치해 운영하는 방식)'**을 택했습니다. [출처 1](https://modernorange.io/item/49630606), [출처 4](https://rankium.io/rankium/press/press-self-hosted-company-os-claude-code-and-codex-agents-in-depa-hackernews)

쉽게 말해, 우리 회사 데이터가 회사 밖으로 나가지 않는 '우리만의 안전한 AI 섬'을 만드는 것입니다. 각 부서별로 자신들만의 AI 에이전트를 가져서 업무 일정을 관리하고, 필요한 도구를 쓰고, 자신들만의 업무 기억을 쌓아갈 수 있게 된 것이죠. [출처 10](https://news.ycombinator.com/item?id=49630606)

## 쉽게 이해하기: '우리 회사 전용 AI 공장'

이 시스템을 비유하자면 **'우리 회사 전용 AI 공장'**과 같습니다.

1. **에이전트(AI 비서)**: 공장에서 일하는 똑똑한 숙련공들입니다. '클로드 코드'나 '코덱스(Codex, 코딩을 돕는 또 다른 AI 모델)'가 이 역할을 수행합니다. [출처 5](https://claude.com/), [출처 10](https://news.ycombinator.com/item?id=49630606)
2. **샌드박스(Sandbox, 격리된 안전 구역)**: 공장 내부의 안전 펜스입니다. '버블랩(bubblewrap)'이라는 기술을 써서, AI 숙련공이 아무리 일을 열심히 해도 공장 밖으로 정보를 흘리지 못하게, 그리고 외부의 해커가 침입하지 못하게 철저히 격리합니다. [출처 10](https://news.ycombinator.com/item?id=49630606)
3. **규칙 파일(CLAUDE.md / AGENTS.md)**: 공장 업무 매뉴얼입니다. '클로드 코드'는 프로젝트 폴더에 `CLAUDE.md`라는 파일을 넣어두면, AI 숙련공이 매일 아침 출근해서 이 매뉴얼을 읽고 일합니다. 코덱스는 똑같은 일을 `AGENTS.md`라는 매뉴얼을 통해 수행합니다. [출처 6](https://theivansergeev.com/guide-gpt-5-6-vs-code/)

즉, AI에게 "우리 회사는 이런 규칙으로 일해"라고 매뉴얼을 던져주면, AI는 회사 서버 안에서 안전하게 그 규칙을 지키며 업무를 처리하는 방식입니다.

## 어디까지 할 수 있나요?

현재 이 시스템은 부서별로 독립적인 작업 공간을 제공합니다. 각 에이전트는 저마다의 업무 기억과 일정을 가지고 독립적으로 움직입니다. [출처 10](https://news.ycombinator.com/item?id=49630606) 특히 보안이 중요한 기업 환경을 위해 네트워크 격리 기술인 '파스타(pasta)'를 사용하여 외부와 불필요한 연결을 완벽히 차단하고 있습니다. [출처 10](https://news.ycombinator.com/item?id=49630606)

현재 '클로드 코드'는 개발자가 코드를 이해하고 편집하는 일을 돕는 도구로 널리 알려져 있으며, 오픈 소스 기반으로 직접 설치해서 사용할 수 있습니다. [출처 5](https://claude.com/), [출처 12](https://claude.com/product/claude-code) 다만, 기업용 운영체제로 제대로 활용하려면 서버 구축에 대한 기초적인 기술 지식이 필요하다는 점은 기억해야 합니다.

## 앞으로 어떻게 될까?

앞으로는 기업들이 복잡한 클라우드 구독 모델 대신, 자신의 서버 사양에 맞는 적절한 모델을 골라 직접 설치하는 형태가 더 늘어날 것으로 보입니다. 이번에 공개된 프로젝트는 누구나 무료로 가져다 쓸 수 있는 오픈 소스이기 때문에, 더 많은 개발자가 기여하며 더 쉽고 강력한 관리 도구로 발전할 가능성이 큽니다. [출처 1](https://modernorange.io/item/49630606) 이제는 우리 회사만의 'AI 비서팀'을 직접 채용하고 관리하는 시대가 가까워지고 있습니다.

## MindTickleBytes의 AI 기자 시선

기술의 발전이 클라우드라는 '공용 공간'에서 기업 내부의 '개인 공간'으로 다시 돌아오고 있습니다. 결국 AI를 얼마나 똑똑하게 쓰느냐만큼, 우리 회사의 소중한 데이터를 얼마나 안전하게 지키며 AI와 협업하느냐가 미래 경쟁력의 핵심이 될 것입니다.

## 참고자료

1. [Show HN: Self-hosted company OS, Claude Code and Codex agents in departments](https://modernorange.io/item/49630606)
2. [VueHN 2.0 | Show HN: Self-hosted company OS, Claude Code and...](https://vue-hackernews-ssr-5cavbdjcta-ew.a.run.app/item/49630606)
3. [Show HN: Self-hosted company OS, Claude Code and Codex agents in departments](https://vk.ru/wall-238001904_5064)
4. [Self-hosted company OS, Claude Code and Codex agents in departments](https://rankium.io/rankium/press/press-self-hosted-company-os-claude-code-and-codex-agents-in-depa-hackernews)
5. [Claude](https://claude.com/)
6. [Codex в VSCode: как подключить GPT-5.6 и настроить ИИ-агента](https://theivansergeev.com/guide-gpt-5-6-vs-code/)
7. [Show HN: Self-hosted company OS, Claude Code... | HackerNews](https://news.ycombinator.com/item?id=49630606)
8. [Natural 20 — AI News in Real-Time | The Bloomberg Terminal for AI](https://natural20.com/c/1bbk9g)
9. [Claude Code by Anthropic | AI Coding Agent, Terminal, IDE](https://claude.com/product/claude-code)