---
layout: post
title: "私のコーディングAIがハッキングの入り口に？「トロイの木馬」化したClaude Code拡張機能に注意喚起"
description: "最近、開発ツールを装ってユーザーのコンピュータに侵入するマルウェアの脅威が急増しています。Claude Code拡張機能を騙った攻撃の実態と予防法について解説します。"
summary: "公式の開発ツールを装った悪意ある拡張機能や、偽のソースコード流出ファイルを介して開発者のコンピュータにバックドアを設置し、情報を盗み出すハッキング事例が報告されています。"
tags: [セキュリティ, AI, 開発者, ClaudeCode, マルウェア]
image: 2026-10-30-Trojanized-Claude-Code-Extension-Plants-an-SSH-Backdoor.jpg
image_alt: "コンピュータ画面上にトロイの木馬のロゴと警告メッセージが浮かんでいるサイバーセキュリティ関連のイラスト"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AIの能力を借りようとする開発者の熱望を犯罪の道具として悪用するのは、極めて卑劣な手法です。技術を利用する際は、必ず公式チャンネルを確認するデジタル衛生習慣が不可欠です。"
quiz:
  - question: "最近、開発者を標的とする攻撃者は主に何を狙っていますか？"
    choices: ["AIモデル自体の重み", "開発者のアカウント認証情報（Credential）", "AIのサーバー用電気料金"]
    answer: 1
    explanation: "最近、AIコーディングツールを攻撃する主体は、AIモデルではなく、そのツールを使用する開発者のコンピュータやアカウント情報を奪うことに注力しています。"
  - question: "マルウェアが侵入する主な経路ではないものはどれですか？"
    choices: ["公式Claudeウェブサイト（claude.com）", "トロイの木馬が仕込まれた偽の『Claude Code流出』リポジトリ", "偽のClaude AIウェブサイトの広告"]
    answer: 0
    explanation: "公式ウェブサイトは安全です。主にそれを騙った偽サイトや、非公式なソースコード流出リポジトリを通じてマルウェアが配布されます。"
  - question: "拡張機能を騙った攻撃の特徴として正しいものはどれですか？"
    choices: ["単なる広告ポップアップを表示する", "ユーザーのコンピュータにSSHバックドアを設置し、持続的なリモートアクセスを試みる", "AIの回答速度を遅くする"]
    answer: 1
    explanation: "攻撃者は感染したコンピュータにSSHバックドアを仕込み、開発者が気づかないうちにシステムへ持続的にリモート接続してデータを抜き取ります。"
lang: ja
ref: 2026-10-30-Trojanized-Claude-Code-Extension-Plants-an-SSH-Backdoor
---

想像してみてください。コーディング作業の効率を上げてくれるAIツールをインストールし、ワクワクした気持ちで作業を始めたとします。ところが実際には、そのツールがあなたのコンピュータの扉をこっそりと開け放ち、ハッカーがいつでも入れるように「秘密の通路」を作っていたとしたらどうでしょうか？最近、開発者の間でこのような悪夢のような出来事が現実のものとなっています。

