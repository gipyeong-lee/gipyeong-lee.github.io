---
layout: learn-module
title: 실패 유형 분류 및 오류 분석
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability
course_locale: ko
lang: ko
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
permalink: /learn/rag-evaluation-reliability/error-analysis/
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
id: m8
slug: error-analysis
phase_id: p3
estimated_hours: 10.0
prerequisites:
- m7
objectives:
- RAG 시스템에서 발생하는 실패 유형을 식별하고 분류할 수 있다.
- 검색(Retrieval) 단계와 생성(Generation) 단계의 오류를 구분하여 분석할 수 있다.
- Ragas 프레임워크의 지표를 활용하여 자동 평가와 인간 검토 결과를 연결할 수 있다.
- 오류 분석 데이터를 바탕으로 RAG 파이프라인 성능 개선안을 도출할 수 있다.
worked_examples:
- '예시 1: 질문 ''모델 A의 출시일은?''에 대해 검색기가 ''모델 B의 사양'' 문서를 가져온 경우. 이는 ''검색 실패''로 분류하며,
  임베딩 모델 조정 또는 검색 쿼리 최적화가 해결책이 될 수 있습니다.'
- '예시 2: 질문 ''X를 설명하라''에 대해 검색기가 X에 대한 정확한 문서를 가져왔으나, LLM이 문서에 없는 정보로 답변한 경우. 이는 ''생성
  실패(충실도 부족)''로 분류하며, 프롬프트 엔지니어링을 통해 ''제공된 문맥만을 사용하라''는 제약을 강화해야 합니다.'
lab:
  title: 실패 데이터셋 수집 및 오류 분석
  steps:
  - 최소 50개의 질문에 대해 RAG 시스템의 답변과 검색된 문맥(context)을 저장합니다.
  - 각 항목에 대해 검색 관련성(Context Precision)과 생성 충실도(Faithfulness)를 Ragas로 측정합니다.
  - 지표가 낮은 하위 20%의 질문-답변 쌍을 추출합니다.
  - 추출된 표본에 대해 '검색 오류', '생성 오류', '논리 오류' 중 하나로 분류 표를 작성합니다.
  safety:
  - 개인정보나 비공개 데이터는 절대 평가 코드에 포함하지 않습니다.
  - 평가 과정에서 사용되는 API 호출 횟수와 비용을 모니터링하여 예산을 준수합니다.
  - 데이터 분석 시 로컬 환경에서 작업을 수행하여 정보 유출을 방지합니다.
  deliverables:
  - 분류가 완료된 오류 분석 CSV 파일
  - 검색 및 생성 품질 지표가 시각화된 Jupyter Notebook
assignment:
  title: RAG 오류 분류 및 개선 보고서 작성
  deliverables:
  - 오류 분석 결과가 요약된 2페이지 분량의 보고서
  - 분류된 실패 유형별 대응 전략(검색 최적화 또는 프롬프트 개선) 제안
  rubric:
  - 실패 유형 분류의 정확성과 타당성
  - 정량적 지표와 인간 검토 결과 간의 상관관계 분석 능력
  - 개선 전략의 논리적 타당성
quiz:
- question: RAG 시스템에서 검색 모듈이 관련 없는 문맥을 가져왔을 때 발생하는 실패는 무엇인가요?
  choices:
  - 생성 실패
  - 검색 실패
  - 데이터베이스 연결 오류
  - 인증 실패
  answer_index: 1
  explanation: 검색 모듈은 질문에 적합한 문서를 식별하는 역할을 하므로, 관련 없는 문맥을 가져오는 것은 검색 단계의 실패입니다 [S3].
- question: Ragas 프레임워크의 가장 큰 특징은 무엇인가요?
  choices:
  - 반드시 대규모의 인간 주석 데이터가 필요하다.
  - 레퍼런스 프리(Reference-free) 평가가 가능하다.
  - LLM 생성 품질 평가만 가능하다.
  - 실시간 스트리밍 시스템에만 적용 가능하다.
  answer_index: 1
  explanation: Ragas는 지면진실(ground truth) 없이도 검색과 생성 품질을 평가할 수 있는 레퍼런스 프리 평가 프레임워크입니다
    [S3].
completion_criteria:
- 실패 유형이 포함된 오류 분류표 제출
- Ragas 지표를 활용한 검색 및 생성 품질 정량 분석 완료
- 오류 분석을 바탕으로 한 파이프라인 개선 제안서 작성 및 검토
source_ids:
- S3
---

## RAG 시스템의 오류 분석 개요

RAG(Retrieval Augmented Generation) 아키텍처는 검색 모듈과 LLM 기반의 생성 모듈로 구성됩니다 [S3]. 시스템 성능을 평가할 때는 이 두 단계를 분리하여 분석하는 것이 중요합니다. 오류는 크게 검색 단계에서의 문제와 생성 단계에서의 문제로 나뉩니다.

### 1. 실패 유형 분류
- **검색 실패 (Retrieval Failure):** 관련성이 없거나 초점이 맞지 않는 문맥(context)을 검색한 경우 [S3].
- **생성 실패 (Generation Failure):** LLM이 제공된 문맥을 충실하게 이용하지 못하거나(Faithfulness), 질문과 관련 없는 답변을 생성하는 경우 [S3].

### 2. 자동 평가와 인간 검토의 보완
Ragas와 같은 레퍼런스 프리(Reference-free) 프레임워크는 인간 주석(ground truth) 없이도 검색과 생성 품질을 평가할 수 있게 해줍니다 [S3]. 하지만 자동화된 평가 지표만으로는 시스템의 미묘한 환각(hallucination)이나 복합적인 논리 오류를 모두 포착하기 어렵습니다. 따라서 정량적 자동 지표를 통해 우선순위가 높은 실패 표본을 추출하고, 이에 대해 반드시 인간 검토(Human Review)를 병행하여 실제 원인을 파악해야 합니다.
