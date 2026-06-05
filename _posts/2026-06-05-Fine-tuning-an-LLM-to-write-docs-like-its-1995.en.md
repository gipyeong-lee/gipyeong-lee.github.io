---
layout: post
title: "Injecting '1995 Vibes' into Cutting-Edge AI: Building a Custom AI Assistant on Your Laptop"
description: "An easy-to-understand guide using everyday analogies to explain 'fine-tuning' and LoRA adapters, showing how to make the latest AI speak like a 1990s technical writer using just a laptop."
summary: "By utilizing fine-tuning techniques that attach small, lightweight adapters to Large Language Models (LLMs), you can perfectly transform AI into your desired domain expert right on your personal laptop."
tags: [Artificial Intelligence, Fine-tuning, LLM, LoRA, AI Assistant]
image: 2026-06-05-Fine-tuning-an-LLM-to-write-docs-like-its-1995.jpg
image_alt: "A retro-style image showing cutting-edge artificial intelligence code being typed in green text on an old, bulky 1990s computer monitor"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "The true value of artificial intelligence will explode not from standardized correct answers, but from 'personalization'—the ability to tame it to perfectly fit your tastes and purposes."
quiz:
  - question: "What is the name of the fine-tuning technique that creates and merges a small, lightweight adapter instead of heavily modifying the entire original language model?"
    choices: ["ChatGPT", "LoRA", "Llama 3.1"]
    answer: 1
    explanation: "Instead of modifying all parameters of the base model, LoRA (Low-Rank Adaptation) enables efficient training by generating a small adapter that can be merged when needed."
  - question: "What was the hardest core element to obtain when training the model to write like a software technical writer from the 1980s and 90s?"
    choices: ["A house-sized supercomputer", "A massive amount of high-quality written materials (training data)", "A budget of billions of won"]
    answer: 1
    explanation: "While the fine-tuning process itself is inexpensive, securing numerous written materials (high-quality training data) in the targeted style is the most difficult part of training a model."
  - question: "In the recent experiment, what device was used to seamlessly run models with approximately 8 billion (8B) parameters?"
    choices: ["Amazon Data Center", "Personal laptop (MacBook Air)", "Large mainframe server"]
    answer: 1
    explanation: "These language models, with about 8 billion (8B) parameters, can run quite comfortably even on a typical consumer-grade personal laptop like a MacBook Air."
lang: en
ref: 2026-06-05-Fine-tuning-an-LLM-to-write-docs-like-its-1995
audio: 2026-06-05-Fine-tuning-an-LLM-to-write-docs-like-its-1995.en.mp3
industry: education
---

Imagine this. One morning, you ask your smartphone's AI assistant, "Could you write a user manual for my new app?" Normally, it would spit out an answer in smooth, polished, modern prose. But what if this AI, as if stepping out of a time machine, started churning out text in the stiff, clunky writing style of the 1990s Windows 95 era? Delivering retro vibes like, "Please insert the floppy disk into the drive and click execute."

