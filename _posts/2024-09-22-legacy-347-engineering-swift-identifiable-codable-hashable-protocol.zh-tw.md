---
layout: post
title: "[Swift] Identifiable, Codable, Hashable 協定"
description: "在 Swift 中，協定（Protocol）扮演著重要的角色。協定是一種介面，定義了執行特定功能所需的屬性和方法，而採用該協定的型別必須實作其需求。本篇文章將介紹在建立使用者模型時非常實用的 Identifiable、Codable 與 Hashable 協定。"
date: 2024-09-22 23:29:23 +0900
section: blog
category: engineering
lang: zh-tw
ref: 2024-09-22-legacy-347-engineering-swift-identifiable-codable-hashable-protocol
tags:
  - "協定"
  - "ios"
  - "protocol"
  - "identifiable"
  - "swift"
  - "SwiftUI"
translation_source_hash: 9b3f4bd22a9a144f388888b70a98f1e4417b71298fb618d5107ace09b1ebb4eb
---

<blockquote>
在 Swift 中，協定（Protocol）扮演著重要的角色。協定是一種介面，定義了執行特定功能所需的屬性和方法，而採用該協定的型別必須實作其需求。本篇文章將介紹在建立使用者模型時非常實用的 Identifiable、Codable 與 Hashable 協定。
</blockquote>
<h3>
<span>
使用者模型結構體定義範例
</span>
</h3>
<p>
<span>
以下是定義名為
<code>
User
</code>
的結構體，並採用
<code>
Identifiable
</code>
、
<code>
Codable
</code>
、
<code>
Hashable
</code>
協定的程式碼。
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
此結構體是用於存放使用者資訊的模型。上述程式碼中最值得關注的部分，是它採用了
<code>
Identifiable
</code>
、
<code>
Codable
</code>
與
<code>
Hashable
</code>
這三種協定。接下來將說明各個協定的意義，以及為何在這個範例中如此重要。
</span>
</p>
<hr>
<h2>
<span>
1.
<code>
Identifiable
</code>
協定
</span>
</h2>
<p>
<span>
<code>
Identifiable
</code>
協定與 SwiftUI 密切相關。由於 SwiftUI 在渲染列表時必須能夠唯一識別每個項目，因此
<code>
Identifiable
</code>
協定負責提供用於識別的唯一識別碼。
</span>
</p>
<h3>
<span>
需求
</span>
</h3>
<p>
<span>
<code>
Identifiable
</code>
協定要求必須具備名為
<code>
id
</code>
的屬性，且該屬性必須是唯一的。在
<code>
User
</code>
結構體中，
<code>
id
</code>
被定義為
<code>
String
</code>
型別，透過此值來唯一識別使用者。
</span>
</p>
<h3>
<span>
優點
</span>
</h3>
<ul>
<li>
<span>
<b>
與 SwiftUI 的相容性
</b>
：在 SwiftUI 中渲染列表或資料時，需要一個能識別各項目的
<code>
id
</code>
。此協定可自動提供支援。
</span>
</li>
<li>
<span>
<b>
唯一的資料管理
</b>
：透過
<code>
id
</code>
區分使用者，可以輕鬆管理列表中不重複且唯一的項目。
</span>
</li>
</ul>
<h3>
<span>
範例程式碼
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
當在 SwiftUI 列表中使用時，
<code>
users
</code>
陣列中的每個項目都會透過
<code>
id
</code>
值進行識別。
</span>
</p>
<hr>
<h2>
<span>
2.
<code>
Codable
</code>
協定
</span>
</h2>
<p>
<span>
<code>
Codable
</code>
協定能夠將資料轉換為外部格式（如 JSON），或將該資料轉換回 Swift 物件。它是兩個協定（
<code>
Encodable
</code>
、
<code>
Decodable
</code>
）的組合，可以輕鬆對物件進行序列化（encode）或反序列化（decode）。
</span>
</p>
<h3>
<span>
需求
</span>
</h3>
<p>
<span>
<code>
Codable
</code>
基本上提供了自動序列化及反序列化結構體所有屬性的功能。換句話說，無需編寫額外的程式碼，即可將 JSON 資料轉換為 Swift 的
<code>
User
</code>
物件，反之亦然。
</span>
</p>
<h3>
<span>
優點
</span>
</h3>
<ul>
<li>
<span>
<b>
網路通訊
</b>
：可以輕鬆將從 API 接收到的 JSON 資料轉換為 Swift 物件，在向伺服器發送資料時也十分方便。
</span>
</li>
<li>
<span>
<b>
檔案儲存
</b>
：將使用者資料儲存為檔案時，可將物件轉換為 JSON 格式輕鬆進行存檔。
</span>
</li>
</ul>
<h3>
<span>
範例程式碼
</span>
</h3>
<pre class="reasonml">
<code>
// 將 User 物件編碼為 JSON
let encoder = JSONEncoder()
if let jsonData = try? encoder.encode(user1) {
    print(String(data: jsonData, encoding: .utf8)!)
}

// 將 JSON 解碼為 User 物件
let decoder = JSONDecoder()
if let decodedUser = try? decoder.decode(User.self, from: jsonData) {
    print(decodedUser)
}
</code>
</pre>
<hr>
<h2>
<span>
3.
<code>
Hashable
</code>
協定
</span>
</h2>
<p>
<span>
<code>
Hashable
</code>
協定使物件能夠被雜湊（hash）。雜湊函式會產生一個用於唯一識別物件的整數值，透過此值，即可將物件用於 Set 或 Dictionary 等集合中。
</span>
</p>
<h3>
<span>
需求
</span>
</h3>
<p>
<span>
<code>
Hashable
</code>
協定要求物件必須擁有一個稱為
<code>
hashValue
</code>
的唯一整數值。不過，在大多數情況下，Swift 會自動產生此值。
</span>
</p>
<h3>
<span>
優點
</span>
</h3>
<ul>
<li>
<span>
<b>
可使用 Set 及 Dictionary
</b>
：可以將
<code>
User
</code>
物件用作 Set 的元素或 Dictionary 的鍵（key）。
</span>
</li>
<li>
<span>
<b>
快速搜尋
</b>
：利用雜湊值可以快速搜尋資料。
</span>
</li>
</ul>
<h3>
<span>
範例程式碼
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
如果
<code>
User
</code>
結構體未遵守
<code>
Hashable
</code>
，則無法用於 Set 或 Dictionary。此時只要採用
<code>
Hashable
</code>
，即可產生並使用物件獨有的雜湊值。
</span>
</p>
<hr>
<h2>
<span>
結論
</span>
</h2>
<p>
<span>
<code>
Identifiable
</code>
、
<code>
Codable
</code>
與
<code>
Hashable
</code>
協定在 Swift 中非常實用，特別是在定義資料模型時經常使用。結合使用這三種協定，可以有效處理
<b>
UI 中的資料管理
</b>
、
<b>
API 通訊
</b>
以及
<b>
集合內的快速資料搜尋
</b>
等各種需求。希望透過本篇文章介紹的使用者模型範例，能讓您更深入理解在 Swift 中活用協定的方法。
</span>
</p>