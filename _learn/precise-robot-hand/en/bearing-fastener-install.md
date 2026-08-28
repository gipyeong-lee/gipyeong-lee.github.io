---
layout: learn-module
title: Bearing and Fastening Part Installation
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.en
course_locale: en
lang: en
ref: learn:precise-robot-hand:bearing-fastener-install
translations:
- lang: ko
  url: /learn/precise-robot-hand/bearing-fastener-install/
- lang: en
  url: /learn/en/precise-robot-hand/bearing-fastener-install/
- lang: ja
  url: /learn/ja/precise-robot-hand/bearing-fastener-install/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/bearing-fastener-install/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/bearing-fastener-install/
module_id: M5
permalink: /learn/en/precise-robot-hand/bearing-fastener-install/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: a92b78cca3164206863047b59d2f6ac9
id: M5
slug: bearing-fastener-install
phase_id: P2
estimated_hours: 10.0
prerequisites:
- M4
objectives:
- Understand mechanical tolerances and installation principles of bearings and shafts
  for precision robotic hand production.
- Master methods to secure fastening strength of engineering plastic parts using heat-set
  inserts.
- Minimize assembly clearance using appropriate torque and fastening specifications.
worked_examples:
- 'Example 1: Housing inner diameter check - The outer diameter of the iglide® JSM-0810-10
  bearing is 10 mm. Therefore, the housing bore should be designed to fit 10 mm, and
  if the pilot hole 4.0 mm is not maintained when inserting, the insert may spin loosely
  or the housing may be damaged [S17, S21].'
- 'Example 2: M3 screw assembly - Fasten M3x10 cap screws using a 2.5 mm hex key;
  excessive torque can cause cracks in the resin around the insert, so fix with minimal
  force at the point where it ''no longer turns'' [S20].'
lab:
  title: Robotic Hand Joint Precision Assembly
  steps:
  - 1. Check if the 4.0 mm pilot hole in the PC-CF print housing is clean, and align
    the insert vertically.
  - 2. Heat the soldering iron to an appropriate temperature and slowly press the
    insert vertically to press-fit it parallel to the housing surface.
  - 3. Press-fit the iglide® bearing into the bore, and insert the 8 mm aluminum shaft
    to check clearance and resistance.
  - 4. Complete fastening between links using M3 screws, and move the joint to verify
    that friction is uniform.
  safety:
  - Soldering irons are high temperature; use caution regarding burns and place in
    a stand immediately after heating.
  - Ventilate thoroughly to avoid inhaling micro-dust generated during insert press-fitting.
  - Proceed with work while wearing safety glasses.
  - If abnormal heat, odor, or smoke is detected, do not approach; disconnect the
    power supply of the 3 adapters at a pre-designated building distribution board
    circuit breaker outside the hazard zone or via an authorized upstream master disconnect,
    and evacuate. If no upstream disconnection means capable of operating outside
    the hazard zone is available, do not energize the system. Torque release is not
    a substitute for power disconnection. Maintenance/access should only be performed
    after planned stops, physical disconnection, and verification of a de-energized
    state by measurement.
  deliverables:
  - Friction test logs per joint
  - Photos of insert vertical alignment confirmation
  - Records of degrees of freedom and clearance measurements of assembled links
assignment:
  title: Assembly Tolerance and Fastening Force Analysis Report
  deliverables:
  - Joint assembly order and torque management plan
  - Technical solution for clearance occurrence (use of shims or tolerance modification)
  - Preliminary grasp test data for assembled robotic hand links
  rubric:
  - Was the verticality of insert insertion clearly described?
  - Was the concept of bearing and shaft tolerance correctly explained?
  - Were assembly stage safety rules followed?
quiz:
- question: Why does the inner diameter of an iglide® J bearing adjust after being
    press-fitted into a housing?
  choices:
  - The inner diameter automatically increases due to the elasticity of the bearing
    material.
  - It is designed so that the inner diameter is precisely adjusted to the tolerance
    of the housing bore during the press-fitting process.
  - Because the inner diameter before press-fitting is always manufactured to be smaller
    than the reference value.
  answer_index: 1
  explanation: iglide® sleeve bearings are manufactured larger than the reference
    value before press-fitting and are designed to have an inner diameter within the
    designed tolerance when press-fitted into the correct housing bore [S17].
- question: What is the appropriate pilot hole size when using brass heat-set inserts
    on PC-CF prints?
  choices:
  - 3.5 mm
  - 4.0 mm
  - 4.4 mm
  answer_index: 1
  explanation: According to the datasheet, the recommended pilot hole size for the
    HTBI-M3-BR insert is 4.0 mm [S21].
completion_criteria:
- Confirm that the frictional resistance of 5 assembled finger joints is uniform and
  submit measurement records.
- Visual and dimensional inspection complete to ensure all inserts are level with
  the PC-CF housing.
- Pledge adherence to safety rules during assembly and submit work log.
source_ids:
- S17
- S18
- S20
- S21
---

### Bearing and Shaft Tolerance Management
For smooth movement and rigidity of precision robot joints, iglide® J sleeve bearings (JSM-0810-10) and 8 mm aluminum precision shafts (AWMP-08) are used. Sleeve bearings are designed to adjust their inner diameter when press-fitted into a housing, and compliance with the recommended housing inner diameter tolerance is key [S17, S18]. If clearance occurs, joint precision drops; conversely, if too narrow, friction increases, degrading the current efficiency of the actuator (DYNAMIXEL XM430).

### Heat-Set Insert Installation
PC-CF (carbon-fiber-reinforced PC) prints tend to wear out threads easily when metal screws are directly fastened due to material characteristics. To prevent this, brass heat-set inserts (HTBI-M3-BR) are used [S21]. Inserts are inserted into 4.0 mm pilot holes and fastened by melting surrounding resin with heat, maintaining high mechanical strength even after repeated disassembly and assembly [S21]. Verticality is essential here, as tilting causes misalignment of the assembled links.
