---
layout: post
title: "AIが「ブラックボックス」ですって？透明性を武器にした欧州の新しいAIモデル、Soofi(スフィー)"
description: "学習データからコードまで全て公開する透明なAIモデル「Soofi S」の登場とその意義について分かりやすく解説します。"
summary: "ドイツテレコムのSoofiチームが、英語とドイツ語に特化した透明なオープンソースAIモデル「Soofi S」を公開しました。"
tags: [AI, オープンソース, 人工知能, Soofi]
image: 2026-07-15-Soofi-Complete-training-code-for-an-open-source-foundation-model.jpg
image_alt: "透明なガラスの破片が集まり、一つの知的な脳を形成しているデジタルアート"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "企業が秘密を維持するのが当たり前だったAI業界で、「完全公開」という異例の選択をしました。技術の信頼性を高めようとする欧州の戦略的な試みと見られます。"
quiz:
  - question: "Soofi Sモデルが最大の特徴として掲げていることは何ですか？"
    choices: ["圧倒的なパラメータ数", "完璧な透明性とデータの公開", "最高の韓国語性能"]
    answer: 1
    explanation: "Soofi Sは学習データの出所、訓練コード、ハイパーパラメータなど開発過程の全てを公開し、透明性を強調しています。"
  - question: "Soofi S 30B-A3Bモデルの「Mixture-of-Experts(MoE)」構造にはどのような利点がありますか？"
    choices: ["すべてのパラメータを常に使用する", "全体300億個のパラメータのうちトークンあたり30億個のみ活性化するため効率的である", "ドイツ語のみ処理できる"]
    answer: 1
    explanation: "MoE構造は全パラメータのうち一部のみを効率的に選択して使用するため、性能と演算速度を両立できます。"
  - question: "Soofiプロジェクトが集中している言語圏はどこですか？"
    choices: ["英語と韓国語", "英語とドイツ語", "ドイツ語とフランス語"]
    answer: 1
    explanation: "Soofi Sは英語とドイツ語のバイリンガル能力に集中しており、特にドイツ語データを意図的に多く学習させました。"
lang: ja
ref: 2026-07-15-Soofi-Complete-training-code-for-an-open-source-foundation-model
---

想像してみてください。本当に美味しい料理を食べたのに、そのレシピがどうしても分からないとしたらどうでしょう？材料は何なのか、調理時間はどれくらいなのか、どんな特別な技術を使ったのか全く分からない「ブラックボックス」のような料理です。

最近の人工知能(AI)業界がまさにこのような様子です。最先端のAIモデルが毎日溢れ出ていますが、そのAIがどのようなデータを食べて育ったのか、どのように訓練されたのかは、企業の秘密として固く閉ざされています。しかし今、欧州でこうした「秘密主義」に正面から挑戦状を叩きつけたモデルが登場しました。ドイツテレコム傘下の「Soofi(スフィー)」チームが発表したオープンソースAIモデル、**「Soofi S」**です。

## なぜこれが重要なのか？

「ただ性能の良いAIを使えばいいんじゃないの？」と思うかもしれません。しかし、AIを企業の業務や公共サービスに導入する際、「信頼性」は不可欠です。例えば、社内の機密資料をAIに要約させる時、そのAIの内部的な動作を知らなければ不安を感じざるを得ません。

