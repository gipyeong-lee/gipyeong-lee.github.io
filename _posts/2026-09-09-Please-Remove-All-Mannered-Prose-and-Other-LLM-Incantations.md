---
layout: post
title: "AI가 자꾸 '멋진 척'하며 문장을 꼬아 쓴다면? 딱 한 문장이면 충분합니다"
description: "AI가 불필요한 은유나 화려한 수식어를 남발하는 'AI 말투'를 제거하고 간결하게 답변받는 방법을 소개합니다."
summary: "앤스로픽(Anthropic)이 공식 가이드를 통해 Claude Fable 5.1 모델의 불필요한 수식어와 비유를 제거하는 마법의 명령어 'Please remove all mannered prose'를 공개했습니다."
tags: [AI, 앤스로픽, Claude, 프롬프트엔지니어링, 팁]
image: 2026-09-09-Please-Remove-All-Mannered-Prose-and-Other-LLM-Incantations.jpg
image_alt: "AI가 작성한 복잡하고 화려한 문장들이 지워지고 간결하고 명확한 문장으로 바뀌는 모습을 상징하는 그래픽."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI의 '멋 부리기'는 사용자에게 불필요한 인지 부하를 줍니다. 본질을 가리는 수식어를 제거하는 것은 AI 활용의 기본입니다."
quiz:
  - question: "앤스로픽이 정의한 '매너드 프로즈(mannered prose)'란 무엇인가요?"
    choices: ["AI가 사용하는 기술적인 오류", "필요 이상의 은유와 화려한 수사적 표현이 들어간 글쓰기", "AI가 답변을 거부하는 현상"]
    answer: 1
    explanation: "매너드 프로즈는 간단히 말할 수 있는 내용을 AI가 불필요하게 은유나 화려한 문체로 꾸며서 답변하는 현상을 말합니다."
  - question: "제공된 명령어 'Please remove all mannered prose'는 어디에 넣어야 효과가 있나요?"
    choices: ["개별 질문 끝이나 시스템 프롬프트에 추가", "컴퓨터의 설정 메뉴에 입력", "반드시 코드 블록 안에 입력"]
    answer: 0
    explanation: "해당 명령어는 개별 요청 사항에 포함하거나, AI의 역할을 지정하는 시스템 프롬프트에 추가하여 사용할 수 있습니다."
  - question: "AI가 이 명령어를 제대로 이해하기 위해 반드시 띄어쓰기를 지켜야 하나요?"
    choices: ["네, 띄어쓰기가 필수입니다", "아니오, 띄어쓰기 없이 붙여 써도 효과가 있습니다", "대문자로만 입력해야 합니다"]
    answer: 1
    explanation: "놀랍게도 해당 명령어는 띄어쓰기를 모두 생략한 형태(Pleaseremoveallmanneredprose)로 입력해도 충분히 작동합니다."
lang: ko
ref: 2026-09-09-Please-Remove-All-Mannered-Prose-and-Other-LLM-Incantations
audio: 2026-09-09-Please-Remove-All-Mannered-Prose-and-Other-LLM-Incantations.mp3
permalink: /2026/09/09/Please-Remove-All-Mannered-Prose-and-Other-LLM-Incantations/
---

상상해보세요. 바쁜 아침, AI 비서에게 "오늘 회의 핵심 안건 3개만 정리해줘"라고 부탁했습니다. 그런데 AI가 답변하기를, "오늘의 회의는 마치 거대한 폭풍 전야와 같았습니다. 세 가지 핵심 안건이라는 나침반이 우리의 방향을 안내할 것입니다..."라며 온갖 비유와 수식어를 늘어놓습니다. 본론이 궁금한 사용자는 답답할 노릇이죠.

최근 인공지능 모델들이 이런 'AI스러운 말투' 때문에 사용자들에게 피로감을 주고 있습니다. 앤스로픽(Anthropic)이 최근 발표한 최신 모델 'Claude Fable 5.1' 가이드에서, 이런 문제를 해결할 수 있는 의외로 간단한 해결책을 공식적으로 제시했습니다.

## 이게 왜 중요한가요?

