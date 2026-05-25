---
layout: post
title: "Business Texts in 'Blue Bubbles'? Twilio for iMessage 'Chert' Emerges"
description: "Learn about the technology and impact of Chert (YC P26), a startup that enables businesses to use Apple iMessage's blue bubbles and read receipts."
summary: "Chert has emerged as a startup providing an API that allows businesses and AI agents to access Apple's closed iMessage environment."
tags: [Chert, iMessage, API, AI Agents, YC, Startup, Twilio]
image: 2026-05-26-Launch-HN-Chert-YC-P26-Twilio-for-iMessage.jpg
image_alt: "An image depicting a conversation between a business and a customer in blue bubbles on an iPhone screen."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "This is an interesting inflection point where business messaging evolves from annoying 'spam' into natural 'conversation.' It will be worth watching how this attempt to technically bypass Apple's solid ecosystem barriers settles in the long term."
quiz:
  - question: "What is the most distinguishing feature of Chert compared to existing SMS messaging services?"
    choices: ["Message sending costs are 100% free", "It supports Apple iMessage's blue bubbles and typing indicator features", "It is a messaging feature exclusively for Android"]
    answer: 1
    explanation: "Chert supports native features such as blue bubbles, read receipts, and typing indicators so that businesses can communicate with customers through iMessage."
  - question: "How does Chert operate when a customer is not in an environment using an iPhone (iMessage)?"
    choices: ["It cancels the message transmission itself", "It switches to standard SMS for normal delivery", "It sends an email instead of the message content"]
    answer: 1
    explanation: "If the recipient is not an iMessage user, Chert automatically falls back to standard SMS to ensure the message is delivered without interruption."
  - question: "What kind of automation system can businesses build through Chert's API?"
    choices: ["It can automatically connect received customer messages to AI agents or human representatives", "It can remotely control the power of the customer's smartphone", "It tracks the customer's location in real-time to send advertisements"]
    answer: 0
    explanation: "Chert provides powerful routing capabilities that integrate received messages with a company's existing systems to automatically connect them to AI agents or actual representatives."
lang: en
ref: 2026-05-26-Launch-HN-Chert-YC-P26-Twilio-for-iMessage
audio: 2026-05-26-Launch-HN-Chert-YC-P26-Twilio-for-iMessage.en.mp3
industry: finance
---

Imagine this: You receive a reservation confirmation text from a hair salon or dentist you frequent. But it's not the usual stiff green bubble (a standard SMS). It arrives as a vivid 'blue bubble,' just like when you're chatting with a close friend. At the bottom of the screen, the three-dot (...) typing indicator flickers, signaling that the other party is writing a reply. You can even long-press the message sent by the business to send 'Tapback' reactions like a heart or a thumbs-up.