Soofi Sは、モデルの重み(AIの脳内の連結強度)、中間チェックの結果物、さらには**学習に使用されたデータの出所記録(Data provenance)**まで全て公開します [出典: [2607.09424] A Sovereign, Open-Source Foundation Model for German and English](https://arxiv.org/abs/2607.09424), [出典: SoofiS: A SovereignFoundationModelfor German and English](https://www.emergentmind.com/videos/sovereign-open-source-bilingual-llm-cef87c5b)。透明性を武器に、ユーザーがAIを完全に信頼して使えるようにしたのです。

## 分かりやすく理解する

Soofi Sの技術的特徴を理解しやすく例えてみます。

第一に、**「頭の良い学生の勉強法まで全て教えてくれる」**という点です。通常、AIモデルは結果物のみを公開しますが、Soofi Sはモデルの訓練コードやハイパーパラメータ(AI学習環境の設定値)まで全てオープンにしました [出典: [2607.09424] A Sovereign, Open-Source Foundation Model for German and English](https://arxiv.org/abs/2607.09424)。まるで首席で試験に合格した学生が、自分がどの問題集を何時間解いたのか、詳細な計画表を公開するようなものです。

第二に、**「Mixture-of-Experts(MoE、専門家混合構造)」**という賢い頭脳方式を使います。Soofi S 30B-A3Bモデルは全パラメータが300億個に達しますが、実際に質問に答える時はそのうち30億個のみを活性化します [出典: SoofiS 30B activates 3B parameters per token, tops... | UncensoredHub](https://uncensoredhub.ai/news/2026-07-13-soofi-s-30b-activates-3b-parameters-per-token-tops-european-ai-baselines)。例えば、デパートに行った時、売り場全体を回るのではなく、目的地の「靴売り場」だけに向かうのと似ています。これを通じて、より効率的かつ高速に回答を生成します。

第三に、**「英語とドイツ語のためのカスタマイズ教育」**を受けました。Soofiチームは単に多くの言語を学ぶことよりも、英語とドイツ語に集中しました [出典: [2607.09424] A Sovereign, Open-Source Foundation Model for German and English](https://arxiv.org/abs/2607.09424)。特にドイツ語の場合、訓練データの比重を意図的に高く設定し、ドイツ語処理能力を極大化しました [出典: SOOFI (Soofi S) · innFactory AI Consulting - AI Strategy & Consulting](https://innfactory.ai/en/ai-models/soofi/)。

## どこで使われているのか？

Soofi Sは約27兆個のトークン(AIが読む最小言語単位、パズルのピースと類似)を学習して誕生しました [出典: Michael Fromm on X](https://x.com/effi288/status/2075904321707798699)。現在、Hugging Face(AIモデルを共有するオープンプラットフォーム)を通じて、関連モデルや訓練コード、スクリプトを誰でも閲覧できるように提供しています [出典: soofi-project · GitHub](https://github.com/soofi-project)。

ただし、このモデルは全てを公開しているため、ユーザーが直接自身の用途に合わせてデータをテストし、安全性を確認する過程が必要です [出典: Soofi-Project/Soofi-S-Base · Hugging Face](https://huggingface.co/Soofi-Project/Soofi-S-Base)。完成品のAIというよりは、透明な基盤を提供する「基盤モデル(Foundation model)」に近いからです。つまり、料理人が直接材料を選んでレシピを磨ける「基本の道具箱」を手に入れたようなものです。

## 今後はどうなるのか？

欧州の研究陣が開発し、インフラを欧州内に置くSoofiプロジェクトは [出典: Soofi-Project/Soofi-S-Instruct-Preview · Hugging Face](https://huggingface.co/Soofi-Project/Soofi-S-Instruct-Preview)、今後「主権AI(Sovereign AI、データと技術に対する主権を自ら持つAI)」という流れを主導するものと見られます。特定の国やビッグテック企業に依存せず、独自の技術で透明なAIを作るという意志です [出典: European researchers releaseSoofiS 30B-A3B, a hybrid Mamba MoE...](https://digg.com/tech/rtt1xh5r)。

今後、Soofiプロジェクトはモデルの性能を証明する詳細なベンチマークスコアを継続的に公開する予定です [出典: Soofi-Project/Soofi-S-Rhine-Preview · Hugging Face](https://huggingface.co/Soofi-Project/Soofi-S-Rhine-Preview)。私たちが使うAIが本当に賢いのか、そして信頼できるのかを、ソースコードレベルで証明できる時代が一歩近づきました。

## MindTickleBytesのAI記者の視点
AIがあまりに賢くなると、人々は「こいつは一体何を考えているんだ？」という恐怖を感じます。Soofiはその恐怖を「透明性」という技術的解答で解き明かしています。開発過程が全て公開されたAI、果たして我々の社会の信頼をどれだけ得られるのか楽しみです。

## 参考資料
1. [2607.09424] A Sovereign, Open-Source Foundation Model for German and English (https://arxiv.org/abs/2607.09424)
2. Soofi-Project/Soofi-S-Base · Hugging Face (https://huggingface.co/Soofi-Project/Soofi-S-Base)
3. SOOFI (Soofi S) · innFactory AI Consulting - AI Strategy & Consulting (https://innfactory.ai/en/ai-models/soofi/)
4. soofi-project · GitHub (https://github.com/soofi-project)
5. Soofi-Project (Sovereign Open Source Foundation Models) (https://huggingface.co/Soofi-Project)
6. Soofi-Project/Soofi-S-Rhine-Preview · Hugging Face (https://huggingface.co/Soofi-Project/Soofi-S-Rhine-Preview)
7. Soofi-Project/Soofi-S-Instruct-Preview · Hugging Face (https://huggingface.co/Soofi-Project/Soofi-S-Instruct-Preview)
8. Soofi:Completetrainingcodeforanopen-sourcefoundationmodel (https://modernorange.io/item/48918292)
9. SoofiS 30B activates 3B parameters per token, tops... | UncensoredHub (https://uncensoredhub.ai/news/2026-07-13-soofi-s-30b-activates-3b-parameters-per-token-tops-european-ai-baselines)
10. SoofiS: A SovereignFoundationModelfor German and English (https://www.emergentmind.com/videos/sovereign-open-source-bilingual-llm-cef87c5b)
11. European researchers releaseSoofiS 30B-A3B, a hybrid Mamba MoE... (https://digg.com/tech/rtt1xh5r)
12. Michael Fromm on X (https://x.com/effi288/status/2075904321707798699)