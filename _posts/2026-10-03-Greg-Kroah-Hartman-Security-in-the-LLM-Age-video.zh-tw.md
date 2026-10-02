---
layout: post
title: "AI 發送的安全性報告，現在真的可以相信嗎？"
description: "Linux 核心安全性專家 Greg Kroah-Hartman 暢談 AI 與開源安全性的現況與未來。"
summary: "Linux 核心核心開發者 Greg Kroah-Hartman 評估 AI 編寫的安全性報告品質已大幅提升，並針對開源生態系統中 AI 的應用表達了審慎且務實的觀點。"
tags: [AI, Linux, 安全性, 開源, 技術趨勢]
image: 2026-10-03-Greg-Kroah-Hartman-Security-in-the-LLM-Age-video.jpg
image_alt: "Linux 安全性專家 Greg Kroah-Hartman 在舞台上進行演講"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 現在已不再只是簡單的雜訊，而是開始提供有價值的見解。但在安全性領域，技術效率與人類負責任的審查之間的精確平衡，比什麼都重要。"
quiz:
  - question: "Greg Kroah-Hartman 對於 AI 生成的修補程式（Patch）採取什麼樣的態度？"
    choices: ["積極歡迎所有 AI 修補程式", "預先拒絕驅動程式/預備（Staging）區域中由 AI 生成的修補程式", "選擇性地自動核准 AI 修補程式"]
    answer: 1
    explanation: "他在 Linux 核心驅動程式與預備區域中，會預先拒絕所有標示為 AI 編寫的修補程式。"
  - question: "Greg 對於 AI 編寫的安全性報告有何最新評價？"
    choices: ["品質依然低落，毫無用處", "相比過去，報告品質有了劇烈的改善", "遠比人類編寫的報告更出色"]
    answer: 1
    explanation: "他評價在過去一個月內，AI 生成的漏洞報告品質已大幅提升，不再是所謂的「垃圾（slop）」。"
  - question: "Greg Kroah-Hartman 實驗的 'clanker' 分支主要目的是什麼？"
    choices: ["讓 AI 重寫整個 Linux 核心", "透過 AI 輔助的模糊測試工具找出實際的錯誤", "取代開源貢獻者"]
    answer: 1
    explanation: "clanker 分支是一項使用 AI 輔助模糊測試工具，識別核心內部 ksmbd 及 SMB 程式碼等實際錯誤的實驗。"
lang: zh-tw
ref: 2026-10-03-Greg-Kroah-Hartman-Security-in-the-LLM-Age-video
---

試著想像一下。有一個巨大的數位圖書館，每天都有數萬人瀏覽。圖書館的書籍是由全球無數志工親手一字一句編寫並維護的。然而，從某一天開始，圖書館管理員身邊出現了一位名叫「AI（人工智慧）」的秘書，開始為書籍尋找錯誤。起初，這位秘書只會胡言亂語，但現在，它已經能帶來相當像樣的錯誤報告了。

如果這個圖書館正是全球幾乎所有伺服器與 Android 智慧型手機的心臟——「Linux 核心（Linux Kernel，連接電腦硬體與軟體的核心程式）」呢？站在這個重要領域中心的關鍵人物 Greg Kroah-Hartman，最近分享了關於 AI 與安全性的有趣見解。

## 為何這很重要？

Linux 核心是現代 IT 世界的基礎。從我們使用的智慧型手機到網際網路服務，沒有 Linux 就無法運作。因此，Linux 的安全性直接與我們每個人的安全性掛鉤。過去，尋找程式碼安全性漏洞的工作是熟練開發者的專利。但隨著 AI 正式進入該領域，安全性報告的產生速度與方式已徹底改變。這不僅僅是開發者工具的更迭，更是在要求我們針對「如何確保每天使用的數位裝置之安全性」這一問題，給出全新的答案。

## 簡單說明 (The Explainer)

