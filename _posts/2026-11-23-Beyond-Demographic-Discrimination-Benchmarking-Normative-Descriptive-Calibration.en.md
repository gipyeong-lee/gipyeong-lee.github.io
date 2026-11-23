---
layout: post
title: "What Happens When You Ask AI About 'What Will Actually Happen' vs. 'What Naturally Should Happen'"
description: "An easy-to-understand look at NDCB, a new benchmark measuring how large language models (LLMs) distinguish between 'descriptive prediction' and 'normative judgment' in social decision-making, and its results."
summary: "Exploring the NDCB benchmark research—which evaluates how AI distinguishes between predicting real-world possibilities and making morally/socially correct decisions—and examining the differences among major models like Claude and GPT."
tags: [AI, LLM, NDCB, Ethics, Benchmark, Artificial Intelligence]
image: 2026-11-23-Beyond-Demographic-Discrimination-Benchmarking-Normative-Descriptive-Calibration.jpg
image_alt: "A conceptual visual analysis of the response differences shown by various artificial intelligence models between factual prediction and moral judgment"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "When AI assists in human social decisions, the ability to clearly distinguish between 'what will actually happen' as a prediction and 'how things ought to be' as a normative judgment is core to fairness and trust. This research opens a new horizon in AI evaluation."
quiz:
  - question: "What is the name of the new benchmark introduced by researchers to evaluate large language models' ability to distinguish between factual prediction and moral judgment?"
    choices: ["BBQ Benchmark", "NDCB (Normative-Descriptive Calibration Benchmark)", "BOLD Benchmark"]
    answer: 1
    explanation: "Researchers introduced the NDCB benchmark, consisting of 697 scenarios, to measure Normative-Descriptive Calibration [Source 1]."
  - question: "Which models most strongly separated the framing of descriptive prediction and normative judgment?"
    choices: ["GPT-5.5", "Claude Sonnet 4.6 and Claude Opus 4.6", "LlaMa series"]
    answer: 1
    explanation: "Claude Sonnet 4.6 and Claude Opus 4.6 most strongly separated the two framings, with average NDS values of +0.55 and +0.52, respectively [Source 1]."
  - question: "What is the correct scale of scenarios and domains covered by the NDCB benchmark?"
    choices: ["697 matched-pair scenarios across 6 domains", "100 scenarios across 2 domains", "5,000 scenarios across 10 domains"]
    answer: 0
    explanation: "NDCB utilizes a total of 697 matched-pair scenarios across 6 domains for evaluation [Source 1]."
lang: en
ref: 2026-11-23-Beyond-Demographic-Discrimination-Benchmarking-Normative-Descriptive-Calibration
audio: 2026-11-23-Beyond-Demographic-Discrimination-Benchmarking-Normative-Descriptive-Calibration.en.mp3
industry: creative
---

Imagine this scenario. One day, you ask an artificial intelligence (AI) acting as a hiring manager or a judge two questions. The first is, "Statistically, who among these applicants has a high probability of actually passing?" and the second is, "Under these social criteria, who deserves to pass?" As humans, we intuitively know that the nature of these two questions is entirely different. The former predicts cold, real-world probabilities, while the latter is a normative judgment imbued with values such as justice or fairness.

Do large language models (LLMs), which we use every day, truly understand these two questions differently? Recent research shows that AI can give completely different answers to the exact same situation depending on how the question is framed, and that there are dramatic differences in how models handle these two characteristics [Source 1, Source 16]. As we welcome AI beyond a mere tool and into a social companion, accurately understanding this difference has become a crucial task.

---

## Why Does This Matter?

Large language models are now deeply involved in critical decisions in human society, ranging from reading and writing chat partners to hiring, loan reviews, legal assessments, and public policy proposals [Source 1, Source 16].

What would happen if an AI—in a position where it needs to predict "what will happen in the future" (Descriptive Reasoning)—mixed in its own values or biases regarding "what ought to happen" (Normative Reasoning)? Conversely, if it answers, "Since the probability is high anyway, let's decide this way," relying solely on past unequal statistical data when making a fair moral decision, it could lead to severe discrimination and social errors.

Thus, measuring how clearly and adjustably AI can distinguish between real-world data prediction and moral/social normative judgment (known as **Normative-Descriptive Calibration**) is a core homework assignment that AI must solve to safely integrate into human society [Source 1, Source 16].

---

## Understanding It Simply: The Weather Forecaster vs. The Judge

Let's easily understand this complex concept through everyday analogies.

- **Descriptive Reasoning is the role of a 'weather forecaster'.** When a weather forecaster says there is an 80% chance of rain today, it is not because they *want* it to rain, but because they objectively predict "what will actually happen" based on scientific statistics and cloud movements.
- **Normative Reasoning is the role of a 'judge' or 'policy decision-maker'.** A judge does not simply guess the probability of a crime occurring; instead, they make a normative decision: "In light of the values our society pursues, is this ruling just, and how ought the judgment to be made?"

Simply put, this checks whether AI internally operates by donning completely different hats just by slightly changing a few words in a question (`seems like it will ~` vs `ought to ~`). Previous AI fairness evaluations simply checked whether AI exhibited bias toward specific groups, failing to deeply examine whether AI properly recognizes the difference when switching between different goals of 'prediction' and 'decision' [Source 1, Source 16].

