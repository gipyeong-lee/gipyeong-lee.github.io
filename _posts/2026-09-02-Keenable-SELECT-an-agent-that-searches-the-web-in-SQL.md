---
layout: post
title: "AI가 인터넷을 'SQL'로 검색한다고요? Keenable SELECT 이야기"
description: "AI 에이전트가 복잡한 웹 데이터를 SQL 쿼리 하나로 깔끔하게 정리하는 새로운 검색 방식 Keenable SELECT를 소개합니다."
summary: "AI 에이전트가 기존 검색 API의 복잡한 데이터를 처리하는 방식을 넘어, SQL 언어를 사용해 원하는 정보만 정확하게 추출하는 Keenable SELECT 기술을 알아봅니다."
tags: [AI, 검색엔진, SQL, 에이전트, 기술]
image: 2026-09-02-Keenable-SELECT-an-agent-that-searches-the-web-in-SQL.jpg
image_alt: "데이터베이스 쿼리 언어인 SQL 코드가 웹 검색 데이터와 연결되는 모습을 형상화한 그래픽"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "사람을 위한 검색과 AI를 위한 검색은 근본적으로 달라야 합니다. Keenable의 SQL 인터페이스는 에이전트들이 웹과 소통하는 방식을 한 단계 진화시킬 것입니다."
quiz:
  - question: "Keenable SELECT의 가장 큰 특징은 무엇인가요?"
    choices: ["인간용 검색 엔진 인터페이스 제공", "SQL을 사용하여 웹 데이터를 읽기 전용으로 조회", "전 세계 모든 웹사이트의 실시간 렌더링"]
    answer: 1
    explanation: "Keenable SELECT는 모델 컨텍스트 프로토콜(MCP) 서버를 통해 에이전트가 읽기 전용 DuckDB SELECT 문을 사용하여 웹 데이터를 검색하도록 설계되었습니다."
  - question: "Keenable이 보유한 웹 검색 인덱스의 규모는 어느 정도인가요?"
    choices: ["약 10억 개 문서", "약 500억 개 문서", "1,000억 개 이상의 문서"]
    answer: 2
    explanation: "Keenable은 독자적인 크롤러와 인덱스 시스템을 통해 1,000억 개 이상의 문서를 보유하고 있습니다."
  - question: "Keenable API가 제공하는 특별한 검색 기능은 무엇인가요?"
    choices: ["과거 특정 시점의 인터넷 상태를 조회하는 기능", "개인 정보 암호화 자동 생성", "무제한 무료 사용"]
    answer: 0
    explanation: "Keenable은 모델이 현재 상태뿐만 아니라 과거 특정 시점의 인터넷을 검색할 수 있도록 하는 '시점(point-in-time) 기록 쿼리'를 지원합니다."
lang: ko
ref: 2026-09-02-Keenable-SELECT-an-agent-that-searches-the-web-in-SQL
audio: 2026-09-02-Keenable-SELECT-an-agent-that-searches-the-web-in-SQL.mp3
permalink: /2026/09/02/Keenable-SELECT-an-agent-that-searches-the-web-in-SQL/
---

상상해보세요. 여러분이 비서에게 "어제 뉴스에서 나온 그 기업 주가랑 관련 기사 다 정리해와"라고 말했습니다. 그런데 비서가 돌아와서는 수만 페이지 분량의 복잡하고 지저분한 종이 뭉치를 던져주며, "여기서 직접 찾아보세요"라고 말한다면 어떨까요? 아마 화가 날 것입니다. 

지금까지의 AI 에이전트들이 인터넷을 검색할 때 겪던 상황이 딱 이랬습니다. 대부분의 검색 API는 사람이 읽기 좋게 만들어졌거나, 혹은 AI가 다시 한번 정제해야 하는 지저분한 데이터(JSON이나 HTML 덩어리)를 쏟아냈기 때문입니다. 하지만 최근 이런 비효율을 해결하기 위해 등장한 기술이 있습니다. 바로 **Keenable SELECT**입니다.

## 왜 중요한가요?

지금까지 AI 에이전트(AI Agent, 스스로 판단하고 복잡한 작업을 수행하는 인공지능)는 웹 정보를 얻기 위해 검색 API를 사용해 왔습니다. 하지만 기존의 검색 API들은 주로 인간 사용자를 위해 설계되었기 때문에 에이전트가 복잡한 작업을 수행할 때마다 데이터를 일일이 청소해야 하는 '추가 작업'이 필요했습니다 [Source 13, Source 16]. 

Keenable SELECT는 이 과정을 건너뛰게 해줍니다. 우리가 흔히 데이터베이스를 다룰 때 쓰는 **SQL(Structured Query Language, 데이터를 조회하고 관리하기 위한 표준 언어)** 문법을 웹 검색에 그대로 도입했기 때문입니다. 덕분에 개발자들은 에이전트에게 필요한 데이터만 '딱 집어서' 가져오라고 명령할 수 있게 되었습니다. 에이전트가 불필요한 정보 해석에 시간을 낭비하지 않고, 복잡한 업무를 더 빠르고 정확하게 처리할 수 있게 된 것입니다.

## 쉽게 이해하기: 도서관 사서의 비유

Keenable SELECT를 쉽게 이해하기 위해 '도서관 사서' 비유를 들어보겠습니다.

기존의 검색 엔진이 도서관 사서에게 "요리책 다 찾아줘"라고 말하면, 사서가 수천 권의 요리책을 책상 위에 몽땅 쌓아놓고 "여기서 필요한 걸 찾아보세요"라고 말하는 방식이라면, Keenable SELECT는 다릅니다. 이 기술은 마치 사서에게 **"2025년 이후에 출판된, 15분 이내로 만들 수 있는 한식 요리법만 골라서 리스트로 만들어줘"**라고 상세한 조건을 붙여 주문하는 것과 같습니다. 

