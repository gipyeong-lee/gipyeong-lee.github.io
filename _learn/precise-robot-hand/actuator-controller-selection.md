---
layout: learn-module
title: 구동기 및 제어기 선정
course_slug: precise-robot-hand
course_data_key: precise-robot-hand
course_locale: ko
lang: ko
ref: learn:precise-robot-hand:actuator-controller-selection
translations:
- lang: ko
  url: /learn/precise-robot-hand/actuator-controller-selection/
- lang: en
  url: /learn/en/precise-robot-hand/actuator-controller-selection/
- lang: ja
  url: /learn/ja/precise-robot-hand/actuator-controller-selection/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/actuator-controller-selection/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/actuator-controller-selection/
module_id: M3
permalink: /learn/precise-robot-hand/actuator-controller-selection/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
primary_category: robotics-hardware
topics:
- robot-hands
- tendon-drive
- embedded-control
course_type: build_project
published_at: '2026-08-29T08:34:02+09:00'
id: M3
slug: actuator-controller-selection
phase_id: P1
estimated_hours: 10.0
prerequisites:
- M2
objectives:
- DYNAMIXEL XM430-W350-T 액추에이터의 정격 전압, 전류 및 통신 특성을 이해한다.
- OpenCR 1.0 제어기의 DYNAMIXEL 포트 구성 및 12V 전원 분리 구조를 숙지한다.
- FSR 402 센서와 10kΩ 저항을 이용한 전압 분압 회로를 설계한다.
- 시스템 전력 요구사항을 계산하고 독립 분기 퓨즈 보호 설계를 수립한다.
worked_examples:
- '예제 1: 분기당 최대 전류 확인. 분기 하나에 4개의 XM430 액추에이터를 연결할 경우, 스톨 전류의 합은 4 * 2.3A = 9.2A이다.
  이는 어댑터의 11.5A 정격 및 인라인 퓨즈의 10A 정격을 만족하며 안전한 범위를 유지한다 [S11, S15, S25].'
- '예제 2: FSR 분압 회로 전압 계산. 3.3V 공급 전압 하에서 FSR 저항이 R_fsr일 때, ADC 입력 전압 V_adc = 3.3 *
  (10k / (10k + R_fsr)) V가 된다. 센서 범위(0.2N~20N)에 따라 저항 변화를 확인하여 0~3.3V 범위를 넘지 않도록 보정한다
  [S12, S13, S26].'
lab:
  title: 전원 분기 구성 및 ADC 센서 인터페이스 실습
  steps:
  - 각 MEAN WELL 어댑터 출력에 0AFH0001Z 퓨즈 홀더를 연결하고 0287010 10A 퓨즈를 삽입한다.
  - 멀티미터를 DC 전압 모드로 설정하여 각 분기의 전압이 안정적인 12V인지 확인한다.
  - OpenCR의 3.3V 센서 레일에 10kΩ 저항과 FSR 402를 사용하여 분압 회로를 구성한다.
  - 비전원 상태에서 분압 회로의 출력 전압이 0~3.3V 범위 내에 있는지 확인한다.
  safety:
  - 작업 시작 전 3개 어댑터의 AC 전원을 물리적으로 차단하고 멀티미터로 0V임을 확인한다.
  - 충격 방지 작업용 보안경을 항시 착용한다.
  - 전원 인가 중에는 절대로 회로를 변경하거나 배선을 만지지 않는다.
  - 퓨즈는 과전류 차단용이며 계획 정지 수단이 아님을 명시한다.
  deliverables:
  - 각 분기별 12V 출력 측정값 기록지
  - FSR 분압 회로 조립 완료 사진
  - 구성된 배선도
assignment:
  title: 전원 분기 및 보호 설계 검토
  deliverables:
  - 전체 로봇 손의 전류 분기 배분 표(각 분기별 액추에이터 할당)
  - 선정한 퓨즈가 액추에이터 스톨 전류를 보호하면서 어댑터 용량을 초과하지 않음을 증명하는 계산서
  rubric:
  - 독립 퓨즈가 각 분기에 정확히 배치되었는가?
  - 액추에이터 분기 배분이 4/4/3으로 규정에 부합하는가?
  - 센서 전원이 12V가 아닌 3.3V 센서 레일에서 공급되는가?
