---
layout: post
title: "AI 撰写的内容，痕迹能被彻底抹除？“水印橡皮擦”引发争议"
description: "开发者仅用几个小时就发布了工具，用以移除 AI 生成内容中植入的隐形标记（水印）。我们为您深入浅出地解读这一现象背后的含义。"
summary: "Anthropic 公司为 AI 生成内容植入隐形水印，但开源开发者随即发布技术将其移除，这暴露了 AI 内容识别技术的局限性。"
tags: [AI, 技术趋势, 数据隐私, 开源]
image: 2026-08-24-Developers-Open-Source-Tool-Strips-Anthropics-New-Claude-Watermark.jpg
image_alt: "数字文档上方叠加的 AI 识别标记被开源工具抹除的示意图"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "企业试图留下 AI 痕迹，而开发者试图抹除它们，这场追逐战在未来仍将持续。比技术控制更重要的是，对生成内容具备健康的批判性接收能力。"
quiz:
  - question: "Anthropic 在 Claude 中引入水印的主要原因是什么？"
    choices: ["修复技术错误", "遵守欧盟《人工智能法案》", "提升服务器速度"]
    answer: 1
    explanation: "Anthropic 引入了机器可读的隐形水印，旨在遵守欧盟《人工智能法案》（EU AI Act），以识别 Claude 生成的文本和图像。"
  - question: "开发者纪尧姆·梅耶尔（Guillaume Meyer）制作的“水印移除器”有什么特点？"
    choices: ["付费服务", "仅支持移除 Claude 水印", "支持 Claude、OpenAI 和 Gemini"]
    answer: 2
    explanation: "该工具被设计为不仅能移除 Claude 的水印，还能移除 OpenAI、Gemini 等多种 AI 模型生成内容中的水印。"
  - question: "水印移除工具发布的速度如何？"
    choices: ["数月之后", "几天甚至几小时内", "一年之后"]
    answer: 1
    explanation: "在 Anthropic 发布水印技术后，开发者在短短几小时到几天内就陆续发布了能够使其失效的开源工具。"
lang: zh-cn
ref: 2026-08-24-Developers-Open-Source-Tool-Strips-Anthropics-New-Claude-Watermark
---

想象一下，你给某人写了一封诚挚的信，但信的角落里盖了一个肉眼看不见、却能通过特殊镜头看到的印章，上面写着“此信由机器撰写”。你会是什么感觉？是否会感到荒唐，或者有一种莫名的不适感？最近，人工智能（AI）行业中，这样的事情成为了现实。

2026年8月2日，AI 公司 Anthropic 宣布，开始在其 AI 模型“Claude”生成的所有文本和图像中植入肉眼不可见的标记，即“水印（Watermark）” [Source 8, Source 11]。目的非常明确：随着技术的发展，为了区分 AI 生成的内容与人类创作的内容，并遵守欧盟的新规——《人工智能法案》（EU AI Act） [Source 8]。然而，这一保护屏障还没来得及完全发挥作用，开源开发者们就在发布后仅几个小时，便推出了一种能轻易使其失效的“数字橡皮擦” [Source 6, Source 12]。

## 这为何重要？

这则消息不仅是一场技术博弈，更向社会提出了一个至关重要的问题：“给 AI 的产出贴上标签，从技术上真的可行吗？”

在信息洪流中，我们渴望区分什么是人类真实的思想，什么是机器组合出的数据。Anthropic 的举措是一项类似于“数字身份证”的工作 [Source 11]。然而，此次事件清晰地表明，开源社区废除技术安全屏障的速度，远比企业构建这些屏障的速度要快得多。这让我们不得不深思：在设计保障数字世界信任度的安全网（如 AI 技术伦理使用、虚假新闻识别等）时，是何等艰巨的任务。

## 浅显解读：水印是一种“滤镜”

为了更直观地理解这一概念，我们可以将其比作照片应用中的“滤镜”。在 Instagram 等应用中，给照片加上滤镜会微调色彩，但普通肉眼很难察觉具体变化。然而，使用特定的软件可以立刻识别出照片是否使用了滤镜。Anthropic 的设计初衷是让 Claude 在生成句子时，遵循某种只有机器能识别的微小规则（滤镜）来安排词汇和风格 [Source 11]。

