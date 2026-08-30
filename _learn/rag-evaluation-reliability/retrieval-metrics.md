---
layout: learn-module
title: 검색 품질 지표(Recall@k, MRR, nDCG)
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability
course_locale: ko
lang: ko
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
permalink: /learn/rag-evaluation-reliability/retrieval-metrics/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: f439c689d3754cecbf386ffcc0c2bd7c
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
- 검색 증강 생성(RAG) 파이프라인에서 검색 단계의 중요성을 이해한다.
- Recall@k, MRR, nDCG 지표의 개념과 RAG 시스템 평가에서의 의미를 학습한다.
- 검색된 컨텍스트의 관련성이 이후 답변 생성 품질에 미치는 영향을 분석한다.
worked_examples:
- '질문에 대해 시스템이 [DocB, DocA, DocC] 순서로 반환했고, 정답 관련 문서가 DocA라면? MRR 계산: DocA는 2번째이므로
  Reciprocal Rank는 1/2 = 0.5이다.'
- k=3일 때 상위 3개 검색 결과에 정답 문서가 포함되어 있다면 Recall@3 = 1, 포함되어 있지 않다면 Recall@3 = 0이다.
lab:
  title: 검색 품질 지표 정량 측정 실습
  steps:
  - 평가셋(질문, 정답 문서)을 사용하여 50개 샘플 데이터 준비하기.
  - 검색 모듈을 실행하여 각 질문에 대한 상위 k(k=3, 5, 10)개의 문서 반환받기.
  - Recall@k, MRR, nDCG 함수를 Python으로 직접 구현하거나 라이브러리를 사용하여 계산하기.
  - 질문별 지표 결과를 데이터프레임으로 정리하여 시각화하기.
  safety:
  - 개인정보나 비공개 문서가 포함된 데이터셋을 외부 API에 전송하지 않는다.
  - 실험 시 API 비용 제한을 설정하고 캐시를 활용하여 요청 수를 최적화한다.
  deliverables:
  - 각 질문별 Recall@k, MRR, nDCG 값이 포함된 결과 데이터프레임 CSV
  - 지표 분포를 보여주는 히스토그램 및 박스플롯 이미지
assignment:
  title: 검색기(Retriever) 성능 비교 리포트
  deliverables:
  - '두 가지 검색 설정(예: Sparse vs Dense Retrieval)을 적용한 평가 결과 보고서'
  - 성능이 낮은 상위 5개 질문에 대한 원인 분석(오검색 유형 분류)
  rubric:
  - Recall@k, MRR, nDCG 지표를 정확하게 계산하였는가?
  - 검색 성능 차이를 통계적으로 유의미하게 해석하였는가?
  - 실패 유형을 체계적으로 분류하였는가?
quiz:
- question: RAG 시스템에서 검색 단계의 품질이 생성 단계에 미치는 영향은 무엇인가?
  choices:
  - 검색 품질은 생성 품질과 무관하다.
  - 관련성 낮은 컨텍스트는 LLM의 환각을 유발할 위험을 높인다.
  - 검색 단계는 LLM의 추론 능력만을 평가한다.
  - 검색 결과가 많을수록 항상 생성 품질이 좋아진다.
  answer_index: 1
  explanation: 검색 단계에서 관련성 없는 정보가 전달되면 LLM은 이를 기반으로 잘못된 답변을 생성하거나 환각을 일으킬 수 있다 [S3].
- question: MRR 지표가 가장 높을 때는 언제인가?
  choices:
  - 관련 문서가 항상 마지막에 나올 때
  - 관련 문서가 항상 가장 상단(1위)에 위치할 때
  - 검색 결과가 전혀 없을 때
  - 관련 문서가 항상 중간에 나올 때
  answer_index: 1
  explanation: MRR은 정답 문서의 순위 역수의 평균이므로, 1위에 위치할 때 값이 최대(1)가 된다.
completion_criteria:
- Recall@k, MRR, nDCG 계산 코드를 완성하고 샘플 데이터에 적용하였다.
- 두 가지 검색 전략을 비교하여 정량적 분석 결과를 도출하였다.
- 검색 실패 유형을 최소 3가지 이상 분류하고 보고서에 기재하였다.
source_ids:
- S3
- S4
---

### RAG 검색 품질 평가의 중요성

RAG 시스템은 외부 데이터베이스에서 관련 정보를 검색하고, 이를 LLM에 전달하여 답변을 생성한다 [S3]. 따라서 검색 단계에서 관련성 높고 집중된 컨텍스트를 식별하지 못하면, 아무리 강력한 LLM이라도 정확한 답변을 생성하기 어렵다 [S3]. 검색 품질을 평가하는 것은 RAG 아키텍처의 전체 성능을 개선하는 첫걸음이다.

### 주요 검색 평가 지표

1. **Recall@k (재현율)**: 검색된 상위 k개의 결과에 실제 정답이 포함되어 있는지 측정한다. 즉, 필요한 정보가 검색 시스템에 의해 포착되었는지 확인하는 지표이다.
2. **MRR (Mean Reciprocal Rank)**: 사용자의 질문에 대한 정답(관련 문서)이 검색 결과 리스트의 몇 번째 위치에 있는지를 측정한다. 가장 첫 번째 위치에 관련 문서가 등장할수록 MRR 값은 1에 가까워지며 높은 점수를 갖는다.
3. **nDCG (normalized Discounted Cumulative Gain)**: 검색 결과의 순서를 고려하는 지표로, 관련성 높은 문서가 상단에 위치할수록 높은 점수를 부여한다. 단순 포함 여부(Recall)보다 검색 결과의 '순위 정확도'를 더 정밀하게 평가한다.

이러한 지표들은 참조 데이터(Ground Truth)가 있는 경우 시스템 개선을 위해 필수적이며, Ragas와 같은 프레임워크는 이러한 차원을 정량적으로 분석할 수 있는 도구를 제공한다 [S3, S4].
