---
layout: post
title: "AI 記得我的臉？Google Gemini 驚人的圖像編輯升級"
description: "介紹 Google Gemini 應用程式中新引入的 Google DeepMind 圖像編輯模型功能。快來看看如何在保持照片中人物與寵物樣貌不變的情況下，僅更改背景或道具的神奇編輯秘訣。"
summary: "Google Gemini 透過 DeepMind 的新模型，推出了能保持人物與寵物長相並進行精細照片修改的「多輪」（Multi-turn）圖像編輯功能。"
tags: [Google, Gemini, AI圖像, 圖像編輯, DeepMind, 人工智慧]
image: 2026-04-15-Image-editing-in-Gemini-just-got-a-major-upgrade.jpg
image_alt: "使用者在智慧型手機上利用 Gemini 應用程式，更改生成圖像中的家具顏色並修改背景的創意操作畫面"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "這項更新在超越單純圖像生成的基礎上確保了「連續性」，大大提升了 AI 圖像工具的實用性。現在 AI 既是畫家，也成為了精細的修圖專家。"
quiz:
  - question: "這次 Gemini 圖像編輯更新的核心特徵是什麼？"
    choices: ["降低圖像解析度", "保持人物或寵物的原有樣貌並進行修改", "自動裁剪照片構圖"]
    answer: 1
    explanation: "這次更新的重點在於保持人物與寵物的一致樣貌，同時對特定部分進行精細修改。"
  - question: "哪個術語最適合用來描述 Gemini 的新圖像編輯功能？"
    choices: ["一次性生成", "多輪（Multi-turn）編輯", "套用濾鏡"]
    answer: 1
    explanation: "使用者透過逐步提供回饋並漸進式地修改圖像的方式，被稱為「多輪」編輯。"
  - question: "目前 Gemini 的 AI 圖像編輯工具尚不支援的功能是什麼？"
    choices: ["更換背景", "裁剪圖像（Crop）", "增加家具"]
    answer: 1
    explanation: "目前的 Gemini 新 AI 編輯器雖然可以進行精細修改，但尚不支援裁剪（Crop）功能。"
lang: zh-tw
ref: 2026-04-15-Image-editing-in-Gemini-just-got-a-major-upgrade
---

想像一下，您用 AI 製作了一張非常滿意的全家福。構圖完美，表情開朗，但只有一點讓人遺憾：希望家裡小狗的毛色不是棕色而是白色，且背景中沉悶的樹木能換成鮮豔的花田。

但到目前為止，如果您對 AI 說「換成花田」，AI 往往不會聽從您的要求，而是直接畫出一張全新的照片。原本拍得很好的爸爸慈祥的微笑，或是家裡小狗可愛的表情全都變了，您一定有過這種令人難過的經驗。

