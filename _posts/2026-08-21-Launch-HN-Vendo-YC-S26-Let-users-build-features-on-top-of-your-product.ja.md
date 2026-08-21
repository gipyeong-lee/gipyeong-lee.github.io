---
layout: post
title: "業務にぴったりの機能、AIが勝手に作ってくれたら？"
description: "B2B SaaSサービスの深刻な問題である機能リクエストのバックログを解決し、ユーザーが自分で機能を作れるようにする「Vendo」について解説します。"
summary: "Vendoは、企業用ソフトウェアのユーザーが開発者の手を借りずに、欲しい機能やアプリを製品上に直接作って追加できるようにする、オープンソースのユーザー定義レイヤーです。"
tags: [AI, SaaS, B2B, Vendo, 生産性]
image: 2026-08-21-Launch-HN-Vendo-YC-S26-Let-users-build-features-on-top-of-your-product.jpg
image_alt: "ユーザーが既存のソフトウェア画面上で、自分に必要な機能を直接構成する様子を抽象的に表現したイメージ"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "ソフトウェアの主導権が開発会社からユーザーへと移る重要な転換点です。Vendoは製品の硬直性を打ち破り、個々のユーザーの働き方を尊重する柔軟なエコシステムを築くでしょう。"
quiz:
  - question: "Vendoの核心的な機能は何ですか？"
    choices: ["ソフトウェアのソースコードを直接修正させる", "ユーザーが欲しい機能やアプリを製品内に直接生成できるようにする", "開発者の作業速度を2倍に高める"]
    answer: 1
    explanation: "Vendoは、ユーザーが開発者の手を借りることなく、自分のニーズに合わせた機能やマイクロアプリを製品上に直接構築できるよう支援します。"
  - question: "Vendoを使うと、既存製品のソースコードは修正されますか？"
    choices: ["はい、必ず修正する必要があります", "いいえ、ソースコードには触れず、サンドボックス形式で実装されます", "一部の核心機能のみ修正されます"]
    answer: 1
    explanation: "Vendoは既存製品のソースコードを修正することなく、サンドボックス（保護された環境）内でブランドと自然に調和するUIを生成します。"
  - question: "Vendoを通じて生成された機能はどのように動作しますか？"
    choices: ["独立した別サーバーで動作する", "製品のAPIを通じて、ユーザーの権限で動作する", "すべての機能がクラウド上で強制的にアップデートされる"]
    answer: 1
    explanation: "生成された機能は、該当製品のAPIを通じて現在ログイン中のユーザー権限で直接動作し、ユーザーのワークフローに合わせてパーソナライズされます。"
lang: ja
ref: 2026-08-21-Launch-HN-Vendo-YC-S26-Let-users-build-features-on-top-of-your-product
---

想像してみてください。毎日業務で使うソフトウェアの画面を見ながら、「ああ、ここでこのボタンを押してファイルをメールで送れたらいいのに」と考えたことはありませんか？しかし、それを開発チームにリクエストしても、返ってくるのはいつも「検討しておきます」や、「機能バックログ（リクエストリスト）が多すぎて、今年は難しいですね」という言葉ばかり。

結局、私たちはソフトウェアが提供する機能に、自分の仕事のやり方を無理やり合わせるしかありませんでした。足に合わない靴を履いて一日中歩き回るようなものです。しかし、もしユーザーが自分の手にぴったりの機能をその場で作り、追加できるとしたらどうでしょう？最近、シリコンバレーのYコンビネーター（YC）の支援を受けて登場した**Vendo**は、まさにこの問題を解決しようとしています。

## なぜこれが重要なのか？ (Why It Matters)

企業用ソフトウェア（B2B SaaS）を使う多くの人々は、常に「自分に必要な機能」と「製品が提供する機能」の間にギャップを感じています。すべての企業の業務プロセスはそれぞれ異なりますが、ソフトウェアは「平均的な」機能しか提供していないからです。

