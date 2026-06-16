---
layout: post
title: "브라질 리우데자네이루의 '자체 개발' AI, 알고 보니 짜깁기? 3,970억 파라미터의 진실"
description: "리우데자네이루가 발표한 자체 개발 거대 인공지능 모델이 사실은 기존 오픈소스 모델들을 섞어 만든 '모델 병합(Merge)' 결과물로 밝혀졌습니다. 이 사건이 의미하는 바를 알기 쉽게 설명합니다."
summary: "브라질 리우데자네이루 시정부가 야심 차게 공개한 거대 인공지능 모델이 독자 개발품이 아닌 기존 모델들의 짜깁기로 밝혀지면서, 진정한 '로컬 AI' 개발의 현실적인 어려움이 수면 위로 떠올랐습니다."
tags: [인공지능, 로컬AI, 거대언어모델, 모델병합, 오픈소스, 기술검증]
image: 2026-06-16-Rio-de-Janeiros-homegrown-LLM-appears-to-be-a-merge-of-an-existing-model.jpg
image_alt: "두 개의 서로 다른 색상의 톱니바퀴가 거대한 하나의 기계장치로 억지로 끼워 맞춰져 있는 모습을 그린 일러스트레이션으로, 여러 인공지능을 섞어서 하나로 둔갑시킨 짜깁기 논란을 은유적으로 표현함."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "인공지능 모델의 거대한 규모가 도시나 국가의 기술적 자존심을 대변하는 시대가 되었습니다. 하지만 전 세계 개발자들이 지켜보는 투명한 오픈소스 생태계 앞에서는, 어설픈 재포장이 오히려 신뢰를 깎아내린다는 사실을 잊지 말아야 합니다."
quiz:
  - question: "리우데자네이루 시정부가 야심 차게 발표한 'Rio-3.5-Open-397B' 모델에 대해 최근 밝혀진 사실은 무엇인가요?"
    choices: ["세계 최초로 인간의 감정을 완벽히 이해하는 모델로 판명되었다.", "기존에 공개된 다른 인공지능 모델들을 단순히 섞은 짜깁기 모델이었다.", "모든 개발 과정을 투명하게 공개해 칭찬을 받았다."]
    answer: 1
    explanation: "해당 모델은 독립적으로 훈련된 것이 아니라, 기존의 'Nex-AGI'와 'Qwen3' 모델을 병합(Merge)한 것으로 밝혀졌습니다."
  - question: "논란이 커지자 개발을 주도한 이플랜리우(IplanRIO) 측은 어떤 해명을 내놓았나요?"
    choices: ["해킹을 당해 원본 파일이 조작되었다.", "데이터 부족으로 어쩔 수 없는 선택이었다.", "최종 버전(증류 모델) 대신 중간 단계의 병합 버전을 실수로 업로드했다."]
    answer: 2
    explanation: "이플랜리우 측은 최종적으로 다듬은 '증류 모델'을 올리려 했으나, 실수로 '기본 병합 버전'을 업로드했다며 사과했습니다."
  - question: "기술 전문가들이 이번 사태를 보며 지적한 '로컬 AI(Local AI)' 개발의 가장 큰 현실적 장벽은 무엇인가요?"
    choices: ["세상에 없던 새로운 인공지능을 처음부터 만들어내는 것은 너무나 어렵다.", "AI 개발에 필요한 전기가 부족하다.", "관련 법적 규제가 너무 강력하다."]
    answer: 0
    explanation: "전문가들은 완전히 새로운 것을 구축하는 독자 개발은 매우 어려운 반면, 기존 모델을 재포장하는 것은 쉽기 때문에 이런 일이 벌어진다고 분석했습니다."
lang: ko
ref: 2026-06-16-Rio-de-Janeiros-homegrown-LLM-appears-to-be-a-merge-of-an-existing-model
audio: 2026-06-16-Rio-de-Janeiros-homegrown-LLM-appears-to-be-a-merge-of-an-existing-model.mp3
permalink: /2026/06/16/Rio-de-Janeiros-homegrown-LLM-appears-to-be-a-merge-of-an-existing-model/
---

