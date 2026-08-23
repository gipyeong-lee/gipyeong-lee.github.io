---
layout: post
title: "[Swift] Identifiable, Codable, Hashable Protocols"
description: "Protocols play an important role in Swift. A protocol is an interface that defines the properties and methods required to perform a specific task, and types that adopt the protocol must implement its requirements. In this post, I will explain the Identifiable, Codable, and Hashable protocols, which are useful when creating user models."
date: 2024-09-22 23:29:23 +0900
section: blog
category: engineering
lang: en
ref: 2024-09-22-legacy-347-engineering-swift-identifiable-codable-hashable-protocol
tags:
  - "protocol"
  - "ios"
  - "protocol"
  - "identifiable"
  - "swift"
  - "SwiftUI"
translation_source_hash: 9b3f4bd22a9a144f388888b70a98f1e4417b71298fb618d5107ace09b1ebb4eb
---

<blockquote>
Protocols play an important role in Swift. A protocol is an interface that defines the properties and methods required to perform a specific task, and types that adopt the protocol must implement its requirements. In this post, I will explain the Identifiable, Codable, and Hashable protocols, which are useful when creating user models.
</blockquote>

<h3>
<span>
User Model Struct Definition Example
</span>
</h3>
<p>
<span>
Below is code that defines a struct named <code>User</code> and adopts the <code>Identifiable</code>, <code>Codable</code>, and <code>Hashable</code> protocols.
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
This struct is a model defined to hold user information. The most notable part of the code above is that it adopts three protocols: <code>Identifiable</code>, <code>Codable</code>, and <code>Hashable</code>. Now, I will explain what each protocol means and why they are important in this code.
</span>
</p>
<hr>
<h2>
<span>
1. <code>Identifiable</code> Protocol
</span>
</h2>
<p>
<span>
The <code>Identifiable</code> protocol is closely related to SwiftUI. Since SwiftUI needs to uniquely identify each item when rendering a list, the <code>Identifiable</code> protocol provides a unique identifier for this purpose.
</span>
</p>
<h3>
<span>
Requirements
</span>
</h3>
<p>
<span>
The <code>Identifiable</code> protocol requires an <code>id</code> property, which must be unique. In the <code>User</code> struct, <code>id</code> is defined as a <code>String</code> type, and users are uniquely identified through this value.
</span>
</p>
<h3>
<span>
Benefits
</span>
</h3>
<ul>
<li>
<span>
<b>Compatibility with SwiftUI</b>: When rendering lists or data in SwiftUI, an <code>id</code> is needed to identify each item. This protocol provides support for that automatically.
</span>
</li>
<li>
<span>
<b>Unique Data Management</b>: Since users are distinguished by their <code>id</code>, it is easy to manage unique items in a list without duplication.
</span>
</li>
</ul>
<h3>
<span>
Example Code
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
When used in a SwiftUI list, each item in the <code>users</code> array is identified by its <code>id</code> value.
</span>
</p>
<hr>
<h2>
<span>
2. <code>Codable</code> Protocol
</span>
</h2>
<p>
<span>
The <code>Codable</code> protocol allows you to convert objects to and from external data formats such as JSON. It is a combination of two protocols (<code>Encodable</code> and <code>Decodable</code>), allowing for easy serialization (encoding) or deserialization (decoding) of objects.
</span>
</p>
<h3>
<span>
Requirements
</span>
</h3>
<p>
<span>
<code>Codable</code> essentially provides the ability to automatically serialize and deserialize all properties of a struct. This means you can convert JSON data into a Swift <code>User</code> object, or vice-versa, without writing any extra code.
</span>
</p>
<h3>
<span>
Benefits
</span>
</h3>
<ul>
<li>
<span>
<b>Network Communication</b>: It is easy to convert JSON data received from an API into Swift objects, and it is also useful when sending data to a server.
</span>
</li>
<li>
<span>
<b>File Storage</b>: When saving user data to a file, you can easily convert the object to JSON format for storage.
</span>
</li>
</ul>
<h3>
<span>
Example Code
</span>
</h3>
<pre class="reasonml">
<code>
// Encode User object to JSON
let encoder = JSONEncoder()
if let jsonData = try? encoder.encode(user1) {
    print(String(data: jsonData, encoding: .utf8)!)
}

// Decode JSON into User object
let decoder = JSONDecoder()
if let decodedUser = try? decoder.decode(User.self, from: jsonData) {
    print(decodedUser)
}
</code>
</pre>
<hr>
<h2>
<span>
3. <code>Hashable</code> Protocol
</span>
</h2>
<p>
<span>
The <code>Hashable</code> protocol allows an object to be hashed. A hash function generates an integer value used to uniquely identify an object, which enables the object to be used in collections such as Sets or Dictionaries.
</span>
</p>
<h3>
<span>
Requirements
</span>
</h3>
<p>
<span>
The <code>Hashable</code> protocol requires that an object have a unique integer value called <code>hashValue</code>. However, in most cases, Swift generates this value automatically.
</span>
</p>
<h3>
<span>
Benefits
</span>
</h3>
<ul>
<li>
<span>
<b>Usable in Sets and Dictionaries</b>: You can use <code>User</code> objects as elements in a Set or as keys in a Dictionary.
</span>
</li>
<li>
<span>
<b>Fast Searching</b>: Data can be searched quickly using the hash value.
</span>
</li>
</ul>
<h3>
<span>
Example Code
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
If the <code>User</code> struct does not conform to <code>Hashable</code>, it cannot be used in a Set or Dictionary. By adopting <code>Hashable</code>, a unique hash value is generated for the object, making it usable.
</span>
</p>
<hr>
<h2>
<span>
Conclusion
</span>
</h2>
<p>
<span>
The <code>Identifiable</code>, <code>Codable</code>, and <code>Hashable</code> protocols are very useful in Swift, and are frequently used when defining data models. By using these three protocols together, you can efficiently handle various requirements such as <b>data management in the UI</b>, <b>API communication</b>, and <b>fast data searching within collections</b>. I hope the user model example introduced in this post helps you better understand how to utilize protocols in Swift.
</span>
</p>