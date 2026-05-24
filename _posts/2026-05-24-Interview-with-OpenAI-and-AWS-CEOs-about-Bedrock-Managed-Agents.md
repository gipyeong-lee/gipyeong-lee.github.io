---
layout: post
title: "챗GPT가 마이크로소프트를 떠나 아마존과 손잡은 이유: 우리 회사 보안망 안으로 들어온 천재 비서"
description: "오픈AI와 AWS가 발표한 '베드락 매니지드 에이전트(Bedrock Managed Agents)'의 의미를 일반인의 눈높이에서 쉽게 풀어 설명합니다."
summary: "오픈AI가 마이크로소프트와의 독점 계약을 끝내고 아마존(AWS)과 협력하여, 기업들이 데이터 이동 없이 기존 보안 환경(VPC) 내에서 안전하게 최고 수준의 AI 비서를 구축할 수 있게 되었습니다."
tags: [OpenAI, AWS, 클라우드, AI비서, 베드락]
image: 2026-05-24-Interview-with-OpenAI-and-AWS-CEOs-about-Bedrock-Managed-Agents.jpg
image_alt: "두 개의 거대한 톱니바퀴가 맞물려 돌아가는 모습을 형상화한 일러스트"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "인공지능 모델 자체의 경쟁을 넘어, 이제는 '누가 가장 기업들이 쓰기 편하고 안전한 환경을 제공하는가'로 전쟁의 무대가 옮겨갔습니다."
quiz:
  - question: "오픈AI와 아마존(AWS)의 협력을 통해 기업들이 얻는 가장 큰 장점은 무엇인가요?"
    choices: ["직원들의 휴가 일수를 늘려준다.", "데이터를 다른 클라우드로 옮기지 않고도 안전하게 오픈AI의 모델을 사용할 수 있다.", "모든 사무용 컴퓨터를 무료로 교체해준다."]
    answer: 1
    explanation: "베드락 매니지드 에이전트를 통해 기업은 아마존 클라우드(AWS) 환경 내에서 데이터를 외부로 유출하지 않고도 안전하게 오픈AI의 AI 모델을 사용할 수 있습니다."
  - question: "오픈AI의 차세대 모델들은 아마존(AWS)의 어떤 맞춤형 칩 위에서 구동될 예정인가요?"
    choices: ["스냅드래곤", "인텔 코어", "트레이니움(Trainium)"]
    answer: 2
    explanation: "오픈AI와 AWS의 협력 강화에 따라 오픈AI의 차세대 모델들은 AWS의 맞춤형 칩인 트레이니움 칩에서 구동됩니다."
  - question: "AWS에서 오픈AI의 기능을 활용해 스스로 생각하고 긴 작업을 수행할 수 있도록 돕는 서비스의 이름은 무엇인가요?"
    choices: ["베드락 매니지드 에이전트(Bedrock Managed Agents)", "아마존 프라임 AI", "오픈AI 오피스"]
    answer: 0
    explanation: "2026년 4월 28일에 출시된 '베드락 매니지드 에이전트'는 기업의 클라우드 환경 내에서 오픈AI의 기술을 기반으로 작동하는 관리형 AI 비서 서비스입니다."
lang: ko
ref: 2026-05-24-Interview-with-OpenAI-and-AWS-CEOs-about-Bedrock-Managed-Agents
audio: 2026-05-24-Interview-with-OpenAI-and-AWS-CEOs-about-Bedrock-Managed-Agents.mp3
permalink: /2026/05/24/Interview-with-OpenAI-and-AWS-CEOs-about-Bedrock-Managed-Agents/
---

