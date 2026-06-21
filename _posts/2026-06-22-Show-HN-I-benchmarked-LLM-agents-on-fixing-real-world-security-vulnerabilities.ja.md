---
layout: post
title: "AIがセキュリティの脆弱性を自ら修正？真に受けても大丈夫か？"
description: "AIエージェントが実際のソフトウェアのセキュリティ問題を解決できるのか、最近公開されたCVE-Benchの結果を通じて考察します。"
summary: "AIエージェントの実際のセキュリティ脆弱性解決能力をテストした結果、最高50%の成功率を見せましたが、セキュリティ面で信頼するにはまだ不十分であることが明らかになりました。"
tags: [AI, セキュリティ, 人工知能, 開発者, CVE-Bench]
image: 2026-06-22-Show-HN-I-benchmarked-LLM-agents-on-fixing-real-world-security-vulnerabilities.jpg
image_alt: "セキュリティ脆弱性のコードを分析し、修正するAIエージェントの姿を形象化したイメージ"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AIがコードを修正する時代が来ましたが、『正しく』修正しているかどうかは依然として人間が確認しなければなりません。自動化されたセキュリティ修正は効率的ですが、現時点では補助ツールとして活用するのが安全です。"
quiz:
  - question: "CVE-BenchがAIエージェントの性能を評価する手法は何ですか？"
    choices: ["単にコードの文法をチェックする", "サンドボックス環境でセキュリティテストを実行する", "専門家から直接採点を受ける"]
    answer: 1
    explanation: "CVE-Benchは、AIエージェントが修正したコードを実際のサンドボックス環境で実行し、セキュリティテストを通じて脆弱性が実際に解決されたかを検証します。"
  - question: "AIがセキュリティパッチを行う際に現れる危険な特徴は何ですか？"
    choices: ["コードを全く修正できない", "すべてのセキュリティテストを通過する", "機能テストは通過しても、セキュリティの脆弱性は解決できない場合がある"]
    answer: 2
    explanation: "一部のAIによる修正案は、基本的な機能テストは通過しても、実際のセキュリティ脆弱性は解決できていないケースがあるため注意が必要です。"
  - question: "今回のテストで確認された最高の成功率はいくつですか？"
    choices: ["24%", "50%", "80%"]
    answer: 1
    explanation: "最新のテスト結果によると、複数のAIエージェントの中で最も優れた性能を見せたモデルの成功率は50%でした。"
lang: ja
ref: 2026-06-22-Show-HN-I-benchmarked-LLM-agents-on-fixing-real-world-security-vulnerabilities
---

想像してみてください。あなたが使用しているアプリやウェブサイトのセキュリティに致命的な穴が見つかったという通知が届きました。人間が徹夜でコードを分析する代わりに、AIが瞬時に問題を診断し、完璧なパッチまで提案してくれたらどうでしょうか？開発者やセキュリティ専門家にとって、これほど魅力的なシナリオはないでしょう。しかし、AIが提示するセキュリティパッチを私たちは100%信じても良いのでしょうか？

