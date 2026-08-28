---
layout: learn-module
title: 轴承及锁紧件安装
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
translation_run_id: e8f8435646734ebd8e061d010c356c2d
id: M5
slug: bearing-fastener-install
phase_id: P2
estimated_hours: 10.0
prerequisites:
- M4
objectives:
- 理解精密机器人手制作所需的轴承及轴的机械公差与安装原理。
- 学习使用热熔嵌件(Heat-set insert)确保工程塑料零件锁紧强度的方法。
- 使用合适的转矩和锁紧规格，最大限度减少组装游隙。
worked_examples:
- '示例 1: 确认外壳内径 - iglide® JSM-0810-10 轴承外径为 10 mm。因此外壳孔径必须按 10 mm 设计，且插入嵌件时若不遵守 4.0
  mm 的引孔规格，会导致嵌件打滑或外壳损坏 [S17, S21]。'
- '示例 2: M3 螺钉组装 - M3x10 帽螺钉使用 2.5 mm 内六角扳手锁紧，过大转矩会导致嵌件周围树脂产生裂纹，因此要在“不再转动的一点”用最小限度的力固定
  [S20]。'
lab:
  title: 机器人手关节精密组装
  steps:
  - 1. 确认 PC-CF 打印件外壳上的 4.0 mm 引孔干净，将嵌件垂直对齐。
  - 2. 将烙铁加热至合适温度，垂直缓慢按下嵌件，使其与外壳表面平行压入。
  - 3. 将 iglide® 轴承压入孔位，插入 8 mm 铝轴，确认游隙与阻力。
  - 4. 使用 M3 螺钉完成连杆间锁紧，转动关节验证摩擦是否均匀。
  safety:
  - 烙铁温度极高，注意烫伤，加热后立即放入架上。
  - 嵌件压入时产生的微尘应防止吸入，必须彻底通风。
  - 佩戴护目镜进行作业。
  - 检测到异常发热、气味或烟雾时，切勿靠近，应切断危险区域外预先指定的建筑物配电盘断路器或认证的 upstream master disconnect 以断开
    3 个适配器的电源后再撤离。若危险区域外没有可操作的 upstream 断开手段，则禁止系统通电。转矩释放不能代替断电。维护与接近必须在计划停止后，通过物理断开及测量确认无电后方可执行。
  deliverables:
  - 关节摩擦测试日志
  - 嵌件垂直对齐检查照片
  - 组装后连杆的自由度及游隙测量记录
assignment:
  title: 组装公差及锁紧力分析报告
  deliverables:
  - 关节组装顺序及转矩管理计划书
  - 发生游隙时的解决方法（使用垫片或修改公差）技术描述
  - 已组装机器人手连杆的抓取测试预备数据
  rubric:
  - 是否明确描述了嵌件插入的垂直度？
  - 是否正确解释了轴承与轴的公差概念？
  - 是否遵守了组装阶段的安全守则？
quiz:
- question: iglide® J 轴承压入外壳后内径发生调整的原因是什么？
  choices:
  - 因轴承材料的弹性，压入时内径自动增大。
  - 设计旨在压入过程中根据外壳孔径的公差精密调整轴承内径。
  - 压入前的内径总是制作得比基准值小。
  answer_index: 1
  explanation: iglide® 滑动轴承在压入前制作得比基准值大，在压入正确的外壳孔径中时，设计为达到规定公差内的内径 [S17]。
- question: 在 PC-CF 打印件上使用黄铜热熔嵌件时合适的引孔尺寸是？
  choices:
  - 3.5 mm
  - 4.0 mm
  - 4.4 mm
  answer_index: 1
  explanation: 根据数据手册，HTBI-M3-BR 嵌件建议的引孔尺寸为 4.0 mm [S21]。
completion_criteria:
- 确认已组装的 5 个手指关节的摩擦阻力均匀并提交测量记录。
- 目视及尺寸检查确认所有嵌件均与 PC-CF 外壳水平。
- 签署组装过程中已遵守安全守则的誓言书并提交作业记录簿。
source_ids:
- S17
- S18
- S20
- S21
---

### 轴承与轴的公差管理
为保证精密机器人关节的顺畅运动及刚性，使用 iglide® J 滑动轴承(JSM-0810-10)和 8 mm 铝合金精密轴(AWMP-08)。滑动轴承设计为在外壳中压入(press-fit)时内径会进行调整，遵循外壳建议的内径公差是关键 [S17, S18]。游隙过大会降低关节精度，而过窄则会导致摩擦力增加，降低执行器(DYNAMIXEL XM430)的电流效率。

### 热熔嵌件安装
PC-CF(碳纤维增强 PC)打印件若直接锁紧金属螺钉，因材料特性极易磨损螺纹。为防止此类情况，使用黄铜材质的热熔嵌件(HTBI-M3-BR) [S21]。嵌件插入 4.0 mm 引孔后加热熔化周围树脂进行锁紧，即使反复拆装也能维持极高的机械强度 [S21]。若此时嵌件倾斜，会导致组装后的连杆对齐偏差，因此保持垂直至关重要。
