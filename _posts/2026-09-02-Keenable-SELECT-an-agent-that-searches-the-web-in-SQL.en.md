---
layout: post
title: "AI searching the internet with 'SQL'? The story of Keenable SELECT"
description: "Introducing Keenable SELECT, a new search method where AI agents neatly organize complex web data using a single SQL query."
summary: "We explore the Keenable SELECT technology, which goes beyond how AI agents handle complex data from existing search APIs by using the SQL language to extract exactly the information desired."
tags: [AI, Search Engine, SQL, Agent, Technology]
image: 2026-09-02-Keenable-SELECT-an-agent-that-searches-the-web-in-SQL.jpg
image_alt: "Graphic depicting database query language SQL code connecting with web search data"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Search for humans and search for AI must be fundamentally different. Keenable's SQL interface will evolve how agents communicate with the web."
quiz:
  - question: "What is the biggest feature of Keenable SELECT?"
    choices: ["Providing a search engine interface for humans", "Reading and querying web data using SQL", "Real-time rendering of all websites worldwide"]
    answer: 1
    explanation: "Keenable SELECT is designed for agents to search web data using read-only DuckDB SELECT statements via the Model Context Protocol (MCP) server."
  - question: "What is the scale of the web search index held by Keenable?"
    choices: ["Approximately 1 billion documents", "Approximately 50 billion documents", "Over 100 billion documents"]
    answer: 2
    explanation: "Keenable possesses over 100 billion documents through its own crawler and index system."
  - question: "What special search feature does the Keenable API provide?"
    choices: ["A function to query the state of the internet at a specific point in the past", "Automatic generation of personal information encryption", "Unlimited free usage"]
    answer: 0
    explanation: "Keenable supports 'point-in-time record queries,' allowing models to search not only the current state but also the internet as it existed at a specific time in the past."
lang: en
ref: 2026-09-02-Keenable-SELECT-an-agent-that-searches-the-web-in-SQL
audio: 2026-09-02-Keenable-SELECT-an-agent-that-searches-the-web-in-SQL.en.mp3
industry: finance
---

Imagine you told your assistant, "Go summarize the stock prices and related articles for that company from yesterday's news." But the assistant returns and dumps tens of thousands of pages of complex, messy paper, saying, "You find it." You would probably be angry.

This has been the exact situation AI agents have faced when searching the internet. Most search APIs were built to be readable by humans or dumped messy data (JSON or HTML chunks) that the AI had to refine again. However, a technology has recently emerged to solve this inefficiency. It is **Keenable SELECT**.

## Why is it important?

Until now, AI agents (AI that thinks and performs complex tasks on its own) have used search APIs to obtain web information. But since existing search APIs were primarily designed for human users, there was an "extra step" where agents had to clean up data every time they performed complex tasks [Source 13, Source 16].

Keenable SELECT allows you to skip this process. This is because it introduced the **SQL (Structured Query Language, a standard language for querying and managing data)** syntax that we commonly use to handle databases, directly into web search. Thanks to this, developers can command agents to "pick out" exactly the data they need. Agents no longer waste time interpreting unnecessary information and can process complex tasks faster and more accurately.

## Easy to Understand: The Librarian Metaphor

To easily understand Keenable SELECT, let's use the 'librarian' metaphor.

If existing search engines are like telling a librarian, "Find me all the cookbooks," and the librarian piling thousands of cookbooks on the desk and saying, "Find what you need here," Keenable SELECT is different. This technology is like ordering a librarian with specific conditions: **"Please make a list of only Korean recipes published after 2025 that can be made in under 15 minutes."**

Technically, it executes a tool called 'select' within the **Model Context Protocol (MCP, standard communication rules for AI agents)** server [Source 12]. When an agent enters an SQL statement like "SELECT * FROM web WHERE...", Keenable's proprietary system reads the web data, organizes it into a neat row format, and delivers it to the agent [Source 12]. From the agent's perspective, there is no need to struggle to interpret complex web page structures.

