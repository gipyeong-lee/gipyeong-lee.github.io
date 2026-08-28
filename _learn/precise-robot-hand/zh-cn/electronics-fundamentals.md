---
layout: learn-module
title: 电子电路基础
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:precise-robot-hand:electronics-fundamentals
translations:
- lang: ko
  url: /learn/precise-robot-hand/electronics-fundamentals/
- lang: en
  url: /learn/en/precise-robot-hand/electronics-fundamentals/
- lang: ja
  url: /learn/ja/precise-robot-hand/electronics-fundamentals/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/electronics-fundamentals/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/electronics-fundamentals/
module_id: m4
permalink: /learn/zh-cn/precise-robot-hand/electronics-fundamentals/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
translation_run_id: caccbaa06fab4625ac40bf6e780cd0cb
id: m4
slug: electronics-fundamentals
phase_id: p2
estimated_hours: 12.0
prerequisites:
- m3
objectives:
- 理解 DYNAMIXEL 智能执行器的电气特性与电源系统。
- 使用 FSR 402 传感器设计电压分压电路并获取 ADC 信号。
- 为系统过电流保护设计基于保险丝的电源分支。
- 掌握电气电路绝缘与物理隔离原则。
worked_examples:
- 示例 1：分支电源电流总和计算。若一个分支分配有 4 台执行器（各堵转电流 2.3 A），最大理论电流为 9.2 A。这在 10 A 保险丝额定范围内，且未超过适配器
  11.5 A 的输出限值，可安全运行 [S14, S17, S26]。
- 示例 2：FSR 分压器输出计算。对 FSR 施加力导致传感器电阻变为 10 kΩ 时，分压节点电压为 3.3 V * (10 kΩ / (10 kΩ + 10
  kΩ)) = 1.65 V。这在 OpenCR 12 位 ADC 有效范围内，因此可进行精密力反馈 [S15, S16, S27]。
lab:
  title: 电源分支配置及传感器输入测试
  steps:
  - 在每个MEAN WELL适配器输出线上串联安装0AFH0001Z在线支架和 10 A ATOF保险丝 [S17, S25, S26]。
  - 利用万用表测量各分支 12 V 电压是否在正常范围内。
  - 使用 OpenCR 3.3 V 引脚、10 kΩ 电阻和 FSR 402 在面包板上构建分压电路 [S16, S27]。
  - 确认传感器电压是否在 0~3.3 V 范围内，并观察施力时的电压变化。
  safety:
  - 维护及接近前，物理断开 3 个电源适配器，并必须使用万用表确认各分支 DC 电压低于 1 V。
  - 电路配置中禁止通电。所有连接完成后，仅在固定夹具状态下测量电压。
  - 全程佩戴防冲击护目镜。
  - 绝不混用执行器电源 (12 V) 与传感器电源 (3.3 V)。
  deliverables:
  - 各电路电压测量数据表
  - FSR 力传感器力-电压响应曲线图
  - 用于过电流保护的各分支保险丝连接照片
assignment:
  title: 电源分配与传感器数据采集设计
  deliverables:
  - 执行器分支电源分配计划书
  - 包含 OpenCR ADC 电路图的配线图
  - 保险丝选型逻辑报告
  rubric:
  - 分支电源合计电流是否遵守各适配器允许范围？
  - FSR 电路是否仅连接至 3.3 V 传感器轨？
  - 是否选用了能适当进行过电流保护的保险丝额定值？
quiz:
- question: 下列哪项是配置电源分支时禁止的行为？
  choices:
  - 分分支串联安装 10 A 保险丝
  - 并联连接独立适配器的阳极 (+) 端子
  - 以 4:4:3 分配执行器
  - 将 FSR 传感器连接至 3.3 V 轨道
  answer_index: 1
  explanation: 必须将各适配器输出作为独立分支使用，严禁并联连接电源适配器输出，否则会导致系统故障及火灾隐患。
- question: 配置 FSR 402 传感器电压分压电路时，注意事项正确的是？
  choices:
  - 必须使用 12 V 执行器电源轨。
  - 必须使用 5 V 电源以提高 ADC 分辨率。
  - 必须使用 OpenCR 的 3.3 V 传感器电源。
  - 不带电阻，仅连接 FSR。
  answer_index: 2
  explanation: FSR 传感器的电压信号不应超过 OpenCR ADC 输入范围 (0~3.3 V)，因此必须使用 3.3 V 传感器电源。
completion_criteria:
- 通过万用表验证所有电源分支电路均物理断开至电压低于 1 V
- 完成保险丝安装及 3.3 V 电源分压电路配置
- 确认 FSR 传感器信号在 OpenCR ADC 中正常获取，范围为 0~3.3 V
source_ids:
- S6
- S9
- S14
- S17
- S26
- S25
- S15
- S27
- S16
---

若发现异常发热、异味或冒烟，请勿接近，并从危险区域外通过预先指定的建筑配电盘断路器或认证的上游主断路器切断 3 个适配器的供电电源后再撤离。若危险区域外无上游断路手段，则禁止系统通电。扭矩释放不能代替电源切断。维护和接近必须在计划停机后通过物理断开并确认无电状态下进行 [S14] [S17] [S26, S25] [S26] [S15] [S27] [S16]
