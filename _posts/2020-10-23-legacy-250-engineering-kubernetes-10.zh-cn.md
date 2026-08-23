---
layout: post
title: "Kubernetes - 10. 高可用性与可扩展性设计"
description: "https://medium.com/@kumarshivam_66534/a-walk-through-on-iaas-paas-and-saas-7e8a4e4793fb 本章主要内容如下： - 高可用性介绍 - 高可用性最佳实践 - 多区域设置 - 安全最佳实践..."
date: 2020-10-23 11:27:53 +0900
section: blog
category: engineering
lang: zh-cn
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
本章主要内容如下：
</p>
<blockquote>
- 高可用性介绍
<br>
- 高可用性最佳实践
<br>
- 多区域设置
<br>
- 安全最佳实践
<br>
- 托管 Kubernetes PaaS 的高可用性设置
<br>
- 集群生命周期事件
<br>
- 准入控制器使用方法
<br>
- 工作负载 API 介绍
<br>
- 什么是自定义资源定义 (CRD)？
</blockquote>

<blockquote>
高可用性
</blockquote>
<p>
在业界，高可用性意味着极高水平的可用性，通常被称为“五个九”（99.999%）。
</p>
<p>
通常，可用性计算如下：
</p>
<blockquote>
可用性（百分比） = (正常运行时间 / (正常运行时间 + 故障停机时间)) x 100
</blockquote>
<p>
正常运行时间的可用性公式如下：
</p>
<blockquote>
MTBF (平均故障间隔时间) = 1年换算成小时数 / 1年内的故障次数
<br>
MTTR (平均故障修复时间) = (故障总次数 x 系统修复时间) / 总故障次数
<br>
正常运行时间可用性 = MTBF / (MTTR + MTBF)
<br>
年度停机时间 (per hour) = (1 - 正常运行时间比率) x 365 x 24
</blockquote>
<p>
SLA (服务等级协议) 保证的可用性水平如下：
</p>
<p>
1. 可用性为 99.9% 时，年停机时间为：8小时45分57.0秒。
</p>
<p>
2. 可用性为 99.99% 时，年停机时间为：52分35.7秒。
</p>
<p>
3. 可用性为 99.999% 时，年停机时间为：5分15.6秒。
</p>

<p>
为了保证“五个九”的可用性，必须非常严格地运营 Kubernetes 集群。
</p>

<blockquote>
HA 最佳实践
</blockquote>
<p>
构建高可用的 Kubernetes 系统时，请记住：“可用性往往不仅仅是技术错误，更是人为和流程层面的问题。”
</p>
<p>
首先要了解一个术语：
<b>
降级运行 (Graceful Degradation)
</b>
的概念。
</p>
<p>
降级运行是指通过将功能分散到多个层和模块中来构建系统的概念。即使系统的一部分发生严重错误，仍能提供一定水平的可用性。
</p>
<p>
Kubernetes 中有两种降级运行的方法：
</p>
<blockquote>
<b>
基础设施降级
</b>
：这种降级方式依赖复杂的算法和软件来处理硬件或虚拟机的意外错误。我们将探索如何确保 Kubernetes 核心组件的高可用性，以实现这种降级方式。
<br>
<br>
<b>
应用降级
</b>
：很大程度上取决于前面提到的微服务 (MS) 最佳实践策略，但也存在一些确保用户成功访问的模式。
</blockquote>
<p>
必须利用核心 Kubernetes 策略隔离底层基础设施故障，同时构建针对应用程序故障的缓存、故障转移和回滚机制，并确保 Kubernetes 组件本身的高可用性。
</p>

<blockquote>
反脆弱性 (Antifragility)
</blockquote>
<p>
<span>
“反脆弱性”简而言之，是指系统不仅能从外部的混乱或压力中生存，反而能从中获益并进化的性质。
</span>
</p>
<p>
<span>
为了应对 Kubernetes 系统的复杂性并利用大规模 Kubernetes 来维护系统，需要掌握几个核心概念。
</span>
</p>
<blockquote>
1. 冗余
<br>
2. 触发故障场景后进行应对、分析、探索和改进。（Netflix Chaos Monkey 是测试复杂系统稳定性的标准且组织良好的方法：https://github.com/Netflix/chaosmonkey）
<br>
3. 在系统中引入适当的模式。（重试、负载均衡、熔断器、超时、健康检查、并发控制是实现反脆弱性的核心模式。更高层级还有 Istio 等服务网格：https://techcafe.tistory.com/133）
</blockquote>

<blockquote>
Kubernetes 的 HA 方法
</blockquote>
<p>
Kubernetes 的 HA 配置包括将 etcd 和管理节点结合的“堆叠式主节点”方式，以及将 etcd 和管理节点分离的方式。
</p>
<p>
此处省略 Kubernetes 安装过程。
</p>

<blockquote>
集群生命周期
</blockquote>
<p>
让我们了解一下如何使用准入控制器、工作负载和 CRD 来扩展集群。
</p>

