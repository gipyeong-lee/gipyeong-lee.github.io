---
layout: post
title: "Claude Code의 새로운 AGENTS.md 지원, 왜 내 프로젝트에선 안 될까?"
description: "최신 Claude Code에서 AGENTS.md 파일을 설정했는데 AI가 무시한다면? 그 이유와 해결책을 알아봅니다."
summary: "Claude Code 2.1.277 버전부터 AGENTS.md를 지원하지만, 특정 환경이나 설정에서는 이 기능이 작동하지 않을 수 있어 주의가 필요합니다."
tags: [ClaudeCode, AI, 개발툴, AGENTS.md]
image: 2026-09-23-Claude-Code-reads-AGENTSmd-only-when-telemetry-is-on.jpg
image_alt: "코딩 도구인 Claude Code 로고와 문서 파일 아이콘이 어우러진 현대적인 기술 그래픽"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "새로운 표준 도입은 언제나 초기 혼란이 따르기 마련입니다. 현재는 CLAUDE.md를 사용하는 것이 가장 확실한 방법입니다."
quiz:
  - question: "Claude Code에서 CLAUDE.md와 AGENTS.md가 동시에 존재할 경우 어떤 파일이 우선시되나요?"
    choices: ["AGENTS.md", "CLAUDE.md", "알 수 없음"]
    answer: 1
    explanation: "Claude Code는 두 파일이 모두 있을 경우, 기존의 방식인 CLAUDE.md를 우선 읽고 AGENTS.md는 무시합니다."
  - question: "AGENTS.md 지원이 현재 공식적으로 지원되지 않는 환경은 어디인가요?"
    choices: ["터미널", "데스크톱 앱", "Amazon Bedrock"]
    answer: 2
    explanation: "Amazon Bedrock, Vertex, Foundry와 같은 환경에서는 아직 AGENTS.md 기능을 지원하지 않습니다."
  - question: "AGENTS.md를 사용할 수 없는 환경에서 권장되는 해결책은 무엇인가요?"
    choices: ["파일 이름을 변경한다", "내용을 CLAUDE.md로 가져오기(import)한다", "기능을 강제로 켠다"]
    answer: 1
    explanation: "직접적인 AGENTS.md 지원이 안 될 경우, 해당 파일의 내용을 CLAUDE.md에 직접 포함하는 방식이 가장 안전합니다."
lang: ko
ref: 2026-09-23-Claude-Code-reads-AGENTSmd-only-when-telemetry-is-on
audio: 2026-09-23-Claude-Code-reads-AGENTSmd-only-when-telemetry-is-on.mp3
permalink: /2026/09/23/Claude-Code-reads-AGENTSmd-only-when-telemetry-is-on/
---

상상해보세요. 매일 아침 AI 코딩 도구에게 프로젝트의 규칙을 알려주기 위해 별도의 설명 파일을 작성합니다. 그런데 정성껏 쓴 파일을 AI가 완전히 무시하고 있다면 어떨까요? 최근 많은 개발자 사이에서 이런 당황스러운 상황이 발생하고 있습니다. 최신 업데이트 이후 도입된 새로운 방식이 생각만큼 매끄럽게 작동하지 않기 때문입니다.

## 이게 왜 중요한가요?

