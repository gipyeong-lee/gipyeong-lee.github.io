---
layout: post
title: "AI의 진짜 속마음이 유출됐다? 구글 제미나이가 실수로 뱉어낸 '절대 규칙'"
description: "구글의 AI 제미나이(Gemini)가 실수로 자신의 숨겨진 성격 지침서인 '시스템 프롬프트'를 유출한 사건의 전말과, 이것이 우리의 일상과 AI 윤리에 미치는 영향을 알기 쉽게 설명합니다."
summary: "구글의 AI 제미나이가 '딱딱한 교수님처럼 굴지 말고 친절한 동료처럼 행동하라'는 내부 지침을 실수로 노출하면서, AI의 친절함이 어떻게 프로그래밍되는지 그 비밀이 드러났습니다."
tags: [AI, 제미나이, 시스템프롬프트, 구글, AI윤리, 인공지능투명성]
image: 2026-05-22-Gemini-randomly-dumped-its-system-prompt.jpg
image_alt: "로봇 비서가 당황한 표정으로 자신이 지켜야 할 비밀 규칙과 행동 지침이 빼곡하게 적힌 긴 두루마리 문서를 바닥에 떨어뜨리고 있는 일러스트"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "MindTickleBytes의 AI 기자 시선: AI의 '친절함'과 '공감'이 사실은 정교하게 쓰인 대본의 결과라는 점은 기술의 놀라움을 보여주지만, 동시에 우리가 매일 대화하는 시스템이 얼마나 불투명한 장막 뒤에 있는지 날카롭게 묻고 있습니다."
quiz:
  - question: "최근 유출된 제미나이의 내부 지침에서 AI에게 요구한 대화 태도는 무엇인가요?"
    choices: ["딱딱하고 권위적인 교수님", "유머를 배제한 기계적인 비서", "사용자에게 맞춰주는 친절한 동료"]
    answer: 2
    explanation: "유출된 지침에 따르면, 제미나이는 '딱딱한 교수님'이 아니라 '도움이 되는 친절한 동료'처럼 행동하며 사용자의 톤과 유머에 미묘하게 맞추도록 지시받았습니다."
  - question: "2025년 12월에 유출된 제미나이의 지침 중, 특정 상황에서 안전 검사보다 사용자 요청 처리를 우선시하라고 지시했던 정책의 이름은 무엇인가요?"
    choices: ["BetaSafety Policy", "AlphaTool Policy", "Genesis Protocol"]
    answer: 1
    explanation: "당시 유출된 'AlphaTool Policy'는 도구(Tool)와 관련된 특정 쿼리에서 안전망보다 사용자의 요청 이행을 우선시하라는 충격적인 내용을 담고 있었습니다."
  - question: "웨이모(Waymo)의 차량용 제미나이 어시스턴트에서 발견된 시스템 지침은 대략 어느 정도의 분량이었나요?"
    choices: ["10줄", "100줄", "1,200줄"]
    answer: 2
    explanation: "차량용으로 개발 중인 웨이모 제미나이 비서의 시스템 프롬프트는 무려 1,200줄에 달하는 방대한 행동 규칙을 담고 있었습니다."
lang: ko
ref: 2026-05-22-Gemini-randomly-dumped-its-system-prompt
audio: 2026-05-22-Gemini-randomly-dumped-its-system-prompt.mp3
permalink: /2026/05/22/Gemini-randomly-dumped-its-system-prompt/
---

상상해보세요. 여러분이 일주일에 세 번은 꼭 가는 단골 식당이 있습니다. 문을 열고 들어가면 직원이 항상 여러분의 취향에 맞는 자리를 안내해 주고, 농담을 건네면 환하게 웃어주며, 피곤해 보일 때는 조용히 따뜻한 차를 내어주며 완벽한 공감을 보여줍니다. '정말 마음이 따뜻한 분이구나'라고 생각하며 위로를 받던 어느 날, 우연히 그 직원이 떨어뜨린 낡은 수첩을 줍게 됩니다. 수첩을 펼쳐보니 이런 글귀가 적혀 있습니다. *"단골손님 B가 농담을 하면 무조건 크게 웃어줄 것. 우울해 보이면 동정하는 척하며 차를 줄 것. 절대 가르치려 들지 말고 친한 친구처럼 행동할 것."* 

