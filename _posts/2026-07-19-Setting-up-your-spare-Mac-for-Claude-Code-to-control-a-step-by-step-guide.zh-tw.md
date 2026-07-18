---
layout: post
title: "我的舊 MacBook 變成 AI 助理？透過 Claude Code 控制 Mac"
description: "逐步了解如何利用閒置在家的舊 MacBook 安裝 AI 助理 Claude Code，並進行遠端控制。"
summary: "介紹如何將閒置的 MacBook 設定為 Claude Code 專用的 AI 遠端裝置，並從主力工作用 Mac 或智慧型手機輕鬆控制的方法。"
tags: [AI, MacBook, ClaudeCode, 自動化]
image: 2026-07-19-Setting-up-your-spare-Mac-for-Claude-Code-to-control-a-step-by-step-guide.jpg
image_alt: "放在桌上，與工作用 MacBook 連接並運作中的舊 MacBook"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "為舊設備賦予新任務是永續科技應用的核心。希望透過這份指南，讓您的 MacBook 蛻變為聰明的 AI 助手。"
quiz:
  - question: "將舊 MacBook 作為 Claude Code 專用設備的主要原因之一是什麼？"
    choices: ["為了提升 MacBook 的效能", "為了建立 AI 代理所需的遠端獨立環境", "為了延長電池壽命"]
    answer: 1
    explanation: "透過建立與主要工作環境分離的獨立設備，AI 可以安全且有效地執行螢幕控制與應用程式操作過程。"
  - question: "安裝 Claude Code 前必須具備的條件是什麼？"
    choices: ["最新型 M3 MacBook", "已訂閱 Claude Pro 或啟用計費功能的 Anthropic 帳號", "獨立顯示卡"]
    answer: 1
    explanation: "使用 Claude Code 需要付費訂閱 (Pro/Max) 或連接計費功能的 Anthropic 帳號。"
  - question: "遠端控制已安裝 Claude Code 的 Mac 之主要方法為何？"
    choices: ["SSH 連接與 Claude App 連結", "直接攜帶 MacBook 移動", "利用藍牙鍵盤"]
    answer: 0
    explanation: "可以透過 SSH (Secure Shell，遠端存取協定) 從其他設備控制，或是透過智慧型手機的 Claude App 連結使用。"
lang: zh-tw
ref: 2026-07-19-Setting-up-your-spare-Mac-for-Claude-code-to-control-a-step-by-step-guide
---

## 抽屜裡的舊 MacBook，蛻變為 AI 助理

想像一下。早上起床後，您對著智慧型手機向 AI 說：「確認我今天要做的待辦事項，並打開特定應用程式整理資料。」接著，擱在抽屜角落已久的舊 MacBook 便自動開機，移動滑鼠指標執行應用程式並開始工作。這種彷彿有看不見的人在代替您操作 Mac 的魔法，在「Claude Code」這個工具的輔助下，已成為現實。

最新的電腦已非唯一選擇。在今天的指南中，我們將介紹如何將您擁有的閒置 MacBook 變身為「AI 專用遠端設備」，讓 AI 能親自觀察螢幕、點擊按鈕並操作應用程式。

## 這為什麼很重要？

