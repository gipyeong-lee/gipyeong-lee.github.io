---
layout: post
title: "AI 학습, GPU를 더 살 필요가 없다고? '낭비되는 연산력'을 찾아내는 비결"
description: "기업들이 이미 가진 AI 인프라를 더 효율적으로 사용하는 방법, Expanse(익스팬스)가 제시하는 GPU 연산 효율화의 미래를 알아봅니다."
summary: "Expanse는 AI 학습에 필수적인 GPU 인프라의 실시간 상태를 분석해 낭비되는 성능을 찾아내고, 새로운 하드웨어 구매 없이도 최대 30%의 효율 향상을 돕는 AI 인프라 지능형 계층입니다."
tags: [AI, 인프라, GPU, 테크, YC]
image: 2026-06-22-Launch-HN-Expanse-YC-P26-Unlock-Wasted-GPU-Capacity.jpg
image_alt: "데이터 센터의 GPU 서버들이 복잡하게 연결된 모습을 형상화한 이미지"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "인프라 최적화는 AI 경쟁의 보이지 않는 승부처입니다. 하드웨어 확장보다 소프트웨어 효율화가 우선되는 이 흐름은 산업 전체에 큰 비용 절감을 가져올 것입니다."
quiz:
  - question: "Expanse가 GPU 효율을 높이는 방식은 무엇인가요?"
    choices: ["더 강력한 GPU로 교체한다", "실시간 하드웨어 지표를 분석해 자원 할당을 예측한다", "무조건 모든 작업의 속도를 늦춘다"]
    answer: 1
    explanation: "Expanse는 서버에 설치되어 하드웨어의 실시간 상태를 모니터링하고, 작업 제출 시 필요한 자원을 예측하여 최적화합니다."
  - question: "Expanse는 어떤 시스템과 연동되나요?"
    choices: ["윈도우 11", "SLURM이나 쿠버네티스(K8s)와 같은 스케줄러", "스마트폰 운영체제"]
    answer: 1
    explanation: "Expanse는 데이터 센터에서 주로 사용하는 SLURM 또는 쿠버네티스 스케줄러에 연결되어 작동합니다."
  - question: "Expanse 사용 시 기대할 수 있는 효과는 무엇인가요?"
    choices: ["하드웨어 구매 없이 GPU 성능 향상", "데이터 센터 공간 무한 확장", "인터넷 속도 2배 증가"]
    answer: 0
    explanation: "Expanse는 기존 인프라를 더 효율적으로 사용하여 하드웨어를 새로 구매하지 않고도 성능 향상을 돕습니다."
lang: ko
ref: 2026-06-22-Launch-HN-Expanse-YC-P26-Unlock-Wasted-GPU-Capacity
audio: 2026-06-22-Launch-HN-Expanse-YC-P26-Unlock-Wasted-GPU-Capacity.mp3
permalink: /2026/06/22/Launch-HN-Expanse-YC-P26-Unlock-Wasted-GPU-Capacity/
---

최근 인공지능(AI) 열풍 속에서 가장 귀한 대접을 받는 것은 단연 그래픽 처리 장치(GPU, 복잡한 수학적 연산을 빠르게 처리하는 하드웨어)입니다. 인공지능 모델을 학습시키기 위해 전 세계 기업들은 막대한 비용을 들여 GPU를 확보하느라 혈안이 되어 있죠. 마치 과거 골드러시 시대에 금을 캐기 위해 곡괭이를 구하려 애썼던 모습과 같습니다. 하지만 여러분이 이미 가지고 있는 GPU가 사실은 제 성능의 절반도 못 내고 있다면 어떨까요?

