---
layout: learn-module
title: 센서 통합 및 피드백 제어
course_slug: precise-robot-hand
course_data_key: precise-robot-hand
course_locale: ko
lang: ko
ref: learn:precise-robot-hand:sensor-integration
translations:
- lang: ko
  url: /learn/precise-robot-hand/sensor-integration/
- lang: en
  url: /learn/en/precise-robot-hand/sensor-integration/
- lang: ja
  url: /learn/ja/precise-robot-hand/sensor-integration/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/sensor-integration/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/sensor-integration/
module_id: M8
permalink: /learn/precise-robot-hand/sensor-integration/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
id: M8
slug: sensor-integration
phase_id: P3
estimated_hours: 10.0
prerequisites:
- M7
objectives:
- FSR 402 센서와 10 kΩ 저항을 이용한 전압 분압 회로 구성 원리 이해
- OpenCR 제어기의 ADC 기능과 입력 범위(0-3.3 V) 제약 조건 숙지
- 센서 데이터의 필터링 및 캘리브레이션 기술 습득
- 피드백 기반 파지 제어 알고리즘 구현 및 로봇손의 접촉력 제어 실습
worked_examples:
- '예제 1: FSR 출력 계산. $R_{FSR}$이 5 kΩ이고 $R_{fixed}$가 10 kΩ일 때, 3.3 V 입력 기준 $V_{out}
  = 3.3 \times (5 / (5 + 10)) = 1.1 V$. 이는 ADC 입력 범위(0-3.3 V) 내에 정상적으로 위치합니다.'
- '예제 2: 파지력 보정. 센서값이 노이즈로 인해 흔들릴 경우, 단순 이동 평균 필터를 적용하여 센서값의 급격한 변동을 줄이고 파지력을 안정적으로
  유지할 수 있습니다.'
lab:
  title: 손끝 FSR 센서 회로 구성 및 보정
  steps:
  - OpenCR의 3.3 V 센서 레일과 GND를 브레드보드에 연결합니다.
  - FSR 402와 10 kΩ 저항을 직렬로 연결하여 전압 분압 회로를 구성합니다 [B4, B5].
  - 분압 접점을 OpenCR의 ADC 핀에 연결합니다 [B2].
  - PC와 OpenCR을 연결하고 센서 값을 읽는 테스트 코드를 실행합니다.
  - 무부하 상태와 목표 힘이 가해질 때의 ADC 값을 기록하여 보정표를 작성합니다.
  safety:
  - 전원 인가 전 반드시 멀티미터로 3.3 V 레일과 12 V 액추에이터 레일의 단락 여부를 확인하십시오 [B2].
  - 보안경을 상시 착용하고, 통전 중에는 로봇손의 가동 범위 내에 손을 넣지 마십시오.
  - 이상 발열·냄새·연기 감지 시 접근하지 말고, 위험 구역 밖에서 사전 지정된 건물 분전반 차단기 또는 인증된 upstream master disconnect로
    3개 어댑터의 공급 전원을 차단한 뒤 대피한다. 위험 구역 밖에서 작동 가능한 upstream 차단 수단이 없으면 시스템 통전을 금지한다.
    토크 해제는 전원 차단을 대신하지 않는다. 정비·접근은 계획 정지 후 물리적 분리 및 무전원 계측 확인 뒤에만 수행한다
  - 수리나 센서 접근 전 3개의 절연 전원 어댑터를 물리적으로 분리하고, 모든 분기의 전압이 1 V 미만임을 계측 확인하십시오.
  deliverables:
  - ADC 센서 읽기 테스트 결과 데이터
  - 센서 보정 테이블(ADC 값 vs 물리적 힘)
  - 센서 데이터 필터링 구현 코드
assignment:
  title: 파지력 피드백 제어 알고리즘 구현
  deliverables:
  - 피드백 제어 코드(센서 읽기, 목표치 비교, 모터 토크 조정)
  - 파지 시험 결과 그래프(시간 대 힘)
  - 최종 보고서(제어 로직 설명 및 파지 안정성 분석)
  rubric:
  - ADC 데이터가 0-3.3 V 범위 내에서 안정적으로 측정되는가?
  - 센서값이 목표치에 도달했을 때 모터가 적절히 토크를 해제하거나 유지하는가?
  - 비상시 토크 해제가 소프트웨어적으로 정상 작동하는가?
  - 보고서에 전원 차단 확인 절차가 기술되었는가?
