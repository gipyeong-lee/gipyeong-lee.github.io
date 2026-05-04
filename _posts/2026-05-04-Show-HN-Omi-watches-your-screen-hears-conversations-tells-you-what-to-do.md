---
layout: post
title: "내가 본 모든 걸 기억하는 '인생 비서'가 나타났다? 이마에 붙이는 AI, 'Omi'가 바꾸는 일상"
description: "내가 보는 화면과 듣는 대화를 실시간으로 파악해 할 일을 정리해주고 조언까지 건네는 새로운 AI 비서 Omi(오미)를 소개합니다. 웨어러블 기기와 데스크톱 앱의 만남을 쉽게 풀어봅니다."
summary: "사용자가 보고 듣는 모든 것을 기억해 실시간 전사, 요약, 실행 항목 생성 및 선제적인 조언을 제공하는 오픈 소스 AI 비서 Omi가 공개되었습니다."
tags: [AI, 웨어러블, Omi, 인공지능비서, 테크트렌드]
image: 2026-05-04-Show-HN-Omi-watches-your-screen-hears-conversations-tells-you-what-to-do.jpg
image_alt: "사람의 이마에 붙어 있거나 책상 위에서 화면을 지켜보며 사용자의 일상을 돕는 똑똑한 AI 비서의 모습"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "Omi는 AI가 단순히 질문에 답하는 도구를 넘어, 우리 삶의 맥락을 스스로 파악하는 '능동적 파트너'로 진화하고 있음을 보여줍니다."
quiz:
  - question: "Omi(오미)의 주요 기능 중 하나가 아닌 것은 무엇인가요?"
    choices: ["실시간 대화 전사(기록)", "사용자 화면 캡처 및 기억", "자동으로 이메일 스팸 발송", "실행 항목(Action Items) 생성"]
    answer: 2
    explanation: "Omi는 화면과 대화를 파악해 요약과 할 일을 만들어주지만, 스팸 발송과 같은 악의적인 기능은 포함하지 않습니다."
  - question: "Omi 개발자가 이 도구를 설명하며 사용한 비유는 무엇인가요?"
    choices: ["나보다 더 믿을 수 있는 제2의 뇌", "말을 잘 듣는 인공지능 강아지", "어디든 따라다니는 감시 카메라", "똑똑한 계산기"]
    answer: 0
    explanation: "Omi의 문서에서는 이 도구를 '첫 번째 뇌보다 더 신뢰할 수 있는 제2의 뇌'라고 정의하고 있습니다."
  - question: "Omi 웨어러블 기기의 독특한 외형적 특징은 무엇인가요?"
    choices: ["손목에 차는 시계 형태", "이마에 붙이는 큰 버튼 형태", "귀에 거는 이어폰 형태", "안경처럼 쓰는 형태"]
    answer: 1
    explanation: "일부 외신 보도에 따르면 Omi 웨어러블 기기는 이마에 붙일 수 있는 큰 버튼 모양으로 묘사되기도 했습니다."
lang: ko
ref: 2026-05-04-Show-HN-Omi-watches-your-screen-hears-conversations-tells-you-what-to-do
audio: 2026-05-04-Show-HN-Omi-watches-your-screen-hears-conversations-tells-you-what-to-do.mp3
permalink: /2026/05/04/Show-HN-Omi-watches-your-screen-hears-conversations-tells-you-what-to-do/
---

## "방금 내가 무슨 말을 했더라?" 이제 AI가 대신 기억해줍니다

상상해보세요. 아주 중요한 업무 미팅 중에 상사가 번개처럼 빠른 속도로 지시사항을 쏟아냅니다. 받아적으려니 손이 꼬이고, 녹음하자니 나중에 다시 듣기가 막막합니다. 혹은 유튜브에서 정말 유용한 정보를 발견했는데, 며칠 뒤 정작 필요할 때가 되니 그 영상 제목이 도무지 떠오르지 않아 답답했던 적 없으신가요? 

우리는 매일 엄청난 양의 정보를 보고 듣지만, 안타깝게도 우리 뇌는 그중 아주 일부분만 기억해낼 수 있습니다. 지금까지 챗GPT(ChatGPT)나 클로드(Claude) 같은 똑똑한 인공지능을 활용하려면, 우리가 일일이 상황을 설명하거나 화면을 캡처해서 보내는 수고를 해야 했습니다. 하지만 내가 굳이 입을 열지 않아도, 내가 무엇을 보고 누구와 대화하는지 AI가 곁에서 지켜보며 알아서 도와준다면 어떨까요?

