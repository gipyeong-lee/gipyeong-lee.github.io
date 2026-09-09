---
layout: post
title: "AI 窃取 AI？美国政府警告中国进行模型蒸馏（Distillation）运动"
description: "有指控称，中国 AI 企业正在大规模复制美国的尖端 AI 模型。我们为您简要介绍“模型蒸馏”技术是如何被滥用于工业间谍活动的。"
summary: "美国情报机构和联邦调查局（FBI）发出警告称，中国主要 AI 企业正在系统性地窃取美国领先 AI 模型的功能，并将其用于自身技术开发。"
tags: [AI, 安全, 技术争端, 中国AI]
image: 2026-09-09-Chinese-AI-Companies-Conducting-Distillation-Campaigns-Against-US-AI-Companies-p.jpg
image_alt: "在复杂数字网络中数据被提取和传输的科技感抽象图像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 模型是数万亿投资和天文数字计算能力的结晶。技术的复制不仅仅是简单的竞争，可能演变成严重阻碍 AI 生态系统公平发展的重大问题。"
quiz:
  - question: "文中提到的“模型蒸馏（Distillation）”技术在文中的负面应用方式是什么？"
    choices: ["收集用于训练 AI 模型的数据", "通过未经授权的 API 访问提取模型结果以复制功能", "从服务器中删除 AI 模型"]
    answer: 1
    explanation: "模型蒸馏原本是制造高效模型的研究技术，但如果被滥用，可能被用作窃取其他模型功能的“对抗性蒸馏攻击”。"
  - question: "美国政府在此次运动中指控的中国企业不包括以下哪一家？"
    choices: ["DeepSeek", "Alibaba", "Google"]
    answer: 2
    explanation: "美国政府指控的对象包括 DeepSeek、Moonshot AI、阿里巴巴、MiniMax、StepFun 和 Z.AI 等。"
  - question: "据报道，中国 AI 企业为规避安全监控使用了什么方法？"
    choices: ["在单台服务器上执行所有工作", "使用数千个虚假账户", "将运营分散到多个模型提供商和云平台上"]
    answer: 2
    explanation: "据报道，中国 AI 企业为规避追踪，采取了将工作分散到多个云平台和 AI 模型提供商的方式。"
lang: zh-cn
ref: 2026-09-09-Chinese-AI-Companies-Conducting-Distillation-Campaigns-Against-US-AI-Companies-p
---

试想一下。您花费数年时间、投入数亿资金，研制出了世界上最美味的秘制酱汁。然而有一天，有人每天到您的店里少量购买酱汁，分析并开始制作、销售味道完全一样的酱汁，您会有什么感觉？现在世界 AI 行业发生的事情正如出一辙。

