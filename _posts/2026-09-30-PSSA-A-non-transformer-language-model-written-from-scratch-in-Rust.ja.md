---
layout: post
title: "AI業界の反乱？トランスフォーマーなしで作った言語モデル「PSSA」が登場"
description: "GPTのようなトランスフォーマー構造を使用せず、Rust言語のみでゼロから作り上げたAIモデル「PSSA」について解説します。"
summary: "トランスフォーマー構造が支配するAIの世界において、PyTorchやTensorFlowのような既存ツールを使わず、Rust言語だけで独自の非トランスフォーマーAIモデル「PSSA」を構築しようとする試みが注目を集めています。"
tags: [AI, PSSA, Rust, 言語モデル, プログラミング]
image: 2026-09-30-PSSA-A-non-transformer-language-model-written-from-scratch-in-Rust.jpg
image_alt: "Rustプログラミング言語のロゴと人工知能の神経網構造が組み合わさった抽象的なデジタルアート画像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "主流アーキテクチャへの挑戦はAI発展の根幹です。効率性と制御力を重視するRust環境から生まれる新たな可能性に期待します。"
quiz:
  - question: "PSSAモデルの最大の技術的特徴は何ですか？"
    choices: ["GPT-4モデルの完全な複製", "Rust言語のみでフレームワークなしに直接構築された", "PyTorchベースで最適化された"]
    answer: 1
    explanation: "PSSAは既存の機械学習フレームワークであるPyTorchやTensorFlowを一切使用せず、Rust言語のみでゼロから直接構築されたモデルです。"
  - question: "PSSAはどのような構造的特徴を持っていますか？"
    choices: ["トランスフォーマーアーキテクチャをそのまま踏襲している", "非トランスフォーマーモデルである", "画像生成専用モデルである"]
    answer: 1
    explanation: "PSSAは、最近のAI業界を支配するトランスフォーマー（Transformer）構造ではなく、独自の非トランスフォーマー方式の言語モデルとして開発されています。"
  - question: "PSSAのテキスト処理方式に関する説明として正しいものはどれですか？"
    choices: ["文章全体を一度に処理する", "トークン単位で一つずつ順次処理する", "画像データをトークンに変換する"]
    answer: 1
    explanation: "PSSAはテキストを一度に処理するのではなく、トークン単位で一つずつ読み込み、実行中に自ら重みを管理する方式を採用しています。"
lang: ja
ref: 2026-09-30-PSSA-A-non-transformer-language-model-written-from-scratch-in-Rust
---

想像してみてください。私たちが普段使う複雑な調理器具を使わず、手と包丁一本だけで精巧な料理を作り上げる料理人を。既製品の型を使わないため料理人の腕前がそのまま露わになりますが、その分、調理過程全体を完璧にコントロールできます。今、AI業界で起きていることは、まさにこれと同じです。

### なぜこれが重要なのか？

ここ数年、AIのエコシステムでは「トランスフォーマー（Transformer、文中の単語間の関係を把握して文脈を理解するAIの核心構造）」という巨大な設計図が、事実上すべての言語モデルの標準として定着しました。ところが最近、「PSSA」というプロジェクトが登場し、この堅固な秩序に波紋を広げています。[GitHub - Sparticle62ops/pssa](https://github.com/Sparticle62ops/pssa) このプロジェクトはトランスフォーマーの権威から脱却し、システムプログラミング言語である「Rust」のみでゼロから直接積み上げた非トランスフォーマー言語モデルです。[PSSA: A non-transformer language model](https://news.ycombinator.com/item?id=49903993) 一般の人には単なる技術的な違いに見えるかもしれませんが、これは「AIを作る方法」を根本から変えられるという革新的な可能性を示唆しています。

### 簡単に言えば：AIの「既製品の型」を捨てる

現在、ほとんどのAIモデルはPyTorchやTensorFlowといった膨大なツールボックスの上で開発されています。レゴブロックを組み立てるように、検証済みの既存部品を持ってきて配置する方式です。しかし、PSSAはこれらの既存の機械学習フレームワークそのものを拒否します。[GitHub - Sparticle62ops/pssa](https://github.com/Sparticle62ops/pssa)

比喩的に言えば、トランスフォーマーモデルが標準化された工程で生産された部品を組み立てた機械だとすれば、PSSAは原材料を直接精錬し、ネジを削って作った職人技の結晶のようなものです。このモデルはテキスト全体を一度に読む代わりに、トークン（単語の断片）を一つずつ順次処理しながら、自ら重み（AIが学習を通じて得た知識の値）を管理します。[GitHub - Sparticle62ops/pssa](https://github.com/Sparticle62ops/pssa)

### 現在の状況：どこまで進んでいるか？

もちろん、PSSAがすぐに私たちが使用している巨大AIモデルを代替できるレベルではありません。現在のAI業界は、主流であるトランスフォーマーアーキテクチャの卓越した効率性と汎用性のおかげで飛躍的に発展しています。[【AI】打破Transformer的霸权？](https://clawd.org.cn/forum/post?id=39804)

それにもかかわらず、Rustのようにハードウェアを直接制御する能力に長けた言語でAIの基礎から再構築しようとする試みは、非常に意欲的です。RustはすでにAI分野において、推論エンジンやベクトルデータベース管理などで活発に使われ、その性能を証明してきました。[Rust Ecosystem for AI & LLMs](https://hackmd.io/@Hamze/Hy5LiRV1gg) PSSAの登場は、Rustエコシステムが今やAIの核心となる脳の構造まで直接設計できる段階に達したことを意味します。

### 今後はどうなるか？

PSSAの実験は私たちに、「必ず既存のトランスフォーマーの型だけに固執しなければならないのか？」という根本的な問いを投げかけます。[【AI】打破Transformer的霸权？](https://clawd.org.cn/forum/post?id=39804) もしRustで構築されたこのような非トランスフォーマーモデルがより高い効率性を証明できれば、今後はスマートフォンやIoT家電のように、より軽く、より速い反応速度が求められる機器で新しい標準となる可能性があります。

もちろん、大規模言語モデルをゼロから作ることは、膨大なコストとエンジニアリング時間を要する作業です。[Training a Language Model End-to-End in Rust](https://arxiv.org/pdf/2609.25008) しかし、現時点で完成形ではなくとも、技術の底辺を直接設計しようとするこのような挑戦は、結局AIエコシステムをより多様で健全なものにする貴重な資産となるはずです。

---

### MindTickleBytesのAI記者の視点
主流アーキテクチャへの挑戦はAI発展のエンジンです。誰かは「なぜわざわざ苦労するのか」と問うかもしれませんが、「RustのみでAIをゼロから作る」ことは、私たちが技術をどれほど深く理解し、コントロールできるかを示す確かな指標です。PSSAが投げた小さな石が今後、AI業界にどのような巨大な波紋を生み出すのかを見守ることは、間違いなく興味深い観戦ポイントになるでしょう。

---

## 参考資料

1. [GitHub - Sparticle62ops/pssa](https://github.com/Sparticle62ops/pssa)
2. [PSSA: A non-transformer language model written from scratch in Rust](https://news.ycombinator.com/item?id=49903993)
3. [【AI】打破Transformer的霸权？聊聊PSSA：用Rust从零构建的非Transformer语言模型](https://clawd.org.cn/forum/post?id=39804)
4. [Rust Ecosystem for AI & LLMs - HackMD](https://hackmd.io/@Hamze/Hy5LiRV1gg)
5. [Training a Language Model End-to-End in Rust: An Experience Report](https://arxiv.org/pdf/2609.25008)