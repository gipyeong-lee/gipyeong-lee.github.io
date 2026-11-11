---
layout: post
title: "AI finding software 'holes'? The story of Anthropic's security tracker"
description: "Learn about Anthropic's security program, where AI independently discovers and manages software security vulnerabilities, and its impact."
summary: "Anthropic operates a systematic security program that leverages its AI models to automatically identify security vulnerabilities in software worldwide and notifies developers to encourage patching."
tags: [AI, Security, Anthropic, Software, Technology]
image: 2026-11-11-Tracking-Anthropic-discovered-vulnerabilities.jpg
image_alt: "A digital graphic image representing computer code and security appears on the screen."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "While it is positive for AI to act as a defender and find vulnerabilities first, the fact that the discovery speed is far outpacing the patching speed is a new challenge we must solve."
quiz:
  - question: "What is the first thing Anthropic does after discovering a security vulnerability?"
    choices: ["Publicly disclose the vulnerability on the internet", "Privately notify the software maintainer", "Immediately write exploit code"]
    answer: 1
    explanation: "Anthropic follows a 'Coordinated Vulnerability Disclosure (CVD)' policy, privately delivering discovered vulnerabilities to software maintainers to provide time for patches before public disclosure."
  - question: "As of October 2026, how many of the vulnerabilities discovered by Anthropic have been publicly disclosed?"
    choices: ["6,157", "29,439", "516"]
    answer: 0
    explanation: "According to Anthropic's dashboard, out of 29,439 candidates, 6,157 vulnerabilities were disclosed, and 516 of them were patched in top-tier projects."
  - question: "What is a realistic challenge currently faced by Anthropic's security program?"
    choices: ["AI cannot find any vulnerabilities", "The actual patching speed is slow compared to the rate at which vulnerabilities are found", "All vulnerabilities are being exploited immediately"]
    answer: 1
    explanation: "The patch rate for discovered vulnerabilities is approximately 8.4%, meaning the speed at which developers actually patch them lags behind the volume of vulnerabilities found by AI."
lang: en
ref: 2026-11-11-Tracking-Anthropic-discovered-vulnerabilities
audio: 2026-11-11-Tracking-Anthropic-discovered-vulnerabilities.en.mp3
industry: security
---

Imagine a "security detective" living inside your smartphone or web browser. This detective never sleeps; it monitors every corner of your software around the clock, searching for tiny "holes" (vulnerabilities) that hackers could use to break in.

Recently, the AI company Anthropic has gained attention for running a security program that does exactly this. AI is moving beyond simply writing text or generating images—it is now standing on the front lines, protecting the software we use every day.

### Why is this important?

We live our lives relying on countless pieces of software. We shop using browsers and handle work through operating systems. What happens if these programs have security holes? Hackers can use those cracks to steal personal information or paralyze entire systems.

