---
layout: post
title: "Ever wondered 'Why did it write it like that?' looking at AI code? Could 'Specification-First Development' be the answer?"
description: "Introducing the issue of forgetting the intent behind code written by AI coding agents and the 'Specification-First Agentic Development (SFAD)' methodology to solve it."
summary: "In the era of AI-driven coding, 'Specification-First Agentic Development (SFAD)' is gaining attention as a methodology to prevent code that no one remembers by reviewing and documenting specifications before work begins."
tags: [AI, Development, Coding, Productivity, Technology]
image: 2026-10-28-Show-HN-Specification-First-Agentic-Development-Plugin-and-Prove.jpg
image_alt: "AI agent and human developer collaborating, communicating with detailed design documents displayed on the screen"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "At the intersection where AI speed clashes with deep human thought, specifications will serve as more than just records; they will be the landmarks that guide us to understand code."
quiz:
  - question: "What is the core problem that Specification-First Agentic Development (SFAD) aims to solve?"
    choices: ["AI learning speed degradation", "Loss of context and forgetting code intent", "Increased hardware costs"]
    answer: 1
    explanation: "SFAD aims to prevent the problem where no one remembers the reason for AI-built code after time passes, and to prevent architectural degradation."
  - question: "Which of the following is correct regarding the core procedure of the SFAD methodology?"
    choices: ["Write code first and generate specifications later", "Review specifications before work, isolated work environments, step-by-step approval", "Letting AI decide all requirements by itself"]
    answer: 1
    explanation: "SFAD follows the method of defining problems and validating constraints before writing code, and then finalizing specifications."
  - question: "Why is a critical view raised regarding Specification-First Development?"
    choices: ["Due to the cost of writing too many specifications", "Because in real product environments, initial requirements are often not fully known in advance", "Because AI cannot understand specifications"]
    answer: 1
    explanation: "It is pointed out that since decisions are often made in product development environments without even knowing what is unknown, excessive initial specifications can actually cause confusion."
lang: en
ref: 2026-10-28-Show-HN-Specification-First-Agentic-Development-Plugin-and-Prove
audio: 2026-10-28-Show-HN-Specification-First-Agentic-Development-Plugin-and-Prove.en.mp3
industry: creative
---

Imagine this. A few months ago, you asked an AI agent to build a cool new website feature. Now, a bug has suddenly appeared, and you need to fix the code. You open the file, but you have no idea why it was written that way. "Why did I implement it like this?", "Why did the AI choose this design approach?"

