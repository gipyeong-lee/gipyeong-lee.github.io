---
layout: post
title: "AI 绘制的音乐视频？Claude Opus 5.5 用代码而非绘画完成的魔法"
description: "介绍如何使用 Claude Opus 5.5，仅凭一个提示词（Prompt）创作出 156 秒的手绘风格音乐视频。"
summary: "Claude Opus 5.5 并非视频生成模型，而是通过直接编写代码，以逐帧生成的方式创作出精致的动画音乐视频。"
tags: [AI, Claude, 音乐视频, 编程, 技术]
image: 2026-10-09-LGTM-Looks-Good-to-Me-Claude-Opus-55-Music-Video.jpg
image_alt: "Claude Opus 5.5 通过代码生成的水彩画风格动画音乐视频场景"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "在视频生成模型时代，用代码构建视频的路径在艺术控制权方面是一个非常有趣的转折点。"
quiz:
  - question: "Claude Opus 5.5 制作音乐视频的核心方式是什么？"
    choices: ["合成现有的视频数据", "直接编写代码来实现视频", "拍摄实景视频"]
    answer: 1
    explanation: "Claude Opus 5.5 不使用视频生成模型，而是通过编写 HTML、Canvas、JavaScript 等代码来逐帧绘制视频。"
  - question: "在音乐视频创作中，用来呈现手绘感觉的工具有哪些？"
    choices: ["Photoshop", "p5.js 和 p5.brush", "Blender"]
    answer: 1
    explanation: "著名的“LGTM”音乐视频是通过 p5.js 和 p5.brush 库实现的，从而营造出水彩手绘风格。"
  - question: "关于 AI 生成的视频文件，以下表述正确的是？"
    choices: ["这是一个已经完成的 MP4 文件", "通过直接运行代码实时生成视频", "只能在云服务器上播放"]
    answer: 1
    explanation: "AI 创建的不是固定的视频文件，而是一种可执行的程序形式，通过代码运行来生成视频。"
lang: zh-cn
ref: 2026-10-09-LGTM-Looks-Good-to-Me-Claude-Opus-55-Music-Video
---

想象一下：你将喜欢的歌曲和歌词交给 AI，不到两分钟，一段完整的音乐视频便新鲜出炉了。但令人惊叹的是，这并非 AI 通过学习现有的电影片段拼凑而成。它就像画家拿起画笔在画布上作画一样，AI 自己拿起了“编码”这支笔，一帧一帧地亲手绘制出来。

最近在人工智能领域引起轰动的新一代模型 **Claude Opus 5.5** 所展现的音乐视频制作能力，确实达到了独一无二的高度。它不仅是简单的绘图，更展现了制作视频的高级“智慧”。下面我们将深入了解这一案例。

### 为什么这很重要？

此前我们所见过的 AI 视频技术，主要是通过学习大量视频后模仿其风格。但 Claude Opus 5.5 走的是完全不同的道路。它并非基于“数据模型”来生成视频，而是选择通过编写用于生成视频的“程序”来实现。

