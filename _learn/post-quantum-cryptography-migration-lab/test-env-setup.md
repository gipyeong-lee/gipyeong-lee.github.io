---
layout: learn-module
title: 격리된 실험 환경 구축
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab
course_locale: ko
lang: ko
ref: learn:post-quantum-cryptography-migration-lab:test-env-setup
translations:
- lang: ko
  url: /learn/post-quantum-cryptography-migration-lab/test-env-setup/
- lang: en
  url: /learn/en/post-quantum-cryptography-migration-lab/test-env-setup/
- lang: ja
  url: /learn/ja/post-quantum-cryptography-migration-lab/test-env-setup/
- lang: zh-cn
  url: /learn/zh-cn/post-quantum-cryptography-migration-lab/test-env-setup/
- lang: zh-tw
  url: /learn/zh-tw/post-quantum-cryptography-migration-lab/test-env-setup/
module_id: m4
permalink: /learn/post-quantum-cryptography-migration-lab/test-env-setup/
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
id: m4
slug: test-env-setup
phase_id: p2
estimated_hours: 8.0
prerequisites:
- m3
objectives:
- 포스트퀀텀 암호(PQC) 실험을 위한 격리된 로컬 개발 환경의 구성 원리와 필수 도구(liboqs, oqs-provider)의 역할을 이해한다.
- TLS 1.3과 같은 프로토콜에서 KEM 성능이 핸드셰이크 지연 시간에 미치는 영향을 분석한다.
- Docker 컨테이너를 사용하여 의존성이 고정된 재현 가능한 실험 환경을 설계하고 구축한다.
worked_examples:
- '예제 1: Dockerfile을 활용한 oqs-provider 기반 환경 구축. 각 라이브러리의 버전을 명시하여 빌드 재현성을 확보하는 방식
  설명.'
- '예제 2: OpenSSL CLI를 이용한 하이브리드 TLS 핸드셰이크 테스트. ''openssl s_server''와 ''s_client''를
  사용하여 ML-KEM-768 지원 하이브리드 TLS 1.3 연결 시뮬레이션 방법.'
lab:
  title: 격리된 PQC 테스트베드 구축
  steps:
  - 실험용 Docker 컨테이너 이미지 베이스(Ubuntu 22.04 LTS 이상) 준비.
  - liboqs 및 oqs-provider 소스 코드를 복제(clone)하고 특정 커밋 해시를 체크아웃하여 버전 고정.
  - 'CMake를 사용하여 liboqs 컴파일 시, 최적화 수준(예: AVX2)을 설정하고 빌드 수행.'
  - OpenSSL 3.x 환경 설정 및 oqs-provider 활성화.
  - 로컬 네트워크 인터페이스에 고정된 루프백 연결을 통해 기본 TLS 1.3 핸드셰이크 성능 기준 측정.
  safety:
  - 실험용 환경은 반드시 로컬 격리된 컨테이너 내에서만 실행한다.
  - 운영 환경의 인증서, 실제 개인키, 고객 데이터는 절대 컨테이너 내로 반입하지 않는다.
  - 컴파일 및 실행 과정에서 생성된 측정값은 공개 테스트 데이터로 간주하며, 실제 보안 정책과는 무관함에 유의한다.
  - 실제 하드웨어나 전력 모니터링 시, 제조사가 명시한 정격 전류 및 전압 범위를 준수한다.
  deliverables:
  - 의존성 버전이 고정된 Dockerfile 및 빌드 로그.
  - OpenSSL에서 PQC 알고리즘 목록을 성공적으로 불러왔음을 보여주는 터미널 캡처.
  - 환경 설정이 완료된 격리된 개발 환경의 체크섬(SHA-256).
