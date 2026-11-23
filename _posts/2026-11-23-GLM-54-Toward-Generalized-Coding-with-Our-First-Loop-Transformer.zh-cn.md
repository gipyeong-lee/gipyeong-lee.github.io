---
layout: post
title: "AI会思考两次？Z.ai颠覆性新模型‘GLM-5.4’的秘密"
description: "中国Z.ai发布的全新AI模型GLM-5.4采用将层重复两次的‘循环Transformer’结构，实现了巨大模型的性能。轻松了解广义编码（Generalized Coding）的概念与主要特点。"
summary: "Z.ai发布了应用循环Transformer（Loop Transformer）结构的旗舰AI模型GLM-5.4，该结构将层重复两次。探讨超越编码、扩展到视频、游戏和3D设计的‘广义编码’世界。"
tags: [GLM-5.4, Zhipu AI, Loop Transformer, AI模型, Generalized Coding]
image: 2026-11-23-GLM-54-Toward-Generalized-Coding-with-Our-First-Loop-Transformer.jpg
image_alt: "具象化表现通过重复神经网络结构与编码生成各种数字内容的情境插图"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "与其盲目增加参数数量，不如通过循环（Loop）‘思考深度’来极大化效率这一点非常新颖且令人印象深刻。可以说是展示了长期沉迷于硬件扩展竞争的AI行业中‘架构创新’能成为多么强大武器的里程碑。预计这也将为其他试图兼顾效率与性能的巨头企业之间的开发竞争点燃战火。"
quiz:
  - question: "GLM-5.4引入的核心架构名称是什么？"
    choices: ["循环Transformer (Loop Transformer)", "扩散Transformer (DiT)", "循环记忆网络 (RNN)"]
    answer: 0
    explanation: "GLM-5.4首次采用了将28个层重复两次（Loop）以实现巨大模型性能的‘循环Transformer’架构。"
  - question: "GLM-5.4所追求的‘广义编码（Generalized Coding）’的最合适含义是？"
    choices: ["纯编程语言学习速度提升10倍", "将代码不仅扩展为软件开发工具，还扩展为视频、游戏、3D设计等工具", "开源代码自动验证功能"]
    answer: 1
    explanation: "广义编码是将代码超越单纯软件开发工具，用作执行视频生成、游戏制作、3D建模等各种任务的通用工具的概念。"
  - question: "关于GLM-5.4架构及规模的说明，正确的是？"
    choices: ["10万亿参数规模的单层模型", "约750亿参数规模", "约750亿参数规模的28个层循环两次（750B scale, 28 layers twice）的结构"]
    answer: 2
    explanation: "GLM-5.4在约750B（750亿/7500亿）参数规模下运行两次28个层，达到媲美2T~3T（2万亿~3万亿）参数模型的智能。"
lang: zh-cn
ref: 2026-11-23-GLM-54-Toward-Generalized-Coding-with-Our-First-Loop-Transformer
---

想象一下。早晨醒来，打开智能手机对AI说：“请帮我制作一个我在脑海中构思的3D游戏世界以及其中移动角色的动画。”片刻之后，AI开始编写代码，并立刻在我们眼前迅速呈现出完美运行的3D游戏画面和视频。曾经只有程序开发者才会使用的“代码”变成了解开所有数字创作基础的魔术杖般的世界，这就是最近在AI行业成为热门话题的新范式 [出处 1, 出处 7, 出处 13]。

正如技术的发展不仅超越了日常生活的便利，更彻底打破了创作的壁垒一样。处于这一中心、吸引了全球科技爱好者目光的主角诞生了 [出处 1, 出处 6]。中国代表性人工智能研究实验室Z.ai（智谱AI，Zhipu AI）正式发布了全新的旗舰AI模型 **GLM-5.4** [出处 1, 出处 6]。这次的新产品摆脱了以往单纯膨胀数字的AI方式，采用了让AI自主反复思考的独创结构 [出处 1, 出处 6, 出处 17]。到底应用了什么技术，又将给我们的日常生活带来怎样的变化呢？让我们循序渐进地一探究竟。

---

## 为什么这很重要？

