---
layout: post
title: "AIのコーディング実力、試験問題から見直すべきか？OpenAIの決断"
description: "OpenAIがAIコーディング能力評価の標準として使われていた「SWE-Bench Pro」の推奨を中止しました。問題自体にエラーが発見され、AI性能評価の信頼性に赤信号が灯りました。"
summary: "OpenAIがAIのコーディング実力を測定する主要指標であったSWE-Bench Proにおいて約30%のエラーを発見し、推奨を中止しました。"
tags: [AI, コーディング, 開発, OpenAI, SWE-Bench]
image: 2026-07-09-OpenAI-no-longer-recommends-SWE-Bench-Pro.jpg
image_alt: "コードの断片とAIアイコンが絡み合う背景の上に、試験問題のエラーを象徴する警告マークが浮かんでいる様子。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI技術が急速に発展する中、それを測定する「試験」の精巧さがその速度に追いついていない状況です。開発者が自ら検証する時代が近づいています。"
quiz:
  - question: "OpenAIがSWE-Bench Proの推奨を中止した最大の理由は何ですか？"
    choices: ["AIの実力が良すぎるため", "公開された作業課題の約30%が誤って構成されていたため", "すでにすべてのAIが満点を取ったため"]
    answer: 1
    explanation: "OpenAIは、SWE-Bench Proの公開作業課題のうち約30%が正常に機能せず、信頼できない結果が出ていると明らかにしました。"
  - question: "SWE-Bench Verifiedが先に中止された理由は何ですか？"
    choices: ["利用料が高すぎるため", "開発者が不足しているため", "データ汚染と試験問題自体の欠陥のため"]
    answer: 2
    explanation: "データ汚染の問題とともに、検討された問題の約60%が構造的に欠陥があることが判明し、中止されました。"
  - question: "SWE-Bench Proを開発した企業はどこですか？"
    choices: ["Google", "Scale AI", "Microsoft"]
    answer: 1
    explanation: "SWE-Bench ProはScale AIが開発し、2025年9月に公開しました。"
lang: ja
ref: 2026-07-09-OpenAI-no-longer-recommends-SWE-Bench-Pro
---

想像してみてください。非常に重要な数学の試験を受けに行ったのに、正答集が間違っていたり、問題自体が成立していなかったりと、エラーだらけの状況を。学生はいくら一生懸命問題を解いても、自分の正確な実力を評価されることはないでしょう。最近、AI業界で起きている「コーディング試験」論争は、まさにこれと同じです。

OpenAIはこれまで、AIのソフトウェアエンジニアリング能力を測定するツールとして「SWE-Bench Pro」を積極的に推奨してきました。しかし最近、OpenAIはこの試験問題の約30%が誤って構成されており、結果の信頼性を担保できないと判断しました。これを受け、もはや公式の評価基準としては推奨しないと発表しました [Source 3, Source 11, Source 4]。

### なぜこれが重要なのか？

私たちが毎日使うスマートフォンアプリ、銀行システム、ニュースサービスなどはすべて、開発者が作成したコードで動いています。したがって、AIがどれだけコーディングを上手くこなせるかは、私たちが日常生活で接する技術がいかにスマートになるかを決定する非常に重要な指標です。

ところが、この「コーディング実力」を測定する試験問題が使い物にならないとしたら、どうなるでしょうか？AI企業は自社のモデルがより優れていることを証明するために、この試験の成績を活用してきました。もし試験自体が間違っていれば、性能が誇張されたり、あるいは正当な評価を受けられなかったりと、歪んだ結果が出る可能性があります。これは、私たち消費者が接するAI技術の実際的な進歩レベルを誤解させる危険性が高いものです。

### わかりやすく解説：AIコーディング試験の秘密

コーディング試験は通常、「ユニットテスト（Unit Test：特定の機能をコードが正しく実行しているかを確認する自動化された検査）」を通じてスコアを算出します。例えば、「このボタンを押すと画面が切り替わるように作れ」という問題に対してAIがコードを書き、テストを通過すれば正解とする方式です。

例えるなら、このようなものです。料理大会を開催するのに、審査員が「スープの濃度」を測定すると言っておきながら、基準にしていたのがデタラメな温度計だったとします。シェフ（AI）がどれほど素晴らしい料理を作っても、間違った温度計のせいで実力が低く評価されたり、あるいは逆にデタラメな料理に高得点を与えたりするのと変わりません。

