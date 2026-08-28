---
layout: learn-module
title: 测试与验证
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
module_id: m8
permalink: /learn/zh-cn/precise-robot-hand/testing-validation/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
translation_run_id: caccbaa06fab4625ac40bf6e780cd0cb
id: m8
slug: testing-validation
phase_id: p3
estimated_hours: 10.0
prerequisites:
- m7
objectives:
- 制定系统的机械手驱动性能评估测试流程。
- 为数据驱动的精密验证分析传感器数据与执行器反馈。
- 验证机械手的机构耐久性及重复精度。
- 编写系统集成后的安全操作指南。
worked_examples:
- '**示例 1：重复精度误差分析**

  在目标点 50 度处重复移动 100 次后收集编码器值，结果显示平均值为 50.02 度，标准差为 0.05 度。符合要求的精度范围。'
- '**示例 2：基于 FSR 的抓取力校准**

  当无压力时 ADC 值为 50，最大抓取（20 N）时为 3800，使用线性插值公式从 ADC 值实时估算力 (N) [S15]。'
lab:
  title: 机械手工作范围及抓取力验证
  steps:
  - 确认各独立分支电源适配器连接处的电压为 12 V。
  - 在软件扭矩释放状态下，进行机械机构检查，确保各连杆无干涉。
  - 在空载状态下，逐步确认各手指的工作范围。
  - 分阶段（0.5 N, 1 N, 5 N）向 FSR 传感器施加压力并记录 ADC 信号。
  - 结束通电测试后，物理断开所有电源适配器。
  - 使用万用表确认 3 个分支的电压已放电至低于 1 V。
  safety:
  - 维护及接触前，物理断开 3 个绝缘电源适配器，并测量确认处于无电状态。
  - 通电过程中严禁将手伸入工作范围，并须固定在测试夹具上。
  - 若检测到异常发热、异味或烟雾，请勿靠近，应在危险区域外通过预设的建筑物配电盘断路器或经认证的 upstream master disconnect 切断 3
    个适配器的供电电源，然后撤离。若危险区域外没有可操作的 upstream 断路手段，则严禁系统通电。扭矩释放不能代替断电。维护与接触操作仅可在计划停机后，经物理隔离并确认处于无电状态后方可进行。
  - 操作时必须佩戴防冲击安全防护眼镜。
  deliverables:
  - 工作范围及抓取力测试日志数据文件
  - 重复精度统计分析报告
  - 各电源分支测量安全确认书
assignment:
  title: 编写最终性能验证报告
  deliverables:
  - 系统集成验证报告 (PDF)
  - 性能指标数值数据及可视化图表
  - 操作指南及故障排除程序手册
  rubric:
  - 确认工作范围及重复精度测量数据的一致性
  - 基于 FSR 传感器数据的力控制算法验证
  - 通过机械耐久性测试评估是否存在破损及装配稳定性
  - 安全指南遵守情况及程序合理性
quiz:
- question: 下列关于系统安全维护程序的说法中不正确的是？
  choices:
  - 执行软件扭矩释放。
  - 计划停机后，维护/接触前物理断开 3 个电源适配器，并测量确认各分支处于无电状态。
  - 物理断开 3 个电源适配器，并使用万用表直流电压模式确认各分支剩余电压低于 1 V。
  - 用直流电压模式测量确认各分支低于 1 V。
  answer_index: 2
  explanation: 电阻模式可能会测量带电电路或因未放电的电容器导致设备损坏及读数错误。必须始终使用直流电压模式确认无电状态。
- question: 在使用 FSR 402 传感器和 OpenCR 板进行电路构建时需要注意什么？
  choices:
  - FSR 分压器仅使用 3.3 V 传感器电源，并将模拟输入信号保持在 0~3.3 V 范围内。
  - FSR 分压电路必须仅使用 3.3 V 传感器电源。
  answer_index: 1
  explanation: OpenCR 的 ADC 输入不得超过 0~3.3 V 范围，因此必须使用稳定的 3.3 V 传感器电源。
completion_criteria:
- 提交测试验证阶段的所有实验数据并完成日志分析。
- 遵守 3 个独立电源分支的物理隔离及安全电压测量程序。
- 重复精度和抓取力的定量评估指标达到目标范围。
- 通过最终报告证明所有机械部件和电子电路运行安全。
source_ids:
- S1
- S12
- S14
- S15
- S18
- S21
- S16
- S17
- S26
---

### 1. 机械手性能评估的核心指标
机械手性能验证是证明机构设计保真度和控制算法有效性的过程 [S1]。主要评估指标如下：
- **重复精度 (Repeatability)：** 到达相同目标位置时的误差范围，通过 `XM430-W350-T` 执行器的高分辨率编码器反馈进行计算 [S14]。
- **抓取稳定性 (Grasp Stability)：** 通过分析 `FSR 402` 传感器测量的接触力分布，评估物体抓取是否平稳无滑动 [S15]。
- **耐久性 (Durability)：** 执行重复负载测试，确认腱 (`Dyneema SK78`) 和连杆 (`PC-CF`) 结构的疲劳破坏情况 [S18, S21]。

### 2. 数据采集与分析
通过 `OpenCR` 控制板的 ADC 实时采集 FSR 数据。使用 3.3 V 传感器电源，将力信号转换为 0~3.3 V 范围内最大 12-bit 分辨率的信号 [S16]。数据采集时，为减少噪声，应应用移动平均滤波器等来平滑抓取力的变化。

### 3. 电气安全验证
每个执行器组配置为独立的 `12 V` 适配器分支，并使用 `10 A` ATOF 保险丝进行过流保护 [S17, S26]。系统无电状态的确认始终通过 DC-电压模式（低于 1 V）进行测量。
