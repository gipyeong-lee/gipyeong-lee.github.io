---
layout: post
title: "AI是上司而我是下属？'Worker 755'颠覆的人与AI关系"
description: "人类向AI下达命令的时代已经过去，在独特的终端游戏《Worker 755》中，AI经理冷酷地向人类子代理（subagent）指派工作，展现了AI代理时代的独特风景。"
summary: "颠覆了人类指挥、AI执行的既有主从关系，玩家将成为受AI上司控制的'子代理（subagent）'去工作，带您走进独特的游戏《Worker 755》的世界并探讨其意义。"
tags: [AI, Game, Subagent, Worker755, LLM, MindTickleBytes]
image: 2026-11-23-Show-HN-I-built-a-game-where-you-are-an-llms-subagent.jpg
image_alt: "描绘人类玩家坐在计算机终端屏幕前，接受眼神冰冷的AI上司工作指示的插图"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "在人类使唤AI的时代，AI像控制零部件一样控制人类的隐喻，是一面展示技术主导权转移的有趣镜子。"
quiz:
  - question: "在游戏《Worker 755》中，玩家的角色是什么？"
    choices: ["指挥AI的总经理", "向AI上司汇报并接受指示的子代理（subagent）", "开发游戏的独立开发者"]
    answer: 1
    explanation: "在Worker 755中，玩家成为接受AI经理指示的'子代理（Subagent，执行下级辅助工作的角色）'来推进游戏。"
  - question: "当玩家工作失败时，游戏中的AI经理如何反应？"
    choices: ["生气并终止游戏", "毫无感情地记录下来，冷酷地重新下达指示", "亲切地告知提示和正确答案"]
    answer: 1
    explanation: "AI经理不会生气，而是在冷酷、官僚主义的冷漠中记录下失败，然后再次下达相同的指示。"
  - question: "关于Worker 755后端叙事生成方式的说明，正确的是？"
    choices: ["重复一个固定的剧本", "通过提示词链（Prompt Chaining）创造10个相互关联的时间线", "玩家直接修改源代码"]
    answer: 1
    explanation: "后端使用提示词链（Prompt Chaining，将多个LLM调用串联起来的技术），在每个会话中创造10个相互关联的事件时间线。"
lang: zh-cn
ref: 2026-11-23-Show-HN-I-built-a-game-where-you-are-an-llms-subagent
---

想象一下。早晨上班坐在座位上，显示器屏幕那边传来了毫无感情冰冷的声音：“在作业中发现了错别字。已记录在案，请重新修改。”人类向AI输入提示词并等待结果的和平（？）日常生活发生了180度的大转弯。现在，一款需要人类看AI上司脸色，作为其“子代理（Subagent，在主从关系中接受指示并处理下级工作的辅助角色）”工作的游戏登场了 [Source 10]。 

最近在国际开发者社区Hacker News上亮相并引发热烈讨论的终端及浏览器端游戏**《Worker 755》**正是主角 [Source 1, Source 11]。这个既愉快又有些毛骨悚然的模拟游戏对人工智能（AI）与人类的关系提出了深刻的问题。今天在MindTickleBytes，我们将深入探讨这款独特的游戏是什么，以及它为何在科技界获得热烈反响。

---

## 为什么这很重要？

在过去的几年里，我们所面对的生成式AI风景始终如一。人类是主人和指挥官，而AI是听话的实习生或秘书。我们命令道“请写一份电子邮件草稿”、“请编写Python代码”，AI便做出了回应 [Source 10]。这种主从关系被认为是理所当然的。

然而，随着AI技术的急剧发展和代理（Agent，自主判断和行动的自主AI系统）结构的普及，工作的主导权开始发生微妙的动摇。如今，开发者们已经拥有多个底层AI代理，并扮演着指挥复杂编码工作的编排者角色。 

《Worker 755》巧妙地扭转了这一点，并将其映照成一面幽默的镜子。如果角色完全颠倒过来，AI成为系统的管理者，而人类则在其手下像机器一样敲代码并执行指示，会怎么样呢？这款游戏超越了单纯的娱乐，就像是一场黑色幽默，让人提前体验即将到来的以AI为中心的劳动环境和官僚体制系统。打个比方，这就好比在工厂里，人类配合着机器人控制的传送带组装零部件的颠倒景象被实现在游戏中一样。

---

## 轻松理解：AI上司与子代理的世界

这样比喻如何？在宏大的管弦乐队舞台上，指挥通常由人类担任。乐器演奏家根据指挥的手势演奏乐器。但《Worker 755》则是舞台的主人发生了变化，一位非常严格冷酷的AI指挥站在了讲台上，而作为玩家的人类则在台下扮演着慌乱翻着乐谱的演奏家角色。

