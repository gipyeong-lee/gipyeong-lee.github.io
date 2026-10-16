---
layout: post
title: "AI 製作的代碼管理系統，是否剽竊了原作者的技術？"
description: "我們將探討圍繞 Anthropic 發布的新版本控制系統 'Scion' 所引發的剽竊爭議，以及開源生態系統中的倫理問題。"
summary: "Anthropic 的新版本控制系統 'Scion' 被指控未經授權盜用了 Meta 開源項目 'Mononoke' 的設計，引發了業界的強烈不滿。"
tags: [AI, Anthropic, 開源, 倫理, Scion]
image: 2026-10-16-More-on-Anthropics-Scion-ripping-off-Mononoke.jpg
image_alt: "一名開發者在寫滿代碼的螢幕前露出複雜的神情"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "開源精神的核心在於共享與貢獻。為了技術效率而抹殺原作者功績的行為，可能會為技術生態系統的信任帶來災難性的先例。"
quiz:
  - question: "此次爭議的核心，Anthropic 發布的系統名稱是什麼？"
    choices: ["Sapling", "Bonsai", "Scion"]
    answer: 2
    explanation: "Anthropic 近期發布了全新的版本控制系統 'Scion'。"
  - question: "Scion 被指控剽竊了誰的技術？"
    choices: ["Google", "Meta", "OpenAI"]
    answer: 1
    explanation: "Scion 被指控剽竊了 Meta 所開發的開源原始碼控制伺服器 'Mononoke' 的設計。"
  - question: "Scion 與 Mononoke 被指出的共同技術特徵是什麼？"
    choices: ["數據壓縮", "衍生數據 (derived data) 結構", "雲端儲存"]
    answer: 1
    explanation: "Scion 被批評幾乎照搬了 Mononoke 的 '衍生數據' 架構與 'Bonsai' 變更集概念。"
lang: zh-tw
ref: 2026-10-16-More-on-Anthropics-Scion-ripping-off-Mononoke
---

想像一下：你花了幾年時間苦思冥想，精心製作了一份美味的食譜，並私下向朋友展示了它。然而幾天後，這位朋友卻彷彿是自己研發的一樣，用這份食譜參加烹飪比賽並贏得了獎項。更過分的是，他沒有提到食譜真正的來源——也就是你，而是隨手借用了自己認識的另一位知名廚師的名字。如今 AI 業界正在發生的爭議，與此如出一轍。

近期，人工智慧公司 Anthropic 發布了全新的版本控制系統「Scion」，隨即引發了激烈的剽竊質疑。批評者認為這不僅僅是製作了類似的系統，而是直接將其他公司花費心血研發並開源公開的技術佔為己有。究竟業界發生了什麼事？

## 這為什麼很重要？

版本控制系統（Version Control System，一種記錄與管理程式碼修改歷史的工具）對開發者而言，就像是「時光機」。當程式碼修改出現問題時，它可以回復至之前的狀態，並且仔細記錄下誰在何時修改了哪些部分，是核心工具。儘管 Anthropic 自誇其開發的 Scion 系統極具效率，但開發者社群對此反應相當冷淡。

