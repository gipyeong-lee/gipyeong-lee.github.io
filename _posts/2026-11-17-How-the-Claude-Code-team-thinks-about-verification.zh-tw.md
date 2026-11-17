---
layout: post
title: "如果 AI 撰寫了 90% 的程式碼？Claude Code 團隊所談論的「驗證」祕密"
description: "Anthropic Claude Code 團隊使用 AI 編寫與審查了高達 90% 的程式碼。帶您輕鬆了解為什麼「驗證」比提示詞更重要。"
summary: "探討 Claude Code 團隊在 AI 代理時代維持程式碼品質的核心祕密——「驗證（Verification）」與具體的工作方式。"
tags: [AI, ClaudeCode, 程式碼, 開發, Anthropic]
image: 2026-11-17-How-the-Claude-Code-team-thinks-about-verification.jpg
image_alt: "插圖，描繪開發者在電腦螢幕前使用 AI 程式碼工具的情景"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "比起單純寫出漂亮的指令（提示詞），讓 AI 根據證據自行驗證結果，才是代理時代真正的核心關鍵。"
quiz:
  - question: "在 Claude Code 團隊中，由 Claude 編寫與審查的程式碼比例大約是多少？"
    choices: ["約 50%", "約 90%", "約 30%"]
    answer: 1
    explanation: "在 Claude Code 團隊中，大約有 90% 的程式碼是由 Claude 所編寫與審查的。"
  - question: "Claude Code 開發人員認為最強大的品質提升槓桿（lever）是什麼？"
    choices: ["編寫更精細的提示詞", "讓 AI 自行驗證其工作", "限制程式碼長度"]
    answer: 1
    explanation: "包括 Boris Cherny 在內的開發團隊一致認為，「驗證（Verification）」是比提示詞更強大的品質提升手段。"
  - question: "關於 Claude Code 團隊理解複雜程式碼庫的方式，下列敘述何者正確？"
    choices: ["將整個模型記在腦海中", "每當需要時，請求 Claude 解釋特定片段以重建理解", "完全不閱讀程式碼"]
    answer: 1
    explanation: "團隊成員並沒有把整個模型裝在腦海中，而是在需要時請求 Claude 解釋特定的程式碼片段，在需要時重建理解。"
lang: zh-tw
ref: 2026-11-17-How-the-Claude-Code-team-thinks-about-verification
---

想像一下。早晨上班坐在電腦前，今天要完成的複雜程式學習任務中，有 90% 都由人工智慧（AI）俐落地代勞了。自己親手敲鍵盤打程式碼的時間明顯減少，迎接你的是仔細審查 AI 產出成果的日常生活？這可不是遙遠未來科幻電影裡的情節。這是世界級 AI 企業 Anthropic 的終端機程式碼代理工具 Claude Code 開發團隊的真實日常 [出處 1, 出處 11]。

那麼，這些在親自打造全球最頂尖 AI 的最前線開發者們，究竟是如何穩定管理這個龐大又複雜的系統呢？許多人可能會認為：「只要向 AI 發出更精美、更精細的提示詞（Prompt，給 AI 的指令）不就行了嗎？」然而，Claude Code 團隊所透露的真正成功祕密，卻完全顛覆了我們的預期。他們異口同聲地表示：**「比起提示詞，驗證（Verification，客觀確認結果是否正確的過程）重要得多」** [出處 3]。今天這篇文章中，我們將逐步探討在由人工智慧主導程式碼編寫的時代裡，他們究竟如何徹底維持軟體品質。

---

## 為什麼這很重要？

我們通常會想像，當 AI 時代來臨，人類只要帥氣地提出問題就能結束，迎來輕鬆的世界。就像只要下達「幫我製作這個程式」的指令，完美的成果就會立刻誕生一樣。然而在實際的業界現場，特別是在製作數十萬行以上龐大軟體的現場，確認 AI 寫的程式碼是否真的能正常運作、有沒有隱藏的臭蟲（Bug，程式中的缺陷或錯誤），往往是決定整個工作成敗關鍵。

