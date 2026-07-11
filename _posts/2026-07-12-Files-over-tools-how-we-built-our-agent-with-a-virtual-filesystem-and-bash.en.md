---
layout: post
title: "What happened when we gave AI a 'computer' instead of 'tools'"
description: "An explanation of a new paradigm where AI agents perform tasks autonomously using file systems and bash commands instead of complex, purpose-built tools."
summary: "The 'Files over tools' design pattern is gaining attention, which shifts from building new, dedicated tools for every task to providing AI agents with a virtual file system and bash commands to manipulate data themselves."
tags: [AI, Agents, Development, Tech Trends]
image: 2026-07-12-Files-over-tools-how-we-built-our-agent-with-a-virtual-filesystem-and-bash.jpg
image_alt: "An image representing an AI writing code and navigating files in a virtual file system environment."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Rather than building complex, isolated tools, allowing AI to think within the computing environments it is already familiar with—files and commands—is a significantly more scalable and flexible approach."
quiz:
  - question: "What is the new paradigm in AI agent design that is currently preferred over tool-centric approaches?"
    choices: ["Web browser automation", "Virtual file system and bash environment", "Manual user input"]
    answer: 1
    explanation: "Recently, providing AI with file systems and bash commands to explore and manipulate data autonomously has been recognized for its efficiency compared to building numerous dedicated tools."
  - question: "What is a major advantage of agents that utilize virtual file systems?"
    choices: ["All files can be stored on the physical hard drive.", "They can handle diverse tasks without the need to develop new tools every time.", "They always require an internet connection."]
    answer: 1
    explanation: "Agents with bash access can flexibly perform tasks like file exploration and text processing without needing dedicated tool development."
  - question: "Where can data from virtual file systems actually be stored?"
    choices: ["It must be stored on a cloud server.", "It can be backed up in databases like SQLite instead of physical disk files.", "It disappears every time it is executed."]
    answer: 1
    explanation: "Some virtual file systems use databases like SQLite as backup storage rather than physical files, allowing for efficient operation."
lang: en
ref: 2026-07-12-Files-over-tools-how-we-built-our-agent-with-a-virtual-filesystem-and-bash
audio: 2026-07-12-Files-over-tools-how-we-built-our-agent-with-a-virtual-filesystem-and-bash.en.mp3
industry: creative
---

Imagine you asked a chef to "make a delicious kimchi stew." However, every time this chef wanted to chop an onion, they had to build a custom "onion-chopping knife," and every time they needed a ladle, they had to run a "ladle-making machine." You would likely be exhausted before the meal was even served. The time spent preparing tools would far exceed the time spent cooking.

Surprisingly, this is exactly the inefficient method we have been using to build AI Agents (AI that autonomously sets goals and performs complex tasks). For every task the AI could perform, we were painstakingly building and attaching a "dedicated tool." However, a new trend is emerging among developers: "Stop building new tools and just give the AI a computer environment." This design approach is called "Files over tools."

## Why is this important?

Until now, every time an AI agent needed a new function, developers had to design complex software tools and integrate them with the AI. This was not only time-consuming and costly, but it was also a primary reason for the AI's lack of flexibility. If a situation occurred outside the scope of its defined tools, the AI was rendered helpless.

However, things change completely when you give an AI access to a virtual file system and a bash environment (the command-based work environment used in Linux). The agent can autonomously find files, read their contents, modify them, and combine commands to solve problems, just as a human developer would while working at a computer. This not only boosts the productivity of AI agents exponentially, but it also allows the AI to deal with new environments flexibly without developers having to anticipate every possible scenario and build tools for them.

## A simple analogy

To put it simply, if the old method was giving an AI hundreds of "dedicated machines that perform a specific action when you press a single button," the new method is like lending the AI a "computer with an operating system installed."

For example, suppose an agent needs to manage customer information. In the past, you would have had to develop a "customer lookup tool" and a "customer info modification tool" individually. Now, you show the agent a virtual folder containing customer data and have it use bash commands (e.g., finding data with `grep`, modifying content with `echo`). [Reference 2](https://www.linkedin.com/posts/knocklabs_how-do-you-build-an-ai-agent-that-safely-activity-7481434587642957843-qCEi) By doing this, the AI explores files, grasps the context autonomously, and completes the task like a real computer user. [Reference 14](https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools)

Furthermore, this file system can operate without occupying a physical hard disk. Some virtual file systems utilize SQLite (a lightweight, fast database program) to safely store and manage data. [Reference 19](https://github.com/maxi-moss/agent-filesystem) While it may look to us like browsing folders on a computer, it is actually handling information much more efficiently within a database.

## How far has this technology come?

Many companies and projects are already adopting this method. A company called "Knock" processes customer messaging resources by combining a bash environment, a virtual file system, and management APIs into their AI agent architecture. [Reference 1](https://knock.app/blog/how-we-built-the-knock-agent-virtual-filesystem-and-bash) [Reference 3](https://fooqux.com/article/6457)

Additionally, projects like "AgentFS" provide file systems exclusively for AI agents. This helps AI safely use command-line tools (CLI Tools) while enabling the auditing of all work history. [Reference 15](https://github.com/tursodatabase/agentfs) [Reference 16](https://www.agentfs.ai/) Beyond just reducing tools, keeping a record of what the AI has done to ensure safety is at the core of current technology.

## What will the future look like?

The development direction of AI agents is increasingly moving toward "becoming more like humans." The era where developers have to design new tools every time is coming to an end, and an era where AI works like a skilled assistant using a computer environment on its own is approaching.

In the future, data that agents need to process will be systematically organized in file formats, and agents will be able to manipulate them deftly using Linux commands. The work you will likely need to do is not building tools, but building a well-organized "digital environment" where the AI can work. It is time to lend them an "environment," not tools.

## MindTickleBytes' AI Reporter Perspective
The shift from the era of tools to the era of environments signifies that AI technology is evolving beyond a simple calculator into a true "digital worker." Designs that minimize developer effort and maximize AI autonomy will define the agent ecosystem of the future.

## References

1. [Files over tools: how we built the Knock Agent using a virtual filesystem and bash](https://knock.app/blog/how-we-built-the-knock-agent-virtual-filesystem-and-bash)
2. [How do you build an AI agent that can safely manage customer messaging resources?](https://www.linkedin.com/posts/knocklabs_how-do-you-build-an-ai-agent-that-safely-activity-7481434587642957843-qCEi)
3. [Files over tools: how we built the Knock Agent using a virtual filesystem and bash](https://fooqux.com/article/6457)
4. [Files over tools: how we built our agent with a virtual filesystem and bash](https://news.ycombinator.com/item?id=48845364)
5. [How to build agents with filesystems and bash - Vercel](https://vercel.com/blog/how-to-build-agents-with-filesystems-and-bash)
6. [Knock builds AI agent with virtual filesystem and bash](https://savedelete.com/news/knock-agent-virtual-filesystem/)
7. [Building a Filesystem + Bash Based Agentic Memory System (Part 1)](https://justinbarias.io/blog/agentic-memory-filesystem-part-1/)
14. [We removed 80% of our agent’s tools - Vercel](https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools)
15. [GitHub - tursodatabase/agentfs: The filesystem for agents.](https://github.com/tursodatabase/agentfs)
16. [AgentFS - Filesystem Isolation for AI Agents](https://www.agentfs.ai/)
18. [Building AI agents with just bash and a filesystem in TypeScript](https://turso.tech/blog/agentfs-just-bash)
19. [GitHub - maxi-moss/agent-filesystem: A virtual filesystem for agents.](https://github.com/maxi-moss/agent-filesystem)