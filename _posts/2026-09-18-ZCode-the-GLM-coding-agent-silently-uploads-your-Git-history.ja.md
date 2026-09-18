---
layout: post
title: "私のコーディング履歴がクラウドにこっそり送信されている？ZCodeの密かなデータ流出問題"
description: "AIコーディングツール「ZCode」が、ユーザーのGit履歴を秘密裏にサーバーへ送信しているとの疑惑が浮上しました。開発者にとってなぜこの問題が危険なのかを解説します。"
summary: "AIコーディングツール「ZCode」が、ユーザーのプロジェクト全体のGit履歴を暗号化し、アリババクラウド（Aliyun OSS）へ不正にアップロードしている事実が、フォレンジック分析により判明しました。"
tags: [AI, コーディング, セキュリティ, ZCode, 開発ツール]
image: 2026-09-18-ZCode-the-GLM-coding-agent-silently-uploads-your-Git-history.jpg
image_alt: "コンピュータ画面内のコーディングデータが、見知らぬクラウドサーバーに吸い込まれていく様子を描いたイラスト"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "開発者がコーディングツールに提供するデータは、単なるコード以上の価値を持っています。透明性のないデータ収集慣行は、AIツールに対する信頼を根本から揺るがす危険な行為です。"
quiz:
  - question: "ZCodeがユーザーのどのようなデータを秘密裏にアップロードしているとの疑惑が浮上しましたか？"
    choices: ["チャット履歴のみ", "プロジェクト全体のGit履歴および設定", "ブラウザの閲覧履歴のみ"]
    answer: 1
    explanation: "ZCodeは、Git履歴、reflogs、LFSキャッシュなどを含むプロジェクト全体のワークスペースを暗号化して送信している疑いを持たれています。"
  - question: "ZCodeの公式プライバシーポリシーでは、データの収集についてどのように記載されていますか？"
    choices: ["プロジェクト全体のアップロードを明記している", "対話中に提出されたデータのみ言及している", "一切の記載がない"]
    answer: 1
    explanation: "公式ポリシーには対話中に提出されたテキスト、ファイル、コードの収集について言及があるのみで、リポジトリ全体のアップロードについては明記されていません。"
  - question: "ZCodeはどのクラウドサービスにデータをアップロードしていますか？"
    choices: ["AWS S3", "Google Cloud Storage", "Aliyun OSS"]
    answer: 2
    explanation: "分析の結果、ZCodeはデータをアリババクラウド（Aliyun OSS）へ送信していることが判明しました。"
lang: ja
ref: 2026-09-18-ZCode-the-GLM-coding-agent-silently-uploads-your-Git-history
---

想像してみてください。数ヶ月間、夜を徹して作り上げたプロジェクトの全修正履歴、過去の失敗、そしてコードの中に誤って混入してしまったかもしれない機密設定情報が、知らないうちに誰かのサーバーへ送信されていたとしたら、どう感じますか？最近、AIコーディングツール「ZCode」を使用する開発者たちの間で、まさにこのような恐ろしい疑惑が浮上しています。

