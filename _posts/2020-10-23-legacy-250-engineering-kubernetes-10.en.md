---
layout: post
title: "Kubernetes - 10. Designing for High Availability and Scalability"
description: "https://medium.com/@kumarshivam_66534/a-walk-through-on-iaas-paas-and-saas-7e8a4e4793fb In this 10th chapter, we cover the following: - Introduction to High Availability - HA Best Practices - Multi-region setup - Security Best Practices..."
date: 2020-10-23 11:27:53 +0900
section: blog
category: engineering
lang: en
ref: 2020-10-23-legacy-250-engineering-kubernetes-10
tags:
  - "HA"
  - "High Availability"
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
In this 10th chapter, we cover the following:
</p>
<blockquote>
- Introduction to High Availability
<br>
- High Availability Best Practices
<br>
- Multi-region setup
<br>
- Security Best Practices
<br>
- HA setup for hosted Kubernetes PaaS
<br>
- Cluster lifecycle events
<br>
- How to use Admission Controllers
<br>
- Introduction to the Workload API
<br>
- What are Custom Resource Definitions (CRDs)?
</blockquote>

<blockquote>
High Availability
</blockquote>
<p>
In the industry, High Availability (HA) refers to a very high level of availability, often referred to as "five nines" availability (99.999%).
</p>
<p>
Basically, availability is calculated as follows:
</p>
<blockquote>
Availability (%) = (Uptime / (Uptime + Downtime)) x 100
</blockquote>
<p>
Availability for uptime is calculated using the following formulas:
</p>
<blockquote>
MTBF (Mean Time Between Failures) = Value of 1 year in hours / Number of failures in 1 year
<br>
MTTR (Mean Time To Repair) = (Number of failures x System repair time) / Total number of failures
<br>
Uptime Availability = MTBF / (MTTR + MTBF)
<br>
Annual Downtime (per hour) = (1 - Uptime ratio) x 365 x 24
</blockquote>
<p>
The guaranteed availability levels for Service Level Agreements (SLA) are as follows:
</p>
<p>
1. If availability is 99.9%, downtime is 8 hours, 45 minutes, 57.0 seconds per year.
</p>
<p>
2. If availability is 99.99%, downtime is 52 minutes, 35.7 seconds per year.
</p>
<p>
3. If availability is 99.999%, downtime is 5 minutes, 15.6 seconds per year.
</p>

<p>
To guarantee "five nines" availability, you must operate your Kubernetes cluster very tightly.
</p>

<blockquote>
HA Best Practices
</blockquote>
<p>
To build a Kubernetes system that guarantees high availability, keep in mind that "availability is often as much about people and processes as it is about technical errors."
</p>
<p>
First, there is a term you should know: the concept of <b>graceful degradation</b>.
</p>
<p>
Graceful degradation is the concept of building functionality by distributing it across multiple layers and modules. Even if a critical error occurs in a part of the system, it continues to provide a certain level of availability.
</p>
<p>
There are two ways to handle graceful degradation in Kubernetes:
</p>
<blockquote>
<b>
Infrastructure Degradation
</b>
: This degradation method relies on complex algorithms and software to handle unexpected hardware or VM errors. We will explore how to secure high availability for the essential Kubernetes components needed to provide this degradation method.
<br>
<br>
<b>
Application Degradation
</b>
: While this is largely dependent on the aforementioned Microservices (MS) best practice strategies, there are several patterns to ensure user success.
</blockquote>
<p>
You should use core Kubernetes strategies to isolate underlying infrastructure failures, while building caching, failover, and rollback mechanisms for application failures, and ensuring high availability for Kubernetes components.
</p>

