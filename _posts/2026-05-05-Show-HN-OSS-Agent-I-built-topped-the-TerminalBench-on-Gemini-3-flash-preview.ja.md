---
layout: post
title: "巨大企業グーグルを抑えた「無名のAI騎士」、ターミナルの王座に就く"
description: "オープンソースAIエージェント「Dirac」がグーグルの公式記録を塗り替え、ターミナル・ベン치マークで1位を獲得した秘訣と、それが私たちの未来に与える影響。"
summary: "オープンソースAIエージェントのDiracが、グーグルのGemini 3を搭載し、コンピュータ専門家の領域である「ターミナル」操作試験で世界記録を更新しました。"
tags: [AIエージェント, Gemini 3, オープンソース, Dirac, TerminalBench]
image: 2026-05-05-Show-HN-OSS-Agent-I-built-topped-the-TerminalBench-on-Gemini-3-flash-preview.jpg
image_alt: "黒いターミナル画面の上で、輝くデジタル脳が複雑なコードをリアルタイムで解決している様子"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "巨大企業の独占技術よりも、開かれた協力の力がより強力であることを証明した出来事です。AIが単なる対話相手を超えて、「行動するヘルパー」へと進化する転換点を示しています。"
quiz:
  - question: "今回世界記録を更新したオープンソースAIエージェントの名前は何ですか？"
    choices: ["Gemini CLI", "Dirac", "Junie CLI"]
    answer: 1
    explanation: "Diracは、Dirac Delta Labsのマックス・トリベディ氏が開発したオープンソースAIエージェントです。"
  - question: "AIのターミナル操作能力を評価する今回の試験の名前は？"
    choices: ["TerminalBench 2.0", "Geminiテスト", "Hacker Newsベンチマーク"]
    answer: 0
    explanation: "TerminalBenchは、AIがコマンドラインインターフェースにおいて、ファイル管理やスクリプト作成をどれだけ正確に実行できるかを評価する基準です。"
  - question: "Diracが今回の試験で記録した正解率は？"
    choices: ["47.8%", "64.3%", "65.2%"]
    answer: 2
    explanation: "Diracは65.2%の成功率を記録し、グーグルの公式記録（47.8%）を大幅に上回りました。"
lang: ja
ref: 2026-05-05-Show-HN-OSS-Agent-I-built-topped-the-TerminalBench-on-Gemini-3-flash-preview
---

想像してみてください。あなたは突然、複雑な機械装置でいっぱいの巨大な工場の制御室に一人で残されました。四方には数千のスイッチがあり、画面には理解できない暗号のようなコードが絶え間なく流れています。ここは工場のすべてを動かす心臓部ですが、非常に熟練した技術者でなければ、手を出すことさえためらわれる恐ろしい空間です。

私たちが毎日使っているコンピュータの中にも、このような「秘密の制御室」が存在します。黒い画面に白い文字だけが並ぶ**ターミナル（Terminal、コマンドを直接入力してコンピュータを制御するウィンドウ）**です。一般のユーザーは綺麗なアイコンをマウスでクリックしてコンピュータを使いますが、本当の専門家はこのターミナルという道具を通じてコンピュータの骨組みを直接動かし、複雑なシステムを設計します。

ところが最近、この専門家だけの聖域であったターミナルで、世界を驚かせる出来事が起きました。グーグル（Google）のような巨大IT企業が作った公式AIを抑えて、一人の個人開発者が作った「無名のオープンソースAI」が、世界で最も賢いターミナル専門家として君臨したのです。まるで路地裏のレストランの料理人が、ミシュラン3つ星シェフたちの料理対決で見事に優勝を果たしたような、大逆転劇です。

## なぜこれが重要なのか？ 「話すAIから行動するAIへ」

これまで私たちが出会ってきたChatGPTやGeminiのようなAIは、主に「話」が得意な存在でした。「詩を書いて」「英語を翻訳して」「長い文章を要約して」といった要望には非常に長けていました。しかし、「自分のコンピュータの中にバラバラに散らばった1,000個のファイルを内容別に整理して、必要なプログラムを勝手にインストールして」といった実質的な作業を任せるには、まだ不安な部分が多くありました。

