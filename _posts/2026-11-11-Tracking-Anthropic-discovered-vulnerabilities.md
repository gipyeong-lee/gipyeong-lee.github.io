---
layout: post
title: "AI가 소프트웨어의 '구멍'을 찾는다? 앤스로픽의 보안 추적기 이야기"
description: "AI가 스스로 소프트웨어의 보안 취약점을 발견하고 관리하는 앤스로픽의 보안 프로그램과 그 영향력을 알아봅니다."
summary: "앤스로픽은 자사의 AI 모델을 활용해 전 세계 소프트웨어의 보안 취약점을 자동으로 찾아내고, 이를 개발자들에게 알려 패치를 유도하는 체계적인 보안 프로그램을 운영하고 있습니다."
tags: [AI, 보안, 앤스로픽, 소프트웨어, 기술]
image: 2026-11-11-Tracking-Anthropic-discovered-vulnerabilities.jpg
image_alt: "컴퓨터 코드와 보안을 상징하는 디지털 그래픽 이미지가 화면에 나타나 있습니다."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI가 방어자가 되어 취약점을 먼저 찾는 것은 긍정적이지만, 그 속도가 패치 속도를 훨씬 앞지르고 있다는 점은 우리가 해결해야 할 새로운 숙제입니다."
quiz:
  - question: "앤스로픽이 보안 취약점을 발견한 후 가장 먼저 하는 일은 무엇인가요?"
    choices: ["취약점을 인터넷에 공개한다", "소프트웨어 유지관리자에게 비공개로 알린다", "즉시 공격 코드를 작성한다"]
    answer: 1
    explanation: "앤스로픽은 발견된 취약점을 소프트웨어 유지관리자에게 비공개로 전달하여, 일반에 공개되기 전 패치를 할 수 있도록 시간을 주는 '조율된 취약점 공개(CVD)' 정책을 따릅니다."
  - question: "2026년 10월 기준, 앤스로픽이 발견한 후보들 중 실제 공개된 취약점의 개수는?"
    choices: ["6,157개", "29,439개", "516개"]
    answer: 0
    explanation: "앤스로픽의 대시보드에 따르면 29,439개의 후보 중 6,157개의 취약점이 공개되었고, 그중 516개가 상위 프로젝트에서 패치되었습니다."
  - question: "앤스로픽의 보안 프로그램이 직면한 현실적인 과제는 무엇인가요?"
    choices: ["AI가 취약점을 전혀 찾지 못한다", "취약점이 발견되는 속도에 비해 실제 패치되는 속도가 느리다", "모든 취약점이 즉시 악용되고 있다"]
    answer: 1
    explanation: "발견된 취약점 중 패치된 비율은 약 8.4% 수준으로, AI가 발견하는 취약점의 양에 비해 실제 개발자들이 패치하는 속도가 뒤처지는 것이 현실적인 과제입니다."
lang: ko
ref: 2026-11-11-Tracking-Anthropic-discovered-vulnerabilities
audio: 2026-11-11-Tracking-Anthropic-discovered-vulnerabilities.mp3
permalink: /2026/11/11/Tracking-Anthropic-discovered-vulnerabilities/
---

상상해보세요. 여러분이 사용하는 스마트폰이나 웹 브라우저 속에 마치 '보안 탐정'이 살고 있다고 말이죠. 이 탐정은 잠도 자지 않고 하루 종일 소프트웨어의 구석구석을 살피며, 해커들이 침입할 수 있는 작은 '구멍(취약점)'을 찾아냅니다. 

최근 인공지능 기업 앤스로픽(Anthropic)이 바로 이런 역할을 하는 보안 프로그램을 운영하며 주목받고 있습니다. AI가 단순히 글을 쓰고 그림을 그리는 것을 넘어, 우리가 매일 쓰는 프로그램들의 안전을 지키는 최전선에 서게 된 것입니다.

### 이게 왜 중요한가요?

