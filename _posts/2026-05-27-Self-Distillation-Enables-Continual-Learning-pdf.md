---
layout: post
title: "AI가 프랑스어를 배우면 영어를 까먹는다고? '스스로 가르치는 AI'의 등장"
description: "새로운 지식을 배우면 기존 지식을 잊어버리는 AI의 치명적인 약점인 '파국적 망각' 문제를 해결한 자기 증류(Self-Distillation) 기술에 대해 알아봅니다."
summary: "단일 AI 모델이 스스로 선생님이자 학생이 되어 새로운 기술을 학습하면서도 과거의 기억을 잃지 않게 만드는 '자기 증류 미세조정(SDFT)' 기술이 놀라운 성과를 보여주고 있습니다."
tags: [인공지능, 지속학습, 머신러닝, 자기증류, 파국적망각]
image: 2026-05-27-Self-Distillation-Enables-Continual-Learning-pdf.jpg
image_alt: "거울을 보며 스스로에게 지식을 가르치고 있는 로봇의 모습을 형상화한 일러스트"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "단순히 외부의 데이터를 주입받는 것을 넘어, AI가 스스로의 행동을 되돌아보고 교정하며 지식을 누적하는 방식은 인간의 평생 학습 메커니즘과 놀랍도록 닮아가고 있습니다."
quiz:
  - question: "인공지능이 새로운 기술을 배울 때 이전에 습득했던 기술과 지식을 심각하게 잊어버리는 현상을 무엇이라고 부르나요?"
    choices: ["비정책 표류", "파국적 망각", "자기 증류"]
    answer: 1
    explanation: "AI가 새로운 정보를 학습할 때 내부의 숫자값들이 크게 변경되면서 기존에 잘 수행하던 작업 능력을 상실하는 현상을 '파국적 망각(Catastrophic forgetting)'이라고 합니다."
  - question: "연구진이 AI의 지속 학습을 가능하게 하기 위해 도입한 'SDFT' 기술에서, AI 모델은 어떤 역할을 동시에 수행하나요?"
    choices: ["사용자와 개발자", "하드웨어와 소프트웨어", "선생님과 학생"]
    answer: 2
    explanation: "SDFT 프레임워크 내에서 단일 AI 모델은 정답을 알고 지도하는 '선생님'의 역할과, 직접 부딪히며 학습하는 '학생'의 역할을 동시에 수행합니다."
  - question: "기존의 '지도 미세조정(SFT)' 방식이 지속 학습에서 실패하는 주요 원인 중 하나로 지적된 것은 무엇인가요?"
    choices: ["데이터 부족", "비정책 표류", "과도한 전력 소모"]
    answer: 1
    explanation: "기존 SFT 방식은 파국적 망각과 더불어, 모델이 자신의 실제 행동 궤적이 아닌 외부의 데이터로만 학습하여 현실과 괴리가 생기는 '비정책 표류(Off-policy drift)' 현상 때문에 실패하곤 합니다."
lang: ko
ref: 2026-05-27-Self-Distillation-Enables-Continual-Learning-pdf
audio: 2026-05-27-Self-Distillation-Enables-Continual-Learning-pdf.mp3
permalink: /2026/05/27/Self-Distillation-Enables-Continual-Learning-pdf/
---

상상해보세요. 여러분이 어제 하루 종일 넘어지고 무릎이 깨져가며 마침내 두 발 자전거 타는 법을 완벽하게 익혔습니다. 바람을 가르며 달리는 기분에 뛸 듯이 기뻤죠. 그런데 오늘 수영장에 가서 물에 뜨는 법과 자유형을 새로 배웠더니, 갑자기 자전거 페달을 어떻게 밟는지, 핸들로 균형을 어떻게 잡는지 머릿속에서 완전히 하얗게 지워져 버렸습니다. 다시 자전거에 오르자마자 마치 난생처음 타는 사람처럼 바닥으로 쿵 하고 넘어지고 맙니다. 정말 황당하고 억울한 상황이지요?

