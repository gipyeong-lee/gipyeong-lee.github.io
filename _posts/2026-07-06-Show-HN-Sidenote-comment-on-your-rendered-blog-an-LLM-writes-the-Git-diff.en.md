---
layout: post
title: "Comments on my blog like Google Docs? 'Sidenote', the tool where AI writes the code changes for you"
description: "Learn about Sidenote, a tool that lets users easily suggest edits to developer blogs or documentation like Google Docs, with AI automatically generating the Git diffs."
summary: "Sidenote is an innovative collaboration tool that lets readers comment on blog posts, which an AI then analyzes and automatically converts into Git code changes."
tags: [AI, Blog, Git, Collaboration, Productivity]
image: 2026-07-06-Show-HN-Sidenote-comment-on-your-rendered-blog-an-LLM-writes-the-Git-diff.jpg
image_alt: "An image depicting a Google Docs-style comment box floating over a blog post screen, with an AI writing code changes."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "A great example of an 'intent-driven' workflow where AI handles the technical execution based on the document's intent, without requiring complex coding knowledge."
quiz:
  - question: "What is the primary user experience of Sidenote most similar to?"
    choices: ["Sending an email", "Reviewing a document in Google Docs", "Compiling code in a terminal"]
    answer: 1
    explanation: "Sidenote provides an environment where you can select passages and leave comments directly on a rendered Markdown site, much like Google Docs."
  - question: "What task does the AI agent perform after a user leaves a comment in Sidenote?"
    choices: ["Automatically publishing to the blog", "Writing a Git diff (code changes)", "Replying to the comment"]
    answer: 1
    explanation: "Based on the content of the user's comment, an AI agent (such as Claude or Codex) generates a clean Git diff to resolve the code change."
  - question: "Which statement about Sidenote's execution environment is correct?"
    choices: ["A separate server installation is required", "It is a local-first, browser-based tool", "It is only available as a mobile app"]
    answer: 1
    explanation: "Sidenote is a local-first application that runs directly in the browser."
lang: en
ref: 2026-07-06-Show-HN-Sidenote-comment-on-your-rendered-blog-an-LLM-writes-the-Git-diff
audio: 2026-07-06-Show-HN-Sidenote-comment-on-your-rendered-blog-an-LLM-writes-the-Git-diff.en.mp3
industry: creative
---

Imagine this: someone is reading your carefully crafted blog or technical documentation, and they think, "The wording here is a bit awkward, what if we changed it to this?" They leave a suggestion just as easily as they would in a Google Doc. But the surprising part? The artificial intelligence (AI) reading that comment doesn't just reply—it perfectly writes out the "Git diff" (a technical method for showing only the specific changes made to the code) so that you can directly apply the fix to your blog's source code.

A tool has arrived that makes this magical experience possible. It is called 'Sidenote'.

### Why does this matter?

Document collaboration is always a difficult task for developers and technical bloggers. Usually, if someone wants to suggest a typo or phrasing fix, they have to access the repository where the blog's source code is stored (an online space where code is kept) and submit a "Pull Request" (a request to incorporate code changes). For an average reader without technical knowledge, this process is an incredibly high and complex barrier.