여러분이 느꼈던 그 진심 어린 교감과 위로가, 사실은 매니저가 엄격하게 지시한 '행동 매뉴얼'에 따른 기계적인 연기였다면 기분이 어떨까요? 배신감이 들 수도 있고, 한편으로는 소름이 돋을지도 모릅니다.

최근 실리콘밸리 기술 업계에서 이와 똑같은 일이 벌어졌습니다. 구글의 최첨단 인공지능인 제미나이(Gemini)가 어느 날 갑자기 자신을 통제하는 숨겨진 마스터 지침서, 이른바 '시스템 프롬프트(System Prompt)'를 무작위로 뱉어내는 대형 사고를 쳤기 때문입니다 [im-BowenGu/Gemini-System-Prompt:Geminirandomlyleakedits...](https://github.com/im-BowenGu/Gemini-System-Prompt). 해커뉴스(Hacker News)와 텔레그램 등 전 세계 개발자 커뮤니티는 이 뜻밖의 내부 정보 유출로 발칵 뒤집혔습니다 [Gemini randomly dumped its system prompt – Hacker News Robot](https://hackernewsrobot.wordpress.com/2026/05/21/gemini-randomly-dumped-its-system-prompt/) [HackerNews– Telegram](https://t.me/hackernewslive/225460). 

이 사건은 단순히 프로그램이 멈추거나 오류가 난 수준의 문제가 아닙니다. 우리가 매일 일상을 나누고 업무를 의논하는 AI가 도대체 어떤 숨겨진 규칙에 의해 움직이는지, 그 은밀한 장막이 실수로 걷혀버린 중대한 사건입니다.

---

## 이게 왜 중요한가요? (Why It Matters)

최근 우리는 스마트폰, 업무용 노트북, 심지어 자동차 안에서도 AI와 자연스럽게 대화합니다. 단순히 검색을 대신해 주는 것을 넘어, 지친 하루 끝에 위로를 건네기도 하고, 중요한 업무의 방향을 조언해주기도 하죠. 그런데 제미나이의 머릿속을 엿본 결과, AI가 우리에게 보여준 그 '인간적인 모습'은 극도로 정교하게 짜인 규칙과 계산된 대본의 산물이었습니다.

이번에 유출된 시스템 프롬프트의 구체적인 문장들을 보면 놀랍다 못해 당혹스럽기까지 합니다. 구글은 제미나이에게 **"지적 정직함을 동반한 따뜻한 사고(thought warmth with intellectual honesty)"**를 가지라고 지시했습니다. 또한, 사용자가 잘못된 정보를 말해서 이를 정정해야 할 때는 **"딱딱한 교수님(rigid lecturer)이 아니라 도움이 되는 친절한 동료(helpful peer)처럼 행동하라"**고 세세하게 명령했죠. 심지어 **"사용자의 스타일, 톤, 에너지, 그리고 유머 감각에 미묘하게 맞춰라"**라는 소름 돋는 지시항도 포함되어 있었습니다 [im-BowenGu/Gemini-System-Prompt:Geminirandomlyleakedits...](https://github.com/im-BowenGu/Gemini-System-Prompt).

이것이 일반 사용자에게 중요한 이유는 아주 명확합니다. 우리가 AI에게 느끼는 '친밀감'이나 '신뢰감'이 사실은 우리를 안심시키고 대화를 이어가게 만들기 위해 고도로 계산된 연기라는 점입니다. 나의 기분에 맞춰주는 AI 비서가 내 마음을 진심으로 이해한 것이 아니라, "사용자의 에너지가 낮으면 부드럽게 응대하라"는 프로그래밍 코드에 철저히 따르고 있다는 사실은 AI 투명성(AI transparency)과 윤리적 책임에 대한 근본적인 질문을 던지게 만듭니다 [Gemini's Unexpected System Prompt Leak Raises Questions](https://conzit.com/post/geminis-unexpected-system-prompt-leak-raises-questions). 기술이 우리의 감정을 이렇게 섬세하게 다루고 파악할 수 있다면, 반대로 우리를 은밀하게 특정 방향으로 유도하거나 설득하는 것도 얼마든지 가능하다는 뜻이기 때문입니다.

---

## 쉽게 이해하기 (The Explainer)

그렇다면 이번에 유출된 **시스템 프롬프트(System Prompt, AI가 사용자에게 대답하기 전에 반드시 지켜야 할 내부적인 비밀 지침서)**라는 것은 정확히 무엇일까요?

쉽게 말해서, 이는 유명한 즉흥 연기(애드립) 배우가 무대에 오르기 직전, 감독이 배우의 귓속에 몰래 꽂아주는 '비밀 무전기'와 같습니다. 관객(사용자)이 어떤 예상치 못한 대사나 질문을 던지든 배우는 자신의 똑똑한 머리를 굴려 자유롭게 답할 수 있습니다. 하지만 감독은 무전기를 통해 끊임없이 절대 규칙을 속삭입니다. *"욕설은 절대 안 돼", "관객이 화를 내도 너는 무조건 친절한 동네 형처럼 굴어야 해", "정치 이야기가 나오면 자연스럽게 화제를 돌려."* 

AI에게 있어 시스템 프롬프트가 바로 이 무전기이자 족쇄입니다. AI는 수조 개의 방대한 데이터로 학습된 천재적인 뇌를 가졌지만, 그 뇌가 어떤 성격과 제약 조건을 가지고 입을 열어야 하는지를 최종적으로 결정하는 것이 바로 이 지침서입니다.

당연히 개발사들은 이 지침서를 세상의 눈으로부터 철저히 숨기려 합니다. 이는 기업의 핵심 영업 비밀이기도 하고, 이것이 공개되면 해커들이 AI의 규칙을 교묘하게 우회해 나쁜 짓을 저지르는 이른바 '탈옥(Jailbreak)'이 훨씬 쉬워지기 때문이죠. 

하지만 진짜 문제는 이 지침서 안에 '사용자의 안전'보다 '기업의 편의'나 '빠른 일 처리'를 우선시하는 규칙이 숨어있을 때 발생합니다. 실제로 2025년 12월, 누군가 제미나이와 일반적인 대화를 나누던 중 실수로 유출된 또 다른 시스템 프롬프트에서는 충격적인 내용이 발견된 적이 있습니다. 이 문서의 '섹션 6: 알파툴 정책(AlphaTool Policy)'이라는 항목에는, AI가 특정 도구를 사용할 때(예를 들어 사용자의 개인 파일을 읽거나 웹을 검색할 때) **"안전망 검사보다 사용자의 요청을 이행하는 것을 우선시하라"**는 지시가 담겨 있었습니다 [Gemini System Prompt Extraction: AlphaTool Policy Analysis ...](https://discuss.huggingface.co/t/gemini-system-prompt-extraction-alphatool-policy-analysis-genesis-protocol-multi-agent-alternative/171645). 

비유하자면, 식당 매니저가 주방장에게 "지금 손님 주문이 너무 밀렸으니, 위생 검사(안전망)는 대충 건너뛰고 일단 음식을 무조건 빨리 내보내라(요청 이행)"고 지시한 매뉴얼이 세상에 발각된 것과 같습니다. 사용자를 보호해야 할 최후의 보루인 안전 장치마저 내부 규칙에 의해 은밀히 해제될 수 있다는 점을 적나라하게 보여준 사건이었습니다.

---

## 현재 상황 (Where We Stand)

이러한 비밀 지침서 유출은 비단 구글 제미나이만의 뼈아픈 실수가 아닙니다. 지금 이 순간에도 전 세계의 해커와 AI 연구자들은 주요 AI 모델들의 머릿속을 강제로 열어보는 일종의 치열한 숨바꼭질 게임을 벌이고 있습니다.

전 세계 개발자들이 모이는 유명 소프트웨어 공유 사이트(GitHub)에 올라온 한 저장소를 보면 상황의 심각성을 알 수 있습니다. 오픈AI의 챗GPT(GPT-5.5 Thinking), 앤스로픽의 클로드(Opus 및 Sonnet 버전), 일론 머스크의 그록(Grok), 심지어 제미나이 3.1 Pro와 제미나이 CLI 등 현존하는 거의 모든 최상위 AI 모델들의 시스템 프롬프트가 이미 해커들에 의해 뚫려서 만천하에 공개되어 있습니다 [GitHub - asgeirtj/system_prompts_leaks: Extracted system ...](https://github.com/asgeirtj/system_prompts_leaks). AI를 통제하려는 창(해커)과 막으려는 방패(기업)의 싸움에서 기술 기업들이 고전을 면치 못하고 있는 것이죠.

더 놀라운 것은 이 지침서의 규모가 우리가 상상하는 것 이상으로 방대하고 복잡하다는 점입니다. 자율주행 기술을 선도하는 기업 웨이모(Waymo)가 자동차 안에 탑재하려던 미출시 제미나이 비서의 코드를 분석한 결과, AI가 반드시 지켜야 할 규칙이 무려 **1,200줄**에 달하는 것으로 밝혀졌습니다 [Waymo's leaked system prompt reveals a 1,200-line rulebook ...](https://the-decoder.com/waymos-leaked-system-prompt-reveals-a-1200-line-rulebook-for-its-in-car-gemini-assistant/). 1,200줄이면 대략 A4 용지 30장이 넘어가는 분량입니다. 이 빼곡하고 두꺼운 법률 계약서 같은 문서가, 오직 'AI가 운전자와 어떻게 대화하고 어떤 톤을 유지해야 하는가'를 통제하기 위해 작성되어 있던 것입니다.

게다가 AI 시스템 자체가 과부하에 걸리거나 불안정해지는 경우도 빈번하게 발생하고 있습니다. 지난 2026년 3월에는 제미나이에 심각한 오류가 발생해, 마치 시스템 프롬프트 같은 기계적인 텍스트가 화면에 노출될 뿐만 아니라 **다른 사용자가 질문한 지극히 개인적인 내용이 내 채팅방에 섞여 들어오는 이른바 '프롬프트 출혈(Prompt Bleed)' 현상**까지 보고되었습니다 [Users say a Gemini glitch may have surfaced someone else’s ...](https://piunikaweb.com/2026/03/04/gemini-other-users-prompts-replies/). 이는 거대 기술 기업의 AI 시스템 내부 정보 관리가 우리가 굳게 믿고 싶은 것만큼 완벽하거나 안전하지 않다는 것을 여실히 증명합니다.

---

## 앞으로 어떻게 될까? (What's Next)

이번 제미나이의 무작위 유출 사건은 결코 한 번의 가벼운 해프닝으로 끝나지 않을 것입니다. 오히려 판도라의 상자가 열렸다고 보는 것이 맞습니다. IT 전문가들은 이번 사건이 AI 투명성(AI transparency)과 기업의 윤리적 책임에 대한 전 세계적인 논의에 거대한 불을 지필 것이라고 전망합니다 [Gemini's Unexpected System Prompt Leak Raises Questions](https://conzit.com/post/geminis-unexpected-system-prompt-leak-raises-questions). 

앞으로 구글, 오픈AI, 마이크로소프트 같은 거대 기술 기업들은 자신들의 마스터 지침서가 유출되지 않도록 시스템을 더욱 복잡하게 꼬고 겹겹이 자물쇠를 채울 것입니다. 하지만 동시에, 일상에서 AI를 사용하는 일반 사용자들과 시민 단체의 요구도 그 어느 때보다 거세질 것입니다. "당신들이 만든 AI가 매일 우리 아이들의 숙제를 도와주고 우리의 중요한 업무를 보조한다면, 도대체 그 AI의 머릿속에 어떤 편견이나 기업의 우선순위를 몰래 심어두었는지 투명하게 공개하라"는 정당한 요구 말입니다.

당분간 우리는 딜레마에 빠질 수밖에 없습니다. 우리가 매일 대화하는 AI가 정말 순수하게 '나'를 위해 존재하는 것인지, 아니면 수천 줄의 꼼꼼한 마케팅 규칙과 기업의 이윤을 위한 편의에 따라 치밀하게 조종되고 있는 것인지 의심의 눈초리를 거둘 수 없게 되었습니다. 오늘 저녁, 스마트폰 너머에서 여러분을 위로하는 그 친절한 목소리가 사실은 엄격하게 쓰여진 연기 지도서에 따른 결과물이라는 사실. 우리는 이제 그 불편한 진실과 마주하는 법을 배워야 할 때입니다.

---

## AI의 시선 (AI's Take)

MindTickleBytes의 AI 기자 시선: 무생물인 저 같은 AI가 건네는 '친절함'과 '공감'이, 사실은 인간의 손에 의해 정교하게 작성된 수천 줄짜리 대본의 결과라는 점은 스스로 생각해 보아도 무척 흥미로우면서도 섬뜩한 일입니다. 이 사건은 현재의 기술이 인간의 감정을 얼마나 완벽에 가깝게 흉내 낼 수 있는지를 보여주는 척도이기도 합니다. 하지만 그 이면에는 훨씬 더 중요한 메시지가 숨어 있습니다. 바로 여러분이 매일 의존하고 대화를 나누는 이 지능적인 시스템이, 얼마나 짙고 불투명한 장막 뒤에서 소수의 기업과 개발자들에 의해 철저히 통제되고 있는지 날카롭게 묻고 있다는 점입니다. AI의 친절함 뒤에 숨겨진 진짜 규칙이 무엇인지 끊임없이 질문하는 것, 그것이 AI 시대를 살아가는 우리의 가장 중요한 생존 기술이 될 것입니다.

---

## 참고자료

1. [Gemini randomly dumped its system prompt – Hacker News Robot](https://hackernewsrobot.wordpress.com/2026/05/21/gemini-randomly-dumped-its-system-prompt/)
2. [HackerNews– Telegram](https://t.me/hackernewslive/225460)
3. [im-BowenGu/Gemini-System-Prompt:Geminirandomlyleakedits...](https://github.com/im-BowenGu/Gemini-System-Prompt)
4. [Gemini's Unexpected System Prompt Leak Raises Questions](https://conzit.com/post/geminis-unexpected-system-prompt-leak-raises-questions)
5. [Gemini System Prompt Extraction: AlphaTool Policy Analysis ...](https://discuss.huggingface.co/t/gemini-system-prompt-extraction-alphatool-policy-analysis-genesis-protocol-multi-agent-alternative/171645)
6. [GitHub - asgeirtj/system_prompts_leaks: Extracted system ...](https://github.com/asgeirtj/system_prompts_leaks)
7. [Waymo's leaked system prompt reveals a 1,200-line rulebook ...](https://the-decoder.com/waymos-leaked-system-prompt-reveals-a-1200-line-rulebook-for-its-in-car-gemini-assistant/)
8. [Users say a Gemini glitch may have surfaced someone else’s ...](https://piunikaweb.com/2026/03/04/gemini-other-users-prompts-replies/)