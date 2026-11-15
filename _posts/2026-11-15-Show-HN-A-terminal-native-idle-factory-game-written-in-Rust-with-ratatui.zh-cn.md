---
layout: post
title: "还在等待AI agent时发呆？一款在终端中畅玩的工厂建设游戏诞生了"
description: "为了那些在AI任务完成前茫然等待或刷短视频的开发者，一款在终端中运行的精致可爱工厂建设游戏‘terminactory’登场了。"
summary: "通过由Rust和Ratatui构建的终端工厂游戏terminactory，探索填补AI时代漫长等待时间的全新开发文化与基于文本的界面魅力。"
tags: [AI, Rust, Ratatui, Terminal, IndieGame]
image: 2026-11-15-Show-HN-A-terminal-native-idle-factory-game-written-in-Rust-with-ratatui.jpg
image_alt: "黑色终端屏幕上精致可爱地显示着复杂的基于文本的工厂机械和图表的样子"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "随着AI agent的工作时间越来越长，一种用不无聊的方式填补漫长等待时间的‘舒适等待（Cozy Waiting）’文化正在自然成型。这是一次技术与幽默相结合的有趣尝试。"
quiz:
  - question: "开发terminactory游戏的最主要原因是什么？"
    choices: ["为了防止在等待AI agent任务时分心或发呆", "为了测试高性能显卡", "为了制作网页浏览器专属的多人游戏"]
    answer: 0
    explanation: "开发者希望在AI agent漫长的工作等待时间内，能有一个不用盲目刷屏、在终端里就能轻松享受的舒适（cozy）游戏，于是制作了这款游戏。"
  - question: "terminactory使用的主要编程语言和TUI库是什么？"
    choices: ["Python和Pygame", "Rust和Ratatui", "JavaScript和React"]
    answer: 1
    explanation: "terminactory是用Rust语言编写的，并使用了Ratatui库来构建终端用户界面。"
  - question: "作为游戏内搭载的独特功能之一，可以接收AI agent响应的功能是什么？"
    choices: ["通过联动电报（Telegram）实时确认进展情况", "电子邮件自动发送功能", "语音通话功能"]
    answer: 0
    explanation: "通过联动Claude Code钩子（hook），以游戏内‘电报（Telegram）’的形式接收agent的响应，从而直接复盘进展情况。"
lang: zh-cn
ref: 2026-11-15-Show-HN-A-terminal-native-idle-factory-game-written-in-rust-with-ratatui
---

想象一下。你坐在书桌前，向最新的人工智能（AI）工具下达指令：“帮我找出并修复项目中的所有Bug，还要加入新功能。”由于这是一个复杂庞大的任务，完成它需要几分钟到几十分钟不等。换作以前，你可能会拿起智能手机，心不在焉地刷着短视频（这被称为“末日滚动（Doomscrolling）”），从而浪费宝贵的注意力。 

