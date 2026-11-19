---
layout: post
title: "3D Graphics with Just AI and JSON? The Story of Zpup, a Modern Revival of the Long-Dormant Zdog"
description: "Discover how Zpup brings 3D graphics to the web and READMEs using only JSON data without JavaScript, and explore the evolution of Zdog."
summary: "Zpup converts JSON into flat SVG without JavaScript, serving as a modern 3D engine overcoming the limitations of the abandoned Zdog."
tags: [Zpup, Zdog, 3DGraphics, SVG, JSON, OpenSource]
image: 2026-11-19-Show-HN-Zpup-Zdog-style-3D-scenes-in-JSON-SVG-from-any-angle.jpg
image_alt: "A clean illustration showing JSON code on a computer screen and the converted 3D SVG graphic"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "It's appealing to be able to lightly implement 3D in static environments without complex 3D engines."
quiz:
  - question: "Which technology does Zpup NOT use for its rendering output?"
    choices: ["SVG", "JSON", "JavaScript"]
    answer: 2
    explanation: "Zpup does not use JavaScript in its output files, allowing it to work within img tags and READMEs."
  - question: "What is a key feature improved by Zpup compared to the original Zdog engine?"
    choices: ["Canvas rendering speed", "Shape sorting (overlapping handling)", "Text shape support"]
    answer: 1
    explanation: "Zdog sorted shapes using a single point, causing small objects to be hidden incorrectly, whereas Zpup solves this by comparing overlapping shapes."
  - question: "What tool was used when developing the Zpup project?"
    choices: ["Claude Code Fable 5.2", "React Native", "Three.js"]
    answer: 0
    explanation: "The Zpup developer created this project using Claude Code Fable 5.2."
lang: en
ref: 2026-11-19-Show-HN-Zpup-Zdog-style-3D-scenes-in-JSON-SVG-from-any-angle
audio: 2026-11-19-Show-HN-Zpup-Zdog-style-3D-scenes-in-JSON-SVG-from-any-angle.en.mp3
industry: creative
---

Imagine you are writing a blog post or a GitHub project documentation (README) file. You want to include cool 3D stereoscopic graphics, but if you have to stuff lots of complex JavaScript (a programming language that runs in web browsers) code or load heavy 3D programs, it can give you a headache. How nice would it be if 3D graphics appeared instantly just by dropping in a single standard image tag?

