---
layout: post
title: "Kubernetes - 10. 高可用性與擴展性設計"
description: "https://medium.com/@kumarshivam_66534/a-walk-through-on-iaas-paas-and-saas-7e8a4e4793fb 本章第 10 節涵蓋內容如下： - 高可用性介紹 - 高可用性最佳實踐 - 多區域設置 - 安全最佳實踐..."
date: 2020-10-23 11:27:53 +0900
section: blog
category: engineering
lang: zh-tw
ref: 2020-10-23-legacy-250-engineering-kubernetes-10
tags:
  - "HA"
  - "高可用性"
  - "kubernetes"
  - "Kubernetes"
  - "engineering"
translation_source_hash: 09bcdc5d9a185b58bea7f7e5864c0b6de3ed3db8a714869ebdb501e3338e3af2
---

<p>
<figure class="imageblock alignCenter">

<figcaption>
https://medium.com/@kumarshivam_66534/a-walk-through-on-iaas-paas-and-saas-7e8a4e4793fb
</figcaption>
</figure>
</p>
<p>
本章第 10 節涵蓋內容如下：
</p>
<blockquote>
- 高可用性介紹
<br>
- 高可用性最佳實踐
<br>
- 多區域設置
<br>
- 安全最佳實踐
<br>
- 託管 Kubernetes PaaS 的高可用性設置
<br>
- 集群生命週期事件
<br>
- 准入控制器（Admission Controller）使用方法
<br>
- 工作負載 API 介紹
<br>
- 什麼是自定義資源定義（CRD）？
</blockquote>

<blockquote>
高可用性 (High Availability)
</blockquote>
<p>
在業界，高可用性意味著極高水準的可用性，通常稱為「五個九」的可用性（99.999%）。
</p>
<p>
基本上，可用性計算方式如下：
</p>
<blockquote>
可用性（百分比） = (正常運行時間 / (正常運行時間 + 停機時間)) x 100
</blockquote>
<p>
正常運行時間的可用性公式如下：
</p>
<blockquote>
MTBF（平均故障間隔時間） = 將 1 年換算為小時 / 1 年內的故障次數
<br>
MTTR（平均修復時間） = (故障次數 x 系統修復時間) / 總故障次數
<br>
正常運行時間可用性 = MTBF / (MTTR + MTBF)
<br>
年均停機時間 (每小時) = (1 - 正常運行時間比率) x 365 x 24
</blockquote>
<p>
SLA（服務等級協議）保證的可用性水準如下：
</p>
<p>
1. 當可用性為 99.9% 時，年均停機時間為：8 小時 45 分 57.0 秒。
</p>
<p>
2. 當可用性為 99.99% 時，年均停機時間為：52 分 35.7 秒。
</p>
<p>
3. 當可用性為 99.999% 時，年均停機時間為：5 分 15.6 秒。
</p>

<p>
若要保證「五個九」的可用性，必須極為嚴謹地運營 Kubernetes 集群。
</p>

<blockquote>
HA 最佳實踐
</blockquote>
<p>
若要構建保證高可用性的 Kubernetes 系統，請記住：「可用性往往不僅是技術錯誤問題，更是人與流程的問題。」
</p>
<p>
首先需了解一個術語：<b>優雅降級（Graceful Degradation）</b>的概念。
</p>
<p>
優雅降級是透過將功能分散到多個層級與模組來構建系統的概念。即使系統的部分組件發生致命錯誤，仍能持續提供一定水準的可用性。
</p>
<p>
Kubernetes 有兩種優雅降級的方法：
</p>
<blockquote>
<b>
基礎設施降級
</b>
：此方式依賴複雜的演算法與軟體來處理硬體或虛擬機（VM）的意外錯誤。我們將探討如何確保提供此種降級方式所需的 Kubernetes 必要組件之高可用性。
<br>
<br>
<b>
應用程式降級
</b>
：儘管很大程度上取決於前述的微服務（MS）最佳實踐策略，但仍有幾種模式可確保用戶體驗。
</blockquote>
<p>
應使用核心 Kubernetes 策略來隔離基礎設施故障，同時構建針對應用程式故障的快取、容錯轉移（Failover）及回滾機制，並確保 Kubernetes 組件本身的高可用性。
</p>

<blockquote>
反脆弱性 (Antifragility)
</blockquote>
<p>
<span>
「反脆弱性」簡單來說，是指在外部混亂或壓力下，績效反而能提升的性質。
</span>
</p>
<p>
<span>
若要應對 Kubernetes 系統的複雜性，並利用龐大的 Kubernetes 來維持系統穩定，需了解幾個核心概念：
</span>
</p>
<blockquote>
1. 冗餘（Redundancy）
<br>
2. 觸發故障場景後進行應對、分析、探討與改進。（Netflix Chaos Monkey 是測試複雜系統穩定性的標準且完善的方法： https://github.com/Netflix/chaosmonkey ）
<br>
3. 在系統中導入適當的模式。（重試、負載平衡、斷路器、逾時、健康檢查、併發連接檢查是實現反脆弱性的核心模式。更高層級還有如 Istio 等服務網格： https://techcafe.tistory.com/133 ）
</blockquote>

<blockquote>
Kubernetes 的 HA 方法
</blockquote>
<p>
Kubernetes 的 HA 配置方式有兩種：結合 etcd 與管理節點的 Stacked Master 方式，以及將 etcd 與管理節點分離的方式。
</p>
<p>
此處省略 Kubernetes 安裝步驟。
</p>

<blockquote>
集群生命週期
</blockquote>
<p>
讓我們來看看如何使用准入控制器、工作負載與 CRD 來擴展集群。
</p>

