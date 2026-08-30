---
layout: learn-module
title: 평가용 문서 코퍼스 큐레이션
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability
course_locale: ko
lang: ko
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
permalink: /learn/rag-evaluation-reliability/corpus-curation/
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
id: m2
slug: corpus-curation
phase_id: p1
estimated_hours: 8.0
prerequisites:
- m1
objectives:
- RAG 평가를 위한 고정 문서 코퍼스의 중요성을 이해한다.
- 평가용 문서 데이터의 품질 결정 요소(정확성, 다양성, 중복 제거)를 학습한다.
- 정량적 평가를 위한 문서-질문-정답 쌍(QA Pair) 데이터셋 구축 전략을 익힌다.
- 데이터 누출(Data Leakage)을 방지하기 위한 학습/평가 분할 방법을 습득한다.
worked_examples:
- '예제 1: 문서 청킹(Chunking) 전략. 텍스트를 고정 크기로 나눌 때 문맥이 끊기지 않도록 문단 단위나 의미 단위로 나누는 파이썬 스크립트
  작성법.'
- '예제 2: 질문-답변 데이터 구성. { ''question'': ''...'', ''ground_truth'': ''...'', ''context_chunk_id'':
  ''...'' } 형식의 JSON 객체 생성 예시.'
lab:
  title: 평가용 코퍼스 구축 실습
  steps:
  - 평가할 대상 도메인의 오픈 라이선스 텍스트 파일(.txt)을 확보한다.
  - 파이썬을 사용하여 텍스트 파일을 읽고 청크 단위로 나누는 스크립트를 작성한다.
  - 각 청크에 고유 식별자(ID)를 부여하고 메타데이터(제목, 소스)를 기록한다.
  - 작성한 청크들 중에서 질문을 생성하고, 답변의 근거가 되는 청크 ID를 기록하여 50개의 QA 쌍을 구성한다.
  - 전체 코퍼스를 8:2 비율로 개발셋과 테스트셋으로 나누어 저장한다.
  safety:
  - 개인정보가 포함된 문서는 평가 코퍼스에 포함하지 않는다.
  - 외부 API 사용 시 요청 수 상한을 설정하여 비용을 제어한다.
  - 작업 시 생성된 데이터는 Git을 통해 버전을 관리하여 재현성을 확보한다.
  deliverables:
  - 구축된 문서 코퍼스 파일(JSONL 형식)
  - 질문과 정답이 포함된 QA 데이터셋(JSON 형식)
  - 코퍼스 분할 기록이 담긴 Jupyter Notebook 파일
assignment:
  title: 도메인 기반 RAG 데이터셋 완성
  deliverables:
  - 최소 100문항의 QA 데이터셋 파일
  - 데이터셋 통계 분석 보고서(질문 길이, 청크 길이 등)
  - 데이터 분할 과정이 포함된 Python 코드
  rubric:
  - 코퍼스 내 중복 청크 제거 완료 여부
  - 테스트셋과 개발셋의 데이터 누출 여부 확인
  - 답변의 근거가 되는 문서 구간(Chunk ID)의 정확한 매핑 여부
quiz:
- question: RAG 시스템에서 '데이터 누출(Data Leakage)'을 방지하는 가장 좋은 방법은 무엇인가요?
  choices:
  - 모든 문서에 대해 동일한 질문을 생성한다.
  - 개발셋과 최종 평가용 테스트셋을 분리하여 관리한다.
  - 학습 데이터에 검색 대상 문서 전체를 포함시킨다.
  - 평가셋을 매번 새로 생성하여 관리한다.
  answer_index: 1
  explanation: 평가셋이 학습(또는 개발) 과정에서 검색 대상 문서에 노출되면 공정한 평가가 불가능하므로, 평가용 테스트셋을 엄격히 분리해야
    합니다.
- question: 코퍼스 큐레이션 과정에서 '중복 제거'가 중요한 이유는 무엇인가요?
  choices:
  - LLM의 생성 속도를 높이기 위해서
  - 디스크 저장 공간을 절약하기 위해서
  - 검색 결과의 다양성을 확보하고 통계적 편향을 방지하기 위해서
  - 문서의 의미론적 유사도를 낮추기 위해서
  answer_index: 2
  explanation: 중복된 정보는 검색 엔진이 특정 정보에 편향되게 검색 결과를 반환하게 만들며, 정량적 평가 지표를 왜곡시킬 수 있습니다.
completion_criteria:
- 평가용 문서 코퍼스(최소 100개 청크 이상) 구축 완료
- 검증 가능한 QA 데이터셋(최소 100문항) 생성 완료
- 데이터셋 분할 정책 준수 확인
- 결과물에 대한 동료 검토 또는 자기 평가 체크리스트 작성 완료
source_ids:
- S2
---

## RAG 평가를 위한 코퍼스 큐레이션

대규모 언어 모델(LLM)은 학습된 파라미터 내의 지식에 의존할 때 환각(Hallucination) 위험이 존재합니다. 검색 증강 생성(RAG)은 모델이 실시간으로 외부 지식에 접근하도록 하여 이러한 한계를 극복합니다 [S2]. 효과적인 RAG 시스템의 신뢰성을 정량적으로 평가하기 위해서는 **고정되고 제어 가능한 평가용 문서 코퍼스(Fixed Evaluation Corpus)**가 필수적입니다.

### 1. 코퍼스 품질 결정 요소
- **정확성(Factuality):** 문서 내의 정보는 최신이고 사실적이어야 합니다. 잘못된 정보가 포함된 코퍼스는 잘못된 답변을 생성하게 합니다.
- **도메인 적합성:** 평가하고자 하는 실제 서비스 환경과 유사한 주제 및 어휘를 포함해야 합니다.
- **중복 제거(De-duplication):** 동일한 정보가 여러 문서에 중복될 경우, 검색 결과의 다양성이 저해되고 평가 통계에 편향을 줄 수 있습니다.

### 2. QA 평가 데이터셋 구축
문서 코퍼스만으로는 평가가 불가능합니다. '문서-질문-정답' 쌍을 구축하여 검색기가 관련 문서를 가져오는지, 생성기가 이를 기반으로 정확한 답변을 하는지 측정해야 합니다.
- **질문 생성:** LLM을 사용하여 문서에서 질문을 자동으로 생성하거나, 도메인 전문가가 직접 작성합니다.
- **정답 정의:** 답변의 근거가 되는 문서 구간(Chunk)을 명확히 명시해야 합니다.

### 3. 데이터 분할 및 무결성
평가셋의 신뢰성을 위해 **개발용(Development Set)**과 **최종 평가용(Hold-out Test Set)**을 엄격히 분할해야 합니다. 평가셋에 포함된 질문이 검색 대상 문서에 직접적으로 포함되어 노출되는 '데이터 누출' 현상을 방지해야 합니다.
