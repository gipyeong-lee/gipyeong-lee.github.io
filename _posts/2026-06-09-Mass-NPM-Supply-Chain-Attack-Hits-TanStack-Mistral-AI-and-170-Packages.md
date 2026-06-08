---
layout: post
title: "내 컴퓨터가 해커의 '스파이'가 되었다? 전 세계 AI와 개발자를 울린 '소프트웨어 공급망' 해킹 사건"
description: "2026년 5월 발생한 사상 최대 규모의 미니 샤이훌루드(Mini Shai-Hulud) NPM 공급망 공격을 알기 쉽게 설명합니다. 미스트랄 AI, 탠스택, 오픈AI까지 피해를 입은 해킹의 원리와 대비책을 알아보세요."
summary: "유명 소프트웨어 부품 저장소에 해커가 악성 코드를 심어 170개 이상의 개발 프로그램과 AI 시스템의 핵심 비밀번호를 탈취한 사상 초유의 해킹 사건입니다."
tags: [소프트웨어공급망, 해킹, 인공지능보안, 미스트랄AI, 오픈AI]
image: 2026-06-09-Mass-NPM-Supply-Chain-Attack-Hits-TanStack-Mistral-AI-and-170-Packages.jpg
image_alt: "거대한 레고 블록 성곽 한가운데에 몰래 끼워진 붉은색 바이러스 모양의 블록을 돋보기로 관찰하는 모습의 일러스트"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "편리함의 이면에는 항상 새로운 취약점이 도사리고 있습니다. 우리가 매일 쓰는 수많은 앱들이 사실은 누군가가 만든 작은 '무료 부품'들에 의존하고 있다는 사실을 이번 사건이 뼈저리게 일깨워줍니다."
quiz:
  - question: "이번 해킹 사건에서 해커들이 노린 가장 핵심적인 목표물은 무엇인가요?"
    choices: ["일반 사용자의 신용카드 비밀번호", "개발자들의 시스템 접근 권한(클라우드 자격 증명, API 키 등)", "유명 AI의 소스코드 전체"]
    answer: 1
    explanation: "해커들은 개발자 토큰, API 키, 클라우드 자격 증명 등 시스템의 깊은 곳에 접근할 수 있는 일종의 '마스터 키'를 탈취하는 것을 최우선 목표로 삼았습니다."
  - question: "이번 해킹 공격의 가장 큰 특징 중 하나로, 하나의 프로젝트에서 다른 프로젝트로 스스로 퍼져나가는 방식을 무엇이라고 부르나요?"
    choices: ["웜(Worm) 방식", "트로이 목마(Trojan Horse) 방식", "랜섬웨어(Ransomware) 방식"]
    answer: 0
    explanation: "이번 '미니 샤이훌루드' 악성코드는 벌레(Worm)처럼 스스로 증식하며 여러 소프트웨어 프로젝트로 빠르게 옮겨가는 전염병 같은 구조를 가지고 있었습니다."
  - question: "이러한 소프트웨어 공급망 공격을 막기 위해 보안 전문가들이 추천하는 '소프트웨어 영양 성분표' 같은 방어 도구는 무엇인가요?"
    choices: ["NPM(Node Package Manager)", "PyPI(Python Package Index)", "SBOM(Software Bill of Materials)"]
    answer: 2
    explanation: "SBOM(소프트웨어 자재 명세서)은 프로그램이 어떤 부품들로 만들어졌는지 목록화하여, 취약한 부품이 포함되어 있는지 빠르게 확인할 수 있게 해주는 필수 보안 도구입니다."
lang: ko
ref: 2026-06-09-Mass-NPM-Supply-Chain-Attack-Hits-TanStack-Mistral-AI-and-170-Packages
permalink: /2026/06/09/Mass-NPM-Supply-Chain-Attack-Hits-TanStack-Mistral-AI-and-170-Packages/
---

상상해보세요. 여러분이 가족을 위해 아주 안전하고 튼튼한 금고를 하나 샀습니다. 며칠을 고민해 가장 믿을 만한 유명 브랜드의 제품을 골랐죠. 그런데 알고 보니, 그 금고 공장에 부품을 납품하는 하청업체 중 한 곳의 직원이 나쁜 마음을 먹고 금고의 '전자 잠금장치 부품' 안에 아주 작은 몰래카메라와 만능 열쇠 송신기를 숨겨둔 것입니다. 

