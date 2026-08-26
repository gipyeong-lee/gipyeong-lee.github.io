---
layout: learn-module
title: 펌웨어 개발 및 제어 알고리즘
course_slug: precise-robot-hand
module_id: M7
permalink: /learn/precise-robot-hand/firmware-control/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: 55abc7c8ab224eebac7f5fce303e08e2
id: M7
slug: firmware-control
phase_id: PH3
estimated_hours: 15.0
prerequisites:
- M6
objectives:
- DYNAMIXEL Protocol 2.0 기반의 액추에이터 통신 체계 이해
- 실시간 제어 루프(Real-time Control Loop) 설계 및 펌웨어 최적화
- 센서 피드백을 활용한 폐루프 제어(Closed-loop Control) 구현
- 시스템 안전을 위한 상태기계(State Machine) 설계
worked_examples:
- '예제 1: DYNAMIXEL 위치 제어 주기 산출. 11대의 액추에이터를 Protocol 2.0으로 50Hz 제어 루프 내에서 처리하기 위해,
  통신 속도를 2Mbps로 설정하여 각 패킷 전송 시간을 최소화합니다.'
- '예제 2: FSR 센서 전압 분압 계산. 10 kΩ 저항을 사용하여 FSR 402와 분압 회로를 구성할 때, 센서 저항이 0.2N 접촉 시 약
  100 kΩ에서 20N 접촉 시 1 kΩ까지 변함에 따라 12-bit ADC 입력 범위를 최대로 활용하도록 오프셋을 설정합니다 [B4, B-SENSOR-RESISTOR].'
lab:
  title: 펌웨어 통합 및 안전 동작 검증
  steps:
  - OpenCR 1.0 보드와 11대 액추에이터를 개별 퓨즈 분기에 연결합니다.
  - 비상정지 버튼의 NC 접점이 EV200 코일 회로에 올바르게 결선되었는지 멀티미터로 도통 시험을 수행합니다.
  - 단일 손가락 펌웨어를 업로드하여 통신 및 위치 제어 동작을 확인합니다.
  - 11대 액추에이터 전체를 대상으로 Sync Write 기능을 활성화합니다.
  - 비상정지 푸시버튼 조작 시 모든 전원 분기가 차단되는지 멀티미터로 확인합니다.
  safety:
  - 반드시 벤치 전원의 전류 제한을 설정 후 배선하십시오.
  - 배선 작업 시에는 전원을 차단하고, 최종 검증 시 보안경을 착용하십시오.
  - 비상정지 버튼 테스트는 액추에이터가 부착되지 않은 상태에서 1차 수행하십시오.
  deliverables:
  - 전체 펌웨어 코드 베이스
  - 비상정지 차단 시간 측정 기록
  - 실시간 제어 루프 주기 로그
assignment:
  title: 제어 알고리즘 최적화 및 보고서
  deliverables:
  - 파지력 피드백을 포함한 제어 알고리즘 설계서
  - 펌웨어 소스 코드
  - 상태기계 다이어그램
  rubric:
  - Sync Write를 통한 동기화 제어 구현 여부
  - ADC 데이터를 활용한 FSR 보정 및 파지력 제어 알고리즘의 정확성
  - 비상정지 회로 및 안전 상태기계 로직의 무결성
quiz:
- question: 로봇손 펌웨어에서 사용되는 제어 통신 규격은 무엇입니까?
  choices:
  - DYNAMIXEL Protocol 1.0
  - DYNAMIXEL Protocol 2.0
  - Standard RS-232
  - EtherCAT
  answer_index: 1
  explanation: OpenCR 1.0과 XM430-W350-T 액추에이터 조합은 DYNAMIXEL Protocol 2.0을 통해 정밀한 피드백을
    제공합니다.
- question: 시스템 안전을 위해 비상정지 버튼이 직접적으로 제어하는 장치는 무엇입니까?
  choices:
  - 모든 액추에이터의 전원(+) 회로
  - EV200 접촉기의 코일 제어 회로
  - OpenCR 보드의 메인 CPU 전원
  - FSR 센서의 신호선
  answer_index: 1
  explanation: 비상정지 버튼은 직접 모터 전류를 차단하지 않고, EV200 접촉기의 NC 코일 회로를 개방하여 안전하게 차단합니다.
- question: ADC 해상도가 12-bit일 때 표현 가능한 값의 범위는 무엇입니까?
  choices:
  - 0 ~ 255
  - 0 ~ 1023
  - 0 ~ 4095
  - 0 ~ 65535
  answer_index: 2
  explanation: 12-bit 해상도는 2^12인 4096개의 단계를 가지며, 0부터 4095까지의 값을 표현합니다.
completion_criteria:
- 전체 11대 액추에이터의 실시간 위치 피드백 확인
- FSR 센서를 이용한 접촉력 데이터 정상 수신
- 비상정지 푸시버튼 동작 시 모든 전원 분기의 하드웨어 차단 검증 완료
source_ids:
- S12
- S7
---

## 펌웨어 구조 및 실시간 제어
로봇손의 펌웨어는 고성능 제어기인 OpenCR 1.0의 216MHz CPU를 활용하여 정밀한 제어 루프를 실행합니다 [S12]. DYNAMIXEL XM430-W350-T 액추에이터는 Protocol 2.0을 사용하여 위치, 속도, 전류 피드백을 실시간으로 제공하며, 제어 보드는 별도의 브리지 없이 이를 직접 통신합니다 [S12].

### 제어 루프 설계
안정적인 파지 성능을 위해서는 제어 주기가 일정해야 합니다. 펌웨어는 다음과 같은 순서로 실행됩니다:
1. **데이터 취득:** 5개 FSR 센서로부터 12-bit ADC 값을 읽어 접촉력을 산출합니다.
2. **상태 업데이트:** 액추에이터의 현재 위치와 부하 전류를 쿼리합니다.
3. **제어 연산:** 위치 제어와 전류 제한을 조합한 알고리즘을 수행합니다 [S7].
4. **명령 전송:** 계산된 목표값을 액추에이터에 동기화(Sync Write)하여 전송합니다.

### 상태기계(State Machine) 기반 안전 관리
시스템은 비상정지 입력을 상시 모니터링합니다. 비상정지 버튼은 EV200 접촉기의 코일 제어 회로(NC)를 차단하여, 하드웨어적으로 3개의 독립 액추에이터 분기를 즉시 비활성화합니다 [B10, B-SAFETY-CUTOFF].
