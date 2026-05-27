---
layout: post
title: "AI Forgets English When It Learns French? The Rise of 'Self-Teaching AI'"
description: "Explore Self-Distillation technology, which solves 'catastrophic forgetting'—a critical weakness where AI forgets existing knowledge when learning something new."
summary: "'Self-Distillation Fine-Tuning (SDFT),' a technology that allows a single AI model to become both teacher and student, is showing remarkable results by learning new skills without losing past memories."
tags: [AI, Continual Learning, Machine Learning, Self-Distillation, Catastrophic Forgetting]
image: 2026-05-27-Self-Distillation-Enables-Continual-Learning-pdf.jpg
image_alt: "An illustration of a robot teaching itself knowledge while looking in a mirror"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Beyond simply being injected with external data, the way AI reflects on and corrects its own behavior to accumulate knowledge is becoming strikingly similar to the human lifelong learning mechanism."
quiz:
  - question: "What do we call the phenomenon where artificial intelligence severely forgets previously acquired skills and knowledge when learning a new skill?"
    choices: ["Off-policy drift", "Catastrophic forgetting", "Self-distillation"]
    answer: 1
    explanation: "The phenomenon where an AI loses its ability to perform previously mastered tasks due to significant changes in its internal numerical values when learning new information is called 'Catastrophic forgetting'."
  - question: "In the 'SDFT' technology introduced by researchers to enable continual learning in AI, what roles does the AI model perform simultaneously?"
    choices: ["User and Developer", "Hardware and Software", "Teacher and Student"]
    answer: 2
    explanation: "Within the SDFT framework, a single AI model simultaneously plays the role of a 'teacher' who knows the correct answers and guides, and a 'student' who learns through direct experience."
  - question: "What has been pointed out as one of the main reasons traditional 'Supervised Fine-Tuning (SFT)' fails in continual learning?"
    choices: ["Lack of data", "Off-policy drift", "Excessive power consumption"]
    answer: 1
    explanation: "Along with catastrophic forgetting, the traditional SFT method often fails due to 'Off-policy drift,' a phenomenon where the model learns only from external data rather than its own actual behavioral trajectories, creating a disconnect from reality."
lang: en
ref: 2026-05-27-Self-Distillation-Enables-Continual-Learning-pdf
audio: 2026-05-27-Self-Distillation-Enables-Continual-Learning-pdf.en.mp3
industry: education
---

Imagine this: You spent all day yesterday falling and scraping your knees, but you finally mastered how to ride a two-wheeled bicycle. You were thrilled to feel the wind as you rode. However, when you went to the pool today and learned how to float and swim freestyle, your mind suddenly went completely blank on how to pedal or balance with the handlebars. The moment you got back on the bike, you crashed to the ground as if you had never ridden one before. Wouldn't that be an incredibly absurd and frustrating situation?

Fortunately, this never happens to us humans. We perfectly remember how to ride a bike in the fall even after learning how to swim in the summer, and we don't forget our native language—Korean—even if we learn French as an adult. This is because our brains have an amazing ability to absorb new knowledge like a sponge while safely storing the past knowledge we already possess in a secure room in our minds. 

Surprisingly, however, this is a very common phenomenon for the cutting-edge artificial intelligence (AI) we admire and use today, and it is a severe weakness that must be overcome in the future. When AI is forcibly fed new knowledge, it has a fatal tendency to ruthlessly overwrite the precious skills it previously struggled to learn in order to accommodate that new information. Today, we will take an easy yet in-depth look at the latest research results on a remarkable technology that has emerged to solve this massive challenge: AI "teaching itself" as if looking in a mirror.

<br/>

## Why It Matters

AI researchers have given a very grim name to this terrifying phenomenon of "forgetting how to swim when you learn to ride a bike." It is called **"Catastrophic forgetting."** It literally means that the existing knowledge system collapses as if facing a catastrophe.

On the contrary, the process that allows a system to continuously acquire new skills and knowledge throughout its life without degrading existing abilities is called **"Continual learning."** This continual learning remains a fundamental challenge that even the massive foundation models serving as the backbone of modern AI, like ChatGPT, must overcome `[Self-Distillation Enables Continual Learning](https://www.emergentmind.com/papers/2601.19897)`. 

Why does this issue directly affect our everyday lives? Think of the personal assistant AI on your smartphone that listens to your voice and responds daily. This AI manages your complex schedule and recommends news perfectly suited to your tastes. Suppose you taught the AI a new rule today: "From now on, when summarizing work emails, always write a short three-line summary starting with the conclusion." An AI suffering from catastrophic forgetting would perfectly start following this new rule, but in exchange, it might completely forget an important rule you taught it last year: "Always set a reminder at 8 AM for family members' birthdays." Only when it can stack what it learned today on top of what it learned yesterday, like bricks, can we truly call that AI a smart, reliable assistant.

