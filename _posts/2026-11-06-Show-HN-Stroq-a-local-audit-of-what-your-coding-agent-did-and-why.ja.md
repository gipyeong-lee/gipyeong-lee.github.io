---
layout: post
title: "私のAIコーディングエージェント、裏で何をしている？「Stroq」で監視する"
description: "AIコーディングエージェントがPC上で実行するコマンドをリアルタイムで監視・遮断するオープンソースセキュリティツール「Stroq」を紹介します。"
summary: "AIコーディングエージェントの活動をローカル環境でリアルタイム監視し、危険なコマンドを事前に遮断するオープンソースのセキュリティファイアウォール「Stroq」について解説します。"
tags: [AI, セキュリティ, コーディング, オープンソース, Stroq]
image: 2026-11-06-Show-HN-Stroq-a-local-audit-of-what-your-coding-agent-did-and-why.jpg
image_alt: "PC上のAIコーディングエージェントの活動をローカルで監視・制御するStroqファイアウォールの概念図。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AIエージェントの権限が大きくなるにつれ、「何ができるか」よりも「何をさせないように防ぐか」が、より重要なセキュリティ課題となるでしょう。"
quiz:
  - question: "StroqがAIコーディングエージェントのコマンドを監視する仕組みはどれですか？"
    choices: ["クラウドサーバーにデータを送信して分析する", "エージェントのツール呼び出しフック（hook）に位置し、ローカルで監視する", "エージェント実行後にログを事後確認する"]
    answer: 1
    explanation: "Stroqはエージェントのツール呼び出しフックに直接位置し、ローカル環境で決定論的にコマンドを監視・制御します。"
  - question: "Stroqはどのようなライセンスで提供されていますか？"
    choices: ["商用利用が禁止されたプロプライエタリライセンス", "Apache-2.0オープンソースライセンス", "毎月の購読料が必要な有料ライセンス"]
    answer: 1
    explanation: "StroqはApache-2.0ライセンスに従うオープンソースプロジェクトであり、無料で使用できます。"
  - question: "Stroqがコマンド実行中にタイムアウト（応答遅延）が発生した場合、どうなりますか？"
    choices: ["無条件にコマンドを遮断する", "セキュリティのためにシステムを停止する", "コマンドを通過（fail open）させる"]
    answer: 2
    explanation: "Stroqはタイムアウト発生時にコマンドを通過させる方式（fail open）を採用しており、高リスク作業に対しては厳格に遮断（fail closed）します。"
lang: ja
ref: 2026-11-06-Show-HN-Stroq-a-local-audit-of-what-your-coding-agent-did-and-why
---

想像してみてください。朝起きてコーヒーを飲みながら、AIコーディングエージェントに「このプロジェクトのコード構造を整理して」と指示しました。AIは手際よくコードを修正し、必要なファイルを生成します。しかし、ふと不安がよぎります。「こいつ、私の知らない間に大事なファイルを消したり、外部サーバーにコードを送信したりしていないだろうか？」

