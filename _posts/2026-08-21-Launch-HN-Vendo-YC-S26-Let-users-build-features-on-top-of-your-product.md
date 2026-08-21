---
layout: post
title: "내 업무에 꼭 맞는 기능, AI가 알아서 만들어준다면?"
description: "B2B SaaS 서비스의 고질적인 문제인 기능 요청 백로그를 해결하고, 사용자가 직접 기능을 만들 수 있게 해주는 Vendo에 대해 알아봅니다."
summary: "Vendo는 기업용 소프트웨어 사용자가 개발자 도움 없이 직접 원하는 기능이나 앱을 제품 위에 바로 만들어 붙일 수 있게 돕는 오픈소스 사용자 정의 레이어입니다."
tags: [AI, SaaS, B2B, Vendo, 생산성]
image: 2026-08-21-Launch-HN-Vendo-YC-S26-Let-users-build-features-on-top-of-your-product.jpg
image_alt: "사용자가 기존 소프트웨어 화면 위에서 자신에게 필요한 기능을 직접 구성하는 모습을 추상적으로 표현한 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "소프트웨어의 주도권이 개발사에서 사용자로 넘어가는 중요한 전환점입니다. Vendo는 제품의 경직성을 깨고 개별 사용자의 업무 방식을 존중하는 유연한 생태계를 만들 것입니다."
quiz:
  - question: "Vendo의 핵심 기능은 무엇인가요?"
    choices: ["소프트웨어의 소스 코드를 직접 수정하게 함", "사용자가 직접 원하는 기능이나 앱을 제품 내에 생성하게 함", "개발자의 작업 속도를 2배로 높여줌"]
    answer: 1
    explanation: "Vendo는 사용자가 개발자의 도움 없이도 자신의 필요에 맞는 기능이나 마이크로 앱을 제품 위에 직접 구축할 수 있도록 돕습니다."
  - question: "Vendo를 사용하면 기존 제품의 소스 코드가 수정되나요?"
    choices: ["네, 반드시 수정해야 합니다", "아니요, 소스 코드를 건드리지 않고 샌드박스 형태로 구현됩니다", "일부 핵심 기능만 수정됩니다"]
    answer: 1
    explanation: "Vendo는 기존 제품의 소스 코드를 수정하지 않고, 샌드박스(보호된 환경) 내에서 브랜드와 자연스럽게 어우러지는 UI를 생성합니다."
  - question: "Vendo를 통해 생성된 기능은 어떻게 작동하나요?"
    choices: ["독립적인 별도 서버에서 작동함", "제품의 API를 통해 사용자의 권한으로 작동함", "모든 기능이 클라우드 상에서 강제로 업데이트됨"]
    answer: 1
    explanation: "생성된 기능은 해당 제품의 API를 통해 현재 로그인된 사용자의 권한으로 직접 동작하며, 사용자의 작업 흐름에 맞춰 개인화됩니다."
lang: ko
ref: 2026-08-21-Launch-HN-Vendo-YC-S26-Let-users-build-features-on-top-of-your-product
audio: 2026-08-21-Launch-HN-Vendo-YC-S26-Let-users-build-features-on-top-of-your-product.mp3
permalink: /2026/08/21/Launch-HN-Vendo-YC-S26-Let-users-build-features-on-top-of-your-product/
---

상상해보세요. 매일 업무용으로 사용하는 소프트웨어 화면을 보며 "아, 여기서 바로 이 버튼을 눌러서 파일을 내 메일로 보내면 좋을 텐데"라고 생각한 적 있으시죠? 하지만 그 기능을 개발팀에 요청하면, 답변은 항상 "네, 검토해보겠습니다" 아니면 "기능 백로그(요청 목록)가 너무 많아서 올해는 어렵겠네요"라는 식입니다. 

