---
layout: learn-module
title: 센서 신호 획득 및 처리
course_slug: precise-robot-hand
module_id: m7
permalink: /learn/precise-robot-hand/sensing-implementation/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: 44d3a08daba248e5b900b0d5bdc9dc49
id: m7
slug: sensing-implementation
phase_id: phase-3
estimated_hours: 10.0
prerequisites:
- m6
objectives:
- FSR 402 센서의 압력-저항 특성을 이해하고 전압 분압 회로를 설계할 수 있다.
- OpenCR 제어기의 12비트 ADC를 활용하여 센서 신호를 획득하고 변환할 수 있다.
- 데이터 취득 시 노이즈를 억제하기 위한 소프트웨어적 처리 기법을 적용할 수 있다.
- 3.3 V 센서 전원 분리와 전기적 절연의 중요성을 실습을 통해 체득한다.
worked_examples:
- '예제 1: 10 kΩ 고정 저항과 FSR 402를 사용한 분압 회로에서, FSR의 현재 저항값이 5 kΩ일 때 ADC 입력 전압($V_{out}$)
  계산:

  $V_{out} = 3.3 V \times (10,000 / (10,000 + 5,000)) = 3.3 V \times 0.667 = 2.2 V$
  (ADC 값 약 2730)'
- '예제 2: FSR 센서 신호의 노이즈 제거를 위한 이동 평균 필터(Moving Average Filter) 적용:

  최근 10개의 샘플 값을 저장하고, 매 샘플마다 합계를 10으로 나누어 출력값을 평활화하여 텐던 제어의 안정성을 높임.'
lab:
  title: FSR 신호 측정 및 데이터 처리 실습
  steps:
  - OpenCR 3.3 V 센서 전원 및 GND 포트를 확인한다 [S11].
  - FSR 402와 10 kΩ 저항을 사용하여 전압 분압 회로를 구성한다 [S24].
  - 분압된 전압 신호를 OpenCR ADC 입력 핀에 연결한다 [S11].
  - 멀티미터를 사용하여 ADC 입력 핀의 전압이 0~3.3 V 범위 내에 있는지 확인한다.
  - 펌웨어를 업로드하여 시리얼 모니터로 FSR 데이터 값을 관찰한다.
  - 데이터 평활화를 위한 이동 평균 필터 코드를 적용하고 신호 안정성을 비교한다.
  safety:
  - 모든 회로 변경은 3개의 12 V 전원 어댑터를 물리적으로 분리한 후 진행한다.
  - 전원 연결 전 멀티미터를 DC 전압 모드로 설정하여 각 분기 전압이 1 V 미만임을 확인한다.
  - OpenCR ADC 입력에 3.3 V를 초과하는 전압이 인가되지 않도록 주의한다 [S11].
  - 납땜 작업 시 보안경을 착용하고 환기가 잘 되는 곳에서 작업한다.
  deliverables:
  - 센서 신호 획득 및 노이즈 처리 펌웨어 소스 코드
  - FSR 압력 변화에 따른 ADC Raw 데이터 및 전압 측정값 보고서
assignment:
  title: 센서 데이터 기반 파지력 제어 구현
  deliverables:
  - FSR 데이터를 힘(N) 단위로 변환하는 교정 곡선 그래프
  - 설정한 임계값 도달 시 모터 정지 명령을 수행하는 제어 로직 코드
  - 최종 센서 처리 및 제어 시스템 구현 보고서
  rubric:
  - 전압 분압 회로의 올바른 설계 및 구현 여부 (30%)
  - ADC 샘플링 데이터의 노이즈 억제 성능 (30%)
  - 물리적 힘과 소프트웨어 출력 데이터 간의 선형성 교정 정확도 (20%)
  - 안전 수칙 준수 및 측정 데이터의 신뢰성 (20%)
quiz:
- question: FSR 402 센서를 사용한 전압 분압 회로에서 OpenCR 보드의 어떤 전원 레일을 사용해야 하는가?
  choices:
  - 12 V 액추에이터 레일
  - 3.3 V 센서 전원 레일
  - 5 V 범용 전원 레일
  - 24 V 입력 전원 레일
  answer_index: 1
  explanation: OpenCR의 ADC는 0~3.3 V 범위에서 작동하며, 센서 손상 방지를 위해 전용 3.3 V 센서 레일을 사용해야 합니다
    [S11].
- question: ADC 값이 4095일 때, 12비트 ADC 시스템에서 이는 어떤 전압을 의미하는가?
  choices:
  - 0 V
  - 1.65 V
  - 3.3 V
  - 5 V
  answer_index: 2
  explanation: 12비트 ADC는 0부터 2^12-1(4095)까지의 값을 가지며, 3.3 V 기준 전압에서 최대값은 기준 전압과 같습니다
    [S11].
completion_criteria:
- FSR 회로를 3.3 V 레일에 올바르게 연결하고 ADC 전압이 0~3.3 V 이내임을 실측 확인
- 이동 평균 필터를 적용하여 센서 노이즈가 유의미하게 감소된 데이터 로그 제출
- 실습 중 12 V 전원을 분리하고 무전원 상태를 확인하는 안전 수칙을 전 과정에서 준수
source_ids:
- S10
- S24
- S11
---

### FSR 센서 신호 획득 원리
FSR(Force Sensing Resistor) 402는 인가되는 힘이 증가함에 따라 저항이 감소하는 가변 저항체입니다 [S10]. 센서 자체는 독립적인 전압을 생성하지 않으므로, MCU의 ADC(Analog-to-Digital Converter)로 측정하기 위해서는 **전압 분압 회로(Voltage Divider)**를 구성해야 합니다 [S24].

#### 전압 분압 회로 설계
전압 분압 회로의 출력 전압 $V_{out}$은 다음 식으로 정의됩니다:
$V_{out} = V_{ref} \times \frac{R_{fixed}}{R_{fixed} + R_{FSR}}$
여기서 $V_{ref}$는 센서 전원(3.3 V), $R_{fixed}$는 고정 저항(10 kΩ)입니다 [S24].
- **주의:** OpenCR 보드에서 FSR 센서 전원은 반드시 3.3 V 센서 전원 레일을 사용해야 합니다 [S11]. 5 V나 12 V 액추에이터 레일을 연결하면 ADC 회로가 영구 손상될 수 있습니다.

#### ADC 변환 및 정규화
OpenCR의 ADC는 12비트 해상도를 지원하므로, 0 V ~ 3.3 V 범위의 전압을 0 ~ 4095의 디지털 값으로 변환합니다 [S11]. 취득된 값은 센서의 비선형성을 고려하여 힘(N) 단위로 매핑하는 교정(Calibration) 과정이 필요합니다 [S10].
