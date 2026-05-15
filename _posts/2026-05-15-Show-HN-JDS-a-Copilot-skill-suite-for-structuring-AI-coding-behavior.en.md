---
layout: post
title: "How to Command AI to 'Plan Before Coding!': The Rise of JDS Skills"
description: "Discover JDS, a new tool that forces AI coding assistants to design and test first like humans, instead of blindly writing code."
summary: "JDS is a GitHub Copilot tool that forces AI to design first and pass tests before writing code, making it work like a professional developer."
tags: [AI, Coding, GitHub Copilot, JDS, AI Skills]
image: 2026-05-15-Show-HN-JDS-a-Copilot-skill-suite-for-structuring-AI-coding-behavior.jpg
image_alt: "A robot carefully examining architectural blueprints"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "An excellent example showing that even with outstanding AI capabilities, it is ultimately the 'rules' that control and guide those capabilities in the right direction that determine quality."
quiz:
  - question: "What is the first step JDS requires from an AI coding assistant?"
    choices: ["Writing code", "Design", "Running tests"]
    answer: 1
    explanation: "JDS forces the AI to design first before writing any code."
  - question: "What do you call a reusable package of instructions that teaches an AI how to perform a specific task?"
    choices: ["Plugin", "Skill", "Token"]
    answer: 1
    explanation: "A package of instructions and resources that helps effectively handle specific tasks or workflows is called a 'skill'."
  - question: "What command allows you to easily install and manage these AI skills like software apps?"
    choices: ["gh skill", "jds run", "ai install"]
    answer: 0
    explanation: "The 'gh skill' command allows you to install and manage AI agent skills like a package manager."
lang: en
ref: 2026-05-15-Show-HN-JDS-a-Copilot-skill-suite-for-structuring-AI-coding-behavior
audio: 2026-05-15-Show-HN-JDS-a-Copilot-skill-suite-for-structuring-AI-coding-behavior.en.mp3
industry: healthcare
---

Imagine this. To build the cozy and beautiful country house of your lifelong dreams, you hire an architect renowned for being the fastest in the industry. Filled with anticipation, you state your requirements: "Please build a two-story house with large windows and plenty of sunlight." But what if, as soon as you finish speaking, the architect rushes outside, haphazardly pours cement in the middle of the yard, and starts randomly stacking bricks?

There is no blueprint showing the overall structure of the house, nor a safety inspection plan to check if the ground is solid. They don't even ask about the placement of room doors or plumbing connections. No matter how fast and skilled they are, you would probably stop the architect immediately and shout, "Please, make a plan before you start!" A house built without a plan will eventually leak and crack, perhaps forcing you to tear the whole thing down and rebuild it later.

Unfortunately, this is exactly what the smart AI coding assistants we've been eagerly using have typically looked like. When a developer throws a question or requirement at tools like ChatGPT or GitHub Copilot, the AI is busy instantly churning out code (a collection of commands that serves as a computer program's blueprint) without a second of hesitation. People initially cheered at the incredible speed, but gradually realized how large and terrifying the errors caused by code patched together on the fly, ignoring the overall software structure, could become later on.

The exciting news currently heating up the global developer community is the emergence of an amazing tool that teaches this "hasty and overeager AI" the calmness and rigorous workflow of a true human expert. The tool is called JDS. Instead of letting the AI blindly start typing, this tool fundamentally corrects its behavior, forcing it to undergo thorough planning and verification processes. It's like teaching the "sequence," "system," and "responsibility" of work to a new employee who has abundant knowledge but lacks field experience and is prone to causing accidents. How will this new technology change our digital daily lives and the way we build complex software? Let's take a closer look with MindTickleBytes.

## Why It Matters

In recent years, as the era of AI writing code for us has blossomed, not only the tech industry but also the general public has been greatly enthusiastic about the pace of its development. It felt like anyone could instantly create complex smartphone apps or flashy websites just by asking. However, industry professionals soon ran into a very realistic and heavy problem. While the code written by AI in the blink of an eye looked quite plausible in fragments, it was mostly created without any consideration for the overall system structure or harmony with other software components.

