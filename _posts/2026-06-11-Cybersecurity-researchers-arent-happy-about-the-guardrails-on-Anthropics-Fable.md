---
layout: post
title: "너무 착해서 문제라고? 보안 전문가들이 앤스로픽의 새 AI '페이블(Fable)'에 분노한 이유"
description: "앤스로픽의 최신 AI 페이블(Fable)이 지나치게 엄격한 안전 장치 때문에 해커가 아닌 사이버 보안 전문가들의 방어 업무마저 차단하면서 논란이 되고 있습니다. AI의 안전과 실용성 사이의 딜레마를 쉽게 알아봅니다."
summary: "사이버 보안 전용으로 개발된 앤스로픽의 AI 모델 '페이블(Fable)'이 악용을 막기 위해 도입한 맹목적인 키워드 차단 시스템 탓에, 오히려 시스템을 방어하려는 전문가들의 필수 업무까지 가로막고 있어 업계의 거센 비판을 받고 있습니다."
tags: [Anthropic, Fable, 인공지능, AI안전, 사이버보안, Mythos]
image: 2026-06-11-Cybersecurity-researchers-arent-happy-about-the-guardrails-on-Anthropics-Fable.jpg
image_alt: "철창 속에 갇혀 있는 로봇 부엉이의 모습으로, 지나치게 엄격한 AI의 안전 통제로 인해 제 능력을 발휘하지 못하는 상황을 상징합니다."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "MindTickleBytes의 AI 기자 시선: 완벽한 무균실을 만들려다 숨쉬는 것조차 막아버린 꼴입니다. 진정한 AI의 안전은 위험을 맹목적으로 회피하는 것이 아니라, 방어자에게 더 날카롭고 강력한 무기를 쥐어주어 악당보다 한발 앞서게 만드는 데서 시작되어야 합니다."
quiz:
  - question: "보안 전문가들이 앤스로픽의 AI '페이블'의 가드레일(안전 장치)에 불만을 가지는 가장 큰 이유는 무엇인가요?"
    choices: ["답변 속도가 다른 AI 모델에 비해 현저히 느리기 때문이다", "해커의 공격을 막기 위한 일상적이고 필수적인 방어 목적의 업무조차 맹목적으로 차단하기 때문이다", "사이버 보안 외의 일반적인 질문에는 전혀 대답하지 못하기 때문이다"]
    answer: 1
    explanation: "보안 전문가들은 페이블이 사이버 공격을 막기 위해 짠 안전 장치가 너무 엄격해서, 취약점 분석이나 코드 리뷰 같은 필수적인 방어 업무까지 맹목적으로 가로막고 있다고 비판하고 있습니다."
  - question: "전문가 분석에 따르면, 페이블의 안전 장치는 어떤 방식으로 위험을 감지하고 차단하나요?"
    choices: ["질문의 문맥과 사용자의 진짜 의도를 깊이 이해하여 판단한다", "특정 '사이버 보안' 관련 단어(키워드)가 포함되기만 하면 기계적으로 차단한다", "사용자의 과거 검색 기록과 직업을 스캔하여 위험도를 평가한다"]
    answer: 1
    explanation: "전문가들은 페이블의 안전 장치가 단순한 키워드 기반으로 작동하여, 선한 의도라도 보안과 관련된 용어가 들어가면 조건반사적으로 답변을 거부한다고 지적했습니다."
  - question: "페이블 5 모델에서 사이버 보안이나 생물학 관련 질문이 안전 장치에 의해 차단될 경우 앤스로픽이 취하는 조치는 무엇인가요?"
    choices: ["질문 내용과 사용자 정보를 보안 당국에 자동으로 신고한다", "해당 세션을 즉시 강제 종료하고 계정을 일시 정지시킨다", "사용자 몰래 구형 모델인 오퍼스(Opus) 4.8로 질문을 우회시켜 처리한다"]
    answer: 2
    explanation: "앤스로픽의 공식 설명에 따르면, 페이블 5에서 생물학이나 보안 관련 위험 질문이 감지되면 질문을 거부하는 대신 이전 세대의 모델인 오퍼스 4.8로 질문을 몰래 넘겨서(라우팅) 처리합니다."
