---
layout: post
title: "If your AI keeps 'trying too hard' with flowery language, one sentence is all you need"
description: "We introduce a method to get concise answers from AI by removing the 'AI voice' characterized by unnecessary metaphors and flowery modifiers."
summary: "Anthropic has officially released a magic command in their guide for the Claude Fable 5.1 model: 'Please remove all mannered prose' to strip away unnecessary modifiers and metaphors."
tags: [AI, Anthropic, Claude, Prompt Engineering, Tips]
image: 2026-09-09-Please-Remove-All-Mannered-Prose-and-Other-LLM-Incantations.jpg
image_alt: "A graphic symbolizing complex, flowery sentences written by AI being erased and replaced with concise, clear ones."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 'showboating' creates unnecessary cognitive load for the user. Removing modifiers that obscure the essence is fundamental to AI utilization."
quiz:
  - question: "What is 'mannered prose' as defined by Anthropic?"
    choices: ["Technical errors used by AI", "Writing that contains more metaphors and flowery rhetorical expressions than necessary", "A phenomenon where AI refuses to answer"]
    answer: 1
    explanation: "Mannered prose refers to the phenomenon where AI decorates its answers with unnecessary metaphors or flowery styles when it could simply state the facts."
  - question: "Where should the provided command, 'Please remove all mannered prose', be placed for effectiveness?"
    choices: ["At the end of individual queries or added to the system prompt", "Input into the computer's settings menu", "Must be input inside a code block"]
    answer: 0
    explanation: "The command can be used by including it in individual requests or adding it to the system prompt that defines the AI's role."
  - question: "Do you absolutely have to keep the spaces for the AI to understand this command correctly?"
    choices: ["Yes, spaces are mandatory", "No, it works even if you remove all spaces", "It must be typed in all caps"]
    answer: 1
    explanation: "Surprisingly, this command works effectively even when all spaces are removed (Pleaseremoveallmanneredprose)."
lang: en
ref: 2026-09-09-Please-Remove-All-Mannered-Prose-and-Other-LLM-Incantations
audio: 2026-09-09-Please-Remove-All-Mannered-Prose-and-Other-LLM-Incantations.en.mp3
industry: general
---

Imagine this: On a busy morning, you ask your AI assistant, "Summarize the three key agenda items for today's meeting." The AI replies, "Today's meeting is like the calm before a great storm. The compass of three key agenda items will guide our direction..." It proceeds to pile on all sorts of metaphors and modifiers. For a user who just wants the bottom line, it’s frustrating.

Recently, AI models have been causing fatigue among users precisely because of this "AI-esque voice." In the guide for their latest model, 'Claude Fable 5.1,' Anthropic has officially proposed a surprisingly simple solution to solve this problem.

## Why does this matter?

