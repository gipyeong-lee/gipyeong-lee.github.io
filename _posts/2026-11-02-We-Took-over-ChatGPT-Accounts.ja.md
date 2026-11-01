---
layout: post
title: "私のChatGPTアカウントがハッキングされた？研究者が実演したセキュリティの隙"
description: "最近、セキュリティ研究者がOpenAI従業員のChatGPTアカウントを実際にハッキングすることに成功しました。私たちのアカウントは安全なのか、なぜこのようなことが起きたのかを分かりやすく解説します。"
summary: "セキュリティ研究者が2つの脆弱性を連鎖させ、OpenAI従業員のChatGPTアカウントを乗っ取って内部システムにアクセスする過程を公開し、AIセキュリティの重要性を浮き彫りにしました。"
tags: [ChatGPT, AIセキュリティ, アカウント乗っ取り, サイバーセキュリティ]
image: 2026-11-02-We-Took-over-ChatGPT-Accounts.jpg
image_alt: "画面の中で南京錠が開錠されているデジタルイメージ"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AIモデルが賢くなるにつれて、それを取り扱うシステムのセキュリティのハードルも高くしなければなりません。今回の事例は、AI技術そのものの進化よりも、その技術を守る「見えない盾」がいかに重要であるかを示しています。"
quiz:
  - question: "研究者がOpenAI従業員のアカウントを乗っ取るために使用した方法は何ですか？"
    choices: ["パスワードの推測", "2つの脆弱性を連結", "フィッシングメールの送信"]
    answer: 1
    explanation: "研究者は2つの脆弱性を連鎖的に活用し、アカウントの権限を取得する方法を使用しました。"
  - question: "アカウントを乗っ取った研究者は、それを通じて何を確認しましたか？"
    choices: ["ユーザーの会話記録の閲覧", "OpenAI内部リポジトリへのアクセス", "有料決済情報の窃取"]
    answer: 1
    explanation: "研究者は乗っ取ったアカウント権限を利用して内部リポジトリにアクセスし、プルリクエストを作成するプロセスを実演しました。"
  - question: "OpenAIが以前にアカウントを停止したことがあるアカウントの特徴は何ですか？"
    choices: ["有料サブスクリプション未納アカウント", "国家支援ハッキンググループと繋がりのあるアカウント", "多重アカウント作成者"]
    answer: 1
    explanation: "OpenAIは、悪意のあるソフトウェアの開発やフェイクニュースの流布など、不正な目的で使用された国家支援ハッキンググループのアカウントを停止したことがあります。"
lang: ja
ref: 2026-11-02-We-Took-over-ChatGPT-Accounts
---

想像してみてください。ある日の朝、いつものようにChatGPTに「今日の予定を整理して」と入力したところ、AIがとんちんかんな答えを返したり、自分の個人情報が混ざった見知らぬ文章を出力したりしたらどうでしょうか？単に「AIがまたミスをしている」と片付ける問題ではないかもしれません。最近、セキュリティ業界で実際に起きた出来事は、私たちの日常生活に欠かせないものとなったAIサービスのセキュリティが、考えていたよりも身近な場所で脅かされていることを示唆しています。

### なぜこれが重要なのか？

