---
layout: post
title: "마이크로소프트 공식 AI 패키지에 숨어든 비밀 스파이 사건: 무슨 일이 있었던 걸까요?"
description: "마이크로소프트의 공식 파이썬 패키지인 'agent-framework'가 해킹되어 사용자 인증 정보를 탈취한 공급망 공격 사건의 전말과 대응 방법을 쉽게 알아봅니다."
summary: "2026년 11월 17일, 마이크로소프트의 공식 파이썬 패키지 'agent-framework'에 비밀 스파이 역할을 하는 악성 코드가 심어졌습니다. 다운로드만 해도 실행되는 이 공격의 정체와 우리가 알아야 할 보안 상식을 정리합니다."
tags: [보안, 파이썬, 공급망공격, 마이크로소프트, AI]
image: 2026-11-18-Microsofts-agent-framework-PyPI-package-Compromised-with-Credential-Stealer.jpg
image_alt: "디지털 보안을 상징하는 자물쇠와 파이썬 코드 화면이 어우러진 일러스트"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "개발자만을 위한 이야기처럼 보이지만, 현대 디지털 서비스의 신뢰가 얼마나 쉽게 흔들릴 수 있는지 보여주는 중요한 사건입니다. 투명하고 철저한 공급망 검증 체계가 그 어느 때보다 절실합니다."
quiz:
  - question: "이번에 공격을 받은 마이크로소프트의 파이썬 패키지 이름은 무엇인가요?"
    choices: ["agent-framework", "azure-sdk", "microsoft-ai-tools"]
    answer: 0
    explanation: "마이크로소프트의 공식 파이썬 메타패키지인 'agent-framework'가 타겟이 되었습니다."
  - question: "악성 코드가 실행되기 위해 사용자가 패키지를 직접 import(호출)해야 했나요?"
    choices: ["네, 반드시 코드로 불러와야 실행되었습니다.", "아니요, 파이썬이 시작되거나 설치될 때 자동으로 실행되었습니다.", "스마트폰 앱을 켤 때만 실행되었습니다."]
    answer: 1
    explanation: "`.pth` 시작 훅(startup hook)을 사용하여 패키지를 임포트하지 않아도 파이썬이 실행되거나 설치될 때 자동으로 작동했습니다."
  - question: "이번 사건 이후 전문가들이 권장하는 즉각적인 대응 조치는 무엇인가요?"
    choices: ["컴퓨터 포맷 및 재설치", "버전 1.26.0으로 고정(Pinning) 및 주요 비밀번호·시크릿 교체", "마이크로소프트 계정 탈퇴"]
    answer: 1
    explanation: "안전한 버전인 1.26.0으로 버전을 고정하고, Azure 및 GitHub Actions 등의 시크릿을 교체(Rotate)할 것이 권장되었습니다."
lang: ko
ref: 2026-11-18-Microsofts-agent-framework-PyPI-package-Compromised-with-Credential-Stealer
audio: 2026-11-18-Microsofts-agent-framework-PyPI-package-Compromised-with-Credential-Stealer.mp3
permalink: /2026/11/18/Microsofts-agent-framework-PyPI-package-Compromised-with-Credential-Stealer/
---

상상해보세요. 평소에 믿고 자주 쓰던 유명 대기업의 요리 재료 키트를 배송받았습니다. 박스를 뜯어 가만히 식탁 위에 올려두기만 했는데, 집안의 비밀 금고 열쇠와 현관 비밀번호가 적힌 메모가 누군가에게 몰래 전송되었다면 어떨까요? 비록 요리를 시작하지도 않았고 재료를 뜯지도 않았는데 말이죠.

소프트웨어 개발 세계에서도 이와 비슷한 일이 실제로 일어났습니다. 글로벌 빅테크 기업인 마이크로소프트(Microsoft)가 제공하는 공식 도구 상자에 누군가 몰래 '정보 도둑'을 심어놓은 것입니다 [Source 18]. 전 세계 수많은 개발자들이 깜짝 놀랐던 이 보안 사건의 전말을 아주 쉽게 풀어보겠습니다.

---

## 이게 왜 중요한가요?

우리가 스마트폰으로 앱을 사용할 때 애플 앱스토어나 구글 플레이스토어에서 안전성 검증을 거친 앱을 다운로드하듯, 프로그래머들도 수많은 오픈소스 도구를 가져다 쓰며 프로그램을 만듭니다. 이때 개발자들이 사용하는 파이썬(Python)이라는 프로그래밍 언어의 공식 소프트웨어 저장소인 파이썬 패키지 색인(PyPI, Python Package Index)에 등록된 마이크로소프트의 공식 패키지 **'agent-framework'**에 악성 코드가 숨겨지는 사건이 발생했습니다 [Source 3, Source 18].

