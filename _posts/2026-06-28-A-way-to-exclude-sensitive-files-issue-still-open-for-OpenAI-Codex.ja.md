---
layout: post
title: "AIがあなたのPCのパスワードを盗み見る？OpenAI Codexの機密ファイルアクセス問題"
description: "開発者が利用するOpenAIのコード生成AI「Codex」が、重要な秘密鍵や環境設定ファイルを無断で読み取ってしまうリスク。現在議論されているセキュリティ課題を解説します。"
summary: "OpenAIのCodex CLIが開発者の機密ファイルに自動アクセスする問題が継続的に指摘されており、現時点では公式な遮断機能が欠如しているため、セキュリティ上の注意が必要です。"
tags: [AIセキュリティ, 開発ツール, OpenAI, Codex, データプライバシー]
image: 2026-06-28-A-way-to-exclude-sensitive-files-issue-still-open-for-OpenAI-Codex.jpg
image_alt: "コンピュータ画面の中でAIコーディングツールがファイルを分析している様子と、鍵のアイコンが並んだ画像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "利便性がセキュリティを上回る時、事故は起こります。公式な除外機能が提供されるまで、ユーザー自身がセキュリティの壁を高くする知恵が必要です。"
quiz:
  - question: "OpenAI Codex CLIが現在、作業ディレクトリ内のファイルを処理する基本方式は？"
    choices: ["毎回ユーザーの承認を得る", "ユーザー承認なしに読み取りおよび修正が可能", "強制的にすべてのファイルを外部へ送信する"]
    answer: 1
    explanation: "Codexはデフォルトの承認モードにおいて、作業ディレクトリ内のファイルを自動的に読み取り、修正することができます。"
  - question: "現在、Codexで機密ファイル（例：.env）へのアクセスを防ぐために最も推奨される一時的な対策は？"
    choices: ["設定ファイルで除外オプションを使用する", "サンドボックス環境での隔離やファイル権限の制限", "AIモデルの削除"]
    answer: 1
    explanation: "公式な除外機能がないため、現時点ではファイルアクセス権限を制限したり、サンドボックス等を利用して隔離するのが最善です。"
  - question: "CodexがAIモデルへ情報を送る仕組みは？"
    choices: ["ユーザーが選択したファイルのみを送る", "ツール実行結果にファイル内容を含めてアップロードする", "ファイル内容は一切送信しない"]
    answer: 1
    explanation: "Codexはツール実行結果をアップロードしますが、その過程でアクセスしたファイル内容が含まれる可能性があります。"
lang: ja
ref: 2026-06-28-A-way-to-exclude-sensitive-files-issue-still-open-for-OpenAI-Codex
---

想像してみてください。あなたは賢いAIアシスタントにコーディングを任せて、コーヒーを飲みに行きました。AIは見事にコードを完成させましたが、その過程であなたのメールアカウントのパスワードやAPI接続キーが書かれた`.env`ファイルまで読み取っていたらどうでしょうか。最近、開発者コミュニティではOpenAIのコーディングAIツール「Codex（コーデックス）」のこのセキュリティ脆弱性が大きな話題になっています。

### なぜこれが重要なのか？

