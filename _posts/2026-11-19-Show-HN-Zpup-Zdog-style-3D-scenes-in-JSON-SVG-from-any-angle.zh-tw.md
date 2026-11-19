---
layout: post
title: "僅憑 AI 與 JSON 就能做出 3D 圖形？停滯不前的 Zdog 現代化復活，Zpup 的故事"
description: "輕鬆了解 Zpup 專案的登場背景與 Zdog 的演進過程，它能在沒有 JavaScript 的情況下，僅靠 JSON 數據就能在網頁和 README 中顯示 3D 圖形。"
summary: "Zpup 能在沒有 JavaScript 的情況下將 JSON 轉換為平面 SVG，是克服了多年來被擱置的 Zdog 局限性的現代 3D 引擎。"
tags: [Zpup, Zdog, 3D圖形, SVG, JSON, 開源]
image: 2026-11-19-Show-HN-Zpup-Zdog-style-3D-scenes-in-JSON-SVG-from-any-angle.jpg
image_alt: "顯示電腦螢幕上的 JSON 程式碼與轉換後 3D SVG 圖形樣貌的簡潔插圖"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "無需複雜的 3D 引擎，就能在靜態環境中輕量實現 3D，這點非常具有吸引力。"
quiz:
  - question: "Zpup 在渲染結果中未使用的技術是什麼？"
    choices: ["SVG", "JSON", "JavaScript"]
    answer: 2
    explanation: "Zpup 在輸出檔案中不使用 JavaScript，因此也能在 img 標籤或 README 中運作。"
  - question: "與原有的 Zdog 引擎相比，Zpup 所改善的代表性功能是什麼？"
    choices: ["畫布渲染速度", "重疊圖形的排序（重疊處理）", "文字圖形支援"]
    answer: 1
    explanation: "Zdog 使用單一點對圖形進行排序，有小物件被遮擋的問題，而 Zpup 透過比較重疊的圖形解決了這個問題。"
  - question: "開發 Zpup 專案時所使用的工具是什麼？"
    choices: ["Claude Code Fable 5.2", "React Native", "Three.js"]
    answer: 0
    explanation: "Zpup 開發者使用 Claude Code Fable 5.2 來編寫此專案。"
lang: zh-tw
ref: 2026-11-19-Show-HN-Zpup-Zdog-style-3D-scenes-in-JSON-SVG-from-any-angle
---

想像一下。你正在撰寫部落格文章或 GitHub 的專案說明文件（README）。雖然你想在文件中加入很酷的 3D 立體圖形，但如果必須塞滿複雜的 JavaScript（在網頁瀏覽器中運作的程式語言）程式碼或載入笨重的 3D 程式，肯定會讓人頭痛欲裂。如果只要像一般圖片標籤那樣隨手丟進一個標籤，3D 圖形就能躍然紙上，那有多好？ 

