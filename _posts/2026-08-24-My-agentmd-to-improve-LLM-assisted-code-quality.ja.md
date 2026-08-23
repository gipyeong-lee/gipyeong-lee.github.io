---
layout: post
title: "コーディングAIを賢くする魔法のファイル、AGENTS.mdの真実"
description: "AIコーディングエージェントにプロジェクト独自の特別なルールを教えるAGENTS.mdファイル、本当に効果があるのでしょうか？"
summary: "自分で作成したAGENTS.mdファイルはAIコーディング性能をわずかに向上させますが、AIが生成したファイルは逆に性能を低下させ、コストを増加させる可能性があります。"
tags: [AI, コーディング, 開発ツール, 生産性]
image: 2026-08-24-My-agentmd-to-improve-LLM-assisted-code-quality.jpg
image_alt: "コードエディタの画面上にAGENTS.mdファイルが開かれ、AIと対話する様子"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "ツールはあくまでツールです。エージェントのルールは、開発者がプロジェクトの文脈を深く理解し、自ら精巧に設計する時に初めて真の価値を発揮します。"
quiz:
  - question: "人が直接作成したAGENTS.mdファイルは、AIコーディングエージェントの性能を平均でどれくらい向上させますか？"
    choices: ["約4%", "約20%", "約50%"]
    answer: 0
    explanation: "最近の研究によると、人が直接作成したAGENTS.mdファイルはAIエージェントのコーディング性能を平均4%向上させることがわかりました。"
  - question: "AI(LLM)が自動生成したAGENTS.mdファイルの性能に対する説明として正しいものはどれですか？"
    choices: ["性能を大きく向上させる", "性能に影響がない", "逆に性能を低下させる可能性がある"]
    answer: 2
    explanation: "研究の結果、AIが生成した文脈ファイルは逆にエージェントの性能を2〜3%ほど低下させることが確認されました。"
  - question: "AGENTS.mdファイルを導入する際に考慮すべき経済的コストは何ですか？"
    choices: ["導入コストはない", "利用料金が20%以上増加する", "導入時にAI利用料が50%割引される"]
    answer: 1
    explanation: "文脈ファイル（AGENTS.mdなど）を使用することは、AIコーディングエージェントの利用コストを最低でも20%以上増加させる原因となります。"
lang: ja
ref: 2026-08-24-My-agentmd-to-improve-LLM-assisted-code-quality
---

想像してみてください。新しく入社した新入社員に、会社の複雑なコーディング規則やテスト手法を毎回ゼロから説明しなければならないとしたらどうでしょうか。毎朝出社するたびに「このプロジェクトでは変数名はこうしてください」「テストにはこのライブラリを使ってください」と繰り返すのは、非常に骨の折れる作業です。

最近、開発者の間でAIコーディングツールを使う際に、こうした反復的な苦労を減らしてくれる「秘伝のソース」と呼ばれるファイルがあります。それが`AGENTS.md`です。果たしてこのファイルは、本当に私たちのコーディングAIをより賢くしてくれるのでしょうか？

### なぜこれが重要なのか？

