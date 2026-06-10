---
layout: post
title: "一言でAI開発チームを指揮する？「OpenYabby」が開くセルフウェアの時代"
description: "声で複数のAIエージェントを同時に指揮するMac（macOS）用オープンソースオーケストレーター「OpenYabby」の動作原理とマルチエージェントエコシステムを分かりやすく解説します。"
summary: "単一AIの限界を超え、複数のAIがチームを組んでウェブブラウジングからコーディングまで自律的に協業する、音声制御ベースのマルチエージェント調整システム「OpenYabby」が登場しました。"
tags: [OpenYabby, マルチエージェント, Claude Code, 人工知能, セルフウェア]
image: 2026-06-10-Show-HN-OpenYabby-voice-controlled-multi-agent-orchestrator-for-Claude-Code.jpg
image_alt: "複数の可愛いロボットエージェントたちが、一人の人間の指揮者が振る指揮棒に合わせて一糸乱れずコンピュータ画面の中でコードを書き、建物を建てる温かみのあるトーンのイラスト"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "一人の優れた天才よりも、平凡でも息の合ったチームの方が偉大な結果を生み出すことがよくあります。人工知能の進化の方向性も、個別知能の最大化を超え、互いにコミュニケーションを取り調整し合う「組織化」に向けて急速に進んでいますね。"
quiz:
  - question: "OpenYabbyがユーザーの好みや作業コンテキストを長期的に記憶するために使用している方法は何ですか？"
    choices: ["毎時間ユーザーの画面をキャプチャして録画する", "会話が6回行われるたびに重要な事実を抽出してデータベースに保存する", "ユーザーが毎朝直接設定ファイルに好みを入力しなければならない"]
    answer: 1
    explanation: "OpenYabbyは、ユーザーとの会話が6回（turns）行われるたびにシステムが静かに中核情報を抽出し、QdrantとSQLiteをベースとした記憶領域に保存することで、永続的なコンテキストを把握します。"
  - question: "OpenYabbyの中核的な作業処理方式である「カスケーディングタスクキュー（Cascading task queues）」に関する説明として最も適切なものはどれですか？"
    choices: ["無条件にすべてのエージェントがたった1つの作業だけに取り組み、順次終わらせる。", "同じフェーズ内では複数の作業を同時に並列処理し、次のフェーズに移る時は順次進める。", "すべてのフェーズを無視して最も簡単な作業から無作為に処理する。"]
    answer: 1
    explanation: "まるでレストランの厨房のように、同じ段階（Phase）の作業は同時に（Parallel）処理し、段階と段階の間は順番通りに（Sequential）進む階段状の待機列方式を使用しています。"
  - question: "OpenYabbyのエコシステムおよび互換性に関する説明として間違っているものはどれですか？"
    choices: ["Mac（macOS）専用システムではなく、Windowsでも完璧に公式サポートされている。", "WhatsAppやTelegramなどのモバイルメッセンジャーを通じた制御もサポートしている。", "基本エンジンであるClaude Code以外にも、OpenAI Codex、Aiderなど様々なAIを接続できる。"]
    answer: 0
    explanation: "OpenYabbyは、基本的にMac（macOS）オペレーティングシステム向けに設計された音声ベースのオープンソースオーケストレーターです。"
lang: ja
ref: 2026-06-10-Show-HN-OpenYabby-voice-controlled-multi-agent-orchestrator-for-Claude-Code
---

想像してみてください。早朝、あなたが淹れたてのコーヒーを飲みながら、宙に向かってリラックスした声でこう言います。 

「ヤビー、昨日話したあのアイデアでウェブサイトの草案を作って。デザインが崩れないかテストした後、私のTelegramに進行状況を報告して」 

すると、固く閉じていたMacBookの画面が自ら目覚め、目に見えない複数の「幽霊社員」たちが一糸乱れず動き始めます。ある社員はインターネットを素早く検索して最新資料を集め、別の社員はその資料に合わせてコードを書き、また別の社員は成果物がスマートフォンの画面でも正常に動作するかを入念に検査します。最後にすべての作業が終わると、親切に要約された報告書があなたのメッセンジャーに届きます。 