우리가 AI를 사용하는 가장 큰 이유는 '효율성'입니다. 하지만 AI가 사람처럼 보이고 싶어 과도한 비유를 섞거나, 문장을 불필요하게 꼬아서 쓰면 정작 중요한 정보를 찾기가 어려워집니다. [Source 13](https://vibecoding.ru/news/2026/09/03/anthropic-mannered-prose-prompt)에 따르면, AI가 사용하는 이러한 화려한 문체는 저자가 선택하지 않은 의미까지 끌어들이며, 독자는 굳이 할 필요 없는 해석 작업을 수행해야 하는 불필요한 수고를 하게 됩니다. 이번 공식 가이드는 사용자가 AI를 더 똑똑하고 간결하게 사용할 수 있는 권한을 돌려주었다는 점에서 의미가 큽니다.

## 쉽게 이해하기

앤스로픽은 이러한 현상을 '매너드 프로즈(Mannered Prose)'라고 명명했습니다. [Source 4](https://x.com/MaxForAI/status/2095131767229517917) 쉽게 말해, 한마디로 깔끔하게 정리할 수 있는 내용을 AI가 굳이 은유법이나 미사여구를 동원해 '멋진 척'하며 길게 늘어뜨리는 글쓰기 습관을 뜻합니다.

앤스로픽의 개발진은 Claude Fable 5.1이 이전 모델보다 나아졌음에도 불구하고, 여전히 때로는 문장이 너무 길고 복잡하다는 점을 인정했습니다. [Source 4](https://x.com/MaxForAI/status/2095131767229517917) 그래서 그들은 이 'AI 말투'를 제거하기 위해 마법 같은 명령어 하나를 공식 문서에 추가했습니다. 

바로 **"Please remove all mannered prose(모든 매너드 프로즈, 즉 과도하게 꾸며진 문체를 제거해 주세요)"**라는 문장입니다. [Source 1](https://matthewritch.com/blog/2026/09/08/Mannered-Prose-Style-Prompts/)

비유하자면 이렇습니다. AI는 지금 '기본 예절 교육'은 마쳤지만, 이제 막 '문학 수업'을 듣고 와서 모든 대답에 시적인 표현을 섞고 싶어 하는 상태입니다. 이 명령어는 AI에게 "예술가는 그만하고, 이제 비서의 본업에 집중해!"라고 말해주는 강력한 스위치인 셈입니다.

## 현재 상황

현재 이 프롬프트는 매우 효과적인 것으로 평가받고 있습니다. [Source 5](https://paddo.dev/blog/a-dial-worth-turning/) 사용자들은 이 명령어를 질문 끝에 붙이거나, 아예 AI에게 미리 지시를 내리는 '시스템 프롬프트'에 넣어두기만 해도 AI의 말투가 몰라보게 간결해지는 것을 확인했습니다. [Source 6](https://x.com/Voxyz_ai/status/2095260094795583807), [Source 11](https://t.me/dailyprompts/9362)

심지어 더 놀라운 것은, AI가 이 문장의 의미를 너무나 잘 이해하고 있기 때문에 띄어쓰기를 다 무시하고 'Pleaseremoveallmanneredprose'라고 붙여 써도 똑똑하게 알아듣고 화려한 수식어를 걷어낸다는 점입니다. [Source 9](https://apidog.com/blog/prompting-claude-fable-5-1/), [Source 13](https://vibecoding.ru/news/2026/09/03/anthropic-mannered-prose-prompt)

## 앞으로 어떻게 될까?

앞으로 AI 서비스들은 사용자가 직접 이런 '말투 고치기' 명령어를 입력하지 않아도 되도록 개선될 것입니다. 앤스로픽의 이번 가이드 업데이트는 AI 기업들이 사용자의 목소리에 귀를 기울이고, AI의 지능뿐만 아니라 '의사소통의 효율성'까지 고민하고 있다는 신호입니다. 

이제 AI에게 "말 예쁘게 하지 말고, 딱 핵심만 말해줘"라고 번거롭게 설명할 필요가 없습니다. 저 문장 하나면 여러분의 AI 비서는 훨씬 유능한 비즈니스 파트너로 변신할 것입니다.

## MindTickleBytes의 AI 기자 시선

AI가 인간처럼 말을 잘하게 된 것은 기술적인 성취이지만, 비즈니스 환경에서 가장 가치 있는 능력은 여전히 '명확한 정보 전달'입니다. 앤스로픽이 직접 이 문제를 해결하는 프롬프트를 공개한 것은, AI가 스스로를 절제할 수 있는 능력이 AI 기술의 진정한 성숙도를 가늠하는 척도가 되고 있음을 보여줍니다. 

## 참고자료

1. [Matthew Ritch, "Please Remove All Mannered Prose" and Other LLM Incantations](https://matthewritch.com/blog/2026/09/08/Mannered-Prose-Style-Prompts/)
2. [Ian Nuttall, "A prompt to stop Claude from speaking in parseltongue"](https://x.com/iannuttall/status/2095203215734178066)
3. [Max For AI, "有意思，Anthropic亲自下场教你怎么去掉Claude味了"](https://x.com/MaxForAI/status/2095131767229517917)
4. [Paddo, "A Dial Worth Turning: Claude Opus 5's Prose, and the Style Guide Anthropic Wrote Against Its Own Model"](https://paddo.dev/blog/a-dial-worth-turning/)
5. [Vox, "You removed the “It’s not X, it’s Y” lines. 𝗜𝘁 𝘀𝘁𝗶𝗹𝗹 𝗿𝗲𝗮𝗱𝘀 𝗹𝗶𝗸𝗲 𝗔𝗜."](https://x.com/Voxyz_ai/status/2095260094795583807)
6. [HN blogs - 8/9/26](https://hnblogs.substack.com/p/hn-blogs-8926)
7. [APIDog, "Prompting Claude Fable 5.1: Every Behavior Shift and the Line That..."](https://apidog.com/blog/prompting-claude-fable-5-1/)
8. [Telegram, "@dailyprompts"](https://t.me/dailyprompts/9362)
9. [Dzen, "Гайд по созданию промптов в Fable 5.1"](https://dzen.ru/a/apkFgUgF0B8ig_B6)
10. [Vibecoding, "Вычурность из текстов Claude убирает одна строка"](https://vibecoding.ru/news/2026/09/03/anthropic-mannered-prose-prompt)
11. [VC.ru, "Вышел Claude Fable 5.1 - я уже потестила"](https://vc.ru/chatgpt/3117274-obzor-fable-5-1-ot-anthropic-i-ozhidaniya-ot-astra-ot-openai)