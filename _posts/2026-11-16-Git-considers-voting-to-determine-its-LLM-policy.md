---
layout: post
title: "개발자의 필수 도구 Git, AI 사용 정책을 '투표'로 결정한다?"
description: "오픈소스 버전 관리 시스템 Git이 대규모 언어 모델(LLM) 사용 정책을 정하기 위해 투표를 검토하는 배경과 오픈소스 생태계의 민주적 의사결정 과정을 알아봅니다."
summary: "Git이 AI(LLM) 사용 정책을 결정하기 위한 투표 절차를 검토하면서, 오픈소스 커뮤니티가 기술 변화에 대응하는 새로운 민주적 거버넌스 방식을 모색하고 있습니다."
tags: [Git, LLM, OpenSource, AI Policy, Governance]
image: 2026-11-16-Git-considers-voting-to-determine-its-LLM-policy.jpg
image_alt: "개발자들이 모니터를 보며 투표와 코드 작성에 대해 논의하는 모습을 담은 일러스트"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "기술이 급변할수록 규칙을 정하는 방식 또한 민주적이고 투명해야 합니다. Git의 이번 시도는오픈소스 커뮤니티가 AI 시대를 항해하는 중요한 이정표가 될 것입니다."
quiz:
  - question: "Git이 현재 검토 중인 LLM 정책 결정 방식은 무엇인가요?"
    choices: ["최고 경영진의 단독 결정", "투표(Voting) 프로세스", "자동화된 AI 알고리즘 판정"]
    answer: 1
    explanation: "Git은 대규모 언어 모델(LLM)과 관련된 정책을 결정하기 위해 투표 방식을 고려하고 있습니다."
  - question: "일부 오픈소스 저장소(예: yt-dlp)에서 개발자들이 준수해야 하는 대표적인 정책 규정은 무엇이 있나요?"
    choices: ["NO AI / NO LLM POLICY", "모든 코드 AI 자동 생성", "상업적 이용 전면 금지"]
    answer: 0
    explanation: "일부 오픈소스 프로젝트에서는 기여 시 'NO AI / NO LLM POLICY'를 확인하고 준수하도록 요구하고 있습니다."
  - question: "오픈소스 생태계에서 정책과 가치를 수립할 때 중요한 이유는 무엇인가요?"
    choices: ["소프트웨어 빌드 속도를 높이기 위해", "사회적 및 기술적 변화 속에서 적절한 방향성을 찾기 위해", "서버 비용을 절감하기 위해"]
    answer: 1
    explanation: "사회와 기술 환경이 변화함에 따라 적절한 정책과 가치를 체계적으로 탐색하고 식별해야 합니다."
lang: ko
ref: 2026-11-16-Git-considers-voting-to-determine-its-LLM-policy
audio: 2026-11-16-Git-considers-voting-to-determine-its-LLM-policy.mp3
permalink: /2026/11/16/Git-considers-voting-to-determine-its-LLM-policy/
---

