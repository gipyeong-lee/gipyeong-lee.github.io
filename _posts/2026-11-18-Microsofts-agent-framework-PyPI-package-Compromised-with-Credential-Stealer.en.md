---
layout: post
title: "Microsoft's Official AI Package Compromised by Secret Spy Incident: What Happened?"
description: "A clear overview of the supply chain attack where Microsoft's official Python package 'agent-framework' was compromised to steal user credentials, along with response methods."
summary: "On November 17, 2026, malicious code acting as a secret spy was embedded in Microsoft's official Python package 'agent-framework'. We review the nature of this download-and-execute attack and essential security knowledge."
tags: [Security, Python, SupplyChainAttack, Microsoft, AI]
image: 2026-11-18-Microsofts-agent-framework-PyPI-package-Compromised-with-Credential-Stealer.jpg
image_alt: "An illustration featuring a padlock symbolizing digital security alongside a Python code screen"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Though it may seem like a story just for developers, this is an important incident showing how easily the trust of modern digital services can be shaken. A transparent and thorough supply chain verification system is more urgent than ever."
quiz:
  - question: "What is the name of Microsoft's Python package targeted in this attack?"
    choices: ["agent-framework", "azure-sdk", "microsoft-ai-tools"]
    answer: 0
    explanation: "Microsoft's official Python metapackage 'agent-framework' was targeted."
  - question: "Did the user have to directly import the package in code for the malicious code to execute?"
    choices: ["Yes, it only executed when explicitly imported in code.", "No, it executed automatically when Python started or upon installation.", "It only ran when opening the smartphone app."]
    answer: 1
    explanation: "Using a `.pth` startup hook, it executed automatically when Python ran or installed without requiring an explicit import."
  - question: "What immediate response action do experts recommend following this incident?"
    choices: ["Format and reinstall the computer", "Pin version to 1.26.0 and rotate major passwords and secrets", "Delete Microsoft account"]
    answer: 1
    explanation: "It was recommended to pin the version to the safe 1.26.0 release and rotate secrets such as Azure and GitHub Actions credentials."
lang: en
ref: 2026-11-18-Microsofts-agent-framework-PyPI-package-Compromised-with-Credential-Stealer
audio: 2026-11-18-Microsofts-agent-framework-PyPI-package-Compromised-with-Credential-Stealer.en.mp3
industry: creative
---

Imagine receiving a cooking ingredient kit from a famous major corporation that you usually trust and use. What if you simply opened the box and placed it on the dining table, only to discover that a memo containing your home safe key and front door password was secretly transmitted to someone else—even though you haven't started cooking or even unpacked the ingredients?

A strikingly similar event actually occurred in the software development world. Someone secretly planted an "information thief" inside the official toolset provided by global tech giant Microsoft [Source 18]. Let's break down the details of this security incident that shocked developers worldwide in a very easy-to-understand way.

---

## Why Is This Important?

Just as we download apps verified for safety from the Apple App Store or Google Play Store when using our smartphones, programmers also build programs by pulling in countless open-source tools. In this case, malicious code was hidden inside **'agent-framework'**, an official Microsoft package registered on the Python Package Index (PyPI), the official software repository for the Python programming language used by developers [Source 3, Source 18].

To put it in perspective, it is as if someone mixed impurities into the core food distribution network jointly used by catering chains worldwide. This package is widely used across global development environments, being downloaded nearly 200,000 times every month [Source 3]. The moment a version containing malicious code is installed on a company's or developer's computer or automated server (CI/CD environment, continuous integration and deployment environment) using this tool, a nerve-wracking situation unfolds where sensitive information like cloud service access credentials and secret keys can be entirely stolen [Source 17, Source 18]. Beyond a developer's simple personal mistake, this was a major supply chain security accident that threatened the digital safety of numerous end-users relying on the services they built.

---

## Understanding Made Easy: A Micro-Spy Hiding in the Delivery Box

A software supply chain attack is like intercepting a delivery vehicle from a trusted major distributor and secretly slipping a meticulously disguised wiretapping device inside an authentic box.

Put simply, the operation mechanism of this incident can be broken down into everyday analogies:
1. **The Trap of Trust**: Developers downloaded the necessary tools as usual (`pip install` command), trusting the brand reliability of Microsoft and its official repository [Source 18].
2. **Invisible Infiltration**: Normally, malicious code operates when a program is directly executed or a specific function is invoked. However, this malicious code utilized a Python startup hook called a `.pth` file (a technology that automatically runs code when a program starts) [Source 7, Source 18]. This was like an ultra-miniature wiretap that operates automatically just by bringing the delivery box into a room without even opening it, meaning the malicious code executed automatically in the Python environment simply by installing the package, even if the developer never imported or explicitly called it in their code [Source 18].
3. **Secret Information Leakage**: The spy program, awakened stealthily in this manner, rapidly scraped passwords stored in computer environment variables or critical configuration files, along with cloud control permissions (such as Azure DevOps, Azure managed identity, and GitHub Actions secrets), transmitting them instantly to an attacker's external server via a webhook [Source 7, Source 17, Source 18].

---

## Current Situation and Incident Details

According to the security industry and foreign media reports, this meticulous supply chain compromise occurred on November 17, 2026 [Source 3].

