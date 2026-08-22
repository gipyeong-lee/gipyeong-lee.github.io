---
layout: post
title: "Kubernetes - 01. 쿠버네티스 소개 ( MiniKube 실습편 )"
description: "본 포스팅은 ' 쿠버네티스 기초 다지기 3/e' 책을 사용하여 스터디를 하면서 정리 한 내용입니다. 1. 요약 MacOS 환경에서 MiniKube 를 활용하여 Kubernetes 환경을 구성하여 테스트해본다. ※ Minikube는 쿠버네티스를 로컬에서 쉽게 실행하는 도구이다 Min..."
date: 2020-08-02 20:55:21 +0900
section: blog
category: engineering
lang: ko
ref: 2020-08-02-legacy-242-engineering-kubernetes-01-minikube
tags:
  - "kubernetes"
  - "Kubernetes"
  - "engineering"
---

<blockquote>
<span>
본 포스팅은  '
</span>
<b>
쿠버네티스 기초 다지기 3/e'
</b>
<span>

책을 사용하여 스터디를 하면서 정리 한 내용입니다.
</span>
</blockquote>
<h2>
1. 요약
</h2>
<p>
MacOS 환경에서 MiniKube 를 활용하여 Kubernetes 환경을 구성하여 테스트해본다.
</p>
<p>
<span>
※ Minikube는 쿠버네티스를 로컬에서 쉽게 실행하는 도구이다
</span>
</p>
<p>
<span>
Minikube는 VM 프로비저닝을 위해서

</span>
<a href="https://github.com/docker/machine/tree/master/libmachine">
libmachine
</a>
<span>
를 사용하고, 쿠버네티스 클러스터를 프로비저닝하기 위해

</span>
<a href="https://github.com/kubernetes/kubeadm">
kubeadm
</a>
<span>
을 사용한다.
</span>
</p>
<h2>
2. 실습
</h2>
<h3>
Hypervisor 설치
</h3>
<p>
필자는
<a href="https://www.virtualbox.org/" target="_blank" rel="noopener">
VirtualBox
</a>
를 설치하였다.
</p>
<h3>
miniKube 설치
</h3>
<h4>
(1) MacOS가상화 지원 VMX 확인

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
만약 출력 중에 (색상으로 강조된)

</span>
VMX
<span>
를 볼 수 있다면, VT-x 기능이 머신에서 활성화된 것이다.
</span>
</p>

<h4>
<span>
(2) brew install minikube
</span>
</h4>
<p>
homebrew 를 통해서 minikube 설치를 진행한다.
</p>
<h4>
</h4>
<h3>
쿠버네티스와 상호작용하기
</h3>
<h4>
(1)
<b>
minikube start --driver=virtualbox
</b>
</h4>
<p>
<span>
Minikube로 부르는

</span>
<a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands/#-em-set-context-em-">
kubectl 콘텍스트
</a>
<span>
를 생성한다. 이 콘텍스트는 Minikube 클러스터와 통신하는 설정을 포함한다
</span>
</p>
<p>
<span>
<span>
※ Kubectl은 쿠버네티스 클러스터를 제어하기 위한 커맨드 라인 도구이다
</span>
</span>
</p>

<pre class="python">
<code>
pc:~ user$ minikube start --driver=virtualbox

?  Darwin 10.14.5 위의 minikube v1.12.1
✨  유저 환경 설정 정보에 기반하여 virtualbox 드라이버를 사용하는 중
?  가상 머신 부트 이미지 다운로드 중 ...
    &gt; minikube-v1.12.0.iso.sha256: 65 B / 65 B [-------------] 100.00% ? p/s 0s
    &gt; minikube-v1.12.0.iso: 173.57 MiB / 173.57 MiB [] 100.00% 9.71 MiB p/s 18s
?  Starting control plane node minikube in cluster minikube
?  Downloading Kubernetes v1.18.3 preload ...
    &gt; preloaded-images-k8s-v4-v1.18.3-docker-overlay2-amd64.tar.lz4: 526.27 MiB
?  virtualbox VM (CPUs=2, Memory=4000MB, Disk=20000MB) 를 생성하는 중 ...
?  쿠버네티스 v1.18.3 을 Docker 19.03.12 런타임으로 설치하는 중
?  Verifying Kubernetes components...
?  Enabled addons: default-storageclass, storage-provisioner
?  끝났습니다! 이제 kubectl 이 "minikube" 를 사용할 수 있도록 설정되었습니다
</code>
</pre>

<p>
(2) 상태 확인
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
(3) Virtualbox 를 확인해보면  minikube vm 이 생성되어 있다.
</p>


<p>
(4) kubectl 을 이용해서 노드를 확인하자.
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
서비스의 NodePort를 확인하려면

</span>
kubectl
<span>

명령어로 아래와 같이 하면 된다
</span>
</p>
<pre class="python">
<code>
kubectl get service $SERVICE --output='jsonpath="{.spec.ports[0].nodePort}"'
</code>
</pre>


<p>
(6) 쿠버네티스(k8s) dashboard를 이용하려면,
<span>

Minikube를 실행한 후 쉘에서 아래 명령어를 실행하여 주소를 확인한다.
</span>
</p>
<pre class="python">
<code>
pc:~ user$ minikube dashboard

?  대시보드를 활성화하는 중 ...
?  Verifying dashboard health ...
?  프록시를 시작하는 중 ...
?  Verifying proxy health ...
?  Opening http://127.0.0.1:63216/api/v1/namespaces/kubernetes-dashboard/
services/http:kubernetes-dashboard:/proxy/ in your default browser...
</code>
</pre>


<p>
(7) 간단한 디플로이먼트 예제를 만들 수 있다.
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
(8) Addon 설정
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
참고 및 출처
</h2>
<p>
-
<a href="https://kubernetes.io/">
https://kubernetes.io/
</a>
</p>
