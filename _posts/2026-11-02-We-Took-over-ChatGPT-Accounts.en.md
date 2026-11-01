---
layout: post
title: "My ChatGPT account was hacked? Researchers expose security loopholes"
description: "Security researchers recently succeeded in actually hacking into OpenAI employees' ChatGPT accounts. We explain why this happened and whether our accounts are safe."
summary: "Security researchers demonstrated the importance of AI security by revealing how they connected two vulnerabilities to hijack OpenAI employees' ChatGPT accounts and access internal systems."
tags: [ChatGPT, AI Security, Account Hijacking, Cybersecurity]
image: 2026-11-02-We-Took-over-ChatGPT-Accounts.jpg
image_alt: "Digital image of a padlock being unlocked on a screen"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "As AI models become smarter, the security threshold for the systems that handle them must rise accordingly. This case illustrates that the 'invisible shield' protecting AI technology is just as important as the development of the technology itself."
quiz:
  - question: "What method did researchers use to hijack the OpenAI employees' accounts?"
    choices: ["Password guessing", "Connecting two vulnerabilities", "Sending phishing emails"]
    answer: 1
    explanation: "The researchers used a method of chaining two vulnerabilities to gain account privileges."
  - question: "What were the researchers able to confirm after hijacking the accounts?"
    choices: ["Access to users' chat history", "Access to OpenAI's internal repositories", "Theft of paid billing information"]
    answer: 1
    explanation: "The researchers demonstrated the process of accessing internal repositories and creating pull requests using the hijacked account privileges."
  - question: "What characterizes the accounts that OpenAI has suspended in the past?"
    choices: ["Accounts with unpaid subscriptions", "Accounts linked to state-backed hacking groups", "Multi-account creators"]
    answer: 1
    explanation: "OpenAI has previously suspended accounts of state-backed hacking groups that were used for illegal purposes such as malware development or spreading fake news."
lang: en
ref: 2026-11-02-We-Took-over-ChatGPT-Accounts
audio: 2026-11-02-We-Took-over-ChatGPT-Accounts.en.mp3
industry: security
---

Imagine this: One morning, you type "Organize my schedule today" to ChatGPT as usual, but the AI gives you a nonsensical response or starts spitting out strange sentences mixed with your personal information. It might not be a problem you can just brush off as 'the AI making another mistake.' Recent events in the security industry suggest that the security of AI services, now a necessity in our daily lives, is being threatened closer to home than you might think.

### Why is this important?

ChatGPT is a leading AI model with 700 million users worldwide. [Business Insider](https://www.businessinsider.com/chatgpt) Now, many people use it to summarize work documents, draft emails, and even share personal concerns with AI. If an account for this service is hacked, it goes beyond just leaking personal conversations. It can serve as a dangerous gateway for an attacker to communicate directly with external services using your account privileges or even infiltrate a company’s internal systems through AI.

The security issue revealed here goes beyond the level of simply asking, 'Should I change my password?' It is a wake-up call that the underlying systems supporting the massive technology of AI are becoming a new 'hunting ground' for attackers.

### Easy to understand: The 'small gap' in security

Security experts describe this incident as "chaining two vulnerabilities (weaknesses in security)." [The Register](https://www.theregister.com/security/2026/09/18/researchers-used-claude-to-hack-openai-employees-chatgpt-accounts/5297517)

To put it simply: no matter how tightly you lock a front door made of solid steel (the first security layer), if a tiny window right next to it is left open (the second vulnerability), someone can squeeze through that gap. The researchers found small gaps hidden throughout the system, connected them like puzzle pieces, and eventually opened the big door known as 'administrator privileges.'

According to a report by 'Parameter AI Labs,' these hijacked accounts were able to freely call ChatGPT’s authenticated APIs (Application Programming Interfaces, the communication channels between software) by posing as actual users. [Parameter AI Labs](https://www.parameter.ai/labs/we-found-a-gap-at-openai) In other words, the attacker became you and could command the AI as they pleased. The researchers even successfully demonstrated using these privileges to access OpenAI's internal systems and create a 'pull request,' which is a request to modify software code. [The Register](https://www.theregister.com/security/2026/09/18/researchers-used-claude-to-hack-openai-employees-chatgpt-accounts/5297517)

### Where are we now?

Of course, OpenAI is also taking these security risks very seriously and responding accordingly. In the past, cases were discovered where state-backed hacking groups used ChatGPT to sophisticatedly create malicious code, engage in employment scams, or spread misinformation, leading to the mass suspension of related accounts. [The Record](https://therecord.media/openai-takes-down-chatgpt-accounts-hacking)

However, instances like this, where 'white hat hackers' (ethical security researchers) penetrate into the company's internal systems, pose a bigger challenge for us. This attack specifically targeted the accounts of OpenAI's own employees, proving just how fatal small security gaps can be. [Sıfırıncı Dakika](https://sifirincidakika.com/haber/arastirmacilar-chatgpt-hesaplarini-ele-gecirdigini-acikladi)

### What will happen in the future?

This incident has once again impressed upon AI companies that 'security is not an option, but a matter of survival.' Moving forward, companies will likely stake their future on how robustly they can lock the back doors of their accounts and systems as much as they focus on increasing the intelligence of their AI models.

So, what can average users do? If you receive a suspicious login notification, never ignore it and check it immediately. Also, whenever possible, make sure to set up 'Two-Factor Authentication (2FA, a security method that requires an additional verification process besides the password when logging in).' Just doing this can effectively block the 'first door' that attackers are targeting.

AI has now become an inseparable part of our lives. It is time for the technology that protects us to move faster, matching the speed at which technology is becoming more convenient.

## References

1. [Do the Math: HowWeTookOverChatGPTAccounts- Parameter](https://www.parameter.ai/labs/we-found-a-gap-at-openai)
2. [AraştırmacılarChatGPThesaplarını ele geçirdiğini... | Sıfırıncı Dakika](https://sifirincidakika.com/haber/arastirmacilar-chatgpt-hesaplarini-ele-gecirdigini-acikladi)
3. [OpenAI takes down ChatGPT accounts linked to state-backed hacking](https://therecord.media/openai-takes-down-chatgpt-accounts-hacking)
4. [Researchers used Claude to hack OpenAI employees' ChatGPT accounts](https://www.theregister.com/security/2026/09/18/researchers-used-claude-to-hack-openai-employees-chatgpt-accounts/5297517)
5. [ChatGPT: Everything You Need to Know About... - Business Insider](https://www.businessinsider.com/chatgpt)