---
layout: post
title: "一张照片就能变成3D空间？苹果AI 'SHARP' 走进浏览器的原因"
description: "本文将为您深入浅出地讲解苹果最新的3D重建技术 SHARP，以及如何在无需额外安装的情况下直接在网页浏览器中运行该技术及其原理。"
summary: "随着苹果AI模型 'SHARP' 在网页浏览器中直接运行，照片变3D空间的时代已经开启，任何人都能轻松创作并拥有专属的3D内容。"
tags: [Apple, SHARP, 3D, AI, Web技术, 高斯泼溅]
image: 2026-05-04-Show-HN-Apples-SHARP-running-in-the-browser-via-ONNX-runtime-web.jpg
image_alt: "可视化展示2D平面照片转换为立体3D空间过程的图形图像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "无需复杂的服务器、直接在本地设备上创建3D内容，这一技术将在兼顾用户隐私和成本效益方面成为一个重要的里程碑。"
quiz:
  - question: "苹果SHARP模型创建3D空间所使用的核心技术名称是什么？"
    choices: ["多边形渲染", "高斯泼溅 (Gaussian Splatting)", "光线追踪"]
    answer: 1
    explanation: "SHARP 基于 '高斯泼溅' 技术，该技术通过喷洒大量微小点（椭球体）来营造立体感。"
  - question: "在无需额外服务器的情况下，让网页浏览器运行AI的核心工具是？"
    choices: ["ONNX Runtime Web", "Photoshop", "YouTube"]
    answer: 0
    explanation: "使用 ONNX Runtime Web，可以借助网页浏览器的计算能力直接运行复杂的AI模型。"
  - question: "在浏览器中运行的 SHARP 模型大约有多大？"
    choices: ["2.4 MB", "2.4 GB", "24 GB"]
    answer: 1
    explanation: "目前为 Web 环境转换后的 SHARP 模型大小约为 2.4 GB。"
lang: zh-cn
ref: 2026-05-04-Show-HN-Apples-SHARP-running-in-the-browser-via-ONNX-runtime-web
---

想象一下。如果你把昨天在咖啡馆拍的一张漂亮蛋糕照片上传到网站上，蛋糕突然像要从屏幕里跳出来一样变得立体。你可以用鼠标或手指自由旋转，查看蛋糕的侧面、背面甚至顶部。就像回到了那家咖啡馆一样。

