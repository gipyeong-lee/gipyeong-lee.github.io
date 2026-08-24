---
layout: learn-module
title: 적응형 구동 원리
course_slug: precise-robot-hand
module_id: M2
permalink: /learn/precise-robot-hand/actuation-theory/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: df0bcf05b81f44e1a71e0ca6fa802bac
id: M2
slug: actuation-theory
phase_id: P1
estimated_hours: 10.0
prerequisites:
- M1
objectives:
- 적응형 로봇손 구동 기구의 기본 원리 이해
- 건 구동(Tendon-driven) 메커니즘의 정역학적 해석 능력 습득
- 능동적 자유도(DOF)와 구동기 비율 최적화 개념 파악
- 모멘트 암 풀리를 이용한 다축 운동 동시 제어 기법 학습
worked_examples:
- '예제 1: 5지 로봇손에서 4개의 모터로 5개의 손가락을 구동할 때, 구동기/손가락 비율(Ratio of actuators per finger)
  계산. 4개의 모터 / 5개의 손가락 = 0.8. 이 비율이 1.0 미만일 때 차동 메커니즘을 통한 적응형 제어가 필수적임을 확인 [S2].'
- '예제 2: 특정 외전 각도(Abduction angle)를 구현하기 위한 모멘트 암 풀리의 반지름 $r$ 계산. 기하학적 관계식 $L = r
  \theta$를 활용하여 외전 시 건의 당김 길이를 산출.'
lab:
  title: 건 구동 메커니즘 모사 및 마찰 분석
  steps:
  - 3D 프린팅된 손가락 링크와 모멘트 암 풀리를 조립한다.
  - 건(Tendon)을 경로에 맞게 라우팅하고 적절한 텐션을 설정한다.
  - 벤치 전원을 사용하여 구동기를 동작시키고 외전 및 굴곡 동작을 관찰한다.
  - 멀티미터를 이용해 모터 소비 전류를 측정하여 부하에 따른 토크 변화를 기록한다.
  safety:
  - 저전압 벤치 전원 사용 필수 (최대 12V 이내)
  - 전류 제한 회로 구성 및 준수 (모터 보호)
  - 동작 중 손가락 끼임 주의
  - 작업 시 보안경 착용
  deliverables:
  - 마찰 및 부하에 따른 구동 토크 데이터 시트
  - 외전 각도에 따른 건 변위 측정 결과
assignment:
  title: 건 구동 로봇손 설계 파라미터 최적화 보고서
  deliverables:
  - 설계 파라미터(풀리 반지름, 링크 길이) 결정 근거가 포함된 CAD 요약본
  - 외전 및 굴곡 동시 수행 시의 정역학적 평형 방정식 유도 문서
  rubric:
  - 적응형 메커니즘의 수학적 모델링 정확성 (40%)
  - 선택된 설계 파라미터의 타당성 (30%)
  - 마찰 모델 고려 및 실험적 검증 데이터의 충실도 (30%)
quiz:
- question: 로봇손에서 구동기/손가락 비율이 1.0보다 작을 때 발생하는 현상은?
  choices:
  - 모든 손가락을 독립적으로 제어할 수 있다.
  - 복잡한 기구적 차동 메커니즘이 필요하다.
  - 모터 출력을 무한히 늘려야 한다.
  - 관절의 마찰이 무시된다.
  answer_index: 1
  explanation: 구동기 수가 손가락 수보다 적으므로, 힘을 배분하거나 동작을 연동하는 차동 메커니즘이 반드시 필요합니다 [S2].
- question: 모멘트 암 풀리를 사용하는 주된 이유는 무엇인가?
  choices:
  - 손가락의 무게를 줄이기 위해
  - 건의 마찰을 제거하기 위해
  - 굴곡과 외전 동작을 동시에 제어하기 위해
  - 모터의 회전 속도를 높이기 위해
  answer_index: 2
  explanation: 모멘트 암 풀리는 건을 측면으로 유도하여 단일 건 구동으로도 다축 운동(굴곡+외전)이 가능하게 합니다 [S2].
completion_criteria:
- 이론 학습 완료 및 퀴즈 80% 이상 득점
- 건 구동 메커니즘 모사 실험 완료 및 데이터 시트 제출
- 설계 파라미터 최적화 보고서 제출 및 통과
source_ids:
- S2
---

### 적응형 구동 기구(Adaptive Actuation Mechanism)

인간형 로봇손의 핵심은 적은 수의 구동기로 복잡한 손가락 움직임을 구현하는 것입니다. 이를 위해 **적응형 구동(Adaptive Actuation)** 메커니즘이 사용됩니다 [S2].

#### 1. 건 구동 시스템(Tendon-driven System)
건 구동은 근육과 힘줄처럼 원격 위치에 있는 모터로부터 힘을 전달하는 방식입니다. 로봇손에서는 유연성과 경량화를 위해 필수적입니다.

#### 2. 차동 및 모멘트 암(Moment Arm Pulleys)
손가락의 중수지절(MCP) 관절에서 굴곡/신전(flexion/extension)과 외전/내전(abduction/adduction)을 동시에 제어하기 위해 모멘트 암 풀리를 사용합니다. 이를 통해 건을 측면으로 유도하여 두 동작을 동시에 수행할 수 있습니다 [S2].

#### 3. 정역학적 해석
로봇 손가락의 정적 평형 상태에서 각 관절에 전달되는 건의 힘($F_{tendon}$)을 계산하는 것은 기구 설계의 필수 단계입니다. 관절의 강성과 마찰(friction)은 구동 효율에 직접적인 영향을 미치며, 설계 시 이들에 대한 정밀한 모델링이 필요합니다 [S2].
