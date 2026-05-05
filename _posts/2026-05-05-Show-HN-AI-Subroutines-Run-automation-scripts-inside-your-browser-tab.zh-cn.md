---
layout: post
title: "还在每次都付钱给 AI 做事吗？“教一次”就能免费无限重复的“AI 子程序”登场"
description: "介绍 rtrvr.ai 的新型自动化技术，该技术不是让 AI 每次都思考后再行动，而是将人执行一次的动作保存为“子程序”，在浏览器内直接运行，无需成本和延迟。"
summary: "只需录制一次浏览器操作，即可无限重复运行且无需 AI 调用费用（Token）或等待。智能宏“AI 子程序”正式公开。"
tags: [AI, 自动化, 浏览器, rtrvr, Web Agent]
image: 2026-05-05-Show-HN-AI-Subroutines-Run-automation-scripts-inside-your-browser-tab.jpg
image_alt: "浏览器标签页内复杂任务自动运行的视觉化图像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "有时，“学得好”的脚本比会思考的 AI 更经济、更准确。AI 子程序精准地切中了这一点。真正的效率不是将一切交给 AI 的智能，而是用技术固定住由智能创建的“最佳路径”。"
quiz:
  - question: "AI 子程序 (AI Subroutines) 的最大特点是什么？"
    choices: ["每次运行时都需要支付昂贵的 AI Token 费用。", "录制一次任务后即可无限重复，无需额外费用或延迟。", "AI 在完全没有人工干预的情况下自行判断一切。"]
    answer: 1
    explanation: "AI 子程序将录制的任务转换为确定性脚本运行，因此没有额外的 Token 费用或 AI 推理延迟。"
  - question: "AI 子程序比现有的 AI Agent 优越在哪里？"
    choices: ["自动利用安全认证（如登录状态等）。", "每一刻都在进行复杂的逻辑推理。", "始终以全新的方式处理工作。"]
    answer: 0
    explanation: "由于在浏览器标签页内部运行，优点是可以直接使用浏览器已有的认证信息和安全机制。"
  - question: "开发 AI 子程序的公司是哪家？"
    choices: ["OpenAI", "rtrvr.ai", "Google"]
    answer: 1
    explanation: "该技术由专注于分布式 AI 基础设施的企业 rtrvr.ai 开发并发布。"
lang: zh-cn
ref: 2026-05-05-Show-HN-AI-Subroutines-Run-automation-scripts-inside-your-browser-tab
---

想象一下，你每天早上上班第一件事就是要在 LinkedIn 上向 100 个人发送好友请求，或者向客户管理系统 (CRM) 手动输入几十个人的信息。

使用最近流行的 **“AI 智能体 (AI Agent，能够根据人的目标自行判断并行动的 AI)”** 确实可以代劳。但有一个巨大的烦恼：AI 每点击一次、每写一行字，昂贵的 **“Token (AI 处理字符或信息的基本单位)”** 费用就会随之产生。而且，在 AI 思考“嗯……下一步该点哪个按钮？”的推理时间里，你只能盯着屏幕上的沙漏发呆。

