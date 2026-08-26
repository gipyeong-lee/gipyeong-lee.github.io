---
layout: learn-module
title: 스마트 액추에이터 및 제어기 통신
course_slug: precise-robot-hand
module_id: M6
permalink: /learn/precise-robot-hand/actuator-controller-integration/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: 269a85a61ef242a9ad03b3d15be4bc06
id: M6
slug: actuator-controller-integration
phase_id: PH3
estimated_hours: 20.0
prerequisites:
- M5
objectives:
- DYNAMIXEL 스마트 액추에이터의 동작 원리와 제어 프로토콜 이해
- OpenCR 제어기의 구조 및 DYNAMIXEL 통신 포트 활용법 습득
- FSR 센서 신호의 아날로그 디지털 변환 및 전압 분압 회로 설계
- 안전 릴레이 체인을 이용한 비상 정지 및 전력 차단 시스템 구현
worked_examples:
- '**분기 전류 계산:** 액추에이터 11대의 최대 스톨 전류 합계는 25.3 A입니다. 3개 전원 분기(11.5 A 정격)를 사용하므로 분기당
  전류 부하는 약 8.43 A이며, 이는 분기별 10 A ATOF 퓨즈 규격 내에 들어옵니다 [S14, S26].'
- '**전압 분압 설계:** FSR(R_fsr)과 10 kΩ(R_fixed) 저항을 직렬 연결 시, 출력 전압 V_out = 3.3 V * (R_fixed
  / (R_fsr + R_fixed))입니다. 3.3 V 센서 레일을 사용하므로 ADC 포화 없이 힘 데이터 취득이 가능합니다 [S11, S12,
  S27].'
lab:
  title: 액추에이터 통신 및 안전 체인 구성
  steps:
  - OpenCR 보드와 DYNAMIXEL 액추에이터를 TTL/RS-485 포트에 연결합니다 [S12].
  - A22E NC 접점과 G7SA 코일을 연결하여 안전 릴레이 체인을 구성합니다 [S21, S23].
  - G7SA NO 접점 3개를 각각 G2R-1-SND 코일과 연결합니다 [S21, S22].
  - G2R 릴레이 접점이 EV200AAANA 코일의 전원을 제어하도록 배선합니다 [S22, S24].
  - 멀티미터를 사용하여 비상정지 작동 시 EV200 접촉기 양단이 개방되는지 확인합니다.
  safety:
  - 모든 회로 변경 전 반드시 전원을 차단합니다.
  - 보안경을 착용하고 비상 정지 시 전압 강하를 확인합니다.
  - 분기 전원은 반드시 독립적으로 운영하며 병렬 연결을 금지합니다.
  - 실제 기계 안전 시스템이 아니므로 사람 접근 시 전문가 검토가 필수입니다.
  deliverables:
  - 구성된 제어 체인 배선도
  - 비상정지 작동/복구 시 접촉기 상태 검증 로그
  - FSR 센서 ADC 출력 데이터 샘플
assignment:
  title: 제어 시스템 통합 설계 보고서
  deliverables:
  - 통합 배선도 및 안전 체인 블록도
  - 액추에이터 전력 분배 계산서
  - FSR 센서 교정 곡선 데이터
  rubric:
  - 안전 체인 시퀀스가 정확히 준수되었는가?
  - 전력 분기가 규격에 맞게 독립적으로 할당되었는가?
  - ADC 입력이 3.3 V 범위를 초과하지 않게 설계되었는가?
quiz:
- question: FSR 센서 ADC 입력 전압 분압 회로를 구동하기 위한 전압 레일은?
  choices:
  - 12 V 액추에이터 전원
  - 3.3 V 센서 전원
  - 24 V 입력 전원
  - 5 V 전원
  answer_index: 1
  explanation: OpenCR의 센서 회로 안정성과 ADC 보호를 위해 반드시 3.3 V 센서 전원을 사용해야 합니다 [S12].
- question: 비상정지 발생 시 EV200 접촉기를 제어하는 올바른 릴레이 체인은?
  choices:
  - A22E NC → EV200 코일
  - A22E NC → G7SA → G2R → EV200 코일
  - A22E NO → G2R → EV200 코일
  - G7SA NC → EV200 코일
  answer_index: 1
  explanation: A22E 저전류 NC 신호로 강제 유도 릴레이(G7SA)와 중계 릴레이(G2R)를 거쳐 EV200 코일을 제어해야 합니다
    [S21, S22, S23, S24].
- question: 전원 분기 어댑터의 양(+) 단자를 병렬로 연결해도 됩니까?
  choices:
  - 예, 전류 용량이 늘어납니다.
  - 절대 금지입니다.
  - 퓨즈가 있다면 가능합니다.
  - 접촉기가 있다면 가능합니다.
  answer_index: 1
  explanation: 독립된 어댑터 분기는 전기적으로 반드시 격리되어야 하며 병렬 연결은 금지됩니다 [B3].
completion_criteria:
- 안전 체인 회로 구성 및 작동 확인
- OpenCR-액추에이터 간 통신 성공
- FSR 센서 데이터 측정 및 전압 분압값 검증
- 안전 설계 통합 보고서 제출
source_ids:
- S3
- S4
- S5
- S12
- S23
- S21
- S22
- S24
- S11
- S27
- S14
- S26
---

## 스마트 액추에이터 통신 및 제어
DYNAMIXEL 스마트 액추에이터는 모터, 제어기, 드라이버, 센서 및 감속기가 통합된 지능형 서보 모듈입니다 [S3]. 제어 명령은 프로토콜 2.0을 통해 패킷 형태로 송수신되며, 실시간 전류, 속도, 위치 피드백을 제공하여 정밀한 장력 제어를 가능하게 합니다 [S3, S4].

## 전력 및 안전 시스템 설계
로봇손 시스템은 12 V 액추에이터 전원 분기를 사용하며, 각 분기는 독립적인 안전 회로를 갖추어야 합니다. 본 설계에서는 A22E 비상정지 스위치 [S23], G7SA 강제 유도 안전 릴레이 [S21], G2R-1-SND 중계 릴레이 [S22], 그리고 EV200AAANA 고전류 접촉기 [S24]로 구성된 4단계 제어 체인을 통해 안전을 확보합니다.

### 안전 체인 시퀀스
1. **입력:** A22E 비상정지 스위치 (NC)가 차단됨 [S23].
2. **분리:** G7SA 안전 릴레이 코일이 소자되며 3개의 NO 접점이 즉시 개방 [S21].
3. **중계:** 개방된 G7SA 접점이 3개의 G2R-1-SND 릴레이 코일 전원을 차단 [S22].
4. **차단:** EV200AAANA 접촉기가 개방되어 3개 분기의 액추에이터 전력을 차단 [S24].
이 방식은 저전류 제어 신호로 고전류 부하를 안전하게 격리합니다.

## 센서 신호 처리
FSR 402 센서는 인가된 힘에 따라 저항값이 감소하는 박막형 센서입니다 [S11]. OpenCR 제어기의 12비트 ADC 입력을 위해 10 kΩ 저항과 분압 회로를 구성합니다 [S12, S27]. 이때 반드시 3.3 V 센서 전원을 사용하여 ADC 입력을 0~3.3 V 범위 내로 유지해야 합니다 [S12].