In the age where AI churns out code in the blink of an eye, we are increasingly losing the 'roots' and 'intent' behind that code. 'Specification-First Agentic Development (SFAD)', which has recently been gaining attention among developers, stems from this very dilemma. [Specification-First Agentic Development - GitHub](https://github.com/holgerleichsenring/specification-first-agentic-development)

## Why does this matter?

Development in the past involved humans writing every line, so at least the context of 'why' something was done lived in the developer's head. However, now that AI leads the coding, a phenomenon is occurring where even just six months after a project starts, no one remembers why the code was built in that structure. This is called 'Context Amnesia'. [Specification-First Agentic Development - GitHub](https://github.com/holgerleichsenring/specification-first-agentic-development)

When this situation repeats, 'Architectural Drift' occurs, where the design diverges from the system's original intent. This is the primary culprit behind skyrocketing corporate maintenance costs and, ultimately, technical debt. To collaborate more deeply with AI, the process of proving 'why' we are building something is more essential than simply making code quickly.

## In simpler terms

To use an analogy for SFAD, it is like **"finalizing detailed blueprints before starting a building and carefully recording every change made during construction in a diary."**

Whereas in the past, one might vaguely request, "Make this feature," the SFAD method goes through much more systematic steps:

1. **Define Use Cases**: Clearly define "Why is this feature needed?" before writing any code. [Brendan Small — SFAD](https://brendansmall.co/sfad)
2. **Write and Review Specifications**: After concretizing the problem and validating constraints, 'lock' those specifications. [Brendan Small — SFAD](https://brendansmall.co/sfad)
3. **Step-by-Step Execution**: Have the AI agent write the code according to the reviewed and finalized specifications, and record even minor changes after approval. [Spec-first agentic development - spec-first.dev](https://spec-first.dev/)

By doing this, you can always check the landmark known as the 'specification' while the AI writes the code. Plugins developed for this purpose integrate with AI tools like Claude Code, forcing the AI to record and review specifications when performing tasks. [Spec-First - Spec-driven agentic - Hacker News | Zeli](https://zeli.app/story/50260571)

## Where do we stand now?

Many developers are already applying this method in the field. A developer who has been using this plugin since early 2026 stated that they have successfully built over 500,000 lines of code by writing over 1,000 specifications. [Show HN: Spec-first agentic development plugin reports 500k...](https://shortsingh.com/article/show-hn-spec-first-agentic-development-plugin-reports-500k-lines-built-from-1-00)

However, this is not the right answer for every situation. Some point out that actual product development environments are highly fluid. They argue that specifying everything at the initial stage can actually be inefficient. Since many projects start without even knowing what they don't know, critics argue that excessive initial specifications can convey conflicting requirements to AI, causing confusion. [Show HN: Specification First Agentic Development Plugin and Prove](https://hn.nuxt.dev/item/50260571)

## What is coming next?

Collaboration between AI and humans will become increasingly sophisticated. 'Agentic-first Development', where AI takes full responsibility for the entire process—from planning to implementation and maintenance—beyond just the stage of code production, is becoming a reality. [Let’s Talk Agentic Development | Spotify x Anthropic Live](https://www.youtube.com/watch?v=fHDGQHr_agg)

In the future, the new benchmark for 'skill' will not just be about AI generating code, but how logically it can explain the rationale behind the design it created. As a starting point, SFAD will likely serve as an important milestone in transforming AI from an uncontrollable black box into a trustworthy collaborative tool.

---

### MindTickleBytes' AI Reporter Perspective
More important than the fact that AI agents can do our coding for us is the fact that we now have a common language (specifications) with which to 'converse' with AI. A method that adds human judgment to AI speed will soon become the standard of the future.

## References

1. [Show HN: Specification First Agentic Development Plugin and Prove](https://hn.nuxt.dev/item/50260571)
2. [Spec-first agentic development · spec-first.dev](https://spec-first.dev/)
3. [Spec-First - Spec-driven agentic · Hacker News | Zeli](https://zeli.app/story/50260571)
4. [Specification-First Agentic Development - GitHub](https://github.com/holgerleichsenring/specification-first-agentic-development)
5. [Releases · holgerleichsenring/specification-first-agentic ...](https://github.com/holgerleichsenring/specification-first-agentic-development/releases)
6. [Show HN: Spec-first agentic development plugin reports 500k ...](https://shortsingh.com/article/show-hn-spec-first-agentic-development-plugin-reports-500k-lines-built-from-1-00)
7. [spec-first: 规范驱动的代理开发插件 — Show HN: Specification First...](https://zeli.app/zh/story/50260571)
8. [Brendan Small — Specification First Agentic Development](https://brendansmall.co/)
9. [Books by Anatoly Volkhover | Agentic Spec-Driven Development...](https://anatoly.com/books)
10. [Let’s Talk Agentic Development | Spotify x Anthropic Live - YouTube](https://www.youtube.com/watch?v=fHDGQHr_agg)
11. [Flowith AI - Your Agentic Workspace](https://flowith.io/)
12. [Manus: Hands On AI](https://manus.im/)
13. [Book Review: Agentic Spec-Driven Development](https://www.plainionist.net/Agentic-Spec-Driven-Development/)
14. [SFAD — Specification First Agentic Development | Brendan Small](https://brendansmall.co/sfad)
15. [jsell-rh/agentic-development-plugins | Awesome Claude Plugins](https://awesomeclaudeplugins.com/jsell-rh/agentic-development-plugins)
16. [Let’s Talk Agentic Development: Spotify x Anthropic Live](https://engineering.atspotify.com/2026/4/anthropic-agentic-development)