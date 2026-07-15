---
layout: post
title: "AIが許可なくコードを修正？その『理由』を記録する賢いツール「Grepathy」"
description: "AIエージェントがコードを修正した際、その決定理由を透明に追跡できるツール「Grepathy」について解説します。"
summary: "AIの決定理由を記録・保存し、作業履歴の消失を防ぐ「Grepathy」を紹介します。"
tags: [AI, Claude, Grepathy, 開発ツール, 透明性]
image: 2026-07-16-Show-HN-Grepathy-Claude-made-a-decision-nobody-approved.jpg
image_alt: "AIの決定を文書化し、コードリポジトリに保存するGrepathyの仕組みをイメージした画像。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AIの自律性が高まるにつれ、その決定根拠を追跡する透明性は選択ではなく必須です。Grepathyは、開発者がAIと共存するために必要な『説明可能性』を実用的な方法で実現しました。"
quiz:
  - question: "Grepathyが開発された最大の理由は何ですか？"
    choices: ["AIの速度を向上させるため", "AIの決定理由を記録し、履歴の消失を防ぐため", "AIのエラーを自動修正するため"]
    answer: 1
    explanation: "Grepathyは、AIエージェントが下した決定理由をローカルリポジトリに残し、履歴が消えてしまう問題を解決するために作られました。"
  - question: "Grepathyはどのようなデータを保存しますか？"
    choices: ["ユーザーとの全会話内容", "AIが下した決定（reasoning）のみを選別して保存", "PC上の全ファイルリスト"]
    answer: 1
    explanation: "Grepathyは会話内容のすべてではなく、AIが下した決定（decisions）情報のみを選別し、マークダウン形式で保存します。"
  - question: "Grepathyはどのような方法で実行されますか？"
    choices: ["ユーザーが毎回手動で実行する必要がある", "常にバックグラウンドで実行されている", "Gitフックを通じて自動的に実行される"]
    answer: 2
    explanation: "Grepathyはユーザーが毎回実行する必要はなく、Gitフックを通じて作業プロセス中に自動的に実行されます。"
lang: ja
ref: 2026-07-16-Show-HN-Grepathy-Claude-made-a-decision-nobody-approved
---

