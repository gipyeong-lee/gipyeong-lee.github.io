---
layout: post
title: "AI가 레딧 게시물 15만 개를 읽고 찾아낸 '승인되지 않은' 다이어트 약의 부작용"
description: "AI를 이용해 온라인 커뮤니티의 비공식 다이어트 약물 후기를 분석, 실제 임상 시험과 다른 부작용을 식별한 연구 사례를 소개합니다."
summary: "펜실베이니아 대학 연구진이 AI로 레딧 게시물 15만 개를 분석하여, 승인되지 않은 비만 치료제 '레타트루타이드'의 실제 사용자 부작용 데이터를 찾아냈습니다."
tags: [AI, 보건의료, 다이어트, 빅데이터, 레타트루타이드]
image: 2026-10-19-LLM-analyzed-150k-Reddit-posts-to-identify-side-effects-of-unapproved-new-GLP-1.jpg
image_alt: "컴퓨터 화면 속 수많은 데이터가 연결되어 있고, 그 위에 알약 아이콘이 떠 있는 모습"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "온라인 공간의 자발적 기록이 의학적 안전망을 보완하는 귀중한 데이터가 될 수 있음을 보여줍니다."
quiz:
  - question: "이번 연구에서 연구진이 AI를 활용해 분석한 데이터의 출처는 어디인가요?"
    choices: ["페이스북 게시물", "레딧(Reddit) 게시물", "병원 진료 기록"]
    answer: 1
    explanation: "연구진은 승인되지 않은 비만 치료제 사용 후기가 많은 레딧 게시물 약 15만 개를 분석했습니다."
  - question: "연구 결과, 임상 시험 데이터와 다르게 나타난 부작용의 예시는 무엇인가요?"
    choices: ["시력 저하", "식욕 증가", "심박수 감소"]
    answer: 1
    explanation: "임상 시험 데이터와 달리 실제 사용자들 사이에서는 식욕 증가와 같은 부작용이 보고되었습니다."
  - question: "이번 연구에서 사용된 기술은 무엇인가요?"
    choices: ["간단한 키워드 검색", "설문 조사", "검증된 대규모 언어 모델(LLM)"]
    answer: 2
    explanation: "연구진은 승인되지 않은 약물 사용 분류와 증상 추출을 위해 검증된 대규모 언어 모델(LLM)을 활용했습니다."
lang: ko
ref: 2026-10-19-LLM-analyzed-150k-Reddit-posts-to-identify-side-effects-of-unapproved-new-GLP-1
audio: 2026-10-19-LLM-analyzed-150k-Reddit-posts-to-identify-side-effects-of-unapproved-new-GLP-1.mp3
permalink: /2026/10/19/LLM-analyzed-150k-Reddit-posts-to-identify-side-effects-of-unapproved-new-GLP-1/
---

상상해보세요. 소셜 미디어 커뮤니티에서 사람들이 입을 모아 말하는 어떤 신약의 효과가, 전문가들이 엄격하게 통제된 환경에서 테스트한 결과와 완전히 다르다면 어떨까요? 최근 펜실베이니아 대학 연구진은 인공지능(AI)을 통해 온라인상의 목소리가 어떻게 의학적 안전 정보를 보완할 수 있는지 보여주는 놀라운 연구 결과를 발표했습니다.

이번 연구는 단순히 온라인 글을 읽는 수준을 넘어, 승인되지 않은 다이어트 약물에 대한 사람들의 실제 경험을 체계적으로 추적했다는 점에서 큰 의미를 갖습니다.

## 이게 왜 중요한가요?

