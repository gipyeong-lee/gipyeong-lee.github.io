---
layout: learn-module
title: 故障类型分类与错误分析
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:rag-evaluation-reliability:error-analysis
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/error-analysis/
- lang: en
  url: /learn/en/rag-evaluation-reliability/error-analysis/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/error-analysis/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/error-analysis/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/error-analysis/
module_id: m8
permalink: /learn/zh-cn/rag-evaluation-reliability/error-analysis/
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
id: m8
slug: error-analysis
phase_id: p3
estimated_hours: 10.0
prerequisites:
- m7
objectives:
- 能够识别并分类 RAG 系统中出现的故障类型。
- 能够区分并分析检索（Retrieval）阶段与生成（Generation）阶段的错误。
- 利用 Ragas 框架的指标将自动化评估与人工审核结果相关联。
- 基于错误分析数据提出 RAG 流水线性能改进方案。
worked_examples:
- 示例 1：针对问题“模型 A 的发布日期是？”，检索器检索到了“模型 B 的规格”文档。这被归类为“检索失败”，可以通过调整嵌入模型或优化检索查询来解决。
- 示例 2：针对问题“解释 X”，检索器检索到了关于 X 的准确文档，但 LLM 的回答包含了文档中没有的信息。这被归类为“生成失败（忠实度不足）”，应通过提示工程（prompt
  engineering）加强“仅使用所提供的上下文”这一约束。
lab:
  title: 故障数据集收集与错误分析
  steps:
  - 针对至少 50 个问题，保存 RAG 系统的回答及检索到的上下文（context）。
  - 使用 Ragas 测量每个项目的上下文精确度（Context Precision）和生成忠实度（Faithfulness）。
  - 提取指标得分最低的后 20% 的问题-回答对。
  - 针对提取的样本，填写包含“检索错误”、“生成错误”、“逻辑错误”的分类表。
  safety:
  - 严禁在评估代码中包含个人信息或非公开数据。
  - 监控评估过程中使用的 API 调用次数和成本，以确保符合预算。
  - 数据分析时在本地环境中进行工作，以防止信息泄露。
  deliverables:
  - 已完成分类的错误分析 CSV 文件
  - 可视化检索和生成质量指标的 Jupyter Notebook
assignment:
  title: RAG 错误分类及改进报告撰写
  deliverables:
  - 汇总错误分析结果的 2 页报告
  - 针对分类出的不同故障类型的应对策略（检索优化或提示词改进）建议
  rubric:
  - 故障类型分类的准确性和合理性
  - 定量指标与人工审核结果之间的相关性分析能力
  - 改进策略的逻辑合理性
quiz:
- question: 当 RAG 系统中的检索模块检索到不相关的上下文时，会发生什么类型的失败？
  choices:
  - 生成失败
  - 检索失败
  - 数据库连接错误
  - 认证失败
  answer_index: 1
  explanation: 检索模块的作用是识别适合问题的文档，因此检索到不相关的上下文属于检索阶段的失败 [S3]。
- question: Ragas 框架最大的特点是什么？
  choices:
  - 必须具备大规模的人工标注数据。
  - 支持无需参考（Reference-free）的评估。
  - 仅能评估 LLM 生成质量。
  - 仅适用于实时流式系统。
  answer_index: 1
  explanation: Ragas 是一种无需地面真值（ground truth）即可评估检索和生成质量的无需参考评估框架 [S3]。
completion_criteria:
- 提交包含故障类型的错误分类表
- 完成利用 Ragas 指标对检索及生成质量的定量分析
- 完成基于错误分析的流水线改进建议书的撰写及评审
source_ids:
- S3
---

## RAG 系统错误分析概述

RAG（检索增强生成）架构由检索模块和基于 LLM 的生成模块组成 [S3]。在评估系统性能时，将这两个阶段分开分析至关重要。错误主要分为检索阶段的问题和生成阶段的问题。

### 1. 故障类型分类
- **检索失败 (Retrieval Failure):** 检索到不相关或重点不明确的上下文（context）[S3]。
- **生成失败 (Generation Failure):** LLM 未能忠实地使用所提供的上下文（Faithfulness），或生成了与问题无关的回答 [S3]。

### 2. 自动化评估与人工审核的互补
Ragas 等无需参考（Reference-free）的框架可以在没有人工标注（ground truth）的情况下评估检索和生成质量 [S3]。然而，仅凭自动化评估指标很难捕捉到系统微妙的幻觉（hallucination）或复杂的逻辑错误。因此，应通过定量自动指标提取高优先级的故障样本，并必须并行进行人工审核（Human Review）以查明实际原因。
