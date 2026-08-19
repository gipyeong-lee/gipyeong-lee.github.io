---
layout: post
title: "AI에게 민감한 정보 줘도 될까? '제로 데이터 보존(ZDR)'이 뭐길래"
description: "기업들이 AI를 안전하게 사용하기 위해 도입하는 '제로 데이터 보존' 계약의 의미와 한계를 쉽게 설명합니다."
summary: "제로 데이터 보존(ZDR)은 AI 제공 업체가 사용자의 데이터를 즉시 삭제하고 학습에 사용하지 않겠다고 약속하는 강력한 보안 계약입니다."
tags: [AI보안, 데이터프라이버시, 제로데이터보존, ZDR]
image: 2026-08-20-Offering-Zero-Data-Retention-for-frontier-modelsCompanyAug-19-2026.jpg
image_alt: "디지털 보안 자물쇠와 AI 모델이 연결된 모습을 나타내는 그래픽"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "기업이 AI의 성능과 보안 사이에서 균형을 잡으려는 노력이 돋보입니다. ZDR은 단순한 설정이 아닌 계약이라는 점을 반드시 기억해야 합니다."
quiz:
  - question: "제로 데이터 보존(ZDR)의 핵심 약속은 무엇인가요?"
    choices: ["데이터를 30일간 보관한다", "데이터를 추론 즉시 삭제하고 학습에 활용하지 않는다", "모든 대화 내용을 공개한다"]
    answer: 1
    explanation: "ZDR은 데이터를 추론하는 순간 이후 보관하지 않으며, 학습이나 서비스 개선을 위해 사용하지 않겠다는 계약입니다."
  - question: "ZDR 계약 시 주의해야 할 점은 무엇인가요?"
    choices: ["성능이 무조건 저하된다", "모든 AI 기능에 적용된다", "상태 유지형(stateful) 기능 등은 계약 범위에서 제외될 수 있다"]
    answer: 2
    explanation: "ZDR은 주로 상태를 유지하지 않는(stateless) 경로에 적용되며, 복잡한 에이전트 시스템의 기능은 제외될 수 있습니다."
  - question: "최근 일부 모델(예: Claude Fable 5)에서 일어난 변화는 무엇인가요?"
    choices: ["ZDR을 강제화했다", "ZDR 대신 30일 데이터 보관 정책을 채택했다", "데이터 보관을 아예 중단했다"]
    answer: 1
    explanation: "Claude Fable 5 모델은 제로 데이터 보존 정책 대신 안전성 확보를 위해 30일 데이터 보관 정책으로 변경되었습니다."
lang: ko
ref: 2026-08-20-Offering-Zero-Data-Retention-for-frontier-modelsCompanyAug-19-2026
audio: 2026-08-20-Offering-Zero-Data-Retention-for-frontier-modelsCompanyAug-19-2026.mp3
permalink: /2026/08/20/Offering-Zero-Data-Retention-for-frontier-modelsCompanyAug-19-2026/
---

상상해보세요. 여러분이 다니는 회사에서 최신 AI를 활용해 아주 비밀스러운 프로젝트의 데이터를 분석하려고 합니다. 하지만 막상 AI에 그 정보를 입력하려고 하니 덜컥 겁이 납니다. "이 데이터가 AI 회사의 서버에 기록되거나, 나중에 다른 사람의 질문에 대한 답변으로 흘러나오지는 않을까?" 하는 걱정 때문이죠. 

이런 고민을 해결하기 위해 등장한 개념이 바로 '제로 데이터 보존(Zero Data Retention, 이하 ZDR)'입니다. 과연 이것이 우리의 데이터를 정말로 안전하게 지켜줄 수 있는 마법의 방패일까요?

## 이게 왜 중요한가요?

