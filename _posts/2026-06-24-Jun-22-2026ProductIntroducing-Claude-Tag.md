---
layout: post
title: "동료 AI '클로드 태그(Claude Tag)'와 함께 일하는 법? 슬랙(Slack)에서 바로 호출하세요"
description: "Anthropic이 새롭게 선보인 슬랙 통합 AI 에이전트 '클로드 태그'가 무엇인지, 어떻게 업무 효율을 높여주는지 쉽게 설명해 드립니다."
summary: "Anthropic이 슬랙에서 대화하듯 업무를 맡길 수 있는 AI 에이전트 '클로드 태그'를 출시하여, 기업용 협업 툴의 새로운 변화를 예고했습니다."
tags: [AI, 협업, 클로드, 슬랙, 업무자동화]
image: 2026-06-24-Jun-22-2026ProductIntroducing-Claude-Tag.jpg
image_alt: "슬랙 메신저 화면 위에 떠 있는 클로드 로고와 AI 에이전트가 업무를 처리하는 모습을 보여주는 그래픽"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "기업 협업 툴에 '에이전트'가 내재화되는 것은 단순한 편리함을 넘어, AI가 팀의 일원으로 정착하는 중요한 변곡점입니다."
quiz:
  - question: "클로드 태그를 슬랙에서 호출하는 방법은 무엇인가요?"
    choices: ["@ClaudeTag를 입력한다", "@CLAUDE.md를 입력한다", "/call-claude 명령어를 사용한다"]
    answer: 1
    explanation: "클로드 태그는 슬랙 채널에서 @CLAUDE.md를 태그하여 호출할 수 있습니다."
  - question: "현재 클로드 태그를 사용할 수 있는 대상은 누구인가요?"
    choices: ["모든 개인 사용자", "Claude Enterprise 및 Team 고객", "공개 베타 신청자"]
    answer: 1
    explanation: "클로드 태그는 현재 Claude Enterprise 및 Team 고객을 대상으로 연구용 프리뷰 버전이 제공되고 있습니다."
  - question: "Anthropic 팀 내부에서 클로드 태그의 활약상은 어느 정도인가요?"
    choices: ["전체 코드의 10% 작성", "전체 코드의 65% 작성", "코드는 작성하지 않음"]
    answer: 1
    explanation: "Anthropic 프로덕트 팀은 전체 코드의 65%를 클로드 태그가 작성하게 하고 있습니다."
lang: ko
ref: 2026-06-24-Jun-22-2026ProductIntroducing-Claude-Tag
audio: 2026-06-24-Jun-22-2026ProductIntroducing-Claude-Tag.mp3
permalink: /2026/06/24/Jun-22-2026ProductIntroducing-Claude-Tag/
---

상상해보세요. 바쁜 업무 시간, 메신저를 통해 팀원들에게 회의 자료를 정리해달라고 요청하거나, 급하게 코드 리뷰를 부탁해야 하는 상황을요. 그런데 만약 여러분의 메신저 대화방에 사람처럼 업무를 척척 도와주는 ‘AI 팀원’이 함께 있다면 어떨까요? 최근 앤스로픽(Anthropic)이 이 상상을 현실로 만들어줄 새로운 도구를 선보였습니다. 바로 우리가 매일 쓰는 협업 메신저, 슬랙(Slack) 안에서 활동하는 AI 에이전트 ‘클로드 태그(Claude Tag)’입니다.

### 이게 왜 중요한가요?

