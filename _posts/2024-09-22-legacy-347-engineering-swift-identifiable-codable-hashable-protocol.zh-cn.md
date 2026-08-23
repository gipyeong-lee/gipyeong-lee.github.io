---
layout: post
title: "[Swift] Identifiable, Codable, Hashable 协议"
description: "在 Swift 中，协议扮演着重要的角色。协议是定义执行特定功能所需属性和方法的接口，遵循该协议的类型必须实现协议的要求。本篇博客将介绍在创建用户模型时非常实用的 Identifiable、Codable 和 Hashable 协议。"
date: 2024-09-22 23:29:23 +0900
section: blog
category: engineering
lang: zh-cn
ref: 2024-09-22-legacy-347-engineering-swift-identifiable-codable-hashable-protocol
tags:
  - "协议"
  - "ios"
  - "protocol"
  - "identifiable"
  - "swift"
  - "SwiftUI"
translation_source_hash: 9b3f4bd22a9a144f388888b70a98f1e4417b71298fb618d5107ace09b1ebb4eb
---

<blockquote>
在 Swift 中，协议扮演着重要的角色。协议是定义执行特定功能所需属性和方法的接口，遵循该协议的类型必须实现协议的要求。本篇博客将介绍在创建用户模型时非常实用的 Identifiable、Codable 和 Hashable 协议。
</blockquote>

<h3>
<span>
用户模型结构体定义示例
</span>
</h3>
<p>
<span>
以下是定义了一个名为 <code>User</code> 的结构体，并遵循 <code>Identifiable</code>、<code>Codable</code> 和 <code>Hashable</code> 协议的代码。
</span>
</p>
<pre class="rust">
<code>
import Foundation

struct User: Identifiable, Codable, Hashable {
    let id: String
    let fullname: String
    let email: String
    let username: String
    let profileImageUrl: String?
    let bio: String?

    init(
        id: String,
        fullname: String,
        email: String,
        username: String,
        profileImageUrl: String? = nil,
        bio: String? = nil)
    {
        self.id = id
        self.fullname = fullname
        self.email = email
        self.username = username
        self.profileImageUrl = profileImageUrl
        self.bio = bio
    }
}
</code>
</pre>
<p>
<span>
该结构体是为了存储用户信息而定义的模型。在上述代码中，最值得关注的是它遵循了 <code>Identifiable</code>、<code>Codable</code> 和 <code>Hashable</code> 这三个协议。现在我将解释每个协议的含义，以及为什么它们在这个代码中如此重要。
</span>
</p>
<hr>
<h2>
<span>
1. <code>Identifiable</code> 协议
</span>
</h2>
<p>
<span>
<code>Identifiable</code> 协议与 SwiftUI 密切相关。当 SwiftUI 渲染列表时，需要能够唯一地识别每一项，因此 <code>Identifiable</code> 协议的作用就是提供用于此目的的唯一标识符。
</span>
</p>
<h3>
<span>
要求
</span>
</h3>
<p>
<span>
<code>Identifiable</code> 协议要求具备一个名为 <code>id</code> 的属性，且该属性必须是唯一的。在 <code>User</code> 结构体中，<code>id</code> 定义为 <code>String</code> 类型，通过该值来唯一标识用户。
</span>
</p>
<h3>
<span>
优点
</span>
</h3>
<ul>
<li>
<span>
<b>
与 SwiftUI 的兼容性
</b>
：在 SwiftUI 中渲染列表或数据时，需要一个能够识别每一项的 <code>id</code>。该协议使其能够自动提供支持。
</span>
</li>
<li>
<span>
<b>
唯一数据管理
</b>
：由于通过 <code>id</code> 来区分用户，因此可以轻松管理列表中不重复的唯一项。
</span>
</li>
</ul>
<h3>
<span>
示例代码
</span>
</h3>
<pre class="reasonml">
<code>
let user1 = User(id: "123", fullname: "John Doe", email: "john@example.com", username: "johnny")
let user2 = User(id: "456", fullname: "Jane Doe", email: "jane@example.com", username: "janedoe")

