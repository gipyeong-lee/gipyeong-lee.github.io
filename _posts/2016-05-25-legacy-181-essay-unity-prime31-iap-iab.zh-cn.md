---
layout: post
title: "[Unity] 使用 Prime31 IAP, IAB"
description: "您好？这次我使用了 Unity 框架之一的 Prime31 来添加应用内购买相关功能。Prime31 分别有 StoreKit 和 Google IAB 两个管理器。通过 #if UNITY_IOS || UNITY_IPHONE #elif 等方式..."
date: 2016-05-25 16:46:55 +0900
section: blog
category: essay
lang: zh-cn
ref: 2016-05-25-legacy-181-essay-unity-prime31-iap-iab
tags:
  - "经验谈"
  - "essay"
translation_source_hash: 496b6373404ac32d83663a681453ea1fc9b6c54a74bf667a1612847d91f2a6c3
---

<p>
您好？
</p>

<p>
这次我使用了 Unity 框架之一的 Prime31 来添加应用内购买相关功能。
</p>


<p>
Prime31 分别有 StoreKit 和 Google IAB 两个管理器。
</p>

<p>
我们通过
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
构建了一个统一的管理器，通过签发相同的商品密钥来控制相关商品的购买。
</p>


<p>
顺序如下。
</p>

<p>
1. 导入 Prime31 ( Android : ver. 2.10 , iOS : ver 2.15 )
</p>
<p>
Prime31 的 iPhone 和 Android 插件版本有所不同。
</p>

<p>
2. 测试 IAP
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
简单解释一下代码。
</p>

<p>
listProducts 是在 iTunes 中注册的产品 ID。执行 requestProductData 后，系统会检查并确认这些产品是否存在。
</p>

<p>
在 ProductListReceived 回调中设置数据即可。
</p>

<p>
Purchase 函数部分已将 IAB 和 IAP 统一。
</p>



<p>
3. 测试 IAB
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
4. 新建类 IAPManager -&gt; 包含 "GoogleIAB" , "StoreKitManager"
</p>

<p>
利用以下指令进行了分支处理。
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
之后，purchase 部分使用通用代码进行了处理。
</p>
<p>
如果 Android 和 iOS 的产品 ID 一致，管理起来会很方便。
</p>
<p>
product_id 建议不要创建太多，按种类（级别）创建几个即可，然后在自己的数据库中复用。
</p>


<p>
5. 实现收据验证服务器
</p>

<p>
使用了 PHP 进行处理。iOS 的情况只需接收 transaction id 即可验证，而 Google 的情况必须使用 API，因此需要 client-id、secret-key 和 token。（准备工作较多，且需要一定时间。）
</p>

<p>
6. 结论
</p>

<p>
如果说在进行过程中耗时最长的部分：
</p>


<p>
Error
</p>

<p>
The item you requested is not available for purchase
</p>

<p>
这是一个报错。
</p>

<p>
查看 queryInventorySucceededEvent，我注册的商品列表都能正常获取，看来应用和开发者控制台（Developer Console）之间的连接是正常的。但该错误一直出现。
</p>

<p>
为了解决这个问题，我尝试了以下应对措施：
</p>


<p>
1. 检查 APK 的 version code 和 version name（Manifest 内的 version code 和 version name 必须一致）。
</p>
<p>
2. 权限设置（Permission Setting）。
</p>

<p>
最终解决了问题。
</p>

<p>
首先，为了判断测试失败的原因，必须确保可以通过链接下载。如果点击链接时出现 404 not found，说明还没准备好。（此时似乎还不是 enable 状态）。我的情况是链接激活后一切正常。链接激活大约花了一天时间。
</p>