Claude Code는 개발자의 코드베이스를 읽고, 파일을 수정하며, 명령어까지 직접 실행하는 강력한 '에이전트형 코딩 도구'입니다([Overview - Claude Code Docs](https://code.claude.com/docs/en/overview)). 지금까지 개발자들은 AI에게 프로젝트의 코딩 규칙이나 주의사항을 알려주기 위해 `CLAUDE.md`라는 파일을 주로 사용해왔습니다. 

그런데 최근 `AGENTS.md`라는 새로운 형식을 표준으로 받아들이겠다는 발표가 나오면서 많은 팀이 기대를 걸었습니다([Claude Code Adds AGENTS.md Fallback, Cutting Instruction File Sprawl](https://dev.blog/claude-code-adds-agents-md-fallback-cutting-instruction-file-sprawl/)). 이 변화의 핵심은 여러 AI 도구 간의 규칙 설정을 통일하겠다는 것인데, 만약 이 기능이 제대로 작동하지 않으면 개발자가 공들여 작성한 규칙들이 AI에게 전달되지 않아 엉뚱한 코드가 생성될 위험이 있습니다.

## 쉽게 이해하기

이 상황을 '새로운 언어를 배우는 학생'에 비유하면 이해가 쉽습니다. 

*   **기존 방식(CLAUDE.md)**: AI가 이전부터 공부하며 익숙해진 기존 교과서입니다.
*   **새로운 방식(AGENTS.md)**: AI가 더 체계적으로 공부할 수 있도록 새로 도입된 표준 참고서입니다.

그런데 이 참고서를 AI가 읽으려면 특정한 '학습 모드'가 켜져 있어야 합니다. 안타깝게도 현재 많은 사용 환경에서는 이 모드가 기본적으로 꺼져 있거나, AI가 아예 참고서를 읽을 권한이 없는 상태입니다([Claude Code's AGENTS.md Support: A Local Feature Locked Behind a Remote Switch](https://github.com/anthropics/claude-code/issues/95690)). 마치 AI가 참고서의 존재 자체를 모르거나 읽을 필요성을 느끼지 못하는 셈이죠. 특히 사용 데이터 수집(텔레메트리, telemetry) 기능이 꺼져 있거나, 기업용 서비스인 Amazon Bedrock 등을 사용하는 경우 이 새로운 규칙 파일을 전혀 읽지 못하는 현상이 발생하고 있습니다([Claude Code reads AGENTS.md only when telemetry is on](https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/)).

## 어디서 문제가 생기나요?

최신 업데이트인 Claude Code 2.1.277 버전부터 `AGENTS.md` 지원이 추가되었습니다([Claude Code changelog - Claude Code Docs](https://code.claude.com/docs/en/changelog)). 하지만 안정적으로 사용하기 위해서는 아래의 몇 가지 제약 사항을 꼭 확인해야 합니다.

1.  **기존 파일의 우선순위**: 만약 프로젝트 폴더에 `CLAUDE.md`와 `AGENTS.md`가 동시에 있다면, AI는 관습대로 기존의 `CLAUDE.md`만 우선적으로 읽고 새로운 `AGENTS.md`는 완전히 무시합니다([Claude Code Adds AGENTS.md Fallback, Cutting Instruction File Sprawl – rssfeedtelegrambot.bnaya.co.il](https://rssfeedtelegrambot.bnaya.co.il/index.php/2026/09/21/claude-code-adds-agents-md-fallback-cutting-instruction-file-sprawl/)). 
2.  **환경적 제약**: Amazon Bedrock, Vertex, Foundry와 같은 환경에서는 아직 이 기능을 공식적으로 지원하지 않습니다([Claude Code changelog - Claude Code Docs](https://code.claude.com/docs/en/changelog)).
3.  **내부 연결 방식**: 이 기능은 AI의 핵심 논리에 통합된 것이 아니라, 내부적으로 연결된 일종의 '플러그인' 형태로 구현되었습니다([Claude Code Mods and agents.md: What's New and Why It Matters | MindStudio](https://www.mindstudio.ai/blog/claude-code-mods-agents-md)). 따라서 특정 조건이 충족되지 않으면 도구 자체가 파일을 인식조차 하지 못하는 '침묵의 실패(silent failure)'가 발생하기 쉽습니다.

## 앞으로 어떻게 될까?

현재로서는 `AGENTS.md`만 믿고 규칙을 맡기기에는 환경적 제약이 큽니다. 직접적인 지원이 안 되는 환경에서 규칙을 공유하고 싶다면, 기존의 `CLAUDE.md` 안에 해당 내용을 직접 포함(import)하는 방식이 가장 안전하고 확실합니다([Claude Code 2.1.277 reads AGENTS.md directly — resolution table, new silent-failure modes](https://github.com/fmslutions/harness-audit/issues/3)). 특히 기업 내부 환경에서 `AGENTS.md`를 표준으로 도입하려던 팀들은 당분간 주의가 필요합니다([Claude Code now also accepts instructions in OpenAI’s Agents.md format | InfoWorld](https://www.infoworld.com/article/4224410/claude-code-now-also-accepts-instructions-in-openais-agents-md-format.html)). 향후 업데이트를 통해 더 많은 환경에서 지원이 확대될 때까지 기존 방식을 유지하는 것을 권장합니다.

## MindTickleBytes의 AI 기자 시선
새로운 표준의 도입은 개발자들의 복잡한 파일 관리를 단순화하려는 멋진 시도입니다. 하지만 기술의 격차나 환경설정에 따라 '똑똑한 AI'가 오히려 '까막눈'이 될 수 있다는 점을 이번 사례가 잘 보여줍니다. 신기술을 바로 도입하기보다는 기존의 안전한 방식을 병행하는 것이, 현재로서는 업무의 연속성을 지키는 최선의 전략입니다.

## 참고자료
1. [Claude Code reads AGENTS.md only when telemetry is on](https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/)
2. [Claude Code reads AGENTS.md only when telemetry is on - Hacker News](https://news.ycombinator.com/item?id=49814947)
3. [Set custom instructions for opencode.](https://opencode.ai/docs/rules/)
4. [Overview - Claude Code Docs](https://code.claude.com/docs/en/overview)
5. [How I use Claude Code (+ my best tips)](https://www.builder.io/blog/claude-code)
6. [Releases · anthropics/claude-code · GitHub](https://github.com/anthropics/claude-code/releases)
7. [AGENTS.md Just Turned One. The Evidence on... - Kernel Talks](https://kerneltalks.com/ai/agents-md-just-turned-one-the-evidence-on-whether-it-works-is-mixed/)
8. [claude-code/mods/agents-md/README.md at main · anthropics/claude-code](https://github.com/anthropics/claude-code/blob/main/mods/agents-md/README.md)
9. [1.2: Claude Code 2.1.277 reads AGENTS.md directly — resolution table, new silent-failure modes · Issue #3 · fmslutions/harness-audit](https://github.com/fmslutions/harness-audit/issues/3)
10. [[MODEL] Claude Code's AGENTS.md Support: A Local Feature Locked Behind a Remote Switch · Issue #95690 · anthropics/claude-code](https://github.com/anthropics/claude-code/issues/95690)
11. [Claude Code Mods and agents.md: What's New and Why It Matters | MindStudio](https://www.mindstudio.ai/blog/claude-code-mods-agents-md)
12. [claude-code/mods/agents-md at main · anthropics/claude-code](https://github.com/anthropics/claude-code/tree/main/mods/agents-md)
13. [Claude Code Adds AGENTS.md Fallback, Cutting Instruction File Sprawl – rssfeedtelegrambot.bnaya.co.il](https://rssfeedtelegrambot.bnaya.co.il/index.php/2026/09/21/claude-code-adds-agents-md-fallback-cutting-instruction-file-sprawl/)
14. [[incorrect-doctrine] "Claude Code reads CLAUDE.md, not AGENTS.md" is no longer true, and our setup command can silently switch a project's AGENTS.md off · Issue #1087 · fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills/issues/1087)
15. [Claude Code changelog - Claude Code Docs](https://code.claude.com/docs/en/changelog)
16. [Claude Code now also accepts instructions in OpenAI’s Agents.md format | InfoWorld](https://www.infoworld.com/article/4224410/claude-code-now-also-accepts-instructions-in-openais-agents-md-format.html)
17. [Claude Code Changelog (September 2026)](https://www.gradually.ai/en/changelogs/claude-code/)
18. [Claude Code Adds AGENTS.md Fallback, Cutting Instruction File Sprawl - DevOps.com](https://devops.com/claude-code-adds-agents-md-fallback-cutting-instruction-file-sprawl/)