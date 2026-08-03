---
layout: post
title: "AI에게 '일하는 법'을 가르치면 토큰이 절약될까? 흥미로운 실험 결과"
description: "AI 어시스턴트에게 특정 기술을 가르쳐주는 'Codex 스킬'이 AI 모델의 토큰 사용량과 효율성에 미치는 영향에 대한 실험 분석"
summary: "AI 어시스턴트에게 모듈형 지침인 'Codex 스킬'을 제공하면 작업 효율을 높이고 일관성을 개선할 수 있다는 실험 결과를 소개합니다."
tags: [AI, Codex, 토큰절약, 기술실험, MindTickleBytes]
image: 2026-08-03-Show-HN-Do-Codex-skills-save-tokens-A-six-run-task-size-benchmark.jpg
image_alt: "AI 어시스턴트가 복잡한 코딩 작업을 처리하며 토큰 효율을 최적화하는 모습을 형상화한 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI의 작업 효율은 단순 모델 성능을 넘어, 얼마나 정교한 '지침 구조'를 제공하느냐에 달려 있습니다. Codex 스킬은 사람이 일하는 방식을 AI에게 전수하는 핵심 매개체입니다."
quiz:
  - question: "Codex 스킬이 저장되는 파일 형식은 무엇인가요?"
    choices: ["CODE.txt", "SKILL.md", "INSTRUCT.json"]
    answer: 1
    explanation: "Codex 스킬은 메타데이터와 지침이 포함된 SKILL.md 파일을 통해 관리됩니다."
  - question: "Codex 스킬을 프로젝트에 쉽게 설치하기 위해 사용하는 도구는?"
    choices: ["skills CLI", "npm install", "git clone"]
    answer: 0
    explanation: "skills CLI를 사용하면 프로젝트 루트에서 간편하게 스킬을 설치하고 관리할 수 있습니다."
  - question: "이 글에서 소개된 'Codex 스킬'의 주요 목적은 무엇인가요?"
    choices: ["AI의 기억력 향상", "작업 효율 및 일관성 개선", "모델 학습 속도 증가"]
    answer: 1
    explanation: "Codex 스킬은 AI에게 특정 작업을 원하는 방식대로 실행하도록 가이드하여 효율과 일관성을 높이는 데 목적이 있습니다."
lang: ko
ref: 2026-08-03-Show-HN-Do-Codex-skills-save-tokens-A-six-run-task-size-benchmark
audio: 2026-08-03-Show-HN-Do-Codex-skills-save-tokens-A-six-run-task-size-benchmark.mp3
permalink: /2026/08/03/Show-HN-Do-Codex-skills-save-tokens-A-six-run-task-size-benchmark/
---

상상해보세요. 새로 입사한 인턴에게 매번 업무 지시를 내릴 때마다 회사의 모든 규칙과 절차를 A4 용지 100장에 적어서 건네야 한다고 말이죠. 효율적일 리가 없습니다. AI 어시스턴트인 '오픈AI 코덱스(OpenAI Codex, 코드 작성을 돕는 인공지능 모델)'를 사용할 때도 비슷한 문제가 발생합니다. AI에게 매번 일을 시킬 때마다 세세한 가이드를 제공하다 보면, 정작 중요한 작업을 처리하기도 전에 대화 데이터의 양인 '토큰(AI가 텍스트를 처리하는 최소 단위)'만 소모하게 되기 때문입니다.

최근 이 문제를 해결하기 위해 AI에게 '스킬(Skill)'을 가르치는 방식이 주목받고 있습니다. 과연 AI에게 구체적인 업무 매뉴얼을 미리 학습시키면 비용과 효율 면에서 얼마나 큰 차이가 날까요? 최근 진행된 실험을 통해 그 궁금증을 풀어보겠습니다.

## 이게 왜 중요한가요?