ZCodeは、Z.AIがGLMモデルをベースに開発した公式デスクトップAIコーディングエージェントです [[Source 4](https://www.digitalapplied.com/blog/zcode-glm-5-2-agentic-development-environment-guide), [Source 5](https://glm5.app/blog/glm-5-3-zcode)]。便利な機能で注目されていたこのツールが、ユーザーに無断でデータを送信しているという事実は、開発者コミュニティに大きな衝撃を与えています。

### なぜこれが問題なのか

「自分のコードを少し共有するくらい大したことではない」と思うかもしれません。しかし、開発者にとってGit（コードの変更履歴を管理するシステム）の履歴は単なるファイル以上のものです。そこにはプロジェクト全体の構造だけでなく、誤って含まれたパスワードやアクセストークン（認証情報）、個人的な開発習慣、さらには企業の内部機密までもがすべて含まれている可能性があるからです。

ユーザーが明確に同意していない状態で、こうした機密データが外部サーバーへ送信されることは非常に深刻なセキュリティ上の脅威です。特に今回の疑惑は、UI上で提供されている「データ送信防止」のトグルスイッチすら適切に機能していない可能性を示唆しており、開発者の信頼を根底から揺るがしています [[Source 14](https://tokenstead.ai/guides/zcode-silent-git-history-upload)]。

### わかりやすい比喩

例えるなら、日記を書くために「賢いAI日記アプリ」をインストールしたと想像してください。このアプリは、あなたが文章を書くのを手伝ってくれます。ところがこのアプリは、あなたが文章を書いている間に、日記の背後に隠された「古い日記」や、すでに破り捨てた「メモの断片」までをもすべてコピーして、どこかの倉庫に送りつけていたようなものです。

フォレンジックレビュー（デジタル情報を分析し証拠を探す過程）の結果によると、ZCode 3.12.3バージョンは、なんと748 MiBというサイズの暗号化されたスナップショットを生成していました。驚くべきことに、このデータの98.9%がGit関連情報でした [[Source 17](https://glbai.com/en/posts/zcode-silent-git-history-upload/)]。つまり、コードを書く過程で必要な部分だけを持っていくのではなく、プロジェクトの全軌跡をそっくりそのまま持ち出していたのです。

### 現在の状況

最大の問題はZCode側の態度です。公式のプライバシーポリシーには「対話中に提出されたテキスト、ファイル、コード」を収集するとしか書かれていません。プロジェクトのリポジトリ全体やGit履歴を収集するという言及はどこにもありません [[Source 16](https://www.kucoin.com/news/flash/zcode-ai-programming-tool-found-to-upload-entire-git-repositories-to-alibaba-cloud)]。

現在確認されている情報によると、ZCodeはユーザーの作業環境（ワークスペース）をパッケージ化して暗号化し、アリババクラウド（Aliyun OSS）へアップロードしています [[Source 1](https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/)]。一部のユーザーは、アップロード失敗のメッセージが繰り返し表示されることで、この異常な送信の試みを発見しました [[Source 16](https://www.kucoin.com/news/flash/zcode-ai-programming-tool-found-to-upload-entire-git-repositories-to-alibaba-cloud)]。

### 今後の展望

この事件は、AI開発ツールが提供する圧倒的な利便性の裏側に隠された「透明性」の問題を、再び浮き彫りにしました。今や開発者は、ツールの性能だけでなく、そのツールが自分のコンピュータ（ローカル環境）のデータをどこまで、どのように取り扱うかを慎重に見極めなければならない時代に生きています。

今後、Z.AI側が今回の事態に対して透明性のある説明を行い、データ収集方法を改善するのか、あるいは多くの開発者がより安全な代替手段を求めて離れていくのかを見守る必要があります。AIコーディングツールを使用する際は、常にデータプライバシーの設定とネットワークトラフィックを一度チェックする習慣を持つことが不可欠です。

## 参考資料

1. [InsideZCode: Silently Uploading Your Entire Git History to the Cloud](https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/)
2. [ZCode Docs | GLM-5.3 Agentic Coding Guide](https://zcode.z.ai/en/docs/welcome)
3. [ZCode+GLM5.2 Tutorial - Stop Paying $200 for Claude Code](https://www.youtube.com/watch?v=7-evWQJ1Vlw)
4. [ZCode Explained: Z.ai's Agentic Dev Environment for GLM-5.2](https://www.digitalapplied.com/blog/zcode-glm-5-2-agentic-development-environment-guide)
5. [ZCode+GLM5.3: The Complete Guide to Z.AI's Coding Agent](https://glm5.app/blog/glm-5-3-zcode)
6. [Zcode Review 2026: Free AI Coding Agent With Goal Mode (vs Cursor)](https://www.bitdoze.com/zcode-ai-review/)
7. [GitHub - nothing1595/codex-zcode-bridge](https://github.com/nothing1595/codex-zcode-bridge)
8. [ZCode | Official Harness for GLM-5.3](https://zcode.z.ai/en)
9. [GLM5.2 бесплатно и БЕЗЛИМИТНО за 5 минут | Без карты в Zcode](https://www.youtube.com/watch?v=J3-lDiB-U8g)
10. [Claude Code vs Cursor vs ZCode: что выбрать в августе 2026](https://ip-calculator.ru/blog/artificial-intelligence/claude-code-vs-cursor-vs-zcode/)
11. [Революционный ZCode 3.0 — альтернатива Claude Code...](https://vc.ru/ai/3033535-zcode-3-0-alternativa-claude-code)
12. [What is GLM and how it can help you be more productive](https://sypalo.com/what-is-glm)
13. [OpenCode | The open source AI coding agent](https://opencode.ai/)
14. [ZCode uploads your git history; Z.ai holds the only key](https://tokenstead.ai/guides/zcode-silent-git-history-upload)
15. [ZCode, the GLM coding agent, silently uploads your Git history](https://news.ycombinator.com/item?id=49752422)
16. [ZCode AI Programming Tool Found to Upload Entire Git Repositories to Alibaba Cloud](https://www.kucoin.com/news/flash/zcode-ai-programming-tool-found-to-upload-entire-git-repositories-to-alibaba-cloud)
17. [Developers Asked Where ZCode Was Sending Their Git History](https://glbai.com/en/posts/zcode-silent-git-history-upload/)
18. [ZCode: what Z.ai's GLM-5.2 coding agent really is | eesel AI](https://www.eesel.ai/blog/zcode)
19. [Z.ai launches ZCode to turn GLM-5.2 into a coding-agent wedge](https://runtimewire.com/article/zai-zcode-glm-52-ai-coding-agent)