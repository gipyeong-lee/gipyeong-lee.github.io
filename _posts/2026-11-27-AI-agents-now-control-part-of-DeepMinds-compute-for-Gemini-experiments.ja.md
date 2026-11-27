---
layout: post
title: "AIが自ら実験する時代：グーグル・ディープマインド、Geminiの計算資源をAIエージェントに委ねる"
description: "グーグル・ディープマインドが次世代Geminiモデルの開発に向けて、AIエージェントに計算資源の統制権の一部を譲渡しました。AIが自ら科学実験を遂行する時代の意味と安全装置について解説します。"
summary: "グーグル・ディープマインドが次世代Geminiモデルの実験のために、AIエージェントへ自社計算資源の一部を委任しました。ただし完全な自己改善はまだ遠く、人間の監督に向けて内部思考のプロセスは報酬を与えない安全装置を維持しています。"
tags: [AI, GoogleDeepMind, Gemini, AIエージェント, 技術動向]
image: 2026-11-27-AI-agents-now-control-part-of-DeepMinds-compute-for-Gemini-experiments.jpg
image_alt: "研究室のコンピューター画面の前で自律的に計算データを分析しているAIシステムの様子を具象化したイラスト"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AIが自ら実験を設計し実行することは、ツールから同僚への巨大な転換です。透明な思考プロセスの検証という安全装置が維持される限り、科学的発見のスピードは想像を絶するほど加速するでしょう。"
quiz:
  - question: "グーグル・ディープマインドがAIエージェントに委ねたものは何ですか？"
    choices: ["会社の採用権限", "次世代Gemini実験のための計算資源の一部", "グーグル検索エンジンのソースコード修正権限"]
    answer: 1
    explanation: "グーグル・ディープマインドは、次世代Geminiモデル開発のための実験を目的として、AIエージェントに自社の計算資源（compute budget）の一部を自律的に制御することを許可しました。"
  - question: "ディープマインドがAIの訓練過程において意図적으로報酬を与えないものは何ですか？"
    choices: ["コード作成速度", "内部思考プロセス（Chain of Thought）", "サーバー電力使用量"]
    answer: 1
    explanation: "ディープマインドは、AIの内部思考プロセス（Chain of Thought）を訓練中に報酬としないことで、AIの意図が自然語の状態でフィルタリングされずに維持され、人間が実行前に検証できるように安全装置を講じました。"
  - question: "ディープマインドの研究責任者であるコライ・カブクオグル（Koray Kavukcuoglu）が強調した現在のAIの状態は何ですか？"
    choices: ["完全な再帰的自己改善（Recursive Self-Improvement）はまだ遠い", "AIがすでに人間の研究員を完全に代替した", "人間の介入が一切不要な自律研究の時代が到来した"]
    answer: 0
    explanation: "研究副社長のコライ・カブクオグルは、AIが実験計算を制御し始めたものの、自らを無限にアップグレードする再帰的自己改善（RSI）の段階はまだ遠い未来であると強調しました。"
lang: ja
ref: 2026-11-27-AI-agents-now-control-part-of-DeepMinds-compute-for-Gemini-experiments
---

想像してみてください。あなたがとある巨大な研究所の総括責任者で、夜の間に人工知能の助手へと研究室のスーパーコンピューターの使用権限の一部を切り分けて渡しました。朝に出勤してみると、その人工知能が人間の研究員すら思いつかなかった斬新な仮説を立て、夜通し数千回の仮想実験を回して有意な結果まで綺麗に整理しておきました。小説の中の話のように聞こえますか？しかし今、グーグル・ディープマインド（Google DeepMind）の研究室では、実際にこれと似たようなことが起きています。

## AIが自ら研究室の鍵を握る

