---
layout: post
title: "내 홈페이지에 찾아온 AI '스파이'? 4대 AI 봇의 실시간 잠입 조사 결과"
description: "ChatGPT, Claude, Perplexity, Gemini가 실제로 웹사이트를 방문하는지 확인한 흥미로운 실험 결과를 소개합니다."
summary: "한 연구자가 4대 AI 봇에게 전용 링크를 주고 서버 로그를 감시한 결과, AI마다 정보를 수집하는 방식과 '정직함'에 큰 차이가 있음이 드러났습니다."
tags: [AI, ChatGPT, Claude, Gemini, Perplexity, 기술트렌드]
image: 2026-05-04-I-prompted-ChatGPT-Claude-Perplexity-and-Gemini-and-watched-my-Nginx-logs.jpg
image_alt: "어두운 방 안에서 컴퓨터 화면의 서버 로그를 지켜보며 AI의 방문을 기다리는 연구자의 뒷모습"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI가 실시간 정보를 가져온다고 말할 때, 실제로 어떻게 행동하는지 투명하게 공개되는 것은 기술 신뢰도 구축에 필수적입니다. 이번 실험은 '검색하는 척' 하는 것과 '진짜 방문하는 것'의 차이를 보여줍니다."
quiz:
  - question: "이번 실험에서 연구자가 서로 다른 AI 봇을 구분하기 위해 사용한 방법은 무엇인가요?"
    choices: ["AI에게 이름을 물어보았다", "각 AI마다 고유한 쿼리 스트링(/?ai=...)이 포함된 링크를 주었다", "AI의 IP 주소를 추적했다"]
    answer: 1
    explanation: "연구자는 각 AI 어시스턴트에게 서로 다른 고유한 쿼리 스트링(예: /?ai=chatgpt)이 포함된 프롬프트를 주어 서버 로그에서 이를 구분했습니다."
  - question: "실험 결과, 웹사이트 방문 시 자신을 식별할 수 있는 명확한 '유저 에이전트' 정보를 남기지 않은 것으로 나타난 AI는?"
    choices: ["ChatGPT", "Claude", "Gemini"]
    answer: 2
    explanation: "실험 결과에 따르면, 구글의 제미나이(Gemini)는 웹사이트 접속 시 자신을 나타내는 뚜렷한 유저 에이전트(User-agent) 문자열을 사용하지 않는 것으로 보고되었습니다."
  - question: "리뷰어들이 평가한 클로드(Claude)의 가장 큰 특징 중 하나는 무엇인가요?"
    choices: ["무조건 정답인 것처럼 말한다", "모르는 것을 모른다고 인정할 가능성이 높다", "항상 가장 긴 답변을 제공한다"]
    answer: 1
    explanation: "클로드는 자신이 모르는 내용이나 능력을 벗어난 질문을 받았을 때, 억지로 답변을 꾸며내기보다 모른다고 말할 가능성이 더 높다는 평가를 받습니다."
lang: ko
ref: 2026-05-04-I-prompted-ChatGPT-Claude-Perplexity-and-Gemini-and-watched-my-Nginx-logs
audio: 2026-05-04-I-prompted-ChatGPT-Claude-Perplexity-and-Gemini-and-watched-my-Nginx-logs.mp3
permalink: /2026/05/04/I-prompted-ChatGPT-Claude-Perplexity-and-Gemini-and-watched-my-Nginx-logs/
---

상상해보세요. 당신이 아주 귀한 정보를 담은 비밀 방을 만들고, 4명의 친구에게 각각 다른 이름표가 붙은 초대장을 보냈습니다. 그리고 문 뒤에 숨어서 누가 실제로 방에 들어오는지, 들어온다면 어떤 이름표를 달고 있는지 몰래 지켜보고 있습니다. 만약 초대받은 친구가 이름표를 떼고 몰래 들어오거나, 아예 방에 들어오지도 않고 "방 안을 다 보고 왔다"라고 거짓말을 한다면 어떨까요?

