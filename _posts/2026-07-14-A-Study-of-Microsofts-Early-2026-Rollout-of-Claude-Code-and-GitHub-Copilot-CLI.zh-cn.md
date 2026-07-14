---
layout: post
title: "微软为何选择自家的Copilot CLI，而非AI编码工具Claude Code？"
description: "微软正在将数千名工程师从Anthropic的Claude Code转向其自家的GitHub Copilot CLI。高昂的成本和实现AI工具的自主性是主要原因。"
summary: "为了节约成本和实现AI自主，微软正将其工程师从Anthropic的Claude Code转向自家的GitHub Copilot CLI。"
tags: [AI, 编码, 微软, GitHubCopilotCLI, ClaudeCode, 成本节约, 技术战略]
image_alt: "电脑屏幕显示AI编码工具的代码，旁边是微软徽标和GitHub Copilot CLI徽标的图片"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "科技巨头对AI工具的选择不仅仅是成本问题。这清晰地表明了他们争取AI生态系统主导权的战略举措。"
quiz:
  - question: "微软从Anthropic的Claude Code转向GitHub Copilot CLI的主要原因是什么？"
    choices: ["Claude Code的性能较低", "Claude Code成本高昂", "GitHub Copilot CLI功能有限", "与Anthropic关系恶化"]
    answer: 1
    explanation: "微软正因为使用Claude Code的高昂成本而转向其自家的GitHub Copilot CLI [来源 5, 来源 7]。"
  - question: "微软此次AI编码工具转换预计何时完成？"
    choices: ["2026年3月30日", "2026年4月30日", "2026年6月30日", "2026年12月31日"]
    answer: 2
    explanation: "微软计划在2026年6月30日之前将Experiences + Devices工程师从Claude Code转向GitHub Copilot CLI [来源 3, 来源 7]。"
  - question: "文章中提到，在组织层面，AI编码工具的Token使用成本每年可能达到多少？"
    choices: ["数十万美元", "数百万美元", "数千万美元", "数亿美元"]
    answer: 1
    explanation: "在组织层面，代理型命令行工具的Token使用成本每年可能高达数百万美元 [来源 1, 来源 2]。"
lang: zh-cn
ref: 2026-07-14-A-Study-of-Microsofts-Early-2026-Rollout-of-Claude-Code-and-GitHub-Copilot-CLI
---

# 微软为何选择自家的Copilot CLI，而非AI编码工具Claude Code？

想象一下，你身边有一个人工智能（AI）助手，能快速帮助你完成复杂的编码任务。最近，在软件开发行业，这种AI编码工具变得越来越普遍，特别是像微软（Microsoft）这样的科技巨头也积极利用它们。然而，最近有消息称，微软正在减少内部使用的Anthropic的AI编码工具“Claude Code”，并大规模转向自家的“GitHub Copilot CLI” [来源 3, 来源 4]。微软为何做出这一决定？这仅仅是内部政策的改变，还是预示着AI市场大趋势的重要信号？

## 这为何重要？

这条消息对我们非专业人士来说也具有很大的启示。首先，它表明AI技术的“成本”问题比想象中更为严重。微软减少使用Claude Code的主要原因据说是“成本高昂” [来源 5, 来源 7]。简而言之，就像父母因为高昂的学费而选择在家亲自教孩子一样，大型企业也感受到了AI工具使用费的压力。在组织层面，代理型命令行工具（Agentic Command Line Tools，指接收用户命令并自主执行复杂任务的AI工具）的“Token使用”成本每年可能高达数百万美元 [来源 1, 来源 2]。这里的“Token”是AI处理文本的最小单位，我们使用的单词或句子都会被转换为Token进行计算。使用AI越多，Token成本就越高。实际上，像Uber这样的公司也曾经历过AI预算一度超过12亿美元的情况 [来源 7]。因此，这些看不见的AI使用费可能达到天文数字，这对企业来说是一个非常重要的考量因素。

其次，这显示出企业在AI技术上寻求“自主”的战略性举动。微软现在更倾向于使用自主开发的AI工具，而非依赖外部AI工具，以此来 확보技术主导权 [来源 6]。这成为了预测AI市场竞争格局将如何变化的重要指标。打个比方，这就像一家汽车公司从外部采购主要零部件转向自主生产，以降低成本并确保技术独立性。这种将AI技术核心能力内化于企业的举动，未来可能会成为许多企业效仿的战略方向。

## 简单理解

那么，微软正在减少使用的“Claude Code”和新转向的“GitHub Copilot CLI”究竟是什么呢？

“Claude Code”是Anthropic开发的基于AI的编码助手。它是一种帮助开发人员高效执行代码编写、调试、文档编制等各种编码任务的工具 [来源 8, 来源 13]。可以把它比作一位经验丰富的程序员在你身边指导你编写代码或查找错误。开发人员通过Claude Code能够更快、更准确地完成代码。

