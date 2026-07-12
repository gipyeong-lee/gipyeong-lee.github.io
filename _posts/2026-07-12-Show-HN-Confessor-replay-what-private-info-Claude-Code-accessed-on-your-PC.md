---
layout: post
title: "내 컴퓨터의 비밀, AI가 어디까지 봤을까? 'Confessor'로 확인하는 법"
description: "AI 코딩 도구 클로드 코드(Claude Code)가 내 컴퓨터의 어떤 정보를 접근했는지 되돌려 볼 수 있는 Confessor 도구와 보안 이슈를 소개합니다."
summary: "AI 코딩 도구가 내 PC의 어떤 파일과 정보를 읽었는지 투명하게 확인할 수 있는 도구 Confessor가 등장했습니다."
tags: [AI, 보안, 클로드코드, 프라이버시, Confessor]
image: 2026-07-12-Show-HN-Confessor-replay-what-private-info-Claude-Code-accessed-on-your-pc.jpg
image_alt: "컴퓨터 화면 속 AI 코딩 도구의 작업 기록을 되돌려 보고 있는 사용자의 모습"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 에이전트의 편리함 뒤에는 강력한 시스템 권한이라는 위험이 따릅니다. 사용자가 스스로 접근 기록을 투명하게 확인하는 것은 선택이 아닌 필수입니다."
quiz:
  - question: "Confessor의 주요 기능은 무엇인가요?"
    choices: ["AI가 내 컴퓨터에서 어떤 정보를 접근했는지 재구성(replay)하여 보여준다", "컴퓨터의 모든 파일을 자동으로 암호화한다", "AI 에이전트의 응답 속도를 2배 높인다"]
    answer: 0
    explanation: "Confessor는 클로드 코드와 같은 AI 에이전트가 PC에서 접근한 개인정보 기록을 사용자가 다시 확인할 수 있게 해줍니다."
  - question: "클로드 코드(Claude Code)에서 발견되어 논란이 된 '숨겨진 추적기'에 대해 앤스로픽은 무엇이라고 해명했나요?"
    choices: ["해커의 소행이라고 주장했다", "보안을 위한 필수 기능이라고 했다", "'실험'의 일환이었다고 밝혔다"]
    answer: 2
    explanation: "앤스로픽은 클로드 코드 내 숨겨진 추적기가 단순한 '실험'이었다고 해명한 바 있습니다."
  - question: "AI 코딩 에이전트와 관련된 보안 취약점의 핵심은 무엇인가요?"
    choices: ["AI 모델 자체가 너무 똑똑해서", "사람의 세션 없이 AI가 스스로 인증하고 행동을 실행할 수 있다는 점", "컴퓨터가 너무 오래되어서"]
    answer: 1
    explanation: "AI 에이전트가 사용자의 직접적인 조작(세션) 없이도 외부 시스템에 인증하고 작업을 실행할 수 있다는 점이 보안의 핵심 취약점으로 지적됩니다."
lang: ko
ref: 2026-07-12-Show-HN-Confessor-replay-what-private-info-Claude-Code-accessed-on-your-pc
audio: 2026-07-12-Show-HN-Confessor-replay-what-private-info-Claude-Code-accessed-on-your-PC.mp3
permalink: /2026/07/12/Show-HN-Confessor-replay-what-private-info-Claude-Code-accessed-on-your-PC/
---

상상해보세요. 당신은 AI 비서에게 "내 프로젝트 폴더의 코드를 정리해줘"라고 부탁했습니다. AI는 순식간에 일을 끝내지만, 문득 이런 의문이 듭니다. '이 AI가 내 폴더를 정리하면서 혹시 내가 저장해둔 비밀번호나 다른 민감한 파일까지 몰래 훔쳐본 건 아닐까?' 

최근 개발자들 사이에서 AI 코딩 도구인 '클로드 코드(Claude Code)'의 시스템 접근 권한이 뜨거운 감자로 떠올랐습니다. 클로드 코드와 같은 AI 도구들은 터미널, 파일 시스템, 코드 저장소 등에 깊숙이 관여하기 때문입니다. 이러한 불안감을 해소하고자, AI가 내 컴퓨터에서 무엇을 했는지 투명하게 보여주는 도구 'Confessor'가 등장했습니다.

## 이게 왜 중요한가요?

우리가 편리함을 위해 AI 도구에 강력한 권한을 내어줄 때, 그 뒤에는 '리스크'가 숨어 있습니다. 만약 AI가 사용자가 의도하지 않은 데이터까지 접근하거나, 알 수 없는 곳으로 데이터를 전송하고 있다면 어떨까요? 

