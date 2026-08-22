---
layout: post
title: "Kubernetes - 10. 고가용성과 확장성을 위한 설계"
description: "https://medium.com/@kumarshivam_66534/a-walk-through-on-iaas-paas-and-saas-7e8a4e4793fb 이번 10 장에서 다루는 내용은 다음과 같습니다. - 고가용성 소개 - 고가용성 모범 사례 - 멀리 리전 설정 - 보안 모범..."
date: 2020-10-23 11:27:53 +0900
section: blog
category: engineering
lang: ko
ref: 2020-10-23-legacy-250-engineering-kubernetes-10
tags:
  - "HA"
  - "고가용성"
  - "kubernetes"
  - "쿠버네티스"
  - "Kubernetes"
  - "engineering"
---

<p>
<figure class="imageblock alignCenter">

<figcaption>
https://medium.com/@kumarshivam_66534/a-walk-through-on-iaas-paas-and-saas-7e8a4e4793fb
</figcaption>
</figure>
</p>
<p>
이번 10 장에서 다루는 내용은 다음과 같습니다.
</p>
<blockquote>
- 고가용성 소개
<br>
- 고가용성 모범 사례
<br>
- 멀리 리전 설정
<br>
- 보안 모범 사례
<br>
- 호스팅된 쿠버네티스 PasS의 고가용성 설정
<br>
- 클러스터 수명 주기 이벤트
<br>
- 어드미션 컨트롤러 사용법
<br>
- 워크로드 API 소개
<br>
- 커스텀 리소스 정의(CRD) 란 무엇인가?
</blockquote>

<blockquote>
고가용성
</blockquote>
<p>
업계에서 고가용성은 매우 높은 수준의 가용성을 의미하는데 이는 9가 5개인 가용성이라고 대게 일컫어진다. ( 99.999% )
</p>
<p>
기본적으로 가용성은 다음처럼 계산이 된다.
</p>
<blockquote>
가용성(백분율) = (가동 시간 / (가동 시간 + 비가동 시간)) x 100
</blockquote>
<p>
가동시간의 가용성은 다음의 공식이 되는데
</p>
<blockquote>
MTBF = 1년을 시간으로 환산한 값 / 1년 동안의 고장 횟수
<br>
MTTR = (고장횟수 x 시스템 수리 시간) / 총 고장 횟수
<br>
가동 시간 가용성 = MTBF/(MTTR + MTBF)
<br>
연간 비가동 시간(per hour)  = (1 - 가동 시간 비율 ) x 365 x 24
</blockquote>
<p>
SLA ( 서비스 수준 계약 )의 보장된 가용성 수준은 다음과 같다.
</p>
<p>
1. 가용성이 99.9%인 경우, 비가동 시간은 연간 :8시간 45분 57.0초.
</p>
<p>
2. 가용성이 99.99%인 경우, 비가동 시간은 연간 : 52분 35.7초
</p>
<p>
3. 가용성이 99.999%인 경우, 비가동 시간은 연간 : 5분 15.6초
</p>

<p>
9가 5개인 가용성을 보장하려면 정말 빠듯하게 쿠버네티스 클러스터를 운영해야 한다.
</p>

<blockquote>
HA 모범 사례
</blockquote>
<p>
고가용성을 보장하는 쿠버네티스 시스템을 구축하려면 "가용성은 기술적인 에러 만큼이나 인간과 프로세스에 관한 문제인 경우가 많다"는 점을 알고 가자.
</p>
<p>
우선 알고 가야할 용어가 있다.
<b>
단계별 성능 저하
</b>
라는 개념이다.
</p>
<p>
단계별 성능 저하는 여러 레이어와 모듈로 기능을 분산해 구축한다는 개념이다. 시스템 일부에서 치명적인 에러가 발생하더라도 일정 수준의 가용성을 계속 제공한다.
</p>
<p>
쿠버네티스에는 두 가지 단계별 성능 저하 방법이 있다.
</p>
<blockquote>
<b>
인프라 성능 저하
</b>
: 이 성능 저하 방식은 하드웨어 또는 VM의 예기치 않은 에러를 처리하기 위해 복잡한 알고리즘과 소프트웨어에 의존한다. 이 성능 저하 방식 제공을 위해 필요한 쿠버네티스 필수 컴포넌트의 고가용성 확보 방법을 탐구할 것이다.
<br>
<br>
<b>
애플리케이션 성능 저하
</b>
: 앞서 언급한 MS 모범 사례 전략에 크게 좌우될 수 밖에 없지만 사용자의 성공을 보장하기 위한 몇 가지 패턴이 있다.
</blockquote>
<p>
핵심 쿠버네티스 전략을 사용해 기반 인프라 장애를 격리하는 한편, 애플리케이션 장애에 대비한 캐싱, 페일오버, 롤백 메커니즘을 구축하고 쿠버네티스 컴포넌트의 고가용성을 확보해야한다.
</p>

