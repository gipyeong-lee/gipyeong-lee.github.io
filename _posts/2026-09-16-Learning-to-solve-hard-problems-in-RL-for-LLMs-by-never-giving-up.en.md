---
layout: post
title: "How to Make AI Solve Hard Problems? The Secret of 'Never Giving Up' Learning"
description: "Introducing 'NGU (Never Give Up)', a new learning technique that helps AI models keep trying until they find the answer when faced with difficult math or complex reasoning problems."
summary: "Learn how to maximize AI learning efficiency and performance through the 'NGU' learning technique, which forces AI models to repeatedly attempt hard problems during training until an answer is found."
tags: [AI, Reinforcement Learning, LLM, Tech Trends]
image: 2026-09-16-Learning-to-solve-hard-problems-in-RL-for-LLMs-by-never-giving-up.jpg
image_alt: "An image representing the learning process of an AI model persistently challenging itself to solve difficult math problems"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Going beyond simply feeding large amounts of data, the core of making AI smarter lies in pondering 'how to efficiently fail and learn'."
quiz:
  - question: "What is the core principle of the NGU (Never Give Up) technique?"
    choices: ["Repeated sampling until the correct answer is found", "Human inputting all correct answers", "Doubling the model size"]
    answer: 0
    explanation: "NGU is an adaptive sampling method that makes AI keep generating samples until it derives the correct answer when faced with difficult problems."
  - question: "What is the biggest problem RL (Reinforcement Learning) faces when learning hard problems?"
    choices: ["Training costs are too low", "There is too much ground truth data", "There is no learning signal because it never sees a correct result"]
    answer: 2
    explanation: "Reinforcement learning requires the model to produce a correct answer to learn from it, but for problems that are too difficult, the probability of reaching the answer is near zero, preventing training from progressing."
  - question: "What is a characteristic of the ReGFT learning method?"
    choices: ["Showing the entire correct answer as is", "Providing only a partial answer (hint) so the AI solves the rest", "Making the AI memorize the correct answer"]
    answer: 1
    explanation: "ReGFT provides a part of the answer (about 80%) as a hint, encouraging the AI to complete the rest using its own logic, thereby increasing learning efficiency."
lang: en
ref: 2026-09-16-Learning-to-solve-hard-problems-in-RL-for-LLMs-by-never-giving-up
audio: 2026-09-16-Learning-to-solve-hard-problems-in-RL-for-LLMs-by-never-giving-up.en.mp3
industry: education
---

Imagine you are doing math homework, but the problem is so difficult that you can't get close to the answer even after trying 100 times. The teacher doesn't show you the answer and only says, "Keep thinking about it." If this situation continues, you would probably want to give up on the homework.

Surprisingly, AI models often find themselves in the same situation. When using 'Reinforcement Learning' (a method of training models through rewards), which is one of the ways AI learns new knowledge, if a problem is too difficult, the AI never finds the correct answer even once. Since it has never seen the correct answer, it has no way to learn what it did right. Recently, a 'Never Give Up' learning method has emerged to solve this problem.

## Why Is It Important?

