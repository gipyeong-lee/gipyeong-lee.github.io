---
layout: learn-module
title: 样本人工审核与对照
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:rag-evaluation-reliability:human-review-validation
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/human-review-validation/
- lang: en
  url: /learn/en/rag-evaluation-reliability/human-review-validation/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/human-review-validation/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/human-review-validation/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/human-review-validation/
module_id: m9
permalink: /learn/zh-cn/rag-evaluation-reliability/human-review-validation/
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
id: m9
slug: human-review-validation
phase_id: p3
estimated_hours: 10.0
prerequisites:
- m8
objectives:
- 理解自动化 RAG 评估指标与实际事实性之间的差距。
- 设计人工审核模型生成回答的事实一致性（Factual Consistency）的协议。
- 识别 LLM 评估的局限性，并分析 TrueTeacher 等合成数据技术的意义 [S5]。
- 掌握系统化分类错误类型及管理可信度数据集的方法。
worked_examples:
- 示例 1：自动化评估指标（如 Faithfulness）得分很高，达到 0.9，但人工审核发现回答中包含了检索文档中不存在的内容。分析：将其归类为模型使用了非检索信息（即内部权重中包含的过去信息）产生的幻觉，并记录在系统错误日志中。
- 示例 2：设计使用 TrueTeacher 模型使系统自行评估回答的事实性。人工抽样调查 LLM 评为“正确”的部分回答，以衡量 LLM 评估器的错误率（误报率，False
  Positive），并将其在评估报告中注明 [S5]。
lab:
  title: 样本人工审核与错误分析执行
  steps:
  - 通过自动化评估流水线（Ragas 等）导出 100 个回答的忠实度（Faithfulness）得分。
  - 随机抽取得分最低的 10 个、中等水平的 10 个及得分最高的 10 个样本，建立审核集。
  - 通过对照回答、检索文档（Context）和标准答案（Ground Truth），人工记录是否存在“检索遗漏”、“信息失真”、“幻觉生成”。
  - 对比记录的人工判断与自动化评估得分，执行相关性分析。
  safety:
  - 务必确认待审核的数据集中不包含实际个人信息或敏感的非公开文档。
  - 审核完成的数据安全保存在本地存储中，严禁上传至未经验证的外部 API。
  deliverables:
  - 包含至少 30 条人工审核记录的错误分类表（CSV/Excel）
  - 分析自动化指标与人工评估一致性的总结报告
assignment:
  title: RAG 可信度分析报告撰写
  deliverables:
  - 通过人工审核分类出的故障类型频率表
  - 当前系统主要脆弱点（检索阶段或生成阶段）的分析报告
  - 改进未来自动化评估流水线的建议
  rubric:
  - 错误类型分类是否系统化？
  - 是否结合具体示例逻辑性地叙述了自动化评估指标的局限性？
  - 人工审核数据是否被恰当地用作可信度分析的依据？
quiz:
- question: 仅凭自动化事实性评估指标难以确定系统可靠性的主要原因是什么？
  choices:
  - 因为自动化评估指标速度非常快。
  - 因为模型生成数据具有与人工撰写数据不同的特征，且自动评估器本身无法捕捉所有事实错误 [S5]。
  - 因为人工审核数据总是比自动化评估指标准确。
  - 因为数据集规模太小。
  answer_index: 1
  explanation: 现有的摘要评估数据集无法充分反映模型实际生成结果的复杂性，且自动评估系统在某些情况下无法检测出幻觉。
- question: TrueTeacher 方法与利用现有摘要数据集的方法有何不同？
  choices:
  - 仅依赖于人工编写的摘要。
  - 利用模型生成的各种摘要，合成生成用于事实性评估的数据 [S5]。
  - 不使用 NLI 模型。
  - 不支持多语言。
  answer_index: 1
  explanation: TrueTeacher 不依赖于人工编写的摘要，而是利用 LLM 对模型生成的各种数据进行合成标注，从而生成训练数据 [S5]。
completion_criteria:
- 需编写至少 30 个数据样本的人工审核日志。
- 需提交包含自动化评估结果与人工审核结果比较分析的报告。
- 需通过错误分类明确定义当前系统的脆弱点。
source_ids:
- S5
---

## 自动化评估的局限性与人工审核的必要性

在评估检索增强生成（RAG）系统的质量时，Ragas 等工具虽然能快速提供定量指标，但在捕捉模型生成回答的微妙事实错误方面存在局限。特别是在复杂的语境下，很难区分 LLM 是在知识范围内进行推理，还是依赖于学习过的数据产生了幻觉（Hallucination）。

### 事实一致性评估

最近的研究利用自然语言推理（NLI）模型或大语言模型（LLM）来评估摘要或回答的事实性。然而，现有方法依赖于人工编写的摘要数据集，这可能与实际模型生成的输出特性存在差异 [S5]。TrueTeacher 等方法试图通过利用 LLM 从模型生成数据中构建合成的事实性评估数据，来克服这些局限性 [S5]。

### 人工审核（Human-in-the-Loop）的作用

无论自动化评估流水线多么先进，最终的可靠性验证仍离不开人工审核。人工审核的作用如下：
1. **验证自动化评估指标：** 识别某些回答虽被评估为“相关”但实际上并非事实的情况。
2. **幻觉类型分类：** 诊断系统结构性缺陷（检索错误 vs. 生成模型错误）。
3. **校准回归测试集：** 基于人工审核的数据持续提升评估集的质量。
