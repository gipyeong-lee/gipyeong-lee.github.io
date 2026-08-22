---
layout: post
title: "생애 첫 번째 Dapp 을 완성하였습니다."
description: "안녕하세요? Slow Thinking 입니다. 약 한달간 개발을 진행하였습니다. AI 가 없었다면 개발하지 못했을 거에요. 게으른 제가 선택한 방법은 다음과 같습니다. Visual studio code 의 좌, 우측 패널에 각각 codex, claude code 를 셋팅하고. To..."
date: 2025-10-18 20:57:34 +0900
section: blog
category: web3
lang: ko
ref: 2025-10-18-legacy-391-web3-dapp
tags:
  - "Ai"
  - "Claude"
  - "Codex"
  - "DAPP"
  - "Project"
  - "Projects"
---

<p>
안녕하세요? Slow Thinking 입니다.
</p>
<p>
약 한달간 개발을 진행하였습니다.
</p>
<p>
AI 가 없었다면 개발하지 못했을 거에요.
</p>
<p>
게으른 제가 선택한 방법은 다음과 같습니다.
</p>

<p>
Visual studio code 의 좌, 우측 패널에 각각 codex, claude code 를 셋팅하고.
</p>
<p>
Token limit 에 걸리면 번갈아가며 진행하였고. 아래는 두 tool 에 대해서 비교한 표입니다. 참고해주세요.
</p>

<table>
<tbody>
<tr>
<td>
<b>
항목
</b>
</td>
<td>
<b>
Codex CLI ( OpenAI )
</b>
</td>
<td>
<b>
Claude Code CLI (Anthropic)
</b>
</td>
</tr>
<tr>
<td>
<b>
플랜명
</b>
</td>
<td>
ChatGPT Plus (월 $20) 내 Codex CLI 포함
</td>
<td>
Claude Pro (월 $20)
</td>
</tr>
<tr>
<td>
<b>
세션 제한 방식
</b>
</td>
<td>
약
<b>
5시간 롤링 윈도우
</b>
(5시간마다 사용량 리셋)
</td>
<td>
약
<b>
5시간 롤링 윈도우
</b>
(5시간마다 리셋)
</td>
</tr>
<tr>
<td>
<b>
세션 한도 (대략)
</b>
</td>
<td>
30 ~ 150 개의 로컬 메시지 또는 5 ~ 40 개의 클라우드 작업
</td>
<td>
약 45 메시지 또는 10 ~ 40 프롬프트 수준
</td>
</tr>
<tr>
<td>
<b>
주간 누적 한도
</b>
</td>
<td>
<b>
공유 주간 할당량(weekly quota)
</b>
존재 (공식 수치 비공개)
</td>
<td>
약
<b>
7일 단위
</b>
리셋되는 주간 한도 존재
</td>
</tr>
<tr>
<td>
<b>
리셋 시점 (세션)
</b>
</td>
<td>
첫 요청 후 5시간 지나면 자동 리셋
</td>
<td>
첫 프롬프트 후 5시간 지나면 자동 리셋
</td>
</tr>
<tr>
<td>
<b>
리셋 시점 (주간)
</b>
</td>
<td>
약
<b>
일주일
</b>
주기로 리셋 (정확 시각 비공개)
</td>
<td>
약
<b>
7일
</b>
후 리셋 (계정별 시간 상이)
</td>
</tr>
<tr>
<td>
<b>
토큰 컨텍스트 창
</b>
</td>
<td>
약
<b>
192 000 토큰
</b>
(입력 + 출력 + 내역 합산 추정)
</td>
<td>
약
<b>
200 000 토큰
</b>
(Pro 기준)최대 500 000 (Enterprise)
</td>
</tr>
<tr>
<td>
<b>
기본 모델
</b>
</td>
<td>
GPT-4 Turbo (Code 해석용 모드)
</td>
<td>
Claude 3 Sonnet (코딩 모드)
</td>
</tr>
<tr>
<td>
<b>
초과 시 메시지
</b>
</td>
<td>
“Usage limit reached. Try again in X hours.”
</td>
<td>
“You’ve hit your limit. Resets in ~X hours.”
</td>
</tr>
<tr>
<td>
<b>
리셋 방식
</b>
</td>
<td>
자동 롤링 리셋 (수동 초기화 불가)
</td>
<td>
자동 롤링 리셋 (5시간 후 세션 갱신)
</td>
</tr>
<tr>
<td>
<b>
추가 특징
</b>
</td>
<td>
- 로컬 vs 클라우드 작업 구분- 코드 실행 기능 포함
</td>
<td>
- /clear, /compact 명령으로 컨텍스트 축소 가능- Sonnet 4 중심 모델 지원
</td>
</tr>
<tr>
<td>
<b>
공식 출처 예시
</b>
</td>
<td>
<a href="https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan">
help.openai.com
</a>
</td>
<td>
<a href="https://claudelog.com/faqs/claude-code-usage/">
claudelog.com
</a>
/
<a href="https://portkey.ai/blog/claude-code-limits/">
portkey.ai
</a>
</td>
</tr>
</tbody>
</table>

<p>
다음은 이번 Project L 에 대한 정보입니다.
</p>


<table>
<tbody>
<tr>
<td>
<b>
프로젝트명
</b>
</td>
<td>
Project L
</td>
</tr>
<tr>
<td>
<b>
개발 언어
</b>
</td>
<td>
Rust (온체인 프로그램) + TypeScript (클라이언트 / 프런트엔드)
</td>
</tr>
<tr>
<td>
<b>
플랫폼
</b>
</td>
<td>
Solana Blockchain (Anchor Framework )
</td>
</tr>
<tr>
<td>
<b>
개발 기간
</b>
</td>
<td>
2025.09.29 ~ 2025.10.18 (총 19 일, 38 시간)
</td>
</tr>
<tr>
<td>
<b>
주요 목표
</b>
</td>
<td>
Solana 네트워크에서 스마트 컨트랙트 배포 및 클라이언트 연동 완료
</td>
</tr>
<tr>
<td>
<b>
Dependency Graph
</b>
</td>
<td>
총 2,130 dependencies (패키지, 모듈, 빌드 종속성 포함 )
</td>
</tr>
</tbody>
</table>

<p>
개발은 완료하였고. 현재 self QA 를 진행중에 있습니다.
</p>
<p>
이후 릴리즈를 진행해볼 예정입니다.
</p>

<hr>

<blockquote>
<s>
devnet QA - Completed
</s>
<br>
testnet QA -
<b>
On going
</b>
<br>
Deploy on mainnet  - To do
</blockquote>