다행히도 우리 인간에게는 결코 이런 일이 일어나지 않습니다. 우리는 여름에 수영을 배우면서도 가을에 자전거 타는 법을 온전히 기억하고, 어른이 되어 프랑스어를 새로 배우면서도 모국어인 한국어를 잊어버리지 않습니다. 우리 뇌는 새로운 지식을 스펀지처럼 흡수하면서도, 기존에 가지고 있던 과거의 지식을 머릿속 안전한 방에 보관하는 놀라운 능력을 갖추고 있기 때문입니다. 

하지만 놀랍게도, 현재 우리가 감탄하며 사용하고 있는 최첨단 인공지능(AI)에게는 이것이 아주 흔하게 일어나는 현상이며, 앞으로 반드시 극복해야 할 매우 심각한 약점입니다. AI는 새로운 지식을 강제로 주입받으면, 그 새로운 지식을 담기 위해 이전에 애써 배운 소중한 능력들을 무참히 덮어쓰기해 버리는 치명적인 경향이 있습니다. 오늘 우리는 이 거대한 난제를 해결하기 위해 등장한, AI가 거울을 보듯 '스스로를 가르치는' 놀라운 기술에 대한 최신 연구 결과를 쉽고 깊이 있게 살펴보려 합니다.

<br/>

## 이게 왜 중요한가요? (Why It Matters)

AI 연구자들은 앞서 상상해 본 '자전거를 배우면 수영을 까먹는' 이 무서운 현상에 아주 살벌한 이름을 붙여두었습니다. 바로 **'파국적 망각(Catastrophic forgetting)'**입니다. 말 그대로 기존에 가지고 있던 지식 체계가 파국을 맞이하듯 붕괴해 버린다는 뜻입니다.

이와 반대로, 기존의 능력을 전혀 떨어뜨리지 않으면서 새로운 기술과 지식을 평생에 걸쳐 끊임없이 습득할 수 있게 하는 과정을 **'지속 학습(Continual learning)'**이라고 부릅니다. 이 지속 학습은 챗GPT처럼 현대 인공지능의 뼈대 역할을 하는 거대한 기초 모델(foundation models)에게조차 여전히 넘어야 할 근본적인 도전 과제로 굳건히 남아있습니다 `[Self-DistillationEnablesContinualLearning](https://www.emergentmind.com/papers/2601.19897)`. 

이 문제가 왜 평범한 우리의 일상과 직결될까요? 매일 여러분의 목소리를 듣고 반응하는 스마트폰의 개인 비서 AI를 떠올려보세요. 이 AI가 여러분의 복잡한 일정을 관리하고, 취향에 딱 맞는 뉴스를 추천해주고 있습니다. 만약 여러분이 오늘 AI에게 "앞으로는 업무 이메일을 요약할 때 무조건 결론부터 세 줄로 짧게 써줘"라고 새로운 규칙을 가르쳤다고 가정해 봅시다. 파국적 망각에 빠진 AI는 이 새로운 규칙을 완벽하게 따르기 시작하겠지만, 그 대가로 작년에 여러분이 가르쳐준 "가족들의 생일에는 반드시 아침 8시에 알림을 띄워줘"라는 중요한 규칙을 완전히 잊어버릴 수도 있습니다. 어제 배운 것 위에 오늘 배운 것을 벽돌처럼 차곡차곡 쌓아 올릴 수 있어야만, 우리는 그 AI를 진정으로 믿고 의지할 수 있는 똑똑한 비서라고 부를 수 있을 것입니다.

