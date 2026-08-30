---
layout: learn-module
title: 자동 평가 프레임워크(Ragas) 적용
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability
course_locale: ko
lang: ko
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
permalink: /learn/rag-evaluation-reliability/automated-eval-framework/
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
id: m7
slug: automated-eval-framework
phase_id: p2
estimated_hours: 10.0
prerequisites:
- m6
objectives:
- RAG 파이프라인의 핵심 평가 차원(검색 및 생성 품질)을 이해한다.
- Ragas 프레임워크를 사용하여 참조 없이(reference-free) RAG 성능을 자동 평가하는 방법을 익힌다.
- 정량적 메트릭을 통해 환각(hallucination) 위험을 분석하고 완화한다.
worked_examples:
- '사례 1: Context Relevance 계산. Ragas는 LLM을 사용해 검색된 문맥(Context)에서 질문에 답변하는 데 실제로 필요한
  문장들을 추출하고, 전체 문맥 대비 필요한 문장들의 비율을 통해 점수를 계산합니다.'
- '사례 2: Faithfulness 평가. 생성된 답변의 각 주장이 검색된 문맥에서 지지받는지 LLM이 판단합니다. 지지받지 못하는 주장이 많을수록
  환각 점수가 높아집니다.'
lab:
  title: Ragas를 활용한 RAG 성능 정량 평가 실습
  steps:
  - 평가 데이터셋(질문, 검색된 문맥, 생성된 답변)을 준비합니다.
  - Python 환경에서 `ragas` 라이브러리를 설치합니다.
  - 평가 데이터셋을 `ragas`의 Dataset 객체로 변환합니다.
  - Ragas의 `evaluate` 함수를 호출하여 Context Relevance, Faithfulness 등 메트릭을 계산합니다.
  - 결과값을 시각화하고 점수가 낮은 쿼리들을 분석합니다.
  safety:
  - 평가에 사용하는 문서 코퍼스에 개인정보나 비공개 데이터가 포함되지 않았는지 확인합니다.
  - API 사용 비용을 방지하기 위해 테스트 시 로컬 모델이나 캐싱을 적극 활용합니다.
  - 자동 평가 결과는 신뢰성의 보조 지표이며, 실제 모델의 품질 확정은 표본 인간 검토와 교차 검증을 병행합니다.
  deliverables:
  - 메트릭 점수가 포함된 평가 결과 데이터프레임
  - 낮은 점수를 받은 쿼리 유형 분석 로그
assignment:
  title: RAG 파이프라인 성능 비교 보고서
  deliverables:
  - 검색 설정(k값, 임베딩 모델 등)이 다른 두 가지 RAG 파이프라인의 Ragas 평가 결과
  - 두 설정 간의 성능 차이 분석 보고서
  rubric:
  - Ragas 메트릭(Context Relevance, Faithfulness 등)이 올바르게 구현되었는가?
  - 평가 결과가 정량적으로 비교되고 논리적인 해석이 포함되었는가?
  - 환각 유형을 최소 3건 이상 분류하고 개선 방안을 제시했는가?
quiz:
- question: Ragas 프레임워크의 가장 큰 특징은 무엇입니까?
  choices:
  - 사람의 정답 데이터셋이 반드시 필요하다
  - 참조 없이(reference-free) RAG 파이프라인을 평가할 수 있다
  - 검색 단계만을 평가하며 생성 단계는 평가하지 않는다
  - 반드시 GPU가 10개 이상 필요하다
  answer_index: 1
  explanation: Ragas는 정답 데이터셋 없이 LLM을 활용해 검색과 생성 품질을 자동 평가하는 프레임워크입니다 [S3, S4].
- question: Ragas에서 측정하는 'Faithfulness' 메트릭의 정의는 무엇입니까?
  choices:
  - 검색된 문맥이 질문과 얼마나 관련이 있는가
  - 질문이 문서 코퍼스 내에 존재하는가
  - 생성된 답변이 검색된 문맥에 기반하고 있는가
  - 질문자가 LLM의 답변을 얼마나 신뢰하는가
  answer_index: 2
  explanation: Faithfulness는 생성된 답변이 제공된 검색 문맥에 얼마나 충실하게 기반하여 생성되었는지(환각 방지)를 측정하는
    지표입니다 [S4].
completion_criteria:
- Ragas 라이브러리를 사용하여 최소 10건의 쿼리에 대해 4가지 이상의 메트릭을 계산 성공함
- 실습 노트북이 Git 저장소에 정기적으로 커밋됨
- 성능 비교 보고서 내에 최소 3건의 오류 분류 사례가 포함됨
source_ids:
- S3
- S4
---

## RAG 평가의 도전 과제와 Ragas

RAG 시스템은 검색 모듈과 LLM 기반 생성 모듈로 구성됩니다 [S3, S4]. 이러한 구조를 평가하는 것은 도전적인 작업인데, 검색 시스템이 관련성 높은 문맥(context)을 얼마나 잘 식별하는지, LLM이 제공된 문맥을 얼마나 충실하게(faithfully) 활용하는지, 그리고 답변의 품질은 어떠한지를 모두 고려해야 하기 때문입니다 [S4].

전통적인 평가 방식은 사람이 직접 정답(ground truth)을 작성하고 비교하는 방식에 의존했으나, 이는 비용이 많이 들고 시간이 오래 걸려 빠른 반복 주기에 부적합합니다 [S3, S4].

### Ragas 프레임워크
Ragas(Retrieval Augmented Generation Assessment)는 정답 데이터셋 없이도 RAG 파이프라인을 평가할 수 있는 프레임워크입니다 [S3, S4]. Ragas는 다음과 같은 핵심 차원을 자동 평가합니다:

1. **검색 품질(Retrieval Quality):** 검색된 문맥이 질문과 얼마나 관련이 있는지(Context Relevance), 모든 필요한 정보를 포함하는지(Context Recall)를 측정합니다.
2. **생성 품질(Generation Quality):** 생성된 답변이 검색된 문맥에 기반하고 있는지(Faithfulness), 질문에 얼마나 관련이 있는지(Answer Relevance)를 측정합니다.

이러한 메트릭은 LLM을 '평가자(judge)'로 활용하여 참조 없이도 평가가 가능하게 하며, RAG 개발 주기를 단축하는 데 기여합니다 [S3, S4].
