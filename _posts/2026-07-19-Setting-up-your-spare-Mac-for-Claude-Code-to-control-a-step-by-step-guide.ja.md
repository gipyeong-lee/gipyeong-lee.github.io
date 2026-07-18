---
layout: post
title: "古いMacBookがAI秘書に？Claude CodeでMacを制御する方法"
description: "家に眠っている古いMacBookを活用し、AI秘書「Claude Code」をインストールして遠隔操作する方法をステップバイステップで解説します。"
summary: "使っていないMacBookをClaude Code専用のAI遠隔操作端末として設定し、普段の仕事用Macやスマートフォンから簡単に制御する方法を紹介します。"
tags: [AI, MacBook, ClaudeCode, 自動化]
image: 2026-07-19-Setting-up-your-spare-Mac-for-Claude-Code-to-control-a-step-by-step-guide.jpg
image_alt: "机の上で仕事用のMacBookと接続されて稼働している古いMacBookの様子"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "古い機器に新しい役割を与えることは、持続可能なテクノロジー活用の核心です。このガイドを通じて、あなたのMacBookが賢いAIの助っ人として生まれ変わることを願っています。"
quiz:
  - question: "古いMacBookをClaude Code専用機として活用する主な理由の一つは何ですか？"
    choices: ["MacBookの性能を向上させるため", "AIエージェントのための独立した遠隔環境を構築するため", "バッテリーの寿命を延ばすため"]
    answer: 1
    explanation: "普段の作業環境から切り離された独立した機器を構築することで、AIが画面を制御したりアプリを操作したりする過程を安全かつ効率的に実行できます。"
  - question: "Claude Codeのインストール前に必須となる要件は何ですか？"
    choices: ["最新のM3 MacBook", "Claude Proサブスクリプションまたは課金が有効なAnthropicアカウント", "別途グラフィックカード"]
    answer: 1
    explanation: "Claude Codeを使用するには、有料サブスクリプション（Pro/Max）または課金設定済みのAnthropicアカウントが必要です。"
  - question: "Claude CodeがインストールされたMacを遠隔操作する主な方法は何ですか？"
    choices: ["SSH接続およびClaudeアプリの連携", "MacBookを直接持ち歩く", "Bluetoothキーボードの活用"]
    answer: 0
    explanation: "SSH（Secure Shell、遠隔接続プロトコル）を介して他の機器から制御したり、スマートフォンのClaudeアプリ経由で連携して使用したりできます。"
lang: ja
ref: 2026-07-19-Setting-up-your-spare-Mac-for-Claude-code-to-control-a-step-by-step-guide
---

## 引き出しの中の古いMacBook、AI秘書として生まれ変わらせる

想像してみてください。朝起きてスマートフォンでAIに「今日やるべき仕事リストを確認して、特定のアプリを開いて資料を整理しておいて」と話しかけます。すると、引き出しの奥で眠っていた古いMacBookが自分で画面をオンにし、マウスカーソルを動かしてアプリを実行し、タスクをこなします。まるで目に見えない誰かが自分のMacBookを代わりに操作しているようなこの魔法のような体験は、「Claude Code」というツールを使えば現実になります。

最新のコンピュータだけがすべてではありません。今日のガイドでは、お手持ちの余っているMacBookを「AI専用の遠隔操作端末」に変身させ、AIが自分で画面を見てボタンをクリックし、アプリを操作できるようにする方法を紹介します。

## なぜこれが重要なのか？

