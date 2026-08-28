---
layout: learn-module
title: Firmware Development and Control
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.en
course_locale: en
lang: en
ref: learn:precise-robot-hand:firmware-development
translations:
- lang: ko
  url: /learn/precise-robot-hand/firmware-development/
- lang: en
  url: /learn/en/precise-robot-hand/firmware-development/
- lang: ja
  url: /learn/ja/precise-robot-hand/firmware-development/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/firmware-development/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/firmware-development/
module_id: M7
permalink: /learn/en/precise-robot-hand/firmware-development/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: 0886d1415b8d413b8654c2195ac9ac00
id: M7
slug: firmware-development
phase_id: P3
estimated_hours: 15.0
prerequisites:
- M6
objectives:
- Understand DYNAMIXEL smart actuator communication and control framework.
- Implement actuator and FSR sensor signal acquisition using OpenCR control board.
- Design real-time robot control state machine and closed-loop feedback loop.
- Program safe power management and torque release sequences.
worked_examples:
- '1. Setting actuator goal position/current: An example of using DYNAMIXEL SDK to
  set current limit (Goal Current) for XM430 actuator and updating finger joint final
  position via a PID loop based on sensor values.'
- '2. FSR voltage data filtering: Code implementation for applying a Moving Average
  Filter to remove noise from raw data collected from ADC and normalizing the range
  with upper (20N) and lower (0.2N) limits [S12].'
lab:
  title: Robotic Hand Integrated Control and Precision Grip Practice
  steps:
  - Verify that the voltage of each independent branch is less than 1V using multimeter
    DC mode before starting assembly.
  - Solder FSR voltage divider circuit to OpenCR's 3.3V sensor rail and connect to
    ADC port.
  - Scan IDs of 11 actuators using DYNAMIXEL SDK and set initial positions.
  - Test finger joint drive commands in no-load state and adjust tendon elongation
    and tension.
  - Visualize FSR sensor data via serial monitor and tune grip force response.
  safety:
  - Never use 5V or 12V actuator power as supply for FSR sensor circuit.
  - Never approach the operating range of fingers while system is energized; use fixtures.
  - Never connect positive (+) terminals of power branch adapters to each other.
  - Before maintenance/assembly access, physically disconnect the 3 power adapters
    and verify that it is less than 1V in all branches by measurement.
  deliverables:
  - Firmware source code including real-time sensor data feedback
  - Data sheet for normalization and calibration of voltage divider data
  - Actuator feedback loop normal operation logs
assignment:
  title: Grip State Machine Design and Implementation
  deliverables:
  - Grip and release state machine diagram
  - Code implementing current-based torque control
  - Final performance evaluation report
  rubric:
  - Is the current limit range (0-2.3A) according to sensor values stably controlled?
  - Does the physical tension dissipate immediately upon the torque release command?
  - Is a safe hardware disconnection procedure explicitly stated in the code?
quiz:
- question: What is the recommended power rail when configuring an FSR 402 sensor
    and a voltage divider circuit?
  choices:
  - 12V actuator power rail
  - 5V general-purpose power rail
  - OpenCR 3.3V sensor rail
  - 24V external input rail
  answer_index: 2
  explanation: For system safety and OpenCR ADC protection, the FSR voltage divider
    circuit must be connected to the 3.3V sensor power rail.
- question: What is the correct way to confirm that the system is in a 'de-energized
    state' when performing robot hand maintenance?
  choices:
  - Send a torque release command via software.
  - Check the wiring status with a multimeter in resistance mode.
  - Measure with a multimeter in DC voltage mode to ensure it is under 1V in all branches.
  - Remove the power branch fuses.
  answer_index: 2
  explanation: After physically disconnecting the power, you must verify with a multimeter
    in DC voltage mode that the residual voltage in all branches is less than 1V.
- question: Is it permissible to connect the positive (+) terminals of multiple independent
    power adapter outputs in parallel?
  choices:
  - It is necessary for current summation.
  - It is strictly prohibited.
  - It is possible if the rated output currents are the same.
  - It is possible if fuses are installed.
  answer_index: 1
  explanation: The positive (+) outputs of power adapters configured as independent
    branches must never be connected or integrated with each other.
completion_criteria:
- Multimeter verification completed that independent power supply and fuse protection
  for each branch are configured according to BOM specifications
- Confirmed precision force signal acquisition and filtering of 5 FSR sensors via
  OpenCR ADC
- Successfully performed the software torque release routine and post-physical power
  disconnection measurement procedure
- The grasping state machine processes actuator and sensor data as intended, and the
  final report is submitted
source_ids:
- S13
- S11
- S12
---

### Firmware Architecture and DYNAMIXEL Control
The robotic hand firmware acquires sensor data and processes actuator commands within a high-speed loop. The `OpenCR 1.0` controller is based on a 216MHz ARM Cortex-M7 processor [S13] and processes DYNAMIXEL protocol 2.0 without a separate bridge [S11], minimizing latency. Each actuator supports current, velocity, and position modes, and the robotic hand uses a current-control-based torque grip strategy.

### FSR Force Feedback System
The FSR 402 sensor has a resistance characteristic inversely proportional to the force applied [S12]. A voltage divider circuit is configured with a 10kΩ resistor on the 3.3V sensor rail using OpenCR's 12-bit ADC [S13]. The divided voltage is normalized via `ADC value = (V_in * R_fsr) / (R_fsr + R_ref)`, and this value is linked with the tendon tension of the fingers and used as grip force feedback.

### Safe Control Routine
System stop is divided into two stages for safety. In the software stage, actuator torque is released (Torque Off) to immediately remove physical driving force. Before maintenance, you must physically disconnect the 3 independent power adapters and verify that all branches are less than 1V using multimeter DC mode.