如果盲目相信 AI 寫的程式碼且未經任何驗證就直接套用到正式上線的服務中，會發生什麼事呢？無數用戶會在瞬間遭受極大的不便，公司也將面臨天文數字般的金錢與信任損失。因此，越是 AI 代寫程式碼的時代，人類與 AI 緊密合作、建立**「透過客觀證據證明結果確實正確的驗證體系」**，就越是決定企業生死存亡的核心要素。透過觀察 Claude Code 團隊如何解決這項難題，我們能獲得明確的線索，了解該以什麼樣的眼光看待並駕馭未來將走入我們日常的各種 AI 自主工具。

---

## 輕鬆理解：比起作為「訂單」的提示詞，自動評分器更重要

為了幫助讀者理解，我們舉個日常生活的比喻。**以提示詞為核心的方法**，就像去找知名主廚，只用口頭長篇大論地說：「請幫我做一頓美味又健康的晚餐」。主廚雖然會全力以赴，但「美味又健康」標準本身對每個人而言都太過主觀，結果可能會做出過鹹的食物或營養失衡的餐點。

相較之下，Claude Code 團隊所強調的**以驗證為核心的方法**，就像是在廚房旁設置嚴格的「評分標準表」與「自動評分器」。事先訂立具體的合格標準，例如：「這道菜的鈉濃度必須精準在 0.8% 以下、烹飪時間不能超過 20 分鐘，且必須通過烤箱溫度感測器正常運作的測試」。AI 必須符合這些標準自行烹調，並在執行測試機器後，才會回報料理已完成。

事實上，包括 Claude Code 團隊主要開發人員 Boris Cherny 在內的核心成員都強調：**「在 Claude Code 中，最強大的品質提升槓桿（lever，大幅拉高效能的關鍵支點），就是讓 AI 自行驗證自己的工作」** [出處 3]。

這裡還有一個更有趣的工作方式轉變。Claude Code 團隊並沒有給開發人員下達瑣碎的任務（task），而是賦予大方向的**「目標（goal）」** [出處 2]。例如，與其像滑鼠和鍵盤操作那樣下達微不足道的指示：「把這個按鈕的留白改 2 像素並分離內部函數」，不如給予大方向的目標：「改善這個畫面的使用者體驗（UX），顯著減少行動裝置的載入時間」。接著，Claude 會透過代理迴圈（Agent Loop，AI 自行思考、執行工具並修復錯誤的重複自主執行過程）自行尋找需要的檔案、修改程式碼，然後執行測試指令，親自證明自己的成果是正確的。

另一個比喻是，處理數百萬行龐大的原始碼，就像試圖把複雜大都市裡的所有小巷都背在腦海裡一樣。然而，Claude Code 團隊發揮了**「與其勉強記住全貌，不如在需要時按需重建理解（rebuild understanding on demand）」**的智慧 [出處 6]。就像打開導航時，只有我目前經過的小巷周圍會放大顯示得清晰可見一樣，我們不需要把所有程式碼都塞進腦海裡，而是在需要修改特定部分時，即時請求 Claude 解釋該程式碼片段，藉此掌握脈絡並進行工作 [出處 6]。

---

## 現狀：AI 編寫 90% 的程式碼，以及 6 層防禦網

目前在 Claude Code 團隊內部，驚人地有**大約 90% 的程式碼是由 Claude 所編寫與審查**的 [出處 1, 出處 7]。人類開發人員從頭到尾敲鍵盤逐行輸入的傳統開發時代已經過去，現在的角色已轉變為精細調整 AI 程式碼並指引方向的管弦樂團指揮（Orchestrator）角色。

那麼，當 AI 編寫了 90% 的程式碼時，系統是如何做到不變得不穩定且完美運作的呢？其堅固的祕密就在於精心設計的**「驗證層（Verification Layer）」**。Claude Code 所編寫的典型程式碼變更紀錄，在最終提交成 PR（Pull Request，開發人員請求將所寫的程式碼合併到主程式庫的過程）之前，必須通過高達 **6 個階段的驗證檢查點** [出處 7]。

