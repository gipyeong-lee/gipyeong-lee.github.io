---
layout: post
title: "在我的 Mac 上运行《使命召唤》？“静态重编译”带来的游戏复活"
description: "无需模拟器，在最新款 Mac (macOS) 上原生运行《使命召唤：黑色行动 2》的技术——了解静态重编译。"
summary: "通过将老游戏的源代码直接转换为现代设备的语言这一“静态重编译”技术，《使命召唤：黑色行动 2》等经典名作开始能够在最新款 Mac 上以原生速度运行。"
tags: [AI, 游戏, 技术, Mac, 使命召唤]
image: 2026-11-11-Show-HN-Black-Ops-II-statically-recompiled-to-native-ARM64-macOS.jpg
image_alt: "在新款 MacBook 上运行《使命召唤：黑色行动 2》的画面"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "突破模拟器局限、直接翻译代码的静态重编译技术，将成为游戏保存史上的新里程碑。过去的游戏资产能够充分利用现代硬件的性能，这一点令人惊叹。"
quiz:
  - question: "静态重编译最大的优势是什么？"
    choices: ["极速的模拟器运行", "无需模拟器实现原生性能", "云游戏流媒体传输"]
    answer: 1
    explanation: "静态重编译将游戏代码直接转换为现代设备的语言，因此无需使用任何模拟器。"
  - question: "最近被重编译到 Mac (macOS) 上的游戏是哪一款？"
    choices: ["《使命召唤：黑色行动 2》", "《战地 2042》", "《赛博朋克 2077》"]
    answer: 0
    explanation: "最近，开发者 adrbn 将《使命召唤：黑色行动 2》成功静态重编译至 ARM64 架构的 Mac 上。"
  - question: "静态重编译是如何工作的？"
    choices: ["互联网实时转换", "将原有游戏代码转换为现代设备的指令集", "仅修改图形画面"]
    answer: 1
    explanation: "这是一种将原有游戏的机器语言代码翻译为可在新硬件（如 ARM64）上直接运行的指令的方法。"
lang: zh-cn
ref: 2026-11-11-Show-HN-Black-Ops-II-statically-recompiled-to-native-ARM64-macOS
---

想象一下：你打开一台 2020 年款的 MacBook Pro，点击运行十多年前的经典游戏《使命召唤：黑色行动 2》。通常情况下，为了运行复杂的模拟器或虚拟机，电脑可能会发热严重或者运行卡顿。但这款游戏就像是昨天刚刚发布的一样，画面运行流畅，几乎达到了 60 帧。

这得益于开发者社区中兴起的一项名为“静态重编译 (Static Recompilation)”的技术。游戏的历史正与现代最尖端的硬件碰撞，焕发出新的生命。

## 这为什么重要？ (Why It Matters)

我们喜爱的经典游戏大多是针对当时的硬件（如老式 PC 或游戏主机）开发的。随着时间推移，设备逐渐老化，这些游戏面临着从历史中消失的风险。迄今为止，我们一直使用“模拟器”技术来运行它们。模拟器就像是一名翻译，将老游戏的语言实时“翻译”成现代电脑能听懂的内容。但在这个过程中会产生显著的性能损耗，有时还会出现画面破碎或声音延迟等问题。

静态重编译则不同。它不是使用翻译，而是将游戏的语言本身完全改写为现代设备的语言。通过这种方式，即使无需模拟器，游戏也能在最新设备上“原生”运行，就像是专门为该设备开发的一样，达到完美的性能表现。现在，我们不再需要将过去的经典名作困在老旧的设备里了。

## 原理解析 (The Explainer)

让我们打个比方。假设你要给说英语的朋友寄一封韩文信：

*   **模拟器方式：** 就像你站在英语国家朋友的旁边，实时将韩语口译成英语。如果你的（模拟器）翻译速度跟不上朋友的理解速度，或者出现误译，交流就会卡壳。
*   **静态重编译方式：** 就像在寄出信件之前，专业翻译员已经将内容完美地重写为地道的英语。朋友收到后，甚至完全不知道原件是韩文，能非常自然地理解和欣赏内容。

从这次在 Mac (macOS) 上运行 [《使命召唤：黑色行动 2》](https://github.com/adrbn/bo2-mac) 的案例来看，开发者使用了名为“Remill”的工具，将游戏的 32 位 x86（旧式 PC 语言）代码转换为“LLVM IR（中间语言）”，然后再将其迁移到最新款 Mac 的大脑——ARM64（Apple Silicon）指令集上。此外，他还直接处理了将当时的 Windows 图形调用方式（Direct3D 11）转换为最新款 Mac 图形标准“Metal”的工作。得益于此，[几乎 60 帧](https://github.com/adrbn/bo2-mac) 的惊人性能才得以实现。

## 当前现状 (Where We Stand)

这项技术已经成为游戏行业的一股巨大潮流。除了《黑色行动 2》，[《马克思佩恩 3》](https://www.youtube.com/watch?v=CGYbWKSA5QU) 已能在 PS5 上以 60 帧运行，还有《[忍者龙剑传：黑之章](https://portedgames.com/recompiled-games/)》、《[战神](https://recomplauncher.com/game/gow-native-pc)》、《[炸弹人 64](https://recompsoftware.com/games/)》、《[光环：战斗进化](https://recompsoftware.com/games/)》、《[暴力破坏者](https://quiverlauncher.com/apps/rampage-recompiled)》、《[最终幻想 7](https://andreyvelsk.github.io/GAFT/project/ff7recomp/)》等大量经典名作，都正在以各自的最新设备端口形式获得新生。

不过，它并不完美。即便在《黑色行动 2》的项目中，[部分发热问题](https://github.com/adrbn/bo2-mac) 仍然是一个待解决的难题。此外，静态重编译需要针对每一款游戏进行代码分析和逐一转换，因此这并非一种可以大规模自动生产的技术。

## 未来展望 (What's Next)

展望未来，“静态重编译”有望成为游戏保存领域的核心标准。开发者们甚至在《黑色行动 2》的项目中尝试添加 [分屏 (Split-screen) 或 LAN 局域网模式](https://github.com/adrbn/bo2-mac) 等功能，意在实现超越原版的扩展。

这项技术让个人能够毫无限制地在最新设备上运行自己拥有的游戏文件，它将成为一种强大的工具，一次性突破大型游戏公司昂贵的重制成本以及模拟器技术上的瓶颈。或许有一天，我们今天购买的最新游戏，在 20 年后也能通过静态重编译技术完美运行。

## 参考资料

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