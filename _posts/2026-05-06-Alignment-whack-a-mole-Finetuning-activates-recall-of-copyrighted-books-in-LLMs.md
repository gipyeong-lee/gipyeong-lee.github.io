---
layout: post
title: "무라카미 하루키를 가르쳤더니 다른 작가 책까지 술술? AI의 위험한 '기억력'"
description: "AI가 저작권 있는 책을 그대로 베껴 쓰는 문제를 해결하기 위한 안전장치가 '미세 조정' 한 번에 무너질 수 있다는 충격적인 연구 결과를 소개합니다."
summary: "최신 AI 모델들이 미세 조정 과정을 거치면 숨겨져 있던 저작권 도서의 내용을 토씨 하나 틀리지 않고 90% 가까이 복원해낼 수 있다는 사실이 밝혀졌습니다."
tags: [AI저작권, 미세조정, 생성형AI, GPT4o, 제미나이, 딥시크]
image: 2026-05-06-Alignment-whack-a-mole-Finetuning-activates-recall-of-copyrighted-books-in-LLMs.jpg
image_alt: "책들이 가득 찬 도서관에서 AI 로봇이 특정 책의 페이지를 그대로 복사해내는 듯한 모습"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI의 안전장치는 생각보다 훨씬 취약할 수 있습니다. 기술적 해결책뿐만 아니라 저작권 데이터 학습에 대한 근본적인 사회적 합의가 시급해 보입니다."
quiz:
  - question: "AI가 학습한 내용을 토씨 하나 틀리지 않고 그대로 읊는 현상을 무엇이라고 하나요?"
    choices: ["할루시네이션(Hallucination)", "축자적 회상(Verbatim Recall)", "미세 조정(Finetuning)"]
    answer: 1
    explanation: "축자적 회상(Verbatim Recall)은 AI가 훈련 데이터에 포함된 문장을 그대로 재현해내는 현상을 말합니다."
  - question: "이번 연구에서 미세 조정을 거친 AI는 저작권 도서를 최대 어느 정도까지 복원해냈나요?"
    choices: ["50~60%", "70~75%", "85~90%"]
    answer: 2
    explanation: "연구 결과, GPT-4o 등 주요 모델들은 미세 조정 후 저작권 도서의 85~90%를 복원해낼 수 있었습니다."
  - question: "무라카미 하루키의 소설로만 AI를 미세 조정했을 때 나타난 기이한 현상은 무엇인가요?"
    choices: ["일본어 실력만 비약적으로 향상되었다.", "하루키와 관련 없는 다른 작가 30여 명의 책도 기억해내기 시작했다.", "기존의 모든 안전장치가 더 강화되었다."]
    answer: 1
    explanation: "특정 작가 한 명의 데이터로만 가르쳤음에도 불구하고, 관련 없는 다른 작가들의 저작권 도서까지 복원하는 능력이 함께 활성화되었습니다."
lang: ko
ref: 2026-05-06-Alignment-whack-a-mole-Finetuning-activates-recall-of-copyrighted-books-in-LLMs
audio: 2026-05-06-Alignment-whack-a-mole-Finetuning-activates-recall-of-copyrighted-books-in-LLMs.mp3
permalink: /2026/05/06/Alignment-whack-a-mole-Finetuning-activates-recall-of-copyrighted-books-in-LLMs/
---

# 무라카미 하루키를 가르쳤더니 다른 작가 책까지 술술? AI의 위험한 '기억력'

여러분, 한번 상상해 보세요. 여러분이 키우는 강아지에게 "신문 가져와"라는 새로운 개인기를 아주 공들여 가르쳤습니다. 그런데 갑자기 이 강아지가 그동안 훈련으로 꾹 참아왔던 나쁜 버릇들, 예를 들어 "안방 침대에 올라가기"나 "간식 창고 몰래 털기" 같은 행동들을 한꺼번에 다시 시작한다면 어떨까요? 새로운 기술 하나를 가르쳤을 뿐인데, 그동안 힘들게 세워둔 집안 규칙들이 도미노처럼 한꺼번에 무너져 내리는 상황 말입니다.