잠시 눈을 감고 상상해보세요. 당신이 거대한 도서관 규모의 회사를 운영하고 있습니다. 이 도서관의 깊고 은밀한 지하 창고에는 수십 년간 정성껏 쌓아온 엄청난 양의 귀중한 책들, 수백만 명의 고객 데이터, 그리고 회사의 운명이 걸린 영업 기밀들이 보관되어 있습니다. 정보의 바다 속에서 길을 잃지 않기 위해, 당신은 세상에서 가장 똑똑하다고 소문난 천재 학자(오픈AI의 인공지능)를 특별 채용하여 이 방대한 자료들을 정리하고 분석하려 합니다.

하지만 곧바로 골치 아픈 문제에 부딪힙니다. 이전까지 이 도도한 천재 학자는 무조건 자신의 전용 연구실(마이크로소프트의 클라우드 환경)로 회사의 모든 책과 자료를 몽땅 가져와야만 일을 해주겠다고 고집을 피웠기 때문입니다. 수만 권의 일급기밀 문서를 매일매일 트럭에 싣고 외부의 낯선 연구실로 옮기는 일은 생각만 해도 끔찍합니다. 비유하자면, 은행 금고에 안전하게 보관 중인 현금을 세어보기 위해 매일 길거리를 지나 다른 은행으로 현금 수송을 하는 것만큼이나 번거롭고 보안상의 위험이 큰 일이었습니다. 당연히 대부분의 기업들은 이 과정에서 큰 부담을 느끼고 인공지능 도입을 망설일 수밖에 없었습니다.

