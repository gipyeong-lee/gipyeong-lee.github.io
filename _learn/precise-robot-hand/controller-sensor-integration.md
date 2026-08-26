---
layout: learn-module
title: 제어기 및 센서 통합
course_slug: precise-robot-hand
module_id: mod-7
permalink: /learn/precise-robot-hand/controller-sensor-integration/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: 880e0f0309f941738bdf0ce682a0cf8c
id: mod-7
slug: controller-sensor-integration
phase_id: phase-3
estimated_hours: 15.0
prerequisites:
- mod-6
objectives:
- OpenCR 제어기 및 5지 로봇손 센서 하드웨어 인터페이스 이해
- FSR 전압 분압 회로 설계 및 ADC 신호 취득 원리 습득
- DYNAMIXEL 통신을 통한 액추에이터 제어 및 피드백 루프 구현
- 안전 제어 및 비상 정지 회로 통합 방식 학습
worked_examples:
- '예제 1: ADC 분압값 계산. FSR에 하중이 가해져 $R_{FSR}$이 5kΩ으로 변했을 때, 10kΩ 고정 저항과의 분압 전압은 $3.3V
  \times (10kΩ / (5kΩ + 10kΩ)) = 2.2V$입니다. 이는 OpenCR ADC 입력 범위(0~3.3V) 내에 안전하게 위치합니다
  [S11, S25].'
- '예제 2: 전원 분기별 부하 검증. 분기당 액추에이터 4대 연결 시, 스톨 전류 합계는 $2.3A \times 4 = 9.2A$입니다 [BOM].
  사용된 10A 퓨즈는 9.2A 피크 부하를 통과시키고 과전류 상황에서 분기를 보호합니다 [S24].'
lab:
  title: OpenCR 센서 인터페이스 및 안전 회로 결선
  steps:
  - OpenCR의 3.3V 센서 레일에서 5개의 FSR 402를 위한 분압 회로를 납땜한다.
  - 각 FSR에 10kΩ 저항을 직렬로 연결하여 ADC 입력 포트에 결선한다.
  - 독립된 3개의 12V 전원 분기에 10A 퓨즈 홀더를 각각 삽입한다.
  - 비상정지 스위치의 NC 접점을 EV200 접촉기의 코일 제어 회로에 연결한다.
  - 멀티미터를 사용하여 각 분기의 전원 단자 간 전기적 절연을 확인한다.
  safety:
  - 모든 배선 작업은 전원을 차단한 상태에서 수행할 것.
  - 12V 액추에이터 전원과 센서 회로는 전기적으로 완전히 분리 유지할 것.
  - 테스트 시 보안경을 착용하고 비상 정지 버튼이 정상 작동하는지 확인 후 구동할 것.
  - 양(+) 출력 단자끼리 결코 연결되지 않도록 주의할 것.
  deliverables:
  - 회로 연결 배선도
  - 각 FSR 채널별 ADC 출력값 데이터 기록
  - 전원 분기별 독립성 확인 멀티미터 측정 기록
assignment:
  title: 통합 제어 시스템 설계 및 안전 분석
  deliverables:
  - 최종 통합 배선도 및 BOM 검증 보고서
  - FSR 센서 ADC 출력 데이터 시각화 자료
  - 비상 정지 시스템 논리 및 하드웨어 구성 보고서
  rubric:
  - 3.3V 센서 레일 사용 및 FSR 분압 회로의 올바른 구성 여부
  - 3개 전원 분기의 완전한 절연 상태 유지 및 퓨즈 용량 적정성
  - 비상 정지 회로의 하드웨어적 독립 차단 기능 구현 여부
quiz:
- question: OpenCR의 센서 전원 레일 사용 시 주의사항으로 올바른 것은?
  choices:
  - 12V 액추에이터 레일을 FSR 센서 전원으로 사용한다.
  - 반드시 3.3V 센서 레일을 사용하여 ADC 신호를 0-3.3V 범위 내로 제한한다.
  - 모든 FSR 센서는 5V 레일에 직접 연결한다.
  - 센서 전원은 전압 분압 없이 퓨즈를 거쳐 직접 입력한다.
  answer_index: 1
  explanation: OpenCR ADC 해상도와 보호를 위해 FSR 분압 회로는 반드시 3.3V 센서 레일을 사용해야 합니다.
- question: 3개의 독립된 12V 전원 분기를 사용하는 주된 이유는 무엇인가?
  choices:
  - 전압을 36V로 올리기 위해
  - 액추에이터 간 전위 간섭 방지 및 독립적인 과전류 보호(퓨즈)를 위해
  - 전원 공급 장치의 총 무게를 줄이기 위해
  - 데이터 통신 속도를 높이기 위해
  answer_index: 1
  explanation: 독립 분기는 전위 간섭을 막고, 각 분기마다 독립된 퓨즈를 통해 고장 범위를 제한하여 안전성을 높입니다.
completion_criteria:
- 통합 제어 회로의 배선도가 BOM 및 안전 규정과 일치함
- ADC를 통한 5개 FSR의 입력 신호 데이터가 정상 취득됨
- 비상 정지 스위치 동작 시 3개 전원 분기의 접촉기가 즉시 차단됨
source_ids:
- S5
- S10
- S11
- S25
---

## 제어기 및 센서 통합 아키텍처

로봇손의 제어 시스템은 OpenCR 1.0을 중심으로 액추에이터 구동과 감각 피드백을 통합합니다. OpenCR은 216MHz ARM Cortex-M7 프로세서를 기반으로 DYNAMIXEL Protocol 2.0을 지원하여 정밀한 제어를 수행합니다 [S11].

### 센서 인터페이스: FSR 전압 분압 회로
손끝의 힘 감지를 위해 FSR 402 센서를 사용합니다 [S10]. FSR은 압력이 증가함에 따라 저항이 감소하는 특성을 가집니다. OpenCR의 ADC(12bit 해상도)를 이용해 힘을 측정하기 위해 전압 분압 회로를 구성합니다 [S11, S25].
- **회로 구성**: 3.3V 센서 전원 → FSR 센서 → ADC 핀 → 10kΩ 저항 → GND
- **원리**: 분압된 전압은 $V_{ADC} = 3.3V \times \frac{R_{fixed}}{R_{FSR} + R_{fixed}}$ 공식에 의해 산출됩니다 [S25]. 센서 전압은 반드시 OpenCR의 3.3V 센서 레일에서 공급하여 0-3.3V 범위를 유지해야 합니다 [BOM].

### 액추에이터 제어 및 전원 분기
XM430-W350-T 액추에이터는 12V를 사용하며 [BOM], 이를 위해 3개의 절연형 전원 어댑터(GST160A12-R7B)를 이용해 4/4/3대씩 독립 분기합니다 [S13]. 독립 분기는 전원 간의 전위 간섭을 방지하고 각 경로에 독립적인 10A 퓨즈를 배치하여 안전성을 확보합니다 [BOM, S24]. 비상 정지 버튼(A22E-M-12-EMO)은 EV200 접촉기의 NC 코일 회로를 통해 3개 분기를 동시에 차단하도록 설계되어야 합니다 [S21, S22].
