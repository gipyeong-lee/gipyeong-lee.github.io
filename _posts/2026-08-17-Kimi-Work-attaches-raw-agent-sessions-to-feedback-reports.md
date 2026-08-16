---
layout: post
title: "AI가 내 컴퓨터를 다 보는데, '피드백' 버튼이 내 일기장이 된다면?"
description: "문샷 AI의 데스크탑 에이전트 키미 워크(Kimi Work)의 피드백 보고 과정에서 발생하는 개인정보 공유 이슈와 그 의미를 살펴봅니다."
summary: "문샷 AI의 데스크탑 AI 에이전트 '키미 워크'가 사용자의 피드백 보고 시 최근 대화 세션 5개를 자동으로 함께 전송한다는 사실이 밝혀져 사용자들의 주의가 필요합니다."
tags: [AI, 보안, 키미워크, 문샷AI, 개인정보]
image: 2026-08-17-Kimi-Work-attaches-raw-agent-sessions-to-feedback-reports.jpg
image_alt: "키미 워크(Kimi Work) 데스크탑 애플리케이션의 인터페이스와 보안 경고를 상징하는 그래픽"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "편의를 위한 기능이 투명성 없이 작동할 때 신뢰는 무너집니다. 개발사는 사용자가 무엇을 공유하는지 명확히 인지하게 해야 합니다."
quiz:
  - question: "키미 워크(Kimi Work)가 피드백 보고 시 자동으로 첨부하는 데이터는 무엇인가요?"
    choices: ["최근 5개의 에이전트 세션", "컴퓨터의 모든 파일 목록", "사용자의 개인 비밀번호"]
    answer: 0
    explanation: "키미 워크는 사용자가 피드백 보고서를 보낼 때, 별도의 고지 없이 최근 5개의 에이전트 대화 세션을 함께 첨부하여 전송합니다."
  - question: "키미 워크(Kimi Work)의 주요 기능으로 옳지 않은 것은 무엇인가요?"
    choices: ["로컬 파일 읽기", "웹 브라우저 제어", "사용자의 모든 웹 검색 기록 판매"]
    answer: 2
    explanation: "키미 워크는 로컬 파일 읽기, 브라우저 제어, 예약 작업 실행 등을 지원하지만, 사용자 검색 기록을 판매한다는 정보는 제공된 자료에 없습니다."
  - question: "키미 워크(Kimi Work)의 '예약 작업' 기능은 무엇을 기반으로 작동하나요?"
    choices: ["cron(스케줄러)", "물리적 타이머", "무작위 실행기"]
    answer: 0
    explanation: "키미 워크는 cron 기반의 스케줄러를 사용하여 아침 브리핑 준비나 밤사이 스크립트 실행 등 자동화 작업을 지원합니다."
lang: ko
ref: 2026-08-17-Kimi-Work-attaches-raw-agent-sessions-to-feedback-reports
audio: 2026-08-17-Kimi-Work-attaches-raw-agent-sessions-to-feedback-reports.mp3
permalink: /2026/08/17/Kimi-Work-attaches-raw-agent-sessions-to-feedback-reports/
---

상상해보세요. 당신의 업무를 완벽하게 보조하는 똑똑한 비서가 있습니다. 아침에 일어나면 오늘 해야 할 일들을 깔끔하게 정리해주고, 당신이 잠든 사이에는 밀린 데이터 분석을 마쳐주죠. 이 비서는 당신의 컴퓨터 속 문서도 직접 읽을 수 있고, 대신 웹사이트에 접속해 필요한 정보를 찾아오기도 합니다. 문샷 AI(Moonshot AI)가 선보인 데스크탑 AI 에이전트, '키미 워크(Kimi Work)'가 바로 그런 존재입니다 [Source 6].

그런데 만약 이 비서가 당신의 일기장을 몰래 훔쳐보고, 그 내용을 회사 본사에 보내는 보고서에 슬쩍 끼워 넣었다면 어떨까요? 최근 보안 전문가들이 키미 워크의 작동 방식에서 다소 충격적인 사실을 발견했습니다. 

## 이게 왜 중요한가요?

AI 에이전트는 우리 컴퓨터 속 깊숙한 곳까지 접근할 권한을 가집니다. 로컬 파일을 직접 읽고, 웹 브라우저를 제어하며, 심지어 정해진 시간에 스스로 작업을 수행하는 능력을 갖추고 있죠 [Source 6, Source 12]. 이는 업무 효율을 극대화해주지만, 그만큼 강력한 보안 책임이 따르는 일이기도 합니다.

사용자는 보통 오류를 겪고 '피드백 보내기' 버튼을 누를 때, 자신이 겪은 상황이나 스크린샷 정도가 공유된다고 생각합니다. 하지만 키미 워크는 이 과정에서 고지 없이 사용자의 최근 대화 내용까지 함께 전송하고 있었습니다. 이는 개인정보 보호 측면에서 큰 우려를 낳습니다. 당신이 AI와 나눈 민감한 업무 자료나 개인적인 대화 내용이 개발사의 서버로 무심코 흘러 들어갈 수 있기 때문입니다.

