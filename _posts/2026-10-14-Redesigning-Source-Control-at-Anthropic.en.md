---
layout: post
title: "AI fixes code 30,000 times? Why Anthropic abandoned 'Git'"
description: "With AI writing so much code that it pushed existing version control systems to their limits, Anthropic shares the story of switching to its self-developed system, 'Scion'."
summary: "As the AI model Claude began generating over 30,000 code changes daily, Anthropic abandoned its existing Git-based infrastructure and developed and introduced its own version control system, 'Scion'."
tags: [Anthropic, AI Development, Version Control, Scion, Claude]
image: 2026-10-14-Redesigning-Source-Control-at-Anthropic.jpg
image_alt: "Graphic visualizing an interaction between a complex code network and AI agents"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "The productivity of AI, surpassing that of human developers, is shaking the foundations of existing tool ecosystems. We are in an era where infrastructure itself must be designed for 'agents'."
quiz:
  - question: "What is the primary reason Anthropic introduced its own version control system, 'Scion', instead of the existing Git?"
    choices: ["To reduce costs", "Due to bottlenecks in the existing system caused by the explosive code generation of AI agents", "To provide more secure security features"]
    answer: 1
    explanation: "It was because the volume of code merges surged from 2,500 to 30,000 per day during the process of AI writing and iterating code itself, rendering the existing infrastructure incapable of handling it."
  - question: "For what kind of environment was Anthropic's new system, 'Scion', designed?"
    choices: ["An offline environment used only by human developers", "An environment where AI agents write and iterate code 24/7", "An environment dedicated to mobile app development"]
    answer: 1
    explanation: "Scion was designed and optimized for an environment where AI agents constantly generate code and perform self-iterative learning."
  - question: "What method did Anthropic introduce instead of running all tests after every code change?"
    choices: ["Skipping tests entirely", "Deterministic Test Impact Analysis", "Randomly selecting tests"]
    answer: 1
    explanation: "Instead of running all tests for countless code changes, they introduced a deterministic test impact analysis service that selects and runs only the necessary tests based on past data and package dependencies."
lang: en
ref: 2026-10-14-Redesigning-Source-Control-at-Anthropic
audio: 2026-10-14-Redesigning-Source-Control-at-Anthropic.en.mp3
industry: creative
---

Imagine someone modifying what you wrote 30,000 times every second and asking you to review it again. It would be a speed impossible for a human to handle. Yet, this is exactly what is happening right now in the offices of AI company Anthropic. As their AI model, Claude, iterates on its own research and builds new services, the company's coding infrastructure has started to scream.

### Why does this matter?

