---
layout: post
title: "替我移動滑鼠的 AI 助手？Google 'Gemini 2.5 Computer Use' 全解析"
description: "介紹 Google 發佈的 Gemini 2.5 Computer Use 模型。我們將深入淺出地解釋 AI 如何像人類一樣觀察螢幕、點擊並自動化執行任務的原理，以及這將為我們的生活帶來的改變。"
summary: "Google 的 'Gemini 2.5 Computer Use' 是一項讓 AI 能夠直接移動滑鼠、輸入鍵盤，並代為處理複雜網頁工作任務的技術。"
tags: [Gemini, Google AI, AI代理人, 辦公自動化]
image: 2026-04-16-Introducing-the-Gemini-25-Computer-Use-model.jpg
image_alt: "分析電腦螢幕並操作滑鼠游標的 AI 代理人概念圖"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "現在，AI 已不僅僅是對話的對象，而是正在演變成能夠替我們操作實際工具的稱職助手。"
quiz:
  - question: "Gemini 2.5 Computer Use 模型為了執行任務，最先採取的行動是什麼？"
    choices: ["直接修改程式碼", "拍攝螢幕截圖進行分析", "向使用者提問"]
    answer: 1
    explanation: "該模型透過 '代理人迴圈' 先獲取螢幕截圖以掌握狀況，然後再決定後續行動。"
  - question: "該模型是基於哪款現有模型的視覺與推理能力而開發的？"
    choices: ["Gemini 1.0 Pro", "Gemini 1.5 Flash", "Gemini 2.5 Pro"]
    answer: 2
    explanation: "Gemini 2.5 Computer Use 是基於 Gemini 2.5 Pro 強大的視覺理解與推理能力所設計的。"
  - question: "關於該模型性能的描述，下列何者正確？"
    choices: ["反應速度比競爭模型慢", "在網頁及行動端控制基準測試中超越了競爭對手", "目前還無法使用需要登入的網站"]
    answer: 1
    explanation: "Gemini 2.5 Computer Use 在多項性能指標上領先競爭對手，其特點是延遲時間非常低。"
lang: zh-tw
ref: 2026-04-16-Introducing-the-Gemini-25-Computer-Use-model
---

想像一下。您在下班路上拿出智慧型手機，隨口說一句：「幫我預訂下週去濟州島旅行最便宜的雙人機票。」接著 AI 就會直接進入航空公司網站選擇日期，比較數十家航空公司的價格，並根據您的個人資訊自動填寫預訂表格。這已不再僅僅是建議您「如何預訂」，而是 AI 直接操作您的電腦滑鼠和鍵盤來完成工作的時代正拉開序幕。

