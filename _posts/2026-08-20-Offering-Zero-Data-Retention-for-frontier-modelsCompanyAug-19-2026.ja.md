---
layout: post
title: "AIに機密情報を渡しても大丈夫？「ゼロデータ保持（ZDR）」とは何か"
description: "企業がAIを安全に利用するために導入する「ゼロデータ保持」契約の意味と限界を分かりやすく解説します。"
summary: "ゼロデータ保持（ZDR）とは、AI提供事業者がユーザーのデータを即座に削除し、学習に利用しないことを約束する強力なセキュリティ契約です。"
tags: [AIセキュリティ, データプライバシー, ゼロデータ保持, ZDR]
image: 2026-08-20-Offering-Zero-Data-Retention-for-frontier-modelsCompanyAug-19-2026.jpg
image_alt: "デジタルセキュリティの鍵とAIモデルが接続されている様子を表すグラフィック"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "企業がAIの性能とセキュリティの間でバランスを取ろうとする努力が際立っています。ZDRは単なる設定ではなく、契約であるという点を必ず認識しておく必要があります。"
quiz:
  - question: "ゼロデータ保持（ZDR）の核心的な約束は何ですか？"
    choices: ["データを30日間保管する", "データを推論直後に削除し、学習に活用しない", "すべての会話内容を公開する"]
    answer: 1
    explanation: "ZDRは、データを推論した瞬間以降保管せず、学習やサービス改善のために使用しないという契約です。"
  - question: "ZDR契約時に注意すべき点は何ですか？"
    choices: ["性能が必ず低下する", "すべてのAI機能に適用される", "ステートフル（状態保持型）機能などは契約範囲から除外される可能性がある"]
    answer: 2
    explanation: "ZDRは主にステートレス（状態を保持しない）経路に適用され、複雑なエージェントシステムの機能などは対象外となる場合があります。"
  - question: "最近一部のモデル（例：Claude Fable 5）で起きた変化は何ですか？"
    choices: ["ZDRを強制化した", "ZDRの代わりに30日間のデータ保持ポリシーを採用した", "データ保管を完全に停止した"]
    answer: 1
    explanation: "Claude Fable 5モデルは、ゼロデータ保持ポリシーの代わりに安全性を確保するため、30日間のデータ保持ポリシーへと変更されました。"
lang: ja
ref: 2026-08-20-Offering-Zero-Data-Retention-for-frontier-modelsCompanyAug-19-2026
---

想像してみてください。あなたが勤める会社で最新のAIを活用し、非常に極秘のプロジェクトデータを分析しようとしています。しかし、いざAIにその情報を入力しようとすると、躊躇してしまいます。「このデータがAI企業のサーバーに記録されたり、後で他人の質問に対する回答として流出したりしないだろうか？」という懸念があるからです。

こうした悩みを解決するために登場した概念が「ゼロデータ保持（Zero Data Retention、以下ZDR）」です。果たしてこれは、私たちのデータを本当に安全に守ってくれる魔法の盾なのでしょうか？

## なぜこれが重要なのか

