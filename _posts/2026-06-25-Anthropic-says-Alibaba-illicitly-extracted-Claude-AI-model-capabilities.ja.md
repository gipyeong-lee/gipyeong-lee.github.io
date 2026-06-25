---
layout: post
title: "私のAIが複製された？『Claude』が巻き込まれた大規模な技術窃盗事件"
description: "Anthropicが、Alibabaなどの中国企業が同社のAIモデル「Claude」の知能を不正に複製（蒸留）したと主張した事件について、分かりやすく解説します。"
summary: "AI企業Anthropicが、Alibabaを含む中国のAI企業が同社モデル「Claude」の知能を不当に盗用したと主張し、米政府に調査を要請しました。"
tags: [AI, 技術, Anthropic, Claude, Alibaba]
image: 2026-06-25-Anthropic-says-Alibaba-illicitly-extracted-Claude-AI-model-capabilities.jpg
image_alt: "複雑に絡み合うデジタルデータノードと、その間を流れる情報の流れを象徴する抽象的な画像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "今回の事件は、AIモデルの「知能」をどのように保護すべきかという新たな法的・倫理的課題を突きつけています。技術開発のスピードが速いだけに、モデルの知的財産を保護するための国際的なガイドライン策定が急務です。"
quiz:
  - question: "今回の事件でAnthropicが主張する「蒸留（Distillation）攻撃」の核心は何ですか？"
    choices: ["AIのデータを直接削除すること", "強力なAIの回答を学習データとして利用し、性能を模倣すること", "AIサーバーを物理的にハッキングすること"]
    answer: 1
    explanation: "Anthropicは、競合モデルが同社モデル「Claude」の回答データを大量に収集し、自社のAIを学習させる手法で性能を不当に高めたと主張しています。"
  - question: "Anthropicの調査結果によると、今回の攻撃に動員されたと疑われる偽アカウントの数は約いくつですか？"
    choices: ["約250個", "約2,500個", "約25,000個"]
    answer: 2
    explanation: "Anthropicの発表によると、約25,000個の偽アカウントを動員し、なんと2,880万件もの質問を投げかけたとのことです。"
  - question: "今回Anthropicが公に指摘した企業が属する国はどこですか？"
    choices: ["米国", "中国", "韓国"]
    answer: 1
    explanation: "AnthropicはAlibabaをはじめ、DeepSeek、Moonshot AI、MiniMaxなど、中国拠点のAI開発企業を名指ししました。"
lang: ja
ref: 2026-06-25-Anthropic-says-Alibaba-illicitly-extracted-Claude-AI-model-capabilities
---

想像してみてください。あなたが数年間、夜を徹して非常に賢く創造的な個人家庭教師を作ったとします。ところが、誰かがこっそりとこの教師の授業内容をすべて録音してまとめ、瓜二つの「偽の教師」を作って格安で授業を提供し始めたら、どんな気分になるでしょうか。

