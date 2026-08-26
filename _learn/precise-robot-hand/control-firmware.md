---
layout: learn-module
title: 펌웨어 개발 및 DYNAMIXEL 제어
course_slug: precise-robot-hand
module_id: M6
permalink: /learn/precise-robot-hand/control-firmware/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: 7cd297f84fb948eaa8320ae5549cb1e4
id: M6
slug: control-firmware
phase_id: PH3
estimated_hours: 15.0
prerequisites:
- M5
objectives:
- DYNAMIXEL 스마트 액추에이터의 동작 원리와 제어 프레임워크인 Protocol 2.0을 이해한다.
- OpenCR 제어 보드를 활용하여 액추에이터 통신 및 센서 데이터 수집 펌웨어를 설계한다.
- 실시간 제어 루프에서 FSR 센서 데이터를 활용한 파지력 피드백 구현 방법을 습득한다.
- 제어 시스템의 운전 상태 기계(Safety State Machine) 설계 원리를 학습한다.
worked_examples:
- '예제 1: DYNAMIXEL 위치 제어 명령 발송

  OpenCR의 DYNAMIXEL Workbench 라이브러리를 사용하여 액추에이터의 Goal Position을 2048(중립)로 설정하는 코드
  예시입니다. `dxl_wb.goalPosition(id, 2048)` 함수를 통해 패킷을 발송하며, 응답 패킷을 통해 성공 여부를 확인합니다 [S14].'
- '예제 2: FSR 아날로그 전압의 힘(N) 변환

  FSR 402 센서로부터 취득한 0~4095(12비트) 값을 전압으로 변환 후, 선형 근사(Linear Approximation)를 통해 0.2~20
  N 범위의 힘으로 매핑합니다 [S7, S14]. 이때 3.3 V 레퍼런스를 기준으로 분압 공식을 적용하여 저항값을 먼저 산출하는 과정이 필수적입니다.'
lab:
  title: 펌웨어 구현 및 센서 데이터 검증
  steps:
  - OpenCR 1.0을 PC에 연결하고 개발 환경을 설정한다 [S14].
  - DYNAMIXEL XM430 1개를 OpenCR의 TTL 포트에 연결하고 통신 아이디를 설정한다 [S3, S14].
  - FSR 402를 10 kΩ 저항과 함께 3.3 V 센서 레일에 연결하여 분압 회로를 구성한다 [S7, S14, S27].
  - 액추에이터의 위치 제어 및 FSR 값 취득 펌웨어를 작성한다.
  - 무부하 상태에서 액추에이터를 가동하고, FSR 센서에 손가락으로 힘을 가하며 ADC 데이터가 변화하는지 확인한다.
  safety:
  - 절대 5 V 또는 12 V 액추에이터 전원을 FSR 분압 회로 공급원으로 사용하지 않는다 [S14].
  - 실험 중 정지는 3개 절연 전원 어댑터를 물리적으로 분리하고, 모든 분기에서 1 V 미만임을 멀티미터 DC 전압 모드로 확인한 뒤 접근한다.
  - 액추에이터 구동 시 가동 범위 내에 손을 넣지 않으며, 고정 지그에 장착하여 무부하 상태부터 시험한다.
  - 납땜 작업 시 보안경을 착용하고 환기가 되는 곳에서 작업한다.
  deliverables:
  - 작동하는 펌웨어 소스 코드
  - FSR 센서 ADC 데이터 변화 기록지
  - 이상 상황 발생 시 제어기 차단 로직(Safety Logic) 구현 증명 자료
assignment:
  title: 안전 기반 로봇손 제어 및 파지 피드백 설계
  deliverables:
  - 로봇손 제어 펌웨어 전체 소스 코드
  - 파지력 피드백 제어 논리 흐름도
  - 최종 프로젝트 보고서 (제어 설계 및 안전 검증 포함)
  rubric:
  - DYNAMIXEL과 정상 통신하며 위치 제어가 구현되었는가?
  - FSR 센서 데이터를 0~3.3 V 범위 내에서 올바르게 읽어오는가?
  - 액추에이터 피크 전류 대비 퓨즈 분기 및 운전 상태 기계 로직이 논리적인가?
  - 코드에 명확한 주석과 안전 조치에 대한 설명이 포함되었는가?
