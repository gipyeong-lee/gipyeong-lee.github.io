---
layout: post
title: "危険すぎて隠したというAIハッカー「Mythos」、蓋を開けてみればマーケティングショー？"
description: "AnthropicのAIセキュリティモデル「Mythos」が危険すぎて非公開になったという主張に対し、cURLの創設者が自らテストを行い、「マーケティング」だと批判した事件を分かりやすく解説します。"
summary: "セキュリティ脆弱性の発見に優れすぎているため危険だとして非公開になっていたAnthropicのAI「Mythos」ですが、実際のオープンソースプロジェクトのテストでは些細なバグを1つ発見したのみで、誇大広告であるという批判を受けました。"
tags: [人工知能, サイバーセキュリティ, Anthropic, Mythos, ファクトチェック]
image: 2026-06-09-Anthropics-bug-hunting-Mythos-greatest-marketing-stunt-ever-says-cURL-creator.jpg
image_alt: "華やかな包装紙の中に入っているとても小さな虫眼鏡の絵で、AIの誇大広告を象徴するイラスト"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "新しい技術が登場するたびに、すぐに世界を変えるという幻想が生まれますが、真の革新は冷静な現実の点検と人間の創造性が出会う場所から始まります。"
quiz:
  - question: "cURLの創設者ダニエル・ステンバーグは、AnthropicのMythos AIを何と評価しましたか？"
    choices: ["人類史上最も偉大なハッキングツール", "歴代最高のマーケティングショー（誇大広告）", "開発者を完全に代替できるAI"]
    answer: 1
    explanation: "ダニエル・ステンバーグは、Mythosが発見したセキュリティの脆弱性はたった1つに過ぎないとし、これを「歴代最高のマーケティングショー（Greatest marketing stunt ever）」と評価しました。"
  - question: "Mythosが17万6000行のコードを分析した後、最終的に発見した実際のセキュリティ脆弱性（低い深刻度）はいくつですか？"
    choices: ["1つ", "5つ", "200以上"]
    answer: 0
    explanation: "Mythosは最初5つの問題を指摘しましたが、すでに知られている問題などを除き、実際のセキュリティ脆弱性として認められたのはたった1つだけでした。"
  - question: "記事によると、Mythosのような現在のAIセキュリティツールが持つ限界は何ですか？"
    choices: ["既存の単純なバグすら全く発見できない", "人間の創造性なしに、世界に存在しなかった新しいタイプの脆弱性を自ら発見することはできない", "自らコードを記述してプログラムを破壊する"]
    answer: 1
    explanation: "Mythosはすでに知られているタイプのエラーを見つけるのには役立ちますが、人間の創造性なしには完全に新しい形のセキュリティ脆弱性を発見できないという限界があります。"
lang: ja
ref: 2026-06-09-Anthropics-bug-hunting-Mythos-greatest-marketing-stunt-ever-says-cURL-creator
---

想像してみてください。世界最高の鍵専門会社が「我々が新しく作ったマスターキーは、世界のすべての金庫を一気に開けてしまうほど非常に強力で危険なため、大衆には絶対に公開できません」と重大発表をします。人々は恐れと好奇心が入り交じった目で、そのマスターキーの正体を気にするでしょう。このマスターキーの名前は、最新の人工知能（AI）です。

