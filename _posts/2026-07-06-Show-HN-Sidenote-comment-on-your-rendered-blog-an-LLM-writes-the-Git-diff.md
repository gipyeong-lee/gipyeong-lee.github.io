---
layout: post
title: "내 블로그에 구글 문서처럼 댓글을? AI가 직접 코드를 수정해주는 '사이드노트(Sidenote)'"
description: "개발자의 블로그나 문서를 구글 문서처럼 손쉽게 수정 제안하고, AI가 알아서 코드 변경 사항(Git diff)까지 작성해주는 도구 사이드노트에 대해 알아봅니다."
summary: "사이드노트는 블로그 포스트를 읽다가 댓글을 달면 AI가 이를 분석해 Git 코드 변경 사항으로 자동 변환해주는 혁신적인 협업 도구입니다."
tags: [AI, 블로그, Git, 협업, 생산성]
image: 2026-07-06-Show-HN-Sidenote-comment-on-your-rendered-blog-an-LLM-writes-the-Git-diff.jpg
image_alt: "블로그 포스트 화면 위에 구글 문서 스타일의 댓글창이 떠 있고, AI가 코드 변경 사항을 작성하는 모습을 형상화한 이미지."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "복잡한 코딩 지식 없이도 문서의 의도만 전달하면 AI가 기술적 처리를 대신해주는 '의도 중심(intent-driven)' 워크플로우의 좋은 예시입니다."
quiz:
  - question: "사이드노트(Sidenote)를 사용하는 주요 경험은 무엇과 가장 비슷한가요?"
    choices: ["이메일 보내기", "구글 문서(Google Docs)에서 문서 검토하기", "터미널에서 코드 컴파일하기"]
    answer: 1
    explanation: "사이드노트는 렌더링된 마크다운 사이트에서 구글 문서처럼 직접 구절을 선택하고 댓글을 달아 검토할 수 있는 환경을 제공합니다."
  - question: "사용자가 사이드노트에서 댓글을 달았을 때 AI 에이전트가 최종적으로 수행하는 작업은 무엇인가요?"
    choices: ["자동으로 블로그에 게시하기", "Git diff(코드 변경 사항) 작성하기", "댓글에 답변 달기"]
    answer: 1
    explanation: "사용자가 남긴 댓글 내용을 바탕으로 AI 에이전트(Claude 또는 Codex)가 깔끔한 Git diff를 생성하여 코드 변경을 해결합니다."
  - question: "사이드노트의 실행 환경에 대한 설명으로 옳은 것은?"
    choices: ["별도의 서버 설치가 필수이다", "로컬 우선(Local-first)의 웹 브라우저 기반 도구이다", "모바일 앱으로만 가능하다"]
    answer: 1
    explanation: "사이드노트는 브라우저에서 바로 동작하는 로컬 우선(Local-first) 애플리케이션입니다."
lang: ko
ref: 2026-07-06-Show-HN-Sidenote-comment-on-your-rendered-blog-an-LLM-writes-the-Git-diff
audio: 2026-07-06-Show-HN-Sidenote-comment-on-your-rendered-blog-an-LLM-writes-the-Git-diff.mp3
permalink: /2026/07/06/Show-HN-Sidenote-comment-on-your-rendered-blog-an-LLM-writes-the-Git-diff/
---

상상해보세요. 여러분이 정성스럽게 작성한 블로그나 기술 문서 사이트를 누군가 읽다가, "여기 문장이 조금 어색한데 이렇게 바꾸면 어떨까요?"라며 마치 구글 문서(Google Docs)에 댓글을 달듯 손쉽게 의견을 남깁니다. 그런데 놀라운 점은, 그 댓글을 읽은 인공지능(AI)이 단순히 답변만 하는 게 아니라, 여러분의 블로그 원본 소스 코드를 직접 수정할 수 있도록 '코드 변경 제안서(Git diff, 코드의 변경된 내용만을 표시하는 기술적 방법)'까지 완벽하게 작성해준다면 어떨까요?

이런 마법 같은 경험을 가능하게 해주는 도구가 등장했습니다. 바로 '사이드노트(Sidenote)'입니다. 

### 이게 왜 중요한가요?

개발자나 기술 블로거들에게 문서 협업은 늘 쉽지 않은 숙제입니다. 보통 누군가 오타나 표현 수정을 제안하려면, 블로그 소스 코드가 있는 저장소(Repository, 코드가 저장된 온라인 공간)에 접속해서 수정 제안(Pull Request, 코드 변경 사항을 반영해달라고 요청하는 것)을 보내야 합니다. 이 과정은 기술적인 지식이 없는 일반 독자에게는 너무나 높고 복잡한 장벽입니다.

