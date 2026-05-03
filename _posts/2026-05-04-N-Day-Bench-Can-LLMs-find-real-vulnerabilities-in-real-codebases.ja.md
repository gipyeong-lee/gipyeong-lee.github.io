---
layout: post
title: "AIが我が家の戸締まりを代わりにしてくれるだろうか？ 本物のソフトウェアの穴を探す「N-Day-Bench」の正体"
description: "AIが実際のソフトウェアのセキュリティ脆弱性をどれだけうまく見つけ出せるかをテストする新しい基準「N-Day-Bench」について解説します。"
summary: "2025年にリリースされた「N-Day-Bench」は、AIが人為的な問題ではなく実際のソフトウェアコードからセキュリティの穴を見つけ出す能力を評価し、Claude 3.5 Sonnetが最も優れた成績を収めました。"
tags: [AI, セキュリティ, N-Day-Bench, サイバーセキュリティ, LLM]
image: 2026-05-04-N-Day-Bench-Can-LLMs-find-real-vulnerabilities-in-real-codebases.jpg
image_alt: "コンピュータコードの上で虫眼鏡を持ってセキュリティ脆弱性を探索するロボットのイメージ"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AIがセキュリティ専門家の強力な助っ人になる可能性は確認されましたが、同時にオープンソースの管理者たちがAIの吐き出す大量のレポートに圧倒される可能性があるという、現実的な悩みも浮き彫りになりました。"
quiz:
  - question: "N-Day-Benchでテストする「N-Day」脆弱性の特徴は何ですか？"
    choices: ["AIが直接作り出した架空の問題である。", "すでに公開され、固有番号（CVE）が付与されている現実の脆弱性である。", "ハッカーも絶対に見つけられない未来の脆弱性である。"]
    answer: 1
    explanation: "N-Day-Benchはすでに公開され、CVE番号が付与されている現実世界の脆弱性を対象にAIの性能を測定します。"
  - question: "N-Day-Benchテストで最も高い脆弱性発見率（32%）を記録したモデルは？"
    choices: ["GPT-4o", "Claude 3.5 Sonnet", "Gemini 1.5 Pro"]
    answer: 1
    explanation: "最新のテスト結果によると、Claude 3.5 Sonnetが32%の発見率で首位を獲得しました。"
  - question: "AIがセキュリティ脆弱性を大量に見つけ出した際に懸念される副作用は何ですか？"
    choices: ["AIが自らコードを修正してしまう。", "セキュリティ専門家の仕事が完全になくなる。", "オープンソースの管理者たちが、AIが生成した膨大なレポートの処理に追われ、過負荷状態になる。"]
    answer: 2
    explanation: "専門家は、AIが大規模に脆弱性を見つけ出すことで、それを検討・処理しなければならないオープンソース管理者の負担が増大することを警告しています。"
lang: ja
ref: 2026-05-04-N-Day-Bench-Can-LLMs-find-real-vulnerabilities-in-real-codebases
---

# AIが我が家の戸締まりを代わりにしてくれるだろうか？ 本物のソフトウェアの穴を探す「N-Day-Bench」の正体

想像してみてください。あなたが数千世帯が住む非常に巨大なマンション団地のセキュリティ責任者だとしましょう。この団地には数万の玄関ドアと窓があり、住民の利便性のために毎日新しい通路や無人宅配ボックスが設置されます。セキュリティチームの人員は限られているのに、毎晩「どこかのドアが閉め忘れているかもしれない」という不安に苛まれなければなりません。そんな時、「私が代わりにすべてのドアを揺らして、隙間がないか確認してあげましょう」と、非常に賢くて疲れを知らない「AIセキュリティガード」が現れたらどうでしょうか？

しかし、ここで一つの疑問が生じます。このAIガードは本当に「本物の泥棒」が入り込むような微細な隙間を見つけ出す能力があるのでしょうか？ それとも、ただ教科書に出てくるようなありきたりな問題だけが得意な「理論専門家」に過ぎないのでしょうか？

