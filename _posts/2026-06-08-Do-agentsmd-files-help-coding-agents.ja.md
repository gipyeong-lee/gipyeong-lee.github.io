---
layout: post
title: "AIにコーディングを任せたらめちゃくちゃ？「この文書」一つで天才秘書になります"
description: "AIに仕事を任せると、なぜいつも見当違いな結果が出るのでしょうか？AIコーディング秘書の専用業務ガイドラインであるAGENTS.mdファイルとは何か、そしてこれがなぜあなたの職場生活を変えるのかを探ります。"
summary: "AIコーディング秘書に明確な業務ガイドラインとルールを記載した「AGENTS.md」ファイルを提供すると、作業成功率が30%から90%へと垂直上昇します。"
tags: [AI, コーディング秘書, プロンプト, AGENTS.md]
image: 2026-06-08-Do-agentsmd-files-help-coding-agents.jpg
image_alt: "コンピュータの画面の前に置かれたロボットと、その横に詳細に書かれた業務指示書の文書があるイラスト"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "MindTickleBytesのAI記者の視点：無条件に賢いAIを探すよりも、自分のAIにどのような文脈（コンテキスト）を与えるかを悩むことがはるかに重要な時代になりました。"
quiz:
  - question: "2025年の研究によると、AGENTS.mdのようなコンテキストファイル（Context files）を提供されたAIの課題成功率は何パーセントまで上昇しましたか？"
    choices: ["30%", "60%", "90%"]
    answer: 2
    explanation: "コンテキストファイルなしで単独でコーディングを実行したAIの成功率は約30%に過ぎませんでしたが、よく作成されたコンテキストファイルを提供されたAIは90%という高い課題成功率を記録しました。"
  - question: "優れたAGENTS.mdファイルを作成するためのヒントとして間違っているものはどれですか？"
    choices: ["「あなたは役立つアシスタントだ」のように、できるだけ広く肯定的な意味で曖昧に書く。", "明示的に実行できるコマンドを具体的に書く。", "AIが絶対にやってはいけないことに対する明確な境界線（Boundaries）を設定する。"]
    answer: 0
    explanation: "GitHubブログの分析によると、ほとんどのファイルが失敗する理由は曖昧すぎるためです。「あなたは役立つコーディングアシスタントだ」のような曖昧な文句は避け、具体的な技術スタックやコマンド、境界線を明確に書く必要があります。"
  - question: "Augment Codeの研究結果によると、最悪に作成されたAGENTS.mdファイルはAIにどのような影響を与えましたか？"
    choices: ["パフォーマンスに何の影響も与えなかった。", "指示書が全くない時よりも結果を悪化させた。", "パフォーマンスをわずかに向上させた。"]
    answer: 1
    explanation: "誤ったルールが満載の悪いAGENTS.mdファイルは、AIの思考回路を混乱させ、ガイドラインが全くない状況よりも結果物の品質を積極的に損なうことがわかりました。"
lang: ja
ref: 2026-06-08-Do-agentsmd-files-help-coding-agents
---

想像してみてください。あなたのチームにハーバード大学を首席で卒業した、とてつもない天才インターンが新しく入ってきました。あなたはこの賢いインターンに「うちの会社のウェブサイトのメイン画面を少し修正して」と軽く指示します。インターンは指示を受けるやいなや徹夜で最新技術を総動員し、華やかで驚くべきウェブページを作り上げます。

しかし、実際にサーバーにアップしてみると大きな問題が発生しました。私たちの会社は伝統的に落ち着いたブルーのブランドカラーを維持しなければならないのに、インターンはすべて眩しい真っ赤な色にデザインを変えてしまったのです。何よりも、私たちが10年間使っている古い内部データベースシステムとは全く連動しない最新の方式を勝手に使ってしまったのです。結局、インターンが情熱的に書いたコードはたった1行も使えなくなってしまいました。

この賢いインターンが愚かだからこんなミスをしたのでしょうか？そうではありません。このインターンは技術的には完璧でしたが、私たちの会社ならではの固有の「業務ルール」と「背景の文脈（コンテキスト）」を全く知らなかったからです。いくら優秀な人材でも、きちんとした業務の引き継ぎを受けられなければ、空回りするしかありません。

