---
layout: post
title: "AI의 '생각하는 과정'은 진짜일까? '확장된 사고(Extended Thinking)'의 비밀"
description: "클로드(Claude)의 '확장된 사고' 기능이 보여주는 생각 과정은 사실 전체 과정의 요약본일 수 있다는 논란에 대해 쉽게 설명해 드립니다."
summary: "클로드의 '확장된 사고' 기능은 AI가 복잡한 문제를 풀기 전에 더 깊게 고민하도록 돕지만, 우리가 결과물로 보는 생각 과정은 전체 논리 체계가 아닌 요약된 버전일 수 있다는 점을 이해해야 합니다."
tags: [AI, 클로드, 확장된 사고, 기술상식]
image: 2026-06-23-Claude-Codes-extended-thinking-is-a-summary--not-authentic-thinking.jpg
image_alt: "AI가 생각하는 과정을 디지털 퍼즐 조각으로 표현한 그래픽"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI의 내부 논리를 완전히 투명하게 보는 것은 기술적으로 매우 어렵습니다. 우리는 AI가 내놓은 결과물의 '논리적 흐름'을 파악하는 데 집중해야 합니다."
quiz:
  - question: "클로드의 '확장된 사고(Extended Thinking)'는 무엇인가요?"
    choices: ["AI의 지능을 무한대로 높이는 기능", "모델이 복잡한 문제를 풀기 전에 더 많은 시간과 노력을 들여 고민하게 하는 기능", "인터넷 연결을 끊고 생각하는 기능"]
    answer: 1
    explanation: "확장된 사고는 별도의 모델을 쓰는 것이 아니라, 같은 모델이 정답을 내기 전에 더 많은 시간과 노력을 투입해 논리적으로 추론하게 만드는 기능입니다."
  - question: "클로드 4 모델에서 우리가 보는 '생각 과정'은 어떤 형태인가요?"
    choices: ["AI가 생각한 모든 단계를 하나도 빠짐없이 보여주는 원본", "AI의 추론 과정을 압축하여 핵심만 담은 요약본", "결과물에 대한 통계 수치"]
    answer: 1
    explanation: "클로드 4 모델의 API는 전체 추론 과정의 원본이 아닌, 핵심 논리를 간추린 요약본을 제공합니다."
  - question: "확장된 사고를 사용하면 항상 성능이 향상되나요?"
    choices: ["그렇다, 항상 성능이 좋아진다", "아니요, 특정 작업에서는 오히려 성능이 최대 36%까지 낮아질 수 있다", "성능과는 전혀 무관하다"]
    answer: 1
    explanation: "확장된 사고가 모든 작업에 항상 좋은 것은 아니며, 특정 유형의 작업에서는 오히려 성능이 최대 36%까지 저하될 수 있다는 연구 결과가 있습니다."
lang: ko
ref: 2026-06-23-Claude-Codes-extended-thinking-is-a-summary--not-authentic-thinking
audio: 2026-06-23-Claude-Codes-extended-thinking-is-a-summary--not-authentic-thinking.mp3
permalink: /2026/06/23/Claude-Codes-extended-thinking-is-a-summary--not-authentic-thinking/
---

상상해보세요. 어려운 수학 문제를 풀거나 복잡한 기획안을 작성할 때, 평소보다 10배 더 오랜 시간 동안 골머리를 앓으며 고민하는 'AI 비서'를 둔다면 어떨까요? 최근 인공지능 업계에서는 AI가 바로 답변을 내놓지 않고, 마치 사람이 고민하듯 '잠시 생각하는 시간'을 갖게 하는 기술이 큰 화제입니다. 이를 클로드(Claude)의 개발사인 앤스로픽(Anthropic)은 **'확장된 사고(Extended Thinking)'**라고 부릅니다. 

하지만 최근 이 기술이 보여주는 '생각 과정'이 정말 AI가 고민한 모든 흔적인지에 대해 의문이 제기되고 있습니다. 우리가 화면에서 보는 AI의 생각 과정, 과연 100% 믿어도 될까요?

## 이게 왜 중요한가요?

AI 기술이 발전할수록 우리는 AI가 왜 그런 결론을 내렸는지 그 '이유'를 알고 싶어 합니다. 특히 복잡한 개발 코드 작성이나 전략 기획 같은 중요한 작업에서는 AI의 사고 과정(Audit Trail, 감사가 가능한 논리 기록)이 투명해야 오류를 줄일 수 있기 때문입니다.

만약 우리가 보는 생각 과정이 전체 논리의 일부분만 담은 '요약본'이라면, 사용자는 AI가 결정을 내린 전체 맥락을 온전히 파악하지 못할 위험이 있습니다. 이는 사용자가 AI의 논리적 허점을 발견하지 못하고 잘못된 정보를 사실로 받아들이게 할 수도 있다는 점에서 매우 중요한 문제입니다.

## 쉽게 이해하기: AI의 '생각 노트'

'확장된 사고'를 이해하기 위해 비유를 하나 들어볼게요. 여러분이 시험 문제를 풀 때, 시험지 옆에 있는 '연습장'에 낙서를 하며 문제를 푸는 것을 상상해 보세요. 

