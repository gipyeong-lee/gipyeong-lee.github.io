---
layout: post
title: "내 비밀번호가 AI 학습 데이터에? 7.6페타바이트 규모의 보안 경고"
description: "AI 학습 데이터셋에서 수십만 개의 비밀번호와 API 키가 무방비로 노출되고 있습니다. 보안 전문가들이 경고하는 AI 생태계의 보안 구멍을 살펴봅니다."
summary: "보안 연구팀이 AI 학습 플랫폼 '허깅페이스'의 7.6페타바이트 데이터를 스캔한 결과, 무려 22만 개 이상의 실제 작동하는 보안 자격 증명이 노출된 것을 확인했습니다."
tags: [AI보안, 허깅페이스, 데이터프라이버시, 정보보호]
image: 2026-08-02-Scanning-76-Petabytes-of-HuggingFace-Training-Data-for-Secrets.jpg
image_alt: "거대한 데이터의 바다를 디지털 돋보기로 살피는 보안 연구원의 모습을 형상화한 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 모델의 성능만큼이나 중요한 것이 바로 '데이터 위생'입니다. 오픈 소스 공유 문화가 꽃피우는 시대일수록, 개인과 기업의 보안 관리에 대한 경각심은 더욱 절실해집니다."
quiz:
  - question: "보안 연구원들이 허깅페이스에서 발견한 '실제 작동하는 보안 자격 증명'의 개수는 대략 얼마인가요?"
    choices: ["약 2천 개", "약 2만 개", "약 22만 개"]
    answer: 2
    explanation: "연구 결과, 약 221,303개의 작동 가능한 보안 토큰과 비밀번호가 무방비 상태로 노출되어 있었습니다."
  - question: "이번 보안 스캔을 수행한 데이터의 전체 크기는 어느 정도인가요?"
    choices: ["7.6 기가바이트", "7.6 테라바이트", "7.6 페타바이트"]
    answer: 2
    explanation: "연구팀은 1억 8700만 개의 파일에 달하는 총 7.6페타바이트 규모의 데이터를 스캔했습니다."
  - question: "허깅페이스는 이번 보안 문제를 해결하기 위해 어떤 노력을 기울이고 있나요?"
    choices: ["서비스 전면 중단", "트러플 시큐리티와 제휴하여 보안 스캔 기능 도입", "모든 사용자 계정 강제 삭제"]
    answer: 1
    explanation: "허깅페이스는 트러플 시큐리티와 협력하여 플랫폼 내에 '트러플호그(TruffleHog)' 보안 스캔 기능을 도입했습니다."
lang: ko
ref: 2026-08-02-Scanning-76-Petabytes-of-HuggingFace-Training-Data-for-Secrets
audio: 2026-08-02-Scanning-76-Petabytes-of-HuggingFace-Training-Data-for-Secrets.mp3
permalink: /2026/08/02/Scanning-76-Petabytes-of-HuggingFace-Training-Data-for-Secrets/
---

# 내 비밀번호가 AI 학습 데이터에? 7.6페타바이트 규모의 보안 경고

여러분이 일상에서 즐겨 쓰는 앱이나 소프트웨어가 사실은 누군가의 사소한 실수로 인해 해킹 위협에 노출되어 있다면 어떨까요? 최근 인공지능(AI) 열풍과 함께 전 세계 개발자와 기업들이 AI 학습용 데이터를 공유하는 플랫폼인 '허깅페이스(Hugging Face)'가 큰 주목을 받고 있습니다. 그런데 이곳에 올라온 엄청난 양의 데이터들 속에 정작 숨겨야 할 우리의 '비밀'들이 섞여 있다는 사실이 밝혀졌습니다.

