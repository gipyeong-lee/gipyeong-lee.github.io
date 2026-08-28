---
layout: learn-module
title: 센싱 및 제어
course_slug: precise-robot-hand
module_id: m8
permalink: /learn/precise-robot-hand/sensing-integration/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: a31c540d33454e5489bdd6fde7912c13
id: m8
slug: sensing-integration
phase_id: p3
estimated_hours: 10.0
prerequisites:
- m6
- m7
objectives:
- FSR 402 센서와 분압 회로의 원리 이해 및 구성
- OpenCR 제어기의 ADC 기능 활용 방법 습득
- 센서 데이터 취득 시 신호 안정화 및 보정법 이해
- 손끝 접촉력 데이터를 활용한 제어 로직 구현 기초 습득
worked_examples:
- '1. 전압 분압 계산: 3.3 V 공급 환경에서 FSR 저항이 10 kΩ, 고정 저항이 10 kΩ일 때 분압 전압 V_out = 3.3 * (10k
  / (10k + 10k)) = 1.65 V.'
- '2. ADC 값 변환: 12비트 ADC에서 1.65 V는 (1.65 / 3.3) * 4095 = 2047.5, 즉 약 2048의 디지털 값으로
  취득됨.'
lab:
  title: FSR 센서 인터페이싱 및 데이터 취득
  steps:
  - 1. FSR 402 센서의 단자 두 곳을 각각 OpenCR의 3.3 V 센서 전원과 아날로그 입력핀에 연결한다 [S13].
  - 2. 아날로그 입력핀과 GND 사이에 10 kΩ 저항을 배치하여 분압 회로를 구성한다 [B-SENSOR-RESISTOR].
  - 3. OpenCR의 ADC 입력값을 실시간으로 시리얼 모니터링한다 [S14].
  - 4. 센서 표면에 점진적으로 힘을 가하며 ADC 데이터 변화량을 관찰한다.
  safety:
  - 모든 회로 구성 전 전원 어댑터가 물리적으로 분리되어 있는지 확인한다.
  - OpenCR의 아날로그 핀에 3.3 V 이상의 전압이 인가되지 않도록 주의한다.
  - 납땜 시 보호용 보안경을 착용하고 환기가 되는 환경에서 작업한다.
  - 전원 인가 후에는 배선 연결 부위의 과열 여부를 멀티미터로 확인한다.
  deliverables:
  - 회로 구성 사진
  - ADC 데이터 수치 기록지
  - 힘 변화에 따른 ADC 응답 그래프
assignment:
  title: 파지력 피드백 제어 로직 설계
  deliverables:
  - 센서 보정 함수 및 코드
  - 목표 접촉력 설정에 따른 텐던 구동 로직 보고서
  rubric:
  - 분압 회로의 정확한 결선 및 ADC 신호의 안정적 취득 여부
  - 센서 데이터의 선형성 또는 비선형성 보정 능력
  - 접촉력 피드백을 통해 텐던 장력을 제어하는 로직의 적절성
quiz:
- question: FSR 402 센서의 특징으로 올바른 것은 무엇입니까?
  choices:
  - 압력이 증가하면 저항이 증가한다.
  - 압력이 증가하면 저항이 감소한다.
  - 전압을 직접 출력하는 액티브 센서이다.
  - 정해진 하중 이상에서는 저항이 변하지 않는다.
  answer_index: 1
  explanation: FSR은 압력이 가해질수록 저항이 낮아지는 특성을 가집니다 [S13].
- question: OpenCR 제어기에서 FSR 신호를 읽기 위해 전압 분압 회로를 구성할 때 사용해야 하는 센서 전원 레일은?
  choices:
  - 12 V 액추에이터 전원
  - 5 V 전원
  - 3.3 V 센서 전원
  - 직접 외부 전원
  answer_index: 2
  explanation: OpenCR의 ADC는 3.3 V까지 허용하며, 센서 전용 레일인 3.3 V 사용을 권장합니다.
- question: 12비트 ADC를 사용하는 경우 출력될 수 있는 최대 디지털 값은 얼마입니까?
  choices:
  - '1023'
  - '2047'
  - '4095'
  - '8191'
  answer_index: 2
  explanation: 12비트 해상도는 2^12 = 4096개 값을 가지며, 0부터 4095까지 표시됩니다.
completion_criteria:
- 모든 센서 인터페이싱 회로의 정상 동작 확인
- ADC 데이터의 노이즈 없는 취득 및 정량화 완료
- 센서 피드백을 반영한 파지력 제어 구현 완료
source_ids:
- S13
- S27
- S14
---

### 힘 감지 센서(FSR) 원리
FSR(Force Sensing Resistor) 402는 압력이 증가함에 따라 저항이 감소하는 고분자 두께 막(PTF) 센서입니다 [S13]. 이 센서는 접촉력을 연속적인 아날로그 값으로 변환할 수 있어 로봇손의 파지력 피드백에 필수적입니다 [S13].

### 분압 회로(Voltage Divider) 구성
FSR은 단독으로 전압을 출력하지 않습니다. 따라서 OpenCR 제어기에서 읽을 수 있는 0~3.3 V 범위의 전압 신호로 변환해야 합니다.
- 센서와 10 kΩ 고정 저항 [B-SENSOR-RESISTOR]을 직렬로 연결하여 전압 분압기를 구성합니다.
- OpenCR의 3.3 V 센서 전원 레일을 사용하며, 센서에서 출력된 전압은 OpenCR의 12비트 ADC를 통해 디지털 값으로 변환됩니다 [S14].

### ADC 취득 및 신호 처리
OpenCR의 ADC는 최대 12비트 해상도를 제공하므로 0~4095의 디지털 값을 갖습니다 [S14]. 측정된 신호는 환경 노이즈나 기계적 진동으로 인해 불안정할 수 있으므로, 이동 평균 필터 등을 사용하여 신호를 안정화해야 합니다.
