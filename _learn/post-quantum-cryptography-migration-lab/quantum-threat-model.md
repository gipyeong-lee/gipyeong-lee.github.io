---
layout: learn-module
title: 양자 위협과 격자 기반 암호
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab
course_locale: ko
lang: ko
ref: learn:post-quantum-cryptography-migration-lab:quantum-threat-model
translations:
- lang: ko
  url: /learn/post-quantum-cryptography-migration-lab/quantum-threat-model/
- lang: en
  url: /learn/en/post-quantum-cryptography-migration-lab/quantum-threat-model/
- lang: ja
  url: /learn/ja/post-quantum-cryptography-migration-lab/quantum-threat-model/
- lang: zh-cn
  url: /learn/zh-cn/post-quantum-cryptography-migration-lab/quantum-threat-model/
- lang: zh-tw
  url: /learn/zh-tw/post-quantum-cryptography-migration-lab/quantum-threat-model/
module_id: m1
permalink: /learn/post-quantum-cryptography-migration-lab/quantum-threat-model/
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
id: m1
slug: quantum-threat-model
phase_id: p1
estimated_hours: 8.0
prerequisites: []
objectives:
- 양자 컴퓨터가 현대 암호 체계(RSA, ECC)에 미치는 위협 모델을 이해한다.
- 격자 기반 암호(Lattice-based Cryptography)의 수학적 기초와 안정성 근거를 분석한다.
- NIST가 권고하는 포스트퀀텀 암호 표준(ML-KEM, ML-DSA)의 설계 원리를 학습한다.
- 격자 기반 알고리즘의 효율성 및 보안적 특성(worst-case hardness)을 기술한다.
worked_examples:
- '예제 1: 양자 컴퓨터가 RSA에 미치는 영향 분석 - RSA는 큰 수의 소인수 분해 난이도에 기반함. 쇼어 알고리즘은 n비트 정수를 소인수
  분해하는 복잡도를 지수 시간에서 다항 시간으로 줄임으로써 암호문을 즉시 해독함.'
- '예제 2: 격자 기반 난제(LWE) 개념 이해 - 비밀 벡터 s와 오류 e를 추가한 선형 방정식 시스템 A*s + e = t를 고려함. 격자
  기반 암호는 행렬 A와 결과 t로부터 s를 찾아내기 어렵다는 ''Learning With Errors'' 문제의 난이도에 기반함.'
lab:
  title: 격자 암호 기초 환경 구축 및 시각화
  steps:
  - 격리된 Linux/Docker 환경에서 Python 3 가상환경 생성
  - liboqs 라이브러리 설치 및 컴파일
  - 격자 기반 LWE 문제의 파라미터 변화에 따른 키 크기 및 연산 시간 수집 스크립트 작성
  - 데이터 분석 및 시각화 노트북 실행
  safety:
  - 모든 실험은 격리된 로컬 가상 환경 내에서 수행함
  - 실제 운영 인증서, 개인키, 고객 데이터 사용 절대 금지
  - 연구용 라이브러리를 실제 서비스 보안 수단으로 간주하지 말 것
  deliverables:
  - 환경 설정 로그 및 컴파일 결과물
  - 알고리즘 성능(키 크기, 시간) 비교 분석 데이터
  - 격자 기반 암호 특성 보고서
assignment:
  title: 양자 위협 분석 보고서 작성
  deliverables:
  - 양자 위협 모델 및 격자 기반 암호 이론 정리 문서
  - 주요 PQC 알고리즘(ML-KEM, ML-DSA) 비교표
  rubric:
  - 쇼어 알고리즘의 원리를 정확히 설명함
  - 격자 기반 암호의 최악의 경우 난제(worst-case hardness) 개념을 논리적으로 서술함
  - 제시된 소스 [S3, S4]를 바탕으로 현대 암호가 직면한 도전을 기술함
quiz:
- question: 쇼어 알고리즘(Shor's algorithm)이 기존 PKI에 주는 위협은 무엇인가?
  choices:
  - 모든 대칭키 암호를 무조건 해독한다.
  - 소인수 분해 및 이산 로그 문제를 다항 시간 내에 해결한다.
  - 해시 함수의 충돌 저항성을 완전히 제거한다.
  - 양자 컴퓨터의 처리 속도를 저하시킨다.
  answer_index: 1
  explanation: 쇼어 알고리즘은 RSA의 기반인 소인수 분해와 ECC의 기반인 이산 로그 문제를 다항 시간 내에 해결함으로써 기존의 공개키
    암호 체계를 위협합니다.
- question: 격자 기반 암호(Lattice-based Cryptography)가 유망한 이유는 무엇인가?
  choices:
  - 최악의 경우 난제를 평균적인 경우 난제로 환산할 수 있기 때문이다.
  - 모든 대칭키 암호보다 훨씬 빠르기 때문이다.
  - 양자 컴퓨터에서도 반드시 풀 수 없기 때문이다.
  - 컴퓨터 메모리를 전혀 사용하지 않기 때문이다.
  answer_index: 0
  explanation: 격자 기반 암호는 최악의 경우 난제(worst-case hardness)로부터 평균적인 경우(average-case)의
    보안을 보장하는 수학적 강점을 가지고 있습니다[S4].
completion_criteria:
- 이론 학습 완료 및 양자 위협 보고서 제출
- 실습 환경에서 liboqs를 이용한 기초 알고리즘 실행 성공
- 퀴즈 항목별 80% 이상의 정답률 달성
source_ids:
- S3
- S4
---

## 양자 위협 모델
현대 공개키 암호(PKI)는 주로 소인수 분해(RSA)와 이산 로그 문제(ECC)의 어려운 난제에 의존한다. 쇼어 알고리즘(Shor's algorithm)은 양자 컴퓨터를 사용하여 다항 시간 내에 이러한 문제를 해결할 수 있으며, 이는 사실상 현재의 모든 표준 PKI를 무력화함을 의미한다[S3].

## 격자 기반 암호 (Lattice-based Cryptography)
격자 기반 암호는 고차원 공간 내에서 격자(Lattice)의 기저 벡터로부터 특정 지점을 찾는 문제(예: SVP, LWE)를 난제로 사용한다. 이 문제들은 최악의 경우(worst-case)에도 풀기 어렵다는 것이 증명되어 있으며, 평균적인 경우(average-case)에도 보안이 보장된다[S4].

## 포스트퀀텀 표준 (ML-KEM/ML-DSA)
- **ML-KEM (Module-Lattice-based Key-Encapsulation Mechanism):** 키 캡슐화 메커니즘으로, 효율적인 구현과 함께 격자 기반 난제를 사용하여 양자 내성을 제공한다.
- **ML-DSA (Module-Lattice-based Digital Signature Algorithm):** 전자 서명 표준으로, 격자 기반 수학 구조를 사용하여 강력한 서명 무결성을 보장한다.
격자 기반 시스템은 현재 표준화 과정에서 강력한 worst-case to average-case 환산성과 효율적인 성능을 입증하여 PQC 전환의 중심이 되고 있다[S4].
