---
layout: learn-module
title: 텐던 구동 메커니즘 설계
course_slug: precise-robot-hand
course_data_key: precise-robot-hand
course_locale: ko
lang: ko
ref: learn:precise-robot-hand:tendon-driven-design
translations:
- lang: ko
  url: /learn/precise-robot-hand/tendon-driven-design/
- lang: en
  url: /learn/en/precise-robot-hand/tendon-driven-design/
- lang: ja
  url: /learn/ja/precise-robot-hand/tendon-driven-design/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/tendon-driven-design/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/tendon-driven-design/
module_id: M2
permalink: /learn/precise-robot-hand/tendon-driven-design/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
id: M2
slug: tendon-driven-design
phase_id: P1
estimated_hours: 10.0
prerequisites:
- M1
objectives:
- 텐던 구동 메커니즘의 기본 역학 구조와 관절 모사 원리를 이해한다.
- 정교한 로봇 손을 위한 텐던 재료(Dyneema SK78)의 특성을 학습한다.
- 텐던의 장력 전달 경로와 캡스턴 설계 시 마찰 및 마모 방지법을 익힌다.
- 액추에이터의 스톨 토크와 텐던 구동 시의 기계적 이득을 계산한다.
worked_examples:
- '예제 1: 텐던 구동 시의 장력 계산

  액추에이터 토크(τ)가 1 N·m이고 캡스턴 반경(r)이 0.01 m일 때, 텐던 장력(T)은 T = τ/r = 1/0.01 = 100 N이다.
  Dyneema SK78의 파단 하중 230 daN(약 2300 N) 대비 안전율을 고려하여 설계한다 [S16].'
- '예제 2: 전원 분기 분배 및 보호

  전체 액추에이터 11대의 스톨 전류 합계는 25.3 A이다 [S11]. 이를 3개 분기에 4대, 4대, 3대로 배분하면 각 분기의 최대 부하는
  각각 9.2 A, 9.2 A, 6.9 A이다. 퓨즈와 부하·전원 정격의 비교만으로 안전성이나 동작 순서를 보장하지 않는다. 퓨즈 제조사 시간-전류
  곡선과 전원 OCP 특성을 함께 검토해 보호 협조를 확인한다. 퓨즈 제조사 시간-전류 곡선과 어댑터 OCP 특성을 함께 검토해 보호 협조를 확인한다
  [S24, S25].'
lab:
  title: 텐던 장력 및 관절 마찰 측정 실습
  steps:
  - 제공된 링크와 베어링을 사용하여 손가락 관절 모델을 조립한다.
  - 텐던을 연결하고 텐셔너를 사용하여 초기 장력을 설정한다.
  - 멀티미터를 DC 전압 모드로 설정하고, 각 분기의 12 V 전원 어댑터 출력을 물리적으로 분리하여 확인한다.
  - 전원 인가 전 관절의 회전 마찰력을 수동으로 측정하여 기록한다.
  safety:
  - 정비·접근 전 3개 절연 전원 어댑터를 물리적으로 분리하고 멀티미터로 1 V 미만 DC 전압을 확인한다.
  - 전원 인가 중에는 절대로 손가락의 가동 범위에 접근하지 않는다.
  - 충격 방지 작업용 보안경을 반드시 착용한다.
  deliverables:
  - 관절 회전 각도에 따른 텐던 장력 측정 데이터
  - 마찰력 분석 보고서
  - 최종 안전 계측 기록
assignment:
  title: 5지 로봇손 텐던 경로 설계
  deliverables:
  - 로봇 손가락 텐던 경로 CAD 도면
  - 텐던 마찰 및 손실 계산서
  - 분기별 전원 부하 배분 및 퓨즈 보호 설계도
  rubric:
  - 텐던 경로가 굴곡부 마찰을 최소화하도록 설계되었는가?
  - Dyneema SK78의 물리적 특성이 고려되었는가?
  - 3개 전원 분기의 부하 배분이 액추에이터 스톨 전류를 적절히 반영하였는가?
  - 퓨즈 및 전원 단락 방지 설계가 BOM 사양을 준수하는가?
