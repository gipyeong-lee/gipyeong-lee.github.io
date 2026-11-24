---
layout: post
title: "Are AI Answers on H5N1 Avian Flu Consistent Every Time? A Deep Dive into GPT-5 and Google Gemini 3 Flash Consistency"
description: "Easily understand research findings analyzing how consistently the latest AI models, GPT-5 and Google Gemini 3 Flash, answer questions related to H5N1 avian influenza."
summary: "Explore the reliability and consistency of AI health information through research on the semantic repeatability and reproducibility demonstrated by GPT-5 and Google Gemini 3 Flash on H5N1 One Health questions."
tags: [AI, GPT-5, Gemini, H5N1, OneHealth, Research]
image: 2026-11-24-Semantic-repeatability-and-reproducibility-of-GPT-5-and-Gemini-3-Flash-on-H5N1-O.jpg
image_alt: "AI model comparative analysis graphs and avian influenza data displayed on a lab monitor screen"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI has entered the crucible of reliability verification in the health and medical sector. Stability ensuring answers do not waver depending on questioning style will become a core competitive edge for future AI healthcare."
quiz:
  - question: "What are the two AI models investigated in this study?"
    choices: ["GPT-4 and Gemini 2", "GPT-5 and Gemini 3 Flash", "Claude and Llama"]
    answer: 1
    explanation: "The study experimented with OpenAI's GPT-5 and Google's Gemini 3 Flash."
  - question: "Where were the H5N1-related questions used in the study collected from?"
    choices: ["Medical paper abstracts", "Social media discourse", "Hospital patient records"]
    answer: 1
    explanation: "15 H5N1 One Health questions derived from social media discourse were used."
  - question: "Between repeatability and reproducibility, which metric was higher for GPT-5?"
    choices: ["Repeatability was higher", "Reproducibility was higher", "Both metrics matched exactly"]
    answer: 1
    explanation: "For GPT-5, reproducibility (consistency when question formats were changed) was significantly higher than repeatability."
lang: en
ref: 2026-11-24-Semantic-repeatability-and-reproducibility-of-GPT-5-and-Gemini-3-Flash-on-H5N1-O
audio: 2026-11-24-Semantic-repeatability-and-reproducibility-of-GPT-5-and-Gemini-3-Flash-on-H5N1-O.en.mp3
industry: healthcare
---

Imagine this. One morning, news breaks about the spread of highly pathogenic avian influenza (H5N1, a highly pathogenic virus capable of infecting various hosts such as birds and mammals). Feeling anxious, you pick up your smartphone and ask an artificial intelligence (AI) chatbot: "I think I might have come into contact with wild birds; what symptoms should I watch out for and how should I handle it?" 

The AI kindly and meticulously explains the symptoms and response methods. You feel reassured. But then a thought suddenly crosses your mind: "Wait, if I ask this question again in the exact same way, or phrase it slightly differently, will the AI give me the exact same accurate answer? Or is it just making things up on the spot each time?"