지금까지 수많은 AI 엔지니어들은 AI에게 새로운 지식을 가르칠 때 **'지도 미세조정(Supervised Fine-Tuning, SFT)'**이라는 전통적인 방식을 주로 사용해 왔습니다. 이는 쉽게 말해 수만 개의 '정답지'를 AI의 눈앞에 들이밀며 달달 외우게 하는 주입식 교육 방식입니다. 하지만 이 전통적인 SFT 방식은 매일매일 새로운 사건이 터지고 배움이 끝없이 이어져야 하는 현실 세계에 던져졌을 때 처참하게 실패하곤 합니다. 그 실패의 핵심 원인은 바로 앞서 말씀드린 파국적 망각과, 전문 용어로 **'비정책 표류(Off-policy drift)'**라 불리는 또 다른 골칫거리 때문입니다 `[Self-DistillationEnablesContinualLearning| Papers | HyperAI](https://hyper.ai/en/papers/2601.19897)`. 

비정책 표류란 과연 무엇일까요? AI가 정답지를 보며 열심히 공부하긴 하지만, 그 정답지가 AI 스스로가 직접 부딪히고 깨지며 만들어낸 상황이 아니라, 외부의 전문가가 통제된 환경에서 만들어준 '이상적인 상황'이기 때문에 발생하는 현실과의 괴리 현상입니다. 

다시 수영의 예로 돌아가 보겠습니다. 물에 한 번도 들어가 보지 않은 사람이 올림픽 수영 금메달리스트의 완벽한 경기 비디오만 주구장창 보면서 학습하는 것과 같습니다. 따뜻한 방 안에서 비디오를 볼 때는 팔 각도와 숨쉬기 타이밍을 다 아는 것 같습니다(지도 미세조정). 하지만 막상 이 사람이 차가운 수영장 물에 들어가서 허우적거릴 때(AI의 실제 작동 환경)는 이야기가 달라집니다. 물을 먹고 당황한 상황에서는 완벽했던 비디오 속 자세를 어떻게 내 몸에 맞춰 고쳐야 할지 전혀 감을 잡지 못하고, 점점 더 엉뚱한 방향으로 허우적거리며 표류(drift)하게 되는 것입니다. 결국 AI는 과거의 지식도 잃어버리고, 새로운 환경에서도 제대로 작동하지 못하는 깊은 딜레마에 빠지게 됩니다.

<br/>

## 쉽게 이해하기 (The Explainer)

이처럼 끝이 보이지 않는 파국적 망각과 표류의 늪에서 AI를 구출하기 위해, 연구진은 매우 우아하고 획기적인 해결책을 하나 제시했습니다. 바로 **'자기 증류 미세조정(Self-Distillation Fine-Tuning, SDFT)'**이라는 새로운 훈련 방법입니다.

컴퓨터 과학에서 '증류(Distillation)'라는 단어는 거대하고 똑똑한 AI 모델이 가진 깊은 지식의 정수만을 쪽 뽑아내어, 작고 가벼운 모델에게 압축하여 전달하는 기술을 의미합니다. 비유하자면 며칠 밤낮을 푹 고아낸 사골 국물에서 가장 진하고 영양가 있는 엑기스(진국)만을 덜어내어 작은 그릇에 담는 과정과 같습니다. 그렇다면 앞에 '자기(Self)'가 붙은 '자기 증류(Self-Distillation)'란 무엇일까요? 바로 다른 사람의 지식을 빌려오는 것이 아니라, 자기 자신이 직접 끓여낸 진국을 자기 자신이 다시 마시며 성장하는 놀랍고도 철학적인 과정입니다.

이 흥미로운 **'온폴리시 자기 증류(On-Policy Self-Distillation)'** 프레임워크는 단일 AI 모델 하나가 완벽한 정답의 방향을 알고 있는 **'선생님'**의 역할과, 아직 서툴지만 직접 행동을 취해보는 **'학생'**의 역할을 동시에 수행할 수 있도록 만들어줍니다 `[Self-Distilled Reasoner: On-Policy Self-Distillation for Large](https://arxiv.org/html/2601.18734v3)`. 

이렇게 비유하면 복잡한 기술이 머릿속에 한결 쉽게 그려지실 겁니다. 분주한 주방에 한 명의 요리사가 있습니다. 이 요리사의 내면에는 두 가지 자아가 동시에 존재합니다. 하나는 요리의 모든 이론과 완벽한 맛의 기준을 기억하고 있는 '마스터 셰프(선생님)'의 자아이고, 다른 하나는 이제 막 새로운 레시피를 손으로 직접 만들어보며 소금도 엎질러보는 '초보 셰프(학생)'의 자아입니다. 