<p>
<b>
准入控制器 (Admission Controller)
</b>
</p>
<p>
准入控制器可在 Kubernetes API 伺服器的認證與授權完成後，攔截對 API 伺服器的呼叫。
</p>
<p>
以下兩個准入控制器特別重要：
</p>
<blockquote>
<b>
MutatingAdmissionWebhook
</b>
：僅在集群處於變更階段時執行，並呼叫會連續變更請求的 Webhook。當您需要自定義 CREATE、DELETE、UPDATE 等操作的核准邏輯以將業務邏輯納入集群時，請使用此控制器。例如，可以使用 StorageClass 自動化儲存配置。
<br>
<br>
<b>
ValidatingAdmissionWebhook
</b>
：在核准階段由准入控制器執行。它會呼叫驗證「請求有效性」的 Webhook，例如驗證配額增加的 Webhook。請注意，此控制器呼叫的所有 Webhook 都無法變更原始物件。
</blockquote>

<blockquote>
工作負載 API
</blockquote>
<p>
在 Kubernetes 初期，Pod 與工作負載與共用 CPU、網路、儲存與生命週期事件的容器緊密耦合。為了管理雲端應用程式的 12 要素（12-Factor App），Kubernetes 引入了副本（Replication）、部署（Deployment）、標籤（Label）等概念，並為了讓運營者處理具狀態工作負載，引入了 StatefulSet。
</p>
<p>
隨著時間推移，Kubernetes 工作負載概念分為多種：
</p>
<blockquote>
Pod
<br>
ReplicationController
<br>
ReplicaSet
<br>
Deployment
<br>
DaemonSet
<br>
StatefulSet
</blockquote>
<p>
這些多樣的要素是 Kubernetes 合理調整工作負載類型的結果，但不幸的是 API 被分散到了 Kubernetes 程式碼庫的多個地方。為了克服此問題，經過數個月努力（甚至部分放棄向後兼容性），終於將所有程式碼統一到了 `apps/v1` API。
</p>
<p>
統一過程中有幾項重要決策如下：
</p>
<blockquote>
<b>
默認選擇器（Default Selectors）
</b>
：若未指定標籤選擇器，則默認使用從模板標籤中提取並自動生成的選擇器。
<br>
<b>
不可變選擇器（Immutable Selectors）
</b>
：雖然變更選擇器對部署有時是有用的，但變更選擇器與 Kubernetes 的建議相違背，因此已改為 Kubernetes 編排的金絲雀（Canary）部署方式，即透過更換 Pod 標籤來實現。
<br>
<b>
滾動更新（Rolling Updates）
</b>
：應 Kubernetes 開發者要求，滾動更新已成為默認配置。
<br>
垃圾回收（Garbage Collection）：在 1.9 版本與 `apps/v1` 版本中，垃圾回收更具侵略性。刪除 DaemonSet、ReplicaSet、StatefulSet 或 Deployment 時，其對應的 Pod 也會被刪除。
</blockquote>

<blockquote>
自定義資源定義 (CRD)
</blockquote>
<p>
自定義資源（Custom Resource）擴展了 Kubernetes API，補充了准入控制器。您可以利用自定義資源來改善正在運行的 Kubernetes 集群。
</p>
<p>
可以應用以下功能：
</p>

<table>
<tbody>
<tr>
<td>
CRUD
</td>
<td>
新的端點透過 HTTP 與 kubectl 支援基本的 CRUD 操作。
</td>
</tr>
<tr>
<td>
Watch
</td>
<td>
新的端點透過 HTTP 支援 Kubernetes Watch 操作。
</td>
</tr>
<tr>
<td>
Discovery
</td>
<td>
如 kubectl 與 Dashboard 等用戶端會自動提供您資源的列表、顯示與欄位編輯操作。
</td>
</tr>
<tr>
<td>
json-patch
</td>
<td>
新的端點支援 Content-Type: application/json-patch+json 的 PATCH 操作。
</td>
</tr>
<tr>
<td>
merge-patch
</td>
<td>
新的端點支援 Content-Type: application/merge-patch+json 的 PATCH 操作。
</td>
</tr>
<tr>
<td>
HTTPS
</td>
<td>
新的端點使用 HTTPS。
</td>
</tr>
<tr>
<td>
內建認證
</td>
<td>
對擴展的存取使用核心 API 伺服器（聚合層）進行認證。
</td>
</tr>
<tr>
<td>
內建授權
</td>
<td>
對擴展的存取可重複使用核心 API 伺服器所使用的授權機制，例如 RBAC。
</td>
</tr>
<tr>
<td>
Finalizers
</td>
<td>
在外部清理完成前，封鎖擴展資源的刪除。
</td>
</tr>
<tr>
<td>
准入 Webhooks
</td>
<td>
在任何建立/更新/刪除操作期間，設定默認值並驗證擴展資源。
</td>
</tr>
<tr>
<td>
UI/CLI 顯示
</td>
<td>
Kubectl 與 Dashboard 可以顯示擴展資源。
</td>
</tr>
<tr>
<td>
未設定與空值
</td>
<td>
用戶端可以區分「未設定的欄位」與「零值欄位」。
</td>
</tr>
<tr>
<td>
生成客戶端程式庫
</td>
<td>
Kubernetes 提供通用客戶端程式庫，以及生成特定類型客戶端程式庫的工具。
</td>
</tr>
<tr>
<td>
標籤與註釋
</td>
<td>
物件間通用的元數據（Metadata），工具已知如何編輯核心資源與自定義資源。
</td>
</tr>
</tbody>
</table>

## 參考資料