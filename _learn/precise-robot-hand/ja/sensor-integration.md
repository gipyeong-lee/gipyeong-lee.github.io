---
layout: learn-module
title: センサー統合およびフィードバック制御
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
translation_run_id: 541c3acee16e441bbae3b5125876cfe4
id: M8
slug: sensor-integration
phase_id: P3
estimated_hours: 10.0
prerequisites:
- M7
objectives:
- FSR 402センサーと10 kΩ抵抗を用いた電圧分割回路の構成原理を理解する
- OpenCRコントローラーのADC機能と入力範囲（0〜3.3 V）の制約条件を習得する
- センサーデータのフィルタリングおよびキャリブレーション技術を習得する
- フィードバックに基づく把持制御アルゴリズムを実装し、ロボットハンドの接触力制御を実習する
worked_examples:
- '例題1: FSR出力計算。$R_{FSR}$が5 kΩ、$R_{fixed}$が10 kΩのとき、3.3 V入力基準で $V_{out} = 3.3 \times
  (5 / (5 + 10)) = 1.1 V$。これはADC入力範囲（0〜3.3 V）内に正常に位置します。'
- '例題2: 把持力補正。センサー値がノイズによって揺れる場合、単純移動平均フィルタを適用することで、センサー値の急激な変動を抑え、把持力を安定的に維持できます。'
lab:
  title: 指先FSRセンサー回路の構成および補正
  steps:
  - OpenCRの3.3 VセンサーレールとGNDをブレッドボードに接続します。
  - FSR 402と10 kΩ抵抗を直列に接続し、電圧分割回路を構成します [B4, B5]。
  - 分圧接点をOpenCRのADCピンに接続します [B2]。
  - PCとOpenCRを接続し、センサー値を読み取るテストコードを実行します。
  - 無負荷状態と目標の力を加えたときのADC値を記録し、補正表を作成します。
  safety:
  - 電源投入前には必ずマルチメーターで3.3 Vレールと12 Vアクチュエータレールの短絡の有無を確認してください [B2]。
  - 保護メガネを常時着用し、通電中はロボットハンドの可動範囲内に手を入れないでください。
  - 異常な発熱・異臭・煙を感知した場合は近づかず、危険区域の外から事前指定された建物配電盤の遮断器、または認証済みのupstream master disconnectにより3個のアダプターの供給電源を遮断した後に避難する。危険区域の外に操作可能なupstream遮断手段がない場合は、システムの通電を禁止する。トルク解除は電源遮断の代わりにはならない。整備・接近は計画停止後、物理的な分離および無電源計測確認の後でのみ行う。
  - 修理やセンサーへの接近前には3個の絶縁電源アダプターを物理的に分離し、すべての分岐の電圧が1 V未満であることを計測確認してください。
  deliverables:
  - ADCセンサー読み取りテストの結果データ
  - センサー補正テーブル（ADC値 vs 物理的な力）
  - センサーデータフィルタリングの実装コード
assignment:
  title: 把持力フィードバック制御アルゴリズムの実装
  deliverables:
  - フィードバック制御コード（センサー読み取り、目標値比較、モータトルク調整）
  - 把持試験結果グラフ（時間 vs 力）
  - 最終報告書（制御ロジックの説明および把持安定性分析）
  rubric:
  - ADCデータが0〜3.3 Vの範囲内で安定的に測定されるか？
  - センサー値が目標値に達したとき、モータが適切にトルクを解除または維持するか？
  - 非常時にトルク解除がソフトウェア的に正常動作するか？
  - 報告書に電源遮断確認手順が技術的に記述されているか？
quiz:
- question: OpenCRコントローラーのADCピンにFSR電圧分割信号を入力する際、必ず守るべきことは何ですか？
  choices:
  - 12 Vアクチュエータ電源レールを使用する。
  - 3.3 Vセンサー電源レールのみを使用する。
  - 5 V電源レールを使用する。
  - 電源を外部から別途供給する。
  answer_index: 1
  explanation: OpenCRのADC入力範囲は0〜3.3 Vであるため、これを超える電圧が印加されないよう、必ず3.3 Vセンサー電源レールのみを使用しなければなりません。
- question: FSRセンサーの抵抗値変化と物理的な力の関係はどうですか？
  choices:
  - 圧力が増加すると抵抗値が増加する。
  - 圧力が増加すると抵抗値が減少する。
  - 圧力変化と抵抗値は無関係である。
  - 圧力が増加すると抵抗値が一定の割合で増幅される。
  answer_index: 1
  explanation: FSRは、圧力を加えるとセンサーの抵抗値が減少する特性を持つ感圧抵抗器です。
- question: ロボットハンド試作作業中に、整備や接近のために電源を遮断した後に確認すべき安全状態は何ですか？
  choices:
  - ソフトウェア的にトルクを解除したか確認する。
  - ヒューズの断線の有無をマルチメーターで測定する。
  - 3個の電源アダプターを物理的に分離し、各分岐の電圧が1 V未満であることをDC電圧モードで計測する。
  - 電源スイッチを切った後、抵抗モードで導線状態を測定する。
  answer_index: 2
  explanation: 電源遮断とは3個の電源を物理的に分離することであり、安全のために必ずマルチメーターのDC電圧モードですべての分岐が1 V未満であることを直接確認しなければなりません。
completion_criteria:
- ADCを通じたFSR値読み取り実習の合格
- 把持力フィードバック制御コードが目標値に90%以上到達
- すべての安全規則（物理的な電源分離および電圧測定）の遵守証明
- 最終結果報告書の提出
source_ids:
- S3
- S12
- S26
---

## センサー統合と接触力フィードバック

ロボットハンドの精密な把持制御は、指先に作用する力を正確に測定することから始まります。FSR 402センサーは、加えられる圧力が増加するほど抵抗値が減少する感圧抵抗器です [S12]。これをマイクロコントローラーが読み取れる電圧信号に変換するには、電圧分割回路が必要です。

### 1. 電圧分割回路
FSRセンサーと10 kΩ分圧抵抗を直列に接続し、3.3 Vセンサー電源を供給します [B4, B5, B2]。ADCピンはセンサーと抵抗の接点に接続され、出力電圧 $V_{out}$は次のように計算されます。
10 kΩプルダウン分圧器は $V_{out}=V_{ref}\frac{R_{fixed}}{R_{FSR}+R_{fixed}}$ を使用する。

- OpenCRコントローラーのADCは12ビットの分解能を持ち、入力範囲は0〜3.3 Vに制限されます [B2]。この範囲を超えた入力は回路素子を損傷させる可能性があるため、必ず指定されたセンサー電源レール（3.3 V）のみを使用しなければなりません [B2]。

### 2. 制御ループとフィードバック
測定された力データは、PID制御アルゴリズムや適応制御戦略の入力値として使用されます [S3]。ロボットハンドが物体を把持する際、腱駆動モーター（DYNAMIXEL XM430-W350-T）はセンサー値を参照し、設定された目標接触力に達するまでトルクを微調整します [B1, B4]。
