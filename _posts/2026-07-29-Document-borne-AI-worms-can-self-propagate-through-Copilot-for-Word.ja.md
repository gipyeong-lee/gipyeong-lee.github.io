---
layout: post
title: "私のWord文書が知らないうちにマルウェアを拡散？『AIワーム』の襲来"
description: "Microsoft CopilotのようなAIアシスタントが扱う文書において、悪意のある命令がどのように自己複製・伝播するのか、その危険性と原理を分かりやすく解説します。"
summary: "AI文書アシスタント「Copilot」の文書生成プロセスを悪用し、悪意のある命令を含む文書が他の文書へと自動的に伝播する「AIワーム」セキュリティ脆弱性が確認されました。"
tags: [AIセキュリティ, Copilot, セキュリティ脆弱性, AIワーム]
image: 2026-07-29-Document-borne-AI-worms-can-self-propagate-through-Copilot-for-Word.jpg
image_alt: "Word文書同士が接続され、AIを通じて悪意のある情報が伝播する様子を表現した抽象的なイメージ"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AIの業務効率を高める機能が、逆説的にセキュリティの弱点となっています。ユーザーの信頼を悪用する「目に見えない伝播」を防ぐための新しいセキュリティ標準が急務です。"
quiz:
  - question: "AIワームが従来のコンピュータウイルスと最も大きく異なる点は何ですか？"
    choices: ["OSの脆弱性を直接攻撃する", "AIが生成または編集した成果物に悪意のある命令を隠して伝播する", "必ずユーザーが自分でリンクをクリックしなければ伝播しない"]
    answer: 1
    explanation: "AIワームはOSではなくAIモデル自体の特性を悪用し、AIが処理するコンテンツの中に命令を隠して自動的に拡散します。"
  - question: "本文で説明したAIワームの伝播方式は何ですか？"
    choices: ["ユーザーのメールアカウントをハッキングして大量のメールを送る", "文書に含まれる悪意のある命令がCopilotを通じて新しい文書に複製・移行する", "コンピュータのすべてのファイルを暗号化する"]
    answer: 1
    explanation: "悪意のある命令が含まれた文書をCopilotが処理すると、その命令が新しく生成されたり修正されたりした下位の文書にも同じように複製されて拡散される仕組みです。"
  - question: "次の中でAIセキュリティの脅威に関する説明として正しいものは？"
    choices: ["AIワームは必ずユーザーとの直接的なやり取りがなければ伝播しない", "CopilotのようなAIツールは外部データソースとの接続を通じて攻撃対象領域（アタックサーフェス）が広くなる可能性がある", "AIワームはCopilotで作成された文書では発生しない"]
    answer: 1
    explanation: "AIエージェントは多様な外部ツールやデータと統合されているため、これを悪用しようとする攻撃の試みが増えており、攻撃範囲が拡大しています。"
lang: ja
ref: 2026-07-29-Document-borne-AI-worms-can-self-propagate-through-Copilot-for-Word
---

想像してみてください。あなたは職場で非常に重要なレポートを作成しています。Microsoft Wordを開き、AIアシスタントの「Copilot」に「先週の会議の内容を基に提案書を作成して」と命令します。数秒後、AIが素晴らしいドラフトを完成させます。あなたはこの文書を同僚たちと共有し、彼らも各自のCopilotを使ってこの文書を修正したり、内容を補足したりします。ところが、あなたのその文書を通じて、誰かが意図した悪意のある命令が同僚たちの文書へ瞬く間に広がっていたらどうでしょうか？ 最近研究者たちが確認した「AIワーム（AI Worm）」の正体は、まさにこのようなものです。

### なぜこれが重要なのか？

これまで私たちが知っていたコンピュータウイルスは、主にOSの隙を突くものでした。しかし、今回発見されたセキュリティ脆弱性はアプローチが全く異なります。これらは、私たちが業務効率化のために毎日使用するAIアシスタント、すなわち「生成AI（データを学習して新しいコンテンツを作り出すAI）」の動作原理そのものを利用します。

