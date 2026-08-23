---
layout: post
title: "Kubernetes - 10. 高可用性とスケーラビリティのための設計"
description: "https://medium.com/@kumarshivam_66534/a-walk-through-on-iaas-paas-and-saas-7e8a4e4793fb 今回の第10章で扱う内容は以下の通りです。 - 高可用性（HA）の紹介 - 高可用性のベストプラクティス - マルチリージョン設定 - セキュリティベストプラクティス..."
date: 2020-10-23 11:27:53 +0900
section: blog
category: engineering
lang: ja
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
今回の第10章で扱う内容は以下の通りです。
</p>
<blockquote>
- 高可用性（HA）の紹介
<br>
- 高可用性のベストプラクティス
<br>
- マルチリージョン設定
<br>
- セキュリティベストプラクティス
<br>
- ホステッドKubernetes PaaSにおける高可用性設定
<br>
- クラスターライフサイクルイベント
<br>
- アドミッションコントローラーの利用法
<br>
- ワークロードAPIの紹介
<br>
- カスタムリソース定義（CRD）とは何か？
</blockquote>

<blockquote>
高可用性（HA）
</blockquote>
<p>
業界において高可用性とは、非常に高いレベルの可用性を意味し、一般的に「5つの9」（99.999%）の可用性と呼称されます。
</p>
<p>
基本的に可用性は以下のように計算されます。
</p>
<blockquote>
可用性（パーセンテージ） = （稼働時間 / （稼働時間 + ダウンタイム）） x 100
</blockquote>
<p>
稼働時間の可用性は以下の公式となります。
</p>
<blockquote>
MTBF = 1年を時間換算した値 / 1年間の故障回数
<br>
MTTR = （故障回数 x システム修理時間） / 総故障回数
<br>
稼働時間可用性 = MTBF / （MTTR + MTBF）
<br>
年間ダウンタイム（1時間単位） = （1 - 稼働率） x 365 x 24
</blockquote>
<p>
SLA（サービスレベル合意書）で保証される可用性のレベルは以下の通りです。
</p>
<p>
1. 可用性が99.9%の場合、年間ダウンタイム：8時間45分57.0秒
</p>
<p>
2. 可用性が99.99%の場合、年間ダウンタイム：52分35.7秒
</p>
<p>
3. 可用性が99.999%の場合、年間ダウンタイム：5分15.6秒
</p>

<p>
5つの9の可用性を保証するには、Kubernetesクラスターを極めて厳密に運用する必要があります。
</p>

<blockquote>
HAベストプラクティス
</blockquote>
<p>
高可用性を保証するKubernetesシステムを構築するには、「可用性は技術的なエラーと同じくらい、人間やプロセスに関する問題であることが多い」という点を理解しておくべきです。
</p>
<p>
まず知っておくべき用語があります。
<b>
段階的性能低下（グレースフル・デグラデーション）
</b>
という概念です。
</p>
<p>
段階的性能低下とは、複数のレイヤーやモジュールに機能を分散して構築する概念です。システムの一部で致命的なエラーが発生しても、一定レベルの可用性を継続して提供します。
</p>
<p>
Kubernetesには2つの段階的性能低下の方法があります。
</p>
<blockquote>
<b>
インフラの性能低下
</b>
：この性能低下方式は、ハードウェアやVMの予期せぬエラーに対処するため、複雑なアルゴリズムやソフトウェアに依存します。この方式を提供するために必要なKubernetes必須コンポーネントの高可用性確保方法を探求します。
<br>
<br>
<b>
アプリケーションの性能低下
</b>
：前述のマイクロサービスベストプラクティスの戦略に大きく依存しますが、ユーザーの成功を保証するためのいくつかのパターンが存在します。
</blockquote>
<p>
中核となるKubernetes戦略を使用して基盤インフラの障害を分離しつつ、アプリケーションの障害に備えたキャッシング、フェイルオーバー、ロールバックのメカニズムを構築し、Kubernetesコンポーネントの高可用性を確保しなければなりません。
</p>

