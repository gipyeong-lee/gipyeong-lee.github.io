---
layout: learn-module
title: 执行器及传感器集成
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-cn
course_locale: zh-cn
lang: zh-cn
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
permalink: /learn/zh-cn/precise-robot-hand/actuators-sensors/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
translation_run_id: caccbaa06fab4625ac40bf6e780cd0cb
id: m5
slug: actuators-sensors
phase_id: p2
estimated_hours: 13.0
prerequisites:
- m4
objectives:
- 理解 DYNAMIXEL 智能执行器的控制信号与电源分配结构。
- 掌握 FSR（力感应电阻）传感器的工作原理，并设计 OpenCR 控制器中的分压电路。
- 习得执行器电源分支与个别保险丝保护的重要性。
- 掌握肌腱驱动系统的机构特性与电子控制反馈的联动方法。
worked_examples:
- 示例 1：执行器分支最大负载计算。若 1 台执行器，堵转电流为 2.3 A [S14]，配置有 4 台执行器的分支最大峰值电流为 4 * 2.3 A = 9.2
  A。这在 10 A 保险丝额定范围内 [S26]，且未超过 11.5 A 适配器输出规范，是安全的 [S17]。
- 示例 2：FSR分压电路的ADC电压计算。设传感器电阻为R_fsr，固定电阻为R_fixed(10 kΩ)，则ADC输入电压 V_adc = 3.3V * (R_fixed
  / (R_fsr + R_fixed)) [S16, S27]。无接触力时(电阻无穷大) V_adc 为 0 V，最大接触时若传感器电阻小于固定电阻，V_adc
  趋近于 3.3 V，从而将力数据数字化。
lab:
  title: 执行器及 FSR 传感器集成测试
  steps:
  - 在各适配器输出端连接 ATO 内联保险丝座并插入 10 A 保险丝 [S25, S26]。
  - 将 DYNAMIXEL 执行器线束连接至保险丝后的电源分支 [S9]。
  - 利用 FSR 传感器和 10 kΩ 电阻构成电压分压电路，并连接至 OpenCR 的 3.3 V ADC 端口 [S16, S27]。
  - 设置万用表为 DC 电压模式，确认各分支输出电压为 12 V。
  - 通过软件以低速空载旋转执行器，检查通信状态。
  safety:
  - 维护前物理断开 3 个电源适配器，测量低于 1 V 后确认处于无电状态。
  - 通电期间，不得将手放入执行器活动范围。
  - 电路测试时务必佩戴护目镜。
  - 若发现异常发热、异味或冒烟，请勿接近，并从危险区域外通过预先指定的建筑配电盘断路器或认证的上游主断路器切断 3 个适配器的供电电源后再撤离。若危险区域外无上游断路手段，则禁止系统通电。扭矩释放不能代替电源切断。维护和接近必须在计划停机后通过物理断开并确认无电状态下进行。
  deliverables:
  - 各分支电压校准记录表
  - FSR 传感器压力-ADC 值特性曲线图
  - 正常运行状态下的机器人手线束照片及配线图
assignment:
  title: 电源系统设计与反馈逻辑实现
  deliverables:
  - 执行器分支负荷分配及保险丝保护计算书
  - 利用 FSR 传感器数据的抓取力控制算法（伪代码）
  - 最终配线及电源集成设计报告
  rubric:
  - 12 V 执行器与 3.3 V 传感器轨是否正确分离？
  - 各分支最大峰值电流是否未超过保险丝额定值？
  - 教育原型不主张遵守机器安全标准或认证，在投入人员接近环境前是否需要合格安全专家的单独审查？
  - 是否理解遵循安全守则的电源物理断开程序？
quiz:
- question: 适合 FSR 电压分压电路的电源是？
  choices:
  - 12 V 执行器电源
  - OpenCR 3.3 V 传感器电源
  answer_index: 1
  explanation: FSR 传感器的 ADC 信号必须使用 OpenCR 的 3.3 V 传感器轨，并与 12 V 执行器电源在电气上完全分离。
- question: 分支保险丝保护的主要目的是什么？
  choices:
  - 为了强制固定电压为 12 V
  - 发现异常发热、异味或冒烟时，应通过危险区域外预先指定的建筑配电盘断路器或认证的上游主断路器切断 3 个适配器的供电电源后再撤离。若无上游断路手段，则禁止系统通电。扭矩释放不能代替电源切断。维护必须在物理断开并确认无电后进行
  answer_index: 1
  explanation: 部署在各分支的 10 A 保险丝在允许执行器峰值电流的同时，能在配线短路等故障发生时保护系统免受过电流危害。
- question: 绝缘电源适配器的独立阳极 (+) 输出可以连接吗？
  choices:
  - 为合计分支电流必须连接
  - 严禁连接，各分支必须保持独立
  answer_index: 1
  explanation: 为实现独立分支结构，严禁并联阳极 (+) 输出，各输出必须以物理隔离的电源线束运行。
completion_criteria:
- 确认在各执行器分支正常测量到 12 V 电压。
- 通过控制器正常获取 FSR 传感器数据，并证实随接触力变化的 ADC 值变化。
- 能够物理切断系统电源并在小于 1 V 的状态下安全进行维护接近。
- 提交了所有实践作业及安全合规承诺书。
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

若发现异常发热、异味或冒烟，请勿接近，并从危险区域外通过预先指定的建筑配电盘断路器或认证的上游主断路器切断 3 个适配器的供电电源后再撤离。若危险区域外无上游断路手段，则禁止系统通电。扭矩释放不能代替电源切断。维护和接近必须在计划停机后通过物理断开并确认无电状态下进行 [S14] [S16] [S17] [S15] [S27] [S26]
