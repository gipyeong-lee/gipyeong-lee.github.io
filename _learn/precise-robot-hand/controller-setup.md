---
layout: learn-module
title: 제어기 및 센서 인터페이스
course_slug: precise-robot-hand
module_id: mod6
permalink: /learn/precise-robot-hand/controller-setup/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: 6107198626784e959dfcf1327da4f9c8
id: mod6
slug: controller-setup
phase_id: phase3
estimated_hours: 15.0
prerequisites:
- mod5
objectives:
- OpenCR 제어 보드의 아키텍처와 DYNAMIXEL 인터페이스를 이해한다.
- FSR 402 센서를 활용한 전압 분압 회로를 설계하고 OpenCR ADC로 힘 데이터를 취득한다.
- 정밀 파지 제어를 위한 센서 데이터 필터링 기초를 습득한다.
worked_examples:
- '예제 1: OpenCR ADC값 계산. FSR에 5N의 힘이 가해져 $R_{FSR}$이 2kΩ이 되었다면, $V_{out} = 3.3V \times
  (10k\Omega / (2k\Omega + 10k\Omega)) = 2.75V$가 출력됩니다. 이를 12비트 ADC로 변환하면 $2.75V /
  3.3V \times 4095 \approx 3412$의 값이 측정됩니다.'
- '예제 2: 안전 설계 확인. FSR 전압 분압 회로는 반드시 3.3V 센서 전원 레일에 연결되어야 합니다. 12V 액추에이터 전원이나 5V 전원을
  사용할 경우 ADC 입력 범위를 초과하거나 제어기가 손상될 수 있으므로 주의해야 합니다.'
lab:
  title: FSR 힘 센서 인터페이스 구축
  steps:
  - OpenCR 보드의 3.3V 센서 전원 핀을 확인합니다.
  - FSR 402 센서의 한쪽 단자와 10kΩ 저항을 연결하고, 저항의 나머지 단자를 GND에 연결합니다.
  - FSR과 저항이 만나는 지점(분압점)을 OpenCR의 ADC 핀에 연결합니다.
  - 멀티미터를 DC 전압 모드로 설정하고 연결부의 전압이 0~3.3V 범위 내에 있는지 측정합니다.
  - PC를 연결하여 OpenCR의 ADC 데이터 스트리밍 코드를 실행하고 힘 변화에 따른 값을 확인합니다.
  safety:
  - 모든 회로 수정은 3개의 독립 전원 어댑터를 물리적으로 분리한 무전원 상태에서 수행합니다.
  - 회로 연결 완료 후 반드시 멀티미터 DC 전압 모드로 측정하여 3.3V 라인에 12V가 유입되지 않았는지 확인합니다.
  - 배선 접근 전 모든 전원 분기 전압이 1V 미만임을 반드시 계측기로 확인합니다.
  deliverables:
  - 회로 연결도
  - 센서 힘-ADC값 데이터 표(최소 5개 지점)
  - 측정된 센서 분압점의 DC 전압값 기록
assignment:
  title: 센서 데이터 필터링 알고리즘 설계
  deliverables:
  - FSR 센서 데이터를 노이즈로부터 보호하기 위한 단순 이동 평균(SMA) 필터 구현 코드
  - 필터 적용 전후의 데이터 파형을 비교한 최종 보고서
  rubric:
  - 필터링 알고리즘이 샘플 데이터를 정상적으로 처리하는가?
  - 3.3V 센서 전원 및 회로 격리 원칙을 준수했는가?
  - 데이터 표와 측정이 정확하게 작성되었는가?
quiz:
- question: OpenCR 1.0에서 FSR 센서의 전압 분압 회로를 위해 반드시 사용해야 하는 전원 레일은 무엇입니까?
  choices:
  - 12V 액추에이터 전원
  - 3.3V 센서 전원
  - 5V 전원
  - AC 220V
  answer_index: 1
  explanation: OpenCR의 ADC 입력은 3.3V를 기준으로 동작하며, 12V나 5V는 회로 손상을 유발합니다.
- question: FSR 센서와 함께 사용되는 10kΩ 저항의 역할은 무엇입니까?
  choices:
  - 전류를 무한대로 제한
  - 전압 분압 회로의 기준 저항
  - 액추에이터 속도 제어
  - 통신 종단 저항
  answer_index: 1
  explanation: FSR은 저항값만 변하므로, 전압 신호로 변환하기 위해 10kΩ 고정 저항과 직렬로 연결하여 전압을 분압합니다.
completion_criteria:
- OpenCR과 FSR 센서의 물리적 인터페이스 구축 완료
- ADC 핀에서 0~3.3V 범위의 전압 신호 정상 측정
- 실습 안전 지침을 준수하며 각 전원 어댑터별 무전원 상태 계측 완료
source_ids:
- S13
- S14
- S26
---

### 제어기 아키텍처: OpenCR
본 프로젝트의 핵심 제어기인 OpenCR 1.0은 216MHz의 고속 CPU를 탑재하여 액추에이터 명령과 센서 데이터를 동시에 처리합니다 [S14]. 특히, 별도의 통신 브리지 없이 DYNAMIXEL TTL 및 RS-485 포트를 내장하고 있어 통신 지연을 최소화하고 시스템 재현성을 높입니다 [S14].

### FSR 센서와 전압 분압 회로
FSR(Force Sensing Resistor) 402는 가해지는 힘이 증가함에 따라 저항이 감소하는 압력 가변 저항 센서입니다 [S13]. 이 센서를 디지털 제어기에서 읽기 위해 전압 분압 회로를 사용합니다.

OpenCR의 ADC는 0~3.3V 범위를 지원합니다 [S14]. FSR 센서의 저항($R_{FSR}$)과 기준 저항($R_{FIX} = 10k\Omega$ [S26])을 조합하여 다음과 같이 전압을 분압합니다:
$$V_{out} = V_{ref} \times \frac{R_{FIX}}{R_{FSR} + R_{FIX}}$$
여기서 $V_{ref}$는 OpenCR의 3.3V 센서 전원 레일입니다. 이 신호는 12비트 ADC를 통해 0~4095의 디지털 값으로 변환됩니다 [S14].
