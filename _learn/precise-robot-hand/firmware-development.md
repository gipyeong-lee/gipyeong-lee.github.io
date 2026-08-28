---
layout: learn-module
title: 펌웨어 개발 및 제어
course_slug: precise-robot-hand
course_data_key: precise-robot-hand
course_locale: ko
lang: ko
ref: learn:precise-robot-hand:firmware-development
translations:
- lang: ko
  url: /learn/precise-robot-hand/firmware-development/
- lang: en
  url: /learn/en/precise-robot-hand/firmware-development/
- lang: ja
  url: /learn/ja/precise-robot-hand/firmware-development/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/firmware-development/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/firmware-development/
module_id: M7
permalink: /learn/precise-robot-hand/firmware-development/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
id: M7
slug: firmware-development
phase_id: P3
estimated_hours: 15.0
prerequisites:
- M6
objectives:
- DYNAMIXEL 스마트 액추에이터 통신 및 제어 프레임워크 이해
- OpenCR 제어 보드를 활용한 액추에이터 및 FSR 센서 신호 취득 구현
- 실시간 로봇 제어 상태기계 및 폐루프 피드백 루프 설계
- 안전한 전원 관리 및 토크 해제 시퀀스 프로그래밍
worked_examples:
- '1. 액추에이터 목표 위치/전류 설정: DYNAMIXEL SDK를 사용하여 XM430 액추에이터의 전류 제한(Goal Current)을 설정하고,
  센서값에 따른 PID 루프를 통해 손가락 관절의 최종 위치를 업데이트하는 예제.'
- '2. FSR 전압 데이터 필터링: ADC에서 수집된 원시 데이터의 노이즈를 제거하기 위해 이동 평균 필터(Moving Average Filter)를
  적용하고, 상한(20N)과 하한(0.2N) 범위를 정규화하는 코드 구현 [S12].'
lab:
  title: 로봇 손 통합 제어 및 정밀 파지 실습
  steps:
  - 각 독립 분기의 전압이 1V 미만인지 멀티미터 DC 모드로 확인한 후 조립을 시작한다.
  - OpenCR의 3.3V 센서 레일에 FSR 전압 분압 회로를 납땜하고 ADC 포트에 연결한다.
  - DYNAMIXEL SDK를 사용하여 11개 액추에이터의 ID를 스캔하고 초기 위치를 설정한다.
  - 무부하 상태에서 손가락 관절 구동 명령을 테스트하며 텐던 신율과 장력을 조절한다.
  - FSR 센서 데이터를 시리얼 모니터로 시각화하며 파지력 응답을 튜닝한다.
  safety:
  - 절대 5V 또는 12V 액추에이터 전원을 FSR 센서 회로의 공급 전원으로 사용하지 않는다.
  - 시스템 통전 중에는 절대 손가락 가동 범위에 접근하지 않으며 고정 지그를 사용한다.
  - 전원 분기 어댑터의 양(+) 단자를 절대 서로 연결하지 않는다.
  - 정비·조립 접근 전, 반드시 3개의 전원 어댑터를 물리적으로 분리하고 모든 분기에서 1V 미만임을 계측 확인한다.
  deliverables:
  - 실시간 센서 데이터 피드백이 포함된 펌웨어 소스 코드
  - 전압 분압 데이터의 정규화 및 교정 데이터시트
  - 액추에이터 피드백 루프 정상 작동 로그
assignment:
  title: 파지 상태기계 설계 및 구현
  deliverables:
  - 파지 및 파지 해제 상태기계 다이어그램
  - 전류 기반 토크 제어 구현 코드
  - 최종 성능 평가 보고서
  rubric:
  - 센서값에 따른 전류 제한 범위(0-2.3A)가 안정적으로 제어되는가?
  - 토크 해제 명령 시 물리적 장력이 즉시 제거되는가?
  - 코드 내에 안전한 하드웨어 분리 절차가 명시되어 있는가?
