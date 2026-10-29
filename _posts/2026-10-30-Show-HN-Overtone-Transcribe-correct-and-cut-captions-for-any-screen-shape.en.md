---
layout: post
title: "AI Automatically Cuts Video Captions to Fit 'Screen Shape'?"
description: "Learn about Overtone, a technology that automatically optimizes captions to fit the aspect ratio of your video, eliminating the need to manually adjust subtitles for landscape and portrait formats when creating short-form content."
summary: "Introducing Overtone, an AI tool that automatically adjusts caption placement to fit different aspect ratios across various video platforms, and exploring its operating principles and benefits."
tags: [AI, Video Editing, Captions, Short-form, Tech]
image: 2026-10-30-Show-HN-Overtone-Transcribe-correct-and-cut-captions-for-any-screen-shape.jpg
image_alt: "Example of a video screen with captions properly placed on smartphones and monitors of various aspect ratios"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "This is a useful tool that will significantly reduce the workload for video creators. It is an essential technology in an era where content optimization is a must."
quiz:
  - question: "What data does Overtone store alongside the captions it generates?"
    choices: ["Video quality and color information", "Word timestamps and speaker information", "Background music beats"]
    answer: 1
    explanation: "Overtone stores the time each word was spoken and speaker information together to enable precise caption editing."
  - question: "What are the aspect ratios that Overtone supports by default?"
    choices: ["1:1 and 4:3", "16:9 and 9:16", "21:9 and 1:1"]
    answer: 1
    explanation: "Overtone automatically separates and cuts captions to fit the 16:9 landscape video and 9:16 portrait short-form video aspect ratios."
  - question: "What is used to display captions created with Overtone in a web player?"
    choices: ["video.js plugin", "Google Translate", "AI speech synthesizer"]
    answer: 0
    explanation: "Overtone uses a video.js plugin to display caption cuts that perfectly fit the player's screen shape."
lang: en
ref: 2026-10-30-Show-HN-Overtone-Transcribe-correct-and-cut-captions-for-any-screen-shape
audio: 2026-10-30-Show-HN-Overtone-Transcribe-correct-and-cut-captions-for-any-screen-shape.en.mp3
industry: creative
---

Imagine this: You want to port a YouTube video you carefully crafted to short-form platforms like Instagram Reels or TikTok. However, the captions you meticulously placed for a landscape (16:9) video are cut off in the wrong places or move off-screen in a portrait (9:16) view. Any video creator has probably struggled for hours manually adjusting caption positions at least once.

Now, a new AI tool called 'Overtone' has arrived to reduce such tedious tasks. It's a smart captioning tool that considers not just the content of the video, but also its 'screen shape.' What kind of technology is it?

## Why is this important?

The content market is currently in the era of 'multi-format.' You can secure more viewers by optimizing the same video for YouTube, TikTok, and Instagram, respectively. However, manually repositioning the 'captions'—the core of the video—for each platform is a very laborious task.

Overtone saves creators time right at this point. It is designed to automatically optimize captions to fit the video's aspect ratio, going beyond simple speech-to-text transcription. [Source 1](https://github.com/lonthq/overtone-captions) This means that creators can drastically reduce the physical time spent on caption editing and focus more on creative planning.

## Easy to understand: A tailor fitting a 'universal suit'

Simply put, Overtone is like a 'digital tailor.' Just as we alter clothes to fit our body shape when dressing, it automatically 'tailors' captions to fit the 'body shape' (aspect ratio) of the video.

The operating principle is as follows: First, Overtone stores the time each word was spoken and information about the speaker in a database based on the input audio. [Source 1](https://github.com/lonthq/overtone-captions) Based on this well-organized data, the AI cuts the captions separately to fit various ratios, such as landscape (16:9) and portrait (9:16). [Source 1](https://github.com/lonthq/overtone-captions)

To use an analogy: in a 16:9 screen, captions look comfortable even if spread out long in one line as if they are in a spacious room, but in a narrow and long vertical screen of 9:16, it would be easier to read if the captions were split into two lines, right? Overtone automatically performs these calculations and then displays caption cuts that perfectly fit the ratio of the video the viewer is watching via a web video player plugin called 'video.js.' [Source 1](https://github.com/lonthq/overtone-captions) Just like how a video screen rotates automatically when you turn your smartphone, the captions wear 'custom-fitted clothes' according to the platform environment.

## Current status: How can it be used?

Currently, Overtone provides features to extract and process caption data from existing caption files, audio, or video sources via a command-line interface (CLI). [Source 1](https://github.com/lonthq/overtone-captions)

However, compared to other existing AI-based caption services, it is a tool that requires a slightly more technical approach. For instance, while typical services that recognize speech in real-time in a web browser and display captions focus on user convenience, Overtone provides features highly specialized for the specific purpose of 'caption optimization according to screen shape.'

## What will happen in the future?

As short-form content has become the mainstream, it is expected that more tools supporting such 'multi-ratios' automatically will emerge. It is highly likely that technology will evolve to the point where the AI identifies the position of the subject (the main character in the screen) within the video and 'intelligently avoids and places' captions so they don't cover the subject, instead of the user manually moving caption positions. Overtone is changing the paradigm of caption production from 'fixed text' to 'fluid data' at that starting point.

## MindTickleBytes' AI Reporter View

Caption placement has been one of the most tedious tasks in video production. Overtone is a case that clearly shows how technology lowers the threshold of content production, beyond simple convenience features. Instead of worrying about 'where to put captions,' the era where we focus more on 'what to say' will come.

## References

1. Show HN: Overtone – Transcribe, correct and cut captions for any screen shape (https://github.com/lonthq/overtone-captions)