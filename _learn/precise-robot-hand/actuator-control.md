---
layout: learn-module
title: 액추에이터 제어
course_slug: precise-robot-hand
module_id: m7
permalink: /learn/precise-robot-hand/actuator-control/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: d9a7f912e090478cab017e340f4b3e42
id: m7
slug: actuator-control
phase_id: phase3
estimated_hours: 10.0
prerequisites:
- m6
objectives:
- DYNAMIXEL 통신 프로토콜 2.0의 구조와 데이터 패킷 처리 이해
- 위치, 속도, 전류 제어 루프의 동작 원리 파악
- OpenCR 제어기를 이용한 안전한 액추에이터 제어 시스템 구성
- 힘 센서 신호를 ADC로 처리하여 폐루프 피드백 제어 구현
worked_examples:
- '목표 위치 설정: XM430 제어를 위해 Packet 구조(Header, ID, Length, Instruction, Parameters, Checksum)를
  생성한다. 예: `ID 1`에게 `Goal Position` 2048을 전송하는 패킷을 작성한다.'
- 'ADC 변환 예시: FSR 센서가 분압기 회로를 통해 1.5V를 출력할 때, 12bit ADC(최대 3.3V) 값은 `(1.5 / 3.3) *
  4095 = 1861`로 계산된다.'
lab:
  title: 액추에이터 제어 및 힘 피드백 통합 실습
  steps:
  - 각 액추에이터 분기에 독립 12V 어댑터를 연결하고 10A 퓨즈와 EV200 접촉기 상태를 점검한다.
  - OpenCR에 3.3V 센서 전원 레일을 연결하고 FSR 분압 회로를 구성한다.
  - DYNAMIXEL SDK를 사용하여 모터 통신 테스트(Ping)를 수행한다.
  - ADC 값을 읽어 모터의 전류 모드(Current Control Mode) 파라미터에 매핑하는 제어 코드를 작성한다.
  safety:
  - 반드시 보안경을 착용하고 작업을 진행한다.
  - 전원 인가 전 멀티미터로 3.3V 센서 레일과 12V 모터 레일의 쇼트 여부를 반드시 확인한다.
  - 이상 발열이나 탄 냄새가 나면 즉시 비상 정지 버튼을 누른다.
  - 절대 두 개 이상의 어댑터 양(+) 단자를 병렬로 연결하지 않는다.
  deliverables:
  - 통신 성공을 증명하는 터미널 캡처 로그
  - ADC 값에 따른 모터 전류 명령 결과 데이터
  - 비상 정지 버튼 동작 시 전원 차단 검증 영상
assignment:
  title: 5지 로봇손 파지 제어 알고리즘 구현
  deliverables:
  - 전류 모드를 활용한 파지력 조절 코드
  - 센서 피드백을 포함한 통합 제어 시스템 설계 보고서
  rubric:
  - OpenCR의 3.3V 센서 전원 사용 여부
  - 3개 분기 독립 전원 및 퓨즈/접촉기 안전 설계 반영
  - PID 루프와 전류 피드백의 안정적 구현
quiz:
- question: FSR 센서의 전압 분압 회로에 공급해야 하는 전압은?
  choices:
  - 12V 액추에이터 레일
  - 3.3V 센서 전원 레일
  - 5V USB 전원
  - 배터리 직접 연결
  answer_index: 1
  explanation: OpenCR의 ADC는 0~3.3V 범위에서 동작하며, FSR 센서 회로는 3.3V 센서 레일에서 공급받아야 정확하고 안전하다.
- question: 전원 분기 시스템의 안전 수칙으로 옳은 것은?
  choices:
  - 분기별 전원 양(+) 출력은 병렬로 연결한다.
  - 하나의 퓨즈로 10개 모터를 통합 보호한다.
  - 독립 전원 분기마다 퓨즈와 접촉기를 직렬로 배치한다.
  - 비상 정지 시 접촉기 코일은 무시한다.
  answer_index: 2
  explanation: 독립 분기를 구성하고 각각 보호 부품을 배치해야 과전류로부터 시스템을 안전하게 보호할 수 있다.
completion_criteria:
- 모든 10개 액추에이터가 독립 분기 전원을 통해 정상 통신함
- FSR 센서 ADC 입력이 3.3V 범위를 초과하지 않음이 확인됨
- 비상 정지 버튼 조작 시 3개 독립 전원 분기가 동시에 즉시 차단됨
- 전류 모드 제어를 통해 파지력이 소프트웨어로 조절됨
source_ids:
- S5
- S14
---

### 액추에이터 제어 기초

DYNAMIXEL XM430-W350-T는 내장된 PID 제어기를 통해 위치, 속도, 전류를 정밀하게 제어한다 [S14]. 통신은 Protocol 2.0을 사용하며, ID 기반 패킷 통신으로 데이지 체인 연결을 지원한다 [S5].

#### 제어 루프
- **위치 제어:** 목표 위치까지의 오차를 PID 알고리즘으로 보상하여 구동한다.
- **전류 제어:** 관절에 가해지는 토크를 전류를 통해 직접 제어하여 파지력을 조절한다.

#### 데이터 처리 및 안전
OpenCR 보드는 216MHz 클럭으로 동작하며 [S16], 12bit ADC를 통해 FSR 센서의 0~3.3V 신호를 변환한다. 모든 센서 회로는 3.3V 센서 전원 레일에서 분리되어 공급받아야 하며, 12V 액추에이터 전원과 전기적으로 분리(Isolation) 상태를 유지하여 노이즈를 방지한다.

#### 전원 및 비상 차단 시스템
시스템은 3개의 독립적인 12V 전원 분기를 사용한다 [S17]. 각 분기는 10A 퓨즈 [S28]와 EV200 접촉기를 직렬 배치한다 [S26]. 비상 정지 버튼 [S25]은 접촉기의 NC 코일 회로를 개방하여 모든 전원을 즉시 차단하는 안전 설계 방식을 따른다.
