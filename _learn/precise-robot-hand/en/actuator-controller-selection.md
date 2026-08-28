---
layout: learn-module
title: Actuator and Controller Selection
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.en
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
translation_run_id: a92b78cca3164206863047b59d2f6ac9
id: M3
slug: actuator-controller-selection
phase_id: P1
estimated_hours: 10.0
prerequisites:
- M2
objectives:
- Understand the rated voltage, current, and communication characteristics of the
  DYNAMIXEL XM430-W350-T actuator.
- Become familiar with the OpenCR 1.0 controller's DYNAMIXEL port configuration and
  12V power separation structure.
- Design a voltage divider circuit using an FSR 402 sensor and a 10kΩ resistor.
- Calculate system power requirements and establish independent branch fuse protection
  designs.
worked_examples:
- 'Example 1: Checking maximum current per branch. When connecting 4 XM430 actuators
  to one branch, the sum of stall current is 4 * 2.3A = 9.2A. This satisfies the 11.5A
  rating of the adapter and the 10A rating of the inline fuse, maintaining a safe
  range [S11, S15, S25].'
- 'Example 2: Calculating FSR divider circuit voltage. Under 3.3V supply voltage,
  when FSR resistance is R_fsr, ADC input voltage V_adc = 3.3 * (10k / (10k + R_fsr))
  V. Verify resistance changes according to sensor range (0.2N~20N) and calibrate
  so it does not exceed the 0~3.3V range [S12, S13, S26].'
lab:
  title: Power Branch Configuration and ADC Sensor Interface Lab
  steps:
  - Connect an 0AFH0001Z fuse holder to each MEAN WELL adapter output and insert a
    0287010 10A fuse.
  - Set the multimeter to DC voltage mode and verify that the voltage of each branch
    is a stable 12V.
  - Configure a voltage divider circuit using a 10kΩ resistor and FSR 402 on the OpenCR
    3.3V sensor rail.
  - Verify in a non-powered state that the output voltage of the divider circuit is
    within the 0~3.3V range.
  safety:
  - Before starting work, physically disconnect the AC power of the 3 adapters and
    verify it is 0V with a multimeter.
  - Always wear impact-resistant safety glasses for work.
  - Never change circuits or touch wiring while power is applied.
  - Explicitly state that the fuse is for overcurrent cutoff and not a means for planned
    stops.
  deliverables:
  - Record of 12V output measurements for each branch
  - Photos of FSR divider circuit assembly completion
  - Configured wiring diagram
assignment:
  title: Power Branch and Protection Design Review
  deliverables:
  - Current branch distribution table for the entire robotic hand (actuator allocation
    per branch)
  - Calculation sheet proving that the selected fuse protects against actuator stall
    current without exceeding adapter capacity
  rubric:
  - Are independent fuses correctly placed in each branch?
  - Does the actuator branch allocation comply with regulations of 4/4/3?
  - Is sensor power supplied from the 3.3V sensor rail, not 12V?
quiz:
- question: What is the correct power connection for a voltage divider circuit using
    an FSR 402 sensor and a 10kΩ resistor?
  choices:
  - 12V actuator power
  - OpenCR 3.3V sensor rail
  - 5V universal power
  - OpenCR 12V output
  answer_index: 1
  explanation: Since OpenCR's ADC input operates based on 3.3V, the voltage divider
    circuit must be supplied from the 3.3V sensor rail [S13].
- question: What is the stall current value of the XM430-W350-T actuator?
  choices:
  - 1.0A
  - 2.3A
  - 4.1A
  - 11.5A
  answer_index: 1
  explanation: According to the datasheet, the stall current of the actuator is 2.3A
    [S11].
- question: What action is strictly prohibited in power branch design?
  choices:
  - Installing fuses on each adapter output
  - Parallel connection of adapter positive (+) outputs
  - Using 10A fuses per branch
  - Using isolated adapters
  answer_index: 1
  explanation: Adapter positive (+) outputs must be maintained as independent branches;
    parallel connection is strictly prohibited [B3].
completion_criteria:
- Verification of 12V voltage for 3 independent branches completed via multimeter
  in lab
- Completion of wiring and ADC input voltage range check for FSR 402 sensor divider
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
We use the DYNAMIXEL XM430-W350-T for precise control of the robotic hand. This actuator operates at a nominal voltage of 12V, and the stall current is 2.3A [S11]. The entire robotic hand consists of 11 actuators, so the total stall current reaches approximately 25.3A. Therefore, an independent power supply system is required for stable operation.

#### 2. Controller Architecture
The OpenCR 1.0 is equipped with a 216MHz ARM Cortex-M7 processor, making it suitable for real-time control [S13]. This controller supports a structure that allows physical separation of the 12V actuator power and the logic/sensor power. Analog inputs, such as those from FSR sensors, must be processed within the 0~3.3V range, so the sensor voltage divider circuit must be supplied by the OpenCR's 3.3V sensor rail [S13].

#### 3. Overcurrent Protection and Power Branch Design
We use 3 MEAN WELL GST160A12-R7B adapters with 138W output [S15]. The rated current of each adapter is 11.5A, which creates 3 independent 12V branches. We install a 10A ATOF fuse inline in each branch to protect the circuit in case of overcurrent [S24, S25]. The fuse is set lower than the rated current of 11.5A to achieve protection coordination.

#### 4. Sensor Signal Acquisition
The FSR 402 has the characteristic that resistance decreases as pressure increases [S12]. We connect this as a voltage divider with a 10kΩ fixed resistor to convert the change in force into a voltage signal and input it into the OpenCR's 12bit ADC port [S12, S13, S26].
