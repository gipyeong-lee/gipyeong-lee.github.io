---
layout: learn-module
title: 전환 우선순위 보고서 작성
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab
course_locale: ko
lang: ko
ref: learn:post-quantum-cryptography-migration-lab:migration-roadmap
translations:
- lang: ko
  url: /learn/post-quantum-cryptography-migration-lab/migration-roadmap/
- lang: en
  url: /learn/en/post-quantum-cryptography-migration-lab/migration-roadmap/
- lang: ja
  url: /learn/ja/post-quantum-cryptography-migration-lab/migration-roadmap/
- lang: zh-cn
  url: /learn/zh-cn/post-quantum-cryptography-migration-lab/migration-roadmap/
- lang: zh-tw
  url: /learn/zh-tw/post-quantum-cryptography-migration-lab/migration-roadmap/
module_id: m8
permalink: /learn/post-quantum-cryptography-migration-lab/migration-roadmap/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e5164bbefc324eff94b7957c62695f66
primary_category: ai-software
topics:
- post-quantum-cryptography
- cryptographic-inventory
- ml-kem
- ml-dsa
- crypto-agility
course_type: academic
published_at: '2026-10-16T00:55:40.127560+09:00'
id: m8
slug: migration-roadmap
phase_id: p3
estimated_hours: 8.0
prerequisites:
- m7
objectives:
- 포스트퀀텀 암호(PQC) 전환을 위한 위험 및 비즈니스 영향 분석 프레임워크 이해
- 암호 자산 인벤토리 데이터를 기반으로 전환 우선순위 결정
- 암호 민첩성(Cryptographic Agility) 확보를 위한 기술적 전략 수립
- 최종 전환 로드맵 및 검증 보고서 구조화
worked_examples:
- '예시 1: 데이터 생명주기 기반 우선순위 산정 - 20년 보존되는 인적 정보 데이터베이스는 5년 보존되는 로그 데이터보다 PQC 전환 우선순위가
  높게 평가됨.'
- '예시 2: 하이브리드 TLS 구성 사례 - 기존 ECDH와 ML-KEM을 결합하여, 두 알고리즘 중 하나만 안전해도 통신 기밀성이 유지되도록
  설계하는 하이브리드 모델 분석.'
lab:
  title: 전환 로드맵 시뮬레이션
  steps:
  - 이전 모듈에서 작성한 인벤토리 CSV 데이터를 로드합니다.
  - 각 자산에 대해 [위험성 * 중요도 * 수명] 점수를 산출하는 Python 스크립트를 작성합니다.
  - 우선순위 상위 3개 자산에 대한 하이브리드 구현 계획을 세웁니다.
  - 전환 시 발생할 수 있는 호환성 문제와 대응책(Fall-back 전략)을 기술합니다.
  safety:
  - 모든 계산 및 분석은 독립된 격리 가상 환경에서만 수행합니다.
  - 운영 서버의 실제 암호 구성을 변경하지 않습니다.
  - 실제 키 자료가 포함되지 않도록 분석 노트북을 검토합니다.
  deliverables:
  - 우선순위가 매겨진 인벤토리 CSV 분석본
  - 전환 계획이 포함된 기술 결정 의사결정표
assignment:
  title: PQC 전환 우선순위 보고서
  deliverables:
  - 암호 민첩성 분석 보고서 (PDF)
  - 위험 등급 기반 전환 로드맵 (표 포함)
  rubric:
  - 데이터 수명 및 노출 위험에 기반한 타당한 우선순위 논리
  - 하이브리드 암호 체계 도입을 통한 암호 민첩성 고려
  - 전환 계획의 단계별 실행 가능성
  - 실험 결과 및 데이터 인벤토리와의 정합성
quiz:
- question: 암호 전환 우선순위를 결정할 때 가장 고려해야 할 데이터 특성은 무엇입니까?
  choices:
  - 데이터가 사용되는 프로그래밍 언어
  - 데이터의 보안 필요 수명(Data Shelf Life)
  - 시스템의 개발자 수
  - 최신 데이터 저장소의 용량
  answer_index: 1
  explanation: 양자 위협은 데이터가 미래에 해독될 위험을 내포하므로, 오랫동안 기밀이 유지되어야 하는 데이터가 가장 우선적으로 PQC
    전환이 필요합니다.
- question: 암호 민첩성(Cryptographic Agility)을 위해 권장되는 소프트웨어 설계 방식은 무엇입니까?
  choices:
  - 하드코딩된 암호 알고리즘 사용
  - 암호화 모듈과 비즈니스 로직의 추상화 분리
  - 단일 알고리즘만 사용하는 폐쇄형 구조
  - 운영체제 수준의 암호 라이브러리 직접 참조
  answer_index: 1
  explanation: 암호 엔진과 로직을 분리하여 알고리즘 교체 시 코드 변경을 최소화하는 구조가 암호 민첩성 확보의 핵심입니다.
completion_criteria:
- 전환 우선순위가 명시된 인벤토리 분석 파일 제출
- 암호 민첩성 고려사항이 포함된 전환 로드맵 보고서 작성
- 모든 실습 코드 및 측정값이 포함된 재현 패키지 완료
source_ids:
- S1
---

### 전환 우선순위 전략 (Migration Prioritization Strategy)

NIST 포스트퀀텀 표준(ML-KEM, ML-DSA)으로의 전환은 시스템 전반의 암호 자산 평가에서 시작됩니다. 전환 우선순위는 단순히 알고리즘의 노후화 정도가 아니라, 데이터의 수명(Data Shelf Life), 암호 노출 위험, 그리고 시스템의 전략적 중요도에 따라 결정됩니다 [S1].

#### 1. 암호 자산 평가 기준 (Assessment Criteria)
전환 시급성을 판단하기 위해 다음 기준을 활용합니다:
- **데이터 보안 수명:** 암호화된 데이터가 미래 양자 컴퓨터에 의해 해독되었을 때 미치는 영향(예: 10년 이상 기밀 유지 필요 데이터).
- **시스템 민첩성:** 현재 구현된 암호가 하드코딩되었는지, 구성 파일(Config)을 통해 알고리즘 교체가 가능한지 여부.
- **기술 부채:** 해당 암호 모듈을 사용하는 종속성(Dependency) 및 유지보수 가능 여부.

#### 2. 암호 민첩성 확보
전환 로드맵의 핵심은 알고리즘 교체 시 코드 변경을 최소화하는 것입니다. 추상화 레이어(Abstraction Layer)를 사용하여 비즈니스 로직과 암호 엔진을 분리하고, 하이브리드 키 교환 방식을 통해 기존 알고리즘의 안정성과 PQC의 양자 저항성을 동시에 확보하는 전략이 권장됩니다.
