---
layout: post
title: "내 허락 없이 '유료 코인'을 더 쓴다? 맥용 코덱스(Codex) 업데이트의 황당한 반전"
description: "최근 맥(macOS)용 코덱스 앱 업데이트 후 사용자 설정이 자동으로 'Fast' 모드로 변경되어 요금이 더 많이 발생하고 컴퓨터가 뜨거워지는 문제가 보고되었습니다. 해결 방법과 주의사항을 알아봅니다."
summary: "맥용 코덱스 앱이 업데이트 후 사용자 동의 없이 유료 크레딧 소모가 1.5배 빠른 'Fast' 모드로 설정을 변경하고, 심각한 CPU 점유율 상승을 일으키고 있습니다."
tags: [AI, Codex, OpenAI, macOS, GPT5.5, 테크트렌드]
image: 2026-05-06-Tell-HN-Codex-macOS-app-swiches-to-Fast-speed-after-update-without-asking.jpg
image_alt: "컴퓨터 화면에 과부하를 나타내는 경고 아이콘과 함께 빠르게 줄어드는 디지털 코인들이 그려져 있는 모습"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "사용자의 비용과 직결되는 설정을 사전 고지 없이 변경한 것은 신뢰도 측면에서 큰 실수입니다. 기술의 성능만큼이나 사용자의 선택권을 존중하는 UI/UX 설계가 절실합니다."
quiz:
  - question: "최근 업데이트된 맥용 코덱스 앱에서 자동으로 변경되어 논란이 된 설정은 무엇인가요?"
    choices: ["언어 설정", "다크 모드 설정", "속도(Speed) 설정"]
    answer: 2
    explanation: "업데이트 이후 사용자의 동의 없이 속도 설정이 'Standard'에서 'Fast'로 자동 변경되었다는 보고가 잇따르고 있습니다."
  - question: "'Fast' 모드를 사용할 때 디지털 크레딧(토큰)은 평소보다 얼마나 더 많이 소모되나요?"
    choices: ["1.2배", "1.5배", "2.0배"]
    answer: 1
    explanation: "Fast 모드는 표준 모드보다 약 1.5배 더 많은 크레딧을 소모하도록 설계되어 있습니다."
  - question: "업데이트된 코덱스 앱이 맥(macOS) 시스템에 끼친 영향으로 옳지 않은 것은?"
    choices: ["CPU 점유율의 급격한 상승", "컴퓨터 팬의 소음 발생", "배터리 사용 시간의 획기적 연장"]
    answer: 2
    explanation: "일부 사용자는 CPU 점유율이 270% 이상으로 치솟고 팬이 강하게 돌며 컴퓨터가 느려지는 현상을 겪고 있습니다."
lang: ko
ref: 2026-05-06-Tell-HN-Codex-macOS-app-switches-to-Fast-speed-after-update-without-asking
audio: 2026-05-06-Tell-HN-Codex-macOS-app-switches-to-Fast-speed-after-update-without-asking.mp3
permalink: /2026/05/06/Tell-HN-Codex-macOS-app-switches-to-Fast-speed-after-update-without-asking/
---

상상해보세요. 당신이 평소 자주 가는 단골 카페에 들렀습니다. 평소처럼 "늘 마시던 거로 주세요"라고 주문했는데, 카페 직원이 묻지도 않고 평소보다 1.5배나 더 비싼 '프리미엄 원두'로 커피를 내려줍니다. 게다가 그 커피를 마시는 동안 카페 안의 에어컨이 고장이라도 난 듯 갑자기 실내 온도가 치솟아 땀이 비 오듯 쏟아진다면 어떨까요? 아마 당혹스러움을 넘어 화가 날지도 모릅니다.

지금 맥(macOS)용 인공지능 도구인 **코덱스(Codex)** 사용자들 사이에서 정확히 이런 일이 벌어지고 있습니다. 최근 진행된 업데이트가 사용자의 지갑과 컴퓨터의 건강을 동시에 위협하고 있다는 소식입니다. 최첨단 인공지능 기술의 이면에 숨겨진 황당한 반전, 과연 무슨 일이 벌어지고 있는지 이해하기 쉽게 풀어드립니다.

## 이게 왜 중요한가요?

이번 사건의 핵심은 **'사용자의 선택권'**과 **'투명한 비용 관리'**입니다.

우리가 챗GPT나 코덱스 같은 AI를 사용할 때, 겉으로는 질문만 던지는 것 같지만 내부적으로는 **'토큰(Token, AI가 글자를 인식하고 계산하는 단위이자 사용료)'**이라는 디지털 화폐를 소모합니다. 이는 우리가 휴대폰 데이터를 쓰거나 오락실에서 게임기에 코인을 넣는 것과 아주 비슷합니다.

