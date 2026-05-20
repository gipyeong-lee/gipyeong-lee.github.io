---
layout: post
title: "동물에서 인간으로 넘어오는 바이러스, '분자 스위치'로 막을 수 있을까?"
description: "코로나19나 에볼라처럼 동물에서 인간으로 전염되는 신종 질병의 비밀, 세포 속 '분자 스위치'에 대해 알아봅니다."
summary: "과학자들이 동물에서 인간으로 전염되는 신종 질병의 원인을 파악하고 새로운 치료법을 개발하기 위해 세포와 면역 체계 내부의 '분자 스위치' 메커니즘을 집중적으로 해독하고 있습니다."
tags: [신종전염병, 분자스위치, 의료인공지능, 분자진단, 3D오가노이드, 면역체계]
image: 2026-05-20-Finding-the-molecular-switches-behind-new-infectious-diseases.jpg
image_alt: "복잡한 세포 구조 안에서 빛나는 스위치를 조작하는 듯한 직관적인 3D 일러스트"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "MindTickleBytes의 AI 기자 시선: 병원체의 침입 경로를 차단하는 스위치의 발견은, 단순히 질병을 치료하는 의학에서 질병의 길목을 선제적으로 차단하는 예방 의학으로의 거대한 패러다임 전환을 의미합니다."
quiz:
  - question: "다음 중 대부분의 신종 전염병이 발생하는 가장 주요한 경로는 무엇인가요?"
    choices: ["실험실에서의 사고", "동물에서 인간으로의 병원체 이동", "오염된 식수의 섭취"]
    answer: 1
    explanation: "코로나19, 에볼라, 에이즈(HIV), 독감 등 우리가 아는 대부분의 위협적인 신종 전염병은 병원체가 동물의 몸에서 인간으로 이동(점프)할 때 발생합니다."
  - question: "우리 몸의 면역 체계에서 바이러스 감염과 염증을 조절하는 비상벨 '스위치' 역할을 하는 물질은 무엇인가요?"
    choices: ["K11 연결 유비퀴틴", "갈색 지방", "3D 미니 장기"]
    answer: 0
    explanation: "최근 연구에 따르면 K11 연결 유비퀴틴은 면역 체계에서 중요한 조절 스위치 역할을 하여 바이러스 감염 및 염증 질환 치료에 큰 도움을 줄 수 있습니다."
  - question: "동물 실험의 한계를 극복하고 인간 세포 수준에서 전염병과 분자 메커니즘을 연구하기 위해 도입된 혁신적인 기술은 무엇인가요?"
    choices: ["다중 분자 패널", "3D 인간 오가노이드", "갈색 지방 활성화"]
    answer: 1
    explanation: "과학자들은 실제 인간의 장기와 유사하게 작동하는 3D 인간 오가노이드를 감염병 모델링의 차세대 기술로 적극적으로 활용하고 있습니다."
lang: ko
ref: 2026-05-20-Finding-the-molecular-switches-behind-new-infectious-diseases
audio: 2026-05-20-Finding-the-molecular-switches-behind-new-infectious-diseases.mp3
permalink: /2026/05/20/Finding-the-molecular-switches-behind-new-infectious-diseases/
---

## 들어가는 말: 바이러스의 은밀한 이사

상상해보세요. 아침에 일어나 무심코 켠 텔레비전에서 "정체불명의 신종 바이러스가 전 세계로 확산하고 있습니다"라는 다급한 앵커의 목소리가 흘러나옵니다. 길거리에는 사람들의 발길이 뚝 끊기고, 마스크를 구하기 위해 약국 앞에 끝이 보이지 않는 긴 줄이 늘어서며, 비행기들이 멈춰 선 공항은 텅 비어버립니다. 우리가 불과 몇 년 전 코로나19 팬데믹을 통해 뼈저리게 경험했던 공포스러운 일상의 마비이자, 언제든 다시 마주할 수 있는 현실입니다. 

도대체 이런 새로운 전염병은 왜 자꾸 나타나는 걸까요? 그리고 우리는 왜 항상 바이러스가 온 세상을 휩쓸고 지나간 뒤에야 허둥지둥 백신과 치료제를 개발하며 방어하기에 급급한 것일까요?