## 서론: 화려한 데뷔 무대 뒤에 숨겨진 진실

상상해보세요. 세계적으로 유명한 마술사가 수년간 뼈를 깎는 수련 끝에 세상에 단 하나뿐인 공중부양 마술을 발명했다고 선언합니다. 화려한 조명 아래서 수많은 관중이 기립 박수를 치며 열광하고 있는데, 무대 뒤편을 우연히 들여다본 한 소년이 소리칩니다. "어? 저거 그냥 밧줄 두 개를 교묘하게 묶어서 천장에 매달아 놓은 것뿐이잖아!" 

이 흥미로운 이야기가 최근 전 세계 최첨단 기술의 각축장인 인공지능(AI) 업계에서 현실로 벌어졌습니다. 브라질의 상징적인 도시, 리우데자네이루(Rio de Janeiro) 시정부가 자체적으로 처음부터 끝까지 개발했다며 자랑스럽게 공개한 거대 인공지능 모델이 사실은 남들이 만들어 놓은 기술을 교묘하게 섞어 만든 '짜깁기' 결과물이라는 의혹이 사실로 드러난 것입니다. 

오늘날 수많은 국가와 도시들은 외국의 거대 기술 기업에 종속되지 않기 위해 자신만의 AI를 가지려 고군분투하고 있습니다. 그렇다면 리우데자네이루에서는 대체 무슨 일이 있었던 것일까요? 왜 사람들은 이 기술이 가짜라고 확신하게 되었으며, 이 사건이 우리의 미래에 던지는 메시지는 무엇일까요? 똑똑한 친구가 따뜻한 커피 한 잔을 마시며 들려주는 이야기처럼, 쉽고 재미있게 이 사태의 전말을 파헤쳐 보겠습니다.

## 왜 중요한가: '국산 AI'의 꿈과 3,970억 개의 별

우리가 매일 사용하는 스마트폰의 음성 비서나 챗GPT 같은 서비스는 엄청난 규모의 '거대 언어 모델(LLM, 대량의 텍스트를 학습해 인간의 언어를 이해하고 문장을 생성하는 AI 시스템)'을 기반으로 작동합니다. 최근 세계 각국은 자국의 데이터 주권과 고유한 문화적 특성을 지키기 위해 '로컬 AI(Local AI)' 또는 '소버린 AI(Sovereign AI)'라는 이름의 독자적인 인공지능 개발에 사활을 걸고 있습니다.

