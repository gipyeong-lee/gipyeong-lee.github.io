---
layout: learn-module
title: ファームウェア開発および制御
course_slug: precise-robot-hand
course_data_key: precise-robot-hand-ja
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
translation_run_id: 541c3acee16e441bbae3b5125876cfe4
primary_category: robotics-hardware
topics:
- robot-hands
- tendon-drive
- embedded-control
course_type: build_project
published_at: '2026-08-29T08:34:02+09:00'
id: M7
slug: firmware-development
phase_id: P3
estimated_hours: 15.0
prerequisites:
- M6
objectives:
- DYNAMIXEL スマートアクチュエータ通信および制御フレームワークの理解
- OpenCR 制御ボードを活用したアクチュエータおよび FSR センサ信号取得の実装
- リアルタイムロボット制御の状態機械および閉ループフィードバックループ設計
- 安全な電源管理およびトルクオフシーケンスプログラミング
worked_examples:
- '1. アクチュエータ目標位置/電流設定: DYNAMIXEL SDK を使用して XM430 アクチュエータの電流制限（Goal Current）を設定し、センサ値に応じた
  PID ループを通じて指関節の最終位置を更新する例題。'
- '2. FSR 電圧データフィルタリング: ADC で収集された生データのノイズを除去するために移動平均フィルタ（Moving Average Filter）を適用し、上限（20N）と下限（0.2N）範囲を正規化するコード実装
  [S12]。'
lab:
  title: ロボットハンド統合制御および精密把持実習
  steps:
  - 各独立分岐の電圧が 1V 未満であることをマルチメータ DC モードで確認した後、組立を開始する。
  - OpenCR の 3.3V センサレールに FSR 電圧分圧回路をはんだ付けし、ADC ポートに接続する。
  - DYNAMIXEL SDK を使用して 11 個のアクチュエータの ID をスキャンし、初期位置を設定する。
  - 無負荷状態で指関節駆動命令をテストしながら、腱の伸長率と張力を調節する。
  - FSR センサデータをシリアルモニタで視覚化しながら把持力応答をチューニングする。
  safety:
  - 絶対に 5V または 12V アクチュエータ電源を FSR センサ回路の供給電源として使用しないこと。
  - システム通電中には決して指の可動範囲に近づかず、固定治具を使用すること。
  - 電源分岐アダプタの陽(+)端子を絶対に相互接続しないこと。
  - 整備・組立接近前には、必ず 3 個の電源アダプタを物理的に分離し、すべての分岐で 1V 未満であることを計測確認すること。
  deliverables:
  - リアルタイムセンサデータフィードバックが含まれたファームウェアソースコード
  - 電圧分圧データの正規化および校正データシート
  - アクチュエータフィードバックループ正常作動ログ
assignment:
  title: 把持状態機械設計および実装
  deliverables:
  - 把持および把持解除状態機械ダイアグラム
  - 電流ベースのトルク制御実装コード
  - 最終性能評価レポート
  rubric:
  - センサ値に応じた電流制限範囲( 0- 2.3A)が安定的に制御されているか？
  - トルク解除指令時、物理的な張力が即座に除去されるか？
  - コード内に安全なハードウェア分離手順が明示されているか？
quiz:
- question: FSR 402センサーと電圧分割回路を構成する際に推奨される電源レールは何ですか？
  choices:
  - 12Vアクチュエータ電源レール
  - 5V汎用電源レール
  - OpenCR 3.3Vセンサーレール
  - 24V外部入力レール
  answer_index: 2
  explanation: システムの安全性とOpenCR ADC保護のため、FSR電圧分割回路は必ず3.3Vセンサー電源レールに接続する必要があります。
- question: ロボットハンド整備時に、システムが「無電源状態」であることを確認する正しい方法は何ですか？
  choices:
  - ソフトウェアでトルク解除指令を送る。
  - マルチメーターの抵抗モードで配線状態を確認する。
  - マルチメーターのDC電圧モードで、すべての分岐が1V未満であることを計測する。
  - 電源分岐のヒューズを外す。
  answer_index: 2
  explanation: 物理的な電源分離後、必ずマルチメーターのDC電圧モードですべての分岐の残留電圧が1V未満であることを直接確認する必要があります。
- question: 複数の独立した電源アダプター出力のプラス(+)端子を並列に接続してもよいですか？
  choices:
  - 電流の合計のために必要である。
  - 絶対禁止である。
  - 定格出力電流が同じであれば可能である。
  - ヒューズを装着すれば可能である。
  answer_index: 1
  explanation: 独立した分岐で構成された電源アダプターのプラス(+)出力は、互いに接続したり統合したりしては絶対にいけません。
completion_criteria:
- 各分岐別の独立した電源供給およびヒューズ保護がBOM仕様に従って構成されたことをマルチメーターで検証完了
- OpenCR ADCを通じた5個のFSRセンサーの精密な力信号取得およびフィルタリング確認
- ソフトウェアのトルク解除ルーチンと物理的な電源遮断後の計測手順を完璧に遂行
- 把持ステートマシンが意図通りにアクチュエータとセンサーデータを処理し、最終報告書が提出された
source_ids:
- S13
- S11
- S12
---

### ファームウェアアーキテクチャおよび DYNAMIXEL 制御
ロボットハンドのファームウェアは、高速ループ内でセンサデータを取得し、アクチュエータ命令を処理します。`OpenCR 1.0` 制御器は 216MHz ARM Cortex-M7 プロセッサをベースとし [S13]、別途のブリッジなしで DYNAMIXEL プロトコル 2.0 を処理して [S11] 遅延時間を最小化します。各アクチュエータは電流、速度、位置モードをサポートし、ロボットハンドは電流制御を通じたトルクベースの把持戦略を使用します。

### FSR 力フィードバックシステム
FSR 402 センサは、加えられた力に反比例する抵抗特性を持ちます [S12]。OpenCR の 12 ビット ADC を使用し [S13]、3.3V センサレールから 10kΩ 抵抗と電圧分圧回路を構成します。分圧された電圧は `ADC値 = (V_in * R_fsr) / (R_fsr + R_ref)` を通じて正規化され、この値は指の腱張力と連動して把持力フィードバックとして使用されます。

### 安全な制御ルーチン
システム停止は安全のために二段階に分けられます。ソフトウェア段階ではアクチュエータのトルクをオフ（Torque Off）にして物理的駆動力即座に除去します。整備前には必ず 3 個の独立電源アダプタの電源を物理的に分離した後、マルチメータの DC モードを使用してすべての分岐で 1V 未満であることを確認しなければなりません。
