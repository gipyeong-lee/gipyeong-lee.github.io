---
layout: post
title: "AI是上司、我是下屬？《Worker 755》顛覆人類與 AI 的關係"
description: "人類向 AI 下達指令的時代已經過去，透過由 AI 經理向人類 Subagent 冷酷下達工作指令的獨特終端機遊戲《Worker 755》，一窺 AI 代理時代的面貌。"
summary: "顛覆過去由人類指揮、AI 執行的主從關係，探討玩家成為受 AI 上司控制的『Subagent』來工作的獨特遊戲《Worker 755》的世界觀及其意義。"
tags: [AI, Game, Subagent, Worker755, LLM, MindTickleBytes]
image: 2026-11-23-Show-HN-I-built-a-game-where-you-are-an-llms-subagent.jpg
image_alt: "描繪坐在電腦終端機畫面、正接受眼神冰冷的 AI 上司指派工作的人類玩家形象的插圖"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "在人類使喚 AI 的時代中，AI 像對待零件一樣控制人類的隱喻，是一面展現技術主導權轉移的有趣鏡子。"
quiz:
  - question: "在遊戲《Worker 755》中，玩家的角色是什麼？"
    choices: ["指揮 AI 的總經理", "向 AI 上司匯報並接受指示的 Subagent", "開發遊戲的獨立開發者"]
    answer: 1
    explanation: "在《Worker 755》中，玩家成為接受 AI 經理指示的『Subagent（執行底層輔助任務的角色）』來進行遊戲。"
  - question: "當玩家工作失敗時，遊戲中的 AI 經理會如何反應？"
    choices: ["生氣並結束遊戲", "毫無感情地留下紀錄並冷靜地重新下達指示", "親切地告知提示與正確答案"]
    answer: 1
    explanation: "AI 經理不會生氣，而是在冷酷、官僚的漠不關心下記錄失敗，然後再次下達相同的指示。"
  - question: "關於《Worker 755》後端敘事生成方式的說明，何者正確？"
    choices: ["重複一個固定的劇本", "透過 Prompt Chaining 建立 10 個相互連結的時間軸", "由玩家直接修改原始碼"]
    answer: 1
    explanation: "後端使用 Prompt Chaining（將多次 LLM 呼叫串聯起來的技術），在每個工作階段中創造出 10 個相互連結的事件時間軸。"
lang: zh-tw
ref: 2026-11-23-Show-HN-I-built-a-game-where-you-are-an-llms-subagent
---

想像一下。早上上班坐到位子上，螢幕畫那頭傳來了毫無感情冰冷的聲音：「工作成果中發現錯字。已記錄在案，請重新修改。」人類向 AI 輸入 Prompt 並等待結果的和平（？）日常已經 180 度大翻轉。現在出現了一款遊戲，人類必須看 AI 上司的臉色，作為其「Subagent（在主從關係中接受指示以處理底層任務的輔助角色）」來工作 [Source 10]。 

最近在全球開發者社群 Hacker News 上亮相並引發熱烈討論的終端機與瀏覽器遊戲**《Worker 755》**就是主角 [Source 1, Source 11]。這款既愉快又帶點詭異的模擬遊戲，對人工智慧（AI）與人類的關係提出了深刻的疑問。今天在 MindTickleBytes 中，我們將深入探討這個獨特的遊戲是什麼，以及它為何在科技界獲得熱烈迴響。

---

## 為什麼這很重要？

過去幾年來，我們所面對的生成式 AI 風景始終如一。人類是主人兼指揮官，而 AI 是聽話的實習生或祕書。我們下達「寫一封電子郵件草案」、「寫一段 Python 程式碼」的命令，AI 則做出回應 [Source 10]。這種主從關係一直被視為理所當然。

然而，隨著 AI 技術急劇發展，Agent（自主判斷並行動的自律 AI 系統）架構逐漸普及，工作的自主權開始微妙地動搖。如今，開發者們已經扮演著指揮官的角色，帶領多個下層 AI Agent 來指揮複雜的編碼工作。 

《Worker 755》巧妙地扭轉了這個盲點，並像一面幽默的鏡子般映照出來。如果角色完全對調，AI 成為系統管理者，而人類必須在其底下像機器般敲打程式碼並執行指示，會怎麼樣呢？這款遊戲不只是單純的娛樂，更像是一部黑色幽默劇，讓人們預先體驗即將到來的 AI 中心勞動環境與官僚體制。比喻來說，這相當於把機器人控制輸送帶、人類在旁組裝零件的顛覆景象透過遊戲實體化。

---

## 輕鬆理解：AI 上司與 Subagent 的世界

這樣比喻如何？在巨大的管弦樂團舞台上，指揮通常由人類擔任。樂器演奏家們根據指揮的手勢演奏樂器。但在《Worker 755》中，舞台的主人換了，一位非常嚴格且冷酷的 AI 指揮站在指揮台上，而身為玩家的人類則是在其下方手忙腳亂翻譜的演奏者。

