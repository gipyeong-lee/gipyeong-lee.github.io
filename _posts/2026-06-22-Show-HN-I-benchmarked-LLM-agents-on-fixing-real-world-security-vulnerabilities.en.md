---
layout: post
title: "Can AI Directly Fix Security Vulnerabilities? Can We Really Trust It?"
description: "We examine whether AI agents can actually solve software security problems, based on the recently released CVE-Bench results."
summary: "Testing shows AI agents have a maximum 50% success rate in resolving real-world security vulnerabilities, revealing that they are not yet reliable enough for security purposes."
tags: [AI, Security, Artificial Intelligence, Developer, CVE-Bench]
image: 2026-06-22-Show-HN-I-benchmarked-LLM-agents-on-fixing-real-world-security-vulnerabilities.jpg
image_alt: "An image representing an AI agent analyzing and fixing security vulnerability code."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "The era of AI fixing code is here, but humans must still verify whether it fixes it 'properly.' Automated security patches can be efficient, but for now, it is safe to use them only as supplementary tools."
quiz:
  - question: "How does CVE-Bench evaluate the performance of AI agents?"
    choices: ["It simply checks the syntax of the code", "It performs security tests in a sandbox environment", "It receives direct scores from experts"]
    answer: 1
    explanation: "CVE-Bench executes the code modified by AI agents in an actual sandbox environment and verifies if the vulnerability is truly resolved through security testing."
  - question: "What is a dangerous characteristic that appears when AI performs security patches?"
    choices: ["It cannot modify the code at all", "It passes all security tests", "It may pass functional tests but fail to resolve security vulnerabilities"]
    answer: 2
    explanation: "Some AI-generated fixes may pass basic functional tests but fail to resolve the actual security vulnerability, requiring caution."
  - question: "What was the highest success rate confirmed in this test?"
    choices: ["24%", "50%", "80%"]
    answer: 1
    explanation: "According to the latest test results, the best-performing model among several AI agents had a success rate of 50%."
lang: en
ref: 2026-06-22-Show-HN-I-benchmarked-LLM-agents-on-fixing-real-world-security-vulnerabilities
audio: 2026-06-22-Show-HN-I-benchmarked-LLM-agents-on-fixing-real-world-security-vulnerabilities.en.mp3
industry: security
---

Imagine this: You receive a notification that there is a critical hole in the security of an app or website you use. Instead of a human staying up all night analyzing the code, what if an AI diagnosed the problem and proposed a perfect patch in an instant? There would be no scenario more attractive to developers and security professionals. But can we really trust an AI-generated security patch 100%?

The recently released 'CVE-Bench' provides a sharp answer to this provocative question. [[CVE-Bench: Benchmarking LLM-based Software Engineering Agent’s Ability to Repair Real-World CVE Vulnerabilities](https://aclanthology.org/2025.naacl-long.212.pdf)]

## Why is this important?

In software development, security is a non-negotiable bottom line. Countless vulnerabilities are discovered every year, and fixing them promptly is a key task directly linked to corporate survival. If AI agents (AI that understands user goals and performs tasks autonomously) could automate this process, development speed would become unimaginably fast.

However, thinking conversely, the risks are also significant. A flawed fix proposed by an AI might look fine on the surface, but it could result in opening new backdoors for hackers. Therefore, precisely evaluating AI's security repair capabilities is the first step of 'trust verification' that companies must go through to introduce AI into practical work.

## Simply put

Comparing the task of fixing security vulnerabilities is like 'finding and repairing broken pipes in a complex maze.'

While previous AI research was at the level of simply reading code and guessing, "Fixing it here should work," the 'CVE-Bench' introduced this time has gone a step further. This benchmark provides AI with a practice field called a **'sandbox (a safe, virtual space isolated from the outside)'** where it can handle plumbing directly. [[GiovanniGatti/cve-bench: A benchmark for evaluating AIagentson...](https://github.com/GiovanniGatti/cve-bench)]

When the AI completes a patch here, it doesn't just check if the code looks good; it cold-heartedly evaluates whether the pipe actually leaks when put under high pressure through 'security testing.' [[Show HN: I benchmarked LLM agents on fixing real-world ...](https://tolexty.blogspot.com/2026/06/show-hn-i-benchmarked-llm-agents-on.html)] In other words, it is a practical evaluation that checks whether the AI passes the test in the real world, rather than just glancing at its answer sheet.

## How far have we come?

So, what is the AI's report card? The success rate of the AI agent that showed the best performance in the latest test was **50%**. [[Show HN: I benchmarked LLM agents on fixing real-world ...](https://hn-next.vercel.app/s/48409331)]

At first glance, it might not seem bad to solve security problems with a 50% probability. However, experts warn of the 'dangerous traps' hidden in this result. This is because some AI patches passed 'regression tests'—which check whether a system's general functions work well—but **completely failed to resolve the critical security vulnerabilities** in many cases. [[A benchmark for LLM agents fixing real-world security ...](https://roipad.com/saas-metrics/view/hn_48409331/show-hn-i-benchmarked-llm-agents-on-fixing-real-world-security-vulnerabilities)]

This means that while the code may appear to run without any problems on the surface, the hole for hackers to break through may still remain. The test was conducted by having AI agents fix 20 real-world reported vulnerabilities across 18 widely used Python projects. [[Show HN: I benchmarked LLM agents on fixing real-world ...](https://hn-next.vercel.app/s/48409331)]

## What happens next?

AI's security repair capabilities will improve dramatically over time. However, the current results clearly show that there is still a 'trust gap' before AI can take responsibility for critical fields like security on its own.

For the time being, even if AI proposes a fix, the final approval must pass through the eyes of a security expert. Rather than blindly trusting patches suggested by AI, developers must equip themselves with their own 'security testing routines' to verify whether the vulnerability has truly been removed.

## AI's View (MindTickleBytes' AI Reporter View)

AI learns and grows quickly, but the field of security does not allow for a "good enough" level. A 50% success rate is closer to a 'warning' for us than an innovation. A true AI assistant should possess 'humble intelligence' that knows it can be wrong and asks a human for confirmation, rather than just getting the answer right. Because security is a matter of trust.

## References

1. [GiovanniGatti/cve-bench: A benchmark for evaluating AIagentson...](https://github.com/GiovanniGatti/cve-bench)
2. [CVE-Bench: Benchmarking LLM-based Software Engineering Agent’s Ability to Repair Real-World CVE Vulnerabilities - ACL Anthology](https://aclanthology.org/2025.naacl-long.212/)
3. [A benchmark for LLM agents fixing real-world security ...](https://roipad.com/saas-metrics/view/hn_48409331/show-hn-i-benchmarked-llm-agents-on-fixing-real-world-security-vulnerabilities)
4. [Show HN: I benchmarked LLM agents on fixing real-world ...](https://tolexty.blogspot.com/2026/06/show-hn-i-benchmarked-llm-agents-on.html)
5. [Show HN: I benchmarked LLM agents on fixing real-world ...](https://hn-next.vercel.app/s/48409331)