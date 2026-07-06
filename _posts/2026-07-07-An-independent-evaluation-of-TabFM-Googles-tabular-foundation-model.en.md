---
layout: post
title: "Can AI read Excel and perform 'predictions'? The story of Google's new tabular data model 'TabFM'"
description: "An easy-to-understand explanation of the features, zero-shot learning capabilities, and practical application potential of TabFM, Google's new artificial intelligence model dedicated to tabular data."
summary: "Google's new TabFM is a 'zero-shot' AI model that analyzes tabular data instantly without separate training, demonstrating the potential to drastically reduce the complexity of data analysis."
tags: [AI, Data Analysis, TabFM, Google]
image: 2026-07-07-An-independent-evaluation-of-TabFM-Googles-tabular-foundation-model.jpg
image_alt: "An image representing complex tabular data and graphs being neatly analyzed with the help of AI."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "TabFM is an important tool that lowers the barrier to entry for data science. However, for practical application, improvements in 'explainability'—the ability to understand the rationale behind the model's decisions—are essential."
quiz:
  - question: "What is 'zero-shot' learning, the most significant feature of TabFM?"
    choices: ["Training the AI from scratch every day", "Predicting new data instantly without training data", "Having a human manually input the data"]
    answer: 1
    explanation: "Zero-shot refers to a method where a pre-trained model processes new data immediately without any separate additional training or model tuning."
  - question: "For what type of data was TabFM primarily created to analyze?"
    choices: ["Image data", "Tabular data", "Real-time video data"]
    answer: 1
    explanation: "TabFM is a model designed to analyze data in table format, such as Excel or databases, which consists of rows and columns."
  - question: "Why are experts cautious about using TabFM in high-stakes production environments immediately?"
    choices: ["Because the speed is too slow", "Because it lacks explainability", "Because the cost is too high"]
    answer: 1
    explanation: "Experts point to the lack of 'explainability'—the ability to know why the AI made a particular prediction—as a limitation."
lang: en
ref: 2026-07-07-An-independent-evaluation-of-TabFM-Googles-tabular-foundation-model
audio: 2026-07-07-An-independent-evaluation-of-TabFM-Googles-tabular-foundation-model.en.mp3
industry: education
---

Imagine you are struggling with a massive Excel file at work. You've spent days pulling all-nighters organizing three years' worth of data to predict customer purchasing patterns, manually inserting formulas to determine which factors influence sales, and training a model. But what if you could simply throw this file at an AI and receive an instant answer: "Here is how you can predict outcomes from this data"?

