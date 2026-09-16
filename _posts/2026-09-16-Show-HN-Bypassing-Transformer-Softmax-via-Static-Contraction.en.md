---
layout: post
title: "AI Is Getting Smarter and Faster? The Secret Behind 'Softmax' Bypassing Techniques"
description: "Introducing the latest technology that innovatively improves the softmax function, which slows down AI model computation and consumes significant memory."
summary: "As technologies emerge that skip or optimize 'softmax,' a chronic computational bottleneck in AI transformer models, a new AI era capable of processing larger volumes of information faster is opening."
tags: [AI, Transformer, Softmax, Deep Learning, Technology Trends]
image: 2026-09-16-Show-HN-Bypassing-Transformer-Softmax-via-Static-Contraction.jpg
image_alt: "Digital art illustrating the process where complex formulas and symbols are simplified to increase AI model efficiency."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Reducing softmax dependency is an essential step for maximizing AI efficiency. This technological breakthrough will be a vital key to broadening the horizon of information that AI can process, beyond mere speed improvements."
quiz:
  - question: "What is the primary role of the Softmax function?"
    choices: ["Compress data", "Convert numbers into a probability distribution", "Delete data"]
    answer: 1
    explanation: "Softmax is a function that helps AI make final judgments by converting various values into a probability distribution [Source: Softmax function - Wikipedia](https://en.wikipedia.org/wiki/Softmax_function)."
  - question: "What does the SOFT (Softmax-free Transformer) model use to replace existing dot-product similarity?"
    choices: ["Gaussian kernel function", "Linear function", "Log function"]
    answer: 0
    explanation: "The SOFT model uses a Gaussian kernel function to implement self-attention without softmax [Source: SOFT: Softmax-free Transformer with Linear Complexity](https://proceedings.neurips.cc/paper/2021/file/b1d10e7bafa4421218a51b1e1f1b0ba2-Paper.pdf)."
  - question: "What is the name of the model that introduced a 'forget gate'?"
    choices: ["ForgettingTransformer(FoX)", "Softmax-free Transformer", "UniAttn"]
    answer: 0
    explanation: "ForgettingTransformer(FoX) integrates a forget gate mechanism into attention scores, enabling better context processing [Source: ForgettingTransformer: Softmax Attention with a Forget Gate](https://arxiv.org/abs/2503.02130)."
lang: en
ref: 2026-09-16-Show-HN-Bypassing-Transformer-Softmax-via-Static-Contraction
audio: 2026-09-16-Show-HN-Bypassing-Transformer-Softmax-via-Static-Contraction.en.mp3
industry: creative
---

Imagine you are trying to find specific information in a massive library. What if the librarian had to open and sort every single book before giving you an answer? As the number of books increases, the time it takes for the librarian to answer would grow exponentially, beyond imagination. The problem currently faced by AI models—especially the 'Transformer' (the core AI structure that grasps relationships between words in a sentence)—is quite similar.

Recently, in the field of artificial intelligence, innovative attempts are being actively made to skip or optimize the 'softmax' operation, which has been taken for granted, to solve this chronic 'bottleneck.'

## Why It Matters

