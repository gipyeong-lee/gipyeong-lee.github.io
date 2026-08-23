---
layout: post
title: "Completed my first Dapp."
description: "Hello? This is Slow Thinking. I've been developing for about a month. I wouldn't have been able to build this without AI. Here is the method I, a lazy person, chose: I set up Codex and Claude Code in the left and right panels of Visual Studio Code, respectively. When I hit the token limit, I switched between them. Below is a comparison table of the two tools for your reference."
date: 2025-10-18 20:57:34 +0900
section: blog
category: web3
lang: en
ref: 2025-10-18-legacy-391-web3-dapp
tags:
  - "Ai"
  - "Claude"
  - "Codex"
  - "DAPP"
  - "Project"
  - "Projects"
translation_source_hash: 80e0e93d306232af16e6f6d408598d3b9b8be3d0a9bae18b179452ac9bae1aa4
---

<p>
Hello? This is Slow Thinking.
</p>
<p>
I have been working on development for about a month.
</p>
<p>
I wouldn't have been able to develop this without AI.
</p>
<p>
Here is the method chosen by a lazy person like me.
</p>

<p>
I set up Codex and Claude Code in the left and right panels of Visual Studio Code, respectively.
</p>
<p>
When I hit the token limit, I alternated between them. The table below compares the two tools. Please refer to it.
</p>

<table>
<tbody>
<tr>
<td>
<b>
Item
</b>
</td>
<td>
<b>
Codex CLI ( OpenAI )
</b>
</td>
<td>
<b>
Claude Code CLI (Anthropic)
</b>
</td>
</tr>
<tr>
<td>
<b>
Plan Name
</b>
</td>
<td>
Included in ChatGPT Plus ($20/month)
</td>
<td>
Claude Pro ($20/month)
</td>
</tr>
<tr>
<td>
<b>
Session Limit Method
</b>
</td>
<td>
Approx.
<b>
5-hour rolling window
</b>
(Resets every 5 hours)
</td>
<td>
Approx.
<b>
5-hour rolling window
</b>
(Resets every 5 hours)
</td>
</tr>
<tr>
<td>
<b>
Session Limit (Approx.)
</b>
</td>
<td>
30 ~ 150 local messages or 5 ~ 40 cloud operations
</td>
<td>
Approx. 45 messages or 10 ~ 40 prompt-level operations
</td>
</tr>
<tr>
<td>
<b>
Weekly Rolling Limit
</b>
</td>
<td>
Shared
<b>
weekly quota
</b>
exists (official figures not disclosed)
</td>
<td>
Weekly limit exists, resets approximately every
<b>
7 days
</b>
</td>
</tr>
<tr>
<td>
<b>
Reset Timing (Session)
</b>
</td>
<td>
Auto-resets 5 hours after the first request
</td>
<td>
Auto-resets 5 hours after the first prompt
</td>
</tr>
<tr>
<td>
<b>
Reset Timing (Weekly)
</b>
</td>
<td>
Resets approximately every
<b>
week
</b>
(exact time not disclosed)
</td>
<td>
Resets after approximately
<b>
7 days
</b>
(varies by account)
</td>
</tr>
<tr>
<td>
<b>
Token Context Window
</b>
</td>
<td>
Approx.
<b>
192,000 tokens
</b>
(estimated sum of input + output + history)
</td>
<td>
Approx.
<b>
200,000 tokens
</b>
(Pro base), up to 500,000 (Enterprise)
</td>
</tr>
<tr>
<td>
<b>
Base Model
</b>
</td>
<td>
GPT-4 Turbo (Code interpretation mode)
</td>
<td>
Claude 3 Sonnet (Coding mode)
</td>
</tr>
<tr>
<td>
<b>
Message When Exceeded
</b>
</td>
<td>
“Usage limit reached. Try again in X hours.”
</td>
<td>
“You’ve hit your limit. Resets in ~X hours.”
</td>
</tr>
<tr>
<td>
<b>
Reset Method
</b>
</td>
<td>
Automatic rolling reset (no manual reset available)
</td>
<td>
Automatic rolling reset (session renews after 5 hours)
</td>
</tr>
<tr>
<td>
<b>
Additional Features
</b>
</td>
<td>
- Distinguishes local vs. cloud operations<br>- Includes code execution capability
</td>
<td>
- Supports context reduction with /clear and /compact commands<br>- Centralized support for Sonnet 3.5/4 models
</td>
</tr>
<tr>
<td>
<b>
Official Source Examples
</b>
</td>
<td>
<a href="https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan">
help.openai.com
</a>
</td>
<td>
<a href="https://claudelog.com/faqs/claude-code-usage/">
claudelog.com
</a>
/
<a href="https://portkey.ai/blog/claude-code-limits/">
portkey.ai
</a>
</td>
</tr>
</tbody>
</table>

<p>
The following is information regarding this Project L.
</p>


<table>
<tbody>
<tr>
<td>
<b>
Project Name
</b>
</td>
<td>
Project L
</td>
</tr>
<tr>
<td>
<b>
Development Language
</b>
</td>
<td>
Rust (On-chain program) + TypeScript (Client / Frontend)
</td>
</tr>
<tr>
<td>
<b>
Platform
</b>
</td>
<td>
Solana Blockchain (Anchor Framework)
</td>
</tr>
<tr>
<td>
<b>
Development Period
</b>
</td>
<td>
2025.09.29 ~ 2025.10.18 (Total 19 days, 38 hours)
</td>
</tr>
<tr>
<td>
<b>
Main Goal
</b>
</td>
<td>
Deploy smart contract on Solana network and complete client integration
</td>
</tr>
<tr>
<td>
<b>
Dependency Graph
</b>
</td>
<td>
Total 2,130 dependencies (including packages, modules, and build dependencies)
</td>
</tr>
</tbody>
</table>

<p>
Development is complete, and I am currently performing self-QA.
</p>
<p>
I plan to proceed with the release afterward.
</p>

<hr>

<blockquote>
<s>
devnet QA - Completed
</s>
<br>
testnet QA -
<b>
On going
</b>
<br>
Deploy on mainnet - To do
</blockquote>