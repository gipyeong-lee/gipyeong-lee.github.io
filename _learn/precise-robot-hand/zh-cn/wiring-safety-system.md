---
layout: learn-module
title: 配线与安全断电构建
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
translation_run_id: e8f8435646734ebd8e061d010c356c2d
id: M6
slug: wiring-safety-system
phase_id: P2
estimated_hours: 10.0
prerequisites:
- M5
objectives:
- 理解执行器驱动所需的独立 12 V 电源分支构建方法。
- 学习用于过电流防护的 ATOF 保险丝的作用及选型原理。
- 掌握安全电源管理及物理断开协议。
- 配置 OpenCR 控制器及 FSR 传感器的安全分压电路。
worked_examples:
- 检测到异常发热、气味或烟雾时，切勿靠近，应切断危险区域外预先指定的建筑物配电盘断路器或认证的 upstream master disconnect 以断开 3
  个适配器的电源后再撤离。若危险区域外没有可操作的 upstream 断开手段，则禁止系统通电。转矩释放不能代替断电。维护与接近必须在计划停止后，通过物理断开及测量确认无电后方可执行
  [S11] [S25]
- '示例 2: FSR ADC 电路电压 - 使用 OpenCR 的 3.3 V 传感器导轨，连接 10 kΩ 分压电阻和 FSR 402 [S13, S26]。传感器信号电压必须在
  0~3.3 V 范围内，该电路必须与 12 V 执行器电源电路进行物理/电气分离防护。'
lab:
  title: 电源分支线束制作与安全点检
  steps:
  - 在各适配器输出线路焊接 ATO 在线保险丝座，并插入 10 A ATOF 保险丝 [S24, S25]。
  - 使用 Molex Micro-Fit 3.0 连接器制作执行器及传感器连接线束 [S14]。
  - 将 OpenCR 板与各执行器分配为 3 个分支进行配线，并连接至各电源适配器 [S13]。
  - 通电前，用万用表电阻模式确认各适配器输出端的绝缘状态。
  - 通电后，在电压模式确认各分支为 12 V，断开时必须移除 3 个适配器。
  safety:
  - 维护前必须物理断开 3 个电源适配器。
  - 在万用表确认残余电压低于 1 V 后，方可更换零件。
  - 通电期间不得将手伸入活动范围。
  - 所有接点需进行绝缘处理，焊接时必须佩戴护目镜。
  deliverables:
  - 制作完成的电源分支线束照片
  - 各分支测量电压记录表
  - 配线图检查确认书
assignment:
  title: 安全配线设计报告
  deliverables:
  - 3 个电源分支的执行器分配设计方案（每分支 4台/4台/3台）
  - 各分支过电流切断计算书（峰值电流与保险丝额定值对比）
  - 维护与接近前，必须物理断开 3 个电源适配器，并计量确认各分支处于无电状态
  rubric:
  - 是否遵守了电源独立性与分离原则？
  - 保险丝与连接器的额定值是否针对负载进行了适当选型？
  - 电源断开及残余电压确认协议是否遵循安全指南？
quiz:
- question: 各电源适配器的 12 V 输出(+)是否可以并联？
  choices:
  - 可以，电流供给能力会增强。
  - 不可以，必须维持为独立分支。
  - 电压一致时可以并联。
  - 添加保险丝后可以并联。
  answer_index: 1
  explanation: 各适配器输出必须维持独立，严禁并联连接 [S15]。
- question: 维护机器人手前最优先采取的安全措施是什么？
  choices:
  - 软件转矩释放
  - 万用表电阻测量
  - 3 个电源适配器的物理断开及残余电压确认
  - 按下计划停止按钮
  answer_index: 2
  explanation: 维护前必须物理断开 3 个电源适配器，并用万用表确认各分支残余电压低于 1 V。
- question: FSR 力传感器 ADC 电路应使用什么电源导轨？
  choices:
  - 12 V 执行器导轨
  - 5 V 电源导轨
  - 3.3 V 传感器导轨
  - 24 V 电源导轨
  answer_index: 2
  explanation: 为保护 OpenCR 的 ADC 电路，必须使用 3.3 V 传感器导轨 [S13]。
completion_criteria:
- 已完成 3 个独立分支线束配置及保险丝安装
- 各分支空载电压测得为 12 V
- 物理断开电源后，所有测量节点的残余电压均记录为低于 1 V
- 提交配线安全设计报告并获通过
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

## 安全配线及电源分离原理

5 仿生机器人手系统使用了多个高转矩执行器，因此高效且安全的电源分配至关重要。本项目使用 11 个电源适配器将执行器分为 4台/4台/3台单位进行独立 배치，目的是分散各分支的电流负载并提高电源稳定性 [S15]。

### 1. 电源独立性保障
各适配器的正(+)输出必须维持为独立分支，严禁任意合并或捆绑。应在 [S15] 指定的适配器额定输出电流(11.5 A)内，设计以承载执行器峰值电流（XM430-W350-T 1台合计 2.3 A）[S11]。 4 台单位分支的峰值电流合计为 9.2 A，在适配器的连续输出允许范围内。

### 2. 过电流防护 (Protection Coordination)
在每个分支部署 10 A ATOF 保险丝，以保护系统免受线路或执行器故障引发的过电流侵害 [S25]。仅凭保险丝与负载/电源额定的对比并不能保证安全性或动作顺序。需结合保险丝制造商的时间-电流曲线及电源 OCP 特性确认保护协调。但保险丝选型必须参照制造商提供的 'Time-Current Curve'，即便负载电流较低也不代表安全性得到保证 [S25]。

### 3. 控制电路分离
使用 DYNAMIXEL 端口内置型 OpenCR 控制板，通过消除复杂的外部桥接电路来提高可再现性 [S13]。 FSR 力传感器为将电压转换为 ADC 输入，使用从 3.3 V 传感器导轨供给的分压电路，该电路必须与 12 V 执行器电源进行电气隔离 [S13]。

### 4. 作业安全守则
台式原型并非认证的机器安全系统，因此在进行维护或修正作业前，必须物理断开 3 个电源适配器，并使用万用表 DC 电压模式计量确认各分支的残余电压低于 1 V [S7]。