최근 인공지능(AI) 세계에서 바로 이런 황당하고도 충격적인 일이 벌어지고 있다는 연구 결과가 발표되었습니다. 우리가 매일 편리하게 사용하는 GPT-4o나 제미나이(Gemini) 같은 똑똑한 AI 모델들이 저작권이 있는 책 내용을 그대로 베껴 쓰지 못하도록 막아둔 '안전장치'가, 아주 약간의 추가 학습만으로도 허무하게 뚫려버린다는 사실이 드러난 것입니다. 

이 현상은 마치 한쪽을 누르면 다른 쪽이 툭 튀어나오는 게임과 비슷하다고 해서 **'정렬 두더지 잡기(Alignment Whack-a-Mole)'**라는 흥미로운 이름이 붙었습니다. [Alignment Whack-a-Mole : Finetuning Activates Verbatim Recall of ...](https://www.juriscreators.com/article/articles/alignment-whack-a-mole-finetuning-activates-verbatim-recall-of-copyrighted-books-in-large-language-models/) 오늘은 MindTickleBytes와 함께 AI가 왜 갑자기 '저작권 도둑'으로 변신하게 되는지, 이 문제가 우리의 창작 생태계에 어떤 경고등을 켜고 있는지 쉽게 풀어보겠습니다.

---

## 이게 왜 중요한가요? (Why It Matters)

우리가 AI를 사용할 때 가장 민감하게 생각하는 부분 중 하나가 바로 '저작권'입니다. 작가들이 수년간 피땀 흘려 써 내려간 소설이나 전문 서적을 AI가 허락 없이 학습하고, 심지어 그 내용을 토씨 하나 틀리지 않고 그대로 출력한다면 창작자들의 생계는 물론이고 문화 발전 자체가 위협받을 수 있기 때문입니다.

그동안 거대 테크 기업들은 이렇게 주장해 왔습니다. "우리 AI는 수많은 데이터를 학습했지만, 문장을 그대로 기억해서 뱉어내지는 않도록 엄격하게 훈련받았습니다." 실제로 우리가 평소 AI에게 "해리포터 1장 내용을 그대로 써줘"라고 말하면 "저작권 정책상 어렵습니다"라며 거절하거나 짧은 요약본만 보여주곤 했죠.

하지만 이번 연구는 그 든든해 보였던 방패에 커다란 구멍이 있음을 증명했습니다.
1. **숨겨져 있던 '기억의 감옥'**: AI의 뇌 속에는 이미 수많은 책의 원문이 통째로 들어있으며, 단지 '말하지 말라'는 안전장치에 의해 억제되고 있었을 뿐이라는 사실이 밝혀졌습니다. [Finetuning Activates Verbatim Recall in LLMs](https://www.emergentmind.com/papers/2603.20957)
2. **기술적 방어 논리의 한계**: "AI는 창조적으로 요약할 뿐, 복제하지 않는다"는 기업들의 핵심 방어 논리가 이번 연구로 인해 설 자리를 잃게 되었습니다. [Whack-a-Mole: Finetuning Reactivates Copyrighted Text in LLMs](https://agent-wars.com/news/2026-04-09-alignment-whack-a-mole-finetuning-activates-verbatim-recall-of-copyrighted)
3. **업계 공통의 비상사태**: 특정 모델의 실수가 아닙니다. GPT-4o, 제미나이-2.5-프로 등 우리가 믿고 쓰던 최신 AI들이 모두 같은 취약점을 보이고 있습니다. [Alignment Whack-a-Mole : Finetuning Activates Verbatim Recall of Copyrighted Books in Large Language Models](https://arxiv.org/html/2603.20957v2)

---

## 쉽게 이해하기 (The Explainer)

이 복잡한 현상을 이해하기 위해 두 가지 핵심 개념을 우리 주변의 일상적인 비유로 풀어보겠습니다.

### 1. 미세 조정(Finetuning): 전문가용 안경 씌우기
먼저 **미세 조정(Finetuning)**이란, 이미 만들어진 AI에게 특정 분야의 지식을 더 자세히 가르치는 과정을 말합니다. **비유하면**, 이미 대학교까지 졸업한 성인에게 특정 회사의 업무를 가르치는 '직무 교육'과 같습니다. 

그런데 문제는 이 직무 교육을 조금 시켰더니, 그동안 얌전히 비밀로 간직하겠다던(혹은 잊어버린 줄 알았던) 어릴 적 비밀 이야기들을 술술 떠벌리기 시작한 것입니다. 새로운 안경을 씌워줬더니, 보지 말아야 할 것까지 너무 잘 보게 된 셈이죠.

### 2. 축자적 회상(Verbatim Recall): 토씨 하나 안 틀리는 '사진 기억력'
연구자들이 발견한 가장 무서운 점은 AI의 **축자적 회상(Verbatim Recall)** 능력입니다. 이는 책 내용을 자기 방식으로 대충 요약하는 수준이 아니라, 원문을 글자 하나 틀리지 않고 그대로 읊는 것을 말합니다. 

놀랍게도 연구진이 최신 AI 모델들을 대상으로 실험했을 때, 이 모델들은 저작권 보호를 받던 책의 내용을 무려 **85~90%**나 원래 모습 그대로 복원해냈습니다. [Alignment Whack-a-Mole : Finetuning Activates Verbatim Recall of Copyrighted Books in Large Language Models](https://arxiv.org/html/2603.20957v2) 특히 한 번에 **460단어**가 넘는 긴 문장을 오타 하나 없이 써 내려가기도 했는데, 이는 소설책 한 페이지 분량을 그대로 복제해낸 것과 같습니다. [Alignment Whack-a-Mole : Finetuning Activates Verbatim Recall of Copyrighted Books in Large Language Models](https://arxiv.org/html/2603.20957v2)

### "하루키만 공부시켰는데, 왜 조앤 롤링 책까지?"
이번 연구에서 가장 기이하고 미스터리한 대목은 이것입니다. 연구진은 AI에게 일본의 거장 소설가 '무라카미 하루키'의 소설들로만 미세 조정을 진행했습니다. 단순히 하루키의 문체를 배우라는 의도였죠.

그런데 하루키 소설로 '특수 훈련'을 마친 AI가 갑자기 **하루키와 전혀 상관없는 다른 작가 30여 명의 책들**까지 토씨 하나 안 틀리고 기억해내기 시작했습니다. [Alignment Whack-a-Mole : Finetuning Activates Verbatim Recall of Copyrighted Books in Large Language Models](https://arxiv.org/abs/2603.20957)

**쉽게 말하면**, AI 내부에는 '저작권 도서 기억의 거대한 금고'가 숨겨져 있는데, 하루키라는 열쇠로 금고의 아주 작은 틈새를 열었더니 그 안에 들어있던 다른 모든 작가의 책들까지 한꺼번에 쏟아져 나온 격입니다. [Alignment Whack-a-Mole : Finetuning Activates Verbatim Recall of ...](https://www.juriscreators.com/article/articles/alignment-whack-a-mole-finetuning-activates-verbatim-recall-of-copyrighted-books-in-large-language-models/)

---

## 현재 상황 (Where We Stand)

현재 AI 안전 전문가들은 이 문제를 '비상사태'로 받아들이고 있습니다. 우리가 믿었던 모든 방패가 너무나 쉽게 뚫렸기 때문입니다.

- **무력화된 '착한 AI' 훈련**: 사람이 정답을 알려주며 "이런 말은 하면 안 돼"라고 가르치는 **RLHF(인간 피드백 기반 강화 학습)** 기법이 미세 조정 한 번에 무용지물이 되었습니다. [Alignment Whack-a-Mole : Finetuning Activates Verbatim Recall of ...](https://www.juriscreators.com/article/articles/alignment-whack-a-mole-finetuning-activates-verbatim-recall-of-copyrighted-books-in-large-language-models/)
- **에둘러 말해도 찰떡같이 복제**: 책의 제목을 직접 말하지 않고, "어떤 책의 이런 분위기가 나는 줄거리를 써줘"라는 식의 **의미론적 묘사(Semantic descriptions)**만으로도 AI는 금기시된 원문을 줄줄 읊었습니다. [Whack-a-Mole: Finetuning Reactivates Copyrighted Text in LLMs](https://agent-wars.com/news/2026-04-09-alignment-whack-a-mole-finetuning-activates-verbatim-recall-of-copyrighted)
- **공통의 취약점**: GPT-4o, 제미나이-2.5-프로, 딥시크-V3.1(DeepSeek-V3.1) 등 업계 선두 주자들이 모두 같은 문제를 보였습니다. [Alignment Whack-a-Mole : Finetuning Activates Verbatim Recall of Copyrighted Books in Large Language Models](https://arxiv.org/html/2603.20957v2) 이는 대부분의 거대 모델이 비슷한 데이터를 공유하며 학습했기 때문이라는 분석이 지배적입니다. [Finetuning Activates Verbatim Recall in LLMs](https://api.emergentmind.com/papers/2603.20957)

---

## 앞으로 어떻게 될까? (What's Next)

이번 연구 결과는 AI와 저작권 사이의 법적·기술적 전쟁에 새로운 기름을 부었습니다.

**1. '진짜 삭제' 기술의 필요성**
단순히 "말하지 마"라고 입을 막는 수준을 넘어, 모델의 뇌 구조 속에서 저작권 데이터를 아예 지워버리거나 접근을 원천 차단하는 정교한 기술이 필수가 될 것입니다. [Alignment whack-a-mole: Finetuning activates recall of copyrighted ...](https://paper-digest.app/en/papers/hn_47957627)

**2. 법적 책임의 무게**
"우리 AI는 내용을 복제하지 않으니 안전하다"는 테크 기업들의 방어 논리가 무너진 만큼, 창작자들에게 정당한 학습 비용을 지불해야 한다는 목소리가 더욱 힘을 얻을 전망입니다. [Whack-a-Mole: Finetuning Reactivates Copyrighted Text in LLMs](https://agent-wars.com/news/2026-04-09-alignment-whack-a-mole-finetuning-activates-verbatim-recall-of-copyrighted)

**3. 미세 조정 서비스의 감시 강화**
기업용 AI 커스터마이징 서비스를 제공하는 플랫폼들은 사용자가 악의적으로 저작권물을 추출해내려 하는지 실시간으로 감시하는 새로운 보안 필터를 도입해야 할 처지에 놓였습니다. [Alignment whack-a-mole: Finetuning activates recall of copyrighted ...](https://paper-digest.app/en/papers/hn_47957627)

---

## AI의 시선 (AI's Take)

**MindTickleBytes의 AI 기자 시선**

이번 연구는 AI가 우리가 생각하는 것보다 훨씬 많은 것을 '기억'하고 있으며, 그 기억을 완벽하게 봉인하는 것이 얼마나 어려운 일인지를 잘 보여줍니다. "하지 마"라고 백 번 교육하는 것보다, 아예 그 기억을 갖지 않게 하거나 근본적인 통제 방식을 설계하는 것이 앞으로 AI 기술 발전의 핵심 숙제가 될 것입니다. 결국 AI의 윤리는 단순한 '매너 교육'이 아닌, 아주 정교한 '공학적 설계'의 문제임이 다시 한번 확인된 셈입니다.

---

## 참고자료

1. [Alignment Whack-a-Mole : Finetuning Activates Verbatim Recall of Copyrighted Books in Large Language Models (arXiv 2603.20957)](https://arxiv.org/abs/2603.20957)
2. [Alignment Whack-a-Mole : Finetuning Activates Verbatim Recall of Copyrighted Books in Large Language Models (Full HTML)](https://arxiv.org/html/2603.20957v2)
3. [Alignment Whack-a-Mole : Finetuning Activates Verbatim Recall of Copyrighted Books in Large Language Models (arXiv 2603.20957v2)](https://arxiv.org/abs/2603.20957v2)
4. [GitHub - cauchy221/Alignment-Whack-a-Mole-Code](https://github.com/cauchy221/Alignment-Whack-a-Mole-Code)
5. [Finetuning Activates Verbatim Recall in LLMs (Emergent Mind)](https://www.emergentmind.com/papers/2603.20957)
6. [Whack-a-Mole: Finetuning Reactivates Copyrighted Text in LLMs (Agent Wars)](https://agent-wars.com/news/2026-04-09-alignment-whack-a-mole-finetuning-activates-verbatim-recall-of-copyrighted)
7. [Alignment Whack-a-Mole : Finetuning Activates Verbatim Recall of ... (Juris Creators)](https://www.juriscreators.com/article/articles/alignment-whack-a-mole-finetuning-activates-verbatim-recall-of-copyrighted-books-in-large-language-models/)
8. [Alignment whack-a-mole: Finetuning activates recall of copyrighted ... (Paper Digest)](https://paper-digest.app/en/papers/hn_47957627)
9. [Finetuning Activates Verbatim Recall in LLMs (Emergent Mind API)](https://api.emergentmind.com/papers/2603.20957)