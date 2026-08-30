---
layout: learn-module
title: 근거 충실도 평가
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability
course_locale: ko
lang: ko
ref: learn:rag-evaluation-reliability:generation-faithfulness
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/generation-faithfulness/
- lang: en
  url: /learn/en/rag-evaluation-reliability/generation-faithfulness/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/generation-faithfulness/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/generation-faithfulness/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/generation-faithfulness/
module_id: m5
permalink: /learn/rag-evaluation-reliability/generation-faithfulness/
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
id: m5
slug: generation-faithfulness
phase_id: p2
estimated_hours: 8.0
prerequisites:
- m4
objectives:
- 근거 충실도(Faithfulness)의 개념을 이해하고 RAG 시스템에서의 중요성을 파악한다.
- Ragas 프레임워크를 활용하여 생성된 답변이 검색된 문맥(Context)에 기반하는지 정량적으로 평가한다.
- 자동화된 평가 지표를 활용하여 환각(Hallucination) 위험을 분석한다.
worked_examples:
- '예시 1: 문맥 ''사과는 비타민 C가 풍부하다''와 답변 ''사과는 비타민 C가 많아 면역력에 좋다''가 있을 경우, ''면역력에 좋다''는
  문맥에 없는 정보이므로 근거 충실도 점수가 낮아진다.'
- '예시 2: 문맥 ''우리 회사의 창립일은 2020년 5월 1일이다''와 답변 ''당사는 2020년 5월에 설립되었다''는 정보가 일치하므로 높은
  근거 충실도 점수를 가진다.'
lab:
  title: Ragas를 활용한 생성 답변 근거 충실도 측정
  steps:
  - 평가 데이터셋(질문, 검색된 문맥, 생성된 답변)을 준비한다.
  - Ragas 라이브러리를 설치하고 `Faithfulness` 메트릭을 임포트한다.
  - 준비된 데이터셋을 Ragas의 데이터 구조로 변환한다.
  - LLM 기반 평가자를 구성하여 데이터셋의 근거 충실도 점수를 산출한다.
  - 점수가 낮은 답변들을 표본 추출하여 검색된 문맥과의 차이를 인간 검토로 분석한다.
  safety:
  - 비공개 문서나 개인정보가 포함된 데이터셋을 외부 LLM API로 전송하지 않는다.
  - API 요청 수 제한을 확인하고 캐시(Cache)를 사용하여 비용을 통제한다.
  - 인간 검토 시 표본 데이터의 보안을 유지한다.
  deliverables:
  - 전체 데이터셋의 평균 근거 충실도 점수 리포트
  - 낮은 점수를 기록한 답변에 대한 분석 데이터셋
  - 자동 평가 결과와 인간 검토 결과 비교 분석
assignment:
  title: RAG 파이프라인 신뢰성 평가 보고서
  deliverables:
  - 근거 충실도 평가가 포함된 Jupyter Notebook
  - 오류 분류 및 환각 발생 빈도 분석 보고서
  rubric:
  - 근거 충실도 메트릭 구현이 올바르게 되었는가?
  - 생성 답변의 환각 사례를 정확히 분류했는가?
  - 자동 평가 결과와 인간 검토의 정성적 일관성을 확보했는가?
quiz:
- question: RAG 시스템에서 근거 충실도(Faithfulness)란 무엇인가?
  choices:
  - 검색된 문맥이 질문과 관련성이 높은 정도
  - 생성된 답변이 검색된 문맥의 정보에 기반하는 정도
  - LLM이 사전 학습된 지식을 많이 활용하는 정도
  - 사용자의 질문에 답변이 정확히 일치하는 정도
  answer_index: 1
  explanation: 근거 충실도는 생성된 답변이 외부에서 검색된 문맥의 사실에 의존하는지를 평가하는 지표입니다.
- question: Ragas 프레임워크의 특징으로 옳은 것은?
  choices:
  - 반드시 인간 주석(Ground Truth)이 있어야만 평가가 가능하다.
  - 참조 기반이 없는(reference-free) 평가 방식을 지원한다.
  - 검색 효율성만 평가하며 생성 품질은 평가하지 않는다.
  - LLM을 평가자로 활용하지 않고 통계적 방식만 사용한다.
  answer_index: 1
  explanation: Ragas는 참조 기반 없이 평가 가능한 프레임워크를 목표로 하며 LLM을 평가자로 적극 활용합니다 [S3, S4].
completion_criteria:
- Ragas 라이브러리를 사용하여 생성 답변의 근거 충실도를 정량 측정할 수 있다.
- 평가 결과에서 환각 발생 유형을 최소 3가지 이상 분류할 수 있다.
- 자동화된 평가 파이프라인의 결과와 실제 답변의 일관성을 검증할 수 있다.
source_ids:
- S3
- S4
---

## 근거 충실도 (Faithfulness) 평가

RAG(Retrieval-Augmented Generation) 시스템의 핵심은 LLM이 외부 지식 데이터베이스에서 검색된 정보를 활용하여 답변을 생성하는 것이다. 근거 충실도(Faithfulness)는 생성된 답변이 검색된 문맥에 기술된 정보만을 충실히 반영하는지를 나타내는 지표이다 [S3].

### 1. 왜 근거 충실도를 평가하는가?
LLM은 사전 학습된 지식을 바탕으로 답변하려는 경향이 있어, 검색된 문맥과 무관한 정보를 생성하거나 문맥을 왜곡할 수 있다. 이를 '환각(Hallucination)'이라 하며, 근거 충실도 평가를 통해 이를 정량적으로 측정할 수 있다 [S4].

### 2. 평가 프레임워크: Ragas
Ragas는 사용자 주석이 없는 상황에서도 참조 기반 없이(reference-free) 평가가 가능한 프레임워크를 제안한다 [S3]. 근거 충실도 평가 과정은 일반적으로 다음 단계를 따른다:
- **답변에서 진술 추출**: 답변으로부터 검증 가능한 사실적 진술들을 분리한다.
- **증거 검색**: 각 진술이 검색된 문맥의 어떤 부분에서 도출되었는지 확인한다.
- **검증**: 추출된 진술들이 문맥 정보와 일치하는지 판단한다.

Ragas는 LLM을 평가자로 사용하여 이 과정을 자동화한다 [S4].
