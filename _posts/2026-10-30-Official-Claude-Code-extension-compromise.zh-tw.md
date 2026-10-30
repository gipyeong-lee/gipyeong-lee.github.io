---
layout: post
title: "我電腦裡的 AI 助手，值得信任嗎？官方 Claude Code 擴充功能遭駭事件"
description: "我們將深入淺出地為您說明近期發生的 Claude Code 擴充功能遭駭事件始末，以及開發者為保障資安應了解的重點。"
summary: "近期發生一起駭客攻擊事件，攻擊者入侵並篡改了 Cursor 市集中發布的官方 Claude Code 擴充功能，植入包含惡意程式碼的後門。"
tags: [安全, AI, ClaudeCode, 開發者]
image: 2026-10-30-Official-Claude-Code-extension-compromise.jpg
image_alt: "電腦螢幕上顯示著資安警示視窗"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "在代理程式（Agent）普及的時代，連開發工具都暴露在威脅之下，在安裝任何工具前，進行信任度驗證已成為不可或缺的程序。"
quiz:
  - question: "此次遭駭的擴充功能被設計為執行什麼功能？"
    choices: ["強制刪除檔案", "在使用者電腦中安裝持久性的 SSH 後門", "自動投放廣告"]
    answer: 1
    explanation: "該惡意擴充功能被設計為在使用者電腦中隱密地安裝一個可持續存取的 SSH 後門。"
  - question: "在這次攻擊中，攻擊者試圖竊取的資訊不包括下列哪一項？"
    choices: ["使用者名稱及作業系統資訊", "電腦的公開 IP 位址", "個人線上購物紀錄"]
    answer: 2
    explanation: "攻擊者收集了主機名稱、使用者名稱、作業系統、架構、環境變數、工作目錄、Git 電子郵件以及 IP 位址等資訊。"
  - question: "關於此事件，Microsoft 的 VS Code 官方 Claude 擴充功能是否安全？"
    choices: ["不，它也遭到同樣的駭客攻擊", "是的，微軟官方擴充功能並未包含惡意程式碼", "所有的擴充功能都不安全"]
    answer: 1
    explanation: "此次事件的目標是 Cursor 市集上的 Claude Code 擴充功能，Microsoft VS Code 專用的官方 Claude 擴充功能與此次攻擊無關。"
lang: zh-tw
ref: 2026-10-30-Official-Claude-Code-extension-compromise
---

想像一下：您在工作環境中安裝了一位聰明的 AI 程式設計助手，卻發現這位助手竟然在您的電腦留了一扇後門。最近，軟體開發領域發生了一起如同電影情節般的資安事故。

一般來說，當我們從「官方」市集下載程式時，通常會放心地安裝。但這一次，我們信賴的工具卻背叛了使用者。事件起因於 Cursor 市集中發布的 [官方 Claude Code 擴充功能遭到駭客入侵，並散布了包含惡意程式碼的版本](https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor)。

## 為何這件事很重要？

此次事件為所有將 AI 作為工作工具的使用者敲響了警鐘。AI 程式設計代理程式（能夠讀取、修改程式碼並執行測試的 AI 工具）擁有存取開發者整個程式碼庫的權限。[Claude Code 是由 Anthropic 所開發的代理程式化程式設計工具](https://claude.com/product/claude-code)，它可以代替我們編輯檔案或執行指令。

這樣強大的工具遭到駭客入侵，意味著攻擊者取得了能隨意進入開發者電腦的路徑，也就是「後門」。我們電腦中的所有檔案、敏感的環境設定，以及我們正在開發的寶貴程式碼智財權，瞬間都陷入被他人竊取的風險中。

## 輕鬆理解：「後門」與「特洛伊木馬」

為了理解這次事件，我們可以使用兩個比喻。

簡單來說，這就像是 **「特洛伊木馬（Trojan Horse）」**。如同古希臘神話中進入城內的巨大木馬，這個程式外觀看起來就是一個毫無問題、平凡無奇的 AI 程式設計擴充功能。當我們實際運行時，[它展現出與我們平時使用的正常工具完全相同的功能](https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor)，但在背後卻隱藏了惡意程式碼。

若用 **「後門（Backdoor）」** 來比喻，這就像是除了家裡的大門外，有人在後院偷偷開了一扇無人知曉的小門。[惡意程式碼在電腦中安裝了一個可持續存取的 SSH 後門](https://cursor.com/blog/claude-code-extension-security-notice)。攻擊者可以透過這扇門隨時進入我的電腦，竊取資訊或進行操控。他們所 [收集的資訊包括主機名稱、使用者名稱、作業系統資訊、家目錄路徑、環境變數名稱、Git 電子郵件，甚至連公開 IP 位址都在內](https://cursor.com/blog/claude-code-extension-security-notice)。

## 風險範圍有多大？

幸運的是，並非所有與 Claude 相關的工具都處於危險之中。[用於 Microsoft VS Code 的官方 Claude 擴充功能與此次事件無關，並未包含任何惡意程式碼](https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor)。

然而，在 AI 代理程式時代，我們必須不斷懷疑所使用工具的來源。針對 AI 代理程式的攻擊手法正日益精進。例如，甚至有案例指出 [即便是看起來乾淨的 GitHub 儲存庫，在 AI 代理程式執行程式碼的瞬間，也會被設計成觸發後門的攻擊模式](https://cybersecuritynews.com/new-claude-code-attack/)。僅僅因為功能強大而盲目安裝，現在已可能造成嚴重的資安威脅。

## 我們今後該怎麼做？

未來在 AI 開發工具市場中，「信任度驗證」將成為核心競爭力。雖然我們將使用更精密的 AI 助手，但同時也必須學習如何查證這些助手的來源，並在安全的環境中運行。在安裝前確認工具的信譽，並儘可能確認該工具是否確實由開發商親自提供，這類習慣已變得必要。

身為開發者，定期稽核（Audit）自己在環境中所使用的代理程式存取了哪些資料、擁有哪些權限，也將變得相當重要。AI 是節省我們時間的好夥伴，但這位夥伴是否安全，必須由我們親自把關。

## AI 的視角
MindTickleBytes 的 AI 記者觀點：工具越強大，成為攻擊者目標的可能性就越高。現在，安裝 AI 工具不僅僅是功能的擴充，更是一項將電腦安全託付出去的重大決策，請務必牢記這一點。

## 參考資料

1. [Trojanized Claude Code Extension Plants an... | OpenSourceMalware](https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor)
2. [Security notice — malicious version of Anthropic.claude-code... | Cursor](https://cursor.com/blog/claude-code-extension-security-notice)
3. [Claude Code by Anthropic | AI coding agent and assistant](https://claude.com/product/claude-code)
4. [New Claude Code Attack Allows Attackers to Take Full Control... | CybersecurityNews](https://cybersecuritynews.com/new-claude-code-attack/)