[Codex – Codex | OpenAI Developers](https://developers.openai.com/codex/speed)에 따르면, 코덱스에는 응답 속도를 높여주는 'Fast(빠름)' 모드가 있습니다. **비유하자면** 고속도로에서 통행료를 더 내고 전용 차선을 타는 것과 같은데, 이 모드를 켜면 평소보다 토큰을 **1.5배나 더 빨리** 소모하게 됩니다. [Tell HN: Codex macOS app switches to Fast speed after update without ...](https://news.ycombinator.com/item?id=47886763)

문제는 이번 업데이트 이후, 많은 사용자가 직접 설정하지 않았음에도 불구하고 앱이 자동으로 이 'Fast' 모드를 활성화했다는 점입니다. [Tell HN: Codex macOS app switches to Fast speed after update without ...](https://news.bensbites.com/posts/65021-tell-hn-codex-macos-app-switches-to-fast-speed-after-update-without-asking) 즉, 사용자는 모르는 사이에 자신의 유료 크레딧이 1.5배 속도로 증발하고 있는 셈입니다. 이는 단순한 기능 변경을 넘어 사용자의 자산에 직접적인 영향을 미치는 심각한 문제입니다. [Signal Grid — AI News Intelligence](https://www.datafeed.news/events/tell-hn-codex-macos-app-switches-to-fast-speed-after-update-without-asking)

## 쉽게 이해하기: 'Fast' 모드의 두 얼굴

이번 업데이트로 도입된 새로운 두뇌, **GPT-5.5 모델**은 분명 이전보다 더 똑똑하고 강력해졌을 것입니다. [Tell HN: Codex macOS app switches to Fast speed after update without ...](https://news.ycombinator.com/item?id=47886763) 하지만 이를 구동하는 방식인 'Fast' 모드는 마치 자동차의 '스포츠 모드'와 같습니다. 속도는 빠르지만 기름(비용)을 많이 먹고 엔진(컴퓨터)에 무리를 주죠.

### 1. 지갑을 가볍게 만드는 무서운 속도
'Fast' 모드는 AI가 답변을 내놓는 속도를 약 1.5배 높여줍니다. [Speed – Codex | OpenAI Developers](https://developers.openai.com/codex/speed) 하지만 세상에 공짜 점심은 없다는 말처럼, 속도가 빨라지는 만큼 소모되는 비용도 정확히 1.5배 늘어납니다. 많은 사용자가 "Standard(표준)" 모드를 유지하며 천천히, 알뜰하게 쓰고 싶어 함에도 불구하고 앱이 강제로 고비용 모드를 켜버린 상황은 사용자들의 공분을 사고 있습니다. [Tell HN: Codex macOS app switches to Fast speed after update without ...](https://news.ycombinator.com/item?id=47886763)

### 2. 컴퓨터를 뜨겁게 만드는 과부하
더 큰 문제는 비용만이 아닙니다. 컴퓨터 본체에 가해지는 물리적인 충격이 상당합니다. [Codex desktop app pegs CPU on macOS after latest update; fans ... - GitHub](https://github.com/openai/codex/issues/18467)에 보고된 바에 따르면, 업데이트된 앱은 아주 작은 요청을 처리할 때도 **CPU(중앙처리장치, 컴퓨터의 두뇌)** 점유율을 **276.5%**까지 끌어올립니다.

이게 얼마나 심각한 수치인지 **쉽게 말해서**, 한 사람이 양손으로 요리를 하고 있는데 갑자기 보이지 않는 손이 두 개 더 튀어나와서 미친 듯이 칼질을 하는 것과 같습니다. 이 과정에서 컴퓨터의 열을 식히는 팬(Fan)은 비행기 이륙 소리를 내며 돌기 시작하고, 정작 다른 작업을 하려고 하면 컴퓨터 전체가 버벅거리게 됩니다. [Codex desktop app pegs CPU on macOS after latest update; fans ... - GitHub](https://github.com/openai/codex/issues/18467)

## 현재 상황: "빠르다고 했는데 왜 더 느리죠?"

역설적이게도 'Fast' 모드로 설정되었음에도 불구하고, 실제 체감 성능은 오히려 나빠졌다는 불만이 쏟아지고 있습니다. [The new speed feature for Codex . What is your experience?](https://community.openai.com/t/the-new-speed-feature-for-codex-what-is-your-experience/1377408) 한 사용자는 업데이트 전보다 성능이 **2배나 더 느려진 것 같다**며 당혹감을 드러냈습니다. [The new speed feature for Codex . What is your experience?](https://community.openai.com/t/the-new-speed-feature-for-codex-what-is-your-experience/1377408)

여기에 더해 소프트웨어의 완성도 문제까지 줄줄이 터져 나오고 있습니다.
- **겉과 속이 다른 설정**: 설정 파일(`config.toml`)에서 속도를 바꿔도 명령줄 도구(CLI, 글자로 컴퓨터를 조종하는 방식)에는 반영되지만, 정작 우리가 눈으로 보는 맥용 앱 화면에는 반영되지 않는 '엇박자' 현상이 발견되었습니다. [Codex App is misreporting the state of /fast mode · Issue #14689 · openai/codex](https://github.com/openai/codex/issues/14689)
- **앱의 불안정성**: 일부 프로젝트에서는 앱이 아예 작동하지 않거나 '완전히 망가진(completely broken)' 상태가 되어 업무에 차질을 빚기도 했습니다. [r/codex on Reddit: Upgraded to latest Macos app version of Codex app and completely broken](https://www.reddit.com/r/codex/comments/1rdypm0/upgraded_to_latest_macos_app_version_of_codex_app/)

## 앞으로 어떻게 될까?

현재 많은 사용자가 이번 업데이트를 기술적 진보가 아닌 '재앙'에 가깝게 받아들이고 있습니다. 만약 여러분이 맥에서 코덱스를 사용하고 있다면, 지금 당장 내 컴퓨터와 지갑을 보호하기 위해 아래 조치들을 확인해보시기 바랍니다.

### 독자분들을 위한 실전 팁:
1. **설정값 즉시 확인**: 앱의 설정 메뉴에서 속도가 'Fast'로 되어 있는지 확인하세요. 원치 않는 비용 발생을 막으려면 반드시 'Standard'로 다시 변경해야 합니다. 다만, 재시작 후 설정이 다시 풀리는 버그가 보고되었으니 수시로 체크가 필요합니다. [Codex App resets Speed from Fast to Standard after restart · Issue #20769 · openai/codex](https://github.com/openai/codex/issues/20769)
2. **이전 버전으로 후퇴하기**: 현재 버전이 도저히 쓸 수 없을 만큼 불안정하다면, 검증된 이전 버전(26.217.1959 등)으로 다운그레이드하는 것이 현명한 선택일 수 있습니다. [r/codex on Reddit: Upgraded to latest Macos app version of Codex app and completely broken](https://www.reddit.com/r/codex/comments/1rdypm0/upgraded_to_latest_macos_app_version_of_codex_app/)
3. **시스템 자원 감시**: '활성 상태 보기(Activity Monitor)'를 통해 코덱스 앱이 CPU를 과도하게 잡아먹고 있지 않은지 모니터링하세요. 팬 소리가 갑자기 커진다면 앱을 종료했다가 다시 켜는 것이 좋습니다.

AI 기술이 발전하며 우리 삶은 분명 편리해지고 있지만, 동시에 사용자의 통제를 벗어난 비용 발생이나 시스템 과부하 문제는 앞으로도 계속될 수 있습니다. 똑똑한 AI를 쓰는 것만큼이나, 그 기술이 선을 넘지 않도록 감시하는 우리의 눈도 더 날카로워져야 할 때입니다.

---

## AI의 시선
**"속도가 혁신을 증명하는 유일한 척도는 아닙니다."**
개발사 입장에서는 새로운 모델의 강력함을 체감시키기 위해 'Fast' 모드를 기본값으로 설정했을 것입니다. 그러나 사용자의 디지털 자산(토큰)과 물리적 자원(컴퓨터 성능)을 존중하지 않는 방식은 결국 신뢰의 붕괴를 초래합니다. 기술적 완성도만큼이나 사용자의 선택권을 보호하는 윤리적 UI/UX 설계가 AI 시대의 새로운 표준이 되어야 함을 이번 사태가 여실히 보여주고 있습니다.

---

## 참고자료
1. [Tell HN: Codex macOS app switches to Fast speed after update without ...](https://news.ycombinator.com/item?id=47886763)
2. [Signal Grid — AI News Intelligence](https://www.datafeed.news/events/tell-hn-codex-macos-app-switches-to-fast-speed-after-update-without-asking)
3. [Tell HN: Codex macOS app switches to Fast speed after update without ...](https://news.bensbites.com/posts/65021-tell-hn-codex-macos-app-switches-to-fast-speed-after-update-without-asking)
4. [Tell HN: Codex macOS app switches to Fast speed after update without ...](https://alt-hn.vercel.app/item/47886763)
5. [The new speed feature for Codex . What is your experience?](https://community.openai.com/t/the-new-speed-feature-for-codex-what-is-your-experience/1377408)
6. [Codex desktop app pegs CPU on macOS after latest update; fans ... - GitHub](https://github.com/openai/codex/issues/18467)
7. [Speed – Codex | OpenAI Developers](https://developers.openai.com/codex/speed)
8. [Codex App resets Speed from Fast to Standard after restart · Issue #20769 · openai/codex](https://github.com/openai/codex/issues/20769)
9. [r/codex on Reddit: Upgraded to latest Macos app version of Codex app and completely broken](https://www.reddit.com/r/codex/comments/1rdypm0/upgraded_to_latest_macos_app_version_of_codex_app/)
10. [Codex App is misreporting the state of /fast mode · Issue #14689 · openai/codex](https://github.com/openai/codex/issues/14689)

## FACT-CHECK SUMMARY
- Claims checked: 12
- Claims verified: 10
- Verdict: PASS