這個問題之所以被嚴正看待，是因為它直接觸及了「開源生態系統的倫理」。開源精神建立在「共享」之上，讓任何企業或個人都能自由使用並貢獻技術。然而，如果大型 AI 公司在運用他人的開源技術時，不給予應有的功績認可，或是刻意隱瞞來源，未來誰還願意辛苦研發技術並公開給世界使用？這可能會成為腐蝕整個技術生態信任體系的危險先例 [[參考資料 16](https://kongchang.com/en/articles/anthropic-s-scion-accused-of-ripping-off-mononoke-sparking-open-source-controversy)]。

## 淺顯易懂：什麼是「衍生數據」？

打個比方，想像圖書館的管理系統。除了書籍的位置資訊外，還會將「誰在何時借走」、「哪些書正在出借中」等資訊整理成額外的清單，我們稱之為「衍生數據 (derived data，為了系統效率，從原始數據中衍生出的附加資訊)」。

Meta 自 2017 年至 2018 年間，開發了一套能有效管理這些衍生數據，進而實現極速查詢程式碼修改歷史的「Mononoke」系統，並將其開源公開 [[參考資料 15](https://daily.dev/posts/more-on-anthropic-s-scion-ripping-off-mononoke-cjser6bvj), [參考資料 17](https://news.lavx.hu/article/anthropic-s-scion-version-control-system-draws-heavily-from-mononoke-design-without-attribution)]。然而，此次 Anthropic 的 Scion 被指控幾乎完美複製了 Mononoke 的架構與被稱為「Bonsai」的變更集（changeset，將程式碼變更事項打包的單位）概念 [[參考資料 15](https://daily.dev/posts/more-on-anthropic-s-scion-ripping-off-mononoke-cjser6bvj), [參考資料 19](https://www.aipulse.it/en/news/anthropic-scion-mononoke-derived-data-design-629367)]。就連確認程式碼作者的工作（blame）等技術細節，也與 Mononoke 的方式極為相似 [[參考資料 8](https://sunshowers.io/posts/anthropic-mononoke/), [參考資料 21](https://alobbs.com/post/2026-10-14/)]。

Anthropic 在解釋自家系統時，雖然提到了另一個名為「Sapling」的系統並給予讚譽，卻對原版 Mononoke 隻字未提 [[參考資料 15](https://daily.dev/posts/more-on-anthropic-s-scion-ripping-off-mononoke-cjser6bvj), [參考資料 19](https://www.aipulse.it/en/news/anthropic-scion-mononoke-derived-data-design-629367)]。特別是後來傳出當初參與 Mononoke 開發的人員已轉職至 Anthropic，這讓「剽竊」而非「參考」的指控更具說服力 [[參考資料 15](https://daily.dev/posts/more-on-anthropic-s-scion-ripping-off-mononoke-cjser6bvj)]。

## 當前情況：AI 寫出的程式碼？

更令人驚訝的是，Scion 並非由人類親手編寫，而是由 AI（LLM，大型語言模型）所生成。據報導，Scion 在短短 5 個月內便透過 AI 完成了生產化 [[參考資料 15](https://daily.dev/posts/more-on-anthropic-s-scion-ripping-off-mononoke-cjser6bvj)]。業界憂心忡忡，認為 AI 在學習既有的開源數據過程中，可能直接獲取了技術核心架構，亦或是此過程模糊了版權的界線。

目前，技術專家們正針對 AI 公司是否妥善遵守了開源授權規定（如 GPL 等），以及企業研發技術時應遵守的最低倫理底線，展開激烈辯論 [[參考資料 16](https://kongchang.com/en/articles/anthropic-s-scion-accused-of-ripping-off-mononoke-sparking-open-source-controversy)]。

## 未來會如何發展？

此次爭議將成為 AI 企業在研發技術時，針對他人的設計究竟能「參考」到何種程度的重要先例。未來關於開源授權範圍的法律爭議將持續加劇，企業在往後公開技術或將產品商業化時，必須嚴格遵守對原作者的出處標註（attribution）義務 [[參考資料 16](https://kongchang.com/en/articles/anthropic-s-scion-accused-of-ripping-off-mononoke-sparking-open-source-controversy)]。

### MindTickleBytes AI 記者的觀點
技術的存在是為了提升世界的效率。但如果這種效率是建立在抹殺他人的正當努力之上，這還能稱之為真正的創新嗎？像 Anthropic 這樣的創新企業，越是在技術成就上卓越，越需要對技術生態保持尊重。希望此次事件能成為重拾開源珍貴價值，並確立透明技術共享文化的契機。

## 參考資料

1. [More on Anthropic's Scion ripping off Mononoke · sunshowers](https://sunshowers.io/posts/anthropic-mononoke-2/)
2. [Anthropic's Scion is heavily inspired by Mononoke · sunshowers](https://sunshowers.io/posts/anthropic-mononoke/)
3. [More on Anthropic's Scion ripping off Mononoke | HotON.ai](https://hoton.ai/tr/news/more-on-anthropic-s-scion-ripping-off-mononoke-doabr1)
4. [More on Anthropic's Scion ripping off Mononoke - daily.dev](https://daily.dev/posts/more-on-anthropic-s-scion-ripping-off-mononoke-cjser6bvj)
5. [Anthropic's Scion Accused of Ripping Off Mononoke, Sparking Open Source Controversy](https://kongchang.com/en/articles/anthropic-s-scion-accused-of-ripping-off-mononoke-sparking-open-source-controversy)
6. [Anthropic's Scion Version Control System Draws Heavily From Mononoke Design without Attribution](https://news.lavx.hu/article/anthropic-s-scion-version-control-system-draws-heavily-from-mononoke-design-without-attribution)
7. [More on Anthropic's Scion ripping off Mononoke | Better HN](https://bhn.pajecawav.dev/post/50106738)
8. [Anthropic's Scion Accused of Copying Meta's Mononoke Design](https://www.aipulse.it/en/news/anthropic-scion-mononoke-derived-data-design-629367)
9. [Anthropic's Scion intentionally ripped · Hacker News | Zeli](https://zeli.app/story/50106738)
10. [2026-10-14 Briefing - alobbs.com](https://alobbs.com/post/2026-10-14/)