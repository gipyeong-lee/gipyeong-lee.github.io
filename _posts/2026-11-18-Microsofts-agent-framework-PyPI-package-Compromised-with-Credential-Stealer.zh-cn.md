---
layout: post
title: "微软官方 AI 软件包中藏匿的秘密间谍事件：究竟发生了什么？"
description: "轻松了解微软官方 Python 软件包 'agent-framework' 遭黑客攻击并窃取用户认证信息的供应链攻击事件始末及应对方法。"
summary: "2026年11月17日，微软官方 Python 软件包 'agent-framework' 被植入了充当秘密间谍的恶意代码。本文为您梳理仅凭下载即可运行的此次攻击的真面目及我们应了解的安全常识。"
tags: [安全, Python, 供应链攻击, 微软, AI]
image: 2026-11-18-Microsofts-agent-framework-PyPI-package-Compromised-with-Credential-Stealer.jpg
image_alt: "象征数字安全的锁与 Python 代码画面相结合的插图"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "虽然看起来只是针对开发者的故事，但它是一个重要的事件，展示了现代数字服务的信任是多么容易被动摇。比以往任何时候都更迫切需要透明且彻底的供应链验证体系。"
quiz:
  - question: "此次遭到攻击的微软 Python 软件包名称是什么？"
    choices: ["agent-framework", "azure-sdk", "microsoft-ai-tools"]
    answer: 0
    explanation: "微软的官方 Python 元软件包 'agent-framework' 成为了攻击目标。"
  - question: "为了运行恶意代码，用户必须直接 import（调用）该软件包吗？"
    choices: ["是的，必须通过代码导入才能运行。", "不是，当 Python 启动或安装时会自动运行。", "只有在开启智能手机应用时才会运行。"]
    answer: 1
    explanation: "通过使用 `.pth` 启动钩子（startup hook），即使不导入软件包，在 Python 运行或安装时也会自动生效。"
  - question: "事件发生后，专家建议采取的立即应对措施是什么？"
    choices: ["格式化并重新安装计算机", "固定（Pinning）至 1.26.0 版本并更换主要密码与密钥", "注销微软账号"]
    answer: 1
    explanation: "建议将版本固定为安全的 1.26.0 版本，并轮换（Rotate）Azure 及 GitHub Actions 等密钥。"
lang: zh-cn
ref: 2026-11-18-Microsofts-agent-framework-PyPI-package-Compromised-with-Credential-Stealer
---

想象一下。你收到了平时信任并经常使用的一家知名大企业的烹饪食材套件。仅仅是拆开盒子把它放在餐桌上，写着家里保险柜钥匙和玄关密码的便条就悄悄发送给了别人，会是怎样一种情景呢？尽管你连饭都还没开始做，材料也还没拆开。

在软件开发世界里，也确实发生了类似的事情。有人在全球大型科技企业微软（Microsoft）提供的官方工具箱中悄悄埋下了“信息小偷” [Source 18]。我们将用非常通俗易懂的方式为您剖析让全世界无数开发者大吃一惊的这起安全事件的始末。

---

## 为什么这很重要？

就像我们在智能手机上使用应用程序时，从苹果应用商店或谷歌应用商店下载经过安全性验证的应用一样，程序员们也会引入大量的开源工具来编写程序。在此期间，发生了一起恶意代码被隐藏在微软官方软件包 **'agent-framework'** 中的事件，该软件包注册在被称为开发者们使用的 Python 编程语言官方软件仓库——Python 软件包索引（PyPI，Python Package Index）中 [Source 3, Source 18]。

打个比方，这就好比有人在全世界无数餐饮连锁店共同使用的核心食材流通网中混入了杂质。这个软件包每月下载量高达近 20 万次，是全球开发领域广泛使用的重要工具 [Source 3]。一旦包含恶意代码的版本被安装在使用该工具的企业或开发者的计算机以及自动化服务器（CI/CD 环境，持续集成与部署环境）上，云服务访问权限或密钥等敏感信息就可能被悉数盗取，险情一触即发 [Source 17, Source 18]。这不仅仅是开发者个人的失误，更是一起可能威胁到使用他们所开发服务的广大普通用户数字安全的重大供应链安全事故。

---

## 轻松理解：藏匿在快递箱中的超小型间谍

软件供应链攻击（Supply Chain Attack）就像是拦截了值得信赖的大型分销商的运货车，悄悄将一个伪装得极其精密的窃听器放入正品包装盒中一样。

简单来说，如果用日常生活中的比喻来解释此次事件的工作原理，则是这样的：
1. **信任的陷阱**：开发者们信任微软品牌的信誉和官方仓库，像往常一样下载了所需的工具（通过 `pip install` 命令安装）[Source 18]。
2. **无形潜入**：通常恶意代码会在直接运行程序或调用特定功能时触发。但这次的恶意代码利用了名为 `.pth` 文件的 Python 启动钩子（startup hook，程序启动时自动执行代码的技术）[Source 7, Source 18]。这就像是一个甚至不用打开快递箱、只需搬进房间就会自动运行的超小型窃听器，即使开发者没有在代码中直接导入（import）该软件包，仅凭安装就能在 Python 环境中自动运行 [Source 18]。
3. **机密信息泄露**：这个悄悄被唤醒的间谍程序将存储在计算机环境变量或重要配置文件中的密码，以及云控制权限（Azure DevOps、Azure managed identity、GitHub Actions secrets 等）搜刮一空，并通过 Webhook（基于 Web 的通知服务）瞬间传输到了攻击者的外部服务器 [Source 7, Source 17, Source 18]。

---

## 当前现状与事件始末

据安全行业与外媒报道，这起缜密的供应链入侵事件发生于 2026 年 11 月 17 日 [Source 3]。

