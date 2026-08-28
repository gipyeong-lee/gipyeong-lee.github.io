---
layout: learn-module
title: 센서 보정
course_slug: precise-robot-hand
module_id: M7
permalink: /learn/precise-robot-hand/sensor-calibration/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: 3d1892052639494f98269f40443e7284
id: M7
slug: sensor-calibration
phase_id: PH3
estimated_hours: 10.0
prerequisites:
- M6
objectives:
- FSR 402 센서와 10 kΩ 저항을 활용한 전압 분압 회로를 이해하고 구성한다.
- OpenCR 제어 보드의 ADC 채널을 통해 센서의 아날로그 신호를 디지털 값으로 변환한다.
- 센서 출력 값을 물리적인 힘(N)으로 변환하기 위한 보정 곡선을 생성한다.
- 센서 보정 과정에서 발생하는 오차 요인을 파악하고 재현성 있는 데이터를 확보한다.
worked_examples:
- '예제 1: 전압 분압기 계산. FSR 저항이 5 kΩ일 때, 3.3 V 입력에서 ADC 입력 전압을 구하시오. 풀이: $V_{out} = 3.3
  \times (10 / (10 + 5)) = 3.3 \times 0.666 = 2.2$ V. ADC 값: $(2.2 / 3.3) \times 4095
  = 2730$.'
- '예제 2: 12비트 ADC 데이터 이해. 측정된 ADC 값이 1024일 때, 입력 전압을 구하시오. 풀이: $(1024 / 4095) \times
  3.3 = 0.825$ V.'
lab:
  title: FSR 힘 센서 보정 실습
  steps:
  - OpenCR의 3.3 V 센서 레일과 GND를 사용하여 FSR 402와 10 kΩ 저항으로 전압 분압 회로를 구성한다 [B2, B4, B-SENSOR-RESISTOR].
  - 구성한 회로를 OpenCR의 ADC 핀에 연결하고, 시리얼 통신을 통해 무부하 상태의 ADC 값을 100회 측정하여 평균을 구한다.
  - '표준 분동(예: 0.5 N, 1 N, 2 N, 5 N, 10 N)을 손끝에 인가하며 ADC 값을 기록한다.'
  - 측정된 (힘, ADC 값) 데이터를 바탕으로 보정 곡선을 도출한다.
  safety:
  - 실습 중 3개 절연 전원 어댑터를 물리적으로 분리하고, 멀티미터 DC 전압 모드로 각 분기 전압이 1 V 미만인지 확인한 후 배선한다.
  - ADC 입력은 반드시 0~3.3 V 범위를 유지하며, 12 V 액추에이터 전원과 혼용하지 않는다.
  - 계획 정지 시 모든 전원 어댑터를 벽면 콘센트에서 물리적으로 분리한다.
  deliverables:
  - 센서 보정 데이터 표 (힘 N, 평균 ADC)
  - 힘-ADC 값 보정 그래프
  - 보정 함수가 포함된 로봇 손 제어 코드
assignment:
  title: 센서 보정 보고서 작성
  deliverables:
  - 센서 보정 데이터가 포함된 실습 보고서
  - 측정된 오차의 원인 분석 및 해결 방안
  rubric:
  - 전압 분압 회로의 올바른 연결 여부
  - 다양한 힘에 따른 ADC 데이터의 정밀도
  - 보정 곡선의 선형성 또는 비선형 보정 모델의 타당성
quiz:
- question: FSR 402 센서와 함께 사용하는 10 kΩ 저항의 용도는 무엇인가?
  choices:
  - 전압 분압기를 구성하여 ADC로 읽을 수 있는 전압 신호를 생성하기 위함
  - 센서의 전류 소모를 제한하여 과열을 방지하기 위함
  answer_index: 0
  explanation: FSR은 저항값만 변하는 가변 저항이므로, 전압 신호로 변환하기 위해 고정 저항과의 직렬 연결(전압 분압기)이 필요합니다.
- question: OpenCR 제어기에서 아날로그 신호를 읽을 때 주의사항은 무엇인가?
  choices:
  - 입력 전압이 0~3.3 V 범위를 초과하지 않아야 함
  - 반드시 12 V 액추에이터 전원과 같은 레일을 사용해야 함
  answer_index: 0
  explanation: OpenCR의 센서 전원은 3.3 V이며, 12 V 액추에이터 전원과 회로가 분리되어야 합니다 [B2].
completion_criteria:
- 실습 결과물로 FSR 센서가 힘에 따라 ADC 값이 변경됨을 확인해야 함.
- 작성된 제어 코드가 센서 값을 물리적인 힘(N)으로 정상적으로 변환해야 함.
- 안전 수칙을 준수하고 실습 완료 후 무전원 상태를 확인해야 함.
source_ids:
- S14
- S28
---

## 센서 보정 원리

FSR 402는 인가되는 힘이 증가함에 따라 저항이 감소하는 특성을 가진 박막형 힘 센서입니다 [S14]. 로봇 손의 정밀한 파지력을 제어하기 위해서는 센서의 아날로그 전압 출력을 물리적인 힘 단위인 뉴턴(N)으로 변환해야 합니다.

### 전압 분압 회로
FSR 402를 OpenCR의 ADC(Analog-to-Digital Converter)로 읽기 위해서는 저항과의 직렬 연결을 통한 전압 분압 회로가 필요합니다 [B2, B4]. 10 kΩ 저항을 사용하며 [B-SENSOR-RESISTOR], 전압($V_{out}$)은 다음과 같이 계산됩니다:

$$V_{out} = V_{ref} \times \frac{R_{fixed}}{R_{fixed} + R_{FSR}}$$

여기서 $V_{ref}$는 3.3 V 센서 전원이며, $R_{fixed}$는 10 kΩ입니다. OpenCR은 12비트 ADC 해상도를 가지므로, 0~3.3 V 입력을 0~4095 사이의 정수 값으로 변환합니다 [B2].

### 데이터 보정
센서의 저항값은 힘에 따라 비선형적으로 변하므로, 0.2 N에서 20 N 사이의 범위를 다루기 위해 다항 회귀(Polynomial Regression)나 룩업 테이블(Look-up Table) 방식을 사용하여 데이터를 보정해야 합니다 [S14].
