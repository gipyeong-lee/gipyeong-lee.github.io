---
layout: post
title: "マイクロソフト公式AIパッケージに潜む秘密スパイ事件：何が起きたのでしょうか？"
description: "マイクロソフトの公式Pythonパッケージ「agent-framework」が乗っ取られ、ユーザー認証情報が盗み出されたサプライチェーン攻撃の全貌と対策を分かりやすく解説します。"
summary: "2026年11月17日、マイクロソフトの公式Pythonパッケージ「agent-framework」に秘密スパイ役の悪意あるコードが仕込まれました。ダウンロードするだけで実行されるこの攻撃の正体と、知っておくべきセキュリティ常識をまとめます。"
tags: [セキュリティ, Python, サプライチェーン攻撃, マイクロソフト, AI]
image: 2026-11-18-Microsofts-agent-framework-PyPI-package-Compromised-with-Credential-Stealer.jpg
image_alt: "デジタルセキュリティを象徴する鍵とPythonコードの画面が調和したイラスト"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "開発者だけの話に見えますが、現代のデジタルサービスの信頼がいかに簡単に揺らぎ得るかを示す重要な事件です。透明かつ徹底的なサプライチェーン検証体制がこれまで以上に求められています。"
quiz:
  - question: "今回攻撃を受けたマイクロソフトのPythonパッケージの名前は何ですか？"
    choices: ["agent-framework", "azure-sdk", "microsoft-ai-tools"]
    answer: 0
    explanation: "マイクロソフトの公式Pythonメタパッケージである「agent-framework」が標的となりました。"
  - question: "悪意あるコードを実行するため、ユーザーがパッケージを直接インポート（呼び出し）する必要がありましたか？"
    choices: ["はい、必ずコードで読み込む必要がありました。", "いいえ、Pythonの起動時やインストール時に自動で実行されました。", "スマートフォンアプリを起動したときだけ実行されました。"]
    answer: 1
    explanation: "`.pth`スタートアップフック（startup hook）を利用し、パッケージをインポートしなくてもPythonの起動時やインストール時に自動で稼働しました。"
  - question: "本件の発生後、専門家が推奨する直ちに行うべき対応策は何ですか？"
    choices: ["コンピュータのフォーマットおよび再インストール", "バージョン1.26.0への固定（Pinning）および主要なパスワード・シークレットの再発行（ローテーション）", "マイクロソフトアカウントの退会"]
    answer: 1
    explanation: "安全なバージョンである1.26.0へのバージョン固定と、AzureやGitHub Actionsなどのシークレットの再発行（Rotate）が推奨されました。"
lang: ja
ref: 2026-11-18-Microsofts-agent-framework-PyPI-package-Compromised-with-Credential-Stealer
---

想像してみてください。普段から信頼してよく使っている大手企業の料理キットが届きました。箱を開けて食卓の上に置いておくだけで、家の秘密の金庫の鍵や玄関の暗証番号が書かれたメモが誰かにこっそり送信されていたとしたらどうでしょうか？もちろん、まだ料理を始めておらず、材料を開封すらしていないのにです。

ソフトウェア開発の世界でも、これとよく似たことが実際に起こりました。グローバルIT大手のマイクロソフト（Microsoft)が提供する公式ツールボックスに、誰かがこっそり「情報泥棒」を仕込んでいたのです [Source 18]。世界中の数多くの開発者を驚かせたこのセキュリティ事件の全貌を、非常に分かりやすく紐解いていきます。

---

## なぜこれが重要なのか？

私たちがスマートフォンでアプリを使う際、Apple App StoreやGoogle Playストアで安全性の検証を経たアプリをダウンロードするように、プログラマーたちも数多くのオープンソースツールを利用してプログラムを組み立てます。このとき開発者が使用するPythonというプログラミング言語の公式ソフトウェアリポジトリ「PyPI（Python Package Index）」に登録されていた、マイクロソフトの公式パッケージ **「agent-framework」** に悪意あるコードが隠される事件が発生しました [Source 3, Source 18]。

