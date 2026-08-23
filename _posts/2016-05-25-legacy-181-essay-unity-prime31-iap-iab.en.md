---
layout: post
title: "[Unity] Using Prime31 IAP, IAB"
description: "Hello? Today, I will look into implementing in-app related features using Prime31, one of Unity's frameworks. Prime31 has two managers: StoreKit and Google IAB. Each uses #if UNITY_IOS || UNITY_IPHONE #elif... to build a unified manager, allowing control of relevant product purchases by issuing identical product keys."
date: 2016-05-25 16:46:55 +0900
section: blog
category: essay
lang: en
ref: 2016-05-25-legacy-181-essay-unity-prime31-iap-iab
tags:
  - "Experience"
  - "essay"
translation_source_hash: 496b6373404ac32d83663a681453ea1fc9b6c54a74bf667a1612847d91f2a6c3
---

<p>
Hello.
</p>

<p>
Today, I implemented in-app related features using Prime31, one of Unity's frameworks.
</p>


<p>
Prime31 provides two separate managers: StoreKit and Google IAB.
</p>

<p>
I proceeded by building a unified manager using:
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
This approach allowed me to control purchases by issuing identical product keys for both platforms.
</p>


<p>
The order of operations is as follows:
</p>

<p>
1. Import Prime31 (Android: ver. 2.10, iOS: ver. 2.15)
</p>
<p>
For Prime31, the plugin versions for iPhone and Android were different.
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
To briefly explain the code:
</p>

<p>
`listProducts` contains the product IDs registered in iTunes. When you call `requestProductData` with these, it checks whether the products exist.
</p>

<p>
You should set the data in the `ProductListReceived` callback.
</p>

<p>
For the `Purchase` function, I unified the implementation for both IAB and IAP.
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
4. New Class `IAPManager` -> include "GoogleIAB", "StoreKitManager"
</p>

<p>
I used the following directives to handle platform branching:
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
After that, the purchase logic was handled with common code.
</p>
<p>
It is easier to manage if you match the product IDs between Android and iOS.
</p>
<p>
Don't create too many `product_id`s; instead, create a few by type (tier) and reuse them within your own database.
</p>


<p>
5. Receipt Verification Server Implementation
</p>

<p>
I used PHP for this. While validation is possible for iOS by receiving only the transaction ID, Google requires the use of their API, which necessitates a client-id, secret-key, and token. (There is a lot to prepare, and it takes some time.)
</p>

<p>
6. Conclusion
</p>

<p>
If there was one part that took the longest while proceeding:
</p>


<p>
Error:
</p>

<p>
"The item you requested is not available for purchase"
</p>

<p>
This was the error.
</p>

<p>
Since the product list I registered was coming in correctly within the `queryInventorySucceededEvent`, the connection between the app and the developer console seemed fine. However, this error kept appearing.
</p>

<p>
To resolve this, I took the following actions:
</p>


<p>
1. Checked APK version code and version name (Version code and version name within the manifest must match.)
</p>
<p>
2. Permission Setting.
</p>

<p>
I eventually solved it.
</p>

<p>
To determine if testing is not working, first, you must be able to download it via the link. This means you should not see "404 not found" when clicking the link. (In that case, it seems it is not yet in an enabled state.) In my case, it worked well after the link was activated. It took about a day for the link to be activated.
</p>