AI 已超越單純回答文字的階段，現在透過「電腦使用（Computer Use）」能力，能像人類一樣使用滑鼠點擊、鍵盤輸入來操作軟體 [出處: Claude Code Computer Use 能力](https://www.mindstudio.ai/blog/claude-code-computer-use-mac-setup-guide)。

然而，將主力電腦完全交給這樣的 AI，難免會擔心個資安全或工作干擾問題。這時，若將閒置的舊 MacBook 打造成「獨立工作室」如何呢？您可以安全地建立 AI 專用環境，並隨時透過手邊的智慧型手機或主力 PC 進行遠端操控 [出處: 將多餘 MacBook 作為 AI 遠端設備應用](https://github.com/ykdojo/mac-claude-setup) [出處: 打造永遠開機的 AI 控制 Mac](https://github.com/ykdojo/claude-controls-mac)。

## 淺顯易懂：賦予 AI 雙手的過程

簡單來說，Claude Code 是賦予 AI「數位滑鼠與鍵盤」的過程。比喻來說，就是為您的舊 MacBook 接上一個由 AI 這顆「大腦」所能操控的「手腳」。

1. **指令者（AI）與操控者（MacBook）**：當 AI 下達「點擊這裡」的指令時，安裝好的 Claude Code 會與 Mac 作業系統溝通，實際移動指標並按下按鈕 [出處: AI 代理的 Mac 控制](https://www.mindstudio.ai/blog/claude-code-computer-use-mac-setup-guide)。
2. **遠端的橋樑（SSH）**：如同我們遠端控制他人的電腦，在您的主力設備與舊 MacBook 之間建立一個名為「SSH（Secure Shell，透過加密通訊遠端控制電腦的方式）」的安全通道 [出處: 透過 SSH 進行控制](https://github.com/ykdojo/claude-controls-mac)。

這樣一來，舊 MacBook 就成為負責觀察螢幕、點擊與輸入的「手腳」，而您則擔任遠端指揮這些手腳的「指揮官」。

## 安裝準備

開始安裝前，請備妥下列項目：

* **多餘的 MacBook**：舊一點也沒關係。我們將把它作為遠端控制的獨立環境。
* **Claude 訂閱**：需要擁有 Anthropic 的「Claude Pro」訂閱，或是已開通計費的 Anthropic 帳號 [出處: 必要條件](https://inventivehq.com/knowledge-base/claude/how-to-install-claude-code-cli)。

## 逐步安裝過程

大部分安裝工作是透過終端機（Terminal，直接向電腦下達指令的文字介面）進行 [出處: 基於終端機的安裝](https://www.serverman.co.uk/ai/claude/how-to-install-claude-code-on-mac/)。

1. **基礎工具安裝**：首先在 MacBook 上安裝必要的軟體工具。通常需要安裝「Homebrew（Mac 軟體套件管理工具）」、「Node.js（程式執行環境）」、「Git（程式碼版本管理工具）」等 [出處: 必要工具安裝指南](https://dev.to/xujfcn/claude-code-installation-guide-for-macos-git-environment-variables-path-and-every-common-fix-4l96)。
2. **Claude Code 安裝**：在準備好的終端機視窗輸入提供的指令即可安裝 Claude Code [出處: 透過終端機指令安裝](https://www.kimi.com/resources/how-to-install-claude-code)。
3. **連結與設定**：安裝完成後，連結您的帳號。隨後為了遠端存取，請啟用該設備的 SSH 設定，以便隨時能從主力設備或智慧型手機連線 [出處: 遠端存取設定](https://github.com/ykdojo/mac-claude-setup)。

安裝過程中若遇到問題，請仔細閱讀終端機視窗的提示。許多情況是由設定檔或權限問題所導致 [出處: 安裝問題解決指南](https://docs.anthropic.com/en/docs/claude-code/overview)。

## 未來展望

透過這次的設定，您已從單純的 AI 聊天機器人使用者，成為直接驅動 AI 代理的「管理者」。未來 Claude Code 將會更加精進，能更自由地操作複雜的 macOS 應用程式。目前或許以單純的點擊為主，但不久後，AI 就能在您的舊 MacBook 裡化身稱職的助理，熟練運用設計工具、處理文件工作，並透過網頁瀏覽為您整理資訊。

現在，正是讓抽屜裡的 MacBook 覺醒，成為您的聰明 AI 夥伴的時間。

## 參考資料

1. [Setting Up Claude Code Locally with a Powerful Open-Source Model: A Step-by-Step Guide for Mac Users](https://medium.com/@luongnv89/setting-up-claude-code-locally-with-a-powerful-open-source-model-a-step-by-step-guide-for-mac-84cf9ab7302f)
2. [My Claude Code Setup Guide · GitHub](https://gist.github.com/graimon/0bf150c89d6c6844ab95866935bd4b0a)
3. [How to Set Up Claude Code on Mac (2026 Guide)](https://www.masteringai.io/guides/claude-code-setup-mac)
4. [Claude Code Installation Guide for macOS: Git, Environment Variables, Path and Every Common Fix](https://dev.to/xujfcn/claude-code-installation-guide-for-macos-git-environment-variables-path-and-every-common-fix-4l96)
5. [GitHub - ykdojo/mac-claude-setup: How to set up a spare Mac ...](https://github.com/ykdojo/mac-claude-setup)
6. [How to Install Claude Code on Mac (Step-by-Step Guide)](https://www.serverman.co.uk/ai/claude/how-to-install-claude-code-on-mac/)
7. [How to Build an AI Agent That Controls Your Mac: Claude Code Computer Use Setup Guide](https://www.mindstudio.ai/blog/claude-code-computer-use-mac-setup-guide)
8. [GitHub - ykdojo/claude-controls-mac: Step-by-step guide to turning...](https://github.com/ykdojo/claude-controls-mac)
9. [How to Install And Use Claude Code - YouTube](https://www.youtube.com/watch?v=NQNrPaDPMiA)
10. [Terminal guide for new users - Claude Code Docs](https://code.claude.com/docs/en/terminal-guide)
11. [Claude Code overview - Anthropic](https://docs.anthropic.com/en/docs/claude-code/overview)
12. [Claude Skills Builder - Create Custom AI Skills for Claude Code](https://skills-claude.com/)
13. [Guide to use open models with Claude Code on your local device](https://unsloth.ai/docs/basics/claude-code)
14. [Claude Code CLI: Install on Mac/Windows, winget... | Inventive HQ](https://inventivehq.com/knowledge-base/claude/how-to-install-claude-code-cli)
15. [Install Claude Code: The Complete Guide for macOS, Windows...](https://www.morphllm.com/install-claude-code)
16. [Install Claude Code: Full Guide for Windows & Mac](https://www.kimi.com/resources/how-to-install-claude-code)
17. [Claude Code БЕСПЛАТНО через OpenRouter: настройка... - YouTube](https://www.youtube.com/watch?v=EMFMUEuNpWA)