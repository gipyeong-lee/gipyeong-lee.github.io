---
layout: post
title: "您还在向AI索要“答案”吗？现在是将其作为“数据厨师”使用的时刻了"
description: "您是否仅仅将大语言模型（LLM）当作获取结果的分类器来使用？现在是时候将AI作为一种智能工程工具，用于发现并结构化数据特征了。"
summary: "我们介绍了一种新的范式：不再将LLM仅仅视为数据分类的终点，而是将其作为一种“特征工程”工具，通过结构化复杂的非结构化数据来最大化预测模型的性能。"
tags: [AI, LLM, 数据分析, 机器学习, 技术趋势]
image: 2026-09-18-LLM-Classification-Is-Feature-Engineering.jpg
image_alt: "象征复杂文本数据通过AI转换成整洁表格数据过程的图像。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "仅仅将LLM视为回答问题的机器只是冰山一角。现在，AI正在演变为理解和润色数据的真正合作伙伴。"
quiz:
  - question: "在利用LLM的分类过程中，最重要的“实际力量”是什么？"
    choices: ["模型的大小", "用于分类数据的最终标签", "LLM为了分类数据而使用的推理过程"]
    answer: 2
    explanation: "最新研究强调，相比于LLM给出的标签本身，得出结论的“推理过程”在结构化复杂数据方面发挥着核心作用。"
  - question: "像LLM-FE这类框架所追求的核心目标是什么？"
    choices: ["无需人类干预的自动化特征发现", "LLM模型大小的缩减", "降低数据标注成本"]
    answer: 0
    explanation: "像LLM-FE这样的工具，重点在于利用LLM的知识和推理能力，自动发现适合表格数据（Tabular Data）的特征。"
  - question: "关于使用LLM进行特征工程的优点，描述正确的是？"
    choices: ["不再需要机器学习模型", "提高预测模型的可解释性和准确性", "彻底废除数据清洗过程"]
    answer: 1
    explanation: "利用LLM不仅可以提高现有预测模型的预测能力，还能使预测依据更容易被理解，从而提高可解释性。"
lang: zh-cn
ref: 2026-09-18-LLM-Classification-Is-Feature-Engineering
---

想象一下。您的办公桌上堆积着数万份客户咨询日志。要一一阅读并掌握内容简直令人望而却步。过去，我们通常会命令AI“请帮我分类这些咨询的内容”，然后只获取最终结果。但最近在AI领域，人们开始将这个过程视为一种让数据变得更有价值的“烹饪”，而非单纯的“分类”。

这不仅仅是信任AI给出的结果，而是利用AI感知上下文的细腻能力，将其作为一种能够将数据打磨得更适合使用的**“特征工程（Feature Engineering）”**工具。在这里，特征工程是指将数据加工成机器学习模型易于理解的核心信息的过程。

### 为什么这很重要？

到目前为止，对于我们而言，大语言模型（LLM）一直是一个回答问题或撰写文章的智能秘书。但在实际工作现场，相比于这个秘书给出的答案，其为了得出答案而使用的“知识”本身，往往具有更大的价值。

