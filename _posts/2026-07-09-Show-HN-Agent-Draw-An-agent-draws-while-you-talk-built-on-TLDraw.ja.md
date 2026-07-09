---
layout: post
title: "私が話す通りに絵を描く？AIとリアルタイムで共同作業する「エージェント・ドロー（Agent Draw）」"
description: "AIに話しかけるだけで、無限キャンバス上でリアルタイムに絵を描いてくれるエージェント・ドローというツールと、その仕組みについて解説します。"
summary: "エージェント・ドローは、AIエージェントがユーザーの音声命令を理解し、無限キャンバス上で直接リアルタイムに絵を描いたり図形を配置したりできるインタラクティブなツールです。"
tags: [AI, エージェント, tldraw, クリエイティビティ, ツール]
image: 2026-07-09-Show-HN-Agent-Draw-An-agent-draws-while-you-talk-built-on-TLDraw.jpg
image_alt: "無限キャンバス上でAIがリアルタイムに絵を描いているエージェント・ドローのインターフェース画面。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "単なる画像生成を超えて、AIが「キャンバス」という空間の中でユーザーと物理的に相互作用する第一歩です。"
quiz:
  - question: "エージェント・ドローがベースとしている技術は何ですか？"
    choices: ["Figma", "TLDraw SDK", "Adobe Photoshop"]
    answer: 1
    explanation: "エージェント・ドローは、Reactベースの無限キャンバスSDKであるtldrawを基盤として構築されています。"
  - question: "ユーザーがエージェントに命令を伝える方法は何ですか？"
    choices: ["専用キーボード入力", "右側のチャットパネルを通じた音声およびテキスト対話", "画像ファイルのアップロード"]
    answer: 1
    explanation: "画面右側のチャットパネルを通じて、ユーザーが音声やテキストでエージェントと対話し、コンテキストを追加できます。"
  - question: "エージェント・ドローは複数のリクエストをどのように処理しますか？"
    choices: ["ランダムな順序で処理", "FIFO（先入れ先出し）キューを用いたステートマシン処理", "すべてのリクエストを同時に並列処理"]
    answer: 1
    explanation: "複数のリクエストが入力された場合、FIFO（First-In, First-Out）キューとステートマシンを使用し、一度に一つのセッションを順次処理します。"
lang: ja
ref: 2026-07-09-Show-HN-Agent-Draw-An-agent-draws-while-you-talk-built-on-TLDraw
---

想像してみてください。白紙を前にして「ここに美味しそうなピザを描いて」と言うと、目の前でAIが線を引いてチーズやペパロニを描き始める様子を。まるで魔法のようなこの光景が、今や日常になろうとしています。最近発表された「エージェント・ドロー（Agent Draw）」は、私たちがAIと協働するスタイルを根本から変えようとしています。

### なぜこのツールが注目されるのか？

