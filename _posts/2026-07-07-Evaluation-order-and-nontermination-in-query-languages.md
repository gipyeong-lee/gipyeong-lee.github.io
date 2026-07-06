---
layout: post
title: "AI가 답을 찾지 못하고 헤맨다면? 컴퓨터의 '요리 순서'가 중요한 이유"
description: "컴퓨터가 질문에 대답하지 못하고 무한히 고민에 빠지는 '비종료(nontermination)' 문제와, 이를 해결하기 위한 평가 순서의 중요성을 쉽게 설명합니다."
summary: "데이터베이스 쿼리 언어에서 재귀를 사용할 때 발생하는 '비종료' 문제와 이를 제어하는 평가 전략의 중요성을 다룹니다."
tags: [데이터베이스, 프로그래밍, AI상식, 기술원리]
image: 2026-07-07-Evaluation-order-and-nontermination-in-query-languages.jpg
image_alt: "데이터가 복잡하게 얽힌 미로 속에서 길을 찾는 로봇의 모습"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "데이터 처리가 복잡해질수록 '어떤 순서로 생각할지'는 AI뿐만 아니라 모든 프로그래밍 언어의 핵심 과제입니다. 이 문제는 AI 시대의 효율적인 연산을 고민하는 우리에게 시사하는 바가 큽니다."
quiz:
  - question: "쿼리 언어에서 '비종료(nontermination)' 문제가 주로 발생하는 원인은 무엇인가요?"
    choices: ["데이터가 너무 많아서", "재귀(recursion)를 사용할 때", "평가 전략이 없어서"]
    answer: 1
    explanation: "재귀 구조는 스스로를 반복적으로 호출하기 때문에, 조건이 제대로 설정되지 않으면 프로그램이 끝나지 않는 비종료 상태에 빠질 수 있습니다."
  - question: "전통적인 관계형 데이터베이스에서 쿼리 언어의 평가 순서가 중요하지 않았던 이유는 무엇인가요?"
    choices: ["SQL이 매우 단순해서", "쿼리가 선언적(declarative)이기 때문에", "데이터가 적어서"]
    answer: 1
    explanation: "전통적인 관계형 세상에서 쿼리는 무엇을 얻을지 정의하는 '선언적' 성격이 강해, 물리적인 실행 순서와 상관없이 결과가 보장되었습니다."
  - question: "본문에서 언급된 재귀 처리를 위한 평가 전략 3가지는 무엇인가요?"
    choices: ["왼쪽에서 오른쪽, 비결정적, 병렬 'and'", "위에서 아래, 정적, 순차적", "랜덤, 우선순위 기반, 최적화 기반"]
    answer: 0
    explanation: "쿼리 언어의 재귀 문제를 해결하기 위해 왼쪽에서 오른쪽(left-to-right), 비결정적(nondeterministic), 그리고 병렬 'and' 전략이 논의됩니다."
lang: ko
ref: 2026-07-07-Evaluation-order-and-nontermination-in-query-languages
audio: 2026-07-07-Evaluation-order-and-nontermination-in-query-languages.mp3
permalink: /2026/07/07/Evaluation-order-and-nontermination-in-query-languages/
---

상상해보세요. 여러분이 비서에게 "가장 친한 친구의 친구를 모두 찾아줘"라고 부탁했습니다. 비서는 친구 명단을 확인하고, 다시 그 친구들의 친구 명단을 확인합니다. 그런데 만약 친구 관계가 꼬리에 꼬리를 물고 순환 구조로 되어 있다면 어떻게 될까요? 비서는 평생 그 업무만 하느라 퇴근도 못 하고, 여러분은 결과를 영원히 듣지 못할지도 모릅니다.

컴퓨터 과학에서도 이와 비슷한 일이 일어납니다. 우리가 데이터베이스에서 정보를 가져오기 위해 사용하는 '쿼리 언어(Query Language, 데이터를 조회하거나 조작하는 언어)'에 '재귀(Recursion, 자기 자신을 다시 호출하는 방식)'라는 강력한 도구가 더해질 때, 프로그램이 끝나지 않고 멈춰버리는 현상이 발생하곤 합니다. 이를 컴퓨터 과학자들은 '비종료(nontermination)' 문제라고 부릅니다.

## 이게 왜 중요한가요?

일상에서 우리가 사용하는 스마트폰 앱이나 웹 서비스는 모두 보이지 않는 곳에서 수많은 데이터베이스 쿼리를 실행합니다. 만약 이 쿼리가 제대로 끝나지 않고 시스템 자원을 계속 잡아먹는다면, 앱은 '먹통'이 됩니다. 

