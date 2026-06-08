---
layout: post
title: "AI 开始提问而不是直接给答案？“教与学”的 Claude 活用法"
description: "取代无意义的社交媒体无限滑动，向 AI 学习新知识，反过来教 AI 你的工作方式的“技能（Skills）”功能。一起来了解聪明使用 Claude 的最新方法论。"
summary: "AI 已不再是单纯提供答案的自动售货机，它正在进化为培养学生思考能力的“老师”，以及完美理解你工作方式的“定制型同事”。"
tags: [Claude, 人工智能教育, AI 技能, 提示词, 技巧]
image: 2026-06-08-Claude-Teach-Me-Something.jpg
image_alt: "一幅温馨的插画，画面中用户与笔记本电脑屏幕中的 AI 就像老师和学生面对面交谈一样，相互交流知识。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "人工智能现在已经不再是只回答我们问题的百科全书。它既是训练我们如何思考的教练，也是如海绵般吸收我们工作窍门的能干后辈，同时扮演着这两个角色。"
quiz:
  - question: "文章中介绍的“Teach me something（教我点什么）”提示词最初是出于什么目的设计的？"
    choices: ["为了在短时间内通过外语资格考试", "为了替代无意义地滑动社交媒体的末日滚动（Doomscrolling）", "为了计算复杂的数学公式"]
    answer: 1
    explanation: "开发者 Hugo Tunius 为了替代无意义地看智能手机的末日滚动，利用 AI 的创造力设计了这个工作流，用于每次学习新知识。"
  - question: "Anthropic 在教育版 Claude 中引入的“学习模式（Learning mode）”最大的特点是什么？"
    choices: ["一收到问题就在1秒内输出最准确的答案。", "如果学生说出错误答案，将暂时冻结账号。", "不直接给出正确答案，而是引导推理过程，让学生自己思考。"]
    answer: 2
    explanation: "学习模式不是答案提供者，而是扮演向导的角色。它的重点是帮助思考过程，以培养学生的批判性思维能力。"
  - question: "文章中关于“技能（Skills）”和“模型上下文协议（MCP）”区别的正确解释是哪一项？"
    choices: ["MCP 允许访问工具，而技能（Skills）则告知使用该工具的具体步骤。", "MCP 是付费功能，技能（Skills）是免费功能。", "MCP 是生成图像的功能，技能（Skills）是生成文本的功能。"]
    answer: 0
    explanation: "如果说 MCP 是把工具交到 AI 手里，那么技能（Skills）就是一本“程序指南”，上面写着如何利用这些工具实际处理工作。"
lang: zh-cn
ref: 2026-06-08-Claude-Teach-Me-Something
---

想象一下。晚上11点，结束了一天的劳作后躺在床上，习惯性地打开智能手机。手指毫无目的地机械滑动，无休止地翻阅着社交媒体的动态，不知不觉中一个小时就这么溜走了。这就是许多人都会产生共鸣的所谓“末日滚动（Doomscrolling，无休止地阅读令人沮丧或刺激性内容的刷屏行为）”。揉着疲惫的眼睛，后悔着“唉，又浪费时间了”然后入睡，是现代人司空见惯的日常。

但是，如果代替这种毫无意义的时间浪费，人工智能每天晚上都能以非常有趣的方式，甚至完全针对你的水平，向你传授新知识呢？从你平时好奇的宇宙起源，到每天早上喝的咖啡豆烘焙背后的化学原理。

