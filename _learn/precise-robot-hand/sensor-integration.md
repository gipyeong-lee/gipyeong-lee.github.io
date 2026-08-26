---
layout: learn-module
title: 센서 통합
course_slug: precise-robot-hand
module_id: m9
permalink: /learn/precise-robot-hand/sensor-integration/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: d9a7f912e090478cab017e340f4b3e42
id: m9
slug: sensor-integration
phase_id: phase3
estimated_hours: 10.0
prerequisites:
- m8
objectives:
- FSR 402 센서의 작동 원리와 저항 변화 특성을 이해한다.
- OpenCR 제어기에서 전압 분압 회로를 사용하여 아날로그 힘 신호를 취득하는 원리를 파악한다.
- 센서 신호의 잡음을 처리하고 실제 물리량(뉴턴)으로 변환하는 교정 절차를 익힌다.
- 3.3 V 센서 전원을 활용한 안전한 아날로그 회로를 구성한다.
worked_examples:
- '예제 1: 분압 전압 계산. 입력 전압 3.3 V, 고정 저항 10 kΩ, 현재 FSR 저항이 20 kΩ일 때 ADC 입력 전압은? 계산: 3.3
  * (20k / (20k + 10k)) = 3.3 * (2/3) = 2.2 V.'
- '예제 2: ADC 디지털 값 변환. 12-bit ADC는 0~4095 범위를 갖습니다. 예제 1의 2.2 V 전압이 ADC 값으로 변환되면?
  계산: (2.2 / 3.3) * 4095 = 2730.'
lab:
  title: FSR 힘 센서 회로 구성 및 데이터 취득
  steps:
  - OpenCR의 3.3 V 센서 전원 핀을 확인하고 분압 회로를 브레드보드에 구성합니다.
  - FSR 402의 한 단자를 3.3 V에, 다른 단자를 ADC 핀과 10 kΩ 고정 저항의 한쪽 끝에 연결합니다.
  - 10 kΩ 저항의 나머지 끝을 OpenCR의 GND에 연결합니다.
  - 멀티미터를 사용하여 회로 구성 후 센서에 힘을 가하지 않았을 때의 V_out 전압이 3.3 V에 가까운지, 힘을 가했을 때 전압이 감소하는지
    확인합니다.
  - OpenCR 펌웨어를 통해 12-bit ADC 값을 직렬 통신으로 PC에 출력하여 데이터의 변화를 확인합니다.
  safety:
  - 회로 연결 시 전원을 차단하고, 멀티미터로 3.3 V 레일과 GND 사이의 단락 여부를 반드시 확인하십시오.
  - 절대 12 V 액추에이터 전원이나 5 V 레일을 FSR 회로에 연결하지 마십시오.
  - 모든 배선은 진동에 빠지지 않도록 마감하고, 보안경을 착용하십시오.
  deliverables:
  - FSR 분압 회로 구성도(배선도 포함)
  - 다양한 힘을 가했을 때의 ADC 데이터 변화 표
  - 센서 교정 결과 그래프
assignment:
  title: 로봇손 파지력 피드백 시스템 구현
  deliverables:
  - 파지력 측정 함수가 포함된 로봇손 제어 코드(펌웨어)
  - 힘-전압 관계 교정 기록 보고서
  rubric:
  - 3.3 V 센서 전원을 올바르게 사용하여 ADC 입력을 0~3.3 V 범위 내로 구현하였는가?
  - 센서의 물리적 힘(N)과 디지털 출력(ADC) 간의 상관관계를 명확히 교정하였는가?
  - 비상시 센서 데이터 이상을 탐지하여 동작을 정지시키는 안전 로직을 포함하였는가?
quiz:
- question: OpenCR 제어기에서 FSR 전압 분압 회로를 구성할 때 가장 안전한 전원 공급 방법은 무엇입니까?
  choices:
  - 액추에이터용 12 V 전원
  - OpenCR의 3.3 V 센서 전용 레일
  - 별도의 5 V 전원
  - 액추에이터 통신 버스의 12 V 전원
  answer_index: 1
  explanation: OpenCR ADC 입력 보호 및 센서 사양 준수를 위해 반드시 3.3 V 센서 전용 레일을 사용해야 합니다.
- question: FSR 402의 힘과 저항의 관계는 무엇입니까?
  choices:
  - 힘이 증가하면 저항도 증가한다
  - 힘이 증가하면 저항이 감소한다
  - 힘과 저항은 관계가 없다
  - 힘이 증가하면 저항이 일정하게 유지된다
  answer_index: 1
  explanation: FSR은 압력이 가해질수록 전도층 접촉 면적이 넓어져 저항이 감소하는 특성을 가집니다.
- question: 12-bit ADC를 사용하는 OpenCR의 디지털 값 범위는 얼마입니까?
  choices:
  - 0 ~ 255
  - 0 ~ 1023
  - 0 ~ 4095
  - 0 ~ 65535
  answer_index: 2
  explanation: 12-bit 해상도는 2^12 = 4096개의 값을 가지므로 0에서 4095까지의 범위를 사용합니다.
completion_criteria:
- FSR 402 센서를 3.3 V 레일에 독립적으로 구성하여 안전하게 연결할 것.
- ADC 취득 값이 0~3.3 V 범위를 벗어나지 않음을 멀티미터로 검증할 것.
- 센서에 가해지는 힘에 따른 ADC 값 변화를 교정 데이터로 기록하고 제출할 것.
source_ids:
- S15
- S29
---

### 센서 통합 및 아날로그 신호 취득

#### 1. FSR(Force Sensing Resistor) 작동 원리
FSR 402는 압력이 가해질 때 저항이 감소하는 감압성 전도성 고분자 필름 센서입니다 [S15]. 센서 표면에 가해지는 힘이 증가할수록 전도층이 접촉하는 면적이 넓어져 전기 저항이 줄어듭니다 [S15]. 0.2 N에서 20 N 사이의 넓은 힘 범위를 감지할 수 있어 로봇손의 파지력 피드백에 적합합니다 [S15].

#### 2. 전압 분압 회로(Voltage Divider)
OpenCR의 ADC는 전압을 읽으므로, FSR의 저항 변화를 전압 신호로 변환해야 합니다. 이를 위해 고정 저항(10 kΩ)과 FSR을 직렬로 연결한 분압 회로를 구성합니다 [S29].
- 센서 전원: OpenCR의 3.3 V 센서 전용 레일 사용 (5 V나 12 V 액추에이터 전원 사용 절대 금지).
- 신호 범위: ADC 입력은 0~3.3 V 범위를 초과하지 않도록 설계합니다.
- 분압식: V_out = V_in * (R_fsr / (R_fsr + R_fixed)). 힘이 가해지면 R_fsr이 감소하여 V_out이 3.3 V에서 0 V 방향으로 변화합니다.

#### 3. 데이터 통합 및 처리
12-bit ADC를 사용하는 OpenCR에서 [S16], 취득된 디지털 값은 센서의 물리적인 힘(N)으로 변환되어야 합니다. 센서마다 고유한 비선형 특성이 있으므로, 표준 분동을 이용한 힘-디지털 값 테이블(Look-up Table) 또는 근사 함수를 사용하여 교정(Calibration)해야 합니다.
