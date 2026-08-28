---
layout: learn-module
title: 성능 시험 및 검증
course_slug: precise-robot-hand
course_data_key: precise-robot-hand
course_locale: ko
lang: ko
ref: learn:precise-robot-hand:testing-validation
translations:
- lang: ko
  url: /learn/precise-robot-hand/testing-validation/
- lang: en
  url: /learn/en/precise-robot-hand/testing-validation/
- lang: ja
  url: /learn/ja/precise-robot-hand/testing-validation/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/testing-validation/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/testing-validation/
module_id: M9
permalink: /learn/precise-robot-hand/testing-validation/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
id: M9
slug: testing-validation
phase_id: P3
estimated_hours: 10.0
prerequisites:
- M8
objectives:
- 로봇 손의 정밀도 및 반복성 검증을 위한 정량적 시험 지표 설계
- FSR 센서 데이터를 활용한 파지력 제어 알고리즘의 안정성 평가
- DYNAMIXEL 액추에이터 피드백 데이터와 실제 물리적 동작의 오차 분석
- 기구적 결함 및 텐던 구동 메커니즘의 내구성 검증 절차 습득
worked_examples:
- '예제 1: OpenCR ADC 전압 계산. FSR 저항이 10 kΩ이고, 직렬 저항이 10 kΩ일 때, 3.3 V 전압 분배기 출력은 V_out
  = 3.3 * (10k / (10k + 10k)) = 1.65 V입니다. 이는 12비트 ADC 범위 내에 적합합니다 [S13, S26].'
- '예제 2: 퓨즈 보호 협조. 액추에이터 4대가 스톨 상태일 때 전류 합계는 9.2 A입니다 [S11]. 10 A 퓨즈의 냉간 저항은 7.7 mΩ이므로
  [S25], 정상 운전 시 전압 강하는 약 0.07 V 수준으로 무시할 수 있으나, 과전류 시 정확한 응답은 퓨즈 제조사의 시간-전류 곡선을 참조해야
  합니다.'
lab:
  title: 로봇 손 통합 기능 시험
  steps:
  - 각 전원 분기를 물리적으로 분리한 상태에서 3개 어댑터의 출력을 DC 전압 모드로 계측하여 12 V가 나오는지 확인합니다.
  - 안전 지그에 로봇 손을 고정하고, 제어기(OpenCR)를 PC에 연결하여 액추에이터 토크를 0으로 해제합니다.
  - 손가락별로 FSR 센서에 인가되는 압력을 손으로 가하며 ADC 데이터 변화를 기록합니다.
  - 무부하 상태에서 각 손가락의 최대 가동 범위(ROM)를 5회 반복 동작시켜 텐던 간섭 여부를 확인합니다.
  - 시험 종료 후 반드시 3개 전원 어댑터를 벽면 콘센트에서 분리하고 잔류 전압을 확인합니다.
  safety:
  - 반드시 보안경을 착용하고 시험에 임합니다.
  - 전원 인가 중 가동 범위 내에 손을 넣지 않습니다.
  - 이상 발열·냄새·연기 감지 시 접근하지 말고, 위험 구역 밖에서 사전 지정된 건물 분전반 차단기 또는 인증된 upstream master disconnect로
    3개 어댑터의 공급 전원을 차단한 뒤 대피한다. 위험 구역 밖에서 작동 가능한 upstream 차단 수단이 없으면 시스템 통전을 금지한다.
    토크 해제는 전원 차단을 대신하지 않는다. 정비·접근은 계획 정지 후 물리적 분리 및 무전원 계측 확인 뒤에만 수행한다
  - 전압 계측 없이 시스템을 만지지 않습니다. 1 V 미만 DC 확인은 필수입니다.
  deliverables:
  - 손가락 파지력 센서 교정 기록
  - 반복 동작 정밀도 측정 데이터
  - 전원 분기별 부하 전류 측정치
assignment:
  title: 로봇 손 성능 분석 최종 보고서
  deliverables:
  - 성능 시험 결과 분석 보고서
  - 데이터 기반 파지 제어 알고리즘 코드
  rubric:
  - 센서 데이터의 신호 대 잡음비(SNR) 분석의 적절성
  - 반복 동작 시험에서의 정밀도 정량화
  - 보호 설계(퓨즈)가 시스템 보호 의도를 만족하는지에 대한 이론적 고찰
  - 설계 사양과 실제 제작품의 성능 지표 비교
