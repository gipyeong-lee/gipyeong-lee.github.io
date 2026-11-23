---
layout: post
title: "I Asked AI 'How Long Will This Take?'… And It Was Wrong by 99%?"
description: "Can Large Language Models (LLMs) predict AI task execution times? An easy-to-understand look at AI's sense of time and realistic limitations through PreRun benchmark research."
summary: "According to the PreRun benchmark developed by researchers, when modern AI models predict execution times based solely on task descriptions, they underestimate actual runtimes by an absurd 90 to 99%."
tags: [AI, Benchmark, Machine Learning, GPU, PreRun]
image: 2026-11-23-How-Long-Will-My-Language-Model-Run-A-Benchmark-for-Pre-Execution-Runtime-Predic.jpg
image_alt: "An illustration showing an advanced supercomputer server room glowing alongside a futuristic digital timer"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "No matter how smart AI becomes, guessing the time required for physical computing resources based purely on intuition remains difficult. This is an interesting case showing why collaboration between traditional statistical models and AI is necessary."
quiz:
  - question: "What is the name of the new benchmark introduced by researchers to predict the execution times of large language models and vision models?"
    choices: ["PreRun", "LiveBench", "TerminalBench"]
    answer: 0
    explanation: "PreRun is a benchmark introduced to predict deep learning training and inference runtimes based on available information prior to execution."
  - question: "When open-weight LLMs processed task settings without examples (few-shot), by how much on average did they underestimate latency?"
    choices: ["10~20%", "50~60%", "90~99%"]
    answer: 2
    explanation: "Open-weight LLMs showed a severe error, underestimating latency by 90 to 99% when prompted without examples."
  - question: "In comparative evaluations, which traditional machine learning method trained on 32 settings performed significantly better than zero-shot Claude's mean absolute error?"
    choices: ["Random Forest", "Linear Regression", "Support Vector Machine (SVM)"]
    answer: 0
    explanation: "The Random Forest regression model recorded a much lower error than Claude's zero-shot error when trained on 32 settings."
lang: en
ref: 2026-11-23-How-Long-Will-My-Language-Model-Run-A-Benchmark-for-Pre-Execution-Runtime-Predic
audio: 2026-11-23-How-Long-Will-My-Language-Model-Run-A-Benchmark-for-Pre-Execution-Runtime-Predic.en.mp3
industry: creative
---

Imagine this: You rent an exorbitantly expensive and massive shared kitchen (a supercomputer GPU cluster) and are about to start preparing a very complex dish (large AI model training and inference tasks). You ask the kitchen manager, "Exactly how many minutes will it take to finish this dish?" The manager quickly glances over the recipe (the task description) and confidently replies, "Hmm, it'll be done in a minute!"

However, once you actually started cooking, it took over 100 minutes, and the kitchen rental costs snowballed.

Recently, an absurd yet serious experiment with the exact same premise was published in the artificial intelligence (AI) research community. When Large Language Models (LLMs)—large AI systems that understand and generate human language—were asked in advance how long AI model training and inference tasks would take, they drastically and absurdly underestimated the time [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)]. Why on earth did this happen?

---

## Why Does This Matter?

As AI technology develops dazzlingly, researchers and companies worldwide are creating and running countless deep learning models (Deep Learning—a technology where computers learn on their own by mimicking human neural networks). One of the most vexing problems in this process is accurately predicting **"how many computer resources and how much time it will take to execute this AI task"** [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)].

In reality, when researchers submit jobs to shared computing resources called GPU clusters (Graphics Processing Units—graphics cards designed for fast high-performance computing), they must set a "time limit." This is because jobs are forcibly terminated once the time expires. Furthermore, accurate runtime prediction is essential for efficiently allocating budgets and selecting hardware [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)].

Instead of performing complex mathematical calculations or running simulations every time, people thought of a tempting shortcut: the idea of **"giving the task description to AI and asking how many minutes it will take!"** [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)]. If an LLM could read the document and accurately guess the runtime, it would enormously reduce the burden on researchers. However, it was necessary to verify whether AI actually possessed such capabilities, so researchers created a special testing ground for this purpose.

