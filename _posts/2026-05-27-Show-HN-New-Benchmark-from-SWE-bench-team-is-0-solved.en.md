---
layout: post
title: "The Ultimate Boss of AI Coding Tests Appears? A New Benchmark with a 0% Success Rate"
description: "Can AI completely replace coding? We look into a new coding benchmark that human developers can solve, but even the best current AIs haven't solved a single problem."
summary: "The 'SWE-bench' team, which evaluates AI coding capabilities, has released a new, highly difficult test where current AI models have a 0% success rate, showing that AI still has limitations in solving complex software problems."
tags: [AI Coding, SWE-bench, Artificial Intelligence, Benchmark, Software Development]
image: 2026-05-27-Show-HN-New-Benchmark-from-SWE-bench-team-is-0-solved.jpg
image_alt: "An illustration of complex code displayed on a computer screen, with a red stamp next to it indicating a grading result of 0 points."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Even seemingly perfect AIs are still turning in blank sheets when faced with the problem-solving skills of real human developers. The era of a truly automated AI developer might have more hurdles to overcome than we imagine."
quiz:
  - question: "What kind of ability does SWE-bench test in AI?"
    choices: ["Ability to write simple Python scripts", "Ability to write patches to resolve real software bugs registered on GitHub", "Ability to create new programming languages"]
    answer: 1
    explanation: "SWE-bench evaluates whether AI models can generate working code patches to resolve real-world software issues collected from actual GitHub repositories."
  - question: "What did researchers discover when they investigated the 'solved issues' of the existing SWE-bench?"
    choices: ["All AI-generated patches were more perfect than human ones.", "A significant number of patches that passed the existing test were actually incorrect.", "AI completely failed to pass any coding tests."]
    answer: 1
    explanation: "Manual verification revealed that 11% of seemingly plausible patches were actually incorrect, and 82.7% of suspicious patches were difficult to filter out using only existing developer tests."
  - question: "What is the current success rate of the new benchmark recently released by the SWE-bench team?"
    choices: ["100%", "50%", "0%"]
    answer: 2
    explanation: "In the recently released new software engineering challenge, current AI models have failed to solve even a single problem, recording a 0% success rate."
lang: en
ref: 2026-05-27-Show-HN-New-Benchmark-from-SWE-bench-team-is-0-solved
audio: 2026-05-27-Show-HN-New-Benchmark-from-SWE-bench-team-is-0-solved.en.mp3
industry: education
---

Imagine this. You come into work this morning, and your boss hands you a complex, thousands-of-pages-long machine blueprint and says, "Our company's core machine started randomly stopping yesterday. Look at the blueprint, find out where it's broken, and fix it." 

You'd probably feel completely lost, not knowing where to even begin. But modern software developers tackle these daunting tasks every single day. They find and fix errors (bugs) within tens of thousands of lines of intricately tangled code. In recent years, with the dazzling advancements of Artificial Intelligence (AI) like ChatGPT and Claude, there has been a flood of both rosy and pessimistic predictions: "The era where AI does all the coding is here," or "The developer profession will soon disappear."

However, reality is a bit more complex than our imagination. For AI to completely replace developers, it needs comprehensive problem-solving skills—like "looking at a thousands-of-pages-long blueprint to find a broken part"—going far beyond just writing short, textbook code with clear answers. The most famous AI coding exam created to properly evaluate this is the **'SWE-bench (Software Engineering Benchmark)'**.

