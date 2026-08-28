---
layout: learn-module
title: 센서 피드백 알고리즘
course_slug: precise-robot-hand
module_id: M7
permalink: /learn/precise-robot-hand/sensor-integration/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: cb69d47af59949d9b2cf040d149dd749
id: M7
slug: sensor-integration
phase_id: PH3
estimated_hours: 12.0
prerequisites:
- M6
objectives:
- FSR 402 센서의 저항 변화 특성을 이해하고 전압 분압 회로를 설계할 수 있다.
- OpenCR 보드의 ADC(Analog-to-Digital Converter) 입력을 사용하여 센서 데이터를 취득할 수 있다.
- 데이터 필터링을 통해 불안정한 센서 신호를 로봇 제어에 활용 가능한 수준으로 정규화할 수 있다.
worked_examples:
- '예제 1: 10 kΩ 분압 저항 선택 이유. FSR이 0.2 N에서 수 MΩ, 20 N에서 수백 Ω의 저항을 가질 때, 10 kΩ은 측정 범위
  전반에서 ADC 입력이 3.3 V 센서 전원 레일을 초과하지 않게 하고, 유효한 전압 스윙을 보장합니다 [S11, S12, S23].'
- '예제 2: 12비트 ADC 값 계산. V_in=3.3 V, R_fixed=10 kΩ일 때, FSR 저항이 10 kΩ(압력 가해짐)이면 V_out=1.65
  V가 됩니다. ADC 값은 (1.65/3.3) * 4095 ≈ 2047이 출력됩니다 [S12, S23].'
lab:
  title: FSR 센서 신호 취득 및 필터링 실습
  steps:
  - OpenCR의 3.3 V 센서 레일과 GND를 이용해 브레드보드에 10 kΩ 분압 회로를 구성한다 [S12, S23].
  - FSR 402 센서를 손끝 프레임에 안착시키고 회로에 연결한다 [S11].
  - OpenCR ADC 핀을 분압기 출력에 연결하여 데이터를 읽는다 [S12].
  - 무부하 상태에서 10 N 정도의 압력을 가하며 시리얼 플로터로 ADC 값을 관찰한다.
  - 이동 평균 필터를 구현하여 시리얼 플로터상에서 신호의 떨림을 제거한다.
  safety:
  - 실험 중 전원을 인가하기 전, 멀티미터의 DC 전압 모드로 센서 단자의 전압이 3.3 V를 넘지 않는지 확인한다.
  - 절대로 12 V 액추에이터 전원을 센서 회로와 공유하지 않는다 [B2, B3].
  - 회로 수정이 필요할 때는 반드시 전원을 물리적으로 분리하고, 각 분기 전압이 1 V 미만으로 방전된 것을 확인한 후 접근한다.
  - 납땜 및 회로 구성 시 보안경을 착용한다.
  deliverables:
  - 센서 취득 및 필터링이 적용된 소스 코드
  - 필터 적용 전후의 센서 출력 데이터 비교 그래프
  - 측정된 힘(N)과 ADC 값의 선형 상관관계 기록
assignment:
  title: 손끝 접촉 피드백 루프 구현
  deliverables:
  - 센서 정규화 알고리즘 보고서
  - DYNAMIXEL 전류 피드백과 FSR 힘 데이터의 통합 제어 코드
  - 파지 시험 결과 및 데이터 기록
  rubric:
  - ADC 신호가 이동 평균 필터를 통해 안정적으로 출력되는가?
  - FSR 데이터가 0~20 N 범위로 정확히 매핑되는가?
  - 액추에이터 구동 중 센서 신호가 3.3 V 안전 범위 내에서 유지되는가?
quiz:
- question: OpenCR 보드에서 FSR 센서를 위한 ADC 입력 회로로 가장 적절한 것은?
  choices:
  - FSR 전압 분압기는 3.3 V 센서 전원만 사용하고 아날로그 입력 신호를 0~3.3 V 범위로 유지한다
  - 3.3 V 센서 전원 분압
  answer_index: 1
  explanation: OpenCR의 ADC 입력은 3.3 V 레퍼런스를 기준으로 동작하며, 12 V 전원 사용 시 보드가 파손될 수 있으므로
    반드시 3.3 V 센서 전원을 사용해야 합니다 [B2, S12].
- question: FSR 402 센서의 저항은 압력이 증가할 때 어떻게 변하는가?
  choices:
  - 저항이 증가한다.
  - 저항이 감소한다.
  answer_index: 1
  explanation: FSR(Force Sensing Resistor)은 압력이 가해지면 내부 도전성 레이어의 접촉 면적이 늘어나 저항이 감소하는
    특성을 가집니다 [S11].
- question: 센서 데이터 취득 시 이동 평균 필터를 사용하는 주요 이유는?
  choices:
  - ADC 해상도를 높이기 위해
  - 센서의 신호 노이즈를 줄이고 데이터를 안정화하기 위해
  answer_index: 1
  explanation: FSR 신호는 접촉 환경이나 전기적 노이즈에 의해 떨림이 발생할 수 있으므로, 이동 평균 필터를 통해 신호의 변동성을 완화하여
    제어의 안정성을 확보합니다.
completion_criteria:
- FSR 센서의 전압 분압 회로를 올바르게 구성하고 ADC 입력을 성공적으로 취득하였다.
- 이동 평균 필터를 적용하여 센서 노이즈를 10% 이하로 감소시켰다.
- 안전 규정을 준수하여 12 V 액추에이터 전원과 센서 전원을 물리적으로 격리하여 운용하였다.
source_ids:
- S11
- S23
- S12
---

### 힘 감지 센서(FSR)와 전압 분압 회로
FSR 402는 가해지는 압력이 증가함에 따라 저항이 감소하는 박막형 센서입니다 [S11]. 이 센서는 직접적으로 전압을 출력하지 않으므로, 제어 보드에서 이를 읽기 위해서는 전압 분압(Voltage Divider) 회로를 구성해야 합니다 [S11, S23].

#### 전압 분압기 설계
센서(R_FSR)와 고정 저항(R_fixed)을 직렬로 연결하고 양단에 3.3 V 전원을 인가합니다. OpenCR의 ADC 입력은 이 두 저항 사이의 전압(V_out)을 측정합니다 [S12].
\[ V_{out} = V_{in} \times \frac{R_{fixed}}{R_{FSR} + R_{fixed}} \]
여기서 10 kΩ 저항을 사용하면 [S23], FSR의 저항 변화에 따른 전압 변화를 ADC가 해석할 수 있는 0~3.3 V 범위 내로 유지할 수 있습니다 [S12, S23].

#### ADC 취득과 정규화
OpenCR의 ADC는 12비트 해상도를 제공하므로 0~4095의 디지털 값을 출력합니다 [S12]. 취득된 원시 데이터는 노이즈를 포함하므로, 이동 평균 필터(Moving Average Filter)를 적용하여 신호를 안정화한 뒤, 0.2 N~20 N 범위의 힘으로 매핑하는 정규화 과정을 거쳐 제어기에 전달합니다 [S11, S12].
