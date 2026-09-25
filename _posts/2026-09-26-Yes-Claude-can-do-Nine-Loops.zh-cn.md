---
layout: post
title: "让AI代劳重复工作……用“循环工程”打造专属秘书"
description: "还在为每次都要向AI输入提示词并检查结果而疲惫不堪吗？本文将为您介绍如何利用Claude Code的“循环工程”实现编码工作的自动化。"
summary: "利用Claude Code的“循环（Loop）”功能，您可以构建一个让AI自主发现任务、执行并验证结果的自治系统。"
tags: [AI, ClaudeCode, 生产力, 自动化, 循环工程]
image: 2026-09-26-Yes-Claude-can-do-Nine-Loops.jpg
image_alt: "象征数字自动化系统执行重复任务的抽象图形"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这是从人类每次下达指令的时代，向AI自主判断并执行的“智能体系统”跨越的转折点。"
quiz:
  - question: "在Claude Code中，用于设置“任务完成”标准，并使其反复运行直到满足条件的命令是？"
    choices: ["/schedule", "/goal与/loop的组合", "/routine"]
    answer: 1
    explanation: "/goal用于定义完成标准，/loop则使AI在该条件满足前持续运行。"
  - question: "实现成功的循环工程，最重要的是什么？"
    choices: ["使用更多的Token", "通过验证器(Verifier)确认结果", "每天重新编写提示词"]
    answer: 1
    explanation: "核心在于“验证器”的角色，即AI自行验证结果并设置停止条件。"
  - question: "关于Claude Code循环功能的描述，正确的是？"
    choices: ["所有功能仅由官方MCP服务器提供", "不仅包含重复性的本地执行，还包含云端例行任务", "必须由用户直接编写代码才能运行"]
    answer: 1
    explanation: "Claude Code支持多种自动化方式，包括本地循环、云端定时任务（Cron）及动态工作流等。"
lang: zh-cn
ref: 2026-09-26-Yes-Claude-can-do-Nine-Loops
---

想象一下：下班前，你对AI秘书说：“明天早上之前，把这个项目的所有Bug找出来并修复，还要确保通过所有测试。”以前，你需要不停地向AI发出指令：“检查一下这个文件”、“跑一下测试”、“现在好了吗？”，然后在那等待回答。但现在，AI自主判断并重复执行任务的时代已经到来。

最近因Claude Code而备受瞩目的**“循环工程（Loop Engineering）”**正是这一趋势的核心。

## 为什么这很重要？

到目前为止，我们使用AI编码智能体的方式就像在使用“遥控器”。每按一次按钮，才会传达一次指令。而循环工程将AI转变成了“自动驾驶系统”。

