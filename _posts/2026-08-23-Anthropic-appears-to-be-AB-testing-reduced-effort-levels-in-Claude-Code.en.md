---
layout: post
title: "Did My AI Suddenly Get Dumber? The Secret Story Behind Anthropic's Claude Code Experiment"
description: "Have you ever felt like your AI model’s performance suddenly dropped? We examine AI transparency issues through Anthropic's 'effort level' adjustments in Claude Code and the resulting user frustration."
summary: "To reduce costs and improve speed, Anthropic quietly lowered the default reasoning intensity of Claude Code, only to restore it following a barrage of user complaints regarding degraded quality."
tags: [AI, Anthropic, ClaudeCode, ArtificialIntelligence, TechEthics]
image: 2026-08-23-Anthropic-appears-to-be-AB-testing-reduced-effort-levels-in-Claude-Code.jpg
image_alt: "Claude Code interface screen and graphic elements representing the reasoning process"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "When companies optimize technology, they must transparently disclose the reasons for changes to maintain user trust. Experimental features should always prioritize ensuring user choice."
quiz:
  - question: "What was the primary reason Anthropic lowered the default reasoning level of Claude Code?"
    choices: ["To enhance model security", "To reduce costs and improve response speed", "To train on more data"]
    answer: 1
    explanation: "Anthropic incorporated user feedback that token consumption was too high, aiming to improve response speed and reduce token usage."
  - question: "What happens when the 'effort level' is high in Claude Code?"
    choices: ["It responds faster", "The depth of thought increases, solving complex problems better", "It automatically incurs more costs"]
    answer: 1
    explanation: "Effort level is linked to depth of thought, enhancing the ability to solve more complex problems."
  - question: "How did Anthropic resolve the recent quality decline issue?"
    choices: ["They charged users higher fees", "They reverted to the previous level on April 7", "They completely replaced the AI model"]
    answer: 1
    explanation: "Anthropic acknowledged that the measure was a misguided compromise and reverted the settings to the original, higher reasoning level on April 7, 2026."
lang: en
ref: 2026-08-23-Anthropic-appears-to-be-AB-testing-reduced-effort-levels-in-Claude-Code
audio: 2026-08-23-Anthropic-appears-to-be-AB-testing-reduced-effort-levels-in-Claude-Code.en.mp3
industry: general
---

Imagine you have a smart AI assistant that helps you with your daily tasks. How baffled would you be if a personal assistant that had been effortlessly solving complex coding problems until yesterday suddenly started providing overly simplistic answers or missing crucial context this morning? Recently, this is exactly what happened to users of "Claude Code," an AI-powered coding tool from Anthropic.

### Why does this matter?

This incident came as a major shock to those who use AI as a professional tool. It wasn't just a simple case of the model slowing down. The AI's "brainstorming" process was changed without the user's knowledge, resulting in an immediate blow to productivity. It is a significant case study showing that the AI services we use daily can have their performance altered without notice based on a company's internal policies.

### Easy explanation: What is AI 'Effort Level'?

Claude Code features something called **'Effort Level (a setting that determines how deeply the AI thinks to solve a problem)'**.

