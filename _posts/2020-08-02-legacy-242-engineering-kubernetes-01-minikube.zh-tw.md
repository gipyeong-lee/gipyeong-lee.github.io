---
layout: post
title: "Kubernetes - 01. Kubernetes 介紹 ( MiniKube 實作篇 )"
description: "本篇文章是使用《쿠버네티스 기초 다지기 3/e》(Kubernetes 基礎紮實 3/e) 一書進行學習時所整理的內容。 1. 摘要 在 MacOS 環境中利用 MiniKube 建構 Kubernetes 環境並進行測試。 ※ Minikube 是在本地端輕鬆執行 Kubernetes 的工具。"
date: 2020-08-02 20:55:21 +0900
section: blog
category: engineering
lang: zh-tw
ref: 2020-08-02-legacy-242-engineering-kubernetes-01-minikube
tags:
  - "kubernetes"
  - "Kubernetes"
  - "engineering"
translation_source_hash: 1cd65f2f8a7d1b0a7949bbb1c6ac83691a63077874ac7023cd252fbfa98545c8
---

<blockquote>
<span>
本篇文章是使用《
</span>
<b>
쿠버네티스 기초 다지기 3/e
</b>
<span>
》（Kubernetes 基礎紮實 3/e）一書進行學習時所整理的內容。
</span>
</blockquote>
<h2>
1. 摘要
</h2>
<p>
在 MacOS 環境中利用 MiniKube 建構 Kubernetes 環境並進行測試。
</p>
<p>
<span>
※ Minikube 是在本地端輕鬆執行 Kubernetes 的工具。
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
進行 VM 配置，並使用 
</span>
<a href="https://github.com/kubernetes/kubeadm">
kubeadm
</a>
<span>
來配置 Kubernetes 叢集。
</span>
</p>
<h2>
2. 實作
</h2>
<h3>
安裝 Hypervisor
</h3>
<p>
筆者安裝了 
<a href="https://www.virtualbox.org/" target="_blank" rel="noopener">
VirtualBox
</a>
。
</p>
<h3>
安裝 miniKube
</h3>
<h4>
(1) 確認 MacOS 虛擬化支援 VMX
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
如果能在輸出中看到（以顏色標示的）
</span>
VMX
<span>
，表示該機器已啟用 VT-x 功能。
</span>
</p>

<h4>
<span>
(2) brew install minikube
</span>
</h4>
<p>
透過 homebrew 安裝 minikube。
</p>
<h4>
</h4>
<h3>
與 Kubernetes 互動
</h3>
<h4>
(1) 
<b>
minikube start --driver=virtualbox
</b>
</h4>
<p>
<span>
建立稱為 Minikube 的 
</span>
<a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands/#-em-set-context-em-">
kubectl context
</a>
<span>
。此 context 包含與 Minikube 叢集通訊的設定。
</span>
</p>
<p>
<span>
<span>
※ Kubectl 是用來控制 Kubernetes 叢集的命令列工具。
</span>
</span>
</p>

<pre class="python">
<code>
pc:~ user$ minikube start --driver=virtualbox

?  Darwin 10.14.5 上的 minikube v1.12.1
✨  基於使用者環境設定資訊，正在使用 virtualbox 驅動程式
?  正在下載虛擬機開機映像檔 ...
    > minikube-v1.12.0.iso.sha256: 65 B / 65 B [-------------] 100.00% ? p/s 0s
    > minikube-v1.12.0.iso: 173.57 MiB / 173.57 MiB [] 100.00% 9.71 MiB p/s 18s
?  正在啟動叢集 minikube 中的 control plane 節點 minikube
?  正在下載 Kubernetes v1.18.3 預載映像檔 ...
    > preloaded-images-k8s-v4-v1.18.3-docker-overlay2-amd64.tar.lz4: 526.27 MiB
?  正在建立 virtualbox VM (CPUs=2, Memory=4000MB, Disk=20000MB) ...
?  正在安裝 Kubernetes v1.18.3 並使用 Docker 19.03.12 執行環境
?  正在驗證 Kubernetes 元件...
?  已啟用擴充功能 (addons): default-storageclass, storage-provisioner
?  完成！現在已設定 kubectl 以使用 "minikube"
</code>
</pre>

<p>
(2) 確認狀態
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
(3) 檢查 Virtualbox，可以看到已建立 minikube vm。
</p>


<p>
(4) 使用 kubectl 查看節點。
</p>
<pre class="python">
<code>
pc:~ user$ kubectl get node

NAME       STATUS   ROLES    AGE   VERSION
minikube   Ready    master   17m   v1.18.3
</code>
</pre>

<p>
(5) 
<span>
若要確認服務的 NodePort，可以使用 
</span>
kubectl
<span>
指令執行以下操作：
</span>
</p>
<pre class="python">
<code>
kubectl get service $SERVICE --output='jsonpath="{.spec.ports[0].nodePort}"'
</code>
</pre>


<p>
(6) 若要使用 Kubernetes (k8s) dashboard，
<span>
請在執行 Minikube 後，於 shell 中執行以下指令以確認位址。
</span>
</p>
<pre class="python">
<code>
pc:~ user$ minikube dashboard

?  正在啟用 dashboard ...
?  正在驗證 dashboard 健康狀態 ...
?  正在啟動 proxy ...
?  正在驗證 proxy 健康狀態 ...
?  正在預設瀏覽器中開啟 http://127.0.0.1:63216/api/v1/namespaces/kubernetes-dashboard/
services/http:kubernetes-dashboard:/proxy/ ...
</code>
</pre>


<p>
(7) 可以建立一個簡單的 Deployment 範例。
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
hello-minikube   NodePort    10.99.129.52   <none>        8080:32226/TCP   5m12s
kubernetes       ClusterIP   10.96.0.1      <none>        443/TCP          3d5h


pc:~ user$ minikube service hello-minikube
|-----------|----------------|-------------|-----------------------------|
| NAMESPACE |      NAME      | TARGET PORT |             URL             |
|-----------|----------------|-------------|-----------------------------|
| default   | hello-minikube |        8080 | http://192.168.99.100:32226 |
|-----------|----------------|-------------|-----------------------------|
?  正在預設瀏覽器中開啟服務 default/hello-minikube...
</code>
</pre>
<p>
(8) Addon 設定
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
?  已啟用 'metrics-server' addon

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
service/kube-dns         ClusterIP   10.96.0.10      <none>        53/UDP,53/TCP,9153/TCP   3d5h
service/metrics-server   ClusterIP   10.98.180.253   <none>        443/TCP                  27s
</code>
</pre>

<h2>
參考資料
</h2>
<p>
-
<a href="https://kubernetes.io/">
https://kubernetes.io/
</a>
</p>