---
layout: post
title: "聰明化辦公室！竟然能在自建伺服器上安裝 Claude 與 Codex 代理？"
description: "探討如何將企業作業系統（Company OS）直接安裝在自建伺服器中，並針對各部門活用 Claude Code 與 Codex 等 AI 代理的方法。"
summary: "一套名為「自託管企業作業系統（Self-hosted Company OS）」的專案正式登場，企業能在無須擔憂資安的情況下，於自建伺服器中基於 Claude Code 與 Codex 代理，直接驅動各部門的 AI 業務流程。"
tags: [AI, 自託管, 企業作業系統, Claude Code, Codex]
image: 2026-09-10-Show-HN-Self-hosted-company-OS-Claude-Code-and-Codex-agents-in-departments.jpg
image_alt: "展示各部門 AI 代理在自建伺服器上運作的未來感圖像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "在資料安全至關重要的企業環境中，將 AI 代理封裝於自建伺服器內進行管理，將成為解決採用雲端 AI 最大阻礙的關鍵轉折點。"
quiz:
  - question: "此次介紹的企業作業系統（Company OS）主要特點為何？"
    choices: ["僅能在雲端伺服器上運作", "任何人皆可免費下載並自行託管", "沒有付費訂閱即無法使用"]
    answer: 1
    explanation: "該系統是以開源形式提供，是一套企業能夠自行安裝並於內部伺服器運行操作的免費專案。"
  - question: "為了維持 AI 代理的安全性，使用了哪些技術手段？"
    choices: ["強化密碼", "應用沙盒核心與網路隔離技術", "始終保持連網狀態"]
    answer: 1
    explanation: "每個代理皆透過沙盒（bubblewrap）環境與網路隔離（pasta）技術，確保其於受到資安保護的伺服器內部安全運行。"
  - question: "傳遞專案規則或指令給 AI 代理的方式為何？"
    choices: ["僅能輸入於專用 App 中", "在專案資料夾內建立 CLAUDE.md 或 AGENTS.md 等規則檔案", "每次都在聊天視窗中輸入"]
    answer: 1
    explanation: "Claude Code 透過 CLAUDE.md 檔案，而 Codex 則透過 AGENTS.md 檔案，在執行前預先學習並遵循專案規則與指令。"
lang: zh-tw
ref: 2026-09-10-Show-HN-Self-hosted-company-OS-Claude-Code-and-Codex-agents-in-departments
---

想像一下：每天早上進辦公室後，告訴 AI 秘書：「請整理上個月的銷售數據，並撰寫各部門的報告草稿。」然而，這套 AI 並不會將資料傳送到外部雲端伺服器，而是僅在公司地下電腦室的專用伺服器中，完全只針對公司內部資料進行學習並產出結果。這樣既無需擔憂資訊外洩，又能維持公司原有的工作流程。