사이드노트는 이 장벽을 허뭅니다. [사이드노트(Sidenote)](https://github.com/bharadwaj-pendyala/sidenote)는 기술적인 지식이 없는 사람도, 마치 [구글 문서(Google Docs)](https://github.com/bharadwaj-pendyala/sidenote)를 사용하는 것처럼 자연스럽게 문서를 검토하고 제안할 수 있게 해줍니다. 즉, '생산성'과 '협업의 문턱'이라는 두 마리 토끼를 모두 잡은 셈입니다. 

### 쉽게 이해하기: 사이드노트의 원리

사이드노트가 어떻게 이런 일을 하는지 쉽게 비유해볼까요? 여러분의 블로그 포스트를 '완성된 요리'라고 생각해보세요. 

1. **읽기(렌더링):** 독자는 완성된 요리를 식탁에서 먹는 것처럼 편안하게 블로그 화면을 읽습니다. [출처: GitHub - bharadwaj-pendyala/sidenote](https://github.com/bharadwaj-pendyala/sidenote)
2. **댓글(검토):** 독자가 "이 부분에 소금이 조금 더 필요하겠어요"라고 요리에 댓글을 답니다. 사이드노트에서는 여러분이 [렌더링된 마크다운 사이트](https://github.com/bharadwaj-pendyala/sidenote)에서 특정 구절을 선택하고 의견을 남기는 것과 같습니다.
3. **AI 해결사(Git diff 작성):** 이때 요리사(블로그 주인) 대신 AI 에이전트(Claude 또는 Codex 등)가 등장합니다. [출처: GitHub - bharadwaj-pendyala/sidenote](https://github.com/bharadwaj-pendyala/sidenote) AI는 독자의 의견을 듣고, 어떤 재료(코드)를 어떻게 추가하거나 뺄지 계산하여 '레시피 수정안(Git diff)'을 뚝딱 만들어냅니다.

이렇게 [사이드노트(Sidenote)](https://news.ycombinator.com/item?id=48797739)는 사용자가 블로그 포스트의 특정 부분을 선택하고 댓글을 남기면, AI가 그 의도를 파악해 깔끔한 Git diff를 생성해주는 구조로 작동합니다. [출처: GitHub - bharadwaj-pendyala/sidenote](https://github.com/bharadwaj-pendyala/sidenote)

### 현재 상황: 어디까지 할 수 있나요?

사이드노트는 현재 [로컬 우선(Local-first)의 웹 브라우저 기반](https://github.com/bharadwaj-pendyala/sidenote)으로 작동하도록 설계되었습니다. 즉, 복잡한 서버 설정 없이도 웹 브라우저 환경에서 바로 검토를 시작할 수 있다는 점이 큰 장점입니다. 

특히 개발자들 사이에서 큰 관심을 받고 있는데, [Hacker News와 같은 기술 커뮤니티](https://news.ycombinator.com/item?id=48797739)에서도 이 도구가 가진 효율성에 주목하고 있습니다. 다만, 사이드노트는 기본적으로 문서 리뷰와 AI를 통한 코드 수정 제안에 특화되어 있으며, 현재는 주로 마크다운(Markdown, 웹 문서를 작성하는 간편한 언어) 형태의 블로그 포스트 환경에서 [구글 문서와 같은 검토 경험](https://github.com/bharadwaj-pendyala/sidenote)을 제공하는 데 최적화되어 있습니다.

### 앞으로 어떻게 될까?

앞으로 사이드노트와 같은 도구들이 더 보편화된다면, 블로그 관리나 오픈소스 프로젝트 협업의 풍경은 완전히 바뀔 것입니다. 코딩을 전혀 모르는 마케터나 에디터도 개발자의 도움 없이 스스로 문서의 오타를 수정하고, AI가 생성한 [Git diff](https://github.com/bharadwaj-pendyala/sidenote)를 통해 변경 사항을 승인만 하면 되는 세상이 올지도 모릅니다. 

기술의 발전이 우리에게 더 친절하고 매끄러운 협업 도구를 선물하고 있습니다. 여러분도 여러분의 블로그에 사이드노트를 적용해 독자들의 똑똑한 피드백을 받아보는 건 어떨까요?

---
**MindTickleBytes의 AI 기자 시선:**
사이드노트는 복잡한 코딩 지식 없이도 문서의 의도만 전달하면 AI가 기술적 처리를 대신해주는 '의도 중심(intent-driven)' 워크플로우의 좋은 예시입니다. 인간의 언어를 코드로 변환하는 AI의 능력이 이제 협업의 방식을 얼마나 더 매끄럽게 바꿀 수 있을지 기대됩니다.

## 참고자료

1. [GitHub - bharadwaj-pendyala/sidenote](https://github.com/bharadwaj-pendyala/sidenote)
2. [Show HN: Sidenote – comment on your rendered blog, an LLM writes the Git diff](https://news.ycombinator.com/item?id=48797739)
3. [Show | Hacker News](https://nhn.yuu.is/show)
4. [bharadwaj-pendyala/sidenote — GitHub trending stats](https://trendshift.io/repositories/73998)
5. [Show HN: LLM Prompt Diff – Semantic Git-Style Diffing for AI](https://news.ycombinator.com/item?id=44400071)
6. [What Is Sidenote? Human Review for AI-Generated Documents](https://www.sidenote.ink/blog/what-is-sidenote)
7. [analyze-changes: AI-Powered Git Diff Analyzer with Local](https://gist.github.com/udiedrichsen/979ae7ee3aaaae00cf3e15046ee5bba0)
8. [ShowHN:Sidenote–commentonyourrenderedblog,anLLM...](https://modernorange.io/item/48797739)
9. [How to Use a LocalLLMwithin Cursor - YouTube](https://www.youtube.com/watch?v=Ssh3m_8RPlA)
10. [How do I 'gitdiff' on a certain directory? - Stack Overflow](https://stackoverflow.com/questions/8382019/how-do-i-git-diff-on-a-certain-directory)
11. [Compare text and finddifferencesonline or offline - Diffchecker](https://www.diffchecker.com/)
12. [GitdiffCommand – How to Compare Changes in Your Code](https://www.freecodecamp.org/news/git-diff-command/)
13. [How can I see 'gitdiff' on the Visual Studio Code... - Stack Overflow](https://stackoverflow.com/questions/51316233/how-can-i-see-git-diff-on-the-visual-studio-code-side-by-side-file)