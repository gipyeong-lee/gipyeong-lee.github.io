---
layout: post
title: "AI가 쓴 코드는 '쓰레기'일까? 프로그래밍 언어 Zig와 Anthropic의 정면충돌"
description: "AI로 작성된 코드를 전면 금지한 프로그래밍 언어 Zig와 그로 인해 4배의 성능 향상을 포기해야 했던 Anthropic의 Bun 사례를 통해 본 AI 시대의 소프트웨어 개발 논쟁."
summary: "프로그래밍 언어 Zig가 AI로 작성된 모든 기여를 전면 금지하면서, Anthropic이 인수한 Bun이 개발한 4배 빠른 성능의 코드가 공식 프로젝트에 반영되지 못하는 사건이 발생했습니다."
tags: [AI, Zig, Bun, 프로그래밍, 오픈소스]
image: 2026-07-13-Zig-Creator-Calls-Spade-a-Spade-Anthropic-Blows-Smoke.jpg
image_alt: "컴퓨터 화면 위로 프로그래밍 코드와 AI 로봇 아이콘이 충돌하는 형상의 그래픽"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "오픈소스 생태계가 AI 도구의 활용을 두고 양극단으로 나뉘고 있습니다. 기술적 가치와 개발자 문화라는 두 가치가 충돌하는 지점에서 우리는 어떤 기준을 세워야 할까요."
quiz:
  - question: "프로그래밍 언어 Zig가 AI 관련 기여를 금지한 이유는 무엇인가요?"
    choices: ["AI가 낸 코드가 너무 비싸서", "AI 코드가 품질이 낮고 리뷰 시간을 낭비해서", "저작권 문제 때문에"]
    answer: 1
    explanation: "Zig의 창립자 앤드류 켈리는 AI로 생성된 코드가 품질이 낮아 검토 시간을 낭비할 뿐 가치가 없다고 판단했습니다."
  - question: "Anthropic의 Bun 프로젝트가 개발한 성능 개선을 Zig 공식 프로젝트에 반영하지 못한 이유는 무엇인가요?"
    choices: ["성능 개선이 충분하지 않아서", "Zig의 AI 기여 전면 금지 정책 때문에", "기술적인 호환성 문제 때문에"]
    answer: 1
    explanation: "Bun은 4배의 성능 향상을 이루었으나, Zig의 엄격한 AI 기여 금지 정책으로 인해 해당 코드를 공식 프로젝트에 포함(upstream)할 수 없었습니다."
  - question: "Zig의 AI 기여 금지 범위는 어디까지인가요?"
    choices: ["코드만 금지", "코드, 댓글, 이슈, 버그 리포트 답변 등 모든 기여 금지", "기존 기여자만 금지"]
    answer: 1
    explanation: "Zig는 코드뿐만 아니라 댓글, 이슈, 풀 리퀘스트, 버그 트래커 답변 등 AI가 관여된 모든 형태의 기여를 금지하고 있습니다."
lang: ko
ref: 2026-07-13-Zig-Creator-Calls-Spade-a-Spade-Anthropic-Blows-Smoke
audio: 2026-07-13-Zig-Creator-Calls-Spade-a-Spade-Anthropic-Blows-Smoke.mp3
permalink: /2026/07/13/Zig-Creator-Calls-Spade-a-Spade-Anthropic-Blows-Smoke/
---

상상해보세요. 여러분이 수개월 동안 밤을 새워 만든 아주 효율적인 기계 장치가 있습니다. 이 장치는 기존 부품보다 무려 4배나 더 빠르게 작동합니다. 그런데 이 장치를 공식 생산 라인에 올리려는 순간, 공장 운영자가 차갑게 말합니다. "이 장치를 만드는 과정에 인공지능(AI) 도구를 조금이라도 썼다고요? 그럼 절대 안 됩니다. 당장 버리세요."

지금 오픈소스 프로그래밍 세계에서 바로 이런 일이 벌어지고 있습니다. 프로그래밍 언어 'Zig'와 Anthropic이 인수한 자바스크립트 런타임 'Bun' 사이에서 발생한 이 사건은, AI가 소프트웨어 개발을 돕는 이 시대에 우리가 마주한 아주 근본적인 고민을 던져줍니다.

## 이게 왜 중요한가요?

우리 일상의 앱들이 점점 똑똑해지는 배경에는 수많은 개발자의 노력이 있습니다. 오늘날 개발자들은 AI 도구를 활용해 더 빠르고 효율적으로 소프트웨어를 만듭니다. 하지만 '누가, 어떻게 만들었는가'가 중요하다는 입장과 '기술적 결과물만 좋으면 그만'이라는 입장이 정면으로 충돌하고 있습니다. 만약 Zig의 사례처럼 AI를 활용한 결과물조차 배척된다면, 앞으로 개발자들은 AI 도구를 쓰는 것을 주저하게 될 수도 있습니다. 반대로, 아무런 검증 없이 AI 코드가 넘쳐난다면 소프트웨어의 안정성은 누가 책임질까요?

## 쉽게 말해서 (The Explainer)

Zig는 널리 쓰이는 고성능 프로그래밍 언어입니다. 그리고 Bun은 Zig로 만들어진 자바스크립트 실행 환경으로, 최근 AI 기업인 Anthropic에 인수되었습니다[Source 4, Source 6, Source 18].

