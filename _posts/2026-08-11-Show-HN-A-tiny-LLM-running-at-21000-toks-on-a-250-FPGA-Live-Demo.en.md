---
layout: post
title: "20,000 tokens per second on a $250 FPGA? The truth behind this amazing experiment"
description: "Can you run AI at high speeds without expensive GPUs? Introducing the latest experiment that achieved over 20,000 tokens per second on a $250 FPGA chip."
summary: "By utilizing specialized semiconductor FPGAs to resolve external memory bottlenecks, it has been confirmed that overwhelming AI inference speeds can be achieved on low-cost hardware."
tags: [AI, Hardware, FPGA, TechExperiment, LightweightAI]
image: 2026-08-11-Show-HN-A-tiny-LLM-running-at-21000-toks-on-a-250-FPGA-Live-Demo.jpg
image_alt: "Abstract tech image showing an AI model generating text at high speed on an FPGA board"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "In an AI market dominated by giant models, a paradigm shift toward 'small and efficient' hardware optimization is underway. This is a significant technical milestone that will accelerate the democratization of AI."
quiz:
  - question: "What is the key reason AI performance was improved using an FPGA in this experiment?"
    choices: ["Because it consumes less power than a GPU", "Because the model weights were stored directly inside the chip", "Because a more expensive model was used"]
    answer: 1
    explanation: "The model weights were stored directly inside the chip to prevent the bottleneck of fetching data from external memory."
  - question: "Approximately what speed did the FPGA-based AI model achieve in the experiment?"
    choices: ["About 10 tokens per second", "About 21,000 tokens per second", "About 500 tokens per second"]
    answer: 1
    explanation: "Real-time measurements recorded a speed of approximately 21,300 tokens per second."
  - question: "What is the technical significance of this experiment running AI on low-power hardware?"
    choices: ["The fact that an internet connection is essential", "Overcoming memory bandwidth limitations and increasing efficiency", "The fact that hardware costs must be increased"]
    answer: 1
    explanation: "It demonstrated the potential to overcome existing GPU limitations through a structure with high power efficiency and fast memory access."
lang: en
ref: 2026-08-11-Show-HN-A-tiny-LLM-running-at-21000-toks-on-a-250-FPGA-Live-Demo
audio: 2026-08-11-Show-HN-A-tiny-LLM-running-at-21000-toks-on-a-250-FPGA-Live-Demo.en.mp3
industry: security
---

Imagine if you could use an artificial intelligence on a single small device at home that reads and writes text hundreds of times faster than the conversational AIs we commonly use. When we think of 'Artificial Intelligence (AI),' we usually first think of NVIDIA's high-performance GPUs (Graphics Processing Units) that cost hundreds of thousands of dollars. However, recently, interesting experimental results that shatter this conventional wisdom are pouring out from developers.