오늘날 새로운 비만 치료제들은 건강에 대한 관심을 높이며 빠르게 확산하고 있습니다 [[참고자료 15](https://www.scientificamerican.com/article/mounjaro-and-ozempic-arent-the-same-heres-how-weight-loss-drugs-compare/)]. 그러나 정식으로 승인되지 않은 경로, 즉 이른바 '그레이 마켓(Gray-market, 공식 유통망을 거치지 않는 비공식 시장)'을 통해 유통되는 약물들의 경우, 공식적인 안전 데이터를 확보하기가 매우 어렵습니다 [[참고자료 9](https://scienmag.com/ai-scans-150000-reddit-posts-to-flag-side-effects-of-gray-market-glp-1-drug-retatrutide/)].

일반인들에게 이는 결코 남의 일이 아닙니다. 공식적인 임상 시험에서는 발견되지 않았던 부작용이 실제 사용자들에게 나타나고 있다면, 누군가는 자신의 건강을 담보로 위험한 실험을 하고 있는 셈이기 때문입니다. 이번 연구는 AI를 활용해 이러한 사각지대의 위험을 조기에 포착할 수 있는 새로운 가능성을 제시했습니다.

## 쉽게 이해하기: AI가 수만 명의 대화를 정리하는 법

이번 연구의 핵심은 '대규모 언어 모델(LLM, Large Language Model, 문장의 단어들 사이 관계를 파악하여 인간처럼 언어를 이해하고 생성하는 AI 구조)'이라는 AI 기술입니다. 연구진은 레딧(Reddit) 커뮤니티의 비만 관리 및 펩타이드(단백질의 일종인 약물 성분) 관련 커뮤니티에서 2025년 12월까지 작성된 약 15만 개의 게시물과 댓글을 수집했습니다 [[참고자료 13](https://www.medrxiv.org/content/10.64898/2026.05.28.26352819v1)].

쉽게 비유하자면, 마치 수천 권의 일기장을 단 한 명의 능숙한 비평가가 며칠 밤을 새워 읽고 중요한 정보만 쏙쏙 뽑아 정리해주는 것과 같습니다. AI는 복잡한 인터넷 은어나 말투를 이해하고, 사용자가 약물을 직접 사용했는지 여부를 분류하며, 사용자가 스스로 언급한 증상들을 의학적 부작용 데이터와 연결했습니다 [[참고자료 9](https://scienmag.com/ai-scans-150000-reddit-posts-to-flag-side-effects-of-gray-market-glp-1-drug-retatrutide/), [참고자료 13](https://www.medrxiv.org/content/10.64898/2026.05.28.26352819v1)].

이렇게 분석된 데이터는 전문가들이 약물의 '부작용 프로파일(약물이 일으킬 수 있는 부작용의 유형과 빈도를 정리한 정보)'을 파악하는 데 유용한 첫 번째 체계적인 가이드가 되었습니다 [[참고자료 8](https://www.engineering.upenn.edu/stories/penn-engineers-use-ai-reddit-to-identify-potential-side-effects-of-unapproved-new-glp-1/)].

## 어디에 서 있나요?

연구 결과는 흥미로웠습니다. AI 분석 결과, 실제 사용자들 사이에서는 임상 시험의 결과와는 차이가 있는 증상들이 보고되었습니다. 대표적인 예로 '식욕 증가'와 같은 증상이 꼽혔습니다 [[참고자료 9](https://scienmag.com/ai-scans-150000-reddit-posts-to-flag-side-effects-of-gray-market-glp-1-drug-retatrutide/), [참고자료 11](https://www.brightsurf.com/news/1474QZ41/penn-engineers-use-ai-reddit-to-identify-potential-side-effects-of-unapproved-new-glp-1.html)].

물론 이 연구는 소셜 미디어 데이터를 기반으로 한 분석이므로 임상 시험과 같은 수준의 확정적 결론을 내리는 것은 아닙니다. 하지만 승인되지 않은 비만 치료제 '레타트루타이드(Retatrutide)'처럼 사용 사례는 늘어나지만 안전 경험이 제대로 기록되지 않은 경우, 이러한 AI 분석은 보건 연구자들이 추가적인 조사를 해야 할 신호를 포착하는 데 아주 효과적인 도구가 될 수 있습니다 [[참고자료 8](https://www.engineering.upenn.edu/stories/penn-engineers-use-ai-reddit-to-identify-potential-side-effects-of-unapproved-new-glp-1/), [참고자료 13](https://www.medrxiv.org/content/10.64898/2026.05.28.26352819v1)].

## 앞으로는?

이번 분석 방법은 앞으로 다이어트 약물뿐만 아니라 다양한 신약이나 의료 기기의 잠재적 위험성을 조기에 발견하는 데 활용될 것으로 보입니다. 온라인상의 사용자 후기는 이제 단순한 정보 교환의 장을 넘어, 의학 발전을 돕는 거대한 데이터베이스가 되어가고 있습니다.

다만, 온라인상의 정보는 검증되지 않은 주관적 내용이 섞여 있을 수 있습니다. 따라서 앞으로는 AI가 솎아낸 신호들이 실제로 얼마나 의학적 근거를 갖는지 확인하는 전문가들의 검증 과정이 더욱 중요해질 것입니다.

## AI의 시선

MindTickleBytes의 AI 기자 시선: 이번 연구는 디지털 시대의 방대한 데이터가 어떻게 실질적인 보건 안전망으로 전환될 수 있는지 잘 보여줍니다. AI는 사람의 눈으로 다 읽을 수 없는 거대한 정보의 바다에서, 건강을 위협할 수 있는 작은 신호들을 찾아내는 등대 역할을 할 것입니다.

## 참고자료

1. [Source 8] [Penn Engineers Use AI, Reddit to Identify Potential Side Effects of...](https://www.engineering.upenn.edu/stories/penn-engineers-use-ai-reddit-to-identify-potential-side-effects-of-unapproved-new-glp-1/)
2. [Source 9] [AI Scans 150,000 Reddit Posts to Flag Side Effects of Gray-Market GLP-1](https://scienmag.com/ai-scans-150000-reddit-posts-to-flag-side-effects-of-gray-market-glp-1-drug-retatrutide/)
3. [Source 11] [Penn engineers use AI, Reddit to identify potential side effects of...](https://www.brightsurf.com/news/1474QZ41/penn-engineers-use-ai-reddit-to-identify-potential-side-effects-of-unapproved-new-glp-1.html)
4. [Source 13] [Self-Reported Side Effects Among Reddit Users Taking Unapproved...](https://www.medrxiv.org/content/10.64898/2026.05.28.26352819v1)
5. [Source 15] [Ozempic and Mounjaro Aren’t the Same. | Scientific American](https://www.scientificamerican.com/article/mounjaro-and-ozempic-arent-the-same-heres-how-weight-loss-drugs-compare/)