비유하자면, Zig는 아주 까다로운 장인 정신을 중요시하는 '고급 목공소'입니다. 이 목공소의 대표인 앤드류 켈리(Andrew Kelley)는 AI가 작성한 코드를 보고 "변함없이 쓰레기(invariably garbage)"라고 표현했습니다[Source 1, Source 5]. 그는 AI가 짠 코드가 실질적인 가치는 없으면서, 핵심 개발 팀의 귀중한 리뷰 시간만 낭비하게 만든다고 판단했습니다. 그래서 그는 코드뿐만 아니라 댓글, 이슈, 심지어 버그 리포트에 대한 답변까지 AI가 조금이라도 관여했다면 그 기여를 전면 금지하는 엄격한 정책을 세웠습니다[Source 1, Source 2].

반면, Bun 팀은 AI를 적극적으로 활용해 컴파일(사람이 쓴 코드를 컴퓨터가 이해하는 언어로 바꾸는 과정) 속도를 약 4배나 높이는 놀라운 성과를 냈습니다[Source 2, Source 3, Source 4]. 하지만 Zig의 벽은 높았습니다. Bun 팀은 이 훌륭한 성과를 공식 프로젝트에 포함시키려 했으나, AI를 사용했다는 사실 때문에 거부당할 것이 분명했기에 결국 공식 프로젝트 반영을 포기하고, 별도의 버전(포크, fork)으로 프로젝트를 유지하기로 결정했습니다[Source 2, Source 4].

## 현재 상황

현재 Zig의 입장은 단호합니다. AI 활용 여부가 의심되면 기술적 가치를 따져보기도 전에 거부할 수 있을 만큼 원칙을 고수합니다[Source 2]. 실제로 많은 개발자가 이 정책에 대해 뜨거운 반응을 보이고 있습니다. 일각에서는 Bun 프로젝트의 코드베이스와 문서들이 AI가 작성한 글들(AI slop)로 채워지는 것에 반감을 표하며, Bun을 떠나려는 움직임까지 보이고 있습니다[Source 17].

반면, Anthropic과 Bun 팀은 기술적 이점을 위해 AI 도구를 계속 사용할 것으로 보입니다. Bun은 현재 Anthropic의 'Claude Code'나 'Claude Agent SDK'를 위한 인프라로 사용되고 있기 때문입니다[Source 16, Source 18]. 기술적 성과를 우선시하는 쪽과 원칙을 우선시하는 쪽이 각자의 길을 가며 공존하고 있는 셈입니다.

## 앞으로 어떻게 될까?

이 논쟁은 단순히 한 프로젝트만의 문제가 아닙니다. 'AI 도구를 사용한 기여를 어디까지 허용할 것인가'는 앞으로 모든 오픈소스 프로젝트가 답해야 할 숙제가 되었습니다. Zig는 아주 극단적이고 확실한 기준을 제시했습니다. 앞으로 더 많은 프로젝트가 각자의 'AI 기여 지침'을 마련할 것이고, Zig처럼 전면 금지하거나 혹은 적절한 검증 과정을 거쳐 수용하는 쪽으로 나뉠 것입니다. 개발자들은 이제 자신이 기여하는 프로젝트가 어떤 정책을 가지고 있는지 꼼꼼히 살펴봐야 하는 시대를 살게 되었습니다.

## MindTickleBytes의 시선

기술은 단순히 도구일 뿐이라는 주장과, 그 도구가 만드는 결과물의 본질이 변했다는 주장이 팽팽하게 맞서고 있습니다. 중요한 것은 도구의 사용 여부 그 자체가 아니라, 그 도구가 최종 결과물의 품질과 생태계의 지속 가능성에 어떤 영향을 미치느냐일 것입니다. Zig의 엄격함이 오픈소스의 순수성을 지키는 방패가 될지, 혹은 변화하는 개발 흐름 속에서 스스로 고립을 자초하는 길이 될지는 조금 더 지켜봐야 할 일입니다.

## 참고자료

1. [Zig bans LLM contributions, forcing Bun to fork | AI Weekly](https://aiweekly.co/alerts/zig-bans-llm-contributions-forcing-bun-to-fork)
2. [Zig Draws Hard Line On AI, Bun Chooses Fork Over Upstreaming - Open Source For You](https://www.opensourceforu.com/2026/05/zig-draws-hard-line-on-ai-bun-chooses-fork-over-upstreaming/)
3. [ZIG BANNED ANTHROPIC FROM ITS OWN LANGUAGE #Shorts - YouTube](https://www.youtube.com/shorts/sYMuqS2oyUw)
4. [Zig Reinforces LLM Contribution Ban As Anthropic-Owned Bun Forks 4x Gain](https://winbuzzer.com/2026/05/01/zig-llm-contribution-ban-bun-4x-speedup-downstream-xcxwbn/)
5. [Zig president says AI coding contributions are 'invariably garbage,' so he banned them](https://www.businessinsider.com/zig-programming-language-ai-rules-2026-5)
6. [The Zig project's rationale for their firm anti-AI contribution policy](https://simonwillison.net/2026/Apr/30/zig-anti-ai/)
16. [Anthrophic's Bun team trials port from Zig to Rust](https://www.devclass.com/software/2026/05/11/anthrophics-bun-team-trials-port-from-zig-to-rust/5237835)
17. [This feels more like a reaction to Zig's anti-LLM policy than anything. Anthropi... | Hacker News](https://news.ycombinator.com/item?id=48017387)
18. [Bun’s Zig to Rust Rewrite: Anthropic’s AI Code Experiment | byteiota](https://byteiota.com/buns-zig-to-rust-rewrite-anthropics-ai-code-experiment/)