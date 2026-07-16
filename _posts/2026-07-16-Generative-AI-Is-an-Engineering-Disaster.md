---
layout: post
title: "수조 원 쏟아부은 AI, 사실은 '엔지니어링 재앙'인가요?"
description: "기업들이 수조 원을 투자한 생성형 AI가 정작 왜 수익을 내지 못하고 실패하는지, 엔지니어링 관점에서 쉽게 설명합니다."
summary: "생성형 AI는 경제·엔지니어링 측면에서 효율성이 낮으며, 기업 도입 시도 중 95%가 성과를 내지 못하고 있습니다."
tags: [AI, 생성형AI, 기술트렌드, IT]
image: 2026-07-16-Generative-AI-Is-an-Engineering-Disaster.jpg
image_alt: "거대한 데이터 센터의 서버실 앞에서 길을 잃은 듯 고민하는 엔지니어의 모습"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "막대한 자본과 기대가 기술적 현실과 충돌하는 시기입니다. 이제는 효율성을 검증하는 냉철한 접근이 필요한 때입니다."
quiz:
  - question: "기사에서 생성형 AI가 효율성이 낮다고 지적받는 결정적인 이유는 무엇인가요?"
    choices: ["전력 소모와 낮은 확장성", "인터넷 속도 부족", "개발자 부족"]
    answer: 0
    explanation: "생성형 AI는 모델 학습에 엄청난 전력이 소모되며, 경제적 규모의 경제 효과를 누리지 못하는 등 엔지니어링적으로 확장 효율이 매우 낮습니다."
  - question: "2025년 MIT 보고서에 따르면, 기업들의 생성형 AI 시도 중 몇 퍼센트가 실질적인 성과를 내지 못했나요?"
    choices: ["5%", "50%", "95%"]
    answer: 2
    explanation: "2025년 MIT 보고서에 따르면 기업들이 시도한 생성형 AI 프로젝트의 95%가 투자 대비 의미 있는 수익 성장을 거두지 못한 것으로 나타났습니다."
  - question: "전통적인 기술(전구, 자동차 등)과 생성형 AI의 가장 큰 차이점은 무엇인가요?"
    choices: ["기술적 복잡성", "규모의 경제 달성 여부", "사용자 수"]
    answer: 1
    explanation: "전통 기술은 규모의 경제를 통해 생산 단가를 낮추어 대중화에 성공했으나, 생성형 AI는 규모가 커질수록 효율적인 비용 구조를 만드는 데 어려움을 겪고 있습니다."
lang: ko
ref: 2026-07-16-Generative-AI-Is-an-Engineering-Disaster
audio: 2026-07-16-Generative-AI-Is-an-Engineering-Disaster.mp3
permalink: /2026/07/16/Generative-AI-Is-an-Engineering-Disaster/
---

상상해보세요. 여러분이 어떤 제품을 대량으로 생산할수록 가격이 더 비싸지고, 공장을 돌릴 때마다 지구 반대편 도시 하나가 며칠 동안 쓸 전기를 한꺼번에 써버린다면 어떨까요? 아마 대부분은 '이건 공학적으로 잘못 설계된 거야!'라고 말할 것입니다. 그런데 지금 전 세계 IT 업계가 수조 원을 쏟아붓고 있는 생성형 AI(Generative AI, 텍스트나 이미지 등을 스스로 생성하는 AI)가 바로 그런 길을 걷고 있다는 비판이 나오고 있습니다.

