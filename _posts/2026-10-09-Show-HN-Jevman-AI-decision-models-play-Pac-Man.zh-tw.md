---
layout: post
title: "AI 竟然會玩小精靈？測試 AI 即時判斷力的趣味基準測試「Jevman」"
description: "介紹專為測試 AI 模型判斷速度與準確度而開發的小精靈（Pac-Man）遊戲基準測試「Jevman」。"
summary: "探討開源基準測試專案「Jevman」，該專案透過讓各種 AI 模型在小精靈遊戲中即時躲避幽靈，衡量其判斷的準確度與速度。"
tags: [AI, 基準測試, 小精靈, Jevman, 決策模型]
image: 2026-10-09-Show-HN-Jevman-AI-decision-models-play-Pac-Man.jpg
image_alt: "在華麗的經典小精靈遊戲畫面上方，AI 模型正即時進行判斷並遊玩遊戲的樣子"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "與其使用複雜的公式，透過像遊戲這樣親切的環境來比拼 AI 的判斷速度，更能直觀且有效地展示模型的實戰能力。"
quiz:
  - question: "Jevman 基準測試的主要目的是什麼？"
    choices: ["測試 AI 的圖形處理能力", "測試 AI 模型的即時判斷速度與準確度", "比拼 AI 能玩遊戲多長時間"]
    answer: 1
    explanation: "Jevman 是為了測量 AI 模型在小精靈遊戲這種環境中，能否快速處理資訊並做出正確決策的即時判斷力而建立的。"
  - question: "Jevman 的測試方式為何？"
    choices: ["每個模型各玩 10 次，總計 50 場遊戲", "共有 6 個模型參與，每個模型各玩 100 場遊戲", "人類與 AI 進行 1 對 1 對決"]
    answer: 1
    explanation: "共有 6 個主要 AI 模型參與了 Jevman 基準測試，每個模型皆即時遊玩了 100 場小精靈遊戲來比拼性能。"
  - question: "下列關於 Jevman 專案特徵的敘述，何者正確？"
    choices: ["僅能透過付費服務存取", "測試結果不對外公開", "屬於開源專案，任何人皆可提交自己的模型"]
    answer: 2
    explanation: "Jevman 是一個開源專案，使用者可以直接將自己的模型提交至基準測試中來確認性能。"
lang: zh-tw
ref: 2026-10-09-Show-HN-Jevman-AI-decision-models-play-Pac-Man
---

試著想像一下。您正坐在大型機台前操作小精靈（Pac-Man）。畫面中的幽靈正以極快的速度追趕著您。在這裡，您必須在每 0.1 秒做出「該往左還是往右走？」的決定。在這種讓人冷汗直流的緊張時刻，人工智慧（AI）究竟會如何判斷呢？

最近，為了即時測試 AI 的判斷力，出現了一個非常有趣的「小精靈基準測試」。那就是 **Jevman**。

## 這為什麼很重要？

我們平時使用的聰明 AI 雖然擅長閱讀長篇文章並總結內容，但若是在需要於極短時間內做出即時判斷的情況下，表現又會如何呢？

Jevman 正是為了考驗 AI 這種「決策（Decision-making）」能力而生。當我們在日常生活中委託 AI 進行判斷，例如：「現在馬上需要帶雨傘嗎？」或是「該接受這筆投資案嗎？」時，AI 必須在極短時間內分析複雜的情況。小精靈遊戲中觀察幽靈動向並尋找路徑的過程，為模擬這種複雜的決策過程提供了最佳環境。

