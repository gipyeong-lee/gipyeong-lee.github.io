---
layout: post
title: "AI 用“SQL”搜索互联网？聊聊 Keenable SELECT"
description: "介绍一种全新的搜索方式 Keenable SELECT，让 AI 代理能通过一条 SQL 查询语句精准整理复杂的网络数据。"
summary: "深入了解 Keenable SELECT 技术。它超越了传统搜索 API 处理复杂数据的方式，利用 SQL 语言精准提取所需信息。"
tags: [AI, 搜索引擎, SQL, 代理, 技术]
image: 2026-09-02-Keenable-SELECT-an-agent-that-searches-the-web-in-SQL.jpg
image_alt: "将数据库查询语言 SQL 代码与网络搜索数据连接起来的图形化表示"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "面向人类的搜索与面向 AI 的搜索本质上必须有所不同。Keenable 的 SQL 接口将推动 AI 代理与网络交互方式的进化。"
quiz:
  - question: "Keenable SELECT 最显著的特点是什么？"
    choices: ["提供面向人类的搜索引擎界面", "使用 SQL 以只读方式查询网络数据", "实时渲染全球所有网站"]
    answer: 1
    explanation: "Keenable SELECT 通过模型上下文协议 (MCP) 服务器设计，使 AI 代理能够使用只读的 DuckDB SELECT 语句来检索网络数据。"
  - question: "Keenable 拥有的网络搜索索引规模有多大？"
    choices: ["约 10 亿个文档", "约 500 亿个文档", "超过 1000 亿个文档"]
    answer: 2
    explanation: "Keenable 通过其自主研发的爬虫和索引系统，拥有超过 1000 亿个文档的索引库。"
  - question: "Keenable API 提供了什么特殊的搜索功能？"
    choices: ["查询过去特定时间点互联网状态的功能", "自动生成个人信息加密", "无限免费使用"]
    answer: 0
    explanation: "Keenable 支持“时间点 (point-in-time) 记录查询”，允许模型不仅可以搜索当前状态，还可以搜索过去特定时间点的互联网信息。"
lang: zh-cn
ref: 2026-09-02-Keenable-SELECT-an-agent-that-searches-the-web-in-SQL
---

想象一下，你告诉秘书：“把昨天新闻里提到的那家公司的股价和相关报道全整理给我。”但秘书回来后，丢给你一叠厚达数万页、复杂且杂乱的纸堆，并对你说：“你自己从中找吧。”你可能会感到非常生气。

这正是迄今为止 AI 代理在互联网搜索时所面临的处境。因为大多数搜索 API 要么是为人类阅读而设计的，要么吐出的是需要 AI 二次清洗的杂乱数据（如 JSON 或 HTML 块）。然而，最近出现了一项旨在解决这种低效问题的技术，它就是 **Keenable SELECT**。

## 为什么它很重要？

到目前为止，AI 代理（AI Agent，指能够自主判断并执行复杂任务的智能体）一直使用搜索 API 来获取网络信息。但由于现有的搜索 API 主要面向人类用户，每当代理执行复杂任务时，都必须进行耗时的“额外工作”来清洗数据 [Source 13, Source 16]。

Keenable SELECT 省去了这一过程。因为它将我们处理数据库时常用的 **SQL (Structured Query Language，用于查询和管理数据的标准语言)** 语法直接引入了网络搜索中。这使得开发者可以命令代理“精准锁定”所需数据。代理不再需要浪费时间解释无关信息，能够更快、更准确地处理复杂业务。

## 轻松理解：图书馆员的比喻

为了方便理解 Keenable SELECT，我们可以借用“图书馆员”的比喻。

如果传统的搜索引擎就像是当被问到“请帮我找齐所有食谱”时，图书馆员把成千上万本食谱堆在桌子上说“你自己找需要的吧”；那么 Keenable SELECT 则完全不同。这项技术就像是向图书馆员下达详细指令：“请帮我挑选出 2025 年以后出版、能在 15 分钟内完成的韩式料理食谱，并整理成列表。”

在技术层面，它是在**模型上下文协议 (MCP，AI 代理的标准通信规则)** 服务器内执行一个名为 'select' 的工具 [Source 12]。当代理输入类似 "SELECT * FROM web WHERE..." 的 SQL 语句时，Keenable 的专有系统会读取网络数据，将其整理成整洁的行（row）形式传给代理 [Source 12]。对代理而言，不再需要为了解析复杂的网页结构而费力。

## 现状如何？

Keenable 不仅仅是一个工具，它是专为 AI 代理设计的独立基础设施 [Source 8, Source 15]。其规模相当庞大：

- **海量知识：** Keenable 构建了自主爬虫和索引系统，将超过 1000 亿个文档数据库化 [Source 5, Source 6, Source 8]。
- **极速响应：** 为了让 AI 代理能实时处理任务，该系统针对美国东部 (us-east) 地区进行了优化，95% 的请求在 250 毫秒（0.25 秒）内处理完毕 [Source 5]。
- **支持历史数据：** 特别有趣的是“时间点记录查询”功能 [Source 9]。这允许代理不仅查询当前的互联网信息，还能精准检索过去特定日期互联网上存在的信息 [Source 9]。

该服务最近成功获得了 2600 万美元的融资，技术实力备受认可 [Source 4, Source 6, Source 9, Source 16]。目前，多家 AI 实验室和数据提供商已在训练及实际服务运营过程中使用该 API [Source 6]。

## 未来会怎样？

Keenable SELECT 的出现展现了“代理时代”搜索技术的发展方向。未来，AI 不再仅仅是下达“搜索一下”的简单命令，像操作数据库那样对网络发起精确查询有望成为标准。当用户说“请把上个月相比有所增长的环保企业股价做成表格”时，AI 代理仅凭几行 SQL 语句就能瞬间从网上提取数据并给出回答的时代，已经触手可及。

## MindTickleBytes 的 AI 记者视角

面向人类的搜索与面向 AI 的搜索本质上必须有所不同。Keenable 的 SQL 接口将推动 AI 代理与网络交互方式的进化。AI 不再仅仅是“阅读”互联网，它正在成为互联网的“查询者”。

## 参考资料

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