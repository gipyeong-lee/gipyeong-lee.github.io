---
layout: post
title: "我的密码在 AI 训练数据里？7.6 PB 规模的安全警示"
description: "AI 训练数据集中正有数十万个密码和 API 密钥处于无防护的暴露状态。我们来看看安全专家对 AI 生态系统安全漏洞发出的警告。"
summary: "安全研究团队对 AI 训练平台“Hugging Face”的 7.6 PB 数据进行了扫描，结果证实有超过 22 万个实际可用的安全凭证被暴露。"
tags: [AI安全, Hugging Face, 数据隐私, 信息保护]
image: 2026-08-02-Scanning-76-Petabytes-of-HuggingFace-Training-Data-for-Secrets.jpg
image_alt: "一幅象征着安全研究人员用数字放大镜观察浩瀚数据海洋的图像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "与 AI 模型性能同等重要的是“数据卫生”。在开源共享文化盛行的时代，个人和企业对安全管理的警惕性显得尤为迫切。"
quiz:
  - question: "安全研究人员在 Hugging Face 中发现的“实际可用安全凭证”数量大约是多少？"
    choices: ["约 2 千个", "约 2 万个", "约 22 万个"]
    answer: 2
    explanation: "研究结果显示，约有 221,303 个可用的安全令牌和密码处于无防护的暴露状态。"
  - question: "此次进行安全扫描的数据总量大约是多少？"
    choices: ["7.6 GB", "7.6 TB", "7.6 PB"]
    answer: 2
    explanation: "研究团队扫描了总计 7.6 PB 的数据，涉及 1.87 亿个文件。"
  - question: "Hugging Face 为解决这一安全问题采取了什么努力？"
    choices: ["全面停止服务", "与 Truffle Security 合作引入安全扫描功能", "强制删除所有用户账户"]
    answer: 1
    explanation: "Hugging Face 已与 Truffle Security 合作，在平台内引入了“TruffleHog”安全扫描功能。"
lang: zh-cn
ref: 2026-08-02-Scanning-76-Petabytes-of-HuggingFace-Training-Data-for-Secrets
---

# 我的密码在 AI 训练数据里？7.6 PB 规模的安全警示

如果说你日常中喜欢使用的应用或软件，其实因为某人的一个小失误而暴露在黑客攻击的威胁之下，会怎么样呢？随着近期人工智能 (AI) 的热潮，全球开发者和企业用于共享 AI 训练数据的平台“Hugging Face”备受关注。然而，事实证明，在这里上传的海量数据中，混杂着我们本应隐藏的“秘密”。

安全研究团队对 Hugging Face 的公共数据集进行了全方位排查，结果发现在 7.6 PB（1 PB 相当于 1,000 TB，容量极其庞大）的海量数据中，竟有数十万个实际的密码和 API 密钥（API 是程序间的对话窗口，密钥是打开该窗口的钥匙）处于无防护的暴露状态。[Scanning 7.6 Petabytes of HuggingFace Training Data for Secrets ◆ Truffle Security Co.](https://trufflesecurity.com/blog/scanning-7-6-petabytes-of-ai-training-data-for-secrets)

## 为什么这很重要？

这个问题不仅是个人失误，更是一个严重的安全性问题。如今，AI 模型基于海量的公开数据进行训练。如果训练数据中包含开发者的密码或敏感访问密钥，那么通过相应的 AI 模型，这些秘密信息就可能被泄露。更进一步，恶意攻击者完全有可能操纵训练数据或在该软件中植入恶意代码。

研究团队发现的 22 万余个凭证中，部分拥有极高的权限，足以让攻击者干预软件更新过程并植入恶意代码。[Scanning 7.6 Petabytes of HuggingFace Training Data for Secrets ◆ Truffle Security Co.](https://trufflesecurity.com/blog/scanning-7-6-petabytes-of-ai-training-data-for-secrets) 我们每天使用的软件由于这类安全漏洞而处于危境，这一点令人深感担忧。

## 简单理解：“图书馆里的秘密纸条”

让我们把这种情况比作图书馆。想象一下，有一个巨大的图书馆，全世界任何人都可以自由地借阅书籍。但如果某位开发者在归还书籍时，不小心把写有自家大门密码和银行账户密码的纸条夹在了书里，会发生什么呢？

更大的问题是，这个图书馆不仅保存书籍，还充当着以这些书籍为素材制造全新“智能助手”的工厂角色。训练 AI 模型的过程，就是浏览图书馆中所有信息并学习其模式的过程。如果训练素材中包含了密码，AI 就可能像学习有用信息一样，把那些密码也一并学了进去。[Hugging Face security analysis: ~70,000 live secrets and API keys, private repos, and leaky pics! 🤖🤗💦🔑😈](https://it4sec.substack.com/p/hugging-face-security-analysis-70000)

## 当前状况

幸运的是，Hugging Face 正在积极行动以解决这些问题。他们与安全专业企业“Truffle Security”携手，引入了“TruffleHog”扫描功能，能够自动检查上传到平台的数据中是否混入了秘密信息。[TruffleHog Partners With Hugging Face to Scan for Secrets ◆ Truffle Security Co.](https://trufflesecurity.com/blog/trufflehog-partners-with-hugging-face-to-scan-for-secrets)

但仍需保持警惕。仅此次研究扫描的数据量就达到了 1.87 亿个文件，总计 7.6 PB。[Scanning 7.6 Petabytes of HuggingFace Training Data for Secrets ◆ Truffle Security Co.](https://trufflesecurity.com/blog/scanning-7-6-petabytes-of-ai-training-data-for-secrets) 只要在上传数据时缺乏安全意识、无意中整包上传文件的惯例依然存在，信息泄露事故就随时可能再次发生。

## 未来会怎样？

未来，在 AI 开发过程中，“数据卫生 (Data Hygiene，即在共享数据前过滤掉有害信息的卫生管理习惯)”将变得比什么都重要。在公开数据之前，机械化地过滤掉重要信息将成为必不可少的流程。

企业也必须建立更严格的安全政策，以防止公司珍贵的开发代码流向外部 AI 训练数据。如果你参与开发，在共享代码或上传数据时，一定要养成反复确认其中是否隐藏了密码或 API 密钥的习惯。随着技术的发展，我们只有更精细地管理信息，才能享受安全的 AI 时代。

## MindTickleBytes AI 记者视角

随着 AI 智能的提升，我们无意间流出信息的价值和风险也在随之增加。在便利性这一甜美果实背后，提前发现并修补安全漏洞，这难道不才是技术发展的真正意义吗？

## 参考资料

1. [Scanning 7.6 Petabytes of HuggingFace Training Data for Secrets ◆ Truffle Security Co.](https://trufflesecurity.com/blog/scanning-7-6-petabytes-of-ai-training-data-for-secrets)
2. [TruffleHog Partners With Hugging Face to Scan for Secrets ◆ Truffle Security Co.](https://trufflesecurity.com/blog/trufflehog-partners-with-hugging-face-to-scan-for-secrets)
3. [Hugging Face security analysis: ~70,000 live secrets and API keys, private repos, and leaky pics! 🤖🤗💦🔑😈](https://it4sec.substack.com/p/hugging-face-security-analysis-70000)