---
layout: learn-module
title: 촉각 센서 인터페이스 구현
course_slug: precise-robot-hand
module_id: mod-7
permalink: /learn/precise-robot-hand/sensor-integration/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e6d0fb4b969e4bc38344d636a236342f
id: mod-7
slug: sensor-integration
phase_id: phase-3
estimated_hours: 10.0
prerequisites:
- mod-6
objectives:
- FSR 402 센서의 작동 원리와 저항-압력 특성을 이해한다.
- OpenCR 제어기에서 전압 분압 회로를 구성하여 ADC 신호를 취득하는 방법을 학습한다.
- 센서 데이터를 보정하고 로봇손 파지력 제어에 활용하는 로직을 구현한다.
worked_examples:
- '예시 1: FSR에 힘이 가해지지 않아 R_FSR이 100 kΩ일 때, V_out = 3.3V * (10k / (100k + 10k)) ≈ 0.3V.
  힘 감지 전 신호값 확인.'
- '예시 2: FSR에 적절한 힘이 가해져 R_FSR이 10 kΩ이 되었을 때, V_out = 3.3V * (10k / (10k + 10k)) =
  1.65V. 중간 압력 상태.'
- '예시 3: FSR에 강한 힘이 가해져 R_FSR이 1 kΩ이 되었을 때, V_out = 3.3V * (10k / (1k + 10k)) ≈ 3.0V.
  최대 압력 상태.'
lab:
  title: FSR 센서 ADC 인터페이스 테스트
  steps:
  - OpenCR의 3.3V 센서 레일과 GND를 확인한다.
  - 브레드보드에 FSR 402와 10 kΩ 저항으로 전압 분압 회로를 구성한다.
  - ADC 입력 신호를 OpenCR의 아날로그 입력 포트에 연결한다.
  - 제어 코드를 실행하여 FSR에 가하는 힘에 따른 ADC 원시 데이터(Raw Data) 변화를 모니터링한다.
  safety:
  - OpenCR의 3.3V 센서 레일만 사용하고, 5V 또는 12V 전원을 센서 회로에 직접 연결하지 않는다.
  - 납땜 시 보안경을 착용하고 환기가 잘 되는 곳에서 작업한다.
  - 전원 연결 전 단락(short) 여부를 멀티미터로 반드시 확인한다.
  deliverables:
  - 회로 배선도
  - 힘 인가량 대비 ADC 출력값 데이터 시트
  - 센서 데이터 로그 파일
assignment:
  title: 촉각 센서 보정 및 파지력 제어 구현
  deliverables:
  - 센서 보정 로직이 포함된 펌웨어 코드
  - 힘-전압 변환 그래프가 포함된 보고서
  rubric:
  - ADC 신호가 0~3.3V 범위를 준수하는가?
  - 물체 접촉 시 센서값이 유의미하게 변화하는가?
  - 코드에서 노이즈 필터링 로직이 구현되었는가?
quiz:
- question: FSR 402 인터페이스를 위해 전압 분압 회로를 사용할 때, 고정 저항은 어디에 연결해야 합니까?
  choices:
  - FSR과 12V 전원 사이
  - ADC 입력과 GND 사이
  - FSR과 5V 전원 사이
  - ADC 입력과 12V 사이
  answer_index: 1
  explanation: ADC 입력과 GND 사이에 고정 저항을 연결해야 FSR 저항 변화에 따른 전압 분압이 올바르게 이루어져 ADC가 전압을
    읽을 수 있습니다.
- question: OpenCR의 센서 전원 레일 사양으로 올바른 것은 무엇입니까?
  choices:
  - 5 V
  - 12 V
  - 3.3 V
  - 24 V
  answer_index: 2
  explanation: OpenCR의 FSR 분압 회로는 3.3V 센서 전원 레일만 사용하여 ADC 입력 신호 범위를 0~3.3V로 제한해야 합니다.
completion_criteria:
- FSR 전압 분압 회로가 OpenCR의 3.3V 레일에 정상적으로 구성됨.
- ADC 원시 데이터가 FSR에 가해지는 힘에 따라 0~3.3V 범위 내에서 변동됨.
- 센서 보정 로직이 정상 작동하고 파지력 피드백이 펌웨어에 기록됨.
source_ids:
- S11
- S26
---

## 촉각 센서 인터페이스 이론

### FSR 402의 특성
FSR(Force Sensing Resistor) 402는 인가되는 힘의 크기에 따라 저항값이 감소하는 압력 민감성 고분자 필름 센서입니다 [S11]. 0.2N에서 20N 범위의 하중을 측정할 수 있으며, 반복적인 압력 입력에 적합한 구조를 가집니다 [S11].

### 전압 분압 회로 (Voltage Divider)
OpenCR 제어기의 ADC는 0~3.3V 범위의 전압을 디지털 값으로 변환합니다 [S12]. FSR은 자체적으로 저항값이 변하므로, 이를 전압으로 변환하기 위해 고정된 값의 저항(10 kΩ)과 직렬로 연결하여 전압 분압 회로를 구성합니다 [S26].

회로 구성:
1. 3.3V 센서 전원 → FSR → ADC 포트
2. ADC 포트 → 10 kΩ 고정 저항 → GND

이때 ADC 입력 전압 V_out은 다음과 같이 계산됩니다:
V_out = V_in * (R_fixed / (R_FSR + R_fixed))

이 방식은 FSR의 저항 변화를 0V~3.3V 사이의 아날로그 전압 신호로 변환하여 제어기가 힘을 감지하게 합니다 [S26].
