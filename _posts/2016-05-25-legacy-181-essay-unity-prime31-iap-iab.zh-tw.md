---
layout: post
title: "[Unity] 使用 Prime31 IAP, IAB"
description: "您好？這次要透過 Unity 的框架之一 Prime31 來串接應用程式內購買（In-App Purchase）功能。Prime31 擁有 StoreKit 和 Google IAB 兩個管理員，分別透過 #if UNITY_IOS || UNITY_IPHONE #elif... 進行處理。"
date: 2016-05-25 16:46:55 +0900
section: blog
category: essay
lang: zh-tw
ref: 2016-05-25-legacy-181-essay-unity-prime31-iap-iab
tags:
  - "心得"
  - "essay"
translation_source_hash: 496b6373404ac32d83663a681453ea1fc9b6c54a74bf667a1612847d91f2a6c3
---

<p>
您好？
</p>

<p>
這次要透過 Unity 的框架之一 Prime31 來串接應用程式內購買（In-App Purchase）功能。
</p>


<p>
Prime31 擁有 StoreKit 和 Google IAB 兩個管理員。
</p>

<p>
我們分別使用
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
來建構整合管理員，並發行相同的產品金鑰（Product Key）來控制相關商品的購買。
</p>


<p>
步驟如下：
</p>

<p>
1. 匯入 Prime31（Android：ver. 2.10，iOS：ver 2.15）
</p>
<p>
Prime 31 的 iPhone 與 Android 外掛版本不同。
</p>

<p>
2. 測試 IAP（iOS）
</p>

<pre class="brush:c#">
var listProducts = new string[2];
listProducts[0] = "com.test.crystal100";
listProducts[1] = "com.test.crystal200";
StoreKitManager.productListReceivedEvent += ProductListReceived;
//監聽購買事件
StoreKitManager.purchaseSuccessfulEvent += PurchaseSuccessful;
StoreKitManager.purchaseFailedEvent += PurchaseFail;
StoreKitManager.purchaseCancelledEvent += PurchaseCancelled;
//請求產品列表
StoreKitBinding.requestProductData(listProducts);
</pre>

<p>
簡單說明程式碼：
</p>

<p>
listProducts 是在 iTunes 註冊的產品 ID。對該部分執行 requestProductData 時，會進行檢查以確認該產品是否存在。
</p>

<p>
您可以在 ProductListReceived 回呼（Callback）中設定資料。
</p>

<p>
Purchase 函式部分已統一處理 IAB 與 IAP。
</p>



<p>
3. 測試 IAB（Android）
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
4. 新增類別 IAPManager -&gt; 包含 "GoogleIAB", "StoreKitManager"
</p>

<p>
使用以下指令進行分歧處理：
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
之後的購買部分則採用共用程式碼處理。
</p>
<p>
將 Android 與 iOS 的產品 ID 設定一致會比較方便管理。
</p>
<p>
product_id 建議不要建立太多，依種類（分等級）建立幾個即可，並在自有的資料庫中靈活運用。
</p>


<p>
5. 實作收據驗證伺服器
</p>

<p>
採用 PHP 處理。iOS 的情況下，僅需取得 transaction id 即可驗證；而 Google 方面則必須使用 API，因此需要 client-id、secret-key 及 token。（需要準備的東西較多，也較花時間。）
</p>

<p>
6. 結論
</p>

<p>
如果說在開發過程中耗時最長的部分，那就是：
</p>


<p>
Error
</p>

<p>
The item you requested is not available for purchase
</p>

<p>
這個錯誤訊息。
</p>

<p>
從 queryInventorySucceededEvent 內可以順利接收到我註冊的商品列表來看，應用程式與 Developer Console 之間的連接應該是正常的。但是，該錯誤仍然一直出現。
</p>

<p>
為了解決這個問題，我採取了以下對策：
</p>


<p>
1. 檢查 APK 的 version code 與 version name（清單中的 version code 與 version name 必須一致）。
</p>
<p>
2. 檢查權限設定（Permission Setting）。
</p>

<p>
最終我解決了。
</p>

<p>
首先，為了判斷測試是否可行，必須先確認是否能透過連結下載。若點擊連結出現 404 not found，代表尚未啟用（此時似乎還沒生效）。就我而言，連結啟用後就能正常運作了。連結啟用大約花了一天的時間。
</p>