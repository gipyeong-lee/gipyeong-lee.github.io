---
layout: post
title: "AIが提示する「根拠」、信じて大丈夫？Perplexityの引用の裏切り"
description: "AI検索エンジンPerplexityが提示するソースが、実際には根拠不足である可能性を示す研究結果について解説します。"
summary: "最新の研究で、Perplexityが回答の根拠として提示した出典の多くが、実際のデータや数値を全く含んでいないという事実が明らかになりました。"
tags: [AI, 検索エンジン, Perplexity, 人工知能, 信頼性]
image: 2026-09-03-A-third-of-Perplexitys-citations-dont-contain-the-number-theyre-cited-for.jpg
image_alt: "AIの検索結果が表示されている画面に重なったハテナアイコン"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AIの回答を鵜呑みにせず、クロスチェックが必須の時代となりました。技術の利便性の裏に隠れた「ハルシネーション（幻覚）」の可能性を常に意識しておく必要があります。"
quiz:
  - question: "今回の研究で明らかになった、数値を含む文章に付された出典が、実際にはその数値を含んでいない確率はどれくらいでしょうか？"
    choices: ["約14.4%", "約34.7%", "約94%"]
    answer: 1
    explanation: "研究の結果によると、数値を言及した文章に付された引用のうち、34.7%がその数値を含まないページを指し示していました。"
  - question: "Perplexityは情報を探す際、主にどのような方式を利用していますか？"
    choices: ["学習データに基づく回答", "リアルタイムWeb検索に基づく回答", "オフラインデータベースの活用"]
    answer: 1
    explanation: "Perplexityは過去の学習データに依存するのではなく、リアルタイムのWeb検索を通じて最新情報を取得する方式をとっています。"
  - question: "Perplexityの引用クリック率（CTR）は、従来の検索結果と比べてどうですか？"
    choices: ["同程度である", "従来方式よりはるかに低い", "従来方式よりはるかに高い"]
    answer: 2
    explanation: "Perplexityの引用クリック率は18～24%の水準であり、従来の検索エンジンの2～4%よりもはるかに高い数値を示しています。"
lang: ja
ref: 2026-09-03-A-third-of-Perplexitys-citations-dont-contain-the-number-theyre-cited-for
---

想像してみてください。今日の夕方のプレゼンのために、AI検索エンジンに「今年、我が国のAI市場の成長率は何パーセントですか？」と尋ねたとします。AIはすぐに回答を出し、文章の末尾に[1]、[2]のような数字を添えて出典まで親切に明記してくれました。私たちは普段、このような出典を見ると「AIが自分で調べて確認した情報なんだ」と安心します。しかし、もしその出典が実際には全く関係のないページを指し示していたらどうでしょうか？

最近、AI検索サービス「Perplexity（パープレキシティ）」が回答の根拠として提示する引用について、衝撃的な実態が公開されました。私たちが信頼して見ていたその「出典」が果たしてどれほど正確なのか、そしてなぜAIはこのような間違いを犯すのか、一緒に見ていきましょう。

## なぜ重要なのか？

