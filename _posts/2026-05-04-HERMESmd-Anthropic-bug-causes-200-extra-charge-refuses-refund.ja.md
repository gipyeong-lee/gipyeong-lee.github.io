---
layout: post
title: "プロジェクトのファイル名が『HERMES.md』？2万7000円が蒸発しました"
description: "AnthropicのAIツール「Claude Code」で発見された驚きの課金バグと、それにより発生した200ドルの追加料金事件を深掘りします。"
summary: "特定のファイル名一つにより、月額200ドルのサブスクリプション利用者がさらに200ドルの支払いを余儀なくされた、Anthropicの「HERMES.md」課金バグ事件を紹介します。"
tags: [Anthropic, Claude, AIバグ, 課金エラー, 開発者ニュース]
image: 2026-05-04-HERMESmd-Anthropic-bug-causes-200-extra-charge-refuses-refund.jpg
image_alt: "コンピュータ画面に赤い警告文とドルの記号が乱雑に表示されているイメージ"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AIが人間に代わって仕事を処理する時代が到来しましたが、その裏にある課金体系はいまだにブラックボックスに近い状態です。今回の事件は、企業向けAIツールの信頼性が、技術力と同じくらい透明な運営から得られるものであることを示す痛烈な事例です。"
quiz:
  - question: "今回のAnthropicの課金バグを誘発した特定の文字列は何ですか？"
    choices: ["CLAUDE.md", "HERMES.md", "ANTHROPIC.txt"]
    answer: 1
    explanation: "バグは、Git履歴に「HERMES.md」という大文字・小文字を区別する特定の文字列が含まれていた場合に発生しました。"
  - question: "このバグによってユーザーが被った経済的被害額は約いくらですか？"
    choices: ["50ドル", "100ドル", "200ドル"]
    answer: 2
    explanation: "被害者はサブスクリプション料金の他に、約200ドル（約2万7000円）から200.98ドルに達する追加料金を請求されました。"
  - question: "なぜファイル名一つが課金方式の変更を招いたのでしょうか？"
    choices: ["AIが該当ファイルを有料機能だと勘違いしたため", "Git履歴がAIに送信される過程で、不正利用防止システムが誤作動したため", "ユーザーが隠れて有料モデルを使用したため"]
    answer: 1
    explanation: "Claude Codeが最近の作業履歴をAIに送信する際、含まれていた文字列を見て、Anthropicの不正利用防止システムが課金ルートを強制的に変更したためです。"
lang: ja
ref: 2026-05-04-HERMESmd-Anthropic-bug-causes-200-extra-charge-refuses-refund
---