我们每天使用的AI聊天助手或生成式AI，随着体量的增大而变得更加聪明。必须将可调节的内部连接网络数量，即参数（Parameter，表示AI模型脑细胞连接网大小的单位）呈天文数字般增加到2万亿、3万亿个，才能模仿人类复杂的推理能力。然而，体量越庞大，服务器维护成本就越暴涨，普通用户使用时的速度变慢，消耗巨大电力等副作用也随之产生。就像为了维持巨大的豪宅，每个月必须支付巨额取暖费一样。

Z.ai推出的GLM-5.4之所以备受瞩目，正是因为它正面突破了这种“体量的极限” [出处 1, 出处 7]。它没有盲目地在物理上增加参数数量，而是选择了**让现有的脑结构相互交替通过两次来进行深度思考的方式** [出处 6, 出处 7]。通过这种方式，在相对保持物理体量的同时，爆发出了媲美2万亿~3万亿参数规模的超级巨兽模型的高度智能 [出处 1, 出处 6]。

除此之外，这一模型摆脱了只能收发文本的上一代，具备了视觉（Vision，图像输入功能），并开启了不仅是开发者、连普通大众也能以更低廉、更强大的方式进行日常创作的道路 [출처 10, 출처 11]。鉴于成本负担减轻、性能飞跃提升，这次升级可谓是加速AI服务大众化的重要二十一世纪里程碑（Milestone） [출처 5, 출처 10]。这不仅意味着一个模型的改变，更在重新书写未来AI发展效率标准方面具有重大意义。

---

## 轻松理解：‘循环Transformer’与‘广义编码’

那么，作为GLM-5.4核心技术的**循环Transformer（Loop Transformer，通过将模型的神经网络层设定为循环结构来引导深度思考的架构）**究竟是什么呢？为了便于理解，我来举个形象的比喻。

> **这样比喻很容易理解：**
> 普通AI在阅读困难的推理小说时，往往只把书页扫一眼，就急于猜测凶手。如果书太厚（参数较少），很容易遗漏前后文脉而指认出错误的凶手。因此，以往总是试图把整本书做厚10倍来解决问题。
> 
> 相比之下，GLM-5.4的“循环Transformer”在读完一遍书页后，会**将最核心的章节（Layer，神经网络的处理阶段）从头到尾重新回顾并仔细复盘** [출처 5, 출처 6]。在750B规模下将28个核心层循环运行两次（Loops 28 layers twice at 750B scale），自主纠正错过的线索和逻辑错误 [출처 5, 출처 6]。无需在物理上建造巨大的书房，仅凭聪明的阅读法就成了名侦探。

另一个需要关注的概念是Z.ai新提出的**广义编码（Generalized Coding，将代码扩展为控制视频、游戏、3D设计等通用工具的概念）** [출처 1, 출처 7]。

> **简单来说：**
> 过去一提到“编码”，人们会认为那是程序员在黑底屏幕上敲击英文指令（if, else, print等）制作程序的专利。但对于GLM-5.4来说，编码并非单纯的软件制作工具。AI在脑海中构想屏幕上应该呈现什么内容后，将其编写成精密的**代码**，在计算机内渲染视频文件，组装互动游戏，甚至直接绘制3D立体模型和机械设计图 [출처 7, 출처 13]。也就是说，代码已经演变成了连接人类与计算机的“万能数字语言”。

这两种创新最终为AI以更少资源进行更深度思考、处理更广泛领域的创意作品提供了坚实的翅膀。

---

## 当前现状：发生了哪些具体变化？

根据博客规格与官方发布，GLM-5.4建立在坚实的技术基础之上 [출처 2]。

* **压倒性效率的循环结构：** 基于约750B（750亿/7500亿）参数规模，采用了将28个层重复执行两次的设计 [출처 2, 출처 5, 출처 11]。凭借这一创新的循环结构，它展现出与2T~3T（2万亿~3万亿）参数巨型模型相媲美的智能水平 [출처 1, 출처 6]。
* **视觉智能（Vision）的结合：** 与上一代GLM-5.3只能收发文本的“纯文本（Text-in, text-out）”模型不同，GLM-5.4在主编码计划模型中全面引入了视觉功能，能够轻松处理图像识别和多模态（Multimodal，同时处理文本、图像等多种形式信息的能够）任务 [출처 10, 출처 11]。
* **庞大的记忆容量：** 支持高达100万个Token（Token，AI单次处理的文字及数据片段单位）的庞大上下文窗口（Context window，AI能够记忆和理解的最大对话及文档范围），即使整篇塞入长篇论文或庞大源代码也不会迷失方向 [출처 11]。
* **性价比与使用价格：** 通过Z.ai Chat和GLM编码计划（Coding Plan)订阅服务已经与用户见面，订阅费用从每月18美元起步 [출처 5, 출처 11]。特别值得注意的是，生成输出时消耗的编码计划额度从原先GLM-5.3的24额度大幅降至16额度，使用户能以更低成本享受高性能AI [출처 5]。产品负责人主管周璇·李（Zixuan Li）通过X（原推特）传播了编码计划50%配额（Quota）提振的好消息，获得了开发者们的热烈响应 [출처 2, 출처 10]。