今回話題になった**Dirac（ディラック）**という名のAIエージェントは、次元が違います。[Dirac OSS Agent Crushes Google's Baseline on TerminalBench](https://www.agent-wars.com/news/2026-04-27-show-hn-oss-agent-i-built-topped-the-terminalbench-on-gemini-3-flash-preview) によると、Diracはコンピュータの最も深い場所であるターミナルに直接アクセスし、複雑な命令を下してファイルを管理し、自ら問題を解決する能力を立証しました。

簡単に言えば、AIが単に情報を教えてくれる「物知りな秘書」を超えて、自分のコンピュータを代わりに管理し、複雑な技術業務をサクサクと遂行する**「有能な代理人（Agent）」**へと進化したということです。特に、数兆円の資本が投入された大企業の有料サービスではなく、誰もが設計図を覗き見ることができ、無料で使える**オープンソース（Open Source、ソフトウェアの設計図であるソースコードを大衆に公開すること）**モデルが堂々と1位を占めたという点が、世界中の開発者を熱狂させています。

## 簡単に理解する：AIの「運転免許試験」、TerminalBench

AIがどれほど賢いかを測定するために、専門家たちはさまざまな「試験」を受けさせます。今回Diracが王座に就いた試験は、**TerminalBench 2.0（ターミナル・ベンチ 2.0）**です。[Open-Source AIAgentTopsTerminalBench2.0 Leaderboard](https://aihaberleri.org/en/news/open-source-ai-agent-scores-652percent-on-terminalbench-20-in-2026-beating-gemini-and-junie-cli)

この試験を例えるなら、**「AIのための高難易度走行試験」**のようなものです。ただし、車の代わりに「コンピュータのターミナル」という非常に厄介で複雑な装置を運転しなければなりません。試験項目には、専門家でも汗をかくような難題が含まれています：[OSS Agent Tops TerminalBench with Gemini-3 - PromptZone](https://www.promptzone.com/maria_gonzalez_419fd1b8/oss-agent-tops-terminalbench-with-gemini-3-3lh2)

1.  **シェルスクリプト（Shell Scripting）**：コンピュータに下す多段階の命令を順番に作成すること（例えるなら、数万人が食べる複雑な料理のレシピを、一分の狂いもなく書くようなものです）。
2.  **ファイル管理**：数万個のファイルの中から微細な違いを見つけ出して必要なものを選び出し、移動させ、修正する緻密な作業。
3.  **システム設定**：コンピュータの内部環境を目的に合わせて完全に作り変える高難易度の業務。

開発者の「umair24171」氏は、「ほとんどのAI試験は単に知識を問う見かけ倒しである場合が多いですが、TerminalBenchはAIが実際に『仕事』ができるかどうかを測ることができる真の実力テストです」と評価しています。[Gemini-3-Flash: My aiagentbenchmarkterminalbenchWin & 3 Fixes](https://dev.to/umair24171/gemini-3-flash-my-ai-agent-benchmark-terminalbench-win-3-fixes-44eb)

## 現状：ダビデがゴリアテに勝った驚くべき点数差

今回の対決の結果は、IT業界全体に大きな衝撃を与えました。まるで学年1位を独占していた裕福な家の秀才を、自ら道を切り拓いて勉強した学生が圧倒的な点数差で破ったようなものだからです。実際の成績表を見てみましょう。

*   **Dirac**：**65.2%**（誰でも使えるオープンソース基盤）[r/GoogleGeminiAI on Reddit: Open Source Agent I built topped the TerminalBench 2.0 on Gemini-3-flash-preview](https://www.reddit.com/r/GoogleGeminiAI/comments/1sx2r4s/open_source_agent_i_built_topped_the/ )
*   **Junie CLI**：64.3%（既存の1位だった高価な有料商用モデル）
*   **グーグル公式記録**：**47.8%**（グーグルが直接自社モデルでテストした結果）

驚くべきことに、Diracはグーグルが立てた公式記録よりも、なんと17.4ポイントも高いスコアを記録しました。学校の試験で言えば、グーグルが48点のときにDiracは65点を超えたことになります。[r/GoogleGeminiAI on Reddit: Open Source Agent I built topped the TerminalBench 2.0 on Gemini-3-flash-preview](https://www.reddit.com/r/GoogleGeminiAI/comments/1sx2r4s/open_source_agent_i_built_topped_the/)

この勝利の影の立役者は、実はグーグルが作った最新AIの脳、**Gemini-3-flash-preview（ジェミナイ3 フラッシュ プレビュー）**モデルです。[Dirac OSS Agent Crushes Google's Baseline on TerminalBench](https://www.agent-wars.com/news/2026-04-27-show-hn-oss-agent-i-built-topped-the-terminalbench-on-gemini-3-flash-preview) Gemini-3 Flashは、複雑なコーディングやシステム作業を実行する際、従来のモデルよりもはるかに速く、賢く動作するように設計されたグーグルの野心作です。[Gemini 3 Flash — Google DeepMind](https://deepmind.google/models/gemini/flash/)

しかし重要なのは、グーグル自身はこの素晴らしいエンジンを十分に活用できず40点台に留まった一方で、開発者のマックス・トリベディ（Max Trivedi）氏はこのエンジンを精巧にチューニングし、最適化することで、世界最高の性能を引き出したという事実です。それも、いかなる隠し事もなく、すべての設計図を公開したままです。[ShowHN: OSS Agent I built topped the TerminalBench on...](https://news.ycombinator.com/item?id=47920787)

## 今後どうなるのか？ 私たちの元にやってくる「万能修理屋」AI

Diracの成功は、私たちがまもなく迎えることになる二つの未来を鮮明に示しています。

第一に、**AIが私たちの家の「コンピュータ万能修理屋」になります。**想像してみてください。コンピュータの速度が突然遅くなったり、原因不明のエラーウィンドウが表示されたりしたとき、高い修理代を払って専門家を呼ぶ代わりに、AIエージェントに「ターミナルでこの問題の原因を見つけて直して」と頼む場面を。AIが黒い画面の中で数万行のコードをスキャンし、1分で修理を終える時代がすぐそこまで来ています。

第二に、**「共に作る力」が巨大企業の独占に勝ちます。**グーグルが作ったエンジンを借りつつも、そのエンジンを活用するより良い方法（エージェント構造）を世界中の人々が共に考え、改善していけば、企業が一人で秘密裏に作るよりもはるかに優れた成果物が出る可能性があることを、今回確認できたからです。

もちろん、まだ道のりは残っています。65.2%という点数は、依然として10回に3回程度はミスをする可能性があることを意味します。ターミナルでのミスは、下手をすれば大切な家族写真や重要な仕事のファイルを消してしまう危険も伴います。そのため、開発者たちはAIが絶対にミスをしないよう、より完璧な「安全装置」を作るために、今日も研究を重ねています。

## AIの視点：MindTickleBytesのAI記者の視点

「Diracの勝利は、単なる数字の対決ではありません。これはAIという強力な道具が、特定の巨大企業の専有物ではなく、私たち全員の知恵と好奇心が集まったときに最も強力な光を放つということを証明した出来事です。今、私たちはAIに『何を質問しようか』と悩んでいた時代を過ぎ、AIに『自分のコンピュータのどんな難しい仕事を任せようか』と悩まなければならない、真の『エージェント時代』の入り口に立っています。」

## 参考資料
1. [ShowHN: OSS Agent I built topped the TerminalBench on...](https://news.ycombinator.com/item?id=47920787)
2. [Gemini-3-Flash: My aiagentbenchmarkterminalbenchWin & 3 Fixes](https://dev.to/umair24171/gemini-3-flash-my-ai-agent-benchmark-terminalbench-win-3-fixes-44eb)
3. [Open-Source AIAgentTopsTerminalBench2.0 Leaderboard](https://aihaberleri.org/en/news/open-source-ai-agent-scores-652percent-on-terminalbench-20-in-2026-beating-gemini-and-junie-cli)
4. [Gemini 3 Flash — Google DeepMind](https://deepmind.google/models/gemini/flash/)
5. [r/GoogleGeminiAI on Reddit: Open Source Agent I built topped the TerminalBench 2.0 on Gemini-3-flash-preview](https://www.reddit.com/r/GoogleGeminiAI/comments/1sx2r4s/open_source_agent_i_built_topped_the/)
6. [OSS Agent Tops TerminalBench with Gemini-3 - PromptZone](https://www.promptzone.com/maria_gonzalez_419fd1b8/oss-agent-tops-terminalbench-with-gemini-3-3lh2)
7. [Gemini 3 — Google DeepMind](https://deepmind.google/models/gemini/)
8. [Dirac OSS Agent Crushes Google's Baseline on TerminalBench](https://www.agent-wars.com/news/2026-04-27-show-hn-oss-agent-i-built-topped-the-terminalbench-on-gemini-3-flash-preview)

## FACT-CHECK SUMMARY
- Claims checked: 15
- Claims verified: 15
- Verdict: PASS