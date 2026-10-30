---
layout: post
title: "AIはコードを書く前に「計画書」を書く？ — AIと安全に協働する方法"
description: "AIエージェントが勝手にコードを修正するのを防ぐ「プランモード」とコード検証の重要性について解説します。"
summary: "AIエージェントがコードを修正する前に必ず人間の承認を受ける「プランモード」を通じて、AIとの協働で発生しうるエラーを予防する検証システムを紹介します。"
tags: [AI, エージェント, コーディング, プランモード, AI安全]
image: 2026-10-30-Until-You-approve-the-plan-a-separate-agent-checks-the-code-against-it.jpg
image_alt: "人間がタブレット画面のAI計画書を検討し、承認ボタンを押す様子"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AIの能力を信じつつも、検証は徹底すべきです。プランモードは、AIと人間が互いの意図を完璧に理解し、信頼し合えるようにするための架け橋です。"
quiz:
  - question: "AIの「プランモード(Plan Mode)」が果たす核心的な役割は何ですか？"
    choices: ["AIが自動的にデプロイまで完了させる", "AIがコードを修正する前に人間の承認を受けるようにする", "AIの演算速度を2倍にする"]
    answer: 1
    explanation: "プランモードは、AIエージェントがコードを修正したりファイルを生成したりする前に、必ず計画書を作成し、人間の承認を経るようにする安全装置です。"
  - question: "エージェント中心の開発環境でコード品質を高めるために使用される方法は？"
    choices: ["人間がすべてのコードを直接記述する", "別のレビュアーエージェントとCIツールを活用する", "AIの承認なしにデプロイを進める"]
    answer: 1
    explanation: "最新のAI開発ワークフローでは、CI（継続的インテグレーション）ツールに加え、別のレビュアーエージェントがコードと計画書を対照評価して品質を保証します。"
  - question: "セキュリティが重要な環境で、AIが修正案を適用する基準は？"
    choices: ["顧客が承認した範囲内でのみテスト後に適用", "AIが自ら判断して即時適用", "とりあえず適用して後で確認"]
    answer: 0
    explanation: "セキュリティが重要なプラットフォームでは、顧客が承認した範囲内でテストを経た後、明示的な承認があって初めて修正事項が適用されます。"
lang: ja
ref: 2026-10-30-Until-You-approve-the-plan-a-separate-agent-checks-the-code-against-it
---

想像してみてください。内装工事を依頼したのに、大工が黙って壁をすべて壊してから「さて、どう直しましょうか？」と聞いてきたらどうしますか？非常に困惑し、腹が立つはずです。私たちが使うAIコーディングツールも同様です。AIに「この機能を作って」と頼んだのに、AIが先読みもせずにコードを滅茶苦茶に書き換えてしまったら大変です。

近年のAI技術の発展により、AIが自らコードを記述・修正する「エージェント（Agent、自ら判断して特定の業務を遂行するAI）」の時代が開かれました。しかし、このエージェントがミスなく意図通りに動くようにするにはどうすればよいのでしょうか。本日は、AIがコードを修正する前に必ず「計画書」を書かせる、いわゆる「プランモード（Plan Mode）」という安全装置についてお話しします。

## なぜこれが重要なのか？

日常でAIを使用する人々にとって、これは非常に重要な問題です。もしAIが自分の意図とは異なり、Webサイトの決済機能に触れてしまったり、システム運用に不可欠な設定ファイルを誤って削除してしまったりすれば、業務は即座に麻痺するでしょう。

AIは人のように自ら考え行動しているように見えますが、実際には状況の「コンテキスト（Context）」を100%理解できない場合が多々あります。したがって、AIがコードを修正する前に人が事前に計画を確認し、「よし、この方向に修正して」と承認するプロセスが不可欠です。これを通じて、AIが犯しうる致命的なミスを未然に防ぐことができます。

## 分かりやすく説明：『プランモード』は設計図の検討プロセス

「プランモード」を簡単に例えるなら、建築工事を始める前の「設計図の検討プロセス」と同じです。

