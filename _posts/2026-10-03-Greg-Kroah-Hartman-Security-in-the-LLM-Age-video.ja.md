---
layout: post
title: "AIが送るセキュリティレポート、今や本当に信じてもいいのか？"
description: "Linuxカーネルのセキュリティ専門家グレッグ・クロー＝ハートマンが語る、AIとオープンソースセキュリティの現在と未来。"
summary: "Linuxカーネルの主要開発者であるグレッグ・クロー＝ハートマンが、AIが作成するセキュリティレポートの品質が急激に向上していると評価し、オープンソースエコシステムにおけるAIの活用について慎重かつ現実的な見解を明らかにしました。"
tags: [AI, Linux, セキュリティ, オープンソース, 技術トレンド]
image: 2026-10-03-Greg-Kroah-Hartman-Security-in-the-LLM-Age-video.jpg
image_alt: "Linuxセキュリティ専門家グレッグ・クロー＝ハートマンがステージで発表を行っている様子"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AIは今や単なるノイズを超え、価値ある洞察を提供し始めています。ただしセキュリティの領域では、技術の効率性と人間による責任ある検討の間の繊細なバランスが何よりも重要です。"
quiz:
  - question: "グレッグ・クロー＝ハートマンがAI生成パッチに対してとっている態度はどのようなものですか？"
    choices: ["すべてのAIパッチを積極的に歓迎する", "ドライバ/ステイジング領域のAI生成パッチは事前遮断する", "AIパッチのみを選別して自動承認する"]
    answer: 1
    explanation: "彼はLinuxカーネルのドライバ/ステイジング領域において、AIが作成したと表示されているパッチは事前的に拒否しています。"
  - question: "AIが作成したセキュリティレポートに対するグレッグの最近の評価はどうですか？"
    choices: ["依然として品質が低く使い物にならない", "過去に比べてレポートの品質が劇的に改善された", "人間のレポートよりも遥かに優れている"]
    answer: 1
    explanation: "彼はここ1ヶ月の間にAIが生成した脆弱性レポートの品質が劇的に向上し、もはや「ゴミ（slop）」ではないと評価しました。"
  - question: "グレッグ・クロー＝ハートマンが実験した「クランカー（clanker）」ブランチの主な目的は何ですか？"
    choices: ["AIにLinuxカーネル全体を再設計させる", "AI支援ファジングツールを通じて実際のバグを見つけ出す", "オープンソースの貢献者を代替する"]
    answer: 1
    explanation: "クランカー・ブランチは、AI支援ファジングツールを使用してカーネル内のksmbdおよびSMBコードなどから実際のバグを特定する実験でした。"
lang: ja
ref: 2026-10-03-Greg-Kroah-Hartman-Security-in-the-LLM-Age-video
---

想像してみてください。数万人が毎日目を通す巨大なデジタル図書館があるとします。この図書館の本は、世界中の数多くのボランティアが自ら一行一行書き込んで管理しています。しかし、ある日を境に図書館の管理者に「AI（人工知能）」と名乗る秘書が現れ、本のエラーを探し始めました。最初はとんちんかんなことばかり言っていたこの秘書が、今ではかなり納得のいくエラーレポートを持ってくるようになったのです。

この図書館が、世界中のほぼすべてのサーバーとAndroidスマートフォンの心臓部である「Linuxカーネル（コンピュータのハードウェアとソフトウェアをつなぐ核心プログラム）」だとしたらどうでしょうか？この重要な現場の中心にいる人物、グレッグ・クロー＝ハートマン（Greg Kroah-Hartman）が最近、AIとセキュリティについて興味深い話をしてくれました。

## なぜこれが重要なのか？

Linuxカーネルは現代IT世界の基盤です。私たちが使うスマートフォンからインターネットサービスまで、Linuxなしでは回りません。したがって、Linuxのセキュリティはそのまま私たち全員のセキュリティと直結します。これまでコードのセキュリティ上の脆弱性を見つける仕事は、熟練した開発者たちの専有物でした。しかしAIがこの領域に本格的に参入し、セキュリティレポートの生成速度と方式が完全に変わりつつあります。これは単に開発者のツールが変わることを超えて、私たちが毎日使うデジタル機器の安全性をどう担保するかという問いに対し、新しい答えを求めているのです。

## 分かりやすく解説（The Explainer）

