---
layout: learn-module
title: Hybrid TLS 핸드셰이크 분석
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab
course_locale: ko
lang: ko
ref: learn:post-quantum-cryptography-migration-lab:hybrid-tls-analysis
translations:
- lang: ko
  url: /learn/post-quantum-cryptography-migration-lab/hybrid-tls-analysis/
- lang: en
  url: /learn/en/post-quantum-cryptography-migration-lab/hybrid-tls-analysis/
- lang: ja
  url: /learn/ja/post-quantum-cryptography-migration-lab/hybrid-tls-analysis/
- lang: zh-cn
  url: /learn/zh-cn/post-quantum-cryptography-migration-lab/hybrid-tls-analysis/
- lang: zh-tw
  url: /learn/zh-tw/post-quantum-cryptography-migration-lab/hybrid-tls-analysis/
module_id: m7
permalink: /learn/post-quantum-cryptography-migration-lab/hybrid-tls-analysis/
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
id: m7
slug: hybrid-tls-analysis
phase_id: p3
estimated_hours: 8.0
prerequisites:
- m6
objectives:
- 양자 위협 환경에서 TLS 1.3의 취약성을 설명한다.
- ML-KEM 기반 하이브리드(Hybrid) TLS 핸드셰이크 구조를 이해한다.
- OQS(Open Quantum Safe) 기반 로컬 환경에서 하이브리드 모드 성능을 측정한다.
- 패킷 캡처를 통해 기존 알고리즘과 PQ 알고리즘이 결합된 핸드셰이크 과정을 분석한다.
worked_examples:
- '예제 1: 하이브리드 키 교환 과정 - 클라이언트는 고전적 공유 비밀 값과 PQC 캡슐화 결과값을 서버에 전송합니다. 서버는 역캡슐화 후 두
  공유 비밀을 KDF(Key Derivation Function)에 결합하여 세션키를 생성합니다.'
- '예제 2: 핸드셰이크 지연 분석 - PQ 알고리즘 적용 시 추가적인 키 크기(Key Size)가 증가함에 따라 네트워크 전송 시간이 늘어나는
  현상을 비교 분석합니다. 성능 최적화(예: AVX-512 사용) 적용 전후의 핸드셰이크 당 처리량(Handshakes per second) 차이를
  수치화합니다[S2].'
lab:
  title: OQS 기반 하이브리드 TLS 핸드셰이크 재현 실험
  steps:
  - 격리된 Docker 환경에서 liboqs 및 oqs-provider가 통합된 OpenSSL 3 빌드 환경을 구축한다.
  - '기존 ECDH 모드와 ML-KEM 기반 하이브리드 모드(예: secp256r1_mlkem768)를 설정한다.'
  - 로컬 루프백(Loopback) 인터페이스를 사용하여 두 모드 간 TLS 1.3 핸드셰이크를 실행한다.
  - Wireshark를 사용하여 ClientHello 및 ServerHello 메시지 내의 키 교환 데이터 필드를 패킷 캡처한다.
  - 실행 시간 측정 스크립트를 사용하여 100회 이상의 핸드셰이크 평균 시간을 측정하고, 하이브리드 모드의 오버헤드를 기록한다.
  safety:
  - 본 실험은 로컬 환경의 격리된 루프백 인터페이스에서만 수행하며 외부 네트워크 트래픽을 생성하지 않는다.
  - 실제 인증서, 개인키, 사용자 데이터 등 운영 보안 자산을 절대 사용하지 않는다.
  - 학습용 OQS 라이브러리는 실험적 도구이므로 실제 운영 보안 서비스에 사용하지 않는다.
  - 실험 종료 시 모든 생성된 임시 키와 로컬 측정 데이터를 삭제한다.
  deliverables:
  - 설정 및 실행 로그 파일
  - Wireshark 패킷 캡처 파일(.pcapng) 및 키 교환 필드 분석 노트
  - 핸드셰이크 성능 비교 측정 CSV 데이터