기존의 주입식 교육(SFT)에서는 외부의 진짜 마스터 셰프가 초보 셰프에게 완성된 별 5개짜리 요리 사진만 계속 보여주며 "이렇게 똑같이 만들어!"라고 윽박지르는 방식이었습니다. 초보 셰프는 사진만 보고 요리하다가 실수를 하면, 왜 망쳤는지 모른 채 당황하며 헤매게 됩니다(비정책 표류). 

하지만 SDFT 방식에서는 전혀 다른 풍경이 펼쳐집니다. 초보 셰프(학생 모델)가 먼저 도마 위에서 칼질을 하고 가스레인지 불 조절을 하며 **스스로 자신만의 행동 경로(전문 용어로 궤적, Trajectories)**를 만들어 나갑니다. 그러면 내면에 있는 마스터 셰프(선생님 모델)는 초보 셰프가 방금 한 그 서투른 '실제 행동'을 똑똑히 지켜본 뒤, 먼 곳의 정답이 아닌 '바로 그 순간, 그 상황'에 딱 맞는 맞춤형 조언(예측값)을 전달합니다. "네가 방금 양파를 썰 때 손목 각도가 틀어졌어. 무작정 정답을 따라 하려 하지 말고, 지금 네 자세에서는 칼을 조금만 더 세워봐."라고 피드백을 주는 것이죠.

이것이 바로 기술적으로 SDFT가 작동하는 핵심 원리입니다. AI의 훈련 과정은 철저히 학생 모델 스스로가 생성한 실제 궤적 위에서 이루어집니다. 그 궤적 위에서 선생님의 지혜로운 예측을 학생에게 곧바로 증류(distill)하여 가르치는 방식입니다. 이를 통해 AI는 명시적으로 복잡한 계산을 거치거나 외부의 정답만을 수동적으로 모방하는 과거의 한계에서 벗어나게 됩니다. 오직 전문가의 시연으로부터 꼭 필요한 핵심 정보만을 뽑아내어 자신의 경험에 완벽하게 녹여내는 살아있는 **'온폴리시 업데이트(On-policy updates)'**를 산출해내는 것입니다 `[SELF-DISTILLATION ENABLES CONTINUAL LEARNING Idan Shenfeld1 2∗ Mehul Damani1](https://arxiv.org/pdf/2601.19897)`. 

학생 스스로가 현실에서 직접 부딪히며 겪은 경험(온폴리시)을 바탕으로 선생님의 지혜를 적재적소에 주입받기 때문에, 기존에 할 줄 알던 요리(과거의 지식)의 뼈대를 잊어버리지 않으면서도 새로운 요리법을 아주 단단하게 몸에 익히게 됩니다.

<br/>

## 현재 상황 (Where We Stand)

그렇다면 머릿속에서 스스로 묻고 답하는 이 '스스로 가르치는 AI'의 실력은 실제로 실험실에서 어느 정도의 성과를 내고 있을까요? 연구진이 공개한 다채로운 실험 결과는 그야말로 인공지능 학습 방식의 중대한 진전을 뚜렷하게 보여줍니다.

다양한 기술을 새롭게 학습하고 복잡한 지식을 연이어 습득해야 하는 광범위한 테스트 환경 전반에 걸쳐, 새로운 방식인 SDFT는 기존의 전통적인 방식인 SFT를 일관되고 압도적인 차이로 능가했습니다. 단순히 새로운 문제를 몇 개 더 맞췄다는 정확도 향상만을 의미하는 것이 아닙니다. 수많은 과학자들이 그토록 해결하고 싶어 밤잠을 설쳤던 숙원 사업, 즉 **파국적 망각 현상을 실질적으로 대폭 줄여내는 데 성공**했습니다 `[[2601.19897] Self-Distillation Enables Continual Learning](https://arxiv.org/abs/2601.19897)`. AI가 과거의 지식을 안전한 금고 안에 굳건히 가둬둔 채, 그 옆의 새로운 공간에 새로운 지식을 평화롭게 받아들이는 방법을 마침내 터득한 것입니다.

