---
layout: learn-module
title: 肌腱驱动机制设计
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:precise-robot-hand:tendon-driven-design
translations:
- lang: ko
  url: /learn/precise-robot-hand/tendon-driven-design/
- lang: en
  url: /learn/en/precise-robot-hand/tendon-driven-design/
- lang: ja
  url: /learn/ja/precise-robot-hand/tendon-driven-design/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/tendon-driven-design/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/tendon-driven-design/
module_id: M2
permalink: /learn/zh-cn/precise-robot-hand/tendon-driven-design/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: 2b7c146b08954623a88a715bf8cc7d0e
id: M2
slug: tendon-driven-design
phase_id: P1
estimated_hours: 10.0
prerequisites:
- M1
objectives:
- 理解肌腱驱动机制的基本动力学结构及关节模拟原理。
- 学习用于精密机器人手的肌腱材料 (Dyneema SK78) 的特性。
- 掌握肌腱张力传递路径及卷扬轮设计时的摩擦与磨损防护方法。
- 计算执行器的停转转矩及肌腱驱动时的机械增益。
worked_examples:
- '例题 1：肌腱驱动时的张力计算

  当执行器转矩 (τ) 为 1 N·m 且卷扬轮半径 (r) 为 0.01 m 时，肌腱张力 (T) 为 T = τ/r = 1/0.01 = 100 N。考虑
  Dyneema SK78 断裂载荷 230 daN（约 2300 N）的安全系数进行设计 [S16]。'
- '例题 2：电源分支分配与保护

  执行器总计 11 台的停转电流合计为 25.3 A [S11]。将其分配至 3 个分支（各为 4 台、4 台、3 台），各分支最大负载分别为 9.2 A、9.2
  A、6.9 A。 4 台执行器分支的理论峰值 9.2 A 低于 10 A 熔断器和 11.5 A 适配器额定值，但该数值不能单独保证安全性或动作顺序。应结合熔断器制造商的时间-电流曲线与适配器
  OCP 特性，检查保护配合 [S24, S25]。'
lab:
  title: 肌腱张力及关节摩擦测量实践
  steps:
  - 使用提供的连杆和轴承组装手指关节模型。
  - 连接肌腱并使用张紧器设定初始张力。
  - 将万用表设为直流电压模式，物理断开并检查各分支的 12 V 电源适配器输出。
  - 通电前，手动测量并记录关节的旋转摩擦力。
  safety:
  - 维护/接近前，物理断开 3 个绝缘电源适配器，并使用万用表确认直流电压低于 1 V。
  - 通电期间绝不接近手指的工作范围。
  - 必须佩戴防冲击工作安全护目镜。
  deliverables:
  - 根据关节旋转角度的肌腱张力测量数据
  - 摩擦力分析报告
  - 最终安全测量记录
assignment:
  title: 5 级机器人手肌腱路径设计
  deliverables:
  - 机器人手指肌腱路径CAD图纸
  - 肌腱摩擦及损耗计算书
  - 各分支电源负载分配及熔断器保护设计图
  rubric:
  - 腱路径是否设计为最小化弯曲部分的摩擦？
  - 是否考虑了 Dyneema SK78 的物理特性？
  - 3个电源分支的负载分配是否适当反映了执行器堵转电流？
  - 保险丝及电源短路保护设计是否符合物料清单规范？
quiz:
- question: 使用 Dyneema SK78 肌腱的主要优势是什么？
  choices:
  - 因高延伸率带来的冲击吸收
  - 极低的工作延伸率与高断裂载荷
  - 比金属轻的重量与低拉伸强度
  - 导电性
  answer_index: 1
  explanation: Dyneema SK78 延伸率低于 1%，极低，提高了位置控制精度，是具备高断裂载荷的高性能纤维 [S16]。
- question: 使用 3 个 12 V 电源适配器（各 11.5 A）的原因描述最恰当的是？
  choices:
  - 为了使用一个电源驱动所有执行器
  - 为了将电压增幅至 36 V 以提高转矩
  - 为了分散承载执行器的总峰值电流，并通过独立的熔断器进行保护
  - 为了消除电源噪声
  answer_index: 2
  explanation: 为了安全地分散 11 台执行器的峰值电流，并用 10 A 熔断器保护各分支，降低系统过流风险 [S11, S15, S25]。
completion_criteria:
- 所有实验数据和图纸必须包含在最终报告中。
- 物理断开电源后，需通过测量证实 3 个分支的直流电压低于 1 V。
- 肌腱路径设计中必须包含考虑卷扬轮摩擦的解析。
source_ids:
- S9
- S10
- S16
- S11
- S15
- S24
- S25
---

## 肌腱驱动机制基础

肌腱驱动 (Tendon-driven) 系统是一种通过肌腱（线）将远程执行器的拉力传递给关节的驱动方式 [S9]。模仿生物手指的肌腱结构，将执行器移至手掌或前臂，从而减少手指自身的质量，并实现精密的运动 [S10]。

### 1. 肌腱的选择及张力传递
本设计使用高强度低延伸率纤维 Dyneema SK78 [S16]。该材料在直径为 1.5 mm 时具有 230 daN（约 230 kgf）的断裂载荷，工作延伸率低于 1%，适合精密位置控制 [S16]。

### 2. 机械增益与执行器选择
XM430-W350-T 智能执行器提供 4.1 N·m 的停转转矩 [S11]。由于肌腱通过卷扬轮半径将力从旋转轴转换，执行器的转矩输出会转换为肌腱张力。整个系统使用 11 台执行器，峰值电流总和可达约 25.3 A [S11]。因此，为稳定供电，构成了总共 3 个独立的 12 V 电源分支，每个分支通过独立的 10 A 熔断器保护以防止过流 [S15, S24, S25]。

### 3. 安全与防护设计
各 12 V 电源分支通过独立的熔断器运行 [S15, S24]。 3 个电源适配器额定电流均为 11.5 A，合计电流容量达到 34.5 A，足以承载系统峰值电流 25.3 A [S11, S15]。设计分支合计额定值高于执行器总峰值电流，以确保运行安全性。