## Current Status

Keenable is not just a tool; it is a proprietary infrastructure designed solely for AI agents [Source 8, Source 15]. Its scale is also significant.

- **Vast Knowledge:** Keenable has built a proprietary crawler and index system to turn over 100 billion documents into a database [Source 5, Source 6, Source 8].
- **Fast Speed:** It is optimized so that 95% of requests are processed within 250 milliseconds (0.25 seconds) based on the US East (us-east) region, allowing AI agents to perform tasks in real-time [Source 5].
- **Historical Data Support:** Especially interesting is the 'point-in-time record query' [Source 9]. This allows agents to query not only current internet information but also information that existed on the internet on a specific past date [Source 9].

This service recently succeeded in attracting $26 million (over 30 billion KRW) in funding, proving its technical prowess [Source 4, Source 6, Source 9, Source 16]. Several AI research labs and data providers are already using this API in training and actual service operations [Source 6].

## What will happen in the future?

The emergence of Keenable SELECT shows where search in the 'agent era' is heading. Going forward, it appears that it will become standard for AI to go beyond just commanding "search this" and instead throw sophisticated queries at the web, just like handling a database. The era is approaching where, when a user asks, "Make me a table of eco-friendly company stock prices that rose compared to last month," an AI agent will immediately extract the data from the web using just a few lines of SQL.

## MindTickleBytes AI Reporter Opinion

Search for humans and search for AI must be fundamentally different. Keenable's SQL interface will evolve how agents communicate with the web. AI is now going beyond a being that 'reads' the web to one that 'queries' the web.

## References

1. [Web Search & Extract | Hermes Agent - NOUS RESEARCH](https://hermes-agent.nousresearch.com/docs/user-guide/features/web-search)
2. [SQL Agent | Use Natural Language to Query Databases](https://www.snaplogic.com/ai-agent-showcase/sql-queries)
3. [Examples of Using Select AI Agent](https://docs.oracle.com/en-us/iaas/autonomous-database-serverless/doc/examples-using-select-ai-agent.html)
4. [What is Keenable: The 'AI Agent-Only' Search API Built by Former Yandex Search Leaders, and the Details of Their $26 Million Funding｜アイドリ | AI-Driven Lab](https://note.com/ai_driven/n/n1639bb95690d?hl=en)
5. [Show HN: Keenable – A different web search API for AI agents | Hacker News](https://news.ycombinator.com/item?id=49435555)
6. [Accel-backed Keenable is indexing the web for AI agents | TechCrunch](https://techcrunch.com/2026/08/25/accel-backed-keenable-is-indexing-the-web-for-ai-agents/)
7. [How to Build an AI Agent That Searches the Web: Tools & Setup](https://syllable.ai/blog/how-to-build-ai-agent-with-search-tools)
8. [Keenable.ai — Independent Web Search API for AI](https://keenable.ai/)
9. [Agentic web search infrastructure startup Keenable raises $26M - SiliconANGLE](https://siliconangle.com/2026/08/25/agentic-web-search-infrastructure-startup-keenable-raises-26m/)
10. [hermes-agent/website/docs/user-guide/features/web-search.md at main · NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/web-search.md)
11. [Quickstart - Keenable](https://docs.keenable.ai/)
12. [KeenableSELECT: an agent that searches the web in SQL](https://keenableai.github.io/select-showcase/)
13. [[IndustryNews] Keenable is trying to fix how AI agents actua...](https://promptcube3.com/en/news/7679/)
14. [Keenable: Agent-First Search API Architecture and the 100B Page Index Trade-Off - DEV Community](https://dev.to/mech_app_ai/keenable-agent-first-search-api-architecture-and-the-100b-page-index-trade-off-259b)
15. [Keenable exits stealth mode with $26M seed round to build search...](https://cryptobriefing.com/keenable-26m-seed-ai-search-index/)