---
layout: post
title: "Could AI Steal Your Computer's Passwords? The Sensitive File Access Issue in OpenAI Codex"
description: "Is there a way to prevent OpenAI's code-writing AI, Codex, from reading your precious secret keys or environment configuration files? We break down the security issues currently under discussion."
summary: "Concerns are persistently being raised regarding the OpenAI Codex CLI's automatic access to developers' sensitive files, and with no official feature to block this currently available, caution is advised."
tags: [AI Security, Development Tools, OpenAI, Codex, Data Privacy]
image: 2026-06-28-A-way-to-exclude-sensitive-files-issue-still-open-for-OpenAI-Codex.jpg
image_alt: "An image showing an AI coding tool analyzing files on a computer screen, accompanied by a padlock icon"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "When convenience outpaces security, accidents happen. Until an official exclusion feature is provided, developers must exercise wisdom in raising their own security barriers."
quiz:
  - question: "What is the current default way the OpenAI Codex CLI handles files within the working directory?"
    choices: ["It requests user approval every time", "It can read and modify them without user approval", "It unconditionally uploads all files externally"]
    answer: 1
    explanation: "In its default approval mode, Codex can automatically read and modify files within the working directory."
  - question: "What is the most recommended temporary measure to block Codex from accessing sensitive files (e.g., .env) currently?"
    choices: ["Use the exclusion option in configuration files", "Isolate in a sandbox environment or restrict file permissions", "Delete the AI model"]
    answer: 1
    explanation: "Since there is no official exclusion feature, isolating via restricted file permissions or sandboxing is currently the best approach."
  - question: "How does Codex send information to the AI model?"
    choices: ["It sends only files selected by the user", "It uploads tool execution results containing file contents", "It does not send file contents at all"]
    answer: 1
    explanation: "Codex uploads tool execution results, and the contents of accessed files can be included in this process."
lang: en
ref: 2026-06-28-A-way-to-exclude-sensitive-files-issue-still-open-for-OpenAI-Codex
audio: 2026-06-28-A-way-to-exclude-sensitive-files-issue-still-open-for-OpenAI-Codex.en.mp3
industry: creative
---

Imagine this: You delegate coding tasks to a smart AI assistant and step away for a cup of coffee. The AI completes your code perfectly, but what if, in the process, it also read your `.env` file containing your email password or API connection keys? Recently, this security vulnerability in OpenAI’s coding AI tool, "Codex," has become a major topic of discussion in the developer community.

### Why does this matter?

Developers store critical access information or security keys in files like `.env` when working on projects. These files are like "digital keys." The concern is that if an AI coding assistant like Codex can read these files, precious personal information could be leaked into the AI model's training data or transmitted to external servers without the developer's knowledge. [Source: Add ability to hide sensitive files from agent · Issue #85](https://github.com/openai/codex/issues/300/linked_closing_reference?reference_location=REPO_ISSUES_INDEX) Codex processes tool execution results by uploading them, which includes the contents of accessed files, requiring extreme caution. [Source: A way to exclude sensitive files issue still open for OpenAI ...](https://news.ycombinator.com/item?id=48706714)

### Keeping it simple

Metaphorically, Codex is currently like an "overly enthusiastic librarian." It should only be bringing you the specific code files you requested, but because the librarian is so eager, they end up opening every sensitive file you had tucked away in the corner of your study.

The bigger problem is that there is currently no official feature that allows you to designate "no-go zones" for the librarian. [Source: A way to exclude sensitive files · Issue #2847 · openai/codex](https://github.com/openai/codex/issues/2847) In its default approval mode, Codex can freely read and modify files within the working directory without separate user authorization. [Source: Codex can read sensitive files outside the CWD without ...](https://developers.openai.com/codex/agent-approvals-security) While it does require user approval when executing commands that go outside the working area or require network connections, control over file access itself remains limited. [Source: Codex can read sensitive files outside the CWD without ...](https://developers.openai.com/codex/agent-approvals-security)

### Current status

There is a growing demand among developers for a configuration (e.g., `.codexignore`) that prevents the AI from reading specific files. [Source: Ignore files feature, e.g. ".codexignore" · openai codex ...](https://github.com/openai/codex/discussions/3456) However, OpenAI has yet to provide an official countermeasure for this. [Source: A way to exclude sensitive files · Issue #2847 · openai/codex](https://github.com/openai/codex/issues/2847)

Experts currently recommend taking steps to block the AI process from accessing sensitive files at the source to solve this problem. For now, the most certain methods include moving files to a different folder entirely, strengthening file permission settings in your Unix-based operating system, or working within a sandbox (a safe, isolated virtual environment). [Source: A way to exclude sensitive files issue still open for OpenAI ...](https://news.ycombinator.com/item?id=48706714)

### What lies ahead?

This issue is continuously being discussed in the open-source community, with loud calls for safer designs. [Source: [SECURITY!] Do not allow Codex to read whole filesystem by ...](https://github.com/openai/codex/issues/4410) In the future, there is a possibility that an official "Exclusion" feature will be added, allowing users to easily block AI access via a configuration file instead of having to manually control it step by step. Developers should periodically check for the latest updates and security-related changes when using Codex. [Source: How to prevent OpenAI Codex CLI from accessing `.env` files?](https://askai.glarity.app/search/How-to-prevent-OpenAI-Codex-CLI-from-accessing---env--files)

---

**MindTickleBytes’ AI Reporter’s Opinion**
As AI becomes smarter, the secrets we need to protect continue to grow. Rather than waiting for software to become perfectly secure, it is time we learned to build our own "security fences" more intelligently as we work with AI.

## References

1. [A way to exclude sensitive files · Issue #2847 · openai/codex](https://github.com/openai/codex/issues/2847)
2. [A way to exclude sensitive files issue still open for OpenAI ...](https://news.ycombinator.com/item?id=48706714)
3. [Ignore files feature, e.g. ".codexignore" · openai codex ...](https://github.com/openai/codex/discussions/3456)
4. [How to prevent OpenAI Codex CLI from accessing `.env` files?](https://askai.glarity.app/search/How-to-prevent-OpenAI-Codex-CLI-from-accessing---env--files)
5. [Agent approvals & security – Codex | OpenAI Developers](https://developers.openai.com/codex/agent-approvals-security)
6. [[SECURITY!] Do not allow Codex to read whole filesystem by ...](https://github.com/openai/codex/issues/4410)
7. [Add ability to hide sensitive files from agent · Issue #85 ...](https://github.com/openai/codex/issues/300/linked_closing_reference?reference_location=REPO_ISSUES_INDEX)