---
layout: learn-module
title: 机器人运动学基础
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-cn
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
translation_run_id: 2b7c146b08954623a88a715bf8cc7d0e
id: M1
slug: robot-mechanics-fundamentals
phase_id: P1
estimated_hours: 10.0
prerequisites: []
objectives:
- 理解机器人运动学的基本定义及刚体变换（Rigid-body transformation）的概念。
- 学习使用坐标变换和旋转矩阵以数学方式描述机器人的位置和姿态的方法。
- 获取 5 级机器人手设计的运动学基础理论并掌握解析方法。
worked_examples:
- 例题 1：求在 2 维平面上具有 1 个旋转关节（Rotation Joint）的机器人连杆的末端位置 $(x, y)$。当关节角为 $\theta$ 且连杆长度为
  $L$ 时，$x = L \cos(\theta)$, $y = L \sin(\theta)$ [S1]。
- 例题 2：描述绕 $x$ 轴旋转 $\theta$ 的 2 维旋转矩阵 $R$。$R = \begin{bmatrix} \cos(\theta) & -\sin(\theta)
  \\ \sin(\theta) & \cos(\theta) \end{bmatrix}$ [S1]。
lab:
  title: 坐标系变换模拟及基础运动学解析
  steps:
  - 使用运动学解析软件创建 2 连杆平面操纵器模型。
  - 改变关节角度，确认末端位置的轨迹。
  - 手动推导逆运动学计算公式并与模拟结果进行比较。
  safety:
  - 进行计算机工作时，请调节屏幕亮度并定期休息。
  - 本实验基于模拟，无需硬件通电。
  deliverables:
  - 包含运动学解析过程的摘要报告
  - 轨迹模拟结果图像
assignment:
  title: 5 级机器人手关节结构运动学建模
  deliverables:
  - 机器人手指 1 个关节的正运动学方程推导结果
  - 根据关节角度变化预测指尖位置变化的数据
  rubric:
  - 旋转矩阵的数学准确性
  - 正运动学方程的物理合理性
  - 报告的逻辑结构
quiz:
- question: 在机器人运动学中，不考虑力或转矩，仅描述运动的学科是什么？
  choices:
  - 动力学 (Dynamics)
  - 运动学 (Kinematics)
  - 控制理论 (Control Theory)
  - 材料力学 (Material Mechanics)
  answer_index: 1
  explanation: 运动学是以位置、速度、加速度为中心的动力学，不含力与转矩 [S1]。
- question: 在 3 维空间中定义两个坐标系间方向的矩阵是？
  choices:
  - 旋转矩阵 (Rotation Matrix)
  - 质量矩阵 (Mass Matrix)
  - 刚度矩阵 (Stiffness Matrix)
  - 阻尼矩阵 (Damping Matrix)
  answer_index: 0
  explanation: 旋转矩阵是将两个坐标系间方向进行数学转换的正交矩阵 [S1]。
completion_criteria:
- 完成理论课程学习
- 提交运动学解析结果报告
- 理论测验达到 100 分
source_ids:
- S1
---

## 机器人运动学基础

机器人运动学是在不考虑力或转矩的情况下，从位置、速度、加速度的角度处理机器人运动的学科 [S1]。像机械手这类操纵器的设计起点是将每个关节的状态描述为空间坐标。

### 1. 刚体变换 (Rigid-body Transformation)
机器人的每个连杆均被视为刚体，从一个坐标系到另一个坐标系的转换表现为旋转（Rotation）与平移（Translation）的组合。在 3 维空间中，旋转矩阵（Rotation Matrix） $R$ 为正交矩阵，通过它定义两个坐标系间的方向 [S1]。

### 2. 正运动学 (Forward Kinematics)
正运动学是在已知关节变量（角度或位置）的情况下，计算机器人末端执行器（End-effector）的位置和方向的过程。在 5 级机器人手中，通过手指关节角（$\theta_1, \theta_2, \dots, \theta_n$）来求取指尖位置。

### 3. 逆运动学 (Inverse Kinematics)
逆运动学是将目标指尖位置设定为目标值，并求解为此所需各关节变量的过程。由于其由非线性方程构成，可能存在无解或多解的情况 [S1]。