<p>
<b>
准入控制器 (Admission Controller)
</b>
</p>
<p>
准入控制器可以在 Kubernetes API 服务器完成认证和授权后，拦截对 API 服务器的调用。
</p>
<p>
以下两个准入控制器尤为重要：
</p>
<blockquote>
<b>
MutatingAdmissionWebhook
</b>
：仅在集群处于变更阶段时执行，用于调用连续变更请求的 Webhook。当需要自定义 CREATE、DELETE、UPDATE 等操作的批准逻辑并将其放入集群的业务逻辑中时，请使用此控制器。可以执行诸如使用 StorageClass 自动化存储配置等任务。
<br>
<br>
<b>
ValidatingAdmissionWebhook
</b>
：在批准阶段执行。用于调用检查“请求有效性”的 Webhook，例如验证配额增加的 Webhook。请记住，此控制器调用的任何 Webhook 都无法修改原始对象。
</blockquote>

<blockquote>
工作负载 API
</blockquote>
<p>
在 Kubernetes 初期，Pod 和工作负载与容器紧密耦合，共享 CPU、网络、存储和生命周期事件。Kubernetes 引入了副本 (Replication)、部署 (Deployment)、标签 (Label) 等概念来管理云原生应用的 12 要素，并引入了 StatefulSet 以帮助 Kubernetes 运维人员处理有状态工作负载。
</p>
<p>
随着时间推移，Kubernetes 工作负载概念被细分为多种：
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
这些多样的元素是 Kubernetes 对工作负载类型合理调整的结果，但遗憾的是，API 被分散到了 Kubernetes 代码库的多个位置。为了解决这个问题，经过数月甚至放弃部分向下兼容性的努力，终于将所有代码整合到了 `apps/v1` API 中。
</p>
<p>
在整合过程中有几个关键决定：
</p>
<blockquote>
<b>
默认选择器 (Selector)
</b>
：如果不指定标签选择器，将默认使用从模板标签中提取并自动生成的选择器。
<br>
<b>
不可变选择器
</b>
：虽然在某些情况下修改选择器对部署有意义，但修改选择器与 Kubernetes 的推荐做法相冲突，因此更改为通过 Kubernetes 编排的 Canary 发布和 Pod 标签替换方式。
<br>
<b>
滚动更新 (Rolling Update)
</b>
：应 Kubernetes 程序员的要求，滚动更新成为默认设置。
<br>
<b>
垃圾回收 (Garbage Collection)
</b>
：在 1.9 版本和 `apps/v1` 版本中，垃圾回收机制更加激进。删除 DaemonSet、ReplicaSet、StatefulSet 或 Deployment 时，对应的 Pod 也会被删除。
</blockquote>

<blockquote>
自定义资源定义 (CRD)
</blockquote>
<p>
自定义资源通过扩展 Kubernetes API 来补充准入控制器。可以使用自定义资源来改进正在运行的 Kubernetes 集群。
</p>
<p>
可以应用以下功能：
</p>

<table>
<tbody>
<tr>
<td>
CRUD
</td>
<td>
新的端点支持通过 HTTP 和 kubectl 进行 CRUD 基本操作
</td>
</tr>
<tr>
<td>
Watch
</td>
<td>
新的端点支持通过 HTTP 进行 Kubernetes Watch 操作
</td>
</tr>
<tr>
<td>
Discovery
</td>
<td>
kubectl 和 dashboard 等客户端会自动提供资源列表、显示和字段编辑操作
</td>
</tr>
<tr>
<td>
json-patch
</td>
<td>
新的端点支持 Content-Type: application/json-patch+json 的 PATCH 请求
</td>
</tr>
<tr>
<td>
merge-patch
</td>
<td>
新的端点支持 Content-Type: application/merge-patch+json 的 PATCH 请求
</td>
</tr>
<tr>
<td>
HTTPS
</td>
<td>
新的端点使用 HTTPS
</td>
</tr>
<tr>
<td>
内置认证
</td>
<td>
对扩展的访问使用核心 API 服务器（聚合层）进行身份验证
</td>
</tr>
<tr>
<td>
内置授权
</td>
<td>
对扩展的访问可以重用核心 API 服务器使用的授权方式；例如 RBAC
</td>
</tr>
<tr>
<td>
Finalizers
</td>
<td>
在执行外部清理之前，阻止删除扩展资源
</td>
</tr>
<tr>
<td>
Admission Webhooks
</td>
<td>
在任何创建/更新/删除操作期间，为扩展资源设置默认值并进行验证
</td>
</tr>
<tr>
<td>
UI/CLI 显示
</td>
<td>
Kubectl 和 Dashboard 可以显示扩展资源
</td>
</tr>
<tr>
<td>
Unset versus Empty
</td>
<td>
客户端可以区分“未设置的字段”和“零值字段”
</td>
</tr>
<tr>
<td>
客户端库生成
</td>
<td>
Kubernetes 提供通用客户端库，以及生成类型特定客户端库的工具
</td>
</tr>
<tr>
<td>
标签和注解
</td>
<td>
跨对象的通用元数据，工具知道如何对其进行核心资源和自定义资源的编辑
</td>
</tr>
</tbody>
</table>

## 参考资料