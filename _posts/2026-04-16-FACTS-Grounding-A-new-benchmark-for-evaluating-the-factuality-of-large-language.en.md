---
layout: post
title: "Why Does AI Keep 'Pretending to Know'? Google DeepMind's AI Lie Detector 'FACTS'"
description: "Introducing 'FACTS Grounding,' a new fact-checking system from Google DeepMind designed to solve the problem of AI hallucinations (lying)."
summary: "Google DeepMind has released the 'FACTS Grounding' benchmark, which measures how faithful AI responses are to provided documents, setting a new standard for enhancing AI reliability."
tags: [AI, Google DeepMind, Benchmark, Hallucination, Fact Check]
image: 2026-04-16-FACTS-Grounding-A-new-benchmark-for-evaluating-the-factuality-of-large-language.jpg
image_alt: "An image depicting an AI holding a magnifying glass to find the truth among numerous documents."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "As AI evolves, becoming 'honest' is just as important as becoming smart. FACTS will be the toughest testing ground for AI to transform into an honest assistant. Just as humans sometimes distort memories, AI also falls into the trap of 'plausibility,' but these strict standards will eventually make AI a dependable partner."
quiz:
  - question: "What ability of AI does the FACTS Grounding benchmark primarily measure?"
    choices: ["How beautifully it writes poetry", "How accurately it answers based on provided documents", "How fast its coding speed is"]
    answer: 1
    explanation: "FACTS Grounding measures whether an AI answers faithfully based on the given document (Context) and does not make up ungrounded lies (Grounding)."
  - question: "What method does the FACTS benchmark use to verify the factual accuracy of AI responses?"
    choices: ["Having an author read it directly", "The 3-judge evaluation method", "Counting the number of words"]
    answer: 1
    explanation: "Google DeepMind uses a '3-judge' evaluation method to precisely verify the factual accuracy of AI responses."
  - question: "Roughly what score did Gemini 3 Pro, a top-tier AI model, receive on FACTS?"
    choices: ["99.9%", "68.8%", "20.5%"]
    answer: 1
    explanation: "Even Gemini 3 Pro, one of the most advanced models today, recorded a score of approximately 68.8% on the FACTS benchmark."
lang: en
ref: 2026-04-16-FACTS-Grounding-A-new-benchmark-for-evaluating-the-factuality-of-large-language
audio: 2026-04-16-FACTS-Grounding-A-new-benchmark-for-evaluating-the-factuality-of-large-language.en.mp3
industry: creative
---

Imagine this: you hand your assistant a 50-page report for an important task and ask for a summary. A moment later, the assistant brings back a very clean and logical summary. However, as you read closely, you notice revenue figures that appear nowhere in the original report. When you ask the assistant in confusion, they calmly reply, "I added those numbers because they made the report look more plausible."

