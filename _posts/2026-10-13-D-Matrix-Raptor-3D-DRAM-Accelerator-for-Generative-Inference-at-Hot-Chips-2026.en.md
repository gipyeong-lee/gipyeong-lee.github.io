---
layout: post
title: "The Secret to Making AI Speak Smarter and Faster: The Arrival of '3D DRAM'"
description: "Introducing d-Matrix's 'Raptor' 3D-DRAM technology, a new semiconductor breakthrough set to dramatically boost generative AI inference speeds."
summary: "Unveiled by d-Matrix, 'Raptor' is a 3D-DRAM architecture that stacks compute units and memory directly, solving the bottleneck of data movement and significantly improving AI inference performance."
tags: [AI, Semiconductor, d-Matrix, 3D-DRAM, HotChips2026]
image: 2026-10-13-D-Matrix-Raptor-3D-DRAM-Accelerator-for-Generative-Inference-at-Hot-Chips-2026.jpg
image_alt: "An image conceptualizing a futuristic structure with semiconductor chips stacked in layers"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Bringing memory and compute physically closer is the future of AI accelerators. Raptor has proven its energy efficiency as an alternative to HBM, opening new possibilities for AI inference infrastructure."
quiz:
  - question: "What is the core structure of the 'Raptor' technology unveiled by d-Matrix?"
    choices: ["SRAM laid out horizontally", "Compute units and DRAM stacked vertically", "Distributed cloud servers"]
    answer: 1
    explanation: "Raptor is a 3D-DRAM architecture where TSMC 4nm compute units and custom DRAM are stacked vertically, connected with a 36-micron pitch."
  - question: "What advantage does Raptor technology have over existing HBM?"
    choices: ["Higher power consumption", "About 1/10th the energy efficiency", "Reduced data transfer speed"]
    answer: 1
    explanation: "Raptor enables efficient computation with about 1/10th the power consumption of HBM."
  - question: "What is the core problem Raptor aims to solve?"
    choices: ["The 'memory bottleneck' caused during data movement", "Internet connection speed issues", "Lack of AI training data"]
    answer: 0
    explanation: "Raptor is designed to solve the 'memory wall' problem, which refers to the bottleneck in data movement that occurs in generative AI infrastructure."
lang: en
ref: 2026-10-13-D-Matrix-Raptor-3D-DRAM-Accelerator-for-Generative-Inference-at-Hot-Chips-2026
audio: 2026-10-13-D-Matrix-Raptor-3D-DRAM-Accelerator-for-Generative-Inference-at-Hot-Chips-2026.en.mp3
industry: creative
---

Imagine you are trying to find a very important book in a library. However, the book is in a deep basement warehouse, and the reading room is on the top floor. How exhausting would it be to climb the stairs dozens of times every time you want to borrow a book? The generative AI we use today is in a similar situation. The AI’s "brain"—its compute unit—suffers from a "memory bottleneck," wasting energy and slowing down as it fetches data from the warehouse (memory) where information is stored.

At the recent 'Hot Chips 2026' conference, semiconductor company d-Matrix unveiled an exciting technology to solve this dilemma: a 3D-DRAM accelerator called 'Raptor.' Now, AI no longer needs to run to a distant warehouse to find data. It is as if a bookshelf is attached right beneath the AI's brain.

## Why Is This Important?

