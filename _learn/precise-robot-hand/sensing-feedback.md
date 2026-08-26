---
layout: learn-module
title: 촉각 센서 통합 및 캘리브레이션
course_slug: precise-robot-hand
module_id: M7
permalink: /learn/precise-robot-hand/sensing-feedback/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: 7cd297f84fb948eaa8320ae5549cb1e4
id: M7
slug: sensing-feedback
phase_id: PH3
estimated_hours: 10.0
prerequisites:
- M6
objectives:
- FSR 402 센서와 10 kΩ 저항을 활용한 전압 분압 회로 구성 원리 이해
- OpenCR 제어기의 12비트 ADC를 이용한 아날로그 신호 취득 및 정규화
- 센서 데이터의 물리적 힘(N)으로의 변환을 위한 캘리브레이션 절차 숙지
- 실시간 피드백 루프를 통한 로봇손 파지력 제어 기초 구현
worked_examples:
- '예제 1: 3.3 V 시스템에서 V_cc=3.3V, R_fixed=10kΩ일 때 FSR 저항이 5kΩ으로 낮아지면 V_out은 3.3 * (10
  / (5+10)) = 2.2V가 된다. 이는 ADC 값으로 약 2730으로 읽힌다.'
- '예제 2: 0.2 N 인가 시 ADC 값이 200, 20 N 인가 시 3800일 경우, 선형 근사식을 적용하여 힘 F = (ADC - 200)
  * (20 - 0.2) / (3800 - 200) + 0.2로 도출한다.'
lab:
  title: FSR 기반 손끝 힘 측정 회로 및 캘리브레이션 실습
  steps:
  - OpenCR의 3.3 V 센서 레일과 GND, ADC 핀을 확인한다.
  - FSR 402와 10 kΩ 저항을 이용하여 전압 분압 회로를 납땜하고 커넥터를 연결한다 [S7, S27].
  - 멀티미터를 DC 전압 모드에 두고 전원 인가 전 V_cc와 GND 간 단락 여부를 먼저 확인한다.
  - 전원 어댑터 3개를 분리한 상태에서 3.3 V 센서 전원을 측정하고 정상 확인 후 회로에 연결한다.
  - '무부하 상태와 알고 있는 하중(예: 100 g 분동) 인가 상태의 ADC 값을 기록한다.'
  - 기록된 데이터를 바탕으로 힘 변환 코드를 작성하고 시리얼 플로터로 확인한다.
  safety:
  - 전원 인가 전 반드시 멀티미터로 각 분기(12 V, 3.3 V)를 측정하여 쇼트 여부를 확인한다.
  - ADC 입력은 절대 3.3 V를 초과하지 않도록 회로를 설계하고 검증한다 [S14].
  - 모든 전원 연결은 물리적으로 분리된 3개의 절연 전원 어댑터 분기를 각각 사용한다 [S16].
  - 절대 3개 어댑터의 (+) 출력을 결합하지 않으며, 각 분기마다 10 A 퓨즈를 확인한다 [S16, S25, S26].
  deliverables:
  - 전압 분압 회로 배선도
  - 힘-ADC 데이터 보간표
  - 힘 측정 검증 영상
assignment:
  title: 손가락 파지력 피드백 구현
  deliverables:
  - 5개 손가락별 센서 캘리브레이션 리포트
  - 설정된 목표 힘 유지 제어 코드
  - 최종 로봇손 파지 시험 데이터 시트
  rubric:
  - ADC 신호가 3.3 V 범위를 안전하게 유지하는가?
  - 센서 보정이 하중별로 정확하게 구현되었는가?
  - 파지 제어 코드가 지정된 힘을 유지하며 동작하는가?
quiz:
- question: FSR 센서 회로 구성 시 OpenCR의 어떤 전압 레일을 사용해야 하는가?
  choices:
  - 12 V 액추에이터 전원
  - 3.3 V 센서 전원
  - 5 V 전원
  - 24 V 입력 전원
  answer_index: 1
  explanation: OpenCR의 ADC는 0~3.3 V 범위를 사용하며, 센서 전원을 사용해야 보드 손상을 방지할 수 있습니다 [S14].
- question: FSR 402의 센싱 범위는 얼마인가?
  choices:
  - 0.1 N ~ 10 N
  - 0.2 N ~ 20 N
  - 0.5 N ~ 50 N
  - 1 N ~ 100 N
  answer_index: 1
  explanation: FSR 402 데이터시트에 따르면 감지 범위는 0.2 N에서 20 N입니다 [S7].
completion_criteria:
- 5개 손가락 모든 센서의 캘리브레이션이 완료됨
- 힘 측정 데이터가 0~3.3 V 범위를 벗어나지 않음을 멀티미터로 검증함
- 파지력 피드백 코드가 10초 이상 목표 하중을 오차 범위 내에서 유지함
source_ids:
- S7
- S27
- S14
- S16
- S25
- S26
---

### 촉각 센서 통합 및 신호 처리

로봇손의 정교한 파지를 위해서는 손끝의 접촉력을 정량적으로 측정해야 합니다. FSR 402는 압력에 따라 저항이 감소하는 감압 센서로, 0.2 N에서 20 N 사이의 힘을 감지합니다 [S7].

#### 1. 전압 분압 회로 (Voltage Divider)
OpenCR은 아날로그 신호를 읽기 위해 ADC를 사용하므로, 저항 변화를 전압 변화로 바꾸어야 합니다. FSR(R_FSR)과 고정 저항(R_fixed = 10 kΩ)을 직렬 연결하여 분압 회로를 구성합니다 [S27].

- 출력 전압 V_out = V_cc * (R_fixed / (R_FSR + R_fixed))
- 이때, V_cc는 OpenCR의 **3.3 V 센서 전원**을 사용해야 합니다. 12 V 액추에이터 전원이나 5 V 전원을 사용하면 ADC 입력 범위를 초과하여 보드가 손상될 수 있습니다 [S14].

#### 2. ADC 및 신호 변환
OpenCR의 ADC는 12비트 해상도를 가지며, 0~3.3 V 범위를 0~4095 값으로 변환합니다 [S14].

- **정규화**: 취득된 ADC 값(0~4095)을 전압값으로 변환합니다: V_adc = (ADC_raw / 4095) * 3.3 V.
- **캘리브레이션**: FSR의 비선형적인 반응 곡선을 보정하기 위해, 알려진 무게(질량)를 센서에 인가하고 ADC 값을 기록하여 다항식 보간(polynomial interpolation) 또는 룩업 테이블(LUT)을 작성해야 합니다.
