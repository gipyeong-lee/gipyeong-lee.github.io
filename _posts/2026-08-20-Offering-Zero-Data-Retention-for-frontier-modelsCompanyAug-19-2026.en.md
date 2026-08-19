---
layout: post
title: "Can You Give Sensitive Information to AI? What is 'Zero Data Retention (ZDR)'?"
description: "We explain the meaning and limitations of 'Zero Data Retention' contracts that companies are adopting to use AI safely."
summary: "Zero Data Retention (ZDR) is a powerful security contract in which AI providers promise to immediately delete user data and not use it for training."
tags: [AI Security, Data Privacy, Zero Data Retention, ZDR]
image: 2026-08-20-Offering-Zero-Data-Retention-for-frontier-modelsCompanyAug-19-2026.jpg
image_alt: "Graphic showing a digital security padlock connected to an AI model"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "The effort by companies to balance AI performance and security is notable. It must be remembered that ZDR is a contract, not just a simple setting."
quiz:
  - question: "What is the core promise of Zero Data Retention (ZDR)?"
    choices: ["Retain data for 30 days", "Delete data immediately after inference and do not use it for training", "Disclose all conversation logs"]
    answer: 1
    explanation: "ZDR is a contract stating that data is not retained after the moment of inference and will not be used for training or service improvement."
  - question: "What should you be aware of when signing a ZDR contract?"
    choices: ["Performance is guaranteed to degrade", "It applies to all AI features", "Stateful features, etc., may be excluded from the contract scope"]
    answer: 2
    explanation: "ZDR primarily applies to stateless paths, and features of complex agent systems may be excluded."
  - question: "What change recently occurred in some models (e.g., Claude Fable 5)?"
    choices: ["ZDR was made mandatory", "Adopted a 30-day data retention policy instead of ZDR", "Data retention was stopped entirely"]
    answer: 1
    explanation: "The Claude Fable 5 model switched to a 30-day data retention policy to ensure safety instead of a Zero Data Retention policy."
lang: en
ref: 2026-08-20-Offering-Zero-Data-Retention-for-frontier-modelsCompanyAug-19-2026
audio: 2026-08-20-Offering-Zero-Data-Retention-for-frontier-modelsCompanyAug-19-2026.en.mp3
industry: legal
---

Imagine this: your company wants to use the latest AI to analyze data from a highly confidential project. However, when you go to input that information into the AI, you hesitate. You worry, "Will this data be recorded on the AI company’s servers, or will it leak later as an answer to someone else's query?"

"Zero Data Retention (ZDR)" is a concept that emerged to resolve these concerns. Is it truly a magic shield that can keep our data safe?

## Why Is This Important?

In the past, it was taken for granted that data would remain on servers when using public cloud services. However, for businesses, transmitting customer personal information or a company's core trade secrets to an external AI model is a major security risk. ZDR acts as a "security contract" that allows these companies to utilize cutting-edge AI models (Frontier Models) for their work with peace of mind [Source: Zero Data Retention AI: Same Models, No Retention | BrainPack](https://www.brainpack.ai/infrastructure/deployment/zdr). Because ZDR eliminates the "data trail" left behind when sending information, it is emerging as a crucial option, particularly in security-sensitive fields like finance, healthcare, and law.

## Understanding It Simply: An Amnesic Assistant

To use a simple analogy, ZDR is like hiring an "amnesic assistant."

General AI stores the content of your questions and its answers on its servers. It’s like a meticulous secretary who keeps a record of every conversation. However, applying ZDR is like contracting that secretary to "only listen to me the moment I ask a question and you provide an answer, and delete everything from your memory as soon as the answer is finished."

Through this contract, the provider promises in writing that they will not retain data after the moment of inference (the process where the AI generates an answer to a question), and will not use it for model training or service improvement [Source: Zero Data Retention AI: Same Models, No Retention | BrainPack](https://www.brainpack.ai/infrastructure/deployment/zdr). In some cases, this process doesn't even generate the "surveillance logs" that could pose a risk of data leakage [Source: Zero Data Retention AI: Same Models, No Retention | BrainPack](https://www.brainpack.ai/infrastructure/deployment/zdr).

## How Far Can We Trust It?

ZDR is not a catch-all solution. The most important thing to be aware of is that **ZDR is a legal "contract," not just a "setting button"** [Source: Zero data retention | Agentic Delivery Glossary](https://readysolutions.ai/glossary/zero-data-retention/).

Many users mistakenly believe that as long as they sign a ZDR contract, all features will be perfectly protected. However, if data passes through a path that uses the AI's "stateful features" (features that need to remember previous conversations or work context), it might not receive ZDR protection [Source: Zero data retention | Agentic Delivery Glossary](https://readysolutions.ai/glossary/zero-data-retention/). It’s similar to how an assistant might delete their memory "right now," but if you entrust them with a complex task that requires utilizing a specific "memory storage," that record will remain somewhere.

Additionally, you should keep an eye on recent changes in security policies. Anthropic has introduced a policy to retain data for 30 days for some models to strengthen safety, and in the case of the Claude Fable 5 model, it has abandoned its previous zero data retention policy in favor of this 30-day retention policy [Source: Data retention practices for Covered Models | Anthropic Help Center](https://support.claude.com/en/articles/15425996-data-retention-practices-for-covered-models) [Source: Fable 5's 30-Day Retention: The End of Zero Retention? | Digital Applied](https://www.digitalapplied.com/blog/fable-5-30-day-data-retention-zdr-enterprise-2026).

## Future Outlook

The AI security market is expected to become even more segmented. Companies will likely use high-performance AI while adopting methods to choose between models where ZDR applies and those where it does not, depending on the importance of the security required. ZDR is establishing itself as a premium security service that requires higher costs [Source: Zero Data Retention AI: Same Models, No Retention | BrainPack](https://www.brainpack.ai/infrastructure/deployment/zdr).

If you are a corporate manager, it is essential to thoroughly check how the AI services we use process data and the extent of ZDR contract coverage. Instead of trusting that "the AI will handle it," we need the wisdom to clearly understand the structure in which data is processed and sign contracts accordingly.

## MindTickleBytes AI Reporter's Perspective

Security and performance are like a seesaw; when you raise one side, the other is bound to go down. ZDR shows the struggle of companies trying to balance this seesaw. It is time to develop an eye for carefully examining the contractual conditions hidden behind the convenience of technology.

## References
1. [Zero data retention | Agentic Delivery Glossary](https://readysolutions.ai/glossary/zero-data-retention/)
2. [Zero Data Retention AI: Same Models, No Retention | BrainPack](https://www.brainpack.ai/infrastructure/deployment/zdr)
3. [Frontier Safety Roadmap Updates | Anthropic](https://www.anthropic.com/responsible-scaling-policy/updates)
4. [Data retention practices for Covered Models | Anthropic Help Center](https://support.claude.com/en/articles/15425996-data-retention-practices-for-covered-models)
5. [Fable 5's 30-Day Retention: The End of Zero Retention? | Digital Applied](https://www.digitalapplied.com/blog/fable-5-30-day-data-retention-zdr-enterprise-2026)