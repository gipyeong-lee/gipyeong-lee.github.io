---
layout: learn-module
title: 로봇 공학 개론
course_slug: precise-robot-hand
course_data_key: precise-robot-hand
course_locale: ko
lang: ko
ref: learn:precise-robot-hand:intro-robotics
translations:
- lang: ko
  url: /learn/precise-robot-hand/intro-robotics/
- lang: en
  url: /learn/en/precise-robot-hand/intro-robotics/
- lang: ja
  url: /learn/ja/precise-robot-hand/intro-robotics/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/intro-robotics/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/intro-robotics/
module_id: m1
permalink: /learn/precise-robot-hand/intro-robotics/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
id: m1
slug: intro-robotics
phase_id: p1
estimated_hours: 10.0
prerequisites: []
objectives:
- 로봇 공학의 정의와 시스템 구성 요소를 이해한다.
- 5지 로봇손 프로토타입에 사용되는 액추에이터와 제어기의 역할을 파악한다.
- 로봇 시스템의 안전한 전원 분기 구성과 물리적 차단 원리를 학습한다.
- 힘 감지 센서(FSR)의 동작 원리와 ADC 데이터 취득 방법을 익힌다.
worked_examples:
- '액추에이터 부하 계산: XM430-W350-T 4대를 1개 분기에 배치할 경우, 피크 전류는 4 * 2.3 A = 9.2 A입니다 [S14].
  이는 10 A 퓨즈의 정격 내에 있으며, 전원 어댑터의 11.5 A 출력 정격보다 작아 안정적인 운용이 가능합니다 [S17, S26].'
- 'FSR 전압 분압기 설계: 센서와 10 kΩ 저항을 직렬 연결한 분압기에서, 3.3 V 입력 시 센서가 누름을 받지 않아 고저항 상태일 때 ADC는
  0 V에 가까운 값을, 강한 힘을 받아 저항이 급감하면 ADC는 3.3 V에 가까운 값을 출력합니다 [S15, S27].'
lab:
  title: 전원 분기 구성 및 시스템 기본 통전 시험
  steps:
  - 각 MEAN WELL 어댑터의 양(+) 단자에 ATO 인라인 홀더와 10 A 퓨즈를 연결하여 3개의 독립 분기를 생성한다 [S17, S25,
    S26].
  - 멀티미터를 DC 전압 모드로 설정하고 각 분기의 출력 전압이 12 V인지 확인한다.
  - OpenCR 제어기를 3.3 V 센서 전원 레일에 연결하고, FSR 센서와 10 kΩ 저항을 활용한 분압 회로를 구성한다 [S16, S27].
  - 제어기에 전원을 인가한 뒤, 각 텐던 액추에이터가 정상적으로 통신하는지 DYNAMIXEL Wizard로 확인한다 [S14, S16].
  safety:
  - 전원 인가 전 모든 결선을 멀티미터의 저항 모드가 아닌 육안과 도면으로 재검증한다.
  - 통전 중에는 시스템 접근을 금지하며, 반드시 비전원 상태(물리적 어댑터 분리)에서 배선한다.
  - 이상 발열·냄새·연기 감지 시 접근하지 말고, 위험 구역 밖에서 사전 지정된 건물 분전반 차단기 또는 인증된 upstream master disconnect로
    3개 어댑터의 공급 전원을 차단한 뒤 대피한다. 위험 구역 밖에서 작동 가능한 upstream 차단 수단이 없으면 시스템 통전을 금지한다.
    토크 해제는 전원 차단을 대신하지 않는다. 정비·접근은 계획 정지 후 물리적 분리 및 무전원 계측 확인 뒤에만 수행한다.
  - 보안경을 상시 착용하고 가동 범위에 신체 부위를 넣지 않는다.
  deliverables:
  - 각 분기별 12 V 측정 기록 사진
  - OpenCR ADC 센서 데이터 취득 코드
  - 독립 분기 결선 배선도
assignment:
  title: 로봇 시스템 안전 설계 리포트
  deliverables:
  - 독립 전원 분기 구성도
  - 액추에이터 피크 전류 대비 퓨즈 정격 타당성 분석
  - FSR 전압 분압 회로 설계값 산출식
  rubric:
  - 액추에이터 11대와 전원 분기 3개의 할당이 명확한가?
  - 3.3 V 센서 레일과 12 V 액추에이터 레일의 분리가 올바르게 설명되었는가?
  - 전원 차단 절차(물리적 분리)가 정확히 서술되었는가?
