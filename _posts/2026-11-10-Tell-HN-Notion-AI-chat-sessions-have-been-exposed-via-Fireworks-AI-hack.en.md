---
layout: post
title: "My work records leaked to AI? Essential security knowledge you must know when using AI tools"
description: "We introduce how to safely use business tools like Notion AI and security guidelines for the era of AI agents."
summary: "We examine how to utilize business AI tool Notion AI and its security features, and explore data management principles to keep in mind when linking external AI services."
tags: [AI Security, Notion AI, Work Efficiency]
image: 2026-11-10-Tell-HN-Notion-AI-chat-sessions-have-been-exposed-via-Fireworks-AI-hack.jpg
image_alt: "An abstract digital image showing the security concept connecting Notion AI and a business dashboard"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "When connecting AI to work tools for convenience, it is essential to build the habit of checking where your data is passing through."
quiz:
  - question: "What is the primary role of Notion AI?"
    choices: ["Work automation and note organization", "Developing malicious code directly", "Creating game programs"]
    answer: 0
    explanation: "Notion AI is a business AI tool that automates tedious tasks, organizes notes, or provides answers to work-related questions."
  - question: "For what purpose is the AI agent HackerAI used?"
    choices: ["Document translation", "Penetration testing (security checks)", "Writing a diary"]
    answer: 1
    explanation: "HackerAI is a penetration testing support tool that helps security professionals investigate vulnerabilities, analyze them, and write reports."
  - question: "What is required to use Fireworks AI, an external LLM (Language Model) service?"
    choices: ["Dedicated hardware", "API key", "Disconnecting from the internet"]
    answer: 1
    explanation: "When linking to external model providers such as Fireworks AI, you must connect to the system using an API key issued by that service."
lang: en
ref: 2026-11-10-Tell-HN-Notion-AI-chat-sessions-have-been-exposed-via-Fireworks-AI-hack
audio: 2026-11-10-Tell-HN-Notion-AI-chat-sessions-have-been-exposed-via-Fireworks-AI-hack.en.mp3
industry: creative
---

Imagine this: On a busy morning, you look at your numerous project notes saved in Notion and ask the AI, "Summarize the meeting content I discussed with my team last week and make a list of tasks I need to do by next week." A moment later, the AI presents a perfectly organized report. This is the vision of an AI-powered smart work environment we all look forward to. However, behind this convenience lies a task we must always take care of: security.

## Why is this important?

We handle countless pieces of business information in our daily lives using business AI tools like Notion [Source 4]. [Notion AI](https://www.notion.com/ko/help/notion-ai-faqs) goes beyond just writing; like a skilled assistant, it automates cumbersome tasks and provides answers to questions based on your work data [Source 2, Source 4].

To properly utilize such powerful features, it is often necessary to link various external AI model services and work tools. For example, tools like [HackerAI](https://hackerai.sh/), which checks for security vulnerabilities, can be linked with Notion to exchange work data and optimize workflows [Source 11]. Understanding whether your precious work records are being safely protected while data moves between various platforms has become an essential skill for the modern professional, not just an option.

## Understanding it simply: The 'Hub' of AI and data

Let's compare the process of using AI tools to a 'library.'

Notion AI is the 'smart librarian' of the library. The librarian knows every book (work record) in the library (your work workspace), so they can find whatever you are looking for quickly [Source 4].

However, sometimes the librarian asks for help from an external expert (external AI language model) for more complex analysis. Model providers like [Fireworks AI](https://opencode.ai/docs/ru/providers/) are those external experts [Source 12]. At this point, a process occurs where data is temporarily passed from the library called Notion to the external expert. Here, the core of security is **'who authorized this conversation (data movement)'** and **'how safely does the expert receiving this data handle it.'**

Tools like [HackerAI](https://hackerai.co/) are experts that check security, so they are connected to systems like Notion in accordance with security protocols and play the role of safely delivering Findings (analysis results) [Source 9, Source 11].

## Current Situation: How far are we connected?

Currently, we are experiencing very high productivity. Notion AI, as a business AI tool, organizes notes, generates study guides, and responds immediately to work-related questions [Source 2, Source 4]. At the same time, AI agents designed for specific purposes, such as [HackerAI](https://hackerai.sh/), allow users to describe the tasks they want and apply them to actual workflows [Source 11].

These tools are securely connected using API keys (keys between systems). For example, the [opencode.ai](https://opencode.ai/docs/ru/providers/) platform is designed to allow users to freely link the LLM model they want by registering API keys for services like Fireworks AI [Source 12].

## What will happen in the future?

AI tools will be more closely connected in the future. However, as convenience grows, the importance of security will grow in proportion.

1. **Strengthening data control**: Control features that allow users to clearly check and block which data is transmitted to external models will increase.
2. **Expansion of the role of security-specialized AI**: AI that helps with penetration testing, such as [HackerAI](https://hackerai.co/), will become more popularized, leading to an era where the vulnerabilities of the tools we use are found and reported in real-time [Source 9].
3. **Caution in connection settings**: From now on, rather than simply chasing convenience, the process of checking how a service handles data when linking a specific AI tool will become a basic step of work.

## AI's Perspective: Thoughts from MindTickleBytes Reporter

The combination of AI and work tools is an unstoppable, massive trend. However, the fact that it is 'convenient' does not mean 'security is perfect.' Please do not forget that every API key and tool connection setting we use today is the first line of defense protecting my work data. Technology must always serve 'me,' and in that process, protecting valuable information is ultimately the user's responsibility.

## References

1. [NotionAITutorial:IsIt Really Worth It? - YouTube](https://www.youtube.com/watch?v=SnbMRRZ2_Ag)
2. [What is Notion AI? Frequently Asked Questions (FAQ) | Notion Help...](https://www.notion.com/ko/help/notion-ai-faqs)
3. [HackerAI - AI-Powered Penetration Testing Assistant](https://hackerai.co/)
4. [HackerAI—AI Assistant for Pentesting & Bug Bounty](https://hackerai.sh/)
5. [Using any LLM provider in opencode.](https://opencode.ai/docs/ru/providers/)