quiz:
- question: OpenCR 제어기의 ADC 핀으로 FSR 전압 분압 신호를 입력할 때, 반드시 지켜야 할 사항은 무엇입니까?
  choices:
  - 12 V 액추에이터 전원 레일을 사용한다.
  - 3.3 V 센서 전원 레일만을 사용한다.
  - 5 V 전원 레일을 사용한다.
  - 전원을 별도로 외부에서 공급한다.
  answer_index: 1
  explanation: OpenCR의 ADC 입력 범위는 0-3.3 V이므로 이를 초과하는 전압이 인가되지 않도록 반드시 3.3 V 센서 전원
    레일만을 사용해야 합니다.
- question: FSR 센서의 저항값 변화와 물리적 힘의 관계는 어떠합니까?
  choices:
  - 압력이 증가하면 저항값이 증가한다.
  - 압력이 증가하면 저항값이 감소한다.
  - 압력 변화와 저항값은 무관하다.
  - 압력이 증가하면 저항값이 일정한 비율로 증폭된다.
  answer_index: 1
  explanation: FSR은 압력을 가할 때 센서의 저항값이 감소하는 특성을 가진 압력 감지 저항기입니다.
- question: 로봇손 프로토타입 작업 중 정비나 접근을 위해 전원을 차단한 후 확인해야 할 안전 상태는 무엇입니까?
  choices:
  - 소프트웨어적으로 토크를 해제했는지 확인한다.
  - 퓨즈의 단선 여부를 멀티미터로 측정한다.
  - 3개 전원 어댑터를 물리적으로 분리하고, 각 분기의 전압이 1 V 미만인지 DC 전압 모드로 계측한다.
  - 전원 스위치를 끈 뒤 저항 모드로 도선 상태를 측정한다.
  answer_index: 2
  explanation: 전원 차단은 3개 전원을 물리적으로 분리하는 것이며, 안전을 위해 반드시 멀티미터의 DC 전압 모드로 모든 분기가 1 V
    미만인지 직접 확인해야 합니다.
completion_criteria:
- ADC를 통한 FSR 값 읽기 실습 통과
- 파지력 피드백 제어 코드가 목표치에 90% 이상 도달
- 모든 안전 수칙(물리적 전원 분리 및 전압 측정) 준수 증명
- 최종 결과 보고서 제출
source_ids:
- S3
- S12
- S26
---

## 센서 통합과 접촉력 피드백

로봇손의 정밀한 파지 제어는 손끝에 작용하는 힘을 정확히 측정하는 데서 시작합니다. FSR 402 센서는 가해지는 압력이 증가할수록 저항값이 감소하는 압력 감지 저항기입니다 [S12]. 이를 마이크로컨트롤러가 읽을 수 있는 전압 신호로 변환하려면 전압 분압 회로가 필요합니다.

### 1. 전압 분압 회로
FSR 센서와 10 kΩ 분압 저항을 직렬로 연결하고 3.3 V 센서 전원을 공급합니다 [B4, B5, B2]. ADC 핀은 센서와 저항의 접점에 연결되며, 출력 전압 $V_{out}$은 다음과 같이 계산됩니다.
10 kΩ 풀다운 분압기는 $V_{out}=V_{ref}\frac{R_{fixed}}{R_{FSR}+R_{fixed}}$를 사용한다

- OpenCR 제어기의 ADC는 12비트 해상도를 가지며 입력 범위는 0~3.3 V로 제한됩니다 [B2]. 이 범위를 벗어난 입력은 회로 소자를 손상시킬 수 있으므로 반드시 지정된 센서 전원 레일(3.3 V)만을 사용해야 합니다 [B2].

### 2. 제어 루프와 피드백
측정된 힘 데이터는 PID 제어 알고리즘이나 적응형 제어 전략의 입력값으로 사용됩니다 [S3]. 로봇손이 물체를 잡을 때, 텐던 구동 모터(DYNAMIXEL XM430-W350-T)는 센서값을 참조하여 설정된 목표 접촉력에 도달할 때까지 토크를 미세 조정합니다 [B1, B4].