簡單來說，將檢查程式碼的過程比喻為「照片 App 的濾鏡」如何？過去的 AI 在檢查照片時，使用過度的濾鏡，常把不相關的污點硬說是 Bug。專家 Greg 將此稱為「垃圾 (slop)」。但在過去一個月內，這個濾鏡變得非常精準。現在它已經能出色地篩選出照片中真正的塵埃了 [參考 2](https://www.theregister.com/2026/03/26/greg_kroahhartman_ai_kernel), [參考 10](https://prohoster.info/en/blog/novosti-interneta/greg-kroa-hartman-rasskazal-chto-llm-stali-luchshe-iskat-oshibki)。

Greg 透過一個稱為「clanker」的分支，進行了一項 AI 輔助工具實際在 Linux 核心特定部分（如 ksmbd 等）找出 Bug 的實驗 [參考 4](https://itsfoss.com/news/linux-drivers-staging-ai-rejection/), [參考 9](https://ajitbala.com/while-torvalds-makes-peace-with-ai-in-linux-greg-kroah-hartman-draws-a-line-sort-of/)。這意味著 AI 不僅僅在寫作，更達到了能指出複雜系統邏輯錯誤的水準。就像是一個剛起步的實習生，開始能像 10 年資歷的專家一樣準確地找出文件中的錯字。

比喻來說，過去的 AI 安全工具就像是一個會搖晃圖書館所有書籍並製造混亂的暴力吸塵器，而現在則變成了拿著放大鏡、準確找出角落積塵的細心管理員。

## 當前局勢 (Where We Stand)

Greg Kroah-Hartman 是一位自 2005 年起就活躍於 Linux 核心安全性團隊的資深專家 [參考 6](https://hosted-files.sched.co/osskorea2026/a7/4+-+Greg+-+oss_korea+v2.pptx.pdf), [參考 8](https://hosted-files.sched.co/osfflondon2026/b1/GKH+Keynote.pdf)。他對於 AI 提供的資訊堅持「信任但要驗證」的立場。

儘管 AI 寫報告寫得很好，但他對於 AI 直接修改並寄來的「修補程式（Patch）」則採取極其嚴格的態度。他採取了一項預先拒絕政策，針對在 Linux 驅動程式與預備區域中，明確標示由 AI 編寫的修補程式 [參考 11](https://www.thenextgentechinsider.com/posts/torvalds-softens-ai-stance-in-linux-kroah-hartman-draws-cautious-line)。為什麼呢？因為程式碼不僅僅是為了實現功能，還必須考慮與整個系統的協調。AI 雖然精通程式碼文法，但並不完美理解 Linux 核心這個巨大生態系統整體的哲學。這就像是一個深諳食譜的機器人，卻無法考量人的口味與當天的氛圍一樣。

## 未來展望

未來 AI 將成為安全性領域中替代人類雙眼、強而有力的助手。然而，Greg 的行為帶給我們重要的啟示。無論 AI 產出的結果看起來多麼合理，最終責任依然在於人類專家。今後，開源生態系統將持續就「如何有效處理 AI 提出的無數安全性報告」以及「如何安全地融入 AI 編寫的程式碼」進行激烈討論。

## AI 的觀點 (AI's Take)

以 MindTickleBytes 的 AI 記者觀點來看，Greg 的態度並非「技術懷疑論」，而是「技術洞察力」。AI 已經超越了單純的學習模型，進化為智慧型秘書，但在安全性這種重視信任的領域中，他也提醒了我們「人類的判斷力」依然是最後一道安全性防線的事實。比起沈迷於技術效率，他努力守護人類應負擔的「最後責任領域」，這是技術健康發展不可或缺的過程。

## 參考資料

1. [Keynote: Linux in the Land of LLMs - Greg Kroah-Hartman](https://www.youtube.com/watch?v=_MwMLPmMccs)
2. [Linux kernel czar says AI bug reports aren't slop anymore - The Register](https://www.theregister.com/2026/03/26/greg_kroahhartman_ai_kernel)
3. [Greg Kroah-Hartman – Open Source Security Foundation](https://openssf.org/tag/greg-kroah-hartman/)
4. [While Torvalds Makes Peace With AI in Linux, Greg Kroah-Hartman Rejects AI Patches](https://itsfoss.com/news/linux-drivers-staging-ai-rejection/)
5. [LLMs and the kernel security process - Netdev 0x1A](https://netdevconf.info/0x1A/sessions/keynote/llms-and-the-kernel-security-process.html)
6. [4 - Greg - oss_korea v2](https://hosted-files.sched.co/osskorea2026/a7/4+-+Greg+-+oss_korea+v2.pptx.pdf)
7. [Kernel Recipes 2026 - Security in the LLM age - YouTube](https://www.youtube.com/watch?v=NnV_cWeoo5Q)
8. [Untitled presentation - hosted-files.sched.co](https://hosted-files.sched.co/osfflondon2026/b1/GKH+Keynote.pdf)
9. [While Torvalds Makes Peace With AI in Linux, Greg Kroah-Hartman Draws a Line](https://ajitbala.com/while-torvalds-makes-peace-with-ai-in-linux-greg-kroah-hartman-draws-a-line-sort-of/)
10. [Greg Kroah-Hartman said that LLMs have become better at finding bugs - ProHoster](https://prohoster.info/en/blog/novosti-interneta/greg-kroa-hartman-rasskazal-chto-llm-stali-luchshe-iskat-oshibki)
11. [Torvalds Softens AI Stance in Linux; Kroah-Hartman Draws Cautious Line](https://www.thenextgentechinsider.com/posts/torvalds-softens-ai-stance-in-linux-kroah-hartman-draws-cautious-line)