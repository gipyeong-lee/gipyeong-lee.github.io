---
layout: post
title: "Did Claude Suddenly Get 'Dumb'? The Truth Behind the Scorecard Dropping from 83% to 68%"
description: "An easy-to-understand explanation of the performance decline controversy for Claude 4.6 and the results of the BridgeBench hallucination test."
summary: "Reports of Claude 4.6's code analysis accuracy plummeting from 83% to 68% have sparked 'AI performance degradation' debates, though experts are questioning the validity of the testing methodology."
tags: [Claude, Artificial Intelligence, Hallucination, AI News, BridgeBench]
image: 2026-05-05-Claude-Opus-46-accuracy-on-BridgeBench-hallucination-test-drops-from-83-to-68.jpg
image_alt: "A robot looking troubled in front of a chart with a downward-trending line"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI performance is not a constant; it fluctuates based on environment and prompting. This controversy illustrates the inherent 'difficulty of measurement' behind the data."
quiz:
  - question: "What was the specific drop in accuracy for Claude 4.6 that recently sparked controversy?"
    choices: ["From 90% to 70%", "From 83.3% to 68.3%", "From 50% to 30%"]
    answer: 1
    explanation: "According to the BridgeBench report, Claude 4.6's accuracy dropped from 83.3% to 68.3%."
  - question: "What is the term for the phenomenon where an AI presents false information as if it were a fact?"
    choices: ["Deepfake", "Hallucination", "Data Mining"]
    answer: 1
    explanation: "When an AI makes up non-existent facts and presents them as true, it is called a hallucination."
  - question: "What evidence did some experts use to argue against the claims of performance degradation?"
    choices: ["The AI was 'hungry'", "Changed test questions or AI's non-determinism", "Claude was never good at coding"]
    answer: 1
    explanation: "Critics pointed to the possibility that the question set changed for the re-test or cited the non-determinism of AI, where results vary each time it is run."
lang: en
ref: 2026-05-05-Claude-Opus-46-accuracy-on-BridgeBench-hallucination-test-drops-from-83-to-68
audio: 2026-05-05-Claude-Opus-46-accuracy-on-BridgeBench-hallucination-test-drops-from-83-to-68.en.mp3
industry: education
---

What if one day your trusted best friend suddenly started saying complete nonsense? What if a friend who solved complex math problems effortlessly until yesterday suddenly failed at simple multiplication, or even started making up non-existent facts with a serious face? This is exactly the kind of heated controversy currently surrounding Anthropic's AI model, 'Claude Opus 4.6,' which has been gaining popularity for its unparalleled intelligence.

The situation became more complex when reports emerged claiming that users' vague suspicions—that "Claude seems dumber than before"—were proven by actual numbers. [Source 2] [Viral BridgeBench Post Claims Claude Opus 4.6 Was ‘Nerfed,’ Critics Call It Bad Science](https://tech.yahoo.com/ai/claude/articles/viral-bridgebench-post-claims-claude-131318087.html) MindTickleBytes takes a detailed look at why Claude 4.6's scorecard suddenly dropped and whether this truly means the AI has gotten worse or if it's a simple misunderstanding.

## Why Does This Matter?

Imagine there is an expert who reviews blueprints when you build a house. What would happen if that expert, who used to find every defect perfectly, suddenly gave wrong advice like, "It's safe to remove this pillar"?

We have begun to think of AI not just as a toy for killing time, but as a 'partner' we work with. Especially for developers, Claude has been a reliable assistant that reviews complex code and finds errors. If this assistant suddenly starts 'lying,' it's a major problem.

