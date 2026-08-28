---
layout: learn-module
title: 機器人機構學基礎
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-tw
course_locale: zh-tw
lang: zh-tw
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
permalink: /learn/zh-tw/precise-robot-hand/robot-mechanics-fundamentals/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: e74d4410eaaa46f38f5fb28134401a2a
id: M1
slug: robot-mechanics-fundamentals
phase_id: P1
estimated_hours: 10.0
prerequisites: []
objectives:
- 理解機器人機構學的基本定義與剛體變換 (Rigid-body transformation) 概念。
- 學習使用座標系變換與旋轉矩陣，以數學方式描述機器人的位置與方向。
- 習得 5 機器人手設計所需的機構學基礎理論與分析方法。
worked_examples:
- 例題 1：在 2 維平面中，求出具有 1 個旋轉關節 (Rotation Joint) 的機器人連桿末端位置 $(x, y)$。當關節角度為 $\theta$
  且連桿長度為 $L$ 時，$x = L \cos(\theta), y = L \sin(\theta)$ [S1]。
- 例題 2：描述繞 $x$ 軸旋轉 $\theta$ 的 2 維旋轉矩陣 $R$。$R = \begin{bmatrix} \cos(\theta) & -\sin(\theta)
  \\ \sin(\theta) \cos(\theta) \end{bmatrix}$ [S1]。
lab:
  title: 座標系變換模擬與基礎機構學分析
  steps:
  - 使用機構分析軟體建立 2 連桿平面機械臂模型。
  - 改變關節角度並確認末端位置的軌跡。
  - 手動推導反向機構學公式，並與模擬結果比較。
  safety:
  - 電腦作業時請調整螢幕亮度並定時休息。
  - 本實習為模擬基礎，不要求硬體通電。
  deliverables:
  - 包含機構分析過程的總結報告
  - 軌跡模擬結果影像
assignment:
  title: 5 機器人手關節結構機構建模
  deliverables:
  - 機器人手指 1 個的正向機構學方程式推導成果
  - 隨關節角度變化之指尖位置變化預測數據
  rubric:
  - 旋轉矩陣的數學精確度
  - 正向機構學方程式的物理合理性
  - 報告的邏輯架構
quiz:
- question: 在機器人機構學中，不考慮力或扭力，僅描述運動的學問為何？
  choices:
  - 動力學 (Dynamics)
  - 機構學 (Kinematics)
  - 控制理論 (Control Theory)
  - 材料力學 (Material Mechanics)
  answer_index: 1
  explanation: 機構學是排除力與扭力，以位置、速度與加速度為中心的運動學 [S1]。
- question: 在 3 維空間中，定義兩個座標系間方向的矩陣為何？
  choices:
  - 旋轉矩陣 (Rotation Matrix)
  - 質量矩陣 (Mass Matrix)
  - 剛性矩陣 (Stiffness Matrix)
  - 阻尼矩陣 (Damping Matrix)
  answer_index: 0
  explanation: 旋轉矩陣是將兩座標系方向進行數學變換的正交矩陣 [S1]。
completion_criteria:
- 完成理論課程學習
- 提交機構分析結果報告
- 達成理論測驗 100 分
source_ids:
- S1
---

## 機器人機構學基礎

機器人機構學是一門探討機器人運動，但不考慮力或扭力的學問，著重於位置、速度與加速度 [S1]。設計如機器人手等機械臂的起點，在於將各關節的狀態描述為空間中的座標。

### 1. 剛體變換 (Rigid-body Transformation)
機器人的各個連桿被視為剛體，從一個座標系變換到另一個座標系的過程，可表示為旋轉 (Rotation) 與移動 (Translation) 的組合。在 3 維空間中，旋轉矩陣 (Rotation Matrix) $R$ 為正交矩陣，藉此定義兩個座標系間的方向 [S1]。

### 2. 正向機構學 (Forward Kinematics)
正向機構學是指在已知關節變數（角度或位置）時，計算機器人末端執行器 (End-effector) 位置與方向的過程。在 5 機器人手中，透過手指關節角度 ($\theta_1, \theta_2, \dots, \theta_n$) 求出指尖位置。

### 3. 反向機構學 (Inverse Kinematics)
反向機構學是指設定期望的指尖位置為目標值後，求出達成該位置所需之各關節變數的過程。由於由非線性方程式構成，可能不存在解或產生多重解 [S1]。
