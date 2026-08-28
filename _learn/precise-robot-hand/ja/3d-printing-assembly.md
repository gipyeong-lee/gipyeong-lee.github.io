---
layout: learn-module
title: 3D プリントおよび部品加工
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.ja
course_locale: ja
lang: ja
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
permalink: /learn/ja/precise-robot-hand/3d-printing-assembly/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: 541c3acee16e441bbae3b5125876cfe4
id: M4
slug: 3d-printing-assembly
phase_id: P2
estimated_hours: 15.0
prerequisites:
- M3
objectives:
- 炭素繊維補強 PC フィラメント（PC-CF）を使用した部品製作およびプリント設定最適化の理解
- 熱圧入インサート（Heat-set insert）およびスリーブベアリングの精密組立公差管理の習得
- 腱駆動メカニズムのための Dyneema ラインの取り扱いおよびキャプスタン設計構造の理解
- ロボット構造物の寸法安定性と剛性確保のための加工および締結技法の熟知
worked_examples:
- '例題 1: PC-CF フィラメント用ノズルの選択 - 炭素繊維の高い摩耗度を考慮すると、Brass（真鍮）ノズルは急速に摩耗してプリント品質低下やノズル詰まりを誘発するため、必ず硬化鋼（Hardened
  steel）ノズルを選択しなければならないことを確認 [S19]。'
- '例題 2: インサート穴の設計 - Accu HTBI-M3-BR インサートの外径が 4.4mm だが公式推奨穴径は 4.0mm であるため [S21]、CAD
  設計時に穴径を 4.0mm に固定して熱圧入時にプラスチックがインサートのナーリング（knurling）間に十分入り込むようにする [S21]。'
lab:
  title: 指構造物製作および組立実習
  steps:
  - 硬化鋼ノズルを装着した FDM 3Dプリンタで炭素繊維 PC フィラメントプリント環境を設定 [S19]。
  - 指リンクと手のひらフレームを出力後、サポート除去および表面整理。
  - 4.0mm パイロット穴に熱圧入インサートをホットツールで垂直設置 [S21]。
  - IGUS 精密アルミニウムシャフトをベアリング規格に合わせて切断および端面取り [S18]。
  - スリーブベアリングをハウジングに圧入後、シャフトを挿入してガタつきを確認 [S17]。
  - M3 キャップスクリューで構造物およびセンサブラケットを締結 [S20]。
  safety:
  - 高温のノズル（285°C）およびベッド（110°C）による火傷に注意 [S19]。
  - 出力物の後加工および面取り時には保護メガネ着用必須。
  - インサート加熱時に煙が発生する可能性があるため、換気設備を稼働。
  - 通電前にすべての機械的締結状態を確認。
  deliverables:
  - 製作された 5 指ロボットハンド構造物（リンク、手のひら）。
  - 熱圧入インサートの垂直度およびベアリングのガタつき測定記録。
  - 最終締結部目視検査完了報告書。
assignment:
  title: ロボットハンド製作精度検証
  deliverables:
  - 完成した構造物の CAD データと実測値の比較表
  - 組立公差管理計画書
  - 腱ルーティング構造の摩擦低減設計説明書
  rubric:
  - 熱圧入インサートの垂直着座の有無 (上/中/下)
  - シャフト・ベアリング組立後のスムーズな回転運動の有無 (合格/不合格)
  - BOMに明示された部品定格およびモデル規格の遵守有無 [B10, B11, B12, B13, B14]
quiz:
- question: PC-CF フィラメント使用時に硬化鋼ノズルを使用しなければならない主な理由は？
  choices:
  - 炭素繊維の摩耗性による真鍮ノズルの急速な摩耗防止
  - フィラメントの融点が低く、通常のノズルでは出力不可
  - 出力物の表面光沢を増大させるため
  - 押出速度を速めるため
  answer_index: 0
  explanation: 炭素繊維は非常に高い摩耗性を持ち、通常の真鍮ノズルを急速に破損させるため、硬化鋼ノズルが必須です [S19]。
- question: M3 熱圧入インサート（Accu HTBI-M3-BR）使用時に推奨されるパイロット穴径は？
  choices:
  - 3.0mm
  - 4.0mm
  - 4.4mm
  - 5.0mm
  answer_index: 1
  explanation: 公式データシートで推奨される穴径は 4.0mm です [S21]。
completion_criteria:
- すべての構造部品が FDM 3Dプリンタで製作完了 [B10]
- 熱圧入インサートがすべての指定された穴に正確に設置済み [B14]
- アルミニウムシャフトとスリーブベアリングの組立ガタつきが基準値を満たしている [B11, B12]
- 締結時に明示された M3 規格のキャップスクリューが正しく使用されている [B13]
source_ids:
- S19
- S21
- S17
- S18
- S16
- S20
---

### 3Dプリントおよび部品加工理論

#### 炭素繊維強化エンジニアリング素材 (PC-CF)
PC(Polycarbonate)は高剛性と耐熱性に優れており、ここに炭素繊維が添加されたPC-CFフィラメントは剛性を極大化し、構造用部品の製作に適しています [S19]。ただし、炭素繊維の摩耗性のため、必ず硬化鋼ノズルを使用しなければならず [S19]、 285°C前後の高温出力が必要です [S19]。

#### 精密組立のためのインサートおよび締結
プラスチック出力物に繰り返しの組立・分解を可能にするため、熱圧入ネジ山インサートを使用します [S21]。M3インサートの場合、 4.0mm直径のパイロットホールをCAD設計時にあらかじめ配置し、正確な位置に着座させる必要があります [S21]。また、無給油ポリマーすべり軸受(iglide J)は、8mmアルミニウムシャフトと組み立てられる際、圧入後に内径が最適な隙間を持つように設計されており [S17]、軸直径8mmとの公差管理が必須です [S17, S18]。

#### 腱駆動構造
Dyneema SK78繊維は 1.5mm直径で 230 daNの高い破断荷重と 1% 未満の伸び率を示し [S16]、鋼製ケーブルの優れた代替材です。腱は回転軸で屈曲が繰り返されるため、キャプスタン端を丸める処理を行い、摩擦による断線を防止する構造設計が重要です。
