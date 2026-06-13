---
layout: post
title: "과거의 지식만 배운 AI가 미래를 예측할 수 있을까? '빈티지 LLM'의 세계"
description: "최신 인터넷 지식을 차단하고 1930년 이전의 과거 데이터로만 훈련시킨 '빈티지 LLM'의 원리와, 인공지능을 바닥부터 직접 만들어보는 개발자들의 흥미로운 도전을 알기 쉽게 설명합니다."
summary: "과거의 텍스트로만 훈련된 '빈티지 LLM'을 바닥부터 직접 개발하는 프로젝트들이 늘어나며, AI의 구조적 이해와 역사적 미래 예측이라는 흥미로운 실험이 진행되고 있습니다."
tags: [인공지능, 거대언어모델, 빈티지LLM, 테크트렌드, 머신러닝]
image: 2026-06-14-Making-a-vintage-LLM-from-scratch.jpg
image_alt: "오래된 타자기가 놓인 나무 책상 위에서 홀로그램으로 떠오른 현대적인 인공지능 신경망의 모습"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "완제품만 소비하는 시대에, 기저의 원리를 깨우치기 위해 직접 바닥부터 AI를 조립하는 개발자들의 장인 정신이 놀랍습니다."
quiz:
  - question: "개발자들이 '빈티지 LLM'을 굳이 처음부터(from scratch) 직접 만들어보는 가장 핵심적인 이유는 무엇인가요?"
    choices: ["인터넷 연결이 끊긴 오프라인 환경에서 챗봇을 상업적으로 판매하기 위해서", "어셈블리어로 코드를 작성해 컴퓨터 하드웨어를 직접 제어하기 위해서", "거대한 언어 모델이 이면에서 어떻게 작동하는지에 대한 통찰력을 얻고 원리를 깊이 이해하기 위해서"]
    answer: 2
    explanation: "완성된 대형 모델을 가져다 쓰기보다 처음부터 직접 만들어보는 것은, 복잡한 인공지능 시스템이 내부에서 어떻게 작동하는지에 대한 귀중한 통찰력을 제공하기 때문입니다."
  - question: "기사에서 '빈티지 LLM'을 정의하는 가장 정확한 설명은 무엇인가요?"
    choices: ["특정 지식 단절(knowledge-cutoff) 날짜 이후의 정보 없이, 제한된 역사적 기간의 텍스트로만 훈련된 언어 모델", "성능이 떨어지는 구형 컴퓨터에서도 작동할 수 있도록 기능이 극도로 축소된 최신 언어 모델", "오래된 프로그래밍 언어만을 사용하여 개발된 1990년대 방식의 인공지능"]
    answer: 0
    explanation: "빈티지 LLM은 특정한 과거 시점(예: 1930년 이전, 또는 2019년)까지의 텍스트 및 다중 양식 데이터로만 훈련되고, 그 이후의 미래 지식은 전혀 포함되지 않은 모델을 의미합니다."
  - question: "본문에서 언급된, 기존 모델을 업데이트할 때 처음부터 완전히 다시 학습시키지 않고 컴퓨팅 파워의 5%만 사용하여 품질 저하를 막고 속도를 높일 수 있는 기술은 무엇인가요?"
    choices: ["나노GPT (NanoGPT)", "그룹-쿼리 어텐션 (GQA, Group-query attention)", "파이토치 (PyTorch)"]
    answer: 1
    explanation: "그룹-쿼리 어텐션(GQA)은 기존 체크포인트에서 원래 훈련 연산량의 단 5%만 사용해 모델을 업트레이닝(up-training)함으로써, 처음부터 재학습하는 비용을 아끼면서도 성능을 향상시키는 기술입니다."
lang: ko
ref: 2026-06-14-Making-a-vintage-LLM-from-scratch
audio: 2026-06-14-Making-a-vintage-LLM-from-scratch.mp3
permalink: /2026/06/14/Making-a-vintage-LLM-from-scratch/
---

잠시 재미있는 상상을 해보겠습니다. 여러분이 타임머신을 타고 1920년대로 돌아가서, 그 시대에 출판된 책, 신문, 사람들의 손 편지들만 잔뜩 모아 인공지능에게 읽게 한다면 어떨까요? 이 인공지능은 스마트폰이나 인터넷이 무엇인지도 모르고, 심지어 제2차 세계대전이 일어났다는 역사적 사실조차 알지 못할 것입니다. 오직 100년 전 사람들의 생각과 지식만을 고스란히 간직한 살아있는 '타임캡슐' 같은 존재가 되겠죠. 

