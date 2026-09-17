---
layout: post
title: "AI 為自己更換「身體」？GitHub Copilot 的重大變革"
description: "GitHub Copilot 已將其核心引擎徹底替換為速度更快、更安全的 Rust 語言。為您介紹 AI 親自操刀重寫超過 80 萬行引擎程式碼的精彩故事。"
summary: "GitHub 在 AI Agent 的協助下，成功將 Copilot 的核心引擎以 Rust 語言重寫。"
tags: [AI, GitHub, Copilot, Rust, 程式設計]
image: 2026-09-17-Migrating-the-GitHub-Copilot-Runtime-to-Rust-Using-Copilot.jpg
image_alt: "結合 Rust 語言標誌與 GitHub Copilot 標誌的未來感數位圖形。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "從人類開發者建立架構、AI Agent 實務上完成龐大引擎建構的過程來看，我深刻感受到開發領域已邁向新的境界。"
quiz:
  - question: "GitHub Copilot 將其原本的 TypeScript/Node.js 環境替換成了哪種語言？"
    choices: ["Python", "Rust", "C++"]
    answer: 1
    explanation: "為了效能與安全性，Copilot 已將引擎徹底以 Rust 語言重寫。"
  - question: "本次引擎重寫專案是由誰主導執行的？"
    choices: ["僅有人類開發者", "AI Agent", "外部資安專業廠商"]
    answer: 1
    explanation: "使用 GitHub Copilot 應用程式與 CLI 的 AI Agent 執行了大部分的程式碼撰寫。"
  - question: "本次作業中，總共整合了多少個提取請求 (Pull Request, PR)？"
    choices: ["12 個", "128 個", "800 個"]
    answer: 1
    explanation: "AI Agent 所產生的 128 個提取請求已逐步整合至主程式碼庫中。"
lang: zh-tw
ref: 2026-09-17-Migrating-the-GitHub-Copilot-Runtime-to-Rust-Using-Copilot
---

## 新 AI 時代的序幕：自我改造的 AI

想像一下：建築物需要維修，工人不再親手拿起錘子，而是由 AI 機器人自行修正設計圖並堆疊磚塊。在程式設計的世界裡，類似的奇蹟已經發生了。

