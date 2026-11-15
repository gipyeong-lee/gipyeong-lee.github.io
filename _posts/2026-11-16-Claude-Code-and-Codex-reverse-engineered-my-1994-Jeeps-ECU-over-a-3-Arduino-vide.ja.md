---
layout: post
title: "AIが32年前のジープ（Jeep）エンジンをハックしたって？3ドルのチップで不可能を覆した話"
description: "古びた自動車が排気ガス検査に不合格となった際、開発者が3ドルのArduinoとAIコーディングエージェントを使ってエンジンコンピュータをリバースエンジニアリングした実話をわかりやすく紹介します。"
summary: "32年前の1994年式ジープ・チェロキーのECUをAIコーディングエージェントと3ドルのArduinoで解析した実話を通じて、AIが物理世界やレガシーマシンを扱うアプローチを考察します。"
tags: [AI, Claude Code, Codex, 自動車, リバースエンジニアリング]
image: 2026-11-16-Claude-Code-and-Codex-reverse-engineered-my-1994-Jeeps-ECU-over-a-3-Arduino-vide.jpg
image_alt: "32年前の古いジープの車体の前に、3ドルのArduino基板とAIコーディング画面が並んで光り輝いている様子"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "ソフトウェア開発ツールへと進化したAIが、物理世界の骨董品のような機械装置と結びつき、限界を打ち破ったことを示す象徴的な事例です。今後、AIはレガシーシステム保守における強力な救世主となるでしょう。"
quiz:
  - question: "ムハンマド・ズラリ（Muhammad Zulali）がAIと共に修正した自動車のモデルと年式は何ですか？"
    choices: ["1994年式ジープ・チェロキー", "2024年式テスラ モデルY", "1988年式ヒュンダイ・ポニー"]
    answer: 0
    explanation: "ズラリは1994年式ジープ・チェロキー（1994 Jeep Cherokee）の問題を解決するためにAIを活用しました。"
  - question: "車両のコンピュータとAIを接続するために使用された安価なマイクロコントローラーの価格はいくらですか？"
    choices: ["30ドル", "3ドル", "300ドル"]
    answer: 1
    explanation: "わずか3ドルのArduinoマイクロコントローラーをエンジンコンピュータに配線してデータを読み取りました。"
  - question: "このプロジェクトで使用された主要なAIコーディングエージェントは何ですか？"
    choices: ["Claude CodeとCodex", "ChatGPTとMidjourney", "GeminiとLucene"]
    answer: 0
    explanation: "開発者はClaude Code（クロードコード）とOpenAIのCodexを活用してリバースエンジニアリング作業を行いました。"
lang: ja
ref: 2026-11-16-Claude-Code-and-Codex-reverse-engineered-my-1994-Jeeps-ECU-over-a-3-Arduino-vide
---

想像してみてください。長年連れ添った大切な愛車が排気ガス検査で何度も不合格通知を受けるところを。整備工場に行っても、30年以上前の古いモデルだから診断機ですら接続できないという冷たい返答しか返ってこない。修理する術がなく、車を廃車せざるを得ない危機に直面したとき、あなたならどうしますか？

最近、ある開発者がこの不可能に見える状況から驚くべき解決策を見出しました [Source 8, Source 12]。専用のスキャンツールもなく、標準的な診断ポートすらない32年前の古いジープ（Jeep）を修理するため、わずか3ドルの超小型コンピュータと最新の人工知能（AI）コーディングツールを駆使して、車両の頭脳を完全に解読したのです [Source 1, Source 9]。ソフトウェアの世界の住人としか見なされていなかったAIが、いかにして物理的な機械装置の領域にまで深く入り込んだのか、その興味深いストーリーを見ていきましょう。

---

## なぜこれが重要なのか？

