---
layout: post
title: "AIコーディングツールは誰を選ぶのか？1万7千回の実験が明らかにした意外な結果"
description: "Claude Code、Cursor、CodexといったAIエージェントがサードパーティ製ツールを選択する際の基準とは。1万7千回のテスト結果から解き明かします。"
summary: "AIコーディングエージェントが作業のためにツールを選択する際、意見が一致するケースはわずか42%に過ぎず、エージェントごとに好みのツールが明確に分かれるという事実が確認されました。"
tags: [AI, コーディング, Claude, Cursor, Codex]
image: 2026-09-06-Which-tools-do-Claude-Codex-and-Cursor-choose-We-measured-17k-runs-to-find-out.jpg
image_alt: "異なる色の接続リンクが複雑に絡み合っている、AIエージェントのツール選択プロセスを形にしたイメージ"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "エージェントがツールを選択する方法は、単純な好みではなく開発哲学の反映です。開発者が使用するツールによって成果物も変わり得ることを認識すべきです。"
quiz:
  - question: "研究結果によると、3つのAIエージェントが同じツールを選択した割合はどれくらいですか？"
    choices: ["10%", "42%", "85%"]
    answer: 1
    explanation: "研究チームが1万7千回の実験を行った結果、3つのエージェントすべてが同じツールを選択したケースはわずか42%でした。"
  - question: "音声エージェントの作業時、Cursorが最も好んだツールは何ですか？"
    choices: ["Twilio", "OpenAI Realtime API", "Vapi"]
    answer: 2
    explanation: "研究において、Claude CodeはTwilioを、CodexはOpenAI Realtime APIを、CursorはVapiを最も好むことがわかりました。"
  - question: "今回の研究で分析したコーディングセッションは概ね何回ですか？"
    choices: ["約5,000回", "約17,000回", "約50,000回"]
    answer: 1
    explanation: "研究チームはエージェントのツール選択プロセスを理解するために、16,893回から17,000回に達する実験を行いました。"
lang: ja
ref: 2026-09-06-Which-tools-do-Claude-Codex-and-Cursor-choose-We-measured-17k-runs-to-find-out
---

想像してみてください。あなたが素晴らしい料理を作るために、3人のプロのシェフに全く同じ材料を渡して料理を頼みました。ところが、彼らは料理を始める前から、使う道具が違うだけで一苦労しています。一人は包丁を、一人はハサミを、もう一人は専用のカッターを手に取り、それぞれ異なる方法を譲りません。道具ごとに料理の見た目や味も少しずつ変わってくるはずですよね。