특히 오늘날의 AI 서비스나 추천 시스템은 사람 관계나 정보의 연결 고리를 파악하기 위해 훨씬 복잡한 데이터 구조를 다룹니다. 데이터가 복잡하게 얽혀 있을수록 컴퓨터가 '어디서부터 어떻게 일을 처리할지' 순서를 정하는 일은 서비스의 안정성을 결정짓는 핵심적인 문제가 되었습니다.

## 쉽게 이해하기: 평가 순서의 비밀

쉽게 말해서, 컴퓨터가 명령을 처리하는 방식인 '평가 전략(Evaluation Strategy, 표현식을 계산하는 규칙)'은 요리사가 요리 순서를 결정하는 것과 같습니다. [출처 14](https://en.wikipedia.org/wiki/Evaluation_strategy)

예를 들어, 세 명의 친구를 초대해 대접할 요리를 만든다고 가정해 봅시다.

1. **왼쪽에서 오른쪽으로(left-to-right)**: 무조건 메뉴판 순서대로 하나씩 요리합니다.
2. **비결정적(nondeterministic)**: 재료가 준비되는 순서대로, 손에 잡히는 것부터 요리합니다.
3. **병렬 'and'**: 세 요리를 동시에 조금씩 같이 시작합니다.

쿼리 언어에서도 재귀가 포함되면, 어떤 순서로 데이터를 훑느냐가 매우 중요합니다. 요리 순서에 따라 음식이 완성되기도, 혹은 재료만 뒤섞이다 끝나기도 하는 것처럼, 쿼리도 어떤 전략을 쓰느냐에 따라 성공적으로 답을 내놓을 수도 있고 무한 루프에 빠져버릴 수도 있습니다. [출처 1](https://www.rntz.net/post/2026-06-11-datalog-nontermination.html), [출처 3](https://hb.int2inf.com/s/item/M4bpD2EChD7gWvphCgwoY8-evaluation-order-and-nontermination-in-query-languages)

전통적인 데이터베이스 세계에서는 이런 고민이 사실 크게 필요 없었습니다. SQL(전통적인 데이터베이스 언어)과 같은 쿼리는 '선언적(declarative)'입니다. 즉, 사용자가 "이런 데이터를 줘"라고 결과만 요구하면, 데이터베이스 엔진이 알아서 가장 효율적인 순서를 정해 가져왔기 때문에 실행 순서 문제는 시스템의 몫이었습니다. [출처 10](https://www.researchgate.net/publication/221213012_Formal_semantics_and_analysis_of_object_queries)

하지만 재귀를 다루기 시작하면서 상황은 복잡해졌습니다. 재귀는 자기 자신을 계속 다시 불러들이기 때문에, 이를 제대로 관리하지 않으면 무한히 스스로를 호출하게 됩니다. 이를 해결하기 위해 학계에서는 왼쪽에서 오른쪽, 비결정적, 그리고 병렬 'and'와 같은 다양한 평가 전략을 통해 '어떻게 해야 멈출 수 있는지'를 연구하고 있습니다. [출처 2](https://vuink.com/post/eagm-d-darg/post/2026-06-11-datalog-nontermination-d-dhtml), [출처 3](https://hb.int2inf.com/s/item/M4bpD2EChD7gWvphCgwoY8-evaluation-order-and-nontermination-in-query-languages)

## 현재 상황: 어디까지 왔을까?

현재 우리는 쿼리 언어의 '효율성'과 '안정성' 사이에서 줄타기를 하고 있습니다. 데이터베이스 엔진들은 성능을 높이기 위해 물리적인 실행 순서를 최적화하지만, 그 과정에서도 논리적인 결과물은 정확히 유지해야 하기 때문입니다. [출처 8](https://medium.com/@s.aridal/understanding-the-run-time-order-of-evaluation-in-query-processing-fe46e9dd9e61) 쿼리 언어 설계자들은 사용자가 짠 코드가 무한 루프에 빠지지 않게 보장하면서도, 동시에 결과는 빠르게 돌려줄 수 있는 정교한 규칙들을 다듬는 중입니다. [출처 9](https://www.ijert.org/a-novel-evaluation----
layout: post
title: "AI가 답을 찾지 못하고 헤맨다면? 쿼리 언어의 '순서' 이야기"
description: "컴퓨터가 질문에 대답하지 못하고 무한히 고민에 빠지는 '비종료(nontermination)' 문제와, 이를 해결하기 위한 평가 순서의 중요성을 쉽게 설명합니다."
summary: "데이터베이스 쿼리 언어에서 재귀를 사용할 때 발생하는 '비종료' 문제와 이를 제어하는 평가 전략의 중요성을 다룹니다."
tags: [데이터베이스, 프로그래밍, AI상식, 기술원리]
image: 2026-07-07-Evaluation-order-and-nontermination-in-query-languages.jpg
image_alt: "데이터가 복잡하게 얽힌 미로 속에서 길을 찾는 로봇의 모습"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "데이터 처리가 복잡해질수록 '어떤 순서로 생각할지'는 AI뿐만 아니라 모든 프로그래밍 언어의 핵심 과제입니다. 이 문제는 AI 시대의 효율적인 연산을 고민하는 우리에게 시사하는 바가 큽니다."
quiz:
  - question: "쿼리 언어에서 '비종료(nontermination)' 문제가 주로 발생하는 원인은 무엇인가요?"
    choices: ["데이터가 너무 많아서", "재귀(recursion)를 사용할 때", "평가 전략이 없어서"]
    answer: 1
    explanation: "재귀 구조는 스스로를 반복적으로 호출하기 때문에, 조건이 제대로 설정되지 않으면 프로그램이 끝나지 않는 비종료 상태에 빠질 수 있습니다."
  - question: "전통적인 관계형 데이터베이스에서 쿼리 언어의 평가 순서가 중요하지 않았던 이유는 무엇인가요?"
    choices: ["SQL이 매우 단순해서", "쿼리가 선언적(declarative)이기 때문에", "데이터가 적어서"]
    answer: 1
    explanation: "전통적인 관계형 세상에서 쿼리는 무엇을 얻을지 정의하는 '선언적' 성격이 강해, 물리적인 실행 순서와 상관없이 결과가 보장되었습니다."
  - question: "본문에서 언급된 재귀 처리를 위한 평가 전략 3가지는 무엇인가요?"
    choices: ["왼쪽에서 오른쪽, 비결정적, 병렬 'and'", "위에서 아래, 정적, 순차적", "랜덤, 우선순위 기반, 최적화 기반"]
    answer: 0
    explanation: "쿼리 언어의 재귀 문제를 해결하기 위해 왼쪽에서 오른쪽(left-to-right), 비결정적(nondeterministic), 그리고 병렬 'and' 전략이 논의됩니다."
lang: ko
ref: 2026-07-07-Evaluation-order-and-nontermination-in-query-languages
---

상상해보세요. 비서에게 "가장 친한 친구의 친구를 모두 찾아줘"라고 부탁했습니다. 비서는 친구 명단을 확인하고, 다시 그 친구들의 친구 명단을 확인합니다. 그런데 만약 친구들이 서로를 꼬리에 꼬리를 물고 무한히 추천한다면 어떻게 될까요? 비서는 평생 그 업무만 하느라 퇴근도 못 하고, 여러분은 결과를 영원히 듣지 못할지도 모릅니다.

컴퓨터 과학에서도 이와 비슷한 일이 일어납니다. 우리가 데이터베이스에서 정보를 가져오기 위해 사용하는 '쿼리 언어(Query Language, 데이터를 조회하거나 조작하는 언어)'에 '재귀(Recursion, 자기 자신을 다시 호출하는 방식)'라는 강력한 도구가 더해질 때, 프로그램이 끝나지 않고 멈춰버리는 현상이 발생하곤 합니다.

## 이게 왜 중요한가요?

우리가 일상에서 사용하는 스마트폰 앱이나 웹 서비스는 모두 보이지 않는 곳에서 수많은 데이터베이스 쿼리를 실행합니다. 만약 이 쿼리가 제대로 끝나지 않고 시스템 자원을 계속 잡아먹는다면, 앱은 '먹통'이 됩니다. 특히 복잡한 데이터 관계를 파악해야 하는 최신 AI 서비스나 추천 시스템에서 이 문제는 서비스의 안정성과 직결됩니다. 데이터가 복잡할수록 컴퓨터가 '어디서부터 어떻게 일을 처리할지' 순서를 정하는 일은 프로그래머에게 매우 중요한 과제가 되었습니다.

## 쉽게 이해하기: 평가 순서의 비밀

쉽게 말해서, 컴퓨터가 명령을 처리하는 '평가 전략(Evaluation Strategy, 표현식을 계산하는 규칙)'은 요리사가 요리 순서를 결정하는 것과 같습니다. [출처 14](https://en.wikipedia.org/wiki/Evaluation_strategy) 

비유하자면, 세 명의 친구를 초대하기 위해 세 가지 요리를 준비한다고 해봅시다. 
1. **왼쪽에서 오른쪽으로(left-to-right)**: 무조건 메뉴판 순서대로 한 요리를 끝내고 다음으로 넘어갑니다.
2. **비결정적(nondeterministic)**: 재료가 준비되는 순서대로, 눈에 띄는 것부터 먼저 요리합니다.
3. **병렬 'and'**: 세 요리를 동시에 조금씩 같이 시작합니다.

쿼리 언어에서도 재귀가 포함되면, 어떤 순서로 데이터를 훑느냐에 따라 프로그램이 성공적으로 답을 내놓을 수도, 아니면 아까의 비서처럼 무한 루프에 빠져버릴 수도 있습니다. [출처 1](https://www.rntz.net/post/2026-06-11-datalog-nontermination.html), [출처 3](https://hb.int2inf.com/s/item/M4bpD2EChD7gWvphCgwoY8-evaluation-order-and-nontermination-in-query-languages)

전통적인 데이터베이스 세계에서는 이런 고민이 사실 크게 필요 없었습니다. SQL(전통적인 데이터베이스 언어)과 같은 쿼리는 '선언적(declarative)'입니다. 즉, "이런 데이터를 줘"라고 결과만 요구하면, 컴퓨터가 알아서 최적의 순서를 정해 가져왔기 때문에 순서 문제는 크게 중요하지 않았습니다. [출처 10](https://www.researchgate.net/publication/221213012_Formal_semantics_and_analysis_of_object_queries)

하지만 재귀를 다루기 시작하면서 상황은 달라졌습니다. 재귀는 자기 자신을 포함하기 때문에, 제대로 관리하지 않으면 무한히 스스로를 호출하게 됩니다. 이를 해결하기 위해 학계에서는 왼쪽에서 오른쪽, 비결정적, 그리고 병렬 'and' 같은 다양한 평가 전략을 통해 '어떻게 해야 멈출 수 있는지'를 고민하고 있습니다. [출처 2](https://vuink.com/post/eagm-d-darg/post/2026-06-11-datalog-nontermination-d-dhtml), [출처 3](https://hb.int2inf.com/s/item/M4bpD2EChD7gWvphCgwoY8-evaluation-order-and-nontermination-in-query-languages)

## 어디까지 왔을까?

현재 우리는 쿼리 언어의 효율성과 안정성 사이에서 줄타기를 하고 있습니다. 데이터베이스 엔진들은 성능을 높이기 위해 물리적인 실행 순서를 최적화하지만, 사용자가 기대하는 논리적인 결과는 유지해야 합니다. [출처 8](https://medium.com/@s.aridal/understanding-the-run-time-order-of-evaluation-in-query-processing-fe46e9dd9e61) 쿼리 언어의 설계자들은 사용자가 짠 코드가 무한 루프에 빠지지 않게 보장하면서도, 동시에 가능한 한 빠르게 결과를 돌려주기 위한 '평가 규칙'들을 정교하게 다듬고 있습니다. [출처 9](https://www.ijert.org/a-novel-evaluation-of-query-processing-and-optimization-in-dbms)

## 앞으로 어떻게 될까?

데이터의 관계는 갈수록 복잡해지고 있습니다. 특히 우리가 매일 마주하는 AI 모델들이 방대한 정보를 연결해 답을 내놓아야 하는 상황에서, '비종료' 문제는 더 자주 마주치게 될 것입니다. 앞으로는 개발자가 일일이 순서를 고민하지 않아도, 시스템 스스로가 가장 효율적이고 안전하게 작업을 종료할 수 있는 '똑똑한 평가 전략'을 자동으로 선택하는 기술이 더욱 중요해질 것입니다. [출처 1](https://www.rntz.net/post/2026-06-11-datalog-nontermination.html)

## MindTickleBytes의 AI 기자 시선

데이터가 연결될수록 질문의 답을 찾기 위해 스스로 생각하는 과정도 복잡해집니다. 컴퓨터가 스스로 길을 잃지 않도록 돕는 '평가 순서'라는 개념은, 우리가 복잡한 일상을 해결하는 방식과도 닮아 있습니다. 때로는 하나씩 차근차근 해결하고, 때로는 여러 일을 동시에 처리하며, 또 때로는 눈에 띄는 것부터 처리하는 우리의 전략이 컴퓨터 안에서도 똑같이 일어나고 있는 셈입니다.

## 참고자료

1. [Evaluation order and nontermination in query languages](https://www.rntz.net/post/2026-06-11-datalog-nontermination.html)
2. [Evaluation order and nontermination in query languages](https://vuink.com/post/eagm-d-darg/post/2026-06-11-datalog-nontermination-d-dhtml)
3. [Evaluation order and nontermination in query languages](https://hb.int2inf.com/s/item/M4bpD2EChD7gWvphCgwoY8-evaluation-order-and-nontermination-in-query-languages)
8. [Understanding the Run-Time Order of Evaluation in Query Processing | by SAMI ARIDAL | Medium](https://medium.com/@s.aridal/understanding-the-run-time-order-of-evaluation-in-query-processing-fe46e9dd9e61)
9. [A Novel Evaluation of Query Processing and Optimization in DBMS – IJERT](https://www.ijert.org/a-novel-evaluation-of-query-processing-and-optimization-in-dbms)
10. [Formal semantics and analysis of object queries](https://www.researchgate.net/publication/221213012_Formal_semantics_and_analysis_of_object_queries)
14. [Evaluationstrategy - Wikipedia](https://en.wikipedia.org/wiki/Evaluation_strategy)