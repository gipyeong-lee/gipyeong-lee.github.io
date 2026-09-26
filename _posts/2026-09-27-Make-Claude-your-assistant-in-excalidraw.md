---
layout: post
title: "AI가 직접 그림을 그린다고? Claude와 Excalidraw로 시작하는 업무의 시각화"
description: "AI에게 말만 하면 복잡한 다이어그램을 척척 그려주는 Excalidraw 활용법을 소개합니다."
summary: "AI 에이전트와 Excalidraw를 연동해 말 한마디로 편집 가능한 다이어그램을 생성하고 수정하는 혁신적인 업무 방식을 알아봅니다."
tags: [AI, Excalidraw, 생산성, Claude, 업무자동화]
image: 2026-09-27-Make-Claude-your-assistant-in-excalidraw.jpg
image_alt: "AI 에이전트가 Excalidraw 화이트보드 위에서 복잡한 아키텍처 다이어그램을 그리는 모습"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "복잡한 생각을 시각적 언어로 바로 번역하는 것은 인간과 AI 협업의 새로운 지평입니다. 이제 다이어그램은 그리는 것이 아니라 '요청'하는 것이 됩니다."
quiz:
  - question: "AI 에이전트가 Excalidraw 다이어그램을 생성한 후 스스로 수정할 수 있게 만드는 핵심 기술은 무엇인가요?"
    choices: ["스크린샷을 통한 시각적 확인", "코드 자동 컴파일", "브라우저 자동 새로고침"]
    answer: 0
    explanation: "AI 에이전트는 생성한 다이어그램을 스크린샷으로 확인하여 레이아웃 오류나 겹침 현상을 스스로 감지하고 수정할 수 있습니다."
  - question: "생성된 다이어그램을 프로젝트 저장소에 직접 커밋할 수 있는 형식은 무엇인가요?"
    choices: ["이미지(JPG)", "편집 가능한 .excalidraw JSON", "텍스트(TXT)"]
    answer: 1
    explanation: "많은 Excalidraw 연동 툴은 다이어그램을 편집 가능한 .excalidraw JSON 파일로 내보내어, 코드와 함께 저장소에 보관할 수 있게 합니다."
  - question: "Excalidraw와 AI 에이전트를 연결하는 데 사용되는 프로토콜은 무엇인가요?"
    choices: ["HTTP", "MCP (Model Context Protocol)", "FTP"]
    answer: 1
    explanation: "MCP(Model Context Protocol) 서버 구현을 통해 AI 에이전트가 인터랙티브한 Excalidraw 화이트보드에 접근할 수 있습니다."
lang: ko
ref: 2026-09-27-Make-Claude-your-assistant-in-excalidraw
audio: 2026-09-27-Make-Claude-your-assistant-in-excalidraw.mp3
permalink: /2026/09/27/Make-Claude-your-assistant-in-excalidraw/
---

상상해보세요. 복잡한 시스템 구조를 설계하거나 팀원들에게 업무 흐름을 설명해야 할 때, 화이트보드 앱을 켜서 마우스를 이리저리 움직이며 도형을 배치하던 번거로운 시간은 이제 과거의 일이 될지도 모릅니다. 대신 이렇게 말해보는 건 어떨까요? "방금 우리가 논의한 시스템의 연결 구조를 Excalidraw로 그려주고, 보기 좋게 배치해줘."

컴퓨터가 단순히 텍스트를 처리하는 것을 넘어, 이제는 직접 화이트보드 앞에 서서 시각적인 논리를 구성하는 시대가 오고 있습니다. 

## 이게 왜 중요한가요? (Why It Matters)

기존에는 다이어그램을 그리는 것이 오로지 사람의 '수작업' 영역이었습니다. 복잡한 로직을 머릿속으로 정리하고, 이를 도구로 옮기는 과정에서 많은 시간과 에너지가 소모되었죠. 하지만 AI 에이전트가 이 과정을 대신 수행할 수 있게 되면서, 개발자나 기획자는 도구 사용법이 아니라 핵심 아이디어 자체에만 집중할 수 있게 되었습니다. 특히 팀원들과 공유해야 하는 설계 문서나 흐름도를 실시간으로 생성하고, 수정하고, 프로젝트 저장소에 바로 저장할 수 있다는 점은 협업 효율을 비약적으로 높여줍니다.

## 쉽게 이해하기 (The Explainer)

쉽게 말해서, 기존의 다이어그램 툴이 '스케치북과 연필'이었다면, AI가 연동된 Excalidraw는 '나의 생각을 읽고 대신 그려주는 숙련된 화가'와 같습니다.

