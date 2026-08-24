---
layout: learn-module
title: 시스템 교정 및 내구 시험
course_slug: precise-robot-hand
module_id: M10
permalink: /learn/precise-robot-hand/calibration-testing/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e444faa5055649a48877852af0b7303b
id: M10
slug: calibration-testing
phase_id: P4
estimated_hours: 6.0
prerequisites:
- M9
objectives:
- 로봇 시스템의 교정(Calibration) 절차를 이해하고 실습한다.
- 로봇손의 성능 검증을 위한 내구 시험 및 환경 시험을 설계하고 수행한다.
- 산업 표준(ISO 10218)에 따른 안전 검증을 수행한다.
- 교정 기록과 최종 프로젝트 보고서를 작성한다.
worked_examples:
- '예제 1: DYNAMIXEL XM430-W350의 위치 정확도 교정. 관절 각도를 0°, 90°, 180°로 설정하고 실제 측정값과의 편차를
  계산하여 `Homing Offset` 레지스터를 보정하는 방법 [S36, S37].'
- '예제 2: 파지력 계산. 4.1Nm의 스톨 토크(Stall Torque)를 갖는 액추에이터가 텐션 구동 메커니즘을 통해 손가락 끝에서 발휘하는
  이론적 파지력을 계산하고 실제 측정값과 비교 [S36, S38].'
lab:
  title: 로봇손 시스템 교정 및 내구 시험 실습
  steps:
  - 각 관절 액추에이터의 영점(Zero Position)을 설정하고 교정 기록지에 기록한다.
  - 로봇손 제어 코드를 사용하여 정격 토크 및 속도 범위 내에서 1,000회 반복 동작 테스트를 수행한다.
  - 파지 시험기를 사용하여 파지력의 일관성을 10회 측정하고 평균값과 오차를 계산한다.
  - ISO 10218 기반의 안전 점검 리스트에 따라 비상 정지 장치의 정상 동작 여부를 확인한다.
  safety:
  - 반드시 보안경을 착용한다.
  - 액추에이터 구동 중 손가락 끼임에 주의한다.
  - 비상 전원 차단 장치를 실습대 옆에 비치하고 상시 사용 가능 상태로 유지한다.
  - 벤치 전원 사용 시 전류 제한(Current Limit)을 반드시 설정한다.
  deliverables:
  - 시스템 교정 기록지
  - 반복 시험 결과 데이터 및 그래프
  - 파지 시험 및 내구 시험 측정 결과 보고서
assignment:
  title: 로봇손 검증 최종 보고서 작성
  deliverables:
  - 시스템 교정 및 내구 시험 데이터가 포함된 최종 보고서 (PDF)
  - 로봇손의 성능 검증 결과 및 개선 제안
  rubric:
  - 교정 절차가 논리적으로 서술되고 데이터가 정확한가?
  - 내구 시험 조건이 명확하고 결과 분석이 타당한가?
  - ISO 10218 안전 기준을 이해하고 적용하였는가?
  - 보고서의 구조가 체계적이고 시각 자료(그래프 등)가 적절한가?
quiz:
- question: 로봇 교정의 주된 목적은 무엇인가?
  choices:
  - 로봇의 미관 개선
  - 실제 기구적 오차와 제어 모델 간의 간극 최소화
  - 액추에이터의 최대 속도 증가
  - 무선 통신 속도 향상
  answer_index: 1
  explanation: 로봇 교정은 실제 기구 구조의 제작 오차를 제어 알고리즘에 반영하여 정밀도를 확보하는 과정입니다.
- question: ISO 10218 표준이 정의하는 로봇 안전 모드 중 하나인 PFL은 무엇의 약자인가?
  choices:
  - Power and Force Limiting
  - Position and Frequency Limiting
  - Pressure and Friction Limiting
  - Performance and Failure Limiting
  answer_index: 0
  explanation: PFL은 Power and Force Limiting의 약자로, 사람과의 협동 작업 시 충격력을 제한하는 안전 모드입니다
    [S34].
- question: 로봇손의 내구 시험 수행 시 반복 횟수가 많은 주된 이유는 무엇인가?
  choices:
  - 액추에이터의 온도를 낮추기 위해
  - 통신 지연을 테스트하기 위해
  - 반복 동작에 의한 마모 및 고장을 조기에 발견하기 위해
  - 소프트웨어 버그를 수정하기 위해
  answer_index: 2
  explanation: 내구 시험은 로봇 시스템의 수명과 신뢰성을 검증하기 위해 충분한 반복 동작을 통해 고장 가능성을 확인합니다.
completion_criteria:
- 시스템 교정 기록지를 성공적으로 작성하여 제출하였다.
- 내구 시험 결과 데이터와 파지 시험 측정치가 타당하게 분석되었다.
- 로봇손 검증 최종 보고서의 요구사항을 모두 충족하였다.
source_ids:
- S12
- S34
---

## 시스템 교정 및 성능 검증 이론

로봇 시스템의 신뢰성을 확보하기 위해서는 제작 후 엄격한 교정과 시험 과정이 필수적입니다. 본 모듈에서는 정교한 5지 로봇손의 제어 정확도, 내구성, 안전성을 검증합니다.

### 1. 시스템 교정 (Calibration)
로봇 교정은 실제 기구학적 파라미터와 제어 모델 간의 오차를 줄이는 과정입니다. 
- **영점 교정 (Zeroing):** 액추에이터의 기준 위치를 절대 엔코더 값과 일치시킵니다 [S36].
- **키네마틱 교정:** 3D 프린팅의 오차로 인한 기구학적 파라미터(Link length 등)의 변형을 측정하여 제어 알고리즘의 파라미터를 보정합니다 [S1].

### 2. 내구 시험 (Durability Testing)
- **반복 동작 시험:** 특정 그리핑 동작을 10만 회 이상 반복하여 기구적 마모나 액추에이터 고장을 확인합니다 [S24].
- **부하 시험 (Load Bearing):** 최대 파지력(Stall Torque)을 측정하고, 정격 토크 범위 내에서 지속적인 동작 성능을 검증합니다 [S36].

### 3. 안전 검증 (Safety Standards)
ISO 10218 표준은 로봇 설계와 시스템 통합에 대한 안전 요구사항을 정의합니다 [S34].
- **비상 정지 (Emergency Stop):** 비상시 전원 차단 시스템의 응답 시간을 측정합니다 [S34].
- **힘 제한 검증 (PFL Mode):** 접촉 시 인체에 가해지는 힘이 허용 임계치(예: 130N 등)를 넘지 않음을 검증합니다 [S34].
