---
layout: learn-module
title: RAG 아키텍처 이해
course_slug: rag-evaluation-reliability
course_data_key: rag-evaluation-reliability
course_locale: ko
lang: ko
ref: learn:rag-evaluation-reliability:intro-rag-architecture
translations:
- lang: ko
  url: /learn/rag-evaluation-reliability/intro-rag-architecture/
- lang: en
  url: /learn/en/rag-evaluation-reliability/intro-rag-architecture/
- lang: ja
  url: /learn/ja/rag-evaluation-reliability/intro-rag-architecture/
- lang: zh-cn
  url: /learn/zh-cn/rag-evaluation-reliability/intro-rag-architecture/
- lang: zh-tw
  url: /learn/zh-tw/rag-evaluation-reliability/intro-rag-architecture/
module_id: m1
permalink: /learn/rag-evaluation-reliability/intro-rag-architecture/
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
id: m1
slug: intro-rag-architecture
phase_id: p1
estimated_hours: 8.0
prerequisites: []
objectives:
- RAG(Retrieval-Augmented Generation) 아키텍처의 핵심 구성 요소를 이해한다.
- 대규모 언어 모델(LLM)이 가진 지식 한계와 검색 기반 증강의 필요성을 파악한다.
- 검색-생성 파이프라인의 구조적 흐름을 설명할 수 있다.
worked_examples:
- '사례 1: 전통적인 LLM 방식 - ''오늘자 뉴스 알려줘''라고 질문할 경우 학습 데이터 이후의 사건을 인지하지 못해 잘못된 정보를 생성할
  위험이 있음.'
- '사례 2: RAG 방식 - ''오늘자 뉴스 알려줘'' 질문 시, 1) 외부 검색 엔진이나 실시간 뉴스 API를 통해 검색기(Retriever)가
  관련 기사를 수집하고, 2) 이를 문맥(context)으로 포함하여 LLM에 전달함으로써 정확한 최신 정보 응답을 생성.'
lab:
  title: RAG 아키텍처 흐름 시각화 및 분석
  steps:
  - Jupyter Notebook을 열고 RAG 기본 파이프라인의 3단계(입력, 검색, 생성) 구조를 도식화한다.
  - 오픈 라이선스 문서 코퍼스에서 5개의 짧은 텍스트를 추출하여 데이터셋 샘플을 만든다.
  - 간단한 키워드 매칭 검색기(Retriever) 함수를 작성하여 질문에 맞는 문서를 반환하도록 구현한다.
  - 검색된 문서를 프롬프트 템플릿에 주입하는 증강 단계를 코드로 작성한다.
  safety:
  - 실제 개인정보나 기밀문서를 절대 코퍼스 데이터로 사용하지 않는다.
  - API 사용 시 호출 횟수 제한(Rate Limit)을 확인하고 테스트 코드에 시드(seed) 값을 설정하여 재현성을 확보한다.
  deliverables:
  - RAG 아키텍처 다이어그램 (Notebook 셀 내 포함)
  - 간단한 키워드 기반 검색기 구현 코드
  - 문서 주입형 프롬프트 생성 결과물
assignment:
  title: RAG 기반 정보 검색 파이프라인 분석 보고서
  deliverables:
  - 구현한 RAG 파이프라인의 작동 원리를 설명하는 Notebook
  - 검색기가 문서의 관련성을 판단할 때 발생할 수 있는 잠재적 실패 사례 3가지 기술
  rubric:
  - RAG의 3단계(검색, 증강, 생성)가 정확하게 구분되어 설명되었는가?
  - 검색 단계에서 관련 없는 문서가 검색될 가능성에 대한 분석이 타당한가?
  - 비공개 데이터 보안 지침을 준수하며 구현하였는가?
quiz:
- question: RAG가 LLM 학습 방식과 비교하여 가지는 주된 장점은 무엇입니까?
  choices:
  - LLM의 파라미터 크기를 줄일 수 있다.
  - 모델의 지식을 최신 상태로 유지하고 근거를 제시할 수 있다.
  - 모델의 학습 속도를 가속화한다.
  - 모든 질문에 대해 100% 사실인 답변을 생성한다.
  answer_index: 1
  explanation: RAG는 외부 문서를 참조하므로 최신 정보를 반영할 수 있고, 생성된 답변의 근거를 문서에서 찾을 수 있어 신뢰성이 높습니다.
- question: 검색기(Retriever)의 역할로 올바른 것은 무엇입니까?
  choices:
  - 답변을 생성하는 역할을 한다.
  - 학습 데이터를 다시 학습시키는 역할을 한다.
  - 질문과 관련된 외부 문서 조각을 검색한다.
  - 사용자 인터페이스를 관리한다.
  answer_index: 2
  explanation: 검색기는 사용자의 질문과 의미적으로 유사하거나 관련성이 높은 문서를 외부 데이터 소스에서 찾아오는 역할을 합니다.
completion_criteria:
- RAG 아키텍처의 구성 요소를 설명할 수 있다.
- 실습한 RAG 파이프라인 코드가 정상적으로 작동하여 관련 문서를 검색 및 증강하는 것을 확인한다.
- RAG 파이프라인의 한계점과 개선 방향을 분석 보고서에 기술한다.
source_ids:
- S1
- S2
---

## RAG(Retrieval-Augmented Generation) 아키텍처 개요

최신 자연어 처리(NLP) 및 딥러닝 모델은 방대한 텍스트 데이터를 학습하여 뛰어난 성능을 보이지만, 모델 학습 시점에 포함되지 않은 최신 정보나 특정 도메인의 비공개 데이터에 대해서는 환각(hallucination)을 보이거나 정보를 알지 못하는 한계가 있습니다 [S1].

### 검색을 통한 LLM의 한계 극복
RAG는 모델이 모든 지식을 매개변수(parameter) 내부에 암기하게 하는 대신, 질문과 관련된 외부의 신뢰할 수 있는 문서를 '적절한 시점(just-in-time)'에 검색하여 생성 단계의 입력으로 제공하는 방식입니다 [S2].

### 핵심 구성 요소
1. **검색기(Retriever)**: 사용자의 질의(query)를 받아 벡터 데이터베이스 등에서 관련성이 높은 문서 조각(chunk)을 식별합니다.
2. **증강(Augmentation)**: 검색된 문서와 원래 질문을 조합하여 LLM에 전달할 프롬프트를 구성합니다.
3. **생성기(Generator)**: 증강된 정보를 바탕으로 사실 기반의 응답을 생성합니다.

이러한 구조는 모델의 지식을 최신 상태로 유지하고, 생성된 답변의 근거를 추적 가능하게 함으로써 신뢰성을 확보하는 데 기여합니다.
