---
layout: post
title: "Kubernetes - 01. Kubernetesの紹介 (MiniKube実践編)"
description: "本記事は『Kubernetes完全ガイド 第3版』を使用して学習した内容をまとめたものです。1. 要約 MacOS環境でMiniKubeを活用し、Kubernetes環境を構築してテストします。※MinikubeはKubernetesをローカルで簡単に実行するためのツールです。Mini..."
date: 2020-08-02 20:55:21 +0900
section: blog
category: engineering
lang: ja
ref: 2020-08-02-legacy-242-engineering-kubernetes-01-minikube
tags:
  - "kubernetes"
  - "Kubernetes"
  - "engineering"
translation_source_hash: 1cd65f2f8a7d1b0a7949bbb1c6ac83691a63077874ac7023cd252fbfa98545c8
---

<blockquote>
<span>
本記事は『
</span>
<b>
Kubernetes完全ガイド 第3版
</b>
<span>
』を使用して学習した内容をまとめたものです。
</span>
</blockquote>
<h2>
1. 要約
</h2>
<p>
MacOS環境でMiniKubeを活用し、Kubernetes環境を構築してテストします。
</p>
<p>
<span>
※ MinikubeはKubernetesをローカルで簡単に実行するためのツールです。
</span>
</p>
<p>
<span>
MinikubeはVMプロビジョニングのために
</span>
<a href="https://github.com/docker/machine/tree/master/libmachine">
libmachine
</a>
<span>
を使用し、Kubernetesクラスタをプロビジョニングするために
</span>
<a href="https://github.com/kubernetes/kubeadm">
kubeadm
</a>
<span>
を使用します。
</span>
</p>
<h2>
2. 実践
</h2>
<h3>
ハイパーバイザのインストール
</h3>
<p>
筆者は
<a href="https://www.virtualbox.org/" target="_blank" rel="noopener">
VirtualBox
</a>
をインストールしました。
</p>
<h3>
miniKubeのインストール
</h3>
<h4>
(1) MacOSの仮想化サポートVMXの確認
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
出力の中に（色で強調された）
</span>
VMX
<span>
があれば、マシンでVT-x機能が有効になっています。
</span>
</p>

<h4>
<span>
(2) brew install minikube
</span>
</h4>
<p>
homebrewを使用してminikubeをインストールします。
</p>
<h3>
Kubernetesとのやり取り
</h3>
<h4>
(1)
<b>
minikube start --driver=virtualbox
</b>
</h4>
<p>
<span>
Minikubeと呼ぶ
</span>
<a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands/#-em-set-context-em-">
kubectlコンテキスト
</a>
<span>
を作成します。このコンテキストには、Minikubeクラスタと通信するための設定が含まれています。
</span>
</p>
<p>
<span>
<span>
※ KubectlはKubernetesクラスタを制御するためのコマンドラインツールです。
</span>
</span>
</p>

<pre class="python">
<code>
pc:~ user$ minikube start --driver=virtualbox

?  Darwin 10.14.5 上の minikube v1.12.1
✨  ユーザー環境設定情報に基づき virtualbox ドライバを使用中
?  仮想マシンブートイメージをダウンロード中 ...
    &gt; minikube-v1.12.0.iso.sha256: 65 B / 65 B [-------------] 100.00% ? p/s 0s
    &gt; minikube-v1.12.0.iso: 173.57 MiB / 173.57 MiB [] 100.00% 9.71 MiB p/s 18s
?  Starting control plane node minikube in cluster minikube
?  Kubernetes v1.18.3 をダウンロード中 ...
    &gt; preloaded-images-k8s-v4-v1.18.3-docker-overlay2-amd64.tar.lz4: 526.27 MiB
?  virtualbox VM (CPUs=2, Memory=4000MB, Disk=20000MB) を作成中 ...
?  Kubernetes v1.18.3 を Docker 19.03.12 ランタイムでインストール中
?  Verifying Kubernetes components...
?  Enabled addons: default-storageclass, storage-provisioner
?  完了しました！これで kubectl が "minikube" を使用するように設定されました
</code>
</pre>

<p>
(2) 状態の確認
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
(3) Virtualboxを確認すると、minikube vmが作成されています。
</p>


<p>
(4) kubectlを使用してノードを確認しましょう。
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
サービスのNodePortを確認するには、
</span>
kubectl
<span>
コマンドで以下のように実行します。
</span>
</p>
<pre class="python">
<code>
kubectl get service $SERVICE --output='jsonpath="{.spec.ports[0].nodePort}"'
</code>
</pre>


<p>
(6) Kubernetes (k8s) ダッシュボードを利用するには、
<span>
Minikubeを実行した後、シェルで以下のコマンドを実行してアドレスを確認します。
</span>
</p>
<pre class="python">
<code>
pc:~ user$ minikube dashboard

?  ダッシュボードを有効化中 ...
?  Verifying dashboard health ...
?  プロキシを開始中 ...
?  Verifying proxy health ...
?  Opening http://127.0.0.1:63216/api/v1/namespaces/kubernetes-dashboard/
services/http:kubernetes-dashboard:/proxy/ in your default browser...
</code>
</pre>


<p>
(7) 簡単なデプロイメントの例を作成できます。
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
(8) アドオン設定
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
参考資料
</h2>
<p>
-
<a href="https://kubernetes.io/">
https://kubernetes.io/
</a>
</p>