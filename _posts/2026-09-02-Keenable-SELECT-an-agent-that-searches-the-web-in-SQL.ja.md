---
layout: post
title: "AIがインターネットを「SQL」で検索？「Keenable SELECT」の物語"
description: "AIエージェントが複雑なWebデータをSQLクエリ一つでスッキリ整理する新しい検索手法「Keenable SELECT」を紹介します。"
summary: "AIエージェントが従来の検索APIの複雑なデータを処理する枠を超え、SQL言語を使って目的の情報を正確に抽出する技術「Keenable SELECT」について解説します。"
tags: [AI, 検索エンジン, SQL, エージェント, 技術]
image: 2026-09-02-Keenable-SELECT-an-agent-that-searches-the-web-in-SQL.jpg
image_alt: "データベースのクエリ言語であるSQLコードが、Web検索データと結びつく様子をイメージしたグラフィック"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "人間向けの検索とAI向けの検索は、根本的に異なるべきです。KeenableのSQLインターフェースは、エージェントがWebと対話する方法を一段と進化させるでしょう。"
quiz:
  - question: "「Keenable SELECT」の最大の特徴は何ですか？"
    choices: ["人間用検索エンジンインターフェースの提供", "SQLを使用してWebデータを読み取り専用で照会", "世界中のあらゆるWebサイトのリアルタイムレンダリング"]
    answer: 1
    explanation: "Keenable SELECTは、モデルコンテキストプロトコル（MCP）サーバーを通じて、エージェントが読み取り専用のDuckDB SELECT文を使用してWebデータを検索できるように設計されています。"
  - question: "Keenableが保有するWeb検索インデックスの規模はどの程度ですか？"
    choices: ["約10億件のドキュメント", "約500億件のドキュメント", "1,000億件以上のドキュメント"]
    answer: 2
    explanation: "Keenableは、独自のクローラーとインデックスシステムを通じて1,000億件以上のドキュメントを保有しています。"
  - question: "Keenable APIが提供する特別な検索機能は何ですか？"
    choices: ["過去のある時点におけるインターネットの状態を照会する機能", "個人情報の暗号化自動生成", "無制限の無料利用"]
    answer: 0
    explanation: "Keenableは、モデルが現在の状態だけでなく、過去のある時点のインターネットを検索できるようにする「時点（point-in-time）記録クエリ」をサポートしています。"
lang: ja
ref: 2026-09-02-Keenable-SELECT-an-agent-that-searches-the-web-in-SQL
---

想像してみてください。あなたが秘書に「昨日ニュースで取り上げられていたあの企業の株価と関連記事をすべてまとめてきて」と頼んだとします。ところが秘書が戻ってきて、何万ページ分もの複雑で散らかった書類の束を投げ出し、「ここから自分で探してください」と言ったらどうでしょう？おそらく怒りを覚えるはずです。

これまでAIエージェントがインターネットを検索する際に直面していた状況は、まさにこれと同じでした。大半の検索APIは人間が読みやすいように作られているか、あるいはAIが改めて精査しなければならない散らかったデータ（JSONやHTMLの塊）を吐き出すものだったからです。しかし、最近になってこうした非効率を解決するために登場した技術があります。それが**「Keenable SELECT」**です。

## なぜ重要なのか？

これまでAIエージェント（自ら判断し、複雑なタスクを実行する人工知能）は、Web情報を得るために検索APIを使用してきました。しかし、既存の検索APIは主に人間のユーザー向けに設計されていたため、エージェントが複雑なタスクを行うたびにデータを一つ一つクリーニングしなければならない「追加作業」が必要でした [Source 13, Source 16]。

Keenable SELECTはこの過程をスキップさせてくれます。私たちが普段データベースを扱う際に使う**SQL（Structured Query Language、データの照会・管理のための標準言語）**の構文を、Web検索にそのまま導入したからです。おかげで開発者は、エージェントに必要なデータだけを「ピンポイント」で抽出するよう命令できるようになりました。エージェントが不要な情報の解釈に時間を浪費することなく、複雑な業務をより迅速かつ正確に処理できるようになったのです。

## わかりやすい例え：図書館司書の比喩

Keenable SELECTを理解するために「図書館司書」の例えを使ってみましょう。

従来の検索エンジンが図書館司書に「料理の本を全部探して」と言ったとき、司書が何千冊もの料理本を机の上に山積みにして「ここから必要なのを探してください」と答えるようなものだとしたら、Keenable SELECTは違います。この技術は、司書に**「2025年以降に出版された、15分以内で作れる韓国料理のレシピだけを厳選してリストにして」**と詳細な条件をつけて注文するようなものです。

