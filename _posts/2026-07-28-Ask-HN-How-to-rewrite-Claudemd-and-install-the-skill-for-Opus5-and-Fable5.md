---
layout: post
title: "내 AI 비서가 똑똑해졌다? 클로드 Opus 5와 Fable 5, 제대로 쓰는 법"
description: "앤스로픽의 최신 AI 모델인 클로드 Opus 5와 Fable 5로 업데이트하는 방법과 기존 설정을 최적화하는 팁을 소개합니다."
summary: "앤스로픽의 새 AI 모델 도입에 맞춰 기존 설정 파일을 최적화하고, 클로드 코드의 /doctor 기능을 통해 새 모델의 성능을 100% 활용하는 방법을 안내합니다."
tags: [AI, 클로드, Opus5, Fable5, 생산성]
image: 2026-07-28-Ask-HN-How-to-rewrite-Claudemd-and-install-the-skill-for-Opus5-and-Fable5.jpg
image_alt: "최신 AI 모델인 클로드 Opus 5와 Fable 5의 로고가 나란히 놓여 있는 모습."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "새로운 기술의 도약은 항상 적응을 요구합니다. 도구에 끌려다니지 말고, 설정 최적화를 통해 AI를 진정한 나의 페이스메이커로 만드세요."
quiz:
  - question: "기존의 CLAUDE.md 파일을 최신 모델에 맞게 조정하려면 어떤 명령어를 사용하는 것이 권장되나요?"
    choices: ["/update", "/doctor", "/optimize"]
    answer: 1
    explanation: "클로드 코드(Claude Code)에서 제공하는 /doctor 명령어를 사용하면 새 모델 환경에 맞게 스킬과 CLAUDE.md 파일을 최적화할 수 있습니다."
  - question: "클로드 Fable 5의 특징으로 가장 적절한 것은 무엇인가요?"
    choices: ["간단한 대화 전용 모델", "복잡하고 긴 프로젝트에 최적화된 모델", "이미지 생성 전문 모델"]
    answer: 1
    explanation: "클로드 Fable 5는 'Mythos-level' 모델로, 특히 복잡하고 긴 호흡이 필요한 프로젝트를 주도적으로 수행하고 스스로 결과물을 검증하는 데 탁월합니다."
  - question: "Opus 5와 Fable 5 도입 시 기존 리소스(CLAUDE.md, 스킬 등)는 어떻게 해야 하나요?"
    choices: ["그대로 사용해도 무방하다", "최신 모델에 맞춰 업데이트가 필요하다", "삭제해야 한다"]
    answer: 1
    explanation: "이전 모델의 설정은 최신 모델과 완벽하게 호환되지 않을 수 있으므로, 최신 환경에 맞춰 재설정하거나 최적화하는 과정이 필요합니다."
lang: ko
ref: 2026-07-28-Ask-HN-How-to-rewrite-Claudemd-and-install-the-skill-for-Opus5-and-Fable5
audio: 2026-07-28-Ask-HN-How-to-rewrite-Claudemd-and-install-the-skill-for-Opus5-and-Fable5.mp3
permalink: /2026/07/28/Ask-HN-How-to-rewrite-Claudemd-and-install-the-skill-for-Opus5-and-Fable5/
---

상상해보세요. 매일 사용하는 AI 비서가 갑자기 최신형 '슈퍼 컴퓨터' 수준의 지능으로 업그레이드되었습니다. 그런데 막상 평소처럼 명령을 내렸더니, 예전만큼 똑똑하게 반응하지 않습니다. 도대체 왜 이런 일이 생길까요?

앤스로픽(Anthropic)이 최근 선보인 최신 AI 모델인 **클로드 Opus 5**와 **Fable 5**가 바로 그런 경우입니다. 기존에 공들여 설정해둔 비서의 '가이드라인'이 새 모델의 사고방식과는 조금 차이가 있기 때문이죠. 마치 아주 똑똑해진 제자에게 여전히 '유치원생용 학습지'를 풀라고 하는 상황과 비슷합니다.

### 왜 업데이트가 필요한가요?

