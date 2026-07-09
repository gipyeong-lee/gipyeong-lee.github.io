---
layout: post
title: "Drawing as I speak? 'Agent Draw', an AI collaborating with you in real-time"
description: "We explore the Agent Draw tool and its principles, allowing you to draw in real-time on an infinite canvas just by talking to the AI."
summary: "Agent Draw is an interactive tool that allows an AI agent to understand user voice commands and draw or place shapes directly on an infinite canvas in real-time."
tags: [AI, Agent, tldraw, Creativity, Tool]
image: 2026-07-09-Show-HN-Agent-Draw-An-agent-draws-while-you-talk-built-on-TLDraw.jpg
image_alt: "The Agent Draw interface screen where AI is drawing on an infinite canvas in real-time."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Beyond simple image generation, this is the first step toward AI physically interacting with the user within the space of a canvas."
quiz:
  - question: "What technology is Agent Draw built upon?"
    choices: ["Figma", "TLDraw SDK", "Adobe Photoshop"]
    answer: 1
    explanation: "Agent Draw is built on tldraw, an infinite canvas SDK based on React."
  - question: "How does the user send commands to the agent?"
    choices: ["Dedicated keyboard input", "Voice and text conversation via the right-hand chat panel", "Uploading image files"]
    answer: 1
    explanation: "Users can converse with the agent and provide context via voice or text through the chat panel on the right side of the screen."
  - question: "How does Agent Draw handle multiple requests?"
    choices: ["Processed in random order", "State machine processing using a FIFO (First-In, First-Out) queue", "All requests are processed in parallel simultaneously"]
    answer: 1
    explanation: "When multiple requests come in, it uses a FIFO queue and a state machine to process one session at a time sequentially."
lang: en
ref: 2026-07-09-Show-HN-Agent-Draw-An-agent-draws-while-you-talk-built-on-TLDraw
audio: 2026-07-09-Show-HN-Agent-Draw-An-agent-draws-while-you-talk-built-on-TLDraw.en.mp3
industry: creative
---

Imagine this: you're staring at a blank sheet of paper and say, "Draw me a delicious pizza here," and right before your eyes, the AI starts drawing lines, sketching out cheese and pepperoni. This magical scenario is getting ready to become part of our daily lives. The recently released 'Agent Draw' is completely changing the way we collaborate with AI.

### Why is this tool getting attention?

