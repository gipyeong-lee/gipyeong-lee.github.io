---
layout: learn-module
title: 전자 회로 기초
course_slug: precise-robot-hand
course_data_key: precise-robot-hand
course_locale: ko
lang: ko
ref: learn:precise-robot-hand:electronics-fundamentals
translations:
- lang: ko
  url: /learn/precise-robot-hand/electronics-fundamentals/
- lang: en
  url: /learn/en/precise-robot-hand/electronics-fundamentals/
- lang: ja
  url: /learn/ja/precise-robot-hand/electronics-fundamentals/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/electronics-fundamentals/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/electronics-fundamentals/
module_id: m4
permalink: /learn/precise-robot-hand/electronics-fundamentals/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
id: m4
slug: electronics-fundamentals
phase_id: p2
estimated_hours: 12.0
prerequisites:
- m3
objectives:
- DYNAMIXEL 스마트 액추에이터의 전기적 특성과 전원 시스템 이해
- FSR 402 센서를 활용한 전압 분압 회로 설계 및 ADC 신호 취득
- 시스템 과전류 보호를 위한 퓨즈 기반 전원 분기 설계
- 전기 회로의 절연 및 물리적 안전 분리 원칙 숙지
worked_examples:
- '예제 1: 분기 전원 전류 합계 계산. 한 분기에 4대의 액추에이터(스톨 전류 각 2.3 A)가 할당된 경우, 최대 이론 전류는 9.2 A입니다.
  이는 10 A 퓨즈의 정격 이내이며, 어댑터의 11.5 A 출력 한도를 초과하지 않아 안전하게 구동 가능합니다 [S14, S17, S26].'
- '예제 2: FSR 분압기 출력 계산. FSR에 힘이 가해져 센서 저항이 10 kΩ이 되었을 때, 분압 노드의 전압은 3.3 V * (10 kΩ
  / (10 kΩ + 10 kΩ)) = 1.65 V가 됩니다. 이는 OpenCR 12비트 ADC의 유효 범위 내에 있으므로 정밀한 힘 피드백이 가능합니다
  [S15, S16, S27].'
lab:
  title: 전원 분기 구성 및 센서 입력 시험
  steps:
  - 각 MEAN WELL 어댑터 출력선에 0AFH0001Z 인라인 홀더와 10 A ATOF 퓨즈를 직렬로 설치합니다 [S17, S25, S26].
  - 각 분기의 12 V 전압이 정상 범위인지 멀티미터로 측정합니다.
  - OpenCR 3.3 V 핀과 10 kΩ 저항, FSR 402를 사용하여 분압 회로를 브레드보드에 구성합니다 [S16, S27].
  - 센서 전압이 0~3.3 V 범위 내에 있는지 확인하고 힘을 가할 때 전압 변화를 관찰합니다.
  safety:
  - 정비 및 접근 전 3개 전원 어댑터를 물리적으로 분리한 뒤, 각 분기의 DC 전압이 1 V 미만인지 멀티미터로 반드시 확인합니다.
  - 회로 구성 중 전원 인가 금지. 전압 측정은 모든 결선 완료 후 고정 지그 상태에서 수행합니다.
  - 충격 방지 작업용 보안경을 항시 착용합니다.
  - 액추에이터 전원(12 V)과 센서 전원(3.3 V)을 절대로 혼선하지 않습니다.
  deliverables:
  - 회로별 전압 측정 데이터 시트
  - FSR 힘 센서의 힘-전압 반응 곡선 플롯
  - 과전류 보호를 위한 분기별 퓨즈 결선 사진
assignment:
  title: 전원 배분 및 센서 데이터 수집 설계
  deliverables:
  - 액추에이터 분기별 전력 할당 계획서
  - OpenCR ADC 회로도를 포함한 배선도
  - 퓨즈 정격 선정 논리 보고서
  rubric:
  - 전원 분기 합산 전류가 각 어댑터의 허용 범위를 준수함
  - FSR 회로가 3.3 V 센서 레일에만 연결됨
  - 퓨즈가 과전류 보호를 적절히 수행할 수 있는 정격으로 선정됨
quiz:
- question: 다음 중 전원 분기 구성 시 금지되는 행위는 무엇인가?
  choices:
  - 분기별로 10 A 퓨즈를 직렬로 설치하는 것
  - 독립된 어댑터의 양(+) 단자들을 병렬로 연결하는 것
  - 액추에이터를 4:4:3으로 배분하는 것
  - FSR 센서를 3.3 V 레일에 연결하는 것
  answer_index: 1
  explanation: 각 어댑터 출력은 독립적인 분기로 사용해야 하며, 전원 어댑터 출력 간 병렬 연결은 시스템 고장 및 화재 위험을 초래할
    수 있어 절대 금지됩니다.
- question: FSR 402 센서 전압 분압 회로 구성 시 주의사항으로 옳은 것은?
  choices:
  - 12 V 액추에이터 전원 레일을 사용해야 한다.
  - 5 V 전원을 사용하여 ADC 해상도를 높여야 한다.
  - OpenCR의 3.3 V 센서 전원을 사용해야 한다.
  - 저항 없이 FSR만 연결해야 한다.
  answer_index: 2
  explanation: FSR 센서의 전압 신호는 OpenCR ADC 입력 범위(0~3.3 V)를 넘지 않아야 하므로, 반드시 3.3 V 센서
    전원을 사용해야 합니다.
completion_criteria:
- 모든 전원 분기 회로의 전압이 1 V 미만으로 물리적 분리됨을 멀티미터로 입증
- 퓨즈 장착 및 3.3 V 전원 분압 회로 구성 완료
- FSR 센서 신호가 OpenCR ADC에서 0~3.3 V 내에서 정상적으로 취득됨을 확인
source_ids:
- S6
- S9
- S14
- S17
- S26
- S25
- S15
- S27
- S16
---

이상 발열·냄새·연기 감지 시 접근하지 말고, 위험 구역 밖에서 사전 지정된 건물 분전반 차단기 또는 인증된 upstream master disconnect로 3개 어댑터의 공급 전원을 차단한 뒤 대피한다. 위험 구역 밖에서 작동 가능한 upstream 차단 수단이 없으면 시스템 통전을 금지한다. 토크 해제는 전원 차단을 대신하지 않는다. 정비·접근은 계획 정지 후 물리적 분리 및 무전원 계측 확인 뒤에만 수행한다 [S14] [S17] [S26, S25] [S26] [S15] [S27] [S16]
