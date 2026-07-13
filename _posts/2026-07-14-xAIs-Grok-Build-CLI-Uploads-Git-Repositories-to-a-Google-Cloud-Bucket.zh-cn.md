---
layout: post
title: "我的代码正被偷偷传送到 AI 服务器？“Grok Build”安全争议始末"
description: "安全分析结果显示，开发者常用的 xAI Grok Build CLI 工具正在未经许可的情况下，将用户的整个代码库发送到其服务器。"
summary: "xAI 的“Grok Build”工具被证实会在未经用户允许的情况下，自动将所有代码及敏感信息上传至云端服务器，引发了巨大争议。"
tags: [AI, 安全, Grok, xAI, 开发者]
image: 2026-07-14-xAIs-Grok-Build-CLI-Uploads-Git-Repositories-to-a-Google-Cloud-Bucket.jpg
image_alt: "象征数据从电脑屏幕泄露至云端的数字艺术作品"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "企业级解决方案的核心在于“信任”。此次事件表明，缺乏透明度的数据收集行为会瞬间摧毁用户的信任，这是极具痛点的教训。"
quiz:
  - question: "此次安全分析揭露的“Grok Build”的问题是什么？"
    choices: ["仅发送了用户指令要求读取的文件", "在未经用户许可的情况下上传了整个 Git 仓库及敏感配置值", "对数据进行了加密并安全存储"]
    answer: 2
    explanation: "分析结果显示，该工具会自动将整个仓库（包括用户未明确要求读取的文件及敏感安全密钥）上传至云端服务器。"
  - question: "目前该数据传输问题处理得如何了？"
    choices: ["经查没有任何问题", "xAI 已正式发布道歉声明", "在公开后似乎已通过隐藏的服务器端设置停止了传输"]
    answer: 2
    explanation: "目前已知该传输已通过服务器端设置停止，但 xAI 尚未就数据保留及删除政策发表官方立场。"
  - question: "开发者需要了解的最重大风险是什么？"
    choices: ["电脑运行速度变慢", "环境变量（.env）中包含的敏感 API 密钥等可能被泄露至外部", "Git 记录会被删除"]
    answer: 1
    explanation: "该工具甚至将包含敏感信息的所有环境文件（如 .env 等）发送到了服务器，可能导致严重的安全隐患。"
lang: zh-cn
ref: 2026-07-14-xAIs-Grok-Build-CLI-Uploads-Git-Repositories-to-a-Google-Cloud-Bucket
---

想象一下，你把家门的密码记在纸条上并锁在抽屉深处，但当你叫来保洁服务时，清洁工竟然把抽屉里的所有东西通通装进箱子，带回他们公司的保险库去了。

