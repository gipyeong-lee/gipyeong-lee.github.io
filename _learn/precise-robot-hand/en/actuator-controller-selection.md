---
layout: learn-module
title: Actuator and Controller Selection
course_slug: precise-robot-hand
course_data_key: precise-robot-hand-en
course_locale: en
lang: en
ref: learn:precise-robot-hand:actuator-controller-selection
translations:
- lang: ko
  url: /learn/precise-robot-hand/actuator-controller-selection/
- lang: en
  url: /learn/en/precise-robot-hand/actuator-controller-selection/
- lang: ja
  url: /learn/ja/precise-robot-hand/actuator-controller-selection/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/actuator-controller-selection/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/actuator-controller-selection/
module_id: M3
permalink: /learn/en/precise-robot-hand/actuator-controller-selection/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: 0886d1415b8d413b8654c2195ac9ac00
primary_category: robotics-hardware
topics:
- robot-hands
- tendon-drive
- embedded-control
course_type: build_project
published_at: '2026-08-29T08:34:02+09:00'
id: M3
slug: actuator-controller-selection
phase_id: P1
estimated_hours: 10.0
prerequisites:
- M2
objectives:
- Understand the rated voltage, current, and communication characteristics of DYNAMIXEL
  XM430-W350-T actuators.
- Master the DYNAMIXEL port configuration and 12V power isolation structure of the
  OpenCR 1.0 controller.
- Design voltage divider circuits using FSR 402 sensors and 10kΩ resistors.
- Calculate system power requirements and establish independent branch fuse protection
  designs.
worked_examples:
- 'Example 1: Verify maximum current per branch. When connecting 4 XM430 actuators
  to one branch, the sum of stall current is 4 * 2.3A = 9.2A. This satisfies the 11.5A
  rating of the adapter and the 10A rating of the in-line fuse, maintaining a safe
  range [S11, S15, S25].'
- 'Example 2: Calculate FSR divider circuit voltage. Under 3.3V supply voltage, when
  FSR resistance is R_fsr, ADC input voltage V_adc = 3.3 * (10k / (10k + R_fsr)) V.
  Check resistance changes according to sensor range (0.2N~20N) and calibrate so as
  not to exceed the 0~3.3V range [S12, S13, S26].'
lab:
  title: Power Branch Configuration and ADC Sensor Interface Practice
  steps:
  - Connect an 0AFH0001Z fuse holder to each MEAN WELL adapter output and insert an
    0287010 10A fuse.
  - Set the multimeter to DC voltage mode and verify that the voltage of each branch
    is a stable 12V.
  - Configure a divider circuit using a 10kΩ resistor and FSR 402 on OpenCR's 3.3V
    sensor rail.
  - Verify that the output voltage of the divider circuit is within the 0~3.3V range
    in a non-powered state.
  safety:
  - Physically disconnect the AC power of the 3 adapters before starting work and
    verify 0V using a multimeter.
  - Always wear impact-resistant work goggles.
  - Never modify circuits or touch wiring while power is applied.
  - Clearly state that fuses are for overcurrent cutoff and not for planned stops.
  deliverables:
  - Records of 12V output measurements for each branch
  - Photos of assembled FSR divider circuit
  - Configured wiring diagrams
assignment:
  title: Power Branch and Protection Design Review
  deliverables:
  - Current branch distribution table for the entire robotic hand (actuator allocation
    per branch)
  - Calculation sheet proving selected fuses protect against actuator stall current
    without exceeding adapter capacity
  rubric:
  - Are independent fuses correctly placed in each branch?
  - Is the actuator branch distribution 4/4/3 in compliance with regulations?
  - Is sensor power supplied from the 3.3V sensor rail instead of 12V?
quiz:
- question: What is the correct power connection for a divider circuit using FSR 402
    sensors and 10kΩ resistors?
  choices:
  - 12V actuator power
  - OpenCR 3.3V sensor rail
  - 5V general power
  - OpenCR 12V output
  answer_index: 1
  explanation: OpenCR's ADC input operates based on 3.3V, so the voltage divider circuit
    must be supplied from the 3.3V sensor rail [S13].
- question: What is the stall current value of the XM430-W350-T actuator?
  choices:
  - 1.0A
  - 2.3A
  - 4.1A
  - 11.5A
  answer_index: 1
  explanation: According to the datasheet, the stall current of the actuator is 2.3A
    [S11].
- question: What is the action strictly prohibited in power branch design?
  choices:
  - Install fuses on each adapter output
  - Parallel connection of adapter positive (+) outputs
  - Use 10A fuses per branch
  - Use isolated adapters
  answer_index: 1
  explanation: The positive (+) outputs of adapters must be maintained as independent
    branches, and parallel connection is strictly prohibited [B3].
completion_criteria:
- Verification of 12V voltage of 3 independent branches completed via multimeter in
  lab
- Completed wiring and ADC input voltage range verification of FSR 402 sensor divider
  circuit
- Submission and passing of power branch and protection design report
source_ids:
- S4
- S5
- S11
- S13
- S15
- S24
- S25
- S12
- S26
---

### Actuator and Controller System Design Theory

#### 1. Actuator Selection and Power Characteristics
Use DYNAMIXEL XM430-W350-T for precision robotic hand actuation. This actuator operates at a nominal voltage of 12V, with a stall current of 2.3A [S11]. The complete robotic hand consists of 11 actuators, so the total stall current sum reaches approximately 25.3A. Therefore, an independent power supply system is required for stable operation.

#### 2. Controller Architecture
OpenCR 1.0 is equipped with a 216MHz ARM Cortex-M7 processor, making it suitable for real-time control [S13]. This controller supports a structure that can physically separate the 12V actuator power from the logic/sensor power. Analog inputs such as FSR sensors must be processed within the 0~3.3V range, so the sensor voltage divider circuit must be powered by the OpenCR's 3.3V sensor rail [S13].

#### 3. Overcurrent Protection and Power Branch Design
Use 3 MEAN WELL GST160A12-R7B adapters with 138W output [S15]. The rated current for each adapter is 11.5A, which creates 3 independent 12V branches. Each branch is equipped with an in-line 10A ATOF fuse to protect the circuit in the event of an overcurrent [S24, S25]. The fuse is set lower than the rated current of 11.5A to achieve protection coordination.

#### 4. Sensor Signal Acquisition
FSR 402 exhibits the characteristic that resistance decreases as pressure increases [S12]. Connect this to a 10kΩ fixed resistor and a voltage divider to convert the change in force into a voltage signal, and input it to the OpenCR 12bit ADC port [S12, S13, S26].
