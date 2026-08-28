---
layout: learn-module
title: ベアリングおよび締結部品設置
course_slug: precise-robot-hand
course_data_key: precise-robot-hand-ja
course_locale: ja
lang: ja
ref: learn:precise-robot-hand:bearing-fastener-install
translations:
- lang: ko
  url: /learn/precise-robot-hand/bearing-fastener-install/
- lang: en
  url: /learn/en/precise-robot-hand/bearing-fastener-install/
- lang: ja
  url: /learn/ja/precise-robot-hand/bearing-fastener-install/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/bearing-fastener-install/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/bearing-fastener-install/
module_id: M5
permalink: /learn/ja/precise-robot-hand/bearing-fastener-install/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: 541c3acee16e441bbae3b5125876cfe4
id: M5
slug: bearing-fastener-install
phase_id: P2
estimated_hours: 10.0
prerequisites:
- M4
objectives:
- 精密ロボットハンド製作のためのベアリングおよびシャフトの機械的公差と設置原理を理解する。
- 熱圧入インサート（Heat-set insert）を使用してエンジニアリングプラスチック部品の締結強度を確保する方法を習得する。
- 適切なトルクと締結規格を使用して組立時のガタつきを最小化する。
worked_examples:
- '例題 1: ハウジング内径確認 - iglide® JSM-0810-10 ベアリングの外径は 10 mm である。したがってハウジングボアは 10 mm に合わせて設計される必要があり、インサート挿入時にパイロット穴
  4.0 mm を守らないと、インサートが空転したりハウジングが破損したりする可能性がある [S17, S21]。'
- '例題 2: M3 ネジ組立 - M3x10 キャップスクリューは 2.5 mm 六角レンチを使用して締結し、過度なトルクはインサート周辺の樹脂にクラックを誘発する可能性があるため、「これ以上回らない時点」で最小限の力で固定する
  [S20]。'
lab:
  title: ロボットハンド関節精密組立
  steps:
  - 1. PC-CF 出力物ハウジングの 4.0 mm パイロット穴がきれいか確認し、インサートを垂直に整列する。
  - 2. はんだごてを適正温度に加熱し、インサートを垂直にゆっくりと押してハウジング表面と平行に圧入する。
  - 3. iglide® ベアリングをボアに圧入し、8 mm アルミニウムシャフトを挿入してガタつきと抵抗を確認する。
  - 4. M3 ネジを使用してリンク間の締結を完了し、関節を動かして摩擦が均一か検証する。
  safety:
  - はんだごては高温のため火傷に注意し、加熱後は直ちにスタンドに置く。
  - インサート圧入時に発生する微細粉塵は吸入しないよう換気を徹底する。
  - 保護メガネを必ず着用して作業を進める。
  - 異常発熱・異臭・煙を感知した場合は接近せず、危険区域外で指定された分電盤ブレーカーまたは認証された upstream master disconnect で
    3 個のアダプタ電源を遮断した後に避難すること。危険区域外で操作可能な upstream 遮断手段がない場合は、システム通電を禁止する。トルクオフは電源遮断の代わりにはならない。整備・接近は計画停止後の物理的分離および無電源計測確認の後でのみ実行すること。
  deliverables:
  - 関節別摩擦試験ログ
  - インサート垂直整列確認写真
  - 組立済みリンクの自由度およびガタつき測定記録
assignment:
  title: 組立公差および締結力分析レポート
  deliverables:
  - 関節組立順序およびトルク管理計画書
  - ガタつき発生時の解決策（Shim 使用または公差修正）記述
  - 組立完了したロボットハンドリンクの把持試験予備データ
  rubric:
  - インサート挿入の垂直度が明確に記述されているか？
  - ベアリングとシャフトの公差概念を正しく説明しているか？
  - 組立段階での安全規則を遵守したか？
quiz:
- question: iglide® J ベアリングがハウジングに圧入された後、内径が調整される理由は何ですか？
  choices:
  - ベアリング材質の弾性により、圧入時に内径が自動的に広がるため。
  - 圧入過程でベアリング内径がハウジングボアの公差に合わせて精密に調整されるよう設計されているため。
  - 圧入前の内径は常に基準値より小さく製作されるため。
  answer_index: 1
  explanation: iglide® スリーブベアリングは圧入前は基準値より大きい状態で製作され、正しいハウジングボアに圧入されたときに設計された公差内の内径を持つように設計されています
    [S17]。
- question: PC-CF 出力物に真鍮製熱圧入インサートを使用する際、適切なパイロット穴サイズは？
  choices:
  - 3.5 mm
  - 4.0 mm
  - 4.4 mm
  answer_index: 1
  explanation: データシートによると、HTBI-M3-BR インサートの推奨パイロット穴サイズは 4.0 mm です [S21]。
completion_criteria:
- 組立済み 5 本の指関節の摩擦抵抗が均一であることを確認し、測定記録を提出。
- すべてのインサートが PC-CF ハウジングと水平をなしているかを目視および寸法検査完了。
- 組立中の安全規則を遵守したことを誓約し、作業記録簿を提出。
source_ids:
- S17
- S18
- S20
- S21
---

### ベアリングとシャフトの公差管理
精密ロボット関節の滑らかな動きと剛性確保のために iglide® J スリーブベアリング（JSM-0810-10）と 8 mm アルミニウム精密シャフト（AWMP-08）を使用する。スリーブベアリングはハウジングに圧入（press-fit）されると内径が調整されるように設計されており、ハウジングの推奨内径公差を遵守することが肝要である [S17, S18]。ガタつきが発生すると関節の精度が低下し、逆に狭すぎると摩擦力が増加して駆動器（DYNAMIXEL XM430）の電流効率を低下させる。

### 熱圧入インサート設置
PC-CF（炭素繊維補強 PC）出力物は、金属ネジを直接締結すると材質の特性上、ネジ山が摩耗しやすい。これを防止するために真鍮製の熱圧入インサート（HTBI-M3-BR）を使用する [S21]。インサートは 4.0 mm パイロット穴に挿入後、熱を加えて周辺の樹脂を溶かして締結することで、繰り返しの分解・組立にも高い機械的強度を維持する [S21]。この際、インサートが傾くと組立済みリンクの整列がずれるため、垂直の維持が必須である。
