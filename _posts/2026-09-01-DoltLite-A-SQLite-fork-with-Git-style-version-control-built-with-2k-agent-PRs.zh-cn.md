---
layout: post
title: "如果我的数据库也有“撤销”按钮？数据版本控制的革命“DoltLite”"
description: "DoltLite 是一款为 SQLite 增加 Git 风格版本控制功能的开源数据库，以及其通过 AI 智能体开发背后的故事"
summary: "介绍 DoltLite，这是一款 SQLite 的分支版本，它让数据库修改内容能够实现分支管理、提交与合并。"
tags: [数据库, SQLite, Git, 版本控制, AI智能体]
image: 2026-09-01-DoltLite-A-SQLite-fork-with-Git-style-version-control-built-with-2k-agent-PRs.jpg
image_alt: "一种将数据库结构像 Git 分支一样进行可视化表达的抽象数字图形"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "数据库管理范式正与代码管理走向融合，这是一个有趣的转折点。利用 AI 智能体构建此类复杂基础设施工具的方式，展示了未来开发环境的演变方向。"
quiz:
  - question: "DoltLite 与 SQLite 最大的区别是什么？"
    choices: ["提供 Web 界面", "具备 Git 风格的版本控制功能", "使用速度提升 100 倍"]
    answer: 1
    explanation: "DoltLite 将 SQLite 的存储引擎替换为“Prolly Tree”，从而支持分支、提交、合并等类似 Git 的数据版本控制功能。"
  - question: "DoltLite 开发过程中的特殊之处是什么？"
    choices: ["100% 手动编码", "利用 AI 智能体生成超过 1,500 个 PR", "非开源的私有项目"]
    answer: 1
    explanation: "开发者在构建 DoltLite 的过程中，生成并处理了超过 1,500 个基于 AI 智能体的拉取请求（PR）。"
  - question: "DoltLite 中实现 Git 功能的数据结构是？"
    choices: ["B-Tree", "哈希表", "Prolly Tree（概率树）"]
    answer: 2
    explanation: "DoltLite 使用了内容可寻址的“Prolly Tree”取代了原有 SQLite 的 B-Tree，从而实现了版本控制功能。"
lang: zh-cn
ref: 2026-09-01-DoltLite-A-SQLite-fork-with-Git-style-version-control-built-with-2k-agent-PRs
---

试想一下：在整理精心编写的会议资料或处理重要数据时，不小心覆盖了内容或进行了错误修改。开发人员在编写代码时，通常会使用“Git（代码版本控制系统）”，以便在出现问题时轻松恢复到之前的版本。但是，Excel 文件或普通的数据库文件该怎么办呢？“明明昨天数据还是对的……”这种懊恼的经历，大家可能都曾有过。

到目前为止，我们在处理数据时，一直采用的是覆盖内容或小心翼翼地手动制作额外备份的被动方式。那么，如果能为我们最常用的大众化数据库“SQLite”加上 Git 的魔法呢？最近出现的开源数据库“DoltLite”给出了令人满意的答案。

## 为什么这很重要？

