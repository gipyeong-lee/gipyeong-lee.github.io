---
layout: learn-module
title: アクチュエーターおよびセンサー統合
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.ja
course_locale: ja
lang: ja
ref: learn:precise-robot-hand:actuators-sensors
translations:
- lang: ko
  url: /learn/precise-robot-hand/actuators-sensors/
- lang: en
  url: /learn/en/precise-robot-hand/actuators-sensors/
- lang: ja
  url: /learn/ja/precise-robot-hand/actuators-sensors/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/actuators-sensors/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/actuators-sensors/
module_id: m5
permalink: /learn/ja/precise-robot-hand/actuators-sensors/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
translation_run_id: 6887538d0dce4b0bbbe63a75ae59d8c4
id: m5
slug: actuators-sensors
phase_id: p2
estimated_hours: 13.0
prerequisites:
- m4
objectives:
- DYNAMIXELスマートアクチュエーターの制御信号と電源配分構造を理解する。
- FSR(力感応抵抗)センサーの動作原理を把握し、OpenCRコントローラーで電圧分圧回路を設計する。
- アクチュエーター電源分岐および個別ヒューズ保護の重要性を習得する。
- テンドン駆動システムの機構的特性と電子制御フィードバックの連動方法を習得する。
worked_examples:
- 例題1：アクチュエータ分岐別最大負荷計算。1台のアクチュエータストール電流2.3 Aの場合[S14]、4台のアクチュエータが配置された分岐の最大ピーク電流は4
  * 2.3 A = 9.2 Aである。これは10 Aヒューズの定格内であり[S26]、11.5 Aアダプタ出力仕様を超えないため安全である[S17]。
- 例題2：FSR分圧回路のADC電圧算出。センサ抵抗をR_fsr、固定抵抗をR_fixed(10 kΩ)とする時、ADC入力電圧V_adc = 3.3V * (R_fixed
  / (R_fsr + R_fixed))である[S16, S27]。接触力がない時(無限大抵抗) V_adcは0 V、最大接触時、センサ抵抗が固定抵抗より小さくなるとV_adcは3.3
  Vに近づき、力データをデジタル化する。
lab:
  title: アクチュエーターおよびFSRセンサー統合試験
  steps:
  - 各アダプタ出力端にATOインラインヒューズホルダを接続し、10 Aヒューズを挿入する[S25, S26]。
  - DYNAMIXELアクチュエーターハーネスをヒューズ以降の電源分岐に接続する [S9]。
  - FSRセンサと10 kΩ抵抗を使用して電圧分圧回路を構成し、OpenCRの3.3 V ADCポートに接続する[S16, S27]。
  - マルチメータをDC電圧モードに設定し、各分岐の出力電圧が12 Vであることを確認する。
  - ソフトウェアでアクチュエーターを低速無負荷回転させ、通信状態を点検する。
  safety:
  - 整備前、3個の電源アダプタを物理的に分離した後、1 V未満であることを測定して無電源状態を確認する。
  - 電源投入中は手をアクチュエーターの可動範囲に入れない。
  - 回路試験時は保護メガネを必ず着用する。
  - 異常発熱・臭気・煙を感知した場合は接近せず、危険区域外の事前指定された建物分電盤ブレーカー、または認証されたupstream master disconnectで3個のアダプターの供給電源を遮断した後に退避する。危険区域外で操作可能なupstream遮断手段がない場合、システムの通電を禁ずる。トルクオフは電源遮断の代わりにはならない。整備・接近は計画停止後、物理的分離および無電源計測確認後にのみ行う
  deliverables:
  - 分岐別電圧測定校正記録用紙
  - FSRセンサー圧力-ADC値特性曲線グラフ
  - 正常作動状態のロボットハンドハーネス写真および配線図
assignment:
  title: 電源システム設計およびフィードバックロジック実装
  deliverables:
  - アクチュエーター分岐別負荷配分およびヒューズ保護計算書
  - FSRセンサーデータを利用した把持力制御アルゴリズム(擬似コード)
  - 最終配線および電源統合設計レポート
  rubric:
  - 12 Vアクチュエータと3.3 Vセンサレールが正しく分離されているか？
  - 分岐別最大ピーク電流がヒューズ定格を超えないか？
  - 教育用プロトタイプは機械安全標準遵守や認証を主張せず、人間が接近する環境へ投入前には有資格の安全専門家の別途検討が必要であるか？
  - 安全規則に従った電源物理分離手順を理解したか？
quiz:
- question: FSR電圧分圧回路の供給電源として適切なものは？
  choices:
  - 12 Vアクチュエータ電源
  - OpenCR 3.3 Vセンサ電源
  answer_index: 1
  explanation: FSRセンサのADC信号はOpenCRの3.3 Vセンサレールを使用しなければならず、12 Vアクチュエータ電源とは電気的に完全に分離されなければならない。
- question: 分岐別ヒューズ保護の主な目的は何ですか？
  choices:
  - 電圧を12 Vに強制固定するため
  - 異常発熱・臭気・煙を感知した場合は接近せず、危険区域外の事前指定された建物分電盤ブレーカー、または認証されたupstream master disconnectで3個のアダプターの供給電源を遮断した後に退避する。危険区域外で操作可能なupstream遮断手段がない場合、システムの通電を禁ずる。トルクオフは電源遮断の代わりにはならない。整備・接近は計画停止後、物理的分離および無電源計測確認後にのみ行う
  answer_index: 1
  explanation: 各分岐に配置された10 Aヒューズは、アクチュエータのピーク電流を許容しながら、配線ショート等の故障発生時、過電流からシステムを保護する。
- question: 絶縁型電源アダプターの独立した陽(+)出力同士を接続してもよいか？
  choices:
  - 分岐電流合計のために必ず接続しなければならない
  - 絶対禁じられ、各分岐を独立的に維持しなければならない
  answer_index: 1
  explanation: 独立型分岐構造のため、陽(+)出力並列接続は絶対禁じられ、各出力は物理的に分離された電源ハーネスとして運営されなければならない。
completion_criteria:
- 各アクチュエータ分岐で12 V電圧が正常に計測されることを確認した。
- FSRセンサーデータをコントローラーで正常に取得し、接触力変化によるADC値変化を立証した。
- システム電源を物理的に遮断し、1 V未満の状態において安全に整備接近を遂行できる。
- すべての実習課題および安全遵守誓約書を提出した。
source_ids:
- S14
- S15
- S16
- S17
- S27
- S26
- S25
- S9
---

異常発熱・臭気・煙を感知した場合は接近せず、危険区域外の事前指定された建物分電盤ブレーカー、または認証されたupstream master disconnectで3個のアダプターの供給電源を遮断した後に退避する。危険区域外で操作可能なupstream遮断手段がない場合、システムの通電を禁ずる。トルクオフは電源遮断の代わりにはならない。整備・接近は計画停止後、物理的分離および無電源計測確認後にのみ行う [S14] [S16] [S17] [S15] [S27] [S26]