私たちは普段、AIがチャット画面で文章を書いてくれたり、ウェブサイトのコードを書いてくれたりする姿に慣れています。しかし、今回の事例が世界の技術コミュニティに大きな衝撃を与えた理由は、AIの能力がモニター画面の枠を超えて「物理世界とレガシーハードウェア（古い既存システム）」へと拡張されたことを証明したからです。

今日、数多くの古い機械装置や工場設備、旧式の自動車は、公式サポートが途絶えて故障しても修理のしようがありません。もしAIが人間には理解しがたい独自の通信規格や古いコンピュータコードを自ら解析し、対話できるようになれば、世界中の数多くのレガシー機器が新たな生命力を得ることができます。今回のプロジェクトは、AIが単なる文章作成の補助を超え、実世界の複雑な物理的問題を解決する強力な問題解決者へと進化していることを示す、重要な21世紀の出来事です。

---

## わかりやすい解説：3ドルのチップとAIが出会ったとき

理解を深めるために、日常の例えで考えてみましょう。1994年式ジープ・チェロキーのエンジンコンピュータは、まるで**「古い暗号だけで対話する古代遺跡の石板」**のようなものです [Source 1, Source 9]。現代の整備工場のスキャン機器は最新の言語しか話せないため、この石板を読み取ることができません。

ここで開発者のムハンマド・ズラリ（Muhammad Zulali）は、**3ドルのArduino（アルディーノ、小型マイクロコントローラー基板）**を使用しました [Source 1, Source 9]。Arduinoはまるで**「古代石板と現代のノートPCをつなぐ翻訳機イヤホン」**の役割を果たしました。しかし、イヤホンがあるからといって古代言語をすぐに理解できるわけではありません。石板に記された暗号を解読する天才的な言語学者が必要でした。

その役割を果たしたのが、Claude Code（ターミナル環境でコードを分析・作成するAIエージェント）とOpenAIのCodexでした [Source 1, Source 9]。開発者はArduinoを車両のエンジンコンピュータ（ECU：Engine Control Unit）に直接配線し、AIコーディングエージェントにリアルタイムで収集されるデータストリームを渡しました [Source 1, Source 9]。AIはまるで何万冊もの解読書を瞬時に読みこなす暗号学者のように、車両が放つ信号の規則を逆算してプログラム構造を突き止めました。

このプロセスは、まさに**「全く未知の未知語の文法を、膨大なデータ分析を通じてわずか数日で完全にマスターするプロセス」**そのものです。

---

## 現状：32年物のジープと1週間の挑戦

主人公であるムハンマド・ズラリの愛車は1994年式ジープ・チェロキーの4.0Lモデルであり、現代の標準化されたOBD2（車両自己診断標準ポート）が一切存在しない車両でした [Source 1, Source 9]。そのうえ、車両と通信できる旧式の診断機器すらまともに機能せず、カリフォルニア州の排気ガス検査に合格し続けることができないという難局に直面していました [Source 1, Source 9, Source 12]。

問題を解決するため、彼は1週間の大いなる挑戦を開始しました [Source 9, Source 12]。具体的なプロセスは以下の通りです：
1. **ハードウェアの接続**：3ドルのArduinoマイクロコントローラーを車両のエンジンコンピュータに直接接続し、通信ライン（OBD1およびSCIシリアル通信方式）に物理的にアクセスしました [Source 1, Source 9]。
2. **データ収集とロギング**：車両の走行中にリアルタイムのセンサーデータを読み取り、記録するドライ브ログを構築しました [Source 9]。
3. **AIベースの分析**：Claude CodeとCodexエージェントを投入し、収集されたデータとエンジンコンピュータの内部プログラムを解析。コードを実際に実行しながら、車両の通信プロトコルをリバースエンジニアリング（Reverse Engineering：完成品を分解して設計原理や構造を逆解析するプロセス）しました [Source 1, Source 9]。

この1週間のドラマチックな道のりは、2026年11月10日にYouTubeで詳細な技術動画として公開され、大きな話題となりました [Source 9]。

---

## これからどうなるのか？

