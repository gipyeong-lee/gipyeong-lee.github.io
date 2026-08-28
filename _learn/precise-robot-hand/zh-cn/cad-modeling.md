---
layout: learn-module
title: 3D CAD 建模
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:precise-robot-hand:cad-modeling
translations:
- lang: ko
  url: /learn/precise-robot-hand/cad-modeling/
- lang: en
  url: /learn/en/precise-robot-hand/cad-modeling/
- lang: ja
  url: /learn/ja/precise-robot-hand/cad-modeling/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/cad-modeling/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/cad-modeling/
module_id: m3
permalink: /learn/zh-cn/precise-robot-hand/cad-modeling/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
translation_run_id: caccbaa06fab4625ac40bf6e780cd0cb
id: m3
slug: cad-modeling
phase_id: p1
estimated_hours: 15.0
prerequisites:
- m2
objectives:
- 理解 3D CAD 建模的设计限制及制造工艺 (FDM)。
- 学习利用 PC-CF 丝材提高结构刚性的技巧。
- 执行考虑热压嵌入螺母与轴承公差的精密组装设计。
worked_examples:
- '**嵌件孔设计**：由于Accu-components的M3嵌件外径为 4.4mm，在3D CAD中需为打印件建模 4.0mm 的引孔 [S23]。打印后加热插入嵌件，黄铜材料会嵌入塑料内部，形成牢固的M3内螺纹。'
- '**轴承外壳公差**：使用igus轴承JSM-0810-10时，10mm外壳孔应设计为在压入后内径与8mm精密轴紧密配合且无间隙。若过宽会产生轴向间隙，过窄则会导致轴承损坏，因此需通过试打印来调整公差
  [S19, S20]。'
lab:
  title: 精密连杆设计及组装验证
  steps:
  - 在 3D CAD 中设计提供的肌腱路径与关节机构并进行仿真。
  - 将 PC-CF 丝材加载至 FDM 打印机，使用硬化钢喷嘴进行打印 [S21]。
  - 确认打印件上的4mm引孔后，插入热压嵌件 [S23]。
  - 装配8mm铝轴与轴承，确认连杆的旋转自由度并测量间隙 [S19, S20]。
  - 使用万用表确认 3 个独立电源分支的保险丝座连接状态，并检查通电前保险丝安装是否正常 [S25, S26]。
  safety:
  - 全程佩戴防冲击护目镜。
  - 热压操作时注意烫伤，并在通风良好的地方作业。
  - 通电时务必使用固定夹具，绝对不要将手放入旋转部位。
  - 维护系统或接近系统时，必须物理断开 3 个电源适配器，并用万用表确认电压低于1V。
  deliverables:
  - 机器人手整体组装 3D CAD 模型文件
  - 包含嵌入件及轴承公差调整的设计验证报告
  - 各电源分支独立连接状态及保险丝安装检查照片
assignment:
  title: 机器人手机构设计与集成配线计划
  deliverables:
  - 包含所有连杆与关节的详细 3D CAD 设计文件
  - BOM 与设计一致性确认报告
  - 包含 3 个独立分支及保险丝布置的配线图
  rubric:
  - 3D设计是否遵守了增材制造公差及黄铜嵌件规格(4.4mm OD)？
  - 轴承外壳与轴之间的间隙是否合理？
  - 电气接线图中12V执行器电源与传感器电路是否分离，且每个分支是否设计了10A保险丝？
quiz:
- question: 针对 PC-CF 打印件模型，若需要螺纹，最合适的方法是什么？
  choices:
  - 直接在建模中输出螺纹。
  - 通过加热插入黄铜热压嵌入螺母。
  answer_index: 1
  explanation: 相比直接对 PC-CF 材料建模螺纹，为确保重复组装的再现性，建议使用黄铜热压嵌入螺母 [S23]。
- question: 配置 3 个独立12V电源分支时的注意事项是？
  choices:
  - 并联连接适配器的阳极 (+) 输出以增加电流容量。
  - 每个分支通过独立的10A保险丝保护以防过流。
  answer_index: 1
  explanation: 禁止并联独立电源适配器的阳极 (+) 输出，必须通过各分支独立保险丝进行保护 [S17, S26]。
- question: FSR 力传感器驱动应使用什么电源？
  choices:
  - OpenCR的 3.3V 传感器电源轨
  - 12V执行器电源轨
  answer_index: 0
  explanation: FSR分压电路必须从 3.3V 传感器电源轨获取电力，且必须与执行器电源分离 [S16]。
completion_criteria:
- 3D CAD 设计文件已按嵌入件与轴承规格准确编写。
- 配线图中确认了 3 个独立电源分支与保险丝配置。
- 提交了包含设计与验证报告的作业，并通过标准评分标准。
source_ids:
- S12
- S21
- S19
- S20
- S23
- S17
- S26
- S15
- S16
- S27
- S25
---

### 3D CAD建模与制造设计

为制作精密的 5 机械手，必须考虑FDM方式增材制造特性的设计(Design for Additive Manufacturing, DfAM)。碳纤维增强PC-CF长丝具有优异的机械刚性和尺寸稳定性，适合制作精密连杆 [S21]。

#### 核心设计注意事项
1. **公差管理及轴承安装**：使用8mm精密铝轴和igus JSM-0810-10 轴承时，需在设计中反映外壳孔径公差。由于轴承采用压入式(Press-fit)固定，孔内径应设计得比轴承外径(10mm)略小，以实现坚固的装配 [S19, S20]。
2. **紧固件设计**：PC-CF打印件不适合直接攻丝。为确保反复拆卸装配的重现性，使用HTBI-M3-BR黄铜热压螺纹嵌件。为此，设计时需布置4mm直径的引孔 [S23]。
3. **结构优化**：在肌腱驱动方式中，连杆可能会因张力而变形。应确保应力集中的关节部位壁厚，并将模型放置在有利于拉伸强度的层积方向上。

### 系统集成及安全
本项目的电气系统由 3 个独立的12V电源分支组成。为防止驱动执行器时出现过流，必须在每个分支安装10A ATOF保险丝，并按 4/4/3 的比例分配执行器以管理峰值电流 [S17, S26]。采集传感器信号时，FSR 402 传感器必须通过 3.3V 传感器电源轨的分压电阻生成ADC输入值，且必须与12V执行器电源完全分离 [S15, S16, S27]。
