---
layout: learn-module
title: Wiring and Safe Power Disconnection Construction
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.en
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
translation_run_id: a92b78cca3164206863047b59d2f6ac9
id: M6
slug: wiring-safety-system
phase_id: P2
estimated_hours: 10.0
prerequisites:
- M5
objectives:
- Understand how to configure independent 12 V power branches for actuator driving.
- Learn the role and selection principles of ATOF fuses for overcurrent protection.
- Acquire safe power management and physical disconnection protocols.
- Configure the OpenCR controller and FSR sensor's safe voltage divider circuit.
worked_examples:
- If abnormal heat, odor, or smoke is detected, do not approach; disconnect the power
  supply of the 3 adapters at a pre-designated building distribution board circuit
  breaker outside the hazard zone or via an authorized upstream master disconnect,
  and evacuate. If no upstream disconnection means capable of operating outside the
  hazard zone is available, do not energize the system. Torque release is not a substitute
  for power disconnection. Maintenance/access should only be performed after planned
  stops, physical disconnection, and verification of a de-energized state by measurement
  [S11] [S25]
- 'Example 2: FSR ADC circuit voltage - Connect a 10 kΩ divider resistor and FSR 402
  using the 3.3 V sensor rail of OpenCR [S13, S26]. Sensor signal voltage must be
  within the 0~3.3 V range, and this circuit must be physically/electrically separated
  and protected from the 12 V actuator power circuit.'
lab:
  title: Power Branch Harness Fabrication and Safety Inspection
  steps:
  - Solder an ATO inline fuse holder to each adapter output line and insert a 10 A
    ATOF fuse [S24, S25].
  - Fabricate actuator and sensor connection harnesses using Molex Micro-Fit 3.0 connectors
    [S14].
  - Distribute and wire the OpenCR board and each actuator into 3 branches and connect
    them to each power adapter [S13].
  - Before applying power, check the insulation state of each adapter output terminal
    using a multimeter in resistance mode.
  - After applying power, verify that each branch is 12 V in voltage mode, and always
    remove both 3 adapters when disconnecting.
  safety:
  - Physically disconnect the 3 power adapters before maintenance.
  - Replace parts after confirming that residual voltage is less than 1 V with a multimeter.
  - Do not place hands in the operating range while power is applied.
  - Insulate all connections and wear safety glasses when soldering.
  deliverables:
  - Photos of the manufactured power branch harness
  - Voltage measurement record sheet for each branch
  - Wiring diagram review confirmation
assignment:
  title: Safety Wiring Design Report
  deliverables:
  - Actuator allocation design plan for 3 power branches (4/4/3 units per branch)
  - Overcurrent cutoff calculation sheet per branch (peak current vs. fuse rating)
  - Physically disconnect the 3 power adapters after planned stops, and verify the
    de-energized state of each branch by measurement before maintenance/access.
  rubric:
  - Were the principles of power independence and separation followed?
  - Were the fuse and connector ratings appropriately selected for the load?
  - Do the power disconnection and residual voltage verification protocols follow
    safety guidelines?
quiz:
- question: Is it permissible to connect the 12 V outputs (+) of each power adapter
    in parallel?
  choices:
  - Possible, current supply capacity increases.
  - Impossible, must maintain independent branches.
  - Possible if voltage matches.
  - Possible if fuses are added.
  answer_index: 1
  explanation: Adapter outputs must be maintained independently; parallel connection
    is strictly prohibited [S15].
- question: What is the safety measure that must be prioritized before robotic hand
    maintenance?
  choices:
  - Software torque release
  - Multimeter resistance measurement
  - Physical disconnection of 3 power adapters and residual voltage verification
  - Planned stop button press
  answer_index: 2
  explanation: Before maintenance, you must physically disconnect the 3 power adapters
    and verify with a multimeter that the residual voltage of each branch is less
    than 1 V.
- question: What power rail must be used for the FSR force sensor ADC circuit?
  choices:
  - 12 V actuator rail
  - 5 V power rail
  - 3.3 V sensor rail
  - 24 V power rail
  answer_index: 2
  explanation: To protect the OpenCR ADC circuit, the 3.3 V sensor rail must be used
    [S13].
completion_criteria:
- 3 independent branch harness configuration and fuse installation complete
- Voltage for each branch measured as 12 V when unloaded
- Record that residual voltage at all measurement nodes is less than 1 V after physical
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

## Safe Wiring and Power Disconnection Principles

The 5-finger robotic hand system uses multiple high-torque actuators, so efficient and safe power distribution is essential. This project uses 11 power adapters to separately arrange actuators in units of 4/4/3 to distribute the current load of each branch and improve power stability [S15].

### 1. Securing Power Independence
Positive (+) outputs of each adapter must be maintained as independent branches, and the act of arbitrarily combining or tying them together is strictly prohibited. Design to accommodate actuator peak current (XM430-W350-T 2.3 A per 1 actuator) within the rated output current (11.5 A) of the adapters specified in [S15] [S11]. The sum of peak current for the 4-unit branches is 9.2 A, which is within the continuous output tolerance range of the adapters.

### 2. Overcurrent Protection (Protection Coordination)
Place a 10 A ATOF fuse in each branch to protect the system from overcurrent in case of wiring or actuator errors [S25]. ATOF fuses operate at the 110%~135% level of rated current, enabling stable protection against the peak current of 9.2 A. However, fuse selection must refer to the 'Time-Current Curve' provided by the manufacturer; safety is not guaranteed just because the load current is low [S25].

### 3. Control Circuit Separation
Reproducibility is improved by removing complex external bridge circuits using an OpenCR control board with a built-in DYNAMIXEL port [S13]. FSR force sensors use a divider circuit supplied from the 3.3 V sensor rail to convert voltage for ADC input, and must be electrically separated from the 12 V actuator power [S13].

### 4. Work Safety Rules
Since the bench prototype is not a certified machine safety system, you must physically disconnect the 3 power adapters before maintenance or modification work, and verify with a multimeter in DC voltage mode that the residual voltage of each branch is less than 1 V [S7].
