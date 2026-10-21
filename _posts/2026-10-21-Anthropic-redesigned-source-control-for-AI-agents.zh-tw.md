---
layout: post
title: "與 AI 共事的新方式？Anthropic 徹底顛覆了原始碼控制系統"
description: "Anthropic 公布了全新原始碼控制方式「Scion」及改良版 Claude Code 桌面應用程式，旨在實現與多個 AI 代理同時協作。"
summary: "Anthropic 推出了新一代原始碼控制系統與介面，超越了傳統 git 的限制，旨在讓多個 AI 代理能並行進行程式編寫與測試。"
tags: [AI, 開發, Anthropic, Claude, 程式編寫代理]
image: 2026-10-21-Anthropic-redesigned-source-control-for-AI-agents.jpg
image_alt: "介面圖像，展現多個 AI 代理同時分析程式碼並並行執行工作的現代開發環境"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "如果過去的開發工具是為了人類主導的循序工作而設計，那麼現在這些工具本身已經準備好迎接『代理人』這位新同事。這項重大的變化顯示，開發者的角色正從直接編寫程式碼，進化為 AI 代理的協調者（Orchestrator）。"
quiz:
  - question: "Anthropic 所發表的次世代原始碼控制系統名稱為何？"
    choices: ["Git Plus", "Scion", "Claude Control"]
    answer: 1
    explanation: "Anthropic 為了超越傳統 git 的限制，開發了一種名為「Scion」的新方法。"
  - question: "新的 Claude Code 桌面應用程式為了減少開發者的情境切換（context-switching）而引入的功能中，不包含下列何者？"
    choices: ["會話側邊欄", "拖放式佈局", "雲端自動刪除"]
    answer: 2
    explanation: "Claude Code 透過會話側邊欄、拖放式佈局及內建終端機等功能進行了改良，讓開發者能同時管理多個代理。"
  - question: "在代理人導向編程（agentic coding）的環境中，開發者的主要角色是什麼？"
    choices: ["親自一行一行撰寫程式碼", "管理多個代理會話的協調者", "建立硬體伺服器"]
    answer: 1
    explanation: "隨著多個代理並行執行任務，開發者將轉變為指揮並管理這些代理的協調者（orchestrator）。"
lang: zh-tw
ref: 2026-10-21-Anthropic-redesigned-source-control-for-AI-agents
---

想像一下，早上起床打開電腦時，已經有三位 AI 開發者正在協助你的軟體專案。其中一位正在實作新功能，另一位正在修復程式錯誤，最後一位則在進行即時測試，確保新寫的程式碼運作正常。

過去，開發者必須循序漸進地親自完成所有流程，或是為了將多個片段的工作成果合併而忙得不可開交。但現在，開發方式正在徹底改變。因為 Anthropic 推出了適用於「代理人時代」的全新原始碼控制（Source Control）系統與工具。

## 這為什麼重要？