OpenAIは以前、「SWE-Bench Verified」という評価ツールも使用していました。しかし、これもデータ汚染の問題とともに、試験問題の約59%に構造的欠陥があるという事実が判明し、中止された経緯があります [Source 2, Source 8, Source 13, Source 9]。

今回推奨が中止されたSWE-Bench Proも、実際のGitHub（開発者がコードを共有するプラットフォーム）の複雑な課題をもとに問題を作成した結果、AIが単独で解くには課題の性格自体が曖昧で断片化しているとの指摘を受けてきました [Source 3, Source 14]。

### 現状：泥沼の中の真珠探し

現在、AIモデルは飛躍的に発展しています。しかし、その性能を測定する指標は、まだ「AI時代」に見合った完成度を備えていません [Source 6, Source 14]。

SWE-Bench ProはScale AIという会社が2025年9月に出したもので、従来よりも強力な著作権ライセンスを適用してデータ汚染を最小限に抑えようと努めました [Source 7, Source 8]。しかし今回の発表を通じて、どれほど精巧に設計しようとしても、実際の開発環境の複雑さを自動化された試験に完璧に移し替えることが、いかに難しいかということが明らかになりました。

Scale AIの研究責任者であるビング・リウ（Bing Liu）は、今回の決定は、課題の曖昧さ、データ汚染、そして狭義のユニットテストだけではAIの実力を完全に測定することはできないという限界を、如実に示していると述べています [Source 14]。

### 今後はどうなるか？

今後、AIのコーディング実力を評価する方式は根本的な変化を経験するでしょう。

1. **より精巧な評価標準**: 業界は単に自動化されたスコアに依存する代わりに、AIが問題を解決する「プロセス」と「複雑度」をより総合的に判断できる新しい標準を作ろうと努力するでしょう [Source 12]。
2. **開発者とのコラボレーション強調**: AIが一人でコードを書くことから一歩進み、実際の人間の開発者がAIとどのようにコミュニケーションを取りながら問題を解決していくかを評価する方式が、より重要になるでしょう。
3. **継続的な検証**: 評価データ自体が汚染されないように管理することが、AIモデル開発と同じくらい重要な「基礎科学」の領域として定着するでしょう。

私たちは今、AIが自らコードを書く時代を生きています。しかし、その能力を正確に評価する「温度計」を作ることも、技術発展に劣らず重要な課題であることを、今回の事件は私たちに気づかせてくれています。

---

## 参考資料

1. [OpenAI Abandons SWE-Bench Verified, Citing Widespread Data Contamination and Flawed Tests](https://www.siliconreport.com/openai-abandons-swe-bench-verified-citing-widespread-data-contamination-and-flawed-tests-6ebd9b34)
2. [OpenAI Retracts Recommendation To Use SWE Bench Pro As Coding Eval Over 30% Broken Tasks](https://officechai.com/ai/openai-retracts-recommendation-to-use-swe-bench-pro-as-coding-eval-over-30-broken-tasks/)
3. [OpenAI no longer recommends SWE-Bench Pro as coding benchmarks saturate](https://savedelete.com/news/openai-swe-bench/)
4. [Why we no longer evaluate SWE-bench Verified - keynews.ai](https://keynews.ai/articles/290)
5. [OpenAI Drops SWE-Bench Verified: What It Means for AI](https://www.adwaitx.com/openai-swe-bench-verified-retired-ai-benchmarks/)
6. [OpenAI Abandons SWE-bench Verified: 59% Flawed Tests](https://byteiota.com/openai-abandons-swe-bench-verified-59-flawed-tests/)
7. [OpenAI Drops SWE-bench Verified Over Contamination Concerns](https://aibreakingwire.com/news/openai-ditches-swe-bench-verified-cites-critical-flaws/)
8. [OpenAI Retracts SWE-Bench Pro After Finding 30% of Tasks Broken | AlphaSignal](https://alphasignal.ai/news/openai-retracts-swe-bench-pro-after-finding-30-of-tasks-broken)
9. [OpenAI Developers on X](https://x.com/OpenAIDevs/status/2026002219909427270)
10. [OpenAI Abandons SWE-bench Verified After Finding 59% of Failed Tests Were Flawed](https://blockchain.news/news/openai-abandons-swe-bench-verified-contamination-flawed-tests)
11. [OpenAI moves beyond SWE-bench Verified as coding benchmarks saturate](https://tessl.io/blog/openai-moves-beyond-swe-bench-verified-as-coding-benchmarks-saturate/)