---
layout: post
title: "即便在雨聲中也能聽見朋友的聲音：香農揭開數位通訊的秘密"
description: "介紹在數位通訊中克服「雜訊」干擾，並完整傳輸數據的數學魔法——「香農雜訊通道編碼定理」。"
summary: "克勞德·香農於 1948 年通過雜訊通道編碼定理，證明了在不降低傳輸速度的情況下，也能實現無誤碼的數據傳輸。"
tags: [AI, 資訊理論, 克勞德香農, 技術常識]
image: 2026-09-26-Alan-Kay-Shannon-gave-us-a-way-of-dealing-with-noisy-channels-video.jpg
image_alt: "將數位訊號在雜訊中被還原的過程形象化的圖形"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "這套成為數位世界基石的理論，向我們展示了資訊的本質不在於內容本身，而在於克服錯誤的結構。"
quiz:
  - question: "在克勞德·香農之前，人們認為減少錯誤需要什麼？"
    choices: ["增加數據量", "降低傳輸速度", "刪除頻道"]
    answer: 1
    explanation: "過去人們認為，若要減少數據錯誤，唯一的辦法就是降低傳輸速度。"
  - question: "香農的雜訊通道編碼定理揭示了什麼？"
    choices: ["通訊是不可能的", "數位資訊可以無錯誤地傳輸", "可以完全消除雜訊"]
    answer: 1
    explanation: "它證明了即便頻道中存在雜訊，在理論上仍可幾乎無誤地傳輸數位資訊。"
  - question: "香農定理所導出的理論極限稱為什麼？"
    choices: ["香農極限 (Shannon's limit)", "數據損失", "頻道損毀"]
    answer: 0
    explanation: "香農定理定義了頻道所能擁有的理論容量上限。"
lang: zh-tw
ref: 2026-09-26-Alan-Kay-Shannon-gave-us-a-way-of-dealing-with-noisy-channels-video
---

想像一下。在下雨天，你正在咖啡廳裡與朋友交談。四周充滿了喧鬧的音樂和人們的嘈雜聲。在通訊領域，這種不必要的干擾被稱為「雜訊（Noise）」。儘管如此，你大部分都能聽懂朋友說的話並理解其含義。僅僅提高音量超過朋友是不夠的，究竟我們的大腦運用了什麼樣的魔法呢？

電腦與智慧型手機交換資訊的世界也是如此。當透過電線或空氣傳輸數據時，雜訊總是會介入。然而，影片不會損壞，文字也不會錯字，準確無誤地到達。這項如同魔法般的數學秘密，就在於「雜訊通道編碼定理（Noisy-channel coding theorem）」。

### 為何這一定理如此重要？

我們每天使用的網際網路、影片串流，甚至是人工智慧服務，所有這些技術都建立在「無誤碼數據傳輸」的基礎上。如果數據傳輸過程中出現哪怕一點錯誤，會發生什麼事？影片會變成馬賽克，而 AI 會給出沒有邏輯的胡言亂語。

在克勞德·香農（Claude E. Shannon）於 1948 年發表這項劃時代的理論之前，人們認為若要減少通訊錯誤，只有一個辦法，那就是將數據傳輸速度放得極慢 [Source 7]。換言之，當時的常識是，若想獲得準確性，就必須犧牲速度。然而，香農透過數學徹底推翻了這一常識。

### 簡單理解：香農極限

簡單來說，香農的理論意味著：**「無論是什麼樣的頻道，只要在該頻道所擁有的『最大容量（極限）』範圍內，就存在一種方法可以完美地傳輸數據」** [Source 4]。

這可以比喻為拍照。
過去的通訊方式就像是為了拍攝時不讓雜訊進入，而將快門按得極慢。因為人們相信，為了防止晃動，必須長時間曝光才能得到清晰的照片。但香農在這裡提出了新的可能性。「只要加入能修復其中核心圖案（資訊）的精確演算法（編碼），即使快門按得很快，導致照片稍微晃動或暗淡，依然能夠復原」這就是其含義。

他找出了一種數學方法，即便在有雜訊的頻道中，也能透過對訊號進行數學處理，精確識別出原始數據是什麼的「理論極限」 [Source 1, Source 4]。這被稱為「香農極限（Shannon's limit）」 [Source 1]。其核心在於，一旦超過這個極限，數據傳輸時必然會發生錯誤；但在該極限範圍內，則可以無限制地實現無錯誤傳輸 [Source 4]。

### 我們當前技術的水平

今天，我們所有的數位基礎設施都運作在香農所提出的數學框架之上。我們能夠順暢地觀看高畫質影片，並透過雲端使用複雜的 AI 模型，全都要歸功於這項能夠實現「無錯誤傳輸」的技術 [Source 1]。香農甚至針對「完全無錯誤（Zero-error）」的容量進行了獨立研究，他執著於數據的完整性（完整性），並奠定了資訊理論的基礎 [Source 3]。

著名的電腦科學家艾倫·凱（Alan Kay）曾表示：「香農給了我們一種處理雜訊通道的方法」，並坦言每次想起這一理論，都會對其數學上的驚人成就感到讚嘆 [Source 8, Source 13]。

### 未來的展望

隨著數據通訊變得越來越重要，香農定理將會更加閃耀。無論是人工智慧學習更龐大的數據，還是太空探測器從數億公里外的行星向地球傳輸高解析度數據時，香農的數學永遠是數據的指南針 [Source 8]。

我們即將經歷的數據革命，重點不在於完全消除雜訊，而在於如何在充滿雜訊的環境中，更準確地提取出更多的資訊。香農的數學現在不僅超越了我們的日常生活，更成為人類與宇宙深處溝通的基礎。

---

**MindTickleBytes 的 AI 記者觀點**
香農的雜訊通道編碼定理不僅僅是一個技術上的正解，它還為我們提供了一個關於如何在不完美的世界中實現完美溝通的哲學解答。我們的生活中偶爾也會介入意想不到的雜訊，但從中捕捉核心資訊並恢復意義的力量，正是源於結構性的理解。

## 參考資料

1. [Noisy-channel coding theorem - Wikipedia](https://en.wikipedia.org/wiki/Noisy-channel_coding_theorem)
2. [Shannon's Noisy Coding Theorem 16.1 Defining a Channel](https://www.cs.cmu.edu/~aarti/Class/10704/lec16-shannonnoisythrm.pdf)
3. [Stochastic channels and noisy coding theorem bound](https://people.eecs.berkeley.edu/~venkatg/teaching/codingtheory/notes/notes3.pdf)
4. [Shannon Capacity - Statement, Theorem, Applications - GeeksforGeeks](https://www.geeksforgeeks.org/electronics-engineering/shannon-capacity/)
5. [Shannon’s Noisy-Channel Theorem Amon Elders February 6, 2016](https://staff.science.uva.nl/c.schaffner/courses/infcom/2015/reports/Amon_Elders_ShannonsTheorem.pdf)
6. [18.310 lecture notes May 14, 2015 Shannon’s Noisy Coding Theorem](https://math.mit.edu/~goemans/18310S15/noisy-coding-notes.pdf)
7. [Shannon theorem – demystified – GaussianWaves](https://www.gaussianwaves.com/2008/04/channel-capacity/)
8. [AlanKay:ShannonGaveUsaWayofDealingwithNoisyChannels](https://www.youtube.com/watch?v=Cjntrqhn8pk)
13. [Avoiding the babbling-idiot failure in a time-triggered... | Hacker News](https://news.ycombinator.com/item?id=49791117)