---
layout: learn-module
title: 駆動機およびコントローラの選定
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.ja
course_locale: ja
lang: ja
ref: learn:precise-robot-hand:actuator-controller-selection
translations:
- lang: ko
  url: /learn/precise-robot-hand/actuator-controller-selection/
- lang: en
  url: /learn/en/precise-robot-hand/actuator-controller-selection/
- lang: ja
  url: /learn/ja/precise-robot-hand/actuator-controller-selection/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/actuator-controller-selection/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/actuator-controller-selection/
module_id: M3
permalink: /learn/ja/precise-robot-hand/actuator-controller-selection/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: 75a701fd44954c3a8681a8f795bedc7d
id: M3
slug: actuator-controller-selection
phase_id: P1
estimated_hours: 10.0
prerequisites:
- M2
objectives:
- DYNAMIXEL XM430-W350-T アクチュエータの定格電圧、電流、および通信特性を理解する。
- OpenCR 1.0 コントローラの DYNAMIXEL ポート構成および 12V 電源分離構造を熟知する。
- FSR 402 センサと 10kΩ 抵抗を用いた電圧分圧回路を設計する。
- システム電力要件を計算し、独立分岐ヒューズ保護設計を樹立する。
worked_examples:
- '例題 1: 分岐あたりの最大電流確認。分岐一つに 4 個の XM430 アクチュエータを接続する場合、ストール電流の合計は 4 * 2.3A = 9.2A である。これはアダプタの
  11.5A 定格およびインラインヒューズの 10A 定格を満たし、安全な範囲を維持する [S11, S15, S25]。'
- '例題 2: FSR 分圧回路電圧計算。3.3V 供給電圧下で FSR 抵抗が R_fsr のとき、ADC 入力電圧 V_adc = 3.3 * (10k /
  (10k + R_fsr)) V となる。センサ範囲(0.2N～20N)に応じて抵抗変化を確認し、0～3.3V 範囲を超えないように補正する [S12, S13,
  S26]。'
lab:
  title: 電源分岐構成および ADC センサインターフェース実習
  steps:
  - 各 MEAN WELL アダプタ出力に 0AFH0001Z ヒューズホルダーを接続し、0287010 10A ヒューズを挿入する。
  - マルチメータを DC 電圧モードに設定し、各分岐の電圧が安定した 12V であることを確認する。
  - OpenCR の 3.3V センサレールに 10kΩ 抵抗と FSR 402 を使用して分圧回路を構成する。
  - 非通電状態で、分圧回路の出力電圧が 0～3.3V 範囲内にあるか確認する。
  safety:
  - 作業開始前には 3 個のアダプタの AC 電源を物理的に遮断し、マルチメータで 0V であることを確認する。
  - 耐衝撃作業用保護メガネを常時着用すること。
  - 電源投入中は、絶対に回路を変更したり配線に触れたりしないこと。
  - ヒューズは過電流遮断用であり、計画停止手段ではないことを明示する。
  deliverables:
  - 各分岐別の 12V 出力測定値記録用紙
  - FSR 分圧回路組み立て完了写真
  - 構成された配線図
assignment:
  title: 電源分岐および保護設計レビュー
  deliverables:
  - ロボットハンド全体の電流分岐分配表(各分岐別の割り当て)
  - 選定したヒューズがアクチュエータのストール電流を保護しながらアダプタ容量を超過しないことを証明する計算書
  rubric:
  - 独立ヒューズが各分岐に正確に配置されているか？
  - アクチュエータ分岐配分が 4/4/3 で規定に合致するか？
  - センサ電源が 12V ではなく 3.3V センサレールから供給されているか？
quiz:
- question: FSR 402 センサと 10kΩ 抵抗を使用した分圧回路の正しい電源接続は？
  choices:
  - 12V アクチュエータ電源
  - OpenCR 3.3V センサレール
  - 5V 汎用電源
  - OpenCR 12V 出力
  answer_index: 1
  explanation: OpenCR の ADC 入力は 3.3V を基準に動作するため、電圧分圧回路は必ず 3.3V センサレールから電源を供給されなければなりません
    [S13]。
- question: XM430-W350-T アクチュエータのストール電流値は？
  choices:
  - 1.0A
  - 2.3A
  - 4.1A
  - 11.5A
  answer_index: 1
  explanation: データシートによると、当該アクチュエータのストール電流は 2.3A です [S11]。
- question: 電源分岐設計において絶対禁止されている行為は？
  choices:
  - 各アダプタ出力へのヒューズ装着
  - アダプタの陽(+)出力の並列接続
  - 分岐あたり 10A ヒューズの使用
  - 絶縁型アダプタの使用
  answer_index: 1
  explanation: アダプタの陽(+)出力は独立した分岐として維持しなければならず、並列接続は絶対禁止です [B3]。
completion_criteria:
- 実習において 3 個の独立分岐の 12V 電圧をマルチメータで検証完了
- FSR 402 センサ分圧回路の配線と ADC 入力電圧範囲確認完了
- 電源分岐および保護設計レポート提出および合格
source_ids:
- S4
- S5
- S11
- S13
- S15
- S24
- S25
- S12
- S26
---

### 駆動機およびコントローラシステム設計理論

#### 1. アクチュエータ選定および電力特性
ロボットハンドの精密駆動のために DYNAMIXEL XM430-W350-T を使用する。このアクチュエータは 12V 定格電圧で動作し、ストール(Stall)電流は 2.3A である [S11]。ロボットハンド全体は 11 個のアクチュエータで構成されるため、全ストール電流合計は約 25.3A に達する。したがって安定した駆動のために独立した電源供給体系が必要である。

#### 2. コントローラアーキテクチャ
OpenCR 1.0 は 216MHz ARM Cortex-M7 プロセッサを搭載しており、リアルタイム制御に適している [S13]。このコントローラは、12V アクチュエータ電源とロジック/センサ電源を物理的に分離できる構造をサポートする。FSR センサのようなアナログ入力は 0～3.3V 範囲内で処理しなければならないため、センサ電圧分圧回路は必ず OpenCR の 3.3V センサレールから供給されなければならない [S13]。

#### 3. 過電流保護および電源分岐設計
138W 出力の MEAN WELL GST160A12-R7B アダプタ 3 個を使用する [S15]。各アダプタの定格電流は 11.5A であり、これを通じて独立した 12V 分岐を 3 個生成する。各分岐には 10A ATOF ヒューズをインラインで装着し、過電流発生時に回路を保護する [S24, S25]。ヒューズは定格電流 11.5A より低く設定し、保護協調を達成する。

#### 4. センサ信号取得
FSR 402 は、圧力が上昇すると抵抗が減少する特性を持つ [S12]。これを 10kΩ 固定抵抗と電圧分圧器に接続して力の変化を電圧信号に変換し、OpenCR の 12bit ADC ポートへ入力する [S12, S13, S26]。
