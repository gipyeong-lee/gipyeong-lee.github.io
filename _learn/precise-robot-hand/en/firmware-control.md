---
layout: learn-module
title: Firmware and Control
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.en
course_locale: en
lang: en
ref: learn:precise-robot-hand:firmware-control
translations:
- lang: ko
  url: /learn/precise-robot-hand/firmware-control/
- lang: en
  url: /learn/en/precise-robot-hand/firmware-control/
- lang: ja
  url: /learn/ja/precise-robot-hand/firmware-control/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/firmware-control/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/firmware-control/
module_id: m7
permalink: /learn/en/precise-robot-hand/firmware-control/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
translation_run_id: c0ec26655d01411d99ed334066b74cb0
id: m7
slug: firmware-control
phase_id: p3
estimated_hours: 10.0
prerequisites:
- m6
objectives:
- Understand the operating principles and control protocols (Protocol 2.0) of DYNAMIXEL
  smart actuators.
- Identify the structure of OpenCR controllers and configure sensor and actuator interfaces.
- Design FSR voltage divider circuits and implement ADC signal processing processes.
- Write grasping and control logic for robotic hands into firmware utilizing State
  Machines.
worked_examples:
- 'Example 1: FSR ADC value normalization. Write code to convert FSR sensor outputs
  (0~4095 (12-bit) range when connected to OpenCR ADC) to a force ratio of 0.0~1.0.
  (Formula: `normalized = adc_value / 4095.0`)'
- 'Example 2: XM430 position control command. Construct a command to move joint 1
  to 2048 (center value) using the DYNAMIXEL SDK. Use a calling scheme such as `packetHandler->write2ByteTxRx(portHandler,
  1, ADDR_GOAL_POSITION, 2048, &error);`.'
lab:
  title: Robotic Hand Firmware Implementation and Sensor Calibration
  steps:
  - Connect the OpenCR 1.0 board to a PC via USB and set up the basic communication
    environment [S16].
  - Solder and connect FSR divider circuits connected to each finger to the OpenCR
    3.3V sensor power rail [S16, S27].
  - Use a multimeter to verify that voltage is within the 0-3.3V range when FSR is
    unloaded and pressurized.
  - Read sensor values from firmware, print to serial monitor, and verify changes
    during physical contact.
  - Connect a single actuator to a fixed jig and test precision movement via control
    code.
  safety:
  - Never connect 5V or 12V actuator power rails directly to ADC sensor circuits [S16].
  - Re-verify wiring diagrams before applying power and confirm short circuits via
    multimeter.
  - Perform initial operation tests in an unloaded actuator state.
  - If abnormal heating, odor, or smoke is detected, do not approach. Evacuate after
    cutting off the supply power of 3 adapter(s) from outside the hazardous zone using
    a pre-designated building distribution board circuit breaker or a certified upstream
    master disconnect. If there is no upstream disconnecting means operable from outside
    the hazardous zone, energizing the system is prohibited. Torque release does not
    replace power disconnection. Maintenance/access shall only be performed after
    a planned shutdown, physical disconnection, and confirmation of zero-energy measurement
    [S17].
  - Physically disconnect 3 power adapters before access, then confirm that the voltage
    of each branch is less than 1V in DC voltage mode.
  deliverables:
  - Sensor data output serial log
  - Operation test and calibration-completed firmware source code
  - ADC normalization formula definition document
assignment:
  title: 5-fingered Robot Hand System Integrated Control Report
  deliverables:
  - State machine design diagram and detailed logic description
  - Integrated control firmware for 11 total actuator(s) and 5 total sensor(s)
  - Motion verification video and gripping force analysis graph
  rubric:
  - Does the state machine safely perform the gripping and release loop?
  - Is sensor data acquired stably without noise?
  - Does the per-power-branch design adhere to the BOM's independent branch principle?
  - Were safety rules (physical power disconnection, etc.) followed and recorded?
quiz:
- question: Which power rail must be used for the FSR voltage divider circuit on the
    OpenCR controller?
  choices:
  - 12V actuator power
  - 3.3V sensor power
  - 5V power
  - USB 5V
  answer_index: 1
  explanation: According to the OpenCR manual and compatibility standards, FSR voltage
    division must use only the 3.3V sensor power rail [S16].
- question: What is the correct power connection method in a situation where there
    are 3 actuator power branch adapter(s)?
  choices:
  - Connect the positive (+) outputs of the 3 adapter(s) in parallel to increase current
    capacity.
  - Configure each adapter as an independent branch and pass through a fuse.
  - Connect all actuators to 1 adapter(s) and keep the others as spares.
  - Combine adapter outputs to boost voltage to 36V for use.
  answer_index: 1
  explanation: Parallel connection of positive (+) outputs is prohibited; each adapter
    must be maintained as an independent branch and protected against overcurrent
    via a fuse [S17].
- question: What is the mandatory step to perform before maintenance or access to
    the robot hand system?
  choices:
  - Issue only the software torque release command.
  - Remove the fuse.
  - Physically disconnect 3 power sources and confirm voltage of each branch is less
    than 1V using a multimeter.
  - Press the Reset button on the controller.
  answer_index: 2
  explanation: Torque release cannot replace power disconnection; you must physically
    disconnect the 3 adapter(s) and confirm via DC voltage measurement.
completion_criteria:
- Integrated control firmware performs the gripping motion of the 5-fingered robot
  hand within a loop.
- All sensors acquire ADC signals normally within the 0-3.3V range.
- All electrical connections meet the independent branch design standard including
  fuses.
- Safety review report includes records of zero-energy measurement verification.
source_ids:
- S16
- S14
- S15
- S27
- S17
---

## DYNAMIXEL Smart Actuator Control
Each joint of the robotic hand is driven using XM430-W350-T actuators [S14]. These actuators provide real-time position, velocity, and current feedback and are controlled via DYNAMIXEL Protocol 2.0 [S14]. The OpenCR 1.0 controller is equipped with a 216MHz ARM Cortex-M7 processor and communicates directly with actuators without a separate communication bridge [S16].

## ADC and Sensor Interface
Fingertip contact force is measured using FSR 402 sensors [S15]. FSR resistance decreases as applied force increases [S15]. OpenCR ADC input resolution is 12 bits [S16], and a voltage divider circuit is configured using the 3.3V sensor power rail [S16, S27].

The 10 kΩ pull-down divider uses $V_{out}=V_{ref}\frac{R_{fixed}}{R_{FSR}+R_{fixed}}$

Here, 10kΩ resistor is used for $R_{fixed}$ [S27]. For safety, all analog signals must be designed not to exceed the 0-3.3V range [S16].

## Firmware Structure
The robotic hand control system is implemented as a state machine of 'Standby', 'Perform Grasp', 'Maintain Grasp', and 'Release'. Firmware periodically polls sensor values within a loop and analyzes actuator current and position data to maintain stable grasping force.