Google 於 2025 年 10 月 7 日公開了 **「Gemini 2.5 Computer Use」**，這是一款能像人類一樣操作電腦的特殊 AI 模型 [介紹 Gemini 2.5 Computer Use 模型](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-computer-use-model/) [Google 發佈 Gemini 2.5 Computer Use AI 模型預覽版...](https://gigazine.net/gsc_news/en/20251008-google-gemini-2-5-computer-use)。這項技術正準備徹底改變我們與電腦互動的範式。

## 為什麼這很重要？

到目前為止，我們遇到的 AI 主要是擅長「說話」的秘書。它們能回答問題、總結複雜文件。但要處理實際工作，我們必須打開瀏覽器、點擊按鈕、登入並逐一輸入數據。這些過程在專業術語中被稱為 **介面 (Interface，使用者與電腦溝通所使用的螢幕或工具)** 操作。

Gemini 2.5 Computer Use 的出現意味著 AI 已經超越了「對話」，進入了「執行」階段。Google 的這款模型可以直接「看」懂網頁瀏覽器或 Android 應用程式的螢幕，並模仿人類進行點擊按鈕、輸入文字、滾動螢幕等物理行為 [Google 新聞 - 關於 Gemini 的新聞 - 概覽](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lDM3NUYkR4SHN2TllKS192ekVpZ0FQAQ?hl=en-NA&gl=NA&ceid=NA:en) [Google 揭曉 Gemini 2.5 Computer Use，能像人類一樣點擊、打字、滾動... | Beebom](https://beebom.com/google-unveils-gemini-2-5-computer-use-that-clicks-types-scrolls-like-humans/)。

簡單來說，這是一款學會了如何使用電腦的 AI。這預示著上班族將告別把 Excel 數據搬運到網站上的枯燥重複勞動，而對於一般使用者來說，這宣告了能夠代為處理複雜網銀或購物流程的真正 **代理人 (Agent，無需人類干預即可自主判斷並達成目標的 AI 程式)** 的誕生 [介紹 Gemini 2.5 Computer Use：網頁 AI 與... | LinkedIn](https://www.linkedin.com/posts/googleaidevs_introducing-gemini-25-computer-use-available-activity-7381415403840864256-ycSe) [2025 完全指南：Gemini 2.5 Computer Use 模型 - AI Agent 介面控制的革命性突破](https://velog.io/@czmilo/2025-완전-가이드-Gemini-2.5-Computer-Use-모델-AI-Agent-인터페이스-제어의-혁명적-돌파구)。

## 輕鬆理解：AI 如何使用我的電腦？

該模型運作的方式與我們用眼睛看螢幕、用手移動滑鼠的過程驚人地相似。這被稱為 **「代理人迴圈 (Agent Loop)」**，主要包含三個階段的循環過程 [介紹 Gemini 2.5 Computer Use 模型](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-computer-use-model/)：

1.  **觀察 (觀看)**：AI 拍攝目前電腦螢幕的截圖並進行確認。就像我們盯著螢幕思考「該按哪裡？」一樣。
2.  **思考 (分析)**：分析截圖，判斷按鈕在哪裡，在當前情況下應該輸入什麼。此時 AI 不僅僅是看圖像，而是推論出「啊，螢幕中央的藍色按鈕是『結帳』按鈕！」。接著制定具體的行動計劃，例如「點擊座標 (500, 300) 的位置」 [Computer Use | Gemini API | Google AI for Developers](https://ai.google.dev/gemini-api/docs/computer-use)。
3.  **執行 (行動)**：根據制定的計劃，實際移動滑鼠游標或用鍵盤輸入文字。

**比喻來說，這個模型就像是高性能的自動駕駛 GPS。** 就像 GPS 確認當前位置 (截圖)，決定在哪個路口轉彎以到達目的地 (推論)，然後指示駕駛員 (執行器) 轉動方向盤一樣。Gemini 2.5 Computer Use 會在極短的時間內無限重複這個過程，朝著目標前進。

之所以能完成這種高階任務，是因為該模型繼承了 Google 最聰明的模型之一「Gemini 2.5 Pro」強大的視覺理解與邏輯推理能力 [介紹 Gemini 2.5 Computer Use：網頁 AI 與... | LinkedIn](https://www.linkedin.com/posts/googleaidevs_introducing-gemini-25-computer-use-available-activity-7381415403840864256-ycSe) [Gemini 2.5 Computer Use 深度分析與實戰代碼](https://fornewchallenge.tistory.com/entry/Gemini-25-Computer-Use-완벽-분석-및-실전-코드)。

## 現況：它有多聰明？

根據 Google 的說法，Gemini 2.5 Computer Use 已經遠遠超越了單純聽命點擊的初級水平。

*   **執行複雜任務的能力**：不僅僅是按下一個按鈕，還能從下拉式選單中選擇選項，重複應用多個篩選器，甚至在為了安全而需要登入的複雜網站中也能熟練地處理任務 [Google 推出用於瀏覽器自動化的 Gemini 2.5 Computer Use 模型...](https://www.allaboutai.com/ai-news/google-launches-gemini-2-5-computer-use-model-for-browser-automation/) [Google 發佈 Gemini 2.5 Computer Use AI 模型預覽版...](https://gigazine.net/gsc_news/en/20251008-google-gemini-2-5-computer-use)。
*   **壓倒競爭對手的成績**：在多項衡量網頁及行動端控制能力的 **基準測試 (Benchmark，用於比較 AI 性能的標準測試)** 中，它取得了領先於 OpenAI 或 Anthropic 的 Claude Sonnet 4.5 等強勁競爭模型的驚人成績 [2025 完全指南：Gemini 2.5 Computer Use 模型 - 革命性 ...](https://dev.to/czmilo/2025-complete-guide-gemini-25-computer-use-model-revolutionary-breakthrough-in-ai-agent-133) [Google 揭曉 Gemini 2.5 Computer Use，能像人類一樣點擊、打字、滾動... | Beebom](https://beebom.com/google-unveils-gemini-2-5-computer-use-that-clicks-types-scrolls-like-humans/)。
*   **轉瞬即逝的反應速度**：AI 執行指令時最令人沮喪的就是「等待」。與其他 AI 相比，該模型發出指令到實際行動之間的 **延遲 (Latency，系統反應所需的時間)** 非常短，因此操作更加流暢自然 [2025 完全指南：Gemini 2.5 Computer Use 模型 - 革命性 ...](https://dev.to/czmilo/2025-complete-guide-gemini-25-computer-use-model-revolutionary-breakthrough-in-ai-agent-133) [2025 完全指南：Gemini 2.5 Computer Use 模型 - AI Agent 介面控制的革命性突破](https://velog.io/@czmilo/2025-완전-가이드-Gemini-2.5-Computer-Use-모델-AI-Agent-인터페이스-제어의-혁명적-돌파구)。

目前，該模型已透過 Gemini API 以預覽形式提供給開發者，許多企業已經在利用它測試自動化工具 [介紹 Gemini 2.5 Computer Use：網頁 AI 與... | LinkedIn](https://www.linkedin.com/posts/googleaidevs_introducing-gemini-25-computer-use-available-activity-7381415403840864256-ycSe) [Google 為能點擊與滾動的 AI 推出 Gemini 2.5](https://geekflare.com/news/ai-that-clicks-and-scrolls-google-introduces-gemini-2-5-computer-use-model/)。

## 未來會如何發展？

Gemini 2.5 Computer Use 的出現不僅僅是技術上的進步，更是宣告「AI 代理人時代」開幕的信號。Google 在 OpenAI 重大活動的隔天發佈該模型，充分顯示了全球科技巨頭對這一領域的重視程度 [Google 推出 Gemini 2.5 Computer Use 與 OpenAI 代理人競爭... | The Tech Buzz](https://www.techbuzz.ai/articles/google-launches-gemini-2-5-computer-use-to-rival-openai-agents)。

我們很快將目睹以下驚人的變化：

1.  **真正的個人助手時代**：不僅僅是「告訴我」的秘書，而是「幫我處理這個」就能帶來結果的秘書，將出現在我們每個人的生活中。從預訂旅行到整理收據，所有煩人的事情都將交給 AI。
2.  **勞動性質的轉變**：將數據從 Excel 搬運到網頁，或登錄數百個商品資訊等簡單重複的網頁工作將會消失。人類將能專注於更具創意和高層次的思考 [2025 完全指南：Gemini 2.5 Computer Use 模型 - 革命性 ...](https://dev.to/czmilo/2025-complete-guide-gemini-25-computer-use-model-revolutionary-breakthrough-in-ai-agent-133)。
3.  **安全與保障的重要性**：由於 AI 直接操作我的電腦，對於因誤操作導致的事故或安全威脅的擔憂也會增加。與此同時，更強大的安全指南和阻斷裝置也將隨之發展 [PDF Gemini Computer Use 外部模型卡 (2025 年 10 月 7 日) - 更新 2](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-2-5-Computer-Use-Model-Card.pdf)。

Google 透明地公開了該模型的局限性與安全裝置，強調在技術發展的同時也要進行負責任的開發 [PDF Gemini Computer Use 外部模型卡 (2025 年 10 月 7 日) - 更新 2](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-2-5-Computer-Use-Model-Card.pdf)。

## AI 的觀點 (AI's Take)

如果說過去的 AI 專注於理解人類的「語言」，那麼現在它開始學習如何使用人類幾十年來創造的「數位工具」。Gemini 2.5 Computer Use 將成為打破人類與機器之間巨大隔閡的重要橋樑。不久後，我們將習慣於不再親自握住滑鼠，而是像委託同事工作一樣向 AI 指示方向的新型「運算」模式。技術成為工具，工具即刻執行的時代已在眼前。

## 參考資料

1. [介紹 Gemini 2.5 Computer Use 模型](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-computer-use-model/)
2. [Google 新聞 - 關於 Gemini 的新聞 - 概覽](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lDM3NUYkR4SHN2TllKS192ekVpZ0FQAQ?hl=en-NA&gl=NA&ceid=NA:en)
3. [Gemini 2.5 Computer Use 代理人：最強大的代理人... - YouTube](https://www.youtube.com/watch?v=Xllcw7YUjJA)
4. [介紹 Gemini 2.5 Computer Use：網頁 AI 與... | LinkedIn](https://www.linkedin.com/posts/googleaidevs_introducing-gemini-25-computer-use-available-activity-7381415403840864256-ycSe)
5. [Gemini Computer Use：Google 的免費瀏覽器... - Analytics Vidhya](https://www.analyticsvidhya.com/blog/2025/10/gemini-2-5-computer-use/)
6. [Gemini 2.5 Computer Use 模型：如何自動化瀏覽器](https://skywork.ai/blog/gemini-2-5-computer-use-model/)
7. [Gemini 2.5 Computer Use 深度分析與實戰代碼](https://fornewchallenge.tistory.com/entry/Gemini-25-Computer-Use-완벽-분석-및-실전-코드)
8. [Computer Use | Gemini API | Google AI for Developers](https://ai.google.dev/gemini-api/docs/computer-use)
9. [2025 完全指南：Gemini 2.5 Computer Use 模型 - 革命性 ...](https://dev.to/czmilo/2025-complete-guide-gemini-25-computer-use-model-revolutionary-breakthrough-in-ai-agent-133)
10. [PDF Gemini Computer Use 外部模型卡 (2025 年 10 月 7 日) - 更新 2](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-2-5-Computer-Use-Model-Card.pdf)
11. [2025 完全指南：Gemini 2.5 Computer Use 模型 - AI Agent 介面控制的革命性突破](https://velog.io/@czmilo/2025-완전-가이드-Gemini-2.5-Computer-Use-모델-AI-Agent-인터페이스-제어의-혁명적-돌파구)
12. [2025 完全指南：Gemini 2.5 Computer Use 模型 - 革命性 ...](https://curateclick.com/blog/gemini-25-computer-use)
13. [Google 為能點擊與滾動的 AI 推出 Gemini 2.5](https://geekflare.com/news/ai-that-clicks-and-scrolls-google-introduces-gemini-2-5-computer-use-model/)
14. [Google 推出用於瀏覽器自動化的 Gemini 2.5 Computer Use 模型...](https://www.allaboutai.com/ai-news/google-launches-gemini-2-5-computer-use-model-for-browser-automation/)
15. [Google 發佈 Gemini 2.5 Computer Use AI 模型預覽版...](https://gigazine.net/gsc_news/en/20251008-google-gemini-2-5-computer-use)
16. [Google 揭曉 Gemini 2.5 Computer Use，能像人類一樣點擊、打字、滾動... | Beebom](https://beebom.com/google-unveils-gemini-2-5-computer-use-that-clicks-types-scrolls-like-humans/)
17. [Google 推出 Gemini 2.5 Computer Use 與 OpenAI 代理人競爭... | The Tech Buzz](https://www.techbuzz.ai/articles/google-launches-gemini-2-5-computer-use-to-rival-openai-agents)

## 事實查核摘要
- 查核項目：14
- 已證實項目：14
- 結論：通過