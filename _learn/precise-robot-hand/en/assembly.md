---
layout: learn-module
title: Robotic Hand Assembly
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.en
course_locale: en
lang: en
ref: learn:precise-robot-hand:assembly
translations:
- lang: ko
  url: /learn/precise-robot-hand/assembly/
- lang: en
  url: /learn/en/precise-robot-hand/assembly/
- lang: ja
  url: /learn/ja/precise-robot-hand/assembly/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/assembly/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/assembly/
module_id: m6
permalink: /learn/en/precise-robot-hand/assembly/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
translation_run_id: c0ec26655d01411d99ed334066b74cb0
id: m6
slug: assembly
phase_id: p2
estimated_hours: 15.0
prerequisites:
- m5
objectives:
- Understand the precision component fastening principles for robotic hand mechanical
  assembly.
- Identify the tension transmission structure of the tendon (Dyneema) drive system.
- Learn independent power branch configuration and physical wiring safety.
- Acquire correct integration methods for FSR sensors and divider circuits.
worked_examples:
- 'Example 1: Fuse capacity calculation. When connecting 11 XM430 actuators (sum of
  stall current 9.2 A) to 1 12 V branches, using 10 A fuses is appropriate. This is
  a standard specification that accommodates normal operating ranges while protecting
  circuits in case of wiring overloads [S14, S26].'
- 'Example 2: Heat-set insert depth. M3 brass inserts must be heat-inserted accurately
  and vertically into PC-CF prints, requiring a 4 mm pilot hole matched to 4.4 mm
  outer diameter [S23]. Be aware that tilting reduces thread assembly precision.'
lab:
  title: Robotic Hand Mechanical Assembly and Wiring Practice
  steps:
  - Install M3 heat-set inserts into finger links and palm frame.
  - Install igus JSM-0810-10 bearings and 8 mm aluminum shafts onto wrist and joint
    axes.
  - Wind Dyneema tendon around capstan and connect to fingers with appropriate tension.
  - Use Micro-Fit 3.0 connectors to wire each actuator and finger sensor harness [S9].
  - Install 10 A fuse in each independent 12 V branch and verify individual power
    connections [S26, S25].
  safety:
  - Before energizing, always verify the isolation status of 3 power branches with
    a multimeter.
  - Always wear safety glasses during tendon tension testing to prevent whipping if
    the tendon breaks.
  - Before maintenance and component access, physically disconnect 3 power adapters
    and verify by measuring that each branch voltage is less than 1 V.
  - Never connect positive (+) outputs of two or more power adapters in parallel.
  deliverables:
  - Videos confirming friction-free movement per joint
  - Photos of fuse installation per power branch
  - Wiring diagrams and fastening torque records of assembled robotic hand
assignment:
  title: Robotic Hand System Integration Report
  deliverables:
  - Assembled entity 3-plane view and detailed fastening point drawing (CAD)
  - Load distribution table per power branch and fuse capacity verification results
  - Records of tendon tension data during finger flexion
  rubric:
  - Mechanical assembly precision and minimization of bearing friction (40%)
  - Independent power wiring per branch and adherence to safety guidelines (40%)
  - Accuracy of technical specifications in submissions (20%)
quiz:
- question: Which of the following descriptions regarding the power supply method
    is correct?
  choices:
  - Connect positive (+) terminals of 3 power adapters in parallel to increase current
    capacity.
  - Each power adapter is used as an independent branch, and positive (+) terminals
    are electrically isolated.
  answer_index: 1
  explanation: For system safety, each power adapter is used as an independent branch,
    and connecting positive (+) outputs in parallel is absolutely forbidden.
- question: What voltage must be used when connecting the FSR 402 sensor to the OpenCR
    board?
  choices:
  - 3.3 V sensor power rail
  - 12 V actuator power rail
  answer_index: 0
  explanation: The FSR sensor voltage divider circuit must be connected to the 3.3
    V sensor rail to ensure the ADC signal remains within the 0-3.3 V range.
- question: What is the primary reason for using Dyneema SK78 as tendon material?
  choices:
  - Low price and easy machinability
  - High breaking load versus small diameter and very low working stretch
  answer_index: 1
  explanation: Dyneema SK78 provides very high strength and low elongation, suitable
    for precision tension transmission.
completion_criteria:
- Physical assembly of all 5 finger joints complete
- Verification of fuse installation for 3 independent power branches
- After assembly, verification of zero-energy state (less than 1 V) for each of the
  3 branches
source_ids:
- S19
- S20
- S21
- S23
- S18
- S17
- S26
- S15
- S27
- S16
- S14
- S9
- S25
---

### Precision Assembly and Harness System

Robotic hand assembly is a precision process requiring simultaneous securing of mechanical stiffness and electronic reliability. The main structures are manufactured from carbon fiber-filled PC filament (PC-CF) with high stiffness and dimensional stability [S21], and are designed for repetitive disassembly and assembly via M3 brass heat-set inserts [S23].

#### Tendon Drive Principle
Tendons convert the rotational motion of actuators into flexion motion of finger joints. Dyneema SK78 material provides a high breaking load of 230 daN at a diameter of 1.5 mm and low working stretch of less than 1% to maximize tension transmission efficiency [S18]. Rounding of capstan edges during assembly is essential to prevent tendon wear.

#### Independent Power and Safety Branches
This system uses 3 independent 12 V power branches [S17]. Each branch is electrically isolated per adapter, and positive (+) outputs are never connected in parallel. A 10 A ATOF fuse is placed in series in each branch for protection from wiring defects [S26]. This is designed so that the sum of actuator stall currents is safely accommodated.

#### Sensor Interface
The fingertip FSR 402 sensor is a variable resistor whose resistance changes according to pressure [S15]. Educational prototypes do not claim compliance with machine safety standards or certifications; separate review by a qualified safety expert is required before deploying in human-accessible environments [S27] [S16].
