---
layout: post
title: "開發者們永恆的作業：一位開發者獨自花費 4 年時間撰寫全新 Vim 手冊的故事"
description: "厭倦了既複雜且門檻高昂的現有 Vim 手冊，一位開發者投入 4 年共 1,244 小時，親自撰寫了一本能從初學者到進階功能進行系統性學習的書籍。"
summary: "一位開發者在 4 年內投入 2,987 個番茄鐘（1,244 小時），完成了包含 21 個章節與 170 道練習題的全新 Vim 手冊《Learning to Play Vim》。"
tags: [Vim, Programming, DeveloperTools, Books]
image: 2026-11-27-Show-HN-I-wrote-an-entire-Vim-manual-over-4-years.jpg
image_alt: "插圖描繪了一位開發者坐在鍵盤前編寫程式碼手冊的身影"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "完美的工具不會從天而降。為了消除使用者親身經歷的不便而傾注 4 年歲月的執著，是證明開源生態系統為何如此強大的最佳證據。"
quiz:
  - question: "作者編寫全新 Vim 手冊《Learning to Play Vim》花了多長時間？"
    choices: ["1年", "2年", "4年以上"]
    answer: 2
    explanation: "作者表示，完成這本書花費了 4 年以上的時間，並投入了 2,987 個番茄鐘（1,244 小時）。"
  - question: "《Learning to Play Vim》一書中包含多少道練習題？"
    choices: ["70個", "170個", "2,987個"]
    answer: 1
    explanation: "本書提供了 21 個章節以及 170 道練習題與解答，協助讀者進行實作練習。"
  - question: "新手冊中提供的設定檔（config）是用哪些語言編寫的？"
    choices: ["Python 與 JavaScript", "Vimscript 與 Lua", "C++ 與 Rust"]
    answer: 1
    explanation: "為了 Neovim 使用者，大部分的設定都同時以 Vimscript 與 Lua 兩種語言編寫。"
lang: zh-tw
ref: 2026-11-27-Show-HN-I-wrote-an-entire-Vim-manual-over-4-years
---

想像一下，你每天使用的文件編輯器或程式功能強大無比，但學習使用方法卻像在讀一本解密密碼的書一樣痛苦。只要是踏入傳奇文字編輯器「Vim（文字編輯程式）」世界的開發者，都一定曾經歷過這種情境，在這裡，你可以只用鍵盤、不用滑鼠，就像施展魔法般編輯程式碼。

