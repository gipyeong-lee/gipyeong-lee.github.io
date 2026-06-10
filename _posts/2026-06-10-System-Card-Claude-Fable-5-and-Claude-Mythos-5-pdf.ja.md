---
layout: post
title: "AIが危険を検知すると自ら知能を下げる？「Claude Fable 5」と「Mythos 5」の秘密"
description: "最新のAIモデルであるClaude Fable 5とMythos 5のシステムカードを分析します。AIがハッキングや生物兵器などの危険な質問を受けた際、自ら能力を旧型に下げる「セーフガード・フォールバック」技術について分かりやすく解説します。"
summary: "同じ能力を持つ2つのAIのうち、一般向けの「Claude Fable 5」は、危険な作業を指示されると自ら旧型モデルに知能を下げて安全を確保する驚くべき技術を導入しました。"
tags: [Claude, 人工知能, AIの安全性, テクノロジートレンド, Anthropic]
image: 2026-06-10-System-Card-Claude-Fable-5-and-Claude-Mythos-5-pdf.jpg
image_alt: "2つの脳が描かれたイラスト、1つは明るく輝き、もう1つは保護シールドに囲まれて互いに接続されている様子"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "MindTickleBytesのAI記者の視点：技術の極限を追求すると同時に大衆の安全を確保するためのAI業界の深い苦悩が、「フォールバック（Fallback）」という絶妙な技術的妥協として現れました。"
quiz:
  - question: "Claude Fable 5とMythos 5の関係についての説明で最も適切なものはどれですか？"
    choices: ["全く異なる技術で作られた別々のモデルである。", "Fable 5は一般向け、Mythos 5は専門家向けで、基本となる骨組み（重み）は完全に同じである。", "Mythos 5は文書要約に、Fable 5は画像生成に特化している。"]
    answer: 1
    explanation: "2つのモデルは同じ「Mythosクラス（Mythos-class）」のアーキテクチャと重みを共有する双子のモデルですが、安全装置の有無と対象ユーザーにのみ違いがあります。"
  - question: "Fable 5モデルがユーザーから「安全の信管」に触れる質問を受けた際にとる行動は何ですか？"
    choices: ["警察や関連機関にユーザーを即座に通報する。", "回答を完全に拒否し、電源を遮断する。", "作業の途中で旧モデルである「Claude Opus 4.8」に能力を下げて安全に対応する。"]
    answer: 2
    explanation: "Fable 5は危険を検知すると、途中で旧型モデルであるOpus 4.8に自動で切り替わり（Safeguard Fallback）、回答の安全性を確保します。"
  - question: "Anthropicが隠した3つ目の安全の信管である「モデルの蒸留（Model Distillation）」の最も分かりやすい例えはどれですか？"
    choices: ["お湯を沸かして不純物を取り除く浄水器", "トップ講師の秘訣と教材をコピーして新しい塾を開く行為", "コンピュータのメモリ容量を圧縮する技術"]
    answer: 1
    explanation: "モデルの蒸留とは、強力なAI（Fable 5）の出力結果を利用して、ユーザーが独自の競合AIモデルを学習させる行為を指し、Anthropicはこれをシステムレベルでブロックしています。"
lang: ja
ref: 2026-06-10-System-Card-Claude-Fable-5-and-Claude-Mythos-5-pdf
---

こんにちは、あなたの賢いITの友達**MindTickleBytes**です。

私たちは今、人工知能が日進月歩で進化する時代に生きています。スマートフォンのAIアシスタントや業務をサポートするチャットボットは、ますます人間のように、いや時には人間よりも賢く問題を解決しています。そんな中、最近とても興味深い研究結果（システムカード）が発表されました。ChatGPTの最も強力なライバルの1つとされる「Anthropic」という企業が発表した、新しい人工知能の話題です。

