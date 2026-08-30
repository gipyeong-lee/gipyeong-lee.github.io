---
layout: learn-module
title: 依据忠实度评估
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:rag-evaluation-reliability:generation-faithfulness
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/generation-faithfulness/
- lang: en
  url: /learn/en/rag-evaluation-reliability/generation-faithfulness/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/generation-faithfulness/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/generation-faithfulness/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/generation-faithfulness/
module_id: m5
permalink: /learn/zh-cn/rag-evaluation-reliability/generation-faithfulness/
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
id: m5
slug: generation-faithfulness
phase_id: p2
estimated_hours: 8.0
prerequisites:
- m4
objectives:
- 理解依据忠实度(Faithfulness)的概念及其在RAG系统中的重要性。
- 利用Ragas框架定量评估生成的答案是否基于检索到的上下文(Context)。
- 利用自动化评估指标分析幻觉(Hallucination)风险。
worked_examples:
- 示例 1：如果上下文为“苹果富含维生素C”，答案为“苹果含有大量维生素C，对免疫力有好处”，由于“对免疫力有好处”在上下文中没有信息，因此依据忠实度得分会降低。
- 示例 2：如果上下文为“本公司成立日期为 2020 年 5 月 1 日”，答案为“本公司成立于 2020 年 5 月”，信息一致，因此具有较高的依据忠实度得分。
lab:
  title: 利用Ragas测量生成答案的依据忠实度
  steps:
  - 准备评估数据集（问题、检索到的上下文、生成的答案）。
  - 安装Ragas库并导入 `Faithfulness` 指标。
  - 将准备好的数据集转换为Ragas的数据结构。
  - 配置基于LLM的评估者，计算数据集的依据忠实度得分。
  - 对得分较低的答案进行抽样，并通过人工审查分析其与检索到的上下文之间的差异。
  safety:
  - 不要将包含私密文档或个人隐私的数据集发送给外部LLM API。
  - 确认API请求次数限制，并使用缓存(Cache)来控制成本。
  - 进行人工审查时，保持抽样数据的安全性。
  deliverables:
  - 整个数据集的平均忠实度得分报告
  - 针对低分回答的分析数据集
  - 自动评估结果与人工评估结果的对比分析
assignment:
  title: RAG流水线可靠性评估报告
  deliverables:
  - 包含忠实度评估的Jupyter Notebook
  - 错误分类及幻觉发生频率分析报告
  rubric:
  - 是否正确实现了忠实度指标？
  - 是否准确分类了生成回答中的幻觉案例？
  - 自动评估结果与人工评估是否具有定性一致性？
quiz:
- question: 在RAG系统中，什么是忠实度（Faithfulness）？
  choices:
  - 检索到的上下文与问题的相关程度
  - 生成的回答基于检索到的上下文信息的程度
  - LLM利用预训练知识的程度
  - 回答与用户问题的精确匹配程度
  answer_index: 1
  explanation: 忠实度是评估生成的回答是否依赖于外部检索到的上下文事实的指标。
- question: 下列关于Ragas框架的描述正确的是？
  choices:
  - 必须有基准答案（Ground Truth）才能进行评估。
  - 支持无引用（reference-free）的评估方式。
  - 仅评估检索效率，不评估生成质量。
  - 不使用LLM作为评估者，仅使用统计方法。
  answer_index: 1
  explanation: Ragas的目标是实现无需基准答案即可评估，并积极利用LLM作为评估者 [S3, S4]。
completion_criteria:
- 能够使用Ragas库定量测量生成回答的忠实度。
- 能够从评估结果中分类至少 3 种幻觉发生类型。
- 能够验证自动化评估流水线的结果与实际回答的一致性。
source_ids:
- S3
- S4
---

## 依据忠实度 (Faithfulness) 评估

RAG(检索增强生成)系统的核心在于利用LLM检索外部知识数据库中的信息来生成答案。依据忠实度(Faithfulness)是衡量生成的答案是否忠实地反映了检索到的上下文中技术信息的指标 [S3]。

### 1. 为什么评估依据忠实度？
LLM倾向于基于预训练知识进行回答，可能会生成与检索到的上下文无关的信息或扭曲上下文。这被称为“幻觉(Hallucination)”，通过依据忠实度评估可以定量衡量这一点 [S4]。

### 2. 评估框架：Ragas
Ragas提出了一种在没有用户注释的情况下，无需参考(reference-free)即可进行评估的框架 [S3]。依据忠实度评估过程通常遵循以下步骤：
- **从答案中提取陈述**：从答案中分离出可验证的事实性陈述。
- **证据检索**：确认每个陈述是从检索到的上下文的哪部分推导出来的。
- **验证**：判断提取出的陈述是否与上下文信息一致。

Ragas使用LLM作为评估者来自动化这一过程 [S4]。