과거에는 공공 클라우드 서비스를 이용할 때 데이터가 서버에 남는 것이 당연했습니다. 하지만 기업 입장에서는 고객의 개인정보나 회사의 핵심 기밀을 외부 AI 모델에 전달하는 것 자체가 큰 보안 위험입니다. ZDR은 이러한 기업들이 마음 놓고 최첨단 AI 모델(Frontier Models, 거대 AI 모델)을 업무에 활용할 수 있도록 돕는 일종의 '보안 계약서'입니다 [출처: Zero Data Retention AI: Same Models, No Retention | BrainPack](https://www.brainpack.ai/infrastructure/deployment/zdr). ZDR을 사용하면 데이터를 보낼 때 남는 '기록의 꼬리표'를 없앨 수 있기 때문에, 보안에 민감한 금융, 의료, 법률 분야에서 특히 중요한 선택지로 떠오르고 있습니다.

## 쉽게 이해하기: 기억상실증에 걸린 도우미

쉽게 비유하자면, ZDR은 '기억상실증에 걸린 도우미'를 고용하는 것과 같습니다. 

일반적인 AI는 사용자가 질문을 하면 그 내용과 답변을 서버에 차곡차곡 저장합니다. 마치 꼼꼼한 비서가 모든 대화 내용을 기록해두는 것과 같죠. 하지만 ZDR을 적용한다는 것은 이 비서에게 "내가 질문을 던지고 네가 답을 하는 그 짧은 순간에만 내 말을 듣고, 답이 끝나면 바로 모든 내용을 뇌 속에서 지워버려"라고 계약하는 것과 같습니다.

업체 측은 이 계약을 통해 데이터를 추론(AI가 질문에 답을 생성하는 과정)하는 순간 이후에는 데이터를 보관하지 않고, 모델 학습이나 서비스 개선을 위해서도 사용하지 않겠다고 문서로 약속합니다 [출처: Zero Data Retention AI: Same Models, No Retention | BrainPack](https://www.brainpack.ai/infrastructure/deployment/zdr). 이 과정에서 데이터가 외부로 유출될 위험이 있는 '감시 기록'조차 생성하지 않는 경우도 있습니다 [출처: Zero Data Retention AI: Same Models, No Retention | BrainPack](https://www.brainpack.ai/infrastructure/deployment/zdr).

## 어디까지 믿어야 할까요?

ZDR이 만능 해결책은 아닙니다. 가장 주의해야 할 점은 **ZDR은 단순한 '설정 버튼'이 아니라 법적인 '계약'**이라는 사실입니다 [출처: Zero data retention | Agentic Delivery Glossary](https://readysolutions.ai/glossary/zero-data-retention/). 

많은 사용자가 ZDR 계약만 맺으면 모든 기능이 완벽하게 보호될 것이라고 오해합니다. 하지만 데이터가 AI의 '상태 유지형 기능(stateful features, 이전 대화나 작업 맥락을 기억해야 하는 기능)'을 사용하는 경로로 넘어가면 ZDR 보호를 받지 못할 수 있습니다 [출처: Zero data retention | Agentic Delivery Glossary](https://readysolutions.ai/glossary/zero-data-retention/). 마치 도우미가 '지금 당장'은 기억을 지우더라도, 특정 '기억 저장소'를 활용해야 하는 복잡한 업무를 맡기면 그 기록은 어딘가에 남게 되는 것과 비슷한 이치입니다.

또한, 최근 보안 정책 변화도 눈여겨봐야 합니다. 앤스로픽(Anthropic)은 안전성 강화를 위해 일부 모델에 대해 30일간 데이터를 보관하는 정책을 도입했고, Claude Fable 5 모델의 경우 기존의 제로 데이터 보존 정책을 거두고 이 30일 보관 정책을 채택하기도 했습니다 [출처: Data retention practices for Covered Models | Anthropic Help Center](https://support.claude.com/en/articles/15425996-data-retention-practices-for-covered-models) [출처: Fable 5's 30-Day Retention: The End of Zero Retention? | Digital Applied](https://www.digitalapplied.com/blog/fable-5-30-day-data-retention-zdr-enterprise-2026).

## 앞으로의 전망

앞으로 AI 보안 시장은 더욱 세분화될 것으로 보입니다. 기업들은 성능이 뛰어난 AI를 쓰되, 보안의 중요성에 따라 ZDR이 적용되는 모델과 그렇지 않은 모델을 골라 쓰는 방식을 취할 것입니다. ZDR은 더 높은 비용을 지불해야 하는 고급 보안 서비스로 자리를 잡아가고 있습니다 [출처: Zero Data Retention AI: Same Models, No Retention | BrainPack](https://www.brainpack.ai/infrastructure/deployment/zdr). 

기업 담당자라면 앞으로 우리가 사용하는 AI 서비스가 어떤 경로로 데이터를 처리하는지, 그리고 ZDR 계약의 범위가 어디까지인지 꼼꼼히 확인하는 것이 필수입니다. "AI가 알아서 해주겠지"라고 믿기보다는, 데이터가 처리되는 구조를 명확히 이해하고 계약하는 지혜가 필요합니다.

## MindTickleBytes의 AI 기자 시선

보안과 성능은 시소와 같아서 한쪽을 올리면 한쪽이 내려가기 마련입니다. ZDR은 이 시소의 균형을 맞추려는 기업들의 고군분투를 보여줍니다. 기술의 편리함 뒤에 숨겨진 계약 조건을 꼼꼼히 살피는 눈을 길러야 할 때입니다.

## 참고자료
1. [Zero data retention | Agentic Delivery Glossary](https://readysolutions.ai/glossary/zero-data-retention/)
2. [Zero Data Retention AI: Same Models, No Retention | BrainPack](https://www.brainpack.ai/infrastructure/deployment/zdr)
3. [Frontier Safety Roadmap Updates | Anthropic](https://www.anthropic.com/responsible-scaling-policy/updates)
4. [Data retention practices for Covered Models | Anthropic Help Center](https://support.claude.com/en/articles/15425996-data-retention-practices-for-covered-models)
5. [Fable 5's 30-Day Retention: The End of Zero Retention? | Digital Applied](https://www.digitalapplied.com/blog/fable-5-30-day-data-retention-zdr-enterprise-2026)