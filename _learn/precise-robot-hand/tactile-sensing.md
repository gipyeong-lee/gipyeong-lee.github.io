---
layout: learn-module
title: 센서 통합 및 데이터 처리
course_slug: precise-robot-hand
module_id: mod-7
permalink: /learn/precise-robot-hand/tactile-sensing/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: c6f6c4e7134945cb931d1d58c837a6d5
id: mod-7
slug: tactile-sensing
phase_id: phase-3
estimated_hours: 10.0
prerequisites:
- mod-6
objectives:
- FSR(Force Sensing Resistor)의 원리 및 신호 처리 회로 이해
- ESP32 MCU를 활용한 아날로그 전압 데이터 취득 및 필터링 기법 습득
- 센서 데이터를 활용한 로봇손의 파지력 제어 루프 설계
- 임베디드 시스템에서의 센서 융합 데이터 처리 절차 실습
worked_examples:
- '예제 1: 10kΩ 고정 저항을 사용한 분압 회로 설계. FSR이 20N(최대압력)에서 500Ω 저항값을 가질 경우 $V_{out}$ 계산.
  $V_{cc}=3.3V$일 때, $V_{out} = 3.3 \cdot (10,000 / (500 + 10,000)) \approx 3.14V$.'
- '예제 2: ESP32의 12비트 ADC(0~4095) 변환. $V_{out} = 3.14V$인 경우, 디지털 값 $D = 4095 \cdot
  (3.14 / 3.3) \approx 3897$.'
lab:
  title: 손끝 FSR 센서 신호 취득 및 필터링 실습
  steps:
  - FSR 402 센서와 10kΩ 저항을 활용하여 브레드보드에 분압 회로 구성
  - ESP32 ADC 핀에 회로 출력 연결 및 멀티미터를 사용하여 전압 범위 측정
  - MCU 펌웨어에서 ADC 샘플링 루프 구현(샘플링 주기 10ms)
  - 구현한 코드를 통해 시리얼 플로터로 FSR에 가해지는 힘에 따른 ADC 값 변화 시각화
  - 이동 평균 필터 알고리즘을 적용하여 센서 노이즈 감소 확인
  safety:
  - 벤치 전원 공급 장치 사용 시 전압을 반드시 3.3V(MCU용)로 확인
  - 회로 연결 시 쇼트 방지를 위해 전류 제한 모드 설정(100mA 권장)
  - 납땜 시 보안경 착용 및 통풍 환경 유지
  deliverables:
  - 센서 분압 회로 배선도
  - ADC 원시 데이터 및 필터링 적용 데이터 비교 그래프
  - 센서 신호 처리 펌웨어 소스 코드
assignment:
  title: 파지력 피드백 루프 알고리즘 구현
  deliverables:
  - 파지력 제어 로직 설계서(상태 기계 포함)
  - 최종 필터링된 센서 데이터를 바탕으로 DYNAMIXEL 액추에이터 토크를 제한하는 제어 코드
  - 실제 5지 로봇손 장착 후 물체 파지 시 데이터 획득 로그
  rubric:
  - 센서 신호 처리가 실시간으로 매끄럽게 이루어지는가?
  - 센서 데이터에 따른 액추에이터의 실시간 토크 변화가 관찰되는가?
  - 비상 정지 상황에서 제어 루프가 안전하게 차단되는가?
quiz:
- question: FSR의 압력이 증가할 때 센서의 저항은 어떻게 변화하는가?
  choices:
  - 증가한다
  - 감소한다
  - 변화하지 않는다
  answer_index: 1
  explanation: FSR은 압력이 증가할수록 전도성 입자 간의 접촉이 늘어나 저항이 감소하는 압저항 특성을 가집니다 [S13].
- question: FSR 신호의 디지털 데이터 안정화를 위해 권장되는 소프트웨어 기법은?
  choices:
  - 이동 평균 필터
  - 저항값 물리적 개조
  - 전압 소스 2배 증폭
  answer_index: 0
  explanation: 측정된 ADC 값의 흔들림을 줄이기 위해 최근 데이터의 평균을 구하는 이동 평균 필터를 사용합니다.
completion_criteria:
- 5개 손가락의 FSR 데이터가 ESP32에서 노이즈 없이 취득됨을 확인
- 센서 데이터를 활용하여 로봇손이 가벼운 물체를 안전하게 파지하는 파지력 알고리즘 동작 성공
- 비상 정지 버튼 동작 시 모터 전원이 즉시 차단됨을 멀티미터로 검증 완료
source_ids:
- S3
- S13
---

## 센서 통합과 데이터 처리의 기초

로봇손이 물체를 안정적으로 파지하기 위해서는 손끝에 작용하는 힘을 실시간으로 감지해야 합니다. 이를 위해 본 로봇손은 박막형 FSR(Force Sensing Resistor)을 활용합니다. FSR은 가해지는 압력이 증가할수록 저항값이 감소하는 비선형적 특성을 가진 압저항(Piezoresistive) 센서입니다 [S13].

### 1. 센서 인터페이스 회로
FSR은 가변 저항기처럼 동작하므로 MCU가 직접 읽을 수 있는 전압으로 변환해야 합니다. 가장 일반적인 방법은 FSR과 고정 저항(Pull-down resistor)을 조합한 분압 회로(Voltage Divider)입니다. 센서의 저항을 $R_{FSR}$, 고정 저항을 $R_{fixed}$라 할 때, 출력 전압 $V_{out}$은 다음과 같습니다:

$$V_{out} = V_{cc} \cdot \frac{R_{fixed}}{R_{FSR} + R_{fixed}}$$

이 회로를 통해 FSR의 저항 변화를 전압 변화로 치환하여 MCU의 ADC(Analog-to-Digital Converter) 입력으로 전달합니다 [S13].

### 2. 신호 처리 및 노이즈 제거
로봇 환경은 전기적 노이즈에 노출되어 있어 ADC 측정값은 흔들림(Jitter)을 포함합니다. 따라서 소프트웨어적으로 신호를 매끄럽게 하는 처리가 필수적입니다. 가장 기본적인 이동 평균 필터(Moving Average Filter)를 사용하여 최근 $N$개의 측정값을 평균함으로써 데이터를 안정화합니다. 고수준 제어에서는 이 데이터를 바탕으로 물체의 미끄러짐을 감지하거나 파지력을 조절하는 피드백 루프를 구성합니다 [S3].
