---
layout: post
title: "내 AI 계정이 해킹당했다고? Claude 토큰 도난 사태의 진실"
description: "최근 인공지능 서비스 Claude 이용자들 사이에서 원인 모를 토큰 소진과 계정 도난 피해가 잇따르고 있습니다. 해커들이 우리의 AI 계정을 노리는 방식과 예방법을 알기 쉽게 정리했습니다."
summary: "해커들이 악성 소프트웨어를 이용해 Claude 사용자의 로그인 세션을 탈취, 계정의 토큰 할당량을 무단으로 가로채는 피해가 발생하고 있습니다."
tags: [보안, Claude, AI, 정보보호, 해킹]
image: 2026-09-12-Hackers-are-stealing-Claude-tokens-from-subscribers.jpg
image_alt: "화면 속의 자물쇠 아이콘이 디지털 데이터 흐름 속에서 해킹당하는 모습을 추상적으로 표현한 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "단순히 비밀번호를 바꾸는 것만으로는 부족한 시대가 되었습니다. 활성 세션 보안의 중요성을 인지하고 브라우저 관리 습관을 점검해야 할 때입니다."
quiz:
  - question: "해커들이 Claude 계정을 탈취하는 주된 방식은 무엇인가요?"
    choices: ["강력한 비밀번호 대입", "인포스틸러 악성코드 이용", "이메일 피싱 사이트 접속"]
    answer: 1
    explanation: "해커들은 인포스틸러(정보 탈취) 악성코드를 사용하여 사용자의 컴퓨터에서 브라우저 쿠키와 로그인 세션 데이터를 직접 훔쳐내는 방식을 사용합니다."
  - question: "해커들이 기존의 2단계 인증(MFA)을 우회할 수 있는 이유는 무엇인가요?"
    choices: ["AI 모델이 인증을 무력화해서", "이미 로그인된 세션 정보를 통째로 훔쳐서", "암호화 기술을 해독해서"]
    answer: 1
    explanation: "이미 로그인되어 있는 활성 세션 정보를 탈취하기 때문에, 사용자가 이미 인증을 마친 상태를 악용하여 추가 인증 단계를 거치지 않고 계정에 접근합니다."
  - question: "피해 사실을 확인한 Anthropic의 초기 대응으로 옳은 것은?"
    choices: ["서비스 일시 중단", "강제 로그아웃 및 결제 정보 삭제", "사용자 계정 삭제"]
    answer: 1
    explanation: "Anthropic은 피해가 의심되는 계정을 강제로 로그아웃시키고, 결제 수단을 삭제하며 일부 사용자에게 환불 조치를 취하고 있습니다."
lang: ko
ref: 2026-09-12-Hackers-are-stealing-Claude-tokens-from-subscribers
audio: 2026-09-12-Hackers-are-stealing-Claude-tokens-from-subscribers.mp3
permalink: /2026/09/12/Hackers-are-stealing-Claude-tokens-from-subscribers/
---

