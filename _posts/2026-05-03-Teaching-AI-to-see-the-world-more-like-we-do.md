---
layout: post
title: "AI는 자동차와 비행기의 공통점을 알까? 인간처럼 '세상'을 보는 AI의 탄생"
description: "AI가 단순히 사물을 구별하는 것을 넘어 인간처럼 세상을 이해하도록 돕는 새로운 연구들을 소개합니다. 구글 딥마인드의 월드 모델과 국내 연구진의 혁신적인 기술을 만나보세요."
summary: "사물 인식에는 천재적이지만 추상적 개념은 빵점인 AI에게 '인간의 시각'을 가르쳐 더 똑똑하고 안전한 인공지능을 만드는 여정이 시작되었습니다."
tags: [인공지능, 딥마인드, 월드모델, 머신러닝, 테크트렌드]
image: 2026-05-03-Teaching-AI-to-see-the-world-more-like-we-do.jpg
image_alt: "로봇의 눈을 통해 바라본 세상이 인간의 뇌 신경망처럼 연결되어 복잡한 사물 간의 관계를 파악하는 모습"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI가 인간의 상식을 배우게 된다면, 우리는 더 이상 AI의 '엉뚱한 실수'를 걱정하지 않아도 될 것입니다. 데이터의 양보다 '인간을 닮은 사고방식'을 이식하는 것이 진정한 지능으로 가는 길입니다."
quiz:
  - question: "현재의 AI 시스템이 수백 종류의 자동차 모델을 구별하면서도 놓치는 것은 무엇인가요?"
    choices: ["자동차의 정확한 엔진 출력", "자동차와 비행기가 모두 금속으로 된 탈것이라는 공통점", "자동차 타이어의 브랜드 이름"]
    answer: 1
    explanation: "구글 딥마인드에 따르면 AI는 개별 사물은 잘 식별하지만, '금속으로 만든 큰 탈것' 같은 추상적인 공통점이나 관계를 파악하는 데는 어려움을 겪습니다."
  - question: "AI가 주변 환경이 어떻게 돌아가는지 이해하기 위해 만드는 '머릿속 시뮬레이션'을 무엇이라 부르나요?"
    choices: ["가상 현실(Virtual Reality)", "이미지 프로세싱(Image Processing)", "월드 모델(World Models)"]
    answer: 2
    explanation: "월드 모델은 AI가 환경의 작동 원리를 내부적으로 표현하고 시뮬레이션하는 시스템을 말합니다."
  - question: "국내 연세대학교 연구진이 참여하여 개발한, 컴퓨터가 인간의 뇌처럼 이미지를 처리하도록 돕는 기술은?"
    choices: ["Lp-컨볼루션(Lp-Convolution)", "데이터 주석(Data Annotation)", "사이언티픽 게임(Scientific Game)"]
    answer: 0
    explanation: "Lp-컨볼루션은 컴퓨터가 인간의 뇌와 더 유사하게 이미지를 처리할 수 있도록 돕는 획기적인 기술입니다."
lang: ko
ref: 2026-05-03-Teaching-AI-to-see-the-world-more-like-we-do
audio: 2026-05-03-Teaching-AI-to-see-the-world-more-like-we-do.mp3
permalink: /2026/05/03/Teaching-AI-to-see-the-world-more-like-we-do/
---