---

## Understanding It Simply: What is the PreRun Benchmark?

To solve this problem, researchers introduced a new benchmark (Benchmark—an evaluation test designed to fairly compare performance) called **PreRun** [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)]. 

Simply put, **PreRun is a "time-sense test paper" for AI models**. This test paper contains massive records collected from actual GPU clusters. Specifically, it includes 801 training records and 1,884 inference records (Inference—the process where a trained model actually generates answers) for language and vision models [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)]. Task configurations are paired with clearly defined time targets here. Additionally, 64 text generation configurations measured under standardized conditions (each run separately three times) are included to enable rigorous verification [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)].

To use an analogy, it is like gathering CCTV footage of a kitchen that cooked thousands of times in the past along with recipe notes to make a chef guess "how long it takes to make two servings of pasta with these ingredients." Scoring how accurately the AI guesses the time after looking at these notes is what this test does.

Through this test, the researchers compared the proficiency of three representative AI models—**Qwen3.5-9B, GPT-OSS-120B, and Claude Opus 5.5**—against existing statistical regression baseline models (Regression baselines—traditional mathematical models that predict numerical relationships based on data) [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)].

---

## Current Status: What Level is AI's Sense of Time?

The experimental results were somewhat shocking. No matter how fluently AI understands human language and performs complex coding, it revealed massive flaws in predicting the execution time of physical computer tasks.

1. **Severe Underestimation (90–99% Error)**: When open-weight LLMs (Open-weight LLMs—open artificial intelligence models with publicly available source code) were given task configurations without any examples (Zero-shot) and asked for the time, they **underestimated latency** (Latency—the delay time from issuing a command until a result is produced) by a staggering **90% to 99%** [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)]. In other words, for a task that actually takes 100 minutes, the AI absurdly predicted, "It'll take 1 minute."
2. **Comparison with Traditional Methods**: In Claude's case, the mean absolute error when predicting directly without examples (zero-shot) was **4.5 times** higher than that of a **Random Forest** model (Random Forest—a traditional machine learning algorithm that improves prediction accuracy by combining multiple decision trees) trained on just 32 settings [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)]. This means that intuition or sentence comprehension alone does not allow AI to properly gauge the physical time required by hardware.
3. **Effect of Model Answers (Examples)**: However, when Claude was provided in advance with just five specific training examples (Labeled examples), its text generation prediction error decreased significantly. Nonetheless, the effectiveness of these examples varied slightly depending on the timing target being measured [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)].

These results clearly demonstrate that while AI brilliantly understands "what kind of task" it is by reading text, it cannot intuitively feel the weight of physical time consumed as electrons move and memory and arithmetic units collide inside actual physical hardware.

---

## What Lies Ahead?

What are the implications of this study for us? In what direction will the world of AI and system operations head in the future?

First, the research team plans to release the data and evaluation pipeline (Pipeline—a series of processing systems through which data flows and is processed) constructed in this study as open-source (Open-source—software released so that anyone can freely use and modify it) to academia and industry [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)]. This will allow researchers worldwide to conduct various follow-up studies to improve AI's "time prediction capabilities."

Future directions of development can be anticipated as follows:
- **Popularization of Hybrid Approaches**: Hybrid systems combining AI's superior document comprehension abilities with the numerical calculation capabilities of traditional machine learning (such as Random Forests) will gain attention. In this approach, AI reads the task description while mathematical regression models supplement the actual time calculation.
- **Efficiency in Cloud Resource Management**: Companies operating GPU clusters will be able to set time limits more accurately before job submission, preventing the waste of computing resources and reducing unnecessary expenditure [[How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)].

Although it seems like an era where AI magically handles everything effortlessly, understanding the "physical time of hardware" still remains the domain of cold, precise data and statistics. It will be immensely interesting to watch whether AI evolves into a smart assistant capable of accurately predicting even its own execution times.

---

## References

1. [How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction](https://arxiv.org/abs/2611.26875)