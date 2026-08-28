---
layout: learn-module
title: Fundamentals of Electronic Circuits
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.en
course_locale: en
lang: en
ref: learn:precise-robot-hand:electronics-fundamentals
translations:
- lang: ko
  url: /learn/precise-robot-hand/electronics-fundamentals/
- lang: en
  url: /learn/en/precise-robot-hand/electronics-fundamentals/
- lang: ja
  url: /learn/ja/precise-robot-hand/electronics-fundamentals/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/electronics-fundamentals/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/electronics-fundamentals/
module_id: m4
permalink: /learn/en/precise-robot-hand/electronics-fundamentals/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
translation_run_id: c0ec26655d01411d99ed334066b74cb0
id: m4
slug: electronics-fundamentals
phase_id: p2
estimated_hours: 12.0
prerequisites:
- m3
objectives:
- Understanding the electrical characteristics and power systems of DYNAMIXEL smart
  actuators
- Design of voltage divider circuits utilizing FSR 402 sensors and ADC signal acquisition
- Design of fuse-based power branches for system overcurrent protection
- Understanding principles of isolation and physical safety separation of electrical
  circuits
worked_examples:
- 'Example 1: Calculation of branch power current sum. If 4 actuators (each with stall
  current 2.3 A) are assigned to one branch, the theoretical maximum current is 9.2
  A. This is within the rating of the 10 A fuse and does not exceed the adapter''s
  11.5 A output limit, enabling safe operation [S14, S17, S26].'
- 'Example 2: Calculation of FSR divider output. When force is applied to the FSR
  and sensor resistance becomes 10 kΩ, the voltage at the divider node is 3.3 V *
  (10 kΩ / (10 kΩ + 10 kΩ)) = 1.65 V. This is within the valid range of the OpenCR
  12-bit ADC, enabling precise force feedback [S15, S16, S27].'
lab:
  title: Power Branch Configuration and Sensor Input Test
  steps:
  - Install an 0AFH0001Z in-line holder and 10 A ATOF fuse in series on the output
    line of each MEAN WELL adapter [S17, S25, S26].
  - Measure with a multimeter whether the 12 V voltage of each branch is within the
    normal range.
  - Configure a voltage divider circuit on a breadboard using the OpenCR 3.3 V pin,
    10 kΩ resistor, and FSR 402 [S16, S27].
  - Verify that the sensor voltage is within the 0~3.3 V range and observe voltage
    changes when force is applied.
  safety:
  - Before maintenance and access, physically disconnect 3 power adapters and verify
    with a multimeter that the DC voltage of each branch is less than 1 V.
  - Do not energize while configuring circuits. Voltage measurement is performed only
    after all connections are complete and in a fixed jig state.
  - Always wear impact-resistant safety glasses.
  - Never mix actuator power (12 V) and sensor power (3.3 V).
  deliverables:
  - Data sheets for voltage measurement per circuit
  - Force-voltage response curve plots for FSR force sensors
  - Photos of fuse connections per branch for overcurrent protection
assignment:
  title: Design of Power Distribution and Sensor Data Collection
  deliverables:
  - Power allocation plan per actuator branch
  - Wiring diagram including OpenCR ADC circuit
  - Fuse rating selection logic report
  rubric:
  - Combined power branch current complies with each adapter's allowable range
  - FSR circuit is connected only to the 3.3 V sensor rail
  - Fuse ratings appropriate for overcurrent protection were selected
quiz:
- question: Which of the following actions is forbidden when configuring power branches?
  choices:
  - Installing an 10 A fuse in series per branch
  - Connecting the positive (+) terminals of independent adapters in parallel
  - Distributing actuators in a 4:4:3 ratio
  - Connecting FSR sensors to the 3.3 V rail
  answer_index: 1
  explanation: Each adapter output must be used as an independent branch; parallel
    connection between power adapter outputs is forbidden as it can lead to system
    failure and fire risk.
- question: Which of the following is correct regarding precautions when configuring
    an FSR 402 sensor voltage divider circuit?
  choices:
  - Must use the 12 V actuator power rail.
  - Must use 5 V power to increase ADC resolution.
  - Must use OpenCR's 3.3 V sensor power.
  - Connect FSR only, without resistors.
  answer_index: 2
  explanation: FSR sensor voltage signals must not exceed the OpenCR ADC input range
    (0~3.3 V), so 3.3 V sensor power must be used.
completion_criteria:
- Proven physical disconnection of all power branch circuits with voltage less than
  1 V via multimeter
- Fuse installation and 3.3 V power divider circuit configuration complete
- Confirmed normal acquisition of FSR sensor signals in OpenCR ADC within 0~3.3 V
source_ids:
- S6
- S9
- S14
- S17
- S26
- S25
- S15
- S27
- S16
---

If abnormal heat, odor, or smoke is detected, do not approach; cut power to the 3 adapter supply from a pre-designated building distribution board circuit breaker outside the hazard zone or an authorized upstream master disconnect, then evacuate. If there are no operable upstream disconnect means outside the hazard zone, do not energize the system. Torque release is not a substitute for power disconnection. Perform maintenance/access only after planned stop, physical disconnection, and non-powered verification [S14] [S17] [S26, S25] [S26] [S15] [S27] [S16]
