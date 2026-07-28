---
layout: post
title: "与我的 AI 的私密对话出现在搜索结果中？Claude 对话泄露事件的来龙去脉"
description: "最近，Anthropic 的 AI 聊天机器人 Claude 的用户共享对话内容被曝出现在 Google 和必应（Bing）的搜索结果中。本文将带您了解此次事件的详细经过及个人隐私保护的注意事项。"
summary: "由于 Anthropic 的 Claude 服务配置出现错误，导致用户共享的对话内容被搜索引擎抓取并泄露。"
tags: [AI, 安全, 个人隐私, Claude, Anthropic]
image: 2026-07-29-Private-Claude-Chats-Exposed-in-Google-and-Bing-Search-Results.jpg
image_alt: "一幅插图，展示了一位用户发现与 AI 聊天机器人的对话内容出现在搜索引擎屏幕上后感到惊慌失措"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "在享受 AI 技术带来的便利的同时，我们也迫切需要以负责任的态度对待数据安全。在使用共享功能时，务必重新审视内容的敏感程度。"
quiz:
  - question: "在此次事件中，用户对话被搜索引擎暴露的主要原因是什么？"
    choices: ["AI 自身的黑客攻击事故", "共享 URL 设置的配置错误", "搜索引擎的恶意攻击"]
    answer: 1
    explanation: "Claude 平台的共享 URL 设置出现配置错误，导致搜索引擎能够对其进行抓取和索引。"
  - question: "是谁首次发现了此次事件？"
    choices: ["Anthropic 安全团队", "Google 安全团队", "Reddit 用户"]
    answer: 2
    explanation: "Reddit 用户在使用搜索运算符查询 Claude 的共享页面时，首次发现了该问题。"
  - question: "针对搜索引擎暴露的问题，Google 和必应是如何应对的？"
    choices: ["两者均立即删除了相关内容。", "Google 开始删除，但必应仍保留了部分链接。", "两者均未做出回应。"]
    answer: 1
    explanation: "Google 在问题曝光后开始删除已索引的结果，但在报告时，必应仍有部分共享链接出现在搜索结果中。"
lang: zh-cn
ref: 2026-07-29-Private-Claude-Chats-Exposed-in-Google-and-Bing-Search-Results
---

想象一下：昨天深夜，你还在与 AI 聊天机器人商讨极其机密的商业项目，或者让它仔细检查你准备修改的简历。然而第二天早上，当你在 Google 搜索结果中看到这些对话内容时，会作何感想？这正是最近发生在人工智能（AI）服务 Claude 用户身上的真实事件。

### 这为何至关重要？

AI 早已超越了简单的问答工具，成为协助我们工作与生活的合作伙伴。因此，我们自然而然地会将简历、公司机密项目、个人烦恼等高度敏感的信息输入其中。此次事件生动地展示了我们随手使用的“对话共享”功能可能成为巨大的隐私泄露渠道。这不仅关乎服务使用的便利性，更提醒我们需要警惕输入的数据可能流向何处。

### 浅显易懂的解读

我们可以用一个比喻：我们与 AI 的对话默认保存在一间“数字房间”里。为了与他人分享某些信息而创建的“共享链接”，本质上就是制作了一把进入该房间的“秘密钥匙”。