最近、人工知能（AI）業界でまさにこのようなことが起きたという主張がなされました。AIモデル「Claude」を開発したAnthropic（アンソロピック）が、Alibabaを含む複数の中国AI企業が、自社モデルの知能をこっそり盗用したと主張して立ち上がったのです。[参考資料 1](https://www.channelnewsasia.com/business/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-6207956)

### なぜこれが重要なのか？

今回の事件は単なる企業間の争いを超えて、私たちの日常生活に深く入り込んでいる「AIの知能」がどのように作られ、保護されているのかという重要な問いを投げかけています。実のところ、AIモデルを一つ作るには天文学的な費用と、数多くの研究者の努力が必要です。[参考資料 9](https://claude.com/) もし誰かがこの膨大な努力を格安で複製できるのであれば、新しいAIを開発しようとする企業の意欲は大きく削がれざるを得ません。これは結局、技術発展のスピードを遅らせ、市場の公正な競争を阻害する結果を招く恐れがあります。[参考資料 8](https://techgolly.com/news/alibaba-illicit-ai-model-accusations-cause-shares-to-drop-as-anthropic-warns-white-house)

### 分かりやすく解説：「蒸留」という名の窃盗

Anthropicは今回の事件を「蒸留（Distillation）攻撃」と呼んでいます。[参考資料 17](https://finance.yahoo.com/technology/ai/articles/anthropic-says-alibaba-illicitly-extracted-203048734.html) ここでいう蒸留とは、AI業界でよく使われる学習方法なのですが、簡単に例えると「賢い先生の要約ノート」をこっそり丸写しするようなものです。

もともと蒸留（小さなモデルが大きなモデルの回答を真似して学習する手法）は、性能が優れた「先生AI」の回答を参考にして、性能の低い「生徒AI」をより賢くする正当な学習手法です。[参考資料 6](https://www.jpost.com/business-and-innovation/article-887718) しかし、Anthropicが問題視しているのは、このプロセスが「許可なく」大規模に行われたという点です。

まるで料理人が秘伝ソースの作り方を知るためにこっそりと厨房に侵入し、ソースの配合表を2,880万回も試したようなものです。[参考資料 8](https://techgolly.com/news/alibaba-illicit-ai-model-extraction-accusations-cause-shares-to-drop-as-anthropic-warns-white-house) Anthropicは、Alibabaの特定の研究チームが、なんと2万5千個もの偽アカウントを作成してClaudeに質問攻めにし、このノウハウを盗み出そうとしたと主張しています。[参考資料 8](https://techgolly.com/news/alibaba-illicit-ai-model-extraction-accusations-cause-shares-to-drop-as-anthropic-warns-white-house), [参考資料 13](https://stocktwits.com/news-articles/markets/equity/anthropic-writes-to-white-house-accusing-alibaba-of-illicitly-accessing-claude-ai-models/cZKyprTR7Qd)

### 現在の状況：Anthropicの反撃

Anthropicはこの件を非常に深刻に受け止めています。単に抗議する次元を超え、米上院議員やホワイトハウスの関係者に公式書簡を送り、この事態を知らせました。[参考資料 2](https://www.zerohedge.com/political/anthropic-accuses-alibaba-running-major-adversarial-distillation-campaign-extract-claude)

今回名指しされた企業はAlibabaだけではありません。Anthropicは、DeepSeek、Moonshot AI、MiniMaxを含む計3社の中国AI開発企業が、同様の手法で自社の技術を無断で抽出し、自社モデルを向上させたと明らかにしました。[参考資料 3](https://www.linkedin.com/posts/vaibhav-pandya_anthropic-says-chinese-ai-firms-used-16-million-activity-7432708525300031488-uasc), [参考資料 5](https://gizmodo.com/anthropic-says-chinese-ai-companies-made-models-by-illicitly-copying-its-capabilities-2000725717) 現在、この問題は国際的なAI技術覇権争いと絡み合い、ホットな話題となっています。[参考資料 16](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/)

### 今後の展望

この事件は今後、「AI知能の著作権」という新たな法的議論を巻き起こす可能性が高いです。これまではソフトウェアやコンテンツの著作権に焦点が当てられてきましたが、これからはAIモデルが学習した「知能の神髄」をどのように保護するかが核心課題となるでしょう。

ユーザーの立場からは、こうした事件がAI開発企業のセキュリティポリシーを強化する契機となり、より安全なAI環境が作られるのか、あるいはサービス制限などの不便さとなって返ってくるのかを見守る必要があります。確かなことは、AIが賢くなればなるほど、それを盗もうとする試みと守ろうとする努力の間の緊張感はますます高まるだろうということです。

## 参考資料

1. [Anthropic says Alibaba illicitly extracted Claude AI model capabilities](https://www.channelnewsasia.com/business/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-6207956)
2. [Anthropic Accuses Alibaba Of Running Major Adversarial Distillation Campaign](https://www.zerohedge.com/political/anthropic-accuses-alibaba-running-major-adversarial-distillation-campaign-extract-claude)
3. [China's AI Companies Illicitly Extract Claude Capabilities](https://www.linkedin.com/posts/vaibhav-pandya_anthropic-says-chinese-ai-firms-used-16-million-activity-7432708525300031488-uasc)
4. [Anthropic accuses Chinese AI firms of siphoning Claude via distillation](https://biz.chosun.com/en/en-it/2026/02/24/7QIXKECJTBBLTA5VZQ42SBM7LY/)
5. [Anthropic Says Chinese AI Companies Improved Models By 'Illicitly Copying'](https://gizmodo.com/anthropic-says-chinese-ai-companies-made-models-by-illicitly-copying-its-capabilities-2000725717)
6. [Anthropic accuses Chinese labs of stealing Claude's data](https://www.jpost.com/business-and-innovation/article-887718)
7. [Anthropic alleges large-scale distillation campaigns targeting Claude](https://www.computerworld.com/article/4136474/anthropic-alleges-large-scale-distillation-campaigns-targeting-claude-2.html)
8. [Alibaba Illicit AI Model Extraction Accusations Cause Shares to Drop](https://techgolly.com/news/alibaba-illicit-ai-model-extraction-accusations-cause-shares-to-drop-as-anthropic-warns-white-house)
9. [Claude](https://claude.com/)
10. [Anthropic Accuses Chinese AI Firms of Illicit Model “Distillation”](https://techgrid.media/news/anthropic-accuses-chinese-ai-firms-of-illicit-model-distillation-in-claude-copying-dispute/)
13. [Anthropic Writes To White House Accusing Alibaba Of “Illicitly” Accessing Claude AI](https://stocktwits.com/news-articles/markets/equity/anthropic-writes-to-white-house-accusing-alibaba-of-illicitly-accessing-claude-ai-models/cZKyprTR7Qd)
16. [Anthropic says Alibaba illicitly extracted Claude AI model capabilities](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/)
17. [Anthropic says Alibaba illicitly extracted Claude AI model capabilities](https://finance.yahoo.com/technology/ai/articles/anthropic-says-alibaba-illicitly-extracted-203048734.html)
18. [Anthropic Accuses Alibaba of Distilling Claude AI Model Capabilities](https://www.globalbankingandfinance.com/anthropic-alibaba-illicitly-extracted-claude-ai-model/)