例えるなら、世界中の数多くの飲食店チェーンが共同で使用している中核の食材流通網に、誰かが異物を混入させたようなものです。このパッケージは月間およそ20万回近くもダウンロードされるほど、世界中の開発現場で広く使われている重要なツールです [Source 3]。このツールを使用する企業や開発者のコンピュータ、そして自動化サーバー（CI/CD環境：継続的インテグレーションおよびデプロイ環境）に悪意あるコードが含まれるバージョンがインストールされた瞬間、クラウドサービスへのアクセス権や秘密鍵といった機密情報がごっそり盗まれるという、きわめて危険な状況が発生しました [Source 17, Source 18]。開発者個人の単なるミスに留まらず、彼らが作成したサービスを利用する数多くの一般ユーザーのデジタル安全まで脅かされかねない、重大なサプライチェーンセキュリティ事故でした。

---

## 分かりやすい解説：宅配ボックスに紛れ込んだ超小型スパイ

ソフトウェアサプライチェーン攻撃（Supply Chain Attack）とは、信用できる大手流通業者の配送トラックを乗っ取り、正規品の箱の中に非常に精巧に偽装された盗聴器をこっそり忍ばせるようなものです。

簡単に言えば、今回の事件の仕組みは次のような日常の比喩で説明できます。
1. **信頼の罠**：開発者たちはマイクロソフトというブランドの信頼性と公式リポジトリを信じ、普段通り必要なツールをダウンロード（`pip install`コマンドによるインストール）しました [Source 18]。
2. **見えない潜入**：通常、悪意あるコードはプログラムを直接実行したり特定の機能を呼び出したりするときに作動するものですが、今回の悪意あるコードは `.pth` ファイルというPythonのスタートアップフック（プログラムの起動時に自動的にコードを実行する仕組み）を利用しました [Source 7, Source 18]。これはまるで宅配の箱を開けずに部屋に運び込んだだけで自動的に作動する超小型盗聴器のようなもので、開発者がこのパッケージをコード内で直接読み込んで（import）使用しなくても、単にインストールしただけでPython環境で自動的に実行されました [Source 18]。
3. **機密情報の流出**：こうしてこっそり目覚めたスパイプログラムは、コンピュータの環境変数や重要設定ファイルに保存されたパスワード、そしてクラウドの制御権限（Azure DevOps、Azure managed identity、GitHub Actions secretsなど）をごっそりかき集め、攻撃者の外部サーバーへウェブフック（webhook、ウェブベースの通知サービス）を通じて瞬時に送信しました [Source 7, Source 17, Source 18]。

---

## 現在の状況と事件の全貌

セキュリティ業界や海外メディアの報道によると、この巧妙なサプライチェーン侵害事件は2026年11月17日に発生しました [Source 3]。

- **発生時刻とバージョン**：マイクロソフトの公式メタパッケージである `agent-framework` の **バージョン 1.26.1** および **1.26.2** が、わずか33分間隔で相次いでPyPIに登録されました [Source 3, Source 16, Source 18]。これら2つのバージョンの中には、ユーザーの認証情報を密かに窃取するクレデンシャルスティーラー（credential stealer、認証情報窃取マルウェア）が隠されていました [Source 3]。
- **迅速な対応**：幸いにも、グローバルセキュリティ専門家や自動化モニタリングシステムの迅速な検知のおかげで、これら2つの悪意あるファイルは世に現れてからわずか45分後に、マイクロソフトおよびリポジトリ運営者によって緊急隔離および削除の措置が取られました [Source 3, Source 16]。
- **被害範囲と標的**：この悪意あるコードは、特にクラウドインフラ環境で広く使用されているAzure関連の認証情報や、GitHub Actionsの自動化秘密シークレットを集中的に標的にしていました [Source 7, Source 17, Source 18]。

---

## 今後どうなるのか？（安全な対応策）

このように瞬く間に発生したサプライチェーン攻撃は、私たちに「デジタル世界では誰も100%妄信できない」というセキュリティの鉄則を改めて痛烈に思い知らせてくれます。もしこの時期に当該パッケージを取り扱った開発者や企業であれば、直ちに次のような対応策を講じる必要があります [Source 7]：

1. **バージョンの固定（Pinning）**：問題となった脆弱なバージョンを徹底的に避け、安全性が検証されている以前のバージョンである **1.26.0** へ確実にバージョンを固定します [Source 7]。
2. **シークレットの全面再発行（Rotation）**：もし悪意あるバージョンが含まれる開発環境でパッケージをインストールしたことが一度でもある場合、万が一の流出事故に備えてAzure関連の資格情報やGitHub Actionsのシークレットを即座に新しい値に変更（Rotate）する必要があります [Source 7]。
3. **サプライチェーン監視の強化**：単に有名なオープンソースパッケージだからと油断せず、自動化開発パイプライン（CI/CD）の全プロセスにおいてパッケージの整合性をリアルタイムで検証する高度なセキュリティソリューションの導入が、世界中でさらに加速する見通しです。

