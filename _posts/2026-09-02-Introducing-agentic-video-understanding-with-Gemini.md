---
layout: post
title: "AI가 영상을 그저 '보는' 걸 넘어 '조사'하기 시작했다? 에이전트형 영상 이해 기술의 등장"
description: "구글 제미나이(Gemini)에 도입된 새로운 에이전트형 영상 이해 기술이 어떻게 AI의 영상 분석 방식을 바꾸고 있는지 쉽게 설명해 드립니다."
summary: "구글이 제미나이 모델에 도입한 '에이전트형 영상 이해' 기술은 AI가 영상을 단순히 보는 단계를 넘어, 스스로 능동적으로 조사하고 분석하게 만듭니다."
tags: [AI, 제미나이, 영상분석, 구글]
image: 2026-09-02-Introducing-agentic-video-understanding-with-Gemini.jpg
image_alt: "제미나이가 영상 속 정보를 능동적으로 분석하고 조사하는 모습을 나타내는 디지털 그래픽"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI가 정지된 이미지나 영상을 보고 단순히 답변을 내뱉는 시대는 지났습니다. 이제 AI는 스스로 계획하고 질문하며 정보를 검증하는 능동적인 조사관으로 진화하고 있습니다."
quiz:
  - question: "이번에 공개된 에이전트형 영상 이해 기술은 어떤 모델들에서 사용할 수 있나요?"
    choices: ["제미나이 3.7 Flash, 3.6 Flash, 3.5 Flash-Lite", "모든 제미나이 모델", "제미나이 1.0 전용"]
    answer: 0
    explanation: "구글은 제미나이 3.7 Flash, 3.6 Flash, 3.5 Flash-Lite 모델을 통해 이 기능을 지원한다고 밝혔습니다."
  - question: "에이전트형 영상 이해가 기존 방식과 다른 가장 큰 특징은 무엇인가요?"
    choices: ["단순히 영상을 보는 것이 아닌 능동적이고 반복적인 조사", "영상을 더 빠르게 압축하는 기술", "영상을 자동으로 수정하는 기능"]
    answer: 0
    explanation: "정적인 관찰에서 벗어나 AI가 능동적이고 반복적인 조사 과정을 거쳐 정보를 도출합니다."
  - question: "이 기술을 사용하려면 어디를 통해 접근해야 하나요?"
    choices: ["구글 AI 스튜디오 및 제미나이 엔터프라이즈 에이전트 플랫폼", "이메일로 신청", "유튜브 댓글창"]
    answer: 0
    explanation: "현재 구글 AI 스튜디오와 제미나이 엔터프라이즈 에이전트 플랫폼의 API를 통해 이용 가능합니다."
lang: ko
ref: 2026-09-02-Introducing-agentic-video-understanding-with-Gemini
audio: 2026-09-02-Introducing-agentic-video-understanding-with-Gemini.mp3
permalink: /2026/09/02/Introducing-agentic-video-understanding-with-Gemini/
---

상상해보세요. 당신이 수십 시간 분량의 보안 카메라 영상 속에서 특정 사건이 발생한 순간을 찾으려고 합니다. 지금까지는 AI에게 영상을 보여주고 "이게 뭐야?"라고 물어본 뒤, AI가 내놓는 불완전한 요약에 의존해야 했습니다. 하지만 이제는 AI가 마치 노련한 수사관처럼 직접 영상을 꼼꼼히 살피고, 필요한 부분을 다시 돌려보며 스스로 결론을 내리는 시대가 열렸습니다. 구글이 최근 공개한 '에이전트형 영상 이해(Agentic video understanding)' 기술이 가져온 변화입니다.

## 이게 왜 중요한가요?

그동안 AI에게 영상을 분석하라고 시키는 것은 마치 시험 문제를 푸는 학생에게 문제지를 던져주고 "답이 뭐야?"라고 묻는 것과 비슷했습니다. 기존의 AI는 전체 내용을 한 번 훑어보고 직관에 의존해 답변을 내놓곤 했죠. 하지만 '에이전트형'이라는 이름이 붙은 이번 기술은 다릅니다.

이 기술은 단순한 '관찰자'였던 AI를 능동적인 '조사관'으로 탈바꿈시킵니다. 단순히 영상 속 내용을 요약하는 것을 넘어, AI가 스스로 판단하여 특정 장면을 더 자세히 살피거나, 이전과 이후의 맥락을 비교하며 논리적인 분석을 수행할 수 있게 된 것이죠. 이는 복잡한 데이터를 다루는 기업이나 정밀한 분석이 필요한 전문가들에게 이전과는 비교할 수 없는 정확도와 통찰력을 제공하게 될 것입니다. [출처: Introducing agentic video understanding with Gemini](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/)

