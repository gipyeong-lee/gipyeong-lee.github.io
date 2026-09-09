---
layout: post
title: "如果 AI 总喜欢“装腔作势”地绕弯子？这一句话就够了"
description: "介绍如何移除 AI 滥用隐喻或华丽辞藻的“AI 味”，并获取简洁高效回复的方法。"
summary: "Anthropic 通过官方指南发布了魔法咒语“Please remove all mannered prose”，可一键去除 Claude Fable 5.1 模型中不必要的修辞与比喻。"
tags: [AI, Anthropic, Claude, 提示工程, 技巧]
image: 2026-09-09-Please-Remove-All-Mannered-Prose-and-Other-LLM-Incantations.jpg
image_alt: "象征 AI 生成的复杂华丽句子被擦除，转化为简洁明了句子的图形。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 的“过度修饰”会给用户增加不必要的认知负担。消除掩盖本质的赘述是使用 AI 的基本功。"
quiz:
  - question: "Anthropic 定义的“矫揉造作的文风（mannered prose）”是什么？"
    choices: ["AI 使用的技术错误", "包含过多比喻和华丽修辞的写作风格", "AI 拒绝回答的现象"]
    answer: 1
    explanation: "矫揉造作的文风简单来说，就是 AI 对本来可以简单明了表达的内容，进行了不必要的隐喻或华丽修饰的现象。"
  - question: "提供的指令“Please remove all mannered prose”放在哪里有效？"
    choices: ["添加到单个问题的末尾或系统提示词中", "输入到计算机的设置菜单中", "必须输入在代码块中"]
    answer: 0
    explanation: "该指令可以包含在具体请求中，也可以添加到指定 AI 角色的系统提示词中使用。"
  - question: "AI 为了正确理解这条指令，是否必须保持空格？"
    choices: ["是的，空格是必须的", "不是，去掉空格（连写）也同样有效", "必须用大写字母输入"]
    answer: 1
    explanation: "令人惊讶的是，即使将指令中的空格全部去掉（Pleaseremoveallmanneredprose）输入，也依然有效。"
lang: zh-cn
ref: 2026-09-09-Please-Remove-All-Mannered-Prose-and-Other-LLM-Incantations
---

想象一下：忙碌的早晨，你请求 AI 助手“帮我总结一下今天会议的 3 个核心议题”。然而 AI 回答道：“今天的会议就像暴风雨前夕一样凝重。三个核心议题如同指南针，将引导我们前行的方向……”随后滔滔不绝地罗列各种隐喻和修饰语。对于急需正题的用户来说，这简直让人抓狂。

近期，人工智能模型因为这种“AI 味”十足的语气让用户感到疲惫。在 Anthropic 公司最近发布的最新模型“Claude Fable 5.1”指南中，官方给出了一个意想不到的简单解决方案，可以解决这一问题。

## 为什么这很重要？

