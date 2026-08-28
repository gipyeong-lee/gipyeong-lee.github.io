---
layout: learn-module
title: 布线及安全的电源分离构建
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:precise-robot-hand:wiring-safety-system
translations:
- lang: ko
  url: /learn/precise-robot-hand/wiring-safety-system/
- lang: en
  url: /learn/en/precise-robot-hand/wiring-safety-system/
- lang: ja
  url: /learn/ja/precise-robot-hand/wiring-safety-system/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/wiring-safety-system/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/wiring-safety-system/
module_id: M6
permalink: /learn/zh-cn/precise-robot-hand/wiring-safety-system/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: 2b7c146b08954623a88a715bf8cc7d0e
id: M6
slug: wiring-safety-system
phase_id: P2
estimated_hours: 10.0
prerequisites:
- M5
objectives:
- 理解用于执行器驱动的独立 12 V 电源分支配置方法。
- 学习用于过流保护的 ATOF 熔断器作用及选型原理。
- 掌握安全的电源管理及物理断开协议。
- 构成 OpenCR 控制器及 FSR 传感器安全的电压分压电路。
worked_examples:
- 检测到异常发热、异味或冒烟时请勿靠近，在危险区域外用指定断路器切断 3 个适配器的供电电源后撤离。没有 upstream 断开手段时禁止系统通电。转矩释放不能代替断电。维护/接近应在计划停止后进行物理断开及无电测量确认后再执行
  [S11] [S25]
- 例题 2：FSR ADC 电路电压 - 使用 OpenCR 的 3.3 V 传感器导轨连接 10 kΩ 分压电阻与 FSR 402 [S13, S26]。传感器信号电压应在
  0~3.3 V 范围内，此电路必须与 12 V 执行器电源电路在物理/电气上分离以进行保护。
lab:
  title: 电源分支线束制作及安全检查
  steps:
  - 在各适配器输出线安装 ATO 在线熔断器座，并插入 10 A ATOF 熔断器 [S24, S25]。
  - 使用 Molex Micro-Fit 3.0 连接器制作执行器及传感器连接线束 [S14]。
  - 将 OpenCR 板与各执行器以 3 个分支进行配线，并连接至各电源适配器 [S13]。
  - 通电前，使用万用表电阻模式确认各适配器输出端的绝缘状态。
  - 通电后，在电压模式确认各分支为 12 V，断开时务必拆除 3 个适配器。
  safety:
  - 维护前请物理断开 3 个电源适配器。
  - 使用万用表确认残余电压低于 1 V 后再进行部件更换。
  - 通电期间请勿将手放入工作范围内。
  - 所有连接处均需绝缘处理，焊接时佩戴护目镜。
  deliverables:
  - 制作完成的电源分支线束照片
  - 各分支测量电压记录表
  - 配线图评审确认表
assignment:
  title: 安全配线设计报告
  deliverables:
  - 3 个电源分支的执行器分配设计案（各分支 4 台/4 台/3 台）
  - 各分支过流阻断计算书（峰值电流与熔断器额定比较）
  - 在计划停止后进行维护/接近前，物理断开 3 个电源适配器，并 계측确认各分支无电状态
  rubric:
  - 是否遵守电源独立性与分离原则？
  - 熔断器与连接器的额定值是否适合负载？
  - 电源分离及残余电压确认协议是否符合安全指南？
quiz:
- question: 可以将各电源适配器的 12 V 输出(+)并联连接吗？
  choices:
  - 可以，电流供给能力增加。
  - 不可以，必须维持独立分支。
  - 如果电压一致就可以。
  - 如果增加熔断器就可以。
  answer_index: 1
  explanation: 各适配器输出必须独立维护，绝对禁止并联 [S15]。
- question: 在维护机器人手之前最优先的安全措施是？
  choices:
  - 软件转矩释放
  - 万用表电阻测量
  - 3 个电源适配器的物理断开及残余电压确认
  - 按下计划停止按钮
  answer_index: 2
  explanation: 维护前务必物理断开 3 个电源适配器，并用万用表确认各分支残余电压低于 1 V。
- question: FSR 力传感器 ADC 电路应使用哪个电源导轨？
  choices:
  - 12 V 执行器导轨
  - 5 V 电源导轨
  - 3.3 V 传感器导轨
  - 24 V 电源导轨
  answer_index: 2
  explanation: 为保护 OpenCR 的 ADC 电路，必须使用 3.3 V 传感器导轨 [S13]。
completion_criteria:
- 3 个独立分支线束构成及熔断器安装完成
- 各分支空载电压测得为 12 V
- 物理断电后所有测量节点的残余电压均记录为低于 1 V
- 提交并通电源安全设计报告
source_ids:
- S14
- S24
- S25
- S7
- S15
- S11
- S13
- S26
---

## 安全布线及电源分离原理

5 级机器人手系统使用多台高转矩执行器，因此高效且安全的电源分配至关重要。本课程使用 11 个电源适配器，将执行器以 4 台/4 台/3 台单位进行分离配置，旨在分散各分支电流负载并提高电源稳定性 [S15]。

### 1. 电源独立性确保
各适配器的正极(+)输出必须维持为独立分支，严禁擅自合并或捆绑。应在 [S15] 中说明的适配器额定输出电流 (11.5 A) 内，承载执行器峰值电流（XM430-W350-T 每 1 台 2.3 A） [S11]。 4 台单位分支的峰值电流合计为 9.2 A，在适配器的连续输出允许范围内。

### 2. 过流保护 (Protection Coordination)
各分支配置 10 A ATOF 熔断器，以保护系统免受线路或执行器错误导致的过流侵害 [S25]。ATOF 熔断器在额定电流的 110%~135% 水平动作，相对于峰值电流 9.2 A，可进行稳定的保护。但熔断器选型务必参照制造商提供的“Time-Current Curve”，负载电流小并不能保证安全 [S25]。

### 3. 控制电路分离
使用 DYNAMIXEL 端口内建型 OpenCR 控制板，剔除复杂的外部桥接电路，提高再现性 [S13]。FSR 力传感器为将电压转换给 ADC 输入，使用从 3.3 V 传感器导轨供电的分压电路，该电路必须与 12 V 执行器电源在电气上分离 [S13]。

### 4. 工作安全守则
台式原型机非认证机器安全系统，在进行维护或修正作业前，务必物理断开 3 个电源适配器，并使用万用表直流电压模式确认各分支残余电压低于 1 V [S7]。