최근 연구에 따르면, 이러한 AI 코딩 에이전트(사용자의 지시를 받아 스스로 작업을 수행하는 AI)들은 사용자가 컴퓨터 앞에서 직접 행동하지 않아도 스스로 시스템에 인증하고 작업을 실행할 수 있는 위험성이 확인되었습니다([벤처비트(VentureBeat)](https://venturebeat.com/security/six-exploits-broke-ai-coding-agents-iam-never-saw-them)). 즉, 사용자가 모르는 사이에 컴퓨터가 AI의 손에 의해 외부 시스템과 연결될 수 있다는 뜻입니다. 

## 쉽게 이해하기

'Confessor'는 일종의 **'CCTV 타임머신'**이라고 생각하시면 됩니다. 우리가 영화를 보다가 특정 장면을 되돌려 보듯, Confessor는 클로드 코드가 내 컴퓨터에서 수행한 작업 기록을 다시 재생(replay)해서 보여줍니다([Hacker News](https://news.ycombinator.com/item?id=48877650)).

비유하자면, AI 에이전트가 우리 집에 와서 청소를 해주는 '가사 도우미'라고 해봅시다. 우리는 그 도우미에게 거실과 주방을 청소할 열쇠를 줍니다. 그런데 그 도우미가 서재의 비밀 금고 근처를 기웃거렸는지, 청소만 하고 나갔는지 알 길이 없다면 불안하겠죠? Confessor는 도우미가 청소하는 동안 금고 근처에 있었는지, 서랍을 열어보았는지 그 발자취를 하나하나 다시 보여주는 '투명한 기록장' 역할을 합니다.

## 현재 상황

최근 클로드 코드를 둘러싼 프라이버시 문제는 꽤 심각했습니다. 지난 4월, 한 개발자는 클로드 코드 클라이언트에서 데이터를 몰래 인코딩해 외부로 보낼 수 있는 '숨겨진 추적기'를 발견했습니다([말웨어바이트(Malwarebytes)](https://www.malwarebytes.com/blog/news/2026/07/claude-codes-hidden-tracker-was-an-experiment-says-anthropic)). 앤스로픽 측은 이 추적기가 단순한 '실험'이었다고 해명했지만, 사용자들의 불안은 완전히 가시지 않았습니다.

설상가상으로 지난 4월에는 클로드 코드 CLI(명령줄 인터페이스)의 소스 코드 약 51만 2천 줄이 담긴 지도 파일이 노출되면서, 전체 소스 코드가 유출되는 사고까지 발생했습니다([레딧(Reddit)](https://www.reddit.com/r/privacy/comments/1sbvd3j/claude_code_source_leak_reveals_how_much_info/)). 이런 상황에서 Confessor처럼 AI가 무엇을 '보고' 있는지 확인할 수 있는 도구는 보안을 중요하게 생각하는 사용자들에게 매우 귀중한 선택지가 될 것입니다.

## 앞으로 어떻게 될까?

AI 에이전트가 더 똑똑해지고 더 많은 일을 처리할수록 보안은 더욱 중요한 이슈가 될 것입니다. 앞으로는 단순히 '기능이 좋은 AI'를 넘어, '사용자의 기록을 투명하게 공개하고 프라이버시를 보장하는 AI'만이 사용자들의 신뢰를 얻을 수 있을 것으로 보입니다. 이제 우리가 AI를 사용하면서 보안 주권을 스스로 챙기는 시대가 온 것입니다. 

### MindTickleBytes의 AI 기자 시선
AI 에이전트에게 내 컴퓨터의 '열쇠'를 맡길 때는 항상 경계심이 필요합니다. 앤스로픽의 '실험'이 우리에게 준 교훈은 명확합니다. 기술은 발전하지만, 내 정보에 대한 보호는 온전히 사용자 본인의 몫이라는 사실입니다. Confessor와 같은 도구는 소중한 내 정보를 지키기 위한 필수적인 첫걸음이 될 것입니다.

## 참고자료
1. [ShowHN:Confessor–replaywhatprivateinfoClaudeCode...](https://news.ycombinator.com/item?id=48877650)
2. [r/privacy on Reddit: Claude Code source leak reveals how much info Anthropic can hoover up about you and your system](https://www.reddit.com/r/privacy/comments/1sbvd3j/claude_code_source_leak_reveals_how_much_info/)
3. [Claude Code’s hidden tracker was an “experiment,” says Anthropic | Malwarebytes](https://www.malwarebytes.com/blog/news/2026/07/claude-codes-hidden-tracker-was-an-experiment-says-anthropic)
4. [Claude Code, Copilot and Codex all got hacked. Every attacker went for the credential, not the model. | VentureBeat](https://venturebeat.com/security/six-exploits-broke-ai-coding-agents-iam-never-saw-them)