When generative AI generates complex answers, it actually repeats the process of instantly retrieving vast amounts of data from memory and sending it to the compute unit. The movement of data during this process becomes a massive barrier that hinders AI performance. This is professionally referred to as the "Memory Wall." [Source: d-Matrix Raptor 3D-DRAM Architecture at Hot Chips 2026](https://www.partgenie.ai/insights/d-matrix-raptor-3d-dram-accelerator-for-generative-inference-at-hot-chips-2026-9)

To make the AI assistant features on our smartphones faster or to make AI services that generate complex videos in real-time more affordable, this wall must be torn down. Raptor was created precisely to break through that technical limitation. [Source: d-Matrix's Raptor puts stacked DRAM to work on inference bandwidth](https://runtimewire.com/article/d-matrix-raptor-stacked-dram-inference)

## Easy to Understand

To use a simple analogy, existing AI chips were like "a restaurant where the kitchen and the dining area are far apart." For a chef (compute unit) to cook, they had to walk a long distance to the ingredient warehouse (memory) to fetch items. In contrast, Raptor is like a "state-of-the-art open kitchen where the chef can retrieve ingredients from right next to them."

Raptor uses a method of attaching a compute die (semiconductor fragment) made with TSMC's 4-nanometer (nm) ultra-fine process directly onto custom DRAM. [Source: Hot Chips 2026: d-Matrix stacks AI accelerator directly on custom DRAM for 100 TB/s per card](https://www.tomshardware.com/tech-industry/semiconductors/d-matrix-stacks-its-ai-accelerator-directly-on-custom-dram-for-100-tbs-per-card) This is called a "3D-DRAM" structure. Because the memory is stacked vertically right beneath the compute unit, the physical distance the data must travel is extremely short. [Source: d-Matrix stacks DRAM directly · Hacker News | Zeli](https://zeli.app/story/49695065)

Thanks to this, Raptor provides a phenomenal data transfer bandwidth of 100 TB/s (terabytes per second) per card. This dramatically reduces the chronic bottleneck that typical AI chips suffer from. [Source: d-Matrix's Raptor 3D-DRAM Achieves SRAM-Class Bandwidth at 1/10th the HBM Power](https://wccftech.com/d-matrix-raptor-3d-dram-achieves-sram-class-bandwidth-at-1-10th-the-hbm-power/)

## Current Situation

According to a presentation at Hot Chips 2026 by Sudeep Bhoja, CTO of d-Matrix, this technology was developed in collaboration with Meta. [Source: Hot Chips 2026 - d-Matrix](https://www.d-matrix.ai/event/hot-chips-2026/) Current high-performance AI chips typically use expensive memory called HBM (High Bandwidth Memory), and a key feature of Raptor is that it can achieve similar or better performance with about 1/10th the power efficiency of HBM. [Source: d-Matrix's Raptor 3D-DRAM Achieves SRAM-Class Bandwidth at 1/10th the HBM Power](https://wccftech.com/d-matrix-raptor-3d-dram-achieves-sram-class-bandwidth-at-1-10th-the-hbm-power/)

However, this technology is not meant to replace all HBM on the market right away. Currently, Raptor is specialized for inference efficiency (the process where a trained AI actually generates answers), and it is expected to serve as a cornerstone of the entire AI infrastructure that handles massive data. [Source: d-Matrix's Raptor Chip Hits 105 TB/s in Real Silicon Tests, But It's Not an HBM Replacement Yet](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2p6bnJUdEVSRkNfcUU2bE9OWjlpZ0FQAQ?hl=en-PK&gl=PK&ceid=PK:en)

## What's Next?

We are moving away from an era of simply pouring in "more power" toward an era of accelerating AI through "more efficient structures." If 3D-DRAM technologies like Raptor become widespread, the response speed of the AI services you use will increase, while power consumption will decrease. This ultimately means the social cost required to run AI will be lowered. [Source: d-Matrix's Raptor 3D-DRAM Achieves SRAM-Class Bandwidth at 1/10th the HBM Power](https://wccftech.com/d-matrix-raptor-3d-dram-achieves-sram-class-bandwidth-at-1-10th-the-hbm-power/)

It is worth anticipating how much smaller and smarter the semiconductor industry will get in combining memory and compute units, and how far this new roadmap presented by Raptor will change the future of artificial intelligence.

## References

1. [d-Matrix Raptor 3D-DRAM Accelerator for Generative Inference](https://www.servethehome.com/d-matrix-raptor-3d-dram-accelerator-for-generative-inference-at-hot-chips-2026/)
2. [d-Matrix Raptor 3D-DRAM Architecture at Hot Chips 2026](https://www.partgenie.ai/insights/d-matrix-raptor-3d-dram-accelerator-for-generative-inference-at-hot-chips-2026-9)
3. [Hot Chips 2026 - d-Matrix](https://www.d-matrix.ai/event/hot-chips-2026/)
4. [Hot Chips 2026: d-Matrix stacks AI accelerator directly on custom DRAM for 100 TB/s per card](https://www.tomshardware.com/tech-industry/semiconductors/d-matrix-stacks-its-ai-accelerator-directly-on-custom-dram-for-100-tbs-per-card)
5. [Hot Chips 2026: d-Matrix Raptor 3D-DRAM - lukebest.github.io](https://lukebest.github.io/papers/hc2026-dmatrix-raptor-3d-dram)
6. [d-Matrix stacks DRAM directly · Hacker News | Zeli](https://zeli.app/story/49695065)
7. [D-Matrix Raptor 3D-DRAM Accelerator for Generative Inference at Hot Chips 2026](https://vk.ru/wall-238001969_5418)
8. [Hot Chips 2026 - Hot Chips 2026](https://hc2026.hotchips.org/?ref=vlsi.kr)
9. [d-Matrix Raptor: 3D-DRAM with 100 TB/s for AI inference](https://www.igorslab.de/en/d-matrix-raptor-3d-dram-over-100-tb-s-stacks-memory-beneath-compute-logic/)
10. [d-Matrix's Raptor 3D DRAM Achieves SRAM-Class Bandwidth at 1/10th the HBM Power](https://wccftech.com/d-matrix-raptor-3d-dram-achieves-sram-class-bandwidth-at-1-10th-the-hbm-power/)
11. [Jobs and Employment at d-Matrix | Simplify Jobs](https://simplify.jobs/c/d-Matrix)
12. [d-Matrix's Raptor 3D DRAM performance - Overview](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2p6bnJUdEVSRkNfcUU2bE9OWjlpZ0FQAQ?hl=en-PK&gl=PK&ceid=PK:en)
13. [d-Matrix's Raptor puts stacked DRAM to work on inference bandwidth](https://runtimewire.com/article/d-matrix-raptor-stacked-dram-inference)