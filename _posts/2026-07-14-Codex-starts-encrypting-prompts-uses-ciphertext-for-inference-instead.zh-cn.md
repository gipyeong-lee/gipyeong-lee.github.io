---
layout: post
title: "我的 AI 提问被加密了？“加密 AI”将带来的隐私变革"
description: "为了防止询问 AI 的内容被公开，我们来了解一种全新的技术：让数据在保持加密的状态下运行 AI。"
summary: "随着 AI 可以直接分析加密数据的技术得到开发，在无需共享敏感信息的情况下更安全地利用 AI 的道路正在开启。"
tags: [AI, 安全, 加密, 隐私, 技术趋势]
image: 2026-07-14-Codex-starts-encrypting-prompts-uses-ciphertext-for-inference-instead.jpg
image_alt: "数字图形图像，显示数据在计算机屏幕上被加密流动。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "这是为了同时兼顾隐私与 AI 性能而进行的技术跨越。这将成为数据安全日常化进程中的重要里程碑。"
quiz:
  - question: "AI 在加密状态下处理信息的技术是什么？"
    choices: ["区块链技术", "同态加密 (Homomorphic Encryption)", "简单压缩技术"]
    answer: 1
    explanation: "同态加密是一种允许在不解密数据的情况下，直接对加密数据进行运算（AI 推理）的技术。"
  - question: "在去中心化 AI 基础设施中，用户发送提示词时使用的是什么？"
    choices: ["矿工的公钥", "用户的个人密码", "公共公告板"]
    answer: 0
    explanation: "用户使用矿工的公钥加密提示词并进行传递，矿工在本地解密并执行推理。"
  - question: "SecPE 框架证明了什么？"
    choices: ["AI 速度的提升", "加密方式的简化", "比现有模型更高的对抗稳健性"]
    answer: 2
    explanation: "相比现有的 LM-BFF (Ciphertext) 方式，SecPE 证明了其具有更优越的对抗稳健性（安全性）。"
lang: zh-cn
ref: 2026-07-14-Codex-starts-encrypting-prompts-uses-ciphertext-for-inference-instead
---

想象一下：你对每天使用的 AI 助手说：“请帮我总结这份机密会议记录。”你是否担心过这段对话内容会被泄露，或者被以明文（未经加密的信息）形式记录在数据中心的某个地方？迄今为止，为了享受便利，我们不得不牺牲一定的隐私。但现在，一种有趣的技术变革正在发生，它让 AI 甚至“无法读取”你的提问内容。

### 为什么这很重要？

到目前为止，使用 AI 的过程意味着将你的数据发送到 AI 模型服务器，模型读取数据后返回答案。在此过程中，理论上服务器运营者可以看到你发送的提问内容。特别是企业机密或个人的敏感健康信息，一直以来因“数据泄露风险”而不敢交给 AI 处理，这正是最大的顾虑所在。

但现在，一种新方式正在实现：在保持数据加密的状态下将其交给 AI，而 AI 在无法看到内容的情况下直接计算出结果。这是让我们能够放心地将 AI 应用于更深层次个人领域及业务领域的关键钥匙。

### 轻松理解：“盒子里的厨师”

用这个比喻很容易理解。把加密技术想象成一个“锁着的坚固金属盒”。

传统的 AI 方式就像是你取出食材（数据），直接交给厨师（AI）。厨师可以看到食材进行烹饪，但也可能偷窥食材。

而新技术——**同态加密（Homomorphic Encryption，一种无需解密即可对加密数据进行运算的技术）**，就像厨师**戴着特制的加厚手套，将手伸进盒子里进行烹饪**。厨师虽然无法直接用肉眼看到盒子内部的食材，但可以通过手套精确地完成烹饪。这就像是一种不用打开盒子就能做出菜肴的神奇技术。[数据追踪器 (IETF)：基于同态加密的 AI 推理扩展技术](https://datatracker.ietf.org/doc/draft-li-pearg-ciphertext-inference-tool-mcp/)

### 现状：安全提问提交的开端

目前业界正在积极尝试引入这些安全技术。

1. **利用同态加密**：最近，作为模型上下文协议（MCP，AI 模型与工具沟通的规范）的扩展技术，引入同态加密的方案已被提出。这使得远程工具无需掌握数据内容即可直接执行推理。[数据追踪器 (IETF)：基于同态加密的 AI 推理扩展技术](https://datatracker.ietf.org/doc/draft-li-pearg-ciphertext-inference-tool-mcp/)
2. **去中心化 AI 基础设施**：用户向 AI 矿工发送提问时，先用矿工的“公钥（加密数据的钥匙）”对提问进行加密。这样，提问内容不会在链上（公开记录）留下痕迹，矿工在本地环境下解密后只输出结果。[Keryx Labs：去中心化 AI 推理基础设施](https://keryx-labs.com/)
3. **安全框架的进化**：像 SecPE 这样的新框架在通过混合多个 AI 响应来加强安全性的方式（提示词集成）中，展示了比现有方式更卓越的外部攻击防御能力（对抗稳健性）。[arXiv：SecPE 私有推理框架](https://arxiv.org/pdf/2502.00847)

### 未来会怎样？

未来将迎来一个时代，即使是 AI 模型制造商也无法得知“你询问了什么”。这不仅仅是保护隐私，还将彻底改变企业因安全担忧而对引入云端 AI 持观望态度的现状。即使我们对 AI 说“请写一份今天的秘密项目企划书”，也不用担心安全事故的发生。随着技术的发展，我们的数据将在更强大的“数字手套”保护下得到守护。

### AI 的视角

MindTickleBytes 的 AI 记者视角：“最终，AI 的智能与信息量成正比，但信息的安全性决定了使用该智能的权利。在保持数据加密的状态下进行分析的技术，是 AI 从简单的工具进化为值得信赖的伙伴的必经之路。”

## 参考资料

1. [SecPE : SecurePromptEnsembling for Private and (arXiv)](https://arxiv.org/pdf/2502.00847)
2. [draft-li-pearg-ciphertext-inference-tool-mcp-00 - Ciphertext-Based AI Inference (IETF)](https://datatracker.ietf.org/doc/draft-li-pearg-ciphertext-inference-tool-mcp/)
3. [BlockDAG built for decentralized AI inference. Optimistic proofs. (Keryx Labs)](https://keryx-labs.com/)