現在您可以不用擔心了。Google 的人工智慧助理 Gemini 終於蛻變成了「機靈」的圖像編輯專家。多虧了 Google DeepMind 開發的新模型，現在 Gemini 可以在守護照片主角臉孔的同時，神奇地更換背景或道具 [Gemini 圖像編輯迎來重大升級 - Android Police](https://www.androidpolice.com/image-editing-in-gemini-just-got-a-major-upgrade/)。

## 這為什麼很重要？

過往的 AI 圖像工具在每次下達新指令時，往往傾向於從頭開始重新繪圖。打個比方，就像您拜託畫家「在這裡多畫一朵花」，畫家卻不回答，而是直接拿出一塊新畫布重新開始畫。這與其說是修改，不如說是「再創造」。

這次更新最大的意義在於確保了**「連續性」**與**「一致性」**。特別是現在已經可以維持照片中人物或寵物原本的樣貌（Likeness，原本的長相或特徵）[Nano Banana：Google Gemini 圖像編輯迎來重大升級](https://blog.google/products-and-platforms/products/gemini/updated-image-editing-model/)。

簡單來說，現在您可以更換生成圖像中人物的衣服風格，或大幅改變周邊環境，同時仍能確認該人物依舊保有「我」或「我家人」的特徵 [Gemini 圖像編輯迎來重大活動 - LinkedIn](https://www.linkedin.com/posts/google_image-editing-in-gemini-just-got-a-major-activity-7369128020512575489-un4-)。這在將 AI 用於商業設計或儲存個人回憶時提供了極大的便利。

## 輕鬆理解：與 AI 進行「對話式編輯」

這次更新的核心技術是**多輪編輯（Multi-turn editing）**。聽起來有點深奧對吧？比喻來說，這意味著「像對話一樣分多次進行小幅修改的方式」[Nano Banana! Gemini 圖像編輯迎來重大升級](https://blog.google/intl/en-mena/product-updates/explore-get-answers/nano-banana-image-editing-in-gemini-just-got-a-major-upgrade/)。

想像您正在一家三明治店點餐：

1. **第 1 階段**：「請給我一個基本的三明治。」（生成完整圖像）
2. **第 2 階段**：「請把這裡的起司去掉，改放培根。」（修改特定要素）
3. **第 3 階段**：「醬汁請幫我淋辣一點。」（變更細節風格）
4. **第 4 階段**：「最後，請在包裝紙上寫下我的名字。」（增加細節）

在這個過程中，店員不會把您點好的三明治扔進垃圾桶重做，而是在已經做好的基礎上，只針對您要求的部分進行更換或添加。Gemini 也是如此。它會記住已經繪製好的圖像結構與顏色，並精細地修改與增加您要求的特定部分 [Nano Banana! Gemini 圖像編輯迎來重大升級](https://blog.google/intl/en-mena/product-updates/explore-get-answers/nano-banana-image-editing-in-gemini-just-got-a-major-upgrade/)。

憑藉這種精細的調整能力，Gemini 現在已能與 OpenAI 的工具並駕齊驅，為使用者提供更強大的創作自由 [Google Gemini 的 AI 圖像模型獲得了「香蕉級」升級](https://techcrunch.com/2025/08/26/google-geminis-ai-image-model-gets-a-bananas-upgrade/)。

## 現況：如「香蕉」般驚人的性能，但仍有功課要做

根據 Google DeepMind 的說法，這次採用的新模型是全球評價最高的 AI 圖像編輯模型之一 [您的 Gemini 應用程式剛獲得了重大 AI 圖像編輯升級...](https://www.zdnet.com/article/your-gemini-app-just-got-a-major-ai-image-editing-upgrade-for-free/)。在初步公開時，海外使用者對這驚人的性能紛紛表示「簡直瘋了（Going bananas）」。在西方文化中，「Bananas」是用來表示非常驚訝或狂熱的俚語 [Gemini 圖像編輯迎來重大升級](https://www.elevenforum.com/t/image-editing-in-gemini-just-got-a-major-upgrade.39202/)。

然而，並非一切都盡善盡美。有趣的是，這麼聰明的 AI 編輯器目前**尚不支援將照片裁剪成所需大小的「裁剪（Crop）」功能** [Google 新聞 - 關於 Gemini • Nano Banana • 圖像編輯...](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lXczZtWER4RmxqMFE4c3JhdjBTZ0FQAQ?hl=en-US&gl=US&ceid=US:en)。雖然能輕易完成更換複雜背景、幫人物換裝等高難度任務，卻缺少最基礎的相片裁剪功能，這確實有點諷刺。

此外，由於它能如此完美地維持人物樣貌，一些人擔心這可能會導致 Deepfake（利用人工智慧進行精細圖像合成的技術）等誤用情況 [Google 新聞 - 關於 Gemini • Nano Banana • 圖像編輯...](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lXczZtWER4RmxqMFE4c3JhdjBTZ0FQAQ?hl=en-US&gl=US&ceid=US:en)。隨著技術的日益強大，我們如何負責任地使用它，也是一個值得思考的課題。

## 未來展望

這次更新將 Gemini 應用程式內建的圖像編輯功能提升到了一個新的層次 [透過 Gemini 應用程式中更新的原生圖像編輯，以驚人的新方式變換圖像。](https://news-tech.io/en/news/image-editing-in-gemini-just-got-a-major-upgrade)。現在使用者無需學習專業的 Photoshop 技術，僅需透過與 Gemini 對話，即可完成夢想中的圖像。

未來，Google 預計將進一步精細化這些編輯功能，使使用者能更細膩地控制圖像的所有要素 [Google Gemini 的 AI 圖像模型獲得了「香蕉級」升級](https://techcrunch.com/2025/08/26/google-geminis-ai-image-model-gets-a-bananas-upgrade/)。不久的將來，從相片裁剪等基礎功能，到如同電影場景般調整燈光或更換天氣的高階變形，都將能透過一個 Gemini 應用程式來解決。

您智慧型手機中的 Gemini 現在已超越了單純的「畫畫朋友」，正逐漸成為能精準理解您的意圖並修飾照片的「專屬設計師」。今天就打開 Gemini 應用程式，嘗試將您的想像力一一填入照片中如何？

## MindTickleBytes 的 AI 記者視角
透過這次更新，AI 圖像生成已從單純等待「中樂透」的偶然領域，進入了使用者能隨心所欲精雕細琢的「工藝」領域。特別是維持人物與寵物樣貌的技術，將成為社交媒體內容創作者或夢想從事角色產業的創作者們的強大武器。雖然缺少基礎的「裁剪」功能看起來像個可愛的小缺點，但這足以讓人確認 DeepMind 的實力。現在我們不再只是「接收」AI 繪圖的人，而是成為了與 AI 共同「創作」圖畫的主體。

## 參考資料
1. [Nano Banana：Google Gemini 圖像編輯迎來重大升級](https://blog.google/products-and-platforms/products/gemini/updated-image-editing-model/)
2. [Nano Banana! Gemini 圖像編輯迎來重大升級](https://blog.google/intl/en-mena/product-updates/explore-get-answers/nano-banana-image-editing-in-gemini-just-got-a-major-upgrade/)
3. [Google 新聞 - 關於 Gemini • Nano Banana • 圖像編輯...](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lXczZtWER4RmxqMFE4c3JhdjBTZ0FQAQ?hl=en-US&gl=US&ceid=US:en)
4. [Gemini 圖像編輯迎來重大升級 | Google](https://www.linkedin.com/posts/google_image-editing-in-gemini-just-got-a-major-activity-7369128020512575489-un4-)
5. [Gemini 中的 AI 照片編輯剛獲得重大升級 – 以下是它如何...](https://tech.yahoo.com/ai/articles/ai-photo-editing-gemini-just-100258282.html)
6. [Gemini 圖像編輯迎來重大升級... | TechNews](https://news-tech.io/en/news/image-editing-in-gemini-just-got-a-major-upgrade)
7. [Gemini 圖像編輯迎來重大升級 - Android Police](https://www.androidpolice.com/image-editing-in-gemini-just-got-a-major-upgrade/)
8. [Google Gemini 的 AI 圖像模型獲得了「香蕉級」升級](https://techcrunch.com/2025/08/26/google-geminis-ai-image-model-gets-a-bananas-upgrade/)
9. [圖像編輯現已在 Gemini 應用程式中推出](https://workspaceupdates.googleblog.com/2025/08/image-editing-now-available-in-gemini-app.html)
10. [您的 Gemini 應用程式剛獲得了重大 AI 圖像編輯升級...](https://www.zdnet.com/article/your-gemini-app-just-got-a-major-ai-image-editing-upgrade-for-free/)
11. [Gemini 圖像編輯迎來重大升級](https://www.elevenforum.com/t/image-editing-in-gemini-just-got-a-major-upgrade.39202/)
12. [Google 新聞 - 關於 Gemini • Nano Banana • 圖像編輯...](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lXczZtWER4RW5QbUlVRXd3dDNpZ0FQAQ?hl=en-US&gl=US&ceid=US:en)
13. [Gemini 圖像編輯迎來重大升級 | NViNiO • 新聞](https://www.linkedin.com/posts/nvinio_image-editing-in-gemini-just-got-a-major-activity-7368636435739873282-gxQy)
14. [Gemini 圖像編輯迎來重大升級 – Sciencx](https://www.scien.cx/2025/08/26/image-editing-in-gemini-just-got-a-major-upgrade/)

## FACT-CHECK SUMMARY
- Claims checked: 15
- Claims verified: 15
- Verdict: PASS