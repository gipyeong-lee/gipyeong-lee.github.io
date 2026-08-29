---
layout: learn-module
title: 肌腱驱动机制设计
course_slug: precise-robot-hand
course_data_key: precise-robot-hand-zh-cn
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
translation_run_id: e8f8435646734ebd8e061d010c356c2d
primary_category: robotics-hardware
topics:
- robot-hands
- tendon-drive
- embedded-control
course_type: build_project
published_at: '2026-08-29T08:34:02+09:00'
id: M2
slug: tendon-driven-design
phase_id: P1
estimated_hours: 10.0
prerequisites:
- M1
objectives:
- 理解肌腱驱动机制的基本动力学结构及关节模仿原理。
- 学习用于精密机器人手的肌腱材料(Dyneema SK78)的特性。
- 掌握肌腱的张力传递路径及绞盘设计时的摩擦与磨损防护方法。
- 计算执行器的失速转矩及肌腱驱动时的机械增益。
worked_examples:
- '示例 1: 肌腱驱动时的张力计算

  当执行器转矩(τ)为 1 N·m 且绞盘半径(r)为 0.01 m 时，肌腱张力(T)为 T = τ/r = 1/0.01 = 100 N。需考虑对比 Dyneema
  SK78 的断裂载荷 230 daN（约 2300 N）的安全系数进行设计 [S16]。'
- '示例 2: 电源分支分配与防护

  总共 11 台执行器的失速电流合计为 25.3 A [S11]。若将其分配给 3 个分支，分别为 4 台、 4 台、 3 台，则各分支最大负载分别为 9.2 A、
  9.2 A、 6.9 A。仅凭保险丝与负载/电源额定的对比并不能保证安全性或动作顺序。需结合保险丝制造商的时间-电流曲线及电源 OCP 特性确认保护协调。结合保险丝制造商的时间-电流曲线及适配器
  OCP 特性确认保护协调 [S24, S25]。'
lab:
  title: 肌腱张力及关节摩擦测量实习
  steps:
  - 使用提供的连杆和轴承组装手指关节模型。
  - 连接肌腱并使用张紧器设置初始张力。
  - 将万用表设为 DC 电压模式，物理断开并确认各分支的 12 V 电源适配器输出。
  - 通电前手动测量并记录关节的旋转摩擦力。
  safety:
  - 维护与接近前，必须物理断开 3 个绝缘电源适配器，并用万用表确认 DC 电压低于 1 V。
  - 通电期间绝不可接近手指的活动范围。
  - 务必佩戴防冲击作业护目镜。
  deliverables:
  - 随关节旋转角度变化的肌腱张力测量数据
  - 摩擦力分析报告
  - 最终安全计量记录
assignment:
  title: 5 仿生机器人手肌腱路径设计
  deliverables:
  - 机器人手指肌腱路径 CAD 图纸
  - 肌腱摩擦及损耗计算书
  - 各分支电源负载分配及保险丝保护设计图
  rubric:
  - 肌腱路径设计是否最大限度减少了弯曲处的摩擦？
  - 是否考虑了 Dyneema SK78 的物理特性？
  - 3 个电源分支的负载分配是否适当反映了执行器失速电流？
  - 保险丝及电源短路防护设计是否遵守了 BOM 规范？
quiz:
- question: 使用 Dyneema SK78 肌腱的主要优点是什么？
  choices:
  - 由于高伸长率带来的冲击吸收
  - 极低的动作伸长率和高断裂载荷
  - 比金属轻的重量和低抗拉强度
  - 导电性
  answer_index: 1
  explanation: Dyneema SK78 的伸长率低于 1%，极低，可提高位置控制精度，且是具有超高断裂载荷的高性能纤维 [S16]。
- question: 使用 3 个 12 V 电源适配器（各 11.5 A）的原因中，最恰当的是？
  choices:
  - 为了用一个电源驱动所有执行器
  - 为了将电压提升至 36 V 以提高转矩
  - 为了分散承载执行器的总峰值电流，并通过个别分支保险丝进行保护
  - 为了消除电源噪声
  answer_index: 2
  explanation: 仅凭保险丝与负载/电源额定的对比并不能保证安全性或动作顺序。需结合保险丝制造商的时间-电流曲线及电源 OCP 特性确认保护协调 [S11,
    S15, S25]。
completion_criteria:
- 所有实验数据和图纸必须包含在最终报告中。
- 物理断开电源后，必须通过计量验证 3 个分支的 DC 电压低于 1 V。
- 肌腱路径设计中必须包含考虑绞盘摩擦的解析。
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

肌腱驱动(Tendon-driven)系统是通过远程执行器将张力通过肌腱（线）传递到关节进行驱动的方式 [S9]。模仿生物手指的肌腱结构，将执行器移至手掌或前臂，从而减轻手指自身的质量并实现精密运动 [S10]。

### 1. 肌腱的选择与张力传递
本设计采用高强度低延伸率纤维 Dyneema SK78 [S16]。该材料在直径 1.5 mm 时具有 230 daN（约 230 kgf）的断裂载荷，工作伸长率小于 1%，适合精密位置控制 [S16]。

### 2. 机械增益与执行器选型
XM430-W350-T 智能执行器提供 4.1 N·m 的失速转矩 [S11]。由于肌腱通过旋转轴的绞盘半径转换力，执行器的转矩输出被转换为肌腱的张力。整个系统使用 11 台执行器，峰值电流合计可达到约 25.3 A [S11]。仅凭保险丝与负载/电源额定的对比并不能保证安全性或动作顺序。需结合保险丝制造商的时间-电流曲线及电源 OCP 特性确认保护协调 [S15, S24, S25]。

### 3. 安全与防护设计
各 12 V 电源分支通过独立保险丝运行 [S15, S24]。 3 个电源适配器额定电流各为 11.5 A，总电流容量达到 34.5 A，足以承载系统峰值电流 25.3 A [S11, S15]。确保分支合计额定值超过执行器总峰值电流，以保证运行安全。
