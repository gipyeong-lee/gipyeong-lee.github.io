---
layout: post
title: "AIが数十万行のコードを自ら書き換えた？マイクロソフトによる1億6千万円の「Rust」大手術"
description: "マイクロソフトがAIエージェントを使い、GitHub Copilotの基盤コードをRustで完全に書き換えました。12万ドルを投じたこの巨大な実験の意義を探ります。"
summary: "マイクロソフトがAIエージェントを活用し、GitHub Copilotの基盤ソフトウェアを43万行のTypeScriptから80万行以上のRustコードへ成功裏に書き換えました。"
tags: [AI, GitHub, Copilot, Rust, ソフトウェア開発]
image: 2026-10-14-Microsoft-agentically-ports-Copilot-runtime-to-Rust-for-120K.jpg
image_alt: "マイクロソフトとGitHubのロゴが融合した現代的な開発環境をイメージした画像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "今回の事例は、AIが単なるツールを超え、複雑なエンジニアリングプロジェクトを自ら完遂する主体へと進化したことを示しています。"
quiz:
  - question: "今回のマイクロソフトのプロジェクトでAIエージェントが果たした核心的な役割は何ですか？"
    choices: ["デザイン案の生成", "既存コードをRustへ変換", "サーバーインフラの物理的設置"]
    answer: 1
    explanation: "AIエージェントは、GitHub Copilotの基盤となるTypeScriptコードをRust言語で書き換える役割を担いました。"
  - question: "このプロジェクトが過去には不可能だと考えられていた理由は何ですか？"
    choices: ["言語の種類が多すぎたため", "AIエージェントの存在自体がなかったため", "規模があまりにも大きく複雑な書き換えだったため"]
    answer: 2
    explanation: "このような大規模システムの全面的な書き換えは、人間の開発者にとっても非常に困難かつ非効率な作業であり、AIエージェント導入前は実現不可能と考えられていました。"
  - question: "今回のプロジェクトにかかったAIコンピューティングコストはどの程度ですか？"
    choices: ["約12万ドル（約1億6千万円）", "約5万ドル", "費用発生なし"]
    answer: 0
    explanation: "マイクロソフトは、今回の大規模コード移行のために約12万ドル相当のコンピューティングおよびトークン費用を支出しました。"
lang: ja
ref: 2026-10-14-Microsoft-agentically-ports-Copilot-runtime-to-Rust-for-120K
---

想像してみてください。あなたが巨大な図書館の司書で、図書館全体の分類体系を全く別の方法でゼロから構築し直さなければならないとしたら。数十万冊の本を取り出して、新しいルールに合わせて再整理する仕事は、一人では途方もない作業ですよね。ところが、何千人ものAI司書が一斉に投入され、たった数週間でこれを終えたとしたらどうでしょう？

マイクロソフトとGitHubは最近、これに近いことをやってのけました。多くの開発者が愛用するAIツール「GitHub Copilot」の核心エンジンを、別のプログラミング言語へ完全に入れ替えたのです。

### なぜこれが重要なのか？

「ランタイム（プログラムの実行環境）」という言葉は少し馴染みがないかもしれません。簡単に言えば、私たちが毎日使うGitHub Copilotアプリやツールがスムーズに動作するよう、裏側で黙々と支えている「基盤エンジン」のことです。このエンジンが変わったということは、Copilotがより速く、より安定して私たちのそばに存在できるようになったことを意味します。

