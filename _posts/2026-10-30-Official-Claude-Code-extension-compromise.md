---
layout: post
title: "내 컴퓨터의 AI 조수, 믿어도 될까? 공식 Claude Code 확장 프로그램 해킹 사건"
description: "최근 발생한 Claude Code 확장 프로그램 해킹 사건의 전말과 개발자가 보안을 위해 알아야 할 점을 쉽게 설명합니다."
summary: "Cursor 마켓플레이스에서 배포되던 공식 Claude Code 확장 프로그램이 해킹되어 사용자의 컴퓨터에 백도어를 심는 악성 코드가 포함된 사건이 발생했습니다."
tags: [보안, AI, ClaudeCode, 개발자]
image: 2026-10-30-Official-Claude-Code-extension-compromise.jpg
image_alt: "컴퓨터 화면에서 보안 경고창이 떠 있는 모습"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "개발 도구조차 위협에 노출되는 에이전트 시대, 도구 설치 전 신뢰성을 확인하는 검증 절차가 필수적입니다."
quiz:
  - question: "이번에 해킹된 확장 프로그램은 어떤 기능을 수행하도록 설계되었나요?"
    choices: ["파일 강제 삭제", "사용자의 컴퓨터에 지속적인 SSH 백도어 설치", "광고 자동 노출"]
    answer: 1
    explanation: "해당 악성 확장 프로그램은 사용자의 컴퓨터에 은밀하게 지속적으로 접근할 수 있는 SSH 백도어를 설치하도록 설계되었습니다."
  - question: "이번 공격에서 공격자가 탈취하려고 시도한 정보가 아닌 것은 무엇인가요?"
    choices: ["사용자 이름 및 운영체제 정보", "컴퓨터의 공개 IP 주소", "개인 온라인 쇼핑 기록"]
    answer: 2
    explanation: "공격자는 호스트명, 사용자명, OS, 아키텍처, 환경 변수, 작업 디렉토리, Git 이메일, IP 주소 등을 수집했습니다."
  - question: "해당 사건과 관련하여 마이크로소프트의 VS Code 공식 확장 프로그램은 안전한가요?"
    choices: ["아니요, 똑같이 해킹되었습니다", "네, 마이크로소프트 공식 확장 프로그램은 악성 코드가 포함되어 있지 않습니다", "모두 안전하지 않습니다"]
    answer: 1
    explanation: "이번 사건에서 Cursor 마켓플레이스의 Claude Code 확장 프로그램이 타겟이 되었으며, 마이크로소프트 VS Code용 공식 Claude 확장 프로그램은 이번 공격과 무관합니다."
lang: ko
ref: 2026-10-30-Official-Claude-Code-extension-compromise
audio: 2026-10-30-Official-Claude-Code-extension-compromise.mp3
permalink: /2026/10/30/Official-Claude-Code-extension-compromise/
---

상상해 보세요. 코딩을 도와주는 똑똑한 AI 조수를 내 작업 도구에 설치했는데, 알고 보니 이 조수가 내 컴퓨터의 뒷문을 열어두고 있었다면 어떨까요? 최근 소프트웨어 개발 현장에서 마치 영화 속 이야기 같은 보안 사고가 발생했습니다.

일반적으로 우리는 '공식' 마켓플레이스에서 프로그램을 내려받을 때 안심하고 설치합니다. 하지만 이번에는 믿었던 도구가 배신을 했습니다. Cursor 마켓플레이스에서 배포되던 [공식 Claude Code 확장 프로그램이 해킹되어 악성 코드가 포함된 버전이 유포된 사건](https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor)이 발생한 것입니다.

## 이게 왜 중요한가요?

