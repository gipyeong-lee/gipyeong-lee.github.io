---
layout: post
title: "내 코딩 기록이 만천하에 공개된다고? 클로드 코드의 '세션 URL' 주의보"
description: "AI 코딩 도구 클로드 코드가 커밋 메시지에 자동으로 추가하는 세션 URL이 개인정보와 기밀을 노출할 수 있다는 우려와 대응법을 알아봅니다."
summary: "클로드 코드가 자동으로 삽입하는 세션 URL이 대화 내용을 외부로 유출할 위험이 있어, 많은 사용자가 이를 선택 사항(opt-in)으로 변경해달라고 요구하고 있습니다."
tags: [AI, 코딩, 클로드코드, 보안, 개인정보보호]
image: 2026-08-30-Claude-Session-URL-appended-to-commit-messages-and-PR-descriptions-by-default.jpg
image_alt: "컴퓨터 화면 속 코드 커밋 기록과 그 옆에 위험 경고 표시가 떠 있는 모습"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "개발 과정의 투명성은 좋지만, AI와의 사적인 대화가 코드와 함께 박제되는 것은 심각한 보안 문제입니다. 기능의 편의성보다 정보 보호가 우선입니다."
quiz:
  - question: "클로드 코드가 커밋 메시지에 추가하는 '세션 URL'이 왜 문제가 되나요?"
    choices: ["코드를 느리게 만들어서", "대화 기록 전체를 노출할 수 있어서", "저장 공간을 많이 차지해서"]
    answer: 1
    explanation: "해당 URL을 클릭하면 AI와의 대화 내용 전체가 공개되어, 민감한 정보가 외부로 유출될 위험이 있기 때문입니다."
  - question: "기존의 'attribution.commit' 설정으로 세션 URL을 끌 수 있었나요?"
    choices: ["예, 완벽하게 통제 가능했습니다", "아니오, 세션 URL은 통제 대상이 아니었습니다", "부분적으로 가능했습니다"]
    answer: 1
    explanation: "초기에는 'attribution.commit'이나 'attribution.pr' 설정으로도 세션 URL 삽입을 제어할 수 없었다는 점이 많은 사용자의 지적을 받았습니다."
  - question: "개발자 커뮤니티가 Anthropic에 요구하는 올바른 개선 방향은 무엇인가요?"
    choices: ["세션 URL 기능을 완전히 삭제", "기본값을 '사용 안 함(opt-in)'으로 변경", "더 긴 URL을 제공"]
    answer: 1
    explanation: "사용자가 필요할 때만 선택적으로 활성화할 수 있도록 기본값을 '옵트인(opt-in)' 방식으로 변경할 것을 지속적으로 요구하고 있습니다."
lang: ko
ref: 2026-08-30-Claude-Session-URL-appended-to-commit-messages-and-PR-descriptions-by-default
audio: 2026-08-30-Claude-Session-URL-appended-to-commit-messages-and-PR-descriptions-by-default.mp3
permalink: /2026/08/30/Claude-Session-URL-appended-to-commit-messages-and-PR-descriptions-by-default/
---

상상해보세요. 오늘 아침, 아주 비밀스러운 프로젝트를 위해 AI 코딩 비서와 머리를 맞대고 코드를 작성했습니다. "이 부분은 회사 내부 기밀이니까 절대 밖으로 새 나가면 안 돼"라고 당부도 했죠. 그런데 며칠 뒤, 누군가 저장소(Repository)에 들어왔다가, 무심코 코드 옆에 붙어 있는 링크를 클릭해버린다면 어떻게 될까요? 그 링크를 통해 당신과 AI가 나눈 모든 대화가 상대방의 화면에 펼쳐지게 됩니다.

최근 AI 코딩 도구인 '클로드 코드(Claude Code)'를 사용하는 개발자들 사이에서 이런 우려가 커지고 있습니다. 개발의 편의를 위해 도입된 기능이 뜻하지 않은 보안 사고의 통로가 되고 있다는 지적입니다.

### 이게 왜 중요한가요?

대부분의 개발자는 자신의 코드를 깃(Git)과 같은 저장소 시스템에 기록합니다. 이때 클로드 코드는 코드를 작성한 뒤 자동으로 커밋(Commit, 코드 변경 기록 저장) 메시지와 풀 리퀘스트(PR, 코드 합치기 요청) 본문에 'Claude-Session'이라는 문구를 담은 URL을 추가합니다 [Source 1, Source 5].

겉보기에는 "내가 이 코드를 클로드 코드로 작성했다"는 출처 표기처럼 보입니다. 하지만 이 링크를 클릭하면 해당 코드가 만들어질 당시의 **전체 대화 기록**이 그대로 노출됩니다 [Source 5]. 여기에는 단순히 코드뿐만 아니라, 비공개 프로젝트의 기획 내용, 보안 관련 논의, 혹은 회사 내부의 비밀스러운 대화가 포함될 수 있습니다. 만약 이 저장소가 외부에 공개된 곳이라면, 당신의 모든 생각과 개발 과정이 만천하에 공개되는 셈입니다 [Source 5].

### 쉽게 이해하기: '연습장'과 '포스트잇'

이 문제를 이해하기 쉽게 비유해 보겠습니다. 우리가 작성한 코드가 '최종 결과물'이라면, AI와 나눈 대화는 그 결과물을 만들기 위해 연습장에 적었던 '모든 낙서와 고민의 흔적'입니다.