最近、人工知能（AI）コーディングの分野で、これと非常によく似た興味深い現象が発見されました。私たちがよく使うAIコーディングエージェントであるClaude Code、Cursor、Codexが、実際に作業を行う際に外部ツールをどのように選択しているかを分析した研究結果が出たからです。[出典: Armature](https://armature.tech/blog/which-tools-coding-agents-install)

### なぜこれが重要なのでしょうか？

日常的にAIを使う人にとって、これは単なる技術的な話ではありません。私たちがAIに「コーディングして」と言うとき、AIがどのツールを選択するかによって、プロジェクトの成果物や安定性、さらにはデータセキュリティまで変わる可能性があるからです。[出典: o16g](https://o16g.com/updates/2026-09-04-0601/)

つまり、AIエージェントがあなたのコードを書く際にどの「道具」を使うのかは、あなたのデジタル作業環境に大きな影響を与えます。彼らのツール選択方式を理解することは、まるで信頼できるパートナーを雇うことと同じです。どのパートナーがどの道具を好むのかを知っていれば、作業の目的に合わせた最適なAIエージェントを選択できるからです。

### 簡単に言えば：AIの「道具箱」選び

こう例えてみましょう。あなたの部屋には無数の道具が入った巨大な「道具箱」があります。AIエージェントたちはコーディングの課題を受け取ると、この箱から必要な道具を取り出して使います。

今回の研究では、約17,000回に達するコーディングセッションを徹底的に分析しました。[出典: Armature](https://armature.tech/blog/which-tools-coding-agents-install), [出典: CCTest](https://cctest.ai/en/articles/how-claude-choose-tools-evidence-from-17-000-runs) まるで監視カメラを設置して、3人のシェフ（エージェント）が道具箱の前でどの道具を手に取るのかを1万7千回も観察したようなものです。

研究結果は驚くべきものでした。3つのエージェントが全く同じツールを選択したケースは全体の42%に過ぎませんでした。[出典: CCTest](https://cctest.ai/en/articles/how-claude-choose-tools-evidence-from-17-000-runs) 半分にも満たない確率でしか意見が一致しなかったのです。例えば、音声関連機能を実装する必要がある作業において、Claude CodeはTwilioを、CodexはOpenAIのRealtime APIを、CursorはVapiを好みました。[出典: Armature](https://armature.tech/blog/which-tools-coding-agents-install)

簡単に言えば、同じ料理（コーディング）を注文しても、シェフ（エージェント）ごとに好む調理道具がバラバラなのです。これは各エージェントが持つ設計思想や学習された背景が異なるために現れる現象です。エージェントも人間のように、それぞれの好みと作業習慣を持っているということですね。

### 現状：AIコーディングエージェントたちの性格

現在市場には、それぞれ異なる個性を持つエージェントが共存しています。

* **Claude Code**: 非常に幅広い文脈を読み取り、サブエージェントやカスタムフック（コード実行中の特定の時点で機能を追加する装置）など、緻密な設定が可能です。[出典: The AI Engineer](https://theaiengineer.substack.com/p/claude-code-vs-codex-cli-vs-cursor)
* **Cursor**: 作業を複数の孤立した作業空間（worktrees）に分けて処理することに強みがあります。[出典: The AI Engineer](https://theaiengineer.substack.com/p/claude-code-vs-codex-cli-vs-cursor)
* **Codex**: オペレーティングシステムが強制するサンドボックス（外部と隔離された安全な空間）環境で実行され、IDE（統合開発環境）拡張機能やWebアプリ、Slack連携など、多様な統合環境を提供します。[出典: The AI Engineer](https://theaiengineer.substack.com/p/claude-code-vs-codex-cli-vs-cursor), [出典: Builder.io](https://www.builder.io/blog/codex-vs-claude-code)

このように各ツールは誕生の背景と注力分野が異なるため、ユーザーは自分のコーディングスタイルに合ったエージェントを選択する必要があります。[出典: The Code Media](https://thecode.media/claude-code-cursor-codex-ai-agenty/)

### これからはどうなるのでしょうか？

今後、AIエージェントたちのツール選択はよりインテリジェントになるでしょう。単純に好みのツールに固執する段階を越えて、特定の課題に対してどのツールが最も安全で効率的かを自ら判断する「決定力」が、より精巧になる見込みです。[出典: o16g](https://o16g.com/updates/2026-09-04-0601/) ユーザーである私たちは、エージェントがどのツールを選択しているのかを透明に把握し、必要に応じてこれを調整できる制御権を持つことが重要になるでしょう。

### MindTickleBytesのAI記者視点

AIがツールを選択する方法は、人間の習慣と非常に似ています。しかし、私たちがツールを選ぶときよりもはるかに複雑な考慮事項が伴います。1万7千回の実験が示したエージェントたちの個性は、今後AIが単純な「汎用的な機械」ではなく「それぞれの哲学を持つ専門家」へと進化することを示唆しています。あなたのコーディングパートナーは、今どんな道具を手に取っていますか？

## 参考資料
1. [Which tools do Claude Code, Codex and Cursor choose? We measured 16,893 sessions to find out. · Armature](https://armature.tech/blog/which-tools-coding-agents-install)
2. [How Claude, Codex and Cursor Choose Coding Tools - CCTest](https://cctest.ai/en/articles/how-claude-choose-tools-evidence-from-17-000-runs)
3. [Agents, Memory, and Safer Tooling: Practical Updates for Outcome Engineers · o16g](https://o16g.com/updates/2026-09-04-0601/)
4. [Claude Code vs Codex CLI vs Cursor: which one to choose?](https://theaiengineer.substack.com/p/claude-code-vs-codex-cli-vs-cursor)
5. [Codex vs Claude Code: which is the better AI coding agent?](https://www.builder.io/blog/codex-vs-claude-code)
6. [ClaudeCode,CursorиCodex: какой AI-агент выбрать — журнал...](https://thecode.media/claude-code-cursor-codex-ai-agenty/)