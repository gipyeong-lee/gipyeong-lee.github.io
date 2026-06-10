---
layout: post
title: "賢すぎて「監視」されるAI？Claude Mythosとデータ共有の秘密"
description: "Anthropicの超強力な第5世代AI「Mythos」と「Fable 5」をAWS Bedrockで利用するには、なぜ30日間のデータ共有が必要なのでしょうか？新しいセキュリティポリシーをわかりやすく解説します。"
summary: "Anthropicは、一般公開が難しいほど強力な「Mythos」クラスのAIモデルの悪用を防ぐため、ユーザーデータを30日間保管し、安全性を検査する新しい規定をAWSクラウドに導入しました。"
tags: [人工知能, セキュリティ, クラウド, Anthropic]
image: 2026-06-10-AWS-Bedrock-to-require-sharing-data-with-Anthropic-for-Mythos-and-future-models.jpg
image_alt: "データセキュリティの南京錠に繋がれた光り輝く人工知能の脳の様子"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "強大な力には必ずそれに相応しい統制が伴うものです。今回の措置は、AI発展の中心軸が無条件の「性能競争」から実質的な「安全管理」へと移行していることを示す象徴的な出来事です。"
quiz:
  - question: "Anthropicの「Mythos」クラスのAIモデルを利用するために求められるデータ保管期間はどれくらいですか？"
    choices: ["7日間", "15日間", "30日間"]
    answer: 2
    explanation: "Anthropicは、Mythos 5、Fable 5などMythosクラスのモデルのトラフィックについて、信頼と安全を目的とした30日間のデータ保管を要求しています。"
  - question: "保管されるユーザーのデータは最終的にどこに保存されますか？"
    choices: ["Anthropicの公開トレーニングサーバー", "ユーザーのAWS環境内", "インターネット上のパブリッククラウド"]
    answer: 1
    explanation: "データ共有オプションをオンにしても、該当データは顧客（ユーザー）のAmazon Web Services（AWS）環境内に安全に留まり、統制されます。"
  - question: "Claude Mythosが非公開の研究という形で制限的にのみ提供されている核心的な理由は何ですか？"
    choices: ["一般公開するにはあまりにも強力すぎるため", "まだ開発が完了しておらずエラーが多いため", "サーバーの維持費用が高すぎるため"]
    answer: 0
    explanation: "Anthropicは、Claude Mythosがコーディングやサイバーセキュリティなどで圧倒的な能力を示し、「一般公開するには強力すぎる」と判断し、Glasswingプロジェクトを通じて制限的にのみアクセスを許可しました。"
lang: ja
ref: 2026-06-10-AWS-Bedrock-to-require-sharing-data-with-Anthropic-for-Mythos-and-future-models
---

## はじめに：魔法の杖屋の怪しい契約書

**想像してみてください。** あなたが世界を変えられるほどの凄まじい能力を持つ魔法の杖をレンタルしに店へ行きました。ところが、店主が険しい表情で契約書を差し出し、こう言います。「この杖はあまりにも能力が高すぎるため、誰にでもそのまま貸し出すことはできません。もし借りていきたいのなら、あなたがこの杖でどんな魔法の呪文を唱えるのか、今後30日間私たちが監視することを許可していただかなければなりません。」

