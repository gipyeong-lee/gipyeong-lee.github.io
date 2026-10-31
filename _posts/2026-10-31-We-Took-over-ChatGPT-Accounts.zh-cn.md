---
layout: post
title: "我的ChatGPT账户被盗？安全研究人员揭露的惊人事实"
description: "安全研究团队发现了一个可以完全夺取ChatGPT账户的严重安全漏洞。这意味着你的账户信息和聊天记录可能处于危险之中，我们为您通俗易懂地解释这背后的隐患。"
summary: "安全研究人员发现了一个安全漏洞，攻击者可以通过直接调用ChatGPT的认证API来窃取用户账户。"
tags: [ChatGPT, 安全, AI, 账户窃取]
image: 2026-10-31-We-Took-over-ChatGPT-Accounts.jpg
image_alt: "可视化数字锁被解除的安全概念图"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "便利性背后往往隐藏着安全漏洞。请密切关注服务的安全更新，并养成对重要账户启用双重认证的习惯。"
quiz:
  - question: "安全研究人员发现的ChatGPT安全漏洞的核心是什么？"
    choices: ["更改了网站设计", "通过调用认证API窃取账户", "导致聊天速度变慢"]
    answer: 1
    explanation: "研究人员演示了攻击者可以通过代替受害者直接调用ChatGPT的认证API来完全夺取账户控制权。"
  - question: "OpenAI向用户警告的ChatGPT特性是什么？"
    choices: ["无条件拒绝用户的命令", "允许用户在对话中中断并夺回主导权", "被设计为无法感知情感"]
    answer: 1
    explanation: "OpenAI解释称，ChatGPT具有“顺从（deferential）”的特性，允许用户中断其发言并夺回对话主导权。"
  - question: "OpenAI首席执行官山姆·奥特曼向用户提出了什么建议？"
    choices: ["建议将ChatGPT作为治疗师使用", "应避免将聊天机器人作为治疗师使用", "建议信任ChatGPT的所有回答"]
    answer: 1
    explanation: "山姆·奥特曼曾对将聊天机器人用作治疗师表示担忧，并表明不建议这样做。"
lang: zh-cn
ref: 2026-10-31-We-Took-over-ChatGPT-Accounts
---

## 导语

试想一下：像往常一样打开ChatGPT进行工作交流时，突然发现账户的主导权不再属于自己，而是被别人控制了。这不仅仅是界面显示异常那么简单。你的个人信息、海量的聊天记录，甚至服务使用权限，全部落入了陌生人之手。最近，一个安全研究团队披露了这一致命的“账户窃取”安全漏洞，向整个行业敲响了警钟。

## 为什么这很重要？

随着AI服务深入我们的日常生活，“账户安全”已成为刚需。研究人员展示的不仅仅是修改网页外观或弹出通知的程度，而是直接利用受害者的账户权限，调用ChatGPT的认证API（应用程序编程接口，连接不同软件的通信通道）[来源：Do the Math: HowWeTookOverChatGPTAccounts- Parameter](https://www.parameter.ai/labs/we-found-a-gap-at-openai)。这意味着你的账户可以在你不知情的情况下被他人操纵，用户的隐私正面临极高的风险。

## 通俗理解：什么是API？

要理解这个问题，首先得知道什么是“API”。

简单来说，当我们与ChatGPT对话时，后台其实是我们电脑与OpenAI服务器在进行不间断的“对话”。这种交流所使用的语言和规则就是API。

**打个比方：**
平时你在银行柜台（ChatGPT服务）与银行职员（OpenAI服务器）对话时，会出示身份证来证明“你”的身份。而这个安全漏洞就像是黑客复制了你的身份证出示给银行职员。职员无法分辨身份证的真伪，误以为黑客就是你，从而按照黑客的要求汇款或泄露账户信息。

研究人员证明，黑客可以利用充当“身份识别”作用的认证令牌，伪装成受害者向服务器发送指令 [来源：Do the Math: HowWeTookOverChatGPTAccounts- Parameter](https://www.parameter.ai/labs/we-found-a-gap-at-openai)。

## 为什么这么危险？

目前，OpenAI仍在不断调整其运营方式。例如，旧模型GPT-4即将退役，并将默认配置切换为更先进的GPT-4o [来源：ChatGPT: Everything you need to know about the AI chatbot](https://techcrunch.com/2025/12/22/chatgpt-everything-to-know-about-the-ai-chatbot/)。

此外，ChatGPT在设计上具备高度的“顺从性（deferential）”，允许用户随时中断其发言并夺回对话主导权 [来源：OpenAI is worried thatChatGPT-4o users are developing... | TechRadar](https://www.techradar.com/computing/artificial-intelligence/openai-is-worried-that-chatgpt-4o-users-are-developing-feelings-for-the-chatbot/)。这种技术灵活性虽然方便了用户，但从安全角度看，也可能成为黑客利用系统漏洞的切入点。

特别是最近，将AI用作治疗师的用户越来越多。然而，连OpenAI首席执行官山姆·奥特曼也曾表示，对将聊天机器人当作治疗师使用持谨慎态度，不建议这样做 [来源：Even The Guy Who MakesChatGPTSays You Probably... - CNET](https://www.cnet.com/tech/services-and-software/even-the-guy-who-makes-chatgpt-says-you-probably-shouldnt-use-chatbots-as-therapists/)。一旦包含隐私困扰或重要信息的对话泄露给黑客，其后果将远超丢失账户本身。

## 未来我们该怎么做？

随着AI技术的发展，旨在保护技术的安全技术也会更加精进。正如这次漏洞披露一样，通过安全研究人员提前提出问题、OpenAI不断修正的过程，服务会变得越来越安全。作为用户，我们需要随时应用最新的安全更新，并通过双重认证等手段主动保护个人账户。

## AI的视角 (AI's Take)

MindTickleBytes的AI记者观点：“技术进步带来的便利，必须跨越安全这道门槛。认识到‘AI善于倾听’这一便利背后的账户窃取风险，是现代数字公民应当具备的第一素养。”

## 参考资料

1. [Do the Math: HowWeTookOverChatGPTAccounts- Parameter](https://www.parameter.ai/labs/we-found-a-gap-at-openai)
2. [OpenAI is worried thatChatGPT-4o users are developing... | TechRadar](https://www.techradar.com/computing/artificial-intelligence/openai-is-worried-that-chatgpt-4o-users-are-developing-feelings-for-the-chatbot/)
3. [Even The Guy Who MakesChatGPTSays You Probably... - CNET](https://www.cnet.com/tech/services-and-software/even-the-guy-who-makes-chatgpt-says-you-probably-shouldnt-use-chatbots-as-therapists/)
4. [ChatGPT: Everything you need to know about the AI chatbot](https://techcrunch.com/2025/12/22/chatgpt-everything-to-know-about-the-ai-chatbot/)