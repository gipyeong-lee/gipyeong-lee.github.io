---
layout: learn-module
title: 로봇공학 기초
course_slug: precise-robot-hand
module_id: m1
permalink: /learn/precise-robot-hand/robotics-fundamentals/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: d9a7f912e090478cab017e340f4b3e42
id: m1
slug: robotics-fundamentals
phase_id: phase1
estimated_hours: 10.0
prerequisites: []
objectives:
- 로봇공학의 정의와 시스템 구성요소(기구부, 액추에이터, 센서, 제어기)를 이해한다.
- 로봇 시스템의 동적 거동과 제어 루프의 기본 개념을 파악한다.
- 정교한 로봇손 구현을 위한 하드웨어 설계 원칙을 학습한다.
worked_examples:
- '액추에이터 전력 요구량 계산: XM430-W350-T 1대의 스톨 전류는 2.3 A입니다 [BOM: actuator-01]. 전체 10대의 액추에이터가
  동시에 스톨 상태가 되면 23 A의 전류가 필요합니다. 이를 위해 11.5 A 출력 어댑터 2대를 독립된 분기로 배치하여 전원을 공급합니다 [BOM:
  power-01].'
- '센서 전압 분압 계산: FSR 402 센서와 10 kΩ 저항을 사용하여 분압 회로를 구성합니다 [BOM: sensor-01, B-SENSOR-RESISTOR].
  3.3 V 전원을 인가할 때, 센서 저항이 변화함에 따라 ADC 입력단은 0 ~ 3.3 V 사이의 신호를 얻게 되어 OpenCR 보드에서 안전하게
  측정됩니다 [BOM: controller-01].'
lab:
  title: 로봇 시스템 안전 전원 및 기본 제어 구성
  steps:
  - '각 12 V 전원 어댑터 출력에 10 A 퓨즈 홀더를 설치하고 10 A 퓨즈를 장착한다 [BOM: B-WIRING-FUSE-HOLDER].'
  - '비상정지 버튼을 EV200 접촉기의 코일 회로와 직렬로 연결하여 비상 시 코일 전원이 차단되도록 한다 [BOM: safety-01, safety-02].'
  - '3.3 V 센서 레일을 사용하여 FSR 분압 회로를 구성하고 OpenCR 보드 ADC 포트에 연결한다 [BOM: controller-01].'
  - '독립된 전원 분기 3개를 구성하고 액추에이터를 분기별로 배분하여 연결한다 [BOM: power-01].'
  safety:
  - 모든 전원 연결 전 멀티미터로 극성과 단락 여부를 반드시 확인한다.
  - 보안경을 착용하고 전원 작업 시 긴급 비상 차단 버튼을 즉시 조작 가능한 거리에 둔다.
  - 12 V 액추에이터 전원과 3.3 V 센서 전원을 절대 혼용하지 않는다.
  deliverables:
  - 정상적으로 전압이 출력되는 독립 퓨즈 분기 회로 측정 기록
  - 비상정지 동작 시 접촉기 차단 확인 로그
  - FSR 센서 입력값이 0~3.3 V 범위 내임을 확인한 데이터
assignment:
  title: 로봇 시스템 구성 및 안전 설계 보고서
  deliverables:
  - BOM 기반 시스템 배선도
  - 액추에이터 피크 전류 대비 퓨즈 및 차단 장치 적합성 계산서
  - 전원 분기 및 안전 시스템 설계 근거
  rubric:
  - 전원 분기 회로의 독립성이 전기적으로 보장됨
  - BOM 시스템 진실(system truth)에 명시된 부품 정격과 안전 부품 사양의 일치
  - 비상 시 전원 차단 로직의 명확한 설계
quiz:
- question: 정교한 5지 로봇손 설계 시 12 V 액추에이터 전원과 3.3 V 센서 전원의 관계는?
  choices:
  - 두 전원은 반드시 하나의 전원에서 공급받아야 한다.
  - 회로적으로 전기적 격리가 필수적이다.
  - 센서 전원은 액추에이터 전원에서 전압 강하를 통해 얻는다.
  - 상관없다.
  answer_index: 1
  explanation: '액추에이터의 높은 전류와 노이즈로부터 센서 회로의 정밀도를 보호하기 위해 전기적으로 분리되어야 합니다 [BOM: controller-01].'
- question: 비상정지 버튼의 적절한 설치 방법은?
  choices:
  - 모터 전류를 직접 차단한다.
  - 배터리의 (+)단자를 직접 끊는다.
  - EV200 접촉기의 코일 회로를 제어하여 DC 분기를 동시에 차단한다.
  - 제어기의 전원을 차단한다.
  answer_index: 2
  explanation: '저전류 비상정지 스위치로 대전류 DC 분기를 안전하게 차단하기 위해 접촉기 코일 회로를 제어합니다 [BOM: safety-01,
    safety-02].'
completion_criteria:
- 안전 전원 분기 및 비상 차단 시스템 구성 완료
- FSR 센서의 3.3 V ADC 입력 측정 및 검증 완료
- BOM 시스템 진실과 일치하는 안전 설계 보고서 제출
source_ids:
- S1
- S2
---

## 로봇공학 기초

로봇은 감지(sensing), 계산(computation), 작용(actuation)을 수행하여 물리적 환경과 상호작용하는 시스템입니다 [S1]. 성공적인 로봇 설계는 메커니즘, 역학, 그리고 제어의 통합적 접근을 요구합니다 [S2].

### 1. 주요 구성요소
- **기구부(Mechanism):** 로봇의 골격과 자유도(DoF)를 정의합니다. 링크와 관절로 구성되며, 정교한 로봇손에서는 텐던(tendon) 구동 방식을 통해 가벼운 링크 구조를 구현합니다.
- **액추에이터(Actuator):** 전기 에너지를 기계적 운동으로 변환합니다. 정밀 제어를 위해 위치, 속도, 전류 피드백이 가능한 스마트 액추에이터(예: DYNAMIXEL XM430)를 사용합니다 [BOM: actuator-01].
- **센서(Sensor):** 환경 정보를 제어기로 전달합니다. 로봇손에서는 접촉력을 측정하는 FSR(Force Sensitive Resistor) 등을 사용하여 파지력을 제어합니다 [BOM: sensor-01].
- **제어기(Controller):** 센서 데이터를 처리하고 액추에이터에 명령을 내립니다. 안전을 위해 실시간 처리가 가능한 전용 보드(예: OpenCR)를 사용합니다 [BOM: controller-01].

### 2. 설계 원칙
로봇 시스템은 안전이 최우선입니다. 특히 전원 구성 시 독립된 분기 회로를 유지하여 과전류를 방지하고, 비상 시 즉각적으로 전원을 차단할 수 있는 시스템을 구축해야 합니다 [BOM: safety-01, safety-02]. 3.3 V 센서 전원과 12 V 액추에이터 전원은 회로적으로 분리되어야 합니다 [BOM: controller-01].
