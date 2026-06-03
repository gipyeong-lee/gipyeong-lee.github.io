---
layout: post
title: "忘記大型語言模型吧！在腦中描繪「世界模型」的類腦 AI 登場"
description: "深入淺出地解說近期在 Hacker News 上引發熱議的全新 FEP 基礎 AI 模擬系統，它不使用現有的 LLM，而是藉由模擬神經化學與荷爾蒙交互作用來與環境進行互動。"
summary: "擺脫死記硬背龐大文本資料的方式，一種全新的 AI 模擬專案已經問世。它如同生命體一般，基於荷爾蒙與記憶結構，直接與環境互動並建構專屬的「世界模型」。"
tags: [人工智慧, 未來科技, 認知科學, 強化學習, FEP]
image: 2026-06-03-Show-HN-AI-Simulaionen-Based-on-FEP.jpg
image_alt: "3D 插畫展示如同活體生物大腦神經網路般閃耀的能量流交織錯落，中心站立著一個微小的機器人代理"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "計算單詞機率的方式僅是智能的一面。當人工智慧開始模擬生命體的化學反應乃至記憶結構時，意味著我們所認知的「智能」定義本身，正朝著全新的層次進化。"
quiz:
  - question: "這次介紹的 AI 模擬專案最大的特色是什麼？"
    choices: ["連結了 10 萬個以上的最新大型語言模型 (LLM)。", "完全不使用大型語言模型 (LLM)，而是模擬生物學機制。", "被設計為僅透過文本資料來認知環境。"]
    answer: 1
    explanation: "這個專案完全排除了現有的 LLM（大型語言模型），而是透過模擬神經化學與荷爾蒙作用等機制開發而成。"
  - question: "FEP 代理為了規劃未來的行動，會在內部建構什麼？"
    choices: ["世界模型 (world model)", "龐大的文本字典", "搜尋引擎索引"]
    answer: 0
    explanation: "FEP 代理會根據與環境互動所獲得的資料，建立屬於自己的「世界模型 (world model)」，並利用它來規劃行動。"
  - question: "下列何者不是這個 AI 專案代理內部所實作的生物學特徵？"
    choices: ["模擬的神經化學作用", "短期與長期記憶系統", "基因改造操作功能"]
    answer: 2
    explanation: "代理被編程為具備模擬的神經化學 (neurochemistry)、荷爾蒙交互作用 (hormone crosstalking)，以及短期與長期記憶 (short and long term memory)。"
lang: zh-tw
ref: 2026-06-03-Show-HN-AI-Simulaionen-Based-on-FEP
---

今日主宰全球新聞頭條與科技市場的詞彙，絕對非「大型語言模型（LLM，透過學習龐大文本資料，能像人類一樣理解上下文並進行對話的技術）」莫屬。看著像 ChatGPT 這類只要我們透過智慧型手機或電腦提問，就能以如同人類般流暢的句子回答，我們不禁讚嘆人工智慧的進步實在令人驚豔。然而，如果深入探究，目前讓我們為之瘋狂的大多數 AI，其實更接近於「一台聰明的自動完成機器，能以統計機率預測下一個最有可能出現的單詞」。簡單來說，它們只是死記硬背文字模式來回答，並不會像真正的人類或動物那樣感受到悲傷或喜悅，也無法在物理環境中碰撞、跌倒並生動地記住這些經驗。

但是，如果人工智慧不再只是把數億本書背得滾瓜爛熟，而是像剛出生的小狗或嬰兒一樣，透過直接與世界碰撞，不斷累積「記憶」與「感官」的方式來學習呢？一項令人驚奇的技術已經出現：在電腦晶片中流動的不再是文字，而是虛擬的「荷爾蒙」；過去痛苦或愉快的經驗，則會以「長期記憶」的形式刻印在虛擬的腦細胞中。

