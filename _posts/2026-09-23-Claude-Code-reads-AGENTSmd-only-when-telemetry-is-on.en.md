---
layout: post
title: "Claude Code's New AGENTS.md Support: Why Is It Not Working in My Project?"
description: "Have you set up an AGENTS.md file in the latest Claude Code, but the AI is ignoring it? Learn the reasons why and how to solve it."
summary: "While Claude Code version 2.1.277 and later supports AGENTS.md, be aware that this feature may not function in certain environments or configurations."
tags: [ClaudeCode, AI, DevTools, AGENTS.md]
image: 2026-09-23-Claude-Code-reads-AGENTSmd-only-when-telemetry-is-on.jpg
image_alt: "A modern technical graphic featuring the Claude Code logo paired with document file icons."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Introducing new standards always brings initial confusion. For now, sticking with CLAUDE.md is the most reliable approach."
quiz:
  - question: "If both CLAUDE.md and AGENTS.md exist in Claude Code, which file is prioritized?"
    choices: ["AGENTS.md", "CLAUDE.md", "Unknown"]
    answer: 1
    explanation: "If both files are present, Claude Code reads the legacy CLAUDE.md first and ignores AGENTS.md."
  - question: "In which environment is AGENTS.md support not yet officially available?"
    choices: ["Terminal", "Desktop App", "Amazon Bedrock"]
    answer: 2
    explanation: "Environments such as Amazon Bedrock, Vertex, and Foundry do not yet support the AGENTS.md feature."
  - question: "What is the recommended solution in environments where AGENTS.md cannot be used?"
    choices: ["Rename the file", "Import the content into CLAUDE.md", "Force the feature on"]
    answer: 1
    explanation: "If direct AGENTS.md support is unavailable, including the file's content directly within CLAUDE.md is the safest method."
lang: en
ref: 2026-09-23-Claude-Code-reads-AGENTSmd-only-when-telemetry-is-on
audio: 2026-09-23-Claude-Code-reads-AGENTSmd-only-when-telemetry-is-on.en.mp3
industry: education
---

Imagine this: every morning, you write a separate instruction file to guide your AI coding tool through your project's rules. But what if the AI is completely ignoring the file you worked so hard on? Many developers are currently encountering this frustrating situation. It is happening because a new method introduced after a recent update is not working as smoothly as expected.

## Why Does This Matter?

Claude Code is a powerful "agentic coding tool" that reads developers' codebases, modifies files, and even executes commands directly ([Overview - Claude Code Docs](https://code.claude.com/docs/en/overview)). Until now, developers primarily used a file named `CLAUDE.md` to inform the AI of project coding rules or specific precautions.

