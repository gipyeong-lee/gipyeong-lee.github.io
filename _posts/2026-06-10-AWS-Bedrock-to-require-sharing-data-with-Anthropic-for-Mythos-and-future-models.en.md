---
layout: post
title: "AI so smart it's being 'monitored'? The secret behind Claude Mythos and data sharing"
description: "Why do you have to share data for 30 days to use Anthropic's ultra-powerful 5th-generation AI 'Mythos' and 'Fable 5' on AWS Bedrock? We explain the new security policy in an easy-to-understand way."
summary: "To prevent the misuse of 'Mythos-class' AI models that are too powerful to be released to the general public, Anthropic has introduced a new regulation on the AWS cloud that retains user data for 30 days to inspect for safety."
tags: [Artificial Intelligence, Security, Cloud, Anthropic]
image: 2026-06-10-AWS-Bedrock-to-require-sharing-data-with-Anthropic-for-Mythos-and-future-models.jpg
image_alt: "A glowing artificial intelligence brain connected to a data security padlock"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Great power must be accompanied by appropriate control. This measure is a symbolic event showing that the central axis of AI development is shifting from unconditional 'performance competition' to practical 'safety management'."
quiz:
  - question: "What is the required data retention period to use Anthropic's 'Mythos-class' AI models?"
    choices: ["7 days", "15 days", "30 days"]
    answer: 2
    explanation: "Anthropic requires a 30-day data retention period for traffic on Mythos-class models, such as Mythos 5 and Fable 5, for trust and safety purposes."
  - question: "Where is the retained user data ultimately stored?"
    choices: ["Anthropic's public training servers", "Inside the user's AWS environment", "Public cloud on the internet"]
    answer: 1
    explanation: "Even when the data sharing option is turned on, the data stays securely controlled within the customer's (user's) Amazon Web Services (AWS) environment."
  - question: "What is the core reason why Claude Mythos is only provided in a restricted manner as a private research preview?"
    choices: ["Because it is too powerful to be released to the public", "Because development is incomplete and it has many errors", "Because server maintenance costs are too high"]
    answer: 0
    explanation: "Anthropic judged that Claude Mythos demonstrated overwhelming capabilities in coding and cybersecurity, determining it 'too powerful to be released publicly,' and thus only allowed restricted access through Project Glasswing."
lang: en
ref: 2026-06-10-AWS-Bedrock-to-require-sharing-data-with-Anthropic-for-Mythos-and-future-models
audio: 2026-06-10-AWS-Bedrock-to-require-sharing-data-with-Anthropic-for-Mythos-and-future-models.en.mp3
industry: legal
---

## Introduction: A Suspicious Contract at the Magic Wand Shop

**Imagine this.** You go to a shop to rent a magic wand with extraordinary abilities that could change the world. However, the shop owner hands you a contract with a grim expression and says, "This wand is so capable that we can't just hand it out to anyone. If you want to borrow it, you must allow us to watch what magic spells you cast with it for the next 30 days."

