---
layout: learn-module
title: センサ統合およびフィードバック制御
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.ja
course_locale: ja
lang: ja
ref: learn:precise-robot-hand:sensor-integration
translations:
- lang: ko
  url: /learn/precise-robot-hand/sensor-integration/
- lang: en
  url: /learn/en/precise-robot-hand/sensor-integration/
- lang: ja
  url: /learn/ja/precise-robot-hand/sensor-integration/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/sensor-integration/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/sensor-integration/
module_id: M8
permalink: /learn/ja/precise-robot-hand/sensor-integration/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: 75a701fd44954c3a8681a8f795bedc7d
id: M8
slug: sensor-integration
phase_id: P3
estimated_hours: 10.0
prerequisites:
- M7
objectives:
- FSR 402 センサと 10 kΩ抵抗を用いた分圧回路の構成原理の理解
- OpenCRコントローラのADC機能と入力範囲(0-3.3 V)の制約条件の習得
- センサデータのフィルタリングおよびキャリブレーション技術の習得
- フィードバックに基づく把持制御アルゴリズムの実装およびロボットハンドの接触力制御実習
worked_examples:
- '例題 1: FSR出力計算。 $R_{FSR}$ が 5 kΩであり、$R_{fixed}$ が 10 kΩであるとき、 3.3 V入力基準で $V_{out}
  = 3.3 \times (5 / (5 + 10)) = 1.1 V$。これはADC入力範囲(0-3.3 V)内に正常に位置します。'
- '例題 2: 把持力補正。センサ値がノイズによって変動する場合、単純移動平均フィルタを適用することで、センサ値の急激な変動を抑え、把持力を安定的に維持できます。'
lab:
  title: 指先FSRセンサ回路の構成および補正
  steps:
  - OpenCRの 3.3 VセンサレールとGNDをブレッドボードに接続します。
  - FSR 402と 10 kΩ抵抗を直列に接続して分圧回路を構成します [B4, B5]。
  - 分圧の接点をOpenCRのADCピンに接続します [B2]。
  - PCとOpenCRを接続し、センサ値を読み取るテストコードを実行します。
  - 無負荷状態と目標力が加えられる時のADC値を記録し、補正表を作成します。
  safety:
  - 電源投入前に必ずマルチメータで 3.3 Vレールと 12 Vアクチュエータレールの短絡の有無を確認してください [B2]。
  - 保護メガネを常時着用し、通電中はロボットハンドの可動範囲内に手を入れないでください。
  - 異常発熱・異臭・煙の感知時は接近せず、危険区域外で事前指定された建物分電盤のブレーカー、または認証されたupstream master disconnectで
    3個のアダプタへの供給電源を遮断した後に避難する。危険区域外で操作可能なupstream遮断手段がない場合、システムの通電を禁止する。トルク解除は電源遮断の代わりにはならない。整備・接近は計画停止後、物理的分離および無通電計測を確認した後にのみ行うこと。
  - 修理やセンサへの接近前に 3個の絶縁電源アダプタを物理的に取り外し、すべての分岐の電圧が 1 V未満であることを計測確認してください。
  deliverables:
  - ADCセンサ読み取りテスト結果データ
  - センサ補正テーブル(ADC値 vs 物理的な力)
  - センサデータフィルタリング実装コード
assignment:
  title: 把持力フィードバック制御アルゴリズムの実装
  deliverables:
  - フィードバック制御コード(センサ読み取り、目標値比較、モータトルク調整)
  - 把持試験結果グラフ(時間対力)
  - 最終報告書(制御ロジックの説明および把持安定性分析)
  rubric:
  - ADCデータが 0-3.3 V範囲内で安定的に測定されているか？
  - センサ値が目標値に達した時、モータが適切にトルクを解除または維持しているか？
  - 非常時にトルク解除がソフトウェア的に正常動作するか？
  - 報告書に電源遮断確認手順が記述されているか？
quiz:
- question: OpenCRコントローラのADCピンにFSR分圧信号を入力する際、必ず守らなければならないことは何ですか？
  choices:
  - 12 Vアクチュエータ電源レールを使用する。
  - 3.3 Vセンサ電源レールのみを使用する。
  - 5 V電源レールを使用する。
  - 電源を別途外部から供給する。
  answer_index: 1
  explanation: OpenCRのADC入力範囲は 0-3.3 Vであるため、これを超える電圧が印加されないよう、必ず 3.3 Vセンサ電源レールのみを使用しなければなりません。
- question: FSRセンサの抵抗値変化と物理的な力の関係はどのようになっていますか？
  choices:
  - 圧力が上昇すると抵抗値が上昇する。
  - 圧力が上昇すると抵抗値が減少する。
  - 圧力の変化と抵抗値は無関係である。
  - 圧力が上昇すると抵抗値が一定の割合で増幅される。
  answer_index: 1
  explanation: FSRは、圧力をかけるとセンサの抵抗値が減少する特性を持つ感圧抵抗器です。
- question: ロボットハンドのプロトタイプ作業中に、整備や接近のために電源を遮断した後で確認すべき安全状態は何ですか？
  choices:
  - ソフトウェア的にトルクを解除したか確認する。
  - ヒューズの断線の有無をマルチメータで測定する。
  - 3個の電源アダプタを物理的に取り外し、各分岐の電圧が 1 V未満であることをDC電圧モードで計測する。
  - 電源スイッチを切った後、抵抗モードで導線の状態を測定する。
  answer_index: 2
  explanation: 電源遮断とは 3個の電源を物理的に取り外すことであり、安全のために必ずマルチメータのDC電圧モードで、すべての分岐が 1 V未満であることを直接確認しなければなりません。
completion_criteria:
- ADCを通じたFSR値読み取り実習合格
- 把持力フィードバック制御コードが目標値に 90%以上到達
- すべての安全規則(物理的電源分離および電圧測定)の遵守証明
- 最終結果報告書の提出
source_ids:
- S3
- S12
- S26
---

## センサ統合と接触力フィードバック

ロボットハンドの精密な把持制御は、指先に作用する力を正確に測定することから始まります。FSR 402 センサは、加えられる圧力が大きくなるほど抵抗値が減少する感圧抵抗器です [S12]。これをマイクロコントローラが読み取れる電圧信号に変換するには、分圧回路が必要です。

### 1. 分圧回路
FSRセンサと 10 kΩの分圧抵抗を直列に接続し、 3.3 Vのセンサ電源を供給します [B4, B5, B2]。ADCピンはセンサと抵抗の接点に接続され、出力電圧 $V_{out}$は次のように計算されます。
10 kΩプルダウン分圧器は $V_{out}=V_{ref}\frac{R_{fixed}}{R_{FSR}+R_{fixed}}$ を使用する

- OpenCRコントローラのADCは 12ビットの解像度を持ち、入力範囲は 0〜3.3 Vに制限されています [B2]。この範囲外の入力は回路素子を損傷させる可能性があるため、必ず指定されたセンサ電源レール(3.3 V)のみを使用しなければなりません [B2]。

### 2. 制御ループとフィードバック
測定された力データは、PID制御アルゴリズムや適応制御戦略の入力値として使用されます [S3]。ロボットハンドが物体を把持する際、腱駆動モータ(DYNAMIXEL XM430-W350-T)はセンサ値を参照し、設定された目標接触力に達するまでトルクを微調整します [B1, B4]。
