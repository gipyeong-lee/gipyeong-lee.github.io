---
layout: learn-module
title: 제어 코드 구현 및 프로그래밍
course_slug: precise-robot-hand
module_id: M9
permalink: /learn/precise-robot-hand/control-programming/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e444faa5055649a48877852af0b7303b
id: M9
slug: control-programming
phase_id: P3
estimated_hours: 10.0
prerequisites:
- M8
objectives:
- DYNAMIXEL 스마트 액추에이터의 제어 모드와 데이터 구조를 이해한다.
- Python을 활용하여 DYNAMIXEL 모터의 위치 및 속도를 제어하는 코드를 작성한다.
- Arduino Mega 2560과 스마트 액추에이터 간의 통신 프로토콜을 설정한다.
- 로봇손의 정교한 움직임을 위한 프로파일 제어 및 피드백 모니터링을 구현한다.
worked_examples:
- '### 예제 1: DYNAMIXEL 위치 제어 활성화 (Python)

  Python DYNAMIXEL SDK를 사용하여 모터의 토크를 활성화하고 특정 위치로 이동시키는 기본 로직입니다.

  ```python

  # Torque Enable

  packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_TORQUE_ENABLE, 1)


  # Goal Position 설정 (0~4095)

  packetHandler.write4ByteTxRx(portHandler, DXL_ID, ADDR_GOAL_POSITION, 2048)

  ```'
- '### 예제 2: 실시간 데이터 피드백 모니터링

  모터의 현재 위치와 온도를 읽어와 로봇손의 상태를 확인합니다.

  ```python

  # Present Position 읽기

  present_pos, _, _ = packetHandler.read4ByteTxRx(portHandler, DXL_ID, ADDR_PRESENT_POSITION)


  # Present Temperature 읽기

  present_temp, _, _ = packetHandler.read1ByteTxRx(portHandler, DXL_ID, ADDR_PRESENT_TEMPERATURE)


  print(f"Position: {present_pos}, Temperature: {present_temp}C")

  ```'
lab:
  title: 로봇손 관절 제어 실습
  steps:
  - DYNAMIXEL 전원 모듈(SMPS)과 Arduino/PC 통신 어댑터(U2D2)를 연결한다 [S40].
  - DYNAMIXEL Wizard 2.0 소프트웨어를 사용하여 모터 ID를 설정하고 동작 여부를 테스트한다 [S40].
  - Python 환경에서 SDK를 설치하고 특정 모터를 Position Control Mode로 설정한다.
  - 로봇손의 손가락 한 마디를 0도에서 90도까지 왕복하는 제어 코드를 작성하여 구동한다.
  - 프로파일 속도와 가속도를 변경하며 움직임의 부드러움을 비교한다.
  safety:
  - 반드시 저전압 벤치 전원 혹은 권장 전원 공급 장치(12V)를 사용한다 [S36, S37].
  - 모터 동작 중 손가락이 끼이지 않도록 주의한다 [S36].
  - 보안경을 착용하고 전원 단락이 발생하지 않도록 배선을 확인한다 [S36].
  - 비상 상황 발생 시 즉시 전원을 차단할 수 있는 장치를 마련한다.
  deliverables:
  - 정상 구동되는 손가락 관절 제어 Python 소스 코드
  - 모터 움직임의 프로파일 변경 전/후 영상 자료
  - 실습 중 측정한 전류 및 위치 데이터 기록
assignment:
  title: 5지 로봇손 파지 제어 알고리즘 구현
  deliverables:
  - 전체 5지 로봇손을 제어하는 파이썬 메인 컨트롤러 코드
  - 물체 파지 시 필요한 전류 기반 토크 제한 구현 기술서
  - 최종 로봇손 동작 테스트 보고서
  rubric:
  - 모든 손가락의 정교한 위치 제어 가능 여부 (40%)
  - 현재 전류 값을 기반으로 한 실시간 파지 힘 제어 구현 (30%)
  - 제어 코드의 가독성 및 문서화 수준 (20%)
  - 끼임 방지 등 안전 기능 포함 여부 (10%)