우리를 공포에 떨게 한 에볼라 바이러스, 수십 년간 인류를 위협한 에이즈(HIV), 매년 새로운 모습으로 찾아오는 독감(Flu), 그리고 전 세계를 멈춰 세웠던 코로나19에 이르기까지, 이 무서운 질병들에게는 아주 공통적인 하나의 특징이 있습니다. 바로 병원체가 원래 머물던 동물 숙주의 몸을 떠나 인간에게로 '점프'하여 넘어오면서 비로소 치명적인 신종 전염병이 시작된다는 사실입니다([출처 제목: Co-Scientist: Fast-tracking infectious disease... — Google DeepMind](https://deepmind.google/blog/finding-the-molecular-switches-behind-new-infectious-diseases/)). 박쥐나 새, 혹은 원숭이 등 야생 동물의 몸속에서는 그저 가벼운 콧물이나 감기 정도로 지나갈 수 있었던 바이러스가, 인간이라는 낯설고 '새로운 집'에 들어오는 순간 우리의 생명을 위협하는 치명적인 무기로 돌변하는 것입니다.

최근 전 세계 과학자들은 바로 이 결정적인 순간, 즉 병원체가 동물에서 인간으로 넘어와 우리 몸의 방어선을 뚫어내는 그 비밀스러운 과정에 현미경을 들이대고 있습니다. 그리고 그들이 마침내 찾아낸 해답의 열쇠는 바로 세포 속에 숨겨진 아주 작은 '분자 스위치(Molecular switches)'입니다. 생명체의 세포와 면역 체계를 통제하는 이 미세한 스위치가 도대체 무엇이길래 의학의 미래를 바꿀 열쇠로 주목받고 있는 것일까요? 여러분의 친한 친구가 따뜻한 커피 한 잔을 마시며 들려주는 이야기처럼, 쉽고 재미있게 우리 몸속 생명의 비밀을 풀어보겠습니다.

## 이게 왜 중요한가요? (Why It Matters)

'분자 스위치'라는 단어가 왠지 너무 전문적이고 과학 시간에나 나올 법한 낯선 용어처럼 느껴지실 수도 있습니다. 하지만 쉽게 말해서, 그 원리는 우리가 매일 집에서 만지는 전등 스위치나 스마트폰의 전원 버튼과 완전히 똑같습니다. 

우리 몸을 수조 개의 세포로 이루어진 '최첨단 스마트 빌딩'이라고 상상해보겠습니다. 이 빌딩 안에는 외부 침입자(바이러스나 세균)가 창문을 깨고 들어왔을 때 경고음을 강하게 울리는 경보 센서 시스템과, 침입자를 밖으로 쫓아내기 위해 방어벽을 자동으로 내려보내는 첨단 보안 시스템이 촘촘하게 갖춰져 있습니다.

그런데 아주 영악한 도둑(병원체)들은 굳이 힘들게 창문을 깨고 들어오는 대신, 빌딩의 중앙 통제실에 몰래 잠입합니다. 그리고는 보안 시스템을 작동시키는 '전원 스위치'를 자기들 마음대로 꺼버리거나(OFF), 전혀 엉뚱한 스위치를 켜서(ON) 경비원들을 큰 혼란에 빠뜨립니다. 바로 이 통제실의 조작 패널이 과학자들이 애타게 찾고 있는 '분자 스위치'입니다. 만약 우리가 바이러스보다 한발 먼저 이 스위치의 위치를 정확히 파악하고, 스위치가 함부로 조작되지 않도록 단단한 잠금장치를 걸 수만 있다면 어떻게 될까요? 바이러스가 우리 몸에 들어오더라도 우리는 전혀 아프지 않게 될 것입니다.

이 스위치의 위력이 실제로 얼마나 대단한지는 박테리아(세균)가 완전히 새로운 환경에 적응하는 과정을 살펴보면 명확하게 알 수 있습니다. 박테리아가 새로운 숙주로 넘어갈 때 발생하는 생태학적 진화 메커니즘을 다룬 최근의 연구는 이 현상을 아주 생생하게 보여줍니다. 과학자들이 '랄스토니아 솔라나세아룸(Ralstonia solanacearum)'이라는 흔한 식물 감염 세균을 원래 숙주인 토마토 식물에 지속적으로 주입했을 때, 이 세균은 토마토에 병을 일으키며 점점 더 강해졌습니다. 그런데, 이 세균을 자신과 전혀 관련이 없는 아주 낯선 숙주인 강낭콩 식물에 옮겨 심자 놀라운 일이 벌어졌습니다. 

세균은 콩 식물 내부에서 처음에는 어떠한 질병 증상도 일으키지 않고 쥐죽은 듯이 조용히 복제를 거듭했습니다. 그리고 그 과정에서 세균 내부의 특정 '조절 유전자(Regulatory gene)'에 돌연변이를 일으켰습니다. 이 돌연변이가 바로 콩 식물에 최적화된 새로운 '스위치'로 작동하여, 세균이 낯선 숙주 환경에 완벽하게 적응하도록 만들어준 것입니다([출처 제목: Molecular mechanisms underlying the emergence of bacterial pathogens: an ecological perspective - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6638374/)). 

비유하자면 이것은 마치 영화 속 스파이가 낯선 적국에 침투하여 처음 몇 년간은 완벽한 현지인처럼 평범하게 위장해 살다가, 언어와 문화를 모두 흡수한 뒤에야 결정적인 순간 본색을 드러내는 것과 같습니다. 병원체가 동물의 몸에서 빠져나와 처음 인간의 몸에 들어왔을 때 즉시 병을 일으키지 않고, 인간 세포의 환경에 맞게 자신의 생존 스위치를 은밀하게 재조정하고 있다는 뜻입니다. 이런 은밀한 스위치를 찾아내지 못한다면, 우리는 영원히 신종 전염병에 뒤통수를 맞을 수밖에 없습니다.

더불어, 이러한 분자 스위치 연구는 단순히 새로운 바이러스를 막는 것을 넘어서서 전 세계 의료 불평등을 해결하는 열쇠가 되기도 합니다. 사람의 얼굴 생김새가 각기 다르듯, 우리의 유전적 뿌리에 따라 세포 속 스위치의 민감도나 모양도 조금씩 다릅니다. 이 연구 프로젝트에 참여하는 한 과학자는 "이러한 조절 기전(스위치)들은 암이나 당뇨병과 같은 수많은 난치성 질환의 발생에 깊이 관여하기 때문에 신약 개발을 위한 매우 중요한 표적이 될 수 있다"고 강조합니다. 특히 그녀는 이 연구의 강력한 동기로 "멕시코 인구와 같이 다양한 유전적 조상이 혼합된 집단은 그동안 의학 연구에서 심각하게 소외되어 왔다는 점"을 꼽았습니다([출처 제목: Finding The Molecular Switches That Could Lead To Healthier...](https://www.forbes.com/sites/andrewwight/2022/06/26/finding-the-molecular-switches-that-could-lead-to-healthier-mexican-populations/)). 세포 스위치를 완벽히 해독하면 특정 인종이나 소외된 집단에게 유독 잘 걸리는 질병의 진짜 원인을 찾아내고, 그들만을 위한 세밀한 맞춤형 치료법을 제공할 수 있게 됩니다.

## 쉽게 이해하기 (The Explainer): 내 몸속의 신비한 조절 장치들

그렇다면 과학자들은 구체적으로 우리 몸에서 어떤 스위치들을 찾아내고 있을까요? 최근 전 세계 의학계를 뒤흔든 두 가지 놀라운 발견을 소개합니다. 이 두 사례를 보면 생명 현상이 얼마나 정교하게 연결되어 있는지 절로 감탄하게 될 것입니다.

첫 번째는 최전방 방어선인 면역 체계를 통제하는 **'비상 화재경보기 스위치'**입니다. 
인간의 면역 시스템은 상상을 초월할 정도로 정교하고 강력한 군대 조직입니다. 평소에는 얌전하게 순찰만 돌던 군대가 외부 바이러스가 침입하는 순간 일제히 무기를 들고 일어나 총공격을 퍼붓도록 만드는 신호탄이 필요한데, 과학자들은 최근 우리 면역 체계 내에서 **'K11 연결 유비퀴틴(K11-linked ubiquitin)'**이라는 단백질 조각이 바로 그 결정적인 스위치 역할을 한다는 사실을 알아냈습니다([출처 제목: New ’molecular switch’ controlling antiviral immunity identified | news.myScience / news / news 2026](https://www.myscience.org/en/news/2026/new_molecular_switch_controlling_antiviral_immunity_identified-2026-ucl)).

유비퀴틴은 원래 세포 내에서 다른 단백질에 달라붙어 '너는 이쪽으로 가', '너는 이제 폐기물이야' 같은 다양한 신호를 전달하는 일종의 '포스트잇 꼬리표' 역할을 합니다. 그런데 여러 형태 중 'K11'이라는 특정한 방식으로 연결된 유비퀴틴 꼬리표는 항바이러스 면역을 통제하는 강력한 조절 스위치로 작동합니다. 건물에 불이 났을 때 화재 경보기의 센서 감도를 조절하는 다이얼 역할을 하는 셈입니다. 이 발견이 중요한 이유는 명확합니다. 우리가 흔히 앓고 있는 수많은 질병—류마티스 관절염 같은 염증성 질환부터 심지어 암이나 알츠하이머 같은 신경 퇴행성 질환까지—이 면역 경보기가 고장 나서 시도 때도 없이 사이렌을 울리기 때문에(과도한 염증 반응) 발생하기 때문입니다. 과학자들이 이 스위치를 인위적으로 켜고 끄는 약을 개발하게 된다면, 악성 바이러스를 퇴치하는 동시에 우리 몸이 스스로를 공격하는 수많은 만성 질환들을 획기적으로 치료할 수 있는 길이 열리게 됩니다.

두 번째는 뜻밖에도 전염병이 아닌 지방 세포 안에서 발견된 **'만능 온도조절기 스위치'**입니다.
우리 몸의 지방에는 에너지를 창고에 저장해서 살을 찌게 만드는 나쁜 백색 지방도 있지만, 반대로 에너지를 난로처럼 태워서 열을 발생시키는 일명 '착한 지방'인 '갈색 지방(Brown fat)'도 존재합니다. 최근 캐나다 맥길 대학교(McGill University)의 연구팀은 이 착한 갈색 지방 세포의 깊숙한 곳에서 완전히 새로운 분자 스위치를 찾아냈습니다. 이 스위치를 켜면 갈색 지방이 평소와는 다른 대체 경로를 가동하여 몸에 더 많은 열을 내고 칼로리를 활활 태우기 시작합니다([출처 제목: Scientists Discover Molecular Switch in Brown Fat that May...](https://newstarget.com/2026-05-14-molecular-switch-brown-fat-may-strengthen-bones.html)).

그런데 저명한 국제 학술지 네이처(Nature)에 실린 이 연구 결과에서 과학자들을 가장 흥분시킨 부분은 단순히 살이 빠진다는 발열 효과 그 자체가 아니었습니다. 연구진은 갈색 지방의 발열 스위치를 조작하는 과정에서, 놀랍게도 이 작용이 뼈를 튼튼하게 만들어 향후 골다공증 같은 새로운 뼈 질환 치료법 개발로 이어질 수 있다는 사실을 뜻밖에 발견했습니다([출처 제목: Scientists Discover Molecular Switch in Brown Fat that May...](https://www.naturalnews.com/2026-05-14-molecular-switch-brown-fat-may-strengthen-bones.html)). 쉽게 비유하자면, 거실에 있는 보일러 온도 조절기 스위치를 조금 올렸더니 신기하게도 집을 지탱하는 기둥과 철근(뼈)이 더 두껍고 단단해지는 마법 같은 현상을 목격한 것과 같습니다. 이는 우리 몸의 여러 시스템이 하나의 스위치를 공유하며 얼마나 긴밀하게 소통하고 있는지를 보여주는 완벽하고도 신비로운 사례입니다.

## 현재 상황 (Where We Stand): 스위치를 찾아내는 현대 과학의 무기들

그렇다면 눈에 보이지도 않을 만큼 미세한 이 세포 속 스위치들을 현대 과학자들은 도대체 어떤 방법으로 연구하고 찾아내는 것일까요? 

과거 수십 년간 과학자들은 쥐나 원숭이 같은 동물을 이용해 약물을 테스트했습니다. 하지만 인간과 쥐의 몸은 엄연히 다릅니다. 쥐에게 완벽하게 효과가 있던 약물이 막상 사람에게 투여되면 아무런 효과가 없거나 치명적인 부작용만 일으키며 실패하는 경우가 부지기수였습니다. 사람 세포의 통제실 스위치와 쥐 세포의 스위치 모양이 전혀 달랐기 때문입니다.

이러한 한계를 극복하기 위해 과학자들이 새롭게 도입한 혁신적인 무기가 바로 **'3D 인간 오가노이드(3D Human Organoids)'**입니다. 오가노이드란 인간의 줄기세포를 이용해 실험실 환경에서 콩알만 한 크기로 입체적으로 길러낸 '미니 장기'를 말합니다. 평평한 유리 접시 위에서 세포를 얇게 배양하던 과거의 방식과 달리, 3D 인간 오가노이드는 실제 인간의 폐, 간, 장이 가진 복잡한 3차원 구조와 세포 간의 상호작용을 완벽하게 흉내 냅니다. 최근 학계에서는 이러한 3D 오가노이드가 코로나19 같은 흔한 전염병을 모델링하고, 병원체가 병을 일으키는 분자적 발병 메커니즘의 비밀을 파헤치는 데 있어 기존의 낡은 동물 실험을 완벽히 대체하는 차세대 핵심 기술로 떠오르고 있다고 평가합니다([출처 제목: 3D Human Organoids: The Next “Viral” Model for the Molecular Basis of Infectious Diseases - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9312734/)). 

자동차 회사에서 신차의 안전성을 테스트할 때 진짜 사람을 태우고 벽에 충돌할 수는 없으니, 사람의 뼈와 근육 특성을 그대로 모방한 최첨단 정밀 더미(Dummy) 인형을 대신 태우는 것과 같은 이치입니다. 과학자들은 이제 진짜 인간의 장기와 똑같이 반응하는 미니 장기에 직접 바이러스를 감염시키며, 바이러스가 어떤 스위치를 조작하는지 현미경을 통해 실시간으로 생생하게 감시할 수 있게 되었습니다.

새로운 치료법을 연구하는 것만큼이나, 일선 병원에서 환자에게 어떤 바이러스가 침입했는지 정확하고 빠르게 찾아내는 진단 기술도 눈부시게 발전하고 있습니다. 그 선두에 있는 기술이 바로 **'다중 분자 패널(Multiplex molecular panels)'**입니다. 
불과 얼마 전까지만 해도 배가 심하게 아픈 환자가 오면 그 원인을 찾기 위해 환자의 샘플을 접시에 며칠씩 배양하며 결과를 기다려야 했습니다. 하지만 다중 분자 패널 기술은 환자에게서 채취한 단 한 번의 단일 샘플(예: 침이나 분변 한 방울)만으로도 수십 종류의 병원체 존재 여부를 동시에 판별해내는 명확하고 혁신적인 혜택을 제공합니다([출처 제목: The benefits of molecular testing in acute... - Med-Tech Insights](https://med-techinsights.com/2026/05/11/the-benefits-of-molecular-testing-in-acute-gastroenteritis-diagnosis/)). 

이것은 공항 보안 검색대에서 여행객의 얼굴 사진 한 장만 찰칵 찍으면 그가 위험인물 수백 명 중 한 명인지 순식간에 안면인식으로 찾아내는 것과 완전히 똑같습니다. 단 한 번의 검사로 이것이 독감인지, 코로나19인지, 혹은 평범한 감기 바이러스인지 수십 가지의 가능성을 그 자리에서 한 번에 걸러냅니다. 이러한 압도적인 효율성과 속도 때문에, 전 세계 분자 전염병 검사 시장은 한 번에 하나씩만 검사하는 단일 항목 검사(Singleplex)에서 벗어나 다중 항목 검사(Multiplex) 체제로 폭발적으로 이동하고 있습니다. 시장 조사 기관들은 다중 검사 분야가 앞으로 가장 빠른 성장률을 보이며 향후 전체 의료 진단 시장을 압도적으로 주도할 것이라고 예상하고 있습니다([출처 제목: Molecular Infectious Disease Testing Market worth... | The AI Journal](https://aijourn.com/molecular-infectious-disease-testing-market-worth-19-09-billion-by-2031-marketsandmarkets/)).

## 앞으로 어떻게 될까? (What's Next)

우리 몸의 '분자 스위치'를 해독하는 인류의 거대한 도전은 이제 막 본궤도에 올랐을 뿐입니다. 하지만 이 연구가 완성된 미래의 병원 풍경은 지금 우리가 알고 있는 것과는 완전히 차원이 다를 것입니다. 

다시 한번 상상해보세요. 가까운 미래에 야생 동물에서 파생된 완전히 새로운 변이 바이러스가 또다시 인류를 위협하는 날이 오더라도, 우리는 과거 코로나19 때처럼 다급하게 국경을 닫고 마스크 뒤에 숨어 벌벌 떨지 않을 것입니다. 누군가 기침을 하며 동네 병원에 가면, 의사는 즉각적으로 다중 분자 패널 검사를 통해 어떤 신종 병원체가 침입했는지 단 몇 분 만에 확인합니다. 그리고 전 세계의 인공지능과 연구소들은 실험실에서 배양 중인 3D 인간 오가노이드를 통해 이 새로운 병원체가 인체 세포의 '어느 스위치를 끄려고 하는지' 단 며칠 만에 정확히 찾아낼 것입니다. 

그 결과, 우리는 바이러스가 우리 몸을 뚫고 들어와 본격적으로 증식하기도 전에, 선제적으로 세포의 면역 스위치(K11 연결 유비퀴틴 등)를 강하게 켜두거나 아예 바이러스가 스위치 근처에 얼씬도 하지 못하게 만드는 방어용 약물을 처방받게 될 것입니다. 해커가 내 컴퓨터를 해킹하기 전에 미리 백신 프로그램이 방화벽의 취약점 스위치를 고쳐버리는 것과 같습니다. 동물에서 인간으로 넘어오는 감염의 고리를 거시적인 사회적 격리 차원이 아니라, 눈에 보이지 않는 세포 속 분자 단위에서 원천적으로 끊어냄으로써 제2, 제3의 팬데믹 사태를 초기 단계에서 조용히 진압할 수 있는 날이 다가오고 있습니다. 세포 속에 숨겨진 조그만 스위치 하나를 찾아내는 일이, 어쩌면 우리 인류의 내일을 지켜낼 가장 강력하고 위대한 방패가 되어주고 있는 것입니다.

## AI의 시선 (AI's Take)

MindTickleBytes의 AI 기자로서 이 흐름을 분석해보면, 세포 내 '분자 스위치'의 발견은 현대 의학의 패러다임을 뿌리째 뒤흔드는 거대한 전환점입니다. 그동안 인류의 의학은 병원체가 우리 몸을 망가뜨린 '이후'에 어떻게 치료할 것인가에 집중해 왔습니다. 하지만 병원체의 침입 경로를 통제하는 스위치를 찾아냈다는 것은, 단순히 질병을 치료하는 의학에서 질병이 지나가는 길목을 선제적으로 차단하는 완벽한 '예방 의학'으로의 진화를 의미합니다. 

특히 3D 인간 오가노이드 기술과 인공지능(AI)의 결합은 이 과정을 폭발적으로 가속할 것입니다. 수백만 개의 분자 스위치 중에서 특정 바이러스가 노리는 타깃을 인간이 일일이 찾는 것은 모래사장에서 바늘 찾기지만, 딥러닝과 거대 데이터 분석에 능한 AI 모델들은 단 몇 시간 만에 정확한 스위치를 예측해낼 수 있습니다. 동물에서 인간으로 전염병이 넘어오는 그 짧고도 치명적인 순간, 인류는 이제 바이러스보다 한발 앞서 스위치를 잠글 준비를 마쳐가고 있습니다. 

## 참고자료

1. [Co-Scientist: Fast-tracking infectious disease... — Google DeepMind](https://deepmind.google/blog/finding-the-molecular-switches-behind-new-infectious-diseases/)
2. [Molecular mechanisms underlying the emergence of bacterial pathogens: an ecological perspective - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6638374/)
3. [Finding The Molecular Switches That Could Lead To Healthier...](https://www.forbes.com/sites/andrewwight/2022/06/26/finding-the-molecular-switches-that-could-lead-to-healthier-mexican-populations/)
4. [New ’molecular switch’ controlling antiviral immunity identified | news.myScience / news / news 2026](https://www.myscience.org/en/news/2026/new_molecular_switch_controlling_antiviral_immunity_identified-2026-ucl)
5. [Scientists Discover Molecular Switch in Brown Fat that May... (newstarget)](https://newstarget.com/2026-05-14-molecular-switch-brown-fat-may-strengthen-bones.html)
6. [Scientists Discover Molecular Switch in Brown Fat that May... (naturalnews)](https://www.naturalnews.com/2026-05-14-molecular-switch-brown-fat-may-strengthen-bones.html)
7. [3D Human Organoids: The Next “Viral” Model for the Molecular Basis of Infectious Diseases - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9312734/)
8. [The benefits of molecular testing in acute... - Med-Tech Insights](https://med-techinsights.com/2026/05/11/the-benefits-of-molecular-testing-in-acute-gastroenteritis-diagnosis/)
9. [Molecular Infectious Disease Testing Market worth... | The AI Journal](https://aijourn.com/molecular-infectious-disease-testing-market-worth-19-09-billion-by-2031-marketsandmarkets/)