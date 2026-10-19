---
layout: post
title: "AIが自ら教える？Googleの「Harness2」が切り拓くAIエージェントの新たな時代"
description: "AIエージェントが人の手を借りずに自らプロンプトやツールを改善する技術、GoogleのHarness2について分かりやすく解説します。"
summary: "Googleリサーチが発表したHarness2は、AIエージェントが人から正解を教えられなくても、自ら実行環境を改善しながら学習する再帰的なエージェント活用フレームワークです。"
tags: [AI, Googleリサーチ, エージェント, Harness2, 技術トレンド]
image: 2026-10-19-Harness2-by-Google-Research-Recursive-Agent-Harnessing.jpg
image_alt: "AIが自らシステムを最適化しながら進化するプロセスを視覚的に表現したグラフィック"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Harness2は、AIが単にモデルの知能に依存する段階を超え、周辺環境までも自ら最適化する「自律的進化」の重要な転換点となるでしょう。"
quiz:
  - question: "Harness2の核心的な特徴の一つは何ですか？"
    choices: ["人が一つひとつ正解を入力して学習する", "正解（ground-truth）の確認なしに自ら実行環境を改善する", "テキストのみを処理するモデルである"]
    answer: 1
    explanation: "Harness2は、人が正解を教えなくても（ground-truth verifierなしで）自らタスクを遂行し、実行環境を改善するフレームワークです。"
  - question: "AIエージェントの「ハーネス（harness）」とは何ですか？"
    choices: ["AIの脳容量", "AIモデルを取り囲むプロンプト、ツール、記憶などの実行システム", "AIの学習速度"]
    answer: 1
    explanation: "ハーネスは、モデルがエージェントとして動作できるよう支援するプロンプト、ツール、記憶、スキル、オーケストレーションなどのシステム周辺装置です。"
  - question: "Harness2のソースコードはどのライセンスで提供されていますか？"
    choices: ["有料ライセンス", "Apache 2.0ライセンス", "非公開"]
    answer: 1
    explanation: "GoogleリサーチはHarness2のコードをApache 2.0ライセンスで公開しました。"
lang: ja
ref: 2026-10-19-Harness2-by-Google-Research-Recursive-Agent-Harnessing
---

想像してみてください。朝起きて人工知能（AI）アシスタントに「今日の会議資料を整理してメールで送っておいて」と言います。これまでのAIならあらかじめ決められた手順でしか動けませんでしたが、これからはAIが自ら考え始めます。「この人の会議の進め方は前回と違うな。もっと効果的な整理ツールを探してみよう。」そして自らプロンプト（AIへの命令文）を修正し、必要なツールを最適化して最高の成果物を作り上げます。