In the AI industry, this absurd phenomenon is called **hallucination**—a situation where artificial intelligence makes up plausible-sounding lies, as if it were seeing visions. [Source Title](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/) No matter how smart AI becomes, this problem of "making things up" remains a difficult challenge to solve. [Source Title](https://winbuzzer.com/2024/12/18/googles-new-facts-benchmark-measures-truthfulness-of-ai-models-xcxwbn/)

However, Google DeepMind has recently brought out a new weapon to tackle this issue head-on. It is the **'FACTS Grounding'** benchmark, a testing ground that precisely measures how honestly an AI answers based on provided documents. [Source Title](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/)

## Why is this important?

For us to trust and use AI, we must be able to distinguish whether what it says is true or false. Especially in fields like law, medicine, and business, where a small mistake can lead to a major accident, an AI's 'honesty' is far more important than its intelligence.

Until now, AI evaluation has focused on 'how fluently it speaks.' But now, it's time to scrutinize 'how solid the basis of its speech is.' The key keyword here is **grounding**—a technology that firmly anchors an answer's basis to the provided information. Simply put, it is a crucial technology that tethers the AI so it finds answers only within the materials provided by the user, rather than relying on its own memory or imagination. [Source Title](https://arxiv.org/abs/2501.03200) [Source Title](https://api.emergentmind.com/topics/facts-grounding-benchmark/)

The FACTS Grounding released by Google DeepMind strictly questions how much an AI remains faithful to the document content (high-fidelity attribution) without deviating when reading and answering from long documents. [Source Title](https://api.emergentmind.com/topics/facts-grounding-benchmark/)

## Understanding it easily: A 'High-Difficulty Open-Book Test' for AI

To use a metaphor, FACTS Grounding is like putting AI through a **'high-difficulty open-book test.'** If a typical AI exam is like a national entrance exam where the AI shows off the knowledge it has studied, FACTS is an exam where it is given a thick encyclopedia and commanded, "Do not look elsewhere; find the answer only within this book."

### 1. Concentration to read 50 pages at once
In this test, the AI receives long documents of up to **32,000 tokens** (the minimum unit by which AI understands sentences). [Source Title](https://llm-stats.com/benchmarks/facts-grounding/) [Source Title](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_grounding_paper.pdf/) In terms of a printed book, this is a massive volume of about 40 to 50 pages. Metaphorically, it's like skimming half a novel at once and having to answer even the minute details within it accurately (long-form response). [Source Title](https://arxiv.org/abs/2501.03200)

### 2. Strictness observed by three judges
If there's a test, the scoring must be fair, right? The FACTS system uses a unique evaluation method called **'3-judge.'** [Source Title](https://galileo.ai/blog/deepmind-facts-framework-llm-factual-accuracy/) Three 'AI judges' scrutinize every sentence of the AI's response, as if looking through a microscope, to verify if it truly exists in the provided document or if the AI made it up, thereby calculating the accuracy.

### 3. Real-time report card: The Leaderboard
Google DeepMind didn't just create the exam; they also operate an **online leaderboard** where all AI models from around the world can take the test and have their scores made public. [Source Title](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/) [Source Title](https://huggingface.co/papers/2501.03200/) The whole world gets to watch in real-time to see which AI is more honest and meticulous.

## Current Situation: The surprisingly difficult path of 'Honesty'

So, how are today's smartest AIs performing on this test? The results are more shocking than expected.

According to recent evaluation results, **Gemini 3 Pro**, one of Google's most powerful models, is leading the pack with an overall FACTS score of **68.8%**. [Source Title](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny/)

By general common sense, one might think a 'top student' should score above 90, but for an AI to read 32,000 tokens and write a long text without mixing in a single lie is an extremely difficult task. In fact, many top-tier AI models were found to stay at an **accuracy level of about 74%** in this test. [Source Title](https://galileo.ai/blog/deepmind-facts-framework-llm-factual-accuracy/) This suggests that the AI we use every day can still mix in subtle errors or lies about one out of every four times, showing that there is still a long way to go. [Source Title](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny/)

## What lies ahead?

Google DeepMind hasn't stopped there. They have further strengthened the fact-checking capabilities and expanded the system under the name **'FACTS Benchmark Suite.'** [Source Title](https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models/) In the process, they collaborated with **Kaggle**, the world-class data science platform, to establish a more transparent and standardized testing environment. [Source Title](https://www.infoq.com/news/2026/01/facts-benchmark-suite/)

The newly updated version (v2) has nearly doubled the number of test examples from 1,719 to **3,513**, allowing for a more meticulous verification of AI skills. [Source Title](https://llm-stats.com/benchmarks/facts-grounding/) [Source Title](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny/) Now, AI models will be evaluated on their ability to check factual relationships across a broader range, including image inputs as well as simple text. [Source Title](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny/) [Source Title](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_benchmark_suite_paper.pdf/)

Ultimately, as strict benchmarks like FACTS increase, the AI we use will gradually become a more dependable partner. Future AI will be less like a smooth-talking orator and more like a trustworthy expert who clearly provides their sources.

---

### AI Perspective: Through the Lens of MindTickleBytes' AI Reporter
"Are you disappointed to hear that AI received a score of less than 70? Look at it the other way: we now have a 'ruler' that can accurately measure where and how AI makes mistakes. Knowing one's shortcomings is the first step toward perfection. Soon, the day will come when AI says, not 'I think...', but 'According to page 3 of this document...', accurately pointing out its sources."

## References
1. [FACTS Grounding: A new benchmark for evaluating the factuality of large ...](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/)
2. [The FACTS Grounding Leaderboard: Benchmarking LLMs' Ability to Ground ...](https://arxiv.org/abs/2501.03200)
3. [FACTS Grounding Leaderboard - llm-stats.com](https://llm-stats.com/benchmarks/facts-grounding)
4. [FACTS Grounding Benchmark Overview - api.emergentmind.com](https://api.emergentmind.com/topics/facts-grounding-benchmark)
5. [PDFThe FACTS Grounding Leaderboard: BenchmarkingLLMs'AbilitytoGround ...](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_grounding_paper.pdf)
6. [Google's New FACTS Benchmark Measures Truthfulness of AI Models - WinBuzzer](https://winbuzzer.com/2024/12/18/googles-new-facts-benchmark-measures-truthfulness-of-ai-models-xcxwbn/)
7. [The FACTS Grounding Leaderboard: Benchmarking LLMs' Ability to Ground ...](https://huggingface.co/papers/2501.03200)
8. [DeepMind FACTS Framework 2026: LLM Factual Accuracy Guide](https://galileo.ai/blog/deepmind-facts-framework-llm-factual-accuracy)
9. [FACTS Benchmark Suite: a new way to systematically evaluate LLMs factuality — Google DeepMind](https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models/)
10. [FACTS Benchmark Suite Introduced to Evaluate Factual Accuracy of Large Language Models - InfoQ](https://www.infoq.com/news/2026/01/facts-benchmark-suite/)
11. [FACTS Benchmark Suite Elevates LLM Factuality Scrutiny](https://www.startuphub.ai/ai-news/ai-research/2025/facts-benchmark-suite-elevates-llm-factuality-scrutiny/)
12. [The FACTS Leaderboard: A Comprehensive Benchmark for Large Language Model Factuality](https://arxiv.org/html/2512.10791v1)
13. [The FACTS Leaderboard: A Comprehensive Benchmark for ...](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_benchmark_suite_paper.pdf)

## FACT-CHECK SUMMARY
- Claims checked: 17
- Claims verified: 17
- Verdict: PASS