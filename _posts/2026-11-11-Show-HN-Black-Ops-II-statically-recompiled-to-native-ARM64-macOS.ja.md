---
layout: post
title: "私のMacでコール オブ デューティ？「静的再コンパイル」がもたらすゲームの復活"
description: "エミュレータなしで最新のMac（macOS）でコール オブ デューティ ブラックオプス 2をネイティブ実行する技術、「静的再コンパイル」について解説します。"
summary: "昔のゲームコードを最新機器の言語へと直接翻訳する「静的再コンパイル」技術により、コール オブ デューティ ブラックオプス 2などの不朽の名作ゲームが、最新のMacでネイティブ速度で動作し始めました。"
tags: [AI, ゲーム, 技術, Mac, コールオブデューティ]
image: 2026-11-11-Show-HN-Black-Ops-II-statically-recompiled-to-native-ARM64-macOS.jpg
image_alt: "最新のMacBookでコール オブ デューティ ブラックオプス 2が動作している様子"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "エミュレーションの限界を超え、コードを直接翻訳する静的再コンパイル技術は、ゲーム保存の新たなマイルストーンとなるでしょう。過去の遺産が現代のハードウェア性能を存分に活用できるようになった点は驚きです。"
quiz:
  - question: "静的再コンパイルの最大の利点は何ですか？"
    choices: ["非常に高速なエミュレータ動作", "エミュレータなしでネイティブ性能を実現", "クラウドゲームストリーミング"]
    answer: 1
    explanation: "静的再コンパイルはゲームコードを最新機器の言語に直接変換するため、別途エミュレータは不要です。"
  - question: "最近Mac（macOS）向けに再コンパイルされたゲームは何ですか？"
    choices: ["コール オブ デューティ：ブラックオプス 2", "バトルフィールド 2042", "サイバーパンク 2077"]
    answer: 0
    explanation: "最近、開発者のadrbn氏によってブラックオプス 2がARM64 Mac向けに静的再コンパイルされました。"
  - question: "静的再コンパイルはどのような仕組みで動作しますか？"
    choices: ["インターネットによるリアルタイム変換", "既存のゲームコードを最新機器の命令セットに変換", "グラフィックのみを修正"]
    answer: 1
    explanation: "既存のゲームの機械語コードを、新しいハードウェア（例：ARM64）で直接実行可能な命令へと翻訳する方式です。"
lang: ja
ref: 2026-11-11-Show-HN-Black-Ops-II-statically-recompiled-to-native-ARM64-macOS
---

想像してみてください。2020年モデルのMacBook Proを開き、10年以上前の名作『コール オブ デューティ：ブラックオプス 2』のアイコンをクリックします。普通なら複雑なエミュレータや仮想マシンを起動させるため、コンピュータが熱くなったり動作が重くなったりするはずです。しかし、このゲームはまるで昨日発売されたかのようにスムーズに、しかもほぼ60フレームで画面に広がります。

最近開発者コミュニティで注目されている「静的再コンパイル（Static Recompilation）」という技術のおかげで、このようなことが可能になりました。ゲームの歴史が現代の最先端ハードウェアと出会い、新たな命を吹き込まれているのです。

## なぜこれが重要なのか？（Why It Matters）

私たちが楽しむ古典的なゲームは、通常、その時代のハードウェア（例えば旧式のPCやコンソール）に合わせて作られています。時が経ち機器が老朽化すると、これらのゲームは歴史の中に消えてしまう危機に瀕します。これまでこれを動かすために「エミュレータ」という技術が使われてきました。エミュレータは、外国語を通訳する通訳者のように、古いゲームの言語を最新のコンピュータが理解できるようにリアルタイムで変換します。しかし、この過程でかなりの性能ロスが発生し、時にはグラフィックが崩れたり音が遅れたりする問題が生じます。

静的再コンパイルは違います。これは通訳者を介するのではなく、ゲームの言語そのものを最新機器の言語へと完全に書き換えてしまう作業です。これにより、エミュレータなしでも最新機器で「ネイティブ」に、つまりその機器のために作られたゲームのように完璧な性能で動作します。もう私たちは、過去の名作を古い機器に閉じ込めておく必要はありません。

## わかりやすい例え（The Explainer）

このように例えてみましょう。皆さんが書いた韓国語の手紙を英語圏の友人に送るとします。

