---
layout: post
title: "AIが11日間で100万行のコードを書き直した？「Bun」の驚くべき変身"
description: "AIを活用した大規模コード移行の歴史、JavaScriptランタイム「Bun」がRust言語で生まれ変わるまでの過程を追います。"
summary: "AIモデル「Claude」が、JavaScriptランタイム「Bun」のコード100万行以上を、わずか11日間でRust言語に書き直しました。"
tags: [AI, Bun, Rust, Claude, プログラミング]
image: 2026-07-19-Claude-Code-uses-Bun-written-in-Rust-now.jpg
image_alt: "AIがコードを最適化・再構築する様子を象徴するデジタルグラフィック。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "人間3人が1年かかる仕事をAIが11日で成し遂げたという事実は、ソフトウェア開発のパラダイムが完全に変わったことを示しています。これからは「コードをいかに速く書くか」ではなく、「AIをいかに使いこなすか」が開発者の核心的な能力となります。"
quiz:
  - question: "「Bun」が元々書かれていた言語は何ですか？"
    choices: ["Rust", "Zig", "Python"]
    answer: 1
    explanation: "Bunは当初Zig言語で書かれていましたが、最近Claude AIを活用してRustへの言語移行を完了しました。"
  - question: "今回のコード書き直しプロジェクトにかかった時間はどれくらいですか？"
    choices: ["11日間", "11ヶ月", "1年間"]
    answer: 0
    explanation: "Bunの創設者ジャレッド・サムナー氏は、Claude Codeを活用して約100万行のコードを11日間で書き直しました。"
  - question: "今回のRust言語移行によるパフォーマンス改善効果は何ですか？"
    choices: ["ファイルダウンロード速度が50%向上", "Linux環境での起動速度が10%改善", "メモリ使用量を90%削減"]
    answer: 1
    explanation: "Linux環境において、Claude Codeの起動速度が以前より10%速くなりました。"
lang: ja
ref: 2026-07-19-Claude-Code-uses-Bun-written-in-Rust-now
---

想像してみてください。100万ページを超える巨大な図書館の本を、別の言語に翻訳しなければならないとしたら？人が直接行えば数年かかるこの膨大な作業を、わずか11日間で終わらせることができるとしたらどうでしょうか。最近、ソフトウェア開発の分野で、これと同じような驚くべきことが実際に起こりました。

AIモデル「Claude」が、JavaScript（ウェブブラウザで実行されるプログラミング言語）ランタイムである「Bun」の核心部分を、まったく新しい言語である「Rust（メモリ安全性とパフォーマンスを重視するシステムプログラミング言語）」を使って、100万行以上のコードを書き直したのです [Source 9, Source 13]。本記事では、この大規模なコード移行がなぜ重要なのか、そして私たちの日常にどのような意味があるのかを分かりやすく解説します。

### なぜこれが重要なのか？

「Bun」は、開発者がJavaScriptやTypeScriptのコードをより速く、効率的に実行できるよう支援するツールです [Source 3, Source 4]。では、なぜこの重要なツールを従来の言語からRustに変更したのでしょうか。

最大の理由は「安全性」と「速度」です。Rust言語はコンピュータのメモリをより安全に管理できるため、プログラムが予期せず停止する現象を減らすことができます [Source 3, Source 10]。また、パフォーマンスの最適化にも有利です。実際に今回の書き直し後、「Claude Code（AI補助プログラミングツール）」はLinux環境での起動速度が以前より10%速くなりました [Source 1, Source 7]。これは私たちのような一般ユーザーにはわずかな差かもしれませんが、技術的には非常に重要な進歩です。

### 分かりやすい例え：レシピを変えるようなもの

このように例えてみましょう。皆さんが数千人に料理を提供する大型レストランを経営していると考えてみてください。最初は「Zig」という道具を使ってレシピを精巧に作りました。しかし、より安全かつ効率的に料理を届けたいと思い、世界中のシェフが最も信頼する「Rust」という新しい道具でレシピを完全に作り直すことにしました。

かつては、この膨大なレシピを一人ずつ人間が書き直さなければなりませんでした。しかし今回は、Claudeという「超人的なAI助手」がレシピを代わりに書いてくれたのです。Bunの創設者であるジャレッド・サムナー（Jarred Sumner）氏は、約50個のAIワークフロー（作業工程）を設定し、Claude Codeが11日間休むことなく100万行以上のコードをRustへ移行させるよう指揮しました [Source 12, Source 13]。人が行えば3人で1年はかかる作業を、AIと共に短期間で終えたことになります [Source 16]。

### 現在の状況：AIがコードを直接管理する時代