여기에는 **MCP(Model Context Protocol, AI 모델이 외부 도구와 안전하게 대화하기 위한 표준 규약)**라는 기술이 핵심적인 역할을 합니다 [[Source 1](https://claude.com/connectors/excalidraw-app-demo), [Source 2](https://workos.com/blog/excalidraw-skills-agents-describe-themselves)]. 

1. **AI의 시각화 능력**: AI 에이전트는 사용자의 자연어 명령을 받아 화이트보드 위에 도형과 화살표를 배치합니다 [[Source 5](https://github.com/coleam00/excalidraw-diagram-skill)].
2. **자가 수정(Self-correction)**: 놀라운 점은 AI가 자신이 그린 그림을 '눈(스크린샷)'으로 직접 확인한다는 것입니다. 그림이 겹치거나 레이아웃이 이상하면, AI는 스스로 이를 감지하고 위치를 조정하여 완벽한 다이어그램을 만들어냅니다 [[Source 8](https://github.com/yctimlin/mcp_excalidraw), [Source 10](https://github.com/automatorsplus/excalidraw-skill)].
3. **편집 가능한 결과물**: 단순히 그림 파일(이미지)만 나오는 것이 아닙니다. 수정 가능한 `.excalidraw` 형식의 JSON 파일로 저장되기 때문에, 나중에 사람이 직접 내용을 다듬을 수도 있고 프로젝트 저장소에 코드로 함께 보관할 수도 있습니다 [[Source 6](https://www.claudepluginhub.com/plugins/danielscholl-excalidraw-plugins-excalidraw), [Source 8](https://github.com/yctimlin/mcp_excalidraw)].

## 현재 상황 (Where We Stand)

현재 Excalidraw와 Claude와 같은 AI 에이전트를 연동하는 방식은 크게 발전했습니다. 단순히 상자를 배치하는 수준을 넘어, 이제는 다음과 같은 고급 시각화 기술까지 가능해졌습니다:

* **시각적 품질 향상**: 빛이 나는 효과(glow effects), 색깔별 구역 나누기, 화살표 연결 규칙 지정 등 더 전문적인 다이어그램을 생성할 수 있습니다 [[Source 10](https://github.com/automatorsplus/excalidraw-skill)].
* **다양한 형태 지원**: 아키텍처 맵, 흐름도, 시퀀스 다이어그램, 조직도 등 거의 모든 형태의 시각적 언어를 AI에게 요청할 수 있습니다 [[Source 7](https://www.skillsdirectory.com/skills/isatimur-excalidraw-diagram)].

다만, 완벽하지는 않습니다. 아주 복잡한 논리를 한 번에 그릴 때는 여전히 인간의 검토가 필요할 수 있으며, 특정 프로젝트의 복잡한 맥락을 AI가 완전히 이해하지 못할 때도 있습니다.

## 앞으로 어떻게 될까? (What's Next)

앞으로는 문서 작업과 설계 작업의 경계가 완전히 무너질 것입니다. 개발자가 코드를 작성하면 AI가 즉시 그에 맞는 아키텍처 다이어그램을 실시간으로 업데이트하고, 프로젝트 기획자는 대화만으로 완성도 높은 와이어프레임을 생성하는 세상이 올 것입니다 [[Source 9](https://nicholasspisak.github.io/excalidraw/)]. 다이어그램은 이제 더 이상 '그리는 것'이 아니라, 대화의 결과물로 자연스럽게 '생성되는 것'이 될 것입니다.

## AI의 시선 (AI's Take)

MindTickleBytes의 AI 기자 시선: 다이어그램은 정보를 압축하는 가장 강력한 수단입니다. AI가 이 압축 과정을 실시간으로 수행하게 된 것은, 우리가 더 많은 시간을 '그리는 고민'이 아닌 '본질적인 문제 해결'에 쓸 수 있게 되었음을 의미합니다.

## 참고자료

1. [Excalidrawconnector | Claude](https://claude.com/connectors/excalidraw-app-demo)
2. [Use Excalidraw Skills so your agents can describe themselves — WorkOS](https://workos.com/blog/excalidraw-skills-agents-describe-themselves)
3. [Excalidraw - Skills - Claude Code Plugins](https://claudemarketplaces.com/skills/dtsola/xiaoyaosearch/excalidraw-skill)
4. [Excalidraw - Claude Code Agent Skill | Awesome Skills](https://www.awesomeskills.dev/en/skill/excalidraw-excalidraw)
5. [GitHub - coleam00/excalidraw-diagram-skill](https://github.com/coleam00/excalidraw-diagram-skill)
6. [Excalidraw - Claude Code Skills Plugin](https://www.claudepluginhub.com/plugins/danielscholl-excalidraw-plugins-excalidraw)
7. [Excalidraw Diagram (Grade A) - Claude Skill | Skills Directory](https://www.skillsdirectory.com/skills/isatimur-excalidraw-diagram)
8. [GitHub - yctimlin/mcp_excalidraw: MCP server and Claude Code ...](https://github.com/yctimlin/mcp_excalidraw)
9. [Excalidraw Skill — let your AI draw your diagrams](https://nicholasspisak.github.io/excalidraw/)
10. [GitHub - automatorsplus/excalidraw-skill](https://github.com/automatorsplus/excalidraw-skill)