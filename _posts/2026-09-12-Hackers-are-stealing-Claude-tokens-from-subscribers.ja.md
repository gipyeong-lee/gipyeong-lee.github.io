---
layout: post
title: "私のAIアカウントがハッキングされた？Claudeトークン盗難事態の真相"
description: "最近、人工知能サービス「Claude」の利用者の間で、原因不明のトークン消費やアカウント盗難の被害が相次いでいます。ハッカーが私たちのAIアカウントを狙う手口と予防法を分かりやすくまとめました。"
summary: "ハッカーが悪性ソフトウェアを利用してClaudeユーザーのログインセッションを奪取し、アカウントのトークン割り当て量を無断で横取りする被害が発生しています。"
tags: [セキュリティ, Claude, AI, 情報保護, ハッキング]
image: 2026-09-12-Hackers-are-stealing-Claude-tokens-from-subscribers.jpg
image_alt: "画面の中の鍵アイコンがデジタルデータの流れの中でハッキングされる様子を抽象的に表現した画像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "単にパスワードを変更するだけでは不十分な時代になりました。アクティブセッションのセキュリティの重要性を認識し、ブラウザの管理習慣を見直すべき時です。"
quiz:
  - question: "ハッカーがClaudeアカウントを奪取する主な手口は何ですか？"
    choices: ["強力なパスワードの総当たり攻撃", "インフォスティーラー（情報窃取）マルウェアの利用", "メールフィッシングサイトへの接続"]
    answer: 1
    explanation: "ハッカーはインフォスティーラー（情報窃取）マルウェアを使用して、ユーザーのコンピュータからブラウザのCookieやログインセッションデータを直接盗み出す手口を使います。"
  - question: "ハッカーが既存の2段階認証（MFA）を回避できる理由は何ですか？"
    choices: ["AIモデルが認証を無効化するため", "すでにログイン中のセッション情報を丸ごと盗むため", "暗号化技術を解読するため"]
    answer: 1
    explanation: "すでにログインされているアクティブなセッション情報を奪取するため、ユーザーがすでに認証を終えた状態を悪用し、追加の認証ステップを経ることなくアカウントにアクセスします。"
  - question: "被害事実を確認したAnthropicの初期対応として正しいものはどれですか？"
    choices: ["サービスの一時停止", "強制ログアウトおよび決済情報の削除", "ユーザーアカウントの削除"]
    answer: 1
    explanation: "Anthropicは被害が疑われるアカウントを強制的にログアウトさせ、決済手段を削除し、一部のユーザーに対して返金措置を取っています。"
lang: ja
ref: 2026-09-12-Hackers-are-stealing-Claude-tokens-from-subscribers
---

