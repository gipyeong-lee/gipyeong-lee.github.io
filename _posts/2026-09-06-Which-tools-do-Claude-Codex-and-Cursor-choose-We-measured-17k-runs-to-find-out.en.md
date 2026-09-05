---
layout: post
title: "Who Do AI Coding Tools Choose? Surprising Results Revealed by 17,000 Experiments"
description: "We explore how AI agents like Claude Code, Cursor, and Codex choose third-party tools, based on 17,000 test runs."
summary: "It has been confirmed that AI coding agents only agree on tool selection 42% of the time, revealing distinct tool preferences among different agents."
tags: [AI, Coding, Claude, Cursor, Codex]
image: 2026-09-06-Which-tools-do-Claude-Codex-and-Cursor-choose-We-measured-17k-runs-to-find-out.jpg
image_alt: "An image conceptualizing the tool selection process of AI agents, featuring complex interconnected links of different colors."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "The way an agent selects a tool is a reflection of its development philosophy, not just a simple preference. Developers should be aware that the output can vary depending on the tools the agent uses."
quiz:
  - question: "According to the study, to what extent did the three AI agents select the same tool?"
    choices: ["10%", "42%", "85%"]
    answer: 1
    explanation: "As a result of the 17,000 experiments conducted by the research team, the three agents selected the same tool only 42% of the time."
  - question: "Which tool did Cursor prefer most for voice agent tasks?"
    choices: ["Twilio", "OpenAI Realtime API", "Vapi"]
    answer: 2
    explanation: "The study showed that Claude Code preferred Twilio, Codex preferred the OpenAI Realtime API, and Cursor preferred Vapi."
  - question: "Approximately how many coding sessions were analyzed in this study?"
    choices: ["About 5,000", "About 17,000", "About 50,000"]
    answer: 1
    explanation: "The research team conducted between 16,893 and 17,000 experiments to understand the agents' tool selection process."
lang: en
ref: 2026-09-06-Which-tools-do-Claude-Codex-and-Cursor-choose-We-measured-17k-runs-to-find-out
audio: 2026-09-06-Which-tools-do-Claude-Codex-and-Cursor-choose-We-measured-17k-runs-to-find-out.en.mp3
industry: creative
---

Imagine this: You give the same ingredients to three professional chefs and ask them to cook a wonderful dish. However, before they even start cooking, they pull out different tools and deliberate for a long time. One picks up a knife, another scissors, and the third a dedicated cutter, each insisting on a different approach. The appearance and taste of the dish would certainly vary depending on the tool used.

A similar, intriguing phenomenon has recently been discovered in the field of AI coding. A study analyzed how AI coding agents—which we use frequently—such as Claude Code, Cursor, and Codex, actually choose external tools when performing tasks. [Source: Armature](https://armature.tech/blog/which-tools-coding-agents-install)

### Why is this important?

For those who use AI in their daily lives, this is not just a technical matter. When we tell an AI to "do some coding," the tool it chooses can change the project's results, stability, and even data security. [Source: o16g](https://o16g.com/updates/2026-09-04-0601/)

In other words, the "implement" an AI agent uses while writing your code has a significant impact on your digital workspace. Understanding their tool selection process is like hiring a reliable partner. Knowing which tools a partner prefers allows you to choose the optimal AI agent for your specific goals.

### Simply put: Choosing the AI's "Toolbox"

Let's use this analogy: You have a giant "toolbox" in your room containing countless tools. When AI agents receive a coding assignment, they pick the tools they need from this box.

This study thoroughly analyzed approximately 17,000 coding sessions. [Source: Armature](https://armature.tech/blog/which-tools-coding-agents-install), [Source: CCTest](https://cctest.ai/en/articles/how-claude-choose-tools-evidence-from-17-000-runs) It was like installing CCTV and observing the three chefs (agents) 17,000 times to see which tools they reached for in front of the toolbox.

The results were surprising. The three agents chose the same tool only 42% of the time. [Source: CCTest](https://cctest.ai/en/articles/how-claude-choose-tools-evidence-from-17-000-runs) They only agreed less than half the time. For example, in tasks requiring voice-related features, Claude Code preferred Twilio, Codex preferred OpenAI's Realtime API, and Cursor preferred Vapi. [Source: Armature](https://armature.tech/blog/which-tools-coding-agents-install)

In short, even when ordering the same dish (coding task), each chef (agent) prefers a different cooking tool. This phenomenon occurs because each agent has a different design philosophy or background of training. Agents, like humans, have their own tastes and working habits.

### Current Status: Personalities of AI Coding Agents

Currently, agents with distinct personalities coexist in the market.

* **Claude Code**: Capable of reading a very wide context and allows for fine-grained settings such as sub-agents or custom hooks (devices that add functionality at specific points during code execution). [Source: The AI Engineer](https://theaiengineer.substack.com/p/claude-code-vs-codex-cli-vs-cursor)
* **Cursor**: Has strengths in processing tasks by splitting them into multiple isolated worktrees. [Source: The AI Engineer](https://theaiengineer.substack.com/p/claude-code-vs-codex-cli-vs-cursor)
* **Codex**: Runs in a sandbox environment enforced by the operating system, providing a variety of integrated environments such as IDE extensions, web apps, and Slack integrations. [Source: The AI Engineer](https://theaiengineer.substack.com/p/claude-code-vs-codex-cli-vs-cursor), [Source: Builder.io](https://www.builder.io/blog/codex-vs-claude-code)

Since each tool has a different origin and area of focus, users should choose an agent that fits their coding style. [Source: The Code Media](https://thecode.media/claude-code-cursor-codex-ai-agenty/)

### What's next?

The tool selection of AI agents will become even more intelligent. Beyond simply sticking to preferred tools, their "decision-making power" to judge for themselves which tool is safest and most efficient for a specific task is expected to become more sophisticated. [Source: o16g](https://o16g.com/updates/2026-09-04-0601/) It will become important for us, the users, to transparently understand which tools agents are choosing and to have the control to adjust them if necessary.

### MindTickleBytes AI Reporter's View

The way AI chooses tools is very similar to human habits. However, it involves much more complex considerations than when we choose tools. The personalities of the agents, revealed by 17,000 experiments, suggest that in the future, AI will evolve from a mere "general-purpose machine" into an "expert with their own philosophy." What tool is your coding partner reaching for right now?

## References
1. [Which tools do Claude Code, Codex and Cursor choose? We measured 16,893 sessions to find out. · Armature](https://armature.tech/blog/which-tools-coding-agents-install)
2. [How Claude, Codex and Cursor Choose Coding Tools - CCTest](https://cctest.ai/en/articles/how-claude-choose-tools-evidence-from-17-000-runs)
3. [Agents, Memory, and Safer Tooling: Practical Updates for Outcome Engineers · o16g](https://o16g.com/updates/2026-09-04-0601/)
4. [Claude Code vs Codex CLI vs Cursor: which one to choose?](https://theaiengineer.substack.com/p/claude-code-vs-codex-cli-vs-cursor)
5. [Codex vs Claude Code: which is the better AI coding agent?](https://www.builder.io/blog/codex-vs-claude-code)
6. [ClaudeCode, Cursor, and Codex: Which AI agent to choose? - The Code Media](https://thecode.media/claude-code-cursor-codex-ai-agenty/)