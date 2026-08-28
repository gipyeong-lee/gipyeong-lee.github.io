---
layout: learn-module
title: 性能试验与验证
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-cn
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
translation_run_id: 2b7c146b08954623a88a715bf8cc7d0e
id: M9
slug: testing-validation
phase_id: P3
estimated_hours: 10.0
prerequisites:
- M8
objectives:
- 设计用于验证机械手精度及重复性的定量试验指标
- 评估利用 FSR 传感器数据的抓取力控制算法的稳定性
- 分析 DYNAMIXEL 执行器反馈数据与实际物理动作之间的误差
- 掌握机械缺陷及肌腱驱动机构的耐久性验证程序
worked_examples:
- '示例 1: 计算 OpenCR ADC 电压。当 FSR 电阻为 10 kΩ，串联电阻为 10 kΩ 时，3.3 V 分压器输出为 $V_{out} = 3.3
  * (10k / (10k + 10k)) = 1.65 V。该值适合 12 位 ADC 范围 [S13, S26]。'
- '示例 2: 熔断器保护协调。当 4 台执行器处于锁定 (Stall) 状态时，电流总和为 9.2 A [S11]。 10 A 保险丝的冷电阻为 7.7 mΩ
  [S25]，因此正常运行时的电压降约为 0.07 V，可以忽略，但在过电流情况下，精确响应必须参考保险丝制造商的时间-电流曲线。'
lab:
  title: 机械手集成功能测试
  steps:
  - 在物理分离各电源分支的状态下，利用 DC 电压档测量 3 个适配器的输出，确认是否为 12 V。
  - 将机械手固定在安全夹具上，连接控制器 (OpenCR) 至 PC，将执行器转矩解为 0。
  - 手动对各手指的 FSR 传感器施加压力，记录 ADC 数据变化。
  - 在无负载状态下，对各手指的活动范围 (ROM) 进行 5 次重复动作，确认肌腱是否产生干涉。
  - 试验结束后，务必将 3 个电源适配器从墙壁插座断开，并确认残留电压。
  safety:
  - 务必佩戴护目镜进行试验。
  - 通电期间请勿将手放入活动范围内。
  - 若检测到异常发热、异味或烟雾，请勿靠近，应在危险区域外利用预先指定的楼宇配电盘断路器或经认证的 upstream master disconnect 切断
    3 个适配器的电源后再撤离。若危险区域外无可操作的 upstream 断开手段，则禁止系统通电。转矩释放不能代替断电。仅在计划停机、物理隔离并确认无电源测量后，方可进行维护或接近。
  - 未经电压测量，请勿触摸系统。确认 DC 低于 1 V 是必需的。
  deliverables:
  - 指尖抓取力传感器校准记录
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
  - 关于保护设计 (保险丝) 是否满足系统保护意图的理论考察
  - 设计规范与实际制造产品性能指标的对比
quiz:
- question: 配置利用 FSR 402 传感器和 OpenCR ADC 的力测量电路时，正确的是什么？
  choices:
  - FSR 分压器仅使用 3.3 V 传感器电源，并将模拟输入信号维持在 0~3.3 V 范围内
  - 用 FSR 和 10 kΩ 电阻构建分压器，并使用 3.3 V 传感器轨
  - ADC 信号必须始终处于 0~5 V 范围内
  - FSR 电阻固定，因此不需要额外的分压电阻
  answer_index: 1
  explanation: 应使用 OpenCR 传感器轨 (3.3 V) 将 ADC 输入限制在 0~3.3 V 范围内，并构建分压电路，以读取电阻变化带来的电压变化
    [S13, S26]。
- question: 管理 DYNAMIXEL XM430-W350-T 执行器的 12 V 电源分支的方法，正确的是什么？
  choices:
  - 将 3 个适配器的阳极 (+) 输出捆绑在一起以合并功率
  - 为每个适配器安装 10 A 保险丝，并将其用作单独的独立分支
  - 由于电流低于保险丝额定值，可在未进行安全验证的情况下使用
  - 电源适配器输出应无需保险丝直接并联连接
  answer_index: 1
  explanation: 各适配器输出应保持独立，并安装适合独立分支的保险丝，以防止过电流 [S15]。
- question: 在机械手验证阶段，最重要的安全程序是什么？
  choices:
  - 软件释放转矩与断电相同
  - 始终在万用表确认 DC 低于 1 V 后，方可接近维护
  - 保险丝作为计划停机装置，因此只需拔出保险丝即可
  - 利用连续性 (Continuity) 模式确认电源已切断
  answer_index: 1
  explanation: 软件释放不能替代物理断电，物理分离后利用 DC 电压档确认无残留能量是必需的。
completion_criteria:
- 提交性能测试结果报告并获得 70 分以上
- 在所有实验步骤中遵守安全准则及完成物理断电确认
- 确认控制代码中传感器数据滤波功能的实现
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

## 性能试验与验证理论

机械手的性能验证是确认设计规范与实际物理行为之间一致性的过程 [S1]。主要指标如下：

### 1. 位置及抓取精度
重复性 (Repeatability) 指机械手执行相同指令时到达位置的误差范围。XM430-W350-T 执行器通过内部编码器提供精确的位置反馈 [S11]，但最终指尖的位置会因肌腱的伸长和摩擦而产生误差。Dyneema 肌腱的伸长率极低，低于 1%，有利于确保重复性 [S16]。

### 2. 力控制与 FSR 传感器信号处理
FSR 402 传感器具有电阻随施加力减小的特性 [S12]。通过 10 kΩ 电阻构建分压电路，利用 OpenCR 的 12 位 ADC 进行测量 [S13, S26]。由于传感器数据噪声较大，必须应用移动平均滤波 (Moving Average Filter) 形成稳定的抓取力反馈回路。

### 3. 过流保护与电源稳定性
系统使用 3 个独立的 12 V 电源分支 [S15]。各分支由 10 A ATOF 保险丝保护 [S25]，必须分配执行器峰值电流总和以确保不超过保护额定值。这需要通过制造商提供的保险丝时间-电流曲线验证保护协调。
