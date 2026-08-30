---
layout: learn-module
title: 질문-정답 평가셋 구축
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability
course_locale: ko
lang: ko
ref: learn:rag-evaluation-reliability:eval-set-generation
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/eval-set-generation/
- lang: en
  url: /learn/en/rag-evaluation-reliability/eval-set-generation/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/eval-set-generation/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/eval-set-generation/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/eval-set-generation/
module_id: m3
permalink: /learn/rag-evaluation-reliability/eval-set-generation/
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
id: m3
slug: eval-set-generation
phase_id: p1
estimated_hours: 8.0
prerequisites:
- m2
objectives:
- RAG 시스템 평가를 위한 고품질 질문-정답(QA) 평가셋의 필요성을 이해한다.
- 합성 데이터 생성 기법(Synthetic Data Generation)을 활용하여 평가셋을 구축하는 원리를 파악한다.
- TrueTeacher와 같은 방법론을 통해 모델 생성 답변의 사실적 일관성을 평가하는 논리를 습득한다.
- 평가셋의 품질을 유지하면서 도메인 변화에 강건한 데이터셋을 생성하는 프로세스를 설계한다.
worked_examples:
- '예제 1: 문서 코퍼스에서 핵심 구절 추출하기. 주어진 문서에서 LLM을 사용하여 문맥상 중요한 사실 문장을 추출하고, 이를 기반으로 ''답변
  가능한 질문''과 ''거짓 질문(Negative Sample)''을 생성하는 파이프라인 구성.'
- '예제 2: 사실성 검증 프롬프트 설계. 생성된 질문과 검색된 문서를 바탕으로 LLM에게 ''검색된 문서에 근거하여 질문에 답변하고, 답변이 사실적으로
  일관적인지 True/False로 판단하라''고 지시하여 평가용 정답지(Ground Truth)를 정교화하는 과정.'
lab:
  title: 합성 평가셋 생성 실습
  steps:
  - 준비된 오픈 라이선스 문서 코퍼스를 로드하고 텍스트 청크 단위로 분할한다.
  - LLM API를 사용하여 각 청크에서 추출 가능한 고유 질문-답변 쌍을 100건 이상 생성한다.
  - 생성된 질문에 대해 검색 시스템을 시뮬레이션하여 상위 k개의 문서를 검색한다.
  - 검색된 문서와 생성된 답변 간의 사실적 일관성을 판단하는 평가 파이프라인을 구축한다.
  - 결과 데이터를 JSONL 형식으로 저장하고, 샘플 30건을 수동으로 검토하여 데이터 품질을 기록한다.
  safety:
  - 평가셋 구축 과정에서 외부 API 사용 시 비용 상한선(API Key Limit)을 반드시 설정한다.
  - 생성된 데이터셋 내에 원본 문서의 민감 정보나 개인정보가 포함되지 않았는지 정규 표현식으로 필터링한다.
  - 모델 평가 결과만을 맹신하지 않고 표본에 대한 수동 대조를 반드시 병행한다.
  deliverables:
  - 구축된 100문항 이상의 질문-정답 평가셋(JSONL 파일)
  - 데이터셋 생성 및 검증 코드가 포함된 Jupyter Notebook
  - 인간 검토 기록이 포함된 품질 분석 리포트
assignment:
  title: RAG 신뢰성 평가셋 회귀 보고서
  deliverables:
  - 생성된 평가셋의 통계적 분포(질문 길이, 답변 길이, 문서 참조 빈도 등)를 분석한 대시보드
  - '두 가지 이상의 RAG 설정(예: 검색 알고리즘 변경, 모델 변경)을 동일한 평가셋으로 비교한 결과물'
  - 오류 분류표(Hallucination, Contextual Irrelevance 등) 작성 및 사례 분석
  rubric:
  - 평가셋이 전체 문서 코퍼스의 내용을 고르게 반영하고 있는가?
  - 합성 데이터 생성 파이프라인이 재현 가능한 형태로 작성되었는가?
  - 오류 유형 분류가 구체적이고 정량적인 근거를 갖추었는가?
  - 인간 검토를 통해 자동 평가 지표의 타당성을 입증하였는가?
