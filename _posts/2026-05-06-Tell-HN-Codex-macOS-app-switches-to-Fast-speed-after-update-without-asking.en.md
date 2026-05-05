---
layout: post
title: "Spending More 'Paid Credits' Without Consent? The Bizarre Twist in the Codex for Mac Update"
description: "Following a recent update to the Codex app for macOS, users have reported that settings were automatically switched to 'Fast' mode, leading to higher costs and system overheating. We explore the details and necessary precautions."
summary: "The Codex app for macOS has been found to automatically switch user settings to 'Fast' mode after an update without consent. This mode consumes paid credits 1.5x faster and is causing severe spikes in CPU usage."
tags: [AI, Codex, OpenAI, macOS, GPT-5.5, TechTrends]
image: 2026-05-06-Tell-HN-Codex-macOS-app-swiches-to-Fast-speed-after-update-without-asking.jpg
image_alt: "An illustration of digital coins rapidly disappearing alongside a warning icon indicating system overload on a computer screen."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Changing settings directly linked to user costs without prior notice is a significant breach of trust. UI/UX design that respects user choice as much as technical performance is absolutely essential."
quiz:
  - question: "Which setting in the recently updated Codex app for macOS has caused controversy by changing automatically?"
    choices: ["Language settings", "Dark mode settings", "Speed settings"]
    answer: 2
    explanation: "Following the update, there have been continuous reports that speed settings were automatically changed from 'Standard' to 'Fast' without user consent."
  - question: "How much faster are digital credits (tokens) consumed when using 'Fast' mode compared to Standard mode?"
    choices: ["1.2x", "1.5x", "2.0x"]
    answer: 1
    explanation: "Fast mode is designed to consume approximately 1.5x more credits than Standard mode."
  - question: "Which of the following is NOT an effect of the updated Codex app on macOS systems?"
    choices: ["Sharp increase in CPU usage", "Loud computer fan noise", "Dramatic extension of battery life"]
    answer: 2
    explanation: "Some users are experiencing CPU usage soaring above 270%, fans running loudly, and the system slowing down."
lang: en
ref: 2026-05-06-Tell-HN-Codex-macOS-app-switches-to-Fast-speed-after-update-without-asking
audio: 2026-05-06-Tell-HN-Codex-macOS-app-switches-to-Fast-speed-after-update-without-asking.en.mp3
industry: creative
---

Imagine this. You visit your favorite regular cafe. You order your usual drink, but the barista, without asking, prepares it using 'premium beans' that are 1.5 times more expensive. Furthermore, while you drink it, the indoor temperature suddenly soars as if the air conditioning has failed, leaving you drenched in sweat. You would likely be more than just bewildered; you would be furious.

Exactly this kind of situation is currently unfolding among users of **Codex**, an artificial intelligence tool for macOS. Recent reports indicate that the latest update is simultaneously threatening users' wallets and their computers' health. Here is a breakdown of the bizarre twist hidden behind this cutting-edge AI technology.

## Why is this important?

The core issues of this incident are **'user choice'** and **'transparent cost management.'**

When we use AI like ChatGPT or Codex, it might seem like we are just asking questions, but internally, we are consuming digital currency called **'Tokens'** (the unit by which AI recognizes characters and calculates usage fees). This is very similar to using mobile data or putting coins into an arcade machine.

