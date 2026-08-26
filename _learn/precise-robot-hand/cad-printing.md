---
layout: learn-module
title: CAD 설계 및 FDM 출력
course_slug: precise-robot-hand
module_id: mod-3
permalink: /learn/precise-robot-hand/cad-printing/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: c6f6c4e7134945cb931d1d58c837a6d5
id: mod-3
slug: cad-printing
phase_id: phase-2
estimated_hours: 12.0
prerequisites:
- mod-2
objectives:
- FDM 3D 프린팅을 위한 기계 부품의 CAD 설계 원칙을 이해한다.
- 탄소섬유 보강 PC 필라멘트(PC-CF)의 물성 및 출력 설정(노즐 온도 285°C, 베드 온도 110°C)을 학습한다.
- 적층 가공 시 발생하는 치수 오차를 고려한 끼워맞춤 설계(Tolerance Design)를 수행한다.
- 경화강 노즐 사용 등 PC-CF 출력에 필요한 하드웨어 준비 사항을 숙지한다.
worked_examples:
- '예시 1: 8mm 슬리브 베어링 하우징 설계. 공칭 내경 10mm 하우징 구멍 설계 시, 출력 오차 0.15mm를 추가하여 CAD에서 10.15mm로
  설계하는 방법.'
- '예시 2: M3 인서트 너트 체결부. 나사산 손상을 방지하기 위해 인서트 홀 지름을 제조사 권장 규격보다 0.05mm 작게 설계하여 열압입(Heat-set)
  시 강한 유지력을 얻는 예시.'
lab:
  title: PC-CF 구조 부품 출력 및 치수 교정
  steps:
  - 경화강 노즐로 교체하고 FDM 3D 프린터의 레벨링을 재수행한다.
  - 손가락 링크 샘플 모델을 설계하여 0.05mm 단위의 공차 테스트 블록을 출력한다.
  - 멀티미터를 이용해 히트베드 온도를 보정하고, 설정된 110°C가 베드 전체에 고르게 분포하는지 확인한다.
  - 출력된 시편의 실측 치수와 CAD 설계 치수를 비교하여 오프셋 보정값을 산출한다.
  safety:
  - 노즐 온도 285°C 및 베드 온도 110°C에서 화상 위험이 있으므로 반드시 보호 장갑을 착용한다.
  - FDM 출력 중 발생하는 휘발성 유기화합물 차단을 위해 환기를 실시한다.
  - 경화강 노즐 교체 시 노즐 히터 블록의 열적 안전성을 확인한다.
  deliverables:
  - 테스트 시편 실측 치수 측정 기록지
  - 공차 보정값(Offset Parameter)이 반영된 5지 로봇손 CAD 파일(STL/STEP)
assignment:
  title: 로봇손 링크 부품 CAD 모델링
  deliverables:
  - 5지 로봇손 전체 어셈블리 CAD 모델링 파일
  - 각 링크별 공차 및 조립 인터페이스 설명서
  - 출력 조건(온도, 속도, 서포트 설정)이 명시된 G-code 리스트
  rubric:
  - 관절축(8mm)과 베어링 사이의 공차가 조립 가능한 범위 내에 있는가(0.05~0.15mm)?
  - 탄소섬유 필라멘트(PC-CF)의 특성을 고려하여 서포트 위치를 최소화하였는가?
  - 체결용 M3 나사 홀 규격이 미스미(Misumi) 표준을 준수하는가 [S20]?
quiz:
- question: PC-CF 필라멘트를 사용할 때 노즐 재질을 경화강(Hardened Steel)으로 변경해야 하는 이유는 무엇인가?
  choices:
  - 탄소섬유가 연마성이 강해 황동 노즐을 빠르게 마모시키기 때문
  - PC-CF의 융점이 400도 이상이기 때문
  - 경화강 노즐이 전기 전도성이 더 좋기 때문
  - 황동 노즐은 285도에서 녹기 때문
  answer_index: 0
  explanation: PC-CF 내의 탄소섬유는 매우 강한 연마 특성을 가지므로 황동과 같은 연한 재질의 노즐은 출력 중 내부 구멍이 확장되어
    품질이 저하됩니다.
- question: 제시된 데이터에 따른 적절한 히트베드 온도는 얼마인가?
  choices:
  - 60°C
  - 110°C
  - 285°C
  - 150°C
  answer_index: 1
  explanation: 제공된 정보에 따르면 PC-CF 필라멘트의 권장 베드 온도는 110°C입니다 [S19].
completion_criteria:
- 출력 테스트 블록을 통해 8mm 베어링과의 끼워맞춤 공차가 0.05mm 정밀도로 구현됨을 확인
- PC-CF의 경화강 노즐 환경 설정 완료
- 설계한 CAD 모델이 5지 로봇손의 조립 요구사항을 충족함
source_ids:
- S19
---

### 3D 프린팅을 위한 기계 설계
정교한 5지 로봇손 제작을 위해서는 부품의 기하학적 형상뿐만 아니라, FDM 적층 방식의 특성을 이해하는 설계가 필수적입니다. 탄소섬유 보강 PC(PC-CF)는 높은 강성과 열적 안정성을 제공하지만, 수축률을 고려한 치수 공차 설계가 중요합니다 [S19].

#### 1. PC-CF 물성과 노즐 선택
PC-CF는 일반적인 PLA와 달리 연마성이 강하므로 반드시 경화강(Hardened Steel) 노즐을 사용해야 합니다 [S19]. 노즐 온도는 285°C(±10°C), 히트베드 온도는 110°C(±10°C)로 설정하여 층간 접착력을 확보합니다 [S19].

#### 2. 끼워맞춤 설계(Tolerance)
베어링(igus JSM-0810-10)이나 캡스크루(M3)가 체결되는 부위는 출력 오차를 고려한 설계가 필요합니다 [S18, S20]. 통상적으로 정밀 부품 조립 시 0.1~0.2mm의 오프셋(Offset)을 적용하여 사후 가공 없이도 조립이 가능하도록 설계합니다.

#### 3. 구조 보강 설계
로봇 손가락 링크와 같이 인장력이 집중되는 부위는 레이어 방향(Layer orientation)을 조절하여 적층 결을 따라 파단이 발생하지 않도록 설계해야 합니다.