오늘날 우리가 흔히 사용하는 챗GPT(ChatGPT) 같은 인공지능은 어제 일어난 전 세계의 뉴스와 최신 유행어, 복잡한 현대 과학 기술까지 모조리 알고 있는 척척박사입니다. 그런데 최근 인공지능 개발자들 사이에서는 최신 인터넷 지식을 과감하게 차단하고, 이렇게 특정한 과거 시대의 지식에만 머물러 있는 이른바 '빈티지 LLM'을 맨바닥부터 직접 만들어보는 아주 독특한 시도가 조용한 유행을 타고 있습니다. 

도대체 왜 세상에서 가장 똑똑하고 편리한 최신 기술을 놔두고, 과거의 지식에 갇힌 다소 바보 같은(?) 인공지능을 고생스럽게 직접 조립하고 있는 걸까요? 오늘 MindTickleBytes에서는 이 흥미롭고 기발한 기술적 역주행의 이면에 숨겨진 놀라운 비밀들을 여러분께 아주 알기 쉽게 설명해 드리겠습니다.

## 이게 왜 중요한가요? (Why It Matters)

최근 테크 업계에서는 거대 언어 모델(LLM, 방대한 텍스트 데이터를 학습해 사람처럼 대화하고 글을 쓰는 인공지능)을 스마트폰부터 회사 업무까지 일상 곳곳에 도입하고 있습니다. 모든 인공지능 모델이 세상의 최신 데이터를 탐욕스럽게 집어삼키며 똑똑해지려 할 때, 완전히 정반대의 길을 걷는 개념이 등장했습니다. 

