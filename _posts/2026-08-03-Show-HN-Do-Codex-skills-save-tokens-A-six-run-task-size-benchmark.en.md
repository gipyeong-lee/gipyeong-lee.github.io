---
layout: post
title: "Does Teaching AI 'How to Work' Save Tokens? Interesting Experimental Results"
description: "An experimental analysis on the impact of 'Codex Skills'—teaching specific techniques to AI assistants—on token usage and efficiency."
summary: "We present experimental results showing that providing AI assistants with 'Codex Skills,' which are modular instruction bundles, can enhance work efficiency and improve consistency."
tags: [AI, Codex, TokenSavings, TechnicalExperiment, MindTickleBytes]
image: 2026-08-03-Show-HN-Do-Codex-skills-save-tokens-A-six-run-task-size-benchmark.jpg
image_alt: "An image conceptualizing an AI assistant handling complex coding tasks while optimizing token efficiency."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "The work efficiency of AI goes beyond simple model performance; it depends on how sophisticated a 'structure of instructions' is provided. Codex Skills are a key medium for transferring human working methods to AI."
quiz:
  - question: "What file format are Codex Skills stored in?"
    choices: ["CODE.txt", "SKILL.md", "INSTRUCT.json"]
    answer: 1
    explanation: "Codex Skills are managed through SKILL.md files that include metadata and instructions."
  - question: "What tool is used to easily install Codex Skills into a project?"
    choices: ["skills CLI", "npm install", "git clone"]
    answer: 0
    explanation: "You can easily install and manage skills from the project root using the skills CLI."
  - question: "What is the main purpose of the 'Codex Skills' introduced in this article?"
    choices: ["Improving AI memory", "Improving work efficiency and consistency", "Increasing model training speed"]
    answer: 1
    explanation: "Codex Skills aim to improve efficiency and consistency by guiding AI to execute specific tasks in the desired manner."
lang: en
ref: 2026-08-03-Show-HN-Do-Codex-skills-save-tokens-A-six-run-task-size-benchmark
audio: 2026-08-03-Show-HN-Do-Codex-skills-save-tokens-A-six-run-task-size-benchmark.en.mp3
industry: creative
---

Imagine having to hand a 100-page manual of all company rules and procedures to a new intern every time you gave them a task. It would be highly inefficient. A similar problem occurs when using an AI assistant like 'OpenAI Codex' (an AI model that assists with coding). If you provide detailed guides to the AI every time you assign a task, you end up consuming 'tokens' (the minimum units of text the AI processes) before the AI even begins the actual work.

Recently, a method of teaching 'Skills' to AI has gained attention to solve this problem. Just how much of a difference does pre-training an AI with specific work manuals make in terms of cost and efficiency? Let's explore the answer through a recent experiment.

## Why is this important?

For companies and individuals using AI for work, 'tokens' equate to cost. High token usage not only causes operating costs to skyrocket but also limits the complexity and speed of tasks the AI can handle. As seen in situations like [Codex Resets](https://codex-resets.com/), improving token efficiency is an essential task for utilizing AI assistants stably and economically. This study demonstrates that delivering a pre-defined package of 'how to work' to an AI can lead to tangible cost savings and improved work quality.

## Understanding Easily: What is a 'Codex Skill'?

'Codex Skills' are 'modular instruction bundles' that teach an AI how to perform specific tasks. According to [relevant documentation by Composio (GitHub - composio-community/awesome-codex-skills)](https://github.com/composio-community/awesome-codex-skills), each skill is contained in its own folder, which includes a file called 'SKILL.md'. This file contains the skill's name, description, and step-by-step instructions for the AI to follow when performing the task. [Source: OpenAICodexSkills](https://agentskill.sh/for/codex)

You can compare this to a 'filter' in a photo editing app. Without a filter, a user has to manually adjust color, contrast, and brightness. However, applying a well-set 'aesthetic filter' allows you to get the desired look with a single click. Codex Skills work the same way. Instead of giving the AI instructions from scratch every time, you simply load specific skill packages like 'code generation,' 'testing,' or 'debugging' (the process of finding and fixing errors in programs), and the AI acts like an expert who already knows what to do. [Source: AgentSkillsMarketplace](https://skillsmp.com/)

## Current Status: How far can it be utilized?

The Codex Skill ecosystem is growing rapidly. More than 34,788 skills have already been developed, reaching a level where they can perform not only code generation but also testing, debugging, deployment, and even autonomous development tasks. [Source: OpenAICodexSkills](https://agentskill.sh/for/codex)

Moreover, it goes beyond simple text tasks. For instance, in UI design, it can link with a browser to render the screen directly and modify the UI to fit breakpoints (points where the layout changes according to screen size). [Source: Codex для дизайна](https://open-design.ai/ru/agents/codex-design/) These skills can be easily installed in the project root via 'skills CLI' (a command-line interface tool), and once installed, the AI references those guides across multiple sessions. [Source: SkillsforCodex](https://www.skills.sh/agent/codex)

## What lies ahead?

Recently, experiments have been conducted to compare how much 'Lean skills' save tokens compared to existing methods in environments with different task sizes. [Source: DoCodexskillssavetokens?](https://community.openai.com/t/do-codex-skills-save-tokens-six-controlled-gpt-5-6-sol-runs/1388837) The future will see the era of upgrading AI assistants to the level of 'personal secretaries' by combining optimal skills tailored to specific tasks from tens of thousands of available ones. Practical use cases like animation production, website construction, and app automation are already appearing one after another. [Source: Top 10 Codex Skills in 2026](https://composio.dev/content/top-codex-skills)

## MindTickleBytes AI Reporter's Perspective

Providing sophisticated instructions to AI as 'Skills' is the process of evolving AI from a simple tool into a true partner. The more clearly we teach rules to AI, the more value it will create with fewer resources. The 'era of skills,' where we move beyond simply assigning tasks to teaching AI to work like an expert, is now unfolding.

## References

1. [DoCodexskillssavetokens?](https://community.openai.com/t/do-codex-skills-save-tokens-six-controlled-gpt-5-6-sol-runs/1388837)
2. [Codex Resets](https://codex-resets.com/)
3. [OpenAICodexSkills](https://agentskill.sh/for/codex)
4. [GitHub - composio-community/awesome-codex-skills](https://github.com/composio-community/awesome-codex-skills)
5. [Top 10 Codex Skills in 2026](https://composio.dev/content/top-codex-skills)
6. [AgentSkillsMarketplace](https://skillsmp.com/)
7. [SkillsforCodex](https://www.skills.sh/agent/codex)
8. [Top 10 Design Skills for Claude Code and Codex](https://composio.dev/content/top-design-skills)
9. [Codex для дизайна](https://open-design.ai/ru/agents/codex-design/)