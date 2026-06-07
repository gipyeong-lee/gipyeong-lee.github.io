---
layout: post
title: "月付 2 萬韓元的 AI 訂閱，其實是 AI 公司每個月都在為你代墊數十萬韓元？"
description: "探討 ChatGPT 和 Claude 等 AI 服務低廉的無限量訂閱費用背後，所隱藏的龐大運算成本虧損、企業的財務極限，以及未來收費機制的可能變化。"
summary: "我們所支付的低廉訂閱費用背後，隱藏著企業為維持運作而產生的龐大虧損，這可能導致 AI 收費機制在不久的將來轉變為按使用量計費。"
tags: [AI訂閱, ChatGPT成本, Claude收費, OpenAI虧損, Anthropic上市]
image: 2026-06-08-AnthropicOpenAI-may-be-spending-more-than-1000-for-every-100-you-pay-them.jpg
image_alt: "巨大的資料中心伺服器電腦正在燃燒硬幣並猛烈運轉，而前方的手機正顯示著廉價訂閱收據的插圖"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "目前低廉的收費方案是一種「戰略性虧損」，旨在讓大眾的日常生活依賴 AI。當帳單上印出真實費用的那一天，我們將會開始思考 AI 的真正價值。"
quiz:
  - question: "目前 AI 企業在維持月費訂閱模式時，所面臨的最致命問題是什麼？"
    choices: ["使用者疲勞導致使用率暴跌", "龐大的伺服器運作成本導致持續的財務虧損", "競爭對手模型的品質下降"]
    answer: 1
    explanation: "AI 服務在使用者每次提出問題並要求生成結果時，都會消耗龐大的運算能力與電力，因此目前固定的月費訂閱模式難以負擔這筆費用。"
  - question: "最近舊金山的一位房屋賣家宣布，願意接受哪種支付方式來代替高達 40 億韓元（約 300 萬美元）的房價，進而引發熱議？"
    choices: ["100 公斤純金", "OpenAI 或 Anthropic 的未上市股票", "10 台最新型超級電腦伺服器"]
    answer: 1
    explanation: "隨著 OpenAI 和 Anthropic 的企業估值飆升，加上對其首次公開發行（IPO）的期待感升高，這些企業的股票在矽谷被視為最令人垂涎的資產。"
  - question: "當 AI 閱讀我們輸入的文字並生成回答時，所使用的「基本單位」以及計算費用的基準是什麼？"
    choices: ["像素 (Pixel)", "位元組 (Byte)", "權杖 (Token)"]
    answer: 2
    explanation: "AI 並非將文字整個識別，而是將其拆解成名為「權杖 (Token)」的小碎片來處理，企業間的 API 使用費也是以這類權杖的數量為基準來精確計費。"
lang: zh-tw
ref: 2026-06-08-AnthropicOpenAI-may-be-spending-more-than-1000-for-every-100-you-pay-them
---

想像一下，下班後您來到了社區新開的一家頂級韓牛吃到飽餐廳。只需區區 2 萬 7 千韓元（約 20 美元）的入場費，您就可以盡情享用頂級牛肉。您興致勃勃地不斷點肉。然而事實上，您每次用餐所點的肉類實際成本早就超過 10 萬韓元。每當您多叫一盤肉，老闆的心都在滴血，但為了吸引顧客並在社區建立起頂級美食餐廳的地位，他只能繼續承受著驚人的虧損，不斷端上頂級牛肉。