Recently, academia and the tech community have provided a deep answer to this very question. According to the study [Semantic repeatability and reproducibility of GPT-5 and Gemini 3 Flash on H5N1 One Health questions](https://arxiv.org/abs/2611.29859), a thorough investigation was conducted into how consistently OpenAI's GPT-5 and Google's Gemini 3 Flash (Google's representative high-speed AI assistant model)—cutting-edge Large Language Models (LLMs) capturing global attention—maintain consistency when answering health-related questions [[Source 1](https://arxiv.org/abs/2611.29859), [Source 7](https://deepmind.google/models/gemini/)]. 

---

## Why is this important?

Highly pathogenic avian influenza A (H5N1) has re-emerged as a major public health issue since 2024 from the perspective of 'One Health' (the concept that the health of humans, animals, and the environment is closely interconnected) [[Source 1](https://arxiv.org/abs/2611.29859)]. Whenever the virus spreads, the public increasingly relies on AI chatbots to obtain accurate medical information [[Source 1](https://arxiv.org/abs/2611.29859)].

A very critical issue arises here. Before evaluating the 'accuracy' of an AI, we must first understand how much 'consistency' its answers possess [[Source 1](https://arxiv.org/abs/2611.29859)]. If posing the exact same question leads to a response of "it is not dangerous" on one day and "go to the hospital immediately" on another, users would not be able to trust any of the answers. In other words, proving whether a single response given by an AI can fairly represent the model's actual behavioral patterns is essential [[Source 1](https://arxiv.org/abs/2611.29859)].

From the perspective of the general public, this acts as a safety guard ensuring that "the AI advice I rely on is not a product of coincidence." In the field of health information where health and lives are directly at stake, an AI's fickleness can immediately lead to confusion and danger. Therefore, measuring how steadfastly an AI maintains consistent answers is both a metric for evaluating technological maturity and a core task in reinforcing the safety net of public health.

---

## Easy to Understand: Repeatability, Reproducibility, and Chains of Thought

In this study, AI consistency was measured by dividing it largely into two concepts: **'Repeatability'** and **'Reproducibility'**. 

Let's use an analogy. 
* **Repeatability** is like checking how identical the taste is when an experienced barista pulls 30 shots of espresso using the exact same coffee beans and tools. That is, it refers to **how similar the AI's responses are when the exact same question is repeated word for word**.
* **Reproducibility** is checking whether the outcome remains essentially the same even when the phrasing of a recipe is slightly modified (e.g., asking "tell me the know-how for a delicious kimchi broth dish" instead of "how to boil kimchi stew") or the questioning method is varied. That is, it evaluates **whether the AI maintains the same truth even when the form or framework of the question changes**.

In addition, the researchers utilized a special method called **'Chain-of-Thought (CoT, a technique where the AI is instructed to sequentially write out logical reasoning steps until reaching a conclusion)'**. It is like a teacher instructing a student solving a difficult descriptive math problem, "Don't just solve it in your head; write out the equations step by step." This tested whether going through this process enables the AI to produce more logical and consistent answers. In particular, reasoning methods such as 'Differential Diagnosis' were highlighted as one of the best frameworks [[Source 1](https://arxiv.org/abs/2611.29859)].

---

## Anatomy of the Study: What 5,400 Responses Tell Us

To verify this massive consistency, the researchers underwent rigorous experimental design. 

First, 15 core One Health questions related to H5N1 avian influenza were carefully selected from actual conversations on social media [[Source 1](https://arxiv.org/abs/2611.29859)]. The scale of the experiment was vast. Each question was submitted directly 30 times, and running them through 5 different Chain-of-Thought variations 30 times each resulted in a total of **5,400 massive responses** collected [[Source 1](https://arxiv.org/abs/2611.29859)]. 

The collected responses underwent MPNet embedding (a technique converting text semantics into high-dimensional numerical vectors) and were analyzed via pairwise cosine similarity (a metric mathematically measuring how closely the directional meaning of two texts aligns), with various nonparametric tests and internal consensus statistical techniques mobilized to enhance statistical reliability [[Source 1](https://arxiv.org/abs/2611.29859)].

What were the results?

1. **Overall High Consistency**: Both OpenAI's GPT-5 and Gemini 3 Flash within Google's [Google Gemini](https://gemini.google.com/) ecosystem recorded **very high average consistency ranging from 0.93 to 0.97** based on scores rescaled between 0 and 1 [[Source 1](https://arxiv.org/abs/2611.29859), [Source 2](https://gemini.google.com/)]. This proved that both models possess a substantial level of stable response capability regarding public health questions posed by users.
2. **GPT-5's Unique Characteristic**: In the case of GPT-5, **reproducibility when questions were phrased differently was statistically significantly higher than repeatability when the exact same question was repeated** ($W = 3.0, p = 0.0003$) [[Source 1](https://arxiv.org/abs/2611.29859)]. This suggests that regardless of how users twist or differently express their questions, GPT-5 excels in penetrating their core essence and deriving consistent conclusions.
3. **Gemini 3 Flash's Balanced Performance**: On the other hand, Google's Gemini 3 Flash showed patterns where repeatability and reproducibility metrics almost matched to the point of being statistically indistinguishable ($W = 42.0, p = 0.33$) [[Source 1](https://arxiv.org/abs/2611.29859)]. This means that whether the question form changes slightly or is repeated, the pattern of semantic consistency exhibited by Gemini 3 Flash is highly stable and uniform.

---

## What Lies Ahead?

This study goes beyond simply ranking the performance of two AI models to determine superiority. It presents a new standard for **how reliability must be verified** in order to introduce AI chatbots as official information channels in the medical and healthcare sectors moving forward [[Source 1](https://arxiv.org/abs/2611.29859)].

In the near future, AI chatbots are highly likely to move beyond mere conversational partners to assume the role of official guides providing quarantine guidelines or infectious disease coping tips during public health crises. At that point, developers will not be able to rest easy on getting good scores in a single test, but will need to release 'consistency report cards' obtained through thousands of variant questions and repeated testing. 

Beneficial changes are also coming for users. The foundation of trust is solidifying, allowing us to obtain unwavering and consistent professional knowledge regardless of what words we use to ask questions or how many times we ask the AI the same question. As AI technology advances, its profile as a reliable assistant protecting our daily lives and health deepens accordingly.

---

## MindTickleBytes' AI Reporter Perspective

In the age of artificial intelligence, the biggest challenge we face is not "knowing the correct answer," but "can we trust that answer." This study on the response consistency of GPT-5 and Gemini 3 Flash regarding H5N1 is an excellent milestone demonstrating that AI is moving beyond a mere talker to stand upon a bedrock of trust that remains unshaken even amidst the solemn reality of health crises. As technology evolves, it is time for our mindset to become smarter as well.

---

## References

1. [Semantic repeatability and reproducibility of GPT-5 and Gemini 3 Flash on H5N1 One Health questions](https://arxiv.org/abs/2611.29859)
2. [Google Gemini](https://gemini.google.com/)
3. [Gemini— Google DeepMind | Our next era of frontier intelligence](https://deepmind.google/models/gemini/)
4. [Gemini 3 Pro vs GPT-5.2](https://evolink.ai/ko/blog/gpt-5-2-vs-gemini-3-pro-comparison-2026)
5. [Нейросеть Gemini 3.5 Flash — ИИ-модель Google AI](https://stiva.ai/models/gemini-3-5-flash)