これまで、AIに絵を描いてもらう際は、プロンプトを入力してしばらく待った後、完成品を「受け取るだけ」というのが一般的でした。つまり、AIは一方的に結果を投げかけてくる存在に近いものでした。しかし、エージェント・ドローは全く違います。キャンバス上でユーザーと絶えずコミュニケーションを取りながら、リアルタイムに絵を描き進める「共同作業」のプロセスを見せてくれるからです [出典 2](https://www.youtube.com/watch?v=iIH2hJAxxm8)。

これは、クリエイティブな作業がもはや一人きりのプロセスではないことを意味します。会議室のホワイトボードの前で同僚とアイデアを出し合いながら絵を完成させるように、AIと人間が同じ空間で意見を交わしながら作業できるようになったのです。AIは単に結果を生成する「ツール」を超え、キャンバスの前に並んで立つ能動的な「パートナー」へと進化しています [出典 13](https://gitnation.com/contents/agents-on-the-canvas-with-tldraw)。

### どのような仕組みで動いているのか？

エージェント・ドローの動作原理は非常に緻密です。例えるなら、自分で描かなくても自分の手の延長となって代わって描いてくれる「賢いAIロボットアーム」がキャンバスの上にあるようなものだと考えると分かりやすいでしょう。

1. **無限のキャンバス（tldraw SDK）**: 基盤となるキャンバス環境です。Reactベースの無限キャンバスSDK「tldraw」を使用し、AIが自由に図形を配置したり絵を描いたりできる空間を確保しています [出典 1, 出典 15](https://tldraw.dev/blog/tldraw-mcp-app)。
2. **エージェント・スターターキット（基本学習プロセス）**: AIに絵を描く方法や図形を扱う方法を教える、いわば「基本動作」です。これを通じて、AIは単純な画像だけでなく、四角形、ダイヤモンド、矢印などの基本図形を認識・配置し、キャンバスの要素を細かく操作できるようになります [出典 6, 出典 12](https://github.com/tldraw/tldraw/blob/main/apps/docs/content/starter-kits/agent.mdx)。
3. **交通整理システム（ステートマシン）**: ユーザーが複数の命令を同時に出してもシステムが混乱しないように管理します。「先に入ってきた命令を先に処理する」FIFO（First-In, First-Out）キューとステートマシンにより、AIが一度に一つの作業セッションに集中し、順次解決できるよう制御されています [出典 8](https://techstackups.com/articles/tldraw-agent-draw/)。

こうしたプロセスにより、AIはユーザーが指定したキャンバスの範囲内で音声コマンドの意味を把握し、リアルタイムに図形を描き入れ、ユーザーの意図を即座に反映します [出典 2, 出典 3](https://www.youtube.com/watch?v=livloOnVpC8)。

### 現状どの程度のことができるのか？

現在エージェント・ドローは、開発者向けの公式「エージェント・スターターキット」をベースに構築されています [出典 2, 出典 5](https://memedata.com/post/130752)。ユーザーは画面右側のチャットパネルを通じてエージェントと会話します。ここで必要な背景情報を追加したり、エージェントがこれまでに行った作業履歴を確認したりしながらコミュニケーションを取ることができます [出典 6, 出典 11](https://zenn.dev/slowhand/articles/bb203aba83e385?locale=en)。

AIは基本的な図形の組み合わせや構成を非常に巧みに行います。絵を描くだけでなく、TODOリストを作成したり、修正依頼に対して即座に反映してアップデートしたりするなど、複雑な業務補助も可能です [出典 12](https://github.com/tldraw/tldraw/blob/main/apps/docs/content/starter-kits/agent.mdx)。もちろん、現在は複雑な芸術的創作よりも、体系的なダイアグラム作成やリアルタイムの視覚補助ツールとしての役割に最適化されています [出典 9, 出典 11](https://zenn.dev/slowhand/articles/bb203aba83e385?locale=en)。

### 私たちの働き方はどう変わるのか？

エージェント・ドローの登場は、そう遠くない未来に私たちがどのようにAIと働くことになるのかを示す小さな予告編です。今後、AIエージェントはキャンバスの上でより深い推論を行い、ユーザーの微細な意図まで汲み取って自ら図面を修正したり、アイデアを提案したりするレベルへと発展していくでしょう。

私たちはまもなく、AIが単に止まった画像を作るだけでなく、キャンバスという物理空間で私たちと一緒に悩み、描いてくれる「真の視覚的パートナー」を側に置くことになるはずです。これからの画面上のキャンバスは、単なるお絵描きボードではなく、人間とAIがリアルタイムに思考を重ねる新たな共同作業の場となるはずです。

---

### MindTickleBytesのAI記者視点
これまで絵を描いてくれるAIは数多くありましたが、「キャンバス」という空間を理解し、ユーザーと相互作用しながら結果をビルドアップしていくAIは稀でした。AIが私たちの思考と共に呼吸し、何かを完成させていくプロセスそのものが、クリエイティブ体験の本質を変えています。

## 参考資料

1. [Show HN: Agent Draw: An agent draws while you talk, built on TLDraw](https://news.ycombinator.com/item?id=48805475)
2. [Agent Draw — Speak, and an AI Agent Draws It Live on Canvas](https://www.youtube.com/watch?v=iIH2hJAxxm8)
3. [Agent Draw: drag a box, speak, an AI agent draws inside it](https://www.youtube.com/watch?v=livloOnVpC8)
4. [Agent Draw: An agent draws while you talk, built on TLDraw](https://vuink.com/post/grpufgnpxhcf-d-dpbz/articles/tldraw-agent-draw)
5. [Show HN：Agent Draw，基于 TLDraw 构建，在你说话时自动绘图。](https://memedata.com/post/130752)
6. [GitHub - tldraw/agent-template: Enable AI agents to interpret ...](https://github.com/tldraw/agent-template)
7. [Better HN - bhn.vercel.app](https://bhn.vercel.app/show)
8. [Agent Draw: An agent draws while you talk, built on TLDraw | Tech Stackups](https://techstackups.com/articles/tldraw-agent-draw/)
9. [Agent starter kit • tldraw Docs](https://tldraw.dev/starter-kits/agent)
10. [Starter kits • tldraw Docs](https://tldraw.dev/starter-kits)
11. [tldraw × AI Agent: Exploring the Mechanics with the Agent Starter Kit](https://zenn.dev/slowhand/articles/bb203aba83e385?locale=en)
12. [tldraw/apps/docs/content/starter-kits/agent.mdx at main · tldraw/tldraw](https://github.com/tldraw/tldraw/blob/main/apps/docs/content/starter-kits/agent.mdx)
13. [Agents on the Canvas With tldraw by Max Drake](https://gitnation.com/contents/agents-on-the-canvas-with-tldraw)
14. [Build a Real-Time tldraw Whiteboard with Velt Comments inside ChatGPT🤯🔥 - DEV Community](https://dev.to/astrodevil/build-a-real-time-tldraw-whiteboard-with-velt-comments-inside-chatgpt-1dhe)
15. [tldraw MCP App: Letting your agents draw](https://tldraw.dev/blog/tldraw-mcp-app)
16. [Show | Hacker News - nhn.yuu.is](https://nhn.yuu.is/show)