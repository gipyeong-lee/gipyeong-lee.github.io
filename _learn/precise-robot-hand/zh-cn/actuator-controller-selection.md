---
layout: learn-module
title: 执行器及控制器选型
course_slug: precise-robot-hand
course_data_key: precise-robot-hand-zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:precise-robot-hand:actuator-controller-selection
translations:
- lang: ko
  url: /learn/precise-robot-hand/actuator-controller-selection/
- lang: en
  url: /learn/en/precise-robot-hand/actuator-controller-selection/
- lang: ja
  url: /learn/ja/precise-robot-hand/actuator-controller-selection/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/actuator-controller-selection/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/actuator-controller-selection/
module_id: M3
permalink: /learn/zh-cn/precise-robot-hand/actuator-controller-selection/
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
id: M3
slug: actuator-controller-selection
phase_id: P1
estimated_hours: 10.0
prerequisites:
- M2
objectives:
- 理解 DYNAMIXEL XM430-W350-T 执行器的额定电压、电流及通信特性。
- 熟悉 OpenCR 1.0 控制器的 DYNAMIXEL 端口配置及 12V 电源分离结构。
- 设计利用 FSR 402 传感器和 10kΩ 电阻的分压电路。
- 计算系统功率需求并制定独立分支保险丝保护设计。
worked_examples:
- '示例 1: 确认各分支最大电流。若在一个分支上连接 4 个 XM430 执行器，失速电流合计为 4 * 2.3A = 9.2A。该值满足适配器的 11.5A
  额定值及在线保险丝的 10A 额定值，并维持在安全范围内 [S11, S15, S25]。'
- '示例 2: FSR 分压电路电压计算。在 3.3V 电源电压下，当 FSR 电阻为 R_fsr 时，ADC 输入电压 V_adc = 3.3 * (10k /
  (10k + R_fsr)) V。根据传感器范围(0.2N~20N)确认电阻变化，进行校准以确保不超过 0~3.3V 范围 [S12, S13, S26]。'
lab:
  title: 电源分支构建及 ADC 传感器接口实习
  steps:
  - 在每个 MEAN WELL 适配器输出端连接 0AFH0001Z 保险丝座并插入 0287010 10A 保险丝。
  - 将万用表设为 DC 电压模式，确认各分支电压是否为稳定的 12V。
  - 在 OpenCR 的 3.3V 传感器导轨上，使用 10kΩ 电阻和 FSR 402 构建分压电路。
  - 在非通电状态下，确认分压电路的输出电压是否在 0~3.3V 范围内。
  safety:
  - 作业开始前，必须物理切断 3 个适配器的 AC 电源，并用万用表确认电压为 0V。
  - 必须时刻佩戴防冲击作业护目镜。
  - 通电期间绝不可修改电路或触碰线路。
  - 明确指出保险丝仅用于过电流切断，并非计划停止手段。
  deliverables:
  - 各分支 12V 输出测量记录表
  - FSR 分压电路组装完成照片
  - 构建的配线图
assignment:
  title: 电源分支及防护设计评审
  deliverables:
  - 机器人手整体电流分支分配表（各分支执行器分配）
  - 证明所选保险丝在保护执行器失速电流的同时未超过适配器容量的计算书
  rubric:
  - 独立保险丝是否准确部署在每个分支上？
  - 执行器分支分配是否符合 4/4/3 的规定？
  - 传感器电源是否从 3.3V 传感器导轨供给，而非 12V？
quiz:
- question: 利用 FSR 402 传感器和 10kΩ 电阻的正确分压电路电源连接是什么？
  choices:
  - 12V 执行器电源
  - OpenCR 3.3V 传感器导轨
  - 5V 通用电源
  - OpenCR 12V 输出
  answer_index: 1
  explanation: OpenCR 的 ADC 输入基准工作电压为 3.3V，因此电压分压电路务必从 3.3V 传感器导轨获取电源 [S13]。
- question: XM430-W350-T 执行器的失速电流值是多少？
  choices:
  - 1.0A
  - 2.3A
  - 4.1A
  - 11.5A
  answer_index: 1
  explanation: 根据数据手册，该执行器的失速电流为 2.3A [S11]。
- question: 在电源分支设计中绝对禁止的行为是？
  choices:
  - 在各适配器输出端安装保险丝
  - 并联适配器的正(+)输出
  - 每个分支使用 10A 保险丝
  - 使用绝缘型适配器
  answer_index: 1
  explanation: 适配器的正(+)输出必须维持为独立分支，严禁并联连接 [B3]。
completion_criteria:
- 实验中已通过万用表验证 3 个独立分支的 12V 电压
- 已确认 FSR 402 传感器分压电路的配线及 ADC 输入电压范围
- 提交电源分支及防护设计报告并获通过
source_ids:
- S4
- S5
- S11
- S13
- S15
- S24
- S25
- S12
- S26
---

### 执行器与控制器系统设计理论

#### 1. 执行器选型与功率特性
为实现机器人手的精密驱动，选用 DYNAMIXEL XM430-W350-T。该执行器在 12V 额定电压下工作，失速(Stall)电流为 2.3A [S11]。整个机器人手由 11 个执行器组成，因此总失速电流合计达到约 25.3A。因此，为了稳定驱动，需要独立的电源供应体系。

#### 2. 控制器架构
OpenCR 1.0 搭载 216MHz ARM Cortex-M7 处理器，适合实时控制 [S13]。该控制器支持物理分离 12V 执行器电源和逻辑/传感器电源的结构。由于 FSR 传感器等模拟输入需在 0~3.3V 范围内处理，因此传感器分压电路必须从 OpenCR 的 3.3V 传感器导轨获取电源 [S13]。

#### 3. 过电流防护与电源分支设计
使用 3 个 138W 输出的 MEAN WELL GST160A12-R7B 适配器 [S15]。每个适配器的额定电流为 11.5A，由此创建 3 个独立的 12V 分支。每个分支串联安装 10A ATOF 保险丝，以在发生过电流时保护电路 [S24, S25]。保险丝设定在低于额定电流 11.5A 的水平，以实现保护协调。

#### 4. 传感器信号获取
FSR 402 具有电阻随压力增加而减小的特性 [S12]。将其与 10kΩ 固定电阻连接成电压分压器，将力变化转换为电压信号输入到 OpenCR 的 12bit ADC 端口 [S12, S13, S26]。