quiz:
- question: 시스템 전원 설계 시 12 V 출력 단자의 양(+) 극을 병렬 연결하는 것은 왜 금지되는가?
  choices:
  - 전압이 24 V로 상승하기 때문에
  - 어댑터 간 전위차로 인한 역전류 발생 및 독립 분기 보호 파괴 위험
  - 액추에이터의 통신 속도가 저하되기 때문에
  - 소프트웨어 토크 해제 기능을 사용할 수 없기 때문에
  answer_index: 1
  explanation: 각 전원 어댑터는 독립적인 분기로 운용되어야 하며, 출력 단자를 결합할 경우 고장이 나거나 독립 퓨즈에 의한 안전 보호
    기능이 무력화될 위험이 있습니다.
- question: OpenCR의 ADC 포트로 FSR 신호를 읽을 때 적절한 공급 전압은?
  choices:
  - 12 V 액추에이터 레일
  - 3.3 V 센서 레일
  - 24 V 입력 전원
  - 비접촉식 무선 전력
  answer_index: 1
  explanation: OpenCR의 ADC는 0~3.3 V 범위를 사용하며, 센서 보호를 위해 반드시 전용 3.3 V 센서 레일에서 공급받아야
    합니다.
- question: 시스템 점검 및 정비를 위해 전원을 차단하는 가장 안전한 방법은?
  choices:
  - 소프트웨어 명령으로 액추에이터 토크 해제
  - 퓨즈 제거
  - 3개 전원 어댑터를 물리적으로 분리한 뒤 전압 계측
  - 제어기 전원 스위치만 끄기
  answer_index: 2
  explanation: 소프트웨어 명령이나 퓨즈는 완벽한 무전원 상태를 보장하지 않습니다. 반드시 어댑터를 물리적으로 분리하고 멀티미터로 1 V
    미만임을 계측해야 합니다.
completion_criteria:
- 각 분기별 12 V 전압이 정상 범위임을 멀티미터로 확인하고 사진으로 제출함
- FSR 센서의 접촉력에 따른 ADC 값 변화를 제어기로 확인하고 정당한 값을 취득함
- 물리적 전원 차단 및 전압 계측을 통한 안전 정지 절차를 이해하고 준수함
source_ids:
- S1
- S14
- S16
- S17
- S25
- S26
- S15
- S27
---

## 로봇 시스템 구성 요소
로봇은 감각(Sensor), 사고(Controller), 동작(Actuator)의 세 가지 핵심 요소로 구성됩니다 [S1]. 본 과정의 5지 로봇손은 DYNAMIXEL XM430-W350-T 액추에이터를 사용하여 텐던 구동 방식으로 관절을 제어하며 [S14], OpenCR 1.0 제어기를 통해 이들 액추에이터와 손끝의 FSR 센서 신호를 처리합니다 [S16].

## 전력 시스템의 안전한 설계
액추에이터는 12 V 전압에서 스톨 전류 2.3 A를 요구하므로 [S14], 시스템 전체 부하를 고려하여 MEAN WELL GST160A12-R7B 어댑터 3개를 사용합니다 [S17]. 각 어댑터는 4대/4대/3대의 액추에이터를 담당하는 독립적인 12 V 분기로 운용되며, 이들 분기의 양(+) 출력은 서로 결합하지 않고 물리적으로 격리됩니다. 각 분기에는 10 A ATOF 퓨즈를 인라인 홀더(0AFH0001Z)를 통해 설치하여 과전류 발생 시 배선을 보호합니다 [S25, S26]. 이는 단순한 정지 기능을 넘어선 전기적 안전의 기초입니다.

## 센서 인터페이스
FSR 402 센서는 접촉력에 따라 저항이 감소하는 특성을 가집니다 [S15]. 이를 10 kΩ 저항과 함께 분압 회로로 구성하여 OpenCR의 12-bit ADC 포트에 연결함으로써 접촉력을 전압으로 환산합니다 [S16, S27]. 이때 센서 회로는 3.3 V 센서 전원 레일에서만 공급받아야 하며, 액추에이터용 12 V 레일과 혼용해서는 안 됩니다.