상상해보세요. 전 세계 수천만 명의 개발자가 매일 사용하는 핵심 도구에서, 인공지능(AI)을 코드 작성에 어떻게 써야 할지 규칙을 정해야 합니다. 이 중요한 결정을 소수의 관리자가 밀실에서 내리는 대신, 커뮤니티 전체의 '투표'로 결정하려면 어떻게 해야 할까요? 최근 전 세계 개발자 사회에서 주목받는 흥미로운 움직임이 있습니다. 버전 관리 시스템의 표준인 Git이 대규모 언어 모델(LLM, Large Language Model, 방대한 텍스트를 학습해 사람처럼 글을 쓰고 코드를 작성하는 AI 기술)과 관련된 정책을 수립하기 위해 투표 방식을 검토하고 나섰습니다 [[Source 1](https://lwn.net/SubscriberLink/1104195/1193ea577aaef643/), [Source 8](https://lwn.net/)].

---

## 이게 왜 중요한가요?

소프트웨어 개발 세상에서 'Git'은 마치 건물의 설계도를 관리하는 공인된 기록소와 같습니다. 누구나 이 기록소를 통해 코드를 고치고, 새로운 기능을 더하고, 전 세계 사람들과 협업합니다. 컴퓨터 과학이나 코딩을 배우는 사람이면 누구나 반드시 알아야 하는 필수 기초 지식이지요 [[Source 2](https://www.youtube.com/watch?v=Yi5Y2_r0t9Y)]. 비유하자면, 전 세계 수많은 요리사들이 하나의 거대한 레시피 북을 함께 고쳐 나갈 때 그 수정 이력을 한 치의 오차도 없이 기록하고 관리하는 '국민 도서관'과 같습니다.

그런데 최근 몇 년 새 생성형 AI가 폭발적으로 성장하면서 전 세계 개발 현장은 큰 혼란에 빠졌습니다. AI가 짜준 코드를 그대로 가져다 써도 되는지, AI가 만든 코드에 저작권 문제는 없는지, 혹은 프로젝트 기여 과정에서 AI 사용을 어디까지 허용해야 할지에 대한 명확한 기준이 없었기 때문입니다. 실제로 일부 오픈소스 프로젝트(예컨대 동영상 다운로드 도구로 유명한 yt-dlp 등)에서는 기여자들이 코드나 이슈를 올릴 때 "나는 AI 사용 정책(NO AI / NO LLM POLICY)을 읽었으며 이를 위반 시 저장소에서 차단될 수 있음을 이해한다"는 체크리스트를 확인하도록 요구하고 있기도 합니다 [[Source 3](https://github.com/yt-dlp/yt-dlp/issues/17585)]. 

이러한 상황에서 Git 같은 핵심 인프라 프로젝트가 AI 정책을 정하기 위해 '투표'라는 민주적 절차를 꺼내 들었다는 것은, 앞으로 수많은 오픈소스 프로젝트가 AI 시대의 규칙을 만들어갈 표준적인 선례가 될 수 있음을 의미합니다 [[Source 1](https://lwn.net/SubscriberLink/1104195/1193ea577aaef643/), [Source 8](https://lwn.net/)].

---

## 쉽게 이해하기: 규칙을 정하는 민주적 실험

이렇게 비유해보겠습니다. 아파트 단지에서 주민들이 모여 반려동물 사육 가이드라인을 만든다고 상상해 보세요. 어떤 사람은 반려동물을 전면 환영하고, 어떤 사람은 엄격한 제한을 원합니다. 이때 관리사무소장이 독단적으로 규칙을 정하면 주민들의 반발이 생기겠지요. 대신 모든 가구가 참여하는 투표를 통해 규칙을 정한다면, 그 결과에 대해 누구나 수긍하기 쉽습니다.

Git이 하려는 것도 이와 비슷합니다. 기술의 발전 속도가 너무 빠르고 입장이 엇갈릴 때, AI가 가져올 정치적·윤리적 영향력이나 편향성 문제에 대해 사회 구성원들이 어떻게 합의를 도출해야 할지 고민하는 과정입니다 [[Source 5](https://arxiv.org/pdf/2410.24190)]. 오픈소스 생태계는 원래부터 자발적인 참여와 토론으로 발전해 왔지만, AI라는 거대한 파도 앞에서 커뮤니티의 의사를 투명하게 묻고 결정하는 제도적 장치(투표 프로세스)를 진지하게 테이블 위에 올린 것입니다 [[Source 1](https://lwn.net/SubscriberLink/1104195/1193ea577aaef643/), [Source 8](https://lwn.net/)].

더 넓은 시각에서 보면, 이는 민주주의 사회가 새로운 기술 앞에서 적절한 정책과 가치를 찾아가는 과정과 정확히 닮아 있습니다. 사회 구성원들이 다양한 지표를 바탕으로 잠재적 결과를 분석하고 더 나은 방향을 모색해야 하듯, 개발 사회 역시 기술적 변화 속에서 체계적인 의사결정 구조를 실험하고 있는 것입니다 [[Source 15](https://iclr-blogposts.github.io/2025/blog/llm-democracy/)].

---

## 현재 상황: 어디까지 왔을까요?

현재 소프트웨어 개발 생태계는 격변기를 지나고 있습니다. 대형 코드 호스팅 플랫폼들의 정책 변화나 중앙집중형 서비스들에 대한 대안을 고민하는 목소리가 커지는 가운데 [[Source 10](https://dbushell.com/2026/04/29/github-is-sinking/)], 개발 도구의 근간을 이루는 Git 커뮤니티 내부에서도 AI 수용성에 대한 찬반 양론이 존재합니다. 

일각에서는 AI를 활용해 생산성을 극대화해야 한다고 주장하는 반면, 다른 한편에서는 코드의 품질, 라이선스 오염, 보안 리스크 등을 이유로 엄격한 통제나 제한을 요구합니다. 이러한 갈등을 힘으로 찍어 누르거나 모호하게 방치하지 않고, 명확한 투표 절차를 거쳐 공식적인 정책을 수립하겠다는 논의가 본격화된 단계가 바로 지금입니다 [[Source 1](https://lwn.net/SubscriberLink/1104195/1193ea577aaef643/), [Source 8](https://lwn.net/)].

---

## 앞으로 어떻게 될까?

Git이 최종적으로 어떤 투표 방식을 채택하고, 어떤 LLM 정책을 확정할지는 전 세계 오픈소스 커뮤니티의 이목을 집중시키고 있습니다. 만약 투표를 통한 정책 결정이 성공적으로 안착한다면, 다른 수많은 오픈소스 프로젝트들도 유사한 거버넌스 모델을 도입할 가능성이 높습니다. 

개발자들은 앞으로 자신이 기여하는 프로젝트가 AI가 작성한 코드를 어떤 기준으로 심사하고 받아들일지, 투명하게 공개된 규칙 속에서 명확히 알 수 있게 될 것입니다. 기술이 발전할수록 규칙을 만드는 방식 또한 함께 진화해야 한다는 교훈을 Git이 보여주고 있는 셈입니다 [[Source 1](https://lwn.net/SubscriberLink/1104195/1193ea577aaef643/), [Source 8](https://lwn.net/)].

---

## 참고자료

1. [Git considers voting to determine its LLM policy](https://lwn.net/SubscriberLink/1104195/1193ea577aaef643/)
2. [We Need To Stop Lying About Git - YouTube](https://www.youtube.com/watch?v=Yi5Y2_r0t9Y)
3. [ok.ru not downloading any video · Issue #17585 · yt-dlp/yt-dlp · GitHub](https://github.com/yt-dlp/yt-dlp/issues/17585)
4. [Hidden Persuaders: LLMs’ Political Leaning and Their Influence on...](https://arxiv.org/pdf/2410.24190)
5. [Welcome to LWN.net [LWN.net]](https://lwn.net/)
6. [GitHub is sinking – David Bushell – Web Dev (UK)](https://dbushell.com/2026/04/29/github-is-sinking/)
7. [LLMs' Potential Influences on Our Democracy: Challenges and...](https://iclr-blogposts.github.io/2025/blog/llm-democracy/)