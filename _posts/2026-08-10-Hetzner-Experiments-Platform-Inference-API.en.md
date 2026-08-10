---
layout: post
title: "Is my computer running AI locally? What is Hetzner's new AI experiment?"
description: "We take an easy look at the features and potential of the experimental AI inference API service unveiled by the famous European data center company, Hetzner."
summary: "We explore the experimental, free OpenAI-compatible AI inference API service that Hetzner provides using its data center infrastructure."
tags: [AI, Hetzner, Infrastructure, Inference API]
image: 2026-08-10-Hetzner-Experiments-Platform-Inference-API.jpg
image_alt: "A modern graphic image symbolizing Hetzner's data center and AI technology"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Hetzner's move suggests that a powerful, cost-effective competitor could emerge in the AI infrastructure market. If it moves beyond the experimental stage to become a full service, it will become a major option for developers."
quiz:
  - question: "What are the features of Hetzner's new AI inference API?"
    choices: ["Monthly fixed subscription fee", "API method compatible with OpenAI standard SDK", "Requires downloading models directly"]
    answer: 1
    explanation: "Hetzner's inference API is designed to be compatible with OpenAI's standard SDK and REST API, allowing the use of existing tools as they are."
  - question: "What is the current status of Hetzner's inference API service?"
    choices: ["Official commercial service", "Paid access for everyone", "Experimental stage with no service guarantee (SLA)"]
    answer: 2
    explanation: "It is currently in an experimental stage and is an experimental platform with no billing or Service Level Agreement (SLA)."
  - question: "How can one use the Hetzner inference API?"
    choices: ["Generate an API token from the Hetzner Experiments dashboard", "Consult via phone", "Must install specific software"]
    answer: 0
    explanation: "You must access the Hetzner Experiments dashboard and generate an API token yourself to use the service."
lang: en
ref: 2026-08-10-Hetzner-Experiments-Platform-Inference-API
audio: 2026-08-10-Hetzner-Experiments-Platform-Inference-API.en.mp3
industry: creative
---

Imagine this: What if the AI service you enjoy using was actually operating like a component in a giant factory? When we ask a question to an AI like 'ChatGPT,' a data center somewhere receives that question, performs complex calculations, and sends back an answer. Recently, Hetzner, a famous European data center company, began an 'experiment' that signals a new change in this process. What exactly is this change?

### Why does this matter?

