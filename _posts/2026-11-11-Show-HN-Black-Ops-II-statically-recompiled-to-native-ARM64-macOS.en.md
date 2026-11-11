---
layout: post
title: "Call of Duty on my Mac? The Resurrection of Games Brought by 'Static Recompilation'"
description: "Learn about static recompilation, a technique that natively runs Call of Duty: Black Ops II on modern Macs (macOS) without an emulator."
summary: "Through 'static recompilation,' a technology that directly translates the code of old games into the language of modern machines, classic masterpieces like Call of Duty: Black Ops II are starting to run natively on modern Macs."
tags: [AI, Gaming, Technology, Mac, Call of Duty]
image: 2026-11-11-Show-HN-Black-Ops-II-statically-recompiled-to-native-ARM64-macOS.jpg
image_alt: "Call of Duty: Black Ops II running on a modern MacBook"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Static recompilation, a technique that transcends the limits of emulation by directly translating code, will become a new milestone in game preservation. It is astonishing that the heritage of the past can now fully utilize the performance of modern hardware."
quiz:
  - question: "What is the biggest advantage of static recompilation?"
    choices: ["Extremely fast emulator execution", "Native performance without an emulator", "Cloud game streaming"]
    answer: 1
    explanation: "Static recompilation directly translates game code into the language of modern devices, so no separate emulator is needed."
  - question: "Which game was recently recompiled for Mac (macOS)?"
    choices: ["Call of Duty: Black Ops II", "Battlefield 2042", "Cyberpunk 2077"]
    answer: 0
    explanation: "Black Ops II was recently statically recompiled for ARM64 Macs by the developer adrbn."
  - question: "How does static recompilation work?"
    choices: ["Internet real-time conversion", "Converting existing game code into modern machine instruction sets", "Modifying graphics only"]
    answer: 1
    explanation: "It translates the machine code of existing games into instructions that can be executed directly on new hardware (e.g., ARM64)."
lang: en
ref: 2026-11-11-Show-HN-Black-Ops-II-statically-recompiled-to-native-ARM64-macOS
audio: 2026-11-11-Show-HN-Black-Ops-II-statically-recompiled-to-native-ARM64-macOS.en.mp3
industry: general
---

Imagine this: You open your 2020 MacBook Pro and click the icon for the decade-old classic, *Call of Duty: Black Ops II*. Normally, your computer would heat up or stutter as it launched a complex emulator or virtual machine. But this game unfolds on your screen as smoothly as if it were released yesterday, running at nearly 60 frames per second.

This is made possible by a technology recently gaining traction in the developer community called "Static Recompilation." The history of gaming is meeting modern cutting-edge hardware and finding new life.

## Why It Matters

The classic games we enjoy were typically crafted for the hardware of their time (such as older PCs or consoles). As these devices age and eventually become obsolete, these games risk vanishing into history. Until now, we used a technology called an "emulator" to run them. Like an interpreter translating a foreign language, an emulator converts the language of old games into something modern computers can understand in real-time. However, this process incurs significant performance loss, often leading to graphical glitches or audio lag.

Static recompilation is different. Instead of using an interpreter, it entirely rewrites the game's language into the language of the modern machine. This allows it to run "natively" on modern hardware without an emulator—just like a game built specifically for that device, with perfect performance. We no longer have to keep our past masterpieces locked away on outdated devices.

## The Explainer

Let’s use an analogy. Suppose you want to send a letter written in Korean to a friend in an English-speaking country.

*   **Emulator Method:** It’s like you standing next to your friend and simultaneously translating your Korean into English in real-time. If your (the emulator's) translation speed can’t keep up with your friend’s understanding speed, or if a mistranslation occurs, the conversation falls apart.
*   **Static Recompilation Method:** It’s like having a professional translator rewrite the entire letter in perfect English before sending it. Your friend can understand and enjoy the content so naturally that they wouldn't even know it was originally written in Korean.

In the case of [Call of Duty: Black Ops II](https://github.com/adrbn/bo2-mac) running on macOS, the developer used a tool called "Remill" to convert the game’s 32-bit x86 (old PC language) code into "LLVM IR" (intermediate representation), and then transferred it to ARM64 (Apple Silicon) instructions—the brain of the latest Macs. They also manually handled the translation of the Windows graphics API (Direct3D 11) to the modern Mac graphics standard, "Metal." This is what made the astonishing performance of [nearly 60 frames per second](https://github.com/adrbn/bo2-mac) possible.

## Where We Stand

This technology is already becoming a major trend in the gaming industry. Beyond *Black Ops II*, [*Max Payne 3*](https://www.youtube.com/watch?v=CGYbWKSA5QU) is running at 60 FPS on PS5, and countless classic masterpieces like [*Ninja Gaiden Black*](https://portedgames.com/recompiled-games/), [*God of War*](https://recomplauncher.com/game/gow-native-pc), [*Bomberman 64*](https://recompsoftware.com/games/), [*Halo: CE*](https://recompsoftware.com/games/), [*Rampage*](https://quiverlauncher.com/apps/rampage-recompiled), and [*Final Fantasy VII*](https://andreyvelsk.github.io/GAFT/project/ff7recomp/) are being reborn as native ports for their respective modern platforms.

However, it is not perfect. In the case of *Black Ops II*, [some heat issues](https://github.com/adrbn/bo2-mac) still remain as a challenge to be solved. Furthermore, static recompilation is not a technology that can be mass-produced, as it requires analyzing and converting the code for each game individually.

## What's Next

Moving forward, "static recompilation" is expected to become the core standard for game preservation. Developers are already looking beyond the original game by adding features like [split-screen or LAN modes](https://github.com/adrbn/bo2-mac) to the *Black Ops II* project.

By allowing individuals to run game files they own on modern hardware without any restrictions, this technology serves as a powerful tool to overcome the high costs of remastering by major game publishers and the technical limitations of emulation. One day, the latest games we buy today will eventually reach a point, 20 years from now, where they are perfectly playable again through static recompilation.

## References

1. [Show HN: Black Ops II statically recompiled to native ARM64 macOS](https://github.com/adrbn/bo2-mac)
2. [Max Payne 3 Running NATIVELY on PS5 at 60 FPS... - YouTube](https://www.youtube.com/watch?v=CGYbWKSA5QU)
3. [Recompiled Games List: Every Native PC Port... | PortedGames](https://portedgames.com/recompiled-games/)
4. [God of War Native PC — PC recomp of God of War · RecompLauncher](https://recomplauncher.com/game/gow-native-pc)
5. [Decompiled & recompiled games · Recomp](https://recompsoftware.com/games/)
6. [Rampage Recompiled – Rampage: World Tour Recomp | Quiver](https://quiverlauncher.com/apps/rampage-recompiled)
7. [Call of Duty: Black Ops II - recomp.party](https://recomp.party/p/adrbn/bo2-mac/)
8. [bo2-mac: Call of Duty: Black Ops II PC recomp, source ...](https://recompsoftware.com/p/bo2-mac/)
9. [Black Ops II Recompiled — PC recomp of Call of Duty: Black ...](https://recomplauncher.com/game/bo2-mac?lang=en-GB)
10. [bo2-recompiled: Call of Duty: Black Ops II recompilation ...](https://recomp.gg/p/bo2-recompiled)
11. [FF7 Recomp | Games & Apps for AYN Thor](https://andreyvelsk.github.io/GAFT/project/ff7recomp/)