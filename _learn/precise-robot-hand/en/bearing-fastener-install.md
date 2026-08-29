---
layout: learn-module
title: Bearing and Fastening Part Installation
course_slug: precise-robot-hand
course_data_key: precise-robot-hand-en
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
translation_run_id: 0886d1415b8d413b8654c2195ac9ac00
primary_category: robotics-hardware
topics:
- robot-hands
- tendon-drive
- embedded-control
course_type: build_project
published_at: '2026-08-29T08:34:02+09:00'
id: M5
slug: bearing-fastener-install
phase_id: P2
estimated_hours: 10.0
prerequisites:
- M4
objectives:
- Understand mechanical tolerances and installation principles of bearings and shafts
  for precision robotic hand fabrication.
- Master methods to secure fastening strength of engineering plastic parts using heat-set
  inserts.
- Minimize assembly clearance using appropriate torque and fastening specifications.
worked_examples:
- 'Example 1: Housing inner diameter check - The outer diameter of iglide® JSM-0810-10
  bearing is 10 mm. Therefore, the housing bore must be designed to 10 mm, and if
  the pilot hole 4.0 mm is not maintained during insert insertion, the insert may
  spin or the housing may be damaged [S17, S21].'
- 'Example 2: M3 screw assembly - M3x10 cap screws are fastened using a 2.5 mm hex
  wrench, and since excessive torque can cause cracks in the resin around the insert,
  fix it with minimum force at the ''point where it no longer turns'' [S20].'
lab:
  title: Robotic Hand Joint Precision Assembly
  steps:
  - 1. Verify the 4.0 mm pilot hole in the PC-CF print housing is clean and align
    the insert vertically.
  - 2. Heat the soldering iron to an appropriate temperature and slowly press the
    insert vertically to press-fit parallel to the housing surface.
  - 3. Press-fit iglide® bearing into the bore, insert 8 mm aluminum shaft, and check
    clearance and resistance.
  - 4. Complete fastening between links using M3 screws and verify that friction is
    uniform by moving the joint.
  safety:
  - Soldering iron is high temperature, so beware of burns and place on stand immediately
    after heating.
  - Ventilate thoroughly so as not to inhale fine dust generated during insert press-fitting.
  - Proceed with work while wearing goggles.
  - In case of abnormal heat, odor, or smoke, do not approach; cut power supply to
    the 3 adapters via a pre-designated building panel breaker outside the hazard
    zone or a certified upstream master disconnect and evacuate. If no upstream disconnect
    is available outside the hazard zone, do not energize the system. Torque release
    is not a substitute for power disconnection. Maintenance/access must only be performed
    after planned stops, physical disconnection, and verifying the de-energized state
    by measurement
  deliverables:
  - Friction test logs per joint
  - Photos verifying vertical alignment of inserts
  - Records of degrees of freedom and clearance of assembled links
assignment:
  title: Assembly Tolerance and Fastening Force Analysis Report
  deliverables:
  - Joint assembly sequence and torque management plan
  - Techniques for solving clearance issues (using shims or modifying tolerances)
  - Preliminary grip test data for assembled robotic hand links
  rubric:
  - Is the verticality of insert insertion clearly described?
  - Did you correctly explain the concept of bearing and shaft tolerance?
  - Were safety rules followed during the assembly phase?
quiz:
- question: Why does the inner diameter of an iglide® J bearing adjust after being
    press-fitted into a housing?
  choices:
  - Inner diameter automatically increases due to elasticity of bearing material during
    press-fit.
  - It is designed so the bearing inner diameter is precisely adjusted to the tolerance
    of the housing bore during the press-fit process.
  - The inner diameter before press-fit is always manufactured smaller than standard.
  answer_index: 1
  explanation: iglide® sleeve bearings are manufactured larger than standard before
    press-fitting and are designed to have an inner diameter within the designed tolerance
    when press-fitted into the correct housing bore [S17].
- question: What is the appropriate pilot hole size when using brass heat-set inserts
    in PC-CF prints?
  choices:
  - 3.5 mm
  - 4.0 mm
  - 4.4 mm
  answer_index: 1
  explanation: According to the datasheet, the recommended pilot hole size for HTBI-M3-BR
    inserts is 4.0 mm [S21].
completion_criteria:
- Verify uniform friction resistance of 5 assembled finger joints and submit measurement
  records.
- Visual and dimensional inspection to ensure all inserts are flush with the PC-CF
  housing.
- Pledge to follow safety rules during assembly and submit work log.
source_ids:
- S17
- S18
- S20
- S21
---

### Tolerance Management of Bearings and Shafts
For smooth movement and rigidity of precision robotic joints, we use iglide® J sleeve bearings (JSM-0810-10) and 8 mm aluminum precision shafts (AWMP-08). Sleeve bearings are designed to adjust their inner diameter when press-fitted into housings, and complying with the recommended housing inner diameter tolerance is key [S17, S18]. If clearance occurs, joint precision drops; if too narrow, friction increases, reducing the current efficiency of the actuator (DYNAMIXEL XM430).

### Heat-set Insert Installation
PC-CF (carbon fiber reinforced PC) prints are prone to thread wear due to material characteristics when metal screws are directly fastened. To prevent this, brass heat-set inserts (HTBI-M3-BR) are used [S21]. Inserts are inserted into 4.0 mm pilot holes and heated to melt surrounding resin for fastening, maintaining high mechanical strength even after repetitive disassembly/reassembly [S21]. If the insert tilts, the alignment of the assembled link becomes misaligned, so maintaining perpendicularity is essential.
