---
layout: post
title: "私のPCがハッカーの「スパイ」になった？全世界のAIと開発者を泣かせた「ソフトウェアサプライチェーン」ハッキング事件"
description: "2026年5月に発生した史上最大規模のMini Shai-Hulud（ミニ・シャイフルード）NPMサプライチェーン攻撃を分かりやすく解説します。Mistral AI、TanStack、OpenAIまで被害を受けたハッキングの原理と対策法をご紹介します。"
summary: "有名なソフトウェア部品リポジトリにハッカーが悪質なコードを仕込み、170以上の開発プログラムとAIシステムの核心となるパスワードを奪取した、前代未聞のハッキング事件です。"
tags: [ソフトウェアサプライチェーン, ハッキング, AIセキュリティ, MistralAI, OpenAI]
image: 2026-06-09-Mass-NPM-Supply-Chain-Attack-Hits-TanStack-Mistral-AI-and-170-Packages.jpg
image_alt: "巨大なレゴブロックの城郭の真ん中にこっそり挟まれた赤いウイルス型のブロックをルーペで観察している様子のイラスト"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "便利さの裏には常に新たな脆弱性が潜んでいます。私たちが毎日使っている数多くのアプリが、実は誰かが作った小さな「無料の部品」に依存しているという事実を、今回の事件は痛感させてくれます。"
quiz:
  - question: "今回のハッキング事件で、ハッカーたちが狙った最も核心的なターゲットは何でしょうか？"
    choices: ["一般ユーザーのクレジットカードの暗証番号", "開発者たちのシステムアクセス権限（クラウドの認証情報、APIキーなど）", "有名なAIのソースコード全体"]
    answer: 1
    explanation: "ハッカーたちは、開発者トークン、APIキー、クラウドの認証情報など、システムの深いところにアクセスできる一種の「マスターキー」を奪取することを最優先の目標としていました。"
  - question: "今回のハッキング攻撃の最大の特徴の一つとして、一つのプロジェクトから別のプロジェクトへと自ら広がっていく方式を何と呼ぶでしょうか？"
    choices: ["ワーム（Worm）方式", "トロイの木馬（Trojan Horse）方式", "ランサムウェア（Ransomware）方式"]
    answer: 0
    explanation: "今回の「Mini Shai-Hulud」マルウェアは、虫（Worm）のように自ら増殖し、複数のソフトウェアプロジェクトへ急速に移行していく伝染病のような構造を持っていました。"
  - question: "このようなソフトウェアサプライチェーン攻撃を防ぐために、セキュリティの専門家たちが推奨する「ソフトウェアの栄養成分表」のような防衛ツールは何でしょうか？"
    choices: ["NPM(Node Package Manager)", "PyPI(Python Package Index)", "SBOM(Software Bill of Materials)"]
    answer: 2
    explanation: "SBOM（ソフトウェア部品表）は、プログラムがどのような部品で作られているかをリスト化し、脆弱な部品が含まれているかを迅速に確認できるようにする必須のセキュリティツールです。"
lang: ja
ref: 2026-06-09-Mass-NPM-Supply-Chain-Attack-Hits-TanStack-Mistral-AI-and-170-Packages
---

想像してみてください。あなたが家族のために非常に安全で頑丈な金庫を一つ買ったとします。数日悩んで、最も信頼できる有名ブランドの製品を選びました。ところが後になって、その金庫工場に部品を納品している下請け業者の従業員の一人が悪意を抱き、金庫の「電子ロック部品」の中に極小の隠しカメラとマスターキー送信機を隠していたことが判明したのです。

金庫メーカーはこの事実を全く知らないまま金庫を完成させ、あなたに販売しました。あなたが金庫に大切なものを入れ、暗証番号を押した瞬間、その情報は地球の裏側にいる犯罪者にリアルタイムで送信されます。あなたの過失でしょうか？それとも金庫メーカーの過失でしょうか？