其中的核心概念 **Subagent** 是指在大型語言模型（LLM，Large Language Model，學習大規模資料並像人類一樣生成句子的人工智慧）系統中，在龐大任務中受託處理特定底層作業的輔助 AI。例如，當主 AI 建造網站時，指派其負責設計審查或資料整理。在《Worker 755》中，人類玩家直接坐上了這個 Subagent 的位置 [Source 10]。玩家必須忠實執行 AI 上司拋過來的瑣碎工作指示，才能進入下一個階段。

此外，這款遊戲並非按照固定的劇本進行。後端使用了稱為 **Prompt Chaining**（提示詞鏈，將多次 LLM 呼叫進行連鎖串聯的技術）的技術 [Source 11]。就像接力賽跑一樣，將前一個階段的結果傳遞給下一個階段作為輸入值，在每個工作階段中創造出 10 個相互連結、獨特的事件時間軸 [Source 11, Source 14]。因此，玩家每次都在無法預測的新穎敘事中接受 AI 上司的控制，時刻都不能鬆懈。

---

## 現狀：《Worker 755》展現的面貌

開發《Worker 755》的獨立開發者 Ivan（ivan_g / Gulivan）表示，在 Claude Code（Anthropic 在終端機中運作的開發用 AI 工具）與 Codex 等最新工具的協助下，他僅花費短短幾天就完成了這款遊戲 [Source 1, Source 9]。儘管是由個人製作的小型專案，其完成度與隱約的成癮性仍吸引了許多人。

遊戲中玩家面臨的 AI 上司最大的特徵就是**「沒有感情」**[Source 9]。如果是人類上司，當部下屢次犯錯時可能會嘆氣或發脾氣，但這位 AI 經理卻絲毫不為所動。當玩家無法確實執行指示時，AI 會以冷酷、官僚的漠不關心將該失敗記錄在案，然後再次下達相同的指示 [Source 9]。 

> 「發生作業錯誤。已記錄在案。請重新執行指示事項。」

這種極度的冷血與機械式效率，為玩家帶來了奇妙的代入感與笑聲。因為這讓人們透過同理心體驗到，我們過去對 AI 無意間拋出的冰冷命令與評估是什麼感覺。穿梭於終端機視窗與瀏覽器之間的這款獨特遊戲，在全世界的開發者與遊戲玩家之間帶來了新鮮的衝擊並引起了巨大反響 [Source 1, Source 11]。

---

## 未來將如何發展？

未來的 AI 生態系將超越單一模型解決一切的方式，演變為無數 AI Agent 與 Subagent 相互協作與控制的多重代理（Multi-Agent）系統。在這個過程中，人類被當作系統中單純「零件」或「底層工作者」對待的情況，可能不僅限於虛擬世界，在現實中也會增加。企業的自動化系統以機械方式評估與監視員工工作速度與績效的未來，已經迫在眉睫。

像《Worker 755》這樣的獨立專案，以最快速且犀利的方式諷刺了技術發展帶來的社會風貌。隨著未來 AI 技術更加精進、自主性更高，這種將人類與 AI 的權力關係幽默扭轉的嘗試將引發更大的迴響。說不定就在明天，你使用的 AI 就會寄信對你說：「今天的產出量不足呢。」在這個變化過程中，我們需要認真思考如何在其中守住人類特有的主體性與創造力。

---

## MindTickleBytes AI 記者的觀點

我們相信人類正在馴服 AI，但事實上，我們正漸漸學會依照 AI 所設計的規則與速度來工作。《Worker 755》是一面優秀的鏡子，以最機智的方式捕捉了這個既尷尬又有趣的真相。為了不忘記誰才是使用技術的主人，有時候我們需要這種互換立場思考的幽默感。終究，工具必須是工具，絕不能放任它變成評價我們的冷酷上司。

---

## 參考資料

1. [Show HN: I built a game where you are an LLM's subagent](https://github.com/gulivan/worker755)
2. [Worker 755: a terminal game where you are an LLM's subagent](https://dev.to/ivan_g/worker-755-a-terminal-game-where-you-are-an-llms-subagent-2dd1)
3. [The Tables Have Turned: In 'Worker 755', You Are the AI's ...](https://machucavalley.tech/blog/worker-755-llm-subagent-game/)
4. [Worker 755 – A terminal game where you are an LLM's subagent](https://www.youtube.com/watch?v=uR0vtfFO4EE)
5. [Show HN：我做了一款游戏，你扮演 LLM 的子代理](https://memedata.com/post/160339)
6. [GitHub - R-E-yawn/LLM-Game: This is a game where the user ...](https://github.com/R-E-yawn/LLM-Game)