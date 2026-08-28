---
layout: learn-module
title: ファームウェアおよび制御
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.ja
course_locale: ja
lang: ja
ref: learn:precise-robot-hand:firmware-control
translations:
- lang: ko
  url: /learn/precise-robot-hand/firmware-control/
- lang: en
  url: /learn/en/precise-robot-hand/firmware-control/
- lang: ja
  url: /learn/ja/precise-robot-hand/firmware-control/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/firmware-control/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/firmware-control/
module_id: m7
permalink: /learn/ja/precise-robot-hand/firmware-control/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
translation_run_id: 6887538d0dce4b0bbbe63a75ae59d8c4
id: m7
slug: firmware-control
phase_id: p3
estimated_hours: 10.0
prerequisites:
- m6
objectives:
- DYNAMIXELスマートアクチュエータの動作原理と制御プロトコル(Protocol 2.0)を理解する。
- OpenCRコントローラーの構造を把握し、センサーおよびアクチュエーターインターフェースを構成する。
- FSR電圧分圧回路を設計し、ADC信号処理過程を実装する。
- 状態機械(State Machine)を活用してロボットハンドの把持および制御ロジックをファームウェアで作成する。
worked_examples:
- '例題1: FSR ADC値の正規化。FSRセンサーがOpenCR ADCに接続され、0～4095(12ビット)範囲の値をするとき、これを0.0～1.0の力比率へ変換するコードを作成せよ。(式:
  `normalized = adc_value / 4095.0`)'
- '例題2: XM430位置制御命令。DYNAMIXEL SDKを使用して1番関節を2048(中央値)へ移動させる命令を構成せよ。 `packetHandler->write2ByteTxRx(portHandler,
  1, ADDR_GOAL_POSITION, 2048, &error);` のような呼び出し体系を使用する。'
lab:
  title: ロボットハンドファームウェア実装およびセンサー補正
  steps:
  - OpenCR 1.0ボードをPCとUSBで接続し、基本通信環境を設定する [S16]。
  - 各指に接続されたFSR分圧回路をOpenCRの3.3Vセンサー電源レールにはんだ付けして接続する [S16, S27]。
  - マルチメーターを使用してFSR無負荷時および加圧時に電圧が0-3.3V範囲内にあるか確認する。
  - ファームウェアからセンサー値を読み取ってシリアルモニターに出力し、物理的接触時の変化を確認する。
  - 単一アクチュエーターを固定治具に接続し、制御コードを通じて精密移動を試験する。
  safety:
  - 絶対に5Vまたは12Vアクチュエーター電源レールをADCセンサー回路に直接接続しない [S16]。
  - 電源投入前に配線図を再確認し、短絡の有無をマルチメーターで確認する。
  - アクチュエーター無負荷状態で初期稼働試験を遂行する。
  - 異常発熱・臭気・煙を感知した場合は接近せず、危険区域外の事前指定された建物分電盤ブレーカー、または認証されたupstream master disconnectで3個のアダプターの供給電源を遮断した後に退避する。危険区域外で操作可能なupstream遮断手段がない場合、システムの通電を禁ずる。トルクオフは電源遮断の代わりにはならない。整備・接近は計画停止後、物理的分離および無電源計測確認後にのみ行う
    [S17]
  - 接近する前に3個の電源アダプターを物理的に取り外し、DC電圧モードで各分岐の電圧が1V未満であることを確認する。
  deliverables:
  - センサーデータ出力シリアルログ
  - 動作試験および校正済みのファームウェアソースコード
  - ADC正規化数式定義書
assignment:
  title: 5指ロボットハンドシステム統合制御報告書
  deliverables:
  - 状態機械設計図およびロジック詳細技術書
  - 全11個のアクチュエーターおよび5個のセンサー統合制御ファームウェア
  - 動作検証動画および把持力分析グラフ
  rubric:
  - 状態機械が安全に把持および解除ループを実行しているか？
  - センサーデータがノイズなく安定的に取得されているか？
  - 電源分岐ごとの設計がBOMの独立分岐原則を遵守しているか？
  - 安全規則（物理的な電源分離など）を遵守し、記録しているか？
quiz:
- question: OpenCRコントローラーでFSR電圧分圧回路のために使用しなければならない電源レールは？
  choices:
  - 12Vアクチュエーター電源
  - 3.3Vセンサー電源
  - 5V電源
  - USB 5V
  answer_index: 1
  explanation: OpenCRマニュアルと互換性基準に従い、FSR電圧分圧は3.3Vセンサー電源レールのみを使用しなければならない [S16]。
- question: アクチュエーター電源分岐アダプターが3個である状況において、正しい電源接続方法は？
  choices:
  - 3個のアダプターの正(+)出力を並列に接続して電流容量を増やす。
  - 各アダプターを独立した分岐として構成し、ヒューズを通す。
  - 1個のアダプターにすべてのアクチュエーターを接続し、残りは予備とする。
  - アダプターの出力を組み合わせて36Vに昇圧して使用する。
  answer_index: 1
  explanation: 正(+)出力の並列接続は禁止されており、各アダプターは独立した分岐として維持し、ヒューズを通じて過電流を保護しなければならない [S17]。
- question: ロボットハンドシステムの整備または接近前に実行しなければならない必須ステップは？
  choices:
  - ソフトウェアのトルク解除命令のみを行う。
  - ヒューズを取り外す。
  - 3個の電源を物理的に分離し、マルチメーターで各分岐の1V未満の電圧を確認する。
  - コントローラーのResetボタンを押す。
  answer_index: 2
  explanation: トルク解除は電源遮断の代わりにはならず、必ず3個のアダプターを取り外し、DC電圧計測で確認しなければならない。
completion_criteria:
- 統合制御ファームウェアが5指ロボットハンドの把持動作をループ内で実行していること。
- すべてのセンサーがADC信号を0-3.3Vの範囲内で正常に取得していること。
- すべての電気的接続が、ヒューズを含む独立分岐設計基準を満たしていること。
- 安全レビュー報告書に、無電源計測確認の記録が含まれていること。
source_ids:
- S16
- S14
- S15
- S27
- S17
---

## DYNAMIXELスマートアクチュエータ制御
ロボットハンドの各関節はXM430-W350-Tアクチュエータを使用して駆動される [S14]。このアクチュエータは位置、速度、電流フィードバックをリアルタイムで提供し、DYNAMIXEL Protocol 2.0を通じて制御される [S14]。コントローラであるOpenCR 1.0は216MHz ARM Cortex-M7プロセッサを搭載し、別途の通信ブリッジなしに直接アクチュエータと通信する [S16]。

## ADCおよびセンサインターフェース
指先の接触力はFSR 402センサを使用して測定する [S15]。FSRは印加された力が強まるにつれて抵抗が減少する特性を持つ [S15]。OpenCRのADC入力解像度は12ビットであり [S16]、3.3Vセンサ電源レールを使用して電圧分圧回路を構成する [S16, S27]。

10 kΩプルダウン分圧器は$V_{out}=V_{ref}\frac{R_{fixed}}{R_{FSR}+R_{fixed}}$を使用する

ここで$R_{fixed}$は10kΩ抵抗を使用する [S27]。安全のためにすべてのアナログ信号は0-3.3V範囲を超えないように設計されなければならない [S16]。

## ファームウェア構造
ロボットハンドの制御システムは「待機」、「把持遂行」、「把持維持」、「解除」の状態機械で具現する。ファームウェアはループ内でセンサ値を周期的にポーリングし、アクチュエータの電流および位置データを分析して安定した把持力を維持する。
