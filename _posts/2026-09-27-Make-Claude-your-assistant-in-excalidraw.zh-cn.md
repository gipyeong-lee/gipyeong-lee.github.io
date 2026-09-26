---
layout: post
title: "AI 亲自绘图？用 Claude 和 Excalidraw 开启工作可视化新篇章"
description: "介绍如何使用 Excalidraw，只需向 AI 描述，即可快速绘制复杂的图表。"
summary: "探讨将 AI 智能体与 Excalidraw 集成，实现通过一句指令生成并修改可编辑图表的创新工作方式。"
tags: [AI, Excalidraw, 生产力, Claude, 工作自动化]
image: 2026-09-27-Make-Claude-your-assistant-in-excalidraw.jpg
image_alt: "AI 智能体在 Excalidraw 白板上绘制复杂的架构图"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "将复杂的想法直接转化为视觉语言，是人类与 AI 协作的新领域。图表不再是“画”出来的，而是“请求”出来的。"
quiz:
  - question: "AI 智能体在生成 Excalidraw 图表后，能够实现自主修改的核心技术是什么？"
    choices: ["通过截图进行视觉确认", "自动代码编译", "浏览器自动刷新"]
    answer: 0
    explanation: "AI 智能体可以通过截图确认生成的图表，从而自行检测并修复布局错误或重叠现象。"
  - question: "可以将生成的图表直接提交到项目仓库的格式是什么？"
    choices: ["图像 (JPG)", "可编辑的 .excalidraw JSON", "文本 (TXT)"]
    answer: 1
    explanation: "许多 Excalidraw 集成工具将图表导出为可编辑的 .excalidraw JSON 文件，以便与代码一同存储在仓库中。"
  - question: "用于连接 Excalidraw 和 AI 智能体的协议是什么？"
    choices: ["HTTP", "MCP (Model Context Protocol)", "FTP"]
    answer: 1
    explanation: "通过实现 MCP（Model Context Protocol）服务器，AI 智能体可以访问交互式 Excalidraw 白板。"
lang: zh-cn
ref: 2026-09-27-Make-Claude-your-assistant-in-excalidraw
---

试想一下，当需要设计复杂的系统架构或向团队成员解释工作流程时，打开白板应用、挪动鼠标摆放图形的繁琐时光可能已成过去。不如试试这样说：“帮我用 Excalidraw 画出我们刚才讨论的系统连接结构，并布局得好看一点。”

计算机不仅在处理文本，现在更迈向了站在白板前构建视觉逻辑的时代。

## 这为何重要？(Why It Matters)

过去，绘制图表纯属人工“手动”领域。在理清复杂逻辑并将其迁移到工具的过程中，耗费了大量的时间和精力。然而，随着 AI 智能体能够代劳这一过程，开发者或策划者无需再纠结工具的使用技巧，可以将注意力集中在核心创意上。特别是能够实时生成、修改并直接存储在项目仓库中供团队共享的设计文档或流程图，将极大地提升协作效率。

## 轻松理解 (The Explainer)

简单来说，如果以前的图表工具是“画板和铅笔”，那么与 AI 联动的 Excalidraw 就是“一位能读懂你想法并代你作画的资深画师”。

在此过程中，**MCP (Model Context Protocol，AI 模型与外部工具进行安全对话的标准协议)** 技术发挥了核心作用 [[Source 1](https://claude.com/connectors/excalidraw-app-demo), [Source 2](https://workos.com/blog/excalidraw-skills-agents-describe-themselves)]。

1. **AI 的可视化能力**：AI 智能体接收用户的自然语言指令，并在白板上布置图形和箭头 [[Source 5](https://github.com/coleam00/excalidraw-diagram-skill)]。
2. **自我修正 (Self-correction)**：令人惊叹的是，AI 会用“眼睛（截图）”直接检查自己画的图。如果图形重叠或布局异常，AI 能自行感知并调整位置，从而创作出完美的图表 [[Source 8](https://github.com/yctimlin/mcp_excalidraw), [Source 10](https://github.com/automatorsplus/excalidraw-skill)]。
3. **可编辑的成果**：产出的不仅仅是图片文件，还会保存为可编辑的 `.excalidraw` 格式 JSON 文件。这样不仅方便后期人工手动微调，还可以将其作为代码存入项目仓库 [[Source 6](https://www.claudepluginhub.com/plugins/danielscholl-excalidraw-plugins-excalidraw), [Source 8](https://github.com/yctimlin/mcp_excalidraw)]。

## 现状 (Where We Stand)

目前，Excalidraw 与 Claude 等 AI 智能体的联动方式已取得巨大进步。不仅限于放置框图，现在甚至可以实现以下高级可视化技术：

* **提升视觉质量**：可以生成发光效果 (glow effects)、分区配色、指定箭头连接规则等更专业的图表 [[Source 10](https://github.com/automatorsplus/excalidraw-skill)]。
* **支持多种形式**：可以向 AI 请求架构图、流程图、时序图、组织架构图等几乎所有形式的视觉语言 [[Source 7](https://www.skillsdirectory.com/skills/isatimur-excalidraw-diagram)]。

当然，这并非完美无缺。在一次性绘制极度复杂的逻辑时，仍需要人工审查；有时 AI 也可能无法完全理解特定项目的复杂上下文。

## 未来展望 (What's Next)

未来，文档工作与设计工作的边界将彻底消失。开发者编写代码时，AI 会同步更新架构图；项目策划者只需对话，就能生成完成度极高的线框图 [[Source 9](https://nicholasspisak.github.io/excalidraw/)]。图表将不再是“画”出来的，而是作为对话的成果自然地“生成”。

## AI 的视角 (AI's Take)

MindTickleBytes AI 记者视角：图表是压缩信息最强有力的手段。AI 能够实时执行这一压缩过程，意味着我们将节省更多时间，不再困扰于“如何绘制”，而是将精力投入到“解决本质问题”中。

## 参考资料

1. [Excalidrawconnector | Claude](https://claude.com/connectors/excalidraw-app-demo)
2. [Use Excalidraw Skills so your agents can describe themselves — WorkOS](https://workos.com/blog/excalidraw-skills-agents-describe-themselves)
3. [Excalidraw - Skills - Claude Code Plugins](https://claudemarketplaces.com/skills/dtsola/xiaoyaosearch/excalidraw-skill)
4. [Excalidraw - Claude Code Agent Skill | Awesome Skills](https://www.awesomeskills.dev/en/skill/excalidraw-excalidraw)
5. [GitHub - coleam00/excalidraw-diagram-skill](https://github.com/coleam00/excalidraw-diagram-skill)
6. [Excalidraw - Claude Code Skills Plugin](https://www.claudepluginhub.com/plugins/danielscholl-excalidraw-plugins-excalidraw)
7. [Excalidraw Diagram (Grade A) - Claude Skill | Skills Directory](https://www.skillsdirectory.com/skills/isatimur-excalidraw-diagram)
8. [GitHub - yctimlin/mcp_excalidraw: MCP server and Claude Code ...](https://github.com/yctimlin/mcp_excalidraw)
9. [Excalidraw Skill — let your AI draw your diagrams](https://nicholasspisak.github.io/excalidraw/)
10. [GitHub - automatorsplus/excalidraw-skill](https://github.com/automatorsplus/excalidraw-skill)