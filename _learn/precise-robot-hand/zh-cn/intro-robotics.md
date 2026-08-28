---
layout: learn-module
title: 机器人工程概论
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:precise-robot-hand:intro-robotics
translations:
- lang: ko
  url: /learn/precise-robot-hand/intro-robotics/
- lang: en
  url: /learn/en/precise-robot-hand/intro-robotics/
- lang: ja
  url: /learn/ja/precise-robot-hand/intro-robotics/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/intro-robotics/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/intro-robotics/
module_id: m1
permalink: /learn/zh-cn/precise-robot-hand/intro-robotics/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
translation_run_id: caccbaa06fab4625ac40bf6e780cd0cb
id: m1
slug: intro-robotics
phase_id: p1
estimated_hours: 10.0
prerequisites: []
objectives:
- 理解机器人工程的定义与系统组成要素。
- 掌握 5 级机器人手原型所用执行器与控制器的作用。
- 学习机器人系统的安全电源分支配置与物理断开原理。
- 掌握力传感器 (FSR) 的工作原理与 ADC 数据获取方法。
worked_examples:
- 执行器负载计算：将 4 台 XM430-W350-T 分配到 1 个分支时，峰值电流为 4 * 2.3 A = 9.2 A [S14]。这在 10 A 保险丝的额定范围内，且小于电源适配器的
  11.5 A 输出额定值，可稳定运行 [S17, S26]。
- FSR 电压分压器设计：在传感器与 10 kΩ 电阻串联的分压器中，输入 3.3 V 时，传感器未受压处于高阻态，ADC 输出接近 0 V；受到强力导致电阻骤减时，ADC
  输出接近 3.3 V [S15, S27]。
lab:
  title: 电源分支配置及系统基本通电测试
  steps:
  - 在各 MEAN WELL 适配器的阳极 (+) 端子上连接 ATO 内联保险丝座和 10 A 保险丝，创建 3 个独立分支 [S17, S25, S26]。
  - 将万用表设置为 DC 电压模式，确认各分支的输出电压为 12 V。
  - 将 OpenCR 控制器连接至 3.3 V 传感器电源轨，并利用 FSR 传感器和 10 kΩ 电阻构成分压电路 [S16, S27]。
  - 给控制器通电后，使用 DYNAMIXEL Wizard 确认各肌腱执行器是否正常通信 [S14, S16]。
  safety:
  - 通电前，不要使用万用表的电阻模式，而应通过肉眼和电路图重新验证所有连接。
  - 通电期间禁止接近系统，必须在非通电状态（物理断开适配器）下进行配线。
  - 若发现异常发热、异味或冒烟，请勿接近，并从危险区域外通过预先指定的建筑配电盘断路器或认证的上游主断路器切断 3 个适配器的供电电源后再撤离。若危险区域外无上游断路手段，则禁止系统通电。扭矩释放不能代替电源切断。维护和接近必须在计划停机后通过物理断开并确认无电状态下进行。
  - 全程佩戴护目镜，身体部位不得进入活动范围。
  deliverables:
  - 各分支 12 V 测量记录照片
  - OpenCR ADC 传感器数据获取代码
  - 独立分支连接配线图
assignment:
  title: 机器人系统安全设计报告
  deliverables:
  - 独立电源分支配置图
  - 执行器峰值电流与保险丝额定值合理性分析
  - FSR 电压分压电路设计计算公式
  rubric:
  - 是否明确分配了 11 台执行器与 3 个电源分支？
  - 是否正确说明了 3.3 V 传感器轨与 12 V 执行器轨的分离？
  - 是否准确叙述了电源切断程序（物理断开）？
quiz:
- question: 在系统电源设计中，为何禁止将 12 V 输出端子的阳极 (+) 极并联连接？
  choices:
  - 因为电压会升高至 24 V
  - 存在因适配器间电位差导致逆电流及破坏独立分支保护的风险
  - 因为会导致执行器的通信速度下降
  - 因为无法使用软件扭矩释放功能
  answer_index: 1
  explanation: 各电源适配器应作为独立分支运行，若连接输出端子，可能会发生故障或导致独立保险丝提供的安全保护功能失效。
- question: 读取 FSR 信号至 OpenCR 的 ADC 端口时，合适的供电电压是？
  choices:
  - 12 V 执行器轨道
  - 3.3 V 传感器轨道
  - 24 V 输入电源
  - 非接触式无线电力
  answer_index: 1
  explanation: OpenCR 的 ADC 使用 0~3.3 V 范围，为保护传感器，必须使用专用的 3.3 V 传感器轨供电。
- question: 进行系统检查和维护时，切断电源的最安全方法是？
  choices:
  - 通过软件指令释放执行器扭矩
  - 移除保险丝
  - 物理断开 3 个电源适配器并测量电压
  - 仅关闭控制器电源开关
  answer_index: 2
  explanation: 软件指令或保险丝不能保证完全的无电状态。必须物理断开适配器并用万用表测量确认电压低于 1 V。
completion_criteria:
- 通过万用表确认各分支 12 V 电压在正常范围内并提交照片
- 通过控制器确认 FSR 传感器随接触力变化的 ADC 值变化并获取有效数据
- 理解并遵守物理切断电源及通过电压测量进行安全停机的程序
source_ids:
- S1
- S14
- S16
- S17
- S25
- S26
- S15
- S27
---

## 机器人系统组成要素
机器人由感知 (Sensor)、思维 (Controller)、动作 (Actuator) 三个核心要素组成 [S1]。本课程的 5 级机器人手使用 DYNAMIXEL XM430-W350-T 执行器，通过肌腱驱动方式控制关节 [S14]，并由 OpenCR 1.0 控制器处理这些执行器及指尖 FSR 传感器的信号 [S16]。

## 电力系统的安全设计
执行器在 12 V 电压下需要 2.3 A 的堵转电流 [S14]，因此考虑到系统总负载，使用了 3 个 MEAN WELL GST160A12-R7B 适配器 [S17]。每个适配器负责 4 台/4 台/3 台执行器的独立 12 V 分支，这些分支的阳极 (+) 输出互不连接，在物理上是隔离的。各分支通过内联保险丝座 (0AFH0001Z) 安装 10 A ATOF 保险丝，以在发生过电流时保护配线 [S25, S26]。这是超越简单停机功能的电气安全基础。

## 传感器接口
FSR 402 传感器具有电阻随接触力增加而减小的特性 [S15]。将其与 10 kΩ 电阻构成电压分压电路，并连接至 OpenCR 的 12 位 ADC 端口，从而将接触力转换为电压 [S16, S27]。此时，传感器电路必须仅由 3.3 V 传感器电源轨供电，不得与执行器用的 12 V 电源轨混用。
