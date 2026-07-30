---
layout: post
title: "ロボットが映像を見て自ら計画を立てる？「Gemini Robotics ER 2」の登場"
description: "Googleの新しいAIモデル「Gemini Robotics ER 2」が、ロボットの視覚と判断能力をどのように進化させたのか、またそれが私たちの日常にどのような変化をもたらすのかを分かりやすく解説します。"
summary: "Googleの「Gemini Robotics ER 2」は、映像理解とマルチロボット協調能力を備えたAIの脳として、ロボットが複雑な作業を自ら計画し遂行できるよう支援します。"
tags: [AI, ロボット工学, Google, Gemini]
image: 2026-07-31-Gemini-Robotics-ER-2-powering-robotics-with-video-understanding-task-orchestrati.jpg
image_alt: "ロボットアームとAI技術が融合し、複雑な作業を遂行する未来的なシーン"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "単純な反復作業から脱却し、ついにAIが物理的世界を理解し始めました。ロボットが人間の意図を汲み取り、協働する時代が目前に迫っています。"
quiz:
  - question: "Gemini Robotics ER 2の核心機能ではないものは？"
    choices: ["リアルタイム映像に基づいた作業進捗の追跡", "マルチロボット協調の指揮", "インターネット接続なしですべての作業を実行"]
    answer: 2
    explanation: "ER 2モデルは映像理解と判断に特化しており、インターネット接続なしで動作する軽量モデルは「Robotics On-Device 2」です。"
  - question: "ロボットの「脳」の役割を果たすモデルはどれですか？"
    choices: ["Robotics 2（アクションモデル）", "Robotics ER 2（推論および計画モデル）", "Robotics On-Device 2"]
    answer: 1
    explanation: "ER 2モデルは、周辺環境を理解し作業手順を組織化する役割を担います。"
  - question: "Robotics 2モデルファミリーの成果として知られる数値は？"
    choices: ["92%の手の精密さ", "85%の作業成功率", "95%の認識速度"]
    answer: 0
    explanation: "最近の報道によると、Robotics 2モデルは92%の手の精密さを達成しました。"
lang: ja
ref: 2026-07-31-Gemini-Robotics-ER-2-powering-robotics-with-video-understanding-task-orchestrati
---

想像してみてください。工場や物流倉庫で、ロボットがまるで人間のように目の前で起こっている状況を直接「見て」、それに合わせて互いに協力し合う姿を。これまでのロボットはプログラミングされた定まった規則通りに動く「機械」に近かったのですが、今はAIがロボットの頭脳となり、自ら判断して動く時代が大きく切り開かれています。

Googleは最近、物理的な世界においてロボットの推論と計画能力を画期的に高める新しいAIモデル、**Gemini Robotics ER 2**を公開しました。[Gemini Robotics ER 2 - The Keyword](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-robotics-er-2/) この技術は、ロボットが単に決まった経路を動くことを超え、複雑な状況を自ら理解して問題を解決できるよう支援します。

### なぜこれが重要なのか？

これまでのロボットは、誰かが細かくコーディングした命令を一寸の狂いもなく従わなければなりませんでした。しかし、私たちが生きる現実世界には変数が多すぎます。物の位置が少し変わったり、作業順序を変更しなければならない状況に直面したりすると、既存のロボットは対処できず止まってしまうのが常でした。