The biggest reason we use AI is for 'efficiency.' However, when AI tries to sound human by mixing in excessive metaphors or unnecessarily complicating sentences, it becomes difficult to find the information that actually matters. According to [Source 13](https://vibecoding.ru/news/2026/09/03/anthropic-mannered-prose-prompt), this flowery style used by AI pulls in meanings not chosen by the author, forcing the reader to perform unnecessary interpretive labor. This official guide is significant in that it restores to the user the authority to use AI more intelligently and concisely.

## Making it easy to understand

Anthropic has termed this phenomenon 'Mannered Prose.' [Source 4](https://x.com/MaxForAI/status/2095131767229517917) Simply put, it refers to the AI's writing habit of "trying too hard" by employing metaphors or flowery language to draw out a point that could be summed up neatly in one sentence.

Anthropic’s development team acknowledged that while Claude Fable 5.1 is an improvement over previous models, sentences can still be too long and complex at times. [Source 4](https://x.com/MaxForAI/status/2095131767229517917) Therefore, they added a magic command to their official documentation to strip away this 'AI voice.'

That command is simply **"Please remove all mannered prose."** [Source 1](https://matthewritch.com/blog/2026/09/08/Mannered-Prose-Style-Prompts/)

Think of it this way: The AI has finished its 'basic etiquette training,' but it has just come from a 'literature class' and wants to sprinkle poetic expressions into every answer. This command is a powerful switch that tells the AI, "Stop being an artist, and focus on your day job as an assistant!"

## Current status

Currently, this prompt is being evaluated as highly effective. [Source 5](https://paddo.dev/blog/a-dial-worth-turning/) Users have confirmed that simply attaching this command to the end of a question or placing it in the 'system prompt' where instructions are given to the AI in advance makes the AI's tone noticeably more concise. [Source 6](https://x.com/Voxyz_ai/status/2095260094795583807), [Source 11](https://t.me/dailyprompts/9362)

What’s even more surprising is that because the AI understands the meaning of this sentence so well, even if you ignore the spaces and type 'Pleaseremoveallmanneredprose,' it intelligently understands and strips away the flowery modifiers. [Source 9](https://apidog.com/blog/prompting-claude-fable-5-1/), [Source 13](https://vibecoding.ru/news/2026/09/03/anthropic-mannered-prose-prompt)

## What happens next?

In the future, AI services will likely be improved so that users don't have to manually input these 'tone-fixing' commands. This update to Anthropic's guide is a signal that AI companies are listening to user feedback and are considering not just the intelligence of the AI, but also the 'efficiency of communication.'

No longer will you need to awkwardly explain to the AI, "Don't sound pretty, just give me the core facts." With that one sentence, your AI assistant will transform into a much more capable business partner.

## MindTickleBytes' AI Reporter Perspective

While AI becoming capable of speaking like a human is a technical achievement, the most valuable ability in a business environment remains 'clear information delivery.' Anthropic's decision to directly release a prompt that solves this issue shows that the AI's ability to exercise self-restraint is becoming a measure of the true maturity of AI technology.

## References

1. [Matthew Ritch, "Please Remove All Mannered Prose" and Other LLM Incantations](https://matthewritch.com/blog/2026/09/08/Mannered-Prose-Style-Prompts/)
2. [Ian Nuttall, "A prompt to stop Claude from speaking in parseltongue"](https://x.com/iannuttall/status/2095203215734178066)
3. [Max For AI, "有意思，Anthropic亲自下场教你怎么去掉Claude味了"](https://x.com/MaxForAI/status/2095131767229517917)
4. [Paddo, "A Dial Worth Turning: Claude Opus 5's Prose, and the Style Guide Anthropic Wrote Against Its Own Model"](https://paddo.dev/blog/a-dial-worth-turning/)
5. [Vox, "You removed the “It’s not X, it’s Y” lines. 𝗜𝘁 𝘀𝘁𝗶𝗹𝗹 𝗿𝗲𝗮𝗱𝘀 𝗹𝗶𝗸𝗲 𝗔𝗜."](https://x.com/Voxyz_ai/status/2095260094795583807)
6. [HN blogs - 8/9/26](https://hnblogs.substack.com/p/hn-blogs-8926)
7. [APIDog, "Prompting Claude Fable 5.1: Every Behavior Shift and the Line That..."](https://apidog.com/blog/prompting-claude-fable-5-1/)
8. [Telegram, "@dailyprompts"](https://t.me/dailyprompts/9362)
9. [Dzen, "Гайд по созданию промптов в Fable 5.1"](https://dzen.ru/a/apkFgUgF0B8ig_B6)
10. [Vibecoding, "Вычурность из текстов Claude убирает одна строка"](https://vibecoding.ru/news/2026/09/03/anthropic-mannered-prose-prompt)
11. [VC.ru, "Вышел Claude Fable 5.1 - я уже потестила"](https://vc.ru/chatgpt/3117274-obzor-fable-5-1-ot-anthropic-i-ozhidaniya-ot-astra-ot-openai)