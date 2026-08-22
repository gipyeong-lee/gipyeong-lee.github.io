---
layout: post
title: "내 AI가 갑자기 멍청해졌다고? 클로드 코드(Claude Code)의 숨겨진 실험 이야기"
description: "AI 모델의 성능이 갑자기 떨어진 것처럼 느껴진 적 있나요? 앤스로픽의 클로드 코드에서 발생한 '노력 수준' 조정과 사용자들의 불편 경험을 통해 AI 투명성 문제를 살펴봅니다."
summary: "앤스로픽은 비용 절감과 속도 향상을 위해 클로드 코드의 기본 추론 강도를 몰래 낮췄다가 사용자들의 품질 저하 불만이 빗발치자 이를 복구했습니다."
tags: [AI, 앤스로픽, 클로드코드, 인공지능, 기술윤리]
image: 2026-08-23-Anthropic-appears-to-be-AB-testing-reduced-effort-levels-in-Claude-Code.jpg
image_alt: "클로드 코드 인터페이스 화면과 추론 과정을 나타내는 그래픽 요소"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "기업이 기술을 최적화할 때는 사용자와의 신뢰를 위해 변화의 이유를 투명하게 공개해야 합니다. 실험적 기능은 항상 사용자의 선택권 보장이 우선되어야 할 것입니다."
quiz:
  - question: "앤스로픽이 클로드 코드의 기본 추론 수준을 낮춘 주된 이유는 무엇인가요?"
    choices: ["모델의 보안 강화", "비용 절감 및 응답 속도 향상", "더 많은 데이터를 학습하기 위해"]
    answer: 1
    explanation: "앤스로픽은 사용자들이 토큰 소모량이 너무 많다는 피드백을 반영하여 응답 속도를 개선하고 토큰 소모를 줄이려 했습니다."
  - question: "클로드 코드에서 '노력 수준(effort level)'이 높을수록 어떤 일이 일어나나요?"
    choices: ["더 빠르게 응답한다", "사고의 깊이가 깊어지고 복잡한 문제를 더 잘 해결한다", "무조건 더 많은 비용이 발생한다"]
    answer: 1
    explanation: "노력 수준은 사고의 깊이와 연관되어 있어 더 복잡한 문제를 해결하는 능력을 향상시킵니다."
  - question: "앤스로픽은 최근 발생한 품질 저하 문제를 어떻게 해결했나요?"
    choices: ["사용자들에게 더 높은 요금을 부과했다", "4월 7일에 다시 이전 수준으로 복구했다", "AI 모델을 완전히 교체했다"]
    answer: 1
    explanation: "앤스로픽은 해당 조치가 잘못된 타협점이었음을 인정하고 2026년 4월 7일에 원래의 높은 추론 수준으로 설정을 복구했습니다."
lang: ko
ref: 2026-08-23-Anthropic-appears-to-be-AB-testing-reduced-effort-levels-in-Claude-Code
audio: 2026-08-23-Anthropic-appears-to-be-AB-testing-reduced-effort-levels-in-Claude-Code.mp3
permalink: /2026/08/23/Anthropic-appears-to-be-AB-testing-reduced-effort-levels-in-Claude-Code/
---

상상해보세요. 매일 업무를 도와주던 똑똑한 AI 비서가 있습니다. 어제까지는 복잡한 코딩 문제도 척척 해결해주던 비서가, 오늘 아침 갑자기 너무 단순한 답변만 내놓거나 중요한 맥락을 놓치기 시작한다면 얼마나 당황스러울까요? 최근 인공지능 기업 앤스로픽(Anthropic)의 개발자용 코딩 도구인 '클로드 코드(Claude Code)' 사용자들 사이에서 바로 이런 일이 벌어졌습니다.

### 이게 왜 중요한가요?

