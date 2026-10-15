---
layout: learn-module
title: OQS 및 oqs-provider 통합
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab
course_locale: ko
lang: ko
ref: learn:post-quantum-cryptography-migration-lab:liboqs-integration
translations:
- lang: ko
  url: /learn/post-quantum-cryptography-migration-lab/liboqs-integration/
- lang: en
  url: /learn/en/post-quantum-cryptography-migration-lab/liboqs-integration/
- lang: ja
  url: /learn/ja/post-quantum-cryptography-migration-lab/liboqs-integration/
- lang: zh-cn
  url: /learn/zh-cn/post-quantum-cryptography-migration-lab/liboqs-integration/
- lang: zh-tw
  url: /learn/zh-tw/post-quantum-cryptography-migration-lab/liboqs-integration/
module_id: m5
permalink: /learn/post-quantum-cryptography-migration-lab/liboqs-integration/
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
id: m5
slug: liboqs-integration
phase_id: p2
estimated_hours: 8.0
prerequisites:
- m4
objectives:
- Open Quantum Safe(OQS) 아키텍처와 oqs-provider의 역할을 이해한다.
- TLS 1.3에서 PQ(Post-Quantum) 알고리즘이 통합되는 방식을 파악한다.
- 로컬 환경에서 하이브리드(Hybrid) TLS 핸드셰이크를 구성하고 검증한다.
- KEM 구현 최적화(AVX-512 등)가 실제 핸드셰이크 성능에 미치는 영향을 고찰한다.
worked_examples:
- '예제 1: oqs-provider가 OpenSSL에 로드되었는지 확인하려면 `openssl list -providers` 명령을 실행한다. 출력
  결과에 ''oqs'' 프로바이더가 포함되어야 한다.'
- '예제 2: 하이브리드 핸드셰이크 수행 시, `openssl s_client -groups kyber768_x25519...`와 같이 명령어 인자를
  통해 키 교환 그룹을 지정한다. 이는 ML-KEM(Kyber)과 고전적 Curve25519를 결합한 하이브리드 그룹이다.'
lab:
  title: 로컬 환경에서의 하이브리드 TLS 테스트
  steps:
  - 격리된 Docker 컨테이너 내에서 liboqs 및 oqs-provider를 빌드하고 설치한다.
  - OpenSSL 설정 파일(`openssl.cnf`)을 수정하여 oqs 프로바이더를 활성화한다.
  - 두 개의 터미널을 열어 하나는 `openssl s_server`, 다른 하나는 `openssl s_client`를 하이브리드 모드로 실행한다.
  - Wireshark를 사용하여 ClientHello 패킷에서 공유 키 그룹(Key Share)이 어떻게 전송되는지 캡처하고 분석한다.
  - 핸드셰이크 성공 여부와 세션 암호화 알고리즘 정보를 확인한다.
  safety:
  - 실험은 반드시 격리된 로컬 가상 환경 내에서만 수행한다.
  - 운영 서비스에 사용되는 인증서나 키는 절대로 사용하지 않는다.
  - Wireshark 캡처 시 실제 서비스 트래픽이 포함되지 않도록 주의한다.
  deliverables:
  - oqs-provider 활성화 확인 스크린샷
  - 하이브리드 핸드셰이크 로그 파일
  - Wireshark 캡처 패킷의 공유 키 그룹 분석 보고서
assignment:
  title: 암호 민첩성 기반 전환 분석 보고서
  deliverables:
  - TLS 핸드셰이크 성능 측정 결과 데이터(CSV)
  - 하이브리드 모드 사용 이유와 성능 저하에 대한 분석 에세이
  - 우선순위 기반 포스트퀀텀 전환 로드맵
  rubric:
  - OQS 도구 체인 빌드 및 실행 성공 여부
  - TLS 패킷 분석을 통해 하이브리드 모드 동작을 정확히 설명했는가
  - 성능 측정 데이터가 실험 환경과 버전 정보를 포함하고 재현 가능한가
  - 암호 민첩성의 개념을 기반으로 전환 로드맵이 논리적으로 작성되었는가
