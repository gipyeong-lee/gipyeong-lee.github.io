---
layout: learn-module
title: Actuator and Sensor Integration
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.en
course_locale: en
lang: en
ref: learn:precise-robot-hand:actuators-sensors
translations:
- lang: ko
  url: /learn/precise-robot-hand/actuators-sensors/
- lang: en
  url: /learn/en/precise-robot-hand/actuators-sensors/
- lang: ja
  url: /learn/ja/precise-robot-hand/actuators-sensors/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/actuators-sensors/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/actuators-sensors/
module_id: m5
permalink: /learn/en/precise-robot-hand/actuators-sensors/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
translation_run_id: c0ec26655d01411d99ed334066b74cb0
id: m5
slug: actuators-sensors
phase_id: p2
estimated_hours: 13.0
prerequisites:
- m4
objectives:
- Understand the control signals and power distribution structure of DYNAMIXEL smart
  actuators.
- Identify the operating principle of FSR (Force Sensing Resistor) sensors and design
  voltage divider circuits in OpenCR controllers.
- Acquire the importance of actuator power branches and individual fuse protection.
- Learn the mechanical characteristics of tendon-driven systems and how to link electronic
  control feedback.
worked_examples:
- 'Example 1: Maximum load calculation per actuator branch. If the stall current of
  1 actuators is 2.3 A each [S14], the maximum peak current for the branch with 4
  actuators is 4 * 2.3 A = 9.2 A. This is within the rating of the 10 A fuse [S26],
  and is safe as it does not exceed the 11.5 A adapter output specification [S17].'
- 'Example 2: ADC voltage calculation for FSR divider circuit. When sensor resistance
  is R_fsr and fixed resistor is R_fixed (10 kΩ), ADC input voltage V_adc = 3.3V *
  (R_fixed / (R_fsr + R_fixed)) [S16, S27]. When there is no contact (infinite resistance),
  V_adc is 0 V; when sensor resistance drops below fixed resistance at maximum contact,
  V_adc approaches 3.3 V, digitizing force data.'
lab:
  title: Actuator and FSR Sensor Integration Test
  steps:
  - Connect an ATO in-line fuse holder to the output terminal of each adapter and
    insert 10 A fuse [S25, S26].
  - Connect the DYNAMIXEL actuator harness to the power branch after the fuse [S9].
  - Configure a voltage divider circuit using the FSR sensor and 10 kΩ resistor and
    connect it to the 3.3 V ADC port of OpenCR [S16, S27].
  - Set the multimeter to DC voltage mode and verify that the output voltage of each
    branch is 12 V.
  - Check the communication status by rotating actuators at low speed without load
    via software.
  safety:
  - Before maintenance, physically disconnect 3 power adapters and verify zero-energy
    state by measuring it is less than 1 V.
  - Do not place hands in the actuator operating range while power is applied.
  - Always wear safety glasses when testing circuits.
  - If abnormal heat, odor, or smoke is detected, do not approach; cut power to the
    3 adapter supply from a pre-designated building distribution board circuit breaker
    outside the hazard zone or an authorized upstream master disconnect, then evacuate.
    If there are no operable upstream disconnect means outside the hazard zone, do
    not energize the system. Torque release is not a substitute for power disconnection.
    Perform maintenance/access only after planned stop, physical disconnection, and
    non-powered verification
  deliverables:
  - Calibration log sheets for voltage per branch
  - Pressure-ADC value characteristic curve graphs for FSR sensors
  - Photos and wiring diagrams of robotic hand harness in normal operation state
assignment:
  title: Design of Power System and Implementation of Feedback Logic
  deliverables:
  - Actuator load distribution and fuse protection calculations per branch
  - Grip force control algorithm (pseudocode) using FSR sensor data
  - Final wiring and power integration design report
  rubric:
  - Are the 12 V actuator and 3.3 V sensor rails correctly separated?
  - Does the maximum peak current per branch exceed the fuse rating?
  - Educational prototypes do not claim compliance with machine safety standards or
    certifications; separate review by a qualified safety expert is required before
    deploying in human-accessible environments?
  - Is the physical power disconnection procedure followed in accordance with safety
    guidelines understood?
quiz:
- question: What is appropriate as the supply voltage for the FSR voltage divider
    circuit?
  choices:
  - 12 V actuator power
  - OpenCR 3.3 V sensor power
  answer_index: 1
  explanation: FSR sensor ADC signals must use OpenCR's 3.3 V sensor power, and must
    be electrically completely separated from 12 V actuator power.
- question: What is the main purpose of fuse protection per branch?
  choices:
  - To force fixed voltage at 12 V
  - If abnormal heat, odor, or smoke is detected, do not approach; cut power to the
    3 adapter supply from a pre-designated building distribution board circuit breaker
    outside the hazard zone or an authorized upstream master disconnect, then evacuate.
    If there are no operable upstream disconnect means outside the hazard zone, do
    not energize the system. Torque release is not a substitute for power disconnection.
    Perform maintenance/access only after planned stop, physical disconnection, and
    non-powered verification
  answer_index: 1
  explanation: The 10 A fuse placed in each branch allows actuator peak current while
    protecting the system from overcurrent in case of failure such as wiring shorts.
- question: Can the independent positive (+) outputs of isolated power adapters be
    connected?
  choices:
  - Must be connected to sum branch current
  - Absolutely forbidden; each branch must be maintained independently
  answer_index: 1
  explanation: Parallel connection of positive (+) outputs for isolated branch structures
    is absolutely forbidden, and each output must be operated as a physically separated
    power harness.
completion_criteria:
- Confirmed 12 V voltage is measured normally in each actuator branch.
- Acquired FSR sensor data normally via the controller and demonstrated ADC value
  changes according to contact force changes.
- Physically disconnect system power and can safely perform maintenance access at
  states less than 1 V.
- Submitted all practice assignments and safety compliance pledges.
source_ids:
- S14
- S15
- S16
- S17
- S27
- S26
- S25
- S9
---

If abnormal heat, odor, or smoke is detected, do not approach; cut power to the 3 adapter supply from a pre-designated building distribution board circuit breaker outside the hazard zone or an authorized upstream master disconnect, then evacuate. If there are no operable upstream disconnect means outside the hazard zone, do not energize the system. Torque release is not a substitute for power disconnection. Perform maintenance/access only after planned stop, physical disconnection, and non-powered verification [S14] [S16] [S17] [S15] [S27] [S26]
