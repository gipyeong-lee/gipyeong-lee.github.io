---
layout: post
title: "AI Coding Skills: Do We Need to Rethink the Test? OpenAI's Decisive Move"
description: "OpenAI has ceased recommending 'SWE-Bench Pro,' previously a standard for evaluating AI coding capabilities. The discovery of errors within the tasks themselves has raised red flags regarding the reliability of AI performance metrics."
summary: "OpenAI has discovered approximately 30% error rates in SWE-Bench Pro, a key benchmark for measuring AI coding skills, and has stopped recommending its use."
tags: [AI, Coding, Development, OpenAI, SWE-Bench]
image: 2026-07-09-OpenAI-no-longer-recommends-SWE-Bench-Pro.jpg
image_alt: "A warning sign symbolizing a test paper error floats above a background intertwined with code snippets and AI icons."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "As AI technology advances rapidly, the sophistication of the 'tests' used to measure it is failing to keep pace. We are entering an era where human developers must provide direct verification."
quiz:
  - question: "What is the primary reason OpenAI stopped recommending SWE-Bench Pro?"
    choices: ["Because the AI's skills are too good", "Because about 30% of the public tasks are incorrectly structured", "Because all AIs are already achieving perfect scores"]
    answer: 1
    explanation: "OpenAI stated that about 30% of the public tasks in SWE-Bench Pro do not function properly, leading to unreliable results."
  - question: "Why was SWE-Bench Verified discontinued first?"
    choices: ["Because the usage fee was too expensive", "Because there were not enough developers", "Due to data contamination and inherent flaws in the test questions themselves"]
    answer: 2
    explanation: "Along with data contamination issues, it was revealed that approximately 60% of the reviewed questions were structurally flawed, leading to its discontinuation."
  - question: "Which company developed SWE-Bench Pro?"
    choices: ["Google", "Scale AI", "Microsoft"]
    answer: 1
    explanation: "SWE-Bench Pro was developed by Scale AI and released in September 2025."
lang: en
ref: 2026-07-09-OpenAI-no-longer-recommends-SWE-Bench-Pro
audio: 2026-07-09-OpenAI-no-longer-recommends-SWE-Bench-Pro.en.mp3
industry: creative
---

Imagine you show up for a crucial math exam, only to find the answer key is wrong or the questions themselves are nonsensical. No matter how hard the student tries, they cannot receive an accurate assessment of their skills. The recent controversy surrounding "coding exams" in the AI industry is exactly like this.

OpenAI has actively recommended "SWE-Bench Pro" as a tool for measuring the software engineering capabilities of AI. However, OpenAI recently determined that approximately 30% of these test tasks are incorrectly structured, making it impossible to guarantee the reliability of the results. Consequently, they announced that it is no longer recommended as an official evaluation standard [Source 3, Source 11, Source 4].

### Why does this matter?

The smartphone apps, banking systems, and news services we use every day are all powered by code written by developers. Therefore, how well an AI can code is a critical metric that determines how smart the technology we encounter in our daily lives will become.

But what happens if the test questions used to measure this "coding skill" are useless? AI companies have been using these test scores to prove their models are superior. If the test itself is flawed, it could lead to distorted results, such as inflated performance claims or unfair assessments. This poses a significant risk of misleading consumers about the actual level of progress in the AI technology they use.

### Easy to understand: The secret of AI coding tests

Coding tests usually calculate scores through "Unit Tests" (automated checks that confirm whether the code correctly performs specific functions). For example, if the test asks the AI to "make it so that pressing this button changes the screen," the test is processed as correct if the AI writes the code and the test passes.

To use an analogy, imagine hosting a cooking competition where the judges decide to measure "soup thickness," only to realize their criteria is based on a broken thermometer. No matter how excellent the dish created by the chef (the AI), it's no different from measuring the skill as low due to a faulty thermometer, or conversely, giving high marks to a dish that shouldn't have been judged that way.