*   **エミュレータ方式:** 皆さんが英語圏の友人の横で、リアルタイムで韓国語を英語に同時通訳するのと同じです。皆さんの通訳速度が友人の理解速度に追いつかなかったり、誤訳が生じたりすると会話が噛み合わなくなります。
*   **静的再コンパイル方式:** 手紙を送る前に、専門の翻訳家が完璧な英語に完全に書き直してから送るのと同じです。友人は、原本が韓国語だったとは気づかないほど非常に自然に内容を理解し、楽しむことができます。

今回Mac（macOS）で動作した[『コール オブ デューティ：ブラックオプス 2』](https://github.com/adrbn/bo2-mac)の事例を見ると、開発者はゲームの32ビットx86（旧式PC言語）コードを「Remill」というツールを使用して「LLVM IR（中間言語）」に変換した後、最新Macの脳であるARM64（Appleシリコン）命令へと移植しました。さらに、当時のWindowsグラフィック呼び出し方式（Direct3D 11）を最新Macのグラフィック標準である「メタル（Metal）」に置き換える作業を直接処理しました。そのおかげで[ほぼ60フレーム](https://github.com/adrbn/bo2-mac)という驚異的なパフォーマンスが可能になったのです。

## 現在の状況（Where We Stand）

すでにこの技術は、ゲーム業界の巨大な流れになりつつあります。ブラックオプス 2だけでなく、[『マックス・ペイン 3』](https://www.youtube.com/watch?v=CGYbWKSA5QU)はPS5で60フレームで動作しており、[『忍者龍剣伝 ブラック』](https://portedgames.com/recompiled-games/)、[『ゴッド・オブ・ウォー』](https://recomplauncher.com/game/gow-native-pc)、[『ボンバーマン64』](https://recompsoftware.com/games/)、[『Halo: CE』](https://recompsoftware.com/games/)、[『ランページ』](https://quiverlauncher.com/apps/rampage-recompiled)、[『ファイナルファンタジーVII』](https://andreyvelsk.github.io/GAFT/project/ff7recomp/)など、数多くの名作がそれぞれの最新機器用ポートとして生まれ変わっています。

ただし、完璧ではありません。ブラックオプス 2の場合でも、[一部の発熱問題](https://github.com/adrbn/bo2-mac)が依然として解決課題として残っています。また、静的再コンパイルはゲームごとにいちいちコードを分析して変換しなければならないため、大量生産が可能な技術ではありません。

## 今後の展望（What's Next）

今後「静的再コンパイル」は、ゲーム保存の中核標準になる見通しです。開発者たちはブラックオプス 2プロジェクトにおいて[画面分割やLANモード](https://github.com/adrbn/bo2-mac)などの機能を追加するなど、原作を超えた拡張まで目指しています。

個人が所有するゲームファイルを最新機器で何の制約もなく動かせるようにするこの技術は、巨大ゲーム会社の複雑なリマスターコストやエミュレーションの技術的限界を一気に突破する強力なツールです。いつの日か、私たちが今日買った最新ゲームも20年後、再び静的再コンパイルを通じて完璧に動作する日が来るでしょう。

## 参考資料

1. [Show HN: Black Ops II statically recompiled to native ARM64 macOS](https://github.com/adrbn/bo2-mac)
2. [Max Payne 3 Running NATIVELY on PS5 at 60 FPS... - YouTube](https://www.youtube.com/watch?v=CGYbWKSA5QU)
3. [Recompiled Games List: Every Native PC Port... | PortedGames](https://portedgames.com/recompiled-games/)
4. [God of War Native PC — PC recomp of God of War · RecompLauncher](https://recomplauncher.com/game/gow-native-pc)
5. [Decompiled & recompiled games · Recomp](https://recompsoftware.com/games/)
6. [Rampage Recompiled – Rampage: World Tour Recomp | Quiver](https://quiverlauncher.com/apps/rampage-recompiled)
7. [Call of Duty: Black Ops II - recomp.party](https://recomp.party/p/adrbn/bo2-mac/)
8. [bo2-mac: Call of Duty: Black Ops II PC recomp, source ...](https://recompsoftware.com/p/bo2-mac/)
9. [Black Ops II Recompiled — PC recomp of Call of Duty: Black ...](https://recomplauncher.com/game/bo2-mac?lang=en-GB)
10. [bo2-recompiled: Call of Duty: Black Ops II recompilation ...](https://recomp.gg/p/bo2-recompiled)
11. [FF7 Recomp | Games & Apps for AYN Thor](https://andreyvelsk.github.io/GAFT/project/ff7recomp/)