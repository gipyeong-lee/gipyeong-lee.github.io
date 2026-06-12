---
layout: post
title: "AI가 똑똑한데도 자꾸 '헛소리'를 하는 진짜 이유: 어텐션의 함정"
description: "챗GPT 같은 AI가 정보를 잘 찾으면서도 종종 엉뚱한 결론을 내리는 이유를 최신 연구를 통해 쉽게 알아봅니다. AI의 '집중력'에는 치명적인 약점이 있습니다."
summary: "AI의 핵심 기술인 '어텐션'에는 인간이 가진 '실행 통제' 능력이 빠져 있어, 불필요한 방해 요소를 걸러내지 못하고 추론에 실패한다는 최신 연구 결과를 분석합니다."
tags: [인공지능, 트랜스포머, 어텐션, 인지심리학, AI한계]
image: 2026-06-12-Deficient-executive-control-in-transformer-attention.jpg
image_alt: "수많은 글자와 기호들이 어지럽게 떠다니는 가운데 돋보기가 엉뚱한 곳을 비추고 있는 모습의 일러스트"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "단순히 데이터를 쏟아붓는 것을 넘어, 이제는 AI에게 '무엇을 무시할지' 가르치는 것이 다음 세대 인공지능의 핵심 과제가 될 것입니다."
quiz:
  - question: "최신 연구에 따르면 현대 AI 모델의 '어텐션' 기능에 명시적으로 빠져 있는 인간의 인지 능력은 무엇인가요?"
    choices: ["기억력(Memory)", "실행 통제(Executive Control)", "패턴 인식(Pattern Recognition)"]
    answer: 1
    explanation: "최근 연구들은 대규모 언어 모델(LLM)이 인간의 '실행 통제' 능력을 갖추지 못해 상충하는 정보를 걸러내는 데 어려움을 겪는다고 지적했습니다."
  - question: "연구진이 AI의 한계를 증명하기 위해 사용한 인지심리학의 고전적인 테스트는 무엇인가요?"
    choices: ["튜링 테스트(Turing Test)", "로르샤흐 검사(Rorschach Test)", "스트룹 검사(Stroop Test)"]
    answer: 2
    explanation: "연구진은 글자의 의미와 색깔이 모순될 때 인지적 갈등을 유발하는 '스트룹 검사'를 활용하여 AI의 실행 통제 결함을 폭로했습니다."
  - question: "논문 내용에 따르면, AI가 문맥 속에서 헷갈리는 '방해꾼(Distractors)'을 만났을 때 어떤 일이 발생하나요?"
    choices: ["오류를 스스로 수정하고 정답을 찾는다.", "처리 속도만 느려질 뿐 결과에는 영향이 없다.", "방해 요소를 무시하지 못해 치명적인 추론 실패를 겪는다."]
    answer: 2
    explanation: "AI는 방해 요소가 섞여 있을 때 이를 걸러내지 못하고 치명적인 추론 실패(Catastrophic reasoning failures)를 겪는 것으로 나타났습니다."
lang: ko
ref: 2026-06-12-Deficient-executive-control-in-transformer-attention
audio: 2026-06-12-Deficient-executive-control-in-transformer-attention.mp3
permalink: /2026/06/12/Deficient-executive-control-in-transformer-attention/
---

상상해보세요. 오랜만에 만난 단짝 친구와 아주 시끄러운 카페에 마주 앉아 있습니다. 옆 테이블에서는 박장대소를 터뜨리며 떠들고 있고, 카페 천장에 달린 거대한 스피커에서는 쾅쾅거리는 비트의 음악이 흘러나옵니다. 심지어 창밖으로는 구급차 사이렌 소리까지 요란하게 지나가죠. 보통 사람이라면 이렇게 혼란스러운 상황에서도 눈앞에 앉은 친구의 목소리에만 온전히 귀를 기울여 대화를 나눌 수 있습니다. 우리 뇌가 현재 상황에서 불필요한 소음과 시각적 자극을 스스로 판단하여 '무시'하고, 내게 필요한 중요한 정보만 쏙쏙 골라내는 놀라운 필터링 능력을 갖추고 있기 때문입니다.

