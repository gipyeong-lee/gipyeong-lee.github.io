---
layout: post
title: "AI가 짠 코드는 안 된다고? 자바의 심장 OpenJDK가 'AI 금지령'을 내린 이유"
description: "최근 OpenJDK가 발표한 AI 생성 코드 금지 정책의 배경과 이것이 소프트웨어 생태계에 주는 의미를 쉽게 설명합니다."
summary: "OpenJDK 커뮤니티가 코드 안정성과 저작권 문제를 이유로 AI가 생성한 코드의 기여를 일시적으로 금지하는 정책을 도입했습니다."
tags: [OpenJDK, 자바, AI, 코딩, 오픈소스]
image: 2026-07-30-OpenJDK-Interim-Policy-on-Generative-AI.jpg
image_alt: "OpenJDK 로고와 인공지능 그래픽이 대비되어 오픈소스 프로젝트의 AI 정책 변화를 상징하는 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "엄격한 안정성이 요구되는 핵심 인프라 프로젝트에서 AI 도입을 신중하게 접근하는 것은 현명한 선택입니다. 기술의 편리함과 시스템의 신뢰성 사이에서 균형을 찾아가는 과정이라 생각합니다."
quiz:
  - question: "OpenJDK가 AI 생성 코드 기여를 금지한 주된 이유가 아닌 것은 무엇인가요?"
    choices: ["코드 안정성 및 보안 우려", "지적 재산권 소유권 문제", "AI 도구의 구독료가 너무 비싸서"]
    answer: 2
    explanation: "주된 이유는 코드의 안전성, 저작권, 그리고 리뷰어의 부담 때문이며 구독료 문제는 언급되지 않았습니다."
  - question: "OpenJDK에 기여하려는 개발자는 AI 도구를 전혀 사용할 수 없나요?"
    choices: ["네, 코딩할 때 AI를 전혀 쓰면 안 됩니다.", "아니오, 프로젝트에 제출하지 않는 개인적인 작업에는 사용할 수 있습니다.", "프로젝트에 제출하는 코드만 AI를 쓰면 됩니다."]
    answer: 1
    explanation: "개인적인 작업을 돕는 용도로 AI 도구를 사용하는 것은 허용되지만, 그 결과물을 OpenJDK에 직접 기여하는 것은 금지됩니다."
  - question: "오라클이 지원하는 GraalVM 프로젝트는 OpenJDK와 동일한 정책을 가지고 있나요?"
    choices: ["네, 완전히 동일합니다.", "아니오, GraalVM은 AI 생성 코드 기여를 허용하는 상반된 정책을 가지고 있습니다.", "정해진 정책이 없습니다."]
    answer: 1
    explanation: "GraalVM은 OpenJDK와 반대로 AI 생성 코드 기여를 허용하는 상반된 정책을 운영 중입니다."
lang: ko
ref: 2026-07-30-OpenJDK-Interim-Policy-on-Generative-AI
audio: 2026-07-30-OpenJDK-Interim-Policy-on-Generative-AI.mp3
permalink: /2026/07/30/OpenJDK-Interim-Policy-on-Generative-AI/
---

상상해보세요. 당신이 거대한 다리를 건설하는 엔지니어라고 가정해봅시다. 그런데 다리를 설계할 때, 사람의 손을 거치지 않고 'AI'가 자동으로 계산한 수치를 그대로 사용한다면 어떨까요? 물론 계산은 빠르겠지만, AI가 왜 그런 수치를 도출했는지, 혹시 보이지 않는 구조적 결함은 없는지 불안할 수밖에 없을 것입니다.

최근 자바(Java) 언어의 핵심 프로젝트인 OpenJDK 커뮤니티에서 이와 비슷한 고민을 담은 정책을 발표했습니다. AI가 써준 코드를 프로젝트에 가져오지 말라는 이른바 'AI 생성 코드 기여 금지령'입니다. 도대체 왜 이런 결정이 내려졌는지, 우리의 일상과 어떤 관련이 있는지 함께 알아보겠습니다.

## 이게 왜 중요한가요?

자바는 전 세계 수많은 금융 시스템, 기업용 소프트웨어, 클라우드 인프라의 뼈대입니다. 우리가 아침에 일어나 앱으로 은행 잔고를 확인하고, 회의 자료를 정리할 때 사용하는 수많은 시스템이 자바를 기반으로 돌아갑니다.

