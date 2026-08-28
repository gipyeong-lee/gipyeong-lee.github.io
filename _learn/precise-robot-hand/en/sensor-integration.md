---
layout: learn-module
title: Sensor Integration and Feedback Control
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.en
course_locale: en
lang: en
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
permalink: /learn/en/precise-robot-hand/sensor-integration/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: a92b78cca3164206863047b59d2f6ac9
id: M8
slug: sensor-integration
phase_id: P3
estimated_hours: 10.0
prerequisites:
- M7
objectives:
- Understand the configuration principle of a voltage divider circuit using an FSR
  402 sensor and a 10 kΩ resistor
- Master the ADC function of the OpenCR controller and its input range (0-3.3 V) constraints
- Acquire sensor data filtering and calibration techniques
- Implement feedback-based grasp control algorithms and practice robot hand contact
  force control
worked_examples:
- 'Example 1: Calculating FSR output. When $R_{FSR}$ is 5 kΩ and $R_{fixed}$ is 10
  kΩ, based on 3.3 V input, $V_{out} = 3.3 \times (5 / (5 + 10)) = 1.1 V. This is
  normally located within the ADC input range (0-3.3 V).'
- 'Example 2: Grasp force calibration. If the sensor value fluctuates due to noise,
  applying a simple moving average filter can reduce rapid fluctuations in sensor
  data and maintain grasp force stably.'
lab:
  title: Fingertip FSR Sensor Circuit Configuration and Calibration
  steps:
  - Connect OpenCR's 3.3 V sensor rail and GND to the breadboard.
  - Connect FSR 402 and 10 kΩ resistor in series to construct a voltage divider circuit
    [B4, B5].
  - Connect the divider junction to the OpenCR's ADC pin [B2].
  - Connect PC to OpenCR and execute the test code to read sensor values.
  - Create a calibration table by recording ADC values in the no-load state and when
    the target force is applied.
  safety:
  - Before applying power, always use a multimeter to check for short circuits between
    the 3.3 V rail and the 12 V actuator rail [B2].
  - Always wear safety glasses, and do not put your hands within the robot hand's
    range of motion while energized.
  - If abnormal heat, odor, or smoke is detected, do not approach. Evacuate after
    cutting off supply power to 3 adapters using a designated building distribution
    board circuit breaker or a certified upstream master disconnect outside the hazard
    zone. Do not energize the system if no upstream disconnecting means is operable
    outside the hazard zone. Torque release does not replace power disconnection.
    Maintenance and access must only be performed after planned shutdown, physical
    disconnection, and verified measurement of a de-energized state.
  - Before repairing or accessing sensors, physically disconnect 3 isolated power
    adapters and verify by measurement that the voltage in all branches is less than
    1 V.
  deliverables:
  - ADC sensor reading test result data
  - Sensor calibration table (ADC value vs physical force)
  - Sensor data filtering implementation code
assignment:
  title: Grasp Force Feedback Control Algorithm Implementation
  deliverables:
  - Feedback control code (sensor reading, target comparison, motor torque adjustment)
  - Grasp test result graph (Force vs Time)
  - Final report (Explanation of control logic and grasp stability analysis)
  rubric:
  - Is ADC data measured stably within the 0-3.3 V range?
  - Does the motor appropriately release or maintain torque when the sensor value
    reaches the target?
  - Does the emergency torque release function normally via software?
  - Is the power-off verification procedure described in the report?
quiz:
- question: When inputting an FSR voltage divider signal to the OpenCR controller's
    ADC pin, what must be observed?
  choices:
  - Use the 12 V actuator power rail.
  - Use only the 3.3 V sensor power rail.
  - Use the 5 V power rail.
  - Supply power externally.
  answer_index: 1
  explanation: The OpenCR ADC input range is 0-3.3 V, so you must use only the 3.3
    V sensor power rail to ensure no voltage exceeding this is applied.
- question: What is the relationship between the FSR sensor's resistance value change
    and physical force?
  choices:
  - Resistance increases as pressure increases.
  - Resistance decreases as pressure increases.
  - There is no relationship between pressure change and resistance.
  - Resistance amplifies at a constant rate as pressure increases.
  answer_index: 1
  explanation: The FSR is a pressure-sensitive resistor characterized by its resistance
    value decreasing when pressure is applied.
- question: What is the safety state that must be verified after turning off the power
    for maintenance or access during robot hand prototype work?
  choices:
  - Confirm that torque has been released via software.
  - Measure whether the fuse is blown using a multimeter.
  - Physically disconnect 3 power adapters and measure with DC voltage mode to ensure
    the voltage in each branch is less than 1 V.
  - Turn off the power switch and measure the conductor state in resistance mode.
  answer_index: 2
  explanation: Power disconnection means physically separating 3 power sources, and
    for safety, you must directly verify by measurement in DC voltage mode that all
    branches are less than 1 V.
completion_criteria:
- Passed FSR value reading practice via ADC
- Grasp force feedback control code reached 90% or more of the target value
- Proof of compliance with all safety protocols (physical power disconnection and
  voltage measurement)
- Submission of final results report
source_ids:
- S3
- S12
- S26
---

## Sensor Integration and Contact Force Feedback

Precise grasp control of a robot hand begins with accurately measuring the force applied to the fingertips. The FSR 402 sensor is a force-sensing resistor whose resistance value decreases as the applied pressure increases [S12]. To convert this into a voltage signal that a microcontroller can read, a voltage divider circuit is required.

### 1. Voltage Divider Circuit
Connect the FSR sensor and the 10 kΩ divider resistor in series and supply 3.3 V sensor power [B4, B5, B2]. The ADC pin is connected to the junction of the sensor and the resistor, and the output voltage $V_{out}$ is calculated as follows:

A 10 kΩ pull-down divider uses $V_{out}=V_{ref}\frac{R_{fixed}}{R_{FSR}+R_{fixed}}$

- The OpenCR controller's ADC has a 12-bit resolution and is limited to an input range of 0~3.3 V [B2]. Input outside this range can damage circuit components, so you must only use the specified sensor power rail (3.3 V) [B2].

### 2. Control Loop and Feedback
The measured force data is used as an input value for PID control algorithms or adaptive control strategies [S3]. When the robot hand grasps an object, the tendon-driven motor (DYNAMIXEL XM430-W350-T) references the sensor values to fine-tune torque until the set target contact force is reached [B1, B4].
