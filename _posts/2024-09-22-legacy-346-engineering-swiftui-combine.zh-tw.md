---
layout: post
title: "[SwiftUI] 使用 Combine 進行實時數據訂閱與更新"
description: "SwiftUI 和 Combine 讓 iOS 應用開發中的異步數據處理變得非常簡單且高效。特別是結合 @Published 和 Combine 的訂閱功能，數據實時更新時，視圖可以自動刷新。本篇將透過 ProfileViewModel 示例，介紹如何在 SwiftUI 中利用 Combine 進行數據實時更新與高效管理。"
date: 2024-09-22 01:43:29 +0900
section: blog
category: engineering
lang: zh-tw
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
SwiftUI 和 Combine 讓 iOS 應用開發中的異步數據處理變得非常簡單且高效。特別是結合 @Published 和 Combine 的訂閱功能，數據實時更新時，視圖可以自動刷新。本篇將透過 ProfileViewModel 示例，介紹如何在 SwiftUI 中利用 Combine 進行數據實時更新與高效管理。
</span>
</blockquote>

<h3>
<span>
代碼示例：
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
此代碼定義了一個 
<code>
ProfileViewModel
</code>
，用於實時更新用戶資料數據並反映至 SwiftUI 視圖。透過 Combine 的數據訂閱以及 
<code>
@Published
</code>
 屬性，可以輕鬆設定與 SwiftUI 的狀態聯動。
</span>
</p>

<h3>
<span>
代碼分析
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
 遵循了 
<code>
ObservableObject
</code>
 協議。這使得 
<b>
ViewModel
</b>
 能夠為 SwiftUI 視圖提供數據，並在數據變更時讓視圖自動更新。
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
 屬性包裝器會讓 
<code>
currentUser
</code>
 在更新時，通知 
<b>
SwiftUI
</b>
 偵測到變更並重新渲染視圖。這使得數據流的管理變得 
<b>
響應式
</b>
，當用戶資訊改變時，視圖能立即反映。
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
這是一個用來儲存訂閱取消對象 
<code>
AnyCancellable
</code>
 的集合。在 Swift 中，為了防止記憶體洩漏並按需取消訂閱，妥善管理 
<b>
Cancellable
</b>
 是非常重要的。
</span>
</p>

<h4>
<span>
4. 
<code>
init()
</code>
 與 
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
 方法會在 
<code>
ProfileViewModel
</code>
 對象建立時呼叫，並透過 
<code>
setupSubscribers()
</code>
 方法初始化 Combine 的訂閱設定。
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
這是 
<b>
Combine
</b>
 的核心部分。它訂閱 (subscribe) 了 
<code>
UserService
</code>
 中宣告為 
<code>
@Published
</code>
 的 
<code>
currentUser
</code>
，一旦數據變更，閉包 (closure) 就會執行。使用 
<code>
[weak self]
</code>
 是為了防止循環參照 (retain cycle)，以弱參照方式獲取 
<code>
self
</code>
，有利於記憶體管理。
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
將數據流中傳遞的 
<code>
user
</code>
 對象賦值給 ViewModel 的 
<code>
currentUser
</code>
。這導致 
<b>
SwiftUI 視圖偵測到數據已變更
</b>
，進而重新渲染視圖。
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
此程式碼用於除錯 (debug)，輸出透過 Combine 傳遞的數據。這在確認實時數據流時非常實用。
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
訂閱完成後將其儲存於 
<b>
cancellables
</b>
 中，以達到 
<b>
防止記憶體洩漏
</b>
 及管理訂閱的目的。此方法確保當 Combine 訂閱不再需要時，能從記憶體中自動釋放。
</span>
</p>

<hr>
<h3>
<b>
<span>
為何需要這段代碼？
</span>
</b>
</h3>
<ol>
<li>
<span>
<b>
實時數據反映
</b>
：當應用內用戶資訊變更時，需要實時更新時非常有用。例如，用戶登入或登出時，視圖模型可自動更新該資訊。
</span>
</li>
<li>
<span>
<b>
記憶體管理
</b>
：為了在訂閱結束時有效管理記憶體，必須能夠取消訂閱。利用 Combine 的 
<code>
AnyCancellable
</code>
 可取消不必要的訂閱，防止記憶體洩漏。
</span>
</li>
<li>
<span>
<b>
響應式應用設計
</b>
：SwiftUI 的優勢之一在於數據與視圖之間的 
<b>
響應式流
</b>
。使用 Combine，數據變更時視圖會自動調整，用戶體驗到的是自然且實時更新的 UI。
</span>
</li>
</ol>

<hr>
<h3>
<span>
結論
</span>
</h3>
<p>
<span>
利用 Combine，可以輕鬆地訂閱數據流，並在狀態實時變更時輕易更新視圖。這種結合 SwiftUI 的機制，是現代 iOS 應用開發中強大的工具。特別是 
<code>
@Published
</code>
 與 Combine 的訂閱模式，對於有效管理數據流以及兼顧記憶體管理的應用開發來說，是必不可少的。
</span>
</p>

## 參考資料