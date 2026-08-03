---
layout: post
title: "教導 AI『如何工作』能節省 Token 嗎？有趣的實驗結果"
description: "分析將特定技術傳授給 AI 助手的「Codex 技能」對 AI 模型 Token 使用量與效率影響的實驗報告"
summary: "介紹將模組化指令「Codex 技能」提供給 AI 助手，能提升工作效率並改善一致性的實驗結果。"
tags: [AI, Codex, Token節省, 技術實驗, MindTickleBytes]
image: 2026-08-03-Show-HN-Do-Codex-skills-save-tokens-A-six-run-task-size-benchmark.jpg
image_alt: "象徵 AI 助手處理複雜程式設計任務並優化 Token 效率的圖像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 的工作效率不僅取決於模型本身的性能，更在於提供了多麼精細的「指令架構」。Codex 技能是將人類工作方式傳授給 AI 的關鍵媒介。"
quiz:
  - question: "Codex 技能所儲存的檔案格式為何？"
    choices: ["CODE.txt", "SKILL.md", "INSTRUCT.json"]
    answer: 1
    explanation: "Codex 技能透過包含元數據與指令的 SKILL.md 檔案進行管理。"
  - question: "用於在專案中輕鬆安裝 Codex 技能的工具為何？"
    choices: ["skills CLI", "npm install", "git clone"]
    answer: 0
    explanation: "使用 skills CLI 可在專案根目錄輕鬆安裝與管理技能。"
  - question: "本篇文章所介紹「Codex 技能」的主要目的為何？"
    choices: ["提升 AI 的記憶力", "改善工作效率與一致性", "增加模型學習速度"]
    answer: 1
    explanation: "Codex 技能旨在引導 AI 依照預期方式執行特定任務，以提升效率與一致性。"
lang: zh-tw
ref: 2026-08-03-Show-HN-Do-Codex-skills-save-tokens-A-six-run-task-size-benchmark
---

想像一下，每當指派工作給新進實習生時，都要遞給他 100 頁寫滿公司所有規則與流程的 A4 紙。這顯然效率低下。在使用 AI 助手「OpenAI Codex」（輔助撰寫程式碼的 AI 模型）時，也會遇到類似的問題。若每次指派任務都要提供詳細指導，在處理實際工作之前，對話數據的單位「Token」（AI 處理文字的最小單位）就已經消耗殆盡了。

為了克服這個問題，近年來「教導 AI 技能（Skill）」的方式備受矚目。若能預先讓 AI 學習具體的工作手冊，在成本與效率上會有多少差異呢？透過最近進行的實驗，讓我們來一探究竟。

## 為何這很重要？

對於將 AI 運用在工作上的企業與個人而言，「Token」就是成本。Token 使用量增加，不僅營運成本飆升，AI 能處理的任務複雜度或速度也會受限。正如在 [Codex 使用限制（Codex Resets）](https://codex-resets.com/) 等情況下所見，提高 Token 效率是穩定且經濟地利用 AI 助手的必要課題。本次研究顯示，將「如何工作」定義為預先設置的套件傳遞給 AI，能實際達成降低成本並提升工作品質的效果。

## 輕鬆理解：「Codex 技能」是什麼？

「Codex 技能」是教導 AI 執行特定任務的「模組化指令集（Modular instruction bundles，將功能單位化的指令集合）」。根據 [Composio 的相關文件（GitHub - composio-community/awesome-codex-skills）](https://github.com/composio-community/awesome-codex-skills)，每項技能都存放於獨立資料夾中，內部包含名為「SKILL.md」的檔案。該檔案包含了技能名稱、說明，以及 AI 執行任務時需遵守的分步驟指令。[出處：OpenAI Codex 技能（OpenAICodexSkills）](https://agentskill.sh/for/codex)

這可以比喻為修圖 App 的「濾鏡」。未套用濾鏡的照片，使用者必須親自逐一調整色調、對比與亮度；但若套用預設好的「感性濾鏡」，只需按一下按鈕就能獲得理想的照片。Codex 技能也是如此。無需每次從頭到尾給予 AI 指示，只需載入「程式碼生成」、「測試」、「除錯（尋找並修正程式內錯誤）」等特定技能包，AI 就會表現得如同熟練的專家。[出處：代理人技能市場（AgentSkillsMarketplace）](https://skillsmp.com/)

## 現況：目前能運用到什麼程度？

目前 Codex 技能生態系正快速成長。已開發出超過 34,788 種技能，涵蓋程式碼生成、測試、除錯、部署，甚至能執行自主開發任務。[出處：OpenAI Codex 技能（OpenAICodexSkills）](https://agentskill.sh/for/codex)

此外，不僅止於文字作業。例如在 UI 設計領域，透過與瀏覽器連動，AI 能直接進行畫面渲染，並根據斷點（Breakpoint，根據畫面尺寸調整佈局的點）修改 UI。[出處：設計用的 Codex（Codexдля дизайна）](https://open-design.ai/ru/agents/codex-design/) 這些技能可透過「skills CLI（命令列介面工具）」輕鬆安裝在專案根目錄，一旦安裝，AI 就會在多個會話中持續參照該指南。[出處：Codex 用技能（SkillsforCodex）](https://www.skills.sh/agent/codex)

## 未來會如何發展？

近期有實驗正在針對不同任務規模（Task-size）的環境，比較「精簡技能（Lean skills）」與既有方式相比能節省多少 Token。[出處：Codex 技能 Token 節省實驗（DoCodexskillssavetokens?）](https://community.openai.com/t/do-codex-skills-save-tokens-six-controlled-gpt-5-6-sol-runs/1388837) 未來，我們將迎來一個時代，從數萬種技能中組合出最適合自己任務的最佳技能，將 AI 助手升級至「個人秘書」的等級。目前，動畫製作、網站建置、App 自動化等各種實務案例已陸續出現。[出處：2026 年前 10 大 Codex 技能（Top 10CodexSkillsin 2026）](https://composio.dev/content/top-codex-skills)

## MindTickleBytes AI 記者觀點

以「技能」形式向 AI 提供精細指令，是將 AI 從單純工具進化為真正合作夥伴的過程。我們教導 AI 的規則越清晰，AI 就越能以更少的資源創造更大的價值。現在，超越單純指令 AI 的階段，教導 AI 如同專家般工作的「技能時代」已經來臨。

## 參考資料

1. [Codex 技能 Token 節省實驗（DoCodexskillssavetokens?）](https://community.openai.com/t/do-codex-skills-save-tokens-six-controlled-gpt-5-6-sol-runs/1388837)
2. [Codex 使用限制（Codex Resets）](https://codex-resets.com/)
3. [OpenAI Codex 技能（OpenAICodexSkills）](https://agentskill.sh/for/codex)
4. [GitHub - composio-community/awesome-codex-skills](https://github.com/composio-community/awesome-codex-skills)
5. [2026 年前 10 大 Codex 技能（Top 10CodexSkillsin 2026）](https://composio.dev/content/top-codex-skills)
6. [代理人技能市場（AgentSkillsMarketplace）](https://skillsmp.com/)
7. [Codex 用技能（SkillsforCodex）](https://www.skills.sh/agent/codex)
8. [Claude 程式碼與 Codex 的 10 大設計技能（Top 10 DesignSkillsfor ClaudeCodeandCodex）](https://composio.dev/content/top-design-skills)
9. [設計用的 Codex（Codexдля дизайна）](https://open-design.ai/ru/agents/codex-design/)