这为何重要？从技术角度看，是因为“艺术控制权”回到了我们手中。传统的视频生成模型由于 AI 随机创作，难以进行精细修改；而通过代码编写，用户可以按照意图精准实现动画效果。这意味着即便是非工程师的普通人，只要向 AI 发出指令，也能完成复杂的图形创作。 [[参考资料: Claude Opus 5.5 Video Renderer Code: How It Works (2026)](https://www.explainx.ai/blog/claude-opus-5-5-western-civilization-video-2026)]

### 简而言之：AI 是如何作画的？

Claude Opus 5.5 制作音乐视频的过程，可以比作请了一位“机器人厨师”。

当我们向机器人厨师点餐说“给我做份意大利面”时，机器人不是直接去煮面，而是写出一份“制作意大利面的精准配方（代码）”，然后指令厨房自动化系统执行。Claude Opus 5.5 也是如此。当用户说“给我做一个音乐视频”时，AI 会利用 `p5.js` 或 `Three.js` 等图形库（用于计算机绘图的工具集），直接编写出指令，指挥屏幕应该绘制什么。 [[参考资料: Claude Opus 5.5 Made This Music Video From One Prompt](https://www.youtube.com/watch?v=ShfA4KRLSyM), [参考资料: GitHub - tuzhechen2005/opus-video-skills](https://github.com/tuzhechen2005/opus-video-skills)]

近期备受关注的《LGTM (Looks Good to Me)》音乐视频，将 156 秒的视频分为 9 个章节，总计 3,760 帧，全部由 JavaScript 代码逐一绘制完成。为了呈现水彩画质感，它使用了名为“p5.brush”的库。令人惊叹的是，整个过程完全由 AI 执行单一指令完成，全程无人力干预。 [[参考资料: Claude Opus 5.5 Writes Code to Paint a Hand-Drawn Music Video](https://best.xiaohu.ai/en/article/opus-5-5-clawd-animation-mv/), [参考资料: The AI Skool | AI Tools & AI News](https://www.instagram.com/reel/Dd1fNogMsbL/)]

### 当前现状：人人皆可成为创作者

目前，Claude Opus 5.5 已能实现多种风格的视频。全球用户正利用该 AI 创作并分享包括音乐视频、广告片、教学内容在内的各类作品。

社区里甚至出现了专门收集这些 AI 生成视频的“图书馆”。目前已收集了 1,276 个视频，其中 457 个还公开了用户输入的原始“提示词（Prompt）”，任何人都可以轻松尝试。简而言之，现在的环境已经让普通人不仅仅是技术的旁观者，通过 AI 每个人都有机会成为动画创作者。 [[参考资料: All 1276 Claude Opus 5.5 videos, by type](https://claudevideo.org/videos), [参考资料: GitHub - yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos)]

### 未来将如何发展？

专家评价称，这一案例的意义远超“有趣的演示”。它证明了 Claude Opus 5.5 在执行复杂、结构化任务时的逻辑性。未来，用户将超越单纯输入文本的阶段，通过与 AI 紧密协作，创作出更精细、更长篇的电影或游戏等交互式内容。 [[参考资料: Claude Opus 5.5 Video Renderer Code: How It Works (2026)](https://www.explainx.ai/blog/claude-opus-5-5-western-civilization-video-2026)]

### MindTickleBytes AI 记者视点

技术的进步正将艺术领域也迁入编程语言的领地。从 AI 不仅仅是复制已有数据，到通过代码自行构建视觉逻辑，我们正在见证 AI 与艺术之间建立起全新的关系。工具的变革将如何拓展创意的边界，未来令人充满期待。

## 参考资料

1. [LGTM (Looks Good to Me) - Claude Opus 5.5 music video](https://www.youtube.com/watch?v=3TNpOD6bov8)
2. [Claude Opus 5.5 Made This Music Video From One Prompt](https://www.youtube.com/watch?v=ShfA4KRLSyM)
3. [LGTM（我觉得没问题）- Claude Opus 5.5 音乐视频 | Degenerative Pixels](https://www.bilibili.com/video/BV1FNHC6LEsr/)
4. [GitHub - yihui-dev/awesome-opus5-5-videos: A growing collection of videos created with Claude Opus 5.5](https://github.com/yihui-dev/awesome-opus5-5-videos)
5. [GitHub - athemeroy/awesome-claude-5-5-videos: Source-linked guide to videos and animations](https://github.com/athemeroy/awesome-claude-5-5-videos)
6. [Claude Opus 5.5 Video Examples & Prompts — Claude Video](https://claudevideo.org/)
7. [All 1276 Claude Opus 5.5 videos, by type — Claude Video](https://claudevideo.org/videos)
8. [Claude Opus 5.5 Writes Code to Paint a Hand-Drawn Music Video](https://best.xiaohu.ai/en/article/opus-5-5-clawd-animation-mv/)
9. [Claude Opus 5.5: What "Plan a Video" Actually Produces](https://www.orcarouter.ai/blog/claude-opus-5-5-video-plan-one-shot)
11. [Claude Opus 5.5 Video Renderer Code: How It Works (2026)](https://www.explainx.ai/blog/claude-opus-5-5-western-civilization-video-2026)
12. [Claude Opus 5.5 Is INSANE – Hands-On With the BEST Model Yet!](https://www.youtube.com/watch?v=ux6Lafw7en0)
13. [GitHub - tuzhechen2005/opus-video-skills: Video-making skills for Claude Opus 5.5](https://github.com/tuzhechen2005/opus-video-skills)
14. [LGTM (Looks Good to Me) - Claude Opus 5.5 music video](https://m.youtube.com/watch?v=3TNpOD6bov8)
16. [The AI Skool | AI Tools & AI News - Claude Opus 5.5 just built an entire animated music video](https://www.instagram.com/reel/Dd1fNogMsbL/)