지난주, 리우데자네이루의 IT 전담 기관인 '이플랜리우(IplanRIO)'는 역사적인 쾌거를 발표했습니다. 전 세계 AI 개발자들이 코드를 공유하는 도서관 같은 플랫폼인 '허깅페이스(Hugging Face)'에 무려 **'Rio-3.5-Open-397B'**라는 이름의 거대 모델을 당당히 공개한 것입니다 [출처: Rio de Janeiro's 'Homegrown' AI Was Someone Else's Model Wit...](https://dev.to/jamilxt/rio-de-janeiros-homegrown-ai-was-someone-elses-model-with-a-new-name-jcb).

이 이름 뒤에 붙은 '397B'라는 숫자에 주목해야 합니다. 이는 해당 인공지능이 **3,970억 개의 파라미터(Parameter)**를 가졌다는 것을 의미합니다. 쉽게 말해서, 파라미터는 사진 앱에서 색감이나 밝기를 미세하게 조절하는 '다이얼'과 같습니다. 인공지능 모델 내부에는 수많은 지식을 기억하고 판단을 내리기 위해 이 다이얼들이 쉴 새 없이 돌아갑니다. 3,970억 개라는 숫자는 맑은 날 밤하늘을 넘어, 우리 은하계 전체에 떠 있는 별의 숫자와 맞먹을 만큼 경이로운 규모입니다. 이 정도 체급은 구글이나 마이크로소프트 같은 세계 최고의 빅테크 기업들이 천문학적인 비용을 들여 만드는 최첨단 모델들과 어깨를 나란히 한다는 뜻입니다 [출처: Rio de Janeiro's 'Homegrown' AI Was Someone Else's Model Wit...](https://dev.to/jamilxt/rio-de-janeiros-homegrown-ai-was-someone-elses-model-with-a-new-name-jcb). 

만약 한 도시의 정부 기관이 이런 어마어마한 인공지능을 완전히 '자체 개발'해 냈다면, 이는 인류 기술사에 남을 엄청난 성취였을 것입니다. 하지만 이 위대한 축제는 곧바로 치명적인 의혹에 휩싸이고 맙니다.

## 쉽게 풀어보기: '독자 개발'과 '모델 병합'의 결정적 차이

이 사건의 핵심을 찌르기 위해서는, 인공지능을 '독자적으로 학습(Train)시키는 것'과 단순히 '병합(Merge)하는 것'의 본질적인 차이를 이해해야 합니다.

비유하면, 여러분이 세상에 없던 전혀 새로운 맛의 특제 카레를 세상에 내놓는다고 상상해보세요.
**'독자 개발(자체 학습)'**은 밭에서 직접 감자와 양파를 기르고, 인도의 척박한 땅에서 향신료를 수입해 배합 비율을 수천 번 테스트하며 나만의 완벽한 카레 가루를 만들어내는 험난한 여정입니다. 엄청난 시간과 막대한 돈, 그리고 수많은 전문가의 땀방울이 필요합니다. AI 세계로 치면, 이는 수천 대의 초고가 컴퓨터(GPU)를 수개월 동안 밤낮없이 가동하며 방대한 양의 데이터를 처음부터 숟가락으로 떠먹여 가르치는 고독하고 혹독한 과정입니다.

반면 **'모델 병합(Model Merge)'**은 완전히 다른 이야기입니다. 동네 대형 마트에서 이미 베스트셀러로 팔리고 있는 'A사 고형 카레'와 'B사 매운맛 카레'를 사 와서 커다란 냄비에 한꺼번에 넣고 끓이는 것과 같습니다. 두 카레가 섞이면서 제법 그럴싸하고 맛있는 결과물이 나올 수는 있습니다. 하지만 이 섞인 요리를 대중 앞에 내놓고 "이것은 우리 시정부가 수년간 연구해 밑바닥부터 독자적으로 개발한 혁신적인 신제품 카레입니다!"라고 광고한다면 어떨까요? 이는 명백한 기만행위가 됩니다.

안타깝게도 리우데자네이루가 발표한 "자체 개발" AI 모델은 완전히 새로운 기반에서 독립적으로 훈련된 시스템이 아니었습니다 [출처: RiodeJaneiro's"homegrown"LLMappearstobeamergeofan...](https://deepintellica.com/ai-work/rio-de-janeiro-s-homegrown-llm-appears-to-be-a-merge-of-an-existing-model/). 

## 현재 상황: 깃허브 명탐정들의 활약과 궁색한 해명

놀랍게도 이 거대한 기술적 허풍을 가장 먼저 잡아낸 곳은 대형 언론사도, 정부의 감사 기관도 아니었습니다. 전 세계 수천만 명의 프로그래머가 활동하는 소프트웨어 개발 플랫폼인 '깃허브(GitHub)'의 평범한 개발자들이었습니다. 깃허브의 오류 보고 공간인 '이슈(Issue)' 게시판에 누군가 예리한 질문을 던지면서 진실의 판도라 상자가 열린 것입니다 [출처: Cosmic Rundown: Billion Dollar Essays, Rio's LLM Drama, Context Window Limits](https://www.cosmicjs.com/blog/cosmic-rundown-billion-dollar-essays-rio-llm-context-windows). 

커뮤니티의 분석 결과, 이 '자체 개발 모델'은 사실 기존에 인터넷에 무료로 공개되어 누구나 다운로드할 수 있었던 **'Nex-AGI'**라는 모델과 **'Qwen3'**라는 모델을 정교하게 섞어 놓은(Merge) 것이라는 사실이 낱낱이 드러났습니다 [출처: Rio LLM Exposed: Major Model Merge, Not Original AI](https://www.squaredtech.co/rios-official-ai-model-is-proven-to-be-a-model-merge), [출처: RiodeJaneiro's"homegrown"LLMappearstobeamergeofan...](https://deepintellica.com/ai-work/rio-de-janeiro-s-homegrown-llm-appears-to-be-a-merge-of-an-existing-model/). 

컴퓨터 코드와 수학적 수치로 이루어진 AI 모델의 내부 뇌 구조를 뜯어본 결과, 바닥부터 새롭게 공부했다는 증거는 단 하나도 발견되지 않았습니다. 오직 남의 모델들을 물리적으로 혼합한 명백한 물증만 쏟아져 나온 것입니다 [출처: Rio LLM Exposed: Major Model Merge, Not Original AI](https://www.squaredtech.co/rios-official-ai-model-is-proven-to-be-a-model-merge). 개발자들의 놀이터인 깃허브가 마치 부패를 고발하는 신문고나 날카로운 탐사보도 블로그처럼 쓰인 셈입니다 [출처: Hacker News 20 on X: "Rio de Janeiro's "homegrown" LLM appears to be a merge of an existing model https://t.co/G1dBFWiQcO (https://t.co/Uht1ZUEPrL)" / X](https://x.com/betterhn20/status/2066300653404667962), [출처: RiodeJaneiro's"homegrown"LLMappearstobeamergeofan...](https://deepintellica.com/ai-work/rio-de-janeiro-s-homegrown-llm-appears-to-be-a-merge-of-an-existing-model/).

비판의 목소리가 산불처럼 번지자, 개발을 주도했던 이플랜리우(IplanRIO) 측은 황급히 해명문을 내놓았습니다. 그들은 "우리가 이전 버전을 업로드하는 과정에서 잘못된 파일을 올리는 실수를 범했다. 최종적으로 완성된 **'증류 모델(Distilled model)'**을 올렸어야 했는데, 작업 중간 단계였던 **'기본 병합 버전(Base merged version)'**을 실수로 잘못 올렸다"며 사과했습니다 [출처: RiodeJaneiro's"homegrown"LLMappearstobeamergeofan...](https://news.ycombinator.com/item?id=48528371).

여기서 말하는 **'증류(Distillation)'**란 또 무엇일까요? 커다란 커피 머신에서 거대한 양의 원두를 강하게 압착해 아주 진하고 향긋한 에스프레소 원액 한 잔을 추출하는 것을 떠올려보세요. AI 분야에서 증류 기술은, 덩치가 너무 커서 다루기 힘든 천재 AI(선생님 모델)의 핵심 지식만 쏙쏙 뽑아내어, 스마트폰처럼 작은 기기에서도 빠르게 돌아가는 가벼운 AI(학생 모델)로 압축하는 고도의 기술입니다. 

즉, 시정부의 변명은 "우리가 다른 모델들을 섞어서 냄비에 끓인(Merge) 것은 맞지만, 원래 대중에게 공개하려고 했던 것은 그 결과물을 예쁘게 압축해낸 완성판 에스프레소(증류 모델)였다"라는 뜻입니다. 하지만 백번 양보해 단순 업로드 실수였다고 쳐도, 시민의 세금이 투입된 공공 인공지능의 뼈대가 결국 '남의 모델을 섞어 만든 것'이라는 본질은 조금도 변하지 않습니다.

## 앞으로의 전망: 재포장의 시대, 진짜 혁신을 가려내는 법

이번 '리우데자네이루 스캔들'은 자신만의 독자적인 AI 생태계를 구축하려는 전 세계의 수많은 지자체와 기업들에게 무거운 현실의 벽을 깨닫게 해주었습니다. 

소셜 미디어 X(옛 트위터)에서 활동하는 한 유명 기술 전문가는 이 촌극을 지켜보며 이렇게 날카롭게 꼬집었습니다. "리우데자네이루의 자체 개발이라는 모델이요? 결국 기존 모델들의 짜깁기로 밝혀졌죠. '로컬 AI'를 둘러싼 뜨거운 기대감(Hype)은 항상 똑같은 거대한 벽에 머리를 부딪히고 맙니다. 세상에 없던 완전히 새로운 것을 실제로 만들어내는 것은 너무나도 혹독하고 어려운 일인 반면, 기존에 있던 것을 그럴싸하게 재포장(Repackaging)하는 것은 훨씬 쉽기 때문입니다." [출처: Anto Patrex on X: "Rio de Janeiro's supposedly homegrown LLM? Turns out it's a merge of existing models. The hype around 'local AI' keeps running into the same wall: actually building something novel is hard. Repackaging is easier." / X](https://x.com/antopatrex1/status/2066375933108314528)

앞으로 인공지능 기술이 우리 삶 깊숙이 들어옴에 따라, 수많은 기관들이 앞다투어 "우리가 드디어 독자적인 인공지능을 완성했다!"며 화려한 팡파르를 울릴 것입니다. 하지만 우리는 이제 그 화려한 포장지 속을 아주 주의 깊고 비판적인 시선으로 들여다봐야 합니다. 겉보기에는 수천억 개의 파라미터를 가진 위대한 발명품처럼 보여도, 그 속은 누군가 피땀 흘려 만들어 놓은 무료 오픈소스 모델을 슬쩍 비벼 놓은 것에 불과할지도 모르기 때문입니다. 

## AI의 시선: 투명성이 곧 최고의 기술력이다

인공지능 모델의 거대한 규모나 천문학적인 파라미터 숫자가 도시나 국가의 기술적 자존심을 대변하는 시대가 되었습니다. 자체적인 기술력을 확보하려는 리우데자네이루의 열망 자체를 무조건 비난할 수는 없습니다. 막대한 자본력의 한계를 극복하기 위해 기존의 오픈소스 기술을 영리하게 결합하고 활용하는 것은 현대 소프트웨어 개발의 자연스럽고 효율적인 흐름이기도 합니다.

하지만 전 세계 수많은 천재 개발자들이 두 눈을 부릅뜨고 지켜보는 투명한 오픈소스 생태계 앞에서는, 어설픈 재포장과 과장 광고가 오히려 신뢰를 심각하게 깎아내린다는 사실을 잊지 말아야 합니다. 진정한 기술적 독립과 주권 확보는 인터넷에 떠도는 레시피를 따라 조미료를 섞고 거창한 이름을 붙이는 데서 나오지 않습니다. 척박한 환경 속에서도 정직하게 양질의 로컬 데이터를 수집하고, 자신들의 한계를 투명하게 공유하며 한 걸음씩 나아가는 인내 속에서만 진짜 혁신의 꽃이 피어날 수 있습니다. 리우데자네이루의 짧고 허망했던 하루 천하는 AI 시대를 살아가는 우리 모두에게 가장 쓰라리지만 값진 교훈을 남겼습니다.

## 참고자료

1. [Rio de Janeiro's 'Homegrown' AI Was Someone Else's Model Wit...](https://dev.to/jamilxt/rio-de-janeiros-homegrown-ai-was-someone-elses-model-with-a-new-name-jcb)
2. [RiodeJaneiro's"homegrown"LLMappearstobeamergeofan... (Deep Intellica)](https://deepintellica.com/ai-work/rio-de-janeiro-s-homegrown-llm-appears-to-be-a-merge-of-an-existing-model/)
3. [Rio LLM Exposed: Major Model Merge, Not Original AI](https://www.squaredtech.co/rios-official-ai-model-is-proven-to-be-a-model-merge)
4. [Cosmic Rundown: Billion Dollar Essays, Rio's LLM Drama, Context Window Limits](https://www.cosmicjs.com/blog/cosmic-rundown-billion-dollar-essays-rio-llm-context-windows)
5. [Hacker News 20 on X: "Rio de Janeiro's "homegrown" LLM appears to be a merge of an existing model https://t.co/G1dBFWiQcO (https://t.co/Uht1ZUEPrL)" / X](https://x.com/betterhn20/status/2066300653404667962)
6. [RiodeJaneiro's"homegrown"LLMappearstobeamergeofan... (Hacker News Discussion)](https://news.ycombinator.com/item?id=48528371)
7. [Anto Patrex on X: "Rio de Janeiro's supposedly homegrown LLM? Turns out it's a merge of existing models. The hype around 'local AI' keeps running into the same wall: actually building something novel is hard. Repackaging is easier." / X](https://x.com/antopatrex1/status/2066375933108314528)