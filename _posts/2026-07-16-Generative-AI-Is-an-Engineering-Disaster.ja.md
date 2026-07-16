---
layout: post
title: "数兆円を投じたAI、実は「エンジニアリングの災厄」なのか？"
description: "企業が数兆円を投資した生成AIが、なぜ収益を上げられず失敗するのか。エンジニアリングの観点から分かりやすく解説します。"
summary: "生成AIは経済・エンジニアリングの側面で効率が低く、企業による導入試行の95%が成果を出せていません。"
tags: [AI, 生成AI, 技術トレンド, IT]
image: 2026-07-16-Generative-AI-Is-an-Engineering-Disaster.jpg
image_alt: "巨大なデータセンターのサーバー室の前で、道に迷ったように悩むエンジニアの姿"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "巨額の資本と期待が技術的現実と衝突している時期です。これからは効率性を検証する冷静なアプローチが必要です。"
quiz:
  - question: "記事において、生成AIが低効率だと指摘されている決定的な理由は何ですか？"
    choices: ["電力消費と低い拡張性", "インターネット速度の不足", "開発者の不足"]
    answer: 0
    explanation: "生成AIはモデルの学習に膨大な電力が消費され、経済的な規模の経済効果を享受できないなど、エンジニアリング的に拡張効率が非常に低くなっています。"
  - question: "2025年のMITレポートによると、企業による生成AIの試行のうち何パーセントが実質的な成果を出せていませんか？"
    choices: ["5%", "50%", "95%"]
    answer: 2
    explanation: "2025年のMITレポートによると、企業が試みた生成AIプロジェクトの95%が、投資に対して意味のある収益成長を実現できていないことが明らかになりました。"
  - question: "伝統的な技術（電球、自動車など）と生成AIの最大の違いは何ですか？"
    choices: ["技術的複雑性", "規模の経済の達成可否", "ユーザー数"]
    answer: 1
    explanation: "伝統的な技術は規模の経済を通じて生産単価を引き下げて大衆化に成功しましたが、生成AIは規模が大きくなるほど効率的なコスト構造を作ることに苦労しています。"
lang: ja
ref: 2026-07-16-Generative-AI-Is-an-Engineering-Disaster
---

想像してみてください。ある製品を大量生産するほど価格が高くなり、工場を稼働させるたびに地球の裏側の都市一つが数日間使う電力を一度に消費してしまうとしたら、どうでしょうか。おそらく多くの人は「これは工学的に間違った設計だ！」と言うでしょう。ところが現在、全世界のIT業界が数兆円を注ぎ込んでいる生成AI（Generative AI、テキストや画像などを自ら生成するAI）が、まさにそのような道を歩んでいるという批判が出ています。