Recently, however, there was an announcement that a new format called `AGENTS.md` would be accepted as a standard, leading many teams to have high expectations ([Claude Code Adds AGENTS.md Fallback, Cutting Instruction File Sprawl](https://dev.blog/claude-code-adds-agents-md-fallback-cutting-instruction-file-sprawl/)). The goal of this change is to unify rule configurations across various AI tools. If this feature does not function correctly, the rules developers carefully drafted may not be communicated to the AI, risking the generation of incorrect code.

## Easy to Understand

This situation is easy to understand if you compare it to a student learning a new language:

*   **Legacy Method (CLAUDE.md)**: The existing textbook that the AI has become familiar with through previous study.
*   **New Method (AGENTS.md)**: A newly introduced standard reference book designed for more systematic AI learning.

However, for the AI to read this reference book, a specific "learning mode" must be enabled. Unfortunately, in many current usage environments, this mode is turned off by default, or the AI lacks the authorization to read the reference book altogether ([Claude Code's AGENTS.md Support: A Local Feature Locked Behind a Remote Switch](https://github.com/anthropics/claude-code/issues/95690)). It is as if the AI is unaware of the reference book's existence or does not perceive the need to read it. Notably, if telemetry is disabled or when using enterprise services like Amazon Bedrock, the AI fails to read these new rule files entirely ([Claude Code reads AGENTS.md only when telemetry is on](https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/)).

## Where Are the Problems Occurring?

Starting with the recent update, Claude Code version 2.1.277, support for `AGENTS.md` was added ([Claude Code changelog - Claude Code Docs](https://code.claude.com/docs/en/changelog)). However, for stable use, you must verify the following limitations:

1.  **Priority of Existing Files**: If both `CLAUDE.md` and `AGENTS.md` exist in the project folder, the AI will default to its habit of reading only the existing `CLAUDE.md` while completely ignoring the new `AGENTS.md` ([Claude Code Adds AGENTS.md Fallback, Cutting Instruction File Sprawl – rssfeedtelegrambot.bnaya.co.il](https://rssfeedtelegrambot.bnaya.co.il/index.php/2026/09/21/claude-code-adds-agents-md-fallback-cutting-instruction-file-sprawl/)).
2.  **Environmental Constraints**: Environments such as Amazon Bedrock, Vertex, and Foundry do not yet officially support this feature ([Claude Code changelog - Claude Code Docs](https://code.claude.com/docs/en/changelog)).
3.  **Internal Connection Method**: This feature is not integrated into the AI's core logic but is implemented as a type of internally linked "plugin" ([Claude Code Mods and agents.md: What's New and Why It Matters | MindStudio](https://www.mindstudio.ai/blog/claude-code-mods-agents-md)). Consequently, if certain conditions are not met, a "silent failure" easily occurs where the tool cannot even recognize the file.

## What's Next?

For now, environmental constraints are too significant to rely solely on `AGENTS.md` for managing your rules. If you wish to share rules in an environment where it is not directly supported, the safest and most reliable method is to include the content directly within your existing `CLAUDE.md` file ([Claude Code 2.1.277 reads AGENTS.md directly — resolution table, new silent-failure modes](https://github.com/fmslutions/harness-audit/issues/3)). Teams planning to adopt `AGENTS.md` as a standard within enterprise environments should proceed with caution for the time being ([Claude Code now also accepts instructions in OpenAI’s Agents.md format | InfoWorld](https://www.infoworld.com/article/4224410/claude-code-now-also-accepts-instructions-in-openais-agents-md-format.html)). It is recommended to maintain the legacy method until support expands to more environments through future updates.

## MindTickleBytes AI Reporter's View
The introduction of a new standard is a commendable attempt to simplify the complex file management faced by developers. However, this case illustrates how a "smart AI" can become "blind" depending on technical gaps or configuration settings. Rather than rushing to adopt new technology, sticking to proven, safe methods remains the best strategy for ensuring work continuity at this moment.

## References
1. [Claude Code reads AGENTS.md only when telemetry is on](https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/)
2. [Claude Code reads AGENTS.md only when telemetry is on - Hacker News](https://news.ycombinator.com/item?id=49814947)
3. [Set custom instructions for opencode.](https://opencode.ai/docs/rules/)
4. [Overview - Claude Code Docs](https://code.claude.com/docs/en/overview)
5. [How I use Claude Code (+ my best tips)](https://www.builder.io/blog/claude-code)
6. [Releases · anthropics/claude-code · GitHub](https://github.com/anthropics/claude-code/releases)
7. [AGENTS.md Just Turned One. The Evidence on... - Kernel Talks](https://kerneltalks.com/ai/agents-md-just-turned-one-the-evidence-on-whether-it-works-is-mixed/)
8. [claude-code/mods/agents-md/README.md at main · anthropics/claude-code](https://github.com/anthropics/claude-code/blob/main/mods/agents-md/README.md)
9. [1.2: Claude Code 2.1.277 reads AGENTS.md directly — resolution table, new silent-failure modes · Issue #3 · fmslutions/harness-audit](https://github.com/fmslutions/harness-audit/issues/3)
10. [[MODEL] Claude Code's AGENTS.md Support: A Local Feature Locked Behind a Remote Switch · Issue #95690 · anthropics/claude-code](https://github.com/anthropics/claude-code/issues/95690)
11. [Claude Code Mods and agents.md: What's New and Why It Matters | MindStudio](https://www.mindstudio.ai/blog/claude-code-mods-agents-md)
12. [claude-code/mods/agents-md at main · anthropics/claude-code](https://github.com/anthropics/claude-code/tree/main/mods/agents-md)
13. [Claude Code Adds AGENTS.md Fallback, Cutting Instruction File Sprawl – rssfeedtelegrambot.bnaya.co.il](https://rssfeedtelegrambot.bnaya.co.il/index.php/2026/09/21/claude-code-adds-agents-md-fallback-cutting-instruction-file-sprawl/)
14. [[incorrect-doctrine] "Claude Code reads CLAUDE.md, not AGENTS.md" is no longer true, and our setup command can silently switch a project's AGENTS.md off · Issue #1087 · fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills/issues/1087)
15. [Claude Code changelog - Claude Code Docs](https://code.claude.com/docs/en/changelog)
16. [Claude Code now also accepts instructions in OpenAI’s Agents.md format | InfoWorld](https://www.infoworld.com/article/4224410/claude-code-now-also-accepts-instructions-in-openais-agents-md-format.html)
17. [Claude Code Changelog (September 2026)](https://www.gradually.ai/en/changelogs/claude-code/)
18. [Claude Code Adds AGENTS.md Fallback, Cutting Instruction File Sprawl - DevOps.com](https://devops.com/claude-code-adds-agents-md-fallback-cutting-instruction-file-sprawl/)