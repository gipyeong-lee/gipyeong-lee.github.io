---
layout: learn-module
title: 执行器与控制器选择
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-cn
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
translation_run_id: 2b7c146b08954623a88a715bf8cc7d0e
id: M3
slug: actuator-controller-selection
phase_id: P1
estimated_hours: 10.0
prerequisites:
- M2
objectives:
- 理解 DYNAMIXEL XM430-W350-T 执行器的额定电压、电流及通信特性。
- 熟知 OpenCR 1.0 控制器的 DYNAMIXEL 端口配置及12V电源分离结构。
- 设计使用 FSR 402 传感器与 10kΩ 电阻的分压电路。
- 计算系统功率要求并建立独立分支熔断器保护设计。
worked_examples:
- 例题 1：确认每分支最大电流。当一个分支连接 4 个 XM430 执行器时，停转电流合计为 4 * 2.3A = 9.2A。这满足适配器 11.5A 额定值及在线熔断器
  10A 额定值，维持在安全范围内 [S11, S15, S25]。
- 例题 2：FSR 分压电路电压计算。在 3.3V 供电电压下，FSR 电阻为 R_fsr 时，ADC 输入电压 V_adc = 3.3 * (10k / (10k
  + R_fsr)) V。根据传感器范围 (0.2N~20N) 确认电阻变化，以确保不超过 0~3.3V 范围 [S12, S13, S26]。
lab:
  title: 电源分支配置及 ADC 传感器接口实践
  steps:
  - 在各 MEAN WELL 适配器输出端连接 0AFH0001Z 熔断器座，并插入 0287010 10A 熔断器。
  - 将万用表设为直流电压模式，确认各分支电压为稳定的 12V。
  - 在 OpenCR 的 3.3V 传感器导轨上，使用 10kΩ 电阻与 FSR 402 构成分压电路。
  - 非通电状态下，确认分压电路输出电压是否在 0~3.3V 范围内。
  safety:
  - 开始作业前，物理断开 3 个适配器的交流电源，并使用万用表确认电压为 0V。
  - 务必始终佩戴防冲击工作安全护目镜。
  - 通电期间绝对禁止更改电路或触摸配线。
  - 说明熔断器用于过流阻断，而非计划停止手段。
  deliverables:
  - 各分支 12V 输出测量记录表
  - FSR 分压电路组装完成照片
  - 配置好的配线图
assignment:
  title: 电源分支及保护设计评审
  deliverables:
  - 整个机器人手电流分配表（各分支执行器分配）
  - 证明所选熔断器既能保护执行器停转电流，又不超过适配器容量的计算书
  rubric:
  - 独立熔断器是否准确布置在各分支？
  - 执行器分支分配是否按照 4/4/3 的规定？
  - 传感器电源是否从非 12V 的 3.3V 传感器导轨供应？
quiz:
- question: 使用 FSR 402 传感器与 10kΩ 电阻的分压电路，正确的电源连接是？
  choices:
  - 12V 执行器电源
  - OpenCR 3.3V 传感器导轨
  - 5V 通用电源
  - OpenCR 12V 输出
  answer_index: 1
  explanation: OpenCR 的 ADC 输入基于 3.3V 运行，因此电压分压电路必须从 3.3V 传感器导轨供电 [S13]。
- question: XM430-W350-T 执行器的停转电流值是？
  choices:
  - 1.0A
  - 2.3A
  - 4.1A
  - 11.5A
  answer_index: 1
  explanation: 根据数据手册，该执行器的停转电流为 2.3A [S11]。
- question: 在电源分支设计中，绝对禁止的行为是？
  choices:
  - 在各适配器输出安装熔断器
  - 将适配器的正极(+)输出并联
  - 每分支使用 10A 熔断器
  - 使用绝缘型适配器
  answer_index: 1
  explanation: 适配器的正极(+)输出必须维持独立分支，绝对禁止并联 [B3]。
completion_criteria:
- 通过实验万用表验证 3 个独立分支的 12V 电压
- 完成 FSR 402 传感器分压电路配线及 ADC 输入电压范围确认
- 提交并通电源分支及保护设计报告
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

### 执行器及控制器系统设计理论

#### 1. 执行器选型及功率特性
为实现机器人手部的精密驱动，使用 DYNAMIXEL XM430-W350-T。该执行器在十二伏额定电压下工作，堵转电流为 2.三安培 [S11]。整个机器人手部由 11 个执行器构成，因此总堵转电流之和约为 25.三安培。因此，为实现稳定驱动，需要独立的电源供应体系。

#### 2. 控制器架构
OpenCR 1.0 搭载二百十六兆赫兹 ARM Cortex-M7 处理器，适用于实时控制 [S13]。该控制器支持将十二伏执行器电源与逻辑/传感器电源在物理上分离的结构。由于 FSR 传感器等模拟输入必须在 0 至 3.三伏范围内处理，传感器分压电路必须从 OpenCR 的 3.三伏传感器轨获取电源 [S13]。

#### 3. 过电流保护及电源分支设计
使用输出功率为一百三十八瓦的 MEAN WELL GST160A12-R7B 适配器 3 个 [S15]。每个适配器的额定电流为 11.五安培，通过此生成 3 个独立的十二伏分支。每个分支均安装十安培 ATOF 保险丝，以便在发生过电流时保护电路 [S24, S25]。保险丝设置得低于额定电流 11.五安培，从而实现保护配合。

#### 4. 传感器信号采集
FSR 402 具有随着压力增加电阻减小的特性 [S12]。将其与十千欧姆固定电阻和分压器连接，将力变化转换为电压信号，并输入到 OpenCR 的十二位模数转换器端口 [S12, S13, S26]。