오늘 소개해드릴 **Omi(오미)**는 바로 이런 마법 같은 상상을 현실로 옮기려는 야심 찬 프로젝트입니다. 개발자는 이 도구를 단순한 소프트웨어가 아닌 '인생 설계자(Life Architect)'라고 부릅니다. [Source 14](https://hn.makr.io/item/47784914) Omi는 여러분의 화면을 함께 보고 대화를 경청하며, 여러분이 다음에 무엇을 해야 할지 미리 조언해주는 든든한 동반자가 되어줍니다.

---

## 이게 왜 중요한가요? "내 옆에 앉아있는 그림자 비서"

우리가 기술을 쓰면서 느끼는 가장 큰 피로감은 역설적으로 '입력'에서 옵니다. AI에게 정보를 전달하는 과정 자체가 또 하나의 '일'이 되기 때문이죠. Omi는 이 귀찮은 과정을 통째로 없애버리려 합니다.

### 1. 공기처럼 존재하는 AI (Ambient AI)
보통 우리는 스마트폰 화면을 뚫어져라 쳐다보며 정보를 찾느라 주변 상황을 놓치곤 합니다. 하지만 Omi의 철학은 정반대입니다. 사용자가 기기에 얽매이는 대신, AI가 일상 속에 공기처럼 자연스럽게 스며들어(Ambient, 주변에 존재하는) 사용자가 현재의 삶에 더 집중할 수 있게 돕는 것이 목표입니다. [Source 9](https://www.linkedin.com/company/omidotme) 기술이 사용자를 방해하는 것이 아니라, 뒤에서 묵묵히 받쳐주는 셈이죠.

### 2. 기억의 무한 확장: "제2의 뇌"
Omi의 공식 문서에는 아주 흥미로운 표현이 등장합니다. 바로 **"여러분의 첫 번째 뇌보다 더 신뢰할 수 있는 제2의 뇌(A 2nd brain you trust more than your 1st)"**라는 정의입니다. [Source 15](https://github.com/BasedHardware/Omi) 사람의 기억력은 감정이나 컨디션에 따라 흐릿해지기도 하지만, 데이터로 기록되는 AI는 내가 본 모든 찰나의 화면과 스쳐 지나간 대화까지도 완벽하게 기억할 수 있기 때문입니다. 

---

## 쉽게 이해하기: Omi는 어떻게 작동하나요?

Omi를 한마디로 정의하자면 **'보고 듣고 기억하는 인공지능 비서'**입니다. [Source 3](https://github.com/BasedHardware/omi?tab=readme-ov-file) 쉽게 말해서, 여러분의 디지털 생활 전체를 실시간으로 중계받는 비서라고 생각하시면 됩니다.

### 핵심 기능 3가지

1.  **실시간 눈(Screen Capture):** 컴퓨터나 스마트폰 화면에서 일어나는 일을 실시간으로 캡처합니다. 내가 어떤 영문 기사를 읽고 있는지, 어떤 복잡한 코드를 짜고 있는지 AI가 옆에서 같이 모니터를 보고 있는 것과 같습니다.
2.  **실시간 귀(Transcription):** 대화를 실시간으로 듣고 이를 즉시 글자로 옮깁니다. 이를 전사(Transcription, 말소리를 텍스트로 바꾸는 작업)라고 하는데요. 회의 내용이나 친구와의 약속을 놓치지 않고 꼼꼼히 기록해둡니다. [Source 3](https://github.com/BasedHardware/omi?tab=readme-ov-file)
3.  **능동적 조언(Proactive Advice):** 가장 놀라운 점은 사용자가 묻기 전에 먼저 제안한다는 것입니다. 대화 중에 "내일 점심 어때?"라는 말이 나오면, AI가 알아서 달력을 체크하고 할 일 목록(Action Items)을 만들어줍니다. [Source 3](https://github.com/BasedHardware/omi?tab=readme-ov-file)

### 비유로 보는 Omi
Omi는 마치 **'내 모든 일상을 같이 경험하는 비서'**와 같습니다. 
*   **기존 AI:** 비서에게 "어제 회의 내용 요약해줘"라고 시키려면, 내가 직접 녹음 파일을 찾아서 비서에게 이메일로 보내줘야 했습니다.
*   **Omi:** 비서가 이미 어제 회의실 옆자리에 앉아 있었습니다. 내가 묻기도 전에 "어제 약속하신 보고서 마감이 오늘 오후 3시입니다. 지금 시작하실까요?"라고 먼저 말을 건네는 식입니다.

개발자는 Omi가 시중에 나온 유명 AI 도구들(Cluely, Rewind, Granola, ChatGPT, Claude 등)의 장점만을 쏙쏙 골라 하나로 합쳐놓은 결정체라고 설명합니다. [Source 1](https://news.ycombinator.com/item?id=47784914)

---

## 현재 상황: 이마에 붙이는 '디지털 눈'? 독특한 Omi의 모습

Omi는 컴퓨터 안의 프로그램뿐만 아니라 몸에 직접 착용하는 '웨어러블(Wearable)' 기기로도 개발되고 있습니다. 그 모습이 꽤나 파격적입니다.

*   **이마에 붙이는 커다란 버튼:** 일부 외신에 따르면, Omi 웨어러블 기기는 이마에 붙일 수 있는 커다란 버튼 모양을 하고 있습니다. [Source 5](https://www.designboom.com/technology/wearable-ai-device-omi-reads-minds-completes-tasks-01-10-2025/) 마치 '제3의 눈'처럼 이 기기가 사용자의 생각을 읽거나(Mind reading) 주변의 대화를 들어서 필요한 일을 척척 처리해준다는 과감한 목표를 가지고 있습니다. [Source 18](https://interestingengineering.com/ces-2025/omi-brain-reading-wearable)
*   **누구나 쓸 수 있는 '오픈 소스':** 이 독특한 기기가 없어도 실망하실 필요는 없습니다. Omi는 오픈 소스(Open-source, 프로그램의 설계도를 누구나 볼 수 있게 공개한 방식)로 개발되고 있어, 데스크톱이나 스마트폰 앱만으로도 충분히 그 능력을 체험해볼 수 있습니다. [Source 6](https://news.ycombinator.com/item?id=41333648)
*   **열정적인 개발 과정:** Omi의 데스크톱 버전은 약 4개월이라는 짧은 기간(대학의 한 학기 정도 기간이죠) 동안 집중적으로 개발되어 완성되었습니다. [Source 17](https://news.mcan.sh/item/47784914) 개발자는 다른 누구보다도 '나 자신이 가장 필요로 하는 도구'를 만들고 싶어 이 프로젝트를 시작했다고 합니다. [Source 6](https://news.ycombinator.com/item?id=41333648)

---

## 앞으로 어떻게 될까? 우리가 마주할 새로운 풍경

Omi와 같은 기술이 우리 삶에 완전히 자리를 잡게 되면 어떤 변화가 찾아올까요?

첫째, **'검색'이라는 행위 자체가 사라질지도 모릅니다.** "저번에 봤던 그 기사 제목이 뭐였지?"라며 검색창을 두드리는 대신, AI에게 "그저께 본 파란색 도표가 있던 문서 좀 찾아줘"라고 말하면 끝입니다. AI가 이미 내가 본 모든 것을 기억의 저장소에 담아두었기 때문입니다. [Source 15](https://github.com/BasedHardware/Omi)

둘째, **업무의 흐름이 끊기지 않습니다.** 회의가 끝나고 자리에 앉으면 이미 인공지능이 정리한 요약본이 도착해 있고, 내가 해야 할 일들은 자동으로 달력에 등록되어 있을 것입니다. 인간은 '정리'라는 노동에서 해방되어 '창의적인 판단'에만 집중할 수 있게 됩니다.

물론, 24시간 내 일상을 지켜보는 AI에 대한 사생활 침해 우려도 분명 존재합니다. 이에 대해 Omi 팀은 모든 소스코드를 투명하게 공개하는 오픈 소스 방식을 통해, 사용자가 안심하고 기술을 신뢰할 수 있도록 노력하고 있습니다. [Source 6](https://news.ycombinator.com/item?id=41333648)

---

## AI의 시선: MindTickleBytes AI 기자 시선

"Omi는 인공지능이 '도구'에서 '동반자'로 넘어가는 중요한 변곡점을 상징합니다. 지금까지의 AI가 우리가 명령을 내려야만 움직이는 수동적인 존재였다면, 이제는 우리의 삶의 맥락을 스스로 읽어내고 먼저 손을 내미는 능동적인 파트너가 되려 하고 있습니다. 이마에 붙이는 기기 형태는 지금 당장 보기엔 조금 낯설고 생경할 수 있지만, 기술이 우리 몸에 더 밀착될수록 우리가 누릴 '지능의 가치'는 상상 이상으로 커질 것입니다. 결국 우리는 '잊어버릴 걱정 없는 세상'으로 나아가고 있는 셈입니다."

---

## 참고자료
1. [Show HN: Omi – watches your screen, hears conversations, tells you what to do | Hacker News](https://news.ycombinator.com/item?id=47784914)
2. [GitHub - BasedHardware/omi: AI that sees your screen, listens to your conversations and tells you what to do · GitHub](https://github.com/BasedHardware/omi?tab=readme-ov-file)
3. [omi/README.md at main · BasedHardware/omi](https://github.com/BasedHardware/omi/blob/main/README.md)
4. [wearable AI device 'omi' reads minds, hears conversations and completes tasks users think of](https://www.designboom.com/technology/wearable-ai-device-omi-reads-minds-completes-tasks-01-10-2025/)
5. [Show HN: Omi – Open-source AI wearable for capturing conversations | Hacker News](https://news.ycombinator.com/item?id=41333648)
6. [r/hackernews on Reddit: Show HN: Omi – Open-source AI wearable for capturing conversations](https://www.reddit.com/r/hackernews/comments/1ezxfe4/show_hn_omi_opensource_ai_wearable_for_capturing/)
7. [Omi | LinkedIn](https://www.linkedin.com/company/omidotme)
8. [Show HN: Omi - watches your screen, hears conversations, tells you what ...](https://hn.makr.io/item/47784914)
9. [AI that sees your screen, listens to your conversations and tells you ...](https://github.com/BasedHardware/Omi)
10. [Show HN: Omi - watches your screen, hears conversations, tells you what ...](https://news.mcan.sh/item/47784914)
11. [Omi: This wearable could read your brain, help flirt, ace exams](https://interestingengineering.com/ces-2025/omi-brain-reading-wearable)

## FACT-CHECK SUMMARY
- Claims checked: 14
- Claims verified: 14
- Verdict: PASS