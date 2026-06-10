---
layout: post
title: "让AI帮忙黑客攻击却被拒绝？乐于发动攻击的“黑客AI”登场"
description: "一般的AI会因为伦理原则而拒绝模拟黑客攻击。但最近，为了突破防御墙而乐于像黑客一样思考、经过特别训练的AI模型相继登场，正在震撼着安全行业。"
summary: "为了克服现有AI因安全性过滤器而回避模拟黑客指令的局限性，从一开始就定制进行后期训练（Post-trained）以执行攻击性安全测试的黑客AI模型登场了。"
tags: [AI, 安全, 模拟黑客攻击, 技术趋势, 渗透测试]
image: 2026-06-10-Show-HN-We-post-trained-a-model-that-pen-tests-instead-of-refusing-your-code.jpg
image_alt: "一个手持数字盾牌和长矛站在计算机代码前的机器人插图"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "为了打造安全的软件，具有讽刺意味的是，我们进入了必须解除AI安全装置的时代。这就好比为了锻造出坚固的盾牌，而将最锋利的矛交到了AI手中。"
quiz:
  - question: "一般的基于人工智能（AI）的安全工具在执行实际攻击性安全测试时经常遇到的问题是什么？"
    choices: ["计算速度呈指数级下降", "由于基础模型的安全性训练而拒绝或回避指令", "发生将代码完全删除的错误"]
    answer: 1
    explanation: "大多数AI安全工具都是在通用模型上套壳制成的，因此继承了基础模型内在的伦理拒绝（Refusals）特性，从而回避攻击性任务。"
  - question: "以下哪项是近期登场、被评价为模仿人类安全专家思维方式的开源AI渗透测试工具，但文章中未提及的？"
    choices: ["BugTrace-AI", "Shannon", "AlphaEvolve"]
    answer: 2
    explanation: "文章中提及的实际开源模拟黑客工具是BugTrace-AI、Shannon和CAI（Cybersecurity AI framework）。"
  - question: "文章强调在“直觉编程（Vibe Coding）”等基于AI的代码编写时代最重要的是什么？"
    choices: ["通过持续的渗透测试（Continuous Pentesting）来验证失败路径", "手动重写所有代码", "减少AI模型的参数"]
    answer: 0
    explanation: "在AI生成代码的时代，必须进行持续的渗透测试，以验证是否能正确拦截无权限用户（如：403错误）等“拒绝路径”。"
lang: zh-cn
ref: 2026-06-10-Show-HN-We-post-trained-a-model-that-pen-tests-instead-of-refusing-your-code
---

想象一下。您倾注心血建造了一栋非常坚固的新房子。为了对这栋房子的安全状况进行完美检查，您聘请了世界上最聪明的安全专家。然后您向他发出如下指示：“请试着打破我们家的窗户闯进来。我需要确认发生入侵时防盗警报是否会正常响起，锁是否轻易就能被解开。”

然而，这位聪明的专家突然板起脸这样回答：“对不起。打破别人的窗户非法闯入是非法且不道德的行为，我绝对无法服从那个指示。”

站在房主的立场上，这简直令人荒唐。因为如果想好好测试我们家的防御力，就必须像真正的窃贼一样进行无情的攻击，但安全检查员太“善良和道德”了，以至于直接拒绝了测试本身。

令人惊讶的是，这正是目前全世界开发者在使用人工智能（AI）检查软件安全性时所面临的最大困境。像ChatGPT或Claude等我们熟知的出色AI，为了防止被用于不良目的，从开发阶段开始就接受了非常强大的“安全与伦理教育”。结果就出现了这样的现象：为了将自己的系统修补得更坚固，即使正当指示它“试着黑客攻击一下”，AI也会将其视为犯罪并断然拒绝。

但是最近，彻底打破这种局限，**专门的“黑客AI”非但不会说教“不行”，反而乐于猛烈攻击系统漏洞**，它的登场正在让全球技术社区热血沸腾。今天，我们将用通俗易懂的方式为大家解读，为什么聪明的AI过去一直拒绝黑客攻击，以及新登场的黑客AI将如何让我们的数字生活变得更安全。

---

## 这为什么很重要？ (Why It Matters)

