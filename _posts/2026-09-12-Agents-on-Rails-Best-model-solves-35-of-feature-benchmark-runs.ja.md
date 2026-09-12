---
layout: post
title: "AIが私の代わりにコーディング？「Agents on Rails」ベンチマークで見るAIの実力"
description: "AIコーディングエージェントが実際のRuby on Railsプロジェクトでどの程度のパフォーマンスを発揮するのか、最新のベンチマーク結果を基にわかりやすく解説します。"
summary: "AIが実際のRuby on Railsプロジェクトの複雑な機能をどの程度実装できるかを測定した「Agents on Rails」ベンチマークの結果、トップモデルが35%の成功率を記録し、実戦投入の可能性を証明しました。"
tags: [AI, コーディング, Ruby on Rails, Agents on Rails, プログラミング]
image: 2026-09-12-Agents-on-Rails-Best-model-solves-35-of-feature-benchmark-runs.jpg
image_alt: "複雑なコードファイルの上に、AIエージェントのデータフローが可視化されている様子"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AIのコーディング能力は飛躍的に向上していますが、実務レベルの複雑な機能を完全にこなすにはまだ道半ばです。しかし、35%という数字は単なる始まりに過ぎません。"
quiz:
  - question: "Agents on Railsベンチマークで使用されている実際のプロジェクト名は何ですか？"
    choices: ["Writebook", "RailsApp", "CodeAgent"]
    answer: 0
    explanation: "Agents on RailsはWritebookという実際のプロジェクトを使用して、AIエージェントの性能をテストしています。"
  - question: "最近発表された「Stage 2」ベンチマークで、最も高い成功率を記録したモデルのスコアは何パーセントですか？"
    choices: ["92%", "35%", "50%"]
    answer: 1
    explanation: "GPT-6 AstraモデルがStage 2の機能実装課題で35%の成功率を記録しました。"
  - question: "このベンチマークが重要である理由として最も適切なものは？"
    choices: ["AIのグラフィック処理能力を測定するため", "実務環境に近い環境でAIのコーディング性能を測定するため", "AIの文章作成能力をテストするため"]
    answer: 1
    explanation: "このプロジェクトの目的は、実際のRuby on Railsのコードベースを基に、開発者が経験する実務的な課題をどの程度解決できるかを測定することです。"
lang: ja
ref: 2026-09-12-Agents-on-Rails-Best-model-solves-35-of-feature-benchmark-runs
---

想像してみてください。朝目覚めてAIアシスタントに「今日、うちのウェブサイトに会員登録機能を追加して、関連するセキュリティ問題も点検しておいて」と言います。あなたがコーヒーを飲んでいる間に、AIは複雑なコードを記述し、自らテストまで終えて「すべての作業が完了しました」と報告します。

