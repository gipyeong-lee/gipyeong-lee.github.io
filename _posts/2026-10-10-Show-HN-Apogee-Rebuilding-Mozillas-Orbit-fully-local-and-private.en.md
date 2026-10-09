---
layout: post
title: "The AI summary tool Mozilla gave up on, revived by an indie developer as 'fully local'"
description: "After Mozilla's AI summary service 'Orbit' disappeared, a privacy-focused alternative, 'Apogee', has emerged that processes all data on your own computer."
summary: "Following the discontinuation of Mozilla's Orbit service, an open-source project called 'Apogee' has been released that performs AI summarization directly on the user's computer without sending data externally."
tags: [AI, Privacy, Browser Extension, Mozilla, Apogee]
image: 2026-10-10-Show-HN-Apogee-Rebuilding-Mozillas-Orbit-fully-local-and-private.jpg
image_alt: "Concept image of a browser extension using local AI to summarize documents on a personal computer"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "For users torn between AI convenience and data privacy, 'local processing' will be the most powerful solution."
quiz:
  - question: "What was one of the primary reasons Mozilla quietly discontinued its 'Orbit' service?"
    choices: ["Lack of users", "Concerns regarding data collection", "Technical limitations"]
    answer: 1
    explanation: "Mozilla's Orbit was quietly discontinued six months after launch due to concerns raised regarding data collection."
  - question: "What is the key differentiator of Apogee compared to the original Orbit?"
    choices: ["More language support", "Use of cloud servers", "Local processing that does not send data externally"]
    answer: 2
    explanation: "Apogee is a privacy-focused tool that processes data directly within the user's device, ensuring it is not sent externally."
  - question: "Which file formats can Apogee process?"
    choices: ["Various formats including web pages, PDFs, and videos", "Only text files", "Only PDF files"]
    answer: 0
    explanation: "Apogee supports various input methods including web pages, videos, PDFs, DOCX files, and copied text."
lang: en
ref: 2026-10-10-Show-HN-Apogee-Rebuilding-Mozillas-Orbit-fully-local-and-private
audio: 2026-10-10-Show-HN-Apogee-Rebuilding-Mozillas-Orbit-fully-local-and-private.en.mp3
industry: creative
---

Imagine this: You are reading a long article on the internet or viewing a complex discussion thread, and as soon as you tell the AI, "Summarize this for me," it neatly organizes the key points. What if, in this process, the sensitive documents or private conversations you are reading were never transmitted to a company's server?

A project called 'Apogee', recently introduced on the online community 'Hacker News', is turning this dream into reality. It takes the idea of 'Orbit', the AI summary tool once ambitiously introduced by Mozilla, and maximizes the core value of user privacy.

## Why is it gaining attention?

We live in a flood of information every day. While AI summary services help us digest this information quickly, the fact that we have to send 'our information' to external servers in exchange has always been a point of discomfort.

Mozilla's Orbit service also garnered high expectations by introducing AI features to the browser, but it quietly disappeared six months after launch as user concerns regarding data collection grew [[Source: Mozilla Killed Its AI Summary Extension — A Developer Rebuilt ...](https://www.opcnew.com/en/mozilla-orbit-local-ai-apogee-zh)]. Apogee demonstrates that we can enjoy sufficiently intelligent summarization features using only the performance of our personal computers, without entrusting our data to cloud AI services [[Source: Apogee brings private AI summaries into the browser](https://www.neotechnews.com/article/apogee-mozilla-killed-orbit-i-rebuilt-it-locally-and-privately-50017301)]. This is an important turning point showing that we no longer need to sacrifice our privacy for the convenience of information.

## Easy to Understand: Inviting 'Your Own Smart Assistant' Home

Let’s use an analogy: If existing cloud AI services are like ordering food from an 'outside restaurant,' Apogee is like cooking directly in 'our home kitchen.'

- **Outside Restaurant (Cloud AI)**: When you place an order, the restaurant owner checks everything in your fridge (what you are viewing) and delivers it after cooking. It is convenient, but your dietary habits are recorded externally.
- **Our Home Kitchen (Apogee Local AI)**: You cook directly at home using the ingredients in your own fridge. Since there is no delivery process, your recipes or ingredients are not exposed externally.

Apogee completes all processing within the user's device in this way [[Source: Apogee: Mozilla Killed Orbit. I Rebuilt It Locally and ...](https://bhn.vercel.app/post/50017301)]. The core technology is 'Local Inference' (technology that performs AI calculations directly on your device without passing through cloud servers). If a user builds and connects 'Ollama' (a tool that runs AI models in a local environment) on their computer, they can even achieve more powerful performance [[Source: Apogee: Mozilla Killed Orbit. I Rebuilt It Locally and ...](https://bhn.vercel.app/post/50017301)].

## Current Status: What can it do?

Apogee operates as a browser extension and provides various features that go beyond simply summarizing a few words [[Source: Apogee brings private AI summaries into the browser](https://www.neotechnews.com/article/apogee-mozilla-killed-orbit-i-rebuilt-it-locally-and-privately-50017301)].

1. **Supports Various Inputs**: It can process not only web pages but also videos, PDF and DOCX files, and even copied and pasted text [[Source: Apogee brings private AI summaries into the browser](https://www.neotechnews.com/article/apogee-mozilla-killed-orbit-i-rebuilt-it-locally-and-privately-50017301)].
2. **Organizes Complex Discussions**: It pulls posts from discussion sites like Reddit, Hacker News, Bluesky, and Mastodon, and organizes them in a clean Markdown format while maintaining the order of authors, scores, and replies [[Source: GitHub - darshi1337/apogee: Private AI summarizer for ...](https://github.com/darshi1337/Apogee)].
3. **Complete Privacy**: There is no need to create a separate account, enter an API key, or worry about sending data to cloud servers [[Source: Apogee brings private AI summaries into the browser](https://www.neotechnews.com/article/apogee-mozilla-killed-orbit-i-rebuilt-it-locally-and-privately-50017301)].

## Where is it heading?

'Local-first AI tools' like Apogee will become increasingly common. This is because they have the powerful advantage of not incurring cloud usage costs, and above all, your data is not recorded somewhere on a server.

Moving forward, beyond browser extensions, a 'local assistant' with built-in privacy protection features will accompany every task we do on our computers. AI technology is now evolving beyond 'how excellent it is' toward 'how useful it can be while protecting my information.'

---

### MindTickleBytes' AI Reporter Perspective
The potential of local AI demonstrated by Apogee, created by an individual developer, realizes the 'independence of the internet' that Mozilla pursued [[Source: Investing in what moves the internet forward](https://blog.mozilla.org/en/mozilla/building-whats-next/)] even more perfectly. The era of paying for convenience with privacy is now slowly coming to an end with local AI.

## References

1. [Mozilla Killed Its AI Summary Extension — A Developer Rebuilt ...](https://www.opcnew.com/en/mozilla-orbit-local-ai-apogee-zh)
2. [Apogee: Mozilla Killed Orbit. I Rebuilt It Locally and ...](https://bhn.vercel.app/post/50017301)
3. [Apogee brings private AI summaries into the browser](https://www.neotechnews.com/article/apogee-mozilla-killed-orbit-i-rebuilt-it-locally-and-privately-50017301)
4. [GitHub - darshi1337/apogee: Private AI summarizer for ...](https://github.com/darshi1337/Apogee)
5. [Investing in what moves the internet forward](https://blog.mozilla.org/en/mozilla/building-whats-next/)