quiz:
- question: FSR 402 센서와 10kΩ 저항을 사용한 분압 회로의 올바른 전원 연결은?
  choices:
  - 12V 액추에이터 전원
  - OpenCR 3.3V 센서 레일
  - 5V 범용 전원
  - OpenCR 12V 출력
  answer_index: 1
  explanation: OpenCR의 ADC 입력은 3.3V를 기준으로 동작하므로 전압 분압 회로는 반드시 3.3V 센서 레일에서 전원을 공급받아야
    합니다 [S13].
- question: XM430-W350-T 액추에이터의 스톨 전류값은?
  choices:
  - 1.0A
  - 2.3A
  - 4.1A
  - 11.5A
  answer_index: 1
  explanation: 데이터시트에 따르면 해당 액추에이터의 스톨 전류는 2.3A입니다 [S11].
- question: 전원 분기 설계에서 절대 금지된 행동은?
  choices:
  - 각 어댑터 출력에 퓨즈 장착
  - 어댑터의 양(+) 출력 병렬 연결
  - 분기당 10A 퓨즈 사용
  - 절연형 어댑터 사용
  answer_index: 1
  explanation: 어댑터의 양(+) 출력은 독립적인 분기로 유지해야 하며, 병렬 연결은 절대 금지됩니다 [B3].
completion_criteria:
- 실습에서 3개 독립 분기의 12V 전압을 멀티미터로 검증 완료
- FSR 402 센서 분압 회로의 배선과 ADC 입력 전압 범위 확인 완료
- 전원 분기 및 보호 설계 보고서 제출 및 통과
source_ids:
- S4
- S5
- S11
- S13
- S15
- S24
- S25
- S12
- S26
---

### 구동기 및 제어기 시스템 설계 이론

#### 1. 액추에이터 선정 및 전력 특성
로봇 손의 정밀 구동을 위해 DYNAMIXEL XM430-W350-T를 사용한다. 이 액추에이터는 12V 정격 전압에서 작동하며, 스톨(Stall) 전류는 2.3A이다 [S11]. 전체 로봇 손은 11개의 액추에이터로 구성되므로, 전체 스톨 전류 합계는 약 25.3A에 달한다. 따라서 안정적인 구동을 위해 독립적인 전원 공급 체계가 필요하다.

#### 2. 제어기 아키텍처
OpenCR 1.0은 216MHz ARM Cortex-M7 프로세서를 탑재하여 실시간 제어에 적합하다 [S13]. 이 제어기는 12V 액추에이터 전원과 로직/센서 전원을 물리적으로 분리할 수 있는 구조를 지원한다. FSR 센서와 같은 아날로그 입력은 0~3.3V 범위 내에서 처리해야 하므로, 센서 전압 분압 회로는 반드시 OpenCR의 3.3V 센서 레일에서 공급받아야 한다 [S13].

#### 3. 과전류 보호 및 전원 분기 설계
138W 출력의 MEAN WELL GST160A12-R7B 어댑터 3개를 사용한다 [S15]. 각 어댑터의 정격 전류는 11.5A이며, 이를 통해 독립적인 12V 분기를 3개 생성한다. 각 분기에는 10A ATOF 퓨즈를 인라인으로 장착하여 과전류 발생 시 회로를 보호한다 [S24, S25]. 퓨즈는 정격 전류 11.5A보다 낮게 설정하여 보호 협조를 달성한다.

#### 4. 센서 신호 취득
FSR 402는 압력이 증가하면 저항이 감소하는 특성을 가진다 [S12]. 이를 10kΩ 고정 저항과 전압 분압기로 연결하여 힘의 변화를 전압 신호로 변환하고 OpenCR의 12bit ADC 포트로 입력한다 [S12, S13, S26].
