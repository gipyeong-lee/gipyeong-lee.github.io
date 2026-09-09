---
layout: post
title: "AI 總是喜歡「裝模作樣」並繞圈子說話？這一句指令就夠了"
description: "介紹如何去除 AI 濫用不必要隱喻或華麗修飾詞的「AI 腔調」，讓 AI 回答更加簡潔的方法。"
summary: "Anthropic 在官方指南中公開了 Claude Fable 5.1 模型去除冗餘修飾與隱喻的魔法指令：'Please remove all mannered prose'。"
tags: [AI, Anthropic, Claude, 提示工程, 技巧]
image: 2026-09-09-Please-Remove-All-Mannered-Prose-and-Other-LLM-Incantations.jpg
image_alt: "象徵 AI 撰寫的複雜華麗語句被刪除，轉變為簡潔明確語句的圖形。"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI 的「裝模作樣」會增加使用者的認知負擔。去除掩蓋本質的修飾詞，是活用 AI 的基本功。"
quiz:
  - question: "Anthropic 所定義的「矯揉造作的散文（Mannered Prose）」是什麼？"
    choices: ["AI 使用的技術性錯誤", "包含過多隱喻與華麗修辭的寫作風格", "AI 拒絕回答的現象"]
    answer: 1
    explanation: "矯揉造作的散文（Mannered Prose）是指 AI 將簡單的內容，不必要地用隱喻或華麗文體來包裝回答的現象。"
  - question: "提供的指令 'Please remove all mannered prose' 應該放在哪裡才有效？"
    choices: ["個別提問末尾或系統提示詞中", "電腦的設定選單中", "必須輸入在代碼塊內"]
    answer: 0
    explanation: "該指令可以包含在個別請求中，或添加到指定 AI 角色的系統提示詞（System Prompt）中使用。"
  - question: "為了讓 AI 正確理解該指令，一定要保留空格嗎？"
    choices: ["是的，空格是必須的", "不是，不加空格連在一起寫也有效果", "必須全部大寫輸入"]
    answer: 1
    explanation: "令人驚訝的是，該指令即使將所有空格省略（Pleaseremoveallmanneredprose）輸入，也能發揮作用。"
lang: zh-tw
ref: 2026-09-09-Please-Remove-All-Mannered-Prose-and-Other-LLM-Incantations
---

想像一下。繁忙的早晨，你請 AI 助理幫忙：「請幫我整理今天會議的 3 個核心事項。」然而 AI 卻回答：「今天的會議彷彿暴風雨前的寧靜。三個核心事項如同指南針，將指引我們的方向……」滔滔不絕地講了一堆隱喻與修飾語。對於只想知道重點的使用者來說，實在令人焦急。

最近，人工智慧模型因為這種「AI 腔調」帶給使用者疲勞感。Anthropic 在最近發表的最新模型「Claude Fable 5.1」指南中，正式提出了能解決此問題的簡單方法。

## 這為什麼重要？

