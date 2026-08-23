---
layout: post
title: "[Unity] Prime31 IAP, IABの実装"
description: "こんにちは。今回はUnityのフレームワークの一つであるPrime31を使用して、アプリ内課金機能を実装してみました。Prime31にはStoreKitとGoogle IABの2つのマネージャーが存在します。それぞれ#if UNITY_IOS || UNITY_IPHONE #elif...を使用して統合マネージャーを構築し、共通のプロダクトキーで商品購入を制御する方式をとりました。"
date: 2016-05-25 16:46:55 +0900
section: blog
category: essay
lang: ja
ref: 2016-05-25-legacy-181-essay-unity-prime31-iap-iab
tags:
  - "体験談"
  - "essay"
translation_source_hash: 496b6373404ac32d83663a681453ea1fc9b6c54a74bf667a1612847d91f2a6c3
---

<p>
こんにちは。
</p>

<p>
今回はUnityのフレームワークの一つであるPrime31を使用して、アプリ内課金機能を実装してみました。
</p>


<p>
Prime31にはStoreKitとGoogle IABの2つのマネージャーが存在します。
</p>

<p>
それぞれ
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
を利用して統合マネージャーを構築した後、同じプロダクトキーを発行して関連商品の購入を制御する方式で進めました。
</p>


<p>
手順は以下の通りです。
</p>

<p>
1. Import Prime31 ( android : ver. 2.10 , ios : ver 2.15 )
</p>
<p>
Prime31の場合、iPhoneとAndroidのプラグインバージョンが異なりました。
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
ソースを簡単に説明すると、
</p>

<p>
listProductsはiTunesで登録した製品IDです。該当部分をrequestProductDataすると、チェックを行い、存在するプロダクトかどうかを確認してくれます。
</p>

<p>
ProductListReceivedコールバックでデータをセットすれば完了です。
</p>

<p>
Purchase関数の場合は、IABとIAPを統一しました。
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
以下のディレクティブを利用して分岐処理を行いました。
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
その後、purchase部分については共通コードで処理しました。
</p>
<p>
AndroidとiOSのプロダクトIDを合わせると管理が楽になります。
</p>
<p>
product_idはあまり多く作らず、種類別（ティア別）にいくつかだけ作成して、独自のデータベースで使い回すのがおすすめです。
</p>


<p>
5. 領収書チェックサーバーの実装
</p>

<p>
PHPを利用して処理しました。iOSの場合はtransaction IDだけ受け取ればバリデーションが可能ですが、Googleの場合はAPIを使用する必要があるため、client-id、secret-key、tokenが必要です。（準備することが多く、少し時間がかかります。）
</p>

<p>
5. 結論
</p>

<p>
進める中で最も時間がかかった部分があるとすれば、
</p>


<p>
Error
</p>

<p>
The item you requested is not available for purchase
</p>

<p>
というエラーです。
</p>

<p>
queryInventorySucceededEvent内に登録した商品リストは正常に入ってくることから、アプリとDeveloper Console間の接続はうまくいっているようです。しかし、該当エラーがずっと表示されていました。
</p>

<p>
これを解決するために、次のような対処を試みました。
</p>


<p>
1. APKのversion code、version nameのチェック（manifest内のversion code、version nameが一致している必要があります。）
</p>
<p>
2. パーミッション設定。
</p>

<p>
結局、解決しました。
</p>

<p>
まずテストしてうまくいかない原因を判断するためには、先にリンクを通じてダウンロードが可能でなければなりません。これはリンクを押したときに404 not foundが表示されてはいけません。（この場合はまだenable状態ではないようです。）私の場合、リンクが有効化されてからはうまく動作しました。リンクの有効化には1日程度かかりました。
</p>