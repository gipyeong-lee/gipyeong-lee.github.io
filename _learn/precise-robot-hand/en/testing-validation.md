---
layout: learn-module
title: Testing and Verification
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
module_id: m8
permalink: /learn/en/precise-robot-hand/testing-validation/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
translation_run_id: c0ec26655d01411d99ed334066b74cb0
id: m8
slug: testing-validation
phase_id: p3
estimated_hours: 10.0
prerequisites:
- m7
objectives:
- Establish systematic testing procedures to evaluate the performance of the robot
  hand drive system.
- Analyze sensor data and actuator feedback for data-driven precision verification.
- Verify mechanical durability and repetitive precision of the robot hand.
- Draft operating guidelines for safe operation after system integration.
worked_examples:
- '**Example 1: Repetitive Precision Error Analysis**

  As a result of collecting encoder values after 100 repeated movements to the target
  point of 50 degrees, it was confirmed to be 50.02 degrees on average, with a standard
  deviation of 0.05 degrees. This is within the required precision range.'
- '**Example 2: FSR-based Gripping Force Calibration**

  When the ADC value is 50 with no pressure and 3800 at maximum grip (20 N), force
  (N) is estimated in real-time from the ADC value using a linear interpolation formula
  [S15].'
lab:
  title: Robot Hand Workspace and Gripping Force Verification
  steps:
  - Verify that the voltage is 12 V at the power adapter connection of each independent
    branch.
  - Mechanically check that there is no link interference of the robot hand in the
    software torque release state.
  - Gradually check the workspace of each finger in an unloaded state.
  - Log ADC signals while applying pressure to the FSR sensor in stages (0.5 N, 1
    N, 5 N).
  - After finishing the continuity test, physically disconnect all power adapters.
  - Use a multimeter to confirm that the voltage of the 3 branch(es) has discharged
    to less than 1 V.
  safety:
  - Before maintenance and access, physically disconnect the 3 isolated power adapter(s)
    and verify the zero-energy state by measurement.
  - Never place hands within the workspace while power is applied; test on a fixed
    jig.
  - If abnormal heating, odor, or smoke is detected, do not approach. Evacuate after
    cutting off the supply power of 3 adapter(s) from outside the hazardous zone using
    a pre-designated building distribution board circuit breaker or a certified upstream
    master disconnect. If there is no upstream disconnecting means operable from outside
    the hazardous zone, energizing the system is prohibited. Torque release does not
    replace power disconnection. Maintenance/access shall only be performed after
    a planned shutdown, physical disconnection, and confirmation of zero-energy measurement.
  - Always wear impact-resistant safety goggles when working.
  deliverables:
  - Workspace and gripping force test logging data file
  - Repetitive precision statistical analysis report
  - Measurement safety confirmation certificate by power branch
assignment:
  title: Writing Final Performance Verification Report
  deliverables:
  - System integration verification report (PDF)
  - Performance index numerical data and visualization graphs
  - Operating guidelines and troubleshooting procedures manual
  rubric:
  - Verification of consistency in workspace and repetitive precision measurement
    data
  - Verification of the effectiveness of the force control algorithm utilizing FSR
    sensor data
  - Evaluation of breakage and assembly stability through mechanical durability tests
  - Adherence to safety guidelines and procedural validity
quiz:
- question: Which of the following is incorrect regarding the system safety maintenance
    procedure?
  choices:
  - Perform software torque release.
  - After a planned shutdown and before maintenance/access, physically disconnect
    3 power adapter(s) and verify the zero-energy state of each branch by measurement.
  - Physically disconnect 3 power adapter(s) and verify with a multimeter in DC voltage
    mode that the residual voltage of each branch is less than 1 V.
  - Verify by measurement in DC voltage mode that each branch is less than 1 V.
  answer_index: 2
  explanation: Resistance mode can cause equipment damage and misreadings if measuring
    a circuit being energized or by capacitors that have not discharged. Zero-energy
    state verification must always use DC-voltage mode.
- question: What should be noted when configuring a circuit utilizing an FSR 402 sensor
    and an OpenCR board?
  choices:
  - The FSR voltage divider must use only 3.3 V sensor power and maintain analog input
    signals in the 0~3.3 V range.
  - The FSR divider circuit must use only 3.3 V sensor power.
  answer_index: 1
  explanation: Since the OpenCR ADC input must not exceed the 0~3.3 V range, a stable
    3.3 V sensor power must be used.
completion_criteria:
- Submit all experimental data from the testing and verification stage and complete
  log analysis.
- Adhere to the physical disconnection and safety voltage measurement procedure of
  3 independent power branch(es).
- Quantitative evaluation indices for repetitive precision and gripping force must
  achieve target ranges.
- Prove in the final report that all mechanical parts and electronic circuits operate
  safely.
source_ids:
- S1
- S12
- S14
- S15
- S18
- S21
- S16
- S17
- S26
---

### 1. Key Indices of Robot Hand Performance Evaluation
Robot hand performance verification is the process of proving the fidelity of mechanical design and the effectiveness of control algorithms [S1]. Major evaluation indices are as follows:
- **Repeatability:** The error range when reaching the same target position, calculated via high-resolution encoder feedback of the `XM430-W350-T` actuator [S14].
- **Grasp Stability:** Evaluates whether an object is gripped without slipping by analyzing the contact force distribution measured by the `FSR 402` sensor [S15].
- **Durability:** Repeated load tests are performed to check for fatigue failure of tendon (`Dyneema SK78`) and link (`PC-CF`) structures [S18, S21].

### 2. Data Acquisition and Analysis
FSR data is collected in real-time via the ADC of the `OpenCR` control board. It converts force signals with up to 12-bit resolution within a 0~3.3 V range using 3.3 V sensor power [S16]. During data acquisition, a moving average filter, etc., is applied to smooth changes in gripping force to reduce noise.

### 3. Electrical Safety Verification
Each actuator group is configured as an independent `12 V` adapter branch and protected from overcurrent with a `10 A` ATOF fuse [S17, S26]. Verification of the system's zero-energy state is always performed by measuring in DC-voltage mode (less than 1 V).
