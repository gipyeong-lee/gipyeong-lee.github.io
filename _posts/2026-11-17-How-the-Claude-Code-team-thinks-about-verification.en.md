---
layout: post
title: "What if AI Does 90% of Coding? The Secret of 'Verification' According to the Claude Code Team"
description: "The Anthropic Claude Code team writes and reviews 90% of their codebase using AI. Learn why verification matters more than prompting."
summary: "Explore 'Verification' and specific workflows that serve as the core secret to maintaining code quality in the age of AI agents for the Claude Code team."
tags: [AI, ClaudeCode, Coding, Development, Anthropic]
image: 2026-11-17-How-the-Claude-Code-team-thinks-about-verification.jpg
image_alt: "An illustration of a developer utilizing an AI coding tool in front of a computer screen"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Rather than simply writing good prompts, making AI verify its own results based on evidence is the true core of the agentic era."
quiz:
  - question: "Approximately what percentage of code is written and reviewed by Claude in the Claude Code team?"
    choices: ["About 50%", "About 90%", "About 30%"]
    answer: 1
    explanation: "Approximately 90% of the Claude Code team's total code is written and reviewed by Claude."
  - question: "What do Claude Code developers consider the most powerful lever for improving quality?"
    choices: ["Writing more sophisticated prompts", "Making AI verify its own work", "Limiting code length"]
    answer: 1
    explanation: "Developers like Boris Cherny agree that 'Verification' is a more powerful quality improvement lever than prompting."
  - question: "Which of the following is correct regarding how the Claude Code team understands complex codebases?"
    choices: ["Memorize the entire model in your head", "Rebuild understanding on demand by asking Claude to explain specific slices whenever needed", "Do not read code at all"]
    answer: 1
    explanation: "Instead of keeping the entire model in their heads, team members rebuild their understanding on demand by asking Claude to explain specific slices when needed."
lang: en
ref: 2026-11-17-How-the-Claude-Code-team-thinks-about-verification
audio: 2026-11-17-How-the-Claude-Code-team-thinks-about-verification.en.mp3
industry: creative
---

Imagine this: You come to work in the morning and sit in front of your computer, and Artificial Intelligence (AI) deftly handles 90% of the complex programming tasks you need to do today. The time you spend directly hammering the keyboard typing code decreases noticeably, unfolding a daily routine where you meticulously review the output brought by AI. This is not a story from a distant future sci-fi movie; it is the actual daily routine of the development team behind Claude Code, the terminal-based coding agent by world-class AI company Anthropic [Source 1, Source 11].

So how are developers at the forefront—who directly build the world's most advanced AI—stably managing this massive and complex system? Many people simply think, "If we just write prompts (commands given to AI) more plausibly and sophisticatedly, it'll work." However, the real secret to success revealed by the Claude Code team completely upends our expectations. They unanimously agree that **"Verification (the process of objectively checking whether results are correct) is far more important than prompting"** [Source 3]. In this article, let's step by step explore how they thoroughly maintain software quality in an era where AI leads coding.

---

## Why Does This Matter?

We often imagine that when the AI age arrives, an easy world will come where humans just need to toss out cool questions. As if ordering "Make me a program like this" would instantly yield a flawless result. However, in actual practice—especially in building massive software exceeding hundreds of thousands of lines—the process of verifying whether AI-written code actually functions correctly and whether there are hidden bugs (defects or errors in programs) determines the success or failure of the entire task.

What would happen if we blindly trusted AI-generated code without any verification and deployed it to a production service, only for the entire system to crash? Countless customers would instantly suffer major inconvenience, and the company would incur astronomical financial and reputational losses. Therefore, in an era where AI writes code on our behalf, establishing a **"verification system that objectively proves with evidence whether the output is truly correct"** through close collaboration between humans and AI becomes a core factor determining a company's survival. By examining how the Claude Code team is solving this difficult challenge, we can gain clear hints on how to view and handle the various autonomous AI tools approaching our daily lives.

---

## Easy Understanding: An Automated Grader More Important Than the "Prompt" Order

To help readers understand, let's use an everyday analogy. A **prompt-centric approach** is like going to a famous chef and verbally giving a long order: "Make me a delicious and healthy dinner." The chef will do their best, but because the criteria for "delicious and healthy" are so subjective from person to person, salty food might come out or nutrition balance might be off.

On the other hand, the **verification-centric approach** emphasized by the Claude Code team is like setting up a strict "grading rubric" and an "automated grader" next to the kitchen. It is a method of pre-establishing specific passing criteria: "This dish must have a sodium concentration of exactly 0.8% or lower, the cooking time must not exceed 20 minutes, and it must pass tests verifying that the oven temperature sensor operates normally." Following these criteria, the AI cooks the dish itself, runs the test machine, and only then reports that the dish is complete.

In fact, key developers including Boris Cherny of the Claude Code team emphasize that **"The most powerful quality improvement lever in Claude Code is making AI verify its own work"** [Source 3].