quiz:
- question: DYNAMIXEL의 제어 데이터 중 전원을 껐을 때 값이 초기화되는 영역은 무엇입니까?
  choices:
  - EEPROM 영역
  - RAM 영역
  - Flash 영역
  - ROM 영역
  answer_index: 1
  explanation: RAM 영역은 휘발성 메모리로, 전원을 끄면 저장된 데이터가 초기화됩니다.
- question: 로봇손 파지 시 과도한 힘을 방지하기 위해 권장되는 제어 모드는 무엇입니까?
  choices:
  - Velocity Control Mode
  - Position Control Mode
  - Current-based Position Control Mode
  - PWM Control Mode
  answer_index: 2
  explanation: Current-based Position Control Mode는 위치 제어와 함께 전류(토크) 제한을 동시에 적용할 수
    있어 안전한 파지에 적합합니다.
- question: DYNAMIXEL XM430 모터의 기본 통신 프로토콜 버전은 무엇입니까?
  choices:
  - Protocol 1.0
  - Protocol 2.0
  - Protocol 3.0
  - CAN
  answer_index: 1
  explanation: DYNAMIXEL-X 시리즈인 XM430은 Protocol 2.0을 기본으로 사용합니다.
completion_criteria:
- 실습 Lab의 모든 단계를 완료하고 정상 동작 확인
- 과제물의 제어 코드가 성공적으로 로봇손을 구동함을 증명
- 로봇손의 위치 제어 및 전류 기반 파지 제어 알고리즘 구현 완료
source_ids:
- S42
- S50
---

## DYNAMIXEL 제어 및 시스템 프로그래밍

정교한 5지 로봇손의 구현을 위해서는 모터의 위치, 속도, 전류를 실시간으로 제어할 수 있는 스마트 액추에이터 시스템이 필수적입니다. 본 모듈에서는 ROBOTIS DYNAMIXEL XM430 시리즈 액추에이터를 중심으로 제어 프로그래밍을 다룹니다 [S36, S38, S40].

### 1. DYNAMIXEL 제어 구조
DYNAMIXEL은 모터, 컨트롤러, 드라이버, 센서, 감속기가 통합된 지능형 액추에이터입니다 [S38, S40]. 제어는 **Control Table**이라 불리는 데이터 구조를 통해 이루어지며, 이는 RAM과 EEPROM 영역으로 나뉩니다 [S36, S41].
- **RAM 영역:** 전원을 끄면 초기화되는 휘발성 데이터로, 현재 위치(`Present Position`), 목표 위치(`Goal Position`), 토크 활성화(`Torque Enable`) 등의 제어/모니터링 데이터가 저장됩니다 [S36, S41].
- **EEPROM 영역:** 전원이 꺼져도 유지되는 비휘발성 데이터로, 모터 ID, 통신 속도(Baud Rate), 동작 모드(`Operating Mode`) 등의 설정값이 저장됩니다 [S36, S41].

### 2. 주요 제어 모드
로봇손의 손가락 관절 제어를 위해 주로 활용되는 모드입니다 [S38, S40]:
- **Position Control Mode:** 특정 각도(0°~360°)로 이동하여 고정합니다. 관절 위치 제어에 핵심적입니다 [S38, S41].
- **Current-based Position Control Mode:** 위치 제어와 함께 출력 전류(토크) 제한을 걸어, 물체를 잡을 때 과도한 힘이 가해지지 않도록 합니다 [S38, S41].
- **Profile Control:** 이동 시 가속도와 속도를 부드럽게 조절하여 급격한 움직임으로 인한 로봇손의 파손이나 떨림을 방지합니다 [S36, S40].

### 3. 하드웨어 연동 및 통신
본 프로젝트에서는 메인 제어기로 Arduino Mega 2560을 사용합니다 [S42, S44]. DYNAMIXEL의 디지털 패킷 통신(TTL 또는 RS-485)은 직렬 통신 프로토콜을 따르며, DYNAMIXEL SDK를 통해 Python 혹은 C++ 환경에서 라이브러리 형태로 손쉽게 제어할 수 있습니다 [S36, S40, S41].
