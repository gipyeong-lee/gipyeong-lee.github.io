---
layout: learn-module
title: 检索质量指标 (Recall, MRR, nDCG)
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:rag-evaluation-reliability:retrieval-metrics
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/retrieval-metrics/
- lang: en
  url: /learn/en/rag-evaluation-reliability/retrieval-metrics/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/retrieval-metrics/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/retrieval-metrics/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/retrieval-metrics/
module_id: m4
permalink: /learn/zh-cn/rag-evaluation-reliability/retrieval-metrics/
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
id: m4
slug: retrieval-metrics
phase_id: p2
estimated_hours: 8.0
prerequisites:
- m3
objectives:
- 了解检索增强生成(RAG)流水线中检索阶段的重要性。
- 学习Recall, MRR, nDCG指标的概念及其在RAG系统评估中的意义。
- 分析检索到的上下文相关性对后续答案生成质量的影响。
worked_examples:
- 若系统对问题的返回顺序为 [DocB, DocA, DocC]，且正确答案相关文档为DocA？MRR计算：DocA是第 2 个，因此倒数排名(Reciprocal
  Rank)为 1/2 = 0.5。
- 当k= 3 时，如果前 3 个检索结果中包含正确文档，则 Recall @ 3 = 1；如果不包含，则 Recall @ 3 = 0。
lab:
  title: 检索质量指标定量测量实践
  steps:
  - 使用评估集（问题、正确答案文档）准备 50 个样本数据。
  - 执行检索模块，为每个问题返回前k个文档（k= 3, 5, 10）。
  - 使用Python直接实现或使用库来计算 Recall, MRR, nDCG 指标。
  - 将各问题的指标结果整理为数据帧(DataFrame)并进行可视化。
  safety:
  - 不要将包含个人隐私或私密文档的数据集发送给外部API。
  - 实验时设置API费用限制，并利用缓存来优化请求次数。
  deliverables:
  - 包含各问题 Recall, MRR, nDCG 值的结果数据帧 CSV 文件
  - 显示指标分布的直方图及箱线图图像
assignment:
  title: 检索器(Retriever)性能对比报告
  deliverables:
  - 应用两种检索设置（例如：稀疏检索 vs 稠密检索）后的评估结果报告
  - 对性能较差的前 5 个问题进行原因分析（错误检索类型分类）
  rubric:
  - 是否准确计算了 Recall, MRR, nDCG 指标？
  - 是否对检索性能差异进行了统计学上有意义的解释？
  - 是否系统地分类了失败类型？
quiz:
- question: 在RAG系统中，检索阶段的质量对生成阶段有什么影响？
  choices:
  - 检索质量与生成质量无关。
  - 不相关的上下文会增加LLM产生幻觉的风险。
  - 检索阶段仅评估LLM的推理能力。
  - 检索结果越多，生成质量就越好。
  answer_index: 1
  explanation: 如果在检索阶段传递了不相关的信息，LLM可能会基于这些信息生成错误的答案或产生幻觉 [S3]。
- question: MRR指标最高的情况是什么？
  choices:
  - 相关文档总是排在最后。
  - 相关文档总是位于最顶端（第 1 位）。
  - 根本没有检索结果。
  - 相关文档总是排在中间。
  answer_index: 1
  explanation: MRR是正确文档排名倒数的平均值，因此位于第 1 位时，其值达到最大( 1 )。
completion_criteria:
- 完成了 Recall, MRR, nDCG 计算代码并应用于样本数据。
- 对比两种检索策略并得出了定量分析结果。
- 至少将检索失败类型分类为 3 种以上并记录在报告中。
source_ids:
- S3
- S4
---

### RAG检索质量评估的重要性

RAG系统通过从外部数据库检索相关信息，并将其传递给LLM来生成答案 [S3]。因此，如果在检索阶段无法识别出相关性高且集中的上下文，即使是再强大的LLM也难以生成准确的答案 [S3]。评估检索质量是改善RAG架构整体性能的第一步。

### 主要检索评估指标

1. **Recall (召回率)**：衡量实际正确答案是否包含在检索到的前k个结果中。即确认所需信息是否被检索系统捕捉到的指标。
2. **MRR (平均倒数排名)**：衡量用户问题的正确答案（相关文档）位于检索结果列表中的第几个位置。相关文档出现的位置越靠前，MRR值越接近 1，得分越高。
3. **nDCG (归一化折损累计增益)**：考虑检索结果顺序的指标，相关性高的文档位于顶部时赋予更高的分数。比起单纯的包含与否(Recall)，它能更精确地评估检索结果的“排序准确性”。

在有参考数据(Ground Truth)的情况下，这些指标对于系统改进至关重要，而像Ragas这样的框架提供了可以定量分析这些维度的工具 [S3, S4]。
