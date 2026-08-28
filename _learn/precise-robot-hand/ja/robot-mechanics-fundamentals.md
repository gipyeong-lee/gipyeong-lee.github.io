---
layout: learn-module
title: ロボット機構学基礎
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.ja
course_locale: ja
lang: ja
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
permalink: /learn/ja/precise-robot-hand/robot-mechanics-fundamentals/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: 75a701fd44954c3a8681a8f795bedc7d
id: M1
slug: robot-mechanics-fundamentals
phase_id: P1
estimated_hours: 10.0
prerequisites: []
objectives:
- ロボット機構学の基本定義と剛体変換(Rigid-body transformation)の概念を理解する。
- 座標系変換と回転行列を使用して、ロボットの位置と方向を数学的に記述する方法を習得する。
- 5 指ロボットハンド設計のための機構学的基礎理論を習得し、解析的アプローチを習得する。
worked_examples:
- '例題 1: 2 次元平面において、1 個の回転関節(Rotation Joint)を持つロボットリンクの先端位置 $(x, y)$ を求めよ。関節角度が $\theta$
  でリンク長が $L$ のとき、$x = L \cos(\theta)$, $y = L \sin(\theta)$ である [S1]。'
- '例題 2: $x$ 軸に対して $\theta$ だけ回転する 2 次元回転行列 $R$ を記述せよ。$R = \begin{bmatrix} \cos(\theta)
  & -\sin(\theta) \\ \sin(\theta) & \cos(\theta) \end{bmatrix}$ である [S1]。'
lab:
  title: 座標系変換シミュレーションおよび基礎機構学解析
  steps:
  - 機構学解析ソフトウェアを使用して、2 リンク平面マニピュレータモデルを作成する。
  - 関節角度を変化させながら、先端位置の軌跡を確認する。
  - 逆機構学計算式を手動で導出し、シミュレーション結果と比較する。
  safety:
  - コンピュータ作業時は画面の明るさを調整し、定期的に休憩を取ること。
  - 本実習はシミュレーションベースであるため、ハードウェアへの通電は要求しない。
  deliverables:
  - 機構学解析過程を含んだ要約レポート
  - 軌跡シミュレーション結果画像
assignment:
  title: 5 指ロボットハンド関節構造機構学モデリング
  deliverables:
  - ロボット指 1 本に対する順機構学方程式の導出成果物
  - 関節角度変化による指先位置変化予測データ
  rubric:
  - 回転行列の数学的正確性
  - 順機構学方程式の物理的妥当性
  - レポートの論理的構成
quiz:
- question: ロボット機構学において、力やトルクを考慮せず運動のみを記述する学問は何か？
  choices:
  - 動力学(Dynamics)
  - 機構学(Kinematics)
  - 制御理論(Control Theory)
  - 材料力学(Material Mechanics)
  answer_index: 1
  explanation: 機構学は、力とトルクを除いた位置、速度、加速度中心の運動論です [S1]。
- question: 3 次元空間において、二つの座標系間の方向を定義する行列は？
  choices:
  - 回転行列(Rotation Matrix)
  - 質量行列(Mass Matrix)
  - 剛性行列(Stiffness Matrix)
  - 減衰行列(Damping Matrix)
  answer_index: 0
  explanation: 回転行列は、二つの座標系間の方向を数学的に変換する直交行列です [S1]。
completion_criteria:
- 理論講座の学習完了
- 機構学解析結果レポートの提出
- 理論クイズで 100 点達成
source_ids:
- S1
---

## ロボット機構学の基礎

ロボット機構学は、ロボットの運動を力やトルクを考慮せず、位置、速度、加速度の側面から扱う学問です [S1]。ロボットハンドのようなマニピュレータ設計の出発点は、各関節の状態を空間上の座標として記述することです。

### 1. 剛体変換 (Rigid-body Transformation)
ロボットの各リンクは剛体とみなされ、ある座標系から他の座標系への変換は、回転(Rotation)と移動(Translation)の組み合わせで表されます。3 次元空間において、回転行列(Rotation Matrix) $R$ は直交行列であり、これを通じて二つの座標系間の方向を定義します [S1]。

### 2. 順機構学 (Forward Kinematics)
順機構学は、関節の変数(角度または位置)を知っているとき、ロボット先端(End-effector)の位置と方向を計算する過程です。5 指ロボットハンドでは、指の関節角度($\theta_1, \theta_2, \dots, \theta_n$)を通じて指先位置を求めます。

### 3. 逆機構学 (Inverse Kinematics)
逆機構学は、希望する指先の位置を目標値に設定したとき、これを達成するための各関節変数を求める過程です。非線形方程式で構成されており、解が存在しなかったり、多重解が発生したりすることがあります [S1]。
