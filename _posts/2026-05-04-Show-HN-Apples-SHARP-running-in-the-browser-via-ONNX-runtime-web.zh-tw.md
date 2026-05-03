---
layout: post
title: "一張照片就能變成 3D 空間？蘋果 AI 'SHARP' 進入瀏覽器的原因"
description: "本文將以簡單有趣的方式，為您解釋如何在無需額外安裝的情況下，於網頁瀏覽器中運行蘋果最新的 3D 重建技術 SHARP 及其原理。"
summary: "隨著蘋果 AI 模型 'SHARP' 可以在網頁瀏覽器中直接運行，一個任何人都能僅憑一張照片輕鬆創建並擁有專屬 3D 空間的時代已經到來。"
tags: [Apple, SHARP, 3D, AI, 網頁技術, 高斯潑濺]
image: 2026-05-04-Show-HN-Apples-SHARP-running-in-the-browser-via-ONNX-runtime-web.jpg
image_alt: "將 2D 平面照片轉換為立體 3D 空間過程的視覺化圖形圖像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "無需複雜伺服器即可在個人裝置上直接創建 3D 的技術，將成為同時兼顧用戶隱私與成本效率的重要里程碑。"
quiz:
  - question: "蘋果 SHARP 模型用於創建 3D 空間的核心技術名稱是什麼？"
    choices: ["多邊形渲染", "高斯潑濺 (Gaussian Splatting)", "光線追蹤"]
    answer: 1
    explanation: "SHARP 基於『高斯潑濺』技術，透過噴灑大量小點（橢球體）來營造立體感。"
  - question: "在網頁瀏覽器中無需額外伺服器即可運行 AI 的核心工具是？"
    choices: ["ONNX Runtime Web", "Photoshop", "YouTube"]
    answer: 0
    explanation: "使用 ONNX Runtime Web，可以借用網頁瀏覽器的運算能力直接運行複雜的 AI 模型。"
  - question: "在瀏覽器中運行的 SHARP 模型大約有多大？"
    choices: ["2.4 MB", "2.4 GB", "24 GB"]
    answer: 1
    explanation: "目前轉換為網頁版使用的 SHARP 模型大小約為 2.4 GB。"
lang: zh-tw
ref: 2026-05-04-Show-HN-Apples-SHARP-running-in-the-browser-via-ONNX-runtime-web
---

想像一下，您將昨天在咖啡廳拍的一張漂亮的蛋糕照片上傳到網站，蛋糕突然像要從螢幕中跳出來一樣變得立體。您可以隨意用滑鼠或手指轉動蛋糕的側面、背面，甚至是頂部來觀看。就像回到了那家咖啡廳一樣。