不过，在发布初期阶段，官方公共基准测试（Performance benchmark）或开源权重（Open weights，公开AI内部权重文件的开放政策）尚未公布，这暗示着我们需要进行彻底的实测验证 [출처 5]。由于爆炸性的关注，发布当天服务器也出现了一定程度的过载 [출처 15]，但市场的期待感有增无减。用户们高度关注这种巨大的效率在实际工作环境中能带来多少切实体会。

---

## 未来将如何发展？

GLM-5.4的问世向AI行业传递了一个重要信息。它证明了摆脱单纯向服务器砸电、盲目扩大参数数量的粗放竞争，**“增加思考深度的架构优化”**正在成为新趋势 [출처 6, 출처 7]。

未来用户需要关注的是，广义编码究竟能在日常与产业现场创造出多大实质性的产出。超越单纯的阅读与总结，仅凭一行自然语言指令，网页游戏、YouTube短视频以及3D模拟模型在完美的自动化流水线中倾泻而出的场景正逐渐成为现实 [출처 7, 출처 13]。现在，普通大众也能轻松制作专家级数字内容的时代已经大步走来。

观察公开权重未来将如何对开源阵营产生影响，以及接下来的后续模型将把这种循环结构推向何种高度，将是今年下半年最令人瞩目的看点。

---

## AI的视角

> **MindTickleBytes的AI记者视角**
> 正如证明了单纯扩大体量并非唯一答案一样，GLM-5.4通过“思考两次的方法”开启了AI效率的新纪元。将代码重新定义为数字世界的万能组装工具而非单纯编程语言的这次尝试，究竟能在未来把我们的日常生活改变得多么便利，着实令人期待。该模型默默向我们展示了技术的本质终究在于“以更少资源提供更多价值”。毫无疑问，它将撼动以硬件扩展竞争为主导的格局，并成为涌现出更智能、更务实AI模型的催化剂。

---

## 参考资料

1. Z.ai, *GLM-5.4: Toward Generalized Coding with Our First Loop Transformer*, https://z.ai/blog/glm-5.4
2. ExplainX, *GLM-5.4 Coding Plan: +50% Quota, Vision (Nov 2026)*, https://explainx.ai/blog/glm-5-4-coding-plan-vision-50-percent-quota-boost-november-2026
3. Tech AI Wire, *GLM-5.4: Loop Transformer, Coding Plan credits, no weights*, https://techaiwire.com/articles/glm-5-4-loop-transformer-no-benchmarks-coding-plan-credits/
4. The Next Web (TNW), *Z.ai’s GLM-5.4 runs its layers twice to rival 2T...*, https://thenextweb.com/news/zai-glm-5-4-loop-transformer-coding-model
5. Unite.AI, *Z.ai’s GLM-5.4 Uses Iterative Depth Without Adding Parameters*, https://www.unite.ai/z-ais-glm-5-4-uses-iterative-depth-without-adding-parameters/
6. TeamOrouter, *GLM-5.4 Released: Vision, Stronger Coding, and When the API Arrives*, https://teamorouter.com/blogs/glm-5-4
7. OrcaRouter, *GLM-5.4 vs GLM-5.3: What the Upgrade Actually Adds*, https://www.orcarouter.ai/blog/glm-5-4-vs-glm-5-3
8. Habr, *Z.ai выпустили GLM-5.4 на архитектуре Loop Transformer...*, https://habr.com/ru/articles/1111176/
9. Unisender News, *Вышла флагманская нейросеть GLM-5.4*, https://neiro.unisender.com/novosti/z-ai-glm-5-4-loop-transformer/
10. VC.ru, *GLM-5.4 оказался Loop Transformer — deksden notes*, https://vc.ru/deksden_notes/3273303-glm-5-4-tsiklicheskiy-transformer