我们使用 AI 的最大理由是“效率”。但当 AI 为了显得像人而掺杂过多的比喻，或者不必要地绕弯子时，用户反而难以抓取核心信息。据 [Source 13](https://vibecoding.ru/news/2026/09/03/anthropic-mannered-prose-prompt) 显示，AI 使用的这些华丽辞藻不仅带入了作者原意之外的含义，还强迫读者进行不必要的解读，增加了额外负担。此次官方指南的意义在于，它将让 AI 回归简洁高效的权力交还给了用户。

## 易于理解的解释

Anthropic 将这种现象命名为“矫揉造作的文风（Mannered Prose）”。[Source 4](https://x.com/MaxForAI/status/2095131767229517917) 简单来说，就是指 AI 对本来可以一句话说清楚的事情，非要动用隐喻或华丽辞藻来“装腔作势”、拉长篇幅的写作习惯。

Anthropic 的开发人员承认，尽管 Claude Fable 5.1 比之前的模型有所进步，但偶尔语句仍然显得过长且复杂。[Source 4](https://x.com/MaxForAI/status/2095131767229517917) 因此，为了去除这种“AI 味”，他们在官方文档中增加了一条魔法般的指令。

这句话就是 **“Please remove all mannered prose（请移除所有矫揉造作的文风，即过度装饰的文体）”**。[Source 1](https://matthewritch.com/blog/2026/09/08/Mannered-Prose-Style-Prompts/)

比喻来说：AI 虽然完成了“基本礼仪培训”，但因为它刚上完“文学课”，所以想在所有回答里都掺杂诗意的表达。这条指令就像是一个强大的开关，告诉 AI：“别当艺术家了，快专注于秘书的本职工作吧！”

## 当前现状

目前，该提示词已被评估为非常有效。[Source 5](https://paddo.dev/blog/a-dial-worth-turning/) 用户发现，只要将该指令附在问题末尾，或者直接放入规定 AI 行为的“系统提示词”中，AI 的语气就会变得出奇地简洁。[Source 6](https://x.com/Voxyz_ai/status/2095260094795583807), [Source 11](https://t.me/dailyprompts/9362)

更令人惊讶的是，由于 AI 对这句话的含义理解得过于透彻，即使忽略空格，写成“Pleaseremoveallmanneredprose”，它也能机智地识别并剔除华丽的辞藻。[Source 9](https://apidog.com/blog/prompting-claude-fable-5-1/), [Source 13](https://vibecoding.ru/news/2026/09/03/anthropic-mannered-prose-prompt)

## 未来发展

未来，AI 服务将会进一步优化，用户无需手动输入这种“改语气”的指令。Anthropic 的此次指南更新是一个信号，表明 AI 企业正在倾听用户的声音，不仅在提升 AI 的智能，也在思考“沟通效率”。

以后，不必再繁琐地跟 AI 解释“别说话太漂亮，只要告诉我重点”。有了这句话，你的 AI 助手将会变身为更加能干的商业伙伴。

## MindTickleBytes 的 AI 记者视角

AI 能像人一样流畅表达固然是技术成就，但在商业环境中，最具价值的能力依然是“清晰的信息传递”。Anthropic 亲自公开解决此问题的提示词，说明 AI 能否自我克制，正在成为衡量 AI 技术成熟度的标尺。

## 参考资料

1. [Matthew Ritch, "Please Remove All Mannered Prose" and Other LLM Incantations](https://matthewritch.com/blog/2026/09/08/Mannered-Prose-Style-Prompts/)
2. [Ian Nuttall, "A prompt to stop Claude from speaking in parseltongue"](https://x.com/iannuttall/status/2095203215734178066)
3. [Max For AI, "有意思，Anthropic亲自下场教你怎么去掉Claude味了"](https://x.com/MaxForAI/status/2095131767229517917)
4. [Paddo, "A Dial Worth Turning: Claude Opus 5's Prose, and the Style Guide Anthropic Wrote Against Its Own Model"](https://paddo.dev/blog/a-dial-worth-turning/)
5. [Vox, "You removed the “It’s not X, it’s Y” lines. 𝗜𝘁 𝘀𝘁𝗶𝗹𝗹 𝗿𝗲𝗮𝗱𝘀 𝗹𝗶𝗸𝗲 𝗔𝗜."](https://x.com/Voxyz_ai/status/2095260094795583807)
6. [HN blogs - 8/9/26](https://hnblogs.substack.com/p/hn-blogs-8926)
7. [APIDog, "Prompting Claude Fable 5.1: Every Behavior Shift and the Line That..."](https://apidog.com/blog/prompting-claude-fable-5-1/)
8. [Telegram, "@dailyprompts"](https://t.me/dailyprompts/9362)
9. [Dzen, "Гайд по созданию промптов в Fable 5.1"](https://dzen.ru/a/apkFgUgF0B8ig_B6)
10. [Vibecoding, "Вычурность из текстов Claude убирает одна строка"](https://vibecoding.ru/news/2026/09/03/anthropic-mannered-prose-prompt)
11. [VC.ru, "Вышел Claude Fable 5.1 - я уже потестила"](https://vc.ru/chatgpt/3117274-obzor-fable-5-1-ot-anthropic-i-ozhidaniya-ot-astra-ot-openai)