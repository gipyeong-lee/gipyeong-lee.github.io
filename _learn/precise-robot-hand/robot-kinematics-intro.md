---
layout: learn-module
title: 로봇 기구학 기초
course_slug: precise-robot-hand
module_id: mod-1
permalink: /learn/precise-robot-hand/robot-kinematics-intro/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: 880e0f0309f941738bdf0ce682a0cf8c
id: mod-1
slug: robot-kinematics-intro
phase_id: phase-1
estimated_hours: 10.0
prerequisites: []
objectives:
- 로봇 기구학의 기본 개념인 자유도(DOF)와 관절 공간 및 작업 공간의 관계를 이해한다.
- DH 파라미터(Denavit-Hartenberg parameters)를 사용하여 5지 로봇손의 링크 구조를 수학적으로 모델링하는 방법을 학습한다.
- 로봇 손가락의 순기구학(Forward Kinematics) 계산 과정을 익히고 텐던 구동 시스템의 기구적 특성을 분석한다.
worked_examples:
- 관절 1개의 회전각 $\theta_1$에 대해 링크 길이 $L_1$인 단순 2차원 평면 로봇 손가락 끝의 좌표 $(x, y)$는 순기구학 식 $x
  = L_1 \cos(\theta_1)$, $y = L_1 \sin(\theta_1)$로 결정됩니다.
- 3관절 손가락 모델에서 DH 파라미터를 적용할 때, 인접 좌표계 간의 동차 변환 행렬 $T_i^{i-1}$을 곱하여 최종 손끝 좌표계의 행렬 $T_3^0
  = T_1^0 T_2^1 T_3^2$를 유도합니다.
lab:
  title: 로봇손 링크 구조 모델링 및 관절 가동 범위 측정
  steps:
  - 제공된 5지 로봇손 CAD 도면을 분석하여 각 손가락 링크의 길이($L_1, L_2, L_3$)를 측정한다.
  - 각 관절의 회전 중심을 기준으로 DH 좌표계를 설정하고 테이블로 파라미터를 작성한다.
  - 멀티미터를 사용하여 DYNAMIXEL XM430-W350-T 액추에이터의 초기 영점 위치를 설정한다[bom_system_truth].
  - 실제 출력된 손가락 링크를 조립하고 수동으로 각 관절을 회전시켜 기구적 간섭이 없는 가동 범위를 기록한다.
  safety:
  - 전동기 구동 시 손가락 끼임 방지를 위해 보호 장갑을 착용하고 비상정지 버튼을 즉시 조작 가능한 위치에 배치한다.
  - 실험 중 전원은 반드시 저전압 벤치 전원을 사용하고 전류 제한 설정을 1A 이하로 유지한다.
  - 보안경을 반드시 착용하여 혹시 모를 텐던 파단 시 튀어 오르는 탄성 에너지를 방지한다.
  deliverables:
  - 작성된 DH 파라미터 테이블
  - 각 관절의 기구적 가동 범위 측정 보고서
  - 로봇손 CAD 도면과 실제 측정값 간의 오차 분석표
assignment:
  title: 5지 로봇손 기구학 해석 보고서
  deliverables:
  - 손가락 1개에 대한 순기구학 수학적 유도식
  - MATLAB 또는 Python을 활용한 손끝 궤적 시뮬레이션 코드
  - 기구학적 특이점(Singularity)이 발생할 수 있는 관절 구성 분석
  rubric:
  - DH 파라미터가 링크 구조와 일치하는가?
  - 순기구학 행렬 유도 과정이 수학적으로 정확한가?
  - 시뮬레이션 결과가 도면의 기구적 가동 범위를 준수하는가?
quiz:
- question: 로봇 기구학에서 순기구학의 정의로 올바른 것은?
  choices:
  - 손끝의 위치로부터 관절 각도를 계산하는 과정
  - 관절 각도로부터 손끝의 위치를 계산하는 과정
  - 액추에이터의 소모 전력을 계산하는 과정
  - 로봇의 무게 중심을 계산하는 과정
  answer_index: 1
  explanation: 순기구학(Forward Kinematics)은 주어진 관절 변수(각도)를 기반으로 로봇의 끝단 위치와 방향을 구하는 과정입니다.
- question: 5지 로봇손과 같은 텐던 구동 시스템에서 Dyneema SK78을 사용하는 주된 이유는?
  choices:
  - 절연 성능이 매우 뛰어나기 때문
  - 파단 하중이 크고 작동 신율이 낮아 정밀한 위치 전달이 가능하기 때문
  - 전기를 생성하여 액추에이터 효율을 높이기 때문
  - 열팽창 계수가 매우 높기 때문
  answer_index: 1
  explanation: Dyneema SK78은 높은 파단 하중(230 daN)과 낮은 작동 신율(<1%)을 가져 텐던 구동 로봇손의 정밀 제어에
    필수적입니다[S14].
- question: DH 파라미터 구성 시 필요한 4가지 기본 요소는?
  choices:
  - 링크 길이, 링크 뒤틀림, 관절 거리, 관절 각도
  - 링크 무게, 모터 토크, 전압, 전류
  - 링크 재질, 노즐 온도, 베드 온도, 노즐 지름
  - 센서 해상도, ADC 샘플링 속도, 저항값, 전압
  answer_index: 0
  explanation: DH 파라미터는 인접한 링크 사이의 변환을 정의하기 위해 a, alpha, d, theta의 4개 값을 사용합니다.
completion_criteria:
- 로봇 기구학 기초 이론 평가에서 80점 이상 획득
- DH 파라미터 기반의 순기구학 모델링 과제 제출 및 승인
- 손가락 1개에 대한 기구학 시뮬레이션 결과가 실제 측정값과 5% 이내의 오차를 보임
source_ids:
- S1
- S7
---

## 로봇 기구학 개요
로봇 기구학은 힘이나 토크를 고려하지 않고 로봇의 기하학적 형상과 움직임을 연구하는 분야입니다[S1]. 5지 로봇손과 같은 다관절 시스템에서 각 관절의 회전 각도(Joint Space)를 통해 손끝(End-effector)의 위치(Task Space)를 결정하는 것을 순기구학이라 합니다.

### 자유도(Degree of Freedom, DOF)
로봇 시스템이 공간상에서 가질 수 있는 독립적인 움직임의 수를 말합니다. 5지 로봇손은 일반적으로 각 손가락이 3~4개의 관절을 가지며, 이는 다자유도 시스템으로서 고도의 작업 공간 제어를 요구합니다.

### Denavit-Hartenberg (DH) 파라미터
임의의 복잡한 로봇 구조를 좌표계 간의 변환 행렬로 표현하기 위한 표준 기법입니다. 링크의 길이($a_i$), 링크의 뒤틀림($\alpha_i$), 관절 거리($d_i$), 관절 각도($\theta_i$)라는 4개의 파라미터를 사용하여 인접한 두 링크 사이의 상대적인 위치와 방향을 정의합니다.

### 텐던 구동의 기구적 특징
로봇손의 구동 방식에서 텐던(Tendon, Dyneema SK78 사용)은 액추에이터의 회전 운동을 관절의 굽힘 운동으로 변환합니다[S14]. 이때 텐던의 경로와 캡스턴 반지름은 관절의 유효 토크와 변위비(Transmission Ratio)를 결정하는 핵심 요소입니다.
