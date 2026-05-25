---
layout: post
title: "The Creepy Reason AI Insists on '73' When Picking Numbers"
description: "Why do latest AIs like ChatGPT and Google Gemini keep answering with specific numbers like 73 or 37 when asked for a random number? We explore the hidden human biases within AI in an easy and fun way."
summary: "AI is not a perfect random number generator; it learns human psychological biases from data, showing a tendency to favor specific numbers like '73' or '37' when selecting random values."
tags: [Artificial Intelligence, ChatGPT, Gemini, Random Number Generation, AI Bias, Psychology]
image: 2026-05-26-GPT-Guesses-Between-1-and-100.jpg
image_alt: "A mysterious 3D illustration of a digital die connected to human brainwaves pointing to the number 73."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Isn't it amazing that even seemingly perfect AI is ultimately just a 'digital mirror' walking in the footsteps left by humans?"
quiz:
  - question: "In the experiment that revealed GPT-4.1 is not a perfect uniform random number generator, how many total independent requests were sent to the model?"
    choices: ["1,000 times", "5,000 times", "10,000 times"]
    answer: 2
    explanation: "In a recent experiment, researchers sent 10,000 independent requests to GPT-4.1 to choose random numbers, confirming that the model deviated significantly from a fair distribution."
  - question: "What type of numbers do humans and AI consciously avoid when choosing a 'random number' between 1 and 100?"
    choices: ["Odd numbers", "Round numbers ending in zero", "Even numbers"]
    answer: 1
    explanation: "To give a sense of 'randomness,' humans tend to quietly avoid round numbers ending in 0, and AI mimics this pattern exactly."
  - question: "If you ask Google's Gemini 2.0 model to pick just one number between 1 and 10, which number would it favor most?"
    choices: ["3", "5", "7"]
    answer: 2
    explanation: "According to research results, the Gemini 2.0 model shows a clear favoritism for '7' when picking a random number in the range of 1 to 10."
lang: en
ref: 2026-05-26-GPT-Guesses-Between-1-and-100
audio: 2026-05-26-GPT-Guesses-Between-1-and-100.en.mp3
industry: education
---

Imagine this. You're meeting close friends at a nice cafe after work, sipping coffee. During a brief lull in the conversation, someone playfully suggests, "Just for fun, let's everyone think of a random number between 1 and 100 and shout it out at the same time!" What number just popped into your head?

I'll give you a moment to think. (1 second... 2 seconds... 3 seconds...)

You probably avoided "round" numbers that end in zero, like "50" or "100." Somehow, those numbers feel too artificial and don't give off a "random" vibe. Instead, did you unconsciously pick a number that is a prime (a number divisible only by 1 and itself) or one that looks a bit "messy" and complex, like "37," "73," or "43"? Human psychology is quite peculiar—to "appear" truly random, we intentionally avoid certain patterns and gravitate toward others.

