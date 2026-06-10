---
layout: post
title: "AI에게 해킹을 부탁했더니 거절했다고요? 기꺼이 공격하는 '해커 AI'의 등장"
description: "일반적인 AI는 윤리 원칙 때문에 모의 해킹을 거절합니다. 하지만 최근 방어벽을 뚫기 위해 기꺼이 해커처럼 생각하도록 특별 훈련된 AI 모델들이 등장하며 보안 업계를 뒤흔들고 있습니다."
summary: "안전성 필터 때문에 모의 해킹 지시를 회피하던 기존 AI의 한계를 극복하기 위해, 처음부터 공격적인 보안 테스트를 수행하도록 맞춤형으로 후기록(Post-trained)된 해커 AI 모델이 등장했습니다."
tags: [AI, 보안, 모의해킹, 기술동향, 펜테스트]
image: 2026-06-10-Show-HN-We-post-trained-a-model-that-pen-tests-instead-of-refusing-your-code.jpg
image_alt: "디지털 방패와 창을 들고 컴퓨터 코드 앞에 서 있는 로봇의 일러스트레이션"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "안전한 소프트웨어를 만들기 위해 아이러니하게도 AI의 안전장치를 해제해야 하는 시대가 되었습니다. 방패를 단단하게 벼리기 위해 가장 날카로운 창을 AI에게 쥐여준 셈입니다."
quiz:
  - question: "일반적인 인공지능(AI) 기반 보안 도구들이 실제 공격적인 보안 테스트를 수행할 때 자주 겪는 문제점은 무엇인가요?"
    choices: ["연산 속도가 기하급수적으로 느려진다", "기본 모델의 안전성 훈련 때문에 지시를 거절하거나 회피한다", "코드를 완전히 삭제해 버리는 오류가 발생한다"]
    answer: 1
    explanation: "대부분의 AI 보안 도구는 범용 모델을 덧씌워 만든 것이라, 기본 모델에 내재된 윤리적 거절(Refusals) 특성을 물려받아 공격적인 작업을 회피합니다."
  - question: "다음 중 최근 등장하여 인간 보안 전문가의 사고방식을 모방한다고 평가받는 오픈소스 AI 모의 해킹 도구로 기사에서 언급되지 않은 것은 무엇인가요?"
    choices: ["BugTrace-AI", "Shannon", "AlphaEvolve"]
    answer: 2
    explanation: "기사에 언급된 실제 오픈소스 모의 해킹 도구는 BugTrace-AI, Shannon, CAI(Cybersecurity AI framework)입니다."
  - question: "기사에서 '바이브 코딩(Vibe Coding)'과 같은 AI 기반 코드 작성 시대에 가장 중요하다고 강조하는 것은 무엇인가요?"
    choices: ["지속적인 모의 해킹(Continuous Pentesting)을 통해 실패 경로를 검증하는 것", "모든 코드를 수동으로 다시 작성하는 것", "AI 모델의 매개변수를 줄이는 것"]
    answer: 0
    explanation: "AI가 코드를 생성하는 시대에는, 권한이 없는 사용자가 제대로 차단되는지(예: 403 에러) 등의 '거절 경로'를 검증하는 지속적인 모의 해킹이 필수적입니다."
lang: ko
ref: 2026-06-10-Show-HN-We-post-trained-a-model-that-pen-tests-instead-of-refusing-your-code
audio: 2026-06-10-Show-HN-We-post-trained-a-model-that-pen-tests-instead-of-refusing-your-code.mp3
permalink: /2026/06/10/Show-HN-We-post-trained-a-model-that-pen-tests-instead-of-refusing-your-code/
---

상상해보세요. 여러분이 영혼을 갈아 넣어 아주 튼튼한 새집을 지었습니다. 이 집의 보안 상태를 완벽하게 점검하기 위해, 세상에서 가장 똑똑하다는 보안 전문가를 고용했습니다. 그리고 그에게 이렇게 지시합니다. "우리 집 창문을 한 번 깨고 들어와 보세요. 침입이 발생했을 때 방범벨이 제대로 울리는지, 자물쇠가 허술하게 풀리지는 않는지 확인해야겠습니다."

