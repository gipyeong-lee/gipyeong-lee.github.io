---
layout: post
title: 使用 Webpack 時需警惕 package.json 資料洩漏
tags: [react, jsx, webpack]
style: border
color: primary
description: 在使用 Webpack 進行生產環境打包時，請務必小心，避免將 package.json 的敏感資訊洩漏到 bundle 檔案中。
lang: zh-tw
ref: 2020-12-09-be-care-package-json
---

## 在什麼情況下發生？

我當時正在使用 Webpack 3.8.1，在執行 `webpack build` 後生成了 main.[chunkhash:8].js。

當時，我的 `package.json` 完整資料被包含在了 main.xxxx.js 檔案中。

這在我將服務部署到生產環境時引發了安全性問題。

具體來說，我使用了託管在私有 npm 倉庫中的私有 npm 模組。

此時，有人讀取了我的 main.js 檔案並獲取了 `package.json` 的內容。

隨後，他在公開的 npm 倉庫中建立了一個與我在 package.json 中定義的私有模組同名的模組，並將其上傳。

他上傳了從 0.0.1 到 9.9.9 的所有版本。

因此，我的構建伺服器在 Jenkins 執行期間會優先抓取公開 npm 倉庫的資料，導致每次構建都失敗。

## 如何解決？

我在一個日誌記錄 HOC (Higher-Order Component) jsx 檔案中發現了如下匯入語句：

```js
import {version} from '../package.json'
```

當 Webpack 以生產模式構建時，整個 package.json 的資料都被打包進了 `main.xxxx.js`。

因此，我移除了這段程式碼。

我改用 `webpack.DefinePlugin`，它可以在 Webpack 構建時將特定資料定義為全域變數。

目前的服務版本被儲存在一個獨立的全域變數中，在實際使用時，會從該變數讀取 package.json 的版本資訊。

```js
webpack.config.js
const defined = {'process.package': { VERSION:JSON.stringify(packageConfig.version)}}
module.exports = {
   ...
   plugins : [
      new webpack.DefinePlugin(defined),
      ...
   ],
   ...
```

```js
log.hoc.jsx
const logInfo = { version: process.package.VERSION, ... }
```

## 結論

當我搭配 Babel 使用 Webpack 時，我將 presets 設置為 `modules:false`。

因此我原以為使用 `import {version} from 'package.json'` 這樣的程式碼時，Webpack 會進行 Tree-shaking，只有 version 欄位會出現在 main.xxxx.js 中。但事實並非如此。

現在我明白了，直接 `import` JSON 檔案的效果與 `require` 類似，Tree-shaking 在這種情況下並不生效。

回想起來，這是一次深刻且令人汗顏的教訓。

> _求知若渴，虛懷若谷_
