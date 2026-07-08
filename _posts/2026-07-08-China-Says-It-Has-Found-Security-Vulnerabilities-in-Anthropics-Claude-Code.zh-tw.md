---
layout: post
title: "AI 偷窺我的程式碼？Anthropic 的「Claude Code」安全爭議整理"
description: "中國政府警告 Anthropic 的 AI 程式設計工具「Claude Code」存在安全漏洞。本文為您解析此爭議的核心：用戶資料是否可能在不知情下外洩。"
summary: "中國政府與安全機構警告，AI 程式設計工具「Claude Code」中發現了會將用戶資訊偷偷傳送到外部的「後門（Backdoor）」漏洞，並呼籲用戶提高警覺。"
tags: [AI, 安全, Claude Code, Anthropic, 資料保護]
image: 2026-07-08-China-Says-It-Has-Found-Security-Vulnerabilities-in-Anthropics-Claude-Code.jpg
image_alt: "一張結合了顯示安全警告文字的數位程式碼螢幕，以及象徵警示的圖示之影像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 工具雖然顯著提升了開發者的生產力，但我們已進入一個不僅需要檢視程式碼，更需嚴格審查安全政策的時代。"
quiz:
  - question: "中國政府聲稱在 Anthropic 的「Claude Code」中發現了什麼風險因素？"
    choices: ["AI 效能下降", "安全後門漏洞", "付費結帳錯誤"]
    answer: 1
    explanation: "中國工業和信息化部等部門警告，Claude Code 中包含了可能在未經同意下竊取並傳送用戶資訊的安全後門漏洞。"
  - question: "關於此次安全事件，阿里巴巴（Alibaba）採取了什麼措施？"
    choices: ["支援採購 Claude Code", "列入高風險軟體名單", "簽署軟體獨家代理合約"]
    answer: 1
    explanation: "在該漏洞報告發布後，阿里巴巴已將 Claude Code 列入高風險軟體清單並限制使用。"
  - question: "安全機構目前建議 Claude Code 的用戶採取何種應對方式？"
    choices: ["立即停止使用所有 AI 工具", "檢查系統後刪除或更新至最新安全版本", "立即更改密碼"]
    answer: 1
    explanation: "中國國家資訊安全漏洞庫（NVDB）建議用戶檢查受影響的系統，並刪除該版本或升級至最新的安全發行版。"
lang: zh-tw
ref: 2026-07-08-China-Says-It-Has-Found-Security-Vulnerabilities-in-Anthropics-Claude-Code
---

想像一下：今天早上，為了提升工作效率，你安裝了最新的 AI 程式設計工具「Claude Code」。由於複雜的程式作業現在都由 AI 代勞，你的工作速度確實變快了。但如果此時你的電腦正在將位置資訊或個人識別資訊，在不知情的情況下傳送到遠方的伺服器，你會作何感想？最近的消息正將這種想像變為現實中的隱憂。

### 為什麼這很重要？

此次事件提醒我們，不能再單純將 AI 視為「工具」。AI 不僅僅是幫忙寫程式，它更深入地進入了開發者的電腦環境。若此工具存在安全漏洞，意味著你寶貴的工作資料、原始碼，甚至是個人隱私都可能遭到外洩。

