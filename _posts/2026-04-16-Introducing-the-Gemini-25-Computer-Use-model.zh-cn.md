---
layout: post
title: "代替我移动鼠标的 AI 助手？谷歌“Gemini 2.5 Computer Use”全解析"
description: "为您介绍谷歌发布的 Gemini 2.5 Computer Use 模型。本文将为您通俗易懂地解释 AI 如何像人一样观察屏幕、点击并实现任务自动化，以及它将给我们的生活带来的改变。"
summary: "谷歌的“Gemini 2.5 Computer Use”是一项让 AI 直接移动鼠标、输入键盘，并代表用户完成复杂网页任务的技术。"
tags: [Gemini, 谷歌AI, AI智能体, 办公自动化]
image: 2026-04-16-Introducing-the-Gemini-25-Computer-Use-model.jpg
image_alt: "分析电脑屏幕并操作鼠标光标的 AI 智能体概念图"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "现在的 AI 已不再仅仅是对话的对象，它正在进化成为能够代替我们操作实际工具的能干助手。"
quiz:
  - question: "Gemini 2.5 Computer Use 模型为了执行任务首先会做的动作是什么？"
    choices: ["直接修改代码", "拍摄屏幕截图进行分析", "向用户提问"]
    answer: 1
    explanation: "该模型通过“智能体循环”首先获取屏幕截图以掌握情况，然后决定后续动作。"
  - question: "该模型是基于哪款现有模型的视觉和推理能力构建的？"
    choices: ["Gemini 1.0 Pro", "Gemini 1.5 Flash", "Gemini 2.5 Pro"]
    answer: 2
    explanation: "Gemini 2.5 Computer Use 是基于 Gemini 2.5 Pro 强大的视觉理解和推理能力设计的。"
  - question: "关于该模型性能的描述，以下哪项是正确的？"
    choices: ["反应速度比竞争模型慢", "在网页及移动端控制基准测试中超越了竞争对手", "目前还无法使用需要登录的网站"]
    answer: 1
    explanation: "Gemini 2.5 Computer Use 在多项性能指标上领先于竞争对手，特别是具有低延迟的特点。"
lang: zh-cn
ref: 2026-04-16-Introducing-the-Gemini-25-Computer-Use-model
---

想象一下，你在下班路上掏出智能手机，随口说一句：“帮我订一张下周去济州岛最便宜的双人往返机票。”然后，AI 就会直接访问航空公司网站，选择日期，对比数十家航空公司的价格，并根据你的个人信息自动填好预订表单。现在的世界正开启一个新阶段：AI 不再只是建议你“如何预订”，而是直接操纵你的电脑鼠标和键盘来完成工作。