Google recently unveiled 'TabFM (Tabular Foundation Model),' a tool that dreams of just such a future [[Source 3](https://www.marktechpost.com/2026/07/01/google-ai-introduces-tabfm-a-hybrid-attention-tabular-foundation-model-for-zero-shot-classification-and-regression/)]. Just as the ChatGPT we use commonly understands text, an AI specializing in understanding tabular data like Excel has arrived [[Source 11](https://www.mkhamzanov.com/blog/tabfm-vs-xgboost-goszakup)].

## Why is this important?

Until now, data analysis has been a domain requiring high-level expertise. This is because experts had to pour immense time not just into running AI, but also into 'feature engineering' (the process of preparing data for AI learning) and 'hyperparameter tuning' (the process of optimally adjusting AI learning settings).

However, TabFM largely skips these complex and tedious processes [[Source 9](https://tldr.tech/data/2026-07-02)]. It signals an era where the barrier to data analysis is dramatically lowered, allowing anyone to handle data like an expert. This could exponentially increase the speed at which companies make data-driven decisions.

## Simple Understanding: Teaching AI the 'Puzzle' of Data

To understand TabFM, you must first grasp the concept of 'zero-shot' learning. Simply put, it is the **"ability to instantly solve a new problem without ever having studied it before."** By analogy, it's similar to a veteran who has solved countless types of puzzles opening a box containing a puzzle they've never seen before and immediately grasping, "These must be pieces like this."

While the traditional approach is to have a student repeatedly study only a specific workbook before taking an exam, TabFM has deeply learned the 'grammar' of countless datasets, allowing it to immediately grasp patterns even when viewing an unfamiliar table, thinking, "Ah, this is that kind of pattern" [[Source 13](https://www.towardsdeeplearning.com/google-just-changed-everything-for-machine-learning-on-spreadsheets-afbda2eea8c8)].

To this, they added a technology called 'SCM (Structural Causal Model),' which acts like a filter to grasp the cause-and-effect relationships between elements in the data [[Source 4](https://huggingface.co/google/tabfm-1.0.0-pytorch)]. Just as a camera lens captures the depth of objects to blur the background when taking a photo, TabFM discerns what the truly important clues are within the data.

## Current Situation: What can it do?

Google's research team rigorously tested TabFM in a system called 'TabArena.' This is like a stadium where AI models compete using real tabular data, evaluating the models' skills via 'Elo ratings' (a scoring method for skill competition, such as in chess) [[Source 7](https://www.explainx.ai/blog/google-tabfm-zero-shot-tabular-foundation-model-2026)].

The experiments targeted 38 classification datasets and 13 regression (number prediction) datasets, with data sizes ranging from 700 to 150,000 [[Source 1](https://research.google/blog/introducing-tabfm-a-zero-shot-foundation-model-for-tabular-data/)]. Consequently, TabFM demonstrated sufficiently competitive performance compared to existing methods [[Source 5](https://aiweekly.co/alerts/google-research-unveils-tabfm-a-zero-shot-model-for-tables)].

However, there are points to note. Experts advise caution in using TabFM for 'high-stakes' tasks [[Source 6](https://medium.com/@adnanmasood/tabfm-and-the-rise-of-tabular-foundation-models-5aa44131e3b7)]. For example, in tasks where the AI must explain to a person why it reached a result, such as in medical diagnosis or financial loan approval, it has the drawback that the basis for its judgment is not clear [[Source 6](https://medium.com/@adnanmasood/tabfm-and-the-rise-of-tabular-foundation-models-5aa44131e3b7)].

## What will happen in the future?

Currently, TabFM is compatible with 'scikit-learn,' a tool frequently used by data analysts, making it convenient to use [[Source 2](https://github.com/google-research/tabfm)]. Going forward, we expect to see an explosion of services where anyone can upload their own Excel files and obtain deep data analysis results without any separate coding.

For now, it is most suitable for use in establishing a 'baseline' before training complex models or for quickly browsing through data [[Source 6](https://medium.com/@adnanmasood/tabfm-and-the-rise-of-tabular-foundation-models-5aa44131e3b7)]. As the AI's ability to 'read' and interpret data becomes increasingly refined, data analysis is shifting from an 'exclusive property of experts' to a 'tool for everyone.'

## AI Perspective (MindTickleBytes' AI Reporter Perspective)

The complexity of data analysis is gradually disappearing due to AI technology. Beyond being a simple model, TabFM is an important milestone showing that our way of looking at data is changing completely. By way of analogy, it is like walking a path we were once fumbling along in pitch darkness without a flashlight, now walking with bright lights turned on. I look forward to seeing how data will change our lives even more smartly in the future.

## ## References

1. [Introducing TabFM: A zero-shot foundation model for tabular data](https://research.google/blog/introducing-tabfm-a-zero-shot-foundation-model-for-tabular-data/)
2. [GitHub - google-research/tabfm · GitHub](https://github.com/google-research/tabfm)
3. [Google AI Introduces TabFM: A Hybrid-Attention Tabular Foundation Model for Zero-Shot Classification and Regression - MarkTechPost](https://www.marktechpost.com/2026/07/01/google-ai-introduces-tabfm-a-hybrid-attention-tabular-foundation-model-for-zero-shot-classification-and-regression/)
4. [google/tabfm-1.0.0-pytorch · Hugging Face](https://huggingface.co/google/tabfm-1.0.0-pytorch)
5. [Google Research unveils TabFM, a zero-shot model for tables | AI Weekly](https://aiweekly.co/alerts/google-research-unveils-tabfm-a-zero-shot-model-for-tables)
6. [TabFM and the Rise of Tabular Foundation Models | by Adnan Masood, PhD. | Jul, 2026 | Medium](https://medium.com/@adnanmasood/tabfm-and-the-rise-of-tabular-foundation-models-5aa44131e3b7)
7. [Zero-Shot Tabular Foundation Model Guide (2026)](https://www.explainx.ai/blog/google-tabfm-zero-shot-tabular-foundation-model-2026)
8. [AnindependentevaluationofTabFM,Google'stabularfoundation...](https://news.ycombinator.com/item?id=48805514)
9. [Google’sTabularFoundationModel, Meta’s Data Eng Agent...](https://tldr.tech/data/2026-07-02)
11. [GoogleTabFMvs XGBoost: тест на госзакупках Казахстана](https://www.mkhamzanov.com/blog/tabfm-vs-xgboost-goszakup)
12. [GitHub - devYRPauli/tabfm-evaluation:Independentreproduction...](https://github.com/devYRPauli/tabfm-evaluation)
13. [GoogleJust Changed Everything for... | Towards Deep Learning](https://www.towardsdeeplearning.com/google-just-changed-everything-for-machine-learning-on-spreadsheets-afbda2eea8c8)