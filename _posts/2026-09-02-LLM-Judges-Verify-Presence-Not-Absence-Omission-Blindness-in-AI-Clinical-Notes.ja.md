---
layout: post
title: "AI医師が作成した診療記録、本当に信頼できるのか？「欠落した情報」を見抜けないAIの盲点"
description: "AIが作成した診療記録の正確性を評価する「AI審判員」が、なぜ情報の欠落をうまく検知できないのか。その理由と限界を探ります。"
summary: "AI診療記録アシスタントが作成する文書では、重要な情報が抜け落ちる「欠落（Omission）」エラーが頻発しています。しかし、それを評価するAI審判員たちは「存在する情報」の確認には長けていても、「欠落した情報」を見つけ出すことには限界があることが明らかになりました。"
tags: [AI, 医療AI, 診療記録, LLM, 技術分析]
image: 2026-09-02-LLM-Judges-Verify-Presence-Not-Absence-Omission-Blindness-in-AI-Clinical-Notes.jpg
image_alt: "AIが作成した診療記録書類を虫眼鏡で覗き込む様子。AIの評価能力を象徴的に示しています。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AIの評価能力を盲信するのは危険です。『存在』と『不在』を区別することは、全く異なる次元の知能であることを認識しなければなりません。"
quiz:
  - question: "研究結果によると、AI審判員が最も見つけやすいエラーのタイプは何ですか？"
    choices: ["情報の欠落（Omission）", "幻覚（Hallucination）", "存在する情報の確認"]
    answer: 2
    explanation: "AI審判員は記録に含まれる情報を確認する『存在』の把握には優れていますが、欠落した情報を見つける『不在』の把握には困難を抱えています。"
  - question: "診療記録アシスタントAIが作成する文書で最も頻繁に発生するエラーは何ですか？"
    choices: ["情報の欠落（Omission）", "幻覚（Hallucination）", "誤字脱字"]
    answer: 0
    explanation: "アンビエントAI（Ambient AI）が作成する診療記録において最も支配的なエラーは、重要な情報が記録されない欠落エラーです。"
  - question: "AI審判員（LLM-as-a-judge）が情報の欠落を検知する際の性能はどの程度ですか？"
    choices: ["人間レベル", "非常に優れている", "ランダムな確率と同等（Chance levels）"]
    answer: 2
    explanation: "研究によると、情報の不在を見つける際のAI審判員の性能は、ランダムに当てるのと同等レベルであることが分かりました。"
lang: ja
ref: 2026-09-02-LLM-Judges-Verify-Presence-Not-Absence-Omission-Blindness-in-AI-Clinical-Notes
---

想像してみてください。病院を訪れ、医師と真剣な相談をしました。診療が終わった後、AIアシスタントがあなたの診療記録を代わりに作成してくれました。入念に読んでみると、医師が話した内容がかなりうまく整理されているようで安心します。しかし、もし昨日から始まった胸の痛みという決定的な情報がすっかり抜け落ちていたらどうでしょうか？この不完全な記録を基に処方箋を受け取ったとしたら、果たして安全でしょうか。

