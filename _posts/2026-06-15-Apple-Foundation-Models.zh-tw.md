---
layout: post
title: "我的 iPhone 大腦是如何運作的？Apple 基礎模型 (AFM) 終極指南"
description: "輕鬆了解 Apple Intelligence 的核心——Apple 基礎模型 (AFM) 是什麼，以及如何在保護個人隱私的同時，使用快速且聰明的 AI。"
summary: "Apple 將在裝置端運行的超高速小型 AI 與具備嚴密安全性的雲端 AI 結合，在保護隱私的同時，完成了強大且獨立的 AI 生態系統。"
tags: [Apple, AI, AppleIntelligence, 基礎模型, 隱私, 技術原理]
image: 2026-06-15-Apple-Foundation-Models.jpg
image_alt: "iPhone 裝置與雲端伺服器透過安全的發光線條連接，彼此交換數據並勾勒出大腦形狀的畫面"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "打破了人工智慧必須龐大且浩瀚的偏見，Apple 專注於「個人日常」與「嚴密安全」這兩個最重要價值的聰明設計，表現得相當出色。"
quiz:
  - question: "在 Apple 智慧型手機裝置內部（裝置端）直接運行的語言模型，其參數（可調整的數值）規模大約是多少？"
    choices: ["約 300 萬個", "約 30 億個", "約 200 億個"]
    answer: 1
    explanation: "Apple 的裝置端模型擁有針對 Apple 晶片最佳化的約 30 億個 (3B) 參數，因此能快速且在離線狀態下高效運作。"
  - question: "下列何者最能比喻 Apple 基礎伺服器模型所採用的「混合專家 (MoE)」架構？"
    choices: ["一個大腦從頭到尾獨自處理所有運算的模式", "將所有電腦電源始終開啟並保持待機的模式", "病患來時，由服務台精準地只將其轉介給所需專科醫師的綜合醫院系統"]
    answer: 2
    explanation: "混合專家 (MoE) 模式是一種從 200 億個龐大參數中，僅啟用最符合請求的 10 億到 40 億個參數，從而將效率與速度最大化的架構。"
  - question: "下列關於 Apple 基礎模型 (AFM) 的敘述，何者有誤？"
    choices: ["Google 的 Gemini 技術作為核心引擎被深度整合其中。", "具備能處理文字以及音訊、圖片等多種形式資訊的多模態能力。", "開發者可透過 Swift 框架，僅用幾行程式碼便將 AI 功能加入應用程式中。"]
    answer: 0
    explanation: "Apple 高層明確表示，這次全新 Apple 基礎模型架構中「完全沒有 (none)」包含 Google 的 Gemini 技術。"
lang: zh-tw
ref: 2026-06-15-Apple-Foundation-Models
---

想像一下，在繁忙的上班早晨，您甚至沒有點亮 iPhone 螢幕，只是對著口袋裡的智慧型手機隔空說道：「把主管昨天用電子郵件寄來的專案時程摘要一下，加到我的行事曆裡。然後傳訊息給團隊成員，說我已經確認過時程了。」