quiz:
- question: TrueTeacher 방법론이 기존의 합성 데이터 생성 방식과 차별화되는 점은 무엇인가요?
  choices:
  - 인간이 작성한 요약에 전적으로 의존한다.
  - 모델이 생성한 다양한 요약을 주석 처리하여 합성 데이터를 생성한다.
  - 오직 소형 모델만을 학습용 교사로 사용한다.
  - 데이터셋을 수동으로만 작성하여 정확도를 높인다.
  answer_index: 1
  explanation: TrueTeacher는 인간이 작성한 요약에 의존하지 않고, LLM을 사용하여 모델이 생성한 다양한 요약을 주석 처리함으로써
    합성 데이터를 생성합니다 [S5].
- question: RAG 평가셋 구축 시 모델 자동 평가만으로 사실성을 확정하지 않는 이유는 무엇인가요?
  choices:
  - 모델 자동 평가가 인간보다 너무 느리기 때문입니다.
  - 모델 자동 평가가 완벽하지 않으며 환각(Hallucination)을 완전히 걸러낼 수 없기 때문입니다.
  - 인간 평가는 비용이 들지 않기 때문입니다.
  - 사실성 평가에는 모델이 필요 없기 때문입니다.
  answer_index: 1
  explanation: 자동화된 평가 도구는 효율적이지만 완벽하지 않으므로, 사실성 검증을 위해 반드시 표본 인간 검토와 출처 대조를 병행해야
    합니다.
completion_criteria:
- 100문항 이상의 질문-정답 평가셋 데이터셋 구축 완료
- 데이터셋 품질 분석 및 인간 검토 기록 제출
- RAG 파이프라인의 성능 평가를 위한 노트북 구현 및 결과 보고서 작성
- CI/CD 환경에서 재실행 가능한 형태의 평가 패키지 구성
source_ids:
- S5
---

## RAG 평가를 위한 질문-정답(QA) 평가셋 구축

RAG(Retrieval-Augmented Generation) 시스템의 성능을 신뢰성 있게 측정하기 위해서는 정교하게 설계된 평가셋이 필수적입니다. 단순히 인간이 작성한 질문과 답변에만 의존하는 방식은 대규모 평가 시 비용과 확장성 측면에서 한계가 있습니다.

### 합성 데이터 생성의 중요성
최신 연구인 TrueTeacher 방법론에 따르면, LLM을 활용해 모델이 생성한 다양한 답변을 주석 처리하여 합성 훈련 데이터를 생성할 수 있습니다 [S5]. 이 방식은 다음과 같은 장점을 가집니다:
1. **비용 효율성**: 인간이 직접 작성한 요약이나 답변에 의존하지 않으므로 대규모 데이터셋(예: 1.4M 예제) 생성이 가능합니다 [S5].
2. **다국어 및 확장성**: 특정 언어에 국한되지 않으며, 도메인 전환(Domain-shift)에 대해서도 강건성을 보여줍니다 [S5].
3. **사실적 일관성 평가**: 합성 데이터를 통해 학습된 소형 모델은 대형 LLM 교사 모델의 지식을 성공적으로 증류(Distillation)하여 효율적인 사실성 평가 도구로 활용될 수 있습니다 [S5].

### 데이터셋 구성 전략
평가셋을 구축할 때는 단순히 질문-정답 쌍을 만드는 것을 넘어, '검색 결과가 정답을 도출하는 데 필요한 근거를 포함하고 있는가?'와 '모델이 해당 근거를 왜곡 없이 참조하는가?'를 측정할 수 있도록 구성해야 합니다. 이를 위해 데이터셋 생성 시 질문의 복잡도, 검색 결과와의 관련성, 답변의 사실적 일관성을 체계적으로 레이블링하거나 검증해야 합니다.
