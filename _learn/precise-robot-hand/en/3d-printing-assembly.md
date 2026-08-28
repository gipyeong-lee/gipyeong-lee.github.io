---
layout: learn-module
title: 3D Printing and Part Machining
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.en
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
translation_run_id: a92b78cca3164206863047b59d2f6ac9
id: M4
slug: 3d-printing-assembly
phase_id: P2
estimated_hours: 15.0
prerequisites:
- M3
objectives:
- Understand part fabrication and print setting optimization using carbon-fiber-reinforced
  PC filament (PC-CF).
- Master assembly tolerance management for heat-set inserts and sleeve bearings.
- Understand Dyneema line handling and capstan design structures for tendon-driven
  mechanisms.
- Master machining and fastening techniques to secure the dimensional stability and
  rigidity of robot structures.
worked_examples:
- 'Example 1: PC-CF filament nozzle selection - Considering the high abrasiveness
  of carbon fiber, verify that a brass nozzle will wear quickly, causing poor print
  quality and nozzle clogging, and therefore a hardened steel nozzle must be selected
  [S19].'
- 'Example 2: Insert hole design - Since the outer diameter of the Accu HTBI-M3-BR
  insert is 4.4mm but the official recommended hole diameter is 4.0mm [S21], fix the
  hole diameter at 4.0mm in CAD design so that plastic sufficiently penetrates between
  insert knurling during heat-set [S21].'
lab:
  title: Finger Structure Fabrication and Assembly Lab
  steps:
  - Set up FDM 3D printer environment for carbon fiber PC filament with a hardened
    steel nozzle installed [S19].
  - Print finger links and palm frame, remove supports, and finish surfaces.
  - Vertically place heat-set inserts into 4.0mm pilot holes using a hot tool [S21].
  - Cut and chamfer IGUS precision aluminum shafts according to bearing specifications
    [S18].
  - Press-fit sleeve bearings into the housing and insert the shaft to check clearance
    [S17].
  - Fasten structures and sensor brackets with M3 cap screws [S20].
  safety:
  - Caution against burns from high-temperature nozzles (285°C) and beds (110°C) [S19].
  - Must wear safety glasses when post-processing and chamfering prints.
  - Operate ventilation facilities as smoke may be generated during insert heating.
  - Verify all mechanical fastening states before applying power.
  deliverables:
  - Manufactured 5-finger robotic hand structure (links, palm).
  - Heat-set insert perpendicularity and bearing clearance measurement records.
  - Final fastening visual inspection completion report.
assignment:
  title: Robotic Hand Fabrication Precision Verification
  deliverables:
  - Comparison table of actual dimension measurements versus CAD data of finished
    structure
  - Assembly tolerance management plan
  - Explanation of friction-reducing design for tendon routing structure
  rubric:
  - Perpendicularity of heat-set insert (High/Med/Low)
  - Smooth rotational movement after shaft-bearing assembly (Pass/Fail)
  - Compliance with part ratings and model specifications listed in BOM [B10, B11,
    B12, B13, B14]
quiz:
- question: What is the main reason for using a hardened steel nozzle when using PC-CF
    filament?
  choices:
  - To prevent rapid wear of brass nozzles due to carbon fiber abrasiveness
  - Filament melting point is low, so it cannot be printed with standard nozzles
  - To increase the surface gloss of the print
  - To increase extrusion speed
  answer_index: 0
  explanation: Carbon fiber is highly abrasive and will quickly damage standard brass
    nozzles, making a hardened steel nozzle essential [S19].
- question: What is the recommended pilot hole diameter when using an M3 heat-set
    insert (Accu HTBI-M3-BR)?
  choices:
  - 3.0mm
  - 4.0mm
  - 4.4mm
  - 5.0mm
  answer_index: 1
  explanation: The hole diameter recommended in the official datasheet is 4.0mm [S21].
completion_criteria:
- All structural parts successfully fabricated with FDM 3D printer [B10]
- Heat-set inserts accurately seated in all designated holes [B14]
- Clearance between aluminum shaft and sleeve bearing satisfies standard values [B11,
  B12]
- Correct M3 cap screws used as specified for fastening [B13]
source_ids:
- S19
- S21
- S17
- S18
- S16
- S20
---

### 3D Printing and Part Machining Theory

#### Carbon-Fiber-Reinforced Engineering Material (PC-CF)
PC (Polycarbonate) has excellent rigidity and heat resistance, and PC-CF filament reinforced with carbon fiber maximizes rigidity, making it suitable for manufacturing structural parts [S19]. However, due to the abrasiveness of carbon fiber, a hardened steel nozzle must be used [S19], and high-temperature printing around 285°C is required [S19].

#### Inserts and Fastening for Precision Assembly
Heat-set threaded inserts are used to enable repeated assembly/disassembly of plastic prints [S21]. For M3 inserts, a pilot hole with a diameter of 4.0mm must be pre-arranged in CAD design to ensure accurate placement [S21]. Additionally, lubrication-free polymer sleeve bearings (iglide J) are designed to have optimal clearance after press-fitting when assembled with 8mm aluminum shafts [S17], and tolerance management for an 8mm shaft diameter is essential [S17, S18].

#### Tendon-Driven Structure
Dyneema SK78 fiber shows a high breaking load of 230 daN at a 1.5mm diameter and an elongation of less than 1% [S16], making it an excellent replacement for steel cables. Since tendons undergo repeated bending at the axis of rotation, structural design that rounds capstan corners to prevent wire breakage due to friction is important.