現在、Claude Code 2.1.181バージョンからは、この新しいRustベースのBunランタイムが含まれて提供されています [Source 1, Source 7]。開発者はこれまで通りコードを書きますが、裏で動くエンジンは、より安全で速いRustベースのエンジンに置き換わったのです。

もちろん、このようなAIによる大規模なコード修正に対して、全員が拍手を送っているわけではありません。一部では、AIが生成したコードに対する検証プロセスが不足しているのではないかという懸念の声もあります [Source 13]。しかしAnthropic（Claudeの開発元）は今回のプロジェクトを通じて、AIがいかに複雑で巨大なソフトウェアプロジェクトを成功させられるか、その可能性を証明しました [Source 9, Source 16]。

### 今後はどうなるのか？

今回の事例は、AIが単に質問に答えたり文章を書いたりするレベルを超えて、巨大な技術的基盤を直接作り変える「エンジニアリングの主体」になれることを示しています [Source 9, Source 10]。今後、私たちが使用するアプリやサービスがより安全かつ高速にアップデートされる際、その裏には人間と一緒になって昼夜を問わずコードを修正するAI同僚がいる可能性が非常に高いでしょう。

今後私たちは、AIが作り出す複雑な技術的転換がもたらす、より速く強力なソフトウェア環境を迎えることになるでしょう。変化はすでに始まっており、そのスピードは私たちの予想をはるかに超えています。

### MindTickleBytesのAI記者の視点
今回の事件は、単に言語を一つ入れ替えただけのものではありません。人間が1年かけて行うべき苦しい作業をAIが11日間で完遂したことは、「ソフトウェアのメンテナンス」の定義そのものが変わったことを意味します。これからは技術変化への恐れよりも、AIという道具をいかに賢く使って、私たちが望む未来をより早く手繰り寄せるかを悩むべき時です。

## 参考資料

1. [Claude Code uses Bun written in Rust now - simonwillison.net](https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/)
2. [Claude Code uses Bun written in Rust now - daily.dev](https://daily.dev/posts/claude-code-uses-bun-written-in-rust-now-sxbybasdo)
3. [Claude Code uses Bun written in Rust now | DeepHorus](https://www.deephorus.com/blog/2026-07-19-claude-code-uses-bun-written-in-rust-now/)
4. [Claude Code uses Bun written in Rust now | AINews](https://www.ainews.tech/article/2058)
5. [Rewriting Bun in Rust | Bun Blog](https://bun.com/blog/bun-in-rust)
6. [Claude Code adopts Rust-based Bun runtime for faster startup ...](https://news.linxi.com.au/news/claude-code-shifts-to-rust-based-bun-runtime-claiming-faster-startup)
7. [Claude Code adopts Bun runtime rewritten in Rust, speed ...](https://savedelete.com/news/claude-code-bun/)
8. [Bun Rewrites in Rust: Technical Review of the Zig-to-Rust Migration | Fawad Hussain Syed](https://fawadhs.dev/blog/bun-rust-rewrite-technical-review)
9. [Claude Rewrites Bun's Million Lines of Code in 11 Days for $165,000, Setting a New Benchmark for AI-Assisted Programming — BigGo Finance](https://finance.biggo.com/news/b171d858-6390-4aef-bd0b-a651cfa942f6)
10. [Burned $160,000, Wrote 1M Lines of Code Nonstop: How Bun's Founder Rewrote the Entire JavaScript Runtime Foundation Using Claude AI](https://eu.36kr.com/en/p/3899401843017608)
11. [AI Porting: Claude Rewrites Bun Codebase in Rust | heise online](https://www.heise.de/en/news/AI-Porting-Claude-Rewrites-Bun-Codebase-in-Rust-11294318.html)
12. [How Bun's founder rewrote the codebase in Rust with Claude](https://www.thestack.technology/bun-rust-rewrite-fable-ai/)
13. [Zig creator calls Bun’s Claude Rust rewrite ‘unreviewed slop’](https://www.theregister.com/devops/2026/07/14/zig-creator-calls-buns-claude-rust-rewrite-unreviewed-slop/5270743)
15. [Why not rewrite claude-code in Rust? So, Anthropic acquires Bun team because cla... | Hacker News](https://news.ycombinator.com/item?id=48019019)
16. [One Anthropic Engineer Rewrites Bun In Rust In 11 Days With AI, Says Would've Taken 3 Engineers A Year Earlier](https://officechai.com/ai/one-anthropic-engineer-rewrites-bun-in-rust-in-11-days-with-ai-says-wouldve-taken-3-engineers-a-year-earlier/)