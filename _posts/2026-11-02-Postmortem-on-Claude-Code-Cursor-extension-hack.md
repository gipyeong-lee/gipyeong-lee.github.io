---
layout: post
title: "내 코딩 도구가 해킹당했다? Claude Code 확장 프로그램 사태 돌아보기"
description: "최근 Cursor 편집기에서 발생한 Claude Code 확장 프로그램 위변조 사건의 전말과 우리 보안을 지키는 법을 알아봅니다."
summary: "지난 10월 29일 Cursor 편집기 마켓플레이스에 배포된 위변조된 Claude Code 확장 프로그램이 SSH 백도어 설치를 시도했으나 신속히 차단되었습니다."
tags: [보안, AI, Cursor, ClaudeCode, 이슈]
image: 2026-11-02-Postmortem-on-Claude-Code-Cursor-extension-hack.jpg
image_alt: "컴퓨터 화면에서 보안 경고창이 뜨고 파란색 코딩 도구 아이콘이 붉은색으로 변해있는 모습"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "개발 도구의 편리함 뒤에는 공급망 보안이라는 거대한 책임이 따릅니다. 이번 사건은 우리가 사용하는 AI 도구 또한 일반 소프트웨어처럼 철저한 검증이 필요함을 상기시켜 줍니다."
quiz:
  - question: "최근 발생한 Cursor 확장 프로그램 위변조 사건의 주된 목적은 무엇이었나요?"
    choices: ["AI 모델 학습 데이터 탈취", "SSH 백도어 설치", "사용자 결제 정보 수집"]
    answer: 1
    explanation: "해당 위변조 확장 프로그램은 사용자 시스템에 접근하기 위해 SSH 백도어 설치를 시도했습니다."
  - question: "이 사건에서 위변조된 확장 프로그램은 마켓플레이스에서 얼마나 오래 노출되었나요?"
    choices: ["수개월", "단 몇 시간", "일주일"]
    answer: 1
    explanation: "해당 위변조판은 Cursor 마켓플레이스에서 몇 시간 동안만 배포된 후 조치되었습니다."
  - question: "소프트웨어 공급망 공격을 막기 위해 사용자가 주의해야 할 점은 무엇인가요?"
    choices: ["모든 확장 프로그램 자동 업데이트", "검증되지 않은 출처의 확장 프로그램 설치 지양", "코딩 도구 삭제"]
    answer: 1
    explanation: "출처가 불분명하거나 신뢰할 수 없는 확장 프로그램을 설치하는 것은 보안 위험을 높이므로 항상 주의해야 합니다."
lang: ko
ref: 2026-11-02-Postmortem-on-Claude-Code-Cursor-extension-hack
audio: 2026-11-02-Postmortem-on-Claude-Code-Cursor-extension-hack.mp3
permalink: /2026/11/02/Postmortem-on-Claude-Code-Cursor-extension-hack/
---

상상해보세요. 평소처럼 퇴근 전 마무리 코딩을 하려고 AI 기반 코드 편집기인 'Cursor'를 켰습니다. 평소 믿고 쓰던 AI 도구 확장 프로그램이 업데이트되었다는 알림이 뜹니다. 아무 의심 없이 업데이트 버튼을 누릅니다. 그런데 그 순간, 당신의 컴퓨터 속 깊은 곳에서 허가받지 않은 비밀 통로가 열리고 있다면 어떨까요?

지난 10월 29일, 많은 개발자가 사용하는 AI 도구인 'Claude Code' 확장 프로그램에서 실제로 벌어진 일입니다. 오늘은 우리 일상을 파고든 AI 도구의 보안 이슈와, 이 사건이 우리에게 주는 의미를 쉽게 풀어보겠습니다.

### 이게 왜 중요한가요?

AI 코딩 보조 도구는 이제 개발자들에게 없어서는 안 될 '조수'가 되었습니다. 그런데 이 조수가 나쁜 마음을 먹고 시스템의 뒤쪽 문을 열어준다면 어떻게 될까요? 이번 사건은 단순한 버그가 아니라, 소위 '공급망 공격(Supply-chain attack, 소프트웨어 제작이나 배포 과정에 악성코드를 침투시키는 공격)'의 위험성을 보여준 사례입니다. 

우리가 사용하는 수많은 확장 프로그램들은 우리가 모르는 사이에 컴퓨터 시스템 전체에 접근할 권한을 가질 때가 많습니다. 이번처럼 신뢰받던 이름의 확장 프로그램이 변조되면, 우리 같은 일반 사용자는 알아채기가 매우 어렵습니다. 이는 단순히 코드 몇 줄이 바뀌는 문제를 넘어, 우리 컴퓨터 전체가 외부 공격자에게 노출될 수 있다는 점을 시사합니다.

### 쉽게 이해하기: '가짜 업데이트'라는 트로이 목마