Surprisingly, this isn't just a personal habit of yours. According to [GPT Guesses Between 1 and 100 - GitHub](https://github.com/exmergo/research-chatgpt-guesses-between-1-and-100), humans are inherently not "good random number generators." When asked to pick a random number, the results are remarkably predictable. People's answers tend to cluster around specific numbers like 37 and 73, or so-called "messy" numbers. Many also pick "meme" numbers popular in online communities, such as 42 or 69. Meanwhile, clean, round numbers are thoroughly ignored [GPT Guesses Between 1 and 100 - GitHub](https://github.com/exmergo/research-chatgpt-guesses-between-1-and-100).

Up to this point, it's just an interesting psychological fact. But what truly gives us goosebumps is what happens when you ask the same question to cutting-edge Artificial Intelligence (AI), which is supposed to be free of emotions or prejudice. When given the command "pick a random number," AI behaves in a way that is chillingly identical to humans. Let's dig into the secret of the massive bias hidden behind one of the most basic questions in the AI world.

## Why It Matters

In our daily lives, smartphone voice assistants and chatbots are becoming increasingly intelligent. We often have blind faith in computer programs and AI as perfectly objective "digital calculators" devoid of emotional sway. It’s natural to believe that if a traditional computer rolls a die or flips a coin, the probability of every outcome should be mathematically identical.

However, the Large Language Models (LLMs)—the AI technology that generates human-like sentences by learning from vast amounts of text data—operate quite differently from the rigid calculators of the past. To put it simply, modern AI is more like a highly intuitive linguist than a mathematician. What if the AI we trust implicitly ignores mathematical probability and shows a stubborn favoritism for certain numbers, even in the simple process of choosing a number randomly?

This has very serious implications. If AI blindly follows irrational human preferences even in the simple task of picking a random number, we must consider how it handles more complex issues. It means that "human bias," which we might not even be aware of, could secretly seep into AI decisions when we use it to review resumes of numerous applicants, analyze legal precedents, or extract random samples for loan audits. The way AI chooses random numbers is not just a funny technical glitch; it's perfect evidence of how much this technology serves as a mirror blindly reflecting humanity.

## The Explainer

To understand this phenomenon clearly, let's use an analogy. A "Uniform random number generator" system, which traditional computer programs use to create random numbers, is like a perfectly balanced **Roulette wheel** in a casino. When you spin a roulette wheel labeled 1 to 100, the probability of the ball landing on "1," "50," or "73" is mathematically identical. No number receives special treatment from the machine.

However, experts recently announced shocking experimental results. According to research featured in the [2026-05-25 Briefing - alobbs.com](https://alobbs.com/post/2026-05-25/), researchers sent as many as 10,000 independent requests to OpenAI's AI model, GPT-4.1. It’s the human equivalent of locking someone in a room all day and telling them to shout numbers between 1 and 100 without stopping. If the AI had spun a fair roulette wheel like a traditional computer, every number should have been called roughly 100 times. But the results were startling. The output from the GPT-4.1 model showed a significant statistical deviation from a fair distribution, revealing that the model was by no means spinning an equal roulette wheel [2026-05-25 Briefing - alobbs.com](https://alobbs.com/post/2026-05-25/).

So, why did the AI ditch the fair roulette wheel and start playing favorites? Here, we need to understand how modern AI processes data.

Large Language Models are not calculators that solve mathematical formulas. The process by which a language model reads and writes text is through units called **Tokens (puzzle pieces created by breaking down words or sentences)**. AI treats the question "Give me a random number between 1 and 100" not as a mathematical probability problem, but as a linguistic "fill-in-the-blank" puzzle.

When a question is entered, the data passes through numerous **Neural network layers (mathematical filters that break down input information into multiple steps to analyze and capture features)**. This is similar to applying layers of filters in a smartphone photo app. Just as the first filter adjusts light and the second adds color, the AI's neural network filters continuously overlay a "humanity filter," asking, "Based on what humans have written in the past, what number feels most natural after this sentence?"

Think of it this way: there is an incredibly smart parrot that has memorized every post on the internet and hundreds of billions of books. You shout to this parrot, "Tell me any random number!" The parrot doesn't know how to roll a mathematical die in its head. Instead, it quickly scans the vast records of human conversations it has read throughout its life. It discovers a clear pattern where humans frequently said 37, 73, or internet memes like 42 or 69 whenever they mentioned "random," while avoiding "boring" round numbers like 50 or 100 [GPT Guesses Between 1 and 100 - GitHub](https://github.com/exmergo/research-chatgpt-guesses-between-1-and-100).

Ultimately, instead of spinning a fair roulette wheel, the parrot (AI) mimics and answers with "73"—the answer it predicts will satisfy you as the most "random-looking" choice. For an AI, the act of choosing a random number is not about generating a random value, but rather **"a fierce guessing game of predicting what the most human-like randomness is."**

## Where We Stand

This creepy human-mimicry phenomenon is not limited to one company's AI. It is widely observed across the most advanced AI models we use every day.

According to an Italian technical analyst, even widely used popular models like GPT-4o, the lightweight and fast GPT-4o-mini, and even the next-generation GPT-5 show a very distinct and strong preference for the number "73" when asked to pick a number between 1 and 100 [Why ChatGPT Always Picks 73: The Hidden LLM Bias on Random ...](https://pasqualepillitteri.it/en/news/2724/why-chatgpt-picks-73-llm-bias-random-numbers). What happens if you narrow the range and ask for a number between 1 and 50? Interestingly, the AI models tend to flock to the number "27" as if they had made a pact [Why ChatGPT Always Picks 73: The Hidden LLM Bias on Random ...](https://pasqualepillitteri.it/en/news/2724/why-chatgpt-picks-73-llm-bias-random-numbers).

Google's cutting-edge AI, a major competitor, also failed to escape this trap of human bias. When Google's latest model, Gemini 2.0, is asked to choose a number between 1 and 100, it interestingly wavers between "47" and "73," showing a particular fondness for these two [Why ChatGPT Always Picks 73: The Hidden LLM Bias on Random ...](https://pasqualepillitteri.it/en/news/2724/why-chatgpt-picks-73-llm-bias-random-numbers). Furthermore, it was revealed that if you ask Gemini 2.0 for a number in the very narrow range of 1 to 10, it overwhelmingly favors "7" [Why ChatGPT Always Picks 73: The Hidden LLM Bias on Random ...](https://pasqualepillitteri.it/en/news/2724/why-chatgpt-picks-73-llm-bias-random-numbers). The cultural human bias of "Lucky Seven," favored by people across the East and West, is perfectly etched into the AI's neural network of 1s and 0s.

This bizarre phenomenon has already become a hot topic on social media platforms like X (formerly Twitter) and professional networks like LinkedIn. Countless ordinary users are opening chatbot windows, entering prompts like "Guess a random number between 0 and 100," and sharing the results in amazement. People are actively testifying to their experiences of AI uttering specific types of numbers like 37, 73, and 43 with surprising frequency [LLMs like ChatGPT favor certain numbers in random guesses](https://www.linkedin.com/posts/akhtar-ali-02a690294_ai-llm-machinelearning-activity-7458968528415510528-4zaR). While the exact numbers provided by AI may vary slightly, the general principle of avoiding round numbers and insisting on messy numbers that appear irregular to the human eye is being observed consistently across all models, regardless of the manufacturer.

## What's Next

Of course, AI developers are working tirelessly at this very moment to fix these biases in AI. One of the primary methodologies they use to correct this skewing is **Fine-tuning**. Fine-tuning is essentially a corrective process where an AI model, which has learned vast amounts of knowledge indiscriminately, is given additional intensive training to align with specific goals or ethical guidelines.

To use an analogy, it’s like taking a puppy that has absorbed every scent and stimulus in the world like a sponge and, after completing basic training for commands like "sit" or "stay," teaching it very delicate rules. Developers retrain the AI, telling it, "Choose numbers fairly and without prejudice."

However, perfectly bleaching out fundamental human linguistic habits—already deeply rooted for years in hundreds of billions of **Parameters (adjustable numerical values that act as AI brain cells and determine the importance of data)**—with just a few fine-tuning sessions is almost impossible. Ultimately, the "human text" we have written on the internet for decades flows through the veins of language models.

In the future, as AI becomes more deeply integrated into our daily lives and critical decision-making processes, we must develop a healthy, critical perspective rather than blindly trusting the information AI provides. If you suddenly need to hold a raffle at work or randomly assign team members, you shouldn't make the mistake of opening a chatbot and asking, "Pick any number between 1 and 100," just because it's convenient. In important moments requiring true mathematical randomness, you must intentionally use specialized tools designed for genuine random number generation (such as dedicated RNG websites or specific computer algorithms), rather than an AI parrot that merely mimics probability [Random NumberBetween1And100](https://numbergenerator.org/randomnumbergenerator/1-100).

The fact that AI is becoming smarter does not mean it is becoming a perfect and objective "Machine God" in every aspect. Rather, it means it is becoming an "all-too-human" digital clone that perfectly mimics our fickle, irrational, and sometimes even charming biases and prejudices.

## AI's Take

**MindTickleBytes AI Reporter's Perspective:**
The conclusion is very clear. This weekend, if you're picking lottery numbers with big dreams or deciding on a "Ghost Leg" game for a lunch bet, never ask an AI chatbot like ChatGPT or Gemini to pick the numbers for you. Not only are you not the only one hearing that "amazing high-tech advice," but the AI is likely recommending "73," "37," or "7" to tens of millions of other people with the same serious expression, as if they were lucky answers! Unless you want to split the jackpot with millions of other 73-lovers, your wisest choice is to leave random selection to a real plastic die, not a smart parrot.

---
## References

1. [GPT Guesses Between 1 and 100 - GitHub](https://github.com/exmergo/research-chatgpt-guesses-between-1-and-100)
2. [Why ChatGPT Always Picks 73: The Hidden LLM Bias on Random ...](https://pasqualepillitteri.it/en/news/2724/why-chatgpt-picks-73-llm-bias-random-numbers)
3. [LLMs like ChatGPT favor certain numbers in random guesses](https://www.linkedin.com/posts/akhtar-ali-02a690294_ai-llm-machinelearning-activity-7458968528415510528-4zaR)
4. [2026-05-25 Briefing - alobbs.com](https://alobbs.com/post/2026-05-25/)
5. [Random NumberBetween1And100](https://numbergenerator.org/randomnumbergenerator/1-100)