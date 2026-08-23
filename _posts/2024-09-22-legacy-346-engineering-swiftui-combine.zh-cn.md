---
layout: post
title: "[SwiftUI] 使用 Combine 进行实时数据订阅与更新"
description: "SwiftUI 和 Combine 让 iOS 应用开发中的异步数据处理变得非常简单且高效。特别是利用 @Published 和 Combine 的订阅功能，可以在数据实时更新时自动刷新视图。在本文中，我们将通过 ProfileViewModel 示例，介绍如何在 SwiftUI 中利用 Combine 高效管理实时更新的数据。"
date: 2024-09-22 01:43:29 +0900
section: blog
category: engineering
lang: zh-cn
ref: 2024-09-22-legacy-346-engineering-swiftui-combine
tags:
  - "Combine"
  - "SwiftUI"
  - " @Published"
  - "ObservableObject"
  - "swift"
  - "Apple Ecosystem Insights"
translation_source_hash: 26c4f698cc23d8e77414996800e645740657f52bc01baf206d502ad82874766a
---

<blockquote>
<span>
SwiftUI 和 Combine 让 iOS 应用开发中的异步数据处理变得非常简单且高效。特别是利用 @Published 和 Combine 的订阅功能，可以在数据实时更新时自动刷新视图。在本文中，我们将通过 ProfileViewModel 示例，介绍如何在 SwiftUI 中利用 Combine 高效管理实时更新的数据。
</span>
</blockquote>

<h3>
<span>
代码示例：
<code>
ProfileViewModel
</code>
</span>
</h3>
<pre class="bash">
<code>
class ProfileViewModel: ObservableObject {
    @Published var currentUser: User?
    private var cancellables = Set&lt;AnyCancellable&gt;()

    init() {
        setupSubscribers()
    }

    private func setupSubscribers() {
        UserService.shared.$currentUser.sink { [weak self] user in
            self?.currentUser = user
        }.store(in: &amp;cancellables)
    }
}
</code>
</pre>
<p>
<span>
这段代码定义了一个 
<code>
ProfileViewModel
</code>
，它能实时更新用户配置数据并将其反映在 SwiftUI 视图中。通过 Combine 的数据订阅以及 
<code>
@Published
</code>
 属性，可以轻松实现与 SwiftUI 的状态同步。
</span>
</p>

<h3>
<span>
代码分析
</span>
</h3>

<h4>
<span>
1. 
<code>
class ProfileViewModel: ObservableObject
</code>
</span>
</h4>
<p>
<span>
<code>
ProfileViewModel
</code>
 遵循 
<code>
ObservableObject
</code>
 协议。通过这种方式，
<b>
ViewModel
</b>
 可以向 SwiftUI 视图提供数据，并在数据变更时触发视图的自动更新。
</span>
</p>

<h4>
<span>
2. 
<code>
@Published var currentUser: User?
</code>
</span>
</h4>
<p>
<span>
<code>
@Published
</code>
 属性包装器可以确保每当 
<code>
currentUser
</code>
 更新时，
<b>
SwiftUI
</b>
 都能检测到变更并重新渲染视图。这使得数据流的管理更加
<b>
响应式
</b>
，用户信息的变动能立即反映在界面上。
</span>
</p>

<h4>
<span>
3. 
<code>
private var cancellables = Set&lt;AnyCancellable&gt;()
</code>
</span>
</h4>
<p>
<span>
这是一个存储 
<code>
AnyCancellable
</code>
（订阅取消对象）的集合。在 Swift 中，妥善管理 
<b>
Cancellable
</b>
 对于防止内存泄漏以及按需取消订阅至关重要。
</span>
</p>

<h4>
<span>
4. 
<code>
init()
</code>
 与 
<code>
setupSubscribers()
</code>
</span>
</h4>
<p>
<span>
<code>
init
</code>
 方法在 
<code>
ProfileViewModel
</code>
 对象创建时调用，并通过 
<code>
setupSubscribers()
</code>
 方法初始化 Combine 的订阅设置。
</span>
</p>

<h4>
<span>
5. 
<code>
UserService.shared.$currentUser.sink { [weak self] user in ... }
</code>
</span>
</h4>
<p>
<span>
这是 
<b>
Combine
</b>
 的核心部分。它订阅了 
<code>
UserService
</code>
 中声明为 
<code>
@Published
</code>
 的 
<code>
currentUser
</code>
，每当数据变更时，闭包就会执行。
<code>
[weak self]
</code>
 用于防止循环引用，通过弱引用 
<code>
self
</code>
 来优化内存管理。
</span>
</p>

<h4>
<span>
6. 
<code>
self?.currentUser = user
</code>
</span>
</h4>
<p>
<span>
将从数据流中传递过来的 
<code>
user
</code>
 对象赋值给视图模型的 
<code>
currentUser
</code>
。由此，
<b>
SwiftUI 视图会检测到变更
</b>
，并对相关视图进行重新渲染。
</span>
</p>

<h4>
<span>
7. 
<code>
print("DEBUG: User in view model from combine is \(user)")
</code>
</span>
</h4>
<p>
<span>
这是用于调试的代码，输出通过 Combine 传递的数据。在确认实时数据流时非常有用。
</span>
</p>

<h4>
<span>
8. 
<code>
.store(in: &amp;cancellables)
</code>
</span>
</h4>
<p>
<span>
订阅完成后，将其存入 
<b>
cancellables
</b>
 以便
<b>
防止内存泄漏
</b>
并进行订阅管理。此方法确保在不需要 Combine 订阅时，内存能被自动释放。
</span>
</p>

<hr>

<h3>
<b>
<span>
为什么需要这段代码？
</span>
</b>
</h3>
<ol>
<li>
<span>
<b>
实时数据反映
</b>
：当应用内的用户信息发生变化时，需要实时更新界面。例如，当用户登录或登出时，ViewModel 可以自动更新该信息。
</span>
</li>
<li>
<span>
<b>
内存管理
</b>
：为有效管理内存，必须能够在订阅结束时注销订阅。使用 Combine 的 
<code>
AnyCancellable
</code>
 可以注销不再需要的订阅，从而防止内存泄漏。
</span>
</li>
<li>
<span>
<b>
响应式应用设计
</b>
：SwiftUI 的优势之一在于其数据与视图之间的
<b>
响应式数据流
</b>
。使用 Combine 后，数据变更时视图会自动更新，用户可以获得自然且实时的 UI 体验。
</span>
</li>
</ol>

<hr>

<h3>
<span>
结论
</span>
</h3>
<p>
<span>
通过使用 Combine，可以简单地订阅数据流，并在状态实时变更时轻松更新视图。这种与 SwiftUI 相结合的机制是现代 iOS 应用开发中非常强大的工具。特别是 
<code>
@Published
</code>
 和 Combine 的订阅模式，对于高效管理数据流以及关注内存管理的开发场景来说是必不可少的。
</span>
</p>

## 参考资料

- [Combine - Apple Developer Documentation](https://developer.apple.com/documentation/combine)
- [ObservableObject - SwiftUI Documentation](https://developer.apple.com/documentation/swiftui/observableobject)