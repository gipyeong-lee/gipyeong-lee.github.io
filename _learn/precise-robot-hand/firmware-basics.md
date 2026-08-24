---
layout: learn-module
title: 임베디드 펌웨어 기초
course_slug: precise-robot-hand
module_id: M7
permalink: /learn/precise-robot-hand/firmware-basics/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: df0bcf05b81f44e1a71e0ca6fa802bac
id: M7
slug: firmware-basics
phase_id: P3
estimated_hours: 10.0
prerequisites:
- M6
objectives:
- ESP-IDF 프레임워크의 기본 구조와 동작 원리를 이해한다.
- RTOS 기반의 태스크(Task) 관리 및 우선순위 개념을 학습한다.
- GPIO 제어 및 PWM 생성을 통해 서보 모터를 구동하는 펌웨어를 작성한다.
- 인터럽트(Interrupt)와 큐(Queue)를 활용한 비동기 데이터 처리를 구현한다.
worked_examples:
- '서보 모터 PWM 제어 예시: `ledc_timer_config`로 주파수를 설정하고 `ledc_channel_config`를 통해 50Hz
  PWM 신호를 생성하여 서보 각도를 변경하는 구조.'
- '태스크 간 데이터 공유 예시: `xQueueCreate`로 생성된 큐를 통해 센서 입력 태스크에서 모터 제어 태스크로 목표 위치 값을 전달하는
  비동기 통신 설계.'
lab:
  title: 서보 모터 제어 및 태스크 통신 실습
  steps:
  - ESP-IDF 환경 구성 및 프로젝트 빌드 시스템(`CMakeLists.txt`) 확인.
  - LED Blink 예제를 기반으로 FreeRTOS 태스크 생성 코드 작성.
  - LEDC API를 활용하여 50Hz PWM 신호 생성 및 서보 모터 연결.
  - 큐(Queue)를 사용하여 시리얼 입력에 따라 서보 각도를 조정하는 펌웨어 통합.
  - 멀티미터를 이용한 출력 전압 확인 및 오실로스코프(사용 가능 시)로 PWM 파형 검증.
  safety:
  - 벤치 전원의 전류 제한을 500mA 이하로 설정하여 과전류 방지.
  - 모터 구동 시 손가락 끼임 주의.
  - 보안경 착용 필수.
  - 배선 수정 전 반드시 전원 차단.
  deliverables:
  - 작성된 펌웨어 소스 코드 (.c, .h)
  - 태스크 구조를 나타내는 순서도
  - 실험 결과 파형 사진 또는 전압 측정 기록
assignment:
  title: 5지 로봇손용 멀티 서보 제어기 구현
  deliverables:
  - 5개 서보 모터를 독립적으로 제어하는 소스 코드
  - 제어 인터페이스 설계 보고서 (API 및 데이터 구조)
  - 로봇손 동작 시연 영상
  rubric:
  - 코드의 가독성 및 주석의 명확성 (20%)
  - FreeRTOS 태스크 및 큐 활용의 적절성 (40%)
  - 서보 모터 동작의 부드러움 및 정밀도 (30%)
  - 제출 기한 준수 및 보고서 내용 충실도 (10%)
quiz:
- question: FreeRTOS에서 태스크가 우선순위가 높은 태스크에 의해 중단되는 현상을 무엇이라 하는가?
  choices:
  - Polling
  - Preemption
  - Interrupting
  - Buffering
  answer_index: 1
  explanation: 우선순위가 높은 태스크가 실행 준비 상태가 되면 현재 실행 중인 낮은 우선순위 태스크를 일시 중지하고 CPU를 점유하는
    것을 Preemption(선점)이라고 합니다.
- question: 서보 모터 제어를 위해 ESP32에서 주로 사용되는 API는 무엇인가?
  choices:
  - GPIO
  - LEDC
  - ADC
  - I2C
  answer_index: 1
  explanation: LEDC(LED Control) 모듈은 PWM 신호를 생성하는 기능을 제공하여 서보 모터의 위치 제어에 주로 사용됩니다.
- question: 펌웨어 개발 시 '큐(Queue)'를 사용하는 주된 이유는 무엇인가?
  choices:
  - 메모리 절약
  - 태스크 간 안전한 데이터 전달
  - CPU 속도 향상
  - 인터럽트 무시
  answer_index: 1
  explanation: 큐는 멀티태스킹 환경에서 여러 태스크 간에 데이터를 안전하게 주고받기 위한 표준 동기화 기법입니다.
completion_criteria:
- 실습 Lab을 완료하고 제어 펌웨어가 5개 서보 모터를 독립적으로 동작시킴을 확인.
- 과제 Assignment의 소스 코드와 보고서 제출.
- 퀴즈에서 3문제 중 2문제 이상 정답.
source_ids:
- S84
---

## 임베디드 펌웨어와 ESP-IDF

로봇손과 같은 정교한 시스템은 실시간성(Real-time)이 보장된 제어를 필요로 합니다. ESP-IDF는 Espressif SoC를 위한 공식 개발 프레임워크로, FreeRTOS를 기반으로 하여 다중 태스크 처리와 하드웨어 자원의 효율적인 관리를 지원합니다 [S84].

### 1. FreeRTOS 태스크 구조
임베디드 소프트웨어는 보통 `main` 함수에서 시스템을 초기화한 후, 여러 개의 태스크를 생성하여 실행합니다. 태스크는 독립적인 스택을 가지며, OS 스케줄러에 의해 시분할 방식으로 CPU 자원을 공유합니다. 우선순위가 높은 태스크가 실행되면 낮은 태스크는 중단(Preemptive)됩니다.

### 2. 하드웨어 추상화 계층(HAL)
직접 레지스터를 제어하는 대신 ESP-IDF의 API를 사용하면 코드의 이식성과 안전성이 높아집니다. 예를 들어, `ledc` API는 서보 모터 제어에 필수적인 고해상도 PWM 신호를 생성하는 데 사용됩니다.

### 3. 이벤트 기반 처리
모터 위치 명령이나 센서 값을 처리할 때, 메인 루프에서 폴링(Polling)하는 대신 큐(Queue)와 세마포어(Semaphore)를 사용하여 태스크 간 데이터를 안전하게 주고받고 인터럽트를 처리하는 것이 정교한 제어의 핵심입니다.
