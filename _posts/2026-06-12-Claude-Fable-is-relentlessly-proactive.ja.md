---
layout: post
title: "質問するだけだったAIは忘れよう：自ら働き、自ら検証する「Claude Fable 5」"
description: "Anthropicが新しくリリースした「Claude Fable 5」は単なるチャットボットではありません。人が数日かけて行うべき複雑なプロジェクトを自ら企画し、検証する新しいAIの登場を分かりやすく解説します。"
summary: "人が数日、数週間かけて行うべき複雑なプロジェクトを自ら企画し、視覚能力を活用して成果物を批判的に検討し、粘り強く主導的に解決する新しい次元のAIモデル「Claude Fable 5」が世に公開されました。"
tags: [AI, Claude, Anthropic, 人工知能, テクノロジートレンド]
image: 2026-06-12-Claude-Fable-is-relentlessly-proactive.jpg
image_alt: "巨大な図書館で数多くの本や設計図を浮かべて自ら研究と校正を繰り返しながら働いているロボットの姿を温かい色合いで描いたイラスト"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "単に知識を吐き出す自動販売機から、自ら問題を見つけて解決する能動的な同僚へと、AIの進化が一段階飛躍しました。"
quiz:
  - question: "Claude Fable 5を最もよく活用する方法は何ですか？"
    choices: ["日常的な簡単な天気の質問をする", "簡単な挨拶を翻訳する", "数日かかる複雑で未解決の最も難しい問題を任せる"]
    answer: 2
    explanation: "Claude Fable 5は、複雑で長期的なプロジェクトのために設計されています。単純な作業だけでテストすると、このモデルの真の能力を過小評価することになります。"
  - question: "Claude Fable 5の特徴の中で、従来のAIと最も差別化される点は何ですか？"
    choices: ["テキストのみで回答できる", "自分の成果物を視覚的に検討し、目標に合っているか批判的に自ら検証する", "価格が常に完全に無料である"]
    answer: 1
    explanation: "このモデルは、視覚（Vision）機能を使用して自分の成果物を目標と照らし合わせて批判的に検討し、主導的に自らを検証する能力を備えています。"
  - question: "一緒に発表された「Claude Mythos 5」は誰のために提供されますか？"
    choices: ["すべての一般無料ユーザー", "Project Glasswingを通じたサイバーセキュリティ専門家", "小学生の教育用"]
    answer: 1
    explanation: "Mythos 5はFable 5と同じモデルですが、一部の保護措置が解除された状態であり、Project Glasswingを通じてサイバーセキュリティ専門家などに限定的に提供されます。"
lang: ja
ref: 2026-06-12-Claude-Fable-is-relentlessly-proactive
---

想像してみてください。朝出勤して、会社に新しく入った有能な新入社員に「我が社の新しいサービスの企画からプロトタイプ開発までの全過程を自分で進めてみて」と指示しました。通常のAIなら、何のことか分からず質問ばかり繰り返すか、ネットに出回っているありきたりな企画書を1秒でポンと作って仕事が終わったと言うでしょう。しかし、この新しい新入社員は違います。自ら企画案を練り、コードを作成した後、画面がきちんと表示されるか自分の目で直接確認します。もし成果物にエラーがあれば、四の五の言わずに徹夜してでも自ら修正し評価して、完璧に近い成果物を翌朝あなたの机の上に静かに置いておきます。