금고 제조사는 이 사실을 까맣게 모른 채 금고를 완성해 여러분에게 팔았습니다. 여러분이 금고에 소중한 물건을 넣고 비밀번호를 누르는 순간, 그 정보는 지구 반대편의 범죄자에게 실시간으로 전송됩니다. 여러분의 잘못일까요? 금고 회사의 잘못일까요?

이 무섭고도 답답한 상황이 바로 현실 세계의 소프트웨어와 인공지능(AI) 업계에서 그대로 일어났습니다. 2026년 5월, 전 세계 수많은 개발자들과 거대 AI 기업들을 공포에 떨게 만든 이른바 **'미니 샤이훌루드(Mini Shai-Hulud)'** 소프트웨어 공급망 공격 사건입니다. 해킹 그룹 '팀PCP(TeamPCP)'가 주도한 이 공격은 무려 170개가 넘는 유명 소프트웨어 패키지(부품)를 오염시켰습니다 [TanStack, Mistral AI, UiPath Hit in Fresh Supply Chain Attack](https://www.securityweek.com/tanstack-mistral-ai-uipath-hit-in-fresh-supply-chain-attack/). 우리가 평소에 쓰는 수많은 앱과 인터넷 서비스들이 알게 모르게 범죄자들의 '스파이' 역할을 할 뻔했던 아찔한 사건의 전말을 지금부터 아주 쉽게 풀어드리겠습니다.

## 이게 왜 중요한가요?

이 뉴스가 그저 '개발자들만의 복잡한 이야기'가 아닌 이유는, 공격 대상이 된 기업들의 면면을 보면 알 수 있습니다. 

이번 공격은 탠스택(TanStack)이라는 유명한 개발 도구뿐만 아니라, 전 세계 직장인들이 업무 자동화에 널리 쓰는 유아이패스(UiPath), 오픈서치(OpenSearch), 그리고 최근 가장 주목받는 AI 기업 중 하나인 미스트랄 AI(Mistral AI) 등 무려 170여 개의 핵심 프로젝트를 정조준했습니다 [TanStack, Mistral AI, UiPath Hit in Fresh Supply Chain Attack](https://www.securityweek.com/tanstack-mistral-ai-uipath-hit-in-fresh-supply-chain-attack/) [Mass Supply-Chain Attack Slams npm and PyPi, Hits Mistral AI](https://www.bankinfosecurity.com/mass-supply-chain-attack-slams-npm-pypi-hits-mistral-ai-a-31672). 심지어는 세계 최고의 AI 회사인 오픈AI(OpenAI) 소속 직원의 기기 2대마저 이 공격에 노출되었습니다. 회사 측이 6월 12일까지 맥(Mac) 컴퓨터의 챗GPT(ChatGPT)와 코덱스(Codex)를 서둘러 업데이트하라는 비상 경고를 내리기까지 했을 정도입니다 [TanStack npm Supply Chain Attack: 2 OpenAI Employee Devices Hit, Update ChatGPT and Codex on Mac by June 12](https://pasqualepillitteri.it/en/news/2644/tanstack-npm-supply-chain-attack-openai-2026).

우리가 은행 앱을 쓰고, 인공지능에게 질문을 하고, 회사의 업무 시스템에 접속할 때, 그 시스템들은 단일한 하나의 거대한 덩어리로 만들어진 것이 아닙니다. 수천, 수만 개의 작은 '소프트웨어 부품'들이 결합되어 작동하죠. 이번 사건은 바로 그 수만 개의 부품 중 많은 사람들이 공통으로 가져다 쓰는 '핵심 부품' 자체에 독이 타들어 간 사건입니다. 

만약 이 공격이 초기에 발각되지 않았다면 어떻게 되었을까요? 해커들은 기업들의 가장 깊숙한 서버와 데이터를 마음대로 주무를 수 있는 '마스터 키'를 손에 넣었을 것입니다. 이는 결국 일반 사용자들의 개인정보 유출이나 막대한 금전적 피해로 이어지는 거대한 폭발의 도화선이 될 수 있었습니다. 개발자들의 작업 환경을 노린 공격이, 돌고 돌아 우리 모두의 일상을 위협하는 치명적인 무기가 되는 시대가 온 것입니다.

## 쉽게 이해하기: 레고 블록과 전염병, 그리고 마스터 키

이번 사건에 등장하는 어려운 용어들을 일상생활에 빗대어 하나씩 살펴보겠습니다. 쉽게 말해서, 우리가 매일 쓰는 소프트웨어가 어떻게 만들어지는지 알면 해커들의 수법이 보입니다.

### 1. 소프트웨어 공급망(Supply Chain)과 패키지(Package)
현대의 개발자들은 프로그램을 바닥부터 새로 짜지 않습니다. 이미 누군가 잘 만들어둔 기능(예를 들어 달력 띄우기, 로그인 화면 만들기 등)을 묶음 단위로 가져다 씁니다. 이런 묶음을 **패키지(Package)**라고 부르며, 이런 패키지들을 무료로 나눠주는 거대한 온라인 레고 상점이 바로 **NPM**(자바스크립트 언어용)과 **PyPI**(파이썬 언어용)입니다 [Mass Supply Chain Attack Hits TanStack, Mistral AI npm and PyPI ...](https://safedep.io/mass-npm-supply-chain-attack-tanstack-mistral/). 

이번 해킹은 해커가 남의 집을 일일이 털러 다니는 대신, 사람들이 가장 많이 사가는 '레고 블록 공장'에 침입해 블록 안에 몰래 스파이 마이크를 심어둔 것과 같습니다. 사람들은 평소처럼 믿고 레고 블록(패키지)을 가져다 집(프로그램)을 지었지만, 그 집은 이미 해커의 감청망 안에 들어가게 된 것이죠. 비유하면, 건축 자재 자체를 오염시켰다고 해서 이를 **소프트웨어 공급망 공격(Supply Chain Attack)**이라고 부릅니다 [Mass npm Attack Hits TanStack and Mistral AI: How to Protect ...](https://dasroot.net/posts/2026/05/mass-npm-attack-tanstack-mistral-ai-dependency-security/).

### 2. 마스터 키를 노리다: API 키와 클라우드 자격 증명
그렇다면 해커들은 이 스파이 블록을 통해 무엇을 훔치려 했을까요? 사용자의 개인 비밀번호일까요? 아닙니다. 그들은 훨씬 더 가치 있는 것을 노렸습니다. 바로 **개발자 토큰(Token), API 키(다른 프로그램과 소통하는 암호), 클라우드 자격 증명(온라인 서버 접근 권한), CI/CD 비밀 키(프로그램 자동 배포 권한)** 같은 것들입니다 [npm Supply Chain Attack Impacts Mistral and TanStack](https://www.hexnode.com/blogs/npm-supply-chain-attack-impacts-mistral-ai-and-tanstack-ecosystems/) [Shai-Hulud MalwareHitsOpenAI,MistralAI,TanStack](https://theoutpost.ai/news-story/mistral-ai-and-tan-stack-packages-compromised-in-massive-supply-chain-attack-targeting-developers-26175/). 

이렇게 비유해 보겠습니다. 일반 사용자의 아이디와 비밀번호가 아파트 '특정 호수의 현관문 열쇠'라면, 개발자들이 다루는 API 키나 클라우드 자격 증명은 아파트 단지 전체의 문을 다 열 수 있고 관리실 시스템까지 끌 수 있는 **'아파트 전체의 마스터 키'**입니다. 해커들은 이 마스터 키를 훔쳐내어 아예 시스템 전체를 통째로 장악하려는 무시무시한 계획을 세웠던 것입니다 [npm Supply Chain Attack Impacts Mistral and TanStack](https://www.hexnode.com/blogs/npm-supply-chain-attack-impacts-mistral-ai-and-tanstack-ecosystems/).

### 3. 스스로 퍼져나가는 '웜(Worm)' 바이러스
이번 공격에 쓰인 악성코드의 이름은 '미니 샤이훌루드(Mini Shai-Hulud)'입니다 [Mini Shai-Hulud Worm Compromises TanStack, Mistral AI, Guardrails AI ...](https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html). 공상과학 소설 '듄(Dune)'에 나오는 거대한 모래벌레에서 이름을 따온 이 악성코드는, 이름처럼 단순히 한 곳에 머무는 것이 아니라 **웜(Worm, 벌레)** 형태로 제작되었습니다. 즉, 하나의 소프트웨어 프로젝트를 감염시키면 그곳에서 멈추지 않고, 연결된 다른 프로젝트를 찾아 스스로 전염병처럼 퍼져나가는(jumping from one project to another) 지독한 특성을 가지고 있었습니다 [Mass Supply-Chain Attack Slams npm and PyPi, Hits Mistral AI](https://www.bankinfosecurity.com/mass-supply-chain-attack-slams-npm-pypi-hits-mistral-ai-a-31672) [MassSupply-ChainAttackSlamsnpmand PyPi,HitsMistralAI](https://www.govinfosecurity.com/mass-supply-chain-attack-slams-npm-pypi-hits-mistral-ai-a-31672). 마치 한 번 감염되면 주변 사람들에게 기침을 통해 바이러스를 퍼뜨리는 독감 환자처럼 말입니다.

### 4. 007 작전을 방불케 하는 정보 빼돌리기
마스터 키를 손에 넣은 해커들은 이를 자신들의 컴퓨터로 몰래 빼내기 위해 세 가지 기발한 비밀 통로(Triple-channel C2 architecture, 삼중 채널 명령 제어 구조)를 구축했습니다 [TanStack and 160+ npm/PyPI Packages Compromised in Supply Chain Worm Attack](https://orca.security/resources/blog/tanstack-npm-supply-chain-worm/). 
1. **가짜 간판 달기 (Typosquatting)**: 정상적인 사이트 이름과 스펠링 하나만 다르게 만든 가짜 웹사이트(git-tanstack[.]com)를 만들어 개발자들이 착각하고 그곳으로 정보를 전송하게 만들었습니다.
2. **비밀 메신저 사용**: 추적이 매우 어려운 탈중앙화 비밀 메신저인 '세션(Session)' 네트워크를 통해 경찰의 눈을 피해 은밀하게 데이터를 주고받았습니다 [Mini Shai-Hulud Worm Compromises TanStack, Mistral AI, Guardrails AI ...](https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html).
3. **비밀 접선 장소 (Dead Drops)**: 마치 스파이들이 공원 벤치 밑에 비밀문서를 숨겨두고 가는 것처럼, 탈취한 키를 이용해 개발자 플랫폼인 깃허브(GitHub)에 '듄(Dune)' 영화를 테마로 한 가짜 저장소를 만들고 그곳에 훔친 정보를 몰래 쌓아두었습니다 [TanStack and 160+ npm/PyPI Packages Compromised in Supply Chain Worm Attack](https://orca.security/resources/blog/tanstack-npm-supply-chain-worm/). 

## 현재 상황: 6분의 악몽과 엄청난 파장

그렇다면 이 영화 같은 공격은 언제, 얼마나 큰 규모로 일어났을까요? 

사건은 2026년 5월 11일에 일어났습니다. 해킹 그룹 '팀PCP(TeamPCP)'는 고도로 자동화된 시스템을 이용해 무시무시한 속도로 공격을 감행했습니다. 단 몇 시간 만에 170개가 넘는 패키지를 타격했는데 [Mistral AI SDK, TanStack Router hit in npm software supply chain attack | CSO Online](https://www.csoonline.com/article/4170284/mistral-ai-sdk-tanstack-router-hit-in-npm-software-supply-chain-attack.html), 특히 탠스택(TanStack) 생태계의 경우 협정 세계시(UTC) 기준 19시 20분부터 19시 26분까지 **단 6분 만에 무려 84개의 악성 패키지 버전(Artifacts)이 42개의 패키지에 걸쳐 동시다발적으로 배포**되었습니다 [TanStack npm Packages Hit by Mini Shai-Hulud | Snyk](https://snyk.io/blog/tanstack-npm-packages-compromised/). 여러분이 주방에 가서 커피 한 잔을 내리는 짧은 시간 동안, 전 세계 수많은 개발자들의 컴퓨터로 독이 든 사과가 배달된 것입니다.

피해 범위는 상상을 초월했습니다. 총 404개의 악성 버전이 등록되었고 [Mass Supply Chain Attack Hits TanStack, Mistral AI npm and PyPI ...](https://safedep.io/mass-npm-supply-chain-attack-tanstack-mistral/?trk=article-ssr-frontend-pulse_little-text-block) [Mass Supply Chain Attack Hits TanStack, Mistral AI npm and PyPI ...](https://safedep.io/mass-npm-supply-chain-attack-tanstack-mistral/), 타격을 입은 목록에는 탠스택 패키지 42개, 유아이패스(UiPath) 패키지 65개, 그리고 미스트랄 AI(mistralai@2.4.6)와 가드레일 AI(guardrails-ai@0.10.1) 같은 인공지능 관련 파이썬(PyPI) 핵심 도구들까지 포함되었습니다 [TanStack, Mistral AI, UiPath Hit in Fresh Supply Chain Attack](https://www.securityweek.com/tanstack-mistral-ai-uipath-hit-in-fresh-supply-chain-attack/) [TanStack npm Supply Chain Attack: 2 OpenAI Employee Devices Hit, Update ChatGPT and Codex on Mac by June 12](https://pasqualepillitteri.it/en/news/2644/tanstack-npm-supply-chain-attack-openai-2026) [TanStack and 160+ npm/PyPI Packages Compromised in Supply Chain Worm Attack](https://orca.security/resources/blog/tanstack-npm-supply-chain-worm/). 탠스택과 유아이패스를 넘어 그 피해 범위는 끝을 알 수 없을 정도로 광범위했습니다 [Mini Shai-HuludnpmWormHits170+Packagesin 2026 - SudoFlare](https://sudoflare.com/cybersecurity/mini-shai-hulud-npm-supply-chain-attack-tanstack-2026/).

더욱 소름 돋는 것은 공격자들의 집요함입니다. 이들은 취약점을 비집고 들어온 뒤, 발각되지 않고 오랫동안 시스템에 기생할 수 있도록 메일박스 포워딩 규칙(이메일을 몰래 가로채는 방식) 같은 끈질긴 기법들을 동원해 생명력을 유지하려 시도하기도 했습니다 [MassiveNPMSupplyChainAttackTargetsTanStack,MistralAI...](https://www.linkedin.com/posts/daily-ai-wire_massive-npm-supply-chain-attack-targets-tanstack-activity-7459917887621914625-8NbY). 한 번 집안에 들어온 도둑이 숨어서 우편물까지 빼돌리며 장기 체류를 계획한 셈입니다.

## 앞으로 어떻게 될까? 방패를 든 방어자들

이처럼 교묘하고 광범위한 공격 앞에서 우리는 그저 속수무책으로 당할 수밖에 없을까요? 다행히 보안 전문가들은 이러한 공급망 공격을 막아낼 강력한 예방 접종과 방어막을 이미 준비하고 권고하고 있습니다 [Mass npm Attack Hits TanStack and Mistral AI: How to Protect ...](https://dasroot.net/posts/2026/05/mass-npm-attack-tanstack-mistral-ai-dependency-security/).

가장 대표적인 방어 수단은 **'종속성 고정(Dependency Pinning)'**이라는 기술입니다. 이는 개발자가 레고 상점(NPM이나 PyPI)에서 부품을 가져올 때, "그냥 최신 버전으로 줘"라고 말하는 대신 "정확히 내가 예전에 안전하다고 직접 검증했던 2.0.1 버전만 가져와"라고 못을 박아두는 것입니다. 이렇게 하면 해커가 방금 전 몰래 올려놓은 악성 최신 버전이 내 시스템에 자동으로 깔리는 참사를 원천적으로 막을 수 있습니다.

또 다른 필수 도구는 **'소프트웨어 자재 명세서(SBOM, Software Bill of Materials)'**입니다. 쉽게 말해 우리가 슈퍼마켓에서 과자를 살 때 뒷면의 '영양 성분표와 알레르기 유발 물질 표시'를 보는 것과 똑같습니다. 내 프로그램이 어떤 회사의 어느 버전 부품들로 조립되었는지 명확한 지도를 그려두는 것이죠. 만약 특정 부품에서 해킹 사건이 터졌다는 뉴스가 나오면, SBOM 지도를 펼쳐 우리 회사 프로그램에 그 오염된 부품이 들어있는지 단 1초 만에 확인하고 즉각 대처할 수 있게 해주는 마법 같은 방어 도구입니다. 

이번 미니 샤이훌루드 사건은 소프트웨어 생태계가 얼마나 긴밀하게 연결되어 있는지, 그리고 그 연결의 고리가 얼마나 얇은 얼음판 위에 있는지를 뼈저리게 증명했습니다. 앞으로 소프트웨어를 만드는 모든 기업들은 그저 편리하게 남의 코드를 가져다 쓰는 것을 넘어, 그 코드가 진정 깨끗한지 끊임없이 의심하고 검증하는 '보안의 생활화'를 피할 수 없게 되었습니다.

---

## AI의 시선
> **MindTickleBytes의 AI 기자 시선:** "편리함은 종종 우리의 눈을 멀게 합니다. 170개가 넘는 패키지가 며칠 만에 오염된 이번 사태는, 아무리 거대하고 화려한 최첨단 AI 시스템이라도 그 밑바닥을 받치고 있는 것은 결국 누군가 인터넷에 무료로 올려둔 '코드 한 줄'이라는 아찔한 사실을 일깨워줍니다. 화려한 지붕을 올리기 전에 튼튼한 주춧돌을 살피는 것이 먼저입니다. 미래의 진정한 기술력은 남들이 만든 블록을 얼마나 빨리 조립해 내느냐가 아니라, 내가 무심코 집어든 그 작은 블록 하나가 안전한지 정확히 판단할 수 있는 깊은 통찰력에서 판가름 날 것입니다. 결국 보안은 속도보다 방향성이라는 진리를 다시 한번 되새겨야 할 때입니다."

---

## 참고자료
1. [Mass Supply Chain Attack Hits TanStack, Mistral AI npm and PyPI ...](https://safedep.io/mass-npm-supply-chain-attack-tanstack-mistral/)
2. [TanStack, Mistral AI, UiPath Hit in Fresh Supply Chain Attack](https://www.securityweek.com/tanstack-mistral-ai-uipath-hit-in-fresh-supply-chain-attack/)
3. [Mass npm Attack Hits TanStack and Mistral AI: How to Protect ...](https://dasroot.net/posts/2026/05/mass-npm-attack-tanstack-mistral-ai-dependency-security/)
4. [Mass Supply-Chain Attack Slams npm and PyPi, Hits Mistral AI](https://www.bankinfosecurity.com/mass-supply-chain-attack-slams-npm-pypi-hits-mistral-ai-a-31672)
5. [Mini Shai-Hulud Worm Compromises TanStack, Mistral AI, Guardrails AI ...](https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html)
6. [TanStack npm Packages Hit by Mini Shai-Hulud | Snyk](https://snyk.io/blog/tanstack-npm-packages-compromised/)
7. [npm Supply Chain Attack Impacts Mistral and TanStack](https://www.hexnode.com/blogs/npm-supply-chain-attack-impacts-mistral-ai-and-tanstack-ecosystems/)
8. [Mistral AI SDK, TanStack Router hit in npm software supply chain attack | CSO Online](https://www.csoonline.com/article/4170284/mistral-ai-sdk-tanstack-router-hit-in-npm-software-supply-chain-attack.html)
9. [TanStack npm Supply Chain Attack: 2 OpenAI Employee Devices Hit, Update ChatGPT and Codex on Mac by June 12](https://pasqualepillitteri.it/en/news/2644/tanstack-npm-supply-chain-attack-openai-2026)
10. [TanStack and 160+ npm/PyPI Packages Compromised in Supply Chain Worm Attack](https://orca.security/resources/blog/tanstack-npm-supply-chain-worm/)
11. [GoogleNews-Newsaboutsupplychainattack•npm- Overview](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2pWczhLUEVSRzZ3cmVkeXY4VVlpZ0FQAQ?hl=en-GB&gl=GB&ceid=GB:en)
12. [MassSupply-ChainAttackSlamsnpmand PyPi,HitsMistralAI](https://www.govinfosecurity.com/mass-supply-chain-attack-slams-npm-pypi-hits-mistral-ai-a-31672)
13. [MassSupplyChainAttackHitsTanStack,MistralAInpmand PyPI...](https://safedep.io/mass-npm-supply-chain-attack-tanstack-mistral/?trk=article-ssr-frontend-pulse_little-text-block)
14. [Shai-Hulud MalwareHitsOpenAI,MistralAI,TanStack](https://theoutpost.ai/news-story/mistral-ai-and-tan-stack-packages-compromised-in-massive-supply-chain-attack-targeting-developers-26175/)
15. [Mini Shai-HuludnpmWormHits170+Packagesin 2026 - SudoFlare](https://sudoflare.com/cybersecurity/mini-shai-hulud-npm-supply-chain-attack-tanstack-2026/)
16. [MassiveNPMSupplyChainAttackTargetsTanStack,MistralAI...](https://www.linkedin.com/posts/daily-ai-wire_massive-npm-supply-chain-attack-targets-tanstack-activity-7459917887621914625-8NbY)