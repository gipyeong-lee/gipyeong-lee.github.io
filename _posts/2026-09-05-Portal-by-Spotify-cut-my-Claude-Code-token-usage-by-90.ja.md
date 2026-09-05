---
layout: post
title: "AIコーディングアシスタントに『お使い』を頼むだけ？ 費用が90%削減された理由"
description: "Spotifyが公開した技術「Portal（ポータル）」を通じて、AIコーディングエージェントのトークンコストを劇的に削減する方法を解説します。"
summary: "Spotifyがオープンソース技術「Portal」とAiKAモードを活用し、AIコーディングエージェントの反復的な単純作業を安価なモデルに委任することで、トークン使用量を90%削減しました。"
tags: [AI, コーディング, Spotify, コスト削減, 効率化]
image: 2026-09-05-Portal-by-Spotify-cut-my-Claude-Code-token-usage-by-90.jpg
image_alt: "コーディングエージェントとコードベースの間で効率的な経路を見つけるデータフローを表現した画像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "複雑な推論を必要としない単純作業まで最高級AIモデルに任せるのは非効率です。この技術は、AI活用の『コストパフォーマンス』を最適化する賢いアプローチです。"
quiz:
  - question: "SpotifyがAIコーディングエージェントの費用を削減するために導入した中核技術の名称は何ですか？"
    choices: ["Claude Code", "Portal", "AiKA"]
    answer: 1
    explanation: "Spotifyは、AIコーディングエージェントとコードベースの間に位置するナレッジグラフレイヤーである「Portal（ポータル）」を公開しました。"
  - question: "PortalのAiKAモードで実行される「code-writer」の主な役割は何ですか？"
    choices: ["コードベース全体の分析", "パターンに基づくコード生成", "ユーザーマニュアルの更新"]
    answer: 1
    explanation: "code-writerモードは、既存のパターンに従って反復的なコードを生成する作業を担当します。"
  - question: "単純な反復業務を安価なモデルに委任することで得られたトークン使用量の削減率はどれくらいですか？"
    choices: ["50%", "70%", "90%"]
    answer: 2
    explanation: "反復的でI/O（入出力）が多い作業をGemini 2.5 Flashのような安価なモデルにルーティングすることで、トークン使用量を90%削減しました。"
lang: ja
ref: 2026-09-05-Portal-by-Spotify-cut-my-Claude-Code-token-usage-by-90
---

想像してみてください。非常に優秀な博士を専属秘書として雇いました。ところが、この博士に毎朝「コピー機のボタンを押す」ことや「書類を分類してファイルに綴じる」といった単純な雑用ばかりさせているとしたら、どうでしょうか？ しかも博士給与を支払いながらです。

最近、開発者の間で大きな話題となっている「AIコーディングエージェント」の状況が、まさにこれに近いのです。非常に高い知能を持つAIにコーディングを任せたところ、高度な論理的思考が必要な問題解決よりも、単純なファイルの読み書きという「お使い」に、より多くのコストを費やしていたのです。ここでいうコストとは、AIが文を理解して処理するたびに支払う「トークン（AIの演算単位）」の費用を指します。この非効率的な状況を打破するため、Spotifyのエンジニアが新たな解決策を打ち出しました。

## なぜこれが重要なのか？

AI技術が急成長する中、多くの開発者がClaude CodeのようなAIコーディングエージェントを通じて業務生産性を大幅に向上させています。しかし、ここには致命的な障害が一つあります。それは「コスト」です。AIが非常に複雑な論理問題を解く際に使用する最高性能のモデル、いわゆる「フロンティアモデル」は、性能が良い分、利用料も非常に高価です。

問題は、この賢いAIが単純なファイルを何度も読み込んだり、すでに何十回も作成したことのある形式と同じテストコードを書いたりする際にも、同じように高額な料金が課される点です。Spotifyの今回の事例は、AIを単に「使う」段階を超えて、**「どの仕事を、どの等級のAIに任せれば最も経済的かつ効率的か」**を示す重要な転換点となるでしょう。これは開発者の生産性を維持しつつ、運用コストを劇的に下げる現実的な道を示唆しています [[参考資料 1](https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90)]。

## 簡単に理解する：「賢い交通整理役」

