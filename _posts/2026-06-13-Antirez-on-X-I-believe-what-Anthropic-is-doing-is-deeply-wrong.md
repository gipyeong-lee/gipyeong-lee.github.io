**Refining Content for Publication**

I'm now polishing the draft, ensuring it's accessible and engaging for a non-technical audience. I'm focusing on expanding explanations, adding transitional elements, and weaving in the necessary analogies to meet the length requirements.

**Refining for Audience Accessibility**

I am now focusing on enhancing the draft's clarity and flow, particularly by elaborating on existing concepts and adding smoother transitions. My objective is to ensure the information is easily digestible and engaging for a broad, non-technical audience, incorporating the necessary elements for comprehensive understanding.

**Refining Text for Clarity**

I'm currently polishing the draft, focusing on enhancing the flow and expanding explanations for a non-technical audience. My objective is to ensure the information is easily understandable and engaging, incorporating necessary elements to meet the length requirements.

permalink: /2026/06/13/Antirez-on-X-I-believe-what-Anthropic-is-doing-is-deeply-wrong/
---
layout: post
title: "안전일까, 견제일까? 앤스로픽의 '과도한 검열'에 전 세계 개발자들이 분노한 이유"
description: "챗GPT의 강력한 라이벌 앤스로픽이 새로운 AI 모델에 과도한 안전 필터를 적용했다가 개발자들의 거센 비판을 받았습니다. 오픈소스 견제 논란까지 일어난 이번 사건의 전말을 알기 쉽게 정리해 드립니다."
summary: "앤스로픽이 AI 연구와 관련된 질문을 일부러 회피하도록 새 모델을 설계했다가 생태계의 반발에 부딪혀 정책을 철회했지만, 신뢰도에 큰 타격을 입었습니다."
tags: [Anthropic, 앤스로픽, AI안전, 오픈소스, Antirez, AI트렌드]
image: 2026-06-13-Antirez-on-X-I-believe-what-Anthropic-is-doing-is-deeply-wrong.jpg
image_alt: "거대한 자물쇠가 채워진 로봇의 머리를 바라보며 답답해하는 사람들의 모습을 그린 일러스트"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI의 '안전'이라는 숭고한 명분이 경쟁자를 배제하기 위한 교묘한 도구로 변질되지 않도록, 기술 통제에 대한 투명한 기준과 감시가 그 어느 때보다 필요한 시점입니다."
quiz:
  - question: "앤스로픽이 새로운 모델에서 사이버 보안이나 화학 관련 질문을 받았을 때 취한 조치는 무엇인가요?"
    choices: ["질문자의 계정을 즉각 정지했다", "성능이 더 낮은 모델로 질문을 우회시켰다", "정부 기관에 관련 데이터를 전송했다"]
    answer: 1
    explanation: "앤스로픽은 사용자가 생물학 무기를 만들거나 사이버 공격을 계획하는 것을 막기 위해, 관련 질문이 들어오면 성능이 떨어지는 덜 똑똑한 모델로 질문을 우회(rerouting)시켰습니다."
  - question: "유명 개발자 안티레즈(Antirez)가 앤스로픽을 비판한 주된 이유는 무엇인가요?"
    choices: ["모델의 월 구독료가 너무 비싸서", "LLM 연구나 의학적 질문과 같은 무해한 작업까지 막는 과도한 필터링 때문에", "AI가 답변을 생성하는 속도가 너무 느려서"]
    answer: 1
    explanation: "안티레즈는 무해한 AI 연구나 단순한 의학적 질문조차 차단해버리는 앤스로픽의 극도로 민감한 필터가 '근본적으로 잘못되었다'고 강하게 지적했습니다."
  - question: "개발자들의 거센 반발 이후 앤스로픽은 어떤 대처를 했나요?"
    choices: ["자신들이 '잘못된 균형'을 잡았다고 인정하고 정책을 철회했다", "더욱 강력한 검열을 예고하며 맞섰다", "오픈소스 모델 개발을 전면 지원하겠다고 발표했다"]
    answer: 0
    explanation: "앤스로픽은 새로운 안전장치에 대해 '잘못된 균형(tradeoff)을 잡았다'고 인정하며 연구자들을 방해하던 정책을 철회했지만, 신뢰도에는 이미 큰 타격을 입었습니다."
lang: ko
ref: 2026-06-13-Antirez-on-X-I-believe-what-Anthropic-is-doing-is-deeply-wrong
---

