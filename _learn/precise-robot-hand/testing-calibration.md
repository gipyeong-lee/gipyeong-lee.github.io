---
layout: learn-module
title: 최종 교정 및 파지 시험
course_slug: precise-robot-hand
module_id: M10
permalink: /learn/precise-robot-hand/testing-calibration/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: 024057fbaaef48f6b3c3847511cb8b54
id: M10
slug: testing-calibration
phase_id: P3
estimated_hours: 10.0
prerequisites:
- M8
- M9
objectives:
- 5지 로봇손의 텐던 장력과 접촉력 간의 상관관계를 이해한다.
- FSR 402 센서를 활용한 전압 분압 회로 구성 및 ADC 신호 처리 기법을 습득한다.
- 로봇손의 파지 성능을 정량적으로 평가하기 위한 교정 및 시험 절차를 수행한다.
worked_examples:
- '예제 1: OpenCR ADC에서 10 kΩ 저항을 사용한 분압 회로의 입력 전압 계산. FSR 저항이 5 kΩ일 때, 3.3 V 입력 기준
  V_out = 3.3 * (10 / (5 + 10)) = 2.2 V. 이는 12-bit ADC 범위 내에서 안전하게 취득 가능함 [S16, S28].'
- '예제 2: 파지력 데이터 수집. 손끝에 0.5 N 무게를 올렸을 때 ADC 코드 409, 1.0 N에서 819가 측정되었다면, 선형 보간을 통해
  힘(F) = 0.5 * (ADC / 409) N으로 모델링 가능 [S15].'
lab:
  title: FSR 센서 교정 및 정적 파지 시험
  steps:
  - 각 독립 12 V 전원 분기 어댑터를 물리적으로 분리한 상태에서 FSR-ADC 회로를 OpenCR 3.3 V 센서 레일에 연결 [S16, S18].
  - 각 센서별로 0.2 N부터 20 N까지의 교정용 하중을 인가하며 ADC 데이터를 수집 [S15].
  - 전원 분기를 연결하고(절차에 따라 퓨즈 분기 확인) [S27], 시험용 물체를 파지하여 센서 피드백에 따른 안정성 확인.
  - 시험 종료 후 3개 독립 전원 어댑터를 물리적으로 분리하고, 모든 분기에서 1 V 미만임을 확인 후 장비 접근 [S3, S18].
  safety:
  - 모든 전원 인가 전 보안경을 착용한다.
  - ADC 회로 구성 시 3.3 V 센서 레일만 사용하며, 12 V 또는 5 V 레일과 절대 혼용하지 않는다 [S16].
  - 시험 중에는 절대 가동 범위 내에 손을 넣지 않으며, 고정 지그를 사용한다.
  - 전원 분기 어댑터 양(+) 출력은 절대 병렬로 연결하지 않는다 [S18].
  deliverables:
  - 센서별 교정 데이터 및 힘-ADC 변환 모델 그래프
  - 최종 교정 기록지
  - 다양한 물체 파지 시험 시의 센서 피드백 데이터 로그
assignment:
  title: 파지 상태 추정 시스템 분석
  deliverables:
  - FSR 센서 데이터 처리 알고리즘 소스 코드
  - 파지 시험 결과 보고서
  rubric:
  - FSR 분압 회로의 전압 범위가 0~3.3 V 이내로 설계되었는가?
  - 교정 데이터를 통해 힘 측정 모델이 정확히 도출되었는가?
  - 파지 시험 중 텐던 장력과 센서 피드백의 연동이 정상적인가?
quiz:
- question: FSR 센서와 분압 저항 구성 시 올바른 전원 연결은?
  choices:
  - OpenCR 12 V 액추에이터 레일
  - OpenCR 3.3 V 센서 레일
  - OpenCR 5 V 전원
  - 데스크톱 어댑터 독립 분기
  answer_index: 1
  explanation: OpenCR ADC 분압 회로는 반드시 규정된 3.3 V 센서 레일에서 공급받아야 안전합니다 [S16].
- question: 시험 중 장비 정지 및 접근을 위한 올바른 절차는?
  choices:
  - 소프트웨어로 모터 정지 명령
  - 10 A 퓨즈 제거
  - 3개 독립 전원 어댑터 물리적 분리 및 전압 확인
  - 비상 정지 버튼 누름
  answer_index: 2
  explanation: 이 프로토타입은 learner-built E-stop이 없으므로, 3개 독립 전원을 물리적으로 분리하고 1 V 미만임을
    계측해야 합니다 [S3, S18].
- question: Dyneema 텐던의 성능 유지를 위한 주요 고려 사항은?
  choices:
  - 반복 굽힘 시험 및 신율 관리
  - 강한 산성 환경 보관
  - 고온 노출
  - 기름칠
  answer_index: 0
  explanation: Dyneema SK78은 신율이 매우 낮으나 반복적인 기계적 스트레스에 대한 관리가 필요합니다 [S19].
completion_criteria:
- 각 FSR 센서의 힘-ADC 변환 모델이 교정 기록지에 문서화되었는가?
- 3개 독립 전원 분기의 배선이 상호 간섭 없이 독립적으로 유지되었는가?
- 실험 종료 후 전원 분리 및 잔류 전압 확인 절차를 정확히 수행했는가?
source_ids:
- S3
- S15
- S28
- S16
- S19
- S18
- S27
---

### 파지력 감지 및 교정 이론

5지 로봇손의 지능형 제어는 손끝에서 측정되는 접촉력을 기반으로 이루어집니다 [S3]. FSR 402 센서는 압력이 증가함에 따라 저항이 감소하는 특성을 가진 박막형 힘 센서입니다 [S15].

#### 1. 전압 분압 회로
FSR은 가변 저항으로 동작하므로, 제어 보드의 ADC 입력으로 신호를 변환하기 위해 고정 저항(R_fixed = 10 kΩ)을 사용하는 전압 분압 회로가 필요합니다 [S28]. ADC 출력 전압 V_out은 다음과 같습니다:

V_out = V_ref * (R_fixed / (R_FSR + R_fixed))

이때 V_ref는 OpenCR의 3.3 V 센서 전원을 사용해야 하며, 5 V나 12 V 전원을 사용하면 안 됩니다 [S16].

#### 2. 교정의 필요성
FSR은 비선형적인 저항 변화를 보이므로, 실제 측정값(ADC 코드)과 물리적인 힘(N) 사이의 상관관계를 도출하는 교정(Calibration) 과정이 필수적입니다 [S15]. 알려진 무게를 손끝에 인가하여 ADC 데이터를 기록함으로써 힘-전압 함수를 얻을 수 있습니다.

#### 3. 파지 시험
다양한 물체를 파지할 때 센서 피드백을 통해 텐던 장력을 동적으로 조절하여 안정적인 파지 상태를 유지합니다 [S3]. 반복적인 굽힘 시험은 Dyneema 텐던의 신율 관리에 중요합니다 [S19].
