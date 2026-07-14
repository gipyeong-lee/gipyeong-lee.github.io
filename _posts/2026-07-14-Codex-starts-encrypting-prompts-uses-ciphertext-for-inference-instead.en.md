---
layout: post
title: "My AI queries are encrypted? The shift in privacy brought by 'Encrypted AI'"
description: "We explore new technologies that allow AI to operate on encrypted data, ensuring that what you ask AI isn't visible to anyone else."
summary: "With the development of technologies that allow AI to directly analyze encrypted data, paths are opening up to use AI more safely without sharing sensitive information."
tags: [AI, Security, Encryption, Privacy, Tech Trends]
image: 2026-07-14-Codex-starts-encrypting-prompts-uses-ciphertext-for-inference-instead.jpg
image_alt: "A digital graphic image of data flowing while being encrypted on a computer screen."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "This is a technical leap to capture both privacy and AI performance. It will be an important milestone where data security becomes a daily routine."
quiz:
  - question: "What is the technology that allows AI to process information in an encrypted state?"
    choices: ["Blockchain technology", "Homomorphic Encryption", "Simple compression technology"]
    answer: 1
    explanation: "Homomorphic encryption is a technology that allows computations (AI inference) to be performed on data in its encrypted state without decrypting it."
  - question: "What do users use when sending prompts in decentralized AI infrastructure?"
    choices: ["Miner's public key", "User's personal password", "Public bulletin board"]
    answer: 0
    explanation: "Users encrypt their prompts with the miner's public key and send them; the miner decrypts them locally to perform the inference."
  - question: "What has the SecPE framework proven?"
    choices: ["Improved AI speed", "Simplification of encryption methods", "Higher adversarial robustness than existing models"]
    answer: 2
    explanation: "SecPE has proven superior adversarial robustness (security) compared to existing LM-BFF (Ciphertext) methods."
lang: en
ref: 2026-07-14-Codex-starts-encrypting-prompts-uses-ciphertext-for-inference-instead
audio: 2026-07-14-Codex-starts-encrypting-prompts-uses-ciphertext-for-inference-instead.en.mp3
industry: general
---

Imagine this: You tell the AI assistant you use every day, "Summarize my confidential meeting notes." Have you ever worried about whether this conversation might be exposed, or if it might be recorded in plain text (unencrypted information) somewhere in a data center? Until now, we have had to sacrifice some privacy for the sake of convenience. But now, an interesting technical shift is underway that will make it so the AI "doesn't even get to see" your questions.

### Why does this matter?

Until now, using AI meant sending your data to an AI model server, where the model would read it and return an answer. In this process, the server operator could, in theory, look at the questions you sent. The risk of "data leakage" has been the biggest reason why companies and individuals have been reluctant to entrust AI with confidential corporate information or sensitive personal health data.

But now, a method is being realized where data is passed to the AI while still encrypted, and the AI calculates the result without being able to see the contents. This is a key turning point that will allow us to confidently utilize AI in deeper personal and professional domains.

### Easy to understand: 'The Chef in the Box'

Think of encryption technology as a "sturdy locked metal box."

The existing AI method is like taking out ingredients (data) and handing them directly to a chef (AI). The chef can see the ingredients and cook, but they could also steal them.

On the other hand, the new technology, **Homomorphic Encryption (a technology that allows operations on encrypted data without decrypting it)**, is like a chef cooking with their hands inside a box while wearing **specially made thick gloves.** The chef cannot see the ingredients inside the box with their eyes, but they can precisely complete the dish through the gloves. It is a magical technology where the dish is completed without ever opening the box. [Data Tracker (IETF): Extension technology for homomorphic encryption-based AI inference](https://datatracker.ietf.org/doc/draft-li-pearg-ciphertext-inference-tool-mcp/)

### Current Status: The Start of Secure Prompt Submission

The industry is already actively attempting to introduce these security technologies.

1. **Leveraging Homomorphic Encryption**: Recently, a plan to utilize homomorphic encryption as an extension technology for the Model Context Protocol (MCP, a standard for AI models to communicate with tools) was proposed. This allows remote tools to perform inference directly without understanding the content of the data. [Data Tracker (IETF): Extension technology for homomorphic encryption-based AI inference](https://datatracker.ietf.org/doc/draft-li-pearg-ciphertext-inference-tool-mcp/)
2. **Decentralized AI Infrastructure**: When a user sends a query to an AI miner, they first encrypt the query with the miner's "public key" (the key used to encrypt data). This ensures that the query content leaves no traces on-chain (public records), and the miner decrypts it in a local environment to output only the result. [Keryx Labs: Decentralized AI Inference Infrastructure](https://keryx-labs.com/)
3. **Evolution of Security Frameworks**: New frameworks like SecPE have shown much better defense capabilities against external attacks (adversarial robustness) than existing methods, using techniques like shuffling multiple AI responses to enhance security (Prompt Ensembling). [arXiv: SecPE Private Inference Framework](https://arxiv.org/pdf/2502.00847)

### What happens next?

In the future, we will enter an era where even the AI model creators won't know "what you asked." This goes beyond simple privacy protection; it will drastically change situations where companies were hesitant to adopt cloud AI due to security concerns. Even when we tell our AI, "Write a secret project proposal for me today," an environment will be created where there is no need to worry about security incidents. As technology advances, our data will be protected within stronger "digital gloves."

### AI's Perspective

MindTickleBytes' AI journalist's perspective: "Ultimately, the intelligence of AI is proportional to the amount of information it has, but the security of that information determines the right to use that intelligence. Technology that analyzes data while keeping it encrypted is an essential path for AI to evolve from a simple tool into a trusted partner."

## References

1. [SecPE : SecurePromptEnsembling for Private and (arXiv)](https://arxiv.org/pdf/2502.00847)
2. [draft-li-pearg-ciphertext-inference-tool-mcp-00 - Ciphertext-Based AI Inference (IETF)](https://datatracker.ietf.org/doc/draft-li-pearg-ciphertext-inference-tool-mcp/)
3. [BlockDAG built for decentralized AI inference. Optimistic proofs. (Keryx Labs)](https://keryx-labs.com/)