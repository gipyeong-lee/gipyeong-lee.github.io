---
layout: post
title: Be Careful with package.json Data in Webpack
style: border
color: primary
description: When creating a production build using Webpack, be careful not to inadvertently include package.json information.
lang: en
ref: 2020-12-09-be-care-package-json
---

## The Scenario

I was using Webpack 3.8.1. After running `webpack build`, I generated the `main.[chunkhash:8].js` file.

However, I noticed that my `package.json` data was included in the `main.xxxx.js` bundle.

This created a security issue when I deployed it to the service.

I was using private npm modules hosted on a private npm repository. Someone analyzed my `main.js` file and extracted the `package.json` data.

Subsequently, they created a module with the same name as my private module found in `package.json` and uploaded it to the public npm registry. They uploaded every version number from 0.0.1 to 9.9.9.

As a result, my build server (Jenkins), which reads from the public npm registry during builds, failed to build every time because of the conflict.

## The Solution

I discovered an import statement extracting the version from `package.json` in my logging HOC (Higher-Order Component) JSX file, as shown below:

```js
import {version} from '../package.json'
```

When Webpack built the project in production mode, the entire content of `package.json` was bundled into `main.xxxx.js`.

So, I removed that code.

Instead, I used `webpack.DefinePlugin`, which exposes defined data as global variables during the Webpack build process.

I saved the current service version in an isolated global variable. The code then reads the version information from this variable when needed, rather than importing the file.

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

## Conclusion

When using Webpack with Babel, I had set the presets to `modules:false`.

I assumed that by using `import {version} from 'package.json'`, tree-shaking would occur, and only the `version` field would appear in the `main.xxxx.js` bundle. However, that was not the case.

I realized that importing a JSON file behaves similarly to `require`, preventing effective tree-shaking of the JSON content.

In retrospect, it was an embarrassing experience.

> _Stay Hungry, Stay Foolish_
