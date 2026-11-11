---
layout: post
title: "在我的 Mac 上玩《決勝時刻》？「靜態重編譯」帶來的遊戲新生"
description: "探索靜態重編譯技術，無需模擬器，即可在最新款 Mac (macOS) 上原生運行《決勝時刻：黑色行動 2》。"
summary: "透過將舊遊戲代碼直接翻譯為現代設備語言的「靜態重編譯」技術，《決勝時刻：黑色行動 2》等經典傑作已開始在最新款 Mac 上實現原生速度運行。"
tags: [AI, 遊戲, 技術, Mac, 決勝時刻]
image: 2026-11-11-Show-HN-Black-Ops-II-statically-recompiled-to-native-ARM64-macOS.jpg
image_alt: "在最新款 MacBook 上運行《決勝時刻：黑色行動 2》的畫面"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "靜態重編譯技術超越了模擬器的限制，直接對代碼進行翻譯，將成為遊戲保存的一個新里程碑。看到過去的遺產能夠充分利用現代硬體的效能，實在令人驚嘆。"
quiz:
  - question: "靜態重編譯最大的優點是什麼？"
    choices: ["極速的模擬器運行", "無需模擬器即可實現原生效能", "雲端遊戲串流"]
    answer: 1
    explanation: "靜態重編譯直接將遊戲代碼轉換為現代設備的語言，因此無需額外的模擬器。"
  - question: "最近哪款遊戲被重編譯到了 Mac (macOS) 上？"
    choices: ["決勝時刻：黑色行動 2", "戰地風雲 2042", "電馭叛客 2077"]
    answer: 0
    explanation: "最近由開發者 adrbn 將《黑色行動 2》靜態重編譯為 ARM64 Mac 版本。"
  - question: "靜態重編譯是以什麼方式運作的？"
    choices: ["網際網路即時轉換", "將既有的遊戲代碼轉換為現代設備的指令集", "僅修改圖形介面"]
    answer: 1
    explanation: "這是一種將舊有遊戲的機器語言代碼翻譯成新硬體（如 ARM64）可直接執行指令的方式。"
lang: zh-tw
ref: 2026-11-11-Show-HN-Black-Ops-II-statically-recompiled-to-native-ARM64-macOS
---

試想一下：你打開 2020 年款的 MacBook Pro，點擊了十多年前的經典遊戲《決勝時刻：黑色行動 2》的圖示。按照以往的經驗，這通常會因為啟動複雜的模擬器或虛擬機而導致電腦過熱或卡頓。但現在，這款遊戲竟然像昨天剛發布一樣流暢，甚至以近乎 60 幀的畫面呈現在你面前。

這一切都要歸功於開發者社群中近期興起的「靜態重編譯（Static Recompilation）」技術。遊戲的歷史正在與現代尖端硬體結合，重獲新生。

## 為什麼這很重要？ (Why It Matters)

我們所喜愛的經典遊戲，通常是為那個時代的硬體（例如舊型 PC 或遊戲主機）量身打造的。隨著時間流逝，硬體逐漸老化，這些遊戲面臨著消失在歷史長河中的風險。至今為止，我們一直採用「模擬器」技術來運行它們。模擬器就像一名口譯員，將舊遊戲的語言即時翻譯給現代電腦聽。但這個過程會產生大量的效能損失，有時還會出現圖形崩壞或聲音延遲等問題。

靜態重編譯則完全不同。它不使用口譯員，而是直接將遊戲的代碼語言「重寫」為現代設備的語言。這使得遊戲無需模擬器，就能在現代設備上「原生（Native）」運行——就像它是專為該設備製作的一樣，擁有完美的效能。從現在起，我們再也不必將經典名作封鎖在老舊的設備中了。

## 淺顯易懂的解釋 (The Explainer)

我們可以這樣比喻：假設你要將一封韓文信寄給英語系國家的朋友。

*   **模擬器方式：** 就像是你站在英語系朋友身旁，進行即時韓語口譯。如果你的翻譯速度跟不上朋友的理解速度，或者出現誤譯，對話就會變得混亂。
*   **靜態重編譯方式：** 這就像是在寄出信件前，先由專業翻譯員將信件完美地重寫為英文。朋友在閱讀時會感到非常自然，甚至不會意識到這封信的原始語言其實是韓文。

以這次在 Mac (macOS) 上運行的 [《決勝時刻：黑色行動 2》](https://github.com/adrbn/bo2-mac) 為例，開發者使用了名為「Remill」的工具，將遊戲的 32 位元 x86（舊型 PC 語言）代碼轉換為「LLVM IR（中間語言）」，然後再轉移到最新款 Mac 的大腦——ARM64（Apple Silicon）指令集上。此外，開發者還親自處理了當時 Windows 的圖形調用方式（Direct3D 11）到現代 Mac 圖形標準「Metal」的轉換工作。正因如此，才能實現[近 60 幀](https://github.com/adrbn/bo2-mac)的驚人效能。

## 現狀 (Where We Stand)

這項技術已經成為遊戲產業的一股巨大潮流。除了《黑色行動 2》之外，[《江湖本色 3》](https://www.youtube.com/watch?v=CGYbWKSA5QU)已能在 PS5 上以 60 幀運行，而《忍者外傳 黑》、《戰神》、《炸彈超人 64》、《最後一戰：戰鬥進化》、《狂暴》（Rampage）、《Final Fantasy VII》等無數經典名作，也正以各自的最新設備移植版重新誕生。

不過，這並非完美。以《黑色行動 2》為例，[部分發熱問題](https://github.com/adrbn/bo2-mac)仍然是需要解決的難題。此外，靜態重編譯需要針對每款遊戲單獨進行代碼分析和轉換，因此目前尚無法實現大規模量產。

## 未來展望 (What's Next)

展望未來，「靜態重編譯」有望成為遊戲保存的核心標準。開發者們在《黑色行動 2》專案中，甚至還計畫增加[分割畫面（Split-screen）或區域網路（LAN）模式](https://github.com/adrbn/bo2-mac)等功能，展現出超越原作的擴展潛力。

這項技術讓個人能夠無限制地在最新設備上運行自己擁有的遊戲檔案，它是一項強大的工具，能一次突破大型遊戲公司的昂貴重製成本與模擬器的技術瓶頸。總有一天，我們今天購買的最新遊戲，在 20 年後也將能透過靜態重編譯，完美地在未來的設備上運行。

## 參考資料

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