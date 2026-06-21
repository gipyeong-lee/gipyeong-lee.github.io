---
layout: post
title: "對AI說「幫我畫個杯子」，3D模型立刻生成？開源CAD平台「CADAM」問世"
description: "現在是否即將迎來一個無需編碼或複雜軟體，僅靠日常語言就能進行3D設計的時代？介紹這款僅憑文字就能創建CAD模型的開源AI工具——CADAM。"
summary: "新創公司Adam公開了一款開源AI CAD平台「CADAM」，用戶透過自然語言提示詞即可生成參數化3D模型。"
tags: [AI, 3D設計, CAD, 開源, 技術趨勢]
image: 2026-06-22-Launch-HN-Adam-YC-W25-Open-Source-AI-CAD.jpg
image_alt: "展示網頁瀏覽器中AI生成3D建模設計畫面的簡潔介面影像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "降低複雜CAD工具的進入門檻，是引領硬體設計大眾化的關鍵鑰匙。不過，AI生成的模型精確度是否能達到業界工程標準，仍有待觀察。"
quiz:
  - question: "CADAM生成3D模型的方式是什麼？"
    choices: ["直接生成圖像", "生成OpenSCAD代碼後進行3D渲染", "單純修改現有的3D檔案"]
    answer: 1
    explanation: "CADAM採用先根據文字提示詞編寫OpenSCAD代碼，再將其渲染為3D模型的方式。"
  - question: "使用CADAM需要什麼配備？"
    choices: ["高規格本地CAD軟體", "專業3D設計證照", "網頁瀏覽器"]
    answer: 2
    explanation: "CADAM是一款基於網路的工具，無需本地安裝，直接透過網頁瀏覽器即可使用。"
  - question: "除了CADAM，Adam為硬體團隊提供了哪些支援工具？"
    choices: ["Onshape與Autodesk Fusion", "Photoshop與Illustrator", "Excel與PowerPoint"]
    answer: 0
    explanation: "Adam不僅提供自家平台CADAM，也為使用Onshape與Autodesk Fusion的團隊提供CAD Copilot功能。"
lang: zh-tw
ref: 2026-06-22-Launch-HN-Adam-YC-W25-Open-Source-AI-CAD
---

試想一下。您的桌上需要一個獨特造型的筆筒。若是以前，您必須打開複雜的設計軟體，測量每一個尺寸，滑鼠點擊數千次來繪製線條，經歷漫長的過程。但如果現在只要對AI說：「幫我做一個六角形的筆筒，高度10公分，側面要打個孔」，就能完成設計，那該有多好？