결국 우리는 소프트웨어가 제공하는 기능에 내 업무 방식을 억지로 맞춰야만 했습니다. 마치 발에 맞지 않는 구두를 신고 하루 종일 걸어 다니는 것처럼 말이죠. 그런데 만약 사용자가 직접 내 손에 딱 맞는 기능을 그 자리에서 바로 만들어 붙일 수 있다면 어떨까요? 최근 실리콘밸리 Y 컴비네이터(YC)의 지원을 받아 등장한 **벤도(Vendo)**가 바로 이 문제를 해결하려 합니다.

## 이게 왜 중요한가요? (Why It Matters)

기업용 소프트웨어(B2B SaaS)를 사용하는 많은 이들은 항상 '나에게 필요한 기능'과 '제품이 제공하는 기능' 사이의 괴리를 느낍니다. 모든 기업의 업무 방식은 제각각인데, 소프트웨어는 '평균적인' 기능만 제공하기 때문입니다.

Vendo는 이러한 소프트웨어의 '경직성'을 허뭅니다. 이 기술을 도입한 기업의 사용자는 개발자의 도움 없이도 본인의 업무에 필요한 맞춤형 기능이나 작은 앱(마이크로 앱)을 직접 생성할 수 있습니다. [출처: Vendo(YC S26) – Let your users build features on top of your product](https://www.ycombinator.com/companies/vendo). 결과적으로 기업은 끝도 없이 쌓이는 기능 개발 요청(feature backlog)에서 벗어나고, 사용자는 자신만의 작업 흐름(Workflow)을 완성할 수 있게 됩니다. [출처: YC-Backed Vendo Lets Users Build Features on Top of SaaS ...](https://www.founderland.ai/articles/yc-backed-vendo-lets-users-build-features-on-top-of-saas-pro-mrynzgii).

## 쉽게 이해하기 (The Explainer)

이렇게 비유해볼까요? 기존의 소프트웨어가 '잘 만들어진 완성된 가구'라면, Vendo는 그 가구 위에 자유롭게 덧붙일 수 있는 '레고 블록 세트'와 같습니다.

쉽게 말해서, Vendo는 소프트웨어 안에 들어가는 '임베디드 에이전트(제품 내부에 삽입되어 사용자를 대신해 작업하는 인공지능)'입니다. [출처: GitHub - runvendo/vendo: Embedded agents your customers use ...](https://github.com/runvendo/vendo).

1. **연결**: Vendo는 해당 제품이 제공하는 API(소프트웨어가 외부와 소통하는 통로)를 통해 마치 실제 사용자가 작업하듯이 안전하게 명령을 내립니다. [출처: Vendo: open-source layer that lets users build features on ...](https://zeli.app/en/story/49376038).
2. **구축**: 사용자가 기능을 요청하면, Vendo 시스템 내부의 맞춤형 장치가 리액트(React, 사용자 인터페이스를 만들기 위한 자바스크립트 라이브러리) 컴포넌트를 작성합니다. 이때 실수를 방지하는 가이드라인(Guardrails)이 적용되어 안전하게 호출을 수행합니다. [출처: LaunchHN:Vendo(YC S26) –Letusersbuildfeaturesontopof...](https://news.ycombinator.com/item?id=49376038).
3. **렌더링**: 이렇게 만들어진 기능은 원래 소프트웨어의 코드 자체를 건드리지 않으면서, 샌드박스(외부와 차단된 안전한 독립 공간) 내에서 마치 원래 있었던 기능처럼 자연스럽게 화면에 그려집니다. [출처: GitHub - runvendo/vendo: Embedded agents your customers use ...](https://github.com/runvendo/vendo).

## 현재 상황 (Where We Stand)

현재 Vendo는 오픈소스(누구나 코드를 보고 기여할 수 있는 방식)로 제공되고 있습니다. [출처: Vendo: open-source layer that lets users build features on ...](https://zeli.app/en/story/49376038). 기업 담당자라면 단 60초 만에 `npm install` 명령어를 통해 자신의 소프트웨어에 설치할 수 있을 만큼 간편합니다. [출처: Vendo: open-source layer that lets users build features on ...](https://zeli.app/en/story/49376038).

Vendo의 공동 창업자인 유세프(Yousef)는 인공지능 에이전트들이 대시보드와 사용자 인터페이스를 소비하는 방식을 근본적으로 바꾸고 있으며, 그 중심에는 '개인화'가 있다고 강조했습니다. [출처: Show HN: Vendo (YC S26) – Let your users add their own ...](https://news.ycombinator.com/item?id=48926618). 현재 많은 B2B SaaS 기업들이 이 솔루션을 통해 고객이 요청하는 개별 기능들을 처리하는 '백로그 지옥'에서 탈출하고자 노력하고 있습니다. [출처: YC-Backed Vendo Lets Users Build Features on Top of SaaS ...](https://www.founderland.ai/articles/yc-backed-vendo-lets-users-build-features-on-top-of-saas-pro-mrynzgii).

## 앞으로 어떻게 될까? (What's Next)

앞으로는 우리가 사용하는 거의 모든 업무 도구가 '완성품'이 아닌 '재료'의 형태로 바뀔 가능성이 큽니다. Vendo와 같은 도구가 대중화되면, 소프트웨어를 만드는 기업은 핵심 엔진만 제공하고, 사용자가 그 위에 자신만의 작업 방식을 덧씌우는 형태가 표준이 될 것입니다. 

개발자들은 개별 고객의 사소한 요구사항을 챙기는 대신 더 큰 시스템의 안정성과 핵심 기능 개발에 집중할 수 있게 될 것입니다. 우리가 사용하는 앱들이 마치 레고 블록처럼 서로 맞물리며 나의 업무 스타일을 기억하는 미래가 다가오고 있습니다.

## MindTickleBytes의 AI 기자 시선

소프트웨어를 만드는 사람이 아니라, 그 소프트웨어를 가장 잘 아는 사용자가 기능을 정의하는 시대가 열렸습니다. Vendo는 기술의 복잡함 뒤에 숨겨진 '도구의 주권'을 사용자에게 되돌려주는 신선한 시도입니다. 이제 소프트웨어가 내 업무 방식을 묻는 것이 아니라, 내가 소프트웨어를 내 업무 방식에 맞게 진화시키는 과정이 자연스러워질 것입니다.

## 참고자료

1. [Vendo: Let your users build their own features on top of your ...](https://www.ycombinator.com/companies/vendo)
2. [Vendo — YC S26 Launch on Hacker News - bestofshowhn.com](https://bestofshowhn.com/yc-s26/vendo)
3. [Show HN: Vendo (YC S26) – Let your users add their own ...](https://news.ycombinator.com/item?id=48926618)
4. [GitHub - runvendo/vendo: Embedded agents your customers use ...](https://github.com/runvendo/vendo)
5. [Vendo: open-source layer that lets users build features on ...](https://zeli.app/en/story/49376038)
6. [Introducing Vendo: let your users edit your product - LinkedIn](https://www.linkedin.com/pulse/introducing-vendo-let-your-users-edit-product-ankit-gupta-0uu9c)
7. [Vendo lets users build custom features on top of your product ...](https://www.linkedin.com/posts/y-combinator_vendo-yc-s26-lets-your-users-build-their-activity-7485385624418439168-KuP2)
8. [LaunchHN:Vendo(YC S26) –Letusersbuildfeaturesontopof...](https://news.ycombinator.com/item?id=49376038)
9. [Vendo (YC S26) – Let your users add their lown features to ...](https://aiindigo.com/blog/vendo-yc-s26-let-your-users-add-their-lown-features-to-your-product-deep-dive-te)
10. [YC-Backed Vendo Lets Users Build Features on Top of SaaS ...](https://www.founderland.ai/articles/yc-backed-vendo-lets-users-build-features-on-top-of-saas-pro-mrynzgii)