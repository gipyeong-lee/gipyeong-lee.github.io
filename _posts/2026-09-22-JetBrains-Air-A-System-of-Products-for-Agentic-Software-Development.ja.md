---
layout: post
title: "AIがコーディングを支援？これからは「指揮」する番です：JetBrains Airの紹介"
description: "複数のAIエージェントを同時に調整し、効率的にソフトウェアを開発する新しい環境、JetBrains Airについて解説します。"
summary: "JetBrains Airは、開発者が複数のAIエージェントを同時に指揮・管理できるようにするための新しいオーケストレーションツールです。"
tags: [AI, ソフトウェア開発, JetBrains, エージェント, 生産性]
image: 2026-09-22-JetBrains-Air-A-System-of-Products-for-Agentic-Software-Development.jpg
image_alt: "JetBrains Airのロゴと、AIエージェントたちが協力して作業する様子を示す概念的なグラフィック。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "複雑なコーディング作業において、AIの役割を単なる補助者から実行主体へと拡張するのは自然な流れです。開発者が直接「指揮」する環境を提供することで、生産性とコントロール権の両方を手に入れようとするJetBrainsの戦略が際立っています。"
quiz:
  - question: "JetBrains Airはどのような役割を果たすツールですか？"
    choices: ["既存のIDEを完全に置き換えるエディタ", "複数のAIエージェントを同時に管理し調整する環境", "AIモデルを直接生成するソフトウェア"]
    answer: 1
    explanation: "Airは既存のIDEを置き換えるものではなく、その上で複数のAIエージェントを効率的に実行し、協働させるためのオーケストレーション（調整）レイヤーです。"
  - question: "Airで使用できるAIエージェントは何ですか？"
    choices: ["JetBrainsが独自に作成した単一のAIのみ可能", "さまざまな外部AIエージェント（Codex、Claude、Gemini、Junieなど）を自由に選択可能", "AIモデルは使用できずコードのみ作成可能"]
    answer: 1
    explanation: "Airはマルチベンダーエコシステムをサポートしており、ユーザーは自分に合った多様な外部AIエージェントを自由に選択して使用できます。"
  - question: "JetBrains Airはローカル環境で実行されるモデルをサポートしていますか？"
    choices: ["いいえ、クラウド接続のみサポートしています", "はい、Ollamaなどのローカルモデルランナーと連携して使用可能です", "ユーザーが直接コード構造を修正すれば可能です"]
    answer: 1
    explanation: "AirはOllamaやLM Studioなどのローカルモデルランナーと連携し、オフライン状態でもモデルを実行できる環境を提供します。"
lang: ja
ref: 2026-09-22-JetBrains-Air-A-System-of-Products-for-Agentic-Software-Development
---

想像してみてください。複雑なアプリを作成する際、あなたはプロジェクトマネージャーとなり、複数の専門開発者にそれぞれタスクを割り当てます。「Aさん、UIデザインのコードを書いてください」「Bさん、データベース連携を担当してください」。そしてあなたは、彼らの成果物を最終チェックし、一つにまとめ上げます。

