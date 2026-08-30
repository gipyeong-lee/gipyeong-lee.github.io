---
layout: learn-module
title: Citation Accuracy and Source Tracking
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-en
course_locale: en
lang: en
ref: learn:rag-evaluation-reliability:citation-accuracy
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/citation-accuracy/
- lang: en
  url: /learn/en/rag-evaluation-reliability/citation-accuracy/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/citation-accuracy/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/citation-accuracy/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/citation-accuracy/
module_id: m6
permalink: /learn/en/rag-evaluation-reliability/citation-accuracy/
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
id: m6
slug: citation-accuracy
phase_id: p2
estimated_hours: 8.0
prerequisites:
- m5
objectives:
- Understand how faithfully a response reflects the content of retrieved documents
  in a RAG system.
- Learn the definition and measurement methods of citation accuracy.
- Quantitatively evaluate the faithfulness and answer relevance of responses using
  the Ragas framework.
- Design a process to verify the traceability of sources in model responses.
worked_examples:
- 'Example 1: Faithfulness score calculation. If the question ''What is A''s revenue
  in 2025?'' generates the response ''A''s revenue in 2025 was 100 billion.'', and
  the context document includes ''A recorded 100 billion in revenue in 2025.'', since
  all information in the response exists within the context, the faithfulness score
  is evaluated as 1.0 (maximum).'
- 'Example 2: Citation accuracy error identification. If the question ''When was A
  founded?'' generates the response ''A was founded in 1990 (Reference: Document 1).'',
  but Document 1 specifies ''A was founded in 1995'', this is classified as a ''Fact
  Distortion'' failure type and is judged as having low citation accuracy.'
lab:
  title: Automated Response Faithfulness Evaluation Practice using Ragas
  steps:
  - Prepare a dataset of search results (Context) and generated responses (Answer)
    for the RAG system to be evaluated.
  - Install the Ragas framework and load the response dataset.
  - Calculate scores for each question-answer pair in the dataset using Ragas' `Faithfulness`
    metric.
  - Separately extract 30 responses with a faithfulness score of less than 0.7.
  - 'Human-review the extracted samples and tag them with corresponding failure types:
    ''Citation Omission'', ''False Citation'', or ''Fact Distortion''.'
  safety:
  - Ensure anonymization is completed in advance so that personal information or corporate
    secrets are not included in the document corpus used during the evaluation process.
  - Set cost limits when calling external APIs and fix seed values for reproducibility
    to prevent repetitive API costs.
  deliverables:
  - Jupyter Notebook file (.ipynb) containing evaluation results
  - Visualization chart of faithfulness score distribution
  - Failure type classification table including human review records
assignment:
  title: RAG System Reliability Regression Evaluation Report Writing
  deliverables:
  - Statistical comparison results of faithfulness based on two or more RAG settings
    (e.g., changing search Top-k values)
  - Human review contrast table for 30 samples
  - Proposal for improvement to enhance system citation accuracy
  rubric:
  - Is the quantitative calculation method for evaluation metrics accurately specified?
  - Is the citation relationship between retrieved documents and generated responses
    logically traceable?
  - Is the failure type classification consistent with human review data and does
    it provide valid evidence?
quiz:
- question: Which explanation is correct regarding the 'Faithfulness' metric in the
    Ragas framework?
  choices:
  - Evaluates whether the response is relevant to the question.
  - Measures whether all information in the response exists within the provided context
    document.
  - Evaluates how grammatically accurate the response is.
  - Measures whether the response includes all information from an external knowledge
    base.
  answer_index: 1
  explanation: Faithfulness is a metric that measures whether the claims in a generated
    response are based on retrieved context.
- question: Which case corresponds to the 'Fact Distortion' failure type when evaluating
    citation accuracy?
  choices:
  - Cases where content not in the retrieved document is included in the response
  - Cases where citation notation is omitted
  - Cases where the citation is correctly marked but the factual relationship of the
    original text is misinterpreted and described
  - Cases where the response is completely different from the intent of the question
  answer_index: 2
  explanation: Fact distortion refers to cases where, despite citing the source document,
    the information from the original text is summarized or transformed in an incorrect
    way.
completion_criteria:
- Completion of automated evaluation metric calculation via Jupyter Notebook
- Submission of human review and failure type classification records for at least
  30 response samples
- Writing a final report containing evaluation results and improvement plans
source_ids:
- S4
---

## RAG System Citation and Faithfulness Evaluation

RAG (Retrieval Augmented Generation) systems utilize external knowledge bases to reduce the risk of LLM hallucinations, but a process to verify whether generated responses accurately cite retrieved documents is essential [S4].

### 1. Key Evaluation Metrics
* **Faithfulness:** Measures whether generated responses are derived from the provided retrieved context. Every claim in the response must be based on retrieved documents; scores are lower if responses rely solely on external knowledge or the model's pre-trained knowledge [S4].
* **Answer Relevance:** Evaluates how directly relevant the response is to the given question. This is used to identify cases where a response deviates from the intent of the question, even if retrieved information is sufficient.

### 2. Citation Accuracy Verification Process
Citation accuracy is the process of identifying which part of the retrieved context a specific sentence in the response cites and verifying if it aligns with facts in the original text. The automated evaluation framework, Ragas, provides metrics that can evaluate faithfulness even without reference data (ground truth) for this process [S4].

### 3. Failure Type Classification
- **Citation Omission:** Facts in the response are present in retrieved documents, but no citation is indicated.
- **False Citation:** Indicates as if it cited content not found in retrieved documents.
- **Fact Distortion:** Citations are correctly indicated, but generated by misinterpreting the meaning of the original text.