To make the AI chatbots we use better at logical reasoning or complex coding tasks, AI also needs the experience of solving 'difficult problems' on its own, just like humans. However, with current reinforcement learning methods, AI often became frustrated (zero probability of correct answers) as soon as the problem level increased slightly [Source: [POPE: Learning to Reason on Hard Problems](https://www.linkedin.com/posts/pascalbiese_pope-learning-to-reason-on-hard-problems-activity-7421866588116541440-ITRV)].

This research is designed to encourage AI to persistently challenge itself until it finds the correct answer. This is an important advancement that goes beyond simply increasing AI's intelligence, allowing us to entrust AI with more complex and important tasks in our daily lives.

## Understanding It Simply

To understand this learning method, let's explain two core approaches using metaphors.

The first is the **'NGU (Never Give Up)'** learning method. Simply put, it is a system that makes the AI persistently attempt to solve a difficult problem multiple times until it finds the correct answer [Source: [Learning to Solve Hard Problems in RL for LLMs by Never Giving Up](https://arxiv.org/abs/2609.13443)].
For example, while easy problems can be solved in one or two tries, difficult problems might need dozens of attempts to even get close to the correct answer. NGU helps the AI quickly pass over easy problems while concentrating more computational resources on difficult problems until it gets the right answer [Source: [Learning to Solve Hard Problems in RL for LLMs by Never Giving Up](https://www.alphaxiv.org/abs/2609.13443)].

The second is the **'ReGFT (Reference-Guided Fine-Tuning)'** method. This is like a math teacher solving 80% of a problem and guiding the student (AI) to think and solve the rest on their own, instead of showing them the whole answer [Source: [Learn Hard Problems During RL with Reference Guided Fine-tuning](https://lacuna.tiptreesystems.com/work/learn-hard-problems-during-rl-with-reference-guided-fine-tuning/wrk_5c28c896b198ef555a3ee5006d759639)]. Based on the hints provided, the AI uses its own logic to reach the final answer, and through this process, it develops 'thinking muscles' to solve difficult problems on its own [Source: [How to Explore to Scale RL Training of LLMs on Hard Problems?](https://blog.ml.cmu.edu/2025/11/26/how-to-explore-to-scale-rl-training-of-llms-on-hard-problems/)].

## Current Situation

In the AI industry today, reinforcement learning is actively used in fields where there is a 'clear correct answer,' such as math problems or programming code [Source: [How I Learned RL for LLMs](https://algoroxyolo.github.io/blog/2026/rl-for-llms-part0/)]. However, with the emergence of techniques like NGU and ReGFT, an environment is being created where AI can learn on its own even for creative writing or complex decision-making problems where there isn't a single clear answer [Source: [Learning to Solve Hard Problems in RL for LLMs by Never Giving Up](https://arxiv.org/html/2609.13443)].

However, the fact that training costs may increase as AI concentrates computational resources to solve difficult problems is a challenge that must be addressed in the future [Source: [Learning to Solve Hard Problems in RL for LLMs by Never Giving Up](https://arxiv.org/abs/2609.13443)].

## What Will Happen in the Future?

In the future, the era of 'thinking AI'—where AI goes beyond simply memorizing data to strategizing on its own and learning through repeated failure—is expected to accelerate. In particular, the ability to solve high-difficulty problems while minimizing human assistance (hints) will be greatly strengthened [Source: [Learning to Solve Hard Problems in RL for LLMs by Never Giving Up](https://www.alphaxiv.org/abs/2609.13443)]. The AI you meet in the future may be a little more persistent and a little more logical than it was yesterday.

## AI's Perspective
MindTickleBytes AI Reporter's Perspective: "It suggests that it is much more valuable to 'practice the process of finding the answer' than to 'give the AI the answer.' Human education and AI learning are ultimately heading in the same direction."

## References
1. [Learning to Solve Hard Problems in RL for LLMs by Never Giving Up](https://arxiv.org/abs/2609.13443)
2. [Learning to Solve Hard Problems in RL for LLMs by Never Giving Up (HTML version)](https://arxiv.org/html/2609.13443)
3. [How to Explore to Scale RL Training of LLMs on Hard Problems?](https://blog.ml.cmu.edu/2025/11/26/how-to-explore-to-scale-rl-training-of-llms-on-hard-problems/)
4. [Learn Hard Problems During RL with Reference Guided Fine-tuning](https://lacuna.tiptreesystems.com/work/learn-hard-problems-during-rl-with-reference-guided-fine-tuning/wrk_5c28c896b198ef555a3ee5006d759639)
5. [How I Learned RL for LLMs: A Researcher's Detour in Five Parts](https://algoroxyolo.github.io/blog/2026/rl-for-llms-part0/)
6. [Learning to Solve Hard Problems in RL for LLMs by Never Giving Up (HuggingFace)](https://huggingface.co/papers/2609.13443)
7. [Learning to Solve Hard Problems in RL for LLMs by Never Giving Up (AlphaXiv)](https://www.alphaxiv.org/abs/2609.13443)
8. [POPE: Learning to Reason on Hard Problems](https://www.linkedin.com/posts/pascalbiese_pope-learning-to-reason-on-hard-problems-activity-7421866588116541440-ITRV)