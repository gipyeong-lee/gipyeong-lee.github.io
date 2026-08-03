---
layout: post
title: "AIに「仕事のやり方」を教えるとトークンは節約できるのか？興味深い実験結果"
description: "AIアシスタントに特定の技術を教える「Codexスキル」が、AIモデルのトークン消費量と効率に与える影響についての実験分析"
summary: "AIアシスタントにモジュール型指示である「Codexスキル」を提供することで、作業効率を高め一貫性を改善できるという実験結果を紹介します。"
tags: [AI, Codex, トークン節約, 技術実験, MindTickleBytes]
image: 2026-08-03-Show-HN-Do-Codex-skills-save-tokens-A-six-run-task-size-benchmark.jpg
image_alt: "AIアシスタントが複雑なコーディング作業を処理し、トークンの効率を最適化する姿を形にしたイメージ"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AIの作業効率は単なるモデルの性能を超え、いかに洗練された「指示構造」を提供するかにかかっています。Codexスキルは、人が働くやり方をAIに伝授するための重要な媒介です。"
quiz:
  - question: "Codexスキルが保存されるファイル形式は何ですか？"
    choices: ["CODE.txt", "SKILL.md", "INSTRUCT.json"]
    answer: 1
    explanation: "Codexスキルは、メタデータと指示が含まれるSKILL.mdファイルを通じて管理されます。"
  - question: "Codexスキルをプロジェクトに簡単にインストールするために使用するツールは？"
    choices: ["skills CLI", "npm install", "git clone"]
    answer: 0
    explanation: "skills CLIを使用すると、プロジェクトルートで手軽にスキルをインストールし管理できます。"
  - question: "この記事で紹介された「Codexスキル」の主な目的は何ですか？"
    choices: ["AIの記憶力向上", "作業効率および一貫性の改善", "モデル学習速度の増加"]
    answer: 1
    explanation: "Codexスキルは、AIに特定の作業を望む方法で実行するようにガイドし、効率と一貫性を高めることを目的としています。"
lang: ja
ref: 2026-08-03-Show-HN-Do-Codex-skills-save-tokens-A-six-run-task-size-benchmark
---

想像してみてください。新入社員に業務指示を出すたびに、会社のあらゆる規則や手順をA4用紙100枚に書いて渡さなければならないとしたら。効率的であるはずがありません。AIアシスタントである「OpenAI Codex（コード作成を支援する人工知能モデル）」を使う際も、似たような問題が発生します。AIに作業を依頼するたびに詳細なガイドを提供していると、肝心の作業を処理する前に、対話データ量である「トークン（AIがテキストを処理する最小単位）」ばかりを消費してしまうからです。

最近、この問題を解決するためにAIに「スキル（Skill）」を教える手法が注目されています。果たしてAIに具体的な業務マニュアルを事前に学習させると、コストや効率面でどれほど大きな差が出るのでしょうか？最近行われた実験を通じて、その疑問を解き明かしてみます。

## なぜこれが重要なのか？

