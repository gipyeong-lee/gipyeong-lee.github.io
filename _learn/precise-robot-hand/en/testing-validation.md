---
layout: learn-module
title: Performance Testing and Verification
course_slug: precise-robot-hand
course_data_key: precise-robot-hand-en
course_locale: en
lang: en
ref: learn:precise-robot-hand:testing-validation
translations:
- lang: ko
  url: /learn/precise-robot-hand/testing-validation/
- lang: en
  url: /learn/en/precise-robot-hand/testing-validation/
- lang: ja
  url: /learn/ja/precise-robot-hand/testing-validation/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/testing-validation/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/testing-validation/
module_id: M9
permalink: /learn/en/precise-robot-hand/testing-validation/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: 0886d1415b8d413b8654c2195ac9ac00
id: M9
slug: testing-validation
phase_id: P3
estimated_hours: 10.0
prerequisites:
- M8
objectives:
- Design quantitative test metrics to verify the robot hand's precision and repeatability
- Evaluate the stability of the grasping force control algorithm utilizing FSR sensor
  data
- Analyze the error between DYNAMIXEL actuator feedback data and actual physical motion
- Learn procedures for verifying mechanical defects and the durability of the tendon
  drive mechanism
worked_examples:
- 'Example 1: OpenCR ADC voltage calculation. When the FSR resistance is 10 kΩ and
  the series resistor is 10 kΩ, the 3.3 V voltage divider output is $V_{out} = 3.3
  * (10k / (10k + 10k)) = 1.65 V. This is suitable for the 12-bit ADC range [S13,
  S26].'
- 'Example 2: Fuse protection coordination. When 4 actuators are in a stall state,
  the sum of currents is 9.2 A [S11]. Since the cold resistance of a 10 A fuse is
  7.7 mΩ [S25], the voltage drop during normal operation is approximately 0.07 V,
  which can be neglected; however, for overcurrent, refer to the fuse manufacturer''s
  time-current curve for the exact response.'
lab:
  title: Robot Hand Integrated Functional Testing
  steps:
  - With each power branch physically disconnected, measure the output of the 3 adapters
    in DC voltage mode to confirm it reads 12 V.
  - Fix the robot hand in a safety jig and connect the controller (OpenCR) to a PC
    to release the actuator torque to 0.
  - Record the ADC data changes while manually applying pressure to the FSR sensor
    of each finger.
  - Repeat the maximum range of motion (ROM) for each finger 5 times in a no-load
    state to check for tendon interference.
  - After the test is complete, you must unplug the 3 power adapters from the wall
    outlet and check for residual voltage.
  safety:
  - Always wear safety glasses during testing.
  - Do not place your hands within the range of motion while power is applied.
  - If abnormal heat, odor, or smoke is detected, do not approach; evacuate after
    cutting the supply power to the 3 adapters at the pre-designated building distribution
    panel breaker or an authorized upstream master disconnect outside the hazardous
    zone. If there is no accessible upstream disconnection means outside the zone,
    do not energize the system. Torque release is not a substitute for power disconnection.
    Maintenance/access must only be performed after a planned shutdown, physical disconnection,
    and confirmation by de-energized measurement.
  - Do not touch the system without measuring voltage. Verifying DC is less than 1
    V is mandatory.
  deliverables:
  - Fingertip grasping force sensor calibration records
  - Repeatability precision measurement data
  - Load current measurements per power branch
assignment:
  title: Robot Hand Performance Analysis Final Report
  deliverables:
  - Performance test result analysis report
  - Data-driven grasping control algorithm code
  rubric:
  - Appropriateness of the Signal-to-Noise Ratio (SNR) analysis of sensor data
  - Quantification of precision in repeatability tests
  - Theoretical reflection on whether the protection design (fuses) satisfies the
    intended system protection
  - Comparison of design specifications and actual built performance metrics
quiz:
- question: Which of the following is correct when configuring a force measurement
    circuit using an FSR 402 sensor and OpenCR ADC?
  choices:
  - The FSR voltage divider uses only the 3.3 V sensor power and keeps the analog
    input signal in the 0~3.3 V range.
  - Configure a voltage divider with an FSR and a 10 kΩ resistor, and use a 3.3 V
    sensor rail.
  - The ADC signal must always be in the 0~5 V range.
  - Since the FSR resistance is constant, no separate divider resistor is needed.
  answer_index: 1
  explanation: Use the OpenCR sensor rail (3.3 V) to limit the ADC input to the 0~3.3
    V range and configure a voltage divider circuit to read the resistance change
    as a voltage change [S13, S26].
- question: Which of the following is correct for managing the 12 V power branch of
    a DYNAMIXEL XM430-W350-T actuator?
  choices:
  - Combine the positive (+) outputs of 3 adapters to sum the power.
  - Install a 10 A fuse for each adapter and use them as separate, independent branches.
  - Use it without safety verification since the current is below the fuse rating.
  - Connect the power adapter outputs directly in parallel without fuses.
  answer_index: 1
  explanation: Each adapter output must remain independent, and you must protect against
    overcurrent by installing a fuse suitable for the independent branch [S15].
- question: What is the most important safety procedure during the robot hand verification
    stage?
  choices:
  - Releasing torque via software is equivalent to cutting power.
  - Always verify that DC is less than 1 V with a multimeter before approaching for
    maintenance.
  - Remove the fuse, as it acts as a planned shutdown device.
  - Verify that power is cut using 'Continuity' mode.
  answer_index: 1
  explanation: Software release cannot substitute for physical power disconnection;
    it is essential to verify by measurement that there is no residual energy using
    DC voltage mode after physical disconnection.
completion_criteria:
- Submitted performance test result report and obtained at least 70 points
- Complied with safety guidelines in all Lab steps and confirmed physical power disconnection
- Confirmed implementation of the sensor data filtering function in the control code
source_ids:
- S1
- S11
- S16
- S12
- S13
- S26
- S15
- S25
---

## Performance Testing and Verification Theory

Robot hand performance verification is the process of confirming the consistency between design specifications and actual physical behavior [S1]. Key metrics include the following:

### 1. Positioning and Grasping Precision
Repeatability refers to the range of error in the position reached by the robot hand when performing the same command. While the XM430-W350-T actuator provides precise position feedback via its internal encoder [S11], the final position of the fingertip incurs errors due to tendon elongation and friction. Dyneema tendons have very low elongation (less than 1%), which is advantageous for ensuring repeatability [S16].

### 2. Force Control and FSR Sensor Signal Processing
The FSR 402 sensor is characterized by a decrease in resistance as the applied force increases [S12]. This is configured with a 10 kΩ resistor in a voltage divider circuit and measured with the OpenCR's 12-bit ADC [S13, S26]. Since sensor data is noisy, a Moving Average Filter must be applied to form a stable grasping force feedback loop.

### 3. Overcurrent Protection and Power Stability
The system uses 3 independent 12 V power branches [S15]. Each branch is protected by a 10 A ATOF fuse [S25], and distribution must be managed so that the sum of the actuator peak currents does not exceed the protection rating. This must be verified by coordinating protection via the time-current curves provided by the manufacturer.