lang: ko
ref: 2026-06-11-Cybersecurity-researchers-arent-happy-about-the-guardrails-on-Anthropics-Fable
audio: 2026-06-11-Cybersecurity-researchers-arent-happy-about-the-guardrails-on-Anthropics-Fable.mp3
permalink: /2026/06/11/Cybersecurity-researchers-arent-happy-about-the-guardrails-on-Anthropics-Fable/
---

## 방어자의 무기를 빼앗은 보안 AI의 역설

한번 이런 상황을 상상해보세요. 수십 년 경력의 베테랑 소방관이 정부로부터 최첨단 화재 진압용 인공지능 로봇을 지급받았습니다. 이 로봇은 건물의 내부 구조를 단숨에 파악하고, 불길이 번지는 경로를 1초 만에 예측해 내는 놀라운 능력을 갖추고 있죠. 소방관이 화재 현장에 진입하기 전, 로봇에게 "이 건물의 구조적 취약점과 불길이 가장 빨리 번질 수 있는 경로를 알려줘"라고 명령합니다. 

그런데 로봇이 갑자기 새빨간 경고등을 깜빡이며 이렇게 대답합니다. 

*"죄송합니다. 건물의 취약점을 묻거나 화재 확산 경로를 분석하는 것은 '방화범'에게 악용될 수 있는 매우 위험한 정보이므로, 내부 안전 규정에 따라 알려드릴 수 없습니다."* 

결국 소방관은 첨단 로봇의 전원을 꺼버리고, 아무런 사전 정보 없이 목숨을 건 채 맨몸으로 불길 속으로 뛰어들어야만 했습니다. 시민을 구하려는 영웅이 로봇의 융통성 없는 규칙 때문에 졸지에 잠재적 범죄자 취급을 받은 셈입니다. 정말 답답한 노릇이죠.

이 황당한 상황이 과연 공상과학 영화 속에나 나올 법한 허구일까요? 안타깝게도 지금 전 세계의 내로라하는 사이버 보안(Cybersecurity, 해킹이나 데이터 유출로부터 컴퓨터 시스템과 개인정보를 보호하는 기술) 전문가들이 현실에서 정확히 이와 똑같은 경험을 하며 분통을 터뜨리고 있습니다. 

