---
layout: post
title: "AI가 제시한 '근거', 믿어도 될까? Perplexity 인용의 배신"
description: "AI 검색 엔진 Perplexity가 제시하는 출처들이 실제로는 근거가 부족할 수 있다는 연구 결과에 대해 알아봅니다."
summary: "최근 연구 결과, Perplexity가 답변의 근거로 제시한 출처 중 상당수가 실제 데이터나 수치를 포함하지 않고 있다는 사실이 밝혀졌습니다."
tags: [AI, 검색엔진, Perplexity, 인공지능, 신뢰성]
image: 2026-09-03-A-third-of-Perplexitys-citations-dont-contain-the-number-theyre-cited-for.jpg
image_alt: "AI가 검색 결과를 보여주는 화면 위에 겹쳐진 물음표 아이콘"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI의 답변을 그대로 믿기보다는 교차 검증이 필수적인 시대가 되었습니다. 기술의 편리함 뒤에 숨겨진 '환각(Hallucination)' 가능성을 늘 염두에 두어야 합니다."
quiz:
  - question: "이번 연구에서 밝혀진 수치가 포함된 문장 뒤에 붙은 출처가 실제로는 수치를 담고 있지 않을 확률은 어느 정도인가요?"
    choices: ["약 14.4%", "약 34.7%", "약 94%"]
    answer: 1
    explanation: "연구 결과에 따르면, 수치를 언급한 문장에 달린 인용 중 34.7%가 해당 수치를 포함하지 않은 페이지를 가리키고 있었습니다."
  - question: "Perplexity는 정보를 찾을 때 주로 어떤 방식을 사용하나요?"
    choices: ["학습 데이터 기반의 답변", "실시간 웹 검색 기반의 답변", "오프라인 데이터베이스 활용"]
    answer: 1
    explanation: "Perplexity는 과거의 데이터를 학습한 내용에 의존하기보다, 실시간 웹 검색을 통해 최신 정보를 가져오는 방식을 사용합니다."
  - question: "Perplexity의 인용 클릭률(CTR)은 전통적인 검색 결과와 비교해 어떤가요?"
    choices: ["비슷하다", "전통적인 방식보다 훨씬 낮다", "전통적인 방식보다 훨씬 높다"]
    answer: 2
    explanation: "Perplexity의 인용 클릭률은 18~24% 수준으로, 전통적인 검색 엔진의 2~4%보다 월등히 높습니다."
lang: ko
ref: 2026-09-03-A-third-of-Perplexitys-citations-dont-contain-the-number-theyre-cited-for
audio: 2026-09-03-A-third-of-Perplexitys-citations-dont-contain-the-number-theyre-cited-for.mp3
permalink: /2026/09/03/A-third-of-Perplexitys-citations-dont-contain-the-number-theyre-cited-for/
---

상상해보세요. 오늘 저녁에 있을 발표를 위해 AI 검색 엔진에게 "올해 우리나라의 AI 시장 성장률이 몇 퍼센트인가요?"라고 물었습니다. AI는 즉시 답변을 내놓고, 문장 끝에 친절하게 [1], [2] 같은 숫자를 붙여 출처까지 명시해주네요. 우리는 보통 이런 출처를 보면 "AI가 직접 찾아보고 확인한 정보구나"라며 안심합니다. 하지만 만약 그 출처가 사실은 엉뚱한 페이지를 가리키고 있다면 어떨까요?

최근 AI 검색 서비스인 퍼플렉시티(Perplexity)가 답변의 근거로 제시하는 인용구들에 대해 충격적인 실태가 공개되었습니다. 우리가 믿고 보던 그 '출처'들이 과연 얼마나 정확한지, 그리고 AI는 왜 이런 실수를 하는지 함께 살펴보겠습니다.

## 왜 중요한가요?