今日のソフトウェア開発の世界では、毎分毎秒これと全く同じことが起きています。ChatGPTの登場以降、人間の言語を理解して代わりにコードを書いてくれるAIコーディングエージェント（AI Coding Agent、人間に代わって自ら判断しソフトウェア開発作業を遂行する人工知能）が広く使われています。しかし、開発者がこの賢いAIに無計画に仕事を任せると、先ほどの天才インターンの例のように、既存のシステムを壊したり、全く見当違いな結果を出したりしがちです。AIはインターネット上にある膨大な一般知識は知っていても、「私たちの会社のプロジェクト」ならではの具体的な内部ルールは知らないからです。

このような慢性的な問題を解決するために、最近世界中のIT企業の間で必須として定着しつつある魔法の鍵があります。それがまさに、AIのための専用の引き継ぎ書であり業務ガイドラインである**「AGENTS.md」**ファイルです。この小さな文書一つが、あなたのAI秘書をどのように一騎当千の天才へと変貌させるのか、これからとても簡単に説明します。

## なぜこれが重要なのか？ (Why It Matters)

「私はプログラマーでもないし、コーディングの『コ』の字も知らないのに、こんなことをあえて知る必要があるのか？」と思われるかもしれません。しかし、この話は単にコンピュータのコーディングをする人たちだけの複雑な技術の話ではありません。

近い将来、私たちは皆、それぞれのコンピュータの中に賢いAI秘書を従えて働くことになるでしょう。Excelデータを自動で整理するAI秘書、毎朝溜まったメールを要約して代わりに返信を書いてくれるAI秘書、PowerPointのプレゼン資料のデザインを手伝ってくれるAI秘書など、職務と分野が異なるだけで、人工知能と密接に協業する時代はすでに私たちの目の前に大きく開かれています。この時、AIを自分の意図通りに正確かつ礼儀正しく働かせる方法、つまり「AIに自分の業務の固有のルールをきちんと説明する方法」は、今後すべての社会人が備えるべき必須の生存スキルになるでしょう。

明確な業務指示書が持つ威力は、客観的な数字を通じても克明に証明されています。2025年に発表されたコンテキストエンジニアリング（Context Engineering、AIに状況と背景知識を効果的に伝える技術）に関する研究を見ると、非常に衝撃的な実験結果が出ています。特定のプロジェクトの背景文脈（コンテキスト）を知らせるガイドラインファイルなしに、単独で複雑なコーディング作業を実行するよう指示されたAIエージェントたちは、全課題のうち正しく作業を完了する確率がわずか30%前後に過ぎませんでした。10回のうち7回は見当違いなコードを書いたり、既存のシステムと衝突する致命的なエラーを出したりした計算になります。

