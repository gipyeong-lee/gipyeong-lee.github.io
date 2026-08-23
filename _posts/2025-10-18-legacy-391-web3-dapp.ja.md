---
layout: post
title: "生涯初のDappを完成させました。"
description: "こんにちは。Slow Thinkingです。約1ヶ月間開発を進めてきました。AIがいなければ完成できなかったでしょう。怠け者の私が選んだ方法は次の通りです。Visual Studio Codeの左右のパネルにそれぞれCodexとClaude Codeをセットアップし、To..."
date: 2025-10-18 20:57:34 +0900
section: blog
category: web3
lang: ja
ref: 2025-10-18-legacy-391-web3-dapp
tags:
  - "Ai"
  - "Claude"
  - "Codex"
  - "DAPP"
  - "Project"
  - "Projects"
translation_source_hash: 80e0e93d306232af16e6f6d408598d3b9b8be3d0a9bae18b179452ac9bae1aa4
---

<p>
こんにちは。Slow Thinkingです。
</p>
<p>
約1ヶ月間、開発を進めてきました。
</p>
<p>
AIがいなければ開発できなかったでしょう。
</p>
<p>
怠け者の私が選んだ方法は次の通りです。
</p>

<p>
Visual Studio Codeの左右のパネルにそれぞれCodexとClaude Codeをセットアップしました。
</p>
<p>
トークン制限に達したら交互に作業を進めました。以下は、両方のツールを比較した表です。参考にしてください。
</p>

<table>
<tbody>
<tr>
<td>
<b>
項目
</b>
</td>
<td>
<b>
Codex CLI ( OpenAI )
</b>
</td>
<td>
<b>
Claude Code CLI (Anthropic)
</b>
</td>
</tr>
<tr>
<td>
<b>
プラン名
</b>
</td>
<td>
ChatGPT Plus (月額20ドル) 内のCodex CLIを含む
</td>
<td>
Claude Pro (月額20ドル)
</td>
</tr>
<tr>
<td>
<b>
セッション制限方式
</b>
</td>
<td>
約
<b>
5時間のローリングウィンドウ
</b>
(5時間ごとに使用量がリセット)
</td>
<td>
約
<b>
5時間のローリングウィンドウ
</b>
(5時間ごとにリセット)
</td>
</tr>
<tr>
<td>
<b>
セッション上限 (概算)
</b>
</td>
<td>
約30〜150件のローカルメッセージ、または5〜40件のクラウド作業
</td>
<td>
約45メッセージ、または10〜40プロンプトレベル
</td>
</tr>
<tr>
<td>
<b>
週間累積上限
</b>
</td>
<td>
<b>
共有週間割当枠 (weekly quota)
</b>
が存在 (公式数値は非公開)
</td>
<td>
約
<b>
7日単位
</b>
でリセットされる週間上限が存在
</td>
</tr>
<tr>
<td>
<b>
リセット時点 (セッション)
</b>
</td>
<td>
初のリクエストから5時間経過後に自動リセット
</td>
<td>
初のリクエストから5時間経過後に自動リセット
</td>
</tr>
<tr>
<td>
<b>
リセット時点 (週間)
</b>
</td>
<td>
約
<b>
1週間
</b>
周期でリセット (正確な時刻は非公開)
</td>
<td>
約
<b>
7日
</b>
後にリセット (アカウントにより時間は異なる)
</td>
</tr>
<tr>
<td>
<b>
トークンコンテキストウィンドウ
</b>
</td>
<td>
約
<b>
192,000トークン
</b>
(入力 + 出力 + 履歴を合計した推定値)
</td>
<td>
約
<b>
200,000トークン
</b>
(Pro基準)、最大500,000 (Enterprise)
</td>
</tr>
<tr>
<td>
<b>
基本モデル
</b>
</td>
<td>
GPT-4 Turbo (コード解釈用モード)
</td>
<td>
Claude 3 Sonnet (コーディングモード)
</td>
</tr>
<tr>
<td>
<b>
超過時のメッセージ
</b>
</td>
<td>
“Usage limit reached. Try again in X hours.”
</td>
<td>
“You’ve hit your limit. Resets in ~X hours.”
</td>
</tr>
<tr>
<td>
<b>
リセット方式
</b>
</td>
<td>
自動ローリングリセット (手動初期化不可)
</td>
<td>
自動ローリングリセット (5時間後にセッション更新)
</td>
</tr>
<tr>
<td>
<b>
追加機能
</b>
</td>
<td>
- ローカル作業とクラウド作業の区分 - コード実行機能を含む
</td>
<td>
- /clear、/compactコマンドでコンテキストの圧縮が可能 - Sonnet 4中心のモデルサポート
</td>
</tr>
<tr>
<td>
<b>
公式出典例
</b>
</td>
<td>
<a href="https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan">
help.openai.com
</a>
</td>
<td>
<a href="https://claudelog.com/faqs/claude-code-usage/">
claudelog.com
</a>
/
<a href="https://portkey.ai/blog/claude-code-limits/">
portkey.ai
</a>
</td>
</tr>
</tbody>
</table>

<p>
次は、今回のProject Lに関する情報です。
</p>


<table>
<tbody>
<tr>
<td>
<b>
プロジェクト名
</b>
</td>
<td>
Project L
</td>
</tr>
<tr>
<td>
<b>
開発言語
</b>
</td>
<td>
Rust (オンチェーンプログラム) + TypeScript (クライアント / フロントエンド)
</td>
</tr>
<tr>
<td>
<b>
プラットフォーム
</b>
</td>
<td>
Solana Blockchain (Anchor Framework )
</td>
</tr>
<tr>
<td>
<b>
開発期間
</b>
</td>
<td>
2025.09.29 ~ 2025.10.18 (合計19日間、38時間)
</td>
</tr>
<tr>
<td>
<b>
主な目標
</b>
</td>
<td>
Solanaネットワーク上でのスマートコントラクトのデプロイおよびクライアント連携の完了
</td>
</tr>
<tr>
<td>
<b>
依存関係グラフ
</b>
</td>
<td>
合計2,130件の依存関係 (パッケージ、モジュール、ビルド依存関係を含む)
</td>
</tr>
</tbody>
</table>

<p>
開発は完了し、現在セルフQAを行っている最中です。
</p>
<p>
その後、リリースを行う予定です。
</p>

<hr>

<blockquote>
<s>
devnet QA - 完了
</s>
<br>
testnet QA -
<b>
進行中
</b>
<br>
Deploy on mainnet - 未着手
</blockquote>