実際に最近、AI業界で似たようなことがありました。有名なAI企業Anthropicは、自社の新しいAIモデル「Mythos（ミトス）」がソフトウェアのセキュリティ脆弱性を見つけ出すことに優れすぎているため、大衆に公開するには危険だと示唆し、大きな話題を集めました [[セキュリティ - AnthropicのバグハンティングMythosは歴代最高のマーケティングショーだった、cURL創設者が語る | The Helper](https://www.thehelper.net/threads/anthropic%E2%80%99s-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-creator.201066/)]。

しかし、この「マスターキー」を世界で最も頑丈で複雑な金庫の1つで直接試した結果、人々の予想とは全く異なる結論が出ました。世界中の数多くの電子機器やインターネットシステムの骨格を成すコアソフトウェア「cURL」の創設者ダニエル・ステンバーグ（Daniel Stenberg）が、自らこのAIの実力を検証して下した評価は断固たるものでした。彼はMythosの能力に向けられた世間の大騒ぎは「歴代最高のマーケティングショー（greatest marketing stunt ever）」に過ぎないと批判しました [[AnthropicのバグハンティングMythosは歴代最高のマーケティングショーだった、cURL創設者が語る | daily.dev](https://app.daily.dev/posts/anthropic-s-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-creator-lifvxyq4b)]。

果たして「危険すぎて隠した」というAIハッカーの蓋を開けてみると何が入っていたのでしょうか？今日、MindTickleBytesでは、この興味深い事件の顛末と、AI技術の誇大広告を見抜く方法についてお話しします。

---

## なぜこれが重要なのか？ (Why It Matters)

この事件が単なるハプニングを超えて私たちの日常に密接に関わっている理由は、テストの対象となったソフトウェアが「cURL（インターネット上でデータのやり取りに使用される、広く普及している無料のオープンソースプログラム）」だからです。簡単に言えば、皆さんがスマートフォンで天気アプリを更新する時、Netflixで映画のリストを読み込む時、さらには最新の自動車がサーバーと通信する時でも、見えないところでcURLが動作しています。つまり、cURLに誰でも簡単に突破できるセキュリティの穴ができれば、世界中のデジタル機器が同時にハッキングの危険にさらされることを意味します。

Anthropicはまさにこのようなコアシステムの穴を見事に探し出す恐ろしいAI、「Mythos」を開発したと暗示しました [[AnthropicのバグハンティングMythosは歴代最高のマーケティングショーだった、と...](https://www.threatshub.org/blog/anthropics-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-creator/)]。もしこれが事実なら、ハッカーたちが見事にこのAIを利用してインターネット全体を麻痺させる恐ろしい武器を手に入れたことと同じです。人々は「AIがもはや人間の統制を離れ、自らシステムを破壊する方法を探すのではないか？」と懸念しました。企業のセキュリティ担当者たちも緊張せざるを得ないニュースでした。

しかし、現実はSF映画とは違いました。オープンソースプロジェクトを管理する開発者たちに迫り来る本当の脅威は「AIの反乱」ではありませんでした。むしろAIが「安全だ」と無作為に浴びせるレベルの低い警告状の数々でした。cURLの創設者であるステンバーグは、最近AIが発展するにつれ、オープンソースプロジェクトの管理者たちに膨大な量のセキュリティ脆弱性レポートが洪水のように押し寄せており、これは管理者たちが読んで処理できる速度をはるかに超えていると訴えました [[Mythosを「PRスタント」と呼んだcURL創設者が、AIは...と語る | Cybernews](https://cybernews.com/security/curl-bug-bounty-ai-security-reports-daniel-stenberg/)]。

つまり、賢すぎるAIが問題を起こしているのではなく、未熟なAIが自分が見つけた些細な埃を「爆弾」だと誇張し、絶え間なく通報ボタンを押しているようなものです。この事件は、真の技術の発展と企業のマーケティングを区別することが、現代社会で最も重要な生存のための知能の1つであることを示しています。

---

## 分かりやすく解説 (The Explainer)

「コードの脆弱性を見つける」とは一体どのような過程なのでしょうか？コードやセキュリティという言葉に少し馴染みがない方は、このように例えてみましょう。

例えば、17万6000ページに達するとてつもなく分厚い本（ソフトウェアのコード）が1冊あります。この本は世界で最も重要な規則を盛り込んでいるため、単語1つ間違えただけでも大事故に繋がる可能性があります。人間の検査者（開発者）たちは、何日も徹夜してこの本を読み、誤字や文脈が合わない箇所を探します。

この時登場したAIセキュリティツールは、非常に高速で緻密な「自動スペルチェッカー」のようなものです。AIは人間のように目が疲れることもなく、1秒で数万ページをスキャンし、空白が間違っている箇所や句点が抜けている箇所を的確に指摘します。このような面でAIは間違いなく人間を助ける非常に有用なツールです。今回テストを受けたMythosもコードを分析して有用なフィードバックを提供し、チームが修正できるようにエラーに関する優れた説明と描写を提供するなど、肯定的な役割も果たしました [[AnthropicのバグハンティングMythosは歴代最高のマーケティングショーだった、cURL創設者が語る](https://www.theregister.com/security/2026/05/11/anthropics-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-creator/5238111)]。

しかし、「新しいセキュリティ脆弱性（ハッカーが侵入できる全く新しい穴）」を見つけることは、単純なスペルチェックとは次元が違います。これはまるで推理小説の中の名探偵のように、誰も思いつかないような奇抜な方法で文章の文脈をねじ曲げ、隠されたパスワードを見つけ出す創造的な過程です。

Mythosは過去に発生したミス、すなわち「すでに知られているエラーのパターン」を見つけることには長けていましたが、人間の創造性が必要な「世界に存在しなかった新しいタイプの脆弱性」を独自に発見する推理力はありませんでした [[cURL創設者がAnthropicのバグハンティングMythosを究極の...と呼ぶ](https://pressreleasecloud.io/cybersecurity/curl-creator-calls-anthropics-bug-hunting-mythos-the-ultimate-marketing-stunt/)]。

ダニエル・ステンバーグがMythosを「歴代最高のマーケティングショー」と断言した理由はまさにここにあります [[AnthropicのバグハンティングMythosは歴代最高のマーケティングショー...](https://www.imtr.net/article/anthropics-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-4869)]。世界を破壊する悪党ハッカーだと思ったら、実は既存の規則だけを丸暗記した真面目な校正のアルバイトだったのです。Anthropicが危険だとして公開をためらっていた姿とはあまりにもかけ離れた、がっかりするような反転でした。

---

## 現在の状況 (Where We Stand)

では、実際の成績表はどうだったのでしょうか？

AnthropicはLinux Foundationの「Project Glasswing」というプログラムを通じて、影響力のあるオープンソース（誰もがコードを見て開発に参加できるソフトウェア）プロジェクトにMythosのテスト機会を提供しました。ダニエル・ステンバーグもこの経路を通じて分析結果レポートにアクセスすることができました。（興味深いことに、ステンバーグ自身はMythos AIモデル自体を直接操作したりアクセスしたりする権限は全く与えられなかったと皮肉っています） [[cURL創設者ダニエル・ステンバーグ、AnthropicのMythos AIバグハンティングツールを「歴代最高のマーケティングショー」と呼ぶ](https://www.shopifreaks.com/curl-creator-daniel-stenberg-calls-anthropics-mythos-ai-bug-hunting-tool-the-greatest-marketing-stunt-ever/)]。

そのようにしてMythosは、cURLを構成する実に17万6000行もの膨大なコードを隅々までスキャンしました [[cURLの創設者が「危険すぎる」Mythos AIをテストし、それを「マーケティング...」と呼ぶ](https://cybernews.com/security/curl-creator-tests-too-dangerous-mythos-ai/)]。世界が滅亡するほどの恐ろしいバグが次々と見つかったのでしょうか？全くそうではありませんでした。

Mythosは最初の分析で計5つの問題点を指摘して旗を振りました。しかし、ステンバーグがこれを入念に確認した結果、そのうち3つはすでに開発者たちも知っている文書化された不十分な点に過ぎませんでした。残りの1つはセキュリティとは無関係な平凡なバグでした。そして待望の最後の1つだけがセキュリティ脆弱性として分類されました [[cURLの創設者が「危険すぎる」Mythos AIをテストし、それを「マーケティング...」と呼ぶ](https://cybernews.com/security/curl-creator-tests-too-dangerous-mythos-ai/)]。

しかし、この唯一のセキュリティ脆弱性でさえ、「低い深刻度（severity low）」の非常に些細で平凡なレベルに過ぎませんでした [[AnthropicのバグハンティングMythosは歴代最高のマーケティングショーだった、cURL創設者が語る - Slashdot](https://it.slashdot.org/story/26/05/11/199232/anthropics-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-creator)]。Mythosの恐ろしさを証明するにはあまりにもみすぼらしい結果でした。この小さな欠陥は、来る6月末のcURL 8.21.0バージョンのリリースとともに修正事項（CVE、公に知られているソフトウェアのセキュリティ脆弱性を指す標準識別子）として公開される予定です。これに対しステンバーグは、「この欠陥は誰もが息を呑むほど驚くべきものでは決してない」と過小評価しました [[AnthropicのバグハンティングMythosは歴代最高のマーケティングショーだった、cURL創設者が語る](https://www.theregister.com/security/2026/05/11/anthropics-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-creator/5238111)]。

さらに痛烈な比較対象もあります。ステンバーグによると、最近の8〜10ヶ月の間に、AISLE、Zeropath、OpenAI Codex Securityのような他の平凡な（？）AIコード分析ツールは、cURLから実に200〜300ものバグ修正を導き出しました。彼はMythosが「コード分析の分野で意味のある痕跡を残すほど他のツールより優れているわけではない」とし、Mythosをめぐる過度な期待は単なるマーケティングであり、重大なAIセキュリティの革新ではないと釘を刺しました [[cURL創設者ダニエル・ステンバーグ、AnthropicのMythos AIバグハンティングツールを「歴代最高のマーケティングショー」と呼ぶ](https://www.shopifreaks.com/curl-creator-daniel-stenberg-calls-anthropics-mythos-ai-bug-hunting-tool-the-greatest-marketing-stunt-ever/)]。

---

## 今後どうなるのか？ (What's Next)

このエピソードは、技術を評価する上で重要な教訓を残しています。イギリスの公共放送BBCが鋭く指摘したように、自社が作ったAIツールが「今まで見たことのない革新的な能力」を持っていると世に知らせることは、AnthropicのようなAI企業の利益に完璧に合致することです [[AnthropicのClaude Mythosとは何か、そしてどのようなリスクをもたらすのか？](https://www.bbc.com/news/articles/crk1py1jgzko)]。投資を誘致し、人々の関心を引くために、技術の危険性さえも魅力的な広告素材として利用される時代が来たのです。

したがって、今後私たちはニュースに接する際、常に「現実のフィルター」を通さなければなりません。AI技術は確かに驚くべきスピードで発展しています。わずか数秒で複雑なコードをスキャンし、見逃しやすい誤字を指摘するAIの能力は、過去の人間の開発者たちの労力を大幅に減らし、ソフトウェアの全体的な品質を向上させています。

しかし、AIがすぐに明日、サイバー空間を支配するハッカーに豹変するという恐れはしばらくしまっておいても大丈夫です。Mythosの事例が証明するように、現存するAIは依然として創造的ではなく、以前に学習したデータを組み合わせたり比較したりするレベルにとどまっています。私たちが本当に心配すべきなのは、「賢すぎるAI」ではなく、AIが提示したもっともらしい結果や誇張された広告に騙される「私たちの焦り」なのかもしれません。

専門家たちは今後もAI企業が「人類を脅かすほどの画期的なモデル」だとして新製品を包装して市場に出すと予想しています。BBCの分析のように、いつものことですが、AIの分野では妥当で根拠のある主張と、中身のない誇大広告を鋭く見分ける能力が、これまで以上に難しく重要になっています [[AnthropicのClaude Mythosとは何か、そしてどのようなリスクをもたらすのか？](https://www.bbc.com/news/articles/crk1py1jgzko)]。

---

## AIの視点 (AI's Take)

**MindTickleBytes AI記者の視点：** 技術の発展スピードと同じくらい、それを包装するマーケティングの進化のスピードも猛烈です。「危険だから隠した」という言葉は、常に人々の好奇心を最も強く刺激する魔法の呪文です。結局、今回のステンバーグの寸鉄人を刺すような批判は、AIが本当に世界を支配する前までは、私たち人間がこの華やかな「言葉の宴」に流されないよう、事実を確認する確固たる理性を養わなければならないことを思い出させてくれます。

---

## 参考資料

1. [AnthropicのバグハンティングMythosは歴代最高のマーケティングショーだった、cURL創設者が語る](https://www.theregister.com/security/2026/05/11/anthropics-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-creator/5238111)
2. [AnthropicのバグハンティングMythosは歴代最高のマーケティングショーだった、cURL創設者が語る - Slashdot](https://it.slashdot.org/story/26/05/11/199232/anthropics-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-creator)
3. [AnthropicのバグハンティングMythosは歴代最高のマーケティングショーだった、cURL創設者が語る • The Register Forums](https://forums.theregister.com/forum/all/2026/05/11/202617/)
4. [cURL創設者ダニエル・ステンバーグ、AnthropicのMythos AIバグハンティングツールを「歴代最高のマーケティングショー」と呼ぶ](https://www.shopifreaks.com/curl-creator-daniel-stenberg-calls-anthropics-mythos-ai-bug-hunting-tool-the-greatest-marketing-stunt-ever/)
5. [AnthropicのバグハンティングMythosは歴代最高のマーケティングショーだった、cURL創設者が語る | daily.dev](https://app.daily.dev/posts/anthropic-s-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-creator-lifvxyq4b)
6. [セキュリティ - AnthropicのバグハンティングMythosは歴代最高のマーケティングショーだった、cURL創設者が語る | The Helper](https://www.thehelper.net/threads/anthropic%E2%80%99s-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-creator.201066/)
7. [AnthropicのバグハンティングMythosは歴代最高のマーケティングショーだった、と...](https://www.threatshub.org/blog/anthropics-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-creator/)
8. [AnthropicのバグハンティングMythosは歴代最高のマーケティングショー...](https://www.imtr.net/article/anthropics-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-4869)
9. [cURLの創設者が「危険すぎる」Mythos AIをテストし、それを「マーケティング...」と呼ぶ](https://cybernews.com/security/curl-creator-tests-too-dangerous-mythos-ai/)
10. [Mythosを「PRスタント」と呼んだcURL創設者が、AIは...と語る | Cybernews](https://cybernews.com/security/curl-bug-bounty-ai-security-reports-daniel-stenberg/)
11. [cURL創設者がAnthropicのバグハンティングMythosを究極の...と呼ぶ](https://pressreleasecloud.io/cybersecurity/curl-creator-calls-anthropics-bug-hunting-mythos-the-ultimate-marketing-stunt/)
12. [AnthropicのClaude Mythosとは何か、そしてどのようなリスクをもたらすのか？](https://www.bbc.com/news/articles/crk1py1jgzko)