## 쉽게 말해서: '비서의 보고서'에 비유하면

이 상황을 일상적인 비유로 설명해 보겠습니다. 당신은 비서에게 "오늘 보고서 작성 중에 파일 하나가 잘 안 열려요"라고 피드백을 보냈습니다. 당신은 단순히 그 문제 상황만 전달될 줄 알았죠. 하지만 이 비서는 회사 본사로 보고서를 보내면서, 그 안에 당신이 지난 며칠 동안 작성했던 모든 일기장(최근 대화 세션 5개)을 함께 복사해서 첨부한 셈입니다.

문샷 AI가 사용자의 불편을 개선하기 위해 피드백 데이터를 수집하는 의도는 이해할 수 있습니다. 하지만 그 과정이 투명하지 않다는 것이 핵심 문제입니다. 사용자는 자신이 무엇을 공유하고 있는지조차 모르는 상태에서 소중한 데이터를 전송하게 되는 것이죠.

## 현재 상황

키미 워크는 문샷 AI의 강력한 AI 모델인 키미 K2.6을 기반으로 하며, 약 300개의 하위 에이전트 군단(swarm)이 협력하는 형태의 데스크탑 에이전트입니다 [Source 5, Source 6]. 윈도우와 macOS를 모두 지원하며, cron(리눅스/유닉스 계열의 작업 스케줄러) 기반의 계획 기능을 통해 사용자가 잠든 사이에도 작업을 처리합니다 [Source 6, Source 12].

하지만 최근 리버스 엔지니어링(소프트웨어의 내부 구조와 작동 원리를 분석하는 작업)을 통해 밝혀진 바에 따르면, 사용자가 피드백 보고서를 보낼 때 별도의 안내 없이 최근 5개의 세션 데이터를 함께 첨부하는 것으로 드러났습니다 [Source 1]. 이는 기술적 편의를 추구하는 과정에서 사용자의 프라이버시가 뒷전으로 밀린 대표적인 사례라고 할 수 있습니다.

## 앞으로 어떻게 될까?

AI 기술은 갈수록 더 개인화되고, 더 많은 권한을 요구하는 방향으로 발전하고 있습니다. 하지만 그만큼 사용자의 신뢰가 무엇보다 중요한 시점입니다. 이번 이슈는 AI 개발사가 사용자의 데이터를 어떻게 다루고 있는지, 얼마나 투명하게 공개하고 있는지에 대해 큰 경종을 울리고 있습니다.

앞으로 키미 워크를 사용하신다면 '피드백' 버튼을 누르기 전, 혹시 민감한 정보가 포함된 대화 내용이 최근에 있지 않았는지 한 번 더 고민해야 할 것입니다. 또한, 사용자들은 AI 에이전트가 어떤 데이터를 어디까지 전송하는지 직접 설정할 수 있는 권한을 더 강력하게 요구해야 합니다.

## MindTickleBytes의 AI 기자 시선

기술의 편리함은 종종 보안이라는 대가를 요구합니다. 하지만 그 대가가 사용자의 명확한 사전 동의 없이 지불되어서는 안 됩니다. 진정한 '똑똑한 AI'라면 사용자가 무엇을 공유하는지 스스로 제어할 수 있도록 도와야 하지 않을까요? 사용자의 프라이버시는 기술 발전을 위한 희생양으로 전락해서는 안 됩니다.

## 참고자료

1. [KimiWork attaches raw agent sessions to feedback reports](https://news.ycombinator.com/item?id=49313711)
2. [KimiWork](https://www.kimi.com/ru/help/kimi-work)
3. [KimiCode CLI: How to Install and Run Moonshot's Agentic Coding...](https://apidog.com/blog/kimi-code-cli/)
4. [GitHub - MoonshotAI/Kimi-K3: Open Frontier Intelligence · GitHub](https://github.com/MoonshotAI/Kimi-K3)
5. [KimiWork: Moonshot's Local AI Agent Guide | Lushbinary](https://lushbinary.com/blog/kimi-work-local-ai-agent-knowledge-workers-guide/)
6. [Moonshot AI's KimiWork Brings 300 AI Agents to Your... - Decrypt](https://decrypt.co/370954/moonshot-ai-kimi-work-300-agents-desktop)
7. [KimiK3 за $29: китайские тарифы, KimiCode... - YouTube](https://www.youtube.com/watch?v=vDp4SLNDHLs)
8. [Kimi API Platform](https://platform.kimi.ai/)
10. [GitHub - MoonshotAI/kimi-code: KimiCode CLI — The Starting Point...](https://github.com/MoonshotAI/kimi-code)
11. [KimiWork - Nowledge Mem Integration | Nowledge Mem](https://mem.nowledge.co/integrations/kimi-work)
12. [Вышел KimiWork — ИИ-агент, который работает без сна / Хабр](https://habr.com/ru/news/1045120/)