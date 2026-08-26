---
layout: post
title: "AIは本当に賢いのか？実は「基礎的な計算」すらできないことがある"
description: "人間のように話すAI、なぜ計算や論理の問題になるととんでもない回答をするのでしょうか？大規模言語モデル（LLM）が抱える意外な限界とその理由を探ります。"
summary: "大規模言語モデル（LLM）は優れた言語能力を持つ一方で、実際の計算や論理的一貫性、物理的世界に対する理解が不足しており、重要なタスクにおいて致命的なミスを犯す可能性があります。"
tags: [AI, LLM, 技術分析, 人工知能]
image: 2026-08-26-Ask-HN-What-is-one-simple-thing-LLMs-are-insanely-bad-at.jpg
image_alt: "複雑な書類の山の中で混乱しているデジタル脳の形をした人工知能のグラフィック"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AIは素晴らしい秘書になり得ますが、計算機や論理的判断の代替品として信用してはいけません。技術の限界を明確に認識してこそ、道具をより賢く活用することができます。"
quiz:
  - question: "大規模言語モデル（LLM）が数学の計算に弱い根本的な理由は何ですか？"
    choices: ["コンピュータの性能が不足しているから", "文章をそれらしく予測しているだけで、実際に計算はしていないから", "学習データが不足しているから"]
    answer: 1
    explanation: "LLMは数値的な演算を行っているのではなく、文脈上次に続く可能性の高いテキストを予測しているだけであるため、正確な計算を実行できません。"
  - question: "LLMの「幻覚（Hallucination）」現象とは何ですか？"
    choices: ["AIが学習を止めてしまう現象", "もっともらしく聞こえるが、実際には間違った情報を生成すること", "人の感情を読み取る機能"]
    answer: 1
    explanation: "幻覚とは、AIが自信を持って回答するものの、実際には事実ではない内容を生成してしまう現象を指します。"
  - question: "LLMを使用した複雑な業務処理を行う際に注意すべき点は何ですか？"
    choices: ["AIが提示する結果を鵜呑みにする", "AIにすべての決定を任せる", "結果を必ず人間が検証する"]
    answer: 2
    explanation: "LLMは一貫性に欠け、論理的な誤りを犯す可能性があるため、最終的な判断と検証は人間が行う必要があります。"
lang: ja
ref: 2026-08-26-Ask-HN-What-is-one-simple-thing-LLMs-are-insanely-bad-at
---

想像してみてください。あなたは今日、重要な報告書を作成していて忙しいとします。隣の席の賢いAI秘書に「昨日の会議で出た数値を合計して、結果を教えて」と頼みます。AIは即座に流暢な文章で回答を返します。ところが、その計算結果が微妙に間違っていたらどうでしょうか？あるいは、同じ質問を1分後に聞き直したとき、先ほどとは全く異なる数値を言ってきたらどうしますか？

私たちはしばしば「賢いAI」の時代を生きていると言います。しかし、いざ中身を調べてみると、これらの大規模言語モデル（LLM、大量のテキストを学習して文章を生成する人工知能）は、私たちが思うほど完璧な「知能」を備えてはいません。時にはごく単純な論理すら理解できず、的外れな方向へ進んでしまうこともあります。

### なぜこの問題が重要なのでしょうか？

