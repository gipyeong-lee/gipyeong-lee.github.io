---
layout: learn-module
title: Faithfulness Evaluation
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-en
course_locale: en
lang: en
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
permalink: /learn/en/rag-evaluation-reliability/generation-faithfulness/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: f439c689d3754cecbf386ffcc0c2bd7c
translation_run_id: e0a3616353a24989a829f247010ab342
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
- Understand the concept of Faithfulness and identify its importance in RAG systems.
- Quantitatively evaluate whether generated answers are based on the retrieved context
  using the Ragas framework.
- Analyze the risk of hallucination using automated evaluation metrics.
worked_examples:
- 'Example 1: If there is context ''Apples are rich in Vitamin C'' and answer ''Apples
  are rich in Vitamin C, so they are good for immunity'', ''good for immunity'' is
  information not in the context, so the faithfulness score decreases.'
- 'Example 2: If context ''The foundation date of our company is 2020 year 5 month
  1 day'' and answer ''The company was founded in 2020 year 5 month'' match information,
  it has a high faithfulness score.'
lab:
  title: Measuring Generated Answer Faithfulness using Ragas
  steps:
  - Prepare an evaluation dataset (questions, retrieved context, generated answers).
  - Install the Ragas library and import the `Faithfulness` metric.
  - Convert the prepared dataset into Ragas's data structure.
  - Construct an LLM-based evaluator to calculate the faithfulness score of the dataset.
  - Sample answers with low scores and analyze the differences with the retrieved
    context through human review.
  safety:
  - Do not send datasets containing private documents or personal information to external
    LLM APIs.
  - Check API request rate limits and use caching to control costs.
  - Maintain security of sample data during human review.
  deliverables:
  - Report on the average faithfulness scores of the entire dataset
  - Dataset analyzing responses with low scores
  - Comparative analysis between automated evaluation results and human review results
assignment:
  title: RAG Pipeline Reliability Evaluation Report
  deliverables:
  - Jupyter Notebook including faithfulness evaluation
  - Report analyzing error classification and frequency of hallucinations
  rubric:
  - Has the faithfulness metric been implemented correctly?
  - Were hallucination cases in generated responses classified accurately?
  - Has qualitative consistency between automated evaluation results and human review
    been secured?
quiz:
- question: What is faithfulness in a RAG system?
  choices:
  - The degree to which retrieved context is highly relevant to the question
  - The degree to which generated responses are based on the information in the retrieved
    context
  - The degree to which an LLM utilizes its pre-trained knowledge
  - The degree to which the response accurately matches the user's question
  answer_index: 1
  explanation: Faithfulness is a metric that evaluates whether a generated response
    relies on facts from externally retrieved context.
- question: Which of the following is a correct characteristic of the Ragas framework?
  choices:
  - Evaluation is only possible if human annotations (ground truth) are provided.
  - It supports reference-free evaluation methods.
  - It only evaluates search efficiency and does not evaluate generation quality.
  - It does not use LLMs as evaluators and only uses statistical methods.
  answer_index: 1
  explanation: Ragas aims for a framework that can evaluate without references and
    actively utilizes LLMs as evaluators [S3, S4].
completion_criteria:
- Can quantitatively measure the faithfulness of generated responses using the Ragas
  library.
- Can classify at least 3 types of hallucination occurrence patterns from evaluation
  results.
- Can verify the consistency between the automated evaluation pipeline results and
  actual responses.
source_ids:
- S3
- S4
---

## Faithfulness Evaluation

The core of a Retrieval-Augmented Generation (RAG) system is that an LLM generates answers by utilizing information retrieved from an external knowledge database. Faithfulness is a metric indicating whether the generated answer faithfully reflects only the information described in the retrieved context [S3].

### 1. Why evaluate Faithfulness?
LLMs tend to answer based on pre-trained knowledge, which can lead to generating information irrelevant to the retrieved context or distorting the context. This is called 'hallucination', and faithfulness evaluation can measure this quantitatively [S4].

### 2. Evaluation Framework: Ragas
Ragas proposes a framework where evaluation is possible without references (reference-free) even when user annotations are absent [S3]. The faithfulness evaluation process generally follows these steps:
- **Statement Extraction from Answer**: Separate verifiable factual statements from the answer.
- **Evidence Retrieval**: Confirm which part of the retrieved context each statement was derived from.
- **Verification**: Judge whether the extracted statements match the context information.

Ragas automates this process by using an LLM as the evaluator [S4].
