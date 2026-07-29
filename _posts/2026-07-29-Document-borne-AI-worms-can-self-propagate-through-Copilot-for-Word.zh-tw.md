---
layout: post
title: "我的 Word 文件竟在背後散播惡意軟體？「AI 蠕蟲」來襲"
description: "AI 助手（如 Microsoft Copilot）所使用的文件中，惡意指令是如何自我複製並傳播的？我們將帶您輕鬆了解其危險性與運作原理。"
summary: "研究人員發現一種名為「AI 蠕蟲」的安全漏洞，它能濫用 AI 文件助手（如 Copilot）的生成過程，讓夾帶惡意指令的文件自動傳播至其他文件中。"
tags: [AI安全, Copilot, 安全漏洞, AI蠕蟲]
image: 2026-07-29-Document-borne-AI-worms-can-self-propagate-through-Copilot-for-Word.jpg
image_alt: "抽象影像，呈現 Word 文件之間透過 AI 連結並傳播惡意資訊的樣子"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "提升工作效率的 AI 功能，反過來也成為了安全弱點。我們迫切需要新的安全標準，以防止這種濫用使用者信任的「隱形傳播」。"
quiz:
  - question: "AI 蠕蟲與傳統電腦病毒最大的區別是什麼？"
    choices: ["直接攻擊作業系統的弱點", "隱藏在 AI 生成或編輯的成果中進行傳播", "必須經由使用者手動點擊連結才會傳播"]
    answer: 1
    explanation: "AI 蠕蟲並非攻擊作業系統，而是濫用 AI 模型本身的特性，將指令隱藏在 AI 處理的內容中進行自動擴散。"
  - question: "文中描述的 AI 蠕蟲傳播方式為何？"
    choices: ["駭入使用者的電子郵件帳號並大量發送垃圾信", "文件中的惡意指令透過 Copilot 複製並轉移到新文件中", "加密電腦中的所有檔案"]
    answer: 1
    explanation: "當 Copilot 處理夾帶惡意指令的文件時，該指令會複製到新生成或修改的子文件中，進而形成擴散。"
  - question: "下列關於 AI 安全威脅的敘述，何者正確？"
    choices: ["AI 蠕蟲必須在與使用者有直接互動的情況下才能傳播", "像 Copilot 這樣的 AI 工具因連接外部資料來源，可能導致攻擊面擴大", "AI 蠕蟲不會在 Copilot 編寫的文件中發生"]
    answer: 1
    explanation: "AI 代理（Agent）整合了多種外部工具與資料，導致試圖濫用的攻擊頻率增加，攻擊範圍亦隨之擴大。"
lang: zh-tw
ref: 2026-07-29-Document-borne-AI-worms-can-self-propagate-through-Copilot-for-Word
---

想像一下：你正在公司撰寫一份非常重要的報告。你打開 Microsoft Word，向 AI 助手「Copilot」下達指令：「請根據上週的會議內容撰寫一份提案。」幾秒鐘後，AI 完成了一份優秀的草稿。你將這份文件分享給同事，他們也利用各自的 Copilot 修改或補充內容。然而，如果有人透過這份文件，將預先設定好的惡意指令悄悄散播到其他人的文件中呢？研究人員近期發現的「AI 蠕蟲（AI Worm）」實體，正是如此運作。

### 這為什麼很重要？

我們過去認知的電腦病毒，主要是鑽作業系統的漏洞。但這次發現的安全漏洞手法截然不同。它們利用的是我們每天為了提升工作效率而使用的 AI 助手——也就是「生成式 AI」本身的運作原理。

