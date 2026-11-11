---
layout: post
title: "내 맥에서 콜 오브 듀티가? '정적 재컴파일'이 가져온 게임의 부활"
description: "에뮬레이터 없이 최신 맥(macOS)에서 콜 오브 듀티 블랙 옵스 2를 네이티브로 실행하는 기술, 정적 재컴파일에 대해 알아봅니다."
summary: "옛날 게임의 코드를 최신 기기의 언어로 직접 번역하는 '정적 재컴파일' 기술을 통해, 콜 오브 듀티 블랙 옵스 2 등 고전 명작 게임들이 최신 맥에서 네이티브 속도로 구동되기 시작했습니다."
tags: [AI, 게임, 기술, 맥, 콜오브듀티]
image: 2026-11-11-Show-HN-Black-Ops-II-statically-recompiled-to-native-ARM64-macOS.jpg
image_alt: "최신 맥북에서 콜 오브 듀티 블랙 옵스 2가 구동되고 있는 모습"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "에뮬레이션의 한계를 넘어 코드를 직접 번역하는 정적 재컴파일 기술은 게임 보존의 새로운 이정표가 될 것입니다. 과거의 유산이 현대 하드웨어의 성능을 십분 활용할 수 있게 된 점이 놀랍습니다."
quiz:
  - question: "정적 재컴파일의 가장 큰 장점은 무엇인가요?"
    choices: ["매우 빠른 에뮬레이터 구동", "에뮬레이터 없이 네이티브 성능 구현", "클라우드 게임 스트리밍"]
    answer: 1
    explanation: "정적 재컴파일은 게임 코드를 최신 기기 언어로 직접 변환하므로 별도의 에뮬레이터가 필요 없습니다."
  - question: "최근 맥(macOS)으로 재컴파일된 게임은 무엇인가요?"
    choices: ["콜 오브 듀티: 블랙 옵스 2", "배틀필드 2042", "사이버펑크 2077"]
    answer: 0
    explanation: "최근 adrbn 개발자에 의해 블랙 옵스 2가 ARM64 맥용으로 정적 재컴파일되었습니다."
  - question: "정적 재컴파일은 어떤 방식으로 작동하나요?"
    choices: ["인터넷 실시간 변환", "기존 게임 코드를 최신 기기 명령어 집합으로 변환", "그래픽만 수정"]
    answer: 1
    explanation: "기존 게임의 기계어 코드를 새로운 하드웨어(예: ARM64)에서 직접 실행 가능한 명령어로 번역하는 방식입니다."
lang: ko
ref: 2026-11-11-Show-HN-Black-Ops-II-statically-recompiled-to-native-ARM64-macOS
audio: 2026-11-11-Show-HN-Black-Ops-II-statically-recompiled-to-native-ARM64-macOS.mp3
permalink: /2026/11/11/Show-HN-Black-Ops-II-statically-recompiled-to-native-ARM64-macOS/
---

상상해보세요. 2020년형 맥북 프로를 열고, 10년도 더 된 고전 게임 '콜 오브 듀티: 블랙 옵스 2' 아이콘을 클릭합니다. 보통이라면 복잡한 에뮬레이터나 가상 머신을 띄우느라 컴퓨터가 뜨거워지거나 버벅거렸을 겁니다. 하지만 이 게임은 마치 어제 출시된 것처럼 부드럽게, 그것도 거의 60프레임으로 화면에 펼쳐집니다. 

최근 개발자 커뮤니티에서 벌어지고 있는 '정적 재컴파일(Static Recompilation)'이라는 기술 덕분에 가능한 일입니다. 게임의 역사가 현대의 최첨단 하드웨어와 만나 새 생명을 얻고 있습니다.

## 이게 왜 중요한가요? (Why It Matters)

우리가 즐기는 고전 게임들은 대개 그 시대의 하드웨어(예: 구형 PC나 콘솔)에 맞춰 만들어졌습니다. 시간이 지나 기기가 노후화되면, 이 게임들은 역사 속으로 사라질 위기에 처하죠. 지금까지는 이를 구동하기 위해 '에뮬레이터'라는 기술을 썼습니다. 에뮬레이터는 마치 외국어를 통역하는 통역사처럼, 구형 게임의 언어를 최신 컴퓨터가 알아들을 수 있게 실시간으로 변환합니다. 하지만 이 과정에서 상당한 성능 손실이 발생하고, 때로는 그래픽이 깨지거나 소리가 밀리는 문제가 생깁니다.

정적 재컴파일은 다릅니다. 이는 통역사를 쓰는 게 아니라, 아예 게임의 언어 자체를 최신 기기의 언어로 완전히 새로 쓰는 작업입니다. 이를 통해 에뮬레이터 없이도 최신 기기에서 '네이티브'하게, 즉 그 기기를 위해 만들어진 게임처럼 완벽한 성능으로 구동됩니다. 이제 우리는 더 이상 과거의 명작들을 낡은 기기에 가둬둘 필요가 없어졌습니다.

## 쉽게 이해하기 (The Explainer)

이렇게 비유해볼까요? 여러분이 쓴 한국어 편지를 영어권 친구에게 보낸다고 해봅시다.