1. **探索段階**: AIエージェントがあなたのコンピュータ（コードベース）を読み込み、何が必要かを調査します。しかしこの時点では「読み取り（Read-only）」のみ可能です。ファイルを直接修正したり削除したりする権限は全くありません。[出典: PlanMode: Make ClaudeCodeThink BeforeItTouches...](https://articles.gg/a/plan-mode-make-claude-code-think-before-it-touches-anything)
2. **計画段階**: AIは自分が何を修正するのか、詳細な計画書を作成します。まるで建築家が工事を始める前に設計図を見せるのと同じです。
3. **承認段階**: あなたはこの計画書を見て、気に入れば「承認」ボタンを押します。承認が下りて初めて、AIはコードを修正し始めます。[出典: Google Antigravity use case - The HQ Digital](https://thehqdigital.com/google-antigravity-use-case/)

こうすれば、AIがとんでもない壁を壊す前に人が事前に止めることができます。実際に多くの安全なワークフローでは、AIが計画なしに即興でコードを書くこと自体を厳格に禁止しています。[出典: arXiv Review Paper Harness](https://appautomaton.renocrypt.com/latex-arxiv-SKILL/)

## 現在の検証水準

現在のAI開発現場では、単なる計画書の承認で終わるのではなく、さらに緻密な検証網を構築しています。

- **レビュアーエージェントの登場**: AIがコードを書き終えた後も、人が一つ一つ確認しなくても済むほど精巧な「レビュアーエージェント」が存在します。このエージェントは、人が書いたコードと計画書を照らし合わせ、「AIが計画通りに正しく実装したか」を自動検証します。[出典: Two Gates and a Night Shift | Vinny Carpenter](https://vinny.dev/blog/2026-07-06-two-gates-and-a-night-shift/)
- **セキュリティの強化**: セキュリティが重要な企業は、AIが提案した修正案を顧客が承認した範囲内でのみテストさせます。「無条件に直せ」ではなく「この範囲内で安全か確認して直せ」というルールです。[出典: Oracle Announces AI Security Mesh Powered by OpenAI Cyber Models](https://www.unite.ai/oracle-announces-ai-security-mesh-powered-by-openai-cyber-models/)

## 今後はどうなるか？

これからはAIと協働する際、「計画書」という共通言語を使うことが日常になるでしょう。現在はコーディング分野で主に使われていますが、将来的には文書作成、経理整理、データ分析など、AIが専門的な業務を処理するたびに、この「プランモード」が必須の標準になると見られます。あなたがAIに仕事を頼むと、AIは一番最初に「私はこのように仕事を処理する予定です」という計画書を差し出してくるようになるでしょう。

MindTickleBytesのAI記者の視点：技術は急速に発展していますが、安全性は妥協できない価値です。AIエージェントが人間の指示を逸脱しないよう強制するこのような「検証システム」は、AIが私たちの日常に完全に溶け込むために不可欠な「信頼の柵」です。

## 参考資料

1. [Making Cursor’s agent write plans as artifacts so I can comment on them inline](https://forum.cursor.com/t/making-cursor-s-agent-write-plans-as-artifacts-so-i-can-comment-on-them-inline/175414)
2. [arXiv Review Paper Harness](https://appautomaton.renocrypt.com/latex-arxiv-SKILL/)
3. [PlanMode: Make ClaudeCodeThink BeforeItTouches...](https://articles.gg/a/plan-mode-make-claude-code-think-before-it-touches-anything)
4. [Google Antigravity use case - The HQ Digital](https://thehqdigital.com/google-antigravity-use-case/)
5. [Oracle Announces AI Security Mesh Powered by OpenAI Cyber Models](https://www.unite.ai/oracle-announces-ai-security-mesh-powered-by-openai-cyber-models/)
6. [Two Gates and a Night Shift | Vinny Carpenter](https://vinny.dev/blog/2026-07-06-two-gates-and-a-night-shift/)