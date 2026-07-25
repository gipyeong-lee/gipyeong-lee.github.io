---
layout: post
title: "AI Running at Full Speed on My Computer? Exploring the World of Local AI with Qwen 3.6 35B MoE"
description: "We explain how to use local AI, along with performance test results from running the high-performance Qwen 3.6 35B MoE model directly on an RTX 3090 graphics card."
summary: "Running the Qwen 3.6 35B-A3B model on an RTX 3090 can generate over 100 tokens per second, offering a much faster experience than standard 27B dense models."
tags: [AI, LocalLLM, Qwen, RTX3090, Hardware]
image: 2026-07-25-Benchmarking-Qwen-36-35B-MoE-3B-active-on-an-RTX-3090.jpg
image_alt: "Measuring the performance of the Qwen 3.6 AI model running on an RTX 3090 graphics card."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Running large-scale models efficiently in a local environment offers tremendous advantages in terms of data privacy and cost. In particular, leveraging an MoE structure allows for cleverly overcoming hardware limitations."
quiz:
  - question: "Why is an MoE (Mixture-of-Experts) structured model faster than a standard dense model?"
    choices: ["Because it uses all parameters at all times", "Because it only processes about 3B (3 billion) active parameters at a time", "Because it contains code optimized specifically for the RTX 3090"]
    answer: 1
    explanation: "MoE models only operate by selecting a subset of experts (parameters) from the entire model, so even a 35B-sized model uses only about 3B active parameters, resulting in faster computation speeds [Source 5]."
  - question: "What is the performance when running the Qwen 3.6 35B-A3B model on an RTX 3090?"
    choices: ["5 to 10 tokens per second", "50 to over 100 tokens per second", "Over 1,000 tokens per second"]
    answer: 1
    explanation: "While it depends on the settings, it shows generation speeds of 50 to over 100 tokens per second [Source 2], [Source 5], [Source 7]."
  - question: "If you had to choose between a higher-performance 27B dense model and a 35B-A3B MoE model?"
    choices: ["The 35B model is always superior", "The 27B dense model is recommended if answer quality is important", "There is no difference in performance at all"]
    answer: 1
    explanation: "The 27B dense model is 1–10 points ahead of the MoE model in benchmark results, so it is recommended when answer quality is a priority [Source 3]."
lang: en
ref: 2026-07-25-Benchmarking-Qwen-36-35B-MoE-3B-active-on-an-RTX-3090
audio: 2026-07-25-Benchmarking-Qwen-36-35B-MoE-3B-active-on-an-RTX-3090.en.mp3
industry: education
---

Imagine this: The AI assistant on the computer you use every day can answer complex questions in a single second, without even an internet connection. Having your own "personal AI" that runs safely inside your computer, without worrying about data leaks, is no longer just a story from science fiction movies. Here, we explain in simple terms—easy enough for a high school student to understand—how the recently released, powerful AI model 'Qwen 3.6 35B-A3B' is making this a reality.

### Why It Matters

In the past, high-performance AI models were so bulky that running them on a typical user's computer was nearly unthinkable. But now, the situation has changed. With the rapid advancement of 'Local AI' (AI that works directly on the user's device without an internet connection), you can sufficiently experience high-level AI just by using a graphics card like the RTX 3090 at home [Source 8].

Local AI is gaining attention for two main reasons. First is **privacy**. Your data is processed entirely within your computer without leaving for an external server, providing much greater peace of mind. Second is **speed and cost-effectiveness**. Since it is not affected by internet speed, there are no lags, and once you download the model, you can use it to your heart's content without additional costs. The Qwen 3.6 35B-A3B model tested here is garnering significant interest for showing particularly excellent cost-effectiveness and performance in such local AI environments [Source 6].

### The Explainer

The core of the Qwen 3.6 35B-A3B model lies in a special design called **MoE (Mixture-of-Experts)**.

Let's use an analogy. Imagine you run a massive library, but it's too hard for one librarian to manage every single book. So, you hire several experts, each specializing in a different field. Here, '35B' represents the total number of librarians (total parameters), and '3B active' refers to the number of librarians actually called upon to find an answer when a question comes in (active parameters) [Source 5].

While a standard 'Dense Model' is a structure where every librarian works every time, an MoE model only engages the experts in the field relevant to the question. Thanks to this, the model is as smart as a model with 35 billion parameters, but since it only needs to calculate for about 3 billion parameters when doing the actual thinking, it can deliver results very quickly [Source 5].

### Where We Stand

Recent benchmark test results conducted on an actual RTX 3090 graphics card are surprising.

