---
layout: learn-module
title: Robotic Mechanical Design
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.en
course_locale: en
lang: en
ref: learn:precise-robot-hand:mechanism-design
translations:
- lang: ko
  url: /learn/precise-robot-hand/mechanism-design/
- lang: en
  url: /learn/en/precise-robot-hand/mechanism-design/
- lang: ja
  url: /learn/ja/precise-robot-hand/mechanism-design/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/mechanism-design/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/mechanism-design/
module_id: m2
permalink: /learn/en/precise-robot-hand/mechanism-design/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
translation_run_id: c0ec26655d01411d99ed334066b74cb0
id: m2
slug: mechanism-design
phase_id: p1
estimated_hours: 15.0
prerequisites:
- m1
objectives:
- Understand underactuated systems, a core principle of robotic hand design.
- Learn the dynamic characteristics of tendon-driven methods and the importance of
  managing friction and elongation.
- Learn selection and design techniques for engineering materials (PC-CF) considering
  stiffness and dimensional stability.
- Lay the foundation for precision assembly design using heat-set inserts and bearings.
worked_examples:
- 'Example 1: Tendon tension transmission analysis. If the tendon''s working stretch
  is 1%, an error of 1 mm occurs over a 100 mm distance. Closed-loop control utilizing
  the actuator''s current feedback and sensor data is essential for precision control
  [S14].'
- 'Example 2: Insert fastening design. When inserting HTBI-M3-BR inserts into PC-CF
  prints, the recommended pilot hole diameter of 4 mm must be strictly observed during
  CAD design to enable backlash-free assembly [S23].'
lab:
  title: Robotic Joint and Tendon Module Assembly Practice
  steps:
  - Wear safety glasses and clear the workbench.
  - Check the pilot hole status of PC-CF prints and process if necessary.
  - Heat the heat-set inserts with a soldering iron and press them vertically into
    the prints.
  - Install igus bearings into the wrist and joint housings.
  - Pass the aluminum shaft through the bearings to check for backlash.
  - Wind the Dyneema tendon around the capstan and fix it to the assembled joint.
  safety:
  - Be careful of high heat when using a soldering iron, and always wear safety glasses.
  - During tendon tension testing, do not place hands in the operating range to prevent
    snapping accidents if the tendon breaks.
  - After system assembly is complete and before energization, verify the physical
    disconnection state with a measuring instrument.
  deliverables:
  - Assembled robotic joint module
  - Measurement records of bearing and shaft backlash
assignment:
  title: 5-fingered Robotic Hand Mechanical Design Project
  deliverables:
  - Full robotic hand CAD assembly drawing
  - Bill of Materials (BOM) and selection rationale report
  - Tendon path optimization design drawing
  rubric:
  - Do the components used comply with the specification (BOM)?
  - Are the heat-set insert and bearing designs appropriate?
  - Is free movement realized without mechanical interference?
quiz:
- question: What is the primary reason for using Dyneema SK78 in tendon driving?
  choices:
  - High elongation and low price
  - Provides low elongation and high breaking load to enable precision acquisition
  answer_index: 1
  explanation: Dyneema SK78 has a very low elongation of less than 1%, which increases
    the repeatability of robot control [S18].
- question: What is the recommended method for repetitive screw assembly into PC-CF
    prints?
  choices:
  - Direct thread machining into the print
  - Insertion of brass heat-set inserts
  answer_index: 1
  explanation: Heat-set inserts greatly improve thread durability in engineering plastics
    like PC-CF [S23].
completion_criteria:
- Documented each component's specification and BOM compliance
- Verified functional movement of the assembled joint module
- Completed the practice while complying with safety guidelines
source_ids:
- S3
- S11
- S18
- S21
- S23
- S19
- S14
---

## Principles of Robotic Mechanical Design

The core of designing a sophisticated 5-fingered robotic hand lies in implementing an underactuated system that efficiently controls more degrees of freedom (DoF) than actuators [S11]. This enables stable grasping of objects of various shapes without excessively increasing the number of joints [S3].

### Tendon-Driven Dynamics
Tendon driving is a method that transmits the tension of a remote motor to the joint. The physical properties of the tendon determine the precision of control. This course uses `Dyneema SK78` fiber, which withstands a high breaking load of 230 daN at a diameter of 1.5 mm and has a very low working stretch of less than 1%, providing excellent repeatability [S18].

### Material and Structural Design
The frame and links of a robotic hand require high stiffness and dimensional stability. FDM-based `Prusament PC Blend Carbon Fiber` is a PC material containing carbon fiber, providing high-temperature resistance and excellent strength suitable for engineering-grade part production [S21]. For repetitive disassembly and reassembly, M3 brass heat-set inserts (OD 4.4 mm, length 5.8 mm) are used instead of direct screw fastening to ensure thread durability [S23]. Oil-free polymer sleeve bearings (JSM-0810-10) are used on rotation axes to realize smooth rotation and friction management without maintenance [S19].
