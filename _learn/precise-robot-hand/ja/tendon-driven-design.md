---
layout: learn-module
title: 腱駆動メカニズム設計
course_slug: precise-robot-hand
course_data_key: precise-robot-hand-ja
course_locale: ja
lang: ja
ref: learn:precise-robot-hand:tendon-driven-design
translations:
- lang: ko
  url: /learn/precise-robot-hand/tendon-driven-design/
- lang: en
  url: /learn/en/precise-robot-hand/tendon-driven-design/
- lang: ja
  url: /learn/ja/precise-robot-hand/tendon-driven-design/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/tendon-driven-design/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/tendon-driven-design/
module_id: M2
permalink: /learn/ja/precise-robot-hand/tendon-driven-design/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: 541c3acee16e441bbae3b5125876cfe4
primary_category: robotics-hardware
topics:
- robot-hands
- tendon-drive
- embedded-control
course_type: build_project
published_at: '2026-08-29T08:34:02+09:00'
id: M2
slug: tendon-driven-design
phase_id: P1
estimated_hours: 10.0
prerequisites:
- M1
objectives:
- 腱駆動メカニズムの基本力学構造と関節模倣原理を理解する。
- 精巧なロボットハンドのための腱材料（Dyneema SK78）の特性を学習する。
- 腱の張力伝達経路とキャプスタン設計時の摩擦および摩耗防止法を習得する。
- アクチュエータのストールトルクと腱駆動時の機械的利得を計算する。
worked_examples:
- '例題 1: 腱駆動時の張力計算

  アクチュエータトルク(τ)が 1 N·m、キャプスタン半径(r)が 0.01 mのとき、腱張力(T)は T = τ/r = 1/0.01 = 100 Nである。Dyneema
  SK78 の破断荷重 230 daN（約 2300 N）に対する安全率を考慮して設計する [S16]。'
- '例題 2: 電源分岐配分および保護

  アクチュエータ全 11 台のストール電流合計は 25.3 A である [S11]。これを 3 個の分岐に 4 台、4 台、3 台ずつ配分すると、各分岐の最大負荷はそれぞれ
  9.2 A、9.2 A、6.9 A となる。ヒューズと負荷・電源定格の比較だけでは安全性や動作順序を保証できない。ヒューズメーカーの時間-電流曲線と電源 OCP
  特性を併せて検討し、保護協調を確認すること。ヒューズメーカーの時間-電流曲線とアダプタ OCP 特性を併せて検討し、保護協調を確認すること [S24, S25]。'
lab:
  title: 腱張力および関節摩擦測定実習
  steps:
  - 提供されたリンクとベアリングを使用して指関節モデルを組み立てる。
  - 腱を接続し、テンショナーを使用して初期張力を設定する。
  - マルチメータを DC 電圧モードに設定し、各分岐の 12 V 電源アダプタ出力を物理的に分離して確認する。
  - 通電前に、関節の回転摩擦力を手動で測定し記録する。
  safety:
  - 整備・接近前には 3 個の絶縁電源アダプタを物理的に分離し、マルチメータで 1 V 未満の DC 電圧であることを確認する。
  - 通電中は決して指の可動範囲に近づかないこと。
  - 耐衝撃作業用保護メガネを必ず着用すること。
  deliverables:
  - 関節回転角度に応じた腱張力測定データ
  - 摩擦力分析レポート
  - 最終安全計測記録
assignment:
  title: 5 指ロボットハンド腱経路設計
  deliverables:
  - ロボット指の腱経路 CAD 図面
  - 腱の摩擦および損失計算書
  - 分岐別電源負荷配分およびヒューズ保護設計図
  rubric:
  - 腱経路が屈曲部の摩擦を最小化するように設計されているか？
  - Dyneema SK78の物理的特性が考慮されているか？
  - 3個の電源分岐の負荷配分が、アクチュエータのストール電流を適切に反映しているか？
  - ヒューズおよび電源短絡防止設計がBOM仕様を遵守しているか？
quiz:
- question: Dyneema SK78 腱を使用する際の主な利点は何か？
  choices:
  - 高い伸長率による衝撃吸収
  - 非常に低い動作伸長率と高い破断荷重
  - 金属より軽い重量と低い引張強度
  - 電気伝導性
  answer_index: 1
  explanation: Dyneema SK78 は伸長率が 1% 未満と非常に低く、位置制御の精度を高め、非常に高い破断荷重を持つ高性能繊維である [S16]。
- question: 3 個の 12 V 電源アダプタ（各 11.5 A）を使用する理由として適切なものは？
  choices:
  - すべてのシステムを一つの電源で駆動するため
  - 電圧を 36 V に増幅してトルクを高めるため
  - アクチュエータの総ピーク電流を分散収容し、個別の分岐ヒューズで保護するため
  - 電源ノイズを除去するため
  answer_index: 2
  explanation: ヒューズと負荷・電源定格の比較だけでは安全性や動作順序を保証できない。ヒューズメーカーの時間-電流曲線と電源 OCP 特性を併せて検討し、保護協調を確認すること
    [S11, S15, S25]。
completion_criteria:
- すべての実習データと図面が最終レポートに含まれていること。
- 物理的電源分離後、3 個の分岐の DC 電圧が 1 V 未満であることを計測で実証すること。
- 腱経路設計においてキャプスタン摩擦を考慮した解析が含まれていること。
source_ids:
- S9
- S10
- S16
- S11
- S15
- S24
- S25
---

## 腱駆動メカニズムの基礎

腱駆動(Tendon-driven)システムは、遠隔地に配置されたアクチュエータからの引張力を、腱（線）を通じて関節に伝達して駆動する方式である [S9]。生物学的な指の腱構造を模倣し、アクチュエータを手のひらや前腕に移動させることで、指自体の質量を減らし、精巧な動きを実現できる [S10]。

### 1. 腱の選択および張力伝達
本設計では、高強度・低伸長繊維であるDyneema SK78を使用する [S16]。この材料は直径 1.5 mmで 230 daN(約 230 kgf)の破断荷重を有し、作動伸び率が 1% 未満であり、精密な位置制御に適している [S16]。

### 2. 機械的利得と駆動機の選定
XM430-W350-T スマートアクチュエータは、ストールトルク 4.1 N·mを提供する [S11]。腱は回転軸からキャプスタン半径を通じて力を変換するため、アクチュエータのトルク出力は腱の張力に置換される。システム全体で 11台のアクチュエータを使用し、ピーク電流合計は約 25.3 Aに達する可能性がある [S11]。ヒューズと負荷・電源定格の比較のみで、安全性や動作順序を保証するものではない。ヒューズメーカーのタイム・電流曲線と電源OCP特性を併せて検討し、保護協調を確認する [S15, S24, S25]。

### 3. 安全および保護設計
各 12 V 電源分岐は、独立したヒューズを介して運用される [S15, S24]。 3個の電源アダプタはそれぞれ 11.5 A 定格であり、合計電流容量は 34.5 Aに達し、システムピーク電流である 25.3 Aを十分に許容する [S11, S15]。分岐合計定格がアクチュエータの総ピーク電流を上回るように設計し、運用安全性を確保する。