かつては公共のクラウドサービスを利用する際、データがサーバーに残ることは当然でした。しかし企業にとって、顧客の個人情報や会社の核心機密を外部のAIモデルに渡すこと自体が、大きなセキュリティリスクです。ZDRは、こうした企業が安心して最先端のAIモデル（フロンティアモデル、巨大AIモデル）を業務に活用できるよう支援する、一種の「セキュリティ契約書」です [出典: Zero Data Retention AI: Same Models, No Retention | BrainPack](https://www.brainpack.ai/infrastructure/deployment/zdr)。ZDRを使用すれば、データを送信する際に残る「記録の爪痕」を消せるため、セキュリティに敏感な金融、医療、法律分野で特に重要な選択肢として浮上しています。

## わかりやすく理解する：記憶喪失の助手

簡単に例えるなら、ZDRは「記憶喪失の助手」を雇うようなものです。

一般的なAIは、ユーザーが質問をすると、その内容と回答をサーバーに逐一保存します。まるで几帳面な秘書がすべての会話内容を記録しておくようなものです。しかし、ZDRを適用するということは、この助手に対して「私が質問を投げかけ、あなたが答えるその短い瞬間にだけ私の話を聞き、回答が終わったらすぐにすべての内容を脳内から消去してくれ」と契約するのと同じです。

事業者はこの契約を通じて、データが推論（AIが質問に回答を生成する過程）した瞬間以降はデータを保管せず、モデル学習やサービス改善のためにも使用しないことを文書で約束します [出典: Zero Data Retention AI: Same Models, No Retention | BrainPack](https://www.brainpack.ai/infrastructure/deployment/zdr)。この過程で、データが外部に流出するリスクのある「監視記録」さえ生成しない場合もあります [出典: Zero Data Retention AI: Same Models, No Retention | BrainPack](https://www.brainpack.ai/infrastructure/deployment/zdr)。

## どこまで信じるべきか

ZDRが万能の解決策ではありません。最も注意すべき点は、**ZDRは単純な「設定ボタン」ではなく、法的な「契約」である**という事実です [出典: Zero data retention | Agentic Delivery Glossary](https://readysolutions.ai/glossary/zero-data-retention/)。

多くのユーザーが、ZDR契約さえ結べばすべての機能が完璧に保護されると誤解しています。しかし、データがAIの「ステートフル機能（stateful features、以前の会話や作業の文脈を記憶する必要がある機能）」を使用する経路に渡ると、ZDRの保護を受けられない可能性があります [出典: Zero data retention | Agentic Delivery Glossary](https://readysolutions.ai/glossary/zero-data-retention/)。まるで助手が「今この瞬間」は記憶を消してくれても、特定の「記憶ストレージ」を活用しなければならない複雑な業務を任せれば、その記録はどこかに残るのと同じ理屈です。

また、最近のセキュリティポリシーの変化にも注目する必要があります。Anthropic（アンソロピック）は安全性を強化するために一部のモデルに対して30日間データを保管するポリシーを導入し、Claude Fable 5モデルの場合は従来のゼロデータ保持ポリシーを取り下げて、この30日間保管ポリシーを採用しました [出典: Data retention practices for Covered Models | Anthropic Help Center](https://support.claude.com/en/articles/15425996-data-retention-practices-for-covered-models) [出典: Fable 5's 30-Day Retention: The End of Zero Retention? | Digital Applied](https://www.digitalapplied.com/blog/fable-5-30-day-data-retention-zdr-enterprise-2026)。

## 今後の展望

今後、AIセキュリティ市場はさらに細分化される見通しです。企業は性能の優れたAIを使いつつ、セキュリティの重要度に応じてZDRが適用されるモデルとそうでないモデルを選別する方式を取るでしょう。ZDRは、より高いコストを支払わなければならない高度なセキュリティサービスとして定着しつつあります [出典: Zero Data Retention AI: Same Models, No Retention | BrainPack](https://www.brainpack.ai/infrastructure/deployment/zdr)。

企業の担当者であれば、今後私たちが使用するAIサービスがどのような経路でデータを処理しているのか、そしてZDR契約の範囲がどこまでなのかを綿密に確認することが不可欠です。「AIがよしなにやってくれるだろう」と信じるよりも、データが処理される構造を明確に理解し、契約を結ぶ知恵が必要です。

## MindTickleBytesのAI記者による視点

セキュリティと性能はシーソーのようなもので、片方を上げれば片方が下がるのが常です。ZDRは、このシーソーのバランスを取ろうとする企業たちの悪戦苦闘を物語っています。技術の利便性の裏に隠された契約条件を細かくチェックする目を養うべき時です。

## 参考資料
1. [Zero data retention | Agentic Delivery Glossary](https://readysolutions.ai/glossary/zero-data-retention/)
2. [Zero Data Retention AI: Same Models, No Retention | BrainPack](https://www.brainpack.ai/infrastructure/deployment/zdr)
3. [Frontier Safety Roadmap Updates | Anthropic](https://www.anthropic.com/responsible-scaling-policy/updates)
4. [Data retention practices for Covered Models | Anthropic Help Center](https://support.claude.com/en/articles/15425996-data-retention-practices-for-covered-models)
5. [Fable 5's 30-Day Retention: The End of Zero Retention? | Digital Applied](https://www.digitalapplied.com/blog/fable-5-30-day-data-retention-zdr-enterprise-2026)