quiz:
- question: FSR 402 센서와 OpenCR ADC를 이용한 힘 측정 회로 구성 시 옳은 것은?
  choices:
  - FSR 전압 분압기는 3.3 V 센서 전원만 사용하고 아날로그 입력 신호를 0~3.3 V 범위로 유지한다
  - FSR과 10 kΩ 저항으로 전압 분배기를 구성하고 3.3 V 센서 레일을 사용한다
  - ADC 신호는 항상 0~5 V 범위가 되어야 한다
  - FSR은 저항이 일정하므로 별도의 분압 저항이 필요 없다
  answer_index: 1
  explanation: OpenCR 센서 레일(3.3 V)을 사용하여 ADC 입력을 0~3.3 V 범위로 제한하고, 분압 회로를 구성하여 저항
    변화를 전압 변화로 읽어야 합니다 [S13, S26].
- question: DYNAMIXEL XM430-W350-T 액추에이터의 12 V 전원 분기를 관리하는 방법으로 옳은 것은?
  choices:
  - 3개의 어댑터 양(+) 출력을 하나로 묶어 전력을 합산한다
  - 어댑터별로 10 A 퓨즈를 장착하고 개별 독립 분기로 사용한다
  - 전류가 퓨즈 정격 이하이므로 안전 검증 없이 사용 가능하다
  - 전원 어댑터 출력은 퓨즈 없이 직접 병렬로 연결한다
  answer_index: 1
  explanation: 각 어댑터 출력은 독립적으로 유지되어야 하며, 독립 분기에 맞는 퓨즈를 장착하여 과전류를 보호해야 합니다 [S15].
- question: 로봇 손 검증 단계에서 가장 중요한 안전 절차는 무엇인가?
  choices:
  - 소프트웨어적으로 토크를 해제하면 전원 차단과 동일하다
  - 항상 멀티미터로 1 V 미만 DC를 확인한 후 정비에 접근한다
  - 퓨즈는 계획 정지 장치 역할을 하므로 퓨즈를 뽑으면 된다
  - 연속성(Continuity) 모드로 전원이 차단되었음을 확인한다
  answer_index: 1
  explanation: 소프트웨어 해제는 물리적 전원 차단을 대체하지 못하며, 물리적 분리 후 DC 전압 모드로 잔류 에너지가 없음을 계측 확인하는
    것이 필수입니다.
completion_criteria:
- 성능 시험 결과 보고서 제출 및 70점 이상 획득
- 모든 Lab 단계에서 안전 지침 준수 및 물리적 전원 분리 확인 완료
- 제어 코드의 센서 데이터 필터링 기능 구현 확인
source_ids:
- S1
- S11
- S16
- S12
- S13
- S26
- S15
- S25
---

## 성능 시험 및 검증 이론

로봇 손의 성능 검증은 설계 사양과 실제 물리적 거동 사이의 일치성을 확인하는 과정입니다. [S1]. 주요 지표는 다음과 같습니다.

### 1. 위치 및 파지 정밀도
반복성(Repeatability)은 동일한 명령을 수행했을 때 로봇 손이 도달하는 위치의 오차 범위를 의미합니다. XM430-W350-T 액추에이터는 내부 엔코더를 통해 정밀한 위치 피드백을 제공하지만 [S11], 최종 손가락 끝의 위치는 텐던의 신율과 마찰에 의해 오차가 발생합니다. Dyneema 텐던은 신율이 1% 미만으로 매우 낮아 반복성 확보에 유리합니다 [S16].

### 2. 힘 제어와 FSR 센서 신호 처리
FSR 402 센서는 가해진 힘에 따라 저항이 감소하는 특성을 가집니다 [S12]. 이를 10 kΩ 저항과 분압 회로로 구성하여 OpenCR의 12비트 ADC로 측정합니다 [S13, S26]. 센서 데이터는 노이즈가 많으므로 이동 평균 필터(Moving Average Filter)를 적용하여 안정적인 파지력 피드백 루프를 형성해야 합니다.

### 3. 과전류 보호 및 전원 안정성
시스템은 3개의 독립된 12 V 전원 분기를 사용합니다 [S15]. 각 분기는 10 A ATOF 퓨즈로 보호되며 [S25], 액추에이터 피크 전류 합계가 보호 정격을 초과하지 않도록 배분해야 합니다. 이는 제조업체에서 제공하는 퓨즈의 시간-전류 곡선을 통해 보호 협조를 검증해야 합니다.
