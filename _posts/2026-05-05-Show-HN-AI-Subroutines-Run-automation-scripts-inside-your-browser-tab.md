---
layout: post
title: "매번 돈 내고 AI에게 시키실 건가요? '한 번만 가르치면' 공짜로 무한 반복하는 'AI 서브루틴' 등장"
description: "AI가 매번 생각하며 행동하는 대신, 사람이 한 번 수행한 동작을 '서브루틴'으로 저장해 비용과 지연 시간 없이 브라우저 내에서 직접 실행하는 rtrvr.ai의 새로운 자동화 기술을 소개합니다."
summary: "사람의 브라우저 작업을 딱 한 번만 녹화하면, 이후엔 AI 호출 비용(토큰)이나 기다림 없이 무한히 반복해주는 똑똑한 매크로 'AI 서브루틴'이 공개되었습니다."
tags: [AI, 자동화, 브라우저, rtrvr, 웹에이전트]
image: 2026-05-05-Show-HN-AI-Subroutines-Run-automation-scripts-inside-your-browser-tab.jpg
image_alt: "브라우저 탭 안에서 복잡한 작업들이 자동으로 돌아가는 모습을 시각화한 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "생각하는 AI보다 '잘 배운' 스크립트가 훨씬 경제적이고 정확할 때가 있습니다. AI 서브루틴은 바로 그 지점을 정확히 파고들었습니다. 모든 것을 AI의 지능에 맡기기보다, 지능으로 만든 '최적의 경로'를 기술로 고정하는 것이 진정한 효율성입니다."
quiz:
  - question: "AI 서브루틴(AI Subroutines)의 가장 큰 특징은 무엇인가요?"
    choices: ["매번 실행할 때마다 비싼 AI 토큰 비용이 든다.", "작업을 한 번 녹화하면 추가 비용이나 지연 없이 무한 반복한다.", "사람의 개입이 전혀 없이 AI가 스스로 모든 것을 판단한다."]
    answer: 1
    explanation: "AI 서브루틴은 한 번 녹화된 작업을 결정론적 스크립트로 변환하여 실행하기 때문에 추가 토큰 비용이나 AI 추론 지연이 없습니다."
  - question: "AI 서브루틴이 기존 AI 에이전트보다 나은 점은 무엇인가요?"
    choices: ["보안 인증(로그인 상태 등)을 자동으로 활용한다.", "복잡한 논리적 추론을 매 순간 수행한다.", "항상 새로운 방식으로 일을 처리한다."]
    answer: 0
    explanation: "브라우저 탭 내부에서 실행되므로 브라우저가 이미 가진 인증 정보와 보안 메커니즘을 그대로 사용할 수 있다는 장점이 있습니다."
  - question: "AI 서브루틴을 만든 회사는 어디인가요?"
    choices: ["OpenAI", "rtrvr.ai", "Google"]
    answer: 1
    explanation: "이 기술은 분산형 AI 인프라 전문 기업인 rtrvr.ai에서 개발하여 발표했습니다."
lang: ko
ref: 2026-05-05-Show-HN-AI-Subroutines-Run-automation-scripts-inside-your-browser-tab
audio: 2026-05-05-Show-HN-AI-Subroutines-Run-automation-scripts-inside-your-browser-tab.mp3
permalink: /2026/05/05/Show-HN-AI-Subroutines-Run-automation-scripts-inside-your-browser-tab/
---

상상해보세요. 여러분이 매일 아침 출근하자마자 링크드인에서 100명에게 일촌 신청을 보내거나, 고객 관리 시스템(CRM)에 수십 명의 정보를 일일이 입력해야 한다고 합시다. 

요즘 유행하는 **'AI 에이전트(AI Agent, 사람이 내린 목표를 위해 스스로 판단하고 행동하는 AI)'**를 쓰면 이 일을 대신 해주긴 합니다. 하지만 큰 고민거리가 하나 있죠. AI가 클릭 한 번을 할 때마다, 문장 한 줄을 쓸 때마다 비싼 **'토큰(Token, AI가 글자나 정보를 처리하는 기본 단위)'** 비용이 꼬박꼬박 빠져나간다는 점입니다. 게다가 AI가 "음... 다음엔 어떤 버튼을 눌러야 하지?"라고 고민하며 머리를 굴리는(추론) 시간 동안, 여러분은 화면 앞에서 모래시계만 멍하니 쳐다보고 있어야 합니다. 