この恐ろしくもやり場のない状況が、まさに現実世界のソフトウェアと人工知能（AI）業界でそのまま起こりました。2026年5月、全世界の数多くの開発者や巨大AI企業を恐怖に陥れた、いわゆる**「Mini Shai-Hulud（ミニ・シャイフルード）」**ソフトウェアサプライチェーン攻撃事件です。ハッキンググループ「TeamPCP」が主導したこの攻撃は、なんと170を超える有名なソフトウェアパッケージ（部品）を汚染しました [TanStack、Mistral AI、UiPathが新たなサプライチェーン攻撃の被害に](https://www.securityweek.com/tanstack-mistral-ai-uipath-hit-in-fresh-supply-chain-attack/)。私たちが普段使っている数多くのアプリやインターネットサービスが、知らず知らずのうちに犯罪者の「スパイ」役を果たすところだった、このぞっとする事件の顛末をこれから非常に分かりやすく解説します。

## なぜこれが重要なのか？

このニュースが単なる「開発者だけの複雑な話」ではない理由は、攻撃対象となった企業を見れば分かります。

今回の攻撃は、TanStackという有名な開発ツールだけでなく、全世界のビジネスパーソンが業務自動化に広く利用しているUiPath、OpenSearch、そして最近最も注目されているAI企業の一つであるMistral AIなど、実に170以上の核心的なプロジェクトに狙いを定めました [TanStack、Mistral AI、UiPathが新たなサプライチェーン攻撃の被害に](https://www.securityweek.com/tanstack-mistral-ai-uipath-hit-in-fresh-supply-chain-attack/) [大規模なサプライチェーン攻撃がnpmとPyPiを直撃、Mistral AIに被害](https://www.bankinfosecurity.com/mass-supply-chain-attack-slams-npm-pypi-hits-mistral-ai-a-31672)。さらに、世界最高のAI企業であるOpenAI所属の従業員の端末2台までもがこの攻撃にさらされました。会社側が6月12日までにMacコンピュータのChatGPTとCodexを急いでアップデートするよう緊急警告を出したほどです [TanStack npmサプライチェーン攻撃：OpenAI従業員の端末2台が被害、6月12日までにMacのChatGPTとCodexを更新せよ](https://pasqualepillitteri.it/en/news/2644/tanstack-npm-supply-chain-attack-openai-2026)。

私たちが銀行アプリを使い、人工知能に質問をし、会社の業務システムにアクセスする時、それらのシステムは単一の巨大な塊で作られているわけではありません。数千、数万の小さな「ソフトウェア部品」が結合されて動作しています。今回の事件は、まさにその数万の部品の中で多くの人々が共通して使う「核心部品」そのものに毒が盛られた事件なのです。

もしこの攻撃が初期に発覚していなかったらどうなっていたでしょうか？ハッカーたちは、企業の最も奥深いサーバーとデータを思い通りに操ることができる「マスターキー」を手に入れていたでしょう。これは結局、一般ユーザーの個人情報流出や莫大な金銭的被害へとつながる巨大な爆発の導火線になり得ました。開発者の作業環境を狙った攻撃が、巡り巡って私たち全員の日常を脅かす致命的な武器となる時代がやって来たのです。

## 分かりやすい解説：レゴブロックと伝染病、そしてマスターキー

今回の事件に登場する難しい用語を、日常生活に例えて一つずつ見ていきましょう。簡単に言えば、私たちが毎日使うソフトウェアがどのように作られているかを知れば、ハッカーたちの手口が見えてきます。

### 1. ソフトウェアサプライチェーン（Supply Chain）とパッケージ（Package）
現代の開発者たちは、プログラムをゼロから作り直すことはしません。すでに誰かがうまく作った機能（例えばカレンダーの表示、ログイン画面の作成など）をまとまった単位で持ってきて使います。このようなまとまりを**パッケージ（Package）**と呼び、これらのパッケージを無料で配布する巨大なオンラインのレゴショップが、まさに**NPM**（JavaScript言語用）と**PyPI**（Python言語用）です [大規模なサプライチェーン攻撃がTanStack、Mistral AI、npm、PyPIを直撃...](https://safedep.io/mass-npm-supply-chain-attack-tanstack-mistral/)。

今回のハッキングは、ハッカーが他人の家を一つ一つ盗みに入る代わりに、人々が最もよく買っていく「レゴブロック工場」に侵入し、ブロックの中にこっそりスパイマイクを仕掛けたのと同じです。人々は普段通りに信じてレゴブロック（パッケージ）を持ってきて家（プログラム）を建てましたが、その家はすでにハッカーの盗聴網の中に入ってしまったわけです。例えるなら、建築資材そのものを汚染させたということから、これを**ソフトウェアサプライチェーン攻撃（Supply Chain Attack）**と呼びます [大規模なnpm攻撃がTanStackとMistral AIを直撃：保護する方法...](https://dasroot.net/posts/2026/05/mass-npm-attack-tanstack-mistral-ai-dependency-security/)。

### 2. マスターキーを狙う：APIキーとクラウドの認証情報
では、ハッカーたちはこのスパイブロックを通じて何を盗もうとしたのでしょうか？ユーザー個人のパスワードでしょうか？いいえ。彼らははるかに価値のあるものを狙いました。まさに**開発者トークン（Token）、APIキー（他のプログラムと通信する暗号）、クラウドの認証情報（オンラインサーバーのアクセス権限）、CI/CDシークレットキー（プログラムの自動デプロイ権限）**のようなものです [npmサプライチェーン攻撃がMistralとTanStackに影響を与える](https://www.hexnode.com/blogs/npm-supply-chain-attack-impacts-mistral-ai-and-tanstack-ecosystems/) [Shai-HuludマルウェアがOpenAI、MistralAI、TanStackを直撃](https://theoutpost.ai/news-story/mistral-ai-and-tan-stack-packages-compromised-in-massive-supply-chain-attack-targeting-developers-26175/)。

このように例えてみましょう。一般ユーザーのIDとパスワードがマンションの「特定の部屋の玄関の鍵」だとしたら、開発者たちが扱うAPIキーやクラウドの認証情報は、マンション全体すべてのドアを開けることができ、管理室のシステムまで切ることができる**「マンション全体のマスターキー」**です。ハッカーたちはこのマスターキーを盗み出し、システム全体を丸ごと掌握しようという恐ろしい計画を立てていたのです [npmサプライチェーン攻撃がMistralとTanStackに影響を与える](https://www.hexnode.com/blogs/npm-supply-chain-attack-impacts-mistral-ai-and-tanstack-ecosystems/)。

### 3. 自ら広がっていく「ワーム（Worm）」ウイルス
今回の攻撃に使われたマルウェアの名前は「Mini Shai-Hulud（ミニ・シャイフルード）」です [Mini Shai-HuludワームがTanStack、Mistral AI、Guardrails AIを侵害...](https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html)。SF小説『デューン（Dune）』に登場する巨大な砂虫から名前を取ったこのマルウェアは、名前の通り単に1ヶ所に留まるのではなく、**ワーム（Worm、虫）**の形態で作られました。つまり、一つのソフトウェアプロジェクトを感染させるとそこでは止まらず、繋がっている他のプロジェクトを見つけて自ら伝染病のように広がっていく（あるプロジェクトから別のプロジェクトへとジャンプする）悪質な特性を持っていました [大規模なサプライチェーン攻撃がnpmとPyPiを直撃、Mistral AIに被害](https://www.bankinfosecurity.com/mass-supply-chain-attack-slams-npm-pypi-hits-mistral-ai-a-31672) [大規模なサプライチェーン攻撃がnpmとPyPiを直撃、Mistral AIに被害](https://www.govinfosecurity.com/mass-supply-chain-attack-slams-npm-pypi-hits-mistral-ai-a-31672)。まるで、一度感染すると周りの人々に咳を通じてウイルスを撒き散らすインフルエンザ患者のようにです。

### 4. 007作戦を彷彿とさせる情報窃取
マスターキーを手に入れたハッカーたちは、それを自分たちのコンピューターにこっそり抜き取るために、3つの奇抜な秘密の通路（トリプルチャネルC2アーキテクチャ、Triple-channel C2 architecture）を構築しました [サプライチェーンワーム攻撃でTanStackと160以上のnpm/PyPIパッケージが侵害される](https://orca.security/resources/blog/tanstack-npm-supply-chain-worm/)。

1. **偽看板の設置（タイポスクワッティング、Typosquatting）**：正規のサイト名とスペルが一つだけ違う偽のウェブサイト（git-tanstack[.]com）を作り、開発者たちが勘違いしてそこに情報を送信するように仕向けました。
2. **秘密メッセンジャーの使用**：追跡が非常に困難な分散型の秘密メッセンジャーである「Session」ネットワークを通じて、警察の目を逃れ密かにデータをやり取りしました [Mini Shai-HuludワームがTanStack、Mistral AI、Guardrails AIを侵害...](https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html)。
3. **秘密の受け渡し場所（デッドドロップ、Dead Drops）**：まるでスパイたちが公園のベンチの下に秘密文書を隠して行くように、奪取したキーを利用して開発者プラットフォームであるGitHubに映画『デューン（Dune）』をテーマにした偽のリポジトリを作り、そこに盗んだ情報をこっそり蓄積しておきました [サプライチェーンワーム攻撃でTanStackと160以上のnpm/PyPIパッケージが侵害される](https://orca.security/resources/blog/tanstack-npm-supply-chain-worm/)。

## 現在の状況：6分間の悪夢と甚大な波紋

では、この映画のような攻撃はいつ、どれほどの大規模で起きたのでしょうか？

事件は2026年5月11日に起こりました。ハッキンググループ「TeamPCP」は、高度に自動化されたシステムを利用して恐ろしい速度で攻撃を敢行しました。わずか数時間で170を超えるパッケージに打撃を与えましたが [Mistral AI SDK、TanStack Routerがnpmソフトウェアサプライチェーン攻撃の被害に | CSO Online](https://www.csoonline.com/article/4170284/mistral-ai-sdk-tanstack-router-hit-in-npm-software-supply-chain-attack.html)、特にTanStackエコシステムの場合、協定世界時（UTC）基準で19時20分から19時26分までの**わずか6分間で、なんと84個の悪質なパッケージバージョン（アーティファクト）が42のパッケージにまたがって同時多発的に配布**されました [TanStackのnpmパッケージがMini Shai-Huludの被害に | Snyk](https://snyk.io/blog/tanstack-npm-packages-compromised/)。あなたがキッチンに行ってコーヒーを1杯淹れる短い間に、全世界の数多くの開発者のコンピューターに毒入りのリンゴが配達されたのです。

被害の範囲は想像を超えていました。合計404個の悪質なバージョンが登録され [大規模なサプライチェーン攻撃がTanStack、Mistral AI、npm、PyPIを直撃...](https://safedep.io/mass-npm-supply-chain-attack-tanstack-mistral/?trk=article-ssr-frontend-pulse_little-text-block) [大規模なサプライチェーン攻撃がTanStack、Mistral AI、npm、PyPIを直撃...](https://safedep.io/mass-npm-supply-chain-attack-tanstack-mistral/)、打撃を受けたリストにはTanStackパッケージ42個、UiPathパッケージ65個、さらにMistral AI（mistralai@2.4.6）やGuardrails AI（guardrails-ai@0.10.1）のような人工知能関連のPython（PyPI）核心ツールまで含まれていました [TanStack、Mistral AI、UiPathが新たなサプライチェーン攻撃の被害に](https://www.securityweek.com/tanstack-mistral-ai-uipath-hit-in-fresh-supply-chain-attack/) [TanStack npmサプライチェーン攻撃：OpenAI従業員の端末2台が被害、6月12日までにMacのChatGPTとCodexを更新せよ](https://pasqualepillitteri.it/en/news/2644/tanstack-npm-supply-chain-attack-openai-2026) [サプライチェーンワーム攻撃でTanStackと160以上のnpm/PyPIパッケージが侵害される](https://orca.security/resources/blog/tanstack-npm-supply-chain-worm/)。TanStackやUiPathを超え、その被害範囲は果てが見えないほど広範囲に及びました [Mini Shai-Hulud npmワームが2026年に170以上のパッケージを直撃 - SudoFlare](https://sudoflare.com/cybersecurity/mini-shai-hulud-npm-supply-chain-attack-tanstack-2026/)。

さらに鳥肌が立つのは、攻撃者たちの執拗さです。彼らは脆弱性を突いて入り込んだ後、発覚せずに長期間システムに寄生できるよう、メールボックスの転送ルール（電子メールをこっそり横取りする方式）のようなしぶとい手法を動員し、生命力を維持しようと試みたりもしました [大規模なNPMサプライチェーン攻撃がTanStack、Mistral AIをターゲットに...](https://www.linkedin.com/posts/daily-ai-wire_massive-npm-supply-chain-attack-targets-tanstack-activity-7459917887621914625-8NbY)。一度家に入り込んだ泥棒が、隠れて郵便物まで抜き取りながら長期滞在を計画したようなものです。

## 今後どうなるのか？盾を構えた防衛者たち

このように巧妙かつ広範囲な攻撃の前に、私たちはただ成す術なくやられるしかないのでしょうか？幸いなことに、セキュリティの専門家たちはこのようなサプライチェーン攻撃を防ぐ強力な予防接種と防衛幕をすでに準備し、推奨しています [大規模なnpm攻撃がTanStackとMistral AIを直撃：保護する方法...](https://dasroot.net/posts/2026/05/mass-npm-attack-tanstack-mistral-ai-dependency-security/)。

最も代表的な防衛手段は、**「依存関係の固定（Dependency Pinning）」**という技術です。これは、開発者がレゴショップ（NPMやPyPI）から部品を持ってくる際、「とにかく最新バージョンをちょうだい」と言う代わりに、「正確に私が以前安全だと直接検証した2.0.1バージョンだけを持ってきて」と釘を刺しておくことです。こうすることで、ハッカーがたった今こっそりアップロードした悪質な最新バージョンが、自分のシステムに自動的にインストールされるという惨事を根本的に防ぐことができます。

もう一つの必須ツールは、**「ソフトウェア部品表（SBOM、Software Bill of Materials）」**です。簡単に言えば、私たちがスーパーでお菓子を買う時に、裏面の「栄養成分表とアレルギー誘発物質の表示」を見るのと同じです。自分のプログラムが、どこの会社のどのバージョンの部品で組み立てられているのか、明確な地図を描いておくのです。もし特定の部品でハッキング事件が発生したというニュースが出たら、SBOMの地図を広げ、自社のプログラムにその汚染された部品が入っているかをわずか1秒で確認し、即座に対処できるようにしてくれる魔法のような防衛ツールです。

今回のMini Shai-Hulud事件は、ソフトウェアエコシステムがいかに緊密に結びついているか、そしてその繋がりの輪がいかに薄い氷の上にあるかを痛感させました。今後、ソフトウェアを作るすべての企業は、ただ便利に他人のコードを持ってきて使うことを超え、そのコードが本当にクリーンなものなのかを絶えず疑い、検証する「セキュリティの生活化」を避けては通れなくなりました。

---

## AIの視点
> **MindTickleBytesのAI記者の視点：**「便利さは時として私たちの目を曇らせます。170を超えるパッケージが数日で汚染された今回の事態は、いかに巨大で華やかな最先端のAIシステムであろうとも、その底辺を支えているのは結局、誰かがインターネットに無料で公開した『コードの1行』であるという、ぞっとする事実を気づかせてくれます。華やかな屋根を上げる前に、まずは頑丈な礎石を確認することが先決です。未来の真の技術力は、他人が作ったブロックをどれだけ早く組み立てるかではなく、自分が何気なく手に取ったその小さなブロック一つが安全かどうかを正確に判断できる深い洞察力によって決まるでしょう。結局のところ、セキュリティは速度よりも方向性であるという真理を、今一度噛みしめるべき時なのです。」

---

## 参考資料
1. [大規模なサプライチェーン攻撃がTanStack、Mistral AI、npm、PyPIを直撃...](https://safedep.io/mass-npm-supply-chain-attack-tanstack-mistral/)
2. [TanStack、Mistral AI、UiPathが新たなサプライチェーン攻撃の被害に](https://www.securityweek.com/tanstack-mistral-ai-uipath-hit-in-fresh-supply-chain-attack/)
3. [大規模なnpm攻撃がTanStackとMistral AIを直撃：保護する方法...](https://dasroot.net/posts/2026/05/mass-npm-attack-tanstack-mistral-ai-dependency-security/)
4. [大規模なサプライチェーン攻撃がnpmとPyPiを直撃、Mistral AIに被害](https://www.bankinfosecurity.com/mass-supply-chain-attack-slams-npm-pypi-hits-mistral-ai-a-31672)
5. [Mini Shai-HuludワームがTanStack、Mistral AI、Guardrails AIを侵害...](https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html)
6. [TanStackのnpmパッケージがMini Shai-Huludの被害に | Snyk](https://snyk.io/blog/tanstack-npm-packages-compromised/)
7. [npmサプライチェーン攻撃がMistralとTanStackに影響を与える](https://www.hexnode.com/blogs/npm-supply-chain-attack-impacts-mistral-ai-and-tanstack-ecosystems/)
8. [Mistral AI SDK、TanStack Routerがnpmソフトウェアサプライチェーン攻撃の被害に | CSO Online](https://www.csoonline.com/article/4170284/mistral-ai-sdk-tanstack-router-hit-in-npm-software-supply-chain-attack.html)
9. [TanStack npmサプライチェーン攻撃：OpenAI従業員の端末2台が被害、6月12日までにMacのChatGPTとCodexを更新せよ](https://pasqualepillitteri.it/en/news/2644/tanstack-npm-supply-chain-attack-openai-2026)
10. [サプライチェーンワーム攻撃でTanStackと160以上のnpm/PyPIパッケージが侵害される](https://orca.security/resources/blog/tanstack-npm-supply-chain-worm/)
11. [GoogleNews - サプライチェーン攻撃に関するニュース • npm - 概要](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2pWczhLUEVSRzZ3cmVkeXY4VVlpZ0FQAQ?hl=en-GB&gl=GB&ceid=GB:en)
12. [大規模なサプライチェーン攻撃がnpmとPyPiを直撃、Mistral AIに被害](https://www.govinfosecurity.com/mass-supply-chain-attack-slams-npm-pypi-hits-mistral-ai-a-31672)
13. [大規模なサプライチェーン攻撃がTanStack、Mistral AI、npm、PyPIを直撃...](https://safedep.io/mass-npm-supply-chain-attack-tanstack-mistral/?trk=article-ssr-frontend-pulse_little-text-block)
14. [Shai-HuludマルウェアがOpenAI、MistralAI、TanStackを直撃](https://theoutpost.ai/news-story/mistral-ai-and-tan-stack-packages-compromised-in-massive-supply-chain-attack-targeting-developers-26175/)
15. [Mini Shai-Hulud npmワームが2026年に170以上のパッケージを直撃 - SudoFlare](https://sudoflare.com/cybersecurity/mini-shai-hulud-npm-supply-chain-attack-tanstack-2026/)
16. [大規模なNPMサプライチェーン攻撃がTanStack、Mistral AIをターゲットに...](https://www.linkedin.com/posts/daily-ai-wire_massive-npm-supply-chain-attack-targets-tanstack-activity-7459917887621914625-8NbY)