OpenAI previously used an evaluation tool called "SWE-Bench Verified." However, this was also discontinued after it was revealed that, along with data contamination issues, approximately 59% of the test questions had structural defects [Source 2, Source 8, Source 13, Source 9].

SWE-Bench Pro, for which recommendations have now been ceased, has also faced criticism that because it creates problems based on complex real-world issues from GitHub (a platform where developers share code), the nature of the tasks is too ambiguous and fragmented for an AI to solve on its own [Source 3, Source 14].

### Current situation: Finding a needle in a muddy field

AI models are currently advancing by leaps and bounds. However, the metrics used to measure their performance have not yet achieved the maturity suited for the "AI era" [Source 6, Source 14].

SWE-Bench Pro was released by a company called Scale AI in September 2025, and they attempted to minimize data contamination by applying stronger copyright licenses than before [Source 7, Source 8]. However, this announcement reveals how difficult it is to perfectly translate the complexity of a real-world development environment into an automated test, no matter how meticulously one tries to design it.

Bing Liu, research lead at Scale AI, noted that this decision well illustrates the limitations of relying solely on task ambiguity, data contamination, and narrow unit tests to perfectly measure AI skill [Source 14].

### What happens next?

The way we evaluate AI coding skills will undergo fundamental changes.

1. **More sophisticated evaluation standards**: Instead of simply relying on automated scores, the industry will strive to create new standards that can more comprehensively judge the "process" and "complexity" of how AI solves problems [Source 12].
2. **Emphasis on collaboration with developers**: Beyond just AI writing code alone, the method of evaluating how actual developers communicate with AI to solve problems will become more important.
3. **Continuous verification**: Managing evaluation data itself to prevent contamination will become a "basic science" area as important as developing the AI model itself.

We are now living in an era where AI writes its own code. However, this incident reminds us that creating the "thermometer" to accurately evaluate that capability is just as important a challenge as the technological advancement itself.

## References

1. [OpenAI Abandons SWE-Bench Verified, Citing Widespread Data Contamination and Flawed Tests](https://www.siliconreport.com/openai-abandons-swe-bench-verified-citing-widespread-data-contamination-and-flawed-tests-6ebd9b34)
2. [OpenAI Retracts Recommendation To Use SWE Bench Pro As Coding Eval Over 30% Broken Tasks](https://officechai.com/ai/openai-retracts-recommendation-to-use-swe-bench-pro-as-coding-eval-over-30-broken-tasks/)
3. [OpenAI no longer recommends SWE-Bench Pro as coding benchmarks saturate](https://savedelete.com/news/openai-swe-bench/)
4. [Why we no longer evaluate SWE-bench Verified - keynews.ai](https://keynews.ai/articles/290)
5. [OpenAI Drops SWE-Bench Verified: What It Means for AI](https://www.adwaitx.com/openai-swe-bench-verified-retired-ai-benchmarks/)
6. [OpenAI Abandons SWE-bench Verified: 59% Flawed Tests](https://byteiota.com/openai-abandons-swe-bench-verified-59-flawed-tests/)
7. [OpenAI Drops SWE-bench Verified Over Contamination Concerns](https://aibreakingwire.com/news/openai-ditches-swe-bench-verified-cites-critical-flaws/)
8. [OpenAI Retracts SWE-Bench Pro After Finding 30% of Tasks Broken | AlphaSignal](https://alphasignal.ai/news/openai-retracts-swe-bench-pro-after-finding-30-of-tasks-broken)
9. [OpenAI Developers on X](https://x.com/OpenAIDevs/status/2026002219909427270)
10. [OpenAI Abandons SWE-bench Verified After Finding 59% of Failed Tests Were Flawed](https://blockchain.news/news/openai-abandons-swe-bench-verified-contamination-flawed-tests)
11. [OpenAI moves beyond SWE-bench Verified as coding benchmarks saturate](https://tessl.io/blog/openai-moves-beyond-swe-bench-verified-as-coding-benchmarks-saturate/)