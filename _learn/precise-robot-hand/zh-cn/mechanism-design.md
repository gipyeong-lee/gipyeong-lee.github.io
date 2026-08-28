---
layout: learn-module
title: 机器人机构设计
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:precise-robot-hand:mechanism-design
translations:
- lang: ko
  url: /learn/precise-robot-hand/mechanism-design/
- lang: en
  url: /learn/en/precise-robot-hand/mechanism-design/
- lang: ja
  url: /learn/ja/precise-robot-hand/mechanism-design/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/mechanism-design/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/mechanism-design/
module_id: m2
permalink: /learn/zh-cn/precise-robot-hand/mechanism-design/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
translation_run_id: caccbaa06fab4625ac40bf6e780cd0cb
id: m2
slug: mechanism-design
phase_id: p1
estimated_hours: 15.0
prerequisites:
- m1
objectives:
- 理解欠驱动系统这一机器人手机构设计的核心原理。
- 学习肌腱驱动方式的动力学特性以及摩擦力与伸长率管理的重要性。
- 掌握考虑刚性与尺寸稳定性的工程材料 (PC-CF) 选择及设计技巧。
- 夯实利用热压嵌入螺母与轴承进行精密组装设计的基础。
worked_examples:
- 示例 1：肌腱张力传递分析。若肌腱工作伸长率为 1%，在 100 mm 距离下会产生 1 mm 的误差。为实现精密控制，利用执行器电流反馈与传感器数据的闭环控制至关重要
  [S14]。
- 示例 2：嵌入件连接处设计。将 HTBI-M3-BR 螺母插入 PC-CF 打印件时，必须在 CAD 设计中遵守 4 mm 的建议导向孔直径，以实现无间隙组装
  [S23]。
lab:
  title: 机器人关节及肌腱模块组装实践
  steps:
  - 佩戴护目镜并整理工作台。
  - 确认 PC-CF 打印件导向孔状态，必要时进行加工。
  - 用电烙铁加热热压嵌入螺母，将其垂直压入打印件。
  - 将 igus 轴承安装至腕部及关节外壳。
  - 将铝轴穿过轴承并确认间隙。
  - 将 Dyneema 肌腱缠绕在绞盘上并固定在组装好的关节上。
  safety:
  - 使用电烙铁时注意高温，务必佩戴护目镜。
  - 肌腱张力测试时，为防止肌腱断裂导致的反弹事故，不得将手放入活动范围。
  - 系统组装完成后，通电前务必使用仪表确认物理断开状态。
  deliverables:
  - 已组装的机器人关节模块
  - 轴承与轴的间隙测量记录
assignment:
  title: 5 级机器人手机构设计项目
  deliverables:
  - 机器人手整体 CAD 装配图
  - 材料清单 (BOM) 及选型依据报告
  - 肌腱路径优化设计图
  rubric:
  - 使用的部件是否符合规格 (BOM)？
  - 热压嵌入螺母与轴承设计是否合理？
  - 是否实现了无机械干涉的自由运动？
quiz:
- question: 肌腱驱动中使用 Dyneema SK78 的主要原因是什么？
  choices:
  - 伸长率大且价格便宜
  - 提供低伸长率和高断裂载荷，能够确保精度
  answer_index: 1
  explanation: Dyneema SK78 的伸长率低于 1%，极低，可提高机器人控制的重复精度 [S18]。
- question: 针对 PC-CF 打印件进行重复螺纹组装，推荐的方法是什么？
  choices:
  - 直接在打印件上加工螺纹
  - 插入黄铜热压嵌入螺母
  answer_index: 1
  explanation: 对于 PC-CF 等工程塑料，热压嵌入螺母可大幅提高螺纹耐久性 [S23]。
completion_criteria:
- 完成各零件规格与参数的 BOM 文档化
- 确认组装完成的关节模块的功能性运动
- 遵守安全指引并完成实践
source_ids:
- S3
- S11
- S18
- S21
- S23
- S19
- S14
---

## 机器人机构设计原理

精密 5 级机器人手设计的核心在于实现欠驱动系统，该系统能有效控制比执行器 (Actuator) 数量更多的自由度 (DoF) [S11]。这使得机器人无需盲目增加关节数量即可稳定抓取各种形状的物体 [S3]。

### 肌腱驱动动力学
肌腱 (Tendon) 驱动是将远程电机的张力传递至关节的方式。肌腱的物理特性决定了控制精度。本课程使用 `Dyneema SK78` 纤维，其在 1.5 mm 直径下可承受 230 daN 的高断裂载荷，工作伸长率低于 1%，重复精度极高 [S18]。

### 材料与结构设计
机器人手的框架与连杆要求高刚性与尺寸稳定性。FDM 方式的 `Prusament PC Blend Carbon Fiber` 是一种含有碳纤维的 PC 材料，提供耐高温性与出色的强度，适合制作工程级零件 [S21]。为实现多次拆装，组装时避免直接切削螺纹，而是使用 M3 黄铜热压嵌入螺母（外径 4.4 mm，长度 5.8 mm）来确保螺纹耐久性 [S23]。旋转轴使用无油聚合物衬套轴承 (JSM-0810-10)，实现无需维护的顺畅旋转与摩擦管理 [S19]。