let users = [user1, user2]
</code>
</pre>
<p>
<span>
当在 SwiftUI 列表中使用时，<code>users</code> 数组的每一项都会通过 <code>id</code> 值进行识别。
</span>
</p>
<hr>
<h2>
<span>
2. <code>Codable</code> 协议
</span>
</h2>
<p>
<span>
<code>Codable</code> 协议允许将对象转换为 JSON 等外部数据格式，或将这些数据转换为 Swift 对象。它是两个协议（<code>Encodable</code> 和 <code>Decodable</code>）的组合，可以轻松地对对象进行序列化（encode）或反序列化（decode）。
</span>
</p>
<h3>
<span>
要求
</span>
</h3>
<p>
<span>
<code>Codable</code> 默认提供自动序列化和反序列化结构体所有属性的功能。这意味着无需编写额外的代码，就可以将 JSON 数据转换为 Swift 的 <code>User</code> 对象，反之亦然。
</span>
</p>
<h3>
<span>
优点
</span>
</h3>
<ul>
<li>
<span>
<b>
网络通信
</b>
：可以轻松地将从 API 获取的 JSON 数据转换为 Swift 对象，在向服务器发送数据时也非常有用。
</span>
</li>
<li>
<span>
<b>
文件存储
</b>
：将用户数据存储到文件时，可以轻松地将对象转换为 JSON 格式进行保存。
</span>
</li>
</ul>
<h3>
<span>
示例代码
</span>
</h3>
<pre class="reasonml">
<code>
// 将 User 对象编码为 JSON
let encoder = JSONEncoder()
if let jsonData = try? encoder.encode(user1) {
    print(String(data: jsonData, encoding: .utf8)!)
}

// 将 JSON 解码为 User 对象
let decoder = JSONDecoder()
if let decodedUser = try? decoder.decode(User.self, from: jsonData) {
    print(decodedUser)
}
</code>
</pre>
<hr>
<h2>
<span>
3. <code>Hashable</code> 协议
</span>
</h2>
<p>
<span>
<code>Hashable</code> 协议允许对象被哈希化。哈希函数用于生成一个整数值，该值用于唯一标识对象，从而可以将对象用于 Set 或 Dictionary 等集合中。
</span>
</p>
<h3>
<span>
要求
</span>
</h3>
<p>
<span>
<code>Hashable</code> 协议要求对象必须具有一个名为 <code>hashValue</code> 的唯一整数值。但在大多数情况下，Swift 会自动生成该值。
</span>
</p>
<h3>
<span>
优点
</span>
</h3>
<ul>
<li>
<span>
<b>
可以使用 Set 和 Dictionary
</b>
：可以将 <code>User</code> 对象用作 Set 的元素或 Dictionary 的键。
</span>
</li>
<li>
<span>
<b>
快速检索
</b>
：可以使用哈希值快速检索数据。
</span>
</li>
</ul>
<h3>
<span>
示例代码
</span>
</h3>
<pre class="groovy">
<code>
var userSet: Set&lt;User&gt; = [user1, user2]
let userDict: [User: String] = [user1: "First User", user2: "Second User"]
</code>
</pre>
<p>
<span>
如果 <code>User</code> 结构体不遵循 <code>Hashable</code>，则无法将其用于 Set 或 Dictionary。通过遵循 <code>Hashable</code>，可以生成对象的唯一哈希值并使用。
</span>
</p>
<hr>
<h2>
<span>
结论
</span>
</h2>
<p>
<span>
<code>Identifiable</code>、<code>Codable</code> 和 <code>Hashable</code> 协议在 Swift 中非常有用，特别是在定义数据模型时经常被使用。如果同时使用这三个协议，可以高效地处理 <b>UI 中的数据管理</b>、<b>API 通信</b> 以及 <b>集合内的快速数据检索</b> 等各种需求。希望通过本篇博客介绍的用户模型示例，能让大家更好地理解在 Swift 中如何利用协议。
</span>
</p>