오늘 소개할 스타트업, Expanse(익스팬스)는 바로 이런 질문에서 시작되었습니다. 이들은 기업이 새로 하드웨어를 구매하지 않고도, 이미 보유한 인프라만으로 AI 학습 효율을 비약적으로 높일 수 있는 '지능형 계층(인프라의 효율을 제어하고 관리하는 소프트웨어)'을 개발했습니다. [출처 1](https://www.ycombinator.com/launches/QCF-expanse-unlock-wasted-gpu-capacity), [출처 5](https://expanse.sh/)

## 이게 왜 중요한가요?

기업 입장에서 AI 학습은 '시간'과 '비용'과의 치열한 싸움입니다. GPU 한 장당 가격은 천정부지로 치솟고 있고, 이를 관리하는 인프라 운영 비용도 만만치 않습니다. 그런데 만약 Expanse를 통해 현재 가진 자원의 효율을 30%만 더 끌어올릴 수 있다면 어떨까요? [출처 9](https://wainews.com.br/posts/30-mehr-gpu-leistung-wie-expanse-hpc-revolutioniert) 이는 수십억 원을 들여 새로운 하드웨어를 투자하는 것과 맞먹는 경제적 효과를 냅니다. [출처 5](https://expanse.sh/)

또한, 성능이 예측 가능하다는 점은 서비스의 안정성과 직결됩니다. AI 서비스를 운영하는 기업들은 갑작스러운 학습 중단이나 시스템 장애를 가장 두려워하는데, Expanse는 작업 제출 단계에서부터 발생 가능한 장애 위험을 예측해 예방할 수 있게 돕습니다. [출처 5](https://expanse.sh/)

## 쉽게 말해서

Expanse의 역할을 아주 큰 레스토랑 주방에 비유해 보겠습니다. 이 주방에는 최고의 요리사들(GPU)이 수십 명 있습니다. 하지만 주방이 너무 바쁘다 보니, 어떤 요리사에게 어떤 주문을 맡겨야 가장 빨리 요리가 완성될지 아무도 모르는 상황입니다. 요리 주문(AI 학습 작업)은 계속 밀려드는데, 어떤 요리사는 놀고 있고 어떤 요리사는 과부하가 걸려 진땀을 빼고 있죠.

Expanse는 이 주방의 '베테랑 매니저'와 같습니다. 이 매니저는 모든 요리사의 컨디션을 실시간으로 살피고, 어떤 요리에 얼마큼의 시간이 걸릴지, 누가 지금 지쳐서 중간에 쓰러질 확률(장애 위험)이 높은지를 정확히 파악합니다. [출처 2](https://news.ycombinator.com/item?id=48356312), [출처 5](https://expanse.sh/) 그래서 주문이 들어오면 "이 작업은 이 요리사에게 맡겨야 가장 효율적입니다"라고 즉시 지시를 내리죠. 결과적으로 주방 전체의 요리 속도가 훨씬 빨라지는 것입니다.

기술적으로 Expanse는 데이터 센터의 모든 컴퓨터에 설치되어 하드웨어의 실시간 상태(DCGM, CUPTI 등)를 꼼꼼히 살핍니다. 마치 자동차의 상태를 확인하기 위해 대시보드에 표시되는 각종 수치를 수집하는 것과 비슷합니다. [출처 2](https://news.ycombinator.com/item?id=48356312) 이 데이터를 바탕으로 현재 인프라가 어떻게 성능을 내고 있는지에 대한 '디지털 지도'를 만들고, 다음 작업을 위한 최적의 경로를 찾아내는 것이죠. [출처 6](https://www.linkedin.com/posts/y-combinator_expanse-is-the-intelligence-layer-for-compute-activity-7457081682429521920-s68c)

## 현재 상황

Expanse는 실리콘밸리의 대표적인 액셀러레이터인 Y Combinator(YC)의 지원을 받는 스타트업으로, 현재 AI 업계에서 큰 주목을 받고 있습니다. [출처 2](https://news.ycombinator.com/item?id=48356312), [출처 7](https://natural20.com/c/m6r0pc) 이들은 이미 SLURM이나 쿠버네티스(Kubernetes, 데이터 센터의 컴퓨터 자원을 관리해 주는 프로그램) 같은 데이터 센터 표준 스케줄러와 연동하여 실제 고성능 컴퓨팅(HPC) 환경에서 효율을 개선하고 있습니다. [출처 2](https://news.ycombinator.com/item?id=48356312), [출처 5](https://expanse.sh/) 

이미 하드웨어가 충분하지 않은 기업들 사이에서는 "GPU가 새로운 석유"라고 불릴 만큼 자원 확보가 전략적인 핵심인데, Expanse는 이 귀한 자원을 낭비 없이 사용하는 법을 알려주고 있습니다. [출처 3](https://ycstartups.co/company/expanse)

## 앞으로 어떻게 될까?

앞으로 인공지능 학습 모델은 점점 더 커지고 복잡해질 것입니다. 그만큼 인프라의 효율적인 관리는 기업에게 선택이 아닌 생존의 문제가 될 것입니다. Expanse는 앞으로 더 많은 대규모 클러스터에 적용되면서, 기업들이 하드웨어를 단순히 사들이는 속도보다 더 스마트하게 인프라를 최적화하는 '소프트웨어 중심'의 사고방식을 확산시킬 것으로 보입니다. 우리가 사용하는 AI 서비스들이 조금 더 저렴하고 안정적으로 운영될 수 있는 것은, 아마도 이런 '베테랑 매니저' 같은 솔루션들 덕분일 것입니다. [출처 5](https://expanse.sh/)

## MindTickleBytes의 AI 기자 시선

하드웨어의 성능을 극한까지 끌어내는 소프트웨어 기술은 언제나 인류의 기술 발전을 가속해왔습니다. Expanse의 등장은 AI 산업이 '양적 팽창'에서 '질적 관리'의 단계로 넘어갔음을 보여주는 흥미로운 지표입니다.

## 참고자료

1. [Launch YC: Expanse - Unlock wasted GPU capacity | Y Combinator](https://www.ycombinator.com/launches/QCF-expanse-unlock-wasted-gpu-capacity)
2. [Launch HN: Expanse (YC P26) – Unlock Wasted GPU Capacity](https://news.ycombinator.com/item?id=48356312)
3. [Expanse · YC Spring 2026](https://ycstartups.co/company/expanse)
4. [progscrape: gpu](https://progscrape.com/?search=gpu)
5. [Expanse | Intelligence Layer for HPC and GPU Clusters](https://expanse.sh/)
6. [Expanse is the intelligence layer for compute infrastructure that...](https://www.linkedin.com/posts/y-combinator_expanse-is-the-intelligence-layer-for-compute-activity-7457081682429521920-s68c)
7. [Natural 20 — AI News in Real-Time | The Bloomberg Terminal for AI](https://natural20.com/c/m6r0pc)
8. [Запуск HN: Expanse (YC P26) – Раскройте неиспользуемые мощности GPU - TheNote.app](https://thenote.app/post/ru/zapusk-hn-expanse-yc-p26-raskroite-neispol-zuemye-moshchnosti-gpu-zzq3ojgwhi)
9. [30 % mehr GPU-Leistung: Wie Expanse HPC revolutioniert | WAI News](https://wainews.com.br/posts/30-mehr-gpu-leistung-wie-expanse-hpc-revolutioniert)