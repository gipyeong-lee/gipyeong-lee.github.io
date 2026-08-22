---
layout: post
title: "[Swift] Identifiable, Codable, Hashable Protocol"
description: "Swift에서는 프로토콜이 중요한 역할을 합니다. 프로토콜은 특정 기능을 수행하기 위해 필요한 속성과 메서드를 정의하는 인터페이스이며, 이 프로토콜을 채택한 타입은 프로토콜의 요구사항을 구현해야 합니다. 이번 포스트에서는 사용자 모델을 만들 때 유용하게 사용되는 Identifiab..."
date: 2024-09-22 23:29:23 +0900
section: blog
category: engineering
lang: ko
ref: 2024-09-22-legacy-347-engineering-swift-identifiable-codable-hashable-protocol
tags:
  - "프로토콜"
  - "ios"
  - "protocol"
  - "identifiable"
  - "swift"
  - "SwiftUI"
---

<blockquote>
Swift에서는 프로토콜이 중요한 역할을 합니다. 프로토콜은 특정 기능을 수행하기 위해 필요한 속성과 메서드를 정의하는 인터페이스이며, 이 프로토콜을 채택한 타입은 프로토콜의 요구사항을 구현해야 합니다. 이번 포스트에서는 사용자 모델을 만들 때 유용하게 사용되는 Identifiable, Codable, Hashable 프로토콜에 대해 설명하겠습니다.
</blockquote>
<h3>
<span>
사용자 모델 구조체 정의 예제
</span>
</h3>
<p>
<span>
아래는
<code>
User
</code>
라는 구조체를 정의하고
<code>
Identifiable
</code>
,
<code>
Codable
</code>
,
<code>
Hashable
</code>
프로토콜을 채택한 코드입니다.
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
이 구조체는 사용자의 정보를 담기 위해 정의된 모델입니다. 위 코드에서 가장 주목할 부분은
<code>
Identifiable
</code>
,
<code>
Codable
</code>
,
<code>
Hashable
</code>
이라는 세 가지 프로토콜을 채택했다는 점입니다. 이제 각각의 프로토콜이 무엇을 의미하며, 왜 이 코드에서 중요한지 설명해드리겠습니다.
</span>
</p>
<hr>
<h2>
<span>
1.
<code>
Identifiable
</code>
프로토콜
</span>
</h2>
<p>
<span>
<code>
Identifiable
</code>
프로토콜은 SwiftUI와 밀접한 관련이 있습니다. SwiftUI는 목록을 렌더링할 때 각 항목을 고유하게 식별할 수 있어야 하기 때문에,
<code>
Identifiable
</code>
프로토콜은 이를 위한 고유 식별자를 제공하는 역할을 합니다.
</span>
</p>
<h3>
<span>
요구 사항
</span>
</h3>
<p>
<span>
<code>
Identifiable
</code>
프로토콜은
<code>
id
</code>
라는 속성을 요구하며, 이 속성은 고유해야 합니다.
<code>
User
</code>
구조체에서
<code>
id
</code>
는
<code>
String
</code>
타입으로 정의되어 있으며, 이 값을 통해 사용자는 고유하게 식별됩니다.
</span>
</p>
<h3>
<span>
장점
</span>
</h3>
<ul>
<li>
<span>
<b>
SwiftUI와의 호환성
</b>
: SwiftUI에서 리스트나 데이터를 렌더링할 때, 각 항목을 식별할 수 있는
<code>
id
</code>
가 필요합니다. 이를 자동으로 지원할 수 있게 해줍니다.
</span>
</li>
<li>
<span>
<b>
고유한 데이터 관리
</b>
:
<code>
id
</code>
를 통해 사용자를 구분하므로, 목록에서 중복되지 않는 고유한 항목을 쉽게 관리할 수 있습니다.
</span>
</li>
</ul>
<h3>
<span>
예시 코드
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
SwiftUI 리스트에서 사용될 때,
<code>
users
</code>
배열의 각 항목은
<code>
id
</code>
값을 통해 식별됩니다.
</span>
</p>
<hr>
<h2>
<span>
2.
<code>
Codable
</code>
프로토콜
</span>
</h2>
<p>
<span>
<code>
Codable
</code>
프로토콜은 JSON과 같은 외부 데이터 형식으로 변환하거나, 그 데이터를 Swift 객체로 변환할 수 있도록 해줍니다. 이는 두 개의 프로토콜(
<code>
Encodable
</code>
,
<code>
Decodable
</code>
)을 결합한 형태로, 객체를 쉽게 직렬화(encode)하거나 역직렬화(decode)할 수 있습니다.
</span>
</p>
<h3>
<span>
요구 사항
</span>
</h3>
<p>
<span>
<code>
Codable
</code>
은 기본적으로 구조체의 모든 속성을 자동으로 직렬화 및 역직렬화하는 기능을 제공합니다. 즉, 별도의 코드를 작성하지 않아도 JSON 데이터를 Swift의
<code>
User
</code>
객체로 변환하거나 그 반대로 변환할 수 있습니다.
</span>
</p>
<h3>
<span>
장점
</span>
</h3>
<ul>
<li>
<span>
<b>
네트워크 통신
</b>
: API에서 받아온 JSON 데이터를 쉽게 Swift 객체로 변환할 수 있으며, 서버로 데이터를 보낼 때도 유용합니다.
</span>
</li>
<li>
<span>
<b>
파일 저장
</b>
: 사용자 데이터를 파일로 저장할 때 객체를 JSON 포맷으로 변환하여 쉽게 저장할 수 있습니다.
</span>
</li>
</ul>
<h3>
<span>
예시 코드
</span>
</h3>
<pre class="reasonml">
<code>
// User 객체를 JSON으로 인코딩
let encoder = JSONEncoder()
if let jsonData = try? encoder.encode(user1) {
    print(String(data: jsonData, encoding: .utf8)!)
}