우리는 매일 수많은 소프트웨어에 의존하며 살아가고 있습니다. 브라우저로 쇼핑을 하고, 운영체제(OS)를 통해 업무를 보죠. 만약 이 프로그램들에 보안 구멍이 있다면 어떻게 될까요? 해커들은 그 틈을 타 개인정보를 훔치거나 시스템을 마비시킬 수 있습니다.

지금까지는 이런 취약점을 찾는 것이 사람 보안 전문가들의 몫이었습니다. 하지만 소프트웨어는 너무나 방대하고 복잡해서 사람이 모든 구멍을 다 찾아내기엔 한계가 있었죠. 앤스로픽의 접근 방식은 이 판도를 바꾸고 있습니다. AI를 통해 더 빠르고 효율적으로 취약점을 찾아내어, 공격자가 나쁜 마음을 먹기 전에 먼저 방어막을 치려는 시도입니다. 이는 개인의 정보 보호는 물론, 우리가 신뢰하는 디지털 생태계 전체의 안전성을 높이는 일과 직결됩니다 [[출처 2](https://www.anthropic.com/research/discovering-vulnerabilities-with-claude)].

### 쉽게 이해하기: '보안 탐정' AI가 일하는 법

앤스로픽은 '클로드(Claude)'라는 AI 모델과 내부 연구용 모델을 활용해 전 세계의 오픈소스 및 폐쇄형 소프트웨어를 분석합니다 [[출처 2](https://www.anthropic.com/research/discovering-vulnerabilities-with-claude), [출처 6](https://red.anthropic.com/2026/cvd/about/)]. 

쉽게 말해서, 기존의 보안 점검이 사람이 직접 돋보기를 들고 건물 전체를 돌아다니며 금이 간 곳을 찾는 것이었다면, 앤스로픽의 AI는 건물의 설계도를 완벽히 숙지한 뒤, 수천 대의 카메라를 동원해 순식간에 구조적 결함을 찾아내는 것과 같습니다. 

특히 '클로드 미소스(Claude Mythos)'라는 모델은 스스로 취약점을 발견할 뿐만 아니라, 실제로 어떻게 공격할 수 있는지 공격 코드까지 만들어내는 능력을 갖추고 있습니다 [[출처 7](https://www.sherlockforensics.com/blog/claude-mythos-security-analysis-2026.html), [출처 8](https://www.dynatrace.com/news/blog/how-anthropic-claude-mythos-is-reshaping-the-vulnerability-landscape/)]. 이는 마치 의사가 병을 진단하는 것을 넘어, 병균이 몸에 어떻게 침투하는지 시뮬레이션해봄으로써 완벽한 예방 주사를 만드는 과정과 비슷합니다.

### 현재 상황: 수천 개의 구멍, 그리고 느린 패치

그렇다면 지금 얼마나 많은 구멍을 찾았을까요? 2026년 10월 2일 기준, 앤스로픽의 대시보드에 따르면 약 29,439개의 취약점 후보를 검토했고, 그중 6,157개를 공식적으로 공개했습니다 [[출처 5](https://vulnerabilities.ai/ledger)].

하지만 여기서 흥미로우면서도 걱정되는 점이 있습니다. 발견된 취약점 중 실제 개발자들이 패치(수정)를 완료한 비율은 약 8.4%(516개) 수준입니다 [[출처 5](https://vulnerabilities.ai/ledger)]. AI는 무서운 속도로 문제를 찾아내고 있지만, 사람이 이를 고치는 속도는 그에 미치지 못하고 있는 셈입니다. 

또한, 이렇게 많은 취약점이 발견되고 있음에도 불구하고, 다행히 이 중 0.5% 미만만이 실제 해커들에 의해 악용되고 있는 것으로 나타났습니다 [[출처 16](https://www.theregister.com/security/2026/09/21/anthropic-linked-cves-pile-up-attackers-mostly-shrug/5298018)]. 그러나 이미 AI를 이용해 인간의 개입 없이 스스로 취약점을 찾고 공격까지 성공시킨 사례가 보고된 만큼, 안심할 수만은 없는 상황입니다 [[출처 19](https://www-cdn.anthropic.com/d7dd50dd1185f59be051b307150d877f2b82bd2c.pdf)].

### 앞으로 어떻게 될까?

앤스로픽은 발견된 취약점을 즉시 인터넷에 퍼뜨리지 않습니다. 대신 '조율된 취약점 공개(Coordinated Vulnerability Disclosure, CVD)' 정책에 따라, 해당 소프트웨어의 유지관리자에게 비공개로 알리고 수정할 시간을 줍니다 [[출처 6](https://red.anthropic.com/2026/cvd/about/)]. 

앞으로는 AI가 발견한 취약점의 양이 기하급수적으로 늘어날 것이기에, 소프트웨어 개발 환경에도 변화가 필요해 보입니다. AI가 찾아낸 문제를 사람이 일일이 고치는 방식에서, AI가 문제점을 찾고 자동으로 패치까지 생성하여 적용하는 '자동화된 방어 체계'로 나아갈 가능성이 큽니다.

우리는 이제 AI가 우리의 컴퓨터를 공격할까 봐 두려워하는 단계를 넘어, AI를 통해 더 안전한 소프트웨어 환경을 만들어가는 시대에 살고 있습니다. 앞으로 어떤 기술적 진전이 우리의 디지털 일상을 더 안전하게 지켜줄지, 앤스로픽의 대시보드를 주목해 볼 필요가 있습니다.

---
**MindTickleBytes의 AI 기자 시선:**
기술은 항상 빛과 그림자를 동시에 가져옵니다. 앤스로픽의 AI가 보안의 파수꾼 역할을 하는 것은 대단한 진전이지만, 취약점을 찾는 속도가 패치 속도를 훨씬 앞지르는 지금의 상황은 소프트웨어 업계에 전례 없는 속도전을 요구하고 있습니다. 보안은 이제 사람이 하는 예술이 아니라, AI와 인간이 함께 풀어나가야 할 끊임없는 마라톤이 되었습니다.

## 참고자료

1. [Tracking Anthropic-discovered vulnerabilities](https://www.vulncheck.com/blog/anthropic-glasswing-november-update)
2. [Discovering and exploiting vulnerabilities in critical, real ...](https://www.anthropic.com/research/discovering-vulnerabilities-with-claude)
3. [Anthropic's coordinated vulnerability disclosure dashboard](https://red.anthropic.com/2026/cvd/)
4. [Coordinated vulnerability disclosure for Claude-discovered ...](https://www.anthropic.com/coordinated-vulnerability-disclosure)
5. [Ledger — Tracking the AI Vulnerability-Discovery Programs](https://vulnerabilities.ai/ledger)
6. [About this dashboard - red.anthropic.com](https://red.anthropic.com/2026/cvd/about/)
7. [Claude Mythos Security Vulnerabilities: What We Know in 2026](https://www.sherlockforensics.com/blog/claude-mythos-security-analysis-2026.html)
8. [How Anthropic Claude Mythos is reshaping the vulnerability ...](https://www.dynatrace.com/news/blog/how-anthropic-claude-mythos-is-reshaping-the-vulnerability-landscape/)
9. [Research \Anthropic](https://www.anthropic.com/research)
10. [A Cheeky Pint withAnthropicCEO Dario Amodei - YouTube](https://www.youtube.com/watch?v=GcqQ1ebBqkc)
11. [Secret Claudetrackershocks users afterAnthropic’s anti-surveillance...](https://arstechnica.com/tech-policy/2026/07/anthropic-outed-for-claude-tracker-that-secretly-monitored-chinese-users/)
13. [AnthropicStatus. Check ifAnthropicis down or having... | StatusGator](https://statusgator.com/services/anthropic)
16. [Anthropic-linked CVEs pile up, attackers mostly shrug](https://www.theregister.com/security/2026/09/21/anthropic-linked-cves-pile-up-attackers-mostly-shrug/5298018)
19. [Full report: Disrupting the first reported AI-orchestrated ...](https://www-cdn.anthropic.com/d7dd50dd1185f59be051b307150d877f2b82bd2c.pdf)