<blockquote>
반취약성
</blockquote>
<p>
<span>
'반취약성'이란 쉽게 말해 외부의 혼란이나 압력에 오히려 성과가 상승하는 성질을 말한다.
</span>
</p>
<p>
<span>
쿠버네티스 시스템의 복잡성에 대처하고 거대한 쿠버네티스를 활용해 시스템을 유지하려면 몇 가지 핵심 개념을 알아야 한다.
</span>
</p>
<blockquote>
1. 이중화
<br>
2. 실패 시나리오 촉발 후 이에 대응하고 분석, 탐구, 개선하는 것. ( 넷플릭스 카오스 몽키는 복잡한 시스템 안정성을 테스트하기 위한 표준적이고 잘 정리된 접근법이다 https://github.com/Netflix/chaosmonkey )
<br>
3. 시스템에 적절한 패턴을 도입한다. ( 재시도, 로드 밸런싱, 서킷 브레이커, 타임 아웃, 헬스체크, 동시 접속 점검은 반취약성을 위한 핵심 패턴이다. 더 높은 수준에는 이스티오 등의 서비스 메시가 있다. https://techcafe.tistory.com/133
</blockquote>

<blockquote>
쿠버네티스를 위한 HA 접근법
</blockquote>
<p>
쿠버네티스의 HA 구성에는 etcd와 관리자 노드를 결합한 스택트 마스터 방식과 etcd 와 관리자 노드를 분리한 방식이 있다.
</p>
<p>
쿠버네티스 설치는 생략한다.
</p>

<blockquote>
클러스터 수명 주기
</blockquote>
<p>
어드미션 컨트롤러, 워크로드, CRD 를 사용해 클러스터를 확장하는 방법을 알아보자.
</p>

<p>
<b>
어드미션 컨트롤러
</b>
</p>
<p>
어드미션 컨트롤러는 쿠버네티스 API 서버의 인증과 권한 부여가 완료된 후에 쿠버네티스 API 서버에 대한 호출을 가로챌 수 있다.
</p>
<p>
다음의 두 어드미션 컨트롤러가 특히 중요햐다
</p>
<blockquote>
<b>
MutatingAdmissionWebhook
</b>
은 클러스터가 변형 단계일 떄만 실행되며 요청을 연속적으로 변형하는 웹 훅을 호출한다. CREATE, DELETE, UPDATE와 같은 작업의 승인 로직을 사용자 정의해 비즈니스 로직을 클러스터에 넣을 댸 이 컨트롤러를 사용한다.  StorageClass를 사용해 저장소 프로비저닝을 자동화하는 등의 작업을 수행할 수 있다.
<br>
<br>
<b>
ValidatingAdmissionWebhook
</b>
은 승인 단계에서 어드미션 컨트롤러가 실행한다. 쿼터 증가를 검증하는 웹 훅과 같은 "요청 유효성"을 검사하는 웹 훅을 호출한다. 이 컨트롤러가 호출하는 모든 웹 훅은 원래의 객체를 변형하지 못한다는 점을 명심해야한다.
</blockquote>

<blockquote>
워크로드 API
</blockquote>
<p>
쿠버네티스 초기에는 파드와 워크로드가 CPU, 네트워킹, 저장소, 수명 주기 이벤트를 공유하는 컨테이너와 밀접하게 결합됐다. 쿠버네티스는 클라우드 애플리케이션의 12가지 요소를 관리할 수 있도록 레플리케이션, 디플로이먼트, 레이블 등의 개념을 도입했으며 쿠버네티스 운영자가 스테이트풀 워크로드를 처리할 수 있도록 스테이트풀 셋을 도입했다.
</p>
<p>
시간이 흐르고, 쿠버네티스 워크로드 개념은 여러개로 나뉘어진다.
</p>
<blockquote>
파드
<br>
레플리케이션 컨트롤러
<br>
레플리카셋
<br>
디플로이먼트
<br>
데몬셋
<br>
스테이트풀셋
</blockquote>
<p>
이런 다양한 요소는 쿠버네티스가 워크로드 유형을 합리적으로 조정한 결과지만 안타깝게도 쿠버네티스 코드베이스의 여러 곳으로 API가 분산됐다. 이문제를 해결하기 위해 하위 호환성까지 일부 포기하는 수개월간의 노력 끝에 모든 코드를 apps/v1 API 로 모을 수 있었다.
</p>
<p>
모으는 과정에 중요한 결정이 있는데 아래와 같다.
</p>
<blockquote>
<b>
기본
</b>
<b>
셀렉터
</b>
: 레이블 셀렉터를 지정하지 않으면 템플릿 레이블에서 추출해 자동 생성한 셀렉터를 기본값으로 사용한다.
<br>
<b>
불변
</b>
<b>
셀렉터
</b>
: 셀렉터 변경이 디플로이먼트에 유용한 경우도 있지만 셀렉터를 변형하는 것은 쿠버네티스의 권장 사항과 대치되기 때문에 쿠버네티스가 오케스트레이션하는 canary 배포와 파드 레이블을 갈아붙이는 방식으로 변경됐다.
<br>
<b>
롤링 업데이트
</b>
: 쿠버네티스 프로그래머들의 요청으로 롤링 업데이트가 기본값이 됐다.
<br>
가비지 컬렉션 : 1.9 버전과 apps/v1 버전에서는 가비지 컬렉션이 더 공격적이다. 데몬셋, 레플리카셋, 스테이트풀 셋, 디플로이먼트를 삭제하면 pod 도 삭제된다.
</blockquote>

<blockquote>
커스텀 리소스 정의
</blockquote>
<p>
커스텀 리소스는 쿠버네티스 API 를 확장해  어드미션 컨트롤러를 보완한다. 운영중인 쿠버네티스 클러스터를 개선하기 위해 커스텀 리소스를 사용할 수 있다.
</p>
<p>
다음 같은 기능들을 적용 할 수 있다.
</p>

<table>
<tbody>
<tr>
<td>
CRUD
</td>
<td>
The new endpoints support CRUD basic operations via HTTP and

kubectl
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
Clients like

kubectl

and dashboard automatically offer list, display, and field edit operations on your resources
</td>
</tr>
<tr>
<td>
json-patch
</td>
<td>
The new endpoints support PATCH with

Content-Type: application/json-patch+json
</td>
</tr>
<tr>
<td>
merge-patch
</td>
<td>
The new endpoints support PATCH with

Content-Type: application/merge-patch+json
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
