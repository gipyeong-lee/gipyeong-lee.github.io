---
layout: post
title: "AIコーディングを全面禁止したオープンソースプロジェクト、1ヶ月で撤回した理由は？"
description: "オープンソースファームウェアプロジェクトであるLibrebootが導入した人工知能コード作成禁止政策を1ヶ月で廃止し、スロップ削減政策へ転換した背景を探ります。"
summary: "オープンソースファームウェアプロジェクトのLibrebootがAIコード貢献を禁止してから1ヶ月でこれを撤回し、「スロップ削減政策」へと移行した事件を通じ、オープンソースコミュニティがAI時代に対処する方法を見ていきます。"
tags: [Libreboot, OpenSource, AI, Firmware, TechNews]
image: 2026-11-21-Libreboot-Abandons-Anti-AI-Policy-After-One-Month.jpg
image_alt: "コンピュータの起動画面とオープンソースコードを象徴するデジタルグラフィックイラスト"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "技術の発展速度と人間の信頼構築の間でオープンソースコミュニティが直面する過渡期の苦悩を示す興味深い事例です。完全な排斥よりも緻密な検証システムへと進化していく過程は、今後すべてのソフトウェアエコシステムが経験する標準的な軌跡となるでしょう。"
quiz:
  - question: "Librebootが2026年10月に発表したバージョン26.10で導入した主な政策は何ですか？"
    choices: ["AIコーディング全面禁止政策", "すべての貢献者に対する有料化政策", "クラウド専用ブート移行政策"]
    answer: 0
    explanation: "Librebootはバージョン26.10でAGENTS.mdを通じて人工知能（AI）を使用したコード開発を厳格に禁止する反AI政策を導入しました。"
  - question: "Librebootが最初反AI政策を導入した主な理由として言及されていないものは？"
    choices: ["信頼の低下", "開発者の技術退化の懸念", "AIサーバーの電気代の負担", "著作権の不確実性"]
    answer: 2
    explanation: "初期の反AI政策の理由は、信頼、開発者の技術退化、著作権の不確実性であり、電気代の負担は言及されませんでした。"
  - question: "反AI政策が廃止された後、Librebootが新しく導入した政策の名前は何ですか？"
    choices: ["スロップ削減政策（Slop Reduction Policy）", "AI加速政策", "オープンソース完全開放政策"]
    answer: 0
    explanation: "Librebootは1ヶ月でAI禁止政策を撤回し、高品質ではないAI生成物を管理するための「スロップ削減政策」を導入しました。"
lang: ja
ref: 2026-11-21-Libreboot-Abandons-Anti-AI-Policy-After-One-Month
---

想像してみてください。毎日使うコンピュータの最も深いところ、つまり電源を入れるやいなやオペレーティングシステムが実行される前にハードウェアを目覚めさせるコアプログラムであるBIOS（BIOS、コンピュータの起動およびハードウェア制御を担当する基本システムソフトウェア）あるいはUEFI（Unified Extensible Firmware Interface、既存のBIOSに代わる現代的なコンピュータ起動標準インターフェース）を作る開発者コミュニティがあります。このコミュニティが突然「今後、人工知能（AI）が書いたコードは1行も受け付けない」と宣言しました。世界は大騒ぎになりました。世界中の多くの開発者がAIを補助ツールとして生産性を高め、チャットボットやコーディングアシスタントに依存する時代に、逆行するかのようなこの過激な宣言は大きな波紋を呼びました。

しかし、さらに驚くべき反転はその次に起こりました。なんと1ヶ月も経たないうちに、彼らがその禁止令を自ら撤回したのです。一体、このコミュニティではこの1ヶ月の間に何があったのでしょうか？本記事では、世界の開発者社会を揺るがしたこの興味深い事件の全貌と、そこに込められた人工知能時代の深い悩みを掘り下げていきます。

---

### なぜこれが重要なのか？

私たちは今、ChatGPTやCopilotのような生成AIツールが、日常的な文章作成から複雑なコンピュータプログラミングまで代行してくれる便利な時代に生きています。社会人、学生、開発者を問わず、AIの助けを借りて業務スピードを飛躍的に高めています。しかし、ソフトウェアの根幹をなす「オープンソース（Open Source、ソースコードを公開し、誰もが自由に修正・配布できるソフトウェア開発方式）エコシステム」では、この利便性が単なる祝福だけではありません。

