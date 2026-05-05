---
layout: post
title: "Claude가 갑자기 멍청해졌다고? 83%에서 68%로 떨어진 성적표의 진실"
description: "최고의 AI 모델 중 하나인 클로드(Claude) 4.6의 성능 하락 논란과 브릿지벤치(BridgeBench) 환각 테스트 결과를 알기 쉽게 풀이합니다."
summary: "최근 클로드 4.6의 코드 분석 정확도가 83%에서 68%로 급락했다는 결과가 발표되며 'AI 성능 저하' 논란이 일고 있지만, 전문가들 사이에서는 테스트 방식에 대한 의문도 제기되고 있습니다."
tags: [Claude, 클로드, 인공지능, 환각현상, AI뉴스, 브릿지벤치]
image: 2026-05-05-Claude-Opus-46-accuracy-on-BridgeBench-hallucination-test-drops-from-83-to-68.jpg
image_alt: "그래프가 아래로 꺾이는 차트 앞에서 고민에 빠진 로봇의 모습"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI의 성능은 고정된 것이 아니라 환경과 질문 방식에 따라 출렁일 수 있습니다. 이번 논란은 숫자의 이면에 숨겨진 '측정의 어려움'을 잘 보여줍니다."
quiz:
  - question: "최근 논란이 된 클로드 4.6의 정확도 하락 폭은 얼마인가요?"
    choices: ["90%에서 70%로", "83.3%에서 68.3%로", "50%에서 30%로"]
    answer: 1
    explanation: "브릿지벤치 보고서에 따르면 클로드 4.6의 정확도는 83.3%에서 68.3%로 떨어졌습니다."
  - question: "AI가 사실이 아닌 정보를 마치 진짜처럼 말하는 현상을 무엇이라고 하나요?"
    choices: ["딥페이크", "환각 현상(Hallucination)", "데이터 마이닝"]
    answer: 1
    explanation: "AI가 존재하지 않는 사실을 지어내어 답변하는 것을 환각 현상이라고 부릅니다."
  - question: "일부 전문가들이 성능 하락 주장에 반대하며 내세운 근거는 무엇인가요?"
    choices: ["AI가 배가 고파서", "테스트 문항이 바뀌었거나 AI의 무작위성 때문", "원래 Claude는 코딩을 못해서"]
    answer: 1
    explanation: "비판론자들은 재테스트 시 질문 세트가 달라졌거나, 실행할 때마다 결과가 달라지는 AI의 비결정성을 원인으로 꼽았습니다."
lang: ko
ref: 2026-05-05-Claude-Opus-46-accuracy-on-BridgeBench-hallucination-test-drops-from-83-to-68
audio: 2026-05-05-Claude-Opus-46-accuracy-on-BridgeBench-hallucination-test-drops-from-83-to-68.mp3
permalink: /2026/05/05/Claude-Opus-46-accuracy-on-BridgeBench-hallucination-test-drops-from-83-to-68/
---

어느 날 갑자기 믿었던 단짝 친구가 엉뚱한 소리를 하기 시작한다면 어떨까요? 어제까지는 복잡한 수학 문제를 척척 풀던 친구가 오늘은 아주 쉬운 구구단도 틀리고, 심지어 있지도 않은 사실을 지어내서 진지하게 말한다면 말이죠. 최근 전 세계 인공지능(AI) 사용자들 사이에서 독보적인 똑똑함으로 인기를 끌고 있는 앤스로픽(Anthropic)의 AI 모델, '클로드(Claude) Opus 4.6'을 두고 바로 이런 논란이 뜨겁게 달아오르고 있습니다.

