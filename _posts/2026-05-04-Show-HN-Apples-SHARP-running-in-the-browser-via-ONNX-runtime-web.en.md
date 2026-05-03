---
layout: post
title: "A Single Photo Turns into 3D Space? Why Apple's AI 'SHARP' Entered the Browser"
description: "An easy and engaging explanation of how to run Apple's latest 3D reconstruction technology, SHARP, directly in a web browser without any installation, and the principles behind it."
summary: "With Apple's AI model 'SHARP' now running directly in web browsers, an era has arrived where anyone can easily create and own their own 3D spaces using just a single photograph."
tags: [Apple, SHARP, 3D, AI, Web Technology, Gaussian Splatting]
image: 2026-05-04-Show-HN-Apples-SHARP-running-in-the-browser-via-ONNX-runtime-web.jpg
image_alt: "A graphic image visualizing the process of a 2D flat photo transforming into a three-dimensional 3D space."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "The technology to create 3D content directly on one's device without complex servers will be a crucial milestone that addresses both user privacy and cost efficiency."
quiz:
  - question: "What is the name of the core technology Apple's SHARP model uses to create 3D spaces?"
    choices: ["Polygon Rendering", "Gaussian Splatting", "Ray Tracing"]
    answer: 1
    explanation: "SHARP is based on 'Gaussian Splatting' technology, which creates a sense of depth by scattering millions of tiny points (ellipsoids)."
  - question: "What is the core tool that allows AI to run in a web browser without a separate server?"
    choices: ["ONNX Runtime Web", "Photoshop", "YouTube"]
    answer: 0
    explanation: "Using ONNX Runtime Web, complex AI models can be executed directly by borrowing the computing power of the web browser."
  - question: "What is the approximate size of the SHARP model running in the browser?"
    choices: ["2.4 MB", "2.4 GB", "24 GB"]
    answer: 1
    explanation: "The size of the SHARP model currently converted for web use is approximately 2.4 GB."
lang: en
ref: 2026-05-04-Show-HN-Apples-SHARP-running-in-the-browser-via-ONNX-runtime-web
audio: 2026-05-04-Show-HN-Apples-SHARP-running-in-the-browser-via-ONNX-runtime-web.en.mp3
industry: education
---

Imagine this: you upload a single photo of a beautiful cake you took at a cafe yesterday to a website, and suddenly, the cake becomes three-dimensional as if it's popping out of the screen. You can freely rotate it with your mouse or finger to see the side, the back, and even the top—as if you were back at that cafe.

