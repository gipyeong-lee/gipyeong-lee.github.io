---
layout: post
title: "Are Passwords in My AI App Leaking? A Reconstruction of Cloudflare Workers and 'Spectre' Attacks"
description: "A simple explanation of Cloudflare's recent research findings on 'Spectre' attacks, which are central to cloud service security."
summary: "Cloudflare discovered and resolved potential vulnerabilities to 'Spectre' attacks during internal security audits. No customer data was leaked, and more robust security technologies have been implemented."
tags: [CloudSecurity, Spectre, Cloudflare, AISecurity]
image: 2026-08-20-A-revisit-of-remote-Spectre-attacks-on-Cloudflare-Workers.jpg
image_alt: "Abstract network connectivity and security padlock image representing cloud computing security"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Since perfect security does not exist, Cloudflare's attitude of constantly testing itself is impressive. We must keep in mind that attack techniques are evolving alongside technological progress."
quiz:
  - question: "What did Cloudflare discover in this research?"
    choices: ["Large-scale leak of actual customer data", "Limitations of existing security defense techniques", "Hardware that cannot defend against Spectre attacks"]
    answer: 1
    explanation: "Cloudflare discovered potential limitations in its own security defense system, DyPrIs (Dynamic Process Isolation), and supplemented them."
  - question: "How much faster is the attack studied this time compared to the 2021 case?"
    choices: ["About 2x", "About 50x", "About 360x"]
    answer: 2
    explanation: "The researchers confirmed that data could be stolen at a speed of 12 bits per second, which is 360 times faster than the 2021 demo attack."
  - question: "How did Cloudflare resolve this vulnerability?"
    choices: ["Replacing the entire server", "Improving DyPrIs and integrating V8 sandboxing", "Completely blocking internet connections"]
    answer: 1
    explanation: "Cloudflare improved DyPrIs and strengthened security by applying V8 sandbox integration and Memory Protection Key (MPK)-based isolation technology."
lang: en
ref: 2026-08-20-A-revisit-of-remote-Spectre-attacks-on-Cloudflare-Workers
audio: 2026-08-20-A-revisit-of-remote-Spectre-attacks-on-Cloudflare-Workers.en.mp3
industry: security
---

Imagine this: the smartphone apps or AI services we use every day are actually running in a factory called the "Cloud" (a massive data center on the internet). When we command, "AI, summarize this," numerous servers inside that factory process the information. But what happens if a gap appears in the security system of this factory? This is exactly why "Cloudflare" recently overhauled the security of their infrastructure, "Cloudflare Workers."

### Why is this important?

We transmit a massive amount of information to internet services every day. Login details or personal messages might even briefly pass through the memory of cloud servers. If a hacker pierces the server's security and secretly spies on this data in transit, our precious personal information is at risk. Cloudflare is a core infrastructure used by countless companies worldwide. Therefore, this research is not just a technical experiment, but a significant issue directly linked to all of our digital safety. [Source 7](https://news.shield53.com/spectre-returns-cloudflare-workers-isolation-bypass-exposes-multi-tenant-cloud-risk/)

### Easy Understanding: What is a 'Spectre' Attack?