近期，開發者 Dimitris 在 Hacker News 社群中公開了一項名為**「企業作業系統（Company OS，協助企業業務處理的 AI 整合系統）」**的專案，引起廣泛關注。[參考資料 1](https://modernorange.io/item/49630606) 該系統讓企業能將我們熟知的「Claude Code（輔助開發的 AI 代理）」等強大工具直接安裝在公司伺服器中，並提供各部門自由使用。[參考資料 1](https://modernorange.io/item/49630606), [參考資料 10](https://news.ycombinator.com/item?id=49630606)

## 為什麼這很重要？

過去許多企業即便想導入 AI，也會因為「資料安全」而卻步。因為企業不希望核心機密傳送到外部雲端服務。然而，此次推出的企業作業系統採用了**「自託管（Self-hosting，不租用外部服務，而是直接在自建伺服器中安裝運行程式的方式）」**。[參考資料 1](https://modernorange.io/item/49630606), [參考資料 4](https://rankium.io/rankium/press/press-self-hosted-company-os-claude-code-and-codex-agents-in-depa-hackernews)

簡單來說，就是打造一個公司資料不出門的「專屬安全 AI 島」。各部門都能擁有自己的 AI 代理，負責管理工作排程、使用所需工具，並累積屬於該部門的工作記憶。[參考資料 10](https://news.ycombinator.com/item?id=49630606)

## 淺顯易懂：企業專屬 AI 工廠

若要比喻這套系統，它就像是**「企業專屬 AI 工廠」**：

1. **代理（AI 秘書）**：在工廠工作的聰明熟練工。「Claude Code」或「Codex（另一款輔助程式開發的 AI 模型）」即扮演此角色。[參考資料 5](https://claude.com/), [參考資料 10](https://news.ycombinator.com/item?id=49630606)
2. **沙盒（Sandbox，隔離的安全區域）**：工廠內部的安全護欄。透過稱為「bubblewrap」的技術，即使 AI 熟練工工作再勤奮，資訊也無法外流至工廠外，同時也能徹底阻擋外部駭客入侵。[參考資料 10](https://news.ycombinator.com/item?id=49630606)
3. **規則檔案（CLAUDE.md / AGENTS.md）**：工廠的工作手冊。若將 `CLAUDE.md` 檔案放入 Claude Code 的專案資料夾中，AI 熟練工每天早上上班時就會閱讀並依此手冊工作。Codex 則透過 `AGENTS.md` 手冊執行同樣的邏輯。[參考資料 6](https://theivansergeev.com/guide-gpt-5-6-vs-code/)

換句話說，只要將「公司是以這些規則運作」的手冊丟給 AI，它就能在公司伺服器內安全地遵守規則並完成工作。

## 功能極限為何？

目前該系統為各部門提供獨立的工作空間。每個代理都擁有自己的工作記憶與排程，能獨立運作。[參考資料 10](https://news.ycombinator.com/item?id=49630606) 特別是為了因應重視資安的企業環境，系統使用了網路隔離技術「pasta」，徹底切斷不必要的外部連接。[參考資料 10](https://news.ycombinator.com/item?id=49630606)

現階段 Claude Code 作為協助開發者理解與編輯程式碼的工具已廣為人知，且基於開源架構可直接安裝使用。[參考資料 5](https://claude.com/), [參考資料 12](https://claude.com/product/claude-code) 不過需留意，若要作為企業作業系統完整運用，仍需具備伺服器建置的基礎技術知識。

## 未來趨勢如何？

預計未來企業將減少使用複雜的雲端訂閱模型，轉而選擇符合自身伺服器規格的模型並直接安裝。由於此次公開的專案是任何人皆可免費取用的開源專案，隨著更多開發者的貢獻，極大可能發展成更簡單、強大的管理工具。[參考資料 1](https://modernorange.io/item/49630606) 企業自行聘僱並管理專屬「AI 秘書團隊」的時代已經近在咫尺。

## MindTickleBytes AI 記者觀點

技術的發展正從雲端這個「公共空間」，回歸到企業內部的「私人空間」。最終，除了 AI 的智能化程度外，如何在守護公司珍貴資料的前提下與 AI 協作，將成為未來競爭力的核心。

## 參考資料

1. [Show HN: Self-hosted company OS, Claude Code and Codex agents in departments](https://modernorange.io/item/49630606)
2. [VueHN 2.0 | Show HN: Self-hosted company OS, Claude Code and...](https://vue-hackernews-ssr-5cavbdjcta-ew.a.run.app/item/49630606)
3. [Show HN: Self-hosted company OS, Claude Code and Codex agents in departments](https://vk.ru/wall-238001904_5064)
4. [Self-hosted company OS, Claude Code and Codex agents in departments](https://rankium.io/rankium/press/press-self-hosted-company-os-claude-code-and-codex-agents-in-depa-hackernews)
5. [Claude](https://claude.com/)
6. [Codex в VSCode: как подключить GPT-5.6 и настроить ИИ-агента](https://theivansergeev.com/guide-gpt-5-6-vs-code/)
7. [Show HN: Self-hosted company OS, Claude Code... | HackerNews](https://news.ycombinator.com/item?id=49630606)
8. [Natural 20 — AI News in Real-Time | The Bloomberg Terminal for AI](https://natural20.com/c/1bbk9g)
9. [Claude Code by Anthropic | AI Coding Agent, Terminal, IDE](https://claude.com/product/claude-code)