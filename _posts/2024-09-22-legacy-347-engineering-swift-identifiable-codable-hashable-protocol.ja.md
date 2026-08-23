---
layout: post
title: "[Swift] Identifiable, Codable, Hashable プロトコル"
description: "Swiftにおいてプロトコルは重要な役割を果たします。プロトコルは特定の機能を実行するために必要なプロパティやメソッドを定義するインターフェースであり、このプロトコルを採用した型はプロトコルの要件を実装しなければなりません。今回の投稿では、ユーザーモデルを作成する際に役立つ Identifiable、Codable、Hashable プロトコルについて説明します。"
date: 2024-09-22 23:29:23 +0900
section: blog
category: engineering
lang: ja
ref: 2024-09-22-legacy-347-engineering-swift-identifiable-codable-hashable-protocol
tags:
  - "プロトコル"
  - "ios"
  - "protocol"
  - "identifiable"
  - "swift"
  - "SwiftUI"
translation_source_hash: 9b3f4bd22a9a144f388888b70a98f1e4417b71298fb618d5107ace09b1ebb4eb
---

<blockquote>
Swiftにおいてプロトコルは重要な役割を果たします。プロトコルは特定の機能を実行するために必要なプロパティやメソッドを定義するインターフェースであり、このプロトコルを採用した型はプロトコルの要件を実装しなければなりません。今回の投稿では、ユーザーモデルを作成する際に役立つ Identifiable、Codable、Hashable プロトコルについて説明します。
</blockquote>
<h3>
<span>
ユーザーモデル構造体の定義例
</span>
</h3>
<p>
<span>
以下は
<code>
User
</code>
という構造体を定義し、
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
プロトコルを採用したコードです。
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
この構造体はユーザーの情報を保持するために定義されたモデルです。上記のコードで最も注目すべき点は、
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
という3つのプロトコルを採用しているという点です。それぞれのプロトコルが何を意味し、なぜこのコードにおいて重要なのかを説明します。
</span>
</p>
<hr>
<h2>
<span>
1.
<code>
Identifiable
</code>
プロトコル
</span>
</h2>
<p>
<span>
<code>
Identifiable
</code>
プロトコルは SwiftUI と密接な関連があります。SwiftUI はリストをレンダリングする際、各項目を一意に識別できる必要があるため、
<code>
Identifiable
</code>
プロトコルはそのための固有識別子を提供する役割を果たします。
</span>
</p>
<h3>
<span>
要件
</span>
</h3>
<p>
<span>
<code>
Identifiable
</code>
プロトコルは
<code>
id
</code>
というプロパティを要求し、このプロパティは一意である必要があります。
<code>
User
</code>
構造体では
<code>
id
</code>
は
<code>
String
</code>
型として定義されており、この値を通じてユーザーは一意に識別されます。
</span>
</p>
<h3>
<span>
利点
</span>
</h3>
<ul>
<li>
<span>
<b>
SwiftUI との互換性
</b>
: SwiftUI でリストやデータをレンダリングする際、各項目を識別できる
<code>
id
</code>
が必要です。これを自動的にサポートできるようになります。
</span>
</li>
<li>
<span>
<b>
一意なデータ管理
</b>
:
<code>
id
</code>
を通じてユーザーを区別するため、リスト内で重複しない一意の項目を簡単に管理できます。
</span>
</li>
</ul>
<h3>
<span>
コード例
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
SwiftUI のリストで使用される際、
<code>
users
</code>
配列の各項目は
<code>
id
</code>
値を通じて識別されます。
</span>
</p>
<hr>
<h2>
<span>
2.
<code>
Codable
</code>
プロトコル
</span>
</h2>
<p>
<span>
<code>
Codable
</code>
プロトコルは、JSON などの外部データ形式に変換したり、そのデータを Swift オブジェクトに変換したりすることを可能にします。これは2つのプロトコル（
<code>
Encodable
</code>
、
<code>
Decodable
</code>
）を組み合わせた形で、オブジェクトを簡単にシリアライズ（encode）したりデシリアライズ（decode）したりできます。
</span>
</p>
<h3>
<span>
要件
</span>
</h3>
<p>
<span>
<code>
Codable
</code>
は基本的に、構造体のすべてのプロパティを自動的にシリアライズおよびデシリアライズする機能を提供します。つまり、別途コードを書かなくても、JSON データを Swift の
<code>
User
</code>
オブジェクトに変換したり、その逆に変換したりできます。
</span>
</p>
<h3>
<span>
利点
</span>
</h3>
<ul>
<li>
<span>
<b>
ネットワーク通信
</b>
: API から受け取った JSON データを簡単に Swift オブジェクトに変換でき、サーバーにデータを送信する際にも役立ちます。
</span>
</li>
<li>
<span>
<b>
ファイル保存
</b>
: ユーザーデータをファイルとして保存する際、オブジェクトを JSON 形式に変換して簡単に保存できます。
</span>
</li>
</ul>
<h3>
<span>
コード例
</span>
</h3>
<pre class="reasonml">
<code>
// User オブジェクトを JSON にエンコード
let encoder = JSONEncoder()
if let jsonData = try? encoder.encode(user1) {
    print(String(data: jsonData, encoding: .utf8)!)
}

// JSON を User オブジェクトにデコード
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
プロトコル
</span>
</h2>
<p>
<span>
<code>
Hashable
</code>
プロトコルは、オブジェクトをハッシュ化できるようにします。ハッシュ関数は、オブジェクトを一意に識別するために使用される整数値を生成し、これを通じてオブジェクトを Set や Dictionary などのコレクションで使用できるようになります。
</span>
</p>
<h3>
<span>
要件
</span>
</h3>
<p>
<span>
<code>
Hashable
</code>
プロトコルは、オブジェクトが
<code>
hashValue
</code>
という固有の整数値を持つことを要求します。しかし、Swift は多くの場合、この値を自動的に生成してくれます。
</span>
</p>
<h3>
<span>
利点
</span>
</h3>
<ul>
<li>
<span>
<b>
Set および Dictionary での使用が可能
</b>
:
<code>
User
</code>
オブジェクトを Set の要素や Dictionary のキーとして使用できます。
</span>
</li>
<li>
<span>
<b>
高速な検索
</b>
: ハッシュ値を使用してデータを高速に検索できます。
</span>
</li>
</ul>
<h3>
<span>
コード例
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
構造体が
<code>
Hashable
</code>
に準拠していない場合、Set や Dictionary には使用できません。このとき
<code>
Hashable
</code>
を採用すれば、オブジェクト固有のハッシュ値を生成して使用可能になります。
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
、
<code>
Hashable
</code>
プロトコルは Swift において非常に便利であり、特にデータモデルを定義する際によく使用されます。これら3つのプロトコルを一緒に使用することで、
<b>
UI でのデータ管理
</b>
、
<b>
API 通信
</b>
、
<b>
コレクション内での高速なデータ検索
</b>
など、様々な要件を効率的に処理できます。今回の投稿で紹介したユーザーモデルの例を通じて、Swift でプロトコルを活用する方法をより深く理解していただけたなら幸いです。
</span>
</p>