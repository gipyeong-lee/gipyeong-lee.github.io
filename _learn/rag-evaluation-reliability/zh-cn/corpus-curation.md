---
layout: learn-module
title: 评估用文档语料库策展
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:rag-evaluation-reliability:corpus-curation
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/corpus-curation/
- lang: en
  url: /learn/en/rag-evaluation-reliability/corpus-curation/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/corpus-curation/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/corpus-curation/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/corpus-curation/
module_id: m2
permalink: /learn/zh-cn/rag-evaluation-reliability/corpus-curation/
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
id: m2
slug: corpus-curation
phase_id: p1
estimated_hours: 8.0
prerequisites:
- m1
objectives:
- 理解用于 RAG 评估的固定文档语料库的重要性。
- 学习评估用文档数据的质量决定因素（准确性、多样性、去重）。
- 掌握用于定量评估的“文档-问题-正解”对 (QA Pair) 数据集的构建策略。
- 学习防止数据泄露 (Data Leakage) 的训练/评估集划分方法。
worked_examples:
- '示例 1: 文档分块 (Chunking) 策略。编写 Python 脚本，在将文本划分为固定大小时，以段落或语义单位为基础进行划分，以避免上下文断裂。'
- '示例 2: 问题-回答数据构成。创建格式为 { ''question'': ''...'', ''ground_truth'': ''...'', ''context_chunk_id'':
  ''...'' } 的 JSON 对象示例。'
lab:
  title: 评估用语料库构建实操
  steps:
  - 获取用于评估的目标领域的开源授权文本文件 (.txt)。
  - 使用 Python 编写读取文本文件并以分块单位进行划分的脚本。
  - 为每个分块赋予唯一标识符 (ID) 并记录元数据（标题、来源）。
  - 在编写的分块中生成问题，并记录作为答案依据的分块 ID，从而构成 50 个 QA 对。
  - 将整个语料库以 8:2 的比例划分为开发集与测试集并保存。
  safety:
  - 评估语料库中不得包含个人信息文档。
  - 使用外部 API 时设置请求次数上限以控制成本。
  - 工作过程中生成的数据通过 Git 进行版本管理，以确保可重现性。
  deliverables:
  - 构建的文档语料库文件 (JSONL 格式)
  - 包含问题与正解的 QA 数据集 (JSON 格式)
  - 包含语料库划分记录的 Jupyter Notebook 文件
assignment:
  title: 完成基于领域的 RAG 数据集
  deliverables:
  - 至少包含 100 道题的 QA 数据集文件
  - 数据集统计分析报告（问题长度、分块长度等）
  - 包含数据划分过程的 Python 代码
  rubric:
  - 语料库内的重复分块是否已剔除
  - 是否确认测试集与开发集之间不存在数据泄露
  - 答案依据的文档区间 (Chunk ID) 是否映射准确
quiz:
- question: 在 RAG 系统中防止“数据泄露 (Data Leakage)”的最佳方法是什么？
  choices:
  - 针对所有文档生成相同的问题。
  - 将开发集与最终评估用的测试集分离管理。
  - 将整个检索目标文档包含在训练数据中。
  - 每次都重新生成并管理评估集。
  answer_index: 1
  explanation: 如果评估集在训练（或开发）过程中暴露在检索目标文档中，则无法进行公平评估，因此必须严格分离评估用测试集。
- question: 在语料库策展过程中，“去重”为何很重要？
  choices:
  - 为了提高 LLM 的生成速度。
  - 为了节省磁盘存储空间。
  - 为了确保检索结果的多样性并防止统计偏差。
  - 为了降低文档的语义相似度。
  answer_index: 2
  explanation: 重复的信息会使搜索引擎返回有偏向的检索结果，并可能扭曲定量评估指标。
completion_criteria:
- 完成评估用文档语料库（至少 100 个分块以上）的构建
- 完成可验证 QA 数据集（至少 100 道题）的生成
- 确认遵守数据集划分政策
- 完成针对结果物的同行评审或自我评估检查表编写
source_ids:
- S2
---

## 用于 RAG 评估的语料库策展

大语言模型 (LLM) 在依赖已学习参数内的知识时，存在幻觉 (Hallucination) 风险。检索增强生成 (RAG) 通过让模型实时访问外部知识来克服这一局限 [S2]。为了定量评估高效 RAG 系统的可靠性，必须拥有固定且可控的评估用文档语料库 (Fixed Evaluation Corpus)。

### 1. 语料库质量决定因素
- **准确性 (Factuality):** 文档内的信息必须是最新且属实的。包含错误信息的语料库会导致生成错误的回答。
- **领域契合度:** 必须包含与实际评估的服务环境相似的主题及词汇。
- **去重 (De-duplication):** 若相同信息在多个文档中重复，会阻碍检索结果的多样性，并对评估统计造成偏差。

### 2. QA 评估数据集构建
仅凭文档语料库无法进行评估。必须构建“文档-问题-正解”对，以测量检索器是否带来了相关文档，以及生成器是否基于此做出了准确回答。
- **问题生成:** 使用 LLM 自动从文档中生成问题，或由领域专家直接编写。
- **正解定义:** 必须明确注明作为答案依据的文档区间 (Chunk)。

### 3. 数据划分与完整性
为确保评估集的可靠性，必须严格划分**开发集 (Development Set)**与**最终评估集 (Hold-out Test Set)**。必须防止评估集中包含的问题直接包含在检索目标文档中并被暴露的“数据泄露”现象。
