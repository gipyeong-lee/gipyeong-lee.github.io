---
layout: learn-module
title: 3D 打印及零件加工
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:precise-robot-hand:3d-printing-assembly
translations:
- lang: ko
  url: /learn/precise-robot-hand/3d-printing-assembly/
- lang: en
  url: /learn/en/precise-robot-hand/3d-printing-assembly/
- lang: ja
  url: /learn/ja/precise-robot-hand/3d-printing-assembly/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/3d-printing-assembly/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/3d-printing-assembly/
module_id: M4
permalink: /learn/zh-cn/precise-robot-hand/3d-printing-assembly/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: 2b7c146b08954623a88a715bf8cc7d0e
id: M4
slug: 3d-printing-assembly
phase_id: P2
estimated_hours: 15.0
prerequisites:
- M3
objectives:
- 理解使用碳纤维增强 PC 丝材 (PC-CF) 进行零件制作及输出设置优化的方法。
- 掌握热熔嵌入螺母 (Heat-set insert) 及滑动轴承的精密组装公差管理。
- 理解用于肌腱驱动机制的 Dyneema 线处理及卷扬轮设计结构。
- 熟知为确保机器人结构尺寸稳定性和刚性的加工及紧固技术。
worked_examples:
- 例题 1：PC-CF 丝材喷嘴选择 - 鉴于碳纤维的高磨损性，黄铜喷嘴会迅速磨损并导致打印质量下降及喷嘴堵塞，因此必须确认选择硬化钢 (Hardened steel)
  喷嘴 [S19]。
- 例题 2：插件孔设计 - Accu HTBI-M3-BR 插件外径为 4.4mm，但官方建议孔径为 4.0mm [S21]，因此 CAD 设计时应将孔直径固定为
  4.0mm，以便热熔嵌入时塑料足以渗入插件滚花 (knurling) 之间 [S21]。
lab:
  title: 手指结构件制造与组装实践
  steps:
  - 设置配备硬化钢喷嘴的 FDM 3D 打印机以适用于碳纤维 PC 丝材环境 [S19]。
  - 打印手指连杆与手掌框架后，清除支撑并整理表面。
  - 用热工具将热熔嵌入插件垂直安装至 4.0mm 引导孔中 [S21]。
  - 切割 IGUS 精密铝轴并对末端进行倒角 [S18]。
  - 将滑动轴承压入外壳，插入轴并确认间隙 [S17]。
  - 使用 M3 帽螺钉紧固结构及传感器支架 [S20]。
  safety:
  - 注意高温喷嘴 (285°C) 及热床 (110°C) 造成的烧伤 [S19]。
  - 后加工打印件及倒角时必须佩戴护目镜。
  - 加热插件时可能产生烟雾，应开启通风设施。
  - 通电前检查所有机械紧固状态。
  deliverables:
  - 制作完成的 5 级机器人手结构（连杆、手掌）。
  - 热熔嵌入插件垂直度及轴承间隙测量记录。
  - 最终紧固部位外观检查完成报告。
assignment:
  title: 机器人手制造精度验证
  deliverables:
  - 成品结构的 CAD 数据与实际尺寸测量对照表
  - 组装公差管理计划书
  - 肌腱布线结构的摩擦减小设计说明书
  rubric:
  - 热熔嵌入插件是否垂直就位（优/良/差）
  - 轴承-轴组装后旋转运动是否平滑（合格/不合格）
  - 是否遵守 BOM 中指定的零件额定值及型号规格 [B10, B11, B12, B13, B14]
quiz:
- question: 使用 PC-CF 丝材时必须使用硬化钢喷嘴的主要原因是什么？
  choices:
  - 防止碳纤维的磨损性导致黄铜喷嘴迅速磨损
  - 丝材熔点低，普通喷嘴无法打印
  - 为了提高打印件的表面光泽
  - 为了提高挤出速度
  answer_index: 0
  explanation: 碳纤维具有极高的磨损性，会迅速损坏普通黄铜喷嘴，因此硬化钢喷嘴是必须的 [S19]。
- question: 使用 M3 热熔嵌入插件 (Accu HTBI-M3-BR) 时建议的引导孔直径是？
  choices:
  - 3.0mm
  - 4.0mm
  - 4.4mm
  - 5.0mm
  answer_index: 1
  explanation: 数据手册中建议的孔直径为 4.0mm [S21]。
completion_criteria:
- 所有结构件均通过 FDM 3D 打印完成 [B10]
- 热熔嵌入插件准确就位于所有指定孔位 [B14]
- 铝轴与滑动轴承的组装间隙满足标准值 [B11, B12]
- 紧固时正确使用了 M3 规格的帽螺钉 [B13]
source_ids:
- S19
- S21
- S17
- S18
- S16
- S20
---

### 3D 打印及零件加工理论

#### 碳纤维增强工程材料 (PC-CF)
PC (Polycarbonate) 具备优异的刚性与耐热性，其中添加了碳纤维的 PC-CF 丝材最大化了刚性，适用于结构件制作 [S19]。但由于碳纤维的磨损性，务必使用硬化钢喷嘴 [S19]，并需要 285°C 左右的高温打印 [S19]。

#### 用于精密组装的插件及紧固
为实现塑料件的可重复装卸，使用热熔嵌入螺纹插件 [S21]。对于 M3 插件，需在 CAD 设计时预先放置 4.0mm 直径的引导孔以精确就位 [S21]。此外，免润滑聚合物滑动轴承 (iglide J) 与 8mm 铝轴组装时，设计为压入后内径具有最佳间隙 [S17]，因此对轴直径 8mm 的公差管理必不可少 [S17, S18]。

#### 肌腱驱动结构
Dyneema SK78 纤维在直径 1.5mm 时具有 230 daN 的高断裂载荷和低于 1% 的延伸率 [S16]，是钢缆的优良替代品。由于肌腱在旋转轴处反复弯曲，将卷扬轮边缘进行倒角处理以防止摩擦造成的断线是重要的结构设计。
