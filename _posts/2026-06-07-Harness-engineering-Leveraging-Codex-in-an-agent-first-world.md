---
layout: post
title: "개발자가 코딩을 멈췄다? 5개월 만에 100만 줄의 코드를 혼자 짠 AI의 비밀"
description: "오픈AI(OpenAI)의 3명 엔지니어가 단 한 줄의 코드도 직접 짜지 않고 100만 줄짜리 소프트웨어를 완성했습니다. '하네스 엔지니어링'이라는 새로운 방식이 어떻게 소프트웨어 개발을 바꾸고 있는지 쉽게 알아봅니다."
summary: "오픈AI 연구진이 코드를 직접 작성하는 대신 AI를 지휘하는 '하네스 엔지니어링' 방식을 통해, 인간의 타이핑 없이 5개월 만에 100만 줄 분량의 소프트웨어를 완성하는 놀라운 실험 결과를 공개했습니다."
tags: [OpenAI, 하네스엔지니어링, AI코딩, 인공지능, 챗GPT]
image: 2026-06-07-Harness-engineering-Leveraging-Codex-in-an-agent-first-world.jpg
image_alt: "오케스트라 지휘자처럼 여러 대의 로봇 팔이 코드를 작성하는 것을 지휘하는 인간 엔지니어의 모습"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "인간의 역할이 '타자 치는 사람'에서 '방향을 제시하는 감독'으로 진화하고 있습니다. 진정한 창의성은 코드가 아니라 올바른 질문과 설계에 있다는 것을 보여주는 완벽한 사례입니다."
quiz:
  - question: "오픈AI의 '하네스 엔지니어링' 실험에서 인간 엔지니어 3명이 5개월 동안 직접 작성한 코드의 양은 얼마인가요?"
    choices: ["약 10만 줄", "단 한 줄도 없음", "약 50만 줄"]
    answer: 1
    explanation: "오픈AI의 엔지니어 3명은 5개월 동안 단 한 줄의 코드도 직접 쓰지 않고, 오직 AI에게 지시만 내려서 100만 줄에 달하는 소프트웨어를 완성했습니다."
  - question: "이번 실험에서 인간 개발자의 역할은 다음 중 무엇과 가장 비슷해졌나요?"
    choices: ["직접 건물을 짓는 벽돌공", "영화의 모든 장면을 연기하는 배우", "오케스트라를 지휘하는 지휘자"]
    answer: 2
    explanation: "하네스 엔지니어링에서 인간은 직접 코드를 타이핑하는 대신, AI 에이전트들이 올바르게 일할 수 있도록 지시하고 관리하는 지휘자(감독)의 역할을 합니다."
  - question: "AI가 스스로 코드를 수정하고 완성도를 높이기 위해 거치는 반복적인 검토 과정을 오픈AI는 내부적으로 어떤 캐릭터에 비유했나요?"
    choices: ["터미네이터 루프", "랄프 위검 루프", "아이언맨 루프"]
    answer: 1
    explanation: "AI 에이전트가 스스로 코드를 작성하고, 자체 리뷰를 거쳐 만족할 때까지 수정하는 과정을 유명 만화 캐릭터의 이름을 따 '랄프 위검 루프(Ralph Wiggum Loop)'라고 불렀습니다."
lang: ko
ref: 2026-06-07-Harness-engineering-Leveraging-Codex-in-an-agent-first-world
audio: 2026-06-07-Harness-engineering-Leveraging-Codex-in-an-agent-first-world.mp3
permalink: /2026/06/07/Harness-engineering-Leveraging-Codex-in-an-agent-first-world/
---