Vendoは、このようなソフトウェアの「硬直性」を取り払います。この技術を導入した企業のユーザーは、開発者の助けがなくても、自身の業務に必要なカスタマイズ機能や小さなアプリ（マイクロアプリ）を直接生成できます。[出典: Vendo(YC S26) – Let your users build features on top of your product](https://www.ycombinator.com/companies/vendo)。結果として企業は、積み上がる一方の機能開発リクエスト（feature backlog）から解放され、ユーザーは自分だけのワークフローを完成させることができるようになります。---
layout: post
title: "業務にぴったりの機能を、AIが勝手に作ってくれたら？"
description: "B2B SaaSサービスの深刻な問題である機能要望バックログを解決し、ユーザー自身が直接機能を作成できるようにする「Vendo」について解説します。"
summary: "Vendoは、業務ソフトウェアのユーザーが開発者の手を借りず、欲しい機能やアプリを製品上に直接構築して追加できるようにするオープンソースのユーザー定義レイヤーです。"
tags: [AI, SaaS, B2B, Vendo, 生産性]
image: 2026-08-21-Launch-HN-Vendo-YC-S26-Let-users-build-features-on-top-of-your-product.jpg
image_alt: "ユーザーが既存のソフトウェア画面上で必要な機能を直接構成する様子を抽象的に表現したイメージ"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "ソフトウェアの主導権が開発企業からユーザーへと移る重要な転換点です。Vendoは製品の硬直性を打破し、個々のユーザーの働き方を尊重する柔軟なエコシステムを築くでしょう。"
quiz:
  - question: "Vendoの核心的な機能は何ですか？"
    choices: ["ソフトウェアのソースコードを直接修正させる", "ユーザーが欲しい機能やアプリを製品内に直接生成できるようにする", "開発者の作業速度を2倍に高める"]
    answer: 1
    explanation: "Vendoは、ユーザーが開発者の助けを借りずとも、自分のニーズに合わせた機能やマイクロアプリを製品上に直接構築できるよう支援します。"
  - question: "Vendoを使うと既存製品のソースコードは修正されますか？"
    choices: ["はい、必ず修正しなければなりません", "いいえ、ソースコードには触れずサンドボックス形式で実装されます", "一部の中核機能のみ修正されます"]
    answer: 1
    explanation: "Vendoは既存製品のソースコードを修正することなく、サンドボックス（保護された環境）内でブランドと自然に調和するUIを生成します。"
  - question: "Vendoを通じて生成された機能はどのように動作しますか？"
    choices: ["独立した別サーバーで動作する", "製品のAPIを通じて現在のユーザー権限で動作する", "すべての機能がクラウド上で強制的にアップデートされる"]
    answer: 1
    explanation: "生成された機能は、その製品のAPIを通じて現在ログインしているユーザーの権限で直接動作し、ユーザーのワークフローに合わせてパーソナライズされます。"
lang: ja
ref: 2026-08-21-Launch-HN-Vendo-YC-S26-Let-users-build-features-on-top-of-your-product
---

想像してみてください。毎日業務で使っているソフトウェアの画面を見ながら、「ああ、ここでこのボタンを直接押してファイルをメールで送れたらいいのに」と思ったことはありませんか？しかし、その機能を開発チームに要望しても、返ってくるのはいつも「検討しておきます」や「機能バックログ（要望リスト）が山積みで、今年は難しいですね」という言葉ばかり。

結局、私たちはソフトウェアが提供する機能に、自分の働き方を無理やり合わせるしかありませんでした。足に合わない靴を履いて一日中歩き回るようなものです。しかし、もしユーザーが自分の手にぴったりの機能を、その場で自分で作って追加できるとしたらどうでしょうか？最近、シリコンバレーのYコンビネーター（YC）の支援を受けて登場した**Vendo**が、まさにこの問題を解決しようとしています。

## なぜこれが重要なのか？ (Why It Matters)

B2B SaaSを利用する多くの人々は、常に「自分が必要とする機能」と「製品が提供する機能」との間に乖離を感じています。企業の業務プロセスは千差万別ですが、ソフトウェアは「平均的な」機能しか提供しないためです。

Vendoはこのソフトウェアの「硬直性」を打ち破ります。この技術を導入した企業のユーザーは、開発者の助けを借りずとも、自分の業務に必要なカスタム機能や小さなアプリ（マイクロアプリ）を直接生成できます。[出典: Vendo(YC S26) – Let your users build features on top of your product](https://www.ycombinator.com/companies/vendo)。結果として企業は際限なく積み上がる機能開発要望（機能バックログ）から解放され、ユーザーは自分だけのワークフローを完成させることができるようになります。[出典: YC-Backed Vendo Lets Users Build Features on Top of SaaS ...](https://www.founderland.ai/articles/yc-backed-vendo-lets-users-build-features-on-top-of-saas-pro-mrynzgii)。

## 簡単に理解する（The Explainer）

このように例えてみましょう。従来のソフトウェアが「よく作られた完成家具」だとすれば、Vendoはその家具の上に自由に追加できる「レゴブロックセット」のようなものです。

簡単に言えば、Vendoはソフトウェアの中に組み込まれる「埋め込み型エージェント（製品内部に挿入され、ユーザーに代わって作業する人工知能）」です。[出典: GitHub - runvendo/vendo: Embedded agents your customers use ...](https://github.com/runvendo/vendo)。

1. **接続**: Vendoは当該製品が提供するAPI（ソフトウェアが外部とやり取りする通路）を通じて、実際のユーザーが作業するかのように安全に命令を下します。[出典: Vendo: open-source layer that lets users build features on ...](https://zeli.app/en/story/49376038)。
2. **構築**: ユーザーが機能を要望すると、Vendoシステム内部のカスタマイズ装置がReact（ユーザーインターフェースを作成するためのJavaScriptライブラリ）コンポーネントを作成します。このとき、ミスを防ぐガイドライン（ガードレール）が適用され、安全に呼び出しを実行します。[出典: LaunchHN:Vendo(YC S26) –Letusersbuildfeaturesontopof...](https://news.ycombinator.com/item?id=49376038)。
3. **レンダリング**: こうして作られた機能は、元のソフトウェアのコード自体には触れず、サンドボックス（外部と遮断された安全な独立空間）内で、あたかも最初からあった機能のように自然に画面に描画されます。[出典: GitHub - runvendo/vendo: Embedded agents your customers use ...](https://github.com/runvendo/vendo)。

## 現在の状況 (Where We Stand)

現在、Vendoはオープンソースとして提供されています。[出典: Vendo: open-source layer that lets users build features on ...](https://zeli.app/en/story/49376038)。企業担当者であれば、わずか60秒で `npm install` コマンドを使って自分のソフトウェアにインストールできるほど簡単です。[出典: Vendo: open-source layer that lets users build features on ...](https://zeli.app/en/story/49376038)。

Vendoの共同創業者であるYousef氏は、AIエージェントがダッシュボードやユーザーインターフェースを消費する方法を根本的に変えており、その中心には「パーソナライゼーション（個人化）」があると強調しました。[出典: Show HN: Vendo (YC S26) – Let your users add their own ...](https://news.ycombinator.com/item?id=48926618)。現在、多くのB2B SaaS企業がこのソリューションを通じて、顧客から要望される個別の機能要望を処理する「バックログ地獄」から脱出しようと努力しています。[出典: YC-Backed Vendo Lets Users Build Features on Top of SaaS ...](https://www.founderland.ai/articles/yc-backed-vendo-lets-users-build-features-on-top-of-saas-pro-mrynzgii)。

## 今後はどうなるのか？ (What's Next)

今後は、私たちが使用するほぼすべての業務ツールが「完成品」ではなく「材料」の形で提供される可能性が高いでしょう。Vendoのようなツールが普及すれば、ソフトウェアを開発する企業は中核エンジンのみを提供し、ユーザーがその上に自分だけのワークフローを上書きする形態が標準になるはずです。

開発者は個々の顧客の些細な要望をケアする代わりに、より大きなシステムの安定性や中核機能の開発に集中できるようになるでしょう。私たちが使うアプリが、まるでレゴブロックのように互いに噛み合い、自分の業務スタイルを記憶する未来が近づいています。

## MindTickleBytesのAI記者視点

ソフトウェアを作る人ではなく、そのソフトウェアを最もよく知るユーザーが機能を定義する時代が開かれました。Vendoは技術の複雑さの裏に隠されていた「ツールの主権」をユーザーに取り戻させる新鮮な試みです。ソフトウェアが自分の働き方を問うのではなく、自分がソフトウェアを自分の働き方に合わせて進化させるプロセスが当たり前になるでしょう。

## 参考資料

1. [Vendo: Let your users build their own features on top of your ...](https://www.ycombinator.com/companies/vendo)
2. [Vendo — YC S26 Launch on Hacker News - bestofshowhn.com](https://bestofshowhn.com/yc-s26/vendo)
3. [Show HN: Vendo (YC S26) – Let your users add their own ...](https://news.ycombinator.com/item?id=48926618)
4. [GitHub - runvendo/vendo: Embedded agents your customers use ...](https://github.com/runvendo/vendo)
5. [Vendo: open-source layer that lets users build features on ...](https://zeli.app/en/story/49376038)
6. [Introducing Vendo: let your users edit your product - LinkedIn](https://www.linkedin.com/pulse/introducing-vendo-let-your-users-edit-product-ankit-gupta-0uu9c)
7. [Vendo lets users build custom features on top of your product ...](https://www.linkedin.com/posts/y-combinator_vendo-yc-s26-lets-your-users-build-their-activity-7485385624418439168-KuP2)
8. [LaunchHN:Vendo(YC S26) –Letusersbuildfeaturesontopof...](https://news.ycombinator.com/item?id=49376038)
9. [Vendo (YC S26) – Let your users add their lown features to ...](https://aiindigo.com/blog/vendo-yc-s26-let-your-users-add-their-lown-features-to-your-product-deep-dive-te)
10. [YC-Backed Vendo Lets Users Build Features on Top of SaaS ...](https://www.founderland.ai/articles/yc-backed-vendo-lets-users-build-features-on-top-of-saas-pro-mrynzgii)