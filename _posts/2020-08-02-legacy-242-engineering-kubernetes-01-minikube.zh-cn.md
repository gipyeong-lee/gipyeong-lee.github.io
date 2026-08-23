---
layout: post
title: "Kubernetes - 01. Kubernetes 介绍 ( MiniKube 实践篇 )"
description: "本篇博文是使用《Kubernetes 基础巩固 3/e》一书进行学习时的总结笔记。1. 摘要：在 MacOS 环境下利用 MiniKube 构建并测试 Kubernetes 环境。※ Minikube 是一个在本地轻松运行 Kubernetes 的工具。Mini..."
date: 2020-08-02 20:55:21 +0900
section: blog
category: engineering
lang: zh-cn
ref: 2020-08-02-legacy-242-engineering-kubernetes-01-minikube
tags:
  - "kubernetes"
  - "Kubernetes"
  - "engineering"
translation_source_hash: 1cd65f2f8a7d1b0a7949bbb1c6ac83691a63077874ac7023cd252fbfa98545c8
---

<blockquote>
<span>
本篇博文是使用
</span>
<b>
《Kubernetes 基础巩固 3/e》
</b>
<span>
一书进行学习时的总结笔记。
</span>
</blockquote>
<h2>
1. 摘要
</h2>
<p>
在 MacOS 环境下利用 MiniKube 构建并测试 Kubernetes 环境。
</p>
<p>
<span>
※ Minikube 是一个在本地轻松运行 Kubernetes 的工具。
</span>
</p>
<p>
<span>
Minikube 使用 
</span>
<a href="https://github.com/docker/machine/tree/master/libmachine">
libmachine
</a>
<span>
来进行虚拟机供应，并使用 
</span>
<a href="https://github.com/kubernetes/kubeadm">
kubeadm
</a>
<span>
来供应 Kubernetes 集群。
</span>
</p>
<h2>
2. 实践
</h2>
<h3>
安装 Hypervisor
</h3>
<p>
笔者安装了 
<a href="https://www.virtualbox.org/" target="_blank" rel="noopener">
VirtualBox
</a>
。
</p>
<h3>
安装 MiniKube
</h3>
<h4>
(1) 确认 MacOS 虚拟化支持 VMX
</h4>
<pre class="python">
<code>
pc:~ user$ sysctl -a | grep -E --color 'machdep.cpu.features|VMX'

machdep.cpu.features: FPU VME DE PSE TSC MSR PAE MCE CX8 APIC SEP
MTRR PGE MCA CMOV PAT PSE36 CLFSH DS ACPI MMX FXSR SSE SSE2 SS HTT
TM PBE SSE3 PCLMULQDQ DTES64 MON DSCPL VMX SMX EST TM2 SSSE3 FMA CX16
TPR PDCM SSE4.1 SSE4.2 x2APIC MOVBE POPCNT AES PCID XSAVE OSXSAVE SEGLIM64
TSCTMR AVX1.0 RDRAND F16C
</code>
</pre>

<p>
<span>
如果能在输出中看到（用颜色高亮显示的）
</span>
VMX
<span>
，说明机器已启用 VT-x 功能。
</span>
</p>

<h4>
<span>
(2) brew install minikube
</span>
</h4>
<p>
通过 homebrew 安装 minikube。
</p>
<h4>
</h4>
<h3>
与 Kubernetes 交互
</h3>
<h4>
(1) <b>minikube start --driver=virtualbox</b>
</h4>
<p>
<span>
创建所谓的 
</span>
<a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands/#-em-set-context-em-">
kubectl 上下文 (context)
</a>
<span>
。该上下文包含与 Minikube 集群通信的设置。
</span>
</p>
<p>
<span>
<span>
※ Kubectl 是用于控制 Kubernetes 集群的命令行工具。
</span>
</span>
</p>

<pre class="python">
<code>
pc:~ user$ minikube start --driver=virtualbox

?  minikube v1.12.1 on Darwin 10.14.5
✨  Using the virtualbox driver based on user configuration
?  Downloading VM boot image ...
    &gt; minikube-v1.12.0.iso.sha256: 65 B / 65 B [-------------] 100.00% ? p/s 0s
    &gt; minikube-v1.12.0.iso: 173.57 MiB / 173.57 MiB [] 100.00% 9.71 MiB p/s 18s
?  Starting control plane node minikube in cluster minikube
?  Downloading Kubernetes v1.18.3 preload ...
    &gt; preloaded-images-k8s-v4-v1.18.3-docker-overlay2-amd64.tar.lz4: 526.27 MiB
?  Creating virtualbox VM (CPUs=2, Memory=4000MB, Disk=20000MB) ...
?  Installing Kubernetes v1.18.3 with Docker 19.03.12 runtime ...
?  Verifying Kubernetes components...
?  Enabled addons: default-storageclass, storage-provisioner
?  Done! kubectl is now configured to use "minikube"
</code>
</pre>

<p>
(2) 查看状态
</p>
<p>
<b>
minikube status
</b>
</p>
<pre class="python">
<code>
pc:~ user$ minikube status

minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured
</code>
</pre>

<p>
(3) 在 Virtualbox 中确认，可以看到创建了 minikube 虚拟机。
</p>


<p>
(4) 使用 kubectl 查看节点。
</p>
<pre class="python">
<code>
pc:~ user$ kubectl get node