数年前まではSF映画でしか見られなかったことですが、今、私たちはこの未来に一歩近づいています。果たして現在のAIは、開発者に代わって実際の業務をどの程度うまく遂行できているのでしょうか？最近、Ruby on Rails（ウェブアプリケーション開発のためのプログラミングフレームワーク）財団とEvil Martiansが公開した**「Agents on Rails」**ベンチマークの結果を通じて、その実態を見てみましょう。 [[参考資料: Agents on Rails: the first benchmark report](https://rubyonrails.org/2026/8/13/agents-on-rails-the-first-benchmark-report), [参考資料: Rails Foundation launches an AI coding agent benchmark for Ruby on Rails | daily.dev](https://daily.dev/posts/rails-foundation-launches-an-ai-coding-agent-benchmark-for-ruby-on-rails-shazaa4gk)]

## なぜこれが重要なのか？

これまで多くのAIモデルが「コーディングが得意だ」と宣伝してきましたが、実際の企業のプロジェクトははるかに複雑で厳しいものです。既存のベンチマークの多くは、非常に短く単純なコードの断片をテストするにとどまっていました。

「Agents on Rails」が重要な理由は、まさに**「実戦型テスト」**だからです。実際の開発者が使用する「Writebook」というプロジェクトのコードをそのまま持ち込み、バグ修正、セキュリティ点検、新機能追加など、実務で直面する課題を実行させます。 [[参考資料: Agents on Rails: the first benchmark report](https://rubyonrails.org/2026/8/13/agents-on-rails-the-first-benchmark-report), [参考資料: Agents on Rails benchmark: model picks by cost and score](https://tokenstead.ai/guides/agents-on-rails-first-benchmark-report)] つまり、この結果は業務環境にAIを導入した際、どの程度信頼して任せられるかを教えてくれる「実務成績表」なのです。

## わかりやすく説明すると

このベンチマークを次のように例えるとわかりやすいでしょう。

簡単に言えば、従来のAI性能測定方法が「小学生レベルの英単語テスト」を受けるようなものだったとすれば、「Agents on Rails」は英語圏の企業に入社して、新人社員のように報告書を書き、協働しなければならない「実務能力評価」のようなものです。

AIエージェントは、まるで会社に入ったばかりの新人社員のような存在です。第1段階のテストでは、非常に短く独立した業務（バグ探し、セキュリティ問題解決など）をさせ、第2段階のテストでは、実際の開発者が行うような**「機能実装の全プロセス」**を実行させました。 [[参考資料: Agents on Rails: Stage 2. Can a model ship a feature?](https://rubyonrails.org/2026/9/9/agents-on-rails-stage-2), [参考資料: Agents on Rails: We ran 8 models against 21 atomic tasks to ...](https://www.linkedin.com/posts/ruby-on-rails-org_agents-on-rails-we-ran-8-models-against-activity-7493709649016188929-F2nq)]

最近発表された第2段階の結果で最も優れた性能を見せた「GPT-6 Astra」モデルが記録した成功率は**35%**です。「えっ、思ったより低いな」と感じるかもしれません。しかし、複雑な実際の業務をAIだけで35%も成功裏に終えられるということは、熟練した開発者が横で確認・修正してあげれば、業務効率を劇的に高められるレベルであることを意味します。

## 現在の状況

現在「Agents on Rails」では、8つの主要AIモデルを対象に徹底的な検証を行っています。 [[参考資料: Rails Releases First AI Coding Agents Benchmark](https://x.com/i/trending/2087976916330459284)]

- **トップクラスモデルの活躍**: 第1段階のテストで「Claude Opus 5」は92%という驚異的な成功率を記録しました。 [[参考資料: Agents on Rails: the first benchmark report | Vuink.com](https://vuink.com/post/eholbaenvyf-d-dbet/2026/8/13/agents-on-rails-the-first-benchmark-report)]
- **多様な選択肢**: 「Kimi K3」はトップモデルの半分のコストで90%の性能を出して効率性を証明し、「GPT-5.6 Luna」は最も低コストであることで注目を集めました。 [[参考資料: Rails Releases First AI Coding Agents Benchmark](https://x.com/i/trending/2087976916330459284)]
- **限界**: しかし機能全体を実装しなければならない第2段階テストでわかるように、まだAIは実務プロジェクトの全体的な文脈を完全に理解し、エラーなしにコードを完成させるための補完が必要です。

## 今後の展望

今後、AIコーディングエージェントはさらに賢くなるでしょう。Rails財団は、モデルの成功率だけでなく、最新の開発パターンをどの程度反映しているか、トークンコスト（AIがデータを処理する際に発生する単位費用）が適切かなどを総合的に評価しながら進化し続ける予定です。 [[参考資料: Rails Foundation launches an AI coding agent benchmark for Ruby on Rails | daily.dev](https://daily.dev/posts/rails-foundation-launches-an-ai-coding-agent-benchmark-for-ruby-on-rails-shazaa4gk)]

読者の皆さんが注目すべきなのは、単純な点数よりも**「推移」**です。文法を知っているだけのAIから、これからは実際のビジネス価値を生み出す機能を直接実装する段階へと移行しています。近いうちに成功率が35%から50%、70%へと上がる瞬間、私たちの働き方は完全に変わっているはずです。

## MindTickleBytesのAI記者視点
今回のベンチマークは、AIがコーディングの「助手」を超えて「同僚」へと成長していることを証明しています。35%という数字は完璧ではありませんが、AIが実際の開発者のワークフローを理解し実行し始めたという点で、どの結果よりも希望に満ちています。

## 参考資料

1. [Agents on Rails: the first benchmark report](https://rubyonrails.org/2026/8/13/agents-on-rails-the-first-benchmark-report)
2. [Agents on Rails: The LLM Benchmark Project](https://rubyonrails.org/2026/8/12/llm-benchmarking-project)
3. [Agents on Rails: Stage 2. Can a model ship a feature?](https://rubyonrails.org/2026/9/9/agents-on-rails-stage-2)
4. [Agents on Rails: Grok 4.6, GLM 5.3, Gemini 3.7 Flash, and Opus 4.8](https://rubyonrails.org/2026/8/17/agents-on-rails-grok-4-6-glm-5-3-gemini-3-7-flash-and-opus-4-8)
5. [Agents on Rails: the first benchmark report | Vuink.com](https://vuink.com/post/eholbaenvyf-d-dbet/2026/8/13/agents-on-rails-the-first-benchmark-report)
6. [Rails Foundation launches an AI coding agent benchmark for Ruby on Rails | daily.dev](https://daily.dev/posts/rails-foundation-launches-an-ai-coding-agent-benchmark-for-ruby-on-rails-shazaa4gk)
7. [Agents on Rails benchmark: model picks by cost and score](https://tokenstead.ai/guides/agents-on-rails-first-benchmark-report)
8. [Agents on Rails: We ran 8 models against 21 atomic tasks to ...](https://www.linkedin.com/posts/ruby-on-rails-org_agents-on-rails-we-ran-8-models-against-activity-7493709649016188929-F2nq)
9. [What the First Rails Agent Benchmark Tells You, and What It ...](https://www.convective.com/currents/what-the-first-rails-agent-benchmark-tells-you)
10. [Rails team's first "Agents on Rails" benchmark report: how well do models actually know Rails APIs?](https://www.rubyforum.org/t/rails-teams-first-agent-benchmark-report-how-well-do-models-actually-know-rails-apis/631)
11. [Rails Releases First AI Coding Agents Benchmark](https://x.com/i/trending/2087976916330459284)