---
layout: learn-module
title: Tendon-Driven Mechanism Design
course_slug: precise-robot-hand
course_data_key: precise-robot-hand-en
course_locale: en
lang: en
ref: learn:precise-robot-hand:tendon-driven-design
translations:
- lang: ko
  url: /learn/precise-robot-hand/tendon-driven-design/
- lang: en
  url: /learn/en/precise-robot-hand/tendon-driven-design/
- lang: ja
  url: /learn/ja/precise-robot-hand/tendon-driven-design/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/tendon-driven-design/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/tendon-driven-design/
module_id: M2
permalink: /learn/en/precise-robot-hand/tendon-driven-design/
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
id: M2
slug: tendon-driven-design
phase_id: P1
estimated_hours: 10.0
prerequisites:
- M1
objectives:
- Understand the basic mechanical structure of tendon-driven mechanisms and the principles
  of joint simulation.
- Learn the characteristics of tendon material (Dyneema SK78) for sophisticated robotic
  hands.
- Learn tendon tension transmission paths and methods to prevent friction and wear
  in capstan design.
- Calculate the stall torque of actuators and mechanical gain during tendon driving.
worked_examples:
- 'Example 1: Calculating tendon tension during driving

  When actuator torque (τ) is 1 N·m and capstan radius (r) is 0.01 m, tendon tension
  (T) is T = τ/r = 1/0.01 = 100 N. Design considering the safety factor against Dyneema
  SK78''s breaking load of 230 daN (approx. 2300 N) [S16].'
- 'Example 2: Power branch distribution and protection

  The sum of stall currents for all 11 actuators is 25.3 A [S11]. If distributed into
  3 branches with 4, 4, and 3 units, the maximum load for each branch is 9.2 A, 9.2
  A, and 6.9 A respectively. Comparing fuse and load/power ratings alone does not
  guarantee safety or operating sequences. Review the fuse manufacturer''s time-current
  curves and power supply OCP characteristics together to verify protection coordination.
  Review the fuse manufacturer''s time-current curves and adapter OCP characteristics
  together to verify protection coordination [S24, S25].'
lab:
  title: Tendon Tension and Joint Friction Measurement Practice
  steps:
  - Assemble the finger joint model using the provided links and bearings.
  - Connect the tendons and set initial tension using the tensioner.
  - Set the multimeter to DC voltage mode and physically verify the 12 V power adapter
    output for each branch.
  - Manually measure and record the rotational friction of the joint before energizing.
  safety:
  - Before maintenance/access, physically disconnect the 3 insulated power adapters
    and verify DC voltage of less than 1 V using a multimeter.
  - Never approach the operating range of the fingers while power is applied.
  - Always wear impact-resistant work goggles.
  deliverables:
  - Tendon tension measurement data according to joint rotation angle
  - Friction analysis report
  - Final safety measurement records
assignment:
  title: 5-Finger Robotic Hand Tendon Path Design
  deliverables:
  - CAD drawings of robotic finger tendon paths
  - Tendon friction and loss calculation sheet
  - Branch-specific power load distribution and fuse protection design
  rubric:
  - Is the tendon path designed to minimize friction at bends?
  - Are the physical characteristics of Dyneema SK78 considered?
  - Does the load distribution of the 3 power branches appropriately reflect actuator
    stall current?
  - Do the fuse and power short-circuit protection designs comply with BOM specifications?
quiz:
- question: What is the main advantage of using Dyneema SK78 tendons?
  choices:
  - Shock absorption due to high elongation
  - Very low operating elongation and high breaking load
  - Lighter weight and lower tensile strength than metal
  - Electrical conductivity
  answer_index: 1
  explanation: Dyneema SK78 has very low elongation of less than 1%, improving precision
    of position control, and is a high-performance fiber with a very high breaking
    load [S16].
- question: What is the appropriate reason for using 3 power adapters (11.5 A each)
    with 12 V?
  choices:
  - To drive all actuators with a single power source
  - To boost voltage to 36 V to increase torque
  - To distribute and accommodate total peak current of actuators and protect with
    individual branch fuses
  - To eliminate power noise
  answer_index: 2
  explanation: Comparing fuse and load/power ratings alone does not guarantee safety
    or operating sequences. Review the fuse manufacturer's time-current curves and
    power supply OCP characteristics together to verify protection coordination [S11,
    S15, S25].
completion_criteria:
- All lab data and drawings must be included in the final report.
- Must prove via measurement that the DC voltage of 3 branches is less than 1 V after
  physical power disconnection.
- Tendon path design must include analysis considering capstan friction.
source_ids:
- S9
- S10
- S16
- S11
- S15
- S24
- S25
---

## Fundamentals of Tendon-Driven Mechanisms

A tendon-driven system is a method of driving by transmitting tension from remotely located actuators to joints via tendons (cables) [S9]. By mimicking the tendon structure of biological fingers and moving actuators to the palm or forearm, the mass of the fingers themselves is reduced, enabling sophisticated movements [S10].

### 1. Selection and Tension Transmission of Tendons
Dyneema SK78, a high-strength, low-elongation fiber, is used in this design [S16]. This material has a breaking load of 230 daN (approx. 230 kgf) at a diameter of 1.5 mm, with an operating elongation of less than 1%, making it suitable for precision position control [S16].

### 2. Mechanical Gain and Actuator Selection
The XM430-W350-T smart actuator provides a stall torque of 4.1 N·m [S11]. Since the tendon transforms force through the capstan radius from the axis of rotation, the actuator's torque output is replaced by tendon tension. The entire system uses 11 actuators, and the peak current total can reach approximately 25.3 A [S11]. Comparing fuse and load/power ratings alone does not guarantee safety or operating sequences. Review the fuse manufacturer's time-current curves and power supply OCP characteristics together to verify protection coordination [S15, S24, S25].

### 3. Safety and Protection Design
Each 12 V power branch is operated through an independent fuse [S15, S24]. The 3 power adapters are each rated at 11.5 A, with a combined current capacity reaching 34.5 A, which sufficiently accommodates the system peak current of 25.3 A [S11, S15]. Design such that the sum of branch ratings exceeds the total actuator peak current to ensure operational safety.
