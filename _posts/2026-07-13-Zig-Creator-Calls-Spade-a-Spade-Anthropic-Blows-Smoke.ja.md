---
layout: post
title: "AIが書いたコードは「ゴミ」か？ プログラミング言語ZigとAnthropicの正面衝突"
description: "AIで作成されたコードを全面的に禁止したプログラミング言語Zigと、それによって4倍の性能向上を諦めざるを得なかったAnthropicのBunの事例から見る、AI時代のソフトウェア開発論争。"
summary: "プログラミング言語ZigがAIによって作成されたあらゆる寄与を全面的に禁止したことで、Anthropicが買収したBunが開発した4倍高速な性能のコードが、公式プロジェクトに反映されないという事態が発生しました。"
tags: [AI, Zig, Bun, プログラミング, オープンソース]
image: 2026-07-13-Zig-Creator-Calls-Spade-a-Spade-Anthropic-Blows-Smoke.jpg
image_alt: "コンピューター画面の上でプログラミングコードとAIロボットアイコンが衝突する形状のグラフィック"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "オープンソースエコシステムがAIツールの活用をめぐって両極端に分かれています。技術的価値と開発者文化という二つの価値が衝突する地点で、私たちはどのような基準を設けるべきでしょうか。"
quiz:
  - question: "プログラミング言語ZigがAI関連の寄与を禁止した理由は何ですか？"
    choices: ["AIが出したコードが高価すぎるから", "AIコードが品質低く、レビュー時間を浪費するから", "著作権問題のため"]
    answer: 1
    explanation: "Zigの創設者アンドリュー・ケリーは、AIで生成されたコードが品質低く、検討時間を浪費するだけで価値がないと判断しました。"
  - question: "AnthropicのBunプロジェクトが開発した性能改善をZig公式プロジェクトに反映できなかった理由は何ですか？"
    choices: ["性能改善が十分でなかったから", "ZigのAI寄与全面禁止ポリシーのため", "技術的な互換性問題のため"]
    answer: 1
    explanation: "Bunは4倍の性能向上を達成しましたが、Zigの厳格なAI寄与禁止ポリシーにより、そのコードを公式プロジェクトに含める（アップストリームする）ことはできませんでした。"
  - question: "ZigのAI寄与禁止の範囲はどこまでですか？"
    choices: ["コードのみ禁止", "コード、コメント、イシュー、バグ報告への回答などすべての寄与を禁止", "既存の寄与者のみ禁止"]
    answer: 1
    explanation: "Zigはコードだけでなく、コメント、イシュー、プルリクエスト、バグトラッカーへの回答など、AIが関与したあらゆる形態の寄与を禁止しています。"
lang: ja
ref: 2026-07-13-Zig-Creator-Calls-Spade-a-Spade-Anthropic-Blows-Smoke
---

想像してみてください。あなたが数ヶ月間、夜を徹して作り上げた非常に効率的な機械装置があるとします。この装置は既存の部品より実に4倍も高速に動作します。ところが、この装置を公式生産ラインに乗せようとした瞬間、工場運営者が冷ややかに言います。「この装置を作る過程で人工知能（AI）ツールを少しでも使ったのですか？それなら絶対にダメです。今すぐ捨ててください。」

現在、オープンソースプログラミングの世界で、まさにこのようなことが起きています。プログラミング言語「Zig」と、Anthropicが買収したJavaScriptランタイム「Bun」の間で発生したこの事件は、AIがソフトウェア開発を支援するこの時代に、私たちが直面している極めて根本的な問いを投げかけています。

## なぜこれが重要なのか？

私たちの日常生活のアプリがどんどん賢くなっている背景には、数多くの開発者の努力があります。今日、開発者はAIツールを活用して、より速く効率的にソフトウェアを作ります。「誰が、どのように作ったか」が重要だという立場と、「技術的な結果さえ良ければそれでいい」という立場が正面から衝突しています。もしZigの事例のように、AIを活用した成果物すら排除されるのであれば、今後開発者はAIツールを使うことを躊躇するかもしれません。逆に、何の検証もなくAIコードが溢れかえれば、ソフトウェアの安定性は誰が責任を負うのでしょうか？

## 簡単に言うと（The Explainer）

Zigは広く使われている高性能プログラミング言語です。そしてBunはZigで作られたJavaScript実行環境であり、最近AI企業であるAnthropicに買収されました[Source 4, Source 6, Source 18]。