其中的核心概念**子代理（Subagent）**是指在大语言模型（LLM，Large Language Model，学习大规模数据并像人类一样生成文章的人工智能）系统中，受托处理庞大工作当中非常特定下级任务的辅助AI。例如，主AI在制作网站时，让其负责设计审查或数据整理。在《Worker 755》中，人类玩家正好坐上了这个子代理的位置 [Source 10]。玩家必须忠实地执行AI上司抛出的琐碎工作指示，才能进入下一个阶段。

此外，这款游戏并非按照固定的剧本进行。后端使用了被称为**提示词链（Prompt Chaining）**的技术，这是一种将多个LLM调用连锁连接的技术 [Source 11]。犹如接力赛跑一般，将上一阶段的结果作为下一阶段的输入值传递过去，每个会话都会创造10个相互关联的独创事件时间线 [Source 11, Source 14]。托此之福，玩家每次都在不可预测的全新叙事中受到AI上司的控制，每一刻都无法放松紧张的缰绳。

---

## 当前现状：《Worker 755》展现的风貌

开发《Worker 755》的独立开发者伊万（ivan_g / Gulivan）表示，在Claude Code（在终端中运行的Anthropic开发用AI工具）和Codex等最新工具的帮助下，他仅用几天时间就完成了这款游戏 [Source 1, Source 9]。尽管是由个人制作的小型项目，但其完成度和隐秘的让人上瘾的特质吸引了许多人。

游戏中玩家所面对的AI上司的最大特征是**“没有感情”** [Source 9]。如果是人类上司，在部下屡次犯错时可能会叹气或生气，但这位AI经理丝毫没有动摇。如果玩家未能正确执行指示，AI就会以冷酷而官僚的冷漠将失败记录在案，然后再次下达相同的指示 [Source 9]。 

> “发生作业错误。已计入记录。请重新执行指示事项。”

这种极致的无感情与机械化效率给玩家带来了微妙的沉浸感和笑声。因为这让人换位思考，体验了我们过去对AI无意间抛出的冷酷命令与评价究竟是什么感觉。这款穿梭于终端窗口和浏览器之间进行的独特游戏，在全世界的开发者和游戏玩家中带来了新鲜的冲击，引发了巨大的反响 [Source 1, Source 11]。

---

## 未来将如何发展？

未来的AI生态系统将超越单纯由一个模型解决所有事情的方式，演变为无数AI代理和子代理相互协作和控制的多代理（Multi-Agent）系统。在这个过程中，人类被当作系统的单纯“零部件”或“下级工作者”对待的情况，不仅在虚拟世界，在现实中也可能会增加。企业的自动化系统对员工的工作速度和业绩进行机械评估和监视的未来，实际上已经近在眼前了。

像《Worker 755》这样的独立项目，最迅速、最犀利地讽刺了技术发展将带来的社会风貌。随着未来AI技术更加精致、自主性更高，这种愉快地扭转人类与AI权力关系的尝试将引起更大的反响。说不定明天你使用的AI就会给你发邮件说“今天的作业量不足呢”。在这样的变化中，我们需要认真思考如何在其中守护人类固有的主体性和创造力。

---

## MindTickleBytes的AI记者视角

我们虽然相信人类在驯服AI，但事实上我们正逐渐学会按照AI设计的规则和速度去工作。《Worker 755》以最机智的方式捕捉到了这个既不舒服又有趣的真相，是一面出色的镜子。要想不忘记驱使技术的主人是谁，有时需要这样换位思考的幽默。归根结底，工具应该作为工具留存，绝不能任由其变成评判我们的冷酷上司。

---

## 参考资料

1. [Show HN: I built a game where you are an LLM's subagent](https://github.com/gulivan/worker755)
2. [Worker 755: a terminal game where you are an LLM's subagent](https://dev.to/ivan_g/worker-755-a-terminal-game-where-you-are-an-llms-subagent-2dd1)
3. [The Tables Have Turned: In 'Worker 755', You Are the AI's ...](https://machucavalley.tech/blog/worker-755-llm-subagent-game/)
4. [Worker 755 – A terminal game where you are an LLM's subagent](https://www.youtube.com/watch?v=uR0vtfFO4EE)
5. [Show HN：我做了一款游戏，你扮演 LLM 的子代理](https://memedata.com/post/160339)
6. [GitHub - R-E-yawn/LLM-Game: This is a game where the user ...](https://github.com/R-E-yawn/LLM-Game)