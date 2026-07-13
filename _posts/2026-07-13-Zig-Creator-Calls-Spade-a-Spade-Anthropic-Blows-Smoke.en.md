---
layout: post
title: "Is AI-written code 'garbage'? The head-on collision between programming language Zig and Anthropic"
description: "A look at the software development debate in the AI era through the case of Zig, a programming language that has completely banned AI-written code, and Bun, a project acquired by Anthropic that had to forgo a 4x performance boost as a result."
summary: "Programming language Zig has completely banned all contributions written by AI, leading to a situation where code developed by Bun—a project acquired by Anthropic—that provided a 4x performance boost could not be incorporated into the official project."
tags: [AI, Zig, Bun, Programming, Open Source]
image: 2026-07-13-Zig-Creator-Calls-Spade-a-Spade-Anthropic-Blows-Smoke.jpg
image_alt: "Graphic of programming code and AI robot icons colliding above a computer screen"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "The open source ecosystem is splitting into polar opposites over the use of AI tools. At the point where technical value and developer culture collide, what standards should we set?"
quiz:
  - question: "Why did the programming language Zig ban AI-related contributions?"
    choices: ["Because AI code is too expensive", "Because AI code has low quality and wastes review time", "Because of copyright issues"]
    answer: 1
    explanation: "Zig founder Andrew Kelley determined that AI-generated code is of low quality and not only wastes review time but lacks actual value."
  - question: "Why could the performance improvements developed by Anthropic's Bun project not be incorporated into the official Zig project?"
    choices: ["Because the performance improvement was insufficient", "Because of Zig's strict policy against AI contributions", "Because of technical compatibility issues"]
    answer: 1
    explanation: "Although Bun achieved a 4x performance boost, it could not include the code in the official project (upstream) due to Zig's strict AI contribution ban policy."
  - question: "What is the scope of Zig's ban on AI contributions?"
    choices: ["Only code is banned", "All forms of contribution including code, comments, issues, and bug report responses are banned", "Only existing contributors are banned"]
    answer: 1
    explanation: "Zig bans all forms of contributions involving AI, not just code, but also comments, issues, pull requests, and bug tracker responses."
lang: en
ref: 2026-07-13-Zig-Creator-Calls-Spade-a-Spade-Anthropic-Blows-Smoke
audio: 2026-07-13-Zig-Creator-Calls-Spade-a-Spade-Anthropic-Blows-Smoke.en.mp3
industry: general
---

Imagine you have a highly efficient mechanical device that you've spent months building through sleepless nights. This device works four times faster than existing parts. However, the moment you try to put this device on the official production line, the factory operator coldly says, "Did you use any artificial intelligence (AI) tools in the process of making this device? Then absolutely not. Throw it away immediately."

This is exactly what is happening in the world of open source programming. This incident between the programming language 'Zig' and the JavaScript runtime 'Bun,' which was acquired by Anthropic, raises a very fundamental concern that we face in this era where AI helps software development.

## Why is this important?

Behind the scenes, as our daily apps become increasingly intelligent, lies the effort of countless developers. Today, developers use AI tools to create software faster and more efficiently. However, the position that 'who and how it was made' is important is colliding head-on with the position that 'it doesn't matter as long as the technical results are good.' If results utilizing AI are rejected like in the case of Zig, developers might hesitate to use AI tools in the future. Conversely, if AI code overflows without any verification, who will be responsible for the stability of the software?

## The Explainer

Zig is a widely used high-performance programming language. And Bun is a JavaScript runtime built with Zig, which was recently acquired by the AI company Anthropic[Source 4, Source 6, Source 18].

Metaphorically speaking, Zig is a 'high-end woodshop' that values very fastidious craftsmanship. The representative of this woodshop, Andrew Kelley, described code written by AI as "invariably garbage"[Source 1, Source 5]. He determined that AI-written code has no practical value while wasting the precious review time of the core development team. So, he established a strict policy that bans contributions entirely if AI was involved in any way—not just in code, but also in comments, issues, and even responses to bug reports[Source 1, Source 2].

On the other hand, the Bun team actively used AI to achieve an amazing feat of increasing compilation speed (the process of converting human-written code into a language a computer understands) by about four times[Source 2, Source 3, Source 4]. However, the wall of Zig was high. The Bun team tried to include this excellent achievement in the official project, but because it was clear it would be rejected due to the fact that AI was used, they eventually decided to give up on reflecting it in the official project and maintain the project as a separate version (a fork)[Source 2, Source 4].

## Current Situation

Zig's position is firm. It adheres to its principles to the point where, if AI usage is suspected, it can be rejected without even considering the technical value[Source 2]. In fact, many developers are reacting heatedly to this policy. Some are expressing aversion to the Bun project's codebase and documentation being filled with 'AI slop,' and there is even talk of developers wanting to leave Bun[Source 17].

On the other hand, Anthropic and the Bun team are expected to continue using AI tools for technical advantages, as Bun is currently being used as infrastructure for Anthropic's 'Claude Code' or 'Claude Agent SDK'[Source 16, Source 18]. It is as if those who prioritize technical achievements and those who prioritize principles are walking their own paths while coexisting.

## What will happen in the future?

This debate is not just a problem for one project. 'To what extent should contributions using AI tools be allowed?' has become a task that all open source projects must answer in the future. Zig has presented a very extreme and clear standard. In the future, more projects will prepare their own 'AI contribution guidelines,' and they will be divided into those that completely ban it like Zig or those that accept it through appropriate verification processes. Developers now live in an era where they must carefully examine the policies of the projects they contribute to.

## MindTickleBytes Perspective

The argument that technology is merely a tool and the argument that the nature of the results created by that tool has changed are clashing sharply. What is important is not whether the tool was used itself, but what impact that tool has on the quality of the final result and the sustainability of the ecosystem. Whether Zig's strictness will become a shield that protects the purity of open source, or a path that invites self-isolation amidst the changing development flow, is something to watch a little longer.

## References

1. [Zig bans LLM contributions, forcing Bun to fork | AI Weekly](https://aiweekly.co/alerts/zig-bans-llm-contributions-forcing-bun-to-fork)
2. [Zig Draws Hard Line On AI, Bun Chooses Fork Over Upstreaming - Open Source For You](https://www.opensourceforu.com/2026/05/zig-draws-hard-line-on-ai-bun-chooses-fork-over-upstreaming/)
3. [ZIG BANNED ANTHROPIC FROM ITS OWN LANGUAGE #Shorts - YouTube](https://www.youtube.com/shorts/sYMuqS2oyUw)
4. [Zig Reinforces LLM Contribution Ban As Anthropic-Owned Bun Forks 4x Gain](https://winbuzzer.com/2026/05/01/zig-llm-contribution-ban-bun-4x-speedup-downstream-xcxwbn/)
5. [Zig president says AI coding contributions are 'invariably garbage,' so he banned them](https://www.businessinsider.com/zig-programming-language-ai-rules-2026-5)
6. [The Zig project's rationale for their firm anti-AI contribution policy](https://simonwillison.net/2026/Apr/30/zig-anti-ai/)
16. [Anthrophic's Bun team trials port from Zig to Rust](https://www.devclass.com/software/2026/05/11/anthrophics-bun-team-trials-port-from-zig-to-rust/5237835)
17. [This feels more like a reaction to Zig's anti-LLM policy than anything. Anthropi... | Hacker News](https://news.ycombinator.com/item?id=48017387)
18. [Bun’s Zig to Rust Rewrite: Anthropic’s AI Code Experiment | byteiota](https://byteiota.com/buns-zig-to-rust-rewrite-anthropics-ai-code-experiment/)