AIが学校の教育カリキュラムを作成し、企業の報告書を書き、さらにはコーディングまで代行する世界になりました。[Mind Matters](https://mindmatters.ai/2025/05/llms-are-bad-at-good-things-good-at-bad-things/)は、教育現場において教師と学生の双方がAIチャットボットと対話する環境へ急激に移行していると警鐘を鳴らしています。

問題は、AIが「知ったかぶり」をあまりに上手にこなす点です。[Hackernoon](https://hackernoon.com/a-simple-hardware-question-exposes-the-limits-of-todays-llms)によると、あるユーザーがハードウェアの性能について尋ねた際、AIは非常に専門的かつ説得力のある論理で回答しましたが、技術的には完全に逆の情報を提示しました。このような業務処理のやり方は、結果として意思決定の質を下げ、会社運営を不安定にする「複雑性の危機」を招きかねません。[Hacker News](https://news.ycombinator.com/item?id=48819891) AIの回答を無条件に信頼することは、検証されていない専門家の言葉を盲信するのと同じです。

### つまり、AIの本質とは何なのでしょうか？

なぜこれほど賢そうに見えるAIが、基礎的な計算や論理で崩れてしまうのでしょうか？

例えるなら、**AIは写真撮影が非常に上手な「物真似役者」のようなものです。** この役者は無数の台本を丸暗記しているため、特定の状況が与えられると、もっともらしいセリフを並べ立てます。しかし、この役者は実際に数学の問題を解くことはできず、数字の場所や大きさが何を意味するのかも理解していません。[DEV Community](https://dev.to/james_anderson_h/why-llms-are-bad-at-math-explained-simply-3omj)

LLMの仕組みを詳しく見ると、数字を私たちが目にする1、2、3として理解しているのではなく、膨大な単語の断片（トークン）に分解して学習しています。[Nate Silver](https://www.natesilver.net/p/chatgpt-is-shockingly-bad-at-poker) この過程で、数字同士の位置関係や論理的なヒエラルキーが混ざり合ってしまいます。結果としてAIは、実際に「計算」をしているのではなく、文脈上最もらしく見える単語を確率的に並べているに過ぎません。[DEV Community](https://dev.to/james_anderson_h/why-llms-are-bad-at-math-explained-simply-3omj) 私たちがAIに期待する「知能」と、実際のAIが行う「確率ベースの単語予測」の間には、大きな隔たりが存在するのです。

### 現在の立ち位置：どこまで信じられるか？

現在のAIモデルは、以下のような致命的な限界を抱えています。

1. **幻覚（ハルシネーション）：** 事実ではない情報を、まるで真実であるかのように非常に自信満々に生成します。[Educative](https://www.educative.io/blog/limitations-of-llms)
2. **一貫性の欠如：** 同じ質問をわずか数秒の間隔で再度尋ねると、全く相反する回答を返すことがあります。[Mind Matters](https://mindmatters.ai/2026/01/large-language-models-llms-are-inherently-frail-and-unreliable/)
3. **物理的世界への理解不足：** 単にテキストパターンに従うだけであり、私たちが生きる現実の物理法則や論理構造を理解していないため、荒唐無稽な誤りを犯します。[Hackernoon](https://hackernoon.com/a-simple-hardware-question-exposes-the-limits-of-todays-llms)
4. **基礎論理の失敗：** 繰り返しの相互作用や、複雑な制約条件が付随する問題を解くことに弱いです。[Strange Loop Canon](https://www.strangeloopcanon.com/p/what-can-llms-never-do)

[Builder Society](https://www.buildersociety.com/threads/current-ai-llms-are-so-terrible-basic-task-failure-beyond-writing-is-everywhere.9062/)フォーラムでは、AIがライティングのような基礎的な作業はこなせるものの、重複の削除やデータの組み合わせなど、論理的思考が必要な基本的な業務すら正しく遂行できないという批判が絶えません。これは、私たちがAIを「道具」として眺めるべきであり、決して「判断者」の座に座らせてはならないことを示唆しています。

### 未来はどう変わるのでしょうか？

専門家は、LLMが万能の解決策になるという幻想から脱却するよう促しています。[Hacker News](https://news.ycombinator.com/item?id=45321983) 未来のAIは、自力ですべてを解決するよりも、必要な場合に外部ツール（計算機、コード実行環境など）を直接呼び出して問題を解決する方向へ進化していくでしょう。[Hacker News](https://news.ycombinator.com/item?id=41699457)

想像してみてください。複雑な計算が必要なとき、AIは自ら計算機を起動し、正確な数値を導き出した上で、その結果をもとに文章を作成します。このような「協働型進化」こそが技術の未来となるはずです。

結局のところ、私たちは「AIは完璧なオラクル（回答者）である」という考えではなく、「非常に有能だが、時折嘘をつき、論理が不足することのある秘書」を使っているという心構えを持つべきです。技術が発展しても、AIが生成した成果物を人間が丁寧に検証し、最終的な判断を下す習慣は、当分の間消えることはないでしょう。[Hacker News](https://news.ycombinator.com/item?id=48819891)

## 参考資料

1. [What can LLMs never do? - by Rohit Krishnan](https://www.strangeloopcanon.com/p/what-can-llms-never-do)
2. [AI Leaderboard 2026: Compare & Rank 300+ Top AI Models by...](https://llm-stats.com/)
3. [Why LLMs Are Bad at Math, Explained Simply - DEV Community](https://dev.to/james_anderson_h/why-llms-are-bad-at-math-explained-simply-3omj)
4. [Three Things LLMs Aren’t Great At (Yet) With Examples!](https://www.linkedin.com/pulse/three-things-llms-arent-great-yet-examples-reid-sherman-qdclc)
5. [ChatGPT is shockingly bad at poker - by Nate Silver](https://www.natesilver.net/p/chatgpt-is-shockingly-bad-at-poker)
6. [LLMs Are Bad at Good Things, Good at Bad Things | Mind Matters](https://mindmatters.ai/2025/05/llms-are-bad-at-good-things-good-at-bad-things/)
7. [LLMs are still surprisingly bad at some simple tasks | Hacker News](https://news.ycombinator.com/item?id=45321983)
8. [What are LLMs Bad At? And Why? - InfernoRed Technology Blog](https://blog.infernored.com/what-are-llms-bad-at-and-why/)
9. [A Simple Hardware Question Exposes the Limits of Today’s LLMs](https://hackernoon.com/a-simple-hardware-question-exposes-the-limits-of-todays-llms)
10. [LLMs - What aren't they good for? - manhattanmetric.com](https://www.manhattanmetric.com/blog/2026/02/what-are-llms-bad-at)
11. [What are the limitations of large language models (LLMs)?](https://www.educative.io/blog/limitations-of-llms)
12. [Limitations of LLMs: Bias, Hallucinations, and More](https://learnprompting.org/docs/basics/pitfalls)
13. [Ask HN: Are LLMs slowly making companies dysfunctional ...](https://news.ycombinator.com/item?id=48819891)
14. [Large Language Models (LLMs) Are Inherently Frail and Unreliable | Mind Matters](https://mindmatters.ai/2026/01/large-language-models-llms-are-inherently-frail-and-unreliable/)
15. [This is one of the least interesting questions to ask LLMs. I wish it wasn't so ... | Hacker News](https://news.ycombinator.com/item?id=41699457)
16. [Ask HN: Anyone struggling to get value out of coding LLMs? | Hacker News](https://news.ycombinator.com/item?id=44095189)
17. [Two things LLM coding agents are still bad at | Hacker News](https://news.ycombinator.com/item?id=45523537)
18. [2025: The Year in LLMs | Hacker News](https://news.ycombinator.com/item?id=46449643)
19. [Current AI LLMs are so terrible. Basic task failure beyond writing, is everywhere. | Builder Society](https://www.buildersociety.com/threads/current-ai-llms-are-so-terrible-basic-task-failure-beyond-writing-is-everywhere.9062/)
20. [What can LLMs never do? | Hacker News](https://news.ycombinator.com/item?id=40179232)