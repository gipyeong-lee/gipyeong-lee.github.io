---
layout: post
title: 在 Xcode 中使用 Swift 進行 Release 編譯時停用 print
tags: [swift, iOS, Xcode]
style: border
color: dark
description: 在 Xcode 的 Release 編譯情況下，覆寫 print 函式以防止偵錯輸出
lang: zh-tw
ref: 2020-12-10-xcode-disable-print-release
---

## 在什麼情況下？

- Xcode 12.2 版本
- 使用 Swift 5

## 如何操作？

停用 print 函式的方法非常簡單。

如果您正在使用 Swift 進行開發，在哪個 Swift 檔案中編寫都沒有關係。請插入下方的程式碼。在我的案例中，我將其插入在 AppDelegate 的最上方。

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

插入程式碼後，請將 Build Scheme 環境從 Debug 更改為 Release。
請參考下圖。

![image](/assets/images/blog/2020-12-10-xcode-disable-print-release/image1.png)

如果您再次需要 print 輸出，請將 Scheme 改回 Debug。

## 結論

在使用 Swift 開發應用程式時，覆寫函式（Override function）非常有用。

> _求知若渴，虛懷若愚 (Stay Hungry, Stay Foolish)_