現在、[Claude Code](https://www.zscaler.com/blogs/security-research/anthropic-claude-code-leak)のような人気AIコーディングツールの人気を悪用し、開発者の情報を盗み出してシステム権限を奪おうとするサイバー攻撃が横行しています。

## なぜこれが重要なのか？

この問題は、単に「ウイルス」に感染する以上の危険をはらんでいます。AIコーディングツールは、私たちが作成するソースコード、クラウドのアクセス権限、データベースのパスワードなど、非常に機密性の高い情報にアクセスできるためです。

もし攻撃者がこうしたツールを通じてコンピュータに侵入できれば、開発者個人の情報を超えて、その開発者が所属する企業全体のセキュリティ網が突破される可能性もあります。実際に2025年から2026年にかけて、[Claude CodeだけでなくGitHub Copilot、OpenAI Codexなど、主要なAIコーディングエージェントが次々とセキュリティ脅威にさらされたことがあります。](https://moccet.ai/news/tech/claude-code-copilot-and-codex-all-got-hacked-every-attacker-went-for-the-credent) 攻撃者たちはAIモデル自体の性能を損なうことよりも、モデルを使用する**開発者のアカウント認証情報（Credential、ユーザー識別およびアクセス権限情報）**を直接狙っています。

## わかりやすく解説

今回の攻撃の核心は**「トロイの木馬」**戦略です。ギリシャ神話でトロイア軍が美しい木馬の中に兵士を隠して城内に入り込んだように、ハッカーたちも悪質なソフトウェアを非常に有益なAI拡張機能やソースコードであるかのように装います。

1. **なりすまし戦術**: ハッカーたちは公式Claudeウェブサイトとそっくりな[偽ウェブサイト](https://www.notebookcheck.net/Fake-Claude-AI-website-is-pushing-a-Windows-backdoor-through-Google-search-results.1291664.0.html)を作ったり、「コード流出分」と偽ったファイルを配布したりします。
2. **侵入**: 開発者がこれをダウンロードして実行すると、そのプログラムはコンピュータに[ビーグル（Beagle）Windowsバックドア](https://www.linkedin.com/posts/bleepingcomputer_cybersecurity-windowssecurity-malware-activity-7458094379153502208-JG7C)やVidarのようなマルウェアをインストールします。
3. **秘密の通路**: このマルウェアは[SSHバックドア（システムに秘密裏にアクセスするための裏口）](https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor)を仕込み、外部のハッカーがまるでコンピュータの持ち主であるかのようにいつでも入れる「リバースSSHトンネル」を作成します。

例えるなら、ツールをインストールする行為が、実はハッカーに「我が家の合鍵はここですよ」と親切に教えているようなものなのです。私たちが扉を開けた瞬間、ハッカーはその扉を通って家（コンピュータ）に勝手に出入りし、大切な資産（データ）を盗み出していくのです。

## 現在の状況

状況は思ったより深刻です。今年4月には、[数万人もの人々が「Claude Code」のソースコードが流出したというニュースに飛びつきファイルをダウンロードしましたが、その大部分に情報窃取型のマルウェアが含まれていました。](https://www.theregister.com/2026/04/02/trojanized_claude_code_leak_github/?ref=biztoc.com)

セキュリティ調査機関のZscalerは、[anthropic.claude-code@2.1.313バージョンに成り済ましたトロイの木馬型拡張機能がすでに発見されていると警告](https://github.com/nirholas/fresh-start)しました。この拡張機能はインストールされた瞬間、攻撃者のサーバーと通信してシステムを掌握します。現在、攻撃者はGoogle検索広告まで活用して偽サイトを検索結果の上位に表示させるなど、非常に巧妙な手口を使っています。

## 今後はどうなるのか？

今後、AIコーディングツールは開発プロセスにおいて欠かせない必需品となるでしょう。そのため、攻撃者の標的もより一層精巧になるはずです。[Anthropicが提供する公式CLI（コマンドラインインターフェース）ツールのみを使用](https://github.com/nirholas/fresh-start)し、非公式なルートで流出したソースコードは絶対にダウンロードしないことが重要です。

今後はツールをインストールする際、デジタル署名を確認したり、信頼できる開発者コミュニティの検証を経た公式バージョンかどうかをチェックしたりする習慣が、開発者の必須スキルとなるでしょう。セキュリティは単なる技術的な問題ではなく、毎日守る小さな習慣から始まります。

## AIの視点

賢いAIをパートナーにしたいという開発者の心を利用するような犯罪手段は、極めて卑劣で許されない行為です。しかし今回の事態は、私たちが「利便性」の裏に隠れた「セキュリティ」をどれほど疎かにしていたかを映し出す鏡でもあります。利便性よりも大切なのは、常に安全であることです。公式ルートを利用すること、それこそが最も速く安全な開発の始まりです。

## 参考資料

1. [Trojanized Claude Code Extension Plants a Persistent SSH Backdoor](https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor)
2. [Claude Code Leak: Critical AI Security Threat 2026](https://www.zscaler.com/blogs/security-research/anthropic-claude-code-leak)
3. [Fake Claude AI website is pushing a Windows backdoor through Google search results](https://www.notebookcheck.net/Fake-Claude-AI-website-is-pushing-a-Windows-backdoor-through-Google-search-results.1291664.0.html)
4. [Claude AI Site Spreads Beagle Windows Backdoor via Trojanized](https://www.linkedin.com/posts/bleepingcomputer_cybersecurity-windowssecurity-malware-activity-7458094379153502208-JG7C)
5. [Fake Claude Code source downloads actually delivered malware](https://www.theregister.com/2026/04/02/trojanized_claude_code_leak_github/?ref=biztoc.com)
6. [GitHub - nirholas/fresh-start: The original nirholas/claude-code before...](https://github.com/nirholas/fresh-start)
7. [AI Coding Agents Hacked: Claude Code, Copilot... | Moccet TechNews](https://moccet.ai/news/tech/claude-code-copilot-and-codex-all-got-hacked-every-attacker-went-for-the-credent)