// JSON을 User 객체로 디코딩
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
프로토콜
</span>
</h2>
<p>
<span>
<code>
Hashable
</code>
프로토콜은 객체를 해시할 수 있도록 해줍니다. 해시 함수는 객체를 고유하게 식별하는 데 사용되는 정수 값을 생성하며, 이를 통해 객체를 Set이나 Dictionary와 같은 컬렉션에 사용할 수 있습니다.
</span>
</p>
<h3>
<span>
요구 사항
</span>
</h3>
<p>
<span>
<code>
Hashable
</code>
프로토콜은 객체가
<code>
hashValue
</code>
라는 고유한 정수 값을 가져야 한다는 것을 요구합니다. 하지만 Swift는 대부분의 경우 자동으로 이 값을 생성해줍니다.
</span>
</p>
<h3>
<span>
장점
</span>
</h3>
<ul>
<li>
<span>
<b>
Set 및 Dictionary 사용 가능
</b>
:
<code>
User
</code>
객체를 Set의 요소나 Dictionary의 키로 사용할 수 있습니다.
</span>
</li>
<li>
<span>
<b>
빠른 검색
</b>
: 해시 값을 사용하여 데이터를 빠르게 검색할 수 있습니다.
</span>
</li>
</ul>
<h3>
<span>
예시 코드
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
<code>
User
</code>
구조체가
<code>
Hashable
</code>
을 준수하지 않으면, Set이나 Dictionary에 사용할 수 없습니다. 이때
<code>
Hashable
</code>
을 채택하면 객체의 고유한 해시 값을 생성해 사용 가능합니다.
</span>
</p>
<hr>
<h2>
<span>
결론
</span>
</h2>
<p>
<span>
<code>
Identifiable
</code>
,
<code>
Codable
</code>
,
<code>
Hashable
</code>
프로토콜은 Swift에서 매우 유용하며, 특히 데이터 모델을 정의할 때 자주 사용됩니다. 이 세 가지 프로토콜을 함께 사용하면,
<b>
UI에서의 데이터 관리
</b>
,
<b>
API 통신
</b>
,
<b>
컬렉션 내 빠른 데이터 검색
</b>
등의 다양한 요구 사항을 효율적으로 처리할 수 있습니다. 이번 포스트에서 소개한 사용자 모델 예제를 통해, Swift에서 프로토콜을 활용하는 방법을 보다 잘 이해하셨길 바랍니다.
</span>
</p>
