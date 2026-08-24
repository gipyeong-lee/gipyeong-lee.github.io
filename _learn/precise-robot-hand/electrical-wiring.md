---
layout: learn-module
title: 전력 및 배선 설계
course_slug: precise-robot-hand
module_id: M6
permalink: /learn/precise-robot-hand/electrical-wiring/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: df0bcf05b81f44e1a71e0ca6fa802bac
id: M6
slug: electrical-wiring
phase_id: P2
estimated_hours: 8.0
prerequisites:
- M2
objectives:
- 로봇 시스템을 위한 안전한 전력 분배 네트워크를 설계할 수 있다.
- 커넥터 사양(Molex Micro-Fit 3.0)을 해석하고 적절한 케이블링을 수행할 수 있다.
- 산업용 전원 어댑터(Mean Well GST160A)의 사양을 이해하고 적절한 전압 및 전류 용량을 산정할 수 있다.
- 로봇 하드웨어의 배선 오류를 방지하기 위한 표준 절차를 숙지한다.
worked_examples:
- '예제 1: 시스템 전력 요구 사항 산정

  로봇 손의 5개 손가락 모터가 각각 피크 시 2A를 소모하고, 제어기가 0.5A를 소모할 때 필요한 총 전원을 계산하십시오.

  풀이: 총 전류 = (5 * 2A) + 0.5A = 10.5A. 12V 시스템 기준 총 전력 = 12V * 10.5A = 126W. GST160A12-R7B
  모델(160W/11.5A)은 충분한 마진(약 20%)을 제공하므로 적합함 [S85].'
- '예제 2: Molex Micro-Fit 커넥터 사양 확인

  사용하려는 모터 배선 전류가 7A인 경우 Micro-Fit 3.0을 사용할 수 있는지 판단하십시오.

  풀이: Micro-Fit 3.0 커넥터 시스템의 최대 정격 전류는 8.5A입니다 [S31]. 7A는 8.5A 이내이므로 허용 가능합니다.'
lab:
  title: 로봇 손 전력 분배 보드 제작 및 통전 시험
  steps:
  - 전원 공급 장치(GST160A)의 출력 전압을 멀티미터로 측정하여 12V가 정상 출력되는지 확인한다.
  - Molex Micro-Fit 3.0 터미널을 적절한 AWG 규격 전선에 압착 도구를 사용하여 연결한다.
  - TPA(터미널 위치 보장) 장치를 장착하고 하우징에 터미널을 삽입한다.
  - 전력 분배 보드에 각 모터 드라이버로 향하는 커넥터들을 결선한다.
  - 최종 결선 전, 멀티미터의 도통 모드로 각 배선 간의 쇼트(Short) 유무를 검사한다.
  safety:
  - 반드시 보안경을 착용하십시오.
  - 납땜 인두 사용 시 화상에 주의하고 통풍이 잘되는 곳에서 작업하십시오.
  - 전원 공급 장치는 단락 보호 기능이 확인된 벤치 전원을 우선 사용하십시오.
  - 끼임 방지를 위해 모터를 물리적으로 고정하거나 동력을 분리한 상태에서 시험하십시오.
  deliverables:
  - 배선도(Wiring Diagram)
  - 멀티미터 측정 기록(전압 및 도통 검사)
  - 제작된 전력 분배 보드 사진
assignment:
  title: 로봇 손 전원 시스템 설계 보고서
  deliverables:
  - 전력 요구 사항 산정 시트(Excel)
  - 커넥터 및 케이블 사양서(BOM)
  - 최종 배선 시스템 회로도
  rubric:
  - 전력 계산의 정확성(피크 부하 고려 여부)
  - 사용한 커넥터 및 전선 규격의 타당성(Molex 사양 준수)
  - 회로도 내 안전 장치(퓨즈 등) 설계 포함 여부
quiz:
- question: Molex Micro-Fit 3.0 시스템에서 'TPA'의 주된 역할은 무엇입니까?
  choices:
  - 전압을 강하시키는 변압 기능
  - 터미널이 하우징에서 뒤로 빠지는 것을 방지
  - 통신 신호를 증폭하는 기능
  - 커넥터의 냉각을 돕는 기능
  answer_index: 1
  explanation: TPA는 Terminal Position Assurance의 약자로, 터미널이 커넥터 하우징에 완전히 장착되어 빠지지 않도록
    보조적으로 잠그는 역할을 합니다 [S31].
- question: GST160A12-R7B 모델을 사용할 때의 정격 전류는 얼마입니까?
  choices:
  - 160A
  - 12A
  - 11.5A
  - 8.5A
  answer_index: 2
  explanation: GST160A12 모델의 정격 전류는 사양서에 따라 11.5A입니다 [S85].
completion_criteria:
- 전력 시스템 설계 보고서 제출
- 제작된 분배 보드의 도통 검사 통과
- 이론 퀴즈 100% 정답
source_ids:
- S85
- S31
---

### 로봇 전력 및 배선 설계 기초

로봇 손과 같은 정밀 메커니즘을 구동하기 위해서는 신뢰할 수 있는 전원 공급과 체계적인 배선이 필수적입니다. 부적절한 배선은 전압 강하(Voltage Drop), 노이즈, 혹은 화재와 같은 안전 사고를 유발할 수 있습니다.

#### 1. 전원 공급 장치 선정
로봇 시스템의 총 전력 소비를 계산한 후, 충분한 마진을 가진 어댑터를 선택해야 합니다. 예를 들어, Mean Well GST160A 시리즈는 최대 160W를 공급하며, 과전압, 과부하, 과온 보호 기능이 내장된 신뢰성 높은 장치입니다 [S85]. 출력 전압(예: 12V)과 정격 전류(예: 11.5A)를 계산하여 로봇의 모터 및 제어기 사양과 일치시켜야 합니다 [S85].

#### 2. 커넥터와 케이블링
Molex Micro-Fit 3.0과 같은 산업용 커넥터 시스템은 신호 및 전력 전달에 안정성을 제공합니다 [S31]. 3.0mm 피치와 최대 8.5A 정격 전류를 지원하며, 오결선을 방지하는 편광(Polarization) 하우징 구조를 가지고 있습니다 [S31]. 

- **TPA(Terminal Position Assurance):** 터미널이 하우징에서 이탈하는 것을 방지하는 필수 안전 기능입니다 [S31].
- **배선 시 고려 사항:** 전류 부하에 적합한 AWG(American Wire Gauge) 규격의 전선을 사용하고, 진동이 많은 로봇 관절 부위에는 스트레인 릴리프(Strain Relief)를 반드시 적용해야 합니다.

#### 3. 전력 분배 설계
로봇 내부의 제어기와 모터 드라이버는 전압 요구 사항이 다를 수 있습니다. 따라서 주 전원 입력단에서 분배 보드(Power Distribution Board)를 구성하고, 각 회로마다 적절한 퓨즈를 배치하여 국부적 고장이 전체 시스템으로 확산되지 않도록 방어해야 합니다.