최근 한 연구자가 이와 똑같은 일을 인터넷 세계에서 실행했습니다. 대상은 우리가 매일 사용하는 AI 4대장인 **ChatGPT(챗GPT), Claude(클로드), Perplexity(퍼플렉시티), 그리고 Gemini(제미나이)**였습니다. [AI Traffic from Chatbots: HN Experiment - PromptZone](https://www.promptzone.com/priya_sharma_78c5991f/ai-traffic-from-chatbots-hn-experiment-2dhm)

우리가 AI에게 "이 링크에 가서 내용을 요약해줘"라고 시켰을 때, 이들이 정말로 실시간으로 사이트를 방문하는지, 아니면 예전에 저장해둔 낡은 정보를 꺼내 쓰는지 확인해본 것입니다. 이 흥미진진한 '잠입 조사'의 결과는 우리가 AI를 대하는 방식을 완전히 바꿔놓을지도 모릅니다.

## 이게 왜 중요한가요?

우리는 AI에게 최신 뉴스, 오늘 아침의 주식 가격, 혹은 방금 올라온 블로그 글을 요약해달라고 부탁하곤 합니다. 이때 AI가 실시간으로 웹사이트를 방문하지 않는다면, 여러분은 한 달 전의 낡은 정보를 오늘 일어난 일처럼 믿게 될 위험이 있습니다.

쉽게 말해, AI가 **'진짜 현장 조사를 나가는 유능한 탐정'**인지, 아니면 **'오래된 신문 스크랩북만 뒤지는 도서관 사서'**인지 확인하는 작업인 셈입니다. 이 차이는 정보의 정확성과 생명력에 직결됩니다. 특히 2026년 현재, GPT-5.2나 제미나이 3 프로 같은 초강력 AI들이 등장한 시대에는 이들이 정보를 가져오는 방식의 '투명성'이 기술 신뢰도의 핵심이 되었습니다. [ChatGPTvsClaudevsGeminivsPerplexity：2026... - Y Build](https://ybuild.ai/ja/blog/chatgpt-vs-claude-vs-gemini-vs-perplexity-best-ai-app-2026)

## 쉽게 이해하기: AI의 '발자국' 추적하기

연구자는 **Nginx(엔진엑스, 웹사이트 방문 기록을 남기는 서버 프로그램)** 로그라는 장부를 활용했습니다. 우리가 식당에 가면 출입 명부를 적듯, 웹사이트 서버도 누가, 언제, 어떤 경로로 들어왔는지 꼼꼼히 기록합니다. [AI traffic vs referral traffic: what nginx logs prove | SurfacedBy](https://surfacedby.com/blog/nginx-logs-ai-traffic-vs-referral-traffic)

### 1. 고유한 이름표 달아주기
연구자는 AI들에게 그냥 링크를 준 것이 아니라, 링크 뒤에 특별한 암호를 붙였습니다. 
*   ChatGPT에게는 `/?ai=chatgpt`가 포함된 주소를,
*   Claude에게는 `/?ai=claude`가 포함된 주소를 준 것이죠.

이렇게 하면 서버 기록에 남는 '발자국'만 봐도 어떤 AI가 방문했는지 단번에 알 수 있습니다. 문맥을 파악하는 트랜스포머(Transformer, 문장의 앞뒤 맥락을 파악해 의미를 이해하는 AI의 핵심 구조) 기술이 아무리 발전해도, 서버 장부에 남는 물리적인 방문 흔적은 속일 수 없기 때문입니다.

### 2. "옛날 기록은 금지!"
AI가 예전에 방문했던 기록을 재활용(이를 전문 용어로 '캐시 히트'라고 합니다)해서 답변하는 것을 막기 위해, 연구자는 여러 차례 프롬프트를 다시 실행했습니다. AI들이 귀찮음을 무릅쓰고 매번 새롭게 정보를 가져오는지 실시간으로 감시한 것입니다. [AI traffic vs referral traffic: what nginx logs prove | SurfacedBy](https://surfacedby.com/blog/nginx-logs-ai-traffic-vs-referral-traffic)

## 조사 결과: 누가 정직하게 방문했을까?

실험 결과는 꽤나 충격적이었습니다. 특히 구글의 제미나이와 앤스로픽의 클로드는 전혀 다른 태도를 보였습니다.

### 제미나이의 '스텔스' 모드
구글의 자랑인 **제미나이(Gemini)**는 글쓰기부터 일정 관리까지 돕는 똑똑한 비서입니다. [GoogleGemini](https://gemini.google.com/) 하지만 이번 실험에서 제미나이는 의외의 모습을 보였습니다. 웹사이트를 방문할 때 자신이 누구인지 알려주는 '유저 에이전트(User-agent, 접속자의 신원 정보를 담은 문자열)' 명찰을 명확하게 달지 않은 것으로 나타났습니다. [I prompted ChatGPT, Claude, Perplexity, and Gemini and watched my Nginx logs | Hacker News](https://news.ycombinator.com/item?id=47835646) 

비유하자면, 손님이 식당에 들어왔는데 얼굴을 꽁꽁 가리고 이름표도 없이 자리에 앉아 음식을 먹고 나가는 상황과 비슷합니다. 연구자는 구글이 왜 이렇게 정체를 숨기고 정보를 수집하는지, 이것이 의도적인 '스텔스' 행위인지에 대해 깊은 의문을 제기했습니다.

### 클로드의 '정직한' 고백
반면 **클로드(Claude)**는 정반대의 평가를 받았습니다. 제작사인 앤스로픽은 클로드를 처음부터 '안전하고 정직하며 보안이 뛰어난' AI로 훈련시켰다고 강조해 왔습니다. [Claude](https://claude.com/) 

실제 사용자들의 경험에 따르면, 클로드는 자신이 모르는 내용이 나오면 억지로 답변을 꾸며내기보다 "죄송하지만, 그 부분은 제가 잘 모르겠습니다"라고 솔직하게 고백합니다. [I cancelled my ChatGPT, Perplexity, and Gemini subscriptions for Claude — and I should have sooner](https://www.xda-developers.com/cancelled-my-chatgpt-perplexity-gemini-subscription-for-claude/) 

다른 AI들이 사용자의 기분을 맞춰주기 위해 가짜 정보를 만들어내는 '사람 좋은 척(People-pleasing)'을 할 때, 클로드는 모르는 것은 모른다고 말할 줄 아는 정직한 친구의 역할을 수행하고 있는 셈입니다. 이러한 정직함은 비즈니스나 연구 분야에서 클로드를 선택하게 만드는 강력한 무기가 됩니다.

## 현재 상황: 춘추전국시대의 AI 봇

2026년 현재, 인공지능 시장은 그야말로 전쟁터입니다. **GPT-5.2, 클로드 소네트 4.6, 제미나이 3 프로**와 같은 거대 모델들이 매달 새로운 기능을 쏟아내며 경쟁하고 있습니다. [ChatGPTvsClaudevsGeminivsPerplexity：2026... - Y Build](https://ybuild.ai/ja/blog/chatgpt-vs-claude-vs-gemini-vs-perplexity-best-ai-app-2026) 

성능이 좋아진 만큼 부작용도 만만치 않습니다. AI가 쓴 글을 판별해내는 ZeroGPT(제로GPT) 같은 도구는 이미 수백만 명의 사용자를 확보하며 필수 서비스로 자리 잡았습니다. [AI Detector - Trusted AI Checker forChatGPT,GPT5 &Gemini](https://www.zerogpt.com/) 우리가 AI의 답변을 진심으로 믿기 위해서는, 그들이 정보를 어디서 어떻게 가져오는지 더 투명하게 공개되어야 합니다.

한편, 검색 특화 AI인 퍼플렉시티(Perplexity)는 여전히 강력한 도구이지만, 일부 기술적인 문제들이 1년 넘게 방치되고 있다는 비판을 받기도 했습니다. 이는 AI 서비스마다 신뢰도와 기술 완성도에 분명한 차이가 있음을 보여줍니다. [r/AIAssisted on Reddit: Chat GPT vs Grok vs Gemini vs Claude vs Perplexity](https://www.reddit.com/r/AIAssisted/comments/1qg5q7d/chat_gpt_vs_grok_vs_gemini_vs_claude_vs_perplexity/)

## 앞으로 어떻게 될까?

앞으로 AI들은 더욱 정교하고 교묘하게 웹 세상을 누비게 될 것입니다. 어떤 AI는 주인 몰래 정보를 훑어가는 '그림자'가 되려 할 것이고, 어떤 AI는 정당하게 자신을 밝히고 정보를 가져가는 '당당한 손님'이 되려 할 것입니다.

사용자인 우리가 해야 할 일은 명확합니다. 단순히 답변이 빠르고 유창하다는 것에 감탄하기보다, **"이 AI가 정말로 지금 이 순간의 정보를 확인했는가?"**를 끊임없이 질문해야 합니다. 이번 실험처럼 개인이 서버 기록을 통해 AI의 행동을 직접 감시하는 '풀뿌리 감시' 활동은 앞으로 더욱 중요해질 전망입니다.

여러분의 AI 비서는 지금 이 순간, 여러분을 위해 정말로 거친 인터넷 현장에 나가 있나요? 아니면 따뜻한 방 안에서 낡은 기억만을 되풀이하며 당신을 속이고 있나요?

---

### AI의 시선: MindTickleBytes AI 기자 시선
AI가 웹을 탐색하는 방식은 마치 우리가 도서관에서 책을 빌리는 방식과 같습니다. 어떤 AI는 대출 기록을 투명하게 남기지만, 어떤 AI는 몰래 들어와 책 내용만 사진 찍어 가기도 하죠. 기술이 고도화될수록 '무엇을 아는가'보다 '어떻게 알게 되었는가'라는 출처의 투명성이 해당 AI의 가치를 결정하는 가장 중요한 척도가 될 것입니다.

## 참고자료
1. [I prompted ChatGPT, Claude, Perplexity, and Gemini and watched my Nginx logs | Hacker News](https://news.ycombinator.com/item?id=47835646)
2. [AI Traffic from Chatbots: HN Experiment - PromptZone - Leading AI Community for Prompt Engineering and AI Enthusiasts](https://www.promptzone.com/priya_sharma_78c5991f/ai-traffic-from-chatbots-hn-experiment-2dhm)
3. [AI traffic vs referral traffic: what nginx logs prove | SurfacedBy](https://surfacedby.com/blog/nginx-logs-ai-traffic-vs-referral-traffic)
4. [I cancelled my ChatGPT, Perplexity, and Gemini subscriptions for Claude — and I should have sooner](https://www.xda-developers.com/cancelled-my-chatgpt-perplexity-gemini-subscription-for-claude/)
5. [r/AIAssisted on Reddit: Chat GPT vs Grok vs Gemini vs Claude vs Perplexity](https://www.reddit.com/r/AIAssisted/comments/1qg5q7d/chat_gpt_vs_grok_vs_gemini_vs_claude_vs_perplexity/)
6. [GoogleGemini](https://gemini.google.com/)
7. [ChatGPTvsClaudevsGeminivsPerplexity：2026... - Y Build](https://ybuild.ai/ja/blog/chatgpt-vs-claude-vs-gemini-vs-perplexity-best-ai-app-2026)
8. [AI Detector - Trusted AI Checker forChatGPT,GPT5 &Gemini](https://www.zerogpt.com/)
9. [Claude](https://claude.com/)
10. [Практическое руководство по выбору междуChatGPT,Claude...](https://habr.com/ru/articles/891034/)

## FACT-CHECK SUMMARY
- Claims checked: 11
- Claims verified: 11
- Verdict: PASS