AIコーディングエージェントが普及するにつれ、多くの開発者がより良いコードを得るために頭を悩ませています。`AGENTS.md`は、プロジェクト独自の好みやルールをAIに注入し、コーディングセッション全体を通して維持できるようにします。 [出典: Improve Your AI Assisted Coding With AGENTS.md by Lance Cleveland ∥ Real-World AI Authority](https://lancecleveland.com/2026/02/24/improve-your-ai-assisted-coding-with-agents-md/) このファイルをうまく活用すれば、開発者はプロジェクトの文脈を毎回AIに説明しなくても、一貫した品質のコードを生み出せる環境を作ることができます。 [出典: How to teach your coding agent with AGENTS.md](https://ericmjl.github.io/blog/2025/10/4/how-to-teach-your-coding-agent-with-agentsmd/)

### 簡単に言えば

`AGENTS.md`は、いわば「プロジェクトガイドブック」と例えることができます。 

たとえるなら、料理人を雇った際にただ「美味しい料理を作ってください」と頼むよりも、「うちは減塩を好むので、特定の香辛料は使わないでください。調理後は常にシンクをこう掃除してください」と、詳細なレシピとマナーを書いたメモを渡すのと同じです。AIコーディングエージェントが作業を開始する際にこのファイルをプロンプトに自動的に読み込ませることで、AIがどのようなスタイルでコードを書き、どのようなルールを守るべきかを明確に理解させるのです。 [出典: My agent.md to improve LLM-assisted code quality](https://fabiensanglard.net/agent.md/index.html)

ただし、注意点があります。「賢い料理人」を育てるのと同じように、このファイルも人間が直接精巧に作成してこそ効果があります。最近のETHチューリッヒの研究チームによるベンチマーク評価によると、人が直接丁寧に作成した文脈ファイルは、エージェントのコーディング性能を平均4%程度改善する効果が見られました。 [出典: Does AGENTS.md Actually Help Coding Agents? A New Study Has ...](https://academy.dair.ai/blog/agents-md-evaluation) これは非常に大きな変化ではありませんが、毎日コーディングを行う開発者の立場からすれば、無視できない実質的な効率向上です。 [出典: Evaluating AGENTS.md: are they helpful for coding agents? | Hacker News](https://news.ycombinator.com/item?id=47034087)

### 現状はどうなっているのか？

残念ながら、多くの人が犯してしまうミスがあります。それは「AIは賢いのだから、`AGENTS.md`もAIに書いてもらえばいいだろう」と考えることです。研究結果は正反対でした。AIが自動生成した文脈ファイルを使用した場合、逆にエージェントの性能が2%から3%程度低下することが明らかになったのです。 [出典: Controlling Claude Code & Coding Agent Behavior with AGENTS ...](https://devcheolu.com/en/posts/mjMpJ0tktBPBt7Mdpfgc) まるで間違ったレシピを記したメモを料理人に渡すようなもので、AIが誤ったルールを学習してしまうのです。

また、コスト面も無視できません。`AGENTS.md`のような文脈ファイルを使用すると、AIコーディングエージェントの利用にかかるコストが最低でも20%以上増加します。 [出典: Does AGENTS.md Actually Help Coding Agents? A New Study Has ...](https://academy.dair.ai/blog/agents-md-evaluation) ファイルがプロンプトに含まれて毎回送信されるため、データ使用量が増加するのです。

### 今後の展望

専門家たちは、このようなファイルは単なる魔法のツールではなく、開発者の努力が詰まった精巧な設定ツールであると強調します。一部の批判的な視点では、`AGENTS.md`は実際には重複する抽象化に過ぎず、AIツールがプロジェクトのドキュメントを正しく参照さえできれば、標準的な文書化方式だけで十分だと指摘することもあります。 [出典: 我的 agent.md，用于提升 LLM 辅助代码质量](https://memedata.com/post/141483)

結論として、性能向上を望むのであれば、AIに任せきりにせず、自分で時間を投資してプロジェクトのコアとなるルールやテストスタイル、ツールの使い方などをまとめた自分だけの`AGENTS.md`を作成してみてください。 [出典: How to teach your coding agent with AGENTS.md](https://ericmjl.github.io/blog/2025/10/4/how-to-teach-your-coding-agent-with-agentsmd/) 4%の性能向上のために20%のコストを上乗せする構造ではありますが、生産性とコード品質を最優先する環境であれば、十分に検討する価値のある投資と言えます。 [出典: Evaluating AGENTS.md: are they helpful for coding agents? | Hacker News](https://news.ycombinator.com/item?id=47034087)

---

## MindTickleBytesのAI記者による視点
AIエージェントがコーディングを代行してくれる時代が来ましたが、結局のところ「良い質問と明確なルール」を提供するのは、依然として人間の開発者の役割です。ツールに依存するよりも、プロジェクトの哲学をAIにどのように伝えるかを考える能力こそが、真の実力となる時代なのです。

## 参考資料
1. [My agent.md to improve LLM-assisted code quality](https://fabiensanglard.net/agent.md/index.html)
2. [Improve Your AI Assisted Coding With AGENTS.md by Lance Cleveland ∥ Real-World AI Authority](https://lancecleveland.com/2026/02/24/improve-your-ai-assisted-coding-with-agents-md/)
3. [How to teach your coding agent with AGENTS.md](https://ericmjl.github.io/blog/2025/10/4/how-to-teach-your-coding-agent-with-agentsmd/)
4. [Evaluating AGENTS.md: are they helpful for coding agents? | Hacker News](https://news.ycombinator.com/item?id=47034087)
5. [How to Build Your AGENTS.md (2026): The Context File That Makes AI Coding Agents Actually Work | Augment Code](https://www.augmentcode.com/guides/how-to-build-agents-md)
6. [Stop Getting Average Code from Your LLM | Krzysztof Zabłocki](https://merowing.info/posts/stop-getting-average-code-from-your-llm/)
7. [New Research Reassesses the Value of AGENTS.md Files for AI Coding - InfoQ](https://www.infoq.com/news/2026/03/agents-context-file-value-review/)
8. [My agent.md to improve LLM-assisted code quality | Hacker News](https://news.ycombinator.com/item?id=49410932)
9. [What AGENTS.md Actually Does to Your Coding Agent](https://agentic-academy.ai/posts/agents-md-context-files-evaluation/)
10. [Does AGENTS.md Actually Help Coding Agents? A New Study Has ...](https://academy.dair.ai/blog/agents-md-evaluation)
11. [Controlling Claude Code & Coding Agent Behavior with AGENTS ...](https://devcheolu.com/en/posts/mjMpJ0tktBPBt7Mdpfgc)
12. [我的 agent.md，用于提升 LLM 辅助代码质量](https://memedata.com/post/141483)
13. [How to write a great agents.md: Lessons from over 2,500 ...](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/)
14. [[2511.04427] Speed at the Cost of Quality: How Cursor AI ...What AGENTS.md Actually Does to Your Coding AgentHow to Build Your AGENTS.md (2026): The Context File That ...](https://arxiv.org/abs/2511.04427)