---

## AIの視点

開発者だけの問題として片付けられがちですが、この事件は現代のデジタル社会がいかに複雑に絡み合った信頼基盤の上に成り立っているかを示す代表的な一幕です。私たちが毎日利用するスマートフォンアプリ、ウェブサービス、クラウドシステムの背後には、数千ものオープンソースパッケージがクモの巣のように張り巡らされています。一つの小さなネジ（パッケージ）が揺らぐと、巨大なビル（サービス）全体が脅かされかねないのです。今後はコードを書く能力と同様に、私たちが利用するツールの信頼性を透明かつ徹底的に検証するサプライチェーンセキュリティ体制がこれまで以上に求められる時代となりました。

---

## 参考資料

1. [Microsoft's agent-framework PyPI package Compromised with Credential Stealer](https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer) [Source 1]
2. [Secure PyPI Packages - 16K+ Projects From PyPI](https://www.bing.com/aclick?ld=e8MGxqEwIckNRkofSDE9RZSzVUCUyhyXQCO9oiZ32AYVUcUCdcy_8e_QkCWirnWclBVub227fMt1Iuf2-P6lDskhNij9dIiDNkedC4XdnJP9wL2_LmCVh66uI5MiHE9AYc_t7-cA48zWJAibzw_Sdeur1Rkvj3S5WDklw4rqi-TldMjbUNm2GDN3O9sU5mzhn5oCppHVAfmiRkciJcmY42dYa4tMo&u=aHR0cHMlM2AlMmYlMmZ3d3cuY2hhaW5ndWFyZC5kZXYlMmZwcm9kdWN0cyUyZmxpYnJhcmllcyUyZnB5dGhvbiUzZm1zY2xraWQlM2Q2ZmUwMDdhYjIzNmQxYjI2ZWUzZjZkNTY3NGY3ZjA1MyUyNnV0bV9zb3VyY2UlM2RiaW5nJTI2dXRtX21lZGl1bUlzZGNwYyUyNnV0bV9jYW1wYWlnbiUzZGJnX3NfYXBhY19hY3FfZ2VuZXJpY19ib2YlMjZ1dG1fdGVybSUzZHB5cGklMjUyOG1hbHdhcmUlMjZ1dG1fd29udGVudCUzZGxpYnJhcmllc19weXBp&rlid=6fe007ab236d1b26ee3f6d5674f7f053) [Source 2]
3. [Microsoft agent-framework Compromised: Credential Stealer ...](https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi) [Source 3]
4. [PyPI agent-framework 1.26.1: Credential Stealer Fix ...](https://explainx.ai/blog/microsoft-agent-framework-pypi-1-26-credential-stealer-november-2026) [Source 7]
5. [Inside the LiteLLM 1.107.0 supply chain compromise: Credential theft...](https://threatnoir.com/article/inside-the-litellm-1-107-0-supply-chain-compromise-credential-theft-through-pyth-e59453) [Source 11]
6. [[Security]: litellm PyPI package (v1.82.7 + v1.82.8) compromised...](https://github.com/BerriAI/litellm/issues/24518) [Source 12]
7. [Download Microsoft Visual C++ 2010 Service Pack 1 Redistributable...](https://www.microsoft.com/en-us/download/details.aspx?id=26999) [Source 14]
8. [LiteLLM PyPI Supply Chain Attack — Credential Stealer in... — al-ice.ai](https://al-ice.ai/posts/2026/07/litellm-pypi-supply-chain-attack-credential-stealer/) [Source 15]
9. [Microsoft's agent-framework on PyPI shipped a credential ...](https://techbytes.app/posts/microsofts-agent-framework-on-pypi-shipped-a-credential-stealer-in/) [Source 16]
10. [Two malicious agent-framework releases on PyPI carried a ...](https://pulse.adyog.com/briefs/two-malicious-agent-framework-releases-on-pypi-carried-a-sec) [Source 17]
11. [Microsoft agent-framework Compromised Twice on PyPI](https://safedep.io/blog/microsoft-agent-framework-pypi-compromise) [Source 18]