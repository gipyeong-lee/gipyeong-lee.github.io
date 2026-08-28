---
layout: learn-module
title: 펌웨어 및 제어 프로그래밍
course_slug: precise-robot-hand
module_id: M6
permalink: /learn/precise-robot-hand/firmware-control/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: 3d1892052639494f98269f40443e7284
id: M6
slug: firmware-control
phase_id: PH3
estimated_hours: 15.0
prerequisites:
- M5
objectives:
- DYNAMIXEL 스마트 액추에이터 통신 및 제어 프레임워크를 이해한다.
- OpenCR 제어기를 통한 센서 데이터 취득 및 액추에이터 상태 모니터링을 구현한다.
- 제어 루프 내에서 FSR 센서 값을 이용한 파지력 피드백 알고리즘을 설계한다.
worked_examples:
- '액추에이터 위치 제어: DYNAMIXEL SDK를 사용하여 목표 관절 각도를 설정하고, 현 위치(Present Position) 데이터를 읽어와
  오차를 보정합니다 [S6].'
- 'FSR 힘 측정: ADC 값을 전압으로 변환하고, 센서의 저항 특성 곡선을 반영하여 현재 파지력을 뉴턴(N) 단위로 계산합니다 [B4, S14].'
lab:
  title: 로봇손 관절 구동 및 센서 데이터 취득 실험
  steps:
  - 각 분기별로 12V 전원 어댑터 3개를 독립적으로 연결하고 무부하 상태에서 전압을 측정합니다.
  - OpenCR 제어기에 펌웨어를 업로드하고 DYNAMIXEL 액추에이터 11대와 통신을 확인합니다.
  - 손가락 끝 FSR 센서를 3.3V 센서 레일에 연결하고 ADC 신호 범위를 0-3.3V 내에서 확인합니다.
  - 제어 코드를 실행하여 특정 손가락을 천천히 닫고 파지력을 모니터링합니다.
  safety:
  - 실험 전 반드시 3개 독립 전원 어댑터를 물리적으로 분리하고 멀티미터로 1V 이하임을 확인합니다 [B3].
  - 전원 인가 중에는 로봇손의 가동 범위 내에 손을 넣지 않습니다 [B3].
  - 회로 변경 시 반드시 전원을 차단하고 퓨즈를 통해 과전류로부터 보호합니다 [B3, B-WIRING-FUSE-HOLDER].
  deliverables:
  - 손가락별 액추에이터 위치 피드백 데이터 로그.
  - FSR 센서에서 취득한 원시 ADC 데이터 및 변환된 힘(N) 데이터 보고서.
assignment:
  title: 파지력 피드백 제어 구현
  deliverables:
  - 파지력 피드백이 포함된 관절 제어 소스 코드.
  - 센서 데이터 교정 기록 및 제어 성능 평가 보고서.
  rubric:
  - 액추에이터와 OpenCR 간 통신이 안정적으로 이루어지는가.
  - FSR 센서 데이터가 3.3V 레일에서 정확히 취득되는가.
  - 파지력 피드백 알고리즘이 목표 압력에 따라 관절 토크를 적절히 조절하는가.
quiz:
- question: FSR 402 센서를 OpenCR에 연결할 때 권장되는 전원 전압은 무엇입니까?
  choices:
  - 12V
  - 3.3V
  - 5V
  - 24V
  answer_index: 1
  explanation: OpenCR의 센서 회로 안정성과 ADC 입력 보호를 위해 반드시 3.3V 센서 레일을 사용해야 합니다 [B2].
- question: 제어 실험 중 전원이 인가된 상태에서 하드웨어를 접근해야 할 때의 올바른 절차는 무엇입니까?
  choices:
  - 퓨즈를 뽑고 저항 모드로 측정한다.
  - 전원 어댑터 3개를 물리적으로 모두 분리하고 DC 전압 모드로 측정하여 1V 미만임을 확인한다.
  - 멀티미터를 연속성 모드로 설정하여 소리가 나지 않으면 접근한다.
  - 제어 보드의 전원 LED가 꺼진 것을 보고 바로 접근한다.
  answer_index: 1
  explanation: 계획 정지 시스템이 없는 벤치 프로토타입에서는 물리적인 전원 분리와 DC 전압 측정이 유일한 안전 확인 방법입니다.
completion_criteria:
- 모든 DYNAMIXEL 액추에이터와의 통신 상태가 양호함.
- FSR 센서 ADC 값이 0-3.3V 범위 내에서 힘 변화를 정상적으로 반영함.
- 제어 코드에서 힘 데이터를 이용한 파지력 제한 알고리즘이 구현됨.
source_ids:
- S15
- S14
- S6
---

### DYNAMIXEL 제어 및 데이터 피드백
정교한 5지 로봇손은 XM430-W350-T 액추에이터를 사용하여 관절을 구동하며, OpenCR 1.0 제어기를 통해 제어 명령을 내리고 상태 데이터를 수집합니다 [B1, B2]. DYNAMIXEL Protocol 2.0은 위치, 속도, 전류 피드백을 지원하며, 이를 통해 실시간으로 로봇손의 관절 상태를 모니터링할 수 있습니다 [B1].

### FSR 센서 신호 처리
손끝에 배치된 FSR 402 센서는 가해진 힘에 따라 저항이 변하는 박막형 센서입니다 [B4, S14]. OpenCR의 12비트 ADC를 활용하기 위해 10kΩ 저항을 사용한 분압 회로를 구성합니다 [B2, B-SENSOR-RESISTOR]. 센서 전원은 반드시 OpenCR의 3.3V 센서 레일을 사용하며, 신호가 0-3.3V 범위를 초과하지 않도록 구성해야 합니다 [B2].