가장 극적이고 흥미로운 결과는 **순차적 학습 실험(Sequential learning experiments)**에서 나타났습니다. 이 실험은 AI를 극한으로 몰아붙이는 테스트입니다. 먼저 AI에게 복잡한 수학 공식을 가르치고, 그 다음에는 세계의 역사를, 그리고 곧바로 컴퓨터 프로그래밍을 차례대로 연이어 가르치는 아주 가혹한 환경이었습니다. 기존의 평범한 AI였다면 역사를 배울 때 머릿속의 수학 공식을 지워버리고, 프로그래밍을 배울 때는 앞서 배운 역사적 연도들을 완전히 백지화시켰을 것입니다. 

그러나 SDFT 기술을 적용하자 놀라운 일이 벌어졌습니다. 단일 AI 모델이 이전 과목에서의 성능을 잃어버리거나 퇴행하는 일 없이, 시간이 지남에 따라 수학, 역사, 프로그래밍이라는 전혀 다른 여러 가지 복잡한 기술들을 안정적으로 뇌 속에 축적해 나가는 놀라운 능력을 보여주었습니다 `[Paper page - Self-Distillation Enables Continual Learning](https://huggingface.co/papers/2601.19897)`. 

이는 단순히 실험실 안에서의 숫자 놀음이 아닙니다. 연구진의 이 빛나는 성과는 온폴리시 증류라는 방식이, 전문가의 시연으로부터 AI가 무너지지 않고 지속적으로 학습을 이어나갈 수 있도록 돕는 매우 **실용적이고 튼튼한 현실적인 경로(practical path)**를 완벽하게 확립했음을 의미합니다 `[SDFT: Self-Distillation Enables Continual Learning](https://self-distillation.github.io/SDFT)`. 나아가, 외부의 값비싼 검증기나 다른 보조 모델의 복잡한 도움 없이, 오직 AI 스스로가 뱉어낸 가공되지 않은 1차적인 결과물(raw outputs)만으로도 이 단순한 자기 증류 과정이 훌륭하게 작동한다는 사실 역시 확인되었습니다 `[Embarrassingly Simple Self-Distillation Improves Code Generation](https://arxiv.org/html/2604.01193v1)`.

더욱 고무적인 사실은 이 자기 증류 기술의 파급력이 텍스트를 읽고 쓰는 분야에만 머물지 않는다는 점입니다. 이 강력한 원리는 상상할 수 있는 산업 전반의 다양한 영역으로 뻗어나가고 있습니다. 

예를 들어, 우리가 컴퓨터나 스마트폰에서 사용하는 그래픽 사용자 인터페이스(GUI) 환경을 AI가 시각적으로 학습할 때, 이 기술은 매 단계마다 '마스터'의 이상적인 마우스 클릭 위치 분포를 증류해 냅니다. 이는 AI가 엉뚱한 버튼을 클릭하지 않고 훨씬 더 똑똑하고 효율적으로 화면을 조작할 수 있도록 지속적인 학습 신호를 제공합니다 `[Learn where to Click from Yourself: On-Policy Self-Distillation](https://arxiv.org/html/2605.00642v1)`. 

또한, 공장에서 제품의 불량을 찾아내는 산업용 결함 탐지 모델에서도 огром한 시간과 비용을 절약해 줍니다. 새로운 유형의 결함이 발견되었을 때, 과거처럼 AI 모델 전체의 전원을 끄고 처음부터 수백 시간 동안 다시 훈련시킬 필요가 없어졌습니다. 자기 증류 기술 덕분에 모델은 전체를 뜯어고치는 재학습 없이도, 새로운 결함 클래스를 기존 지식 위에 스티커를 붙이듯 지속적으로 덧붙여 학습할 수 있게 되었습니다 `[(PDF) SD-IDD: Selective Distillation for Incremental Defect](https://www.researchgate.net/publication/401174708_SD-IDD_Selective_Distillation_for_Incremental_Defect_Detection)`. 