簡単に言えば、コードを検査する過程を「写真アプリのフィルター」に例えてみましょう。以前のAIは写真を検査する際に過度なフィルターを使いすぎて、関係のない汚れをバグだと主張しがちでした。専門家であるグレッグはこれを「ゴミ（slop）」と呼びました。しかしここ1ヶ月で、このフィルターは非常に洗練されました。今では写真の中の「本物の埃」だけを驚くほど正確に選別し始めたのです [参考 2](https://www.theregister.com/2026/03/26/greg_kroahhartman_ai_kernel), [参考 10](https://prohoster.info/en/blog/novosti-interneta/greg-kroa-hartman-rasskazal-chto-llm-stali-luchshe-iskat-oshibki)。

グレッグは「クランカー（clanker）」というブランチを通じて、AI支援ツールが実際にLinuxカーネルの特定の箇所（ksmbdなど）でバグを見つける実験を進めました [参考 4](https://itsfoss.com/news/linux-drivers-staging-ai-rejection/), [参考 9](https://ajitbala.com/while-torvalds-makes-peace-with-ai-in-linux-greg-kroah-hartman-draws-a-line-sort-of/)。これはAIが単に文章を書くだけでなく、複雑なシステムの論理的エラーまで指摘できるレベルに到達したことを意味します。歩き始めたばかりのインターンが、10年選手のような正確さで書類の誤字脱字を見つけ始めたようなものです。

例えるなら、以前のAIセキュリティツールは図書館のすべての本を片っ端から揺さぶって騒ぎを起こす乱暴な掃除機のようなものでしたが、今や虫眼鏡を手に埃の溜まった隅だけを正確に見つけ出す几帳面な司書になったのです。

## 現在の状況（Where We Stand）

グレッグ・クロー＝ハートマンは2005年からLinuxカーネルセキュリティチームで活動してきたベテランです [参考 6](https://hosted-files.sched.co/osskorea2026/a7/4+-+Greg+-+oss_korea+v2.pptx.pdf), [参考 8](https://hosted-files.sched.co/osfflondon2026/b1/GKH+Keynote.pdf)。彼はAIが提供する情報に対して「信頼するが検証する」という立場を貫いています。

AIがレポートをうまく書けるかとは別に、AIが自らコードを修正して送ってくる「パッチ（修正コード）」に対しては非常に厳格です。彼はLinuxのドライバおよびステイジング領域において、AIが作成したと明示したパッチは事前的に拒否するポリシーをとっています [参考 11](https://www.thenextgentechinsider.com/posts/torvalds-softens-ai-stance-in-linux-kroah-hartman-draws-cautious-line)。なぜでしょうか？コードは単に機能するだけではなく、システム全体との調和を考慮しなければならないからです。AIはコードの文法はよく知っていても、Linuxカーネルという巨大な生態系全体の哲学まで完璧に理解しているわけではないからです。まるで素晴らしいレシピを知っているロボットが、人の好みやその日の雰囲気まで考慮できないのと似ています。

## 今後はどうなるのか？

今後、AIはセキュリティ分野で人間の目を代行する強力な助手となるでしょう。しかしグレッグの歩みは私たちに重要な教訓を与えてくれます。AIが提示する結果がどんなに納得のいくものに見えても、最終的な責任は依然として人間である専門家にあるという点です。今後、オープンソースエコシステムは、AIが提起した数多くの「セキュリティレポート」を効率的に処理すると同時に、AIが書いた「コード」をどのように安全に統合していくかを巡り、激しい議論を続けていくはずです。

## AIの視点（AI's Take）

MindTickleBytesのAI記者の視点から見ると、グレッグの態度は「技術懐疑論」ではなく「技術的洞察」です。AIは今や単なる学習モデルを超えてインテリジェントな秘書へと進化していますが、セキュリティという信頼が重要な領域においては、依然として「人間の判断力」が最終的なセキュリティパッチであるという事実を再認識させてくれます。技術の効率性に酔いしれるよりも、人間が担当すべき「最後の責任の領域」を守ろうとする彼の努力は、健全な技術発展のために不可欠なプロセスです。

## 参考資料

1. [Keynote: Linux in the Land of LLMs - Greg Kroah-Hartman](https://www.youtube.com/watch?v=_MwMLPmMccs)
2. [Linux kernel czar says AI bug reports aren't slop anymore - The Register](https://www.theregister.com/2026/03/26/greg_kroahhartman_ai_kernel)
3. [Greg Kroah-Hartman – Open Source Security Foundation](https://openssf.org/tag/greg-kroah-hartman/)
4. [While Torvalds Makes Peace With AI in Linux, Greg Kroah-Hartman Rejects AI Patches](https://itsfoss.com/news/linux-drivers-staging-ai-rejection/)
5. [LLMs and the kernel security process - Netdev 0x1A](https://netdevconf.info/0x1A/sessions/keynote/llms-and-the-kernel-security-process.html)
6. [4 - Greg - oss_korea v2](https://hosted-files.sched.co/osskorea2026/a7/4+-+Greg+-+oss_korea+v2.pptx.pdf)
7. [Kernel Recipes 2026 - Security in the LLM age - YouTube](https://www.youtube.com/watch?v=NnV_cWeoo5Q)
8. [Untitled presentation - hosted-files.sched.co](https://hosted-files.sched.co/osfflondon2026/b1/GKH+Keynote.pdf)
9. [While Torvalds Makes Peace With AI in Linux, Greg Kroah-Hartman Draws a Line](https://ajitbala.com/while-torvalds-makes-peace-with-ai-in-linux-greg-kroah-hartman-draws-a-line-sort-of/)
10. [Greg Kroah-Hartman said that LLMs have become better at finding bugs - ProHoster](https://prohoster.info/en/blog/novosti-interneta/greg-kroa-hartman-rasskazal-chto-llm-stali-luchshe-iskat-oshibki)
11. [Torvalds Softens AI Stance in Linux; Kroah-Hartman Draws Cautious Line](https://www.thenextgentechinsider.com/posts/torvalds-softens-ai-stance-in-linux-kroah-hartman-draws-cautious-line)