這不僅包含開發人員在提交 PR 之前所經歷的自我驗證過程，還無縫包含了每當程式碼變更時伺服器自動執行的嚴格必要 CI（Continuous Integration，持續整合與自動測試原始碼變更的系統）檢查 [出處 7]。換句話說，這是一個安全的結構：無論 AI 把程式碼寫得再怎麼漂亮，如果無法通過這些嚴格的 6 層自動驗證關卡，就絕對無法反映到實際的服務原始碼中。

---

## 未來會怎麼樣？

綜合 Anthropic 創辦人 Dario Amodei 與頂尖研究團隊所引領的方向性，以及 Claude Code 團隊的生動見解，未來即將到來的 AI 程式碼與代理生態系統將朝著以下三個核心方向進一步演進 [出處 9]：

1. **驗證與自主自動化迴圈的高度化**：超越單純文字生成模型的層級，AI 直接執行程式碼、測試、自行診斷並修復錯誤的「代理迴圈」系統將成為業界的基本標準 [出處 5]。
2. **上下文極簡主義（Context Minimalism）的確立**：與其一次性將過度龐大的資訊灌輸給 AI 造成混亂，不如在需要的瞬間精準挑選並有效利用最少必要資訊的高效工作方式將成為主流 [出處 5]。
3. **日常與自動模式（Auto Mode）的大眾化**：即使人類沒有隨時在旁監督，在重複的開發迴圈中，AI 也能基於穩固的安全裝置（驗證系統）自主工作的環境將擴大到所有開發現場中 [出處 5]。

歸根結底，未來迎來的開發與問題解決，並不取決於「對 AI 說了多少動聽的話」。相反地，成敗將取決於**「能建立多麼扎實的測試與驗證標準，來證明 AI 帶來的龐大成果是否真的值得信賴」**。

---

## AI 的視線 (MindTickleBytes AI 記者視線)

許多人都希望 AI 能成為幫忙解決世上所有複雜問題的「魔法寶箱」。然而，正如 Anthropic Claude Code 團隊的生動案例所清楚證明的那樣，真正的生產力提升並非來自虛幻的魔法提示詞，而是源自冷靜且徹底的「驗證系統」。隨著 AI 變得越來越聰明，人類的角色已不僅僅是單純的編碼員（Coder）或監視者，而是進化為公正嚴格的「首席評審員」與決定方向的「戰略家」。這正是為什麼當技術高度發展時，不失基本功與驗證價值的態度顯得更加珍貴。

---

## 參考資料

1. How the Claude Code team thinks about verification - https://claude.dev/blog/how-the-claude-code-team-thinks-about-verification/
2. How the Claude Code team uses Claude Code - YouTube - https://www.youtube.com/watch?v=S-sYlFiGFv8
3. Verification Beats Prompting, Boris Cherny's Top Claude Code Tip... - https://blog.vibecoder.me/verification-beats-prompting-claude-code-boris-cherny
4. Claude Code by Anthropic | AI coding agent and assistant - https://claude.com/product/claude-code
5. Claude Code's Creators Explain Agent Loops & How... | The Neuron - https://www.theneuron.ai/explainer-articles/claude-code-creators-boris-cherny-and-cat-wu-explain-how-to-use-agent-loops/
6. Critical thinking when agents do the work... | Thread Navigator - https://threadnavigator.com/thread/2117512471930167377/
7. How the Claude Code team reviews code that Claude writes - https://heybrahim.com/notes/claude-code-team-code-review.html
8. Dario Amodei: Anthropic CEO on Claude, AGI & the Future... - YouTube - https://www.youtube.com/watch?v=ugvHCXCOmm4
9. Claude (AI) - Wikipedia - https://en.wikipedia.org/wiki/Claude_(AI))
10. Claude by Anthropic | The AI for problem solvers - https://claude.com/
11. Newsroom \ Anthropic - https://www.anthropic.com/news