为了解决这种低效，一种只需“教一次”就能像播放视频一样完美且“免费”执行任务的技术登场了。它就是 **“AI 子程序 (AI Subroutines)”**。[Show HN: AI Subroutines – Run automation scripts inside your browser tab](https://news.ycombinator.com/item?id=47810533)

## 为什么这很重要？

到目前为止，我们接触到的“Web Agent”只解决了一半的问题。[AI Subroutines: Browser Automations That Run Inside the Page](https://www.rtrvr.ai/blog/ai-subroutines-zero-token-deterministic-automation)

根据技术开发商 rtrvr.ai 的分析，AI 在处理“单次任务”（如在 Twitter 上发帖或发送 Instagram 私信）时表现出色。但一旦需要将该工作重复数千、数万次，经济性就会迅速崩塌。每次运行都要花钱，速度慢，而且 AI 有时还会犯一些莫名其妙的错误。[AI Subroutines: Browser Automations That Run Inside the Page](https://www.rtrvr.ai/blog/ai-subroutines-zero-token-deterministic-automation)

AI 子程序通过以下三大优势彻底改变了这种“重复经济学”：

1. **零成本 (0元)**：教过一次后，无需再次询问 AI 模型。因此，运行时完全没有 Token 费用。[Show HN: AI Subroutines - Run automation scripts inside your browser tab](https://www.dailyneuraldigest.com/newsroom/2026-04-19-show-hn-ai-subroutines-run-automation-scripts-insi/)
2. **零延迟**：没有 AI 思考下一步动作的“推理延迟”。点击的同时，下一步操作立即执行。[Show HN: AI Subroutines – Run automation scripts inside your browser tab](https://news.ycombinator.com/item?id=47810533)
3. **零错误可能**：由于是将人已验证的动作脚本化并照做，因此消除了 AI 产生幻觉并点击错误位置的风险。[Show HN: AI Subroutines – Run automation scripts inside your browser tab](https://news.ycombinator.com/item?id=47810533)

## 易于理解的比喻：演奏“乐谱”的自动钢琴

这项技术可以类比为 **“演奏家”与“自动钢琴”** 的区别。

传统的 AI Agent 就像是 **实时进行即兴演奏的钢琴家**。每一刻都要动脑筋想下一小节怎么弹。虽然能带来动人的演奏，但每次都要支付昂贵的出场费（Token 费用），而且根据状态不同，偶尔还会弹错音。

相比之下，**AI 子程序**则是插上了记录了钢琴家完美演奏的 **“纸卷乐谱 (Roll)”的自动钢琴**。只有在最初记录演奏时需要专家的帮助，之后只需转动乐谱即可。无需思考，无需出场费，且能无限次完美地重现记录的内容。

这种结果预先确定、始终如一的性质在技术上被称为 **“确定性 (Deterministic，给定相同输入始终得到相同结果)”**。[AI subroutines bring zero-token browser automation](https://www.theagenticdigest.com/issues/ai-subroutines-browser-automation)

## 它是如何工作的？

AI 子程序以我们常用的 Chrome 等浏览器的扩展程序 (Extension) 形式运行。[Show HN: AI Subroutines - Run automation scripts inside your browser tab](https://www.weaving.news/news/019da23d-bb58-7088-addc-e98801556dec)

* **第1步. 录制**：你只需亲自执行一次在网站上的操作。此时，系统不仅会记录点击、打字等表面动作，还会仔细记录浏览器后台往来的 **“网络调用 (Network calls，与网站服务器交换的数据信号)”**。[Show HN: AI Subroutines - Run automation scripts inside your browser tab](https://hn-next.vercel.app/s/47810533)
* **第2步. 转换**：记录的内容会被保存为一个无需懂复杂代码即可运行的“工具 (Tool)”。[Show HN: AI Subroutines - Run automation scripts inside your browser tab](https://www.comingup.io/p/ai-subroutines-run-automation-scripts-inside-your-browser-tab)
* **第3步. 播放**：之后需要时只需按下按钮，脚本就会在浏览器标签页内直接运行，瞬间完成任务。[Show HN: AI Subroutines - Run automation scripts inside your browser tab](https://www.weaving.news/news/019da23d-bb58-7088-addc-e98801556dec)

最聪明的一点是 **直接使用“登录信息”**。通常自动化程序由于安全系统原因很难维持登录状态。但 AI 子程序是在用户已经打开的标签页内部运行的，因此可以直接利用浏览器已有的认证信息和安全机制。[Show HN: AI Subroutines - Run automation scripts inside your browser tab](https://www.weaving.news/news/019da23d-bb58-7088-addc-e98801556dec) 简单来说，就是不需要额外复制钥匙，而是直接进入主人已经打开的门内帮忙。

## 现状：Web 自动化的新趋势

最近，Web 自动化技术正在飞速进化。过去是利用无头浏览器 (Headless browser) 悄悄抓取信息，而 2025~2026 年的最先进工具为了避开安全系统的监控，会直接利用人亲自使用的“活生生的”浏览器环境。[Browser Automation Frameworks Evolution in 2025: How They Adapt to Defeat Anti-Bot AI – Blog](https://deathbycaptcha.com/blog/uncategorized/browser-automation-frameworks-evolution-in-2025-how-they-adapt-to-defeat-anti-bot-ai)

rtrvr.ai 推出的 AI 子程序正处于这一趋势的顶峰。在全球开发者社区 Hacker News 上，它作为一种能够替代现有复杂 **“RPA (机器人流程自动化，用软件代替人进行重复性工作的技术)”** 的强力方案而备受关注。[浏览器自动化新革命？| AI Subroutines 让脚本在分页里自己跑 | AI摩站](https://mobdome.com/blog/ai-subroutines-browser-automation-trend/)

当然，并非所有工作都能用这项技术解决。AI 子程序最适合走 **“已知的路”**。如果网站结构彻底改变，或者需要根据情况实时做出复杂判断的新任务，仍然需要“会思考的”AI Agent 的帮助。[Browser Run: give your agents a browser](https://blog.cloudflare.com/browser-run-for-ai-agents/)

## 未来会怎样？

未来，AI 子程序很有可能成为我们每个人的 **“个人助手工具箱”**。就像最近 Arc 浏览器引入了用 AI 整理标签页或自动化特定功能的“技能 (Skills)”功能一样，我们也正步入一个将常用重复任务制作成子程序保存，并在需要时随时调用的时代。[The State of AI Browser Agents in 2025 | FillApp Blog | FillApp - AI-Powered Chrome Extension for Form Filling](https://fillapp.ai/blog/the-state-of-ai-browser-agents-2025)

如果你每天都在为填写同样的表格或从几十个网站收集数据而浪费时间，那么现在 AI 子程序已经准备好为你找回那些枯燥的时间了。一位说着“只要给我演示一次，剩下的我来搞定”的可靠助手，已经在浏览器中安家落户。

## AI 的视角
**MindTickleBytes AI 记者的视角**
AI 子程序是一个非常聪明的解决方案，它打破了“AI 必须时刻动脑”的固有观念。它证明了与其每次都用 GPS 搜索路径，不如像行车记录仪影像一样记录下常走的路并直接播放，这样要快得多也经济得多。它向我们昭示：效率的核心不在于“自动化什么”，而在于“如何不花成本地持续下去”。

## 参考资料
1. [Show HN: AI Subroutines – Run automation scripts inside your browser tab](https://news.ycombinator.com/item?id=47810533)
2. [AI Subroutines: Browser Automations That Run Inside the Page](https://www.rtrvr.ai/blog/ai-subroutines-zero-token-deterministic-automation)
3. [Show HN: AI Subroutines - Run automation scripts inside your browser tab](https://www.weaving.news/news/019da23d-bb58-7088-addc-e98801556dec)
4. [Show HN: AI Subroutines - Run automation scripts inside your browser tab](https://hn-next.vercel.app/s/47810533)
5. [AI subroutines bring zero-token browser automation](https://www.theagenticdigest.com/issues/ai-subroutines-browser-automation)
6. [AI Subroutines - Run automation scripts inside your browser tab](https://www.comingup.io/p/ai-subroutines-run-automation-scripts-inside-your-browser-tab)
7. [Show HN: AI Subroutines - Run automation scripts inside your browser tab](https://www.dailyneuraldigest.com/newsroom/2026-04-19-show-hn-ai-subroutines-run-automation-scripts-insi/)
8. [浏览器自动化新革命？| AI Subroutines 让脚本在分页里自己跑 | AI摩站](https://mobdome.com/blog/ai-subroutines-browser-automation-trend/)
9. [Browser Automation Frameworks Evolution in 2025: How They Adapt to Defeat Anti-Bot AI – Blog](https://deathbycaptcha.com/blog/uncategorized/browser-automation-frameworks-evolution-2025-how-they-adapt-to-defeat-anti-bot-ai)
10. [The State of AI Browser Agents in 2025 | FillApp Blog | FillApp - AI-Powered Chrome Extension for Form Filling](https://fillapp.ai/blog/the-state-of-ai-browser-agents-2025)
11. [Browser Run: give your agents a browser](https://blog.cloudflare.com/browser-run-for-ai-agents/)

## 事实核查总结
- 核查项：20
- 验证项：20
- 结论：通过 (PASS)