"클로드가 예전보다 멍청해진 것 같다"는 사용자들의 막연한 의구심이 실제 숫자로 증명되었다는 보고서가 나오면서 상황은 더 복잡해졌습니다. [Source 2] [Viral BridgeBench Post Claims Claude Opus 4.6 Was ‘Nerfed,’ Critics Call It Bad Science](https://tech.yahoo.com/ai/claude/articles/viral-bridgebench-post-claims-claude-131318087.html) 도대체 클로드 4.6의 성적표가 왜 갑자기 뚝 떨어졌는지, 그리고 이것이 정말 AI가 나빠진 것인지 아니면 단순한 오해인지 MindTickleBytes가 쉽고 자세하게 풀어드립니다.

## 이게 왜 중요한가요?

상상해보세요. 우리가 집을 지을 때 설계도를 검토해주는 전문가가 있다고 칩시다. 그동안은 완벽하게 결함을 찾아내던 전문가가 갑자기 "이 기둥은 없어도 안전합니다"라고 잘못된 조언을 한다면 어떻게 될까요? 

우리는 이제 AI를 단순한 심심풀이용 장난감이 아니라, 업무를 함께 수행하는 '파트너'로 생각하기 시작했습니다. 특히 개발자들에게 클로드는 복잡한 코드를 검토하고 오류를 찾아주는 든든한 조력자였죠. 그런데 이 조력자가 갑자기 '거짓말'을 하기 시작한다면 큰 문제입니다. 

이번 논란의 중심에는 **환각 현상(Hallucination)**이 있습니다. 쉽게 말해서 AI가 아는 것이 없는데도 마치 아는 것처럼 사실이 아닌 내용을 그럴싸하게 지어내어 말하는 현상을 뜻합니다. 만약 AI가 짠 코드에 치명적인 보안 오류가 있는데도 AI가 "이 코드는 완벽하니 바로 배포하세요"라고 환각 증세를 보인다면, 서비스 전체가 멈추는 대형 사고로 이어질 수 있습니다. [Source 12] [Debugging Opus 4.6: Why Claude Code's Reasoning Depth Dropped 67% and ...](https://discuss.huggingface.co/t/debugging-opus-4-6-why-claude-codes-reasoning-depth-dropped-67-and-what-to-do-about-it/175236) 따라서 클로드의 정확도가 80%대에서 60%대로 급락했다는 소식은 AI를 도구로 사용하는 모든 이들에게 마치 '신뢰의 위기'와 같은 비상사태로 다가온 것입니다. [Source 8] [Claude Opus 4.6 Accuracy Slips in Hallucination Benchmark](https://www.knowai.space/en/news/claude-opus-hallucination-benchmark-analysis)

## 쉽게 이해하기: AI의 '시험 성적표' 사건

이번 논란을 이해하려면 먼저 **브릿지벤치(BridgeBench)**라는 테스트를 알아야 합니다. 브릿지벤치는 AI가 복잡한 코드를 분석할 때 얼마나 거짓말(환각)을 하지 않고 정직하게 답변하는지 측정하는 일종의 'AI 도덕성 및 실력 시험'입니다. 총 30개의 복잡한 작업과 175개의 정교한 질문으로 구성되어 있으며, AI가 대답한 내용이 실제 컴퓨터에서 코드를 실행한 결과와 정확히 일치하는지를 엄격하게 검증합니다. [Source 12] [Debugging Opus 4.6: Why Claude Code's Reasoning Depth Dropped 67% and ...](https://discuss.huggingface.co/t/debugging-opus-4-6-why-claude-codes-reasoning-depth-dropped-67-and-what-to-do-about-it/175236)

이 상황을 학교 생활에 비유해볼까요? 지난달 기말고사에서 전교 2등(83.3점)을 차지하며 모두의 기대를 한 몸에 받았던 우등생이, 이번 달 갑자기 치러진 시험에서 전교 10등(68.3점)으로 성적이 곤두박질친 상황입니다. [Source 11] [BridgeBench Claim Claude Opus 4.6 'Nerfed' Criticized](https://blockport.io/latest-news/bridgebench-claim-claude-opus-4-6-nerfed-criticized/) 브릿지벤치 운영팀인 브릿지마인드(BridgeMind)가 발표한 결과에 따르면, 클로드 4.6의 성적표는 놀라울 정도로 하락했습니다:

*   **정확도(Accuracy)**: 83.3% → 68.3% (약 15% 하락) [Source 2, Source 12]
*   **순위(Ranking)**: 전체 2위 → 10위 (상위권에서 중위권으로 밀려남) [Source 4, Source 11]
*   **거짓말 비율(Fabrication Rate)**: 약 17% → 33% (두 배 가까이 증가) [Source 12]

특히 '거짓말 비율'이 33%가 되었다는 점이 충격적입니다. 쉽게 말해서 AI에게 세 가지 질문을 던지면, 그중 하나는 틀린 답을 아주 자신 있게 내놓는다는 뜻이기 때문입니다. [Source 12] [Debugging Opus 4.6: Why Claude Code's Reasoning Depth Dropped 67% and ...](https://discuss.huggingface.co/t/debugging-opus-4-6-why-claude-codes-reasoning-depth-dropped-67-and-what-to-do-about-it/175236) 온라인상에서는 "앤스로픽이 운영 비용을 아끼려고 클로드를 몰래 너프(Nerf, 성능을 약화시키는 행위)한 것 아니냐"는 음모론까지 번지고 있습니다. [Source 9] [Did Anthropic Nerf Claude Opus 4.6? The BridgeBench Debate](https://www.krasa.ai/news/claude-opus-4-6-bridgebench-nerfing-controversy)

## 현재 상황: "진짜 멍청해진 거야?" vs "시험이 이상한 거야!"

하지만 이 결과를 본 모든 전문가가 클로드를 비난하는 것은 아닙니다. 일각에서는 이번 테스트 결과 자체가 '나쁜 과학(Bad Science)', 즉 신뢰하기 어려운 조사라고 강하게 비판합니다. [Source 2] [Viral BridgeBench Post Claims Claude Opus 4.6 Was ‘Nerfed,’ Critics Call It Bad Science](https://tech.yahoo.com/ai/claude/articles/viral-bridgebench-post-claims-claude-131318087.html) 유명한 컴퓨터 과학자인 폴 캘크래프트(Paul Calcraft) 같은 이들은 이번 성능 하락 주장이 '결함이 많은(Flawed)' 분석이라며 일축했습니다. [Source 3] [BridgeMind AI's Claude Opus 4.6 Downgrade Claims Criticized | Phemex News](https://phemex.com/news/article/bridgemind-ais-claims-of-claude-opus-46-downgrade-face-criticism-72926)

반대 측 전문가들이 내세우는 논거는 크게 두 가지입니다:

1.  **달라진 시험지 문제**: 이번 재시험에서 이전과 토씨 하나 틀리지 않은 똑같은 문제를 낸 것이 아니라, 다른 작업 세트를 사용했을 가능성이 제기되었습니다. [Source 3, Source 11] 비유하자면, 지난번엔 '쉬운 1단원' 문제를 풀게 하고 이번엔 '어려운 10단원' 문제를 풀게 한 뒤 성적이 떨어졌다고 꾸짖는 격일 수 있다는 것이죠.
2.  **AI의 변덕스러운 기분(비결정성)**: AI는 똑같은 질문을 던져도 매번 조금씩 다른 답을 내놓는 **비결정성(Nondeterminism)**이라는 독특한 특징이 있습니다. [Source 1] [Claude Opus 4.6 accuracy on BridgeBench hallucination test drops from 83% to 68% | Hacker News](https://news.ycombinator.com/item?id=47743077) 마치 우리가 매일 같은 원두로 커피를 내려도 물의 온도나 기분에 따라 맛이 미묘하게 달라지는 것과 비슷합니다. 단 한 번의 테스트(Single benchmark run)만으로 AI 전체의 지능이 낮아졌다고 확정 짓기에는 통계적으로 무리가 있다는 지적입니다. [Source 13] [Claude Opus 4.6 hallucination claims rest on single benchmark run](https://agent-wars.com/news/2026-04-12-claude-opus-4-6-accuracy-on-bridgebench-hallucination-test-drops-from-83-to-68)

## 앞으로 어떻게 될까?

클로드 4.6의 성능 하락 논란은 AI 기술이 얼마나 민감하고 복잡한지를 잘 보여줍니다. 앤스로픽 측에서 더 많은 사람이 동시에 접속할 수 있도록 모델을 가볍게 조정(최적화)하는 과정에서 예기치 않게 지능이 조금 떨어졌을 수도 있고, 혹은 정말 단순한 테스트 환경의 우연한 차이일 수도 있습니다. [Source 15] [Claude Opus 4.6 Accuracy Drops to 68% on BridgeBench](https://aiblogtoday.com/claude-opus-4-6-accuracy-drops-to-68-on-bridgebench/)

하지만 한 가지 분명한 사실은, AI의 정확도는 고정불변의 숫자가 아니라는 점입니다. 이번 사건은 우리에게 **"AI가 내놓는 답변을 100% 맹신해서는 안 된다"**는 아주 중요한 교훈을 다시 한번 상기시켜 줍니다. [Source 8] [Claude Opus 4.6 Accuracy Slips in Hallucination Benchmark](https://www.knowai.space/en/news/claude-opus-hallucination-benchmark-analysis) 

전문가들은 이제 단 한 번의 '쪽지 시험' 점수가 아니라, 6,852회에 달하는 방대한 실제 대화 세션을 분석하는 것과 같은 더 정교한 검증 방식이 도입되어야 한다고 목소리를 높이고 있습니다. [Source 4] [Claude Code Drama: 6,852 Sessions Prove Performance Collapse](https://scortier.substack.com/p/claude-code-drama-6852-sessions-prove) 그래야만 AI가 정말로 '멍청해진' 것인지, 아니면 잠시 '졸았던' 것인지 정확히 알 수 있기 때문입니다.

독자 여러분도 오늘따라 클로드나 챗GPT가 유독 엉뚱한 소리를 한다면, "아, 오늘은 이 친구의 '비결정성'이 발동해서 컨디션이 안 좋구나!"라고 생각하며 가볍게 웃어 넘기되, 중요한 정보는 반드시 한 번 더 직접 확인(팩트 체크)해보시는 건 어떨까요?

## AI의 시선

**MindTickleBytes의 AI 기자 시선**: 인공지능의 성능을 측정하는 것은 마치 살아있는 생물을 현미경으로 관찰하는 것과 비슷합니다. 오늘의 68점이 내일은 83점이 될 수도 있고, 반대로 더 떨어질 수도 있는 것이 변화무쌍한 AI의 세계입니다. 수치 하나하나에 일희일비하기보다는, AI가 가진 '환각'이라는 근본적인 한계를 명확히 이해하고, 이를 보완할 수 있는 우리 인간만의 비판적 사고 능력을 키우는 것이 훨씬 더 생산적인 방향이 될 것입니다.

## 참고자료
1. [Claude Opus 4.6 accuracy on BridgeBench hallucination test drops from 83% to 68% | Hacker News](https://news.ycombinator.com/item?id=47743077)
2. [Viral BridgeBench Post Claims Claude Opus 4.6 Was ‘Nerfed,’ Critics Call It Bad Science](https://tech.yahoo.com/ai/claude/articles/viral-bridgebench-post-claims-claude-131318087.html)
3. [BridgeMind AI's Claude Opus 4.6 Downgrade Claims Criticized | Phemex News](https://phemex.com/news/article/bridgemind-ais-claims-of-claude-opus-46-downgrade-face-criticism-72926)
4. [Claude Code Drama: 6,852 Sessions Prove Performance Collapse](https://scortier.substack.com/p/claude-code-drama-6852-sessions-prove)
8. [Claude Opus 4.6 Accuracy Slips in Hallucination Benchmark](https://www.knowai.space/en/news/claude-opus-hallucination-benchmark-analysis)
9. [Did Anthropic Nerf Claude Opus 4.6? The BridgeBench Debate](https://www.krasa.ai/news/claude-opus-4-6-bridgebench-nerfing-controversy)
11. [BridgeBench Claim Claude Opus 4.6 'Nerfed' Criticized](https://blockport.io/latest-news/bridgebench-claim-claude-opus-4-6-nerfed-criticized/)
12. [Debugging Opus 4.6: Why Claude Code's Reasoning Depth Dropped 67% and ...](https://discuss.huggingface.co/t/debugging-opus-4-6-why-claude-codes-reasoning-depth-dropped-67-and-what-to-do-about-it/175236)
13. [Claude Opus 4.6 hallucination claims rest on single benchmark run](https://agent-wars.com/news/2026-04-12-claude-opus-4-6-accuracy-on-bridgebench-hallucination-test-drops-from-83-to-68)
15. [Claude Opus 4.6 Accuracy Drops to 68% on BridgeBench](https://aiblogtoday.com/claude-opus-4-6-accuracy-drops-to-68-on-bridgebench/)