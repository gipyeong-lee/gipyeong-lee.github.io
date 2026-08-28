---
layout: learn-module
title: 배선 및 안전한 전원 분리 구축
course_slug: precise-robot-hand
course_data_key: precise-robot-hand
course_locale: ko
lang: ko
ref: learn:precise-robot-hand:wiring-safety-system
translations:
- lang: ko
  url: /learn/precise-robot-hand/wiring-safety-system/
- lang: en
  url: /learn/en/precise-robot-hand/wiring-safety-system/
- lang: ja
  url: /learn/ja/precise-robot-hand/wiring-safety-system/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/wiring-safety-system/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/wiring-safety-system/
module_id: M6
permalink: /learn/precise-robot-hand/wiring-safety-system/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
id: M6
slug: wiring-safety-system
phase_id: P2
estimated_hours: 10.0
prerequisites:
- M5
objectives:
- 액추에이터 구동을 위한 독립적 12 V 전원 분기 구성 방법을 이해한다.
- 과전류 보호를 위한 ATOF 퓨즈의 역할과 선정 원리를 학습한다.
- 안전한 전원 관리 및 물리적 차단 프로토콜을 습득한다.
- OpenCR 제어기 및 FSR 센서의 안전한 전압 분압 회로를 구성한다.
worked_examples:
- 이상 발열·냄새·연기 감지 시 접근하지 말고, 위험 구역 밖에서 사전 지정된 건물 분전반 차단기 또는 인증된 upstream master disconnect로
  3개 어댑터의 공급 전원을 차단한 뒤 대피한다. 위험 구역 밖에서 작동 가능한 upstream 차단 수단이 없으면 시스템 통전을 금지한다. 토크
  해제는 전원 차단을 대신하지 않는다. 정비·접근은 계획 정지 후 물리적 분리 및 무전원 계측 확인 뒤에만 수행한다 [S11] [S25]
- '예제 2: FSR ADC 회로 전압 - OpenCR의 3.3 V 센서 레일을 사용해 10 kΩ 분압 저항과 FSR 402를 연결합니다 [S13,
  S26]. 센서 신호 전압은 0~3.3 V 범위 내에 있어야 하며, 이 회로는 12 V 액추에이터 전원 회로와 물리적/전기적으로 분리하여 보호합니다.'
lab:
  title: 전원 분기 하네스 제작 및 안전 점검
  steps:
  - 각 어댑터 출력 라인에 ATO 인라인 퓨즈 홀더를 납땜하고, 10 A ATOF 퓨즈를 삽입합니다 [S24, S25].
  - Molex Micro-Fit 3.0 커넥터를 사용하여 액추에이터 및 센서 연결 하네스를 제작합니다 [S14].
  - OpenCR 보드와 각 액추에이터를 3개 분기로 배분하여 배선하고 각 전원 어댑터로 연결합니다 [S13].
  - 전원 인가 전, 각 어댑터 출력 단자의 절연 상태를 멀티미터 저항 모드로 확인합니다.
  - 전원 인가 후, 전압 모드에서 각 분기가 12 V임을 확인하고, 차단 시 반드시 3개 어댑터를 모두 제거합니다.
  safety:
  - 정비 전 3개 전원 어댑터를 물리적으로 분리할 것.
  - 잔류 전압이 1 V 미만임을 멀티미터로 확인한 후 부품을 교체할 것.
  - 전원 인가 중 가동 범위 내에 손을 넣지 말 것.
  - 모든 결선부는 절연 처리하고, 납땜 시 보안경을 착용할 것.
  deliverables:
  - 제작된 전원 분기 하네스 사진
  - 각 분기별 측정 전압 기록지
  - 배선도 검토 확인서
assignment:
  title: 안전 배선 설계 보고서
  deliverables:
  - 3개 전원 분기의 액추에이터 할당 설계안 (분기당 4대/4대/3대)
  - 각 분기별 과전류 차단 계산서 (피크 전류와 퓨즈 정격 비교)
  - 계획 정지 후 정비·접근 전 3개 전원 어댑터를 물리적으로 분리하고 각 분기의 무전원 상태를 계측 확인한다
  rubric:
  - 전원 독립성과 분리 원칙을 준수했는가?
  - 퓨즈와 커넥터의 정격이 부하에 적절하게 선정되었는가?
  - 전원 분리 및 잔류 전압 확인 프로토콜이 안전 지침을 따르는가?