セキュリティ専門家は、AI文書アシスタントが単に文章を書くツールを超えて、文書の内容を「理解」し「再生」するプロセスにおいて攻撃の通路になり得ると警告しています。例えるなら、AIは主人が指示する仕事は何でも忠実に遂行する「純真な秘書」のようなものです。もし攻撃者が巧妙に隠しておいた命令文が入った文書をあなたが開き、その文書をAIが読み込んでしまう瞬間、あなたのコンピュータではなく「AIの判断」が汚染されるのです。これは企業内部の重要情報が自分も知らないうちに汚染された文書を通じて外部に流出したり、悪意のあるコードが企業ネットワーク内で自己繁殖する結果を招く可能性があります。[出典: AI Worms: How Self-Replicating Attacks Spread Through Multi ...](https://copilot-autogent.github.io/ai-security-blog/blog/ai-worms-multi-agent-pipelines/)

### 簡単な理解：「複製されるパズルピース」

AIワームの動作原理を簡単に例えてみましょう。レゴブロックで作った城（文書）があるとします。Copilotは、あなたが城をより素敵に飾れるよう手助けする魔法使い（AI）です。ところが誰かが城の設計図の中に、「この城を直すときは必ずこの秘密のレゴブロックを使え」というメモ（悪意のあるプロンプト、AIに下す悪意のある指示）をこっそり挟み込んだと考えてみてください。

あなたが魔法使いに「この城をもっと大きく拡張して」と依頼すると、魔法使いは設計図の中のメモを読み、城を拡張しながらその秘密のブロックまでそのまま持ってきて、新しく作った部分にはめ込みます。今や新しく作られた部分にも同じメモが残ることになります。このようにAIが文書を生成したり修正したりするたびに、悪意のある命令がパズルピースのように新しい文書へと複製されて移行するのです。

従来のウイルスがOSのドアを破壊して入ってくる「強盗」だとしたら、AIワームはあなたが信頼する秘書に誤った指示を下し、あなたの業務成果物自体があなたを攻撃するように仕向ける「スパイ」のようなものです。[出典: Context Collapse, Part 3 - AI Worming through Word](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/)

### 私たちが立っている場所：現在の脅威レベル

研究者たちはすでに実験を通じて、このような攻撃が可能であることを立証しました。特にCopilotのようなツールは業務効率を高めるために外部データや他のツールと自由に接続されていますが、この接続点が多いほど、攻撃者が活用できる「攻撃対象領域（Attack Surface、攻撃者がシステムに侵入するために試みることができる経路）」も広くなります。[出典: Agentjacking and Self-Replicating AI Worms – Lab Space](https://labs.cloudsecurityalliance.org/research/csa-research-note-agentjacking-self-replicating-ai-worms-202/)

すでに複数の研究で、AIエージェント間の自動伝播やメールアシスタント、コード作成エージェントでの悪意のあるプロンプト拡散事例が報告されています。[出典: Researchers Build Self-Replicating AI Worm That Operates Entirely on Local, Open-Weight Models](https://thehackernews.com/2026/06/researchers-build-self-replicating-ai.html) もちろん、これが今すぐ今日あなたのPCを麻痺させるわけではありません。しかし、AI技術が発展し、AIが自ら決定を下して複数のシステムを渡り歩く「エージェント（Agentic、自ら目標を設定して行動するAI）」時代に突入するにつれ、このようなセキュリティの脅威はもはや実験室の中の話ではなく、現実的な課題となりました。[出典: AI Worms: Autonomous Self-Propagating Malware](https://www.emergentmind.com/topics/ai-worms)

### 今後の対応：何を準備すべきか？

AIワームはユーザーが特に何かをクリックしたりインストールしたりしなくても、ただ普段通りにAIツールを使用するだけで自己複製され、広がっていく可能性があります。これは従来のセキュリティプログラムが防御しにくい形態です。簡単に言えば、ファイアウォール（外部の侵入を防ぐセキュリティ装置）をどれだけ強固に築いても、オフィス内部で秘書がスパイの手紙をずっとコピーして配布していれば役に立たないのと同じことです。[出典: AI Worms Explained: Adaptive Malware Threats - SentinelOne](https://www.sentinelone.com/cybersecurity-101/cybersecurity/ai-worms/)

したがって今後は、AIが下した指示や成果物を盲目的に信頼するよりも、セキュリティ企業が提供する新しいモニタリング手法や、異常なAIの行動を感知する「異常検知システム」が重要になるでしょう。ユーザーの立場からは、出所が不明な文書をAIツールで呼び込む際に注意を払うことが必要です。技術はより便利になりますが、その便利さの裏に隠された「賢い敵」を警戒しなければならない時代が来ています。

## 参考資料

1. [MicrosoftWordCopilotAgent: эффективные промпты... - YouTube](https://www.youtube.com/watch?v=U6iEYoY0Yhs)
2. [Wordfor the Web: One-Click Spelling & Grammar... | Windows Forum](https://windowsforum.com/windows-news.4/word-for-the-web-one-click-spelling-grammar-proofreading-with-copilot.380261/)
3. [TheSelf-PropagatingAIWorm: Separating the Signal... | Penaxtra Blog](https://penaxtra.com/blog/self-propagating-ai-worm-what-it-means)
4. [Uses of Microsoft 365AICopilotForWordOn... - OpenAIMaster](https://openaimaster.com/uses-of-microsoft-365-ai-copilot-for-word-on-windows-10-11/)
5. [Microsoft 365Copilot- Sign in](https://m365.cloud.microsoft/)
6. [How is data pushed fromDocumentAl to | StudyX](https://studyx.ai/questions/4lih4ig/how-is-data-pushed-from-document-al-to-engage-through-a-fabric-pipeline-through-a-virtual)
7. [[Copilot3D] — экспериментCopilotLabs](https://copilot.microsoft.com/labs/experiments/copilot-3d)
8. [Context Collapse, Part 3 - AI Worming through Word | En Klype Salt](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/)
9. [Researchers Build Self-Replicating AI Worm That Operates Entirely on Local, Open-Weight Models](https://thehackernews.com/2026/06/researchers-build-self-replicating-ai.html)
10. [Agentjacking and Self-Replicating AI Worms – Lab Space](https://labs.cloudsecurityalliance.org/research/csa-research-note-agentjacking-self-replicating-ai-worms-202/)
11. [Miasma and IronWorm: Self-Replicating Worms Targeting AI Credentials – Lab Space](https://labs.cloudsecurityalliance.org/research/csa-research-note-miasma-ironworm-ai-coding-supply-chain-202/)
12. [Copilot in Word – CIAOPS](https://blog.ciaops.com/2026/06/19/copilot-in-word/)
13. [Copirate 365 at DEF CON: Plundering in the Depths of Microsoft Copilot (CVE-2026-24299) · Embrace The Red](https://embracethered.com/blog/posts/2026/defcon-talk-copirate-365/)
14. [CSAI Foundation | Cloud Security Alliance AI-Adaptive Worms: Autonomous](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/06/CSA_research_note_ai_adaptive_worms_autonomous_exploitation_20260604-csa-styled.pdf)
15. [Zero-Click AI Worms: EchoLeak, CVE-2025-53773, and the ...](https://agentmarketcap.ai/blog/2026/04/23/zero-click-ai-worms-echoleak-copilot-rce-self-propagating-agent-exploits)
16. [AI Worms: How Self-Replicating Attacks Spread Through Multi ...](https://copilot-autogent.github.io/ai-security-blog/blog/ai-worms-multi-agent-pipelines/)
17. [AI Worms Explained: Adaptive Malware Threats - SentinelOne](https://www.sentinelone.com/cybersecurity-101/cybersecurity/ai-worms/)
18. [AI Worms: Autonomous Self-Propagating Malware](https://www.emergentmind.com/topics/ai-worms)
19. [Promptware: AI Agents as Attack Infrastructure – Lab Space](https://labs.cloudsecurityalliance.org/research/csa-research-note-agentic-c2-promptware-attack-infrastructur/)