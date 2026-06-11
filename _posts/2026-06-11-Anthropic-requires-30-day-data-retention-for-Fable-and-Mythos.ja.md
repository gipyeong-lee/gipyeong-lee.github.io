---
layout: post
title: "私の質問を30日間保存する？Anthropicの新しいAIポリシーが物議を醸している理由"
description: "Anthropicが最高性能のAIであるClaude Fable 5とMythos 5をリリースし、30日間のデータ保持ポリシーを強制しました。企業が反発し、Microsoftが社内利用を制限した理由をわかりやすく解説します。"
summary: "強力な性能を持つ新しいAIモデルが、システムの安全監視を理由にユーザーの質問と回答を30日間強制的に保存することになり、企業秘密の流出を懸念した主要企業が使用を制限するなど、プライバシーに関する論争が拡大しています。"
tags: [Anthropic, Claude, プライバシー, AIの安全性, エンタープライズ, サイバーセキュリティ]
image: 2026-06-11-Anthropic-requires-30-day-data-retention-for-Fable-and-Mythos.jpg
image_alt: "防犯カメラが作動している部屋の中で重要書類を検討している賢いロボットの姿"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "より賢いAIがもたらす利点を享受するために、私たちはどこまでプライバシーを譲歩すべきでしょうか？強力な技術統制とデータ主権の間の激しい綱引きが、今まさに本格的に始まりました。"
quiz:
  - question: "AnthropicがClaude Fable 5とMythos 5に新たに導入したデータ保持期間はどれくらいですか？"
    choices: ["保存しない（即時削除）", "30日", "1年"]
    answer: 1
    explanation: "Anthropicは、システムの安全監視を名目に、すべてのプロンプトと生成物を最低30日間義務的に保存するポリシーを適用しました。"
  - question: "企業顧客が以前Anthropicと結んでいた「ゼロリテンション（データの即時削除）」契約は、この新しいポリシーの下でどのように扱われますか？"
    choices: ["既存の契約が優先され、引き続き維持される", "新しい30日間の保持ポリシーが既存の契約を無効化し、強制的に適用される", "ユーザーが保存の有無を自由に選択できる"]
    answer: 1
    explanation: "新しい30日間のデータ保持義務ポリシーは、企業が以前に締結していたゼロリテンション契約をすべて強制的に無効化（override）し、最優先で適用されます。"
  - question: "Microsoftが自社従業員のClaude Fable 5の使用を制限した主な理由は何ですか？"
    choices: ["競合モデルのシェアを下げるため", "新しいデータ保持ポリシーによる社内機密情報の流出やプライバシー侵害の懸念のため", "AIモデルのコーディング能力が著しく低いため"]
    answer: 1
    explanation: "Microsoftは、Anthropicの強制的な30日間のデータ保持ポリシーが企業のデータプライバシーに深刻なリスクをもたらすと判断し、社内での使用を全面的に制限しました。"
lang: ja
ref: 2026-06-11-Anthropic-requires-30-day-data-retention-for-Fable-and-Mythos
---

想像してみてください。あなたが職場で、会社の運命を左右する非常に重要な新製品の発売計画や、コア技術の骨格となる設計図を作成しているとします。一人でこの膨大な作業を処理するのはあまりにも大変なので、とても賢くて仕事の処理速度が速いAIアシスタントに助けを求めることにしました。

「当社の極秘レシピと核心的なマーケティング戦略の資料を渡すから、明日の朝の役員向けプレゼン資料として完璧にまとめて。」

幸いなことに、この優秀なアシスタントは「先ほど見た文書の内容は、業務が終わり次第、頭の中から完全に消去する」という徹底した機密保持の誓約書をすでに交わしている状態です。あなたは安心して会社の未来がかかった機密文書をアシスタントの手に委ねました。

ところがある日、このアシスタントが自身の業務能力を大幅にアップグレードしたと言って、突然態度を変えます。「これからは私が賢くなりすぎたため、もしかすると私が扱う情報が悪い犯罪に巻き込まれるのではないかと恐れています。そのため、安全を確認するために、あなたがくれたすべての文書を『30日間』私の個人金庫に義務的に保管し、監視しなければなりません。以前書いた即時削除の誓約書は、本日をもって全面無効です。」

あなたなら、このアシスタントに引き続き会社の最高機密を安心して任せることができるでしょうか？おそらくほとんどの人は、慌てて書類を取り上げ、今すぐ部屋を出ていくでしょう。