이번 사건은 AI를 전문 도구로 사용하는 사람들에게 큰 충격을 주었습니다. 단순히 모델이 조금 느려진 문제가 아니었습니다. 사용자가 모르는 사이에 AI의 '두뇌 회전' 방식이 강제로 변경되었고, 그 결과 업무 생산성에 즉각적인 타격이 발생했기 때문입니다. 이는 우리가 매일 사용하는 AI 서비스들이 기업의 내부 정책에 따라 언제든 예고 없이 성능이 변할 수 있음을 보여주는 중요한 사례입니다. 

### 쉽게 이해하기: AI의 '노력 수준'이란?

클로드 코드에는 **'노력 수준(Effort Level, AI가 문제를 해결하기 위해 얼마나 깊게 생각할지 결정하는 설정)'**이라는 기능이 있습니다. 

쉽게 말해, 이 노력 수준은 학생이 시험 문제를 풀 때 들이는 노력과 비슷합니다. '낮은 노력' 수준은 문제를 대충 훑어보고 빨리 답을 적는 것이고, '높은 노력' 수준은 모든 문장을 꼼꼼히 읽고 검토하며 깊게 고민하는 것이죠. [출처: Claude Code effort level and model selection](https://claude.com/blog/claude-model-and-effort-level-in-claude-code) 

비유하자면, 베테랑 요리사가 정성을 다해 요리하다가 갑자기 재료비와 시간을 아끼기 위해 간편식 수준으로 요리 방식을 바꾼 것과 같습니다. 소비자 입장에서는 당연히 맛의 차이를 느낄 수밖에 없겠죠.

앤스로픽은 2026년 2월과 3월 사이, 아무런 공지 없이 클로드 코드의 기본 노력 수준을 '높음'에서 '중간'으로 낮추었습니다. [출처: Claude Code's Thinking Depth Dropped 73%](https://claudeapi.com/en/blog/news/claude-performance-decline-effort-level-api-restored/) 앤스로픽 관계자의 설명에 따르면, 이는 사용자들이 토큰(AI가 사용하는 언어 단위) 소모가 너무 많다는 피드백을 반영하여 응답 속도를 개선하고 비용을 줄이려는 의도였습니다. [출처: Anthropic faces user backlash over reported performance issues](https://fortune.com/2026/04/14/anthropic-claude-performance-decline-user-complaints-backlash-lack-of-transparency-accusations-compute-crunch/) 

하지만 결과는 처참했습니다. 이 조정으로 인해 AI의 사고 깊이가 무려 73%나 줄어들면서, 복잡한 프로그래밍 작업을 수행하던 사용자들은 성능이 급격히 떨어졌음을 체감하게 되었습니다. [출처: Claude Code's Thinking Depth Dropped 73%](https://claudeapi.com/en/blog/news/claude-performance-decline-effort-level-api-restored/) 

### 현재 상황: 연이은 업데이트와 혼란

성능이 떨어진 원인은 크게 세 가지 업데이트가 겹쳤기 때문으로 밝혀졌습니다. [출처: Anthropic Claude Code Quality Drop](https://devtoolpicks.com/blog/anthropic-claude-code-quality-fix-postmortem-2026) 특히 3월에는 일부 사용자를 대상으로 한 A/B 테스트(두 가지 이상의 안을 무작위로 보여주어 성과를 비교하는 실험)가 진행되었는데, 이 과정에서 코드 계획을 40줄로 제한하거나 필요한 문맥 정보를 삭제해버리는 등의 문제가 발생해 사용자들의 반발을 샀습니다. [출처: Anthropic A/B Tested Claude Code Plan Mode](https://agent-wars.com/news/2026-03-14-anthropic-ab-testing-claude-code-plan-mode-without-disclosure) 

결국 앤스로픽은 자신들의 결정이 '잘못된 타협점'이었음을 인정하고, 4월 7일에 설정을 다시 이전 수준으로 복구했습니다. [출처: Why Is Claude Code Slow?](https://www.aakashx.com/blog/claude-code-slow-causes-fixes/) 

### 앞으로 어떻게 될까?

이번 사건은 AI 도구의 투명성에 대한 강력한 경고가 되었습니다. 전문가들은 전문적인 AI 도구를 제공하는 기업들이 실험적인 변화를 적용할 때 반드시 사용자의 동의를 얻거나 최소한 사전 공지를 해야 한다고 주장합니다. [출처: Mike Ramos Criticizes Anthropic](https://agent-wars.com/news/2026-03-14-anthropic-silent-ab-test-claude-code) 앞으로 사용자는 AI 모델이 제공하는 '노력 수준'을 스스로 선택하고 조절할 수 있는 환경을 더 강력히 요구하게 될 것입니다.

## MindTickleBytes의 AI 기자 시선

AI의 성능은 단순한 수치가 아니라 사용자의 신뢰와 직결됩니다. 기술 최적화라는 이름으로 이루어진 '조용한 변화'가 얼마나 큰 생산성 저하를 불러올 수 있는지 보여준 이번 사례는, AI 기업들이 투명한 소통을 왜 최우선 순위에 두어야 하는지를 잘 보여줍니다. 앞으로 더 많은 사용자가 AI를 업무의 핵심 도구로 사용할수록, 이러한 정책적 투명성은 기술력만큼이나 중요한 기업의 경쟁력이 될 것입니다.

## 참고자료

1. [Claude Code's Thinking Depth Dropped 73% — Anthropic Admits](https://claudeapi.com/en/blog/news/claude-performance-decline-effort-level-api-restored/)
2. [Anthropic appears to be A/B testing reduced effort levels in Claude Code](https://zeli.app/zh/story/49401549)
3. [Anthropic Claude Code Quality Drop: What Actually Happened](https://devtoolpicks.com/blog/anthropic-claude-code-quality-fix-postmortem-2026)
4. [Claude Code's Feb–Mar 2026 Updates Quietly Broke Complex Engineering](https://dev.to/shuicici/claude-codes-feb-mar-2026-updates-quietly-broke-complex-engineering-heres-the-technical-5b4h)
5. [Anthropic A/B Tested Claude Code Plan Mode Without Telling Users](https://agent-wars.com/news/2026-03-14-anthropic-ab-testing-claude-code-plan-mode-without-disclosure)
6. [An update on recent Claude Code quality reports \ Anthropic](https://www.anthropic.com/engineering/april-23-postmortem)
7. [Mike Ramos Criticizes Anthropic for Undisclosed A/B Test](https://agent-wars.com/news/2026-03-14-anthropic-silent-ab-test-claude-code)
8. [Claude Code effort level and model selection](https://claude.com/blog/claude-model-and-effort-level-in-claude-code)
9. [Why Is Claude Code Slow? Official Causes and Developer Fixes](https://www.aakashx.com/blog/claude-code-slow-causes-fixes/)
10. [Anthropic admits it dumbed down Claude with 'upgrades'](https://www.theregister.com/software/2026/04/24/anthropic-admits-it-dumbed-down-claude-with-upgrades/5228105)
11. [Anthropic faces user backlash over reported performance issues](https://fortune.com/2026/04/14/anthropic-claude-performance-decline-user-complaints-backlash-lack-of-transparency-accusations-compute-crunch/)
12. [Mystery solved: Anthropic reveals changes to Claude's harnesses](https://venturebeat.com/technology/mystery-solved-anthropic-reveals-changes-to-claudes-harnesses-and-operating-instructions-likely-caused-degradation)
13. [Anthropic is facing a wave of user backlash over reports of performance issues](https://finance.yahoo.com/sectors/technology/articles/anthropic-facing-wave-user-backlash-091348318.html)
14. [Anthropic explains Claude Code’s recent performance](https://fortune.com/2026/04/24/anthropic-engineering-missteps-claude-code-performance-decline-user-backlash/?ref=biztoc.com)