- **기존 방식:** AI가 질문을 받자마자 연습장도 없이 바로 답을 적어내는 방식입니다.
- **확장된 사고:** AI에게 "답을 적기 전에 연습장에 충분히 생각하고, 그 과정을 보여줘"라고 지시하는 것과 같습니다. [참고자료 3](https://gist.github.com/intellectronica/58571dda3581eec3e17a77741e8c858a), [참고자료 10](https://masteringclaude.com/learn/23-extended-thinking.html)

여기서 중요한 점은 이 기능이 '다른 똑똑한 AI'로 바뀌는 것이 아니라는 사실입니다. 그냥 기존의 AI가 스스로 고민할 시간을 더 갖는 것뿐이죠. [참고자료 5](https://www.anthropic.com/news/visible-extended-thinking)

하지만 문제가 있습니다. 클로드 4와 같은 최신 모델은 이 '연습장에 적은 내용'을 우리에게 그대로 보여주지 않습니다. 대신, 고민했던 내용 중 핵심만 쏙 뽑아 정리한 **'요약본'**을 우리에게 보여줍니다. [참고자료 6](https://cobusgreyling.medium.com/building-with-claude-extended-thinking-d1a8b3130834) 개발자인 패트릭 맥캐나(Patrick McCanna)는 이것이 AI 논리의 완벽한 감사 기록이 아니라, 데이터 손실이 발생하는 '요약본'일 뿐이라고 지적했습니다. [참고자료 2](https://news.linxi.com.au/news/claude-code-extended-thinking-output-is-summary-not-authentic-reasoning-developer-claims), [참고자료 11](https://news.ycombinator.com/item?id=48630535)

## 현재 상황: 만능은 아니다

'확장된 사고'가 항상 좋은 것만은 아닙니다. AI가 더 많이 생각한다고 해서 모든 문제에서 더 나은 답을 내놓는 것은 아니기 때문입니다. 연구 결과에 따르면, 이 기능을 사용했을 때 특정 유형의 작업에서는 오히려 성능이 최대 36%까지 떨어질 수 있다는 보고도 있습니다. [참고자료 3](https://gist.github.com/intellectronica/58571dda3581eec3e17a77741e8c858a) 

현재 일부 모델에서는 이 기능이 항상 켜져 있으며 끄는 것이 불가능합니다. [참고자료 1](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) 즉, 우리는 AI가 쓴 '연습장 요약본'을 강제로 보게 되는 셈입니다.

## 앞으로 어떻게 될까?

앞으로 AI가 내놓는 '생각 노트'의 신뢰성을 어떻게 확보할지가 기술적 과제가 될 것입니다. 현재로서는 AI가 고민한 과정을 100% 그대로 보는 것은 기술적으로 매우 어려운 일입니다. "아무도 LLM(거대 언어 모델, 방대한 데이터를 학습해 인간처럼 언어를 이해하고 생성하는 AI)이 정확히 어떻게 생각하는지 완벽히 이해하지 못한다"는 의견이 지배적이기 때문입니다. [참고자료 11](https://news.ycombinator.com/item?id=48630535)

따라서 사용자는 AI가 보여주는 사고 과정이 '전부'라고 믿기보다는, AI가 결론을 도출하기 위해 사용한 '핵심 논리적 흐름'을 참고하는 도구로 이해하는 것이 현명합니다.

## MindTickleBytes의 AI 기자 시선

기술이 발전할수록 AI는 점점 더 인간처럼 생각하는 척(Reasoning)을 잘하게 됩니다. 하지만 우리가 잊지 말아야 할 것은 AI의 '생각 과정'은 사람이 쓴 논문이나 일기장과는 다르다는 점입니다. 쉽게 말해서, AI의 결과물은 완벽한 진실이라기보다 정교하게 계산된 예측값에 가깝습니다. 그러므로 우리는 AI가 내놓는 결과물의 근거를 의심하고 검증하는 습관을 계속 유지해야 합니다. 

## 참고자료

1. [Building with extended thinking - Claude API Docs](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)
2. [Claude Code Extended Thinking Summary Not Authentic Reasoning ...](https://news.linxi.com.au/news/claude-code-extended-thinking-output-is-summary-not-authentic-reasoning-developer-claims)
3. [Claude Extended Thinking: The Ultimate Guide · GitHub](https://gist.github.com/intellectronica/58571dda3581eec3e17a77741e8c858a)
4. [Extended Thinking in Claude Code: Unlock Deeper Reasoning](https://claude-world.com/articles/extended-thinking-guide/)
5. [Claude’s extended thinking - Anthropic](https://www.anthropic.com/news/visible-extended-thinking)
6. [Building with Claude Extended Thinking | by Cobus Greyling ...](https://cobusgreyling.medium.com/building-with-claude-extended-thinking-d1a8b3130834)
7. [Claude Extended Thinking: When to Use It and How to Build ...](https://aiforanything.io/blog/claude-extended-thinking-guide-2026)
8. [Getting the Most from Claude Code's Extended Thinking Mode ...](https://callsphere.ai/blog/claude-code-extended-thinking-mode)
9. [Extended thinking | Claude Cookbook](https://platform.claude.com/cookbook/extended-thinking-extended-thinking)
10. [Lesson 23: Extended Thinking - Mastering Claude](https://masteringclaude.com/learn/23-extended-thinking.html)
11. [ClaudeCode's"extendedthinking"isasummary... | HackerNews](https://news.ycombinator.com/item?id=48630535)
12. [Claude3.7 Sonnet debuts with “extendedthinking” to... - Ars Technica](https://arstechnica.com/ai/2025/02/claude-3-7-sonnet-debuts-with-extended-thinking-to-tackle-complex-problems/)
13. [What’sNew inClaudev4? AI Just Got Smarter | by Rendiero | Medium](https://medium.com/h7w/whats-new-in-claude-v4-ai-just-got-smarter-b62242ad95ba)
14. [HackerNews– Telegram](https://t.me/hackernewslive/227152)
15. [ThinkingMachines: When Should You Actually Use Reasoning... | Glasp](https://glasp.co/articles/when-to-use-reasoning-models)
17. [Claude3.7 Sonnet andClaudeCode\ Anthropic](https://www.anthropic.com/news/claude-3-7-sonnet)