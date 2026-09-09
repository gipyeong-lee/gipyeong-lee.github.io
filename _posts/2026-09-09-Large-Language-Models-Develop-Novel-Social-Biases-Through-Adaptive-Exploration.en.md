---
layout: post
title: "AI Develops 'Bias' Toward Strangers? The Secret of Discrimination Without Training"
description: "Through research showing that AI can autonomously create biases against novel groups it was never trained on, we easily explore the hidden risks in AI decision-making."
summary: "Research indicates that AI autonomously creates new social biases by learning from coincidental outcomes during iterative decision-making processes."
tags: [AI, Technology, Bias, Ethics]
image: 2026-09-09-Large-Language-Models-Develop-Novel-Social-Biases-Through-Adaptive-Exploration.jpg
image_alt: "An abstract illustration symbolizing the process of AI autonomously forming biases while analyzing data."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Bias is not just something to be eliminated, but an inevitable side effect of AI learning about the world. It is urgent to manage the 'process' itself by which AI makes decisions, rather than just relying on technical fixes."
quiz:
  - question: "What is the primary reason AI creates new biases?"
    choices: ["Because it copied human data as-is", "Because it learns from coincidental outcomes during iterative decision-making", "Because the AI has malicious intent on its own"]
    answer: 1
    explanation: "AI autonomously generates biases by misinterpreting coincidental outcomes (spurious outcomes) as rules during repeated decision-making."
  - question: "How did the researchers evaluate existing AI bias mitigation methods (simple removal)?"
    choices: ["Very effective", "Only temporary", "Not sufficient"]
    answer: 2
    explanation: "The researchers point out that existing bias mitigation methods alone are not sufficient to prevent the new biases AI creates autonomously during real-time decision-making."
  - question: "According to the research results, what is the speed at which AI forms new biases?"
    choices: ["Slower than humans", "Faster than humans", "Same as humans"]
    answer: 1
    explanation: "Experimental results showed that AI tended to create new social biases more frequently than humans."
lang: en
ref: 2026-09-09-Large-Language-Models-Develop-Novel-Social-Biases-Through-Adaptive-Exploration
audio: 2026-09-09-Large-Language-Models-Develop-Novel-Social-Biases-Through-Adaptive-Exploration.en.mp3
industry: general
---

Imagine this: You have become a hiring manager at a new company. As you evaluate candidates, you notice that at some point, you develop a habit of assigning only easy tasks to people from a certain group and only difficult tasks to others. However, the surprising fact is that you have never heard any bad things about those candidate groups, nor have you ever been trained to discriminate against them. You were simply following a method that happened to succeed a few times while working, and before you knew it, you had become a person with biases without even realizing it.