quiz:
- question: Dyneema SK78 텐던을 사용할 때의 주요 이점은 무엇인가?
  choices:
  - 높은 신율로 인한 충격 흡수
  - 매우 낮은 작동 신율과 높은 파단 하중
  - 금속보다 가벼운 무게와 낮은 인장 강도
  - 전기 전도성
  answer_index: 1
  explanation: Dyneema SK78은 신율이 1% 미만으로 매우 낮아 위치 제어의 정밀도를 높이고, 매우 높은 파단 하중을 가진 고성능
    섬유이다 [S16].
- question: 3개의 12 V 전원 어댑터(각 11.5 A)를 사용하는 이유로 적절한 것은?
  choices:
  - 모든 액추에이터를 하나의 전원으로 구동하기 위해
  - 전압을 36 V로 증폭하여 토크를 높이기 위해
  - 액추에이터의 총 피크 전류를 분산 수용하고 개별 분기 퓨즈로 보호하기 위해
  - 전원 노이즈를 제거하기 위해
  answer_index: 2
  explanation: 퓨즈와 부하·전원 정격의 비교만으로 안전성이나 동작 순서를 보장하지 않는다. 퓨즈 제조사 시간-전류 곡선과 전원 OCP
    특성을 함께 검토해 보호 협조를 확인한다 [S11, S15, S25].
completion_criteria:
- 모든 실습 데이터와 도면이 최종 보고서에 포함되어야 한다.
- 물리적 전원 분리 후 3개 분기의 DC 전압이 1 V 미만임을 계측으로 입증해야 한다.
- 텐던 경로 설계에서 캡스턴 마찰을 고려한 해석이 포함되어야 한다.
source_ids:
- S9
- S10
- S16
- S11
- S15
- S24
- S25
---

## 텐던 구동 메커니즘의 기초

텐던 구동(Tendon-driven) 시스템은 원격지에 위치한 액추에이터에서 인장력을 텐던(줄)을 통해 관절로 전달하여 구동하는 방식이다 [S9]. 생물학적 손가락의 힘줄 구조를 모사하여 액추에이터를 손바닥이나 팔뚝으로 이동시킴으로써, 손가락 자체의 질량을 줄이고 정교한 움직임을 구현할 수 있다 [S10].

### 1. 텐던의 선택 및 장력 전달
본 설계에서는 고강도 저신율 섬유인 Dyneema SK78을 사용한다 [S16]. 이 재료는 지름 1.5 mm에서 230 daN(약 230 kgf)의 파단 하중을 가지며, 작동 신율이 1% 미만으로 정밀한 위치 제어에 적합하다 [S16].

### 2. 기계적 이득과 구동기 선정
XM430-W350-T 스마트 액추에이터는 스톨 토크 4.1 N·m를 제공한다 [S11]. 텐던은 회전축에서 캡스턴 반경을 통해 힘을 변환하므로, 액추에이터의 토크 출력은 텐던의 장력으로 치환된다. 전체 시스템은 11대의 액추에이터를 사용하며, 피크 전류 합계는 약 25.3 A에 도달할 수 있다 [S11]. 퓨즈와 부하·전원 정격의 비교만으로 안전성이나 동작 순서를 보장하지 않는다. 퓨즈 제조사 시간-전류 곡선과 전원 OCP 특성을 함께 검토해 보호 협조를 확인한다 [S15, S24, S25].

### 3. 안전 및 보호 설계
각 12 V 전원 분기는 독립적인 퓨즈를 통해 운용된다 [S15, S24]. 3개의 전원 어댑터는 각각 11.5 A 정격으로, 합산 전류 용량은 34.5 A에 달하여 시스템 피크 전류인 25.3 A를 충분히 수용한다 [S11, S15]. 분기 합산 정격이 액추에이터 총 피크 전류를 상회하도록 설계하여 운용 안전성을 확보한다.
