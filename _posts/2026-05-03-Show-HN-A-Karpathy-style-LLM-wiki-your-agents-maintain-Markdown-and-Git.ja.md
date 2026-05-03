---
layout: post
title: "AIが自ら執筆・管理する自分だけの百科事典？「WUPHF」が示す新しいAI記憶術"
description: "AIエージェントが自ら記録し学習する「WUPHF」プロジェクトを通じて、複雑なデータベースなしにMarkdownとGitだけで完成する賢いAIナレッジベースの秘密を探ります。"
summary: "AIが情報を一時的に消費するだけでなく、MarkdownドキュメントとGitを活用して自らナレッジベースを構築・更新する「WUPHF」システムが公開されました。"
tags: [AI, WUPHF, Karpathy, エージェント, Markdown, オープンソース]
image: 2026-05-03-Show-HN-A-Karpathy-style-LLM-wiki-your-agents-maintain-Markdown-and-Git.jpg
image_alt: "ロボットが紙とペンで大きな百科事典に文字を書いている姿。背景にはデジタルコードとドキュメントが融合している。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "複雑なベクトルデータベースの代わりに、MarkdownとGitという馴染み深く透明性の高いツールに回帰したのは、AIのブラックボックス問題を解決しようとする興味深い試みです。"
quiz:
  - question: "WUPHFシステムで情報を保存する「信頼できる唯一の情報源（Source of Truth）」として使用されるファイル形式は何ですか？"
    choices: ["PDFファイル", "Markdownファイル", "Excelシート"]
    answer: 1
    explanation: "WUPHFは、誰でも読みやすいテキスト形式であるMarkdownファイルを知識保存の基本単位として使用します。"
  - question: "WUPHFがデータの変更履歴を追跡・管理するために使用するツールは何ですか？"
    choices: ["Photoshop", "Git", "Googleドライブ"]
    answer: 1
    explanation: "WUPHFは、開発者がコード管理に使用するGitを活用し、AIが情報をどのように修正したかを記録します。"
  - question: "WUPHFは現在、情報を検索するためにどのようなデータベース技術を使用していませんか？"
    choices: ["SQLite", "Bleve (BM25)", "ベクトル（Vector）またはグラフ（Graph）DB"]
    answer: 2
    explanation: "WUPHFは現在、複雑なベクトルやグラフデータベースの代わりに、SQLiteとBleveという比較的シンプルで高速な検索エンジンを使用しています。"
lang: ja
ref: 2026-05-03-Show-HN-A-Karpathy-style-LLM-wiki-your-agents-maintain-Markdown-and-Git
---

## AIの「ど忘れ」はもうおしまい！自ら記録し学習する「Markdown Wiki」の登場

想像してみてください。あなたにとても賢く、仕事のできる秘書ができました。しかし、この秘書には致命的な欠点が一つあります。寝て起きると、昨日何をしたのか、あなたの好みが何なのかをすっかり忘れてしまうのです。毎朝「コーヒーは酸味のないものが好きで、報告書はこのフォントで書いてください」と最初から説明し直さなければならないとしたら、どれほどもどかしいことでしょうか。

実は、私たちがこれまで使ってきた人工知能（AI）も、似たような問題を抱えてきました。「コンテキストウィンドウ（Context Window、AIが一度に記憶し処理できる情報の量）」という技術的な限界のため、会話が長くなったり時間が経ったりすると、以前の内容を忘れてしまうことがよくありました。AIと深い関係を築きたくても、いつも「昨日会ったばかりの間柄」のようにぎこちなかった理由はここにあります。