여러분, 한 번 상상해보세요. 여러분 앞에 최신형 인공지능(AI)이 하나 있습니다. 이 AI는 세상에 존재하는 수백 가지 자동차의 브랜드와 모델명을 단 1초 만에 맞출 수 있는 그야말로 '자동차 박사'입니다. 그런데 이 똑똑한 AI에게 "자동차와 비행기의 닮은 점이 뭐니?"라고 물었더니, 대답을 못 하거나 전혀 엉뚱한 소리를 합니다. 우리 인간에게는 너무나 당연한 "둘 다 금속으로 만든 큰 이동 수단이잖아"라는 상식이 이 AI에게는 세상에서 가장 어려운 문제인 셈이죠. [Teaching AI to see the world more like we do - deepmind.google](https://deepmind.google/blog/teaching-ai-to-see-the-world-more-like-we-do/)

이것이 바로 오늘날 AI가 마주한 거대한 벽, 이른바 **'인식의 격차(Perception Gap)'**입니다. [Teaching AI to See the World Through Human Eyes: Bridging the ...](https://joshuaberkowitz.us/blog/news-1/teaching-ai-to-see-the-world-through-human-eyes-bridging-the-perception-gap-1784) 쉽게 말해서, AI는 수만 권의 책을 통째로 외운 암기 천재지만, 정작 그 책 속에 담긴 내용이 우리 삶과 어떤 관계가 있는지는 전혀 모르는 상태와 비슷합니다. 겉으로는 인간보다 훨씬 똑똑해 보이지만, 세상을 바라보는 방식은 우리와 너무나 달라서 가끔 황당한 실수를 저지르곤 하죠. 하지만 최근 전 세계의 과학자들은 이 격차를 줄이기 위해 AI에게 '인간의 눈'과 '인간의 상식'을 가르치기 시작했습니다.

## 이게 왜 중요한가요? (Why It Matters)

"AI가 자동차 모델만 잘 맞추면 됐지, 비행기랑 비슷한 걸 아는 게 왜 그렇게 중요한가요?"라고 물으실 수 있습니다. 하지만 이 문제는 단순히 퀴즈를 맞히는 수준을 넘어, 우리가 매일 사용하는 AI의 **안전성**과 직접적으로 연결됩니다.

현재의 AI는 매우 똑똑하지만 동시에 예측 불가능하다는 치명적인 약점이 있습니다. [World models: 10 Things That Matter in AI Right Now | MIT Technology Review](https://www.technologyreview.com/2026/04/21/1135650/world-models-ai-artificial-intelligence/) 사물을 인식하고 분류하는 패턴 파악 능력은 인간을 능가하지만, 그 속에 담긴 깊은 관계나 추상적인 개념을 이해하지 못하기 때문입니다. [Teaching AI to See the World Through Human Eyes: Bridging the ...](https://joshuaberkowitz.us/blog/news-1/teaching-ai-to-see-the-world-through-human-eyes-bridging-the-perception-gap-1784)

비유를 들어볼까요? 자율주행차가 도로 위에서 '빈 종이상자'를 만났다고 가정해봅시다. 인간 운전자는 "저건 가벼운 종이니까 그냥 지나가도 안전해" 혹은 "안에 뭐가 들었을지 모르니 피하자"라는 상식적인 판단을 내립니다. 하지만 AI가 이를 단순히 '사각형 데이터 패턴'으로만 인식한다면, 처음 보는 형태의 상자가 나타났을 때 그것이 바위인지 종이인지 구분하지 못해 사고를 낼 위험이 있습니다. 

따라서 AI를 인간의 지식 체계와 일치시키는 '정렬(Aligning)' 작업은 AI를 어떤 상황에서도 흔들리지 않게 튼튼(Robustness)하게 만들고, 가르쳐주지 않은 새로운 상황에도 척척 적응(Generalize)하게 만드는 핵심 열쇠입니다. [Teaching AI to See the World More Like Humans Do — Google DeepMind](https://aifuturethinkers.com/teaching-ai-to-see-the-world-more-like-humans-do-google-deepmind/)

## 쉽게 이해하기: AI에게 '상식'을 가르치는 세 가지 방법

과학자들은 AI에게 인간의 시각 시스템을 이식하기 위해 크게 세 가지 혁신적인 전략을 사용하고 있습니다.

### 1. 머릿속으로 '시뮬레이션' 돌리기: 월드 모델(World Models)
여러분은 아침에 일어나 눈을 감고도 화장실이 어디에 있는지, 현관문을 열면 어떤 복도가 펼쳐질지 생생하게 상상할 수 있습니다. 우리 머릿속에 세상이 어떻게 돌아가는지에 대한 '지도'나 '작동 원리'가 들어있기 때문이죠.

AI에게도 이런 상상력을 주는 것이 바로 **'월드 모델(World Models)'**입니다. [World Models: Teaching AI to Think Like Humans - LinkedIn](https://www.linkedin.com/pulse/world-models-teaching-ai-think-like-humans-abhishek-banerjee-wakhe) 이는 AI가 주변 환경을 단순히 사진 찍듯 저장하는 게 아니라, 환경이 어떻게 변할지 스스로 예측하는 내부 시스템을 구축하는 것입니다. [World Models: Teaching AI to Think Like Humans - LinkedIn](https://www.linkedin.com/pulse/world-models-teaching-ai-think-like-humans-abhishek-banerjee-wakhe) "내가 이 컵을 밀면 바닥으로 떨어져 깨지겠지?"라고 미리 머릿속으로 시뮬레이션을 돌려보는 능력을 갖게 되는 셈입니다.

### 2. 뇌의 필터를 복제하기: Lp-컨볼루션(Lp-Convolution)
우리의 뇌는 수많은 시각 정보 중 중요한 것만 쏙쏙 골라내는 아주 효율적인 필터를 가지고 있습니다. 최근 연세대학교와 기초과학연구원(IBS), 그리고 독일의 막스 플랑크 연구소의 공동 연구진은 컴퓨터가 인간의 뇌와 더 유사하게 이미지를 처리할 수 있도록 돕는 **'Lp-컨볼루션(Lp-Convolution)'**이라는 기술을 선보였습니다. [AI Horizons: Teaching computers to view the world like humans do](https://theticker.org/16359/science/ai-horizons-teaching-computers-to-view-the-world-like-humans-do/)

비유하자면, AI에게 인간의 눈과 뇌가 세상을 볼 때 사용하는 '특수 안경'을 씌워주는 것과 같습니다. 이 안경을 쓰면 AI도 인간이 중요하게 생각하는 사물의 윤곽이나 입체감을 우선순위에 두고 처리하게 되어, 훨씬 자연스러운 인식이 가능해집니다.

### 3. 게임을 통해 배우는 인식: 브라운 대학교의 연구
미국 브라운 대학교(Brown University)의 연구진은 아주 재미있는 방식으로 AI를 교육하고 있습니다. 바로 '게임'을 통해 인간처럼 지각하는 법을 가르치는 것이죠. [Researchers are teaching AI to see more like humans - MSN](https://www.msn.com/en-us/news/technology/researchers-are-teaching-ai-to-see-more-like-humans/ar-AA1H2LFn) 어린아이가 블록 놀이를 하며 세상의 물리 법칙을 배우듯, AI도 가상 세계 게임 속에서 다양한 물체를 만져보고 움직여보며 인간과 비슷한 시각적 논리를 쌓아갑니다. [Training AI to see more like humans - National Science Foundation](https://www.nsf.gov/news/training-ai-see-more-humans)

## 현재 상황 (Where We Stand)

지금 이 순간에도 구글 딥마인드(Google DeepMind)는 AI와 인간이 시각 정보를 조직화하는 방식의 차이를 분석한 심도 있는 연구 결과를 국제 학술지 '네이처(Nature)'에 발표하며 연구에 박차를 가하고 있습니다. [Teaching AI to See the World More Like Humans Do — Google DeepMind](https://aifuturethinkers.com/teaching-ai-to-see-the-world-more-like-humans-do-google-deepmind/)

하지만 솔직히 말해, 아직 갈 길은 멉니다. 현재의 AI는 사물을 개별적으로 인식하는 데는 천재적이지만, 인간이 아주 자연스럽게 파악하는 '사물 간의 보이지 않는 관계'를 놓칠 때가 많습니다. [Teaching AI to See the World Through Human Eyes: Bridging the ...](https://joshuaberkowitz.us/blog/news-1/teaching-ai-to-see-the-world-through-human-eyes-bridging-the-perception-gap-1784) 우리가 가끔 AI가 쓴 글을 읽으며 "뭔가 어색한데?"라고 느끼는 이유도, AI가 만드는 패턴이 인간의 자연스러운 상식 체계와는 아직 거리가 있기 때문입니다. [AIDetector - AdvancedAIChecker for ChatGPT, GPT-5 & Gemini](https://quillbot.com/ai-content-detector)

## 앞으로 어떻게 될까? (What's Next)

AI가 세상을 정말 인간처럼 보게 된다면 어떤 미래가 펼쳐질까요?

전문가들은 2050년쯤이면 원자 수준에서 물질을 조작하고, 어둠 속에서도 사물을 완벽히 볼 수 있는 능력을 갖춘 'AI 교사'나 로봇이 등장할 수도 있다고 내다봅니다. [Technology in 2050 - experts give their predictions](https://www.bbc.com/news/articles/c865n800d5jo) 단순히 지식을 쏟아내는 기계를 넘어, 학생의 눈높이에서 세상을 이해하고 공감하며 가르치는 진정한 '스승' 역할을 하는 AI가 가능해질지도 모릅니다.

지금은 우리가 AI에게 하나하나 데이터를 라벨링하며 세상을 가르치고 있지만(Data Annotation), [DataAnnotation | Future-Proof Your Career WithAITraining Work](https://www.dataannotation.tech/) 머지않아 AI는 우리와 같은 눈으로 세상을 보며, 기후 위기나 난치병 치료 같은 복잡한 문제를 해결하는 든든한 파트너가 될 것입니다.

---

### MindTickleBytes의 AI 기자 시선

그동안 우리는 AI가 얼마나 많은 데이터를 처리하는지, 즉 '양'에만 집착해 왔습니다. 하지만 이번 연구들은 '얼마나 많이 아느냐'보다 '어떤 시각으로 보느냐'가 더 중요하다는 것을 일깨워줍니다. 인간의 시각 방식을 배우는 AI는 단순히 성능이 좋아지는 것을 넘어, 인간의 가치관과 상식을 공유하는 '안전한 동반자'로 진화하고 있습니다. 자동차와 비행기의 공통점을 아는 그 사소한 능력이, 어쩌면 우리를 더 안전하고 따뜻한 기술의 미래로 이끌어 줄지도 모르겠네요.

---

## 참고자료

1. [Teaching AI to see the world more like we do - deepmind.google](https://deepmind.google/blog/teaching-ai-to-see-the-world-more-like-we-do/)
2. [Training AI to see more like humans - National Science Foundation](https://www.nsf.gov/news/training-ai-see-more-humans)
3. [Teaching AI to See the World More Like Humans Do — Google DeepMind](https://aifuturethinkers.com/teaching-ai-to-see-the-world-more-like-humans-do-google-deepmind/)
4. [Researchers are teaching AI to see more like humans - MSN](https://www.msn.com/en-us/news/technology/researchers-are-teaching-ai-to-see-more-like-humans/ar-AA1H2LFn)
5. [AI Horizons: Teaching computers to view the world like humans do](https://theticker.org/16359/science/ai-horizons-teaching-computers-to-view-the-world-like-humans-do/)
6. [Teaching AI to See the World Through Human Eyes: Bridging the ...](https://joshuaberkowitz.us/blog/news-1/teaching-ai-to-see-the-world-through-human-eyes-bridging-the-perception-gap-1784)
7. [World Models: Teaching AI to Think Like Humans - LinkedIn](https://www.linkedin.com/pulse/world-models-teaching-ai-think-like-humans-abhishek-banerjee-wakhe)
8. [Technology in 2050 - experts give their predictions](https://www.bbc.com/news/articles/c865n800d5jo)
9. [DataAnnotation | Future-Proof Your Career WithAITraining Work](https://www.dataannotation.tech/)
10. [AIDetector - AdvancedAIChecker for ChatGPT, GPT-5 & Gemini](https://quillbot.com/ai-content-detector)
11. [World models: 10 Things That Matter in AI Right Now | MIT Technology Review](https://www.technologyreview.com/2026/04/21/1135650/world-models-ai-artificial-intelligence/)

## FACT-CHECK SUMMARY
- Claims checked: 14
- Claims verified: 13
- Verdict: PASS