AIを業務に活用する企業や個人にとって、「トークン」はすなわちコストです。トークンの消費量が増えれば運営コストが急増するだけでなく、AIが処理できる作業の複雑さや速度にも制約が生じます。[Codex使用制限（Codex Resets）](https://codex-resets.com/)のような状況に見られるように、トークンの効率性を高めることは、AIアシスタントを安定的かつ経済的に活用するための必須課題です。今回の研究は、AIに「どう働くべきか」を事前に定義されたパッケージで伝える手法が、実質的なコスト削減と作業品質の向上につながることを示しています。

## 簡単に理解する：「Codexスキル」とは？

「Codexスキル」とは、AIに特定の業務を遂行する方法を教える「モジュール型指示バンドル（機能を単位別にまとめた指示集）」です。[Composioの関連ドキュメント（GitHub - composio-community/awesome-codex-skills）](https://github.com/composio-community/awesome-codex-skills)によると、各スキルは固有のフォルダに収められており、その中には「SKILL.md」というファイルが入っています。このファイルには当該スキルの名前、説明、そしてAIが業務を遂行する際に従うべきステップ別の指示が含まれています。[出典：OpenAI Codexスキル（OpenAICodexSkills）](https://agentskill.sh/for/codex)

これを写真加工アプリの「フィルター」に例えることができます。フィルターが適用されていない写真は、ユーザーが直接色味、コントラスト、明るさを一つ一つ調節しなければなりません。しかし、あらかじめよく設定された「感性フィルター」を適用すれば、ボタン一つで望む雰囲気の写真を得られます。Codexスキルも同じです。AIに毎回最初から最後まで指示を出す必要はなく、「コード生成」、「テスト」、「デバッグ（プログラム内のエラーを探して修正する作業）」のような特定のスキルパッケージを読み込むだけで、AIはすでに知っている専門家のように振る舞うようになります。[出典：エージェントスキルマーケットプレイス（AgentSkillsMarketplace）](https://skillsmp.com/)

## 現状：どこまで活用可能か？

現在、Codexスキルエコシステムは急速に成長しています。すでに34,788個以上のスキルが開発されており、コード生成はもちろん、テスト、デバッグ、デプロイ、さらには自律的な開発業務まで遂行できるレベルです。[出典：OpenAI Codexスキル（OpenAICodexSkills）](https://agentskill.sh/for/codex)

また、単なるテキスト作業にとどまりません。例えば、UIデザイン分野ではブラウザと連携して直接画面をレンダリングし、ブレークポイント（画面サイズに応じてレイアウトが変わる地点）に合わせてUIを修正する作業まで遂行します。[出典：デザインのためのCodex（Codexдля дизайна）](https://open-design.ai/ru/agents/codex-design/) これらのスキルは「skills CLI（コマンドラインインターフェースツール）」を通じてプロジェクトルートに簡単にインストールでき、一度インストールされれば、AIが複数のセッションにわたってそのガイドを参照するようになります。[出典：Codex用スキル（SkillsforCodex）](https://www.skills.sh/agent/codex)

## 今後はどうなるか？

最近では、異なる作業サイズ（Task-size）を持つ環境において、「Lean（簡潔な）スキル」が従来の手法よりもどれほどトークンを節約できるかを比較する実験が行われています。[出典：Codexスキルトークン節約実験（DoCodexskillssavetokens?）](https://community.openai.com/t/do-codex-skills-save-tokens-six-controlled-gpt-5-6-sol-runs/1388837) 今後は、数万個のスキルの中から自分の作業にぴったりの最適なスキルを組み合わせ、AIアシスタントを「個人秘書」レベルまで高度化する時代が来るでしょう。すでにアニメーション制作、ウェブサイト構築、アプリ自動化など、多様な実務事例が続々と登場しています。[出典：2026年トップ10 Codexスキル（Top 10CodexSkillsin 2026）](https://composio.dev/content/top-codex-skills)

## MindTickleBytesのAI記者の視点

AIに洗練された指示を「スキル」として提供することは、AIを単なるツールから真のパートナーへと進化させるプロセスです。私たちがAIにより明確なルールを教えるほど、AIはより少ないリソースでより多くの価値を創造するでしょう。今、AIに単に仕事をやらせる段階を越え、専門家のように働けるよう教える「スキルの時代」が幕を開けています。

## 参考資料

1. [Codexスキルトークン節約実験（DoCodexskillssavetokens?）](https://community.openai.com/t/do-codex-skills-save-tokens-six-controlled-gpt-5-6-sol-runs/1388837)
2. [Codex使用制限（Codex Resets）](https://codex-resets.com/)
3. [OpenAI Codexスキル（OpenAICodexSkills）](https://agentskill.sh/for/codex)
4. [GitHub - composio-community/awesome-codex-skills](https://github.com/composio-community/awesome-codex-skills)
5. [2026年トップ10 Codexスキル（Top 10CodexSkillsin 2026）](https://composio.dev/content/top-codex-skills)
6. [エージェントスキルマーケットプレイス（AgentSkillsMarketplace）](https://skillsmp.com/)
7. [Codex用スキル（SkillsforCodex）](https://www.skills.sh/agent/codex)
8. [ClaudeコードおよびCodexのためのトップ10デザインスキル（Top 10 DesignSkillsfor ClaudeCodeandCodex）](https://composio.dev/content/top-design-skills)
9. [デザインのためのCodex（Codexдля дизайна）](https://open-design.ai/ru/agents/codex-design/)