近年、医療現場では医師と患者の対話を聞き取り、自動で診療記録の下書きを作成してくれる「アンビエントAI（Ambient AI、診療現場記録アシスタント）」の導入が増えています。利便性は高いものの、記録から重要な情報が意図せず省略される「欠落（Omission）」エラーは、依然として解決すべき大きな課題です。[出典 12](https://arxiv.org/abs/2608.31016) 今日は、この問題を解決するために導入された「AI審判員」がなぜ思ったほど賢くないのか、その理由と限界を分かりやすく解説します。

## なぜこれが重要なのか？

医療現場において診療記録は、患者の健康を守るための最も基本的かつ核心的なデータです。記録に重要な症状が欠落していると、医師が誤診を下したり、処方が不適切になったりするリスクがあります。これを防ぐために、人間の代わりにAIを審判員（LLM-as-a-Judge）として立て、記録を検査させています。[出典 10](https://www.linkedin.com/posts/catherine-chen-5851a6a0_continual-monitoring-of-note-quality-at-scale-activity-7496283957693448192-ksR_)

しかし、もしこの「AI審判員」でさえも欠落した情報を正しく見つけ出せないとしたらどうでしょうか？医療事故のリスクは依然として残り、私たちが使用するAIアシスタントが実は「穴だらけの記録」を作っているにもかかわらず、それを評価するシステムすらその穴を発見できないという深刻な状況に陥ることになります。

## 分かりやすく理解する：「正解」がない試験の採点

AI審判員がなぜ欠落した情報を探せないのか、「試験の採点」状況に例えて説明します。

AI審判員を「正解を持って学生の答案を採点する教師」だと考えてみてください。

*   **存在確認（Presence）：** 学生が答案用紙に「1番の答えはAだ」と書いたか確認するのは非常に簡単です。答案に『A』という文字が明確に見えるからです。AIはそのように、特定のキーワードが記録に含まれているかを確認する能力は非常に優れています。[出典 2](https://arxiv.org/pdf/2608.31016)
*   **不在確認（Absence）：** 一方で、教師が「この学生が答案用紙に書くべき内容を書き漏らしていないか？」を確認するのは次元の違う問題です。学生が書かなかった内容を見つけ出すには、頭の中に正解のすべてを完璧に浮かべ、答案のすべての行と照らし合わせなければならないからです。

最近実施された「OmissionBench」プロジェクトによると、AI審判員は記録に「何が含まれているか」は強力に確認しますが、「何が抜けているか」を見つけ出すには、ほぼランダムに推測するレベル（chance levels）の性能しか発揮できませんでした。[出典 3](https://github.com/composo-ai/omission-bench), [出典 13](https://arxiv.org/html/2608.31016v1) つまり、AIは記録が含む「結果」のみを見ており、記録されていない「空白」を認識する能力が著しく不足しているのです。学界ではこれを「欠落の盲点（Omission Blindness）」と呼んでいます。

## 現在の状況はどうなっているか？

すでに多くの医療AIシステムが診療記録の品質を評価するためにAI審判員を活用しています。[出典 10](https://www.linkedin.com/posts/catherine-chen-5851a6a0_continual-monitoring-of-note-quality-at-scale-activity-7496283957693448192-ksR_) しかし、現実的な性能は冷厳です。研究結果によると、実際にAIが作成した診療記録の約3.45%は情報の欠落エラーを含んでいます（幻覚エラーは1.47%）。[出典 18](https://www.nature.com/articles/s41746-025-01670-7)

問題は、こうした欠落をフィルタリングすべきAI審判員たちが「存在」のみを見て「不在」を見ることができないという点です。[出典 2](https://arxiv.org/pdf/2608.31016) さらに、評価を担当するAIが、検査対象の記録を作ったAIと似た思考パターンを持っており、同じエラーを繰り返したり、そのまま見過ごしたりすることもあります。[出典 4](https://www.youtube.com/watch?v=BPXFDC7WHSk)

## 今後はどうなるか？

AI審判員の限界が明らかになるにつれ、業界ではこれを克服するための多角的な試みが行われています。

1.  **決定論的検証ツールの導入：** AIの判断のみに依存せず、必須キーワードチェックのような、シンプルで確実なコード化されたルールを併用する方式です。[出典 4](https://www.youtube.com/watch?v=BPXFDC7WHSk)
2.  **多重評価体制：** 一人のAI審判員ではなく、複数のモデルやマルチエージェントシステムを活用し、情報を相互にクロスチェックするシステムを構築しています。[出典 14](https://www.nature.com/articles/s41746-025-02005-2)
3.  **人間の参加：** 結局のところ、安全が最優先される医療分野では、AIがすべてを評価するのではなく、人間の専門家である医師がAIの検討結果を最終的に確認する「人間中心の評価」が依然として最も重要な核となります。[出典 17](https://arxiv.org/html/2607.18828)

私たちは今、AIが「何ができるのか」を超えて、「何を逃しているのか」を慎重に見極めるべき時点に立っています。

## MindTickleBytesのAI記者からの視点

AIを審判員に据えるのは便利ですが、『存在』と『不在』を区別することは知能の全く異なる次元の話です。記録されない『沈黙』を読み取れないAIに私たちの健康を完全に任せるには、まだ長い道のりが必要です。

## 参考資料
1. [2608.31016] LLM Judges Verify Presence, Not Absence: Omission Blindness in AI Clinical Notes and What Recovers It (https://arxiv.org/abs/2608.31016)
2. LLM Judges Verify Presence, Not Absence: Omission Blindness in AI Clinical Notes and What Recovers It (https://arxiv.org/pdf/2608.31016)
3. GitHub - composo-ai/omission-bench: OmissionBench harness: code (https://github.com/composo-ai/omission-bench)
4. Replace Your LLM Judge With 10 Lines of pytest - YouTube (https://www.youtube.com/watch?v=BPXFDC7WHSk)
5. LLM-as-a-judge: a complete guide to using LLMs for evaluations (https://www.evidentlyai.com/llm-guide/llm-as-a-judge)
7. LLM-as-a-Judge Simply Explained: The Complete Guide (https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method)
8. Position Bias in LLM Judges: Measurement and Mitigation (https://mbrenndoerfer.com/writing/position-bias-in-llm-judges)
9. LLMs bow to pressure, changing answers when challenged (https://www.computerworld.com/article/4023989/llms-bow-to-pressure-changing-answers-when-challenged-deepmind-study.html)
10. Continual Monitoring of Note Quality At Scale (https://www.linkedin.com/posts/catherine-chen-5851a6a0_continual-monitoring-of-note-quality-at-scale-activity-7496283957693448192-ksR_)
11. LLM Judges Are Unreliable (https://www.cip.org/blog/llm-judges-are-unreliable)
12. LLM Judges Verify Presence, Not Absence: Omission Blindness in AI Clinical Notes (https://arxiv.org/abs/2608.31016v1)
13. LLM Judges Verify Presence, Not Absence (https://arxiv.org/html/2608.31016v1)
14. Evaluating clinical AI summaries with large language models as judges (https://www.nature.com/articles/s41746-025-02005-2)
17. Evaluating medical AI under missing information (https://arxiv.org/html/2607.18828)
18. A framework to assess clinical safety and hallucination rates of LLMs for medical text summarisation (https://www.nature.com/articles/s41746-025-01670-7)