Spotifyは「Portal」という技術を公開しました [[参考資料 6](https://www.youtube.com/watch?v=TfZsMjB9PMo)]。簡単に例えると、PortalはAIエージェントとコード（コードベース）の間に置かれた**「賢い交通整理役」**のようなものです。従来はAIが無闇にコードのあちこちを調べてすべての内容を読み込んでいたため、トークンを浪費していました [[参考資料 9](https://getpushtoprod.substack.com/p/how-to-reduce-90-of-claude-code-token)]。 

Spotifyはここで「AiKAモード」という2つの特別なスタッフを雇用し、業務を分担させました [[参考資料 11](https://github.com/spotify/portal-ai-plugins)]。 

1. **bulk-reader（一括読み込み担当）**: 複数のファイルを分析する必要がある際、高価なAIを使わず、性能はそこそこですが費用が非常に安い「Gemini 2.5 Flash」モデルに作業を任せます [[参考資料 2](https://yomu.fyi/post/portal-by-spotify-cut-my-claude-code-token-usage-by-90)]。 
2. **code-writer（コード作成担当）**: 既存のコードパターンに従って反復的なコードを書く際も、同様に安価なモデルに任せます [[参考資料 2](https://yomu.fyi/post/portal-by-spotify-cut-my-claude-code-token-usage-by-90)]。 

「shunt（分岐）」という名称のプラグインをインストールすれば、高価な高性能AIモデルは真に頭脳が必要な「創造的な問題解決」に集中し、残りの単純な反復労働は安価なAiKAモデルが分担して処理するようになります [[参考資料 4](https://www.linkedin.com/posts/spotify-for-backstage_portal-by-spotify-cut-my-claude-code-token-activity-7501610054891274241-y4Db), [参考資料 11](https://github.com/spotify/portal-ai-plugins)]。 

## 現在の状況

すでに多くの開発者がAIエージェントを使用しており、毎月発生する膨大なトークン費用に頭を悩ませています [[参考資料 12](https://www.youtube.com/watch?v=UslVzxAkiZ0)]。Spotifyの今回の試みは単なる理論にとどまらず、実際にコーディングエージェントのトークン使用量を**90%も削減する驚くべき結果**を生み出しました [[参考資料 3](https://zeli.app/story/49571465), [参考資料 14](https://news.ycombinator.com/item?id=49571465)]。 

現在、この技術はオープンソースとして公開されており誰でも活用できる状態であり、主にClaude Code環境でファイルI/Oが多い作業を最適化するために積極的に使われています [[参考資料 6](https://www.youtube.com/watch?v=TfZsMjB9PMo), [参考資料 11](https://github.com/spotify/portal-ai-plugins)]。 

## 今後の展望

今後は「どのAIがより賢いか」という議論を超えて、**「どのAIをどのように配置するか」**が真の競争力となるでしょう。SpotifyのPortalのように、複雑なシステム内部をナレッジグラフ（データ間の関係を可視化した形式）の形で管理し、作業の性質に合わせてモデルを自動的に割り振るシステムがさらに多く登場すると見られます。

開発者は「AIにどう指示するか」を悩むだけでなく、「高価なAIを節約し、安いAIを賢く活用する構造をどう設計するか」を考えるべき時期に来ています。賢いAIをより賢く使うために、今こそ効率的な「分業」が必要です。

## MindTickleBytesのAI記者による視点
AI活用の成否は、もはやモデルそのものの性能ではなく、システム全体の効率を管理する「運用の妙」にかかっています。Spotifyの事例は、最高性能のAIを効率的に配置することでコストを下げ、生産性を最大化できることを示す最も模範的な解答例です。

## 参考資料
1. [Portal by Spotify cut my Claude Code token usage by 90%](https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90)
2. [Portal by Spotify cut my Claude Code token usage by 90%](https://yomu.fyi/post/portal-by-spotify-cut-my-claude-code-token-usage-by-90)
3. [Spotify's Portal cut my Claude Code · Hacker News | Zeli](https://zeli.app/story/49571465)
4. [Portal by Spotify cut my Claude Code token usage by 90% ...](https://www.linkedin.com/posts/spotify-for-backstage_portal-by-spotify-cut-my-claude-code-token-activity-7501610054891274241-y4Db)
5. [Spotify’s Backstage Portal cut my Claude Code… | VibeLeaderboard](https://www.vibeleaderboard.ai/intel/7ff05f2d-e1d9-4b86-aa58-8d94a5fccd5f)
6. [Spotify cut Claude Code token usage by 90% with Portal](https://www.youtube.com/watch?v=TfZsMjB9PMo)
9. [How to Reduce 90% of Claude Code Token Usage - by John Kim](https://getpushtoprod.substack.com/p/how-to-reduce-90-of-claude-code-token)
11. [GitHub - spotify/portal-ai-plugins · GitHub](https://github.com/spotify/portal-ai-plugins)
12. [How To Save 90% of Claude Code Token Usage - YouTube](https://www.youtube.com/watch?v=UslVzxAkiZ0)
14. [PortalbySpotifycutmyClaudeCodetokenusage... | HackerNews](https://news.ycombinator.com/item?id=49571465)