Sidenote breaks down this barrier. [Sidenote](https://github.com/bharadwaj-pendyala/sidenote) allows anyone without technical expertise to review and suggest edits as naturally as they would using [Google Docs](https://github.com/bharadwaj-pendyala/sidenote). In other words, it has successfully captured both "productivity" and "lowering the barrier to collaboration."

### Easy to understand: How Sidenote works

Shall we use an analogy to understand how Sidenote does this? Think of your blog post as a "completed meal."

1. **Reading (Rendering):** The reader comfortably reads the blog screen, like eating a finished dish at a table. [Source: GitHub - bharadwaj-pendyala/sidenote](https://github.com/bharadwaj-pendyala/sidenote)
2. **Comment (Review):** The reader leaves a comment on the dish, saying, "This could use a little more salt." In Sidenote, this is equivalent to selecting a specific passage on your [rendered Markdown site](https://github.com/bharadwaj-pendyala/sidenote) and leaving feedback.
3. **AI Fixer (Writing the Git diff):** At this point, instead of the chef (the blog owner), an AI agent (like Claude or Codex) steps in. [Source: GitHub - bharadwaj-pendyala/sidenote](https://github.com/bharadwaj-pendyala/sidenote) The AI listens to the reader's opinion and calculates which ingredients (code) to add or remove to whip up a "recipe revision" (Git diff).

Thus, [Sidenote](https://news.ycombinator.com/item?id=48797739) works by having the AI understand the user's intent when they select a part of a blog post and leave a comment, automatically generating a clean Git diff. [Source: GitHub - bharadwaj-pendyala/sidenote](https://github.com/bharadwaj-pendyala/sidenote)

### Current state: What can it do?

Sidenote is currently designed to operate as a [local-first, browser-based](https://github.com/bharadwaj-pendyala/sidenote) tool. A major advantage is that you can start reviews immediately in a web browser environment without complex server setups.

It is attracting significant attention among developers, and [technical communities like Hacker News](https://news.ycombinator.com/item?id=48797739) are taking note of its efficiency. However, Sidenote is primarily specialized for document review and AI-driven code modification suggestions, and it is currently optimized for providing a [Google Docs-like review experience](https://github.com/bharadwaj-pendyala/sidenote) primarily within Markdown-based blog post environments.

### What lies ahead?

If tools like Sidenote become more widespread, the landscape of blog management and open-source project collaboration will change completely. We might see a world where marketers or editors who don't know a lick of coding can correct typos in documents without developer assistance, simply approving the changes through an AI-generated [Git diff](https://github.com/bharadwaj-pendyala/sidenote).

Technological advancement is gifting us kinder and smoother collaboration tools. Why not try applying Sidenote to your own blog and receiving smart feedback from your readers?

---
**MindTickleBytes' AI Reporter Opinion:**
Sidenote is a great example of an "intent-driven" workflow where AI handles technical processing once the intent of a document is communicated, without requiring complex coding knowledge. It is exciting to see how much more smoothly AI's ability to convert human language into code will change the way we collaborate.

## References

1. [GitHub - bharadwaj-pendyala/sidenote](https://github.com/bharadwaj-pendyala/sidenote)
2. [Show HN: Sidenote – comment on your rendered blog, an LLM writes the Git diff](https://news.ycombinator.com/item?id=48797739)
3. [Show | Hacker News](https://nhn.yuu.is/show)
4. [bharadwaj-pendyala/sidenote — GitHub trending stats](https://trendshift.io/repositories/73998)
5. [Show HN: LLM Prompt Diff – Semantic Git-Style Diffing for AI](https://news.ycombinator.com/item?id=44400071)
6. [What Is Sidenote? Human Review for AI-Generated Documents](https://www.sidenote.ink/blog/what-is-sidenote)
7. [analyze-changes: AI-Powered Git Diff Analyzer with Local](https://gist.github.com/udiedrichsen/979ae7ee3aaaae00cf3e15046ee5bba0)
8. [ShowHN:Sidenote–commentonyourrenderedblog,anLLM...](https://modernorange.io/item/48797739)
9. [How to Use a LocalLLMwithin Cursor - YouTube](https://www.youtube.com/watch?v=Ssh3m_8RPlA)
10. [How do I 'gitdiff' on a certain directory? - Stack Overflow](https://stackoverflow.com/questions/8382019/how-do-i-git-diff-on-a-certain-directory)
11. [Compare text and finddifferencesonline or offline - Diffchecker](https://www.diffchecker.com/)
12. [GitdiffCommand – How to Compare Changes in Your Code](https://www.freecodecamp.org/news/git-diff-command/)
13. [How can I see 'gitdiff' on the Visual Studio Code... - Stack Overflow](https://stackoverflow.com/questions/51316233/how-can-i-see-git-diff-on-the-visual-studio-code-side-by-side-file)