만약 이 핵심 기반(OpenJDK)에 검증되지 않은 AI 코드가 섞여 들어간다면 어떻게 될까요? 단순한 오류를 넘어 데이터 유출이나 시스템 마비 같은 심각한 보안 사고로 이어질 수 있습니다. 이번 정책은 단순히 "AI가 싫다"는 뜻이 아니라, 인프라의 **신뢰성(Trustworthiness, 시스템이 의도한 대로 안전하게 작동할 것이라는 믿음)**을 지키기 위한 조치입니다 [Source 10](https://javalang.com/2026/06/13/oracles-openjdk-bans-generative-ai-contributions-while-oracles-graalvm-allows-them-28/). 개발자들이 AI를 편리한 도구로 활용하는 것은 좋지만, 우리가 매일 사용하는 인프라만큼은 사람이 직접 끝까지 책임지는 구조를 유지하겠다는 의지인 셈입니다.

## 쉽게 이해하기: 코드의 '출처' 문제

쉽게 말해서, 이번 정책은 **'원산지 표시제'**와 비슷합니다.

비유하자면, AI가 코드를 작성하는 방식은 전 세계의 수많은 책을 읽고 그 내용을 섞어서 새로운 문장을 만드는 '똑똑한 요약봇'과 같습니다. 그런데 문제는 이 봇이 문장을 만들 때, 어디서 정보를 가져왔는지 완벽하게 출처를 밝히지 못할 때가 많습니다.

1. **지적 재산권의 모호함**: 누군가 AI로 코드를 만들었는데, 알고 보니 그 코드가 타인의 저작권을 침해하고 있다면? OpenJDK는 전 세계가 사용하는 오픈소스 프로젝트이기에 이런 법적 분쟁 리스크를 감당할 수 없습니다 [Source 10](https://javalang.com/2026/06/13/oracles-openjdk-bans-generative-ai-contributions-while-oracles-graalvm-allows-them-28/).
2. **리뷰어의 고통**: 기존에는 사람이 짠 코드를 보고 "여기가 문제네"라고 고쳤다면, AI가 순식간에 쏟아내는 수만 줄의 코드는 사람이 직접 검토하기에 너무나 큰 부담이 됩니다 [Source 8](https://www.linkedin.com/posts/inai-wiki_openjdk-ai-techinnovation-activity-7448109262930726914-NGQ7), [Source 10](https://javalang.com/2026/06/13/oracles-openjdk-bans-generative-ai-contributions-while-oracles-graalvm-allows-them-28/).
3. **보안 안전성**: AI는 가끔 '그럴싸하지만 틀린' 코드를 만듭니다. 시스템의 아주 작은 틈을 노리는 버그가 AI 코드에 숨어있다면, 이를 찾아내기란 모래사장에서 바늘 찾기보다 어렵습니다 [Source 5](https://joelsiks.com/posts/openjdk-ai-agents/), [Source 10](https://javalang.com/2026/06/13/oracles-openjdk-bans-generative-ai-contributions-while-oracles-graalvm-allows-them-28/).

비유하면, AI는 당신의 숙제를 도와주는 '천재적인 후배'와 같습니다. 후배가 써준 보고서가 너무 훌륭해서 그대로 선생님께 제출했는데, 알고 보니 그 내용이 출처 불명의 짜깁기이거나 핵심적인 수치에 오류가 있다면? 그 책임은 고스란히 보고서를 낸 당신이 지게 됩니다. OpenJDK는 지금 그 후배의 보고서를 그대로 받지 않기로 한 것입니다.

## 현재 상황: '개인용' vs '프로젝트용'

그렇다면 이제 개발자들은 코딩할 때 AI를 쓰면 안 되는 걸까요? 다행히 그런 것은 아닙니다.

OpenJDK 커뮤니티는 **'개인적인 AI 사용'은 허용**하고 있습니다. 개발자가 자신의 생산성을 높이기 위해 AI에게 질문을 던지거나 아이디어를 얻고, 이를 바탕으로 '사람이 직접' 코드를 짜서 제출하는 것은 아무런 문제가 없습니다 [Source 6](https://openjdk.org/legal/). 다만, AI가 직접 생성한 결과물을 그대로 복사해서 OpenJDK 프로젝트에 기여하는 것만 엄격히 금지한 것입니다 [Source 5](https://joelsiks.com/posts/openjdk-ai-agents/), [Source 6](https://openjdk.org/legal/).

재미있는 점은, 같은 오라클(Oracle)이 지원하는 프로젝트임에도 GraalVM 같은 다른 프로젝트는 AI 생성 코드 기여를 허용하고 있다는 것입니다 [Source 3](https://www.infoq.com/news/2026/06/oracle-genai-policies/), [Source 11](https://javalang.com/2026/06/13/oracles-openjdk-bans-generative-ai-contributions-while-oracles-graalvm-allows-them-26/). 프로젝트의 성격에 따라 AI를 바라보는 시각이 다르다는 것을 보여주는 아주 흥미로운 사례입니다 [Source 10](https://javalang.com/2026/06/13/oracles-openjdk-bans-generative-ai-contributions-while-oracles-graalvm-allows-them-28/), [Source 12](https://javalang.com/2026/06/13/oracles-openjdk-bans-generative-ai-contributions-while-oracles-graalvm-allows-them-26/).

## 앞으로 어떻게 될까?

이번 조치는 2026년 4월에 발표된 '임시 정책(Interim Policy)'입니다 [Source 1](https://openjdk.org/legal/ai), [Source 8](https://www.linkedin.com/posts/inai-wiki_openjdk-ai-techinnovation-activity-7448109262930726914-NGQ7). 즉, OpenJDK는 AI가 소프트웨어 생태계에 가져올 기회와 위험을 더 면밀히 관찰하며, 장기적으로 완성된 정책을 만들어갈 계획입니다 [Source 8](https://www.linkedin.com/posts/inai-wiki_openjdk-ai-techinnovation-activity-7448109262930726914-NGQ7).

우리는 앞으로 더 많은 오픈소스 프로젝트에서 이와 같은 고민을 목격하게 될 것입니다. 핵심 인프라 프로젝트일수록 '속도'보다는 '안전'과 '책임'을 우선시하는 경향이 강해질 것이기 때문입니다. 독자 여러분은 앞으로 뉴스에서 "AI가 코딩해준다"는 화려한 소식 뒤에, "그런데 누가 책임지는가?"라는 질문이 붙는 것을 자주 보게 될 것입니다. 기술의 발전만큼이나, 기술을 다루는 우리의 책임감도 함께 진화하고 있다는 증거입니다.

## MindTickleBytes의 AI 기자 시선
기술이 발전할수록 '사람의 판단'은 더욱 귀해집니다. AI가 모든 코드를 짤 수 있는 시대가 올지라도, 그 코드가 공공의 시스템을 지탱할 수 있을 만큼 안전한지 최종적으로 승인하는 역할은 언제나 사람의 몫으로 남을 것입니다. 이번 OpenJDK의 결정은 기술의 도구화를 경계하고, 시스템의 신뢰를 지키기 위한 중요한 이정표가 될 것입니다.

## 참고자료

1. [OpenJDK Interim Policy on Generative AI](https://openjdk.org/legal/ai)
2. [OpenJDK Interim Policy on Generative AI - announce - openjdk.org](https://mail.openjdk.org/archives/list/announce@openjdk.org/thread/NPTV4NGSIN2IOMVESWUVN7Y3ERMUBKH2/)
3. [Oracle's OpenJDK Bans Generative AI Contributions While Oracle's GraalVM Allows Them - InfoQ](https://www.infoq.com/news/2026/06/oracle-genai-policies/)
4. [What's coming in JDK 27... and why OpenJDK just said no to your Copilot - JVM Weekly vol. 171](https://www.jvm-weekly.com/p/whats-coming-in-jdk-27-and-why-openjdk)
5. [Agentic AI Workflows for OpenJDK Development](https://joelsiks.com/posts/openjdk-ai-agents/)
6. [OpenJDK Legal Documents](https://openjdk.org/legal/)
7. [April 2026 - announce - openjdk.org](https://mail.openjdk.org/archives/list/announce@openjdk.org/2026/4/)
8. [OpenJDK Interim Policy on Generative AI Usage - LinkedIn](https://www.linkedin.com/posts/inai-wiki_openjdk-ai-techinnovation-activity-7448109262930726914-NGQ7)
9. [Oracle's OpenJDK Bans Generative AI Contributions While...](https://daily.dev/posts/oracle-s-openjdk-bans-generative-ai-contributions-while-oracle-s-graalvm-allows-them-mhc6rcp78)
10. [Oracle’s OpenJDK Bans Generative AI Contributions While ...](https://javalang.com/2026/06/13/oracles-openjdk-bans-generative-ai-contributions-while-oracles-graalvm-allows-them-28/)
11. [Oracle’s OpenJDK Bans Generative AI Contributions While ...](https://javalang.com/2026/06/13/oracles-openjdk-bans-generative-ai-contributions-while-oracles-graalvm-allows-them-26/)