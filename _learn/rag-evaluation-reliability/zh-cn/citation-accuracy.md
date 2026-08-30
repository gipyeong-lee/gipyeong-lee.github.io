---
layout: learn-module
title: 引用准确度及来源追踪
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:rag-evaluation-reliability:citation-accuracy
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/citation-accuracy/
- lang: en
  url: /learn/en/rag-evaluation-reliability/citation-accuracy/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/citation-accuracy/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/citation-accuracy/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/citation-accuracy/
module_id: m6
permalink: /learn/zh-cn/rag-evaluation-reliability/citation-accuracy/
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
id: m6
slug: citation-accuracy
phase_id: p2
estimated_hours: 8.0
prerequisites:
- m5
objectives:
- 理解RAG系统中的回答在多大程度上忠实于检索到的文档内容。
- 学习引用（Citation）准确度的定义及其测量方式。
- 利用Ragas框架定量评估回答的忠实度（Faithfulness）和回答相关性（Answer Relevance）。
- 设计验证模型回答中来源可追踪性的流程。
worked_examples:
- 示例 1：忠实度得分计算。针对问题“A公司的 2025 年销售额是多少？”，生成了回答“A公司的 2025 年销售额为 100 亿。”。如果背景文档中包含“A公司在
  2025 年记录了 100 亿销售额。”，由于回答的所有信息都存在于上下文中，因此该回答的忠实度得分被评为 1.0（最高分）。
- 示例 2：引用准确度错误识别。针对问题“A公司的成立年份是？”，生成了回答“A公司成立于 1990 年（参考：文档 1）。”，但文档 1 中明确写着“A公司成立于
  1995 年”，这被归类为“事实扭曲”失败类型，并判定为引用准确度较低。
lab:
  title: 使用Ragas进行回答忠实度自动化评估实践
  steps:
  - 准备待评估RAG系统的检索结果（Context）和生成的回答（Answer）数据集。
  - 安装Ragas框架并加载回答数据集。
  - 使用Ragas的 `Faithfulness` 指标为数据集中的每个问答对计算得分。
  - 单独提取出忠实度低于 0.7 的 30 条回答。
  - 对提取的样本进行人工审核，并标记对应的失败类型（“漏引”、“虚假引用”、“事实扭曲”）。
  safety:
  - 在评估过程中使用的文档语料库中，请预先进行去标识化处理，以防包含个人信息或企业机密。
  - 调用外部API时请设定费用上限，并固定随机种子（Seed）值以确保可重现性，防止重复产生API费用。
  deliverables:
  - 包含评估结果的Jupyter Notebook文件（.ipynb）
  - 忠实度得分分布可视化图表
  - 包含人工审核记录的失败类型分类表
assignment:
  title: RAG系统可靠性回归评估报告撰写
  deliverables:
  - 基于两种以上RAG设置（例如更改检索Top-k值）的忠实度统计对比结果
  - 针对 30 条样本的人工审核对照表
  - 旨在提高系统引用准确度的改进方案建议书
  rubric:
  - 是否准确说明了评估指标的定量计算方法？
  - 检索文档与生成回答之间的引用关系是否逻辑可追溯？
  - 失败类型分类是否与人工审核数据一致并提出了合理的论据？
quiz:
- question: 下列关于Ragas框架“忠实度（Faithfulness）”指标的解释正确的是？
  choices:
  - 评估回答与问题是否相关。
  - 测量回答中的所有信息是否都存在于提供的上下文文档中。
  - 评估回答在语法上是否正确。
  - 测量回答是否包含了外部知识库的所有信息。
  answer_index: 1
  explanation: 忠实度是测量生成的回答中主张是否有据可依（基于检索到的上下文）的指标。
- question: 在进行引用准确度评估时，哪种情况属于“事实扭曲”失败类型？
  choices:
  - 在回答中包含了检索文档中不存在的内容。
  - 遗漏了引用标记。
  - 虽然正确标记了引用，但在描述时误解了原意导致事实关系有误。
  - 回答与问题的意图完全不同。
  answer_index: 2
  explanation: 事实扭曲是指即使引用了源文档，但在概括或转换原文档信息时产生错误的情况。
completion_criteria:
- 通过Jupyter Notebook完成自动化评估指标计算。
- 提交至少 30 条回答样本的人工审核及失败类型分类记录。
- 编写包含评估结果及改进方案的最终报告。
source_ids:
- S4
---

## RAG系统的引用及忠实度评估

RAG（检索增强生成）系统利用外部知识库来降低LLM产生幻觉（Hallucination）的风险，但验证生成的回答是否准确引用了检索到的文档是一个必要过程 [S4]。

### 1. 主要评估指标
* **忠实度 (Faithfulness)：** 衡量生成的回答是否源于提供的检索上下文（Context）。回答中的所有主张都必须基于检索到的文档，如果仅凭外部知识或模型的预训练知识进行回答，得分会降低 [S4]。
* **回答相关性 (Answer Relevance)：** 评估回答与给定问题之间的直接相关程度。即使检索到的信息充足，该指标也能用于识别回答偏离问题意图的情况。

### 2. 引用准确度验证流程
引用准确度是指识别回答中的特定句子引用了检索上下文的哪一部分，并确认其是否与原文档的事实一致的过程。自动化评估框架Ragas为这一过程提供了无需引用数据（Ground Truth）即可评估忠实度的指标 [S4]。

### 3. 失败类型分类
- **漏引：** 回答的事实关系虽存在于检索文档中，但未进行引用标注。
- **虚假引用：** 将检索文档中不存在的内容标记为引用。
- **事实扭曲：** 虽然正确标记了引用，但因误解原意而导致生成内容有误。
