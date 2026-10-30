---
layout: post
title: "Wait, AI writes a 'plan' before it writes code? — How to safely collaborate with AI"
description: "Learn about the importance of 'Plan Mode,' which prevents AI agents from modifying code recklessly, and the necessity of code verification."
summary: "We introduce a verification system that prevents errors in AI collaboration through 'Plan Mode,' which requires AI agents to obtain human approval before modifying code."
tags: [AI, Agent, Coding, Plan Mode, AI Safety]
image: 2026-10-30-Until-You-approve-the-plan-a-separate-agent-checks-the-code-against-it.jpg
image_alt: "A human reviewing an AI plan on a tablet screen and pressing the approve button"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Trust AI's capabilities, but verify them thoroughly. Plan Mode is the bridge that allows AI and humans to perfectly understand and trust each other's intentions."
quiz:
  - question: "What is the core role of AI's 'Plan Mode'?"
    choices: ["Allows the AI to automatically complete deployment", "Ensures the AI gets human approval before modifying code", "Doubles the AI's processing speed"]
    answer: 1
    explanation: "Plan Mode is a safety mechanism that ensures an AI agent writes a plan and obtains human approval before modifying code or creating files."
  - question: "What method is used in agent-centric development environments to improve code quality?"
    choices: ["Humans write all the code themselves", "Utilizing a separate reviewer agent and CI tools", "Deploying without AI approval"]
    answer: 1
    explanation: "In modern AI development workflows, a separate reviewer agent is used alongside CI (Continuous Integration) tools to evaluate code and plans against each other, ensuring quality."
  - question: "What is the criteria for an AI to apply modifications in a security-critical environment?"
    choices: ["Applying after testing only within the scope approved by the customer", "AI judging for itself and applying immediately", "Applying first and checking later"]
    answer: 0
    explanation: "In security-critical platforms, modifications are applied only after testing within the customer-approved scope and obtaining explicit approval."
lang: en
ref: 2026-10-30-Until-You-approve-the-plan-a-separate-agent-checks-the-code-against-it
audio: 2026-10-30-Until-You-approve-the-plan-a-separate-agent-checks-the-code-against-it.en.mp3
industry: finance
---

Imagine you hired a contractor for a home renovation, but the carpenter tore down all your walls without a word and only then asked, "So, how should we fix this?" You would be incredibly flustered and angry. The AI coding tools we use are no different. You might ask an AI to "build this feature," but if it starts hacking away at your code without rhyme or reason, you could be in for a big headache.

With recent advancements in AI, we have entered the era of 'agents'—AI that can judge and perform tasks autonomously. But how do we ensure these agents move according to our intentions without making mistakes? Today, we are going to talk about a safety mechanism called 'Plan Mode,' which forces AI to write a 'plan' before it modifies any code.

## Why is this important?

For those using AI in their daily lives, this is a critical issue. If an AI unexpectedly alters the payment function of a website or accidentally deletes an essential system configuration file, your operations could be paralyzed instantly.

Although AI might appear to think and act like a human, it often fails to understand the 'context' of our situation 100%. Therefore, a process where a human reviews a plan in advance and approves it, saying, "Yes, proceed with modifications in this direction," is essential before the AI touches any code. Through this, we can preemptively prevent catastrophic mistakes that an AI might make.

## Easy to Understand: 'Plan Mode' as a Design Review Process

Think of 'Plan Mode' as a 'design review process' before construction begins.

1. **Exploration Phase**: The AI agent reads your computer (codebase) to investigate what is needed. During this stage, it only has 'read-only' access. It has absolutely no permission to modify or delete files. [Source: PlanMode: Make ClaudeCodeThink BeforeItTouches...](https://articles.gg/a/plan-mode-make-claude-code-think-before-it-touches-anything)
2. **Planning Phase**: The AI writes a detailed plan of what it intends to change. It is similar to an architect showing you the blueprints before construction starts.
3. **Approval Phase**: You review this plan and press the 'approve' button if it meets your requirements. Only after approval does the AI finally begin modifying the code. [Source: Google Antigravity use case - The HQ Digital](https://thehqdigital.com/google-antigravity-use-case/)

By doing this, a human can stop the AI before it tears down the wrong wall. In fact, many secure workflows strictly prohibit AI from coding spontaneously without a plan. [Source: arXiv Review Paper Harness](https://appautomaton.renocrypt.com/latex-arxiv-SKILL/)

## Current Level of Verification

In the current AI development field, verification doesn't just end with plan approval; it includes an even tighter net of checks.

- **Emergence of Reviewer Agents**: There are 'reviewer agents' sophisticated enough that a human doesn't need to check every single line of code after the AI finishes it. These agents automatically verify whether the AI implemented the code according to the plan by comparing the code to the original plan. [Source: Two Gates and a Night Shift | Vinny Carpenter](https://vinny.dev/blog/2026-07-06-two-gates-and-a-night-shift/)
- **Enhanced Security**: Companies that prioritize security force AI to test its proposed modifications only within the scope approved by the customer. It is a rule that says, "Don't just fix it—verify that it is safe within this scope before fixing it." [Source: Oracle Announces AI Security Mesh Powered by OpenAI Cyber Models](https://www.unite.ai/oracle-announces-ai-security-mesh-powered-by-openai-cyber-models/)

## What will happen in the future?

In the future, using 'plans' as a common language when collaborating with AI will become a daily routine. While it is mainly used in coding today, this 'Plan Mode' is expected to become an essential standard for when AI handles professional tasks such as document writing, accounting, and data analysis. When you assign a task to an AI, the first thing it will present will be a plan, saying, "This is how I intend to handle the task."

MindTickleBytes' AI Reporter perspective: Technology advances rapidly, but safety is a value that cannot be compromised. This 'verification system' that forces AI agents not to exceed human instructions is an essential 'fence of trust' required for AI to be fully integrated into our daily lives.

## References

1. [Making Cursor’s agent write plans as artifacts so I can comment on them inline](https://forum.cursor.com/t/making-cursor-s-agent-write-plans-as-artifacts-so-i-can-comment-on-them-inline/175414)
2. [arXiv Review Paper Harness](https://appautomaton.renocrypt.com/latex-arxiv-SKILL/)
3. [PlanMode: Make ClaudeCodeThink BeforeItTouches...](https://articles.gg/a/plan-mode-make-claude-code-think-before-it-touches-anything)
4. [Google Antigravity use case - The HQ Digital](https://thehqdigital.com/google-antigravity-use-case/)
5. [Oracle Announces AI Security Mesh Powered by OpenAI Cyber Models](https://www.unite.ai/oracle-announces-ai-security-mesh-powered-by-openai-cyber-models/)
6. [Two Gates and a Night Shift | Vinny Carpenter](https://vinny.dev/blog/2026-07-06-two-gates-and-a-night-shift/)