---
layout: post
title: "AI가 더 똑똑하고 빠르게 말할 수 있게 된 비결: '3D DRAM'의 등장"
description: "생성형 AI의 추론 속도를 획기적으로 높여줄 새로운 반도체 기술, d-Matrix의 '랩터(Raptor)' 3D-DRAM 기술을 소개합니다."
summary: "d-Matrix가 공개한 '랩터(Raptor)'는 연산 장치와 메모리를 직접 쌓아 올린 3D-DRAM 구조로, 데이터 이동의 병목 현상을 해결해 AI의 추론 성능을 획기적으로 개선했습니다."
tags: [AI, 반도체, d-Matrix, 3D-DRAM, HotChips2026]
image: 2026-10-13-D-Matrix-Raptor-3D-DRAM-Accelerator-for-Generative-Inference-at-Hot-Chips-2026.jpg
image_alt: "반도체 칩이 층층이 쌓여 있는 미래지향적인 구조를 형상화한 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "메모리와 연산 장치를 물리적으로 가깝게 만드는 것은 AI 가속기의 미래입니다. 랩터는 HBM의 대안으로서 에너지 효율성을 입증하며 AI 추론 인프라의 새로운 가능성을 열었습니다."
quiz:
  - question: "d-Matrix가 공개한 '랩터(Raptor)' 기술의 핵심 구조는 무엇인가요?"
    choices: ["SRAM을 수평으로 나열함", "연산 장치와 DRAM을 수직으로 쌓아 올림", "클라우드 서버를 분산함"]
    answer: 1
    explanation: "랩터는 TSMC 4nm 연산 장치와 맞춤형 DRAM을 36마이크론 피치로 맞대어 수직으로 쌓아 올린 3D-DRAM 구조입니다."
  - question: "랩터 기술이 기존 HBM과 비교해 가지는 장점은 무엇인가요?"
    choices: ["더 많은 전력 소모", "약 1/10 수준의 에너지 효율", "데이터 이동 속도 저하"]
    answer: 1
    explanation: "랩터는 HBM 대비 약 1/10 수준의 전력으로 효율적인 연산을 가능하게 합니다."
  - question: "랩터가 해결하고자 하는 핵심 문제는 무엇인가요?"
    choices: ["데이터 이동 시 발생하는 '메모리 병목 현상'", "인터넷 연결 속도 문제", "AI 학습 데이터 부족"]
    answer: 0
    explanation: "랩터는 생성형 AI 인프라에서 발생하는 데이터 이동의 병목 현상, 이른바 '메모리 벽' 문제를 해결하기 위해 설계되었습니다."
lang: ko
ref: 2026-10-13-D-Matrix-Raptor-3D-DRAM-Accelerator-for-Generative-Inference-at-Hot-Chips-2026
audio: 2026-10-13-D-Matrix-Raptor-3D-DRAM-Accelerator-for-Generative-Inference-at-Hot-Chips-2026.mp3
permalink: /2026/10/13/D-Matrix-Raptor-3D-DRAM-Accelerator-for-Generative-Inference-at-Hot-Chips-2026/
---

상상해보세요. 당신이 도서관에서 아주 중요한 책을 한 권 찾으려 합니다. 그런데 그 책은 건물 지하 깊숙한 창고에 있고, 도서관 열람실은 꼭대기 층에 있습니다. 책을 한 권 빌려 올 때마다 계단을 수십 번씩 오르내려야 한다면 얼마나 힘들까요? 지금 우리가 사용하는 생성형 AI도 이와 비슷한 상황입니다. AI의 '뇌' 역할을 하는 연산 장치가 정보를 기억하는 창고(메모리)에서 데이터를 가져오느라 에너지를 낭비하고 속도가 느려지는 '메모리 병목 현상'에 시달리고 있기 때문이죠.

최근 열린 '핫 칩스(Hot Chips) 2026' 학술 대회에서 반도체 기업 d-Matrix는 이 고민을 해결할 흥미로운 기술을 공개했습니다. 바로 '랩터(Raptor)'라는 이름의 3D-DRAM 가속기입니다. 이제 AI가 데이터를 찾으러 멀리 있는 창고까지 뛰어가지 않아도 됩니다. AI의 뇌 바로 아래에 책장이 붙어있는 것과 같으니까요.

