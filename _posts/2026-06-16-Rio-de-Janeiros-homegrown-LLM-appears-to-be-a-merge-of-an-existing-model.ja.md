---
layout: post
title: "ブラジル・リオデジャネイロの「独自開発」AI、実はつぎはぎだった？ 3,970億パラメータの真実"
description: "リオデジャネイロが発表した独自開発の巨大人工知能モデルが、実は既存のオープンソースモデルを混ぜ合わせた「モデルマージ（Merge）」の産物であることが判明しました。この事件が意味することを分かりやすく解説します。"
summary: "ブラジルのリオデジャネイロ市政府が野心的に公開した巨大人工知能モデルが、独自開発ではなく既存モデルのつぎはぎであることが判明し、真の「ローカルAI」開発の現実的な難しさが浮き彫りになりました。"
tags: [人工知能, ローカルAI, 大規模言語モデル, モデルマージ, オープンソース, 技術検証]
image: 2026-06-16-Rio-de-Janeiros-homegrown-LLM-appears-to-be-a-merge-of-an-existing-model.jpg
image_alt: "異なる色の2つの歯車が巨大な1つの機械装置に無理やりはめ込まれている様子を描いたイラスト。複数の人工知能を混ぜ合わせて1つに見せかけた「つぎはぎ」の論争を隠喩的に表現している。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "人工知能モデルの巨大な規模が、都市や国の技術的なプライドを代弁する時代になりました。しかし、世界中の開発者が見守る透明なオープンソースエコシステムの前では、中途半端な再パッケージングはかえって信頼を損なうという事実を忘れてはなりません。"
quiz:
  - question: "リオデジャネイロ市政府が野心的に発表したモデル「Rio-3.5-Open-397B」について、最近明らかになった事実は何ですか？"
    choices: ["世界で初めて人間の感情を完璧に理解するモデルであることが判明した。", "すでに公開されている他の人工知能モデルを単に混ぜ合わせただけのモデルだった。", "すべての開発プロセスを透明に公開し、称賛を浴びた。"]
    answer: 1
    explanation: "該当モデルは独立して訓練されたものではなく、既存の「Nex-AGI」と「Qwen3」モデルをマージ（Merge）したものであることが判明しました。"
  - question: "論争が拡大する中、開発を主導したIplanRIO（イプランリオ）側はどのような釈明を出しましたか？"
    choices: ["ハッキングに遭い、元のファイルが改ざんされた。", "データ不足によるやむを得ない選択だった。", "最終バージョン（蒸留モデル）の代わりに、中間段階のマージバージョンを誤ってアップロードしてしまった。"]
    answer: 2
    explanation: "IplanRIO側は、最終的に調整した「蒸留モデル」をアップロードするつもりだったが、誤って「基本マージバージョン」をアップロードしてしまったと謝罪しました。"
  - question: "技術専門家たちが今回の事態を見て指摘した、「ローカルAI（Local AI）」開発における最も大きな現実的障壁は何ですか？"
    choices: ["世の中になかった新しい人工知能をゼロから作り出すことは非常に難しい。", "AI開発に必要な電力が不足している。", "関連する法的規制が厳しすぎる。"]
    answer: 0
    explanation: "専門家たちは、全く新しいものを構築する独自開発は非常に難しい反面、既存のモデルを再パッケージングするのは簡単であるため、このようなことが起こると分析しました。"
lang: ja
ref: 2026-06-16-Rio-de-Janeiros-homegrown-LLM-appears-to-be-a-merge-of-an-existing-model
---

## 序論：華麗なデビューの裏に隠された真実

想像してみてください。世界的に有名なマジシャンが、何年にもわたる骨を削るような修行の末、世界に一つだけの空中浮遊マジックを発明したと宣言します。華やかな照明の下、大勢の観客がスタンディングオベーションで熱狂している中、舞台裏を偶然覗き込んだ一人の少年が叫びます。「あれ？ ただ2本のロープを巧妙に結んで天井から吊るしているだけじゃないか！」

この興味深い物語が最近、世界中の最先端技術がしのぎを削る人工知能（AI）業界で現実に起こりました。ブラジルを象徴する都市、リオデジャネイロ（Rio de Janeiro）の市政府が自ら一から開発したと誇らしげに公開した巨大人工知能モデルが、実は他人が作った技術を巧妙に混ぜ合わせた「つぎはぎ」の産物であるという疑惑が事実として明らかになったのです。

