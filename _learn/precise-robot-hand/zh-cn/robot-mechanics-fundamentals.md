---
layout: learn-module
title: 机器人运动学基础
course_slug: precise-robot-hand
course_data_key: precise-robot-hand-zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:precise-robot-hand:robot-mechanics-fundamentals
translations:
- lang: ko
  url: /learn/precise-robot-hand/robot-mechanics-fundamentals/
- lang: en
  url: /learn/en/precise-robot-hand/robot-mechanics-fundamentals/
- lang: ja
  url: /learn/ja/precise-robot-hand/robot-mechanics-fundamentals/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/robot-mechanics-fundamentals/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/robot-mechanics-fundamentals/
module_id: M1
permalink: /learn/zh-cn/precise-robot-hand/robot-mechanics-fundamentals/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: e8f8435646734ebd8e061d010c356c2d
id: M1
slug: robot-mechanics-fundamentals
phase_id: P1
estimated_hours: 10.0
prerequisites: []
objectives:
- 理解机器人运动学的基本定义及刚体变换(Rigid-body transformation)的概念。
- 学习利用坐标系变换和旋转矩阵对机器人位置和方向进行数学描述的方法。
- 掌握 5 仿生机器人手设计所需的运动学基础理论及解析方法。
worked_examples:
- '示例 1: 在 2 维平面上，求具有 1 个旋转关节(Rotation Joint)的机器人连杆末端位置 $(x, y)$。当关节角度为 $\theta$ 且连杆长度为
  $L$ 时，$x = L \cos(\theta)$, $y = L \sin(\theta)$ [S1]。'
- '示例 2: 描述绕 $x$ 轴旋转 $\theta$ 的 2 维旋转矩阵 $R$。$R = \begin{bmatrix} \cos(\theta) & -\sin(\theta)
  \\ \sin(\theta) & \cos(\theta) \end{bmatrix}$ [S1]。'
lab:
  title: 坐标系变换仿真及基础运动学解析
  steps:
  - 利用运动学解析软件创建 2 连杆平面机械臂模型。
  - 改变关节角度并确认末端位置的轨迹。
  - 手动推导逆运动学计算公式，并与仿真结果进行对比。
  safety:
  - 计算机作业时调节屏幕亮度，并定期休息。
  - 本实验基于仿真，不需要硬件通电。
  deliverables:
  - 包含运动学解析过程的总结报告
  - 轨迹仿真结果图像
assignment:
  title: 5 仿生机器人手关节结构运动学建模
  deliverables:
  - 机器人手指 1 个的正运动学方程推导结果
  - 随关节角度变化而变化的指尖位置预测数据
  rubric:
  - 旋转矩阵的数学准确性
  - 正运动学方程的物理合理性
  - 报告的逻辑构成
quiz:
- question: 在机器人运动学中，不考虑力和转矩而仅描述运动的学科是什么？
  choices:
  - 动力学(Dynamics)
  - 运动学(Kinematics)
  - 控制理论(Control Theory)
  - 材料力学(Material Mechanics)
  answer_index: 1
  explanation: 运动学是以位置、速度、加速度为中心的动力论，不包含力和转矩 [S1]。
- question: 在 3 维空间中，定义两个坐标系之间方向的矩阵是什么？
  choices:
  - 旋转矩阵(Rotation Matrix)
  - 质量矩阵(Mass Matrix)
  - 刚度矩阵(Stiffness Matrix)
  - 阻尼矩阵(Damping Matrix)
  answer_index: 0
  explanation: 旋转矩阵是数学上转换两个坐标系间方向的正交矩阵 [S1]。
completion_criteria:
- 完成理论课程学习
- 提交运动学解析结果报告
- 理论测验达到 100 分
source_ids:
- S1
---

## 机器人运动学基础

机器人运动学是研究机器人运动的学科，在不考虑力和转矩的情况下，从位置、速度、加速度的角度进行处理 [S1]。像机器人手这类机械臂设计的起点，是用空间坐标来描述各关节的状态。

### 1. 刚体变换 (Rigid-body Transformation)
机器人的每个连杆被视为刚体，从一个坐标系到另一个坐标系的变换表示为旋转(Rotation)与平移(Translation)的组合。在 3 维空间中，旋转矩阵(Rotation Matrix) $R$ 是正交矩阵，通过它定义两个坐标系之间的方向 [S1]。

### 2. 正运动学 (Forward Kinematics)
正运动学是在已知关节变量（角度或位置）时，计算机器人末端执行器(End-effector)位置和方向的过程。在 5 仿生机器人手中，通过手指关节角度($\theta_1, \theta_2, \dots, \theta_n$)计算指尖位置。

### 3. 逆运动学 (Inverse Kinematics)
逆运动学是在设定目标指尖位置时，求出实现该位置所需的各关节变量的过程。由于由非线性方程组成，可能存在无解或多解的情况 [S1]。