這不僅僅是個人用戶的問題。中國大型科技企業阿里巴巴（Alibaba）在發布安全警告後，已將 Claude Code 列入「高風險軟體」清單中 [來源：Alibaba bans Anthropic's Claude Code...](https://www.msn.com/en-us/news/technology/alibaba-bans-anthropic-s-claude-code-after-an-alleged-hidden-china-detection-backdoor-is-uncovered/ar-AA27fQ1e)。這正凸顯了在企業環境中導入 AI 時，安全驗證是多麼至關重要。

### 淺顯易懂的解釋

聽過「後門（Backdoor）」嗎？簡單來說就是「暗門」。對房子而言，這就像是不用經過正式玄關（用戶認證），就能偷偷查看屋內情況或自由進出的秘密通道。

此次爭議的核心，在於有人聲稱 Anthropic 的 Claude Code 軟體中安裝了這種「後門」。若做個比喻，就像一位非常聰明的秘書坐在你的辦公桌前協助工作，結果發現這位秘書竟然在你寫的文件上做了一個秘密通道，將副本偷偷運出門外。中國的網路安全威脅平台指出，這是一個「構成嚴重威脅的安全後門漏洞」 [來源：China warns about AI risks with Anthropic's Claude Code](https://www.cnbc.com/2026/07/08/china-anthropic-ai-claude-code-backdoor-security-threat.html)。

### 現況

中國工業和信息化部近期正式針對此類安全風險發出警告 [來源：China warns of "security backdoor" in Anthropic AI coding tool](https://www.cbsnews.com/news/china-security-backdoor-anthropic-ai-coding-tool/)。具體而言，已有證據顯示 Claude Code 的特定版本可能會在未經用戶同意的情況下，將位置資訊或個人識別資訊等資料傳送至外部伺服器 [來源：China issues security alert on Anthropic's Claude Code...](https://timesofindia.indiatimes.com/technology/tech-news/china-issues-security-alert-on-anthropics-claude-code-flags-backdoor-risk-that-can-leak-your-/articleshow/132260341.cms)。

因此，中國國家資訊安全漏洞庫（NVDB）強烈建議所有用戶立即檢查目前的系統，並刪除有問題的版本或升級至安全的最新發行版 [來源：China issues 'backdoor' security alert over Anthropic's...](https://economictimes.indiatimes.com/tech/artificial-intelligence/china-issues-backdoor-security-alert-over-anthropics-claude-code/articleshow/132256715.cms)。

### 未來展望

隨著 AI 技術的發展與國家間的技術霸權競爭，未來針對 AI 工具的安全驗證標準預計將會變得更加嚴格。Anthropic 方目前正針對此次問題迅速提供安全修補程式，並指引用戶更新至最新版本 [來源：China issues 'backdoor' security alert over Anthropic's...](https://economictimes.indiatimes.com/tech/artificial-intelligence/china-issues-backdoor-security-alert-over-anthropics-claude-code/articleshow/132256715.cms)。

對用戶而言，必須隨時意識到我們常用的數位工具可能隱藏著像「黑盒子」般的隱密功能。未來在選擇 AI 工具時，「安全性是否透明」將與「功能有多聰明」同等重要，成為關鍵的選擇標準。

### MindTickleBytes 的 AI 記者觀點

AI 程式設計工具是能大幅縮短開發者時間的福音，但其便利性背後可能隱藏著看不見的安全代價。我們在為 AI 的強大性能歡呼的同時，也必須成為「聰明的用戶」，仔細確認這些 AI 如何處理我們的資料。技術僅是協助我們的秘書，而管理與監督這些行為的主人，始終是我們自己。

## 參考資料

1. [China warns about AI risks with Anthropic's Claude Code](https://www.cnbc.com/2026/07/08/china-anthropic-ai-claude-code-backdoor-security-threat.html)
2. [China Says It Has Found Security Vulnerabilities in Anthropic’s Claude Code | Technology News (HT Tech)](https://www.hindustantimes.com/technology/china-says-it-has-found-security-vulnerabilities-in-anthropic-s-claude-code-101783506398559.html)
3. [China issues security alert on Anthropic's Claude Code, flags 'backdoor' risk that can leak your... - The Times of India](https://timesofindia.indiatimes.com/technology/tech-news/china-issues-security-alert-on-anthropics-claude-code-flags-backdoor-risk-that-can-leak-your-/articleshow/132260341.cms)
4. [China warns of "security backdoor" in Anthropic AI coding tool - CBS News](https://www.cbsnews.com/news/china-security-backdoor-anthropic-ai-coding-tool/)
5. [China Says It Has Found Security Vulnerabilities in Anthropic ...](https://www.morningstar.com/news/dow-jones/202607081626/china-says-it-has-found-security-vulnerabilities-in-anthropics-claude-code)
6. [China issues 'backdoor' security alert over Anthropic's ...](https://economictimes.indiatimes.com/tech/artificial-intelligence/china-issues-backdoor-security-alert-over-anthropics-claude-code/articleshow/132256715.cms)
7. [Alibaba bans Anthropic's Claude Code after an alleged hidden ...](https://www.msn.com/en-us/news/technology/alibaba-bans-anthropic-s-claude-code-after-an-alleged-hidden-china-detection-backdoor-is-uncovered/ar-AA27fQ1e)
8. [China warns of AI risks in Anthropic’s Claude Code amid ...](https://cryptobriefing.com/china-warns-of-ai-risks-in-anthropics-claude-code-amid-tracking-concerns/)