技術的には、**モデルコンテキストプロトコル（MCP、AIエージェントのための標準通信ルール）**サーバー内で「select」というツールを実行します [Source 12]。エージェントが「SELECT * FROM web WHERE...」のようなSQL文を入力すると、Keenableの独自システムがWebデータを読み込み、きれいな行（row）形式に整理してエージェントに伝えます [Source 12]。エージェントの立場からすれば、複雑なWebページの構造を解釈するためにわざわざ力を割く必要がなくなるわけです。

## 現在の状況

Keenableは単なるツールではなく、AIエージェント専用に設計された独自のインフラです [Source 8, Source 15]。その規模も相当なものです。

- **膨大な知識:** Keenableは独自のクローラーとインデックスシステムを構築し、1,000億件以上のドキュメントをデータベース化しました [Source 5, Source 6, Source 8]。
- **高速なスピード:** AIエージェントがリアルタイムで業務を処理できるよう、米国東部（us-east）リージョン基準でリクエストの95%が250ミリ秒（0.25秒）以内に処理されるよう最適化されています [Source 5]。
- **歴史的データのサポート:** 特に興味深いのが「時点記録クエリ」です [Source 9]。これはエージェントが現在のインターネット情報だけでなく、過去のある日付にインターネット上に存在していた情報だけを照会できるようにします [Source 9]。

このサービスは最近、2,600万ドル（日本円で約38億円以上）の資金調達に成功し、その技術力を認められました [Source 4, Source 6, Source 9, Source 16]。すでに複数のAI研究所やデータ提供業者が、学習および実際のサービス運用過程でこのAPIを使用しています [Source 6]。

## 今後はどうなるのか？

Keenable SELECTの登場は、「エージェント時代」の検索がどこへ向かっているのかを示しています。今後はAIが単に「検索して」と命令するだけでなく、データベースを扱うかのように洗練されたクエリをWebに投げかけることが標準になるでしょう。ユーザーが「先月と比較して上昇した環境関連企業の株価を表にして」と頼んだとき、AIエージェントがわずか数行のSQL文だけでWebから即座にデータを抽出し、回答する時代がすぐそこまで来ています。

## MindTickleBytesのAI記者による視点

人間向けの検索とAI向けの検索は、根本的に異なるべきです。KeenableのSQLインターフェースは、エージェントがWebと対話する方法を一段と進化させるでしょう。AIはWebを「読む」存在から、Webを「クエリする（問い合わせる）」存在へと変わろうとしています。

## 参考資料

1. [Web Search & Extract | Hermes Agent - NOUS RESEARCH](https://hermes-agent.nousresearch.com/docs/user-guide/features/web-search)
2. [SQL Agent | Use Natural Language to Query Databases](https://www.snaplogic.com/ai-agent-showcase/sql-queries)
3. [Examples of Using Select AI Agent](https://docs.oracle.com/en-us/iaas/autonomous-database-serverless/doc/examples-using-select-ai-agent.html)
4. [What is Keenable: The 'AI Agent-Only' Search API Built by Former Yandex Search Leaders, and the Details of Their $26 Million Funding｜アイドリ | AI-Driven Lab](https://note.com/ai_driven/n/n1639bb95690d?hl=en)
5. [Show HN: Keenable – A different web search API for AI agents | Hacker News](https://news.ycombinator.com/item?id=49435555)
6. [Accel-backed Keenable is indexing the web for AI agents | TechCrunch](https://techcrunch.com/2026/08/25/accel-backed-keenable-is-indexing-the-web-for-ai-agents/)
7. [How to Build an AI Agent That Searches the Web: Tools & Setup](https://syllable.ai/blog/how-to-build-ai-agent-with-search-tools)
8. [Keenable.ai — Independent Web Search API for AI](https://keenable.ai/)
9. [Agentic web search infrastructure startup Keenable raises $26M - SiliconANGLE](https://siliconangle.com/2026/08/25/agentic-web-search-infrastructure-startup-keenable-raises-26m/)
10. [hermes-agent/website/docs/user-guide/features/web-search.md at main · NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/web-search.md)
11. [Quickstart - Keenable](https://docs.keenable.ai/)
12. [KeenableSELECT: an agent that searches the web in SQL](https://keenableai.github.io/select-showcase/)
13. [[IndustryNews] Keenable is trying to fix how AI agents actua...](https://promptcube3.com/en/news/7679/)
14. [Keenable: Agent-First Search API Architecture and the 100B Page Index Trade-Off - DEV Community](https://dev.to/mech_app_ai/keenable-agent-first-search-api-architecture-and-the-100b-page-index-trade-off-259b)
15. [Keenable exits stealth mode with $26M seed round to build search...](https://cryptobriefing.com/keenable-26m-seed-ai-search-index/)