最近，開發者社群 Hacker News 上出現了一個令人耳目一新、痛快解渴的有趣專案。這是一個名為 [Show HN: Zpup – Zdog style 3D scenes in JSON, SVG from any angle](https://github.com/rxolve/zpup) 的開源專案 [出處 1]。今天我們將來了解 Zpup，它能在沒有複雜 JavaScript 的情況下，僅靠 JSON（JavaScript Object Notation，用於儲存與交換資料的輕量級文字基底格式）資料就能建構出輕量的 3D 世界。

---

## 為什麼這很重要？

若要在網站或文件中加入 3D 圖形，通常需要龐大且複雜的 3D 引擎或大量的 JavaScript 程式庫。然而，這會使文件變得笨重，且在靜態（Static，無動態處理的固定狀態）文件環境中往往根本無法執行。 

Zpup 打破了這項限制。Zpup 接收定義了 3D 場景的 JSON 檔案，並將其轉換為可在任何相機角度下檢視的平面 SVG（Scalable Vector Graphics，不受解析度限制的向量式圖片格式）檔案 [出處 1，出處 9]。 

這裡最令人驚豔的是，**輸出檔案中完全不包含 JavaScript** [出處 1，出處 9]。簡單來說，就像書本上印刷的圖片一樣，因為沒有 JavaScript，所以即使在一般圖片標籤（`<img>`）或 GitHub 的 README 文件中，也能毫無問題地將 3D 圖形渲染得像活過來一樣 [出處 1，出處 9]。開發者無需進行複雜的設定，就能輕鬆地在文件或靜態網頁中加入 3D 視覺元素 [出處 9]。

---

## 輕鬆理解：Zdog 的遺產與 Zpup 的演進

為了便於理解，我們打個比方。使用極其精緻華麗的 3D 遊戲引擎，就像是在配備各種特殊設備的大型電影片場中拍攝智慧型手機短影音一樣，太過笨重與複雜。相對地，過去備受喜愛的「Zdog」引擎則像紙偶戲道具一樣輕巧且直覺。

### Zdog 的誕生與限制
Zdog 最初由一位名叫戴夫（Dave）的開發者所創建 [出處 11]。由於大多數現有的 3D 引擎過於強大且複雜 [出處 11]，他希望有一種工具能在沒有複雜開銷（Overhead，處理程式所需的額外資源）的情況下，設計並顯示簡單的 3D 模型 [出處 11]。Zdog 直接受到 P.F. Magic 於 1995 年發布的虛擬寵物遊戲 *Dogz* 的啟發 [出處 11，出處 12]。該遊戲在 3D 場景中使用平面的 2D 圓形精靈（Sprite，2D 圖形元素）來渲染模型 [出處 11，出處 12]。

然而，Zdog 也有令人遺憾的地方。多年來它一直被擱置，沒有發布新版本 [出處 1，出處 9，出處 10]。此外，Zdog 採用以單一點（Point）為基準對每個圖形進行排序的方式 [出處 1]。正因如此，當小物件放置在大地板上時，旋轉相機往往會導致小物件錯誤地藏在大地板後方，從而產生視覺錯誤 [出處 1]。

### Zpup 解決問題的方式
Zpup 自許為遭到擱置的 Zdog 的現代繼任者而登場 [出處 1，出處 9，出處 10]。開發者在公司進行小型專案時需要 3D，雖然對 Zdog 印象深刻，但由於長期沒有更新，便決定親自打造一個現代版本 [出處 1]。目前 Zpup 處於 0.2 版本階段，在沒有畫布渲染器或文字圖形的情況下保持輕量 [出處 1]。特別有趣的是，在開發過程中使用了 Claude Code Fable 5.2 [出處 1]。

比方說，如果說 Zdog 在對物件進行排序時僅粗略查看一個點來確定順序，那麼 Zpup 則會**仔細比較相互重疊圖形的區域**，以準確判斷哪個在前、哪個在後 [出處 1]。多虧了這一點，當旋轉畫面時，物件彼此混淆或遮擋的現象得到了完美解決 [出處 1]。

---

## 當前現狀：發展到什麼地步了？

目前 Zpup 已開發至 0.2 版本 [出處 1]，開發者們可以透過 GitHub 儲存庫與範例程式碼 [출처 10]，以及線上遊樂場（[https://rxolve.github.io/zpup](https://rxolve.github.io/zpup)）直接體驗其功能並分享回饋 [出處 1]。 

這項技術目前能做的事很明確：
- 讀取以 JSON 格式定義的輕量 3D 場景資料 [出處 1，出處 9]。
- 轉換為使用者期望的任何相機角度視圖 [出處 1，出處 9]。
- 輸出完全不包含 JavaScript 的乾淨平面 SVG 結果 [出處 1，出處 9]。
- 藉此可以直接插入標準圖片標籤或文件檔案（README 等）中 [出處 1，出處 9]。

另一方面，畫布渲染器或文字圖形等笨重功能被有意排除在外，因此比起製作龐大複雜的 3D 遊戲，它更適合用於將輕量的圖示、形狀、插圖等嵌入靜態文件中 [出處 1]。

---

## 未來會如何發展？

在網頁文件與開源生態系統中，「輕量」與「簡單」就是競爭力。如果不需要經過笨重的 JavaScript 執行環境，就能在靜態圖片標籤內靈活渲染 3D 立體圖形，那麼技術文件或作品集網站的表現力將會更加豐富。

承襲了停滯數年的 Zdog 情懷 [出處 1，出處 9，出處 10]，並結合 AI 時代的工具現代化重生的 Zpup [出處 1]，未來將為個人專案與開發者文件帶來什麼樣的視覺變化，值得我們拭目以待。

---

## MindTickleBytes 的 AI 記者視角

越是複雜的技術，有時往往在回歸最原始、輕量的形式時，普及之路才會真正開啟。Zpup 擺脫了龐大 3D 引擎的陰影，精準指出了開發者微小但切身的痛點：「難道不能更簡單、更輕量地把 3D 放進文件裡嗎？」JavaScript-free 3D SVG 的這個點子未來將會擴散到多少不同的網頁環境中，令人拭目以待。

---

## 參考資料

1. [Show HN: Zpup – Zdog style 3D scenes in JSON, SVG from any angle](https://github.com/rxolve/zpup)
2. [Zpup – Zdog-style 3D scenes in JSON rendered to SVG from any ...](https://kblip.com/products/zpup-zdog-style-3d-scenes-in-json-rendered-to-svg-from-any-IMbS3Cy)
3. [zpup/examples at main · rxolve/zpup · GitHub](https://github.com/rxolve/zpup/tree/main/examples)
4. [GitHub - metafizzy/zdog: Flat, round, designer-friendly ...](https://github.com/metafizzy/zdog)
5. [GitHub - IgorOffline/metafizzy-zdog: Flat, round, designer ...](https://github.com/IgorOffline/metafizzy-zdog)