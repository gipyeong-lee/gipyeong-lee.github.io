---
layout: learn-module
title: 표본 인간 검토 및 대조
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability
course_locale: ko
lang: ko
ref: learn:rag-evaluation-reliability:human-review-validation
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/human-review-validation/
- lang: en
  url: /learn/en/rag-evaluation-reliability/human-review-validation/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/human-review-validation/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/human-review-validation/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/human-review-validation/
module_id: m9
permalink: /learn/rag-evaluation-reliability/human-review-validation/
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
id: m9
slug: human-review-validation
phase_id: p3
estimated_hours: 10.0
prerequisites:
- m8
objectives:
- 자동화된 RAG 평가 지표와 실제 사실성 간의 간극을 이해한다.
- 모델이 생성한 답변의 근거 충실도(Factual Consistency)를 인간이 검토하는 프로토콜을 설계한다.
- LLM 평가의 한계를 파악하고, TrueTeacher와 같은 합성 데이터 기법의 의의를 분석한다 [S5].
- 오류 유형을 체계적으로 분류하고 신뢰성 데이터셋을 관리하는 방법을 익힌다.
worked_examples:
- '예시 1: 자동 평가 지표(예: Faithfulness)가 0.9로 높게 나왔으나, 인간 검토 결과 검색 문서에는 없는 내용이 포함된 경우.
  분석: 모델이 검색된 정보가 아닌 내부 가중치에 포함된 과거 정보를 사용한 환각으로 분류하고, 이를 시스템 오류 로그에 기록함.'
- '예시 2: TrueTeacher 모델을 사용하여 시스템이 답변의 사실성을 스스로 평가하도록 설계한 경우. LLM이 ''참''이라고 평가한 답변
  중 일부를 인간이 표본 조사하여, LLM 평가기의 오류율(False Positive)을 측정하고 이를 평가 보고서에 명시함 [S5].'
lab:
  title: 표본 인간 검토 및 오류 분석 수행
  steps:
  - 자동 평가 파이프라인(Ragas 등)을 통해 100건의 답변에 대한 Faithfulness 점수를 도출한다.
  - 점수가 가장 낮은 10건과 중간 수준의 10건, 높은 10건을 무작위로 추출하여 검토셋을 만든다.
  - 답변, 검색 문서(Context), 정답(Ground Truth)을 대조하며 '검색 누락', '정보 왜곡', '환각 생성' 여부를 수동 기록한다.
  - 기록된 인간 판단과 자동 평가 점수를 비교하여 상관관계 분석을 수행한다.
  safety:
  - 검토 대상 데이터셋에 실제 개인정보나 민감한 비공개 문서가 포함되지 않았는지 반드시 확인한다.
  - 검토 완료된 데이터는 로컬 스토리지에 안전하게 보관하며, 검증되지 않은 외부 API에 업로드하지 않는다.
  deliverables:
  - 최소 30건의 인간 검토 기록이 포함된 오류 분류 시트(CSV/Excel)
  - 자동 지표와 인간 평가 간의 일치도를 분석한 요약 리포트
assignment:
  title: RAG 신뢰성 분석 보고서 작성
  deliverables:
  - 인간 검토를 통해 분류된 실패 유형 빈도 표
  - 현재 시스템의 주요 취약점(검색 단계 혹은 생성 단계)에 대한 분석 보고서
  - 향후 자동 평가 파이프라인 개선을 위한 제언
  rubric:
  - 오류 유형이 체계적으로 분류되었는가?
  - 자동 평가 지표의 한계를 구체적인 예시와 함께 논리적으로 서술했는가?
  - 인간 검토 데이터가 신뢰성 분석의 근거로 적절하게 활용되었는가?
quiz:
- question: 자동화된 사실성 평가 지표만으로 시스템 신뢰성을 확정하기 어려운 주된 이유는 무엇인가?
  choices:
  - 자동 평가 지표는 매우 빠르기 때문에.
  - 모델 생성 데이터는 인간이 작성한 데이터와는 다른 특징을 가지며, 자동 평가기 자체가 사실적 오류를 모두 잡아내지 못할 수 있기 때문 [S5].
  - 인간 검토 데이터가 항상 자동 평가 지표보다 정확하기 때문.
  - 데이터셋의 규모가 작기 때문.
  answer_index: 1
  explanation: 기존의 요약 기반 평가 데이터셋은 모델이 생성하는 실제 결과물의 복잡성을 충분히 반영하지 못하며, 자동 평가 시스템은 특정
    상황에서 환각을 검출하지 못할 수 있습니다.
- question: TrueTeacher 방식이 기존 요약 데이터셋 활용법과 다른 점은 무엇인가?
  choices:
  - 인간이 작성한 요약문에만 의존한다.
  - 모델이 생성한 다양한 요약을 활용하여 사실성 평가를 위한 합성 데이터를 생성한다 [S5].
  - NLI 모델을 사용하지 않는다.
  - 다국어 지원이 불가능하다.
  answer_index: 1
  explanation: TrueTeacher는 인간이 작성한 요약에 의존하지 않고, LLM을 사용하여 모델이 생성한 다양한 데이터를 합성적으로
    주석 달아 학습 데이터를 생성합니다 [S5].
completion_criteria:
- 최소 30건의 데이터 표본에 대한 인간 검토 로그가 작성되어야 함.
- 자동 평가 결과와 인간 검토 결과 간의 비교 분석이 포함된 리포트가 제출되어야 함.
- 오류 분류를 통해 현재 시스템의 취약점이 명확히 정의되어야 함.
source_ids:
- S5
---

## 자동화 평가의 한계와 인간 검토의 필요성

검색 증강 생성(RAG) 시스템의 품질을 평가할 때 Ragas와 같은 도구는 정량적 지표를 빠르게 제공하지만, 모델이 생성한 답변의 미묘한 사실적 오류를 완벽히 포착하는 데는 한계가 있습니다. 특히 복잡한 맥락에서 LLM이 지식 내에서 추론하는지, 혹은 학습된 데이터에 의존하여 환각(Hallucination)을 생성하는지 구분하기 어렵습니다.

### 사실적 일관성 평가

최근 연구는 자연어 추론(NLI) 모델이나 대형 언어 모델(LLM)을 활용하여 요약이나 답변의 사실성을 평가합니다. 그러나 기존 방식은 인간이 작성한 요약 데이터셋에 의존하며, 이는 실제 모델이 생성하는 결과물의 특성과 차이가 발생할 수 있습니다 [S5]. TrueTeacher와 같은 접근법은 LLM을 활용하여 모델 생성 데이터에서 합성적인 사실성 평가 데이터를 생성함으로써 이러한 한계를 극복하려 합니다 [S5].

### 인간 검토(Human-in-the-Loop)의 역할

자동 평가 파이프라인이 아무리 고도화되더라도, 최종적인 신뢰성 검증은 인간의 검토가 필수적입니다. 인간 검토는 다음 역할을 수행합니다:
1. **자동 평가 지표의 검증:** 특정 답변이 '관련 있음'으로 평가되었으나 실제로는 사실이 아닌 경우를 식별.
2. **환각 유형 분류:** 시스템의 구조적 결함(검색 오류 vs. 생성 모델 오류)을 진단.
3. **회귀 테스트 셋의 보정:** 인간이 검수한 데이터를 바탕으로 평가셋의 품질을 지속적으로 개선.
