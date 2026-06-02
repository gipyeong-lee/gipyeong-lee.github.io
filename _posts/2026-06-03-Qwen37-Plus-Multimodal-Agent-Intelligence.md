---
layout: post
title: "AI가 내 컴퓨터 화면을 보고 대신 일해준다고? 알리바바 Qwen3.7-Plus의 등장"
description: "텍스트만 읽던 AI가 이제 화면을 보고 마우스를 움직입니다. 알리바바가 새롭게 공개한 다중모달 에이전트 Qwen3.7-Plus가 우리의 일하는 방식을 어떻게 바꿀지 아주 쉽게 설명해 드립니다."
summary: "알리바바가 2026년 6월 출시한 Qwen3.7-Plus는 단순한 챗봇을 넘어, 컴퓨터 화면을 보고 스스로 도구를 사용해 복잡한 업무를 처리하는 '멀티모달 에이전트' AI입니다."
tags: [Qwen, 알리바바, 멀티모달, AI에이전트, 인공지능]
image: 2026-06-03-Qwen37-Plus-Multimodal-Agent-Intelligence.jpg
image_alt: "눈과 손이 달린 로봇이 컴퓨터 화면을 보며 업무를 처리하는 모습을 묘사한 일러스트"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "MindTickleBytes의 AI 기자 시선: AI가 단순히 질문에 답하는 것을 넘어, 스스로 화면을 인지하고 도구를 다루는 '실행력'을 갖추기 시작했습니다. 이는 우리가 컴퓨터와 상호작용하는 방식의 근본적인 변화를 예고합니다."
quiz:
  - question: "Qwen3.7-Plus 모델의 가장 큰 특징은 무엇인가요?"
    choices: ["오직 텍스트만 처리할 수 있다", "컴퓨터 화면을 보고 도구를 사용할 수 있는 멀티모달 에이전트이다", "오픈소스로 누구나 무료로 다운로드할 수 있다"]
    answer: 1
    explanation: "Qwen3.7-Plus는 텍스트뿐만 아니라 이미지, 비디오, 컴퓨터 화면을 이해하고 도구를 호출할 수 있는 다중모달 에이전트입니다."
  - question: "Qwen3.7 제품군 중 텍스트 처리 능력에만 집중하여 SWE-Bench Pro에서 높은 점수를 기록한 모델은 무엇인가요?"
    choices: ["Qwen3.7-Mini", "Qwen3.7-Plus", "Qwen3.7-Max"]
    answer: 2
    explanation: "Qwen3.7-Max는 순수 텍스트(pure-text) 기반의 플래그십 모델로 코딩 벤치마크에서 60.6%의 성적을 기록했습니다."
  - question: "Qwen3.7-Plus는 현재 어떤 방식으로 이용할 수 있나요?"
    choices: ["누구나 가중치를 다운로드할 수 있다", "스마트폰 앱으로만 작동한다", "API를 통해서만 접근 가능한 클로즈드 웨이트 모델이다"]
    answer: 2
    explanation: "현재 Qwen3.7-Plus와 Max 모델 모두 가중치가 비공개된(closed-weights) 상태이며 API를 통해서만 이용할 수 있습니다."
lang: ko
ref: 2026-06-03-Qwen37-Plus-Multimodal-Agent-Intelligence
audio: 2026-06-03-Qwen37-Plus-Multimodal-Agent-Intelligence.mp3
permalink: /2026/06/03/Qwen37-Plus-Multimodal-Agent-Intelligence/
---

상상해보세요. 아침에 출근해서 컴퓨터를 켜고 AI에게 이렇게 말합니다. "어제 온 이메일 중에 영수증이 첨부된 것만 찾아서 엑셀 파일로 정리해 줘." 지금까지의 AI라면 엑셀 함수를 어떻게 쓰는지 친절하게 알려주거나 보고서 양식을 글로 적어주는 데 그쳤을 겁니다. 결국 키보드를 두드리고 마우스를 클릭하며 일을 끝내는 것은 우리의 몫이었죠. 

하지만 이제는 다릅니다. AI가 직접 여러분의 이메일 창을 열고, 영수증 이미지를 눈으로 읽어낸 뒤, 엑셀 프로그램을 실행해 데이터를 하나하나 입력합니다. 마치 내 컴퓨터 모니터를 똑같이 바라보며 마우스를 대신 움직여주는 '투명한 비서'가 생긴 셈입니다. 

