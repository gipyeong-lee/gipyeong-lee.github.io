---
layout: post
title: "27年隠されていたハッキングの抜け道を見つけ出したAI探知犬？私たちの電気と水道を守る「プロジェクト・グラスウィング」"
description: "Anthropicが電力、水道などの重要インフラのセキュリティのため、「Claude Mythos」AIを活用したプロジェクト・グラスウィングを150の機関に拡大します。27年前のセキュリティ脆弱性までも発見するAIの驚くべき活躍を分かりやすく解説します。"
summary: "Anthropicの最先端AI「Claude Mythos」が、世界中の電力および水道インフラをハッキングから守るため、15か国150の機関に電撃的に投入され、大規模なセキュリティ網を構築します。"
tags: [人工知能, サイバーセキュリティ, プロジェクトグラスウィング, ClaudeMythos, Anthropic, テックトレンド]
image: 2026-06-03-Expanding-Project-Glasswing.jpg
image_alt: "巨大なダムと送電塔の上にデジタルシールドが張られ、明るく輝く透明な羽を持つ蝶（グラスウィング）の形をしたAIシステムが都市全体のサイバーセキュリティ網を保護する温かみのある3Dイラスト"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "人工知能がハッカーの武器になり得るという懸念の中で、グラスウィング・プロジェクトは、AIがむしろ私たちが想像し得る最も圧倒的で頼もしい盾になり得ることを証明しています。"
quiz:
  - question: "プロジェクト・グラスウィングが新たに保護の対象とし、世界150の機関に拡大した主な重要インフラは何ですか？"
    choices: ["ソーシャルメディアとエンターテインメントプラットフォーム", "電力および水道システム", "株式取引および仮想通貨取引所"]
    answer: 1
    explanation: "最近の発表によると、プロジェクト・グラスウィングは15か国150の機関に対象を拡大し、特に電力や水道といった国家の重要インフラの保護に集中しています。"
  - question: "このプロジェクトで使用されたAIモデル「Claude Mythos」が示した独自の安全装置の特徴は何ですか？"
    choices: ["通常のAIのように、人間が事前に入力した規則にのみ従う。", "危険な要求を受けても無条件で実行する。", "基本的な安全装置がなくても、自ら危険な要求を拒否する「創発的セーフガード」を示す。"]
    answer: 2
    explanation: "Claude Mythosは、一般的な商用モデルの安全装置が取り除かれた状態でも、自ら悪意のある要求を退ける「創発的セーフガード（emergent guardrails）」という独自の防衛本能を示しました。"
  - question: "プロジェクト・グラスウィングがわずか1か月で発見した深刻なソフトウェアの脆弱性の数は、およそいくつですか？"
    choices: ["約100個", "約1,000個", "10,000個以上"]
    answer: 2
    explanation: "初期の成果発表によると、このイニシアチブを通じてわずか1か月で10,000個以上の致命的なソフトウェア脆弱性が発見されました。"
lang: ja
ref: 2026-06-03-Expanding-Project-Glasswing
---

想像してみてください。平凡な火曜日の朝、私たちが毎日飲み、洗う水を浄化する巨大な水資源公社の制御システムが突然麻痺します。数日後には、都市全体に電気を供給する主要な送電網が原因不明の理由で機能を停止し、世界が暗闇に包まれます。映画の中に登場する天才ハッカーたちの劇的なシーンのようですか？しかし、これは現実のコンピュータシステムのどこかに隠された、ごく小さな「セキュリティの穴」が一つでも開けば、いつでも実際に起こり得る恐ろしい状況です。