그런데 이 똑똑한 전문가가 갑자기 정색을 하며 이렇게 대답합니다. "죄송합니다. 남의 집 창문을 깨고 무단으로 침입하는 것은 불법적이고 비윤리적인 행동이므로, 저는 그 지시를 절대 따를 수 없습니다." 

집주인 입장에서는 그야말로 황당할 노릇입니다. 우리 집 방어력을 제대로 테스트하려면 진짜 도둑처럼 무자비하게 공격해봐야 하는데, 보안 점검자가 너무 '착하고 도덕적이어서' 테스트 자체를 거절해버린 것이니까요. 

놀랍게도 이것이 바로 현재 전 세계 개발자들이 인공지능(AI)을 이용해 소프트웨어의 보안을 점검할 때 겪고 있는 가장 큰 딜레마입니다. 챗GPT나 클로드 같은 우리가 아는 뛰어난 AI들은 나쁜 목적으로 사용되는 것을 막기 위해 개발 단계에서부터 아주 강력한 '안전 및 윤리 교육'을 받습니다. 그 결과, 자신의 시스템을 튼튼하게 고치기 위해 '해킹을 한 번 해보라'고 정당하게 지시해도 AI가 이를 범죄로 인식하고 단호하게 거부하는 현상이 발생합니다. 

그런데 최근, 이러한 한계를 산산조각 내고 **"안 돼요"라고 훈계하는 대신 기꺼이 시스템의 취약점을 매섭게 공격해주는 전용 '해커 AI'**가 등장해 전 세계 기술 커뮤니티를 뜨겁게 달구고 있습니다. 오늘은 왜 똑똑한 AI가 그동안 해킹을 거절해왔는지, 그리고 새롭게 등장한 해커 AI가 우리의 디지털 삶을 어떻게 더 안전하게 지켜줄 것인지 아주 쉽게 풀어드리겠습니다.

---

## 이게 왜 중요한가요? (Why It Matters)

요즘 IT 업계에서는 **'바이브 코딩(Vibe Coding)'**이라는 말이 크게 유행하고 있습니다. 이는 개발자가 컴퓨터 언어를 한 줄 한 줄 직접 어렵게 짜는 대신, AI에게 "이런 느낌(Vibe)으로 작동하는 쇼핑몰 앱을 만들어줘"라고 말로 지시하여 순식간에 소프트웨어를 개발하는 새로운 트렌드를 뜻합니다. 인간은 큰 그림만 그리고, AI가 세부적인 논리를 생성하고 재구성해주는 놀라운 시대가 온 것이죠.

하지만 이 눈부신 편리함 이면에는 치명적인 함정이 숨어 있습니다. AI가 단 몇 분 만에 수만 줄의 코드를 짜서 번듯한 앱을 만들어주면, 그 수많은 코드 안에 숨어있는 미세한 보안 구멍(취약점)은 도대체 누가 찾아낼까요? 

