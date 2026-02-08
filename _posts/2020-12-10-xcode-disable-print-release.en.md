---
layout: post
title: Disabling the print function for Release builds in Xcode with Swift
tags: [swift, iOS, Xcode]
style: border
color: dark
description: Learn how to override the print function in Xcode Release builds to prevent debug logs from appearing in production.
lang: en
ref: 2020-12-10-xcode-disable-print-release
---

## Environment

- Xcode 12.2
- Swift 5

## Implementation

It is a very simple process to disable the `print` function.

When developing with Swift, you can add the following code to any Swift file. In my case, I placed it at the top of the `AppDelegate`.

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

After adding the code, change the build scheme from **Debug** to **Release**.
Refer to the image below:

![image](/assets/images/blog/2020-12-10-xcode-disable-print-release/image1.png)

If you need to enable printing again, simply switch the scheme back to **Debug**.

## Conclusion

Overriding functions is a very useful technique when developing applications with Swift.

> _Stay Hungry, Stay Foolish_