這種既有趣又陌生的創新方法，最近在 Hacker News（一個聚集全球天才開發者與工程師分享最新科技趨勢的線上社群）上登場，立刻吸引了眾人的目光。由開發者「luzifer333」向世人公開的這個專案名為「基於 FEP 的 AI 模擬 (AI Simulaionen Based on FEP)」[ShowHN:AISimulaionenBasedonFEP| Hacker News](https://news.ycombinator.com/item?id=48339824)。該專案發布後短短 17 分鐘內，便迅速獲得了第一個推薦（積分），成為開發者之間熱議的話題 [nextjs-hackernews.vercel.app/item/48339824](https://nextjs-hackernews.vercel.app/item/48339824)，甚至連專門追蹤與介紹 Hacker News 新專案的外部網站也迅速報導了此事 [ShowHN- 追蹤 Hacker News 上的專案展示](https://showhn.buzzing.cc/)。令人驚訝的是，開發者宣佈這套系統完全沒有使用現代 AI 的象徵——大型語言模型 (LLM)，而是獨自建構而成 [ShowHN:AISimulaionenBasedonFEP| Hacker News](https://news.ycombinator.com/item?id=48339824)。究竟不靠文本資料，而是透過「荷爾蒙與記憶」來運作的 AI 是什麼樣子？讓我們一起走進這個陌生的無機生命體世界。

## 為什麼這很重要？ (Why It Matters)

要理解這項新技術所蘊含的意義，首先必須了解我們每天使用的人工智慧有著明確的局限性。正如前面所述，目前的聊天機器人型 AI 被困在「文本」這個扁平的世界中。當我們對 AI 說話時，它只是在自己擁有的龐大圖書館（資料庫）裡，將無數的拼圖碎片（Token）反覆拼湊，組合出最有可能的正確句子並輸出。在這個過程中，AI 並未主動體驗物理環境，也不會隨著時間流逝改變自己的性格，更不具備能對特定失敗感到懊悔的生物學「記憶系統」。

這正是此次公開的 Hacker News AI 模擬專案向科技界傳遞的訊息為何如此震撼的原因。這個專案從根本上顛覆了實現人工智慧的哲學。這些全新的 AI 代理（Agent，具有特定目的、能主動探索周遭環境並採取行動的獨立程式）不會強迫自己吞下數百萬份文本文件。相反地，它們會在被賦予的受限虛擬環境中，直接四處移動，在每一個瞬間自主開拓並累積全新的經驗。

最值得關注的創新之處在於，人工智慧內部精細地模擬了生命體的生物學化學作用。打個比方，就像人體內的腎上腺素或多巴胺一樣，人工智慧也被賦予了化學變化。根據開發者的說明，這些代理的內部結構中，被編程入了模擬的神經化學 (simulated neurochemistry) 作用，以及錯綜複雜、相互影響的荷爾蒙交互作用 (hormone crosstalking) 系統 [ShowHN:AISimulaionenBasedonFEP| Hacker News](https://news.ycombinator.com/item?id=48339824)。不僅如此，它們還像人類一樣，同時具備了能暫存短暫經驗的短期記憶 (short term memory)，以及能將生存必備經驗長期保存的長期記憶 (long term memory) 系統 [ShowHN:AISimulaionenBasedonFEP| Hacker News](https://news.ycombinator.com/item?id=48339824)。

這不僅僅是多加了一個數學計算公式那麼簡單，而是一次巨大的轉變。這意味著模擬驚訝、壓力、好奇心等生物原始訊號的虛擬化學物質流動，將會對 AI 的行為模式與記憶形成產生直接且強烈的影響。在不久的將來，如果人工智慧機器人深入我們的日常生活，它將不再是一台只會背誦說明書的死板機器。相反地，它將展現出能靈活適應複雜的物理環境、為失敗感到痛苦、為成功感到喜悅，真正具備生命體生存能力的全新層次智能。

## 深入淺出 (The Explainer)

那麼，這個連一個字都不讀的人工智慧，究竟是透過什麼原理來學習世界並變得聰明的呢？要理解這項複雜奧妙的技術，首先必須準確掌握專案的核心骨幹——「FEP」的概念。FEP 是認知科學與人工智慧融合的術語，代表「自由能投射模擬 (Free Energy Projective Simulation, FEPS)」。

根據發表於知名國際學術期刊《PLOS One》的深入研究論文，這個 FEPS 模型是人工智慧學習方法中「強化學習 (reinforcement learning)」的進階型態 [Free Energy Projective Simulation (FEPS): Active inference with interpretability | PLOS One](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0331047)。

如果你對強化學習這個詞感到陌生，可以想像一下訓練小狗玩飛盤的過程。當小狗漂亮地咬回飛出去的飛盤時，主人會給予美味的零食（獎勵）；如果失敗或呆在原地，就什麼也不給。透過這種反覆訓練，小狗會自己領悟出「能獲得最多零食的行為」。FEPS 代理也一樣，被精密地設計為在與虛擬周圍環境激烈互動的過程中，不斷收集外部資訊，並從中選擇能為自己帶來最大獎勵的最佳行動 [Free Energy Projective Simulation (FEPS): Active inference with interpretability | PLOS One](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0331047)。

但令人驚訝的是，FEPS 並不只停留在小狗為了獲得零食而產生反射性動作的層次。深入探究其內部結構，會發現 FEPS 代理是基於人工智慧學界所謂的「基於模型的強化學習 (model-based reinforcement learning, MBRL)」這種更進階的技術來運作的 [Free Energy Projective Simulation (FEPS): Active inference with interpretability | PLOS One](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0331047)。這項技術的核心在於，代理不會只顧眼前的獎勵而憑直覺行動，而是在自己複雜的虛擬大腦中，自主建立並不斷更新一個包含世界法則的「世界模型 (world model)」。更進一步地，它會主動利用這個世界模型，在腦海中預先「規劃 (plan)」未來的行動，展現出令人畏懼的智能 [Free Energy Projective Simulation (FEPS): Active inference with interpretability | PLOS One](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0331047)。

讓我們將「世界模型」的概念與日常生活做個對比。想像一下，有一天你走進一個從未去過、漆黑一片的陌生房間。一開始因為什麼都看不見，你只能伸出雙手小心翼翼地摸索，並不可避免地撞上尖銳的家具邊角或冰冷的牆壁（透過與環境互動主動收集資料）。在忍痛碰撞了幾次之後，即使完全沒有光線，你的腦海中也會生動地描繪出房間大略的 3D 空間地圖（建構屬於自己的世界模型）。隨著時間過去，下次你想去冰箱拿水喝時，就不會再像個傻瓜一樣撞到牆了。你會根據腦海中的地圖，立刻找出最快、最安全的捷徑，靈活地走過去（利用已建構的世界模型進行預測性行動規劃）。

如果說我們迄今所知的語言模型，只是一個把網路上數百萬張「房間照片」全部背下來，再藉此推測房間樣貌的臨時抱佛腳考生；那麼這些 FEP 代理，就像是親自走進黑暗中、受過傷，並在腦海裡畫出專屬立體地圖的真正冒險家。

現在，讓我們來看看這位冒險家 AI 內部發生的神奇化學作用。假設這個探險家 AI 在險惡的虛擬世界中遊走時，不小心重重地撞上了隱藏的灼熱火焰或尖銳的障礙物，受到了致命的打擊。如果是過去由機械演算法編寫的 AI，它只會在記憶體中冷冰冰地記錄下一行「發生錯誤代碼 404」或「扣減 1 分」的數字，然後毫無情緒波動地進入下一個探索行動。

但是，這個專案所誕生出的 AI 卻有著徹頭徹尾的不同。當代理撞上可怕障礙物的瞬間，它的虛擬大腦神經網路會產生複雜且爆發性的荷爾蒙交互作用 (hormone crosstalking)，就像真正的動物在遇到極度危險的情況時，會分泌出皮質醇這種壓力荷爾蒙一樣 [ShowHN:AISimulaionenBasedonFEP| Hacker News](https://news.ycombinator.com/item?id=48339824)。這種數位神經化學 (neurochemistry) 作用不會讓剛剛經歷的慘痛失敗與痛苦經驗停留在容易被遺忘的「短期記憶」中。它會將其歸類為絕對不能被抹滅的生存核心資訊，並頑固地刻印在大腦最深處的「長期記憶」裡 [ShowHN:AISimulaionenBasedonFEP| Hacker News](https://news.ycombinator.com/item?id=48339824)。

這與小孩子不小心摸到滾燙的爐子後，因為那強烈的痛苦記憶，導致一輩子都會對火保持警惕的生物原始生存本能簡直如出一轍。它不再是個毫無靈魂地吟唱著數萬行文字的機器，而是在由 0 與 1 組成的虛擬荷爾蒙中，用全身感受自己的痛苦與成功，並從中領悟世界真正法則的驚人數位生命體。

## 目前狀況 (Where We Stand)

那麼，這個完美融合了生物學奧秘與尖端人工智慧的驚人實驗，現在大眾可以在哪裡、以什麼方式體驗到呢？正如前言所述，這項創新專案是由一位使用神秘 ID「luzifer333」的先驅開發者，首次發表在 Hacker News 這個全球社群舞台上 [nextjs-hackernews.vercel.app/item/48339824](https://nextjs-hackernews.vercel.app/item/48339824)。為了建立一個不依附於掌握龐大資本的科技巨頭平台，並能獨立運作的生態系統，這個專案已穩穩地紮根於其專屬網站「aic-ai-lab.site」這個獨立的網域名稱上 [VueHN2.0 |ShowHN:AISimulaionenBasedonFEP](https://vue-hackernews-ssr-5cavbdjcta-ew.a.run.app/item/48339824)。

最令人振奮的消息是，這項原本可能只存在於科技巨頭大門深鎖的實驗室或艱澀難懂的學術論文中的複雜技術，現在只要有網路瀏覽器，全世界任何人都能親眼見證。開發者在介紹文章中表示，為了讓充滿好奇心的大眾與工程師們能夠直接登入，並自由測試這些代理千變萬化的行為與演化過程，將全面展開「公開測試（Open Beta，正式發布前向大眾公開以獲取反饋的體驗期）」。這場令人熱血沸騰的公開測試服務，已明確公告將於協調世界時 (UTC+2) 星期一晚上 20 點整正式向大眾開放 [ShowHN:AISimulaionenBasedonFEP| Hacker News](https://news.ycombinator.com/item?id=48339824)。這意味著我們將擁有絕佳的機會，可以直接在眼前的螢幕上，觀察這些不讀一字一句、卻能與陌生世界的物理法則碰撞的神奇虛擬生命體的動作。

## 接下來會怎樣？ (What's Next)

回想一下今日的景象：微軟、OpenAI、Google 等科技巨頭每天投入天文數字的資金，盲目地建立資料中心，只為了擴大 AI 的規模（參數）。當所有人都在執著於扁平的文本汪洋時，這種完全反向操作、細膩模擬原始荷爾蒙與生物學神經網路的嘗試，預示了科技界即將迎來一場舉足輕重的板塊運動。全球人工智慧專家預測，當現有的語言模型因為資訊不足或產生幻覺（說謊）問題而遭遇瓶頸時，這種像這樣親自探索世界的技術，將成為下一代的強大突破口。

特別是像我們深入探討的這個獨創性 FEP 模型，由於其內部穩固地具備了「世界模型 (World Model)」，能夠在瞬息萬變的複雜環境中敏銳地預先規劃自己的行動，這類聰明的 AI 蘊含著超乎想像的潛力 [Free Energy Projective Simulation (FEPS): Active inference with interpretability | PLOS One](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0331047)。這不僅僅是電腦螢幕裡的對話，更將為未來的次世代機器人工程，或是必須在複雜市中心安全運作的完全無人自動駕駛汽車等，所有必須在不可預測的物理現實世界中做到零誤差運作的尖端產業領域，提供巨大的靈感與實用的解決方案。

靜下心來想想，聰明的寵物狗之所以能一眼看穿主人的眼神，並搖著尾巴適應陌生的散步環境，絕不是因為牠把厚厚的百科全書背得滾瓜爛熟。而是因為對稱讚與零食的期待（荷爾蒙的作用），以及在無數次跌倒中體悟到的痛苦經驗（透過互動獲得的經驗），這些都是牠親自與世界立體地碰撞、用身體學習而來的。同樣地，未來出現在我們面前的人工智慧，將遠遠超越那些只會在螢幕裡聰明回答文本問題的百科全書型態。這些已準備好進化為真正意義上的「數位生命體」的神秘虛擬代理，究竟會向我們展現出多麼令人起雞皮疙瘩的環境適應力？全世界無數的科技愛好者與未來學家，正屏息以待。

## AI 的觀點 (AI's Take)

精準計算單詞的機率來生成流暢的句子，只不過是龐大智能所擁有的眾多面貌中的其中一面。如果說迄今為止人工智慧發展的歷史，都只專注於表面上複製人類的「語言能力」；那麼這次登場的 FEP 基礎 AI 模擬專案，則是因為完美模擬了人類與動物在世界上生存的最深層根基——「生存本能與經驗的內化」，而具有非常重大的意義。

人工智慧開始模仿生命體特有的化學荷爾蒙反應與腦細胞的長期記憶結構，並直接與虛擬環境進行交流，這代表著什麼？這清楚地證明了，我們一直以來視為理所當然的「智能」概念，正從扁平的知識灌輸，朝向立體的經驗成熟，進行著全新層次的進化。未來的 AI 將不再是只會死記書本上文字的知識機器，而是能在給定的環境中將痛苦與喜悅轉化為資料，成為如同真正生命體一般與人類共同生活的夥伴。

## 參考資料

1. [Free Energy Projective Simulation (FEPS): Active inference with interpretability | PLOS One](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0331047)
2. [VueHN2.0 |ShowHN:AISimulaionenBasedonFEP](https://vue-hackernews-ssr-5cavbdjcta-ew.a.run.app/item/48339824)
3. [ShowHN- 追蹤 Hacker News 上的專案展示](https://showhn.buzzing.cc/)
4. [ShowHN:AISimulaionenBasedonFEP| Hacker News](https://news.ycombinator.com/item?id=48339824)
5. [nextjs-hackernews.vercel.app/item/48339824](https://nextjs-hackernews.vercel.app/item/48339824)