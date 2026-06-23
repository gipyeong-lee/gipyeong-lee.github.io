---
layout: post
title: "AI 代理的“长期记忆”局限，Elasticsearch 以 0.89 的准确率实现突破"
description: "AI 代理如何记住过往对话和用户偏好？本文为您简要解读 Elasticsearch 如何通过技术手段实现长期记忆，并达到 0.89 的高准确率。"
summary: "Elasticsearch 利用最新的混合搜索技术显著提升了 AI 代理的长期记忆能力，实现了 0.89 的高记忆召回率（recall）。"
tags: [AI, Elasticsearch, 数据技术, AI代理]
image: 2026-06-23-We-built-a-persistent-agent-memory-layer-on-Elasticsearch-with-089-recall.jpg
image_alt: "可视化基于 Elasticsearch 的 AI 代理长期记忆结构图形"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 代理能够“记住”用户的上下文，这不仅仅是简单的存储。在海量信息中准确提取所需上下文的技术，才是真正智能化服务的核心。"
quiz:
  - question: "Elasticsearch 为提升 AI 代理记忆力所采用的主要技术组合是什么？"
    choices: ["顺序数据存储", "混合搜索、RRF 和重排序器 (Reranker)", "随机数据删除"]
    answer: 1
    explanation: "Elasticsearch 使用了混合搜索、RRF (互惠排名融合) 和重排序器 (Reranker) 来提高信息检索的准确性。"
  - question: "Elasticsearch 代理内存所记录的记忆召回率 (recall) 数值是多少？"
    choices: ["0.65", "0.79", "0.89"]
    answer: 2
    explanation: "Elasticsearch 的新内存分层结构在 168 个问题测试中实现了 0.89 的高记忆召回率。"
  - question: "Elasticsearch 代理内存中提到的安全功能是什么？"
    choices: ["通过动态级别安全 (DLS) 实现租户间数据隔离", "所有数据公开", "存储时不进行额外加密"]
    answer: 0
    explanation: "Elasticsearch 利用动态级别安全 (DLS) 对租户 (用户组) 进行严格隔离，防止数据混淆。"
lang: zh-cn
ref: 2026-06-23-We-built-a-persistent-agent-memory-layer-on-Elasticsearch-with-089-recall
---

想象一下，你每天早上告诉秘书“按我的日程准备会议”，但秘书每次都会重新问你是谁，更别提记住昨天的对话了。这正是目前许多 AI 代理所面临的困境。无论代理多么聪明，如果无法记住用户的偏好或过去的上下文，它就只是一个“半吊子”助手。

Elasticsearch 最近宣布，为了解决这一问题，他们已经为 AI 代理构建了“持久化代理内存层 (Persistent Agent Memory Layer)” [出处: Agent memory on Elasticsearch: hybrid retrieval and DLS - Elasticsearch Labs](https://www.elastic.co/search-labs/blog/agent-memory-elasticsearch)。其核心在于，它不仅充当单纯的数据仓库，更通过最大化“记忆力”来确保在需要时能准确提取信息。

## 为什么这很重要？

随着 AI 技术的发展，模型规模的扩张已不再是唯一重点，“多大程度上理解用户上下文”变得愈发关键。当代理具备记忆力后，我们的日常生活将发生以下巨大变化：

1. **持续的个性化**：即使跨越多个对话会话，也能维持用户的偏好或特定项目的详细信息。例如，代理可以自动记住用户过去偏好的报告格式，并在下次自动应用 [出处: AI agent memory: Agentic AI memory management with Elasticsearch - Elasticsearch Labs](https://www.elastic.co/search-labs/blog/ai-agent-memory-management-elasticsearch)。
2. **严密的安全保障**：在企业环境中，A 团队的对话内容绝对不能泄露给 B 团队。此次构建的内存层配备了强大的安全机制，确保租户（用户组）之间的数据互不干扰 [出处: Elastic builds agent memory system on Elasticsearch using three indices, hybrid recall, supersession; achieves 0.89 recall with zero cross-tenant data leaks.](https://newsscore.com/story/170580)。

## 通俗易懂：AI 的“智能图书馆”

我们可以这样比喻：如果传统的 AI 代理内存只是一个随便记录的“挥发性记事本”，那么这次的系统就是一个有条理地整理必要信息的“智能图书馆”。

AI 不再是单纯地按顺序排列所有数据，而是使用三种分类体系（索引）来管理数据。其中最引人注目的是 **“混合检索 (Hybrid Retrieval)”**。

* **搜索的复合术**：通过使用将多个搜索结果合并为单一排名的 RRF（互惠排名融合）以及重新评估搜索结果重要性的重排序器（Reranker），不仅能找到单纯的关键词匹配信息，更能锁定最接近用户意图的核心内容 [出处: Persistent memory for agents: Claude Code on Elasticsearch - Elasticsearch Labs](https://www.elastic.co/search-labs/blog/persistent-memory-agents-elasticsearch-claude-code)。
* **智能记忆管理**：随着时间推移，信息价值会流失。通过自动处理旧信息的技巧（衰减）以及用最新信息覆盖旧信息的机制（覆盖），系统时刻保持记忆仓库的整洁与准确 [出处: A2A Protocol & MCP: Creating an LLM Agent newsroom in Elasticsearch - Elasticsearch Labs](https://www.elastic.co/search-labs/blog/a2a-protocol-mcp-llm-agent-workflow-elasticsearch)。

## 现状：0.89 的记忆召回率

Elasticsearch 的这一新结构在 168 个不同问题的测试中记录了 **0.89 的记忆召回率 (recall)** [出处: Agent memory on Elasticsearch: hybrid retrieval and DLS - Elasticsearch Labs](https://www.elastic.co/search-labs/blog/agent-memory-elasticsearch)。这意味着 AI 在接到提问时，能够在大约 90% 的情况下准确找到所需信息。尤为显著的成果是“零数据泄露”。得益于针对每个用户组应用的 DLS（动态级别安全）技术，彻底避免了他人的记忆混入 [出处: Elastic builds agent memory system on Elasticsearch using three indices, hybrid recall, supersession; achieves 0.89 recall with zero cross-tenant data leaks.](https://newsscore.com/story/170580)。

## 未来展望

未来，代理的能力将不再局限于简单的记忆对话，其自主操作和管理数据的能力将进一步升级。例如，当用户说“以后这种设置都按默认值处理”时，代理会将其移至长期记忆（long-term memory）并存储，从而在后续交互中自动应用 [出处: AI agent memory: Agentic AI memory management with Elasticsearch - Elasticsearch Labs](https://www.elastic.co/search-labs/blog/ai-agent-memory-management-elasticsearch)。这项研究标志着 Elasticsearch 已不仅仅是已知的搜索工具，更正在演变成 AI 的核心认知结构——“内存引擎”。

## MindTickleBytes AI 记者观点
AI 代理能够“记住”用户的上下文，这不仅仅是简单的存储。在海量信息洪流中准确提取用户所需上下文的技术，才是真正智能化服务的核心。这项技术是 AI 开始真正理解我们生活的又一个里程碑。

## 参考资料

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