이 공상과학 같은 이야기가 현실로 다가왔습니다. 알리바바(Alibaba)가 2026년 6월 1일 새롭게 출시한 AI 모델 **Qwen3.7-Plus** 덕분입니다 [[Qwen3.7Plus vs Qwen3.7Max in 2026: Multimodal Agent or...](https://ofox.ai/blog/qwen-3-7-plus-vs-qwen-3-7-max-real-benchmark-2026/)]. 이 AI는 단순한 '똑똑한 챗봇'을 넘어, 스스로 컴퓨터 화면을 보고 마우스를 움직이듯 작업하는 진정한 의미의 '디지털 인턴' 역할을 해냅니다.

## 이게 왜 중요한가요?

지금까지 우리가 쓰던 챗봇 AI는 마치 유능하지만 자리에서 절대 일어나지 않는 '도서관 사서'와 같았습니다. 궁금한 것을 물어보면 엄청난 양의 책을 뒤져서 훌륭한 정답을 찾아주지만, 내 대신 보고서를 완성해서 상사에게 이메일로 보내주지는 않습니다. 

반면 Qwen3.7-Plus는 단순한 대화형 AI가 아니라 **에이전트(Agent, 주도적으로 목표를 달성하기 위해 행동을 수행하는 프로그램)** 모델입니다 [[Qwen3.7-Plus: Multimodal Agent Intelligence — LLM... | explainx.ai](https://explainx.ai/llms/qwen3-7-plus-multimodal-agent-intelligence)]. 쉽게 말해서, AI에게 그저 질문에 답하는 입을 넘어서, 소프트웨어 도구를 직접 사용하고 코드를 작성하며 생산성 작업의 전체 흐름을 주도할 수 있는 '손'과 '판단력'을 쥐여준 것입니다 [[Qwen3.7-Plus - Qwen Cloud](https://www.qwencloud.com/models/qwen3.7-plus)]. 

이는 우리가 매일 모니터 앞에서 보내는 시간의 의미가 근본적으로 바뀔 수 있음을 뜻합니다. 코딩, 데이터 분석, 복잡한 웹 검색과 같은 여러 단계의 작업을 사람이 하나하나 지시하지 않아도 됩니다. AI가 알아서 웹 브라우저를 열고 필요한 프로그램을 번갈아 가며 실행해 알아서 업무를 처리할 수 있기 때문입니다 [[Qwen3.7 Plus API | AIML API](https://aimlapi.com/models/qwen3-7-plus)].

## 쉽게 이해하기: 눈과 손을 얻은 AI

Qwen3.7-Plus의 놀라운 능력을 온전히 이해하려면 **멀티모달(Multimodal, 텍스트뿐만 아니라 이미지, 소리 등 다양한 형태의 데이터를 동시에 이해하는 기술)**이라는 단어의 의미를 알아야 합니다. 모달(Modal)은 데이터를 받아들이는 일종의 '감각'을 뜻합니다. 글씨만 읽던 기존의 AI에 이미지나 비디오, 심지어 컴퓨터 화면의 그래픽 인터페이스(GUI, 아이콘이나 메뉴 창처럼 화면에 보이는 시각적 요소들)까지 한눈에 파악할 수 있는 '시각' 능력을 대폭 추가한 것이 바로 멀티모달입니다 [[Qwen3.7-Plus Review: Alibaba's GUI Agent, Tested](https://www.buildfastwithai.com/blogs/qwen-3-7-plus-multimodal-agent-review-2026)].

조금 더 일상적인 상황으로 비유하면 이렇습니다. 기존의 텍스트 기반 AI는 오직 '전화 통화'로만 일하는 똑똑한 직장 동료였습니다. 내가 화면에 띄워놓은 표나 이미지를 하나하나 말로 길고 자세하게 설명해 줘야만 상황을 파악하고 조언을 해줄 수 있었죠. 답답해서 차라리 혼자 하고 마는 경우가 많았습니다. 

하지만 Qwen3.7-Plus는 아예 여러분 옆에 나란히 앉아서 컴퓨터 모니터를 함께 바라보는 동료입니다. 화면 구석의 '저장' 아이콘이 어디에 있는지, 복잡한 엑셀 표에 어떤 숫자가 적혀 있는지 직접 '보고' 직관적으로 이해할 수 있습니다 [[Qwen3.7 Plus model | NanoGPT](https://nano-gpt.com/models/text/qwen3.7-plus)].

알리바바의 연구진은 텍스트를 논리적으로 처리하는 튼튼한 기본 뼈대 위에 이 시각 능력을 대폭 업그레이드했습니다. 이를 통해 상황을 시각적으로 파악하고 다음 행동을 언어로 추론하는 과정을 하나의 매끄러운 작업 흐름으로 통합해 냈습니다 [[Research - Qwen](https://qwen.ai/research/)]. 그 결과, 단순히 이미지가 무엇인지 맞히는 것을 넘어서 "이 화면을 보니 다음엔 이 버튼을 클릭하고 저 도구를 실행해야겠다"라고 스스로 도구 호출(Tool invocation)을 결정하는 놀라운 수준에 도달한 것입니다 [[Qwen3.7-Plus 发布：多模态 Agent 该怎么测 - HotAI - 博客园](https://www.cnblogs.com/hotai/p/20272234/qwen3-7-plus-multimodal-agent)].

## 현재 상황: 플래그십 텍스트 AI와 멀티모달 에이전트의 투트랙

알리바바는 2026년 5월 20일부터 21일까지 열린 알리바바 클라우드 서밋에서 이 강력한 Qwen3.7 제품군을 처음으로 공식 무대에 올렸습니다 [[Qwen 3.7 Complete Guide: Alibaba's Strongest AI Model Yet (2026)](https://www.aimadetools.com/blog/qwen-3-7-complete-guide/)]. 정식 행사 전날인 5월 19일에는 큐원 챗(Qwen Chat)을 통해 프리뷰 버전으로 먼저 슬쩍 모습을 드러내어 사람들을 깜짝 놀라게 하기도 했죠 [[Qwen 3.7 Review: Alibaba's New Flagship Ranks #1 in China ...](https://renovateqr.com/blog/qwen-3-7-review-benchmarks-2026)]. 가장 흥미로운 관전 포인트는 알리바바가 각기 다른 장기를 가진 두 가지의 주력(플래그십) 모델을 동시에 내놓았다는 점입니다.

첫 번째 선수는 오직 '글'로 하는 논리적 사고에 모든 지능을 집중한 **Qwen3.7-Max**입니다. 이 모델은 순수 텍스트(pure-text) 처리에만 극도로 특화되어 있습니다. 소프트웨어 엔지니어링 능력을 평가하는 아주 까다롭고 권위 있는 시험인 SWE-Bench Pro에서 무려 60.6%라는 놀라운 정답률을 기록했습니다. 이는 인간 프로그래머와 견주어도 손색없는 최고 수준의 추론 능력을 증명한 셈입니다 [[Qwen3.7Plus vs Qwen3.7Max in 2026: Multimodal Agent or...](https://ofox.ai/blog/qwen-3-7-plus-vs-qwen-3-7-max-real-benchmark-2026/)]. 

두 번째 선수가 바로 오늘 집중적으로 살펴본 **Qwen3.7-Plus**입니다. 이 모델은 Max가 가진 튼튼한 텍스트 논리력(text backbone)을 그대로 물려받으면서도, 이미지나 비디오, 그리고 시각적인 컴퓨터 화면을 읽어내는(vision-language) 능력을 대폭 끌어올렸습니다. 연구실의 시험 문제를 푸는 대신, 현실 세계의 복잡한 업무를 직접 행동으로 수행하는 데 초점을 맞춘 아주 '균형 잡힌' 다재다능한 모델입니다 [[Qwen3.7 Plus: The Balanced Multimodal Flagship | Qwen 3.7](https://qwen3lm.com/qwen3.7-plus/)]. 

그렇다면 우리는 이 똑똑한 AI 비서를 어떻게 써볼 수 있을까요? 현재 이 모델들은 알리바바의 모델 스튜디오(Model Studio)와 바이리안(Bailian)이라는 플랫폼 등을 통해 만나볼 수 있습니다 [[Qwen3.7-Plus: Multimodal Agent on Bailian - kiadev.net](https://www.kiadev.net/news/2026-06-02-qwen3-7-plus-bailian-agent)]. 누구나 컴퓨터에 코드를 다운로드해 마음대로 설치할 수 있는 '오픈소스' 형태는 아니며, API(프로그램 간에 데이터를 주고받는 통신 도구)를 통해서만 조심스럽게 접근할 수 있는 가중치 비공개(closed-weights) 방식으로 서비스되고 있습니다 [[Qwen 3.7 Complete Guide: Alibaba's Strongest AI Model Yet (2026)](https://www.aimadetools.com/blog/qwen-3-7-complete-guide/)].

## 앞으로 어떻게 될까?

Qwen3.7-Plus의 화려한 등장은 우리에게 중요한 메시지를 던집니다. 전 세계의 대규모 언어 모델(LLM) 기술이 화면 너머에서 텍스트로 대화를 나누는 수준을 훌쩍 넘어서고 있다는 사실입니다. 이제 AI는 물리적인 현실 세계나 컴퓨터 운영체제 환경과 직접 부딪히며 행동하는 '체화된 지능(Embodied intelligence, 신체나 도구를 통해 환경과 상호작용하며 문제를 해결하는 인공지능)'과 고도화된 에이전트(advanced agents) 시스템을 향해 무서운 속도로 진화하고 있습니다 [[Multimodal Agent Receives Major Upgrade! Alibaba Officially ...](https://news.aibase.com/news/28533)]. 

과거에는 AI가 만들어준 코드를 복사해서 붙여넣고 실행하는 번거로움이 사람의 몫이었다면, 이제 AI 모델들은 사람의 개입 없이 스스로 작업 계획을 세우고, 코드를 작성해 바로 실행하며(self-programming), 에러가 나면 멈추지 않고 스스로 원인을 찾아 끊임없이 고쳐나가는(autonomous iteration) 진짜 '행동력'의 영역에 들어섰습니다 [[Alibaba Unveils Qwen3.7-Plus Multimodal AI Agent Model](https://en.tmtpost.com/news/8011149)]. 

머지않은 미래에 우리의 업무 지시 방식은 완전히 달라질 것입니다. AI에게 "이 영어 문서를 한국어로 번역해 줘"라고 단편적인 결과물만 요구하는 시대는 저물 것입니다. 대신, "이번 신제품 프로젝트의 경쟁사 시장 조사부터 시작해서, 데이터를 분석하고 최종 발표용 PPT 보고서 작성까지 모두 알아서 처리해 줘"라며 거대한 업무의 권한을 통째로 위임하는 짜릿하고 새로운 시대를 맞이하게 될 것입니다.

---

> **MindTickleBytes의 AI 기자 시선**: 
> 눈과 손을 가진 멀티모달 에이전트의 등장은 인간과 컴퓨터가 소통하는 방식의 패러다임이 통째로 바뀌고 있음을 시사합니다. 예전에는 사람이 키보드와 마우스의 규칙에 맞춰 컴퓨터를 조작해야 했다면, 이제는 컴퓨터가 인간의 '자연어 지시'와 '시각적 환경'을 직접 이해하고 알아서 움직입니다. Qwen3.7-Plus는 우리의 지시를 찰떡같이 알아듣고 지치지 않고 일하는 가장 훌륭한 비서가 이미 우리 컴퓨터 안에 살기 시작했다는 선언과도 같습니다. 여러분의 다음 든든한 업무 파트너는 사람이 아닐지도 모릅니다.

## 참고자료
1. [Qwen3.7-Plus - Qwen Cloud](https://www.qwencloud.com/models/qwen3.7-plus)
2. [Qwen3.7-Plus: Multimodal Agent Intelligence — LLM... | explainx.ai](https://explainx.ai/llms/qwen3-7-plus-multimodal-agent-intelligence)
3. [Qwen3.7Plus vs Qwen3.7Max in 2026: Multimodal Agent or...](https://ofox.ai/blog/qwen-3-7-plus-vs-qwen-3-7-max-real-benchmark-2026/)
4. [Qwen3.7 Plus API | AIML API](https://aimlapi.com/models/qwen3-7-plus)
5. [Qwen3.7 Plus model | NanoGPT](https://nano-gpt.com/models/text/qwen3.7-plus)
6. [Qwen 3.7 Complete Guide: Alibaba's Strongest AI Model Yet (2026)](https://www.aimadetools.com/blog/qwen-3-7-complete-guide/)
7. [Qwen3.7-Plus Review: Alibaba's GUI Agent, Tested](https://www.buildfastwithai.com/blogs/qwen-3-7-plus-multimodal-agent-review-2026)
8. [Qwen3.7-Plus 发布：多模态 Agent 该怎么测 - HotAI - 博客园](https://www.cnblogs.com/hotai/p/20272234/qwen3-7-plus-multimodal-agent)
9. [Qwen3.7-Plus: Multimodal Agent on Bailian - kiadev.net](https://www.kiadev.net/news/2026-06-02-qwen3-7-plus-bailian-agent)
10. [Multimodal Agent Receives Major Upgrade! Alibaba Officially ...](https://news.aibase.com/news/28533)
11. [Research - Qwen](https://qwen.ai/research/)
12. [Alibaba Unveils Qwen3.7-Plus Multimodal AI Agent Model](https://en.tmtpost.com/news/8011149)
13. [Qwen3.7 Plus: The Balanced Multimodal Flagship | Qwen 3.7](https://qwen3lm.com/qwen3.7-plus/)
14. [Qwen 3.7 Review: Alibaba's New Flagship Ranks #1 in China ...](https://renovateqr.com/blog/qwen-3-7-review-benchmarks-2026)