另一方面，“GitHub Copilot CLI”是微软收购的GitHub提供的AI编码工具。“CLI”是Command Line Interface（命令行界面）的缩写，指的是通过键盘直接输入命令来与计算机交互的方式，而不是使用鼠标的图形界面（GUI）。GitHub Copilot已经因其在代码编辑器（如Visual Studio Code）中自动完成代码的功能而闻名 [来源 9]，而“CLI”版本则更进一步，在命令行环境中充当辅助整体编码任务的代理角色 [来源 8]。可以把它想象成一个多功能工作台，将编码所需的各种工具汇集一处。GitHub Copilot CLI支持开发人员直接在命令行中获得AI的帮助，生成和管理代码。

微软从Claude Code转向GitHub Copilot CLI不仅仅是简单地将外部产品替换为自家产品。微软计划在2026年6月30日之前，将数千名Experiences + Devices工程师从Claude Code转移到GitHub Copilot CLI [来源 3, 来源 7]。这是一个巨大的战略布局，旨在内部解决巨额的AI使用成本，并强化其自身的AI技术生态系统 [来源 5, 来源 6]。这就像电影制片公司不再依赖昂贵的外部特效工作室，而是利用自家的特效团队，从而降低成本，提高成片的质量和控制力。这一举动表明微软致力于在AI领域进一步巩固其影响力。

## 当前情况

微软目前正在取消Anthropic的Claude Code许可证，并引导工程师使用GitHub Copilot CLI [来源 5, 来源 6, 来源 7]。预计这项内部转换将在2026年6月30日之前完成 [来源 3, 来源 7]。这一过程不仅仅是工具的更换，更将成为大型组织重新评估AI引入的经济可行性和战略重要性的重要案例 [来源 1, 来源 2]。对于工程师来说，他们将面临适应新工具而非原有熟悉AI工具的挑战，但从长远来看，他们将在微软生态系统内获得更加整合的AI体验。这一变化有望提高微软内部开发工作流程的效率并优化成本。

## 未来展望

微软的这一决定预计将对AI编码工具市场产生巨大影响。其他企业在引入AI工具时，也将更加重视成本效益和自身技术能力的强化。这将促使AI服务提供商在价格竞争的同时，提供差异化的价值；同时，拥有自主AI开发能力的企业将有机会巩固市场主导地位。此外，开发人员在选择各种AI编码工具时，将面临更深入的思考。判断是依附于特定企业的生态系统，还是灵活运用多种工具，将变得更加重要。最终，这些变化将进一步加速AI编码工具的进步和创新。

## AI的视角

MindTickleBytes AI记者视角：微软的AI编码工具转换清晰地表明，随着AI技术逐渐成为产业的核心基础设施，“内化”和“成本效益”正成为企业战略的重要支柱。这不仅仅是简单的工具替换，更可以解读为科技巨头们旨在掌控AI生态系统主导权、在未来技术竞争中占据优势的深刻战略举措。
<br>

## 参考资料

1.  [2607.01418] Adoption and Impact of Command-Line AI Coding ... [https://arxiv.org/abs/2607.01418](https://arxiv.org/abs/2607.01418)
2.  Adoption and Impact of Command-Line AI Coding Agents: A Study ... [https://arxiv.org/pdf/2607.01418v1](https://arxiv.org/pdf/2607.01418v1)
3.  Microsoft Shifts Engineers from Claude Code to GitHub Copilot CLI [https://winbuzzer.com/2026/05/15/microsoft-starts-canceling-claude-code-licenses-xcxwbn/](https://winbuzzer.com/2026/05/15/microsoft-starts-canceling-claude-code-licenses-xcxwbn/)
4.  GitHub Copilot CLI vs Claude Code: Enterprise Pick (June 2026) [https://andrew.ooo/answers/github-copilot-cli-vs-claude-code-enterprise-june-2026/](https://andrew.ooo/answers/github-copilot-cli-vs-claude-code-enterprise-june-2026/)
5.  Microsoft Cancels Claude Code Licenses, Shifts Engineers to ... [https://www.linkedin.com/pulse/microsoft-cancels-claude-code-licenses-shifts-engineers-john-cloud-lvd6c](https://www.linkedin.com/pulse/microsoft-cancels-claude-code-licenses-shifts-engineers-john-cloud-lvd6c)
6.  Microsoft Ends Claude Code Licenses As It Shifts Developers ... [https://www.forbes.com/sites/jonmarkman/2026/06/01/microsoft-ends-claude-coda-licenses-as-it-pushes-copilot-cli/](https://www.forbes.com/sites/jonmarkman/2026/06/01/microsoft-ends-claude-coda-licenses-as-it-pushes-copilot-cli/)
7.  Microsoft Cancels Claude Code Licenses, Pushes Engineers to ... [https://opentools.ai/news/microsoft-cancels-claude-code-licenses-copilot-cli](https://opentools.ai/news/microsoft-cancels-claude-code-licenses-copilot-cli)
8.  GitHub- anthropics/claude-code:ClaudeCodeis an agenticcoding... [https://github.com/anthropics/claude-code](https://github.com/anthropics/claude-code)
9.  Set upGitHubCopilotin VSCode [https://code.visualstudio.com/docs/setup/copilot](https://code.visualstudio.com/docs/setup/copilot)
13. ClaudeCodeCLI: Install on Mac/Windows, winget... | Inventive HQ [https://inventivehq.com/knowledge-base/claude/how-to-install-claude-code-cli](https://inventivehq.com/knowledge-base/claude/how-to-install-claude-code-cli)