---
layout: post
title: "AI가 짠 코드는 안 받아요? 인터넷 심장을 지키는 사람들의 선언"
description: "오픈소스 프로젝트 NLnet Labs가 코드와 문서 작성에 AI 사용을 제한하는 새로운 정책을 발표했습니다. 왜 이런 결정을 내렸을까요?"
summary: "인터넷 인프라를 개발하는 비영리 단체 NLnet Labs가 2026년 6월 26일부터 모든 코드와 문서 기여에 대해 '인간의 직접 작성'을 원칙으로 하는 엄격한 AI 사용 정책을 도입했습니다."
tags: [AI, 오픈소스, NLnetLabs, 정책, 인공지능]
image: 2026-06-27-NLNet-Labs-LLM-Policy.jpg
image_alt: "컴퓨터 화면 앞에 앉아 고민하고 있는 사람의 실루엣과 그 뒤로 복잡한 네트워크 구조가 희미하게 그려진 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "인프라의 안정성을 최우선으로 하는 오픈소스 커뮤니티가 기술적 편리함보다 '책임감 있는 출처'를 택한 신중한 행보로 평가됩니다."
quiz:
  - question: "NLnet Labs가 새롭게 도입한 정책의 핵심은 무엇인가요?"
    choices: ["AI 생성 코드 사용 권장", "모든 코드와 문서의 인간 저자 작성 의무화", "모든 AI 도구의 사용 금지"]
    answer: 1
    explanation: "NLnet Labs는 코드와 문서를 기여할 때 인간이 직접 작성해야 한다는 원칙을 명시했습니다."
  - question: "NLnet Labs 프로젝트 기여자들은 AI를 사용했을 경우 어떻게 해야 하나요?"
    choices: ["아무것도 안 해도 됨", "AI 사용 사실을 공개적으로 밝혀야 함", "코드에 표시를 남겨야 함"]
    answer: 1
    explanation: "이슈 제기나 버그 보고, 포럼 게시 시 LLM(대규모 언어 모델) 사용 여부를 반드시 공개해야 합니다."
  - question: "NLnet Labs는 어떤 종류의 프로젝트를 주로 다루나요?"
    choices: ["상업적 게임 개발", "인터넷 인프라(DNS 등)", "개인 블로그 플랫폼"]
    answer: 1
    explanation: "NLnet Labs는 DNS, 라우팅 등 인터넷의 핵심 인프라를 개발하고 연구하는 비영리 단체입니다."
lang: ko
ref: 2026-06-27-NLNet-Labs-LLM-Policy
audio: 2026-06-27-NLNet-Labs-LLM-Policy.mp3
permalink: /2026/06/27/NLNet-Labs-LLM-Policy/
---

상상해보세요. 당신이 매일 사용하는 수도관이 사실은 로봇이 설계한 것인데, 그 로봇이 가끔 엉뚱한 결정을 내려 물의 흐름을 멈추게 한다면 어떨까요? 우리 눈에 보이지 않는 인터넷 세상에도 이런 '수도관' 역할을 하는 기술들이 있습니다. 우리가 접속하는 웹사이트 주소를 숫자로 바꿔주는 DNS(도메인 네임 시스템, 인터넷 주소록 같은 역할) 등이 바로 그것이죠. 그런데 이 중요한 인프라를 만드는 커뮤니티에서 최근 흥미롭고도 단호한 결정이 내려졌습니다.

