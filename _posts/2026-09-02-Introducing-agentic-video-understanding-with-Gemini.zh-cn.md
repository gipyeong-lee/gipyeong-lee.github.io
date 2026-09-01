---
layout: post
title: "AI 不再只是“看”视频，开始“调查”了？代理型视频理解技术登场"
description: "为您简要介绍谷歌 Gemini 引入的全新代理型视频理解技术，以及它如何改变 AI 的视频分析方式。"
summary: "谷歌在 Gemini 模型中引入的“代理型视频理解”技术，使 AI 不再局限于简单的观看，而是能够主动地进行调查与分析。"
tags: [AI, Gemini, 视频分析, 谷歌]
image: 2026-09-02-Introducing-agentic-video-understanding-with-Gemini.jpg
image_alt: "展示 Gemini 主动分析和调查视频中信息的数字图形"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 仅凭观看静态图像或视频就能给出答案的时代已经过去。现在，AI 正在演变成一名能够自主规划、提问并验证信息的积极调查员。"
quiz:
  - question: "此次发布的代理型视频理解技术可以在哪些模型上使用？"
    choices: ["Gemini 3.7 Flash, 3.6 Flash, 3.5 Flash-Lite", "所有 Gemini 模型", "Gemini 1.0 专用"]
    answer: 0
    explanation: "谷歌宣布该功能通过 Gemini 3.7 Flash, 3.6 Flash 及 3.5 Flash-Lite 模型提供支持。"
  - question: "代理型视频理解与传统方式相比，最大的特点是什么？"
    choices: ["主动且反复的调查，而非单纯观看", "更快速压缩视频的技术", "自动修改视频的功能"]
    answer: 0
    explanation: "它摆脱了静态观察，让 AI 通过主动且反复的调查过程来获取信息。"
  - question: "通过什么途径可以访问该技术？"
    choices: ["Google AI Studio 及 Gemini 企业代理平台", "通过邮件申请", "在 YouTube 评论区"]
    answer: 0
    explanation: "目前可通过 Google AI Studio 和 Gemini 企业代理平台的 API 使用。"
lang: zh-cn
ref: 2026-09-02-Introducing-agentic-video-understanding-with-Gemini
---

想象一下，你正试图在长达几十小时的监控录像中寻找特定事件发生的瞬间。以往，你只能将视频丢给 AI 并问“这是什么？”，然后依赖它给出不完整的摘要。但现在，一个 AI 能够像老练的调查员一样，仔细检查视频，必要时反复回放，并自主得出结论的时代已经到来。这就是谷歌近期发布的“代理型视频理解（Agentic video understanding）”技术所带来的变革。

## 为什么这很重要？

此前，让 AI 分析视频就像给学生发试卷并问“答案是什么？”一样。传统的 AI 通常只会匆匆扫视整体内容，依靠直觉给出回答。但被冠以“代理型”称号的这项技术则完全不同。

该技术将曾是“观察者”的 AI 转变为了积极的“调查员”。它不仅限于概括视频内容，AI 还能自主判断，深入研究特定画面，对比前后文脉络，进行逻辑分析。对于处理复杂数据的企业或需要精密分析的专业人士而言，这将提供前所未有的准确度和洞察力。[出处: Introducing agentic video understanding with Gemini](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/)

## 轻松理解

若要形象地比喻“代理型视频理解”，这就像是 **“在图书馆寻找书籍方式的差异”**。

如果说传统的 AI 仅凭书名揣测内容，那么这项技术就像是 **聘请了一位能干的图书馆员**。当你请求“帮我在视频里找到发生事故的片段”时，名为 AI 的图书管理员会直接进入图书馆（视频文件），翻找书架，亲自查阅内容，必要时还会取出多本书籍进行对比，然后温和地告诉你：“这是 34 号书架 2 层资料里的确切证据”。

在相同的背景下，谷歌此前曾引入“代理型视觉（Agentic Vision，指 AI 自主掌握并调查图像或视频内容的技术）”，将主动调查循环应用到了静态图像理解过程中。[出处: Introducing Agentic Vision in Gemini 3 Flash](https://blog.google/innovation-and-ai/technology/developers-tools/agentic-vision-gemini-3-flash/) 该方式将 AI 推导出信息的过程构筑为三步循环（规划-执行-验证），确保最终答案不是简单的推测，而是基于经过验证的视觉证据。[出处: Google Introduces Agentic Vision: Gemini 3 Flash Now...](https://labnotes.tech/blog/google-introduces-agentic-vision-gemini-3-flash-now-zooms-annotates-and-investigates-images) 此次视频分析技术也可以理解为将这种主动调查原理应用于视频这一动态数据。

## 当前状况

目前，开发者可以通过 Google AI Studio 和 Gemini 企业代理平台（Gemini Enterprise Agent Platform）的 API 使用这一强大的代理型视频理解功能。[出处: Introducing agentic video understanding with Gemini](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/)

谷歌正在将其逐步应用于 Gemini 的最新模型阵容：**Gemini 3.7 Flash、3.6 Flash 和 3.5 Flash-Lite**。[出处: Introducing agentic video understanding with Gemini](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/) 这意味着，现在只需传入视频，AI 就能够利用内部工具进行更复杂、更深入的分析。[出处: Video understanding | Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding)

## 未来发展

未来，AI 将不仅限于指出视频中“有什么”，还将更深入地回答诸如“那个人为什么做出那种行为”、“视频中复杂机械的运作原理是什么”等问题。

当用户能够像对话一样自然地指示视频剪辑或分析时，AI 将能够把握流程并逐步处理，这种“对话式 AI 视频编辑器”体验有望更加普及。[出处: GeminiOmni – Create & edit videos as easy as having a conversation](https://gemini.google/us/overview/video-generation/?hl=en) 随着技术的进步，我们日常生活中的视频内容消费方式也将发生巨大改变，从单纯的观看转变为与 AI 一起“调查并讨论”视频。

## 参考资料

1. Introducing Agentic Vision in Gemini 3 Flash (https://blog.google/innovation-and-ai/technology/developers-tools/agentic-vision-gemini-3-flash/)
2. Video understanding | Gemini Enterprise Agent Platform | Google Cloud Documentation (https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding)
3. Introducing agentic video understanding with Gemini (https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/)
4. GeminiOmni – Create & edit videos as easy as having a conversation (https://gemini.google/us/overview/video-generation/?hl=en)
5. Google Introduces Agentic Vision: Gemini 3 Flash Now... | LabNotes (https://labnotes.tech/blog/google-introduces-agentic-vision-gemini-3-flash-now-zooms-annotates-and-investigates-images)