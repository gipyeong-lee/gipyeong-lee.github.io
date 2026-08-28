---
layout: learn-module
title: 3D 프린팅 및 부품 가공
course_slug: precise-robot-hand
course_data_key: precise-robot-hand
course_locale: ko
lang: ko
ref: learn:precise-robot-hand:3d-printing-assembly
translations:
- lang: ko
  url: /learn/precise-robot-hand/3d-printing-assembly/
- lang: en
  url: /learn/en/precise-robot-hand/3d-printing-assembly/
- lang: ja
  url: /learn/ja/precise-robot-hand/3d-printing-assembly/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/3d-printing-assembly/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/3d-printing-assembly/
module_id: M4
permalink: /learn/precise-robot-hand/3d-printing-assembly/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
id: M4
slug: 3d-printing-assembly
phase_id: P2
estimated_hours: 15.0
prerequisites:
- M3
objectives:
- 탄소섬유 보강 PC 필라멘트(PC-CF)를 사용한 부품 제작 및 출력 설정 최적화 이해
- 열압입 인서트(Heat-set insert) 및 슬리브 베어링의 정밀 조립 공차 관리 습득
- 텐던 구동 메커니즘을 위한 Dyneema 라인 취급 및 캡스턴 설계 구조 이해
- 로봇 구조물의 치수 안정성과 강성 확보를 위한 가공 및 체결 기법 숙지
worked_examples:
- '예제 1: PC-CF 필라멘트 노즐 선택 - 탄소섬유의 높은 마모도를 고려할 때, Brass(황동) 노즐은 빠르게 마모되어 출력 품질 저하와
  노즐 막힘을 유발하므로 반드시 경화강(Hardened steel) 노즐을 선택해야 함을 확인 [S19].'
- '예제 2: 인서트 홀 설계 - Accu HTBI-M3-BR 인서트의 외경이 4.4mm이나 공식 권장 구멍 지름은 4.0mm이므로 [S21],
  CAD 설계 시 구멍 직경을 4.0mm로 고정하여 열압입 시 플라스틱이 인서트 널링(knurling) 사이로 충분히 파고들도록 함 [S21].'
lab:
  title: 손가락 구조물 제작 및 조립 실습
  steps:
  - 경화강 노즐을 장착한 FDM 3D 프린터로 탄소섬유 PC 필라멘트 출력 환경 설정 [S19].
  - 손가락 링크와 손바닥 프레임 출력 후 서포트 제거 및 표면 정리.
  - 4.0mm 파일럿 홀에 열압입 인서트를 핫툴로 수직 안착 [S21].
  - IGUS 정밀 알루미늄 샤프트를 베어링 규격에 맞춰 절단 및 끝단 모따기 [S18].
  - 슬리브 베어링을 하우징에 압입 후 샤프트를 삽입하여 유격 확인 [S17].
  - M3 캡스크루로 구조물 및 센서 브래킷 체결 [S20].
  safety:
  - 고온의 노즐(285°C) 및 베드(110°C)에 의한 화상 주의 [S19].
  - 출력물 후가공 및 모따기 시 보안경 착용 필수.
  - 인서트 가열 시 연기 발생 가능성이 있으므로 환기 시설 가동.
  - 전원 인가 전 모든 기계적 체결 상태 확인.
  deliverables:
  - 제작된 5지 로봇손 구조물(링크, 손바닥).
  - 열압입 인서트 수직도 및 베어링 유격 측정 기록.
  - 최종 체결부 육안 검사 완료 보고서.
assignment:
  title: 로봇손 제작 정밀도 검증
  deliverables:
  - 완성된 구조물의 CAD 데이터와 실제 치수 측정 비교표
  - 조립 공차 관리 계획서
  - 텐던 라우팅 구조의 마찰 감소 설계 설명서
  rubric:
  - 열압입 인서트의 수직 안착 여부 (상/중/하)
  - 샤프트-베어링 조립 후 부드러운 회전 운동 여부 (합격/불합격)
  - BOM에 명시된 부품 정격 및 모델 규격 준수 여부 [B10, B11, B12, B13, B14]
quiz:
- question: PC-CF 필라멘트 사용 시 경화강 노즐을 사용해야 하는 주된 이유는?
  choices:
  - 탄소섬유의 마모성으로 인한 황동 노즐의 급격한 마모 방지
  - 필라멘트 녹는점이 낮아 일반 노즐로는 출력 불가
  - 출력물의 표면 광택을 증대시키기 위해
  - 압출 속도를 높이기 위해
  answer_index: 0
  explanation: 탄소섬유는 매우 높은 마모성을 가지며 일반 황동 노즐을 빠르게 파손시키므로 경화강 노즐이 필수적입니다 [S19].
- question: M3 열압입 인서트(Accu HTBI-M3-BR) 사용 시 권장되는 파일럿 홀 지름은?
  choices:
  - 3.0mm
  - 4.0mm
  - 4.4mm
  - 5.0mm
  answer_index: 1
  explanation: 공식 데이터시트에서 권장하는 구멍 지름은 4.0mm입니다 [S21].
completion_criteria:
- 모든 구조용 부품이 FDM 3D 프린터로 제작 완료됨 [B10]
- 열압입 인서트가 모든 지정된 구멍에 정확히 안착됨 [B14]
- 알루미늄 샤프트와 슬리브 베어링의 조립 유격이 기준치를 만족함 [B11, B12]
- 체결 시 명시된 M3 규격의 캡스크루가 올바르게 사용됨 [B13]
source_ids:
- S19
- S21
- S17
- S18
- S16
- S20
---

### 3D 프린팅 및 부품 가공 이론

#### 탄소섬유 강화 엔지니어링 소재 (PC-CF)
PC(Polycarbonate)는 고강성과 내열성이 뛰어나며, 여기에 탄소섬유가 첨가된 PC-CF 필라멘트는 강성을 극대화하여 구조용 부품 제작에 적합합니다 [S19]. 다만, 탄소섬유의 마모성으로 인해 반드시 경화강 노즐을 사용하여야 하며 [S19], 285°C 내외의 고온 출력이 필요합니다 [S19].

#### 정밀 조립을 위한 인서트 및 체결
플라스틱 출력물에 반복적인 조립·분해를 가능하게 하기 위해 열압입 나사산 인서트를 사용합니다 [S21]. M3 인서트의 경우 4.0mm 직경의 파일럿 홀을 CAD 설계 시 미리 배치하여 정확한 위치에 안착시켜야 합니다 [S21]. 또한, 무급유 폴리머 슬리브 베어링(iglide J)은 8mm 알루미늄 샤프트와 조립될 때 압입 후 내경이 최적의 유격을 갖도록 설계되어 있으며 [S17], 축 지름 8mm와의 공차 관리가 필수입니다 [S17, S18].

#### 텐던 구동 구조
Dyneema SK78 섬유는 1.5mm 지름에서 230 daN의 높은 파단 하중과 1% 미만의 신율을 보여 [S16], 강철 케이블의 우수한 대체재입니다. 텐던은 회전축에서 굽힘이 반복되므로, 캡스턴 모서리를 라운딩 처리하여 마찰에 의한 단선을 방지하는 구조 설계가 중요합니다.