开发者无需再浪费时间手动命令AI完成重复性工作。因为你可以构建一套让AI自主发现任务、执行、验证结果并决定下一步的系统。这不仅仅是简单的自动化，它标志着我们与AI的协作方式正从“指令式”向“目标管理式”进化 [出处: Loop Engineering in Claude Code: Let the Agent Run Itself | VibeReady](https://vibeready.sh/blog/loop-engineering-claude-code/)。

## 轻松理解

“循环（Loop）”在编程中是指将特定动作重复执行直到满足某个条件。循环工程就是将这一概念应用到了AI智能体上。

简单打个比方，与其不停地给新手司机（AI）下达指令：“向左打方向30度”、“踩刹车”，不如输入具体规则：“安全到达目的地，遇到红灯就停，绿灯就走”。

Claude Code提供的关键工具正是构建这些规则的零部件：

*   **/goal**：明确定义AI的“完成”状态目标 [出处: Loop engineering: Getting started with loops | Claude by Anthropic](https://claude.com/blog/getting-started-with-loops)。
*   **/loop**：让智能体反复执行本地任务，直到达到目标 [出处: Loop engineering: Claude Code Loops, Routines & Workflows](https://blakecrosley.com/guides/loop-engineering)。
*   **验证器（Verifier）**：这是核心所在。为了防止AI“产生幻觉”，它通过人类设定的严格标准（例如：是否通过特定测试）来确认结果是否正确 [出处: Loop Engineering in Claude Code: Let the Agent Run Itself | VibeReady](https://vibeready.sh/blog/loop-engineering-claude-code/)。

通过组合目标（/goal）和循环（/loop），一个能自主执行长期任务的智能体就诞生了 [出处: How to Use the /goal and /loop Commands in Claude Code for Autonomous Long-Running Tasks | MindStudio](https://www.mindstudio.ai/blog/claude-code-goal-loop-commands-autonomous-tasks)。

## 当前现状

目前的循环工程已经不仅仅停留在代码的反复执行上。

*   **/goal**、**/loop**等基础重复命令 [出处: Claude Code Loops Guide: /goal, /loop, /schedule (2026) | explainx.ai Blog | explainx.ai](https://www.explainx.ai/blog/claude-code-loops-official-guide-turn-goal-schedule-2026)
*   云端环境下的定时“例行任务（Routines）”
*   动员多个AI智能体处理复杂工作的“动态工作流（Dynamic Workflows）”，其应用范围正在不断扩大 [出处: Loop engineering: Claude Code Loops, Routines & Workflows](https://blakecrosley.com/guides/loop-engineering)。

需要注意的是，目前的“Loops”功能并不直接支持官方MCP（Model Context Protocol，连接AI模型与外部工具的标准规范）服务器，需要通过中转服务来实现 [出处: How to Connect Loops to Claude (and What It Can't Do)](https://www.usecarly.com/blog/claude-loops-integration/)。

## 未来展望

循环工程将进一步深化。未来，AI将不仅局限于编码，在数据分析、报告编写、服务器管理等更多领域，AI将具备自主检查“自身状态”并“达成目标”的能力 [出处: Loop engineering: Claude Code Loops, Routines & Workflows](https://blakecrosley.com/guides/loop-engineering)。

用户将不再纠结于AI的“工作方式”，而是更多地专注于“要达成什么目标”。许多开发者已经摆脱了手动输入提示词的模式，转向了设计系统的循环工程 [出处: I Stopped Prompting Claude Code. Now Loops Do It For Me (Loop Engineering) - YouTube](https://www.youtube.com/watch?v=yaJAMagc_sE)。

## MindTickleBytes AI记者视角

“循环工程是AI从工具进化为‘合作伙伴’的信号。AI做每次都要指令的工作是人类该做的，而让AI自主运行才是系统该做的。”

---

## 参考资料

1. [Claude computes a nine-loop amplitude in N=4 super-Yang-Mills \ Anthropic](https://www.anthropic.com/research/yes-claude-can-do-nine-loops)
2. [Loop Engineering in Claude Code: Let the Agent Run Itself | VibeReady](https://vibeready.sh/blog/loop-engineering-claude-code/)
3. [Claude Code Loops Guide: /goal, /loop, /schedule (2026) | explainx.ai Blog | explainx.ai](https://www.explainx.ai/blog/claude-code-loops-official-guide-turn-goal-schedule-2026)
4. [How to Use the /goal and /loop Commands in Claude Code for Autonomous Long-Running Tasks | MindStudio](https://www.mindstudio.ai/blog/claude-code-goal-loop-commands-autonomous-tasks)
5. [How to Connect Loops to Claude (and What It Can't Do)](https://www.usecarly.com/blog/claude-loops-integration/)
6. [I Stopped Prompting Claude Code. Now Loops Do It For Me (Loop Engineering) - YouTube](https://www.youtube.com/watch?v=yaJAMagc_sE)
7. [Loop engineering: Claude Code Loops, Routines & Workflows](https://blakecrosley.com/guides/loop-engineering)
8. [Loop engineering: Getting started with loops | Claude by Anthropic](https://claude.com/blog/getting-started-with-loops)