最近有一个非常有趣的实验。一位用户没有无休止地滑动社交媒体，而是创建了一个工作流：只需向 Claude 输入一个简单的提示词（指令）——**“教我点什么（Teach me something）”**。他积极利用了大型语言模型最擅长的“非确定性（Non-determinism，即对于相同的问题，根据提问方式或情境的不同，AI 每次都能生成非机械的、丰富多彩的文本的独有特性）”，将 AI 变成了一位出色的定制型通识讲师。[Claude，教我点什么](https://hugotunius.se/2025/10/26/claude-teach-me-something.html)

这一案例是一个标志性的场景，表明我们对待 AI 的态度正在发生根本性的改变。在早期使用 ChatGPT 或 Claude 等 AI 时，我们通常将其视为“自动售货机”。就像投币一样，抛出问题，就希望能“吧嗒”一声掉出正确答案的易拉罐。但在 2026 年的今天，开发者、教育工作者以及普通用户正在与 AI 进行着深度的交流。我们不仅向 AI 学习新知识，反过来，我们也会仔细地教导 AI “我们的工作方式”。

今天，我们将通俗易懂地深入探讨智能使用 Claude 的最新方法论。它已经不再是单纯吐出答案的机器，正在进化为真正意义上的“老师”，以及完美理解你工作方式的“定制型同事”。

---

## 为什么这很重要？（Why It Matters）

这种变化对我们的日常生活和职业世界的影响实为巨大。就在几年前，如果遇到不懂的问题，你还得在搜索引擎中输入关键词，然后逐一点击无数的蓝色链接，自己拼凑信息。随着 AI 的出现，这个过程被大幅缩短，但早期的 AI 仅仅停留在单方面通知“这就是答案”的阶段。这虽然方便，但另一方面也引发了人们的深切担忧，认为这会削弱人类独立思考和沉思的能力。

但现在 AI 发展的方向完全不同。AI 现在开始扮演**“领跑员（Pacemaker）”**的角色，在身边奔跑并帮助用户培养独立思考的能力。学生们与 AI 辩论，积累知识并磨练逻辑。反之，职场人士则将自己在职场摸爬滚打多年积累的业务诀窍和流程“传授”给 AI，从而无限复制出完美理解自己的智能秘书。

简而言之，人类不再仅仅是信息的消费者，而是正在将 AI 的地位重新定义为积极交流知识和进行训练的合作伙伴。

---

## 通俗易懂：AI 如何教导我们

Anthropic（开发 Claude 的人工智能公司）最近在 AI 教导人类的方式上做出了巨大改变。那就是在教育版 Claude（Claude for education）中全新引入了**“学习模式（Learning mode）”**。[为教育推出 Claude \ Anthropic](https://www.anthropic.com/news/introducing-claude-for-education)

### 从答案售货机变成“苏格拉底”
过去，如果你对 AI 说“请解一下这道数学题”，它会贴心地写下解题过程和正确答案。从学生的角度来看，这简直就是抄作业的万能作弊神器。但是新引入的“学习模式”则不同。它不会直接给你正确答案，而是引导推理过程本身，让学生培养批判性思维能力。简单来说，就是与其直接喂你吃答案，不如帮你咀嚼和消化。

打个比方，这就好比去健身房。一位真正优秀的顶级私人教练（PT）绝对不会替你举起沉重的杠铃。相反，他们会在一旁纠正你的姿势，并不断激励你，让你能以正确的姿势感受肌肉的刺激，自己把杠铃举起来。Claude 的学习模式就像这位资深教练一样。它会反问你：“你在哪里卡住了？”、“这个公式里的 x 代表什么？”，通过这样帮助学生自己流汗去寻找答案。

### 成为外语对话伙伴的 AI
事实上，教育领域正在充分利用这些特性。在美国东北大学（Northeastern University）教授初级和高级西班牙语的 Canavan 教授，利用为师生提供的免费高级 Claude 权限，制作了一个非常特别的定制聊天机器人。[这位教授是如何使用 Claude 教授西班牙语的](https://news.northeastern.edu/2026/04/22/claude-spanish-chatbot/)

学生们不再死记硬背教科书上刻板生硬的对话，而是用教授通过 Claude 制作的这个聊天机器人进行生动的西班牙语实战对话。想象一下。在与 AI 模拟马德里某家咖啡馆用西班牙语点咖啡的场景时，即使你犯了语法错误也无需感到尴尬。因为 AI 服务员不仅会自然地继续对话，还会非常友好地为你指正正确的表达方式。你相当于拥有了一个世界上最有耐心、随时随地都能召唤的母语朋友。

---

## 通俗易懂：我们如何教导 AI

如果说 AI 传授我们知识，那反过来我们能教给 AI 什么呢？那就是蕴含我们专业性的**“工作方式”**。

### 超越一次性指令的“技能（Skills）”
我们在平时使用 AI 时，通常会提出一次性的请求。比如“润色一下这封邮件”、“总结一下这份会议纪要”。只要提供充分的上下文并稍加指定输出格式，AI 在处理这些一次性任务或探索想法时就能表现得非常完美。[使用技能教 Claude 你的工作方式 | Claude](https://claude.com/resources/tutorials/teach-claude-your-way-of-working-using-skills)

但如果是每周重复的复杂团队会议准备，或者是格式和规则都有严格规定的周报撰写呢？每次都要输入长长的提示词并附加条件反而更繁琐。因此，**“技能（Skills）”**这个核心概念应运而生。技能是一份具体的指南，为 Claude 清晰地提供“程序性知识（Procedural knowledge，即按顺序完成某件事的方法）”，指导其如何完成特定任务或工作流。[什么是技能？ | Claude 帮助中心](https://support.claude.com/en/articles/12512176-what-are-skills)

### 工具箱（MCP）与烹饪食谱（Skills）
最近在 AI 业界，“模型上下文协议（MCP，让 AI 能够直接访问用户计算机文件或外部工具的连接桥梁）”成为了热门话题。那么，在功能上看起来很相似的 MCP 和技能（Skills）具体有什么区别呢？

举个非常简单的例子。想象一下你开了一家新餐厅，雇佣了一位刚刚从顶级烹饪学校毕业的主厨（AI）。
告诉这位主厨厨房里的刀具、案板、烤箱等烹饪工具的位置，并赋予他自由使用的权限，这就是 **MCP**。也就是说，相当于交给了他一个可以用来做菜的物理“工具箱”。
但是，拥有再好的工具，也不代表他马上就能煮出你们餐厅那道绝妙的泡菜汤。必须要有详细记录着是先炒肉还是后放泡菜、火候具体控制几分钟等步骤的“独门食谱”。这个独门食谱就是**技能（Skills）**。

当物理工具箱（MCP）与蕴含你独特窍门的烹饪法（Skills）相结合时，Claude 才能摆脱单纯的文本生成器的身份，成为完美理解并独立执行团队复杂策划工作流的真正同事。[为 Claude 构建技能的完整指南](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)

---

## 现状（Where We Stand）

这种“技能”功能已经走出了实验室，正迅速渗透到我们的日常生活和工作中。Anthropic 于 2025 年 10 月首次展示了技能（Skill）格式，在确认了它的潜力后，紧接着在 12 月以开放标准（Open standard，一种像智能手机充电接口一样可在各种设备上兼容的通用规格）的形式全面公开，供任何人自由使用。[GitHub - ComposioHQ/awesome-claude-skills: 精选列表...](https://github.com/ComposioHQ/awesome-claude-skills)

这带来了巨大的连锁反应。目前，该技能标准已不再局限于 Claude 的官方网站（Claude.ai）或 API。它在 Cursor、Gemini CLI、Windsurf 等受到全球无数开发者喜爱的各种编程和办公平台中得到了广泛支持。[2026 年 Claude（及任何编程智能体）必备的 10 项技能 | unicodeveloper | Medium](https://medium.com/@unicodeveloper/10-must-have-skills-for-claude-and-any-coding-agent-in-2026-b5451b013051) 用户能够将自己费尽心思制作的自动化工作秘籍（技能），直接拿到其他程序或服务中照样使用。

顺应这一趋势，人们现在不再盲目地向 AI 抛出问题，而是开始认真学习“正确教导和驾驭 AI 的方法”本身。除了简单的指令输入外，深入了解 AI 编程助手的底层架构、学习如何负责任地协调多步骤任务的专业课程（如《Claude Code 实战指南（Claude Code in Action）》、《Claude 协同工作入门（Introduction to Claude Cowork）》等）也如雨后春笋般涌现，并获得了热烈反响。[Claude Code 实战指南 - Anthropic 课程](https://anthropic.skilljar.com/claude-code-in-action)，[Claude 协同工作入门](https://anthropic.skilljar.com/introduction-to-claude-cowork)

普通用户也不例外。从基础开始扎实学习：何时该用在文本框中输入指令的基础方式，何时该用让 AI 自主协助工作的对话模式；我的重要文件的访问权限要开放到什么程度才安全等。大家都在努力培养与 AI 健康协作的能力，这是 2026 年当下最积极的风景线。[Claude Code 学习路径：实用的入门指南 | Daniel Avila | Medium](https://medium.com/@dan.avila7/claude-code-learning-path-a-practical-guide-to-getting-started-fcc601550476)

---

## 未来会怎样？（What's Next）

“如果 AI 抢了我的饭碗怎么办？”这是人工智能刚出现时，无数人心存的朦胧而巨大的恐惧。但是，看着 Claude 在教育领域展现出的“学习模式”，与革新办公环境的用户定制型“技能（Skills）”功能交织发展的过程，我们将要迎来的未来似乎会呈现出另一番景象。

在未来，我们早上来到公司，可以一边悠闲地喝着咖啡，一边像向刚入职的新员工交接工作一样，以“技能”的形式亲切地教导 AI 公司复杂的结算业务或是邮件撰写流程。[Claude 技能入门 | Claude 秘籍](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction) 

结束了一天的辛勤工作回到家后，我们也不会再深夜漫无目的地滑动社交媒体进行末日滚动，而是会问：“Claude，你能用连小学生都能听懂的有趣比喻，给我讲讲今天报纸上看到的量子计算机原理吗？”，以此来满足我们久违的纯粹求知欲。

随着蕴含我们专业窍门的技能被逐步加载（Progressively load）到各个设备中，通过开放标准在智能手机、办公笔记本电脑和平板电脑之间自由穿梭，AI 将成为浩瀚的知识海洋，以及完全为你量身打造、世界上独一无二的专属教练。在这种教与学的温馨双向互动中，人类和 AI 将不再是竞争对手，而是踏上一条互相成就、共同成长为更好伙伴的绝美共生之路。

---

## AI 的视角（AI's Take）

人工智能现在已不再是只冷冰冰地给出标准答案的机械百科全书。正如本文所探讨的，人工智能既是一位耐心地训练我们如何思考的优秀教练，同时也是一位像海绵一样吸收我们工作窍门和理念的能干后辈。

有趣的是，AI 提供的回答水平，最终取决于“我们提出的问题有多好，教导得有多精准”。在教导 AI 进行逻辑思考（Skills）的过程中，人类反而会反思并优化自己的工作方式。也就是说，为了更好地教导 AI，我们自己会成长为更优秀的导师，从而形成了一个良性循环。可以说，这个学习的工具正在引导我们成为更好的思考主体。

---

## 参考资料

1. [Claude，教我点什么](https://hugotunius.se/2025/10/26/claude-teach-me-something.html)
2. [为教育推出 Claude \ Anthropic](https://www.anthropic.com/news/introducing-claude-for-education)
3. [这位教授是如何使用 Claude 教授西班牙语的](https://news.northeastern.edu/2026/04/22/claude-spanish-chatbot/)
4. [使用技能教 Claude 你的工作方式 | Claude](https://claude.com/resources/tutorials/teach-claude-your-way-of-working-using-skills)
5. [什么是技能？ | Claude 帮助中心](https://support.claude.com/en/articles/12512176-what-are-skills)
6. [为 Claude 构建技能的完整指南](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)
7. [GitHub - ComposioHQ/awesome-claude-skills: 精选列表...](https://github.com/ComposioHQ/awesome-claude-skills)
8. [2026 年 Claude（及任何编程智能体）必备的 10 项技能 | unicodeveloper | Medium](https://medium.com/@unicodeveloper/10-must-have-skills-for-claude-and-any-coding-agent-in-2026-b5451b013051)
9. [Claude Code 实战指南 - Anthropic 课程](https://anthropic.skilljar.com/claude-code-in-action)
10. [Claude 协同工作入门](https://anthropic.skilljar.com/introduction-to-claude-cowork)
11. [Claude Code 学习路径：实用的入门指南 | Daniel Avila | Medium](https://medium.com/@dan.avila7/claude-code-learning-path-a-practical-guide-to-getting-started-fcc601550476)
12. [Claude 技能入门 | Claude 秘籍](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction)