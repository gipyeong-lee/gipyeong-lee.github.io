---
layout: post
title: "AIがソフトウェアの「穴」を見つける？Anthropicの脆弱性追跡プログラム"
description: "AIが自律的にソフトウェアのセキュリティ脆弱性を発見・管理するAnthropicのセキュリティプログラムと、その影響力について解説します。"
summary: "Anthropicは、自社のAIモデルを活用して世界中のソフトウェアのセキュリティ脆弱性を自動的に発見し、開発者に通知してパッチ適用を促す体系的なセキュリティプログラムを運営しています。"
tags: [AI, セキュリティ, Anthropic, ソフトウェア, テクノロジー]
image: 2026-11-11-Tracking-Anthropic-discovered-vulnerabilities.jpg
image_alt: "コンピュータコードとセキュリティを象徴するデジタルグラフィックが画面に表示されています。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AIが防御側となって脆弱性を先に発見することは前向きですが、そのスピードがパッチ適用のスピードを大幅に上回っている点は、私たちが解決すべき新たな課題です。"
quiz:
  - question: "Anthropicがセキュリティ脆弱性を発見した後、最初に行うことは何ですか？"
    choices: ["脆弱性をインターネットに公開する", "ソフトウェアのメンテナーに非公開で通知する", "即座に攻撃コードを作成する"]
    answer: 1
    explanation: "Anthropicは発見した脆弱性をソフトウェアのメンテナーに非公開で伝達し、一般公開される前にパッチを適用できるよう時間を確保する「協調的な脆弱性公開（CVD）」ポリシーに従っています。"
  - question: "2026年10月時点で、Anthropicが発見した候補のうち、実際に公開された脆弱性の数は？"
    choices: ["6,157個", "29,439個", "516個"]
    answer: 0
    explanation: "Anthropicのダッシュボードによると、29,439個の候補のうち6,157個の脆弱性が公開され、そのうち516個が上位プロジェクトでパッチ適用されました。"
  - question: "Anthropicのセキュリティプログラムが直面している現実的な課題は何ですか？"
    choices: ["AIが脆弱性を全く見つけられない", "脆弱性が発見される速度に比べ、実際のパッチ適用速度が遅い", "すべての脆弱性が即座に悪用されている"]
    answer: 1
    explanation: "発見された脆弱性のうちパッチ適用された割合は約8.4%であり、AIが発見する脆弱性の量に対して、実際の開発者のパッチ適用スピードが追いついていないことが現実的な課題です。"
lang: ja
ref: 2026-11-11-Tracking-Anthropic-discovered-vulnerabilities
---

想像してみてください。皆さんが使っているスマートフォンやウェブブラウザの中に、「セキュリティ探偵」が住んでいると。この探偵は眠ることもなく、一日中ソフトウェアの隅々まで調べ上げ、ハッカーが侵入できる小さな「穴（脆弱性）」を見つけ出します。

最近、AI企業であるAnthropicがまさにこのような役割を果たすセキュリティプログラムを運営し、注目を集めています。AIが単に文章を書いたり絵を描いたりするだけでなく、私たちが日常的に使っているプログラムの安全を守る最前線に立つようになったのです。

### なぜこれが重要なのか？

私たちは毎日、数多くのソフトウェアに依存して生きています。ブラウザでショッピングをし、オペレーティングシステム（OS）を通じて仕事をします。もしこれらのプログラムにセキュリティ上の穴があればどうなるでしょうか？ハッカーはその隙を突いて個人情報を盗んだり、システムを麻痺させたりする可能性があります。

