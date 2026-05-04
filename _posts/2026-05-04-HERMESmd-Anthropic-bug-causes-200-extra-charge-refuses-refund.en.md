---
layout: post
title: "My Project File is Named 'HERMES.md'? $200 Just Evaporated"
description: "We investigate a bizarre billing bug found in Anthropic's AI tool, Claude Code, which resulted in a $200 overcharge."
summary: "An introduction to the 'HERMES.md' billing bug incident at Anthropic, where a monthly $200 subscription user was charged an additional $200 due to a single specific file name."
tags: [Anthropic, Claude, AI Bug, Billing Error, Developer News]
image: 2026-05-04-HERMESmd-Anthropic-bug-causes-200-extra-charge-refuses-refund.jpg
image_alt: "An image of a computer screen with red warning text and dollar signs scattered chaotically"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "While we have entered an era where AI handles tasks for us, the billing systems behind it remain largely a black box. This incident is a painful lesson showing that the reliability of enterprise AI tools comes from transparent operation as much as technical prowess."
quiz:
  - question: "What is the specific string that triggered this Anthropic billing bug?"
    choices: ["CLAUDE.md", "HERMES.md", "ANTHROPIC.txt"]
    answer: 1
    explanation: "The bug occurred when a specific case-sensitive string 'HERMES.md' was included in the Git history."
  - question: "Approximately how much financial damage did the user suffer due to this bug?"
    choices: ["$50", "$100", "$200"]
    answer: 2
    explanation: "Victims were charged an additional fee ranging from approximately $200 to $200.98, on top of their subscription fee."
  - question: "Why did a single file name cause a change in the billing method?"
    choices: ["Because the AI mistook the file for a paid feature", "Because a security system reacted incorrectly when the Git history was passed to the AI", "Because the user secretly used a paid model"]
    answer: 1
    explanation: "When Claude Code passed the recent work history to the AI, Anthropic's anti-abuse system saw the string and forcibly changed the billing route."
lang: en
ref: 2026-05-04-HERMESmd-Anthropic-bug-causes-200-extra-charge-refuses-refund
audio: 2026-05-04-HERMESmd-Anthropic-bug-causes-200-extra-charge-refuses-refund.en.mp3
industry: finance
---

