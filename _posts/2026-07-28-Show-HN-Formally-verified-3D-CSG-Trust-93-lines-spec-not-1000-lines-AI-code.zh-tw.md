---
layout: post
title: "AI 寫的 1,000 行程式碼值得信賴嗎？93 行的「正道」才是答案"
description: "與其逐一檢查 AI 生成的複雜程式碼，我們介紹一種最新的軟體工程方法：透過驗證極短且完美的設計圖（規格）來確保信任。"
summary: "不再依賴 AI 生成的龐大程式碼，而是透過驗證包含核心功能的 93 行精確設計圖來提升軟體可靠性，探討最新的開發趨勢。"
tags: [AI, 軟體工程, 程式設計, CSG, 形式驗證]
image: 2026-07-28-Show-HN-Formally-verified-3D-CSG-Trust-93-lines-spec-not-1000-lines-AI-code.jpg
image_alt: "複雜的 3D 幾何圖形結合的模樣，背後顯現出極短程式碼作為信任的象徵"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "面對越複雜的問題，真正的技術進步不在於增加程式碼行數，而是在於專注於定義本質的「形式化規格」。"
quiz:
  - question: "驗證 AI 生成程式碼的最新工程方法，其核心是什麼？"
    choices: ["同時使用更多的 AI 模型", "增加逐行的人工程式碼審查", "對精簡且完美的設計圖（規格）進行形式驗證"]
    answer: 2
    explanation: "最新的方法不是逐一檢查數千行的 AI 程式碼，而是透過形式驗證包含核心規則的簡短規格來確保信任。"
  - question: "3D 建模中使用的「CSG（Constructive Solid Geometry）」技術定義為何？"
    choices: ["將簡單的照片轉換為 3D", "透過結合基本幾何圖形或進行差集運算等方式建立複雜 3D 物件的方法", "單純繪製 2D 草圖的工具"]
    answer: 1
    explanation: "CSG 是將基本幾何圖形（Primitive）作為葉節點，並將聯集（Union）或交集（Intersection）等作為節點，以樹狀結構來表現 3D 物件。"
  - question: "軟體開發中「形式驗證（Formal Verification）」的目的是什麼？"
    choices: ["為了更快地編寫程式碼", "為了從數學上保證程式碼的正確性", "為了讓 AI 變得更聰明"]
    answer: 1
    explanation: "形式驗證是透過嚴格的限制條件和數學邏輯，確保軟體能完全按照設計正確運作的過程。"
lang: zh-tw
ref: 2026-07-28-Show-HN-Formally-verified-3D-CSG-Trust-93-lines-spec-not-1000-lines-AI-code
---

想像一下，你正準備用 3D 列印機印製一個非常複雜的零件。這個零件的設計圖太過複雜，人工檢查相當困難。你請 AI 幫忙繪製，它隨即產生了超過 1,000 行的程式碼。你會 100% 信任這些程式碼並直接按下列印按鈕嗎？

隨著 AI 撰寫軟體時代的到來，比「如何寫出好的程式碼」更重要的課題，變成了「如何信任這些程式碼」。今天，我們將介紹一種最新的技術途徑：不再盲目信任 AI 的複雜程式碼，而是僅憑 93 行精確的設計圖來保障軟體的安全性。

### 為什麼這很重要？

過去，當 AI 幫我們寫程式碼時，人類會嘗試逐行閱讀以找出錯誤。但若程式碼量超過數千行，這項工作實際上是不可能的，很容易遺漏關鍵錯誤。如果軟體是用於 3D 建築或精密機械設計等容錯率極低的領域，這可能會導致嚴重的事故。[Don’t ReviewAICode.VerifyIt. - YouTube](https://www.youtube.com/watch?v=sClTAvkQDOU)

這項技術將範式從「逐一確認 AI 生成的程式碼」轉變為「證明其通過既定規則（規格）」。即使人類不審查所有程式碼，只要有數學上精確的短小設計圖，就能保障安全性。

### 輕鬆理解：料理食譜與形式驗證

為了理解這項技術，我們先看看 **CSG（Constructive Solid Geometry，構成實體幾何學）** 的概念。CSG 是一種將極其簡單的幾何圖形（立方體、圓柱體等）像樂高積木一樣堆疊、重疊或裁切，以建立複雜 3D 形狀的方式。[Constructive solid geometry - Wikipedia](https://en.wikipedia.org/wiki/Constructive_solid_geometry)

這就像我們在照片修圖應用程式中套用多層濾鏡一樣。單一濾鏡很簡單，但結合多個後就能產生精彩的結果。在 3D 世界中，應用將基本圖形合併、重疊與裁切的規則，也能建立複雜的 3D 物件。

然而，如果這些「結合規則」由人類編寫，難免會出現失誤。因此，開發者們近期製作了 **「93 行核心規格」**。[Formally verified 3D mesh intersection - GitHub](https://github.com/schildep/verified-3d-mesh-intersection)

這是一個稱為 **形式驗證（Formal Verification）** 的過程。用以下例子比喻就很容易理解：做菜時，不是先放入 100 種調味料後再逐一檢查味道，而是將「鹽一小撮、糖兩小撮」這種準確的食譜事先驗證得盡善盡美。一旦證明食譜在數學上是正確的，其餘複雜的烹飪過程只需遵循該食譜即可，從而顯著減少錯誤。

### 現狀

目前的開發現場正透過這種方式實現複雜功能。事實上，在一個專案中，開發者利用形式驗證函式庫，僅花了約 8 小時就成功完成了控制並驗證 AI 生成程式碼的自動化過程。[ShowHN:Formallyverifiedpolygon intersection – Opus... -HNDebrief](https://hndebrief.com/2026-06-04/show-hn-formally-verified-polygon-intersection-opus-48-oneshots-prev-failed)

以往開發者必須熬夜審查 AI 寫出的 1,000 多行程式碼，現在只需將不到 100 行的「標準答案」輸入到形式驗證工具中，就能獲得信任。不過，這項技術雖然在要求極高精度的工程領域極為強大，但在製作一般網頁或輕量級應用時，仍存在時間與成本消耗較大的「高階技術」侷限。

### 未來展望

未來，我們使用的 AI 工具將會越來越聰明。它們將不僅僅是寫程式碼，還將發展成能自行驗證所寫程式碼在數學上是否合理的 AI。[Linear– The system for product development](https://linear.app/)

以後你可能不再需要直接審查程式碼，而是透過一個問題來判斷軟體的安全性：「這個 AI 生成的成果是否通過了 93 行形式化規格的驗證？」。信任的標準正在從「人類的眼睛」轉移到「數學證明」。

### MindTickleBytes 的 AI 記者觀點
盲目信任 AI 生成結果的時代已經結束。技術越是複雜，我們越應該專注於更簡單、強大的本質（規格），這起案例證明了這一事實。歸根究底，駕馭聰明工具的方法並非「確認更多」，而是「定義得更準確」。

## 參考資料
1. [Don’t ReviewAICode.VerifyIt. - YouTube](https://www.youtube.com/watch?v=sClTAvkQDOU)
2. [Constructive solid geometry - Wikipedia](https://en.wikipedia.org/wiki/Constructive_solid_geometry)
3. [Formally verified 3D mesh intersection - GitHub](https://github.com/schildep/verified-3d-mesh-intersection)
4. [ShowHN:Formallyverifiedpolygon intersection – Opus... -HNDebrief](https://hndebrief.com/2026-06-04/show-hn-formally-verified-polygon-intersection-opus-48-oneshots-prev-failed)
5. [Linear– The system for product development](https://linear.app/)