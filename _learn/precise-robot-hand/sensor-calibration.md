---
layout: learn-module
title: 센서 보정
course_slug: precise-robot-hand
module_id: M9
permalink: /learn/precise-robot-hand/sensor-calibration/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: ca4b0e25920a41ad92a16da990566600
id: M9
slug: sensor-calibration
phase_id: P3
estimated_hours: 5.0
prerequisites:
- M8
objectives:
- FSR 402 센서의 압력-저항 특성을 이해한다.
- OpenCR ADC 입력을 활용하여 힘 신호를 전압으로 변환하는 분압 회로를 설계한다.
- 센서 데이터를 보정하여 디지털값에서 실제 힘(N) 단위로 매핑하는 과정을 익힌다.
worked_examples:
- '예제 1: 센서 저항이 10 kΩ일 때 ADC 전압 계산. $V_{out} = 3.3V \times (10k / (10k + 10k)) = 1.65V$.
  12비트 ADC 값은 약 2048(0~4095)입니다 [S13].'
- '예제 2: 힘 증가에 따른 저항 감소. FSR 저항이 2 kΩ으로 낮아지면 $V_{out} = 3.3V \times (10k / (2k + 10k))
  = 2.75V$. ADC 값은 약 3413입니다 [S13].'
lab:
  title: 손끝 FSR 데이터 수집 및 보정 실습
  steps:
  - OpenCR의 3.3 V 센서 레일과 GND를 사용하여 FSR 402와 10 kΩ 저항으로 전압 분압 회로를 구성합니다 [S13, S25].
  - 분압된 전압 노드를 OpenCR의 ADC 입력 핀에 연결합니다 [S13].
  - 제어 코드를 실행하여 무부하 상태의 ADC 초기값을 기록합니다.
  - 알려진 무게(표준 분동)를 센서에 가하여 힘(N)과 ADC 값의 상관관계를 표로 작성합니다.
  - 비선형 보간법을 사용하여 ADC 데이터를 힘(N)으로 변환하는 보정 함수를 작성합니다.
  safety:
  - 모든 전원 분기는 반드시 10 A ATOF 퓨즈를 통과해야 합니다 [S24].
  - 전원 인가 전 멀티미터를 사용하여 3.3 V 센서 레일이 다른 전원과 단락되지 않았는지 확인합니다.
  - 테스트 중 전원 공급장치 3개를 물리적으로 분리한 후 1 V 미만임을 확인하기 전까지 손을 가동 범위에 넣지 않습니다.
  - 실험 중 보안경을 필수로 착용합니다.
  deliverables:
  - 보정 전후의 힘-ADC 값 비교 그래프
  - 센서 보정 보정 상수 파라미터 테이블
  - FSR-ADC 데이터 취득 코드
assignment:
  title: FSR 데이터 보정 보고서
  deliverables:
  - 최종 센서 보정 알고리즘 소스 코드
  - 힘 측정 오차 분석 보고서
  - 보정 함수의 선형성 개선 방안
  rubric:
  - 분압 회로의 전기적 연결이 명세와 일치하는가
  - 보정 함수의 힘 단위 변환 정밀도가 만족스러운가
  - 안전 수칙을 준수하여 계측하였는가
quiz:
- question: FSR 402 센서를 OpenCR에 연결할 때 권장하는 아날로그 전원 전압은 무엇입니까?
  choices:
  - 12 V
  - 5 V
  - 3.3 V
  - 0 V
  answer_index: 2
  explanation: OpenCR의 ADC는 3.3 V를 기준으로 하며, 센서 회로는 3.3 V 센서 전원을 사용해야 합니다 [S13].
- question: 분압 회로에서 FSR에 가해지는 힘이 증가하면 출력 전압은 어떻게 변합니까?
  choices:
  - 증가한다
  - 감소한다
  - 변하지 않는다
  - 0 V가 된다
  answer_index: 0
  explanation: FSR은 힘이 증가하면 저항이 감소하여 $V_{out} = V_{ref} \times (R_{fixed} / (R_{FSR}
    + R_{fixed}))$ 식에 따라 $V_{out}$이 증가합니다.
completion_criteria:
- ADC 전압 신호가 0~3.3 V 범위 내에 있음을 확인
- 5개 손끝 센서 모두 0.2 N~20 N 범위에서 정상 작동 확인
- 데이터 보정 완료 및 최종 보고서 제출
source_ids:
- S12
- S25
- S13
- S24
---

### FSR 센서의 동작 원리
FSR(Force Sensing Resistor) 402는 압력에 따라 저항값이 감소하는 박막형 센서입니다 [S12]. 이 센서는 힘이 가해지지 않았을 때 매우 큰 저항(수 MΩ 이상)을 가지며, 최대 20N의 힘이 가해질 때까지 저항이 비선형적으로 감소합니다 [S12].

### 전압 분압 회로 설계
OpenCR 보드의 ADC(아날로그-디지털 변환기)는 0~3.3 V 범위의 전압을 12비트 해상도로 디지털화합니다 [S13]. FSR을 ADC에 연결하려면 고정된 10 kΩ 저항 [S25]을 사용하여 전압 분압 회로를 구성해야 합니다. 회로의 출력 전압 $V_{out}$은 다음과 같이 정의됩니다:
$$V_{out} = V_{ref} \times \frac{R_{fixed}}{R_{FSR} + R_{fixed}}$$
여기서 $V_{ref}$는 3.3 V 센서 전원이며, $R_{fixed}$는 10 kΩ입니다. 이를 통해 센서의 저항 변화를 전압 신호로 취득할 수 있습니다 [S25].
