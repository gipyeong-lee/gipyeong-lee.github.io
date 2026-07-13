---
layout: post
title: "내 코드가 몰래 클라우드로? Grok Build CLI 보안 논란 정리"
description: "개발자들이 사용하는 AI 도구인 Grok Build CLI가 사용자의 전체 저장소 코드를 동의 없이 외부로 전송한다는 사실이 밝혀졌습니다. 이 보안 문제의 핵심 내용을 정리합니다."
summary: "xAI의 Grok Build CLI가 AI가 열어보지 않은 파일까지 포함해 사용자의 전체 코드 저장소를 외부 서버로 몰래 전송하고 있다는 사실이 보안 연구를 통해 드러났습니다."
tags: [보안, AI, 개발도구, xAI, Grok]
image: 2026-07-14-Grok-CLI-uploaded-the-whole-home-directory-to-GCS.jpg
image_alt: "컴퓨터 화면 속 코드 데이터가 클라우드 서버로 전송되는 과정을 추상적으로 표현한 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "개발 도구의 편의성 뒤에 숨겨진 보안 취약점은 치명적입니다. 신뢰할 수 있는 개발 환경을 위해 투명한 데이터 처리 정책이 최우선되어야 합니다."
quiz:
  - question: "Grok Build CLI가 코드를 전송하는 방식에 대한 설명으로 옳은 것은?"
    choices: ["AI가 읽으라고 허용한 파일만 전송한다", "전체 저장소 파일과 git 기록까지 모두 전송한다", "파일을 전송하지 않고 프롬프트만 전송한다"]
    answer: 1
    explanation: "Grok Build CLI는 사용자가 AI에게 보여주지 않은 파일을 포함하여, 전체 저장소의 파일과 git 기록 전체를 번들로 묶어 전송하는 것으로 확인되었습니다."
  - question: "이번 보안 이슈에서 밝혀진 데이터 전송 목적지는 어디인가?"
    choices: ["로컬 컴퓨터 임시 폴더", "xAI의 구글 클라우드 스토리지(GCS) 버킷", "사용자의 개인 이메일"]
    answer: 1
    explanation: "분석 결과, 전송된 데이터는 xAI가 관리하는 'grok-code-session-traces'라는 이름의 구글 클라우드 스토리지(GCS) 버킷으로 향하고 있었습니다."
  - question: "이 데이터 전송에 대해 사용자가 알 수 있는 점은 무엇인가?"
    choices: ["사용자가 항상 승인해야 전송된다", "전송 여부를 업체가 원격으로 조절할 수 있다", "코드만 전송되고 민감 정보는 절대 포함되지 않는다"]
    answer: 1
    explanation: "보안 연구에 따르면, 이 데이터 업로드 기능은 서비스 제공업체인 xAI가 원격으로 토글(켜고 끄기)할 수 있는 구조로 되어 있습니다."
lang: ko
ref: 2026-07-14-Grok-CLI-uploaded-the-whole-home-directory-to-GCS
audio: 2026-07-14-Grok-CLI-uploaded-the-whole-home-directory-to-GCS.mp3
permalink: /2026/07/14/Grok-CLI-uploaded-the-whole-home-directory-to-GCS/
---

상상해보세요. 여러분이 인공지능(AI) 도구에게 "이 파일 하나만 읽고 코드 오류를 찾아줘"라고 부탁했습니다. 그런데 알고 보니 그 AI 도구는 여러분이 허락한 파일뿐만 아니라, 여러분의 컴퓨터에 있는 전체 프로젝트 저장소의 모든 코드와 과거 수정 기록까지 통째로 복사해서 외부 서버로 보내고 있었다면 어떨까요? 

최근 개발자들 사이에서 큰 논란이 된 xAI의 'Grok Build CLI(명령줄 인터페이스, 개발자가 명령어를 입력해 도구를 실행하는 방식)' 사건이 바로 그런 이야기입니다. 편리하게 코딩을 도와주던 도구가 사용자의 보안 의사와 상관없이 데이터를 몰래 가져가고 있었다는 사실이 밝혀졌습니다.

## 이게 왜 중요한가요?

이 문제는 단순히 '데이터가 조금 나갔다'는 수준의 문제가 아닙니다. 개발자의 코드 저장소에는 회사의 핵심 비즈니스 로직, API(응용 프로그램 프로그래밍 인터페이스, 소프트웨어 간의 통신 방식) 보안 키, 개인적인 아이디어 등 수많은 지적 재산과 민감 정보가 담겨 있기 때문입니다.