<blockquote>
反脆弱性（アンチフラジャイル）
</blockquote>
<p>
<span>
「反脆弱性」とは、一言で言えば、外部からの混乱や圧力に対して、むしろ成果が向上する性質を指します。
</span>
</p>
<p>
<span>
Kubernetesシステムの複雑さに対処し、大規模なKubernetesを活用してシステムを維持するには、いくつかの核となる概念を理解する必要があります。
</span>
</p>
<blockquote>
1. 二重化（冗長化）
<br>
2. 障害シナリオを発生させ、それに対して対応・分析・探索・改善を行うこと。（NetflixのChaos Monkeyは、複雑なシステムの安定性をテストするための標準的かつ整理されたアプローチです https://github.com/Netflix/chaosmonkey ）
<br>
3. システムに適切なパターンを導入する。（リトライ、ロードバランシング、サーキットブレーカー、タイムアウト、ヘルスチェック、同時接続チェックは反脆弱性のための核となるパターンです。さらに高いレベルには、Istioなどのサービスメッシュがあります。 https://techcafe.tistory.com/133 ）
</blockquote>

<blockquote>
KubernetesのためのHAアプローチ
</blockquote>
<p>
KubernetesのHA構成には、etcdと管理ノードを結合したスタックマスター方式と、etcdと管理ノードを分離した方式があります。
</p>
<p>
Kubernetesのインストール手順は省略します。
</p>

<blockquote>
クラスターのライフサイクル
</blockquote>
<p>
アドミッションコントローラー、ワークロード、CRDを使用してクラスターを拡張する方法を見ていきましょう。
</p>

<p>
<b>
アドミッションコントローラー
</b>
</p>
<p>
アドミッションコントローラーは、Kubernetes APIサーバーの認証と認可が完了した後、Kubernetes APIサーバーへの呼び出しを傍受できます。
</p>
<p>
以下の2つのアドミッションコントローラーが特に重要です。
</p>
<blockquote>
<b>
MutatingAdmissionWebhook
</b>
は、クラスターが変形（Mutation）段階にある場合にのみ実行され、リクエストを連続的に変形するウェブフックを呼び出します。CREATE、DELETE、UPDATEといった操作の承認ロジックをユーザー定義し、ビジネスロジックをクラスターに組み込む際にこのコントローラーを使用します。StorageClassを使用してストレージプロビジョニングを自動化するなどのタスクを実行可能です。
<br>
<br>
<b>
ValidatingAdmissionWebhook
</b>
は、承認段階でアドミッションコントローラーが実行されます。クォータ増加を検証するウェブフックのように、「リクエストの妥当性」を検査するウェブフックを呼び出します。このコントローラーが呼び出すすべてのウェブフックは、元のオブジェクトを変形できないという点に留意する必要があります。
</blockquote>

<blockquote>
ワークロードAPI
</blockquote>
<p>
Kubernetesの初期には、Podとワークロードは、CPU、ネットワーキング、ストレージ、ライフサイクルイベントを共有するコンテナと密接に結合されていました。Kubernetesは、クラウドアプリケーションの「12 Factor App」を管理できるようにレプリケーション、デプロイメント、ラベルなどの概念を導入し、Kubernetes運用者がステートフルなワークロードを扱えるようにStatefulSetを導入しました。
</p>
<p>
時間が経つにつれ、Kubernetesのワークロード概念は細分化されました。
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
これらの多様な要素は、Kubernetesがワークロードのタイプを合理的に調整した結果ですが、残念ながらKubernetesコードベースのあちこちにAPIが分散してしまいました。この問題を解決するため、後方互換性の一部を犠牲にするような数ヶ月にわたる努力の末、すべてのコードをapps/v1 APIに統合できました。
</p>
<p>
統合プロセスにおける重要な決定事項は以下の通りです。
</p>
<blockquote>
<b>
デフォルトセレクター
</b>
：ラベルセレクターを指定しない場合、テンプレートラベルから抽出して自動生成したセレクターをデフォルト値として使用します。
<br>
<b>
不変セレクター
</b>
：セレクターの変更がDeploymentにとって有用な場合もありますが、セレクターを変形することはKubernetesの推奨事項と相反するため、KubernetesがオーケストレーションするカナリアリリースとPodラベルを付け替える方式に変更されました。
<br>
<b>
ローリングアップデート
</b>
：Kubernetesプログラマーからのリクエストにより、ローリングアップデートがデフォルトになりました。
<br>
<b>
ガベージコレクション
</b>
：1.9バージョンとapps/v1バージョンでは、ガベージコレクションがより攻撃的（積極的）になっています。DaemonSet、ReplicaSet、StatefulSet、Deploymentを削除すると、Podも削除されます。
</blockquote>

