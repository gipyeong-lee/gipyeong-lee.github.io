---
layout: learn-module
title: Wiring and Building Safe Power Isolation
course_slug: precise-robot-hand
course_data_key: precise-robot-hand-en
course_locale: en
lang: en
ref: learn:precise-robot-hand:wiring-safety-system
translations:
- lang: ko
  url: /learn/precise-robot-hand/wiring-safety-system/
- lang: en
  url: /learn/en/precise-robot-hand/wiring-safety-system/
- lang: ja
  url: /learn/ja/precise-robot-hand/wiring-safety-system/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/wiring-safety-system/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/wiring-safety-system/
module_id: M6
permalink: /learn/en/precise-robot-hand/wiring-safety-system/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: 0886d1415b8d413b8654c2195ac9ac00
id: M6
slug: wiring-safety-system
phase_id: P2
estimated_hours: 10.0
prerequisites:
- M5
objectives:
- Understand how to configure independent 12 V power branches for actuator driving.
- Learn the role and selection principles of ATOF fuses for overcurrent protection.
- Master safe power management and physical disconnection protocols.
- Configure safe voltage divider circuits for OpenCR controllers and FSR sensors.
worked_examples:
- In case of abnormal heat, odor, or smoke, do not approach; cut the power supply
  to the 3 adapters via a pre-designated building panel breaker outside the hazard
  zone or a certified upstream master disconnect and evacuate. If no upstream disconnect
  is available outside the hazard zone, do not energize the system. Torque release
  is not a substitute for power disconnection. Maintenance/access must only be performed
  after planned stops, physical disconnection, and verifying the de-energized state
  by measurement [S11] [S25]
- 'Example 2: FSR ADC circuit voltage - Connect 10 kΩ divider resistors and FSR 402
  using OpenCR''s 3.3 V sensor rail [S13, S26]. The sensor signal voltage must be
  within the 0~3.3 V range, and this circuit must be physically/electrically isolated
  from the 12 V actuator power circuit.'
lab:
  title: Power Branch Harness Fabrication and Safety Inspection
  steps:
  - Solder ATO in-line fuse holders to each adapter output line and insert 10 A ATOF
    fuses [S24, S25].
  - Fabricate actuator and sensor connection harnesses using Molex Micro-Fit 3.0 connectors
    [S14].
  - Distribute and wire the OpenCR board and each actuator into 3 branches and connect
    to each power adapter [S13].
  - Verify insulation state of each adapter output terminal using multimeter resistance
    mode before applying power.
  - Verify that each branch is 12 V in voltage mode after applying power, and always
    remove 3 adapters when disconnecting.
  safety:
  - Physically disconnect 3 power adapters before maintenance.
  - Replace parts after verifying residual voltage is less than 1 V using a multimeter.
  - Do not place hands inside operating range while power is applied.
  - Insulate all connection points and wear goggles when soldering.
  deliverables:
  - Photos of fabricated power branch harness
  - Voltage measurement records per branch
  - Wiring diagram review confirmation
assignment:
  title: Safety Wiring Design Report
  deliverables:
  - Actuator allocation design for 3 power branches (4/4/3 units per branch)
  - Calculation sheet for overcurrent protection per branch (comparison of peak current
    and fuse rating)
  - Physically disconnect 3 power adapters before maintenance/access after planned
    stops and verify de-energized state of each branch by measurement
  rubric:
  - Was power independence and isolation principle followed?
  - Were fuse and connector ratings appropriately selected for the load?
  - Does the power disconnection and residual voltage verification protocol follow
    safety guidelines?
quiz:
- question: Is it permissible to connect the 12 V output (+) of each power adapter
    in parallel?
  choices:
  - Possible, current supply capacity increases.
  - Impossible, must maintain as independent branches.
  - Possible if voltage matches.
  - Possible if fuses are added.
  answer_index: 1
  explanation: Each adapter output must be maintained independently, and parallel
    connection is strictly prohibited [S15].
- question: What is the most prioritized safety measure before robotic hand maintenance?
  choices:
  - Software torque release
  - Multimeter resistance measurement
  - Physical disconnection of 3 power adapters and residual voltage verification
  - Press planned stop button
  answer_index: 2
  explanation: Before maintenance, you must physically disconnect the 3 power adapters
    and verify that residual voltage of each branch is less than 1 V using a multimeter.
- question: Which power rail should be used for FSR force sensor ADC circuit?
  choices:
  - 12 V actuator rail
  - 5 V power rail
  - 3.3 V sensor rail
  - 24 V power rail
  answer_index: 2
  explanation: To protect OpenCR's ADC circuit, the 3.3 V sensor rail must be used
    [S13].
completion_criteria:
- Configuration of 3 independent branch harness and fuse installation completed
- Voltage measured as 12 V at no-load per branch
- Recorded that residual voltage of all measurement nodes is less than 1 V after physical
  power disconnection
- Submission and passing of wiring safety design report
source_ids:
- S14
- S24
- S25
- S7
- S15
- S11
- S13
- S26
---

## Principles of Safe Wiring and Power Isolation

The 5-finger robotic hand system uses multiple high-torque actuators, so efficient and safe power distribution is essential. This project uses 11 power adapters to separately arrange actuators in units of 4/4/3, which distributes current load per branch and increases power stability [S15].

### 1. Ensuring Power Independence
The positive (+) output of each adapter must be maintained as an independent branch, and the act of arbitrarily joining or bundling them is strictly prohibited. Design to accommodate peak current (2.3 A per 1 XM430-W350-T actuator) within the rated output current (11.5 A) of the adapters specified in [S15] [S11]. The sum of peak currents for units of 4 branches is 9.2 A, which is within the allowable continuous output range of the adapters.

### 2. Overcurrent Protection (Protection Coordination)
Place an 10 A ATOF fuse per branch to protect the system from overcurrent in case of wiring or actuator error [S25]. Comparing fuse and load/power ratings alone does not guarantee safety or operating sequences. Review the fuse manufacturer's time-current curves and power supply OCP characteristics together to verify protection coordination. However, fuse selection must refer to the 'Time-Current Curve' provided by the manufacturer; low load current does not guarantee safety [S25].

### 3. Control Circuit Isolation
We increase reproducibility by eliminating complex external bridge circuits using an OpenCR control board with a built-in DYNAMIXEL port [S13]. FSR force sensors use a divider circuit supplied from the 3.3 V sensor rail to convert voltage for ADC input and must be electrically isolated from the 12 V actuator power [S13].

### 4. Work Safety Rules
Since the bench prototype is not a certified machine safety system, you must physically disconnect the 3 power adapters before maintenance or modification, and measure and verify that residual voltage of each branch is less than 1 V using the multimeter DC voltage mode [S7].
