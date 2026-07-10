---
layout: post
title: "边说边画？与 AI 实时协作的“智能绘图（Agent Draw）”"
description: "带你了解如何只需对 AI 说出想法，它就能在无限画布上为你实时绘图的智能绘图工具及其背后原理。"
summary: "智能绘图（Agent Draw）是一款交互式工具，允许 AI 智能体理解用户的语音指令，并在无限画布上实时进行绘图和图形布局。"
tags: [AI, 智能体, tldraw, 创造力, 工具]
image: 2026-07-09-Show-HN-Agent-Draw-An-agent-draws-while-you-talk-built-on-TLDraw.jpg
image_alt: "智能绘图界面的屏幕截图，AI 正在无限画布上实时作画。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这不仅是简单的图像生成，更是 AI 在画布空间内与用户进行物理交互迈出的第一步。"
layout: post
title: "听我说就能画出来？与AI实时协作的“智能绘图（Agent Draw）”"
description: "了解智能绘图工具，它能让你只需对AI口述，即可在无限画布上实现实时绘图，并解析其背后的原理。"
summary: "智能绘图（Agent Draw）是一款交互式工具，AI代理可以理解用户的语音指令，并在无限画布上实时进行绘图和图形布局。"
tags: [AI, 智能体, tldraw, 创造力, 工具]
image: 2026-07-09-Show-HN-Agent-Draw-An-agent-draws-while-you-talk-built-on-TLDraw.jpg
image_alt: "智能绘图界面截图，AI正在无限画布上实时作画。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这不仅仅是简单的图像生成，而是AI在画布这一空间中与用户进行物理交互的第一步。"
lang: zh-cn
ref: 2026-07-09-Show-HN-Agent-Draw-An-agent-draws-while-you-talk-built-on-TLDraw
---

想象一下，你面前放着一张白纸，说道：“在这里给我画一个美味的披萨”，然后AI就开始在你眼前画线，一点点勾勒出奶酪和意大利辣香肠。这种宛如魔法般的场景正准备走进我们的日常生活。近期发布的“智能绘图（Agent Draw）”正在彻底改变我们与AI协作的方式。

### 为什么这个工具备受关注？

