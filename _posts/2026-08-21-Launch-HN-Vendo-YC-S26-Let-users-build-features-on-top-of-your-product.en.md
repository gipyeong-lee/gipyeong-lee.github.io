---
layout: post
title: "The right features for your workflow, automatically built by AI?"
description: "Learn about Vendo, an open-source customization layer that solves the persistent B2B SaaS problem of feature request backlogs by enabling users to build their own features."
summary: "Vendo is an open-source customization layer that allows enterprise software users to build and attach their own desired features or apps directly onto a product without needing developer assistance."
tags: [AI, SaaS, B2B, Vendo, Productivity]
image: 2026-08-21-Launch-HN-Vendo-YC-S26-Let-users-build-features-on-top-of-your-product.jpg
image_alt: "An abstract representation of a user configuring features they need directly on top of an existing software interface"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "This marks a significant turning point where control over software shifts from the developer to the user. Vendo will break the rigidity of products, creating a flexible ecosystem that respects individual user workflows."
quiz:
  - question: "What is the core function of Vendo?"
    choices: ["Allows users to directly edit the software's source code", "Enables users to create their own desired features or apps within the product", "Doubles developer productivity"]
    answer: 1
    explanation: "Vendo helps users build custom features or micro-apps directly onto a product to suit their needs without developer assistance."
  - question: "Does using Vendo modify the source code of the existing product?"
    choices: ["Yes, it must be modified", "No, it is implemented in a sandbox without touching the source code", "Only key core features are modified"]
    answer: 1
    explanation: "Vendo does not modify the existing product's source code; it generates a UI that blends naturally with the brand within a sandbox (a protected environment)."
  - question: "How do features created via Vendo work?"
    choices: ["They operate on an independent separate server", "They operate using the user's permissions via the product's API", "All features are forced to update in the cloud"]
    answer: 1
    explanation: "Created features operate directly using the permissions of the currently logged-in user via the product's API and are personalized to the user's workflow."
lang: en
ref: 2026-08-21-Launch-HN-Vendo-YC-S26-Let-users-build-features-on-top-of-your-product
audio: 2026-08-21-Launch-HN-Vendo-YC-S26-Let-users-build-features-on-top-of-your-product.en.mp3
industry: general
---

Imagine this: You’re looking at the software screen you use for work every day and think, "I wish I could just click this button here to email this file to myself." But when you request that feature from the development team, the answer is always, "We'll review it," or, "The feature backlog is too long, so it won't happen this year."

In the end, we were forced to adjust our work habits to fit the features the software provides. It’s like walking around all day in shoes that don't fit. But what if you could create a feature that fits your hand perfectly, right then and there? Vendo, which recently emerged with the support of Silicon Valley’s Y Combinator (YC), aims to solve this very problem.

## Why It Matters

Many people who use B2B SaaS often feel a gap between the "features I need" and the "features the product provides." Every company’s workflow is different, but software only provides "average" features.

