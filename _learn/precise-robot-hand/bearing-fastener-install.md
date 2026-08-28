---
layout: learn-module
title: 베어링 및 체결 부품 설치
course_slug: precise-robot-hand
course_data_key: precise-robot-hand
course_locale: ko
lang: ko
ref: learn:precise-robot-hand:bearing-fastener-install
translations:
- lang: ko
  url: /learn/precise-robot-hand/bearing-fastener-install/
- lang: en
  url: /learn/en/precise-robot-hand/bearing-fastener-install/
- lang: ja
  url: /learn/ja/precise-robot-hand/bearing-fastener-install/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/bearing-fastener-install/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/bearing-fastener-install/
module_id: M5
permalink: /learn/precise-robot-hand/bearing-fastener-install/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
id: M5
slug: bearing-fastener-install
phase_id: P2
estimated_hours: 10.0
prerequisites:
- M4
objectives:
- 정밀 로봇손 제작을 위한 베어링 및 샤프트의 기계적 공차와 설치 원리를 이해한다.
- 열압입 인서트(Heat-set insert)를 사용하여 엔지니어링 플라스틱 부품의 체결 강도를 확보하는 방법을 습득한다.
- 적절한 토크와 체결 규격을 사용하여 조립 유격을 최소화한다.
worked_examples:
- '예시 1: 하우징 내경 확인 - iglide® JSM-0810-10 베어링의 외경은 10 mm이다. 따라서 하우징 보어는 10 mm에 맞게 설계되어야
  하며, 인서트 삽입 시 파일럿 홀 4.0 mm를 지키지 않으면 인서트가 헛돌거나 하우징이 파손될 수 있다 [S17, S21].'
- '예시 2: M3 나사 조립 - M3x10 캡스크루는 2.5 mm 육각 렌치를 사용하여 체결하며, 과도한 토크는 인서트 주변 수지에 크랙을 유발할
  수 있으므로 ''더 이상 돌아가지 않는 시점''에서 최소한의 힘으로 고정한다 [S20].'
lab:
  title: 로봇손 관절 정밀 조립
  steps:
  - 1. PC-CF 출력물 하우징에 4.0 mm 파일럿 홀이 깨끗한지 확인하고 인서트를 수직으로 정렬한다.
  - 2. 인두기를 적정 온도로 가열하여 인서트를 수직으로 천천히 눌러 하우징 표면과 평행하게 압입한다.
  - 3. iglide® 베어링을 보어에 압입하고, 8 mm 알루미늄 샤프트를 삽입하여 유격과 저항을 확인한다.
  - 4. M3 나사를 사용하여 링크 간 체결을 완료하고, 관절을 움직여 마찰이 균일한지 검증한다.
  safety:
  - 인두기는 고온이므로 화상에 주의하고 가열 후 즉시 거치대에 놓는다.
  - 인서트 압입 시 발생하는 미세 먼지는 흡입하지 않도록 환기를 철저히 한다.
  - 보안경을 필히 착용하고 작업을 진행한다.
  - 이상 발열·냄새·연기 감지 시 접근하지 말고, 위험 구역 밖에서 사전 지정된 건물 분전반 차단기 또는 인증된 upstream master disconnect로
    3개 어댑터의 공급 전원을 차단한 뒤 대피한다. 위험 구역 밖에서 작동 가능한 upstream 차단 수단이 없으면 시스템 통전을 금지한다.
    토크 해제는 전원 차단을 대신하지 않는다. 정비·접근은 계획 정지 후 물리적 분리 및 무전원 계측 확인 뒤에만 수행한다
  deliverables:
  - 관절별 마찰 시험 로그
  - 인서트 수직 정렬 확인 사진
  - 조립된 링크의 자유도 및 유격 측정 기록
assignment:
  title: 조립 공차 및 체결력 분석 보고서
  deliverables:
  - 관절 조립 순서 및 토크 관리 계획서
  - 유격 발생 시 해결 방안(Shim 사용 또는 공차 수정) 기술
  - 조립 완료된 로봇손 링크의 파지 시험 예비 데이터
  rubric:
  - 인서트 삽입의 수직도가 명확하게 기술되었는가?
  - 베어링과 샤프트의 공차 개념을 올바르게 설명했는가?
  - 조립 단계에서의 안전 수칙을 준수했는가?
quiz:
- question: iglide® J 베어링이 하우징에 압입된 후 내경이 조정되는 이유는 무엇인가?
  choices:
  - 베어링 재질의 탄성 때문에 압입 시 내경이 자동으로 늘어난다.
  - 압입 과정에서 베어링 내경이 하우징 보어의 공차에 맞춰 정밀하게 조정되도록 설계되었기 때문이다.
  - 압입 전의 내경은 항상 기준치보다 작게 제작되기 때문이다.
  answer_index: 1
  explanation: iglide® 슬리브 베어링은 압입 전 기준치보다 큰 상태로 제작되며, 올바른 하우징 보어에 압입되었을 때 설계된 공차
    내의 내경을 갖도록 설계되었습니다 [S17].
- question: PC-CF 출력물에 황동 열압입 인서트를 사용할 때 적절한 파일럿 홀 크기는?
  choices:
  - 3.5 mm
  - 4.0 mm
  - 4.4 mm
  answer_index: 1
  explanation: 데이터시트에 따르면 HTBI-M3-BR 인서트의 권장 파일럿 홀 크기는 4.0 mm입니다 [S21].
completion_criteria:
- 조립된 5개 손가락 관절의 마찰 저항이 균일함을 확인하고 측정 기록 제출.
- 모든 인서트가 PC-CF 하우징과 수평을 이루는지 육안 및 치수 검사 완료.
- 조립 중 안전 수칙을 준수했음을 서약하고 작업 기록부 제출.
source_ids:
- S17
- S18
- S20
- S21
---

### 베어링과 샤프트의 공차 관리
정밀 로봇 관절의 부드러운 움직임과 강성 확보를 위해 iglide® J 슬리브 베어링(JSM-0810-10)과 8 mm 알루미늄 정밀 샤프트(AWMP-08)를 사용한다. 슬리브 베어링은 하우징에 압입(press-fit)될 때 내경이 조정되도록 설계되었으며, 하우징의 권장 내경 공차를 준수하는 것이 핵심이다 [S17, S18]. 유격이 발생하면 관절의 정밀도가 떨어지고, 반대로 너무 좁으면 마찰력이 증가하여 구동기(DYNAMIXEL XM430)의 전류 효율을 저하시킨다.

### 열압입 인서트 설치
PC-CF(탄소섬유 보강 PC) 출력물은 금속 나사를 직접 체결할 경우 재질의 특성상 나사산이 마모되기 쉽다. 이를 방지하기 위해 황동 재질의 열압입 인서트(HTBI-M3-BR)를 사용한다 [S21]. 인서트는 4.0 mm 파일럿 홀에 삽입 후 열을 가해 주변 수지를 녹여 체결함으로써, 반복적인 분해 조립에도 높은 기계적 강도를 유지한다 [S21]. 이때 인서트가 기울어지면 조립된 링크의 정렬이 어긋나므로 수직 유지가 필수적이다.