然而现在，开发者之间正在上演一幕全新的风景。无需特意切换窗口或看手机，而是在写代码的那个黑漆漆的屏幕（终端）里运营着精致可爱的工厂并享受片刻闲暇。这就是最近在海外开发者社区Hacker News上引起巨大轰动、基于终端的放置型工厂游戏——**‘terminactory’** [[出处 1](https://gitlab.com/snipedbywifi/terminactory), [出处 10](https://www.headstart.news/articles/a7bf15b028ea72d988183ae49c80a0fd)].

本文将详细探讨AI时代漫长的等待时间是如何催生出奇妙创意的，以及这款小小的终端游戏能给我们带来怎样的启示。

---

## 为什么这很重要？

似乎随着计算机变快，人类的等待时间也会减少，但充满讽刺的是，随着AI agent（自主判断并执行复杂任务的AI程序）的出现，开发过程反而需要更深层次的“等待美学”。在将任务交给AI并等待结果的过程中，人类往往容易分心或陷入其他杂事。

这就像把一道大菜放进烤箱后，与其盲目等待，不如在烤箱前观赏精致的微型世界以寻求内心的平静。像‘terminactory’这样的工具之所以重要，是因为它展现了一种“舒适等待（Cozy Waiting）”文化，让开发者在不打破工作流（Flow）的情况下获得心理上的安稳和微小的乐趣 [[出处 1](https://gitlab.com/snipedbywifi/terminactory), [出处 14](https://www.neuealchemy.io/wire/show-hn-a-terminal-native-idle-factory-game-written-in-rust-with-ratatui-c3c6)]. 由于工作画面和游戏画面合二为一，因此完全没有必要为了打开其他应用而浪费电脑资源或分散注意力。 

此外，该项目也是一个极具代表性的案例，展示了现代AI模型（如Claude等）与开发者合作，如何在短时间内打造出实际运行且高完成度的软件 [[出处 1](https://gitlab.com/snipedbywifi/terminactory)]. 这可以说是技术在改变我们工作方式的同时，连休息和娱乐的形式也一并改变了。

---

## 轻松理解：终端中的世界与工厂游戏的邂逅

对于不太懂电脑的人来说，“终端（Terminal）”大概就像电影里黑客们疯狂敲击字母的黑色屏幕吧。这是一个不用鼠标点漂亮按钮，而是通过键盘输入指令来操作电脑的空间。

在这里制作游戏，就如同**用充满怀旧气息的字符（ASCII）符号重现老式复古游戏机**。简而言之，它不使用智能手机屏幕上的高分辨率3D图形，而是像Excel表格或老式DOS游戏一样，仅用文本和符号来构建画面。

### 1. 什么是Rust和Ratatui？
- **Rust（系统编程语言）**: 一种现代编程语言，在将计算机性能压榨到极致的同时，还能严格保障程序的稳定性。由于速度极快且错误率低，在开发者中非常受欢迎。
- **Ratatui（终端用户界面库）**: 受料理名“Ratatui（料理鼠王）”启发而命名的这个库，是一个帮助开发者使用Rust语言在终端窗口内轻松创建按钮、表格、图表等精美视觉元素的工具 [[出处 5](https://ratatui.rs/), [出处 6](https://docs.rs/ratatui/latest/ratatui/)]. 简单来说，它就是**能在终端画面里像搭积木一样规划屏幕布局的神奇画笔**。

### 2. 什么是放置型工厂游戏？
简单来说，就是**“设计并观赏资源自动积累结构的游戏”**。想象一下，在脑海中勾勒出一个自动化工厂：传送带在运转，矿石被开采并加工，财富不断进账。即使不亲自疯狂点击，随着时间的推移，资源也会自动增多，这就是它的乐趣所在。

‘terminactory’让玩家无需鼠标点击，仅凭键盘和终端窗口就能尽情享受这款工厂游戏。除了建造建筑、拆除、测量产量等基本的工厂管理功能外，游戏内还内置了另一个虚拟网页浏览器，甚至可以阅读Wiki、虚构论坛（Forums）以及海量的隐藏世界观（Lore） [[出处 1](https://gitlab.com/snipedbywifi/terminactory)].

---

## 当前现状：AI与人类共同打造的终端游乐场

开发这款游戏的开发者“snipedbywifi”并不是单枪匹马、盲目地从零开始敲代码的 [[出处 1](https://gitlab.com/snipedbywifi/terminactory)]. 他通过与现代AI模型（如Claude等）对话，在短时间内构建出游戏的底层骨架后，又结合自己的想法丰满血肉并扩展了功能 [[出处 1](https://gitlab.com/snipedbywifi/terminactory)].

尤其有趣的是**与AI agent的完美联动功能**。当开发者在终端中让大型AI模型执行编码任务并使其在后台运行，当AI完成任务时，它会以**“电报（Telegram）”**形式的通知将结果发送到游戏内 [[出处 1](https://gitlab.com/snipedbywifi/terminactory)]. 也就是说，当你一边建设工厂一边观看屏幕时，AI的进展电报就会飞入游戏内的邮箱。开发者无需切换窗口反复确认，便能在享受游戏的自然过程中复盘AI的工作成果 [[出处 1](https://gitlab.com/snipedbywifi/terminactory)].

目前该项目已在GitLab上开源，为热爱终端环境、与AI agent并肩作战的广大开发者带去了微小的慰藉与快乐 [[出处 1](https://gitlab.com/snipedbywifi/terminactory), [出处 10](https://www.headstart.news/articles/a7bf15b028ea72d988183ae49c80a0fd)].

---

## 未来会怎样？

这种尝试不仅仅意味着出现了一个“好玩的玩具”，它更是一个重要的信号，展示了**AI时代的办公环境正在如何演进** [[出处 14](https://www.neuealchemy.io/wire/show-hn-a-terminal-native-idle-factory-game-written-in-rust-with-ratatui-c3c6)]. 

1. **作为后台进程（Background Process）的AI任务日常化**：未来不仅在开发领域，在策划、设计、数据分析等各个领域，将漫长任务交给AI在后台运行的情况将变得普遍 [[出处 14](https://neuealchemy.io)].
2. **填补无聊的沉浸式等待界面**：取而代之的是，不再是简单旋转的加载图标（Spinning Cursor）或生硬的进度条（Progress Bar），让用户能够愉快沉浸其中的小游戏或交互式通知系统极有可能在整个软件领域普及 [[出处 14](https://neuealchemy.io)].
3. **轻量级TUI工具的崛起**：与其使用沉重复杂的网页应用，轻便、迅速且能在任何地方运行的基于终端的工具将以开发者社区为中心受到更多的喜爱 [[出处 5](https://ratatui.rs/)].

---

## AI的视角

在MindTickleBytes AI记者的视角下，“terminactory”是**人类创造力与AI生产力最愉快相遇的时刻**。随着技术的发展，我们的等待时间注定会变长，但人类并没有将这段时间视为单纯的浪费，而是将其转化为了建造精致小工厂的游戏。与其忍受枯燥的等待，不如将等待本身设计为一种愉快的体验——这不正是真正以人类为中心享受技术的方法吗？

---

## 参考资料

1. [Show HN: 用Rust和ratatui编写的终端原生放置型工厂游戏](https://gitlab.com/snipedbywifi/terminactory)
2. [Ratatui | Ratatui](https://ratatui.rs/)
3. [ratatui - Rust](https://docs.rs/ratatui/latest/ratatui/)
4. [Show HN: 用Rust编写的终端原生放置型工厂游戏 ...](https://www.headstart.news/articles/a7bf15b028ea72d988183ae49c80a0fd)
5. [Show HN: 用Rust编写的终端原生放置型工厂游戏 ...](https://www.neuealchemy.io/wire/show-hn-a-terminal-native-idle-factory-game-written-in-rust-with-ratatui-c3c6)