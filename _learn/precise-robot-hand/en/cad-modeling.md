---
layout: learn-module
title: 3D CAD Modeling
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.en
course_locale: en
lang: en
ref: learn:precise-robot-hand:cad-modeling
translations:
- lang: ko
  url: /learn/precise-robot-hand/cad-modeling/
- lang: en
  url: /learn/en/precise-robot-hand/cad-modeling/
- lang: ja
  url: /learn/ja/precise-robot-hand/cad-modeling/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/cad-modeling/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/cad-modeling/
module_id: m3
permalink: /learn/en/precise-robot-hand/cad-modeling/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
translation_run_id: c0ec26655d01411d99ed334066b74cb0
id: m3
slug: cad-modeling
phase_id: p1
estimated_hours: 15.0
prerequisites:
- m2
objectives:
- Understand design constraints and manufacturing processes (FDM) for 3D CAD modeling.
- Learn techniques for utilizing PC-CF filament to increase structural stiffness.
- Perform precision assembly design considering heat-set inserts and bearing tolerances.
worked_examples:
- '**Insert hole design**: Since the outer diameter of the M3 insert from Accu-components
  is 4.4mm, model a 4.0mm pilot hole in the print in 3D CAD [S23]. Heating and inserting
  the insert after printing allows the brass material to seat inside the plastic,
  forming a robust M3 female thread.'
- '**Bearing housing tolerance**: When using the igus bearing JSM-0810-10, design
  the 10mm housing bore so that after press-fit, the inner diameter fits tightly with
  the 8mm precision shaft without backlash. If too wide, shaft backlash occurs; if
  too narrow, the bearing is damaged, so adjust tolerances via test prints [S19, S20].'
lab:
  title: Precision Link Design and Assembly Verification
  steps:
  - Design the provided tendon path and joint mechanism in 3D CAD and simulate.
  - Load PC-CF filament into the FDM printer and print specimens using a hardened
    steel nozzle [S21].
  - After verifying the 4mm pilot hole in the print, insert the heat-set insert [S23].
  - Assemble the 8mm aluminum shaft and bearing to verify the rotation degrees of
    freedom of the link and measure backlash [S19, S20].
  - Use a multimeter to verify the fuse holder connection status of the 3 independent
    power branches, and inspect that fuses are normally installed before energization
    [S25, S26].
  safety:
  - Always wear impact-resistant safety glasses.
  - Use caution for burns during heat-set work and work in a well-ventilated area.
  - When energizing, always use a fixing jig and never place hands in rotating areas.
  - When maintaining or accessing the system, always physically disconnect the 3 power
    adapters and verify with a multimeter that it is less than 1V.
  deliverables:
  - Full robotic hand assembly 3D CAD modeling file
  - Design verification report including insert and bearing tolerance adjustments
  - Photos of independent connection status and fuse installation for each power branch
assignment:
  title: Robotic Hand Mechanical Design and Integrated Wiring Plan
  deliverables:
  - Detailed 3D CAD design file including all links and joints
  - BOM and design consistency verification report
  - Wiring diagram including 3 independent branches and fuse placement
  rubric:
  - Does the 3D design comply with additive manufacturing tolerances and brass insert
    specifications (4.4mm OD)?
  - Is the backlash between the bearing housing and shaft appropriate?
  - In the electrical wiring diagram, are the 12V actuator power and sensor circuits
    separated, and is a 10A fuse designed for each branch?
quiz:
- question: What is the most appropriate method if threads are needed in a model printed
    with PC-CF filament?
  choices:
  - Model the threads directly when printing.
  - Heat and insert brass heat-set inserts.
  answer_index: 1
  explanation: Using brass heat-set inserts is recommended for repetitive assembly
    reproducibility rather than modeling threads directly into the PC-CF material
    [S23].
- question: What are the precautions when configuring 3 independent 12V power branches?
  choices:
  - Connect positive (+) adapter outputs in parallel to increase current capacity.
  - Each branch is protected against overcurrent via independent 10A fuses.
  answer_index: 1
  explanation: Parallel connection of adapter positive (+) outputs is forbidden, and
    each branch must be protected by installing an independent fuse [S17, S26].
- question: What voltage source should be used for driving the FSR force sensing sensor?
  choices:
  - OpenCR's 3.3V sensor power rail
  - 12V actuator power rail
  answer_index: 0
  explanation: FSR voltage divider circuits must be supplied from the 3.3V sensor
    power rail and must be separated from actuator power [S16].
completion_criteria:
- 3D CAD design file accurately created according to insert and bearing specifications.
- Confirmed 3 independent power branches and fuse configuration in the wiring diagram.
- Assignments including design and verification report submitted and passed standard
  rubric.
source_ids:
- S12
- S21
- S19
- S20
- S23
- S17
- S26
- S15
- S16
- S27
- S25
---

### 3D CAD Modeling and Design for Manufacturing

Design for Additive Manufacturing (DfAM) considering FDM layered manufacturing characteristics is essential for producing a sophisticated 5-fingered robotic hand. Carbon fiber-containing PC-CF filament is suitable for manufacturing precision links due to its excellent mechanical stiffness and dimensional stability [S21].

#### Key Design Considerations
1. **Tolerance management and bearing installation**: When using 8mm precision aluminum shafts and igus JSM-0810-10 bearings, housing bore tolerances must be reflected in the design. Since bearings are fixed via press-fit, design the bore inner diameter to be slightly smaller than the bearing outer diameter (10mm) to induce robust assembly [S19, S20].
2. **Fastening component design**: PC-CF prints are unsuitable for direct threading. For reproducibility of repetitive disassembly and reassembly, use HTBI-M3-BR brass heat-set threaded inserts. For this, design a 4mm diameter pilot hole [S23].
3. **Structural optimization**: In tendon driving, links can deform due to tension. For joint areas where stress is concentrated, ensure wall thickness, and place the model so that the layer orientation is favorable for tensile strength.

### System Integration and Safety
The electrical system of this project consists of 3 independent 12V power branches. For overcurrent protection during actuator operation, you must install 10A ATOF fuses in each branch, distributing actuators in a 4/4/3 ratio to manage peak current [S17, S26]. When acquiring sensor signals, FSR 402 sensors must generate ADC input values via voltage divider resistors from the 3.3V sensor power rail, and must be completely separated from 12V actuator power [S15, S16, S27].
