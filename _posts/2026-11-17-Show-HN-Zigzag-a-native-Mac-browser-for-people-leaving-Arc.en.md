---
layout: post
title: "Is the Arc Browser Disappearing? 'Zigzag', the Miraculous Mac Browser Built by a Shanghai High School Student in Just 3 Weeks"
description: "Everything about Zigzag, an ultra-lightweight Mac browser developed by a Shanghai high school student using Swift and WebKit in just 3 weeks as an alternative to the Arc browser, which is ending in December 2026."
summary: "The features and behind-the-scenes development of 'Zigzag', an 18MB ultra-lightweight Mac browser developed in just 3 weeks by a Shanghai high school student shocked by the news of Arc browser's shutdown."
tags: [Zigzag, Arc, MacBrowser, WebKit, OpenSource]
image: 2026-11-17-Show-HN-Zigzag-a-native-Mac-browser-for-people-leaving-Arc.jpg
image_alt: "Interface screen of the Zigzag browser featuring a clean sidebar and split-view functionality on a Mac screen"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "The tenacity of a high school developer who didn't get discouraged by a major corporation's service shutdown decision and found a solution through direct coding stands out. It's a lightweight alternative that brings a refreshing shock to the bloated modern browser ecosystem."
quiz:
  - question: "What is the background of the developer who created the Zigzag browser?"
    choices: ["Veteran browser engineer in Silicon Valley", "High school student from Shanghai", "Open source researcher in Europe"]
    answer: 1
    explanation: "Zigzag is a browser directly developed in just 3 weeks by ZigaoWang, a high school student from Shanghai, who was shocked by the news of the Arc browser's shutdown [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)."
  - question: "Which Apple engine is the Zigzag browser based on?"
    choices: ["Chromium engine", "WebKit engine", "Gecko engine"]
    answer: 1
    explanation: "Zigzag is built with Apple's pure WebKit engine and the Swift language, rather than Chromium or Electron [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)."
  - question: "What is approximately the installation size of the Zigzag browser?"
    choices: ["About 18 MB", "About 871 MB", "About 1.5 GB"]
    answer: 0
    explanation: "Zigzag sheds unnecessary bloat and boasts an ultra-lightweight installation size of about 18 MB [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)."
lang: en
ref: 2026-11-17-Show-HN-Zigzag-a-native-Mac-browser-for-people-leaving-Arc
audio: 2026-11-17-Show-HN-Zigzag-a-native-Mac-browser-for-people-leaving-Arc.en.mp3
industry: education
---

Imagine opening your computer every morning to organize work and personal life, opening a browser window cleanly arranged like a custom-built drawer tailored to your hands. Unlike the past where numerous tabs lined up horizontally and caused chaos, the sidebar elegantly positioned on the side of the screen and Space-based categorization were a new world of digital workflow. Then one day, a shocking news piece arrives: "The browser you use every day is closing down soon."