以往我们要求AI绘图时，通常是输入指令，等待片刻，然后“被动接收”完成的成品。也就是说，AI更像是一个单向投递结果的存在。但智能绘图完全不同。它展示了与用户在画布上进行持续交流、实时共同绘画的“协作”过程 [出处 2](https://www.youtube.com/watch?v=iIH2hJAxxm8)。

这意味着创意工作不再是单打独斗的过程。正如在会议室白板前与同事交流想法并共同完善画作一样，人类与AI可以在同一空间中交换意见并共同作业。此时，AI不再仅仅是生成结果的“工具”，而是进化成了站在画布旁的积极“伙伴” [出处 13](https://gitnation.com/contents/agents-on-the-canvas-with-tldraw)。

### 它是如何工作的？

智能绘图的工作原理比想象中更精细。打个比方，可以将其理解为画布上存在一只“智能AI机械臂”，它成为我们手的延伸，即使我们不动手，它也能代我们画出想要的内容。

1. **无限画板（tldraw SDK）**：这是基础画布环境。使用基于React的无限画布SDK“tldraw”，为AI提供了可以自由布局图形和绘画的空间 [出处 1, 出处 15](https://tldraw.dev/blog/tldraw-mcp-app)。
2. **智能体入门套件（基础训练课程）**：这是教导AI如何绘图和处理图形的“基本功”。通过该套件，AI不仅能处理简单图像，还能识别并摆放矩形、菱形、箭头等基本图形，精细操纵画布元素 [出处 6, 出处 12](https://github.com/tldraw/tldraw/blob/main/apps/docs/content/starter-kits/agent.mdx)。
3. **交通指挥系统（状态机）**：确保用户同时发出多个请求时系统不会混乱。通过“先进先出（FIFO）”队列和状态机，系统管理AI一次专注于一个会话并顺序解决任务 [出处 8](https://techstackups.com/articles/tldraw-agent-draw/)。

通过这些过程，AI能在用户指定的画布区域内识别语音指令含义，实时绘制图形，并即时反映用户的意图 [出处 2, 出处 3](https://www.youtube.com/watch?v=livloOnVpC8)。

### 目前进展如何？

目前的智能绘图是基于开发者官方的“智能体入门套件”构建的 [出处 2, 出处 5](https://memedata.com/post/130752)。用户通过屏幕右侧的聊天面板与智能体对话。在这里，可以添加背景说明，或查看智能体的工作记录并进行沟通 [出处 6, 出处 11](https://zenn.dev/slowhand/articles/bb203aba83e385?locale=en)。

AI在处理基本图形组合或构图方面非常熟练。它不仅能绘图，还可以编写待办事项列表，或在收到修改请求后立即反映并更新，实现复合型的业务辅助 [出处 12](https://github.com/tldraw/tldraw/blob/main/apps/docs/content/starter-kits/agent.mdx)。当然，目前它更适合作为系统的图表生成或实时视觉辅助工具，而非复杂的艺术创作 [出处 9, 出处 11](https://zenn.dev/slowhand/articles/bb203aba83e385?locale=en)。

### 未来的工作方式会怎样？

智能绘图的出现，预示了我们在不久的将来与AI共同工作的模式。未来，AI代理将在画布上进行更深入的推理，甚至能够洞察用户细微的意图，从而自主修改图纸或提出创意。

我们很快就会拥有一个“真正的视觉伙伴”，它不仅是在制造静止的图像，而是能在画布这一物理空间中与我们共同思考、共同创作。届时，屏幕上的画布将不再仅仅是画板，而是人类与AI实时碰撞思想的全新协作平台。

---

### MindTickleBytes AI记者视角
迄今为止，能绘图的AI很多，但能够理解“空间”、与用户交互并逐步构建成果的AI却很少见。AI与我们的思想共同呼吸并完成某种创作的过程本身，正在改变创造性体验的本质。

## 参考资料

1. [Show HN: Agent Draw: An agent draws while you talk, built on TLDraw](https://news.ycombinator.com/item?id=48805475)
2. [Agent Draw — Speak, and an AI Agent Draws It Live on Canvas](https://www.youtube.com/watch?v=iIH2hJAxxm8)
3. [Agent Draw: drag a box, speak, an AI agent draws inside it](https://www.youtube.com/watch?v=livloOnVpC8)
4. [Agent Draw: An agent draws while you talk, built on TLDraw](https://vuink.com/post/grpufgnpxhcf-d-dpbz/articles/tldraw-agent-draw)
5. [Show HN：Agent Draw，基于 TLDraw 构建，在你说话时自动绘图。](https://memedata.com/post/130752)
6. [GitHub - tldraw/agent-template: Enable AI agents to interpret ...](https://github.com/tldraw/agent-template)
7. [Better HN - bhn.vercel.app](https://bhn.vercel.app/show)
8. [Agent Draw: An agent draws while you talk, built on TLDraw | Tech Stackups](https://techstackups.com/articles/tldraw-agent-draw/)
9. [Agent starter kit • tldraw Docs](https://tldraw.dev/starter-kits/agent)
10. [Starter kits • tldraw Docs](https://tldraw.dev/starter-kits)
11. [tldraw × AI Agent: Exploring the Mechanics with the Agent Starter Kit](https://zenn.dev/slowhand/articles/bb203aba83e385?locale=en)
12. [tldraw/apps/docs/content/starter-kits/agent.mdx at main · tldraw/tldraw](https://github.com/tldraw/tldraw/blob/main/apps/docs/content/starter-kits/agent.mdx)
13. [Agents on the Canvas With tldraw by Max Drake](https://gitnation.com/contents/agents-on-the-canvas-with-tldraw)
14. [Build a Real-Time tldraw Whiteboard with Velt Comments inside ChatGPT🤯🔥 - DEV Community](https://dev.to/astrodevil/build-a-real-time-tldraw-whiteboard-with-velt-comments-inside-chatgpt-1dhe)
15. [tldraw MCP App: Letting your agents draw](https://tldraw.dev/blog/tldraw-mcp-app)
16. [Show | Hacker News - nhn.yuu.is](https://nhn.yuu.is/show)