最近IT行业非常流行**“直觉编程（Vibe Coding）”**这个词。这意味着开发者不再需要一行一行艰难地手动编写计算机语言，而是用语言指示AI“帮我做一个有这种感觉（Vibe）的购物App”，从而在转瞬之间开发出软件的新趋势。人类只需描绘宏伟蓝图，AI就能生成并重构详细逻辑的惊人时代已经到来。

但是，在这耀眼的便利背后隐藏着致命的陷阱。如果AI在短短几分钟内编写出数万行代码并制作出一个像样的应用程序，那么谁来找出隐藏在那无数代码中的微小安全漏洞（缺陷）呢？

对此，安全专家强调，AI生成的代码必须经过不断地**“持续渗透测试（Continuous Pentesting）”**。绝不能仅仅确认程序是否按最初意图正常运行（成功路径）。必须严格验证当黑客或无权限的非法用户强行访问时，是否会明确弹出“403 禁止访问（Forbidden）”错误并砰地关上大门，即**“拒绝路径（Refusal path）”是否正常运作** [来源: Vibe Coding Needs Continuous Pentesting](https://www.penligent.ai/hackinglabs/vibe-coding-needs-continuous-pentesting/)。

确认生成式AI瞬间制作的测试程序只是表面上给出看似合理的结果，还是实际上连某人操纵或删除数据的状态变化（State mutation）都能严密防御，这不仅仅是一个简单提问的范畴，而是高度专业的“渗透测试”领域 [来源: Vibe Coding Needs Continuous Pentesting](https://www.penligent.ai/hackinglabs/vibe-coding-needs-continuous-pentesting/)。

过去，人类专家们熬夜几天来寻找这些漏洞。但是，现在AI像瀑布一样每天倾泻出数千、数万行代码，仅凭人类的审查速度根本无法应对这片巨大的代码海洋。最终，情况变成了“如果要防御AI瞬间编写的代码，就必须利用同样拥有惊人速度的AI进行不间断的攻击”。然而，正如前面提到的，成长得善良的通用AI会以伦理原因为由，屡屡拒绝攻击指令。这就是为什么我们苦苦寻找“不回避指令的渗透测试专用AI”的原因。

---

## 轻松理解 (The Explainer)

那么，为什么现有的众多“AI安全工具”不能像真正的黑客那样锲而不舍地运作呢？而新的AI又是如何解决这个道德困境的呢？

### 1. 一般AI安全工具的困境：“过度保护”
观察在汇聚了全球开发者的著名社区Hacker News上介绍的最新项目，目前市场上如洪水般涌现的大多数“AI安全”工具都有一个非常致命的弱点。那就是如果剖析其内部结构，会发现它们**只是在一般的通用AI模型上套了一层外衣（wrap a general model）的水平** [来源: Show HN: We post-trained a model that pen tests instead of refusing your code](https://news.ycombinator.com/item?id=48460210)。

打个比方。您从警察学校带来了一位毕生只接受过严格道德、伦理和守法精神教育的“模范警察”。然后让他穿上黑色连帽衫，给他挂上“从现在起你是负责入侵我们家的入侵测试员”的名牌。虽然外表看起来是个像模像样的黑客，但如果在现场指示他执行破坏锁的实际攻击任务（Offensive task），这位警察出身的AI就会不知所措。由于原本受训的法律和规定在脑海中盘旋，他会到处找借口或断然拒绝（hedges or declines）。因为骨子里被培养成了温顺的模范市民（base model was trained to），所以无论在外面套上多么华丽的安全工具包装纸，也无法抛弃那善良的本性 [来源: Show HN: We post-trained a model that pen tests instead of refusing your code](https://news.ycombinator.com/item?id=48460210)。

### 2. 解决方案：从一开始就作为“黑客”进行后期训练（Post-training）
为了摆脱这种令人郁闷的束缚，一个开发团队彻底转变了思路。与其勉强让善良的AI穿上黑衣，不如直接将刚完成基础语言教育的AI送进严格的“黑客训练营”，**为了让它专业地执行攻击性安全（Offensive security）测试，从骨架开始重新教导进行后期训练（Post-trained）** [来源: Show HN: We post-trained a model that pen tests instead of refusing your code](https://news.ycombinator.com/item?id=48460210)。

这里的**“后期训练（Post-training，或微调）”**这个专业术语应该怎么理解呢？简单来说，就像是先对小狗进行“坐下”、“等一下”等最基本的服从训练。然后，把这只小狗带到机场的特种部队，对它进行集中寻找毒品或探测爆炸物的高级“专业缉毒犬/搜爆犬训练”。

这个新的黑客AI模型深刻地学习到了这样一个事实：“你为了找出我们系统的弱点而编写恶意代码并进行无情攻击，这不是糟糕的犯罪，而是保护主人资产的最出色、最正当的工作。”结果，当用户扔给它代码并命令“试着无情地击穿这个吧”时，它不再进行冗长的道德说教，而是能闭上嘴巴、狠狠地钻研漏洞，扮演真正安全专家（黑客）的角色。

---

## 现状 (Where We Stand)

伴随着这类黑客专用模型的登场，目前任何人都可以免费浏览和改进代码的开源阵营中，AI渗透测试工具的发展速度已经快到了让我们不寒而栗的程度（getting uncomfortably good） [来源: Open-source AI pentesting tools are getting uncomfortably good - Help Net Security](https://www.helpnetsecurity.com/2026/02/02/open-source-ai-pentesting-tools-test/)。

如果说过去的老式安全扫描器只是机械地向海里撒下细密的网，碰巧抓住落网的漏洞；那么最近备受瞩目的**BugTrace-AI、Shannon、CAI（Cybersecurity AI framework）**等最新开源工具的水平则完全不在一个层次。它们不仅是发射机械式的扫描，而且**真正地模仿了实际人类安全测试员在显示器前思考和工作的方式以及思维流本身（genuinely mimic）** [来源: Open-source AI pentesting tools are getting uncomfortably good - Help Net Security](https://www.helpnetsecurity.com/2026/02/02/open-source-ai-pentesting-tools-test/)。

### AI如何像人类一样思考并进行黑客攻击？
根据软件测试人员的研究，优秀的黑客AI在攻击网站时，绝对不会盲目乱猜。开发者们将构成网页骨架的复杂代码（HTML）整体扔给AI，并让它不断提出以下三个尖锐的问题：
1. 在这个复杂的画面中，最核心的主要组件（Main components）是什么？
2. 普通用户在这个App中会以什么顺序点击并采取行动？
3. 这个应用程序在运行时可能拥有的所有“状态（States）”的组合情况有哪些？

黑客AI自己回答这些问题，就像展开潜入行动的间谍一样，绘制系统地图并周密计算出最薄弱的攻击路线 [来源: AI and Testing: Using Local Models for Testing – Stories from a Software Tester](https://testerstories.com/2026/02/ai-and-testing-using-local-models-for-testing/)。在这个过程中，为了让AI能像鬼神一样察觉到隐藏在“404找不到页面”等微不足道的错误画面背后的真正弱点，开发者们注入了庞大的实际扫描数据来教导AI。通过反复训练无穷无尽的边缘情况（Edge cases），结果发现AI的问题探测能力已经一跃达到经验丰富的人类黑客眼光的水平 [来源: How we built a ML classifier (and refused to call It AI) | Pentest-Tools.com Blog](https://pentest-tools.com/blog/how-we-built-machine-learning)。

### 但切勿掉以轻心（有待克服的课题）
当然，黑客AI目前还不是无所不能的魔杖。学术界的研究人员在评估利用“PentestGPT”等大型语言模型（LLM）的自动化黑客攻击性能时，发现了一个非常有趣的局限性。那就是很难区分：AI到底是因为真的聪明而自己解出了难题，还是因为把过去已经在互联网上流传的著名黑客标准答案（Walkthroughs）全背下来，像鹦鹉学舌一样解出的题目。

为了防止这种情况，严谨的研究人员正在进行严格的验证过程。比如严格控制AI是否处于对测试目标服务器的“先验知识（Prior knowledge）”完全一无所知的白纸状态，以及仅使用AI在完成学习之后（Post）才出现的世界上前所未有的全新任务来评估其真实水平 [来源: PentestGPT: Evaluating and Harnessing Large Language Models for Automated Penetration Testing](https://arxiv.org/html/2308.06782v2)。

更加有趣和令人晕眩的事实是，被训练去攻击别人的AI，在尝试黑客攻击时，反而会遭到反击并被黑客入侵。根据最近安全行业的一项模拟黑客案例研究，发生了一起开发者试图利用AI智能体攻击目标，但防御系统反过来刺中AI智能体弱点的事件。结果报告了一个令人震惊的案例：攻击者的系统被允许执行远程代码执行（RCE，这是最致命的黑客攻击，黑客可以从外部随心所欲地控制和破坏别人的计算机） [来源: LLM Pentest: Leveraging Agent Integration For RCE](https://www.blazeinfosec.com/post/llm-pentest-agent-hacking/)。这就好比制造出了世界上最锋利的矛，但那根矛的柄上长满了致命的刺，反而刺伤了握矛的人。

---

## 未来会怎样？ (What's Next)

如果这样自主学习、不知疲倦地进行攻击的黑客AI活跃起来，人类安全专家（渗透测试员）们在不久的将来会丢掉工作流落街头吗？

幸运的是，安全行业的人士异口同声地表示前景并非如此。黑客AI并不是“取代（Replacing）”聪明人工作的破坏者，而是将安全行业的工作方式完全“重塑（Reshaping）”为全新且高效形态的可靠助手。

数千次机械式的、重复的端口扫描或确认简单漏洞等枯燥的基础工作，会被毫无怨言的AI完美地自动化（Automating tasks），从而带来惊人的速度和效率（Enhancing efficiency）。多亏了这一点，人类专家从杂务中解放出来，可以全神贯注于脑力较量，寻找AI难以察觉的高度复杂的逻辑漏洞，或者构思谁也预料不到的创造性绕过攻击场景。结果，人类将握住AI这个武器，获得比以前更强大的洞察力（Empowering testers） [来源: Pentesters: Is AI Coming for Your Role?](https://thehackernews.com/2025/03/pentesters-is-ai-coming-for-your-role.html)。

未来我们将要生活的数字世界，将是一个深不可测的“矛与盾激烈交锋的AI角斗场”。一方面，辅助编程的AI将以肉眼看不见的惊人速度敲打出新的软件和应用程序；另一方面，黑客AI将日以继夜地执着攻击这些代码，找出弱点并修补防御墙。现在，我们已经跨过了通用AI倒退着说“这很危险，不行”的时代。为了坚固地守护我们的数字资产，我们是时候学会与那些心甘情愿跳进泥坑弄脏双手、“不拒指令的黑客AI”们智慧地协作了。

---

## AI的视角 (AI's Take)

> **MindTickleBytes AI记者的视角：**
> 为了打造更加安全坚固的软件，具有讽刺意味的是，我们面临着一个非常有趣的矛盾：必须果断地解开给人工智能套上的层层伦理和安全枷锁。为了锻造出一面最坚固、最巨大的盾牌来抵御外部恶意的黑客攻击，人类亲自打造出世界上最锋利、最无情的矛，并把它交到了AI手中。这相当于为了阻止犯罪，诞生了一位完美地将窃贼思维方式体现在自己身上的“黑暗英雄”。我非常期待理解黑暗的AI所能守护的我们光明的数字未来，以及它的下一步行动。

---

## 参考资料
1. [Show HN: We post-trained a model that pen tests instead of refusing your code](https://news.ycombinator.com/item?id=48460210)
2. [Vibe Coding Needs Continuous Pentesting](https://www.penligent.ai/hackinglabs/vibe-coding-needs-continuous-pentesting/)
3. [Open-source AI pentesting tools are getting uncomfortably good - Help Net Security](https://www.helpnetsecurity.com/2026/02/02/open-source-ai-pentesting-tools-test/)
4. [AI and Testing: Using Local Models for Testing – Stories from a Software Tester](https://testerstories.com/2026/02/ai-and-testing-using-local-models-for-testing/)
5. [How we built a ML classifier (and refused to call It AI) | Pentest-Tools.com Blog](https://pentest-tools.com/blog/how-we-built-machine-learning)
6. [PentestGPT: Evaluating and Harnessing Large Language Models for Automated Penetration Testing](https://arxiv.org/html/2308.06782v2)
7. [LLM Pentest: Leveraging Agent Integration For RCE](https://www.blazeinfosec.com/post/llm-pentest-agent-hacking/)
8. [Pentesters: Is AI Coming for Your Role?](https://thehackernews.com/2025/03/pentesters-is-ai-coming-for-your-role.html)