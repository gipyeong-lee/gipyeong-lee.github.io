---
layout: post
title: "用AI像對話一樣寫程式？1978年的天才程式設計師曾警告過的「危險錯覺」"
description: "透過1978年艾茲赫爾·戴克斯特拉（Edsger Dijkstra）的敏銳洞察，探討為什麼像與人對話一樣使用自然語言來進行程式設計是危險的。"
summary: "電腦科學泰斗艾茲赫爾·戴克斯特拉早在1978年就強烈批判自然語言程式設計，認為其會瓦解精確的邏輯體系，並導致智力怠惰。"
tags: [程式設計, AI, 戴克斯特拉, 軟體工程]
image: 2026-10-23-The-foolishness-of-natural-language-programming-1978.jpg
image_alt: "一位程式設計師站在寫滿複雜符號的黑板前苦思。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "與戴克斯特拉的擔憂不同，現代基於大型語言模型（LLM）的程式設計雖然提供了便利，但「精確」這一根本價值，仍然取決於人類。"
quiz:
  - question: "艾茲赫爾·戴克斯特拉批評自然語言程式設計的最大原因是？"
    choices: ["自然語言的歧義性", "電腦效能不足", "使用者教育困難"]
    answer: 0
    explanation: "戴克斯特拉認為自然語言本質上具有歧義，不適合以「精確」為生命的電腦程式設計。"
  - question: "戴克斯特拉指出代表「自然語言歧義性」的單詞是什麼？"
    choices: ["和", "是 (to be)", "如果"]
    answer: 1
    explanation: "「是」同時包含「……的一部分」與「等於……」的意思，這可能會導致電腦混淆。"
  - question: "戴克斯特拉將對自然語言程式設計的依賴現象稱為什麼？"
    choices: ["新文盲", "智力懶惰", "邏輯跳躍"]
    answer: 0
    explanation: "他將其稱為「新文盲 (The New Illiteracy)」並發出強烈警告。"
lang: zh-tw
ref: 2026-10-23-The-foolishness-of-natural-language-programming-1978
---

想像一下。你對 AI 說：「幫我整理一下這些資料。」過去可能需要一行一行編寫複雜的程式碼，現在卻變成了像與人對話一樣，下達指令就結束的世界。我們認為這就像魔法般的技術進步。然而，四十多年前，該領域的一位傳奇電腦科學家早已預見並發出了警告。他將此稱為「新文盲（The New Illiteracy）」。

### 為什麼這很重要？

如今我們生活在一個「AI 代勞所有程式設計」的時代。僅用「自然語言 (Natural Language，人類日常使用的語言)」下達指令就能產出結果，確實非常方便。然而，當我們越習慣 AI 的便利，就越逐漸遺忘電腦為什麼會這樣運作，以及什麼是邏輯上的精確性。1978 年艾茲赫爾·W·戴克斯特拉 (Edsger W. Dijkstra) 所寫的論文 [On the foolishness of "natural language programming"](https://www.cs.utexas.edu/~EWD/transcriptions/EWD06xx/EWD667.html) 在今日依然發出擲地有聲的警示。 [參考資料 5, 參考資料 6, 參考資料 11, 參考資料 14]

### 淺顯易懂：為什麼自然語言不適合用於程式設計？

戴克斯特拉認為自然語言不是精確思考的「盟友」，反而是「敵人」。 [參考資料 6]

打個比方，日常對話就像「套了滿滿濾鏡的照片」。我們對朋友說「把那個拿來」，透過上下文就能心領神會是什麼東西。但電腦就像「沒有任何濾鏡、超高解析度的鏡頭」。只要指令輸入稍微模糊一點，就很容易抓到錯誤的資料。

戴克斯特拉以「是 (to be)」這個動詞作為代表性的例子。 [參考資料 14] 韓文的「~이다」或英文的「is」有兩種含義。既有「哲秀是學生（……的一部分）」的意思，也有「哲秀是兇手（等於……）」的意思。我們人類可以透過上下文區分，但電腦在邏輯上可能會混淆這兩個截然不同的命令。因此，他核心的主張是：電腦程式設計絕對需要一種排除這種歧義，像 0 與 1 一樣明確的「形式符號 (Formal Symbolism)」。 [參考資料 1, 參考資料 2, 參考資料 14]

### 現狀：在便利與精確之間走鋼索

當然，當今的人工智慧模型與過去的自然語言程式設計相比，在規模與精確度上早已不可同日而語。 [參考資料 9] 然而，戴克斯特拉的擔憂在今天看來依然一針見血。他批判自然語言程式設計的趨勢，終究是在助長使用者的「智力懶惰」，並將程式設計所要求的必要訓練與精確性腐蝕殆盡，這是一種「愚蠢的行為 (foolishness)」。 [參考資料 12]

我們現在生活在「感覺程式設計 (Vibe Coding，憑感覺寫程式)」的時代，但如果失去了自行判斷 AI 生成的程式碼為何會出錯的能力，這或許真的會變成一個「新文盲」的時代。 [參考資料 6, 參考資料 7]

### 未來會如何發展？

技術會持續進步，但我們必須銘記一點：AI 能理解自然語言，並不代表程式設計變成了「可以不用那麼精確」的工作。就算未來有一天 AI 能完美理解我們的所有指令，電腦依然只在人類輸入的邏輯體系內運作。無論是使用自然語言還是使用符號，程式設計的本質是「準確且精確的邏輯實作」，戴克斯特拉的教誨在未來也絕不會改變。

---

### MindTickleBytes 的 AI 記者觀點

戴克斯特拉的尖銳批判就像是來自 1978 年的警告信。在我們享受將程式設計委託給 AI 的便利同時，或許該回頭檢視：我們是否正在喪失邏輯嚴謹性這一基礎體力。我們絕不能忘記工具越先進，使用者的基本功就必須越紮實的真理。

---

## 參考資料

1. [On the foolishness of "natural language programming"](https://www.cs.utexas.edu/~EWD/transcriptions/EWD06xx/EWD667.html)
2. [On the foolishness of "natural language programming"](https://www.cs.utexas.edu/~EWD/transcriptions/EWD06xx/EWD667.html?fileGuid=H2TBGtSx56EjErDS)
3. [On the foolishness of "natural language programming"](https://research.tue.nl/en/publications/on-the-foolishness-of-natural-language-programming/)
4. [Dijkstra Called It in 1978: Natural Language Programming Is Still ...](https://www.daita.io/en/blog/dijkstra_natural_language_programming/)
5. [PDF On the foolishness of "natural language programming"](https://link.springer.com/content/pdf/10.1007/BFb0014656.pdf)
6. [On Natural Language Programming – @dsyme on software](https://dsyme.net/2025/08/27/on-natural-language-programming/)
7. [On the foolishness of "natural language programming"](https://research.tue.nl/en/publications/on-the-foolishness-of-natural-language-programming)
8. [Of course. EWD 1008, titled "On the foolishness of 'natural language.....](https://pastebin.com/Kd5PARvB)
9. [Dijkstra on foolishness of Natural Language Programming](https://daily.dev/posts/dijkstra-on-foolishness-of-natural-language-programming-tzpv24mqa)
10. [Ten months ago, I published an article by Edsger W. Dijkstra from 1978...](https://www.linkedin.com/posts/sdalbera_ten-months-ago-i-published-an-article-by-activity-7427226210809745408-JEZv)