The Transformer is the foundation for almost all modern AI. Within this structure, the softmax function is like a 'toll' that must be paid every time information is processed. Softmax plays an essential role in helping AI make final choices or judgments by converting various data values into a probability distribution [Source: Softmax function - Wikipedia](https://en.wikipedia.org/wiki/Softmax_function).

The issue is that the amount of information AI handles has exploded recently. As more data needs to be processed, softmax operations become the primary culprit for consuming massive amounts of memory and slowing down overall computational speed. If this operation can be bypassed or optimized, AI can process longer contexts much faster while using far less energy. This signals a hopeful future where we can comfortably use smarter, more responsive AI assistants in our daily lives.

## The Explainer

To understand softmax, let’s use a simple analogy. Think of the process of picking your 'favorite product' at a shopping mall. The process of comparing the price, quality, and design of numerous products and then assigning a probability to how much each product appeals to you is essentially a softmax operation. You score all the choices and sum them up to convert them into a 100% probability distribution.

But what if an AI model had to read an entire book’s worth of content that is very long and complex? Calculating the precise probability by comparing every single word one by one is an extremely arduous task.

Researchers have recently found a few clever ways around this.

1. **Static Contraction Technique**: Just like paving a road in advance, this method pre-blocks unnecessary calculation paths during the operation and replaces them with efficient formulas. This significantly reduces the risk of AI models experiencing Out-Of-Memory (OOM) issues in long contexts [Source: GitHub - PJHkorea/jax-softmax-bypass](https://github.com/PJHkorea/jax-softmax-bypass), [Source: ShowHN: Bypassing Transformer Softmax via Static Contraction](https://news.ycombinator.com/item?id=49666335).
2. **Softmax-free**: A model called 'SOFT' uses a relatively simple mathematical function called a 'Gaussian kernel' instead of existing complex operations. It is like choosing a more intuitive shortcut instead of punching into a complex scientific calculator every time for probability calculations [Source: SOFT: Softmax-free Transformer with Linear Complexity](https://proceedings.neurips.cc/paper/2021/file/b1d10e7bafa4421218a51b1e1f1b0ba2-Paper.pdf), [Source: [2110.11945] SOFT: Softmax-free Transformer with Linear Complexity](https://arxiv.org/abs/2110.11945).
3. **Forgetting Mechanism**: 'ForgettingTransformer(FoX)' utilizes a 'forget gate' that appropriately forgets unnecessary information. Just as we naturally memorize important information and let the rest go, it selectively adjusts the attention scores, making context processing much easier [Source: ForgettingTransformer: Softmax Attention with a Forget Gate](https://arxiv.org/abs/2503.02130), [Source: ForgettingTransformer: Softmax Attention with... | Papers with Code](https://paperswithcode.co/paper/2503.02130), [Source: GitHub - zhixuan-lin/forgetting-transformer](https://github.com/zhixuan-lin/forgetting-transformer).

## Where We Stand

Currently, these technologies are rapidly developing in various forms, from laboratory-stage Proof of Concepts (PoC) to academic proposals. However, it is premature to say that softmax has been completely replaced. While it is clearly proven to be more efficient than standard existing methods, there remain aspects that require additional verification before being applied to all general-purpose AI models. Nevertheless, attempts such as 'UniAttn,' which drastically reduce computational costs while minimizing performance degradation, are consistently achieving results, raising expectations [Source: UniAttn: Reducing Inference Costs via Softmax... | Papers with Code](https://paperswithcode.co/paper/2502.00439).

## What's Next

The future AI technology race will shift from merely creating 'bigger models' to 'who can create more efficient models.' These softmax bypassing techniques will be essential keys to running more powerful AI on devices with physically limited computational resources, like the smartphones we use. If these current studies come to fruition, we will encounter smarter AI in our daily lives that perfectly remembers longer conversation histories and responds at a faster speed.

## References

1. GitHub - PJHkorea/jax-softmax-bypass: [https://github.com/PJHkorea/jax-softmax-bypass](https://github.com/PJHkorea/jax-softmax-bypass)
2. Vertex-Softmax: Tight Transformer Verification via Exact Softmax Optimization∗: [https://arxiv.org/pdf/2605.10974](https://arxiv.org/pdf/2605.10974)
3. SimA: Simple Softmax-free Attention for Vision Transformers: [https://openaccess.thecvf.com/content/WACV2024/papers/Koohpayegani_SimA_Simple_Softmax-Free_Attention_for_Vision_Transformers_WACV_2024_paper.pdf](https://openaccess.thecvf.com/content/WACV2024/papers/Koohpayegani_SimA_Simple_Softmax-Free_Attention_for_Vision_Transformers_WACV_2024_paper.pdf)
4. SOFT: Softmax-free Transformer with Linear Complexity: [https://proceedings.neurips.cc/paper/2021/file/b1d10e7bafa4421218a51b1e1f1b0ba2-Paper.pdf](https://proceedings.neurips.cc/paper/2021/file/b1d10e7bafa4421218a51b1e1f1b0ba2-Paper.pdf)
5. [2110.11945] SOFT: Softmax-free Transformer with Linear Complexity: [https://arxiv.org/abs/2110.11945](https://arxiv.org/abs/2110.11945)
6. Differential Transformer | Hacker News: [https://news.ycombinator.com/item?id=41776324](https://news.ycombinator.com/item?id=41776324)
7. Softmax function - Wikipedia: [https://en.wikipedia.org/wiki/Softmax_function](https://en.wikipedia.org/wiki/Softmax_function)
8. ForgettingTransformer: Softmax Attention with a Forget Gate: [https://arxiv.org/abs/2503.02130](https://arxiv.org/abs/2503.02130)
9. ShowHN: Bypassing Transformer Softmax via Static Contraction: [https://news.ycombinator.com/item?id=49666335](https://news.ycombinator.com/item?id=49666335)
10. ForgettingTransformer: Softmax Attention with... | Papers with Code: [https://paperswithcode.co/paper/2503.02130](https://paperswithcode.co/paper/2503.02130)
11. In-Context Learning with Transformers: Softmax... | OpenReview: [https://openreview.net/forum?id=lfxIASyLxB](https://openreview.net/forum?id=lfxIASyLxB)
12. Transformers are RNNs: Fast Autoregressive... - YouTube: [https://www.youtube.com/watch?v=hAooAOFRsYc](https://www.youtube.com/watch?v=hAooAOFRsYc)
13. UniAttn: Reducing Inference Costs via Softmax... | Papers with Code: [https://paperswithcode.co/paper/2502.00439](https://paperswithcode.co/paper/2502.00439)
14. GitHub - zhixuan-lin/forgetting-transformer: [https://github.com/zhixuan-lin/forgetting-transformer](https://github.com/zhixuan-lin/forgetting-transformer)
15. Softmax Function in Deep Learning: [https://lzwjava.com/notes/2025-06-03-softmax-en](https://lzwjava.com/notes/2025-06-03-softmax-en)