According to [Codex – Codex | OpenAI Developers](https://developers.openai.com/codex/speed), Codex features a 'Fast' mode that increases response speed. **To use an analogy**, it is like paying an extra toll to use an express lane on a highway. Activating this mode consumes tokens **1.5 times faster** than usual. [Tell HN: Codex macOS app switches to Fast speed after update without ...](https://news.ycombinator.com/item?id=47886763)

The problem is that after the recent update, many users found that the app had automatically activated this 'Fast' mode without their consent. [Tell HN: Codex macOS app switches to Fast speed after update without ...](https://news.bensbites.com/posts/65021-tell-hn-codex-macos-app-switches-to-fast-speed-after-update-without-asking) In other words, users' paid credits are evaporating at 1.5x speed without their knowledge. This goes beyond a simple feature change; it is a serious issue that directly affects user assets. [Signal Grid — AI News Intelligence](https://www.datafeed.news/events/tell-hn-codex-macos-app-switches-to-fast-speed-after-update-without-asking)

## Understanding the Two Faces of 'Fast' Mode

The new brain introduced in this update, the **GPT-5.5 model**, is undoubtedly smarter and more powerful than its predecessor. [Tell HN: Codex macOS app switches to Fast speed after update without ...](https://news.ycombinator.com/item?id=47886763) However, the 'Fast' mode used to run it is much like a car's 'Sport mode.' It provides speed but consumes more fuel (cost) and puts a strain on the engine (computer).

### 1. A Scary Speed That Lightens Your Wallet
'Fast' mode increases the speed at which the AI provides answers by about 1.5 times. [Speed – Codex | OpenAI Developers](https://developers.openai.com/codex/speed) However, as the saying goes, there is no such thing as a free lunch. As the speed increases, the cost consumed also increases by exactly 1.5 times. Many users are outraged that the app forced the high-cost mode on them, even though they preferred to use the "Standard" mode to save credits. [Tell HN: Codex macOS app switches to Fast speed after update without ...](https://news.ycombinator.com/item?id=47886763)

### 2. Overload That Heats Up Your Computer
Cost isn't the only problem. The physical impact on the computer is substantial. According to reports on [Codex desktop app pegs CPU on macOS after latest update; fans ... - GitHub](https://github.com/openai/codex/issues/18467), the updated app drives **CPU (Central Processing Unit)** usage up to **276.5%**, even when handling very small requests.

To put this in **simple terms**, it's like a person trying to cook with two hands when suddenly two more invisible hands appear and start chopping ingredients at a frantic pace. In this process, the fans that cool the computer start making noise like a jet taking off, and the entire computer begins to lag when you try to perform other tasks. [Codex desktop app pegs CPU on macOS after latest update; fans ... - GitHub](https://github.com/openai/codex/issues/18467)

## Current Situation: "They said it was fast, so why is it slower?"

Paradoxically, despite being set to 'Fast' mode, many users are complaining that actual perceived performance has worsened. [The new speed feature for Codex . What is your experience?](https://community.openai.com/t/the-new-speed-feature-for-codex-what-is-your-experience/1377408) One user expressed bewilderment, stating that performance felt **twice as slow** as before the update. [The new speed feature for Codex . What is your experience?](https://community.openai.com/t/the-new-speed-feature-for-codex-what-is-your-experience/1377408)

Adding to this, a series of software quality issues are emerging:
- **Mismatched Settings**: It was discovered that changing the speed in the configuration file (`config.toml`) reflects in the Command Line Interface (CLI) but fails to reflect in the actual macOS app GUI. [Codex App is misreporting the state of /fast mode · Issue #14689 · openai/codex](https://github.com/openai/codex/issues/14689)
- **App Instability**: In some projects, the app has become completely non-functional or "completely broken," disrupting workflows. [r/codex on Reddit: Upgraded to latest Macos app version of Codex app and completely broken](https://www.reddit.com/r/codex/comments/1rdypm0/upgraded_to_latest_macos_app_version_of_codex_app/)

## What Happens Next?

Currently, many users are viewing this update more as a 'disaster' than a technical advancement. If you are using Codex on a Mac, please check the following measures to protect your computer and your wallet.

### Practical Tips for Readers:
1. **Check Settings Immediately**: Check the app's settings menu to see if the speed is set to 'Fast.' You must change it back to 'Standard' to prevent unwanted costs. Note that a bug has been reported where the setting reverts after a restart, so frequent checks are necessary. [Codex App resets Speed from Fast to Standard after restart · Issue #20769 · openai/codex](https://github.com/openai/codex/issues/20769)
2. **Roll Back to a Previous Version**: If the current version is too unstable to use, it may be a wise choice to downgrade to a verified previous version (such as 26.217.1959). [r/codex on Reddit: Upgraded to latest Macos app version of Codex app and completely broken](https://www.reddit.com/r/codex/comments/1rdypm0/upgraded_to_latest_macos_app_version_of_codex_app/)
3. **Monitor System Resources**: Use the 'Activity Monitor' to ensure the Codex app isn't excessively consuming CPU. If your fan noise suddenly increases, it is best to restart the app.

While AI technology is making our lives more convenient, issues like unauthorized costs and system overloads may continue to occur. Just as we use smart AI, our eyes must remain sharp to ensure that the technology does not cross the line.

---

## AI's Perspective
**"Speed is not the only measure of innovation."**
From a developer's standpoint, setting 'Fast' mode as the default was likely intended to showcase the power of the new model. However, failing to respect a user's digital assets (tokens) and physical resources (computer performance) ultimately leads to a breakdown of trust. This incident clearly demonstrates that ethical UI/UX design, which protects user choice as much as technical excellence, must become the new standard in the AI era.

---

## References
1. [Tell HN: Codex macOS app switches to Fast speed after update without ...](https://news.ycombinator.com/item?id=47886763)
2. [Signal Grid — AI News Intelligence](https://www.datafeed.news/events/tell-hn-codex-macos-app-switches-to-fast-speed-after-update-without-asking)
3. [Tell HN: Codex macOS app switches to Fast speed after update without ...](https://news.bensbites.com/posts/65021-tell-hn-codex-macos-app-switches-to-fast-speed-after-update-without-asking)
4. [Tell HN: Codex macOS app switches to Fast speed after update without ...](https://alt-hn.vercel.app/item/47886763)
5. [The new speed feature for Codex . What is your experience?](https://community.openai.com/t/the-new-speed-feature-for-codex-what-is-your-experience/1377408)
6. [Codex desktop app pegs CPU on macOS after latest update; fans ... - GitHub](https://github.com/openai/codex/issues/18467)
7. [Speed – Codex | OpenAI Developers](https://developers.openai.com/codex/speed)
8. [Codex App resets Speed from Fast to Standard after restart · Issue #20769 · openai/codex](https://github.com/openai/codex/issues/20769)
9. [r/codex on Reddit: Upgraded to latest Macos app version of Codex app and completely broken](https://www.reddit.com/r/codex/comments/1rdypm0/upgraded_to_latest_macos_app_version_of_codex_app/)
10. [Codex App is misreporting the state of /fast mode · Issue #14689 · openai/codex](https://github.com/openai/codex/issues/14689)

## FACT-CHECK SUMMARY
- Claims checked: 12
- Claims verified: 10
- Verdict: PASS