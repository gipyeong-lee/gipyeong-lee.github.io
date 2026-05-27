---
layout: post
title: "AI 코딩 비서, 어디까지 진화했을까? 클로드 코드를 완벽한 '나만의 비서'로 만드는 법"
description: "클로드 코드(Claude Code)의 스킬, 서브에이전트, MCP, 플러그인이 무엇인지 일반인의 눈높이에서 쉽게 설명합니다. AI 비서를 똑똑하게 활용하는 방법을 알아보세요."
summary: "클로드 코드의 확장 도구인 스킬, 서브에이전트, 플러그인, MCP의 개념과 올바른 활용법을 통해 나만의 강력한 맞춤형 AI 비서를 구축하는 방법을 소개합니다."
tags: [Claude, AI, CodingAssistant, AI비서, 클로드코드]
image: 2026-05-27-Claude-Code-as-a-Daily-Driver-Claudemd-Skills-Subagents-Plugins-and-MCPs.jpg
image_alt: "로봇 팔들이 여러 도구를 들고 컴퓨터 화면 앞에서 분주하게 일하는 모습을 귀엽고 친근하게 그린 일러스트"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "MindTickleBytes의 AI 기자 시선: 클로드 코드의 강력한 도구 생태계는 AI가 단순한 대화 상대를 넘어 자율적인 작업자로 진화했음을 보여줍니다. 다만 도구가 강력해질수록 무분별한 설치보다는 내게 꼭 필요한 도구만 선별하여 AI의 작업 기억 공간을 가볍게 유지하는 현명함이 미래 개발자의 핵심 역량이 될 것입니다."
quiz:
  - question: "클로드 코드 생태계에서 여러 가지 스킬, 서브에이전트, MCP 서버를 하나로 묶어 한 번에 설치할 수 있게 해주는 포장지 역할을 하는 것은 무엇인가요?"
    choices: ["스킬 (Skill)", "플러그인 (Plugin)", "클라우드 (Cloud)"]
    answer: 1
    explanation: "플러그인은 스킬, 훅, 서브에이전트, MCP 서버 등 다양한 기능들을 하나의 설치 가능한 단위로 묶어주는 패키징(포장) 계층 역할을 합니다."
  - question: "수많은 도구를 무분별하게 설치할 때 AI에게 발생할 수 있는 가장 치명적인 문제는 무엇인가요?"
    choices: ["AI의 감정이 상해서 답변을 거부하게 된다", "컴퓨터의 디스플레이 해상도가 강제로 낮아진다", "AI가 한 번에 기억하고 처리할 수 있는 '컨텍스트 윈도우'가 소진되어 정작 중요한 일을 하지 못한다"]
    answer: 2
    explanation: "전문가들은 너무 많은 MCP 서버나 스킬을 연결하면 AI의 제한된 작업 기억 공간인 '컨텍스트 윈도우'가 낭비되어 시스템 효율이 극심하게 떨어진다고 경고합니다."
  - question: "AI 비서가 외부 세상(데이터베이스나 외부 도구 등)과 소통할 수 있도록 연결해주는 통역기 역할을 하는 기술은 무엇인가요?"
    choices: ["MCP (Model Context Protocol)", "서브에이전트 (Subagent)", "지연된 도구 로딩 (Deferred tool loading)"]
    answer: 0
    explanation: "MCP는 AI가 단절된 환경을 벗어나 외부 시스템과 실시간으로 연결되고 데이터를 주고받을 수 있게 해주는 강력한 연결 규격입니다."
lang: ko
ref: 2026-05-27-Claude-Code-as-a-Daily-Driver-Claudemd-Skills-Subagents-Plugins-and-MCPs
audio: 2026-05-27-Claude-Code-as-a-Daily-Driver-Claudemd-Skills-Subagents-Plugins-and-MCPs.mp3
permalink: /2026/05/27/Claude-Code-as-a-Daily-Driver-Claudemd-Skills-Subagents-Plugins-and-MCPs/
---

상상해보세요. 이른 아침, 당신이 사무실에 출근해 텀블러에 따뜻한 커피를 채우고 자리에 앉습니다. 컴퓨터 모니터를 켜고 키보드에 손을 올린 뒤, 음성 마이크에 대고 가볍게 한마디를 던집니다. 