接著，智慧型手機會默默讀取您的電子郵件內容，打開行事曆 App 將行程一一記錄，再透過訊息 App 以親切的語氣發送回覆給團隊成員。就像一位能徹底理解您生活中所有脈絡、精準認知螢幕上狀況，並自然地穿梭於各個 App 之間的能幹私人助理。能實現這種驚人體驗的 Apple 智慧系統，正是「Apple Intelligence」。[來源標題](https://developer.apple.com/apple-intelligence/) 

那麼，這位如此聰明行動的助理腦中，究竟裝了什麼樣的大腦？過去只會快速計算的智慧型手機，是怎麼變成能聽懂我的話，甚至代替我採取行動的呢？今天 MindTickleBytes 將為大家深入淺出地剖析這項在 Apple 裝置心臟地帶安靜卻又極其強大跳動著的技術——**「Apple 基礎模型 (Apple Foundation Models, AFM)」**，讓您讀完後也能輕鬆向朋友解釋。

---

## 這為什麼重要？ (Why It Matters)

最近人工智慧業界的流行趨勢可以說是「量級之爭」。所有焦點都集中在誰能打造出更龐大得誇張的大腦，也就是超大型 AI。然而，要在我們每天握在手中的智慧型手機或輕薄筆電上完整運行如此巨大的大腦，在物理上幾乎是不可能的。如果硬要運行，電池不到 10 分鐘就會瞬間耗盡，裝置也會變得像暖暖包一樣燙手。

這裡提到的基礎模型 (Foundation Model)，指的並非只擅長一兩項特定工作，而是指受過龐大數據訓練、能廣泛執行語言翻譯、摘要、推理等多種任務的多用途人工智慧的「基礎體力」。為了克服智慧型手機的限制，Apple 並未選擇直接拿其他公司巨大骨架來用的捷徑。直到最近，關於 Apple 裝置是否會採用 Google 技術的猜測依然滿天飛，但 Apple 高層斷然劃清界線，表示全新的 Apple 基礎模型中「完全沒有 (none)」包含 Google 的 Gemini 技術。[來源標題](https://www.macrumors.com/2026/06/09/apples-new-ai-contains-no-gemini/)、[來源標題](https://macdailynews.com/2026/06/09/new-apple-foundation-models-contain-none-of-googles-gemini-assistant/)、[來源標題](https://www.ithinkdiff.com/apple-foundation-models-built-with-google/)

Apple 如此堅持採用獨自開發的大腦，在我們平凡的日常中具有非凡的意義。這正是為了同時達成**「絕對的隱私保障」**與**「無需等待的任務處理」**這兩個目標。

過去許多人工智慧服務，都採用將使用者的問題無條件傳送到龐大網際網路伺服器，在那裡完成運算後再將答案傳回來的模式。如此一來，我私密的日記內容、重要的公司文件、個人的家庭照片脈絡，都會被傳送到某間公司龐大的伺服器深處，這種不安心感實在難以抹滅。然而，Apple 制定了混合式策略，將直接在裝置本身運行的「裝置端 (On-device) 模型」與在安全性受嚴密控管的專屬伺服器上運行的「雲端模型」相結合。這提出了一個新時代的標準：在確保個人隱私安全留在手機內的同時，也能完整享受 AI 帶來的便利。

---

## 輕鬆理解 (The Explainer)

要理解 Apple 基礎模型的運作方式，把它比喻為我們大腦的**「快速反射神經」**與**「深度思考區域」**就非常容易了。Apple 完美地劃分了這兩種角色，並進行了細膩的設計，以確保不會干擾到我們的日常生活。

### 1. 裝置內部敏捷的大腦：30 億個旋鈕調節器

在您的 iPhone 或 Mac 裡，住著一個只為您一人 24 小時待命工作的小型 AI。Apple 建構了一個擁有約 30 億個 (3B) 參數規模的裝置端語言模型，該模型針對 Apple 自行設計的 Apple 晶片 (Apple Silicon) 進行了最佳化，以發揮最高效率。[來源標題](https://machinelearning.apple.com/research/introducing-apple-foundation-models)、[來源標題](https://machinelearning.apple.com/research/apple-foundation-models-tech-report-2025)、[來源標題](https://machinelearning.apple.com/research/apple-foundation-models-2025-updates) 

這裡的參數 (Parameter)，可以想成是人工智慧透過學習所獲得的「可調整數值」，或者是「連接腦細胞的突觸」。您可能對 30 億這個數字沒有什麼概念，打個比方，想像您的智慧型手機裡裝了一個**帶有 30 億個微小旋鈕的巨大烤箱**。當「幫我摘要昨天的會議紀錄」這個問題材料放進烤箱時，在眨眼瞬間，30 億個旋鈕就會喀喀喀地調整到各自的位置，烘烤出最完美摘要的美味答案。這等同於大約韓國總人口數的 60 倍的旋鈕，在您的掌心中瞬間轉動。

為了將這個巨大的烤箱塞進薄薄的智慧型手機裡，Apple 使用了驚人的壓縮魔法。具代表性的技術便是「2 位元量化感知訓練 (2-bit quantization-aware training)」與「KV-快取共享 (KV-cache sharing)」這種創新的架構。[來源標題](https://machinelearning.apple.com/research/apple-foundation-models-tech-report-2025) 

這些詞彙看起來有點複雜，但簡單來說原理是這樣的：為了把一整座超大國家圖書館的書本塞進小小的 USB 隨身碟裡，我們保留了文字所包含的核心意義，只將空白處的大小或墨水濃度等不必要的細節資訊壓縮到極致（量化）。此外，每次讀書時不是每次都從第 1 頁重新讀起，而是聰明地重複使用寫有重要核心摘要的虛擬便利貼（KV-快取），以便快速掌握上下文。多虧了這些技術，即使在完全沒有網路連線的飛機上或隧道裡，我們的手機也能以令人眼花撩亂的速度回答問題。

### 2. 雲端上的巨型綜合醫院：私有雲端運算 (Private Cloud Compute)

那麼，如果我們要求它解答裝置內小型 AI 難以應付的複雜數學題，或是完整分析數百頁的文件，會發生什麼事呢？就在裝置的大腦即將超載之前，Apple Intelligence 會將您想問的核心問題安全打包，安靜且迅速地傳送到 Apple 的伺服器。

但是，這時所使用的伺服器與一般的雲端伺服器在本質上有著天壤之別。Apple 將這個巨大的伺服器模型，運行在一個僅由自家晶片 (Apple Silicon) 驅動的**「私有雲端運算 (Private Cloud Compute)」**這個銅牆鐵壁般的安全堡壘上。進入這個堡壘的您的數據，會在作業完成、答案傳回的瞬間不留痕跡地蒸發，絕對不會被永久儲存，也不會與包含 Apple 在內的任何人分享。[來源標題](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models)、[來源標題](https://machinelearning.apple.com/research/introducing-apple-foundation-models)

住這個安全堡壘伺服器裡的人工智慧非常龐大。近期公開的第三代基礎模型 (AFM 3 Core Advanced) 擁有多達 200 億個參數。[來源標題](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models) 不過，這裡有一個驚人的效率反轉。那就是為了回答一個問題，它並不會每次都一口氣轉動所有的 200 億個旋鈕。

Apple 在這個巨大的伺服器模型中，應用了「交錯式全域-區域注意力機制 (Interleaved global-local attention)」以及「基於混合專家 (Mixture-of-Experts, MoE) 的並列軌道 (PT-MoE)」等稀疏 (sparse) 運算技術。[來源標題](https://machinelearning.apple.com/research/apple-foundation-models-tech-report-2025) 

打個比方，這個巨大的 AI 的運作方式，就和**聚集了各領域頂尖專家的最尖端綜合醫院**一模一樣。當病患（使用者的複雜問題）推開醫院大門進來時，非常聰明的服務台（路由器）會迅速掃描症狀。接著，它不會把在醫院待命的 200 位醫師全部叫到同一個地方，而是精準地只呼叫正好需要的 10 到 40 位皮膚科專科醫師和內科專科醫師來解決問題。

實際上，這個有 200 億個參數的模型，在每次收到請求時並不會喚醒自己整個大腦，而是選擇性地只點亮（啟用）所需的 10 億到 40 億個參數來使用。[來源標題](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models) 多虧如此，在不浪費大量電力的同時，更建構了讓使用者完全無需等待，便能快速獲得最高品質專家解答的架構。

---

## 目前現況 (Where We Stand)

目前 Apple 基礎模型已經遠遠超越了單純打字交換文字的程度。由共 5 個模型陣容所組成的這個龐大智能家族，在初期皆接受了理解世界的共通基礎體力訓練。在那之後，它們配合各自特化的職業進行深度學習，進化成了能同時理解並處理音訊（聲音）、圖片視覺理解、長篇語境的邏輯推理、高品質圖片生成等多種形式資訊，展現其多模態（Multimodal，同時使用多種感官的能力）能力的 AI。[來源標題](https://9to5mac.com/2026/06/11/apples-new-foundation-models-explained-on-device-ai-cloud-ai-and-everything-in-between/) 

特別是透過近期的大幅更新，這些基礎語言模型現在被設計為能熟練理解並自然支援 15 個國家的語言。其運用工具自如的能力，以及按部就班解決難題的推理能力，也有了飛躍性的提升。[來源標題](https://machinelearning.apple.com/research/apple-foundation-models-2025-updates) 

此外，它並非堅持在所有情況下都使用一個沉重且遲鈍的萬能模型，而是有專精於特殊職業的小型模型在背後可靠地支援。例如，在訊息 App 中能為使用者隨興想像畫出有趣圖片的擴散模型 (Diffusion model)，或是開發者在稱為 Xcode 的專業程式中開發 App 時，能自動幫忙編寫程式碼的程式編寫專用模型，也都是這個龐大基礎模型家族的一員。[來源標題](https://machinelearning.apple.com/research/introducing-apple-foundation-models)

不過，我們最能深刻感受到的巨大改變，莫過於能豐富 iPhone 生態系統的**「開發者體驗改善」**了。過去，開發者若想在自己製作的平凡 App 中加入優秀的 AI 助理，必須花費高昂的費用依賴雲端模型；但現在，他們可以隨心所欲地取用裝置內已安裝好、由 Apple 提供的小巧聰明模型來加以活用。[來源標題](https://sivabalanb.medium.com/exploring-apple-foundation-models-for-developer-workflows-37c72ec81cf0) 為此，Apple 向大眾公開了全新以 Swift 為中心的「基礎模型框架 (Foundation Models Framework)」。[來源標題](https://developer.apple.com/documentation/FoundationModels)、[來源標題](https://developer.apple.com/ios/whats-new/) 

這個框架（為了讓開發變得更容易而預先寫好的程式碼工具箱）到底有多方便呢？開發者只需輸入幾行程式碼，就能在 App 中立刻啟動語言理解或複雜結構化工作模型的會話。[來源標題](https://habr.com/ru/articles/1047288/) 甚至還有一個叫做 `Prompt` 的功能，開發者不用寫生硬的電腦語言，只要用我們平常使用的日常語言輸入字串，例如 `Prompt("為這個劇本段落建立最佳化的圖片生成提示詞")`，人工智慧就能立刻聽懂並給出出色的結果。[來源標題](https://grokipedia.com/page/Prompt_Apple_Foundation_Models)

更令人驚訝的是，連「LoRA 適配器微調 (LoRA adapter fine-tuning)」這樣的高階技術，也只需幾行程式碼便能提供。[來源標題](https://arxiv.org/pdf/2507.13575) 這就好比訓練一隻優秀的導盲犬。我們不是把已經完美完成基本服從與引導訓練的聰明狗狗（基礎模型）帶回家，然後從「坐下、起立」開始完全重新教起；取而代之的是，我們只需像為牠背上一個輕便背包（適配器）一樣，輕鬆迅速地教會牠「去我們家冰箱拿藍色的飲料」這項特定才藝。透過這項技術，開發者無需重新訓練整個沉重的 AI，便能瞬間打造出完全符合自己 App 性質的客製化 AI 助理。

---

## 未來將會如何？ (What's Next)

未來，Apple 基礎模型將會在 iPhone、Mac、iPad 等裝置內部的深處，進一步極大化其解讀使用者語境與情況的能力。它將精準認知螢幕上目前顯示的內容（螢幕感知能力，On-screen awareness），並在您無需親自用手指觸控的情況下，自由穿梭於各個 App 之間代替您執行動作 (App actions)，預計將奠定其作為完美綜合智慧的地位。[來源標題](https://developer.apple.com/apple-intelligence/)

想像一下即將到來的未來日常。當我在通訊軟體畫面上和朋友聊到即將到來的濟州島旅行時，我只要用說的指示：「AI，把我們剛才提到的住宿加到明天的行程裡，然後找一下附近的餐廳評論，摘要在備忘錄中。」接著，AI 就會自行判斷對話的脈絡找出住宿名稱，打開地圖 App 搜尋餐廳，然後自動操作行事曆 App 和備忘錄 App，為我寫好一份完美的旅遊計畫表。 

這些令人驚嘆甚至起雞皮疙瘩的所有助理角色，都在不讓我的個人隱私外洩一滴點的情況下，安全地在裝置內部完成。這將很快成為我們即將迎來的理所當然的日常。

---

## AI 的視角 (AI's Take)

**MindTickleBytes 的 AI 記者視角：**
現代人工智慧業界曾被一個巨大的偏見所支配。那就是「人工智慧模型必須體積龐大且參數浩瀚，才會聰明且有用」的信念。然而，Apple 漂亮地打破了這種盲目的信念，專注於「個人日常中的效率」與「絕對的隱私保護」這兩個與使用者生活最密切相關的實質價值。 

即使在雲端準備了具備數百億個參數的龐大智慧，平時也不會盲目浪費電力來運作它。只有在需要時，才像綜合醫院的專科醫師一樣選擇性呼叫特定部位的效率；加上日常提問完全依賴在裝置內快速且安全運作的 30 億個聰明反射神經——這樣的發想是驚人地聰明且實用。能夠在不將自己絕對不想讓別人看到的掌中日記本和相簿秘密交給他人的情況下，僱用到世界上最強大且聰明的助手。這正是 Apple 基礎模型平靜卻又堅定地描繪出的真正人工智慧未來。

---

## 參考資料

1. [Prompt (Apple Foundation Models)](https://grokipedia.com/page/Prompt_Apple_Foundation_Models)
2. [AppleIntelligence -AppleDeveloper](https://developer.apple.com/apple-intelligence/)
3. [ExploringAppleFoundationModelsfor Developer Workflows | Medium](https://sivabalanb.medium.com/exploring-apple-foundation-models-for-developer-workflows-37c72ec81cf0)
4. [Applereveals new AIfoundationmodelsbuilt with Google](https://www.ithinkdiff.com/apple-foundation-models-built-with-google/)
5. [Apple's New AIModelsContain 'None' of... - MacRumors](https://www.macrumors.com/2026/06/09/apples-new-ai-contains-no-gemini/)
6. [NewAppleFoundationModelscontain 'none' of Google's Gemini...](https://macdailynews.com/2026/06/09/new-apple-foundation-models-contain-none-of-googles-gemini-assistant/)
7. [LLM на iPhone: от llama.cpp доFoundationModels/ Хабр](https://habr.com/ru/articles/1047288/)
8. [Introducing the Third Generation of Apple’s Foundation Models - Apple Machine Learning Research](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models)
9. [Introducing Apple’s On-Device and Server Foundation Models - Apple Machine Learning Research](https://machinelearning.apple.com/research/introducing-apple-foundation-models)
10. [Apple Intelligence Foundation Language Models Tech Report 2025 - Apple Machine Learning Research](https://machinelearning.apple.com/research/apple-foundation-models-tech-report-2025)
11. [Apple’s new Foundation Models explained: on-device AI, cloud AI, and everything in between](https://9to5mac.com/2026/06/11/apples-new-foundation-models-explained-on-device-ai-cloud-ai-and-everything-in-between/)
12. [Foundation Models | Apple Developer Documentation](https://developer.apple.com/documentation/FoundationModels)
13. [Updates to Apple’s On-Device and Server Foundation Language Models - Apple Machine Learning Research](https://machinelearning.apple.com/research/apple-foundation-models-2025-updates)
14. [Apple Intelligence Foundation Language Models Tech Report 2025 Apple](https://arxiv.org/pdf/2507.13575)
15. [What’s New - iOS -AppleDeveloper](https://developer.apple.com/ios/whats-new/)