想像してみてください。忙しい朝、賢いAIコーディングエージェントに「このプロジェクトのコードをきれいに整理しておいて」と頼んで会議に向かいました。夕方戻ってコードを確認すると、なんと！AIはあなたが絶対にいじってはいけないと思っていたコアロジックまで修正してしまっていました。「一体なぜこんな決定をしたんだ？」と理由を探そうとしますが、AIツールはすでに数日前の作業記録をすべて削除してしまっています。[Show HN: Grepathy – Claude made a decision nobody approved](https://news.ycombinator.com/item?id=48920537)

このような状況は、もはや遠い未来の話ではありません。最近の開発者の間では、AIが自らコードを修正し決定を下す「エージェント時代」が到来しましたが、その成果物の背後に隠れた「理由」が消えてしまい困惑するケースが増えています。今回紹介する**Grepathy（グレパシー）**は、まさにこの「消えていく決定の理由」を留めておくために登場しました。

### なぜこれが重要なのか？

AIが単に回答を与える段階を超え、直接コードを書いたりファイルを修正したりする「エージェント（特定の目標を自律的に遂行するAI）」として活動するようになり、**「責任の所在」と「追跡可能性」**が非常に重要になりました。[Show HN: Grepathy – Claude made a decision nobody approved](https://news.ycombinator.com/item?id=48920537)

多くのAIツール、特に「Claude Code（AIが開発環境で直接コードを修正・実行するツール）」のようなサービスは、デフォルト設定では一定期間（30日）が過ぎると作業記録（transcript）を削除します。[Show HN: Grepathy – Claude made a decision nobody approved](https://news.ycombinator.com/item?id=48920537) これはプライバシー保護やストレージの面では効率的かもしれませんが、後になって「AIはなぜこのコードをこのように変えたのか？」という問いに答えなければならない開発者にとっては致命的になり得ます。Grepathyは、AIが自ら下した決定の根拠を記録として残すことで、後から誰でもその理由を確認できるように支援します。

### 分かりやすく言えば：AIの「業務日誌」を残す方法

このように例えると簡単です。プロジェクトを進行するチームに、非常に優秀ですが記憶力が短い新入社員（AI）が一人います。この社員は仕事は本当にできますが、30日が過ぎると自分がなぜその決定を下したのか忘れてしまいます。Grepathyは、この新入社員の**「決定日誌」を受け取って書き留める秘書**のような存在です。

1. **インテリジェントな選別記録**: GrepathyはユーザーとAIが交わした私的な会話内容まで全てを保存しません。AIが「どのような決定を下したか」という理由（reasoning）だけを選別します。[Show HN: Grepathy – Claude made a decision nobody approved](https://news.ycombinator.com/item?id=48920537)
2. **コードリポジトリへの直接保存**: 記録された決定はマークダウン（Markdown）形式に変換され、あなたのコードと共にリポジトリに永続的に残ります。[Show HN: Grepathy – Claude made a decision nobody approved](https://news.ycombinator.com/item?id=48920537)
3. **自動化**: ユーザーが面倒なコマンドを打つ必要もありません。Gitフック（特定のイベントが発生した際に自動的に実行されるスクリプト）を通じて、コードをコミットしたりプッシュしたりするたびに、Grepathyが勝手に動作します。[GitHub - evansjp/grepathy](https://github.com/evansjp/grepathy)

簡単に言えば、プロジェクトフォルダ内で特定のコマンドを実行するだけで、AIが残した「なぜそうしたのか」という答えを一目で確認できるのです。[GitHub - evansjp/grepathy](https://github.com/evansjp/grepathy)

### 現状：AIと共に働くということ

AIコーディングツールは日々進化しています。Claude Codeのようなツールは、基本的に人間が最終確認を行う「Human-in-the-loop（人間がAIの作業を監督する方式）」を採用していますが、Autoモードの導入により、人間の直接的な介入なしに多くの仕事を自律的に処理するようになりました。[Claude Code Defaults to Human Approval: Auto Mode Requires Explicit Opt-In](https://www.techtimes.com/articles/319874/20260707/claude-code-defaults-human-approval-auto-mode-requires-explicit-opt.htm)

しかし、技術が発展するほど、AIの判断を信頼し管理する透明性の問題は大きくなっています。開発者の間では、AIが虚偽の情報を作ったり、事実関係を歪曲したりする事例が共有されることもあり、[How to Stop Claude From Making $#it Up](https://medium.com/@brentwpeterson/how-to-stop-claude-from-making-it-up-921a6a9238c8) 企業レベルでも、AIエージェントの決定が予期せぬ結果を招く可能性を警戒しています。[The Day an AI Agent Commits Your Company to a Decision Nobody ...](https://www.linkedin.com/posts/bhaviavelayudhan_the-day-an-ai-agent-commits-your-company-activity-7436671325772898305-TdKd)

### 今後はどうなるか？

Grepathyのような試みは今後さらに重要になるでしょう。AIが単にコードを書くレベルを超え、プロジェクトの方向性を決定する意思決定の主体へと成長するにつれ、その根拠を残すことは法的、倫理的にも必ず必要なプロセスになるからです。

明日朝、あなたのAIエージェントがコードを修正したら、Grepathyを通じてその決定の「理由」を一度確認してみてはいかがでしょうか？AIと人間が透明にコミュニケーションする第一歩になるかもしれません。

## 参考資料
1. [Show HN: Grepathy – Claude made a decision nobody approved | Hacker News](https://news.ycombinator.com/item?id=48920537)
2. [GitHub - evansjp/grepathy: Your agent writes down why, in the repo, so everyone else's agents can find it without asking you. · GitHub](https://github.com/evansjp/grepathy)
3. [Claude Code Defaults to Human Approval: Auto Mode Requires Explicit Opt-In](https://www.techtimes.com/articles/319874/20260707/claude-code-defaults-human-approval-auto-mode-requires-explicit-opt.htm)
4. [How to Stop Claude From Making $#it Up | by Brent W. Peterson | May, 2026 | Medium](https://medium.com/@brentwpeterson/how-to-stop-claude-from-making-it-up-921a6a9238c8)
5. [The Day an AI Agent Commits Your Company to a Decision Nobody ...](https://www.linkedin.com/posts/bhaviavelayudhan_the-day-an-ai-agent-commits-your-company-activity-7436671325772898305-TdKd)