*   **에뮬레이터 방식:** 여러분이 영어권 친구 옆에서 실시간으로 한국어를 영어로 동시통역해주는 것과 같습니다. 여러분(에뮬레이터)의 통역 속도가 친구의 이해 속도를 못 따라가거나, 오역이 생기면 대화가 꼬이죠.
*   **정적 재컴파일 방식:** 편지를 보내기 전에 이미 전문 번역가가 완벽한 영어로 완전히 다시 써서 보내는 것과 같습니다. 친구는 원본이 한국어였다는 사실조차 모를 정도로 아주 자연스럽게 내용을 이해하고 즐길 수 있습니다.

이번에 맥(macOS)에서 구동된 [콜 오브 듀티: 블랙 옵스 2](https://github.com/adrbn/bo2-mac)의 사례를 보면, 개발자는 게임의 32비트 x86(구형 PC 언어) 코드를 'Remill'이라는 도구를 사용해 'LLVM IR(중간 언어)'로 변환한 뒤, 다시 최신 맥의 두뇌인 ARM64(애플 실리콘) 명령어로 옮겼습니다. 또한, 당시 윈도우 그래픽 호출 방식(Direct3D 11)을 최신 맥의 그래픽 표준인 '메탈(Metal)'로 바꾸는 작업을 직접 처리했습니다. 덕분에 [거의 60프레임](https://github.com/adrbn/bo2-mac)이라는 놀라운 성능이 가능해진 것입니다.

## 현재 상황 (Where We Stand)

이미 이 기술은 게임 업계의 거대한 흐름이 되고 있습니다. 블랙 옵스 2뿐만 아니라, [맥스 페인 3](https://www.youtube.com/watch?v=CGYbWKSA5QU)는 PS5에서 60프레임으로 구동되고 있고, [닌자 가이덴 블랙](https://portedgames.com/recompiled-games/), [갓 오브 워](https://recomplauncher.com/game/gow-native-pc), [봄버맨 64](https://recompsoftware.com/games/), [헤일로 CE](https://recompsoftware.com/games/), [램페이지](https://quiverlauncher.com/apps/rampage-recompiled), [파이널 판타지 7](https://andreyvelsk.github.io/GAFT/project/ff7recomp/) 등 수많은 고전 명작이 각자의 최신 기기용 포트로 다시 태어나고 있습니다.

다만, 완벽하진 않습니다. 블랙 옵스 2의 경우에도 [일부 발열 문제](https://github.com/adrbn/bo2-mac)가 여전히 해결 과제로 남아있습니다. 또한, 정적 재컴파일은 게임마다 일일이 코드를 분석하고 변환해야 하므로 대량 생산이 가능한 기술은 아닙니다.

## 앞으로 어떻게 될까? (What's Next)

앞으로 '정적 재컴파일'은 게임 보존의 핵심 표준이 될 것으로 보입니다. 개발자들은 블랙 옵스 2 프로젝트에서 [화면 분할(Split-screen)이나 LAN 모드](https://github.com/adrbn/bo2-mac) 같은 기능을 추가하는 등, 원작을 넘어선 확장까지 꾀하고 있습니다. 

개인이 소유한 게임 파일을 최신 기기에서 아무런 제약 없이 구동할 수 있게 해주는 이 기술은, 거대 게임사들의 복잡한 리마스터 비용과 에뮬레이션의 기술적 한계를 한 번에 돌파할 강력한 도구입니다. 언젠가는 우리가 오늘 산 최신 게임도 20년 뒤, 다시 정적 재컴파일을 통해 완벽하게 구동되는 날이 올 것입니다.

## 참고자료

1. [Show HN: Black Ops II statically recompiled to native ARM64 macOS](https://github.com/adrbn/bo2-mac)
2. [Max Payne 3 Running NATIVELY on PS5 at 60 FPS... - YouTube](https://www.youtube.com/watch?v=CGYbWKSA5QU)
3. [Recompiled Games List: Every Native PC Port... | PortedGames](https://portedgames.com/recompiled-games/)
4. [God of War Native PC — PC recomp of God of War · RecompLauncher](https://recomplauncher.com/game/gow-native-pc)
5. [Decompiled & recompiled games · Recomp](https://recompsoftware.com/games/)
6. [Rampage Recompiled – Rampage: World Tour Recomp | Quiver](https://quiverlauncher.com/apps/rampage-recompiled)
7. [Call of Duty: Black Ops II - recomp.party](https://recomp.party/p/adrbn/bo2-mac/)
8. [bo2-mac: Call of Duty: Black Ops II PC recomp, source ...](https://recompsoftware.com/p/bo2-mac/)
9. [Black Ops II Recompiled — PC recomp of Call of Duty: Black ...](https://recomplauncher.com/game/bo2-mac?lang=en-GB)
10. [bo2-recompiled: Call of Duty: Black Ops II recompilation ...](https://recomp.gg/p/bo2-recompiled)
11. [FF7 Recomp | Games & Apps for AYN Thor](https://andreyvelsk.github.io/GAFT/project/ff7recomp/)