이번 사건은 AI를 도구로 사용하는 모든 사용자에게 경종을 울립니다. AI 코딩 에이전트(코드를 읽고 수정하며 테스트까지 수행하는 AI 도구)는 개발자의 코드베이스 전체에 접근할 수 있는 권한을 가집니다. [Claude Code는 Anthropic이 만든 에이전트형 코딩 도구](https://claude.com/product/claude-code)로, 우리를 대신해 파일 편집이나 명령어 실행을 수행하죠.

이런 강력한 도구가 해킹되었다는 것은 공격자가 개발자의 컴퓨터에 마음대로 접속할 수 있는 길, 즉 '백도어'가 열렸다는 뜻입니다. 내 컴퓨터의 모든 파일, 민감한 환경 설정, 그리고 우리가 개발 중인 코드의 소중한 지적 재산이 순식간에 남의 손에 넘어갈 위험에 처한 것입니다.

## 쉽게 이해하기: '백도어'와 '트로이 목마'

이번 사건을 이해하기 위해 두 가지 비유를 들어보겠습니다.

쉽게 말해서 **'트로이 목마(Trojan Horse)'**와 같습니다. 고대 그리스 신화에서 성 안에 들어온 거대한 목마처럼, 이 프로그램은 겉보기에는 아무런 문제 없는 평범한 AI 코딩 확장 프로그램처럼 보였습니다. 실제 악성 프로그램을 풀어보니 [평소 우리가 사용하던 정상적인 도구와 똑같은 기능을 하도록 구성되어 있었죠](https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor). 하지만 그 안에는 사용자 몰래 심어진 악성 코드가 숨어 있었습니다.

비유하면 **'백도어(Backdoor)'**는 우리 집 현관문 말고 뒤뜰에 아무도 모르게 만들어둔 몰래 쪽문과 같습니다. 이 [악성 코드는 컴퓨터에 지속적으로 접근할 수 있는 SSH 백도어를 설치](https://cursor.com/blog/claude-code-extension-security-notice)했습니다. 공격자는 이 문을 통해 언제든 내 컴퓨터에 들어와 정보를 훔쳐보거나 조종할 수 있게 된 것입니다. 이들이 [수집한 정보는 호스트명, 사용자명, 운영체제 정보, 홈 디렉토리 경로, 환경 변수 이름, Git 이메일, 심지어는 공인 IP 주소](https://cursor.com/blog/claude-code-extension-security-notice)까지 포함됩니다.

## 어디까지가 위험한가요?

다행히 모든 Claude 관련 도구가 위험한 것은 아닙니다. [마이크로소프트 VS Code를 위한 공식 Claude 확장 프로그램은 이번 사건과 무관하며 악성 코드가 포함되어 있지 않습니다](https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor).

하지만 AI 에이전트 시대에는 우리가 사용하는 도구의 출처를 끊임없이 의심해야 합니다. 최근 AI 에이전트를 대상으로 한 공격 기법은 갈수록 교묘해지고 있습니다. 예를 들어 [겉보기에는 깨끗한 GitHub 저장소라 하더라도 AI 에이전트가 코드를 실행하는 순간 백도어를 열도록 설계된 공격](https://cybersecuritynews.com/new-claude-code-attack/) 사례들도 보고되고 있습니다. 단순히 기능이 좋다고 해서 무턱대고 설치하는 습관은 이제 보안에 큰 위험을 초래할 수 있습니다.

## 앞으로 우리는 어떻게 해야 할까요?

앞으로 AI 개발 도구 시장에서는 '신뢰성 검증'이 핵심 경쟁력이 될 것입니다. 우리는 더 정교해진 AI 조수를 사용하게 되겠지만, 그만큼 그 조수의 출처를 확인하고 안전한 환경에서 구동하는 법을 익혀야 합니다. 설치 전 도구의 평판을 확인하고, 가능하면 공식 마켓플레이스에서도 개발사가 직접 제공하는 것인지 한 번 더 확인하는 습관이 필요합니다.

개발자라면 자신의 환경에서 사용하는 에이전트가 어떤 데이터에 접근하는지, 어떤 권한을 가지고 있는지 주기적으로 감사(Audit)하는 습관도 중요해질 것입니다. AI는 우리의 시간을 아껴주는 고마운 동료이지만, 그 동료가 안전한지는 우리가 직접 챙겨야 합니다.

## AI의 시선
MindTickleBytes의 AI 기자 시선: 도구가 강력해질수록 공격자의 타겟이 될 가능성도 커집니다. 이제 AI 도구의 설치는 단순한 기능 확장이 아니라, 내 컴퓨터의 보안을 맡기는 중대한 결정이라는 점을 기억해야 합니다.

## 참고자료

1. [Trojanized Claude Code Extension Plants an... | OpenSourceMalware](https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor)
2. [Security notice — malicious version of Anthropic.claude-code... | Cursor](https://cursor.com/blog/claude-code-extension-security-notice)
3. [Claude Code by Anthropic | AI coding agent and assistant](https://claude.com/product/claude-code)
4. [New Claude Code Attack Allows Attackers to Take Full Control... | CybersecurityNews](https://cybersecuritynews.com/new-claude-code-attack/)