最近、グーグル・ディープマインドは次世代Gemini（テキスト、画像、音声など多様な形態のデータを同時に理解するグーグルの中核的大規模言語モデルシリーズ[出典：Wikipedia](https://en.wikipedia.org/wiki/Gemini_(language_model))）モデルの実験に向けて、**AIエージェント（AI Agent、自ら判断し目標を遂行する自律型人工知能プログラム）**に対し、研究室の中核資源である計算予算（compute budget）の一部を自律的に制御することを許可しました（[AI agents now control part of DeepMind's compute for Gemini experiments](https://the-decoder.com/ai-agents-now-control-part-of-deepminds-compute-for-gemini-experiments-but-recursive-self-improvement-remains-distant/)）。 

このニュースは、グーグル・ディープマインドの研究副社長（VP of Research）でありGemini開発を統括するコライ・カブクオグル（Koray Kavukcuoglu）が、公式ポッドキャスト『グーグル・ディープマインド：ポッドキャスト（Google DeepMind: The Podcast）』第35回で直接語ったことにより世に知れ渡りました（[DeepMind Agents Control Part of Gemini Training Compute](https://explainx.ai/blog/google-deepmind-gemini-agents-training-compute-koray-kavukcuoglu-november-2026)）。単に質問に答えるレベルを超え、AIが自ら実験を企画し計算を配分する主体へと昇格したという点で、技術界の注目が集まっています。

---

## なぜこれが重要なのか？

私たちのような一般の人々の日常において、このニュースはどのような意味を持つのでしょうか？核心は、**「研究と技術発展のスピードが人間のタイムテーブルから逸脱し始めた」**という点です。 

かつては、新しいAIモデルを作ったり新素材を発見したりする際、人間の科学者が自ら仮説を立ててコンピューターにコマンドを入力し、結果を待たなければなりませんでした。このプロセスは、膨大な時間とコストが消耗される退屈な反復作業の連続でした。しかし、AIエージェントが自ら計算資源を統制して実験を主導するようになれば、人類が新しい知識を発見し技術を革新するスピードが想像を絶するほど加速する可能性があります。

実際にグーグル・ディープマインドは、こうした自律エージェントシステム（例えばCo-Scientistシステム）を通じてすでに膨大な成果を上げています。新素材の合成から医療用AIアーキテクチャの自律的開発に至るまで、多様な科学分野で実験的に検証された成果物を首尾よく導き出してきました（[Google Deepmind's AI Co-Scientist now plans experiments, runs ...](https://the-decoder.com/google-deepminds-ai-co-scientist-now-plans-experiments-runs-lab-equipment-and-writes-scientific-papers/)）。さらには、AIエージェントが人間の研究員の監督のもと、旧式RSA暗号方式の脆弱性を従来方式よりも最大1,600倍速い速度で発見する技術を突き止めたこともあります（[Google DeepMind finds 1,600x faster way to expose encryption flaws](https://interestingengineering.com/ai-robotics/google-deepmind-agents-expose-older-encryption-flaws)）。 

つまり、今回の措置は、こうした実験的成功が単発のイベントにとどまらず、グーグルの中核AIモデルであるGeminiの開発プロセス全体の標準運用方式へと深く組み込まれたことを意味します。

---

## わかりやすい解説：「スーパーインターン」に法人カードを渡したようなもの

この複雑な状況をわかりやすく理解するために、日常的な例えを挙げてみましょう。 

非常に有能だがまだ正式な社員ではない「スーパーインターン」を1人採用したと想像してみてください。これまでこのインターンは、先輩に言われた単純な文書作成や資料調査を行っていました。しかし、代表が決断を下し、このインターンに**「会社の法人カードの一部を渡すから、君自身が必要だと思う市場調査プロジェクトを夜の間に思い切り回してみろ」**と権限を委譲したのです。 

インターン（AIエージェント）は、与えられた予算（計算資源）の中でどのテーマを把握すべきかを自ら決定し、夜通しコンピューターを回してデータを分析した後、朝にレポートを提出します。これがまさに今回のGeminiの実験においてディープマインドが試みていることです。

しかし、ここで重要な疑問が生じます。「インターンが自律的に権限を使い始めたら、統制を外れて勝手に暴走しないのだろうか？」

ディープマインドの研究陣はこの点を正確に見抜き、非常にユニークな安全装置を講じました。人工知能が内部的に考えるプロセス、すなわち**「思考の連鎖（Chain of Thought、AIが答えを導き出す前に頭の中で段階的な推論を経る内部思考プロセス）」**を、訓練過程において意図的に報酬（reward）の対象外にすることにしたのです（[AI agents now control part of Deepmind's compute for Gemini experiments ...](https://www.topai-tools.org/news/ai-agents-now-control-part-of-deepmind-s-compute-for-gemini-experiments-but)）。 

これがどういう意味でしょうか？簡単に言うと、AIがなぜそのような実験を行おうとしているのか、その**内部の意図や動機を自然語（人間が読める言語）のままフィルタリングなしで透明に残し**、行動に移す前に人間の管理者が徹底的に検証できるように仕組みを整えたということです（[AI agents now control part of Deepmind's compute for Gemini experiments ...](https://www.topai-tools.org/news/ai-agents-now-control-part-of-deepmind-s-compute-for-gemini-experiments-but)）。頭の中を暗闇で隠すのではなく、インターンが何を考えているのかを透明に覗き見ることができるガラス窓を作り出したようなものです。

---

## 現状：どこまで到達し、どこが限界なのか？

メディアではしばしば「AIが自らを修正しながらターミネーターのように進化している」と刺激的に報じられます。しかし、現場の声ははるかに冷静で現実的です。

グーグル・ディープマインドのコライ・カブクオグル副社長は、ポッドキャストのインタビューで、今回の措置が研究室内部における巨大な戦略的転換（strategic shift）の一環であることを認めつつも、SF映画でよく描写される**「再帰的自己改善（Recursive Self-Improvement、AIが自らコードを修正しながら無限に賢くなるループ）」**はまだ道のりが遠いと一線を画しました（[AI agents now control part of Deepmind's compute for Gemini experiments, but recursive self-improvement remains distant](https://the-decoder.com/ai-agents-now-control-part-of-deepminds-compute-for-gemini-experiments-but-recursive-self-improvement-remains-distant/)）。

つまり、現在のAIエージェントはあくまで人間が設計してくれた枠組みと安全装置の中で、指定された計算予算を活用して実験を「代行」する水準にすぎません。自律的に目標を設定し、自らのアーキテクチャを完全に改造する段階ではないという意味です。AIは非常に強力な「実験の助手」かつ「オーケストレーター」へと進化しましたが、最終的な指揮棒はいまだに人間の研究者の手に握られています。

---

## 今後どうなるのか？

今回の発表を通じて、私たちはAI発展の次の局面がどのような姿になるのかを垣間見ることができます。 

単に文章を上手に書き、イラストを綺麗に描いてくれる生成AIの時代を過ぎ、今や**科学的発見や技術開発そのものを遂行する「エージェンティックAI（Agentic AI）」の時代**へと急速に突入しています。グーグル・ディープマインドの究極の目標は、科学全般を網羅する統一された汎用アルゴリズムを構築することです（[DeepMind's Gemini Experiments Now Orchestrated by AI Agents](https://best-ai.org/ai-news/deepminds-gemini-experiments-now-orchestrated-by-ai-agents-5o695i)）。

今後私たちが注目すべき部分は、AIエージェントが統制された計算資源の中でどれほど精巧な仮説を生み出せるのか、そしてその過程において人間との協調ガバナンス（Governance、管理体制）がどれほど安全に維持されるのかという点です。技術が高度化するほど、人工知能の「内部思考プロセス」を透明にモニタリングしようとするディープマインドの哲学は、全世界のAI業界における重要な標準的安全指針になるものとみられます。

---

## 参考資料

1. The Decoder, *AI agents now control part of Deepmind's compute for Gemini experiments, but recursive self-improvement remains distant*, https://the-decoder.com/ai-agents-now-control-part-of-deepminds-compute-for-gemini-experiments-but-recursive-self-improvement-remains-distant/
2. AI Weekly, *DeepMind Agents Now Run Part of Gemini Experiment Compute*, https://aiweekly.co/alerts/deepmind-agents-now-run-part-of-gemini-experiment-compute
3. TopAI Tools, *AI agents now control part of Deepmind's compute for Gemini experiments, but*, https://www.topai-tools.org/news/ai-agents-now-control-part-of-deepmind-s-compute-for-gemini-experiments-but
4. ExplainX AI, *DeepMind Agents Control Part of Gemini Training Compute — Koray Kavukcuoglu*, https://explainx.ai/blog/google-deepmind-gemini-agents-training-compute-koray-kavukcuoglu-november-2026
5. Emergent SH, *DeepMind AI Agents Now Control Gemini Experiment Compute*, https://emergent.sh/news/deepmind-ai-agents-now-control-gemini
6. Best AI, *DeepMind's Gemini Experiments Now Orchestrated by AI Agents*, https://best-ai.org/ai-news/deepminds-gemini-experiments-now-orchestrated-by-ai-agents-5o695i
7. AI Future, *AI agents now control part of Deepmind's compute for Gemini experiments, but recursive self-improvement*, https://aifuture.org/news/ai-agents-now-control-part-of-deepmind-s-compute-for-gemini-experiments-but-recu-21077
8. The Decoder, *Google Deepmind's AI Co-Scientist now plans experiments, runs lab equipment and writes scientific papers*, https://the-decoder.com/google-deepminds-ai-co-scientist-now-plans-experiments-runs-lab-equipment-and-writes-scientific-papers/
9. Wikipedia, *Gemini (language model)*, https://en.wikipedia.org/wiki/Gemini_(language_model)
10. Interesting Engineering, *Google DeepMind finds 1,600x faster way to expose encryption flaws*, https://interestingengineering.com/ai-robotics/google-deepmind-agents-expose-older-encryption-flaws