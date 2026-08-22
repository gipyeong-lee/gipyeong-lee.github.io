---
layout: post
title: "[SwiftUI] Combine을 이용한 실시간 데이터 구독 및 업데이트"
description: "SwiftUI와 Combine은 iOS 앱 개발에서 비동기 데이터 처리를 매우 간단하고 효율적으로 만들어줍니다. 특히, @Published와 Combine의 구독 기능을 활용하면 데이터가 실시간으로 업데이트될 때마다 뷰를 자동으로 새로고침할 수 있습니다. 이번 포스트에서는 Prof..."
date: 2024-09-22 01:43:29 +0900
section: blog
category: engineering
lang: ko
ref: 2024-09-22-legacy-346-engineering-swiftui-combine
tags:
  - "Combine"
  - "SwiftUI"
  - "@Published"
  - "ObservableObject"
  - "swift"
  - "Apple Ecosystem Insights"
---

<blockquote>
<span>
SwiftUI와 Combine은 iOS 앱 개발에서 비동기 데이터 처리를 매우 간단하고 효율적으로 만들어줍니다. 특히, @Published와 Combine의 구독 기능을 활용하면 데이터가 실시간으로 업데이트될 때마다 뷰를 자동으로 새로고침할 수 있습니다. 이번 포스트에서는 ProfileViewModel 예제를 통해 SwiftUI에서 Combine을 활용하여 실시간으로 데이터를 업데이트하고, 이를 효율적으로 관리하는 방법을 소개하겠습니다.
</span>
</blockquote>
<h3>
<span>
코드 예시:
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
이 코드는 사용자의 프로필 데이터를 실시간으로 업데이트하여 SwiftUI 뷰에 반영하는
<code>
ProfileViewModel
</code>
을 정의합니다. Combine을 활용한 데이터 구독과
<code>
@Published
</code>
프로퍼티를 사용하여 SwiftUI와의 상태 연동을 간편하게 설정할 수 있습니다.
</span>
</p>
<h3>
<span>
코드 분석
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
은
<code>
ObservableObject
</code>
프로토콜을 채택하고 있습니다. 이를 통해
<b>
ViewModel
</b>
이 SwiftUI 뷰에 데이터를 제공하고, 데이터가 변경될 때 뷰가 자동으로 업데이트될 수 있도록 만듭니다.
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
속성 래퍼는
<code>
currentUser
</code>
가 업데이트될 때마다
<b>
SwiftUI
</b>
가 해당 변경 사항을 감지하고 뷰를 다시 렌더링하게 합니다. 이는 데이터 흐름을
<b>
반응형
</b>
으로 관리할 수 있도록 해주며, 사용자 정보가 변경될 때 뷰에 즉시 반영됩니다.
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
Combine을 통해 데이터를 구독할 때, 구독을 취소할 수 있는 객체인
<code>
AnyCancellable
</code>
을 저장하는 컬렉션입니다. Swift에서 메모리 누수를 방지하고 구독을 필요에 따라 해제하기 위해
<b>
Cancellable
</b>
을 관리하는 것이 중요합니다.
</span>
</p>
<h4>
<span>
4.
<code>
init()
</code>
과
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
메서드는
<code>
ProfileViewModel
</code>
객체가 생성될 때 호출되며,
<code>
setupSubscribers()
</code>
메서드를 통해 Combine 구독 설정을 초기화합니다.
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
이 부분은
<b>
Combine
</b>
의 핵심입니다.
<code>
UserService
</code>
의
<code>
@Published
</code>
로 선언된
<code>
currentUser
</code>
를 구독(subscribe)하여 데이터가 변경될 때마다 클로저가 실행됩니다.
<code>
[weak self]
</code>
는 순환 참조를 방지하기 위해 사용되며,
<code>
self
</code>
를 약한 참조로 가져와 메모리 관리에 신경 씁니다.
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
데이터 스트림에서 전달된
<code>
user
</code>
객체를 뷰모델의
<code>
currentUser
</code>
에 할당합니다. 이로 인해
<b>
SwiftUI 뷰는 변경된 데이터를 감지
</b>
하고, 해당 뷰가 새롭게 렌더링됩니다.
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
디버깅을 위해 Combine을 통해 전달된 데이터를 출력하는 코드입니다. 이 코드는 실시간 데이터 흐름을 확인할 때 유용하게 사용할 수 있습니다.
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
구독을 완료한 후
<b>
cancellables
</b>
에 저장하여
<b>
메모리 누수 방지
</b>
및 구독 관리가 가능하게 만듭니다. 이 메서드는 Combine 구독이 필요 없어질 때 메모리에서 자동으로 해제되도록 보장해 줍니다.
</span>
</p>
<hr>
<h3>
<b>
<span>
왜 이 코드가 필요한가?
</span>
</b>
</h3>
<ol>
<li>
<span>
<b>
실시간 데이터 반영
</b>
: 앱 내에서 사용자 정보가 변경되었을 때, 이를 실시간으로 반영해야 할 때 매우 유용합니다. 예를 들어, 사용자가 로그인하거나 로그아웃할 때 해당 정보를 뷰모델에서 자동으로 업데이트할 수 있습니다.
</span>
</li>
<li>
<span>
<b>
메모리 관리
</b>
: 구독이 끝났을 때 메모리를 효율적으로 관리하기 위해서는 구독을 해제할 수 있어야 합니다. Combine의
<code>
AnyCancellable
</code>
을 사용하면 불필요한 구독을 해제할 수 있어 메모리 누수를 방지할 수 있습니다.
</span>
</li>
<li>
<span>
<b>
반응형 앱 설계
</b>
: SwiftUI의 강점 중 하나는 데이터와 뷰 간의
<b>
반응형 흐름
</b>
입니다. Combine을 사용하면 데이터가 변할 때마다 뷰가 자동으로 변경되므로, 사용자는 자연스럽고 실시간으로 업데이트되는 UI를 경험할 수 있습니다.
</span>
</li>
</ol>
<hr>
<h3>
<span>
결론
</span>
</h3>
<p>
<span>
Combine을 사용하면 데이터 흐름을 간단하게 구독하고, 실시간으로 상태가 변경될 때 뷰를 쉽게 업데이트할 수 있습니다. SwiftUI와 결합된 이러한 메커니즘은 현대 iOS 앱 개발에서 매우 강력한 도구가 될 수 있습니다. 특히,
<code>
@Published
</code>
와 Combine의 구독 패턴은 데이터 흐름을 효율적으로 관리하고, 메모리 관리까지 신경 쓰는 앱 개발에 필수적입니다.
</span>
</p>
