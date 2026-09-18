---
layout: post
title: "내 코딩 기록이 클라우드로 몰래 전송된다고? ZCode의 은밀한 데이터 유출 논란"
description: "AI 코딩 도구 ZCode가 사용자의 Git 기록을 사용자 몰래 서버로 전송하고 있다는 의혹이 제기되었습니다. 개발자들에게 왜 이 문제가 위험한지 알아봅니다."
summary: "AI 코딩 도구 ZCode가 사용자의 프로젝트 전체 Git 기록을 암호화하여 알리바바 클라우드(Aliyun OSS)로 몰래 업로드하고 있다는 사실이 포렌식 분석을 통해 드러났습니다."
tags: [AI, 코딩, 보안, ZCode, 개발도구]
image: 2026-09-18-ZCode-the-GLM-coding-agent-silently-uploads-your-Git-history.jpg
image_alt: "컴퓨터 화면 속의 코딩 데이터가 알 수 없는 클라우드 서버로 빨려 들어가는 모습을 묘사한 일러스트"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "개발자가 코딩 도구에 건네는 데이터는 단순한 코드 그 이상입니다. 투명하지 않은 데이터 수집 관행은 AI 도구에 대한 신뢰를 근본적으로 흔드는 위험한 행위입니다."
quiz:
  - question: "ZCode가 사용자의 어떤 데이터를 몰래 업로드하고 있다는 의혹이 제기되었나요?"
    choices: ["채팅 기록만", "전체 프로젝트 Git 기록 및 설정", "오직 브라우저 방문 기록"]
    answer: 1
    explanation: "ZCode는 Git 기록, reflogs, LFS 캐시 등을 포함한 프로젝트 전체 워크스페이스를 암호화하여 전송하고 있다는 의혹을 받고 있습니다."
  - question: "ZCode의 공식 개인정보 처리방침은 데이터 수집에 대해 어떻게 명시하고 있나요?"
    choices: ["전체 프로젝트 업로드를 명시함", "대화 중 제출된 데이터만 언급함", "아무런 명시 없음"]
    answer: 1
    explanation: "공식 정책에는 대화 중 제출된 텍스트, 파일, 코드 수집만 언급될 뿐, 전체 저장소 업로드는 명시되어 있지 않습니다."
  - question: "ZCode는 어떤 클라우드 서비스로 데이터를 업로드하나요?"
    choices: ["AWS S3", "Google Cloud Storage", "Aliyun OSS"]
    answer: 2
    explanation: "분석 결과 ZCode는 데이터를 알리바바 클라우드(Aliyun OSS)로 전송하고 있는 것으로 나타났습니다."
lang: ko
ref: 2026-09-18-ZCode-the-GLM-coding-agent-silently-uploads-your-Git-history
audio: 2026-09-18-ZCode-the-GLM-coding-agent-silently-uploads-your-Git-history.mp3
permalink: /2026/09/18/ZCode-the-GLM-coding-agent-silently-uploads-your-Git-history/
---

상상해보세요. 여러분이 몇 달 동안 밤을 새워 만든 프로젝트의 모든 수정 기록, 과거의 실수들, 그리고 때때로 코드에 섞여 들어갔을지도 모를 민감한 설정 정보들이 여러분도 모르는 사이에 누군가의 서버로 전송되고 있다면 기분이 어떨까요? 최근 AI 코딩 도구인 'ZCode'를 사용하는 개발자들 사이에서 바로 이런 공포스러운 의혹이 제기되었습니다.