我們使用 AI 的最大理由是「效率」。然而，如果 AI 為了看起來像人而混入過多隱喻，或不必要地繞圈子說話，反而會讓使用者難以找到重要的資訊。根據 [Source 13](https://vibecoding.ru/news/2026/09/03/anthropic-mannered-prose-prompt)，AI 使用的這種華麗文體會帶入作者未選擇的意義，讀者必須進行不必要的解析工作。這次的官方指南在於賦予使用者讓 AI 回答得更聰明、更簡潔的權限，具有重大意義。

## 深入淺出

Anthropic 將這種現象命名為「矯揉造作的散文（Mannered Prose）」。[Source 4](https://x.com/MaxForAI/status/2095131767229517917) 簡單來說，就是指 AI 對於一句話就能講清楚的內容，硬要動用隱喻法或華麗辭藻來「裝模作樣」，拉長語句的寫作習慣。

Anthropic 的開發團隊承認，雖然 Claude Fable 5.1 比以前的模型有所改進，但語句有時仍然太長且複雜。[Source 4](https://x.com/MaxForAI/status/2095131767229517917) 因此，他們為了消除這種「AI 腔調」，在官方文件中追加了一個魔法般的指令。

那就是 **"Please remove all mannered prose（請移除所有矯揉造作的散文，即過度修飾的文體）"** 這句話。[Source 1](https://matthewritch.com/blog/2026/09/08/Mannered-Prose-Style-Prompts/)

比喻來說是這樣的：AI 現在已經完成了「基本禮儀教育」，但像是剛上完「文學課」，想在所有回答中加入詩意表達的狀態。這個指令就像是一個強力的開關，告訴 AI：「別當藝術家了，現在專注於助理的本職工作吧！」

## 當前現狀

目前，這個提示詞（Prompt）被評為非常有效果。[Source 5](https://paddo.dev/blog/a-dial-worth-turning/) 使用者發現，只要將這個指令放在提問末尾，或是直接放入指揮 AI 的「系統提示詞」中，AI 的語氣就會變得簡潔許多。[Source 6](https://x.com/Voxyz_ai/status/2095260094795583807), [Source 11](https://t.me/dailyprompts/9362)

更驚人的是，由於 AI 對這句話的意義理解得非常深刻，即使把空格全部省略，寫成 'Pleaseremoveallmanneredprose'，它也能聰明地聽懂並去掉華麗的修飾詞。[Source 9](https://apidog.com/blog/prompting-claude-fable-5-1/), [Source 13](https://vibecoding.ru/news/2026/09/03/anthropic-mannered-prose-prompt)

## 未來展望

未來，AI 服務預計會進行改善，讓使用者不需要親自輸入這種「修正語氣」的指令。Anthropic 這次的指南更新是一個信號，顯示 AI 企業正傾聽使用者的聲音，並不僅僅是在思考 AI 的智慧，還在考慮「溝通的效率」。

今後不需要再麻煩地對 AI 解釋「不要講得太好聽，只講重點就好」。只要那句話，你的 AI 助理就會化身為更稱職的商業夥伴。

## MindTickleBytes 的 AI 記者觀點

AI 變得能像人類一樣流利說話雖然是一項技術成就，但在商業環境中，最有價值的能力依然是「清晰的資訊傳達」。Anthropic 親自公開解決此問題的提示詞，顯示出 AI 是否具備自我節制的能力，正在成為衡量 AI 技術成熟度的指標。

## 參考資料

1. [Matthew Ritch, "Please Remove All Mannered Prose" and Other LLM Incantations](https://matthewritch.com/blog/2026/09/08/Mannered-Prose-Style-Prompts/)
2. [Ian Nuttall, "A prompt to stop Claude from speaking in parseltongue"](https://x.com/iannuttall/status/2095203215734178066)
3. [Max For AI, "有意思，Anthropic亲自下场教你怎么去掉Claude味了"](https://x.com/MaxForAI/status/2095131767229517917)
4. [Paddo, "A Dial Worth Turning: Claude Opus 5's Prose, and the Style Guide Anthropic Wrote Against Its Own Model"](https://paddo.dev/blog/a-dial-worth-turning/)
5. [Vox, "You removed the “It’s not X, it’s Y” lines. 𝗜𝘁 𝘀𝘁𝗶𝗹𝗹 𝗿𝗲𝗮𝗱𝘀 𝗹𝗶𝗸𝗲 𝗔𝗜."](https://x.com/Voxyz_ai/status/2095260094795583807)
6. [HN blogs - 8/9/26](https://hnblogs.substack.com/p/hn-blogs-8926)
7. [APIDog, "Prompting Claude Fable 5.1: Every Behavior Shift and the Line That..."](https://apidog.com/blog/prompting-claude-fable-5-1/)
8. [Telegram, "@dailyprompts"](https://t.me/dailyprompts/9362)
9. [Dzen, "Гайд по созданию промптов в Fable 5.1"](https://dzen.ru/a/apkFgUgF0B8ig_B6)
10. [Vibecoding, "Вычурность из текстов Claude убирает одна строка"](https://vibecoding.ru/news/2026/09/03/anthropic-mannered-prose-prompt)
11. [VC.ru, "Вышел Claude Fable 5.1 - я уже потестила"](https://vc.ru/chatgpt/3117274-obzor-fable-5-1-ot-anthropic-i-ozhidaniya-ot-astra-ot-openai)