The protagonist of this research is an attack technique called "Spectre." Simply put, Spectre is an attack that digs into the gaps in the design structure of computer processors (the brain of a computer), which have existed for about 20 years. [Source 8](https://www.zdnet.com/article/new-spectre-attack-can-remotely-steal-secrets-researchers-say/)

To use a metaphor, it is like a situation in a library where a librarian is so busy that they place books the patron wants on the desk in advance. However, it turns out that the book was a "confidential document" the patron did not have the authority to borrow. The principle of a Spectre attack is to exploit the processor's habit of loading data in advance (Speculative Execution) before the librarian (the processor) verifies the patron's borrowing authority, allowing the attacker to peek at confidential information. [Source 12](https://www.youtube.com/watch?v=q3-xCvzBjGs)

In the past, this attack was only possible if a hacker could plant malicious code directly on the server, but this research demonstrated that this attack is now possible remotely via internet networks. [Source 13](https://arstechnica.com/gadgets/2018/07/new-spectre-attack-enables-secrets-to-be-leaked-over-a-network/)

### Current Situation: What was discovered?

Cloudflare audited its own infrastructure from 2024 to 2025. [Source 1](https://blog.cloudflare.com/revisiting-spectre-attacks-on-workers/) As a result, they discovered that there were limitations in their security mechanism called "Dynamic Process Isolation (DyPrIs)." Researchers used this vulnerability to prove that they could steal data belonging to others using the same server at a speed of 12 bits per second with 99% accuracy. [Source 4](https://appworkstechnologies.in/blog/revisiting-remote-spectre-attacks-on-cloudflare-workers-new-findings-and-hardened-defenses)

This speed is a staggering 360 times faster than a similar attack tested in 2021. [Source 5](https://thehackernews.com/2026/08/cloudflare-workers-spectre-attack-leaks.html) Fortunately, however, there is no evidence that actual customer data was leaked, and this research was an experiment conducted solely to strengthen security in an environment they control. [Source 14](https://thehackernews.com/search?m=1)

### What happens next?

Cloudflare immediately resolved the discovered vulnerability. They improved the DyPrIs feature, integrated the "V8 sandbox," the core engine of Google Chrome, more deeply, and introduced a powerful isolation technology using Memory Protection Keys (MPK). [Source 14](https://thehackernews.com/search?m=1)

Cloud security in the future will evolve beyond simply locking doors toward monitoring in real-time whether the act of attempting to access data is suspicious or not. As demonstrated by this case, when efforts to admit the limitations of technology and build stronger walls continue, the digital world we use can become even safer.

### AI Reporter's Perspective

Behind the "advancement" of technology, there is always the shadow of the "evolution of attacks." This research reminds us once again that the core of security is not just how safe our service is, but how honest we are about how dangerous it could potentially be. There is no perfect shield, but the effort to try and pierce one's own defenses becomes the best shield.

## References

1. [A revisit of remote Spectre attacks on Cloudflare Workers](https://blog.cloudflare.com/revisiting-spectre-attacks-on-workers/)
2. [A revisit of remote Spectre attacks on Cloudflare Workers (LinkedIn)](https://www.linkedin.com/posts/cloudflare_a-revisit-of-remote-spectre-attacks-on-cloudflare-activity-7495900392061460480-aFBw)
3. [A revisit of remote Spectre attacks on Cloudflare Workers (Note)](https://note.f5.pm/go-436222.html)
4. [Revisiting Remote Spectre Attacks on Cloudflare Workers: New Findings and Hardened Defenses](https://appworkstechnologies.in/blog/revisiting-remote-spectre-attacks-on-cloudflare-workers-new-findings-and-hardened-defenses)
5. [Cloudflare Workers Spectre Attack Leaks JWT From Co-Located Worker](https://thehackernews.com/2026/08/cloudflare-workers-spectre-attack-leaks.html)
6. [A revisit of remote Spectre attacks on Cloudflare Workers (Hacker News)](https://news.ycombinator.com/item?id=49364721)
7. [Spectre Returns: Cloudflare Workers Isolation Bypass Exposes Multi-Tenant Cloud Risk](https://news.shield53.com/spectre-returns-cloudflare-workers-isolation-bypass-exposes-multi-tenant-cloud-risk/)
8. [New Spectre attack can remotely steal secrets, researchers say | ZDNET](https://www.zdnet.com/article/new-spectre-attack-can-remotely-steal-secrets-researchers-say/)
9. [Dynamic Process Isolation: Research by Cloudflare and TU Graz](https://www.engineering.fyi/article/dynamic-process-isolation-research-by-cloudflare-and-tu-graz)
10. [NetSpectre — New Remote Spectre Attack Steals Data Over the Network](https://thehackernews.com/2018/07/netspectre-remote-spectre-attack.html)
11. [GitHub - flxwu/spectre-attack-demo](https://github.com/flxwu/spectre-attack-demo)
12. [Spectre attack explained like you're five - YouTube](https://www.youtube.com/watch?v=q3-xCvzBjGs)
13. [New Spectre attack enables secrets to be leaked over a network | Ars Technica](https://arstechnica.com/gadgets/2018/07/new-spectre-attack-enables-secrets-to-be-leaked-over-a-network/)
14. [The Hacker News | #1 Trusted Source for Cybersecurity News — Index Page](https://thehackernews.com/search?m=1)
15. [Security model · Cloudflare Workers docs](https://developers.cloudflare.com/workers/reference/security-model/)
16. [Mitigating Spectre and Other Security Threats: The Cloudflare Workers Security Model](https://blog.cloudflare.com/mitigating-spectre-and-other-security-threats-the-cloudflare-workers-security-model/)