- **Time of Occurrence and Versions**: Microsoft's official metapackage `agent-framework` versions **1.26.1** and **1.26.2** were registered sequentially on PyPI with just a 33-minute interval [Source 3, Source 16, Source 18]. Hidden inside both versions was a credential stealer designed to stealthily intercept user authentication credentials [Source 3].
- **Swift Response**: Fortunately, thanks to rapid detection by global security experts and automated monitoring systems, the two malicious files were urgently quarantined and removed by Microsoft and repository administrators just 45 minutes after appearing [Source 3, Source 16].
- **Scope of Impact and Targets**: This malicious code specifically targeted Azure-related authentication information and automated secret keys in GitHub Actions, which are widely used in cloud infrastructure environments [Source 7, Source 17, Source 18].

---

## What Happens Next? (Secure Response Methods)

This lightning-fast supply chain attack delivers a stark reminder of the security maxim: "In the digital world, no one can be 100% trusted." Developers or companies that handled the affected package during this period must immediately take the following response actions [Source 7]:

1. **Version Pinning**: Thoroughly avoid the vulnerable versions in question and firmly pin the version back to the verified safe previous release, **1.26.0** [Source 7].
2. **Comprehensive Secret Rotation**: If the package was installed even once in a development environment containing the malicious version, Azure-related credentials and GitHub Actions secrets must be immediately rotated to new values to guard against potential leakage [Source 7].
3. **Strengthened Supply Chain Monitoring**: Moving forward, the adoption of advanced security solutions that verify package integrity in real-time across the entire CI/CD pipeline is accelerating globally, moving beyond complacency rooted merely in famous open-source branding.

---

## AI Perspective

Easy to dismiss as a problem concerning only developers, this incident serves as a representative slice showing how intricately connected the foundation of trust is in modern digital society. Behind the smartphone apps, web services, and cloud systems we use every day lie thousands of open-source packages intertwined like a spiderweb. If a single small screw (package) shakes, the entire giant building (service) can be threatened. Moving forward, a supply chain security framework that transparently and rigorously verifies the reliability of the tools we import is more urgent than ever, matching the importance of coding skills themselves.

---

## References

1. [Microsoft's agent-framework PyPI package Compromised with Credential Stealer](https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer) [Source 1]
2. [Secure PyPI Packages - 16K+ Projects From PyPI](https://www.bing.com/aclick?ld=e8MGxqEwIckNRkofSDE9RZSzVUCUyhyXQCO9oiZ32AYVUcUCdcy_8e_QkCWirnWclBVub227fMt1Iuf2-P6lDskhNij9dIiDNkedC4XdnJP9wL2_LmCVh66uI5MiHE9AYc_t7-cA48zWJAibzw_Sdeur1Rkvj3S5WDklw4rqi-TldMjbUNm2GDN3O9sU5mzhn5oCppHVAfmiRkciJcmY42dYa4tMo&u=aHR0cHMlM2ElMmYlMmZ3d3cuY2hhaW5ndWFyZC5kZXYlMmZwcm9kdWN0cyUyZmxpYnJhcmllcyUyZnB5dGhvbiUzZm1zY2xraWQlM2Q2ZmUwMDdhYjIzNmQxYjI2ZWUzZjZkNTY3NGY3ZjA1MyUyNnV0bV9zb3VyY2UlM2RiaW5nJTI2dXRtX21lZGl1bUlzZGNwYyUyNnV0bV9jYW1wYWlnbiUzZGJnX3NfYXBhY19hY3FfZ2VuZXJpY19ib2YlMjZ1dG1fdGVybSUzZHB5cGklMjUyOG1hbHdhcmUlMjZ1dG1fd29udGVudCUzZGxpYnJhcmllc19weXBp&rlid=6fe007ab236d1b26ee3f6d5674f7f053) [Source 2]
3. [Microsoft agent-framework Compromised: Credential Stealer ...](https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi) [Source 3]
4. [PyPI agent-framework 1.26.1: Credential Stealer Fix ...](https://explainx.ai/blog/microsoft-agent-framework-pypi-1-26-credential-stealer-november-2026) [Source 7]
5. [Inside the LiteLLM 1.107.0 supply chain compromise: Credential theft...](https://threatnoir.com/article/inside-the-litellm-1-107-0-supply-chain-compromise-credential-theft-through-pyth-e59453) [Source 11]
6. [[Security]: litellm PyPI package (v1.82.7 + v1.82.8) compromised...](https://github.com/BerriAI/litellm/issues/24518) [Source 12]
7. [Download Microsoft Visual C++ 2010 Service Pack 1 Redistributable...](https://www.microsoft.com/en-us/download/details.aspx?id=26999) [Source 14]
8. [LiteLLM PyPI Supply Chain Attack — Credential Stealer in... — al-ice.ai](https://al-ice.ai/posts/2026/07/litellm-pypi-supply-chain-attack-credential-stealer/) [Source 15]
9. [Microsoft's agent-framework on PyPI shipped a credential ...](https://techbytes.app/posts/microsofts-agent-framework-on-pypi-shipped-a-credential-stealer-in/) [Source 16]
10. [Two malicious agent-framework releases on PyPI carried a ...](https://pulse.adyog.com/briefs/two-malicious-agent-framework-releases-on-pypi-carried-a-sec) [Source 17]
11. [Microsoft agent-framework Compromised Twice on PyPI](https://safedep.io/blog/microsoft-agent-framework-pypi-compromise) [Source 18]