AI 기술의 발전은 단순히 모델의 지능 수치만 높이는 과정이 아닙니다. 예전에는 AI에게 아주 구체적인 지시를 하나하나 내려야 했다면, 최신 모델들은 스스로 생각하고 검증하는 능력이 훨씬 강력해졌습니다. [클로드 Fable 5](https://www.anthropic.com/claude/fable)는 특히 복잡하고 긴 프로젝트를 수행하는 데 특화되어 있어, 마치 베테랑 연구원과 협업하는 듯한 놀라운 경험을 제공합니다([클로드 Fable 5](https://miniapps.ai/claude-5-fable)). 

하지만 우리가 예전 모델을 위해 작성해둔 설정 파일(`CLAUDE.md`)이나 커스텀 스킬들은 새 모델의 작동 방식과 완전히 호환되지 않을 수 있습니다([출처: Ask HN](https://news.mcan.sh/item/49080135)). 즉, 설정을 그대로 방치하면, 당신의 비서는 잠재력을 100% 발휘하지 못하고 구식 가이드라인에 갇힌 채 제 성능을 내지 못하게 됩니다.

### 쉽게 이해하기: '고급 비서' 길들이기

AI 모델의 설정 파일을 '비서에게 건네는 업무 매뉴얼'이라고 생각해보세요. 기존 매뉴얼이 '간단한 심부름'을 잘하도록 짜여 있었다면, 새로운 매뉴얼은 '전략적 의사결정'까지 가능하도록 업데이트되어야 합니다.

- **비유하자면**: 당신이 10년 전 신입사원에게 준 업무 매뉴얼을 그대로 팀장에게 주고 있는 셈입니다. 팀장은 더 큰 그림을 보고 스스로 판단하고 싶어 하는데, 매뉴얼에는 "커피는 이렇게 타세요"라는 세세한 내용만 적혀 있다면 비효율적이겠죠? 
- **설정 최적화**: 앤스로픽은 새 모델의 특징인 응답의 길이 조절, 스스로 판단하여 임무를 쪼개는 능력 등을 잘 활용할 수 있도록 가이드라인을 수정하라고 권장합니다([출처: Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)).

### 현재 상황: 어떻게 시작할까?

가장 먼저 할 일은 전문가의 도움을 받는 것입니다. 클로드 코드(Claude Code)를 사용 중이라면 `/doctor` 명령어를 입력해보세요. 이 명령어는 당신의 시스템이 새 모델의 환경에 맞춰 적절하게 세팅되었는지 확인하고, 스킬과 `CLAUDE.md` 파일을 최신 환경에 맞게 자동으로 정리해줍니다([출처: The new rules of context engineering](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models)).

1. **설정 업데이트**: 기존의 `CLAUDE.md`와 스킬 파일들을 최신 모델의 요구사항에 맞춰 단순화하고 최적화해야 합니다([출처: Anthropic Releases Claude Opus 5](https://www.ghacks.net/2026/07/27/anthropic-releases-claude-opus-5-at-half-the-token-price-of-claude-fable-5/)).
2. **모델 선택**: 새로운 클로드 코드 세션에서 모델을 선택하고, 작업의 복잡도에 따라 effort(노력치) 레벨을 조정하여 성능을 최적화하세요([출처: Claude code update](https://thevibefather.com/blog/claude-code-opus-5-update-effort-guide)).

### 앞으로 어떻게 될까?

클로드 Fable 5와 같은 모델들은 앞으로 100만 토큰(AI가 한 번에 기억할 수 있는 정보의 단위 — 책 수십 권 분량)에 달하는 방대한 문맥을 이해하며, 스스로 코드를 작성하고 검증까지 완료하는 수준으로 발전할 것입니다([출처: Fable5AI](https://fable5.io/)). 앞으로는 단순한 코딩을 넘어, AI 비서와 함께 당신의 아이디어를 설계하고, 복잡한 오류를 스스로 찾아 해결하는 시대가 열리고 있습니다. 이제 당신이 해야 할 일은 이 강력한 비서를 위한 '매뉴얼'을 최신 버전으로 업데이트하는 것뿐입니다.

### MindTickleBytes의 AI 기자 시선
기술은 항상 우리가 생각하는 것보다 빠르게 달립니다. 도구를 바꾸는 것보다 중요한 것은 그 도구를 다루는 우리의 '질문하는 방식'을 바꾸는 것입니다. 최신 설정으로 AI를 깨우고, 더 큰 문제를 해결해보세요.

## 참고자료
1. [Ask HN: How to rewrite `Claude.md` and install the skill for Opus5 and Fable5](https://news.mcan.sh/item/49080135)
2. [GitHub - DizzyMii/fable-skills: Six Claude Code skills](https://github.com/DizzyMii/fable-skills)
3. [The new rules of context engineering for Claude 5 generation models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models)
4. [Prompting Claude Opus 5 - Claude Platform Docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)
5. [Claude Opus 5 in Claude Code: A 2026 Guide - codersera.com](https://codersera.com/blog/claude-opus-5-claude-code-guide-2026/)
6. [Claude code update — Using Claude Opus 5 in Claude Code](https://thevibefather.com/blog/claude-code-opus-5-update-effort-guide)
7. [Writing Opus 5 / Fable 5 Prompts - GitHub](https://github.com/CodingCossack/writing-opus-5-fable-5-prompts)
8. [claude-skills/fable-mode/SKILL.md](https://github.com/henriquetell/claude-skills/blob/main/fable-mode/SKILL.md)
9. [GitHub - samirinyemi/fable5-skill-library](https://github.com/samirinyemi/fable5-skill-library)
10. [Hacker News | Ask HN](https://nilaykhandelwal.com/item/49080135)
11. [Claude Opus 5 Is Powerful. Your Setup Decides How Powerful](https://emergingai.substack.com/p/claude-opus-5-is-powerful-your-setup)
12. [Karpathy's CLAUDE.md Skills File: The Complete Guide](https://agentpedia.codes/blog/karpathy-claude-code-skills-guide)
13. [Migration guide - Claude Platform Docs](https://platform.claude.com/docs/en/about-claude/models/migration-guide)
14. [Claude](https://claude.com/)
15. [Claude Fable | Anthropic](https://www.anthropic.com/claude/fable)
16. [Fable5AI — Independent Model Guide & Prompt Workspace](https://fable5.io/)
17. [Claude Opus 5 review: great at coding (but I hate talking to it)](https://www.youtube.com/watch?v=dfre9hN0HCs)
18. [GitHub - alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)
19. [Claude Fable 5 · Free AI Chatbot](https://miniapps.ai/claude-5-fable)
20. [Anthropic Releases Claude Opus 5 at Half the Token Price of Claude Fable 5 - gHacks TechNews](https://www.ghacks.net/2026/07/27/anthropic-releases-claude-opus-5-at-half-the-token-price-of-claude-fable-5/)