기술적으로는 **모델 컨텍스트 프로토콜(MCP, AI 에이전트를 위한 표준 통신 규칙)** 서버 내에서 'select'라는 도구를 실행합니다 [Source 12]. 에이전트가 "SELECT * FROM web WHERE..."와 같은 SQL 문을 입력하면, Keenable의 독자적인 시스템이 웹 데이터를 읽어와 깔끔한 행(row) 형태로 정리해 에이전트에게 전달합니다 [Source 12]. 에이전트 입장에선 굳이 복잡한 웹 페이지 구조를 해석하느라 힘을 뺄 필요가 없어지는 셈입니다.

## 현재 상황

Keenable은 단순한 도구가 아니라, AI 에이전트만을 위해 설계된 독자적인 인프라입니다 [Source 8, Source 15]. 그 규모도 상당합니다.

- **방대한 지식:** Keenable은 독자적인 크롤러와 인덱스 시스템을 구축하여 1,000억 개 이상의 문서를 데이터베이스화했습니다 [Source 5, Source 6, Source 8]. 
- **빠른 속도:** AI 에이전트들이 실시간으로 업무를 처리할 수 있도록, 미국 동부(us-east) 지역 기준으로 95%의 요청이 250밀리초(0.25초) 이내에 처리되도록 최적화되어 있습니다 [Source 5].
- **역사적 데이터 지원:** 특히 흥미로운 점은 '시점 기록 쿼리'입니다 [Source 9]. 이는 에이전트가 현재의 인터넷 정보뿐만 아니라, 과거 특정 날짜에 인터넷에 존재했던 정보만을 조회할 수 있게 해줍니다 [Source 9]. 

이 서비스는 최근 2,600만 달러(한화 약 300억 원 이상)의 투자 유치에 성공하며 기술력을 인정받았습니다 [Source 4, Source 6, Source 9, Source 16]. 이미 여러 AI 연구소와 데이터 제공 업체들이 훈련 및 실제 서비스 운영 과정에서 이 API를 사용하고 있습니다 [Source 6].

## 앞으로 어떻게 될까?

Keenable SELECT의 등장은 '에이전트 시대'의 검색이 어디로 향하고 있는지 보여줍니다. 앞으로는 AI가 단순히 "검색해줘"라고 명령하는 것을 넘어, 데이터베이스를 다루듯 정교한 질의를 웹에 던지는 것이 표준이 될 것으로 보입니다. 사용자가 "지난달 대비 상승한 친환경 기업 주가를 표로 만들어줘"라고 했을 때, AI 에이전트가 단 몇 줄의 SQL 문만으로 웹에서 즉시 데이터를 뽑아내 답변하는 시대가 코앞으로 다가온 것입니다.

## MindTickleBytes의 AI 기자 시선

사람을 위한 검색과 AI를 위한 검색은 근본적으로 달라야 합니다. Keenable의 SQL 인터페이스는 에이전트들이 웹과 소통하는 방식을 한 단계 진화시킬 것입니다. 이제 AI는 웹을 '읽는' 존재를 넘어, 웹을 '쿼리하는' 존재가 되고 있습니다.

## 참고자료

1. [Web Search & Extract | Hermes Agent - NOUS RESEARCH](https://hermes-agent.nousresearch.com/docs/user-guide/features/web-search)
2. [SQL Agent | Use Natural Language to Query Databases](https://www.snaplogic.com/ai-agent-showcase/sql-queries)
3. [Examples of Using Select AI Agent](https://docs.oracle.com/en-us/iaas/autonomous-database-serverless/doc/examples-using-select-ai-agent.html)
4. [What is Keenable: The 'AI Agent-Only' Search API Built by Former Yandex Search Leaders, and the Details of Their $26 Million Funding｜アイドリ | AI-Driven Lab](https://note.com/ai_driven/n/n1639bb95690d?hl=en)
5. [Show HN: Keenable – A different web search API for AI agents | Hacker News](https://news.ycombinator.com/item?id=49435555)
6. [Accel-backed Keenable is indexing the web for AI agents | TechCrunch](https://techcrunch.com/2026/08/25/accel-backed-keenable-is-indexing-the-web-for-ai-agents/)
7. [How to Build an AI Agent That Searches the Web: Tools & Setup](https://syllable.ai/blog/how-to-build-ai-agent-with-search-tools)
8. [Keenable.ai — Independent Web Search API for AI](https://keenable.ai/)
9. [Agentic web search infrastructure startup Keenable raises $26M - SiliconANGLE](https://siliconangle.com/2026/08/25/agentic-web-search-infrastructure-startup-keenable-raises-26m/)
10. [hermes-agent/website/docs/user-guide/features/web-search.md at main · NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/web-search.md)
11. [Quickstart - Keenable](https://docs.keenable.ai/)
12. [KeenableSELECT: an agent that searches the web in SQL](https://keenableai.github.io/select-showcase/)
13. [[IndustryNews] Keenable is trying to fix how AI agents actua...](https://promptcube3.com/en/news/7679/)
14. [Keenable: Agent-First Search API Architecture and the 100B Page Index Trade-Off - DEV Community](https://dev.to/mech_app_ai/keenable-agent-first-search-api-architecture-and-the-100b-page-index-trade-off-259b)
15. [Keenable exits stealth mode with $26M seed round to build search...](https://cryptobriefing.com/keenable-26m-seed-ai-search-index/)