quiz:
- question: FSR 402 센서와 전압 분압 회로 구성 시 권장되는 전원 레일은 무엇입니까?
  choices:
  - 12V 액추에이터 전원 레일
  - 5V 범용 전원 레일
  - OpenCR 3.3V 센서 레일
  - 24V 외부 입력 레일
  answer_index: 2
  explanation: 시스템 안전과 OpenCR ADC 보호를 위해 FSR 분압 회로는 반드시 3.3V 센서 전원 레일에 연결해야 합니다.
- question: 로봇 손 정비 시 시스템이 '무전원 상태'임을 확인하는 올바른 방법은 무엇입니까?
  choices:
  - 소프트웨어로 토크 해제 명령을 보낸다.
  - 멀티미터 저항 모드로 배선 상태를 확인한다.
  - 멀티미터 DC 전압 모드로 모든 분기에서 1V 미만인지 계측한다.
  - 전원 분기 퓨즈를 제거한다.
  answer_index: 2
  explanation: 물리적 전원 분리 후 반드시 멀티미터 DC 전압 모드로 모든 분기의 잔류 전압이 1V 미만인지 직접 확인해야 합니다.
- question: 여러 독립 전원 어댑터 출력의 양(+) 단자를 병렬로 연결해도 됩니까?
  choices:
  - 전류 합산을 위해 필요하다.
  - 절대 금지된다.
  - 정격 출력 전류가 같으면 가능하다.
  - 퓨즈를 장착하면 가능하다.
  answer_index: 1
  explanation: 독립 분기로 구성된 전원 어댑터의 양(+) 출력은 서로 연결하거나 통합해서는 절대 안 됩니다.
completion_criteria:
- 각 분기별 독립 전원 공급 및 퓨즈 보호가 BOM 사양에 따라 구성되었음을 멀티미터로 검증 완료
- OpenCR ADC를 통한 5개 FSR 센서의 정밀한 힘 신호 취득 및 필터링 확인
- 소프트웨어 토크 해제 루틴과 물리적 전원 차단 후 계측 절차를 완벽히 수행
- 파지 상태기계가 의도대로 액추에이터와 센서 데이터를 처리하고 최종 보고서가 제출됨
source_ids:
- S13
- S11
- S12
---

### 펌웨어 아키텍처 및 DYNAMIXEL 제어
로봇 손의 펌웨어는 고속 루프 내에서 센서 데이터를 취득하고 액추에이터 명령을 처리합니다. `OpenCR 1.0` 제어기는 216MHz ARM Cortex-M7 프로세서를 기반으로 [S13], 별도의 브리지 없이 DYNAMIXEL 프로토콜 2.0을 처리하여 [S11] 지연 시간을 최소화합니다. 각 액추에이터는 전류, 속도, 위치 모드를 지원하며, 로봇 손은 전류 제어를 통한 토크 기반 파지 전략을 사용합니다.

### FSR 힘 피드백 시스템
FSR 402 센서는 가해진 힘에 반비례하는 저항 특성을 가집니다 [S12]. OpenCR의 12비트 ADC를 사용하여 [S13] 3.3V 센서 레일에서 10kΩ 저항과 전압 분압 회로를 구성합니다. 분압된 전압은 `ADC값 = (V_in * R_fsr) / (R_fsr + R_ref)`를 통해 정규화되며, 이 값은 손가락의 텐던 장력과 연동되어 파지력 피드백으로 사용됩니다.

### 안전한 제어 루틴
시스템 정지는 안전을 위해 두 단계로 나뉩니다. 소프트웨어 단계에서는 액추에이터 토크를 해제(Torque Off)하여 물리적 구동력을 즉시 제거합니다. 정비 전 반드시 3개 독립 전원 어댑터의 전원을 물리적으로 분리한 뒤, 멀티미터 DC 모드를 사용하여 모든 분기에서 1V 미만임을 확인해야 합니다.
