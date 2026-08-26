---
layout: post
title: "マイPCが賢いAI秘書に？PerplexityとNVIDIAが挑む「ローカルAI」"
description: "PerplexityとNVIDIAが提携し発表したAIエージェントプラットフォーム「Portable Computer」。インターネット接続なしで、自分のPC上で安全かつコストを気にせず利用する方法とは。"
summary: "PerplexityとNVIDIAは、インターネット接続なしで個人のPC上で直接実行されるAIエージェントプラットフォーム「Portable Computer」を公開しました。"
tags: [AI, ローカルAI, Perplexity, NVIDIA, 人工知能]
image: 2026-08-27-Perplexity-partners-with-Nvidia-to-launch-a-local-AI-agent.jpg
image_alt: "NVIDIA GPUベースのパーソナルコンピュータ上で動作するPerplexityのAIエージェントインターフェース画面"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "クラウドへの依存度を下げ、データの主権を個人に還元する重要な転換点です。セキュリティとコスト効率の面で、ローカルAIの魅力はますます高まっていくでしょう。"
quiz:
  - question: "今回PerplexityとNVIDIAが共同で発表したプラットフォームの名称は何ですか？"
    choices: ["クラウドコンピュータ", "ポータブルコンピュータ", "AIローカルハブ"]
    answer: 1
    explanation: "正解は「Portable Computer（ポータブルコンピュータ）」です。インターネット接続なしで個人のデバイス上で直接駆動するAIエージェントプラットフォームです。"
  - question: "このプラットフォームを使用する際に得られるコスト上の利点は何ですか？"
    choices: ["月額サブスクリプション無料", "トークンコストゼロ", "電気代免除"]
    answer: 1
    explanation: "クラウドベースのAIサービス利用時に発生する「トークン費用」が、このプラットフォームでは発生しません。"
  - question: "このAIエージェントは主にどのようなハードウェア環境で実行されますか？"
    choices: ["Webブラウザ", "すべてのスマートフォン", "NVIDIA GPU搭載のPCおよびサーバー"]
    answer: 2
    explanation: "初期段階では、NVIDIA DGX SparkやNVIDIA RTXグラフィックカードを搭載したLinuxベースのPCなどで実行可能です。"
lang: ja
ref: 2026-08-27-Perplexity-partners-with-Nvidia-to-launch-a-local-AI-agent
---

想像してみてください。朝起きてコンピュータに「今日の会議資料を整理しておいて」と話しかける様子を。これまで私たちが使ってきた生成AIの多くは、巨大なクラウド（インターネットで接続された遠隔サーバー）を経由する必要がありました。しかし今、その賢いAI秘書がインターネットの向こう側ではなく、机の上のコンピュータの中で安全に作業を処理してくれる未来が目前に迫っています。