assignment:
  title: PQC 테스트베드 문서화 및 평가
  deliverables:
  - 구축한 테스트베드의 구성도와 선택한 알고리즘 버전 명세서.
  - 테스트베드 환경에서 고전 알고리즘과 하이브리드 ML-KEM 알고리즘의 핸드셰이크 시간 비교 데이터 CSV.
  - 격리된 환경 유지를 위한 보안 정책 보고서.
  rubric:
  - 의존성 버전 고정 및 빌드 재현 가능 여부 (30%)
  - 격리된 실험 환경에서의 하이브리드 TLS 핸드셰이크 성공 여부 (40%)
  - 알고리즘 구성 및 측정 절차의 명확성과 보안 준수 (30%)
quiz:
- question: oqs-provider의 주된 역할은 무엇인가요?
  choices:
  - PQC 알고리즘을 하드웨어 수준에서 가속화한다.
  - OpenSSL 3에서 포스트퀀텀 알고리즘을 TLS 프로토콜 등에 사용할 수 있도록 연결하는 인터페이스 역할을 한다.
  - 운영 환경의 보안 인증서를 자동으로 갱신한다.
  - 양자 컴퓨터의 공격 벡터를 차단한다.
  answer_index: 1
  explanation: oqs-provider는 OpenSSL 프로바이더 아키텍처를 사용하여 PQC 알고리즘을 표준 라이브러리에 통합하고, 이를
    통해 기존 응용 프로그램이 PQC 알고리즘을 사용할 수 있게 합니다.
- question: 격리된 실험 환경에서 버전을 고정(Locking)해야 하는 이유는 무엇인가요?
  choices:
  - 최신 버전이 항상 더 빠르기 때문이다.
  - 재현성을 보장하고 연구자 간의 실행 환경 차이로 인한 측정 오차를 줄이기 위해서이다.
  - 운영 보안을 강화하기 위해서이다.
  - 빌드 시간을 단축하기 위해서이다.
  answer_index: 1
  explanation: 버전 고정은 동일한 환경을 재현 가능하게 하여, 성능 측정 값의 무결성과 연구의 객관성을 확보하는 데 필수적입니다.
completion_criteria:
- Docker 기반의 격리된 빌드 환경 구성 성공.
- oqs-provider를 통한 ML-KEM 하이브리드 모드 시연 완료.
- 실험 데이터 측정 및 보안 정책이 포함된 보고서 제출.
source_ids:
- S2
---

### 격리된 PQC 실험 환경의 필요성
양자 컴퓨터의 위협으로부터 기존 공개키 암호(RSA, ECDH 등)를 보호하기 위해 NIST는 ML-KEM(Kyber 기반) 및 ML-DSA(Dilithium 기반)와 같은 포스트퀀텀 알고리즘을 표준화했습니다. 이러한 알고리즘의 성능과 보안성을 로컬 환경에서 평가하려면 **암호 민첩성(Crypto-agility)**을 갖춘 재현 가능한 환경이 필수적입니다 [S2].

#### 1. 주요 구성 요소
*   **liboqs**: PQC 알고리즘을 C로 구현한 라이브러리로, 다양한 KEM 및 서명 알고리즘을 테스트할 수 있는 기반을 제공합니다.
*   **oqs-provider**: OpenSSL 3의 프로바이더 아키텍처를 사용하여 PQC 알고리즘을 기존 TLS 인프라에 통합하게 해주는 인터페이스입니다.
*   **하이브리드 모드**: 기존 고전 암호(ECDH)와 PQC 알고리즘을 결합하여, PQC 라이브러리의 잠재적 취약성에도 불구하고 기존 보안 수준을 유지하는 전환기 전략입니다 [S2].

#### 2. 실험 환경의 핵심: 격리 및 재현성
실험은 운영 환경과 완전히 분리되어야 합니다. Docker와 같은 컨테이너 기술을 사용하여 의존성 버전을 고정(Locking)하면, 연구자 간의 실행 결과 차이를 줄이고 알고리즘 최적화(예: AVX-512 활용) 효과를 정확히 측정할 수 있습니다 [S2]. 핸드셰이크 성능 평가 시에는 고정된 하드웨어와 격리된 네트워크를 사용하여 지연 시간의 불확실성을 최소화해야 합니다.
