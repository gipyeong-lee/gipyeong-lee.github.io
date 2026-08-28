---
layout: learn-module
title: 로봇 기구학 기초
course_slug: precise-robot-hand
module_id: M1
permalink: /learn/precise-robot-hand/robotics-kinematics-basics/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: cb69d47af59949d9b2cf040d149dd749
id: M1
slug: robotics-kinematics-basics
phase_id: PH1
estimated_hours: 12.0
prerequisites: []
objectives:
- 로봇손 기구학 모델링을 위한 강체 변환 행렬 이해
- 텐던 구동 로봇손의 자유도(DOF)와 운동학적 제약 조건 분석
- DYNAMIXEL 스마트 액추에이터의 피드백 데이터를 이용한 위치 제어 기초 학습
worked_examples:
- '관절 토크 계산: 액추에이터 스톨 토크가 4.1 N·m이고 캡스턴 반지름이 0.01 m일 때, 이론적인 텐던 최대 장력은 $T = \tau /
  r = 4.1 / 0.01 = 410 N$입니다 [B1].'
- '전류 부하 산정: 11개의 액추에이터가 동시에 스톨 전류를 발생시킬 때 전체 피크 전류는 $11 \times 2.3 A = 25.3 A$입니다
  [B1]. 이를 3개의 독립 퓨즈 분기로 나누어 배분하면 분기당 최대 약 9.2 A(4대 배분 시)가 되어 10 A 퓨즈 보호 하에 안전하게 동작합니다
  [B3, B10].'
lab:
  title: 로봇손 링크 설계 및 텐던 장력 측정 실험
  steps:
  - FDM 프린터를 사용하여 PC-CF 필라멘트로 손가락 링크 출력
  - 8 mm 샤프트와 무급유 베어링을 사용하여 관절 조립
  - Dyneema 텐던을 액추에이터 캡스턴에 연결하고 초기 장력 설정
  - 멀티미터를 DC 전압 모드로 설정하여 전원 분기별 12V 안정성 확인
  - DYNAMIXEL Wizard를 통해 액추에이터 위치 피드백 데이터 수집
  safety:
  - 실험 중 전원 인가 시 손가락 가동 범위에 신체 부위 진입 금지
  - 모든 정비 및 접근 전 3개의 12V 어댑터를 물리적으로 분리하고 멀티미터로 1V 미만 잔류 전압 확인
  - PC-CF 출력물 조립 및 텐던 장력 시험 중 충격 방지 보안경 필수 착용
  - 배선 분기에는 반드시 지정된 10 A 퓨즈를 장착하고 메인 전원 버스 병렬 연결 절대 금지
  deliverables:
  - 관절 가동 범위 측정 데이터
  - 텐던 장력 조절 기록
  - 전원 분기별 잔류 전압 측정 로그
assignment:
  title: 5지 로봇손 운동학 모델링 및 전류 분석 보고서
  deliverables:
  - 5지 로봇손 각 관절에 대한 Denavit-Hartenberg 파라미터 테이블
  - 11개 액추에이터의 총 피크 전류를 고려한 3개 전원 분기 구성도
  - FSR 센서 신호 처리를 위한 3.3V 분압 회로 설계도
  rubric:
  - 운동학 모델의 정확성(좌표계 설정 적절성)
  - BOM에 명시된 퓨즈 정격 및 액추에이터 스톨 전류를 고려한 전원 분기 설계 적절성
  - 안전 수칙 준수 명시 및 무전원 검증 절차 이해도
quiz:
- question: 본 시스템에서 11개의 액추에이터를 3개의 전원 분기로 나누어 사용하는 주된 이유는 무엇입니까?
  choices:
  - 전원 분기별 퓨즈를 통해 과전류로부터 배선을 보호하기 위해
  - 액추에이터의 통신 속도를 높이기 위해
  answer_index: 0
  explanation: 각 액추에이터 분기는 10A 퓨즈와 독립적인 물리적 분리 수단을 갖추어 과전류 사고로부터 보호되어야 합니다 [B3, B10].
- question: OpenCR 보드에서 FSR 힘 센서를 사용할 때 올바른 전원 공급 방식은 무엇입니까?
  choices:
  - 12V 액추에이터 전원 라인 사용
  - 3.3V 전용 센서 rail 사용
  answer_index: 1
  explanation: 센서 신호의 ADC 정밀도와 안전을 위해 반드시 3.3V 센서 전원 rail만 사용해야 합니다 [B2].
completion_criteria:
- 5지 로봇손의 운동학 모델링 보고서 제출
- 전원 분기별 퓨즈 보호 및 무전원 검증 절차 이해 확인
- 실습 실험 데이터(가동 범위 및 전압 측정) 기록 완료
source_ids:
- S7
- S14
- S10
---

### 로봇 기구학 기초
로봇손의 제어는 각 관절의 각도와 위치를 정확히 계산하는 기구학(Kinematics)에서 시작됩니다. 5지 로봇손은 다수의 관절을 가진 고자유도 시스템으로, 각 링크의 위치는 동차 변환 행렬(Homogeneous Transformation Matrix)을 사용하여 표현합니다 [S7].

#### 텐던 구동 시스템
텐던 구동은 액추에이터를 손가락 끝단이 아닌 손바닥이나 팔뚝에 배치하여 로봇손의 질량을 줄이고 민첩성을 높입니다. 텐던 장력 $T$는 관절 토크 $\tau$와 캡스턴 반지름 $r$의 관계식 $\tau = T \times r$을 통해 결정됩니다. 텐던 구동기 설계 시 Dyneema SK78과 같은 고강도 저신율 섬유를 사용하여 위치 정밀도를 확보합니다 [S14].

#### 액추에이터 및 제어
본 시스템은 11개의 DYNAMIXEL XM430-W350-T 액추에이터를 사용하여 구동합니다 [B1]. 각 액추에이터는 12V 전압에서 동작하며 스톨 전류 2.3A를 가집니다 [B1, S10]. OpenCR 컨트롤러는 이 액추에이터와 직접 통신하며, 시스템의 안전을 위해 각 액추에이터 분기를 독립적으로 퓨즈 보호해야 합니다 [B2, B3, B10].