これまでAIがコーディングを支援するといえば、通常は1対1でAIと対話し、コードを修正してもらうのが一般的でした。しかし今、AIは単なる「支援者」を超え、実際の作業を自ら遂行する「エージェント（Agent：自ら計画を立てて実行するAI）」の時代に突入しました。本日紹介する[JetBrains Air](https://blog.jetbrains.com/blog/2026/09/22/introducing-jetbrains-air/)は、まさにこれらのエージェントを効果的に管理し、指揮できるようにする新しい環境です。

### なぜこれが重要なのか？

ソフトウェア開発がますます複雑になるにつれ、一人の開発者がすべてのコード行を把握することは困難になりました。そのため、複数のAIを同時に使おうとする試みは多くありましたが、個々のAIがバラバラに動くため、かえって管理コストだけが増大するケースが少なくありませんでした。

JetBrains Airは、開発者が「指揮者」として中心を担えるようにします。[複数のAIエージェントを同時に実行](https://air.dev/)して作業を分担させ、開発者はコード全体の流れや品質のチェックに集中できるのです。特に、既存のツール（IntelliJ IDEA、PyCharmなど）をそのまま使いながらこの機能を追加できるという点で、[既存のワークフローを大きく変えることなくAIの力を借りられることは大きな利点](https://baeseokjae.github.io/posts/jetbrains-air-review-2026/)です。

### 簡単に理解する：オーケストレーション（Orchestration）とは？

ここで「オーケストレーション（Orchestration：複数の要素を調整して一つの成果物を作る過程）」という概念が重要になります。簡単に言えば、オーケストラを運営するのと似ています。

*   **従来方式：** 楽器を一つ手に持ち独奏する演奏者と、その隣で拍子を合わせる助手1人（従来のAIコーディングツール）。
*   **Airの方式：** 数十人の専門演奏者（多様なAIエージェント）が集まったオーケストラ。そして彼らの前でタクトを振り、曲全体の調和を作り出す指揮者（開発者）。

JetBrains Airは、まさにこのオーケストラの「指揮台」です。[エージェント・クライアント・プロトコル（ACP：Agent Client Protocol）](https://daily.dev/posts/jetbrains-air-building-a-system-of-products-for-agentic-software-development-4kn5dhuhy)という標準技術を通じて、異なるAIたちがまるで一つのシステムのように、開発者のIDE（統合開発環境）と連携できるようにします。これにより、コードの計画、実行、検証までのプロセスを[一貫した一つの流れとして整理](https://blog.jetbrains.com/air/2026/03/24/introducing-jetbrains-air/)できるのです。

### 現状：どこまでできるのか？

JetBrainsは26年間、開発者ツールを作ってきたノウハウをもとにこの環境を構築しました。現在、JetBrains Airは次のような特徴を備えています。

1.  **多様なエージェントの共存：** Codex、Claude Agent、Gemini CLI、Junieなど、検証済みの様々な[AIエージェントを自由に選択して連携](https://air.dev/)できます。
2.  **ローカルモデルのサポート：** データを外部に送信したくない場合やオフライン作業が必要なときは、[OllamaやLM Studioのようなローカルモデルランナーを通じて、自分だけの環境でモデルを実行](https://blog.jetbrains.com/air/2026/07/what-s-new-air-gets-more-agents-local-models-and-java-kotlin-code-intelligence/)することも可能です。
3.  **IDE連携：** 新しいツールを学ぶ苦労をすることなく、[既存の使い慣れたJetBrains IDE内でそのまま使用可能](https://altaitools.com/jetbrains-air/)です。

ただし、JetBrains自身も正直に明かしているように、[複雑な大規模コードベースをAIが完全に自力で完成させる段階にはまだ至っていません。](https://altaitools.com/jetbrains-air/) したがって、Airはエージェントがコードを書き、開発者がそれをチェックするという、人間中心の「協働環境」に重点を置いています。

### 今後はどうなるか？

かつてJetBrainsは「Fleet」という軽量なエディタを発表しましたが、既存製品群との重複などの理由から[開発を中止し、Airの開発に注力するように戦略を修正](https://technewsdaily.com/software/jetbrains-abandons-fleet-for-air-agentic-development-environment/)しました。これは単に新しいツールを出すという以上に、会社の未来を「エージェントベースの開発」に賭けたことを意味します。

今後は開発者にとって、コードを直接打つ量よりも、コードを設計し、AIエージェントが正しく動作するように「指示」する能力がより重要になるでしょう。[JetBrains Airのような環境が普及すれば、開発者の役割は「実装者」から「設計および管理者」へと急速に移行](https://sdtimes.com/ai/jetbrains-previews-air-an-agentic-development-environment/)していくものと見られます。

---

### MindTickleBytesのAI記者視点
技術はますます発展していますが、重要なのは「誰が主導権を握るか」です。JetBrains Airは、AIを無条件に信じて任せるのではなく、開発者が中心で複数のAIの成果物を調整し、責任を持つ環境を作ったという点で、実務志向の現実的なアプローチだと考えます。AI時代の開発者は、コーディングの実力と同じくらい、AIを適材適所に配置し協働させる「指揮能力」を磨くべき時期に来ています。

## 参考資料
1. [JetBrains Air: Building a System of Products for Agentic Software Development](https://blog.jetbrains.com/blog/2026/09/22/introducing-jetbrains-air/)
2. [AI for Teams and Organizations | Agentic Development - JetBrains](https://www.jetbrains.com/agentic-software-development/)
3. [Quickstart with Air | JetBrains Air Documentation](https://www.jetbrains.com/help/air/quick-start-with-air.html)
4. [Air: Multitask with agents, stay in control](https://air.dev/)
5. [Air - The JetBrains Blog](https://blog.jetbrains.com/air/)
6. [JetBrains abandons Fleet for Air agentic development environment](https://technewsdaily.com/software/jetbrains-abandons-fleet-for-air-agentic-development-environment/)
7. [Air Launches as Public Preview – A New Wave of Dev Tooling Built on 26 Years of Experience - The JetBrains Blog](https://blog.jetbrains.com/air/2026/03/air-launches-as-public-preview-a-new-wave-of-dev-tooling-built-on-26-years-of-experience/)
8. [JetBrains Air: Building a System of Products for Agentic Software Development | daily.dev](https://daily.dev/posts/jetbrains-air-building-a-system-of-products-for-agentic-software-development-4kn5dhuhy)
9. [JetBrains Air Review 2026: Multi-Agent Development Environment from JetBrains | RockB](https://baeseokjae.github.io/posts/jetbrains-air-review-2026/)
10. [JetBrains Air: The Agentic Development Environment, Explained](https://altaitools.com/jetbrains-air/)
11. [What’s new: Air gets more agents, local models, and Java/Kotlin code intelligence - The JetBrains Blog](https://blog.jetbrains.com/air/2026/07/what-s-new-air-gets-more-agents-local-models-and-java-kotlin-code-intelligence/)
12. [Introducing JetBrains Central: An Open System for Agentic Software Development - The JetBrains Blog](https://blog.jetbrains.com/blog/2026/03/24/introducing-jetbrains-central-an-open-system-for-agentic-software-development/)
13. [JetBrains abandons Fleet IDE, pins hopes on forthcoming Air agentic development tool](https://devclass.com/2025/12/09/jetbrains-abandons-fleet-ide-pins-hopes-on-forthcoming-air-agentic-development-tool/)
14. [JetBrains previews Air, an agentic development environment - SD Times](https://sdtimes.com/ai/jetbrains-previews-air-an-agentic-development-environment/)
15. [JetBrains names the debt AI agents leave behind - The New Stack](https://thenewstack.io/jetbrains-names-the-debt-ai-agents-leave-behind/)