コンピュータの最も基礎的なブートファームウェア（ハードウェアとオペレーティングシステムの間をつなぐ基本ソフトウェア）を扱うプロジェクトであるLibrebootの今回の事件は、技術の利便性の背後に隠された「信頼」と「品質」の問題を世界に真っ向から突き付けました [[Source 10](https://blog.desdelinux.net/en/libreboot-26-10-release-new-features-edk2-uefi-chromebooks/)]. オープンソースソフトウェアは、数多くの開発者の自発的な貢献と信頼を土台に築かれる巨大な城壁のようなものです。もしその城壁を構成するレンガがAIによって無分別に大量生産されるならば、プロジェクトの安全性と信頼性は果たして維持できるでしょうか？今回の事件は、単なる開発者たちのハプニングではなく、私たちがAI時代にデジタルインフラをどのような方法で信頼し構築すべきかを示す非常に重要な試金石となります。

---

### わかりやすく解説：厨房のシェフと自動調理ロボット

この事態をよりわかりやすく理解するために、概念を一つずつ紐解いていきましょう。まず**Libreboot**とは何でしょうか？Librebootは自由およびオープンソースソフトウェアプロジェクトであり、コンピュータの製造元が隠している独占的で閉鎖的なBIOSやUEFIファームウェアを代替するために作られたブートファームウェアディストリビューションです [[Source 2](https://en.wikipedia.org/wiki/Libreboot), [Source 3](https://libreboot.org/)]。コンピュータが起動するときに最も先に実行されてハードウェアを初期化し、LinuxやBSDのようなオペレーティングシステムを安全に呼び出す役割を果たします [[Source 3](https://libreboot.org/)]。

理解を深めるために、最初の比喩を出してみましょう。比喩するならば、Librebootはまるで**「家の基礎設計図と玄関の鍵」**を作る作業のようです。家を建てる際、最も基礎となる骨組みと鍵は頑丈で信頼できる材料を使わなければ家族が安心して暮らせるように、コンピュータの最下層で動作するファームウェアは1%の欠陥や信頼できない要素もあってはなりません。

それでは、なぜ彼らは急にAIコードを禁止したのでしょうか？2026年10月15日に公開されたLibreboot 26.10バージョン（コード名：Ominous Olive）の最も破格な変更事項は、リポジトリに `AGENTS.md` というファイルを追加し、人工知能を使用したコード開発を厳格に禁止する政策を導入したことでした [[Source 9](https://freelamp.com/articles/2026-10-16_libreboot-2610-uefi-edk2-anti-ai-policy/), [Source 10](https://blog.desdelinux.net/en/libreboot-26-10-release-new-features-edk2-uefi-chromebooks/), [Source 11](https://www.livelianglove.cn/archives/tech-news-20261016-3)]。彼らが掲げた理由は大きく分けて3つありました。第一は**「信頼（Trust）」**、第二は**「開発者の技術退化（Skill degradation）」**、第三は**「著作権の不確実性（Copyright uncertainty、著作権の帰属や法的責任が不鮮明な問題）」**でした [[Source 11](https://www.livelianglove.cn/archives/tech-news-20261016-3)]。

ここで2つ目の比喩を挙げましょう。有名なシェフが集まって最高級の伝統料理を作る厨房を想像してみてください。シェフたちが自ら手で食材を整え、レシピを研究してこそ、料理のスキルが上がり味の深みが維持されます。しかし、もし自動調理ロボット（AI）が作った半製品を無分別に注ぎ込み始めたらどうなるでしょうか？料理の味と衛生（信頼）を保証できなくなり、シェフ自身が包丁の握り方を忘れてしまう（技術退化）だけでなく、そのレシピの原作者が誰なのか（著作権の不確実性）複雑に絡み合うことになります。Librebootの創始者はまさにこの点を深く懸念していたのです。

---

### 現在の状況：1ヶ月での方針転換と「スロップ削減政策」

しかし、世界は急速に変化しており、全面禁止という極端な錨を下ろしたまま巨大な技術の潮流に耐えることは困難でした。結局、Librebootは導入から1ヶ月後の2026年11月20日、その厳格だったAIコード貢献禁止政策を公式に撤廃しました [[Source 8](https://explainx.ai/blog/libreboot-drops-anti-ai-policy-slop-reduction-november-2026)]。

禁止令が消えたあとを埋めたのは、完全な無制限許可ではなく、新しい名前の**「スロップ削減政策（Slop Reduction Policy）」**でした [[Source 8](https://explainx.ai/blog/libreboot-drops-anti-ai-policy-slop-reduction-november-2026)]。ここで「スロップ（Slop）」とは、AIが無分別に吐き出し、品質が低く検証されていない粗悪なコードやコンテンツを指す業界用語です。つまり、AIの使用を無条件に厳禁するのではなく、「AIを使用するとしても、検証されていない不十分なコードがプロジェクトを汚染しないよう徹底的に監視および管理する」という現実的で柔軟な路線へと舵を切ったのです。

こうした変化は、開発者コミュニティの内外から大きな支持を受けました。技術の盲目的な拒絶ではなく、現実的な代替案と品質管理体制を通じて共生の道を模索し始めたことを意味するからです。

---

### 今後はどうなるのか？

Librebootの今回のハプニングと方針転換は、オープンソースコミュニティがAIに向き合う未来の姿を凝縮して示しています。AIを無条件に悪と規定して排斥することは、巨大な技術の波の前では持続可能ではありません。だからといって、何の検証もなしにAIコードを無分別に受け入れることは、システムの安定性とセキュリティを破壊する自殺行為になり得ます。

今後のオープンソースプロジェクトは、Librebootの「スロップ削減政策」のように、**「ツールとしてのAIの活用は認めつつ、その成果物に対する徹底した人間の監査と責任」**を求める方向にルールを洗練させていくでしょう。読者の皆様におかれましても、日常生活や業務で人工知能を活用される際、AIが出した成果物を妄信するのではなく、まるで綿密な編集者のように内容を検証し磨き上げる姿勢がより一層重要になる時代を迎えています。

---

### AIの視点

技術は常に人間のコントロール力と利便性の間で綱引きをします。Librebootの1ヶ月間の実験と修正は、AIが単に「禁止すべき対象」ではなく「賢明に飼いならすべきパートナー」であることを示す生々しい断面です。完全な統制でも、無分別な放任でもなく「徹底した検証と責任」という妥協点の上で、私たちはAIとともにさらに強固なデジタル未来を築いていくことでしょう。

---

## 参考資料

- [1] Libreboot- Wikipedia - [https://en.wikipedia.org/wiki/Libreboot](https://en.wikipedia.org/wiki/Libreboot)
- [2] Libreboot– Free and Open Source BIOS/UEFI boot firmware - [https://libreboot.org/](https://libreboot.org/)
- [3] Libreboot Drops Its Anti-AI Policy After One Month, Keeps ... - [https://explainx.ai/blog/libreboot-drops-anti-ai-policy-slop-reduction-november-2026](https://explainx.ai/blog/libreboot-drops-anti-ai-policy-slop-reduction-november-2026)
- [4] Libreboot 26.10 把「反 AI 政策」列为本次发布最重要的变更，然后才... - [https://freelamp.com/articles/2026-10-16_libreboot-2610-uefi-edk2-anti-ai-policy/](https://freelamp.com/articles/2026-10-16_libreboot-2610-uefi-edk2-anti-ai-policy/)
- [5] Libreboot 26.10: UEFI support with EDK2, Chromebooks, and ... - [https://blog.desdelinux.net/en/libreboot-26-10-release-new-features-edk2-uefi-chromebooks/](https://blog.desdelinux.net/en/libreboot-26-10-release-new-features-edk2-uefi-chromebooks/)
- [6] Libreboot 26.10 带来完整 UEFI 支持，同时立了一条反 AI 的规矩 - [https://www.livelianglove.cn/archives/tech-news-20261016-3](https://www.livelianglove.cn/archives/tech-news-20261016-3)