---
layout: learn-module
title: 인용 정확도 및 출처 추적
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability
course_locale: ko
lang: ko
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
permalink: /learn/rag-evaluation-reliability/citation-accuracy/
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
id: m6
slug: citation-accuracy
phase_id: p2
estimated_hours: 8.0
prerequisites:
- m5
objectives:
- RAG 시스템에서 답변이 검색된 문서의 내용을 얼마나 충실히 반영하는지 이해한다.
- 인용(Citation) 정확도의 정의와 측정 방식을 학습한다.
- Ragas 프레임워크를 활용하여 답변의 근거 충실도(Faithfulness)와 답변 관련성(Answer Relevance)을 정량 평가한다.
- 모델의 답변에서 출처 추적 가능성을 검증하는 프로세스를 설계한다.
worked_examples:
- '예제 1: 근거 충실도 점수 계산. 질문 ''A사의 2025년 매출은?''에 대해 답변 ''A사의 2025년 매출은 100억입니다.''가 생성되었고,
  맥락 문서에 ''A사는 2025년 100억 매출을 기록했다.''가 포함된 경우, 답변의 모든 정보가 맥락 내에 존재하므로 근거 충실도 점수는 1.0(최대치)으로
  평가됩니다.'
- '예제 2: 인용 정확도 오류 식별. 질문 ''A사의 창립 연도는?''에 대해 답변 ''A사는 1990년에 창립되었습니다(참고: 문서 1).''가
  생성되었으나, 문서 1에 ''A사는 1995년 창립''이라고 명시된 경우, 이는 ''사실 왜곡'' 실패 유형으로 분류되며 인용 정확도가 낮은 것으로
  판단합니다.'
lab:
  title: Ragas를 활용한 답변 근거 충실도 자동 평가 실습
  steps:
  - 평가할 RAG 시스템의 검색 결과(Context)와 생성된 답변(Answer) 데이터셋을 준비합니다.
  - Ragas 프레임워크를 설치하고 답변 데이터셋을 로드합니다.
  - Ragas의 `Faithfulness` 지표를 사용하여 데이터셋의 각 질문-답변 쌍에 대해 점수를 계산합니다.
  - 근거 충실도가 0.7 미만인 답변 30건을 별도로 추출합니다.
  - 추출된 샘플을 인간이 직접 검토하여 '인용 누락', '허위 인용', '사실 왜곡' 중 해당하는 실패 유형을 태깅합니다.
  safety:
  - 평가 과정에서 사용되는 문서 코퍼스에 개인정보나 기업 기밀이 포함되지 않도록 사전에 비식별화 처리를 완료하십시오.
  - 외부 API 호출 시 비용 상한을 설정하고, 재현성을 위해 시드(Seed) 값을 고정하여 반복적인 API 비용 발생을 방지하십시오.
  deliverables:
  - 평가 결과가 포함된 Jupyter Notebook 파일(.ipynb)
  - 근거 충실도 점수 분포 시각화 차트
  - 인간 검토 기록이 포함된 실패 유형 분류 테이블
assignment:
  title: RAG 시스템 신뢰성 회귀 평가 보고서 작성
  deliverables:
  - '두 가지 이상의 RAG 설정(예: 검색 Top-k 값 변경)에 따른 근거 충실도 통계 비교 결과'
  - 샘플 30건에 대한 인간 검토 대조표
  - 시스템의 인용 정확도 향상을 위한 개선 방안 제안서
  rubric:
  - 평가 지표의 정량적 산출 방식이 정확하게 명시되었는가?
  - 검색 문서와 생성 답변 간의 인용 관계가 논리적으로 추적 가능한가?
  - 실패 유형 분류가 인간 검토 데이터와 일치하며 타당한 근거를 제시하는가?
quiz:
- question: Ragas 프레임워크의 '근거 충실도(Faithfulness)' 지표에 대한 설명으로 옳은 것은?
  choices:
  - 답변이 질문과 관련성이 있는지를 평가한다.
  - 답변의 모든 정보가 제공된 맥락 문서 내에 존재하는지 측정한다.
  - 답변이 문법적으로 얼마나 정확한지 평가한다.
  - 답변이 외부 지식 베이스의 모든 정보를 포함하는지 측정한다.
  answer_index: 1
  explanation: 근거 충실도는 생성된 답변의 주장이 검색된 컨텍스트에 근거하고 있는지 측정하는 지표입니다.
- question: 인용 정확도 평가 시 '사실 왜곡' 실패 유형에 해당하는 경우는?
  choices:
  - 검색 문서에 없는 내용을 답변에 포함시킨 경우
  - 인용 표기를 누락한 경우
  - 인용은 올바르게 표시했으나 원문의 사실 관계를 잘못 해석하여 서술한 경우
  - 답변이 질문의 의도와 완전히 다른 경우
  answer_index: 2
  explanation: 사실 왜곡은 출처 문서를 인용했음에도 불구하고, 원문의 정보를 잘못된 방식으로 요약하거나 변형하여 생성하는 경우를 말합니다.
completion_criteria:
- Jupyter Notebook을 통한 자동화된 평가 지표 산출 완료
- 최소 30건의 답변 샘플에 대한 인간 검토 및 실패 유형 분류 기록 제출
- 평가 결과와 개선 방안이 포함된 최종 보고서 작성
source_ids:
- S4
---

## RAG 시스템의 인용 및 근거 충실도 평가

RAG(Retrieval Augmented Generation) 시스템은 외부 지식 베이스를 활용하여 LLM의 환각(Hallucination) 위험을 줄이지만, 생성된 답변이 검색된 문서를 정확히 인용하고 있는지 검증하는 과정이 필수적이다 [S4].

### 1. 주요 평가 지표
* **근거 충실도 (Faithfulness):** 생성된 답변이 제공된 검색 맥락(Context)으로부터 파생되었는지 측정합니다. 답변의 모든 주장이 검색된 문서를 기반으로 해야 하며, 외부 지식이나 모델의 사전 학습 지식으로만 답변하는 경우 점수가 낮아집니다 [S4].
* **답변 관련성 (Answer Relevance):** 답변이 주어진 질문에 얼마나 직접적으로 관련이 있는지 평가합니다. 이는 검색된 정보가 충분하더라도 답변이 질문의 의도와 어긋나는 경우를 식별하는 데 사용됩니다.

### 2. 인용 정확도 검증 프로세스
인용 정확도는 답변의 특정 문장이 검색된 문맥의 어느 부분을 인용했는지 식별하고, 해당 원문의 사실과 일치하는지 확인하는 과정입니다. 자동화 평가 프레임워크인 Ragas는 이러한 과정을 위해 참조 데이터(Ground Truth) 없이도 근거 충실도를 평가할 수 있는 지표를 제공합니다 [S4].

### 3. 실패 유형 분류
- **인용 누락:** 답변의 사실 관계가 검색 문서에 존재함에도 인용을 표시하지 않음.
- **허위 인용:** 검색 문서에 없는 내용을 인용한 것처럼 표시.
- **사실 왜곡:** 인용은 올바르게 표시했으나 원문의 의미를 잘못 해석하여 생성함.
