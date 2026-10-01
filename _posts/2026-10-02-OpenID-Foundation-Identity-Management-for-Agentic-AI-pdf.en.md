---
layout: post
title: "Can we give AI 'Agent' status? The story of AI Agent identity cards"
description: "When an AI agent handles tasks on behalf of a person, how can it safely prove its identity and receive delegated authority? Introducing the new AI identity management standard proposed by the OpenID Foundation."
summary: "Through a white paper released by the OpenID Foundation, we explore the systematic management standards for granting secure identity and authority to 'AI agents' as entities with independent personalities."
tags: [AI, Agent, Identity Management, Security, OpenID]
image: 2026-10-02-OpenID-Foundation-Identity-Management-for-Agentic-AI-pdf.jpg
image_alt: "A graphic depicting the safe connection between AI agents and users in the digital space"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "For an AI agent to move beyond a simple tool and become an 'agent' (proxy), it is essential to prove 'who I am' and 'under whose authority I am acting.' This standard is a very important first step in building trust in the AI business ecosystem."
quiz:
  - question: "Which of the following is one of the core principles of AI agent management proposed by the OpenID Foundation?"
    choices: ["AI must always share the human's ID", "AI agents should be treated as 'independent primary identities' separate from humans", "All AI agents automatically have administrator privileges"]
    answer: 1
    explanation: "AI agents should have independent digital identities, rather than simply mimicking users, to safely receive and manage delegated authority."
  - question: "What information can be included in the tokens used by AI agents?"
    choices: ["The user's entire password", "The agent's owner, trust posture, and scope of authority", "All training data of the AI model"]
    answer: 1
    explanation: "Attempts are underway to extend OpenID Connect (OIDC) tokens to clearly define the agent's trustworthiness and allowed range of functions."
  - question: "Which institution participated in the work of this white paper?"
    choices: ["Google's independent research team", "Stanford University's 'Loyal Agents Initiative'", "An alliance of private security companies only"]
    answer: 1
    explanation: "This white paper was prepared in collaboration with Stanford University's Loyal Agents Initiative and the AI Identity Management Community Group."
lang: en
ref: 2026-10-02-OpenID-Foundation-Identity-Management-for-Agentic-AI-pdf
audio: 2026-10-02-OpenID-Foundation-Identity-Management-for-Agentic-AI-pdf.en.mp3
industry: education
---

Imagine this. On a busy morning, you ask the AI assistant on your smartphone, "Check my emails, schedule meetings according to my calendar, and even book my flights." The AI handles these complex tasks before your eyes in an instant. However, this raises a question: when the AI pays for a flight ticket in your name, how can the airline site be sure that "this AI is a legitimate agent moving with the permission of you, the owner"?