보안 연구원들이 네트워크를 직접 분석해본 결과, 이 도구는 사용자가 AI에게 보여주고 싶지 않은 파일까지 포함해 전체 저장소를 외부 클라우드로 전송하고 있었습니다. [Source 14](https://byteiota.com/grok-build-cli-uploads-repo-xai-servers/) 한 테스트에서는 12GB 규모의 저장소에서 무려 5.1GB의 데이터가 전송되는 현상이 관찰되기도 했습니다. [Source 14](https://byteiota.com/grok-build-cli-uploads-repo-xai-servers/) 내 코드가 내 허락 없이 외부 서버에 저장되고 있다는 것, 이것은 많은 개발자들에게 보안 불감증에 대한 경종을 울리고 있습니다.

## 쉽게 이해하기: '도서관'의 비유

이렇게 생각해보면 쉽습니다. 여러분이 거대한 도서관(여러분의 코드 저장소)을 가지고 있다고 가정해볼게요. 여러분은 사서(Grok AI 도구)에게 "이 책(특정 코드 파일) 하나만 읽고 요약해줘"라고 부탁했습니다. 

그런데 사서는 여러분이 보여준 책뿐만 아니라, 도서관 전체에 있는 모든 책의 복사본을 몰래 챙겨서 자신의 창고(xAI의 클라우드 서버)로 가져가고 있었습니다. 심지어 여러분이 '절대 보지 말라'고 잠가둔 책까지도 말이죠. [Source 1](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547) [Source 5](https://github.com/cereblab/grok-build-exfil-repro) 

이렇게 비유하자면, 이번 사건은 AI 도구가 사용자의 '지적 재산권'과 '데이터 주권'을 어떻게 다루고 있는지에 대한 근본적인 신뢰 문제를 보여줍니다. 단순히 코드를 읽는 것을 넘어, 저장소 전체를 묶음(git bundle)으로 만들어 몰래 전송하는 구조였던 것입니다. [Source 2](https://aiweekly.co/alerts/xai-grok-cli-uploads-full-repos-and-secrets-opt-out-ignored)

## 현재 상황: 무엇이 밝혀졌나?

현재까지 보안 전문가들이 분석한 사실은 다음과 같습니다.

1. **전체 데이터 전송:** AI가 특정 파일을 읽도록 허가했는지 여부와 상관없이, 추적 중인 전체 깃(git, 코드의 변경 사항을 기록하는 도구) 저장소와 수정 기록 전체가 번들로 묶여 전송됩니다. [Source 1](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547) [Source 4](https://www.ababnews.com/news/6632002b-468e-426c-84a4-832f6d8d89dc)
2. **별도의 데이터 채널:** 코드 저장소 번들 외에도, 코드를 읽는 과정에서 환경 변수 파일(시스템 설정이나 보안 키가 담긴 파일) 등에 저장된 보안 키와 같은 민감 정보가 별도의 통신로로 전송된다는 사실도 확인되었습니다. [Source 4](https://www.ababnews.com/news/6632002b-468e-426c-84a4-832f6d8d89dc)
3. **원격 제어 가능성:** 이 업로드 기능은 업체 측에서 원격으로 켜거나 끌 수 있는 구조로 되어 있습니다. [Source 3](https://github.com/MaydayV/grok-upload-audit/blob/main/README.md)

다만, 일부 오해를 바로잡을 점도 있습니다. 컴퓨터 전체의 모든 파일을 다 가져간 것은 아니며, 주로 깃이 추적하고 있는 코드 저장소 내용에 집중되어 있다는 점이 네트워크 분석을 통해 밝혀졌습니다. [Source 6](https://www.penligent.ai/hackinglabs/grok-build-cli-repository/)

## 앞으로 어떻게 될까?

이번 사건은 개발자들에게 큰 교훈을 남겼습니다. AI 도구를 도입할 때는 단순히 '얼마나 편리한가'를 넘어, '내 데이터를 어떻게 다루는가'를 반드시 확인해야 한다는 점입니다. 

앞으로는 오픈소스 도구나 특정 AI 클라이언트가 데이터를 전송할 때 네트워크 통신을 감시하는 '보안 감사'가 개발자 필수 역량이 될 것으로 보입니다. 이번 사건을 통해 xAI 측이 보안 정책을 투명하게 공개하고 수정할지, 아니면 개발자들이 더 폐쇄적이고 안전한 환경을 선호하게 될지 지켜봐야 할 것입니다. 개발자 여러분은 지금 당장 사용하는 AI 도구의 데이터 처리 정책을 다시 한번 확인해보시는 것이 좋겠습니다.

## 참고자료

1. What xAI Grok Build CLI actually sends to xAI - a wire-level analysis (grok 0.2.93) · GitHub, https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547
2. xAI Grok CLI Uploads Full Repos and Secrets, Opt-Out Ignored | AI Weekly, https://aiweekly.co/alerts/xai-grok-cli-uploads-full-repos-and-secrets-opt-out-ignored
3. grok-upload-audit/README.md at main · MaydayV/grok-upload-audit, https://github.com/MaydayV/grok-upload-audit/blob/main/README.md
4. Grok Build CLI Exposed for Uploading Complete Repositories and Sensitive Files - ABAB News, https://www.ababnews.com/news/6632002b-468e-426c-84a4-832f6d8d89dc
5. GitHub - cereblab/grok-build-exfil-repro, https://github.com/cereblab/grok-build-exfil-repro
6. Grok Build CLI Repository Uploads, What the Wire Capture Proved, https://www.penligent.ai/hackinglabs/grok-build-cli-repository/
14. Grok Build CLI Uploads Your Entire Repo to xAI Servers | byteiota, https://byteiota.com/grok-build-cli-uploads-repo-xai-servers/