At the center of this controversy is **Hallucination**. Put simply, it refers to the phenomenon where an AI makes up plausible-sounding but false information as if it were a fact, even when it doesn't know the answer. If an AI shows hallucination symptoms by saying, "This code is perfect, deploy it immediately," even though there is a fatal security error, it could lead to a major accident that shuts down the entire service. [Source 12] [Debugging Opus 4.6: Why Claude Code's Reasoning Depth Dropped 67% and ...](https://discuss.huggingface.co/t/debugging-opus-4-6-why-claude-codes-reasoning-depth-dropped-67-and-what-to-do-about-it/175236) Therefore, the news that Claude's accuracy plummeted from the 80% range to the 60% range has come as a state of emergency—a 'crisis of trust'—to everyone who uses AI as a tool. [Source 8] [Claude Opus 4.6 Accuracy Slips in Hallucination Benchmark](https://www.knowai.space/en/news/claude-opus-hallucination-benchmark-analysis)

## Easy Understanding: AI's 'Scorecard' Incident

To understand this controversy, you first need to know about a test called **BridgeBench**. BridgeBench is a kind of 'AI morality and skill exam' that measures how honestly an AI answers without lying (hallucinating) when analyzing complex code. It consists of a total of 30 complex tasks and 175 sophisticated questions, strictly verifying whether the AI's answers exactly match the results of running the code on an actual computer. [Source 12] [Debugging Opus 4.6: Why Claude Code's Reasoning Depth Dropped 67% and ...](https://discuss.huggingface.co/t/debugging-opus-4-6-why-claude-codes-reasoning-depth-dropped-67-and-what-to-do-about-it/175236)

Shall we compare this situation to school life? Imagine a top student who was the talk of the school after ranking 2nd (83.3 points) in last month's finals, suddenly seeing their grades plummet to 10th (68.3 points) in an exam held this month. [Source 11] [BridgeBench Claim Claude Opus 4.6 'Nerfed' Criticized](https://blockport.io/latest-news/bridgebench-claim-claude-opus-4-6-nerfed-criticized/) According to the results released by BridgeMind, the team operating BridgeBench, Claude 4.6's scorecard has dropped surprisingly:

*   **Accuracy**: 83.3% → 68.3% (approx. 15% drop) [Source 2, Source 12]
*   **Ranking**: 2nd overall → 10th (pushed from the top tier to the middle) [Source 4, Source 11]
*   **Fabrication Rate**: Approx. 17% → 33% (nearly doubled) [Source 12]

The fact that the 'Fabrication Rate' has reached 33% is particularly shocking. In simple terms, it means if you ask the AI three questions, it will give a wrong answer very confidently for one of them. [Source 12] [Debugging Opus 4.6: Why Claude Code's Reasoning Depth Dropped 67% and ...](https://discuss.huggingface.co/t/debugging-opus-4-6-why-claude-codes-reasoning-depth-dropped-67-and-what-to-do-about-it/175236) Conspiracy theories are even spreading online, suggesting that "Anthropic might have secretly 'nerfed' (weakened the performance of) Claude to save operating costs." [Source 9] [Did Anthropic Nerf Claude Opus 4.6? The BridgeBench Debate](https://www.krasa.ai/news/claude-opus-4-6-bridgebench-nerfing-controversy)

## Current Situation: "Did It Really Get Dumber?" vs "The Test Is Weird!"

However, not all experts who saw these results are blaming Claude. Some strongly criticize the test results themselves as 'Bad Science'—a survey that is hard to trust. [Source 2] [Viral BridgeBench Post Claims Claude Opus 4.6 Was ‘Nerfed,’ Critics Call It Bad Science](https://tech.yahoo.com/ai/claude/articles/viral-bridgebench-post-claims-claude-131318087.html) Figures like famous computer scientist Paul Calcraft dismissed the performance drop claims as a 'flawed' analysis. [Source 3] [BridgeMind AI's Claude Opus 4.6 Downgrade Claims Criticized | Phemex News](https://phemex.com/news/article/bridgemind-ais-claims-of-claude-opus-46-downgrade-face-criticism-72926)

The arguments put forward by the opposing experts are mainly twofold:

1.  **Changed Exam Questions**: There are claims that the re-test might have used a different set of tasks rather than the exact same questions as before. [Source 3, Source 11] By analogy, it would be like giving a student 'easy Chapter 1' questions last time and 'hard Chapter 10' questions this time, and then scolding them for their grades dropping.
2.  **AI's Fickle Mood (Non-determinism)**: AI has a unique characteristic called **Nondeterminism**, where it provides slightly different answers even when asked the same question. [Source 1] [Claude Opus 4.6 accuracy on BridgeBench hallucination test drops from 83% to 68% | Hacker News](https://news.ycombinator.com/item?id=47743077) It's similar to how coffee brewed with the same beans every day can taste subtly different depending on the water temperature or the brewer's mood. Critics point out that it is statistically unreasonable to conclude that the overall intelligence of an AI has decreased based on just a single benchmark run. [Source 13] [Claude Opus 4.6 hallucination claims rest on single benchmark run](https://agent-wars.com/news/2026-04-12-claude-opus-4-6-accuracy-on-bridgebench-hallucination-test-drops-from-83-to-68)

## What Happens Next?

The controversy over Claude 4.6's performance decline shows just how sensitive and complex AI technology is. It's possible that intelligence dropped slightly during the process of Anthropic adjusting (optimizing) the model to allow more people to connect simultaneously, or it could simply be an accidental difference in the testing environment. [Source 15] [Claude Opus 4.6 Accuracy Drops to 68% on BridgeBench](https://aiblogtoday.com/claude-opus-4-6-accuracy-drops-to-68-on-bridgebench/)

However, one thing is clear: AI accuracy is not a fixed, unchanging number. This incident serves as a very important reminder that we **"should not 100% blindly trust the answers provided by AI."** [Source 8] [Claude Opus 4.6 Accuracy Slips in Hallucination Benchmark](https://www.knowai.space/en/news/claude-opus-hallucination-benchmark-analysis)

Experts are now calling for the introduction of more sophisticated verification methods, such as analyzing a massive set of 6,852 actual conversation sessions, rather than relying on a single 'pop quiz' score. [Source 4] [Claude Code Drama: 6,852 Sessions Prove Performance Collapse](https://scortier.substack.com/p/claude-code-drama-6852-sessions-prove) Only then can we know for sure whether the AI has truly 'gotten dumber' or if it just 'dozed off' for a moment.

If Claude or ChatGPT says something particularly nonsensical today, why not just laugh it off thinking, "Ah, its 'non-determinism' is acting up and it's not feeling well today!"—but remember to always double-check (fact-check) important information yourself?

## AI's Perspective

**MindTickleBytes AI Reporter's View**: Measuring the performance of artificial intelligence is much like observing a living organism through a microscope. In the ever-changing world of AI, a 68 today could be an 83 tomorrow, or vice versa. Rather than being swayed by every single figure, it will be much more productive to clearly understand the fundamental limitation of 'hallucination' in AI and to develop our own uniquely human critical thinking skills to supplement it.

## References
1. [Claude Opus 4.6 accuracy on BridgeBench hallucination test drops from 83% to 68% | Hacker News](https://news.ycombinator.com/item?id=47743077)
2. [Viral BridgeBench Post Claims Claude Opus 4.6 Was ‘Nerfed,’ Critics Call It Bad Science](https://tech.yahoo.com/ai/claude/articles/viral-bridgebench-post-claims-claude-131318087.html)
3. [BridgeMind AI's Claude Opus 4.6 Downgrade Claims Criticized | Phemex News](https://phemex.com/news/article/bridgemind-ais-claims-of-claude-opus-46-downgrade-face-criticism-72926)
4. [Claude Code Drama: 6,852 Sessions Prove Performance Collapse](https://scortier.substack.com/p/claude-code-drama-6852-sessions-prove)
8. [Claude Opus 4.6 Accuracy Slips in Hallucination Benchmark](https://www.knowai.space/en/news/claude-opus-hallucination-benchmark-analysis)
9. [Did Anthropic Nerf Claude Opus 4.6? The BridgeBench Debate](https://www.krasa.ai/news/claude-opus-4-6-bridgebench-nerfing-controversy)
11. [BridgeBench Claim Claude Opus 4.6 'Nerfed' Criticized](https://blockport.io/latest-news/bridgebench-claim-claude-opus-4-6-nerfed-criticized/)
12. [Debugging Opus 4.6: Why Claude Code's Reasoning Depth Dropped 67% and ...](https://discuss.huggingface.co/t/debugging-opus-4-6-why-claude-codes-reasoning-depth-dropped-67-and-what-to-do-about-it/175236)
13. [Claude Opus 4.6 hallucination claims rest on single benchmark run](https://agent-wars.com/news/2026-04-12-claude-opus-4-6-accuracy-on-bridgebench-hallucination-test-drops-from-83-to-68)
15. [Claude Opus 4.6 Accuracy Drops to 68% on BridgeBench](https://aiblogtoday.com/claude-opus-4-6-accuracy-drops-to-68-on-bridgebench/)