<blockquote>
Antifragility
</blockquote>
<p>
<span>
In simple terms, 'antifragility' is the property where performance actually increases in the face of external chaos or pressure.
</span>
</p>
<p>
<span>
To cope with the complexity of Kubernetes systems and maintain systems using large-scale Kubernetes, you need to know a few key concepts.
</span>
</p>
<blockquote>
1. Redundancy
<br>
2. Triggering failure scenarios, then responding to, analyzing, exploring, and improving them. (Netflix's Chaos Monkey is a standard, well-organized approach for testing complex system stability: https://github.com/Netflix/chaosmonkey)
<br>
3. Introducing appropriate patterns into the system. (Retry, load balancing, circuit breakers, timeouts, health checks, and concurrent connection checks are key patterns for antifragility. At a higher level, there is service mesh, such as Istio: https://techcafe.tistory.com/133)
</blockquote>

<blockquote>
HA Approaches for Kubernetes
</blockquote>
<p>
Kubernetes HA configurations include the "stacked master" approach, which combines etcd and control plane nodes, and the approach where etcd and control plane nodes are separated.
</p>
<p>
Installation of Kubernetes is omitted.
</p>

<blockquote>
Cluster Lifecycle
</blockquote>
<p>
Let's learn how to extend the cluster using Admission Controllers, Workloads, and CRDs.
</p>

<p>
<b>
Admission Controllers
</b>
</p>
<p>
Admission controllers can intercept calls to the Kubernetes API server after authentication and authorization are complete.
</p>
<p>
The following two admission controllers are particularly important:
</p>
<blockquote>
<b>
MutatingAdmissionWebhook
</b>
is executed only when the cluster is in the mutation phase, and it calls webhooks that modify requests sequentially. Use this controller when you want to customize approval logic for operations such as CREATE, DELETE, or UPDATE to inject business logic into the cluster. You can perform tasks such as automating storage provisioning using StorageClass.
<br>
<br>
<b>
ValidatingAdmissionWebhook
</b>
is executed by the admission controller during the validation phase. It calls webhooks that verify "request validity," such as a webhook that validates quota increases. Keep in mind that any webhook called by this controller cannot modify the original object.
</blockquote>

<blockquote>
Workload API
</blockquote>
<p>
In the early days of Kubernetes, pods and workloads were tightly coupled with containers, sharing CPU, networking, storage, and lifecycle events. Kubernetes introduced concepts such as replication, deployment, and labels to manage the 12-factor app methodology for cloud applications, and introduced StatefulSets to help Kubernetes operators handle stateful workloads.
</p>
<p>
Over time, Kubernetes workload concepts have been divided into several types:
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
These various elements are the result of Kubernetes rationally adjusting workload types, but unfortunately, the API was distributed throughout various parts of the Kubernetes codebase. After months of effort, including sacrificing some backward compatibility, we were able to consolidate all code into the apps/v1 API.
</p>
<p>
Important decisions made during the consolidation process are as follows:
</p>
<blockquote>
<b>
Default Selector
</b>
: If a label selector is not specified, it defaults to a selector automatically generated from the template labels.
<br>
<b>
Immutable Selector
</b>
: While changing selectors can be useful for Deployments, mutating selectors is contrary to Kubernetes recommendations. It has been changed to a method where Kubernetes orchestrates canary deployments and swaps out pod labels.
<br>
<b>
Rolling Update
</b>
: Rolling updates have become the default at the request of Kubernetes programmers.
<br>
Garbage Collection: In version 1.9 and apps/v1, garbage collection is more aggressive. If you delete a DaemonSet, ReplicaSet, StatefulSet, or Deployment, the associated pods are also deleted.
</blockquote>

<blockquote>
Custom Resource Definitions
</blockquote>
<p>
Custom resources extend the Kubernetes API and complement admission controllers. You can use custom resources to improve running Kubernetes clusters.
</p>
<p>
You can apply features such as:
</p>

<table>
<tbody>
<tr>
<td>
CRUD
</td>
<td>
The new endpoints support CRUD basic operations via HTTP and kubectl
</td>
</tr>
<tr>
<td>
Watch
</td>
<td>
The new endpoints support Kubernetes Watch operations via HTTP
</td>
</tr>
<tr>
<td>
Discovery
</td>
<td>
Clients like kubectl and dashboard automatically offer list, display, and field edit operations on your resources
</td>
</tr>
<tr>
<td>
json-patch
</td>
<td>
The new endpoints support PATCH with Content-Type: application/json-patch+json
</td>
</tr>
<tr>
<td>
merge-patch
</td>
<td>
The new endpoints support PATCH with Content-Type: application/merge-patch+json
</td>
</tr>
<tr>
<td>
HTTPS
</td>
<td>
The new endpoints uses HTTPS
</td>
</tr>
<tr>
<td>
Built-in Authentication
</td>
<td>
Access to the extension uses the core API server (aggregation layer) for authentication
</td>
</tr>
<tr>
<td>
Built-in Authorization
</td>
<td>
Access to the extension can reuse the authorization used by the core API server; for example, RBAC.
</td>
</tr>
<tr>
<td>
Finalizers
</td>
<td>
Block deletion of extension resources until external cleanup happens.
</td>
</tr>
<tr>
<td>
Admission Webhooks
</td>
<td>
Set default values and validate extension resources during any create/update/delete operation.
</td>
</tr>
<tr>
<td>
UI/CLI Display
</td>
<td>
Kubectl, dashboard can display extension resources.
</td>
</tr>
<tr>
<td>
Unset versus Empty
</td>
<td>
Clients can distinguish unset fields from zero-valued fields.
</td>
</tr>
<tr>
<td>
Client Libraries Generation
</td>
<td>
Kubernetes provides generic client libraries, as well as tools to generate type-specific client libraries.
</td>
</tr>
<tr>
<td>
Labels and annotations
</td>
<td>
Common metadata across objects that tools know how to edit for core and custom resources.
</td>
</tr>
</tbody>
</table>