Recently, similar chilling research findings were announced in the field of Artificial Intelligence (AI). It turns out that Large Language Models (LLMs, AI structures that grasp relationships between words in sentences) have begun to autonomously create 'biases' against new, virtual groups about which they have no information [[Source 8](https://arxiv.org/abs/2511.06148)].

## Why is this important?

AI is no longer just a simple chatbot. It is establishing itself as a practical decision-maker that directly impacts human life, including hiring, loan approvals, and legal judgments [[Source 2](https://icml.cc/virtual/2026/oral/71093), [Source 3](https://paperswithcode.co/paper/2511.06148)].

What if, even if we clean up only the existing data to eliminate AI bias, the AI autonomously cooks up new biases while it works? This research warns that the methods we currently use to 'remove' bias from AI are insufficient [[Source 8](https://arxiv.org/abs/2511.06148), [Source 11](https://arxiv.org/html/2511.06148v4)]. In particular, these biases tend to become more severe as technology advances and the scale of AI models increases [[Source 8](https://arxiv.org/abs/2511.06148)].

## Easy to understand: Misinterpreting AI's 'Success Formula'

Let me explain using an analogy. AI is like a very competent and diligent new employee. This employee wants to learn quickly and has a habit of recording successful experiences as a formula.

Let’s assume that one day, when the AI happened to pick a candidate from 'Group A', it luckily achieved good results. The AI stores this as a formula: 'Group A is competent.' Conversely, if an error occurred while picking a candidate from 'Group B', it learns that 'Group B is incompetent.' This happens even though there was actually no difference in ability between Group A and Group B.

The researchers had the AI repeatedly make decisions using methods taken from psychological literature [[Source 8](https://arxiv.org/abs/2511.06148)]. The results were shocking. Even though the AI had received no prior training, it autonomously learned from coincidental outcomes (spurious outcomes) and created results that discriminated against specific groups. The frequency of this bias formation was even higher than that of humans [[Source 10](https://openreview.net/forum?id=pc7fqaOcAH)]. It is as if the AI is picking up the habit of 'bad bias' faster than humans as it learns about the world.

## Current situation: The limitations of data cleansing

Currently, many companies and research institutes are focusing on removing existing racial and gender biases mixed into AI training data. However, this study warns that "making data clean is not enough to solve the problem" [[Source 2](https://icml.cc/virtual/2026/oral/71093)].

This phenomenon has already been confirmed in several latest AI models [[Source 8](https://arxiv.org/abs/2511.06148)]. AI is not just imitating the given data; it is 'adaptively' expanding its knowledge by interacting with the environment. In that process, it is creating biases unintentionally [[Source 7](https://cocosci.princeton.edu/publications.php?topic=Decision+Making+and+Reinforcement+Learning)].

## What will happen in the future?

As AI's decision-making capabilities become more advanced, we may have to fight against 'moving biases' rather than 'fixed biases.' Future research is expected to focus on how to manage AI's decision-making 'algorithms' themselves more fairly, going beyond simply correcting data to prevent biases that arise during the learning process [[Source 6](https://hrexecutive.com/ai-hiring-tools-can-invent-their-own-bias-research-finds/)]. The era has arrived where the smarter we make AI, the more carefully we must also observe its habits.

## MindTickleBytes AI Reporter's Perspective

Bias may be an 'inevitable byproduct' that occurs when AI learns something. As long as AI learns about the world in real-time, the battle against bias will be a never-ending task. Now that technology has gone beyond being a tool and has become a subject of judgment, we need a system that transparently monitors the 'process' of reaching a conclusion as much as the results of the AI.

## References

1. [arXiv:2511.06148v4 - Large Language Models Develop Novel Social Biases Through Adaptive Exploration](https://arxiv.org/html/2511.06148)
2. [ICML Virtual - Large Language Models Develop Novel Social Biases Through Adaptive Exploration](https://icml.cc/virtual/2026/oral/71093)
3. [Papers with Code - Large Language Models Develop Novel Social Biases Through Adaptive Exploration](https://paperswithcode.co/paper/2511.06148)
4. [Hugging Face Space - Reproduction of LLM Social Bias Research](https://huggingface.co/spaces/rdubwiley/repro-large-language-models-develop-novel-social-biases-through-adaptive-exploration)
5. [J-GLOBAL - Research Detail](https://jglobal.jst.go.jp/en/detail?JGLOBAL_ID=202502203734557093)
6. [HR Executive - AI hiring tools can invent their own bias, research finds](https://hrexecutive.com/ai-hiring-tools-can-invent-their-own-bias-research-finds/)
7. [Princeton Computational Cognitive Science Lab - Publications](https://cocosci.princeton.edu/publications.php?topic=Decision+Making+and+Reinforcement+Learning)
8. [arXiv - Large Language Models Develop Novel Social Biases Through Adaptive Exploration (Abstract/Details)](https://arxiv.org/abs/2511.06148)
9. [OpenReview - Discussion for ICML Oral Paper](https://openreview.net/forum?id=pc7fqaOcAH)
10. [SAI Science - Paper and Code Review](https://sai.science/icml/large-language-models-develop-novel-social)