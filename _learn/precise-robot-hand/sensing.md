---
layout: learn-module
title: 촉각 센서 통합 및 검증
course_slug: precise-robot-hand
module_id: M8
permalink: /learn/precise-robot-hand/sensing/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: c47c267ad26a468f8562a7ad6bf075b5
id: M8
slug: sensing
phase_id: PH3
estimated_hours: 5.0
prerequisites:
- M7
objectives:
- 박막형 압력 센서(FSR)의 저항-압력 특성 이해
- 전압 분압 회로를 이용한 힘 측정 원리 학습
- OpenCR 제어기를 이용한 아날로그 신호 취득 및 데이터 교정
- 촉각 데이터를 로봇손 파지 제어 루프에 통합
worked_examples:
- '예제 1: FSR 출력 전압 계산. V_in=3.3V, R_fixed=10kΩ일 때, 센서 저항이 5kΩ으로 감소하면 V_out = 3.3 *
  (10 / (5 + 10)) = 2.2V가 됩니다.'
- '예제 2: 12비트 ADC 변환. V_out이 2.2V일 때, ADC 값 = (2.2 / 3.3) * 4095 ≈ 2730이 출력됩니다 [S14].'
lab:
  title: 촉각 센서 데이터 취득 및 분압 회로 구성
  steps:
  - OpenCR의 3.3V 센서 전원단과 ADC 입력 핀을 확인합니다 [S14].
  - FSR 402 센서의 두 단자 중 하나를 3.3V에, 다른 하나를 ADC 입력 핀에 연결합니다.
  - ADC 입력 핀과 GND 사이에 10kΩ 저항을 연결하여 분압기를 완성합니다 [S27].
  - 로봇손 끝에 센서를 배치하고 고정 지그에 장착합니다.
  - 멀티미터를 사용하여 센서 미가동 시 전압이 0V 부근인지 확인합니다.
  - 프로그램을 구동하여 미가동 시와 손으로 가압 시의 ADC 값 변화를 관찰합니다.
  safety:
  - 정비·접근 전 3개 독립 절연 전원을 물리적으로 분리하고, 멀티미터 DC 전압 모드로 각 분기 전압이 1V 미만인지 확인하십시오.
  - FSR 전압 분압 회로는 반드시 3.3V 센서 전원 레일에 연결하십시오. 12V 또는 5V 레일 연결 시 ADC 핀이 파손될 수 있습니다 [B2].
  - 시험 중 손을 로봇손의 가동 범위에 넣지 말고 고정 지그에서 무부하부터 가동하십시오.
  deliverables:
  - 회로 연결도
  - ADC 원시 데이터 로그
  - 힘-ADC 교정 곡선 데이터
assignment:
  title: 촉각 센서 기반 파지 제어 알고리즘 구현
  deliverables:
  - FSR 기반 힘 측정 함수 구현 코드
  - 힘 변화에 따른 로봇손 정지 임계값 설정 보고서
  - 파지 시험 영상
  rubric:
  - FSR 전압 분압 회로가 3.3V 레일을 사용하는지 확인
  - 취득한 데이터의 노이즈 제거 알고리즘 적용 여부
  - 임계 힘 도달 시 로봇손 모션 중단 기능의 정확성
quiz:
- question: FSR의 저항값은 압력이 증가할 때 어떻게 변화하는가?
  choices:
  - 증가한다
  - 감소한다
  answer_index: 1
  explanation: FSR은 압력을 받으면 저항이 감소하는 압력 감지 저항 센서입니다 [S13].
- question: OpenCR ADC 입력으로 분압 회로를 구성할 때 사용해야 하는 센서 전원은?
  choices:
  - 12V 액추에이터 전원
  - 3.3V 센서 전원
  answer_index: 1
  explanation: OpenCR의 ADC는 0~3.3V 범위를 지원하므로 3.3V 센서 전원을 사용해야 합니다 [B2].
- question: 분압 회로에서 FSR 저항이 0이 되면 ADC 입력 전압은 어떻게 되는가?
  choices:
  - 입력 전압(3.3V)과 같아진다
  - 0V가 된다
  answer_index: 0
  explanation: FSR 저항이 0이면 ADC 입력 핀은 3.3V와 직접 연결되어 V_in 전압을 출력합니다.
completion_criteria:
- FSR 전압 분압 회로의 올바른 배선 검증 (전압 1V 미만 확인)
- 센서 가압 시 ADC 데이터의 명확한 상승 추이 확인
- 구현된 제어 루프에서 센서 임계치 기반의 안전 정지 동작 확인
source_ids:
- S1
- S13
- S27
- S14
---

## 촉각 센서 통합의 원리

로봇손의 제어에서 촉각은 파지 안정성을 결정짓는 핵심 입력입니다. 본 프로젝트에서는 FSR 402 센서를 사용하여 손끝의 접촉력을 측정합니다. FSR(Force Sensing Resistor)은 압력이 가해질수록 저항이 감소하는 고분자 필름 센서로, 0.2N에서 20N 사이의 힘을 측정할 수 있습니다 [S13].

### 1. 전압 분압 회로 (Voltage Divider)
OpenCR 제어기의 ADC는 전압을 읽으므로, FSR의 저항 변화를 전압 신호로 변환해야 합니다. 이를 위해 10 kΩ 고정 저항(R_fixed)과 FSR(R_fsr)을 직렬로 연결하는 분압 회로를 구성합니다 [S27].

- 입력 전압 (V_in): OpenCR의 3.3V 센서 전원
- 출력 전압 (V_out): ADC 핀으로 입력되는 신호

V_out = V_in * (R_fixed / (R_fsr + R_fixed))

이 회로를 통해 FSR에 압력이 가해져 저항이 감소하면 V_out은 상승하며, 이를 OpenCR의 12비트 ADC(0~4095 값)로 취득합니다 [S14].

### 2. 신호 처리 및 교정
센서 원시 데이터는 비선형성을 가집니다. 따라서 실험을 통해 힘(N)과 ADC 값 사이의 매핑 테이블을 작성하거나 보간법을 사용하여 실시간 힘을 추정합니다 [S1]. 비접촉 시 측정되는 노이즈를 제거하기 위해 이동 평균 필터(Moving Average Filter)를 적용하는 것이 권장됩니다.
