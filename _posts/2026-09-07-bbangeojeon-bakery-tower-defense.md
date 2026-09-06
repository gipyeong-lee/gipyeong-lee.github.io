---
layout: post
title: "빵어전 — 빵을 굽고 조합하며 화덕을 지키는 타워디펜스"
description: "64종의 빵 타워를 재료 조합으로 만드는 모바일 게임, 빵어전을 소개합니다. 플레이 방식과 다운로드 링크, 심사 중인 1.5.0 업데이트 미리보기를 함께 정리했습니다."
date: 2026-09-07 08:10:00 +0900
section: blog
category: projects
lang: ko
ref: 2026-09-07-bbangeojeon-bakery-tower-defense
permalink: /blog/projects/bbangeojeon/
tags:
  - 빵어전
  - 인디게임
  - 타워디펜스
  - PixiJS
  - 프로젝트
---

**빵을 구워 적을 막는다면 어떨까요?** 제가 개발하는 **빵어전**은 재료를 조합해 빵 타워를 만들고, 밀려오는 적으로부터 화덕을 지키는 모바일 타워디펜스 게임입니다.

귀여운 빵을 모으는 재미에, 어떤 빵을 어디에 배치할지 고민하는 방어 전략을 더했습니다. 작은 도트 빵집에서 시작해 나만의 빵 수비대를 만들어가는 게임을 소개합니다.

[공식 사이트에서 살펴보기](https://bbangeojeon.vercel.app/) · [iPhone 다운로드](https://apps.apple.com/kr/app/id6805946937) · [Android 다운로드](https://play.google.com/store/apps/details?id=com.eternaxcode.bbangeojeon)

> 아래 이미지는 **심사 중인 1.5.0 업데이트 미리보기**입니다. 2026년 9월 7일 기준 Android는 검토 중, iOS는 심사 대기 중이며, 현재 스토어에서 설치되는 버전의 화면·콘텐츠와 다를 수 있습니다.

<figure>
  <img src="/images/bbangeojeon/v1-5-0-home-preview.png" alt="빵어전 1.5.0 미리보기: 도트 빵집 앞에 모인 캐릭터와 화덕, 모험 시작 버튼이 있는 홈 화면" width="1080" height="1920" style="display: block; width: 100%; max-width: 360px; height: auto; margin: 0 auto;">
  <figcaption>1.5.0 미리보기 — 빵집에서 모험을 준비하는 홈 화면.</figcaption>
</figure>

## 재료를 더하면 빵이 되고, 빵이 모이면 수비대가 됩니다

전투의 중심은 **굽기와 조합**입니다. 반죽을 놓고 재료를 더해 빵 타워를 만들며, 같은 빵을 합치거나 조합을 바꾸어 수비대를 갖춥니다. 빵어전에는 총 **64종의 빵 타워**가 있습니다.

화덕으로 다가오는 적을 막으려면 빵의 배치와 조합을 함께 생각해야 합니다. 새로운 빵을 알아가는 도감 수집과, 다음 전투에서 다른 구성을 시도하는 전략이 이어지도록 구성했습니다.

처음 시작한다면 공식 사이트의 [게임 가이드](https://bbangeojeon.vercel.app/game-guide.html)를 참고해 주세요. 반죽과 재료를 다루는 흐름부터 살펴볼 수 있습니다.

<figure>
  <img src="/images/bbangeojeon/v1-5-0-battle-preview.png" alt="빵어전 1.5.0 미리보기: 세로 전장에 배치된 빵 타워가 적을 막고 아래쪽 화덕을 지키는 전투 화면" width="1080" height="1920" loading="lazy" style="display: block; width: 100%; max-width: 360px; height: auto; margin: 0 auto;">
  <figcaption>1.5.0 미리보기 — 빵 타워를 배치하고 재료를 더해 화덕을 지킵니다.</figcaption>
</figure>

## 1.5.0에서 준비한 다음 모험

현재 양쪽 스토어에 제출한 1.5.0에서는 모험의 범위를 넓히고, 빵집과 전투의 도트 표현을 다듬었습니다. **다음 내용은 승인 후 공개될 업데이트 기준**입니다.

- **4개 대륙·40개 챕터·400개 스테이지**: 대륙별 적과 지도, 원정 목표를 따라 모험합니다.
- **개별 장비 옵션**: 장비마다 붙는 옵션과 희귀도에 따른 옵션 확장을 추가했습니다.
- **수동 승리 기록을 활용하는 AUTO**: 새 수동 승리에서 기록한 행동을 호환되는 구성의 자동 전투에 활용합니다. 구성이 맞지 않거나 진행이 막히면 일반 AUTO로 전환합니다.
- **움직이는 빵집**: 홈 캐릭터의 제빵·간식·불씨 활동과 터치 반응, 장착한 화덕의 모습이 빵집에 반영됩니다.

<figure>
  <img src="/images/bbangeojeon/v1-5-0-world-preview.png" alt="빵어전 1.5.0 미리보기: 밀보라 대륙의 첫 챕터와 스테이지 목록을 보여주는 모험 지도" width="1080" height="1920" loading="lazy" style="display: block; width: 100%; max-width: 360px; height: auto; margin: 0 auto;">
  <figcaption>1.5.0 미리보기 — 대륙과 챕터를 따라 이어지는 모험 지도.</figcaption>
</figure>

## 웹 기술로 만드는 모바일 도트 게임

빵어전의 게임 화면은 **TypeScript와 PixiJS**로 만들고, **Capacitor**를 통해 Android와 iOS 앱으로 제공합니다. 작은 도트가 흐려지지 않도록 원본 픽셀과 정수 배율을 기준으로 화면·캐릭터·효과를 정돈하고 있습니다.

빵이라는 익숙한 소재가 실제 플레이에서도 드러나도록, 재료를 더하는 과정과 빵이 전투에서 하는 역할을 함께 다듬는 프로젝트입니다. 빵집의 분위기와 타워디펜스의 선택하는 재미를 함께 즐겨주시면 좋겠습니다.

## 빵집의 첫 방어전을 시작해 보세요

- [빵어전 공식 사이트](https://bbangeojeon.vercel.app/): 게임 소개, 가이드, 빵 도감과 커뮤니티
- [App Store에서 다운로드](https://apps.apple.com/kr/app/id6805946937)
- [Google Play에서 다운로드](https://play.google.com/store/apps/details?id=com.eternaxcode.bbangeojeon)

플레이하면서 마음에 든 빵, 조합에서 헷갈렸던 점, 더 보고 싶은 빵집의 모습이 있다면 [공식 커뮤니티](https://bbangeojeon.vercel.app/community.html)에 남겨주세요. 다음 개선을 생각할 때 참고하겠습니다.
