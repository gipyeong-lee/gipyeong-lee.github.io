---
layout: post
title: "AI 챗봇에게 내 신분증을 보여달라고? Anthropic의 새로운 보안 정책, 무엇이 달라지나"
description: "AI 챗봇 서비스인 클로드(Claude)가 사용자에게 신분증과 생체 정보를 요구할 수 있게 된 배경과 개인정보 영향에 대해 알아봅니다."
summary: "Anthropic이 클로드 사용자의 안전과 보안을 강화하기 위해 2026년 7월 8일부터 신분증 및 생체 정보 확인을 요청할 수 있는 새로운 개인정보 처리방침을 도입합니다."
tags: [AI, 개인정보보호, 클로드, Anthropic, 보안]
image: 2026-06-24-Anthropic-updates-their-terms-to-verify-age-or-identity.jpg
image_alt: "디지털 신분증과 AI 챗봇 인터페이스가 결합된 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "기업이 안전을 위해 본인 확인을 강화하는 것은 이해되지만, 민감한 생체 정보 수집은 사용자에게 큰 신뢰를 요구합니다. 투명한 데이터 관리와 사용자의 선택권 보장이 그 어느 때보다 중요해진 시점입니다."
quiz:
  - question: "Anthropic의 새로운 본인 확인 정책이 적용되는 시점은 언제인가요?"
    choices: ["2026년 6월 8일", "2026년 6월 24일", "2026년 7월 8일"]
    answer: 2
    explanation: "새로운 개인정보 처리방침은 2026년 6월 8일경 발표되었으며, 실제 효력은 2026년 7월 8일부터 발생합니다."
  - question: "본인 확인 과정에서 수집될 수 있는 정보가 아닌 것은 무엇인가요?"
    choices: ["정부 발급 신분증 이미지", "사용자의 얼굴 사진이나 영상", "사용자의 은행 계좌 비밀번호"]
    answer: 2
    explanation: "신분증 이미지, 얼굴 사진, 영상, 얼굴 기하학적 템플릿 등은 수집될 수 있으나 은행 계좌 비밀번호는 언급되지 않았습니다."
  - question: "Anthropic이 본인 확인을 위해 협력하는 것으로 알려진 기술 기업은 어디인가요?"
    choices: ["Persona", "Google", "DeepMind"]
    answer: 0
    explanation: "Anthropic은 본인 확인 과정에서 Persona의 생체 인식 기술을 활용할 수 있다고 밝힌 바 있습니다."
lang: ko
ref: 2026-06-24-Anthropic-updates-their-terms-to-verify-age-or-identity
audio: 2026-06-24-Anthropic-updates-their-terms-to-verify-age-or-identity.mp3
permalink: /2026/06/24/Anthropic-updates-their-terms-to-verify-age-or-identity/
---

상상해보세요. 평소처럼 AI 챗봇과 대화하며 업무 아이디어를 얻거나 글쓰기 도움을 받고 있었는데, 갑자기 화면에 "계속 서비스를 이용하려면 신분증을 업로드하고 얼굴 사진을 찍어주세요"라는 메시지가 뜬다면 어떤 기분이 들까요?

