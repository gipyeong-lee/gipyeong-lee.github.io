---
layout: learn-module
title: ロボット工学概論
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.ja
course_locale: ja
lang: ja
ref: learn:precise-robot-hand:intro-robotics
translations:
- lang: ko
  url: /learn/precise-robot-hand/intro-robotics/
- lang: en
  url: /learn/en/precise-robot-hand/intro-robotics/
- lang: ja
  url: /learn/ja/precise-robot-hand/intro-robotics/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/intro-robotics/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/intro-robotics/
module_id: m1
permalink: /learn/ja/precise-robot-hand/intro-robotics/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
translation_run_id: 6887538d0dce4b0bbbe63a75ae59d8c4
id: m1
slug: intro-robotics
phase_id: p1
estimated_hours: 10.0
prerequisites: []
objectives:
- ロボット工学の定義とシステム構成要素を理解する。
- 5知ロボットハンドのプロトタイプに使用されるアクチュエーターとコントローラーの役割を把握する。
- ロボットシステムの安全な電源分岐構成と物理的遮断原理を学習する。
- 力覚センサー(FSR)の動作原理とADCデータ取得方法を習得する。
worked_examples:
- アクチュエータ負荷計算：XM430-W350-Tを4台、1個の分岐に配置する場合、ピーク電流は4 * 2.3 A = 9.2 Aとなります [S14]。これは10
  Aヒューズの定格内であり、電源アダプタの11.5 A出力定格よりも小さいため安定した運用が可能です [S17, S26]。
- FSR電圧分圧器の設計：センサと10 kΩ抵抗を直列接続した分圧器において、3.3 V入力時、センサが押圧を受けず高抵抗状態のとき、ADCは0 Vに近い値を出力し、強い力を受けて抵抗が急減するとADCは3.3
  Vに近い値を出力します [S15, S27]。
lab:
  title: 電源分岐構成およびシステム基本通電試験
  steps:
  - 各MEAN WELLアダプタの陽(+)端子にATOインラインホルダと10 Aヒューズを接続し、3個の独立した分岐を生成する [S17, S25, S26]。
  - マルチメータをDC電圧モードに設定し、各分岐の出力電圧が12 Vであることを確認する。
  - OpenCRコントローラを3.3 Vセンサ電源レールに接続し、FSRセンサと10 kΩ抵抗を活用した分圧回路を構成する [S16, S27]。
  - コントローラーに電源を投入した後、各テンドンアクチュエーターが正常に通信しているかDYNAMIXEL Wizardで確認する [S14, S16]。
  safety:
  - 電源投入前、すべての結線をマルチメーターの抵抗モードではなく、目視と図面で再検証する。
  - 通電中はシステムへの接近を禁じ、必ず非通電状態(物理的なアダプター分離)で配線する。
  - 異常発熱・臭気・煙を感知した場合は接近せず、危険区域外の事前指定された建物分電盤ブレーカーまたは認証されたupstream master disconnectで3個のアダプターの供給電源を遮断した後に退避する。危険区域外で操作可能なupstream遮断手段がない場合、システムの通電を禁ずる。トルクオフは電源遮断の代わりにはならない。整備・接近は計画停止後、物理的分離および無電源計測確認後にのみ行う。
  - 保護メガネを常時着用し、可動範囲に身体の一部を入れない。
  deliverables:
  - 各分岐別の12 V測定記録写真
  - OpenCR ADCセンサーデータ取得コード
  - 独立分岐結線配線図
assignment:
  title: ロボットシステム安全設計レポート
  deliverables:
  - 独立電源分岐構成図
  - アクチュエーターピーク電流対ヒューズ定格妥当性分析
  - FSR電圧分圧回路設計値算出式
  rubric:
  - アクチュエーター11台と電源分岐3個の割り当てが明確か？
  - 3.3 Vセンサレールと12 Vアクチュエータレールの分離が正しく説明されているか？
  - 電源遮断手順(物理的分離)が正確に記述されているか？
quiz:
- question: システム電源設計時、12 V出力端子の陽(+)極を並列接続することが禁止される理由は何か？
  choices:
  - 電圧が24 Vに上昇するため
  - アダプター間の電位差による逆電流の発生および独立分岐保護破壊の危険
  - アクチュエーターの通信速度が低下するため
  - ソフトウェアによるトルクオフ機能を使用できないため
  answer_index: 1
  explanation: 各電源アダプターは独立した分岐として運用されなければならず、出力端子を結合する場合、故障したり独立ヒューズによる安全保護機能が無効化される危険があります。
- question: OpenCRのADCポートでFSR信号を読み取る際の適切な供給電圧は？
  choices:
  - 12 Vアクチュエータレール
  - 3.3 Vセンサレール
  - 24 V入力電源
  - 非接触式無線電力
  answer_index: 1
  explanation: OpenCRのADCは0~3.3 V範囲を使用し、センサ保護のために必ず専用の3.3 Vセンサレールから供給を受ける必要があります。
- question: システム点検および整備のために電源を遮断する最も安全な方法は？
  choices:
  - ソフトウェア命令でアクチュエーターのトルクをオフにする
  - ヒューズを取り外す
  - 3個の電源アダプターを物理的に分離した後、電圧を計測する
  - コントローラーの電源スイッチのみを切る
  answer_index: 2
  explanation: ソフトウェアコマンドやヒューズは完全な無電源状態を保証しません。必ずアダプタを物理的に分離し、マルチメータで1 V未満であることを計測しなければなりません。
completion_criteria:
- 各分岐別の12 V電圧が正常範囲内であることをマルチメータで確認し、写真を提出する
- FSRセンサーの接触力に応じたADC値の変化をコントローラーで確認し、正当な値を取得すること
- 物理的電源遮断および電圧計測を通じた安全停止手順を理解し、遵守すること
source_ids:
- S1
- S14
- S16
- S17
- S25
- S26
- S15
- S27
---

## ロボットシステムの構成要素
ロボットは感覚(Sensor)、思考(Controller)、動作(Actuator)の三つの核心要素で構成されます [S1]。本課程の5本指ロボットハンドはDYNAMIXEL XM430-W350-Tアクチュエータを使用し、腱駆動方式で関節を制御します [S14]。また、OpenCR 1.0コントローラを通じてこれらアクチュエータと指先のFSRセンサ信号を処理します [S16]。

## 電力システムの安全な設計
アクチュエータは12 Vの電圧でストール電流2.3 Aを要求するため [S14]、システム全体の負荷を考慮してMEAN WELL GST160A12-R7Bアダプタを3個使用します [S17]。各アダプタは4台/4台/3台のアクチュエータを担当する独立した12 V分岐として運用され、これら分岐の陽(+)出力は互いに結合せず、物理的に隔離されます。各分岐には10 A ATOFヒューズをインラインホルダ(0AFH0001Z)経由で設置し、過電流発生時に配線を保護します [S25, S26]。これは単純な停止機能を超えた電気的安全の基礎です。

## センサインターフェース
FSR 402センサは接触力に応じて抵抗が減少する特性を持ちます [S15]。これを10 kΩ抵抗と共に分圧回路で構成し、OpenCRの12ビットADCポートに接続することで接触力を電圧に換算します [S16, S27]。この際、センサ回路は3.3 Vセンサ電源レールからのみ供給を受ける必要があり、アクチュエータ用12 Vレールと混用してはいけません。