Surprisingly, someone has turned this fun and quirky imagination into reality. Recently, a developer successfully experimented with training a modern AI to write like a software technical writer from the 1980s and 90s [[Fine-tuning an LLM to write docs like it's 1995 - vuink.com](https://vuink.com/post/cnffb-d-dhab/fine-tuning-docs-llm)]. This story is not just an interesting episode about reviving old-school nostalgia. It is a decisive scene that demonstrates just how deeply AI technology has moved beyond the hands of massive corporations and into our everyday lives and personal control.

In our imaginations, AI development has always been grandiose. We thought it was something possible only in the secret labs of massive tech giants or in server rooms housing thousands of computers blasting immense heat. However, the magic of creating this remarkable '1995-vibe AI assistant' happened right on an ordinary personal laptop—the kind you might rest on your lap while sipping coffee at a cafe. How on earth did this become possible?

## Why It Matters

We usually think of giant AIs like ChatGPT as 'know-it-alls'. However, what businesses and individuals truly want in their daily lives and work isn't a 'well-rounded AI' that scores a mediocre 70 in every field. What we genuinely crave is 'my own custom expert AI' that perfectly understands the nuances of my work, thinks like I do, and works in my style. No matter how nice clothes from a ready-to-wear store might be, they can never beat the comfort of a bespoke suit tailored perfectly to your body.

The process of training freely accessible open-source Large Language Models (LLMs—AIs that understand language like humans by reading and learning from vast amounts of text) to suit our purposes unlocks immense potential for hyper-personalizing artificial intelligence [[Fine Tune an open-source LLM - ashutosh.dev](https://www.ashutosh.dev/how-to-fine-tune-an-open-source-llm-step-by-step-2025-edition/)]. 

For example, you can create an assistant that uses complex legal jargon for a lawyer poring over vast precedents, a dedicated developer aide that mimics your exact coding habits, or a secretary that trims long, boring meeting minutes down to the key points just the way you like them. You can build all these top-tier experts with your own hands [[Fine Tune an open-source LLM - ashutosh.dev](https://www.ashutosh.dev/how-to-fine-tune-an-open-source-llm-step-by-step-2025-edition/)]. 

The greatest significance of this technology is that it grants us 'complete control', 'consistency', and deep 'expertise' over AI [[Fine Tune an open-source LLM - ashutosh.dev](https://www.ashutosh.dev/how-to-fine-tune-an-open-source-llm-step-by-step-2025-edition/)]. 'Dedicated AIs', which in the past could only be built with tens of millions of dollars in capital and brilliant researchers, can now easily be created by everyday individual developers or small local businesses. The so-called massive shift in AI power has begun.

## The Explainer

At the core of all this magic lies a key technology called **'Fine-tuning'**. While it might sound like an unfamiliar technical term, its underlying principle is surprisingly similar to our everyday lives. Simply put, fine-tuning is a special training process that adapts a smart base AI model (Foundation LLM)—which has already learned vast amounts of general knowledge—once more to fit a specific task [[LLMs:Fine-tuning, distillation, and prompt engineering](https://developers.google.com/machine-learning/crash-course/llm/tuning)]. The interesting part is that through this training, the AI's performance on specific tasks improves dramatically, while the overall size of the model doesn't bloat but stays as lean as it originally was [[LLMs:Fine-tuning, distillation, and prompt engineering](https://developers.google.com/machine-learning/crash-course/llm/tuning)].

To use an analogy: a freshly downloaded base AI is like a 'brilliant new hire' who just graduated at the top of their class from a prestigious university. This new hire has absorbed all sorts of knowledge from the internet and knows a tremendous amount. However, since it is their first time experiencing corporate life, they know absolutely nothing about your company's unique approval document formats or the specific jargon used among senior colleagues. 

The on-the-job training process where you sit this smart new hire down, show them 1,000 past company documents, and say, "Your foundational knowledge is excellent, so keep it, but from now on, you need to write exactly in the style of these documents"—that is fine-tuning. In the aforementioned 1995-vibe documentation experiment, this new hire was essentially force-fed a mountain of old, rigid technical documents from the 1980s and 90s and put through intensive acting classes to sound just like someone from that era.

However, this special training isn't always smooth sailing. While the computational process of training the model itself can be relatively inexpensive, the biggest hurdle that determines the success or failure of this training is the need to gather enough 'high-quality training data' [[Fine-tuninganLLMtowritedocslikeit's1995– Fabrizio Ferri...](https://passo.uno/fine-tuning-docs-llm/)]. To train a personalized model so the AI writes naturally like a person from the 1990s, a massive amount of text (data) actually used during that era is absolutely necessary [[Fine-tuning an LLM to write docs like it's 1995 - vuink.com](https://vuink.com/post/cnffb-d-dhab/fine-tuning-docs-llm)]. Producing high-quality learning materials is by no means easy, and even if you find the perfect textbook, you must carefully select a smart base model capable of perfectly grasping its contents [[Fine-tuninganLLMtowritedocslikeit's1995– Fabrizio Ferri...](https://passo.uno/fine-tuning-docs-llm/)].

Add to this another remarkable magic dust that changed the history of computing: a technique called **LoRA (Low-Rank Adaptation)**. When fine-tuning a language model, overhauling all billions of parameters (adjustable numeric values) that act as the AI's brain cells is costly and places an overly heavy burden on the computer [[DoppelBot:Fine-tuneanLLMtoreplace your CEO | ModalDocs](https://modal.com/docs/examples/llm-finetuning)]. Instead, LoRA technology leaves the original brain cells untouched and creates only very small, lightweight 'adapters' that can be slipped in when needed [[DoppelBot:Fine-tuneanLLMtoreplace your CEO | ModalDocs](https://modal.com/docs/examples/llm-finetuning)].

Let's imagine this a bit more practically. Suppose you want to modify some content in a massive, tens of thousands of pages thick encyclopedia to fit your work. Resetting the type and reprinting the entire book from scratch would be horrendously inefficient. Instead, LoRA technology is like writing the notes you want on a thin 'Post-it' or transparent cellophane and lightly sticking it over the necessary page. By simply attaching or detaching these lightweight Post-its, you gain the incredible flexibility to revert to the original smart AI at any time, or instantly transform it into an employee with a 90s typewriter vibe.

## Where We Stand

So, where exactly does this movie-like technology stand in our reality right now? Let's take another look at the 1990s-vibe technical writing experiment mentioned earlier. To achieve their goal, the developer who conducted this ingenious experiment selected two open-source AI models as training targets: 'Llama 3.1 8B Instruct' and 'Qwen 2.5 7B Instruct' [[Fine-tuninganLLMtowritedocslikeit's1995| Hacker News](https://news.ycombinator.com/item?id=48408442)].

Here, it is worth noting the numbers '8B' and '7B' appended to the model names. This means the number of 'brain cells' (parameters) inside the AI is approximately 8 billion and 7 billion. You can think of it as an astronomical number of values—roughly equal to the global human population—intricately intertwining with one another to understand context and find the optimal words. 

Just a few years ago, running an AI with a brain cell count matching the global population required a massive data center with roaring cooling systems and house-sized server computers. However, the pace of technological advancement is blinding. Surprisingly, these heavy models reaching the 8-billion parameter (8B) level can now run quite comfortably and smoothly on the thin, light laptops we commonly use in cafes or libraries—namely, a 'MacBook Air' [[Fine-tuninganLLMtowritedocslikeit's1995| Hacker News](https://news.ycombinator.com/item?id=48408442)]. 

This is a monumental achievement that will be recorded in human computing history. Without paying expensive cloud usage fees or buying million-dollar equipment, anyone can download a free AI to their personal laptop and attach the magic Post-it (LoRA) described earlier. It means that the perfect factory for building your own genius AI assistant is already set up on your desk. Now, only one homework assignment remains: it all depends on how diligently humans can curate the nutritious and delicious 'data textbooks' (for example, a collection of 1990s manuals, your company's secret recipes, etc.) to feed the smart AI.

## What's Next

The future of the AI industry will explosively grow by diverging into two massive waves: 'General-purpose AI for everyone' that broadly benefits the world, and 'Custom AI just for me' that fits snugly into my room. Among these, fine-tuning is our most powerful weapon, granting us absolute control while perfectly maintaining consistency in the AI's output [[Fine Tune an open-source LLM - ashutosh.dev](https://www.ashutosh.dev/how-to-fine-tune-an-open-source-llm-step-by-step-2025-edition/)]. 

In the near future, we will be able to summon our own assistants on our smartphones and light laptops, even on an airplane where the internet cuts out or deep in the mountains. We will carry around several small, loyal AI assistants that speak in our own unique tone and perfectly comprehend the top-secret knowledge of our jobs. Just like this experiment that resurrected an old 1995 technical writer, a designer will create a design evaluation AI with the same fastidious aesthetic sense as theirs, and a novelist will personally 'educate' a co-writer AI inside their laptop to replicate their exact writing style. The era of this delightful magic is already quietly seeping into our daily lives.

## AI's Take

The ultimate destination that all great technologies eventually reach has always been 'personalization'. Just as house-sized computers that once filled an entire city have become the smartwatches on our wrists. The fact that an artificial intelligence with tens of billions of brains has fit inside a thin laptop, and that the powerful training whip called 'fine-tuning' has been placed in the hands of ordinary individuals, is truly marvelous.

Now, the true value of artificial intelligence no longer lies in the 'standardized correct answers' unilaterally handed down by tech giants. It depends on how exquisitely and affectionately you can tame the AI to match your life's purpose and tastes. What kind of expert do you want to nurture into your own reliable colleague on the laptop sitting on your desk right now?

## References
1. [Fine-tuninganLLMtowritedocslikeit's1995– Fabrizio Ferri...](https://passo.uno/fine-tuning-docs-llm/)
2. [Fine-tuninganLLMtowritedocslikeit's1995| Hacker News](https://news.ycombinator.com/item?id=48408442)
3. [DoppelBot:Fine-tuneanLLMtoreplace your CEO | ModalDocs](https://modal.com/docs/examples/llm-finetuning)
4. [LLMs:Fine-tuning, distillation, and prompt engineering](https://developers.google.com/machine-learning/crash-course/llm/tuning)
5. [Fine-tuning an LLM to write docs like it's 1995 - vuink.com](https://vuink.com/post/cnffb-d-dhab/fine-tuning-docs-llm)
6. [Fine Tune an open-source LLM - ashutosh.dev](https://www.ashutosh.dev/how-to-fine-tune-an-open-source-llm-step-by-step-2025-edition/)