Most of our daily interactions with businesses are one-sided and mechanical. Texts from companies are often just one-way 'notifications' or spammy 'advertisements,' hardly feeling like a true 'conversation.' In particular, it has been nearly impossible for general businesses to provide this kind of natural iMessage conversation experience to a large number of customers. This is because Apple has not opened an official channel—an API (Application Programming Interface, a pathway for computer programs to exchange data)—for general companies to send marketing messages or notifications via iMessage [[1]](https://ttj.kr/tech-news/imessage용-twilio가-등장했다-chert가-푸는-애플의-폐쇄-생태계).

However, an interesting startup has recently emerged in Silicon Valley, prying open this tightly closed door. That startup is **Chert (YC P26)**, backed by Y Combinator, the world's premier startup accelerator and investment firm [[2]](https://www.linkedin.com/posts/y-combinator_chert-yc-p26-is-building-the-infrastructure-activity-7458289615548895232-3Dw2). They are generating significant buzz in the tech industry by building the infrastructure that acts as a bridge for businesses to exchange and automate conversations via iMessage using an API.

So, why the obsession with iMessage's 'blue bubbles' among so many messaging apps? To understand that, we first need to understand the emotional difference we feel when we receive a text.

## Why Does This Matter? The Color of Trust: Blue Bubbles

Before diving deep into technical details, it's worth noting what this small change in color means in our daily lives. In modern society, a smartphone's default inbox is often treated as little more than a 'spam folder.' From weekend sale alerts from shopping malls to credit card payment notifications and loan advertisements from unknown sources, countless green bubbles (SMS) pour in every day. We subconsciously dismiss green texts as 'annoying flyers distributed in bulk by machines' and ignore them easily.

On the other hand, iMessage's blue bubbles evoke a completely different set of emotions. A blue bubble represents an intimate, private space for sharing the minutiae of daily life with family, partners, and friends. Thanks to 'read receipts' that tell you if the other person has seen your message and 'typing indicators' that show they are currently writing, it provides a much higher level of trust and intimacy.

Simply put, if a green text is an 'advertisement flyer' shoved through a door crack, a blue text feels like an 'invitation' handed directly to you by a close acquaintance.

Chert has sharply targeted this emotional difference—the 'trust gap' felt by consumers. To avoid looking like one-way spam from a machine and instead provide the warm feeling of a 1:1 conversation with a real person, they have preserved iMessage's unique features. Using Chert's technology, business messages also support the 'blue bubble user experience (UX),' 'read receipts,' 'Tapbacks (reactions like hearts),' and 'typing indicators' [[3]](https://poweredbyai.app/project/chert) [[4]](https://news.ycombinator.com/item?id=48267829). This is why many companies are paying close attention to the potential of this technology to move beyond being treated as spam and have 'real conversations' with customers.

So, how exactly did Chert implement these features that Apple hasn't even officially allowed? Let's look at the complex world of technology using an analogy of a post office.

## Easy Understanding: A 'Special Post Office' That Only Enters Apple Village

Developers and businesses usually use a very famous SMS delivery system called 'Twilio' to send large volumes of automated texts, such as order confirmations or shipping notices. If Twilio is a massive 'public post office' that delivers general letters and flyers anywhere in the world, Chert has essentially built a 'special post office' that can sneak into the sturdy walls built by Apple—specifically, the iMessage village.

Even a giant like Twilio was blocked by Apple's uniquely closed ecosystem barriers and couldn't properly touch the blue bubble territory [[1]](https://ttj.kr/tech-news/imessage용-twilio가-등장했다-chert가-푸는-애플의-폐쇄-생태계). That's why the Silicon Valley industry and developers intuitively call Chert **"Twilio for iMessage"** [[1]](https://ttj.kr/tech-news/imessage용-twilio가-등장했다-chert가-푸는-애플의-폐쇄-생태계) [[5]](https://news.mcan.sh/item/48267829).

Here's an analogy for how it works: A business enters a message on their customer management program. Then, Chert's infrastructure (invisible connection paths called REST APIs and webhooks that allow computers to talk to each other) receives this message. It then wraps it up perfectly as if it were an iMessage sent by a real person using an iPhone and beams it to the customer's iPhone [[6]](https://www.everydev.ai/tools/chert).

One obvious question might arise here: "What happens if a customer doesn't use an iPhone and uses an Android smartphone like a Galaxy? Do they not receive the blue bubble, and does the message disappear?"

Fortunately, Chert has solved this smoothly. If the system detects in real-time that the recipient cannot receive an iMessage, it automatically reroutes it to a standard green SMS (Fallback). In other words, they have built a safety net to ensure that important business messages arrive regardless of the customer's smartphone model [[3]](https://poweredbyai.app/project/chert).

Moreover, this special post office also acts as a smart 'telephone operator.' When a customer replies via iMessage, it analyzes the content or context of the reply to determine if a human needs to respond. Thus, it can cleverly decide the route (routing)—whether to connect to a real human representative's monitor or to the company's AI agent (AI assistant) to continue the conversation automatically [[5]](https://news.mcan.sh/item/48267829) [[6]](https://www.everydev.ai/tools/chert).

Thanks to such an original yet practical idea, this fledgling startup is already making a clear mark on key players in Silicon Valley.

## Current Status: Intense Silicon Valley Interest and Successful Experiments

While Chert is in the early stages of making its name known, it has already secured solid support within the Silicon Valley ecosystem. In addition to the aforementioned Y Combinator (YC P26 batch), it has successfully attracted consecutive investments from prominent investment firms like Z Fellows and Betafund. This is strong evidence of the industry's recognition of their potential in the business-to-business (B2B) communications infrastructure market [[6]](https://www.everydev.ai/tools/chert).

In fact, before fully commercializing this large and complex enterprise infrastructure, Chert's founders conducted a very interesting experiment. They released a pilot tool on the internet that allowed people to directly create simple AI agents that operate as one-offs within iMessage. The results were surprising. Despite having zero expensive marketing, 2,000 users flocked to it voluntarily in just one week [[4]](https://news.ycombinator.com/item?id=48267829). It's like opening a tiny pop-up store in a neighborhood and having a massive line form instantly just through word-of-mouth.

This simple experiment suggests something very important: people feel it is much more 'human' to converse with an AI in a blue iMessage environment—alive with typing indicators and emotional expressions (reactions)—than in unfamiliar, stiff website chatbot windows or fatiguing standard SMS environments. As a result, people open their hearts more and communicate more actively.

Based on these overwhelming strengths, a large number of B2C (business-to-consumer) startups and customer experience (CX) management teams are already moving quickly to adopt Chert's solution to communicate with their customers [[7]](https://www.youtube.com/watch?v=g0BYKdbaNFo).

So, as the way businesses and customers communicate fundamentally changes, how will our daily lives change in the future?

## What's Next? The Future of Conversational Infrastructure

Until now, using the latest AI technology or a company's smart chatbot service required cumbersome procedures. You had to download a heavy dedicated app made by the company or log in to a complex website after searching for your ID and password. However, as the 'conversational infrastructure' Chert is building becomes popularized, our daily scenery will become much simpler and more elegant. This is because the familiar messaging apps we habitually turn to every day to chat with friends will directly become the stage for cutting-edge AI services.

For example, when you want to change the time of a reservation at a popular restaurant for this weekend, get a refund for a suddenly canceled flight, or inquire about how to use a product you just received, there will be no need to navigate menus on a complex company website.

You can just open iMessage to the business's number saved in your contacts and say, "Can you push my reservation for tomorrow evening to 7 PM?"—just like sending a text to a friend. Then, an AI agent connected to the business system will immediately understand the context of your message and send a natural reply with the three-dot (...) typing indicator: "Sure, I've changed it to 7 PM! Shall I prepare a window seat for you?" We are entering an era where invisible, complex technology quietly seeps into our daily chat windows, making life more convenient and seamless.

---

**Perspective from MindTickleBytes' AI Reporter**

We live in an era where capturing a customer's 'attention' is a company's greatest competitiveness and asset. In this context, the ability for businesses to directly and naturally enter the 'personal messenger'—the intimate space that consumers trust and open most frequently—is clearly a major innovation in the history of telecommunications. It is also a golden opportunity for the inbox, once filled with green spam notifications we hated to look at, to be transformed into a useful assistant space where real conversations that actually solve life's problems take place.

However, a massive mountain stands before this innovative step: Apple. Traditionally, Apple has made the closed nature of its ecosystem and strict security rules its strongest weapon and identity. The key will be how long Chert's attempt to technically bypass this solid barrier as a third party without official permission can be maintained under Apple's tacit consent or allowance. This is because there is always the risk that Apple could block this pathway through a security update.

Therefore, whether Chert can move beyond a short-term workaround and grow into a stable infrastructure standard while surviving Apple's stringent platform policy changes will be one of the most interesting and tension-filled points to watch in the IT industry. It will be exciting to see how this challenge toward 'real conversation' between businesses and customers ends, and what the future holds for the blue bubble.

---

## References
1. [Twilio for iMessage Emerges - Chert Solves Apple's Closed Ecosystem](https://ttj.kr/tech-news/imessage용-twilio가-등장했다-chert가-푸는-애플의-폐쇄-생태계)
2. [Chert Launches iMessage API for Business Automation | Y ...](https://www.linkedin.com/posts/y-combinator_chert-yc-p26-is-building-the-infrastructure-activity-7458289615548895232-3Dw2)
3. [Chert- Business & Marketing | PoweredbyAI](https://poweredbyai.app/project/chert)
4. [Launch HN: Chert (YC P26) – Twilio for iMessage | Hacker News](https://news.ycombinator.com/item?id=48267829)
5. [Launch HN: Chert (YC P26) – Twilio for iMessage | Remix ...](https://news.mcan.sh/item/48267829)
6. [Chert - iMessage API for Developers | EveryDev.ai](https://www.everydev.ai/tools/chert)
7. [Chert (YC P26): iMessage infrastructure for trusted communication at scale - YouTube](https://www.youtube.com/watch?v=g0BYKdbaNFo)