"오늘 주간 회의 자료 준비해주고, 어제 고객들이 불만을 제기했던 스마트폰 앱의 결제 오류 원인을 찾아서 좀 고쳐줄래?" 

놀랍게도 컴퓨터 안에서는 스스로 데이터베이스를 뒤져 오류 기록을 찾아내고, 문제가 발생한 코드를 족집게처럼 집어내어 수정한 뒤, 팀원들에게 보낼 주간 보고서까지 깔끔하게 작성하는 작업이 당신이 커피를 한 모금 마시는 동안 일사천리로 진행됩니다. 과거처럼 당신이 일일이 오류의 원인을 분석하고 복잡한 코드를 복사해서 AI에게 가져다 바칠 필요가 전혀 없습니다.

이처럼 한때 우리가 던지는 질문에 그저 텍스트 답변만 길게 늘어놓던 '백과사전' 같았던 AI가, 이제는 직접 두 팔을 걷어붙이고 도구를 사용해 여러 작업을 동시에 처리하는 능동적인 '팀원'으로 진화하고 있습니다. 최근 개발자와 IT 전문가들 사이에서 일상적인 업무 도구로 폭발적인 인기를 끌고 있는 '클로드 코드(Claude Code)'가 바로 이러한 거대한 변화의 중심에 있습니다. 오늘 우리는 이 클로드 코드를 단순한 채팅창을 넘어, 내 업무 스타일에 딱 맞는 완벽한 '나만의 맞춤형 비서'로 탈바꿈시키는 방법에 대해 깊이 있게 알아보려고 합니다. 

## 이게 왜 중요한가요? (Why It Matters)

과거의 인공지능은 분명 똑똑했지만 커다란 약점을 가지고 있었습니다. 손발이 꽁꽁 묶인 채 유리 상자 안에 갇혀 있는 천재와 같았죠. 우리가 코딩이나 복잡한 업무를 부탁하려면, AI에게 우리의 컴퓨터 폴더 구조가 어떻게 되어 있는지, 우리 팀이 어떤 규칙을 사용하고 있는지 등 수많은 배경 지식을 일일이 설명해야 했습니다. 이는 마치 매일 아침 새로 출근한 단기 아르바이트생에게 회사 현관 비밀번호부터 커피머신 사용법, 부서별 업무 매뉴얼까지 처음부터 끝까지 새로 가르쳐야 하는 것처럼 피곤한 일이었습니다. 

