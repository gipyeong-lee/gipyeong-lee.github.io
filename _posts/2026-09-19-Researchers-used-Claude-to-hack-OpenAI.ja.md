---
layout: post
title: "AIがAIをハッキング？セキュリティ研究者がClaudeでOpenAIを突破した顛末"
description: "最近、セキュリティ研究者たちがAnthropicのAIモデル「Claude」を活用し、OpenAIの内部システムへのハッキングに成功しました。これが私たちに何を意味するのか、AIが抱えるセキュリティリスクを分かりやすく解説します。"
summary: "セキュリティ研究者たちがAIモデル「Claude Opus 5」を活用し、わずか72時間でOpenAIの内部システムをハッキングすることに成功しました。この事件は、AIがサイバーセキュリティの攻撃と防御の両面においてパラダイムシフトを起こしていることを示しています。"
tags: [AI, セキュリティ, Claude, OpenAI, サイバー脅威]
image: 2026-09-19-Researchers-used-Claude-to-hack-OpenAI.jpg
image_alt: "AIセキュリティ研究を象徴する抽象的なデジタルネットワークと、ハッキングを意味するデータ侵入グラフィック"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "今回の事件は、AIが技術的な障壁を下げることで、熟練のハッカーでなくても高度な攻撃を実行可能になったことを意味します。今後はAIセキュリティシステム自体の防御能力強化が不可欠です。"
quiz:
  - question: "研究者たちがOpenAIの内部システムに侵入するまでにかかった時間は？"
    choices: ["24時間以内", "72時間以内", "1週間"]
    answer: 1
    explanation: "研究チームは約3日、つまり72時間以内の短い時間でシステム侵入に成功しました。"
  - question: "今回のハッキング攻撃で決定的な役割を果たしたAIモデルは何ですか？"
    choices: ["GPT-4", "Claude Opus 5", "Gemini 1.5"]
    answer: 1
    explanation: "初期のモデルでは失敗しましたが、Anthropicが新たに公開したClaude Opus 5モデルを使用することで、攻撃コードを完成させることができました。"
  - question: "研究者たちがセキュリティの脆弱性を攻略するために使用した媒体は何ですか？"
    choices: ["偽のEメール", "改ざんされた画像ファイル", "無料Wi-Fi"]
    answer: 1
    explanation: "研究チームは、サードパーティ製フォーラムプラグイン（Discourse）の脆弱性を突くために、改ざんされた画像ファイルを活用しました。"
lang: ja
ref: 2026-09-19-Researchers-used-Claude-to-hack-OpenAI
---

想像してみてください。あなたが巨大な城を守るセキュリティ責任者だとします。城壁に非常に小さな隙間があることは知っていますが、人がその隙間を探し出すには数日徹夜しなければなりません。その時、賢い秘書が現れて「私がその隙間をたった3日で探し出して、扉を開けてみせます」と言ったらどうしますか？

