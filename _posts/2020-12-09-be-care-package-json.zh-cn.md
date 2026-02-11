---
layout: post
title: 在使用 Webpack 时注意 package.json 数据安全
tags: [react, jsx, webpack]
style: border
color: primary
description: 在使用 webpack 创建生产环境构建时，请务必小心，避免将 package.json 信息泄露到构建文件中。
lang: zh-cn
ref: 2020-12-09-be-care-package-json
---

## 在什么背景下？

我当时正在使用 webpack 3.8.1，运行 `webpack build` 后得到了 `main.[chunkhash:8].js`。

那时，我的 `package.json` 数据被包含在了 `main.xxxx.js` 文件中。

当我将其部署到服务中时，这引发了安全问题。

实际上，我使用了私有 npm 仓库中的私有 npm 模块。

就在这时，有人阅读了我的 `main.js` 文件并获取了 `package.json` 的数据。

之后，他在公共 npm 仓库中创建了一个与我在 `package.json` 中使用的私有模块同名的模块，并将其上传。

他上传了从 0.0.1 到 9.9.9 的所有版本。

正因为如此，我的构建服务器在 Jenkins 构建过程中会优先读取公共 npm 数据，导致每次构建都失败。

## 如何解决？

我在我的日志 HOC jsx 文件中发现了从 `package.json` 导入 `{version}` 的代码，如下所示：

```js
import {version} from '../package.json'
```

当 webpack 以生产模式构建时，所有 `package.json` 的数据都被打包进了 `main.xxxx.js` 中。

于是，我删除了这段代码。

我改用 `webpack.DefinePlugin`，它可以在构建 webpack 时使指定的数据作为全局变量可用。

当前的服务版本被保存在一个隔离的全局变量中，当实际使用时从该变量中读取 `package.json` 的版本信息。

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

## 结论

当我结合 babel 使用 webpack 时，我设置了 presets `modules:false`。

所以我认为当我使用类似 `import {version} from 'package.json'` 的代码时，它会被 Tree-shaking 优化掉，因此只有版本号会出现在 `main.xxxx.js` 捆绑文件中。但事实并非如此。

现在我知道对于 JSON 文件，`import` 的工作方式与 `require` 类似，所以它不支持 Tree-shaking。

回想起来，这是一次令人羞愧的经历。

> _求知若渴，虚心若愚 (Stay Hungry, Stay Foolish)_