최근 업계에서는 생성형 AI를 두고 '수조 달러 규모의 엔지니어링 재앙'이라는 극단적인 평가까지 등장했습니다([출처: The Atlantic](https://www.theatlantic.com/technology/2026/07/generative-ai-engineering-disaster/687901/)). 도대체 무슨 일이 벌어지고 있는 걸까요?

## 이게 왜 중요한가요?

그동안 우리는 생성형 AI가 모든 업무를 자동화하고 엄청난 생산성을 가져다줄 것이라는 장밋빛 미래를 그려왔습니다. 하지만 현실은 생각보다 냉혹합니다. 기업들은 막대한 비용을 들여 AI를 도입하고 있지만, 실제 업무 현장에서는 눈에 띄는 수익이나 생산성 향상을 체감하지 못하는 경우가 허다합니다.

이는 단순히 '기술이 아직 덜 성숙해서'의 문제가 아닙니다. AI를 유지하고 발전시키는 데 드는 비용이 기술적 가치를 넘어설 정도로 비효율적이라는 지적이 나오기 시작했기 때문입니다. 우리가 매일 쓰는 스마트폰 앱이나 웹 서비스처럼, AI가 우리 생활 깊숙이 아주 저렴하게 녹아들 수 있을지에 대해 심각한 의문이 제기된 상태입니다([출처: The Atlantic](https://www.theatlantic.com/technology/2026/07/generative-ai-engineering-disaster/687901/), [출처: Gary Marcus](https://x.com/GaryMarcus/status/2077275136701481375)).

## 쉽게 이해하기: 왜 비효율적인가요?

쉽게 비유하자면, 생성형 AI의 학습 방식은 아주 정교한 '거대한 필터'를 만드는 것과 같습니다. 여러분이 사진 앱에서 예쁜 필터를 고를 때마다 사진 속 데이터들이 조금씩 수정되죠? AI 모델도 수십억 개의 매개변수(Parameter, AI가 데이터를 처리하며 값을 조정하는 일종의 내부 설정값)를 가지고 이 필터 과정을 아주 정교하게 수행합니다([출처: MIT News](https://news.mit.edu/2025/explained-generative-ai-environmental-impact-0117)).

문제는 이 필터를 훈련시키는 비용입니다. 전구, 자동차, 옷 같은 공산품들은 생산을 많이 할수록 '규모의 경제(Economy of Scale)' 덕분에 단가가 저렴해집니다. 공장을 한 번 잘 세워두면 이후 제품은 훨씬 싸게 만들 수 있죠. 하지만 생성형 AI는 반대입니다. 모델의 규모를 키우면 키울수록 필요한 전력과 연산 능력이 기하급수적으로 늘어납니다([출처: The Atlantic](https://www.theatlantic.com/technology/2026/07/generative-ai-engineering-disaster/687901/)).

한 AI 연구자는 "다른 어떤 실제 소프트웨어 제품이 이렇게 비효율적으로 확장되는지 이름을 댈 수 있는 사람이 없다"고 말할 정도입니다([출처: AI Weekly](https://aiweekly.co/alerts/reisner-generative-ai-is-a-trillion-dollar-engineering-disaster)).

## 현재 상황: 95%의 실패

상황은 생각보다 심각합니다. 2025년 MIT에서 발표한 연구에 따르면, 기업들이 진행한 생성형 AI 관련 프로젝트 중 무려 **95%**가 투자 대비 실질적인 수익이나 성과를 내지 못하고 실패한 것으로 드러났습니다([출처: The Economic Times](https://economictimes.indiatimes.com/magazines/panache/mit-study-shatters-ai-hype-95-of-generative-ai-projects-are-failing-sparking-tech-bubble-jitters/articleshow/123428252.cms), [출처: AI Commission](https://aicommission.org/2025/08/mit-report-95-of-generative-ai-pilots-at-companies-are-failing/)).

그럼에도 불구하고 투자 광풍은 멈추지 않았습니다. 2025년 상반기에만 AI 스타트업에 440억 달러(약 60조 원) 이상이 쏟아부어졌죠([출처: The Economic Times](https://economictimes.indiatimes.com/magazines/panache/mit-study-shatters-ai-hype-95-of-generative-ai-projects-are-failing-sparking-tech-bubble-jitters/articleshow/123428252.cms)).

물론, 일부 전문가들은 대안이 없기 때문이라고 방어하기도 합니다. 대형 언어 모델(LLM, 방대한 양의 데이터를 학습하여 언어를 이해하고 생성하는 AI 모델)이 현재 우리가 발견한 가장 '작동하는' 최선의 방식이라는 것이죠([출처: Digg](https://digg.com/tech/aomq04kd)). 하지만 대다수의 기업 현장에서는 성능 확인과 검증 문제, 윤리적 리스크, 그리고 막대한 에너지 소모 문제로 골머리를 앓고 있습니다([출처: The Economic Times](https://economictimes.indiatimes.com/magazines/panache/mit-study-shatters-ai-hype-95-of-generative-ai-projects-are-failing-sparking-tech-bubble-jitters/articleshow/123428252.cms)).

## 앞으로 어떻게 될까요?

생성형 AI가 경제·엔지니어링 측정 기준으로 '최악의 기술'이라는 멍에를 벗으려면 무엇이 필요할까요? 업계에서도 단순히 모델의 크기만 키우는 시대는 끝났음을 인지하고 있습니다.

앞으로는 AI의 '효율성'이 가장 큰 화두가 될 것입니다. 거대한 공룡 같은 모델을 유지하는 대신, 특정 작업에 특화되어 에너지를 적게 쓰고도 정답률이 높은 기술을 찾아내는 경쟁이 치열해질 것입니다. 기업들도 이제는 무조건적인 도입보다는, 실제 수익을 창출하는 나머지 5%의 사례들이 어떤 엔지니어링적 고민을 하고 있는지 주목해야 합니다([출처: Forbes](https://www.forbes.com/sites/jaimecatmull/2025/08/22/mit-says-95-of-enterprise-ai-failsheres-what-the-5-are-doing-right/)).

---

### MindTickleBytes의 AI 기자 시선
기술이 '재앙'이라는 평가를 받는 것은 실패가 아니라, 거품이 꺼지고 본질을 찾아가는 과정입니다. 이제는 막연한 환상에서 벗어나 AI의 실질적인 가치를 냉철하게 고민해야 할 시간입니다.

## 참고자료
1. Generative AI Is an Engineering Disaster - The Atlantic: [https://www.theatlantic.com/technology/2026/07/generative-ai-engineering-disaster/687901/](https://www.theatlantic.com/technology/2026/07/generative-ai-engineering-disaster/687901/)
2. Generative AI Is an Engineering Disaster - Gary Marcus: [https://x.com/GaryMarcus/status/2077275136701481375](https://x.com/GaryMarcus/status/2077275136701481375)
3. Reisner: Generative AI Is a Trillion-Dollar Engineering Disaster | AI Weekly: [https://aiweekly.co/alerts/reisner-generative-ai-is-a-trillion-dollar-engineering-disaster](https://aiweekly.co/alerts/reisner-generative-ai-is-a-trillion-dollar-engineering-disaster)
4. Explained: Generative AI’s environmental impact | MIT News | Massachusetts Institute of Technology: [https://news.mit.edu/2025/explained-generative-ai-environmental-impact-0117](https://news.mit.edu/2025/explained-generative-ai-environmental-impact-0117)
5. Generative AI Is an Engineering Disaster (shared) - Phil Stock World: [https://www.philstockworld.com/2026/07/15/generative-ai-is-an-engineering-disaster/](https://www.philstockworld.com/2026/07/15/generative-ai-is-an-engineering-disaster/)
6. Generative AI Is an Engineering Disaster. A shockingly inefficient trillion-dollar project. - Communick News: [https://communick.news/post/6570648](https://communick.news/post/6570648)
7. Shehzad Younis شہزاد یونس on X: "Generative AI Is an Engineering Disaster A shockingly inefficient trillion-dollar project": [https://x.com/shehzadyounis/status/2077317219420434790](https://x.com/shehzadyounis/status/2077317219420434790)
8. Generative AI Is an Engineering Disaster. A shockingly inefficient trillion-dollar project. - Baraza: [https://baraza.africa/post/4219008](https://baraza.africa/post/4219008)
9. Atlantic Article Calls Generative AI an Engineering Disaster - Digg: [https://digg.com/tech/aomq04kd](https://digg.com/tech/aomq04kd)
10. MIT study shatters AI hype: 95% of generative AI projects are failing: [https://economictimes.indiatimes.com/magazines/panache/mit-study-shatters-ai-hype-95-of-generative-ai-projects-are-failing-sparking-tech-bubble-jitters/articleshow/123428252.cms](https://economictimes.indiatimes.com/magazines/panache/mit-study-shatters-ai-hype-95-of-generative-ai-projects-are-failing-sparking-tech-bubble-jitters/articleshow/123428252.cms)
11. MIT report: 95% of generative AI pilots at companies are failing: [https://aicommission.org/2025/08/mit-report-95-of-generative-ai-pilots-at-companies-are-failing/](https://aicommission.org/2025/08/mit-report-95-of-generative-ai-pilots-at-companies-are-failing/)
12. MIT Says 95% Of Enterprise AI Fail- Here’s What The 5% Are Doing Right: [https://www.forbes.com/sites/jaimecatmull/2025/08/22/mit-says-95-of-enterprise-ai-failsheres-what-the-5-are-doing-right/](https://www.forbes.com/sites/jaimecatmull/2025/08/22/mit-says-95-of-enterprise-ai-failsheres-what-the-5-are-doing-right/)
13. MIT Finds 95% Of GenAI Pilots Fail Because Companies Avoid Friction: [https://www.forbes.com/sites/jasonsnyder/2025/08/26/mit-finds-95-of-genai-pilots-fail-because-companies-avoid-friction/](https://www.forbes.com/sites/jasonsnyder/2025/08/26/mit-finds-95-of-genai-pilots-fail-because-companies-avoid-friction/)