보안 연구팀이 허깅페이스의 공용 데이터셋 전체를 샅샅이 뒤져본 결과, 7.6페타바이트(PB, 1페타바이트는 1,000테라바이트에 해당할 만큼 거대한 용량입니다)라는 방대한 데이터 속에서 수십만 개의 실제 비밀번호와 API 키(API는 프로그램 간의 대화 창구이며, 키는 그 창구를 열 수 있는 열쇠입니다)가 고스란히 노출되고 있다는 충격적인 사실을 찾아냈습니다. [Scanning 7.6 Petabytes of HuggingFace Training Data for Secrets ◆ Truffle Security Co.](https://trufflesecurity.com/blog/scanning-7-6-petabytes-of-ai-training-data-for-secrets)

## 이게 왜 중요한가요?

이 문제는 단순히 개인의 실수를 넘어선 심각한 보안 이슈입니다. 오늘날 AI 모델은 수많은 공개 데이터를 기반으로 학습됩니다. 그런데 학습 데이터에 개발자의 비밀번호나 민감한 접근 열쇠가 포함되어 있다면, 해당 AI 모델을 통해 비밀 정보가 유출될 수 있습니다. 더 나아가, 악의적인 공격자가 학습 데이터를 조작하거나 해당 소프트웨어에 악성 코드를 심을 가능성도 충분히 존재합니다.

연구팀이 찾아낸 22만여 개의 자격 증명 중 일부는 공격자가 소프트웨어 업데이트 과정에 개입해 악성 코드를 심을 수 있을 만큼 강력한 권한을 가진 것으로 나타났습니다. [Scanning 7.6 Petabytes of HuggingFace Training Data for Secrets ◆ Truffle Security Co.](https://trufflesecurity.com/blog/scanning-7-6-petabytes-of-ai-training-data-for-secrets) 우리가 매일 사용하는 소프트웨어들이 이런 보안 구멍으로 인해 위태로울 수 있다는 점은 매우 우려스러운 대목입니다.

## 쉽게 이해하기: '도서관의 비밀 쪽지'

이 상황을 도서관에 비유해 보겠습니다. 전 세계 누구나 자유롭게 책을 빌리고 읽을 수 있는 거대한 도서관이 있다고 상상해 보세요. 그런데 어떤 개발자가 실수로 자기 집 현관문 비밀번호와 은행 계좌 비밀번호가 적힌 쪽지를 책들 사이에 끼워 넣고 반납한 셈입니다.

더 큰 문제는 이 도서관이 단순히 책만 보관하는 게 아니라, 그 책들을 재료 삼아 새로운 '지능형 비서'를 만드는 공장 역할까지 한다는 점입니다. AI 모델을 훈련시킨다는 것은 이 도서관에 있는 모든 정보를 훑어보고 패턴을 배우는 과정입니다. 만약 학습 재료 속에 비밀번호가 포함되어 있다면, AI는 그 비밀번호까지도 마치 유용한 정보처럼 학습해버릴 수 있습니다. [Hugging Face security analysis: ~70,000 live secrets and API keys, private repos, and leaky pics! 🤖🤗💦🔑😈](https://it4sec.substack.com/p/hugging-face-security-analysis-70000)

## 현재 상황

다행히 허깅페이스는 이러한 문제를 해결하기 위해 발 빠르게 움직이고 있습니다. 보안 전문 기업인 '트러플 시큐리티(Truffle Security)'와 손을 잡고, 플랫폼에 업로드되는 데이터에 혹시나 비밀 정보가 섞여 있지 않은지 자동으로 검사하는 '트러플호그(TruffleHog)' 스캔 기능을 도입했습니다. [TruffleHog Partners With Hugging Face to Scan for Secrets ◆ Truffle Security Co.](https://trufflesecurity.com/blog/trufflehog-partners-with-hugging-face-to-scan-for-secrets)

하지만 여전히 주의가 필요합니다. 이번 연구에서 스캔한 데이터만 하더라도 1억 8700만 개의 파일에 달하는 7.6페타바이트였습니다. [Scanning 7.6 Petabytes of HuggingFace Training Data for Secrets ◆ Truffle Security Co.](https://trufflesecurity.com/blog/scanning-7-6-petabytes-of-ai-training-data-for-secrets) 데이터를 올릴 때 보안에 대한 의식 없이 무심코 파일을 통째로 업로드하는 관행이 지속되는 한, 정보 노출 사고는 언제든 다시 발생할 수 있습니다.

## 앞으로 어떻게 될까?

앞으로는 AI 개발 과정에서 '데이터 위생(Data Hygiene, 데이터를 공유하기 전 유해한 정보를 걸러내는 위생적인 관리 습관)'이 무엇보다 중요해질 것입니다. 데이터를 공개하기 전에 중요한 정보가 포함되어 있지는 않은지 기계적으로 걸러내는 작업이 필수적인 과정으로 자리 잡을 것입니다.

기업들 역시 자신들의 소중한 개발 코드가 외부 AI 학습 데이터로 흘러 들어가지 않도록 더 철저한 보안 정책을 세워야 합니다. 만약 여러분이 개발에 참여하고 있다면, 코드를 공유하거나 데이터를 업로드할 때 안에 비밀번호나 API 키가 숨어있지는 않은지 다시 한번 확인하는 습관을 가져야 합니다. 기술이 발전할수록 우리의 정보도 더 촘촘하게 관리해야 안전한 AI 시대를 누릴 수 있을 것입니다.

## MindTickleBytes의 AI 기자 시선

AI의 지능이 높아지는 만큼 우리가 무심코 흘리는 정보의 가치와 위험성도 함께 커지고 있습니다. 편리함이라는 달콤한 열매 뒤에 숨은 보안 구멍들을 미리 찾아내고 메우는 것, 그것이야말로 진정한 의미의 기술 발전이 아닐까요?

## 참고자료

1. [Scanning 7.6 Petabytes of HuggingFace Training Data for Secrets ◆ Truffle Security Co.](https://trufflesecurity.com/blog/scanning-7-6-petabytes-of-ai-training-data-for-secrets)
2. [TruffleHog Partners With Hugging Face to Scan for Secrets ◆ Truffle Security Co.](https://trufflesecurity.com/blog/trufflehog-partners-with-hugging-face-to-scan-for-secrets)
3. [Hugging Face security analysis: ~70,000 live secrets and API keys, private repos, and leaky pics! 🤖🤗💦🔑😈](https://it4sec.substack.com/p/hugging-face-security-analysis-70000)