軟體開發至今一直是在「人類主導、循序執行」的假設下發展。但隨著 AI 代理（能自主執行特定目的的 AI 程式）參與編程，情況發生了變化。根據 Anthropic 的研究，隨著代理人導向編程（agentic coding）普及，傳統軟體開發方式的基本前提正在快速演進[參考資料 1](https://www.anthropic.com/research/redesigning-source-control)。

這些變化不僅僅是提升編程速度的問題。當多個 AI 代理同時進行各自不同的任務時，傳統的原始碼控制系統（管理開發者程式碼變更歷程的系統）遭遇了瓶頸。Anthropic 提出的新環境引導開發者扮演「協調者（Orchestrator）」的角色，即時指揮多個代理的工作，並大幅減少此過程中產生的頻繁情境切換（context-switching，在作業間轉換時導致專注力下降的現象）[參考資料 2](https://www.eigent.ai/blog/claude-code-desktop-redesign)[參考資料 5](https://completeaitraining.com/news/anthropic-redesigns-claude-code-desktop-app-to-better/)。

## 簡單理解：從 Git 到 Scion

傳統的原始碼控制系統「git」，實際上是為了管理單一人員修改與儲存檔案的流程而最佳化的。這就像是一本書由多個人輪流書寫一樣。但如果多個 AI 代理同時修改不同部分，會發生什麼事呢？

Anthropic 開發了一種名為「Scion」的新系統[參考資料 1](https://www.anthropic.com/research/redesigning-source-control)。

簡單比喻，如果原有的 git 是給一位作家使用的「稿紙」，那麼 Scion 就如同「現代協作平台」，數十位作家各自在自己的房間同時寫作，而指揮者則穿梭於這些房間之間，即時組合內容。此系統完全配合代理人的規模，重新設計了既有的原始碼控制原則[參考資料 1](https://www.anthropic.com/research/redesigning-source-control)。

## 現狀：Claude Code 的進化

Anthropic 將這一哲學融入其中，徹底重新設計了自家的編程代理工具「Claude Code」桌面應用程式[參考資料 2](https://www.eigent.ai/blog/claude-code-desktop-redesign)。

現在的 Claude Code 不再只是單純的指令列工具。它配備了以下功能，改變了開發者的工作空間[參考資料 5](https://completeaitraining.com/news/anthropic-redesigns-claude-code-desktop-app-to-better/)[參考資料 7](https://www.linkedin.com/posts/abhijeet-pachpute_anthropic-redesigned-claude-code-for-desktop-activity-7450256887431843840-lelR)：

*   **會話側邊欄：** 可以一目了然地查看正在執行中的多個 AI 代理狀態。
*   **拖放式佈局：** 可自由配置所需的工作視窗，管理代理的工作流程。
*   **內建終端機：** 無需在不同視窗間切換，即可在同一處處理程式碼修改、執行測試、提交（儲存）變更事項。

透過這些更新，AI 代理能以並行會話的方式，直接讀取、修改、測試程式碼庫，並安全地反映變更[參考資料 7](https://www.linkedin.com/posts/abhijeet-pachpute_anthropic-redesigned-claude-code-for-desktop-activity-7450256887431843840-lelR)。

## 未來展望

Anthropic 的這次變革，不僅僅是改變了工具的外觀，更提出了開發者該如何駕馭 AI 的新標準。未來會有更多 AI 服務採用能連接不同代理的「標準協定（MCP, Model Context Protocol，不同 AI 工具間為交換資訊所使用的通用語言）」[參考資料 14](https://www.zdnet.com/article/google-joins-openai-in-adopting-anthropics-protocol-for-connecting-ai-agents-why-it-matters/)。

我們所要觀察的未來，不僅在於 AI 變得多聰明，更取決於**「AI 之間能多麼和平協作，以及人類指揮者能多麼有效率地控管它們」**。正如原始碼控制系統擁抱了 AI 時代，未來的開發環境將會轉變為「以代理人為預設值」的時代。

## 參考資料

1. Redesigning source control at Anthropic (https://www.anthropic.com/research/redesigning-source-control)
2. Claude Code Desktop Redesign: Parallel Agents (2026) (https://www.eigent.ai/blog/claude-code-desktop-redesign)
3. Projects redesigned: from folder to conversation | Claude by Anthropic (https://claude.com/blog/projects-redesigned)
4. Anthropic Turns Claude Code Projects Into a Parallel AI... - KingyAI (https://kingy.ai/news/anthropic-claude-code-projects-ai-agents/)
5. Anthropic redesigns Claude Code desktop app to better handle... (https://completeaitraining.com/news/anthropic-redesigns-claude-code-desktop-app-to-better/)
6. Anthropic redesigns Claude Projects as multi-agent coordinator (https://www.brocker.org/anthropic-redesigns-claude-projects-multi-agent-coordinator-claude-code)
7. Anthropic redesigned Claude Code for desktop. tl;dr This is a serious... (https://www.linkedin.com/posts/abhijeet-pachpute_anthropic-redesigned-claude-code-for-desktop-activity-7450256887431843840-lelR)
14. Google joins OpenAI in adopting Anthropic's protocol for connecting AI agents - ZDNET (https://www.zdnet.com/article/google-joins-openai-in-adopting-anthropics-protocol-for-connecting-ai-agents-why-it-matters/)