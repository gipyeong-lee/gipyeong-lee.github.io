---
layout: learn-module
title: Introduction to Robotics
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.en
course_locale: en
lang: en
ref: learn:precise-robot-hand:intro-robotics
translations:
- lang: ko
  url: /learn/precise-robot-hand/intro-robotics/
- lang: en
  url: /learn/en/precise-robot-hand/intro-robotics/
- lang: ja
  url: /learn/ja/precise-robot-hand/intro-robotics/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/intro-robotics/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/intro-robotics/
module_id: m1
permalink: /learn/en/precise-robot-hand/intro-robotics/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
translation_run_id: c0ec26655d01411d99ed334066b74cb0
id: m1
slug: intro-robotics
phase_id: p1
estimated_hours: 10.0
prerequisites: []
objectives:
- Understand the definition and system components of robotics.
- Identify the roles of actuators and controllers used in the 5-fingered robotic hand
  prototype.
- Learn the principles of safe power branching configurations and physical isolation
  for robotic systems.
- Learn the operating principle of Force Sensing Resistors (FSR) and methods for ADC
  data acquisition.
worked_examples:
- 'Actuator load calculation: When placing 4 XM430-W350-T actuators on 1 branch, peak
  current is 4 * 2.3 A = 9.2 A [S14]. This is within the rating of the 10 A fuse and
  less than the 11.5 A output rating of the power adapter, enabling stable operation
  [S17, S26].'
- 'FSR voltage divider design: In a divider connecting a sensor and 10 kΩ resistor
  in series, when 3.3 V is input, the ADC outputs a value near 0 V when the sensor
  is in a high-resistance state without pressure, and a value near 3.3 V when resistance
  drops sharply due to strong force [S15, S27].'
lab:
  title: Power Branch Configuration and System Initial Energization Test
  steps:
  - Connect an ATO in-line holder and 10 A fuse to the positive (+) terminal of each
    MEAN WELL adapter to create 3 independent branches [S17, S25, S26].
  - Set the multimeter to DC voltage mode and verify that the output voltage of each
    branch is 12 V.
  - Connect the OpenCR controller to the 3.3 V sensor power rail and configure the
    voltage divider circuit using the FSR sensor and 10 kΩ resistor [S16, S27].
  - After energizing the controller, verify via DYNAMIXEL Wizard that each tendon
    actuator communicates normally [S14, S16].
  safety:
  - Before energizing, re-verify all connections visually and via schematics, not
    the multimeter's resistance mode.
  - Prohibit system access during energization, and always wire in a non-powered state
    (physical adapter disconnection).
  - If abnormal heat, odor, or smoke is detected, do not approach; cut power to the
    3 adapter supply from a pre-designated building distribution board circuit breaker
    outside the hazard zone or an authorized upstream master disconnect, then evacuate.
    If there are no operable upstream disconnect means outside the hazard zone, do
    not energize the system. Torque release is not a substitute for power disconnection.
    Perform maintenance/access only after planned stop, physical disconnection, and
    non-powered verification.
  - Always wear safety glasses and do not place body parts in the operating range.
  deliverables:
  - Photos of 12 V measurement records for each branch
  - OpenCR ADC sensor data acquisition code
  - Wiring diagram for independent branch connections
assignment:
  title: Robotic System Safety Design Report
  deliverables:
  - Independent power branch configuration diagram
  - Fuse rating feasibility analysis against actuator peak current
  - Calculation formula for FSR voltage divider circuit design values
  rubric:
  - Are assignments of 11 actuators and 3 power branches clear?
  - Is the separation of the 3.3 V sensor rail and the 12 V actuator rail correctly
    explained?
  - Is the power-off procedure (physical disconnection) accurately described?
quiz:
- question: Why is it forbidden to connect the positive (+) poles of 12 V output terminals
    in parallel when designing system power?
  choices:
  - Because voltage rises to 24 V
  - Risk of reverse current due to potential difference between adapters and destruction
    of independent branch protection
  - Because actuator communication speed decreases
  - Because software torque release functions cannot be used
  answer_index: 1
  explanation: Each power adapter must operate as an independent branch; combining
    output terminals risks failure and nullification of safety protection features
    by independent fuses.
- question: What is the appropriate supply voltage when reading FSR signals with an
    OpenCR ADC port?
  choices:
  - 12 V actuator rail
  - 3.3 V sensor rail
  - 24 V input power
  - Non-contact wireless power
  answer_index: 1
  explanation: OpenCR ADC uses an 0~3.3 V range, and for sensor protection, it must
    be supplied from the dedicated 3.3 V sensor rail.
- question: What is the safest way to disconnect power for system inspection and maintenance?
  choices:
  - Software command to release actuator torque
  - Remove fuses
  - Physically disconnect 3 power adapters and measure voltage
  - Turn off the controller power switch only
  answer_index: 2
  explanation: Software commands or fuses do not guarantee a perfect zero-energy state.
    You must physically disconnect the adapters and measure that it is less than 1
    V with a multimeter.
completion_criteria:
- Verified 12 V voltage for each branch with a multimeter and submitted photos.
- Verified ADC value changes according to FSR sensor contact force via the controller
  and acquired valid values.
- Understood and followed safety stop procedures through physical power disconnection
  and voltage measurement.
source_ids:
- S1
- S14
- S16
- S17
- S25
- S26
- S15
- S27
---

## Robotic System Components
A robot consists of three core elements: Sensing, Thinking (Controller), and Acting (Actuator) [S1]. The 5-fingered robotic hand in this course uses DYNAMIXEL XM430-W350-T actuators to control joints via a tendon-driven method [S14], and processes signals from these actuators and fingertip FSR sensors through an OpenCR 1.0 controller [S16].

## Safe Power System Design
Since actuators require a stall current of 2.3 A at 12 V [S14], 3 MEAN WELL GST160A12-R7B adapters are used considering total system load [S17]. Each adapter operates on an independent 12 V branch handling 4/4/3 actuators, and the positive (+) outputs of these branches must not be combined and must be physically isolated. Install 10 A ATOF fuses in each branch via in-line holders (0AFH0001Z) to protect wiring during overcurrent events [S25, S26]. This is the foundation of electrical safety beyond simple stop functions.

## Sensor Interface
FSR 402 sensors have the characteristic that resistance decreases according to contact force [S15]. Configure this as a voltage divider circuit with a 10 kΩ resistor and connect it to an OpenCR 12-bit ADC port to convert contact force into voltage [S16, S27]. Sensor circuits must be supplied only from the 3.3 V sensor power rail and must not be mixed with the 12 V rail for actuators.