인터넷 인프라의 근간을 연구하고 개발하는 비영리 단체인 NLnet Labs가 2026년 6월 26일, AI 사용과 관련된 새로운 정책을 발표했습니다. [NLnetLabsrestrictsLLM-generated code and docs | LavX News](https://news.lavx.hu/article/nlnet-labs-restricts-llm-generated-code-and-docs) 그 핵심은 매우 명확합니다. "사람이 직접 써야 한다"는 것이죠.

### 이게 왜 중요한가요?

일상에서 AI가 쓴 이메일이나 보고서를 보는 것은 흔한 일이 되었지만, 인터넷의 심장부를 다루는 곳에서는 이야기가 완전히 다릅니다. 이 정책은 단순한 규칙을 넘어, **'인터넷 인프라의 신뢰'**를 어디까지 인간이 책임질 것인가에 대한 묵직한 화두를 던집니다. [NLnetLabs| lobbyfacts](https://www.lobbyfacts.eu/datacard/nlnet-labs?rid=604493250015-26) 

일반 사용자 입장에서는 당장 인터넷이 느려지는 것은 아니지만, 오픈소스(누구나 코드를 보고 수정할 수 있는 소프트웨어) 생태계가 AI의 거대한 영향 아래에서 어떻게 자신의 정체성을 유지하려 하는지를 보여주는 중요한 사례입니다. 코드는 단순한 명령어가 아니라, 누군가의 깊은 고민이 담긴 정교한 설계도이기 때문입니다.

### 쉽게 이해하기: '기본기'를 확인하는 과정

이렇게 비유해볼까요? 요리사가 손님에게 음식을 대접할 때, 레시피를 AI가 짰는지 사람이 직접 고민했는지는 맛에서 큰 차이가 안 날 수도 있습니다. 하지만 식당의 위생 관리나 식재료의 원산지를 증명하는 '기록지'를 누군가 대신 써준다면 어떨까요? 혹시라도 문제가 생겼을 때, "그 기록은 로봇이 쓴 거라 잘 모른다"고 답변한다면 손님들은 큰 불안을 느낄 것입니다.

이번 NLnet Labs의 결정도 이와 비슷합니다. 코드를 '잘' 짜는 것만큼이나 **'누가 책임지고 작성했는가'**가 인프라 안전성에서는 핵심이기 때문입니다. [NLnet Labs restricts LLM-generated contributions to projects](https://letsdatascience.com/news/nlnet-labs-restricts-llm-generated-contributions-to-projects-0897df70) 

기존의 오픈소스 협업이 '함께 만드는 동료'들의 신뢰에 기반했다면, AI의 등장은 그 신뢰의 대상을 모호하게 만들었습니다. 앞으로 기여자들은 버그를 보고하거나 코드를 제출할 때 AI(대규모 언어 모델, 방대한 데이터를 학습해 문장을 만드는 AI)를 사용했는지 여부를 투명하게 공개해야 합니다. [NLnet Labs restricts LLM-generated contributions to projects](https://letsdatascience.com/news/nlnet-labs-restricts-llm-generated-contributions-to-projects-0897df70)

### 어디까지 제한하나요?

현재 NLnet Labs는 모든 코드, 문서, 그리고 프로젝트 댓글까지 인간이 직접 저술할 것을 요구합니다. [NLnetLabsrestrictsLLM-generated code and docs | LavX News](https://news.lavx.hu/article/nlnet-labs-restricts-llm-generated-code-and-docs) 즉, 기계가 초안을 잡고 사람이 살짝 다듬는 수준조차도 정책적으로는 거부하겠다는 강한 의지입니다.

물론, AI를 무조건 배척하는 것은 아닙니다. 사용했다면 그 사실을 숨기지 말고 정직하게 밝히라는 것이 핵심입니다. [NLnet Labs restricts LLM-generated contributions to projects](https://letsdatascience.com/news/nlnet-labs-restricts-llm-generated-contributions-to-projects-0897df70) 이는 AI 기술 자체의 효율성을 부정하는 것이 아니라, 기술의 산출물에 대한 '인간의 책임감'을 다시금 확인하려는 조치로 이해해야 합니다.

### 앞으로 어떻게 될까?

앞으로 다른 오픈소스 프로젝트들도 이러한 'AI 저자 확인' 정책을 속속 도입할 가능성이 큽니다. 인터넷 인프라처럼 안정성이 무엇보다 중요한 분야일수록 코드가 어떻게 만들어졌는지 추적하고 검증하는 것이 더욱 중요해지기 때문입니다. [NLnet;NLnetLabs](https://nlnet.nl/project/nlnetlabs/) 독자 여러분도 앞으로 오픈소스 소프트웨어를 접하실 때 '이 코드가 인간에 의해 직접 관리되고 있나?'를 눈여겨보는 것이 더욱 중요해질 것입니다.

인터넷이라는 거대한 수도관을 안전하게 관리하려는 이들의 노력이 AI 시대에 어떤 방식으로 진화할지 지켜봐야 할 이유가 여기에 있습니다.

---

## MindTickleBytes의 AI 기자 시선
AI의 효율성은 부인할 수 없지만, 인터넷 인프라처럼 한 번의 오류가 전 세계에 영향을 줄 수 있는 곳에서는 '책임 질 줄 아는 사람'의 자리가 대체 불가능함을 잘 보여줍니다. 효율보다 안전이 우선되는 영역에서 인간의 개입은 앞으로도 더욱 귀한 가치를 지니게 될 것입니다.

---

## 참고자료
1. [NLnetLabsrestrictsLLM-generated code and docs | LavX News](https://news.lavx.hu/article/nlnet-labs-restricts-llm-generated-code-and-docs)
2. [NLnet Labs restricts LLM-generated contributions to projects](https://letsdatascience.com/news/nlnet-labs-restricts-llm-generated-contributions-to-projects-0897df70)
3. [NLnetLabs| lobbyfacts](https://www.lobbyfacts.eu/datacard/nlnet-labs?rid=604493250015-26)
4. [NLnet;NLnetLabs](https://nlnet.nl/project/nlnetlabs/)