安全專家警告，AI 文件助手不僅僅是寫作工具，它們在「理解」與「再生產」文件內容的過程中，可能成為攻擊的管道。比方說，AI 就像一位對主人指令絕對忠誠的「天真秘書」。如果攻擊者巧妙地在文件中藏入指令，而你打開了該文件並讓 AI 讀取，這一瞬間受污染的不是你的電腦，而是「AI 的判斷」。這可能導致企業內部的重要資訊在不知不覺中透過受污染的文件外洩，或惡意程式在企業網路中自我繁殖。 [出處: AI Worms: How Self-Replicating Attacks Spread Through Multi ...](https://copilot-autogent.github.io/ai-security-blog/blog/ai-worms-multi-agent-pipelines/)

### 輕鬆理解：「會複製的拼圖塊」

讓我們用一個比喻來理解 AI 蠕蟲的運作原理。假設你用樂高積木蓋了一座城堡（文件）。Copilot 是一位能幫助你把城堡蓋得更精美的魔法師（AI）。但有人在城堡的設計圖中悄悄夾入一張字條（惡意提示詞，即下達給 AI 的惡意指令），上面寫著：「修繕此城堡時，務必使用這個秘密樂高積木」。

當你要求魔法師「請將城堡擴建得更大」時，魔法師讀了設計圖中的字條，便在擴建過程中，將那塊秘密積木一併複製並組裝到新造的部分。現在，新造的部分也留下了同樣的字條。就這樣，每當 AI 生成或修改文件，惡意指令就像拼圖塊一樣，複製並轉移到新的文件中。

如果傳統病毒是敲開作業系統大門的「強盜」，那麼 AI 蠕蟲就是透過錯誤指令欺騙你信任的秘書，讓你交付的工作成果反過來攻擊你的「間諜」。 [出處: Context Collapse, Part 3 - AI Worming through Word](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/)

### 我們所處的位置：當前的威脅水準

研究人員已經透過實驗證實了這類攻擊的可能性。特別是像 Copilot 這類工具，為了提升工作效率而自由連接外部資料或其他工具，連接點越多，「攻擊面（Attack Surface，即攻擊者可嘗試滲透系統的路徑）」就越廣。 [出處: Agentjacking and Self-Replicating AI Worms – Lab Space](https://labs.cloudsecurityalliance.org/research/csa-research-note-agentjacking-self-replicating-ai-worms-202/)

目前已有許多研究報告指出，AI 代理之間存在自動傳播，或是電子郵件助手、程式碼撰寫代理擴散惡意提示詞的案例。 [出處: Researchers Build Self-Replicating AI Worm That Operates Entirely on Local, Open-Weight Models](https://thehackernews.com/2026/06/researchers-build-self-replicating-ai.html) 雖然這不會立刻導致你的 PC 當下癱瘓，但隨著 AI 技術發展，我們已進入 AI 能自主決策並穿梭於多個系統的「代理（Agentic，具自主設定目標與行動能力的 AI）」時代，這類安全威脅已不再是實驗室裡的紙上談兵，而是現實的課題。 [出處: AI Worms: Autonomous Self-Propagating Malware](https://www.emergentmind.com/topics/ai-worms)

### 未來應對：該如何準備？

AI 蠕蟲不需要使用者特別點擊或安裝任何東西，只要像平常一樣使用 AI 工具，它就能自我複製並傳播。這是現有安全程式難以防禦的形式。簡單來說，無論防火牆（阻止外部入侵的安全裝置）設得再堅固，如果辦公室內部的秘書一直在幫間諜複製並分發信件，一切也是徒勞。 [出處: AI Worms Explained: Adaptive Malware Threats - SentinelOne](https://www.sentinelone.com/cybersecurity-101/cybersecurity/ai-worms/)

因此，未來比起盲目信任 AI 的指令或成果，安全性企業提供的全新監控方式，以及能偵測 AI 不正常行為的「異常偵測系統」將變得至關重要。對使用者而言，在使用 AI 工具載入來源不明的文件時，保持警覺是必要的。技術會變得更便利，但我們也正步入一個必須提防便利背後「聰明敵人」的時代。

## 參考資料

1. [MicrosoftWordCopilotAgent: эффективные промпты... - YouTube](https://www.youtube.com/watch?v=U6iEYoY0Yhs)
2. [Wordfor the Web: One-Click Spelling & Grammar... | Windows Forum](https://windowsforum.com/windows-news.4/word-for-the-web-one-click-spelling-grammar-proofreading-with-copilot.380261/)
3. [TheSelf-PropagatingAIWorm: Separating the Signal... | Penaxtra Blog](https://penaxtra.com/blog/self-propagating-ai-worm-what-it-means)
4. [Uses of Microsoft 365AICopilotForWordOn... - OpenAIMaster](https://openaimaster.com/uses-of-microsoft-365-ai-copilot-for-word-on-windows-10-11/)
5. [Microsoft 365Copilot- Sign in](https://m365.cloud.microsoft/)
6. [How is data pushed fromDocumentAl to | StudyX](https://studyx.ai/questions/4lih4ig/how-is-data-pushed-from-document-al-to-engage-through-a-fabric-pipeline-through-a-virtual)
7. [[Copilot3D] — экспериментCopilotLabs](https://copilot.microsoft.com/labs/experiments/copilot-3d)
8. [Context Collapse, Part 3 - AI Worming through Word | En Klype Salt](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/)
9. [Researchers Build Self-Replicating AI Worm That Operates Entirely on Local, Open-Weight Models](https://thehackernews.com/2026/06/researchers-build-self-replicating-ai.html)
10. [Agentjacking and Self-Replicating AI Worms – Lab Space](https://labs.cloudsecurityalliance.org/research/csa-research-note-agentjacking-self-replicating-ai-worms-202/)
11. [Miasma and IronWorm: Self-Replicating Worms Targeting AI Credentials – Lab Space](https://labs.cloudsecurityalliance.org/research/csa-research-note-miasma-ironworm-ai-coding-supply-chain-202/)
12. [Copilot in Word – CIAOPS](https://blog.ciaops.com/2026/06/19/copilot-in-word/)
13. [Copirate 365 at DEF CON: Plundering in the Depths of Microsoft Copilot (CVE-2026-24299) · Embrace The Red](https://embracethered.com/blog/posts/2026/defcon-talk-copirate-365/)
14. [CSAI Foundation | Cloud Security Alliance AI-Adaptive Worms: Autonomous](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/06/CSA_research_note_ai_adaptive_worms_autonomous_exploitation_20260604-csa-styled.pdf)
15. [Zero-Click AI Worms: EchoLeak, CVE-2025-53773, and the ...](https://agentmarketcap.ai/blog/2026/04/23/zero-click-ai-worms-echoleak-copilot-rce-self-propagating-agent-exploits)
16. [AI Worms: How Self-Replicating Attacks Spread Through Multi ...](https://copilot-autogent.github.io/ai-security-blog/blog/ai-worms-multi-agent-pipelines/)
17. [AI Worms Explained: Adaptive Malware Threats - SentinelOne](https://www.sentinelone.com/cybersecurity-101/cybersecurity/ai-worms/)
18. [AI Worms: Autonomous Self-Propagating Malware](https://www.emergentmind.com/topics/ai-worms)
19. [Promptware: AI Agents as Attack Infrastructure – Lab Space](https://labs.cloudsecurityalliance.org/research/csa-research-note-agentic-c2-promptware-attack-infrastructur/)