우리는 흔히 챗GPT나 클로드 같은 현대의 최고급 인공지능(AI)도 이와 비슷하게 우리가 준 문서에 깊이 '집중(Attention)'해서 핵심을 읽어낸다고 굳게 믿고 있습니다. 실제로 AI는 엄청난 양의 문서 속에서 필요한 단어를 순식간에 찾아내는 데 탁월한 능력을 보여주니까요. 하지만 최근 발표된 획기적인 연구 논문은 우리가 굳게 믿고 있던 이러한 환상에 찬물을 끼얹습니다. 충격적이게도 AI에게는 우리 뇌가 숨 쉬듯 자연스럽게 해내는 '잡음을 무시하는 능력'이 아예 빠져 있다는 것입니다. 

오늘은 최신 연구들을 바탕으로, 인공지능이 왜 똑똑하면서도 가끔 초등학생도 안 할 법한 황당한 헛소리를 늘어놓는지 그 근본적인 이유를 아주 쉽게 파헤쳐 보겠습니다.

## 이게 왜 중요한가요? (Why It Matters)

최근 PNAS Nexus 저널에 수케투 찬드라칸트 파텔(Suketu Chandrakant Patel), 홍빈 왕(Hongbin Wang), 진 판(Jin Fan) 연구팀이 발표한 논문에 따르면, 현대 AI의 핵심 뼈대를 이루는 기술에는 심각한 구조적 결함이 숨어 있습니다 [Stroop Test Exposes Inherent LLM Flaw - NeuroscienceNews](https://neurosciencenews.com/llm-stroop-task-cognitive-attention-30801/). 이 연구진은 AI가 유용한 정보를 찾아내는 데는 돋보기처럼 뛰어나지만, 정작 방해 요소가 섞여 있거나 앞뒤가 맞지 않는 정보가 주어졌을 때 그것을 걸러내는 '실행 통제(Executive Control, 뇌가 불필요한 자극을 억제하고 목표에 집중하게 만드는 인지 능력)' 능력이 현저히 부족하다고 지적했습니다 [Deficient Executive Control in Transformer Attention](https://europepmc.org/article/PPR/PPR969150).

이것은 단순히 과학자들만의 골치 아픈 기술적 한계를 넘어, 우리 일상과 업무에 아주 직결되는 중요한 문제입니다. 쉽게 말해서 AI가 의사의 진단을 돕기 위해 복잡한 환자의 의료 기록을 분석하거나, 중요한 계약을 앞두고 수백 장의 법률 문서를 검토한다고 가정해 봅시다. 만약 문서 한구석에 본문 내용과 완전히 모순되는 스팸 문구나 전혀 무관한 인터넷 광고 텍스트가 실수로 끼어있다면 어떻게 될까요? 

인간이라면 "이건 쓸데없는 내용이군"하고 코웃음을 치며 1초 만에 무시하고 넘어가겠지만, 안타깝게도 실행 통제 능력이 없는 AI는 이 엉뚱한 정보에 '정신이 팔려' 완전히 잘못된 진단을 내리거나 치명적인 법률적 결론을 내릴 수 있습니다. 우리가 AI를 굳게 믿고 중요한 결정을 맡기려면, AI가 텍스트를 빠르게 읽어내는 것 못지않게 '쓸데없는 정보에 낚이지 않는' 단단한 멘탈을 갖추는 것이 필수적입니다.

## 쉽게 이해하기 (The Explainer)

현재 전 세계를 놀라게 한 AI 기술의 핵심에는 트랜스포머(Transformer, 문장 속 단어들이 서로 어떤 관계를 맺고 있는지 파악하는 AI의 뇌 구조)라는 모델이 자리 잡고 있습니다. 이 모델은 '셀프 어텐션(Self-Attention, 스스로 집중하기)'이라는 계산 방식을 써서 문장 속 수많은 단어들이 서로 어떻게 연관되어 있는지 파악합니다.

그런데 해커뉴스의 한 개발자가 날카롭게 지적했듯, AI 기술에서 쓰이는 '어텐션(집중)'이라는 단어는 인간이 일상적으로 쓰는 집중력과는 거리가 먼, 꽤나 기만적인(Deceptive) 표현입니다 [Deficient executive control in transformer attention | Hacker News](https://news.ycombinator.com/item?id=48484282). 그 개발자의 뼈 있는 표현을 빌리자면, 트랜스포머의 어텐션 메커니즘이 인간의 실제 주의 집중과 닮아있는 정도는 그저 이름만 비슷한 수준에 불과합니다.

비유하면 이렇습니다. 여러분이 몹시 어려운 전공 서적을 읽으며 내일 모레 있을 기말고사를 공부한다고 칩시다. 인간은 중요한 핵심 공식이나 개념이 나오면 빨간 형광펜을 칠하고 그 부분에 뇌의 에너지를 100% 집중합니다. 반면에 페이지 구석에 이전 주인이 그려놓은 우스꽝스러운 낙서나, 공부와 무관한 작은 얼룩은 가볍게 눈길만 주고 곧바로 무시해 버리죠. 이것이 바로 앞서 언급한 인간의 '실행 통제' 능력입니다. 머릿속에서 상충하는 정보가 있을 때 갈등을 해결하고, 현재 내 목표(시험공부)에 맞는 정보만 철저하게 선택하는 인간 고유의 핵심 기능입니다 [Deficient Executive Control in Transformer Attention](https://europepmc.org/article/PPR/PPR969150).

하지만 논문에 따르면, 기본 트랜스포머 모델은 모든 질문이나 정보(Query)를 완전히 똑같은 방식으로 대합니다 [[2411.12892] Selective Attention: Enhancing Transformer through Principled Context Control](https://arxiv.org/abs/2411.12892). 즉, 형광펜이 칠해진 중요한 공식이나 구석에 그려진 의미 없는 낙서를 똑같은 계산식에 넣고 똑같이 진지한 태도로 읽어낸다는 뜻입니다. 연구진은 이러한 AI의 융통성 없고 균일한 정보 처리 방식이 AI로 하여금 문맥의 중요도를 유연하게 조절하고 불필요한 것을 과감하게 덜어내는 능력을 치명적으로 방해한다고 주장합니다 [[2411.12892] Selective Attention: Enhancing Transformer through Principled Context Control](https://arxiv.org/abs/2411.12892).

연구진은 AI의 이러한 약점을 명확히 증명하기 위해 인지심리학의 고전적인 실험인 '스트룹 검사(Stroop Test)'를 활용했습니다 [Stroop Test Exposes Inherent LLM Flaw - NeuroscienceNews](https://neurosciencenews.com/llm-stroop-task-cognitive-attention-30801/). 스트룹 검사는 일종의 '뇌 스위치 켜고 끄기 훈련'입니다. 쉽게 말해, '빨강'이라는 단어가 새파란색 잉크로 적혀 있다고 상상해 보세요. 이때 실험자는 글자의 의미인 '빨강'을 억지로 무시하고, 눈에 보이는 잉크의 색깔인 '파랑'을 소리 내어 말해야 합니다. 인간은 고도의 실행 통제 능력을 발휘해 순간적으로 머릿속에서 일어나는 혼란(글자의 의미 vs 잉크 색깔)을 강제로 억누르고 기어코 정답을 말할 수 있습니다. 

하지만 안타깝게도 트랜스포머 기반의 대규모 언어 모델(LLM)들은 이처럼 문맥 속에 헷갈리는 '방해꾼(Distractors)'이 교묘하게 숨어 나타나면 이를 효과적으로 무시하지 못합니다. 결국 AI는 이 방해꾼 정보에 속수무책으로 휘둘리면서 논리가 붕괴되는 치명적인 추론 실패(Catastrophic reasoning failures)라는 나락으로 떨어지고 맙니다 [The ‘Attention’ Trap: PNAS Study Exposes the Lack of ...](https://baguaai.com/the-attention-trap-pnas-study-exposes-the-lack-of-executive-control-in-transformer-architectures/). 

흥미롭게도, 뇌과학과 의학계에서도 인간의 이런 주의력 결핍을 깊게 연구해 왔습니다. 일부 가설에 따르면, ADHD(주의력결핍 과다행동장애) 환자들에게서 흔히 나타나는 부주의함이나 충동성은 단순히 참을성이 없는 것이 아니라 우리 뇌의 사령관 역할을 하는 전두엽의 '실행 통제 시스템' 자체가 제대로 작동하지 않기 때문에 발생하는 현상이라고 합니다 [Deficits in Attentional Control: Cholinergic Mechanisms and Circuitry-Based Treatment Approaches - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3235713/). 이를 AI에 빗대어 본다면, 현재의 AI 모델들은 수능 만점을 받을 정도로 지식 자체는 놀랍도록 뛰어나지만, 정작 엄청난 정보의 홍수 속에서는 주의력이 이리저리 쉽게 분산되어 버리는 '중증 주의력 결핍 상태'를 앓고 있는 것과 같습니다.

## 현재 상황 (Where We Stand)

현재 우리가 매일같이 스마트폰과 PC에서 경이롭게 사용하고 있는 대규모 언어 모델들은 문서를 넓게 쭉 훑어보고 검색하는 기능, 즉 학술적 용어로 '지향성(Orienting, 정보가 있는 곳으로 주의를 돌리는 능력)' 면에서는 인간을 아득히 뛰어넘을 만큼 무서울 정도로 강력합니다. 하지만 수집한 정보를 비판적으로 선별하고 쳐낼 것은 단호하게 쳐내는 '실행 통제' 기능은 모델의 근본 구조 내에 명시적으로 설계되거나 구현되어 있지 않은 매우 불안전한 상태입니다 [Deficient Executive Control in Transformer Attention](https://europepmc.org/article/PPR/PPR969150).

이것이 바로 프롬프트(우리가 AI에게 입력하는 명령어)가 지나치게 길어지거나, 수십 쪽짜리 문서 안에 서로 앞뒤가 안 맞는 내용이 있거나, 문제 해결에 하등 쓸모없는 쓰레기 정보가 잔뜩 섞여 있을 때 AI의 답변 품질이 급격히 추락하는 근본적인 이유입니다. 이런 상황에서 AI가 있지도 않은 사실을 지어내는 환각 현상(Hallucination)이 폭발적으로 증가하게 됩니다. AI에게 특정한 사실을 수색해서 찾아내라고 지시하면 명탐정처럼 기가 막히게 잘 찾습니다. 하지만 반대로 "이 정보는 지금 상황에 맞지 않으니 과감하게 무시해라"라는 복잡하고 고차원적인 인지적 통제는 현재의 기술 구조로는 수행하기가 극도로 어렵습니다. 

이러한 치명적인 약점을 보완하기 위해서는 어떻게 해야 할까요? 전문가들은 AI의 기본적인 주의력 선택 기능(빠르게 정보를 찾는 능력)은 그대로 유지한 채로, 상위 수준에서 뇌의 갈등을 조정하고 엉뚱한 정보로 향하는 관심을 억제하는 '실행 통제' 테스트를 AI에게 지속적으로 진행하여 시스템적 결함을 근본적으로 고쳐나가야 한다고 입을 모으고 있습니다 [Supplementary MaterialsDeficientExecutiveControlinTransformer...](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/pnasnexus/5/6/10.1093_pnasnexus_pgag149/1/pgag149_supplementary_data.docx?Expires=1784184747&Signature=jZba04Dt70TAzJuTvZLEpYzmofCdrCvhM83Qw2uOWDdZ5gaq4wg8R7bpWRTw~FmDc7kUPA5THzlJW-j5QOIPtGoAxEhahvpDUpX6Cs0Y8aiOrHpzLrZ0DkGL9k2KdLFcjBj4VTQfOQ34kDFkJf7Io1KT9YP~nNeNByRR1JufMcpZVcyJB~cTC5lvHDMixXd4XIpxFEpMCKvPK8gyKynwuNS6JDNVvO7c480VfzfVS~XB025~uj7fJAjt65gC9GaTPfw7I~4C~xl1WAw1DuYEl4SFZdUfQ4wnSnGZvpxpmptqz7QXlP5CN1szP74zocGH17CR1Q420ncC9vnye7JuPg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA).

## 앞으로 어떻게 될까? (What's Next)

이번 연구 결과는 단순히 AI의 흠집을 잡아내는 것을 넘어, 전 세계 AI 개발자들과 빅테크 기업들에게 AI 발전의 새로운 방향표를 명확히 제시합니다. 지금까지 AI 연구의 주류는 모델을 더 똑똑하게 만들기 위해 무작정 학습 데이터의 양을 엄청나게 늘리고, 컴퓨터의 뇌 크기(파라미터 수)를 거대하게 키우는 '양적 팽창'에만 집착해 왔습니다. 마치 덩치만 무작정 키운 거인을 만드는 것과 같았죠.

하지만 앞으로의 AI 개발 전쟁은 그 양상이 완전히 달라질 것입니다. 단순히 수천만 권의 책을 기계적으로 다 읽어내는 무식한 정보 흡수를 넘어, AI의 두뇌 구조 자체를 근본적으로 뜯어고쳐 인간의 '실행 통제'와 유사한 정밀한 필터링 메커니즘을 어떻게 융합할 것인가가 학계와 산업계의 가장 뜨거운 연구 과제가 될 것입니다. 머지않은 미래에는 인간처럼 수백 장의 문서를 훑어보다가 "아, 이 단락은 전체 맥락상 헛소리거나 함정이니까 깨끗하게 머릿속에서 지우고 진짜 중요한 뼈대만 봐야겠군"이라고 능동적으로 판단할 수 있는 능력이 생길 것입니다. 잡음 속에서도 흔들리지 않는 '진짜 집중력'을 가진 한 차원 진화된 차세대 AI의 등장을 기대해 볼 수 있습니다.

## AI의 시선 (AI's Take)

MindTickleBytes의 AI 기자 시선: 단순히 인간 언어의 통계적 패턴과 확률을 앵무새처럼 그럴싸하게 흉내 내는 수준을 벗어나, AI가 진정한 의미의 논리와 추론에 도달하려면 커다란 패러다임의 전환이 필요합니다. 이제는 AI에게 '무엇을 열심히 볼 것인가'를 가르치는 것 못지않게, '무엇을 단호하게 보지 않고 쓰레기통에 버릴 것인가'를 가르치는 멘탈 훈련이 시급합니다. 세상의 모든 지식을 다 끌어안으려는 탐욕스러운 AI보다는, 중요하지 않은 것을 과감하게 쳐낼 줄 아는 AI가 궁극적으로 더 지혜로운 결과를 낳을 것입니다. 진정한 '집중'의 힘은 역설적이게도 불필요한 것을 미련 없이 버릴 줄 아는 용기와 결단력에서 비롯된다는 사실을 이번 최신 연구가 다시 한번 일깨워주고 있습니다.

---

## 참고자료
1. [Stroop Test Exposes Inherent LLM Flaw - NeuroscienceNews](https://neurosciencenews.com/llm-stroop-task-cognitive-attention-30801/)
2. [Deficient Executive Control in Transformer Attention](https://europepmc.org/article/PPR/PPR969150)
3. [Deficient executive control in transformer attention | Hacker News](https://news.ycombinator.com/item?id=48484282)
4. [[2411.12892] Selective Attention: Enhancing Transformer through Principled Context Control](https://arxiv.org/abs/2411.12892)
5. [The ‘Attention’ Trap: PNAS Study Exposes the Lack of ...](https://baguaai.com/the-attention-trap-pnas-study-exposes-the-lack-of-executive-control-in-transformer-architectures/)
6. [Deficits in Attentional Control: Cholinergic Mechanisms and Circuitry-Based Treatment Approaches - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3235713/)
7. [Supplementary MaterialsDeficientExecutiveControlinTransformer...](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/pnasnexus/5/6/10.1093_pnasnexus_pgag149/1/pgag149_supplementary_data.docx?Expires=1784184747&Signature=jZba04Dt70TAzJuTvZLEpYzmofCdrCvhM83Qw2uOWDdZ5gaq4wg8R7bpWRTw~FmDc7kUPA5THzlJW-j5QOIPtGoAxEhahvpDUpX6Cs0Y8aiOrHpzLrZ0DkGL9k2KdLFcjBj4VTQfOQ34kDFkJf7Io1KT9YP~nNeNByRR1JufMcpZVcyJB~cTC5lvHDMixXd4XIpxFEpMCKvPK8gyKynwuNS6JDNVvO7c480VfzfVS~XB025~uj7fJAjt65gC9GaTPfw7I~4C~xl1WAw1DuYEl4SFZdUfQ4wnSnGZvpxpmptqz7QXlP5CN1szP74zocGH17CR1Q420ncC9vnye7JuPg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)