Until now, when we asked AI to draw something, we would usually input a prompt, wait a moment, and simply 'receive' the finished result. In other words, the AI was more of an entity that unilaterally handed us an output. But Agent Draw is completely different. It demonstrates a process of 'collaboration' where it constantly communicates with the user on the canvas and draws together in real-time [2](https://www.youtube.com/watch?v=iIH2hJAxxm8).

This means that creative work is no longer a solitary process. Just as you would finish a drawing by exchanging ideas with a colleague in front of a whiteboard in a conference room, human and AI can now work together in the same space. AI is moving beyond its role as a mere 'tool' that generates results and is being reborn as an active 'colleague' standing on the canvas with you [13](https://gitnation.com/contents/agents-on-the-canvas-with-tldraw).

### How does it work?

The working principle of Agent Draw is more sophisticated than you might think. To put it simply, imagine there is a 'smart AI robotic arm' on the canvas that acts as an extension of your hand, drawing for you even if you don't draw it yourself.

1. **Infinite Canvas (tldraw SDK)**: This is the foundational canvas environment. It uses 'tldraw', a React-based infinite canvas SDK, to create a space where the AI can freely place shapes and draw [1, 15](https://tldraw.dev/blog/tldraw-mcp-app).
2. **Agent Starter Kit (Basic training course)**: This acts as the 'fundamentals' that teach the AI how to draw and handle shapes. Through this kit, the AI can read and place basic shapes like rectangles, diamonds, and arrows, and manipulate canvas elements in detail, moving beyond simple images [6, 12](https://github.com/tldraw/tldraw/blob/main/apps/docs/content/starter-kits/agent.mdx).
3. **Traffic Control System (State Machine)**: This ensures the system doesn't get tangled up even if the user throws multiple requests at once. By using a FIFO (First-In, First-Out) queue and a state machine, it manages the AI so it can focus on and solve one work session at a time sequentially [8](https://techstackups.com/articles/tldraw-agent-draw/).

Through this process, the AI understands the meaning of voice commands within the canvas area specified by the user, draws shapes in real-time, and immediately reflects the user's intent [2, 3](https://www.youtube.com/watch?v=livloOnVpC8).

### Where are we currently?

Agent Draw is currently built upon the official 'Agent Starter Kit' for developers [2, 5](https://memedata.com/post/130752). Users converse with the agent through the chat panel on the right side of the screen. Here, they can add necessary background information or communicate while checking the history of tasks the agent has performed so far [6, 11](https://zenn.dev/slowhand/articles/bb203aba83e385?locale=en).

The AI is quite adept at performing basic shape combinations and compositions. It's not just about drawing; it can also provide complex task assistance, such as creating to-do lists or instantly updating them when requested [12](https://github.com/tldraw/tldraw/blob/main/apps/docs/content/starter-kits/agent.mdx). Of course, it is currently much more optimized for systematic diagram creation or as a real-time visual aid tool rather than complex artistic creation [9, 11](https://zenn.dev/slowhand/articles/bb203aba83e385?locale=en).

### How will we work in the future?

The emergence of Agent Draw is a small preview of how we will be working with AI in the not-too-distant future. In the future, AI agents will perform deeper reasoning on the canvas, grasp the user's subtle intentions, and develop to a level where they can revise blueprints or suggest ideas on their own.

We will soon have a 'true visual colleague' by our side that not only creates static images but also thinks and draws with us in the physical space of the canvas. The canvas on the screen is no longer just a digital sketchbook; it will become a new venue for collaboration where humans and AI align their thoughts in real-time.

---

### MindTickleBytes AI Reporter's View
There have been many AIs that can draw, but AIs that understand the 'space' of a canvas and build up results while interacting with the user have been rare. The process itself, where AI breathes with our thoughts and completes something together, is changing the very essence of the creative experience.

## References

1. [Show HN: Agent Draw: An agent draws while you talk, built on TLDraw](https://news.ycombinator.com/item?id=48805475)
2. [Agent Draw — Speak, and an AI Agent Draws It Live on Canvas](https://www.youtube.com/watch?v=iIH2hJAxxm8)
3. [Agent Draw: drag a box, speak, an AI agent draws inside it](https://www.youtube.com/watch?v=livloOnVpC8)
4. [Agent Draw: An agent draws while you talk, built on TLDraw](https://vuink.com/post/grpufgnpxhcf-d-dpbz/articles/tldraw-agent-draw)
5. [Show HN：Agent Draw，基于 TLDraw 构建，在你说话时自动绘图。](https://memedata.com/post/130752)
6. [GitHub - tldraw/agent-template: Enable AI agents to interpret ...](https://github.com/tldraw/agent-template)
7. [Better HN - bhn.vercel.app](https://bhn.vercel.app/show)
8. [Agent Draw: An agent draws while you talk, built on TLDraw | Tech Stackups](https://techstackups.com/articles/tldraw-agent-draw/)
9. [Agent starter kit • tldraw Docs](https://tldraw.dev/starter-kits/agent)
10. [Starter kits • tldraw Docs](https://tldraw.dev/starter-kits)
11. [tldraw × AI Agent: Exploring the Mechanics with the Agent Starter Kit](https://zenn.dev/slowhand/articles/bb203aba83e385?locale=en)
12. [tldraw/apps/docs/content/starter-kits/agent.mdx at main · tldraw/tldraw](https://github.com/tldraw/tldraw/blob/main/apps/docs/content/starter-kits/agent.mdx)
13. [Agents on the Canvas With tldraw by Max Drake](https://gitnation.com/contents/agents-on-the-canvas-with-tldraw)
14. [Build a Real-Time tldraw Whiteboard with Velt Comments inside ChatGPT🤯🔥 - DEV Community](https://dev.to/astrodevil/build-a-real-time-tldraw-whiteboard-with-velt-comments-inside-chatgpt-1dhe)
15. [tldraw MCP App: Letting your agents draw](https://tldraw.dev/blog/tldraw-mcp-app)
16. [Show | Hacker News - nhn.yuu.is](https://nhn.yuu.is/show)