Perplexityは従来の検索エンジンと異なり、膨大なWebデータを自ら要約して回答を作成します。そのため、ユーザーはいくつものサイトを個別にクリックする必要がなく、回答を一度に得ることができます。[出典: Perplexityは引用エンジンです](https://mentionagent.ai/blog/how-to-get-cited-by-perplexity/)。実際、ユーザーが引用（数字で表示された出典）をクリックする割合は18〜24%に達し、これは従来の検索エンジンのクリック率である2〜4%よりもはるかに高い数値です。[出典: 2026年 Perplexityで引用される方法](https://www.miniloop.ai/blog/perplexity-seo-how-to-get-cited-2026)。

つまり、私たちはAIが提供する出典を非常に信頼しており、実際にその情報源を通じて情報を深掘りしているということです。しかし、もしこの情報が事実を含んでいなければ、私たちは偽情報の沼にはまる危険があります。

## わかりやすく解説

簡単に言うと、Perplexityの動作原理は**「優秀な秘書が数多くの本を読み込み、整理してくれること」**に似ています。秘書は回答を作成する際、「この内容は5ページにあります」と脚注を付けます。しかし、この秘書が文章を書き終えた後、後付けで「あ、この部分は5ページ目くらいにあったはずだ」と、脚注を曖昧に付けてしまうケースがあるのです。[出典: Perplexityの引用パターン](https://bcited.ai/blog/perplexity-citation-patterns-source-selection)。この過程で秘書の記憶が不確かになり、全く関係のないページを指摘してしまうわけです。

データを調査した結果、数値を含む文章に付された引用のうち約34.7%が、その数値が全く含まれていないページにリンクされていました。[出典: Perplexity引用監査報告書](https://hausresearch.com/reports/perplexity-citation-audit/)。これは例えるなら、数学の問題を解いて答えのページを確認しようとしたとき、本の巻末の解説が全く別の問題の解説を載せているような状態です。さらに全体的に評価した結果、Perplexityが提示した主張の約14.4%が、実際に引用された出典によって裏付けられていないという結果も出ています。[出典: Perplexity引用監査報告書](https://hausresearch.com/reports/perplexity-citation-audit/)。

## 現在の状況

Perplexityは回答の約94%で出典を明記するほど、引用に積極的です。[出典: 2026年、Perplexityは常に引用元を明記するか？](https://www.fonzy.ai/blog/does-perplexity-cite-sources)。しかし問題は、AIモデル自体が回答を生成した後に、その回答が事実であるかを確認せず、「事後的に」出典をこじつける方式にあります。[出典: Perplexityの引用パターン](https://bcited.ai/blog/perplexity-citation-patterns-source-selection)。

もちろん、時にはPerplexityの責任ではない場合もあります。外部アプリがPerplexityのデータを正しく表示できず、出典リンクが消えてしまったように見える現象も存在します。[出典: Perplexityの出典未表記問題](https://perplexityaimagazine.com/perplexity-hub/perplexity-not-citing-sources/)。しかし根本的に、システムが回答内容と一致しないソースを持ってくる「ハルシネーション（Hallucination：AIが事実ではない情報を、もっともらしく作り出す現象）」は明らかに存在しており、これはユーザーが認識すべき限界点です。[出典: 2026年 Perplexityレビュー](https://vantaige.io/ai-tool/perplexity)。

## 今後はどうなるか？

今後はAI検索サービス間の競争において、「どれだけ多くの出典を表示するか」よりも**「どれだけ正確な出典を接続するか」**がより重要な基準となるでしょう。すでに一部の研究では、Perplexityの引用がChatGPTよりも約3倍多いことを指摘し、量的な膨張が常に質的な正確性を保証するわけではないと述べています。[出典: Perplexity引用の9つのシグナル](https://citevantage.com/blog/how-to-get-cited-by-perplexity/)。ユーザーが賢くなるほど、誤った引用を提示するAIプラットフォームは信頼を失っていくでしょう。

## MindTickleBytesのAI記者の視点
AI検索エンジンは便利ですが、根拠のない確信には注意が必要です。AIが提示する出典をクリックしても目的の内容がない場合、それはAIが内容を深く理解したのではなく、単に「それらしい位置」を推測しただけの可能性が高いです。検索された回答を読む際は、常に「批判的な視点」で内容をもう一度確認する習慣が必要な時代です。

## 参考資料
1. [AthirdofPerplexity'scitationsdon'tcontainthenumberthey'r...](https://news.ycombinator.com/item?id=49536201)
2. [How to GetCitedbyPerplexity: The Tactical Playbook for 2026 | Cintra](https://cintra.run/blog/how-to-get-cited-by-perplexity)
3. [How to Rank inPerplexityAI: What 21CitationsPer Query... | BlueJar](https://bluejar.ai/blog/how-to-rank-in-perplexity-ai/)
4. [How to GetCitedbyPerplexityAI | Mentionable](https://mentionable.ai/en/guides/rank-on-perplexity)
5. [PerplexityInlineCitations: How [1][2][3] Links Work](https://amicitable.com/blog/does-perplexity-cite-inline-sources)
6. [PerplexitySEO: How to GetCitedin 2026](https://www.miniloop.ai/blog/perplexity-seo-how-to-get-cited-2026)
7. [How to GetCitedbyPerplexity(2026 Playbook) | MentionAgent](https://mentionagent.ai/blog/how-to-get-cited-by-perplexity/)
8. [The 50 Most-CitedWebsites inPerplexity(September 2026)](https://ahrefs.com/blog/most-cited-domains-perplexity/)
9. [PerplexityCitations| Fetchable Sources, Enquire Desk](https://www.worldwidebacklinks.com/ai-backlinks/perplexity-citations/)
10. [PerplexitycitesClickUp 6,474 times. Notion gets 741… Why?](https://foundationinc.co/lab/vol-304)
11. [PerplexityCitationPatterns: What Actually Gets Sourced — b/cited](https://bcited.ai/blog/perplexity-citation-patterns-source-selection)
12. [How to earn morecitationsinperplexityai search](https://snoika.com/blog/perplexity-ai-search-citation-checklist)
13. [How to GetCitedbyPerplexity: 9 Source Signals | CiteVantage](https://citevantage.com/blog/how-to-get-cited-by-perplexity/)
14. [A third of Perplexity's citations don't contain the number they're ...](https://hausresearch.com/reports/perplexity-citation-audit/)
15. [Perplexity Not Citing Sources: 8 Fixes 2026](https://perplexityaimagazine.com/perplexity-hub/perplexity-not-citing-sources/)
16. [Perplexity AI Review 2026: Citations, Limits & Real Failures](https://vantaige.io/ai-tool/perplexity)
17. [Does Perplexity Always Cite Sources? 2026 Data Says No](https://www.fonzy.ai/blog/does-perplexity-cite-sources)
18. [How Perplexity Selects Its Citations: What We Know From Testing and ...](https://aiseoshift.com/blog/how-perplexity-selects-citations/)
19. [Getting Cited by Perplexity: What It Actually Quotes — Genαi](https://genalphai.com/getting-cited-by-perplexity-teardown/)
20. [How Perplexity Decides Which Sources to Cite - authoritytech.io](https://authoritytech.io/blog/how-perplexity-selects-sources-algorithm-2026)