---
layout: learn-module
title: 机器人手组装
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:precise-robot-hand:assembly
translations:
- lang: ko
  url: /learn/precise-robot-hand/assembly/
- lang: en
  url: /learn/en/precise-robot-hand/assembly/
- lang: ja
  url: /learn/ja/precise-robot-hand/assembly/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/assembly/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/assembly/
module_id: m6
permalink: /learn/zh-cn/precise-robot-hand/assembly/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
translation_run_id: caccbaa06fab4625ac40bf6e780cd0cb
id: m6
slug: assembly
phase_id: p2
estimated_hours: 15.0
prerequisites:
- m5
objectives:
- 理解用于机器人手机构组装的精密零件连接原理。
- 掌握肌腱 (Dyneema) 驱动系统的张力传递结构。
- 学习独立电源分支配置与物理配线安全。
- 掌握 FSR 传感器与分压电路的正确集成方法。
worked_examples:
- 示例 1：保险丝容量计算。若 XM430 执行器 11 台（堵转电流合计 9.2 A）连接至 1 个 12 V 分支，使用 10 A 保险丝是恰当的。这在承载正常运行范围的同时，可在配线过载时保护电路
  [S14, S26]。
- 示例 2：热压嵌入螺母深度。M3 黄铜嵌入件必须垂直准确热压入 PC-CF 打印件，需要与 4.4 mm 外径匹配的 4 mm 导向孔 [S23]。歪斜会降低螺纹组装精度，需注意。
lab:
  title: 机器人手机构组装及配线练习
  steps:
  - 在手指连杆与手掌框架上安装 M3 热压嵌入螺母。
  - 将 igus JSM-0810-10 轴承与 8 mm 铝轴安装至腕部及关节轴。
  - 将 Dyneema 肌腱缠绕在绞盘上，以适当张力连接至手指。
  - 使用 Micro-Fit 3.0 连接器为各执行器及手指传感器进行配线 [S9]。
  - 在各独立 12 V 分支安装 10 A 保险丝，并确认单独电源连接 [S26, S25]。
  safety:
  - 通电前务必使用万用表确认 3 个电源分支的绝缘状态。
  - 肌腱张力测试时，为防断裂反弹，务必佩戴护目镜。
  - 维护及接近零件前，物理断开 3 个电源适配器，并测量确认各分支电压低于 1 V。
  - 绝不并联连接两个及以上电源适配器的阳极 (+) 输出。
  deliverables:
  - 确认各关节无摩擦运行的视频
  - 各电源分支保险丝安装照片
  - 已组装机器人手的配线图及紧固扭矩记录
assignment:
  title: 机器人手系统集成报告
  deliverables:
  - 完成后的组装体 3 面图及连接点详图 (CAD)
  - 各电源分支负载分配表及保险丝容量验证结果
  - 手指弯曲时肌腱张力数据记录
  rubric:
  - 机构组装精度及轴承摩擦最小化 (40%)
  - 各独立分支的独立电源配线及遵守安全守则 (40%)
  - 提交物技术规格准确性 (20%)
quiz:
- question: 下列关于电源供应方式的说明中，正确的是？
  choices:
  - 并联连接 3 个电源适配器的阳极 (+) 端子以增加电流容量。
  - 各电源适配器作为独立分支使用，阳极 (+) 端子电气绝缘。
  answer_index: 1
  explanation: 为保障系统安全，各电源适配器均作独立分支，严禁并联连接阳极 (+) 输出。
- question: 将 FSR 402 传感器连接至 OpenCR 板时，应使用的电压是？
  choices:
  - 3.3 V 传感器电源轨
  - 12 V 执行器电源轨
  answer_index: 0
  explanation: FSR传感器分压电路必须连接到 3.3 V 传感器导轨，以将 ADC 信号保持在 0-3.3 V 的范围内。
- question: 肌腱使用 Dyneema SK78 的主要原因是？
  choices:
  - 低廉的价格和容易加工
  - 小直径下的高断裂载荷与极低的工作伸长率
  answer_index: 1
  explanation: Dyneema SK78 提供极高的强度与低伸长率，适合精密张力传递。
completion_criteria:
- 完成所有 5 个手指关节的物理组装
- 确认独立 3 个电源分支的保险丝安装
- 组装完成后，确认 3 个分支均为非通电状态（低于 1 V）
source_ids:
- S19
- S20
- S21
- S23
- S18
- S17
- S26
- S15
- S27
- S16
- S14
- S9
- S25
---

### 精密组装及线束系统

机器人手组装是必须同时确保机构刚性与电子可靠性的精密工序。主体结构采用高刚性与高尺寸稳定性的碳纤维填充 PC 丝材 (PC-CF) 制作 [S21]，并设计为可通过 M3 黄铜热压嵌入螺母进行多次拆装 [S23]。

#### 肌腱驱动原理
肌腱将执行器的旋转运动转换为手指关节的弯曲运动。Dyneema SK78 材料在 1.5 mm 直径下提供 230 daN 的高断裂载荷与低于 1% 的低工作伸长率，使张力传递效率最大化 [S18]。组装时绞盘边缘的倒圆处理是防止肌腱磨损的必备要素。

#### 独立电源及安全分支
本系统使用 3 个独立的 12 V 电源分支 [S17]。各分支在适配器间电气隔离，绝对不得并联阳极 (+) 输出。各分支串联配置 10 A ATOF 保险丝，以防配线缺陷 [S26]。设计确保了执行器堵转电流合计可被安全接纳。

#### 传感器接口
指尖的 FSR 402 传感器是随压力变化而电阻改变的可变电阻体 [S15]。教育原型不主张遵守机器安全标准或认证，在投入人员接近环境前是否需要合格安全专家的单独审查 [S27] [S16]。