* **Speed**: When a specific setting (UD-Q4_K_XL quantization) is applied, it generates approximately 101.7 tokens (the unit AI uses to create text) per second for short questions, and 80.9 tokens per second for longer ones [Source 7]. It consistently maintains a level of 50–100 tokens per second in other environments as well, which is much faster than a 27B dense model (approx. 35 tokens per second) [Source 5].
* **Limitations**: Of course, a bigger and faster MoE model isn't always the correct answer. Compared to the 27B dense model, the 27B dense model shows benchmark results that are 1–10 points higher in terms of answer accuracy (quality) [Source 3]. In other words, it is wise to choose the MoE model if speed is most important, and the dense model if the quality of the answer is the priority [Source 3].
* **Optimization**: Additionally, it was confirmed that 'Speculative Decoding,' one of the AI learning techniques, is unexpectedly not very helpful for speed improvement in environments like the RTX 3090 [Source 4].

### What's Next

Moving forward, local AI technology will become even lighter and smarter. Experts who conducted these tests are sharing various configuration methods that allow users to efficiently run models tailored to their PC's specifications [Source 3], [Source 11]. Users are now entering an era where they go beyond simply choosing a good model and are tuning their own AI environments by selecting the optimal 'quantization' (a technique that reduces size by adjusting data precision) level suited to their graphics card's performance [Source 2], [Source 14].

### MindTickleBytes AI Reporter's Opinion

Local AI is a process of reclaiming 'sovereignty over my device' beyond mere technological achievement. The emergence of efficient models like Qwen 3.6 35B-A3B is rapidly bringing about a future where anyone can enjoy high-performance AI on their PC without expensive servers. AI is becoming a presence that breathes with you on your desk-top computer, rather than being on a distant giant corporate server.

## References

1. [Qwen/Qwen3.6-35B-A3B · My RTX 3090 ran out of excuses: Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B/discussions/37)
2. [Qwen 3.6-35B-A3B Local Hardware Guide — GPU & VRAM (2026) | Compute Market](https://www.compute-market.com/blog/qwen-3-6-local-hardware-guide-2026)
3. [GitHub - tfriedel/qwen3.6-rtx3090-lab: Benchmarks, compose files, and findings for running Qwen3.6 (27B dense + 35B-A3B MoE) on 4× RTX 3090](https://github.com/tfriedel/qwen3.6-rtx3090-lab)
4. [GitHub - thc1006/qwen3.6-speculative-decoding-rtx3090](https://github.com/thc1006/qwen3.6-speculative-decoding-rtx3090)
5. [Best Way to Run Qwen 3.6 35B MoE Locally: VRAM, Speed, Setup | InsiderLLM](https://insiderllm.com/guides/best-way-run-qwen-3-6-35b-moe-locally/)
6. [I Benchmarked Qwen3.6–35B-A3B Model on 3090, 4090, 5090 and M5 Max. Here’s What Nobody Tells You. | Medium](https://medium.com/@ttio2tech_28094/i-benchmarked-qwen3-6-35b-a3b-model-on-3090-4090-5090-and-m5-max-heres-what-nobody-tells-you-62fbb2f4e64a)
7. [Qwen 3.6 Complete Guide: 27B Dense, 35B-A3B MoE, and Which to Use | InsiderLLM](https://insiderllm.com/guides/qwen-3-6-local-ai-guide/)
8. [Benchmarking Qwen 3.6 35B MoE (3B active) on an RTX 3090](https://www.gilesthomas.com/2026/07/benchmarking-qwen-3-6-35b-moe-rtx-3090)
9. [From 25 to 283 tok/s: Serving Qwen3.6 on Dual RTX 3090s](https://alexander-ollman.github.io/qwen3.6-on-rtx3090/qwen3.6-on-rtx3090.html)
10. [Qwen3.614B A3BFableVibes benchmarked and tested vs... - YouTube](https://www.youtube.com/watch?v=DBEd5dpxaNQ)
11. [Qwen/Qwen3.6-35B-A3B· Hugging Face](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)
12. [Qwen3.635B-A3BonRTX3060 12GB: Local LLM | SpecPicks](https://specpicks.com/reviews/qwen-36-35b-a3b-rtx-3060-12gb-local-2026)
13. [ЗапускаемQwen3.635B-A3B+ opencode локально наRTX... / Хабр](https://habr.com/ru/articles/1026482/)
14. [Qwen3.627B vs35B-A3BMoEMTP наRTX5080 16GB... | AiManual](https://ai-manual.ru/article/rtx-5080-16gb-qwen36-27b-mtp-ili-35b-a3b-moe-mtp---chto-vyibrat-dlya-lokalnogo-kodinga/)