assignment:
  title: TLS 1.3 하이브리드 전환 성능 분석 보고서
  deliverables:
  - 핸드셰이크 지연 시간 비교 분석 그래프 및 데이터 시각화
  - 하이브리드 모드 패킷 분석 및 키 교환 알고리즘 특징 요약
  - 운영 환경 적용 시 예상되는 성능 및 보안 고려사항 의사결정표
  rubric:
  - 실험의 재현 가능성(환경 설정 및 스크립트 명시 여부)
  - 패킷 분석의 정확성(키 교환 필드 식별)
  - 성능 측정 데이터의 논리적 해석
  - 이론적 보안 가정과 실험 결과의 연결성
quiz:
- question: 하이브리드 TLS 핸드셰이크의 주된 보안적 이점은 무엇입니까?
  choices:
  - 핸드셰이크 단계를 획기적으로 줄여 속도를 높인다.
  - 고전적 알고리즘과 PQC 알고리즘 중 하나만 안전해도 비밀성을 유지한다.
  - 네트워크 전송 비용을 완전히 제거한다.
  - 인증서 관리의 복잡도를 낮춘다.
  answer_index: 1
  explanation: 하이브리드 모드는 기존 알고리즘과 PQC 알고리즘의 결과를 결합하여, 두 알고리즘 중 하나만 안전해도 보안이 유지되도록
    설계된 전환기 전략입니다.
- question: TLS 1.3 핸드셰이크 성능에 가장 큰 영향을 미치는 PQ 알고리즘 요소는 무엇입니까?
  choices:
  - 네트워크 레이턴시만 고려한다.
  - KEM(키 캡슐화 메커니즘)의 키 생성, 캡슐화, 역캡슐화 연산 비용
  - 서버의 디스크 I/O 속도
  - 클라이언트의 브라우저 버전
  answer_index: 1
  explanation: KEM 알고리즘의 계산 비용은 TLS 1.3 핸드셰이크 성능과 직결되며, 이를 최적화하는 것이 성능 개선의 핵심입니다[S2].
completion_criteria:
- 로컬 환경에서 liboqs 기반 하이브리드 TLS 핸드셰이크 재현 성공
- Wireshark 분석을 통해 하이브리드 키 교환 메시지 확인
- 성능 측정 데이터 기반의 결과 분석 보고서 제출
- 안전 제약 사항(데이터 격리, 운영 키 미사용) 준수 확인
source_ids:
- S2
---

### 하이브리드 TLS 핸드셰이크 이론

현행 TLS 1.3은 ECDH(Elliptic Curve Diffie-Hellman)와 같은 고전적 공개키 암호에 의존하며, 이는 충분한 성능의 양자 컴퓨터가 등장할 경우 공격 위협에 노출된다[S2]. 이에 대한 대응으로 NIST 표준인 ML-KEM(Module-Lattice-Based Key-Encapsulation Mechanism)과 같은 포스트퀀텀 암호(PQC)를 통합하는 연구가 활발하다[S2].

#### 하이브리드 모드의 보안 가정
완전한 PQC 전환 이전에 운영 안정성을 위해 고전적 알고리즘과 PQ 알고리즘을 결합한 '하이브리드(Hybrid) 모드'를 사용한다. 이 방식은 두 알고리즘의 공유 비밀(Shared Secret)을 결합하여, 두 알고리즘 중 하나만 안전해도 통신의 비밀성을 보장하도록 설계한다.

#### 성능 고려사항
TLS 1.3 핸드셰이크 성능은 KEM의 계산 비용에 직접적으로 의존한다[S2]. 특히 키 생성(Key Generation), 캡슐화(Encapsulation), 역캡슐화(Decapsulation) 단계에서의 연산 효율성이 전체 핸드셰이크 속도를 결정한다. 최근에는 AVX-512와 같은 명령어 집합 최적화를 통해 다항식 곱셈과 모듈러 축소 과정을 가속화하여 핸드셰이크 성능을 높이는 기법이 적용되고 있다[S2].