最近、AI検索サービスで有名なPerplexityは、グラフィック処理装置（GPU）の覇者であるNVIDIAと手を組み、新しいAIエージェントプラットフォーム「Portable Computer」を公開しました([PerplexityとNVIDIA、Portable Computerを発表](https://venturebeat.com/infrastructure/perplexity-partners-with-nvidia-to-launch-portable-computer-a-fully-local-ai-agent-with-zero-token-costs))。このサービスは、AIの駆動方式をクラウド中心から個人デバイス中心へと変えようとする革新的な試みです。

## なぜ重要なのか？

最大の変化はコストとセキュリティです。これまでクラウドAIを利用するには、AIが回答を生成するたびに、いわゆる「トークン（AIが使用する単語単位の情報量）」に応じた利用料を支払う必要がありました。しかし「Portable Computer」は、自分のコンピュータのハードウェア性能を借りてAIを直接実行するため、トークン料金を支払う必要はもうありません([Perplexity、Portable Computerを発表](https://www.androidauthority.com/perplexity-portable-computer-local-ai-agent-3703083/))。

また、セキュリティ面でも画期的です。従来は作業内容が外部サーバーに送信されていましたが、今後はAIモデル、ユーザーデータ、そしてAIが行う業務そのものがデバイス内に留まるため、個人情報保護の面で非常に安心できます([PerplexityとNVIDIAによるローカルデスクトップAIエージェント](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lhM3JydkVSRWVaUGZFWUJReU1pZ0FQAQ?hl=en-IN&gl=IN&ceid=IN:en))。

## わかりやすい例え

「Portable Computer」の原理を例えるなら、**「有料図書館」と「個人の書斎」の違い**と同じです。

これまでのクラウドAIが、毎回利用料を払って外部の図書館で本を借りて読む方式だったとすれば、「Portable Computer」は自分の部屋の中に図書館をそのまま持ち込んだようなものです。初期の機器導入費用はかかりますが、一度環境を整えてしまえば、いつでも好きなだけAIを使っても追加費用はかかりません。

技術的には、AIの脳となる「モデル」だけでなく、AIが何をすべきか判断する「オーケストレーター（指揮者）」と「エージェントハーネス（AIエージェントの駆動環境）」のすべてを個人デバイス内で動作させるよう設計されています([PerplexityのローカルAIの動き](https://www.theregister.com/ai-and-ml/2026/08/26/now-perplexity-is-trying-to-get-into-the-local-ai-action/5292449))。つまり、インターネットが切れてもAIが自ら判断し、複雑なタスクを解決するのです([Perplexity、Portable Computerを発表](https://x.com/wallstengine/status/2092262633068277776))。

## 現在の状況

現在、このプラットフォームはNVIDIAのハードウェア環境に最適化された形でスタートします。具体的には、NVIDIAのDGX Sparkシステムや、NVIDIA RTXグラフィックカードを搭載したLinuxベースのPCで利用可能です([NVIDIA DGX SparkとローカルAI](https://www.gadgetvoize.com/2026/08/26/nvidia-pushes-local-ai-with-open-models-agents-and-perplexity-partnership/))。

リリース段階では「Qwen 3.8 27B」モデルや追加学習を経た「Qwen PPLX 27B」モデルをサポートしており、間もなくNVIDIAの「Nemotron 3.5 Lightning (30B)」モデルにも対応予定です([PerplexityとNVIDIAのローカルAIエージェント](https://www.howtogeek.com/perplexity-release-portable-computer-a-local-ai-agent/))。一般的な情報検索から複雑なワークフロー処理まで、ローカルで完結できる点が大きな特徴です([Perplexity、Portable Computerを発表](https://aistart.ai/ainews/perplexity-local-ai-agent-nvidia))。

## 今後の展望

今後はより多くの一般向けPC環境でも、このような「ローカルAI」を体験できるようになると見込まれます。AI技術がクラウドという巨大な枠組みを越えてユーザーのデバイスの奥深くまで浸透することで、インターネット接続が不安定な環境でも高性能AIの恩恵を享受できる時代が始まっています([Perplexity、Portable Computerを発表](https://basic-tutorials.com/news/perplexity-portable-computer-ai-agent-now-runs-locally-on-nvidia-dgx-spark/))。今後、個人用PCを選ぶ際、CPUやRAMだけでなく「どのようなAIエージェントをどれほど高速に動かせるか」が重要な購入基準になる日も近いでしょう。

---

## MindTickleBytesのAI記者による視点
クラウドへの依存度を下げ、データの主権を個人に還元する今回の試みは、人工知能の発展における重要な転換点です。技術が利便性を超え、どれだけ個人の日常に密着して安全に定着できるのか、期待が高まります。

## 参考資料
1. [Perplexity partners with Nvidia to launch Portable Computer, a fully local AI agent with zero token costs | VentureBeat](https://venturebeat.com/infrastructure/perplexity-partners-with-nvidia-to-launch-portable-computer-a-fully-local-ai-agent-with-zero-token-costs)
2. [Perplexity and NVIDIA team up to release a local AI agent | How-To Geek](https://www.howtogeek.com/perplexity-release-portable-computer-a-local-ai-agent/)
3. [Perplexity launches a local AI agent with zero token costs - Android Authority](https://www.androidauthority.com/perplexity-portable-computer-local-ai-agent-3703083/)
4. [Perplexity and Nvidia partner for local-first AI platform | CNBC](https://www.cnbc.com/video/2026/08/25/perplexity-and-nvidia-partner-for-local-first-ai-platform.html)
5. [Wall St Engine on X: "PERPLEXITY LAUNCHES FULLY LOCAL AI AGENTS..."](https://x.com/wallstengine/status/2092262633068277776)
6. [NVIDIA Pushes Local AI With Open Models, Agents and Perplexity Partnership – Gadget Voize](https://www.gadgetvoize.com/2026/08/26/nvidia-pushes-local-ai-with-open-models-agents-and-perplexity-partnership/)
7. [Perplexity and Nvidia partner for local desktop AI agent - Overview | Google News](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lhM3JydkVSRWVaUGZFWUJReU1pZ0FQAQ?hl=en-IN&gl=IN&ceid=IN:en)
8. [Perplexity Launches Local AI Agent Portable Computer | The Outpost](https://theoutpost.ai/news-story/perplexity-portable-computer-brings-local-ai-agent-to-your-desktop-with-no-cloud-dependency-30115/)
9. [Perplexity partners With Nvidia to launch... | VMVirtualMachine.com](https://vmvirtualmachine.com/perplexity-partners-with-nvidia-to-launch-portable-computer-a-fully-local-ai-agent-with-zero-token-costs/)
10. [Portable Computer is Perplexity's new local AI agent - why... | ZDNET](https://www.zdnet.com/article/portable-computer-perplexity-local-ai-agent/)
11. [World Leader in Artificial Intelligence Computing | NVIDIA](https://www.nvidia.com/)
12. [Perplexity and Nvidia Launch a Zero-Token-Cost Local AI Agent | AI Market Watch](https://www.ai-market-watch.com/news/perplexity-and-nvidia-launch-portable-computer-a-fully-local-ai-agent-with-zero--kyx83w)
13. [Perplexity Launches Fully Local AI Agent with Nvidia | AI News](https://aistart.ai/ainews/perplexity-local-ai-agent-nvidia)
14. [Now Perplexity is trying to get into the local AI action | The Register](https://www.theregister.com/ai-and-ml/2026/08/26/now-perplexity-is-trying-to-get-into-the-local-ai-action/5292449)
15. [Perplexity Portable Computer: AI agent now runs locally on NVIDIA DGX Spark | Basic Tutorials](https://basic-tutorials.com/news/perplexity-portable-computer-ai-agent-now-runs-locally-on-nvidia-dgx-spark/)
16. [Perplexity AI launches Portable Computer on-device AI agent | SiliconAngle](https://siliconangle.com/2026/08/25/perplexity-ai-launches-portable-computer-on-device-ai-agent/)