これがまさに2026年6月9日、人工知能企業Anthropicが世に新しく公開した人工知能、**「Claude Fable 5」**を最もよく説明する場面です [Claude Fable 5 Is Here: Anthropic's First Public Mythos-Class ...](https://pasqualepillitteri.it/en/news/4523/claude-fable-5-fruitcake-eap-mythos-public-release) [Claude Fable 5 Is Here: What the New Top Model Means for Your ...](https://theaicareerlab.com/blog/claude-fable-5-for-professionals)。著名なソフトウェア開発者であるSimon Willisonは、このAIを2日間集中的に使用した後、たった一文で強力な感想を残しました。

「このAIを説明する最も良い方法は、**『執拗なまでに主導的（relentlessly proactive）』**だということです。このモデルは数多くの技術的な秘訣（tricks）を知っています。」 [Claude Fable is relentlessly proactive](https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/) [Claude Fable 5 AI model described as relentlessly proactive ...](https://news.linxi.com.au/news/willison-describes-claude-fable-5-as-relentlessly-proactive-following-initial-testing)

一体、Claude Fable 5は従来のチャットボットと何が違うからこそ、専門家たちがこのような驚くべき評価を下すのでしょうか？一般の目線から、この新しい技術の意味と波及力を順を追って見ていきましょう。

---

## なぜ重要なのか？ (Why It Matters)

私たちがこれまで使ってきた馴染みのあるチャットボット型AIは、例えるなら一種の「高級飲料自動販売機」のようでした。コインを入れて（質問をして）ボタンを押すと、それに合った飲み物（答え）がポトンと落ちてきます。しかし、飲料自販機に「私のために1週間分の健康な献立を考え、スーパーで買い物をして、毎朝私の体質に合わせて料理までして」と頼むことはできません。自販機は単発の要求に応答するだけで、長期的な目標に向かって自ら動くことはできないからです。

Claude Fable 5は、このような単純な自販機やチャットボットの限界を軽々と超えました。このモデルは、人が直接取り組めば数時間、数日、あるいは数週間かけて苦心して解決しなければならない大規模で複雑なプロジェクトを、最初から最後まで一人で成し遂げる「自律的な知識労働者（Autonomous knowledge worker）」の役割を果たすように設計されています [Prompting Claude Fable 5 - Claude API Docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5) [ClaudeFable5 - API Pricing & Benchmarks | OpenRouter](https://openrouter.ai/anthropic/claude-fable-5)。

Anthropicはこのモデルを指して、**「Mythos（神話）クラス」**の能力を備えていると呼んでいます [Anthropic Claude Fable 5 on AWS: Mythos-class capabilities with built-in safeguards now available | Amazon Web Services](https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/) [ClaudeFable5 - API Pricing & Benchmarks | OpenRouter](https://openrouter.ai/anthropic/claude-fable-5)。「Mythos」とは神話や伝説を意味する言葉ですが、このクラスのモデルは、あなたの最も野心的で長時間を要するプロジェクト（Long-running projects）のために作られました。過去のAIモデルでは思いもよらなかった、複雑で曖昧かつ膨大な問題を解決することに特化しているという意味です [Claude Fable \ Anthropic](https://www.anthropic.com/claude/fable) [Prompting Claude Fable 5 - Claude API Docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)。

これが普通の会社員や大衆に意味するところは計り知れません。これまでは、ユーザーがAIに対して一々「この段落を要約して」「次はこれをコードで組んで」と細かく分けて指示しなければなりませんでした。人間がAIの管理者として絶えず介入しなければならなかったのです。しかし今では、「このような巨大な目標を達成して」という大きな方向性だけを投げかければよくなりました。するとAIが自ら詳細な計画を立て、障害物に出会えば迂回し、最後まで責任を持って実行する、真の意味での「委任」が可能な時代が大きく開かれているのです。簡単に言えば、私の仕事を手伝う単なる「ツール」から、私の仕事を自ら代行してくれる心強い「同僚」へと進化したのです。

---

## 分かりやすい解説 (The Explainer)

では、Claude Fable 5はどのようにしてこのような数日かかるプロジェクトを一人で成し遂げることができるのでしょうか？このモデルを特別なものにする3つの核心的な特徴を見てみましょう。

**1. 自ら正解を確かめる几帳面な優等生：「主導的な自己検証」**

従来のAIに難しい数学の問題やコーディングの問題を投げかけると、誤答であれ正答であれ、とりあえず素早く文章を作成して終わらせていました。誤答を提出しても堂々と立っている学生のようでした。しかし、Claude Fable 5は答案用紙を提出する前に徹底的に「検算」をする学生です。

Anthropicによると、このモデルは働き方が非常に徹底しており（thorough）、主導的（proactive）で、自分が作った成果物を自らテストします [Claude Fable \ Anthropic](https://www.anthropic.com/claude/fable)。技術的な用語ではこれを**「主導的な自己検証（Proactive self-verification）」**と呼びます。このAIは作業途中で新しく学んだ内容があれば自分のスキルを自らアップデートし、自分の成果物を評価するための独自の評価ツール群（Evaluations and harnesses）まで自ら開発します [Anthropic Claude Fable 5 on AWS: Mythos-class capabilities with built-in safeguards now available | Amazon Web Services](https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/)。他人が検査する前に自らを過酷に評価し、完成度を極限まで高めるのです。

**2. 目を持つコーディングの魔法使い：「視覚を活用した批判的検討」**

最も驚くべき発展の一つは、このAIが単に文字（コード）だけをタイピングする盲目の魔法使いではなく、自分が作った成果物を両目で直接「見る」ということです。

例えば、Fable 5にコンピュータープログラムのウェブ画面を作ってほしいと指示したと想像してみてください。Fable 5はコードを作成し、高い再現度（High fidelity）でデザインを実装します。驚くべきことはその次です。自分が書いたコードの結果画面を視覚（Vision、画像を見て理解する機能）機能で直接確認した後、当初設定した目標と比較して批判的に評価（Critique）します [Anthropic Claude Fable 5 on AWS: Mythos-class capabilities with built-in safeguards now available | Amazon Web Services](https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/)。まるでシェフがレシピ通りに料理を終えた後、客のテーブルに出す前に直接目で盛り付けを確認し、自ら味見をして評価するのと同じです。コーディング、マルチモーダル（テキストと画像を同時に理解する能力）推論などで並外れた強みを持っています [AffordableClaudeFable5 API for Coding and Mythos-Class... | Kie.ai](https://kie.ai/claude-fable-5)。

**3. 無条件に「はい」とは言わない大胆な同僚：「プロンプトに対する論評」**

以前のAIは、ユーザーがどんなに愚かな質問をしても、無条件に機械的でもっともらしい答えをでっち上げようとしました。しかし、Claude Fable 5を使ってみた人たちは、このモデルがユーザーの質問（プロンプト）自体に対して自ら意見を述べているかのような奇妙な傾向をすぐに見出します [Claude Fable 5 is Mythos for the masses - Techzine Global](https://www.techzine.eu/blogs/applications/141978/claude-fable-5-is-mythos-for-the-masses/)。

依然として巨大言語モデル（LLM、大規模テキストデータを学習したAI）の枠組みの中にありますが、Fable 5は入力された指示事項に対して自己反省（Self-reflect）をする姿を見せます [Claude Fable 5 is Mythos for the masses - Techzine Global](https://www.techzine.eu/blogs/applications/141978/claude-fable-5-is-mythos-for-the-masses/)。「この質問はこのようなアプローチをした方が良いかもしれません」とユーザーに逆にフィードバックを与える、賢くて大胆な実務者に近い存在です。間違った指示を出すと無条件に服従する代わりに、より良い道を提示してくれる頼もしいパートナーができたというわけです。

---

## 現在の状況 (Where We Stand)

Claude Fable 5は遠い未来の話ではなく、すでに私たちの現実に入り込んでいます。Anthropicはこのモデルを最も進歩した汎用モデルとして大衆に正式に公開しました [Introducing Claude Fable 5 and Claude Mythos 5 - Claude API Docs](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5)。

興味深い事実は、今回の発表には**隠された双子の兄弟**がいるという点です。大衆に公開され、私たちが日常やビジネスで安全に使えるように各種の安全装置（Safeguards、有害または危険な出力を防ぐ保護機能）が内蔵されたバージョンが、まさに私たちが今話している「Claude Fable 5」です。一方、このモデルと双子のようにそっくりですが、AIの強力な力を制限する保護措置を意図的に解除した、危険かつ強力なバージョンが存在します。この秘密めいたモデルの名前は**「Claude Mythos 5」**で、「Project Glasswing」という極秘プログラムを通じて、身元と目的が確実なサイバーセキュリティ専門家など少数にのみ、密かに限定的に提供されます [Claude Fable 5 Is Here: Anthropic's First Public Mythos-Class ...](https://pasqualepillitteri.it/en/news/4523/claude-fable-5-fruitcake-eap-mythos-public-release)。

それでは、一般人や企業はFable 5をどこで使用できるのでしょうか？現在このモデルは、独自のClaude APIだけでなく、Amazonの強力なクラウド網であるAWS Bedrock、GoogleのVertex AI、Microsoft Foundryなど、世界中の主要なビッグテックプラットフォームにすでに構築されており、すぐに使用することができます [ClaudeFable5 Just Shipped: 80.3% on... | WaveSpeed Blog](https://wavespeed.ai/blog/posts/claude-fable-5-launch-benchmarks-pricing/)。新しい技術が出るやいなや、世界中のデジタル神経網にすでに張り巡らされているのです。

利用料金に関しては、Anthropicの重要な戦略が隠されています。一般消費者向けサービスであるClaudeの有料プラン（Pro、Max、Teamプラン）の購読者であれば、2026年6月22日までは追加費用なしでこの最高級モデルを自由にテストしてみることができます [Claude Fable 5 Is Here: What the New Top Model Means for Your ...](https://theaicareerlab.com/blog/claude-fable-5-for-professionals) [ClaudeFable5 Just Shipped: 80.3% on... | WaveSpeed Blog](https://wavespeed.ai/blog/posts/claude-fable-5-launch-benchmarks-pricing/)。

しかし、開発者がプログラムの裏側（API）で大量に使用する際のコストは、かなり高価に設定されています。AIが単語を処理する単位である「トークン（Token）」を基準に、100万入力トークンあたり10ドル、100万出力トークンあたり50ドルという価格が付けられました [ClaudeFable5 (with fallback) - Intelligence, Performance & Price...](https://artificialanalysis.ai/models/claude-fable-5) [ClaudeFable5 - API Pricing & Benchmarks | OpenRouter](https://openrouter.ai/anthropic/claude-fable-5)。通常、本1冊が約10万トークンだと仮定すると、本10冊をAIに読ませるのに10ドル（約1500円）かかることになります。他の安価な日常用AIモデルの費用が1〜2ドル程度であることを考慮すると、まさに超プレミアムな専門家の「人件費」を支払うようなものです。

**ここで最も注意すべき点があります。**
この非常に高価で賢い「頭脳」を無駄に使ってはいけません。Anthropicの公式ドキュメントは、開発者やユーザーに向けて強力な警告でありアドバイスを残しています。

*「Claude Fable 5を単純なワークロードだけでテストすると、このモデルの能力範囲をむしろ過小評価することになるでしょう。」* [Prompting Claude Fable 5 - Claude API Docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)

つまり、「今日のソウルの天気を教えて」や「この短い英語のメールを翻訳して」のような日常的な質問にこのAIを使うのは、世界最高のロケット工学者を連れてきて小学生の九九を解かせ、「大したことないね」とがっかりするのと同じです。Fable 5で最高の結果を得ているチームは、このAIを彼らが抱える**「最も解決の難しい未解決問題（Hardest unsolved problems）」**に投入しています [Prompting Claude Fable 5 - Claude API Docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)。

実際に5つの現実的で複雑な実務業務を与えて性能をテストしてみた結果、Fable 5は膨大な文書を扱ったり、コーディングをアーキテクチャレベルで設計したりするなど、一般的な専門職従事者（Working professional）が数日かけて苦心して行うべき深みのある業務において真の価値を証明しました [I Tested Claude Fable 5 with 5 Real-World Prompts: Here's ...](https://aitoolsclub.com/i-tested-claude-fable-5-with-5-real-world-prompts-heres-what-it-can-actually-do/) [Claude Fable 5 Is Here: What the New Top Model Means for Your ...](https://theaicareerlab.com/blog/claude-fable-5-for-professionals)。

---

## 今後どうなるのか？ (What's Next)

「あなたはClaude Fable 5を完全に間違って使用しています。」YouTubeでこのモデルの使い方をレビューしたある専門家が残した苦言です [You are usingClaudeFable5 wrong - YouTube](https://www.youtube.com/watch?v=vjdHAWvVCP4)。過去の慣性に従って、単に尋ねて答えるという一問一答の用途だけで使っていては、この進歩した技術の恩恵を十分に享受できないからです。

Claude Fable 5の登場は、私たちが働く方式を根本から揺るがしています。これまでAIが粗削りな草案を作成し、人間がそれを長時間かけて修正する「人間主導型の補助ツール」だったとすれば、今や状況は逆転しました。逆にAIが数日間自ら企画案を練り直し、エラーを修正して完璧に近い最終案を提出すれば、人間の監督者はそれを検討して最終承認だけを行うという方向へ、業務の重心が劇的に移動しています。要求事項が多く複雑な、長期的なエージェント（Agentic、自ら判断して行動する自律的な主体）作業の時代が正式に幕を開けたのです [Introducing Claude Fable 5 and Claude Mythos 5 - Claude API Docs](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5)。

私たちは今、粘り強く仕事に食らいつき、自らの成果物を反省して修正する優れたAIという新しい職場の同僚を迎えました。現在、私たちに残された最も重要な課題はただ一つです。この賢いデジタルの同僚に任せる「最も巨大で野心的な問題」とは何かを真剣に悩むことです。質問の大きさがすなわち成果物の大きさになる世界がやって来たのです。

---

**MindTickleBytesのAI記者の視点：**
過去のAIが、私たちが指示した仕事だけを受動的にこなすのに忙しい見習い社員だったとすれば、Fable 5は自ら会社の問題を見つけ、目で結果を確認し、粘り強く探求する責任感のあるシニア実務者へと成長しました。人工知能が人間の作業時間を単に「短縮」してくれることを超えて、数日間の激しい悩みを必要とする「思考の深さ」にまで拡張してくれる、真の自動化の時代が広がっています。このような目覚ましい進歩を完全に自分の武器にするために、私たち人間はツールの使い方を覚える代わりに、より鋭く大胆な質問を投げかけることができる「企画者」としての力量を養うべき時です。

---

## 参考資料

1. [Claude Fable 5 Is Here: Anthropic's First Public Mythos-Class ...](https://pasqualepillitteri.it/en/news/4523/claude-fable-5-fruitcake-eap-mythos-public-release)
2. [Claude Fable is relentlessly proactive](https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/)
3. [Claude Fable 5 AI model described as relentlessly proactive ...](https://news.linxi.com.au/news/willison-describes-claude-fable-5-as-relentlessly-proactive-following-initial-testing)
4. [Prompting Claude Fable 5 - Claude API Docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)
5. [Claude Fable \ Anthropic](https://www.anthropic.com/claude/fable)
6. [Anthropic Claude Fable 5 on AWS: Mythos-class capabilities with built-in safeguards now available | Amazon Web Services](https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/)
7. [Claude Fable 5 is Mythos for the masses - Techzine Global](https://www.techzine.eu/blogs/applications/141978/claude-fable-5-is-mythos-for-the-masses/)
8. [Introducing Claude Fable 5 and Claude Mythos 5 - Claude API Docs](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5)
9. [Claude Fable 5 Is Here: What the New Top Model Means for Your ...](https://theaicareerlab.com/blog/claude-fable-5-for-professionals)
10. [ClaudeFable5 Just Shipped: 80.3% on... | WaveSpeed Blog](https://wavespeed.ai/blog/posts/claude-fable-5-launch-benchmarks-pricing/)
11. [ClaudeFable5 (with fallback) - Intelligence, Performance & Price...](https://artificialanalysis.ai/models/claude-fable-5)
12. [ClaudeFable5 - API Pricing & Benchmarks | OpenRouter](https://openrouter.ai/anthropic/claude-fable-5)
13. [AffordableClaudeFable5 API for Coding and Mythos-Class... | Kie.ai](https://kie.ai/claude-fable-5)
14. [I Tested Claude Fable 5 with 5 Real-World Prompts: Here's ...](https://aitoolsclub.com/i-tested-claude-fable-5-with-5-real-world-prompts-heres-what-it-can-actually-do/)
15. [You are usingClaudeFable5 wrong - YouTube](https://www.youtube.com/watch?v=vjdHAWvVCP4)