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
translation_run_id: a92b78cca3164206863047b59d2f6ac9
id: M7
slug: firmware-development
phase_id: P3
estimated_hours: 15.0
prerequisites:
- M6
objectives:
- Understand the communication and control framework for DYNAMIXEL smart actuators.
- Implement actuator and FSR sensor signal acquisition using the OpenCR control board.
- Design real-time robot control state machines and closed-loop feedback loops.
- Program safe power management and torque release sequences.
worked_examples:
- '1. Setting actuator goal position/current: Example of code implementation to set
  the goal current of the XM430 actuator using DYNAMIXEL SDK and update the final
  position of the finger joint via PID loop according to sensor values.'
- '2. FSR voltage data filtering: Code implementation to apply a Moving Average Filter
  to remove noise from raw data collected from the ADC, and normalize the upper (20N)
  and lower (0.2N) limits [S12].'
lab:
  title: Robotic Hand Integrated Control and Precision Grasp Lab
  steps:
  - After confirming that the voltage of each independent branch is less than 1V in
    DC mode with a multimeter, start assembly.
  - Solder the FSR voltage divider circuit to the 3.3V sensor rail of OpenCR and connect
    it to the ADC port.
  - Scan the IDs of 11 actuators and set initial positions using DYNAMIXEL SDK.
  - Test finger joint driving commands in a no-load state and adjust tendon elongation
    and tension.
  - Tune grasp force response while visualizing FSR sensor data on a serial monitor.
  safety:
  - Never use 5V or 12V actuator power as a supply voltage for the FSR sensor circuit.
  - Never approach the finger operating range while the system is energized, and use
    a mounting jig.
  - Never connect the positive (+) terminals of power branch adapters to each other.
  - Before maintenance/assembly access, you must physically disconnect the 3 power
    adapters and verify that it is less than 1V in all branches by measurement.
  deliverables:
  - Firmware source code including real-time sensor data feedback
  - Normalization and calibration datasheet for voltage divider data
  - Actuator feedback loop normal operation log
assignment:
  title: Grasp State Machine Design and Implementation
  deliverables:
  - Grasp and release state machine diagram
  - Code implementation of current-based torque control
  - Final performance evaluation report
  rubric:
  - Is the current limit range (0-2.3A) based on sensor values stably controlled?
  - Does the torque release command immediately remove physical tension?
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
- question: What is the correct method to verify that the system is in a 'de-energized
    state' during robotic hand maintenance?
  choices:
  - Send a torque release command via software.
  - Check the wiring state with a multimeter in resistance mode.
  - Measure with a multimeter in DC voltage mode to ensure it is less than 1V in all
    branches.
  - Remove the power branch fuse.
  answer_index: 2
  explanation: After physical power disconnection, you must verify with a multimeter
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
- Verified with a multimeter that independent power supply and fuse protection for
  each branch are configured according to BOM specifications
- Confirmed precise force signal acquisition and filtering for 5 FSR sensors via OpenCR
  ADC
- Successfully performed software torque release routine and post-physical power disconnection
  measurement procedure
- Grasp state machine processes actuator and sensor data as intended and final report
  is submitted
source_ids:
- S13
- S11
- S12
---

### Firmware Architecture and DYNAMIXEL Control
The robotic hand's firmware acquires sensor data and processes actuator commands within a high-speed loop. The `OpenCR 1.0` controller is based on a 216MHz ARM Cortex-M7 processor [S13] and processes DYNAMIXEL protocol 2.0 without a separate bridge [S11], minimizing latency. Each actuator supports current, velocity, and position modes, and the robotic hand uses a grasp strategy based on torque through current control.

### FSR Force Feedback System
The FSR 402 sensor has resistance characteristics inversely proportional to the force applied [S12]. A voltage divider circuit is configured with a 10kΩ resistor and a 12-bit ADC [S13] using OpenCR's 3.3V sensor rail. The divided voltage is normalized via `ADC_value = (V_in * R_fsr) / (R_fsr + R_ref)`, and this value is linked with the tendon tension of the finger and used as feedback for grasp force.

### Safe Control Routines
System stops are divided into two stages for safety. In the software stage, actuator torque is released (Torque Off) to immediately remove physical driving force. Before maintenance, you must physically disconnect the power of the 3 independent power adapters, then use a multimeter in DC mode to verify that it is less than 1V in all branches.