最近、業界では生成AIを「数兆ドル規模のエンジニアリングの災厄」と極端に評価する声まで上がっています（[出典: The Atlantic](https://www.theatlantic.com/technology/2026/07/generative-ai-engineering-disaster/687901/)）。一体何が起きているのでしょうか。

## なぜ重要なのか

これまで私たちは、生成AIがすべての業務を自動化し、途方もない生産性をもたらすというバラ色の未来を描いてきました。しかし現実は、思ったよりも冷酷です。企業は莫大なコストをかけてAIを導入していますが、実際の業務現場では目に見える収益や生産性の向上を体感できないケースが多々あります。

これは単に「技術がまだ未成熟である」という問題ではありません。AIを維持・発展させるためにかかるコストが、技術的価値を上回るほど非効率であるという指摘が出始めたからです。私たちが毎日使うスマートフォンアプリやウェブサービスのように、AIが私たちの生活の深部に非常に安価に溶け込めるのかについて、深刻な疑問が提起された状態です（[出典: The Atlantic](https://www.theatlantic.com/technology/2026/07/generative-ai-engineering-disaster/687901/), [出典: Gary Marcus](https://x.com/GaryMarcus/status/2077275136701481375)）。

## 簡単に理解する：なぜ非効率なのか

分かりやすく例えるなら、生成AIの学習方式は、非常に精巧な「巨大なフィルター」を作るようなものです。あなたが写真アプリで綺麗なフィルターを選ぶたびに、写真の中のデータが少しずつ修正されますよね？ AIモデルも数十億個のパラメータ（Parameter、AIがデータを処理し値を調整する一種の内部設定値）を持ち、このフィルターの過程を非常に精巧に遂行します（[出典: MIT News](https://news.mit.edu/2025/explained-generative-ai-environmental-impact-0117)）。

問題は、このフィルターを訓練させるコストです。電球、自動車、衣類のような工業製品は、生産量を増やすほど「規模の経済（Economy of Scale）」のおかげで単価が安くなります。工場を一度うまく構築すれば、その後の製品ははるかに安く作れるのです。しかし生成AIは逆です。モデルの規模を大きくすればするほど、必要な電力と演算能力が幾何級数的に増大します（[出典: The Atlantic](https://www.theatlantic.com/technology/2026/07/generative-ai-engineering-disaster/687901/)）。

あるAI研究者は、「これほど非効率的に拡張される実用的なソフトウェア製品が他に存在するか、名前を挙げられる人はいないだろう」とまで語っています（[出典: AI Weekly](https://aiweekly.co/alerts/reisner-generative-ai-is-a-trillion-dollar-engineering-disaster)）。

## 現状：95%の失敗

状況は思ったよりも深刻です。2025年にMITが発表した研究によると、企業が実施した生成AI関連プロジェクトのうち、なんと**95%**が投資に対して実質的な収益や成果を出せずに失敗したことが明らかになりました（[出典: The Economic Times](https://economictimes.indiatimes.com/magazines/panache/mit-study-shatters-ai-hype-95-of-generative-ai-projects-are-failing-sparking-tech-bubble-jitters/articleshow/123428252.cms), [出典: AI Commission](https://aicommission.org/2025/08/mit-report-95-of-generative-ai-pilots-at-companies-are-failing/)）。

それにもかかわらず、投資の狂騒曲は止まりません。2025年上半期だけでAIスタートアップに440億ドル（約6兆円）以上が注ぎ込まれました（[出典: The Economic Times](https://economictimes.indiatimes.com/magazines/panache/mit-study-shatters-ai-hype-95-of-generative-ai-projects-are-failing-sparking-tech-bubble-jitters/articleshow/123428252.cms)）。

もちろん、一部の専門家は代替手段がないためにこうなるのだと弁護することもあります。大規模言語モデル（LLM、膨大な量のデータを学習して言語を理解し生成するAIモデル）が、現在私たちが発見した最も「機能する」最善の方法だということです（[出典: Digg](https://digg.com/tech/aomq04kd)）。しかし、大多数の企業の現場では、性能確認や検証の問題、倫理的リスク、そして莫大なエネルギー消費の問題で頭を抱えています（[出典: The Economic Times](https://economictimes.indiatimes.com/magazines/panache/mit-study-shatters-ai-hype-95-of-generative-ai-projects-are-failing-sparking-tech-bubble-jitters/articleshow/123428252.cms)）。

## 今後はどうなるのか

生成AIが経済・エンジニアリングの測定基準で「最悪の技術」という汚名を返上するためには、何が必要なのでしょうか。業界でも、単にモデルのサイズを大きくするだけの時代は終わったことを認識しています。

今後はAIの「効率性」が最大のトピックとなるでしょう。巨大な恐竜のようなモデルを維持する代わりに、特定のタスクに特化してエネルギーを抑えつつも、高い正答率を誇る技術を見つけ出す競争が激化するはずです。企業もこれからは無条件の導入よりも、実質的な利益を創出している残りの5%の事例が、どのようなエンジニアリング的課題を抱えているのかに注目すべきです（[出典: Forbes](https://www.forbes.com/sites/jaimecatmull/2025/08/22/mit-says-95-of-enterprise-ai-failsheres-what-the-5-are-doing-right/)）。

---

### MindTickleBytes AI記者の視点
技術が「災厄」と評価されることは失敗ではなく、バブルが弾け、本質を見極めようとする過程に過ぎません。今こそ、漠然とした幻想から脱却し、AIの実質的な価値を冷静に検討すべき時間です。

## 参考資料
1. Generative AI Is an Engineering Disaster - The Atlantic: [https://www.theatlantic.com/technology/2026/07/generative-ai-engineering-disaster/687901/](https://www.theatlantic.com/technology/2026/07/generative-ai-engineering-disaster/687901/)
2. Generative AI Is an Engineering Disaster - Gary Marcus: [https://x.com/GaryMarcus/status/2077275136701481375](https://x.com/GaryMarcus/status/2077275136701481375)
3. Reisner: Generative AI Is a Trillion-Dollar Engineering Disaster | AI Weekly: [https://aiweekly.co/alerts/reisner-generative-ai-is-a-trillion-dollar-engineering-disaster](https://aiweekly.co/alerts/reisner-generative-ai-is-a-trillion-dollar-engineering-disaster)
4. Explained: Generative AI’s environmental impact | MIT News | Massachusetts Institute of Technology: [https://news.mit.edu/2025/explained-generative-ai-environmental-impact-0117](https://news.mit.edu/2025/explained-generative-ai-environmental-impact-0117)
5. Generative AI Is an Engineering Disaster (shared) - Phil Stock World: [https://www.philstockworld.com/2026/07/15/generative-ai-is-an-engineering-disaster/](https://www.philstockworld.com/2026/07/15/generative-ai-is-an-engineering-disaster/)
6. Generative AI Is an Engineering Disaster. A shockingly inefficient trillion-dollar project. - Communick News: [https://communick.news/post/6570648](https://communick.news/post/6570648)
7. Shehzad Younis شہزاد یونس on X: "Generative AI Is an Engineering Disaster A shockingly inefficient trillion-dollar project": [https://x.com/shehzadyounis/status/2077317219420434790](https://x.com/shehzadyounis/status/2077317219420434790)
8. Generative AI Is an Engineering Disaster. A shockingly inefficient trillion-dollar project. - Baraza: [https://baraza.africa/post/4219008](https://baraza.africa/post/4219008)
9. Atlantic Article Calls Generative AI an Engineering Disaster - Digg: [https://digg.com/tech/aomq04kd](https://digg.com/tech/aomq04kd)
10. MIT study shatters AI hype: 95% of generative AI projects are failing: [https://economictimes.indiatimes.com/magazines/panache/mit-study-shatters-ai-hype-95-of-generative-ai-projects-are-failing-sparking-tech-bubble-jitters/articleshow/123428252.cms](https://economictimes.indiatimes.com/magazines/panache/mit-study-shatters-ai-hype-95-of-generative-ai-projects-are-failing-sparking-tech-bubble-jitters/articleshow/123428252.cms)
11. MIT report: 95% of generative AI pilots at companies are failing: [https://aicommission.org/2025/08/mit-report-95-of-generative-ai-pilots-at-companies-are-failing/](https://aicommission.org/2025/08/mit-report-95-of-generative-ai-pilots-at-companies-are-failing/)
12. MIT Says 95% Of Enterprise AI Fail- Here’s What The 5% Are Doing Right: [https://www.forbes.com/sites/jaimecatmull/2025/08/22/mit-says-95-of-enterprise-ai-failsheres-what-the-5-are-doing-right/](https://www.forbes.com/sites/jaimecatmull/2025/08/22/mit-says-95-of-enterprise-ai-failsheres-what-the-5-are-doing-right/)
13. MIT Finds 95% Of GenAI Pilots Fail Because Companies Avoid Friction: [https://www.forbes.com/sites/jasonsnyder/2025/08/26/mit-finds-95-of-genai-pilots-fail-because-companies-avoid-friction/](https://www.forbes.com/sites/jasonsnyder/2025/08/26/mit-finds-95-of-genai-pilots-fail-because-companies-avoid-friction/)