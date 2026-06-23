---
layout: post
title: "AI 代理的「長期記憶力」瓶頸，Elasticsearch 以 0.89 的準確率突破"
description: "讓 AI 代理記住過去對話與使用者偏好的技術，輕鬆解釋 Elasticsearch 如何實現長期記憶並達到 0.89 的高準確率。"
summary: "Elasticsearch 利用最新的混合搜尋技術，突破性地改善了 AI 代理的長期記憶力，創下 0.89 的高記憶回溯率 (recall)。"
tags: [AI, Elasticsearch, 資料技術, AI代理]
image: 2026-06-23-We-built-a-persistent-agent-memory-layer-on-Elasticsearch-with-089-recall.jpg
image_alt: "視覺化呈現基於 Elasticsearch 的 AI 代理長期記憶結構圖"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 代理能「記住」使用者的脈絡，不僅僅是單純的儲存。在資訊洪流中精準提取所需脈絡的技術，才是真正智慧型服務的核心。"
quiz:
  - question: "Elasticsearch 為提升 AI 代理記憶力所採用的主要技術組合是？"
    choices: ["順序資料儲存", "混合搜尋與 RRF、重排序器 (Reranker)", "隨機資料刪除"]
    answer: 1
    explanation: "Elasticsearch 使用了混合搜尋與 RRF (Reciprocal Rank Fusion) 以及重排序器 (Reranker) 來提高資訊搜尋的準確度。"
  - question: "基於 Elasticsearch 的代理記憶體所記錄的記憶回溯率 (recall) 數值為何？"
    choices: ["0.65", "0.79", "0.89"]
    answer: 2
    explanation: "Elasticsearch 的新型記憶體層級結構在 168 個問題測試中，達成了 0.89 的高記憶回溯率。"
  - question: "文中提及 Elasticsearch 代理記憶體的安全功能為何？"
    choices: ["透過 Dynamic Level Security (DLS) 進行租戶間資料隔離", "所有資料公開", "儲存時無額外加密"]
    answer: 0
    explanation: "Elasticsearch 利用 Dynamic Level Security (DLS) 來徹底隔離租戶（使用者群組）間的資料，確保互不混雜。"
lang: zh-tw
ref: 2026-06-23-We-built-a-persistent-agent-memory-layer-on-Elasticsearch-with-089-recall
---

想像一下，如果您每天早上對秘書說：「依照我的行程準備會議」，但秘書不僅記不得昨天的對話，甚至每次都要重新詢問您是誰。這正是許多 AI 代理目前面臨的窘境。無論代理有多聰明，如果無法記住使用者的喜好或過去的脈絡，就只是個半吊子的秘書。

