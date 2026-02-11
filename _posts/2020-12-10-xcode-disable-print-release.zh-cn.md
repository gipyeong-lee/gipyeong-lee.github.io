---
layout: post
title: 在 Xcode 中使用 Swift 构建 Release 方案时禁用 print
tags: [swift, iOS, Xcode]
style: border
color: dark
description: 在 Xcode 的 Release 构建情况下，通过重写 print 函数来防止调试信息输出
lang: zh-cn
ref: 2020-12-10-xcode-disable-print-release
---

## 在什么情况下？

- Xcode 12.2 版本
- 使用 Swift 5

## 如何操作？

这是一种禁用 print 函数的非常简单的方法。

如果你正在使用 Swift 进行开发，放在哪个 Swift 文件中都无所谓。请插入下面的代码。在我的案例中，我将其插入到了 AppDelegate 的顶部。

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

插入代码后，请将构建方案（build scheme）的环境从 debug 更改为 release。请参考下图。

![image](/assets/images/blog/2020-12-10-xcode-disable-print-release/image1.png)

如果你需要再次打印，请将方案更改回 debug。

## 结论

在使用 Swift 开发应用程序时，重写函数非常有用。

> _求知若渴，虚心若愚_