今日、多くの国や都市は、外国の巨大テクノロジー企業に依存しないために、独自のAIを持とうと奮闘しています。では、リオデジャネイロでは一体何が起きたのでしょうか？ なぜ人々はこの技術が偽物であると確信するようになり、この事件が私たちの未来に投げかけるメッセージとは何でしょうか？ 賢い友人が温かいコーヒーを飲みながら語ってくれる物語のように、この事態の全貌を分かりやすく面白く紐解いてみましょう。

## なぜ重要なのか：「国産AI」の夢と3,970億個の星

私たちが毎日使っているスマートフォンの音声アシスタントやChatGPTのようなサービスは、とてつもない規模の「大規模言語モデル（LLM：大量のテキストを学習して人間の言語を理解し、文章を生成するAIシステム）」を基盤として動作しています。最近、世界各国は自国のデータ主権と固有の文化的特性を守るために、「ローカルAI（Local AI）」または「ソブリンAI（Sovereign AI）」と呼ばれる独自の人工知能開発に死力を尽くしています。

先週、リオデジャネイロのIT専門機関である「IplanRIO（イプランリオ）」は、歴史的な快挙を発表しました。世界中のAI開発者がコードを共有する図書館のようなプラットフォーム「Hugging Face（ハギングフェイス）」に、なんと**「Rio-3.5-Open-397B」**という名の巨大モデルを堂々と公開したのです [出処: Rio de Janeiro's 'Homegrown' AI Was Someone Else's Model Wit...](https://dev.to/jamilxt/rio-de-janeiros-homegrown-ai-was-someone-elses-model-with-a-new-name-jcb)。

この名前の後に付いている「397B」という数字に注目する必要があります。これは、該当の人工知能が**3,970億個のパラメータ（Parameter）**を持っていることを意味します。簡単に言うと、パラメータは写真アプリで色合いや明るさを微調整する「ダイヤル」のようなものです。人工知能モデルの内部では、数多くの知識を記憶し判断を下すために、これらのダイヤルが絶え間なく回っています。3,970億個という数字は、晴れた日の夜空を超えて、私たちの銀河系全体に浮かぶ星の数に匹敵するほどの驚異的な規模です。これほどの体格は、GoogleやMicrosoftのような世界トップクラスのビッグテック企業が天文学的な費用をかけて作る最先端モデルと肩を並べるということを意味します [出処: Rio de Janeiro's 'Homegrown' AI Was Someone Else's Model Wit...](https://dev.to/jamilxt/rio-de-janeiros-homegrown-ai-was-someone-elses-model-with-a-new-name-jcb)。

もし一都市の政府機関がこのような途方もない人工知能を完全に「独自開発」したとすれば、それは人類の技術史に残る途方もない成果だったはずです。しかし、この偉大な祭典はすぐに致命的な疑惑に包まれることになります。

## わかりやすく解説：「独自開発」と「モデルマージ」の決定的な違い

この事件の核心を突くためには、人工知能を「独自に学習（Train）させること」と、単に「マージ（Merge）すること」の本質的な違いを理解しなければなりません。

比喩的に言えば、あなたが世の中になかった全く新しい味の特製カレーを世に出すと想像してみてください。
**「独自開発（独自学習）」**は、畑で直接ジャガイモや玉ねぎを育て、インドの荒涼とした土地からスパイスを輸入し、配合比率を何千回もテストしながら、自分だけの完璧なカレー粉を作り上げる険しい道のりです。膨大な時間と莫大なお金、そして数多くの専門家の汗と努力が必要です。AIの世界で言えば、これは何千台もの超高価なコンピュータ（GPU）を数ヶ月間昼夜問わず稼働させ、膨大な量のデータをゼロからスプーンで食べさせるように教え込む、孤独で過酷なプロセスです。

一方、**「モデルマージ（Model Merge）」**は全く別の話です。近所の大型スーパーですでにベストセラーとして売られている「A社の固形カレー」と「B社の辛口カレー」を買ってきて、大きな鍋に一緒に入れて煮込むようなものです。2つのカレーが混ざり合うことで、それなりに本格的で美味しい結果が出ることはあります。しかし、この混ざり合った料理を大衆の前に出して、「これは我が市政府が何年も研究し、ゼロから独自に開発した革新的な新製品カレーです！」と宣伝したらどうなるでしょうか？ これは明らかな欺瞞行為となります。

残念ながら、リオデジャネイロが発表した「独自開発」のAIモデルは、全く新しい基盤の上で独立して訓練されたシステムではありませんでした [出処: RiodeJaneiro's"homegrown"LLMappearstobeamergeofan...](https://deepintellica.com/ai-work/rio-de-janeiro-s-homegrown-llm-appears-to-be-a-merge-of-an-existing-model/)。

## 現在の状況：GitHubの名探偵たちの活躍と苦しい釈明

驚くべきことに、この巨大な技術的虚勢を真っ先に見抜いたのは、大手メディアでも政府の監査機関でもありませんでした。世界中の何千万ものプログラマーが活動するソフトウェア開発プラットフォーム、「GitHub（ギットハブ）」の平凡な開発者たちでした。GitHubのバグ報告スペースである「Issue（イシュー）」掲示板で、誰かが鋭い質問を投げかけたことで真実のパンドラの箱が開いたのです [出処: Cosmic Rundown: Billion Dollar Essays, Rio's LLM Drama, Context Window Limits](https://www.cosmicjs.com/blog/cosmic-rundown-billion-dollar-essays-rio-llm-context-windows)。

コミュニティの分析の結果、この「独自開発モデル」は実は、既存のインターネット上で無料で公開され、誰でもダウンロードできた**「Nex-AGI」**というモデルと**「Qwen3」**というモデルを精巧に混ぜ合わせた（Merge）ものであるという事実が次々と明らかになりました [出処: Rio LLM Exposed: Major Model Merge, Not Original AI](https://www.squaredtech.co/rios-official-ai-model-is-proven-to-be-a-model-merge), [出処: RiodeJaneiro's"homegrown"LLMappearstobeamergeofan...](https://deepintellica.com/ai-work/rio-de-janeiro-s-homegrown-llm-appears-to-be-a-merge-of-an-existing-model/)。

コンピュータのコードと数学的な数値からなるAIモデルの内部の脳構造を解剖した結果、ゼロから新しく学習したという証拠はただの一つも発見されませんでした。他人のモデルを物理的に混合したという明白な物的証拠だけがこぼれ落ちてきたのです [出処: Rio LLM Exposed: Major Model Merge, Not Original AI](https://www.squaredtech.co/rios-official-ai-model-is-proven-to-be-a-model-merge)。開発者たちの遊び場であるGitHubが、まるで不正を告発する目安箱や鋭い調査報道ブログのように使われたというわけです [出処: Hacker News 20 on X: "Rio de Janeiro's "homegrown" LLM appears to be a merge of an existing model https://t.co/G1dBFWiQcO (https://t.co/Uht1ZUEPrL)" / X](https://x.com/betterhn20/status/2066300653404667962), [出処: RiodeJaneiro's"homegrown"LLMappearstobeamergeofan...](https://deepintellica.com/ai-work/rio-de-janeiro-s-homegrown-llm-appears-to-be-a-merge-of-an-existing-model/)。

批判の声が山火事のように広がると、開発を主導したIplanRIO側は慌てて釈明文を出しました。彼らは「以前のバージョンをアップロードする過程で、間違ったファイルを上げてしまうミスを犯した。最終的に完成した**『蒸留モデル（Distilled model）』**をアップロードすべきだったが、作業の中間段階であった**『基本マージバージョン（Base merged version）』**を誤ってアップロードしてしまった」と謝罪しました [出処: RiodeJaneiro's"homegrown"LLMappearstobeamergeofan...](https://news.ycombinator.com/item?id=48528371)。

ここで言う**「蒸留（Distillation）」**とはまた何でしょうか？ 大きなコーヒーマシンで大量のコーヒー豆を強く圧搾し、非常に濃くて香り高いエスプレッソの原液を一杯抽出することを思い浮かべてみてください。AI分野において蒸留技術とは、体が大きすぎて扱うのが難しい天才AI（教師モデル）の核心知識だけをすくい出し、スマートフォンのような小さなデバイスでも高速で動作する軽いAI（生徒モデル）に圧縮する高度な技術です。

つまり、市政府の言い訳は「私たちが他のモデルを混ぜ合わせて鍋で煮た（Merge）のは事実だが、本来大衆に公開しようとしていたのは、その結果をきれいに圧縮した完成版のエスプレッソ（蒸留モデル）だった」という意味です。しかし百歩譲って単なるアップロードミスだったとしても、市民の税金が投入された公共の人工知能の骨格が、結局のところ「他人のモデルを混ぜ合わせたもの」であるという本質は少しも変わりません。

## 今後の展望：再パッケージングの時代、真のイノベーションを見極める方法

今回の「リオデジャネイロスキャンダル」は、独自のAIエコシステムを構築しようとする世界中の多くの自治体や企業に対して、重い現実の壁を思い知らせてくれました。

ソーシャルメディアX（旧Twitter）で活動するある有名な技術専門家は、この茶番劇を見守りながら次のように鋭く指摘しました。「リオデジャネイロの独自開発というモデルですか？ 結局、既存モデルのつぎはぎであることが判明しましたね。『ローカルAI』を取り巻く熱狂的な期待（Hype）は、常に同じ巨大な壁に頭をぶつけることになります。世の中になかった全く新しいものを実際に作り出すことは過酷で難しすぎるのに対し、既存のものをそれらしく再パッケージング（Repackaging）するのははるかに簡単だからです。」 [出処: Anto Patrex on X: "Rio de Janeiro's supposedly homegrown LLM? Turns out it's a merge of existing models. The hype around 'local AI' keeps running into the same wall: actually building something novel is hard. Repackaging is easier." / X](https://x.com/antopatrex1/status/2066375933108314528)

今後、人工知能技術が私たちの生活の深くまで入り込むにつれて、多くの機関が競って「ついに独自の人工知能を完成させた！」と華やかなファンファーレを鳴らすでしょう。しかし私たちは今後、その華やかな包装紙の中を非常に注意深く批判的な視線で覗き込まなければなりません。一見すると数千億個のパラメータを持つ偉大な発明品のように見えても、その中身は誰かが血と汗を流して作った無料のオープンソースモデルをこっそり混ぜ合わせたものに過ぎないかもしれないからです。

## AIの視点：透明性こそが最高の技術力である

人工知能モデルの巨大な規模や天文学的なパラメータの数が、都市や国の技術的なプライドを代弁する時代になりました。独自の技術力を確保しようとするリオデジャネイロの熱望自体を、無条件に非難することはできません。莫大な資本力の限界を克服するために、既存のオープンソース技術を賢く結合して活用することは、現代のソフトウェア開発の自然かつ効率的な流れでもあります。

しかし、世界中の数多くの天才開発者たちが目を皿のようにして見守る透明なオープンソースエコシステムの前では、中途半端な再パッケージングや誇大広告は、かえって信頼を深刻に損なうという事実を忘れてはなりません。真の技術的独立と主権の確保は、インターネット上に出回っているレシピに従って調味料を混ぜ合わせ、大げさな名前をつけることから生まれるわけではありません。荒涼とした環境の中でも正直に良質なローカルデータを収集し、自分たちの限界を透明に共有しながら一歩ずつ進んでいく忍耐の中でこそ、本物のイノベーションの花が咲くのです。リオデジャネイロの短く虚しい天下は、AI時代を生きる私たち全員にとって、最も辛くとも価値ある教訓を残しました。

## 参考資料

1. [Rio de Janeiro's 'Homegrown' AI Was Someone Else's Model Wit...](https://dev.to/jamilxt/rio-de-janeiros-homegrown-ai-was-someone-elses-model-with-a-new-name-jcb)
2. [RiodeJaneiro's"homegrown"LLMappearstobeamergeofan... (Deep Intellica)](https://deepintellica.com/ai-work/rio-de-janeiro-s-homegrown-llm-appears-to-be-a-merge-of-an-existing-model/)
3. [Rio LLM Exposed: Major Model Merge, Not Original AI](https://www.squaredtech.co/rios-official-ai-model-is-proven-to-be-a-model-merge)
4. [Cosmic Rundown: Billion Dollar Essays, Rio's LLM Drama, Context Window Limits](https://www.cosmicjs.com/blog/cosmic-rundown-billion-dollar-essays-rio-llm-context-windows)
5. [Hacker News 20 on X: "Rio de Janeiro's "homegrown" LLM appears to be a merge of an existing model https://t.co/G1dBFWiQcO (https://t.co/Uht1ZUEPrL)" / X](https://x.com/betterhn20/status/2066300653404667962)
6. [RiodeJaneiro's"homegrown"LLMappearstobeamergeofan... (Hacker News Discussion)](https://news.ycombinator.com/item?id=48528371)
7. [Anto Patrex on X: "Rio de Janeiro's supposedly homegrown LLM? Turns out it's a merge of existing models. The hype around 'local AI' keeps running into the same wall: actually building something novel is hard. Repackaging is easier." / X](https://x.com/antopatrex1/status/2066375933108314528)