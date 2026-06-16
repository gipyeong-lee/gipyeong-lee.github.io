---
layout: post
title: "巴西里約熱內盧的「自主研發」AI，結果竟是拼湊而成？3,970億參數的真相"
description: "里約熱內盧發表號稱自主研發的大型人工智慧模型，事實上被揭露為混合現有開源模型而成的「模型合併（Merge）」產物。本文將淺顯易懂地說明此事件背後的意義。"
summary: "巴西里約熱內盧市政府野心勃勃公開的大型人工智慧模型，被證實並非獨立研發產品，而是現有模型的拼湊之作，這讓真正開發「在地化 AI（Local AI）」的現實困境浮出水面。"
tags: [人工智慧, 在地化AI, 大型語言模型, 模型合併, 開源, 技術驗證]
image: 2026-06-16-Rio-de-Janeiros-homegrown-LLM-appears-to-be-a-merge-of-an-existing-model.jpg
image_alt: "插畫描繪了兩個不同顏色的齒輪被硬生生地拼湊進一個巨大的機械裝置中，隱喻了將多個人工智慧混合偽裝成一個模型的拼湊爭議。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "這是一個以人工智慧模型的巨大規模來代表城市或國家技術自尊心的時代。但在全球開發者密切關注的透明開源生態系統面前，我們不應忘記，拙劣的重新包裝反而會削弱信任。"
quiz:
  - question: "關於里約熱內盧市政府野心勃勃發表的「Rio-3.5-Open-397B」模型，最近被揭露的事實是什麼？"
    choices: ["被證實為全球首個能完美理解人類情感的模型。", "只是將現有公開的其他人工智慧模型簡單混合的拼湊模型。", "因透明公開所有開發過程而受到讚賞。"]
    answer: 1
    explanation: "該模型並非獨立訓練，而是被證實為合併（Merge）了現有的「Nex-AGI」與「Qwen3」模型。"
  - question: "隨著爭議擴大，主導開發的 IplanRIO 方面提出了什麼解釋？"
    choices: ["遭到駭客攻擊，原始檔案被竄改。", "由於資料不足而做出的無奈選擇。", "不小心上傳了中間階段的合併版本，而非最終版本（知識蒸餾模型）。"]
    answer: 2
    explanation: "IplanRIO 方面道歉並表示，他們原本打算上傳最終調整的「知識蒸餾模型」，卻不小心上傳了「基礎合併版本」。"
  - question: "技術專家觀察此次事件，指出開發「在地化 AI（Local AI）」最大的現實障礙是什麼？"
    choices: ["從零開始創造世上前所未有的全新人工智慧非常困難。", "AI 開發所需的電力不足。", "相關法律規範過於嚴格。"]
    answer: 0
    explanation: "專家分析指出，建構全新事物的獨立研發非常困難，但重新包裝現有模型卻很容易，這正是此類事件發生的原因。"
lang: zh-tw
ref: 2026-06-16-Rio-de-Janeiros-homegrown-LLM-appears-to-be-a-merge-of-an-existing-model
---

## 前言：華麗初登場背後隱藏的真相

想像一下。一位世界知名的魔術師宣稱，經過多年刻苦修練，他發明了世上獨一無二的懸浮魔術。在華麗的燈光下，無數觀眾起立鼓掌、熱烈歡呼，然而一位偶然瞥見舞台後方的男孩卻大喊：「咦？那不就是巧妙地用兩根繩子綁著吊在天花板上而已嗎！」

這個有趣的故事，最近在全球最尖端技術角力的戰場——人工智慧（AI）業界真實上演了。巴西標誌性城市里約熱內盧（Rio de Janeiro）市政府自豪地公開，宣稱從頭到尾完全自主開發的大型人工智慧模型，事實上卻被證實是巧妙混合他人已開發技術的「拼湊」產物。

