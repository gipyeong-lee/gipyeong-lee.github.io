---
layout: learn-module
title: 펌웨어 개발 및 제어기 구현
course_slug: precise-robot-hand
module_id: m10
permalink: /learn/precise-robot-hand/firmware-controller/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: d9a7f912e090478cab017e340f4b3e42
id: m10
slug: firmware-controller
phase_id: phase3
estimated_hours: 10.0
prerequisites:
- m9
objectives:
- OpenCR 제어기의 구조와 펌웨어 배포 프로세스를 이해한다.
- 로봇손의 상태기계(State Machine)를 설계하고 C++로 구현한다.
- DYNAMIXEL SDK를 사용하여 액추에이터의 위치와 전류 피드백을 처리한다.
- FSR 센서 데이터를 아날로그 입력을 통해 처리하고 파지력 제어 알고리즘에 통합한다.
worked_examples:
- '예제 1: DYNAMIXEL 위치 제어 루프. 루프 내에서 `dxl_wb.syncWrite`를 사용하여 여러 액추에이터의 목표 위치를 동시에
  갱신하고, 상태기계의 현재 단계에 따라 속도 제한을 가변하는 방식을 구현한다 [S16].'
- '예제 2: FSR 센서 전압-힘 변환. 12-bit ADC 값(`raw`)을 입력받아 `Voltage = (raw / 4095.0) * 3.3`으로
  계산하고, 미리 측정된 힘-저항 곡선 데이터를 사용하여 선형 보간으로 실제 접촉력(N)을 추정한다 [S16, S15].'
lab:
  title: 로봇손 펌웨어 통합 및 안전 테스트
  steps:
  - OpenCR 제어기 회로를 연결하고 3.3 V 센서 전원 및 12 V 액추에이터 전원 분기를 검증한다.
  - FSR 센서의 ADC 값을 실시간 출력하여 노이즈 수준을 확인하고 필터를 설계한다.
  - 비상 정지 버튼을 누르고 DC 접촉기가 즉시 차단되는지 멀티미터로 전압을 측정한다.
  - 간단한 펌웨어 로직을 통해 10개의 액추에이터가 동시에 초기 위치로 이동하는지 테스트한다.
  safety:
  - 실험 시 항상 보안경을 착용한다.
  - 과전류 제한이 설정된 저전압 벤치 전원을 사용한다.
  - 액추에이터 구동 전 기구부 끼임 방지를 위해 비상 전원 차단 시스템이 동작하는지 먼저 확인한다.
  - 12 V 액추에이터 전원과 센서 회로의 전원을 분리하여 유지한다.
  deliverables:
  - 비상 정지 버튼 동작 및 전원 차단 확인 기록
  - 센서 데이터 취득 및 신호 처리 결과 보고서
  - 펌웨어 소스 코드 저장소 주소
assignment:
  title: 5지 로봇손 제어기 구현 보고서
  deliverables:
  - 로봇손 제어 상태기계 다이어그램
  - FSR 데이터 보정 및 파지력 제어 구현 C++ 코드
  - 안전 시스템(비상 차단) 검증 결과 보고서
  rubric:
  - 상태기계가 안전하게 동작하며 비상 상황 시 즉각적인 차단이 수행되는가?
  - DYNAMIXEL과 FSR 데이터를 효율적으로 처리하여 정밀한 제어가 가능한가?
  - 전원 분기 및 안전 규정을 정확히 준수하여 회로를 설계하고 테스트했는가?
quiz:
- question: OpenCR 제어기에서 FSR 402 센서 전압 분압 회로에 권장되는 전압원은 무엇인가?
  choices:
  - 12 V 액추에이터 전원
  - 3.3 V 센서 전원
  - 5 V 공통 전원
  - 24 V 입력 전원
  answer_index: 1
  explanation: OpenCR 사양에 따라 FSR 분압 회로는 3.3 V 센서 레일에서 전원을 공급받아야 하며, ADC 입력 신호를 안전하게
    관리해야 한다.
- question: 로봇손의 안전한 제어를 위해 비상 정지 버튼이 직접 제어해야 하는 부품은 무엇인가?
  choices:
  - 액추에이터의 12 V 주전원
  - EV200 접촉기의 코일 제어 회로
  - OpenCR의 메인 CPU 전원
  - FSR 센서 신호선
  answer_index: 1
  explanation: 비상 정지 버튼은 고전류 모터 전원을 직접 차단하지 않고, 저전류 제어 회로를 통해 DC 접촉기(EV200)의 코일을 해제하여
    3개의 독립 분기를 동시에 차단하도록 설계한다.
- question: DYNAMIXEL XM430-W350-T의 기준 동작 전압은 얼마인가?
  choices:
  - 5 V
  - 12 V
  - 24 V
  - 3.3 V
  answer_index: 1
  explanation: DYNAMIXEL XM430-W350-T 액추에이터의 기준 입력 전압은 12 V이다.
completion_criteria:
- 펌웨어 프로젝트 저장소에 제어 로직이 포함되어야 한다.
- 비상 정지 시스템의 전기적 차단이 멀티미터로 검증되어야 한다.
- FSR 데이터 처리 알고리즘이 ADC 입력 값에 대해 정상적으로 동작함을 확인해야 한다.
source_ids:
- S6
- S16
---

### OpenCR 제어기 및 로봇 펌웨어 아키텍처

OpenCR 1.0은 216MHz 주파수의 CPU를 탑재하여 로봇의 실시간 제어와 센서 데이터 취득을 담당한다 [S16]. 제어기는 액추에이터 통신(RS-485, TTL)과 아날로그 센서 입력을 통합 처리하여 외부 브리지 없이 안전한 상태기계를 실행하도록 설계되었다 [S16].

### 상태기계 설계 (Finite State Machine)
로봇손의 안전한 작동을 위해 다음 상태를 정의한다:
1. **INIT**: 모든 액추에이터 및 센서 초기화 확인.
2. **IDLE**: 명령 대기 상태.
3. **GRASP**: FSR 센서 피드백을 기반으로 한 파지 실행.
4. **EMERGENCY**: 비상 정지 입력 시 하드웨어 분기 차단 및 액추에이터 토크 해제.

### 센서 데이터 처리
FSR 402 센서는 전압 분압 회로를 사용하여 OpenCR의 ADC(12-bit)로 입력된다 [S16, S15]. 분압 저항(10 kΩ)을 통해 3.3 V 센서 레일에서 안정적인 신호를 얻으며, ADC 입력 범위 0~3.3 V를 초과하지 않도록 설계한다 [S16, S29].
