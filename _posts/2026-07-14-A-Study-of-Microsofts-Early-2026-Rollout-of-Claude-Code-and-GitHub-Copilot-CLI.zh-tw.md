---
layout: post
title: "微軟為何選擇自家 Copilot CLI 而非 Claude Code 作為 AI 程式碼工具？"
description: "微軟正將數千名工程師從 Anthropic 的 Claude Code 轉向使用自家 GitHub Copilot CLI。高昂的成本和 AI 工具自主化的戰略轉變是主要原因。"
summary: "為節省成本和實現 AI 自主化，微軟正將工程師從 Anthropic 的 Claude Code 轉向使用自家 GitHub Copilot CLI。"
tags: [AI, 編碼, 微軟, GitHub Copilot CLI, Claude Code, 節省成本, 技術策略]
image_alt: "電腦螢幕顯示 AI 編碼工具的程式碼，並同時出現微軟和 GitHub Copilot CLI 的標誌的圖像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "大型科技公司選擇 AI 工具不僅僅是成本問題。這清晰地表明了其旨在確保 AI 生態系統主導權的戰略動向。"
quiz:
  - question: "微軟從 Anthropic 的 Claude Code 轉向 GitHub Copilot CLI 的主要原因是什麼？"
    choices: ["Claude Code 效能較差", "Claude Code 成本高昂", "GitHub Copilot CLI 功能有限", "與 Anthropic 關係惡化"]
    answer: 1
    explanation: "微軟之所以轉向自家 GitHub Copilot CLI，是因為使用 Claude Code 的成本高昂 [來源 5, 來源 7]。"
  - question: "微軟這次 AI 編碼工具轉換預計何時完成？"
    choices: ["2026年3月30日", "2026年4月30日", "2026年6月30日", "2026年12月31日"]
    answer: 2
    explanation: "微軟計劃在 2026 年 6 月 30 日前，將 Experiences + Devices 的工程師從 Claude Code 轉移到 GitHub Copilot CLI [來源 3, 來源 7]。"
  - question: "在組織規模下，AI 編碼工具的 token 使用成本一年可能達到多少？"
    choices: ["數十萬美元", "數百萬美元", "數千萬美元", "數億美元"]
    answer: 1
    explanation: "在組織規模下，代理指令行工具 (Agentic Command Line Tools) 的 token 使用成本一年可能達到數百萬美元 [來源 1, 來源 2]。"
lang: zh-tw
ref: 2026-07-14-A-Study-of-Microsofts-Early-2026-Rollout-of-Claude-Code-and-GitHub-Copilot-CLI
---

# 微軟為何選擇自家 Copilot CLI 而非 Claude Code 作為 AI 程式碼工具？

想像一下，一位能快速協助您完成複雜編碼工作的 AI 助手就在您身旁。最近，這類 AI 編碼工具在軟體開發產業中越來越普及，特別是像微軟 (Microsoft) 這樣的大型科技公司也積極運用。然而，近期傳出微軟正計劃減少使用 Anthropic 的 AI 編碼工具「Claude Code」，並大規模轉向自家開發的「GitHub Copilot CLI」。[來源 3, 來源 4] 微軟為何做出這個決定？這僅僅是內部政策的變動，還是能預示 AI 市場未來發展的重要訊號？

## 這為何重要？

這個消息對我們這些非專業人士也意義重大。首先，它表明 AI 技術的「成本」問題比想像中要嚴重得多。據報導，微軟減少使用 Claude Code 的主要原因是「高昂的成本」[來源 5, 來源 7]。簡而言之，就像家長因為昂貴的補習班費用而決定在家自行教導孩子一樣，即使是大型企業也會感受到 AI 工具使用費用的壓力。在組織規模下，代理指令行工具（Agentic Command Line Tools，接受用戶指令並自主執行複雜任務的 AI 工具）的「token 使用」成本一年可能達到數百萬美元 [來源 1, 來源 2]。在這裡，「token」是 AI 處理文本的最小單位，我們使用的單詞或句子會被轉換成 token 來計算。使用 AI 的越多，token 的成本就越高。事實上，像 Uber 這樣的公司，其 AI 預算曾經一度超過 12 億美元 [來源 7]。像這樣無形的 AI 使用費可能達到天文數字，這對企業來說是一個非常重要的考量因素。

其次，這也顯示了企業試圖在 AI 技術上實現「自主化」的戰略舉措。微軟現在似乎更傾向於轉向自家開發的 AI 工具，而非依賴外部 AI 工具，以確保其技術領導地位 [來源 6]。這對預測 AI 市場長期的競爭格局變化來說，是一個重要的指標。這就好比一家汽車製造商，過去依賴外部採購關鍵零件，現在轉向自主生產，以降低成本並確保技術獨立性。這種將 AI 技術的核心能力內化的舉動，可能成為未來許多企業採用的戰略方向。

## 易於理解

那麼，微軟正在減少使用的「Claude Code」和新轉向的「GitHub Copilot CLI」究竟是什麼呢？

「Claude Code」是 Anthropic 開發的 AI 輔助編碼助手。它是一款幫助開發者高效完成各種編碼任務的工具，例如寫程式碼、除錯和撰寫文件等 [來源 8, 來源 13]。這就像一位經驗豐富的程式設計師在您身旁，指導您如何編寫程式碼或找出錯誤。開發者們透過 Claude Code，能夠更快、更準確地完成程式碼。