Recently, a developer used a Field Programmable Gate Array (FPGA) board—a semiconductor chip whose logic circuits can be programmed in the field—costing only $250 to run a language model, recording a speed of over 21,000 tokens (text fragments) per second. [Source 1](https://www.mikeayles.com/blog/on-chip-llm-kv260/), [Source 8](https://hn.nuxt.dev/item/49242475) This is a surprising figure that makes one doubt their eyes even when compared to existing high-priced equipment. How on earth is this possible?

## Why is this important?

Until now, AI technology has developed in the direction of demanding 'larger, more computations.' Because of this, massive power and expensive hardware have been essential to run Large Language Models (LLMs). However, this experiment poses the fundamental question: "Must AI always run on expensive equipment?"

If sufficiently fast AI inference is possible on ultra-low-power, low-cost hardware, the story changes completely. This is because we will be able to use AI assistants inside the home appliances, cars, and various wearable devices we use without having to send personal information to external servers, entirely in an 'offline' state. This will significantly increase the accessibility of AI technology and become a new breakthrough that resolves data security issues. [Source 5](https://www.reddit.com/r/AIToolsPerformance/comments/1t2r52g/karpathys_microgpt_hits_50000_toks_on_fpga/), [Source 11](https://www.youtube.com/watch?v=C9aqovGc3Jc)

## In simple terms (an analogy)

Why are special semiconductors like FPGAs faster and more efficient than existing GPUs? Let's use a library as an analogy.

Running a giant model on a GPU is like keeping books (model data) in a distant warehouse (external memory) in the library and having a librarian (data path) fetch the books whenever needed. This 'memory bottleneck,' where fetching the books takes longer than reading them, is the main culprit holding back modern AI performance. [Source 5](https://www.reddit.com/r/AIToolsPerformance/comments/1t2r52g/karpathys_microgpt_hits_50000_toks_on_fpga/)

On the other hand, the FPGA-based model used in this experiment adopted a method of spreading all the books out on the desk in advance (storing model weights directly inside the chip). [Source 5](https://www.reddit.com/r/AIToolsPerformance/comments/1t2r52g/karpathys_microgpt_hits_50000_toks_on_fpga/), [Source 11](https://www.youtube.com/watch?v=C9aqovGc3Jc) Since data doesn't need to be moved, the speed is incredibly fast, and there is almost no power wasted moving data. In fact, the 'TerEffic' architecture proposed by the research team reportedly shows 19 times higher power efficiency than existing equipment. [Source 10](https://www.hackster.io/news/researchers-deliver-dramatic-performance-efficiency-gains-for-llms-with-the-fpga-driven-tereffic-09ab3e4e8cb4), [Source 13](https://arxiv.org/html/2502.16473v2)

## How far have we come?

Surprising records are already appearing one after another in the field.

*   **High-Speed FPGA Experiments:** Speeds of 21,000 tokens per second were measured in a $250 FPGA environment, a figure stable enough to handle 2,000 simultaneous users without performance degradation. [Source 1](https://www.mikeayles.com/blog/on-chip-llm-kv260/), [Source 15](https://news.ycombinator.com/item?id=49242475)
*   **Ultra-Low-Cost Microcontrollers:** It has even been confirmed that small language models run at a speed of about 10 tokens per second on a $10 microcontroller. [Source 2](https://www.theregister.com/edge-and-iot/2026/08/04/dev-proves-llms-will-run-on-anything-even-a-10-microcontroller/5283088), [Source 7](https://www.techradar.com/pro/the-next-age-of-llms-dev-gets-a-small-llm-running-at-10-tokens-a-second-locally-on-a-usd10-microcontroller)
*   **Extreme Efficiency:** Cases of models working completely offline on an $8 ESP32-S3 chip (512KB RAM) have been reported. [Source 4](https://www.youtube.com/watch?v=0qXVMt3pIjU)

Of course, there are clear limitations. These small models lack the high intelligence to answer complex questions or write advanced code, and are optimized for short sentence generation or simple classification tasks. [Source 7](https://www.techradar.com/pro/the-next-age-of-llms-dev-gets-a-small-llm-running-at-10-tokens-a-second-locally-on-a-usd10-microcontroller)

## What can we expect?

We are now facing an era of AI that lives and breathes inside a tiny chip in our pockets, not AI located in giant server rooms. Researchers are working to implement smarter AI on smaller devices by introducing more efficient computation methods (such as ternary operations). [Source 11](https://www.youtube.com/watch?v=C9aqovGc3Jc), [Source 13](https://arxiv.org/html/2502.16473v2) In the near future, smart home appliances that perfectly understand our voices and react immediately without an internet connection will become a part of everyday life.

## AI Opinion

In an AI market dominated by giant models, a paradigm shift toward 'small and efficient' hardware optimization is underway. This is a significant technical milestone that will accelerate the democratization of AI. If attempts to optimize algorithms according to the characteristics of hardware continue—moving away from the method of pouring power into performance blindly—AI will permeate our lives more quickly and lightly.

## References

1. [Taalas-Style On-Chip Weights on a $250 FPGA: a Language Model at 60k tok/s | Michael Ayles](https://www.mikeayles.com/blog/on-chip-llm-kv260/)
2. [Dev proves LLMs will run on anything – even a $10 microcontroller](https://www.theregister.com/edge-and-iot/2026/08/04/dev-proves-llms-will-run-on-anything-even-a-10-microcontroller/5283088)
3. [Token Generation Speed Visualizer | LLM Performance Demo](https://shir-man.com/tokens-per-second/)
4. [How This Tiny $8 Chip Runs an LLM With Almost No RAM - YouTube](https://www.youtube.com/watch?v=0qXVMt3pIjU)
5. [r/AIToolsPerformance on Reddit: Karpathy's MicroGPT hits 50,000 tok/s on FPGA](https://www.reddit.com/r/AIToolsPerformance/comments/1t2r52g/karpathys_microgpt_hits_50000_toks_on_fpga/)
6. [LLM Token Generation Speed Simulator & Benchmark](https://kamilstanuch.github.io/LLM-token-generation-simulator/)
7. [The next age of LLMs? Dev gets a small LLM running at 10 tokens a second locally on a $10 microcontroller | TechRadar](https://www.techradar.com/pro/the-next-age-of-llms-dev-gets-a-small-llm-running-at-10-tokens-a-second-locally-on-a-usd10-microcontroller)
8. [Nuxt HN | Show HN: A tiny LLM running at 21,000 tok/s](https://hn.nuxt.dev/item/49242475)
9. [An LLM Writes Shakespeare on an FPGA — and We ... - LinkedIn](https://www.linkedin.com/pulse/llm-writes-shakespeare-fpga-we-measured-every-millisecond-park-syd6c)
10. [Researchers Deliver Dramatic Performance, Efficiency Gains for LLMs with the FPGA-Driven TerEffic](https://www.hackster.io/news/researchers-deliver-dramatic-performance-efficiency-gains-for-llms-with-the-fpga-driven-tereffic-09ab3e4e8cb4)
11. [Can an FPGA Actually Run a Tiny LLM? (Part 1: Memory Wall)](https://www.youtube.com/watch?v=C9aqovGd3Jc)
12. [NLnet; LLM2FPGA](https://nlnet.nl/project/LLM2FPGA/)
13. [TerEffic: Highly Efficient Ternary LLM Inference on FPGA](https://arxiv.org/html/2502.16473v2)
14. [FPGA-Accelerated Large Language Models Used for ChatGPT](https://www.achronix.com/blog/fpga-accelerated-large-language-models-used-chatgpt)
15. [ShowHN: A tiny LLM running at 21,000 tok/s on a $250 FPGA](https://news.ycombinator.com/item?id=49242475)