quiz:
- question: OpenCR 1.0 제어 보드에서 FSR 분압 회로에 공급해야 하는 전압은 얼마입니까?
  choices:
  - 12 V
  - 5 V
  - 3.3 V
  - 24 V
  answer_index: 2
  explanation: 교육용 프로토타입은 기계 안전 표준 준수나 인증을 주장하지 않으며, 사람 접근 환경 투입 전 자격 있는 안전 전문가의 별도
    검토가 필요하다 [S14].
- question: 실험 중 계획 정지가 필요할 때 취해야 할 가장 안전한 방법은 무엇입니까?
  choices:
  - 제어 소프트웨어의 'Stop' 버튼 클릭
  - 3개의 절연 전원 어댑터를 물리적으로 분리하고 계측 확인
  - 퓨즈를 뽑음
  - 메인 전원 스위치 차단
  answer_index: 1
  explanation: 이 프로토타입은 learner-built 정지 회로를 갖추고 있지 않으므로, 3개 분기 어댑터를 물리적으로 분리하고 전압을
    측정하여 에너지가 없음을 확인하는 것이 유일한 안전 절차입니다.
- question: DYNAMIXEL XM430-W350-T의 기준 전압은 무엇입니까?
  choices:
  - 5 V
  - 12 V
  - 24 V
  - 3.3 V
  answer_index: 1
  explanation: 데이터시트에 따르면 XM430-W350-T의 입력 전압 사양은 12 V입니다 [S3].
completion_criteria:
- 펌웨어 코드 내 운전 상태 기계 로직 구현 및 주석 작성 완료
- 멀티미터로 1 V 미만 확인 후 안전하게 접근하는 절차 수행 가능
- DYNAMIXEL Workbench를 통한 위치 제어 명령 성공
- FSR 데이터 변환 알고리즘의 유효성 실험 보고서 제출
source_ids:
- S14
- S3
- S7
- S27
- S16
---

### DYNAMIXEL 제어 및 펌웨어 설계

로봇손의 각 관절은 DYNAMIXEL XM430-W350-T 액추에이터를 통해 독립적으로 구동된다 [S3]. 이 액추에이터는 ROBOTIS의 Protocol 2.0을 사용하여 위치, 속도, 전류 피드백을 실시간으로 제공한다 [S3].

#### 1. 시스템 아키텍처
OpenCR 1.0 제어 보드는 216MHz ARM Cortex-M7 프로세서를 탑재하여 액추에이터와의 TTL/RS-485 통신을 직접 처리한다 [S14]. 외장 브리지 없이 내부 포트를 사용함으로써 통신 신뢰성을 확보하며, 12비트 ADC를 통해 FSR 402 센서 신호를 취득한다 [S14]. FSR 센서는 인가된 힘에 따라 저항이 감소하는 특성을 가지며, 10 kΩ 저항과 함께 분압 회로를 구성하여 OpenCR의 3.3 V 센서 레일로부터 정확한 전압 신호를 생성한다 [S7, S14, S27].

#### 2. 운전 상태 기계 (Safety State Machine)
펌웨어는 단순히 명령을 수행하는 것을 넘어, 시스템 상태를 지속적으로 모니터링해야 한다. 12 V 액추에이터 전원은 센서 회로와 전기적으로 분리되어 관리되며, 이상 전류 발생 시 퓨즈 분기 및 제어기의 동작 제한 로직이 작동한다 [S14, S16]. 펌웨어 레벨에서는 액추에이터의 온도, 전류, 전압 경고를 주기적으로 체크하여 위험 단계 진입 시 즉시 구동을 중단하고 'Safe' 상태로 천이하도록 설계해야 한다 [S3].