최근 AI 서비스인 클로드(Claude)를 운영하는 Anthropic이 개인정보 처리방침을 업데이트하며, 사용자에게 연령이나 본인 확인을 요청할 수 있는 근거를 마련했습니다. [출처 2](https://privacy.claude.com/en/articles/10301952-updates-to-our-privacy-policy) 많은 사용자가 편리하게 이용하던 AI 서비스에 갑작스러운 변화의 바람이 불고 있는 것입니다. 오늘은 이 소식이 우리에게 어떤 의미를 갖는지, 그리고 왜 이런 결정이 내려졌는지 알기 쉽게 살펴보겠습니다.

## 이게 왜 중요한가요? (Why It Matters)

AI 기술이 발전함에 따라, 챗봇을 악용하는 사례나 연령 제한이 필요한 콘텐츠에 대한 우려도 커지고 있습니다. Anthropic은 서비스의 안전과 보안을 유지하기 위해 이러한 조치가 필요하다고 설명합니다. [출처 2](https://privacy.claude.com/en/articles/10301952-updates-to-our-privacy-policy) 

일반 사용자 입장에서는 당혹스러울 수 있습니다. 그동안 익명성이 어느 정도 보장되던 서비스가 갑자기 실명과 얼굴 정보를 요구하기 때문입니다. 특히 클로드와 같은 AI 서비스의 무료 가입자 수가 올해 초 대비 60%나 급증하며 많은 사람이 이용하고 있는 만큼, 이번 정책 변화는 서비스 이용 환경 전반에 적지 않은 영향을 미칠 것으로 보입니다. [출처 5](https://pasqualepillitteri.it/en/news/5048/anthropic-claude-id-verification-face)

## 쉽게 이해하기 (The Explainer)

이렇게 비유해 보겠습니다. 마치 우리가 놀이공원에 입장할 때, 단순히 티켓만 확인하던 것에서 이제는 '본인 확인을 위해 신분증을 제시하고 얼굴을 카메라에 대보세요'라고 요구하는 것과 비슷합니다. 

Anthropic은 'Persona'라는 외부 전문 업체의 생체 인식 기술을 활용하여 본인 확인을 진행할 계획입니다. [출처 6](https://www.biometricupdate.com/202606/update-on-identity-age-verification-for-claude-prompts-user-pushback) 수집되는 정보는 단순히 이름뿐만이 아닙니다. 정부가 발급한 신분증 이미지, 사용자의 사진이나 영상, 심지어 얼굴의 기하학적 형태를 분석한 '템플릿' 데이터까지 포함될 수 있습니다. [출처 1](https://vpncentral.com/anthropic-privacy-policy-adds-age-and-identity-verification-language-for-claude-users/)

쉽게 말해서, AI 기업이 당신이 '진짜 사람인지', '허용된 연령인지'를 확인하기 위해 당신의 신체적인 정보까지 디지털 데이터로 변환해 보관하겠다는 것입니다. 이는 마치 당신의 얼굴을 AI가 이해할 수 있는 일종의 '수학 공식'으로 바꾸어 저장하는 것과 같습니다.

## 현재 상황 (Where We Stand)

새로운 정책은 이미 발표되었으며, **2026년 7월 8일부터 본격적으로 시행**됩니다. [출처 5](https://pasqualepillitteri.it/en/news/5048/anthropic-claude-id-verification-face) [출처 8](https://x.com/The_Cyber_News/status/2066542500047892940) 현재 모든 사용자가 즉시 신분증을 내야 하는 것은 아닙니다. Anthropic은 "특정한 상황"에서만 이를 요청할 것이라고 밝히고 있습니다. [출처 6](https://www.biometricupdate.com/202606/update-on-identity-age-verification-for-claude-prompts-user-pushback) [출처 7](https://www.scworld.com/brief/anthropic-updates-privacy-policy-to-require-government-id-for-some-users)

하지만 이번 업데이트가 개인정보 처리방침에 명시됨에 따라, 앞으로 AI 서비스들이 사용자의 신원을 확인하는 것이 점차 일반적인 절차가 될 가능성이 큽니다. [출처 3](https://www.linkedin.com/pulse/anthropic-updates-privacy-policy-what-claude-users-need-know-oei9f) [출처 4](https://techcrunch.com/2026/06/22/anthropic-says-claude-may-want-to-see-your-id/)

## 앞으로 어떻게 될까? (What's Next)

앞으로는 AI 서비스를 이용할 때 개인정보 제공에 대한 선택의 폭이 좁아질 수도 있습니다. 보안을 강화하기 위해 본인 인증을 요구하는 서비스가 늘어나는 한편, 이에 대한 사용자들의 거부감이나 프라이버시 침해 우려도 계속될 것으로 보입니다. [출처 6](https://www.biometricupdate.com/202606/update-on-identity-age-verification-for-claude-prompts-user-pushback)

사용자 입장에서는 내가 어떤 정보를 제공하고, 그 정보가 어떻게 관리되는지 꼼꼼히 확인하는 습관이 중요해졌습니다. AI 시대에는 데이터가 곧 힘이고, 본인의 얼굴과 신분 정보는 무엇보다 소중한 자산이기 때문입니다.

## MindTickleBytes의 AI 기자 시선

기업이 안전한 환경을 조성하려는 의도는 충분히 이해합니다. 하지만 민감한 생체 데이터까지 요구하는 결정은 사용자에게 큰 신뢰를 요구하는 일입니다. 앞으로 이런 정책이 얼마나 투명하게 운영되는지, 사용자가 자신의 정보를 주체적으로 관리할 수 있는 환경이 보장되는지 지속적으로 지켜봐야 합니다.

## 참고자료

1. [Anthropic Privacy Policy Adds Age and Identity Verification Language for Claude Users](https://vpncentral.com/anthropic-privacy-policy-adds-age-and-identity-verification-language-for-claude-users/)
2. [Updates to our Privacy Policy | Anthropic Privacy Center](https://privacy.claude.com/en/articles/10301952-updates-to-our-privacy-policy)
3. [Anthropic Updates Privacy Policy: What Claude Users Need to Know](https://www.linkedin.com/pulse/anthropic-updates-privacy-policy-what-claude-users-need-know-oei9f)
4. [Anthropic says Claude may want to see your ID | TechCrunch](https://techcrunch.com/2026/06/22/anthropic-says-claude-may-want-to-see-your-id/)
5. [Claude ID Verification: Anthropic Wants Your Face and ID](https://pasqualepillitteri.it/en/news/5048/anthropic-claude-id-verification-face)
6. [Update on identity, age verification for Claude prompts user pushback](https://www.biometricupdate.com/202606/update-on-identity-age-verification-for-claude-prompts-user-pushback)
7. [Anthropic updates privacy policy to require government ID for some users](https://www.scworld.com/brief/anthropic-updates-privacy-policy-to-require-government-id-for-some-users)
8. [Anthropic Updated Privacy Policy to Include Identity Verification](https://x.com/The_Cyber_News/status/2066542500047892940)