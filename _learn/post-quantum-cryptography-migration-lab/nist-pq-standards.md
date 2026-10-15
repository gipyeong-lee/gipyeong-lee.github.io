---
layout: learn-module
title: ML-KEM 및 ML-DSA 표준 이해
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab
course_locale: ko
lang: ko
ref: learn:post-quantum-cryptography-migration-lab:nist-pq-standards
translations:
- lang: ko
  url: /learn/post-quantum-cryptography-migration-lab/nist-pq-standards/
- lang: en
  url: /learn/en/post-quantum-cryptography-migration-lab/nist-pq-standards/
- lang: ja
  url: /learn/ja/post-quantum-cryptography-migration-lab/nist-pq-standards/
- lang: zh-cn
  url: /learn/zh-cn/post-quantum-cryptography-migration-lab/nist-pq-standards/
- lang: zh-tw
  url: /learn/zh-tw/post-quantum-cryptography-migration-lab/nist-pq-standards/
module_id: m2
permalink: /learn/post-quantum-cryptography-migration-lab/nist-pq-standards/
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
id: m2
slug: nist-pq-standards
phase_id: p1
estimated_hours: 8.0
prerequisites:
- m1
objectives:
- 격자 기반 암호 체계(Lattice-based cryptography)의 수학적 기초와 안정성 근거를 설명한다.
- NIST 표준 ML-KEM(키 캡슐화 메커니즘)의 동작 원리를 이해한다.
- NIST 표준 ML-DSA(디지털 서명 알고리즘)의 구조적 특성을 파악한다.
- 격자 암호가 타 암호 방식(코드 기반, 해시 기반) 대비 실무적 이점을 갖는 이유를 분석한다.
worked_examples:
- '예제 1: 격자 기반 KEM의 보안 강도 비교. ML-KEM-512, 768, 1024는 각각 NIST 보안 강도 1, 3, 5 레벨에 대응한다.
  이는 고전적 암호의 AES-128, 192, 256과 유사한 보안 수준을 목표로 한다.'
- '예제 2: 모듈 격자(Module Lattice) 개념 적용. 벡터와 행렬을 사용하여 연산을 효율화함으로써, 일반 격자보다 성능은 최적화하되
  보안 강도는 유지한다.'
lab:
  title: ML-KEM 및 ML-DSA 알고리즘 기초 실험
  steps:
  - liboqs를 설치하고 환경 변수를 설정한다.
  - 샘플 Python 코드를 사용하여 ML-KEM 키 쌍 생성 및 캡슐화 과정을 실행한다.
  - ML-DSA를 사용하여 메시지에 서명하고 검증하는 스크립트를 수행한다.
  - 각 연산에 소요되는 시간을 측정하여 기록한다.
  safety:
  - 실험용 가상 환경 외의 시스템 인증서나 실제 키 파일에 접근하지 않는다.
  - liboqs 라이브러리는 연구 및 테스트 용도로만 사용하며 운영 환경 보안 솔루션으로 오해하지 않는다.
  - 실험 데이터는 모두 로컬 가상 환경에 유지하며 외부 네트워크로 전송하지 않는다.
  deliverables:
  - 연산 시간 측정 데이터가 담긴 CSV 파일
  - 알고리즘 구현체 실행 결과 캡처
  - 실습 과정 요약 로그
assignment:
  title: 포스트퀀텀 암호 표준 분석 보고서
  deliverables:
  - ML-KEM과 ML-DSA의 알고리즘적 특징 요약 표
  - 격자 기반 시스템이 실제 전환 시 고려해야 할 성능적 제약(키 크기 등) 분석
  - 연구용 라이브러리를 활용한 테스트의 한계점 기술
  rubric:
  - 표준 알고리즘의 수학적 근거를 정확히 기술했는가?
  - 격자 기반 시스템의 이점과 한계를 분석했는가?
  - 보안 위협 모델에 대한 올바른 이해를 보여주는가?
quiz:
- question: 다음 중 격자 기반 시스템이 실무 표준화를 주도하는 주된 이유는 무엇인가?
  choices:
  - 가장 짧은 보안 이력을 가지고 있기 때문
  - 최악의 사례에서 평균적인 사례로의 환산이 가능하며 효율적 구현이 가능하기 때문
  - 양자 알고리즘으로 쉽게 풀릴 수 있기 때문
  - 오직 코드 기반의 암호만을 사용하여 보안을 극대화하기 때문
  answer_index: 1
  explanation: 격자 기반 시스템은 강력한 수학적 환산 근거와 효율적인 구현 가능성으로 인해 NIST 표준화의 중심에 있습니다 [S4].
- question: ML-KEM이 기반으로 하는 수학적 문제 유형은 무엇인가?
  choices:
  - 소인수 분해 문제
  - 타원 곡선 이산 대수 문제
  - 모듈 학습 오차 문제(MLWE)
  - 해시 충돌 문제
  answer_index: 2
  explanation: ML-KEM은 모듈 격자 기반의 학습 오차(MLWE) 문제를 안전성의 근거로 합니다.
completion_criteria:
- 이론 학습 확인용 퀴즈를 모두 정답으로 통과할 것
- 실험 과정 및 측정 데이터가 포함된 보고서를 제출할 것
- 실습 안전 지침을 준수하고 격리된 환경에서 테스트를 수행했음을 확인한 체크리스트 제출
source_ids:
- S4
---

## ML-KEM 및 ML-DSA 표준 이해

### 1. 격자 기반 암호의 부상
현재 실무적 표준화를 주도하는 것은 격자 기반(Lattice-based) 시스템이다. 이는 최악의 사례(worst-case)에서 평균적인 사례(average-case)로의 강력한 수학적 환산(reductions)이 존재하며, 효율적인 구현이 가능하기 때문이다 [S4]. 반면, 코드 기반(Code-based)이나 해시 기반(Hash-based) 방식은 보수적인 닻(conservative anchors) 역할을 수행하며, 더 긴 보안 이력이나 최소한의 가정만을 요구하는 특성을 갖는다 [S4].

### 2. ML-KEM (Module-Lattice Key Encapsulation Mechanism)
ML-KEM은 이전에 Kyber로 알려졌던 알고리즘에 기반한다. 모듈 격자 문제(Module Learning With Errors, MLWE)를 기반으로 하며, 다음과 같은 흐름을 가진다.
- **KeyGen:** 모듈 격자 내에서 공개키와 비밀키를 생성.
- **Encapsulation:** 공개키를 사용하여 공유 비밀값(Shared Secret)과 캡슐화된 키(Ciphertext)를 생성.
- **Decapsulation:** 비밀키를 사용하여 캡슐화된 키로부터 원래의 공유 비밀값을 복구.

### 3. ML-DSA (Module-Lattice Digital Signature Algorithm)
ML-DSA는 Dilithium에 기반하며, 'Fiat-Shamir with Aborts' 기법을 사용한다. 격자 문제의 어려움을 통해 위조 저항성을 제공하며, 서명 크기와 공개키 크기 사이의 균형을 맞춘 실용적인 표준이다.

### 4. 보안 가정
격자 기반 시스템의 안전성은 가장 짧은 벡터를 찾는 문제(Shortest Vector Problem, SVP)와 밀접하게 연관되어 있다. 양자 컴퓨터의 '쇼어 알고리즘(Shor's Algorithm)'이 기존 RSA나 ECC를 효율적으로 깨는 것과 달리, 격자 문제는 양자 알고리즘으로도 다항 시간 내에 풀리지 않는다고 가정한다.