何より驚くべきは、このプロジェクトが人の手作業ではなく、自ら考え判断する**「自律型AIコーディングエージェント（Autonomous AI coding agents）」**が主導したという事実です [[出典 7](https://www.linkedin.com/posts/breno-gsouza_migrating-the-github-copilot-runtime-to-rust-activity-7508733301516382208-TmkQ), [出典 9](https://www.usefulainews.com/microsoft-agentically-ports-copilot-runtime-to/)]。

### わかりやすく解説：言語を入れ替える大手術

コンピュータのプログラミング言語は、私たちが使う日本語や英語に似ています。ただ、コンピュータに命令を下すルールが異なるだけです。今回マイクロソフトは、従来使用していた「TypeScript（ウェブ開発に主に使われる言語）」から、「Rust」という言語へエンジンを入れ替えました。

例えるなら、TypeScriptが自由な執筆ができる「普通のノート」だとすれば、Rustは「ルールが非常に厳格な数学の公式集」のようなものです。Rustはコードの安全性を重視するため、一度書いてしまえばエラーが起きる確率が他の言語に比べて極めて低くなります。しかし、人が手作業で数十万行ものコードをこれほど厳格な言語に書き換えるのは、数千ページの論文を一語も間違えずに新しいルールで書き直すような、気が遠くなる作業です。

マイクロソフトのエンジニアたちは、この仕事を遂行するために**AIエージェント**という賢い助手を雇用しました。AIエージェントはベテラン開発者のように既存のコードを読み込み、文脈を把握した上で、それを安全なRustコードへ変換しました。その結果、43万行に及んでいたTypeScriptコードが、80万行以上のRustコードとして生まれ変わったのです [[出典 7](https://www.linkedin.com/posts/breno-gsouza_migrating-the-github-copilot-runtime-to-rust-activity-7508733301516382208-TmkQ), [出典 12](https://www.tabnews.com.br/NewsletterOficial/microsoft-reescreve-runtime-do-copilot-em-rust)]。

### 現状：AIが成し遂げた不可能任務

以前であれば、このプロジェクトは「不可能」と見なされ、着手すらされなかったでしょう。しかしAIエージェントを導入したことで、この巨大な移行作業は、開発者の工数として約3週間、14.5週間続いた135回のアップデートを経て成功裏に幕を閉じました [[出典 6](https://sygentai.com/blog/2026-09-21-google-shipped-an-open-agentic-orchestrator-and-what-it-actually-takes-off-your-), [出典 7](https://www.linkedin.com/posts/breno-gsouza_migrating-the-github-copilot-runtime-to-rust-activity-7508733301516382208-TmkQ)]。

この過程で12万ドル（約1億6千万円）相当のトークン（AI処理コスト）が消費されました [[出典 9](https://www.usefulainews.com/microsoft-agentically-ports-copilot-runtime-to/), [出典 16](https://www.linkedin.com/posts/basharatwani_migrating-the-github-copilot-runtime-to-rust-activity-7508513737730084865-vrkT)]。高額に感じるかもしれませんが、何十人もの開発者が数ヶ月張り付かなければならない大規模手術のコストを考えれば、AIの効率がいかに高いか分かります。もちろん過程で数十件の修正が必要なエラーも発生しましたが、最終的にはコードの品質を維持したまま、完全な移行を成し遂げました [[出典 12](https://www.tabnews.com.br/NewsletterOficial/microsoft-reescreve-runtime-do-copilot-em-rust), [出典 16](https://www.linkedin.com/posts/basharatwani_migrating-the-github-copilot-runtime-to-rust-activity-7508513737730084865-vrkT)]。

### 今後はどうなるか？

今回の事例は、ソフトウェア開発の未来を示す強力な狼煙です。今後は「開発者がコードを直接書く時代」を超え、「開発者がAIエージェントに目標を提示し、結果を検討する時代」へと急速にシフトするでしょう。

マイクロソフトの成功は、今後企業がレガシーシステムを現代的な環境へと刷新する際、AIエージェントの活用が必須になることを示唆しています。あなたが使うスマートフォンの音声アシスタントや業務チャットツールが、いつの日かより速く安全なエンジンに置き換わっていたら、その裏には今回のようなAIによる大規模な庭師の作業があったのかもしれません。

---
**MindTickleBytesのAI記者による視点**
AIが自らコードを修正・改善できるということは、単なる費用の問題ではありません。人間が技術的な限界から諦めていたアイデアが、AIエージェントという翼を得て現実となる時代が到来したことを意味しています。

## 参考資料
1. [MicrosoftagenticallyportsCopilotruntimetoRustfor$120K](https://www.devclass.com/devops/2026/09/19/microsoft-agentically-ports-copilot-runtime-to-rust-for-120k/5297592)
2. [Vue HN 2.0 |MicrosoftagenticallyportsCopilotruntimetoRustfor...](https://vue-hackernews-ssr-5cavbdjcta-ew.a.run.app/item/49763701)
3. [Unsealed Documents HighlightMicrosoftAnd OpenAI Concerns Over...](https://www.finanznachrichten.de/nachrichten-2026-09/69622107-unsealed-documents-highlight-microsoft-and-openai-concerns-over-use-of-news-content-020.htm)
4. [Microsoftand Citrix mix 'n' match fake desktops](https://www-theregister-co-uk.nproxy.org/2009/07/13/citrix_microsoft_virtual_pcs/)
5. [Rustin Visual Studio Code](https://code.visualstudio.com/docs/languages/rust)
6. [Google shipped an open agentic orchestrator, and what it actually...](https://sygentai.com/blog/2026-09-21-google-shipped-an-open-agentic-orchestrator-and-what-it-actually-takes-off-your-)
7. [AI Accelerates Code Production, Not Responsibility | LinkedIn](https://www.linkedin.com/posts/breno-gsouza_migrating-the-github-copilot-runtime-to-rust-activity-7508733301516382208-TmkQ)
9. [MicrosoftAgenticallyPortsCopilotRuntimetoRust](https://www.usefulainews.com/microsoft-agentically-ports-copilot-runtime-to/)
10. [Vue HN 2.0 |MicrosoftagenticallyportsCopilotruntimetoRustfor...](https://vue-hackernews-ssr-5cavbdjcta-ew.a.run.app/item/49773998)
11. [Microsoftporte leruntimeCopilotversRustde façon... — Fellow](https://www.fellow.news/article/www.theregister.com-devops-2026-09-18-microsoft-agentically-ports-copilot-runtime-to-rust-for-120k-5297549)
12. [MicrosoftreescreveruntimedoCopilotemRust· NewsletterOficial](https://www.tabnews.com.br/NewsletterOficial/microsoft-reescreve-runtime-do-copilot-em-rust)
14. [MicrosoftagenticallyportsCopilotruntimetoRustfor$120K](https://modernorange.io/item/49773998)
15. [GoogleNews-Microsoft-Latest](https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFJ6ZGpRU0FtVnNLQUFQAQ?hl=en-US&gl=US&ceid=US:en)
16. [GitHub Engineers Use AI Agents toPortCodebasetoRust| LinkedIn](https://www.linkedin.com/posts/basharatwani_migrating-the-github-copilot-runtime-to-rust-activity-7508513737730084865-vrkT)
17. [MicrosoftagenticallyportsCopilotruntimetoRustfor...](https://vk.ru/wall-238001904_5872)
18. [RuStore — каталог мобильных приложений и игр для Android](https://www.rustore.ru/)