---
layout: post
title: Disable print when build release scheme in Xcode with swift
tags: [swift, iOS, Xcode]
style: border
color: dark
description: In case of release build in Xcode, override print function to prevent debugging
---

## Under what circumstances?

- Under Xcode 12.2
- With Swift5

## How to do?

It's very simple way to be disable print function.

If you are developing using Swift, it doesn't matter which swift file. Please insert the code below. In my case, I inserted it at the top of the AppDelegate.

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

After insert codes, please change build scheme environment debug to release.
follow below image.

![image](/assets/images/blog/2020-12-10-xcode-disable-print-release/image1.png)

If you need print again, changed scheme to debug.

## Conclusion

Override function is very useful when i develop application by swift

> _Stay Hunger, Stay Foolish_
