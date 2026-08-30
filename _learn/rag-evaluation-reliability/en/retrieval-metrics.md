---
layout: learn-module
title: Search Quality Metrics (Recall @k, MRR, nDCG)
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability-en
course_locale: en
lang: en
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
permalink: /learn/en/rag-evaluation-reliability/retrieval-metrics/
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
id: m4
slug: retrieval-metrics
phase_id: p2
estimated_hours: 8.0
prerequisites:
- m3
objectives:
- Understand the importance of the retrieval step in a Retrieval-Augmented Generation
  (RAG) pipeline.
- Learn the concepts of Recall @k, MRR, nDCG metrics and their significance in RAG
  system evaluation.
- Analyze the impact of retrieved context relevance on subsequent answer generation
  quality.
worked_examples:
- 'If the system returned results in the order [DocB, DocA, DocC] for a query, and
  the relevant document is DocA? MRR calculation: Since DocA is at the 2 position,
  the Reciprocal Rank is 1/2 = 0.5.'
- When k=3, if the correct answer document is included in the top 3 search results,
  Recall @3 = 1, and if not included, Recall @3 = 0.
lab:
  title: Quantitative Measurement of Retrieval Quality Metrics
  steps:
  - Prepare 50 sample data using an evaluation set (questions, correct answer documents).
  - Run the retrieval module to receive the top k (k=3, 5, 10) documents for each
    question.
  - Implement the Recall @k, MRR, and nDCG functions directly in Python or use a library
    to calculate them.
  - Organize and visualize the metric results per question into a dataframe.
  safety:
  - Do not send datasets containing personal information or private documents to external
    APIs.
  - Set API cost limits during experiments and utilize caching to optimize the number
    of requests.
  deliverables:
  - A result dataframe CSV containing Recall @k, MRR, and nDCG values for each query.
  - Histogram and boxplot images showing metric distribution
assignment:
  title: Retriever Performance Comparison Report
  deliverables:
  - Evaluation result report applying two retrieval configurations (e.g., Sparse vs
    Dense Retrieval)
  - Cause analysis (mis-retrieval type classification) for the top 5 questions with
    poor performance
  rubric:
  - Were the Recall @k, MRR, and nDCG metrics calculated accurately?
  - Was the difference in retrieval performance interpreted in a statistically significant
    way?
  - Were failure types classified systematically?
quiz:
- question: What is the impact of retrieval step quality on the generation step in
    a RAG system?
  choices:
  - Retrieval quality is irrelevant to generation quality.
  - Context with low relevance increases the risk of LLM hallucinations.
  - The retrieval step evaluates only the LLM's reasoning ability.
  - Generation quality always improves as search results increase.
  answer_index: 1
  explanation: If irrelevant information is passed in the retrieval step, the LLM
    may generate incorrect answers or trigger hallucinations based on it [S3].
- question: When is the MRR metric highest?
  choices:
  - When the relevant document always appears last.
  - When the relevant document is always at the very top (1 position)
  - When there are no search results at all.
  - When the relevant document always appears in the middle.
  answer_index: 1
  explanation: Since MRR is the mean of the reciprocal ranks of the relevant documents,
    the value is at its maximum (1) when it is located at the 1 position.
completion_criteria:
- Completed the Recall @k, MRR, and nDCG calculation code and applied it to sample
  data.
- Derived quantitative analysis results by comparing two retrieval strategies.
- Classified retrieval failure types into at least 3 categories and included them
  in the report.
source_ids:
- S3
- S4
---

### The Importance of RAG Search Quality Evaluation

RAG systems retrieve relevant information from external databases and pass it to an LLM to generate answers [S3]. Therefore, if the search stage fails to identify highly relevant and focused context, even a powerful LLM will struggle to generate accurate answers [S3]. Evaluating search quality is the first step toward improving the overall performance of the RAG architecture.

### Key Search Evaluation Metrics

1. **Recall @k**: Measures whether the actual correct answer is included in the top k retrieved results. In other words, it is a metric to confirm whether the necessary information was captured by the search system.
2. **MRR (Mean Reciprocal Rank)**: Measures the position of the correct answer (relevant document) for a user query within the search result list. The more the relevant document appears in the first position, the closer the MRR value is to 1, resulting in a higher score.
3. **nDCG (normalized Discounted Cumulative Gain)**: A metric that considers the ranking of search results; it assigns higher scores as more relevant documents are positioned toward the top. It evaluates the 'ranking accuracy' of search results more precisely than simple inclusion (Recall).

These metrics are essential for system improvement when ground truth is available, and frameworks like Ragas provide tools to quantitatively analyze these dimensions [S3, S4].