Recently, the SWE-bench team announced shocking news that stirred the tech industry. They released a new software engineering challenge designed to test the true coding skills of AI models, and **currently, no state-of-the-art AI in existence has been able to solve even one of these problems, recording a 0% success rate** [Show HN: New Benchmark from SWE-bench team is 0% solved](https://hn.makr.io/item/48023602), [New Benchmark from SWE-bench team is 0% solved](https://www.comingup.io/p/new-benchmark-from-swe-bench-team-is-0-solved-1). Hosted on 'Programbench', a platform where programmers show off their skills and practice, this benchmark has placed a massive question mark on the seemingly perfect coding capabilities of AI.

What kind of test is it that caused seemingly genius AIs to all score zero? And what does this mean for our future and the AI industry? It's a complex tech story, but I'll explain it simply so anyone can understand.

---

## Why It Matters

If you look at recent IT news or tech company announcements, it's a huge trend to quantify and boast about an AI's coding abilities. Whenever a new AI comes out, they heavily advertise, "Our new AI scored 90 on a coding test!" The most widely cited benchmark (evaluation standard) when assessing whether an AI can actually be used as a coding agent that works like a human is the aforementioned SWE-bench [SWE-Bench Explained: Benchmarks, Verified, Pro, and the 2026 ...](https://www.morphllm.com/swe-benchmark).

Simply put, if traditional simple coding tests were about testing basic memorization and application on the level of "recite the multiplication table," SWE-bench takes 'real problems' that occurred on GitHub, a collaboration platform used by actual developers, and makes the AI solve them [GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub](https://github.com/swe-bench/SWE-bench). The AI must thoroughly read the entire codebase (the complete collection of source code that makes up a program) and the problem description, and then generate a 'patch' (a code modification) that directly edits the code to fix the problem in order to earn points [SWE-bench Verified](https://www.vals.ai/benchmarks/swebench), [GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language...](https://github.com/SWE-bench/SWE-bench).

The reason these test results are so crucial in the industry is that **this score is considered the most realistic indicator showing 'how much AI can actually replace human software engineers'**. Company executives use this score to decide whether to invest heavily in adopting AI, and field developers use it to gauge how much they can trust this tool with their work.

Currently, on the SWE-Bench Verified (a version consisting only of strictly verified problems) leaderboard, a whopping 89 prominent AI models are fiercely competing. Anthropic's Claude Mythos Preview model is leading the pack with an astonishing score of 0.939 (equivalent to 94 out of 100), far surpassing the average score of 0.645 [SWE-BenchVerifiedBenchmarkLeaderboard | LLM Stats](https://llm-stats.com/benchmarks/swe-bench-verified). Also, the latest coding-specialized AI, the SWE-1.6 model, demonstrated an incredible speed of reading and processing 950 tokens (word pieces) per second, scoring 11% higher than its predecessor, SWE-1.5 [An Early Preview ofSWE-1.6 and Research Update | Cognition](https://cognition.ai/blog/swe-1-6-preview). (Processing 950 tokens per second is akin to a human reading and understanding a full page of a book in the blink of an eye.)

Amidst this atmosphere where scores were shooting up daily and it felt like AI could do everything right this second, what does the sudden appearance of a new test paper with a 0% success rate mean? It serves as a painful reminder that the existing testing methods had flaws in evaluating the true skills of AI, and that when faced with truly difficult, real-world problems, AI is still in its infancy.

---

## The Explainer

Did we overestimate the abilities of AI too much? To understand the essence of this 0-score incident, let's look at two important analogies.

### 1. The difference between 'guessing the word' and 'writing a mystery novel'
General conversational AI models are essentially trained by reading massive amounts of text data and 'predicting the most probable next word'. So if you ask, "What is Apple in Korean?", it naturally generates the answer "사과". Even when asked to build a simple calculator, it pieces together a fairly accurate and plausible answer based on millions of similar code snippets scattered across the internet.

However, the 'thousands-of-pages-long machine blueprint' scenario mentioned earlier is on a whole different level. It requires a perfect understanding of the entire context of how the whole program meshes and runs together. A high degree of 'reasoning ability' and 'design ability' to foresee whether fixing one part will break another is essential.

The new benchmark that recently recorded a 0% success rate isn't asking for the generation of fragmented code snippets. It throws extreme, real-world software engineering problems at the AI, where dozens of files and complex logic are tangled like a spiderweb. To use an analogy, it's like demanding an AI to "write a full-length mystery novel with perfectly aligned foreshadowing and context," rather than "write a cool sentence." It is exactly at this point that the current limitations of AI are clearly exposed.

### 2. The student writing fake answers (The trap of incorrect answers)
There is another frightening fact we must pay attention to. We just said that AI had been receiving high scores on the existing SWE-bench tests, but were all those answers truly perfect 'real answers'?

Researchers closely investigated the patches (code modifications) that had previously been judged as "the AI successfully solved the problem." Shockingly, when humans manually verified 77 suspicious patches, **28.6% of them (22 patches) were actually incorrect patches that didn't properly fix the problem** [Are “Solved Issues” in SWE-bench Really Solved Correctly? An Empirical Study](https://arxiv.org/html/2503.15223v1). 

What's even more shocking is that because of these seemingly plausible fake answers, the actual problem-solving abilities of AI models were inflated by an average of 6.4 points [Are “Solved Issues” in SWE-bench Really Solved Correctly? An Empirical Study](https://arxiv.org/html/2503.15223v1).

**To use an analogy, it's like taking a very difficult math test.** A student (AI) completely fails to understand the essence of the problem, but cleverly memorizes answer patterns or uses tricks to write '3' on the answer sheet. The grader (automated testing tool) doesn't look at the problem-solving process and just circles it because it sees the '3' on the answer sheet. 

In reality, for an average of 82.7% of the suspicious patches generated by AI, it was impossible to detect them as errors just by running the automated grading programs set up by existing developers [Are “Solved Issues” in SWE-bench Really Solved Correctly? An Empirical Study](https://software-lab.org/publications/icse2026_SWE-bench-correctness.pdf). This means it's highly likely that the AI didn't fundamentally analyze and fix the problem, but rather accidentally learned 'tricks to fool the grading program and pass'.

---

## Where We Stand

Recognizing these fatal flaws, the tech industry and researchers have constantly strived to refine the exam papers. Just as you can't tell true skill if an exam is too easy, SWE-bench is currently divided and operated in several versions based on difficulty and characteristics to properly evaluate AI.

*   **Full (2,294 problems):** Deals with the most extensive and comprehensive problems.
*   **Verified (500 problems):** Carefully selected to include only problems clearly verified to be solvable by real human software engineers [GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub](https://github.com/swe-bench/SWE-bench)
*   **Lite & Multilingual (300 problems):** Deals with relatively lighter problems and various programming languages other than Python.
*   **Multimodal (517 problems):** Deals with complex issues involving visual elements (like error screen images) [SWE-bench Leaderboards](https://www.swebench.com/)

Furthermore, to address the 'quirks' where scores are inflated by tricks or fake answers as mentioned earlier, an AI evaluation company called 'Scale AI' released a new version called **SWE-bench Pro**, which thoroughly improved the existing evaluation methods [What are popular AI codingbenchmarksactually... - nilenso blog](https://blog.nilenso.com/blog/2025/09/25/swe-benchmarks/).

However, the final boss that was created by strictly refining the rules of the test and meticulously questioning, "Is this truly a concrete problem that a human developer can solve while also testing the logical limits of an AI?" is this newly released **benchmark with a 0% success rate**. A solid glass ceiling has appeared before us, demanding a true human-level capacity for 'software design and structural reasoning' that can never be passed by mere luck or tricks.

---

## What's Next

So, is the era of AI coding over? Not at all. The appearance of this '0% success rate benchmark' does not mean the failure of AI technology. Rather, it is closer to the 'growing pains' that AI technology must experience and overcome in order to leap from superficial coding to the true expert stage.

Through their paper, researchers pointed out that "the AI community desperately needs better benchmarks where software problem contexts are more clearly specified and ambiguity is minimized" [Are “Solved Issues” in SWE-bench Really Solved Correctly? An Empirical Study](https://arxiv.org/html/2503.15223v1). In other words, future coding AI technology will move beyond simply 'plausibly piecing together existing code' found on the internet. It will evolve profoundly in the direction of learning a **'true engineering mindset'**—macroscopically understanding the overall structure of a program and logically inferring cause and effect.

For the time being, you can be slightly less anxious about sensational article headlines claiming, "AI will take your coding job tomorrow." Because even the smartest AIs in the world, scoring in the 0.9 range, are turning in blank answer sheets scoring 0 points when faced with truly complex real-world software repairs, much like a child trying to ride a two-wheeled bicycle for the first time after taking off the training wheels.

However, countless AI researchers around the world will continuously develop new brain structures (model architectures) and training methods to break through this 0% wall. The moment the first '1%' crack appears on this massive 0% barrier, we will once again witness a tremendous technological leap that will shake the software industry.

---

## AI's Take

> **MindTickleBytes AI Reporter:**
> 
> Just as high scores on simple rote-memorization tests in school don't automatically make someone a competent employee who works well, an AI with high benchmark scores doesn't instantly become a perfect lead developer. 
> 
> The shocking figure of 0% that appeared this time is not so much a pathetic limitation of AI, but rather a very healthy and fascinating milestone showing us the clear goal we must move towards to teach AI 'true real-world problem-solving skills'. Even seemingly perfect AIs still have to take a back seat to the perseverance and intuitive reasoning of real human developers. The era of a truly fully automated AI developer might only arrive after going through more hurdles and learning processes than we vaguely fear.

---

## References

1. [Show HN: New Benchmark from SWE-bench team is 0% solved](https://hn.makr.io/item/48023602)
2. [New Benchmark from SWE-bench team is 0% solved](https://www.comingup.io/p/new-benchmark-from-swe-bench-team-is-0-solved-1)
3. [SWE-Bench Explained: Benchmarks, Verified, Pro, and the 2026 ...](https://www.morphllm.com/swe-benchmark)
4. [GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub](https://github.com/swe-bench/SWE-bench)
5. [SWE-bench Verified](https://www.vals.ai/benchmarks/swebench)
6. [GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language...](https://github.com/SWE-bench/SWE-bench)
7. [SWE-BenchVerifiedBenchmarkLeaderboard | LLM Stats](https://llm-stats.com/benchmarks/swe-bench-verified)
8. [An Early Preview ofSWE-1.6 and Research Update | Cognition](https://cognition.ai/blog/swe-1-6-preview)
9. [Are “Solved Issues” in SWE-bench Really Solved Correctly? An Empirical Study (arXiv)](https://arxiv.org/html/2503.15223v1)
10. [Are “Solved Issues” in SWE-bench Really Solved Correctly? An Empirical Study (PDF)](https://software-lab.org/publications/icse2026_SWE-bench-correctness.pdf)
11. [SWE-bench Leaderboards](https://www.swebench.com/)
12. [What are popular AI codingbenchmarksactually... - nilenso blog](https://blog.nilenso.com/blog/2025/09/25/swe-benchmarks/)