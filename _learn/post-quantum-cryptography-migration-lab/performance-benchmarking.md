---
layout: learn-module
title: 성능 평가 및 벤치마킹
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab
course_locale: ko
lang: ko
ref: learn:post-quantum-cryptography-migration-lab:performance-benchmarking
translations:
- lang: ko
  url: /learn/post-quantum-cryptography-migration-lab/performance-benchmarking/
- lang: en
  url: /learn/en/post-quantum-cryptography-migration-lab/performance-benchmarking/
- lang: ja
  url: /learn/ja/post-quantum-cryptography-migration-lab/performance-benchmarking/
- lang: zh-cn
  url: /learn/zh-cn/post-quantum-cryptography-migration-lab/performance-benchmarking/
- lang: zh-tw
  url: /learn/zh-tw/post-quantum-cryptography-migration-lab/performance-benchmarking/
module_id: m6
permalink: /learn/post-quantum-cryptography-migration-lab/performance-benchmarking/
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
id: m6
slug: performance-benchmarking
phase_id: p3
estimated_hours: 8.0
prerequisites:
- m5
objectives:
- 포스트퀀텀 암호 알고리즘(ML-KEM)의 성능 평가 지표(시간, 메모리, 처리량)를 이해한다.
- TLS 1.3 핸드셰이크 과정에서 KEM 연산이 성능에 미치는 영향을 분석한다.
- Liboqs 및 oqs-provider 프레임워크를 활용하여 하이브리드 암호 모드의 성능을 벤치마킹한다.
worked_examples:
- '예제 1: Liboqs를 사용한 단일 KEM 연산 벤치마킹

  Python 스크립트를 통해 `ML-KEM-768`의 `keypair`, `encaps`, `decaps` 동작 시간을 `timeit` 모듈로
  측정하고 결과를 CSV로 저장하는 방법입니다.'
- '예제 2: 하이브리드 TLS 1.3 핸드셰이크 처리량 측정

  oqs-provider가 적용된 로컬 서버/클라이언트 환경에서 `s_client`와 `s_server`를 사용하여 100회 연결 시 소요되는 총
  시간을 측정하여 초당 핸드셰이크 수(TPS)를 산출하는 분석 절차입니다.'
lab:
  title: PQC 성능 벤치마킹 실습
  steps:
  - 격리된 개발 환경에서 liboqs 및 oqs-provider를 설치하고 환경 설정을 확인한다.
  - 벤치마킹용 Python 스크립트를 작성하여 ML-KEM 알고리즘의 연산 시간을 측정한다.
  - Wireshark를 실행하여 TLS 핸드셰이크 패킷을 캡처하고, 하이브리드 모드 시 데이터 크기 변화를 분석한다.
  - 측정된 데이터를 기반으로 연산 시간과 처리량 지표를 그래프화한다.
  safety:
  - 실험은 로컬 격리 환경 내에서만 수행하며 실제 운영 환경의 인증서나 키를 절대 사용하지 않는다.
  - 벤치마킹 과정에서 높은 CPU 부하가 발생할 수 있으므로 시스템 리소스를 모니터링한다.
  - 실제 비밀값이나 키 데이터를 캡처 파일에 포함하지 않도록 주의한다.
  deliverables:
  - 연산 성능 측정 스크립트(.py)
  - 측정 결과 CSV 데이터
  - 알고리즘별 성능 비교 분석 보고서(.md 또는.ipynb)
assignment:
  title: 암호 민첩성 기반 성능 평가 보고서
  deliverables:
  - 알고리즘 선택 이유 및 보안/성능 트레이드오프 분석
  - 벤치마킹 데이터 시각화 자료
  - 성능 결과를 바탕으로 한 전환 로드맵 수정안
  rubric:
  - 벤치마킹 데이터가 재현 가능하고 독립된 환경에서 측정되었는가?
  - 성능 저하의 기술적 원인(키 크기, 연산 복잡도)을 정확히 분석했는가?
  - 하이브리드 모드의 이점과 비용을 균형 있게 논의했는가?
quiz:
- question: TLS 1.3 핸드셰이크 성능에서 가장 중요한 PQC 알고리즘 관련 요소는?
  choices:
  - 대칭키 암호 알고리즘의 블록 크기
  - KEM의 키 생성 및 캡슐화 연산 시간
  - 해시 알고리즘의 종류
  - 서버의 운영체제 종류
  answer_index: 1
  explanation: TLS 1.3 핸드셰이크 성능은 KEM 알고리즘의 연산 효율성에 크게 좌우됩니다 [S2].
- question: 성능 평가 시 하이브리드 모드를 사용하는 주된 이유는?
  choices:
  - 전통적인 알고리즘보다 항상 빠르기 때문에
  - PQC의 보안 위협에 대비하면서 보안성을 유지하기 위해
  - 네트워크 대역폭을 줄이기 위해
  - 연산 리소스를 최소화하기 위해
  answer_index: 1
  explanation: 하이브리드 모드는 PQC의 미래 보안성과 전통적 알고리즘의 검증된 보안성을 결합하여 점진적 전환을 가능하게 합니다.
completion_criteria:
- 벤치마킹 스크립트 실행 및 결과 데이터 확보 완료
- 성능 평가 보고서 제출 및 통과
- TLS 하이브리드 모드 성능 분석 완료
source_ids:
- S2
---

## 성능 평가 및 벤치마킹

포스트퀀텀 암호(PQC)로의 전환은 단순히 알고리즘을 교체하는 것이 아니라, 기존 네트워크 프로토콜(예: TLS 1.3)의 성능과 직결되는 문제입니다. 특히 KEM(Key Encapsulation Mechanism) 연산은 핸드셰이크의 지연 시간(latency)과 서버의 초당 연결 처리량(handshakes per second)에 직접적인 영향을 미칩니다 [S2].

### 성능 지표
1. **연산 시간(Computation Time):** 키 생성(KeyGen), 캡슐화(Encaps), 역캡슐화(Decaps) 각각에 소요되는 CPU 사이클 또는 시간(ms).
2. **데이터 크기:** 공개키 및 캡슐화된 텍스트(ciphertext)의 크기. 이는 네트워크 대역폭 소비와 단편화 발생 가능성을 결정합니다.
3. **처리량(Throughput):** 초당 처리 가능한 핸드셰이크 수. 최적화된 구현(예: AVX-512 활용)은 폴리노미얼 곱셈 및 모듈러 연산 속도를 높여 처리량을 크게 개선할 수 있습니다 [S2].

### 하이브리드 모드
전환기에는 전통적인 알고리즘(ECDH)과 PQC(ML-KEM)를 함께 사용하는 하이브리드 접근법이 권장됩니다. 이는 PQC의 잠재적 취약성에 대비하면서도 PQC의 보안 이점을 확보하기 위함입니다. 하이브리드 모드는 연산 복잡도가 증가하므로 성능 저하를 면밀히 평가해야 합니다 [S2].
