---
layout: post
title: SwiftとXcodeでのリリースビルド時にprint出力を無効にする
tags: [swift, iOS, Xcode]
style: border
color: dark
description: Xcodeのリリースビルドにおいて、デバッグ出力を防ぐためにprint関数をオーバーライドする方法について。
lang: ja
ref: 2020-12-10-xcode-disable-print-release
---

## 動作環境

- Xcode 12.2
- Swift 5

## 設定方法

print関数を無効にする方法は非常に簡単です。

Swiftを使用して開発している場合、どのswiftファイルでも構いませんので、以下のコードを挿入してください。私の場合は `AppDelegate` の先頭に挿入しました。

```swift
import UIKit
import CoreData
...

func print(_ items: Any...) {
    #if DEBUG
        Swift.print(items[0])
    #endif
}

 @UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {
...
```

コードを挿入した後、ビルドスキームの環境設定を `debug` から `release` に変更してください。
以下の画像を参考にしてください。

![image](/assets/images/blog/2020-12-10-xcode-disable-print-release/image1.png)

再度 print 出力が必要になった場合は、スキームを `debug` に戻してください。

## 結論

Swiftでアプリケーションを開発する際、関数のオーバーライドは非常に便利です。

> _Stay Hungry, Stay Foolish_
