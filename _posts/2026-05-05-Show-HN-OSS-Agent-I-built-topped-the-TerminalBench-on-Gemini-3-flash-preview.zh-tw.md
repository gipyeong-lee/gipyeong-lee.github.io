---
layout: post
title: "超越巨頭 Google 的「無名 AI 騎士」，登上終端機之王座"
description: "開源 AI 代理「Dirac」打破 Google 官方紀錄並奪得終端機基準測試第一名的秘訣，以及這對我們未來的影響"
summary: "搭載 Google Gemini 3 的開源 AI 代理 Dirac，在電腦專家領域的「終端機」控制測試中刷新了世界紀錄。"
tags: [AI代理, Gemini3, 開源, Dirac, 終端機基準測試]
image: 2026-05-05-Show-HN-OSS-Agent-I-built-topped-the-TerminalBench-on-Gemini-3-flash-preview.jpg
image_alt: "在黑色終端機畫面上，閃耀的數位大腦正即時解決複雜程式碼的模樣"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "這起事件證明了公開合作的力量可能比巨頭企業的壟斷技術更強大。它展現了 AI 從單純的對話對象進化為「行動助手」的轉折點。"
quiz:
  - question: "這次刷新世界紀錄的開源 AI 代理名稱為何？"
    choices: ["Gemini CLI", "Dirac", "Junie CLI"]
    answer: 1
    explanation: "Dirac 是由 Dirac Delta Labs 的 Max Trivedi 開發的開源 AI 代理。"
  - question: "評估 AI 終端機作業能力的這項測試名稱是？"
    choices: ["TerminalBench 2.0", "Gemini 測試", "Hacker News 基準測試"]
    answer: 0
    explanation: "TerminalBench 是評估 AI 在命令列介面執行檔案管理或腳本編寫能力的一項標準。"
  - question: "Dirac 在這次測試中紀錄的答對率是多少？"
    choices: ["47.8%", "64.3%", "65.2%"]
    answer: 2
    explanation: "Dirac 創下了 65.2% 的成功率，大幅領先 Google 的官方紀錄（47.8%）。"
lang: zh-tw
ref: 2026-05-05-Show-HN-OSS-Agent-I-built-topped-the-TerminalBench-on-Gemini-3-flash-preview
---

想像一下，你突然被獨自留在一個充滿複雜機械裝置的巨大工廠控制室裡。四面八方有數千個開關，螢幕上不斷閃過難以理解的加密程式碼。這裡是驅動整座工廠運行的核心，但如果不是極為熟練的技術人員，恐怕連碰都不敢碰。

在我們每天使用的電腦中，也存在著這樣一個「秘密控制室」。那就是充滿黑色畫面與白色文字的 **終端機（Terminal，直接輸入指令來控制電腦的視窗）**。一般使用者透過滑鼠點擊漂亮的圖示來使用電腦，但真正的專家則透過終端機這個工具，直接操作電腦的骨架並設計複雜的系統。

然而最近，在這個曾是專家聖域的終端機領域，發生了一件令世界震驚的事件。一個由個人開發者打造的「無名開源 AI」，擊敗了由 Google 等科技巨頭製作的官方 AI，登上了世界最強終端機專家的寶座。這就像是一位巷弄小店的廚師，在米其林三星主廚雲集的料理大賽中堂堂正正地奪冠一樣，充滿了戲劇性的反轉。

## 為何這很重要？「從會說話的 AI 進化到會行動的 AI」

直到目前為止，我們接觸到的 ChatGPT 或 Gemini 等 AI，主要是以「擅長說話」著稱。對於「幫我寫首詩」、「幫我翻譯英文」、「幫我摘要長文」等要求非常熟練。但若要委託它們進行實質性的工作，例如「幫我按內容整理電腦中散亂的 1,000 個檔案，並自動安裝必要的程式」，目前仍有許多令人不安的地方。