## 쉽게 이해하기

'에이전트형 영상 이해'를 쉽게 비유하자면, **'도서관에서 책을 찾는 방식의 차이'**와 같습니다.

기존의 AI가 책 제목만 보고 대충 내용을 추측했다면, 이번 기술은 **유능한 사서를 고용한 것**과 같습니다. 당신이 "이 영상에서 사고가 난 장면을 찾아줘"라고 요청하면, AI라는 사서가 직접 도서관(영상 파일)으로 들어가 이리저리 서가를 뒤지고, 내용을 직접 확인하고, 필요하다면 여러 권의 책을 꺼내 대조해본 뒤 "여기 34번 선반 2층에 있는 자료가 정확한 증거입니다"라고 친절히 알려주는 셈이죠.

비슷한 맥락에서 구글은 앞서 '에이전트형 비전(Agentic Vision, 이미지나 영상의 내용을 스스로 파악하고 조사하는 기술)' 기술을 도입하여 정적인 이미지 이해 과정에도 능동적인 조사 루프를 적용한 바 있습니다. [출처: Introducing Agentic Vision in Gemini 3 Flash](https://blog.google/innovation-and-ai/technology/developers-tools/agentic-vision-gemini-3-flash/) 이 방식은 AI가 정보를 도출하는 과정을 3단계 루프(계획-실행-검증)로 구성하여, 최종적인 답변이 단순히 추측이 아니라 검증된 시각적 증거에 근거하도록 만듭니다. [출처: Google Introduces Agentic Vision: Gemini 3 Flash Now...](https://labnotes.tech/blog/google-introduces-agentic-vision-gemini-3-flash-now-zooms-annotates-and-investigates-images) 이번 영상 분석 기술 역시 이러한 능동적 조사 원리가 영상이라는 다이내믹한 데이터에 적용된 것이라 이해하면 쉽습니다.

## 현재 상황

현재 이 강력한 에이전트형 영상 이해 기능은 구글 AI 스튜디오(Google AI Studio)와 제미나이 엔터프라이즈 에이전트 플랫폼(Gemini Enterprise Agent Platform)의 API를 통해 개발자들이 사용할 수 있습니다. [출처: Introducing agentic video understanding with Gemini](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/)

구글은 이 기능을 제미나이의 최신 모델 라인업인 **제미나이 3.7 Flash, 3.6 Flash, 3.5 Flash-Lite**에 순차적으로 적용하고 있습니다. [출처: Introducing agentic video understanding with Gemini](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/) 즉, 이제 단순히 영상을 전달하는 것만으로도 AI가 내부적인 도구들을 활용해 더 복잡하고 긴 호흡의 분석을 수행할 수 있는 환경이 마련된 것입니다. [출처: Video understanding | Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding)

## 앞으로 어떻게 될까?

앞으로 AI는 영상 속에서 단순히 '무엇이 있다'를 말하는 것을 넘어, "왜 저 사람이 저런 행동을 했는지", "영상 속 복잡한 기계의 작동 원리가 무엇인지"와 같은 질문에 더 깊이 답하게 될 것입니다. 

사용자가 대화하듯이 자연스럽게 영상 편집이나 분석을 지시하면, AI가 그 흐름을 파악하여 단계별로 처리해주는 '대화형 AI 영상 에디터'와 같은 경험이 더욱 보편화될 것으로 보입니다. [출처: GeminiOmni – Create & edit videos as easy as having a conversation](https://gemini.google/us/overview/video-generation/?hl=en) 기술이 발전할수록 우리의 일상 속 영상 콘텐츠 소비 방식 또한 단순히 보는 것을 넘어, AI와 함께 영상을 '조사하고 대화하는' 방향으로 크게 변모할 것입니다.

## 참고자료

1. Introducing Agentic Vision in Gemini 3 Flash (https://blog.google/innovation-and-ai/technology/developers-tools/agentic-vision-gemini-3-flash/)
2. Video understanding | Gemini Enterprise Agent Platform | Google Cloud Documentation (https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding)
3. Introducing agentic video understanding with Gemini (https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/)
4. GeminiOmni – Create & edit videos as easy as having a conversation (https://gemini.google/us/overview/video-generation/?hl=en)
5. Google Introduces Agentic Vision: Gemini 3 Flash Now... | LabNotes (https://labnotes.tech/blog/google-introduces-agentic-vision-gemini-3-flash-now-zooms-annotates-and-investigates-images)