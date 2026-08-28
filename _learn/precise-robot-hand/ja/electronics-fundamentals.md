---
layout: learn-module
title: 電子回路基礎
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.ja
course_locale: ja
lang: ja
ref: learn:precise-robot-hand:electronics-fundamentals
translations:
- lang: ko
  url: /learn/precise-robot-hand/electronics-fundamentals/
- lang: en
  url: /learn/en/precise-robot-hand/electronics-fundamentals/
- lang: ja
  url: /learn/ja/precise-robot-hand/electronics-fundamentals/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/electronics-fundamentals/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/electronics-fundamentals/
module_id: m4
permalink: /learn/ja/precise-robot-hand/electronics-fundamentals/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e40f5b399c3a49a386d28778db2b6fc5
translation_run_id: 6887538d0dce4b0bbbe63a75ae59d8c4
id: m4
slug: electronics-fundamentals
phase_id: p2
estimated_hours: 12.0
prerequisites:
- m3
objectives:
- DYNAMIXELスマートアクチュエーターの電気的特性と電源システムの理解
- FSR 402センサを活用した電圧分圧回路設計およびADC信号取得
- システム過電流保護のためのヒューズベース電源分岐設計
- 電気回路の絶縁および物理的安全分離原則の熟知
worked_examples:
- 例題1：分岐電源電流合計計算。一分岐に4台のアクチュエータ(ストール電流各2.3 A)が割り当てられた場合、最大理論電流は9.2 Aです。これは10 Aヒューズの定格内であり、アダプタの11.5
  A出力限度を超えないため安全に駆動可能です [S14, S17, S26]。
- 例題2：FSR分圧器出力計算。FSRに力が加わりセンサ抵抗が10 kΩになったとき、分圧ノードの電圧は3.3 V * (10 kΩ / (10 kΩ + 10
  kΩ)) = 1.65 Vとなります。これはOpenCR 12ビットADCの有効範囲内であるため精密な力フィードバックが可能です [S15, S16, S27]。
lab:
  title: 電源分岐構成およびセンサー入力試験
  steps:
  - 各MEAN WELLアダプタ出力線に0AFH0001Zインラインホルダと10 A ATOFヒューズを直列に設置します [S17, S25, S26]。
  - 各分岐の12 V電圧が正常範囲内であるかマルチメータで測定します。
  - OpenCR 3.3 Vピンと10 kΩ抵抗、FSR 402を使用して分圧回路をブレッドボードに構成します [S16, S27]。
  - センサ電圧が0~3.3 V範囲内にあるか確認し、力を加える際、電圧変化を観察します。
  safety:
  - 整備および接近前、3個の電源アダプタを物理的に分離した後、各分岐のDC電圧が1 V未満であることをマルチメータで必ず確認します。
  - 回路構成中、電源投入禁止。電圧測定はすべての結線完了後、固定治具状態で行います。
  - 耐衝撃用保護メガネを常時着用します。
  - アクチュエータ電源(12 V)とセンサ電源(3.3 V)を絶対に混線させないでください。
  deliverables:
  - 回路別電圧測定データシート
  - FSR力センサーの力-電圧反応曲線プロット
  - 過電流保護のための分岐別ヒューズ結線写真
assignment:
  title: 電源配分およびセンサーデータ収集設計
  deliverables:
  - アクチュエーター分岐別電力割り当て計画書
  - OpenCR ADC回路図を含む配線図
  - ヒューズ定格選定論理レポート
  rubric:
  - 電源分岐合計電流が各アダプターの許容範囲を遵守している
  - FSR回路が3.3 Vセンサレールのみに接続されていること
  - ヒューズが過電流保護を適切に遂行できる定格で選定されている
quiz:
- question: 次の中で電源分岐構成時に禁じられる行為は何ですか？
  choices:
  - 分岐ごとに10 Aヒューズを直列に設置すること
  - 独立したアダプターの陽(+)端子を並列に接続すること
  - アクチュエーターを4:4:3で配分すること
  - FSRセンサを3.3 Vレールに接続すること
  answer_index: 1
  explanation: 各アダプター出力は独立した分岐として使用しなければならず、電源アダプター出力間の並列接続はシステム故障および火災の危険を招く恐れがあるため、絶対禁じられます。
- question: FSR 402センサ電圧分圧回路構成時の注意事項として正しいものは？
  choices:
  - 12 Vアクチュエータ電源レールを使用しなければならない。
  - 5 V電源を使用してADC解像度を高めなければならない。
  - OpenCRの3.3 Vセンサ電源を使用しなければならない。
  - 抵抗なしにFSRのみを接続しなければならない。
  answer_index: 2
  explanation: FSRセンサの電圧信号はOpenCR ADC入力範囲(0~3.3 V)を超えてはいけないため、必ず3.3 Vセンサ電源を使用しなければなりません。
completion_criteria:
- すべての電源分岐回路の電圧が1 V未満に物理的に分離されていることをマルチメータで立証
- ヒューズ装着および3.3 V電源分圧回路構成完了
- FSRセンサ信号がOpenCR ADCで0~3.3 V内で正常に取得されることを確認
source_ids:
- S6
- S9
- S14
- S17
- S26
- S25
- S15
- S27
- S16
---

異常発熱・臭気・煙を感知した場合は接近せず、危険区域外の事前指定された建物分電盤ブレーカー、または認証されたupstream master disconnectで3個のアダプターの供給電源を遮断した後に退避する。危険区域外で操作可能なupstream遮断手段がない場合、システムの通電を禁ずる。トルクオフは電源遮断の代わりにはならない。整備・接近は計画停止後、物理的分離および無電源計測確認後にのみ行う [S14] [S17] [S26, S25] [S26] [S15] [S27] [S16]