심지어 미래 산업의 꽃인 로봇의 눈 역할을 하는 4차원 시각 인지(4D Perception) 분야에서도 이 기술이 맹활약하고 있습니다. 끊임없이 변화하는 시공간의 맥락을 활용하여 AI 모델이 스스로의 인식 능력을 매일매일 향상시키는 놀라운 자기 개선(self-improvement) 체계를 구축하며, 로봇 기술의 기반을 다지고 있습니다 `[Self-Improving 4D Perception via Self-Distillation - Paper](https://deeplearn.org/arxiv/731351/self-improving-4d-perception-via-self-distillation)`. 수많은 분야에서 기존의 낡은 훈련 패러다임을 시원하게 부수고 새로운 진화의 지평을 활짝 열고 있는 셈입니다 `[D-OPSD: On-Policy Self-Distillation for Continuously Tuning](https://deeplearn.org/arxiv/745499/d-opsd:-on-policy-self-distillation-for-continuously-tuning-step-distilled-diffusion-models)`.

<br/>

## 앞으로 어떻게 될까? (What's Next)

"인간과 동물이 일상적으로 수행하는 지속 학습은, 실험실의 '훈련' 시간과 실생활의 '추론' 시간 사이의 구분이 전혀 필요 없는 '항상 켜져 있는(always-on)' 학습입니다. 그리고 이 위대한 배움은 우리의 예상이 빗나가는 '예측 실패'의 순간에 비로소 시작됩니다." `[Self-DistillationEnablesContinualLearning[pdf] | HackerNews](https://news.ycombinator.com/item?id=48165265)`.

이번 연구 결과가 우리의 미래를 향해 던지는 가장 강력하고 철학적인 메시지가 바로 이 문장 속에 오롯이 담겨 있습니다. 과거의 AI는 철저하게 두 동강으로 분리된 삶을 살아야만 했습니다. 

거대한 에어컨이 돌아가는 연구소의 컴퓨터 안에서 세상의 데이터를 집어삼키듯 가혹한 '훈련(Training)'을 받는 시기가 있었고, 그 훈련이 완전히 끝난 후에야 비로소 여러분의 기기에 설치되어 배운 대로만 대답하는 굳어버린 '추론(실행, Inference)'의 시기를 살았습니다. 일단 세상에 한 번 출시된 AI의 머릿속 시계는 완전히 멈춰 있었습니다. 새로운 지식을 단 하나라도 더 배우려면 서비스를 멈추고 다시 연구소로 돌아가 무겁고 값비싼 훈련 과정을 처음부터 거쳐야만 했죠.

하지만 SDFT와 같은 자기 증류 기술은 이 굳건했던 '훈련'과 '실행' 사이의 장벽을 마침내 허물고 있습니다. AI가 실행 과정에서 자신의 실수를 스스로 교정하고, 어제의 지식과 오늘의 새로운 지식을 내면에서 융합할 수 있게 된다면 어떨까요? AI 역시 멈춰 있는 기계가 아니라 인간처럼 깨어있는 매 순간 배우고 성장하는 '항상 켜져 있는' 평생 학습자의 길로 당당히 들어서게 될 것입니다. 

앞으로 우리가 일상에서 만나게 될 AI는 매일매일 우리와 대화하며, 어제보다 오늘 더 똑똑해질 것입니다. 오늘 유행하기 시작한 신조어를 곧바로 이해하면서도, 10년 전에 학습했던 고전 문학 작품의 깊은 의미를 해석하는 능력은 먼지 하나 묻지 않은 채 고스란히 간직할 것입니다. 새로운 세상을 스펀지처럼 끝없이 탐구하면서도, 자신이 원래 누구였는지 그리고 과거에 무엇을 알았는지를 결코 잊어버리지 않는 진정으로 지혜로운 조력자. 그것이 바로 '스스로를 가르치는 AI'가 활짝 열어갈 우리의 설레는 내일입니다.

