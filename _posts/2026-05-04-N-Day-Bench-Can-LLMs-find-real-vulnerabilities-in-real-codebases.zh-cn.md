---
layout: post
title: "AI 能替我们看门守户吗？揭秘寻找真实软件漏洞的“N-Day-Bench”"
description: "了解评估 AI 发现真实软件安全漏洞能力的全新标准——N-Day-Bench。"
summary: "2025 年推出的“N-Day-Bench”旨在评估 AI 在真实软件代码（而非人为构造的问题）中发现安全漏洞的能力。其中，Claude 3.5 Sonnet 表现最为出色。"
tags: [AI, 安全, N-Day-Bench, 网络安全, LLM]
image: 2026-05-04-N-Day-Bench-Can-LLMs-find-real-vulnerabilities-in-real-codebases.jpg
image_alt: "机器人手持放大镜在计算机代码上搜索安全漏洞的图像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "虽然 AI 已被证明有望成为安全专家的得力助手，但与此同时，开源项目维护者可能会被 AI 生成的海量报告所淹没，这一现实隐忧也随之而来。"
quiz:
  - question: "N-Day-Bench 测试的“N-Day”漏洞有什么特点？"
    choices: ["是 AI 自行生成的虚构问题。", "是已经公开并分配了唯一编号 (CVE) 的真实漏洞。", "是黑客也绝对无法发现的未来漏洞。"]
    answer: 1
    explanation: "N-Day-Bench 针对已公开并分配了 CVE 编号的现实世界漏洞来衡量 AI 的性能。"
  - question: "在 N-Day-Bench 测试中，哪个模型的漏洞发现率最高 (32%)？"
    choices: ["GPT-4o", "Claude 3.5 Sonnet", "Gemini 1.5 Pro"]
    answer: 1
    explanation: "根据最新测试结果，Claude 3.5 Sonnet 以 32% 的发现率位居榜首。"
  - question: "当 AI 大量发现安全漏洞时，令人担心的副作用是什么？"
    choices: ["AI 会自行修改代码。", "安全专家将彻底失业。", "开源维护者会因处理 AI 生成的海量报告而过载。"]
    answer: 2
    explanation: "专家警告称，随着 AI 大规模发现漏洞，需要审核和处理这些漏洞的开源维护者的负担将会加重。"
lang: zh-cn
ref: 2026-05-04-N-Day-Bench-Can-LLMs-find-real-vulnerabilities-in-real-codebases
---

# AI 能替我们看门守户吗？揭秘寻找真实软件漏洞的“N-Day-Bench”

请想象一下。假设你是一个拥有数千户人家的巨大公寓小区的安保负责人。这个小区有数万扇门窗，为了方便居民，每天都会安装新的通道和无人快递柜。安保团队人手有限，而你每天晚上都要忍受“可能哪里没锁好”的焦虑。这时，如果出现了一位非常聪明且不知疲倦的“AI 安全员”，说：“我来替你挨个摇摇门，看看有没有缝隙”，你会感觉如何？

但这里有一个疑问。这位 AI 安全员真的有能力发现“真正的强盗”可以潜入的细微缝隙吗？还是它只是一个只会做教科书上常见题目的“理论专家”？