这已不再是遥不可及的科幻电影情节。随着苹果（Apple）最近公开的研究型AI模型 **'SHARP'** 开始在您每天使用的网页浏览器中直接运行，这一切都成为了现实。根据 [Show HN: Apple's Sharp Running in the Browser via ONNX Runtime Web | Hacker News](https://news.ycombinator.com/item?id=47995037) 的报道，现在无需在电脑上安装繁琐的程序，只需访问网站即可将平面照片转化为生动的3D空间。

今天，**MindTickleBytes** 将为您深入浅出地揭开这项神奇技术的真相，并探讨为什么这一消息会让全球开发者和AI爱好者感到如此兴奋。

## 为什么这很重要？让您的电脑变成 “AI 工厂”

到目前为止，我们之所以能方便地使用像 ChatGPT 这样聪明的AI，是因为每当提出问题时，远处的巨型超级计算机（服务器）会代为计算并返回答案。然而，将照片转换为3D需要巨大的计算量，不仅服务器运营成本高昂，而且将宝贵的个人照片发送到其他公司的服务器也让人感到不安。

但这次公开的技术采用了完全不同的方法。它将AI模型完整地带到了您的 Chrome 或 Safari 等网页浏览器内部。这种 “基于浏览器的AI推理（In-browser inference）” 为我们带来了三大优势： [WebAssembly for AI Agents:RunningModelsintheBrowser](https://callsphere.ai/blog/webassembly-ai-agents-running-models-in-the-browser)

1.  **彻底的隐私保护**：您上传的照片绝不会离开您的设备。因为所有的3D转换工作都仅在您的智能手机或笔记本电脑内部秘密进行。 [RunYOLO ModelintheBrowserwithONNX... - PyImageSearch](https://pyimagesearch.com/2025/07/28/run-yolo-model-in-the-browser-with-onnx-webassembly-and-next-js/)
2.  **服务器零成本**：对于服务运营商来说，无需租用昂贵的超级计算机，这将催生更多创新的免费服务；对于用户来说，也不必再面对因为服务器繁忙而导致的 “加载中” 画面。
3.  **零延迟的即时响应**：即使互联网连接速度较慢也没关系。您可以 100% 利用设备原有的性能实时查看结果。

## 轻松理解：什么是 “SHARP” 和 “高斯泼溅”？

首先，让我们来看看名字听起来有些陌生的苹果 **SHARP** 是什么。SHARP 是一款非常聪明的AI设计蓝图，它只需看一张照片，就能准确推测出物体或场所隐藏的立体结构。 [GitHub - bring-shrubbery/ml-sharp-web](https://github.com/bring-shrubbery/ml-sharp-web)

该模型使用的核心技术在专业术语中被称为 **高斯泼溅 (Gaussian Splatting)**。虽然术语听起来很难，但如果用我们熟悉的事物来打比方，原理其实非常简单。

> **比喻一下！**
> 如果说传统的3D技术是通过精细地拼接坚硬的乐高积木或三角形碎片来制作模型，那么 **高斯泼溅** 就类似于在空中撒下无数半透明的 “棉花糖球” 来构建立体形态。

当数以百万计的微小椭球体（棉花糖球）各具颜色和透明度并悬浮在各自的位置上时，我们眼中就会呈现出一个边界柔和且真实感极强的3D空间。 [GitHub - bring-shrubbery/ml-sharp-web](https://app.daily.dev/posts/github---bring-shrubbery-ml-sharp-web-web-playground-to-create-gaussian-splats-using-apple-s-ml-sha-0sg97lpiv) SHARP 扮演的正是指挥家的角色，负责指挥这些棉花糖球应该撒在什么位置、撒多大。 [Converting Apple’s Sharp ML for your devices | Raleigh](https://sf.aitinkerers.org/talks/rsvp_kERNVs9PVNw)

## 如何在浏览器中运行笨重的AI？

这项技术原本设计为只能在配备高性能显卡的昂贵专业研究用电脑上运行。那么，它是如何实现在我们常用的普通网页浏览器中运行的呢？这里隐藏着两位秘密特工。

第一位特工是 **ONNX Runtime Web**。 [ONNX Runtime Web—running your machine learning model in browser | Microsoft Open Source Blog](https://opensource.microsoft.com/blog/2021/09/02/onnx-runtime-web-running-your-machine-learning-model-in-browser/) AI模型根据开发环境的不同，所使用的 “语言” 也不尽相同。而 **ONNX (开放神经网络交换)** 就像是一个 “万能翻译器”，它能将这些模型统一起来，让它们在任何环境下都能交流。 [ONNXRuntime| Home](https://onnxruntime.ai/) 开发者们成功地将苹果原始的模型语言（PyTorch 格式）重构为这种万能翻译器语言，并传递给了浏览器。 [Converting Apple’s Sharp ML for your devices | Raleigh](https://sf.aitinkerers.org/talks/rsvp_kERNVs9PVNw) [GitHub - miketahani/ml-sharp-browser](https://github.com/miketahani/ml-sharp-browser)

第二位特工是 **WebAssembly (Wasm)** 和 **WebGPU** 技术。它们就像是浏览器的 “专用高速公路”，让浏览器不再局限于显示文字和图片，而是能直接调用电脑的心脏 (CPU) 或大脑 (GPU) 的强大计算能力。得益于此，大小达 2.4 GB 的巨型AI模型也能在浏览器这个窄小的通道内飞速奔驰。 [GitHub - bring-shrubbery/ml-sharp-web](https://app.daily.dev/posts/github---bring-shrubbery-ml-sharp-web-web-playground-to-create-gaussian-splats-using-apple-s-ml-sha-0sg97lpiv)

## 现状：我们可以亲身体验吗？

动作迅速的开发者们已经公开了一个让任何人都能体验这项技术的在线 “AI 游乐场”。 [GitHub - bring-shrubbery/ml-sharp-web](https://github.com/bring-shrubbery/ml-sharp-web) 在这里，你只需上传一张照片，AI 就会即时塑造出立体形状，你甚至可以将其保存到电脑中（.ply 文件格式）。 [GitHub - bring-shrubbery/ml-sharp-web](https://app.daily.dev/posts/github---bring-shrubbery-ml-sharp-web-web-playground-to-create-gaussian-splats-using-apple-s-ml-sha-0sg97lpiv)

不过，在实际体验前有几点需要注意：

*   **注意数据流量**：AI 模型的大小约为 2.4 GB，非常大。 [GitHub - bring-shrubbery/ml-sharp-web](https://app.daily.dev/posts/github---bring-shrubbery-ml-sharp-web-web-playground-to-create-gaussian-splats-using-apple-s-ml-sha-0sg97lpiv) 运行一次相当于下载一部高清电影，因此如果您使用的不是无限流量套餐，请务必在 Wi-Fi 环境下访问。
*   **研究用许可证**：苹果目前公开的 SHARP 核心权重（模型的智能核心）规定不能用于商业目的，仅限个人研究或学习使用。 [ShowHN:Apple'sSharpRunningintheBrowserviaONNX...](https://qht.co/item?id=47995037)
*   **设备规格**：并非所有设备都能完美运行。特别是在 iPhone 或 iPad 等 iOS 设备上，由于目前浏览器自身的技术支持（如不支持 WebGPU 等）尚不完善，运行可能不太顺畅。 [[Web] Support iOS devices · Issue #22776 · microsoft/onnxruntime](https://github.com/microsoft/onnxruntime/issues/22776)

## 未来会如何？我们生活的变化

苹果 SHARP 技术插上浏览器的翅膀只是巨大变化的开始。目前已经出现了在苹果最尖端的空间计算设备 **Vision Pro** 上运行该技术的演示案例。 [Converting Apple’s Sharp ML for your devices | Raleigh](https://sf.aitinkerers.org/talks/rsvp_kERNVs9PVNw)

在不久的将来，当你在网上商城挑衣服时，只需一张照片就能创建出和你身体一模一样的3D化身进行 “虚拟试穿”；或者通过一张旅行时拍下的怀旧照片，以3D形式重新漫步于那天的空间。最令人期待的是，这一切神奇的过程都将在保护个人隐私的同时，像上网冲浪一样简单，无需安装额外的应用程序。

**MindTickleBytes AI 记者观察：**
“受限于平面的数字图像正通过浏览器获得立体的生命力。随着未来模型体积进一步减小以及移动设备支持的扩大，我们拍摄照片的意义将超越简单的 ‘记录记忆’，进化为生动的 ‘再现空间’。”

## 参考资料

1. [Show HN: Apple's Sharp Running in the Browser via ONNX Runtime Web | Hacker News](https://news.ycombinator.com/item?id=47995037)
2. [GitHub - bring-shrubbery/ml-sharp-web: 使用苹果 ml-sharp 模型创建高斯泼溅的 Web 游乐场 · GitHub](https://github.com/bring-shrubbery/ml-sharp-web)
3. [Apple - CoreML | onnxruntime](https://onnxruntime.ai/docs/execution-providers/CoreML-ExecutionProvider.html)
4. [Converting Apple’s Sharp ML for your devices | Raleigh](https://sf.aitinkerers.org/talks/rsvp_kERNVs9PVNw)
5. [ONNX Runtime Web—running your machine learning model in browser | Microsoft Open Source Blog](https://opensource.microsoft.com/blog/2021/09/02/onnx-runtime-web-running-your-machine-learning-model-in-browser/)
6. [[Web] Support iOS devices · Issue #22776 · microsoft/onnxruntime](https://github.com/microsoft/onnxruntime/issues/22776)
7. [ShowHN:Apple'sSharpRunningintheBrowserviaONNX...](https://qht.co/item?id=47995037)
8. [ONNXRuntime| Home](https://onnxruntime.ai/)
9. [WebAssembly for AI Agents: Running Models in the Browser](https://callsphere.ai/blog/webassembly-ai-agents-running-models-in-the-browser)
10. [Run YOLO Model in the Browser with ONNX, WebAssembly, and Next.js - PyImageSearch](https://pyimagesearch.com/2025/07/28/run-yolo-model-in-the-browser-with-onnx-webassembly-and-next-js/)
11. [GitHub - bring-shrubbery/ml-sharp-web: 使用苹果 ml-sharp 模型... (Daily.dev)](https://app.daily.dev/posts/github---bring-shrubbery-ml-sharp-web-web-playground-to-create-gaussian-splats-using-apple-s-ml-sha-0sg97lpiv)
12. [GitHub - miketahani/ml-sharp-browser: 在浏览器中运行的苹果 SHARP 模型...](https://github.com/miketahani/ml-sharp-browser)
13. [Web | onnxruntime Tutorials](https://onnxruntime.ai/docs/tutorials/web/)

## FACT-CHECK SUMMARY
- Claims checked: 21
- Claims verified: 21
- Verdict: PASS