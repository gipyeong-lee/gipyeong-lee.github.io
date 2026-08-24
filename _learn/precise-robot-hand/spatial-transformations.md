---
layout: learn-module
title: 공간 변환 및 기구학
course_slug: precise-robot-hand
module_id: M2
permalink: /learn/precise-robot-hand/spatial-transformations/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e444faa5055649a48877852af0b7303b
id: M2
slug: spatial-transformations
phase_id: P1
estimated_hours: 8.0
prerequisites:
- M1
objectives:
- 공간상에서 물체의 위치와 방향을 나타내는 수학적 표현(좌표계와 회전 행렬)을 이해한다.
- 동차 변환 행렬(Homogeneous Transformation Matrix)을 사용하여 다물체 시스템의 관계를 기술한다.
- 로봇 관절의 기구학적 구조와 자유도(DOF)의 개념을 학습한다.
- 산업용 로봇 핸드의 손가락 좌표계 할당 및 변환 과정을 실습한다.
worked_examples:
- '예제 1: 2차원 평면에서 좌표계 {B}가 {A}를 기준으로 x축으로 2, y축으로 3만큼 이동하고 90도 회전했을 때의 변환 행렬을 구하시오.
  R = [0 -1 0; 1 0 0; 0 0 1], P = [2, 3, 0]이므로 T = [0 -1 0 2; 1 0 0 3; 0 0 1 0; 0
  0 0 1]입니다.'
- '예제 2: 텐션 구동 손가락의 관절 위치 해석. 만약 손가락이 3개의 관절을 가진다면, 각 관절의 각도 \(\theta_1, \theta_2,
  \theta_3\)에 따른 최종 말단(tip) 좌표를 T_0^3 = T_0^1 * T_1^2 * T_2^3 행렬 곱으로 계산합니다.'
lab:
  title: 로봇 핸드 모델링 및 좌표계 설정 실습
  steps:
  - 제공된 로봇 핸드 CAD 모델을 분석하여 각 관절(MCP, PIP, DIP)의 위치를 확인한다.
  - 각 링크에 대해 DH(Denavit-Hartenberg) 파라미터를 사용하여 국부 좌표계를 할당한다.
  - Python을 사용하여 각 관절의 동차 변환 행렬을 계산하는 스크립트를 작성한다.
  - 작성한 코드를 검증하여 특정 관절 각도에서의 손가락 끝 위치를 시뮬레이션한다.
  safety:
  - 납땜 인두 사용 시 화상 주의 (보안경 착용)
  - 전동 공구 사용 시 끼임 방지 설계 확인
  - 벤치 전원 사용 시 전류 제한 설정 필수
  deliverables:
  - 좌표계 할당 도면
  - 변환 행렬 계산 Python 스크립트 코드
  - 시뮬레이션 결과 보고서
assignment:
  title: 5지 로봇 핸드 기구학 해석 프로젝트
  deliverables:
  - 선택한 로봇 핸드 구조에 대한 DH 파라미터 테이블
  - 전체 핸드의 기구학적 모델링 보고서 (변환 행렬 포함)
  - Python 기반 시뮬레이션 결과
  rubric:
  - 좌표계 할당의 적절성 (30%)
  - DH 파라미터 추출의 정확성 (30%)
  - 변환 행렬 도출 및 코드 구현 (30%)
  - 보고서의 논리적 구성 및 시각화 (10%)
quiz:
- question: 동차 변환 행렬(Homogeneous Transformation Matrix)의 크기는 무엇인가?
  choices:
  - 2x2
  - 3x3
  - 4x4
  - 6x6
  answer_index: 2
  explanation: 동차 변환 행렬은 회전(3x3)과 이동(3x1)을 포함하여 4x4 행렬로 정의됩니다.
- question: 로봇 핸드 설계 시 '언더액추에이션(Underactuation)'의 장점은?
  choices:
  - 제어가 매우 복잡해진다.
  - 제어 시스템의 복잡도를 낮추고 비용을 절감한다.
  - 관절의 개수가 항상 무한하다.
  - 항상 모든 관절을 독립적으로 제어해야 한다.
  answer_index: 1
  explanation: 언더액추에이션은 액추에이터의 수를 자유도보다 적게 사용하여 구조를 단순화하고 비용을 절감하는 기술입니다.
completion_criteria:
- 각 관절에 대한 좌표계 할당을 완료함.
- 변환 행렬 도출 과정을 이해하고 계산함.
- 제출된 Python 스크립트가 정상적으로 작동함.
source_ids:
- S2
- S9
---

### 1. 공간 변환의 기초
로봇 공학에서 모든 물체(링크, 공구, 환경)의 위치와 방향은 3차원 공간 내에서 정의되어야 합니다 [S2, S9]. 위치는 3차원 벡터(x, y, z)로, 방향은 3x3 회전 행렬(Rotation Matrix) R로 표현합니다.

### 2. 동차 변환 행렬 (Homogeneous Transformation Matrix)
회전과 평행 이동을 하나의 4x4 행렬로 통합한 것이 동차 변환 행렬 T입니다 [S2].
\[ T = \begin{bmatrix} R & P \\ 0 & 1 \end{bmatrix} \]
여기서 R은 3x3 회전 행렬, P는 3x1 위치 벡터입니다 [S2]. 이 행렬은 좌표계 간의 변환을 연쇄적으로 곱하여 계산할 수 있어 로봇 기구학 해석에 필수적입니다 [S9].

### 3. 자유도와 기구학적 체인
로봇 핸드는 다수의 링크가 관절로 연결된 기구학적 체인입니다. 로봇의 자유도(Degrees of Freedom, DOF)는 로봇의 모든 부품이 독립적으로 움직일 수 있는 독립적 좌표의 수입니다 [S13]. 인간형 로봇 손은 대개 다수의 관절을 가지며, 이를 효과적으로 제어하기 위해 텐션(Tendon) 구동 및 언더액추에이션(Underactuation) 기술이 사용됩니다 [S12, S13].
