---
layout: post
title: "私の代わりにクリックしてタイピングするAI？グーグル「Gemini 2.5 Computer Use」の登場"
description: "人間のように画面を見てマウスを動かし、タスクを実行するグーグルの新しいAIモデル「Gemini 2.5 Computer Use」を紹介します。"
summary: "グーグルが画面を理解し、自ら13種類の動作を実行してウェブブラウザを操作する「エージェント級」AIモデルを公開しました。"
tags: [Gemini, AIエージェント, Google, 人工知能, Computer Use]
image: 2026-04-22-Introducing-the-Gemini-25-Computer-Use-model.jpg
image_alt: "コンピュータ画面上でAIがマウスカーソルを操作し、様々なウェブページを行き来する様子をイメージした画像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "単に話が上手なAIを超えて、今や私たちの「手」となってくれるAIエージェントの時代が本格的に幕を開けました。"
quiz:
  - question: "Gemini 2.5 Computer Useモデルがタスクを実行する際、最初に受け取るデータは何ですか？"
    choices: ["ユーザーの音声", "画面のスクリーンショットやコンテキスト情報", "エクセルファイルのデータ"]
    answer: 1
    explanation: "このモデルは「エージェントループ」を通じて画面のスクリーンショットを撮り、現状を把握してから次の動作を決定します。"
  - question: "このモデルが学習を通じて実行できる動作は合計で何種類ですか？"
    choices: ["5種類", "13種類", "100種類"]
    answer: 1
    explanation: "Gemini 2.5 Computer Useは、ブラウザを探索・操作するために13種類の異なる動作を実行するように訓練されています。"
  - question: "このモデルが優れた性能を示したベンチマーク（性能指標）のうち、Android環境をテストするものはどれですか？"
    choices: ["Online-Mind2Web", "WebVoyager", "AndroidWorld"]
    answer: 2
    explanation: "Gemini 2.5 Computer Useは、AndroidWorldを含む複数のインターフェース制御ベンチマークで強力な性能を示しました。"
lang: ja
ref: 2026-04-22-Introducing-the-Gemini-25-Computer-Use-model
---

月曜日の朝、出勤してすぐに直面する山のようなメールや領収書を想像してみてください。一つひとつ開き、日付と金額を確認した後、会社の精算システムにいちいち入力していく退屈なプロセスです。ログインし、ファイルをアップロードし、空欄を埋めるという単純な繰り返し作業は、私たちの貴重な時間の大部分を奪います。しかし、そんな時にAIに「この領収書を全部整理して提出して」と一言頼めるとしたらどうでしょうか？AIがまるで人間のように、私の目の代わりに画面を見つめ、私の手の代わりにマウスを動かして、すべての作業を完璧に終わらせる世界。もはやSF映画の中の話ではありません。グーグルが最近公開した**「Gemini 2.5 Computer Use」**モデルが、私たちの目の前に描き出している近い未来の姿です。[Gemini 2.5 Computer Useモデルの紹介](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-computer-use-model/)

## なぜこれが重要なのでしょうか？

これまで私たちが熱狂したChatGPTや既存のGeminiは、主に「話」が得意なAIでした。疑問に思ったことを聞けばスラスラと答えてくれ、複雑な論文を要約して私たちを驚かせました。しかし、よく考えてみると、私たちがコンピュータで行う業務の80〜90％は会話ではなく、具体的な「行動」です。特定のボタンをクリックし、画面を下にスクロールし、検索窓に文字を入力する一連の操作です。