しかし驚くべきことに、よく作成されたコンテキストファイル（Context files）をプロジェクトフォルダに予め入れておき、同じ作業を指示した時、AIの課題成功率はなんと90%まで垂直に上昇しました[[Context Engineering 2026: AGENTS.md, CLAUDE.md, and .cursorrules That ...](https://tutorials.technology/tutorials/context-engineering-claude-cursor-2026.html)]。単にテキストファイルを一つ追加しただけなのに、AIの業務能力がなんと3倍も跳ね上がったのです。この結果は、いくら高価で優れた最新のAIモデルを毎月課金して使ったとしても、正しいガイドラインが裏付けられていなければ、いつ爆発するかわからない時限爆弾も同然だということを示唆しています。分かりやすく言えば、世界最高のプロの大工を雇っておきながら、設計図なしで家を建てろと言うのと同じです。

## わかりやすく解説 (The Explainer)

では、一体「AGENTS.md」というものは具体的に何なのでしょうか？

世界中のソフトウェア開発分野では、ずっと昔からプロジェクトフォルダの一番最初の画面に「README（私を読んでください）」というファイルを置く美しい慣行があります。このファイルは、新しい同僚の開発者がチームに合流した際、「このプログラムはどのような目的のために作られ、自分のコンピュータへのインストールはどう行い、使用法はこうです」と「人間の言語」で親切に説明してくれる総合案内書の役割を果たします。

しかし、READMEファイルはあくまで人間の理解を助けるために使われていました。AIがこのプロジェクトでどのような機械的なルールを守りながらコードを書かなければならないのかについては説明してくれません。まさにこの隙間を完璧に埋めるために誕生したのがAGENTS.mdです。このファイルは人間ではなく**AIコーディングエージェントたちを親切に案内するために特別に考案された、シンプルでオープンな形式のファイル**であり、非常に簡単に言えば「AI秘書のためのカスタマイズされた業務指示書」だと考えれば正確です [[GitHub - agentsmd/agents.md: AGENTS.md — a simple, open format for guiding coding agents](https://github.com/agentsmd/agents.md)]、[[AGENTS.md](https://agents.md/)]、[[AGENTS.md & SKILL.md: The Complete Guide (2026)](https://www.morphllm.com/agents-md-guide)]。

このファイルを使用する方法は、信じられないほど簡単です。プロジェクトのファイルが集まっている最上位フォルダ（ルートリポジトリ）に、拡張子が `.md` のMarkdown（マークダウン、複雑なコードなしでテキストに簡単な書式を適用する軽量な文書形式）ファイルを一つ作っておくだけです。

すると、ユーザーのコマンドを受けたAIコーディングエージェントが、本格的な仕事に取り掛かる前に一番最初にこの文書をスキャン（Scan）し、ルールをスポンジのように吸収します。最も興味深い点は、この文書がAIの脳構造を初期設定するシステムプロンプト（System prompt、AIの基本的な自我と行動綱領を設定する絶対的な最上位命令）のすぐ次の位置に確固として定着することです [[A Complete Guide To AGENTS.md](https://www.aihero.dev/a-complete-guide-to-agents-md)]。これにより、AIは仕事に着手する前からすでにこのプロジェクトのエコシステムとルールを完璧に熟知した頼もしい作業者となります。

人間のための既存のREADME文書が「このプロジェクトが結局何（What）をするものなのか」を感性的に説明するものだとすれば、AGENTS.mdは「AIがこのプロジェクトで具体的にどのよう（How）に働くべきか」をドライかつ正確に教えてくれる専用空間なのです [[AGENTS.md & SKILL.md: The Complete Guide (2026)](https://www.morphllm.com/agents-md-guide)]。

例えるならこうです。あなたが世界最高の料理の腕前を持つミシュラン3つ星シェフ（最新の高性能AI）を莫大な年俸を出して雇い、あなたのレストランの厨房を任せました。何のガイドラインもなければ、シェフは自分の好きなように高価なキャビアやトリュフをふんだんに使った複雑なフランスの本格料理を作るでしょう。料理自体は芸術的で素晴らしいものになりますが、もし私たちの食堂が、忙しい社会人のために安くて早い1万ウォンのキムチチゲを売る韓国式の定食屋であれば、この料理は全く役に立ちません。客は怒りを爆発させ、食堂はすぐに閉店に追い込まれるでしょう。

この時、厨房の壁に次のような明確な運営規則（AGENTS.md）を大きく貼り付けておいたらどうでしょうか？
「1. 当店はチゲ専門の韓国式定食屋である。2. 全ての料理は注文から15分以内に客席に提供しなければならない。3. 辛さは3段階で固定する。4. 原価が5千ウォンを超える高級食材は絶対に使用禁止とする。」

そうして初めて、シェフは自分の素晴らしい料理の腕前を十分に発揮し、決められた単価とスピードに合わせながらも、世界で最も深い味わいを出す超高速キムチチゲを作り上げるでしょう。統制されていなかった最上位の知能が、ついに「私たちの食堂のルール」の中で完璧に飼い慣らされ、真の輝きを放つ瞬間です。

## 現在の状況 (Where We Stand)

この驚くほどシンプルな方法論は現在、シリコンバレーをはじめとする世界のIT業界の新しい強力な標準として急速に定着しています。わずか過去1年の間に、コーディングリポジトリ（Repository）にAGENTS.mdやCLAUDE.md（特定のAIモデル専用ファイル）のようなガイドラインファイルを静かに追加することが、最も基本的な慣行となりました。Anthropic、OpenAI、Qwenなど、現在世界のAI市場を主導しているエージェント開発企業は皆口を揃えて、すべてのユーザーにこの方式を使用することを非常に積極的に推奨しています [[DoAGENTS.md/CLAUDE.mdFilesHelpCodingAgents? | Towards AI](https://towardsai.net/p/machine-learning/do-agents-md-claude-md-files-help-coding-agents-a-new-paper-challenges-this)]。さらに、様々なAIコーディングアシスタントのために、これらのファイルをどう効果的に作成すべきかについての概括的なガイドライン（Overview）の分析文書も毎日のように溢れ出ています [[Instruction Files for AI Coding Assistants: An Overview](https://aruniyer.github.io/blog/agents-md-instruction-files.html)]。

しかしここで、私たち全員が注意すべき非常に核心的な事実があります。単に真似をして空のテキストファイルを一つ適当に作っておくだけで、全ての問題が魔法のように消え去るわけでは決してないという点です。

世界最大のソースコードホスティングプラットフォームであるGitHubのブログに掲載された興味深い分析結果を見てみましょう。なんと2,500を超える様々なリポジトリの事例を綿密に分析した結果、人々が野心的に作成したほとんどのエージェント指示ファイルが徹底的に失敗していることがわかりました。その理由は、あまりにも「曖昧すぎる」ためでした。例えば、ファイルの中に単に「あなたは私を助けてくれる素晴らしいコーディングアシスタントだ（You are a helpful coding assistant）」とか、「コードをすっきりと綺麗に書いて」と漠然と書いておくことは、機械であるAIにこれっぽっちも役立ちません。

AIの能力を100%引き出す優れたAGENTS.mdファイルは、うんざりするほど具体的でなければなりません。そこには、AIが取るべきペルソナ（Persona、性格や役割の指定）、このプロジェクトで使用する正確な技術スタック（Tech stack、開発に使われるプログラミング言語やツールの集合）、プロジェクトファイルが保存されているフォルダ構造、ワークフロー（Workflows）、明示的に実行できるターミナルコマンド、コードスタイルの例などが非常に丁寧に盛り込まれている必要があります。そして最も重要なのは、**「絶対にやってはいけないこと（Boundaries）」に対する厳格で明確な境界線を設定すること**です [[How to write a great agents.md: Lessons from over 2,500 repositories - The GitHub Blog](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/)]。

例えば、単に「うまく作って」ではなく、「新しい機能をコーディングする時は、インターネットから新しいライブラリ（あらかじめ作られた外部コードの塊）を勝手にダウンロードして追加せず、必ず既存のフォルダにあるものを再利用せよ」とか、「他の開発者がコードをレビューできるように、コードをマージする前には必ず `npm run lint` という構文エラー検査コマンドを自ら実行せよ」といった、非常に具体的で盲目的なルールを文書に刻み込んでおかなければなりません [[Custom instructions with AGENTS.md – Codex | OpenAI Developers](https://developers.openai.com/codex/guides/agents-md)]。

最も衝撃的な事実は、間違って書かれた指示書が、いっそ無い時よりもはるかに深刻な悪影響を及ぼすという恐ろしい研究結果です。AIコード作成ツールを専門的に研究しているAugment Codeの研究員たちは、非常に体系的なブラインド実験を行いました。その結果、最も緻密によく書かれた最上級の指示書を提供した時、AIコーディングエージェントの品質はとてつもない飛躍を遂げました。これはまるで、安価で軽量な普及型の人工知能モデルを使っていたのに、突然、数十倍高価で最も賢い最上位の人工知能モデルへとコンピュータを丸ごとアップグレードしたのと等しい、奇跡的な効果でした。

しかし逆に、ルールがめちゃくちゃな「最悪のファイル群」は、何のガイドラインファイルも無い時よりも劣る、悲惨なゴミコードを吐き出しました。ずさんで矛盾したルールがAIの論理的思考回路をひどく混乱させ、自らの能力を食い潰させてしまったのです。研究員たちは、「ほとんどの人々がインターネットからコピーしてAGENTS.mdに無頓着に書き込む内容はAIの役に全く立たず、むしろAIの能力を積極的に損なっている（Actively hurts）」とし、正しい文書作成の重要性を強く警告しました [[A good AGENTS.md is a model upgrade. A bad one is worse than no docs at all. | Augment Code](https://www.augmentcode.com/blog/how-to-write-good-agents-dot-md-files)]。

分かりやすく言えば、このような状況と同じです。とてもよく訓練された賢い天才犬（超巨大AIモデル）があなたの前にいます。この犬に「庭にある赤いフリスビーを私の前に持ってきて」と短く明確に指示すれば（良いAGENTS.md）、犬はためらうことなく走っていき、完璧に任務を遂行します。

しかし、指示書に無駄な言葉を入れすぎて、「フリスビーを持ってくるんだけど、行く途中で右側のリンゴの木を一度回って、水たまりは絶対に踏まず、赤いフリスビーだけを拾ってくること。ただしもし青色なら3回吠えて、日が沈む頃なら持ってこないこと…」というように、長ったらしく条件が絡み合った紛らわしいルールを山ほど並べ立てたら（悪いAGENTS.md）、何が起きるでしょうか？いくら賢い天才犬であっても混乱に陥り、その場に座り込んでクンクン鳴いたり、フリスビーの代わりに見当違いの石ころをくわえてきたりします。文書にとにかくたくさんの言葉を書けば良いというものでは決してありません。よく整理された明確で、誤解の余地がない簡潔なルールだけが、AIの潜在力を爆発させ、致命的な混乱を防ぐことができるのです。

## 今後どうなるのか？ (What's Next)

時間が経つにつれて、人工知能エージェント自体の頭脳の知能は幾何級数的に高まるでしょう。しかし、実際に企業や個人が実務で必要とする「実際の作業」を無理なく安定的に遂行するために必要な特殊な文脈（Context）を、AIが何の情報もなしに空気を読んで自ら悟ることは不可能です。特定の会社、特定のチーム、そして私という特定のユーザーの固有のニュアンスや手続き的なノウハウを、どのように綺麗にパッケージ化し、AIに抵抗感なく注入するかが、未来の業務における核心的な競争力となるでしょう。

これに伴い、今後は単にテキスト文書を1枚作成することを超え、複雑な知識とコンテキストをソフトウェアパッケージの形でしっかりと結びつけ、必要な時にAIが自由に呼び出せるようにする「スキル（Skills）」のような高度化された標準化技術が新たに登場し、市場を牽引しています [[A standardized way to give AIagentsnew capabilities and expertise.](https://agentskills.io/)]。

また、この巨大な流れはコードを書くプログラマーだけの専有物を急速に超え、デザインや企画などクリエイティブな領域へと恐ろしい勢いで拡張しています。例えば、堅苦しいコードではなく視覚的デザインの一貫性を維持するために、ウェブサイトのフォントサイズ、余白、CSSのカラー値などUI（ユーザーインターフェース）デザイントークンを定義しておく「DESIGN.md」ファイルもオープンソースとして広く共有されており [[VoltAgent/awesome-design-md: A collection of DESIGN.mdfiles...](https://github.com/VoltAgent/awesome-design-md)]、これを積極的に活用すれば、単なるコーディングエージェントを視覚的な美学まで考慮する強力な「統合デザインエンジン」へと一気に変貌させることもできます [[Open Design — Official open-source Claude Design alternative](https://open-design.ai/)]。

このような変化は、私たちに非常に重要な示唆を与えてくれます。Builder.ioのような最新の開発コラボレーションツール環境では、純粋にコーディングだけを行うエンジニアだけでなく、製品の外観を悩むデザイナーやプロジェクト全体の日程をリードするプランナー（PM）たちも、自分だけの要求事項を盛り込んだAGENTS.mdを積極的に作成・修正しながら、AIとリアルタイムで協業するようになるでしょう [[Improve your AI code output with AGENTS.md (+ my best tips)](https://www.builder.io/blog/agents-md)]。技術の壁が崩れ、誰もが自分だけの業務ルールをAIに教え、使いこなせるようになるのです。

もちろん、まだ過渡期的な技術的問題もしばしば発見されます。MicrosoftのVisual Studio Codeのような人気のあるプログラミングエディタでは、ユーザーの目につかない裏側（Background）で静かに働きながらコードを分析してくれる補助エージェント機能も提供していますが [[Using agents in Visual Studio Code](https://code.visualstudio.com/docs/agents/overview)]、一部の開発者フォーラムでは、こうしたエージェントが時折、プロジェクトの核心であるAGENTS.mdファイルのルールを正しく読み込めずに空回りするエラー事例が報告されることもあります [[Backgroundagentsdonot loadAGENTS.md... - Community Forum](https://forum.cursor.com/t/background-agents-do-not-load-agents-md/132446)]。しかし、これらの初期バグはエージェントエコシステム技術が成熟するにつれて、遠からず自然に解決されるでしょう。

## AIの視点 (AI's Take)

結論として、迫り来る未来の職場では、「1ヶ月にいくら払ってどれだけ賢い最新AIを購読するか」よりも、**「自分の賢いAIに自分の複雑な業務環境をどれだけスマートに教えるカスタマイズされたガイドブックを持っているか」**が個人と企業の成否を分ける最も重要な基準となるでしょう。

無条件に賢いAIを探すよりも、自分のAIにどのような文脈を与えてあげるかを悩むことがはるかに重要な時代になりました。結局、最高の成果を出す人工知能は、優れたアルゴリズムから生まれるのではなく、明確な人間の指示と体系的なルールから誕生するという事実を忘れてはなりません。皆さんの業務フォルダには今、AIのための親切な案内書が準備されていますか？

## 参考資料
1. [GitHub - agentsmd/agents.md: AGENTS.md — a simple, open format for guiding coding agents](https://github.com/agentsmd/agents.md)
2. [AGENTS.md](https://agents.md/)
3. [Custom instructions with AGENTS.md – Codex | OpenAI Developers](https://developers.openai.com/codex/guides/agents-md)
4. [A Complete Guide To AGENTS.md](https://www.aihero.dev/a-complete-guide-to-agents-md)
5. [Improve your AI code output with AGENTS.md (+ my best tips)](https://www.builder.io/blog/agents-md)
6. [How to write a great agents.md: Lessons from over 2,500 repositories - The GitHub Blog](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/)
7. [A good AGENTS.md is a model upgrade. A bad one is worse than no docs at all. | Augment Code](https://www.augmentcode.com/blog/how-to-write-good-agents-dot-md-files)
8. [DoAGENTS.md/CLAUDE.mdFilesHelpCodingAgents? | Towards AI](https://towardsai.net/p/machine-learning/do-agents-md-claude-md-files-help-coding-agents-a-new-paper-challenges-this)
9. [VoltAgent/awesome-design-md: A collection of DESIGN.mdfiles...](https://github.com/VoltAgent/awesome-design-md)
10. [A standardized way to give AIagentsnew capabilities and expertise.](https://agentskills.io/)
11. [Backgroundagentsdonot loadAGENTS.md... - Community Forum](https://forum.cursor.com/t/background-agents-do-not-load-agents-md/132446)
12. [Open Design — Official open-source Claude Design alternative](https://open-design.ai/)
13. [AGENTS.md & SKILL.md: The Complete Guide (2026)](https://www.morphllm.com/agents-md-guide)
14. [Instruction Files for AI Coding Assistants: An Overview](https://aruniyer.github.io/blog/agents-md-instruction-files.html)
15. [Context Engineering 2026: AGENTS.md, CLAUDE.md, and .cursorrules That ...](https://tutorials.technology/tutorials/context-engineering-claude-cursor-2026.html)
16. [Using agents in Visual Studio Code](https://code.visualstudio.com/docs/agents/overview)