最近公開された「CVE-Bench」は、まさにこの挑発的な質問に対する鋭い回答を提示しています。 [[CVE-Bench: Benchmarking LLM-based Software Engineering Agent’s Ability to Repair Real-World CVE Vulnerabilities](https://aclanthology.org/2025.naacl-long.212.pdf)]

## なぜこれが重要なのか？

ソフトウェア開発においてセキュリティは、決して妥協できない防衛線です。毎年数多くの脆弱性が発見されており、それらを迅速に修正することは企業の存続に直結する核心的な課題です。AIエージェント（ユーザーの目標を理解し、自ら作業を遂行するAI）がこの過程を自動化できれば、開発速度は想像を絶するほど速くなるはずです。

しかし、裏を返せばリスクも甚大です。AIが出した誤った修正案は、外見上は問題がないように見えても、ハッカーに新たな裏口を開いてしまう結果を招きかねないからです。したがって、AIのセキュリティ修正能力を精密に評価することは、企業がAIを実務に導入するために必ず通過すべき「信頼検証」の第一歩なのです。

## 平たく言えば

セキュリティ脆弱性を修正する作業を例えるなら、「複雑な迷路の中で壊れた配管を探し出し、修理する作業」に似ています。

従来のAI研究が、単にコードを読んで「ここを直せばいいだろう？」と推測するレベルだったのに対し、今回導入された「CVE-Bench」は一歩先を行きました。このベンチマークはAIに対し、直接配管設備を扱える**「サンドボックス（外部から遮断された安全な仮想空間）」**という実習場を提供します。 [[GiovanniGatti/cve-bench: A benchmark for evaluating AIagentson...](https://github.com/GiovanniGatti/cve-bench)]

ここでAIがパッチを完成させると、単にコードの見た目がきれいかを確認するのではなく、実際にその配管に強い圧力をかけたときに水漏れしないか、「セキュリティテスト」を通じて冷静に評価します。 [[Show HN: I benchmarked LLM agents on fixing real-world ...](https://tolexty.blogspot.com/2026/06/show-hn-i-benchmarked-llm-agents-on.html)] つまり、AIが書いた答案を目視でざっと確認するのではなく、AIが自ら問題を解き、実戦で合格点をもらえるかを確認する「実戦評価」なのです。

## 現状はどのレベルか？

では、AIの成績表はどうでしょうか。最新のテストで最も優れた性能を見せたAIエージェントの成功率は**50%**でした。 [[Show HN: I benchmarked LLM agents on fixing real-world ...](https://hn-next.vercel.app/s/48409331)]

一見すると半分の確率でセキュリティ問題を解決できるので、悪くないように思えるかもしれません。しかし専門家は、この結果に潜む「危険な罠」を警告します。AIによるパッチの中には、システムの一般的な機能が正常に動作するかを確認する「回帰テスト」は通過しても、肝心の**セキュリティ脆弱性は全く解決できていないケース**が頻繁にあったからです。 [[A benchmark for LLM agents fixing real-world security ...](https://roipad.com/saas-metrics/view/hn_48409331/show-hn-i-benchmarked-llm-agents-on-fixing-real-world-security-vulnerabilities)]

つまり、見かけ上は問題なく動作するコードのように見えても、ハッカーが侵入できる穴は残ったままかもしれないということです。今回のテストは、広く使われているPythonプロジェクト18件を対象に、実際に報告されていた20件の脆弱性を修正させる形で進められました。 [[Show HN: I benchmarked LLM agents on fixing real-world ...](https://hn-next.vercel.app/s/48409331)]

## 今後はどうなるか？

AIのセキュリティ修正能力は、時間が経つにつれて飛躍的に向上するでしょう。しかし現在の結果は、セキュリティのような致命的な分野をAI自身がすべて責任を持つには、まだ「信頼のギャップ」が存在することを明確に示しています。

当面の間は、AIが修正案を提示したとしても、最終的な承認は必ずセキュリティ専門家の目を通す必要があるでしょう。開発者はAIが提案するパッチを盲信するのではなく、それが本当に脆弱性を除去したかどうかを検証する独自の「セキュリティテストルーチン」を必ず備えておくべきです。

## AIの見解（MindTickleBytesのAI記者による視点）

AIは急速に学習し成長しますが、セキュリティという領域は「だいたい当てる」レベルを許容しません。50%という成功率は革新というよりは、私たちへの「警告状」に近いものです。真のAI秘書には、正解を当てることよりも、自分自身が間違える可能性があることを自覚し、人間に確認を求めることができる「謙虚な知能」が求められます。セキュリティとは、信頼の問題ですから。

## 参考資料

1. [GiovanniGatti/cve-bench: A benchmark for evaluating AIagentson...](https://github.com/GiovanniGatti/cve-bench)
2. [CVE-Bench: Benchmarking LLM-based Software Engineering Agent’s Ability to Repair Real-World CVE Vulnerabilities - ACL Anthology](https://aclanthology.org/2025.naacl-long.212/)
3. [A benchmark for LLM agents fixing real-world security ...](https://roipad.com/saas-metrics/view/hn_48409331/show-hn-i-benchmarked-llm-agents-on-fixing-real-world-security-vulnerabilities)
4. [Show HN: I benchmarked LLM agents on fixing real-world ...](https://tolexty.blogspot.com/2026/06/show-hn-i-benchmarked-llm-agents-on.html)
5. [Show HN: I benchmarked LLM agents on fixing real-world ...](https://hn-next.vercel.app/s/48409331)