想像してみてください。いつものように仕事を終え、人工知能（AI）サービス「Claude」の使用量を確認したところ、驚くような数字が記録されています。今日はAIに一度も質問をした覚えがないのに、トークン割り当て量（AIが処理できる情報量）は、まるで一晩中誰かが懸命に作業させたかのように減っています。[参考資料4](https://theoutpost.ai/news-story/hackers-drain-claude-accounts-as-security-breach-exposes-stolen-tokens-and-session-keys-30616/) 実際に最近、多くのClaude有料購読者が経験している不可解な被害事例です。

単にAIを無料で使おうとする試みを超え、いまやハッカーたちは私たちの貴重な有料AI購読アカウントまで狙い始めています。一体ハッカーたちはどのようにして私たちのアカウントを盗み、トークンを勝手に使用しているのでしょうか？

## なぜこれが重要なのか？

AI技術は今や日常生活に欠かせないパートナーとなりました。しかし、自分のアカウントがハッキングされたということは、単に「トークンを奪われる」以上の意味を持ちます。ハッカーがアカウントを奪取すると、彼らは私たちの割り当て量を使って独自の作業を行います。[参考資料14](https://techround.co.uk/artificial-intelligence/malware-is-now-stealing-claude-sessions-to-drain-paid-ai-usage-how-does-that-work/) 自分が支払った費用が他人の作業のために使われることはもちろん、自分のアカウントから生成されるすべてのAI活用結果が他人に露出したり、犯罪に悪用されたりする危険性を内包しているからです。さらに大きな問題は、運営会社のAnthropicが、ユーザーが自分のトークンが正確にどこで消費されたのかを把握できる詳細な分析ツールをまだ提供していないという点です。[参考資料5](https://news.ycombinator.com/item?id=49662941)

## わかりやすい解説

ハッカーたちがアカウントを奪取する手法を「鍵」に例えてみましょう。

私たちが普段使うパスワードや2段階認証（MFA、追加のセキュリティ確認手続き）は、家（アカウント）に入る時に使う「鍵」や「ドアロックの暗証番号」のようなものです。毎回入るたびに施錠を確認しますよね。しかし、ハッカーが使用する**「インフォスティーラー（Infostealer、情報窃取用マルウェア）」**はこの仕組みを完全に回避します。

簡単に言えば、ハッカーは私たちが家を出る時に不用意に玄関のドアに挿したままにしてきた**「複製された入館証（ブラウザのCookieやアクティブセッションデータ）」**を盗み出すのです。[参考資料7](https://diasporadigitalmedia.com/hackers-are-stealing-claude-tokens-from-subscribers/), [参考資料12](https://nerdstool.com/blog/hackers-are-stealing-claude-tokens-from-subscribers/) このカードさえあれば、ハッカーはパスワードを知らなくても、すでにログインされた状態のまま私たちの家の寝室まで何の制止もなく入ることができます。[参考資料9](https://techmash.blog/blog/hackers-stealing-claude-subscriber-tokens) システムからすれば、すでに認証を終えた「持ち主」が再び接続してきたと認識されるため、追加のセキュリティチェックが行われないのです。

## 現状

現在、多くのユーザーが原因不明のトークン消費被害を訴えています。[参考資料10](https://relvehq.com/blog/noise/hackers-steal-claude-tokens) あるユーザーの事例を見ると、特別な作業をしていないにもかかわらず、トークン使用量が45%から55%に急増したケースもあります。[参考資料1](https://techcrunch.com/2026/09/08/hackers-are-stealing-claude-tokens-from-subscribers/)

Anthropic側はこの事態を認識し、一部の被害者に警告メールを送っていますが、すべてのユーザーに通知が届いていないという批判も出ています。[参考資料11](https://www.bestaitools.com/hackers-are-stealing-claude-tokens-from-paying-subscribers-and-anthropic-cant-tell-you-how-much-was-taken/) 現在会社側は、被害が疑われるアカウントを強制的にログアウトさせ、登録済みの決済手段を削除し、一部のユーザーに対して返金を行うなどの対応をとっています。[参考資料12](https://nerdstool.com/blog/hackers-are-stealing-claude-tokens-from-subscribers/) しかし根本的に、このような「セッションハイジャック（アクティブセッション奪取）」攻撃を完璧に防御できる構造的なツールは、まだ完成していない状態です。[参考資料2](https://www.gadgetreview.com/hackers-are-stealing-claude-subscribers-ai-tokens)

## 今後はどうなるのか？

専門家は、こうしたハッキングキャンペーンがさらに精巧になると警告しています。マルウェアはユーザーが知らないうちにコンピュータに侵入するため、今後はブラウザのセキュリティ管理が個人情報保護の最前線となるでしょう。

ユーザーの皆さんは、自身のアカウント使用量を定期的に確認し、疑わしい動作が検知されたらすぐにアカウントをログアウトして再ログインする習慣をつけなければなりません。また、セキュリティソフトウェアを通じてシステム内にマルウェアがないか、随時検査することも重要です。さらに、AIサービス企業側も、ユーザーが自分のトークン消費内訳を透明に確認し、異常兆候を迅速に報告できるセキュリティツールを早急に用意すべきでしょう。

## 参考資料

1. [HackersarestealingClaudetokensfromsubscribers| TechCrunch](https://techcrunch.com/2026/09/08/hackers-are-stealing-claude-tokens-from-subscribers/)
2. [HackersAreStealingClaudeSubscribers’ AITokens](https://www.gadgetreview.com/hackers-are-stealing-claude-subscribers-ai-tokens)
3. [AnthropicClaudeSecurity Breach:StolenTokensHit Users](https://theoutpost.ai/news-story/hackers-drain-claude-accounts-as-security-breach-exposes-stolen-tokens-and-session-keys-30616/)
4. [HackersarestealingClaudetokensfromsubscribers|HackerNews](https://news.ycombinator.com/item?id=49662941)
5. [ClaudeTokenTheft HitsSubscribersasHackersTarget Accounts...](https://www.itechpost.com/articles/237270/20260909/claude-token-theft-hits-subscribers-hackers-target-accounts-security.htm)
6. [HackersarestealingClaudetokensfromsubscribers- Diaspora...](https://diasporadigitalmedia.com/hackers-are-stealing-claude-tokens-from-subscribers/)
7. [Hackers Are Stealing Claude Subscribers’ AI Tokens](https://tech.yahoo.com/ai/claude/articles/hackers-stealing-claude-subscribers-ai-154417768.html)
8. [Hackers Are Stealing Claude Tokens From Subscribers](https://techmash.blog/blog/hackers-stealing-claude-subscriber-tokens)
9. [Hackers are stealing Claude tokens - relvehq.com](https://relvehq.com/blog/noise/hackers-steal-claude-tokens)
10. [Hackers are stealing Claude tokens from paying subscribers ...](https://www.bestaitools.com/hackers-are-stealing-claude-tokens-from-paying-subscribers-and-anthropic-cant-tell-you-how-much-was-taken/)
11. [Hackers are stealing Claude tokens from subscribers](https://nerdstool.com/blog/hackers-are-stealing-claude-tokens-from-subscribers)
12. [Hackers draining Claude tokens from subscriber accounts](https://newsgab.com/hackers-drain-claude-tokens-from-subscriber-accounts/)
13. [MalwareIsNowStealingClaudeSessions To Drain Paid... - TechRound](https://techround.co.uk/artificial-intelligence/malware-is-now-stealing-claude-sessions-to-drain-paid-ai-usage-how-does-that-work/)
14. [Newsroom \ Anthropic](https://www.anthropic.com/news)