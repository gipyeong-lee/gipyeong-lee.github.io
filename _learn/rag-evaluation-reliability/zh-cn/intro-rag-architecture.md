---
layout: learn-module
title: 理解 RAG 架构
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:rag-evaluation-reliability:intro-rag-architecture
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/intro-rag-architecture/
- lang: en
  url: /learn/en/rag-evaluation-reliability/intro-rag-architecture/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/intro-rag-architecture/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/intro-rag-architecture/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/intro-rag-architecture/
module_id: m1
permalink: /learn/zh-cn/rag-evaluation-reliability/intro-rag-architecture/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: f439c689d3754cecbf386ffcc0c2bd7c
translation_run_id: a3ecae3cd64041daa42409713fd13427
primary_category: ai-software
topics:
- retrieval-augmented-generation
- rag-evaluation
- information-retrieval
- llm-reliability
course_type: academic
published_at: '2026-08-30T15:42:37.390479+09:00'
id: m1
slug: intro-rag-architecture
phase_id: p1
estimated_hours: 8.0
prerequisites: []
objectives:
- 理解 RAG (Retrieval-Augmented Generation) 架构的核心组件。
- 识别大语言模型 (LLM) 的知识局限性以及检索增强的必要性。
- 能够解释检索-生成流水线的结构流程。
worked_examples:
- '案例 1: 传统 LLM 方式 - 若提问“告诉我今天的新闻”，因无法获知训练数据之后发生的事件，存在生成错误信息的风险。'
- '案例 2: RAG 方式 - 当提问“告诉我今天的新闻”时，1) 检索器 (Retriever) 通过外部搜索引擎或实时新闻 API 收集相关报道，2) 将其作为上下文
  (context) 包含在内传递给 LLM，从而生成准确的最新信息回答。'
lab:
  title: RAG 架构流程可视化与分析
  steps:
  - 打开 Jupyter Notebook，对 RAG 基本流水线的 3 阶段（输入、检索、生成）结构进行绘图。
  - 从开源授权文档语料库中提取 5 个短文本，制作数据集样本。
  - 编写简单的关键词匹配检索器 (Retriever) 函数，实现根据问题返回对应文档。
  - 通过代码编写将检索到的文档注入提示词模板的增强阶段。
  safety:
  - 绝不使用实际个人信息或机密文档作为语料库数据。
  - 使用 API 时确认调用次数限制 (Rate Limit)，并在测试代码中设置种子 (seed) 值以确保可重现性。
  deliverables:
  - RAG 架构图 (包含在 Notebook 单元中)
  - 简单的基于关键词的检索器实现代码
  - 文档注入型提示词生成结果
assignment:
  title: 基于 RAG 的信息检索流水线分析报告
  deliverables:
  - 解释所实现 RAG 流水线工作原理的 Notebook
  - 检索器在判断文档相关性时可能产生的潜在失败案例 3 种技术描述
  rubric:
  - RAG 的 3 阶段（检索、增强、生成）是否被准确区分并解释？
  - 对于检索阶段可能检索到无关文档的分析是否合理？
  - 是否遵守非公开数据安全指南进行实现？
quiz:
- question: 与 LLM 训练方式相比，RAG 的主要优点是什么？
  choices:
  - 可以减小 LLM 的参数规模。
  - 可以让模型的知识保持最新并提出依据。
  - 可以加速模型的训练速度。
  - 可以生成 100% 事实正确的回答。
  answer_index: 1
  explanation: 由于 RAG 引用外部文档，因此可以反映最新信息，并且可以在文档中找到生成回答的依据，从而具有高可靠性。
- question: 下列哪项是检索器 (Retriever) 的正确角色？
  choices:
  - 负责生成回答。
  - 负责重新训练学习数据。
  - 负责检索与问题相关的外部文档片段。
  - 负责管理用户界面。
  answer_index: 2
  explanation: 检索器的作用是从外部数据源中查找与用户的问题语义相似或相关性高的文档。
completion_criteria:
- 能够解释 RAG 架构的组件。
- 确认实操的 RAG 流水线代码正常运行，能够检索并增强相关文档。
- 在分析报告中描述 RAG 流水线的局限性与改进方向。
source_ids:
- S1
- S2
---

## RAG (Retrieval-Augmented Generation) 架构概述

最新的自然语言处理 (NLP) 和深度学习模型通过学习海量文本数据展现出卓越性能，但在处理模型训练时未包含的最新信息或特定领域的非公开数据时，存在幻觉 (hallucination) 或无法获知信息的局限性 [S1]。

### 通过检索克服 LLM 的局限性
RAG 不是让模型在参数 (parameter) 内部死记硬背所有知识，而是在“适当时机 (just-in-time)”检索与问题相关的外部可靠文档，并将其提供给生成阶段作为输入的方案 [S2]。

### 核心组件
1. **检索器 (Retriever)**: 接收用户查询 (query)，从向量数据库等中识别相关性高的文档片段 (chunk)。
2. **增强 (Augmentation)**: 组合检索到的文档与原始问题，构成传递给 LLM 的提示词。
3. **生成器 (Generator)**: 基于增强后的信息生成事实依据的回答。

这种结构有助于使模型的知识保持最新，并追踪生成答案的依据，从而在确保可靠性方面做出贡献。