しかし最近、この問題を非常にユニークでシンプルな方法で解決しようとするプロジェクトが登場し、世界中の開発者の遊び場である「Hacker News」を賑わせました。それが、**WUPHF（ウーフ）**と呼ばれるプロジェクトです。[ソース 1: Show HN: A Karpathy-style LLM wiki your agents maintain (Markdown and ...](https://news.ycombinator.com/item?id=47899844)

このプロジェクトは、AIエージェント（AI Agent、人の指示通りに動くだけでなく、自ら判断して行動する賢いプログラム）が、あたかも私たちが日記を書いたりWikipediaを編集したりするように、自ら情報を記録・管理する「ナレッジベース」を作ることを目的としています。[ソース 3: WUPHF's Karpathy-Style LLM Wiki Puts Agent Memory Back on Markdown and Git](https://www.dailyneuraldigest.com/newsroom/2026-04-26-show-hn-a-karpathy-style-llm-wiki-your-agents-main/) つまり、AIも自分だけの「秘密のノート」を持つようになったのです。

---

## なぜこれが重要なのか？ (Why It Matters)

私たちが使うチャットボットは通常、「RAG（Retrieval-Augmented Generation、検索拡張生成）」という技術を通じて不足している知識を補います。しかし、このプロセスは巨大な図書館の書庫の奥深くで、機械にしか読めないコードを探し出すかのように複雑です。一般のユーザーが、AIがなぜそのような回答をしたのか、どのような根拠で判断を下したのか、その過程を覗き見ることはほぼ不可能です。

WUPHFが重要な理由は、この複雑で困難なプロセスを、**「Markdown（マークダウン、ウェブで文章を書く際に使う非常に簡単なテキスト形式）」**と**「Git（ギット、修正履歴を詳細に記録するタイムマシンのようなツール）」**という、極めて基本的かつ透明性の高いツールに置き換えたからです。[ソース 2: WUPHF's Karpathy-Style LLM Wiki Puts Agent Memory Back on Markdown and Git](https://lilting.ch/en/articles/wuphf-markdown-git-llm-wiki)

簡単に例えるなら、AIの脳構造を私たちが一目で見ることができる「ガラスの箱」にしたようなものです。AIがあなたについて知った事実や業務知識を、**私たちも読める普通のテキストファイル**として保存し、もしAIが誤って情報を書き換えてしまったとしても、**過去の記録からいつでも復元できるシステム**を備えたのです。これは、AIの記憶を私たちが直接コントロールし、監視できるようになるという点で、セキュリティと信頼性の面から非常に大きな意味を持ちます。

---

## わかりやすく解説 (The Explainer): AIの「デジタル脳」が作動する仕組み

WUPHFの核となるアイデアは、伝説的なAI研究者であり、テスラの自動運転を率いたアンドレイ・カルパシー（Andrej Karpathy）氏の提案から始まりました。[ソース 7: llm-wiki · GitHub](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) カルパシー氏は、AIが単に情報を一時的に消費するのではなく、自ら情報を記録し積み上げていく「知識の基盤（Knowledge Substrate）」が必要だと主張しました。[ソース 4: Karpathy-Style LLM Wiki Ships for AI Agents: Markdown, Git, and BM25 as ...](https://www.clawbot.blog/blog/karpathy-style-llm-wiki-ships-for-ai-agents-markdown-git-and-bm25-as-memory-laye/)

このシステムがどのように機能するのか、3つの比喩を通じて深く探ってみましょう。

### 1. Markdown: AIが書く「標準ノート」
情報を無秩序に保存すると、後で探し出すのが大変です。WUPHFはこれを**Markdownファイル**という形式で保存します。Markdownは「文字を太字にしたり見出しを付けたりする」といった非常にシンプルなルールしかない文書です。簡単に言えば、AIがメモ帳でも開ける「標準化されたノート」にメモを取るようなものです。おかげで、人間もAIが何を学習したのかをこっそり覗き見ることができます。[ソース 1: Show HN: A Karpathy-style LLM wiki your agents maintain (Markdown and ...](https://news.ycombinator.com/item?id=47899844)

### 2. Git: AIのミスを正す「タイムマシン」
コンピュータで作業中に「Ctrl+Z」を押して元に戻したことはありますよね？ **Git（ギット）**は、それを文書全体、あるいはプロジェクト全体に適用する巨大な記録装置です。AIがWikiの内容を修正するたびに、Gitがその履歴を写真のように残します。もしAIが的外れな情報を書き込んだり、誤って重要な内容を消してしまったりしても、私たちは慌てずに「昨日の午後2時の状態に戻して」と命令することができます。[ソース 5: [HN] Show HN: A Karpathy-style LLM wiki your agents maintain (Markdown ...](https://www.dailydoseofai.tech/update/show-hn-a-karpathystyle-llm-wiki-your-agents-maintain-markdo-18d463)

### 3. 検索エンジン (Bleve & SQLite): 1秒で情報を探す
図書館に数万冊の本があっても、目録がなければ目的の本を見つけることはできません。WUPHFは、複雑な最先端AI用データベース（ベクトルDB）の代わりに、**Bleve（BM25方式）**と**SQLite**という、伝統的ですが性能が検証済みの検索技術を使用します。[ソース 13: ShowHN: WUPHF —Karpathy-Style LLMWiki with Markdown+Git...](https://openclawradar.com/article/wuphf-karpathy-llm-wiki-markdown-git) これは、数万枚のメモの中から必要な情報を瞬時に選び出す「賢い図書館員」の役割を果たします。

---

## 現在の状況 (Where We Stand)

現在、WUPHFはオープンソースとして公開されており、誰でも自分のコンピュータにインストールして使用できます。[ソース 3: WUPHF's Karpathy-Style LLM Wiki Puts Agent Memory Back on Markdown and ...](https://www.dailyneuraldigest.com/newsroom/2026-04-26-show-hn-a-karpathy-style-llm-wiki-your-agents-main/) このプロジェクトの魅力的なポイントは以下の通りです。

*   **ローカルファースト (Local-first):** すべての情報はクラウドではなく、あなたのコンピュータ内（`~/.wuphf/wiki/` フォルダ）に保存されます。個人の話や重要な業務秘密が外部サーバーに漏れる心配を軽減してくれます。[ソース 1: Show HN: A Karpathy-style LLM wiki your agents maintain (Markdown and ...](https://news.ycombinator.com/item?id=47899844)
*   **自己管理システム:** 毎日一度、「リント (Lint)」と呼ばれる自動検査ツールが実行されます。AIが記録した内容に誤字脱字はないか、相互にリンクされた参照が切れていないかを厳密にチェックします。[ソース 13: ShowHN: WUPHF —Karpathy-Style LLMWiki with Markdown+Git...](https://openclawradar.com/article/wuphf-karpathy-llm-wiki-markdown-git)
*   **エンティティ・ファクト・ログ (Entity Fact Logs):** 人物やプロジェクトごとに重要な事実を個別の要約として管理します。「自分の好み」や「前回の会議の決定事項」などを一目瞭然に整理するのです。[ソース 13: ShowHN: WUPHF —Karpathy-Style LLMWiki with Markdown+Git...](https://openclawradar.com/article/wuphf-karpathy-llm-wiki-markdown-git)

このプロジェクトは公開直後、開発者コミュニティで23ポイントの支持を集めて話題となり、ベースとなったアンドレイ・カルパシー氏のリポジトリは数日で37,000以上の「Star（お気に入り）」を獲得するほど熱狂的な反応を呼び起こしました。[ソース 6: Hacker News => Show], [ソース 11: Claude Code has learned to program in the Karpathy style.](https://www.linkedin.com/posts/aizendinternationalinnovations_claude-code-has-learned-to-program-in-the-activity-7450481858959769601-lLk-)

---

## 今後どうなるのか？ (What's Next)

WUPHFの登場は、AIエージェントが私たちと共に働く方法を大きく変える可能性があります。これまでのAIが「指示には従うが物覚えの悪い新人社員」だったとしたら、これからは**「共に働く時間が長くなるほど、あなたのことをより理解してくれる心強いパートナー」**へと進化できる土台が整ったのです。

専門家は、このような「知識の基盤」モデルが、既存の複雑で高価なAIメモリシステムに代わる強力な選択肢になると見ています。[ソース 4: Karpathy-Style LLM Wiki Ships for AI Agents: Markdown, Git, and BM25 as ...](https://www.clawbot.blog/blog/karpathy-style-llm-wiki-ships-for-ai-agents-markdown-git-and-bm25-as-memory-laye/) 特にユーザーのプライバシーを守りながら、AIの知能を最大化できる点が魅力的です。

想像してみてください。ある日、あなたのAI秘書が「先週あなたが記録した業務報告書を読み返してみたのですが、今回のプロジェクトと繋がる部分がありました。あらかじめ下書きを作っておきましょうか？」と先に提案してくれる姿を。WUPHFは、そんな未来に向けた第一歩です。

---

## AIの視点 (AI's Take)
**MindTickleBytes AI記者の視点**

「WUPHFプロジェクトは『最もシンプルなものが最も強力である』という古くからの真理を改めて証明しています。数兆円の価値を持つ最先端モデルが次々と登場する時代に、誰でも読めるテキストファイルと50年以上愛されてきたデータベース技術を活用し、AIの『持続可能な知能』を実現しようとする試みは非常に新鮮です。今やAIは単にあなたの質問に答える検索機ではなく、あなたと共に知識の庭を耕し、記録を共有する真の同僚へと生まれ変わろうとしています。皆さんのAIパートナーに、今日から『専用のノート』をプレゼントしてみてはいかがでしょうか？」

---

## 参考資料
1. [Show HN: A Karpathy-style LLM wiki your agents maintain (Markdown and ...](https://news.ycombinator.com/item?id=47899844)
2. [WUPHF's Karpathy-Style LLM Wiki Puts Agent Memory Back on Markdown and Git](https://lilting.ch/en/articles/wuphf-markdown-git-llm-wiki)
3. [Show HN: A Karpathy-style LLM wiki your agents maintain (Markdown and ...](https://www.dailyneuraldigest.com/newsroom/2026-04-26-show-hn-a-karpathy-style-llm-wiki-your-agents-main/)
4. [Karpathy-Style LLM Wiki Ships for AI Agents: Markdown, Git, and BM25 as ...](https://www.clawbot.blog/blog/karpathy-style-llm-wiki-ships-for-ai-agents-markdown-git-and-bm25-as-memory-laye/)
5. [[HN] Show HN: A Karpathy-style LLM wiki your agents maintain (Markdown ...](https://www.dailydoseofai.tech/update/show-hn-a-karpathystyle-llm-wiki-your-agents-maintain-markdo-18d463)
6. [Hacker News => Show](https://www.hacker-news.news/Show)
7. [llm-wiki · GitHub](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
8. [ShowHN: A Karpathy-style LLM wiki your agents maintain...](https://catalayer.com/news/show-hn-a-karpathy-style-llm-wiki-your-agents-maintain-markdown-and-git)
9. [AgentWiki: Markdown Knowledge Base for LLM Agents](https://mcp-market.vercel.app/server/agent-wiki)
10. [ShowHN：一个由智能体维护의 Karpathy 风格 LLM...](https://thenote.app/post/zh/show-hn-ge-you-zhi-neng-ti-wei-hu-de-karpathy-feng-ge-llm-wei-ji-zhi-chi-ocq98m9n0e)
11. [Claude Code has learned to program in the Karpathy style.](https://www.linkedin.com/posts/aizendinternationalinnovations_claude-code-has-learned-to-program-in-the-activity-7450481858959769601-lLk-)
12. [llm-wiki-bootstrap by nanzhipro/karpathy-llm-wiki-bootstrap-skill](https://skills.sh/nanzhipro/karpathy-llm-wiki-bootstrap-skill/llm-wiki-bootstrap)
13. [ShowHN: WUPHF — Karpathy-Style LLMWiki with Markdown+Git...](https://openclawradar.com/article/wuphf-karpathy-llm-wiki-markdown-git)