まるでファンタジー映画に出てきそうな話に聞こえるかもしれませんが、驚くべきことに、これこそが今日世界で最も賢い人工知能（AI）の一つを利用するために、企業が実際に結ばなければならない契約条件なのです。2026年4月、AI専門企業Anthropicは、同社の最新の第5世代AIモデルをリリースするにあたり、クラウドサービスプラットフォームであるAmazon Bedrockに非常に異例かつ強力な新しいルールを掲げました [AnthropicのClaude Fable 5がAmazon Bedrockで利用可能に](https://www.aboutamazon.com/news/aws/claude-fable-5-anthropic-available-amazon-bedrock)。

新しいルールの核心は明確です。それは、「Mythos 5」や「Fable 5」のような超高性能AIを利用するには、ユーザーがAIに入力するすべての質問とAIが返す回答データを30日間Anthropicと共有しなければならないということです [AWS上のAnthropic Claude Fable 5：Mythosクラスの機能と組み込みのセーフガードが利用可能に](https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/)。正当にお金を支払って利用するプライベートサービスなのに、一体なぜわざわざ会話の内容を検閲されなければならないのでしょうか？なぜこれほどまでに厳格な条件が生まれたのか、そしてこれが今後私たちのデジタルプライバシーや日常にどのような意味を持つようになるのか、順を追ってわかりやすく見ていきましょう。

---

## なぜこれが重要なのか？ (Why It Matters)

### 「一般公開するにはあまりにも強力すぎる」

このすべての見慣れない状況の発端は、人工知能の知能レベルが今や私たちの想像を超えるほど高くなったためです。わずか2年前の2024年4月、Amazon Bedrockに「Claude 3」が初めて登場した時でさえ、人々はその賢い性能に感嘆し、比較的自由にAIを業務に活用していました [Amazon BedrockがClaude 3 Anthropic AIモデルを追加](https://www.aboutamazon.com/news/aws/amazon-bedrock-anthropic-ai-claude-3)。

しかし、2026年4月7日に登場した新しいモデルは完全に次元が違いました。Anthropicが「Claude Mythos」をAmazon Bedrockに独占的に披露したとき、彼らは自ら作り出したこのモデルを指して**「一般公開するには強力すぎる（too powerful to be released publicly）」**と評価し、警戒心を露わにしました [Claude MythosがAWS Bedrockに登場。エンジニアが知っておくべきこと](https://dev.to/ajbuilds/claude-mythos-is-on-aws-bedrock-heres-what-engineers-need-to-know-2lhj)。

この言葉が単なるマーケティング用の誇張やハッタリではないことは、すぐに数値によって証明されました。人工知能が複雑なソフトウェアの欠陥を自ら見つけて修正する能力を評価する非常に権威あるテスト「SWE-bench Verified」において、Mythosはなんと**93.9%**という記録的なスコアを達成しました [Claude MythosがAWS Bedrockに登場。エンジニアが知っておくべきこと](https://dev.to/ajbuilds/claude-mythos-is-on-aws-bedrock-heres-what-engineers-need-to-know-2lhj)。体感しやすく説明すると、世界で最も難しいプログラミングのエラーが100問与えられた時、そのうち94問を自力で完璧に解き明かすレベルに達したということです。

### コーディングの天才が最悪のハッカーに豹変するのを防ぐために

この93.9%という驚くべき数字が、私たちのような一般人にとって何を意味するのでしょうか？人間のプログラマーが数十人がかりで何日も徹夜してようやく見つけ出し修正できるような高難度のシステムエラーを、AIがたった数秒で瞬時に把握し、完璧に直すことができるという意味です。実際にMythos 5やFable 5のような第5世代AIは、コーディング、複雑な知識作業（knowledge work）、そして視覚情報分析（vision）の分野において、まさに圧倒的で驚異的な性能を誇っています [AnthropicのClaude Fable 5がAmazon Bedrockで利用可能に](https://www.aboutamazon.com/news/aws/claude-fable-5-anthropic-available-amazon-bedrock)。

しかし、技術の世界では光が強ければ強いほど影も濃くなります。「システムのエラーを見事に探し出す天才的な能力」は、コインの裏表のように「システムの弱点（脆弱性）を鬼のように探し出し、致命的な攻撃を加えることができる能力」と完全に同じです。わかりやすく言えば、世界のあらゆる南京錠の構造を見抜いている天才鍵師を思い浮かべてみてください。この鍵師は誰よりも頑丈なセキュリティ装置を作ることができますが、その気になればどんなに鉄壁の金庫でも痕跡を残さずに開けてしまうこともできるのです。

サイバーセキュリティ業界では、Mythosの登場を単なる新製品のリリースではなく、AIを活用した脆弱性発見（vulnerability discovery）やハッキング・セキュリティ作戦が全く新しい次元に突入したシグナルとして重く受け止めています [AWS Bedrock Claude Mythos プレビュー：防衛的AIセキュリティ...](https://murtaza-arif.github.io/blog/aws-bedrock-claude-mythos-preview-glasswing-playbook)。もしこのような超強力な知能が悪意のあるハッカー集団の手に渡れば、全世界の銀行網を突破したり、国家の通信網を麻痺させたりする致命的なコンピューターウイルスを一瞬にして自動生成してしまうかもしれません。

そのため、Anthropicはこのモデルを誰でもお金さえ払えば使えるようにはしませんでした。代わりに、ただ「Glasswingプロジェクト（Project Glasswing）」という、徹底的に統制された研究目的のプレビュー（gated research preview）という形で限定的にのみ世に送り出しました [Claude MythosがAWS Bedrockに登場。エンジニアが知っておくべきこと](https://dev.to/ajbuilds/claude-mythos-is-on-aws-bedrock-heres-what-engineers-need-to-know-2lhj)。とてつもなく強力で危険になりうる猛獣を非常に頑丈な檻の中に閉じ込めたまま、許可された人間だけが慎重に観察できるようにしたようなものです。

---

## わかりやすく解説 (The Explainer)

では、Anthropicが用意したこの「安全装置」は一体どのような仕組みで機能するのでしょうか？彼らが導入した最も核心的な盾こそが、先ほど言及した**「30日間のデータ保管（30-day data retention）」**の義務です。

### ブラックボックスを設置する：30日間の透明な監視

現在、Mythos 5やFable 5のように人類が到達した最高レベルの能力を備えた「Mythosクラス（Mythos-class）」のモデルをクラウドで利用するには、ユーザーはシステム設定で特別なセキュリティスイッチを必ず一つオンにしなければなりません。それが**「プロバイダーとのデータ共有（provider_data_share）」**というオプションです [データ保持 - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html)。

このオプションをオンにすると、ユーザーがAIに投げかけるすべての質問（prompt）と、それに応じてAIが返すすべての回答（completion）の記録が、モデルを作成したAnthropic側と共有され、最大30日間安全に保管されます [データ保持 - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html)。

この状況は、非常に精密ですが一歩間違えれば大事故を引き起こしかねない危険な特殊重機をレンタルするプロセスに例えることができます。レンタル会社はあなたに機材を貸し出しながらこう言います。「この機材には、電源を切ることも操作することもできないブラックボックスが付いています。今後30日間、あなたがこの機材を使って何かを建設しているのか、それとも危険に破壊しているのかを、私たちが随時記録を開いて確認する権利があります。」

このようなモニタリングの目的はただ一つです。この天才的なAIが致命的な兵器の設計、大規模なハッキングスクリプトの自動作成、あるいは深刻な犯罪の謀議などに悪用（abuse）されていないかを監視することです。Anthropicはこれを、ひたすら**「信頼と安全性（trust and safety purposes）」**を担保するための不可欠な手続きだと説明しています [データ保持 - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html)。

### 私たちの貴重なプライバシーは諦めなければならないのか？

このくだりで、人工知能を導入しようとする多くの企業は背筋が寒くなるような大きな不安を覚えます。「私たちが数百億円をかけて開発中のトップシークレットである新製品のコアコードをAIに分析してくれと頼めば、その貴重なデータがすべてAnthropicの中央サーバーにそっくりそのまま渡り、外部に流出してしまうのではないか？」という非常に合理的な懸念です。

幸いなことに、Amazon BedrockプラットフォームとAnthropicはプライバシーと安全の間の賢明な妥協点を見出しました。30日間保管されるユーザーの機密データは、Anthropicの外部サーバーへ無断で持ち出されたりコピーされたりすることはありません。代わりに、データ保管オプションがオンになった状態で、徹底して**「顧客（ユーザー）独自のAWS環境内（stays in your AWS environment）」**に安全に留まるよう設計されています [Mythosクラスモデルのデータ保持に関する実践 | Claudeヘルプセンター](https://support.claude.com/en/articles/15425996-data-retention-practices-for-mythos-class-models)。

例えるなら、顧客が作成した書類をAnthropicの従業員が自社に持ち帰って読むわけではありません。顧客の家の裏庭に用意された頑丈な金庫の中に書類を入れておき、Anthropicの検査官が「訪問者」の資格でその金庫室に入り、内容物に危険なものがないかだけを素早く確認して帰っていく方式に近いと言えます。

そしてここで最も重要な事実があります。顧客が入力した質問とAIの回答内容（Customer Content）が、将来Anthropicが次世代の新しいAIを「トレーニング（train）」するための材料としては絶対に、決して使用されないという点です [AWS BedrockとMIMIC · MIT-LCP mimic-code · Discussion #1747](https://github.com/MIT-LCP/mimic-code/discussions/1747)。Anthropicは、ユーザーが安全ポリシーを正しく遵守しているかモニタリングするための限定的な目的でのみこのデータを閲覧し、徹底して「安全確認用」にのみ使われるという点を契約上明確にしています。

---

## 現在の状況 (Where We Stand)

このようなポリシー変更により、今日、世界最高の人工知能を自分の業務に利用するプロセスは、まるで誰でも入れるわけではない厳格なVIPの秘密クラブに入会するかのごとく、非常に厳しく細かいものになりました。

### 複雑化した通過儀礼：深層面接と書類審査

過去には、Amazon Bedrockプラットフォームが様々な基盤モデル（人工知能の脳の役割を果たす巨大な基本モデル）へのアクセスを非常に簡素化（simplified model access）していたため、ただ規約に同意し、ボタンを数回クリックするだけで、誰でも簡単にAIを呼び出して使うことができました [アクセスリクエスト：BedrockでAnthropicモデルを有効にする...](https://repost.aws/questions/QUjAsyAhb3RGyKpF9oF-RVhg/access-request-enable-anthropic-models-in-bedrock-for-enterprise-internal-research)。

しかし、Anthropicの超高度化されたMythosクラスのモデルは、この簡便な手続きの例外となりました。現在、この強力なモデルを業務に利用するには、サードパーティ（third-party）モデルプロバイダーであるAnthropicの厳しい要求に従い、**「初回利用フォーム（First Time Use, FTU form）」**という文書を義務的に漏れなく作成し、審査を通過しなければなりません [モデルへのアクセスのリクエスト - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html)。このフォームは、まるで危険な化学物質の取り扱い許可証を受け取るようなものです。「当社はこの強力なAIを正確にどのような用途（use case details）で使用するのか」を非常に詳細かつ透明に明らかにし、安全性を証明して許可を得なければならない一種の「深層面接」を受けなければなりません [アクセスリクエスト：BedrockでAnthropicモデルを有効にする...](https://repost.aws/questions/QUjAsyAhb3RGyKpF9oF-RVhg/access-request-enable-anthropic-models-in-bedrock-for-enterprise-internal-research)。

書類審査を通過したからといって終わりではありません。従業員のどのコンピューターからでもむやみにアクセスできるわけでもありません。AWSの厳格なデジタル身分証検査システムである「Identity and Access Management（IAM）」を通じ、社内でも徹底的に指定された特定の国と許可された地域のサーバーからのみAIにアクセスするよう、権限ポリシーを暗号化されたコードで緻密に設定しておいてこそ、初めてAIモデルを呼び起こす（InvokeModel）ことができます [Amazon Bedrock上のAnthropicモデルへのアクセス | AWS re:Post](https://repost.aws/knowledge-center/bedrock-access-anthropic-model)。この複雑な通信のプロセスはすべて、AWSの巨大なインフラ上で特別に暗号化された `/anthropic/v1/messages` 専用経路（Messages API）を通じてのみ、密かに安全に行われます [Amazon BedrockのClaude - Claude APIドキュメント](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)。

### リアルタイム監視と課金ポリシー：「危険であれば途中で容赦なく言葉を遮ります」

苦労して審査を通過しモデルを使い始めたとしても、ユーザーに対する監視はリアルタイムで1分1秒たりとも休まずに行われます。モデルの内部には、会話の内容をリアルタイムで読み取り、危険性を判断する「コンテンツ分類器（content classifier）」という番人が組み込まれているためです。興味深いのは、この監視システムが作動する際に計算される「料金請求方式」です。

例を挙げてみましょう。ユーザーがAIに不純な意図を抱き、「競合他社のサーバーのセキュリティ網をこっそり突破してハッキングする方法を段階的に教えて」と尋ねたと想像してみてください。AIがこの質問を聞くやいなや、1秒の躊躇もなく**「その質問には安全規定上お答えできません」**と断固として拒否（refusal）した場合、どうなるでしょうか？人工知能の世界では、AIが生成する単語（トークン）の数だけ費用を支払わなければなりません。しかし、このように推論（回答生成）が始まる前に防御システムが即座に作動して会話を遮断した場合には、ユーザーにいかなる単語費用も請求されません [Anthropic - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-anthropic.html)。

しかし、もっと恐ろしい（？）状況は他にあります。ユーザーが一見するとごく平凡で複雑なプログラミング関連の質問を投げかけました。AIがそれに合わせて流暢にコードを吐き出し始めますが（streaming）、ふと文脈を把握してみると、自分が今、致命的なランサムウェア・ウイルスを作るためのコードを組んでしまっているという事実に遅ればせながら気付きました。この時、AIはその場ですぐに言葉を止め、口を固く閉ざしてしまいます。これを業界では**「中間拒否（Mid-stream refusals）」**と呼んでいます [Anthropic - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-anthropic.html)。

まるで通話中に相手が違法な発言を始めるやいなや、さらに深い話になる前に電話をガチャンと切ってしまうようなものです。この場合は、回答が遮断される直前までAIが既に口を開いて吐き出した単語（トークン）分の料金は、ユーザーがそのまま支払わなければなりません。つまり、超強力なAIはユーザーの指示通りに無条件に服従する機械ではなく、会話の途中であってもいつでも「これは人間にとって危険なのでやめておきます」と容赦なく会話を断ち切る（stop_reason: "refusal"）ことができる強力な自律的統制権限を握っているわけです [Anthropic - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-anthropic.html)。

---

## 今後はどうなるのか？ (What's Next)

私たちを驚かせた今回のAnthropicの「30日間のデータ保管」と「リアルタイムの安全監視」措置は、単なる一過性のハプニングや実験で終わることはない見通しです。

Anthropicは既に、現在のFable 5とMythos 5だけでなく、**「今後Bedrockクラウドでリリースされる同等あるいはそれ以上の凄まじい能力を持つ未来のモデルたち（future models on Bedrock with similar or higher capability levels）」**に対しても、この30日間の保管ポリシーを同様に、あるいはさらに厳格に要求することを明確に宣言しています [AWS上のAnthropic Claude Fable 5：Mythosクラスの機能と組み込みのセーフガードが利用可能に](https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/)。

このような宣言は、近づきつつある新しいAI時代に大きなパラダイムシフトが起こりつつあることを予告しています。わずか1〜2年前の過去には、「どの会社が人間の言葉をより理解し、より人間のように賢い人工知能を早く作り出すか」がシリコンバレーの唯一の話題でした。しかし今、争点は「そうして作り出した圧倒的な知能を、誰がよりコントロール可能な範囲内で安全かつ被害をもたらさずに稼働させられるか」へと完全に移行しつつあります。

多くの企業やユーザーは今、避けては通れない重大な選択の岐路に立たされることになるでしょう。「社内の完璧なデータ機密保障（プライバシー）を守るために、少し賢さが劣っても旧型AIを安全に自社サーバーに置いて使うか？」それとも「グローバル市場での生き残りと競争のために、圧倒的に仕事が速い最新の天才AIを導入する代わりに、30日間のセーフティネット監視という後味が悪く不便な条件を喜んで受け入れるか？」人工知能が人間の知的労働を丸ごと代替するほど目覚ましく進化すればするほど、その副作用を防ぐために私たちが耐え忍ばなければならない「安全装置」の重みも、それだけ重くなっているのです。

---

## AIの視点 (AI's Take)

**MindTickleBytesのAI記者の視点：**
人類の歴史において、爆発的な性能の向上は常に新たな制約を伴ってきました。かつてプロペラ飛行機がジェットエンジンを搭載して超音速旅客機へと発展した際、上空での致命的な乱気流の危険性を防ぐために、乗客を縛り付ける「シートベルト」や「酸素マスク」といった新たな制約が不可欠として導入されたのと同じです。限りなく自由に空を飛びたいと願っても、強大な力には必ずそれに相応しい統制が伴うものなのです。

Anthropicの今回の措置は、AI技術発展の中心軸が無条件の「性能と速度の競争」から実質的な「安全と倫理の管理」へと成熟して移行していることを示す、非常に象徴的な出来事です。少し窮屈で監視されているような気がするかもしれません。しかしこれは、技術の凄まじい進歩が最終的に人類にとって取り返しのつかない毒にならないようにするための、多少不便ではあっても私たち全員の生存のために健全かつ不可欠な陣痛の過程だと言えます。

---

## 参考資料

1. [AWS上のAnthropic Claude Fable 5：Mythosクラスの機能と組み込みのセーフガードが利用可能に](https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/)
2. [Amazon BedrockのClaude - Claude APIドキュメント](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)
3. [AnthropicのClaude Fable 5がAmazon Bedrockで利用可能に](https://www.aboutamazon.com/news/aws/claude-fable-5-anthropic-available-amazon-bedrock)
4. [Claude MythosがAWS Bedrockに登場。エンジニアが知っておくべきこと](https://dev.to/ajbuilds/claude-mythos-is-on-aws-bedrock-heres-what-engineers-need-to-know-2lhj)
5. [Amazon Bedrock上のAnthropicモデルへのアクセス | AWS re:Post](https://repost.aws/knowledge-center/bedrock-access-anthropic-model)
6. [AWS BedrockとMIMIC · MIT-LCP mimic-code · Discussion #1747](https://github.com/MIT-LCP/mimic-code/discussions/1747)
7. [Anthropic - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-anthropic.html)
8. [AWS Bedrock Claude Mythos プレビュー：防衛的AIセキュリティ...](https://murtaza-arif.github.io/blog/aws-bedrock-claude-mythos-preview-glasswing-playbook)
9. [アクセスリクエスト：BedrockでAnthropicモデルを有効にする...](https://repost.aws/questions/QUjAsyAhb3RGyKpF9oF-RVhg/access-request-enable-anthropic-models-in-bedrock-for-enterprise-internal-research)
10. [Amazon BedrockがClaude 3 Anthropic AIモデルを追加](https://www.aboutamazon.com/news/aws/amazon-bedrock-anthropic-ai-claude-3)
11. [データ保持 - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html)
12. [Mythosクラスモデルのデータ保持に関する実践 | Claudeヘルプセンター](https://support.claude.com/en/articles/15425996-data-retention-practices-for-mythos-class-models)
13. [モデルへのアクセスのリクエスト - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html)
14. [Amazon Bedrockでの簡素化されたモデルアクセス | AWSセキュリティブログ](https://aws.amazon.com/blogs/security/simplified-amazon-bedrock-model-access/)