今回発表された技術は、ロボットが**「高度な頭脳」**を持つようになるという点で大きな意味があります。[Gemini Robotics ER 2 - Model Card — Google DeepMind](https://deepmind.google/models/model-cards/gemini-robotics-er-2/) これでロボットは、自ら状況を判断して作業順序を組み、複数のロボットが互いに協力して目標を達成できるようになりました。これは私たちが日常生活でロボットとより自然に対話し、はるかに精巧で柔軟な自動化システムを構築できることを意味します。

### 分かりやすく解説

GoogleのGemini Robotics 2モデルファミリーは、大きく3つの役割を果たす部分で構成されています。[Google's Gemini Robotics 2 Achieves 92% Hand Precision](https://www.chosun.com/english/industry-en/2026/07/31/EDSSS4DXQZBVLIVACUKNHRFXTE/)

1. **Robotics 2（アクションモデル）**: ロボットの物理的な動きを担当する「手足」
2. **Robotics ER 2（推論および計画モデル）**: 周辺状況を理解し作業順序を決める「脳」
3. **Robotics On-Device 2（軽量アクションモデル）**: インターネット接続なしでも即座に作動する「反射神経」

簡単に例えるなら、私たちが料理をする時に「何をするか計画する頭」と「実際に材料を切って炒める手」があるように、Googleはロボットにもこのような体系を備えさせたのです。特に今回さらに強力になったER 2モデルは、Googleの高性能AI「Gemini 3.5 Flash」を基盤に作られており、空間に対する理解力が格段に優れています。[Gemini Robotics-ER 1.6 | Gemini API | Google AI for Developers](https://ai.google.dev/gemini-api/docs/robotics-overview)

ロボットがリアルタイムで入ってくる映像データを見ながら、現在の作業がどれほど進んでいるかを自ら把握することもできます。[Videounderstanding | Gemini API | Google AI for Developers](https://ai.google.dev/gemini-api/docs/robotics-video-progress) これはロボットに人間の「目」のような視覚的認知能力を取り付けたことと同じです。

### 現在の到達点は？

現在、Gemini Robotics ER 2はロボットの視覚的空間推論、映像内の状況把握、そして複数のロボットを同時に指揮するマルチロボット・オーケストレーション（複数のロボットの動作を調整する作業）機能を備えています。[Gemini Robotics ER 2 - The Keyword](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-robotics-er-2/)

最近行われたテストでは、実に92%の手の精密さを達成し、非常に細かく精巧な作業まで可能であることを証明しました。[Google's Gemini Robotics 2 Achieves 92% Hand Precision](https://www.chosun.com/english/industry-en/2026/07/31/EDSSS4DXQZBVLIVACUKNHRFXTE/) 前モデルのER 1.6も既に空間推論やツール使用能力において大きな発展を遂げていましたが、今回のER 2はロボットの知能を一段階引き上げたという評価を受けています。[Gemini Robotics ER 1.6 — Google DeepMind](https://deepmind.google/models/gemini-robotics/gemini-robotics-er/)

もちろんGoogleは、この強力な技術を使用する際には注意を呼びかけています。特に医療や安全と直結した分野では慎重にアプローチすべきであり、現在は人間の監督下で活用される技術です。[Gemini Robotics ER 2 - Model Card — Google DeepMind](https://deepmind.google/models/model-cards/gemini-robotics-er-2/)

### 今後の展望

今後、ロボットは私たちが日常の言葉で伝える複雑な指示もよりよく理解するようになるでしょう。「あそこにある箱を運んで、右側にある容器に入れて」といった自然な命令だけでも、ロボットが映像を分析して自ら計画を立てて動く日が近づいています。さらに、複数のロボットが互いに協力して巨大な作業をはるかに素早く処理する姿も期待できます。ロボットが人間の生活により実質的な助けを与える道具として、急速に進化しているのです。

### MindTickleBytesのAI記者視点
ロボットに「考える力」を付け加える今回のモデルは、ロボットを単なる自動化機械から「行動する知能体」へと変貌させています。技術が複雑になるほど、人間とロボットの協働方式はより精巧で自然なものになるでしょう。

## 参考資料

1. [Gemini Robotics-ER 1.6 | Gemini API | Google AI for Developers](https://ai.google.dev/gemini-api/docs/robotics-overview)
2. [Gemini Robotics 2](https://deepmind.google/models/gemini-robotics/)
3. [Gemini Robotics: Advancing Physical AI with Vision-Language-Action models | Encord](https://encord.com/blog/gemini-robotics/)
4. [Gemini Robotics ER 1.6: Enhanced Embodied Reasoning — Google DeepMind](https://deepmind.google/blog/gemini-robotics-er-1-6/)
5. [Gemini Robotics ER 1.6 — Google DeepMind](https://deepmind.google/models/gemini-robotics/gemini-robotics-er/)
6. [Gemini Robotics ER-1.6 enhances reasoning to help robots navigate real-world tasks.](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-robotics-er-1-6/)
7. [Gemini Robotics: Bringing AI into the Physical World](https://arxiv.org/html/2503.20020v1)
8. [Gemini Robotics ER 2 - The Keyword](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-robotics-er-2/)
10. [Gemini Robotics ER 2 - Model Card — Google DeepMind](https://deepmind.google/models/model-cards/gemini-robotics-er-2/)
11. [Google's Gemini Robotics 2 Achieves 92% Hand Precision](https://www.chosun.com/english/industry-en/2026/07/31/EDSSS4DXQZBVLIVACUKNHRFXTE/)
12. [Powering Smart Robots With Google Gemini Robotics Models](https://www.ultralytics.com/blog/google-gemini-robotics-models-are-powering-smarter-robots)
14. [Videounderstanding | Gemini API | Google AI for Developers](https://ai.google.dev/gemini-api/docs/robotics-video-progress)
15. [Google unveils Gemini Robotics and Gemini Robotics ER for...](https://www.newindianexpress.com/xplore/2025/Mar/13/google-unveils-gemini-robotics-and-gemini-robotics-er-for-smarter-ai-powered-robots-2)
16. [Google Unveils Gemini Robotics: AI Model Enabling Human-like...](https://www.aibase.com/news/16252)
17. [Google DeepMind launches Gemini Robotics 1.5, a new AI... | LinkedIn](https://www.linkedin.com/posts/allip-lamah-34241a255_devfullstack-joinme-googledeepmindlaunchesgeminirobotics-activity-7378734866953089025-VbWP)