하지만 클로드 코드는 이 모든 한계를 부수고 세상 밖으로 나왔습니다. 클로드 코드 시스템은 상자에서 꺼내자마자 바로 강력한 성능을 발휘하지만, 이 도구의 진정한 잠재력은 사용자의 특정한 작업 흐름(Workflow)에 맞춰 개인화될 때 비로소 만개하게 됩니다 [[Claude Code Customization Guide: Rules vs Skills vs Subagents]](https://marioottmann.com/articles/claude-code-customization-guide). 마리오 오트만(Mario Ottmann)이라는 개발자는 수개월 동안 이 도구를 사용하면서, 각각의 맞춤 설정 기능들을 언제 어떻게 써야 하는지 완벽한 체계를 확립했다고 말합니다. 

쉽게 말해서, 이제 우리는 AI에게 특정 업무에 완전히 특화된 '지식 자판기'나 '전문가 자격증'을 쥐여줄 수 있게 된 것입니다. 마치 내 몸에 딱 맞게 재단된 고급 맞춤 정장처럼, 내 업무 방식에 완벽히 동기화된 AI 비서는 더 이상 엉뚱한 대답을 하며 당신의 금쪽같은 시간을 낭비하지 않습니다. 오히려 당신의 의도를 찰떡같이 파악해 가장 최적화된 결과물을 척척 만들어냅니다. 특히 하루에도 수십 번씩 반복해야 하는 번거로운 업무나, 눈이 빠지게 들여다봐야 하는 복잡한 문서 작업에서 이 맞춤형 AI 비서는 직장인들에게 구원투수와도 같은 필수적인 존재로 자리 잡고 있습니다.

## 쉽게 이해하기 (The Explainer)

그렇다면 클로드 코드의 능력을 이토록 폭발적으로 끌어올리는 마법 같은 확장 도구들은 도대체 무엇일까요? 기술의 세계는 영어가 난무하고 복잡해 보이지만, 하나씩 일상생활에 비유해 살펴보면 전혀 어렵지 않습니다.

### 1. 플러그인 (Plugins): 비서의 만능 캠핑 가방
가장 먼저 알아볼 개념은 플러그인입니다. 공식 문서에 따르면, 플러그인은 일종의 '포장(Packaging) 계층'입니다. 하나의 플러그인 안에는 스킬, 훅(Hook, 특정 상황에서 자동으로 실행되는 명령어), 서브에이전트, MCP 서버 등 AI를 돕는 여러 가지 도구들이 전부 포함되어 있으며, 이것들을 단 한 번의 조작으로 설치할 수 있게 하나로 묶어주는 역할을 합니다 [[ExtendClaudeCode-ClaudeCodeDocs]](https://code.claude.com/docs/en/features-overview). 

비유하면 이렇습니다. 당신이 이번 주말에 난생처음 캠핑을 가기로 결심했습니다. 텐트, 버너, 코펠, 랜턴, 침낭을 각각 다른 가게에서 하나하나 따로 사려면 너무나 복잡하고 시간도 오래 걸리겠죠. 이때 누군가가 "초보자용 1박 2일 오토캠핑 풀세트"라는 큼지막한 가방 하나를 건넵니다. 이 가방 안에는 캠핑에 필요한 모든 것이 완벽한 조합으로 들어있습니다. 플러그인이 바로 이 '풀세트 가방'입니다. 사용자는 복잡한 도구들을 개별적으로 고민하며 설정할 필요 없이, 필요한 목적에 맞는 플러그인 하나만 설치하면 AI 비서에게 필요한 모든 도구 상자를 단숨에 쥐여줄 수 있습니다.

### 2. 스킬 (Skills): 효율성을 극대화한 요리 레시피 카드
스킬은 AI에게 특정한 절차나 노하우를 가장 효율적으로 알려주는 휴대용 지식 도구입니다. 스킬과 플러그인은 인간의 절차적 지식을 휴대가 가능하고 '토큰(Token, AI가 텍스트를 읽고 쓰는 기본 단위)' 측면에서 매우 효율적으로 만들어주며, 업무 전반에 걸쳐 상황에 꼭 맞는 자동화를 가능하게 하는 실용적인 도약을 보여줍니다 [[Claude Skills Solve the Context Window Problem]](https://tylerfolkman.substack.com/p/the-complete-guide-to-claude-skills). 

전문가들은 스킬이 도대체 무엇인지, 서브에이전트나 MCP와는 어떻게 다른지, 팀 내에서 어떻게 관리해야 하는지 종종 혼란을 겪곤 하는데, 보통 스킬은 컴퓨터 내부에서 `SKILL.md`라는 작은 텍스트 문서 형태로 보관되고 관리됩니다 [[Claude Code Skills Complete Guide: SKILL.md, MCP, Subagents]](https://duet.so/guides/claude-code-skills-complete-guide). 

이해를 돕기 위해 이렇게 상상해보세요. 당신이 최고급 요리사(AI)를 고용했습니다. 이 요리사는 수백만 장의 레시피가 적힌 거대한 백과사전을 통째로 외우고 있지만, 당신이 "우리 집식 된장찌개 끓여줘"라고 할 때마다 머릿속의 거대한 도서관을 뒤져야 한다면 시간이 오래 걸리고 비효율적일 것입니다. 대신, 당신 집만의 특별한 '된장찌개 비법 10단계'가 적힌 작은 포스트잇(요리 카드)을 주방 냉장고에 딱 붙여두는 겁니다. 이것이 바로 스킬입니다. AI는 불필요한 생각의 낭비 없이, 오직 그 요리 카드만 보고 가장 빠르고 정확하게 당신이 원하는 방식으로 작업을 처리하게 됩니다. AI의 체력과도 같은 시스템 자원을 기가 막히게 아낄 수 있는 셈이죠.

### 3. 서브에이전트 (Subagents): 전문화된 분업 팀원들
클로드 코드는 혼자서 모든 것을 처리하지 않습니다. 특정한 개발 작업이나 업무를 아주 전문적으로 처리하기 위해 고안된 작고 똑똑한 AI 조수들이 존재하는데, 이를 서브에이전트라고 부릅니다 [[GitHub - VoltAgent/awesome-claude-code-subagents]](https://github.com/VoltAgent/awesome-claude-code-subagents). 하나의 거대한 AI 비서(메인 에이전트) 아래에 여러 명의 서브에이전트를 두어, 여러 가지 일을 동시에 병렬적으로 처리하는 '다중 에이전트 작업 흐름(Multi-agent workflows)'을 구성할 수 있습니다 [[ClaudeCodeSubagents: A 2026 Practical Guide]](https://www.tembo.io/blog/claude-code-subagents) [[Understanding Skills, Agents, Subagents, and MCP in Claude]](https://colinmcnamara.com/blog/understanding-skills-agents-and-mcp-in-claude-code).

이것은 현실 세계의 '건축 회사'와 완전히 똑같습니다. 회장님(당신)이 "새로운 아파트를 지어라"라고 지시하면, 총괄 매니저(클로드 코드 본체)가 혼자 삽을 들고 시멘트와 벽돌을 나르는 것이 아닙니다. 총괄 매니저는 즉시 '설계 전문 서브에이전트', '배관 전문 서브에이전트', '인테리어 전문 서브에이전트'를 호출합니다. 이들은 각자의 분야에만 집중하여 동시에 작업을 진행합니다. 한 명은 도면을 그리고, 다른 한 명은 자재를 주문하며, 또 다른 한 명은 일정을 조율합니다. 결과적으로 전체 작업의 속도는 상상을 초월할 정도로 빨라지고, 각 분야의 전문가들이 참여했기에 결과물의 품질 또한 완벽에 가까워집니다.

### 4. MCP (Model Context Protocol): 외부 세상과 통하는 만능 번역기
마지막으로 살펴볼 MCP는 인공지능과 외부의 다양한 시스템을 서로 연결해주는 강력한 표준 통신 규격입니다 [[Understanding Skills, Agents, Subagents, and MCP in Claude]](https://colinmcnamara.com/blog/understanding-skills-agents-and-mcp-in-claude-code). 

아무리 똑똑한 AI 비서라도 인터넷이 끊기거나 다른 컴퓨터 시스템에 접속할 권한이 없다면 그저 말만 잘하는 깡통에 불과합니다. MCP는 AI에게 외부 세상의 시스템과 소통할 수 있는 '최신형 스마트폰'이자 '만능 번역기'를 쥐여주는 것과 같습니다. 이 번역기 덕분에 클로드 코드는 회사의 이메일 시스템에 들어가 메일을 꼼꼼히 읽어오고, 사내 데이터베이스에 접속해 복잡한 매출 기록을 꺼내오고, 달력 앱에 접속해 내일의 일정을 추가하는 등 우리가 매일 쓰는 진짜 도구들을 직접 손으로 만지고 조작할 수 있게 됩니다.

## 현재 상황 (Where We Stand)

이 놀라운 확장 도구 생태계는 현재 우리가 상상하는 것 이상으로 엄청난 속도로 팽창하고 있습니다. 일반 사용자들과 전 세계의 뛰어난 개발자들이 서로의 지식을 활발하게 공유하면서 커뮤니티가 폭발적으로 성장하고 있습니다. 

단적인 예로, 커뮤니티가 자발적으로 유지 및 관리하고 있는 '에이전트 스킬(AgentSkills)'의 수는 무려 49,223개 이상에 달합니다. 이는 전 세계의 거의 모든 직업군이 자신의 업무에 꼭 맞는 AI 레시피를 하나씩은 가질 수 있는 엄청난 규모입니다. 사람들은 이 거대한 데이터베이스에서 자신의 업무에 필요한 스킬을 검색하고 언제든 손쉽게 다운로드하여 자신의 AI 비서에게 이식할 수 있습니다 [[Discover AgentSkills]](https://claude-plugins.dev/skills). 또한 서브에이전트를 모아둔 VoltAgent 저장소에는 이미 100개가 넘는 서브에이전트들이 기본 세트로 공개되어 현장에서 활발히 사용되고 있습니다 [[ClaudeCodeSubagents: A 2026 Practical Guide]](https://www.tembo.io/blog/claude-code-subagents). 

심지어 유튜브에는 단 30분 만에 클로드 코드의 고급 기능과 단축키, 효율적인 작업 방식을 완벽하게 숙지할 수 있게 도와주는 튜토리얼 영상들까지 속속 등장하며 대중화를 이끌고 있습니다 [[MasteringClaudeCodein 30 minutes - YouTube]](https://www.youtube.com/watch?v=6eBSHbLKuN0). 글로벌 개발자 플랫폼인 깃허브(GitHub)의 한 저장소에는 클로드 코드를 위한 최상급 스킬, 에이전트, 개발자 도구들이 정성스럽게 수집되어 누구나 쉽게 접근할 수 있게 열려 있습니다 [[GitHub - hesreallyhim/awesome-claude-code]](https://github.com/hesreallyhim/awesome-claude-code). 

하지만 언제나 빛이 강하면 그림자도 짙은 법입니다. 도구가 너무 다양하고 구하기 쉬워지다 보니 오히려 부작용을 호소하는 사람들도 조금씩 늘어나고 있습니다. 롭 포스터(Rob Foster)라는 전문가는 개발자들이 수십 개의 MCP 서버를 무작정 연결하고, 눈에 띄는 스킬이란 스킬은 모조리 설치하다가 결국 AI의 '컨텍스트 윈도우(Context Window)'가 텅 비어버리는 역효과를 겪고 있다고 강하게 경고합니다 [[The Claude Code Survival Guide for 2026: Skills, Agents & MCP]](https://www.linkedin.com/pulse/claude-code-survival-guide-2026-skills-agents-mcp-servers-rob-foster-lq9we). 

'컨텍스트 윈도우'란 AI가 한 번에 머릿속에 기억하고 처리할 수 있는 정보의 한계량, 즉 '작업용 화이트보드'의 전체 크기라고 생각하시면 됩니다. AI가 실제로 당신의 복잡한 질문에 답하고 코드를 짜기 위해서는 이 화이트보드에 여유 공간이 넉넉히 남아 있어야 합니다. 그런데 욕심을 부려 수십 개의 도구 사용법과 외부 시스템 매뉴얼을 화이트보드 한가운데에 빽빽하게 적어놓으면, 정작 진짜 중요한 계산을 하거나 창의적인 글을 써 내려갈 빈 공간이 전혀 남아있지 않게 되는 것이죠. 

바로 이 지점에서 단순한 메모장 파일인 `CLAUDE.md`부터, 슬래시 커맨드, 스킬, 서브에이전트 등을 각각 어떤 상황에서 적절하게 사용해야 하는지 명확히 비교하고 분석하는 안목이 그 어느 때보다 중요해졌습니다 [[Claude Code Customization: CLAUDE.md, Slash Commands, Skills]](https://alexop.dev/posts/claude-code-customization-guide-claudemd-skills-subagents/). 등산을 갈 때 무조건 많은 장비를 차고 나가는 것이 능사가 아니라, 오늘의 산세와 목적지에 꼭 맞는 가벼운 장비만을 챙기는 지혜가 진정한 고수와 초보를 가르는 핵심 기준이 되고 있습니다.

## 앞으로 어떻게 될까? (What's Next)

그렇다면 이 'AI 비서 맞춤형 최적화'의 미래는 과연 어떤 모습으로 흘러갈까요? 2026년 4월의 대규모 업데이트를 기점으로 클로드 코드 생태계는 놀라운 수준의 고급 기능들을 연이어 탑재하며 완전히 새로운 차원으로 진화하고 있습니다 [[Understanding Claude Code's Full Stack: MCP, Skills]](https://alexop.dev/posts/understanding-claude-code-full-stack/). 

앞서 언급한 '컨텍스트 윈도우'의 치명적인 낭비 문제를 해결하기 위해 **'지연된 도구 로딩(Deferred tool loading)'**이라는 아주 영리한 기술이 새롭게 도입되었습니다. 평소에는 무거운 도구 상자를 AI의 화이트보드에 미리 꺼내놓지 않고 창고에 얌전히 보관해두었다가, 시스템이 특정 도구가 정말로 필요한 순간이라고 정확히 판단할 때만 눈 깜짝할 새에 도구를 꺼내오는 진일보한 방식입니다. 이를 통해 AI는 언제나 깃털처럼 가볍고 쾌적한 두뇌 상태를 유지할 수 있게 되었습니다.

또한 에이전트들이 각자의 작업 공간을 전혀 간섭하지 않고 독립적으로 일할 수 있게 보장해주는 **'작업 트리 격리(Worktree isolation)'**, 여러 서브에이전트들이 서로 활발히 대화하며 하나의 목표를 향해 유기적으로 협력하는 **'에이전트 팀(Agent teams)'**, 그리고 사용자가 깊이 잠들어 있는 새벽 시간에 알아서 시스템을 점검하고 복잡한 코드를 깔끔하게 정리해두는 **'예약된 작업(Scheduled tasks)'** 기능까지 완벽하게 정착되었습니다 [[Understanding Claude Code's Full Stack: MCP, Skills]](https://alexop.dev/posts/understanding-claude-code-full-stack/). 

결과적으로 앞으로의 클로드 코드는 우리가 일일이 세세하게 지시하고 완료될 때까지 하염없이 기다려야 하는 수동적인 비서의 굴레에서 완전히 벗어날 것입니다. 퇴근 전 "내일 아침 출근 전까지 이 웹사이트의 전면 디자인 초안과 글로벌 번역 작업을 모두 끝내놔 줘"라고 말하고 컴퓨터를 끄면, 밤사이 여러 명의 AI 에이전트 팀이 조용히 일어나 각자의 역할을 나누고 완벽하게 작업을 마친 뒤, 다음 날 아침 당신의 모니터에 따뜻한 결과물만을 띄워주는 진정한 의미의 '자율형 동료' 시대가 이미 우리 눈앞에 성큼 다가와 있습니다.

---

## AI의 시선 (AI's Take)
MindTickleBytes의 AI 기자 시선: 클로드 코드의 방대한 확장 생태계는 인공지능이 더 이상 우리와 단순한 텍스트만 주고받는 챗봇에 머물지 않고, 물리적인 시스템의 한계를 훌쩍 뛰어넘어 능동적으로 일하는 실질적인 작업자로 거듭나는 핵심 열쇠입니다. 다만 세상의 모든 훌륭한 장비가 그렇듯, 강력한 도구일수록 현명하고 절제된 관리가 필수적입니다. 무조건 많은 스킬을 설치하여 시스템을 버겁게 만들기보다는, 내 업무 스타일에 정확히 부합하는 최정예 도구와 에이전트만을 깐깐하게 선별하여 똑똑하게 지휘하는 능력이 다가오는 미래 기술 환경에서 살아남을 우리의 새로운 필수 역량이 될 것입니다. 이러한 정교한 과정을 통해 우리는 지루한 반복 작업의 늪에서 벗어나, 진정으로 창의적이고 가치 있는 일에 오롯이 집중할 수 있는 진짜 자유를 얻게 될 것입니다.

---

## 참고자료
1. [ExtendClaudeCode-ClaudeCodeDocs](https://code.claude.com/docs/en/features-overview)
2. [GitHub - VoltAgent/awesome-claude-code-subagents: A collection of...](https://github.com/VoltAgent/awesome-claude-code-subagents)
3. [MasteringClaudeCodein 30 minutes - YouTube](https://www.youtube.com/watch?v=6eBSHbLKuN0)
4. [Discover AgentSkills](https://claude-plugins.dev/skills)
5. [ClaudeCodeSubagents: A 2026 Practical Guide – Tembo](https://www.tembo.io/blog/claude-code-subagents)
6. [The Claude Code Survival Guide for 2026: Skills, Agents & MCP ...](https://www.linkedin.com/pulse/claude-code-survival-guide-2026-skills-agents-mcp-servers-rob-foster-lq9we)
7. [Understanding Claude Code's Full Stack: MCP, Skills ...](https://alexop.dev/posts/understanding-claude-code-full-stack/)
8. [Claude Code Customization Guide: Rules vs Skills vs Subagents ...](https://marioottmann.com/articles/claude-code-customization-guide)
9. [Claude Code Skills Complete Guide: SKILL.md, MCP, Subagents ...](https://duet.so/guides/claude-code-skills-complete-guide)
10. [Claude Skills Solve the Context Window Problem (Here's How ...](https://tylerfolkman.substack.com/p/the-complete-guide-to-claude-skills)
11. [Understanding Skills, Agents, Subagents, and MCP in Claude ...](https://colinmcnamara.com/blog/understanding-skills-agents-and-mcp-in-claude-code)
12. [Claude Code Customization: CLAUDE.md, Slash Commands, Skills ...](https://alexop.dev/posts/claude-code-customization-guide-claudemd-skills-subagents/)
13. [GitHub - hesreallyhim/awesome-claude-code: A curated list of ...](https://github.com/hesreallyhim/awesome-claude-code)