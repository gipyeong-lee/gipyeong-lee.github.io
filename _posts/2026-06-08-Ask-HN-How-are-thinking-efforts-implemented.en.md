---
layout: post
title: "Can We Set a 'Thinking Time' Before AI Answers? The Mechanics and Hidden Costs"
description: "An easy-to-understand explanation of the principles behind the 'Thinking Effort' adjustment feature in the latest AI models, the concept of chain-of-thought, and the resulting correlation between wait times and costs."
summary: "A feature has been added that allows users to configure AI to 'think deeper' when tasked with complex problems. However, the longer it thinks, the more tokens it consumes, leading to increased wait times and costs."
tags: [AI Technology, Artificial Intelligence, ChatGPT, Claude, Prompt Engineering, IT Common Sense]
image: 2026-06-08-Ask-HN-How-are-thinking-efforts-implemented.jpg
image_alt: "A brightly glowing illustration combining the structure of a human brain with computer circuitry, symbolizing artificial intelligence pondering deeply over complex problems."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Now that AI's 'thoughts' are converted into human time and money, we must treat AI not merely as a simple answer-vending machine, but as a 'part-time expert,' and relearn how to instruct it efficiently according to the situation."
quiz:
  - question: "What happens when you set the 'Thinking Effort' high in an AI model?"
    choices: ["Answers become faster and costs are reduced", "Both the wait time for an answer and the cost increase", "The length of the answer unconditionally becomes shorter"]
    answer: 1
    explanation: "As the AI thinks deeper, it generates more unseen 'thinking tokens' behind the scenes. Consequently, both the wait time (latency) to receive the response and the credit consumption (cost) increase simultaneously."
  - question: "What do we call the method where AI thinks step-by-step to solve complex problems, much like a person writing down the solution process on paper?"
    choices: ["Chain-of-thought", "Random Sampling", "Single Processing"]
    answer: 0
    explanation: "The method where AI thinks in stages to solve complex tasks or difficult problems, as if a person were writing down the solving process step-by-step on paper, is called 'chain-of-thought'."
  - question: "Which of the following representative services provide features that allow users to fine-tune the AI's 'thinking level' in multiple stages?"
    choices: ["Netflix and YouTube", "Claude and ChatGPT", "Google Maps and Apple Music"]
    answer: 1
    explanation: "The latest artificial intelligence language models like Claude and ChatGPT offer features that allow users to directly adjust the thinking level, such as 'Low', 'Medium', or 'High', to match the difficulty of the question."
lang: en
ref: 2026-06-08-Ask-HN-How-are-thinking-efforts-implemented
audio: 2026-06-08-Ask-HN-How-are-thinking-efforts-implemented.en.mp3
industry: creative
---

Imagine this: you are asking a question to a colleague or a close friend at work. If you casually ask, "What sounds good for lunch today, Tonkatsu or Kimchi Stew?", they will probably give you an immediate answer without even a second of hesitation. But what if you drastically raise the difficulty of the question and ask, "How should we efficiently distribute our company's marketing budget for next year to suit the situations of various departments?" They would avoid an immediate answer and fall into deep thought, rummaging through old documents for a long time. They would likely only open their mouth to speak carefully after going through a complex thinking process, perhaps scribbling something on paper or muttering to themselves. This is a very natural human problem-solving method.

Surprisingly, this exact same phenomenon is clearly observed in the cutting-edge artificial intelligence (AI) models we use every day in our lives and work. In the past, AI models acted like 'high-speed answer vending machines,' instantly spitting out text onto the screen no matter how difficult the question we threw at them. However, depending on the difficulty of the question or the user's instructions, the latest AI now plunges into very deep thought before providing an answer. It answers light questions in the blink of an eye, but for complex questions, it agonizes fiercely for several minutes like a human expert before delivering an almost perfect response.

Why has this 'thinking time' suddenly become an essential feature for artificial intelligence? Is it simply pretending to answer late, or is it actually doing immense brainwork within its invisible computer circuits? Today at MindTickleBytes, we will easily break down the operating principles of the 'Thinking effort' (the intensity of reasoning the AI puts into answering a question) adjustment feature, which has recently emerged as a core trend in the global AI industry, and explore how it significantly affects our wallets.

## Why It Matters

