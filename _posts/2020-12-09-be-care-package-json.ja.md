---
layout: post
title: Webpack使用時のpackage.jsonデータの取り扱いに注意
style: border
color: primary
description: Webpackを使用して本番ビルドを作成する際、package.jsonの情報が巻き込まれないように注意してください。
lang: ja
ref: 2020-12-09-be-care-package-json
---

## どのような状況だったか？

Webpack 3.8.1を使用しており、`webpack build`を実行した後、main.[chunkhash:8].jsが生成されました。

その際、私の`package.json`のデータがmain.xxxx.jsファイルに含まれてしまっていました。

これをサービスにデプロイした際、セキュリティ上の問題となりました。

実際、私は独自のプライベートnpmリポジトリにあるプライベートnpmモジュールを使用していました。

この時点で、誰かが私のmain.jsファイルを読み、`package.json`のデータを取得してしまったのです。

その後、その人物は私が`package.json`で個人的に作成したモジュールと同じ名前のモジュールを作成し、パブリックnpmリポジトリにアップロードしました。

0.0.1から9.9.9までのすべてのバージョンがアップロードされてしまったのです。

このため、Jenkinsビルド中にパブリックnpmデータを先に読みに行く私のビルドサーバーは、毎回ビルドに失敗するようになってしまいました。

## 解決策は？

ロギング用のHOC JSXファイル内に、以下のような`import {version} from package.json`という記述を見つけました。

```js
import {version} from '../package.json'
```

Webpackでプロダクションモードでビルドすると、`package.json`のすべてのデータが`main.xxxx.js`に実装されてしまっていました。

そこで、そのコードを削除しました。

代わりに`webpack.DefinePlugin`を使用しました。これは、Webpackのビルド時に保存されたデータをグローバル変数として利用できるようにするものです。

現在のサービスのバージョンを独立したグローバル変数に保存し、実際に使用される際にその変数から`package.json`のバージョン情報を読み込むようにしました。

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

Babelと一緒にWebpackを使用する際、プリセットで`modules:false`を設定していました。

そのため、`import {version} from 'package.json'`のようなコードを使えばTree Shakingが行われ、バージョン情報だけが`main.xxxx.js`バンドルファイルに含まれると考えていました。しかし、そうではありませんでした。

今では、ファイルの`import`は`require`と同じように動作するため、Tree Shakingが機能していなかったことがわかりました。

振り返ってみると、恥ずかしい経験でした。

> _Stay Hungry, Stay Foolish_