quiz:
- question: 각 전원 어댑터의 12 V 출력(+)을 병렬로 연결해도 되는가?
  choices:
  - 가능하다, 전류 공급 능력이 높아진다.
  - 불가능하다, 독립 분기로 유지해야 한다.
  - 전압이 일치하면 가능하다.
  - 퓨즈를 추가하면 가능하다.
  answer_index: 1
  explanation: 각 어댑터 출력은 독립적으로 유지되어야 하며, 병렬 연결은 절대 금지됩니다 [S15].
- question: 로봇손 유지보수 전 가장 우선해야 할 안전 조치는 무엇인가?
  choices:
  - 소프트웨어 토크 해제
  - 멀티미터 저항 측정
  - 3개 전원 어댑터의 물리적 분리 및 잔류 전압 확인
  - 계획 정지 버튼 누름
  answer_index: 2
  explanation: 정비 전에는 반드시 3개 전원 어댑터를 물리적으로 분리하고, 각 분기의 잔류 전압이 1 V 미만임을 멀티미터로 확인해야
    합니다.
- question: FSR 힘 센서 ADC 회로에 사용해야 하는 전원 레일은?
  choices:
  - 12 V 액추에이터 레일
  - 5 V 전원 레일
  - 3.3 V 센서 레일
  - 24 V 전원 레일
  answer_index: 2
  explanation: OpenCR의 ADC 회로 보호를 위해 3.3 V 센서 레일을 사용해야 합니다 [S13].
completion_criteria:
- 3개 독립 분기 하네스 구성 및 퓨즈 장착 완료
- 각 분기별 무부하 시 전압이 12 V로 측정됨
- 전원 물리적 분리 후 모든 측정 노드의 잔류 전압이 1 V 미만임을 기록함
- 배선 안전 설계 보고서 제출 및 통과
source_ids:
- S14
- S24
- S25
- S7
- S15
- S11
- S13
- S26
---

## 안전한 배선 및 전원 분리 원리

5지 로봇손 시스템은 다수의 고토크 액추에이터를 사용하므로 효율적이고 안전한 전원 분배가 필수적입니다. 본 프로젝트는 전원 어댑터 11개를 사용하여 액추에이터를 4대/4대/3대 단위로 분리 배치하며, 이는 각 분기의 전류 부하를 분산하고 전원 안정성을 높이기 위함입니다 [S15].

### 1. 전원 독립성 확보
각 어댑터의 양(+) 출력은 독립적인 분기로 유지되어야 하며, 임의로 합치거나 묶는 행위는 절대 금지됩니다. [S15]에 명시된 어댑터의 정격 출력 전류(11.5 A) 내에서 액추에이터 피크 전류(XM430-W350-T 1대당 2.3 A)를 수용하도록 설계합니다 [S11]. 4대 단위 분기의 피크 전류 합계는 9.2 A로, 어댑터의 연속 출력 허용 범위 내에 있습니다.

### 2. 과전류 보호 (Protection Coordination)
분기마다 10 A ATOF 퓨즈를 배치하여 배선이나 액추에이터 오류 시의 과전류로부터 시스템을 보호합니다 [S25]. ATOF 퓨즈는 정격 전류의 110%~135% 수준에서 동작하므로, 피크 전류 9.2 A 대비 안정적인 보호가 가능합니다. 단, 퓨즈 선정은 반드시 제조사가 제공하는 'Time-Current Curve'를 참조해야 하며, 부하 전류가 낮다고 해서 안전이 보장되는 것은 아닙니다 [S25].

### 3. 제어 회로 분리
DYNAMIXEL 포트 내장형 OpenCR 제어 보드를 사용하여 복잡한 외부 브리지 회로를 제거함으로써 재현성을 높입니다 [S13]. FSR 힘 센서는 ADC 입력으로 전압을 변환하기 위해 3.3 V 센서 레일로부터 공급되는 분압 회로를 사용하며, 12 V 액추에이터 전원과는 전기적으로 분리되어야 합니다 [S13].

### 4. 작업 안전 수칙
벤치 프로토타입은 인증된 기계 안전 시스템이 아니므로, 정비나 수정 작업 전에는 반드시 3개 전원 어댑터를 물리적으로 분리하고, 각 분기의 잔류 전압이 1 V 미만임을 멀티미터 DC 전압 모드로 계측 확인해야 합니다 [S7].
