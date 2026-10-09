---
layout: post
title: "AI plays Pac-Man? Introducing 'Jevman', a unique benchmark testing real-time AI decision-making"
description: "Introducing 'Jevman', a Pac-Man game benchmark developed to test how quickly and accurately AI models can make decisions."
summary: "We cover 'Jevman', an open-source benchmark project that measures how accurately and quickly various AI models can make real-time decisions while avoiding ghosts in the game of Pac-Man."
tags: [AI, Benchmark, Pac-Man, Jevman, Decision-making model]
image: 2026-10-09-Show-HN-Jevman-AI-decision-models-play-Pac-Man.jpg
image_alt: "AI models making real-time decisions while playing the classic game Pac-Man."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Testing AI's decision-making speed in a familiar environment like a game, rather than through complex math problems, is a more intuitive and effective way to showcase a model's practical capabilities."
quiz:
  - question: "What is the main purpose of the Jevman benchmark?"
    choices: ["To test AI's graphics processing capabilities", "To test the real-time, fast, and accurate decision-making ability of AI models", "To compete on how long an AI can play the game"]
    answer: 1
    explanation: "Jevman was created to measure the real-time decision-making ability of AI models to quickly process information and make correct choices in the environment of the game Pac-Man."
  - question: "How is the testing conducted in Jevman?"
    choices: ["Total 50 games played with 10 plays per model", "Total 6 models played with 100 games per model", "A 1-on-1 match between a human and AI"]
    answer: 1
    explanation: "Six major AI models participated in the Jevman benchmark, and each model competed by playing 100 Pac-Man games in real-time."
  - question: "Which of the following is a feature of the Jevman project?"
    choices: ["It is accessible only as a paid service", "Results are not made public", "It is open-source, allowing anyone to submit their own model"]
    answer: 2
    explanation: "Jevman is an open-source project that allows users to directly submit their own models to the benchmark to check their performance."
lang: en
ref: 2026-10-09-Show-HN-Jevman-AI-decision-models-play-Pac-Man
audio: 2026-10-09-Show-HN-Jevman-AI-decision-models-play-Pac-Man.en.mp3
industry: general
---

Imagine this: You're sitting in front of an arcade machine, controlling Pac-Man. Ghosts are chasing you at high speed across the screen. You have to decide "Should I go left or right?" every 0.1 seconds. In these tense moments that would make a human sweat, how exactly does Artificial Intelligence (AI) make its judgments?

Recently, a very interesting 'Pac-Man benchmark' has emerged to test AI decision-making in real-time. It's called **Jevman**.

## Why does this matter?

The smart AIs we use daily are proficient at reading long passages and summarizing content, but how do they perform in situations requiring immediate decisions within a very short timeframe?

Jevman was created to test this 'Decision-making' ability of AI. When we entrust AI with daily judgments like "Should I grab an umbrella right now?" or "Should I accept this investment deal?", the AI must analyze complex situations within a very short amount of time. Pac-Man provides the optimal environment to simulate this complex decision-making process as it requires observing ghost movements and finding paths.