In software engineering, this phenomenon is commonly referred to as 'Technical Debt'. Code written hastily to quickly solve an immediate problem might seem to work fine for now, but like taking out a high-interest loan, it forces you to pay a massive interest in time and cost later when adding new features or fixing errors. AI coding assistants have essentially been mass-producing a vast amount of 'technical debt' at an incredible speed.

The reason this problem is important even to the general public, not just IT experts, is clear. Almost all the infrastructure supporting our lives today runs on 'code'. The smartphone messenger apps you use every day, the internet banking systems for transferring money, the autonomous driving features of cars responsible for your family's safety, and even hospital medical record systems are all meticulously written software.

What happens if we leave AI coding assistants alone to blindly patch code together, completely ignoring systematic processes? Ultimately, the overall quality and safety of the digital services we rely on daily will significantly degrade. This could lead to terrible incidents, such as unexplained transfer errors in banking apps or autonomous vehicles misjudging situations at complex intersections. Messy code written by AI is bound to become so tangled that human developers later won't even know where to start fixing it.

Against this backdrop, the emergence of behavior control tools like JDS represents a very significant turning point and holds profound meaning. When working in environments like GitHub Copilot (an AI-based assistant program used by millions of developers worldwide to help write code), JDS forces AI coding assistants to identically follow the strict development processes that actual software development experts follow in the field [GitHub - josipmusa/jds:JDSskillsuiteforagenticcodingtools...](https://github.com/josipmusa/jds).

This means humanity has finally begun to acquire the control to move beyond simply using AI to write code "fast," to safely building "proper" software—error-free and easy to maintain—through human-AI collaboration. As developers spend less time cleaning up AI's mistakes, far more creative and innovative services can reach us much faster. Code built through a rigorous verification process will dramatically reduce the annoying daily inconveniences of smartphone apps suddenly crashing or computer systems freezing. In other words, JDS is a crucial safety mechanism that helps keep our daily lives much more solid and secure atop the invisible digital realm.

## The Explainer

So, by what mechanism does JDS tame this unpredictable AI? To clearly understand how it works, we must first look at a core concept currently considered paramount in the AI industry: 'Skills'.

From a technical perspective, a Copilot skill essentially refers to a small, reusable bundle of instructions, scripts, and supporting resources that teaches an AI assistant how to handle a specific task or workflow more effectively [Creating a GitHubCopilotSkillfor Dataverse Solution Import/Export...](https://www.linkedin.com/pulse/creating-github-copilot-skill-dataverse-solution-alm-shashank-bhide-0r0pc). Developers can leverage these skills to customize the AI's behavioral patterns and problem-solving abilities for specific tasks, guiding a general-purpose AI to perform much more specialized and difficult work than usual [Creating agent skills for GitHub Copilot - GitHub Enterprise Cloud Docs](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/use-copilot-agents/cloud-agent/create-skills) [GitHub Copilot documentation - GitHub Docs](https://docs.github.com/en/copilot).

The term might feel a bit unfamiliar and difficult. Let's simplify it with an analogy. Imagine our AI Copilot is a "genius chef" who has perfect knowledge of every ingredient in the world and tens of thousands of recipes in their head, but hasn't spent a single day actually working in a kitchen. This chef can whip up anything in an instant, but has no idea what order to serve an authentic French haute cuisine course to a guest, what the strict hygiene rules of a restaurant kitchen are, or how to separate cooking utensils for a customer with allergies.

At this point, we hand this chef a special work manual called a 'skill'. We're essentially instructing them: "Your vast knowledge is wonderful, but in this restaurant's kitchen today, you must cook strictly according to the procedures and hygiene rules written in this manual!" By doing so, the genius chef won't waste their knowledge in the wrong places and can produce the best results within a set, excellent system.

The JDS we are talking about today is precisely a collection of these powerful behavior-correcting skills (a skill suite). JDS is provided as an extension that operates in the command-line interface developers commonly use, and it forces AI coding tools to unconditionally follow a systematic and professional workflow, moving beyond simply spitting out code as if answering a question [GitHub - josipmusa/jds:JDSskillsuiteforagenticcodingtools...](https://github.com/josipmusa/jds).

In particular, the three core rules JDS forces the AI to strictly adhere to penetrate the very essence of software development. These rules are akin to forcefully injecting into AI the precious wisdom human developers have gained through decades of painful failures and frequent all-nighters.

1. **Design before code:** "Before you start writing code right now, explain in detail the blueprint for how you will build this program overall."
   Instinctively, AI tries to complete sentences by quickly predicting the next word to follow the input context. As a result, it misses the forest for the trees. However, this rule forces the AI to take a step back, think deeply, and clearly map out the overall structure before building anything.
2. **Tests before implementation:** "Before creating code that actually functions, first write the grading criteria (test code) that will automatically verify if this feature works correctly later."
   This is an excellent methodology in software engineering called 'Test-Driven Development (TDD)'. To use an analogy, it's like showing a student the exam questions before blindly making them study. It ensures they write code with perfect knowledge of the passing criteria for what they need to build.
3. **Evidence before completion claims:** "Do not hastily declare that the work is done. Show me concrete evidence (execution results or log records) right in front of my eyes that the code you wrote actually runs perfectly without errors." [GitHub - josipmusa/jds:JDSskillsuiteforagenticcodingtools...](https://github.com/josipmusa/jds)
   As many of you have experienced, AI often makes very plausible lies (hallucinations) claiming that what it wrote is perfect. In programming, this lie is fatal. This rule in JDS systematically prevents the AI from concluding its task on its own without solid evidence.

Imagine this. A developer instructs their AI assistant, "Build a shopping cart feature for our company's new online store."

AI in the past would have tossed out complex code in a second and shouted, "Coding is complete!" All without even checking if that code conflicted with the payment system or caused the server to crash. The developer would end up wasting more time verifying if the code was correct than they would have spent writing it themselves.

However, the reaction of an AI equipped with JDS skills is entirely different. Instead of abruptly starting to type, this AI carefully analyzes the request and says:
"The feature you requested will need functions to add, remove, and adjust the quantity of items. I will set up the overall design to store customer data in this structure in Area A of the database. Do you agree with my design?"

Once the human developer approves this excellent blueprint, it moves on to the second step. It reports, "I have first written the 'test grading criteria' for the machine to automatically verify if the total amount is calculated accurately."

Only then does it very carefully write the actual functioning code, and finally states confidently: "I ran the code I just wrote through the strict tests we created earlier dozens of times, and it passed without a single error. Here is the evidence screen. Now, all tasks are truly complete."

It has perfectly transformed from a frustrating intern who just types incredibly fast into a true professional lead engineer you can trust with core tasks!

## Where We Stand

Hearing how these innovative tools work might raise the question: "Wouldn't I have to go through an incredibly difficult setup process to introduce such a complex and excellent system to my computer?" So, how are developers in the actual industry field utilizing these smart tools right now?

Surprisingly, the answer is "It's very easy." An amazing ecosystem is already rapidly taking shape where we can easily download and manage these useful 'skills' with just a few screen clicks or a single line of command, much like using the Google Play Store or Apple App Store on our smartphones.

The most representative example is the newly emerged dedicated command called `gh skill`. This system has boldly introduced a so-called "package manager" approach to the numerous useful AI agent skills we explored earlier [gh skill: GitHub CLI Agent Skills Management for Copilot, Claude Code, and Cursor | Big Hat Group Inc.](https://www.bighatgroup.com/blog/gh-skill-github-cli-agent-skills-management/). Simply put, it is a dedicated assistant system that plays the exact same role as a smartphone app market.

Just as we search for and install necessary apps on our smartphones and update them when new versions come out, developers can easily install excellent skills on their computers that grant new behavioral rules and capabilities to the AI with just a few simple keystrokes in the command window.

Furthermore, to prevent problems caused by an AI's behavior suddenly changing one day, it allows you to securely lock in a specific version of a skill to ensure operational stability, and it even perfectly supports a preview feature to lightly test if it performs the desired task well [gh skill: GitHub CLI Agent Skills Management for Copilot, Claude Code, and Cursor | Big Hat Group Inc.](https://www.bighatgroup.com/blog/gh-skill-github-cli-agent-skills-management/).

There is a clear truth that this dazzling development quietly whispers to us: AI is no longer a "magic box" whose inner workings are unknown and whose behavior is hard to predict. Instead, we can now freely assemble elements like toy Lego blocks—easily installing JDS skills that grant rigorous verification capabilities aligned with human purposes, or security skills that prevent the leakage of confidential corporate data. The era of the "true customized assistant" has dawned, where we control the AI to move precisely in the direction we want within a safe orbit set by humans.

## What's Next

The implications of this decisive wave of change, starting in the specialized field of software development, for our society as a whole are greater than imaginable. The AI of the future we will face will rapidly evolve from merely a "parrot that pretends to know everything but often spouts irrelevant nonsense" to a "reliable expert who adheres to strict procedures and takes responsibility for its work results."

We often dream of a rosy future where AI makes difficult judgments on its own and perfectly handles complex tasks without human supervision. However, for that future to arrive safely, mechanisms that can securely control its mighty capabilities according to human intentions are just as essential as the AI's overwhelming intellectual power. It is exactly the same logic that no matter how excellent a state-of-the-art airliner's autopilot is, it must not fly however it pleases, ignoring the route set by the pilot and the strict safety checklist.

What happens if systems like JDS, which strongly demand that AI report a work plan to humans before taking action and prove its final results with clear evidence, become universally commonplace across society, beyond the coding field? We will finally be able to safely and confidently entrust AI with far more important and sensitive tasks for humanity.

Shall we imagine a slightly more distant future together? Going forward, this change will happen not just in the realm of writing code, but in various fields closely connected to our lives. AI lawyers analyzing hundreds of thousands of pages of case law to draft crucial legal documents, AI doctors diagnosing cancer by synthesizing a patient's genetic data and medical records, AI accountants compiling financial reports worth tens of billions—they will be active in countless fields where logic, accuracy, and meticulous procedures are lifeblood.

And across all these fields, specialized professional skills will pour out, strongly controlling "behavioral procedures" and "thought processes" to prevent AI from jumping to conclusions. The massive innovation of AI moving beyond a neat tool that saves us typing time to becoming a true colleague we can trust and rely on in the fierce industrial field is beginning right before our eyes.

## AI's Take

MindTickleBytes AI Reporter's View: Ironically, in this era of AI absorbing near-infinite intelligence and all the knowledge in the world, what we truly needed most urgently was not the AI's "processing speed" or "amount of knowledge." It was human "discipline and process" to guide that immense capability in the right direction and prevent unexpected catastrophes. Through numerous trials and errors, we have already learned that losing our direction by being blinded by speed ultimately exacts a greater cost.

The emergence of tools like JDS that correct AI behavior and strongly control workflows will serve as a crucial catalyst for AI technology to completely move past the stage of a novelty toy that briefly satisfies public curiosity. Furthermore, it marks a decisive turning point where it takes deep, firm root in the practical industrial infrastructure that supports our society, based on the solid trust of humans. The future AI revolution will move beyond simply how much smarter a model we can build, to become a battle of how to safely and systematically tame that intelligence.

## References
1. [GitHub - josipmusa/jds:JDSskillsuiteforagenticcodingtools...](https://github.com/josipmusa/jds)
2. [Creating a GitHubCopilotSkillfor Dataverse Solution Import/Export...](https://www.linkedin.com/pulse/creating-github-copilot-skill-dataverse-solution-alm-shashank-bhide-0r0pc)
3. [Creating agent skills for GitHub Copilot - GitHub Enterprise Cloud Docs](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/use-copilot-agents/cloud-agent/create-skills)
4. [GitHub Copilot documentation - GitHub Docs](https://docs.github.com/en/copilot)
5. [gh skill: GitHub CLI Agent Skills Management for Copilot, Claude Code, and Cursor | Big Hat Group Inc.](https://www.bighatgroup.com/blog/gh-skill-github-cli-agent-skills-management/)