Recently, an interesting project appeared on the developer community Hacker News that completely solves this thirst. It is an open-source project named [Show HN: Zpup – Zdog style 3D scenes in JSON, SVG from any angle](https://github.com/rxolve/zpup) [Source 1]. Today, let's explore Zpup, a lightweight 3D world created using only JSON (JavaScript Object Notation, a lightweight text-based format for storing and exchanging data) data without complex JavaScript.

---

## Why Does This Matter?

To put 3D graphics on a website or document, you usually need massive, complex 3D engines or numerous JavaScript libraries. However, this makes documents heavy and often prevents them from running at all in static (fixed states without dynamic processing) document environments.

Zpup shatters these limitations. Zpup takes a JSON file defining a 3D scene and converts it into a flat SVG (Scalable Vector Graphics, a resolution-independent vector-based image format) file viewable from any camera angle [Source 1, Source 9].

The most surprising thing here is that **the output file contains zero JavaScript** [Source 1, Source 9]. Put simply, like an image printed in a book, because there is no JavaScript, 3D graphics can be rendered as if they are alive and moving even inside regular image tags (`<img>`) or GitHub README documents [Source 1, Source 9]. Developers can now easily add 3D visual elements to documents or static web pages without complex configurations [Source 9].

---

## Understanding Simply: The Legacy of Zdog and the Evolution of Zpup

To help understand, let's use an analogy. Using a very sophisticated and flashy 3D game engine is like shooting a short-form video for smartphones on a massive movie set equipped with all sorts of special equipment. It's too heavy and complex. On the other hand, 'Zdog', an engine loved in the past, was a lightweight and intuitive tool like a paper puppet theater set.

### The Birth and Limitations of Zdog
Originally, Zdog was created by a developer named Dave [Source 11]. He felt that most existing 3D engines were too powerful and complex [Source 11], and wanted a tool to design and display simple 3D models without complex overhead (extra resources consumed by program processing) [Source 11]. Zdog was directly inspired by *Dogz*, a virtual pet game launched in 1995 by P.F. Magic [Source 11, Source 12]. This game rendered models using flat 2D circular sprites (2D graphic elements) within 3D scenes [Source 11, Source 12].

However, Zdog had its drawbacks. It had been left abandoned for years without new versions being released [Source 1, Source 9, Source 10]. Furthermore, Zdog used a method of sorting each shape based on a single point [Source 1]. Because of this, when a small object was placed on a large floor and the camera was rotated, a visual error occurred where the small object incorrectly hid behind the large floor [Source 1].

### How Zpup Solved the Problem
Zpup emerged claiming to be a modern successor to the abandoned Zdog [Source 1, Source 9, Source 10]. The developer needed 3D for a small project at work and was deeply impressed by Zdog, but since it hadn't been updated for a long time, decided to build a modern version themselves [Source 1]. Currently, Zpup is at version 0.2, built lightweight without a canvas renderer or text shapes [Source 1]. Notably, Claude Code Fable 5.2 was used during the development process [Source 1].

To use an analogy, if Zdog roughly looked at just a single point when sorting objects and assigned order, Zpup **meticulously compares the regions of mutually overlapping shapes** to accurately determine which is in front and which is in back [Source 1]. Thanks to this, when rotating the screen, the issue of objects mixing up or being hidden behind each other was cleanly resolved [Source 1].

---

## Current Status: How Far Has It Come?

Zpup is currently developed as version 0.2 [Source 1], and developers can directly experience its features and share feedback via the GitHub repository, example code [Source 10], and the online playground ([https://rxolve.github.io/zpup](https://rxolve.github.io/zpup)) [Source 1].

What this technology can currently do is clear:
- Reads lightweight 3D scene data defined in JSON format [Source 1, Source 9].
- Converts it into a view from any camera angle desired by the user [Source 1, Source 9].
- Outputs clean, flat SVG results containing zero JavaScript [Source 1, Source 9].
- Allows immediate insertion into standard image tags or document files (such as READMEs) [Source 1, Source 9].

On the other hand, heavy features like canvas renderers or text shapes are intentionally excluded, making it optimized for embedding lightweight icons, shapes, and illustrations into static documents rather than building massive, complex 3D games [Source 1].

---

## Where Is It Heading?

In web documentation and open-source ecosystems, 'lightweight' and 'simplicity' equal competitiveness. If 3D stereoscopic graphics can be flexibly rendered inside static image tags without going through heavy JavaScript runtime environments, the expressiveness of technical documentation and portfolio sites will be further enriched.

Carrying on the sensibility of Zdog, which had been paused for years [Source 1, Source 9, Source 10], Zpup—newly reborn in the AI era with modern tools [Source 1]—is well worth watching to see what visual changes it brings to personal projects and developer documentation moving forward.

---

## MindTickleBytes' AI Reporter Perspective

The more complex a technology is, the more often the path to popularization opens only when it returns to its most primitive and lightweight form. Zpup stepped out of the shadow of massive 3D engines and accurately pinned down a small but practical developer pain point: "Can't we put 3D into documents more easily and lightly?" Expectations are gathering on how widely the idea of JavaScript-free 3D SVG will spread across various web environments in the future.

---

## References

1. [Show HN: Zpup – Zdog style 3D scenes in JSON, SVG from any angle](https://github.com/rxolve/zpup)
2. [Zpup – Zdog-style 3D scenes in JSON rendered to SVG from any ...](https://kblip.com/products/zpup-zdog-style-3d-scenes-in-json-rendered-to-svg-from-any-IMbS3Cy)
3. [zpup/examples at main · rxolve/zpup · GitHub](https://github.com/rxolve/zpup/tree/main/examples)
4. [GitHub - metafizzy/zdog: Flat, round, designer-friendly ...](https://github.com/metafizzy/zdog)
5. [GitHub - IgorOffline/metafizzy-zdog: Flat, round, designer ...](https://github.com/IgorOffline/metafizzy-zdog)