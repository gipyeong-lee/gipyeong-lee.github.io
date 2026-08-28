---
layout: learn-module
title: 固件及控制
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-cn
course_locale: zh-cn
lang: zh-cn
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
permalink: /learn/zh-cn/precise-robot-hand/firmware-control/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
translation_run_id: caccbaa06fab4625ac40bf6e780cd0cb
id: m7
slug: firmware-control
phase_id: p3
estimated_hours: 10.0
prerequisites:
- m6
objectives:
- 理解 DYNAMIXEL 智能执行器的工作原理与控制协议 (Protocol 2.0)。
- 掌握 OpenCR 控制器结构，并配置传感器与执行器接口。
- 设计 FSR 电压分压电路并实现 ADC 信号处理过程。
- 利用状态机 (State Machine) 在固件中编写机器人手的抓取与控制逻辑。
worked_examples:
- 示例 1：FSR ADC 值归一化。若 FSR 传感器连接至 OpenCR ADC 并输出 0~4095 (12 位) 范围的值，编写代码将其转换为 0.0~1.0
  的力比率。（公式：`normalized = adc_value / 4095.0`）
- 示例 2：XM430 位置控制指令。使用 DYNAMIXEL SDK 构建指令，将 1 号关节移动至 2048 (中心值)。使用 `packetHandler->write2ByteTxRx(portHandler,
  1, ADDR_GOAL_POSITION, 2048, &error);` 这样的调用体系。
lab:
  title: 机器人手固件实现及传感器校准
  steps:
  - 将 OpenCR 1.0 板通过 USB 连接至 PC 并设置基础通信环境 [S16]。
  - 将连接到每个手指的FSR分压电路焊接连接到OpenCR的 3.3V 传感器电源轨 [S16, S27]。
  - 使用万用表确认FSR无负载和加压时的电压是否在 0-3.3V 范围内。
  - 在固件中读取传感器值并输出至串口监视器，确认物理接触时的变化。
  - 将单台执行器连接至固定夹具，并通过控制代码测试精密运动。
  safety:
  - 绝对禁止将5V或12V执行器电源轨直接连接到ADC传感器电路 [S16]。
  - 通电前重新确认配线图，并用万用表检查是否短路。
  - 在执行器空载状态下执行初步启动测试。
  - 若检测到异常发热、异味或烟雾，请勿靠近，应在危险区域外通过预设的建筑物配电盘断路器或经认证的 upstream master disconnect 切断 3
    个适配器的供电电源，然后撤离。若危险区域外没有可操作的 upstream 断路手段，则严禁系统通电。扭矩释放不能代替断电。维护与接触操作仅可在计划停机后，经物理隔离并确认处于无电状态后方可进行
    [S17]。
  - 接近前物理断开 3 个电源适配器，然后在直流电压模式下确认各分支电压低于1V。
  deliverables:
  - 传感器数据输出串行日志
  - 完成运行测试及校准的固件源代码
  - ADC 归一化公式定义书
assignment:
  title: 5 指机械手系统集成控制报告
  deliverables:
  - 状态机设计图及逻辑详细技术文档
  - 总计 11 个执行器及 5 个传感器集成控制固件
  - 动作验证视频及抓取力分析图表
  rubric:
  - 状态机是否安全地执行了抓取和释放循环？
  - 传感器数据采集是否稳定且无噪声？
  - 各电源分支设计是否遵循 BOM 的独立分支原则？
  - 是否遵守并记录了安全守则（物理断电等）？
quiz:
- question: 在 OpenCR 控制器中，用于 FSR 分压电路的电源轨应为？
  choices:
  - 12V执行器电源
  - 3.3V 传感器电源
  - 5V电源
  - USB 5V
  answer_index: 1
  explanation: 根据OpenCR手册和兼容性标准，FSR电压分压必须仅使用 3.3V 传感器电源轨 [S16]。
- question: 当执行器电源分支适配器有 3 个时，正确的电源连接方法是？
  choices:
  - 将 3 个适配器的正 (+) 输出并联以增加电流容量。
  - 将每个适配器配置为独立分支并经过保险丝。
  - 将所有执行器连接到 1 个适配器，其余作为备用。
  - 组合适配器输出，升压至36V使用。
  answer_index: 1
  explanation: 严禁并联正 (+) 输出，每个适配器应保持为独立分支，并必须通过保险丝进行过流保护 [S17]。
- question: 在维护或接触机械手系统前必须执行的必要步骤是？
  choices:
  - 仅下达软件扭矩释放指令。
  - 移除保险丝。
  - 物理断开 3 个电源，并用万用表确认各分支电压低于1V。
  - 按下控制器的 Reset 按钮。
  answer_index: 2
  explanation: 扭矩释放不能代替断电，必须物理断开 3 个适配器，并通过直流电压测量进行确认。
completion_criteria:
- 集成控制固件在循环内执行 5 指机械手的抓取动作。
- 所有传感器均能正常采集 0-3.3V 范围内的ADC信号。
- 所有电气连接符合包含保险丝的独立分支设计标准。
- 安全评估报告中包含无电测量确认记录。
source_ids:
- S16
- S14
- S15
- S27
- S17
---

## DYNAMIXEL 智能执行器控制
机械手的每个关节使用XM430-W350-T执行器驱动 [S14]。该执行器实时提供位置、速度、电流反馈，并通过DYNAMIXEL Protocol 2.0 进行控制 [S14]。控制器OpenCR 1.0 搭载216MHz ARM Cortex-M7处理器，无需额外的通信桥接器，直接与执行器通信 [S16]。

## ADC 及传感器接口
指尖的接触力使用FSR 402 传感器测量 [S15]。FSR具有随着施加力增大电阻减小的特性 [S15]。OpenCR的ADC输入分辨率为 12 位 [S16]，使用 3.3V 传感器电源轨构成电压分压电路 [S16, S27]。

10 kΩ 下拉分压器使用 $V_{out}=V_{ref}\frac{R_{fixed}}{R_{FSR}+R_{fixed}}$

此处 $R_{fixed}$ 使用10kΩ电阻 [S27]。为安全起见，所有模拟信号的设计范围必须不超过 0-3.3V [S16]。

## 固件结构
机械手的控制系统由‘待机’、‘执行抓取’、‘保持抓取’、‘释放’的状态机实现。固件在循环中周期性轮询传感器值，分析执行器的电流及位置数据，以保持稳定的抓取力。
