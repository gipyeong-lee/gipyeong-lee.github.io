---
layout: learn-module
title: Evaluation Document Corpus Curation
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-en
course_locale: en
lang: en
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
permalink: /learn/en/rag-evaluation-reliability/corpus-curation/
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
id: m2
slug: corpus-curation
phase_id: p1
estimated_hours: 8.0
prerequisites:
- m1
objectives:
- Understand the importance of a fixed document corpus for RAG evaluation.
- Learn the quality determination factors (accuracy, diversity, de-duplication) for
  evaluation document data.
- Master strategies for building Document-Question-Answer pair (QA Pair) datasets
  for quantitative evaluation.
- Learn training/evaluation split methods to prevent data leakage.
worked_examples:
- 'Example 1: Document Chunking strategy. How to write Python scripts that divide
  text into fixed sizes, such as by paragraph or semantic unit, so context is not
  broken.'
- 'Example 2: Question-Answer data construction. Example of generating a JSON object
  in the format { ''question'': ''...'', ''ground_truth'': ''...'', ''context_chunk_id'':
  ''...'' }.'
lab:
  title: Evaluation Corpus Construction Practice
  steps:
  - Obtain open-license text files (.txt) in the domain to be evaluated.
  - Write a script using Python to read text files and divide them into chunk units.
  - Assign a unique identifier (ID) to each chunk and record metadata (title, source).
  - Generate questions from the created chunks and compose 50 QA pairs by recording
    the Chunk ID that serves as the evidence for the answer.
  - Divide and save the entire corpus into development and test sets in an 8:2 ratio.
  safety:
  - Do not include documents containing personal information in the evaluation corpus.
  - Control costs by setting request limits when using external APIs.
  - Manage versions of data generated during work via Git to ensure reproducibility.
  deliverables:
  - Constructed document corpus file (JSONL format)
  - QA dataset containing questions and answers (JSON format)
  - Jupyter Notebook file containing corpus split records
assignment:
  title: Domain-based RAG Dataset Completion
  deliverables:
  - QA dataset file with at least 100 questions
  - Dataset statistical analysis report (question length, chunk length, etc.)
  - Python code including the data splitting process
  rubric:
  - Completion of duplicate chunk removal in the corpus
  - Verification of data leakage between test and development sets
  - Accurate mapping of document segments (Chunk ID) serving as evidence for answers
quiz:
- question: What is the best way to prevent 'Data Leakage' in a RAG system?
  choices:
  - Generate the same questions for all documents.
  - Separate and manage the development set and the final evaluation test set.
  - Include the entire set of retrieval target documents in the training data.
  - Generate and manage the evaluation set anew each time.
  answer_index: 1
  explanation: If the evaluation set is exposed to retrieval target documents during
    the training (or development) process, fair evaluation is impossible, so the evaluation
    test set must be strictly separated.
- question: Why is 'de-duplication' important during the corpus curation process?
  choices:
  - To increase the LLM's generation speed
  - To save disk storage space
  - To ensure retrieval result diversity and prevent statistical bias
  - To lower the semantic similarity of documents
  answer_index: 2
  explanation: Duplicated information causes the search engine to return biased retrieval
    results for specific information and can distort quantitative evaluation metrics.
completion_criteria:
- Evaluation document corpus (at least 100 chunks) construction complete
- Verifiable QA dataset (at least 100 questions) generation complete
- Confirmation of adherence to dataset splitting policy
- Peer review or self-evaluation checklist completed for results
source_ids:
- S2
---

## Corpus Curation for RAG Evaluation

Large Language Models (LLMs) carry a risk of Hallucination when relying on knowledge within learned parameters. Retrieval-Augmented Generation (RAG) overcomes this limitation by allowing models to access external knowledge in real-time [S2]. A **Fixed Evaluation Corpus** that is controlled and stable is essential to quantitatively evaluate the reliability of an effective RAG system.

### 1. Corpus Quality Determination Factors
- **Factuality:** Information within documents must be up-to-date and factual. A corpus containing incorrect information leads to the generation of incorrect answers.
- **Domain Suitability:** It must include topics and vocabulary similar to the actual service environment being evaluated.
- **De-duplication:** If identical information is duplicated across multiple documents, it hinders retrieval result diversity and introduces bias into evaluation statistics.

### 2. Building QA Evaluation Datasets
Evaluation is impossible with only a document corpus. You must build 'Document-Question-Answer' pairs to measure whether the retriever brings in relevant documents and whether the generator provides accurate answers based on them.
- **Question Generation:** Automatically generate questions from documents using an LLM, or have them written directly by domain experts.
- **Answer Definition:** Clearly specify the document segment (Chunk) that serves as the evidence for the answer.

### 3. Data Splitting and Integrity
For evaluation set reliability, you must strictly split the data into a **Development Set** and a **Hold-out Test Set**. You must prevent 'data leakage', where questions in the evaluation set are directly exposed because they are contained in the retrieval target documents.
