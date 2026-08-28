---
layout: learn-module
title: ファームウェア開発および制御
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.ja
course_locale: ja
lang: ja
ref: learn:precise-robot-hand:firmware-development
translations:
- lang: ko
  url: /learn/precise-robot-hand/firmware-development/
- lang: en
  url: /learn/en/precise-robot-hand/firmware-development/
- lang: ja
  url: /learn/ja/precise-robot-hand/firmware-development/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/firmware-development/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/firmware-development/
module_id: M7
permalink: /learn/ja/precise-robot-hand/firmware-development/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: 75a701fd44954c3a8681a8f795bedc7d
id: M7
slug: firmware-development
phase_id: P3
estimated_hours: 15.0
prerequisites:
- M6
objectives:
- DYNAMIXEL スマートアクチュエータ通信および制御フレームワークの理解
- OpenCR 制御ボードを活用したアクチュエータおよび FSR センサ信号取得の実装
- リアルタイムロボット制御状態機械および閉ループフィードバックループ設計
- 安全な電源管理およびトルクオフシーケンスプログラミング
worked_examples:
- '1. アクチュエータ目標位置/電流設定: DYNAMIXEL SDK を使用して XM430 アクチュエータの電流制限(Goal Current)を設定し、センサ値に応じた
  PID ループを通じて指関節の最終位置を更新する例題。'
- '2. FSR 電圧データフィルタリング: ADC から収集された元データ(RAW データ)のノイズを除去するために移動平均フィルタ(Moving Average
  Filter)を適用し、上限(20N)と下限(0.2N)範囲を正規化するコード実装 [S12]。'
lab:
  title: ロボットハンド統合制御および精密把持実習
  steps:
  - 各独立分岐の電圧が 1V 未満であることをマルチメータ DC モードで確認した後、組み立てを開始する。
  - OpenCR の 3.3V センサレールに FSR 電圧分圧回路をはんだ付けし、ADC ポートに接続する。
  - DYNAMIXEL SDK を使用して 11 個のアクチュエータの ID をスキャンし、初期位置を設定する。
  - 無負荷状態で指関節駆動命令をテストし、腱の伸度と張力を調節する。
  - FSR センサデータをシリアルモニタで視覚化し、把持力応答をチューニングする。
  safety:
  - 絶対に 5V または 12V アクチュエータ電源を FSR センサ回路の供給電源として使用しないこと。
  - システム通電中は絶対に指の可動範囲に接近せず、固定治具を使用すること。
  - 電源分岐アダプタの陽(+)端子を絶対に互いに接続しないこと。
  - 整備・組み立て接近前には、必ず 3 個の電源アダプタを物理的に分離し、すべての分岐で 1V 未満であることを計測確認すること。
  deliverables:
  - リアルタイムセンサデータフィードバックを含むファームウェアソースコード
  - 電圧分圧データの正規化および校正データシート
  - アクチュエータフィードバックループ正常動作ログ
assignment:
  title: 把持状態機械設計および実装
  deliverables:
  - 把持および把持解除状態機械ダイアグラム
  - 電流ベーストルク制御実装コード
  - 最終性能評価レポート
  rubric:
  - センサ値に応じた電流制限範囲(0-2.3A)が安定的に制御されるか？
  - トルク解除指令時に物理的な張力が即座に解除されるか？
  - コード内に安全なハードウェア分離手順が明示されているか？
quiz:
- question: FSR 402 センサと分圧回路を構成する際に推奨される電源レールは何ですか？
  choices:
  - 12Vアクチュエータ電源レール
  - 5V汎用電源レール
  - OpenCR 3.3Vセンサレール
  - 24V外部入力レール
  answer_index: 2
  explanation: システム安全とOpenCR ADC保護のため、FSR分圧回路は必ず 3.3Vセンサ電源レールに接続しなければなりません。
- question: ロボットハンド整備時にシステムが「無通電状態」であることを確認する正しい方法は何ですか？
  choices:
  - ソフトウェアでトルク解除指令を送る。
  - マルチメータの抵抗モードで配線状態を確認する。
  - マルチメータのDC電圧モードですべての分岐が1V未満であることを計測する。
  - 電源分岐ヒューズを取り外す。
  answer_index: 2
  explanation: 物理的な電源分離後、必ずマルチメータのDC電圧モードですべての分岐の残留電圧が1V未満であることを直接確認しなければなりません。
- question: 複数の独立電源アダプタ出力のプラス(+)端子を並列に接続してもよいですか？
  choices:
  - 電流合計のために必要だ。
  - 絶対禁止される。
  - 定格出力電流が同じであれば可能だ。
  - ヒューズを装着すれば可能だ。
  answer_index: 1
  explanation: 独立分岐で構成された電源アダプタのプラス(+)出力は、相互に接続したり統合したりしては絶対にいけません。
completion_criteria:
- 各分岐別の独立電源供給およびヒューズ保護がBOM仕様に従って構成されていることをマルチメータで検証完了
- OpenCR ADCを通じた 5個のFSRセンサの精密な力信号取得およびフィルタリング確認
- ソフトウェアトルク解除ルーチンと物理的な電源遮断後の計測手順を完璧に遂行
- 把持状態機械が意図通りにアクチュエータとセンサデータを処理し、最終報告書が提出済み
source_ids:
- S13
- S11
- S12
---

### ファームウェアアーキテクチャおよび DYNAMIXEL 制御
ロボットハンドのファームウェアは高速ループ内でセンサデータを取得し、アクチュエータ命令を処理する。`OpenCR 1.0` コントローラは 216MHz ARM Cortex-M7 プロセッサを基盤とし [S13]、別途ブリッジなしで DYNAMIXEL プロトコル 2.0 を処理して [S11] 遅延時間を最小化する。各アクチュエータは電流、速度、位置モードをサポートし、ロボットハンドは電流制御を通じたトルクベース把持戦略を使用する。

### FSR 力フィードバックシステム
FSR 402 センサは印加された力に反比例する抵抗特性を持つ [S12]。OpenCR の 12 ビット ADC を使用して [S13] 3.3V センサレールから 10kΩ 抵抗と電圧分圧回路を構成する。分圧された電圧は `ADC値 = (V_in * R_fsr) / (R_fsr + R_ref)` を通じて正規化され、この値は指の腱張力と連動し、把持力フィードバックとして使用される。

### 安全な制御ルーチン
システム停止は安全のため二段階に分けられる。ソフトウェア段階ではアクチュエータトルクを解除(Torque Off)し、物理的駆動力を即時除去する。整備前には必ず 3 個の独立電源アダプタの電源を物理的に分離した後、マルチメータ DC モードを使用してすべての分岐で 1V 未満であることを確認しなければならない。
