---
layout: learn-module
title: 로봇 손 CAD 설계
course_slug: precise-robot-hand
module_id: M4
permalink: /learn/precise-robot-hand/cad-design/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: df0bcf05b81f44e1a71e0ca6fa802bac
id: M4
slug: cad-design
phase_id: P2
estimated_hours: 12.0
prerequisites:
- M1
objectives:
- 로봇 손의 운동학적 구조와 자유도(DoF) 할당 원리 이해
- 손바닥 자유도가 엄지의 대립(Opposability)에 미치는 영향 분석
- 적응형 구동 기구(Adaptive Actuation Mechanism) 설계 파라미터 도출
- FDM 3D 프린팅을 고려한 부품 설계 및 조립 공차 최적화
worked_examples:
- '예제 1: 자유도 재배치 분석. 총 자유도가 20으로 제한된 경우, 손가락에서 손바닥으로 2 DoF를 이전했을 때 대립 영역이 얼마나 변하는지
  복셀 기반 방법으로 평가하는 모델링 시나리오를 설정합니다 [S1].'
- '예제 2: 텐던 구동력 계산. 외전 각도를 30도로 고정했을 때, 메타카르포팔랑지(MCP) 관절의 굴곡을 위해 필요한 정적 텐던 힘을 자유물체도(FBD)를
  통해 계산하는 과정을 수행합니다 [S2].'
lab:
  title: 로봇 손 메커니즘 설계 및 CAD 검증
  steps:
  - 'CAD 소프트웨어(예: Fusion 360, SolidWorks)를 사용하여 손가락 관절 모델링'
  - 텐던 라우팅 풀리의 직경을 파라미터로 설정하고 모멘트 암 분석 수행
  - 복셀 기법을 사용하여 설계된 손의 접근 가능 영역 시뮬레이션
  - 조립 간섭 체크 및 3D 프린팅을 위한 부품 분할 및 공차 조정
  - 최종 설계 모델의 STL 파일 내보내기
  safety:
  - 컴퓨터 작업 중 올바른 자세 유지
  - CAD 프로그램 강제 종료 시 데이터 손실 주의
  - 적층 제조(3D 프린팅) 시 뜨거운 노즐(화상 주의) 근처 접근 금지
  - 프린팅 종료 후 챔버 냉각 대기
  deliverables:
  - 완성된 로봇 손 전체 CAD 파일(STEP/STL)
  - 텐던 라우팅 및 액추에이터 배치 설계 도면
  - 복셀 기반 접근 영역 분석 결과 보고서
assignment:
  title: 로봇 손 Kinematic 설계 보고서
  deliverables:
  - 설계 도면이 포함된 PDF 보고서
  - 선택한 기구학적 구조의 이유(손바닥 자유도 포함) 기술
  rubric:
  - 운동학적 구조(DoF) 할당이 엄지의 대립 기능을 논리적으로 설명하는가?
  - 텐던 구동 파라미터가 기구학적 요구사항을 만족하는가?
  - 3D 프린팅 공차 및 조립성이 적절하게 고려되었는가?
quiz:
- question: 손바닥 자유도(Palm DoF)가 로봇 손 설계에서 가장 크게 기여하는 기능은 무엇인가?
  choices:
  - 손가락 길이를 직접 늘리는 것
  - 손가락 베이스 위치를 재배치하여 엄지 대립 영역을 확장하는 것
  - 액추에이터의 무게를 줄이는 것
  - 손가락의 최대 굴곡 각도를 높이는 것
  answer_index: 1
  explanation: 손바닥 자유도는 손가락 베이스 위치의 재배치를 통해 작업 공간의 중첩(overlap)을 효율적으로 최적화하여 대립 기능을
    향상시킵니다 [S1].
- question: 텐던 구동 기구에서 모멘트 암 풀리의 주된 역할은 무엇인가?
  choices:
  - 텐던의 마찰을 제거하는 것
  - 동시에 굴곡과 외전 동작을 구현하기 위해 텐던을 측면으로 유도하는 것
  - 전력을 절약하는 것
  - 구조적 강성을 낮추는 것
  answer_index: 1
  explanation: 모멘트 암 풀리는 텐던을 측면으로 유도하여 하나의 모터 입력으로 굴곡과 외전 동작을 동시에 수행할 수 있게 합니다 [S2].
completion_criteria:
- 로봇 손 CAD 모델 완료 및 파일 제출
- 설계 보고서에서 Kinematic 구조와 텐던 구동 방식의 타당성 입증
- 퀴즈 전 문항 정답 및 해설 이해
source_ids:
- S1
- S2
---

### 로봇 손 설계의 운동학적 기초
로봇 손 설계의 핵심은 생체 손의 기능을 모사하는 복잡한 운동학적 구조를 구현하는 것입니다. 연구에 따르면, 5지 로봇 손은 엄지 5 DoF, 나머지 손가락 3~4 DoF로 구성되는 것이 일반적입니다 [S1].

#### 1. 손바닥 자유도(Palm DoF)의 역할
단순히 손가락의 관절 수를 늘리는 것보다 손바닥의 자유도를 통해 손가락 베이스 위치를 재배치하는 것이 엄지의 대립 기능을 향상시키는 데 효과적입니다 [S1]. 이는 손가락이 닿을 수 있는 영역(reachable region)을 단순히 확장하는 것이 아니라, 작업 공간의 중첩(overlap workspace)을 최적화함으로써 달성됩니다 [S1].

#### 2. 적응형 구동 기구(Adaptive Actuation)
anthropomorphic(인간형) 로봇 손을 위해 텐던(tendon) 구동 방식을 흔히 채택합니다. 이때 굴곡/신전(flexion/extension)과 외전/내전(abduction/adduction) 동작을 소수의 액추에이터로 구현하기 위해 차동 메커니즘을 사용합니다 [S2]. 모멘트 암 풀리를 설계하여 텐던을 측면으로 유도함으로써 구동 효율을 극대화합니다 [S2].

#### 3. 설계 고려 사항
- **강성(Stiffness):** 회전 굴곡 관절의 강성은 텐던 힘 계산 및 제어 정밀도에 직접적인 영향을 미칩니다 [S2].
- **제작성:** 하이브리드 증착 제조(hybrid deposition manufacturing)와 같은 FDM 방식의 적층 제조 기법을 고려하여 설계 시 지지대(support) 최소화와 조립 공차(tolerance)를 고려해야 합니다 [S2].
