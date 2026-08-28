---
layout: learn-module
title: 固件开发及控制
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:precise-robot-hand:firmware-development
translations:
- lang: ko
  url: /learn/precise-robot-hand/firmware-development/
- lang: en
  url: /learn/en/precise-robot-hand/firmware-development/
- lang: ja
  url: /learn/ja/precise-robot-hand/firmware-development/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/firmware-development/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/firmware-development/
module_id: M7
permalink: /learn/zh-cn/precise-robot-hand/firmware-development/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: 2b7c146b08954623a88a715bf8cc7d0e
id: M7
slug: firmware-development
phase_id: P3
estimated_hours: 15.0
prerequisites:
- M6
objectives:
- 理解 DYNAMIXEL 智能执行器通信及控制框架。
- 实现利用 OpenCR 控制板执行器及 FSR 传感器信号采集。
- 设计实时机器人控制状态机及闭环反馈回路。
- 进行安全的电源管理及转矩释放序列编程。
worked_examples:
- 1. 执行器目标位置/电流设定：使用 DYNAMIXEL SDK 设置 XM430 执行器的限流 (Goal Current)，并通过传感器值联动 PID 回路更新手指关节最终位置的示例。
- 2. FSR 电压数据滤波：为去除 ADC 采集的原始数据噪声，应用移动平均滤波器 (Moving Average Filter)，并实现归一化上限 (20N)
  和下限 (0.2N) 范围的代码 [S12]。
lab:
  title: 机器人手集成控制及精密抓取实践
  steps:
  - 使用万用表 DC 模式确认各独立分支电压低于 1V 后开始组装。
  - 在 OpenCR 的 3.3V 传感器导轨焊接 FSR 电压分压电路并连接至 ADC 端口。
  - 使用 DYNAMIXEL SDK 扫描 11 个执行器的 ID 并设定初始位置。
  - 在无负载状态测试手指关节驱动指令，调节肌腱延伸率与张力。
  - 可视化 FSR 传感器数据并调试抓取力响应。
  safety:
  - 绝对禁止将 5V 或 12V 执行器电源用作 FSR 传感器电路的供电电源。
  - 系统通电期间绝不接近手指工作范围，使用固定夹具。
  - 绝对禁止将电源分支适配器的正极(+)端相互连接。
  - 维护/组装接近前，务必物理断开 3 个电源适配器，并测量确认所有分支低于 1V。
  deliverables:
  - 包含实时传感器数据反馈的固件源代码
  - 电压分压数据的归一化及校准数据手册
  - 执行器反馈回路正常运作日志
assignment:
  title: 抓取状态机设计及实现
  deliverables:
  - 抓取与释放状态机流程图
  - 实现基于电流的转矩控制代码
  - 最终性能评价报告
  rubric:
  - 根据传感器值的限流范围 (0-2.3A) 是否稳定受控？
  - 当发出转矩释放指令时，物理张力是否立即消除？
  - 代码中是否明确了安全硬件隔离程序？
quiz:
- question: 配置 FSR 402 传感器和分压电路时，推荐的电源轨是什么？
  choices:
  - 12V 执行器电源轨
  - 5V 通用电源轨
  - OpenCR 3.3V 传感器电源轨
  - 24V 外部输入电源轨
  answer_index: 2
  explanation: 为了系统安全和 OpenCR ADC 保护，FSR 分压电路必须连接到 3.3V 传感器电源轨。
- question: 维护机械手时，确认系统处于“无电源状态”的正确方法是什么？
  choices:
  - 通过软件发送转矩释放指令。
  - 用万用表电阻档检查接线状态。
  - 用万用表 DC 电压档测量所有分支是否低于 1V。
  - 拆除电源分支保险丝。
  answer_index: 2
  explanation: 物理断电后，必须务必使用万用表 DC 电压档直接确认所有分支的残留电压是否低于 1V。
- question: 可以将多个独立电源适配器输出的阳极(+)端并联连接吗？
  choices:
  - 为了电流求和是必须的。
  - 绝对禁止。
  - 如果额定输出电流相同，则可以。
  - 如果安装了保险丝，则可以。
  answer_index: 1
  explanation: 由独立分支构成的电源适配器的阳极(+)输出绝对不能相互连接或合并。
completion_criteria:
- 利用万用表验证各分支独立供电及保险丝保护是否按照 BOM 规范配置完成
- 通过 OpenCR ADC 确认 5 个 FSR 传感器的精密力信号获取及滤波
- 完整执行软件转矩释放例程及物理断电后的测量程序
- 抓取状态机按预期处理执行器及传感器数据，并提交最终报告
source_ids:
- S13
- S11
- S12
---

### 固件架构及 DYNAMIXEL 控制
机器人手的固件在高频循环内采集传感器数据并处理执行器指令。`OpenCR 1.0` 控制器基于 216MHz ARM Cortex-M7 处理器 [S13]，无需额外桥接即可处理 DYNAMIXEL 协议 2.0 [S11]，最小化延迟。各执行器支持电流、速度、位置模式，机器人手使用基于电流控制的转矩抓取策略。

### FSR 力反馈系统
FSR 402 传感器具有与施加力成反比的电阻特性 [S12]。使用 OpenCR 的 12 位 ADC [S13]，在 3.3V 传感器导轨上构成 10kΩ 电阻与电压分压电路。分压后的电压通过 `ADC值 = (V_in * R_fsr) / (R_fsr + R_ref)` 归一化，该值与手指的肌腱张力联动，作为抓取力反馈使用。

### 安全控制例程
系统停止为安全起见分为两阶段。在软件阶段，转矩释放 (Torque Off) 立即移除物理驱动力。维护前必须物理断开 3 个独立电源适配器，并使用万用表 DC 模式确认所有分支低于 1V。
