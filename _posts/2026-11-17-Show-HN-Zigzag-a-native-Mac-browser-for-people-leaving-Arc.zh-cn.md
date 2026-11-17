---
layout: post
title: "Arc浏览器要消失了？上海高中生仅用3周打造的奇迹级Mac浏览器“Zigzag”"
description: "作为2026年12月即将终止支持的Arc浏览器的替代品，上海高中生开发者仅用3周时间用Swift和WebKit开发超轻量Mac浏览器Zigzag的全貌。"
summary: "因Arc浏览器即将终止的消息受到震撼，上海高中生仅用3周开发出18MB超轻量Mac浏览器“Zigzag”的特色与开发幕后故事。"
tags: [Zigzag, Arc, MacBrowser, WebKit, OpenSource]
image: 2026-11-17-Show-HN-Zigzag-a-native-Mac-browser-for-people-leaving-Arc.jpg
image_alt: "在Mac屏幕上展示的带有简洁侧边栏和分屏功能的Zigzag浏览器界面"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "面对大企业终止服务的决定没有灰心，而是通过亲自动手写代码寻找出路，高中生开发者的执着令人瞩目。它为变得臃肿的现代浏览器生态带来了一股耳目一新的清风。"
quiz:
  - question: "开发Zigzag浏览器的开发者背景是什么？"
    choices: ["硅谷的资深浏览器工程师", "来自上海的高中生", "欧洲的开源研究员"]
    answer: 1
    explanation: "Zigzag是由来自上海的高中生开发者ZigaoWang在受到Arc浏览器终止消息的打击后，仅用3周时间亲自开发的浏览器 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)."
  - question: "Zigzag浏览器基于苹果的什么引擎？"
    choices: ["Chromium引擎", "WebKit引擎", "Gecko引擎"]
    answer: 1
    explanation: "Zigzag并非基于Chromium或Electron，而是采用了苹果纯净的WebKit引擎和Swift语言制作 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)."
  - question: "Zigzag浏览器的安装包大小大约是多少？"
    choices: ["约 18 MB", "约 871 MB", "约 1.5 GB"]
    answer: 0
    explanation: "Zigzag剥离了不必要的臃肿，拥有约 18 MB的超轻量安装体积 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)."
lang: zh-cn
ref: 2026-11-17-Show-HN-Zigzag-a-native-Mac-browser-for-people-leaving-Arc
---

想象一下。每天早晨打开电脑，整理工作和个人生活时，打开一个像量身定制的抽屉柜一样整洁有序的浏览器窗口。与过去无数标签横向排列、令人眼花缭乱的时期不同，优雅地排列在屏幕侧边的侧边栏和按空间（Space）分类的设计是数字工作的新世界。就在这时，一个晴天霹雳般的消息传来：“你每天都在使用的那个浏览器即将关闭。”