如果仅将AI用作分类器，当AI给出错误答案时，我们往往束手无策；但将其用作数据加工者，情况则完全不同。基于AI提取的结构化信息，运行现有的传统机器学习模型（例如 XGBoost），预测准确度会大幅提升。也就是说，AI现在不再是预测的主角，而是成为了让预测变得更准确的最强“助手” [出处: LLM Classification Is Feature Engineering | Minimally Sufficient](https://minimallysufficient.com/posts/llm-classification-is-feature-extraction/) [出处: Stop Labeling, Start Engineering: The New Era of LLM ...](https://www.machucavalley.tech/blog/llm-classification-as-feature-engineering/)。

### 轻松理解：AI是一位出色的翻译家

“特征工程”这个词听起来很难吗？打个比方，AI是一位非常出色的“翻译家”。想象一下，您需要阅读非常复杂且杂乱的外语文档，并整理核心内容表格。

*   **传统方式（分类）**：命令AI“告诉我这份文档是积极的还是消极的”，然后贴上“积极”这样一个标签。剩下的丰富信息全被丢弃了。
*   **新方式（特征工程）**：将AI用作智能翻译家。AI阅读文档，提取出“这位客户对配送速度不满，对价格满意，并有复购意向”这样的核心信息。然后，将其整理成“配送满意度”、“价格评分”等项目。

这样整理出来的信息，变成了计算机最易于理解的形态。 [出处: Feature engineering from LLM outputs | Xgboost Advanced Course | The Neural Base](https://theneuralbase.com/xgboost/learn/advanced/feature-engineering-from-llm-outputs/)。在此过程中，AI为得出分类结论而使用的逻辑推理过程本身，就成了数据的核心特征（Feature） [出处: Stop Labeling, Start Engineering: The New Era of LLM ...](https://www.machucavalley.tech/blog/llm-classification-as-feature-engineering/)。

### 现状：进展如何？

相关技术已经活跃地应用于现场。

1.  **自动化特征发现**：像 FeatLLM 或 LLM-FE 这样的框架，利用AI的知识和推理能力，自动发现人类难以逐一寻找的数据特征 [出处: Large Language Models Can Automatically Engineer Features for ...](https://arxiv.org/html/2404.09491v1) [出处: LLM-FE: Automated Feature Engineering for Tabular Data with ...](https://arxiv.org/html/2503.14434v1)。
2.  **性能的飞跃性提升**：研究结果显示，当利用基于LLM的数据加工时，传统机器学习模型的性能得到了压倒性的改善。一项研究显示，在19个数据集中，该方法以最低的排名（1.47）证明了其最佳性能 [出处: LLM-FE: Automated Feature Engineering for Tabular Data with LLMs as Evolutionary Optimizers [Quick Review]](https://liner.com/review/llmfe-automated-feature-engineering-for-tabular-data-with-llms-as)。甚至在复杂的分类任务中，将预测误差指标——布莱尔分数（Brier Score）从0.26降低到0.13，减少了近一半 [出处: LLM Classifiers: Cut Brier Score 0.26 to 0.13 | explainx.ai ...](https://www.explainx.ai/blog/llm-classification-feature-engineering-calibration-2026)。
3.  **便捷的访问**：现在是一个无需从零开始重新训练模型（Fine-tuning），只需通过精心设计的提示词（指令）就能执行此类高级工作的时代 [出处: How to UseLLMforClassification](https://blog.usro.net/2024/11/how-to-use-llm-for-classification/)。

### 未来将会如何？

未来，比起直接构建AI模型，“使用哪种AI作为数据加工者”以及“如何向AI提问使其更好地理解数据”，将成为工程师最重要的能力。像 FeRG-LLM 那样通过推理结果创建特征的方式（FeRG-LLM展示了比现有大型模型更高效、更卓越的性能）预计将成为主流 [出处: FeRG-LLM : Feature Engineering by Reason Generation Large Language Models [Quick Review]](https://liner.com/review/fergllm-feature-engineering-by-reason-generation-large-language-models)。

数据现在不再是原石本身，通过AI这一精细工具将其打磨成宝石的过程，将成为必经之路。

---

### MindTickleBytes 的 AI 记者视角
LLM 不是得出正确答案的“考试机器”，而是辨别何为重要的“显微镜”。我们不应满足于AI的答案，而应借用AI寻找答案的“眼睛”，让我们的数据变得更有价值。

## 参考资料

1. [LLM Classification Is Feature Engineering | Minimally Sufficient](https://minimallysufficient.com/posts/llm-classification-is-feature-extraction/)
2. [Stop Labeling, Start Engineering: The New Era of LLM ...](https://www.machucavalley.tech/blog/llm-classification-as-feature-engineering/)
3. [LLM Classifiers: Cut Brier Score 0.26 to 0.13 | explainx.ai ...](https://www.explainx.ai/blog/llm-classification-feature-engineering-calibration-2026)
5. [Large Language Models Can Automatically Engineer Features for ...](https://arxiv.org/html/2404.09491v1)
6. [LLM-FE: Automated Feature Engineering for Tabular Data with ...](https://arxiv.org/html/2503.14434v1)
9. [LLM-FE: Automated Feature Engineering for Tabular Data with LLMs as Evolutionary Optimizers [Quick Review]](https://liner.com/review/llmfe-automated-feature-engineering-for-tabular-data-with-llms-as)
10. [Feature engineering from LLM outputs | Xgboost Advanced Course | The Neural Base](https://theneuralbase.com/xgboost/learn/advanced/feature-engineering-from-llm-outputs/)
12. [FeRG-LLM : Feature Engineering by Reason Generation Large Language Models [Quick Review]](https://liner.com/review/fergllm-feature-engineering-by-reason-generation-large-language-models)
15. [How to UseLLMforClassification](https://blog.usro.net/2024/11/how-to-use-llm-for-classification/)