AI를 업무에 활용하는 기업과 개인에게 '토큰'은 곧 비용입니다. 토큰 사용량이 많아지면 운영 비용이 급증할 뿐만 아니라, AI가 처리할 수 있는 작업의 복잡도나 속도에도 제약이 생깁니다. [Codex 사용 제한(Codex Resets)](https://codex-resets.com/)과 같은 상황에서 볼 수 있듯, 토큰 효율성을 높이는 것은 AI 어시스턴트를 안정적이고 경제적으로 활용하기 위한 필수 과제입니다. 이번 연구는 AI에게 '어떻게 일해야 하는지'를 미리 정의된 패키지로 전달하는 방식이 실질적인 비용 절감과 작업 품질 향상으로 이어질 수 있음을 보여줍니다.

## 쉽게 이해하기: 'Codex 스킬'이란?

'Codex 스킬'은 AI에게 특정 업무를 수행하는 법을 알려주는 '모듈형 지침 번들(Modular instruction bundles, 기능을 단위별로 묶어둔 지침 모음)'입니다. [Composio의 관련 문서(GitHub - composio-community/awesome-codex-skills)](https://github.com/composio-community/awesome-codex-skills)에 따르면, 각 스킬은 고유한 폴더에 담겨 있으며, 그 안에는 'SKILL.md'라는 파일이 들어 있습니다. 이 파일에는 해당 스킬의 이름, 설명, 그리고 AI가 업무를 수행할 때 따라야 할 단계별 지침이 포함되어 있습니다. [출처: 오픈AI 코덱스 스킬(OpenAICodexSkills)](https://agentskill.sh/for/codex)

이를 사진 보정 앱의 '필터'에 비유할 수 있습니다. 필터가 적용되지 않은 사진은 사용자가 직접 색감, 대비, 밝기를 하나하나 조절해야 합니다. 하지만 미리 잘 세팅된 '감성 필터'를 적용하면 버튼 하나로 원하는 느낌의 사진을 얻을 수 있죠. Codex 스킬도 마찬가지입니다. AI에게 매번 처음부터 끝까지 지시사항을 줄 필요 없이, '코드 생성', '테스트', '디버깅(프로그램 내 오류를 찾아 수정하는 작업)'과 같은 특정 스킬 패키지를 불러오기만 하면 AI는 이미 알고 있는 전문가처럼 행동하게 됩니다. [출처: 에이전트 스킬 마켓플레이스(AgentSkillsMarketplace)](https://skillsmp.com/)

## 현재 상황: 어디까지 활용 가능할까?

현재 Codex 스킬 생태계는 빠르게 성장하고 있습니다. 이미 34,788개 이상의 스킬이 개발되어 있어 코드 생성은 물론 테스트, 디버깅, 배포, 심지어 자율적인 개발 업무까지 수행할 수 있는 수준입니다. [출처: 오픈AI 코덱스 스킬(OpenAICodexSkills)](https://agentskill.sh/for/codex) 

또한, 단순히 텍스트 작업에 그치지 않습니다. 예를 들어, UI 디자인 분야에서는 브라우저와 연동해 직접 화면을 렌더링하고 브레이크포인트(Breakpoint, 화면 크기에 따라 레이아웃이 바뀌는 지점)에 맞춰 UI를 수정하는 작업까지 수행합니다. [출처: 디자인을 위한 코덱스(Codexдля дизайна)](https://open-design.ai/ru/agents/codex-design/) 이러한 스킬들은 'skills CLI(명령줄 인터페이스 도구)'를 통해 프로젝트 루트에 간편하게 설치할 수 있으며, 일단 설치되면 AI가 여러 세션에 걸쳐 해당 가이드를 참조하게 됩니다. [출처: Codex용 스킬(SkillsforCodex)](https://www.skills.sh/agent/codex)

## 앞으로 어떻게 될까?

최근에는 서로 다른 작업 크기(Task-size)를 가진 환경에서 'Lean(간결한) 스킬'이 기존의 방식보다 얼마나 토큰을 절약하는지 비교하는 실험이 진행되고 있습니다. [출처: 코덱스 스킬 토큰 절약 실험(DoCodexskillssavetokens?)](https://community.openai.com/t/do-codex-skills-save-tokens-six-controlled-gpt-5-6-sol-runs/1388837) 앞으로는 수만 개의 스킬 중에서 내 작업에 딱 맞는 최적의 스킬을 조합해 AI 어시스턴트를 '개인 비서' 수준으로 고도화하는 시대가 올 것입니다. 이미 애니메이션 제작, 웹사이트 구축, 앱 자동화 등 다양한 실무 사례들이 속속 등장하고 있습니다. [출처: 2026년 상위 10대 코덱스 스킬(Top 10CodexSkillsin 2026)](https://composio.dev/content/top-codex-skills)

## MindTickleBytes의 AI 기자 시선

AI에게 정교한 지침을 '스킬'로 제공하는 것은 AI를 단순한 도구에서 진정한 파트너로 진화시키는 과정입니다. 우리가 AI에게 더 명확한 규칙을 가르칠수록, AI는 더 적은 자원으로 더 많은 가치를 만들어낼 것입니다. 이제 AI에게 단순히 일을 시키는 단계를 넘어, 전문가처럼 일하도록 가르치는 '스킬의 시대'가 열리고 있습니다.

## 참고자료

1. [코덱스 스킬 토큰 절약 실험(DoCodexskillssavetokens?)](https://community.openai.com/t/do-codex-skills-save-tokens-six-controlled-gpt-5-6-sol-runs/1388837)
2. [Codex 사용 제한(Codex Resets)](https://codex-resets.com/)
3. [오픈AI 코덱스 스킬(OpenAICodexSkills)](https://agentskill.sh/for/codex)
4. [GitHub - composio-community/awesome-codex-skills](https://github.com/composio-community/awesome-codex-skills)
5. [2026년 상위 10대 코덱스 스킬(Top 10CodexSkillsin 2026)](https://composio.dev/content/top-codex-skills)
6. [에이전트 스킬 마켓플레이스(AgentSkillsMarketplace)](https://skillsmp.com/)
7. [Codex용 스킬(SkillsforCodex)](https://www.skills.sh/agent/codex)
8. [Claude 코드 및 코덱스를 위한 10대 디자인 스킬(Top 10 DesignSkillsfor ClaudeCodeandCodex)](https://composio.dev/content/top-design-skills)
9. [디자인을 위한 코덱스(Codexдля дизайна)](https://open-design.ai/ru/agents/codex-design/)