AIは単にテキストで回答する段階を超え、今や**「コンピュータ使用（Computer Use）」**能力によって、人間のようにマウスでクリックし、キーボードをタイピングしてソフトウェアを操作できるようになりました [出典: Claude Code Computer Use能力](https://www.mindstudio.ai/blog/claude-code-computer-use-mac-setup-guide)。

しかし、こうしたAIにメインのコンピュータを丸ごと任せるのは、プライバシーや作業の妨げといった懸念があるかもしれません。そこで、使っていない古いMacBookを「独立した作業室」にしてみてはいかがでしょうか？ 安全にAI専用環境を構築し、いつでも手元のスマートフォンやメインPCからその機器を遠隔操作できるようになります [出典: 余ったMacBookをAI遠隔端末として活用](https://github.com/ykdojo/mac-claude-setup) [出典: 常に起動しているAI制御MacBookの作り方](https://github.com/ykdojo/claude-controls-mac)。

## 簡単な解説：AIに「手」を与えるプロセス

Claude Codeは簡単に言えば、AIに「デジタルのマウスとキーボード」を持たせるプロセスです。例えるなら、あなたの古いMacBookに、AIという「脳」が操作できる「手足」を取り付けるようなものです。

1. **指示者（AI）と操作者（MacBook）**: AIが「ここをクリックして」という命令を下すと、インストールされたClaude CodeがMacBookのOSと通信し、実際にカーソルを移動させてボタンを押します [出典: AIエージェントによるMac制御](https://www.mindstudio.ai/blog/claude-code-computer-use-mac-setup-guide)。
2. **遠隔の橋渡し（SSH）**: 私たちが他人のコンピュータを遠隔操作するように、メイン機器と古いMacBookの間に「SSH（Secure Shell、暗号化通信を介して遠隔でコンピュータを操作する方式）」という安全なトンネルを作ります [出典: SSHによる制御](https://github.com/ykdojo/claude-controls-mac)。

こうすることで、古いMacBookは画面を見て、クリックし、入力する「手足」となり、あなたは遠隔地からその手を操作する「司令官」の役割を担うことになります。

## インストールの準備

インストールを始める前に、以下のものを用意してください。

* **余っているMacBook**: 古くても構いません。遠隔操作のための独立した環境として使用します。
* **Claudeのサブスクリプション**: Anthropicの「Claude Pro」サブスクリプション、または課金設定が有効なAnthropicアカウントが必要です [出典: 必須要件](https://inventivehq.com/knowledge-base/claude/how-to-install-claude-code-cli)。

## ステップバイステップのインストール手順

インストール作業のほとんどは、ターミナル（Terminal、コンピュータに直接コマンドを送るテキストベースのウィンドウ）を通じて行います [出典: ターミナルベースのインストール](https://www.serverman.co.uk/ai/claude/how-to-install-claude-code-on-mac/)。

1. **基本ツールのインストール**: まずMacBookに必要なソフトウェアツールをインストールします。通常、「Homebrew（Mac用パッケージ管理ツール）」や「Node.js（プログラム実行環境）」、「Git（コードのバージョン管理ツール）」などをインストールすることになります [出典: 必須ツールインストール案内](https://dev.to/xujfcn/claude-code-installation-guide-for-macos-git-environment-variables-path-and-every-common-fix-4l96)。
2. **Claude Codeのインストール**: 準備されたターミナルウィンドウに、提供されたコマンドを入力してClaude Codeをインストールします [出典: ターミナルコマンドによるインストール](https://www.kimi.com/resources/how-to-install-claude-code)。
3. **連携と設定**: インストールが完了したら自分のアカウントを連携します。その後、遠隔接続のために当該機器のSSH設定を有効化し、メイン機器やスマートフォンからいつでもアクセスできるようにします [出典: 遠隔接続設定](https://github.com/ykdojo/mac-claude-setup)。

インストール中に問題が発生した場合は、ターミナルウィンドウの案内を注意深く読んでください。多くの場合、設定ファイルや権限の問題であるケースがほとんどです [出典: インストールトラブル解決ガイド](https://docs.anthropic.com/en/docs/claude-code/overview)。

## 今後はどうなるのか？

この設定により、あなたは単なるAIチャットボットのユーザーを超え、AIエージェントを直接操る「管理者」になりました。今後、Claude Codeはさらに洗練され、より複雑なmacOSアプリを自由自在に扱えるようになるでしょう。今はクリック操作が中心ですが、遠くない将来、AIがあなたの古いMacBookの中でデザインツールを操作したり、書類作成を代行したり、ウェブサーフィンで情報を整理したりといった秘書の役割を立派に果たしてくれるはずです。

引き出しの中のMacBookが、ただの粗大ゴミではなく、スマートなAIパートナーとして目覚める時間です。

## 参考資料

1. [Setting Up Claude Code Locally with a Powerful Open-Source Model: A Step-by-Step Guide for Mac Users](https://medium.com/@luongnv89/setting-up-claude-code-locally-with-a-powerful-open-source-model-a-step-by-step-guide-for-mac-84cf9ab7302f)
2. [My Claude Code Setup Guide · GitHub](https://gist.github.com/graimon/0bf150c89d6c6844ab95866935bd4b0a)
3. [How to Set Up Claude Code on Mac (2026 Guide)](https://www.masteringai.io/guides/claude-code-setup-mac)
4. [Claude Code Installation Guide for macOS: Git, Environment Variables, Path and Every Common Fix](https://dev.to/xujfcn/claude-code-installation-guide-for-macos-git-environment-variables-path-and-every-common-fix-4l96)
5. [GitHub - ykdojo/mac-claude-setup: How to set up a spare Mac ...](https://github.com/ykdojo/mac-claude-setup)
6. [How to Install Claude Code on Mac (Step-by-Step Guide)](https://www.serverman.co.uk/ai/claude/how-to-install-claude-code-on-mac/)
7. [How to Build an AI Agent That Controls Your Mac: Claude Code Computer Use Setup Guide](https://www.mindstudio.ai/blog/claude-code-computer-use-mac-setup-guide)
8. [GitHub - ykdojo/claude-controls-mac: Step-by-step guide to turning...](https://github.com/ykdojo/claude-controls-mac)
9. [How to Install And Use Claude Code - YouTube](https://www.youtube.com/watch?v=NQNrPaDPMiA)
10. [Terminal guide for new users - Claude Code Docs](https://code.claude.com/docs/en/terminal-guide)
11. [Claude Code overview - Anthropic](https://docs.anthropic.com/en/docs/claude-code/overview)
12. [Claude Skills Builder - Create Custom AI Skills for Claude Code](https://skills-claude.com/)
13. [Guide to use open models with Claude Code on your local device](https://unsloth.ai/docs/basics/claude-code)
14. [Claude Code CLI: Install on Mac/Windows, winget... | Inventive HQ](https://inventivehq.com/knowledge-base/claude/how-to-install-claude-code-cli)
15. [Install Claude Code: The Complete Guide for macOS, Windows...](https://www.morphllm.com/install-claude-code)
16. [Install Claude Code: Full Guide for Windows & Mac](https://www.kimi.com/resources/how-to-install-claude-code)
17. [Claude Code БЕСПЛАТНО через OpenRouter: настройка... - YouTube](https://www.youtube.com/watch?v=EMFMUEuNpWA)