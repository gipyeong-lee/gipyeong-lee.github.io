---
layout: post
title: "[SwiftUI] Real-time Data Subscription and Updates with Combine"
description: "SwiftUI and Combine make asynchronous data processing in iOS app development simple and efficient. In particular, you can automatically refresh views whenever data is updated in real-time by leveraging @Published and Combine's subscription features. In this post, we will look at how to..."
date: 2024-09-22 01:43:29 +0900
section: blog
category: engineering
lang: en
ref: 2024-09-22-legacy-346-engineering-swiftui-combine
tags:
  - "Combine"
  - "SwiftUI"
  - "@Published"
  - "ObservableObject"
  - "swift"
  - "Apple Ecosystem Insights"
translation_source_hash: 26c4f698cc23d8e77414996800e645740657f52bc01baf206d502ad82874766a
---

<blockquote>
<span>
SwiftUI and Combine make asynchronous data processing in iOS app development simple and efficient. In particular, you can automatically refresh views whenever data is updated in real-time by leveraging @Published and Combine's subscription features. In this post, using the ProfileViewModel example, we will introduce how to update data in real-time and manage it efficiently in SwiftUI using Combine.
</span>
</blockquote>

<h3>
<span>
Code Example: <code>ProfileViewModel</code>
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
This code defines <code>ProfileViewModel</code>, which updates user profile data in real-time and reflects it in the SwiftUI view. You can easily set up state synchronization with SwiftUI by using Combine-based data subscription and the <code>@Published</code> property wrapper.
</span>
</p>

<h3>
<span>
Code Analysis
</span>
</h3>

<h4>
<span>
1. <code>class ProfileViewModel: ObservableObject</code>
</span>
</h4>
<p>
<span>
<code>ProfileViewModel</code> conforms to the <code>ObservableObject</code> protocol. This allows the <b>ViewModel</b> to provide data to SwiftUI views and enables the view to automatically update when the data changes.
</span>
</p>

<h4>
<span>
2. <code>@Published var currentUser: User?</code>
</span>
</h4>
<p>
<span>
The <code>@Published</code> property wrapper ensures that whenever <code>currentUser</code> is updated, <b>SwiftUI</b> detects the change and re-renders the view. This allows you to manage the data flow <b>reactively</b>, ensuring that changes to user information are immediately reflected in the view.
</span>
</p>

<h4>
<span>
3. <code>private var cancellables = Set&lt;AnyCancellable&gt;()</code>
</span>
</h4>
<p>
<span>
This is a collection that stores <code>AnyCancellable</code> objects, which represent subscriptions that can be cancelled. It is important in Swift to manage <b>Cancellables</b> to prevent memory leaks and cancel subscriptions when they are no longer needed.
</span>
</p>

<h4>
<span>
4. <code>init()</code> and <code>setupSubscribers()</code>
</span>
</h4>
<p>
<span>
The <code>init</code> method is called when the <code>ProfileViewModel</code> object is created, and it initializes the Combine subscription setup via the <code>setupSubscribers()</code> method.
</span>
</p>

<h4>
<span>
5. <code>UserService.shared.$currentUser.sink { [weak self] user in ... }</code>
</span>
</h4>
<p>
<span>
This is the core of <b>Combine</b>. It subscribes to <code>currentUser</code>, which is declared as a <code>@Published</code> property in <code>UserService</code>, and executes the closure whenever the data changes. <code>[weak self]</code> is used to prevent retain cycles, capturing <code>self</code> weakly to ensure proper memory management.
</span>
</p>

<h4>
<span>
6. <code>self?.currentUser = user</code>
</span>
</h4>
<p>
<span>
The <code>user</code> object passed from the data stream is assigned to the ViewModel's <code>currentUser</code>. As a result, the <b>SwiftUI view detects the changed data</b> and is re-rendered accordingly.
</span>
</p>

<h4>
<span>
7. <code>print("DEBUG: User in view model from combine is \(user)")</code>
</span>
</h4>
<p>
<span>
This code prints the data received via Combine for debugging purposes. It is useful for verifying real-time data flow.
</span>
</p>

<h4>
<span>
8. <code>.store(in: &amp;cancellables)</code>
</span>
</h4>
<p>
<span>
After completing the subscription, it is stored in <b>cancellables</b> to enable <b>memory leak prevention</b> and subscription management. This method ensures that the Combine subscription is automatically released from memory when it is no longer required.
</span>
</p>

<hr>

<h3>
<b>
<span>
Why is this code necessary?
</span>
</b>
</h3>
<ol>
<li>
<span>
<b>Real-time data reflection</b>: It is highly useful when user information changes within the app and needs to be reflected in real-time. For example, when a user logs in or logs out, this information can be updated automatically in the ViewModel.
</span>
</li>
<li>
<span>
<b>Memory management</b>: To manage memory efficiently when a subscription ends, you must be able to cancel it. Using Combine's <code>AnyCancellable</code> allows you to release unnecessary subscriptions, preventing memory leaks.
</span>
</li>
<li>
<span>
<b>Reactive app design</b>: One of the strengths of SwiftUI is the <b>reactive flow</b> between data and views. Using Combine allows the view to update automatically whenever data changes, providing users with a natural, real-time UI experience.
</span>
</li>
</ol>

<hr>

<h3>
<span>
Conclusion
</span>
</h3>
<p>
<span>
Using Combine makes it easy to subscribe to data flow and update views whenever the state changes in real-time. This mechanism, combined with SwiftUI, can be a powerful tool in modern iOS app development. In particular, the subscription pattern between <code>@Published</code> and Combine is essential for managing data flow efficiently and handling memory management.
</span>
</p>

## References

- [Combine - Apple Developer Documentation](https://developer.apple.com/documentation/combine)
- [ObservableObject - Apple Developer Documentation](https://developer.apple.com/documentation/combine/observableobject)