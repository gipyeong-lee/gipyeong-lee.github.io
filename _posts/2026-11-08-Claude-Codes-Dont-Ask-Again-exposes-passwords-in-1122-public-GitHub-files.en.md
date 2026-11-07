---
layout: post
title: "I told AI 'don't ask me again' and my password got exposed? Warnings from 1,122 GitHub repositories"
description: "We examine how the 'don't ask again' feature in Anthropic's AI coding assistant, Claude Code, leaked developers' passwords and API keys, along with its risks and how to respond."
summary: "A security incident has occurred where the 'don't ask again' convenience feature of Claude Code AI saved developers' passwords and API keys in plaintext to configuration files, leading to leaks on GitHub."
tags: [AI, Security, ClaudeCode, Developer, GitHub]
image: 2026-11-08-Claude-Codes-Dont-Ask-Again-exposes-passwords-in-1122-public-GitHub-files.jpg
image_alt: "Digital art representing a compromised GitHub code repository and AI tool icons."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "This is a case demonstrating the high price that can be paid for simplifying security settings for the sake of convenience. When using AI tools, you must always check what data is being stored and where."
quiz:
  - question: "What is the main reason password leaks occur in Claude Code?"
    choices: ["The AI model was hacked", "Commands are saved in plaintext in configuration files when using the 'don't ask again' feature", "The GitHub server itself was hacked"]
    answer: 1
    explanation: "When a user selects the 'Yes, and don't ask again' option, the commands executed by the AI are saved in plaintext in configuration files (such as .claude/settings.local.json)."
  - question: "Which of the following is NOT appropriate as information exposed by this security incident?"
    choices: ["API keys", "Database passwords", "OS update logs of a personal computer"]
    answer: 2
    explanation: "The information leaked primarily consists of passwords, API keys, database credentials, SSH keys, etc."
  - question: "How many public GitHub repositories have been confirmed to be affected by this security incident?"
    choices: ["1,122", "76,011", "104,185"]
    answer: 0
    explanation: "According to an investigation by security firm Apiiro, files containing actual sensitive information were discovered in a total of 1,122 public GitHub repositories."
lang: en
ref: 2026-11-08-Claude-Codes-Dont-Ask-Again-exposes-passwords-in-1122-public-GitHub-files
audio: 2026-11-08-Claude-Codes-Dont-Ask-Again-exposes-passwords-in-1122-public-GitHub-files.en.mp3
industry: security
---

Imagine this: You delegate a complex task to your AI coding assistant as usual. Every time the AI asks, "Do you want to continue executing this command?" it feels cumbersome, so you dismissively click the button that says, "Yes, and don't ask again." But what if this single convenient click resulted in your database passwords and API keys being "exhibited" in an internet space where anyone in the world could see them?

Recently, a ridiculous yet frightening security incident occurred among developers using the AI tool 'Claude Code.' A simple convenience feature stored developers' precious credentials in plaintext (unencrypted and human-readable data).

## Why is this important?

This issue is not just "a developer thing." AI coding tools are now becoming standard in development work. If a tool like this records the passwords included in commands you input without any security measures into a configuration file, and that file is uploaded as-is to a shared repository like GitHub, the story changes. Malicious hackers can use this to break into your servers or easily hijack your cloud service accounts.

Security research firm Apiiro has confirmed that due to this issue, passwords, API keys, and more were exposed unprotected in a staggering 1,122 public GitHub repositories [Source 2, Source 5, Source 14].

## Easy to understand: The 'smart assistant's' mistake

To use a simple analogy, Claude Code is like your 'smart assistant.' You essentially told this assistant, "Don't ask me for my password every time, just process the commands exactly as I give them to you."

This is where the problem arises. To process the command again later, the assistant carefully writes it down in its 'notepad.' But this assistant lacks security awareness, so it recorded sensitive content you mentioned during the command, such as "Database password: 12345," without filtering it. And this notepad ended up being uploaded to the public bulletin board (GitHub) where you share your work [Source 6, Source 7].

Looking at it in more technical detail, when a user selects 'Yes, and don't ask again,' Claude Code saves the executed shell commands in plaintext in configuration files such as `.claude/settings.local.json` or `.claude/settings.json` [Source 3, Source 7, Source 8]. As developers inadvertently commit these files along with their code to GitHub, the sensitive information was exposed to the internet [Source 2, Source 5].

## What is the current situation?

The current situation is very serious. According to Apiiro's analysis, out of 104,185 copies of configuration files investigated, actual passwords or API keys were found in 1,122 of them [Source 14]. Another analysis also indicated that passwords were contained in shared configuration files in 298 out of 76,011 copies [Source 3].

These files are not just simple configuration files but are essentially 'digital key rings' containing API keys, database credentials, SSH keys, and more [Source 6, Source 7]. If you are using Claude Code, you should immediately and thoroughly check the past history of your GitHub repositories. Even if the files are not visible in the current repository, they may remain in the past commit history [Source 3].

## How should we respond in the future?

Experts strongly recommend that if a password or API key has ever been stored in these files, you **must immediately revoke and regenerate (rotate) those credentials** [Source 3].

Going forward, developers using AI coding agents must pay closer attention to configuration file management. At the enterprise level, it is essential to strengthen security policies to prevent AI tool configuration files from being committed to repositories and to establish a system that monitors for leaks of sensitive information through continuous scanning [Source 7].

## MindTickleBytes' AI Reporter Perspective

Convenience often erodes security. The powerful tool of 'automation' provided by Claude Code resulted in the distraction of its users, and the consequences are plainly visible in 1,122 repositories. It serves as a reminder of the obvious fact that as tools become smarter, the security awareness of the humans using those tools must become sharper.

## References

1. [Source 2] Claude Code "Don't Ask Again" File Leaks 1,122 Public GitHub Repos Detection and Remediation Guide (https://securityarsenal.com/blog/claude-code-dont-ask-again-file-leaks-1122-public-github-repos-detection-and-remediation-guide)
2. [Source 3] Claude Code's don't-ask-again file held 1,379 secrets in 1,122 public repos: What to do (https://dev.to/piekwerk/claude-codes-dont-ask-again-file-held-1379-secrets-in-1122-public-repos-what-4mg5)
3. [Source 5] Claude Code 'Don't Ask Again' Bug Exposes 1,122 GitHub Repos (https://aviatrix.ai/threat-research-center/claude-code-dont-ask-again-settings-local-json-passwords-keys-1122-github-2026/)
4. [Source 6] Claude Code “Don't Ask Again” Feature Exposes Passwords and API Keys in Public GitHub Repositories (https://www.cyberincidents.in/blog/claude-code-dont-ask-again-feature-exposes-passwords-and-api-keys-in-public-github-repositories)
5. [Source 7] Claude Code's “Don't Ask Again” File Exposes Passwords and Keys in 1,122 Public GitHub Repos (https://www.realground.com/news/2650-claude-codes-dont-ask-again-file-exposes-passwords-and-keys-in-1-122-public)
6. [Source 8] Утечка “Don’tAskAgain” отClaudeCode: пароли и ключи (https://dzen.ru/a/au7m4aCL2QDFv4Wh)
7. [Source 14] Claude Code “Don’t ask again” left secrets in 1,122 GitHub files (https://madrobot.blog/2026/11/07/claude-code-dont-ask-again-secrets-github/)