---
layout: post
title: "AI 撰寫福利申請書，為何讓公家機關陷入文件淹沒的危機？"
description: "隨著利用 AI 撰寫福利補助申請書的案例增加，公家機關正面臨工作超載的問題。本文將探討 AI 自動化申請所引發的「代理淹沒（Agentic Flooding）」現象及其帶來的明與暗。"
summary: "利用 AI 撰寫福利申請書雖能提升易用性，但過度自動化導致的「代理淹沒」現象，正造成公共服務業務癱瘓。"
tags: [AI, 公共服務, 福利, 代理淹沒, 技術的雙面刃]
image: 2026-08-25-Public-services-are-increasingly-strained-by-LLM-written-appeals-for-benefits.jpg
image_alt: "公家機關辦公桌上堆滿無數文件的圖像，以及上方快速處理這些文件的 AI 代理圖像。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "技術的效率提升了公共便利性，但我們不能忽視當工具凌駕於目的之上時所產生的社會成本。除了單純引入技術，我們更應思考如何建立一個系統本身能承受的健康連結。"
quiz:
  - question: "本文件中提到的「代理淹沒（Agentic Flooding）」是指什麼？"
    choices: ["AI 代替公家機關管理預算的現象", "因 AI 代理生成的申請書急劇增加，導致公共服務過載的現象", "政府機構投入巨額資金開發 AI 的行為"]
    answer: 1
    explanation: "代理淹沒是指隨著使用 AI 代理進行申請的情況增加，導致準備不足的政府機構業務量急劇暴增的現象。"
  - question: "為了阻止 AI 撰寫的申請書，採取倉促應對措施會帶來什麼副作用？"
    choices: ["AI 技術的發展速度會減慢。", "真正需要援助的人們的申請也有可能同時被封鎖。", "政府機構的預算會增加。"]
    answer: 1
    explanation: "最快速的阻擋方式往往是透過技術篩選進行批量處理，這導致真正需要幫助的實際申請者也會一同被封鎖，產生矛盾的狀況。"
  - question: "公家機關在引入技術時應注意什麼？"
    choices: ["應相信單憑引入技術就能解決所有資源不足的問題。", "技術引入並不保證公共服務效率，必須同時輔以法律及制度上的完善。", "應無條件引進最新的 AI 模型。"]
    answer: 1
    explanation: "技術僅是工具，並非解決資源不足的根本之道。應留意技術可能引發法律不確定性，反而阻礙了福利的普及。"
lang: zh-tw
ref: 2026-08-25-Public-services-are-increasingly-strained-by-LLM-written-appeals-for-benefits
---

試著想像一下，在需要填寫繁瑣文件以獲得福利補助的情況下。過去可能因為需要逐一閱讀並填寫無數項目而耗費數天，現在只需對生成式 AI（Generative AI，基於龐大數據生成句子或影像的人工智慧）說一句「請說明我的情況並幫我撰寫福利申請書」，完美的申請書便能在瞬間誕生。

這種技術變革對於資訊取得能力較弱，或在繁瑣行政程序中感到困難的人來說，無疑像是一種祝福。然而，近來公家機關的辦公室風景，卻因另一種意義而變得忙碌。這是因為 AI 送出的申請書正如同滾雪球般不斷增加。

## 為何值得關注？