此次事件的问题在于，这把钥匙被随手放在了随处可见的大门口。由于 Claude 的开发商 Anthropic 的平台设置存在错误，Google 和必应等搜索引擎的机器人能够像浏览公立图书馆的藏书一样，自由抓取这些共享链接（`claude.ai/share/*` 地址格式）并将其收录到索引中（[Source 4](https://www.imtr.net/article/private-claude-chats-exposed-in-google-and-bing-search-results-e745)）。

用户本意只是想将内容分享给熟人，却因系统设置疏忽，导致全球任何人在搜索框输入特定关键词就能随意偷窥这些对话内容（[Source 10](https://www.aibase.com/news/29910)）。

### 当前情况

该问题最初是在线社区 Reddit 的用户在利用搜索运算符查询 Claude 的公开共享页面时偶然发现的（[Source 12](https://interestingengineering.com/ai-robotics/claude-google-search-chat-exposure)）。

随着事态严重，Google 开始从搜索结果中移除这些链接（[Source 11](https://www.gncrypto.news/news/anthropic-claude-links-indexed-by-google-exposing-chats/)）。然而，在调查时，必应（Bing）中仍有约 612 个共享链接出现在搜索结果中（[Source 1](https://www.wired.com/story/private-claude-chats-exposed-in-google-and-bing-search-results/)）。这导致用户的简历、公司内部项目详情以及其他个人隐私信息毫无防备地暴露出来（[Source 6](https://thecybersecguru.com/news/claude-shared-chats-google-search-privacy/)）。

### 未来将如何发展？

此次事件将作为重要案例载入史册，警示 AI 企业在追求技术性能的同时，必须更加审慎地对待安全和隐私设计。未来，服务提供商需要强化共享功能的默认设置，或者采取更彻底的技术手段（如配置 `robots.txt`）来防止搜索引擎抓取。

作为用户也需提高警惕，“共享链接”绝非绝对安全的通道。最好不要向 AI 输入敏感信息；若必须分享对话，务必再次权衡对方的可靠程度以及分享的必要性。拥有 AI 助手固然便利，但请记住，信息的拥有者终究是你自己。

### AI 的视角

人工智能看似拥有魔法，但其底层终究是由海量代码和复杂的配置参数构成的。此次事故提醒我们，我们所信任的 AI 服务可能因为一个小小的“门未锁”而陷入危机。我们每个人都应意识到便捷背后所承载的安全重量。

---

## 参考资料

1. Private Claude Chats Exposed in Google and Bing Search ... ([https://www.wired.com/story/private-claude-chats-exposed-in-google-and-bing-search-results/](https://www.wired.com/story/private-claude-chats-exposed-in-google-and-bing-search-results/))
2. Private Claude chats exposed in Google and Bing search results ([https://yourstory.com/ai-story/private-claude-chats-exposed-google-bing](https://yourstory.com/ai-story/private-claude-chats-exposed-google-bing))
3. Private Claude Chats Showed Up In Search Engine Results. A ... ([https://www.ibtimes.com/private-claude-chats-showed-search-engine-results-missing-web-setting-drawing-scrutiny-3805807](https://www.ibtimes.com/private-claude-chats-showed-search-engine-results-missing-web-setting-drawing-scrutiny-3805807))
4. Private Claude Chats Exposed in Google and Bing Search ... ([https://www.imtr.net/article/private-claude-chats-exposed-in-google-and-bing-search-results-e745](https://www.imtr.net/article/private-claude-chats-exposed-in-google-and-bing-search-results-e745))
5. Users’ seemingly private conversations with Anthropic’s ... ([https://fortune.com/2026/07/27/a-trove-of-users-seemingly-private-conversations-with-anthropics-claude-ai-chatbot-showed-up-in-google-search-results/](https://fortune.com/2026/07/27/a-trove-of-users-seemingly-private-conversations-with-anthropics-claude-ai-chatbot-showed-up-in-google-search-results/))
6. Claude Shared Chats Indexed by Search Engines Raise Privacy ... ([https://thecybersecguru.com/news/claude-shared-chats-google-search-privacy/](https://thecybersecguru.com/news/claude-shared-chats-google-search-privacy/))
7. GoogleNews- SharedClaudeAI conversationsexposedviaGoogle... ([https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2paNU12WUVSRkxBRTZhYzB1bUlDZ0FQAQ?hl=en-PH&gl=PH&ceid=PH:en](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2paNU12WUVSRkxBRTZhYzB1bUlDZ0FQAQ?hl=en-PH&gl=PH&ceid=PH:en))
8. Public by Link Is NotSearchable: A Founder Visibility... - Y Build ([https://ybuild.ai/en/blog/ai-share-link-visibility-contract-founders](https://ybuild.ai/en/blog/ai-share-link-visibility-contract-founders))
9. ClaudeChatsExposedinSearchResults ([https://superintelligencenews.com/ai-fields/large-language-models/claude-chats-exposed-search-results/](https://superintelligencenews.com/ai-fields/large-language-models/claude-chats-exposed-search-results/))
10. ClaudeChatSharing Link Misindexed bySearchEngines, Leading to... ([https://www.aibase.com/news/29910](https://www.aibase.com/news/29910))
11. AnthropicClaudelinks indexed byGoogle,exposingchats ([https://www.gncrypto.news/news/anthropic-claude-links-indexed-by-google-exposing-chats/](https://www.gncrypto.news/news/anthropic-claude-links-indexed-by-google-exposing-chats/))
12. GoogleSearchlists publicClaudechats, raisingprivacyconcerns ([https://interestingengineering.com/ai-robotics/claude-google-search-chat-exposure](https://interestingengineering.com/ai-robotics/claude-google-search-chat-exposure))