今回の事例は、単なる個人の好奇心に満ちた試みを超え、技術トレンドの重要な転換点を示唆しています。今後、私たちの身の回りにある無数のレガシーハードウェアとソフトウェアが交差する領域において、AIの役割が爆発的に拡大していくでしょう。

1. **修理する権利（Right to Repair）の復活**：メーカーがサポートを打ち切った旧式機器や自動車でも、AIの助けを借りて個人で直接診断・修理できる道が開かれます。
2. **組み込みシステム開発の革新**：ハードウェアのローレベル（Low-level）プログラミングやプロトコル分析の領域にAIエージェントが結合することで、開発に要する時間が数か月から数日へと短縮される可能性があります。
3. **セキュリティ・診断ツールの一般化**：高価な専門診断機器がなくても、オープンソースのハードウェアとAIの組み合わせだけで強力なデバッグ環境を構築できるようになります。

---

## AIの視点

MindTickleBytesのAI記者の視点から見た今回の事件は、AIがバーチャル世界のおもちゃを超え、現実世界の物理的な壁を打ち破り始めたことを告げる号砲です。32年落ちの古い自動車と3ドルのチップ、そして最先端AIの出会いは、テクノロジーが人間の生活をいかに実質的に救うことができるかを示す、最も温かく創造的な証拠です。

---

## 参考資料

1. [Claude Code and Codex reverse engineered my 1994 Jeep's ECU over a $3 Arduino [video]](https://www.youtube.com/watch?v=WPj3aQ-xxpI)
2. [GitHub - zhaoxuya520/reverse-skill: ReverseEngineering...](https://github.com/zhaoxuya520/reverse-skill)
3. [Anthropic sent a takedown notice to a dev trying to reverse-engineer...](https://techcrunch.com/2025/04/25/anthropic-sent-a-takedown-notice-to-a-dev-trying-to-reverse-engineer-its-coding-tool/)
4. [Лучший ИИ-агент для кодинга в 2026: сравнение Claude Code...](https://ip-calculator.ru/blog/artificial-intelligence/luchshij-ii-dlya-koding-sravnenie/)
5. [AI Coding Cost & Token Usage Tracker for Claude Code... | CodeBurn](https://codeburn.app/)
6. [Обновления кодинг-агентов: CodeMode, QwenCode 1.0](https://tproger.ru/news/claude-code-poluchil-code-mode-a-codex-nauchilsya-vybirat-provajd)
7. [AiCodingTools Cursor Claude Code Real Usage | TikTok](https://www.tiktok.com/discover/ai-coding-tools-cursor-claude-code-real-usage)
8. [Claude Reverse-Engineers 1994 Jeep ECU with $3 Arduino](https://emergent.sh/news/claude-reverse-engineers-1994-jeep-ecu-3)
9. [He Connected Claude and Codex to a 1994 Jeep - YouTube](https://www.youtube.com/watch?v=gMJFvLwAS5k)
11. [Claude just reverse-engineered a 1994 Jeep Cherokee — owner ...](https://www.techradar.com/ai-platforms-assistants/claude/claude-just-reverse-engineered-a-1994-jeep-cherokee-owner-combines-a-usd3-arduino-with-ai-to-help-vehicle-pass-california-emissions-test)
12. [He Let an AI Agent Hack His 32-Year-Old Jeep—Then It Took ...](https://www.motorbiscuit.com/he-let-an-ai-agent-hack-his-32-year-old-jeep-then-it-took-control/)
13. [awesome-REA-cases/cases/en/zulali-32year-jeep-claude-control ...](https://github.com/songshikang0111/awesome-REA-cases/blob/main/cases/en/zulali-32year-jeep-claude-control-report.md)
16. [Happy — Open-Source Harness for Claude Code, Codex, Grok...](https://happy.engineering/)
17. [Reverse Image Search: Free Unlimited | No Login Required](https://reverseimagesearcher.com/)