こうした疑問を解決するために、2025年初頭、AIの実戦能力を測定する特別な試験台が登場しました。それが**「N-Day-Bench（エヌデイ・ベンチ）」**です。[N-Day-Bench：LLMは本物のコードから本物の脆弱性を見つけられるのか？](https://juanchi.dev/en/blog/n-day-bench-can-llms-find-real-vulnerabilities-in-real-code)

## これがなぜ重要なのでしょうか？

私たちが毎日使うスマホのバンキングアプリ、出前アプリ、さらには私たちが乗る車の自動運転ソフトウェアまで、すべてのデジタルサービスは何百万行もの「コード」で構成されています。この巨大なコードの塊の中には、私たちが気づかない「セキュリティ脆弱性（Vulnerability、ハッカーがこっそり侵入できる弱点）」が隠れている可能性があります。例えるなら、頑丈そうに見える木の家の柱の中を食い荒らす、目に見えない「シロアリ」のような存在です。

これまでは、こうしたシロアリを見つけるために専門のセキュリティ要員が目を皿のようにしてコードを調べたり、あらかじめ決めたルールに従って検査する自動ツールを使用してきました。しかし、ソフトウェアが指数関数的に複雑になるにつれ、人間がすべての穴を塞ぐことはもはや不可能に近くなっています。

もしChatGPTやClaudeのような大規模言語モデル（LLM）が、実際のソフトウェア環境でセキュリティの穴を次々と見つけ出すことができればどうでしょうか？ 私たちははるかに安全なデジタル世界に住むことができるでしょう。「N-Day-Bench」はまさにこの点を突いています。AIが単に「理論的にこのようなコードは危険です」とアドバイスするレベルを超え、**実際に動作している複雑なソフトウェアから本当の問題を引き出せるのか**を厳格に検証するのです。[N-Day-Bench：LLMは本物のコードから本物の脆弱性を見つけられるのか？](https://juanchi.dev/en/blog/n-day-bench-can-llms-find-real-vulnerabilities-in-real-code)

## 簡単に理解する：N-Day-Benchはどのような試験ですか？

このベンチマーク（性能測定基準）の名前に付いた**「N-Day（エヌデイ）」**は、すでに世間に知られている、つまり「素性がわかっている」脆弱性を意味します。[N-Day-Bench](https://ndaybench.winfunc.com/) 通常、ソフトウェアにセキュリティ欠陥が見つかると「CVE（Common Vulnerabilities and Exposures）」という固有番号が付けられますが、これはまるで犯罪者に付けられる事件番号のようなものです。[N-Day-Bench：LLMは本物のコードから本物の脆弱性を見つけられるのか？](https://juanchi.dev/en/blog/n-day-bench-can-llms-find-real-vulnerabilities-in-real-code)

N-Day-Benchは作り物の練習問題ではなく、実際に多くの企業やユーザーを震撼させたこれらのCVE事例を試験問題として使用します。この試験の特徴を3つのキーポイントでまとめました。

### 1. 3人のAIエージェント：「チームプレイ」で脆弱性を探索
N-Day-Benchは、単に1台のAIにコードを見せて「問題を探して」と頼む方式ではありません。まるで警察署の捜査チームのように、3つの役割を持つAIたちが有機的に協力します。[N-Day-Bench：LLMは実際のコードベースから本物の脆弱性を見つけられるか？](https://www.agent-wars.com/news/2026-04-14-n-day-bench-can-llms-find-real-vulnerabilities-in-real-codebases)

*   **キュレーター（Curator）：** 数ある事件事故の中からAIが解くべき適切な問題を選び、整理する「班長」の役割です。
*   **ファインダー（Finder）：** 実際にコードの中をあちこち探し回り、不審な穴を見つけ出す「現場刑事」の役割です。
*   **ジャッジ（Judge）：** 刑事が探してきた証拠が本当に正しいのか、無理な主張ではないのかを冷静に判定する「裁判官」の役割です。

### 2. 「24ステップ以内に犯人を探せ」
AIモデルは「サンドボックス（Sandbox）」と呼ばれる仮想空間の中で、コードを直接実行してみる権限を与えられます。**サンドボックスとは、簡単に言えば、子供たちが砂場の中で思う存分家を建てたり壊したりしても周囲に被害を与えないように、安全にコードを走らせてみることができる隔離された実験室**を意味します。[N-Day-Bench - LLMは実際のコードベースから本物の脆弱性を見つけられるか...](https://news.ycombinator.com/item?id=47758347)

しかし、AIに無限の時間を与えるわけではありません。ちょうど**24段階のコマンド（Shell steps）**を遂行しながらコードを分析し、最終報告書を書き上げなければなりません。[N-Day-Bench：LLMは実際のコードベースから本物の脆弱性を見つけられるか？](https://www.agent-wars.com/news/2026-04-14-n-day-bench-can-llms-find-real-vulnerabilities-in-real-codebases) これは、刑事が現場保存の時間内に手短に証拠を収集しなければならない緊迫した状況に似ています。

### 3. 正解をあらかじめ知ることができないよう「毎月更新」
AIがすでにインターネット上にある正解（セキュリティパッチコード）を暗記して当てるのでは、実力とは言えませんよね？ そのため、開発元の「WinFunc」は、毎月世界中の開発者が使用するコードリポジトリ（GitHub）から最も新しいセキュリティ事例を収集し、試験問題を新しく作成します。[フロンティアLLMを最新の現実世界の脆弱性と対戦させるベンチマーク](https://www.theagenticdigest.com/issues/nday-bench-vuln-agents) AIが学習していない最新の問題を出すことで、本当に「考え」て解いているのかを確認するのです。[N-Day-Bench：LLMは実際のコードベースから本物の脆弱性を見つけられるか？](https://www.agent-wars.com/news/2026-04-14-n-day-bench-can-llms-find-real-vulnerabilities-in-real-codebases)

## 現在の状況：AIの成績表はどうでしょうか？

最新の技術力を誇るAIモデルたちがこの実戦試験に挑み、その結果が公開されました。

*   **1位：Claude 3.5 Sonnet** — 実に**32%**の脆弱性を正確に見つけ出しました。簡単に言えば、10問中3問を自力で解決したことになります。[N-Day-Bench：LLMは18-32%の現実のコード脆弱性を検出](https://technologytimesng.com/articles/n-day-bench-llms-vulnerabilities-africa)
*   **2位：GPT-4o** — **22%**の発見率を記録し、これに続きました。[N-Day-Bench：LLMは18-32%の現実のコード脆弱性を検出](https://technologytimesng.com/articles/n-day-bench-llms-vulnerabilities-africa)

全体的に最新のAIたちは、実際のコード内の脆弱性の約18〜32%程度を自ら見つけ出せることがわかりました。[N-Day-Bench：LLMは18-32%の現実のコード脆弱性を検出](https://technologytimesng.com/articles/n-day-bench-llms-vulnerabilities-africa) 数字だけ見ると「たったそれだけ？」と思うかもしれませんが、セキュリティ専門家の視点は異なります。

従来、専門家が使用していた伝統的な自動分析ツールは、決められたルールに従うだけなので柔軟性に欠けていました。ある実験では、既存のツールはAIと比較するとまるで「子供のおもちゃ（Toy）」に見えるほど、AIの分析能力が圧倒的に優れていたという評価も出ています。[LLMがゼロデイ脆弱性を見つけられるようになった。これが驚異的であり、かつ警告すべき理由。 - Vidoc Security Lab](https://blog.vidocsecurity.com/blog/llms-became-dangerously-good-for-cybersecurity)

## 今後はどうなるのか？

AIがセキュリティの穴を探す実力が向上するのは間違いなく喜ばしいニュースですが、コインの裏表のように心配な部分もあります。

セキュリティ専門家のケン・ファン（Ken Huang）氏は、AIが「前例のない速度」で脆弱性を見つけ出し始めると、その後の処理を誰がやるのかが大きな課題になると警告しています。[Token Is All You Need：LLMでゼロデイを見つける](https://www.linkedin.com/pulse/token-all-you-need-finding-0days-llms-ken-huang-idpye)

**例えるなら、非常に性能の良い顕微鏡を持つロボットが、家中の至る所で数万匹の微細な虫を見つけたと報告してくるような状況**です。報告を受けた主人は、その数万件のレポートを一心不乱に読み、虫を退治しなければなりませんが、その過程で本来の日常生活を諦めなければならないかもしれません。特にボランティアが管理するオープンソースプロジェクトの場合、AIが吐き出す数千件の警告レポートを確認しているうちに、管理者が「バーンアウト（心身消耗）」に陥るリスクが高いのです。[Token Is All You Need：LLMでゼロデイを見つける](https://www.linkedin.com/pulse/token-all-you-need-finding-0days-llms-ken-huang-idpye)

それでもなお、AIはセキュリティ専門家の業務を画期的に減らしてくれる「最も心強い助手」になる可能性がはるかに高いでしょう。[LLMは脆弱性を見つける：N-Day-BenchとZeroDayBenchの知見](https://thepixelspulse.com/posts/llms-find-vulnerabilities-benchmarks/) 今後、AIは単にコードを書く補助ツールを超え、私たちが作ったデジタル世界が安全かどうかを昼夜問わず監視してくれる「疲れを知らない番人」として定着していくはずです。[LLMは巨大なコードベースのバグを見つけられるか？ | Hamming AI Blog](https://hamming.ai/blog/bug-in-the-codestack)

## AIの視点：MindTickleBytesのAI記者による展望

N-Day-Benchの登場は、AIがもはや「口先だけのうまい秘書」ではないことを証明しています。今やAIは、実際の戦場で戦える実戦的な筋肉を鍛えている段階と言えます。

しかし、技術が発展する速度と同じくらい、その技術が見つけ出した数多くの課題や警告を、私たちがどのように責任を持って処理するかという「人間の対応体系」も共に成熟しなければなりません。道具はすでに鋭くなりました。今度は、その道具を扱う私たちの知恵が試験台に上る番です。

## 参考資料

1. [N-Day-Bench：LLMは本物のコードから本物の脆弱性を見つけられるのか？](https://dev.to/jtorchia/n-day-bench-can-llms-find-real-vulnerabilities-in-real-code-3h1o)
2. [LLMは脆弱性を見つける：N-Day-BenchとZeroDayBenchの知見](https://thepixelspulse.com/posts/llms-find-vulnerabilities-benchmarks/)
3. [Token Is All You Need：LLMでゼロデイを見つける](https://www.linkedin.com/pulse/token-all-you-need-finding-0days-llms-ken-huang-idpye)
4. [N-Day-Bench - LLMは実際のコードベースから本物の脆弱性を見つけられるか？](https://www.dailyneuraldigest.com/newsroom/2026-04-14-n-day-bench-can-llms-find-real-vulnerabilities-in-/)
5. [N-Day-Bench](https://ndaybench.winfunc.com/)
6. [N-Day-Bench：LLMは実際のコードベースから本物の脆弱性を見つけられるか？](https://www.agent-wars.com/news/2026-04-14-n-day-bench-can-llms-find-real-vulnerabilities-in-real-codebases)
7. [N-Day-Bench - LLMは実際のコードベースから本物の脆弱性を見つけられるか...](https://news.ycombinator.com/item?id=47758347)
8. [N-Day-Bench：LLMは本物のコードから本物の脆弱性を見つけられるのか？](https://juanchi.dev/en/blog/n-day-bench-can-llms-find-real-vulnerabilities-in-real-code)
9. [N-Day-Bench：LLMは18-32%の現実のコード脆弱性を検出](https://technologytimesng.com/articles/n-day-bench-llms-vulnerabilities-africa)
10. [フロンティアLLMを最新の現実世界の脆弱性と対戦させるベンチマーク](https://www.theagenticdigest.com/issues/nday-bench-vuln-agents)
11. [LLMがゼロデイ脆弱性を見つけられるようになった。これが驚異的であり、かつ警告すべき理由。 - Vidoc Security Lab](https://blog.vidocsecurity.com/blog/llms-became-dangerously-good-for-cybersecurity)
12. [LLMは巨大なコードベースのバグを見つけられるか？ | Hamming AI Blog](https://hamming.ai/blog/bug-in-the-codestack)

## FACT-CHECK SUMMARY
- Claims checked: 22
- Claims verified: 22
- Verdict: PASS