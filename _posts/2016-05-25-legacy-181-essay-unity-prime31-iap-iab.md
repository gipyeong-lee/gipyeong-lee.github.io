---
layout: post
title: "[Unity] Prime31 IAP,IAB 사용하기"
description: "안녕하세요? 이번시간에는 unity 의 프레임웍중 하나인 prime31 을 이용해서 인앱 관련 기능을 붙여보았습니다. prime31 의 경우 storeKit 과 google iab 두개의 매니저가 존재합니다. 각각은 #if UNITY_IOS || UNITY_IPHONE #elif..."
date: 2016-05-25 16:46:55 +0900
section: blog
category: essay
lang: ko
ref: 2016-05-25-legacy-181-essay-unity-prime31-iap-iab
tags:
  - "경험담"
  - "essay"
---

<p>
안녕하세요?
</p>

<p>
이번시간에는 unity 의 프레임웍중 하나인 prime31 을 이용해서 인앱 관련 기능을 붙여보았습니다.
</p>


<p>
prime31 의 경우 storeKit 과 google iab 두개의 매니저가 존재합니다.
</p>

<p>
각각은
</p>

<p>
#if UNITY_IOS || UNITY_IPHONE
</p>
<p>
#elif UNITY_ANDROID
</p>
<p>
#endif
</p>

<p>
를 이용하여 통합 매니저를 구축한 후 동일한 프로덕트키를 발급하여 관련 상품구매를 컨트롤 하는 방식으로 진행하였습니다.
</p>


<p>
순서는 아래와 같습니다.
</p>

<p>
1. Import Prime31 ( android : ver. 2.10 , ios : ver 2.15 )
</p>
<p>
prime 31 의 경우 아이폰과 안드로이드의 plugin 버전이 달랐습니다.
</p>

<p>
2. Test IAP
</p>

<pre class="brush:c#">
var listProducts = new string[2];
listProducts[0] = "com.test.crystal100";
listProducts[1] = "com.test.crystal200";
StoreKitManager.productListReceivedEvent += ProductListReceived;
//listen for purchase
StoreKitManager.purchaseSuccessfulEvent += PurchaseSuccessful;
StoreKitManager.purchaseFailedEvent += PurchaseFail;
StoreKitManager.purchaseCancelledEvent += PurchaseCancelled;
//Request product list
StoreKitBinding.requestProductData(listProducts);
</pre>

<p>
소스를 간단히 설명 드리면
</p>

<p>
listProducts 의 경우 itunes 에서 등록한 제품ID 입니다. 해당 부분을 requestProductData 를 하시게 되면 체크를하여 존재하는 프로덕트인지 확인해줍니다.
</p>

<p>
ProductListReceived 콜백에서 데이터를 셋해주시면 됩니다.
</p>

<p>
Purchase 함수의 경우 IAB,IAP 통일을 하였습니다.
</p>



<p>
3. Test IAB
</p>


<pre class="brush:c#">
<p>
GoogleIAB.init( key );
GoogleIAB.setAutoVerifySignatures (true);

GoogleIABManager.billingSupportedEvent += billingSupportedEvent;
GoogleIABManager.billingNotSupportedEvent += billingNotSupportedEvent;
GoogleIABManager.queryInventorySucceededEvent += queryInventorySucceededEvent;
GoogleIABManager.queryInventoryFailedEvent += queryInventoryFailedEvent;
GoogleIABManager.purchaseCompleteAwaitingVerificationEvent += purchaseCompleteAwaitingVerificationEvent;
GoogleIABManager.purchaseSucceededEvent += purchaseSucceededEvent;
GoogleIABManager.purchaseFailedEvent += purchaseFailedEvent;
GoogleIABManager.consumePurchaseSucceededEvent += consumePurchaseSucceededEvent;
GoogleIABManager.consumePurchaseFailedEvent += consumePurchaseFailedEvent;
</p>
</pre>



<p>
4. New Class IAPManager -&gt; include "GoogleIAB" , "StoreKitManager"
</p>

<p>
다음의 지시문을 이용해 분기처리 하였습니다.
</p>

<p>
#if UNITY_IOS
</p>
<p>
#elif UNITY_ANDROID
</p>
<p>
#endif
</p>


<p>
이후 purchase 부분에 대해서는 공통코드로 처리를 하였습니다.
</p>
<p>
Android 와 ios 의 프로덕트 id 를 맞추면 관리하기가 편합니다.
</p>
<p>
product_id 의 경우 많이 만들지 마시고 종류별로 (티어별로 몇개만 만드셔서 , 자체 디비에서 돌려 쓰시면 좋습니다. )
</p>


<p>
5. 영수증 체크 서버 구현
</p>

<p>
php 를 이용하여 처리하였습니다. ios 의 경우에는 transaction id 만 받아서 validation 이 가능한 반면, 구글의 경우  api 를 사용해야하므로,  client-id, secret-key, token 이 필요합니다. ( 준비해야할게 많고 시간이 좀 걸립니다. )
</p>

<p>
5. 결론
</p>

<p>
진행하면서 가장 시간이 오래걸렸던 부분이 있다면.
</p>


<p>
Error
</p>

<p>
The item you requested is not available for purchase
</p>

<p>
라는 에러입니다.
</p>

<p>
queryInventorySucceededEvent 내로 제가 등록한 상품리스트는 잘 들어오는 것으로 보아, 앱과 developer console 간의 연결은 잘 된것 같습니다. 그러나, 해당 에러가 계속 뜨게되었습니다.
</p>

<p>
이를 해결하기 위해 다음과 같은 대처를 해보았습니다.
</p>


<p>
1. APK 의 version code, version name 체크 ( manifest 내의 version code, version name 이 일치 해야합니다. )
</p>
<p>
2. Permission Setting .
</p>

<p>
결국 해결 하였습니다.
</p>

<p>
우선 테스트해서 안되는지를 판단하기 위해서는 먼저 링크를 통해서 다운로드가 가능해야합니다. 이는 링크를 눌렀을때  404 not found 가 뜨면 안됩니다. ( 이때는 아직 enable 상태가 아닌것 같습니다. ) 저의 경우 링크가 활성화 된 후부터 잘 되었습니다. 링크 활성화는 시간이 하루정도 걸렸습니다.
</p>