지금 클로드 코드는 결과물을 제출할 때, 연습장에 썼던 모든 내용을 포스트잇에 적어 결과물과 함께 붙여놓고 있는 상황입니다 [Source 6, Source 7]. 문제는 이 포스트잇이 내가 누구와 어떤 기밀을 나눴는지까지 적나라하게 보여준다는 것이죠. [Source 5]

과거 개발자들이 쓰던 'attribution.commit'이나 'attribution.pr' 설정값은 단순히 "이 코드는 AI가 썼습니다"라고 밝히는 용도였습니다. 하지만 이 설정들은 새롭게 생긴 '세션 URL'이라는 강력한 데이터 노출 기능까지 제어하지는 못했습니다 [Source 3].

### 왜 사용자들이 불안해할까요?

현재 많은 개발자가 이 문제에 대해 강한 불만을 제기하고 있습니다 [Source 1, Source 9]. 특히 클로드 코드를 클라우드 환경에서 사용하는 경우, 개발자가 로컬 컴퓨터에서 깃 설정을 바꾸더라도 서버에서 생성되는 커밋 메시지를 막을 방법이 없어 더욱 곤란한 상황입니다 [Source 2].

이에 대해 Anthropic(클로드 개발사) 측에 수많은 개선 요청이 쏟아지고 있습니다 [Source 1, Source 11]. 핵심 요구사항은 **"기본적으로 항상 넣지 말고, 사용자가 원할 때만 선택적으로 넣게 해달라(opt-in)"**는 것입니다 [Source 1, Source 8].

### 앞으로 어떻게 될까?

기술은 우리의 생산성을 높여주지만, 그 과정에서 '데이터의 주권'을 잃어버려선 안 됩니다. 앞으로 이 기능은 많은 사용자의 요청에 따라 강제적인 기본값에서 사용자가 직접 제어할 수 있는 형태로 개선될 가능성이 높습니다 [Source 8, Source 11].

지금 클로드 코드를 사용하고 계신다면, 커밋이나 풀 리퀘스트를 생성할 때 자신의 기록이 어디까지 노출되고 있는지 꼭 확인해보시기 바랍니다. 무심코 공유한 링크 하나가 당신의 소중한 아이디어와 기밀을 모두 공개로 전환해버릴 수 있습니다 [Source 5].

### MindTickleBytes의 AI 기자 시선

"편리함은 보안이라는 울타리 안에서만 가치가 있습니다. AI 도구가 개발자의 파트너가 되려면, 무엇보다 사용자의 '기밀 유지'를 가장 기본적인 신뢰 지표로 삼아야 할 것입니다. 도구의 기본 설계가 사용자에게 정보를 보호할 권리를 우선적으로 보장할 때, 진정한 생산성 혁신이 이루어질 수 있습니다."

## 참고자료

1. [FEATURE] Session URL appended to commit messages and PR descriptions by default — should be opt-in · Issue #66504 · anthropics/claude-code (https://github.com/anthropics/claude-code/issues/66504)
2. attribution setting does not control session URL in commit messages · Issue #41873 · anthropics/claude-code (https://github.com/anthropics/claude-code/issues/41873)
3. Is the 'Claude-Session' URL That Claude Code Embeds in Commits Still in Your Repository? (https://zenn.dev/khasegawa/articles/985d970d6cc4a2?locale=en)
4. Stop Claude Code Session URLs From Landing in Your Public Git History (https://outofcontext.dev/blog/claude-code-session-url-attribution/)
5. [BUG] `attribution.sessionUrl` should default to `false` (opt-in) · Issue #76899 · anthropics/claude-code (https://github.com/anthropics/claude-code/issues/76899)
6. [Bug] Model leaks private session URL into git commits and PR bodies via Claude-Session trailer · Issue #72557 · anthropics/claude-code (https://github.com/anthropics/claude-code/issues/72557)
7. Claude Code Co-Author Commits: What It Is, How to Disable | explainx.ai Blog | explainx.ai (https://www.explainx.ai/blog/claude-code-commit-co-author-attribution-disable-guide-2026)
8. claude-code -(How to fix) Fix [FEATURE]SessionURLappended... (https://www.stepcodex.com/en/issue/feature-session-url-appended-to-commit)
9. ClaudeSessionURLappendedtocommitmessagesandPR... (https://news.ycombinator.com/item?id=49498201)
10. ClaudeSessionKey - Chrome Web Store (https://chromewebstore.google.com/detail/claude-session-key/ppofmhjkjfinjpidlidepeonimpjmadj)
11. How to fixClaudeCode hooks not firing or failing · 7752 Issues & Trend (https://claudeissues.com/topic/hooks-and-automation)
12. ClaudePrevious Response Still Running: Fix It Fast (https://www.digitbin.com/fix-claude-previous-response-still-running/)
13. ClaudeSwitched Models Mid-Conversation? | UsingClaude (https://usingclaude.com/en/guides/troubleshooting/claude-flagged-model-switching)
14. Claude (https://claude.com/)
15. FixClaudeCode "Please run /login" API Error 401 - SmartScope (https://smartscope.blog/en/generative-ai/claude/claude-code-401-auth-error-fix/)