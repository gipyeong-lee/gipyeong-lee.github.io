---
layout: learn-module
title: 구동부 제작 및 배치
course_slug: precise-robot-hand
module_id: M3
permalink: /learn/precise-robot-hand/actuator-assembly/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: d15f1f9bf2e148d5b847db3615e52388
id: M3
slug: actuator-assembly
phase_id: P2
estimated_hours: 20.0
prerequisites:
- M2
objectives:
- 로봇 구동기(Actuator)의 기본 원리와 DYNAMIXEL X 시리즈의 통신 사양을 이해한다.
- 로봇손의 각 관절에 필요한 토크와 속도를 계산하여 적합한 구동기를 선정한다.
- 구동기를 로봇 프레임에 견고하게 배치하고 기계적 간섭을 최소화하는 조립 기술을 습득한다.
- 통신 브리지(U2D2 등)를 사용하여 구동기를 제어 환경에 연결한다.
worked_examples:
- '사례 1: MCP 관절의 필요 토크 계산. 무게 0.5kg의 물체를 0.1m 떨어진 거리에서 지지할 때 필요한 토크 $\tau = 0.5kg
  \times 9.8m/s^2 \times 0.1m = 0.49 Nm$. 선정된 XM430-W350의 사양을 비교하여 안전율 1.5 적용 시 0.735
  Nm 이상의 토크가 보장되는지 확인합니다.'
- '사례 2: DYNAMIXEL ID 설정. 여러 개의 모터를 동일한 통신 버스에 연결할 때, ''DYNAMIXEL Wizard 2.0''을 사용하여
  각 모터에 고유 ID를 할당하고 보레이트(Baud Rate)를 설정하는 과정을 수행합니다 [S17].'
lab:
  title: DYNAMIXEL 제어 환경 구축 및 테스트
  steps:
  - U2D2와 PC를 연결하고 DYNAMIXEL Wizard 2.0을 실행합니다.
  - 각 관절용 모터의 고유 ID를 순차적으로 설정합니다.
  - 3D 프린팅된 테스트 핑거 프레임에 모터를 조립합니다.
  - 벤치 전원을 사용하여 모터에 전원을 인가하고 토크를 측정합니다.
  - 간단한 위치 제어 코드를 작성하여 모터의 회전 범위를 확인합니다.
  safety:
  - 보안경을 반드시 착용합니다.
  - 전류 제한 회로를 구현하여 모터 과부하 시 전원을 즉시 차단합니다.
  - 움직이는 관절부에 손가락이 끼이지 않도록 주의합니다.
  - 저전압(12V~24V) 벤치 전원만을 사용합니다.
  deliverables:
  - 조립된 관절 프레임 사진
  - 각 모터의 ID 및 통신 설정 기록표
  - 모터 구동 테스트 영상
assignment:
  title: 5지 로봇손 구동 배치 설계서
  deliverables:
  - CAD 도면 (모터 배치 및 케이블 경로 표시)
  - 관절별 부하 계산서
  - BOM(Bill of Materials) 및 부품 사양서
  rubric:
  - 부하 계산의 정확성 (40%)
  - 기구학적 간섭 발생 여부 및 최적화 (30%)
  - 문서의 표준화된 형식 준수 (30%)
quiz:
- question: DYNAMIXEL X 시리즈에서 제공하는 주요 제어 방식이 아닌 것은?
  choices:
  - 위치 제어
  - 전류(토크) 제어
  - 자기장 직접 제어
  - 속도 제어
  answer_index: 2
  explanation: DYNAMIXEL X 시리즈는 위치, 속도, 전류 기반 제어를 제공하며 자기장을 직접 제어하는 방식은 제공하지 않습니다
    [S17].
- question: 관절 배치 시 케이블 구동(Tendon-driven) 방식을 사용하는 주된 이유는?
  choices:
  - 모터의 무게를 손가락 끝으로 이동시켜 힘을 증폭하기 위해
  - 손가락의 무게와 부피를 줄이기 위해
  - 모터의 통신 속도를 빠르게 하기 위해
  - 모터의 수명을 늘리기 위해
  answer_index: 1
  explanation: 모터를 손가락이 아닌 손바닥이나 팔뚝에 배치하여 손가락 자체의 부피와 관성을 줄이기 위함입니다.
completion_criteria:
- 모든 모터의 통신이 성공적으로 확인됨.
- 관절 부하 계산서가 사양 범위 내에 있음을 검증함.
- 제출된 CAD 도면에서 기구학적 간섭이 없음을 입증함.
source_ids:
- S17
---

### 구동기 선정 및 기계적 통합

로봇손의 성능은 구동기의 출력 특성에 직결됩니다. 5지 로봇손 설계 시 가장 중요한 단계는 각 관절이 감당해야 할 정적/동적 부하를 계산하는 것입니다.

1. **DYNAMIXEL X 시리즈 사양 분석**:
로봇 관절용 서보 모터로 널리 사용되는 DYNAMIXEL XM430-W350은 고성능 기어 감속기와 위치, 속도, 전류 기반 제어를 제공합니다 [S17]. 통신은 DYNAMIXEL Protocol 2.0을 사용하며 [S17], 이는 실시간 위치 피드백과 상태 모니터링을 가능하게 합니다.

2. **부하 분석 및 선정**:
관절의 토크 계산식: $\tau = F \times d \times \sin(\theta)$
($\tau$: 토크, $F$: 말단부 작용력, $d$: 회전축으로부터의 거리, $\theta$: 각도).
손가락의 각 관절은 말단으로 갈수록 요구 토크가 낮아지지만, 기초 관절(MCP)은 최대 부하를 받으므로 이를 기준으로 모터를 선정해야 합니다.

3. **배치 전략**:
로봇손의 공간 제약으로 인해 모터를 손바닥이나 팔뚝에 배치하는 케이블 구동(Tendon-driven) 방식을 고려해야 합니다. 이때 모터 간의 간섭과 케이블의 마찰을 최소화하는 배치가 핵심입니다.
