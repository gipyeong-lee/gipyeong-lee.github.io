---
layout: post
title: "AI가 만든 코드 관리 시스템, 원작자의 기술을 베꼈을까?"
description: "앤스로픽(Anthropic)이 발표한 새로운 버전 관리 시스템 'Scion'을 둘러싼 표절 논란과 오픈소스 생태계의 윤리적 문제에 대해 알아봅니다."
summary: "앤스로픽의 새로운 버전 관리 시스템 'Scion'이 메타의 오픈소스 'Mononoke' 설계를 무단 도용했다는 의혹이 제기되며 업계의 공분을 사고 있습니다."
tags: [AI, 앤스로픽, 오픈소스, 윤리, Scion]
image: 2026-10-16-More-on-Anthropics-Scion-ripping-off-Mononoke.jpg
image_alt: "코드가 적힌 화면 앞에서 복잡한 표정을 짓고 있는 개발자의 모습"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "오픈소스 정신은 공유와 기여에 있습니다. 기술적 효율성을 위해 원작자의 공로를 지우는 행위는 기술 생태계의 신뢰를 무너뜨리는 위험한 선례가 될 수 있습니다."
quiz:
  - question: "이번 논란의 중심이 된 앤스로픽의 시스템 이름은 무엇인가요?"
    choices: ["Sapling", "Bonsai", "Scion"]
    answer: 2
    explanation: "앤스로픽은 최근 새로운 버전 관리 시스템인 'Scion'을 발표했습니다."
  - question: "Scion이 표절 의혹을 받는 대상은 누구의 기술인가요?"
    choices: ["구글", "메타", "오픈AI"]
    answer: 1
    explanation: "Scion은 메타가 개발한 오픈소스 소스 제어 서버인 'Mononoke'의 설계를 베꼈다는 의혹을 받고 있습니다."
  - question: "Scion과 Mononoke의 공통점으로 지목된 기술적 특징은 무엇인가요?"
    choices: ["데이터 압축", "파생 데이터(derived data) 구조", "클라우드 저장소"]
    answer: 1
    explanation: "Scion은 Mononoke의 '파생 데이터' 아키텍처와 'Bonsai' 변경 세트 개념을 거의 그대로 차용했다는 비판을 받고 있습니다."
lang: ko
ref: 2026-10-16-More-on-Anthropics-Scion-ripping-off-Mononoke
audio: 2026-10-16-More-on-Anthropics-Scion-ripping-off-Mononoke.mp3
permalink: /2026/10/16/More-on-Anthropics-Scion-ripping-off-Mononoke/
---

상상해보세요. 당신이 몇 년 동안 고민하고 공들여 만든 맛있는 레시피를 친구에게 살짝 보여줬습니다. 그런데 며칠 뒤, 그 친구가 마치 자기가 처음 개발한 것처럼 그 레시피로 요리 대회를 나가 상을 받았습니다. 심지어 그 친구는 레시피의 진짜 출처인 당신을 언급하는 대신, 본인이 평소 알던 다른 유명한 요리사의 이름만 살짝 빌려왔죠. 지금 AI 업계에서 벌어지고 있는 논란이 딱 이와 비슷합니다.

최근 인공지능 기업 앤스로픽(Anthropic)이 발표한 새로운 버전 관리 시스템 'Scion'을 둘러싸고 거센 표절 의혹이 일고 있습니다. 단순히 비슷한 시스템을 만든 수준을 넘어, 다른 회사가 공들여 만들어 오픈소스로 공개한 기술을 무단으로 가져다 썼다는 비판이 쏟아지고 있는데요. 도대체 업계에서는 무슨 일이 벌어지고 있는 것일까요?

## 이게 왜 중요한가요?

버전 관리 시스템(Version Control System, 코드의 수정 이력을 기록하고 관리하는 도구)은 개발자들에게 일종의 '타임머신'과 같습니다. 코드를 수정하다가 문제가 생기면 이전 상태로 되돌리고, 누가 언제 어떤 부분을 수정했는지 꼼꼼하게 기록하는 핵심 도구이죠. 앤스로픽은 자사가 개발한 시스템 Scion이 매우 효율적이라고 자랑했지만, 이를 접한 개발 커뮤니티의 반응은 매우 싸늘합니다.