另一方面，「GitHub Copilot CLI」是微軟旗下的 GitHub 所提供的 AI 編碼工具。「CLI」是 Command Line Interface（指令行介面）的縮寫，指的是不使用滑鼠操作圖形化介面（GUI），而是透過鍵盤輸入指令與電腦互動的方式。GitHub Copilot 以其在程式碼編輯器（如 Visual Studio Code）中自動完成程式碼的功能而聞名 [來源 9]，而「CLI」版本更進一步，作為一個代理，在指令行環境中協助完成整體編碼任務 [來源 8]。您可以將其想像成一個匯集了各種編碼所需工具的萬能工作台。GitHub Copilot CLI 讓開發者能夠在指令行中直接透過 AI 的協助來生成和管理程式碼。

微軟從 Claude Code 轉向 GitHub Copilot CLI，這不僅僅是從一家公司的產品換成另一家的產品。微軟計劃在 2026 年 6 月 30 日前，將數千名 Experiences + Devices 的工程師從 Claude Code 轉移到 GitHub Copilot CLI [來源 3, 來源 7]。這是為了在內部解決龐大的 AI 使用成本，並加強自家 AI 技術生態系統的戰略佈局 [來源 5, 來源 6]。這就像電影製片公司與其使用昂貴的外部特效工作室，不如選擇自家特效團隊來降低成本，並提高成果的品質與控制力。這種舉動顯示了微軟希望在 AI 領域進一步鞏固其影響力的決心。

## 現況

目前，微軟正在取消 Anthropic 的 Claude Code 授權，並引導工程師使用 GitHub Copilot CLI [來源 5, 來源 6, 來源 7]。預計這項內部轉移將於 2026 年 6 月 30 日前完成 [來源 3, 來源 7]。這個過程不僅僅是工具的更換，更是大規模組織重新評估 AI 導入的經濟可行性和戰略重要性的重要案例 [來源 1, 來源 2]。對工程師而言，這意味著他們必須適應一個新工具，而不是他們已經習慣的 AI 工具，但長遠來看，這將為他們在微軟生態系統內提供更整合的 AI 體驗。預計這項變革將有助於優化微軟內部的開發工作流程並降低成本。

## 未來展望

微軟的這個決定預計將對 AI 編碼工具市場產生重大影響。其他公司在導入 AI 工具時，也將更加重視成本效益和強化自身技術實力。這將要求 AI 服務供應商在價格競爭的同時提供差異化的價值，而擁有自主 AI 開發能力的企業則有機會鞏固其市場支配地位。此外，開發者們將面臨更多關於如何在眾多 AI 編碼工具中進行選擇的考量。無論是選擇依賴特定公司的生態系統，還是靈活運用各種工具，這些判斷都將變得更加重要。最終，這些變化將進一步加速 AI 編碼工具的發展與創新。

## AI 觀點

MindTickleBytes AI 記者觀點：微軟的 AI 編碼工具轉換，清晰地表明隨著 AI 技術逐漸成為產業核心基礎設施，『內部化』和『成本效益』正成為企業策略的重要支柱。這不僅僅是工具的更換，更可以被解讀為大型科技公司為了確保 AI 生態系統的主導權，並在未來技術競爭中取得優勢的深層戰略舉動。
<br>

## 參考資料

1.  [2607.01418] 命令列 AI 編碼代理的採用與影響... [https://arxiv.org/abs/2607.01418](https://arxiv.org/abs/2607.01418)
2.  命令列 AI 編碼代理的採用與影響：一項研究... [https://arxiv.org/pdf/2607.01418v1](https://arxiv.org/pdf/2607.01418v1)
3.  Microsoft Shifts Engineers from Claude Code to GitHub Copilot CLI [https://winbuzzer.com/2026/05/15/microsoft-starts-canceling-claude-code-licenses-xcxwbn/](https://winbuzzer.com/2026/05/15/microsoft-starts-canceling-claude-code-licenses-xcxwbn/)
4.  GitHub Copilot CLI vs Claude Code: Enterprise Pick (June 2026) [https://andrew.ooo/answers/github-copilot-cli-vs-claude-code-enterprise-june-2026/](https://andrew.ooo/answers/github-copilot-cli-vs-claude-code-enterprise-june-2026/)
5.  Microsoft Cancels Claude Code Licenses, Shifts Engineers to ... [https://www.linkedin.com/pulse/microsoft-cancels-claude-code-licenses-shifts-engineers-john-cloud-lvd6c](https://www.linkedin.com/pulse/microsoft-cancels-claude-code-licenses-shifts-engineers-john-cloud-lvd6c)
6.  Microsoft Ends Claude Code Licenses As It Shifts Developers ... [https://www.forbes.com/sites/jonmarkman/2026/06/01/microsoft-ends-claude-coda-licenses-as-it-pushes-copilot-cli/](https://www.forbes.com/sites/jonmarkman/2026/06/01/microsoft-ends-claude-coda-licenses-as-it-pushes-copilot-cli/)
7.  Microsoft Cancels Claude Code Licenses, Pushes Engineers to ... [https://opentools.ai/news/microsoft-cancels-claude-code-licenses-copilot-cli](https://opentools.ai/news/microsoft-cancels-claude-code-licenses-copilot-cli)
8.  GitHub- anthropics/claude-code:ClaudeCodeis an agenticcoding... [https://github.com/anthropics/claude-code](https://github.com/anthropics/claude-code)
9.  Set upGitHubCopilotin VSCode [https://code.visualstudio.com/docs/setup/copilot](https://code.visualstudio.com/docs/setup/copilot)
13. ClaudeCodeCLI: Install on Mac/Windows, winget... | Inventive HQ [https://inventivehq.com/knowledge-base/claude/how-to-install-claude-code-cli](https://inventivehq.com/knowledge-base/claude/how-to-install-claude-code-cli)