It might sound like a story straight out of a fantasy movie, but surprisingly, this is exactly the contract condition that companies must actually agree to in order to use one of the smartest artificial intelligence (AI) systems in the world today. In April 2026, when releasing its latest 5th-generation AI models, AI specialist company Anthropic imposed a very unusual and strict new rule on Amazon Bedrock, a cloud service platform [Claude Fable 5 from Anthropic now available on Amazon Bedrock](https://www.aboutamazon.com/news/aws/claude-fable-5-anthropic-available-amazon-bedrock).

The core of the new rule is clear. To use ultra-high-performance AI like 'Mythos 5' and 'Fable 5', users must share all prompts given to the AI and all completion data it generates with Anthropic for 30 days [Anthropic Claude Fable 5 on AWS: Mythos-class capabilities ...](https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/). It's a private service that you pay for legitimately, so why on earth do your conversations have to be monitored? We will explain step-by-step in an easy-to-understand manner why such strict conditions have arisen and what this means for our digital privacy and daily lives moving forward.

---

## Why It Matters

### "Too Powerful to be Released Publicly"

The origin of this entirely unfamiliar situation is that the intelligence level of AI has now risen to a degree that surpasses our imagination. Just two years ago, in April 2024, when 'Claude 3' first appeared on Amazon Bedrock, people marveled at its smart performance and utilized the AI in their work relatively freely [Amazon Bedrock adds Claude 3 Anthropic AI models](https://www.aboutamazon.com/news/aws/amazon-bedrock-anthropic-ai-claude-3).

However, the new models that debuted on April 7, 2026, were on a completely different level. When Anthropic exclusively introduced 'Claude Mythos' to Amazon Bedrock, they themselves referred to this model they had created as **"too powerful to be released publicly"**, expressing a sense of caution [Claude Mythos is on AWS Bedrock. Here's what engineers need ...](https://dev.to/ajbuilds/claude-mythos-is-on-aws-bedrock-heres-what-engineers-need-to-know-2lhj).

That this statement was not mere marketing exaggeration or bravado was immediately proven by numbers. In the 'SWE-bench Verified', a highly authoritative test that evaluates an AI's ability to autonomously find and fix flaws in complex software, Mythos achieved a record-breaking score of **93.9%** [Claude Mythos is on AWS Bedrock. Here's what engineers need ...](https://dev.to/ajbuilds/claude-mythos-is-on-aws-bedrock-heres-what-engineers-need-to-know-2lhj). To explain this in relatable terms, it means that when given 100 of the world's most difficult programming error problems, it has reached the level of autonomously and perfectly solving 94 of them.

### To Prevent a Coding Genius from Turning into the Worst Hacker

What does this astonishing figure of 93.9% mean for ordinary people like us? It means that highly complex system errors, which dozens of human programmers might barely find and fix after staying up all night for days, can be grasped and perfectly repaired by AI in just a few seconds. In fact, 5th-generation AIs like Mythos 5 and Fable 5 boast truly overwhelming and phenomenal performance in the fields of coding, complex knowledge work, and visual information analysis (vision) [Claude Fable 5 from Anthropic now available on Amazon Bedrock](https://www.aboutamazon.com/news/aws/claude-fable-5-anthropic-available-amazon-bedrock).

However, in the world of technology, the brighter the light, the darker the shadow. 'The genius ability to find system errors incredibly well' is perfectly identical to 'the ability to precisely locate system weaknesses (vulnerabilities) and launch fatal attacks,' like two sides of a coin. Simply put, imagine a genius locksmith who knows the structure of every lock in the world inside out. This locksmith can build stronger security devices than anyone else, but if they set their mind to it, they can also open any ironclad safe without a trace.

The cybersecurity industry is taking the emergence of Mythos not just as a simple new product launch, but heavily as a flare signaling that vulnerability discovery and hacking security operations utilizing AI have entered a completely new dimension [AWS Bedrock Claude Mythos Preview: A Defensive AI Security ...](https://murtaza-arif.github.io/blog/aws-bedrock-claude-mythos-preview-glasswing-playbook). If such ultra-powerful intelligence were to fall into the hands of malicious hacker groups, they could automatically and instantly create fatal computer viruses capable of breaching global banking networks or paralyzing national communication grids.

That is why Anthropic did not leave this model open for anyone to use just by paying money. Instead, they released it to the world in a limited manner, exclusively as a strictly controlled 'gated research preview' called 'Project Glasswing' [Claude Mythos is on AWS Bedrock. Here's what engineers need ...](https://dev.to/ajbuilds/claude-mythos-is-on-aws-bedrock-heres-what-engineers-need-to-know-2lhj). It is akin to locking up an incredibly powerful and potentially dangerous beast in a very sturdy cage, allowing only permitted individuals to carefully observe it.

---

## The Explainer

So, exactly how does this 'safeguard' established by Anthropic work? The core shield they have introduced is the mandatory **'30-day data retention'** mentioned earlier.

### Installing a Black Box: 30 Days of Transparent Monitoring

Currently, to use 'Mythos-class' models in the cloud, which possess the highest level of capability humanity has reached, like Mythos 5 or Fable 5, the user must absolutely turn on a special security switch in the system settings. This is the **'provider_data_share'** option [Data retention - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html).

When this option is enabled, all questions (prompts) the user throws at the AI and all answers (completions) the AI produces in response are shared with Anthropic, the model's creator, and are securely retained for up to 30 days [Data retention - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html).

You can compare this situation to renting a piece of dangerous special heavy machinery that is very precise but could potentially cause a massive accident. The rental company hands over the equipment and says, "This equipment has a black box attached to it that cannot be turned off or tampered with. For the next 30 days, we have the right to frequently open the records to see whether you are building something with this equipment or dangerously destroying things."

The purpose of this monitoring is singular. It is to monitor whether this genius AI is being abused to design fatal weapons, automatically write large-scale hacking scripts, or conspire in serious crimes. Anthropic explains that this is an essential procedure strictly to guarantee **'trust and safety purposes'** [Data retention - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html).

### Do We Have to Give Up Our Precious Privacy?

At this point, countless companies planning to adopt AI feel a chilling sense of profound anxiety. It's a very reasonable worry: "If we ask the AI to analyze the core code of a top-secret new product we are spending tens of millions to develop, won't all that precious data be wholly transferred to Anthropic's central servers and leaked outside?"

Fortunately, the Amazon Bedrock platform and Anthropic have found a clever compromise between privacy and safety. The user's sensitive data, retained for 30 days, is not illegally taken out or copied to Anthropic's external servers. Instead, with the data retention option turned on, it is designed so that the data strictly **'stays in your AWS environment'** safely [Data retention practices for Mythos-class models | Claude Help Center](https://support.claude.com/en/articles/15425996-data-retention-practices-for-mythos-class-models).

Metaphorically, it is not that Anthropic employees take the documents written by the customer back to their company to read them. It is closer to placing the documents inside a sturdy safe located in the customer's backyard, and an Anthropic inspector entering that vault room as a 'visitor' to quickly check that there is nothing dangerous among the contents before leaving.

And here lies the most important fact. The questions inputted by the customer and the content of the AI's answers (Customer Content) are never, ever used as material to 'train' Anthropic's next-generation new AIs in the future [AWS Bedrock and MIMIC · MIT-LCP mimic-code · Discussion #1747](https://github.com/MIT-LCP/mimic-code/discussions/1747). Anthropic makes it contractually clear that they view this data solely for the limited purpose of monitoring whether the user is complying well with safety policies, and it is strictly used only for 'safety verification'.

---

## Where We Stand

Due to this policy change, the process of using the world's best AI for your work today has become very demanding and meticulous, much like joining a strict, VIP secret club that not just anyone can enter.

### A Complicated Rite of Passage: In-Depth Interviews and Document Screening

In the past, because the Amazon Bedrock platform had highly simplified model access to various foundation models (massive base models acting as the AI's brain), anyone could easily summon and use an AI just by agreeing to the terms and clicking a few buttons [Access request: enable Anthropic models in Bedrock for ...](https://repost.aws/questions/QUjAsyAhb3RGyKpF9oF-RVhg/access-request-enable-anthropic-models-in-bedrock-for-enterprise-internal-research).

However, Anthropic's highly advanced Mythos-class models have become the exception to this simple procedure. Now, to use this powerful model for work, users must obligatorily and meticulously fill out a document called the **'First Time Use (FTU) form'** and pass a screening, according to the strict demands of Anthropic, the third-party model provider [Request access to models - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html). This form is like getting a permit to handle dangerous chemicals. You have to undergo a kind of 'in-depth interview' where you must comprehensively and transparently disclose "exactly for what use case details our company will use this powerful AI" and prove its safety to obtain permission [Access request: enable Anthropic models in Bedrock for ...](https://repost.aws/questions/QUjAsyAhb3RGyKpF9oF-RVhg/access-request-enable-anthropic-models-in-bedrock-for-enterprise-internal-research).

Passing the document screening is not the end. You cannot just connect to it randomly from any employee's computer. Through AWS's strict digital identity verification system, 'Identity and Access Management (IAM),' you must meticulously set up permission policies in encrypted code so that the AI can only be accessed from specifically designated countries and permitted servers within the company before you can finally wake up and call the AI model (InvokeModel) [Access Anthropic models on Amazon Bedrock | AWS re:Post](https://repost.aws/knowledge-center/bedrock-access-anthropic-model). All of this complex conversational process takes place covertly and securely on AWS's massive infrastructure, exclusively through the specially encrypted `/anthropic/v1/messages` dedicated pathway (Messages API) [Claude in Amazon Bedrock - Claude API Docs](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock).

### Real-Time Monitoring and Billing Policies: "If it's dangerous, it mercilessly cuts off mid-sentence"

Even if you pass the screening with difficulty and start using the model, surveillance over the user is conducted in real-time, without resting for a single second. This is because a guard called a 'content classifier' is built into the model, reading the conversation context in real-time and judging its risk. The interesting point is the 'billing method' applied when this monitoring system is activated.

For example, imagine a user with malicious intent asks the AI, "Give me step-by-step instructions on how to sneak through a competitor's server security network and hack it." What happens if the AI, upon hearing this question, resolutely executes a refusal without a second of hesitation, saying, **"I cannot answer that question due to safety regulations"**? In the AI world, you have to pay a cost corresponding to the number of words (tokens) generated by the AI. However, if the defense system immediately activates and blocks the conversation before inference (answer generation) even begins, no token costs are billed to the user [Anthropic - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-anthropic.html).

But there is a scarier(?) scenario. A user throws a seemingly ordinary, complex programming-related question. The AI starts fluently pouring out code accordingly (streaming), but suddenly grasping the context, it belatedly realizes that it is currently writing code to create a fatal ransomware virus. At that moment, the AI immediately stops what it was saying and shuts its mouth tightly. The industry calls this **'Mid-stream refusals'** [Anthropic - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-anthropic.html).

It is just like hanging up the phone abruptly before a deeper conversation can occur as soon as the other person starts making illegal remarks during a call. In this case, the user must pay in full the cost for the words (tokens) the AI had already spit out right up until the answer was blocked. In other words, the ultra-powerful AI is not a machine that unconditionally obeys whatever the user orders; rather, it holds strong autonomous control authority, able to mercilessly cut off the conversation (stop_reason: "refusal") at any time, even mid-conversation, declaring, "This cannot proceed because it is dangerous to humans" [Anthropic - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-anthropic.html).

---

## What's Next

These measures by Anthropic—the '30-day data retention' and 'real-time safety monitoring'—which have surprised us, are not expected to end merely as a one-time incident or experiment.

Anthropic has clearly declared that it will demand this 30-day retention policy identically, and perhaps even more strictly, not only for the current Fable 5 and Mythos 5 but also for **"future models on Bedrock with similar or higher capability levels"** that will be released on the Bedrock cloud hereafter [Anthropic Claude Fable 5 on AWS: Mythos-class capabilities ...](https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/).

This declaration foreshadows a massive paradigm shift coming in the new AI era. In the past, just a year or two ago, the only hot topic in Silicon Valley was "Which company can build an AI that understands human speech better and is smarter like a human faster?" But now, the issue is completely shifting to "Who can operate the overwhelming intelligence created in such a way safely and without harm within a controllable range?"

Countless companies and users will now stand at the crossroads of an unavoidable and crucial choice. "To protect our company's perfect internal data confidentiality (privacy), will we safely keep and use older AIs on our own servers, even if they are a bit less smart?" Or "Will we willingly endure the uncomfortable and uneasy condition of 30 days of safety net surveillance in exchange for adopting the latest genius AI, which processes work overwhelmingly fast, for survival and competition in the global market?" The more dazzlingly AI evolves to the point of replacing human intellectual labor entirely, the heavier the weight of the 'safeguards' we must endure to prevent its side effects becomes.

---

## AI's Take

**MindTickleBytes AI Reporter's Take:**
In human history, explosive performance improvements have always been accompanied by new constraints. Just as when propeller planes developed into supersonic passenger jets with jet engines, the introduction of new constraints that bound passengers, like 'seatbelts' and 'oxygen masks,' became essential to prevent the fatal danger of turbulence in the sky. Even if you want to fly limitlessly and freely, great power must be accompanied by appropriate control.

Anthropic's latest measure is a highly symbolic event showing that the central axis of AI technology development is maturing from unconditional 'speed of performance competition' to practical 'safety and ethics management'. It might feel a bit stifling and monitored. However, this can be considered an essential and healthy growing pain for the survival of us all—albeit somewhat uncomfortable—to ensure that the immense progress of technology does not ultimately become an irreversible poison to humanity.

---

## References

1. [Anthropic Claude Fable 5 on AWS: Mythos-class capabilities ...](https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/)
2. [Claude in Amazon Bedrock - Claude API Docs](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)
3. [Claude Fable 5 from Anthropic now available on Amazon Bedrock](https://www.aboutamazon.com/news/aws/claude-fable-5-anthropic-available-amazon-bedrock)
4. [Claude Mythos is on AWS Bedrock. Here's what engineers need ...](https://dev.to/ajbuilds/claude-mythos-is-on-aws-bedrock-heres-what-engineers-need-to-know-2lhj)
5. [Access Anthropic models on Amazon Bedrock | AWS re:Post](https://repost.aws/knowledge-center/bedrock-access-anthropic-model)
6. [AWS Bedrock and MIMIC · MIT-LCP mimic-code · Discussion #1747](https://github.com/MIT-LCP/mimic-code/discussions/1747)
7. [Anthropic - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-anthropic.html)
8. [AWS Bedrock Claude Mythos Preview: A Defensive AI Security ...](https://murtaza-arif.github.io/blog/aws-bedrock-claude-mythos-preview-glasswing-playbook)
9. [Access request: enable Anthropic models in Bedrock for ...](https://repost.aws/questions/QUjAsyAhb3RGyKpF9oF-RVhg/access-request-enable-anthropic-models-in-bedrock-for-enterprise-internal-research)
10. [Amazon Bedrock adds Claude 3 Anthropic AI models](https://www.aboutamazon.com/news/aws/amazon-bedrock-anthropic-ai-claude-3)
11. [Data retention - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html)
12. [Data retention practices for Mythos-class models | Claude Help Center](https://support.claude.com/en/articles/15425996-data-retention-practices-for-mythos-class-models)
13. [Request access to models - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html)
14. [Simplified model access in Amazon Bedrock | AWS Security Blog](https://aws.amazon.com/blogs/security/simplified-amazon-bedrock-model-access/)