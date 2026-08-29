---
layout: post
title: "영상 제작, 이제 '감독'처럼 대화하며 완성한다? 구글 제미나이 옴니 1.1 플래시 공개"
description: "구글의 새로운 AI 모델 제미나이 옴니 1.1 플래시가 영상 제작을 어떻게 변화시킬지, 어떤 새로운 기능들이 추가되었는지 쉽게 알아봅니다."
summary: "영상 길이를 최대 40초까지 확장하고, 4K 고화질 업스케일링을 지원하는 등 한층 정교해진 구글의 영상 생성 AI 제미나이 옴니 1.1 플래시를 소개합니다."
tags: [AI, 영상제작, 제미나이, 구글]
image: 2026-08-29-Gemini-Omni-11-Flash.jpg
image_alt: "구글의 AI 영상 모델 제미나이 옴니 1.1 플래시가 생성한 다양한 영상 편집 작업 화면을 보여주는 이미지."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "단순히 영상을 만들어내는 단계를 넘어, 창작자가 의도한 장면을 구체적으로 통제할 수 있게 되었다는 점이 핵심입니다. 이제 AI는 도구를 넘어 진정한 창작 파트너가 되어가고 있습니다."
quiz:
  - question: "제미나이 옴니 1.1 플래시에서 영상을 얼마나 더 길게 연장할 수 있나요?"
    choices: ["10초", "20초", "40초"]
    answer: 2
    explanation: "이 모델은 기존 영상에서 10초 단위로 최대 40초까지 장면을 연장할 수 있습니다."
  - question: "영상 제작 비용을 절감하기 위해 도입된 새로운 모드는 무엇인가요?"
    choices: ["360p 초안 모드", "흑백 모드", "무음 모드"]
    answer: 0
    explanation: "360p 해상도의 초안 모드를 통해 저렴한 비용으로 빠르게 제작하고 테스트할 수 있습니다."
  - question: "제미나이 옴니 1.1 플래시가 영상 연장 시 일관성을 높이기 위해 분석하는 기존 영상 분량은 얼마인가요?"
    choices: ["마지막 1초", "마지막 5초", "최대 10초"]
    answer: 2
    explanation: "기존 영상의 마지막 10초까지 분석하여 장면 연결의 일관성을 더욱 높였습니다."
lang: ko
ref: 2026-08-29-Gemini-Omni-11-Flash
audio: 2026-08-29-Gemini-Omni-11-Flash.mp3
permalink: /2026/08/29/Gemini-Omni-11-Flash/
---

상상해보세요. 주말에 직접 만든 여행 브이로그 영상이 조금 짧아 아쉬운데, 카메라를 다시 꺼내 촬영하러 나갈 시간은 없습니다. 이때 AI에게 "방금 그 해변 장면을 40초 정도로 자연스럽게 이어줘"라고 말하면, AI가 이전 장면의 흐름을 완벽하게 파악해 영상을 이어 붙여줍니다. 꿈같은 이야기처럼 들리지만, 이제 구글의 새로운 AI 모델을 통해 현실이 되고 있습니다.