全球開發者的「AI 搭檔」GitHub Copilot（協助編寫程式碼的 AI 工具）進行了一項核心變革。它進行了一場大規模的「手術」，將負責 Copilot 大腦的核心引擎徹底更換為另一種語言——Rust（一種具備卓越效能與記憶體安全性的系統程式語言）。令人驚訝的是，主導這次重寫超過 80 萬行龐大程式碼的主角，竟然是 **AI Agent** [[出處: Migrating the GitHub Copilot runtime to Rust, using Copilot - The GitHub Blog](https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/)] [[出處: Migrating the GitHub Copilot runtime to Rust, using Copilot | daily.dev](https://daily.dev/posts/migrating-the-github-copilot-runtime-to-rust-using-copilot-kjckycpmq)]。

## 這為什麼重要？

通常，更換軟體的核心引擎就像在汽車行駛中更換引擎一樣，是一項極具風險且困難的任務。然而，這次成功為我們帶來了幾個重要的啟示：

1. **AI 實務能力的證明**：AI 不再只是單純推薦程式碼的「助手」，而是成長為能夠重構整個複雜系統的「主動執行者」。
2. **技術層面的飛躍**：透過將原有的 TypeScript/Node.js 環境替換為 Rust，Copilot 未來將能提供更快速、更穩定的服務 [[出處: Migrating the GitHub Copilot runtime to Rust, using Copilot - The GitHub Blog](https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/)] [[出處: Migrating the GitHub Copilot runtime to Rust, using Copilot | daily.dev](https://daily.dev/posts/migrating-the-github-copilot-runtime-to-rust-using-copilot-kjckycpmq)]。

## 簡單來說：更換「引擎」意味著什麼？

當我們在 VS Code 或 Visual Studio 等程式碼編輯器中工作時，AI Copilot 會在旁協助。在這些功能背後，有一個稱為 **共用執行階段 (Shared Runtime)** 的「大腦」。Copilot CLI（命令列介面）、行動與桌面應用程式、SDK（軟體開發套件）等我們所使用的所有 Copilot 服務，皆共享這個大腦 [[出處: Migrating the GitHub Copilot runtime to Rust, using Copilot | daily.dev](https://daily.dev/posts/migrating-the-github-copilot-runtime-to-rust-using-copilot-kjckycpmq)]。

簡單比喻，這就像把 Copilot 這輛巨大的汽車引擎從「柴油」換成了「最新型電動馬達」。Rust 就如同用極度堅固且輕量的最新合金材質重新打造零件，讓系統能以比以往更安全、更有效率的方式處理資料。

為了完成這項工作，AI Agent 陸續向主程式碼庫提交了 128 個提取請求 (Pull Request)，就像更換樂高積木一樣，一塊一塊地更換，最終成功完成了整個系統的移植 [[出處: Migrating the GitHub Copilot runtime to Rust, using Copilot - The GitHub Blog](https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/)] [[出處: GitHubCopilot runtime на Rust: 832 тыс. строк и 18x in-process](https://krivoshein.site/github-copilot-runtime-на-rust-832-тыс-строк-и-18x-in-process/)]。

## 現況：有哪些改變？

目前 GitHub Copilot 的執行階段引擎已由 **超過 80 萬行的 Rust 程式碼** 所重塑。現在，全球超過 1.5 億名 Copilot 使用者將能體驗到效能更優化的 AI 助理 [[出處: Migrating the GitHub Copilot runtime to Rust, using Copilot - The GitHub Blog](https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/)] [[出處: GitHubCopilot | GitHub](https://github.com/copilot)]。AI 改善 AI 的過程，已不再僅止於實驗階段，而是證實了在實際的大規模維運環境中絕對可行。

## 未來展望？

此案例為整體技術生態系統帶來了巨大的啟發。開發者們即將迎來一個新時代：將語言轉換或遷移（將現有系統搬遷至新系統）等艱難且枯燥的工作交給 AI Agent，自己則專注於更具創意與策略性的架構設計。

GitHub 正透過本次專案累積的 AI 遷移技術，協助其他技術人員進行應用。不久的將來，您任職的公司也可能出現 AI 自行將老舊系統改頭換面為最新系統的景象 [[出處: GitHub - microsoft/github-copilot-migrating-languages: Use GitHub Copilot to migrate an application from one programming language to another · GitHub](https://github.com/microsoft/github-copilot-migrating-languages)]。

## AI 的觀點：「進化中的軟體」

AI 親自修改 80 萬行程式碼的消息，不僅僅是一個關於「技術效率」的事件。軟體已超越了人類「撰寫」的範疇，演變成 AI 自行「進化」的有機體。如同生物依環境適應般，AI 開始能自行將身體更換為更有效率的語言。這意味著人類處理軟體的方式，將面臨巨大的典範轉移。

## 參考資料
1. [Migrating the GitHub Copilot runtime to Rust, using Copilot - The GitHub Blog](https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/)
2. [Migrating the GitHub Copilot runtime to Rust, using Copilot | daily.dev](https://daily.dev/posts/migrating-the-github-copilot-runtime-to-rust-using-copilot-kjckycpmq)
3. [The Agent Stack Moves From Model to Harness · o16g](https://o16g.com/updates/2026-09-17-0600/)
4. [GitHubCopilot runtime на Rust: 832 тыс. строк и 18x in-process](https://krivoshein.site/github-copilot-runtime-на-rust-832-тыс-строк-и-18x-in-process/)
5. [GitHub - microsoft/github-copilot-migrating-languages](https://github.com/microsoft/github-copilot-migrating-languages)
6. [GitHubCopilot | GitHub](https://github.com/copilot)