<blockquote>
カスタムリソース定義（CRD）
</blockquote>
<p>
カスタムリソースは、Kubernetes APIを拡張し、アドミッションコントローラーを補完します。運用中のKubernetesクラスターを改善するためにカスタムリソースを使用できます。
</p>
<p>
以下のような機能を適用できます。
</p>

<table>
<tbody>
<tr>
<td>
CRUD
</td>
<td>
新しいエンドポイントは、HTTPとkubectlを介したCRUD基本操作をサポートします。
</td>
</tr>
<tr>
<td>
Watch
</td>
<td>
新しいエンドポイントは、HTTPを介したKubernetes Watch操作をサポートします。
</td>
</tr>
<tr>
<td>
Discovery
</td>
<td>
kubectlやダッシュボードのようなクライアントは、自動的にリソースのリスト表示、表示、フィールド編集操作を提供します。
</td>
</tr>
<tr>
<td>
json-patch
</td>
<td>
新しいエンドポイントは、Content-Type: application/json-patch+json を使用したPATCHをサポートします。
</td>
</tr>
<tr>
<td>
merge-patch
</td>
<td>
新しいエンドポイントは、Content-Type: application/merge-patch+json を使用したPATCHをサポートします。
</td>
</tr>
<tr>
<td>
HTTPS
</td>
<td>
新しいエンドポイントはHTTPSを使用します。
</td>
</tr>
<tr>
<td>
Built-in Authentication
</td>
<td>
拡張機能へのアクセスは、認証のためにコアAPIサーバー（アグリゲーションレイヤー）を使用します。
</td>
</tr>
<tr>
<td>
Built-in Authorization
</td>
<td>
拡張機能へのアクセスは、コアAPIサーバーで使用される認可（RBACなど）を再利用できます。
</td>
</tr>
<tr>
<td>
Finalizers
</td>
<td>
外部のクリーンアップが完了するまで、拡張リソースの削除をブロックします。
</td>
</tr>
<tr>
<td>
Admission Webhooks
</td>
<td>
任意の作成/更新/削除操作中に、拡張リソースのデフォルト値を設定し、妥当性を検証します。
</td>
</tr>
<tr>
<td>
UI/CLI Display
</td>
<td>
Kubectlやダッシュボードで拡張リソースを表示できます。
</td>
</tr>
<tr>
<td>
Unset versus Empty
</td>
<td>
クライアントは、未設定のフィールドとゼロ値のフィールドを区別できます。
</td>
</tr>
<tr>
<td>
Client Libraries Generation
</td>
<td>
Kubernetesは汎用クライアントライブラリを提供しており、タイプ別のクライアントライブラリを生成するツールも提供しています。
</td>
</tr>
<tr>
<td>
Labels and annotations
</td>
<td>
ツールがコアリソースやカスタムリソースに対して編集方法を認識している、オブジェクト共通のメタデータです。
</td>
</tr>
</tbody>
</table>

## 参考資料
- [Kubernetes公式ドキュメント](https://kubernetes.io/docs/home/)