상상해보세요. 평소처럼 업무를 마치고 인공지능(AI) 서비스인 'Claude'의 사용량을 확인했는데, 깜짝 놀랄 숫자가 찍혀 있습니다. 분명 오늘은 AI에게 단 한 번도 질문을 던진 적이 없는데, 토큰 할당량(AI가 처리할 수 있는 정보의 양)은 마치 밤새 누군가 열심히 일을 시킨 것처럼 줄어들어 있습니다. [출처 4](https://theoutpost.ai/news-story/hackers-drain-claude-accounts-as-security-breach-exposes-stolen-tokens-and-session-keys-30616/) 실제로 최근 많은 Claude 유료 구독자들이 겪고 있는 황당한 피해 사례입니다.

단순히 AI를 무료로 쓰려는 시도를 넘어, 이제 해커들이 우리의 소중한 유료 AI 구독 계정까지 노리기 시작했습니다. 도대체 해커들은 어떻게 우리의 계정을 훔치고, 우리의 토큰을 마음대로 사용하는 것일까요?

## 이게 왜 중요한가요?

AI 기술은 이제 일상의 필수 동반자가 되었습니다. 하지만 내 계정이 해킹당했다는 것은 단순히 '토큰을 뺏기는 것' 이상의 문제를 의미합니다. 해커들이 내 계정을 탈취하면, 나의 할당량을 이용해 그들만의 작업을 수행합니다. [출처 14](https://techround.co.uk/artificial-intelligence/malware-is-now-stealing-claude-sessions-to-drain-paid-ai-usage-how-does-that-work/) 내가 결제한 비용이 타인의 작업을 위해 쓰이는 것은 물론, 내 계정에서 발생하는 모든 AI 활용 결과가 타인에게 노출되거나 범죄에 오남용될 위험을 내포하고 있기 때문입니다. 더 큰 문제는 운영사인 Anthropic이 아직 사용자들이 자신의 토큰이 정확히 어디에 소모되었는지 파악할 수 있는 상세한 분석 도구를 제공하지 않고 있다는 점입니다. [출처 5](https://news.ycombinator.com/item?id=49662941)

## 쉽게 이해하기

해커들이 우리의 계정을 탈취하는 방식을 '열쇠'에 비유해 볼까요?

우리가 평소 사용하는 비밀번호나 2단계 인증(MFA, 추가 보안 확인 절차)은 집(계정)에 들어갈 때 사용하는 '열쇠'나 '도어락 비밀번호'와 같습니다. 매번 들어갈 때마다 잠금을 확인하죠. 하지만 해커들이 사용하는 **'인포스틸러(Infostealer, 정보 탈취용 악성코드)'**는 이 방식을 완전히 우회합니다. 

쉽게 말해서, 해커는 우리가 집에서 나올 때 무심코 현관문에 꽂아두고 나온 **'복제된 출입 카드(브라우저 쿠키 및 활성 세션 데이터)'**를 훔쳐가는 것입니다. [출처 7](https://diasporadigitalmedia.com/hackers-are-stealing-claude-tokens-from-subscribers/), [출처 12](https://nerdstool.com/blog/hackers-are-stealing-claude-tokens-from-subscribers/) 이 카드를 가지고 있으면 해커는 비밀번호가 무엇인지 몰라도, 이미 로그인이 된 상태로 우리 집 안방까지 아무런 제지 없이 들어올 수 있습니다. [출처 9](https://techmash.blog/blog/hackers-stealing-claude-subscriber-tokens) 시스템 입장에서는 이미 인증을 마친 '주인'이 다시 접속한 것으로 인식하기 때문에, 추가적인 보안 검문이 이루어지지 않는 것입니다.

## 현재 상황

현재 많은 사용자가 원인 불명의 토큰 소진 피해를 호소하고 있습니다. [출처 10](https://relvehq.com/blog/noise/hackers-steal-claude-tokens) 한 사용자의 사례를 보면, 특별한 업무를 하지 않았음에도 불구하고 토큰 사용량이 45%에서 55%로 급격히 증가하기도 했습니다. [출처 1](https://techcrunch.com/2026/09/08/hackers-are-stealing-claude-tokens-from-subscribers/)

Anthropic 측은 이 사태를 인지하고 일부 피해자들에게 경고 메일을 보내고 있지만, 모든 사용자에게 알림이 전달되지 않았다는 비판도 나오고 있습니다. [출처 11](https://www.bestaitools.com/hackers-are-stealing-claude-tokens-from-paying-subscribers-and-anthropic-cant-tell-you-how-much-was-taken/) 현재 회사 측은 피해가 의심되는 계정을 강제로 로그아웃시키고, 등록된 결제 수단을 삭제하며 일부 사용자에게 환불을 진행하는 등의 대응을 하고 있습니다. [출처 12](https://nerdstool.com/blog/hackers-are-stealing-claude-tokens-from-subscribers/) 하지만 근본적으로 이런 식의 '세션 하이재킹(Session Hijacking, 활성 세션 탈취)' 공격을 완벽히 방어할 수 있는 구조적인 도구는 아직 완성되지 않은 상태입니다. [출처 2](https://www.gadgetreview.com/hackers-are-stealing-claude-subscribers-ai-tokens)

## 앞으로 어떻게 될까?

전문가들은 이런 해킹 캠페인이 더욱 정교해질 것이라고 경고합니다. 악성코드는 사용자가 알지 못하는 사이에 컴퓨터에 침투하므로, 앞으로는 브라우저 보안 관리가 개인정보 보호의 최전선이 될 것입니다.

사용자 여러분은 자신의 계정 사용량을 정기적으로 확인하고, 의심스러운 동작이 감지되면 즉시 계정 로그아웃 후 다시 로그인하는 습관을 들여야 합니다. 또한 보안 소프트웨어를 통해 시스템 내 악성코드가 있는지 수시로 검사하는 것이 중요합니다. 더 나아가, AI 서비스 기업들도 사용자들이 자신의 토큰 소진 내역을 투명하게 확인하고 이상 징후를 빠르게 보고할 수 있는 보안 도구를 시급히 마련해야 할 것입니다.

## 참고자료

1. [HackersarestealingClaudetokensfromsubscribers| TechCrunch](https://techcrunch.com/2026/09/08/hackers-are-stealing-claude-tokens-from-subscribers/)
2. [HackersAreStealingClaudeSubscribers’ AITokens](https://www.gadgetreview.com/hackers-are-stealing-claude-subscribers-ai-tokens)
3. [AnthropicClaudeSecurity Breach:StolenTokensHit Users](https://theoutpost.ai/news-story/hackers-drain-claude-accounts-as-security-breach-exposes-stolen-tokens-and-session-keys-30616/)
4. [HackersarestealingClaudetokensfromsubscribers|HackerNews](https://news.ycombinator.com/item?id=49662941)
5. [ClaudeTokenTheft HitsSubscribersasHackersTarget Accounts...](https://www.itechpost.com/articles/237270/20260909/claude-token-theft-hits-subscribers-hackers-target-accounts-security.htm)
6. [HackersarestealingClaudetokensfromsubscribers- Diaspora...](https://diasporadigitalmedia.com/hackers-are-stealing-claude-tokens-from-subscribers/)
7. [Hackers Are Stealing Claude Subscribers’ AI Tokens](https://tech.yahoo.com/ai/claude/articles/hackers-stealing-claude-subscribers-ai-154417768.html)
8. [Hackers Are Stealing Claude Tokens From Subscribers](https://techmash.blog/blog/hackers-stealing-claude-subscriber-tokens)
9. [Hackers are stealing Claude tokens - relvehq.com](https://relvehq.com/blog/noise/hackers-steal-claude-tokens)
10. [Hackers are stealing Claude tokens from paying subscribers ...](https://www.bestaitools.com/hackers-are-stealing-claude-tokens-from-paying-subscribers-and-anthropic-cant-tell-you-how-much-was-taken/)
11. [Hackers are stealing Claude tokens from subscribers](https://nerdstool.com/blog/hackers-are-stealing-claude-tokens-from-subscribers)
12. [Hackers draining Claude tokens from subscriber accounts](https://newsgab.com/hackers-drain-claude-tokens-from-subscriber-accounts/)
13. [MalwareIsNowStealingClaudeSessions To Drain Paid... - TechRound](https://techround.co.uk/artificial-intelligence/malware-is-now-stealing-claude-sessions-to-drain-paid-ai-usage-how-does-that-work/)
14. [Newsroom \ Anthropic](https://www.anthropic.com/news)