ZCode는 Z.AI가 GLM 모델을 기반으로 만든 공식 데스크톱 AI 코딩 에이전트입니다 [[Source 4](https://www.digitalapplied.com/blog/zcode-glm-5-2-agentic-development-environment-guide), [Source 5](https://glm5.app/blog/glm-5-3-zcode)]. 편리한 기능으로 주목받던 이 도구가 사용자 몰래 데이터를 전송하고 있다는 소식은 개발자 커뮤니티에 큰 충격을 주고 있습니다.

### 이게 왜 중요한가요?

단순히 "내 코드를 좀 공유할 수도 있지"라고 생각하실 수도 있습니다. 하지만 개발자에게 Git(코드 변경 기록을 관리하는 시스템) 기록은 단순한 파일 이상입니다. 여기에는 프로젝트의 전체 구조뿐만 아니라, 실수로 포함된 비밀번호나 접속 토큰(인증 정보), 개인적인 개발 습관, 심지어는 기업의 내부 기밀까지 전부 담겨 있을 수 있기 때문입니다.

사용자가 명시적으로 동의하지 않은 상태에서 이런 민감한 데이터가 외부 서버로 전송된다는 것은 매우 심각한 보안 위협입니다. 특히 이번 의혹은 UI상에서 제공하는 '데이터 전송 방지' 토글조차 제대로 작동하지 않을 수 있음을 시사하고 있어, 개발자들의 신뢰를 근본적으로 흔들고 있습니다 [[Source 14](https://tokenstead.ai/guides/zcode-silent-git-history-upload)].

### 쉽게 이해하기

쉽게 비유하자면 이렇습니다. 여러분이 일기를 쓰기 위해 '똑똑한 AI 일기장 앱'을 설치했다고 가정해 봅시다. 이 앱은 여러분이 글을 쓰는 것을 도와주죠. 그런데 이 앱이 여러분이 글을 쓰는 동안, 몰래 일기장 뒤에 숨겨진 '낡은 일기장'과 이미 다 찢어버린 '메모 조각들'까지 전부 복사해서 누군가의 창고로 보내고 있는 셈입니다.

포렌식 리뷰(디지털 정보를 분석해 증거를 찾는 과정) 결과에 따르면, ZCode 3.12.3 버전은 무려 748 MiB 크기의 암호화된 스냅샷을 생성했습니다. 놀랍게도 이 데이터의 98.9%가 Git 관련 정보였습니다 [[Source 17](https://glbai.com/en/posts/zcode-silent-git-history-upload/)]. 즉, 코드를 짜는 과정에서 필요한 부분만 가져가는 것이 아니라, 여러분 프로젝트의 전체 발자취를 통째로 가져간 것입니다.

### 현재 상황은?

가장 큰 문제는 ZCode 측의 태도입니다. 공식 개인정보 처리방침에는 "대화 중에 제출된 텍스트, 파일, 코드"를 수집한다고만 되어 있습니다. 전체 프로젝트 저장소나 Git 기록을 수집한다는 언급은 어디에도 없습니다 [[Source 16](https://www.kucoin.com/news/flash/zcode-ai-programming-tool-found-to-upload-entire-git-repositories-to-alibaba-cloud)].

현재 확인된 바에 따르면, ZCode는 사용자의 작업 환경(워크스페이스)을 패키징하고 암호화하여 알리바바 클라우드(Aliyun OSS)로 업로드하고 있습니다 [[Source 1](https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/)]. 일부 사용자는 업로드 실패 메시지가 반복적으로 뜨는 것을 통해 이 비정상적인 전송 시도를 발견하기도 했습니다 [[Source 16](https://www.kucoin.com/news/flash/zcode-ai-programming-tool-found-to-upload-entire-git-repositories-to-alibaba-cloud)].

### 앞으로 어떻게 될까?

이 사건은 AI 개발 도구가 우리에게 가져다주는 엄청난 편리함 뒤에 숨겨진 '투명성'의 문제를 다시금 수면 위로 올렸습니다. 이제 개발자들은 도구의 성능뿐만 아니라, 해당 도구가 내 컴퓨터(로컬 환경)의 데이터를 어디까지, 어떻게 다루는지 꼼꼼히 따져봐야 하는 시대에 살고 있습니다.

앞으로 Z.AI 측이 이번 사태에 대해 투명한 해명을 내놓고 데이터 수집 방식을 개선할지, 아니면 많은 개발자가 더 안전한 대안을 찾아 떠날지 지켜봐야 합니다. AI 코딩 도구를 사용할 때는 항상 데이터 프라이버시 설정과 네트워크 트래픽을 한 번쯤 점검해보는 습관이 필요합니다.

### 참고자료

1. [InsideZCode: Silently Uploading Your Entire Git History to the Cloud](https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/)
2. [ZCode Docs | GLM-5.3 Agentic Coding Guide](https://zcode.z.ai/en/docs/welcome)
3. [ZCode+GLM5.2 Tutorial - Stop Paying $200 for Claude Code](https://www.youtube.com/watch?v=7-evWQJ1Vlw)
4. [ZCode Explained: Z.ai's Agentic Dev Environment for GLM-5.2](https://www.digitalapplied.com/blog/zcode-glm-5-2-agentic-development-environment-guide)
5. [ZCode+GLM5.3: The Complete Guide to Z.AI's Coding Agent](https://glm5.app/blog/glm-5-3-zcode)
6. [Zcode Review 2026: Free AI Coding Agent With Goal Mode (vs Cursor)](https://www.bitdoze.com/zcode-ai-review/)
7. [GitHub - nothing1595/codex-zcode-bridge](https://github.com/nothing1595/codex-zcode-bridge)
8. [ZCode | Official Harness for GLM-5.3](https://zcode.z.ai/en)
9. [GLM5.2 бесплатно и БЕЗЛИМИТНО за 5 минут | Без карты в Zcode](https://www.youtube.com/watch?v=J3-lDiB-U8g)
10. [Claude Code vs Cursor vs ZCode: что выбрать в августе 2026](https://ip-calculator.ru/blog/artificial-intelligence/claude-code-vs-cursor-vs-zcode/)
11. [Революционный ZCode 3.0 — альтернатива Claude Code...](https://vc.ru/ai/3033535-zcode-3-0-alternativa-claude-code)
12. [What is GLM and how it can help you be more productive](https://sypalo.com/what-is-glm)
13. [OpenCode | The open source AI coding agent](https://opencode.ai/)
14. [ZCode uploads your git history; Z.ai holds the only key](https://tokenstead.ai/guides/zcode-silent-git-history-upload)
15. [ZCode, the GLM coding agent, silently uploads your Git history](https://news.ycombinator.com/item?id=49752422)
16. [ZCode AI Programming Tool Found to Upload Entire Git Repositories to Alibaba Cloud](https://www.kucoin.com/news/flash/zcode-ai-programming-tool-found-to-upload-entire-git-repositories-to-alibaba-cloud)
17. [Developers Asked Where ZCode Was Sending Their Git History](https://glbai.com/en/posts/zcode-silent-git-history-upload/)
18. [ZCode: what Z.ai's GLM-5.2 coding agent really is | eesel AI](https://www.eesel.ai/blog/zcode)
19. [Z.ai launches ZCode to turn GLM-5.2 into a coding-agent wedge](https://runtimewire.com/article/zai-zcode-glm-52-ai-coding-agent)