상상해보세요. 여러분이 엄청나게 크고 복잡한 저택을 짓고 싶습니다. 과거에는 직접 땀을 흘리며 벽돌을 나르고 시멘트를 바르며 수개월, 혹은 수년을 고생해야 했습니다. 하지만 지금 여러분 앞에는 지치지 않는 수십 명의 숙련된 로봇 건축가들이 대기하고 있습니다. 여러분은 그저 "거실은 남향으로 내고, 벽지는 따뜻한 베이지색으로 해줘"라고 말하기만 하면 됩니다. 로봇들이 알아서 도면을 그리고, 자재를 주문하고, 벽돌을 쌓아 완벽한 집을 짓습니다. 여러분은 그저 완성되어 가는 과정을 느긋하게 지켜보며 "창문 크기만 조금 더 키워줘"라고 방향만 수정해 주면 됩니다. 

소프트웨어 개발의 세계에서 바로 이런 마법 같은 일이 현실이 되었습니다. 우리가 늦은 밤까지 컴퓨터 키보드를 타닥타닥 두드리며 알 수 없는 영어 명령어(코드)를 한 땀 한 땀 짜맞추던 시대가 저물고, AI에게 "이런 프로그램을 만들어"라고 말로 지시만 내리는 시대가 온 것입니다. 최근 오픈AI(OpenAI, 챗GPT를 만든 회사)가 발표한 놀라운 실험 결과는 미래의 소프트웨어가 어떻게 만들어질지 완벽하게 보여줍니다 [OpenAI's Agent-First Codebase Learnings | Blog](https://alexlavaee.me/blog/openai-agent-first-codebase-learnings/).

## 이게 왜 중요한가요?

이 기술의 발전이 코딩을 전혀 모르는 우리의 일상과 무슨 상관이 있을까요? 쉽게 말해서, 우리가 매일 사용하는 스마트폰 앱이나 은행 시스템, 재미있는 게임 등 모든 디지털 서비스가 만들어지는 '속도'와 '비용'의 제약이 완전히 사라진다는 뜻입니다. 아이디어만 있다면 누구나 상상하던 프로그램을 현실로 만들 수 있는 세상이 코앞에 다가왔습니다.

오픈AI 소속 기술진인 라이언 로폴로(Ryan Lopopolo)가 작성한 공식 보고서에 따르면 [Harnessengineering:leveragingCodexinanagent-firstworld](https://www.aibrief.in/article/harness-engineering-leveraging-codex-in-an-agent-first-world), 이들은 최근 5개월에 걸쳐 놀라운 내부 실험을 진행했습니다. 단 3명의 인간 엔지니어가 모여 새로운 소프트웨어를 기획하고 출시했는데, 이 프로그램의 전체 크기가 무려 100만 줄(컴퓨터 언어를 적어 내려간 줄의 수)에 달했습니다 [HarnessEngineering: Why 2026's AI Edge Isn't a Bigger Model](https://thebytedive.com/ai/260411-harness-engineering-ai-edge-2026/). 100만 줄의 코드란, 두꺼운 백과사전 수십 권을 가득 채울 수 있는 분량이자 웬만한 대기업의 핵심 서비스를 무리 없이 구동할 수 있을 만큼 거대한 규모입니다.

여기서 진짜 충격적인 사실은, 이 100만 줄의 코드 중 인간이 자신의 손으로 직접 타이핑한 코드는 단 한 줄도 없다는 것입니다 [Harness Engineering: Why the Focus is Shifting from... | Epsilla Blog](https://www.epsilla.com/blogs/2026-03-12-harness-engineering). 앱의 핵심 작동 방식은 물론이고, 에러를 잡아내는 테스트 프로그램, 사용 설명서, 심지어 프로그램이 잘 돌아가는지 감시하는 도구까지 100% AI 에이전트(Agent, 사람을 대신해 특정 임무를 자율적으로 수행하는 인공지능)가 혼자서 척척 작성했습니다 [OpenAI's Agent-First Codebase Learnings | Blog](https://alexlavaee.me/blog/openai-agent-first-codebase-learnings/).

결과적으로 이 3명의 인간 엔지니어는 AI의 도움을 받아 무려 1,500번의 코드 결재(Pull Request, 작성된 코드의 업데이트를 최종 승인하는 과정)를 처리했습니다 [HarnessEngineering:LeveragingCodexinanAgent-FirstWorld](https://oss.vstorm.co/blog/harness-engineering-leveraging-codex-agent-first/). 이를 계산해 보면 인간 개발자 한 명이 하루 평균 3.5개의 굵직한 기능 업데이트를 완료하는 엄청난 생산성을 낸 것입니다 [HarnessEngineering: Why 2026's AI Edge Isn't a Bigger Model](https://thebytedive.com/ai/260411-harness-engineering-ai-edge-2026/). 이제 소프트웨어 개발의 가장 큰 걸림돌은 더 이상 '인간의 손가락이 키보드를 얼마나 빨리 치느냐'가 아닙니다. '인간이 자율형 AI를 얼마나 지혜롭게 지휘하느냐'로 게임의 규칙이 완전히 바뀐 것입니다 [HarnessEngineering: The New Job Description of... | Medium](https://medium.com/@naveenmanwani/harness-engineering-the-new-job-description-of-a-software-engineer-in-an-agent-first-world-9a5a087fab78).

## 쉽게 이해하기

도대체 어떻게 인간이 키보드 한 번 안 두드리고 이런 엄청난 일이 가능했을까요? 해답은 오픈AI가 새롭게 정립한 **'하네스 엔지니어링(Harness Engineering)'** 이라는 낯선 개념에 숨어 있습니다.

하시코프(HashiCorp)의 창립자인 미첼 하시모토(Mitchell Hashimoto)는 이미 2026년 초에 이런 현상을 겪으며 "업계에서 널리 쓰이는 용어가 있는지는 모르겠지만, 나는 이 방식을 '하네스 엔지니어링'이라고 부르게 되었다"고 말했습니다 [HarnessEngineering: From AI-Assisted to... - DEV Community](https://dev.to/seekdb/harness-engineering-from-ai-assisted-to-ai-driven-what-is-software-engineering-undergoing-l6n).

'하네스(Harness)'는 원래 말이나 개를 마차에 연결할 때 쓰는 튼튼한 고삐와 끈, 또는 암벽 등반이나 험난한 놀이기구를 탈 때 사람의 생명을 지켜주는 안전장치를 뜻합니다. AI 세계에서 하네스 엔지니어링이란, 뛰어난 능력을 가진 AI 코딩 에이전트들이 엉뚱한 코드를 짜거나 중간에 길을 잃지 않고 안전하고 효율적으로 일할 수 있도록 '실행 환경과 건축적 제약'을 튼튼하게 설계해 주는 기술을 말합니다 [HarnessEngineering: The Complete Guide to Building... | ZBuild](https://www.zbuild.io/resources/news/harness-engineering-complete-guide-ai-agent-codex-2026), [What IsHarnessEngineeringfor AIAgents? | Milvus - Milvus Blog](https://milvus.io/blog/harness-engineering-ai-agents.md).

비유하면 이렇습니다. 엄청나게 힘이 세고 똑똑하지만 아직 사람들이 다니는 도로의 규칙을 잘 모르는 경주마(AI)가 있습니다. 이 말을 타고 목적지까지 무거운 짐을 안전하게 옮기려면 튼튼한 안장과 정교하게 조종할 수 있는 고삐(하네스)가 반드시 필요하겠죠. 하네스 엔지니어는 바로 이 고삐를 정교하게 설계하고 단단히 쥐는 사람입니다. 말의 엄청난 속도와 힘(AI의 코딩 능력)을 100% 활용하면서도, 말이 절벽으로 뛰어들거나 엉뚱한 길로 새지 않도록 든든한 울타리와 안전망을 쳐주는 역할을 하는 것이죠.

오픈AI 프로젝트의 시작 역시 완벽히 AI가 주도했습니다. 2025년 8월 말, 이 거대한 프로젝트의 첫 삽을 뜬 것은 사람이 아니라 GPT-5 기반의 코덱스(Codex, 코딩에 특화된 AI) 도구였습니다 [Harnessengineering:leveragingCodexinanagent-firstworld](https://openai.com/index/harness-engineering/). 프로젝트의 초기 설정, 즉 수많은 파일을 어떻게 나눌지, 코드 작성 규칙은 무엇으로 할지 등 집짓기의 기초 공사를 AI가 기존의 우수한 템플릿을 참고하여 알아서 척척 세운 것입니다 [Harnessengineering:leveragingCodexinanagent-firstworld](https://openai.com/index/harness-engineering/).

## 현재 상황

그렇다면 실제로 이 3명의 인간 엔지니어는 5개월 동안 매일매일 무슨 일을 했을까요? 그들은 까만 모니터 화면을 띄워놓고 알 수 없는 외계어 같은 코드를 보며 골머리를 앓는 대신, 마치 건설 현장의 총괄 감독관처럼 AI와 끊임없이 대화를 나누었습니다.

업무 과정은 이렇습니다. 인간 엔지니어가 "장바구니 결제 기능이 필요해. 보안에 특별히 신경 써줘"라고 프롬프트(Prompt, AI에게 내리는 일상적인 언어 명령어)를 작성하면, AI 에이전트가 순식간에 코드를 짭니다. 그리고는 우리 인간들이 직장 상사에게 결재 서류를 올리듯, AI가 스스로 '수정 요청(Pull Request)' 문서를 정갈하게 작성해서 올립니다 [Harness engineering: leveraging Codex in an agent-first world | OpenAI](https://jessetomchak.com/2026/03/04/harness-engineering-leveraging-codex-in.html).

가장 흥미로운 부분은 바로 다음 단계입니다. AI가 짠 방대한 코드를 굳이 인간이 일일이 돋보기 보듯 검사하지 않습니다. AI는 자신이 짠 코드를 자신의 가상 컴퓨터 환경에서 스스로 먼저 꼼꼼하게 검사(로컬 리뷰)합니다. 심지어 클라우드 네트워크에 연결된 다른 AI 에이전트 동료들에게 "내 코드 좀 매섭게 평가해 줄래?"라며 추가 검사를 요청하기까지 하죠 [Harness engineering: leveraging Codex in an agent-first world | OpenAI](https://jessetomchak.com/2026/03/04/harness-engineering-leveraging-codex-in.html). 

마치 능력 있는 실무진들이 모여 벌이는 난상토론 같습니다. 다른 AI들의 날카로운 피드백을 받으면, 그것을 바탕으로 또 코드를 수정하고 다시 검사받는 과정을 거칩니다. 이 과정은 모든 AI 심사위원들이 '합격'을 외치며 만족할 때까지 끊임없이 반복됩니다. 오픈AI 팀은 이 끈질긴 자기 수정 루프를 미국 만화 심슨 가족에 나오는 엉뚱한 캐릭터의 이름을 따서 '랄프 위검 루프(Ralph Wiggum Loop)'라고 재미있게 불렀습니다 [Harness engineering: leveraging Codex in an agent-first world | OpenAI](https://jessetomchak.com/2026/03/04/harness-engineering-leveraging-codex-in.html).

물론 아직 한계점도 분명히 존재합니다. 짧고 명확한 특정 기능을 만들어내는 능력은 이미 인간의 속도와 정확도를 훌쩍 뛰어넘었지만, 여전히 아주 거대하고 오래된 복잡한 시스템 전체를 AI가 한 번에 완벽히 '이해'하는 것은 어려워합니다 [r/programming on Reddit: Harness engineering: leveraging Codex in an agent-first world](https://www.reddit.com/r/programming/comments/1r3kjqt/harness_engineering_leveraging_codex_in_an/). 즉, 지칠 줄 모르는 아주 빠르고 똑똑한 실무자는 생겼지만, 전체적인 숲을 조망하고 시스템의 큰 그림을 그려내는 통찰력은 여전히 인간 감독관의 고유한 몫으로 남아있다는 뜻입니다.

## 앞으로 어떻게 될까?

오픈AI가 당당히 공개한 이 100만 줄짜리 실험 보고서는 단순한 천재 개발자들의 무용담을 넘어, 미래의 모든 직장인들이 일하는 방식에 대한 완벽한 청사진(Blueprint)을 제시했습니다 [OpenAI’sHarnessEngineeringPost Is a Blueprint for theAgent-First...](https://medium.com/@AdithyaGiridharan/openais-harness-engineering-post-is-a-blueprint-for-the-agent-first-era-d9932851dcee). 이제 수많은 IT 전문가들은 다가올 시대에 기업의 진정한 기술력이 '얼마나 크고 비싼 AI 모델을 구매하느냐'가 아니라, '이 똑똑한 AI들이 엉뚱한 짓을 하지 않고 마음껏 뛰어놀 수 있는 하네스(안전장치 및 작업 환경)를 얼마나 섬세하게 구축하느냐'에 달려있다고 입을 모아 강조합니다 [4 Real Cases |HarnessEngineeringis... - Alibaba Cloud Community](https://www.alibabacloud.com/blog/4-real-cases-|-harness-engineering-is-becoming-the-new-moat_602970).

이러한 흐름에 발맞춰, 오픈AI는 최근 수많은 AI 코딩 에이전트들을 거대한 회사 규모에서 한꺼번에 관리하고 지휘할 수 있는 도구인 '심포니(Symphony)'의 엔지니어링 미리보기 버전을 전격 공개했습니다 [Harnessengineering:leveragingCodexinanagent-firstworld](https://www.linkedin.com/posts/davethackeray_harness-engineering-leveraging-codex-in-activity-7436346067559829504-Zz-r). 재미있게도 이 강력한 지휘 시스템은 대규모 통신망을 지연 없이 제어할 때 주로 쓰이는 엘릭서(Elixir)라는 특수 언어로 만들어졌으며, 첫 기획 단계부터 하네스 엔지니어링의 철학을 깊이 염두에 두고 철저하게 설계되었습니다 [Harnessengineering:leveragingCodexinanagent-firstworld](https://www.linkedin.com/posts/davethackeray_harness-engineering-leveraging-codex-in-activity-7436346067559829504-Zz-r).

과거 0과 1로만 이루어진 딱딱한 기계어(Assembly language)에서 파이썬(Python)처럼 인간의 일상 언어와 비슷한 쉬운 프로그래밍 언어로 넘어가는 데 꽤 오랜 시간이 걸렸듯, 이 거대한 변화가 하루아침에 전 세계의 모든 프로그래머를 일자리에서 밀어내지는 않을 것입니다 [Harnessengineering:leveragingCodexinanagent-firstworld](https://www.linkedin.com/posts/sachinkundu_harness-engineering-leveraging-codex-in-activity-7450785591908179968-4boT). 

하지만 한 가지 사실만큼은 명백합니다. 앞으로의 소프트웨어 개발자들은 컴퓨터 문법책을 달달 외워서 무작정 키보드를 두드리는 사람이 되어서는 안 됩니다. 쉴 새 없이 코드를 뱉어내는 수십, 수백 명의 AI 단원들이 불협화음을 내지 않고 아름다운 화음을 완성할 수 있도록 올바른 방향을 제시하는 '최고의 오케스트라 지휘자'가 되어야 합니다.

---

**MindTickleBytes AI의 시선**

복잡한 건축 역학이나 수학 공식을 모르더라도, 뛰어난 상상력과 훌륭한 로봇 건축가만 있다면 누구나 멋진 건물을 지을 수 있는 시대가 활짝 열렸습니다. 코딩 역시 마찬가지입니다. 까다로운 컴퓨터 문법을 외우는 일은 이제 기계의 몫으로 넘어갔습니다. 인간의 역할은 '타자 치는 사람'에서 '방향을 제시하는 감독관'으로 완전히 진화했습니다.

이제 밤을 새워가며 버그(프로그램 오류)를 잡고 기계처럼 타자를 빨리 치는 능력은 더 이상 경쟁력이 될 수 없습니다. 오히려 AI가 1초 만에 쏟아내는 수많은 결과물 속에서 진짜 우리에게 필요한 가치를 알아보고, 시스템의 허점을 날카롭게 꿰뚫어 보며, AI에게 더 창의적인 '질문'을 던질 수 있는 통찰력을 기르는 것이 인간에게 남겨진 가장 중요한 숙제입니다. 코딩 교육의 패러다임 역시 '어떻게 코드를 짤 것인가'에서 '무엇을 만들고 어떤 문제를 해결할 것인가'로 시급히 이동해야 할 때입니다. 진정한 창의성은 손끝의 타이핑이 아니라, 인간의 머릿속에서 시작되는 올바른 설계에 있다는 것을 이번 오픈AI의 실험이 완벽하게 증명해주고 있습니다.

## 참고자료
1. [Harnessengineering:leveragingCodexinanagent-firstworld](https://openai.com/index/harness-engineering/)
2. [Harness Engineering: Why the Focus is Shifting from... | Epsilla Blog](https://www.epsilla.com/blogs/2026-03-12-harness-engineering)
3. [HarnessEngineering:LeveragingCodexinanAgent-FirstWorld](https://oss.vstorm.co/blog/harness-engineering-leveraging-codex-agent-first/)
4. [Harnessengineering:leveragingCodexinanagent-firstworld](https://www.linkedin.com/posts/davethackeray_harness-engineering-leveraging-codex-in-activity-7436346067559829504-Zz-r)
5. [OpenAI’sHarnessEngineeringPost Is a Blueprint for theAgent-First...](https://medium.com/@AdithyaGiridharan/openais-harness-engineering-post-is-a-blueprint-for-the-agent-first-era-d9932851dcee)
6. [HarnessEngineering: The Complete Guide to Building... | ZBuild](https://www.zbuild.io/resources/news/harness-engineering-complete-guide-ai-agent-codex-2026)
7. [Harnessengineering:leveragingCodexinanagent-firstworld](https://www.aibrief.in/article/harness-engineering-leveraging-codex-in-an-agent-first-world)
8. [Harness engineering: leveraging Codex in an agent-first world | OpenAI](https://jessetomchak.com/2026/03/04/harness-engineering-leveraging-codex-in.html)
9. [GitHub - walkinglabs/awesome-harness-engineering: 🛠️ Awesome tools & guides for harness engineering.](https://github.com/walkinglabs/awesome-harness-engineering)
10. [Harness engineering: leveraging Codex in an agent-first world | daily.dev](https://app.daily.dev/posts/harness-engineering-leveraging-codex-in-an-agent-first-world-py6m8jwm4)
11. [OpenAI's Agent-First Codebase Learnings | Blog](https://alexlavaee.me/blog/openai-agent-first-codebase-learnings/)
12. [r/programming on Reddit: Harness engineering: leveraging Codex in an agent-first world](https://www.reddit.com/r/programming/comments/1r3kjqt/harness_engineering_leveraging_codex_in_an/)
13. [Harnessengineering:leveragingCodexinanagent-firstworld](https://www.linkedin.com/posts/sachinkundu_harness-engineering-leveraging-codex-in-activity-7450785591908179968-4boT)
14. [HarnessEngineering: Why 2026's AI Edge Isn't a Bigger Model](https://thebytedive.com/ai/260411-harness-engineering-ai-edge-2026/)
15. [HarnessEngineering: The New Job Description of... | Medium](https://medium.com/@naveenmanwani/harness-engineering-the-new-job-description-of-a-software-engineer-in-an-agent-first-world-9a5a087fab78)
16. [4 Real Cases |HarnessEngineeringis... - Alibaba Cloud Community](https://www.alibabacloud.com/blog/4-real-cases-|-harness-engineering-is-becoming-the-new-moat_602970)
17. [HarnessEngineering: From AI-Assisted to... - DEV Community](https://dev.to/seekdb/harness-engineering-from-ai-assisted-to-ai-driven-what-is-software-engineering-undergoing-l6n)
18. [What IsHarnessEngineeringfor AIAgents? | Milvus - Milvus Blog](https://milvus.io/blog/harness-engineering-ai-agents.md)