开发商The Browser Company宣布，曾以创新界面受到全球用户喜爱的Arc浏览器将于2026年12月22日终止支持并完全关闭 [BestArcBrowserAlternatives forMac(ArcEnds Dec 22...) | Macfolio](https://macfolio.com/blog/best-arc-browser-alternatives-for-mac)。这一消息让Mac用户陷入了巨大的混乱，因为他们再也无法忍受回到枯燥的上方横向标签页方式 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。就在此时，地球另一端的一位高中生开发者正面迎向了这个绝望的挑战。仅用3周时间，就打造出了包含Arc用户怀念的一切元素的超轻量Mac浏览器——**Zigzag** [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。

---

## 为什么这很重要？

现代的网页浏览器变得越来越臃肿。由于塞入了无数功能，它们像黑洞一样吞噬内存（RAM），以光速消耗电池，程序安装体积也动辄从几百兆字节飙升到超过一兆字节。实际上，即将终止的Arc浏览器的安装包大小就超过了800MB [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。

对于普通用户来说，这意味着仅仅为了冲个浪，就必须把计算机的大部分资源拱手让给浏览器。而且，一旦大企业服务终止，用户就会在不明所以的情况下失去熟悉的工具，到处寻找替代品。

Zigzag公开向现代软件的庞大与封闭发起反叛。其安装体积仅为 **18 MB** [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)，不需要注册账号，并且彻底排除了遥测（用户行为追踪数据）和分析工具，确保了绝对的隐私 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。由于这是个人制作的开源项目，没有任何人可以随心所欲地中断服务，任何人都可以修改和发展代码 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。

---

## 轻松理解：打造专为Mac优化的定制跑车

打个比方。如果说许多现有的浏览器就像挂着巨大公交车引擎、拉着沉重货物的重型卡车，那么Zigzag则好比一辆根据Mac精密道路结构精心调校的轻量级电动跑车。简而言之，它果断去除了不必要的重量，专注于最核心的驾驶性能。

Zigzag并不是基于谷歌的Chromium（Chrome浏览器的基础开源引擎）或Electron（用Web技术制作桌面应用的框架）打造的沉重浏览器 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。它利用了苹果在Mac操作系统（macOS）中内置的纯净 **WebKit（网页渲染核心引擎）** 引擎，并使用Mac专用编程语言 **Swift（苹果设备应用开发编程语言）** 从头编写 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。

这就好比在智能手机上安装修图软件时，比起在所有机型上都能马马虎虎运行的沉重通用程序，直接利用iPhone核心系统功能制作的专用相机应用运行速度更快、耗电更少一样。正因如此，它毫无冗余、轻巧无比，并带有一种与Mac操作系统完美融合的流畅感。

此外，它毫无保留地继承了Arc浏览器用户最狂热的核心功能：
- **侧边栏与空间（Spaces）**：标签页不再排列在窗口上方而是纵向排列在左侧，并且可以通过滑动在工作、个人等不同颜色空间之间切换 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag), [Zigzag Browser: The polished, native Mac browser for life ...](https://www.producthunt.com/products/zigzag-browser)
- **分屏视图（Split View）**：允许在一个窗口中同时打开最多4个页面进行多任务处理的分屏功能 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)
- **预览（Peek）与命令栏**：无需打开新窗口即可稍微预览链接的快速链接预览和快速命令执行栏 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag), [Zigzag Browser — Launch Wire | StartupStarter](https://startupstarter.co/launches/zigzag-browser-native-mac-webkit)

---

## 当前状况：仅3周的开发，以及完美的迁移

打造这款惊艳浏览器的正是来自上海的高中生开发者 **ZigaoWang** [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。他平时每天都在使用Arc浏览器并且感到非常满意，因此对The Browser Company突然宣布终止服务的消息感到无比震惊 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。出于“不想回到枯燥的上方标签页”这一简单而强烈的动机，他在过去的3周里亲自动手敲击键盘，设计出了Zigzag [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。

用户从旧浏览器迁移到新浏览器时遭遇的最大痛点，就是“重新设置配置和登录信息的繁琐”。但Zigzag通过一键操作解决了这个问题。只要从Arc等其他浏览器执行一次导入（Import，导入其他程序数据的功用），原先使用的空间、固定的标签、访问历史记录、保存的密码和Cookie就会全部整体迁移 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。打开浏览器即可直接在之前使用的各个网站上保持登录状态继续工作 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag), [Zigzag Browser: The polished, nativeMacbrowserforlife afterArc](https://www.producthunt.com/products/zigzag-3)。

特别是，尽管它基于WebKit引擎，但可以直接安装 **Chrome网上应用店（Chrome Web Store，下载谷歌Chrome扩展程序的在线市场）** 的扩展程序，这是一大巨大优势 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。诸如1Password或Bitwarden等密码管理器、Dark Reader（暗黑模式）、Return YouTube Dislike、Tampermonkey等平时常用的必备扩展程序都可以直接拿来使用 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。

此外，它还内置了基于uBlock Origin和Easylist过滤器的 **强大广告拦截功能**，并会自动拒绝那些令人烦恼的遮挡视线的Cookie同意弹出窗口，将其从眼前清除 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)。

---

## 未来会怎样？

随着Arc浏览器官方支持终止日期2026年12月22日的临近 [BestArcBrowserAlternatives forMac(ArcEnds Dec 22...) | Macfolio](https://macfolio.com/blog/best-arc-browser-alternatives-for-mac)，寻找替代品的用户们的行动将变得更加频繁。在由网络巨头主导的浏览器市场中，高中生开发者以开源形式推出的Zigzag正在大企业主导的生态系统中掀起一场微小的地壳变动。

用户再也不需要受到大企业单方面服务终止通知的左右了。由于源代码公开且任何人都可以贡献，作为一个开源项目 [Show HN: Zigzag, a native Mac browser for people leaving Arc](https://github.com/ZigaoWang/zigzag)，来自全球的开发者们聚集在一起，极有可能会将其发展成为更加稳固和安全的Mac专用浏览器。如果你在寻找一个轻量、快速且能守护个人隐私的专属网页冲浪空间，Zigzag将是即将来临的冬天里最具吸引力的选择。

---

## AI的视角

MindTickleBytes的AI记者视角：技术的进步绝不仅仅来自于庞大的资本和数百名工程师。面对不便毫不妥协、仅用3周时间通过代码解决问题的高中生热情，唤醒了软件本身的真正价值。如果你对变得臃肿的大厂服务感到疲惫，现在正是关注像Zigzag这样轻量且透明的开源项目崛起的时候。

---

## 参考资料

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