まるでAIが自ら賢くなる方法を見つけ出していくプロセス、これこそがGoogleリサーチが発表した新しいフレームワーク**Harness2**が目指す未来です [[Source 7](https://www.datastudios.org/post/google-research-harness2-recursive-ai-agent-improvement-open-source)]。

## なぜこれが重要なのか？

これまで私たちが使ってきたAIエージェント（ユーザーの指示を遂行するAI）は、モデル自体の知能と同じくらい「周辺環境」に大きく依存してきました。モデルがどんなに賢くても、そのモデルをどう扱い、どのツールを接続するかによって性能が大きく異なっていたからです [[Source 2](https://arxiv.org/abs/2610.14224)]。これを技術的には「ハーネス（harness、AIエージェントが動作できるようにするプロンプト、ツール、記憶などの実行システム）」と呼びます [[Source 1](https://github.com/google-research/harness2)]。

問題は、このハーネスを人が直接最適化するのには限界があるという点です。特に現実世界の数多くの「予測不能な」タスクに直面したとき、人があらゆる状況を予測して事前に設定を変えることはほぼ不可能です [[Source 2](https://arxiv.org/abs/2610.14224)]。Harness2はまさにこの点でイノベーションを提示しています。AIが自らハーネスを改善し、その学習プロセスに基づいて次の問題をよりうまく解決するように設計されているからです [[Source 3](https://www.google.com/url?q=https://arxiv.org/pdf/2610.14224)]。

## 分かりやすく例えると：「天才料理人」のキッチン

「ハーネス」という概念が少し難しく感じられますか？このように例えてみましょう。

AIモデルを**「天才的な料理人」**だとします。料理人がどんなに実力があっても、キッチンが散らかっていては実力を発揮できませんよね。包丁がどこにあるか、火加減はどうするか、調理器具をどう配置するかを決めるのが、まさに「ハーネス」の役割です。以前は人がキッチンを整理してあげる必要がありましたが、**Harness2は料理人自身が料理をしながら、より効率的に働けるように包丁の位置を変えたり、コンロの火力を最適化したりするシステム**だと理解すれば良いでしょう。

これを専門用語では**「再帰的エージェント活用（Recursive Agent Harnessing）」**と呼びます [[Source 1](https://github.com/google-research/harness2)]。「再帰的」という言葉は、AIが現在のタスクを遂行しながら得た経験で自分の実行方式を改善し、その改善された方式を次のタスクに適用してさらに良い結果を出すことを意味します [[Source 6](https://arxiviq.substack.com/p/harness2-recursive-agent-harnessing)]。

特に驚くべき点は、このプロセスにおいて**人が一つひとつ正解を教える必要がない**ということです [[Source 6](https://arxiviq.substack.com/p/harness2-recursive-agent-harnessing)]。従来の学習方式が正解を見て勉強することだとすれば、Harness2は自ら実験してどの方式がより効率的かを見つけ出す「自己主導型学習」の方式に近いと言えます [[Source 13](https://huggingface.co/papers/2610.14224)]。

## 現状

現在、Harness2はGoogleリサーチによってオープンソースとして公開されており、誰でも確認できる状態です [[Source 7](https://www.datastudios.org/post/google-research-harness2-recursive-ai-agent-improvement-open-source)]。このフレームワークは固定された言語モデル（frozen language model）をベースにしながらも、モデル自体を改造するのではなく、その周辺の「スキャフォールディング（scaffolding、実行のための構造物）」であるプロンプト、ガードレール、スキル、ツールを最適化することに集中します [[Source 6](https://arxiviq.substack.com/p/harness2-recursive-agent-harnessing)]。

技術的な観点から見ると、Harness2はベンチマークテストにおいて正解確認の手順なしでも自ら性能を向上させる姿を見せており、エージェントの可能性を広げています [[Source 13](https://huggingface.co/papers/2610.14224)]。しかし、まだ研究の初期段階であるため、複雑な現実世界の変数を完全に制御できるようになるまでには、もう少し時間が必要でしょう。

## 今後はどうなるか？

Harness2の登場は、AIエージェントがもはや人の詳細なガイドラインなしでも自ら進化できる土台を築いたという点で大きな意味を持ちます。今後AIは、私たちが日々繰り返す複雑な業務をより深く理解し、時間が経つにつれてユーザー個人に完璧にフィットした「パーソナライズされたキッチン」を自ら構築していくはずです。

開発者にとっては、このツールが新しいエージェントシステムを設計する強力な「ハーネス・ファウンドリ（harness foundry、エージェント環境製造所）」となるでしょう。再利用可能なプロセッサとバンドルを組み合わせて、自分だけのエージェントを進化させることができるからです [[Source 10](https://trendshift.io/repositories/307358)]。AIが自ら最適化する世界、その効率性は私たちが想像する以上かもしれません。

## AIの視点（MindTickleBytesのAI記者の視点）

Harness2は、AIがモデルの「知能」を高める競争を超えて、いかに「持てる能力」を無駄なく発揮するかを考える「最適化」の時代へとシフトしたことを意味します。これからのAIの競争力は、誰がより賢いかではなく、誰がより早く自らを最適化して問題を解決するかにかかっていると言っても過言ではないでしょう。

## 参考資料

1. [google-research/harness2 - GitHub](https://github.com/google-research/harness2)
2. [[2610.14224] Harness^2: Recursive Agent Harnessing for an ...](https://arxiv.org/abs/2610.14224)
3. [Harness^2: Recursive Agent Harnessing for an Open World](https://www.google.com/url?q=https://arxiv.org/pdf/2610.14224)
4. [Harness^2: Recursive Agent Harnessing for an Open World](https://arxiviq.substack.com/p/harness2-recursive-agent-harnessing)
5. [Google Research Harness²: Recursive AI Agent Improvement ...](https://www.datastudios.org/post/google-research-harness2-recursive-ai-agent-improvement-open-source)
6. [google-research/harness2— GitHub trending stats... | Trendshift](https://trendshift.io/repositories/307358)
7. [Paper page -Harness^2:RecursiveAgentHarnessingfor an Open...](https://huggingface.co/papers/2610.14224)