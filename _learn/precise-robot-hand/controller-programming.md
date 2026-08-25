---
layout: learn-module
title: 임베디드 제어 프로그래밍
course_slug: precise-robot-hand
module_id: M6
permalink: /learn/precise-robot-hand/controller-programming/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: d15f1f9bf2e148d5b847db3615e52388
id: M6
slug: controller-programming
phase_id: P3
estimated_hours: 15.0
prerequisites:
- M5
objectives:
- ESP-IDF 프레임워크 기반의 임베디드 제어 환경 이해
- 실시간 제어를 위한 태스크(Task) 스케줄링 및 큐(Queue) 활용법 습득
- 서보 모터 제어를 위한 PWM 신호 생성 및 설정
- 로봇손 관절 피드백을 위한 센서 데이터 수집 및 처리
worked_examples:
- '서보 모터 PWM 제어 예제: LEDC를 설정하고 0도에서 180도까지 서보 각도를 변경하는 코드를 작성합니다. 주파수는 50Hz, 분해능은
  16비트로 설정하여 미세한 각도 제어를 가능하게 합니다.'
- '태스크 간 큐 통신 예제: 센서 태스크에서 측정한 로봇손의 현재 상태 데이터를 큐에 넣고, 제어 태스크가 이를 받아 모터 출력을 결정하는 Producer-Consumer
  패턴 구현 예제를 분석합니다.'
lab:
  title: 로봇손 서보 제어 및 센서 데이터 피드백 구현
  steps:
  - ESP-IDF 개발 환경을 설정하고 서보 모터 PWM 설정을 위한 LEDC API를 분석합니다.
  - 서보 모터 1개를 벤치 전원에 연결하고, 0도와 90도 위치로 주기적으로 이동시키는 펌웨어를 업로드합니다.
  - 가변 저항(Potentiometer)을 ADC 핀에 연결하여 모터의 위치 값을 읽어들입니다.
  - 센서 값을 읽어 목표 위치와 비교하고, 오차를 줄이는 제어 알고리즘을 추가합니다.
  safety:
  - 저전압 벤치 전원 사용 시 출력 전압을 5V~6V로 제한합니다.
  - 모터 구동 시 과전류로 인한 보드 손상을 방지하기 위해 전류 제한 기능을 활성화합니다.
  - 움직이는 관절부 주위에 손가락 끼임 주의합니다.
  - 납땜 시 보안경을 착용합니다.
  deliverables:
  - 제어 펌웨어 소스 코드 (.c 및 .h)
  - PWM 파형 측정 데이터 (멀티미터 혹은 오실로스코프)
  - 센서 데이터가 올바르게 전송되는 것을 보여주는 시리얼 모니터 로그
assignment:
  title: 5지 로봇손 동시 제어 알고리즘 구현
  deliverables:
  - 5개 손가락 서보 모터 동시 제어 소스 코드
  - 각 손가락별 센서 값 기반 폐루프(Closed-loop) 제어 구현서
  - 비상 정지(Emergency Stop) 및 전원 차단 로직 설명
  rubric:
  - 5개 모터의 개별적인 제어가 성공적으로 구현되었는가?
  - 센서 데이터 기반의 오차 보정 알고리즘이 안정적으로 작동하는가?
  - 임베디드 태스크 스케줄링이 적절히 배치되어 시스템 지연이 없는가?
  - 비상 정지 로직이 즉각적으로 반영되는가?
quiz:
- question: ESP-IDF에서 태스크 간 데이터를 안전하게 주고받기 위해 권장되는 방법은 무엇입니까?
  choices:
  - 전역 변수 직접 사용
  - 큐(Queue) 사용
  - 파일 쓰기
  - 메모리 포인터 직접 전달
  answer_index: 1
  explanation: ESP-IDF는 다중 태스크 환경에서 데이터 안전성을 위해 큐(Queue) 사용을 권장합니다.
- question: 서보 모터의 회전 각도를 결정하는 핵심 신호 방식은?
  choices:
  - GPIO 디지털 신호
  - 아날로그 전압
  - PWM 펄스 폭
  - UART 시리얼 데이터
  answer_index: 2
  explanation: 서보 모터는 PWM 신호의 펄스 폭에 의해 회전 각도가 결정됩니다.
completion_criteria:
- 서보 모터 5개를 독립적으로 제어하는 펌웨어 작성 완료
- 센서 데이터를 활용한 위치 제어 루프 정상 작동 검증
- 임베디드 제어 코드의 메모리 및 태스크 할당 최적화 확인
source_ids:
- S19
---

## 임베디드 제어 프로그래밍 개요
로봇손의 정교한 동작을 위해서는 고성능 MCU(ESP32 등)와 이를 지원하는 공식 개발 프레임워크인 ESP-IDF를 활용해야 합니다 [S19]. ESP-IDF는 FreeRTOS를 기반으로 하여 다중 태스크 환경을 효율적으로 지원합니다.

### 1. 태스크 관리 및 인터럽트
로봇손은 여러 손가락의 움직임을 동시에 제어해야 하므로, 각 손가락을 별도의 태스크로 분리하여 스케줄링합니다. `xTaskCreate`를 사용하여 태스크를 생성하고, `vTaskDelay`를 통해 CPU 점유율을 최적화합니다.

### 2. PWM 기반 모터 제어
서보 모터는 PWM(Pulse Width Modulation) 신호의 펄스 폭(Pulse Width)에 따라 각도가 결정됩니다. ESP32의 LEDC(LED Control) 주변장치는 고해상도 PWM 신호를 생성하는 데 최적화되어 있습니다.

### 3. 데이터 교환
센서 데이터(위치, 압력)와 모터 명령은 큐(Queue)를 통해 태스크 간 안전하게 전달됩니다. 이는 데이터 레이스(Race Condition)를 방지하고 실시간성을 확보하기 위한 핵심 설계 패턴입니다.