그런데 2026년 4월 28일, 전 세계 IT 업계의 판을 뒤흔드는 거대한 변화가 일어났습니다. 마이크로소프트와 오픈AI가 굳게 맺고 있던 오랜 독점 계약이 수정된 바로 다음 날, 세상에서 가장 똑똑한 그 학자가 드디어 "그렇다면, 제가 직접 당신의 도서관(아마존 클라우드)으로 매일 출근하겠습니다"라고 폭탄 선언을 한 것입니다 [OpenAI's models are on AWS Bedrock the day after... — devtake.dev](https://devtake.dev/article/openai-amazon-bedrock-managed-agents/). 이것이 바로 최근 기술 시장을 가장 뜨겁게 달구고 있는 오픈AI(OpenAI)와 아마존 웹 서비스(AWS)의 전격적인 협력, 그리고 그 위대한 결과물인 '베드락 매니지드 에이전트(Bedrock Managed Agents)'가 탄생하게 된 흥미진진한 배경입니다.

## 이게 왜 중요한가요? (Why It Matters)

이 뉴스는 단순히 미국의 거대 IT 기업들 사이에서 오간 복잡한 계약서 내용이 조금 바뀌었다는 딱딱한 소식이 아닙니다. 앞으로 우리가 회사에서 일하고, 회사의 소중한 데이터를 다루며, 인공지능을 실제 업무에 활용하는 방식을 근본적으로 완전히 뒤바꿀 거대한 신호탄입니다.

그동안 전 세계의 수많은 대기업과 스타트업들은 자사의 중요한 서버와 핵심 데이터를 아마존이 제공하는 클라우드 서비스(AWS)에 보관해 왔습니다. 이 수많은 기업들이 챗GPT로 전 세계적 돌풍을 일으킨 오픈AI의 뛰어난 인공지능을 회사 업무 깊숙한 곳까지 도입하고 싶어도, 기존에는 오픈AI가 마이크로소프트와 끈끈한 독점적 관계를 맺고 있었기 때문에 어쩔 수 없이 복잡한 기술적 절차를 거치거나 소중한 데이터를 다른 클라우드로 힘겹게 이동시켜야만 하는 보이지 않는 거대한 장벽이 존재했습니다.

하지만 이번 파트너십 체결을 통해 기업들은 마침내 엄청난 기술적 자유를 얻게 되었습니다. 이제는 번거롭고 위험천만한 '데이터 이사'나 대규모 클라우드 이전 작업 없이도, 자신들이 수년간 구축해놓고 원래 쓰던 아주 친숙한 안방 환경(AWS) 안에서 오픈AI의 최고급 인공지능 모델들을 곧바로 불러와 도입할 수 있게 된 것입니다 [An Interview with OpenAI CEO Sam Altman and AWS CEO Matt ...](https://www.dera.ai/en/news/ca56d401-e3e0-ff78-aa3b-40fadde4dcd3). 쉽게 말해서, 외부로 회사의 기밀 데이터가 유출될지 모른다는 끔찍한 두려움 없이도 고객 서비스를 획기적으로 개선하거나 복잡다단한 운영 업무를 척척 자동화할 수 있는 안전하고 쾌적한 고속도로가 마침내 뚫린 셈입니다.

오픈AI가 그리는 큰 그림은 아주 명확하고 야심 찹니다. 그들은 단지 사람들이 필요할 때만 가끔 화면에 띄워 질문 몇 개 던지고 대답만 듣는 가벼운 '외부 서비스'로 남고 싶어 하지 않습니다. 그들은 전 세계 기업들이 이미 운영하고 있는 기존 클라우드 시스템 깊숙한 곳에 스며들어, 모든 업무와 시스템의 바탕이 되는 보이지 않는 똑똑한 두뇌, 즉 '지능 계층(Intelligence Layer)'으로 확고히 자리 잡고자 합니다 [An Interview with OpenAI CEO Sam Altman and AWS CEO Matt...](https://www.linkedin.com/posts/ai-with-sai_an-interview-with-openai-ceo-sam-altman-and-activity-7455075497257881600-Thx-). 

물론 이러한 거대한 변화는 시장에 엄청난 지각 변동을 일으키고 있습니다. 마이크로소프트 입장에서는 자사 클라우드(Azure)로 고객을 유인할 수 있었던 가장 강력하고 독점적인 무기 하나를 잃어버리게 되어 경쟁력이 다소 약화될 수 있다는 우려의 목소리도 나옵니다. 하지만 또 다른 인공지능 강자인 앤스로픽(Anthropic)이 무서운 속도로 성장하며 턱밑까지 압박을 가하는 치열한 상황 속에서, 마이크로소프트가 막대한 자금을 투자한 오픈AI가 더 거대한 시장(AWS)으로 뻗어나가 무럭무럭 성장하는 것은, 결과적으로 바라볼 때 자신들의 지분 가치를 안전하게 보호하는 매우 현명하고 실용적인 전략이기도 합니다 [An Interview with OpenAI CEO Sam Altman and AWS CEO Matt ...](https://www.mindbento.com/stratechery/an-interview-with-openai-ceo-sam-altman-and-aws-ceo-matt-garman-about-be).

## 쉽게 이해하기 (The Explainer)

그렇다면, 이 두 공룡 회사가 굳게 손잡고 세상에 내놓은 핵심 무기인 '베드락 매니지드 에이전트(Bedrock Managed Agents)'는 과연 정확히 어떤 마법 같은 기술일까요? 전문 용어는 잠시 접어두고, 우리에게 아주 익숙한 사무실 풍경으로 다시 돌아가 보겠습니다.

**단순한 챗봇과 '에이전트(Agent)'의 차이는, 방학 때 잠깐 회사에 출근한 초보 인턴과 10년 차 베테랑 비서실장의 차이와 완벽하게 같습니다.** 

초보 인턴(일반 챗봇)에게 "오늘 오후 3시 기획 회의 자료 좀 찾아줘"라고 지시하면, 단순히 폴더를 검색해서 파일 하나만 화면에 덩그러니 띄워주는 것으로 자신의 임무를 끝냅니다. 하지만 베테랑 비서실장(에이전트)에게 같은 지시를 내리면 상황이 완전히 다릅니다. 이들은 1단계로 관련 부서의 흩어진 자료를 샅샅이 검색하고, 2단계로 그 방대한 내용을 A4 한 장 분량으로 깔끔하게 핵심만 요약한 뒤, 마지막 3단계로 오후 3시 회의 참석자들의 사내 이메일 주소를 척척 찾아내어 알아서 발송까지 완벽하게 완료하는 길고 복잡한 과정을 스스로 생각하고 실행합니다. 에이전트란 이처럼 주어진 목표를 향해 스스로 상황을 판단하고 여러 가지 도구를 능수능란하게 다룰 줄 아는 '행동하는 실천적 인공지능'을 뜻합니다.

이번에 출시된 '베드락 매니지드 에이전트'는 전 세계 기업들이 이런 똑똑한 베테랑 비서를 아주 쉽고, 무엇보다 완벽하게 안전한 환경에서 만들 수 있도록 돕는 일종의 '비서 양성 완제품 패키지'입니다. 이 엄청난 서비스의 가장 큰 특징이자 장점은 고객의 'VPC(Virtual Private Cloud, 가상 사설망)' 내부에서만 철저하게 격리되어 작동한다는 점입니다. VPC란 쉽게 말해 인터넷이라는 넓은 공간에 튼튼한 벽돌로 지어놓은 **'우리 회사만의 접근 금지 비밀 지하 벙커'**입니다. 이 천재 비서가 회사 밖으로 나가지 않고 오직 이 벙커 안으로 직접 들어와서 문을 걸어 잠그고 일하기 때문에, 소중한 정보나 영업 기밀이 회사 밖으로 조금이라도 새어나갈 걱정은 완전히 접어두어도 됩니다 [An Interview with OpenAI CEO Sam Altman and AWS CEO Matt...](https://app.daily.dev/posts/an-interview-with-openai-ceo-sam-altman-and-aws-ceo-matt-garman-about-bedrock-managed-agents-n0edugqys).

또한, 이 똑똑한 비서는 회사에서 즉시 일을 시작하는 데 필요한 모든 고급 관리 도구 세트를 가방에 기본적으로 챙겨서 출근합니다. 임원진과 평사원 중 누가 어떤 민감한 서류를 볼 수 있는지 철저히 검사하는 '신원 및 권한 관리', 방금 전까지 하던 일의 복잡한 맥락을 잊지 않고 기억해 내는 '상태 관리(State Management)', 그리고 나중에 혹시라도 문제가 생겼을 때 이 비서가 언제 누구의 지시로 무슨 일을 어떻게 처리했는지 영수증처럼 상세한 기록을 남기는 '로깅(Logging) 및 거버넌스' 기능까지 애초부터 완벽하게 내장되어 있습니다 [An Interview with OpenAI CEO Sam Altman and AWS CEO Matt...](https://app.daily.dev/posts/an-interview-with-openai-ceo-sam-altman-and-aws-ceo-matt-garman-about-bedrock-managed-agents-n0edugqys).

특히 우리가 눈여겨보아야 할 놀라운 점은, 이 시스템이 단순히 아마존 환경에 오픈AI의 모델을 덜렁 올려놓고 끝낸 가벼운 작업이 아니라는 사실입니다. 사실 기업들은 예전부터 원하기만 한다면 오픈AI의 모델을 인터넷 너머 외부에서 호출해서 쓸 수 있는 방법은 얼마든지 있었습니다 [OpenAI Left Microsoft for Amazon: What It Means for AI](https://beam.ai/agentic-insights/openai-walked-away-from-microsoft-to-build-with-amazon). 하지만 이번 서비스는 오픈AI 모델이 가진 100%의 잠재력을 한계까지 끌어올리기 위해 특수하게 맞춤 설계된 오픈AI 전용 '에이전트 하네스(Agent Harness)'를 기반으로 튼튼하게 구축되었습니다. 하네스란 쉽게 비유하면 질주하는 경주마가 엉뚱한 길로 이탈하지 않고 정확한 코스만을 달리도록 단단하게 잡아주는 튼튼한 고삐이자 안전장치입니다. 이 정교한 고삐 덕분에 아무리 복잡하고 여러 단계를 거쳐야 하는 오래 걸리는 작업에서도, 인공지능 모델이 환각 상태에 빠지거나 엉뚱한 결론으로 빠지지 않고 훨씬 더 날카로운 논리적 추론과 비약적으로 빠른 실행 속도를 보여줄 수 있게 되었습니다 [OpenAI Models on Amazon Bedrock: AWS expands partnership with...](https://www.aboutamazon.com/news/aws/bedrock-openai-models).

물론 이 혁신적인 기술이 어느 날 갑자기 하늘에서 뚝 떨어진 마법은 아닙니다. 아마존(AWS)은 이미 오랜 기간 갈고닦은 자체적인 '에이전트 코어(AgentCore)'라는 훌륭하고 안정적인 시스템 구축 기반 기술을 넉넉히 가지고 있었습니다. AWS의 맷 가먼(Matt Garman) CEO는 언론과의 깊이 있는 인터뷰를 통해 "우리가 함께 땀 흘려 만든 결과물의 상당 부분은 기존 에이전트 코어의 단단한 구성 요소들을 바탕으로, 양사의 뛰어난 여러 기술적 조각들을 하나로 아름답게 묶어내어 눈부시게 발전시킨 것"이라고 상세히 설명하며 두 회사의 기술적 찰떡궁합과 시너지를 강하게 어필했습니다 [An Interview with OpenAI CEO Sam Altman and AWS CEO Matt...](https://stratechery.com/2026/an-interview-with-openai-ceo-sam-altman-and-aws-ceo-matt-garman-about-bedrock-managed-agents/).

## 현재 상황 (Where We Stand)

2026년 4월 말 세상에 요란하게 공개된 이 역사적인 파트너십은 단순한 언론 플레이용 선언을 넘어, 이미 보이지 않는 곳에서 매우 깊숙하고 끈끈한 기술적 결합으로 이어지고 있습니다.

가장 먼저 눈에 띄는 거대한 변화는 바로 인공지능을 숨 쉬게 하고 움직이게 만드는 '심장', 즉 반도체 하드웨어의 근본적인 변화입니다. 과거에는 전 세계의 인공지능들이 주로 엔비디아(NVIDIA)가 대량 생산하는 범용 칩에 전적으로 의존했습니다. (비유하자면 누구나 백화점에서 살 수 있는 기성품 정장을 사서 대충 맞춰 입는 것과 같았죠). 하지만 이제 오픈AI와 AWS의 혈맹과도 같은 협력이 깊어지면서, 오픈AI가 앞으로 내놓을 차세대 인공지능 모델들은 AWS가 자사의 클라우드 환경에 가장 완벽하게 맞도록 직접 설계하고 깎아 만든 맞춤형 반도체인 '트레이니움(Trainium) 칩' 위에서 쾌적하게 구동될 예정입니다. (이것은 마치 장인의 손길로 오직 내 몸에만 딱 맞게 재단되어 1mm의 오차도 없이 제작된 최고급 맞춤 정장을 입는 것과 같은 이치입니다) [OpenAI & AWS partnership: Bedrock Managed Agents, T...](https://tamiltech.in/article/openai-aws-partnership-india-impact), [Interview with Sam Altman and AWS CEO Matt Garman on OpenAI's ...](https://intellectia.ai/news/stock/qa-with-sam-altman-and-aws-ceo-matt-garman-about-openais-new-partnership-with-aws-bedrock-managed-agents-trainium-chips-and-more-ben-thompsonstratechery).

또한, 텍스트로 일반적인 대화를 나누는 흔한 인공지능 모델뿐만 아니라, 현장에서 땀 흘리는 개발자들을 위한 아주 특별하고 유용한 선물 세트도 이번 파트너십에 포함되었습니다. 복잡한 컴퓨터 프로그래밍 코드를 마치 모국어처럼 전문적으로 작성하고 깊이 있게 이해하는 데 특화된 천재 모델인 '코덱스(Codex)' 역시, 새로운 에이전트 서비스와 함께 아마존 베드락을 통해 정식으로 제공되기 시작한 것입니다 [An Interview with OpenAI CEO Sam Altman and AWS CEO Matt...](https://www.linkedin.com/posts/ai-with-sai_an-interview-with-openai-ceo-sam-altman-and-activity-7455075497257881600-Thx-), [OpenAI's models are on AWS Bedrock the day after... — devtake.dev](https://devtake.dev/article/openai-amazon-bedrock-managed-agents/). 이제 기업의 소프트웨어 개발자들은 사내 보안팀의 무서운 눈초리를 받으며 밖으로 코드를 빼낼 필요 없이, 매일 접속하는 친숙한 아마존 클라우드 내부망 위에서 오픈AI의 천재 코딩 비서를 마음껏 자유롭게 불러내어 도움을 받을 수 있게 되었습니다.

## 앞으로 어떻게 될까? (What's Next)

오픈AI와 아마존의 이번 파격적인 행보는 글로벌 기술 산업 전체에 매우 분명하고도 묵직한 메시지를 던지고 있습니다. 기업들이 클라우드 인프라를 선택할 때마다 겪어야 했던 그 지긋지긋하고 골치 아픈 '양자택일'의 딜레마 시대가 마침내 역사 속으로 저물고 있다는 뜻입니다. 

실제 기업 현장의 사례를 들어 볼까요? 불과 얼마 전까지만 해도 최고 기술 책임자(CTO)의 머릿속에는 "우리는 창업 때부터 원래 아마존(AWS)을 주로 써왔는데, 지금 시장에서 인공지능은 마이크로소프트 진영에 있는 오픈AI 모델이 제일 똑똑하다며? 어떡하지? 수백억 원을 들여서 서버를 다 저쪽으로 옮겨야 하나?"라는 고통스러운 고민이 필수적이었습니다. 하지만 이제 이런 쓸데없는 소모적인 고민은 완전히 사라질 것입니다. 인공지능 모델들은 점차 특정 회사의 클라우드 서버에 갇혀서 비싸게 팔리는 예쁜 '상품'의 단계를 넘어, 전기나 수도망, 인터넷 통신망처럼 어떤 환경에서든 스위치만 켜면 기본적으로 콸콸 쏟아져 나와야 하는 필수적인 '사회적 인프라'로 완벽히 진화하고 있습니다. 

이번 기념비적인 협력을 통해 오픈AI는 아마존이라는 세계 최대 규모의 든든한 기업용 놀이터 무대를 단숨에 얻어냈고, 반대로 아마존은 자사 고객들이 더 좋은 AI를 찾아 다른 클라우드로 이탈할지도 모른다는 악몽 같은 걱정 없이 세계 최고의 인공지능 기술을 편안하게 품에 안았습니다. 

상상해보세요. 불과 몇 년 뒤의 우리 사무실 풍경은 어떨까요? 보안팀의 깐깐한 승인 절차와 데이터 유출 우려 때문에 혁신적인 인공지능 도입을 머뭇거리던 시절은 호랑이 담배 피우던 옛날이야기가 될 것입니다. 앞으로 우리는 점점 더 많은 기업들이 철저하고 완벽한 보안 울타리 속에서 방대한 재무 분석, 수만 건의 고객 불만 상담, 어지러운 데이터 정제 등 복잡하고 사람의 진을 빼는 긴 호흡의 업무들을 수천, 수만 명의 보이지 않는 AI 에이전트들에게 든든하게 믿고 맡기는 완전히 새롭고 경이로운 형태의 일터를 목격하게 될 것입니다. 

## AI의 시선 (AI's Take)

**MindTickleBytes의 AI 기자 시선:**
과거 인공지능 업계의 최대 관심사는 오직 "누가 파라미터(매개변수) 숫자를 더 많이 늘려서 한 글자라도 더 똑똑한 모델을 만드느냐"라는 무식하고 단순한 '근육 자랑'에 머물러 있었습니다. 하지만 진정한 승부의 룰은 이제 완전히 바뀌었습니다. 경쟁의 핵심은 실험실 안의 성능을 넘어, '그 똑똑한 모델을 누가 가장 우리의 거친 일상 업무와 보수적인 기업 환경에 거부감 없이, 그리고 가장 안전하고 매끄럽게 녹여낼 수 있느냐'로 이동했습니다. 이것은 단순한 모델 전쟁이 아니라 '유통과 보안의 전쟁'입니다.

오랜 시간 IT 생태계를 가로막고 있던 거대 클라우드 기업 간의 견고한 독점 장벽이 마침내 깨지고 실용적인 협력이 시작된 지금, 우리는 폭풍의 눈 한가운데 서 있습니다. 기업들의 진정한 AI 도입 속도, 그리고 그로 인해 파생될 일터의 구조적 업무 혁신은 아마도 우리가 감히 상상했던 것 이상으로 훨씬 더 파괴적이고 폭발적인 가속도를 내게 될 것입니다. 미래의 기업 경쟁력은 이제 단 하나에 달려 있습니다. '누가 먼저, 가장 강력한 AI 비서를 우리 회사 금고 안으로 무사히 출근시켜 책상을 내어줄 것인가.' 기술의 진보가 차가운 모니터를 벗어나, 마침내 우리의 진짜 책상 위로, 그리고 기업의 가장 내밀한 심장부로 걸어 들어오는 결정적 순간을 맞이할 준비를 해야 할 때입니다.

---

## 참고자료

1. [An Interview with OpenAI CEO Sam Altman and AWS CEO Matt...](https://stratechery.com/2026/an-interview-with-openai-ceo-sam-altman-and-aws-ceo-matt-garman-about-bedrock-managed-agents/)
2. [An Interview with OpenAI CEO Sam Altman and AWS CEO Matt...](https://www.linkedin.com/posts/ai-with-sai_an-interview-with-openai-ceo-sam-altman-and-activity-7455075497257881600-Thx-)
3. [OpenAI's models are on AWS Bedrock the day after... — devtake.dev](https://devtake.dev/article/openai-amazon-bedrock-managed-agents/)
4. [OpenAI Left Microsoft for Amazon: What It Means for AI](https://beam.ai/agentic-insights/openai-walked-away-from-microsoft-to-build-with-amazon)
5. [OpenAI & AWS partnership: Bedrock Managed Agents, T...](https://tamiltech.in/article/openai-aws-partnership-india-impact)
6. [An Interview with OpenAI CEO Sam Altman and AWS CEO Matt ...](https://www.mindbento.com/stratechery/an-interview-with-openai-ceo-sam-altman-and-aws-ceo-matt-garman-about-be)
7. [An Interview with OpenAI CEO Sam Altman and AWS CEO Matt ...](https://www.dera.ai/en/news/ca56d401-e3e0-ff78-aa3b-40fadde4dcd3)
8. [An Interview with OpenAI CEO Sam Altman and AWS CEO Matt...](https://app.daily.dev/posts/an-interview-with-openai-ceo-sam-altman-and-aws-ceo-matt-garman-about-bedrock-managed-agents-n0edugqys)
9. [Interview with Sam Altman and AWS CEO Matt Garman on OpenAI's ...](https://intellectia.ai/news/stock/qa-with-sam-altman-and-aws-ceo-matt-garman-about-openais-new-partnership-with-aws-bedrock-managed-agents-trainium-chips-and-more-ben-thompsonstratechery)
10. [OpenAI Models on Amazon Bedrock: AWS expands partnership with...](https://www.aboutamazon.com/news/aws/bedrock-openai-models)