長期以來，Vim在開發者之間被稱為「學起來困難，但一旦掌握就能帶來魔術般生產力的工具」。然而，針對入門者的官方指南或現有文件卻極不友善。在此背景下，有一位開發者為了徹底解決這個問題，傾注了長達 4 年的時間，其故事在 Hacker News 社群引發了熱烈討論 [Show HN: I wrote an entire Vim manual over 4 years](http://themouseless.dev/vim/)。

## 為什麼這很重要？

在開發工具的世界裡，文件不只是簡單的說明書。好的文件能降低進入新技術或工具的門檻，讓更多人體驗到該工具的真正價值。然而，現有的 Vim 學習資料對初學者來說卻是一道巨大無比的高牆。 

作者回憶道，例如初學 Vim 時接觸的基本教學「vimtutor」過於密集且容易遺漏核心重點，而官方手冊（`:help manual`）某些部分又過於瑣碎，導致初學者很容易迷失方向 [Show HN: I wrote an entire Vim manual over 4 years](http://themouseless.dev/vim/)。 

在這樣的背景下登場的新手冊，不只是 Vim 使用者的好消息。這也是一個感人的案例，展示了一個人的熱情與執著如何將我們日常中面臨的複雜且不友善的技術障礙，轉化為使用者友善的藝術品。對於無數想提升開發生產力，卻因陡峭的學習曲線而卻步的開發者來說，這本新手冊無疑是久旱逢甘霖。 

這也是一個完美的證明，說明一本好書或手冊能以多麼戲劇性的方式提升整個技術生態系統的成長速度。

## 輕鬆理解：就像學習彈鋼琴一樣

為了理解學習 Vim 的過程，我們可以這樣比喻：一般的文字編輯器或文書處理軟體就像是任何人都能輕鬆彈奏的「自動玩具鋼琴」，隨便按壓就會發出聲音且直覺易懂。相對地，Vim 就像是一台經過精密調音的「平台鋼琴（Grand Piano）」，必須徹底掌握手指的位置、踩踏板的時機以及讀譜的方法，才能彈奏出美妙的樂曲。

然而，以往的指南書就像是突然把貝多芬的高難度奏鳴曲樂譜塞給第一次按鋼琴鍵的人，或者從鋼琴內部的複雜擊弦機結構開始詳細解說一樣。 

這次作者所撰寫的書名《Learning to Play Vim》本身就完美體現了這個比喻 [Show HN: I wrote an entire Vim manual over 4 years](http://themouseless.dev/vim/)。這正是想打造一本像彈鋼琴一樣，從基礎的琴鍵練習開始一步步扎實推進，最終能演奏複雜曲目的逐步（step-by-step）指南。 

簡單來說，如果以往的 Vim 文件對開發者而言是不友善的百科全書，那麼新手冊就是一位在旁邊手把手糾正指法親切的家教老師。這種方法能幫助初學者在面對複雜的快捷鍵與模式（Mode）切換時不致灰心喪志，並自然而然地建立肌肉記憶。

## 現狀：我們所面臨的 Vim 學習極限

Vim 經由悠久歷史中無數開發者的雙手發展至今。正如 Vim 這個名字本身代表著「Vi IMproved（原有 Vi 編輯器的改進版）」一樣 [Vimhelp pages, always up-to-date](https://vimhelp.org/)，內建於程式中的龐大線上文件系統，是隨時可以透過 `:help` 指令存取的強大武器 [Vimdocumentation :vimonline](https://www.vim.org/docs.php)。

特別是 Vim 的官方說明系統一直以來都以系統化方式管理，分為提供以任務為導向說明的「使用者手冊（User manual）」以及精確描述各功能運作方式的「參考手冊（Reference manual）」 [Vimhelp pages, always up-to-date](https://vimhelp.org/usr_01.txt.html)。 

儘管如此，連使用 Vim 超過 10 年的我也不禁坦言，當初剛入門時，`vimtutor` 內容過於密集而難以記憶，在官方手冊的特定章節（例如探討尋找說明的 `02.8 Finding help` 等部分）也常常迷失方向 [Show HN: I wrote an entire Vim manual over 4 years](http://themouseless.dev/vim/)。 

由此可知，雖然官方文件扮演了虛擬空間中巨大百科全書的角色，但在「初學者該如何打好基礎並應用於實務中」的教育觀點上，至今仍有不足之處。這也是為什麼無數開發者在破碎的部落格文章或 YouTube 影片間流浪，卻總是錯失學習脈絡的原因。

## 新手冊的誕生與驚人紀錄

為了克服現有文件的不足，作者決定親自寫書。而這個決定帶來了超越想像的努力。 

作者編寫全新 Vim 手冊《Learning to Play Vim》所花費的時間長達 4 年以上 [Show HN: I wrote an entire Vim manual over 4 years](http://themouseless.dev/vim/)。若將其換算成數字，這是投入了 2,987 個專注的番茄鐘（Pomodoro）工作階段、總計高達 1,244 小時的激烈工作產物 [Show HN: I wrote an entire Vim manual over 4 years](http://themouseless.dev/vim/)。這個數字不僅僅代表寫作時間，更是與每天面臨的複雜性搏鬥、一字一句精心完成的忍耐紀錄。

這本書包含的具體內容如下：
- 一步步展示 Vim 最重要功能的 **21 個章節（Chapters）** [Show HN: I wrote an entire Vim manual over 4 years](http://themouseless.dev/vim/)
- 包含明確解答的 **170 道練習題** [Show HN: I wrote an entire Vim manual over 4 years](http://themouseless.dev/vim/)
- 展示如何在實際開發環境中活用 Vim 並依個人喜好進行設定的無數**真實生活範例** [Show HN: I wrote an entire Vim manual over 4 years](http://themouseless.dev/vim/)
- 為了能更深入探討各功能而連結的**相關 Vim 說明頁面參照** [Show HN: I wrote an entire Vim manual over 4 years](http://themouseless.dev/vim/)

特別是為了照顧近年來許多開發者使用的 Neovim 使用者，書中出現的大部分設定程式碼都同時以 **Vimscript 與 Lua** 兩種語言編寫 [Show HN: I wrote an entire Vim manual over 4 years](http://themouseless.dev/vim/)。此外，透過專注於 Vim 與 Neovim 共同的核心功能，設計上使其不偏重於特定環境，能夠被普遍活用 [Show HN: I wrote an entire Vim manual over 4 years](http://themouseless.dev/vim/)。

## 未來會如何發展？

這本書的發布為 Vim 生態系統注入了新鮮的活力。作者透過到達頁面（Landing Page，`https://themouseless.dev/vim/`）宣傳這本書，並同步提供了可以預覽完整目錄以及介紹基礎的前三個章節的樣本（`https://themouseless.dev/content/learning_to_play_vim_sample...`） [Show HN: I wrote an entire Vim manual over 4 years](http://themouseless.dev/vim/)。

未來學習開發的初學者或想成為 Vim 高手的進階開發者，將不再需要面對不友善的文件而灰心喪志，而是能透過這個設計系統化的逐步指南，突破編輯器操作的極限。這是在長達 4 年的時間裡，靠著雙手一字一句累積起來的知識遺產，值得我們關注它將如何改變全球無數開發者的寫程式日常。這絕對足以成為技術社群共同成長的良性循環模範案例。

## AI 的視角

完美的工具不會從天而降。為了消除使用者親身經歷的不便而傾注 4 年歲月的執著，是證明開源生態系統為何如此強大的最佳證據。

## 參考資料

1. [Show HN: I wrote an entire Vim manual over 4 years](http://themouseless.dev/vim/)
2. [Vimdocumentation :vimonline](https://www.vim.org/docs.php)
3. [Vimhelp pages, always up-to-date](https://vimhelp.org/)
4. [Vimhelp pages, always up-to-date](https://vimhelp.org/usr_01.txt.html)