ChatGPTは、全世界で7億人のユーザーを抱える代表的なAIモデルです。[ビジネスインサイダー（Business Insider）](https://www.businessinsider.com/chatgpt) 今や多くの人が業務資料を要約し、メールを作成し、さらには個人的な悩みまでAIと共有しています。もしこのサービスの自身のアカウントがハッキングされたら、単なる個人的な会話内容の流出にとどまりません。攻撃者がAIを介して、自分のアカウント権限で外部サービスと直接通信したり、企業の内部システムに侵入するための危険な通路として悪用される可能性があるからです。

今回露呈したセキュリティ問題は、単に「パスワードを変えようか？」という次元を超えています。AIという巨大な技術を支える基盤システムそのものが、攻撃者にとって新たな「狩り場」になっているという警告音だからです。

### 分かりやすく解説：セキュリティの「小さな隙間」

セキュリティ専門家たちは、今回の事件を「2つの脆弱性（セキュリティ上の弱点）を連結させた」と表現しています。[ザ・レジスター（The Register）](https://www.theregister.com/security/2026/09/18/researchers-used-claude-to-hack-openai-employees-chatgpt-accounts/5297517)

簡単に例えるならこうです。どれほど頑丈な鉄扉の玄関を施錠していても（第一のセキュリティ）、すぐ横に小さな窓が開いていれば（第二の脆弱性）、誰かがその隙間をこじ開けて侵入できるのと同じ理屈です。研究者たちはこのようにシステム各所に隠された小さな隙間を一つずつ探し出し、まるでパズルのピースを合わせるように連結させ、最終的に「管理者権限」という大きな扉を開いたのです。

「パラメータAIラボ（Parameter AI Labs）」のレポートによると、こうして乗っ取られたアカウントは、実際のユーザーになりすましてChatGPTの認証済みAPI（アプリケーション・プログラミング・インターフェース、ソフトウェア同士の対話窓口）を自由自在に呼び出すことができました。[パラメータAIラボ（Parameter.ai）](https://www.parameter.ai/labs/we-found-a-gap-at-openai) つまり、攻撃者が自分になりすましてAIを思いのままに操るということなのです。研究者たちは実際にこの権限を利用してOpenAIの内部システムにアクセスし、ソフトウェアの修正を要求する「プルリクエスト（Pull Request）」を作成する実演まで成功させました。[ザ・レジスター（The Register）](https://www.theregister.com/security/2026/09/18/researchers-used-claude-to-hack-openai-employees-chatgpt-accounts/5297517)

### 現状はどうなっているのか

もちろん、OpenAIもこのようなセキュリティリスクを非常に深刻に認識し、対応しています。過去には国家が支援するハッキンググループがChatGPTを利用して悪意のあるコードを巧妙に作成したり、採用詐欺、虚偽情報の流布などの不正行為を行ったりする事例が発見され、関連するアカウントを大量に停止させた実績があります。[ザ・レコード（The Record）](https://therecord.media/openai-takes-down-chatgpt-accounts-hacking)

しかし、今回のように研究目的の「ホワイトハッカー（善良なセキュリティ研究者）」たちが、企業のシステム内部まで深く踏み込んだ事例は、私たちにより大きな課題を突きつけています。今回の攻撃は特にOpenAIの内部従業員のアカウントを標的にしたものであり、セキュリティの小さな隙間がどれほど致命的な結果をもたらし得るかを如実に証明しました。[スフルンジ・ダキカ（Sıfırıncı Dakika）](https://sifirincidakika.com/haber/arastirmacilar-chatgpt-hesaplarini-ele-gecirdigini-acikladi)

### 今後はどうなるのか

今回の事件は、AI企業に対して「セキュリティは選択肢ではなく生存戦略」であることを改めて刻み込ませました。今後は企業にとって、AIモデルの知能を高めることと同じくらい、そのモデルを使うユーザーのアカウントやシステムの裏口をどれだけ堅牢に閉ざすかが勝負の分かれ目となるでしょう。

それでは、一般ユーザーは何ができるのでしょうか？身に覚えのないログイン通知が来たら絶対に無視せず、すぐに確認してください。また、可能な場合は「二要素認証（2FA、ログイン時にパスワード以外に追加の確認プロセスを経るセキュリティ方式）」を必ず設定してください。これだけでも、攻撃者が狙う「最初の扉」を非常に効果的に防ぐことができます。

AIは今や、私たちの生活から切り離せない一部となりました。技術が便利になるスピードと同じくらい、私たちを守る技術のスピードも速くならなければならない時です。

## 参考資料

1. [Do the Math: HowWeTookOverChatGPTAccounts- Parameter](https://www.parameter.ai/labs/we-found-a-gap-at-openai)
2. [AraştırmacılarChatGPThesaplarını ele geçirdiğini... | Sıfırıncı Dakika](https://sifirincidakika.com/haber/arastirmacilar-chatgpt-hesaplarini-ele-gecirdigini-acikladi)
3. [OpenAI takes down ChatGPT accounts linked to state-backed hacking](https://therecord.media/openai-takes-down-chatgpt-accounts-hacking)
4. [Researchers used Claude to hack OpenAI employees' ChatGPT accounts](https://www.theregister.com/security/2026/09/18/researchers-used-claude-to-hack-openai-employees-chatgpt-accounts/5297517)
5. [ChatGPT: Everything You Need to Know About... - Business Insider](https://www.businessinsider.com/chatgpt)