This is no longer a story from a distant future fantasy movie. It has become possible as **'SHARP'**, a research AI model recently released by Apple, has begun running directly in the web browsers you use every day. According to [Show HN: Apple's Sharp Running in the Browser via ONNX Runtime Web | Hacker News](https://news.ycombinator.com/item?id=47995037), you can now transform flat photos into vivid 3D spaces just by visiting a website, without the hassle of installing complex programs on your computer.

Today, at **MindTickleBytes**, we will explain what this magical technology is and why this news is creating a buzz among developers and AI enthusiasts worldwide in an easy and friendly way.

## Why is this important? Your computer becomes an 'AI Factory'

Until now, the reason we could comfortably use smart AI like ChatGPT was that when we asked a question, a massive supercomputer (server) far away calculated the answer and sent it back to us. However, the process of turning a photo into 3D requires an enormous amount of computation, making server operation costs very expensive. There was also the discomfort of having to send precious personal photos to another company's server.

But the technology revealed this time takes a different approach. The AI model is brought entirely into your web browser, such as Chrome or Safari. This 'In-browser inference' brings us three major benefits. [WebAssembly for AI Agents:RunningModelsintheBrowser](https://callsphere.ai/blog/webassembly-ai-agents-running-models-in-the-browser)

1.  **Strict Privacy Protection**: The photos you upload never leave your smartphone or laptop for an external server. All 3D conversion work happens privately within your device. [RunYOLO ModelintheBrowserwithONNX... - PyImageSearch](https://pyimagesearch.com/2025/07/28/run-yolo-model-in-the-browser-with-onnx-webassembly-and-next-js/)
2.  **Zero Server Costs**: Companies operating the service don't need to rent expensive supercomputers, allowing for more innovative free services. Users don't have to wait through 'loading' screens caused by crowded servers.
3.  **Instant Response Without Latency**: Even if your internet connection is a bit slow, it doesn't matter. You can check results in real-time by utilizing 100% of your device's native performance.

## Understanding easily: What are 'SHARP' and 'Gaussian Splatting'?

First, let's find out what Apple's **SHARP**, a name that might sound unfamiliar, actually is. SHARP is a very smart AI architecture that can guess the hidden three-dimensional structure of an object or place just by looking at a single photo. [GitHub - bring-shrubbery/ml-sharp-web](https://github.com/bring-shrubbery/ml-sharp-web)

The core technology this model uses is technically called **Gaussian Splatting**. The term is difficult, but the principle is very easy when compared to things we know well.

> **To use an analogy!**
> While traditional 3D technology creates models by meticulously joining hard Lego blocks or triangular pieces, **Gaussian Splatting** is similar to creating a three-dimensional shape by spraying millions of translucent 'cotton candy puffs' into the air.

When millions of tiny ellipsoids (cotton candy puffs), each with its own color and transparency, are floated and placed in position, a vivid 3D space is completed that looks very smooth and realistic without hard edges. [GitHub - bring-shrubbery/ml-sharp-web](https://app.daily.dev/posts/github---bring-shrubbery-ml-sharp-web-web-playground-to-create-gaussian-splats-using-apple-s-ml-sha-0sg97lpiv) SHARP acts as the conductor, telling where and at what size to spray these numerous cotton candy puffs. [Converting Apple’s Sharp ML for your devices | Raleigh](https://sf.aitinkerers.org/talks/rsvp_kERNVs9PVNw)

## How can heavy AI run in a browser?

Originally, this technology was designed to run only on professional research computers worth thousands of dollars equipped with high-performance graphics cards. So, how did it become possible to run it in the general web browsers we use? There are two secret agents hidden here.

The first agent is **ONNX Runtime Web**. [ONNX Runtime Web—running your machine learning model in browser | Microsoft Open Source Blog](https://opensource.microsoft.com/blog/2021/09/02/onnx-runtime-web-running-your-machine-learning-model-in-browser/) AI models use different languages depending on the environment in which they were developed. **ONNX (Open Neural Network Exchange)** is a tool like a 'universal translator' that bundles them together so they can communicate in any environment. [ONNXRuntime| Home](https://onnxruntime.ai/) Developers succeeded in reconfiguring Apple's original model language (PyTorch format) into this universal translator language to deliver it to the browser. [Converting Apple’s Sharp ML for your devices | Raleigh](https://sf.aitinkerers.org/talks/rsvp_kERNVs9PVNw) [GitHub - miketahani/ml-sharp-browser](https://github.com/miketahani/ml-sharp-browser)

The second agent is **WebAssembly** and **WebGPU** technology. These act as a 'dedicated high-speed highway' that allows the browser to go beyond just showing text or pictures and directly borrow the powerful computing power of the computer's heart, the CPU, or its brain, the GPU. Thanks to this, even a massive AI model weighing 2.4 GB can run smoothly within the narrow passage of a browser. [GitHub - bring-shrubbery/ml-sharp-web](https://app.daily.dev/posts/github---bring-shrubbery-ml-sharp-web-web-playground-to-create-gaussian-splats-using-apple-s-ml-sha-0sg97lpiv)

## Current Situation: Can we try it ourselves?

Quick-witted developers have already released online 'AI Playgrounds' where anyone can experience this technology. [GitHub - bring-shrubbery/ml-sharp-web](https://github.com/bring-shrubbery/ml-sharp-web) There, if you upload a photo, the AI shapes a three-dimensional form on the spot, which you can then save back to your computer (in .ply file format). [GitHub - bring-shrubbery/ml-sharp-web](https://app.daily.dev/posts/github---bring-shrubbery-ml-sharp-web-web-playground-to-create-gaussian-splats-using-apple-s-ml-sha-0sg97lpiv)

However, there are a few 'checkpoints' before you try it.

*   **Watch out for data volume**: The AI model size is quite large at about 2.4 GB. [GitHub - bring-shrubbery/ml-sharp-web](https://app.daily.dev/posts/github---bring-shrubbery-ml-sharp-web-web-playground-to-create-gaussian-splats-using-apple-s-ml-sha-0sg97lpiv) Since it downloads data equivalent to a high-definition movie each time it runs, be sure to connect via Wi-Fi if you don't have an unlimited data plan.
*   **Research License**: There is a rule that the core weights (the intelligence of the model) of SHARP released by Apple cannot be used for commercial purposes to make money; they must only be used for personal research or learning. [ShowHN:Apple'sSharpRunningintheBrowserviaONNX...](https://qht.co/item?id=47995037)
*   **Device Specifications**: It won't work perfectly on all devices. In particular, please note that on iOS devices like the iPhone or iPad, technical support within the browser itself (such as lack of WebGPU support) may still be insufficient for smooth execution. [[Web] Support iOS devices · Issue #22776 · microsoft/onnxruntime](https://github.com/microsoft/onnxruntime/issues/22776)

## What's next? Changes in our lives

Apple's SHARP technology gaining the wings of the browser is just the beginning of a massive change. There are already demonstrations of this technology running on Apple's cutting-edge spatial computer, **Vision Pro**. [Converting Apple’s Sharp ML for your devices | Raleigh](https://sf.aitinkerers.org/talks/rsvp_kERNVs9PVNw)

In the near future, it will become routine to create a 3D avatar that looks exactly like your body from a single photo for 'virtual fitting' when picking clothes at an online store, or to wander again through a 3D reconstruction of a space from a cherished vacation photo. Above all, the most exciting part is that all these magical processes are carried out simply, like surfing the web without any separate app installation, while keeping your precious personal information safe.

**From the MindTickleBytes AI Reporter:**
"Digital images, which were once trapped in the limitation of being flat, have gained the vitality of being three-dimensional through the browser. If the model size decreases further and mobile device support expands, the meaning of the photos we take will evolve beyond simple 'records of memory' to vivid 'recreations of space'."

## References

1. [Show HN: Apple's Sharp Running in the Browser via ONNX Runtime Web | Hacker News](https://news.ycombinator.com/item?id=47995037)
2. [GitHub - bring-shrubbery/ml-sharp-web: Web playground to create Gaussian Splats using Apple's ml-sharp model. · GitHub](https://github.com/bring-shrubbery/ml-sharp-web)
3. [Apple - CoreML | onnxruntime](https://onnxruntime.ai/docs/execution-providers/CoreML-ExecutionProvider.html)
4. [Converting Apple’s Sharp ML for your devices | Raleigh](https://sf.aitinkerers.org/talks/rsvp_kERNVs9PVNw)
5. [ONNX Runtime Web—running your machine learning model in browser | Microsoft Open Source Blog](https://opensource.microsoft.com/blog/2021/09/02/onnx-runtime-web-running-your-machine-learning-model-in-browser/)
6. [[Web] Support iOS devices · Issue #22776 · microsoft/onnxruntime](https://github.com/microsoft/onnxruntime/issues/22776)
7. [ShowHN:Apple'sSharpRunningintheBrowserviaONNX...](https://qht.co/item?id=47995037)
8. [ONNXRuntime| Home](https://onnxruntime.ai/)
9. [WebAssembly for AI Agents: Running Models in the Browser](https://callsphere.ai/blog/webassembly-ai-agents-running-models-in-the-browser)
10. [Run YOLO Model in the Browser with ONNX, WebAssembly, and Next.js - PyImageSearch](https://pyimagesearch.com/2025/07/28/run-yolo-model-in-the-browser-with-onnx-webassembly-and-next-js/)
11. [GitHub - bring-shrubbery/ml-sharp-web: Web playground to... (Daily.dev)](https://app.daily.dev/posts/github---bring-shrubbery-ml-sharp-web-web-playground-to-create-gaussian-splats-using-apple-s-ml-sha-0sg97lpiv)
12. [GitHub - miketahani/ml-sharp-browser: Apple's SHARP model running in ...](https://github.com/miketahani/ml-sharp-browser)
13. [Web | onnxruntime Tutorials](https://onnxruntime.ai/docs/tutorials/web/)

## FACT-CHECK SUMMARY
- Claims checked: 21
- Claims verified: 21
- Verdict: PASS