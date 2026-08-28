---
layout: learn-module
title: 3D 打印及零部件加工
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
translation_run_id: e8f8435646734ebd8e061d010c356c2d
id: M4
slug: 3d-printing-assembly
phase_id: P2
estimated_hours: 15.0
prerequisites:
- M3
objectives:
- 理解使用碳纤维增强 PC 线材(PC-CF)进行零部件制作及优化打印设置。
- 掌握热熔嵌件(Heat-set insert)及滑动轴承的精密组装公差管理。
- 理解用于肌腱驱动机制的 Dyneema 线处理方法及绞盘设计结构。
- 掌握确保机器人结构件尺寸稳定性与刚性的加工及锁紧技术。
worked_examples:
- '示例 1: PC-CF 线材喷嘴选择 - 考虑到碳纤维的高磨损性，Brass(黄铜)喷嘴会快速磨损导致打印质量下降和堵头，因此确认必须选择硬化钢(Hardened
  steel)喷嘴 [S19]。'
- '示例 2: 嵌件孔设计 - Accu HTBI-M3-BR 嵌件外径为 4.4mm，但官方建议孔径为 4.0mm [S21]，因此 CAD 设计时将孔径固定为
  4.0mm，使塑料在热熔时能充分嵌入嵌件滚花(knurling)之间 [S21]。'
lab:
  title: 手指结构件制作与组装实习
  steps:
  - 设定配备硬化钢喷嘴的 FDM 3D 打印机打印碳纤维 PC 线材的环境 [S19]。
  - 手指连杆和手掌框架打印完成后，去除支撑并整理表面。
  - 利用热工具将热熔嵌件垂直安放在 4.0mm 引孔内 [S21]。
  - 按轴承规格切割 IGUS 精密铝轴并对端部倒角 [S18]。
  - 滑动轴承压入外壳后插入轴，确认游隙 [S17]。
  - 使用 M3 帽螺钉锁紧结构件及传感器支架 [S20]。
  safety:
  - 注意高温喷嘴(285°C)及平台(110°C)导致的烫伤风险 [S19]。
  - 打印件后处理及倒角作业时必须佩戴护目镜。
  - 热熔嵌件加热时可能会产生烟雾，应开启通风设备。
  - 通电前确认所有机械锁紧状态。
  deliverables:
  - 制作完成的 5 仿生机器人手结构件（连杆、手掌）。
  - 热熔嵌件垂直度及轴承游隙测量记录。
  - 最终锁紧部位目视检查完成报告。
assignment:
  title: 机器人手制作精度验证
  deliverables:
  - 成品结构的 CAD 数据与实际尺寸测量对比表
  - 组装公差管理计划书
  - 肌腱路径结构的减摩设计说明书
  rubric:
  - 热熔嵌件是否垂直安装（优/良/差）
  - 轴-轴承组装后是否旋转运动顺畅（合格/不合格）
  - 是否遵守 BOM 中明确的零件额定值及型号规格 [B10, B11, B12, B13, B14]
quiz:
- question: 使用 PC-CF 线材时必须使用硬化钢喷嘴的主要原因是？
  choices:
  - 防止碳纤维的磨损性导致黄铜喷嘴快速磨损
  - 线材熔点低，普通喷嘴无法打印
  - 为了增加打印件的表面光泽
  - 为了提高挤出速度
  answer_index: 0
  explanation: 碳纤维具有极高的磨损性，会快速损坏普通黄铜喷嘴，因此硬化钢喷嘴必不可少 [S19]。
- question: 使用 M3 热熔嵌件(Accu HTBI-M3-BR)时建议的引孔直径是？
  choices:
  - 3.0mm
  - 4.0mm
  - 4.4mm
  - 5.0mm
  answer_index: 1
  explanation: 数据手册建议的孔径为 4.0mm [S21]。
completion_criteria:
- 所有结构件均通过 FDM 3D 打印完成制作 [B10]
- 热熔嵌件准确安装在所有指定孔位 [B14]
- 铝轴与滑动轴承的组装游隙满足标准 [B11, B12]
- 锁紧时正确使用了指定的 M3 规格帽螺钉 [B13]
source_ids:
- S19
- S21
- S17
- S18
- S16
- S20
---

### 3D 打印及零部件加工理论

#### 碳纤维增强工程材料 (PC-CF)
PC(Polycarbonate)具有优异的刚性和耐热性，添加碳纤维的 PC-CF 线材可最大化刚性，适合制作结构件 [S19]。但由于碳纤维的磨损性，必须使用硬化钢喷嘴 [S19]，且需要 285°C 左右的高温打印 [S19]。

#### 精密组装用的嵌件及锁紧
为使塑料打印件能够反复拆装，使用热熔螺纹嵌件 [S21]。对于 M3 嵌件，必须在 CAD 设计阶段预先布置 4.0mm 直径的引孔，以确保精准定位 [S21]。此外，免润滑聚合物滑动轴承(iglide J)在与 8mm 铝轴组装时，其设计旨在压入后内径具有最佳游隙 [S17]，因此轴径 8mm 的公差管理至关重要 [S17, S18]。

#### 肌腱驱动结构
Dyneema SK78 纤维在 1.5mm 直径下具有 230 daN 的高断裂载荷和低于 1% 的伸长率 [S16]，是钢缆的优良替代品。由于肌腱在旋转轴处反复弯曲，设计圆角化的绞盘边缘以防止摩擦导致的断裂结构非常重要。
