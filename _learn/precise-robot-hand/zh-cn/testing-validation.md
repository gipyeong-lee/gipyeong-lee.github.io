---
layout: learn-module
title: 性能测试与验证
course_slug: precise-robot-hand
course_data_key: precise-robot-hand-zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:precise-robot-hand:testing-validation
translations:
- lang: ko
  url: /learn/precise-robot-hand/testing-validation/
- lang: en
  url: /learn/en/precise-robot-hand/testing-validation/
- lang: ja
  url: /learn/ja/precise-robot-hand/testing-validation/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/testing-validation/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/testing-validation/
module_id: M9
permalink: /learn/zh-cn/precise-robot-hand/testing-validation/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: e8f8435646734ebd8e061d010c356c2d
id: M9
slug: testing-validation
phase_id: P3
estimated_hours: 10.0
prerequisites:
- M8
objectives:
- 设计用于验证机械手精度及重复性的定量测试指标
- 评估利用 FSR 传感器数据的抓取力控制算法稳定性
- 分析 DYNAMIXEL 执行器反馈数据与实际物理动作之间的误差
- 掌握机械缺陷及肌腱驱动机构的耐久性验证流程
worked_examples:
- '示例 1: 计算 OpenCR ADC 电压。当 FSR 电阻为 10 kΩ，串联电阻为 10 kΩ 时，3.3 V 分压器的输出为 V_out = 3.3
  * (10k / (10k + 10k)) = 1.65 V。这适合于 12 位 ADC 范围 [S13, S26]。'
- '示例 2: 保险丝保护协调。当 4 个执行器处于堵转状态时，电流总和为 9.2 A [S11]。10 A 保险丝的冷电阻为 7.7 mΩ [S25]，因此在正常运行时电压降约为
  0.07 V，可忽略不计。但在过流时，必须参考保险丝制造商的时间-电流曲线以获取准确响应。'
lab:
  title: 机械手集成功能测试
  steps:
  - 在物理分离各电源分支的状态下，用直流电压档测量 3 个适配器的输出，确认其是否为 12 V。
  - 将机械手固定在安全夹具上，连接控制器 (OpenCR) 与 PC，将执行器力矩设为 0 以解除力矩。
  - 手动对各手指的 FSR 传感器施加压力，记录 ADC 数据的变化。
  - 在无负载状态下，重复 5 次各手指的最大活动范围 (ROM) 动作，检查是否存在肌腱干扰。
  - 试验结束后，务必从墙壁插座断开 3 个电源适配器并确认残余电压。
  safety:
  - 必须佩戴护目镜进行试验。
  - 通电期间请勿将手放入活动范围内。
  - 若检测到异常发热、异味或烟雾，请勿靠近。从危险区域外使用指定的楼宇配电盘断路器或经认证的上游主断路器切断 3 个适配器的电源后再撤离。如果没有可在危险区域外操作的上游断路手段，则禁止为系统通电。解除力矩并不能替代断电。维护和靠近操作仅限在计划停机、物理分离并确认无源测量后方可进行。
  - 未测量电压前请勿触摸系统。必须确认直流电压低于 1 V。
  deliverables:
  - 手指抓取力传感器校准记录
  - 重复动作精度测量数据
  - 各电源分支负载电流测量值
assignment:
  title: 机械手性能分析最终报告
  deliverables:
  - 性能测试结果分析报告
  - 基于数据的抓取控制算法代码
  rubric:
  - 传感器数据信噪比 (SNR) 分析的合理性
  - 重复动作测试中精度的量化
  - 关于保护设计（保险丝）是否满足系统保护意图的理论探讨
  - 设计规格与实际成品性能指标的比较
quiz:
- question: 使用 FSR 402 传感器和 OpenCR ADC 构建力测量电路时，正确的是？
  choices:
  - FSR 分压器仅使用 3.3 V 传感器电源，并将模拟输入信号保持在 0~3.3 V 范围内
  - 构建由 FSR 和 10 kΩ 电阻组成的分压器并使用 3.3 V 传感器轨
  - ADC 信号必须始终处于 0~5 V 范围
  - 由于 FSR 电阻恒定，因此无需额外的分压电阻
  answer_index: 1
  explanation: 使用 OpenCR 传感器轨 (3.3 V) 将 ADC 输入限制在 0~3.3 V 范围，并构建分压电路将电阻变化读取为电压变化 [S13,
    S26]。
- question: 管理 DYNAMIXEL XM430-W350-T 执行器 12 V 电源分支的正确方法是什么？
  choices:
  - 将 3 个适配器的正极 (+) 输出汇总以增加功率
  - 为每个适配器安装 10 A 保险丝，并作为独立分支使用
  - 由于电流低于保险丝额定值，可在未经安全验证的情况下使用
  - 电源适配器输出无需保险丝直接并联连接
  answer_index: 1
  explanation: 每个适配器输出必须保持独立，并安装适合独立分支的保险丝以保护过流 [S15]。
- question: 在机械手验证阶段，最重要的安全流程是什么？
  choices:
  - 通过软件解除力矩等同于切断电源
  - 在进行维护操作前，始终用万用表确认直流电压低于 1 V
  - 保险丝作为计划停机装置，只需拔掉保险丝即可
  - 使用连续性 (Continuity) 档确认电源已切断
  answer_index: 1
  explanation: 软件解除不能替代物理断电，物理分离后必须使用直流电压档测量确认无残余能量。
completion_criteria:
- 提交性能测试结果报告并获得 70 分以上
- 在所有实验阶段遵守安全准则，并完成物理断电确认
- 确认实现控制代码中的传感器数据滤波功能
source_ids:
- S1
- S11
- S16
- S12
- S13
- S26
- S15
- S25
---

## 性能测试与验证理论

机械手的性能验证是确认设计规格与实际物理行为一致性的过程 [S1]。主要指标如下。

### 1. 位置与抓取精度
重复性 (Repeatability) 指在执行相同指令时机械手到达位置的误差范围。XM430-W350-T 执行器通过内部编码器提供精确的位置反馈 [S11]，但最终指尖位置会因肌腱的伸长和摩擦产生误差。Dyneema 肌腱伸长率极低（小于 1%），有利于确保重复性 [S16]。

### 2. 力控制与 FSR 传感器信号处理
FSR 402 传感器具有电阻随所受力增大而减小的特性 [S12]。将其与 10 kΩ 电阻构建成分压电路，并通过 OpenCR 的 12 位 ADC 进行测量 [S13, S26]。由于传感器数据噪声较大，需应用移动平均滤波器 (Moving Average Filter) 以形成稳定的抓取力反馈环路。

### 3. 过流保护与电源稳定性
系统使用 3 个独立的 12 V 电源分支 [S15]。每个分支由 10 A ATOF 保险丝保护 [S25]，必须合理分配以使执行器峰值电流总和不超过保护额定值。必须通过制造商提供的保险丝时间-电流曲线验证保护协调性。