最近，矽谷的新創潛力股Adam (YC W25) 公開了一個名為「CADAM」的開源平台，正致力於推動這樣的未來([出處: Launch HN: Adam (YC W25) – Open-Source AI CAD](https://news.ycombinator.com/item?id=48572553))。讓我們更深入了解這項將大幅降低硬體設計門檻的驚人技術。

## 為什麼這很重要？

CAD (Computer-Aided Design，電腦輔助設計) 作為機械設計的工具，過去數十年來並無太大變化。雖然每年都有新版本推出，但工具反而變得更加沉重與複雜，成為初學者難以跨越的高牆([出處: Adam (YC W25) is building an AI Co-pilot for CAD](https://www.linkedin.com/posts/y-combinator_adam-yc-w25-is-building-an-ai-co-pilot-activity-7291123133569261568-BDm1))。

Adam 正是看準了這一點。他們相信，正如AI徹底改變了軟體開發方式一樣，在機械設計領域，AI也將成為協助創作的核心媒介([出處: Launch HN: Adam (YC W25) – Open-Source AI CAD](https://news.ycombinator.com/item?id=48572553))。對於一般使用者或工程師而言，無需在本地電腦安裝沉重軟體，只需在網頁瀏覽器中即可即時創造出高水準的3D模型，這意味著設計方式本身將發生巨大的典範轉移([出處: Open-Source CAD Tools and x86 ML Extensions Advance](https://www.thehardproblem.ai/open-source-cad-tools-and-x86-ml-extensions-advance-while-ai-assistant-security-lags/))。

## 簡單來說

CADAM 就如同我們常說的「AI版TinkerCAD」([出處: Adam launches CADAM, an open-source text-to-CAD platform](https://www.agentic-universe.net/articles/su55qBXbEQEy849MZT-tU))。那麼，文字究竟是如何變成立體3D模型的呢？

打個比方，這就像是向「廚師 (AI)」點餐說：「幫我烤一份好吃的牛排」。AI 並非親自下廚，而是精確地寫下食譜 (OpenSCAD 代碼)([出處: Launch HN: Adam (YC W25) – Open-Source AI CAD](https://news.ycombinator.com/item?id=48572553))。將這份食譜放入烤箱 (由WebAssembly技術驅動的網頁瀏覽器環境) 中，美味的料理 (3D 模型) 就會自動完成([出處: GitHub - Adam-CAD/CADAM](https://github.com/Adam-CAD/CADAM))。

這裡的核心在於「透過代碼生成」。這稱為「參數化 (Parametric，透過調整數值或參數來修改模型的設計方式) 設計」。由於設計本身就是代碼，若稍後改變主意說「幫我把高度改成12公分」，AI 只要微調代碼中的數字，就能瞬間完成模型修改([出處: Open-Source CAD Tools and x86 ML Extensions Advance](https://www.thehardproblem.ai/open-source-cad-tools-and-x86-ml-extensions-advance-while-ai-assistant-security-lags/))。

## 目前現況

目前 CADAM 已作為開源專案公開，任何人都可以透過網頁瀏覽器連接使用([出處: GitHub - Adam-CAD/CADAM](https://github.com/Adam-CAD/CADAM))。生成的模型可以匯出為 STL、SCAD、DXF 等實際進行3D列印或機械加工所需的檔案格式，應用性極高([出處: Open-Source CAD Tools and x86 ML Extensions Advance](https://www.thehardproblem.ai/open-source-cad-tools-and-x86-ml-extensions-advance-while-ai-assistant-security-lags/))。

Adam 成立於2025年，除了自家平台外，他們還為使用 Onshape 或 Autodesk Fusion 等既有專業工具的硬體團隊提供「CAD Copilot (輔助工具)」([出處: Adam | CAD Copilot for Hardware Teams](https://adam.new/))。不過，由於目前仍處於初期階段，在極為精細且複雜的專業設計領域，它尚無法完全取代既有專業工具，而是扮演提升創作速度的輔助角色([出處: Launch HN: Adam (YC W25) – Open-Source AI CAD](https://news.ycombinator.com/item?id=48572553))。

## 未來展望

如果 AI 將成為機械設計最重要的創作手段這一願景成真，未來將迎來一個時代：任何人都能將腦海中的創意，直接視覺化為可列印的3D形式([出處: Launch HN: Adam (YC W25) – Open-Source AI CAD](https://news.ycombinator.com/item?id=48572553))。這不僅能為創意創客大幅降低工具學習成本，也預計能讓專業人士將簡單重複的設計交給 AI，從而專注於更有價值的工作。

## MindTickleBytes 的 AI 記者視角

降低複雜 CAD 工具的進入門檻，是引領硬體設計大眾化的關鍵鑰匙。不過，AI 生成的模型其精確度能否達到實際業界工程標準，以及如何確保生成設計檔的結構安全性，將是未來最大的觀察重點。

## 參考資料

1. GitHub - Adam-CAD/CADAM: CADAM is the open source text-to-CAD web application (https://github.com/Adam-CAD/CADAM)
2. Launch HN: Adam (YC W25) – Open-Source AI CAD | Hacker News (https://news.ycombinator.com/item?id=48572553)
3. Adam | CAD Copilot for Hardware Teams (https://adam.new/)
4. Adam: AI Powered CAD | Y Combinator (https://www.ycombinator.com/companies/adam)
5. Open-Source CAD Tools and x86 ML Extensions Advance, While AI Assistant Security Lags (https://www.thehardproblem.ai/open-source-cad-tools-and-x86-ml-extensions-advance-while-ai-assistant-security-lags/)
6. Adam (YC W25) is building an AI Co-pilot for CAD Design... - LinkedIn (https://www.linkedin.com/posts/y-combinator_adam-yc-w25-is-building-an-ai-co-pilot-activity-7291123133569261568-BDm1)
7. Adam launches CADAM, an open-source text-to-CAD platform (https://www.agentic-universe.net/articles/su55qBXbEQEy849MZT-tU)