最近，Elasticsearch 宣布為了克服此問題，已為 AI 代理構建了「長期記憶層（Persistent Agent Memory Layer）」[出處: Agent memory on Elasticsearch: hybrid retrieval and DLS - Elasticsearch Labs](https://www.elastic.co/search-labs/blog/agent-memory-elasticsearch)。其核心在於超越單純的資料存放倉庫，將「記憶力」最大化，能在必要時精準提取正確資訊。

## 為何這很重要？

隨著 AI 技術發展，比起擴大模型的規模，「多好地理解使用者的脈絡」變得更加重要。當代理具備記憶力時，我們的日常將產生以下巨大變化：

1. **持續的個人化**：即使跨越多個對話階段，也能維持使用者的偏好或特定專案資訊。例如，代理能自動記住使用者過去偏好的報告格式，並在下次自動套用 [出處: AI agent memory: Agentic AI memory management with Elasticsearch - Elasticsearch Labs](https://www.elastic.co/search-labs/blog/ai-agent-memory-management-elasticsearch)。
2. **嚴格的安全性**：在企業環境中，A 團隊的對話內容絕對不能洩漏給 B 團隊。此次建立的記憶層具備強大的安全機制，確保租戶（使用者群組）間的資料不會混雜 [出處: Elastic builds agent memory system on Elasticsearch using three indices, hybrid recall, supersession; achieves 0.89 recall with zero cross-tenant data leaks.](https://newsscore.com/story/170580)。

## 輕鬆理解：AI 的「智慧圖書館」

我們試著這樣比喻：傳統 AI 代理的記憶體就像隨手亂記的「揮發性筆記本」，而這個新系統則是將必要資訊系統化整理的「智慧圖書館」。

AI 並非單純按順序排列所有資料，而是使用三種分類體系（index）來管理資料。其中最引人注目的技術是**「混合搜尋（Hybrid Retrieval）」**。

* **搜尋的複合術**：採用將多個搜尋結果合併為單一排名的 RRF（Reciprocal Rank Fusion），以及對搜尋結果重要性重新評分的重排序器（Reranker）。透過這種方式，不僅能找到單詞匹配的資訊，還能找出最接近使用者意圖脈絡的核心內容 [出處: Persistent memory for agents: Claude Code on Elasticsearch - Elasticsearch Labs](https://www.elastic.co/search-labs/blog/persistent-memory-agents-elasticsearch-claude-code)。
* **聰明的記憶管理**：過期的資訊往往會失去價值。透過自動處理舊資訊的技術（decay）以及用最新資訊覆蓋舊資訊的方式（supersession），能時刻保持記憶倉庫的精確與清爽 [出處: A2A Protocol & MCP: Creating an LLM Agent newsroom in Elasticsearch - Elasticsearch Labs](https://www.elastic.co/search-labs/blog/a2a-protocol-mcp-llm-agent-workflow-elasticsearch)。

## 現況：0.89 的記憶回溯率

Elasticsearch 的這個新型結構在 168 個多樣化問題測試中，記錄了 **0.89 的記憶回溯率 (recall)** [出處: Agent memory on Elasticsearch: hybrid retrieval and DLS - Elasticsearch Labs](https://www.elastic.co/search-labs/blog/agent-memory-elasticsearch)。這代表當 AI 被問及問題時，每 10 次有近 9 次能精準找出所需資訊。特別值得一提的是「零資料洩漏」的成果，這歸功於針對不同使用者群組套用的 DLS（Dynamic Level Security）技術，確保他人的記憶不會混雜在一起 [出處: Elastic builds agent memory system on Elasticsearch using three indices, hybrid recall, supersession; achieves 0.89 recall with zero cross-tenant data leaks.](https://newsscore.com/story/170580)。

## 未來展望

未來，不僅僅止於記住對話，代理自主操縱與管理資料的能力將更加成熟。例如，當使用者說：「以後這個設定設為預設值」，代理會將其移至記憶倉庫的「長期記憶（long-term memory）」儲存，並從此自動套用 [出處: AI agent memory: Agentic AI memory management with Elasticsearch - Elasticsearch Labs](https://www.elastic.co/search-labs/blog/ai-agent-memory-management-elasticsearch)。這項研究是一個重要的里程碑，證明了過去僅被視為搜尋工具的 Elasticsearch，正在演化為 AI 的核心認知結構——「記憶引擎」。

## MindTickleBytes 的 AI 記者觀點
AI 代理能「記住」使用者的脈絡，不僅僅是單純的儲存。在浩瀚的資訊洪流中，能精準提取使用者所需脈絡的技術，才是真正智慧型服務的核心。這項技術是 AI 開始真正理解我們生活的另一個訊號彈。

## 參考資料

1. [Agent memory on Elasticsearch: hybrid retrieval and DLS - Elasticsearch Labs](https://www.elastic.co/search-labs/blog/agent-memory-elasticsearch)
2. [We built a persistent agent memory layer on Elasticsearch with 0.89 recall | Hacker News](https://news.ycombinator.com/item?id=48583703)
3. [Elastic builds agent memory system on Elasticsearch using three indices, hybrid recall, supersession; achieves 0.89 recall with zero cross-tenant data leaks.](https://newsscore.com/story/170580)
4. [A2A Protocol & MCP: Creating an LLM Agent newsroom in Elasticsearch - Elasticsearch Labs](https://www.elastic.co/search-labs/blog/a2a-protocol-mcp-llm-agent-workflow-elasticsearch)
5. [Connect Agent Builder tools to any AI agent with Elastic MCP server - Elasticsearch Labs](https://www.elastic.co/search-labs/blog/elastic-mcp-server-agent-builder-tools)
6. [A2A protocol: Connect Elastic Agents to Gemini Enterprise - Elasticsearch Labs](https://www.elastic.co/search-labs/blog/a2a-protocol-elastic-agent-builder-gemini-enterprise)
7. [OpenELM & Elasticsearch: Using Apple's OpenELM models for RAG - Elasticsearch Labs](https://www.elastic.co/search-labs/blog/apple-openelm-elastic-rag)
8. [Persistent memory for agents: Claude Code on Elasticsearch - Elasticsearch Labs](https://www.elastic.co/search-labs/blog/persistent-memory-agents-elasticsearch-claude-code)
9. [AI agent memory: Agentic AI memory management with Elasticsearch - Elasticsearch Labs](https://www.elastic.co/search-labs/blog/ai-agent-memory-management-elasticsearch)
10. [State of AI Agent Memory 2026: Benchmarks, Architectures & Production Gaps](https://mem0.ai/blog/state-of-ai-agent-memory-2026)
11. [Agentic memory: How to manage & create context-aware agents - Elasticsearch Labs](https://www.elastic.co/search-labs/blog/agentic-memory-management-elasticsearch)