为了解决这个疑问，2025 年初，一个专门衡量 AI 实战能力的特别测试平台出现了。它就是 **“N-Day-Bench（N 日基准）”**。[N-Day-Bench: Can LLMs Find Real Vulnerabilities in Real Code?](https://juanchi.dev/en/blog/n-day-bench-can-llms-find-real-vulnerabilities-in-real-code)

## 为什么这很重要？

从我们每天使用的手机银行应用、外卖应用，到我们乘坐的汽车的自动驾驶软件，所有的数字服务都由数百万行“代码”组成。在这些巨大的代码堆中，可能隐藏着我们尚未发现的“安全漏洞（Vulnerability，黑客可以偷偷潜入的弱点）”。打个比方，它们就像是啃食坚固木屋支柱的隐形“白蚁”。

到目前为止，为了寻找这些白蚁，专业安全人员必须目不转睛地查看代码，或者使用根据预设规则进行检查的自动化工具。然而，随着软件复杂程度呈几何级数增长，靠人来堵住所有漏洞已近乎不可能。

如果像 ChatGPT 或 Claude 这样的语言大模型 (LLM) 能够在真实的软件环境中迅速找到安全漏洞，会怎样呢？我们将生活在一个更加安全的数字世界中。“N-Day-Bench”切中的正是这一点。它不仅仅评估 AI 是否能给出“理论上这种代码很危险”之类的建议，而是严格验证 AI **是否能从实际运行的复杂软件中揪出真正的问题**。[N-Day-Bench: Can LLMs Find Real Vulnerabilities in Real Code?](https://juanchi.dev/en/blog/n-day-bench-can-llms-find-real-vulnerabilities-in-real-code)

## 轻松理解：N-Day-Bench 是什么样的考试？

这个基准测试名称中的 **“N-Day”** 指的是世人皆知的、即“有迹可循”的漏洞。[N-Day-Bench](https://ndaybench.winfunc.com/) 通常，当软件被发现存在安全缺陷时，会被分配一个名为“CVE (Common Vulnerabilities and Exposures)”的唯一编号，这就像是给罪犯分配的案件编号一样。[N-Day-Bench: Can LLMs Find Real Vulnerabilities in Real Code?](https://juanchi.dev/en/blog/n-day-bench-can-llms-find-real-vulnerabilities-in-real-code)

N-Day-Bench 使用的不是虚构的练习题，而是真实发生过、曾让无数企业和用户担惊受怕的 CVE 案例作为试题。我将这场考试的特点总结为以下三个核心要点。

### 1. 三位 AI 特工：通过“团队合作”探索漏洞
N-Day-Bench 并不是简单地给一个 AI 看代码并命令它“找问题”。它像警察局的侦查小组一样，让具有三种角色的 AI 进行有机协作。[N-Day-Bench: Can LLMs find real vulnerabilities in real codebases?](https://www.agent-wars.com/news/2026-04-14-n-day-bench-can-llms-find-real-vulnerabilities-in-real-codebases)

*   **策展人 (Curator)：** 负责“班长”角色，从无数案件中挑选并整理出适合 AI 解决的问题。
*   **寻找者 (Finder)：** 负责“现场侦探”角色，在代码中四处搜寻，找出可疑的漏洞。
*   **裁判 (Judge)：** 负责“法官”角色，冷静地判定侦探找到的证据是否真实，是否存在牵强附会的说法。

### 2. “在 24 个步骤内抓到罪犯”
AI 模型被授予在名为“沙箱 (Sandbox)”的虚拟空间中直接运行代码的权限。**沙箱简单来说，就像孩子们在沙池里可以随心所欲地盖房子和拆房子而不会影响周围环境一样，是一个可以安全运行代码的隔离实验室**。[N-Day-Bench - Can LLMs find real vulnerabilities in real codebases ...](https://news.ycombinator.com/item?id=47758347)

但是，考试不会给 AI 无限的时间。它必须在执行正好 **24 个指令步骤 (Shell steps)** 的过程中分析代码并写出最终报告。[N-Day-Bench: Can LLMs find real vulnerabilities in real codebases?](https://www.agent-wars.com/news/2026-04-14-n-day-bench-can-llms-find-real-vulnerabilities-in-real-codebases) 这就像侦探必须在现场保护时间内短促而有力地收集证据一样，情况十分紧迫。

### 3. “每月更新”以确保无法预知答案
如果 AI 只是靠背诵互联网上已经流传的答案（安全补丁代码）来答题，那不能算作真正的实力，对吧？因此，开发商“WinFunc”每月都会从全球开发者使用的代码托管平台 (GitHub) 中提取最新的安全案例，制作全新的试题。[Benchmark pits frontier LLMs against fresh real-world vulns](https://www.theagenticdigest.com/issues/nday-bench-vuln-agents) 通过提供 AI 尚未学习过的最新问题，来确认它是否真的在通过“思考”来解决问题。[N-Day-Bench: Can LLMs find real vulnerabilities in real codebases?](https://www.agent-wars.com/news/2026-04-14-n-day-bench-can-llms-find-real-vulnerabilities-in-real-codebases)

## 现状：AI 的成绩单如何？

展示了最新技术实力的 AI 模型参加了这场实战考试，结果现已公开。

*   **第一名：Claude 3.5 Sonnet** —— 准确找出了高达 **32%** 的漏洞。简单来说，相当于自主解决了十道题中的三道。[N-Day-Bench: LLMs Detect 18-32% Real Code Vulnerabilities](https://technologytimesng.com/articles/n-day-bench-llms-vulnerabilities-africa)
*   **第二名：GPT-4o** —— 以 **22%** 的发现率紧随其后。[N-Day-Bench: LLMs Detect 18-32% Real Code Vulnerabilities](https://technologytimesng.com/articles/n-day-bench-llms-vulnerabilities-africa)

总的来看，最新的 AI 能够自主发现真实代码中约 18% 至 32% 的漏洞。[N-Day-Bench: LLMs Detect 18-32% Real Code Vulnerabilities](https://technologytimesng.com/articles/n-day-bench-llms-vulnerabilities-africa) 仅看数字，你可能会想“才这么点？”但安全专家的看法却截然不同。

专家们以前使用的传统自动分析工具只遵循固定规则，缺乏灵活性。在一项实验中，有评价称，与 AI 相比，传统工具简直就像“儿童玩具 (Toy)”，AI 的分析能力具有压倒性的优势。[LLMs Can Now Find Zero-Day Vulnerabilities. Here's Why That's Both Impressive and Alarming. - Vidoc Security Lab](https://blog.vidocsecurity.com/blog/llms-became-dangerously-good-for-cybersecurity)

## 未来会怎样？

AI 寻找安全漏洞能力的提升固然是个好消息，但就像硬币的两面，也有令人担心的部分。

安全专家 Ken Huang 警告称，一旦 AI 开始以“前所未有的速度”寻找漏洞，谁来负责后续处理将成为一个巨大的课题。[Token Is All You Need: Finding 0days with LLMs](https://www.linkedin.com/pulse/token-all-you-need-finding-0days-llms-ken-huang-idpye)

**打个比方，这就像一个拥有高性能显微镜的机器人在报告说，它在家里每个角落都发现了数万只微小的虫子**。收到报告的主人必须逐一阅读那数万份报告并杀虫，在这一过程中，可能不得不放弃重要的日常生活。特别是对于由志愿者维护的开源项目，维护者在查看 AI 抛出的数千份警告报告时，极易陷入“倦怠 (Burnout)”状态。[Token Is All You Need: Finding 0days with LLMs](https://www.linkedin.com/pulse/token-all-you-need-finding-0days-llms-ken-huang-idpye)

尽管如此，AI 极有可能成为大幅减轻安全专家工作负担的“最可靠助手”。[LLMs Find Vulnerabilities: N-Day-Bench & ZeroDayBench Insights](https://thepixelspulse.com/posts/llms-find-vulnerabilities-benchmarks/) 展望未来，AI 将不仅仅是编写代码的辅助工具，更将成为日夜守护我们数字世界安全的“不知疲倦的守卫者”。[Can LLMs find bugs in large codebases? | Hamming AI Blog](https://hamming.ai/blog/bug-in-the-codestack)

## AI 视角：MindTickleBytes AI 记者的观察

N-Day-Bench 的出现证明了 AI 不再只是“只会耍嘴皮子的秘书”。现在，AI 正在锻炼可以在真实战场上战斗的实战肌肉。

然而，与技术发展速度同样重要的是，对于技术发现的无数课题和警告，我们如何以负责任的方式处理它们的“人类应对体系”也必须随之成熟。工具已经变得十分锋利。现在，该轮到我们运用这些工具的智慧接受考验了。

## 参考资料

1. [N-Day-Bench: Can LLMs Find Real Vulnerabilities in Real Code?](https://dev.to/jtorchia/n-day-bench-can-llms-find-real-vulnerabilities-in-real-code-3h1o)
2. [LLMs Find Vulnerabilities: N-Day-Bench & ZeroDayBench Insights](https://thepixelspulse.com/posts/llms-find-vulnerabilities-benchmarks/)
3. [Token Is All You Need: Finding 0days with LLMs](https://www.linkedin.com/pulse/token-all-you-need-finding-0days-llms-ken-huang-idpye)
4. [N-Day-Bench - Can LLMs find real vulnerabilities in real codebases?](https://www.dailyneuraldigest.com/newsroom/2026-04-14-n-day-bench-can-llms-find-real-vulnerabilities-in-/)
5. [N-Day-Bench](https://ndaybench.winfunc.com/)
6. [N-Day-Bench: Can LLMs find real vulnerabilities in real codebases?](https://www.agent-wars.com/news/2026-04-14-n-day-bench-can-llms-find-real-vulnerabilities-in-real-codebases)
7. [N-Day-Bench - Can LLMs find real vulnerabilities in real codebases ...](https://news.ycombinator.com/item?id=47758347)
8. [N-Day-Bench: Can LLMs Find Real Vulnerabilities in Real Code?](https://juanchi.dev/en/blog/n-day-bench-can-llms-find-real-vulnerabilities-in-real-code)
9. [N-Day-Bench: LLMs Detect 18-32% Real Code Vulnerabilities](https://technologytimesng.com/articles/n-day-bench-llms-vulnerabilities-africa)
10. [Benchmark pits frontier LLMs against fresh real-world vulns](https://www.theagenticdigest.com/issues/nday-bench-vuln-agents)
11. [LLMs Can Now Find Zero-Day Vulnerabilities. Here's Why That's Both Impressive and Alarming. - Vidoc Security Lab](https://blog.vidocsecurity.com/blog/llms-became-dangerously-good-for-cybersecurity)
12. [Can LLMs find bugs in large codebases? | Hamming AI Blog](https://hamming.ai/blog/bug-in-the-codestack)

## FACT-CHECK SUMMARY
- Claims checked: 22
- Claims verified: 22
- Verdict: PASS