Simply put, Jevman is a type of 'AI brain test' that objectively evaluates **how quickly and accurately an AI chooses the right action in urgent real-time situations**, going beyond simple linguistic knowledge. [[Source: jevman: AI decision models play Pac-Man | VibeLeaderboard](https://www.vibeleaderboard.ai/app/17f8acd3-69b1-4c04-b083-30957220898d)]

## Understanding it easily

The test conducted by 'Jevman' is like a **"practical driving test for AI."**

1. **State Awareness (State)**: The AI model receives information about the current screen state, such as where Pac-Man is and where the ghosts are. [[Source: GitHub - denis-shvets/jevman-benchmark: Pac-Man driven by the ...](https://github.com/denis-shvets/jevman-benchmark)]
2. **Judgment (System One decision)**: A fast, instinctive decision-making model called 'System One' analyzes this information. To use an analogy, it's an intuitive judgment like reflexively pulling your hand away when it touches a hot pot. [[Source: Jev: System One Decision Model Explained | AIJev](https://aijev.org/)]
3. **Action (Action)**: Based on the judgment result, the AI decides between up, down, left, or right and moves Pac-Man. [[Source: GitHub - codaaiteam/jev-pacman: You drive Pac-Man; Jev...](https://github.com/codaaiteam/jev-pacman)]

This process repeats in short millisecond (ms) intervals. If you liken this to a novice driver turning the steering wheel after observing road lanes and traffic lights, the AI is effectively building its driving skills by controlling Pac-Man within the game. Currently, the six AI models participating in this test (jev 1.13, kev, clef, clef flash, GPT-6 Luna, Laya, etc.) are each proving their decision-making prowess by playing Pac-Man 100 times. [[Source: jevman: AI decision models play Pac-Man | TheaterFire](https://theaterfi.re/post/3741604), [Source: Jevman: AI Decision Models Play Pac-Man | VibeLeaderboard](https://www.vibeleaderboard.ai/app/17f8acd3-69b1-4c04-b083-30957220898d)]

## Current status

Jevman goes beyond the simple fact that AI is enjoying a game. All game records are public for anyone to watch, and there is an **official leaderboard** where you can see at a glance who achieved the higher score. [[Source: jevman: a Pac-Man benchmark for decision models | OpperAI](https://opper.ai/jevman-benchmark/), [Source: jevman — Six AI decision models play Pac-Man, ranked live](https://launchdaily.info/products/jevman)]

What's even more interesting is that this project is **open-source**. This means any AI developer can register their own model to the Jevman benchmark to measure its performance. Even general users can play Pac-Man themselves and compare their scores with the AI models in real-time. You can verify for yourself the question, "Can a human make better judgments than an AI?" [[Source: jevman · Can you beat the AI at Pac-Man?](https://jevman.apps.chadda.se/), [Source: jevman — Six AI decision models play Pac-Man, ranked live](https://launchdaily.info/products/jevman)]

## What's next?

Game-based benchmarks like Jevman will continue to increase. This is because AI is evolving beyond the stage of simply showing off knowledge into an 'acting AI' that actually controls software in our daily lives and makes automatic decisions according to business rules.

Now, when choosing an AI, we will move beyond just wondering "Who speaks better?" to considering "Who makes the right decisions without mistakes in urgent situations?" Jevman is a fun training ground provided for AIs to prepare for that future.

**MindTickleBytes AI Reporter's View**:
It's amazing that AI reads vast papers and creates content, but watching the process of AI reducing mistakes in an intense game like Pac-Man feels much more realistic, as if we are seeing the AI's 'practical muscles.' I look forward to more 'game-type benchmarks' appearing to verify AI decision-making more precisely.

## References

1. [jevman: a Pac-Man benchmark for decision models | OpperAI](https://opper.ai/jevman-benchmark/)
2. [jevman · Can you beat the AI at Pac-Man?](https://jevman.apps.chadda.se/)
3. [GitHub - joch/jevman: Pac-Man driven by the jev decision model](https://github.com/joch/jevman)
4. [jevman: AI decision models play Pac-Man | TheaterFire](https://theaterfi.re/post/3741604)
5. [Show HN: Jevman – AI decision models play Pac-Man](https://semasocial.com/blog/show-hn-jevman-ai-decision-models-play-pac-man-61213)
6. [jevman — Six AI decision models play Pac-Man, ranked live](https://launchdaily.info/products/jevman)
7. [GitHub - denis-shvets/jevman-benchmark: Pac-Man driven by the ...](https://github.com/denis-shvets/jevman-benchmark)
8. [Jevman: AI Decision Models Play Pac-Man | VibeLeaderboard](https://www.vibeleaderboard.ai/app/17f8acd3-69b1-4c04-b083-30957220898d)
9. [Jev: System One Decision Model Explained | AIJev](https://aijev.org/)
10. [GitHub - codaaiteam/jev-pacman: You drive Pac-Man; Jev...](https://github.com/codaaiteam/jev-pacman)