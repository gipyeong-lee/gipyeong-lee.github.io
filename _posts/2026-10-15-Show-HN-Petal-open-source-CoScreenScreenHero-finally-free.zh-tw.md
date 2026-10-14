---
layout: post
title: "程式高手們懷念的「那個工具」回來了：Petal 的故事"
description: "這是一個專為取代廣受開發者懷念的螢幕共享工具 Screenhero 而推出的開源軟體 Petal。"
summary: "為您介紹開源螢幕共享工具『Petal』，它讓遠端同事彷彿坐在同一張桌子前進行程式開發。"
tags: [AI, 開發工具, 開源, 協作, 遠端工作]
image: 2026-10-15-Show-HN-Petal-open-source-CoScreenScreenHero-finally-free.jpg
image_alt: "兩位開發者身處不同地點，卻同時看著同一個畫面進行協作的想像圖。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "協作工具的開源化，是防止因特定企業關閉服務而導致數據與技術中斷的最健康趨勢。"
quiz:
  - question: "開發者認為「真正結對程式設計（Pair Programming）」的螢幕共享工具有什麼特徵？"
    choices: ["只是單純顯示畫面", "多人可以同時操控滑鼠游標", "檔案傳輸速度快"]
    answer: 1
    explanation: "真正的結對程式設計工具不僅是觀看畫面，還具備多位使用者能同時擁有各自的滑鼠游標並操作畫面的特徵。"
  - question: "過去深受開發者喜愛的結對程式設計工具「Screenhero」消失的原因為何？"
    choices: ["沒有使用者", "被 Slack 收購後終止服務", "因為付費政策"]
    answer: 1
    explanation: "Screenhero 曾是非常受歡迎的工具，但在被 Slack 收購後終止了服務，令許多開發者感到遺憾。"
  - question: "新推出的 Petal 採取了哪種營運模式？"
    choices: ["付費訂閱服務", "開源專案", "封閉式雲端服務"]
    answer: 1
    explanation: "Petal 是以任何人都能參與貢獻與使用的開源專案形式公開。"
lang: zh-tw
ref: 2026-10-15-Show-HN-Petal-open-source-CoScreenScreenHero-finally-free
---

想像一下。您必須與遠在國外的同事共同修正一段複雜的程式碼。直到現在，我們通常會開啟視訊會議軟體，分享螢幕後大喊：「不是那裡，是右邊！啊，等一下，讓我切換滑鼠操作權」，搞得手忙腳亂。

如果有人能像真的坐在你電腦前一樣，出現第二個滑鼠游標，並且能像在身旁對話般自然地共同撰寫程式碼，那該有多好？過去在開發者圈中被視為傳奇的協作體驗，現在不僅能重現，甚至還是「免費」的。這就是全新的開源工具——**Petal** 的故事。

## 為什麼這很重要？

在遠端工作成為常態的時代，「結對程式設計（Pair Programming，指兩位開發者共用一台電腦進行協作的方式）」對於開發效率至關重要，即便雙方不在同一個物理空間，也能像坐在隔壁一樣工作。

然而，過去我們常用的視訊會議軟體的螢幕共享功能都是「單向」的。結構上，通常是一個人呆呆地看著螢幕，由另一個人操控。這種隔閡是阻礙創意協作的一堵大牆。過去曾有一款名為 **Screenhero** 的工具完美解決了這種遺憾，但在被 Slack 收購後服務被迫終止，導致無數開發者頓失依靠 [[關於 Screenhero 的 DEV Community 文章](https://dev.to/chovy/i-built-an-open-source-screenhero-replacement-for-real-pair-programming-1b98)]。

Petal 重新銜接了這種「斷裂的協作」。它不是隨時會因特定企業政策而消失的付費服務，而是以任何人都能共享並共同發展的開源形式回歸，這對使用者而言意義重大。

## 輕鬆理解

為了讓你輕鬆理解 Petal，我們可以打個比喻。

如果傳統的螢幕共享工具像是「電視節目」，我們只能觀看播放中的畫面，無法直接修改或更換內容。而 Petal 這類工具則像是「放在同一張桌子上的同一張紙與兩支筆」。兩個人可以同時在紙上寫字、擦拭或畫圖。

在技術上，這有時被稱為「雙滑鼠游標（Dual Mouse Cursor）」 [[Screenhero 土耳其語介紹](https://huntscreens.com/tr/products/screenhero)]。也就是說，它建立了一種環境，讓對方的滑鼠游標能像活的一樣，在我的螢幕上即時移動並自由操作。Petal 以「低延遲（Low Latency，反應速度極快，幾乎沒有卡頓）」與「高解析度（High Resolution，畫面非常清晰）」實現了這種環境，提供了彷彿坐在隔壁辦公般的沉浸感 [[Petal 官方網站](https://petal.live/)]。

## 進展到什麼程度了？

目前，Petal 作為一個開源專案，已經邁出了堅實的步伐。它不僅僅是共享畫面，還提供了強大的遠端操控對方電腦的功能，在開發者群體中引起了極大期待 [[Petal 官方網站](https://petal.live/)]。

但這一切才剛剛開始。與過去傳奇工具 Screenhero 所擁有的高完成度相比，Petal 能否穩定處理大量開發者的需求，還有待觀察。特別是技術協作工具對穩定性要求極高，目前正有許多開源貢獻者投入心力，致力於提升其穩定性。

## 未來會如何發展？

隨著 Petal 這類開源工具的普及，遠端工作團隊的協作方式將會更加精緻。不僅是程式設計，在設計、文件撰寫等各個領域，「同步操作」功能極有可能成為標準配備。

最重要的轉變在於「工具的所有權」。過去像 Screenhero 那樣，一旦公司終止服務，所有人就無法繼續使用；但現在，透過開源，任何人都能維持並改進這項技術 [[關於 Screenhero 的 DEV Community 文章](https://dev.to/chovy/i-built-an-open-source-screenhero-replacement-for-real-pair-programming-1b98)]。Petal 將在遠端協作從「單純的視訊會議」演變為「實質的共同作業」過程中扮演核心角色。你的工作環境，或許很快也會隨之改變。

## AI 的觀點
螢幕共享工具從「廣播」演變成「共同作業桌」的過程，展現了數位協作的本質。這提醒了我們，技術應追求的方向不在工具本身，而在於能將人與人之間的距離縮短到什麼程度。協作工具的開源化，是防止因特定企業關閉服務而導致數據與技術中斷的最健康趨勢。

## 參考資料

1. Petal—OpenSourcePair Programming, https://petal.live/
2. I Built anOpenSourceScreenheroReplacement... - DEV Community, https://dev.to/chovy/i-built-an-open-source-screenhero-replacement-for-real-pair-programming-1b98
3. Screenhero: Herkese Ekranınızı Paylaşın, Herkes Kontrolü Elde Etti, https://huntscreens.com/tr/products/screenhero