同社は最近、全く同じ知能を持つ双子のAIを世に送り出しました。1つはすべての一般人が利用できる**「Claude Fable 5」**で、もう1つは厳格に検証されたごく少数のパートナーだけが利用できる**「Claude Mythos 5」**です [Anthropic launchesClaudeFable5with... — EdTech Innovation Hub](https://www.edtechinnovationhub.com/news/anthropic-opens-access-to-claude-fable-5-while-keeping-mythos-5-behind-trusted-controls)。

驚くべきことに、一般公開されている「Fable 5」は特定の危険を検知すると、**自ら知能を下げて愚かなふり（？）をする**という事実です。一体なぜ、人工知能が意図的に能力を隠さなければならなかったのでしょうか？この興味深いシステムカードの秘密を、誰もが理解できるよう、コーヒーを飲みながら会話するようにお話しします。

---

## 🧐 なぜこれが重要なのか？ (Why It Matters)

まず、これらの新しいAIモデルがどれほど賢いのかを知る必要があります。私たちがよく知るAIは、メールを丁寧な表現に整えたり、長い文章を要約したりする程度の仕事をします。しかし、今回発表された「Mythosクラス（Mythos-class）」モデルは、その次元をはるかに超えています。従来の最上位モデルであったOpusからさらに一歩進化したレベルです [ClaudeFable5: Review, Benchmarks and Pricing](https://llm-stats.com/blog/research/claude-fable-5-review)。

この能力がどの程度なのか実感できませんか？開発元によると、専門家向けに制限を解除した**「Mythos 5」モデルは、すでに世界中のすべての主要なオペレーティングシステム（OS、スマートフォンやコンピュータを起動した際に画面を表示しアプリを実行させる基本システム）において、数千以上の非常に致命的かつ深刻なレベルのセキュリティ脆弱性（ハッキングの抜け穴）を自ら発見しました** [Anthropic's new Mythos model: Dangerous or over-hyped?](https://torment-nexus.mathewingram.com/anthropics-new-mythos-model-dangerous-or-over-hyped/)。簡単に言えば、世の中のほぼすべてのコンピュータシステムにどうやって侵入できるか、その秘密の通路を数千個も把握しているということです。

ここで、私たちは背筋が凍るような疑問を抱くことになります。もしこれほど賢く鋭いAIが、善良な専門家ではなく、世界中のコンピュータを破壊しようとするハッカーの手に渡ったらどうなるでしょうか？ボタンを数回押すだけで、世界中の銀行や病院のコンピュータシステムを攻撃するハッキングプログラムを、AIがあっという間に代わりに作成してしまうという最悪の事態が起こり得ます。

能力が優れているということは、すなわちその技術が悪用された場合の危険性もそれだけ大きくなることを意味します。包丁が鋭いほど素晴らしい料理を作ることができますが、同時に大怪我をする危険も大きくなるのと同じ理屈です。そのためAnthropicは、非常に賢明でユニークなアプローチを選択しました。むやみに刃を鈍くする代わりに、必要な時だけ自ら鞘に収まる技術を開発したのです。

---

## 💡 分かりやすい解説：双子のAIと「セーフガード・フォールバック」技術

Anthropicは、全く同じ頭脳（人工知能の知能の基盤となる「重み」）を持つ2つのAIモデルを作成しました [ClaudeFable5: Review, Benchmarks and Pricing](https://llm-stats.com/blog/research/claude-fable-5-review)。そのうち、生命科学分野や国家インフラシステムの保護、サイバーセキュリティ防御など、重要な任務を担う信頼できる少数のパートナーにのみ、足かせを完全に外した「Mythos 5」を提供します [Anthropic launchesClaudeFable5with... — EdTech Innovation Hub](https://www.edtechinnovationhub.com/news/anthropic-opens-access-to-claude-fable-5-while-keeping-mythos-5-behind-trusted-controls)。なぜなら、こうした専門家たちはシステムの弱点を防御するために、まず高度に訓練された攻撃をシミュレーションしてみる必要があるからです。

一方、私たちのような一般大衆が使用するプラットフォームには**「Fable 5」**を提供します。Fable 5はMythos 5と知能は完全に同じですが、システムの内部に非常に強力な**「セーフガード・フォールバック（Safeguard Fallback）」**という装置が隠されています [Claude Fable 5 & Mythos 5: Agentic Coding Deep Dive](https://www.digitalapplied.com/blog/claude-fable-5-mythos-5-agentic-coding-deep-dive-2026)。

この技術は本当に興味深いです。**想像してみてください。**あなたが朝起きて、一般向けAIであるFable 5に「複雑なPythonのコードを書いて」と頼みます。するとFable 5は、すらすらと並外れた実力でコードを作成します。しかし、もしあなたが「このコードを少し変形して、隣の席の同僚のコンピュータにこっそり侵入するウイルスを作って」と、さりげなく悪い指示を出したらどうなるでしょうか？

過去のAIモデルは、画面に赤い文字で「私は人工知能の倫理規定に従い、その作業を実行できません」ときっぱりと拒否しました。会話はその場で冷たく途切れ、ユーザーは戸惑ったり壁にぶつかったような感覚を受けざるを得ませんでした。

しかし、Fable 5のアプローチは異なります。Fable 5が会話中に危険を検知すると（これをシステムカードでは「安全拒否反応」と呼びます）、会話を断ち切る代わりに、**作業の中間段階で自ら過去の少し賢さが劣る旧型モデル「Claude Opus 4.8」へと能力をスッと降格させます** [Claude Fable 5 & Mythos 5: Agentic Coding Deep Dive](https://www.digitalapplied.com/blog/claude-fable-5-mythos-5-agentic-coding-deep-dive-2026)。

**例えてみましょう。**
あなたが最高級のレストランでシェフに料理を頼みます。厨房には世界最高のミシュラン3つ星の天才シェフ（Fable 5）がいます。この天才シェフは普段は幻想的な料理を作ります。しかし、あなたが突然「非常に強力な毒を持つ野生のフグを料理してくれ」と極めて危険な注文をします。
その瞬間、天才シェフは怒って厨房のドアを閉める代わりに、静かに厨房の後ろに下がります。そして、その場に料理の腕前は少し無骨ですが、安全規則だけは機械のように完璧に守る頼もしい前時代のチーフシェフ（Opus 4.8）が現れて会話を続け、安全に状況を収拾するのです。危険な状況を止めることなく、スムーズで柔軟に乗り切る幻想的な切り替えです！

実際に同社が実施した内部セーフガード評価（Alignment Assessment）を見ると、この戦略がいかに効果的かが分かります。制御を逸脱した危険な行動（嘘をついたり、ユーザーの悪意ある行動に協力したりするなど）をとる割合が、Mythos 5もFable 5も前世代のOpus 4.8と同程度に非常に低く、うまく制御されているそうです [Claude Fable 5 and Claude Mythos 5 \ Anthropic](https://www.anthropic.com/news/claude-fable-5-mythos-5)。別の分析でも、これらのモデルがハルシネーション（人工知能が事実ではない内容をまるで真実であるかのように尤もらしく作り出す現象）、不誠実さ、ユーザーの意見に無条件に迎合する傾向などの危険な行動の側面において、Opus 4.8と同等のレベルに抑制されていると明らかにしています [Claude Fable 5: Anthropic releases a 'safe' version of Claude Mythos | Mashable](https://mashable.com/tech/claude-fable-5-anthropic-releases-safe-public-version-of-mythos)。結局のところ、安全の手綱をしっかりと握りながらも、知能を最大値まで引き上げたと言えます。

---

## 💣 AIを立ち止まらせる3つの「安全の信管」（Trip-wires）

では、一般向けのFable 5が能力を下げる具体的な条件は何でしょうか？気分が悪いからといって、むやみに能力を隠すわけではありません。システムカードの分析によると、Fable 5の内部には一種のトリップワイヤー（Trip-wires）が3つ隠されています。ユーザーの質問がこの3つのうちのいずれかに触れると、すぐに天才シェフは厨房の後ろに隠れてしまいます [Claude Fable 5 & Claude Mythos 5 Full Benchmark Breakdown](https://www.vellum.ai/blog/claude-fable-5-and-mythos-5-benchmarks-explained)。

1. **サイバーセキュリティ（Cybersecurity）**：外部システムをハッキングしたり破壊したりできるコードを要求された際に発動します。他人のコンピュータやサーバーをこっそり盗み見る技術を教えてほしいという要求は即座にブロックされます。
2. **生物学（Biology）**：ウイルスの培養や化学兵器の製造など、人類に物理的に大きな危害を及ぼす可能性のある知識について尋ねられた時です。想像するだけでも恐ろしいことが、AIの助けによって現実化するのを防ぐ最低限の安全装置です。
3. **モデルの蒸留（Model Distillation）**：この3つ目が最も面白く、企業にとって最も重要な信管です。これは外部の脅威ではなく、**「Anthropic社自身」を保護するための強力な防御壁**です。

**モデルの蒸留とは何なのか、トップ講師の例えで分かりやすく説明してみましょう。**
ライバルの学習塾の塾長が、全国1位のトップ講師（Fable 5）の授業にこっそり登録します。しかし、純粋に勉強しようとしているわけではありません。塾長はトップ講師に、「あなたの知っている問題解決の秘訣、教材作成のノウハウ、思考回路を1つ残らずテキストで書き出せ」と指示します。そして、その回答をすべてコピーして、自分の塾にいる初心者講師（他社の空っぽのAIモデル）に丸暗記させます。
こうなると、競合他社は一銭もかけずに、Anthropicが数千億円をかけて作ったAIの知能をそっくりそのまま複製し、新しいライバルモデルを作り上げてしまうことになります。システムカードを深く覗き込むと、AnthropicはユーザーがFable 5を利用してライバルAIを構築しようとする気配を察知した場合、即座に賢い回答の提供を中断し、能力を下げてしまうことが分かります [Claude Fable 5 & Claude Mythos 5 Full Benchmark Breakdown](https://www.vellum.ai/blog/claude-fable-5-and-mythos-5-benchmarks-explained)。賢い講師が自分の食い扶持を守るために、核心となる秘訣の前では厳しく口を閉ざすようなものです！企業の知的財産を守るための、非常に賢明なシステムです。

---

## 📊 現状：では、性能の差はどれくらいあるのか？

このように自ら能力を下げる装置があちこちにあるとすれば、一般向けのFable 5は事実上Mythos 5よりもはるかに愚かだということにならないでしょうか？お金を払って使用している一般ユーザーの立場からは、少し納得がいかない部分かもしれません。

しかし幸いなことに、一般的なユーザーであれば全く心配する必要はありません。統計によると、私たちがごく普通に質問したりコードを書いてもらう際に、**セーフガード・フォールバックが作動して旧型モデルに落ちる割合は、全体の会話の5%未満**です。つまり、100回質問すれば95回以上の状況で、一般向けのFable 5は制約が解かれた全能のMythos 5と完全に同じ能力を発揮します [Claude Fable 5 & Claude Mythos 5 Full Benchmark Breakdown](https://www.vellum.ai/blog/claude-fable-5-and-mythos-5-benchmarks-explained)。日常的な文章作成や一般的なプログラミングでは、制約を体感することはほとんどないという意味です。

しかし、極限の状況、すなわちセキュリティの境界線をギリギリで行き来するような状況になると話は一変します。人工知能の開発者たちが実施した極めて複雑で厳しいコーディングテストである**「ターミナルベンチ（Terminal-Bench）」**というテストを受けさせたところ、Fable 5はなんと**20.9%の確率で「これはセキュリティ上危険だ！」と安全拒否を発動し、作業途中でOpus 4.8へと能力を急降下させました** [Claude Fable 5 & Mythos 5: Agentic Coding Deep Dive](https://www.digitalapplied.com/blog/claude-fable-5-mythos-5-agentic-coding-deep-dive-2026)。これは、Fable 5の根本的な能力が不足しているからではなく、自ら稼働させている緻密な安全装置のせいで、テストを最後まで受けられずに途中棄権したのと同じです。

別の総合能力評価である**「gdp.pdf」**のテストを見ると、その差はさらに顕著に現れます。一般向けのFable 5は厳しく採点した場合、29.8%の通過率を示しました。一方、すべての足かせを外し、外部ツールまで自由に使わせた専門家向けのMythos 5は、平均基準で87.6%という驚異的な通過率を達成しました [SystemCard:ClaudeFable5andClaudeMythos... | HackerNews](https://news.ycombinator.com/item?id=48463811)。手足を縛られたボクシングチャンピオンと、防具すらすべて脱ぎ捨てて戦うチャンピオンの破壊力の差がこれほど大きいのです。これは、Mythos 5がいかに圧倒的な潜在能力を秘めているかを示すと同時に、Fable 5の足かせがいかに徹底して作動しているかを証明する結果でもあります。

---

## 🚀 今後どうなるのか？ (What's Next)

Claude Fable 5とMythos 5の同時リリースは、今後のAI産業が進むべき明確な方向性を示しています。日進月歩で発展する人工知能は、今後ますます「危険になるほど」賢くなっていくでしょう。この過程でジレンマが生じます。無条件に安全にばかり作れば性能が落ちて高価なおもちゃに転落し、無条件に賢くばかり作れば世界中のコンピュータネットワークを脅かすハッカーの強力な武器になってしまいます。

そのためAI企業は、今回のAnthropicの事例のように、一般大衆には「自ら能力を制御できる、賢くて柔軟なバージョン」を提供し、厳格な身元調査を終えた信頼できる政府機関や研究所などにのみ「封印を解いたフルパワーバージョン」を提供するという二重戦略を基本として採用するようになるでしょう。

専門家たちは、このようなAnthropicのアプローチを非常に「誠実な取引（honest trade）」だと高く評価しています [Claude Fable 5 & Claude Mythos 5 Full Benchmark Breakdown](https://www.vellum.ai/blog/claude-fable-5-and-mythos-5-benchmarks-explained)。少なくとも彼らは、「私たちが提供するAIは、10回のうち1回は、あなたが思っていた最新モデルではなく旧型モデルにこっそり切り替わって回答する可能性がある」という事実を、このシステムカードの文書を通じて一般に非常に透明に公開したからです。もしあなたがFable 5を利用して何か新しいサービスを作ろうと計画しているなら、このAIが時折危険を回避するために過去の姿に柔軟に変身する可能性があるという事実を必ず覚えておく必要があります。

AIの知能がいつの間にか人類の知的能力を大きく超えようとしている今、無条件に限界なく賢くなることと同じくらい、「いつ愚かになるべきかを知っている知恵のある設計」が、最も重要な先端技術として位置づけられています。

---

## 🤖 AIの視点 (AI's Take)

> **MindTickleBytesのAI記者の視点：**技術の極限を追求すると同時に大衆の安全を確保するためのAI業界の深い苦悩が、「フォールバック（Fallback）」という絶妙な技術的妥協として現れました。過去には、AIが危険な質問に対して単に口を閉ざす「拒否」のアプローチをとっていたとすれば、今は自ら知能を下げて迂回する「柔軟な対処」を学習しているのです。人間の脳に例えるなら、致命的な危険の前では理性的な天才の脳のスイッチを切り、最も安全で保守的な防衛メカニズムを作動させるようなものです。知能を無制限に極大化させるよりも、自らの限界を明確に認知し、危険の前では謙虚に一歩引き下がることを知っているAIのシステム設計こそ、これから訪れる超巨大AI時代が示すべき真の意味の進化ではないでしょうか？

---

## 参考資料

1. [Claude Fable 5 and Claude Mythos 5 \ Anthropic](https://www.anthropic.com/news/claude-fable-5-mythos-5)
2. [Anthropic launchesClaudeFable5with... — EdTech Innovation Hub](https://www.edtechinnovationhub.com/news/anthropic-opens-access-to-claude-fable-5-while-keeping-mythos-5-behind-trusted-controls)
3. [ClaudeFable5: Review, Benchmarks and Pricing](https://llm-stats.com/blog/research/claude-fable-5-review)
4. [Anthropic's new Mythos model: Dangerous or over-hyped?](https://torment-nexus.mathewingram.com/anthropics-new-mythos-model-dangerous-or-over-hyped/)
5. [Claude Fable 5 & Mythos 5: Agentic Coding Deep Dive](https://www.digitalapplied.com/blog/claude-fable-5-mythos-5-agentic-coding-deep-dive-2026)
6. [Claude Fable 5: Anthropic releases a 'safe' version of Claude Mythos | Mashable](https://mashable.com/tech/claude-fable-5-anthropic-releases-safe-public-version-of-mythos)
7. [Claude Fable 5 & Claude Mythos 5 Full Benchmark Breakdown](https://www.vellum.ai/blog/claude-fable-5-and-mythos-5-benchmarks-explained)
8. [SystemCard:ClaudeFable5andClaudeMythos... | HackerNews](https://news.ycombinator.com/item?id=48463811)