---
layout: learn-module
title: 센서 인터페이스
course_slug: precise-robot-hand
module_id: M8
permalink: /learn/precise-robot-hand/sensor-integration/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: 024057fbaaef48f6b3c3847511cb8b54
id: M8
slug: sensor-integration
phase_id: P3
estimated_hours: 10.0
prerequisites:
- M7
objectives:
- FSR 402 센서의 원리와 전압 분압 회로를 이해한다.
- OpenCR 제어기에서 아날로그-디지털 변환(ADC)을 통해 물리량을 취득한다.
- 센서 신호의 노이즈 처리 및 데이터를 파지 제어 알고리즘에 활용하는 방법을 배운다.
worked_examples:
- '예제 1: FSR 저항 계산. 특정 파지력에서 $R_{FSR}$이 5 kΩ으로 측정되었다면, $V_{ADC} = 3.3 V \times \frac{10k}{5k
  + 10k} = 2.2 V$입니다. 12-bit ADC 값은 $(2.2 / 3.3) \times 4095 \approx 2730$이 됩니다 [S16,
  S28].'
- '예제 2: 노이즈 필터링. FSR 신호는 손가락의 미세 진동으로 인해 흔들림이 발생합니다. 소프트웨어적으로는 `val_new = (val_prev
  * 0.9) + (val_raw * 0.1)`과 같은 1차 지수 이동 평균 필터를 적용하여 데이터를 안정화할 수 있습니다.'
lab:
  title: FSR 센서 인터페이스 구성 및 신호 취득
  steps:
  - 각 절연형 전원 어댑터 전원을 분리하고 무전원 상태를 멀티미터 DC 모드로 측정(1 V 미만 확인)한다.
  - OpenCR의 3.3 V 센서 전원 레일과 FSR, 10 kΩ 저항을 사용하여 분압 회로를 브레드보드에 구성한다 [S16, S28].
  - 전원 인가 전, 멀티미터 저항 모드로 배선 연결 및 단락 여부를 검증한다.
  - 12 V 액추에이터 전원과 3.3 V 센서 전원이 별도로 유지되는지 다시 확인한다 [B2].
  - 각 분기별 어댑터 전원을 인가하고, 시리얼 플로터로 FSR에 힘을 가할 때 ADC 값이 0~4095 사이에서 변하는지 확인한다.
  safety:
  - 모든 회로 수정은 3개 어댑터를 물리적으로 분리한 무전원 상태에서 수행한다.
  - ADC 입력은 0~3.3 V 범위를 초과하지 않도록 회로를 설계하고 검증한다 [B2].
  - 보안경을 착용하고, 고정된 지그에서 무부하 상태로 초기 신호 시험을 진행한다.
  deliverables:
  - ADC 값을 포함한 데이터 취득 코드(Arduino 스케치)
  - 측정된 센서 신호의 노이즈 필터링 적용 전후 시리얼 플로터 캡처 이미지
assignment:
  title: 파지력 피드백 구현
  deliverables:
  - 5개 손가락 FSR 센서 ADC 값을 읽어 파지력을 판단하는 로직 코드
  - 특정 ADC 임계값 도달 시 DYNAMIXEL 전류 제한 제어를 통한 파지 유지 알고리즘 보고서
  rubric:
  - 회로가 3.3 V 센서 레일을 정확히 사용하는가?
  - 센서 데이터가 필터링을 통해 안정적으로 갱신되는가?
  - 물리적인 FSR 접촉력을 ADC 값으로 성공적으로 매핑하는가?
quiz:
- question: OpenCR의 FSR 전압 분압 회로에서 센서 전원으로 적합한 전압은 무엇인가?
  choices:
  - 12 V 액추에이터 전원
  - 5 V 시스템 전원
  - 3.3 V 센서 레일
  - OpenCR VIN 전원
  answer_index: 2
  explanation: OpenCR 사양에 따라 아날로그 분압 회로는 반드시 3.3 V 센서 레일을 사용해야 하며, 12 V 액추에이터 전원과
    분리해야 안전합니다 [B2].
- question: FSR 402의 저항 특성은 어떠한가?
  choices:
  - 압력을 가할수록 저항이 증가한다.
  - 압력을 가할수록 저항이 감소한다.
  - 압력과 관계없이 저항이 일정하다.
  - 전압이 가해지면 저항이 무한대가 된다.
  answer_index: 1
  explanation: FSR(Force Sensing Resistor)은 물리적 힘이 증가할수록 내부 저항이 감소하는 특성을 가집니다 [S15].
completion_criteria:
- 5개 손가락의 FSR 센서가 모두 독립적으로 신호를 입력받음을 확인.
- ADC 취득 코드에 1차 지수 이동 평균 필터가 구현됨.
- 실험 중 어떠한 경우에도 12 V 전원이 3.3 V 센서 회로로 유입되지 않음을 계측으로 증명함.
source_ids:
- S15
- S28
- S16
---

### 힘 감지 센서(FSR) 인터페이스

FSR 402는 인가되는 힘에 따라 저항값이 감소하는 고분자 후막 센서입니다 [S15]. 힘이 없을 때는 수 MΩ 이상의 높은 저항을 가지며, 최대 20 N의 힘이 인가되면 수 kΩ 수준까지 저항이 낮아집니다 [S15].

#### 전압 분압 회로
OpenCR은 ADC(Analog-to-Digital Converter)를 사용하여 입력 전압을 디지털 값으로 변환합니다 [S16]. FSR은 직접적인 전압원이 아니므로, 10 kΩ 고정 저항을 직렬로 연결하여 전압 분압 회로를 구성해야 합니다 [S28].

- **회로 구성**: 3.3 V 센서 레일 - FSR - (ADC 입력 지점) - 10 kΩ 저항 - GND
- **출력 전압**: $V_{ADC} = 3.3 V \times \frac{R_{10k}}{R_{FSR} + R_{10k}}$

이 회로를 통해 힘이 증가하여 $R_{FSR}$이 감소하면, ADC 입력 전압($V_{ADC}$)은 0 V에서 3.3 V 사이로 상승합니다. OpenCR의 ADC는 12-bit 해상도를 가지므로 0~3.3 V 입력을 0~4095 사이의 디지털 값으로 매핑합니다 [S16].
