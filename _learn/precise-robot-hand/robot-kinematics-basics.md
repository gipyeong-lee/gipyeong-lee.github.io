---
layout: learn-module
title: 로봇 기구학 기초
course_slug: precise-robot-hand
module_id: M1
permalink: /learn/precise-robot-hand/robot-kinematics-basics/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: ca4b0e25920a41ad92a16da990566600
id: M1
slug: robot-kinematics-basics
phase_id: P1
estimated_hours: 10.0
prerequisites: []
objectives:
- 로봇 기구학의 기본 개념인 강체 변환(Spatial Transformations)을 이해한다.
- 순기구학(Forward Kinematics)을 사용하여 로봇 손가락의 위치와 자세를 수학적으로 모델링한다.
- 로봇 작업공간(Workspace)의 개념을 파악하고 최적화의 필요성을 학습한다.
- 좌표계 변환과 회전 행렬을 적용하여 다관절 시스템을 해석한다.
worked_examples:
- '예제 1: 2차원 평면에서 1자유도 링크(길이 $L=100$ mm, 각도 $\theta=30^\circ$)의 끝단 좌표 $(x, y)$ 계산.
  $x = L \cos(\theta) = 100 \times \cos(30^\circ) \approx 86.6$ mm, $y = L \sin(\theta)
  = 100 \times \sin(30^\circ) = 50.0$ mm.'
- '예제 2: 3차원 공간에서 $z$축 기준으로 $90^\circ$ 회전하는 회전 행렬 $R_z(90^\circ)$ 구성. $R_z = \begin{bmatrix}
  \cos(90^\circ) & -\sin(90^\circ) & 0 \\ \sin(90^\circ) & \cos(90^\circ) & 0 \\ 0
  & 0 & 1 \end{bmatrix} = \begin{bmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$.'
lab:
  title: 좌표계 모델링 및 손가락 관절 해석 실습
  steps:
  - OpenCR 제어기에 연결된 DYNAMIXEL XM430-W350-T의 통신 상태를 DYNAMIXEL Wizard 2.0으로 확인한다 [S11,
    S13].
  - 로봇 손가락의 링크 길이를 버니어 캘리퍼스로 측정하여 기록한다.
  - 측정한 값을 바탕으로 각 관절의 회전 중심을 기준으로 좌표계를 설정한다.
  - 설정된 좌표계를 바탕으로 로봇 손가락의 순기구학 수식을 작성한다.
  - 실제 액추에이터를 회전시켜 계산된 손끝 위치와 실제 위치의 오차를 멀티미터로 센서 전압을 확인하며 간접 검증한다.
  safety:
  - 실험 중 정지는 3개 절연 전원 어댑터(GST160A12-R7B)를 물리적으로 분리하고 멀티미터로 각 분기 전압이 1 V 미만인지 DC-voltage
    모드에서 반드시 확인한다 [S15].
  - 절대 양(+) 출력 단자를 병렬로 연결하지 않는다.
  - 전원 인가 중 가동 범위 내에 손이나 이물질을 절대 넣지 않는다.
  - 모든 회로는 퓨즈(10 A ATOF)가 포함된 독립 분기로 구성하며 직접 구성한 정지 회로를 안전 기능으로 신뢰하지 않는다 [S24].
  deliverables:
  - 작성된 로봇 손가락 기구학 모델 보고서
  - 관절 각도에 따른 손끝 좌표 계산 결과 표
  - 안전 확인 실측 기록
assignment:
  title: 로봇 손가락 기구학 설계 및 분석
  deliverables:
  - 손가락 1개에 대한 순기구학 방정식 유도 자료
  - 작업공간 도식화 결과물 (CAD 또는 그래프)
  - 좌표계 설정이 포함된 설계 도면
  rubric:
  - 순기구학 방정식이 관절 각도와 링크 길이를 적절히 반영하는가?
  - 좌표계 설정이 D-H 파라미터 또는 표준 방식에 부합하는가?
  - 작업공간 분석이 물리적 한계를 고려했는가?
quiz:
- question: 순기구학(Forward Kinematics)의 정의로 올바른 것은?
  choices:
  - 끝단의 위치를 알 때 관절 각도를 계산하는 과정
  - 관절 각도를 알 때 끝단의 위치와 자세를 계산하는 과정
  - 로봇의 동역학적 힘을 분석하는 과정
  - 센서 데이터를 보정하는 과정
  answer_index: 1
  explanation: 순기구학은 조인트 변수(관절 각도)로부터 작업 공간 내의 위치와 자세를 도출하는 과정입니다 [S2].
- question: 로봇 시스템에서 작업공간(Workspace)을 제한하는 주요 요인은?
  choices:
  - 링크의 길이와 관절의 가동 범위
  - 제어기의 CPU 클럭 속도
  - 액추에이터의 통신 프로토콜
  - 퓨즈의 정격 전류
  answer_index: 0
  explanation: 로봇의 작업공간은 기하학적 형상(링크 길이)과 관절의 회전 한계에 의해 결정됩니다 [S2].
completion_criteria:
- 순기구학 수식 유도 보고서 제출 및 통과
- 작업공간 도식화 및 설계 도면 완료
- 안전 절차를 준수하여 실습 수행 및 기록 완료
source_ids:
- S1
- S2
- S11
- S13
- S15
- S24
---

## 로봇 기구학 기초

로봇 기구학은 로봇의 기계적 구조를 기하학적 관점에서 해석하는 학문으로, 힘이나 토크를 고려하지 않고 위치, 속도, 가속도 사이의 관계를 다룹니다 [S1, S2].

### 1. 공간 변환 (Spatial Transformations)
로봇 손의 각 관절 위치는 좌표계(Coordinate Frame)의 조합으로 표현됩니다. 관절 $i$와 관절 $i+1$ 사이의 상대적 관계는 회전 행렬 $R$과 위치 벡터 $P$를 포함하는 동차 변환 행렬(Homogeneous Transformation Matrix) $T$로 정의됩니다 [S2].

$$T = \begin{bmatrix} R & P \\ 0 & 1 \end{bmatrix}$$

### 2. 순기구학 (Forward Kinematics)
순기구학은 관절 각도(Joint Variables)가 주어졌을 때, 로봇 끝단(End-effector, 예: 손끝)의 공간상 위치와 자세를 계산하는 과정입니다 [S2]. 로봇 손가락 모델링 시, 각 링크의 길이와 관절의 회전 각도를 사용하여 전체 좌표계에서의 손끝 위치를 산출합니다.

### 3. 작업공간 (Workspace)
로봇이 도달할 수 있는 모든 공간의 집합을 작업공간이라 합니다 [S2]. 5지 로봇손의 경우, 각 손가락 관절의 가동 범위 제한에 의해 작업공간이 결정되며, 이는 기계 설계 시 최적화되어야 하는 핵심 요소입니다 [S2].
