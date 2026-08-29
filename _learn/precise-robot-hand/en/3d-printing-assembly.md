---
layout: learn-module
title: 3D Printing and Part Machining
course_slug: precise-robot-hand
course_data_key: precise-robot-hand-en
course_locale: en
lang: en
ref: learn:precise-robot-hand:3d-printing-assembly
translations:
- lang: ko
  url: /learn/precise-robot-hand/3d-printing-assembly/
- lang: en
  url: /learn/en/precise-robot-hand/3d-printing-assembly/
- lang: ja
  url: /learn/ja/precise-robot-hand/3d-printing-assembly/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/3d-printing-assembly/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/3d-printing-assembly/
module_id: M4
permalink: /learn/en/precise-robot-hand/3d-printing-assembly/
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
id: M4
slug: 3d-printing-assembly
phase_id: P2
estimated_hours: 15.0
prerequisites:
- M3
objectives:
- Understand part fabrication using carbon-fiber-reinforced PC filament (PC-CF) and
  optimization of printing settings
- Acquire precision assembly tolerance management for heat-set inserts and sleeve
  bearings
- Understand handling of Dyneema lines and capstan design structure for tendon-driven
  mechanisms
- Master machining and fastening techniques to ensure dimensional stability and rigidity
  of robotic structures
worked_examples:
- 'Example 1: PC-CF filament nozzle selection - Considering the high abrasiveness
  of carbon fiber, confirm that a Brass nozzle must be avoided as it wears quickly,
  causing printing quality degradation and nozzle clogging, and a Hardened steel nozzle
  must be selected [S19].'
- 'Example 2: Insert hole design - Since the outer diameter of the Accu HTBI-M3-BR
  insert is 4.4mm but the official recommended hole diameter is 4.0mm [S21], fix the
  hole diameter to 4.0mm in CAD design so that plastic sufficiently penetrates between
  insert knurling during heat-setting [S21].'
lab:
  title: Finger Structure Fabrication and Assembly Practice
  steps:
  - Configure FDM 3D printing environment for carbon-fiber PC filament with a hardened
    steel nozzle [S19].
  - Remove supports and finish surfaces after printing finger links and palm frame.
  - Vertically seat heat-set inserts into 4.0mm pilot holes using a hot tool [S21].
  - Cut IGUS precision aluminum shafts according to bearing specifications and deburr
    the ends [S18].
  - Press-fit sleeve bearings into housing, insert shafts, and check clearance [S17].
  - Fasten structure and sensor brackets with M3 cap screws [S20].
  safety:
  - Beware of burns from high-temperature nozzles (285°C) and beds (110°C) [S19].
  - Always wear goggles when finishing and deburring prints.
  - Operate ventilation facilities as smoke may be generated during insert heating.
  - Check all mechanical fastening states before applying power.
  deliverables:
  - Fabricated 5-finger robotic hand structure (links, palm).
  - Records of heat-set insert perpendicularity and bearing clearance measurements.
  - Final fastening visual inspection completion report.
assignment:
  title: Robotic Hand Fabrication Precision Verification
  deliverables:
  - Comparison table of CAD data and actual dimensional measurements of completed
    structures
  - Assembly tolerance management plan
  - Manual for friction-reducing design of tendon routing structure
  rubric:
  - Vertical seating of heat-set inserts (High/Medium/Low)
  - Smooth rotational movement after shaft-bearing assembly (Pass/Fail)
  - Compliance with part ratings and model specifications specified in BOM [B10, B11,
    B12, B13, B14]
quiz:
- question: What is the main reason for using a hardened steel nozzle when using PC-CF
    filament?
  choices:
  - Prevent rapid wear of brass nozzles due to carbon fiber abrasiveness
  - Filament melting point is too low for ordinary nozzles
  - Increase surface gloss of prints
  - Increase extrusion speed
  answer_index: 0
  explanation: Carbon fiber is highly abrasive and quickly damages ordinary brass
    nozzles, making a hardened steel nozzle essential [S19].
- question: What is the recommended pilot hole diameter when using M3 heat-set inserts
    (Accu HTBI-M3-BR)?
  choices:
  - 3.0mm
  - 4.0mm
  - 4.4mm
  - 5.0mm
  answer_index: 1
  explanation: The hole diameter recommended by the official datasheet is 4.0mm [S21].
completion_criteria:
- All structural parts fabricated with FDM 3D printer [B10]
- Heat-set inserts seated accurately in all designated holes [B14]
- Assembly clearance of aluminum shaft and sleeve bearing satisfies standard [B11,
  B12]
- M3 spec cap screws correctly used when fastening [B13]
source_ids:
- S19
- S21
- S17
- S18
- S16
- S20
---

### 3D Printing and Part Machining Theory

#### Carbon Fiber Reinforced Engineering Material (PC-CF)
PC (Polycarbonate) has excellent rigidity and heat resistance, and PC-CF filament added with carbon fiber maximizes rigidity, making it suitable for structural parts [S19]. However, due to the abrasiveness of carbon fiber, a hardened steel nozzle must be used [S19], and high-temperature printing of around 285°C is required [S19].

#### Inserts and Fastening for Precision Assembly
Heat-set threaded inserts are used to allow repetitive assembly/disassembly in plastic prints [S21]. For M3 inserts, a 4.0mm diameter pilot hole must be pre-placed in CAD design to ensure accurate seating [S21]. Also, maintenance-free polymer sleeve bearings (iglide J) are designed to have optimal clearance after being press-fitted when assembled with 8mm aluminum shafts [S17], and tolerance management with the 8mm shaft diameter is essential [S17, S18].

#### Tendon Driving Structure
Dyneema SK78 fiber shows a high breaking load of 230 daN and elongation of less than 1% at a 1.5mm diameter [S16], making it an excellent alternative to steel cables. Since the tendon is repeatedly bent at the rotation axis, structural design that rounds capstan corners to prevent breakage due to friction is important.
