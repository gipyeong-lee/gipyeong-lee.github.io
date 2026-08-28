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
translation_run_id: 75a701fd44954c3a8681a8f795bedc7d
id: M4
slug: 3d-printing-assembly
phase_id: P2
estimated_hours: 15.0
prerequisites:
- M3
objectives:
- 炭素繊維補強 PC フィラメント(PC-CF)を使用した部品製作および出力設定最適化の理解
- 熱圧入インサート(Heat-set insert)およびスリーブベアリングの精密組み立て公差管理の習得
- 腱駆動メカニズムのための Dyneema ライン取り扱いおよびキャプスタン設計構造の理解
- ロボット構造物の寸法安定性と剛性確保のための加工および締結技法の熟知
worked_examples:
- '例題 1: PC-CF フィラメントノズルの選定 - 炭素繊維の高い摩耗度を考慮するとき、Brass(真鍮)ノズルは急速に摩耗して出力品質低下とノズル詰まりを誘発するため、必ず硬化鋼(Hardened
  steel)ノズルを選択しなければならないことを確認 [S19]。'
- '例題 2: インサートホール設計 - Accu HTBI-M3-BR インサートの外径が 4.4mm だが、公式推奨穴直径は 4.0mm であるため [S21]、CAD
  設計時に穴直径を 4.0mm に固定して熱圧入時にプラスチックがインサート・ナーリング(knurling)の間へ十分に食い込むようにする [S21]。'
lab:
  title: 指構造物製作および組み立て実習
  steps:
  - 硬化鋼ノズルを装着した FDM 3D プリンタで炭素繊維 PC フィラメント出力環境設定 [S19]。
  - 指リンクと手のひらフレーム出力後、サポート除去および表面整理。
  - 4.0mm パイロットホールに熱圧入インサートをホットツールで垂直定着 [S21]。
  - IGUS 精密アルミニウムシャフトをベアリング規格に合わせて切断および端面モデリング [S18]。
  - スリーブベアリングをハウジングに圧入後、シャフトを挿入して隙間を確認 [S17]。
  - M3 キャップスクリューで構造物およびセンサブラケットを締結 [S20]。
  safety:
  - 高温のノズル(285°C)およびベッド(110°C)による火傷に注意 [S19]。
  - 出力物後加工および面取り時は保護メガネ着用必須。
  - インサート加熱時に煙が発生する可能性があるため、換気施設を稼働。
  - 電源投入前にすべての機械的締結状態を確認。
  deliverables:
  - 製作された 5 指ロボットハンド構造物(リンク、手のひら)。
  - 熱圧入インサートの垂直度およびベアリングの隙間測定記録。
  - 最終締結部肉眼検査完了レポート。
assignment:
  title: ロボットハンド製作精度検証
  deliverables:
  - 完成した構造物の CAD データと実寸法測定比較表
  - 組み立て公差管理計画書
  - 腱ラウティング構造の摩擦低減設計説明書
  rubric:
  - 熱圧入インサートの垂直定着の有無 (上/中/下)
  - シャフト・ベアリング組み立て後の円滑な回転運動の有無 (合格/不合格)
  - BOM に明示された部品定格およびモデル規格遵守の有無 [B10, B11, B12, B13, B14]
quiz:
- question: PC-CF フィラメント使用時、硬化鋼ノズルを使用しなければならない主な理由は？
  choices:
  - 炭素繊維の摩耗性による真鍮ノズルの急激な摩耗防止
  - フィラメントの融点が低く、一般ノズルでは出力不可
  - 出力物の表面光沢を増大させるため
  - 押出速度を高めるため
  answer_index: 0
  explanation: 炭素繊維は非常に高い摩耗性を持ち、一般的な真鍮ノズルを急速に破損させるため、硬化鋼ノズルが必須です [S19]。
- question: M3 熱圧入インサート(Accu HTBI-M3-BR)使用時、推奨されるパイロットホール直径は？
  choices:
  - 3.0mm
  - 4.0mm
  - 4.4mm
  - 5.0mm
  answer_index: 1
  explanation: 公式データシートで推奨される穴直径は 4.0mm です [S21]。
completion_criteria:
- すべての構造用部品が FDM 3D プリンタで製作完了 [B10]
- 熱圧入インサートがすべての指定された穴に正確に定着 [B14]
- アルミニウムシャフトとスリーブベアリングの組み立て隙間が基準値を満足 [B11, B12]
- 締結時、明示された M3 規格のキャップスクリューが正しく使用された [B13]
source_ids:
- S19
- S21
- S17
- S18
- S16
- S20
---

### 3D プリントおよび部品加工理論

#### 炭素繊維強化エンジニアリング素材 (PC-CF)
PC(Polycarbonate)は高剛性と耐熱性に優れており、ここに炭素繊維が添加された PC-CF フィラメントは剛性を極大化するため、構造部品の製作に適している [S19]。ただし、炭素繊維の摩耗性により、必ず硬化鋼ノズルを使用しなければならず [S19]、285°C 前後の高温出力が必要である [S19]。

#### 精密組み立てのためのインサートおよび締結
プラスチック出力物に反復的な組み立て・分解を可能にするため、熱圧入ネジ山インサートを使用する [S21]。M3 インサートの場合、4.0mm 直径のパイロットホールを CAD 設計時にあらかじめ配置し、正確な位置に定着させなければならない [S21]。また、無給油ポリマー・スリーブベアリング(iglide J)は 8mm アルミニウムシャフトと組み立てられる際、圧入後に内径が最適な隙間を持つよう設計されており [S17]、軸径 8mm との公差管理が必須である [S17, S18]。

#### 腱駆動構造
Dyneema SK78 繊維は 1.5mm 直径で 230 daN の高い破断荷重と 1% 未満の伸度を示し [S16]、鋼鉄ケーブルの優れた代替材である。腱は回転軸から屈曲が繰り返されるため、キャプスタン端をラウンド処理して摩擦による断線を防止する構造設計が重要である。