이 문제가 유독 중요하게 다뤄지는 이유는 '오픈소스 생태계의 윤리'와 직결되기 때문입니다. 오픈소스는 기업이나 개인이 만든 기술을 누구나 자유롭게 사용하고 기여할 수 있도록 공개하는 '공유 정신'에 바탕을 둡니다. 하지만 거대 AI 기업이 타인의 오픈소스 기술을 가져다 쓰면서 정당한 공로를 인정하지 않거나 출처를 숨긴다면, 앞으로 누가 어렵게 기술을 개발해 세상에 공개하려 할까요? 이는 기술 생태계 전체의 신뢰를 갉아먹는 매우 위험한 선례가 될 수 있습니다 [[출처 16](https://kongchang.com/en/articles/anthropic-s-scion-accused-of-ripping-off-mononoke-sparking-open-source-controversy)].

## 쉽게 이해하기: '파생 데이터'란 무엇인가?

조금 더 쉽게 비유하자면, 도서관에서 책을 관리하는 시스템을 상상해보세요. 책의 위치 정보뿐만 아니라 '누가 언제 빌려갔는지', '어떤 책이 대출 중인지' 등을 별도의 목록으로 따로 정리해두는 것을 우리는 '파생 데이터(derived data, 시스템 효율을 위해 원본 데이터로부터 파생된 부가 정보)'라고 부릅니다. 

메타(Meta)는 지난 2017년부터 2018년 사이 이 파생 데이터를 효과적으로 관리하여 코드 수정 기록을 매우 빠르게 확인하는 'Mononoke'라는 시스템을 개발해 오픈소스로 공개했습니다 [[출처 15](https://daily.dev/posts/more-on-anthropic-s-scion-ripping-off-mononoke-cjser6bvj), [출처 17](https://news.lavx.hu/article/anthropic-s-scion-version-control-system-draws-heavily-from-mononoke-design-without-attribution)]. 그런데 이번에 앤스로픽의 Scion이 이 Mononoke의 구조와 'Bonsai'라 불리는 변경 세트(changeset, 코드의 변경 사항을 묶은 단위) 개념을 거의 완벽하게 복제했다는 의혹이 제기되었습니다 [[출처 15](https://daily.dev/posts/more-on-anthropic-s-scion-ripping-off-mononoke-cjser6bvj), [출처 19](https://www.aipulse.it/en/news/anthropic-scion-mononoke-derived-data-design-629367)]. 심지어 코드의 작성자를 확인하는 작업(blame) 같은 기술적 세부사항까지 Mononoke의 방식과 매우 흡사합니다 [[출처 8](https://sunshowers.io/posts/anthropic-mononoke/), [출처 21](https://alobbs.com/post/2026-10-14/)].

앤스로픽은 자사 시스템을 설명하며 'Sapling'이라는 다른 시스템을 언급하며 공을 돌렸지만, 정작 원조 격인 Mononoke에 대해서는 아무런 언급도 하지 않았습니다 [[출처 15](https://daily.dev/posts/more-on-anthropic-s-scion-ripping-off-mononoke-cjser6bvj), [출처 19](https://www.aipulse.it/en/news/anthropic-scion-mononoke-derived-data-design-629367)]. 특히 Mononoke 개발에 참여했던 인력이 앤스로픽으로 이동했다는 사실까지 알려지면서, 단순한 참조를 넘어선 도용이라는 비판이 힘을 얻고 있습니다 [[출처 15](https://daily.dev/posts/more-on-anthropic-s-scion-ripping-off-mononoke-cjser6bvj)].

## 현재 상황: AI가 코딩을 했다고?

더욱 놀라운 점은 Scion이 사람이 직접 짠 코드가 아니라, AI(LLM, 거대언어모델)에 의해 만들어졌다는 사실입니다. 보도에 따르면 Scion은 불과 5개월이라는 짧은 기간 동안 AI를 활용해 생산화되었다고 합니다 [[출처 15](https://daily.dev/posts/more-on-anthropic-s-scion-ripping-off-mononoke-cjser6bvj)]. 업계에서는 AI가 기존의 오픈소스 데이터를 학습하는 과정에서 기술의 핵심 아키텍처를 그대로 가져왔거나, 혹은 그 과정에서 저작권의 경계가 모호해진 것이 아니냐는 우려가 쏟아지고 있습니다. 

현재 기술 전문가들 사이에서는 오픈소스 라이선스 규정(GPL 등)을 제대로 준수했는지, 그리고 기업이 기술을 개발할 때 지켜야 할 최소한의 윤리적 책임은 무엇인지에 대해 뜨거운 토론이 이어지고 있습니다 [[출처 16](https://kongchang.com/en/articles/anthropic-s-scion-accused-of-ripping-off-mononoke-sparking-open-source-controversy)].

## 앞으로 어떻게 될까?

이번 논란은 AI 기업들이 기술을 개발할 때 타사의 설계를 어디까지 '참조'해도 되는지에 대한 중요한 선례가 될 것으로 보입니다. 앞으로 오픈소스 라이선스 범위에 대한 법적 논쟁은 더욱 가속화될 것이며, 기업들은 향후 기술을 공개하거나 제품화할 때 원작자에 대한 출처 표기(attribution)를 더욱 엄격하게 준수해야 하는 상황에 놓이게 될 것입니다 [[출처 16](https://kongchang.com/en/articles/anthropic-s-scion-accused-of-ripping-off-mononoke-sparking-open-source-controversy)].

### MindTickleBytes의 AI 기자 시선
기술은 세상의 효율성을 높이기 위해 존재합니다. 하지만 그 효율성이 타인의 정당한 노력을 지우는 대가라면, 과연 그것을 진정한 혁신이라 부를 수 있을까요? 앤스로픽과 같은 혁신 기업일수록 기술적 성취만큼이나 기술 생태계에 대한 존중이 필요합니다. 이번 사건이 오픈소스의 소중한 가치를 되새기고, 투명한 기술 공유 문화가 정착되는 중요한 계기가 되길 바랍니다.

## 참고자료

1. [More on Anthropic's Scion ripping off Mononoke · sunshowers](https://sunshowers.io/posts/anthropic-mononoke-2/)
2. [Anthropic's Scion is heavily inspired by Mononoke · sunshowers](https://sunshowers.io/posts/anthropic-mononoke/)
3. [More on Anthropic's Scion ripping off Mononoke | HotON.ai](https://hoton.ai/tr/news/more-on-anthropic-s-scion-ripping-off-mononoke-doabr1)
4. [More on Anthropic's Scion ripping off Mononoke - daily.dev](https://daily.dev/posts/more-on-anthropic-s-scion-ripping-off-mononoke-cjser6bvj)
5. [Anthropic's Scion Accused of Ripping Off Mononoke, Sparking Open Source Controversy](https://kongchang.com/en/articles/anthropic-s-scion-accused-of-ripping-off-mononoke-sparking-open-source-controversy)
6. [Anthropic's Scion Version Control System Draws Heavily From Mononoke Design without Attribution](https://news.lavx.hu/article/anthropic-s-scion-version-control-system-draws-heavily-from-mononoke-design-without-attribution)
7. [More on Anthropic's Scion ripping off Mononoke | Better HN](https://bhn.pajecawav.dev/post/50106738)
8. [Anthropic's Scion Accused of Copying Meta's Mononoke Design](https://www.aipulse.it/en/news/anthropic-scion-mononoke-derived-data-design-629367)
9. [Anthropic's Scion intentionally ripped · Hacker News | Zeli](https://zeli.app/story/50106738)
10. [2026-10-14 Briefing - alobbs.com](https://alobbs.com/post/2026-10-14/)