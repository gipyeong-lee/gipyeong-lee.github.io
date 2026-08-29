---
layout: learn-module
title: Sensor Integration and Feedback Control
course_slug: precise-robot-hand
course_data_key: precise-robot-hand-en
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
translation_run_id: 0886d1415b8d413b8654c2195ac9ac00
primary_category: robotics-hardware
topics:
- robot-hands
- tendon-drive
- embedded-control
course_type: build_project
published_at: '2026-08-29T08:34:02+09:00'
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
- Implement feedback-based grasping control algorithms and practice robot hand contact
  force control
worked_examples:
- 'Example 1: FSR output calculation. When $R_{FSR}$ is 5 kΩ and $R_{fixed}$ is 10
  kΩ, given a 3.3 V input, $V_{out} = 3.3 \times (5 / (5 + 10)) = 1.1 V. This is normally
  within the ADC input range (0-3.3 V).'
- 'Example 2: Grasping force calibration. If sensor values fluctuate due to noise,
  applying a simple moving average filter can reduce rapid variations in sensor readings
  and maintain stable grasping force.'
lab:
  title: Fingertip FSR Sensor Circuit Configuration and Calibration
  steps:
  - Connect the OpenCR's 3.3 V sensor rail and GND to the breadboard.
  - Configure a voltage divider circuit by connecting the FSR 402 and a 10 kΩ resistor
    in series [B4, B5].
  - Connect the voltage divider junction to an OpenCR ADC pin [B2].
  - Connect the PC to the OpenCR and run the test code to read sensor values.
  - Record ADC values in no-load and target force-applied states to create a calibration
    table.
  safety:
  - Before applying power, you must verify with a multimeter that there is no short
    circuit between the 3.3 V rail and the 12 V actuator rail [B2].
  - Always wear safety glasses and do not place your hands within the robot hand's
    range of motion while it is powered.
  - If abnormal heat, odor, or smoke is detected, do not approach; evacuate after
    cutting the supply power to the 3 adapters at the pre-designated building distribution
    panel breaker or an authorized upstream master disconnect outside the hazardous
    zone. If there is no accessible upstream disconnection means outside the zone,
    do not energize the system. Torque release is not a substitute for power disconnection.
    Maintenance/access must only be performed after a planned shutdown, physical disconnection,
    and confirmation by de-energized measurement.
  - Before maintenance or sensor access, physically disconnect the 3 isolated power
    adapters and verify by measurement that the voltage in all branches is less than
    1 V.
  deliverables:
  - ADC sensor reading test result data
  - Sensor calibration table (ADC value vs. physical force)
  - Sensor data filtering implementation code
assignment:
  title: Grasping Force Feedback Control Algorithm Implementation
  deliverables:
  - Feedback control code (sensor reading, target comparison, motor torque adjustment)
  - Grasping test result graph (Force over time)
  - Final report (control logic explanation and grasping stability analysis)
  rubric:
  - Is the ADC data measured stably within the 0-3.3 V range?
  - Does the motor appropriately release or maintain torque when the sensor value
    reaches the target?
  - Does the torque release function work normally in software during an emergency?
  - Is the power disconnection verification procedure described in the report?
quiz:
- question: What must be strictly observed when inputting an FSR voltage divider signal
    to an OpenCR controller ADC pin?
  choices:
  - Use the 12 V actuator power rail.
  - Use only the 3.3 V sensor power rail.
  - Use the 5 V power rail.
  - Supply power separately from an external source.
  answer_index: 1
  explanation: The OpenCR ADC input range is 0-3.3 V, so you must use only the 3.3
    V sensor power rail to ensure no voltage exceeding this is applied.
- question: What is the relationship between the FSR sensor's resistance change and
    physical force?
  choices:
  - Resistance increases as pressure increases.
  - Resistance decreases as pressure increases.
  - There is no relationship between pressure change and resistance.
  - Resistance is amplified at a constant rate as pressure increases.
  answer_index: 1
  explanation: An FSR is a pressure-sensing resistor characterized by a decrease in
    sensor resistance when pressure is applied.
- question: What is the safety state that must be verified after disconnecting power
    for maintenance or access while working on the robot hand prototype?
  choices:
  - Confirm that torque has been released via software.
  - Measure if the fuse is blown using a multimeter.
  - Physically disconnect the 3 power adapters and measure with a multimeter in DC
    voltage mode to ensure the voltage in each branch is less than 1 V.
  - Turn off the power switch and measure the wire continuity in resistance mode.
  answer_index: 2
  explanation: Power disconnection refers to physically disconnecting the 3 power
    sources, and for safety, it is essential to personally verify with a multimeter
    in DC voltage mode that all branches are less than 1 V.
completion_criteria:
- Passed ADC-based FSR value reading lab
- Grasping force feedback control code reaches at least 90% of the target
- Proof of compliance with all safety rules (physical power disconnection and voltage
  measurement)
- Final results report submission
source_ids:
- S3
- S12
- S26
---

## Sensor Integration and Contact Force Feedback

Precise grasping control of a robot hand begins with accurately measuring the force applied to the fingertips. The FSR 402 sensor is a Force-Sensing Resistor whose resistance value decreases as the applied pressure increases [S12]. To convert this into a voltage signal that a microcontroller can read, a voltage divider circuit is required.

### 1. Voltage Divider Circuit
Connect the FSR sensor and a 10 kΩ divider resistor in series and supply 3.3 V sensor power [B4, B5, B2]. The ADC pin is connected to the junction of the sensor and the resistor, and the output voltage $V_{out}$ is calculated as follows:
For a 10 kΩ pull-down voltage divider, $V_{out}=V_{ref}\frac{R_{fixed}}{R_{FSR}+R_{fixed}}$ is used.

- The OpenCR controller's ADC has a 12-bit resolution, and the input range is limited to 0~3.3 V [B2]. Inputs outside this range can damage circuit components, so you must use only the specified sensor power rail (3.3 V) [B2].

### 2. Control Loop and Feedback
Measured force data is used as an input for PID control algorithms or adaptive control strategies [S3]. When the robot hand grasps an object, the tendon-driven motor (DYNAMIXEL XM430-W350-T) refers to sensor values and fine-tunes the torque until the target contact force is reached [B1, B4].
