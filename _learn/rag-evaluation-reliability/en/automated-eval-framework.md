---
layout: learn-module
title: Applying Automated Evaluation Framework (Ragas)
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-en
course_locale: en
lang: en
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
permalink: /learn/en/rag-evaluation-reliability/automated-eval-framework/
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
id: m7
slug: automated-eval-framework
phase_id: p2
estimated_hours: 10.0
prerequisites:
- m6
objectives:
- Understand the core evaluation dimensions (retrieval and generation quality) of
  a RAG pipeline.
- Learn how to automatically evaluate RAG performance without references (reference-free)
  using the Ragas framework.
- Analyze and mitigate hallucination risks through quantitative metrics.
worked_examples:
- 'Case 1: Context Relevance calculation. Ragas uses an LLM to extract sentences actually
  needed to answer the question from the retrieved context, and calculates the score
  through the ratio of needed sentences to the total context.'
- 'Case 2: Faithfulness evaluation. An LLM determines whether each claim in the generated
  response is supported by the retrieved context. The more unsupported claims there
  are, the higher the hallucination score becomes.'
lab:
  title: Practice Quantitatively Evaluating RAG Performance using Ragas
  steps:
  - Prepare an evaluation dataset (question, retrieved context, generated response).
  - Install the `ragas` library in a Python environment.
  - Convert the evaluation dataset into a `ragas` Dataset object.
  - Call Ragas' `evaluate` function to calculate metrics such as Context Relevance
    and Faithfulness.
  - Visualize the result values and analyze queries with low scores.
  safety:
  - Ensure that personal information or private data is not included in the document
    corpus used for evaluation.
  - Actively utilize local models or caching during testing to prevent API usage costs.
  - Automated evaluation results are supplementary indicators of reliability; cross-validate
    the confirmation of actual model quality in parallel with sample human review.
  deliverables:
  - Evaluation result dataframe containing metric scores
  - Logs analyzing query types that received low scores
assignment:
  title: RAG Pipeline Performance Comparison Report
  deliverables:
  - Ragas evaluation results for two RAG pipelines with different search settings
    (k-value, embedding model, etc.)
  - Performance analysis report between the two settings
  rubric:
  - Were Ragas metrics (Context Relevance, Faithfulness, etc.) implemented correctly?
  - Are evaluation results quantitatively compared and interpreted logically?
  - Were hallucination types classified for at least 3 cases and were improvement
    plans suggested?
quiz:
- question: What is the biggest characteristic of the Ragas framework?
  choices:
  - A human answer dataset is absolutely required
  - It can evaluate RAG pipelines without references (reference-free)
  - It only evaluates the search stage and does not evaluate the generation stage
  - At least 10 GPU(s) are absolutely required
  answer_index: 1
  explanation: Ragas is a framework that automatically evaluates search and generation
    quality using LLMs without an answer dataset [S3, S4].
- question: What is the definition of the 'Faithfulness' metric measured by Ragas?
  choices:
  - How relevant retrieved context is to the question
  - Whether the question exists within the document corpus
  - Whether the generated response is based on retrieved context
  - How much the questioner trusts the LLM's response
  answer_index: 2
  explanation: Faithfulness is a metric that measures how faithfully a generated response
    is based on the provided retrieved context (hallucination prevention) [S4].
completion_criteria:
- Successfully calculate at least 4 metrics for at least 10 queries using the Ragas
  library.
- The lab notebook is regularly committed to the Git repository.
- The performance comparison report includes at least 3 error classification cases.
source_ids:
- S3
- S4
---

## Challenges of RAG Evaluation and Ragas

RAG systems consist of a retrieval module and an LLM-based generation module [S3, S4]. Evaluating this structure is a challenging task because it must consider how well the retrieval system identifies relevant context, how faithfully the LLM utilizes the provided context, and what the quality of the response is [S4].

Traditional evaluation methods relied on manual creation and comparison of ground truth, but this is costly and time-consuming, making it unsuitable for fast iteration cycles [S3, S4].

### Ragas Framework
Ragas (Retrieval Augmented Generation Assessment) is a framework that can evaluate RAG pipelines even without ground truth datasets [S3, S4]. Ragas automatically evaluates the following core dimensions:

1. **Retrieval Quality:** Measures how relevant the retrieved context is to the question (Context Relevance) and whether it contains all necessary information (Context Recall).
2. **Generation Quality:** Measures whether the generated response is based on the retrieved context (Faithfulness) and how relevant it is to the question (Answer Relevance).

These metrics utilize LLMs as 'judges' to enable evaluation without references, contributing to shortening the RAG development cycle [S3, S4].