例えるなら、Zigは非常にこだわりを持った職人精神を大切にする「高級家具工房」です。この工房の代表であるアンドリュー・ケリー（Andrew Kelley）は、AIが作成したコードを見て「例外なくゴミ（invariably garbage）」と表現しました[Source 1, Source 5]。彼は、AIが書いたコードが実質的な価値はないにもかかわらず、中核となる開発チームの貴重なレビュー時間だけを浪費させると判断しました。そこで彼は、コードだけでなく、コメント、イシュー、さらにはバグ報告に対する回答まで、AIが少しでも関与していればその寄与を全面的に禁止する厳格なポリシーを立てました[Source 1, Source 2]。

一方、BunチームはAIを積極的に活用し、コンパイル（人間が書いたコードをコンピューターが理解できる言語に変換する過程）速度を約4倍も高める驚くべき成果を出しました[Source 2, Source 3, Source 4]。しかし、Zigの壁は厚いものでした。Bunチームはこの優れた成果を公式プロジェクトに含めようとしましたが、AIを使用したという事実から拒否されるのが明らかであったため、結局公式プロジェクトへの反映を諦め、別のバージョン（フォーク、fork）としてプロジェクトを維持することにしました[Source 2, Source 4]。

## 現在の状況

現在、Zigの立場は断固としています。AI活用かどうかが疑わしければ、技術的価値を吟味する前に拒否できるほど原則を固守しています[Source 2]。実際に多くの開発者がこのポリシーに対して熱い反応を見せています。一部では、BunプロジェクトのコードベースやドキュメントがAIが作成した文章（AI slop）で埋め尽くされることに反感を覚え、Bunを去ろうとする動きまで見せています[Source 17]。

その一方で、AnthropicとBunチームは技術的な利点のためにAIツールを使い続けると見られます。Bunは現在、Anthropicの「Claude Code」や「Claude Agent SDK」のためのインフラとして使用されているからです[Source 16, Source 18]。技術的成果を優先する側と原則を優先する側が、それぞれの道を行きながら共存していると言えます。

## 今後はどうなるか？

この論争は単に一つのプロジェクトだけの問題ではありません。「AIツールを使用した寄与をどこまで許可するか」は、今後すべてのオープンソースプロジェクトが答えを出さなければならない宿題となりました。Zigは非常に極端で明確な基準を提示しました。今後、より多くのプロジェクトがそれぞれの「AI寄与指針」を設けるようになり、Zigのように全面的に禁止するか、あるいは適切な検証プロセスを経て受け入れるかに分かれるでしょう。開発者は今や、自分が寄与するプロジェクトがどのようなポリシーを持っているのかを細かく調べなければならない時代を生きています。

## MindTickleBytesの視点

技術は単なる道具に過ぎないという主張と、その道具が作る結果物の本質が変わったという主張が鋭く対立しています。重要なのは道具を使用したか否かそのものではなく、その道具が最終的な結果物の品質とエコシステムの持続可能性にどのような影響を及ぼすかでしょう。Zigの厳格さがオープンソースの純粋性を守る盾となるのか、あるいは変化する開発の流れの中で自ら孤立を招く道となるのか、もう少し見守る必要があります。

## 参考資料

1. [Zig bans LLM contributions, forcing Bun to fork | AI Weekly](https://aiweekly.co/alerts/zig-bans-llm-contributions-forcing-bun-to-fork)
2. [Zig Draws Hard Line On AI, Bun Chooses Fork Over Upstreaming - Open Source For You](https://www.opensourceforu.com/2026/05/zig-draws-hard-line-on-ai-bun-chooses-fork-over-upstreaming/)
3. [ZIG BANNED ANTHROPIC FROM ITS OWN LANGUAGE #Shorts - YouTube](https://www.youtube.com/shorts/sYMuqS2oyUw)
4. [Zig Reinforces LLM Contribution Ban As Anthropic-Owned Bun Forks 4x Gain](https://winbuzzer.com/2026/05/01/zig-llm-contribution-ban-bun-4x-speedup-downstream-xcxwbn/)
5. [Zig president says AI coding contributions are 'invariably garbage,' so he banned them](https://www.businessinsider.com/zig-programming-language-ai-rules-2026-5)
6. [The Zig project's rationale for their firm anti-AI contribution policy](https://simonwillison.net/2026/Apr/30/zig-anti-ai/)
16. [Anthrophic's Bun team trials port from Zig to Rust](https://www.devclass.com/software/2026/05/11/anthrophics-bun-team-trials-port-from-zig-to-rust/5237835)
17. [This feels more like a reaction to Zig's anti-LLM policy than anything. Anthropi... | Hacker News](https://news.ycombinator.com/item?id=48017387)
18. [Bun’s Zig to Rust Rewrite: Anthropic’s AI Code Experiment | byteiota](https://byteiota.com/buns-zig-to-rust-rewrite-anthropics-ai-code-experiment/)