私たちの日常をしっかりと支えるこれらの巨大なシステムは、実は数百億行にも及ぶソフトウェアコード（コンピュータへの命令の集合）で構成されています。残念ながら、これらのコードはすべて人間が直接書いたものであるため、必然的にミスや隙間が隠れているものです。そんな中、最近、世界的な人工知能企業であるAnthropic（アンスロピック）は、見えないハッキングの脅威から私たちの日常を安全に守るための大規模な発表を行いました。それは、最先端のAIを前面に投入し、コンピュータシステムの致命的な弱点を事前に見つけ出して強固な防壁を築く**「プロジェクト・グラスウィング（Project Glasswing）」**を世界的に大幅に拡大するというニュースです [Expanding Project Glasswing \ Anthropic](https://www.anthropic.com/news/expanding-project-glasswing)。

ハッカーたちよりも一歩先んじて、コンピュータの奥深い弱点を隈なく探し出すこの賢いAIの正体はいったい何なのでしょうか？そして、この巨大なプロジェクトは今後私たちの生活をどのように変えていくのでしょうか？これから、賢くて親切な友人が温かいコーヒーを飲みながら語りかけるように、とても簡単で面白く解説していきます。

---

### これがなぜ重要なのか (Why It Matters)

私たちは通常「サイバーセキュリティ」と言うと、自分のスマートフォンがハッキングされて写真が流出したり、ウェブサイトのパスワードが盗まれたりする個人的な被害だけを思い浮かべがちです。しかし、現代社会において最も致命的で破壊的なセキュリティの脅威は、まさに**「重要インフラ（Critical Infrastructure）」**に向けられた攻撃です。重要インフラとは、国家や社会が正常に機能するために必ず必要な根幹、つまり骨組みを意味します。

今回Anthropicが発表した内容の中で、私たちが最も注目すべき部分はこのプロジェクトの保護対象です。Anthropicはプロジェクト・グラスウィングを15か国の150の機関へと大規模に拡大し、特に**「電力（Power）」と「水道（Water）」システムのような重要インフラを集中的にターゲティング**していると明らかにしました [Anthropic scales Claude Mythos to critical infrastructure in ...](https://techcrunch.com/2026/06/02/anthropic-scales-claude-mythos-to-critical-infrastructure-in-15-countries/)。

なぜ数多くの分野の中で、よりによって電気と水なのでしょうか？これらのシステムは、たった1分止まっただけでも市民の生存に直結するからです。もしハッカーが悪意を持って、水道浄化施設の化学物質の濃度を調節するソフトウェアを遠隔で操作したり、真冬に数百万世帯の暖房を担う巨大な送電網を丸ごと遮断したりすれば、その被害はお金に換算することすらできない災難となります。

これまで、こうした巨大なシステムを守る盾の役割は、世界最高のサイバーセキュリティ専門家たちの役割でした。しかし、いくら優れた専門家が数千人集まったとしても、世界中にクモの巣のように張り巡らされた膨大なソフトウェアコードを365日24時間完璧に監視することはできません。さらに、防御する側は数万回の攻撃をすべて防がなければなりませんが、攻撃するハッカーはたった一つのごく小さな隙を見つけて入り込めば勝つゲームなのです。サイバーセキュリティは常に「防御側が絶対的に不利な、傾いた運動場」での戦いでした。

しかし、絶対に疲れることなく、1秒間に数百万冊の本の分量を軽々と読みこなす圧倒的な能力を持つ人工知能が防御側の味方になってくれたらどうでしょうか？不利だった戦いの形勢が完全に覆ることになります。私たちの日常的な電気と水を24時間安全に守る、頼もしい見えない守護者が誕生したということ。これこそが、このニュースが専門家だけでなく一般人である私たちにとっても非常に重要で喜ばしい理由なのです。

---

### 分かりやすい解説 (The Explainer)

それでは、プロジェクト・グラスウィングはいったいどんな魔法を使って、コンピュータの奥深い弱点をあんなにも次々と見つけ出すのでしょうか？これを正しく理解するためには、まずこのプロジェクトの頭脳であり中核である**「Claude Mythos（クロード・ミトス）」**という非常に特別なAIモデルを知る必要があります。

**1つ目の例え：27年前の建物の巨大な設計図の中に潜むごく微細な亀裂を見つけ出す**

私たちが使用するすべてのコンピュータプログラムには、開発者本人すら気づかなかったエラーやセキュリティの隙間が潜んでいるものです。業界ではこれを主に「ゼロデイバグ（Zero-day bug、ハッカーも開発者もまだ知らない致命的なセキュリティ脆弱性）」と呼んでいます。このような弱点を見つける過程を分かりやすく例えてみましょう。

あなたが27年前に建てられた数十階建ての巨大なビルの安全検査官だと想像してみてください。あなたの前には、床から天井まで届くほど巨大な数百万枚の古い紙の設計図の山が積まれています。その設計図のどこかに、一歩間違えれば建物を一瞬で崩壊させかねない「髪の毛の太さほどの微細な亀裂」が一つ間違って描かれています。人間が何日も徹夜して探そうとしても、目が霞んで疲労が溜まり、結局決定的な手がかりを見逃してしまいがちです。

ところがClaude Mythosは、この数百万枚の設計図をたった1秒で完璧にスキャンし、27年前の建築家が疲れていて無意識に間違えて描いた微細な線1本まで正確に指摘する、超人的な視力を持った無敵の検査官なのです。人間の目と脳では到底不可能なほどの膨大な量のソフトウェアコードを瞬時に読み込み、ハッカーがこっそり侵入できるごく微細な針の穴のような隙間を指摘する役割を果たしているのです。

**2つ目の例え：大人しい盲導犬と野生の本能を秘めた特殊探知犬**

簡単に言えば、Claude Mythosは私たちが普段よく使うChatGPT（GPT-5.5）や通常のClaude（Opus 4.7）モデルとは、その出自や性格が完全に異なります。この違いを理解するために、性格の異なる2匹の犬を想像してみましょう。

私たちが知っている一般的なAIモデル（Opus 4.7、GPT-5.5など）は、訓練所で人間を助けるように徹底的に安全教育を受けた「親切で大人しい盲導犬」のようなものです。人々が危険な質問（例：ハッキングの方法を教えて）をしても絶対に応えないように、数多くの安全装置、つまり頑丈な「首輪」がつけられています。一方、セキュリティの脆弱性を専門的に狩るために特化して作られたClaude Mythosは、一般大衆には公開されていない秘密のモデルです [Anthropic Project Glasswing: AI 시대 소프트웨어 보안 협력 프레임...](https://rupijun.tistory.com/entry/Anthropic-Project-Glasswing-AI-시대-소프트웨어-보안-협력-프레임워크)。一般的な商用AIが窮屈につけている緻密な安全装置（首輪）が完全に解かれている自由な状態です。狡猾なハッカーの複雑な思考回路を同じように理解し、最も深層にある脆弱性を先んじて見つけ出すためには、AI自身が枠に囚われることなく自由奔放に考えることができなければならないからです。

ところが、本当に驚くべきことはここで発生します。外部から強制する抑圧的な安全装置が全くないにもかかわらず、Claude Mythosは一線を越える危険なサイバー攻撃の要求に対して、**自ら断固として拒否する姿（organically pushes back）**を見せたというのです [Project Glasswing: what Mythos showed us - The Cloudflare Blog](https://blog.cloudflare.com/cyber-frontier-models/)。セキュリティのために自らシステムの弱点を見つける高度な能力が備わった結果、まるで優れた知能を持つ特殊探知犬が、首輪がなくても爆発物のような致命的に危険な物を見ると、自ら吠えて後ずさりし警戒するのと全く同じわけです。

専門家たちはAIのこのような神秘的な行動を**「創発的セーフガード（emergent guardrails）」**と呼んでいます [Project Glasswing: what Mythos showed us - The Cloudflare Blog](https://blog.cloudflare.com/cyber-frontier-models/)。人間の開発者がいちいち「これは絶対にやってはいけない！」と無理やりプログラミングしたわけでもないのに、AIが複雑なシステムの構造と危険性をあまりにも深く理解したあまり、「自ら」何が一線を越える危険な行動なのかを悟ったという意味です。知能が進化するにつれて、道徳性のような防衛本能まで自ら備えたとは、本当に驚異的ではないでしょうか？

---

### 現在の状況 (Where We Stand)

このように偉大で野心的なプロジェクトは、ある朝突然パッと作られたわけではありません。Anthropicは去る2026年4月に、初めてこの驚くべきプロジェクト・グラスウィングを世に発表しました [Anthropic Project Glasswing: AI 시대 소프트웨어 보안 협력 프레임...](https://rupijun.tistory.com/entry/Anthropic-Project-Glasswing-AI-시대-소프트웨어-보안-협력-프레임워크)。初期にはAmazon、Microsoftなど、世界のIT市場を揺るがすわずか12の主要なビッグテック企業だけが密かに参加する、最精鋭の小規模エリート部隊として始まりました [2026년 핵심 소프트웨어 보안 강화 프로젝트 Glasswing 완벽 분석 | T...](https://trendpulse.blog/2026년-핵심-소프트웨어-review-2026/)。そして最近では、iPhoneで私たちの日常を掌握した巨大企業Appleまでもがこの歴史的なサイバーセキュリティ連合軍（イニシアチブ）に合流し、強力な力を添えています [Apple Joins ‘ProjectGlasswing’ Amid New Cybersecurity Push](https://azat.tv/en/apple-project-glasswing-cybersecurity/)。

普段であれば、市場シェアの1%をめぐって毎日のように銃声のない戦争を繰り広げている犬猿の仲のような競合企業たちです。しかし、彼らが企業の垣根を越え、セキュリティという巨大な目的の前に一つに固く団結した理由はただ一つです。Claude MythosというAIが示した驚異的な防衛能力が、人間の想像を完全に超えていたからです。

初期のテスト運用を行ったわずか1か月の間の結果は、セキュリティ業界を騒然とさせるほど衝撃的なものでした。Anthropicの公式な初期成果のアップデートによると、Claude Mythosを先鋒とするグラスウィング・プロジェクトは、**たった1か月でなんと10,000個を超える致命的なソフトウェアの脆弱性（Critical Vulnerabilities）を発見するという奇跡を起こしました** [Anthropic'sProjectGlasswingFinds 10,000+ Vulnerabilities... | LinkedIn](https://www.linkedin.com/posts/kdshah_project-glasswing-an-initial-update-activity-7465401472223027200-QUOc)。

この数字がどれほどすごいものかお分かりになりますか？1か月で1万個ということは、1日も休むことなく毎日300個を超える致命的なデジタル爆弾を見つけ出して除去したという意味です。これは、数百人の人間のセキュリティの天才たちが何年もかかりきりになって、ようやく見つけられるかどうかという膨大な量です。まるで映画『マトリックス』のようなSF（Sci-Fi）小説の一節のように聞こえますが、これは今私たちが生きている現実で実際に起こったことなのです [Anthropic'sProjectGlasswingFinds 10,000+ Vulnerabilities... | LinkedIn](https://www.linkedin.com/posts/kdshah_project-glasswing-an-initial-update-activity-7465401472223027200-QUOc)。

特にコンピュータの歴史に永遠に記録されるほどの、非常に大きく驚くべき成果もありました。Claude Mythosのプレビュー（Preview）モデルは、投入されてからわずか数週間で世界中の主要なコンピュータオペレーティングシステム（OS）やインターネットブラウザのコードを自律的に隈なく探し回りました [GitHub - gameworkerkim/ProjectGlasswing: Find old security ...](https://github.com/gameworkerkim/ProjectGlasswing)。その結果、世界中の開発者が毎日のように目を通していたにもかかわらず、実に**27年間もの間、誰の目にも留まることなく真っ暗闇の中に放置されていたシステム（OpenBSD）の致命的なバグ**を一気に発見しました [Project Glasswing과 Claude Mythos Preview — Anthropic의 선제적 사...](https://ice-ice-bear.github.io/ko/posts/2026-04-16-glasswing-mythos/)。

また、私たちが毎日YouTubeやNetflixなどインターネットで動画を見る時に、見えないところでよく使われているコアメディアソフトウェア（FFmpeg）に深く隠れていた**16年越しの古いバグ**までも正確に指摘しました [Project Glasswing과 Claude Mythos Preview — Anthropic의 선제적 사...](https://ice-ice-bear.github.io/ko/posts/2026-04-16-glasswing-mythos/)。人間の専門家たちがもしかして問題があるかもしれないと、500万回を超える自動化テストを機械的に回しながらも結局見逃していた針の穴を、AI探知犬がまるで幽霊のように匂いを嗅ぎつけるかのように、見事に探し出したのです [GitHub - gameworkerkim/ProjectGlasswing: Find 전 old security ...](https://github.com/gameworkerkim/ProjectGlasswing)。

---

### 今後はどうなるのか？ (What's Next)

このような目覚ましく成功した初期テスト期間を経て、Anthropicは今、より広い世界に向けて頼もしい盾を大きく広げようとしています。既存の12の大手テック企業の垣根を飛び越え、現在はなんと15か国にわたる約150の新たな主要重要機関へとClaude Mythosのアクセス権限を大幅に拡張し、戦線を広げています [Anthropic Expanding Mythos Access to 150 New Organizations](https://www.securityweek.com/anthropic-expanding-mythos-access-to-150-new-organizations/) [Anthropic Expanding Project Glasswing - SD Times](https://sdtimes.com/security/anthropic-expanding-project-glasswing/)。このプロジェクトの名前であるグラスウィング（透明な羽を持つ神秘的な蝶）のように、安全を象徴する透明な蝶の頼もしい羽が、今や数億人に達する世界中の人々の日常の上に広がり、覆いかぶさっているのです [Anthropic Lets Claude Mythos Spread ItsGlasswings](https://gizmodo.com/anthropic-lets-claude-mythos-spread-its-glasswings-2000766445)。

さらに驚くべきことであり幸いな点は、このAIが単に「ここのコードが間違っているから直してください！」と知らせる警告アラームで終わらないということです。Claude Mythosが入り込みやすいシステムの弱点（CVE、世界的に識別されたセキュリティ脆弱性）をピンポイントで発見すると、保護を受けている機関は待ってましたとばかりに即座に既存のデジタルシールド—エンドポイントセキュリティシステム（EDR、コンピュータやサーバーを細かく守る高性能ワクチン）、次世代ファイアウォール（NGFW）、ウェブアプリケーションファイアウォール（WAF）など—を積極的に活用します。これにより、危険な弱点をしっかりと包み込み、ハッカーが攻め込んでくる前に入口を完全に封鎖してしまうという即時的な防御措置（Mitigate）を取ることができるようになります [Project Glasswing Defense - Mitigate AI-Found CVEs](https://www.bing.com/aclick?ld=e8mdqNSKjitsAeQJu2_t_7IzVUCUxUlo7y7MArZWOo_p7w5CbpPpw5y2m22v-Ok7rBctiRMyegr95I7ikqaysjHLZ2URaJUqycbThDD_fl3kVVm8LOZDcEywiz4sSWIXJgxIVWLsCMUWPZ8QKvxN3ghSwKWr4WEYRgrI1sQGjN_7l0mZ2HIkTi0O6Ig-XLAXQMYJthz6r-Ug5xvsmBQgJ5no2BvHc&u=aHR0cHMlM2ElMmYlMmZ3d3cuemFmcmFuLmlvJTJmcmVzb3VyY2VzJTJmYWZ0ZXItbXl0aG9zLXByZXBhcmluZy1mb3ItY3liZXJzZWN1cml0eXMtbWFuaGF0dGFuLXByb2plY3QtbW9tZW50JTNmdXRtX2ZlZWRpdGVtaWQlM2QlMjZ1dG1fZGV2aWNlJTNkYyUyNnV0bV90ZXJtJTNkR2xhc3N3aW5nJTI2dXRtX3NvdXJjZSUzZGJpbmclMjZ1dG1fbWVkaXVtJTNkcHBjJTI2dXRtX2NhbXBhaWduJTNkTkEtU2VhcmNoLU15dGhvcy1HbGFzc3dpbmclMjZoc2FfY2FtJTNkMjM3NTMxMzA4OTclMjZoc2FfZ3JwJTNkMTIzOTE1MTAwOTk2MTc0MSUyNmhzYV9tdCUzZHAlMjZoc2Ffc3JjJTNkbyUyNmhzYV9hZCUzZCUyNmhzYV9hY2MlM2QzMjg3MDUyNjYwJTI2aHNhX25ldCUzZGFkd29yZHMlMjZoc2Ffa3clM2RHbGFzc3dpbmclMjZoc2FfdGd0JTNka3dkLTc3NDQ3NDM5OTA4ODkxJTNhbG9jLTEwMCUyNmhzYV92ZXIlM2QzJTI2bXNjbGtpZCUzZDlkZmRmZWQ5MGUzZDFjNWEzOTNhOTRjNjMzMWY5YjU2&rlid=9dfdfed90e3d1c5a393a94c6331f9b56)。

例えるなら、痛いところを見事に見つけ出す名医（AI）が診断を下すや否や、常に待機していた最新鋭の手術チーム（セキュリティシステム）が一糸乱れず投入され、病気を完璧に治療する頼もしい自動化システムが備わったということです。

今後わずか数年以内に、私たちは朝目を覚まして毎日使うスマートフォン、大切なお金が行き交う銀行アプリ、道路を走る自動車、そしてさらには私たちの家に絶えず供給されるきれいな水道と明るい電力網までもが、AIによって24時間鉄壁に守られる安全な時代を生きることになるでしょう。私たちが暖かい布団の中で深く眠りについた静かな時間にも、疲労を知らない透明な羽のAIは、数十年前に作られた古いコードの中に深く隠されたハッカーたちの抜け道をせっせと防ぎながら、私たちの平穏な明日を黙々と守ってくれていることでしょう。

---

### AIの視点 (AI's Take)
*MindTickleBytesのAI記者の視点*

「これまで人工知能技術が目覚ましく発展する中で、多くの方々が恐れ混じりの視線でAIを見つめてきました。まるで映画の中のターミネーターのように、この賢くて強力な技術が悪意のあるハッカーの鋭い槍となり、私たちの世界をより危険で不安なものにするのではないかと心配していたのは事実です。

しかし、プロジェクト・グラスウィングはその正反対の可能性をあまりにも燦然と示しています。AIはむしろ、人間の狭い視野が及ばない暗くて深いところまで明るく照らしてくれる灯台であり、私たちが想像し得る最も圧倒的で頼もしい『デジタルシールド』になり得ることを完璧な実力で証明しています。技術の爆発的な発展が決して人類を脅かす刃になるのではなく、むしろ私たちの日常を最も安全かつ温かく包み込む癒しの手へと進化しているという前向きな号砲を力強く打ち上げたと言えるでしょう。頼もしいAI探知犬と共に作り上げていく、より安全な明日が心から楽しみになる瞬間です。」

---

## 参考資料

1. [Expanding Project Glasswing \ Anthropic](https://www.anthropic.com/news/expanding-project-glasswing)
2. [Anthropic scales Claude Mythos to critical infrastructure in ...](https://techcrunch.com/2026/06/02/anthropic-scales-claude-mythos-to-critical-infrastructure-in-15-countries/)
3. [Anthropic Project Glasswing: AI 시대 소프트웨어 보안 협력 프레임...](https://rupijun.tistory.com/entry/Anthropic-Project-Glasswing-AI-시대-소프트웨어-보안-협력-프레임워크)
4. [Project Glasswing: what Mythos showed us - The Cloudflare Blog](https://blog.cloudflare.com/cyber-frontier-models/)
5. [2026년 핵심 소프트웨어 보안 강화 프로젝트 Glasswing 완벽 분석 | T...](https://trendpulse.blog/2026년-핵심-소프트웨어-review-2026/)
6. [Apple Joins ‘ProjectGlasswing’ Amid New Cybersecurity Push](https://azat.tv/en/apple-project-glasswing-cybersecurity/)
7. [Anthropic'sProjectGlasswingFinds 10,000+ Vulnerabilities... | LinkedIn](https://www.linkedin.com/posts/kdshah_project-glasswing-an-initial-update-activity-7465401472223027200-QUOc)
8. [GitHub - gameworkerkim/ProjectGlasswing: Find old security ...](https://github.com/gameworkerkim/ProjectGlasswing)
9. [Project Glasswing과 Claude Mythos Preview — Anthropic의 선제적 사...](https://ice-ice-bear.github.io/ko/posts/2026-04-16-glasswing-mythos/)
10. [Anthropic Expanding Mythos Access to 150 New Organizations](https://www.securityweek.com/anthropic-expanding-mythos-access-to-150-new-organizations/)
11. [Anthropic Expanding Project Glasswing - SD Times](https://sdtimes.com/security/anthropic-expanding-project-glasswing/)
12. [Anthropic Lets Claude Mythos Spread ItsGlasswings](https://gizmodo.com/anthropic-lets-claude-mythos-spread-its-glasswings-2000766445)
13. [Project Glasswing Defense - Mitigate AI-Found CVEs](https://www.bing.com/aclick?ld=e8mdqNSKjitsAeQJu2_t_7IzVUCUxUlo7y7MArZWOo_p7w5CbpPpw5y2m22v-Ok7rBctiRMyegr95I7ikqaysjHLZ2URaJUqycbThDD_fl3kVVm8LOZDcEywiz4sSWIXJgxIVWLsCMUWPZ8QKvxN3ghSwKWr4WEYRgrI1sQGjN_7l0mZ2HIkTi0O6Ig-XLAXQMYJthz6r-Ug5xvsmBQgJ5no2BvHc&u=aHR0cHMlM2ElMmYlMmZ3d3cuemFmcmFuLmlvJTJmcmVzb3VyY2VzJTJmYWZ0ZXItbXl0aG9zLXByZXBhcmluZy1mb3ItY3liZXJzZWN1cml0eXMtbWFuaGF0dGFuLXByb2plY3QtbW9tZW50JTNmdXRtX2ZlZWRpdGVtaWQlM2QlMjZ1dG1fZGV2aWNlJTNkYyUyNnV0bV90ZXJtJTNkR2xhc3N3aW5nJTI2dXRtX3NvdXJjZSUzZGJpbmclMjZ1dG1fbWVkaXVtJTNkcHBjJTI2dXRtX2NhbXBhaWduJTNkTkEtU2VhcmNoLU15dGhvcy1HbGFzc3dpbmclMjZoc2FfY2FtJTNkMjM3NTMxMzA4OTclMjZoc2FfZ3JwJTNkMTIzOTE1MTAwOTk2MTc0MSUyNmhzYV9tdCUzZHAlMjZoc2Ffc3JjJTNkbyUyNmhzYV9hZCUzZCUyNmhzYV9hY2MlM2QzMjg3MDUyNjYwJTI2aHNhX25ldCUzZGFkd29yZHMlMjZoc2Ffa3clM2RHbGFzc3dpbmclMjZoc2FfdGd0JTNka3dkLTc3NDQ3NDM5OTA4ODkxJTNhbG9jLTEwMCUyNmhzYV92ZXIlM2QzJTI2bXNjbGtpZCUzZDlkZmRmZWQ5MGUzZDFjNWEzOTNhOTRjNjMzMWY5YjU2&rlid=9dfdfed90e3d1c5a393a94c6331f9b56)