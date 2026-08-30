---
layout: learn-module
title: Understanding RAG Architecture
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-en
course_locale: en
lang: en
ref: learn:rag-evaluation-reliability:intro-rag-architecture
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/intro-rag-architecture/
- lang: en
  url: /learn/en/rag-evaluation-reliability/intro-rag-architecture/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/intro-rag-architecture/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/intro-rag-architecture/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/intro-rag-architecture/
module_id: m1
permalink: /learn/en/rag-evaluation-reliability/intro-rag-architecture/
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
id: m1
slug: intro-rag-architecture
phase_id: p1
estimated_hours: 8.0
prerequisites: []
objectives:
- Understand the core components of the RAG (Retrieval-Augmented Generation) architecture.
- Identify the knowledge limitations of Large Language Models (LLMs) and the necessity
  of retrieval-based augmentation.
- Explain the structural flow of the retrieval-generation pipeline.
worked_examples:
- 'Case 1: Traditional LLM approach - When asked ''Tell me today''s news'', there
  is a risk of generating incorrect information because it is unaware of events after
  the training data cutoff.'
- 'Case 2: RAG approach - When asked ''Tell me today''s news'', 1) the Retriever collects
  relevant articles through an external search engine or real-time news API, and 2)
  generates an accurate, up-to-date response by including these as context and passing
  them to the LLM.'
lab:
  title: RAG Architecture Flow Visualization and Analysis
  steps:
  - Open Jupyter Notebook and diagram the structure of the RAG base pipeline's 3 stages
    (input, retrieval, generation).
  - Extract 5 short texts from an open-license document corpus to create a dataset
    sample.
  - Implement a simple keyword-matching Retriever function to return documents matching
    the question.
  - Write code for the augmentation stage that injects the retrieved documents into
    a prompt template.
  safety:
  - Never use actual personal information or confidential documents as corpus data.
  - Check the Rate Limit when using APIs and set a seed value in the test code to
    ensure reproducibility.
  deliverables:
  - RAG architecture diagram (included within a Notebook cell)
  - Simple keyword-based retriever implementation code
  - Document-injected prompt generation output
assignment:
  title: RAG-based Information Retrieval Pipeline Analysis Report
  deliverables:
  - Notebook explaining the working principles of the implemented RAG pipeline
  - Describe 3 potential failure cases that can occur when the retriever judges document
    relevance
  rubric:
  - Are the 3 stages of RAG (retrieval, augmentation, generation) explained and distinguished
    accurately?
  - Is the analysis of the possibility of retrieving irrelevant documents during the
    retrieval stage valid?
  - Was the implementation done in compliance with private data security guidelines?
quiz:
- question: What is the main advantage of RAG compared to LLM training methods?
  choices:
  - It can reduce the parameter size of the LLM.
  - It can keep the model's knowledge up-to-date and provide evidence.
  - It accelerates the model's training speed.
  - It generates 100% factual answers to all questions.
  answer_index: 1
  explanation: Because RAG references external documents, it can reflect the latest
    information and offers high reliability as the evidence for generated answers
    can be found in the documents.
- question: What is the correct role of the Retriever?
  choices:
  - It plays the role of generating answers.
  - It plays the role of retraining the training data.
  - It searches for external document chunks related to the question.
  - It manages the user interface.
  answer_index: 2
  explanation: The retriever plays the role of finding documents that are semantically
    similar or highly relevant to the user's question from external data sources.
completion_criteria:
- Can explain the components of the RAG architecture.
- Confirm that the practiced RAG pipeline code works properly to retrieve and augment
  relevant documents.
- Describe the limitations of the RAG pipeline and directions for improvement in an
  analysis report.
source_ids:
- S1
- S2
---

## RAG (Retrieval-Augmented Generation) Architecture Overview

While state-of-the-art Natural Language Processing (NLP) and deep learning models show excellent performance by learning from vast amounts of text data, they have limitations such as exhibiting hallucinations or lacking knowledge regarding the latest information not included at the time of model training, or private data within specific domains [S1].

### Overcoming LLM Limitations through Retrieval
RAG is a method that, instead of forcing the model to memorize all knowledge within its parameters, retrieves reliable external documents related to the question at the 'just-in-time' moment and provides them as input for the generation stage [S2].

### Core Components
1. **Retriever**: Receives the user's query and identifies highly relevant document chunks from sources such as vector databases.
2. **Augmentation**: Combines the retrieved documents with the original question to construct the prompt to be delivered to the LLM.
3. **Generator**: Generates a fact-based response based on the augmented information.

This structure contributes to securing reliability by keeping the model's knowledge up-to-date and making the generated answers' evidence traceable.
