---
layout: learn-module
title: 固件开发与控制
course_slug: precise-robot-hand
course_data_key: precise-robot-hand-zh-cn
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
translation_run_id: e8f8435646734ebd8e061d010c356c2d
primary_category: robotics-hardware
topics:
- robot-hands
- tendon-drive
- embedded-control
course_type: build_project
published_at: '2026-08-29T08:34:02+09:00'
id: M7
slug: firmware-development
phase_id: P3
estimated_hours: 15.0
prerequisites:
- M6
objectives:
- 理解 DYNAMIXEL 智能执行器通信及控制框架。
- 实现利用 OpenCR 控制板进行执行器及 FSR 传感器信号获取。
- 设计实时机器人控制状态机及闭环反馈回路。
- 编程安全电源管理及转矩释放序列。
worked_examples:
- 1. 执行器目标位置/电流设定：使用 DYNAMIXEL SDK 设定 XM430 执行器的电流限制(Goal Current)，并通过传感器反馈值的 PID
  回路更新手指关节最终位置的示例。
- 2. FSR 电压数据滤波：为去除 ADC 采集的原始数据噪声，应用移动平均滤波(Moving Average Filter)，并实现归一化上限(20N)与下限(0.2N)范围的代码
  [S12]。
lab:
  title: 机器人手集成控制与精密抓取实习
  steps:
  - 用万用表 DC 模式确认各独立分支电压低于 1V 后，开始组装。
  - 在 OpenCR 的 3.3V 传感器导轨焊接 FSR 分压电路并连接至 ADC 端口。
  - 使用 DYNAMIXEL SDK 扫描 11 个执行器 ID 并设定初始位置。
  - 空载状态测试手指关节驱动指令，调节肌腱伸长率与张力。
  - 在串口监视器可视化 FSR 传感器数据，调优抓取力响应。
  safety:
  - 绝不可将 5V 或 12V 执行器电源用作 FSR 传感器电路的供给电源。
  - 系统通电期间绝不可接近手指活动范围，应使用固定夹具。
  - 绝不可将电源分支适配器的正(+)端子相互连接。
  - 维护与组装接近前，必须物理断开 3 个电源适配器，并计量确认所有分支低于 1V。
  deliverables:
  - 包含实时传感器数据反馈的固件源代码
  - 电压分压数据的归一化及校准数据手册
  - 执行器反馈回路正常工作日志
assignment:
  title: 抓取状态机设计与实现
  deliverables:
  - 抓取及释放状态机流程图
  - 基于电流的力矩控制实现代码
  - 最终性能评估报告
  rubric:
  - 根据传感器值进行的电流限制范围(0-2.3A)控制是否稳定？
  - 当发出力矩解除指令时，物理张力是否立即消失？
  - 代码中是否明确了安全的硬件分离流程？
quiz:
- question: 配置 FSR 402 传感器和分压电路时，推荐的电源轨是什么？
  choices:
  - 12V 执行器电源轨
  - 5V 通用电源轨
  - OpenCR 3.3V 传感器轨
  - 24V 外部输入轨
  answer_index: 2
  explanation: 为确保系统安全和保护 OpenCR ADC，FSR 分压电路必须连接到 3.3V 传感器电源轨。
- question: 维护机械手时，确认系统处于“无源状态”的正确方法是什么？
  choices:
  - 通过软件发送力矩解除指令。
  - 使用万用表的电阻档检查布线状态。
  - 使用万用表直流电压档测量所有分支电压是否低于 1V。
  - 拆除电源分支保险丝。
  answer_index: 2
  explanation: 物理断电后，必须使用万用表直流电压档直接确认所有分支的残余电压低于 1V。
- question: 可以将多个独立电源适配器的正极(+)端并联连接吗？
  choices:
  - 为了电流求和是必要的。
  - 绝对禁止。
  - 若额定输出电流相同则可以。
  - 安装保险丝后可以。
  answer_index: 1
  explanation: 独立分支配置的电源适配器的正极(+)输出绝对不能相互连接或合并。
completion_criteria:
- 使用万用表验证各分支独立供电及保险丝保护均已按 BOM 规范配置完毕
- 确认通过 OpenCR ADC 精确获取 5 个 FSR 传感器的力信号及滤波效果
- 完整执行软件力矩解除例程及物理断电后的测量流程
- 抓取状态机按预期处理执行器和传感器数据，并提交最终报告
source_ids:
- S13
- S11
- S12
---

### 固件架构与 DYNAMIXEL 控制
机器人手的固件在高频循环内获取传感器数据并处理执行器指令。 `OpenCR 1.0` 控制器基于 216MHz ARM Cortex-M7 处理器 [S13]，直接处理 DYNAMIXEL 协议 2.0，无需额外桥接 [S11]，最大限度减小延迟。各执行器支持电流、速度、位置模式，机器人手使用基于电流控制的力矩抓取策略。

### FSR 力反馈系统
FSR 402 传感器具有电阻与施加力成反比的特性 [S12]。使用 OpenCR 的 12 位 ADC [S13]，在 3.3V 传感器导轨上构建 10kΩ 电阻分压电路。分压电压通过 `ADC值 = (V_in * R_fsr) / (R_fsr + R_ref)` 归一化，该值与手指肌腱张力联动，作为抓取力反馈使用。

### 安全控制例程
系统停止为确保安全分为两阶段。软件阶段，释放执行器转矩(Torque Off)，立即移除物理驱动力。维护前，必须物理断开 3 个独立电源适配器，并使用万用表 DC 模式确认所有分支均低于 1V。
