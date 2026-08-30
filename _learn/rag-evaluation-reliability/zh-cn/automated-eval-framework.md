---
layout: learn-module
title: 自动化评估框架（Ragas）应用
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:rag-evaluation-reliability:automated-eval-framework
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/automated-eval-framework/
- lang: en
  url: /learn/en/rag-evaluation-reliability/automated-eval-framework/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/automated-eval-framework/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/automated-eval-framework/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/automated-eval-framework/
module_id: m7
permalink: /learn/zh-cn/rag-evaluation-reliability/automated-eval-framework/
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
id: m7
slug: automated-eval-framework
phase_id: p2
estimated_hours: 10.0
prerequisites:
- m6
objectives:
- 理解RAG流水线的核心评估维度（检索及生成质量）。
- 学习如何使用Ragas框架进行无引用（reference-free）的RAG性能自动化评估。
- 通过定量指标分析并缓解幻觉（hallucination）风险。
worked_examples:
- 案例 1：Context Relevance 计算。Ragas利用LLM从检索到的上下文（Context）中提取回答问题实际所需的句子，并通过所需句子占整个上下文的比例来计算得分。
- 案例 2：Faithfulness 评估。由LLM判断生成的回答中的每一项主张是否都能在检索到的上下文中找到支撑。无法得到支撑的主张越多，幻觉得分就越高。
lab:
  title: 使用Ragas进行RAG性能定量评估实践
  steps:
  - 准备评估数据集（问题、检索到的上下文、生成的回答）。
  - 在Python环境中安装 `ragas` 库。
  - 将评估数据集转换为 `ragas` 的 Dataset 对象。
  - 调用 Ragas 的 `evaluate` 函数来计算上下文相关性（Context Relevance）、忠实度（Faithfulness）等指标。
  - 可视化结果并分析得分较低的查询。
  safety:
  - 确认评估使用的文档语料库中不包含个人信息或非公开数据。
  - 为防止API使用成本过高，在测试时请积极使用本地模型或缓存。
  - 自动化评估结果是衡量可靠性的辅助指标，实际模型质量的确定应结合人工样本审核进行交叉验证。
  deliverables:
  - 包含指标得分的评估结果数据框（Dataframe）
  - 低分查询类型的分析日志
assignment:
  title: RAG流水线性能对比报告
  deliverables:
  - 两种不同检索设置（k值、嵌入模型等）的RAG流水线的Ragas评估结果
  - 两种设置间的性能差异分析报告
  rubric:
  - 是否正确实现了Ragas指标（Context Relevance, Faithfulness等）？
  - 评估结果是否进行了定量对比并包含了逻辑解释？
  - 是否分类了至少 3 种幻觉类型并提出了改进方案？
quiz:
- question: Ragas框架最大的特点是什么？
  choices:
  - 必须拥有人工标注的答案数据集
  - 可以在无引用（reference-free）的情况下评估RAG流水线
  - 仅评估检索阶段，不评估生成阶段
  - 必须至少拥有 10 个GPU
  answer_index: 1
  explanation: Ragas是一个无需基准答案数据集，利用LLM自动评估检索和生成质量的框架 [S3, S4]。
- question: Ragas中衡量的“Faithfulness”指标定义是什么？
  choices:
  - 检索到的上下文与问题有多大关联
  - 问题是否存在于文档语料库中
  - 生成的回答是否基于检索到的上下文
  - 提问者对LLM回答的信任程度
  answer_index: 2
  explanation: Faithfulness是衡量生成的回答在多大程度上基于提供的检索上下文（防止幻觉）的指标 [S4]。
completion_criteria:
- 使用 Ragas 库成功计算至少 10 个查询的 4 种以上指标
- 定期将实操笔记本提交至 Git 仓库
- 性能比较报告中至少包含 3 个错误分类案例
source_ids:
- S3
- S4
---

## RAG评估的挑战与Ragas

RAG系统由检索模块和基于LLM的生成模块组成 [S3, S4]。评估这种结构是一项挑战，因为必须同时考虑检索系统识别相关上下文（context）的准确度、LLM利用所提供上下文的忠实度（faithfulness）以及回答的质量 [S4]。

传统的评估方式依赖于人工编写答案并进行对比，但这不仅成本高昂，而且耗时，不适合快速迭代周期 [S3, S4]。

### Ragas框架
Ragas (Retrieval Augmented Generation Assessment) 是一个无需基准数据集即可评估RAG流水线的框架 [S3, S4]。Ragas会自动评估以下核心维度：

1. **检索质量 (Retrieval Quality)：** 衡量检索到的上下文与问题的相关性（Context Relevance），以及是否包含所有必要信息（Context Recall）。
2. **生成质量 (Generation Quality)：** 衡量生成的回答是否基于检索到的上下文（Faithfulness），以及是否与问题相关（Answer Relevance）。

这些指标通过利用LLM作为“评估者（judge）”，实现了无需基准答案即可进行评估，有助于缩短RAG的开发周期 [S3, S4]。
