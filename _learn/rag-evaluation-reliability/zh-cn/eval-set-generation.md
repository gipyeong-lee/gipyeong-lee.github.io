---
layout: learn-module
title: 构建问答评估集
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:rag-evaluation-reliability:eval-set-generation
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/eval-set-generation/
- lang: en
  url: /learn/en/rag-evaluation-reliability/eval-set-generation/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/eval-set-generation/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/eval-set-generation/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/eval-set-generation/
module_id: m3
permalink: /learn/zh-cn/rag-evaluation-reliability/eval-set-generation/
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
id: m3
slug: eval-set-generation
phase_id: p1
estimated_hours: 8.0
prerequisites:
- m2
objectives:
- 理解构建用于评估 RAG 系统的高质量问答 (QA) 评估集的重要性。
- 掌握利用合成数据生成技术 (Synthetic Data Generation) 构建评估集的原理。
- 通过 TrueTeacher 等方法论，掌握评估模型生成回答事实一致性的逻辑。
- 设计在保持评估集质量的同时，能够生成对领域变化具有稳健性的数据集的流程。
worked_examples:
- 示例 1：从文档语料库中提取关键段落。使用LLM从给定文档中提取上下文中重要的事实性句子，并以此为基础构建包含“可回答问题”和“错误问题(Negative Sample)”的流水线。
- 示例 2：事实性验证提示词设计。基于生成的问题和检索到的文档，指示LLM“根据检索到的文档回答问题，并判断答案在事实层面上是否一致（True/False）”，从而细化评估用的标准答案(Ground
  Truth)的过程。
lab:
  title: 合成评估集生成实践
  steps:
  - 加载准备好的开源文档语料库，并将其划分为文本块。
  - 使用LLM API为每个文本块生成 100 个以上的唯一问答对。
  - 针对生成的问题模拟检索系统，搜索并返回前k个文档。
  - 构建评估流水线，以判断检索到的文档与生成的答案之间的事实一致性。
  - 将结果数据保存为JSONL格式，并手动检查 30 个样本以记录数据质量。
  safety:
  - 在评估集构建过程中使用外部API时，必须设置费用上限(API Key Limit)。
  - 使用正则表达式过滤生成的数据集，确保其中不包含原始文档的敏感信息或个人隐私。
  - 不可盲目依赖模型评估结果，必须结合人工抽样核对。
  deliverables:
  - 已构建 100 条目以上的问答评估集(JSONL文件)
  - 包含数据集生成和验证代码的Jupyter Notebook
  - 包含人工审查记录的质量分析报告
assignment:
  title: RAG可靠性评估集回归报告
  deliverables:
  - 分析评估集统计分布（问题长度、答案长度、文档引用频率等）的仪表板
  - 使用相同评估集比较两种以上RAG设置（例如：更改检索算法、更改模型）的结果
  - 错误分类表（幻觉、上下文不相关等）编写及案例分析
  rubric:
  - 评估集是否均匀反映了整个文档语料库的内容？
  - 合成数据生成流水线是否以可重现的形式编写？
  - 错误类型分类是否具体且具有定量依据？
  - 是否通过人工审查验证了自动评估指标的有效性？
quiz:
- question: TrueTeacher方法论与传统的合成数据生成方式有何区别？
  choices:
  - 完全依赖人工编写的摘要。
  - 通过注释模型生成的各种摘要来生成合成数据。
  - 仅使用小型模型作为学习用的教师模型。
  - 仅通过手工编写数据集来提高准确性。
  answer_index: 1
  explanation: TrueTeacher不依赖人工编写的摘要，而是利用LLM通过注释模型生成的各种摘要来生成合成数据 [S5]。
- question: 在构建RAG评估集时，为什么不能仅通过模型自动评估来确定事实性？
  choices:
  - 因为模型自动评估比人类慢得多。
  - 因为模型自动评估并不完美，无法完全过滤掉幻觉(Hallucination)。
  - 因为人工评估不需要成本。
  - 因为事实性评估不需要模型。
  answer_index: 1
  explanation: 自动化评估工具虽然高效但并不完美，因此为了进行事实性验证，必须结合人工抽样审查和源文档核对。
completion_criteria:
- 完成 100 条目以上的问答评估集构建
- 提交数据集质量分析及人工审查记录
- 实现用于RAG流水线性能评估的Notebook并编写结果报告
- 在CI/CD环境中配置可重执行形式的评估包
source_ids:
- S5
---

## 构建用于RAG评估的问答(QA)评估集

为了可靠地衡量检索增强生成(RAG)系统的性能，精心设计的评估集是必不可少的。仅仅依赖人工编写的问题和答案在进行大规模评估时，在成本和可扩展性方面存在局限性。

### 合成数据生成的意义
根据最新的TrueTeacher方法论，可以利用大语言模型(LLM)对模型生成的各种答案进行注释，从而生成合成训练数据 [S5]。该方法具有以下优点：
1. **成本效益**：不依赖人工直接编写的摘要或答案，因此能够生成大规模数据集（例如：1.4M个示例） [S5]。
2. **多语言与可扩展性**：不局限于特定语言，并且在领域迁移(Domain-shift)方面也表现出稳健性 [S5]。
3. **事实一致性评估**：通过合成数据训练的小型模型，可以成功提炼(Distillation)大型LLM教师模型的知识，并作为高效的事实性评估工具使用 [S5]。

### 数据集构建策略
在构建评估集时，不仅要创建问答对，还必须进行结构化设计，以便衡量“检索结果是否包含得出正确答案所需的依据？”以及“模型是否在没有扭曲的情况下引用了相关依据？”。为此，在生成数据集时，需要对问题的复杂度、与检索结果的相关性以及答案的事实一致性进行系统的标注或验证。