Gemini 2.5 Computer Useの登場は、AIが単に知識を伝える「話す秘書」から脱却し、ユーザーの業務を実際に遂行する**「エージェント（Agent、代理人）」**へと進化したことを象徴しています。[Introducing Gemini 2.5 Computer Use model: A Paradigm Shift in AI's Digital Dexterity](https://markets.financialcontent.com/wedbush/article/tokenring-2025-10-7-gemini-25-computer-use-model-a-paradigm-shift-in-ais-digital-dexterity) このモデルは、ウェブブラウザやスマートフォンアプリの画面構成を人間のように直感的に理解し、マウスとキーボードを直接制御できます。[Introducing Gemini 2.5 Computer Use: AI for web and... | LinkedIn](https://www.linkedin.com/posts/googleaidevs_introducing-gemini-25-computer-use-available-activity-7381415403840864256-ycSe) 簡単に言えば、AIにコンピュータを扱う「手」ができたわけです。これは、企業の反復的な事務自動化はもちろん、ソフトウェアが正常に動作するかを検査する方法自体を根本的に変える可能性を秘めています。[Gemini 2.5 Computer Useモデル | Gemini API | Google AI for Developers](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-computer-use-preview-10-2025)

## 簡単に理解する：AIに「目」と「手」ができました

Gemini 2.5 Computer Useが働く仕組みは、**「エージェントループ（Agent Loop）」**という概念で説明できます。例えるなら、私たちが初めての道で運転する際に「道路状況を確認し（目）→ナビの経路と比較して判断し（頭）→ハンドルを切ったりブレーキを踏んだりする（手）」プロセスを繰り返すのと同じです。[Gemini 2.5 Computer Useモデルの紹介](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-computer-use-model/)

1. **状況把握（目）：** AIはまず、現在のコンピュータ画面のスクリーンショットを撮り、リアルタイムで分析します。どこにボタンがあり、どこに入力欄があるのかを「見る」段階です。[Gemini 2.5 Computer Useモデルの紹介](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-computer-use-model/)
2. **推論（頭）：** ユーザーが「飛行機のチケットを予約して」とリクエストした場合、AIは現在の画面とリクエスト内容を照らし合わせます。そして「今は『ログイン』ボタンを先に押さなければならない」と判断を下します。[Google's Gemini 2.5 Computer Use model can navigate the web like a ...](https://siliconangle.com/2025/10/07/googles-gemini-2-5-computer-use-model-can-navigate-web-like-human/)
3. **実行（手）：** 判断が決まれば、実際にマウスカーソルをその位置に移動させてクリックしたり、キーボードでIDとパスワードをタイピングしたりします。[Gemini 2.5 Computer Useモデルの紹介](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-computer-use-model/)

この魔法のような能力は、グーグルの最も強力なAIモデルの一つである「Gemini 2.5 Pro」の優れた視覚分析能力と推論能力をベースに作られました。[Introducing Gemini 2.5 Computer Use: AI for web and... | LinkedIn](https://www.linkedin.com/posts/googleaidevs_introducing-gemini-25-computer-use-available-activity-7381415403840864256-ycSe) 特にマウスカーソルをピクセル単位で精密に制御し、ウェブブラウザ上で行われる**13種類の核心的な動作**を集中的に学習することで、習熟度を高めました。[Google News - Google releases Gemini 2.5, a new AI model with web...](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lDM3NUYkR4RU1DYjNPMmlnelhpZ0FQAQ?hl=en-US&gl=US&ceid=US:en)

再び例えるなら、従来のAIが「コンピュータの使用法」という分厚い百科事典を丸暗記した理論家だったとすれば、Gemini 2.5 Computer Useは実際にマウスを握って実習に飛び込んだ新入社員のようなものです。まだ「プレビュー」段階なので速度が少し遅かったり、ミスがあったりするかもしれませんが、自ら画面を見て道を探していくという点自体が大きな飛躍です。[Google releases a preview of its Gemini 2.5 Computer Use AI model ...](https://gigazine.net/gsc_news/en/20251008-google-gemini-2-5-computer-use/)

## 現在の状況：どこまで進んでいるのか？

グーグルは2025年10月初旬、競合他社のOpenAIが同様の技術に言及した翌日にこのモデルを電撃公開し、AIエージェント市場の主導権を握るための強力な勝負に出ました。[Google launches Gemini 2.5 Computer Use to rival OpenAI agents](https://www.techbuzz.ai/articles/google-launches-gemini-2-5-computer-use-to-rival-openai-agents) 現在、このモデルは開発者が直接テストし、自身のサービスに組み込んでみることができる「公開プレビュー」として提供されています。[Introducing Gemini 2.5 Computer Use model: A Paradigm Shift in AI's Digital Dexterity](https://markets.financialcontent.com/wedbush/article/tokenring-2025-10-7-gemini-25-computer-use-model-a-paradigm-shift-in-ais-digital-dexterity)

グーグルは単に可能性を示しただけでなく、客観的な性能指標（ベンチマーク）を通じてその実力を証明しました。
- **Online-Mind2Web & WebVoyager:** 複雑なウェブサイト内でAIが道に迷わず目標を達成できるかを測定する試験で、優れた成績を収めました。[Google DeepMind Launches Gemini 2.5 Computer Use Model to Power UI-Controlling AI Agents - InfoQ](https://www.infoq.com/news/2025/10/gemini-computer-use/)
- **AndroidWorld:** WindowsやMacのようなPC環境だけでなく、Androidスマートフォンの環境をいかに巧みに操作できるかを測定する試験でも、強力な性能を示しました。[Google DeepMind Launches Gemini 2.5 Computer Use Model to Power UI-Controlling AI Agents - InfoQ](https://www.infoq.com/news/2025/10/gemini-computer-use/)

これらのテスト結果は、Gemini 2.5 Computer Useが人間が画面を見て感じる直感をAIも共有でき、それに基づいて実際の問題を解決していけることを裏付けています。[Gemini 2.5 Computer Use Model: How It Automates Browsers](https://skywork.ai/blog/gemini-2-5-computer-use-model/)

## 今後はどうなるのでしょうか？

専門家たちは、今回のモデルの登場が、AIが私たちの生活に浸透する方法における分岐点になると見ています。[2025 Complete Guide: Gemini 2.5 Computer Use Model - Revolutionary ...](https://dev.to/czmilo/2025-complete-guide-gemini-25-computer-use-model-revolutionary-breakthrough-in-ai-agent-133) 近いうちに、私たちは以下のような驚くべき変化を日常で目にするようになるかもしれません。

1. **想像以上のパーソナルアシスタント：** 「今週末、友達と江南駅の近くで会うんだけど、評価4点以上の店を予約して、グループチャットに場所と時間を共有して」と一言言うだけで済みます。AIがレストラン予約アプリを起動して予約を完了し、メッセンジャーを開いて友達にメッセージまで送るのです。
2. **ソフトウェア品質の革命：** 新しいアプリを作った開発者は、もう徹夜でバグを探す必要はありません。AIエージェントが何千回、何万回とアプリのあちこちをクリックしてエラーを見つけ出し、レポートを作成してくれるからです。[Gemini 2.5 Computer Useモデル | Gemini API | Google AI for Developers](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-computer-use-preview-10-2025)
3. **すべての人のための技術：** スマートフォンやコンピュータの操作が苦手な高齢者や、画面を見ることが難しい視覚障害者の方々にとっても大きな力になります。複雑なクリックのプロセスなしに、音声コマンドだけであらゆるデジタルサービスを自由に利用できるようになるからです。

もちろん、解決すべき課題も残っています。AIが誤って見当違いな商品を購入してしまったり、ユーザーの機密性の高い個人情報を誤って扱ったりした場合にどう対応するかという、セキュリティと倫理的なガイドラインが必要です。しかし、グーグルが踏み出したこの第一歩は、AIが単なる道具を超えて、私たちと共にデジタル世界を生きる心強い「パートナー」になる時代がすぐそこまで来ていることを確信させます。[Is Gemini 2.5 Computer Use Model the Future of AI-Driven Interface Control?](https://apidog.com/blog/gemini-2-5-computer-use-model/)

## AIの視点
**MindTickleBytesのAI記者の視点：** 「言葉だけが達者だったAIが、ついに実際にコンピュータのマウスを握りました。これは、AI技術が『言語の壁』を超えて『行動の領域』に進入したことを意味する非常に象徴的な出来事です。近いうちに私たちは『AIにこの仕事をさせよう』と意識することさえないほど、空気のように自然にAIエージェントと協業することになるでしょう。便利さが大きくなる分、AIの自律性をどこまで許容し、信頼するのかについての社会的な合意も真剣に始めるべき時です。」

## 参考資料
1. [Introducing the Gemini 2.5 Computer Use model](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-computer-use-model/)
2. [Google News - Google releases Gemini 2.5, a new AI model with web...](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lDM3NUYkR4RU1DYjNPMmlnelhpZ0FQAQ?hl=en-US&gl=US&ceid=US:en)
3. [Gemini 2.5 Computer Use AGENT: THE BEST AGENTIC... - YouTube](https://www.youtube.com/watch?v=Xllcw7YUjJA)
4. [Introducing Gemini 2.5 Computer Use: AI for web and... | LinkedIn](https://www.linkedin.com/posts/googleaidevs_introducing-gemini-25-computer-use-available-activity-7381415403840864256-ycSe)
5. [Gemini 2.5 Computer Use Model: How It Automates Browsers](https://skywork.ai/blog/gemini-2-5-computer-use-model/)
6. [Gemini Computer Use: Google's FREE Browser... - Analytics Vidhya](https://www.analyticsvidhya.com/blog/2025/10/gemini-2-5-computer-use/)
7. [Gemini 2.5 Computer Use model | Gemini API | Google AI for Developers](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-computer-use-preview-10-2025)
8. [Is Gemini 2.5 Computer Use Model the Future of AI-Driven Interface Control?](https://apidog.com/blog/gemini-2-5-computer-use-model/)
9. [Google DeepMind Launches Gemini 2.5 Computer Use Model to Power UI-Controlling AI Agents - InfoQ](https://www.infoq.com/news/2025/10/gemini-computer-use/)
10. [2025 Complete Guide: Gemini 2.5 Computer Use Model - Revolutionary ...](https://dev.to/czmilo/2025-complete-guide-gemini-25-computer-use-model-revolutionary-breakthrough-in-ai-agent-133)
11. [Google launches Gemini 2.5 Computer Use to rival OpenAI agents](https://www.techbuzz.ai/articles/google-launches-gemini-2-5-computer-use-to-rival-openai-agents)
12. [Google releases a preview of its Gemini 2.5 Computer Use AI model ...](https://gigazine.net/gsc_news/en/20251008-google-gemini-2-5-computer-use/)
13. [Introducing Gemini 2.5 Computer Use model: A Paradigm Shift in AI's Digital Dexterity](https://markets.financialcontent.com/wedbush/article/tokenring-2025-10-7-gemini-25-computer-use-model-a-paradigm-shift-in-ais-digital-dexterity)
14. [Google's Gemini 2.5 Computer Use model can navigate the web like a ...](https://siliconangle.com/2025/10/07/googles-gemini-2-5-computer-use-model-can-navigate-web-like-human/)

## FACT-CHECK SUMMARY
- Claims checked: 15
- Claims verified: 15
- Verdict: PASS