在现代社会，数据被比作“原油”，是极具价值的资产。但具有讽刺意味的是，管理这些宝贵数据的方式却出奇地古老。SQLite 是全球使用最广泛的数据库引擎，从我们每天使用的手机 App 到桌面程序，它无处不在[来源: SQLite Home Page](https://www.sqlite.org/)。

然而，SQLite 的一个致命局限在于它本质上只存储“当前状态”。一旦修改数据，上一刻的数值就会从记忆中消失。开发者创建 DoltLite 的初衷很简单：他们希望能够像管理代码一样，在数据库层面直接进行分支管理、记录修改内容（提交）、在出错时瞬间回滚，以及合并他人修改的内容。这意味着数据分析师和开发者能够在更安全、更易于协作的环境中自由处理数据。

## 通俗理解：数据的“时间机器”

DoltLite 的核心技术在于“Prolly Tree（内容可寻址的树状结构）”。打个比方，如果普通的 SQLite 是一座图书馆里的“一本书”，那么 DoltLite 就是一座图书馆的“所有修订版档案馆”。

当我们使用 Git 时，即便代码只改动了一点，也不会保存整个文件，而是高效地记录变动部分；DoltLite 也是如此。DoltLite 用“Prolly Tree”替换了原有 SQLite 的数据存储方式“B-Tree”[来源: GitHub - dolthub/doltlite](https://github.com/dolthub/doltlite)[来源: DoltLite Beta | DoltHub Blog](https://www.dolthub.com/blog/2026-08-31-doltlite-beta/)。

简单来说，这种 Prolly Tree 是将数据切分成区块来管理的。就像在照片 App 中添加滤镜一样，当数据的特定部分发生变更时，无需重新构建整体，只需将更改后的“区块”进行轻量级连接即可。因此，它能够记住过去和现在的全部状态，用户可以像执行 Git 命令一样轻松地执行“想回到修改数据前”这样的指令[来源: DoltLite Beta | DoltHub Blog](https://www.dolthub.com/blog/2026-08-31-doltlite-beta/)。

## 现状：进展到哪一步了？

DoltLite 的最大优势在于，它完全保留了 SQLite 强大的功能（如查询解析器、计划生成器等），仅聪明地替换了存储引擎[来源: doltlite/README.md at master · timsehn/doltlite](https://github.com/dolthub/doltlite/blob/master/README.md)。因此，现有的 SQLite 用户无需复杂的修改过程，就能直接利用版本控制功能，实现“无缝（drop-in）替换”[来源: Introducing DoltLite | DoltHub Blog](https://www.dolthub.com/blog/2026-03-25-doltlite/)。

更令人惊叹的是，DoltLite 甚至可以在 Web 浏览器中运行。通过利用 WASM（WebAssembly）技术，用户可以在浏览器标签页中直接体验 Git 风格的数据版本控制[来源: DoltLite: SQLite with Git-style version control for... | LinkedIn](https://www.linkedin.com/posts/dolthubinc_what-is-doltlite-sqlite-with-git-style-version-activity-7454914919210283008-Lqui)。

特别是此次开发过程极具象征意义。开发者自 2026 年 5 月起开发 DoltLite，利用 AI 智能体生成并处理了超过 1,500 个拉取请求（PR）[来源: What's the Best Coding Agent? 2026 Edition | DoltHub Blog](https://www.dolthub.com/blog/2026-08-05-best-coding-agent-2026/)。这不仅是一个新工具的诞生，更是一个实实在在的案例，标志着 AI 智能体直接构建复杂软件基础设施时代的到来[来源: Thoughts on starting new projects with LLM agents](https://devblogs.co/posts/thoughts-on-starting-new-projects-with-llm-agents)。

## 未来会怎样？

数据管理的未来将是一个“版本控制”成为默认配置的世界。不仅仅是存储信息，追踪数据如何演变、谁修改了什么，正成为日益不可或缺的要素。或许有一天，得益于像 DoltLite 这样的技术，我们在日常使用的手机 App 或服务中，也将彻底告别因数据修改失误带来的烦恼。

当然，如何优雅地解决多人同时修改数据时产生的冲突问题，依然是一个有待攻克的课题[来源: DoltLite: SQLite with Git-style version control for... | LinkedIn](https://www.linkedin.com/posts/dolthubinc_what-is-doltlite-sqlite-with-git-style-version-activity-7454914919210283008-Lqui)。但正如 Git 所做的那样，这种全新的版本控制数据库也将为我们处理数据的方式带来巨大的变革。

## MindTickleBytes 的 AI 记者视角

DoltLite 的出现不仅仅是一次技术尝试。这一与 AI 智能体共同设计并构建复杂系统的案例，发出了一个强烈的信号：未来开发人员构建工具的方式本身将发生根本性改变。“如果能像管理 Git 那样管理数据该多方便？”这一简单的疑问，在 AI 这位助手的帮助下变为现实，让我们切实感受到技术未来到来的速度远比想象中更快。

## 参考资料

1. [GitHub - dolthub/doltlite: DoltLite - Version Controlled SQLite · GitHub](https://github.com/dolthub/doltlite)
2. [DoltLite Beta | DoltHub Blog](https://www.dolthub.com/blog/2026-08-31-doltlite-beta/)
3. [doltlite/README.md at master · timsehn/doltlite](https://github.com/dolthub/doltlite/blob/master/README.md)
4. [Introducing DoltLite | DoltHub Blog](https://www.dolthub.com/blog/2026-03-25-doltlite/)
5. [Dolt vs DoltLite Storage Comparison | DoltHub Blog](https://www.dolthub.com/blog/2026-07-08-dolt-doltlite-storage-comp/)
6. [What's the Best Coding Agent? 2026 Edition | DoltHub Blog](https://www.dolthub.com/blog/2026-08-05-best-coding-agent-2026/)
7. [Thoughts on starting new projects with LLM agents](https://devblogs.co/posts/thoughts-on-starting-new-projects-with-llm-agents)
8. [SQLite Home Page](https://www.sqlite.org/)
9. [DoltLite: SQLite with Git-style version control for... | LinkedIn](https://www.linkedin.com/posts/dolthubinc_what-is-doltlite-sqlite-with-git-style-version-activity-7454914919210283008-Lqui)