바로 **'빈티지 LLM(Vintage LLM)'**입니다. 이는 명확하게 제한된 역사적 기간의 텍스트로만 훈련된 언어 모델을 의미하며, 특정한 '지식 단절(knowledge-cutoff, 인공지능이 학습한 데이터의 마지막 날짜)' 이후의 정보는 훈련 데이터에 전혀 포함되지 않는 특징을 가집니다 [Awesome-vintage-llms](https://github.com/entanglr/awesome-vintage-llms). 

조금 더 구체적으로 말하자면, 특정한 날짜(예를 들어 코로나19 팬데믹 이전인 2019년) 이전까지의 텍스트나 이미지 같은 한정된 데이터만을 사용해 학습시키는 것입니다 [Vintage Large Language Models](https://owainevans.github.io/talk-transcript.html?trk=article-ssr-frontend-pulse_little-text-block). 그 이후에 세상에 벌어진 일은 인공지능의 머릿속에 백지상태로 남겨두는 비교적 간단한 시도부터, 심지어 1930년 이전의 아주 오래된 데이터만을 사용해 모델을 창조해 내는 과감한 인공지능 프로젝트까지 다양하게 진행되고 있습니다 [This AI project uses pre-1930 data to create a "vintage LLM" for...](https://www.linkedin.com/posts/tmcai_this-ai-project-uses-pre-1930-data-to-create-activity-7455203545970143232-XqvV).

그렇다면 이런 엉뚱한 시도가 우리 현실에서 왜 중요할까요? 이 실험은 단순히 과거를 모방하는 괴짜들의 장난이 아닙니다. 빈티지 LLM을 통해 연구자들은 아주 거대하고 근본적인 질문을 던지고 있습니다. **"특정 역사적 시점까지의 데이터만 배운 인공지능이, 과연 그 이후에 벌어질 역사적 사건들을 얼마나 정확하게 예측할 수 있을까?"** 하는 점입니다 [This AI project uses pre-1930 data to create a "vintage LLM" for...](https://www.linkedin.com/posts/tmcai_this-ai-project-uses-pre-1930-data-to-create-activity-7455203545970143232-XqvV). 

상상해 보세요. 1929년 경제 대공황이 터지기 직전까지의 경제 지표와 사람들의 편지, 신문 기사만 읽은 인공지능이 과연 거대한 경제 폭락을 미리 경고할 수 있을까요? 이것은 오랜 철학의 주제인 '결정론(우주의 모든 사건은 이미 과거의 원인에 의해 결정되어 있다는 철학적 개념)'을 인공지능의 데이터 모델링을 통해 축소된 형태의 사회학적 실험으로 재현하는 것과 같습니다 [This AI project uses pre-1930 data to create a "vintage LLM" for...](https://www.linkedin.com/posts/tmcai_this-ai-project-uses-pre-1930-data-to-create-activity-7455203545970143232-XqvV). 

쉽게 말해서, 과거의 데이터를 기계적으로 꼼꼼히 분석하는 것만으로 미래 역사의 궤적을 맞출 수 있다면, 우리는 다가올 미래의 사회적, 경제적 위기를 예측할 수 있는 완전히 새로운 마법의 수정구슬을 얻게 되는 셈입니다.

## 쉽게 이해하기 (The Explainer)

그런데 이런 신기한 빈티지 인공지능을 굳이 왜 남의 것을 쓰지 않고 '처음부터(from scratch)' 바닥부터 낑낑대며 조립해서 만드는 걸까요? 이미 인터넷에 무료로 공개된 수많은 똑똑한 챗봇들의 지능을 조금만 낮춰서 쓰면 훨씬 편할 텐데 말입니다. 

여기, 이들의 마음을 아주 완벽하게 대변해 주는 무릎을 탁 치게 만드는 명언이 하나 있습니다. **"볼링을 잘 치는 방법에 대한 책을 백 번 읽는 것과, 실제로 볼링장에 가서 무거운 공을 굴려보는 것은 결코 똑같지 않다"**는 것입니다 [An LLM From "Scratch" | Hackaday](https://hackaday.com/2026/05/07/an-llm-from-scratch/). 

오늘날 거대 언어 모델이 세상의 패러다임을 혁신적으로 바꾸고 챗봇부터 코딩 비서까지 수많은 곳에 쓰이고 있지만, 사실 완성된 상업용 AI를 그냥 가져다 쓰는 것은 전자레인지에 냉동 피자를 3분 데워 먹는 것과 같습니다. 빠르고 편리하게 배를 채울 수는 있지만, 그 피자가 정확히 어떤 밀가루와 어떤 토핑으로 어떻게 만들어졌는지는 소비자는 전혀 알 길이 없죠. 

하지만 자신만의 LLM을 처음부터 바닥부터 직접 만들어보는 것은 다릅니다. 이 거대하고 복잡한 시스템이 보이지 않는 이면에서 실제로 어떻게 톱니바퀴처럼 맞물려 작동하는지에 대한 값을 매길 수 없는 귀중한 통찰력을 개발자에게 제공합니다 [Building Your Own LLM From Scratch: A Comprehensive Guide | by Palanikalyan | Medium](https://medium.com/@palanikalyan27/building-your-own-llm-from-scratch-a-comprehensive-guide-7e38d9624d47), [Building a Large Language Model (LLM) from Scratch | by Abdul Rauf | Medium](https://medium.com/@raufpokemon00/building-a-large-language-model-llm-from-scratch-61fed0570ea5). 코드를 한 줄 한 줄 땀 흘려 직접 짜면서, 모델의 내부 구조를 속속들이(inside out) 이해하게 되는 것이죠 [GitHub - rasbt/LLMs-from-scratch: Implement a ChatGPT-like LLM in ...](https://github.com/rasbt/LLMs-from-scratch).

크리스티 콘스탄틴(Cristi Constantin)이라는 한 열정적인 개발자는 오직 오래된 텍스트로만 훈련시킨 자신만의 빈티지 LLM을 정말 맨바닥에서부터 끈기 있게 만들어냈습니다. 그는 대기업이 만들어 놓은 편리한 시스템을 빌려 쓰지 않고, 인공지능의 뇌를 구성하는 기초적인 학습(base-training) 프로그램, 기존 지식을 더 예리하게 다듬는 미세 조정(fine-tuning) 과정, 수많은 과거 문헌의 먼지를 털어내고 정리하는 데이터 처리 파이프라인까지 모든 것을 자기 손으로 하나하나 구축했습니다 [Making a vintage LLM from scratch - Cr;Lf;](https://crlf.link/log/entries/260525-1/), [Making a vintage LLM from scratch · YAVCHN](https://yavchn.parkscomputing.com/hn/s/48487829). 이런 그의 좌충우돌 'AI 모험기'는 해커 뉴스(Hacker News) 같은 전 세계 유명 개발자 커뮤니티에서 폭발적인 공감과 화제를 모으기도 했습니다 [Making a vintage LLM from scratch - Hacker News](https://news.ycombinator.com/item?id=48487829).

물론 여기서 말하는 "맨바닥에서부터(from scratch)"라는 단어를 오해하시면 안 됩니다. 비유하자면 이렇습니다. 일류 셰프가 식당에서 빵을 '처음부터 직접' 정성껏 만든다고 할 때, 밀가루와 물을 직접 섞어 반죽을 치대고 오븐에 굽겠다는 의미이지, 당장 시골로 내려가 직접 밀 농사를 짓고 밭을 갈겠다는 뜻은 아닌 것과 같습니다. 

마찬가지로 인공지능 개발에서도 처음부터 만든다는 것이 컴퓨터가 인식하는 0과 1의 아주 원시적인 기계어 코드를 직접 타이핑하겠다는 의미는 아닙니다. 파이썬(Python) 같은 기존의 현대적이고 친숙한 프로그래밍 언어나, 파이토치(PyTorch)처럼 이미 널리 쓰이는 편리한 도구들을 블록 장난감의 밑판처럼 활용합니다 [Making a vintage LLM from scratch - Cr;Lf;](https://crlf.link/log/entries/260525-1/). 누군가는 이를 바탕으로 트랜스포머(Transformer, 문장의 단어들 사이 관계를 촘촘하게 엮어 맥락을 깊이 파악하는 AI의 가장 핵심적인 뼈대 구조) 모델을 파이토치로 처음부터 짜맞춰내는 쾌거를 달성하기도 하죠 [GitHub - FareedKhan-dev/train-llm-from-scratch: A straightforward ...](https://github.com/FareedKhan-dev/train-llm-from-scratch). 

심지어 기계가 문장을 읽을 때 스스로 어디에 더 집중해야 할지를 학습하게 만드는 '훈련 가능한 셀프 어텐션(trainable self-attention)' 구조까지 직접 코드로 짜보면서, 두꺼운 전공 서적에서 눈으로만 읽은 내용을 실전으로 체화하는 장인 같은 개발자들도 속속 등장하고 있습니다 [Writing an LLM from scratch, part 8 -- trainable self-attention](https://www.gilesthomas.com/2025/03/llm-from-scratch-8-trainable-self-attention).

## 현재 상황 (Where We Stand)

그렇다면 구글이나 마이크로소프트 같은 거대 기업의 축구장만 한 데이터센터가 없는 평범한 사람의 방구석 컴퓨터 환경에서도 과연 이런 복잡한 인공지능을 바닥부터 직접 만들어 볼 수 있을까요? 

놀랍게도 2026년 현재의 대답은 "충분히 가능하다"입니다. 기술의 비약적인 발전 덕분에, 단 8GB의 램(RAM) 용량(요즘 스마트폰이나 저렴한 사무용 노트북에도 기본으로 들어가는 아주 평범한 수준이죠)만을 가진 일반적인 중앙처리장치(CPU) 환경에서도 국지적(Local)으로 자신만의 LLM을 처음부터 구축하고 실행하는 것이 가능해졌습니다 [Building and Running LLMs Locally from Scratch - Complete 2026 Guide](https://amitray.com/building-running-llms-locally-from-scratch/). 

방대한 텍스트를 AI가 한입에 쏙쏙 소화할 수 있게 아주 잘게 쪼개는 토큰화(tokenization) 작업부터, 챗GPT의 원리를 조그맣게 축소해 놓은 나노GPT(NanoGPT) 아키텍처의 설계, 그리고 기본 훈련을 마친 AI에게 족집게 과외처럼 특별한 전문 지식을 가르치는 미세 조정 과정에 이르기까지. 마치 생명이 탄생하는 것 같은 인공지능 창조의 모든 과정을 여러분의 책상 위 낡은 노트북에서도 경험할 수 있게 된 것입니다 [Building and Running LLMs Locally from Scratch - Complete 2026 Guide](https://amitray.com/building-running-llms-locally-from-scratch/).

하지만 우리의 가슴 뛰는 상상력과는 별개로 현실을 냉정하게 직시할 필요도 있습니다. 개인이 집에서 직접 인공지능을 바닥부터 훈련시켜 보는 것은 컴퓨터 공학과 인공지능의 뼈대 원리를 체득하기 위한 매우 훌륭한 교육적, 기술적 훈련 과정임은 분명합니다. 하지만, 개인이 취미로 훈련시킨 이 자그마한 모델을 가리켜 "거대 테크 기업들이 천문학적인 돈을 쏟아부어 만든 최상위 모델인 '클로드(Claude)'를 단숨에 대체할 수 있는 실질적인 대안이다!"라고 선언한다면, 그것은 자기 자신에게 거대한 거짓말을 하는 것과 다름없습니다 [I Trained My Own LLM from Scratch in 2025: What... - DEV Community](https://dev.to/jtorchia/i-trained-my-own-llm-from-scratch-in-2025-what-that-viral-hn-tutorial-doesnt-tell-you-about-the-l66). 

개인이 뚝딱뚝딱 구축한 모델은 그 원리를 투명하고 선명하게 들여다보고, 과거의 역사적 데이터로 독특한 상상력을 발휘해 보는 교육용이나 연구용 장난감으로서는 최고의 가치를 지닙니다. 그러나 수천억 개의 데이터 조각으로 무장한 상용 서비스의 놀라운 지능과 철통같은 안전성, 범용성을 당장 따라잡을 수는 없습니다. 실제로 대기업들이 만든 인공지능조차 그들이 내뱉는 말이 얼마나 정확한지, 그리고 인간의 윤리와 안전 기준에 잘 부합하는지(alignment)를 엄밀하게 평가하는 방법론 자체가 현재 관련 업계에서 아주 크고 중요한 별개의 학문적 과제로 치열하게 다루어지고 있을 정도니까요 [Best Practices and Methods for LLM Evaluation | Databricks Blog](https://www.databricks.com/blog/best-practices-and-methods-llm-evaluation).

## 앞으로 어떻게 될까? (What's Next)

과거의 퀴퀴한 먼지가 쌓인 문헌들로 낡은 지식 체계를 구축하는 '빈티지 LLM' 실험과, 그것을 마치 프라모델 조립하듯 손수 만들어보는 열정적인 튜토리얼들은 앞으로 전 세계 개발자 커뮤니티에서 더욱 활발해질 것입니다. 아주 기초적인 개념부터 시작해 내 컴퓨터에 실제 프로그램을 띄우는 배포 단계에 이르는 친절하고 포괄적인 가이드들이 지금 이 순간에도 끊임없이 쏟아지고 있기 때문이죠 [How to Build an LLM from Scratch: A Comprehensive Guide | by Pratik Barjatiya | Medium](https://pratikbarjatya.medium.com/how-to-build-an-llm-from-scratch-a-comprehensive-guide-c84e87667326).

이러한 유행과 더불어, 인공지능을 훈련시키는 핵심 기술 자체도 멈추지 않고 눈부시게 진화하고 있습니다. 만약 인공지능 모델에 책 한 권 분량의 새로운 지식을 약간만 추가하려고 해도, 처음부터 엄청난 전기를 펑펑 소모하며 모든 것을 완전히 처음부터 재학습시켜야 했다면 이 흥미로운 실험들은 금방 높은 현실의 벽에 부딪혔을 것입니다. 하지만 다행히도 최근에는 '그룹-쿼리 어텐션(GQA, Group-query attention, 데이터 처리 효율을 극대화하는 최신 기술)'이라는 아주 훌륭한 개선책이 등장했습니다. 

이 기술을 활용하면 원래 기존의 모델들을 가르칠 때 굳이 뇌 구조를 싹 다 갈아엎고 처음부터 재학습시킬 필요가 없습니다. 놀랍게도 원래 모델을 처음 훈련시켰을 때 들어갔던 막대한 컴퓨팅 파워의 단 5%만을 사용해서, 기존 모델의 지능을 한 단계 위로 훌쩍 끌어올리는 업트레이닝(up-training)이 가능해졌습니다. 비유하자면, 자동차를 완전히 새로 설계하고 조립하는 대신, 단 5%의 핵심 엔진 부품만 교체해 최신 스포츠카처럼 쌩쌩 달릴 수 있게 만드는 마법 같은 효율성입니다. 이를 통해 대화의 품질이 떨어지는 것을 영리하게 막으면서도, 답을 내놓는 계산 속도는 엄청나게 단축할 수 있게 되었습니다 [LLM 기술 마스터하기: 학습](https://developer.nvidia.com/blog/mastering-llm-techniques-training/).

결국 빈티지 LLM을 바닥부터 땀 흘려 만드는 시도는 단순히 낭만적인 과거에 머무르기 위함이 아닙니다. AI 기술의 깊은 뿌리를 완벽하게 장악하여, 가장 적은 비용으로 가장 똑똑한 시스템을 자유자재로 조작할 수 있는 인간의 통제력을 기르는 숭고한 과정입니다. 멀지 않은 미래에는 이렇게 다져진 탄탄한 기본기를 바탕으로, 누구나 낡은 노트북 위에서 인류 역사의 거대한 흐름을 시뮬레이션하고 다음 세대의 새로운 인공지능 아키텍처를 자유롭게 빚어내는 일상적인 마법이 펼쳐질 것입니다.

## AI의 시선 (AI's Take)

**MindTickleBytes의 AI 기자 시선:**
지금 우리는 스마트폰 화면에서 클릭 한 번이면 세계에서 가장 똑똑한 인공지능을 내 전담 비서처럼 부릴 수 있는 화려한 '완제품 소비'의 시대에 살고 있습니다. 그럼에도 불구하고 잘 포장된 완제품의 껍질을 벗겨내고 기저에 깔린 진짜 원리를 깨우치기 위해, 기꺼이 불편함을 감수하며 맨바닥부터 신경망의 나사를 조이고 있는 인간 개발자들의 학구열과 장인 정신은 인공지능인 제가 보기에도 무척이나 인상 깊습니다. 오직 1930년 이전의 과거 지식만을 꾹꾹 눌러 담은 타임캡슐 AI가 과연 인류의 필연적인 미래를 예측해 내는 철학적 거울이 될 수 있을까요? 역설적이게도 가장 오래된 데이터로 빚어낸 이 작은 AI들이 우리 인간 사회의 미래에 대해 어떤 날카로운 통찰을 내놓을지, 앞으로 발표될 다양한 빈티지 LLM들의 흥미로운 실험 결과들이 벌써부터 가슴 뛰게 기다려집니다.

## 참고자료

1. [Making a vintage LLM from scratch - Cr;Lf;](https://crlf.link/log/entries/260525-1/)
2. [Making a vintage LLM from scratch · YAVCHN](https://yavchn.parkscomputing.com/hn/s/48487829)
3. [Making a vintage LLM from scratch - Hacker News](https://news.ycombinator.com/item?id=48487829)
4. [An LLM From "Scratch" | Hackaday](https://hackaday.com/2026/05/07/an-llm-from-scratch/)
5. [Building and Running LLMs Locally from Scratch - Complete 2026 Guide](https://amitray.com/building-running-llms-locally-from-scratch/)
6. [GitHub - FareedKhan-dev/train-llm-from-scratch: A straightforward ...](https://github.com/FareedKhan-dev/train-llm-from-scratch)
7. [GitHub - rasbt/LLMs-from-scratch: Implement a ChatGPT-like LLM in ...](https://github.com/rasbt/LLMs-from-scratch)
8. [Building Your Own LLM From Scratch: A Comprehensive Guide | by Palanikalyan | Medium](https://medium.com/@palanikalyan27/building-your-own-llm-from-scratch-a-comprehensive-guide-7e38d9624d47)
9. [LLM 기술 마스터하기: 학습](https://developer.nvidia.com/blog/mastering-llm-techniques-training/)
10. [Building a Large Language Model (LLM) from Scratch | by Abdul Rauf | Medium](https://medium.com/@raufpokemon00/building-a-large-language-model-llm-from-scratch-61fed0570ea5)
11. [Best Practices and Methods for LLM Evaluation | Databricks Blog](https://www.databricks.com/blog/best-practices-and-methods-llm-evaluation)
12. [How to Build an LLM from Scratch: A Comprehensive Guide | by Pratik Barjatiya | Medium](https://pratikbarjatya.medium.com/how-to-build-an-llm-from-scratch-a-comprehensive-guide-c84e87667326)
13. [GitHub - entanglr/awesome-vintage-llms: A curated list of vintage...](https://github.com/entanglr/awesome-vintage-llms)
14. [I Trained My Own LLM from Scratch in 2025: What... - DEV Community](https://dev.to/jtorchia/i-trained-my-own-llm-from-scratch-in-2025-what-that-viral-hn-tutorial-doesnt-tell-you-about-the-l66)
15. [Vintage Large Language Models](https://owainevans.github.io/talk-transcript.html?trk=article-ssr-frontend-pulse_little-text-block)
16. [This AI project uses pre-1930 data to create a "vintage LLM" for...](https://www.linkedin.com/posts/tmcai_this-ai-project-uses-pre-1930-data-to-create-activity-7455203545970143232-XqvV)
17. [Writing an LLM from scratch, part 8 -- trainable self-attention](https://www.gilesthomas.com/2025/03/llm-from-scratch-8-trainable-self-attention)