우리는 매일 수많은 메신저 알림 속에서 메일을 확인하고, 복잡한 코드를 수정하며, 흩어진 매출 수치를 찾아 헤맵니다. 이런 단순하고 반복적인 업무들은 정작 우리가 집중해야 할 기획이나 창의적인 고민을 할 시간을 앗아가곤 하죠. '클로드 태그'는 바로 이런 지점에서 중요합니다. 단순히 질문에 답하는 챗봇을 넘어, 우리가 이미 일하고 있는 공간에서 직접 '행동'하는 비서가 생기는 것이기 때문입니다. [출처: Anthropic releases Claude Tag, a virtual employee that works within slack | Fortune](https://fortune.com/2026/06/23/anthropic-claude-tag-virtual-employee-tool-slack/)

### 쉽게 이해하기: 슬랙 속 똑똑한 신입 사원

클로드 태그는 쉽게 말해 '슬랙 안에서 일하는 똑똑한 신입 사원'이라고 비유할 수 있습니다. 

보통의 AI가 '질문하면 답변하는' 백과사전 같은 존재라면, 클로드 태그는 여러분의 팀원으로 슬랙 채널에 직접 초대받을 수 있습니다. 회의 중에 "지난달 매출 수치 정리해줘"라고 @CLAUDE.md를 태그해 요청하면, 이 친구는 관련 데이터를 분석해 깔끔한 결과물로 답을 내놓습니다. [출처: Anthropic introduced “Claude Tag,” a new AI agent Slack integration. | The Verge](https://www.theverge.com/ai-artificial-intelligence/954921/anthropic-introduced-claude-tag-a-new-ai-agent-slack-integration)

더 구체적인 비유를 들어볼까요? 여러분이 사진 앱에서 필터를 적용할 때, 사용자가 직접 수치를 조정하지 않아도 AI가 알아서 색감을 최적화해주죠? 클로드 태그도 마찬가지입니다. 개발자라면 코드를 수정하고 병합(Merge, 여러 코드 파일을 하나로 합치는 작업)해달라고 요청할 수 있고, 기획자라면 복잡한 데이터를 정리해달라고 부탁할 수 있습니다. 즉, 슬랙이라는 익숙한 환경 위에서 AI가 알아서 업무를 처리해주는 것입니다. [출처: Anthropic introduced “Claude Tag,” a new AI agent Slack integration. | The Verge](https://www.theverge.com/ai-artificial-intelligence/954921/anthropic-introduced-claude-tag-a-new-ai-agent-slack-integration)

### 현재 상황

현재 클로드 태그는 '연구용 프리뷰(Research Preview, 정식 출시 전 사용성을 검증하는 초기 단계)' 버전으로 제공되고 있습니다. 모든 사용자에게 공개된 것은 아니며, Claude Enterprise(기업용) 및 Claude Team 고객들이 먼저 사용해볼 수 있습니다. [출처: Sorry, Slackbot. Claude is taking your job - Engadget](https://www.engadget.com/2199619/anthropic-announces-claude-tag-for-slack/) [출처: Anthropic’s Claude Tag is learning your company, one Slack message at a time | TechCrunch](https://techcrunch.com/2026/06/23/anthropics-claude-tag-is-learning-your-company-one-slack-message-at-a-time/)

흥미로운 점은 앤스로픽 내부에서 이미 이 도구를 적극적으로 활용하고 있다는 사실입니다. 앤스로픽의 프로덕트 팀은 자신들이 만드는 전체 코드의 65%를 이 클로드 태그에게 맡기고 있다고 합니다. 심지어 클로드 태그를 만드는 과정 자체도 클로드 태그 스스로의 도움을 받아 진행했을 정도죠. [출처: Anthropic launches Claude Tag enterprise collaborative tool for agentic workflows - 9to5Mac](https://9to5mac.com/2026/06/23/anthropic-launches-cla-collaborative-tool-for-agentic-workflows/)

### 앞으로 어떻게 될까?

앤스로픽은 앞으로 이 '상시 가동(Always-on)' AI 팀원의 사용 범위를 점차 넓혀갈 예정입니다. [출처: Sorry, Slackbot. Claude is taking your job - Engadget](https://www.engadget.com/2199619/anthropic-announces-claude-tag-for-slack/) 앞으로 더 많은 기업들이 이를 도입하게 된다면, 슬랙 메신저 창은 단순한 소통 공간을 넘어 AI와 사람이 실시간으로 협업하며 업무를 완수하는 '디지털 사무실'로 진화할 것입니다. 매번 웹사이트에 접속해 질문하고 답변을 복사해 붙여넣던 번거로움이 사라질 날이 머지않았습니다.

---

**MindTickleBytes의 AI 기자 시선**
메신저라는 가장 일상적인 공간에 '직접 일하는 AI'가 들어왔다는 점이 핵심입니다. AI가 단순한 도구를 넘어 우리 팀의 일원인 '동료'의 영역으로 한 발짝 더 들어온 셈이죠. 이제 AI는 우리가 시키는 것을 하는 것을 넘어, 팀의 흐름을 이해하고 함께 움직이는 존재가 되어가고 있습니다.

## 참고자료
1. [Anthropic releases Claude Tag, a virtual employee that works within slack | Fortune](https://fortune.com/2026/06/23/anthropic-claude-tag-virtual-employee-tool-slack/)
2. [Anthropic introduced “Claude Tag,” a new AI agent Slack integration. | The Verge](https://www.theverge.com/ai-artificial-intelligence/954921/anthropic-introduced-claude-tag-a-new-ai-agent-slack-integration)
3. [Anthropic’s Claude Tag is learning your company, one Slack message at a time | TechCrunch](https://techcrunch.com/2026/06/23/anthropics-claude-tag-is-learning-your-company-one-slack-message-at-a-time/)
4. [Anthropic’s Claude Tag is learning your company, one Slack message at a time - RocketNews](https://rocketnews.com/2026/06/anthropics-claude-tag-is-learning-your-company-one-slack-message-at-a-time/)
5. [Anthropic launches Claude Tag enterprise collaborative tool for agentic workflows - 9to5Mac](https://9to5mac.com/2026/06/23/anthropic-launches-claude-tag-enterprise-collaborative-tool-for-agentic-workflows/)
6. [Sorry, Slackbot. Claude is taking your job - Engadget](https://www.engadget.com/2199619/anthropic-announces-claude-tag-for-slack/)
7. [Anthropic Release Notes - June 2026 Latest Updates - Releasebot](https://releasebot.io/updates/anthropic)