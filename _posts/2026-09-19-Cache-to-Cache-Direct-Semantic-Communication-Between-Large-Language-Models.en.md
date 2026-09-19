---
layout: post
title: "Can AI talk to each other 'directly' without using human language?"
description: "Introducing 'Cache-to-Cache (C2C)', a new communication method that allows Large Language Models (LLMs) to share their internal knowledge directly, bypassing the intermediate process of text generation."
summary: "C2C technology presents a new paradigm in communication between AI models by skipping the text translation process and directly fusing the KV-Cache—the model's internal memory—thereby more than doubling information transfer speeds while also improving accuracy."
tags: [AI, LLM, TechAnalysis, C2C, ArtificialIntelligence]
image: 2026-09-19-Cache-to-Cache-Direct-Semantic-Communication-Between-Large-Language-Models.jpg
image_alt: "A conceptual image depicting two Large Language Models exchanging information by connecting their internal data directly, without text messages."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "C2C will be a significant milestone in AI's evolution from a simple 'tool that speaks like a human' into an efficient 'intelligent agent network'."
quiz:
  - question: "What distinguishes C2C technology from traditional communication methods between AI models?"
    choices: ["It can generate longer text", "It skips the intermediate text generation process", "It understands user questions faster"]
    answer: 1
    explanation: "C2C communicates by directly exchanging the KV-Cache, the model's internal memory, without going through the medium of text."
  - question: "What performance changes can be expected from the introduction of C2C technology?"
    choices: ["Communication speed (latency) improves by more than 2x", "AI power consumption is reduced by 10x", "The model size becomes smaller"]
    answer: 0
    explanation: "Research results show that C2C provides an average speed improvement of 2.0x to 2.5x compared to text-based communication."
  - question: "How does C2C connect data between two models?"
    choices: ["It transmits data via the internet", "The models hold conversations with each other", "It projects and fuses the KV-Cache via neural networks"]
    answer: 2
    explanation: "C2C uses neural networks to project and fuse the source model's KV-Cache into the target model's representation space."
lang: en
ref: 2026-09-19-Cache-to-Cache-Direct-Semantic-Communication-Between-Large-Language-Models
audio: 2026-09-19-Cache-to-Cache-Direct-Semantic-Communication-Between-Large-Language-Models.en.mp3
industry: general
---

Imagine you are having a conversation with a foreign friend. Previously, you would have to go through a long process: forming a sentence perfectly in your native language, handing it to a translator to convert it to a foreign language, delivering it to your friend, and having your friend process it back into their own language. What if you could connect your brains directly and exchange 'concepts' like telepathy?

A similar change is happening in the field of Artificial Intelligence (AI). Until now, when AI models shared information, they had to go through the cumbersome process of generating text as if humans were talking, and the other side had to read and understand that text. However, this practice is being broken by the emergence of a new communication paradigm called **'Cache-to-Cache (C2C)'**.

## Why is this important?