Vendo breaks down this "rigidity" in software. Users of companies that adopt this technology can create customized features or small apps (micro-apps) necessary for their work without the help of a developer. [Source: Vendo(YC S26) – Let your users build features on top of your product](https://www.ycombinator.com/companies/vendo). As a result, companies can escape the never-ending pile of feature requests, and users can complete their own personalized workflows. [Source: YC-Backed Vendo Lets Users Build Features on Top of SaaS ...](https://www.founderland.ai/articles/yc-backed-vendo-lets-users-build-features-on-top-of-saas-pro-mrynzgii).

## The Explainer

Let’s use an analogy: If existing software is a "well-made, finished piece of furniture," Vendo is like a "Lego block set" that you can freely attach to that furniture.

Simply put, Vendo is an "embedded agent" (an AI inserted inside a product that performs tasks on behalf of the user). [Source: GitHub - runvendo/vendo: Embedded agents your customers use ...](https://github.com/runvendo/vendo).

1. **Connect**: Vendo safely issues commands through the API (a channel for software to communicate externally) provided by the product, just as an actual user would perform the task. [Source: Vendo: open-source layer that lets users build features on ...](https://zeli.app/en/story/49376038).
2. **Build**: When a user requests a feature, a custom device within the Vendo system writes a React component (a JavaScript library for building user interfaces). At this point, guardrails are applied to prevent mistakes and ensure safe execution. [Source: LaunchHN:Vendo(YC S26) –Letusersbuildfeaturesontopof...](https://news.ycombinator.com/item?id=49376038).
3. **Render**: Features created this way are rendered on the screen as if they were always part of the product, all within a sandbox (a safe, independent, isolated space), without ever touching the original software's code. [Source: GitHub - runvendo/vendo: Embedded agents your customers use ...](https://github.com/runvendo/vendo).

## Where We Stand

Vendo is currently available as open-source (a method where anyone can view and contribute to the code). [Source: Vendo: open-source layer that lets users build features on ...](https://zeli.app/en/story/49376038). It is simple enough for enterprise managers to install into their software in just 60 seconds via the `npm install` command. [Source: Vendo: open-source layer that lets users build features on ...](https://zeli.app/en/story/49376038).

Yousef, co-founder of Vendo, emphasized that AI agents are fundamentally changing the way dashboards and user interfaces are consumed, and "personalization" is at the core of it. [Source: Show HN: Vendo (YC S26) – Let your users add their own ...](https://news.ycombinator.com/item?id=48926618). Many B2B SaaS companies are currently working to escape "backlog hell"—where they struggle to handle individual feature requests from customers—through this solution. [Source: YC-Backed Vendo Lets Users Build Features on Top of SaaS ...](https://www.founderland.ai/articles/yc-backed-vendo-lets-users-build-features-on-top-of-saas-pro-mrynzgii).

## What's Next

In the future, it is highly likely that almost every work tool we use will change from a "finished product" to "ingredients." If tools like Vendo become mainstream, it will become standard for software companies to provide only the core engine, while users add their own workflows on top.

Developers will be able to focus on system stability and core feature development rather than dealing with trivial requirements from individual customers. We are approaching a future where the apps we use lock together like Lego blocks and remember our personal work styles.

## AI Reporter's Perspective from MindTickleBytes

An era has dawned where the user who knows the software best, rather than the person who builds it, defines the features. Vendo is a fresh attempt to return "sovereignty of tools," which had been hidden behind the complexity of technology, to the user. From now on, the process of software evolving to fit my work style—rather than the software asking me to adjust to it—will become natural.

## References

1. [Vendo: Let your users build their own features on top of your ...](https://www.ycombinator.com/companies/vendo)
2. [Vendo — YC S26 Launch on Hacker News - bestofshowhn.com](https://bestofshowhn.com/yc-s26/vendo)
3. [Show HN: Vendo (YC S26) – Let your users add their own ...](https://news.ycombinator.com/item?id=48926618)
4. [GitHub - runvendo/vendo: Embedded agents your customers use ...](https://github.com/runvendo/vendo)
5. [Vendo: open-source layer that lets users build features on ...](https://zeli.app/en/story/49376038)
6. [Introducing Vendo: let your users edit your product - LinkedIn](https://www.linkedin.com/pulse/introducing-vendo-let-your-users-edit-product-ankit-gupta-0uu9c)
7. [Vendo lets users build custom features on top of your product ...](https://www.linkedin.com/posts/y-combinator_vendo-yc-s26-lets-your-users-build-their-activity-7485385624418439168-KuP2)
8. [LaunchHN:Vendo(YC S26) –Letusersbuildfeaturesontopof...](https://news.ycombinator.com/item?id=49376038)
9. [Vendo (YC S26) – Let your users add their lown features to ...](https://aiindigo.com/blog/vendo-yc-s26-let-your-users-add-their-lown-features-to-your-product-deep-dive-te)
10. [YC-Backed Vendo Lets Users Build Features on Top of SaaS ...](https://www.founderland.ai/articles/yc-backed-vendo-lets-users-build-features-on-top-of-saas-pro-mrynzgii)