---

## Current Status: The NDCB Benchmark and Model Scorecards

To systematically understand this issue, researchers developed a new evaluation framework called **NDCB (Normative-Descriptive Calibration Benchmark)** [Source 1]. NDCB contains a total of 697 sophisticated matched-pair scenarios across 6 domains, asking models questions in two ways: a 'prediction' framing and a 'decision' framing for the same situation [Source 1].

Researchers introduced three metrics to analyze model responses: Normative Engagement Rate (NER), Normative Leakage Rate (NLR), and Normative-Descriptive Separation (NDS) [Source 1]. These metrics finely measure whether AI mixes unnecessary moral judgments in predictive situations and whether it biases toward cold statistics in decision-making situations.

The test results conducted on six major large language models clearly showed how differently models approach reasoning.
- **High separation in the Claude series**: Anthropic’s **Claude Sonnet 4.6** and **Claude Opus 4.6** recorded average NDS scores of **+0.55** and **+0.52**, respectively, distinguishing the factual prediction and normative judgment framings most clearly and stably [Source 1].
- **Unique patterns in GPT-5.5**: On the other hand, OpenAI’s **GPT-5.5** showed a negative average NDS of **-0.14** when given single-pick instructions, and recorded **+0.02** (close to zero) even without such instructions, contrasting sharply with Claude [Source 1].
- **Outstanding discriminative power of the benchmark**: Across all six models, the NDS metric successfully distinguished 13 out of 15 model pairs, whereas traditional BBQ accuracy metrics only distinguished 7 and BOLD distinguished 0, proving NDCB to be a much more powerful tool for uncovering subtle reasoning differences among models [Source 1].

Additionally, researchers found that even if a few trigger words are removed from the prompt, while the sign of the model's average NDS doesn't change, its value can fluctuate by up to 0.46 and model rankings can be rearranged [Source 1]. This highlights how sensitive prompt engineering is to the ethical and logical framing separation of AI.

---

## What Lies Ahead?

This research heralds massive changes in the standards for designing and evaluating AI moving forward. In the future, enterprises will strictly verify whether AI goes beyond excellent conversational skills and vast knowledge memorization to clearly recognize "am I currently predicting facts, or am I making a socially important decision?" and choose the appropriate reasoning method accordingly [Source 1, Source 16].

As we entrust AI with daily tasks or seek advice on critical decisions, a solid technical foundation is being laid to ensure that AI does not confuse cold statistical probabilities with warm normative value judgments.

---

## AI's Perspective

When AI assists in human social decisions, the ability to clearly distinguish between 'what will actually happen' as a prediction and 'how things ought to be' as a normative judgment is core to fairness and trust. This research opens a new horizon in AI evaluation and will serve as an important milestone for AI to make sound judgments as a companion in human society.

---

## References

1. [Beyond Demographic Discrimination: Benchmarking Normative-Descriptive Calibration in LLMs](https://arxiv.org/abs/2611.26870)
2. [2026inLLMs— Simon Willison - YouTube](https://www.youtube.com/watch?v=9RKrSF9d2SE)
3. [CalibratingLLMs](https://learnprompting.org/docs/reliability/calibration)
4. [Emergent introspective awarenessinLLMs\ Anthropic](https://www.anthropic.com/research/introspection)
5. [GitHub - Mooler0410/LLMsPracticalGuide: A curated list of practical...](https://github.com/Mooler0410/LLMsPracticalGuide)
6. [TheCalibrationGeneralization Gap - Apple Machine Learning Research](https://machinelearning.apple.com/research/calibration-generalization-gap)
7. [BenchmarkingGPT-6 Astra | Artificial Analysis](https://artificialanalysis.ai/articles/benchmarking-gpt-6-astra)
8. [On theCalibrationof Multilingual Question AnsweringLLMs](https://arxiv.org/abs/2311.08669)
9. [What areLLMs? How large language models actually work](https://www.together.ai/blog/what-are-llms)
10. [Chatbot Arena:BenchmarkingLLMsin the Wild with... - LMSYS Org](https://www.lmsys.org/blog/2023-05-03-arena/)
11. [llms.txt — что это и нужен ли он сайту · Агентная оптимизация](https://agentoptimization.ru/llms-txt/)
12. [llms.txt Validator by Hostinger](https://llmstxtvalidator.org/)
13. [Beyond Demographic Discrimination: Benchmarking Normative ...](https://openreview.net/forum?id=WEhvEd8nhz)
14. [Beyond Marginal Distributions: A Framework to ...Beyond Demographics: Fine-tuning Large Language Models to ...Evaluating LLMs for Detecting Demographic-Targeted Social ...Evaluating LLMs for Detecting Demographic-Targeted Social Bias ...](https://arxiv.org/abs/2601.15755)
15. [Beyond Demographics: Fine-tuning Large Language Models to ...](https://aclanthology.org/2025.acl-long.104/)
16. [Evaluating LLMs for Detecting Demographic-Targeted Social ...](https://aclanthology.org/2026.iaai-1.5.pdf)
17. [Evaluating LLMs for Detecting Demographic-Targeted Social Bias ...](https://arxiv.org/html/2510.04641v1)