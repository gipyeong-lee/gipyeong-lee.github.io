---
layout: learn-module
title: 轴承及紧固件安装
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:precise-robot-hand:bearing-fastener-install
translations:
- lang: ko
  url: /learn/precise-robot-hand/bearing-fastener-install/
- lang: en
  url: /learn/en/precise-robot-hand/bearing-fastener-install/
- lang: ja
  url: /learn/ja/precise-robot-hand/bearing-fastener-install/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/bearing-fastener-install/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/bearing-fastener-install/
module_id: M5
permalink: /learn/zh-cn/precise-robot-hand/bearing-fastener-install/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: 2b7c146b08954623a88a715bf8cc7d0e
id: M5
slug: bearing-fastener-install
phase_id: P2
estimated_hours: 10.0
prerequisites:
- M4
objectives:
- 理解用于精密机器人手制作的轴承及轴的机械公差与安装原理。
- 掌握使用热熔嵌入插件 (Heat-set insert) 确保工程塑料件紧固强度的方法。
- 通过使用适当的转矩和紧固规格最小化组装间隙。
worked_examples:
- 例题 1：确认外壳内径 - iglide® JSM-0810-10 轴承外径为 10 mm。因此外壳内孔设计必须符合 10 mm，若不遵守插件安装时 4.0 mm
  引导孔，插件可能产生空转或导致外壳破裂 [S17, S21]。
- 例题 2：M3 螺钉组装 - M3x10 帽螺钉使用 2.5 mm 内六角扳手锁紧，由于过大转矩会导致插件周围树脂开裂，应在“不再转动时”以最小力度固定 [S20]。
lab:
  title: 机器人手关节精密组装
  steps:
  - 1. 确认 PC-CF 打印件外壳中 4.0 mm 引导孔清洁，并将插件垂直对齐。
  - 2. 将烙铁加热至适当温度，垂直缓慢按下插件，使其与外壳表面平行压入。
  - 3. 将 iglide® 轴承压入内孔，插入 8 mm 铝轴，确认间隙与阻力。
  - 4. 使用 M3 螺钉完成连杆间的紧固，并活动关节验证摩擦是否均匀。
  safety:
  - 烙铁为高温物件，注意烧伤，加热后立即放入支架。
  - 插件压入时产生的微尘不得吸入，务必充分通风。
  - 必须佩戴护目镜进行作业。
  - 检测到异常发热、异味或冒烟时请勿靠近，在危险区域外用指定断路器切断 3 个适配器的供电电源后撤离。没有 upstream 断开手段时禁止系统通电。转矩释放不能代替断电。维护/接近应在计划停止后进行物理断开及无电测量确认后再执行。
  deliverables:
  - 各关节摩擦测试记录表
  - 插件垂直对齐确认照片
  - 组装后的连杆自由度及间隙测量记录
assignment:
  title: 组装公差及紧固力分析报告
  deliverables:
  - 关节组装顺序及转矩管理计划书
  - 出现间隙时的解决方法（使用 Shim 或修正公差）说明
  - 组装完成后的机器人手连杆抓取测试初步数据
  rubric:
  - 是否明确描述了插件安装的垂直度？
  - 是否正确说明了轴承与轴的公差概念？
  - 组装阶段是否遵守了安全守则？
quiz:
- question: 为什么 iglide® J 轴承压入外壳后内径会发生调整？
  choices:
  - 由于轴承材质的弹性，压入时内径自动增大。
  - 是因为设计上使得压入过程中的内径可以根据外壳内孔的公差精确调整。
  - 是因为压入前的内径总是被制作得比标准值小。
  answer_index: 1
  explanation: iglide® 滑动轴承制作时比标准值大，设计为压入正确的外壳内孔时，内径达到设计公差内 [S17]。
- question: 在 PC-CF 打印件上使用黄铜热熔嵌入插件时合适的引导孔大小是？
  choices:
  - 3.5 mm
  - 4.0 mm
  - 4.4 mm
  answer_index: 1
  explanation: 根据数据手册，HTBI-M3-BR 插件的建议引导孔大小为 4.0 mm [S21]。
completion_criteria:
- 完成 5 个手指关节摩擦阻力均匀性的确认及测量记录提交。
- 完成所有插件与 PC-CF 外壳水平度及尺寸检查。
- 承诺遵守组装中的安全守则并提交工作记录表。
source_ids:
- S17
- S18
- S20
- S21
---

### 轴承与轴的公差管理
为确保精密机器人关节的平稳运动及刚性，使用 iglide® J 滑动轴承 (JSM-0810-10) 和 8 mm 精密铝轴 (AWMP-08)。滑动轴承设计为压入 (press-fit) 外壳时调整内径，遵守外壳建议内径公差是核心 [S17, S18]。间隙过大会降低关节精度，反之过小会增加摩擦，从而降低执行器 (DYNAMIXEL XM430) 的电流效率。

### 热熔嵌入插件安装
PC-CF (碳纤维增强 PC) 打印件在直接锁紧金属螺钉时，由于材质特性容易磨损螺纹。为防止此类现象，使用黄铜材质的热熔嵌入插件 (HTBI-M3-BR) [S21]。插件插入 4.0 mm 引导孔后加热，使周围树脂熔化并紧固，从而在反复拆装时保持高机械强度 [S21]。此时插件如果倾斜，会导致连杆排列偏差，因此保持垂直是必须的。