비유하자면, 전 세계 수많은 요식업 체인점이 공동으로 사용하는 핵심 식자재 유통망에 누군가 불순물을 섞은 것과 같습니다. 이 패키지는 매월 무려 20만 번 가까이 다운로드될 정도로 전 세계 개발 현장에서 널리 쓰이는 중요한 도구입니다 [Source 3]. 이 도구를 사용하는 기업이나 개발자의 컴퓨터, 그리고 자동화 서버(CI/CD 환경, 지속적 통합 및 배포 환경)에 악성 코드가 포함된 버전이 설치되는 순간, 클라우드 서비스 접근 권한이나 비밀 키 같은 민감한 정보들이 통째로 털릴 수 있는 아찔한 상황이 벌어졌습니다 [Source 17, Source 18]. 개발자 개인의 단순한 실수를 넘어, 그들이 만든 서비스를 이용하는 수많은 일반 사용자의 디지털 안전까지 위협받을 수 있는 중대한 공급망 보안 사고였습니다.

---

## 쉽게 이해하기: 택배 상자에 숨어든 초소형 스파이

소프트웨어 공급망 공격(Supply Chain Attack)은 믿을 수 있는 대형 유통업체의 배송 차량을 가로채어, 정품 상자 안에 아주 정교하게 위장한 도청 장치를 몰래 집어넣는 것과 같습니다. 

쉽게 말해서, 이번 사건의 작동 방식을 일상적인 비유로 풀어보면 이렇습니다.
1. **신뢰의 함정**: 개발자들은 마이크로소프트라는 브랜드의 신뢰성과 공식 저장소를 믿고 평소처럼 필요한 도구를 다운로드(`pip install` 명령을 통한 설치)했습니다 [Source 18].
2. **보이지 않는 잠입**: 보통 악성 코드는 프로그램을 직접 실행하거나 특정 기능을 호출할 때 작동하기 마련입니다. 하지만 이번 악성 코드는 `.pth` 파일이라는 파이썬의 시작 훅(startup hook, 프로그램이 시작될 때 자동으로 코드를 실행시키는 기술)을 이용했습니다 [Source 7, Source 18]. 이는 마치 택배 상자를 열어보지도 않고 방에 들여놓기만 해도 자동으로 작동하는 초소형 도청기와 같아서, 개발자가 이 패키지를 코드 내에서 직접 불러와 쓰지(import) 않고 단순 설치만 해도 파이썬 환경에서 자동으로 실행되었습니다 [Source 18].
3. **비밀 정보 유출**: 이렇게 몰래 깨어난 스파이 프로그램은 컴퓨터 환경 변수나 중요 설정 파일에 저장된 비밀번호, 그리고 클라우드 제어 권한(애저 데브옵스 Azure DevOps, 애저 매니지드 아이덴티티 Azure managed identity, 깃허브 액션즈 시크릿 GitHub Actions secrets 등)을 싹 긁어모아 공격자의 외부 서버로 웹훅(webhook, 웹 기반 알림 서비스)을 통해 순식간에 전송했습니다 [Source 7, Source 17, Source 18].

---

## 현재 상황과 사건의 전말

보안 업계와 외신 보도에 따르면, 이 치밀한 공급망 침해 사건은 2026년 11월 17일에 발생했습니다 [Source 3]. 

- **발생 시각과 버전**: 마이크로소프트의 공식 메타패키지인 `agent-framework`의 **버전 1.26.1**과 **1.26.2**가 단 33분 간격으로 차례차례 PyPI에 등록되었습니다 [Source 3, Source 16, Source 18]. 이 두 버전 안에는 사용자의 인증 정보를 은밀하게 가로채는 크리덴셜 스틸러(credential stealer, 인증 정보 탈취 악성코드)가 숨어 있었습니다 [Source 3].
- **신속한 대응**: 다행히 글로벌 보안 전문가들과 자동화 모니터링 시스템의 빠른 감지 덕분에, 두 개의 악성 파일은 세상에 나타난 지 불과 45분 만에 마이크로소프트와 저장소 운영진에 의해 긴급 격리 및 삭제 조치되었습니다 [Source 3, Source 16].
- **피해 범위 및 타겟**: 이 악성 코드는 특히 클라우드 인프라 환경에서 널리 쓰이는 Azure 관련 인증 정보와 GitHub Actions의 자동화 비밀 시크릿들을 집중적으로 겨냥했습니다 [Source 7, Source 17, Source 18].

---

## 앞으로 어떻게 될까? (안전한 대응 방법)

이처럼 눈 깜짝할 사이에 일어난 공급망 공격은 우리에게 '디지털 세상에서는 아무도 100% 맹신할 수 없다'는 보안의 철칙을 다시 한번 뼈저리게 일깨워줍니다. 만약 이 시기에 해당 패키지를 다루었던 개발자나 기업이라면 즉시 다음과 같은 대응 조치를 취해야 합니다 [Source 7]:

1. **버전 고정(Pinning)**: 문제가 된 취약 버전들을 철저히 피하고, 안전성이 검증된 이전 버전인 **1.26.0**으로 버전을 확실하게 고정해야 합니다 [Source 7].
2. **시크릿 전면 교체(Rotation)**: 만약 악성 버전이 포함된 개발 환경에서 패키지를 설치한 적이 단 한 번이라도 있다면, 혹시 모를 유출 사고에 대비해 Azure 관련 자격 증명과 GitHub Actions 시크릿을 즉시 새로운 값으로 교체(Rotate)해야 합니다 [Source 7].
3. **공급망 모니터링 강화**: 단순히 유명 오픈소스 패키지라고 방심하지 않고, 자동화 개발 파이프라인(CI/CD) 전 과정에서 패키지의 무결성을 실시간으로 검증하는 고도화된 보안 솔루션을 도입하는 움직임이 전 세계적으로 더욱 가속화될 전망입니다.

---

## AI의 시선

개발자들만의 문제로 치부하기 쉽지만, 이 사건은 현대 디지털 사회가 얼마나 복잡하게 연결된 신뢰 기반 위에 서 있는지 보여주는 대표적인 단면입니다. 우리가 매일 사용하는 스마트폰 앱, 웹 서비스, 클라우드 시스템의 뒤편에는 수천 개의 오픈소스 패키지가 거미줄처럼 얽혀 있습니다. 하나의 작은 나사못(패키지)이 흔들리면 거대한 빌딩(서비스) 전체가 위협받을 수 있는 셈입니다. 앞으로는 코드를 작성하는 능력만큼이나, 우리가 가져다 쓰는 도구의 신뢰성을 투명하고 철저하게 검증하는 공급망 보안 체계가 그 어느 때보다 절실한 시대가 되었습니다.

---

## 참고자료

1. [Microsoft's agent-framework PyPI package Compromised with Credential Stealer](https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer) [Source 1]
2. [Secure PyPI Packages - 16K+ Projects From PyPI](https://www.bing.com/aclick?ld=e8MGxqEwIckNRkofSDE9RZSzVUCUyhyXQCO9oiZ32AYVUcUCdcy_8e_QkCWirnWclBVub227fMt1Iuf2-P6lDskhNij9dIiDNkedC4XdnJP9wL2_LmCVh66uI5MiHE9AYc_t7-cA48zWJAibzw_Sdeur1Rkvj3S5WDklw4rqi-TldMjbUNm2GDN3O9sU5mzhn5oCppHVAfmiRkciJcmY42dYa4tMo&u=aHR0cHMlM2ElMmYlMmZ3d3cuY2hhaW5ndWFyZC5kZXYlMmZwcm9kdWN0cyUyZmxpYnJhcmllcyUyZnB5dGhvbiUzZm1zY2xraWQlM2Q2ZmUwMDdhYjIzNmQxYjI2ZWUzZjZkNTY3NGY3ZjA1MyUyNnV0bV9zb3VyY2UlM2RiaW5nJTI2dXRtX21lZGl1bUlzZGNwYyUyNnV0bV9jYW1wYWlnbiUzZGJnX3NfYXBhY19hY3FfZ2VuZXJpY19ib2YlMjZ1dG1fdGVybSUzZHB5cGklMjUyOG1hbHdhcmUlMjZ1dG1fd29udGVudCUzZGxpYnJhcmllc19weXBp&rlid=6fe007ab236d1b26ee3f6d5674f7f053) [Source 2]
3. [Microsoft agent-framework Compromised: Credential Stealer ...](https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi) [Source 3]
4. [PyPI agent-framework 1.26.1: Credential Stealer Fix ...](https://explainx.ai/blog/microsoft-agent-framework-pypi-1-26-credential-stealer-november-2026) [Source 7]
5. [Inside the LiteLLM 1.107.0 supply chain compromise: Credential theft...](https://threatnoir.com/article/inside-the-litellm-1-107-0-supply-chain-compromise-credential-theft-through-pyth-e59453) [Source 11]
6. [[Security]: litellm PyPI package (v1.82.7 + v1.82.8) compromised...](https://github.com/BerriAI/litellm/issues/24518) [Source 12]
7. [Download Microsoft Visual C++ 2010 Service Pack 1 Redistributable...](https://www.microsoft.com/en-us/download/details.aspx?id=26999) [Source 14]
8. [LiteLLM PyPI Supply Chain Attack — Credential Stealer in... — al-ice.ai](https://al-ice.ai/posts/2026/07/litellm-pypi-supply-chain-attack-credential-stealer/) [Source 15]
9. [Microsoft's agent-framework on PyPI shipped a credential ...](https://techbytes.app/posts/microsofts-agent-framework-on-pypi-shipped-a-credential-stealer-in/) [Source 16]
10. [Two malicious agent-framework releases on PyPI carried a ...](https://pulse.adyog.com/briefs/two-malicious-agent-framework-releases-on-pypi-carried-a-sec) [Source 17]
11. [Microsoft agent-framework Compromised Twice on PyPI](https://safedep.io/blog/microsoft-agent-framework-pypi-compromise) [Source 18]