quiz:
- question: oqs-provider가 OpenSSL에서 담당하는 핵심 역할은 무엇인가?
  choices:
  - 네트워크 패킷을 암호화하는 하드웨어 가속기
  - OpenSSL이 liboqs의 PQC 알고리즘을 호출할 수 있게 해주는 계층
  - 인터넷에서 공개키 인증서를 발급하는 서비스
  - 양자 컴퓨터의 공격을 탐지하는 IDS 도구
  answer_index: 1
  explanation: oqs-provider는 OpenSSL의 프로바이더 구조를 통해 liboqs의 알고리즘을 OpenSSL 애플리케이션에서
    직접 사용할 수 있도록 연결해줍니다.
- question: TLS 1.3에서 '하이브리드 모드' 키 교환을 사용하는 주된 이유는 무엇인가?
  choices:
  - 성능을 100배 이상 높이기 위해
  - 단일 알고리즘 구현 오류나 미래 취약성에 대비하여 보안을 보장하기 위해
  - 모든 기존 클라이언트를 지원하기 위해
  - 양자 컴퓨터를 사용하여 핸드셰이크를 하기 위해
  answer_index: 1
  explanation: 하이브리드 모드는 고전적인 알고리즘과 PQC 알고리즘을 결합하여, 구현 결함이나 알려지지 않은 취약성에 대비하는 다층 방어
    전략입니다.
completion_criteria:
- oqs-provider 기반 로컬 테스트 환경 빌드 완료
- 하이브리드 TLS 핸드셰이크 성공 및 패킷 캡처 검증 완료
- 실험 결과와 분석이 포함된 보고서 작성 완료
- 포스트퀀텀 전환 로드맵 수립 완료
source_ids:
- S2
---

## OQS 및 oqs-provider 통합 이론

양자 컴퓨터의 위협으로부터 기존 데이터 전송을 보호하기 위해, NIST 표준 기반의 포스트퀀텀 알고리즘(PQC)을 TLS 1.3과 같은 기존 프로토콜에 통합하는 것이 필수적이다. OQS(Open Quantum Safe) 프로젝트는 이러한 통합을 가속화하기 위한 주요 프레임워크를 제공한다 [S2].

### 1. liboqs와 oqs-provider
- **liboqs**: PQC 알고리즘(ML-KEM, ML-DSA 등)의 C 언어 구현을 담은 핵심 라이브러리다. 다양한 알고리즘에 대한 통일된 API를 제공한다.
- **oqs-provider**: OpenSSL 3의 프로바이더 구조를 활용하여, OpenSSL 애플리케이션(예: `s_client`, `s_server`)이 liboqs의 PQC 알고리즘을 네이티브하게 사용하게 돕는 중간 계층이다. 이를 통해 수정 없이 기존 TLS 도구에서 PQC 기능을 테스트할 수 있다.

### 2. TLS 1.3의 PQ 통합 방식
TLS 1.3 핸드셰이크 과정에서 PQC KEM은 기존 키 교환(예: ECDH)을 대체하거나 보완한다.
- **PQ-only 모드**: PQC KEM만 사용하여 키를 교환한다.
- **하이브리드(Hybrid) 모드**: 기존 고전 알고리즘(ECDH)과 PQC 알고리즘을 결합한다. 이는 포스트퀀텀 안전성을 확보하는 동시에 고전적인 보안 보장을 유지하여, 알고리즘 구현 오류나 미래의 취약성으로부터 보호받으려는 전략이다.

### 3. 성능 고려사항
PQC KEM은 기존 알고리즘보다 키 크기나 계산량이 클 수 있어 핸드셰이크 성능에 직접적인 영향을 준다 [S2]. 최신 하드웨어 명령어 세트(AVX-512 등)를 사용하여 다항식 곱셈과 모듈러 축소 등을 최적화함으로써 핸드셰이크 속도를 향상시킬 수 있다 [S2].