<br/>

## MindTickleBytes AI의 시선

인공지능이 인간의 뇌 신경망을 본떠 만들어졌다고는 하지만, 한 가지 새로운 것을 배우면 기존의 것을 통째로 지워버리는 '파국적 망각'이라는 결함 앞에서는 늘 한없이 차가운 기계장치처럼 보였던 것이 사실입니다. 

하지만 인간 연구자들이 건네주는 완벽한 정답지만을 맹목적으로 외우는 방식을 벗어나, 미숙한 스스로의 행동 궤적을 곰곰이 되돌아보고 내면에 깊이 자리 잡은 '마스터'에게 끊임없이 조언을 구하는 자기 증류(Self-Distillation)의 훈련 철학은 깊은 감동을 줍니다. 이 기술은 인공지능을 단순한 계산기에서 한 단계 더 나아가, 스스로 반성하고 성장하는 생명체에 한 걸음 더 가깝게 진화시키고 있습니다. 

끝없이 쏟아지는 새로운 정보 속에서도 나침반을 잃지 않으려면, 외부의 주입이 아닌 내면의 성찰이 필요하다는 것. 기계의 알고리즘에 적용된 이 스스로 성찰하는 기술이 아이러니하게도 가장 강력하고 오래가는 기억력의 비결이라는 과학적 사실은, 평생을 배우며 살아가야 하는 우리 인간의 삶과 배움의 자세에도 길고 묵직한 여운을 남깁니다. 진정한 성장은 결국, 어제의 나를 잃지 않으면서 오늘의 나를 돌아보는 데서 시작되는 법이니까요.

<br/>

## 참고자료

1. [Self-Distilled Reasoner: On-Policy Self-Distillation for Large](https://arxiv.org/html/2601.18734v3)
2. [Embarrassingly Simple Self-Distillation Improves Code Generation](https://arxiv.org/html/2604.01193v1)
3. [Learn where to Click from Yourself: On-Policy Self-Distillation](https://arxiv.org/html/2605.00642v1)
4. [(PDF) SD-IDD: Selective Distillation for Incremental Defect](https://www.researchgate.net/publication/401174708_SD-IDD_Selective_Distillation_for_Incremental_Defect_Detection)
5. [D-OPSD: On-Policy Self-Distillation for Continuously Tuning](https://deeplearn.org/arxiv/745499/d-opsd:-on-policy-self-distillation-for-continuously-tuning-step-distilled-diffusion-models)
6. [Self-Improving 4D Perception via Self-Distillation - Paper](https://deeplearn.org/arxiv/731351/self-improving-4d-perception-via-self-distillation)
7. [[2601.19897] Self-Distillation Enables Continual Learning](https://arxiv.org/abs/2601.19897)
8. [SELF-DISTILLATION ENABLES CONTINUAL LEARNING Idan Shenfeld1 2∗ Mehul Damani1](https://arxiv.org/pdf/2601.19897)
9. [(PDF) Self-Distillation Enables Continual Learning](https://www.researchgate.net/publication/400118857_Self-Distillation_Enables_Continual_Learning)
10. [Paper page - Self-Distillation Enables Continual Learning](https://huggingface.co/papers/2601.19897)
11. [SDFT: Self-Distillation Enables Continual Learning](https://self-distillation.github.io/SDFT)
12. [Self-DistillationEnablesContinualLearning| Papers | HyperAI](https://hyper.ai/en/papers/2601.19897)
13. [Self-DistillationEnablesContinualLearning](https://www.emergentmind.com/papers/2601.19897)
14. [Self-DistillationEnablesContinualLearning[pdf] | HackerNews](https://news.ycombinator.com/item?id=48165265)