상상해보세요. 주말에 짬을 내어 도서관에 방문했습니다. 화학이나 최신 컴퓨터 과학에 대한 전문 서적을 빌려서 깊이 있게 공부하려고 하는데, 갑자기 도서관 사서가 앞을 가로막습니다. 사서는 진지한 표정으로 "당신이 이 지식을 이용해 사제 폭탄을 만들거나 국가 기관을 해킹할지도 모르니, 이 책은 빌려줄 수 없습니다"라고 말합니다. 그러고는 대신 유치원생들이 읽는 얇은 과학 동화책을 건네줍니다. 정말 황당하고 불쾌한 상황이겠죠? 내가 범죄를 저지른 것도 아닌데 잠재적 범죄자 취급을 받은 셈이니까요.

최근 전 세계 인공지능(AI) 업계에서 이와 똑같은 일이 벌어졌습니다. 챗GPT(ChatGPT)를 만든 오픈AI(OpenAI)의 가장 강력한 라이벌이자, 스스로 '가장 안전한 AI'를 만든다고 자부해 온 기업 **앤스로픽(Anthropic)** 이 그 주인공입니다. 앤스로픽이 새롭게 내놓은 AI 모델이 AI 연구나 특정 전문 분야에 대한 질문에 일부러 '바보같이' 대답하도록 설계되어 있었다는 사실이 밝혀졌기 때문입니다. 

이로 인해 유명 개발자들을 포함한 전 세계 AI 연구자들이 크게 분노했고, 결국 앤스로픽이 백기를 들고 한발 물러서는 거대한 해프닝이 발생했습니다. 과연 실리콘밸리를 뜨겁게 달군 이 '안전 검열' 논란의 전말은 무엇일까요? 왜 개발자들은 이토록 분노했을까요?

## 이게 왜 중요한가요? : 도구가 나의 가능성을 제한할 때

오늘날 AI는 단순한 대화형 챗봇을 훨씬 넘어서고 있습니다. 뛰어난 프로그래머들의 복잡한 코드 작성을 돕고, 과학자들의 방대한 논문 분석을 보조하며, 새로운 아이디어를 떠올리게 하는 강력한 '지적 파트너'이자 '동료'로 자리 잡았습니다. 특히 많은 IT 전문가들은 기존의 AI 모델을 활용해 또 다른 AI 기술을 연구하고 발전시키는 이른바 'AI로 AI를 만드는' 연구를 일상적으로 수행하고 있습니다.

그런데 이 AI를 개발하고 서비스하는 거대 기업이 "안전"이라는 명분 아래, 사용자가 AI를 활용해 새로운 연구를 하거나 한계점을 탐구하는 것 자체를 원천적으로 차단해 버린다면 어떤 일이 발생할까요? 도구가 사용자의 가능성을 무한히 확장해 주는 것이 아니라, 반대로 사용자가 할 수 있는 일의 범위를 거대 기업의 입맛대로 엄격하게 제한하게 되는 것입니다.

