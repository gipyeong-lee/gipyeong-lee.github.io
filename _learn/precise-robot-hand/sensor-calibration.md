---
layout: learn-module
title: 센서 데이터 처리 및 교정
course_slug: precise-robot-hand
module_id: M7
permalink: /learn/precise-robot-hand/sensor-calibration/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: d15f1f9bf2e148d5b847db3615e52388
id: M7
slug: sensor-calibration
phase_id: P3
estimated_hours: 10.0
prerequisites:
- M6
objectives:
- FSR(Force Sensing Resistor)의 물리적 동작 원리와 압력-저항 관계를 이해한다.
- 로봇손의 접촉 제어를 위해 FSR 데이터를 전압 신호로 변환하는 회로를 설계한다.
- 센서 출력 데이터의 비선형성을 보정하는 교정 알고리즘을 구현한다.
- 정밀한 파지력을 확보하기 위한 센서 데이터 필터링 기법을 습득한다.
worked_examples:
- '문제: FSR 402 센서가 $V_{cc}=5V$이고 $R_{fixed}=10k\Omega$인 분압 회로에 연결되어 있습니다. FSR 저항이
  $2k\Omega$일 때 ADC 출력 전압을 계산하세요. 해결: $V_{out} = 5 \cdot (2000 / (10000 + 2000)) =
  5 \cdot (2000 / 12000) \approx 0.833V$.'
- '문제: 센서 데이터에 노이즈가 많을 때 EWMA 필터 가중치 $\alpha=0.1$을 적용하는 코드 논리를 세우세요. 해결: $y_{filtered}[n]
  = \alpha \cdot x[n] + (1 - \alpha) \cdot y_{filtered}[n-1]$. 매 주기마다 현재 입력값에 0.1,
  이전 출력값에 0.9를 곱해 더합니다.'
lab:
  title: FSR 신호 응답 테스트 및 교정 실습
  steps:
  - 분압 회로(FSR + 10k옴 저항)를 브레드보드에 구성하고 멀티미터로 전압 변화를 확인합니다.
  - 마이크로컨트롤러(Arduino/ESP32)의 ADC 핀에 연결하여 힘을 가하지 않을 때와 최대 압력을 가할 때의 Raw 데이터를 기록합니다.
  - 정확한 무게를 가진 물체를 사용하여 5개 이상의 구간에서 힘(N) vs ADC 값 데이터를 수집합니다.
  - 수집된 데이터를 바탕으로 교정 계수를 계산하고, 코드에 적용하여 실제 힘(Newton) 단위로 출력되도록 수정합니다.
  safety:
  - 벤치 전원 사용 시 쇼트 방지를 위해 전류 제한 회로를 반드시 적용하십시오.
  - 회로 연결 시 전원 분리 상태에서 배선 상태를 재확인하십시오.
  - 센서 보호를 위해 너무 날카로운 물체로 직접 누르지 마십시오.
  deliverables:
  - 측정 데이터 로그 파일 (CSV)
  - 힘(N)으로 변환된 최종 제어 코드
  - 센서 응답 곡선 그래프
assignment:
  title: 로봇손 5지 파지력 균형 조정 과제
  deliverables:
  - 각 손가락별 센서 교정 계수 보고서
  - 파지력 보정 알고리즘 소스 코드
  - 물체 파지 시 안정성 테스트 결과서
  rubric:
  - FSR 센서의 비선형성을 보정하는 물리적 근거를 논리적으로 설명하였는가?
  - 다양한 물체에 대해 파지력이 일관되게 작용하도록 알고리즘이 설계되었는가?
  - 센서 데이터의 노이즈 처리 방법이 적절하게 구현되었는가?
quiz:
- question: FSR 센서의 압력-저항 특성에 대한 설명으로 옳은 것은?
  choices:
  - 압력이 증가하면 저항이 증가한다.
  - 압력이 증가하면 저항이 감소한다.
  - 압력과 저항은 아무런 상관이 없다.
  - 압력이 증가하면 전압이 항상 0이 된다.
  answer_index: 1
  explanation: FSR은 압력을 가할수록 센서의 저항값이 감소하는 압저항 센서입니다 [S18].
- question: 분압 회로에서 FSR을 사용하여 힘을 측정할 때 고정 저항의 역할은 무엇인가?
  choices:
  - 전압을 무한대로 증폭하기 위해
  - 회로의 전류를 완전히 차단하기 위해
  - 센서 저항 변화를 전압 신호로 변환하기 위해
  - 센서를 보호하는 퓨즈 역할
  answer_index: 2
  explanation: FSR은 가변 저항이므로 고정 저항과 함께 분압기를 구성하여 저항 변화를 전압으로 변환해야 ADC가 값을 읽을 수 있습니다.
completion_criteria:
- FSR 데이터 수집 및 물리 단위 변환 성공
- 교정된 알고리즘을 통한 로봇손 파지력의 정밀한 제어 수행
- 노이즈 필터링이 적용된 센서 데이터 출력 확인
source_ids:
- S18
---

### 1. FSR(Force Sensing Resistor)의 원리
FSR은 인가되는 압력에 따라 저항값이 감소하는 압저항(Piezoresistive) 특성을 가진 고분자 후막 센서입니다 [S18]. Interlink Electronics의 FSR 402 모델과 같은 장치는 인가된 힘이 증가할수록 전도성 층이 기판에 더 많이 접촉하여 회로의 총 저항을 낮추는 구조를 가집니다 [S18]. 이 센서는 0.2N에서 20N 사이의 힘을 측정할 수 있어 [S18] 로봇손의 손끝 접촉력 제어에 적합합니다.

### 2. 신호 변환 및 분압 회로
FSR은 자체적으로 저항값이 변화하는 수동 소자이므로, 마이크로컨트롤러가 읽을 수 있는 전압 신호로 변환해야 합니다. 가장 흔한 방법은 고정 저항(Reference Resistor)과 함께 분압 회로(Voltage Divider)를 구성하는 것입니다.

$$V_{out} = V_{cc} \cdot \frac{R_{FSR}}{R_{fixed} + R_{FSR}}$$

여기서 $R_{FSR}$은 센서의 저항, $R_{fixed}$는 고정 저항값입니다. 이 회로를 통해 힘이 가해질수록 $V_{out}$이 특정 방향으로 변화하게 됩니다.

### 3. 비선형성 보정 및 데이터 처리
FSR의 응답은 로그(log) 특성을 보이며 비선형적입니다. 정밀한 제어를 위해서는 다음과 같은 교정 단계가 필요합니다:
1. **데이터 수집(Calibration Curve):** 표준 분동을 사용하여 힘(N) 대 ADC 출력(V) 데이터를 수집합니다.
2. **커브 피팅(Curve Fitting):** 멱함수($F = a \cdot R^b$)나 다항식 근사를 통해 저항값을 힘의 단위로 변환합니다.
3. **노이즈 필터링:** 센서 신호는 진동에 민감하므로, 이동 평균 필터(Moving Average Filter)나 지수 가중 이동 평균(EWMA)을 적용하여 신호를 안정화합니다.
