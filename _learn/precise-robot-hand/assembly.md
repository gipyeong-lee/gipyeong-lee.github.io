---
layout: learn-module
title: 로봇손 조립
course_slug: precise-robot-hand
course_data_key: precise-robot-hand
course_locale: ko
lang: ko
ref: learn:precise-robot-hand:assembly
translations:
- lang: ko
  url: /learn/precise-robot-hand/assembly/
- lang: en
  url: /learn/en/precise-robot-hand/assembly/
- lang: ja
  url: /learn/ja/precise-robot-hand/assembly/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/assembly/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/assembly/
module_id: m6
permalink: /learn/precise-robot-hand/assembly/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
id: m6
slug: assembly
phase_id: p2
estimated_hours: 15.0
prerequisites:
- m5
objectives:
- 로봇손 기구 조립을 위한 정밀 부품 체결 원리를 이해한다.
- 텐던(Dyneema) 구동 시스템의 장력 전달 구조를 파악한다.
- 독립 전원 분기 구성과 물리적 배선 안전을 학습한다.
- FSR 센서와 분압 회로의 올바른 통합 방법을 습득한다.
worked_examples:
- '예시 1: 퓨즈 용량 계산. XM430 액추에이터 11대(스톨 전류 합계 9.2 A)를 1개의 12 V 분기에 연결할 경우, 10 A 퓨즈를
  사용하는 것이 적절합니다. 이는 정상 운전 범위를 수용하면서 배선 과부하 시 회로를 보호하는 표준 규격입니다 [S14, S26].'
- '예시 2: 열압입 인서트 깊이. M3 황동 인서트는 PC-CF 출력물에 수직으로 정확히 열압입되어야 하며, 4.4 mm 외경에 맞춘 4 mm
  파일럿 홀이 필요합니다 [S23]. 기울어짐은 나사산 조립 정밀도를 저하시키므로 주의해야 합니다.'
lab:
  title: 로봇손 기구 조립 및 배선 실습
  steps:
  - M3 열압입 인서트를 손가락 링크와 손바닥 프레임에 설치합니다.
  - igus JSM-0810-10 베어링과 8 mm 알루미늄 샤프트를 손목 및 관절축에 장착합니다.
  - Dyneema 텐던을 캡스턴에 감고 적정 장력으로 손가락에 연결합니다.
  - Micro-Fit 3.0 커넥터를 사용하여 각 액추에이터와 손가락 센서 하네스를 배선합니다 [S9].
  - 각 독립 12 V 분기에 10 A 퓨즈를 설치하고 개별 전원 연결을 확인합니다 [S26, S25].
  safety:
  - 전원 인가 전에는 반드시 멀티미터로 3개 전원 분기의 절연 상태를 확인하십시오.
  - 텐던 장력 시험 중 텐던 파단 시 튕김 방지를 위해 항상 보안경을 착용하십시오.
  - 정비 및 부품 접근 전 3개의 전원 어댑터를 물리적으로 분리하고 각 분기의 전압이 1 V 미만임을 계측 확인하십시오.
  - 절대 두 개 이상의 전원 어댑터 양(+) 출력을 병렬로 연결하지 마십시오.
  deliverables:
  - 관절별 마찰 없는 구동 확인 영상
  - 각 전원 분기별 퓨즈 설치 사진
  - 조립 완료된 로봇손의 배선도 및 체결 토크 기록
assignment:
  title: 로봇손 시스템 통합 보고서
  deliverables:
  - 완성된 조립체 3면도 및 체결점 상세도(CAD)
  - 전원 분기별 부하 배분표 및 퓨즈 용량 검증 결과
  - 손가락 굴곡 시 텐던 장력 데이터 기록
  rubric:
  - 기구 조립 정밀도 및 베어링 마찰 최소화(40%)
  - 독립 분기별 독립적인 전원 배선 및 안전 지침 준수(40%)
  - 제출물 기술 사양의 정확성(20%)
quiz:
- question: 다음 중 전원 공급 방식에 대한 설명으로 옳은 것은?
  choices:
  - 3개 전원 어댑터의 양(+) 단자를 병렬로 연결하여 전류 용량을 키운다.
  - 각 전원 어댑터는 독립적인 분기로 사용하며 양(+) 단자는 전기적으로 절연한다.
  answer_index: 1
  explanation: 시스템 안전을 위해 각 전원 어댑터는 독립적인 분기로 사용하며, 양(+) 출력을 병렬로 연결하는 것은 절대 금지됩니다.
- question: FSR 402 센서를 OpenCR 보드에 연결할 때 사용해야 하는 전압은?
  choices:
  - 3.3 V 센서 전원 레일
  - 12 V 액추에이터 전원 레일
  answer_index: 0
  explanation: FSR 센서 분압 회로는 ADC 신호를 0-3.3 V 범위 내로 유지하기 위해 반드시 3.3 V 센서 레일에 연결해야 합니다.
- question: 텐던 소재로 Dyneema SK78을 사용하는 주된 이유는?
  choices:
  - 저렴한 가격과 쉬운 가공성
  - 작은 지름 대비 높은 파단 하중과 매우 낮은 작동 신율
  answer_index: 1
  explanation: Dyneema SK78은 매우 높은 강도와 낮은 신율을 제공하여 정밀한 장력 전달에 적합합니다.
completion_criteria:
- 모든 5개 손가락 관절의 물리적 조립 완료
- 독립적인 3개 전원 분기의 퓨즈 설치 확인
- 조립 완료 후 3개 분기 각각 무전원 상태(1 V 미만) 확인
source_ids:
- S19
- S20
- S21
- S23
- S18
- S17
- S26
- S15
- S27
- S16
- S14
- S9
- S25
---

### 정밀 조립 및 하네스 시스템

로봇손 조립은 기구적 강성과 전자적 신뢰성을 동시에 확보해야 하는 정밀 공정입니다. 주요 구조물은 강성과 치수 안정성이 높은 탄소섬유 충전 PC 필라멘트(PC-CF)로 제작되며 [S21], M3 황동 열압입 인서트를 통해 반복적인 분해와 조립이 가능하도록 설계되었습니다 [S23].

#### 텐던 구동 원리
텐던은 액추에이터의 회전 운동을 손가락 관절의 굴곡 운동으로 변환합니다. Dyneema SK78 소재는 지름 1.5 mm에서 230 daN의 높은 파단 하중과 1% 미만의 낮은 작동 신율을 제공하여, 장력 전달 효율을 극대화합니다 [S18]. 조립 시 캡스턴 모서리의 라운딩 처리는 텐던의 마모를 방지하는 필수 요소입니다.

#### 독립 전원 및 안전 분기
본 시스템은 3개의 독립적인 12 V 전원 분기를 사용합니다 [S17]. 각 분기는 어댑터별로 전기적으로 절연되며, 절대 양(+) 출력을 병렬로 연결하지 않습니다. 각 분기에는 10 A ATOF 퓨즈가 직렬로 배치되어 배선 결함으로부터 보호합니다 [S26]. 이는 액추에이터의 스톨 전류 합계가 안전하게 수용되도록 설계되었습니다.

#### 센서 인터페이스
손끝의 FSR 402 센서는 압력에 따라 저항이 변하는 가변 저항체입니다 [S15]. 교육용 프로토타입은 기계 안전 표준 준수나 인증을 주장하지 않으며, 사람 접근 환경 투입 전 자격 있는 안전 전문가의 별도 검토가 필요하다 [S27] [S16].