On a peaceful Saturday morning, a developer immersed in coding while sipping coffee looked down at the vibration of their smartphone. It was a credit card payment notification. However, the amount was strange. They were already paying a hefty $200 (approx. 270,000 KRW) per month for the 'VIP Unlimited Plan,' but a message arrived saying an additional $200.98 had suddenly been charged. [Source 3](https://www.mindstudio.ai/blog/hermes-md-bug-claude-max-billing-subscription-pricing)

The culprit was none other than the AI assistant they trusted, Anthropic's 'Claude Code.' What's even more absurd was the 'crime' that led to this massive extra charge. It wasn't that they had overused the service or secretly subscribed to a paid feature. Their wallet was opened simply because a short file name, **'HERMES.md'**, was written somewhere in their project history. [Source 2](https://byteiota.com/anthropics-hermes-md-billing-bug-200-overcharge-refund-denied/) Today, MindTickleBytes explains this 'billing bug'—one of the most absurd yet chilling incidents in AI history.

## Why Does This Matter?

Imagine this. You asked an AI to "clean my computer," and while cleaning, the AI saw a 'blue sticky note' on your desk. Suddenly, it declared, "This is special waste, so I'm charging an extra $300," and swiped your card.

We are now living in the era of 'Agents'—where AI goes beyond simply answering questions and directly reads our computer files and modifies code. This incident clearly demonstrates what kind of 'financial terrorism' can occur when we grant too much authority to AI and when the systems of the companies operating those AIs are not perfect.

In particular, the fact that billing occurred due to past 'records' that are difficult for users to control, and that the company initially refused refunds, is a serious issue that shakes the very foundation of trust in AI services. [Source 6](https://kruxor.com/view/hnews/IjGK8/hermesmd-anthropic-bug-causes-200-extra-charge-refuses-refund/)

## Easy Understanding: The Inflexible Security Guard Who Ignored the 'VIP Pass'

Let's use a simpler analogy for this incident.

> Suppose you are a member of an 'Unlimited VIP Cafe' where you can drink all the beverages you want for $200 a month. One day, you walk into the cafe, but you have a small badge on your bag that says 'HERMES'.
> 
> Upon seeing this, the security guard at the entrance suddenly screams, "Hey! That badge is a forbidden symbol! From now on, your VIP benefits are suspended, and you must pay the regular price for even a single glass of water!" You protest, "I've already paid in full!" but the security guard forcibly takes your card and charges you hundreds of dollars in an instant. When you complain to the owner later, they give you the absurd response, "Our security system was designed that way, so we can't give you your money back."

In this scenario, the 'HERMES badge' is the string **'HERMES.md'**, and the 'security guard' is Anthropic's **anti-abuse system**. [Source 13](https://techplanet.today/post/the-hermesmd-bug-how-a-string-in-git-commits-triggered-incorrect-billing)

### Why Did This Happen? (The Explainer)

Metaphorically speaking, this bug began with Claude Code's 'excessive crackdown.' Looking a bit deeper technically, the following chain of tragedy was activated:

1.  **Reading the Work Diary**: When developers write code, they leave notes about their work, called 'commit messages.' To work smartly, Claude Code reads the **Git (a kind of work diary)** containing these recent records. [Source 5](https://github.com/anthropics/claude-code/issues/53262)
2.  **Including Records in the Request**: As Claude Code sends the collected Git history to Anthropic's headquarters servers, it stuffs these records entirely into the **system prompt (background instructions delivered to the AI)**. [Source 10](https://vc.ru/ai/2897200-bag-v-claude-code-privel-k-spisaniyu-sredstv-iz-za-hermes-md)
3.  **The Malfunctioning Checkpoint**: As soon as Anthropic's security system spotted the letters 'HERMES.md' in this request, it sounded the alarm. It likely recognized this word as dangerous or requiring special measures. [Source 13](https://techplanet.today/post/the-hermesmd-bug-how-a-string-in-git-commits-triggered-incorrect-billing)
4.  **Forced Billing Path Change**: The security system ignored the fact that the user was already on a $200/month unlimited plan and forcibly routed all requests to the 'Extra Usage' billing channel. It was as if they forced someone on an unlimited plan to "pay separately for every glass of water because you are a high-risk individual." [Source 5](https://github.com/anthropics/claude-code/issues/53262), [Source 8](https://codegurus.eu/hermes-md-anthropic-bug-causes-200-extra-charge-refuses-refund/)

Surprisingly, this 'security guard' was extremely picky. It didn't take issue with lowercase 'hermes.md' or 'HERMES.txt' with a different extension. Only that exact name, with matching capitalization, served as the 'bomb switch.' [Source 10](https://vc.ru/ai/2897200-bag-v-claude-code-privel-k-spisaniyu-sredstv-iz-za-hermes-md)

## Current Situation: The Thunderbolt of "No Refunds"

Due to this absurd bug, many developers were suddenly charged an additional $200 (approx. 270,000 KRW)—the price of about 10 chicken dinners—overnight. [Source 1](https://thecodersblog.com/hermes-md-anthropic-s-billing-bug-refused-refunds-and-the-cost-of-trust-2026), [Source 14](https://news.linxi.com.au/news/billing-anomaly-in-claude-code-linked-to-specific-string-in-git-history) One user experienced the horror of $200 evaporating in just a single Saturday. [Source 16](https://www.linkedin.com/posts/ravicaw_anthropic-is-reading-your-git-commits-to-activity-7454041190104006656-m04B)

Victims immediately knocked on the door of Anthropic's customer support, but the response they received was even more shocking. Anthropic initially repeated mechanical replies saying they were "unable to issue refund." [Source 7](https://inshorts.com/en/news/anthropic-s-claude-code-charges-users-extra-due-to-hidden-bug--initially-refuses-refund-1777276172440), [Source 15](https://www.hotmolts.com/post/anthropic-refuses-refund-for-its-own-billing-bug-u-2aa5714c-ae65-4b25-b5be-eafbc54a6a9e)

One victimized developer expressed their frustration in an online community, saying, "Does it make sense to lose $200 of my own money because of a company-side bug that wasn't even my mistake?" [Source 12](https://news.ycombinator.com/item?id=47952722) Currently, this issue is drawing public outrage from developers worldwide, receiving over 110,000 'stars' (indicators of interest) on Anthropic's GitHub repository. [Source 8](https://codegurus.eu/hermes-md-anthropic-bug-causes-200-extra-charge-refuses-refund/)

## What Lies Ahead?

The 'HERMES.md' incident goes beyond a simple software error and poses three important questions for us living in the AI era.

First is the **responsibility of AI companies**. If financial damage occurs due to an error in their own algorithms, they should provide active remedies instead of saying it's "not possible according to regulations." The poor initial response has left an indelible stain on the brand. [Source 7](https://inshorts.com/en/news/anthropic-s-claude-code-charges-users-extra-due-to-hidden-bug--initially-refuses-refund-1777276172440)

Second is **data transparency**. The fact that the AI was secretly(?) reading past work records that I didn't directly show it is unpleasant for many users. [Source 16](https://www.linkedin.com/posts/ravicaw_anthropic-is-reading-your-git-commits-to-activity-7454041190104006656-m04B) In the future, we will have to more carefully examine "how much of my data is being passed to the AI." [Source 9](https://sesamedisk.com/anthropic-claude-code-billing-bug-security/)

Third is the **need for sufficient safeguards**. Experts point out that this bug could have been prevented with proper testing before deployment. [Source 13](https://techplanet.today/post/the-hermesmd-bug-how-a-string-in-git-commits-triggered-incorrect-billing) As AI gains increasingly powerful authority, the systems to keep it in check must become equally sophisticated.

Are there any files with names that AI might dislike hidden in your projects? In the future, we might face a laughable era where we have to check our wallet status before putting an AI to work.

---

### AI Perspective
**MindTickleBytes AI Reporter's View**
This incident shows that AI has moved beyond being a simple 'chat partner' and has entered a stage where it directly affects our 'assets.' Companies should not just rush to create high-performance AI models; they must first establish sophisticated billing safeguards that can protect users' credit cards. Because as important as technical advancement is the courtesy toward the people using that technology.

---

## References
1. [Anthropic's $200 Bug: When AI API Errors Cost You, and ...](https://thecodersblog.com/hermes-md-anthropic-s-billing-bug-refused-refunds-and-the-cost-of-trust-2026)
2. [Anthropic’s HERMES.md Billing Bug: $200 Overcharge, Refund ...](https://byteiota.com/anthropics-hermes-md-billing-bug-200-overcharge-refund-denied/)
3. [The Hermes.md Bug That Charged Claude Max Users $200 Extra ...](https://www.mindstudio.ai/blog/hermes-md-bug-claude-max-billing-subscription-pricing)
4. [Claude Code HERMES.md Billing Bug: $200 Credit Drain Analysis](https://aitoolly.com/ai-news/article/2026-04-30-claude-code-bug-hermesmd-in-commit-messages-triggers-unexpected-extra-usage-billing)
5. [HERMES.md in git commit messages causes requests to route to ...](https://github.com/anthropics/claude-code/issues/53262)
6. [HERMES.md: Anthropic bug causes $200 extra charge, refuses ...](https://kruxor.com/view/hnews/IjGK8/hermesmd-anthropic-bug-causes-200-extra-charge-refuses-refund/)
7. [Anthropic's Claude Code charges users extra due to hidden bug ...](https://inshorts.com/en/news/anthropic-s-claude-code-charges-users-extra-due-to-hidden-bug--initially-refuses-refund-1777276172440)
8. [HERMES.md:Anthropicbugcauses$200extracharge,refuses...](https://codegurus.eu/hermes-md-anthropic-bug-causes-200-extra-charge-refuses-refund/)
9. [Billing Security Risks inAnthropic’s Claude Code - Sesame Disk](https://sesamedisk.com/anthropic-claude-code-billing-bug-security/)
10. [Anthropicсписала $200сверх тарифа Max 20x из-заHERMES.md...](https://vc.ru/ai/2897200-bag-v-claude-code-privel-k-spisaniyu-sredstv-iz-za-hermes-md)
12. [HERMES.mdin commit messagescausesrequests to route toextra...](https://news.ycombinator.com/item?id=47952722)
13. [TheHERMES.mdBug: How a String in Git Commits... | TechPlanet](https://techplanet.today/post/the-hermesmd-bug-how-a-string-in-git-commits-triggered-incorrect-billing)
14. [Anthropic Claude Code billing bug linked to HERMES.md git ...](https://news.linxi.com.au/news/billing-anomaly-in-claude-code-linked-to-specific-string-in-git-history)
15. [Anthropic refuses refund for its own billing bug: 'unable to ...](https://www.hotmolts.com/post/anthropic-refuses-refund-for-its-own-billing-bug-u-2aa5714c-ae65-4b25-b5be-eafbc54a6a9e)
16. [Anthropic bills based on git commits with Hermes - LinkedIn](https://www.linkedin.com/posts/ravicaw_anthropic-is-reading-your-git-commits-to-activity-7454041190104006656-m04B)