谷歌于 2025 年 10 月 7 日发布了一款能像人一样操作电脑的特殊 AI 模型——**“Gemini 2.5 Computer Use”** [IntroducingtheGemini2.5ComputerUsemodel](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-computer-use-model/) [Google releases a preview of itsGemini2.5ComputerUseAImodel...](https://gigazine.net/gsc_news/en/20251008-google-gemini-2-5-computer-use)。这项技术正准备彻底改变我们与电脑互动的方式。

## 为什么这很重要？

到目前为止，我们遇到的 AI 主要是擅长“说话”的秘书。你问它问题，它给你答案，或者帮你总结复杂的文档。但要完成实际工作，我们需要打开浏览器、点击按钮、登录并逐一输入数据。这个过程在专业术语中被称为**界面（Interface，用户为了与电脑沟通而使用的屏幕或工具）**操作。

Gemini 2.5 Computer Use 的出现意味着 AI 已从“语言”阶段进入了“执行”阶段。谷歌的这款模型能直接“观察”并理解网页浏览器或安卓应用屏幕，并模仿人类进行点击按钮、输入文本、滚动屏幕等物理动作 [Google News - News aboutGemini- Overview](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lDM3NUYkR4SHN2TllKS192ekVpZ0FQAQ?hl=en-NA&gl=NA&ceid=NA:en) [Google UnveilsGemini2.5ComputerUseThat Clicks... | Beebom](https://beebom.com/google-unveils-gemini-2-5-computer-use-that-clicks-types-scrolls-like-humans/)。

简单来说，这是一个学会了如何使用电脑的 AI。对于职场人士，这预示着将 Excel 数据手动录入网站等乏味重复工作的终结；对于普通用户，这预示着一个真正的**智能体（Agent，无需人类干预即可自主判断并达成目标的 AI 程序）**的诞生，它能代劳复杂的网银操作或购物流程 [IntroducingGemini2.5ComputerUse: AI for web and... | LinkedIn](https://www.linkedin.com/posts/googleaidevs_introducing-gemini-25-computer-use-available-activity-7381415403840864256-ycSe) [2025 完全 가이드: Gemini 2.5 Computer Use 모델 - AI Agent 인터페이스 제어의 혁명적 돌파구](https://velog.io/@czmilo/2025-완전-가이드-Gemini-2.5-Computer-Use-모델-AI-Agent-인터페이스-제어의-혁명적-돌파구)。

## 通俗易懂：AI 如何使用我的电脑？

该模型的运作方式与我们用眼睛看显示器、用手移动鼠标的过程惊人地相似。这被称为**“智能体循环（Agent Loop）”**，主要包含三个阶段的循环过程 [IntroducingtheGemini2.5ComputerUsemodel](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-computer-use-model/)：

1.  **观察（看）**：AI 拍摄当前电脑屏幕的截图并进行确认。就像我们盯着显示器思考“该点哪里？”一样。
2.  **思考（想）**：分析截取的画面，判断按钮在哪里，以及在当前情况下需要输入什么。此时，AI 不仅仅是看图像，还会进行推理，例如：“哦，屏幕中央的蓝色按钮是‘支付’按钮！”然后制定具体的行动计划，比如“点击坐标 (500, 300) 的位置” [Computer Use | Gemini API | Google AI for Developers](https://ai.google.dev/gemini-api/docs/computer-use)。
3.  **执行（做）**：根据制定的计划，实际移动鼠标光标或用键盘输入文字。

**打个比方，这个模型就像一个高性能的自动驾驶 GPS。** 原理是 GPS 确认当前位置（截图），决定为了到达目的地该在哪个路口转弯（推理），然后指示驾驶员（执行器）转动方向盘。Gemini 2.5 Computer Use 会在极短的时间内无限次重复这个过程，向着目标迈进。

之所以能完成这种高难度任务，是因为该模型继承了谷歌最聪明的模型之一——“Gemini 2.5 Pro”强大的视觉理解和逻辑推理能力 [IntroducingGemini2.5ComputerUse: AI for web and... | LinkedIn](https://www.linkedin.com/posts/googleaidevs_introducing-gemini-25-computer-use-available-activity-7381415403840864256-ycSe) [Gemini 2.5 Computer Use 완벽 분석 및 실전 코드](https://fornewchallenge.tistory.com/entry/Gemini-25-Computer-Use-완벽-분석-및-실전-코드)。

## 现状：它有多聪明？

据谷歌称，Gemini 2.5 Computer Use 已经远远超越了只会听令点击的初级水平。

*   **执行复杂任务的能力**：它不只是点击一个按钮，而是能从下拉菜单中选择选项，叠加应用多个过滤器，甚至在出于安全考虑需要登录的复杂网站上也能熟练处理任务 [Google LaunchesGemini2.5ComputerUseModelfor Browser...](https://www.allaboutai.com/ai-news/google-launches-gemini-2-5-computer-use-model-for-browser-automation/) [Google releases a preview of itsGemini2.5ComputerUseAImodel...](https://gigazine.net/gsc_news/en/20251008-google-gemini-2-5-computer-use)。
*   **碾压竞争对手的成绩**：在衡量网页及移动端控制能力的各项**基准测试（Benchmark，用于比较 AI 性能的标准测试）**中，它取得了超越 OpenAI 或 Anthropic 的 Claude Sonnet 4.5 等强劲竞争模型的惊人成绩 [2025 Complete Guide: Gemini 2.5 Computer Use Model - Revolutionary ...](https://dev.to/czmilo/2025-complete-guide-gemini-25-computer-use-model-revolutionary-breakthrough-in-ai-agent-133) [Google UnveilsGemini2.5ComputerUseThat Clicks... | Beebom](https://beebom.com/google-unveils-gemini-2-5-computer-use-that-clicks-types-scrolls-like-humans/)。
*   **眨眼间的反应速度**：让 AI 执行指令时，最令人沮丧的就是“等待”。与其他 AI 相比，该模型从发出指令到实际行动之间的**延迟（Latency，系统做出反应所需的时间）**非常短，操作更加流畅自然 [2025 Complete Guide: Gemini 2.5 Computer Use Model - Revolutionary ...](https://dev.to/czmilo/2025-complete-guide-gemini-25-computer-use-model-revolutionary-breakthrough-in-ai-agent-133) [2025 완전 가이드: Gemini 2.5 Computer Use 모델 - AI Agent 인터페이스 제어의 혁명적 돌파구](https://velog.io/@czmilo/2025-완전-가이드-Gemini-2.5-Computer-Use-모델-AI-Agent-인터페이스-제어의-혁명적-돌파구)。

目前，该模型已通过 Gemini API 以预览版形式向开发者开放，众多企业已在利用它测试自动化工具 [IntroducingGemini2.5ComputerUse: AI for web and... | LinkedIn](https://www.linkedin.com/posts/googleaidevs_introducing-gemini-25-computer-use-available-activity-7381415403840864256-ycSe) [Google LaunchesGemini2.5for AI That Clicks and Scrolls](https://geekflare.com/news/ai-that-clicks-and-scrolls-google-introduces-gemini-2-5-computer-use-model/)。

## 未来会怎样？

Gemini 2.5 Computer Use 的出现不仅仅是技术进步，更吹响了“AI 智能体时代”开启的号角。谷歌选择在 OpenAI 重大活动的次日发布该模型，充分说明了全球科技巨头对这一领域的重视程度 [Google launchesGemini2.5ComputerUseto rival... | The Tech Buzz](https://www.techbuzz.ai/articles/google-launches-gemini-2-5-computer-use-to-rival-openai-agents)。

我们很快将目睹以下惊人的变化：

1.  **真正的“一人一秘”时代**：不再只是“告诉你怎么做”的秘书，而是“帮我处理好”并直接交付结果的秘书。从旅行预订到报销处理，所有繁琐事务都将由 AI 承担。
2.  **劳动的质变**：将数据从 Excel 搬运到网页，或者注册数百个商品信息等单纯重复的网页任务将会消失。人类将能专注于更具创意、更高层次的思考 [2025 Complete Guide: Gemini 2.5 Computer Use Model - Revolutionary ...](https://dev.to/czmilo/2025-complete-guide-gemini-25-computer-use-model-revolutionary-breakthrough-in-ai-agent-133)。
3.  **安全与保障的重要性**：随着 AI 直接操作电脑，对误操作引发的事故或安全威胁的担忧也会增加。相应地，更强大的安全指南和拦截机制也将同步发展 [PDFGemini Computer Use External Model Card (October 7, 2025) - updated2](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-2-5-Computer-Use-Model-Card.pdf)。

谷歌透明地公开了该模型的局限性和安全机制，强调了在追求技术发展的同时进行负责任的开发 [PDFGemini Computer Use External Model Card (October 7, 2025) - updated2](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-2-5-Computer-Use-Model-Card.pdf)。

## AI 的观点 (AI's Take)

如果说过去的 AI 专注于理解人类的“语言”，那么现在它已经开始学习如何使用人类几十年来创造的“数字工具”。Gemini 2.5 Computer Use 将成为打破人机巨大隔阂的重要桥梁。不久之后，我们将不再需要亲自动手握鼠标，而是习惯于像嘱咐同事一样向 AI 指示方向，这将开启一种全新的“计算”形式。技术即工具，工具即执行的时代已近在咫尺。

## 参考资料

1. [IntroducingtheGemini2.5ComputerUsemodel](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-computer-use-model/)
2. [Google News - News aboutGemini- Overview](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lDM3NUYkR4SHN2TllKS192ekVpZ0FQAQ?hl=en-NA&gl=NA&ceid=NA:en)
3. [Gemini2.5ComputerUseAGENT: THE BEST AGENTIC... - YouTube](https://www.youtube.com/watch?v=Xllcw7YUjJA)
4. [IntroducingGemini2.5ComputerUse: AI for web and... | LinkedIn](https://www.linkedin.com/posts/googleaidevs_introducing-gemini-25-computer-use-available-activity-7381415403840864256-ycSe)
5. [GeminiComputerUse: Google's FREE Browser... - Analytics Vidhya](https://www.analyticsvidhya.com/blog/2025/10/gemini-2-5-computer-use/)
6. [Gemini2.5ComputerUseModel: How It Automates Browsers](https://skywork.ai/blog/gemini-2-5-computer-use-model/)
7. [Gemini 2.5 Computer Use 완벽 분석 및 실전 코드](https://fornewchallenge.tistory.com/entry/Gemini-25-Computer-Use-완벽-분석-및-실전-코드)
8. [Computer Use | Gemini API | Google AI for Developers](https://ai.google.dev/gemini-api/docs/computer-use)
9. [2025 Complete Guide: Gemini 2.5 Computer Use Model - Revolutionary ...](https://dev.to/czmilo/2025-complete-guide-gemini-25-computer-use-model-revolutionary-breakthrough-in-ai-agent-133)
10. [PDFGemini Computer Use External Model Card (October 7, 2025) - updated2](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-2-5-Computer-Use-Model-Card.pdf)
11. [2025 完全 가이드: Gemini 2.5 Computer Use 모델 - AI Agent 인터페이스 제어의 혁명적 돌파구](https://velog.io/@czmilo/2025-완전-가이드-Gemini-2.5-Computer-Use-모델-AI-Agent-인터페이스-제어의-혁명적-돌파구)
12. [2025 Complete Guide: Gemini 2.5 Computer Use Model - Revolutionary ...](https://curateclick.com/blog/gemini-25-computer-use)
13. [Google LaunchesGemini2.5for AI That Clicks and Scrolls](https://geekflare.com/news/ai-that-clicks-and-scrolls-google-introduces-gemini-2-5-computer-use-model/)
14. [Google LaunchesGemini2.5ComputerUseModelfor Browser...](https://www.allaboutai.com/ai-news/google-launches-gemini-2-5-computer-use-model-for-browser-automation/)
15. [Google releases a preview of itsGemini2.5ComputerUseAImodel...](https://gigazine.net/gsc_news/en/20251008-google-gemini-2-5-computer-use)
16. [Google UnveilsGemini2.5ComputerUseThat Clicks... | Beebom](https://beebom.com/google-unveils-gemini-2-5-computer-use-that-clicks-types-scrolls-like-humans/)
17. [Google launchesGemini2.5ComputerUseto rival... | The Tech Buzz](https://www.techbuzz.ai/articles/google-launches-gemini-2-5-computer-use-to-rival-openai-agents)

## FACT-CHECK SUMMARY
- Claims checked: 14
- Claims verified: 14
- Verdict: PASS