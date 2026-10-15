---
layout: learn-module
title: 암호 자산 식별 및 관리
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab
course_locale: ko
lang: ko
ref: learn:post-quantum-cryptography-migration-lab:crypto-inventory
translations:
- lang: ko
  url: /learn/post-quantum-cryptography-migration-lab/crypto-inventory/
- lang: en
  url: /learn/en/post-quantum-cryptography-migration-lab/crypto-inventory/
- lang: ja
  url: /learn/ja/post-quantum-cryptography-migration-lab/crypto-inventory/
- lang: zh-cn
  url: /learn/zh-cn/post-quantum-cryptography-migration-lab/crypto-inventory/
- lang: zh-tw
  url: /learn/zh-tw/post-quantum-cryptography-migration-lab/crypto-inventory/
module_id: m3
permalink: /learn/post-quantum-cryptography-migration-lab/crypto-inventory/
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
id: m3
slug: crypto-inventory
phase_id: p2
estimated_hours: 8.0
prerequisites:
- m2
objectives:
- 암호 자산 식별(Cryptographic Inventory)의 개념과 필요성을 설명한다.
- 조직 내 암호화 알고리즘, 라이브러리, 사용처를 체계적으로 분류하는 방법을 익힌다.
- 암호 민첩성(Crypto-agility)을 위한 메타데이터 관리 요소를 파악한다.
- 식별된 암호 자산의 위험도를 평가하여 포스트퀀텀 전환 우선순위를 결정한다.
worked_examples:
- '시스템 스캔 결과 예시: ''TLS 1.2(ECDHE-RSA-AES128-GCM-SHA256) 사용 중''이라는 자산 식별. 이 경우 RSA와
  ECDHE가 양자 위협에 노출됨을 인지하고 ML-KEM/ML-DSA 전환 대상을 분류함.'
- '암호 민첩성 자가 점검표: ''알고리즘이 하드코딩되어 있는가?''에 대해 ''예''라면 위험 점수 상향. ''설정 파일을 통한 암호 알고리즘
  선택이 가능한가?''에 대해 ''아니오''라면 전환 난이도 상향.'
lab:
  title: 암호 자산 식별 및 위험도 평가 실습
  steps:
  - 샘플 프로젝트의 소스 코드를 대상으로 'AES', 'RSA', 'ECC' 키워드 검색을 수행하여 사용처를 찾는다.
  - 식별된 암호 구현체(라이브러리 포함)를 '암호 자산 Inventory CSV'에 기록한다.
  - 각 자산에 대해 '보안 수명', '양자 위협 수준', '데이터 중요도'를 기준으로 위험 점수를 산정한다.
  - 산정된 점수를 기반으로 전환 우선순위(P0~P3)를 분류한다.
  safety:
  - 실제 운영 중인 시스템의 개인키나 실제 서비스 인증서를 스캔하지 않는다.
  - 테스트를 위해 가상 환경 내에 격리된 더미 인증서(테스트용)만을 사용한다.
  - 분석 결과물(CSV, 문서)에 실제 비밀값이나 암호화 키 값을 포함하지 않는다.
  deliverables:
  - 암호 자산 Inventory CSV 파일 (알고리즘, 사용처, 라이브러리, 라이브러리 버전 포함)
  - 우선순위 기반의 암호 자산 위험 평가 보고서 (Markdown)
assignment:
  title: 암호 민첩성 분석 및 전환 로드맵 수립
  deliverables:
  - 암호 자산 Inventory CSV
  - 전환 우선순위가 정의된 의사결정표
  - 포스트퀀텀 전환 로드맵
  rubric:
  - 암호 자산이 포괄적으로 식별되었는가?
  - 위험 평가 기준이 객관적이고 타당한가?
  - 전환 로드맵이 포스트퀀텀 기술 전환의 논리적 순서를 따르고 있는가?
  - 암호 민첩성 개선을 위한 구체적인 기술 제안이 포함되었는가?
quiz:
- question: 암호 자산 식별(Cryptographic Inventory)의 주된 목적은 무엇인가?
  choices:
  - 모든 암호화 라이브러리의 성능을 최적화하기 위해
  - PQC 전환을 준비하기 위해 조직 내 암호 의존성을 파악하기 위해
  - 암호화 알고리즘을 모두 삭제하기 위해
  - 비대칭 암호만 사용하도록 강제하기 위해
  answer_index: 1
  explanation: 암호 자산 식별은 전환해야 할 암호화 알고리즘의 위치와 의존성을 체계적으로 관리하여 PQC 전환을 효율적으로 수행하는 것을
    목적으로 합니다.
- question: 다음 중 암호 민첩성(Crypto-agility)의 정의로 가장 적절한 것은?
  choices:
  - 더 강력한 암호화를 위해 하드웨어를 교체하는 과정
  - 암호화 라이브러리 업데이트를 자동화하는 기능
  - 코드 변경을 최소화하고 필요 시 신속하게 암호 알고리즘을 교체할 수 있는 유연성
  - 암호화 키를 매우 자주 변경하는 것
  answer_index: 2
  explanation: 암호 민첩성은 알고리즘 교체 시 코드 변경 부담을 최소화하여 변화하는 보안 환경에 적응하는 능력을 의미합니다.
completion_criteria:
- 암호 자산 식별 Inventory CSV를 제출하고 위험 평가가 완료됨
- 각 암호 자산의 전환 난이도 및 위험 우선순위가 명시된 보고서 작성
- 퀴즈 항목에서 100% 정답 도달
source_ids:
- S1
---

## 암호 자산 식별 (Cryptographic Inventory)

암호 자산 식별은 조직 내에서 사용되는 모든 암호화 알고리즘, 프로토콜, 라이브러리, 그리고 이들이 적용된 시스템 및 데이터를 체계적으로 목록화하는 과정이다. 이는 포스트퀀텀 암호(PQC)로의 전환을 준비하는 첫 번째 단계로, 보호 대상인 암호 알고리즘의 의존성을 명확히 파악하는 것이 핵심이다 [S1].

### 1. 주요 관리 대상
- **알고리즘 및 프로토콜**: TLS, SSH, 코드 서명, 데이터 암호화(AES, RSA, ECC 등) 등.
- **인프라**: 인증기관(CA), 키 관리 시스템(KMS), HSM, 클라우드 키 저장소.
- **소프트웨어**: 암호화 라이브러리 버전(OpenSSL, BoringSSL 등) 및 정적/동적 연결 여부.

### 2. 암호 민첩성(Crypto-agility)
암호 민첩성은 코드 변경을 최소화하면서 암호화 알고리즘을 신속하게 교체할 수 있는 능력을 의미한다. 이를 위해 시스템은 특정 알고리즘에 하드코딩되지 않고, 설정 파일을 통해 알고리즘을 선택할 수 있는 추상화 계층을 가져야 한다.

### 3. 위험도 평가 기준
- **데이터 생명주기**: 암호화된 데이터가 미래에도 비밀을 유지해야 하는가? (예: 지금 탈취하여 미래에 해독될 위험이 있는 데이터)
- **전환 난이도**: 하드웨어 교체가 필요한가, 아니면 소프트웨어 업데이트만으로 충분한가?
- **규제 및 준수**: NIST PQC 표준 적용 시기와의 정렬 여부.