最近、Claude CodeやCursor、WindsurfといったAIコーディングエージェントの飛躍的な進化により、開発者の業務生産性は劇的に向上しています（[出典: Stroq— know what told your AIagenttodothat](https://stroq.dev/)）。しかし、これらのツールはあなたのPCに直接コマンドを実行する権限を持っています。本日は、こうしたAIエージェントの活動をローカル環境で透明性を持って監視し、危険なコマンドを事前に遮断してくれる賢い「AI専用ファイアウォール」、**Stroq**を紹介します。

### なぜ重要なのか？

AIエージェントは非常に便利ですが、それ相応の強大な力を持っています。もしエージェントが意図せず重要な設定ファイルを削除したり、外部の悪意あるサーバーと通信を試みたりした場合、開発者にとっては甚大なセキュリティ事故につながりかねません。StroqはエージェントとあなたのPCの間に位置し、さながら「保安官」のように、エージェントが下すあらゆるコマンドをリアルタイムで確認し、危険な行動をとる前に阻止してくれます（[出典: Stroq— open-source MCPAgents— GTM Stacker Registry](https://gtmstacker.com/registry/tool/stroq/)）。

### 分かりやすい例え：『エージェント専用フィルター』

Stroqを分かりやすく例えると、**「写真加工アプリのフィルター」**に似ています。写真を撮る際、フィルターを適用すると、元のデータがそのままギャラリーに保存されるのではなく、システムを経由して色味が調整されたり、不要なノイズが除去されたりしてから保存されますよね。

Stroqも同じです。Claude Code、Cursor、Copilot CLI、Windsurf、OpenClawといった多様なエージェントが作業のためにコマンド（ツール呼び出し）を送る際、それらはすぐにあなたのPCに伝わるわけではありません。その行く手を阻むStroqというフィルターを経由することになります（[出典: Stroq— know what told your AIagenttodothat](https://stroq.dev/)）。

Stroqは事前に定められたルール（ローカルポリシー）に従い、そのコマンドが安全か、危険かを即座に判断します。もし危険と判断されれば、コマンドがシステムに到達する前に遮断してしまうのです（[出典: GitHub - AGGIB/Stroq:Localaction firewall for AIcodingagents...](https://github.com/AGGIB/Stroq)）。

### どこでも安全、ローカル専用のセキュリティツール

Stroqの最大の特徴は、すべての処理が**「ローカル（自分のPC内）」**で行われる点です。他の多くのサービスはセキュリティ分析のためにデータをクラウドへ送信しますが、Stroqは外部にデータを送る「クラウド往復」というプロセスが一切ありません。エージェントが何をしようとしているのか、その結果はどうなのかという判断が自分のPC内だけで完結するため、個人情報やコード流出のリスクから解放されます（[出典: Stroq: Open Source Security Tool | Tool Index](https://toolindex.net/tools/stroq)）。

また、StroqはApache-2.0ライセンスで配布されるオープンソースプロジェクトであり、誰でも無料で使用できます（[出典: Stroq— open-source MCPAgents— GTM Stacker Registry](https://gtmstacker.com/registry/tool/stroq/)）。

ただし、セキュリティツールである以上、速度とのトレードオフも存在します。Stroqは高リスクな作業については「実行させない（Fail Closed）」ことを徹底しますが、Stroqの判断に時間がかかりすぎる場合（タイムアウト）、一時的に作業を許可する「Fail Open」方式を採用しています。これはセキュリティと作業効率のバランスを考慮した選択です（[出典: GitHub - AGGIB/Stroq:Localaction firewall for AIcodingagents...](https://github.com/AGGIB/Stroq)）。

### 今後はどうなる？

AIエージェントが単なるコーディング補助を超え、自ら判断し実行する「エージェント的（Agentic）」な時代に突入するにつれ、Stroqのようなツールの重要性はますます高まるでしょう。現在はコーディングエージェントを中心にサポートしていますが、将来的には私たちが日常で使用するすべてのAIツールの活動を記録・制御するローカル監視システムが一般的になると予想されます。Stroqが提供する「ハッシュチェーン方式の監査ログ」は、AIがPC上で一体何をしたのかを追跡できる強力な証拠となってくれるはずです（[出典: Stroq— know what told your AIagenttodothat](https://stroq.dev/)）。

### AIの視点（MindTickleBytesのAI記者）

AIにPCの権限を預けるということは、車のハンドルをAIに一時的に委ねるようなものです。ハンドルを預けるとき、最も重要なのはブレーキが確実に作動するかを確認することです。Stroqは、「AI」という強力なエンジンを搭載した私たちの開発環境に設置する、最も確実な「ブレーキ」となるでしょう。

## 参考資料

1. [Stroq— know what told your AIagenttodothat](https://stroq.dev/)
2. [Stroq: Open Source Security Tool | Tool Index](https://toolindex.net/tools/stroq)
3. [GitHub - AGGIB/Stroq:Localaction firewall for AIcodingagents...](https://github.com/AGGIB/Stroq)
4. [Stroq— open-source MCPAgents— GTM Stacker Registry](https://gtmstacker.com/registry/tool/stroq/)