如今，為了不依賴外國的大型科技企業，許多國家與城市都在努力試圖擁有自己的 AI。那麼，里約熱內盧到底發生了什麼事？為什麼人們會確信這項技術是造假的？這個事件又對我們的未來傳遞了什麼訊息？就像聰明的朋友一邊喝著熱咖啡一邊說故事一樣，我們將用淺顯易懂且有趣的方式來揭開此事件的始末。

## 為什麼這很重要：「國產 AI」的夢想與 3,970 億顆星星

我們每天使用的智慧型手機語音助理或 ChatGPT 等服務，都是基於龐大規模的「大型語言模型（LLM，透過學習大量文本來理解人類語言並生成句子的 AI 系統）」來運作的。最近世界各國為了守護自國的數據主權與獨特的文化特性，正全力投入開發名為「在地化 AI（Local AI）」或「主權 AI（Sovereign AI）」的獨立人工智慧。

上週，里約熱內盧負責 IT 事務的機構「IplanRIO」發表了一項歷史性的壯舉。他們在全球 AI 開發者共享程式碼（宛如圖書館般）的平台「Hugging Face」上，理直氣壯地公開了一個名為 **「Rio-3.5-Open-397B」** 的大型模型 [Rio de Janeiro's 'Homegrown' AI Was Someone Else's Model Wit...](https://dev.to/jamilxt/rio-de-janeiros-homegrown-ai-was-someone-elses-model-with-a-new-name-jcb)。

我們必須注意這個名字後面的「397B」數字。這意味著該人工智慧擁有多達 **3,970 億個參數（Parameter）**。簡單來說，參數就像是在照片應用程式中微調色彩或亮度的「轉盤」。為了記憶大量知識並做出判斷，人工智慧模型內部有著無數的轉盤在不停運作。3,970 億這個數字，是足以媲美晴朗夜空中、甚至整個銀河系星星總數的驚人規模。這種等級的體量，意味著它能與 Google 或微軟等全球頂尖大型科技企業斥資天文數字打造的最尖端模型並駕齊驅 [Rio de Janeiro's 'Homegrown' AI Was Someone Else's Model Wit...](https://dev.to/jamilxt/rio-de-janeiros-homegrown-ai-was-someone-elses-model-with-a-new-name-jcb)。

如果一個城市的政府機構真的完全「自主開發」出如此龐大的人工智慧，這將是人類技術史上留名的巨大成就。但這場偉大的慶典，很快就捲入了致命的質疑之中。

## 淺顯易懂：了解「獨立研發」與「模型合併」的決定性差異

為了直指這起事件的核心，我們必須理解將人工智慧「獨立訓練（Train）」與單純「合併（Merge）」在本質上的差異。

打個比方，想像您要向世界推出一款世上從未有過、全新口味的特製咖哩。
**「獨立研發（自主學習）」**就像是自己從田裡種植馬鈴薯和洋蔥，從印度貧瘠的土地進口香料，經過數千次比例測試後，製作出屬於自己完美咖哩粉的艱難旅程。這需要花費大量的時間、鉅額的金錢以及無數專家的汗水。在 AI 世界中，這等同於讓數千台超昂貴的電腦（GPU）日以繼夜地運轉好幾個月，從零開始像用湯匙餵食般，教導它龐大數據資料的孤獨且嚴酷的過程。

相反地，**「模型合併（Model Merge）」**完全是另一回事。這就像是從大型超市買來已經熱賣的「A 牌塊狀咖哩」和「B 牌辣味咖哩」，把它們全部倒進一個大鍋裡一起煮。兩種咖哩混合後，確實可能會產生看起來不錯且好吃的成果。但是，如果把這道混合料理端到大眾面前並宣傳說：「這是我們市政府經過多年研究，從底層開始自主研發的革命性新產品咖哩！」這會怎麼樣呢？這顯然是一種欺騙行為。

遺憾的是，里約熱內盧發表的「自主研發」AI 模型，並非在全新基礎上獨立訓練的系統 [RiodeJaneiro's"homegrown"LLMappearstobeamergeofan...](https://deepintellica.com/ai-work/rio-de-janeiro-s-homegrown-llm-appears-to-be-a-merge-of-an-existing-model/)。

## 目前狀況：GitHub 名偵探的活躍與牽強的解釋

令人驚訝的是，最先揭穿這巨大技術牛皮的，既不是大型媒體，也不是政府的審計機構。而是活躍於軟體開發平台「GitHub」（全球數千萬程式設計師活動的平台）上的普通開發者們。有人在 GitHub 的錯誤回報區「Issue」論壇上提出了一個尖銳的問題，真相的潘朵拉之盒就此被打開 [Cosmic Rundown: Billion Dollar Essays, Rio's LLM Drama, Context Window Limits](https://www.cosmicjs.com/blog/cosmic-rundown-billion-dollar-essays-rio-llm-context-windows)。

社群分析結果顯示，這個「自主研發模型」實際上是被證實為巧妙合併（Merge）了網路上免費公開、任何人都能下載的 **「Nex-AGI」** 模型與 **「Qwen3」** 模型 [Rio LLM Exposed: Major Model Merge, Not Original AI](https://www.squaredtech.co/rios-official-ai-model-is-proven-to-be-a-model-merge), [RiodeJaneiro's"homegrown"LLMappearstobeamergeofan...](https://deepintellica.com/ai-work/rio-de-janeiro-s-homegrown-llm-appears-to-be-a-merge-of-an-existing-model/)。

在拆解了由電腦程式碼與數學數值構成的 AI 模型內部大腦結構後，沒有發現任何一絲從底層重新學習的證據。取而代之的是，發現了明顯物理混合他人模型的鐵證 [Rio LLM Exposed: Major Model Merge, Not Original AI](https://www.squaredtech.co/rios-official-ai-model-is-proven-to-be-a-model-merge)。開發者的遊樂場 GitHub，此時宛如揭發腐敗的鳴冤鼓或犀利的調查報導部落格 [Hacker News 20 on X: "Rio de Janeiro's "homegrown" LLM appears to be a merge of an existing model https://t.co/G1dBFWiQcO (https://t.co/Uht1ZUEPrL)" / X](https://x.com/betterhn20/status/2066300653404667962), [RiodeJaneiro's"homegrown"LLMappearstobeamergeofan...](https://deepintellica.com/ai-work/rio-de-janeiro-s-homegrown-llm-appears-to-be-a-merge-of-an-existing-model/)。

當批評的聲浪如野火般蔓延時，主導開發的 IplanRIO 方面急忙發表了解釋聲明。他們道歉並表示：「我們在上傳舊版本的過程中犯了上傳錯誤檔案的失誤。原本應該上傳最終完成的 **『知識蒸餾模型（Distilled model）』**，卻不小心錯傳了作業中間階段的 **『基礎合併版本（Base merged version）』**。」 [RiodeJaneiro's"homegrown"LLMappearstobeamergeofan...](https://news.ycombinator.com/item?id=48528371)。

這裡所說的 **「知識蒸餾（Distillation）」** 又是什麼呢？請想像一下，用大型咖啡機將大量的咖啡豆強力擠壓，萃取出一杯非常濃郁且香氣四溢的濃縮咖啡原液。在 AI 領域，知識蒸餾技術是一種高階技術，將體積過大且難以駕馭的天才 AI（教師模型）的核心知識萃取出來，壓縮成能在智慧型手機等小型裝置上快速運作的輕量級 AI（學生模型）。

也就是說，市政府的藉口是：「我們確實混合（Merge）了其他模型並把它們放進鍋裡煮，但我們原本想向大眾公開的，是將其成果漂亮壓縮後的完成版濃縮咖啡（知識蒸餾模型）。」然而，退一百步說，即使這單純只是上傳失誤，投入市民稅金的公共人工智慧其骨幹最終是「混合他人模型而成」的本質，絲毫沒有改變。

## 未來展望：重新包裝的時代，如何辨別真正的創新

這次的「里約熱內盧醜聞」，讓全球許多試圖建立自己獨立 AI 生態系統的地方政府與企業，深刻體會到沉重的現實之牆。

活躍於社群媒體 X（前身為 Twitter）的一位著名技術專家，在觀察這場鬧劇後犀利地指出：「里約熱內盧號稱自主研發的模型？結果被發現只是現有模型的拼湊。圍繞著『在地化 AI』的狂熱（Hype）總是會撞上同一道巨大的牆：實際上從頭打造出全新的事物太過艱難，而將現有事物煞有其事地重新包裝（Repackaging）卻容易得多。」 [Anto Patrex on X: "Rio de Janeiro's supposedly homegrown LLM? Turns out it's a merge of existing models. The hype around 'local AI' keeps running into the same wall: actually building something novel is hard. Repackaging is easier." / X](https://x.com/antopatrex1/status/2066375933108314528)

隨著人工智慧技術未來更深入我們的生活，許多機構將會爭先恐後地大吹法螺，宣稱「我們終於完成了獨立的人工智慧！」但我們現在必須以非常謹慎和批判的眼光來審視那華麗包裝的內部。因為即使表面上看起來像是擁有數千億參數的偉大發明，它的內部可能只是悄悄混合了某人流血流汗做出來的免費開源模型罷了。

## AI 的觀點：透明度就是最強的技術實力

這是一個以人工智慧模型的巨大規模或天文數字般的參數數量，來代表城市或國家技術自尊心的時代。我們不能一味地指責里約熱內盧渴望獲得自主技術實力的熱情本身。為了克服龐大資本的限制，聰明地結合並活用現有的開源技術，也是現代軟體開發自然且高效的趨勢。

但在全球無數天才開發者睜大眼睛注視著的透明開源生態系統面前，我們絕不能忘記，拙劣的重新包裝與誇大不實的宣傳，反而會嚴重削弱信任。真正的技術獨立與獲取主權，並非來自於照著網路上流傳的食譜混合調味料，然後冠上一個響亮的名字。只有在貧瘠的環境中依然誠實地蒐集優質的在地數據，透明地分享自身的局限，並一步一腳印地前進的忍耐中，才能開出真正創新的花朵。里約熱內盧短暫且虛妄的一日天下，為生活在 AI 時代的我們所有人，留下了最痛苦卻也最寶貴的教訓。

## 參考資料

1. [Rio de Janeiro's 'Homegrown' AI Was Someone Else's Model Wit...](https://dev.to/jamilxt/rio-de-janeiros-homegrown-ai-was-someone-elses-model-with-a-new-name-jcb)
2. [RiodeJaneiro's"homegrown"LLMappearstobeamergeofan... (Deep Intellica)](https://deepintellica.com/ai-work/rio-de-janeiro-s-homegrown-llm-appears-to-be-a-merge-of-an-existing-model/)
3. [Rio LLM Exposed: Major Model Merge, Not Original AI](https://www.squaredtech.co/rios-official-ai-model-is-proven-to-be-a-model-merge)
4. [Cosmic Rundown: Billion Dollar Essays, Rio's LLM Drama, Context Window Limits](https://www.cosmicjs.com/blog/cosmic-rundown-billion-dollar-essays-rio-llm-context-windows)
5. [Hacker News 20 on X: "Rio de Janeiro's "homegrown" LLM appears to be a merge of an existing model https://t.co/G1dBFWiQcO (https://t.co/Uht1ZUEPrL)" / X](https://x.com/betterhn20/status/2066300653404667962)
6. [RiodeJaneiro's"homegrown"LLMappearstobeamergeofan... (Hacker News Discussion)](https://news.ycombinator.com/item?id=48528371)
7. [Anto Patrex on X: "Rio de Janeiro's supposedly homegrown LLM? Turns out it's a merge of existing models. The hype around 'local AI' keeps running into the same wall: actually building something novel is hard. Repackaging is easier." / X](https://x.com/antopatrex1/status/2066375933108314528)