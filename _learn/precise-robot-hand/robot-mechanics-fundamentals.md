---
layout: learn-module
title: 로봇 기구학 기초
course_slug: precise-robot-hand
course_data_key: precise-robot-hand
course_locale: ko
lang: ko
ref: learn:precise-robot-hand:robot-mechanics-fundamentals
translations:
- lang: ko
  url: /learn/precise-robot-hand/robot-mechanics-fundamentals/
- lang: en
  url: /learn/en/precise-robot-hand/robot-mechanics-fundamentals/
- lang: ja
  url: /learn/ja/precise-robot-hand/robot-mechanics-fundamentals/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/robot-mechanics-fundamentals/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/robot-mechanics-fundamentals/
module_id: M1
permalink: /learn/precise-robot-hand/robot-mechanics-fundamentals/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
id: M1
slug: robot-mechanics-fundamentals
phase_id: P1
estimated_hours: 10.0
prerequisites: []
objectives:
- 로봇 기구학의 기본 정의와 강체 변환(Rigid-body transformation)의 개념을 이해한다.
- 좌표계 변환과 회전 행렬을 사용하여 로봇의 위치와 방향을 수학적으로 기술하는 방법을 익힌다.
- 5지 로봇손 설계를 위한 기구학적 기초 이론을 습득하고 해석적 접근법을 익힌다.
worked_examples:
- '예제 1: 2차원 평면에서 1개의 회전 관절(Rotation Joint)을 가진 로봇 링크의 끝단 위치 $(x, y)$를 구하시오. 관절 각도가
  $\theta$이고 링크 길이가 $L$일 때, $x = L \cos(\theta)$, $y = L \sin(\theta)$이다 [S1].'
- '예제 2: $x$축에 대해 $\theta$만큼 회전하는 2차원 회전 행렬 $R$을 기술하시오. $R = \begin{bmatrix} \cos(\theta)
  & -\sin(\theta) \\ \sin(\theta) & \cos(\theta) \end{bmatrix}$ 이다 [S1].'
lab:
  title: 좌표계 변환 시뮬레이션 및 기초 기구학 해석
  steps:
  - 기구학 해석 소프트웨어를 사용하여 2링크 평면 매니퓰레이터 모델을 생성한다.
  - 관절 각도를 변화시키며 끝단 위치의 궤적을 확인한다.
  - 역기구학 계산식을 수기로 유도하고 시뮬레이션 결과와 비교한다.
  safety:
  - 컴퓨터 작업 시 화면 밝기를 조절하고 주기적으로 휴식한다.
  - 본 실습은 시뮬레이션 기반이므로 하드웨어 통전은 요구하지 않음.
  deliverables:
  - 기구학 해석 과정이 포함된 요약 보고서
  - 궤적 시뮬레이션 결과 이미지
assignment:
  title: 5지 로봇손 관절 구조 기구학 모델링
  deliverables:
  - 로봇 손가락 1개에 대한 순기구학 방정식 유도 결과물
  - 관절 각도 변화에 따른 손끝 위치 변화 예측 데이터
  rubric:
  - 회전 행렬의 수학적 정확성
  - 순기구학 방정식의 물리적 타당성
  - 보고서의 논리적 구성
quiz:
- question: 로봇 기구학에서 힘이나 토크를 고려하지 않고 운동만을 기술하는 학문은 무엇인가?
  choices:
  - 동역학(Dynamics)
  - 기구학(Kinematics)
  - 제어 이론(Control Theory)
  - 재료 역학(Material Mechanics)
  answer_index: 1
  explanation: 기구학은 힘과 토크를 제외한 위치, 속도, 가속도 중심의 운동론입니다 [S1].
- question: 3차원 공간에서 두 좌표계 간의 방향을 정의하는 행렬은?
  choices:
  - 회전 행렬(Rotation Matrix)
  - 질량 행렬(Mass Matrix)
  - 강성 행렬(Stiffness Matrix)
  - 감쇠 행렬(Damping Matrix)
  answer_index: 0
  explanation: 회전 행렬은 두 좌표계 간의 방향을 수학적으로 변환하는 직교 행렬입니다 [S1].
completion_criteria:
- 이론 강좌 학습 완료
- 기구학 해석 결과 보고서 제출
- 이론 퀴즈 100점 달성
source_ids:
- S1
---

## 로봇 기구학의 기초

로봇 기구학은 로봇의 운동을 힘이나 토크를 고려하지 않고 위치, 속도, 가속도 측면에서 다루는 학문입니다 [S1]. 로봇손과 같은 매니퓰레이터 설계의 출발점은 각 관절의 상태를 공간상의 좌표로 기술하는 것입니다.

### 1. 강체 변환 (Rigid-body Transformation)
로봇의 각 링크는 강체로 간주되며, 하나의 좌표계에서 다른 좌표계로의 변환은 회전(Rotation)과 이동(Translation)의 조합으로 나타납니다. 3차원 공간에서 회전 행렬(Rotation Matrix) $R$은 직교 행렬이며, 이를 통해 두 좌표계 간의 방향을 정의합니다 [S1].

### 2. 순기구학 (Forward Kinematics)
순기구학은 관절의 변수(각도 또는 위치)를 알고 있을 때, 로봇 끝단(End-effector)의 위치와 방향을 계산하는 과정입니다. 5지 로봇손에서는 손가락 관절 각도($\theta_1, \theta_2, \dots, \theta_n$)를 통해 손끝의 위치를 구합니다.

### 3. 역기구학 (Inverse Kinematics)
역기구학은 원하는 손끝의 위치를 목표값으로 설정했을 때, 이를 달성하기 위한 각 관절 변수를 구하는 과정입니다. 비선형 방정식으로 구성되어 있어 해가 존재하지 않거나 다중 해가 발생할 수 있습니다 [S1].