The Browser Company announced that the Arc browser, loved by users worldwide for its innovative interface, will only be supported until December 22, 2026, and then completely shut down [BestArcBrowserAlternatives forMac(ArcEnds Dec 22...) | Macfolio](https://macfolio.com/blog/best-arc-browser-alternatives-for-mac). This news plunged Mac users into massive chaos, as they could not bear to go back to the boring top horizontal tab method [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag). Right at that moment, a high school student developer on the other side of the globe directly challenged this desperate situation. Thus, **Zigzag**, an ultra-lightweight Mac browser containing everything Arc users missed, was born in just 3 weeks [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag).

---

## Why does this matter?

Modern web browsers are getting heavier and heavier. By packing in countless features, they devour RAM like a black hole, consume battery at lightning speed, and have program installation sizes ranging from hundreds of megabytes to over a gigabyte. In fact, the soon-to-be-discontinued Arc browser has an installation size exceeding 800MB [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag). 

For average users, this means giving up most computer resources to a browser just to do some web surfing. Moreover, when a big tech service shuts down, users lose their familiar tools without knowing why and have to wander around looking for alternatives. 

Zigzag rebels against the enormity and closed nature of modern software. Its installation size is a mere **18 MB** [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag), requires no account sign-up, and completely excludes telemetry (user behavior tracking data) or analytics tools to ensure absolute privacy [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag). Because it is an open-source project created by an individual, no one can arbitrarily discontinue the service, and anyone can modify and improve the code [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag).

---

## Easy to Understand: Building a Customized Sports Car Optimized for Mac

To put it into perspective, if many existing browsers are like large trucks carrying heavy loads with a giant bus engine, Zigzag can be likened to a sleek, lightweight electric sports car crafted to fit the refined road structure of Mac. In short, it boldly sheds unnecessary weight and focuses solely on essential driving performance.

Zigzag is not a heavy browser built on Google's Chromium (the open-source engine underlying Chrome) or Electron (a framework allowing desktop apps to be made with web technologies) [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag). It utilizes Apple's pure **WebKit** engine built into macOS by default and was written from scratch using **Swift**, Apple's dedicated programming language for device apps [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag). 

It is the same principle as installing a photo editing app on your smartphone: instead of using a heavy general-purpose program that runs poorly across all devices, a dedicated camera app built by directly leveraging iPhone's core system functions runs much faster and consumes less battery. Thanks to this, it delivers a lightweight feel without clutter and a smoothness as if seamlessly fused with the macOS operating system.

It also inherits without exception the core features that Arc browser users were most enthusiastic about:
- **Sidebar and Spaces**: Tabs arranged vertically on the left rather than the top of the window, and space management features allowing you to swipe between work and personal spaces coded with colors [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag), [Zigzag Browser: The polished, native Mac browser for life ...](https://www.producthunt.com/products/zigzag-browser)
- **Split View**: Screen splitting functionality allowing multitasking with up to 4 pages displayed simultaneously in a single window [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)
- **Peek and Command Bar**: Quick link previews that let you peek at links without opening a new window, and a fast command execution bar [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag), [Zigzag Browser — Launch Wire | StartupStarter](https://startupstarter.co/launches/zigzag-browser-native-mac-webkit)

---

## Current Status: Development in Just 3 Weeks, and Seamless Migration

The mastermind behind this amazing browser is **ZigaoWang**, a high school student developer from Shanghai [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag). He stated that he used the Arc browser daily with complete satisfaction and no complaints, so he was deeply shocked by The Browser Company's sudden shutdown announcement [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag). With a simple yet powerful motivation: "I didn't want to go back to boring top tabs," he spent the past 3 weeks tapping away at his keyboard to design Zigzag [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag).

The biggest pain point users face when switching from an existing browser is the hassle of resetting settings and login information. However, Zigzag solved this problem with a single click. Running a single import from other browsers including Arc migrates spaces, pinned tabs, history, saved passwords, cookies, and more all at once [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag). As soon as you open the browser, you can continue your work with existing websites already logged in [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag), [Zigzag Browser: The polished, nativeMacbrowserforlife afterArc](https://www.producthunt.com/products/zigzag-3).

In particular, despite being WebKit engine-based, the ability to directly install extensions from the **Chrome Web Store** (the online marketplace for downloading Google Chrome extensions) is a huge advantage [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag). You can continue using essential extensions you usually rely on, such as password managers like 1Password or Bitwarden, Dark Reader (dark mode), Return YouTube Dislike, and Tampermonkey [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag). 

Additionally, a **powerful built-in ad blocker** based on uBlock Origin and Easylist filters is included by default, automatically rejecting and clearing annoying cookie consent pop-up windows blocking your view [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag).

---

## What's Next?

As Arc browser's official support end date of December 22, 2026, approaches [BestArcBrowserAlternatives forMac(ArcEnds Dec 22...) | Macfolio](https://macfolio.com/blog/best-arc-browser-alternatives-for-mac), user movements to find alternatives will become even busier. In a browser market dominated web giants, Zigzag, presented as an open-source project by a high school developer, is causing a small tectonic shift in the enterprise-centric ecosystem.

Users no longer need to be swayed by a giant corporation's unilateral service termination notice. As an open-source project where source code is public and anyone can contribute [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag), developers worldwide are likely to gather and grow it into an even more robust and secure Mac-exclusive browser. If you are looking for your own lightweight, fast web surfing space that protects your privacy, Zigzag will be the most attractive choice this coming winter.

---

## AI's Perspective

MindTickleBytes AI Reporter's Perspective: Technological progress does not necessarily stem solely from massive capital and hundreds of engineers. The passion of a high school student who refused to endure inconvenience and solved it with code in just 3 weeks reminds us of the true value of software. If you feel fatigued by bloated big tech services, it is time to pay attention to the rise of lightweight and transparent open source projects like Zigzag.

---

## References

1. [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)
2. [Zigzag Browser: The polished, native Mac browser for life ...](https://www.producthunt.com/products/zigzag-browser)
3. [Zigzag: A Lightweight Web Browser for Mac](https://zigzagbrowser.com/)
4. [Zigzag Browser — Launch Wire | StartupStarter](https://startupstarter.co/launches/zigzag-browser-native-mac-webkit)
5. [[5-Minute Review] The Mac browser 'Zigzag Browser' that lets ...](https://note.com/1sht0s/n/n5aa2825dac32?hl=en)
6. [Hacker News => Show](https://www.hacker-news.news/Show)
7. [Zigzag Browser — Launch Wire | StartupStarter](https://startupstarter.co/launches/zigzag-browser-native-mac-webkit)
8. [byearc: newbrowserssto replaceArc](https://byearc.com/)
9. [DownloadArc](https://arc.net/download)
10. [DiaBrowserReview 2026: Is It Worth It? Pricing vsArc| Macfolio](https://macfolio.com/blog/dia-browser-review)
11. [ZigzagBrowser: The polished,nativeMacbrowserforlife afterArc](https://www.producthunt.com/products/zigzag-3)
12. [BestArcBrowserAlternatives forMac(ArcEnds Dec 22...) | Macfolio](https://macfolio.com/blog/best-arc-browser-alternatives-for-mac)