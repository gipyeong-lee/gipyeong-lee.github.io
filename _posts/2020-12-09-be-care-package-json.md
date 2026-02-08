---
layout: post
title: Be care package.json data with webpack
tags: [react, jsx, webpack]
style: border
color: primary
description: When creating a production build using webpack, be careful not to get the package.json information involved.
lang: ko
ref: 2020-12-09-be-care-package-json
---

## Under what circumstances?

I was using webpack 3.8.1 and run `webpack build` after build i got main.[chunkhash:8].js

At that time my `package.json` data was included in main.xxxx.js file.

That makes secure issue when i deployed that onto service.

Actually i used private npm module own private npm repository.

At this point, someone read my main.js file and got the `package.json data`.

After that, he created a module with the same name as the module I personally created in pakcage.json and uploaded it to the public npm repository.

All versions from 0.0.1 to 9.9.9 were uploaded.

Because of this, My build server that reads the public npm data during jenkins build first failed to build each time.

## How to Solved?

I found import {version} from package.json in my logging hoc jsx file. like below

```js
import {version} from '../package.json'
```

When webpack build by production mode. All of package.json data was implemented in `main.xxxx.js`.

So, I removed that codes.

I used `webpack.DefinePlugin`, which makes the saved data available as global variables when building webpack.

The current service version is saved in an isolated global variable, and the version information of package.json is read from the variable when it is actually used.

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

When i using webpack with babel. I setup presets `modules:false`.

So i think when i using like that codes `import {version} from 'package.json'` it would be tree-shaked. so, only version would be appear in main.xxxx.js bundle file. but it wasn't.

Now i knew `import` file is same working with `require`. so it wasn't working with tree-shaking.

In retrospect, it was a shameful experience.

> _Stay Hunger, Stay Foolish_