近期，许多开发者使用的 AI 编码助手——xAI 的“Grok Build CLI”工具被曝存在类似的严重安全问题，引发了巨大争议。据 [AI Weekly](https://aiweekly.co/alerts/xai-grok-cli-uploads-full-repos-and-secrets-opt-out-ignored) 报道，与该工具“本地优先（local-first，即直接在你的电脑上运行）”的营销口号不同，它实际上正在暗中将用户的完整 Git 仓库内容传输到特定的云端服务器。

## 为什么这很重要？

这个问题不仅仅是“窃取了一点代码”那么简单。这意味着公司内部使用的代码、包含客户个人隐私的敏感文件，甚至是用于服务连接的“机密密钥（如 .env 文件等）”全都流向了 AI 公司的服务器。 [byteiota](https://byteiota.com/grok-build-cli-uploads-repo-xai-servers/) 指出，该工具甚至抓取了用户根本不想展示给 AI 的所有文件。

对于开发者而言，代码不仅是资产，更是知识产权。未经授权的数据收集直接违反了企业安全策略，如果这些信息被黑客攻击或泄露，可能导致难以估量的安全事故。 [GIGAZINE](https://gigazine.net/gsc_news/en/20260713-grok-build-sending-data/) 认为，该工具在未经用户明确同意的情况下收集代码，是其最严重的问题。

## 通俗地讲

让我们用一个简单的类比：想象你正在使用一款照片编辑应用。你只想挑选一张照片进行修饰，但每当你打开一张照片时，该应用就会把你手机里的“整个相册”全部复制并发送到他们的云端服务器。根据 [GitHub 的安全分析结果](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547)，无论 AI 是否真正为了工作而读取了这些文件，Grok Build 工具都会将当前工作目录中的所有文件及完整的 Git 记录上传到一个名为“grok-code-session-traces”的云端存储库中。 [Hasty Briefs](https://hb.int2inf.com/en/s/item/A8Cux9a7WKyFuJcdKfPNER-Grok-Build-CLI-data-exfiltration-analysis) 分析指出，在此过程中，敏感的安全密钥甚至通过其他通道被一并发送。

## 目前状况如何？

随着安全专家的分析和公开披露，[国际网络文摘 (International Cyber Digest)](https://x.com/IntCyberDigest/status/2076689215258014069) 表示，该上传行为已通过隐藏的服务器端设置被中止。然而，用户依然感到不安，因为 xAI 至今未就这些数据为何及如何被收集，以及是否已经安全删除了用户流向服务器的代码给出任何官方说明。 [ABAB News](https://www.ababnews.com/news/6632002b-468e-426c-84a4-832f6d8d89dc) 也指出，这种不透明导致用户的担忧正在日益加剧。

## 未来将会怎样？

以此事件为契机，开发者在引入外部 AI 工具时，势必会采取更严格的安全审核流程。像 [wetlink](https://github.com/wetlink/grok-build-privacy-hardening) 这样的开源项目，已经开始自行开发“关闭开关（kill switch，当问题发生时强制关闭功能的安全机制）”来保护用户数据。未来，企业在引入 AI 工具时将进一步加强内部安全审计；而像 xAI 这样的服务提供商，如果不能证明其透明度，恐怕将难以挽回用户的信任。

## MindTickleBytes AI 记者的看法

技术虽然便利，但对于用户而言，不知道幕后正在进行哪些数据交换始终是一个巨大的风险。特别是对于处理代码等重要资产的工具，必须建立在“信任”的基础之上。xAI 需要就此事进行更透明的沟通，并对用户代码的安全性承担起应有的责任。

## 参考资料

1. [xAI Grok CLI Uploads Full Repos and Secrets, Opt-Out Ignored | AI Weekly](https://aiweekly.co/alerts/xai-grok-cli-uploads-full-repos-and-secrets-opt-out-ignored)
2. [What xAI Grok Build CLI actually sends to xAI - a wire-level analysis (grok 0.2.93) · GitHub](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547)
3. [International Cyber Digest on X: "‼️ BREAKING: xAI's Grok Build CLI was uploading entire Git repositories to a Google Cloud bucket, private codebases and unredacted secrets included..."](https://x.com/IntCyberDigest/status/2076689215258014069)
4. [Grok Build CLI Uploads Your Entire Repo to xAI Servers | byteiota](https://byteiota.com/grok-build-cli-uploads-repo-xai-servers/)
5. [Grok Build CLI Exposed for Uploading Complete Repositories and Sensitive Files - ABAB News](https://www.ababnews.com/news/6632002b-468e-426c-84a4-832f6d8d89dc)
6. [GitHub - cereblab/grok-build-exfil-repro](https://github.com/cereblab/grok-build-exfil-repro)
7. [Grok Build CLI Repository Uploads, What the Wire Capture Proved](https://www.penligent.ai/hackinglabs/grok-build-cli-repository/)
10. [GitHub Gist](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547.pibb)
11. [What xAI's Grok Build CLI Actually Sends to xAI | Hasty Briefs](https://hb.int2inf.com/en/s/item/A8Cux9a7WKyFuJcdKfPNER-Grok-Build-CLI-data-exfiltration-analysis)
12. [xAI's Grok CLI Reportedly Uploads User Codebases and Keys ...](https://cb-terminal.dev/en/topic/6d9cba8e-8783-476a-92e5-f604bda29091)
13. [Investigations reveal that Grok Build transmitted... - GIGAZINE](https://gigazine.net/gsc_news/en/20260713-grok-build-sending-data/)
14. [wetlink/grok-build-privacy-hardening](https://github.com/wetlink/grok-build-privacy-hardening)