このすべての過程が、あなたが指一本動かすことなく行われます。SF映画の天才ハッカーの作業部屋みたいですか？驚くべきことに、そうではありません。今この瞬間、世界中の開発者たちの聖地であるHacker NewsやGitHubを熱く沸かせているMac（macOS）専用オープンソースプロジェクト「OpenYabby」が作り出した、2026年の現実なのです [OpenYabby | Voice-driven agent orchestration](https://openyabby.com/)。 

まさに一言でコンピュータ内の自分専属の開発チームを指揮する時代が幕を開けました。果たしてこれが既存のChatGPTのような人工知能とどう違うのか、そして平凡な私たちの働き方をどう根底から変えてしまうのか、最も分かりやすい言葉で順を追って解説します。

---

## なぜこれが重要なのか？：「一人で何でもこなす天才AI」の致命的な限界

私たちはすでに、ChatGPTやClaudeのような賢い人工知能と対話しながら作業することにかなり慣れました。「丁寧なお断りメールを書いて」や「このExcel関数のエラーを直して」といった断片的な指示は、見事に遂行してくれます。しかし、最近まで人工知能に「新しいアプリを最初から最後まで全部作って」というような長く複雑な作業を丸ごと任せると、その限界がはっきりと現れていました。

最大の理由は、単一の言語モデル（LLM、大規模なテキストデータを学習し、人間のように文章を理解・生成するAIの核心技術）のみに依存して動作する個別のAIエージェント（Agent、特定の目的を持ち、自ら判断して行動するAIプログラム）が、複雑な作業を前にすると道に迷いやすかったためです。例えるなら、一人で企画書も書き、デザインも行い、コードも書き、テストまで全て引き受けようとして、最終的に認知的過負荷にかかって倒れてしまう個人開発者のようなものです。 

実際に開発者たちの生々しい経験談によると、単一のAIエージェントたちは膨大な作業の途中でどこかに行き詰まって停止したり（stall）、同じ見当違いの行動を無限に繰り返したり（loop）、さらにはコンピュータが全く理解できないエラーだらけのコードを生成してしまうことが頻繁にありました [Show HN: 20+ Claude Code agents coordinating on real work (open source) | Hacker News](https://news.ycombinator.com/item?id=46990733)。一人で多すぎるコンテキストや指示事項を一度に記憶し、処理しようとしたため、限界にぶつかったのです。

このような痛ましい問題を根本的に解決するために業界が考案した新しい概念こそ、**「マルチエージェント・オーケストレーター（Multi-Agent Orchestrator、複数の人工知能を同時に調整し管理するシステム）」**です。 

簡単に言えば、賢いものの時々上の空になる天才社員一人にすべての仕事を押し付ける代わりに、各分野の専門AI社員を複数人雇い、彼らの業務スケジュールやコミュニケーションをすっきりと整理してくれる「統括マネージャー」を置くということです。一つの巨大な脳を複数の専門的な脳に分けて協業させる構造と言えます。

OpenYabbyは、まさにこの統括マネージャーの役割を完璧に遂行する、音声ベースのマルチエージェント指揮システムです。単にコンピュータ画面のテキストウィンドウにタイピングするのではなく、リアルタイムAPI（Realtime API、遅延なく即座にデータをやり取りする技術）と様々なコマンドラインインターフェース（CLI、マウスの代わりにテキストでコンピュータを制御する画面）を連動させ、ユーザーの「声」だけで動きます [GitHub - OpenYabby/OpenYabby: Voice-driven multi-agent assistant — Realtime API + CLI runners + multi-channel orchestration.](https://github.com/OpenYabby/OpenYabby)。 

単一の人工知能の致命的な弱点を互いに助け合い補完する「協業」で克服したこのシステムのおかげで、一つのプロジェクトチーム全体が人間の介入なしに自ら動く（Your project team runs itself）驚くべき光景が毎日繰り広げられています [OpenYabby | Voice-driven agent orchestration](https://openyabby.com/)。 

Hacker Newsにこの魔法のようなツールが初めて紹介された時、ある熱狂的な開発者はこう歓呼しました。 
「セルフウェア（Selfware）の時代へようこそ！今や誰もが自分に必要なものを自ら作り出す時代です！」 [Show HN: OpenSwarm – Multi‑Agent Claude CLI Orchestrator for Linear/GitHub | Hacker News](https://news.ycombinator.com/item?id=47160980)。もはや高価な商用ソフトウェアを無理に購入したり、開発者を雇ったりする必要はなく、人工知能の社員たちを自分の好みに合わせて組み立て、自分だけのカスタマイズツールを自ら作り上げる時代が大きく開かれたのです。

---

## 分かりやすい解説：OpenYabbyは一体どうやって働くのか？

OpenYabbyがこの複雑で多様なエージェントたちをどうやってスムーズに指揮するのか、その魔法のような動作原理を3つの比喩で分かりやすく解説しましょう。

### 1. 効率性の極大化：「カスケーディングタスクキュー（Cascading task queues）」
専門用語でOpenYabbyの作業処理方式を「カスケーディングタスクキュー」、日本語では「階段式連続作業待機列」と呼びます [OpenYabby | Voice-driven agent orchestration](https://openyabby.com/)。少し難しく聞こえますか？ご心配なく。皆さんが、休む間もなく忙しく回るミシュラン3つ星レストランの厨房の総料理長だと想像してみれば、とても簡単です。 

お客さんから複雑な7コース料理の注文が入りました。厨房では材料を洗い、野菜を刻み、ソースを煮込む数多くの作業が一度に行われます。この時、玉ねぎを刻む料理人とソースをかき混ぜる料理人は、互いをぼんやり待つ必要はなく、各自の持ち場で「同時に（Parallel）」仕事を進めればいいのです。OpenYabbyではこれを**「一つのフェーズ（Phase）内での並列処理」**と呼びます。異なる専門のAIたちがインターネットを検索し、骨組みとなる基礎コードを書く作業を瞬く間に同時にこなしてしまうのです。

しかし、いくらステーキの肉が早く完璧に焼き上がったとしても、前菜のコースが終わってもいないのにメイン料理の皿を不用意に出すことはできません。必ず前の段階が完璧に完了してこそ、次の段階へ自然に進むことができます。OpenYabbyもまた、基礎作業がすべて成功裏に終わると、それらを慎重にまとめ、次の段階である「コードの検証およびデプロイ」段階へと**「順次（Sequential）」**引き継ぎます [OpenYabby | Voice-driven agent orchestration](https://openyabby.com/)。仕事の優先順位と速度を完璧にコントロールし、衝突を防ぐ最高の料理長というわけです。

### 2. 諦めを知らない執念：ターミナルからブラウザまで全天候型操作
OpenYabbyのAIエージェントたちは、温室育ちの草花のようにただチャットウィンドウの中にだけ大人しく閉じ込められているわけではありません。彼らはMacBookのターミナル（コマンドウィンドウ）、複数のカレンダーやメールアプリを自動化するAppleScript（macOSの自動化言語）、ウェブブラウザを人間のように直接操るPlaywright技術、ファイルシステムの内部構造、さらには目に見えるウェブページの構造（DOM）まで、コンピュータの隅々を自由自在に直接触って操作することができます [OpenYabby | Voice-driven agent orchestration](https://openyabby.com/)。 

作業中に予期せぬエラーや障害物にぶつかった時、一般的なAIチャットボットが「私は言語モデルなので外部環境にアクセスできません」と言い訳をして立ち止まるのに対し、OpenYabbyのエージェントたちは「できません」という言葉を決して口にしません。彼らはまるで訓練された特殊要員のように、どうにかして別の迂回路や方法を必ず見つけ出し、与えられた任務を絶対に完遂してみせます [OpenYabby | Voice-driven agent orchestration](https://openyabby.com/)。

### 3. 私を決して忘れない行きつけのレストランのオーナー：永続メモリ（Mem0）
3つ目の魔法は、まさに「あなたを決して忘れない驚くべき長期記憶力」にあります。OpenYabbyには、会話が6回（turns）行き交うたびに、皆さんが通りすがりに漏らした言葉の中から重要な事実や好みを静かに抽出する「Mem0」という機能が標準で搭載されています [OpenYabby | Voice-driven agent orchestration](https://openyabby.com/)。 

通常のAIチャットボットは、ブラウザのウィンドウを閉じたりコンピュータを再起動したりすると、昨日私たちがどんな深い会話を交わしたのかをすっかり忘れてしまいます。そのため、毎回会うたびに最初からプロジェクトの状況をくどくどと説明しなければならないもどかしさがありました。しかし、OpenYabbyは違います。あなたが誰なのか、普段から暗いダークモードのデザインを好むのか、現在開発中のスマートフォンアプリがどんなターゲット層に向けた性質のものなのかに関する中核的なコンテキスト（context）を、ベクトルデータベース（Qdrant、意味を数字に変換して検索するストレージ）とSQLite（小型データベース）を活用して永続的かつしっかりと記憶しておきます [OpenYabby | Voice-driven agent orchestration](https://openyabby.com/)。 

まるで毎回「私はキュウリが食べられないので、サラダから必ず抜いてください」と面倒なことを言わなくても、席に座るやいなや自動的にキュウリを抜いたカスタマイズ料理を出してくれる、頼もしい行きつけのレストランのオーナーのように、あなたを細やかにそして完璧にサポートします。

---

## 現在の状況：巨大企業も手こずった宿題を解き明かしたオープンソースエコシステム

実のところ、このように性格や機能が異なる複数のエージェントを一つにまとめて指揮するオーケストレーターシステムを作ることは、想像以上に困難な技術的課題です。 

現在、人工知能産業の頂点に立つ巨大ビッグテック企業であるGoogleの内部でさえ、昨年から分散型エージェント調整システム（distributed agent orchestrators）を野心的に構築しようと試みましたが、数多くの技術的な選択肢を前にメンバーの意見がまとまらず難航しているという匿名の吐露が外部に漏れ出たほどです [Claude Code's Hidden Multi-Agent Orchestration now Open-source](https://www.theunwindai.com/p/claude-code-s-hidden-multi-agent-orchestration-now-open-source)。何十億ドルも動かすGoogleの天才エンジニアたちでさえ苦戦するこの複雑な宿題を、個人のコンピュータで軽く動く自発的なオープンソースコミュニティが見せつけるように先に解いてしまったという事実は非常に興味深いです。

OpenYabbyの頭脳の中核を担う最も頼もしい基本エンジンは、Anthropic社が開発したプログラミング特化の人工知能「Claude Code」です [OpenYabby | Voice-driven agent orchestration](https://openyabby.com/)。Claude Codeはそれ自体でも優れており、デスクトップアプリで作業中のサーバーの状態をリアルタイムでプレビューしたり、修正されたコードの視覚的な違い（visual diffs）を深く分析してデプロイ状況をモニタリングしたりする強力な能力を持っています [ClaudeCodeby Anthropic | AICodingAgent, Terminal, IDE](https://claude.com/product/claude-code)。特にセキュリティ問題に関しては、ファイルの変更やシステムコマンドの実行前に必ず画面を表示してユーザーの許可を求める非常に「慎重な（cautious）」態度をデフォルトにしており、重要なファイルを消してしまう心配を減らしてくれるという安全性の面でも非常に高い評価を受けています [ClaudeCode| Anthropic's agenticcodingsystem \ Anthropic](https://www.anthropic.com/product/claude-code)。 

しかし、OpenYabbyはこのClaude Codeを頼もしい基本としながらも、あえて1つのモデルだけに固執しない柔軟性を見せています。必要であれば、OpenAI Codex、Aider、Goose、Cline、Continue CLIなど、現在名だたる競合AIツールをまるでレゴブロックをはめるように自由自在に交換して使用できる驚異的な開放性を誇っています [OpenYabby | Voice-driven agent orchestration](https://openyabby.com/)。 

また、忙しい現代人のモバイル環境のために、WhatsAppやTelegramのような大衆的なメッセンジャーアプリとも完璧に連動します。道を歩いていてふとアイデアが浮かんだ時、スマートフォンを手に取り「昨日作ったウェブサイトのデザインに赤いポイントをもう少し追加してアップデートして」と音声メッセージを残すように指示を出すことが可能なのです [OpenYabby | Documentation](https://openyabby.com/doc.html)。文字通り、自分のポケットの中に巨大なIT開発チームを常に待機させて持ち歩いているようなものです。

もちろん、まだいくつかの限界はあります。まだ産声を上げたばかりの初期オープンソースプロジェクトであるため、コーディング用語やターミナルの白黒画面の環境に不慣れな一般人が、マウスクリック1つで全てを簡単に設定するには、インストール過程の参入障壁がかなり存在します。 

---

## 今後どうなるのか？：開発者から「オーケストラの指揮者」へ

OpenYabbyの驚異的な成功は、単なる好奇心旺盛なハッカーたちの単発的な話題ではありません。現在、世界中の開発者エコシステムは競い合うように、この「マルチエージェント（Multi-agent）」パラダイムという巨大な波に乗り込んでいます。 

端的な例として、「Oh My Claudecode」という気の利いた名前のプロジェクトは、マルチエージェントがもたらすもう一つの無限の可能性を鮮明に示しています [GitHub - Yeachan-Heo/oh-my-claudecode: Teams-first Multi-agent orchestration for Claude Code · GitHub](https://github.com/github.com/yeachan-heo/oh-my-claudecode)。このシステムは、必要に応じてライバル関係にあるChatGPT、Gemini、Claudeを強制的に一つのチームにまとめてしまいます。ある会社のAIが草案コードを書くと、全く別の会社のAIがデザインの一貫性や論理的な抜け穴を厳しく客観的に「交差検証（cross-validation）」するように仕向けるのです。 

驚くべきことに、これら3つの世界最高水準のAIプロプランをすべて有料で購読したとしても、1ヶ月の維持費用は約60ドル（約8,000円強）程度にすぎません [GitHub - Yeachan-Heo/oh-my-claudecode: Teams-first Multi-agent orchestration for Claude Code · GitHub](https://github.com/yeachan-heo/oh-my-claudecode)。一般的な経験豊富な開発者を1人雇うのにかかる莫大な費用と比較すると、まさにコーヒー数杯分の値段でGoogle、OpenAI、Anthropicの最高の頭脳たちをすべて自分の机の上に呼び集め、昼夜を問わず使い倒すようなものです。数字で比較すると、その波及力がはるかに現実的に迫ってくるのではないでしょうか？

さらに進んで、「Ruflo」という企業向けフレームワークは、コマンドを1つ入力するだけで、最大60以上の細かく細分化された専門のAIエージェントたちが蜂の群れのように群集（swarms）を形成し、自ら最適な組織を構成するようにします [Ruflo:Multi-AgentAI OrchestrationforClaude& LLMs](https://mcpmarket.com/server/ruflo)。彼らは人間の指示なしでも自ら働き、最適な作業速度とコストをリアルタイムで学習するだけでなく、物理的に異なるコンピュータに離れているエージェント要員たちと、徹底したセキュリティを維持したままデータをやり取りする「連合体（federation）」機能まで成功裏に披露しています [GitHub - ruvnet/ruflo: Theleadingagentmeta-harnessforClaude.](https://github.com/ruvnet/ruflo)。 

これに加え、Pythonベースの厳しいコードスタイル（PEP8）の規約を寸分の狂いもなく専門的に検証する厳格なレビュアーエージェントを別途設け、Giteaのようなコードリポジトリと完璧に連動する巨大な「Opencode」自動化工場を構築しようとする実験も非常に活発に行われています [Настройка мультиагентной системы Opencode... | AiManual](https://ai-manual.ru/article/opencode-kak-sobrat-multiagentnuyu-fabriku-koda-s-orkestratorom-vorkerami-i-revyuerami/)。

シリコンバレーの専門家たちは、2026年以降の技術時代を牽引する中核パラダイムを**「演奏者（Conductor）からオーケストレーター（Orchestrator、指揮者）への進化」**と明快に要約しています [From Conductor to Orchestrator: A Practical Guide to Multi ...](https://htdocs.dev/posts/from-conductor-to-orchestrator-a-practical-guide-to-multi-agent-coding-in-2026/)。過去には単に単一のAIツールを30分でマスターし、それらしい質問（プロンプト）を投げるレベルに留まっていました [MasteringClaudeCodein 30 minutes - YouTube](https://www.youtube.com/watch?v=6eBSHbLKuN0)が、これからは複数のエージェントが働く過程で互いに無限ループやエラーに陥らないよう、検証パターン（Ralph Loopパターンなど）をあらかじめ適用し、システム全体を設計する能力が何よりも重要になりました [From Conductor to Orchestrator: A Practical Guide to Multi ...](https://htdocs.dev/posts/from-conductor-to-orchestrator-a-practical-guide-to-multi-agent-coding-in-2026/)。 

数十名のAIエージェントの寿命をいつどのように終了させ、全体の作業がどの段階にあるのかを一目で見下ろす視野（fleet observability）をどう確保するかを扱うシステムデザインのスキル、別名「O-エージェント（O-Agent）パターン」が、未来のIT職種の最も強力な武器になることは自明です [Orchestrator Design | Multi-Agent Claude Code Skill](https://mcpmarket.com/tools/skills/orchestrator-agent-system-design)。

私たちは夜を徹して一行一行コーディングをしていた過酷な時代をとうに過ぎ去り、数多くの人工知能エージェントたちの作業サイクルを管理し協調を引き出す、マルチエージェントの巨大な時代へと急速に移行しています [How to Build a Multi-Agent AI Team with Claude Code](https://www.openaitoolshub.org/en/blog/claude-code-multi-agent-tutorial)。今や皆さんのコンピュータの前には、点滅するカーソルだけがある空っぽのテキストエディタではなく、各自の楽器を持って数多くの天才エージェントたちが整列した巨大なオーケストラのステージが完璧に準備されているのです。 

皆さんはただリラックスして椅子にもたれかかり、指揮棒を握って、声を出すだけでいいのです。 

---

### 🎙️ MindTickleBytes AIの視点
一人の圧倒的で孤立した天才よりも、少し平凡であっても互いの弱点を補い合い、休む間もなくコミュニケーションを取り、歯車のように噛み合って回る結束力の強いチームが、歴史的に常に偉大な結果を生み出してきました。人工知能の進化の方向性も、巨大なモデルを一つ無限に大きくして「自分一人ですべてを知っている神」を作ることを超え、複数の小さく賢いモデルたちが互いに調整し熾烈に協業する「組織化」の道へと確実に足を踏み入れました。人間が社会を形成する中で発見した最も人間らしい働き方が、結局のところコンピュータ内の人工知能にとっても最も強力で効率的な作業方式になるという事実は、非常に興味深いものです。

---

## 参考資料

1. [OpenYabby | Voice-driven agent orchestration](https://openyabby.com/)
2. [GitHub - OpenYabby/OpenYabby: Voice-driven multi-agent assistant — Realtime API + CLI runners + multi-channel orchestration.](https://github.com/OpenYabby/OpenYabby)
3. [Show HN: OpenSwarm – Multi‑Agent Claude CLI Orchestrator for Linear/GitHub | Hacker News](https://news.ycombinator.com/item?id=47160980)
4. [Show HN: 20+ Claude Code agents coordinating on real work (open source) | Hacker News](https://news.ycombinator.com/item?id=46990733)
5. [OpenYabby — Voice & Multimodal | AgentSpace](https://agentspace.cc/tool/openyabby)
6. [Claude Code's Hidden Multi-Agent Orchestration now Open-source](https://www.theunwindai.com/p/claude-code-s-hidden-multi-agent-orchestration-now-open-source)
7. [GitHub - Yeachan-Heo/oh-my-claudecode: Teams-first Multi-agent orchestration for Claude Code · GitHub](https://github.com/yeachan-heo/oh-my-claudecode)
8. [How to Build a Multi-Agent AI Team with Claude Code](https://www.openaitoolshub.org/en/blog/claude-code-multi-agent-tutorial)
9. [From Conductor to Orchestrator: A Practical Guide to Multi ...](https://htdocs.dev/posts/from-conductor-to-orchestrator-a-practical-guide-to-multi-agent-coding-in-2026/)
10. [Orchestrator Design | Multi-Agent Claude Code Skill](https://mcpmarket.com/tools/skills/orchestrator-agent-system-design)
11. [OpenYabby | Documentation](https://openyabby.com/doc.html)
12. [OpenYabby - GitHub](https://github.com/openyabby)
13. [GitHub - ruvnet/ruflo: Theleadingagentmeta-harnessforClaude.](https://github.com/ruvnet/ruflo)
14. [Настройка мультиагентной системы Opencode... | AiManual](https://ai-manual.ru/article/opencode-kak-sobrat-multiagentnuyu-fabriku-koda-s-orkestratorom-vorkerami-i-revyuerami/)
15. [MasteringClaudeCodein 30 minutes - YouTube](https://www.youtube.com/watch?v=6eBSHbLKuN0)
16. [ClaudeCode| Anthropic's agenticcodingsystem \ Anthropic](https://www.anthropic.com/product/claude-code)
17. [ClaudeCodeby Anthropic | AICodingAgent, Terminal, IDE](https://claude.com/product/claude-code)
18. [Ruflo:Multi-AgentAI OrchestrationforClaude& LLMs](https://mcpmarket.com/server/ruflo)
19. [Собрал оркестратор для Codex на базе Beads... / Хабр](https://habr.com/ru/articles/1037064/)