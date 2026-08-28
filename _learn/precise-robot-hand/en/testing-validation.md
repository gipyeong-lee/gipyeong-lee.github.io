---
layout: learn-module
title: Performance Testing and Verification
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.en
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
translation_run_id: a92b78cca3164206863047b59d2f6ac9
id: M9
slug: testing-validation
phase_id: P3
estimated_hours: 10.0
prerequisites:
- M8
objectives:
- Design quantitative test metrics to verify robot hand precision and repeatability
- Evaluate the stability of grasp force control algorithms utilizing FSR sensor data
- Analyze errors between DYNAMIXEL actuator feedback data and actual physical motion
- Acquire procedure for verifying mechanical defects and tendon drive mechanism durability
worked_examples:
- 'Example 1: Calculating OpenCR ADC voltage. When FSR resistance is 10 kΩ and serial
  resistance is 10 kΩ, the 3.3 V voltage divider output V_out = 3.3 * (10k / (10k
  + 10k)) = 1.65 V. This is suitable within the 12-bit ADC range [S13, S26].'
- 'Example 2: Fuse protection coordination. When 4 actuators are in a stall state,
  the sum of current is 9.2 A [S11]. Since the cold resistance of a 10 A fuse is 7.7
  mΩ [S25], the voltage drop during normal operation is about 0.07 V and can be ignored,
  but for precise response during overcurrent, refer to the fuse manufacturer''s time-current
  curve.'
lab:
  title: Robot Hand Integrated Function Test
  steps:
  - With each power branch physically disconnected, measure the output of 3 adapters
    in DC voltage mode to verify that 12 V is output.
  - Fix the robot hand in a safety jig, connect the controller (OpenCR) to the PC,
    and release actuator torque to 0.
  - Record ADC data changes by manually applying pressure to the FSR sensor for each
    finger.
  - Repeatedly operate each finger to its maximum range of motion (ROM) 5 times in
    a no-load state to check for tendon interference.
  - After the test, always disconnect 3 power adapters from the wall outlet and verify
    residual voltage.
  safety:
  - Always wear safety glasses during the test.
  - Do not put your hands within the range of motion while power is applied.
  - If abnormal heat, odor, or smoke is detected, do not approach. Evacuate after
    cutting off supply power to 3 adapters using a designated building distribution
    board circuit breaker or a certified upstream master disconnect outside the hazard
    zone. Do not energize the system if no upstream disconnecting means is operable
    outside the hazard zone. Torque release does not replace power disconnection.
    Maintenance and access must only be performed after planned shutdown, physical
    disconnection, and verified measurement of a de-energized state.
  - Do not touch the system without voltage measurement. DC verification of less than
    1 V is mandatory.
  deliverables:
  - Fingertip grasp force sensor calibration records
  - Repeatability precision measurement data
  - Load current measurements per power branch
assignment:
  title: Final Robot Hand Performance Analysis Report
  deliverables:
  - Performance test result analysis report
  - Data-driven grasp control algorithm code
  rubric:
  - Appropriateness of sensor data signal-to-noise ratio (SNR) analysis
  - Quantification of precision in repeatability testing
  - Theoretical reflection on whether the protection design (fuse) satisfies the system
    protection intent
  - Comparison of design specifications and performance indicators of the final product
quiz:
- question: When configuring a force measurement circuit using an FSR 402 sensor and
    OpenCR ADC, what is correct?
  choices:
  - The FSR voltage divider uses only the 3.3 V sensor power and keeps the analog
    input signal in the 0~3.3 V range.
  - Construct a voltage divider with an FSR and a 10 kΩ resistor and use the 3.3 V
    sensor rail.
  - The ADC signal must always be in the 0~5 V range.
  - An FSR has constant resistance, so no separate divider resistor is needed.
  answer_index: 1
  explanation: Use the OpenCR sensor rail (3.3 V) to limit the ADC input to the 0~3.3
    V range, and configure a divider circuit to read resistance changes as voltage
    changes [S13, S26].
- question: What is the correct way to manage the 12 V power branch of a DYNAMIXEL
    XM430-W350-T actuator?
  choices:
  - Bundle the positive (+) outputs of 3 adapters together to sum the power.
  - Equip each adapter with a 10 A fuse and use it as an individual independent branch.
  - It can be used without safety verification because the current is below the fuse
    rating.
  - Connect power adapter outputs directly in parallel without fuses.
  answer_index: 1
  explanation: Each adapter output must be maintained independently, and overcurrent
    must be protected by installing a fuse suitable for the independent branch [S15].
- question: What is the most important safety procedure in the robot hand verification
    stage?
  choices:
  - Releasing torque via software is equivalent to cutting off power.
  - Always approach maintenance after checking for less than 1 V DC with a multimeter.
  - The fuse acts as a planned shutdown device, so you can pull the fuse out.
  - Confirm that power is disconnected with continuity mode.
  answer_index: 1
  explanation: Software release does not replace physical power cutoff; it is essential
    to verify that there is no residual energy by measuring in DC voltage mode after
    physical disconnection.
completion_criteria:
- Submission of performance test result report and achieving 70 points or more
- Compliance with safety guidelines and verification of physical power disconnection
  completed in all Lab steps
- Verification of sensor data filtering function implementation in control code
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

Robot hand performance verification is the process of confirming the correspondence between design specifications and actual physical behavior [S1]. The main indicators are as follows.

### 1. Position and Grasp Precision
Repeatability refers to the error range of the position reached by the robot hand when performing the same command. The XM430-W350-T actuator provides precise position feedback via internal encoders [S11], but errors occur in the final fingertip position due to tendon elongation and friction. Dyneema tendons have very low elongation, less than 1%, which is advantageous for securing repeatability [S16].

### 2. Force Control and FSR Sensor Signal Processing
The FSR 402 sensor is characterized by its resistance decreasing according to the applied force [S12]. This is configured with a 10 kΩ resistor and a voltage divider circuit to be measured by OpenCR's 12-bit ADC [S13, S26]. Since sensor data has significant noise, a Moving Average Filter must be applied to form a stable grasp force feedback loop.

### 3. Overcurrent Protection and Power Stability
The system uses 3 independent 12 V power branches [S15]. Each branch is protected by a 10 A ATOF fuse [S25], and distribution must be done so that the sum of actuator peak currents does not exceed protection ratings. Protection coordination must be verified using the time-current curves of the fuses provided by the manufacturer.