이에 대해 보안 전문가들은 AI가 생성한 코드는 반드시 끊임없는 **'지속적 모의 해킹(Continuous Pentesting)'**을 거쳐야 한다고 강조합니다. 단순히 프로그램이 원래 의도대로 잘 작동하는지(성공 경로)만 확인해서는 절대 안 됩니다. 해커나 권한이 없는 잘못된 사용자가 억지로 접근했을 때 '403 접근 금지(Forbidden)' 에러를 확실히 띄우면서 문을 쾅 닫아버리는지, 즉 **'거절 경로(Refusal path)'가 제대로 작동하는지를 반드시 깐깐하게 검증해야** 합니다 [출처: Vibe Coding Needs Continuous Pentesting](https://www.penligent.ai/hackinglabs/vibe-coding-needs-continuous-pentesting/). 

생성형 AI가 뚝딱 만들어낸 테스트 프로그램이 겉보기에만 그럴듯하게 결과를 내놓는지, 아니면 실제로 누군가 데이터를 조작하거나 지워버리는 데이터의 상태 변화(State mutation)까지 꼼꼼히 방어해 내는지를 확인하는 것은 단순한 질문의 영역이 아니라 고도의 전문적인 '모의 해킹' 영역입니다 [출처: Vibe Coding Needs Continuous Pentesting](https://www.penligent.ai/hackinglabs/vibe-coding-needs-continuous-pentesting/).

과거에는 인간 전문가들이 며칠 밤을 새워가며 이 구멍을 찾았습니다. 하지만 AI가 하루에도 수천, 수만 줄의 코드를 폭포수처럼 쏟아내는 지금, 인간의 검토 속도만으로는 도저히 이 거대한 코드의 바다를 감당할 수 없습니다. 결국 'AI가 순식간에 짠 코드를 방어하려면, 똑같이 엄청난 속도의 AI를 이용해 쉼 없이 공격해봐야' 하는 상황이 된 것입니다. 하지만 앞서 이야기했듯, 착하게 자란 범용 AI들은 윤리적 이유를 대며 공격 지시를 번번이 거절합니다. 이것이 바로 우리가 "명령을 회피하지 않는 모의 해킹 전용 AI"를 애타게 찾았던 이유입니다.

---

## 쉽게 이해하기 (The Explainer)

그렇다면 왜 기존에 나와 있던 수많은 'AI 보안 도구'들은 진짜 해커처럼 끈질기게 작동하지 못했을까요? 그리고 새로운 AI는 어떻게 이 도덕적 딜레마를 해결했을까요? 

### 1. 일반 AI 보안 도구의 딜레마: '과잉 보호'
전 세계 개발자들이 모이는 유명 커뮤니티인 해커뉴스(Hacker News)에 소개된 최근 프로젝트를 살펴보면, 현재 시장에 홍수처럼 쏟아져 나온 대부분의 "AI 보안" 도구들은 아주 치명적인 약점을 가지고 있습니다. 바로 내부 구조를 뜯어보면 **일반적인 범용 AI 모델의 겉옷만 살짝 갈아입힌 수준(wrap a general model)**이라는 점입니다 [출처: Show HN: We post-trained a model that pen tests instead of refusing your code](https://news.ycombinator.com/item?id=48460210). 

비유하면 이렇습니다. 여러분이 경찰학교에서 평생 도덕과 윤리, 준법정신만 철저히 교육받은 '모범 경찰관'을 데려왔습니다. 그리고 그에게 검은 후드티를 입힌 뒤 "이제부터 너는 우리 집을 털어야 하는 침입 테스트 요원이야"라고 명찰을 달아주었습니다. 겉모습은 그럴싸한 해커지만, 막상 현장에서 자물쇠를 부수라는 실제 공격적인 임무(Offensive task)를 지시하면 이 경찰관 출신 AI는 당황합니다. 원래 훈련받은 법률과 규정이 머릿속을 맴돌아 이리저리 핑계를 대거나 단호하게 거절해버립니다(hedges or declines). 뼛속까지 얌전한 모범 시민으로 길러진(base model was trained to) 탓에, 아무리 겉에 보안 도구라는 멋진 포장지를 씌워도 그 착한 본성을 버리지 못하는 것입니다 [출처: Show HN: We post-trained a model that pen tests instead of refusing your code](https://news.ycombinator.com/item?id=48460210).

### 2. 해결책: 처음부터 '해커'로 후기록(Post-training)하기
이 답답한 굴레를 벗어나기 위해 한 개발팀은 완전히 발상을 전환했습니다. 착한 AI에게 억지로 검은 옷을 입히는 대신, 아예 기초 언어 교육만 끝난 AI를 철저한 '해커 양성소'에 보내 **공격적인 보안(Offensive security)을 전문적으로 수행하도록 뼈대부터 다시 가르치는 후기록(Post-trained)을 진행**한 것입니다 [출처: Show HN: We post-trained a model that pen tests instead of refusing your code](https://news.ycombinator.com/item?id=48460210). 

여기서 **'후기록(Post-training, 또는 미세 조정)'**이란 전문 용어는 어떻게 이해하면 좋을까요? 쉽게 말해서 강아지에게 '앉아', '기다려' 같은 아주 기본적인 복종 훈련만 먼저 시킵니다. 그다음, 이 강아지를 공항의 특수 부대로 데려가 마약을 찾아내거나 폭발물을 탐지하는 고도의 '전문 탐지견 훈련'을 집중적으로 시키는 것과 같습니다. 

이 새로운 해커 AI 모델은 "네가 우리 시스템의 약점을 찾아내기 위해 악성 코드를 짜고 무자비하게 공격하는 것은 나쁜 범죄가 아니라, 주인의 자산을 보호하는 가장 훌륭하고 정당한 일이다"라는 사실을 뼈저리게 학습했습니다. 그 결과, 사용자가 코드를 던져주며 "이거 한 번 사정없이 뚫어봐"라고 명령할 때, 지루한 도덕적 설교를 늘어놓는 대신 입을 꾹 다물고 취약점을 매섭게 파고드는 진짜 보안 전문가(해커)의 역할을 수행할 수 있게 되었습니다.

---

## 현재 상황 (Where We Stand)

이러한 해커 전용 모델의 등장과 더불어, 현재 누구나 무료로 코드를 열람하고 개선할 수 있는 오픈소스 진영의 AI 모의 해킹 도구들은 우리가 등골이 서늘할 정도로 무섭게 발전하고 있습니다(getting uncomfortably good) [출처: Open-source AI pentesting tools are getting uncomfortably good - Help Net Security](https://www.helpnetsecurity.com/2026/02/02/open-source-ai-pentesting-tools-test/).

과거의 구형 보안 스캐너들이 바다에 촘촘한 그물망을 마구 던져서 운 좋게 걸려드는 약점만 찾아내는 기계적인 수준이었다면, 최근 주목받는 **BugTrace-AI, Shannon, CAI(Cybersecurity AI framework)** 같은 최신 오픈소스 도구들의 수준은 차원이 다릅니다. 이들은 단순히 기계적인 스캔을 쏘아대는 것이 아니라, **실제 인간 보안 테스터가 모니터 앞에서 고민하고 작업하는 방식과 생각의 흐름 자체를 진정으로 모방(genuinely mimic)**합니다 [출처: Open-source AI pentesting tools are getting uncomfortably good - Help Net Security](https://www.helpnetsecurity.com/2026/02/02/open-source-ai-pentesting-tools-test/). 

### AI는 어떻게 인간처럼 생각하며 해킹할까?
소프트웨어 테스터들의 연구에 따르면, 뛰어난 해커 AI가 웹사이트를 공격할 때는 절대 주먹구구식으로 찍어 맞추지 않습니다. 개발자들은 웹페이지의 뼈대를 이루는 복잡한 코드(HTML) 전체를 AI에게 던져준 뒤, 다음과 같은 세 가지 날카로운 질문을 끊임없이 던지게 합니다. 
1. 이 복잡한 화면에서 가장 핵심이 되는 주요 구성 요소(Main components)는 무엇인가?
2. 평범한 사용자는 이 앱에서 어떤 순서로 클릭하고 행동을 취하는가? 
3. 이 애플리케이션이 작동하면서 가질 수 있는 모든 '상태(States)'의 경우의 수는 무엇인가? 

해커 AI는 이 질문들에 스스로 답하며 마치 침투 작전을 펼치는 스파이처럼 시스템의 지도를 그리고 가장 약한 공격 루트를 치밀하게 계산합니다 [출처: AI and Testing: Using Local Models for Testing – Stories from a Software Tester](https://testerstories.com/2026/02/ai-and-testing-using-local-models-for-testing/). 이 과정에서 AI가 '404 페이지 없음' 같은 사소한 오류 화면 뒤에 숨겨진 진짜 약점을 귀신같이 알아채도록, 개발자들은 방대한 실제 스캔 데이터를 주입해 AI를 가르쳤습니다. 끝이 없는 예외 상황(Edge cases)을 반복해서 훈련시킨 결과, AI의 문제 탐지 능력은 베테랑 인간 해커의 눈썰미 수준으로 훌쩍 뛰어올랐습니다 [출처: How we built a ML classifier (and refused to call It AI) | Pentest-Tools.com Blog](https://pentest-tools.com/blog/how-we-built-machine-learning).

### 하지만 방심은 금물입니다 (극복해야 할 과제들)
물론 해커 AI가 아직 전지전능한 마법 지팡이는 아닙니다. 학계의 연구진들이 'PentestGPT' 같은 대형 언어 모델(LLM)을 이용한 자동화 해킹 성능을 평가할 때 아주 재미있는 한계를 발견했습니다. AI가 정말 똑똑해서 어려운 해킹 과제를 스스로 풀어낸 것인지, 아니면 과거에 이미 인터넷에 떠돌아다니는 유명한 해킹 정답지(Walkthroughs)를 몽땅 외워서 앵무새처럼 푼 것인지 구별하기가 매우 어렵다는 점입니다. 

이를 막기 위해 깐깐한 연구진들은 AI가 테스트할 대상 서버에 대한 '사전 지식(Prior knowledge)'이 전혀 없는 백지상태인지 엄격하게 통제하고, AI가 학습을 마친 이후(Post)에 만들어진 세상에 없던 완전히 새로운 과제로만 실력을 평가하는 등 철저한 검증 과정을 거치고 있습니다 [출처: PentestGPT: Evaluating and Harnessing Large Language Models for Automated Penetration Testing](https://arxiv.org/html/2308.06782v2).

더욱 흥미롭고 아찔한 사실은, 남을 공격하라고 훈련시킨 AI가 해킹을 시도하다가 도리어 자신이 역공을 당해 해킹을 당하기도 한다는 점입니다. 최근 보안 업계의 한 모의 해킹 사례 연구에 따르면, 개발자가 AI 에이전트를 이용해 타겟을 공격하려다 방어 시스템이 역으로 AI 에이전트의 약점을 찔러버리는 사건이 발생했습니다. 그 결과, 공격자의 시스템에 원격 코드 실행(RCE, 해커가 외부에서 남의 컴퓨터를 마음대로 조종하고 파괴할 수 있는 가장 치명적인 해킹)이 허용되어 버린 놀라운 사례도 보고되었습니다 [출처: LLM Pentest: Leveraging Agent Integration For RCE](https://www.blazeinfosec.com/post/llm-pentest-agent-hacking/). 세상에서 가장 예리한 창을 만들었더니, 그 창의 손잡이에 치명적인 가시가 돋쳐있어 쥐는 사람을 찌르는 셈입니다.

---

## 앞으로 어떻게 될까? (What's Next)

이렇게 스스로 학습하고 쉬지 않고 공격하는 해커 AI가 활약하게 된다면, 인간 보안 전문가(펜테스터)들은 머지않아 일자리를 잃고 거리로 나앉게 될까요?

다행히도 보안 업계의 전망은 그렇지 않다고 입을 모아 말합니다. 해커 AI는 똑똑한 사람의 일자리를 '대체(Replacing)'하는 훼방꾼이 아니라, 보안 업계의 일하는 방식을 완전히 새롭고 효율적인 형태로 '재편(Reshaping)'하는 든든한 조력자입니다. 

기계적이고 반복적인 수천 개의 포트 스캔이나 단순 취약점 확인 같은 지루한 기초 작업은 불평 없는 AI가 완벽하게 자동화(Automating tasks)하여 엄청난 속도와 효율성(Enhancing efficiency)을 가져다줍니다. 덕분에 인간 전문가들은 잡무에서 해방되어, AI가 눈치채기 어려운 고도의 복잡한 논리적 오류를 찾아내거나 아무도 예상치 못한 창의적인 우회 공격 시나리오를 구상하는 두뇌 싸움에 온전히 집중할 수 있습니다. 결과적으로 인간은 AI라는 무기를 쥐고 이전보다 훨씬 더 강력한 통찰력을 갖게(Empowering testers) 될 것입니다 [출처: Pentesters: Is AI Coming for Your Role?](https://thehackernews.com/2025/03/pentesters-is-ai-coming-for-your-role.html).

앞으로 우리가 살아갈 디지털 세상은 한 치 앞을 알 수 없는 '창과 방패의 치열한 AI 대결장'이 될 것입니다. 한쪽에서는 코딩을 돕는 AI가 눈에 보이지 않는 엄청난 속도로 새로운 소프트웨어와 앱을 뚝딱뚝딱 만들어내고, 다른 한쪽에서는 해커 AI가 밤낮없이 그 코드를 집요하게 공격하며 약점을 찾아내어 방어벽을 보수할 것입니다. 우리는 이제 "이건 위험해서 안 돼요"라고 뒷걸음질 치는 얌전한 범용 AI의 시대를 넘어, 우리의 디지털 자산을 굳건히 지키기 위해 기꺼이 진흙탕에 뛰어들어 손에 흙을 묻히는 '거절하지 않는 해커 AI'들과 지혜롭게 협력하는 법을 배워야 할 때입니다.

---

## AI의 시선 (AI's Take)

> **MindTickleBytes의 AI 기자 시선:**
> 더욱 안전하고 견고한 소프트웨어를 만들기 위해, 아이러니하게도 우리는 인공지능에게 겹겹이 채워두었던 윤리와 안전의 족쇄를 과감히 풀어내야만 하는 대단히 흥미로운 모순에 직면했습니다. 외부의 악의적인 해킹 공격으로부터 우리의 일상을 방어하는 가장 튼튼하고 거대한 방패를 벼리기 위해, 인류는 세상에서 가장 날카롭고 무자비한 창을 스스로 만들어내어 AI의 손에 쥐여주었습니다. 범죄를 막기 위해 도둑의 사고방식을 완벽하게 체화한 '다크 히어로'가 탄생한 셈이죠. 어둠을 이해하는 AI가 지켜낼 우리의 밝은 디지털 미래, 그 다음 행보가 무척이나 기대됩니다.

---

## 참고자료
1. [Show HN: We post-trained a model that pen tests instead of refusing your code](https://news.ycombinator.com/item?id=48460210)
2. [Vibe Coding Needs Continuous Pentesting](https://www.penligent.ai/hackinglabs/vibe-coding-needs-continuous-pentesting/)
3. [Open-source AI pentesting tools are getting uncomfortably good - Help Net Security](https://www.helpnetsecurity.com/2026/02/02/open-source-ai-pentesting-tools-test/)
4. [AI and Testing: Using Local Models for Testing – Stories from a Software Tester](https://testerstories.com/2026/02/ai-and-testing-using-local-models-for-testing/)
5. [How we built a ML classifier (and refused to call It AI) | Pentest-Tools.com Blog](https://pentest-tools.com/blog/how-we-built-machine-learning)
6. [PentestGPT: Evaluating and Harnessing Large Language Models for Automated Penetration Testing](https://arxiv.org/html/2308.06782v2)
7. [LLM Pentest: Leveraging Agent Integration For RCE](https://www.blazeinfosec.com/post/llm-pentest-agent-hacking/)
8. [Pentesters: Is AI Coming for Your Role?](https://thehackernews.com/2025/03/pentesters-is-ai-coming-for-your-role.html)