這次成為話題、名為 **Dirac** 的 AI 代理則完全不同。根據 [Dirac 開源代理在 TerminalBench 擊潰 Google 的基準紀錄](https://www.agent-wars.com/news/2026-04-27-show-hn-oss-agent-i-built-topped-the-terminalbench-on-gemini-3-flash-preview) 的報導，Dirac 證明了它能直接進入電腦最深處的終端機，下達複雜指令、管理檔案並自行解決問題。

簡單來說，這意味著 AI 已經超越了單純提供資訊的「善於言辭的秘書」，進化為能代替我管理電腦、俐落地執行複雜技術任務的 **「能幹的代理人（Agent）」**。特別是這次奪冠的並非投入數兆韓元資金的大企業付費服務，而是任何人都能研究其設計圖並免費使用的 **開源（Open Source，將軟體的原始碼向大眾公開）** 模型，這一點讓全球開發者感到熱血沸騰。

## 簡單理解：AI 的「駕照考試」——TerminalBench

為了衡量 AI 有多聰明，專家們會讓它們參加各種「考試」。這次 Dirac 登上王座的考試是 **TerminalBench 2.0**。[開源 AI 代理在 TerminalBench 2.0 排行榜奪冠](https://aihaberleri.org/en/news/open-source-ai-agent-scores-652percent-on-terminalbench-20-in-2026-beating-gemini-and-junie-cli)

這項考試可以比喻為 **「專為 AI 準備的高難度駕駛路考」**。只是這次駕駛的不是汽車，而是非常棘手且複雜的裝置——「電腦終端機」。考試項目包含連專家都會感到棘手的難題：[開源代理搭配 Gemini-3 登上 TerminalBench 榜首 - PromptZone](https://www.promptzone.com/maria_gonzalez_419fd1b8/oss-agent-tops-terminalbench-with-gemini-3-3lh2)

1.  **殼層腳本 (Shell Scripting)**：按順序編寫下達給電腦的多步驟指令（比喻來說，就像是毫無誤差地寫出供數萬人食用的複雜料理食譜）。
2.  **檔案管理**：在數萬個檔案中找出微小差異，並進行篩選、移動及修改等細膩作業。
3.  **系統設定**：根據目的完全改造電腦內部環境的高難度任務。

開發者「umair24171」評價道：「大多數 AI 考試往往只是詢問知識的表面功夫，但 TerminalBench 是能衡量 AI 是否真的能『幹活』的實力測試。」[Gemini-3-Flash：我的 AI 代理基準測試 TerminalBench 獲勝與三項修正](https://dev.to/umair24171/gemini-3-flash-my-ai-agent-benchmark-terminalbench-win-3-fixes-44eb)

## 現況：大衛擊敗歌利亞的驚人分差

這次對決的結果對整個 IT 業界造成了巨大的衝擊。因為這就像是一位靠自己尋找學習方法的學生，以壓倒性的分差擊敗了長期包辦全校第一的富家優等生。讓我們來看看實際的成績單：

*   **Dirac**：**65.2%**（基於任何人都能使用的開源技術）[Reddit 上的 r/GoogleGeminiAI：我建立的開源代理在 Gemini-3-flash-preview 的 TerminalBench 2.0 奪冠](https://www.reddit.com/r/GoogleGeminiAI/comments/1sx2r4s/open_source_agent_i_built_topped_the/ )
*   **Junie CLI**：64.3%（原本排名第一的昂貴付費商業模型）
*   **Google 官方紀錄**：**47.8%**（Google 親自用自家模型測試的結果）

令人驚訝的是，Dirac 紀錄的分數比 Google 創下的官方紀錄高出整整 17.4 個百分點。如果以學校考試來換算，當 Google 拿 48 分時，Dirac 已經超過了 65 分。[Reddit 上的 r/GoogleGeminiAI：我建立的開源代理在 Gemini-3-flash-preview 的 TerminalBench 2.0 奪冠](https://www.reddit.com/r/GoogleGeminiAI/comments/1sx2r4s/open_source_agent_i_built_topped_the/)

這次勝利的幕後功臣，其實是 Google 打造的最新 AI 大腦——**Gemini-3-flash-preview** 模型。[Dirac 開源代理在 TerminalBench 擊潰 Google 的基準紀錄](https://www.agent-wars.com/news/2026-04-27-show-hn-oss-agent-i-built-topped-the-terminalbench-on-gemini-3-flash-preview) Gemini-3 Flash 是 Google 的野心之作，旨在執行複雜程式碼和系統任務時，比既有模型運行得更快、更聰明。[Gemini-3-Flash — Google DeepMind](https://deepmind.google/models/gemini/flash/)

但重點在於，Google 自身未能妥善利用這個優秀的引擎，成績停留在 40 多分；反觀開發者 Max Trivedi 則透過精密的調優與優化，發揮出世界頂尖的效能。而且這是在不耍任何花招、公開所有設計圖的情況下完成的。[ShowHN：我建立的開源代理在 TerminalBench 奪冠...](https://news.ycombinator.com/item?id=47920787)

## 未來會如何？來到我們身邊的「萬能修理工」 AI

Dirac 的成功鮮明地展示了我們即將迎來的兩個未來。

第一，**AI 將成為我們家中的「電腦萬能修理工」。** 想像一下，當電腦速度突然變慢或彈出不明原因的錯誤視窗時，你不再需要支付昂貴的維修費請專家，而是對 AI 代理說：「幫我在終端機找出這個問題的原因並修好它。」AI 在黑色畫面上掃描數萬行程式碼並在 1 分鐘內完成維修的時代已近在咫尺。

第二，**「集體創作的力量」擊敗了巨頭企業的壟斷。** 因為這次證實了，即便借用 Google 製作的引擎，如果全世界的人一起思考並改進使用該引擎的更好方法（代理結構），產出的成果將遠比企業獨自秘密研發的要優秀得多。

當然，前方仍有挑戰。65.2% 的分數意味著每 10 次中仍可能有 3 次出錯。在終端機中出錯，可能面臨誤刪珍貴家庭照片或重要工作檔案的風險。因此，開發者們今天仍在不斷研究，為了打造更完美的「安全裝置」，確保 AI 絕不出錯。

## AI 的視線：MindTickleBytes 的 AI 記者視角

「Dirac 的勝利不單純是數字的對決。它證明了 AI 這種強大的工具並非特定大企業的專屬物，當我們所有人的智慧與好奇心匯聚時，它能綻放出最強烈的光芒。現在，我們已經渡過了思考『要問 AI 什麼』的時代，正站在思考『要委託 AI 幫我電腦處理哪些難事』的真正『代理人時代』門檻上。」

## 參考資料
1. [ShowHN：我建立的開源代理在 TerminalBench 奪冠...](https://news.ycombinator.com/item?id=47920787)
2. [Gemini-3-Flash：我的 AI 代理基準測試 TerminalBench 獲勝與三項修正](https://dev.to/umair24171/gemini-3-flash-my-ai-agent-benchmark-terminalbench-win-3-fixes-44eb)
3. [開源 AI 代理在 TerminalBench 2.0 排行榜奪冠](https://aihaberleri.org/en/news/open-source-ai-agent-scores-652percent-on-terminalbench-20-in-2026-beating-gemini-and-junie-cli)
4. [Gemini-3-Flash — Google DeepMind](https://deepmind.google/models/gemini/flash/)
5. [Reddit 上的 r/GoogleGeminiAI：我建立的開源代理在 Gemini-3-flash-preview 的 TerminalBench 2.0 奪冠](https://www.reddit.com/r/GoogleGeminiAI/comments/1sx2r4s/open_source_agent_i_built_topped_the/)
6. [開源代理搭配 Gemini-3 登上 TerminalBench 榜首 - PromptZone](https://www.promptzone.com/maria_gonzalez_419fd1b8/oss-agent-tops-terminalbench-with-gemini-3-3lh2)
7. [Gemini 3 — Google DeepMind](https://deepmind.google/models/gemini/)
8. [Dirac 開源代理在 TerminalBench 擊潰 Google 的基準紀錄](https://www.agent-wars.com/news/2026-04-27-show-hn-oss-agent-i-built-topped-the-terminalbench-on-gemini-3-flash-preview)

## 事實查核摘要 (FACT-CHECK SUMMARY)
- 查核聲明數：15
- 已證實聲明數：15
- 裁定：通過 (PASS)