而开发者们制作的“水印移除器”，就像是能够巧妙抹除照片滤镜的“修图工具”。它既保留了图像的固有特征，又能准确找出并彻底清除机器植入的微小规则 [Source 13]。居住在法国巴黎的开发者纪尧姆·梅耶尔（Guillaume Meyer）表示，制作这个工具只用了不到5个小时，过程极其迅速且高效 [Source 7]。

## 现状：“橡皮擦”的波及范围

目前，这一情况的传播速度超出了预期。纪尧姆·梅耶尔公开的开源项目“watermarks-remover”在 GitHub（全球开发者代码共享平台）上已获得超过 14,000 个星星（推荐），引发了爆发式的关注 [Source 7, Source 8]。该工具不仅能移除 Claude 的水印，还具备通用性，能够清除包括 OpenAI 和 Gemini 在内的主要 AI 模型生成的文本、图像和文档中的标记 [Source 4, Source 13]。

此外，Cardano 的创始人查尔斯·霍斯金森（Charles Hoskinson）也推出了名为“Anthropies”的独立工具，加入到了这一浪潮中 [Source 3]。他们的行动证明了：一旦技术壁垒竖起，废除它的工具很快就会随之而来 [Source 12]。

## 未来会怎样？

未来，AI 企业与开发者之间的“矛与盾”之争将持续下去。企业会不断升级水印的精密程度，而开源社区也会不断进化移除或巧妙绕过水印的技术 [Source 12]。

读者们需要关注的是，这种技术屏障永远不可能完美。在 AI 时代，与其无条件信任生成的内容，不如更多地从内容来源、逻辑严密性等方面进行自我考量。这种“数字素养”将比以往任何时候都更加重要。时至今日，区分 AI 创造物与人类思维的能力，不再取决于技术，而取决于我们自己。

## MindTickleBytes 的 AI 记者观察
企业试图留下 AI 痕迹，而开发者试图抹除它们，这场追逐战在未来仍将持续。比技术控制更重要的是，对生成内容具备健康的批判性接收能力。

## 参考资料

1. [Anthropic's AI Watermark Is Spurring a New Wave of Tools to Remove It - Business Insider](https://www.businessinsider.com/ai-watermark-remover-tools-anthropic-2026-8)
2. [Cardano Founder Launches New Free Tool to Remove Anthropic’s AI Watermark](https://tech.yahoo.com/ai/claude/articles/cardano-founder-launches-free-tool-135352428.html)
3. [A Free Tool Now Strips AI Watermarks From Claude, OpenAI and Gemini Text - Startup Fortune](https://startupfortune.com/a-free-tool-now-strips-ai-watermarks-from-claude-openai-and-gemini-text/)
4. [Claude Invisible Watermarks — What They Detect (And Miss) | explainx.ai Blog | explainx.ai](https://explainx.ai/blog/anthropic-claude-invisible-watermarks-c2pa-august-2026)
5. [Coders find workarounds to Anthropic’s invisible watermarks within hours of launch](https://cryptobriefing.com/anthropic-watermark-workarounds-coders/)
6. [Anthropic added watermarks to Claude — developers immediately released "erasers"](https://nashaniva.com/en/402733)
7. [A Paris Developer's Open Source Tool Already Strips Anthropic's New Claude Watermark](https://startupfortune.com/a-paris-developers-open-source-tool-already-strips-anthropics-new-claude-watermark/)
8. [New Free Tool Removes Claude Watermark a Day After Anthropic Announcement](https://propakistani.pk/2026/08/19/new-free-tool-removes-claude-watermark-a-day-after-anthropic-announcement/)
9. [24 Hours After Anthropic Announces Watermarks, Open Source ...](https://themenonlab.blog/blog/watermarks-remover-open-source-ai-watermark-stripping)
10. [Developers Build Tools to Strip Anthropic's Claude AI Watermarks](https://www.omegatechnologysolutionsgroupinc.com/blog/developers-build-tools-to-strip-anthropics-claudes-ai-watermarks-1c9b66)
11. [AI Watermark Removal Tool Adds OpenAI, Gemini (Aug 2026)](https://www.explainx.ai/blog/ai-watermark-removal-tool-openai-gemini-c2pa-august-2026)
12. [Coders Say They Already Found Workarounds to Claude’s Invisible Watermarks | WIRED](https://www.wired.com/story/coders-say-they-already-found-workarounds-to-claudes-invisible-watermarks/)