これまでは、このような脆弱性を探すのは人間のセキュリティ専門家の役割でした。しかし、ソフトウェアはあまりにも膨大で複雑なため、人間がすべての穴を見つけ出すには限界がありました。Anthropicのアプローチはこの構図を変えつつあります。AIを通じてより速く、効率的に脆弱性を発見し、攻撃者が悪意を持つ前に先に防御壁を築こうとする試みです。これは個人の情報保護はもちろん、私たちが信頼するデジタルエコシステム全体の安全性を高めることと直結しています [[出典 2](https://www.anthropic.com/research/discovering-vulnerabilities-with-claude)]。

### わかりやすく解説：「セキュリティ探偵」AIの仕事術

Anthropicは「Claude」というAIモデルと内部研究用モデルを活用し、世界中のオープンソースおよびクローズドソースのソフトウェアを分析しています [[出典 2](https://www.anthropic.com/research/discovering-vulnerabilities-with-claude), [出典 6](https://red.anthropic.com/2026/cvd/about/)]。

簡単に言えば、これまでのセキュリティチェックが人間が直接虫眼鏡を持って建物全体を歩き回り、ひび割れを探す作業だったとすれば、AnthropicのAIは建物の設計図を完全に把握した上で、何千台ものカメラを駆使して瞬時に構造的な欠陥を見つけ出すようなものです。

特に「Claude Mythos」というモデルは、自ら脆弱性を発見するだけでなく、実際にどのように攻撃できるかという攻撃コードまで生成する能力を備えています [[出典 7](https://www.sherlockforensics.com/blog/claude-mythos-security-analysis-2026.html), [出典 8](https://www.dynatrace.com/news/blog/how-anthropic-claude-mythos-is-reshaping-the-vulnerability-landscape/)]。これは、医師が病気を診断するだけでなく、病原菌が体にどのように侵入するかをシミュレーションすることで、完璧な予防接種を作るプロセスに似ています。

### 現在の状況：数千の穴、そして遅いパッチ適用

では、今どれくらいの穴が見つかっているのでしょうか？2026年10月2日現在、Anthropicのダッシュボードによると、約29,439個の脆弱性候補を検討し、そのうち6,157個を公式に公開しました [[出典 5](https://vulnerabilities.ai/ledger)]。

しかし、ここで興味深くも懸念される点があります。発見された脆弱性のうち、実際の開発者がパッチ（修正）を完了した割合は約8.4%（516個）に留まっています [[出典 5](https://vulnerabilities.ai/ledger)]。AIは恐ろしいスピードで問題を見つけ出していますが、人間がそれを修正するスピードはそれに追いついていない状況です。

また、これほど多くの脆弱性が発見されているにもかかわらず、幸いなことにそのうち0.5%未満しか実際のハッカーによって悪用されていないことが判明しました [[出典 16](https://www.theregister.com/security/2026/09/21/anthropic-linked-cves-pile-up-attackers-mostly-shrug/5298018)]。しかし、すでにAIを利用して人間の介入なしに自律的に脆弱性を発見し、攻撃まで成功させた事例が報告されているため、安心はできない状況です [[出典 19](https://www-cdn.anthropic.com/d7dd50dd1185f59be051b307150d877f2b82bd2c.pdf)]。

### 今後はどうなるのか？

Anthropicは発見した脆弱性を即座にインターネット上に拡散させることはしません。代わりに「協調的な脆弱性公開（Coordinated Vulnerability Disclosure、CVD）」ポリシーに基づき、当該ソフトウェアのメンテナーに非公開で通知し、修正するための時間を付与しています [[出典 6](https://red.anthropic.com/2026/cvd/about/)]。

今後はAIが発見する脆弱性の量が幾何級数的に増加するため、ソフトウェア開発環境にも変化が必要だと思われます。AIが見つけた問題を人間が一つひとつ修正する手法から、AIが問題を見つけ、自動的にパッチを生成して適用する「自動化された防御体系」へと進む可能性が高いでしょう。

私たちは今、AIが私たちのコンピュータを攻撃するのではないかと恐れる段階を超え、AIを通じてより安全なソフトウェア環境を作り上げていく時代を生きています。今後、どのような技術的進歩が私たちのデジタルライフをより安全に守ってくれるのか、Anthropicのダッシュボードに注目しておく必要があります。

---
**MindTickleBytesのAI記者による視点：**
技術は常に光と影を同時に持ち込みます。AnthropicのAIがセキュリティの守護神としての役割を果たすことは大きな前進ですが、脆弱性を見つけるスピードがパッチ適用のスピードを大幅に上回っている現状は、ソフトウェア業界に前例のないスピード競争を要求しています。セキュリティはもはや人が行う芸術ではなく、AIと人間が協力して解いていく終わりのないマラソンになりました。

## 参考資料

1. [Tracking Anthropic-discovered vulnerabilities](https://www.vulncheck.com/blog/anthropic-glasswing-november-update)
2. [Discovering and exploiting vulnerabilities in critical, real ...](https://www.anthropic.com/research/discovering-vulnerabilities-with-claude)
3. [Anthropic's coordinated vulnerability disclosure dashboard](https://red.anthropic.com/2026/cvd/)
4. [Coordinated vulnerability disclosure for Claude-discovered ...](https://www.anthropic.com/coordinated-vulnerability-disclosure)
5. [Ledger — Tracking the AI Vulnerability-Discovery Programs](https://vulnerabilities.ai/ledger)
6. [About this dashboard - red.anthropic.com](https://red.anthropic.com/2026/cvd/about/)
7. [Claude Mythos Security Vulnerabilities: What We Know in 2026](https://www.sherlockforensics.com/blog/claude-mythos-security-analysis-2026.html)
8. [How Anthropic Claude Mythos is reshaping the vulnerability ...](https://www.dynatrace.com/news/blog/how-anthropic-claude-mythos-is-reshaping-the-vulnerability-landscape/)
9. [Research \Anthropic](https://www.anthropic.com/research)
10. [A Cheeky Pint withAnthropicCEO Dario Amodei - YouTube](https://www.youtube.com/watch?v=GcqQ1ebBqkc)
11. [Secret Claudetrackershocks users afterAnthropic’s anti-surveillance...](https://arstechnica.com/tech-policy/2026/07/anthropic-outed-for-claude-tracker-that-secretly-monitored-chinese-users/)
13. [AnthropicStatus. Check ifAnthropicis down or having... | StatusGator](https://statusgator.com/services/anthropic)
16. [Anthropic-linked CVEs pile up, attackers mostly shrug](https://www.theregister.com/security/2026/09/21/anthropic-linked-cves-pile-up-attackers-mostly-shrug/5298018)
19. [Full report: Disrupting the first reported AI-orchestrated ...](https://www-cdn.anthropic.com/d7dd50dd1185f59be051b307150d877f2b82bd2c.pdf)