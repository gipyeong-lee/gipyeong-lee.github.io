---
layout: learn-module
title: 제어 펌웨어 및 로직
course_slug: precise-robot-hand
module_id: m8
permalink: /learn/precise-robot-hand/firmware-development/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: 44d3a08daba248e5b900b0d5bdc9dc49
id: m8
slug: firmware-development
phase_id: phase-3
estimated_hours: 10.0
prerequisites:
- m7
objectives:
- DYNAMIXEL Protocol 2.0을 이해하고 액추에이터 상태를 제어합니다.
- OpenCR 제어기의 ADC를 활용해 힘 감지 센서(FSR) 신호를 처리합니다.
- 운전 상태 기계(Safety State Machine) 로직을 설계하여 과전류 및 센서 이상에 대응합니다.
- 모터 제어, 센서 취득, 동작 제한 로직이 통합된 단일 펌웨어 구조를 구축합니다.
worked_examples:
- '전류 피드백 기반 토크 제한: 액추에이터의 ''Present Current'' 레지스터 값을 읽어 2.0 A 초과 시 명령 토크(Goal Torque)를
  0으로 설정하여 스톨 방지.'
- 'FSR 신호 필터링: 이동 평균 필터(Moving Average Filter)를 적용하여 FSR 분압 전압의 고주파 노이즈를 제거하고 정밀한
  파지 감지 구현.'
- '안전 모니터링 루프: 메인 루프에서 ''System OK'', ''Warning'', ''Halt'' 3단계 상태기계를 통해 액추에이터 상태
  모니터링.'
lab:
  title: 실시간 데이터 취득 및 토크 제한 시험
  steps:
  - OpenCR에 12V 액추에이터 전원과 3.3V 센서 전원을 분리하여 연결합니다.
  - FSR 센서 1개를 OpenCR의 ADC 핀에 연결하고 멀티미터로 3.3V 레일 확인 후 무부하 시 신호 취득합니다.
  - DYNAMIXEL Protocol 2.0으로 액추에이터를 초기화하고 현재 전류(Present Current) 값을 읽어옵니다.
  - '소프트웨어적으로 전류 임계값(예: 1.5A)을 설정하고 이를 초과할 때 명령 속도를 0으로 제한하는 코드를 실행합니다.'
  - 손가락 모듈을 지그에 고정하고 부하를 가하며 토크 제한 로직이 작동하는지 시리얼 모니터로 확인합니다.
  safety:
  - 실험 중 정지는 3개 절연 전원 어댑터를 물리적으로 분리하고 멀티미터를 DC 모드로 설정하여 각 분기 전압이 1V 미만임을 확인 후 접근합니다.
  - 전원 인가 중 가동 범위 내에 손을 넣지 않습니다.
  - 과전류 발생 시 즉시 전원을 분리하고 배선 단락 여부를 확인합니다.
  - ADC 회로에 12V 액추에이터 전원이 유입되지 않도록 회로 분리를 재확인합니다.
  deliverables:
  - 전류 피드백 기반 토크 제한 구현 펌웨어 코드
  - FSR 데이터 선형화 및 필터링 결과 그래프
  - 상태기계 로직 전환 시험 결과 로그
assignment:
  title: 로봇손 펌웨어 시스템 구축 및 검증
  deliverables:
  - 모든 관절 및 센서 제어가 통합된 최종 펌웨어 소스 코드
  - 전류 및 힘 데이터 분석을 포함한 상태기계 작동 최종 보고서
  rubric:
  - Protocol 2.0을 이용한 액추에이터 제어 완결성
  - 3.3V 레일 기반 ADC 노이즈 제어 효율성
  - 운전 상태 기계의 논리적 오류 없는 구현
  - 코드 주석의 기술적 명확성
quiz:
- question: FSR 센서 신호 취득을 위해 사용할 OpenCR 전압 레일은?
  choices:
  - 12V 액추에이터 전원 레일
  - 3.3V 센서 전원 레일
  - 5V 범용 전원 레일
  - 외부 24V 배터리 레일
  answer_index: 1
  explanation: OpenCR의 ADC는 3.3V 기준이며, 시스템 안전과 정확도를 위해 전용 3.3V 센서 레일만 사용해야 합니다.
- question: 액추에이터의 전류 피드백을 모니터링하는 주된 이유는?
  choices:
  - 모터 회전 방향 결정
  - 통신 속도 최적화
  - 과전류에 의한 스톨 방지 및 안전 확보
  - 펌웨어 업데이트 시간 측정
  answer_index: 2
  explanation: 스톨 전류(2.3A) 초과를 감지하고 소프트웨어적 제한을 통해 하드웨어 손상 및 사고를 예방합니다.
- question: 실험 중 시스템을 안전하게 정지하는 올바른 절차는?
  choices:
  - 시리얼 명령으로 정지
  - 퓨즈를 뽑음
  - 어댑터 3개를 물리적으로 분리하고 DC 전압을 확인
  - 전원 스위치 하나만 끔
  answer_index: 2
  explanation: 비상 시에는 반드시 3개의 독립적인 절연 전원 어댑터를 분리하고, 멀티미터로 무전원(1V 미만) 상태임을 확인해야 합니다.
completion_criteria:
- 통합 제어 펌웨어 코드가 모든 관절 및 센서에 대해 정상 작동함
- 토크 제한 임계값 시험에서 과전류 발생 전 소프트웨어 차단이 검증됨
- 안전 정지 절차를 모든 실험 항목에서 준수함
source_ids:
- S9
- S11
- S10
- S24
- S13
- S23
---

### 제어 시스템 아키텍처
로봇손의 펌웨어는 실시간성과 안전성을 보장하기 위해 단일 OpenCR 제어기에서 루프를 운영합니다 [S11]. DYNAMIXEL XM430-W350-T 액추에이터는 Protocol 2.0을 사용하여 위치, 속도, 전류 피드백을 실시간으로 제공합니다 [S9]. OpenCR은 216MHz의 CPU 주파수를 활용하여 1ms 단위의 제어 루프를 실행하며, 12비트 ADC를 통해 0~3.3V 범위의 FSR 신호를 읽습니다 [S11].

### 센서 데이터 처리
FSR 402 센서는 인가된 힘에 따라 저항이 감소하는 원리를 이용합니다 [S10]. 10 kΩ 저항과 함께 분압 회로를 구성하여 OpenCR의 3.3V 센서 전원 레일로부터 공급받습니다 [S11, S24]. ADC 입력값은 비선형적인 힘 특성을 고려하여 구간별 선형화(Piecewise Linearization)를 적용합니다.

### 운전 상태 기계(Safety State Machine)
펌웨어는 각 액추에이터의 전류 피드백을 모니터링합니다. 액추에이터 스톨 전류(2.3 A)를 초과하거나 급격한 과전류가 감지될 경우, 시스템은 'Emergency Halt' 상태로 전이합니다 [S9]. 모든 전원 분기는 독립적으로 퓨즈 보호되지만, 펌웨어는 물리적 퓨즈 차단(10 A) 이전에 소프트웨어적으로 토크를 제한하여 안전성을 높입니다 [S13, S23].
