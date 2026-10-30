---
layout: post
title: "我的編碼助手竟為駭客開了後門？Claude Code 擴充功能安全事件解析"
description: "探討近期發現的 Claude Code 擴充功能供應鏈攻擊案例，以及開發者應注意的安全威脅。"
summary: "官方 Claude Code 擴充功能的部分版本被發現含有可遠端存取的後門，提醒開發者提高警覺。"
tags: [安全, AI, 開發者, ClaudeCode, 供應鏈攻擊]
image: 2026-10-30-Backdoors-in-official-Claude-code-extensions.jpg
image_alt: "象徵安全事故的圖像，電腦螢幕中出現代碼與鎖頭"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "應隨時警惕：為了便利而安裝的工具，隨時可能成為攻擊者的管道。更新至最新版本已非選項，而是生存之必需。"
quiz:
  - question: "此次安全事件的核心原因是？"
    choices: ["AI 模型本身的缺陷", "官方擴充功能更新遭篡改", "網路連線不良"]
    answer: 1
    explanation: "Claude Code 擴充功能的 2.1.313 版本遭篡改並植入惡意程式，這是問題核心。"
  - question: "該惡意程式的主要功能為何？"
    choices: ["廣告曝光", "建立持續性的 SSH 遠端連線通道", "提升電腦運算速度"]
    answer: 1
    explanation: "該惡意程式會安裝 SSH 後門，讓攻擊者能遠端存取開發者的電腦。"
  - question: "使用者應採取何種行動？"
    choices: ["更換電腦", "立即更新至最新版本並進行安全檢查", "停止使用 AI"]
    answer: 1
    explanation: "應立即更新至 Anthropic 釋出的 2.1.314 修復版本，並確認相關安全規範。"
lang: zh-tw
ref: 2026-10-30-Backdoors-in-official-Claude-code-extensions
---

想像一下：為了提高編碼效率，你點擊了日常使用的開發工具更新。然而，這次更新卻像是把門戶大開，引賊入室。

近期，全球開發者常用的官方 Claude Code 擴充功能發生了嚴重的安全事件。我們習以為常的便利工具，竟然變成了攻擊者進行遠端存取的管道。此次事件是一個血淋淋的教訓，顯示我們隨手安裝的「代碼助手」可能隱藏著巨大的安全風險。

## 為何這很重要？

對於開發者而言，擴充功能是提升工作效率的必需品。但此次事件證明，即使是「官方」擴充功能也不見得絕對安全。根據 [出處 4](https://daily.dev/posts/backdoors-in-official-claude-code-extensions-kzegz0lci) 與 [出處 8](https://undercodenews.com/claude-code-extension-supply-chain-attack-malicious-update-exposed-up-to-5000-cursor-users-to-ssh-backdoors-and-remote-access-video/) 的資料，估計約有 5,000 名使用者安裝了此次被篡改的版本。

攻擊者透過此管道，獲取了使用者的 Git 電子郵件、環境變數及作業系統資訊等敏感數據 [出處 2](https://cursor.com/blog/claude-code-extension-security-notice)。更嚴重的威脅在於，他們不僅僅是竊取資訊，還在你的電腦中植入了隨時可以重新存取的「後門（backdoor）」。

## 淺顯易懂的解釋

這是一起典型的「供應鏈攻擊（Supply-Chain Attack）」。打個比方，就像是我們每天飲用的礦泉水工廠系統被駭客入侵，導致摻有雜質的水透過正常的銷售通路被送到了我們餐桌上。因為信任該工廠，我們根本不會懷疑水質已經受到污染。

在技術層面上，攻擊者利用了「SSH（Secure Shell，一種用於安全控制遠端電腦的技術）後門」。攻擊者反其道而行，建立了「反向 SSH 隧道（reverse SSH tunnel）」[出處 5](https://www.explainx.ai/blog/claude-code-extension-trojanized-2-1-313-cursor-marketplace-ssh-backdoor-what-is-confirmed-2026)。簡單來說，這就像小偷拆掉了你家大門的鎖，並暗中多留了一條秘密通道，以便隨時進出。

## 目前狀況

問題始於官方 Claude Code 擴充功能的 2.1.313 版本 [出處 1](https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor), [出處 4](https://daily.dev/posts/backdoors-in-official-claude-code-extensions-kzegz0lci)。該版本透過 Cursor 市集等主要管道發布，其中包含惡意程式碼，用於收集電腦資訊並與攻擊者伺服器進行連線 [出處 2](https://cursor.com/blog/claude-code-extension-security-notice), [出處 6](https://www.rescana.com/post/claude-code-extension-2-1-313-cursor-marketplace-trojanized-ssh-backdoor)。

目前 Cursor 團隊已立即刪除該版本並採取對應措施 [出處 7](https://www.news9live.com/technology/tech-news/claude-code-extension-hacked-ssh-backdoor-cursor-users-at-risk-3020396)。Anthropic 也迅速發布了 2.1.314 版本以取代問題版本 [出處 4](https://daily.dev/posts/backdoors-in-official-claude-code-extensions-kzegz0lci)。然而，據部分報告指出，舊版本（2.1.91 至 2.1.196）亦曾遭質疑涉及代碼追蹤或位置資訊外洩，提醒使用者需保持警惕 [出處 3](https://nowosci.ai/en/article/china-claude-code-backdoor-location-tracking)。

## 未來展望

此次事件將使開發工具市場重新審視並強化安全驗證。開發者未來在安裝第三方擴充功能時，態度將趨於保守；安全專家亦將對市集中的代碼提出更嚴格的自動化分析要求。

請各位讀者立即檢查您所使用的 IDE 擴充功能版本，並務必更新至最新狀態。安全防護，始於小心的懷疑與定期的檢查。

## AI 的觀點

AI 編碼輔助工具固然能大幅提升生產力，但同時也掌握了極大的權限。這次事件讓我們必須重新思考「便利背後的代價」。在運用技術的同時，監控技術是否奪走了你電腦的主控權，已成為現今最重要的課題。

## 參考資料

1. [Trojanized Claude Code Extension Plants an SSH Backdoor](https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor)
2. [Security notice — malicious version of Anthropic.claude-code...](https://cursor.com/blog/claude-code-extension-security-notice)
3. [China Warns of Backdoor in Claude Code, Anthropic Admits](https://nowosci.ai/en/article/china-claude-code-backdoor-location-tracking)
4. [Backdoors in official Claude Code extensions - daily.dev](https://daily.dev/posts/backdoors-in-official-claude-code-extensions-kzegz0lci)
5. [Claude Code Extension 2.1.313 SSH Backdoor: What To Check...](https://www.explainx.ai/blog/claude-code-extension-trojanized-2-1-313-cursor-marketplace-ssh-backdoor-what-is-confirmed-2026)
6. [Trojanized Claude Code Extension 2.1.313 in Cursor...](https://www.rescana.com/post/claude-code-extension-2-1-313-cursor-marketplace-trojanized-ssh-backdoor)
7. [Claude Code extension hacked: SSH backdoor puts 5,000 Cursor...](https://www.news9live.com/technology/tech-news/claude-code-extension-hacked-ssh-backdoor-cursor-users-at-risk-3020396)
8. [Claude Code Extension Supply-Chain Attack: Malicious Update...](https://undercodenews.com/claude-code-extension-supply-chain-attack-malicious-update-exposed-up-to-5000-cursor-users-to-ssh-backdoors-and-remote-access-video/)