더 큰 문제는 숨은 의도에 대한 강한 의심입니다. 이번 사건은 단순히 "AI가 내 질문에 답변을 거부해서 불편하다"는 1차원적인 불만을 넘어섰습니다. 전 세계 기술 커뮤니티는 거대 AI 기업인 앤스로픽이 '안전'이라는 겉보기에 그럴듯하고 숭고한 명분을 내세워, 사실은 다른 경쟁자들의 성장을 막으려 한 것이 아니냐고 의심합니다. 구체적으로는 오픈소스(Open Source, 누구나 무료로 코드를 보고 수정할 수 있게 공개된 소프트웨어) 진영이나 독립적인 연구자들이 기술을 발전시키는 것을 교묘하게 방해하려 한 것은 아닌지 강한 의심의 눈초리를 보내고 있습니다. [Why Anthropic Freaked Out the AI Industry This Week - Business Insider](https://www.businessinsider.com/anthropic-freaked-out-ai-industry-mythos-fable-open-source-models-2026-6) 

즉, 개발자들은 "이 검열이 정말 우리를 위험으로부터 지키려는 것인가, 아니면 앤스로픽 자신들의 독점적 시장 지위를 지키려는 것인가?"라는 근본적인 질문을 던지기 시작한 것입니다.

## 쉽게 이해하기: '안전'이라는 이름의 족쇄와 '우회(Rerouting)'

이 상황을 이해하기 위해 다른 비유를 하나 더 들어보겠습니다. 쉽게 말해서, 당신이 엄청난 운전 실력을 뽐낼 수 있는 최첨단 자율주행 스포츠카를 샀다고 가정해 봅시다. 당신은 안전이 확보된 텅 빈 레이싱 서킷에서 운전 연습을 하려고 왼쪽으로 핸들을 꺾습니다. 그런데 자동차가 갑자기 "왼쪽으로 꺾으면 보행자를 칠 위험이 있습니다"라며 임의로 엔진 출력을 대폭 줄여버리고 핸들을 강제로 잠가버린다면 어떨까요? 사고를 막겠다는 명분이지만, 정작 서킷에서의 정상적인 주행조차 불가능하게 만든 셈입니다.

앤스로픽이 최근 출시한 '미토스(Mythos)' 기반의 새로운 모델들에서 바로 이런 황당한 일이 일어났습니다. 이 모델들은 충격적이게도 거대언어모델(LLM, 대규모 텍스트 데이터를 학습해 사람처럼 문장을 이해하고 대화하는 AI 기술) 자체에 대한 연구를 돕는 데 있어 일부러 성능을 떨어뜨리고 제대로 된 답변을 하지 못하도록 설계되어 있었습니다. [Anthropic purposely made its new Mythos-based models bad at AI research, and developers are fuming](https://www.businessinsider.com/researchers-furious-anthropic-mythos-fable-hidden-ai-limits-2026-6) 

도대체 왜 이런 극단적인 조치를 취했을까요? 앤스로픽의 공식적인 해명에 따르면, 이는 철저히 '인류의 안전'을 위한 조치였습니다. 악의적인 해커나 테러리스트가 똑똑한 AI를 이용해 사이버 공격을 정교하게 계획하거나, 치명적인 생물학 무기를 합성해 내는 끔찍한 사태를 미연에 완벽하게 방지해야 한다는 것입니다. 

이를 위해 앤스로픽은 모델 내부에 일종의 깐깐한 '비밀 문지기'를 두었습니다. 만약 사용자가 사이버 보안, 생물학, 화학과 관련된 조금이라도 민감한 질문을 던지면, 이 문지기가 질문을 중간에 가로챕니다. 그러고는 대답을 논리적으로 잘하는 똑똑한 메인 AI 모델이 아니라, 그보다 훨씬 지능이 떨어지는 '덜 똑똑한(less capable)' 모델로 질문을 우회(rerouting)하도록 시스템을 구축했습니다. [Anthropic Says 'We Made the Wrong Tradeoff' in New Model Guardrails - Business Insider](https://www.businessinsider.com/anthropic-mythos-made-wrong-tradeoff-new-model-guardrails-llm-development-2026-6)

문제는 이 '안전 필터'가 촘촘해도 너무 촘촘했다는 점입니다. 사용자가 폭탄 제조법이나 치명적인 바이러스 합성법을 물어본 것이 아니라, 정상적인 컴퓨터 프로그래밍 기법이나 AI 모델의 기초적인 작동 원리, 심지어 일상적인 의학 질문을 할 때조차 이 문지기가 과민 반응을 보였습니다. 그 결과 AI가 답변을 거부하거나, 맥락에 전혀 맞지 않는 엉뚱하고 유치한 대답을 내놓는 현상이 일상적으로 발생하게 된 것입니다. 빈대 잡으려다 초가삼간을 다 태워버린 격입니다.

## 현재 상황: 분노한 개발자들, 결국 꼬리를 내린 앤스로픽

이러한 앤스로픽의 과도한 통제 사실이 알려지자 개발자 커뮤니티는 그야말로 폭발했습니다. 특히 전 세계 수많은 대기업들이 핵심 시스템으로 사용하는 데이터베이스 소프트웨어인 '레디스(Redis)'의 창시자이자 업계에서 널리 존경받는 개발자인 안티레즈(Antirez)는 소셜 미디어 X(옛 트위터)를 통해 앤스로픽을 향해 날 선 비판을 가하며 여론에 불을 지폈습니다.

그는 "거대언어모델(LLM) 연구와 같은 전혀 무해한 작업들조차 할 수 없도록 막고, 심지어 의학적 질문조차 자주 차단될 정도로 극도로 민감한 필터를 두는 앤스로픽의 현재 행태는 **근본적으로(deeply) 잘못되었다**"고 일갈했습니다. [I believe what Anthropic is doing, gating the ability to do ...](https://x.com/antirez/status/2064766431531532588) 이는 단순한 서비스 품질에 대한 불만의 표현을 넘어, 특정 소수 기업이 기술 발전의 방향을 입맛대로 재단하려는 태도 자체에 대한 철학적인 비판이었습니다. 

사실 안티레즈의 비판은 이번이 처음이 아닙니다. 그는 이전에도 앤스로픽의 '소넷(Sonnet) 3.7' 모델을 향해 AI가 인간의 도덕적 기준이나 의도에 맞게 행동하도록 조정하는 '정렬(alignment)' 과정에 심각한 오류가 있으며, 제품 출시가 너무 성급하게 이루어졌다고 강하게 비판한 바 있습니다. [Redis Creator Antirez Criticizes Anthropic’s Sonnet 3.7 AI ...](https://digialps.com/redis-creator-antirez-criticizes-anthropics-sonnet-3-7-ai-feels-rushed/)

안티레즈를 비롯한 수많은 글로벌 연구자들의 분노는 단순히 'AI 사용이 불편해졌다'는 수준에서 멈추지 않았습니다. 비판의 화살은 앤스로픽의 진정한 숨은 의도를 향해 정조준되었습니다. 앤스로픽이 '인류 보호와 안전'이라는 거대한 방패 뒤에 숨어서, 사실은 외부의 독립적인 개발자들이나 오픈소스 AI 생태계가 자신들과 경쟁할 수 있을 만큼 빠르게 발전하는 것을 고의로 막으려는 이기적인 목적이 아니냐는 짙은 의혹이 제기된 것입니다. [Why Anthropic Freaked Out the AI Industry This Week - Business Insider](https://www.businessinsider.com/anthropic-freaked-out-ai-industry-mythos-fable-open-source-models-2026-6) 

미국의 대형 온라인 커뮤니티 레딧(Reddit)의 'ClaudeAI(앤스로픽의 AI 서비스 이름)' 게시판에서도 앤스로픽을 향한 실망감과 조롱이 쏟아졌습니다. 일부 유저들은 앤스로픽을 가리켜 맹목적인 믿음을 강요하는 "사이비 종교 같은 회사(cult company)"라고 원색적으로 비난하며, "앤스로픽은 더 이상 평범하고 투명한 회사가 아니다"라는 강한 불신을 드러냈습니다. 초창기에 상업성을 배제하고 오직 인간을 위한 안전한 AI를 만들겠다며 혜성처럼 등장했던 그들의 맑은 초심이 퇴색되었다는 뼈아픈 목소리였습니다. [r/ClaudeAI on Reddit: Anthropic is not a normal company](https://www.reddit.com/r/ClaudeAI/comments/1tybrpv/anthropic_is_not_a_normal_company/)

이처럼 기술 업계 전반의 반발이 걷잡을 수 없이 커지며 불매 운동 조짐까지 보이자, 굳건하던 앤스로픽도 결국 두 손을 들 수밖에 없었습니다. 그들은 공식적인 입장을 내고 새로운 모델에 적용했던 강력한 안전장치에 대해 "우리가 잘못된 균형(tradeoff)을 잡았다"고 깨끗하게 인정했습니다. [Anthropic Says 'We Made the Wrong Tradeoff' in New Model Guardrails - Business Insider](https://www.businessinsider.com/anthropic-mythos-made-wrong-tradeoff-new-model-guardrails-llm-development-2026-6) 안보와 통제를 지나치게 강조한 나머지, 고객들의 정당하고 창의적인 활용까지 망쳐버렸다는 것을 시인한 것입니다. 결국 앤스로픽은 AI 연구자들의 정당한 연구 활동을 노골적으로 방해하던 해당 정책을 부랴부랴 철회하며 급하게 사태 수습에 나섰습니다. [r/ClaudeAI on Reddit: Anthropic Walks Back Policy That Could Have ‘Sabotaged’ AI Researchers Using Claude](https://www.reddit.com/r/ClaudeAI/comments/1u2nenw/anthropic_walks_back_policy_that_could_have/)

## 앞으로 어떻게 될까? : 잃어버린 신뢰의 무게

개발자들의 거센 항의에 부딪힌 앤스로픽의 백기 투항으로 논란이 되었던 모델 검열 정책은 다행히 이전 상태로 되돌려졌습니다. 하지만 이미 엎질러진 물이었습니다. 업계 전문가들과 연구자들 사이에서는 이번 일로 인해 앤스로픽에게 가장 치명적이고 무형적인 손실이 발생했다고 입을 모읍니다. 바로 '신뢰(Trust)'입니다. 

창립 이래 줄곧 "우리는 다른 빅테크와 달리 투명하고 안전하며 신뢰할 수 있는 윤리적인 기업"이라고 스스로 외쳐왔던 앤스로픽의 명성에, 이번 사태로 돌이킬 수 없는 거대한 타격(massive hit)이 입혀졌다는 것이 현재 실리콘밸리와 기술 생태계의 전반적인 합의(consensus)입니다. [r/ClaudeAI on Reddit: Anthropic Walks Back Policy That Could Have ‘Sabotaged’ AI Researchers Using Claude](https://www.reddit.com/r/ClaudeAI/comments/1u2nenw/anthropic_walks_back_policy_that_could_have/)

이번 앤스로픽 사태는 단순히 한 기업의 기술적 실수를 넘어, AI 산업 전체에 아주 중요하고 무거운 질문을 던지고 있습니다. 앞으로 AI 기술은 우리가 상상하는 것 이상으로 더욱 똑똑해지고 사회 전반에 강력한 영향을 미칠 것입니다. 그렇다면 기술 기업들은 범죄나 테러에 악용되는 것을 막기 위한 '대중을 위한 필수적인 안전장치'와, 시장을 독점하고 오픈소스 등 잠재적 경쟁자의 싹을 자르기 위한 '비윤리적인 기술 견제' 사이의 경계선을 대체 어떻게 설정해야 할까요?

자칫하면 소수의 거대 자본을 가진 AI 기업들이 '세상을 위험으로부터 보호하겠다'는 명분을 내세워, 인류의 지식과 정보 접근 권한을 자기들 마음대로 통제하는 '디지털 검열관'이자 '독재자'가 될 수도 있습니다. 앞으로 우리는 기업들이 얼마나 똑똑하고 신기한 AI를 만들어 내는지 감탄하는 것을 넘어서야 합니다. 그들이 손에 쥔 거대한 권력을 어떻게 행사하고, 그 안전 필터가 정말 투명하고 공정하게 작동하는지 매의 눈으로 감시해야 할 새로운 과제를 안게 되었습니다.

## AI의 시선

기술은 본질적으로 중립적이지만, 그 기술의 한계를 설정하고 제어하는 정책은 다분히 인간적이며 때로는 기업의 이기적인 목적이 개입될 수 있습니다. AI의 '안전'이라는 숭고한 명분이 잠재적인 경쟁자를 배제하고 생태계의 발전을 가로막기 위한 교묘한 도구로 변질되지 않도록 경계해야 합니다. 기술이 소수에게 독점되는 것을 막기 위해서는, 기업이 임의로 정하는 통제 방식에 대해 투명한 기준을 요구하고 사회 전체가 참여하는 다각적인 감시가 그 어느 때보다 필요한 시점입니다.

## 참고자료
1. [Why Anthropic Freaked Out the AI Industry This Week - Business Insider](https://www.businessinsider.com/anthropic-freaked-out-ai-industry-mythos-fable-open-source-models-2026-6)
2. [Anthropic purposely made its new Mythos-based models bad at AI research, and developers are fuming](https://www.businessinsider.com/researchers-furious-anthropic-mythos-fable-hidden-ai-limits-2026-6)
3. [Anthropic Says 'We Made the Wrong Tradeoff' in New Model Guardrails - Business Insider](https://www.businessinsider.com/anthropic-mythos-made-wrong-tradeoff-new-model-guardrails-llm-development-2026-6)
4. [I believe what Anthropic is doing, gating the ability to do ...](https://x.com/antirez/status/2064766431531532588)
5. [Redis Creator Antirez Criticizes Anthropic’s Sonnet 3.7 AI ...](https://digialps.com/redis-creator-antirez-criticizes-anthropics-sonnet-3-7-ai-feels-rushed/)
6. [r/ClaudeAI on Reddit: Anthropic is not a normal company](https://www.reddit.com/r/ClaudeAI/comments/1tybrpv/anthropic_is_not_a_normal_company/)
7. [r/ClaudeAI on Reddit: Anthropic Walks Back Policy That Could Have ‘Sabotaged’ AI Researchers Using Claude](https://www.reddit.com/r/ClaudeAI/comments/1u2nenw/anthropic_walks_back_policy_that_could_have/)