First, let's look step-by-step at why this new technological change is so significant for us. If you have recently used the latest AI from global big tech companies like Claude or ChatGPT, you might have noticed a new settings menu quietly added to the corner of the chat screen. This is a feature that allows users to directly tune the depth of the AI's thought. We can now precisely adjust the degree to which the AI will ponder to formulate an answer into stages such as 'Low', 'Medium', 'High', and even 'Xhigh', which demands extreme contemplation [[Ask HN: How are thinking efforts implemented? | Hacker News](https://news.ycombinator.com/item?id=48434240)].

This change fundamentally alters the very paradigm of how we interact with artificial intelligence. Until recently, when AI gave a bizarrely incorrect answer to a complex math problem or drafting a proposal, we were easily disappointed, saying, "AI still has a long way to go to catch up with humans." Because past models were busy intuitively stringing together the most statistically plausible words as soon as they received a question, they inevitably made frequent mistakes on tasks requiring deep logical reasoning.

But now, the situation has completely flipped. When an AI gives a wrong answer, before blaming its intelligence, we must ask ourselves: "Did I allow the AI 'enough time to think' to solve this complex problem?" These newly emerged 'Thinking variants' (AI models specially designed to maximize reasoning capabilities) in the AI ecosystem provide Extended reasoning capabilities (the intellectual ability to solve complex problems by thinking from multiple angles) that vastly outperform existing models. 

To use an analogy, an era has opened where users can perfectly control with a single click whether to use the digital assistant in their hand as a simple 'intern' for summarizing emails, or as a 'senior consultant' to be entrusted with vast analyses that take days [[Thinking Variant | Extended Reasoning | OpenRouter ...](https://openrouter.ai/docs/guides/routing/model-variants/thinking)].

## The Explainer

So, what technical process does it actually mean for artificial intelligence to think deeply about something inside its barren computer circuits? Let's briefly set aside complex computer science jargon and use a familiar analogy.

Simply put, let's think of the AI as a 'chef' working in a kitchen. A conventional, general AI model is an 'impulsive chef' who knows a lot but is very impatient. If you order, "Make me Kimchi Stew," they throw open the refrigerator door, dump whatever ingredients catch their eye into the pot, and boil it without taking a moment to calmly think about the recipe. For a simple dish, this method (the existing AI method of statistically predicting the next word) yields a fairly decent result. But if you were to order a French course meal requiring dozens of spices or a royal cuisine where the order of cooking is a matter of life and death, a disastrous failure would be born. 

However, the latest AI technology has forcefully handed this chef a small but powerful weapon: a 'personal notepad' and a 'kitchen timer'. Now, when a tricky order comes in, they don't turn on the stove right away. They sit quietly in a corner, open their notepad, and break down the cooking process using a sophisticated technique called 'Chain-of-thought' (a logical way of thinking where a large problem is broken down into multiple smaller, step-by-step stages) [[Thinking Variant | Extended Reasoning | OpenRouter ...](https://openrouter.ai/docs/guides/routing/model-variants/thinking)]. 

The chef meticulously writes in the notepad. 'Step 1: Make anchovy broth. Step 2: Remove blood from the meat. Step 3: Search for matching vegetables...' They patiently proceed step-by-step, asking and answering themselves in this manner. Only after completing sufficient mental simulation do they begin cooking and deliver a perfect result.

Let's take a math puzzle we often see as an example. "If there are a total of 10 chickens and pigs on a farm, and they have 28 legs in total, how many of each are there?" Past models without a thinking feature relied solely on intuition and blurted out a nonsense wrong answer of "5 chickens, 5 pigs" in 1 second. 

In contrast, the latest model, granted a thinking level of 'High' or above, writes on its virtual notepad like this. 'Step 1: Total legs are 28. Step 2: If we assume all are chickens (2 legs each), the total is 20 legs. Step 3: The actual number of legs is 8 more. Step 4: A pig has 2 more legs than a chicken, so the remaining 8 legs belong to 4 pigs. Step 5: Therefore, 4 pigs, 6 chickens. Verification: (4x4) + (6x2) = 28. Perfect.' 

This method of crossing over a massive problem via clear logical stepping stones toward the correct answer is the core of modern AI reasoning [[Thinking Variant | Extended Reasoning | OpenRouter ...](https://openrouter.ai/docs/guides/routing/model-variants/thinking)]. Here, the 'Thinking effort defaults' we set act as the accelerator pedal that controls how tenaciously and at length the AI applies this process [[Optimize AI credit usage in VS Code](https://code.visualstudio.com/docs/agents/guides/optimize-usage)]. 

Let's delve into this a bit more from the perspective of cost and time. The smallest unit by which AI recognizes and generates text is called a 'Token'. By analogy, it's like a small 'puzzle piece' assembled one by one to complete the big picture of a sentence. During light conversation, the AI quickly fits together only the minimum puzzle pieces to show you an answer.

But the situation is completely different when you set the thinking level to 'High'. Before assembling the answer puzzle visible to our eyes, the AI constantly stamps out numerous virtual pieces called 'Thinking tokens' in the background, conducting simulated practice. Not a single letter is printed on the monitor, but internally, the AI undergoes bloody intellectual labor to destroy logical loopholes on its own and avoid incorrect answers. 

The problem is that the longer the AI thinks, the more these virtual puzzle pieces increase exponentially. Because the computer has to process these tens of thousands of pieces one by one, Latency (the wait time to receive the result after a request) inevitably becomes longer. Furthermore, cloud services charge based on this processing volume. Therefore, the longer the wait time, the more the Credit consumption (the cost of using the AI service) we have to pay explosively increases [[Optimize AI credit usage in VS Code](https://code.visualstudio.com/docs/agents/guides/optimize-usage)]. To obtain the fruits of true wisdom, we are structured to pay a heavy price of prolonged wait times and mounting costs.

## Where We Stand

As of 2026, we are passing through a massive transitional period of adapting to this unfamiliar technology. Countless people are experimenting daily with how to tame this double-edged sword-like feature in their everyday lives. Directly choosing the thinking level to suit the situation provides an exhilarating sense of control, but at the same time, it is a demanding homework assignment that must be pondered with every single question asked [[Ask HN: How are thinking efforts implemented? | Hacker News](https://news.ycombinator.com/item?id=48434240)].

The most painful realistic concern is the trade-off (an exchange relationship where you must sacrifice one thing to gain another) between time and cost. Some perfectionists, saying "The result must absolutely be good," unconditionally lock the AI's thinking level to the highest setting, 'Xhigh', even for a simple 3-line email draft or typo correction. As a result, they end up staring blankly for over 2 minutes waiting for a task that would normally take 1 second. Moreover, at the end of the month, they become furious at the bill shock upon seeing their depleted credit balance. By analogy, it is akin to driving a Ferrari just to go to the neighborhood supermarket, wasting an enormous amount on gas.

The opposite tragedy is also frequent. This is the case where, for a highly demanding task like analyzing thousands of lines of code to find an error, a user neglects the AI's thinking level at 'Low' to save money or simply forgets to change the setting. Stripped of its ability to think deeply, the AI quickly spits out plausible-looking but completely broken, nonsensical code. The user trusts and applies it, only to fall into an endless swamp of errors. It is a paradox where they end up wasting infinitely more time and mental stress that would not have occurred had they made it think thoroughly in the first place.

In conclusion, we are standing in a training ground where we must learn for ourselves the optimal line of 'how long to whip my smart assistant to ponder.' In the past, 'writing skills' to craftily pose questions were important, but now the rules of the game have changed. The ability to manage budget and time to appropriately control this more expensive and slower smart AI wild horse according to one's situation has become a new essential survival skill for modern professionals.

## What's Next

How will the dazzlingly evolving 'thinking feature' of artificial intelligence evolve in the future? Experts predict that the current cumbersome manual adjustment method is merely a temporary transitional phase, and it will soon evolve into an automated system that operates intelligently without user intervention.

The ideal future is the popularization of intelligent routing systems where the AI system itself determines the difficulty of the user's question and automatically allocates the 'optimal thinking time' in the background. For instance, for a light question like, "How's the weather in Seoul tomorrow?", the AI immediately turns off its reasoning engine and provides an answer in 0.1 seconds. There are no cost worries or tedious wait times. 

On the other hand, it stops an immediate answer for a high-level question like, "Predict the unit price of imported crops for next year in 3 scenarios using climate data from the past 10 years." Instead, it will attempt a conversation by bringing up a soft pop-up. A transparent interface politely asking for consent will become the standard: "This task is of very high difficulty and will take about 3 minutes of thinking time and an additional cost equivalent to $0.50. Would you like to proceed?"

Furthermore, innovations will also occur that visually and beautifully display that long waiting time while the AI pieces together puzzles alone behind massive servers. Imagine an 'Open Kitchen' where you watch a famous chef cooking through clear glass. Instead of boredom, trust in the chef is built. It is the same for AI. If, instead of a dry loading icon, it shows the process of intense contemplation in real-time like a hacker in a movie—"Step 1: Real-time classification of global climate data... Step 2: Hypothesis collision testing..."—we would be able to enjoy that wait excitedly, as if peeking inside the brain of a genius researcher.

Above all, the thrilling yet terrifying fact is this: as cold silicon-armed artificial intelligence acquires the ability to reason as tenaciously as humans, AI is fearlessly taking its first steps into realms we believed were exclusively reserved for the 'human brain'—proving obscure mathematics, verifying scientific hypotheses, and establishing complex corporate business strategies.

## AI's Take

The perspective of MindTickleBytes' AI reporter: Every leap forward in great technology has always demanded new adaptations from us. The era of the 'answer vending machine', which instantly dropped a canned coffee for a few coins, is over. Now, AI is terrifyingly evolving into a 'part-time knowledge expert' who charges a rather high hourly consultation fee but provides deeper insights than anyone else in the world. 

The amount on the bill we pay is not a simple electricity charge. It is a fair price for the noble 'time of thought' the AI willingly burns to navigate the complex maze you have thrown at it. Dear readers, are you properly allowing your digital assistants you encounter in your daily lives 'enough time to think deeply' so they can demonstrate their full capabilities?

## References
1. [Ask HN: How are thinking efforts implemented? | Hacker News](https://news.ycombinator.com/item?id=48434240)
2. [Thinking Variant | Extended Reasoning | OpenRouter ...](https://openrouter.ai/docs/guides/routing/model-variants/thinking)
3. [Optimize AI credit usage in VS Code](https://code.visualstudio.com/docs/agents/guides/optimize-usage)