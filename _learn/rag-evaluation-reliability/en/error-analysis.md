---
layout: learn-module
title: Failure Type Classification and Error Analysis
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-en
course_locale: en
lang: en
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
permalink: /learn/en/rag-evaluation-reliability/error-analysis/
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
id: m8
slug: error-analysis
phase_id: p3
estimated_hours: 10.0
prerequisites:
- m7
objectives:
- Able to identify and classify failure types occurring in RAG systems.
- Able to distinguish and analyze errors in the retrieval stage and the generation
  stage.
- Able to link automated evaluation and human review results by utilizing Ragas framework
  metrics.
- Able to derive RAG pipeline performance improvement plans based on error analysis
  data.
worked_examples:
- 'Example 1: When the retriever fetches a ''Model B specifications'' document for
  the question ''What is the release date of Model A?''. This is classified as a ''Retrieval
  Failure'', and embedding model adjustment or search query optimization can be the
  solution.'
- 'Example 2: When the retriever fetches the correct document for X for the question
  ''Explain X'', but the LLM answers with information not in the document. This is
  classified as a ''Generation Failure (lack of Faithfulness)'', and the constraint
  ''Use only the provided context'' should be reinforced through prompt engineering.'
lab:
  title: Failure Dataset Collection and Error Analysis
  steps:
  - Save the RAG system's answers and retrieved contexts for at least 50 questions.
  - Measure Context Precision and Faithfulness for each item using Ragas.
  - Extract the bottom 20% question-answer pairs with low metrics.
  - Create a classification table for the extracted samples as one of 'Retrieval Error',
    'Generation Error', or 'Logic Error'.
  safety:
  - Never include personal information or private data in evaluation code.
  - Monitor API call frequency and costs used during the evaluation process to comply
    with the budget.
  - Prevent information leakage by performing tasks in a local environment during
    data analysis.
  deliverables:
  - Error analysis CSV file with completed classification
  - Jupyter Notebook with visualized retrieval and generation quality metrics
assignment:
  title: Writing RAG Error Classification and Improvement Report
  deliverables:
  - 2-page report summarizing error analysis results
  - Proposal of response strategies per classified failure type (retrieval optimization
    or prompt improvement)
  rubric:
  - Accuracy and validity of failure type classification
  - Ability to analyze the correlation between quantitative metrics and human review
    results
  - Logical validity of improvement strategies
quiz:
- question: What is the failure that occurs when the retrieval module fetches irrelevant
    context in a RAG system?
  choices:
  - Generation failure
  - Retrieval failure
  - Database connection error
  - Authentication failure
  answer_index: 1
  explanation: Since the retrieval module plays the role of identifying documents
    suitable for the question, fetching irrelevant context is a failure in the retrieval
    stage [S3].
- question: What is the biggest feature of the Ragas framework?
  choices:
  - It necessarily requires large-scale human annotated data.
  - Reference-free evaluation is possible.
  - Only LLM generation quality evaluation is possible.
  - It is applicable only to real-time streaming systems.
  answer_index: 1
  explanation: Ragas is a reference-free evaluation framework that can evaluate retrieval
    and generation quality without ground truth [S3].
completion_criteria:
- Submission of error classification table including failure types
- Completion of quantitative analysis of retrieval and generation quality utilizing
  Ragas metrics
- Drafting and review of a pipeline improvement proposal based on error analysis
source_ids:
- S3
---

## Overview of RAG System Error Analysis

The Retrieval Augmented Generation (RAG) architecture consists of a retrieval module and an LLM-based generation module [S3]. When evaluating system performance, it is important to analyze these two stages separately. Errors are broadly divided into issues in the retrieval stage and issues in the generation stage.

### 1. Classification of Failure Types
- **Retrieval Failure:** The case where irrelevant or unfocused context is retrieved [S3].
- **Generation Failure:** The case where the LLM fails to faithfully utilize the provided context (Faithfulness) or generates answers irrelevant to the question [S3].

### 2. Complementing Automated Evaluation with Human Review
Reference-free frameworks such as Ragas enable the evaluation of retrieval and generation quality without human annotations (ground truth) [S3]. However, automated evaluation metrics alone find it difficult to capture all subtle hallucinations or complex logical errors in the system. Therefore, high-priority failure samples should be extracted via quantitative automated metrics, and actual causes must be identified by necessarily conducting a Human Review alongside them.