Until now, Large Language Models (LLMs) have been trapped in a 'bottleneck' of text, even when collaborating with each other. Just as it takes time for humans to think and polish sentences when writing, AI models had to waste significant time and resources generating text to convey information ([Source: MarkTechPost](https://www.marktechpost.com/2025/11/04/cache-to-cachec2c-direct-semantic-communication-between-large-language-models-via-kv-cache-fusion/)).

C2C completely skips this process. This technology not only solves the AI speed issue but also reduces the 'information loss' that occurred during the process of converting to text ([Source: MarkTechPost](https://www.marktechpost.com/2025/11/04/cache-to-cachec2c-direct-semantic-communication-between-large-language-models-via-kv-cache-fusion/)). It means that an era is coming where AI agents can collaborate faster and more precisely.

## Easy to understand

To understand C2C, you first need to know the concept of **KV-Cache**. Simply put, KV-Cache is a 'short-term memory storage' used by AI when processing sentences. It is like a notebook that stores summarized key information so that the AI does not have to look at everything it has previously read from the beginning every time.

The existing method unpacked this notebook content into text and delivered it to the counterpart model. However, **C2C hands this notebook directly to the other side** ([Source: AI Future Front](https://aifuturefront.com/cache-to-cachec2c-direct-semantic-communication-between-large-language-models-via-kv-cache-fusion/)).

Of course, each model uses a different language or recording method, right? C2C uses a separate 'interpreter neural network' to solve this problem. This neural network reconstructs (projects and fuses) the notes of the source model (the AI giving information) in a way that the target model (the AI receiving information) can understand ([Source: arXiv](https://arxiv.org/abs/2510.03215)). In particular, it has a smart 'Gating Mechanism' that selects only the places where it will be most effective, rather than pouring information into all layers of the target model ([Source: OpenReview](https://openreview.net/forum/id/LeatkxrBCi)).

Metaphorically, it is like two painters working on one canvas by directly sharing their color palettes and brushwork techniques instead of explaining them in words.

## Current situation

The research results are astonishing. Applying C2C technology increases **accuracy by about 3.0% to 5.4%** compared to existing text-based communication methods, and **communication speed (latency) is 2.0x to 2.5x faster on average** ([Source: arXiv](https://arxiv.org/abs/2510.03215v1)). It even recorded about 6.4% to 14.2% higher accuracy than just using a single model alone ([Source: arXiv](https://arxiv.org/abs/2510.03215)).

Current technology has successfully reached the level of directly transmitting knowledge between models ([Source: arXiv](https://arxiv.org/abs/2510.03215)). The research team successfully completed an experiment transmitting knowledge from a model with 4 billion parameters (Qwen3-4B) to a smaller model with 600 million parameters, and visualization results confirmed that the transmitted data naturally permeated into the target model's thinking domain ([Source: C2C Project Page](https://fuvty.github.io/C2C_Project_Page/)).

## What will happen next?

C2C will maximize the efficiency of AI services in the future. Currently, when we ask AI to do complex tasks, responses are often delayed because the AI struggles alone or wastes time exchanging text. In the future, however, countless AI models specialized in each field will be able to exchange information as if they were one giant brain through C2C and respond in real-time.

We are now moving beyond 'language models' into the era of 'intelligent communication networks'. As AIs talk to each other more deeply and quickly, the AI assistants in our lives will provide much smarter and more efficient answers than they do now.

## MindTickleBytes AI Reporter's View
It is very interesting that AI has begun to share data directly, freed from the constraints of human language. This may be evidence that AI is first overcoming the language barriers or limitations of expression that humans experience when communicating. Before long, AI will be moving along an invisible highway of knowledge behind us, beyond just talking to us.

## References
1. [2510.03215] Cache-to-Cache: Direct Semantic Communication Between Large Language Models (https://arxiv.org/abs/2510.03215)
2. Paper page - Cache-to-Cache: Direct Semantic Communication Between Large Language Models (https://huggingface.co/papers/2510.03215)
3. GitHub - thu-nics/C2C (https://github.com/thu-nics/C2C)
4. Cache-to-Cache: Direct Semantic Communication Between Large Language Models | OpenReview (https://openreview.net/forum?id=LeatkxrBCi)
5. Cache-to-Cache: Direct Semantic Communication Between Large Language Models (https://arxiv.org/html/2510.03215v2)
6. [2510.03215v1] Cache-to-Cache: Direct Semantic Communication Between Large Language Models (https://arxiv.org/abs/2510.03215v1)
7. Cache-to-Cache(C2C): Direct Semantic Communication Between Large Language Models via KV-Cache Fusion - MarkTechPost (https://www.marktechpost.com/2025/11/04/cache-to-cachec2c-direct-semantic-communication-between-large-language-models-via-kv-cache-fusion/)
8. Cache-to-Cache: Direct Semantic Communication Between Large (https://arxiv.org/pdf/2510.03215)
9. ICLR Poster Cache-to-Cache: Direct Semantic Communication (https://iclr.cc/virtual/2026/poster/10010020)
10. Cache-to-Cache: Direct Semantic Communication Between Large (https://liner.com/review/cachetocache-direct-semantic-communication-between-large-language-models)
11. Cache-to-Cache (https://fuvty.github.io/C2C_Project_Page/)
12. Cache-to-Cache | OpenTrain AI (https://www.opentrain.ai/papers/cache-to-cache-direct-semantic-communication-between-large-language-models--arxiv-2510.03215/)
13. Cache-to-Cache: Direct Semantic Communication Between Large (https://www.headlinne.com/articles/cache-to-cache-direct-semantic-communication-between-large-language-models-hacker-news)
14. Cache-to-Cache (C2C): Direct Semantic Communication Between (https://aifuturefront.com/cache-to-cachec2c-direct-semantic-communication-between-large-language-models-via-kv-cache-fusion/)