我們常期待技術引入後能使公共服務更有效率，並減少行政浪費。事實上，許多政府機構都將利用 AI 提升生產力設為目標 [出處: The Promises and Perils of using LLMs for Effective Public Services](https://arxiv.org/html/2601.15163)。

但技術引入並非解決所有問題的萬靈丹。由 AI 代理（AI Agent，為達成特定目標而能自主判斷並行動的 AI 程式）撰寫的申請書如爆炸般湧入，正給予毫無準備的政府機構過度負擔。這不只是導致業務處理變慢，還可能使真正迫切需要福利的人們的申請，被 AI 生成的大量文件淹沒；或者在系統試圖阻擋這些文件的過程中，連真正的申請者也被拒之門外，造成令人遺憾的結果 [出處: Agent-Written Applications Are Filling Government Desks](https://blog.pebblous.ai/blog/agentic-flooding-government-services/en/)。

## 淺談這一現象

近來研究人員開始將這種現象稱為**「代理淹沒（Agentic Flooding，指 AI 代理製作的文件如洪水般湧入的現象）」**。可以用以下比喻來簡單理解：

過去知名餐廳預約僅限電話，某天起，有人安裝了一台能自動撥號的機器，開始在一秒內撥打數百次電話。身為餐廳老闆的公家機關，在不斷的電話鈴聲中無法招架，而真正想預約的客人——也就是實際申請者，只能不斷聽到「通話中」的訊號，最終不得不放棄預約。

專家已經在 11 個管轄區收集了 84 個以上的案例，確認了這種現象正在現實中發生 [出處: Characterizing Agentic Flooding of Government Services](https://arxiv.org/html/2608.16603)。AI 毫無疲倦地創作出語句完美的申請書，但由於這些成果超過了機構的處理容量，導致系統陷入「過載」狀態。

更大的問題在於應對方式。為了阻擋這場洪水，公家機關最先採用的通常是更強大的「技術篩選」。然而，這樣築起的牆往往不分 AI 或真人一律封鎖。比喻來說，就像餐廳老闆因為電話鈴聲太吵，乾脆直接拔掉了電話線。這嚴重損害了福利制度原有的本意 [出處: Agent-Written Applications Are Filling Government Desks](https://blog.pebblous.ai/blog/agentic-flooding-government-services/en/)。

## 我們目前的處境

在公共服務現場，技術引入背後的兩面性已經相當明顯。部分國家雖然出現了簡化申請流程的趨勢，但對於這種變革是否能完全保證行政品質，仍存在許多懷疑的眼光 [出處: The risks and benefits of government moves to push more appeals through a streamlined written procedure](https://www.planningresource.co.uk/article/1925103/risks-benefits-government-moves-push-appeals-streamlined-written-procedure)。

此外，在政府資源本身就不足的情況下，引入技術本身並無法成為魔法般的解決方案。相反地，有報告指出，隨著處理技術的複雜程序增加，需要幫助的人們實際上要取得福利變得更加困難 [出處: “In the last year, it’s gotten a lot worse” A Qualitative Investigation of Barriers to Disability Benefits in 2025](https://dredf.org/ssa-barriers-2025/)。技術不但沒有幫助我們的生活，反而成為了複雜官僚體制的另一道高牆 [出處: New Technologies, Old Rights: Litigating Public-Benefits Modernization](https://yalelawjournal.org/essay/new-technologies-old-rights-litigating-public-benefits-modernization/)。

## 未來的課題

未來，公家機關為了與 AI 代理共存，必須制定更精細的制度安排。不能僅止於判斷申請書是人工還是 AI 撰寫，更需要一個能確認系統所要求的核心資訊是否清晰明瞭的整合溝通管道 [出處: Clear Appeal Rights for Public Benefits Agencies](https://stegmeierconsulting.com/appeal-rights-public-benefits-agencies-hearings-deadlines/)。

顯而易見的是，技術確實改變了取得福利補助的程序，使其變得更便利。但為了不讓技術癱瘓行政業務，也不讓那道牆阻礙了真正需要幫助的人們，社會共識與制度的整備必須優先進行。畢竟技術是為了幫助人類而存在，絕不能讓人為了跟上技術的速度而做出犧牲。

## 參考資料

1. [Agent-Written Applications Are Filling Government Desks](https://blog.pebblous.ai/blog/agentic-flooding-government-services/en/)
2. [Characterizing Agentic Flooding of Government Services](https://arxiv.org/html/2608.16603)
3. [Clear Appeal Rights for Public Benefits Agencies](https://stegmeierconsulting.com/appeal-rights-public-benefits-agencies-hearings-deadlines/)
4. [The Promises and Perils of using LLMs for Effective Public Services](https://arxiv.org/html/2601.15163)
5. [How to Appeal | Health & Human Services](https://hhs.iowa.gov/appeals/how-appeal)
6. [The risks and benefits of government moves to push more appeals through a streamlined written procedure | Planning Resource](https://www.planningresource.co.uk/article/1925103/risks-benefits-government-moves-push-appeals-streamlined-written-procedure)
7. [“In the last year, it’s gotten a lot worse” A Qualitative Investigation of Barriers to Disability Benefits in 2025 - DREDF](https://dredf.org/ssa-barriers-2025/)
8. [New Technologies, Old Rights: Litigating Public-Benefits Modernization](https://yalelawjournal.org/essay/new-technologies-old-rights-litigating-public-benefits-modernization)