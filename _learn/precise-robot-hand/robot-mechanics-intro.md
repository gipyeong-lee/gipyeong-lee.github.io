---
layout: learn-module
title: 로봇 기구학 및 역학 기초
course_slug: precise-robot-hand
module_id: M1
permalink: /learn/precise-robot-hand/robot-mechanics-intro/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: d15f1f9bf2e148d5b847db3615e52388
id: M1
slug: robot-mechanics-intro
phase_id: P1
estimated_hours: 15.0
prerequisites: []
objectives:
- 강체 변환(Rigid-body transformations)의 수학적 기초를 이해한다.
- 순기구학(Forward Kinematics)과 역기구학(Inverse Kinematics)의 기본 개념을 파악한다.
- 로봇 메커니즘의 야코비안(Jacobian)과 자유도(Degree of Freedom) 개념을 정의한다.
- 로봇 손과 같은 조작기(Manipulator) 설계 시 고려해야 할 기구학적 제약 조건을 분석한다.
worked_examples:
- '예제 1: 2차원 평면 내 2-링크 로봇의 순기구학 계산

  링크 길이를 $l_1, l_2$, 관절 각도를 $\theta_1, \theta_2$라 할 때, 끝단 위치 $(x, y)$는 다음과 같다.

  $x = l_1 \cos(\theta_1) + l_2 \cos(\theta_1 + \theta_2)$

  $y = l_1 \sin(\theta_1) + l_2 \sin(\theta_1 + \theta_2)$

  이는 삼각함수의 덧셈 정리를 활용한 전형적인 순기구학 모델이다 [S1].'
- '예제 2: 자유도 정의

  5지 로봇손에서 각 손가락이 3개의 관절(DOF)을 가지고 있고 손바닥이 1개의 DOF를 가진다면, 총 자유도는 $5 \times 3 + 1 =
  16$이 된다. 이 시스템을 제어하려면 최소 16개의 독립적인 액추에이터 신호가 필요함을 의미한다 [S14].'
lab:
  title: 로봇 관절 기구학 시뮬레이션 및 분석
  steps:
  - CAD 소프트웨어를 사용하여 5지 로봇손의 단일 손가락 관절 모델을 생성한다.
  - 각 관절의 회전 중심축을 설정하고 DH 파라미터(Denavit-Hartenberg)를 표로 작성한다.
  - '파이썬(Python) 라이브러리(예: NumPy)를 사용하여 순기구학 계산 함수를 구현한다.'
  - 관절 각도 변화에 따른 끝단의 궤적을 3D 그래프로 시각화한다.
  safety:
  - 실습 중 3D 프린터나 구동 모듈의 끼임 주의.
  - 전기 회로 구성 시 벤치 전원의 전류 제한 설정을 확인하여 과전류 방지.
  - 보안경 착용 필수.
  deliverables:
  - 작성된 DH 파라미터 테이블
  - 순기구학 구현 소스 코드
  - 궤적 시각화 결과 이미지
assignment:
  title: 로봇 손의 기구학 모델링 보고서
  deliverables:
  - 5지 로봇손의 전체 자유도 분석 보고서
  - 임의의 손가락 관절에 대한 순기구학 행렬 계산식
  - 역기구학 해결 시 발생할 수 있는 특이점(Singularity)에 대한 고찰
  rubric:
  - 좌표계 설정의 논리적 타당성 (30%)
  - 순기구학 행렬 계산의 정확성 (40%)
  - 자유도 분석의 포괄성 및 창의적 고찰 (30%)
quiz:
- question: 순기구학(Forward Kinematics)이 구하는 대상은 무엇인가?
  choices:
  - 관절의 각도
  - 로봇 끝단의 위치와 방향
  - 모터의 소모 전류
  - 야코비안 행렬의 역행렬
  answer_index: 1
  explanation: 순기구학은 관절 변수(각도)로부터 끝단(End-effector)의 공간적 위치와 방향을 계산하는 과정입니다 [S1].
- question: 로봇 시스템에서 야코비안(Jacobian) 행렬의 주요 용도는?
  choices:
  - 관절의 물리적 강도 계산
  - 끝단 속도와 관절 속도 간의 관계 기술
  - 3D 모델의 텍스처 렌더링
  - 로봇의 전체 무게 추정
  answer_index: 1
  explanation: 야코비안은 관절 공간의 속도와 작업 공간(끝단)의 속도를 연결하는 선형 변환 행렬입니다 [S1].
completion_criteria:
- 로봇 기구학의 핵심 이론(변환 행렬, 야코비안)을 설명할 수 있음.
- 단일 손가락에 대한 순기구학 모델을 수학적으로 유도함.
- 제시된 과제에서 5지 로봇손의 자유도를 정확히 분석함.
source_ids:
- S1
- S14
---

## 1. 개요
로봇 공학은 기계공학, 컴퓨터 과학, 제어 이론의 융합체입니다 [S1]. 정교한 5지 로봇손을 설계하기 위해서는 먼저 로봇의 운동을 수학적으로 기술하는 기구학(Kinematics) 기초가 확립되어야 합니다.

## 2. 강체 변환
로봇의 각 관절은 좌표계(Coordinate Frame)로 표현됩니다. 한 좌표계에서 다른 좌표계로의 위치와 방향 변화는 회전 행렬(Rotation Matrix)과 이동 벡터(Translation Vector)로 구성된 동차 변환 행렬(Homogeneous Transformation Matrix)을 사용하여 기술합니다 [S1].

## 3. 순기구학 및 역기구학
* **순기구학(Forward Kinematics):** 관절의 각도($\theta$)로부터 로봇 끝단(End-effector)의 위치와 방향을 계산합니다.
* **역기구학(Inverse Kinematics):** 로봇 끝단이 목표 위치에 도달하기 위해 필요한 각 관절의 각도를 역산합니다. 다관절 로봇손에서는 해가 유일하지 않거나(Redundancy) 없을 수 있어 최적화 기법이 필수적입니다 [S1].

## 4. 야코비안과 자유도
로봇의 관절 속도와 끝단 속도 사이의 관계를 나타내는 행렬이 **야코비안(Jacobian)**입니다. 이는 로봇의 정밀한 제어와 힘 제어(Force Control) 방법론을 구축하는 핵심 도구입니다 [S1]. 자유도(DOF)는 로봇이 독립적으로 움직일 수 있는 최소 변수 개수를 의미하며, 5지 로봇손은 손가락별 복합 관절로 인해 고차원적인 기구학 해석이 필요합니다 [S14].