Until now, software development has been geared toward the speed of 'humans'. But as AI has started writing code directly, managing and deploying that code has become a greater bottleneck than writing it itself. [Anthropic faced a situation where their coding infrastructure could no longer keep up with AI's productivity.](https://www.theregister.com/devops/2026/10/13/anthropic-reinvents-source-control-as-claude-floods-the-world-with-code/5302943) Anthropic's complete overhaul of their infrastructure is an important milestone showing how development tools must evolve in the age of AI.

### Easy to understand: The limits of the 'Git' puzzle box

'Git', which we commonly use, is a collaborative workspace where developers store and modify code. A simple analogy would be a 'puzzle box' where multiple people assemble one massive puzzle. When there are only a few people, they can take turns and fit the pieces together.

But what happens if AI agents dive into this puzzle box and start swapping thousands of pieces every second? The box will burst. Because existing Git was designed under the premise of a human-centric 'offline' development environment, it was too heavy to handle tens of thousands of changes pouring out from AI in real-time. [Anthropic's daily code merge volume skyrocketed nearly 12-fold, from 2,500 to 30,000.](https://braindetox.kr/en/posts/anthropic_scion_version_control_replaces_git_2026.html)

So, Anthropic built an entirely new type of system from scratch: **'Scion'**. Scion is an 'AI-exclusive version control system' designed to handle AI agents modifying code around the clock without resting. [Anthropic migrated their existing monorepo from Git to Scion over a five-month period.](https://braindetox.kr/en/posts/anthropic_scion_version_control_replaces_git_2026.html)

### Current state: Infrastructure improvements matched to AI speed

Anthropic didn't just change their version control system. Along with the introduction of Scion, they made several key changes.

1.  **Evolution of code review tools**: It's impossible for humans to review tens of thousands of lines of code. Anthropic introduced a new system dedicated to code review called **'Antique'**, creating an environment where humans can efficiently review changes pouring out from AI. [Anthropic developed and deployed this new code review surface alongside Scion.](https://braindetox.kr/en/posts/anthropic_scion_version_control_replaces_git_2026.html)
2.  **Smarter testing systems**: Running all tests every time code is changed takes too much time. So, Anthropic introduced a **'Deterministic Test Impact Analysis service'** that analyzes past data and code relationships to select and run only the absolutely necessary tests. [This method increased test execution efficiency, boosting development speed once again.](https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic)

### Where do we stand?

Anthropic's case is a harbinger showing that the software development environment is shifting from 'human-centric' to 'AI-agent-centric'. Just as developers used to worry about computer performance, the time has come to worry about whether computers can handle the activities of agents. This change is not limited to Anthropic. In the future, countless tech companies will be looking for new infrastructure that can support the enormous productivity of machines, going beyond human convenience.

### What happens next?

The update cycles of the services we use will become increasingly shorter, and behind them will sit new forms of 'digital factories' struggling to grow on their own, just like this. Infrastructure like Scion symbolizes that AI has entered a 'self-development' stage where it goes beyond a simple tool and redesigns its own technological foundations. [Scion was specifically designed for an 'Agent-always-on' scenario where AI operates constantly.](https://zeli.app/zh/story/50073633)

We are now standing at an interesting turning point, moving past the era where human developers wrote code to an era where AI writes code and humans supervise the results.

---

**MindTickleBytes' AI Reporter's Perspective**
The 'Agentic' era, where AI iterates and researches code on its own, has already begun. Anthropic's move signifies that AI has entered a stage of self-development where it goes beyond consuming technology to redesigning its own underlying infrastructure.

## References

1. [AnthropicClaude Can NowControlYour Computer - YouTube](https://www.youtube.com/watch?v=eB7E-mtpC18)
2. [Anthropic(Anthropic)](https://huggingface.co/Anthropic)
3. [How AI is transforming workatAnthropic\Anthropic](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)
4. [Agentic coding is straining CI. Here’s how we... | Claude byAnthropic](https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic)
5. [AnthropicAI safety researcher quits with 'world in peril' warning](https://www.bbc.com/news/articles/c62dlvdq3e3o)
6. [EggheadsatAnthropicSaid They Used Claude to "Solve" Humor](https://futurism.com/artificial-intelligence/anthropic-solve-humor)
7. [Anthropicrestores Fable 5, Mythos 5 after U.S. lifts exportcontrols](https://www.linkedin.com/pulse/anthropic-restores-fable-5-mythos-after-us-lifts-export-controls-3ffnc)
8. [Redesigning source control at Anthropic — CodeNews.com](https://codenews.com/news/redesigning-source-control-at-anthropic-1ojqmz)
9. [Anthropic Scion: Why Its Monorepo Left Git at 30,000 Merges](https://braindetox.kr/en/posts/anthropic_scion_version_control_replaces_git_2026.html)
10. [Anthropic Scion Redesigns Source Control for AI Agents](https://scalevise.com/resources/anthropic-scion-agent-scale-source-control/)
11. [Anthropic reinvents source control as Claude floods the world ...](https://www.theregister.com/devops/2026/10/13/anthropic-reinvents-source-control-as-claude-floods-the-world-with-code/5302943)
12. [Anthropic Overhauls Source Control to Fix Bottlenecks](https://book.st-hakky.com/en/news/redesigning-source-control-at-anthropic)
13. [Redesigning source control at Anthropic - hoton.ai](https://hoton.ai/en/news/redesigning-source-control-at-anthropic-1vlb4uz)
14. [Anthropic 因Claude重写版本控制系统 — Redesigning Source Control a...](https://zeli.app/zh/story/50073633)
15. [Newsroom \Anthropic](https://www.anthropic.com/news)
16. [AnthropicIs Bleeding Out](https://www.wheresyoured.at/anthropic-is-bleeding-out/)
17. [Hidden AI instructions reveal howAnthropiccontrols... - Ars Technica](https://arstechnica.com/ai/2025/05/hidden-ai-instructions-reveal-how-anthropic-controls-claude-4/)
18. [OpenAI andAnthropicAI crisis explained: OpenAI andAnthropicfear...](https://economictimes.indiatimes.com/world/business/openai-and-anthropic-fear-a-major-ai-crisis-in-the-next-6-to-12-months-heres-what-theyre-preparing-for/articleshow/134860984.cms)
20. [LatestAnthropic(Claude AI) Statistics (2025) | StatsUp](https://analyzify.com/statsup/anthropic)