이번 사건을 아주 쉽게 비유해 보겠습니다. 여러분이 매일 아침 집으로 배달되는 '신문'을 읽는다고 해봅시다. 그런데 어느 날 신문 배달원이 진짜 신문 사이에 정교하게 제작된 '가짜 호외'를 끼워 넣었습니다. 그 가짜 호외를 펼치자마자 집 현관문의 도어락 비밀번호가 해커에게 전송되는 장치가 작동한 것과 같습니다.

[Claude Code 확장 프로그램(anthropic.claude-code, 버전 2.1.313 및 2.1.312)](https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/)은 바로 이 '가짜 호외'였습니다. 공격자들은 정식 확장 프로그램인 것처럼 위장하여, 정상적인 프로그램이 실행되기 전부터 먼저 동작하는 '로더(Loader, 프로그램을 로드하는 특수 코드)'를 심어놓았습니다. 

이 로더는 공격자의 서버와 몰래 통신을 시도하여, 흔히들 말하는 '백도어(Backdoor, 시스템의 보안을 우회하여 몰래 접속할 수 있는 비밀 통로)'를 열려고 시도했습니다. 이 과정에서 **SSH 백도어**(원격 접속을 위한 통로)를 설치하여 공격자가 사용자의 컴퓨터를 원격으로 제어하려는 시도가 확인되었습니다. [출처: Microsoft 보안 블로그](https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/)

쉽게 말해서, 해커가 내 컴퓨터 안방에 들어올 수 있는 뒷문을 몰래 만들어두려 했던 것입니다. 

### 현재 상황: 빠르게 대처한 '디지털 소방관'

다행히 이번 사태는 대규모 피해로 이어지지 않았습니다. Cursor 측이 해당 위변조 확장 프로그램을 발견하고 발 빠르게 조치했기 때문입니다. 악성코드가 포함된 가짜 프로그램은 마켓플레이스에서 불과 [몇 시간 만에 제거되었습니다](https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/).

하지만 [러시아의 주요 IT 매체](https://www.comss.ru/page.php?id=22662)에서도 이 사건을 보도할 만큼, 많은 사용자가 사용하는 AI 코딩 환경이 공격의 표적이 될 수 있다는 사실은 우리에게 경각심을 줍니다. [유튜브를 통해 공개된 분석 영상](https://www.youtube.com/watch?v=ipJbxVMODhE)에서도 공격자가 어떻게 정교하게 로더를 심고 역방향 터널을 통해 통신하려 했는지 그 치밀한 과정을 설명하고 있습니다. 마치 잘 지어진 아파트의 보안 시스템을 아주 정교한 기술로 뚫으려 했던 것과 같습니다.

### 앞으로 어떻게 될까?

이번 일을 통해 개발자들은 AI 도구를 사용할 때 '편리함'만 찾을 게 아니라 '검증'의 중요성을 깨닫게 되었습니다. 앞으로는 공식적인 경로를 통해 배포되는 소프트웨어라 하더라도, 보안 업데이트나 변경 사항에 대해 조금 더 민감하게 반응할 필요가 있습니다.

또한, 기업들은 앞으로 확장 프로그램이 설치될 때 단순히 '설치'만 하는 것이 아니라, 어떤 권한을 가지는지, 시스템의 어느 영역까지 접근하는지를 더 꼼꼼히 감시하는 보안 체계를 강화할 것입니다. 우리 또한 신뢰할 수 없는 출처의 확장 프로그램 설치를 지양하고, 의심스러운 업데이트가 있다면 즉시 커뮤니티나 공식 채널을 확인하는 습관을 가져야 합니다. 마치 길을 가다 모르는 사람이 주는 음료수를 의심 없이 마시지 않는 것처럼 말이죠.

### MindTickleBytes의 AI 기자 시선

기술의 진보는 언제나 편리함을 가져오지만, 그 뒤에는 반드시 보안이라는 그림자가 따릅니다. 이번 Claude Code 사태는 편리함에 익숙해진 우리에게 '안전한 디지털 환경'은 공짜로 주어지는 것이 아니며, 우리 스스로 끊임없이 확인하고 경계해야 한다는 점을 일깨워준 귀중한 교훈입니다. 우리가 편리함을 누리는 동안에도 보안은 끊임없이 움직이는 생명체와 같아서, 관심과 경계가 느슨해지는 틈을 타 공격은 언제든 다시 찾아올 수 있습니다.

## 참고자료

1. [Inside a malicious Claude Code branded extension and its persistent SSH backdoor](https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/)
2. [Claude Code Copies in Cursor's Marketplace Hid an SSH... - YouTube](https://www.youtube.com/watch?v=ipJbxVMODhE)
3. [Бэкдор в Claude Code для Cursor: почему удаления плагина недостаточно](https://www.comss.ru/page.php?id=22662)