NAME       STATUS   ROLES    AGE   VERSION
minikube   Ready    master   17m   v1.18.3
</code>
</pre>

<p>
(5) <span>若要查看服务的 NodePort，可以使用</span> kubectl <span>命令如下：</span>
</p>
<pre class="python">
<code>
kubectl get service $SERVICE --output='jsonpath="{.spec.ports[0].nodePort}"'
</code>
</pre>


<p>
(6) 若要使用 Kubernetes (k8s) Dashboard，<span>在运行 Minikube 后，请在 Shell 中执行以下命令以确认地址。</span>
</p>
<pre class="python">
<code>
pc:~ user$ minikube dashboard

?  Enabling dashboard ...
?  Verifying dashboard health ...
?  Launching proxy ...
?  Verifying proxy health ...
?  Opening http://127.0.0.1:63216/api/v1/namespaces/kubernetes-dashboard/
services/http:kubernetes-dashboard:/proxy/ in your default browser...
</code>
</pre>


<p>
(7) 可以创建一个简单的 Deployment 示例。
</p>
<pre class="scala">
<code>
pc:~ user$ kubectl run hello-minikube --image=k8s.gcr.io/echoserver:1.4 --port=8080
pod/hello-minikube created

pc:~ user$ kubectl get pods
NAME                              READY   STATUS    RESTARTS   AGE
hello-minikube                    1/1     Running   0          14s

pc:~ user$ kubectl delete pod hello-minikube
pod "hello-minikube" deleted

pc:~ user$ kubectl create deployment hello-minikube --image=k8s.gcr.io/echoserver:1.4
deployment.apps/hello-minikube created

pc:~ user$ kubectl expose deployment hello-minikube --type=NodePort
error: couldn't find port via --port flag or introspection

pc:~ user$ kubectl expose deployment hello-minikube --type=NodePort --port=8080
service/hello-minikube exposed

pc:~ user$ kubectl get services
NAME             TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
hello-minikube   NodePort    10.99.129.52   &lt;none&gt;        8080:32226/TCP   5m12s
kubernetes       ClusterIP   10.96.0.1      &lt;none&gt;        443/TCP          3d5h


pc:~ user$ minikube service hello-minikube
|-----------|----------------|-------------|-----------------------------|
| NAMESPACE |      NAME      | TARGET PORT |             URL             |
|-----------|----------------|-------------|-----------------------------|
| default   | hello-minikube |        8080 | http://192.168.99.100:32226 |
|-----------|----------------|-------------|-----------------------------|
?  Opening service default/hello-minikube in default browser...
</code>
</pre>
<p>
(8) Addon 设置
</p>
<pre class="scala">
<code>
$ minikube addons list
|-----------------------------|----------|--------------|
|         ADDON NAME          | PROFILE  |    STATUS    |
|-----------------------------|----------|--------------|
| ambassador                  | minikube | disabled     |
| dashboard                   | minikube | enabled ✅   |
| default-storageclass        | minikube | enabled ✅   |
| efk                         | minikube | disabled     |
| freshpod                    | minikube | disabled     |
| gvisor                      | minikube | disabled     |
| helm-tiller                 | minikube | disabled     |
| ingress                     | minikube | disabled     |
| ingress-dns                 | minikube | disabled     |
| istio                       | minikube | disabled     |
| istio-provisioner           | minikube | disabled     |
| kubevirt                    | minikube | disabled     |
| logviewer                   | minikube | disabled     |
| metallb                     | minikube | disabled     |
| metrics-server              | minikube | disabled     |
| nvidia-driver-installer     | minikube | disabled     |
| nvidia-gpu-device-plugin    | minikube | disabled     |
| olm                         | minikube | disabled     |
| pod-security-policy         | minikube | disabled     |
| registry                    | minikube | disabled     |
| registry-aliases            | minikube | disabled     |
| registry-creds              | minikube | disabled     |
| storage-provisioner         | minikube | enabled ✅   |
| storage-provisioner-gluster | minikube | disabled     |
|-----------------------------|----------|--------------|

$ minikube addons enable metrics-server
?  The 'metrics-server' addon is enabled

$ kubectl get pod,svc -n kube-system
NAME                                   READY   STATUS    RESTARTS   AGE
pod/coredns-66bff467f8-6pwgf           1/1     Running   1          3d5h
pod/etcd-minikube                      1/1     Running   1          3d5h
pod/kube-apiserver-minikube            1/1     Running   1          3d5h
pod/kube-controller-manager-minikube   1/1     Running   1          3d5h
pod/kube-proxy-msnjp                   1/1     Running   1          3d5h
pod/kube-scheduler-minikube            1/1     Running   1          3d5h
pod/metrics-server-7bc6d75975-nc2l5    1/1     Running   0          27s
pod/storage-provisioner                1/1     Running   2          3d5h

NAME                     TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                  AGE
service/kube-dns         ClusterIP   10.96.0.10      &lt;none&gt;        53/UDP,53/TCP,9153/TCP   3d5h
service/metrics-server   ClusterIP   10.98.180.253   &lt;none&gt;        443/TCP                  27s
</code>
</pre>

<h2>
参考资料
</h2>
<p>
-
<a href="https://kubernetes.io/">
https://kubernetes.io/
</a>
</p>