The OpenID Foundation recently released a white paper titled "Identity Management for Agentic AI," which provides answers to these concerns [[Ref 12](https://www.linkedin.com/posts/ankita-gupta-89214515_authorization-authentication-and-security-activity-7390768403097120768-dS_R), [Ref 13](https://openid.or.jp/news/2025/11/identity-management-for-agentic-ai.html)]. This is because AI is evolving beyond a simple tool that carries out commands into an "Agent" that thinks and acts for itself like a human.

## Why is this important?

Most of the numerous apps and services we have used so far were designed on the premise that a "human" logs in directly. But now, AI sends emails, retrieves data, and accesses external services on our behalf. If there is no identity verification system for AI agents, there is a risk that AI could indiscriminately abuse its authority, or that malicious users could impersonate AI to steal your valuable personal information.

To ensure security and interoperability, this white paper presents strategic guidelines on how AI agents can prove their identity online and safely receive "delegation" of authority from humans [[Ref 3](https://www.linkedin.com/posts/ayeshadissanayaka_ai-identitymanagement-agenticai-activity-7381670116700332033-FQMG), [Ref 10](https://www.alphaxiv.org/overview/2510.25819v1)]. Simply put, it is about issuing a kind of "digital employee ID card" to an AI agent to precisely define the scope of its work.

## Understanding it easily: The AI agent's digital ID card

Let's use a simple analogy. Suppose you are the CEO of a large company. Because you cannot handle all tasks yourself, you hired a capable secretary (AI agent). Instead of letting the secretary use the company seal (access authority) as they please, you would give them a power of attorney stating that "the seal can only be used for secretarial duties."

The core idea proposed by the OpenID Foundation is exactly this "digital power of attorney."

1. **Granting an independent identity**: We must treat the AI agent not as a being that simply borrows a human's ID, but as one with a unique "digital identity" [[Ref 15](https://www.emergentmind.com/topics/agentic-jwt-a-jwt)].
2. **Delegated Authority**: When a user gives an AI permission to perform a specific task, the AI acts safely only within that scope [[Ref 4](https://podcasts.apple.com/us/podcast/390-identity-management-for-agentic-ai-with-tobin-south/id1471899975?i=1000740200992)].
3. **Including specialized information**: The digital ID card (ID token) used by an AI agent includes information such as "who the owner is," "how trustworthy it is (Trust Posture)," and "what functions it is allowed to use (Authorized Capabilities)" [[Ref 5](https://changegamer.ai/resources/agent-identity-authentication)].

## How far have we come?

The field of AI security is changing very rapidly. This white paper is the result of intense deliberation throughout 2025, with participation from Stanford University's 'Loyal Agents Initiative' and the AI Identity Management Community Group [[Ref 14](https://conectia.pro/en/blog/identity-management-for-agentic-ai-paper-deep-dive)].

We are currently in an experimental stage of managing AI agent access rights using various security standards (OAuth 2.1, OIDC, etc.). Of course, perfectly preventing unexpected risks that arise in the process of agents acting on their own remains a major challenge. Many companies and research institutions are currently working to establish standards for AI agent security [[Ref 2](https://seclab.cs.hm.edu/theses/ek-agentic-identity/), [Ref 7](https://www.kakunin.ai/blog/identity-and-access-management-for-ai-agents)].

## What happens next?

AI services will increasingly handle complex tasks automatically. The changes we need to pay attention to are "prevention of agent impersonation" and "transparent authority management." Just as we approve permissions when we first install an app on our smartphone, in the future, a procedure for clearly confirming and approving permissions before an AI agent performs tasks on our behalf will be standardized.

This white paper, edited by Tobin South, clearly shows what the first virtue required for AI agents to become core members of businesses and daily life is [[Ref 14](https://conectia.pro/en/blog/identity-management-for-agentic-ai-paper-deep-dive)]. Rather than how smart the AI assistant we use will become, how "trustworthy" it is will become the core competitive edge.

---
## References

1. AgenticAIのための (https://openid.or.jp/Identity-Management-for-Agentic-AI-jp_v1.1.pdf)
2. Designing and Evaluating Auditable DelegatedIdentityforAIAgents (https://seclab.cs.hm.edu/theses/ek-agentic-identity/)
3. OpenIDFoundationreleases paper onIdentityManagementfor... (https://www.linkedin.com/posts/ayeshadissanayaka_ai-identitymanagement-agenticai-activity-7381670116700332033-FQMG)
4. #390 -IdentityManagementfor… -Identityat the... - Apple Podcasts (https://podcasts.apple.com/us/podcast/390-identity-management-for-agentic-ai-with-tobin-south/id1471899975?i=1000740200992)
5. AgentIdentityand Authentication — ChangeGamer (https://changegamer.ai/resources/agent-identity-authentication)
6. Who Governs the Machine? A MachineIdentityGovernance... (https://arxiv.org/pdf/2604.06148)
7. Identityand AccessManagementforAIAgents | Kakunin (https://www.kakunin.ai/blog/identity-and-access-management-for-ai-agents)
8. IdentityManagementforAgenticAI解説 - Speaker Deck (https://speakerdeck.com/fujie/identity-management-for-agentic-ai-jie-shuo)
9. IdentityManagementforAgenticAI: The new frontier of... | alphaXiv (https://www.alphaxiv.org/overview/2510.25819v1)
10. FYI:OpenIDFoundationpublished a white paper titledIdentity... (https://bgin.discourse.group/t/fyi-openid-foundation-published-a-white-paper-titled-identity-management-for-agentic-ai/819)
11. OpenIDFoundation's whitepaper onIdentityManagement... | LinkedIn (https://www.linkedin.com/posts/ankita-gupta-89214515_authorization-authentication-and-security-activity-7390768403097120768-dS_R)
12. 「IdentityManagementforAgenticAI」の翻訳版公開 | お知らせ (https://openid.or.jp/news/2025/11/identity-management-for-agentic-ai.html)
13. (2/3) The Best Map We Have of theAgenticIdentityProblem | Conectia (https://conectia.pro/en/blog/identity-management-for-agentic-ai-paper-deep-dive)
14. AgenticJWT (A-JWT) Protocol (https://www.emergentmind.com/topics/agentic-jwt-a-jwt)