這不再是遙遠未來的科幻電影情節。隨著蘋果 (Apple) 最近公開的研究用 AI 模型 **「SHARP」** 開始直接在您每天使用的網頁瀏覽器中運行，這已成為現實。根據 [Show HN: 蘋果 SHARP 模型透過 ONNX Runtime Web 在瀏覽器中運行 | Hacker News](https://news.ycombinator.com/item?id=47995037) 的報導，現在無需在電腦上安裝複雜程式的麻煩，只需訪問網站即可將平面照片轉換為生動的 3D 空間。

今天 **MindTickleBytes** 將以簡單易懂的方式，為您揭開這項魔法般技術的真面目，並解釋為什麼這個消息會讓全球開發者和 AI 愛好者感到興奮。

## 為什麼這很重要？您的電腦將成為「AI 工廠」

到目前為止，我們能方便地使用 ChatGPT 這種聰明的 AI，是因為我們提出問題後，由遠方巨大的超級電腦（伺服器）代為運算並傳回答案。然而，將照片轉換為 3D 的過程需要龐大的運算量，伺服器營運成本非常昂貴，而且還要將珍貴的個人照片傳送到其他公司的伺服器，不免令人感到不安。

但這次公開的技術採用了截然不同的方法。它將 AI 模型完整地帶進了您的 Chrome 或 Safari 等網頁瀏覽器中。這種「瀏覽器端 AI 推論 (In-browser inference)」為我們帶來了三個大禮： [AI 代理的 WebAssembly：在瀏覽器中運行模型](https://callsphere.ai/blog/webassembly-ai-agents-running-models-in-the-browser)

1.  **徹底的隱私保護**：您上傳的照片絕不會踏出外部伺服器半步。因為所有的 3D 轉換工作都只在您的智慧型手機或筆記型電腦內部秘密進行。 [在瀏覽器中使用 ONNX 運行 YOLO 模型... - PyImageSearch](https://pyimagesearch.com/2025/07/28/run-yolo-model-in-the-browser-with-onnx-webassembly-and-next-js/)
2.  **零伺服器成本**：對於營運服務的公司來說，無需租用昂貴的超級電腦，因此可以增加創新的免費服務；對於用戶來說，則不必因為伺服器擁擠而盯著「載入中」的畫面苦苦等待。
3.  **無延遲的即時反應**：即使網路連接速度稍慢也沒關係。它能 100% 發揮您裝置本身擁有的性能，即時確認結果。

## 輕鬆理解：什麼是「SHARP」與「高斯潑濺」？

首先，讓我們來了解一下名字聽起來很陌生的蘋果 **SHARP** 是什麼吧。SHARP 是一個非常聰明的 AI 藍圖，它只要看到一張照片，就能準確推測出該物體或場所隱藏的立體結構。 [GitHub - bring-shrubbery/ml-sharp-web](https://github.com/bring-shrubbery/ml-sharp-web)

該模型使用的核心技術在專業術語上稱為 **高斯潑濺 (Gaussian Splatting)**。雖然名詞很深奧，但如果用我們熟悉的事物來比喻，原理就非常簡單。

> **比喻如下！**
> 如果說傳統的 3D 技術是透過精確拼接硬梆梆的樂高積木或三角形碎片來製作模型，那麼 **高斯潑濺** 就像是在空中噴灑無數半透明的「棉花糖球」來塑造立體形狀。

當數百萬個帶有獨特顏色和透明度的小橢球體（棉花糖球）漂浮在各自的位置上時，在我們眼中就會呈現出一個邊界柔和且栩栩如生的 3D 空間。 [GitHub - bring-shrubbery/ml-sharp-web](https://app.daily.dev/posts/github---bring-shrubbery-ml-sharp-web-web-playground-to-create-gaussian-splats-using-apple-s-ml-sha-0sg97lpiv) 而 SHARP 正是扮演著指揮家的角色，告訴這些無數的棉花糖球應該分佈在什麼位置、以多大的尺寸呈現。 [為您的裝置轉換蘋果的 Sharp ML | Raleigh](https://sf.aitinkerers.org/talks/rsvp_kERNVs9PVNw)

## 瀏覽器如何運行如此沉重的 AI？

這項技術原本被設計成只能在配備高性能顯示卡、價值數百萬元的專業研究用電腦上運行。那麼，它是如何在我們使用的普通網頁瀏覽器中實現的呢？這裡隱藏著兩位秘密特工。

第一位特工是 **ONNX Runtime Web**。 [ONNX Runtime Web — 在瀏覽器中運行您的機器學習模型 | Microsoft 開源部落格](https://opensource.microsoft.com/blog/2021/09/02/onnx-runtime-web-running-your-machine-learning-model-in-browser/) AI 模型會根據開發環境的不同而使用不同的語言，而 **ONNX (開放神經網路交換)** 就像是一個「萬能翻譯機」，能將它們統一起來，使其在任何環境下都能溝通。 [ONNX Runtime | 首頁](https://onnxruntime.ai/) 開發者們成功地將蘋果原始的模型語言（PyTorch 格式）重構為這種萬能翻譯機語言，並傳遞到瀏覽器中。 [為您的裝置轉換蘋果的 Sharp ML | Raleigh](https://sf.aitinkerers.org/talks/rsvp_kERNVs9PVNw) [GitHub - miketahani/ml-sharp-browser](https://github.com/miketahani/ml-sharp-browser)

第二位特工是 **WebAssembly (Wasm)** 與 **WebGPU** 技術。這就像是一條「專用高速公路」，讓瀏覽器不再僅限於顯示文字或圖片，而是可以直接借用電腦心臟 CPU 或大腦 GPU 的強大運算能力。正因如此，即使是高達 2.4 GB 的龐大 AI 模型，也能在瀏覽器這個狹窄的通道內飛馳。 [GitHub - bring-shrubbery/ml-sharp-web](https://app.daily.dev/posts/github---bring-shrubbery-ml-sharp-web-web-playground-to-create-gaussian-splats-using-apple-s-ml-sha-0sg97lpiv)

## 現狀：我們能親自體驗嗎？

動作敏捷的開發者們已經公開了一個任何人都可以體驗這項技術的線上「AI 遊樂場」。 [GitHub - bring-shrubbery/ml-sharp-web](https://github.com/bring-shrubbery/ml-sharp-web) 在那裡上傳一張照片，AI 就會即時塑造出立體形象，您還可以將其儲存在電腦中（.ply 檔案格式）。 [GitHub - bring-shrubbery/ml-sharp-web](https://app.daily.dev/posts/github---bring-shrubbery-ml-sharp-web-web-playground-to-create-gaussian-splats-using-apple-s-ml-sha-0sg97lpiv)

不過，在實際體驗前有幾個「注意點」：

*   **注意數據流量**：AI 模型的大小約為 2.4 GB，相當龐大。 [GitHub - bring-shrubbery/ml-sharp-web](https://app.daily.dev/posts/github---bring-shrubbery-ml-sharp-web-web-playground-to-create-gaussian-splats-using-apple-s-ml-sha-0sg97lpiv) 每運行一次都會下載相當於一部高畫質電影的數據量，如果您使用的不是數據吃到飽方案，請務必在 Wi-Fi 環境下連接。
*   **研究用許可證**：目前蘋果公開的 SHARP 核心權重（模型的智能）不能用於商業營利目的，規定只能用於個人研究或學習。 [Show HN: 蘋果 SHARP 模型透過 ONNX...](https://qht.co/item?id=47995037)
*   **裝置規格**：並非在所有裝置上都能完美運作。特別是在 iPhone 或 iPad 等 iOS 裝置上，由於瀏覽器本身技術支援不足（如尚未支援 WebGPU 等），可能無法順暢運行。 [[網頁] 支援 iOS 裝置 · Issue #22776 · microsoft/onnxruntime](https://github.com/microsoft/onnxruntime/issues/22776)

## 未來會如何發展？我們生活的變化

蘋果的 SHARP 技術插上瀏覽器的翅膀，僅僅是巨大變革的開始。目前已經出現了在蘋果最尖端的空間運算設備 **Vision Pro** 上運行該技術的演示案例。 [為您的裝置轉換蘋果的 Sharp ML | Raleigh](https://sf.aitinkerers.org/talks/rsvp_kERNVs9PVNw)

在不久的將來，當我們在網上商店挑選衣服時，只需一張照片即可創建與自己體型相同的 3D 化身進行「虛擬試穿」，或是透過旅遊時拍下的一張充滿回憶的照片，再次以 3D 方式漫步於那天的空間感中。最重要的是，這所有魔法般的過程都能在保護個人隱私的安全前提下，像瀏覽網頁一樣簡便地完成，無需額外安裝應用程式，這點最令人期待。

**MindTickleBytes AI 記者觀點：**
「受困於平面限制的數位影像，透過瀏覽器獲得了立體生命力。未來如果模型容量能進一步縮減，且行動裝置的支援度擴大，我們拍攝照片的意義將超越單純的『記錄記憶』，進化為栩栩如生的『空間再現』。」

## 參考資料

1. [Show HN: Apple's Sharp Running in the Browser via ONNX Runtime Web | Hacker News](https://news.ycombinator.com/item?id=47995037)
2. [GitHub - bring-shrubbery/ml-sharp-web: 使用蘋果 ml-sharp 模型創建高斯潑濺的網頁遊樂場 | GitHub](https://github.com/bring-shrubbery/ml-sharp-web)
3. [Apple - CoreML | onnxruntime](https://onnxruntime.ai/docs/execution-providers/CoreML-ExecutionProvider.html)
4. [為您的裝置轉換蘋果的 Sharp ML | Raleigh](https://sf.aitinkerers.org/talks/rsvp_kERNVs9PVNw)
5. [ONNX Runtime Web — 在瀏覽器中運行您的機器學習模型 | Microsoft 開源部落格](https://opensource.microsoft.com/blog/2021/09/02/onnx-runtime-web-running-your-machine-learning-model-in-browser/)
6. [[網頁] 支援 iOS 裝置 · Issue #22776 · microsoft/onnxruntime](https://github.com/microsoft/onnxruntime/issues/22776)
7. [Show HN: 蘋果 SHARP 模型透過 ONNX...](https://qht.co/item?id=47995037)
8. [ONNX Runtime | 首頁](https://onnxruntime.ai/)
9. [AI 代理的 WebAssembly：在瀏覽器中運行模型](https://callsphere.ai/blog/webassembly-ai-agents-running-models-in-the-browser)
10. [在瀏覽器中使用 ONNX、WebAssembly 和 Next.js 運行 YOLO 模型 - PyImageSearch](https://pyimagesearch.com/2025/07/28/run-yolo-model-in-the-browser-with-onnx-webassembly-and-next-js/)
11. [GitHub - bring-shrubbery/ml-sharp-web: 網頁遊樂場... (Daily.dev)](https://app.daily.dev/posts/github---bring-shrubbery-ml-sharp-web-web-playground-to-create-gaussian-splats-using-apple-s-ml-sha-0sg97lpiv)
12. [GitHub - miketahani/ml-sharp-browser: 在瀏覽器中運行的蘋果 SHARP 模型...](https://github.com/miketahani/ml-sharp-browser)
13. [網頁 | onnxruntime 教程](https://onnxruntime.ai/docs/tutorials/web/)