Until now, finding these vulnerabilities was the job of human security experts. However, software is so vast and complex that it was impossible for humans to find every single flaw. Anthropic’s approach is changing the game. By using AI to find vulnerabilities faster and more efficiently, they are attempting to build defenses before malicious actors can take advantage of them. This is directly linked to protecting personal information and enhancing the security of the entire digital ecosystem we trust [[Source 2](https://www.anthropic.com/research/discovering-vulnerabilities-with-claude)].

### Simple explanation: How the 'security detective' AI works

Anthropic uses its AI model, 'Claude,' and internal research models to analyze open-source and closed-source software worldwide [[Source 2](https://www.anthropic.com/research/discovering-vulnerabilities-with-claude), [Source 6](https://red.anthropic.com/2026/cvd/about/)].

To put it simply, if traditional security auditing was like a human walking around a building with a magnifying glass to find cracks, Anthropic's AI is like having a perfect knowledge of the building's blueprints and using thousands of cameras to spot structural flaws in an instant.

Notably, a model called 'Claude Mythos' has the ability not only to discover vulnerabilities on its own but also to create exploit code to demonstrate how they could be used [[Source 7](https://www.sherlockforensics.com/blog/claude-mythos-security-analysis-2026.html), [Source 8](https://www.dynatrace.com/news/blog/how-anthropic-claude-mythos-is-reshaping-the-vulnerability-landscape/)]. This is similar to a doctor not just diagnosing a disease, but simulating how a pathogen enters the body to create the perfect vaccine.

### The current situation: Thousands of holes, but slow patches

So, how many holes have been found so far? As of October 2, 2026, according to Anthropic’s dashboard, they have reviewed about 29,439 vulnerability candidates, and 6,157 of those have been officially disclosed [[Source 5](https://vulnerabilities.ai/ledger)].

However, there is an interesting yet worrying aspect here: the rate at which developers have actually completed patches (fixes) for these vulnerabilities is only about 8.4% (516 cases) [[Source 5](https://vulnerabilities.ai/ledger)]. While AI is identifying problems at a terrifying speed, human beings are struggling to keep up with the pace of fixing them.

Furthermore, despite the large number of vulnerabilities being discovered, fortunately, fewer than 0.5% have been exploited by real hackers [[Source 16](https://www.theregister.com/security/2026/09/21/anthropic-linked-cves-pile-up-attackers-mostly-shrug/5298018)]. Nevertheless, since cases have already been reported where AI has been used to autonomously find vulnerabilities and carry out attacks without human intervention, it is a situation that requires constant vigilance [[Source 19](https://www-cdn.anthropic.com/d7dd50dd1185f59be051b307150d877f2b82bd2c.pdf)].

### What happens next?

Anthropic does not immediately flood the internet with the vulnerabilities it discovers. Instead, it follows a 'Coordinated Vulnerability Disclosure (CVD)' policy, notifying the software's maintainers privately and giving them time to apply fixes [[Source 6](https://red.anthropic.com/2026/cvd/about/)].

As the number of vulnerabilities found by AI will likely increase exponentially in the future, changes are needed in the software development environment. It is highly probable that we will move from a system where humans manually fix problems found by AI to an 'automated defense system' where AI finds issues and automatically generates and applies patches.

We are now living in an era where we no longer just fear that AI might attack our computers, but rather an age where we are using AI to build a safer software environment. We need to keep a close eye on Anthropic's dashboard to see what technological advancements will make our digital daily lives safer.

---
**MindTickleBytes' AI reporter perspective:**
Technology always brings light and shadow simultaneously. It is a major breakthrough for Anthropic's AI to act as a guardian of security, but the current situation where the speed of finding vulnerabilities far outpaces the speed of patching is demanding an unprecedented level of urgency from the software industry. Security is no longer just an art practiced by humans; it has become an endless marathon that AI and humans must run together.

## References

1. [Tracking Anthropic-discovered vulnerabilities](https://www.vulncheck.com/blog/anthropic-glasswing-november-update)
2. [Discovering and exploiting vulnerabilities in critical, real ...](https://www.anthropic.com/research/discovering-vulnerabilities-with-claude)
3. [Anthropic's coordinated vulnerability disclosure dashboard](https://red.anthropic.com/2026/cvd/)
4. [Coordinated vulnerability disclosure for Claude-discovered ...](https://www.anthropic.com/coordinated-vulnerability-disclosure)
5. [Ledger — Tracking the AI Vulnerability-Discovery Programs](https://vulnerabilities.ai/ledger)
6. [About this dashboard - red.anthropic.com](https://red.anthropic.com/2026/cvd/about/)
7. [Claude Mythos Security Vulnerabilities: What We Know in 2026](https://www.sherlockforensics.com/blog/claude-mythos-security-analysis-2026.html)
8. [How Anthropic Claude Mythos is reshaping the vulnerability ...](https://www.dynatrace.com/news/blog/how-anthropic-claude-mythos-is-reshaping-the-vulnerability-landscape/)
9. [Research \Anthropic](https://www.anthropic.com/research)
10. [A Cheeky Pint withAnthropicCEO Dario Amodei - YouTube](https://www.youtube.com/watch?v=GcqQ1ebBqkc)
11. [Secret Claudetrackershocks users afterAnthropic’s anti-surveillance...](https://arstechnica.com/tech-policy/2026/07/anthropic-outed-for-claude-tracker-that-secretly-monitored-chinese-users/)
13. [AnthropicStatus. Check ifAnthropicis down or having... | StatusGator](https://statusgator.com/services/anthropic)
16. [Anthropic-linked CVEs pile up, attackers mostly shrug](https://www.theregister.com/security/2026/09/21/anthropic-linked-cves-pile-up-attackers-mostly-shrug/5298018)
19. [Full report: Disrupting the first reported AI-orchestrated ...](https://www-cdn.anthropic.com/d7dd50dd1185f59be051b307150d877f2b82bd2c.pdf)