## 이게 왜 중요한가요?

생성형 AI가 복잡한 답변을 내놓을 때, 실제로는 수많은 데이터를 순식간에 메모리에서 꺼내 연산 장치로 보내는 과정이 엄청나게 반복됩니다. 이 과정에서 발생하는 데이터 이동은 AI 성능의 발목을 잡는 거대한 장벽이 됩니다. 이를 전문 용어로 '메모리 벽(Memory Wall)'이라고 부릅니다. [출처 d-Matrix Raptor 3D-DRAM Architecture at Hot Chips 2026](https://www.partgenie.ai/insights/d-matrix-raptor-3d-dram-accelerator-for-generative-inference-at-hot-chips-2026-9)

우리가 사용하는 스마트폰의 인공지능 비서 기능이 더 빨라지거나, 실시간으로 복잡한 영상을 생성하는 AI 서비스가 더 저렴해지기 위해서는 이 벽을 무너뜨려야 합니다. 랩터는 바로 그 기술적인 한계를 돌파하기 위해 탄생했습니다. [출처 d-Matrix's Raptor puts stacked DRAM to work on inference bandwidth](https://runtimewire.com/article/d-matrix-raptor-stacked-dram-inference)

## 쉽게 이해하기

쉽게 비유하자면, 기존의 AI 칩은 '부엌과 식당이 멀리 떨어진 식당'과 같았습니다. 요리사(연산 장치)가 요리를 하려면 재료 창고(메모리)까지 한참을 걸어가서 재료를 가져와야 했습니다. 반면, 랩터는 '요리사가 식재료를 바로 옆에서 꺼내 쓸 수 있는 최신형 오픈 키친'입니다.

랩터는 TSMC의 4나노미터(nm) 초미세 공정으로 만든 연산 장치 다이(반도체 조각)를 맞춤형 DRAM 위에 직접 붙이는 방식을 택했습니다. [출처 Hot Chips 2026: d-Matrix stacks AI accelerator directly on custom DRAM for 100 TB/s per card](https://www.tomshardware.com/tech-industry/semiconductors/d-matrix-stacks-its-ai-accelerator-directly-on-custom-dram-for-100-tbs-per-card) 이를 '3D-DRAM' 구조라고 합니다. 메모리를 연산 장치 바로 밑에 수직으로 쌓아 올렸기 때문에, 데이터가 이동해야 하는 물리적 거리가 극도로 짧아집니다. [출처 d-Matrix stacks DRAM directly · Hacker News | Zeli](https://zeli.app/story/49695065)

덕분에 랩터는 카드당 100TB/s(테라바이트 매초)라는 경이로운 데이터 전송 대역폭을 제공합니다. 이는 일반적인 AI 칩들이 겪는 고질적인 병목 현상을 획기적으로 줄여줍니다. [출처 d-Matrix's Raptor 3D-DRAM Achieves SRAM-Class Bandwidth at 1/10th the HBM Power](https://wccftech.com/d-matrix-raptor-3d-dram-achieves-sram-class-bandwidth-at-1-10th-the-hbm-power/)

## 현재 상황

d-Matrix의 CTO 수딥 보자(Sudeep Bhoja)가 핫 칩스 2026에서 발표한 내용에 따르면, 이 기술은 메타(Meta)와 협력하여 연구가 진행되었습니다. [출처 Hot Chips 2026 - d-Matrix](https://www.d-matrix.ai/event/hot-chips-2026/) 현재의 고성능 AI 칩들은 대개 HBM(고대역폭 메모리)이라는 고가의 메모리를 사용하는데, 랩터는 HBM보다 약 1/10 수준의 전력 효율로도 비슷한 혹은 더 나은 성능을 낼 수 있다는 점이 큰 특징입니다. [출처 d-Matrix's Raptor 3D-DRAM Achieves SRAM-Class Bandwidth at 1/10th the HBM Power](https://wccftech.com/d-matrix-raptor-3d-dram-achieves-sram-class-bandwidth-at-1-10th-the-hbm-power/)

하지만 이 기술이 당장 시장의 모든 HBM을 대체하는 것은 아닙니다. 현재 랩터는 추론(Inference, 학습된 AI가 실제로 답변을 만들어내는 과정) 효율성에 특화되어 있어, 방대한 데이터를 다루는 전체 AI 인프라의 한 축을 담당할 것으로 기대됩니다. [출처 d-Matrix's Raptor Chip Hits 105 TB/s in Real Silicon Tests, But It's Not an HBM Replacement Yet](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2p6bnJUdEVSRkNfcUU2bE9OWjlpZ0FQAQ?hl=en-PK&gl=PK&ceid=PK:en)

## 앞으로 어떻게 될까?

우리는 이제 단순히 '더 많은 전력'을 투입하는 시대에서, '더 효율적인 구조'로 AI를 가속하는 시대로 넘어가고 있습니다. 랩터와 같은 3D-DRAM 기술이 보편화된다면, 당신이 사용하는 AI 서비스의 응답 속도는 더 빨라지면서도 전력 소모량은 줄어들 것입니다. 이는 곧 AI를 실행하는 데 드는 사회적 비용이 낮아진다는 뜻이기도 합니다. [출처 d-Matrix's Raptor 3D-DRAM Achieves SRAM-Class Bandwidth at 1/10th the HBM Power](https://wccftech.com/d-matrix-raptor-3d-dram-achieves-sram-class-bandwidth-at-1-10th-the-hbm-power/)

앞으로 반도체 업계가 얼마나 더 작고 똑똑한 방식으로 메모리와 연산 장치를 결합할지, 랩터가 제시한 이 새로운 지도가 인공지능의 미래를 어디까지 바꿀지 기대해 볼 만합니다.

## 참고자료

1. [d-Matrix Raptor 3D-DRAM Accelerator for Generative Inference](https://www.servethehome.com/d-matrix-raptor-3d-dram-accelerator-for-generative-inference-at-hot-chips-2026/)
2. [d-Matrix Raptor 3D-DRAM Architecture at Hot Chips 2026](https://www.partgenie.ai/insights/d-matrix-raptor-3d-dram-accelerator-for-generative-inference-at-hot-chips-2026-9)
3. [Hot Chips 2026 - d-Matrix](https://www.d-matrix.ai/event/hot-chips-2026/)
4. [Hot Chips 2026: d-Matrix stacks AI accelerator directly on custom DRAM for 100 TB/s per card](https://www.tomshardware.com/tech-industry/semiconductors/d-matrix-stacks-its-ai-accelerator-directly-on-custom-dram-for-100-tbs-per-card)
5. [Hot Chips 2026: d-Matrix Raptor 3D-DRAM - lukebest.github.io](https://lukebest.github.io/papers/hc2026-dmatrix-raptor-3d-dram)
6. [d-Matrix stacks DRAM directly · Hacker News | Zeli](https://zeli.app/story/49695065)
7. [D-Matrix Raptor 3D-DRAM Accelerator for Generative Inference at Hot Chips 2026](https://vk.ru/wall-238001969_5418)
8. [Hot Chips 2026 - Hot Chips 2026](https://hc2026.hotchips.org/?ref=vlsi.kr)
9. [d-Matrix Raptor: 3D-DRAM with 100 TB/s for AI inference](https://www.igorslab.de/en/d-matrix-raptor-3d-dram-over-100-tb-s-stacks-memory-beneath-compute-logic/)
10. [d-Matrix's Raptor 3D DRAM Achieves SRAM-Class Bandwidth at 1/10th the HBM Power](https://wccftech.com/d-matrix-raptor-3d-dram-achieves-sram-class-bandwidth-at-1-10th-the-hbm-power/)
11. [Jobs and Employment at d-Matrix | Simplify Jobs](https://simplify.jobs/c/d-Matrix)
12. [d-Matrix's Raptor 3D DRAM performance - Overview](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2p6bnJUdEVSRkNfcUU2bE9OWjlpZ0FQAQ?hl=en-PK&gl=PK&ceid=PK:en)
13. [d-Matrix's Raptor puts stacked DRAM to work on inference bandwidth](https://runtimewire.com/article/d-matrix-raptor-stacked-dram-inference)