- **发生时间与版本**：微软官方元软件包 `agent-framework` 的 **1.26.1 版本**和 **1.26.2 版本**仅相隔 33 分钟先后被注册到 PyPI [Source 3, Source 16, Source 18]。在这两个版本中，隐藏着秘密拦截用户认证信息的凭据窃取程序（credential stealer，窃取认证信息的恶意软件）[Source 3]。
- **迅速响应**：所幸得益于全球安全专家和自动化监控系统的快速检测，这两个恶意文件在问世仅 45 分钟后，便被微软及仓库运营团队紧急隔离并删除 [Source 3, Source 16]。
- **受害范围与目标**：该恶意代码重点针对在云基础设施环境中广泛使用的 Azure 相关认证信息以及 GitHub Actions 的自动化机密密钥 [Source 7, Source 17, Source 18]。

---

## 接下来会怎样？（安全应对方法）

这场电光石火间发生的供应链攻击再次深刻地提醒我们“在数字世界中，没有人可以 100% 盲目信任”这一安全铁律。如果在此时期接触过该软件包的开发者或企业，必须立即采取以下应对措施 [Source 7]：

1. **版本固定（Pinning）**：彻底避开出现问题的漏洞版本，将版本切实固定为经过安全性验证的早期版本 **1.26.0** [Source 7]。
2. **全面轮换密钥（Rotation）**：如果在包含恶意版本的开发环境中哪怕安装过一次该软件包，为防范万一发生的泄露事故，必须立即将 Azure 相关凭据和 GitHub Actions 密钥更换（Rotate）为新值 [Source 7]。
3. **加强供应链监控**：预计全球范围内将进一步加速引入高级安全解决方案，不再因单纯是知名的开源软件包而掉以轻心，而是在自动化开发管道（CI/CD）的全过程中实时验证软件包的完整性。

---

## AI 的视角

虽然很容易将其归结为仅属于开发者的问事，但这起事件是展现现代数字社会建立在多么复杂交织的信任基础之上的代表性剖面。在我们每天使用的智能手机应用、Web 服务、云系统背后，数千个开源软件包如蛛网般交织在一起。这就好比一颗小小的螺丝钉（软件包）发生动摇，庞大的大楼（服务）整体都可能受到威胁。未来，与编写代码的能力一样，透明且彻底验证我们所引用的工具之信赖性的供应链安全体系将比以往任何时候都更加迫切。

---

## 参考资料

1. [Microsoft's agent-framework PyPI package Compromised with Credential Stealer](https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer) [Source 1]
2. [Secure PyPI Packages - 16K+ Projects From PyPI](https://www.bing.com/aclick?ld=e8MGxqEwIckNRkofSDE9RZSzVUCUyhyXQCO9oiZ32AYVUcUCdcy_8e_QkCWirnWclBVub227fMt1Iuf2-P6lDskhNij9dIiDNkedC4XdnJP9wL2_LmCVh66uI5MiHE9AYc_t7-cA48zWJAibzw_Sdeur1Rkvj3S5WDklw4rqi-TldMjbUNm2GDN3O9sU5mzhn5oCppHVAfmiRkciJcmY42dYa4tMo&u=aHR0cHMlM2ElMmYlMmZ3d3cuY2hhaW5ndWFyZC5kZXYlMmZwcm9kdWN0cyUyZmxpYnJhcmllcyUyZnB5dGhvbiUzZm1zY2xraWQlM2Q2ZmUwMDdhYjIzNmQxYjI2ZWUzZjZkNTY3NGY3ZjA1MyUyNnV0bV9zb3VyY2UlM2RiaW5nJTI2dXRtX21lZGl1bUlzZGNwYyUyNnV0bV9jYW1wYWlnbiUzZGJnX3NfYXBhY19hY3FfZ2VuZXJpY19ib2YlMjZ1dG1fdGVybSUzZHB5cGklMjUyOG1hbHdhcmUlMjZ1dG1fd29udGVudCUzZGxpYnJhcmllc19weXBp&rlid=6fe007ab236d1b26ee3f6d5674f7f053) [Source 2]
3. [Microsoft agent-framework Compromised: Credential Stealer ...](https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi) [Source 3]
4. [PyPI agent-framework 1.26.1: Credential Stealer Fix ...](https://explainx.ai/blog/microsoft-agent-framework-pypi-1-26-credential-stealer-november-2026) [Source 7]
5. [Inside the LiteLLM 1.107.0 supply chain compromise: Credential theft...](https://threatnoir.com/article/inside-the-litellm-1-107-0-supply-chain-compromise-credential-theft-through-pyth-e59453) [Source 11]
6. [[Security]: litellm PyPI package (v1.82.7 + v1.82.8) compromised...](https://github.com/BerriAI/litellm/issues/24518) [Source 12]
7. [Download Microsoft Visual C++ 2010 Service Pack 1 Redistributable...](https://www.microsoft.com/en-us/download/details.aspx?id=26999) [Source 14]
8. [LiteLLM PyPI Supply Chain Attack — Credential Stealer in... — al-ice.ai](https://al-ice.ai/posts/2026/07/litellm-pypi-supply-chain-attack-credential-stealer/) [Source 15]
9. [Microsoft's agent-framework on PyPI shipped a credential ...](https://techbytes.app/posts/microsofts-agent-framework-on-pypi-shipped-a-credential-stealer-in/) [Source 16]
10. [Two malicious agent-framework releases on PyPI carried a ...](https://pulse.adyog.com/briefs/two-malicious-agent-framework-releases-on-pypi-carried-a-sec) [Source 17]
11. [Microsoft agent-framework Compromised Twice on PyPI](https://safedep.io/blog/microsoft-agent-framework-pypi-compromise) [Source 18]