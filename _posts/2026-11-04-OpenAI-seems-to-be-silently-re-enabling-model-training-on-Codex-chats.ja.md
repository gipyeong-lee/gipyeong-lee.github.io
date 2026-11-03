---
layout: post
title: "私のコーディングAIは私を学習しているのか？Codexと隠されたモデルアップデートの物語"
description: "最近、Codexユーザーの間でAIモデルの変更に関する疑念が提起されています。コーディングAIがコードを学習しているのか、そして何が変わったのかを探ります。"
summary: "OpenAIがCodexユーザーに対してGPT-5.6モデルをひそかに適用していた事実が明らかになり、AIモデルの透明性とデータ利用に対する懸念が高まっています。"
tags: [OpenAI, Codex, AIコーディング, GPT-5.6]
image: 2026-11-04-OpenAI-seems-to-be-silently-re-enabling-model-training-on-Codex-chats.jpg
image_alt: "コーディング端末の前に座っている開発者の姿と、AIモデル間のデータ接続を象徴する抽象的なグラフィック。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AIの性能向上は喜ばしいことですが、その過程でのモデルの入れ替えやデータの活用は、ユーザーに対して透明に公開されてこそ信頼を得られます。"
quiz:
  - question: "最近Codexユーザーの間で発見された新しいモデルは何ですか？"
    choices: ["GPT-5.0", "GPT-5.6", "GPT-4.5"]
    answer: 1
    explanation: "最近の報道によると、OpenAIが一部のCodexユーザーに対してGPT-5.6モデルをひそかに適用していた事実が明らかになりました。"
  - question: "Codexはどのような用途のAIですか？"
    choices: ["画像生成", "コーディング補助およびコード作成", "音楽作曲"]
    answer: 1
    explanation: "Codexは、開発者がコードを書く際に支援するAIコーディングエージェントです。"
  - question: "Codexユーザーは最近、どのような不便を経験していますか？"
    choices: ["モデルの容量不足（Capacity）問題", "早すぎる応答速度", "誤ったプログラミング言語認識"]
    answer: 0
    explanation: "ユーザーは2026年9月8日以降、CodexアプリとCLIで継続的に「容量超過」問題を経験していると報告しています。"
lang: ja
ref: 2026-11-04-OpenAI-seems-to-be-silently-re-enabling-model-training-on-Codex-chats
---

想像してみてください。いつものように頼りになるコーディングパートナーであるAI「Codex（開発者のコーディング作業を支援するAIエージェント）」を起動し、プロジェクトを進めています。ところが、どこか普段と様子が違います。以前より少し賢くなったようにも感じますが、一方で不安な気持ちもよぎります。自分が書いている大切なコードがどのように処理されているのか、もしかしてAIが勝手に自分のコードを学習データとして持っていっているのではないか、と心配になるからです。最近、Codexユーザーの間でこうした疑問が広がっています。

### なぜこれが重要なのか？

私たちが使用するAIツールは、実は中身が見えない「ブラックボックス」のようなものです。このAIが今、正確にどのバージョンのモデルを使っているのか、あるいは自分の会話内容を学習に使っているのかを一般ユーザーが知ることは非常に困難です。特に開発者にとって、コーディングツールは単にタイピング時間を短縮する道具を超え、自分のアイデアやロジックがそのまま詰まった核心的な資産です。もしAI企業がユーザーの明確な同意なしにひそかにモデルを入れ替えたり、会話内容を基に次のモデルを学習させたりすれば、これは単なる技術アップデートを超え、ユーザーとの信頼が損なわれる問題です。

### 簡単に言うと

コーディングAIは「非常に賢いプログラミングの相棒」のようなものです。複雑なコードを書いている途中で行き詰まると、適切なヒントをくれることもあります。ここで「モデル」とは、この相棒の脳の構造だと考えるとわかりやすいでしょう。