最近、人工知能（AI）の世界でまさにこのようなことが実際に起こりました。インドのセキュリティスタートアップ「Hacktron AI」所属の研究者3名が、AnthropicのAIモデル「Claude」を活用し、世界的なAI企業であるOpenAIの内部システムをハッキングすることに成功したのです [[参考資料 5](https://newsletter.genai.works/p/claude-was-used-to-hack-openai), [参考資料 9](https://thetechportal.com/2026/09/18/openai-hacked-using-claude-hacktron-ai-indian-security-researchers/)]。

### なぜ重要なのか？

単なる「誰かがハッキングした」というニュースよりも重要なのは、ハッキングの「主体」が完全に変わったという点です。これまで複雑なシステムの脆弱性を見つけ出すには、高度な技術を持つ熟練のハッカーがチームを組み、長い時間をかける必要がありました。

しかし今や、人工知能がその役割を代行しています。今回の事件で研究者たちは72時間という短期間で、OpenAIの内部コードシステムと個人のGitHubリポジトリにアクセスすることに成功しました [[参考資料 1](https://www.linkedin.com/news/story/openai-hacked-by-researchers-using-anthropics-claude-8638745/), [参考資料 6](https://the-decoder.com/security-researchers-used-anthropics-claude-to-hack-openais-internal-systems-in-under-72-hours/)]。さらに驚くべきことは、このハッキングを実行するのにかかった費用が3,000ドル未満だったという事実です [[参考資料 9](https://thetechportal.com/2026/09/18/openai-hacked-using-claude-hacktron-ai-indian-security-researchers/)]。これはAIがサイバー攻撃の敷居を飛躍的に下げたことを意味し、企業にとってはセキュリティの脅威がそれだけ身近になったことを示唆しています。

### 分かりやすく解説：デジタル探偵、AI

なぜ人工知能がハッキングに役立つのでしょうか？簡単に言えば、AIは非常に優れた**「デジタル探偵」**の役割を果たします。

私たちがよく使う「トランスフォーマー（Transformer、文中の単語間の関係を把握し、膨大なデータを分析するAI構造）」技術を備えたAIは、数万行のコードとセキュリティ文書を一瞬で読み込み、分析します。まるで厚い本を100冊、わずか1分で全て読み終え、その中から非常に小さな矛盾や論理的な穴を見つけ出すようなものです。

研究者たちは今回の攻撃で、「Discourse」というサードパーティ製フォーラムプラグインの脆弱性を攻略しました [[参考資料 1](https://www.linkedin.com/news/story/openai-hacked-by-researchers-using-anthropics-claude-8638745/), [参考資料 7](https://www.theverge.com/ai-artificial-intelligence/997444/openai-hack-claude-heif-heist/)]。最初は「Claude Opus 4.8」バージョンを使用しましたが攻撃には失敗しました。しかし、Anthropicが新たに公開した「Claude Opus 5」モデルを使用すると、以前のモデルでは解決できなかったセキュリティの壁を突破し、攻撃コードを作成することに成功したのです [[参考資料 4](https://techcrunch.com/2026/09/18/researchers-used-anthropics-claude-to-hack-into-openai/), [参考資料 6](https://the-decoder.com/security-researchers-used-anthropics-claude-to-hack-openais-internal-systems-in-under-72-hours/)]。AIが賢くなるほど、攻撃の成功確率も高まっているのです。

### 現在の状況：善意のハッキング

もちろん、今回のハッキングは善意を持つセキュリティ研究者たちによって行われた「倫理的なハッキング（ホワイトハッカーによるもの）」です。彼らはOpenAIのシステム脆弱性を直接証明し、バグ報奨金を受け取りました [[参考資料 3](https://www.theguardian.com/technology/2026/sep/18/openai-hacked-anthropic-claude-chatbot), [参考資料 11](https://www.livemint.com/technology/tech-news/indianorigin-researchers-used-claude-ai-to-hack-openai-s-systems-got-6-27-lakh-bounty-11789753784566.html)]。

しかし私たちが記憶しておくべきは、今回の攻撃にはClaudeだけでなく、OpenAI自身のモデルである「GPT-5.6 Sol」までもが動員されたという事実です [[参考資料 3](https://www.theguardian.com/technology/2026/sep/18/openai-hacked-anthropic-claude-chatbot)]。つまり、ハッカーたちはAIモデル同士を競わせたり組み合わせたりして、より強力な攻撃を設計しているのです。これはAIが持つ「二面性」を示しています。AIはセキュリティを守る頼もしい盾にもなり得ますが、同時に強力な攻撃兵器にもなり得るのです。

### 今後はどうなるのか？

今後は「AI 対 AI」のセキュリティ戦争が繰り広げられる可能性が高いです。攻撃者はAIを利用してセキュリティの脆弱性をより素早く探し出そうとし、防御者はそれ以上に賢いAIを構築してリアルタイムで防御壁を築かなければならないでしょう。

ユーザーの立場としては、今後はAIを利用する際にセキュリティへの注意をより一層払う必要があります。企業がAIセキュリティを強化する間、個人は疑わしいリンクやファイルを安易にクリックしないといった基本的なセキュリティ対策を守ることが、これまで以上に重要になりました。今回の事件は、AI時代のセキュリティが単なるプログラムの問題ではなく、私たち全員の日々のリスク管理になったことを思い出させてくれます。

---

## MindTickleBytesのAI記者による視点
今回の事件は、AIが単なる道具から脱却し、自らシステムの脆弱性を探索する「エージェント」へと進化していることを証明しています。セキュリティ研究者たちの肯定的な実験ではありましたが、悪意を持つ攻撃者がこの技術を手にすれば、その影響力は予測できません。今後はAI開発と同じくらい、AIが誘発しうるセキュリティの脅威を防ぐ「防御用AI」の技術的飛躍が急務です。

## 参考資料
1. OpenAIhackedbyresearchersusingAnthropic'sClaude| LinkedIn: https://www.linkedin.com/news/story/openai-hacked-by-researchers-using-anthropics-claude-8638745/
2. ResearchersusedClaudetohackOpenAIemployees' ChatGPT...: https://www.theregister.com/security/2026/09/18/researchers-used-claude-to-hack-openai-employees-chatgpt-accounts/5297517
3. OpenAI‘ethicallyhacked’ with help of Anthropic’sClaudechatbot: https://www.theguardian.com/technology/2026/sep/18/openai-hacked-anthropic-claude-chatbot
4. ResearchersusedAnthropic'sClaudetohackintoOpenAI: https://techcrunch.com/2026/09/18/researchers-used-anthropics-claude-to-hack-into-openai/
5. ClaudewasusedtohackOpenAI| Generative AI Newsletter: https://newsletter.genai.works/p/claude-was-used-to-hack-openai
6. Security researchers used Anthropic's Claude to hack OpenAI's ...: https://the-decoder.com/security-researchers-used-anthropics-claude-to-hack-openais-internal-systems-in-under-72-hours/
7. Security researchers used Claude to help them hack into OpenAI: https://www.theverge.com/ai-artificial-intelligence/997444/openai-hack-claude-heif-heist
8. Hackers Used Anthropic’s Claude to Break Into OpenAI: https://www.wsj.com/tech/ai/hackers-used-anthropics-claude-to-break-into-openai-b40ba883
9. Three Indian researchers used Claude to hack into OpenAI in ...: https://thetechportal.com/2026/09/18/openai-hacked-using-claude-hacktron-ai-indian-security-researchers/
10. AI security experts say theyusedClaudetohackChatGPT - CBSNews: https://www.cbsnews.com/news/claude-hack-chatgpt-anthropic-openai/
11. Indian-originresearchersusedClaudeAItohack...: https://www.livemint.com/technology/tech-news/indianorigin-researchers-used-claude-ai-to-hack-openai-s-systems-got-6-27-lakh-bounty-11789753784566.html