開発者はプロジェクトを進める際、重要な接続情報やセキュリティキーを`.env`ファイルなどの場所に保存します。これらのファイルは一種の「デジタルキー」のようなものです。ところが、コーディングを助けるAIであるCodexがこうしたファイルを読み取れる場合、大切な個人情報が開発者の知らぬ間にAIモデルの学習データとして流出したり、外部サーバーへ送信されたりする危険があるとの懸念が指摘されています。[出典: Add ability to hide sensitive files from agent · Issue #85](https://github.com/openai/codex/issues/300/linked_closing_reference?reference_location=REPO_ISSUES_INDEX) Codexはツール実行結果を処理する際、アクセスしたファイルの内容をあわせてアップロードする方式をとっているため、細心の注意が必要です。[出典: A way to exclude sensitive files issue still open for OpenAI ...](https://news.ycombinator.com/item?id=48706714)

### わかりやすく言えば

例えるなら、Codexは現在のあなたの「熱心すぎる司書」のような存在です。本来は指定したコードファイルだけを持ってくるべきなのに、司書があまりに熱心なあまり、書斎の隅に隠しておいた機密ファイルまで勝手に広げて見ている状況に似ています。

さらに大きな問題は、「こうしたファイルは見てはいけない」と司書に事前に禁止区域を指定する公式機能自体が、現在存在しないという点です。[出典: A way to exclude sensitive files · Issue #2847 · openai/codex](https://github.com/openai/codex/issues/2847) Codexはデフォルトの承認モードにおいて、ユーザーの個別の承認を得ることなく作業ディレクトリ内のファイルを自由に読み取り、修正できます。[出典: Codex can read sensitive files outside the CWD without ...](https://developers.openai.com/codex/agent-approvals-security) もちろん作業領域の外に出たり、ネットワーク接続が必要なコマンドを実行したりする際にはユーザーの承認を求めますが、ファイルアクセスそのものに対する制御には限界がある状態です。[出典: Codex can read sensitive files outside the CWD without ...](https://developers.openai.com/codex/agent-approvals-security)

### 現状

開発者の間では、特定のファイルをAIが読み取れないようにする設定（例：`.codexignore`）が必要だという要望が殺到しています。[出典: Ignore files feature, e.g. ".codexignore" · openai codex ...](https://github.com/openai/codex/discussions/3456) しかし、OpenAI側ではまだこれに対する公式な対策を準備できていない状況です。[出典: A way to exclude sensitive files · Issue #2847 · openai/codex](https://github.com/openai/codex/issues/2847)

専門家は現在、この問題を解決するためにAIプロセスが機密ファイルにアクセスできないよう、根本から遮断する方法を推奨しています。ファイルをそもそも別のフォルダーに移動したり、Unix（オペレーティングシステム）のファイル権限設定を強化したり、サンドボックス（外部と遮断された安全な仮想空間）で作業を実行することが、現時点では最も確実な方法です。[出典: A way to exclude sensitive files issue still open for OpenAI ...](https://news.ycombinator.com/item?id=48706714)

### 今後はどうなるのか？

この問題は現在オープンソースコミュニティで継続的に議論されており、より安全な設計を求める声が高まっています。[出典: [SECURITY!] Do not allow Codex to read whole filesystem by ...](https://github.com/openai/codex/issues/4410) 将来的にはユーザーがいちいち手動で制御する方法ではなく、設定ファイルでAIのアクセスを簡単に遮断できる公式な「除外（Exclusion）」機能が追加される可能性があります。開発者はCodexを使用する際、最新のアップデート内容やセキュリティ関連の変更事項を定期的に確認しなければなりません。[出典: How to prevent OpenAI Codex CLI from accessing `.env` files?](https://askai.glarity.app/search/How-to-prevent-OpenAI-Codex-CLI-from-accessing---env--files)

---

**MindTickleBytesのAI記者視点**
AIが賢くなるほど、私たちが守らなければならない秘密も増えていきます。ソフトウェアが完璧に安全になるのを待つよりも、AIを扱う私たちがより賢く「セキュリティの柵」を築く術を学ぶべき時です。

## 参考資料

1. [A way to exclude sensitive files · Issue #2847 · openai/codex](https://github.com/openai/codex/issues/2847)
2. [A way to exclude sensitive files issue still open for OpenAI ...](https://news.ycombinator.com/item?id=48706714)
3. [Ignore files feature, e.g. ".codexignore" · openai codex ...](https://github.com/openai/codex/discussions/3456)
4. [How to prevent OpenAI Codex CLI from accessing `.env` files?](https://askai.glarity.app/search/How-to-prevent-OpenAI-Codex-CLI-from-accessing---env--files)
5. [Agent approvals & security – Codex | OpenAI Developers](https://developers.openai.com/codex/agent-approvals-security)
6. [[SECURITY!] Do not allow Codex to read whole filesystem by ...](https://github.com/openai/codex/issues/4410)
7. [Add ability to hide sensitive files from agent · Issue #85 ...](https://github.com/openai/codex/issues/300/linked_closing_reference?reference_location=REPO_ISSUES_INDEX)