퍼플렉시티는 기존의 검색 엔진과 달리, 방대한 웹 데이터를 스스로 요약해서 답변을 만들어줍니다. 그래서 사용자는 여러 사이트를 일일이 클릭할 필요 없이 답변을 한 번에 얻을 수 있죠. [출처: Perplexity는 인용 엔진입니다](https://mentionagent.ai/blog/how-to-get-cited-by-perplexity/). 실제로 사용자들이 인용구(숫자로 표시된 출처)를 클릭하는 비율은 18~24%에 달하는데, 이는 전통적인 검색 엔진의 클릭률인 2~4%보다 훨씬 높은 수치입니다. [출처: 2026년 Perplexity에서 인용되는 방법](https://www.miniloop.ai/blog/perplexity-seo-how-to-get-cited-2026).

즉, 우리는 AI가 제공하는 출처를 매우 신뢰하며, 실제로 그곳을 통해 정보를 더 깊게 파고든다는 뜻입니다. 그런데 만약 이 정보가 사실을 담고 있지 않다면, 우리는 가짜 정보의 늪에 빠지게 될 위험이 있습니다.

## 쉽게 이해하기

쉽게 말해, 퍼플렉시티의 작동 방식은 **'똑똑한 비서가 수많은 책을 찾아보고 정리해주는 것'**과 비슷합니다. 비서는 답변을 쓰다가 "이 내용은 5페이지에 있습니다"라고 각주를 답니다. 그런데 이 비서가 글을 다 쓰고 나서, 나중에 "아, 이 부분은 5페이지쯤에 있었던 것 같아"라며 각주를 뒤늦게 붙이는 경우가 있습니다. [출처: Perplexity 인용 패턴](https://bcited.ai/blog/perplexity-citation-patterns-source-selection). 이 과정에서 비서의 기억이 흐릿해서 엉뚱한 페이지를 지목하게 되는 것이죠.

데이터를 조사한 결과, 수치가 포함된 문장에 달린 인용구 중 약 34.7%는 해당 수치가 전혀 포함되지 않은 페이지로 연결되었습니다. [출처: Perplexity 인용 감사 보고서](https://hausresearch.com/reports/perplexity-citation-audit/). 이는 비유하자면, 우리가 수학 문제를 풀고 정답 페이지를 확인하려는데, 책 뒤편의 해설지가 전혀 다른 문제의 해설을 담고 있는 것과 같습니다. 또한 전체적으로 평가했을 때, 퍼플렉시티가 제시한 주장의 약 14.4%가 실제 인용된 출처에서 뒷받침되지 않는다는 결과도 나왔습니다. [출처: Perplexity 인용 감사 보고서](https://hausresearch.com/reports/perplexity-citation-audit/).

## 현재 상황

퍼플렉시티는 답변의 약 94%에서 출처를 명시할 정도로 인용에 적극적입니다. [출처: 2026년, 퍼플렉시티는 항상 출처를 명시할까?](https://www.fonzy.ai/blog/does-perplexity-cite-sources). 하지만 문제는 AI 모델 자체가 답변을 생성한 뒤, 그 답변이 사실인지 확인하지 않고 '사후적으로' 출처를 꿰맞추는 방식에 있습니다. [출처: Perplexity 인용 패턴](https://bcited.ai/blog/perplexity-citation-patterns-source-selection). 

물론 가끔은 퍼플렉시티의 잘못이 아닌 경우도 있습니다. 외부 앱이 퍼플렉시티의 데이터를 제대로 보여주지 못해서 출처 링크가 사라진 것처럼 보이는 현상도 존재하죠. [출처: Perplexity 출처 미표기 이슈](https://perplexityaimagazine.com/perplexity-hub/perplexity-not-citing-sources/). 하지만 근본적으로 시스템이 답변 내용과 일치하지 않는 소스를 가져오는 '환각(Hallucination, 인공지능이 사실이 아닌 정보를 그럴듯하게 만들어내는 현상)' 현상은 명백히 존재하며, 이는 사용자가 인지해야 할 한계점입니다. [출처: 2026년 Perplexity 리뷰](https://vantaige.io/ai-tool/perplexity).

## 앞으로 어떻게 될까?

앞으로는 AI 검색 서비스 간의 경쟁에서 '얼마나 많은 출처를 보여주느냐'보다 **'얼마나 정확한 출처를 연결하느냐'**가 더 중요한 기준이 될 것입니다. 이미 일부 연구에서는 퍼플렉시티의 인용이 챗GPT보다 약 3배 더 많다는 점을 지적하며, 양적인 팽창이 항상 질적인 정확성을 보장하지는 않는다고 말합니다. [출처: Perplexity 인용 9가지 신호](https://citevantage.com/blog/how-to-get-cited-by-perplexity/). 사용자들이 더 똑똑해질수록, 잘못된 인용을 내놓는 AI 플랫폼은 신뢰를 잃게 될 것입니다.

## MindTickleBytes의 AI 기자 시선
AI 검색 엔진은 편리하지만, 근거 없는 확신에 주의해야 합니다. AI가 주는 출처를 클릭했을 때 원하는 내용이 없다면, 그것은 AI가 내용을 깊이 있게 이해한 것이 아니라 단순히 '그럴듯한 위치'를 추측했기 때문일 가능성이 큽니다. 검색된 답변을 읽을 때는 늘 '비판적 시각'으로 내용을 한 번 더 확인하는 습관이 필요한 시대입니다.

## 참고자료
1. [AthirdofPerplexity'scitationsdon'tcontainthenumberthey'r...](https://news.ycombinator.com/item?id=49536201)
2. [How to GetCitedbyPerplexity: The Tactical Playbook for 2026 | Cintra](https://cintra.run/blog/how-to-get-cited-by-perplexity)
3. [How to Rank inPerplexityAI: What 21CitationsPer Query... | BlueJar](https://bluejar.ai/blog/how-to-rank-in-perplexity-ai/)
4. [How to GetCitedbyPerplexityAI | Mentionable](https://mentionable.ai/en/guides/rank-on-perplexity)
5. [PerplexityInlineCitations: How [1][2][3] Links Work](https://amicitable.com/blog/does-perplexity-cite-inline-sources)
6. [PerplexitySEO: How to GetCitedin 2026](https://www.miniloop.ai/blog/perplexity-seo-how-to-get-cited-2026)
7. [How to GetCitedbyPerplexity(2026 Playbook) | MentionAgent](https://mentionagent.ai/blog/how-to-get-cited-by-perplexity/)
8. [The 50 Most-CitedWebsites inPerplexity(September 2026)](https://ahrefs.com/blog/most-cited-domains-perplexity/)
9. [PerplexityCitations| Fetchable Sources, Enquire Desk](https://www.worldwidebacklinks.com/ai-backlinks/perplexity-citations/)
10. [PerplexitycitesClickUp 6,474 times. Notion gets 741… Why?](https://foundationinc.co/lab/vol-304)
11. [PerplexityCitationPatterns: What Actually Gets Sourced — b/cited](https://bcited.ai/blog/perplexity-citation-patterns-source-selection)
12. [How to earn morecitationsinperplexityai search](https://snoika.com/blog/perplexity-ai-search-citation-checklist)
13. [How to GetCitedbyPerplexity: 9 Source Signals | CiteVantage](https://citevantage.com/blog/how-to-get-cited-by-perplexity/)
14. [A third of Perplexity's citations don't contain the number they're ...](https://hausresearch.com/reports/perplexity-citation-audit/)
15. [Perplexity Not Citing Sources: 8 Fixes 2026](https://perplexityaimagazine.com/perplexity-hub/perplexity-not-citing-sources/)
16. [Perplexity AI Review 2026: Citations, Limits & Real Failures](https://vantaige.io/ai-tool/perplexity)
17. [Does Perplexity Always Cite Sources? 2026 Data Says No](https://www.fonzy.ai/blog/does-perplexity-cite-sources)
18. [How Perplexity Selects Its Citations: What We Know From Testing and ...](https://aiseoshift.com/blog/how-perplexity-selects-citations/)
19. [Getting Cited by Perplexity: What It Actually Quotes — Genαi](https://genalphai.com/getting-cited-by-perplexity-teardown/)
20. [How Perplexity Decides Which Sources to Cite - authoritytech.io](https://authoritytech.io/blog/how-perplexity-selects-sources-algorithm-2026)