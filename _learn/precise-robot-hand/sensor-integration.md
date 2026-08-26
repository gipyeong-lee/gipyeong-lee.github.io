---
layout: learn-module
title: 센서 인터페이스 및 피드백 처리
course_slug: precise-robot-hand
module_id: M8
permalink: /learn/precise-robot-hand/sensor-integration/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: 269a85a61ef242a9ad03b3d15be4bc06
id: M8
slug: sensor-integration
phase_id: PH3
estimated_hours: 15.0
prerequisites:
- M7
objectives:
- FSR 402 센서와 저항을 이용한 전압 분압 회로의 원리를 이해하고 설계한다.
- OpenCR 보드의 ADC(아날로그-디지털 변환) 기능을 활용하여 센서 데이터를 취득하고 처리한다.
- 센서 데이터를 필터링하고 물리량으로 변환하는 소프트웨어 구현 기법을 습득한다.
- 로봇손의 파지력 제어를 위한 피드백 루프의 구조를 설계한다.
worked_examples:
- '예제 1: 10 kΩ 고정 저항 사용 시 전압 계산

  FSR이 5 kΩ의 저항을 가질 때, 3.3 V 입력에서 $V_{out} = 3.3 \times (10 / (10 + 5)) = 2.2 V$가
  됩니다. ADC 값은 $(2.2 / 3.3) \times 4095 \approx 2730$으로 취득됩니다.'
- '예제 2: 단순 이동 평균 필터 구현

  최근 5개의 ADC 샘플값 $d_1, d_2, d_3, d_4, d_5$를 더한 뒤 5로 나누어 잡음을 제거합니다. `(d1+d2+d3+d4+d5)
  / 5.0`을 매 루프마다 연산하여 파지 제어 알고리즘의 입력값으로 사용합니다.'
lab:
  title: FSR 센서 인터페이스 구현 및 데이터 취득
  steps:
  - OpenCR의 3.3 V 센서 전원 레일과 GND를 사용하여 브레드보드에 FSR 402와 10 kΩ 저항으로 전압 분압 회로를 구성합니다 [S11,
    S12, S27].
  - 분압된 전압 출력 노드를 OpenCR의 아날로그 입력 핀(ADC 포트)에 연결합니다 [S12].
  - OpenCR 예제 코드를 수정하여 특정 핀의 ADC 값을 읽어 시리얼 통신으로 PC에 전송하도록 펌웨어를 작성합니다 [S12].
  - 손끝 센서에 다양한 무게의 물체를 접촉시키며 PC 시리얼 모니터에서 ADC 데이터의 변화를 확인합니다.
  - 소프트웨어 코드에서 이동 평균 필터를 적용하여 센서 접촉 시의 잡음이 감소하는지 확인합니다.
  safety:
  - 모든 전원 연결 전에는 멀티미터를 사용하여 회로의 단락(Short) 여부를 반드시 확인합니다.
  - ADC 입력 신호가 0~3.3 V 범위를 절대 초과하지 않도록 회로를 주의 깊게 배선합니다 [S12].
  - 5 V 또는 12 V 전원 라인을 센서 회로에 직접 연결하지 마십시오 [S12].
  - 회로 작업 시 보안경을 착용하십시오.
  deliverables:
  - 구성된 FSR 전압 분압 회로 사진
  - ADC 값을 취득하고 이동 평균 필터링을 수행하는 소스 코드
  - 센서 접촉 전후의 ADC 데이터 변화를 기록한 교정 데이터 테이블
assignment:
  title: 파지력 피드백 제어 시스템 구현
  deliverables:
  - FSR 데이터 기반의 파지력 추정 알고리즘 코드
  - 파지력의 변화에 따라 로봇손 관절의 토크 제한을 조정하는 로직 설명서
  - 실제 파지 실험을 통한 성능 검증 보고서
  rubric:
  - 전압 분압 회로의 올바른 구성 (3.3 V 사용 준수)
  - ADC 샘플링 및 이동 평균 필터의 정확한 구현
  - 측정된 ADC 값이 물리적 힘(N)으로 적절하게 매핑되는지 여부
  - 센서 입력값에 따른 액추에이터 토크 제어 연동성
quiz:
- question: FSR 402 센서와 전압 분압 회로 구성 시 OpenCR에서 권장되는 전원 레일은 무엇입니까?
  choices:
  - 12 V 액추에이터 전원
  - 5 V 전원
  - 3.3 V 센서 전원
  - 별도의 외부 24 V 전원
  answer_index: 2
  explanation: OpenCR의 ADC 입력은 3.3 V 범위 내에서 안전하게 작동하므로, 센서 회로는 3.3 V 센서 전원 레일에서 전력을
    공급받아야 합니다 [S12].
- question: 12비트 ADC를 사용하는 OpenCR에서 3.3 V 입력 시 출력되는 디지털 값은 얼마입니까?
  choices:
  - '1023'
  - '2047'
  - '4095'
  - '8191'
  answer_index: 2
  explanation: 12비트 해상도는 $2^{12} - 1 = 4095$의 범위를 가집니다 [S12].
completion_criteria:
- FSR 전압 분압 회로의 올바른 배선 및 OpenCR 아날로그 입력 정상 동작 확인
- 이동 평균 필터가 적용된 센서 데이터 취득 코드 작성 완료
- 실험을 통해 센서에 가해지는 물리적인 힘의 크기에 따라 ADC 값이 변화함을 검증
- 실습 결과물에 대한 안전 조치 및 교정 기록 작성
source_ids:
- S11
- S27
- S12
---

### FSR 센서와 전압 분압기
FSR(Force Sensing Resistor) 402는 가해지는 압력이 증가함에 따라 저항값이 감소하는 압력 가변 저항체입니다 [S11]. OpenCR의 ADC(12비트, 0~3.3 V 범위)를 사용하여 힘을 측정하려면 고정 저항과 FSR을 직렬로 배치한 전압 분압(Voltage Divider) 회로가 필요합니다 [S12, S27].

분압 회로의 출력 전압 $V_{out}$은 다음과 같이 계산됩니다:
$V_{out} = V_{ref} \times \frac{R_{fixed}}{R_{fixed} + R_{FSR}}$
여기서 $V_{ref}$는 3.3 V이며, $R_{fixed}$는 10 kΩ 저항입니다 [S27]. 이 회로를 통해 FSR의 저항 변화를 전압 신호로 변환하여 OpenCR이 읽을 수 있게 합니다.

### ADC 데이터 처리 및 변환
12비트 ADC는 전압을 0에서 4095까지의 정수값으로 변환합니다 [S12]. 취득된 원시 데이터(Raw Data)는 센서 특성상 잡음이 포함될 수 있으므로, 이동 평균 필터(Moving Average Filter)를 적용하여 안정적인 힘 값을 얻어야 합니다. 이후 측정된 전압 값을 힘(N)으로 변환하기 위해서는 해당 센서의 응답 곡선에 기반한 교정(Calibration) 데이터를 사용하거나 근사화된 함수를 적용합니다 [S11].