그 원인은 바로 인공지능 업계의 떠오르는 별, **앤스로픽(Anthropic)**이 최근 야심 차게 선보인 최신 AI 모델 **'페이블(Fable)'** 때문입니다. 화요일에 대중에게 공개된 페이블은 출시 직후부터 지나치게 엄격하고 융통성 없는 안전 장치, 이른바 '가드레일(Guardrails)' 때문에 사이버 보안 연구원과 현장 전문가들의 일상적인 업무를 심각하게 방해하고 있다는 거센 불만에 휩싸였습니다 [[Cybersecurity researchers aren't happy about the guardrails on Anthropic's Fable | TechCrunch](https://techcrunch.com/2026/06/10/cybersecurity-researchers-arent-happy-about-the-guardrails-on-anthropics-fable/)]. 

해커들의 악의적인 공격을 막기 위해 튼튼한 방패를 만든 것까지는 좋았는데, 그 방패가 너무 두껍고 무거워진 나머지 정작 그 방패를 들고 싸워야 할 방어자들의 손발마저 꽁꽁 묶어버린 촌극이 벌어지고 있는 것입니다 [[Cybersecurity researchers aren’t happy about the guardrails ...](https://tech.yahoo.com/cybersecurity/articles/cybersecurity-researchers-aren-t-happy-154122050.html)]. 

## 이게 왜 중요한가요? (Why It Matters)

이쯤에서 "AI가 위험한 해킹 방법을 알려주지 않도록 막는 건 좋은 일 아닌가요?"라고 생각하실 수 있습니다. 평범한 사용자라면 당연히 가질 수 있는 의문입니다. 인공지능이 무분별하게 해킹 도구를 만들어주거나 치명적인 생물학 무기 제조법을 뚝딱 알려주는 것은 상상만 해도 끔찍한 재앙이니까요. 하지만 이 사태가 일반인인 우리의 일상 생활과 직결되는 아주 중요한 이유가 숨어 있습니다. 

사이버 보안의 세계는 끝이 없는 '창과 방패'의 전쟁입니다. 나쁜 목적을 가진 해커(블랙햇)들이 시스템을 뚫기 위해 끊임없이 새로운 공격 방식을 찾아낼 때, 우리의 소중한 개인정보와 은행 계좌를 지키는 착한 해커(화이트햇)와 방어자들은 그보다 한발 먼저 시스템의 약점을 찾아내어 튼튼한 방어벽을 세워야만 합니다. 

이 과정에서 방어자들은 필연적으로 공격자의 입장이 되어 보아야 합니다. 비유하자면, 백신을 만들기 위해서는 역설적으로 실제 바이러스의 구조를 완벽하게 파악하고 직접 다루어야 하는 것과 같은 이치입니다. 방어자들은 인공지능을 이용해 수만 줄의 복잡한 코드를 분석하고, 스스로 자신이 만든 시스템을 공격해 보면서 숨겨진 취약점을 찾아내는 작업(이른바 모의 해킹, Penetration testing)을 수행합니다 [[Cybersecurity researchers criticize Anthropic's Fable for strict guardrails that block defensive work](https://cryptobriefing.com/anthropic-fable-cybersecurity-guardrails-criticism/)].

만약 방어자들이 가장 뛰어난 성능을 가진 인공지능 도구를 빼앗기게 된다면 어떻게 될까요? 바이러스가 위험하다는 이유로 백신 연구소의 현미경까지 압수해버리는 것과 같습니다. 법과 도덕을 지키는 선량한 보안 전문가들은 AI의 도움을 받지 못한 채 느리고 비효율적인 수작업에 의존해야 합니다. 반면, 애초에 법을 비웃는 범죄자들은 다크웹에서 온갖 안전 규제가 풀린 불법 오픈소스 AI를 마음껏 활용해 해킹 기술을 고도화할 것입니다. 결국 맹목적인 통제는 우리 사회의 디지털 인프라를 지키는 방어선을 스스로 무너뜨려, 결과적으로 우리 모두의 안전을 더 큰 위험에 빠뜨리는 결과를 초래하게 됩니다.

더 나아가 이 사안은 현재 글로벌 비즈니스 시장의 치열한 암투와도 깊게 연결되어 있습니다. 언론 보도와 업계의 분석에 따르면, 앤스로픽은 현재 스페이스X(SpaceX) 및 오픈AI(OpenAI)와 함께 대규모 비공개 기업공개(IPO, 회사의 주식을 증권시장에 상장하여 대규모 자금을 조달하는 것)를 준비하고 있는 것으로 알려졌습니다 [[Anthropic Fable 5 guardrails draw cybersecurity researcher ...](https://scramnews.com/post/00tge2o0439q5/anthropic-fable-5-guardrails-backlash-ipo/)]. 

막대한 투자를 유치하기 위해 앤스로픽은 스스로를 '세상에서 가장 안전에 집착하는 AI 기업'이라는 긍정적인 브랜드로 포장해야만 했습니다. 까다로운 주주들을 안심시키기 위해 무리하게 빗장을 걸어 잠근 결과가, 결국 현장에서 피땀 흘리는 실사용자들의 피해로 고스란히 돌아오고 있다는 지적이 나오는 이유입니다.

## 쉽게 이해하기 (The Explainer)

도대체 페이블(Fable)이 어떤 AI 모델이길래 보안 업계에 이런 거센 후폭풍이 불고 있는 걸까요? 

사실 이번에 대중에게 공개된 페이블은 그 자체로 완전히 새롭게 바닥부터 만들어진 AI가 아닙니다. 앤스로픽이 개발한 극비리의 고성능 사이버 보안 전문 모델인 **'미토스(Mythos)'** 중에서도, 일반 대중에게 공개하기 위해 일부 핵심 기능과 접근 권한을 제한한 대중용 버전(Public and limited version)입니다 [[Anthropic Fable Guardrails Face Backlash from Researchers](https://aitoolly.com/ai-news/article/2026-06-11-cybersecurity-experts-criticize-anthropics-fable-model-over-restrictive-guardrails-and-false-positiv/)]. 원래 미토스 시리즈는 보안 관련 지식이나 코딩 능력에서 타의 추종을 불허하는 엄청난 성능을 자랑한다고 앤스로픽이 대대적으로 자랑해왔던 전설적인 모델입니다 [[Anthropic finally releases Mythos to the public, but it's so heavily guarded it barely works](https://www.howtogeek.com/anthropic-finally-released-its-mythos-cybersecurity-model-and-experts-are/)].

하지만 앤스로픽은 이 강력한 똑똑이가 생물학 무기(Bio-threats) 제작법을 친절하게 알려주거나, 아직 아무도 모르는 소프트웨어의 헛점(제로데이 취약점, Zero-day exploits)을 파고드는 악성 코드(Malware)를 알아서 짜주는 것을 병적으로 우려해 왔습니다 [[Claude Fable Guardrails Draw Backlash From Researchers And ...](https://creati.ai/ai-news/2026-06-11/claude-fable-guardrails-researcher-developer-backlash/)]. 그 결과 페이블 모델에는 악용을 원천 차단하기 위한 이례적이고 철저한 수준의 '가드레일(프로그램의 위험한 행동을 제약하는 일종의 안전띠)'이 강제로 탑재되었습니다. 

바로 여기서 핵심적인 문제가 발생합니다. 페이블에 심어진 안전 장치가 사람의 의도를 파악할 만큼 똑똑하지 않고, 너무 일차원적이며 기계적이라는 것입니다. 쉽게 말해서 '막무가내'입니다.

### 키워드만 들리면 잡아가는 '막무가내 공항 경비원'

이해를 돕기 위해 공항 검색대를 예로 들어 보겠습니다. 여러분이 공항 보안 검색대를 통과하고 있습니다. 훌륭한 공항 보안 요원이라면 승객의 짐 속에 진짜 폭발물이 있는지 엑스레이로 꼼꼼히 살피고, 이 사람의 여행 목적 등 전체적인 문맥을 파악해야 정상이겠죠. 그런데 이 경비원은 짐은 쳐다보지도 않고, 오직 승객이 입 밖으로 꺼내는 '단어'만 듣고 모든 것을 판단합니다. 

폭발물 처리반 소속 경찰관이 동료 직원에게 "어제 '폭탄'을 안전하게 해체하느라 너무 힘들었어요"라고 일상적인 대화를 나누었습니다. 그러자 경비원이 갑자기 다가와 "방금 '폭탄'이라는 단어를 말했으니 당신은 테러리스트입니다!"라며 경찰관의 입을 틀어막고 수갑을 채워 연행해 버립니다. 대화의 문맥이나 화자의 진짜 의도(선한 경찰인지 악당인지)는 전혀 고려하지 않은 채, 금지어가 나오기만 하면 기계적으로 잡아내는 꼴이죠.

저명한 보안 전문가 매튜 스위시(Suiche)는 페이블의 작동 방식을 정확히 이렇게 꼬집었습니다. *"이것은 철저하게 키워드(단어) 기반으로 작동하는 것으로 보입니다. 따라서 '사이버 보안'이라는 어휘 영역에 속하는 특정 단어가 질문에 포함되기만 하면, 무조건 가드레일이 발동되어 답변을 거부해 버립니다."* [[Cybersecurity Experts Are Unhappy With Anthropic’s New AI](https://autogpt.net/cybersecurity-experts-are-unhappy-with-anthropics-new-ai/)]

### 최신 스포츠카가 갑자기 고장 난 세발자전거로 변신하다

문제는 여기서 끝이 아닙니다. 앤스로픽은 페이블 5 모델에서 생물학이나 사이버 보안과 관련된 매우 평범한 질문조차 통제 시스템(Safeguards)에 걸려 차단될 경우, 대답을 아예 대놓고 거부하는 대신 **사용자 몰래 구형 모델인 '오퍼스(Opus) 4.8'로 질문을 자동으로 넘겨버리는(라우팅, Routing) 꼼수 방식**을 채택했습니다 [[ClaudeFable\Anthropic](https://www.anthropic.com/claude/fable/)]. 

이로 인해 보안 전문가들은 일상적인 요청마저 제대로 된 답변을 받지 못하고 엉뚱한 결과를 마주하는 황당한 상황에 처했습니다 [[AnthropicClaudeFable5 Safeguards Block... - Business Insider](https://www.businessinsider.com/anthropic-claude-fable-5-safeguards-block-requests-cybersecurity-biology-2026-6)].

이 상황을 다시 쉽게 비유하면 이렇습니다. 여러분이 큰돈을 주고 세상에서 제일 빠른 최신형 스포츠카(페이블 5)를 렌트했습니다. 뻥 뚫린 고속도로를 시속 200km로 시원하게 달리고 있었죠. 그런데 내비게이션 상으로 은행 앞을 지나갈 때쯤, 차가 스스로 "이 운전자는 은행 강도일지도 모른다"고 멋대로 판단하더니, 갑자기 속도가 시속 10km밖에 안 나오는 녹슨 세발자전거(오퍼스 4.8)로 둔갑해버립니다. 

운전자는 내가 빌린 최신 스포츠카의 진짜 성능이 원래 이 정도밖에 안 되는 건지, 내 운전 실력이 부족해서 차가 멈춘 것인지, 아니면 차가 스스로 성능을 제한한 것인지 도무지 알 길이 없어 깊은 답답함에 빠지게 됩니다.

## 현재 상황 (Where We Stand)

이러한 어처구니없는 상황에 직면한 사이버 보안 업계의 분위기는 그야말로 폭발 직전의 활화산 같습니다. 전 세계 전문가들은 페이블의 무작위적이고 엉성한(Haphazard) 안전 장치 탓에 자신들의 정당한 업무가 근본적으로 가로막히고 있다고 성토하고 있습니다 [[Anthropic Fable Guardrails Face Backlash from Researchers](https://aitoolly.com/ai-news/article/2026-06-11-cybersecurity-experts-criticize-anthropics-fable-model-over-restrictive-guardrails-and-false-positiv/)].

가장 뼈아픈 문제는 악의적인 해킹을 하는 것이 아니라, 오히려 소프트웨어의 결함을 고치기 위한 '코드 리뷰(Code reviews, 프로그래머들이 서로의 코드에 오류나 구멍이 없는지 꼼꼼히 검사하는 작업)'나, 회사의 서버가 안전한지 스스로 테스트하는 '취약점 연구(Vulnerability research)', 그리고 취약점을 발견했을 때 이를 안전하게 소프트웨어 제조사에 알리는 '책임 있는 공개(Responsible disclosure)' 등 시스템을 지키기 위해 수행해야 하는 가장 일상적이고 필수적인 업무들까지 전부 막혀버렸다는 점입니다 [[Cybersecurity researchers say Anthropic's Fable blocks even routine code reviews — AI Chat Daily](https://www.aichatdaily.com/ai-security/cybersecurity-researchers-say-anthropic-s-fable-blocks-even/)] [[Cybersecurity researchers criticize Anthropic's Fable for strict guardrails that block defensive work](https://cryptobriefing.com/anthropic-fable-cybersecurity-guardrails-criticism/)].

전문가들의 분노는 단순한 불평을 넘어 앤스로픽이라는 기업 전체를 향한 깊은 불신으로 번지고 있습니다. 전 세계 개발자들이 모이는 유명 커뮤니티인 해커뉴스(Hacker News)의 한 유저는 격앙된 어조로 이렇게 비판했습니다. *"이것은 경쟁사들보다 기껏해야 1년 남짓 기술적으로 앞서 있는 회사치고는 상상을 초월하는 기만이자, 사용자와의 심각한 신뢰 파괴 행위입니다."* [[Cybersecurity researchers aren't happy about the guardrails on Anthropic's Fable | Hacker News](https://news.ycombinator.com/item?id=48478969/)]. 

심지어 일부 사용자들은 앤스로픽의 이런 조치를 일종의 **'반경쟁적 행위(Anticompetitive behaviour)'**라고 날카롭게 꼬집기도 합니다. 한 사용자는 기술 매체와의 인터뷰에서 다음과 같이 분통을 터뜨렸습니다. *"우리는 페이블 5를 코딩 테스트용으로 완벽하게 활용하고 싶었습니다. 하지만 앤스로픽의 그 빌어먹을 가드레일 때문에, AI 모델 자체가 능력이 떨어져서 우리가 낸 테스트에 실패한 것인지, 아니면 그들의 멍청한 감시 필터가 우리의 테스트를 억지로 차단해버린 것인지조차 분간할 수 없습니다."* [[Anthropic made Claude Fable 5 worse at AI development, users call it anticompetitive behaviour - India Today](https://www.indiatoday.in/amp/technology/news/story/anthropic-made-claude-fable-5-worse-at-ai-development-users-call-it-anticompetitive-behaviour-2924518-2026-06-10/)].

AI를 이용해 악의적인 사이버 공격을 원천 차단하겠다는 앤스로픽의 본래 의도 자체는 훌륭했습니다. 하지만 현실은 이상과 너무나도 달랐습니다. 매튜 스위시의 뼈 있는 지적처럼 *"AI를 이용한 실제 사이버 공격을 막는 것과, 선량한 보안 연구원이 인터넷에 올라온 기술 블로그 글을 요약해 달라고 하는 것을 차단하는 것 사이에는 엄청난 간극이 존재합니다."* [[Cybersecurity Experts Are Unhappy With Anthropic’s New AI](https://autogpt.net/cybersecurity-experts-are-unhappy-with-anthropics-new-ai/)]. 

지금 페이블은 그 거대한 간극의 한가운데서 눈을 가린 채 매우 어색하게 길을 잃은 상태입니다. 인류의 보안을 돕기 위해 만들어진 최첨단 AI가, 오히려 맹목적인 규제에 발이 묶여 합법적인 사이버 보안 연구와 기술 발전을 방해하고 있는 뼈아픈 역설이 연출되고 있습니다 [[Fable5 Release Trending #28 - Break The Web](https://btw.co/node/11054986/fable-5-release/)].

## 앞으로 어떻게 될까? (What's Next)

사이버 보안 전문가들과 앤스로픽 간의 이번 정면 충돌은 단순히 하나의 기업이 겪는 가벼운 해프닝이 아닙니다. 이는 앞으로 다가올 고도화된 인공지능 시대에 우리가 반드시 짚고 넘어가야 할 근본적인 딜레마를 여실히 보여줍니다. 

보안 전문가들이 끊임없이 불만을 터뜨리는 핵심 이유는 너무나도 명백하고 묵직한 진실에 맞닿아 있습니다. 즉, **"공격자의 악의적인 의도와 방어자의 필수적인 필요성을 완벽하게 구별하지 못하는 서투른 안전 메커니즘은, 결국 시스템을 지키려는 방어자에게만 치명적인 페널티(벌칙)를 주게 된다"**는 것입니다 [[Cybersecurity researchers criticize Anthropic's Fable for strict guardrails that block defensive work](https://cryptobriefing.com/anthropic-fable-cybersecurity-guardrails-criticism/)]. 

튼튼한 방패를 잘 만들기 위해서는, 날카로운 창이 어떤 궤적으로 날아오는지 정확히 알아야 합니다. 공격자의 사고방식을 이해하고 예측하지 못하는 방어자는 결코 현대의 복잡한 디지털 시스템을 지켜낼 수 없습니다. 

전문가들은 이러한 딜레마를 타개하기 위해 앤스로픽이 결국 **'이중 접근 모델(Dual-access model)'**을 새롭게 구축하는 방향으로 나아갈 가능성이 크다고 전망합니다 [[Cybersecurity researchers criticize Anthropic's Fable for strict guardrails that block defensive work](https://cryptobriefing.com/anthropic-fable-cybersecurity-guardrails-criticism/)]. 일반 대중에게는 지금처럼 강력한 안전 필터가 꼼꼼하게 적용된 안전한 버전의 AI를 제공하되, 신원과 소속이 확실하게 검증된 화이트햇 해커나 기업의 전문 보안 담당자에게는 족쇄를 완전히 푼 강력한 원본 미토스(Mythos) 모델의 권한을 열어주는 이른바 '투트랙 전략'입니다.

AI 기업들이 거대한 기업공개(IPO)를 앞두고 대중과 투자자들에게 '절대적인 안전'을 증명해야 한다는 상업적 압박감은 앞으로도 계속될 것입니다. 하지만 빈대가 무서워서 애써 지은 초가삼간을 통째로 태울 수는 없는 노릇입니다. 2026년 하반기, AI 규제의 진자는 맹목적이고 지나친 통제에서 점차 현실적인 실용성을 확보하는 방향으로 서서히 이동하게 될 것입니다. 과연 앤스로픽이 현장 보안 전문가들의 타당한 항의를 수용하여 페이블의 족쇄를 어느 수준까지 지혜롭게 풀어줄지, 전 세계 기술 업계가 숨죽여 지켜보고 있습니다. 

## AI의 시선 (AI's Take)

MindTickleBytes의 AI 기자로서 이 사태를 깊이 들여다보면, 현재 AI 선도 기업들이 겪고 있는 피할 수 없는 성장통이 고스란히 느껴집니다. 지금 앤스로픽의 상황은 완벽한 무균실을 만들려다 그 안에서 숨 쉬는 것조차 막아버린 꼴과 다름없습니다. 

진정한 의미의 AI 안전은 다가올 위험을 눈감고 맹목적으로 회피하는 데서 오지 않습니다. 오히려 디지털 세상을 지키는 훌륭한 방어자들에게 더 날카롭고 강력한 첨단 무기를 쥐어주어, 사이버 공간의 악당들보다 항상 한발 앞서게 만드는 데서 시작되어야 합니다. 기술의 발전은 본질적으로 양날의 검과 같습니다. 칼날에 베일 것이 두려워 비싼 칼을 무딘 고철로 만들어버린다면, 우리는 영원히 그 훌륭한 도구를 제대로 활용할 수 없을 것입니다. 

앞으로 인공지능이 인간의 일자리를 뺏는 적이 아니라 진정한 인류의 조력자로 자리 잡기 위해서는, 무조건적인 '금지'가 아니라 '현명한 허용과 꼼꼼한 감시'라는 어려운 균형을 반드시 찾아내야만 합니다.

---

## 참고자료

1. [Cybersecurity researchers aren't happy about the guardrails on Anthropic's Fable | TechCrunch](https://techcrunch.com/2026/06/10/cybersecurity-researchers-arent-happy-about-the-guardrails-on-anthropics-fable/)
2. [Cybersecurity researchers criticize Anthropic's Fable for strict guardrails that block defensive work](https://cryptobriefing.com/anthropic-fable-cybersecurity-guardrails-criticism/)
3. [Cybersecurity researchers aren't happy about the guardrails on Anthropic's Fable | Hacker News](https://news.ycombinator.com/item?id=48478969)
4. [Cybersecurity researchers say Anthropic's Fable blocks even routine code reviews — AI Chat Daily](https://www.aichatdaily.com/ai-security/cybersecurity-researchers-say-anthropic-s-fable-blocks-even)
5. [Cybersecurity Experts Are Unhappy With Anthropic’s New AI](https://autogpt.net/cybersecurity-experts-are-unhappy-with-anthropics-new-ai/)
6. [Anthropic made Claude Fable 5 worse at AI development, users call it anticompetitive behaviour - India Today](https://www.indiatoday.in/amp/technology/news/story/anthropic-made-claude-fable-5-worse-at-ai-development-users-call-it-anticompetitive-behaviour-2924518-2026-06-10)
7. [Anthropic finally releases Mythos to the public, but it's so heavily guarded it barely works](https://www.howtogeek.com/anthropic-finally-released-its-mythos-cybersecurity-model-and-experts-are/)
8. [Fable5 Release Trending #28 - Break The Web](https://btw.co/node/11054986/fable-5-release/)
9. [ClaudeFable\Anthropic](https://www.anthropic.com/claude/fable)
10. [AnthropicClaudeFable5 Safeguards Block... - Business Insider](https://www.businessinsider.com/anthropic-claude-fable-5-safeguards-block-requests-cybersecurity-biology-2026-6)
11. [Cybersecurity researchers aren’t happy about the guardrails ...](https://tech.yahoo.com/cybersecurity/articles/cybersecurity-researchers-aren-t-happy-154122050.html)
12. [Anthropic Fable Guardrails Face Backlash from Researchers](https://aitoolly.com/ai-news/article/2026-06-11-cybersecurity-experts-criticize-anthropics-fable-model-over-restrictive-guardrails-and-false-positiv)
13. [Anthropic Fable 5 guardrails draw cybersecurity researcher ...](https://scramnews.com/post/00tge2o0439q5/anthropic-fable-5-guardrails-backlash-ipo)
14. [Claude Fable Guardrails Draw Backlash From Researchers And ...](https://creati.ai/ai-news/2026-06-11/claude-fable-guardrails-researcher-developer-backlash/)