Simply put, this effort level is similar to the effort a student puts into solving exam questions. A 'low effort' level means glancing over the problem and quickly writing an answer, while a 'high effort' level means reading every sentence carefully, reviewing it, and thinking deeply. [Source: Claude Code effort level and model selection](https://claude.com/blog/claude-model-and-effort-level-in-claude-code)

Metaphorically, it's like a veteran chef who was cooking with all their heart suddenly switching to a convenience-food style to save on ingredients and time. Naturally, the consumer would be able to taste the difference.

Between February and March 2026, Anthropic lowered the default effort level of Claude Code from 'High' to 'Medium' without any notice. [Source: Claude Code's Thinking Depth Dropped 73%](https://claudeapi.com/en/blog/news/claude-performance-decline-effort-level-api-restored/) According to an Anthropic spokesperson, this was intended to reflect user feedback that token (the unit of language the AI uses) consumption was too high, with the goal of improving response speed and reducing costs. [Source: Anthropic faces user backlash over reported performance issues](https://fortune.com/2026/04/14/anthropic-claude-performance-decline-user-complaints-backlash-lack-of-transparency-accusations-compute-crunch/)

However, the result was disastrous. As this adjustment caused the AI's depth of thought to drop by a whopping 73%, users performing complex programming tasks felt a sharp decline in performance. [Source: Claude Code's Thinking Depth Dropped 73%](https://claudeapi.com/en/blog/news/claude-performance-decline-effort-level-api-restored/)

### Current Situation: Successive updates and confusion

It was revealed that the cause of the performance drop was the overlapping of three major updates. [Source: Anthropic Claude Code Quality Drop](https://devtoolpicks.com/blog/anthropic-claude-code-quality-fix-postmortem-2026) In particular, an A/B test (an experiment where two or more versions are shown randomly to compare performance) was conducted on some users in March, which caused issues such as limiting code plans to 40 lines or deleting necessary contextual information, sparking backlash from users. [Source: Anthropic A/B Tested Claude Code Plan Mode](https://agent-wars.com/news/2026-03-14-anthropic-ab-testing-claude-code-plan-mode-without-disclosure)

Eventually, Anthropic acknowledged that their decision was a 'misguided compromise' and reverted the settings to the previous level on April 7. [Source: Why Is Claude Code Slow?](https://www.aakashx.com/blog/claude-code-slow-causes-fixes/)

### What happens next?

This incident has served as a strong warning regarding the transparency of AI tools. Experts argue that companies providing professional AI tools must obtain user consent or at least provide advance notice when applying experimental changes. [Source: Mike Ramos Criticizes Anthropic](https://agent-wars.com/news/2026-03-14-anthropic-silent-ab-test-claude-code) Going forward, users will likely demand more strongly an environment where they can choose and adjust the 'effort level' provided by AI models themselves.

## MindTickleBytes AI Reporter's View

AI performance is not just a number; it is directly tied to user trust. This case, which showed how much productivity loss a "quiet change" made in the name of technical optimization can cause, clearly illustrates why AI companies should prioritize transparent communication. As more users rely on AI as a core professional tool in the future, such policy transparency will become a company's competitive advantage as important as its technical prowess.

## References

1. [Claude Code's Thinking Depth Dropped 73% — Anthropic Admits](https://claudeapi.com/en/blog/news/claude-performance-decline-effort-level-api-restored/)
2. [Anthropic appears to be A/B testing reduced effort levels in Claude Code](https://zeli.app/zh/story/49401549)
3. [Anthropic Claude Code Quality Drop: What Actually Happened](https://devtoolpicks.com/blog/anthropic-claude-code-quality-fix-postmortem-2026)
4. [Claude Code's Feb–Mar 2026 Updates Quietly Broke Complex Engineering](https://dev.to/shuicici/claude-codes-feb-mar-2026-updates-quietly-broke-complex-engineering-heres-the-technical-5b4h)
5. [Anthropic A/B Tested Claude Code Plan Mode Without Telling Users](https://agent-wars.com/news/2026-03-14-anthropic-ab-testing-claude-code-plan-mode-without-disclosure)
6. [An update on recent Claude Code quality reports \ Anthropic](https://www.anthropic.com/engineering/april-23-postmortem)
7. [Mike Ramos Criticizes Anthropic for Undisclosed A/B Test](https://agent-wars.com/news/2026-03-14-anthropic-silent-ab-test-claude-code)
8. [Claude Code effort level and model selection](https://claude.com/blog/claude-model-and-effort-level-in-claude-code)
9. [Why Is Claude Code Slow? Official Causes and Developer Fixes](https://www.aakashx.com/blog/claude-code-slow-causes-fixes/)
10. [Anthropic admits it dumbed down Claude with 'upgrades'](https://www.theregister.com/software/2026/04/24/anthropic-admits-it-dumbed-down-claude-with-upgrades/5228105)
11. [Anthropic faces user backlash over reported performance issues](https://fortune.com/2026/04/14/anthropic-claude-performance-decline-user-complaints-backlash-lack-of-transparency-accusations-compute-crunch/)
12. [Mystery solved: Anthropic reveals changes to Claude's harnesses](https://venturebeat.com/technology/mystery-solved-anthropic-reveals-changes-to-claudes-harnesses-and-operating-instructions-likely-caused-degradation)
13. [Anthropic is facing a wave of user backlash over reports of performance issues](https://finance.yahoo.com/sectors/technology/articles/anthropic-facing-wave-user-backlash-091348318.html)
14. [Anthropic explains Claude Code’s recent performance](https://fortune.com/2026/04/24/anthropic-engineering-missteps-claude-code-performance-decline-user-backlash/?ref=biztoc.com)