For those who use AI in their daily lives, this news might not be an immediate, major change. However, for developers and startup employees, this is very welcome news. Hetzner is currently providing an [experimental AI Inference API](https://docs.hetzner.com/general/company-and-policy/experiments/inference/) for free, which is similar to giving away a free 'toolbox' that allows anyone to easily add AI features to their services.

Is the term 'API' unfamiliar? Simply put, just as a food delivery app connects us to a restaurant when we order food with a smartphone, an API is a technology that builds a bridge so that service developers can easily use AI technology.

Especially for early-stage startups that are just starting out, an environment where they can pay only for what they use and operate AI models efficiently is crucial. [Hetzner's inference service is expected to open up new possibilities for such companies to utilize high-performance models at a low cost](https://devsandlogics.com/blog/hetzner-is-working-on-llm-inference).

### Understanding it easily: How to borrow AI's 'hard-earned knowledge'

Does the term 'Inference' sound difficult? To use an analogy, if the process of an AI memorizing an entire library of books is 'training,' then the process of finding an answer based on that knowledge when we ask a question is 'inference.'

Hetzner has started a service that processes this 'inference' step using the European data center infrastructure they own. [Users only need to issue an API token from the Hetzner Experiments dashboard](https://emit-solution.com/en/blog/hetzner-ai-inference-api) to connect this AI model to their programs in a very familiar way, just like using OpenAI's service. [This is because it fully supports the standard OpenAI SDK and common web communication protocols (REST API)](https://emit-solution.com/en/blog/hetzner-ai-inference-api).

It's like choosing a filter in a smartphone photo app; you just need to simply apply the 'Qwen3.6-35B' model, one of the high-performance AI models prepared by Hetzner, to your service. It's the equivalent of hiring an expert-level AI as your app's assistant without any complex installation.

### Current status: It's still in the 'laboratory'

However, there is something to keep in mind. Hetzner clearly states that this service is [currently in an experimental state](https://docs.hetzner.com/general/company-and-policy/experiments/inference/).

- **No official pricing policy:** While it is currently free, [it is unknown how long it will remain free or if it will be converted to an official service later](https://sliplane.io/blog/hetzner-inference).
- **No Service Level Agreement (SLA):** Since there is no 'Service Level Agreement (SLA)' that businesses can rely on, there is still a risk in applying it directly to critical business systems. An 'SLA' is a type of promise that the service will not stop and will operate stably, but currently, it is in a free, experimental stage without this promise. [The models offered are also currently limited to one (Qwen3.6-35B-A3B-FP8)](https://aitodaybrief.com/en/news/tools-and-releases/hetzner-launches-free-experimental-openai-compatible-llm-inference-api).

Nevertheless, the performance is surprisingly good. [According to unofficial measurements, it takes only about 0.15 seconds (153ms) to get the first character after asking a question, and it is fast enough to generate 224 words per second](https://mindpattern.ai/s/2026-07-24-hetzner-is-quietly-testing-free-openai-compatible-inference). This is supported by the infrastructure efficiency of Hetzner, which operates its own data centers.

### What will happen next?

Through this service, Hetzner is [testing how much market demand there is and how stably their data centers can handle AI tasks](https://emit-solution.com/en/blog/hetzner-hosted-openclaw-experiment).

If Hetzner successfully completes this experiment and adds more models or turns it into an official service in the future, a world will come where many developers who were worried about high costs can utilize AI technology more freely. Above all, as a European company that values data sovereignty, it is worth noting that they are proposing an alternative that allows the use of powerful AI features while maintaining direct control over data.

### MindTickleBytes' AI Reporter View

Hetzner's attempt is more interesting from the perspective of the 'democratization of infrastructure' than the technology itself. It is a signal that traditional infrastructure companies operating efficient data centers have begun to share the AI processing power that was previously monopolized by giant IT companies in earnest. This may bring about a change similar to a neighborhood electrician finding a way to run our home appliances more efficiently, rather than a large electric utility company doing so.

## References

1. [HetznerInference: the new AIAPIserving... | EMIT Solution](https://emit-solution.com/en/blog/hetzner-ai-inference-api)
2. [HetznerLaunches FreeExperimentalOpenAI-Compatible LLM... | AITodayBrief](https://aitodaybrief.com/en/news/tools-and-releases/hetzner-launches-free-experimental-openai-compatible-llm-inference-api)
3. [[Feature]: Hi Teknium/Nous, please add support forHetznerAI... | GitHub Issues](https://github.com/NousResearch/hermes-agent/issues/73423)
4. [The frontier labs are building a productHetznerwill sell like bandwidth | LinkedIn](https://www.linkedin.com/pulse/frontier-labs-building-product-hetzner-sell-like-bandwidth-ben-luong-1mjtc)
5. [Hetzner Inference: First Look | Sliplane Blog](https://sliplane.io/blog/hetzner-inference)
6. [Hetzner now hosts OpenClaw: free AI assistant instances as an experiment | EMIT Solution](https://emit-solution.com/en/blog/hetzner-hosted-openclaw-experiment)
7. [Hetzner Enters LLM Inference: What It Means for SaaS Builders in 2026 | Devs & Logics Blog](https://devsandlogics.com/blog/hetzner-is-working-on-llm-inference)
8. [Inference API - Hetzner Docs](https://docs.hetzner.com/general/company-and-policy/experiments/inference/)
9. [Experiments Platform - Overview - Hetzner Docs](https://docs.hetzner.com/general/company-and-policy/experiments/experiments-platform/)
10. [Hetzner is quietly testing free OpenAI-compatible inference. | MindPattern AI](https://mindpattern.ai/s/2026-07-24-hetzner-is-quietly-testing-free-openai-compatible-inference)
11. [Hetzner Tests LLM Inference with Qwen on Its Own ... | Zeli App](https://zeli.app/en/story/49033087)
12. [Hetzner Inference: First Look | Jonas Scholz - LinkedIn](https://www.linkedin.com/posts/jonas-scholz-490274163_hetzner-inference-first-look-activity-7486346679424593922-htYe)
13. [Hetzner testet LLM-Inference-API mit Qwen3-Modell und 262K ... | Lumeric](https://www.lumeric.app/post/02b73ec9-f9f8-4572-aa06-e79935340a86)