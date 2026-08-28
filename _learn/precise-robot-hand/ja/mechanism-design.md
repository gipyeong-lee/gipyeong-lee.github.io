---
layout: learn-module
title: ロボット機構設計
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.ja
course_locale: ja
lang: ja
ref: learn:precise-robot-hand:mechanism-design
translations:
- lang: ko
  url: /learn/precise-robot-hand/mechanism-design/
- lang: en
  url: /learn/en/precise-robot-hand/mechanism-design/
- lang: ja
  url: /learn/ja/precise-robot-hand/mechanism-design/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/mechanism-design/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/mechanism-design/
module_id: m2
permalink: /learn/ja/precise-robot-hand/mechanism-design/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
translation_run_id: 6887538d0dce4b0bbbe63a75ae59d8c4
id: m2
slug: mechanism-design
phase_id: p1
estimated_hours: 15.0
prerequisites:
- m1
objectives:
- ロボットハンド機構設計の核心原理であるアンダーアクチュエート(Underactuated)システムを理解する。
- テンドン駆動方式の動力学的特性と摩擦および伸長率管理の重要性を学習する。
- 剛性と寸法安定性を考慮したエンジニアリング素材(PC-CF)の選択および設計技法を習得する。
- 熱圧入インサートとベアリングを活用した精密組み立て設計の基礎を固める。
worked_examples:
- 例題1：腱張力伝達分析。腱の作動伸率が1%の場合、100 mmの距離で1 mmの誤差が発生します。精密制御のためにはアクチュエータの電流フィードバックとセンサデータを活用した閉ループ制御が必須です
  [S14]。
- 例題2：インサート締結部設計。PC-CF出力物にHTBI-M3-BRインサートを挿入する際、推奨パイロットホール直径である4 mmをCAD設計時に必ず遵守しなければ、遊びのない組み立ては不可能です
  [S23]。
lab:
  title: ロボット関節およびテンドンモジュールの組み立て実習
  steps:
  - 保護メガネを着用し、作業台を整理します。
  - PC-CF出力物のパイロットホールの状態を確認し、必要に応じて加工します。
  - 熱圧入インサートをはんだごてで加熱し、出力物に垂直に圧入します。
  - igusベアリングを手首および関節ハウジングに装着します。
  - アルミシャフトをベアリングに通し、ガタを確認します。
  - Dyneemaテンドンをキャプスタンに巻き、組み立てられた関節に固定します。
  safety:
  - はんだごて使用時は高温に注意し、保護メガネを必ず着用します。
  - テンドン張力試験中、テンドン破断時の跳ね返り事故を防ぐため、可動範囲に手を入れません。
  - システム組み立て完了後、電源投入前に物理的分離状態を計測器で確認します。
  deliverables:
  - 組み立てられたロボット関節モジュール
  - ベアリングおよびシャフトのガタ測定記録
assignment:
  title: 5知ロボットハンド機構設計プロジェクト
  deliverables:
  - ロボットハンド全体のCAD組み立て図
  - 部品リスト(BOM)および選定根拠レポート
  - テンドン経路最適化設計図
  rubric:
  - 使用された部品が規格(BOM)を遵守しているか？
  - 熱圧入インサートおよびベアリング設計が適切か？
  - 機構的な干渉なしに自由な動きが実現されているか？
quiz:
- question: テンドン駆動でDyneema SK78を使用する主な理由は何ですか？
  choices:
  - 伸長率が大きく、価格が安いため
  - 低い伸長率と高い破断荷重を提供し、精度の確保が可能なため
  answer_index: 1
  explanation: Dyneema SK78は伸長率が1%未満と非常に低く、ロボット制御の繰り返し精度を高めてくれます [S18]。
- question: PC-CF出力物に繰り返しのねじ組み立てをするために推奨される方法は？
  choices:
  - 出力物に直接ねじ山を加工する
  - 真鍮熱圧入インサートを挿入する
  answer_index: 1
  explanation: 熱圧入インサートはPC-CFのようなエンジニアリングプラスチックにおいて、ねじ山の耐久性を大幅に向上させます [S23]。
completion_criteria:
- 各部品の規格と仕様をBOMに合わせて文書化完了
- 組み立て完了した関節モジュールの機能的な動きを確認
- 安全指針を遵守し、実習を完遂した
source_ids:
- S3
- S11
- S18
- S21
- S23
- S19
- S14
---

## ロボット機構設計原理

精巧な5本指ロボットハンド設計の核心は、駆動器(Actuator)数より多い自由度(DoF)を効率的に制御するアンダーアクチュエイテッドシステムの実現にあります [S11]。これにより、関節数を無理に増やさなくても多様な形状の物体を安定して把持できます [S3]。

### 腱駆動動動力学
腱(Tendon)駆動は、遠隔モータの張力を関節に伝達する方式です。このとき、腱の物理的特性が制御の精密さを決定します。本課程では`Dyneema SK78`繊維を使用しており、これは直径1.5 mmで230 daNの高い破断荷重に耐え、作動伸率(Working stretch)が1%未満と非常に低いため繰り返し精度が優れています [S18]。

### 素材および構造設計
ロボットハンドのフレームとリンクには高い剛性と寸法安定性が求められます。FDM方式の`Prusament PC Blend Carbon Fiber`は炭素繊維が含まれたPC素材で、高温耐性と優れた強度を提供し、エンジニアリンググレードの部品製作に適しています [S21]。組み立て時、繰り返しの分解と再組み立てのために直接ねじ山を締結する代わりに、M3真鍮熱圧入インサート(外径4.4 mm、長さ5.8 mm)を使用してねじ山の耐久性を確保します [S23]。回転軸には無給油ポリマースリーブベアリング(JSM-0810-10)を使用し、メンテナンス不要で滑らかな回転と摩擦管理を実現します [S19]。