이런 비효율을 해결하기 위해, 딱 한 번만 가르쳐주면 마치 비디오를 재생하듯 작업을 완벽하고 '공짜'로 수행하는 기술이 등장했습니다. 바로 **'AI 서브루틴(AI Subroutines)'**입니다. [Show HN: AI Subroutines – Run automation scripts inside your browser tab](https://news.ycombinator.com/item?id=47810533)

## 이게 왜 중요한가요?

지금까지 우리가 접해온 '웹 에이전트'들은 문제의 절반만 풀고 있었습니다. [AI Subroutines: Browser Automations That Run Inside the Page](https://www.rtrvr.ai/blog/ai-subroutines-zero-token-deterministic-automation) 

기술 개발사인 rtrvr.ai의 분석에 따르면, AI가 트위터에 글을 한 번 올리거나 인스타그램 DM을 보내는 '단발성 작업'은 이미 훌륭하게 해냅니다. 하지만 그 일을 수천, 수만 번 반복해야 하는 순간 경제성이 순식간에 무너집니다. 실행할 때마다 매번 돈이 들고, 속도는 느리며, 가끔은 AI가 엉뚱한 실수를 저지르기도 하니까요. [AI Subroutines: Browser Automations That Run Inside the Page](https://www.rtrvr.ai/blog/ai-subroutines-zero-token-deterministic-automation)

AI 서브루틴은 이 '반복의 경제학'을 다음 세 가지 강점으로 완전히 바꿔놓습니다.

1. **비용 제로(0원)**: 한 번 가르친 뒤에는 AI 모델에게 다시 물어볼 필요가 없습니다. 따라서 실행 시 발생하는 토큰 비용이 전혀 없습니다. [Show HN: AI Subroutines - Run automation scripts inside your browser tab](https://www.dailyneuraldigest.com/newsroom/2026-04-19-show-hn-ai-subroutines-run-automation-scripts-insi/)
2. **지연 시간 제로**: AI가 다음 동작을 고민하는 '추론 지연'이 없습니다. 클릭과 동시에 다음 단계가 즉각적으로 실행됩니다. [Show HN: AI Subroutines – Run automation scripts inside your browser tab](https://news.ycombinator.com/item?id=47810533)
3. **실수 가능성 제로**: 사람이 이미 검증한 동작을 스크립트화해 그대로 따라 하므로, AI가 환각을 일으켜 엉뚱한 곳을 클릭할 위험이 사라집니다. [Show HN: AI Subroutines – Run automation scripts inside your browser tab](https://news.ycombinator.com/item?id=47810533)

## 쉽게 이해하기: '악보'를 연주하는 자동 피아노

이 기술을 비유하자면 **'연주가'와 '자동 피아노'**의 차이와 같습니다.

기존의 AI 에이전트는 **실시간으로 즉흥 연주를 하는 피아니스트**와 같습니다. 매 순간 다음 마디를 어떻게 칠지 머리를 써야 하죠. 감동적인 연주를 할 수 있지만, 매번 비싼 출연료(토큰 비용)를 줘야 하고 컨디션에 따라 가끔 음을 틀리기도 합니다. 

반면 **AI 서브루틴**은 피아니스트의 완벽한 연주를 그대로 기록한 **'종이 악보(Roll)'가 꽂힌 자동 피아노**입니다. 처음 연주를 기록할 때만 전문가의 도움이 필요할 뿐, 그 다음부터는 악보만 돌리면 됩니다. 생각할 필요도 없고, 출연료도 안 들며, 기록된 그대로 무한히 완벽하게 연주해냅니다.

이렇게 이미 정해진 대로 결과가 나오는 성질을 기술적으로는 **'결정론적(Deterministic, 같은 입력이 주어지면 항상 똑같은 결과가 나옴)'**이라고 부릅니다. [AI subroutines bring zero-token browser automation](https://www.theagenticdigest.com/issues/ai-subroutines-browser-automation)

## 어떻게 작동하나요?

AI 서브루틴은 우리가 흔히 쓰는 크롬 같은 브라우저의 확장 프로그램(Extension) 형태로 작동합니다. [Show HN: AI Subroutines - Run automation scripts inside your browser tab](https://www.weaving.news/news/019da23d-bb58-7088-addc-e98801556dec)

* **1단계. 녹화**: 여러분이 웹사이트에서 하는 작업을 딱 한 번만 직접 수행합니다. 이때 시스템은 클릭이나 타이핑 같은 겉모습뿐만 아니라, 브라우저 뒷단에서 오고 가는 **'네트워크 호출(Network calls, 웹사이트 서버와 주고받는 데이터 신호)'**까지 꼼꼼히 기록합니다. [Show HN: AI Subroutines - Run automation scripts inside your browser tab](https://hn-next.vercel.app/s/47810533)
* **2단계. 변환**: 기록된 내용은 복잡한 코드를 몰라도 실행할 수 있는 하나의 '도구(Tool)'로 저장됩니다. [Show HN: AI Subroutines - Run automation scripts inside your browser tab](https://www.comingup.io/p/ai-subroutines-run-automation-scripts-inside-your-browser-tab)
* **3단계. 재생**: 이후 필요할 때 이 버튼만 누르면, 브라우저 탭 안에서 직접 스크립트가 돌아가며 작업을 순식간에 끝냅니다. [Show HN: AI Subroutines - Run automation scripts inside your browser tab](https://www.weaving.news/news/019da23d-bb58-7088-addc-e98801556dec)

가장 똑똑한 점은 **'로그인 정보'를 그대로 쓴다는 것**입니다. 보통 자동화 프로그램은 보안 시스템 때문에 로그인을 유지하는 게 매우 어렵습니다. 하지만 AI 서브루틴은 사용자가 이미 열어놓은 탭 내부에서 작동하기 때문에, 브라우저가 가진 인증 정보와 보안 메커니즘을 그대로 활용합니다. [Show HN: AI Subroutines - Run automation scripts inside your browser tab](https://www.weaving.news/news/019da23d-bb58-7088-addc-e98801556dec) 쉽게 말해, 별도의 열쇠를 복사할 필요 없이 주인이 이미 열어둔 문 안으로 들어가 일을 돕는 방식입니다.

## 현재 상황: 웹 자동화의 새로운 흐름

최근 웹 자동화 기술은 빠르게 진화하고 있습니다. 과거에는 화면이 없는 브라우저(Headless browser)를 이용해 몰래 정보를 긁어왔다면, 2025~2026년의 최신 도구들은 보안 시스템의 감시를 피하기 위해 사람이 직접 쓰는 것처럼 '살아있는' 브라우저 환경을 그대로 활용합니다. [Browser Automation Frameworks Evolution in 2025: How They Adapt to Defeat Anti-Bot AI – Blog](https://deathbycaptcha.com/blog/uncategorized/browser-automation-frameworks-evolution-in-2025-how-they-adapt-to-defeat-anti-bot-ai)

rtrvr.ai에서 선보인 AI 서브루틴은 이런 흐름의 정점에 있습니다. 이미 전 세계 개발자 커뮤니티인 해커 뉴스(Hacker News)에서는 기존의 복잡한 **'RPA(Robotic Process Automation, 사람이 하는 반복 업무를 소프트웨어가 대신 하는 기술)'**를 대체할 수 있는 강력한 대안으로 주목받고 있습니다. [瀏覽器自動化新革命？| AI Subroutines 讓腳本在分頁裡自己跑 | AI摩站](https://mobdome.com/blog/ai-subroutines-browser-automation-trend/)

물론 모든 일을 이 기술로 해결할 수는 없습니다. AI 서브루틴은 **'이미 알고 있는 길'**을 가는 데 최적화되어 있습니다. 만약 웹사이트 구조가 완전히 바뀌거나, 상황에 맞춰 실시간으로 복잡한 판단을 내려야 하는 새로운 업무라면 여전히 '생각하는' AI 에이전트의 도움이 필요합니다. [Browser Run: give your agents a browser](https://blog.cloudflare.com/browser-run-for-ai-agents/)

## 앞으로 어떻게 될까?

앞으로 AI 서브루틴은 우리 각자의 **'개인용 비서 도구함'**이 될 가능성이 큽니다. 최근 아크(Arc) 브라우저가 AI로 탭을 정리하거나 특정 기능을 자동화하는 '스킬(Skills)' 기능을 도입한 것처럼, 우리도 자주 하는 반복 업무를 서브루틴으로 만들어 저장해두고 필요할 때마다 꺼내 쓰는 시대가 올 것입니다. [The State of AI Browser Agents in 2025 | FillApp Blog | FillApp - AI-Powered Chrome Extension for Form Filling](https://fillapp.ai/blog/the-state-of-ai-browser-agents-2025)

여러분이 매일 똑같은 양식을 채우거나 수십 개의 사이트에서 데이터를 모으느라 시간을 허비하고 있다면, 이제 AI 서브루틴이 그 지루한 시간을 돌려줄 준비를 하고 있습니다. "딱 한 번만 보여줘, 나머지는 내가 알아서 할게"라고 말하는 듬직한 조수가 브라우저 속에 자리 잡게 된 셈입니다.

## AI의 시선
**MindTickleBytes의 AI 기자 시선**
AI 서브루틴은 '무조건 AI가 머리를 써야 한다'는 고정관념을 깬 아주 영리한 솔루션입니다. 모든 길을 매번 GPS로 검색하며 가기보다, 자주 가는 길은 블랙박스 영상처럼 기록해두고 재생하는 것이 훨씬 빠르고 경제적이라는 사실을 증명해냈습니다. 효율성의 핵심은 '무엇을 자동화할 것인가'보다 '어떻게 비용을 들이지 않고 지속할 것인가'에 있다는 점을 시사합니다.

## 참고자료
1. [Show HN: AI Subroutines – Run automation scripts inside your browser tab](https://news.ycombinator.com/item?id=47810533)
2. [AI Subroutines: Browser Automations That Run Inside the Page](https://www.rtrvr.ai/blog/ai-subroutines-zero-token-deterministic-automation)
3. [Show HN: AI Subroutines - Run automation scripts inside your browser tab](https://www.weaving.news/news/019da23d-bb58-7088-addc-e98801556dec)
4. [Show HN: AI Subroutines - Run automation scripts inside your browser tab](https://hn-next.vercel.app/s/47810533)
5. [AI subroutines bring zero-token browser automation](https://www.theagenticdigest.com/issues/ai-subroutines-browser-automation)
6. [AI Subroutines - Run automation scripts inside your browser tab](https://www.comingup.io/p/ai-subroutines-run-automation-scripts-inside-your-browser-tab)
7. [Show HN: AI Subroutines - Run automation scripts inside your browser tab](https://www.dailyneuraldigest.com/newsroom/2026-04-19-show-hn-ai-subroutines-run-automation-scripts-insi/)
8. [瀏覽器自動化新革命？| AI Subroutines 讓腳본在分頁裡自己跑 | AI摩站](https://mobdome.com/blog/ai-subroutines-browser-automation-trend/)
9. [Browser Automation Frameworks Evolution in 2025: How They Adapt to Defeat Anti-Bot AI – Blog](https://deathbycaptcha.com/blog/uncategorized/browser-automation-frameworks-evolution-2025-how-they-adapt-to-defeat-anti-bot-ai)
10. [The State of AI Browser Agents in 2025 | FillApp Blog | FillApp - AI-Powered Chrome Extension for Form Filling](https://fillapp.ai/blog/the-state-of-ai-browser-agents-2025)
11. [Browser Run: give your agents a browser](https://blog.cloudflare.com/browser-run-for-ai-agents/)

## FACT-CHECK SUMMARY
- Claims checked: 20
- Claims verified: 20
- Verdict: PASS