まさにこの戸惑うようなシナリオが、現在世界中のグローバルIT業界の現実としてそのまま起こっています。2026年6月9日、著名な人工知能企業であるAnthropicが、自社の歴代最高性能のAIモデルである「Claude Fable 5」と、さらに専門的で限定的なバージョンである「Mythos 5」を電撃的にリリースしました [[AnthropicのClaude Fable 5に対する新しい30日間のデータ保持は...](https://www.linkedin.com/pulse/does-anthropics-new-30-day-data-retention-claude-fable-jonathan-milne-qhrfe)]。

しかし、世間の熱い関心は、これらのモデルが示す驚異的な知能や圧倒的なコーディングスキルではありませんでした。人々の視線は、彼らが新たに掲げた「データの30日間強制保存」という隠された請求書に鋭く注がれています。

オンラインコミュニティやインターネット空間はすぐに激しい怒りで沸き返り [[Claude Fable 5のリリース後、インターネットはAnthropicに激怒している - Decrypt](https://decrypt.co/370688/internet-furious-anthropic-claude-mythos-fable-5)]、Microsoftをはじめとする主要な巨大テック企業は、セキュリティ部門に直ちに非常ベルを鳴らしました。世界最高レベルの能力を備えたAIが華々しく登場したのに、拍手と歓声の代わりに懸念と警戒心が注がれる理由。果たして舞台裏で何が起こっているのでしょうか？

## なぜこれが重要なのか？ (Why It Matters)

AI技術が飛躍的に発展するにつれて、現代の企業や個人は、過去とは比較にならないほど機密性の高い情報をAIシステムに入力し、その結果に依存するようになっています。

ソフトウェアエンジニアは、企業の核心となるソースコードを書く際にAIの助けを借りて作業時間を短縮し、医師は病院の複雑な患者データを分析してより正確な診断を下そうとし、財務の専門家はまだ世間に公開されていない企業の業績表をAIに事前に検討させます。このように致命的で機密性の高い情報を毎日扱う際、企業が最も優先する絶対的な価値はただ一つ、プライバシー（個人情報および機密保護）と徹底したデータセキュリティです。一度の流出がそのまま会社の倒産につながる可能性もあるからです。

このような企業の巨大な不安を払拭するため、これまで大多数の企業顧客は、AIサービスプロバイダーと厳格な「ゼロリテンション（データをサーバーに1秒たりとも保存せず、処理直後に即時削除するポリシー）」契約を結んできました。この契約のおかげで、企業はようやく安心してAIを実務で積極的に活用することができました。つまり、ユーザーがAIにどのような機密事項を尋ね、どのような素晴らしい回答を得ようとも、そのセッションウィンドウを閉じた瞬間に、関連する記録がサーバーから永久に破棄されるという、強固で確実な約束が存在していたのです。企業の立場からすれば、これがAIを内部ネットワークに導入するための唯一の防衛線でした。

しかしAnthropicは、今回の新型Claudeモデルを世に公開するにあたり、とてつもない爆弾宣言を投げかけました。すべてのユーザーのプロンプト（AIに与える命令や質問）と、AIが生成した結果のトラフィックを義務的に「30日間」自社のサーバーに保存するという新しいポリシーを一方的に通達したのです [[Fable 5とMythos 5がAIセキュリティとデータ保持をどう変えるか...](https://www.forrester.com/blogs/how-fable-5-and-mythos-5-change-ai-security-data-retention-and-vendor-risk/)]。

特に業界に最大の衝撃を与えた事実は、この新しい30日間の義務的な保持条項が、数多くの企業顧客が数百万ドルを費やして以前に結んでいた鉄壁のゼロリテンション契約さえも強制的に無効化（override）し、最優先で適用されるという点です [[AnthropicのClaude Fableは一般人がアクセスできるMythosのバージョンである...](https://techcrunch.com/2026/06/09/anthropics-claude-fable-5-is-a-version-of-mythos-the-public-can-access-today/)]。もはや過去の約束は守られなくなったというわけです。

さらに深刻なのは、この恐ろしいポリシーの適用範囲です。単にAnthropicの公式ウェブサイト（ファーストパーティのインターフェース）でモデルを使用する場合に限った話ではありません。Amazon Web Services（AWS）のクラウドプラットフォームであるBedrockや、GitHub Copilotのようなサードパーティ（第三者）のパートナープラットフォームを経由して間接的にこのAIを稼働させる場合でさえ、この30日間の保存義務はただ一つの例外もなく無条件に適用されます [[AWS上のAnthropic Claude Fable 5：組み込みのセーフガードを備えたMythosクラスの機能が利用可能に | Amazon Web Services](https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/)][[AnthropicはFable 5のリスクプロンプトをOpus 4.8にルーティングする](https://www.implicator.ai/anthropic-routes-high-risk-fable-5-queries-to-opus-4-8-in-public-rollout/)][[Claude Fable 5のデータ保持コンプライアンス | Lushbinary](https://lushbinary.com/blog/claude-fable-5-enterprise-data-retention-compliance-guide/)][[Claude Fable 5のリリース後、インターネットはAnthropicに激怒している - Decrypt](https://decrypt.co/370688/internet-furious-anthropic-claude-mythos-fable-5)]。

わかりやすく例えるなら、最高級ホテルの部屋（AWS）を数日間借りて、外部の干渉がない完璧な秘密会議をしようとしているのに、部屋の中のふかふかなベッドを作った家具会社（Anthropic）が「当社のベッドを使うなら、部屋の中に当社の防犯カメラを必ず設置し、30日分の録画データを私たちが持ち帰らなければならない」と言い張っているようなものです。これは事実上、世界中のすべての企業に対して「私たちの最高級のAI知能を借りて使いたければ、あなたたちの心臓部とも言える機密データを丸1ヶ月間、私たちに大人しく預けなさい」と堂々と宣言したのと同じです。

## わかりやすい解説 (The Explainer)

一体なぜAnthropicは、最も重要な顧客である企業の激しい反発と離脱をはっきりと予想しながらも、このような無理な要求を押し通すのでしょうか？彼らが盾として掲げた名目はただ一つ、致命的な危険から人類を保護するという「安全性（Safety）」です。

私たちが日常で使う道具の危険性に例えてみましょう。近所の公園で砂の城を作るための軽いプラスチックのシャベルを隣人に貸すときは、身元確認や書類などを要求しません。間違った使い方をしても、せいぜい砂が少し跳ねる程度だからです。しかし、巨大な岩山を丸ごと吹き飛ばせるような高性能の爆薬を貸し出すときは状況が全く異なります。徹底的に身元調査を行い、爆薬を正確にどこに使ったのか追跡装置を取り付け、事故を防ぐために監視カメラですべてのプロセスを綿密に監視しなければなりません。

同様に、AIモデルの能力が過去とは比較にならないほど強力になったことで、それを悪意のある目的で使用した場合に人類全体に及ぼす被害の規模も指数関数的に大きくなりました。

今回新たにリリースされたClaude Fable 5は、膨大な知識作業、複雑な視覚情報の処理、さらには自らマウスを動かしてコンピューターを操作する能力、そして高度なコーディング分野において、現存する最高レベル（State-of-the-art）の能力を備えています [[Claude Fable \ Anthropic](https://www.anthropic.com/claude/fable)]。そして、ここからさらに一歩進んだMythos 5モデルは、高度なサイバーセキュリティシステムの防衛網の構築、専門的な生物学研究、専門的な医療分野の最高峰に位置する究極のモデルです [[Claude Mythos \ Anthropic](https://www.anthropic.com/claude/mythos)]。

これほど途方もない専門的な知識と能力を持つAIが、もしハッカーやテロリストの手に渡り、国家の電力網を麻痺させるマルウェアを瞬く間に作成したり、ひそかに致命的な生物兵器の製造方法を親切に案内したりすれば、それは到底取り返しのつかない恐ろしい災難となるでしょう。

したがってAnthropicは、AIがユーザーと対話する過程で、このような危険な行動や自社の規定に違反していないかをリアルタイムで監視するために、「安全分類器（Safety Classifiers、リアルタイムで危険の兆候を判別する人工知能監視プログラム）」という一種の能動的な24時間監視システムを全面稼働させることを決定しました [[Fable 5に飛び込むすべての組織への注意：彼らはあなたの...を保持します](https://cybernews.com/ai-news/claude-fable-five-data-retention-collection/)][[Microsoftはデータ保持の懸念から従業員向けのClaude Fableを制限する | The Verge](https://www.theverge.com/report/947575/microsoft-claude-fable-5-restricted-internally)]。

しかし、この監視システムが対話の前後関係を完璧に把握し、実際の危険性を正確に評価するためには、ユーザーが一体どのような意図を持って質問を投げかけ、AIがどのような答えを提示したのかという前後の文脈を深く分析するための絶対的な「時間」と保存された「データ」が不可欠です。

結局、Anthropicは、この複雑な安全監視作業をエラーなく適切に実行するためには、最低でも30日間という保管期間が絶対に必要だと結論づけたのです。企業があれほど信じて望んでいたゼロリテンションという心強い「文書の即時シュレッダー」の電源コードを思い切って引き抜き、その場所に丸30日間も強制的に録画される強力な「防犯監視カメラ」を設置してしまったというわけです。

もちろんAnthropicも、腹を立てた企業顧客の激しい反発と深い懸念を和らげるために、一つの重要な約束を急いで付け加えました。強制的に保存されるビジネス顧客の機密トラフィックデータは、安全監視という本来の防御的な目的のためだけに極めて限定的に使用されるのみであり、このデータを無差別に掻き集めて新しい次世代のClaude AIモデルを訓練（学習）するためには決して使用しないと明記したのです [[AnthropicがClaude Fable 5を立ち上げ... — EdTech Innovation Hub](https://www.edtechinnovationhub.com/news/anthropic-opens-access-to-claude-fable-5-while-keeping-mythos-5-behind-trusted-controls)]。しかし、このような積極的な釈明と約束にもかかわらず、一度崩れた信頼と企業の深い不安感を完全に払拭するにはまだ力不足な状況です。

## 現在の状況 (Where We Stand)

この破格でやや一方的なポリシーが発表されるやいなや、IT市場と主要な企業顧客の反応は冷たく断固としたものでした。最も早く、そして敏感に動いたのは他でもない、IT業界の巨大な恐竜であり徹底したセキュリティの象徴であるMicrosoftでした。

Microsoftは、Anthropicのこの新しいデータ保持ポリシーが自社の厳格なデータプライバシー基準と真っ向から衝突するという重い懸念を提起し、社内の数多くの従業員が内部の業務ネットワークからClaude Fable 5モデルにアクセスして使用することを直ちに制限するという強硬手段に出ました [[Microsoftはデータ保持の懸念からAnthropicのClaude Fable 5への従業員のアクセスを制限する](https://cryptobriefing.com/microsoft-restricts-claude-fable-5-data-retention/)][[Microsoftはデータ保持の懸念から従業員向けのClaude Fableを制限する | The Verge](https://www.theverge.com/report/947575/microsoft-claude-fable-5-restricted-internally)]。世界で最もセキュリティに徹底し、AIのトレンドに敏感な世界最高のテクノロジー企業でさえも、自社の骨格となる内部機密が丸30日間もコントロールできない外部サーバーに縛られるという、めまいがするようなリスクを絶対に負うことはできないと冷静に判断したのです。

ユーザーの夜も眠れなくさせるさらに不安な点は、データが縛られる期間が必ずしも30日という短い（？）時間で終わるとは限らないという点です。関連報道やAnthropicのポリシーの細かい内容によると、もし安全分類器システムが特定のユーザーのプロンプトやAIの生成物を、深刻な潜在的リスク要因（例：巧妙なハッキングの試み、危険な化学物質に関する議論など）として疑い赤信号を点灯させた場合、該当データは精密な分析と徹底的な調査のために最大2年間もサーバーに保管される可能性が開かれています [[Microsoftはデータ保持の懸念から従業員向けのClaude Fableを制限する | The Verge](https://www.theverge.com/report/947575/microsoft-claude-fable-5-restricted-internally)]。

一体どのような曖昧で秘密めいた基準によって、私の大切な業務データが丸2年という長い間、他社の金庫に閉じ込められることになるのか、ユーザーの立場からはその透明性を担保したり問い詰めたりする方法が見当たらず、ハラハラするしかありません。

これにより、現在世界中の数多くのグローバル大企業や革新的なスタートアップ企業は、痛ましい進退両難のジレンマに陥っています。現存する最も賢く、自社の従業員の作業効率を数十倍にも跳ね上げてくれる優れたAIアシスタント（Fable 5、Mythos 5）を雇用して、熾烈な市場競争を勝ち抜くか？それとも会社の生命線とも言える絶対的なデータ主権とセキュリティを確固として守るために、作業パフォーマンスが少し落ちたとしても、既存の安全な「ゼロリテンション」を保証する旧型のAIや、他の競合他社の少し賢くない代替モデルにこだわり続けるか？今この瞬間も、数多くの企業のセキュリティ責任者や経営陣の会議室では、連日激しいマラソン討論が繰り広げられています。

何よりも、インターネットコミュニティの多くの開発者たちが最も深い懸念を示している理由は、このポリシーが持つ恐ろしい拡張性のためです。Anthropicが断固として発表した文面によると、この強制的な保持ポリシーは、単に今月リリースされたFable 5やMythos 5モデルにのみ適用されて終わる一過性の措置では決してありません。今後リリースされる同レベルの能力を持った、あるいはそれ以上の超巨大知能を備えたすべての未来の「Mythosクラス（Mythos-class）」巨大モデルに対して、永久に、そして例外なく適用される予定です [[Anthropicは、これまでで最も強力で一般利用可能なモデルであるClaude Fable 5でMythosを大衆にもたらす | VentureBeat](https://venturebeat.com/technology/anthropic-brings-mythos-to-the-masses-with-claude-fable-5-its-most-powerful-generally-available-model-ever/)][[Claude Fable 5のデータ保持コンプライアンス | Lushbinary](https://lushbinary.com/blog/claude-fable-5-enterprise-data-retention-compliance-guide/)][[Claude Fable 5のリリース後、インターネットはAnthropicに激怒している - Decrypt](https://decrypt.co/370688/internet-furious-anthropic-claude-mythos-fable-5)]。

最新のIT動向をいち早く議論するHacker Newsのような開発者コミュニティでも、このニュースは直ちに熱い話題として浮上し、激しい賛否両論の論争を生んでいます [[AnthropicはFableの30日間のデータ保持を義務付けている... | HackerNews](https://news.ycombinator.com/item?id=48464258)]。つまり、人類がより優れて幻想的な人工知能の恩恵を享受するために、これからは必ず支払わなければならない避けられない「新しい形の通行税」であり、人工知能業界全体の固定化された新しいルール（Standard）として定着する危険性が色濃く潜んでいるのです。

## 今後どうなるのか？ (What's Next)

私たちは今、驚異的な人工知能技術の歴史の中で、人間のプライバシーの行方を永遠に左右する、非常に重大でギリギリの変曲点を通過しています。

AIが人間よりも賢くなり、人間でさえ容易にはできない非常に複雑で精巧な領域にまで深く浸透するほど、それがもたらす可能性のある破滅的なリスクを未然に防ぐための統制と監視の強度も、それに比例して綿密に高まらなければならないというAnthropicの「安全性最優先」の主張には、確かに哲学的に妥当な一面があります。目覚ましい技術発展の恐ろしいほどの加速度が、ある瞬間、人間の微弱な制御力を完全に超えてしまわないように、強固で巨大な「安全網」を先制的に構築することは、もしかすると人類全体の生存と未来のために、誰かが非難の的になってでも必ずやり遂げなければならない、苦痛を伴うが必須の作業なのかもしれません。

しかし、その重くて巨大な安全網を強制的に構築し維持する過程で、個人や企業が非常に長い間苦労して戦い守ってきた「プライバシー」と「データ主権」という、決して譲ることのできない根本的な基本権が深刻に揺さぶられ、鋭く衝突しています。Microsoftの素早い内部アクセスの全面制限措置は、巨大な葛藤の氷山の一角に過ぎないかもしれません。

今後、たった一度のデータ流出事故に会社の存亡全体がかかっている厳しい金融業界、極めて機密性が高く私的な患者の生命情報を扱う保守的な医療業界、厳格な秘密保持が存在理由である法律分野の数多くの企業は、最新のClaudeモデルの業務導入と使用を原点から全面的に見直す可能性が非常に高いでしょう。

## AIの視点 (AI's Take)

より賢いAIがもたらす利点を享受するために、私たちはどこまでプライバシーを譲歩すべきでしょうか？強力な技術統制とデータ主権の間の激しい綱引きが、今まさに本格的に始まりました。

人工知能の知能が爆発的に成長するにつれて、人間は今やAIを単なる便利な単純な道具ではなく、潜在的なリスク要因として認識し始めました。Anthropicの今回の頑固な決定は、AIの能力がいつか人間の統制力を完全に超えてしまうかもしれないという根本的な恐れから出発しています。

しかし、企業や個人の立場からすれば、自分が心血を注いで作った最も機密性の高い情報が、コントロールできない誰かのサーバーに30日間、さらには曖昧な基準に従って最大2年間も留まらなければならないという事実は、非常に不安で不快なものにならざるを得ません。

革新的な最高性能のAI技術を思いのまま自由に活用しつつも、自分の大切な情報は外部の視線から完璧に保護されたいと願う人間の根本的な欲求。そして、人類全体の安全のためにすべての危険の可能性をくまなく覗き込み監視しなければならないというAIの安全網。この二つの間の張り詰めた息の詰まるような緊張感は、今後さらに強まるでしょう。結局、この巨大な矛盾を技術的に最も優雅に解決する企業が、おそらく未来のAI市場を真に支配することになるはずです。

当分の間、私たちは、Anthropicのこのブレない強硬なプライバシー制限ポリシーが、果たして効率性を重視する市場の冷酷な論理に打ち勝ち、業界全体の新しい標準としてしっかりと定着できるのかを、非常に興味深く見守らなければなりません。また、その葛藤の隙間を鋭く突き入る数多くの競合AI企業が、不安に震える企業顧客を誘惑するためにどのような創造的なアメと魅力的な代替ポリシーを持ち出してくるかも、非常に重要な見どころです。技術の真の革新は、いつもこのように予想外の激しい葛藤と痛みを伴う陣痛の中で、その明快な答えを見つけ出していくものだからです。

---

## 参考資料

1. [How Fable 5 And Mythos 5 Change AI Security, Data Retention ...](https://www.forrester.com/blogs/how-fable-5-and-mythos-5-change-ai-security-data-retention-and-vendor-risk/)
2. [Does Anthropic’s New 30-Day Data Retention for Claude Fable 5 ...](https://www.linkedin.com/pulse/does-anthropics-new-30-day-data-retention-claude-fable-jonathan-milne-qhrfe)
3. [The Internet Is Furious at Anthropic After Claude Fable 5 Release - Decrypt](https://decrypt.co/370688/internet-furious-anthropic-claude-mythos-fable-5)
4. [Anthropic’s Claude Fable is a version of Mythos the public ...](https://techcrunch.com/2026/06/09/anthropics-claude-fable-5-is-a-version-of-mythos-the-public-can-access-today/)
5. [Anthropic Claude Fable 5 on AWS: Mythos-class capabilities with built-in safeguards now available | Amazon Web Services](https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/)
6. [AnthropicRoutesFable5 Risk Prompts to Opus 4.8](https://www.implicator.ai/anthropic-routes-high-risk-fable-5-queries-to-opus-4-8-in-public-rollout/)
7. [Claude Fable 5 Data Retention Compliance | Lushbinary](https://lushbinary.com/blog/claude-fable-5-enterprise-data-retention-compliance-guide/)
8. [Claude Fable \ Anthropic](https://www.anthropic.com/claude/fable)
9. [ClaudeMythos\Anthropic](https://www.anthropic.com/claude/mythos)
10. [Attention all orgs diving into Fable 5: they’ll keep your ...](https://cybernews.com/ai-news/claude-fable-five-data-retention-collection/)
11. [Microsoft restricts Claude Fable for employees over data retention concerns | The Verge](https://www.theverge.com/report/947575/microsoft-claude-fable-5-restricted-internally)
12. [Anthropiclaunches ClaudeFable5 with... — EdTech Innovation Hub](https://www.edtechinnovationhub.com/news/anthropic-opens-access-to-claude-fable-5-while-keeping-mythos-5-behind-trusted-controls)
13. [Microsoft limits employee access to Anthropic's Claude Fable 5 over data retention concerns](https://cryptobriefing.com/microsoft-restricts-claude-fable-5-data-retention/)
14. [Anthropic brings Mythos to the masses with Claude Fable 5, its most powerful generally available model ever | VentureBeat](https://venturebeat.com/technology/anthropic-brings-mythos-to-the-masses-with-claude-fable-5-its-most-powerful-generally-available-model-ever)
15. [Anthropicrequires30daydataretentionforFable... | HackerNews](https://news.ycombinator.com/item?id=48464258)