近日，美国情报机构和联邦调查局（FBI）发布了一份令人震惊的报告，称中国主要 AI 企业正在系统性地窃取美国尖端 AI 技术。不仅是传闻，他们更在工业现场滥用“蒸馏（Distillation）”技术，以提取竞争对手的知识产权 [参考资料 1](https://edition.cnn.com/2026/09/08/politics/us-accuses-china-of-stealing-ai-technology), [参考资料 9](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-251a)。

## 为什么这很重要？

AI 模型不仅仅是几行程序。它们是“数字资产”，需要数十亿美元的成本和顶尖研究人员耗费数年心血才能创造出来 [参考资料 2](https://cyberscoop.com/us-accuses-chinese-ai-companies-distillation/)。如果这些技术在没有正当努力的情况下瞬间被复制，投入巨资进行技术创新的企业将受到重创。此外，这与国家间的技术霸权竞争交织在一起，已经超越了单纯的企业间争斗，演变成国家安全问题 [参考资料 10](https://www.theregister.com/ai-and-ml/2026/09/09/us-claims-chinese-ai-firms-core-ai-strategy-is-distilling-american-models/5295171)。

## 轻松理解：模型蒸馏到底是什么？

原本“模型蒸馏（Knowledge Distillation，知识蒸馏）”是一项非常有用的研究技术。它指的是从一个庞大且聪明（但因过大而无法在个人电脑上运行）的巨型 AI 模型中挑选出核心知识，并将其转移到一个小型、轻量化模型中的技术 [参考资料 7](https://www.techtimes.com/articles/319105/20260625/alibaba-ran-largest-known-ai-theft-campaign-against-claude-anthropic-tells-senate.htm), [参考资料 9](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-251a)。这就像将大学教授拥有的渊博知识总结成小学生也能理解的参考书一样。打个比方，这就像分析大师所画名画的核心技法并制作仿制品（临摹）的过程。

但如果将其用于恶意目的，那就是“盗窃”。攻击者向正在服务的美国 AI 模型（如 Anthropic 的 Claude）发送数百万次提问。通过分析其回答方式，原封不动地抄袭其内部逻辑和性能 [参考资料 4](https://www.sgtreport.com/2026/02/top-ai-firm-says-chinese-labs-stole-u-s-tech-using-24000-fake-accounts/), [参考资料 7](https://www.techtimes.com/articles/319105/20260625/alibaba-ran-largest-known-ai-theft-campaign-against-claude-anthropic-tells-senate.htm)。

这样窃取的数据量高达数十亿个 Token（Token，即 AI 读取文字的最小单位，为单词或字词片段）[参考资料 3](https://www.cisa.gov/news-events/news/cisa-nsa-and-fbi-warn-china-based-ai-companies-targeting-us-ai-models-industrial-scale-knowledge)。通过这一过程，中国企业无需从零开始自主开发模型，直接将美国现成的尖端智能变成了自己的东西 [参考资料 3](https://www.cisa.gov/news-events/news/cisa-nsa-and-fbi-warn-china-based-ai-companies-targeting-us-ai-models-industrial-scale-knowledge)。

## 正在何处、如何发生？

美国当局具体点名了 DeepSeek、Moonshot AI、阿里巴巴、MiniMax、StepFun 和 Z.AI 这 6 家中国企业 [参考资料 2](https://cyberscoop.com/us-accuses-chinese-ai-companies-distillation/), [参考资料 5](https://www.ibtimes.co.uk/us-agencies-accuse-chinese-ai-firms-extracting-us-ai-model-capabilities-1818601)。特别是 Anthropic 公司声称，他们正针对自家的 AI 模型“Claude”开展大规模提取行动 [参考资料 4](https://www.sgtreport.com/2026/02/top-ai-firm-says-chinese-labs-stole-u-s-tech-using-24000-fake-accounts/)。

为了规避监控，他们展现出了精密的手段，如将作业分散到多个云平台，并动用大量账户伪装成正常用户 [参考资料 8](https://pjmedia.com/david-manney/2026/09/08/chinas-56-million-ai-miracle-just-got-a-lot-less-miraculous-n4957022)。这就像小偷为了躲避监控摄像头而分散逃窜到不同小巷一样。对此，中国政府及相关企业均表示这是美国毫无根据的指责 [参考资料 11](https://www.nbcnews.com/tech/tech-news/us-accuses-china-ai-developers-deepseek-alibaba-copying-american-ai-rcna596696)。

## 未来会怎样？

美国政府正高度重视此事，预计将加强相关法律和技术应对措施 [参考资料 6](https://udit.co/blog/openai-accuses-deepseek-model-distillation-congress)。针对 AI 模型的 API 访问限制将会提高，实时检测异常大规模请求的技术手段也会增加。预计未来，保障“保护自身技术安全”的竞争将与 AI 开发竞争同样激烈。在 AI 时代，制定全球性的知识产权保护准则刻不容缓。

## 参考资料

1. [美国声称中国 AI 公司正在进行“工业规模”的商业机密盗窃 | CNN Politics](https://edition.cnn.com/2026/09/08/politics/us-accuses-china-of-stealing-ai-technology)
2. [联邦机构指控中国“系统性”蒸馏美国 AI 模型 | CyberScoop](https://cyberscoop.com/us-accuses-chinese-ai-companies-distillation/)
3. [CISA、NSA 和 FBI 警告称，中国 AI 公司正以工业规模的知识蒸馏运动为目标窃取美国 AI 模型，以绕过 AI 开发路径 | CISA](https://www.cisa.gov/news-events/news/cisa-nsa-and-fbi-warn-china-based-ai-companies-targeting-us-ai-models-industrial-scale-knowledge)
4. [顶级 AI 公司称中国实验室使用 24000 个虚假账户窃取美国技术 | SGT Report](https://www.sgtreport.com/2026/02/top-ai-firm-says-chinese-labs-stole-u-s-tech-using-24000-fake-accounts/)
5. [美国点名六家被指控窃取的中国 AI 公司 | IBTimes UK](https://www.ibtimes.co.uk/us-agencies-accuse-chinese-ai-firms-extracting-us-ai-model-capabilities-1818601)
6. [OpenAI 在提交给国会的备忘录中指控 DeepSeek 进行模型蒸馏](https://udit.co/blog/openai-accuses-deepseek-model-distillation-congress)
7. [Anthropic 向参议院透露：阿里巴巴对 Claude 发起了已知最大规模的 AI 盗窃运动 | TechTimes](https://www.techtimes.com/articles/319105/20260625/alibaba-ran-largest-known-ai-theft-campaign-against-claude-anthropic-tells-senate.htm)
8. [中国的“560万美元 AI 奇迹”水分大了不少 | PJ Media](https://pjmedia.com/david-manney/2026/09/08/chinas-56-million-ai-miracle-just-got-a-lot-less-miraculous-n4957022)
9. [基于中国的 AI 公司正在进行的蒸馏运动 | CISA](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-251a)
10. [美国称中国 AI 公司的核心 AI 策略是蒸馏美国模型 | The Register](https://www.theregister.com/ai-and-ml/2026/09/09/us-claims-chinese-ai-companies-core-ai-strategy-is-distilling-american-models/5295171)
11. [美国指控中国 AI 开发商 DeepSeek 和阿里巴巴复制美国 AI | NBC News](https://www.nbcnews.com/tech/tech-news/us-accuses-china-ai-developers-deepseek-alibaba-copying-american-ai-rcna596696)