您知道嗎？在目前震撼全球科技產業的巨型人工智慧（AI）服務背後，正在發生完全一樣的事情。在我們每個月支付 20 美元，或是為了工作支付 100 美元來使用這些神奇的 AI 助理背後，隱藏著企業間不可理喻的「流血競爭」。根據 IT 策略與架構專業媒體的深入分析，針對重度使用者所支付的每 100 美元，AI 企業為了維持伺服器運轉，可能代為投入了高達 1,000 美元以上的成本 [Anthropic/OpenAI may be spending more than $1000 for every $100 you pay them – R&A IT Strategy & Architecture](https://ea.rna.nl/2026/06/07/anthropic-openai-may-be-spending-more-than-1000-for-every-100-you-pay-them/)。

這場危險且不切實際的派對究竟能持續到什麼時候？如果有一天老闆宣布：「從現在起，我們將按您吃下的每一塊肉來收費」，我們的日常生活又會發生什麼樣的變化？

## 這為什麼重要？ (Why It Matters)

我們已經非常習慣在週末用 Netflix 狂追劇，或者一整天開著 Spotify 播放音樂。只要每個月支付固定的金額就能無限量享受內容的「統一費率訂閱（Flat-rate subscription）」模式，似乎已被視為現代數位社會的常識。這是因為影片或音樂檔案一旦上傳到伺服器，即使有數百萬人同時播放，公司所負擔的額外成本也幾乎趨近於「零」。打個比方，這就像是把已經做好的料理用微波爐加熱後端給好幾個人吃一樣。因此，許多人會理所當然地認為，ChatGPT 或 Claude 等 AI 服務也是完全相同的架構。

簡單來說，人工智慧與播放預先錄製好的影片有著天壤之別。AI 提供的並非固定的檔案，而是每當您提出問題時，遠方資料中心裡龐大的電腦群就必須耗費大量電力，進行即時的數學運算與「思考」。問題越長、要求的答案越複雜，AI 所消耗的電力與運算資源就會呈指數級暴增。這就好比專屬廚師每次都收到名為「新問題」的新鮮食材，從頭到尾為您重新製作出一道世上獨一無二的料理。

這些龐大的人工智慧開發與營運成本，迫使企業必須全面重新檢視現有的支出與收費策略，進而對 OpenAI 和 Anthropic 等領先企業的商業模式本身帶來了巨大的挑戰 [AI's Spending Problem: Why Fixes Hurt OpenAI, Anthropic | StartupHub.ai](https://www.startuphub.ai/ai-news/artificial-intelligence/2026/ai-s-spending-problem-why-fixes-hurt-openai-anthropic)。如果像現在這樣，任何人都能以低廉的價格無限量使用 AI 智慧的時代落下帷幕，那麼無數依賴 AI 來編寫程式碼、翻譯文件與進行創作的新創公司和個人，其工作模式將會受到根本性的衝擊。

## 簡單理解 (The Explainer)

為了真正理解這種畸形的虧損結構，我們必須了解 AI 是如何閱讀和書寫我們的語言，並由此產生費用的。在這個過程中有兩個核心概念。

第一個是「Transformer」（一種掌握句子中單字之間關係的 AI 架構）。這不是指會變形成汽車或飛機的機器人玩具，而是指在海量文字數據中掌握上下文，並預測下一個單字的 AI 大腦結構模型。第二個是「權杖（Token，AI 閱讀和書寫文字的基本單位）」。AI 並不像人類那樣將我們寫下的句子視為一個整體來辨識，而是將單字拆解成名為「權杖」的微小拼圖碎片來進行消化。

讓我們這樣比喻。想像您正搭乘計程車移動。計程車的計費表會隨著車輪轉動和距離的增加而「咔嚓咔嚓」地跳表。在 AI 的世界裡，當 AI 讀取我們寫下的問題拼圖碎片（輸入權杖）時，計費表會跳動一次；而為了生成回答，當它逐一寫下新的拼圖碎片（輸出權杖）時，計費表又會再跳動一次。向 AI 提出問題並獲得回答的整個過程，我們稱之為「推論（Inference）」。

如果我們看看一般消費者無法接觸到，而是企業所使用的 API（協助作業系統或程式之間通訊的媒介）收費表，就能體會到這個計費表在現實中跳得有多麼嚇人。以 Anthropic 在 2026 年 5 月推出的最高效能模型「Claude Opus 4.8」為例，它具備了一次能記住高達 100 萬個權杖（相當於數十本厚重書籍的份量）的壓倒性能力，但同時也訂出了每 100 萬個輸入權杖 5 美元、每 100 萬個輸出權杖 25 美元的驚人運作成本 [Anthropic API Pricing in 2026: Complete Guide — Models, Caching, Batch & Optimization](https://www.finout.io/blog/anthropic-api-pricing)。

雪上加霜的是，如果因為金融數據的安全性或法規要求，必須設定透過 Amazon Bedrock 或 Vertex AI 等雲端平台的美國專用區域伺服器，還會再額外加上 10% 的溢價費用。例如，一個每月使用 1 億個輸入權杖和 3,000 萬個輸出權杖的團隊，原本應支付 1,250 美元的基本費用，加上區域附加費後，實際費用將飆升至約 1,375 美元 [Anthropic API Pricing: Claude Opus 4.8 Costs Explained - Amnic](https://amnic.com/blogs/anthropic-api-pricing)。

考量到這種計費表收費機制，一般使用者每月支付的 20 美元訂閱費簡直是便宜得不可思議。根據一家分析機構的調查，在 20 美元的月費背後，公司實際需要承擔的服務提供成本可能高達 2 到 5 倍。換算下來，這等於是企業每吸引一名付費訂閱者，每個月就必須硬生生虧損 40 到 80 美元來做生意 [OpenAI and Anthropic Launch Price War for AI Coding Tools | KuCoin](https://www.kucoin.com/news/flash/openai-and-anthropic-launch-pricing-war-for-ai-coding-tools)。

特別是當軟體開發人員在編寫程式碼時那樣「嚴苛地」驅使 AI 時，成本更是會成指數級爆發。在程式設計過程中，將數千行程式碼整個丟給 AI，並透過蠻力運算（Brute-forcing）來修正錯誤，會消耗超乎想像的龐大權杖。部分分析指出，為了支援這些複雜的寫程式工作，在支付 100 美元的重度使用者背後，公司可能正承擔著高達 1,000 美元以上的伺服器成本。他們提出了根本性的質疑：「就算我們支付了真正的成本，利用這個工具來減少程式設計師的數量真的划算嗎？」[Anthropic/OpenAI may be spending more than $1000 for every $100 you pay them – R&A IT Strategy & Architecture](https://ea.rna.nl/2026/06/07/anthropic-openai-may-be-spending-more-than-1000-for-every-100-you-pay-them/)。

知名開發者 Simon Willison 也分享了現場的氛圍。他表示：「最近有很多傳聞說，企業讓員工用公費自由使用 AI 後，收到了超乎想像的龐大語言模型（LLM）帳單而大吃一驚」，他認為這正證明了 OpenAI 和 Anthropic 已經完美地滲透進了企業市場 [I think Anthropic and OpenAI have found product-market fit](https://simonwillison.net/2026/May/27/product-market-fit/)。此外，只要想想在個人電腦上為了運行輕量級的開源模型而讓顯示卡全速運轉時所消耗的龐大電費，就很難想像這些巨大的集中式企業的耗電量究竟有多麼驚人 [I think Anthropic and OpenAI have found product-market fit ...](https://news.ycombinator.com/item?id=48296794)。

## 目前情況 (Where We Stand)

在這種伺服器越是運轉、公司的現金就燃燒得越快的畸形成本結構下，企業們依然選擇承受眼前的虧損。這是因為巨頭們為了爭奪 AI 市場霸權的競爭，正處於歷史上最白熱化的階段。

成立於 2015 年的領先者 OpenAI，在 2026 年初透過大規模招商引資，獲得了高達約 8,520 億美元的天文數字企業估值。他們透過 ChatGPT 達成了每週 9 億活躍使用者的壓倒性數字，主宰了全球的消費者 AI 市場 [Anthropic vs OpenAI 2026: 30x Revenue Gap and 4x Context ...](https://tech-insider.org/anthropic-vs-openai-2026/)。相當於一個國家預算的龐大資本，正作為他們虧損前進的堅實後盾。

不甘示弱的競爭對手 Anthropic 的氣勢也同樣猛烈。由 OpenAI 前研究人員於 2021 年成立的 Anthropic，以打造「可操控、可解釋且無致命錯誤的堅固」AI 系統為堅定信念，持續投入技術開發 [Anthropicisthe new AI research outfit fromOpenAI's Dario Amodei...](https://techcrunch.com/2021/05/28/anthropic-is-the-new-ai-research-outfit-from-openais-dario-amodei-and-it-has-124m-to-burn/)。他們接連成功推出了具備強大推論與進階編碼能力的 Claude 4 與 4.1 模型，成為 OpenAI 的強勁對手 [Anthropic API Pricing in 2026: Complete Guide — Models, Caching, Batch & Optimization](https://www.finout.io/blog/anthropic-api-pricing)。

甚至在 2026 年 6 月 1 日，Anthropic 祭出了殺手鐧，為了爭奪下一個「兆元企業」的頭銜，搶先 OpenAI 一步，秘密提交了首次公開發行（IPO）的文件 [Anthropic files for IPO before OpenAI as trillion-dollar ...](https://www.msn.com/en-us/money/companies/anthropic-files-for-ipo-before-openai-as-trillion-dollar-startups-race-to-go-public/ar-AA24zvbK), [A San Francisco seller wantsOpenAIorAnthropicstock for... | Fortune](https://fortune.com/2026/06/03/san-francisco-homeowner-wants-anthropic-openai-stock-for-3-million-dollar-home/)。在矽谷，對這兩家企業的幻想幾乎達到了宗教般的狂熱。發生了一件標誌性事件，足以顯示市場的期待有多麼具爆炸性。美國舊金山諾伊谷（Noe Valley）地區一棟掛牌求售、價值 299 萬美元（約 40 億韓元）的美麗維多利亞式房屋的屋主公開宣布，他願意接受以 OpenAI 或 Anthropic 的未上市股票來代替現金支付房款 [SF Victorian AcceptsAnthropicorOpenAIStock asPayment](https://zillowgonewild.com/san-francisco-victorian-accepts-anthropic-openai-stock-160-noe-st/)。就連價值數十億韓元的房地產都想拿來換取他們的一張股票，這兩家企業的股票在矽谷被視為最令人垂涎的「魔戒」。

然而，在如此華麗的光環與如潮水般的投資資金背後，為了生存的慘烈搏鬥仍在繼續。為了稍微彌補龐大的伺服器成本，OpenAI 陸續推出了每月 100 美元的 Pro 方案，Anthropic 也推出了每月 100 美元的 Max 方案，開始搶攻有支付能力的專家客群 [I think Anthropic and OpenAI have found product-market fit](https://simonwillison.net/2026/May/27/product-market-fit/)。但令人遺憾的兩難是，購買昂貴方案的重度使用者往往會將 AI 模型逼到極限來生成程式碼和進行推論，因此公司需要承擔的實際運算成本，增長幅度遠遠超過了費用的調漲幅度。他們既是創造利潤的客戶，矛盾的是，他們也是最快燃燒公司伺服器、加速虧損的存在。

## 接下來會怎樣？ (What's Next)

所有 IT 分析師和經濟專家異口同聲發出的警告非常明確：「這場甜蜜的無限吃到飽派對絕不可能永遠持續下去」。總不能一直把水倒進無底洞裡。

如果使用者繼續將模型逼到極限，目前的訂閱商業模式將無法永遠維持，達到獲利極限的企業終將不得不對收費機制進行大規模的徹底改革。就像開發人員和大型企業客戶已經經歷的那樣，未來一般訂閱者也將全面迎來「按使用量計費（Usage-Based Billing）」系統，就像計程車跳表一樣，使用了多少「權杖」就付多少錢 [Usage-Based Billing, No Flat Rate: Why Anthropic’s 2026 ...](https://kingy.ai/ai/usage-based-billing-no-flat-rate-why-anthropics-2026-pricing-shift-changes-everything-for-claude-users/)。

當然，對消費者而言，也並非完全沒有防線。因為市場上已經出現了像中國的 DeepSeek 或基礎設施專業供應商 DeepInfra 這樣強大的競爭對手，他們以相對低廉的成本提供價格合理的「開源模型」，因此領先企業也很難在一夕之間將訂閱費暴漲 10 倍 [Anthropic/OpenAI may be spending more than $1000 for every $100 you pay them | Hacker News](https://news.ycombinator.com/item?id=48434342)。

但最終無法避免的現實正在逼近。在不久的將來，我們將從無限量方案的幻想中清醒，並對人工智慧所提供的價值是否超過我們必須支付的「實際成本」進行冷酷的重新評估。

## AI 的觀點 (AI's Take)

我們現在所享受的這種舒適且低廉的無限量收費方案，並不是單純的慈善事業。這可以被視為一種高度的「戰略性虧損」，目的是讓大眾的日常生活完全依賴 AI。在隨時隨地向 AI 提問並將複雜工作交給它的習慣深植於現代人的生活之前，這些巨頭企業正心甘情願地代為承擔龐大的帳單。

但是，總有一天這些甜蜜的補貼會中斷，帳單上必然會印出我們實際使用量所對應的真實金額。到了那時候，我們將會認真重新思考每天漫不經心丟出的「把這個寫得有趣一點」這類輕鬆問題的份量。我們是否真的準備好為了 AI 提供答案的便利性而直接支付那筆費用？我們即將面臨的真正考驗，不是技術會變得多聰明，而是 AI 是否對我們的生活不可或缺，以至於讓我們心甘情願地掏出錢包。

## 參考資料

1. [Anthropic/OpenAI may be spending more than $1000 for every $100 you pay them – R&A IT Strategy & Architecture](https://ea.rna.nl/2026/06/07/anthropic-openai-may-be-spending-more-than-1000-for-every-100-you-pay-them/)
2. [Anthropic/OpenAI may be spending more than $1000 for every $100 you pay them | Hacker News](https://news.ycombinator.com/item?id=48434342)
3. [AI's Spending Problem: Why Fixes Hurt OpenAI, Anthropic | StartupHub.ai](https://www.startuphub.ai/ai-news/artificial-intelligence/2026/ai-s-spending-problem-why-fixes-hurt-openai-anthropic)
4. [Anthropic API Pricing: Claude Opus 4.8 Costs Explained - Amnic](https://amnic.com/blogs/anthropic-api-pricing)
5. [Anthropic API Pricing in 2026: Complete Guide — Models, Caching, Batch & Optimization](https://www.finout.io/blog/anthropic-api-pricing)
6. [I think Anthropic and OpenAI have found product-market fit](https://simonwillison.net/2026/May/27/product-market-fit/)
7. [OpenAI and Anthropic Launch Price War for AI Coding Tools | KuCoin](https://www.kucoin.com/news/flash/openai-and-anthropic-launch-pricing-war-for-ai-coding-tools)
8. [SF Victorian AcceptsAnthropicorOpenAIStock asPayment](https://zillowgonewild.com/san-francisco-victorian-accepts-anthropic-openai-stock-160-noe-st/)
9. [A San Francisco seller wantsOpenAIorAnthropicstock for... | Fortune](https://fortune.com/2026/06/03/san-francisco-homeowner-wants-anthropic-openai-stock-for-3-million-dollar-home/)
10. [Anthropicisthe new AI research outfit fromOpenAI's Dario Amodei...](https://techcrunch.com/2021/05/28/anthropic-is-the-new-ai-research-outfit-from-openais-dario-amodei-and-it-has-124m-to-burn/)
11. [Anthropic vs OpenAI 2026: 30x Revenue Gap and 4x Context ...](https://tech-insider.org/anthropic-vs-openai-2026/)
12. [Usage-Based Billing, No Flat Rate: Why Anthropic’s 2026 ...](https://kingy.ai/ai/usage-based-billing-no-flat-rate-why-anthropics-2026-pricing-shift-changes-everything-for-claude-users/)
13. [I think Anthropic and OpenAI have found product-market fit ...](https://news.ycombinator.com/item?id=48296794)
14. [Anthropic files for IPO before OpenAI as trillion-dollar ...](https://www.msn.com/en-us/money/companies/anthropic-files-for-ipo-before-openai-as-trillion-dollar-startups-race-to-go-public/ar-AA24zvbK)