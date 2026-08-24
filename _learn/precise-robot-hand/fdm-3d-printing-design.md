---
layout: learn-module
title: FDM 3D 프린팅 설계 가이드
course_slug: precise-robot-hand
module_id: M5
permalink: /learn/precise-robot-hand/fdm-3d-printing-design/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e444faa5055649a48877852af0b7303b
id: M5
slug: fdm-3d-printing-design
phase_id: P2
estimated_hours: 8.0
prerequisites:
- M4
objectives:
- FDM(Fused Deposition Modeling) 3D 프린팅의 기본 원리와 공정 매개변수를 이해한다.
- 로봇손 부품 제작에 적합한 기하학적 설계 규칙(벽 두께, 공차, overhang 등)을 익힌다.
- 적층 방향(Orientation)이 부품의 기계적 강도에 미치는 이방성(Anisotropy) 영향을 해석한다.
- FDM 장비의 한계를 고려한 효율적인 부품 분할 및 조립 전략을 수립한다.
worked_examples:
- '예제 1: 로봇 손가락 관절의 벽 두께 결정. 하중을 받는 부품이므로 최소 1.5mm의 벽 두께와 3개 이상의 외곽선(Perimeter)을 설정하여
  강성을 극대화한다.'
- '예제 2: 적층 방향 최적화. 손가락 마디를 Z축으로 세워서 출력하면 층간 분리 현상으로 쉽게 부러진다. 이를 평면(XY)에 눕혀 출력하여 층
  결합력이 응력 방향과 평행하게 설계한다 [S75].'
lab:
  title: 로봇 손가락 마디 출력 및 파지 시험
  steps:
  - 제공된 로봇 손가락 마디 CAD 파일을 슬라이싱 소프트웨어에서 적층 방향을 다르게 설정하여 3종 출력한다.
  - 출력된 시편의 치수를 버니어 캘리퍼스로 측정하여 설계값과의 공차를 확인한다.
  - 각 시편을 벤치 바이스에 고정하고 손가락 끝에 점진적 하중을 가하여 파손 지점을 기록한다.
  - 가장 강도가 높았던 출력 방향과 실패 사례를 비교 분석하여 최종 조립 부품의 출력 전략을 세운다.
  safety:
  - 3D 프린터 노즐 고온(200°C 이상) 주의, 출력물 제거 시 장갑 착용 필수.
  - 하중 시험 시 부품 파손으로 인한 파편 비산 방지를 위해 보안경 착용.
  - 비상 전원 차단 버튼 위치 확인.
  deliverables:
  - 출력 전략에 따른 출력물 3종
  - 공차 측정 데이터 시트
  - 적층 방향별 하중 시험 비교 분석 보고서
assignment:
  title: 5지 로봇손 부품 설계 최적화
  deliverables:
  - 최적화된 손가락 마디 CAD 데이터(STL 및 원본)
  - 서포트 최소화 설계 근거 보고서
  - 조립부 간격(Clearance) 분석서
  rubric:
  - 설계 규칙(벽 두께 1.2mm 이상, 챔퍼 적용) 준수 여부
  - 출력 방향 고려를 통한 강성 확보 전략의 타당성
  - 조립 정밀도 확보를 위한 공차 설계 적절성
quiz:
- question: FDM 3D 프린팅의 강도 특성인 이방성(Anisotropy)에 대한 설명으로 옳은 것은?
  choices:
  - 모든 방향에서 동일한 강도를 갖는다.
  - 수평 방향(XY) 강도가 수직 방향(Z)보다 일반적으로 높다.
  - 수직 방향(Z) 강도가 수평 방향(XY)보다 항상 높다.
  - 적층 높이와는 무관하다.
  answer_index: 1
  explanation: FDM은 층을 쌓아 올리는 방식이므로 층간 결합력의 한계로 인해 Z축 방향의 인장 강도가 XY 평면보다 낮습니다 [S75].
- question: 조립되는 부품 사이의 간격(Clearance) 설계 시 권장되는 최소값은?
  choices:
  - 0.01 mm
  - 0.1 mm
  - 0.5 mm
  - 2.0 mm
  answer_index: 2
  explanation: FDM 장비의 치수 정밀도를 고려할 때, 움직이는 조립 부품 사이에는 최소 0.5mm의 간격을 설계해야 부품끼리 융착되는
    것을 방지할 수 있습니다 [S76, S77].
- question: 서포트 사용을 최소화하기 위한 설계 방법으로 옳지 않은 것은?
  choices:
  - 출력 방향을 변경하여 overhang 각도를 줄인다.
  - 복잡한 형상은 여러 부품으로 분할하여 출력한다.
  - 가능한 모든 곳에 sharp edge를 사용하여 날카롭게 설계한다.
  - chamfer를 활용하여 서포트 없는 경사를 만든다.
  answer_index: 2
  explanation: Sharp edge는 FDM 출력 시 노즐의 라운딩 특성으로 인해 정확하게 출력되기 어렵고, 서포트 문제와 무관하게 설계
    시 기하학적 정밀도를 떨어뜨립니다 [S77].
completion_criteria:
- 실습 결과물 3종 이상 제출
- 설계 규칙 준수 CAD 데이터 제출
- 강도 분석 및 공차 분석 보고서 승인
source_ids:
- S73
- S74
---

## FDM 3D 프린팅의 기구적 원리
FDM은 열가소성 필라멘트를 노즐에서 녹여 층(layer) 단위로 적층하는 방식이다 [S73]. 노즐의 궤적은 CAD 모델의 슬라이싱 결과를 따르며, 이는 노즐 직경과 층 높이에 의해 최소 형상 정밀도가 결정된다 [S75].

### 설계 고려사항
1. **벽 두께(Wall Thickness)**: FDM 부품은 최소 1.2mm 이상의 벽 두께를 확보해야 구조적 강성을 유지할 수 있다 [S74]. 얇은 벽은 층간 결합력 저하로 파손 위험이 크다 [S75].
2. **이방성(Anisotropy)**: FDM 부품은 출력 방향에 따라 강도가 달라진다. 수평 방향(XY 평면) 강도가 수직 방향(Z축)보다 50~75% 높으므로, 하중 경로를 고려한 출력 방향 설정이 필수적이다 [S75].
3. **공차(Tolerance) 및 조립**: FDM은 CNC 가공보다 정밀도가 낮으므로(일반적 ±0.3mm 수준), 조립되는 부품 사이에는 최소 0.5mm의 간격(Clearance)을 설계해야 한다 [S76, S77].
4. **Overhang과 서포트**: 45도 이상의 기울기를 가진 형상은 서포트가 필요하며, 적절한 챔퍼(Chamfer) 설계를 통해 서포트 사용을 최소화할 수 있다 [S74].

### 최적화 전략
복잡한 로봇손 부품은 전체를 한번에 출력하기보다 기능별로 분할(Sectioning)하여 출력한 후 조립하는 것이 설계 자유도와 출력 신뢰성을 높인다 [S73].