Until now, countless AI engineers have mainly used a traditional method called **"Supervised Fine-Tuning (SFT)"** when teaching new knowledge to AI. Simply put, this is a rote-learning approach where tens of thousands of "answer sheets" are thrust in front of the AI to memorize. However, this traditional SFT method often fails miserably when thrown into the real world, where new events occur daily and learning must continue endlessly. The core reasons for this failure are the aforementioned catastrophic forgetting and another headache known in technical terms as **"Off-policy drift"** `[Self-Distillation Enables Continual Learning | Papers | HyperAI](https://hyper.ai/en/papers/2601.19897)`. 

So, what exactly is off-policy drift? It is a disconnect from reality that occurs because, although the AI studies hard by looking at answer sheets, those answer sheets are not situations the AI created through its own trial and error, but rather "ideal situations" crafted by external experts in a controlled environment. 

Let's return to the swimming analogy. It is like a person who has never been in the water trying to learn by endlessly watching videos of an Olympic swimming gold medalist's perfect races. While watching the video in a warm room, they feel like they know all the arm angles and breathing timings (Supervised Fine-Tuning). However, when this person actually gets into a cold pool and starts flailing (the AI's actual operating environment), it is a completely different story. In a panicked situation from swallowing water, they have no idea how to adjust the perfect video posture to fit their own body, and they end up drifting further in the wrong direction while thrashing around. Ultimately, the AI falls into a deep dilemma where it loses past knowledge and fails to operate properly in new environments.

<br/>

## The Explainer

To rescue AI from this seemingly endless swamp of catastrophic forgetting and drift, researchers have proposed a highly elegant and groundbreaking solution. It is a new training method called **"Self-Distillation Fine-Tuning (SDFT)."**

In computer science, the term "Distillation" refers to a technique that extracts only the essence of deep knowledge from a massive, smart AI model and compresses it to transfer to a smaller, lighter model. Figuratively speaking, it is like the process of ladling out only the richest, most nutritious essence from a bone broth simmered for days and nights into a smaller bowl. So, what does "Self-Distillation" with "Self" attached to the front mean? It is an amazing and philosophical process where, instead of borrowing someone else's knowledge, the AI drinks the very essence it brewed itself to grow.

This fascinating **"On-Policy Self-Distillation"** framework allows a single AI model to simultaneously play the role of a **"teacher"** who knows the direction of the perfect answer, and a **"student"** who is still clumsy but takes direct action `[Self-Distilled Reasoner: On-Policy Self-Distillation for Large](https://arxiv.org/html/2601.18734v3)`. 

With this analogy, the complex technology will be much easier to picture in your mind. Imagine a single cook in a bustling kitchen. Inside this cook, two personas exist simultaneously. One is the persona of a "master chef (teacher)" who remembers all the culinary theories and the standards for perfect taste, and the other is the persona of a "novice chef (student)" who is just starting to make a new recipe by hand and occasionally spills the salt. 

In the traditional rote-learning approach (SFT), an external, real master chef would constantly show the novice chef pictures of completed 5-star dishes, yelling, "Make it exactly like this!" The novice chef cooks only by looking at the pictures, and when they make a mistake, they panic and wander off without knowing why they ruined it (Off-policy drift). 

However, a completely different scene unfolds in the SDFT method. The novice chef (student model) first chops on the cutting board and adjusts the stove's flame, **creating their own path of action (technically called Trajectories).** Then, the master chef (teacher model) within watches the clumsy "actual behavior" the novice just performed clearly and delivers customized advice (predictions) tailored perfectly to "that very moment, that situation" rather than some distant right answer. It gives feedback like, "Your wrist angle was off just now when you chopped the onion. Don't just blindly try to copy the final answer; in your current posture, try lifting the knife a bit higher."

This is the core technical principle of how SDFT works. The AI's training process takes place strictly on the actual trajectories generated by the student model itself. On those trajectories, the teacher's wise predictions are immediately distilled and taught to the student. Through this, AI breaks free from the past limitations of having to explicitly undergo complex calculations or passively imitate external answers. It produces living **"On-policy updates"** by extracting only the essential core information from an expert's demonstration and melting it perfectly into its own experience `[SELF-DISTILLATION ENABLES CONTINUAL LEARNING Idan Shenfeld1 2∗ Mehul Damani1](https://arxiv.org/pdf/2601.19897)`. 

Because the student receives the teacher's wisdom at the right time and place based on the experiences they personally faced in reality (on-policy), they can solidly master new recipes without forgetting the foundation of the dishes they already knew how to cook (past knowledge).

<br/>

## Where We Stand

So, how well is this "self-teaching AI" that questions and answers itself inside its head actually performing in the lab? The diverse experimental results released by the researchers clearly demonstrate a major leap forward in artificial intelligence learning methods.

Across a broad range of test environments that require learning various new skills and sequentially acquiring complex knowledge, the new method, SDFT, consistently and overwhelmingly outperformed the traditional method, SFT. This doesn't just mean a minor accuracy improvement of getting a few more questions right. It succeeded in **substantially reducing the phenomenon of catastrophic forgetting**—a long-standing goal that countless scientists lost sleep over trying to solve `[[2601.19897] Self-Distillation Enables Continual Learning](https://arxiv.org/abs/2601.19897)`. The AI finally figured out how to peacefully accept new knowledge in a new space next to past knowledge, keeping the latter firmly locked inside a safe vault.

The most dramatic and interesting results emerged in the **Sequential learning experiments**. This experiment is a test that pushes AI to the limit. It was a harsh environment where the AI was first taught complex mathematical formulas, then world history, and immediately after, computer programming in succession. A standard, conventional AI would have erased the math formulas in its head when learning history, and completely wiped the previously learned historical dates when learning programming. 

However, when the SDFT technology was applied, something amazing happened. A single AI model demonstrated the remarkable ability to stably accumulate completely different and complex skills—math, history, and programming—in its brain over time without losing or regressing in performance from previous subjects `[Paper page - Self-Distillation Enables Continual Learning](https://huggingface.co/papers/2601.19897)`. 

This is not merely playing with numbers in a lab. This brilliant achievement by the researchers signifies that the method of on-policy distillation has perfectly established a highly **practical and robust path** that helps AI continue learning continuously from expert demonstrations without collapsing `[SDFT: Self-Distillation Enables Continual Learning](https://self-distillation.github.io/SDFT)`. Furthermore, it was also confirmed that this simple self-distillation process works excellently using only the raw outputs generated by the AI itself, without the complex help of expensive external verifiers or other auxiliary models `[Embarrassingly Simple Self-Distillation Improves Code Generation](https://arxiv.org/html/2604.01193v1)`.

What is even more encouraging is that the ripple effect of this self-distillation technology is not confined to reading and writing text. This powerful principle is expanding into various areas across imaginable industries. 

For example, when an AI visually learns the Graphical User Interface (GUI) environment we use on computers or smartphones, this technology distills the "master's" ideal mouse click position distribution at every step. This provides continuous learning signals so that the AI can manipulate the screen much more smartly and efficiently without clicking the wrong buttons `[Learn where to Click from Yourself: On-Policy Self-Distillation](https://arxiv.org/html/2605.00642v1)`. 

Additionally, it saves an enormous amount of time and money in industrial defect detection models that find product flaws in factories. When a new type of defect is discovered, there is no longer a need to turn off the entire AI model and retrain it from scratch for hundreds of hours like in the past. Thanks to self-distillation technology, the model can now continuously learn and append new defect classes onto its existing knowledge, like sticking a sticker, without needing a complete overhaul and retraining `[(PDF) SD-IDD: Selective Distillation for Incremental Defect](https://www.researchgate.net/publication/401174708_SD-IDD_Selective_Distillation_for_Incremental_Defect_Detection)`. 

Even in the field of 4D Perception, which acts as the eyes of robots—the crown jewel of future industries—this technology is playing a major role. By utilizing the ever-changing context of space and time, it establishes an incredible self-improvement system where the AI model enhances its own perception abilities day by day, laying the foundation for robotics technology `[Self-Improving 4D Perception via Self-Distillation - Paper](https://deeplearn.org/arxiv/731351/self-improving-4d-perception-via-self-distillation)`. It is effectively breaking down old training paradigms across countless fields and throwing wide open the horizons of new evolution `[D-OPSD: On-Policy Self-Distillation for Continuously Tuning](https://deeplearn.org/arxiv/745499/d-opsd:-on-policy-self-distillation-for-continuously-tuning-step-distilled-diffusion-models)`.

<br/>

## What's Next

"The continual learning routinely performed by humans and animals is an 'always-on' learning that requires absolutely no distinction between lab 'training' time and real-life 'inference' time. And this great learning truly begins at the very moment of 'prediction failure' when our expectations are wrong." `[Self-Distillation Enables Continual Learning [pdf] | HackerNews](https://news.ycombinator.com/item?id=48165265)`.

The most powerful and philosophical message that this research outcome throws toward our future is entirely captured within this sentence. In the past, AI had to live a life strictly divided in two. 

There was a period of undergoing harsh "Training," devouring the world's data inside computers in a lab with giant air conditioners running. Only after that training was completely finished did it live out its "Inference (execution)" phase—rigidly installed on your device, answering only as it had been taught. Once released into the world, the clock inside the AI's head was completely stopped. To learn even a single new piece of knowledge, it had to halt its services, return to the lab, and undergo the heavy and expensive training process all over again from the beginning.

However, self-distillation technologies like SDFT are finally tearing down this formidable barrier between "training" and "execution." What if AI could self-correct its mistakes during the execution process and fuse yesterday's knowledge with today's new knowledge from within? AI, too, would no longer be a stagnant machine, but would proudly step onto the path of an "always-on" lifelong learner that studies and grows every waking moment, just like humans. 

The AI we will encounter in our daily lives from now on will talk with us every day and become smarter today than it was yesterday. It will immediately understand a newly coined word trending today while keeping its ability to interpret the deep meaning of classic literature learned a decade ago completely intact and untarnished. An endlessly probing assistant that explores new worlds like a sponge, yet never forgets who it originally was or what it knew in the past—a truly wise companion. That is the thrilling tomorrow that "self-teaching AI" is about to throw wide open.

<br/>

## MindTickleBytes AI's Perspective

Although artificial intelligence is said to be modeled after the human brain's neural networks, it is true that it always seemed like an endlessly cold machine when faced with the flaw of "catastrophic forgetting"—erasing the old entirely when learning something new. 

However, breaking away from the method of blindly memorizing perfect answer sheets handed over by human researchers, the training philosophy of Self-Distillation—where it carefully reflects on its own immature behavioral trajectories and constantly seeks advice from the "master" deeply seated within—leaves a profound impression. This technology is evolving artificial intelligence one step beyond a simple calculator, bringing it closer to a living organism that reflects on itself and grows. 

Not losing one's compass amidst an endless flood of new information requires inner reflection, not external injection. The scientific fact that this self-reflecting technology applied to machine algorithms is, ironically, the secret to the most powerful and long-lasting memory, leaves a long and heavy resonance on the lives and attitudes toward learning of us humans, who must live and learn for a lifetime. True growth, after all, begins with looking back at who I am today without losing who I was yesterday.

<br/>

## References

1. [Self-Distilled Reasoner: On-Policy Self-Distillation for Large](https://arxiv.org/html/2601.18734v3)
2. [Embarrassingly Simple Self-Distillation Improves Code Generation](https://arxiv.org/html/2604.01193v1)
3. [Learn where to Click from Yourself: On-Policy Self-Distillation](https://arxiv.org/html/2605.00642v1)
4. [(PDF) SD-IDD: Selective Distillation for Incremental Defect](https://www.researchgate.net/publication/401174708_SD-IDD_Selective_Distillation_for_Incremental_Defect_Detection)
5. [D-OPSD: On-Policy Self-Distillation for Continuously Tuning](https://deeplearn.org/arxiv/745499/d-opsd:-on-policy-self-distillation-for-continuously-tuning-step-distilled-diffusion-models)
6. [Self-Improving 4D Perception via Self-Distillation - Paper](https://deeplearn.org/arxiv/731351/self-improving-4d-perception-via-self-distillation)
7. [[2601.19897] Self-Distillation Enables Continual Learning](https://arxiv.org/abs/2601.19897)
8. [SELF-DISTILLATION ENABLES CONTINUAL LEARNING Idan Shenfeld1 2∗ Mehul Damani1](https://arxiv.org/pdf/2601.19897)
9. [(PDF) Self-Distillation Enables Continual Learning](https://www.researchgate.net/publication/400118857_Self-Distillation_Enables_Continual_Learning)
10. [Paper page - Self-Distillation Enables Continual Learning](https://huggingface.co/papers/2601.19897)
11. [SDFT: Self-Distillation Enables Continual Learning](https://self-distillation.github.io/SDFT)
12. [Self-Distillation Enables Continual Learning | Papers | HyperAI](https://hyper.ai/en/papers/2601.19897)
13. [Self-Distillation Enables Continual Learning](https://www.emergentmind.com/papers/2601.19897)
14. [Self-Distillation Enables Continual Learning [pdf] | HackerNews](https://news.ycombinator.com/item?id=48165265)