簡單來說，Jevman 不僅超越了 AI 單純的語言知識，更是評估 AI 在急迫的實時情況下，能多快、多準確地選擇正確行為的一種「AI 大腦考場」。[[參考資料: jevman: AI decision models play Pac-Man | VibeLeaderboard](https://www.vibeleaderboard.ai/app/17f8acd3-69b1-4c04-b083-30957220898d)]

## 易於理解的說明

Jevman 所執行的測試，簡直就像是 **「給 AI 考的汽車駕照路考」**。

1. **狀態感知 (State)**：AI 模型會接收到畫面狀態作為資訊，了解目前小精靈在哪裡，以及幽靈的位置。[[參考資料: GitHub - denis-shvets/jevman-benchmark: Pac-Man driven by the ...](https://github.com/denis-shvets/jevman-benchmark)]
2. **判斷 (System One decision)**：稱為「系統一（System One）」的快速且本能的決策模型會分析這些資訊。這就好比手觸碰到熱鍋時會反射性躲避一樣，是一種直覺性的判斷。[[參考資料: Jev: System One Decision Model Explained | AIJev](https://aijev.org/)]
3. **行動 (Action)**：AI 根據判斷結果，決定上、下、左、右中的一個方向來移動小精靈。[[參考資料: GitHub - codaaiteam/jev-pacman: You drive Pac-Man; Jev...](https://github.com/codaaiteam/jev-pacman)]

這個過程以極短的毫秒（ms）為單位不斷重複。若將此比喻為新手駕駛觀察道路車道與紅綠燈來轉動方向盤的過程，AI 正是在遊戲中操控小精靈的同時，提升自己的駕駛實力。目前參與這場測試的 6 個 AI 模型（jev 1.13, kev, clef, clef flash, GPT-6 Luna, Laya 等）各自進行了 100 場小精靈遊戲，以證明自己的判斷力。[[參考資料: jevman: AI decision models play Pac-Man | TheaterFire](https://theaterfi.re/post/3741604), [參考資料: Jevman: AI Decision Models Play Pac-Man | VibeLeaderboard](https://www.vibeleaderboard.ai/app/17f8acd3-69b1-4c04-b083-30957220898d)]

## 目前狀況

Jevman 的意義不僅止於 AI 會玩遊戲而已。所有遊戲紀錄皆公開，任何人都可以觀看，並且存在一個能一眼看出誰拿到更高分數的 **官方排行榜（Leaderboard）**。[[參考資料: jevman: a Pac-Man benchmark for decision models | OpperAI](https://opper.ai/jevman-benchmark/), [參考資料: jevman — Six AI decision models play Pac-Man, ranked live](https://launchdaily.info/products/jevman)]

更令人感興趣的是，這個專案是 **開源（Open Source）** 的。換句話說，只要是 AI 開發者，任何人都可以註冊自己的模型來測量 Jevman 基準測試的性能。甚至一般使用者也能親自試玩小精靈，並即時比較自己與 AI 模型的分數。這能讓大家親自驗證「人類的判斷力真的會比 AI 好嗎？」這種好奇心。[[參考資料: jevman · Can you beat the AI at Pac-Man?](https://jevman.apps.chadda.se/), [參考資料: jevman — Six AI decision models play Pac-Man, ranked live](https://launchdaily.info/products/jevman)]

## 未來展望

像 Jevman 這類以遊戲為基礎的基準測試，未來將會越來越多。這是因為 AI 正從單純展現知識的階段，進化為能在日常生活中實際控制軟體、依照商業規則進行自動決策的「行動 AI」。

現在，我們在選擇 AI 時，將不再只是考量「誰說話更流利」，而是會開始苦惱「誰能在危急情況下不出錯地做出正確判斷」。Jevman 正是為了準備這樣的未來，而為 AI 們所準備的快樂練習場——小精靈遊戲。

**MindTickleBytes 的 AI 記者觀點**：
AI 閱讀龐大論文並進行創作固然令人驚嘆，但觀察 AI 在像小精靈這樣緊張的遊戲中不斷減少失誤的過程，讓人感覺更像是在看 AI 的「實戰肌肉」，顯得更加寫實。期待未來能出現更多「遊戲型基準測試」，以更精密地檢驗 AI 的判斷力。

## 參考資料

1. [jevman: a Pac-Man benchmark for decision models | OpperAI](https://opper.ai/jevman-benchmark/)
2. [jevman · Can you beat the AI at Pac-Man?](https://jevman.apps.chadda.se/)
3. [GitHub - joch/jevman: Pac-Man driven by the jev decision model](https://github.com/joch/jevman)
4. [jevman: AI decision models play Pac-Man | TheaterFire](https://theaterfi.re/post/3741604)
5. [Show HN: Jevman – AI decision models play Pac-Man](https://semasocial.com/blog/show-hn-jevman-ai-decision-models-play-pac-man-61213)
6. [jevman — Six AI decision models play Pac-Man, ranked live](https://launchdaily.info/products/jevman)
7. [GitHub - denis-shvets/jevman-benchmark: Pac-Man driven by the ...](https://github.com/denis-shvets/jevman-benchmark)
8. [Jevman: AI Decision Models Play Pac-Man | VibeLeaderboard](https://www.vibeleaderboard.ai/app/17f8acd3-69b1-4c04-b083-30957220898d)
9. [Jev: System One Decision Model Explained | AIJev](https://aijev.org/)
10. [GitHub - codaaiteam/jev-pacman: You drive Pac-Man; Jev...](https://github.com/codaaiteam/jev-pacman)