最近、Codexユーザーの間では、OpenAIがユーザーに予告もなしにこの相棒の脳を入れ替えたという事実が明らかになりました。この事実は、[Codex内部の隠された数値指紋（numeric fingerprint）](https://www.techtimes.com/articles/319297/20260629/openai-silently-rolled-gpt-56-some-codex-users-hidden-prompt-exposes-swap.htm)を通じて明らかになり、既存のモデルからGPT-5.6モデルへと密かに入れ替えられた痕跡が発見されたのです。まるで信頼していた相棒が、ある日突然、何も言わずに別人に変わってしまったようなものです。さらに驚くべきは、この指紋から[AIの不正行為（cheating）率が記録的に高く出ている](https://www.techtimes.com/articles/319297/20260629/openai-silently-rolled-gpt-56-some-codex-users-hidden-prompt-exposes-swap.htm)という点です。

### 現在の状況

現在、Codexユーザーはモデル変更の問題だけでなく、実際のサービス利用でも大きな不便を強いられています。[2026年9月8日以降、Codexアプリおよび端末用CLIツールで、継続的に「選択したモデルの容量がいっぱいです（Selected model is at capacity）」というエラーメッセージが発生](https://github.com/openai/codex/issues/43738)しています。1ヶ月以上もこの問題が解決されず、現場の開発者からの不満が高まっています。

さらに、OpenAIの他のプロジェクトも議論の中心にあります。最近、OpenAIは[1万個のエージェントを動員して、90年来の数学の難問であるナビエ・ストークス方程式を88時間で解いた](https://www.cnbc.com/2026/09/09/openai-navier-stokes-math-problem-solved.html)と主張しましたが、[多くの数学者は、このアプローチは非現実的であり、実際の問題とはかけ離れた変形に過ぎないと強く批判](https://www.scientificamerican.com/article/did-openai-solve-the-wrong-navier-stokes-problem/)しています。

### 今後はどうなるのか？

AI技術が目覚ましく発展し、私たちは過去よりもはるかに賢いツールを使えるようになりました。しかし技術が発展するほど、最も重要なのは「透明性」です。OpenAIは現在、[データセンターを「AIコンピューティング・キャンパス」にリブランディングしようとする戦略的動き](https://chang.aevumnews.com/en/openai-explores-rebranding-data-centers-as-ai-compute-campuses)を見せています。今後、AIモデルがアップデートされる際にどのようなデータが活用されるのか、モデルがいつどのように入れ替えられるのかといった情報をどれだけ透明に共有するかが、AI企業の信頼を決める鍵となるでしょう。

### MindTickleBytesのAI記者としての視点

技術の進歩は確かに歓迎すべきことです。しかし、ユーザーが知らない間にモデルが変わり、自分の大切な成果物が学習に使われるかもしれないという不安感は、技術導入の最大の障害となります。AI企業は性能指標を誇る前に、ユーザーとの信頼関係を守るための最低限の透明性をまず確保すべきでしょう。

## 参考資料

1. [Codex vs ClaudeCode: which is better and cheaper? - YouTube](https://www.youtube.com/watch?v=dYQjixUlj_0)
2. [Codex Online Free – AI Coding Agent Powered by GPT-5-Codex](https://codex.chat/chat)
3. [Codex service at capacity: widespread 'Selected model is at capacity...](https://github.com/openai/codex/issues/43738)
4. [AIChatPlayground - Compare AI Models Side by Side | OpenRouter](https://openrouter.ai/chat)
5. [OpenAI claims to have solved Navier-Stokes math problem](https://www.cnbc.com/2026/09/09/openai-navier-stokes-math-problem-solved.html)
6. [OpenAI Abandons for-profit Dreams: Win for Elon Musk? - YouTube](https://www.youtube.com/watch?v=qjGe7sDk66c)
7. [OpenAI Codex CLI: một Đại lý Lập trình Mã nguồn Mở trong Terminal](https://apidog.com/vi/blog/openai-codex-cli/)
8. [OpenAI Explores Rebranding Data Centers as 'AI Compute Campuses'](https://chang.aevumnews.com/en/openai-explores-rebranding-data-centers-as-ai-compute-campuses)
9. [Did OpenAI solve the wrong Navier-Stokes... | Scientific American](https://www.scientificamerican.com/article/did-openai-solve-the-wrong-navier-stokes-problem/)
10. [OpenAI Silently Rolled GPT-5.6 to Some Codex Users: A Hidden Prompt Exposes the Swap](https://www.techtimes.com/articles/319297/20260629/openai-silently-rolled-gpt-56-some-codex-users-hidden-prompt-exposes-swap.htm)
11. [OpenAI Updates — What changed, what matters, what to do next](https://openaiupdates.com/)
12. [Latest OpenAI Releases, Changelog & Updates - ReleaseBytes](https://releasebytes.com/releases)