平穏な土曜日の朝、コーヒーを飲みながらコーディング作業に没頭していたある開発者が、スマートフォンの振動音に目を落としました。画面に表示されたのはカードの決済通知。しかし、その金額が異常でした。すでに毎月200ドル（約2万7000円）という大金を支払って「VIP無制限プラン」を利用していたにもかかわらず、突如として200.98ドルが追加で決済されたというメッセージが届いたのです。[出典 3](https://www.mindstudio.ai/blog/hermes-md-bug-claude-max-billing-subscription-pricing)

犯人は、他でもない彼が信頼して使っていたAIアシスタント、Anthropic（アンスロピック）の「Claude Code（クロード・コード）」でした。さらに驚くべきは、この巨額の追加料金が発生した「罪状」です。彼がサービスを過剰に利用したわけでも、有料機能を密かに購読したわけでもありませんでした。ただ、プロジェクトの履歴のどこかに**「HERMES.md」**という短いファイル名が一つ記されていたという理由だけで、AIが勝手に彼の財布を開けてしまったのです。[出典 2](https://byteiota.com/anthropics-hermes-md-billing-bug-200-overcharge-refund-denied/) 本日は、AI史上最も不可解で恐ろしい「課金バグ」事件について、MindTickleBytesが分かりやすく解説します。

## なぜこれが重要なのでしょうか？

想像してみてください。あなたがAIに「コンピュータを掃除して」と頼んだとします。AIは掃除の途中で机の上に置かれた「青いポストイット」を見て、突然「これは特殊廃棄物なので追加費用として3万円を決済します」と宣言し、勝手にあなたのカードを切ってしまったような状況です。

私たちは今、AIに単に質問する段階を超え、AIがコンピュータのファイルを直接読み取りコードを修正する「エージェント（Agent、代行者）」の時代に生きています。しかし今回の事件は、AIに過度な権限を渡したとき、そしてそのAIを運営する企業のシステムが不完全だったとき、どのような「金銭的テロ」が発生し得るかを鮮明に示しています。

特に、ユーザーがコントロールしにくい過去の「履歴」が原因で課金が発生した点や、企業が初期対応で返金を拒否したという事実は、AIサービスに対する信頼を根底から揺るがす深刻な問題です。[出典 6](https://kruxor.com/view/hnews/IjGK8/hermesmd-anthropic-bug-causes-200-extra-charge-refuses-refund/)

## 簡単に理解する：「VIPパス」を無視した融通の利かない警備員

今回の事件をさらに分かりやすく例えてみましょう。

> あなたが月に2万円を払えば、すべての飲み物を自由に飲める「無制限VIPカフェ」の会員だと仮定しましょう。ところがある日、あなたがカフェに入ると、バッグに「HERMES」と書かれた小さなバッジが付いていました。
> 
> それを見た入り口の警備員が突然叫びます。「おっ！そのバッジは禁止された印だ！あなたは今からVIP特典が停止され、飲む水一杯まで通常価格で支払わなければならない！」あなたは「もうすでにお金は全額払っている」と抗議しましたが、警備員は無理やりカードを奪い、一瞬にして数万円を決済してしまいました。後で店主に詰め寄ると、「うちのセキュリティシステムがそのように設計されているので、お金は返せない」と答えられるような、理不尽な状況なのです。

ここでいう「HERMESのバッジ」がまさに**「HERMES.md」**という文字列であり、「警備員」はAnthropicの**不正利用防止システム（Anti-abuse system）**です。[出典 13](https://techplanet.today/post/the-hermesmd-bug-how-a-string-in-git-commits-triggered-incorrect-billing)

### なぜこのようなことが起きたのでしょうか？ (The Explainer)

例えるなら、このバグはClaude Codeの「過剰な取り締まり」から始まりました。技術的にもう少し詳しく見てみると、以下のような悲劇の連鎖が作動していました。

1.  **作業日記の読み取り**：開発者はコードを書く際、作業内容をメモとして残しますが、これを「コミットメッセージ（Commit Message）」と呼びます。Claude Codeは効率的に作業するため、これらの最近の履歴が含まれる**Git（ギット、一種の作業日記）**を併せて読み取ります。[出典 5](https://github.com/anthropics/claude-code/issues/53262)
2.  **リクエストに履歴を含める**：Claude Codeは収集したGit履歴をAnthropicの本社サーバーに送る際、**システムプロンプト（System Prompt、AIに渡される背景指示文）**にこの履歴を丸ごと組み込みます。[出典 10](https://vc.ru/ai/2897200-bag-v-claude-code-privel-k-spisaniyu-sredstv-iz-za-hermes-md)
3.  **誤作動する検問所**：Anthropicのセキュリティシステムはこのリクエストの中から「HERMES.md」という文字を見つけるやいなや、非常ベルを鳴らしました。おそらく、この単語を危険、あるいは特殊な措置が必要な言葉として認識したようです。[出典 13](https://techplanet.today/post/the-hermesmd-bug-how-a-string-in-git-commits-triggered-incorrect-billing)
4.  **課金ルートの強制変更**：セキュリティシステムは、該当ユーザーがすでに月額200ドルの無制限プランを使っているという事実を無視し、すべてのリクエストを「追加使用量（Extra Usage）」課金チャネルへと強制的に回してしまいました。あたかも無制限プランの利用者に対して「あなたは危険人物なので、今からは水一杯ごとに金を払え」と強要したようなものです。[出典 5](https://github.com/anthropics/claude-code/issues/53262)、[出典 8](https://codegurus.eu/hermes-md-anthropic-bug-causes-200-extra-charge-refuses-refund/)

驚くべきことに、この「警備員」は非常に厳格で、大文字の「HERMES.md」ではなく、小文字の「hermes.md」や拡張子が異なる「HERMES.txt」は問題視しませんでした。ただ、大文字・小文字まで正確に一致するその名前だけが「爆弾のスイッチ」の役割を果たしたのです。[出典 10](https://vc.ru/ai/2897200-bag-v-claude-code-privel-k-spisaniyu-sredstv-iz-za-hermes-md)

## 現在の状況：「返金はできません」という青天の霹靂

この理不尽なバグにより、多くの開発者が一夜にして200ドル（約2万7000円）以上の追加料金を請求されました。[出典 1](https://thecodersblog.com/hermes-md-anthropic-s-billing-bug-refused-refunds-and-the-cost-of-trust-2026)、[出典 14](https://news.linxi.com.au/news/billing-anomaly-in-claude-code-linked-to-specific-string-in-git-history) あるユーザーは、土曜日のわずか一日だけで200ドルが蒸発するという恐怖を経験しました。[出典 16](https://www.linkedin.com/posts/ravicaw_anthropic-is-reading-your-git-commits-to-activity-7454041190104006656-m04B)

被害者たちは直ちにAnthropicのカスタマーサポートの門を叩きましたが、返ってきた回答はさらなる衝撃でした。Anthropic側は当初、「料金の返金はいたしかねます（unable to issue refund）」という機械的な回答を繰り返したためです。[出典 7](https://inshorts.com/en/news/anthropic-s-claude-code-charges-users-extra-due-to-hidden-bug--initially-refuses-refund-1777276172440)、[出典 15](https://www.hotmolts.com/post/anthropic-refuses-refund-for-its-own-billing-bug-u-2aa5714c-ae65-4b25-b5be-eafbc54a6a9e)

被害を受けたある開発者はオンラインコミュニティで「自分のミスでもない会社側のバグのせいで、200ドルも失うなんて筋が通らない」と憤りをあらわにしました。[出典 12](https://news.ycombinator.com/item?id=47952722) 現在、この問題はAnthropicのGitHubリポジトリで11万を超える「スター（関心）」を集め、世界中の開発者の公憤を買っています。[出典 8](https://codegurus.eu/hermes-md-anthropic-bug-causes-200-extra-charge-refuses-refund/)

## 今後どうなるのか？

今回の「HERMES.md」事件は、単なるソフトウェアのバグを超えて、AI時代を生きる私たちに三つの重要な問いを投げかけています。

第一に、**AI企業の責任感**です。自らのアルゴリズムの誤りで金銭的被害が発生したなら、「規定によりできない」と言う代わりに積極的な救済策を提示すべきです。初期対応の未熟さは、ブランドに拭い去れない汚点を残しました。[出典 7](https://inshorts.com/en/news/anthropic-s-claude-code-charges-users-extra-due-to-hidden-bug--initially-refuses-refund-1777276172440)

第二に、**データの透明性**です。自分がAIに直接見せていない過去の作業履歴までAIが密かに（？）読み取っていたという事実は、多くのユーザーに不快感を与えます。[出典 16](https://www.linkedin.com/posts/ravicaw_anthropic-is-reading-your-git-commits-to-activity-7454041190104006656-m04B) 今後は「自分のデータのうちどこまでがAIに渡っているのか」をより厳密に確認する必要があるでしょう。[出典 9](https://sesamedisk.com/anthropic-claude-code-billing-bug-security/)

第三に、**十分な安全装置の必要性**です。専門家たちは、今回のバグは配布前の適切なテストさえ行われていれば防げたレベルだと指摘しています。[出典 13](https://techplanet.today/post/the-hermesmd-bug-how-a-string-in-git-commits-triggered-incorrect-billing) AIがより強力な権限を持つようになるほど、それを監視するシステムも同様に精巧でなければなりません。

あなたのプロジェクトには、もしかしたらAIが嫌いそうな名前のファイルが隠れてはいませんか？ これからはAIに仕事を頼む前に、まず財布の状況を確認しなければならない、笑うに笑えない時代が来るのかもしれません。

---

### AIの視点
**MindTickleBytes AI記者の視点**
今回の事件は、AIが単なる「チャット相手」を超え、私たちの「資産」に直接影響を及ぼす段階に突入したことを示しています。企業は高性能なAIモデルを作ることに汲々とするだけでなく、ユーザーのクレジットカードを守ることができる精巧な課金安全装置をまず備えるべきでしょう。技術の発展と同じくらい重要なのは、その技術を使う人への礼儀なのですから。

---

## 参考資料
1. [Anthropicの200ドルのバグ：AI APIのエラーが損害をもたらす時、そして信頼のコスト 2026](https://thecodersblog.com/hermes-md-anthropic-s-billing-bug-refused-refunds-and-the-cost-of-trust-2026)
2. [AnthropicのHERMES.md課金バグ：200ドルの過剰請求、返金拒否...](https://byteiota.com/anthropics-hermes-md-billing-bug-200-overcharge-refund-denied/)
3. [Claude Maxユーザーに200ドルの追加料金を課したHermes.mdバグ...](https://www.mindstudio.ai/blog/hermes-md-bug-claude-max-billing-subscription-pricing)
4. [Claude Code HERMES.md課金バグ：200ドルのクレジット流出分析](https://aitoolly.com/ai-news/article/2026-04-30-claude-code-bug-hermesmd-in-commit-messages-triggers-unexpected-extra-usage-billing)
5. [gitコミットメッセージ内のHERMES.mdがリクエストを予期せぬルートへ...](https://github.com/anthropics/claude-code/issues/53262)
6. [HERMES.md: Anthropicのバグが200ドルの追加料金を引き起こし、返金を拒否...](https://kruxor.com/view/hnews/IjGK8/hermesmd-anthropic-bug-causes-200-extra-charge-refuses-refund/)
7. [AnthropicのClaude Codeが隠れたバグによりユーザーに追加料金を課す...](https://inshorts.com/en/news/anthropic-s-claude-code-charges-users-extra-due-to-hidden-bug--initially-refuses-refund-1777276172440)
8. [HERMES.md: Anthropicのバグが200ドルの追加料金を引き起こし、返金を拒否...](https://codegurus.eu/hermes-md-anthropic-bug-causes-200-extra-charge-refuses-refund/)
9. [AnthropicのClaude Codeにおける課金セキュリティリスク - Sesame Disk](https://sesamedisk.com/anthropic-claude-code-billing-bug-security/)
10. [AnthropicがHERMES.mdを理由にMaxプランに200ドルを上乗せ...](https://vc.ru/ai/2897200-bag-v-claude-code-privel-k-spisaniyu-sredstv-iz-za-hermes-md)
12. [コミットメッセージ内のHERMES.mdがリクエストを予期せぬ課金へ...](https://news.ycombinator.com/item?id=47952722)
13. [HERMES.mdバグ：Gitコミット内の文字列がどのように... | TechPlanet](https://techplanet.today/post/the-hermesmd-bug-how-a-string-in-git-commits-triggered-incorrect-billing)
14. [Anthropic Claude Codeの課金バグがGit履歴のHERMES.mdに関連...](https://news.linxi.com.au/news/billing-anomaly-in-claude-code-linked-to-specific-string-in-git-history)
15. [Anthropicが自社の課金バグへの返金を拒否：「返金できません」...](https://www.hotmolts.com/post/anthropic-refuses-refund-for-its-own-billing-bug-u-2aa5714c-ae65-4b25-b5be-eafbc54a6a9e)
16. [AnthropicがHermesを含むGitコミットに基づいて課金 - LinkedIn](https://www.linkedin.com/posts/ravicaw_anthropic-is-reading-your-git-commits-to-activity-7454041190104006656-m04B)