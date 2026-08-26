---
layout: learn-module
title: 펌웨어 개발 및 제어 로직
course_slug: precise-robot-hand
module_id: mod-8
permalink: /learn/precise-robot-hand/firmware-control/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: c6f6c4e7134945cb931d1d58c837a6d5
id: mod-8
slug: firmware-control
phase_id: phase-3
estimated_hours: 10.0
prerequisites:
- mod-7
objectives:
- DYNAMIXEL Protocol 2.0 패킷 통신 원리 이해
- 실시간 제어 시스템을 위한 ESP32 펌웨어 아키텍처 설계
- 힘 센서 피드백을 활용한 정밀 파지 제어 알고리즘 구현
- 안전 상태기계(Safety State Machine) 기반의 비상 정지 로직 구성
worked_examples:
- '통신 패킷 생성 예시: DYNAMIXEL의 특정 ID에 위치 명령을 내리기 위해 ''Instruction Packet''을 구성하고 Checksum을
  계산하여 송신하는 과정.'
- '힘 센서 맵핑 예시: FSR 센서 ADC 값을 0~4095에서 0~20N으로 매핑하고, 이를 액추에이터의 1024 스텝 토크 제한값으로 변환하는
  수식.'
- '비상 정지 루틴: 비상 정지 인터럽트 트리거 시, `detachInterrupt()`를 통해 시스템 정지 상태를 유지하고, 재부팅 전까지 제어
  루프를 완전히 중단하는 코드 구조.'
lab:
  title: 실시간 제어 루프 검증 및 비상 정지 시험
  steps:
  - ESP32와 DYNAMIXEL 간의 통신 확인 (Ping 패킷 테스트)
  - 힘 센서 가압 실험을 통한 ADC 피드백 안정성 확인
  - 비상 정지 버튼 구동 시 고전류 접촉기(EV200) 개방 동작 확인
  - 전류 제한 루프가 로봇손 구동 중 과부하를 감지하는지 시험
  safety:
  - 모든 테스트는 12V 저전압 벤치 전원 사용 필수 [bom-3]
  - 전류 제한 회로가 물리적으로 구성되었는지 확인 후 전원 인가
  - 로봇손 구동부 주변에 신체 접촉 금지 (끼임 방지)
  - 비상 정지 시스템 동작 검증 시 반드시 보안경 착용
  deliverables:
  - 제어 주기(주파수) 로그 데이터
  - 힘 센서-토크 변환 교정 기록
  - 비상 정지 동작 시간 측정 결과
assignment:
  title: 지능형 파지 제어 펌웨어 구현
  deliverables:
  - 제어 펌웨어 소스 코드 (.ino/.cpp)
  - 안전 상태기계 설계 문서
  - 파지력 성능 측정 보고서
  rubric:
  - DYNAMIXEL Protocol 2.0 통신 패킷 구현 정확도
  - 센서 데이터 기반 실시간 토크 피드백 제어 안정성
  - 비상 정지 신호 인지부터 전원 차단까지의 지연 시간
  - 코드의 가독성 및 안전 로직의 논리적 완결성
quiz:
- question: DYNAMIXEL XM430-W350-T 액추에이터 제어에 권장되는 통신 규격은 무엇인가?
  choices:
  - Protocol 1.0
  - Protocol 2.0
  answer_index: 1
  explanation: XM430 시리즈는 DYNAMIXEL Protocol 2.0을 사용합니다 [S5].
- question: FSR Model 402 센서의 감지 범위는?
  choices:
  - 0.2N ~ 20N
  - 1N ~ 100N
  answer_index: 0
  explanation: 해당 FSR 센서의 공식 사양은 0.2N에서 20N까지입니다 [bom-4].
- question: 비상 정지 버튼이 EV200 코일을 제어하는 방식은?
  choices:
  - NC 접점을 통해 전원 공급 차단
  - NO 접점을 통해 직접 전류 차단
  answer_index: 0
  explanation: 비상 정지 버튼의 NC 접점은 평소에 코일 전원을 통과시키다가, 눌리면 회로를 개방하여 코일 전원을 끊습니다 [B-SAFETY-CUTOFF].
completion_criteria:
- 모든 테스트 단계 완료 및 안전 기록 작성
- 비상 정지 시스템이 500ms 이내에 DC 버스를 차단함을 입증
- 힘 센서 피드백을 활용하여 물체를 미끄러지지 않게 파지하는 코드 검증
- 과제 제출 및 루브릭 기준 80점 이상 획득
source_ids:
- S5
---

### 펌웨어 아키텍처와 DYNAMIXEL 제어
로봇손 펌웨어는 고속 직렬 통신과 실시간 센서 루프를 안정적으로 처리해야 합니다. DYNAMIXEL XM430-W350-T는 Protocol 2.0을 통해 위치, 속도, 전류 피드백을 제공합니다 [S5]. ESP32는 240MHz 듀얼 코어를 활용하여 한 코어는 통신 및 제어 루프를, 다른 코어는 센서 데이터 취득 및 시스템 상태 모니터링을 분담합니다 [bom-2].

### 센서 융합 및 파지 제어
손끝 FSR 센서는 0.2N에서 20N까지의 접촉력을 감지합니다 [bom-4]. 펌웨어는 ADC 값을 변환하여 비선형적인 힘 데이터를 선형화한 후, 이를 타겟 전류값으로 환산하여 액추에이터 토크를 제어합니다. 파지 시에는 전류 제한 루프를 사용하여 과부하로부터 텐던과 모터를 보호합니다.

### 안전 제어 로직
시스템은 비상정지 푸시버튼 입력을 감지하는 전용 인터럽트를 가집니다 [bom-10]. 입력 발생 시, 펌웨어는 모든 DYNAMIXEL의 출력을 즉시 차단(Torque-off)함과 동시에 EV200 고전류 접촉기 코일의 전원을 끊어 전체 DC 버스를 물리적으로 분리합니다 [bom-10, B-SAFETY-CUTOFF].