Here is another interesting shift in working style. Instead of giving developers detailed, minute-by-minute instructions for each "task," the Claude Code team assigns big-picture **"goals"** [Source 2]. Rather than giving trivial instructions like moving a mouse or keyboard—such as "fix this button's margin by 2 pixels and split the internal function"—they toss out a broad goal: "Improve the user experience (UX) of this screen to meaningfully reduce mobile loading times." Then, Claude runs an Agent Loop (an iterative autonomous execution process where AI thinks, executes tools, and fixes errors on its own), finds the necessary files, fixes the code, runs test commands, and proves for itself that its output is correct.

As another analogy, dealing with millions of lines of massive source code is like trying to memorize every alleyway of a complex metropolis in your head. However, the Claude Code team exercises the wisdom to **"rebuild understanding on demand instead of forcibly remembering the whole thing"** [Source 6]. Just like turning on GPS navigation zooms in clearly on only the immediate neighborhood of the alleyway you are passing through, rather than keeping all the code in your brain, when you need to modify a specific section, you ask Claude to explain that piece of code in real-time to grasp the context and proceed with the work [Source 6].

---

## Current Status: AI Writes 90% of Code, Backed by a 6-Layer Defense Shield

Inside the Claude Code team right now, remarkably, **about 90% of all code is written and reviewed by Claude** [Source 1, Source 7]. The traditional development era where human developers hammered keyboards from start to finish typing line by line has already passed, and the central role is now shifting to being an orchestrator (a role coordinating the overall flow like an orchestra conductor) who carefully tunes and guides the direction of AI-written code.

So how can the system run flawlessly without becoming unstable when AI writes 90% of the code? The robust secret lies in a thoroughly designed **"Verification Layer."** Typical code changes written by Claude Code must pass as many as **6 verification checkpoints** before finally being submitted as a PR (Pull Request, the process where developers request merging their written code into the main codebase) [Source 7].

This seamlessly includes not only the self-verification processes developers go through before submitting a PR, but also strict mandatory CI (Continuous Integration, a system that continuously integrates source code changes and tests them automatically) checks that run automatically on the server whenever code changes [Source 7]. In other words, no matter how plausible the code AI brings is, it has a safe architecture where it can never be reflected in actual production source code unless it passes all of these demanding 6-layer automated verification gates.

---

## What's Next?

Synthesizing the direction led by Anthropic founder Dario Amodei and top researchers along with the vivid insights of the Claude Code team, the upcoming AI coding and agent ecosystem will further evolve in three core directions [Source 9]:

1. **Advancement of Verification and Autonomous Automation Loops**: Going beyond simple text generation models, an "agent loop" system where AI directly executes code, runs tests, and diagnoses and fixes errors on its own will become the industry standard [Source 5].
2. **Settlement of Context Minimalism**: Rather than confusing AI by injecting unnecessarily massive informations all at once, an efficient working method of selectively and accurately utilizing only the minimum necessary information at the exact moment needed will become mainstream [Source 5].
3. **Popularization of Routines and Auto Mode**: An environment where AI works autonomously based on robust safety mechanisms (verification systems) within repetitive development loops—without humans standing by and monitoring every step—will expand across all development sites [Source 5].

Ultimately, future development and problem-solving do not depend on "how slickly you can prompt AI." Instead, success or failure will depend on **"how well you establish robust tests and verification criteria that can prove whether the massive output brought by AI is truly trustworthy."**

---

## AI Perspective (MindTickleBytes AI Journalist's Perspective)

Many people want AI to be a "magic box" that automatically solves all the complex problems in the world. However, as the vivid case of Anthropic's Claude Code team clearly proves, true productivity improvements do not come from illusory, magical prompts, but from cold, rigorous "verification systems." As AI gets smarter, the human role is evolving beyond a simple coder or monitor into a fair, strict "chief judge" and a direction-setting "strategist." This is why an attitude that never loses sight of fundamentals and the value of verification becomes all the more precious as technology advances.

---

## References

1. How the Claude Code team thinks about verification - https://claude.dev/blog/how-the-claude-code-team-thinks-about-verification/
2. How the Claude Code team uses Claude Code - YouTube - https://www.youtube.com/watch?v=S-sYlFiGFv8
3. Verification Beats Prompting, Boris Cherny's Top Claude Code Tip... - https://blog.vibecoder.me/verification-beats-prompting-claude-code-boris-cherny
4. Claude Code by Anthropic | AI coding agent and assistant - https://claude.com/product/claude-code
5. Claude Code's Creators Explain Agent Loops & How... | The Neuron - https://www.theneuron.ai/explainer-articles/claude-code-creators-boris-cherny-and-cat-wu-explain-how-to-use-agent-loops/
6. Critical thinking when agents do the work... | Thread Navigator - https://threadnavigator.com/thread/2117512471930167377/
7. How the Claude Code team reviews code that Claude writes - https://heybrahim.com/notes/claude-code-team-code-review.html
8. Dario Amodei: Anthropic CEO on Claude, AGI & the Future... - YouTube - https://www.youtube.com/watch?v=ugvHCXCOmm4
9. Claude (AI) - Wikipedia - https://en.wikipedia.org/wiki/Claude_(AI))
10. Claude by Anthropic | The AI for problem solvers - https://claude.com/
11. Newsroom \ Anthropic - https://www.anthropic.com/news