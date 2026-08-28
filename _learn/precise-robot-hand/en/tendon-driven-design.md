---
layout: learn-module
title: Tendon-Driven Mechanism Design
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.en
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
translation_run_id: a92b78cca3164206863047b59d2f6ac9
id: M2
slug: tendon-driven-design
phase_id: P1
estimated_hours: 10.0
prerequisites:
- M1
objectives:
- Understand the basic mechanical structure and joint mimicry principles of tendon-driven
  mechanisms.
- Learn the characteristics of tendon materials (Dyneema SK78) for sophisticated robotic
  hands.
- Learn tendon tension transmission paths and methods to prevent friction and wear
  in capstan design.
- Calculate the stall torque of actuators and the mechanical advantage in tendon-driven
  systems.
worked_examples:
- 'Example 1: Tendon tension calculation

  When actuator torque (τ) is 1 N·m and capstan radius (r) is 0.01 m, the tendon tension
  (T) is T = τ/r = 1/0.01 = 100 N. Design considering a safety factor against the
  230 daN (approx. 2300 N) breaking load of Dyneema SK78 [S16].'
- 'Example 2: Power branch distribution and protection

  The sum of stall currents for all 11 actuators is 25.3 A [S11]. Distributing this
  into 3 branches of 4, 4, and 3 units results in maximum loads for each branch of
  9.2 A, 9.2 A, and 6.9 A respectively. Although the theoretical peak of 9.2 A for
  the 4-actuator branch is lower than the 10 A fuse and 11.5 A adapter rating, these
  figures alone do not guarantee safety or operational sequences. Verify protection
  coordination by reviewing fuse manufacturer time-current curves and adapter OCP
  characteristics together [S24, S25].'
lab:
  title: Tendon Tension and Joint Friction Measurement Lab
  steps:
  - Assemble the finger joint model using the provided links and bearings.
  - Connect the tendons and set initial tension using a tensioner.
  - Set the multimeter to DC voltage mode and physically disconnect and verify the
    output of each 12 V power adapter branch.
  - Manually measure and record the rotational friction of the joint before applying
    power.
  safety:
  - Before maintenance/access, physically disconnect the 3 isolated power adapters
    and verify a DC voltage of less than 1 V with a multimeter.
  - Never approach the operating range of the fingers while power is applied.
  - Must wear impact-resistant safety glasses for work.
  deliverables:
  - Tendon tension measurement data according to joint rotation angle
  - Friction analysis report
  - Final safety measurement records
assignment:
  title: 5-Finger Robotic Hand Tendon Path Design
  deliverables:
  - CAD drawings of robotic finger tendon paths
  - Tendon friction and loss calculation sheet
  - Power load distribution and fuse protection design by branch
  rubric:
  - Was the tendon path designed to minimize friction at bends?
  - Were the physical properties of Dyneema SK78 considered?
  - Did the load distribution of the 3 power branches appropriately reflect actuator
    stall currents?
  - Do the fuse and power short-circuit prevention designs comply with BOM specifications?
quiz:
- question: What is the main advantage of using Dyneema SK78 tendons?
  choices:
  - Shock absorption due to high elongation
  - Very low operating elongation and high breaking load
  - Lighter weight than metal and low tensile strength
  - Electrical conductivity
  answer_index: 1
  explanation: Dyneema SK78 is a high-performance fiber with very low elongation of
    less than 1%, increasing position control precision, and a very high breaking
    load [S16].
- question: What is the appropriate reason for using 3 12 V power adapters (11.5 A
    each)?
  choices:
  - To drive all actuators with a single power source
  - To boost voltage to 36 V to increase torque
  - To distribute the total peak current of actuators and protect them with individual
    branch fuses
  - To eliminate power noise
  answer_index: 2
  explanation: It is to safely distribute the peak current of 11 actuators and lower
    the system overcurrent risk by protecting each branch with 10 A fuses [S11, S15,
    S25].
completion_criteria:
- All lab data and drawings must be included in the final report.
- Must demonstrate via measurement that the DC voltage of 3 branches is less than
  1 V after physical power disconnection.
- Analysis considering capstan friction must be included in tendon path design.
source_ids:
- S9
- S10
- S16
- S11
- S15
- S24
- S25
---

## Foundations of Tendon-Driven Mechanisms

Tendon-driven systems are a method of driving joints by transmitting tensile force from remotely located actuators through tendons (cables) [S9]. By mimicking the tendon structure of biological fingers and moving actuators to the palm or forearm, the mass of the fingers themselves can be reduced, enabling sophisticated movements [S10].

### 1. Selection and Tension Transmission of Tendons
This design uses Dyneema SK78, a high-strength, low-stretch fiber [S16]. This material has a breaking load of 230 daN (approx. 230 kgf) at a diameter of 1.5 mm, and is suitable for precision position control with an operating elongation of less than 1% [S16].

### 2. Mechanical Advantage and Actuator Selection
The XM430-W350-T smart actuator provides a stall torque of 4.1 N·m [S11]. Since tendons convert force through the capstan radius at the rotation axis, actuator torque output is replaced by tendon tension. The entire system uses 11 actuators, and the sum of peak currents can reach approximately 25.3 A [S11]. Therefore, to supply this stably, a total of 3 independent 12 V power branches are configured, and each branch prevents overcurrent through an independent 10 A fuse protection [S15, S24, S25].

### 3. Safety and Protection Design
Each 12 V power branch operates via an independent fuse [S15, S24]. The 3 power adapters are each rated at 11.5 A, and their combined current capacity reaches 34.5 A, sufficient to accommodate the system peak current of 25.3 A [S11, S15]. Operational safety is secured by designing the combined branch rating to exceed the total peak current of the actuators.