구글은 최근 영상 생성 및 편집의 정밀도를 획기적으로 높인 새로운 멀티모달(Multimodal, 텍스트·이미지·영상 등 다양한 형태의 데이터를 동시에 이해하는) AI 모델인 **제미나이 옴니 1.1 플래시(Gemini Omni 1.1 Flash)**를 공개했습니다 [[출처 3](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/omni-1-1-flash), [출처 16](https://windowsreport.com/gemini-omni-1-1-flash-adds-4k-upscaling-and-longer-videos/)].

## 이게 왜 중요한가요?

지금까지 대부분의 영상 생성 AI는 '한 번에 그럴싸한 결과물을 쏟아내는' 것에 집중했습니다. 하지만 실제로 영상을 만드는 창작자들에게는 이 방식이 불편했습니다. "여기서 장면을 조금만 더 길게 해줘", "이 시작점과 끝점을 맞춰줘" 같은 세밀한 요구를 반영하기 어려웠기 때문이죠.

이번 업데이트는 영상 제작을 '운에 맡기는 창작'에서 '감독이 의도하는 제작'으로 바꾸는 데 큰 의미가 있습니다 [[출처 17](https://enterprisedna.co/resources/ai-pulse/ai-pulse-2026-08-27-google-ships-gemini-omni-1-1-flash/)]. 특히 영상 제작 환경에서 효율성과 비용은 매우 중요한 요소인데, 이번 모델은 개발자와 창작자들이 더 낮은 비용으로 빠르게 초안을 만들고, 고화질로 완성할 수 있는 환경을 제공합니다 [[출처 14](https://explainx.ai/blog/gemini-omni-1-1-flash-video-generation-update-august-2026), [출처 17](https://enterprisedna.co/resources/ai-pulse/ai-pulse-2026-08-27-google-ships-gemini-omni-1-1-flash/)].

## 쉽게 이해하기

제미나이 옴니 1.1 플래시를 이해하기 위해 두 가지 비유를 들어볼게요.

첫째, **'장면 이어달리기'**입니다. 기존 모델들은 아주 짧은 순간만 보고 다음을 추측했다면, 1.1 플래시는 이전 영상의 마지막 10초 분량을 꼼꼼하게 분석합니다 [[출처 6](https://the-decoder.com/googles-gemini-omni-1-1-flash-makes-ai-video-generation-cheaper-and-more-flexible/), [출처 19](https://explainx.ai/blog/gemini-omni-1-1-flash-video-generation-update-august-2026)]. 마치 달리기 선수가 이전 주자가 건네주는 바통의 속도와 방향을 정확히 파악하는 것과 같죠. 덕분에 영상이 끊김 없이 최대 40초까지 자연스럽게 연장됩니다 [[출처 16](https://windowsreport.com/gemini-omni-1-1-flash-adds-4k-upscaling-and-longer-videos/), [출처 19](https://explainx.ai/blog/gemini-omni-1-1-flash-video-generation-update-august-2026)].

둘째, **'저화질 스케치와 고화질 완성본'**의 관계입니다. 우리가 그림을 그릴 때 처음부터 정밀한 붓터치를 하지는 않죠? 이 모델은 360p 해상도의 '스케치 버전'을 초당 0.03달러라는 저렴한 비용으로 빠르게 먼저 만들어 보여줍니다 [[출처 14](https://explainx.ai/blog/gemini-omni-1-1-flash-video-generation-update-august-2026), [출처 17](https://enterprisedna.co/resources/ai-pulse/ai-pulse-2026-08-27-google-ships-gemini-omni-1-1-flash/)]. 이 과정에서 마음에 들면 그때 4K라는 고화질로 업스케일링(Upscaling, 낮은 해상도를 높은 해상도로 변환)을 진행하면 됩니다 [[출처 13](https://postium.ru/google-otkryla-dostup-k-gemini-omni-1-1-flash/), [출처 14](https://explainx.ai/blog/gemini-omni-1-1-flash-video-generation-update-august-2026)]. 시간을 아끼고 비용은 줄이면서 완성도는 높이는 전략입니다.

## 현재 상황

현재 제미나이 옴니 1.1 플래시는 개발자들을 위한 프리뷰(미리보기) 단계로 제공되고 있습니다 [[출처 3](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/omni-1-1-flash)]. 사용자들은 텍스트, 이미지, 오디오, 비디오를 복합적으로 입력해 영상을 생성하고 편집할 수 있습니다 [[출처 16](https://windowsreport.com/gemini-omni-1-1-flash-adds-4k-upscaling-and-longer-videos/)]. 

핵심적인 기능은 다음과 같습니다.
- **장면 연장:** 최대 40초까지 10초 단위로 장면을 늘릴 수 있습니다 [[출처 14](https://explainx.ai/blog/gemini-omni-1-1-flash-video-generation-update-august-2026), [출처 17](https://enterprisedna.co/resources/ai-pulse/ai-pulse-2026-08-27-google-ships-gemini-omni-1-1-flash/)].
- **프레임 제어:** 영상의 시작과 끝 프레임을 직접 지정해 화면 전환을 매끄럽게 조절합니다 [[출처 1](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/), [출처 17](https://enterprisedna.co/resources/ai-pulse/ai-pulse-2026-08-27-google-ships-gemini-omni-1-1-flash/)].
- **경제적 제작:** 360p 초안 모드를 통해 훨씬 저렴하고 빠르게 반복 작업이 가능합니다 [[출처 14](https://explainx.ai/blog/gemini-omni-1-1-flash-video-generation-update-august-2026), [출처 17](https://enterprisedna.co/resources/ai-pulse/ai-pulse-2026-08-27-google-ships-gemini-omni-1-1-flash/)].

## 앞으로 어떻게 될까?

앞으로는 영상 편집의 전문적인 기술이 없어도 누구나 자연스러운 영상을 만들 수 있는 시대가 될 것입니다. 구글은 이미 제미나이 플랫폼을 통해 사용자가 대화하듯 영상을 수정하고 스타일을 바꾸는 경험을 제공하고 있습니다 [[출처 15](https://gemini-omni.dev/gemini-omni-1-1-flash), [출처 17](https://enterprisedna.co/resources/ai-pulse/ai-pulse-2026-08-27-google-ships-gemini-omni-1-1-flash/)]. 영상 제작 도구들이 더욱 정교해짐에 따라, 앞으로는 단순한 짧은 클립을 넘어 복잡한 서사를 가진 영상들도 AI와 협업하여 제작되는 사례가 늘어날 것으로 보입니다.

---

## AI의 시선
MindTickleBytes의 AI 기자 시선: 이번 업데이트는 AI가 단순한 '발생기'를 넘어 '편집자'이자 '감독'으로 진화하고 있음을 보여줍니다. 창작자가 제어권을 쥐게 될 때 AI 기술은 비로소 실무 현장에서의 가치를 증명할 것입니다.

---

## 참고자료

1. [Gemini Omni 1.1 Flash lets you build with more control](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/)
2. [Gemini Omni – Create & edit videos as easy as having a conversation](https://gemini.google/overview/video-generation/)
3. [Gemini Omni 1.1 Flash Preview | Gemini Enterprise Agent Platform | Google Cloud Documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/omni-1-1-flash)
4. [Google AI Studio on X](https://x.com/GoogleAIStudio/status/2093008678118998298)
5. [r/singularity on Reddit: Gemini Omni 1.1 Flash now available](https://www.reddit.com/r/singularity/comments/1vzzcgo/gemini_omni_11_flash_now_available/)
6. [Google's Gemini Omni 1.1 Flash makes AI video generation cheaper and more flexible](https://the-decoder.com/googles-gemini-omni-1-1-flash-makes-ai-video-generation-cheaper-and-more-flexible/)
7. [Gemini Omni 1.1 Flash: 40s Extensions, $0.03/s Drafts (Aug 2026)](https://explainx.ai/blog/gemini-omni-1-1-flash-video-generation-update-august-2026)
8. [Gemini Omni Flash - Model Card — Google DeepMind](https://deepmind.google/models/model-cards/gemini-omni-flash/)
9. [Gemini Omni 1.1 Flash Adds 4K Upscaling and Longer Videos](https://windowsreport.com/gemini-omni-1-1-flash-adds-4k-upscaling-and-longer-videos/)
10. [Google ships Gemini Omni 1.1 Flash — Enterprise DNA](https://enterprisedna.co/resources/ai-pulse/ai-pulse-2026-08-27-google-ships-gemini-omni-1-1-flash/)
11. [Gemini Omni 1.1 Flash: New Control Features for AI Builders](https://aitoolly.com/ai-news/article/2026-08-28-google-deepmind-announces-gemini-omni-11-flash-empowering-developers-with-enhanced-control)
12. [Gemini Omni 1.1 Flash: Next-Gen AI Video Generator](https://gemini-omni.dev/gemini-omni-1-1-flash)
13. [Google выпустила Gemini Omni 1.1 Flash для генерации... | Postium](https://postium.ru/google-otkryla-dostup-k-gemini-omni-1-1-flash/)